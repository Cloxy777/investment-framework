#!/usr/bin/env python3
"""Integration healthcheck — Stage 3 of scripts/TOKEN-OPTIMIZATION-PLAN.md.

Runs the 7 checks documented in .claude/commands/healthcheck.md and prints pass/fail JSON
per check. This script only *reports* status — deciding whether to stay silent, or to
open/update/close the `integration-healthcheck` GitHub issue, stays Claude's job at the
command layer (per the Stage 3 instructions: "this script just reports status, it doesn't
touch GitHub itself").

Checks 1 (Interactive Brokers `get_account_summary`) and 2 (GitHub `get_me`) can only be
made from inside a Claude session holding those MCP connectors — no standalone script can
call them (see scripts/TOKEN-OPTIMIZATION-PLAN.md finding #1). This script therefore takes
their already-performed pass/fail outcome as input (Claude calls the MCP tool, then reports
the outcome here) rather than guessing or skipping them. Checks 3-7 (yfinance, FRED, the
Telegram Bot API, the Telegram monitored channels, and the IBKR ticker CSV) are plain HTTP/
library calls this script performs itself.

Usage:
    python -m scripts.healthcheck --ibkr-result '{"passed": true, "detail": "..."}' \
                                   --github-result '{"passed": true, "detail": "..."}'
    python -m scripts.healthcheck --ibkr-result ibkr.json --github-result github.json --json

Hard requirement: never silently default a check's result. If check 1 or 2's result isn't
supplied, this script hard-fails naming exactly what's missing (per CLAUDE.md's "never
invent or estimate" rule) rather than reporting a guessed pass/fail.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

from scripts.scoring.common import MissingInputError, require

YFINANCE_TICKER = "AAPL"
FRED_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10"
TELEGRAM_GETME_URL = "https://api.telegram.org/bot{token}/getMe"
TELEGRAM_CHANNEL_URL = "https://t.me/s/{channel}"
IBKR_CSV_URL = "https://www.interactivebrokers.com/download/fracshare_stk.csv"
DEFAULT_TELEGRAM_WATCH_FILE = Path("portfolio/snapshots/telegram-watch.md")


def _result(name: str, passed: bool, detail: str) -> dict:
    return {"check": name, "passed": bool(passed), "detail": detail}


def _load_precomputed(raw: str | None, check_name: str) -> dict:
    """Parse a precomputed MCP-call result, supplied as inline JSON or a file path.

    Raises MissingInputError if not supplied — checks 1/2 cannot be performed by this
    script itself, so a missing result is an ambiguous input, not a "fail".
    """
    if raw is None:
        raise MissingInputError(
            f"Missing required input: '{check_name}' result — this check needs an MCP "
            "call only a Claude session can make; fetch it first and pass its outcome"
        )
    path = Path(raw)
    if path.is_file():
        raw = path.read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise MissingInputError(f"'{check_name}' result is not valid JSON: {exc}") from exc
    passed = require(data, "passed", f"{check_name} result")
    detail = data.get("detail", "")
    return _result(check_name, bool(passed), str(detail))


def check_ibkr(raw: str | None) -> dict:
    return _load_precomputed(raw, "ibkr")


def check_github(raw: str | None) -> dict:
    return _load_precomputed(raw, "github")


def _default_yfinance_fetch(ticker_symbol: str):
    import yfinance as yf

    return yf.Ticker(ticker_symbol).fast_info["last_price"]


def check_yfinance(ticker_symbol: str = YFINANCE_TICKER, fetch=None) -> dict:
    fetch = fetch or _default_yfinance_fetch
    try:
        price = fetch(ticker_symbol)
    except Exception as exc:  # pragma: no cover - network/dependency failure path
        return _result("yfinance", False, f"exception fetching {ticker_symbol}: {exc}")
    if price is None:
        return _result("yfinance", False, f"fast_info['last_price'] for {ticker_symbol} was None")
    try:
        price = float(price)
    except (TypeError, ValueError):
        return _result("yfinance", False, f"non-numeric price returned: {price!r}")
    return _result("yfinance", True, f"{ticker_symbol} last_price={price}")


def _default_url_fetch(url: str, timeout: float = 10.0) -> str:
    with urllib.request.urlopen(url, timeout=timeout) as resp:  # noqa: S310 - fixed, documented URLs
        return resp.read().decode("utf-8", errors="replace")


def check_fred(fetch=None) -> dict:
    fetch = fetch or _default_url_fetch
    try:
        body = fetch(FRED_URL)
    except Exception as exc:  # pragma: no cover - network failure path
        return _result("fred", False, f"exception fetching FRED CSV: {exc}")
    lines = [ln for ln in body.strip().splitlines() if ln.strip()]
    if len(lines) < 2:
        return _result("fred", False, "FRED CSV had no data rows")
    last_row = lines[-1]
    parts = last_row.split(",")
    if len(parts) < 2 or not parts[1].strip() or parts[1].strip() == ".":
        return _result("fred", False, f"most recent row has a blank/missing value: {last_row!r}")
    return _result("fred", True, f"most recent DGS10 row: {last_row}")


def check_telegram_bot(token: str | None, fetch=None) -> dict:
    fetch = fetch or _default_url_fetch
    if not token:
        raise MissingInputError("Missing required input: TELEGRAM_BOT_TOKEN environment variable")
    url = TELEGRAM_GETME_URL.format(token=token)
    try:
        body = fetch(url)
    except Exception as exc:  # pragma: no cover - network failure path
        return _result("telegram_bot", False, f"exception calling getMe: {exc}")
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return _result("telegram_bot", False, f"non-JSON response: {body[:200]!r}")
    if not data.get("ok"):
        return _result("telegram_bot", False, f"getMe returned ok=false: {data}")
    return _result("telegram_bot", True, f"bot username={data.get('result', {}).get('username')}")


def _parse_channels(watch_file_text: str) -> list[str]:
    """Extract the monitored-channel list from the "## Monitored channels" table only.

    The rest of the file (the "## Mention log" section) is a long running log whose prose
    incidentally mentions other t.me/ links (quoted posts, cross-references, etc.) — scanning
    the whole file for "t.me/" substrings picks those up too. Restricting to the Monitored
    channels section's own table matches what healthcheck.md actually documents ("for each
    channel listed in portfolio/snapshots/telegram-watch.md ... currently t.me/tarasguk, ...").
    """
    lines = watch_file_text.splitlines()
    section_lines = []
    in_section = False
    for line in lines:
        if line.strip().startswith("## "):
            in_section = line.strip().lower() == "## monitored channels"
            continue
        if in_section:
            section_lines.append(line)

    channels = []
    for line in section_lines:
        if "t.me/" not in line or not line.strip().startswith("|"):
            continue
        cell = line.split("|")[1].strip()
        if "t.me/" not in cell:
            continue
        channel = cell.split("t.me/", 1)[1].strip(").,`*[] ")
        if channel and channel not in channels:
            channels.append(channel)
    return channels


def check_telegram_channels(watch_file: Path = DEFAULT_TELEGRAM_WATCH_FILE, fetch_status=None) -> dict:
    if not watch_file.is_file():
        raise MissingInputError(f"Telegram watch file not found: {watch_file}")
    channels = _parse_channels(watch_file.read_text(encoding="utf-8"))
    if not channels:
        raise MissingInputError(f"No 't.me/<channel>' entries found in {watch_file}")

    def default_fetch_status(channel: str) -> int:
        req = urllib.request.Request(TELEGRAM_CHANNEL_URL.format(channel=channel), method="HEAD")
        with urllib.request.urlopen(req, timeout=10.0) as resp:  # noqa: S310
            return resp.status

    fetch_status = fetch_status or default_fetch_status
    statuses = {}
    for channel in channels:
        try:
            statuses[channel] = fetch_status(channel)
        except urllib.error.HTTPError as exc:
            statuses[channel] = exc.code
        except Exception as exc:  # pragma: no cover - network failure path
            statuses[channel] = f"error: {exc}"

    failing = {c: s for c, s in statuses.items() if s != 200}
    passed = not failing
    detail = ", ".join(f"{c}={s}" for c, s in statuses.items())
    return _result("telegram_channels", passed, detail)


def check_ibkr_csv(fetch=None) -> dict:
    fetch = fetch or _default_url_fetch
    try:
        body = fetch(IBKR_CSV_URL)
    except Exception as exc:  # pragma: no cover - network failure path
        return _result("ibkr_ticker_csv", False, f"exception fetching CSV: {exc}")
    if not body.strip():
        return _result("ibkr_ticker_csv", False, "empty response")
    first_line = body.strip().splitlines()[0]
    if not first_line.startswith("#SYMBOL"):
        return _result("ibkr_ticker_csv", False, f"unexpected header row: {first_line!r}")
    return _result("ibkr_ticker_csv", True, f"header OK: {first_line}")


def run_all(
    ibkr_raw: str | None,
    github_raw: str | None,
    *,
    telegram_watch_file: Path = DEFAULT_TELEGRAM_WATCH_FILE,
    telegram_token: str | None = None,
    yfinance_fetch=None,
    fred_fetch=None,
    telegram_bot_fetch=None,
    telegram_channel_fetch_status=None,
    ibkr_csv_fetch=None,
) -> list[dict]:
    return [
        check_ibkr(ibkr_raw),
        check_github(github_raw),
        check_yfinance(fetch=yfinance_fetch),
        check_fred(fetch=fred_fetch),
        check_telegram_bot(telegram_token, fetch=telegram_bot_fetch),
        check_telegram_channels(telegram_watch_file, fetch_status=telegram_channel_fetch_status),
        check_ibkr_csv(fetch=ibkr_csv_fetch),
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--ibkr-result", help="Inline JSON or path to a file: {\"passed\": bool, \"detail\": str}")
    parser.add_argument("--github-result", help="Inline JSON or path to a file: {\"passed\": bool, \"detail\": str}")
    parser.add_argument(
        "--telegram-watch-file",
        default=str(DEFAULT_TELEGRAM_WATCH_FILE),
        help="Path to the file listing monitored t.me/<channel> entries",
    )
    args = parser.parse_args(argv)

    token = os.environ.get("TELEGRAM_BOT_TOKEN")

    try:
        results = run_all(
            args.ibkr_result,
            args.github_result,
            telegram_watch_file=Path(args.telegram_watch_file),
            telegram_token=token,
        )
    except MissingInputError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(results, indent=2))
    return 0 if all(r["passed"] for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())

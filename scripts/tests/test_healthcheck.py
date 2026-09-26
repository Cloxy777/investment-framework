import json

import pytest

from scripts.healthcheck import (
    check_fred,
    check_github,
    check_ibkr,
    check_ibkr_csv,
    check_telegram_bot,
    check_telegram_channels,
    check_yfinance,
    run_all,
)
from scripts.scoring.common import MissingInputError

GOOD_IBKR = json.dumps({"passed": True, "detail": "account U19421206 data returned"})
BAD_IBKR = json.dumps({"passed": False, "detail": "auth/connection error"})
GOOD_GITHUB = json.dumps({"passed": True, "detail": "authenticated as cloxy777"})


def test_ibkr_precomputed_pass():
    assert check_ibkr(GOOD_IBKR) == {"check": "ibkr", "passed": True, "detail": "account U19421206 data returned"}


def test_ibkr_precomputed_fail():
    result = check_ibkr(BAD_IBKR)
    assert result["passed"] is False


def test_ibkr_missing_input_hard_fails():
    with pytest.raises(MissingInputError, match="ibkr"):
        check_ibkr(None)


def test_github_missing_input_hard_fails():
    with pytest.raises(MissingInputError, match="github"):
        check_github(None)


def test_yfinance_known_good_fixture():
    result = check_yfinance(fetch=lambda ticker: 227.45)
    assert result == {"check": "yfinance", "passed": True, "detail": "AAPL last_price=227.45"}


def test_yfinance_known_bad_fixture_none_price():
    result = check_yfinance(fetch=lambda ticker: None)
    assert result["passed"] is False


def test_yfinance_known_bad_fixture_exception():
    def raise_timeout(ticker):
        raise TimeoutError("connection timed out")

    result = check_yfinance(fetch=raise_timeout)
    assert result["passed"] is False
    assert "connection timed out" in result["detail"]


def test_fred_known_good_fixture():
    csv = "DATE,DGS10\n2026-09-24,4.12\n2026-09-25,4.15\n"
    result = check_fred(fetch=lambda url: csv)
    assert result["passed"] is True


def test_fred_known_bad_fixture_blank_value():
    csv = "DATE,DGS10\n2026-09-24,4.12\n2026-09-25,.\n"
    result = check_fred(fetch=lambda url: csv)
    assert result["passed"] is False


def test_fred_known_bad_fixture_wrong_url_times_out():
    def raise_conn_error(url):
        raise ConnectionError("wrong URL / unreachable")

    result = check_fred(fetch=raise_conn_error)
    assert result["passed"] is False


def test_telegram_bot_known_good_fixture():
    result = check_telegram_bot("fake-token", fetch=lambda url: json.dumps({"ok": True, "result": {"username": "bot"}}))
    assert result["passed"] is True


def test_telegram_bot_known_bad_fixture():
    result = check_telegram_bot("fake-token", fetch=lambda url: json.dumps({"ok": False}))
    assert result["passed"] is False


def test_telegram_bot_missing_token_hard_fails():
    with pytest.raises(MissingInputError, match="TELEGRAM_BOT_TOKEN"):
        check_telegram_bot(None)


def _watch_file_text(*channels: str) -> str:
    rows = "\n".join(f"| https://t.me/{c} | ... | ... |" for c in channels)
    return (
        "# Telegram Stock-Mention Watch\n\n## Monitored channels\n\n"
        f"| Channel | Last-seen post (UTC) | Last checked |\n|---|---|---|\n{rows}\n\n"
        "## Mention log\n\nsome prose mentioning https://t.me/unrelated-channel should be ignored\n"
    )


def test_telegram_channels_known_good_fixture(tmp_path):
    watch_file = tmp_path / "telegram-watch.md"
    watch_file.write_text(_watch_file_text("tarasguk", "FinnInvestChannel"))
    result = check_telegram_channels(watch_file, fetch_status=lambda channel: 200)
    assert result["passed"] is True


def test_telegram_channels_ignores_mention_log_prose(tmp_path):
    watch_file = tmp_path / "telegram-watch.md"
    watch_file.write_text(_watch_file_text("tarasguk"))
    seen = []
    check_telegram_channels(watch_file, fetch_status=lambda c: seen.append(c) or 200)
    assert seen == ["tarasguk"]  # "unrelated-channel" from the Mention log prose must not appear


def test_telegram_channels_known_bad_fixture(tmp_path):
    watch_file = tmp_path / "telegram-watch.md"
    watch_file.write_text(_watch_file_text("tarasguk", "deadchannel"))

    def fetch_status(channel):
        return 200 if channel == "tarasguk" else 404

    result = check_telegram_channels(watch_file, fetch_status=fetch_status)
    assert result["passed"] is False
    assert "deadchannel=404" in result["detail"]


def test_telegram_channels_missing_file_hard_fails(tmp_path):
    with pytest.raises(MissingInputError):
        check_telegram_channels(tmp_path / "nope.md")


def test_ibkr_csv_known_good_fixture():
    csv = "#SYMBOL,MAIN_EXCHANGE,DESCRIPTION,IB_CONTRACT_ID,SCHEDULED_INELIGIBILTY_DATE\nAAPL,NASDAQ,Apple,265598,\n"
    result = check_ibkr_csv(fetch=lambda url: csv)
    assert result["passed"] is True


def test_ibkr_csv_known_bad_fixture_wrong_header():
    csv = "SYMBOL,EXCHANGE\nAAPL,NASDAQ\n"
    result = check_ibkr_csv(fetch=lambda url: csv)
    assert result["passed"] is False


def test_run_all_seven_checks(tmp_path):
    watch_file = tmp_path / "telegram-watch.md"
    watch_file.write_text(_watch_file_text("tarasguk"))
    results = run_all(
        GOOD_IBKR,
        GOOD_GITHUB,
        telegram_watch_file=watch_file,
        telegram_token="fake-token",
        yfinance_fetch=lambda t: 227.45,
        fred_fetch=lambda url: "DATE,DGS10\n2026-09-25,4.15\n",
        telegram_bot_fetch=lambda url: json.dumps({"ok": True, "result": {"username": "bot"}}),
        telegram_channel_fetch_status=lambda c: 200,
        ibkr_csv_fetch=lambda url: "#SYMBOL,X\nAAPL,X\n",
    )
    assert len(results) == 7
    assert all(r["passed"] for r in results)


def test_run_all_reports_mixed_failures(tmp_path):
    watch_file = tmp_path / "telegram-watch.md"
    watch_file.write_text(_watch_file_text("tarasguk"))
    results = run_all(
        BAD_IBKR,
        GOOD_GITHUB,
        telegram_watch_file=watch_file,
        telegram_token="fake-token",
        yfinance_fetch=lambda t: 227.45,
        fred_fetch=lambda url: "DATE,DGS10\n2026-09-25,4.15\n",
        telegram_bot_fetch=lambda url: json.dumps({"ok": True, "result": {"username": "bot"}}),
        telegram_channel_fetch_status=lambda c: 200,
        ibkr_csv_fetch=lambda url: "#SYMBOL,X\nAAPL,X\n",
    )
    by_check = {r["check"]: r["passed"] for r in results}
    assert by_check["ibkr"] is False
    assert by_check["github"] is True

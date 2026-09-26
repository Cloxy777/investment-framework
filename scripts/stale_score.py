#!/usr/bin/env python3
"""Watchlist stale-score mechanics — Stage 4 of scripts/TOKEN-OPTIMIZATION-PLAN.md.

Implements the general, repeatable "stale score" mechanism documented in
watchlist/README.md#stale-scores--when-the-scoring-methodology-changes and
CLAUDE.md's "Iterating on the framework itself" section: when the scoring
methodology version (a date stamped at the top of framework/valuation-scoring.md)
is bumped, every watchlist entry carrying a *numeric* score computed under an
older version is flagged with a `⚠️ STALE SCORE` banner in its entry file and a
row in the central registry watchlist/STALE.md. The mark clears automatically
once /rescore or /new-position brings that ticker current.

Per-ticker "current" state: a ticker's watchlist directory
(watchlist/{in-portfolio,not-in-portfolio}/<TICKER>/) can hold several dated
files (<TICKER>-YYYY-MM-DD.md) side by side — this repo keeps every dated file
live rather than replacing it in place (see the PR description for why this is
flagged as a drift from the literal README wording, "one file per ticker, most
of the time"). This script always treats the file with the *latest* filename
date as the ticker's current state; older dated files are historical snapshots
and are not touched.

Two operations, both centered on one "target" methodology version (the current
declared version by default, or an explicit --version to simulate/apply a bump):

- Newly stale: a ticker's current entry has a real numeric score dated before
  the target version and does not yet carry a banner naming that version.
- Resolvable: a ticker's current entry carries a banner naming the target
  version but is now dated on/after it (i.e. it's been rescored) — the banner
  and its STALE.md row are stale bookkeeping and should be cleared.

--check reports both sets without writing anything. --apply writes: inserts
banners (given an explicit, non-invented --reason) for newly-stale entries,
strips the named banner from resolvable entries, and updates a machine-owned
block in watchlist/STALE.md (see STALE_BLOCK_BEGIN/END below) — the rest of
that file's hand-written narrative sections are left untouched (see the PR
description for why this script does not attempt to regenerate the file's
full prose structure).

Hard requirement (same as Stages 1-3): never silently default, zero-fill, or
guess on missing/ambiguous input — hard-fail naming exactly what's missing.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from scripts.scoring.common import MissingInputError

DEFAULT_VALUATION_SCORING = Path("framework/valuation-scoring.md")
DEFAULT_WATCHLIST_ROOT = Path("watchlist")
DEFAULT_STALE_MD = Path("watchlist/STALE.md")
SECTIONS = ("in-portfolio", "not-in-portfolio")

VERSION_RE = re.compile(r"Scoring methodology version:\s*(\d{4}-\d{2}-\d{2})")
FILENAME_RE = re.compile(r"^(?P<ticker>.+)-(?P<date>\d{4}-\d{2}-\d{2})\.md$")
ROW_DATE_RE = re.compile(r"^\|\s*\**(\d{4}-\d{2}-\d{2})")
BANNER_VERSION_RE = re.compile(r"predates the (\d{4}-\d{2}-\d{2}) scoring-methodology change")
NOT_SCORED_MARKERS = ("phase 01 fail", "not scored")

STALE_BLOCK_BEGIN = "<!-- stale-score:auto version={version} -->"
STALE_BLOCK_END = "<!-- /stale-score:auto -->"


class StaleScoreDataError(MissingInputError):
    """Watchlist file structure doesn't match what this script expects to parse."""


@dataclass(frozen=True)
class Entry:
    ticker: str
    section: str
    path: Path
    entry_date: str
    is_scored: bool
    banner_versions: tuple[str, ...]
    filename_date: str
    filename_mismatch: bool


def read_current_version(path: Path = DEFAULT_VALUATION_SCORING) -> str:
    if not path.is_file():
        raise MissingInputError(f"Scoring methodology file not found: {path}")
    text = path.read_text(encoding="utf-8")
    match = VERSION_RE.search(text)
    if not match:
        raise MissingInputError(
            f"Could not find 'Scoring methodology version: YYYY-MM-DD' stamp in {path}"
        )
    return match.group(1)


def _latest_file_for_ticker(ticker_dir: Path) -> Path:
    candidates = []
    for f in sorted(ticker_dir.glob("*.md")):
        m = FILENAME_RE.match(f.name)
        if not m:
            raise StaleScoreDataError(
                f"Unrecognized watchlist filename (expected TICKER-YYYY-MM-DD.md): {f}"
            )
        if m.group("ticker") != ticker_dir.name:
            raise StaleScoreDataError(
                f"Filename ticker prefix '{m.group('ticker')}' does not match "
                f"directory name '{ticker_dir.name}': {f}"
            )
        candidates.append((m.group("date"), f))
    if not candidates:
        raise StaleScoreDataError(f"No dated watchlist files found in {ticker_dir}")
    candidates.sort(key=lambda pair: pair[0])
    return candidates[-1][1]


def _parse_latest_row(path: Path) -> tuple[str, bool, str, bool]:
    """Return (entry_date, is_scored, filename_date, filename_mismatch).

    entry_date is the *maximum* date found among the table's own data rows —
    not simply "the first row" — because table row order is not consistent
    across this repo: most files list newest-first (e.g. NOW, ADBE), but a
    backfilled file can list oldest-first (e.g. ABNB-2026-08-24.md, whose own
    banner explains it starts with a 2026-06-07 backfilled row followed by the
    2026-08-24 current one). Picking the max date is order-independent and
    matches what "most recent" actually means.

    filename_mismatch flags a second, independent drift found live in this
    repo: watchlist/in-portfolio/NKE/NKE-2026-07-01.md's most recent row is
    dated 2026-09-11 — a rescore appended a new top row to the existing dated
    file instead of creating a fresh TICKER-YYYY-MM-DD.md, so the filename no
    longer matches the table's own most recent date. Surfaced rather than
    hard-failed, since crashing on one ticker's naming drift would block
    staleness checking for every other ticker too — see the PR description.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    header_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("| Date |"):
            header_idx = i
            break
    if header_idx is None:
        raise StaleScoreDataError(f"No '| Date | ...' table header found in {path}")
    # header, then a '|---|...' separator, then data rows until a non-'|' line.
    if header_idx + 2 >= len(lines):
        raise StaleScoreDataError(f"Table in {path} has no data rows")
    rows = []
    for line in lines[header_idx + 2 :]:
        if not line.strip().startswith("|"):
            break
        rows.append(line)
    if not rows:
        raise StaleScoreDataError(f"Table in {path} has no data rows")

    dated_rows = []
    for row in rows:
        m = ROW_DATE_RE.match(row)
        if not m:
            raise StaleScoreDataError(f"Could not parse a date from a table row in {path}: {row!r}")
        dated_rows.append((m.group(1), row))
    entry_date, latest_row = max(dated_rows, key=lambda pair: pair[0])

    filename_date = FILENAME_RE.match(path.name).group("date")
    # Strip markdown emphasis before matching — e.g. "Phase 01 **FAIL**" would otherwise
    # dodge a plain "phase 01 fail" substring check (real example: HY9H-2026-06-20.md,
    # which also computes a Phase 02 number "for documentation" alongside the FAIL —
    # per STALE.md's own notes that's still not a binding score, so it must not count
    # as scored here either).
    cleaned_row = re.sub(r"\*+", "", latest_row).lower()
    is_scored = not any(marker in cleaned_row for marker in NOT_SCORED_MARKERS)
    return entry_date, is_scored, filename_date, entry_date != filename_date


def _banner_versions(path: Path) -> tuple[str, ...]:
    head = "\n".join(path.read_text(encoding="utf-8").splitlines()[:12])
    return tuple(BANNER_VERSION_RE.findall(head))


def discover_entries(watchlist_root: Path = DEFAULT_WATCHLIST_ROOT) -> list[Entry]:
    entries: list[Entry] = []
    for section in SECTIONS:
        section_dir = watchlist_root / section
        if not section_dir.is_dir():
            continue
        for ticker_dir in sorted(p for p in section_dir.iterdir() if p.is_dir()):
            latest = _latest_file_for_ticker(ticker_dir)
            entry_date, is_scored, filename_date, mismatch = _parse_latest_row(latest)
            entries.append(
                Entry(
                    ticker=ticker_dir.name,
                    section=section,
                    path=latest,
                    entry_date=entry_date,
                    is_scored=is_scored,
                    banner_versions=_banner_versions(latest),
                    filename_date=filename_date,
                    filename_mismatch=mismatch,
                )
            )
    return entries


def find_newly_stale(entries: list[Entry], version: str) -> list[Entry]:
    return [
        e
        for e in entries
        if e.is_scored and e.entry_date < version and version not in e.banner_versions
    ]


def find_resolvable(entries: list[Entry], version: str) -> list[Entry]:
    return [e for e in entries if version in e.banner_versions and e.entry_date >= version]


def _build_banner(version: str, reason: str, decision_link: str | None) -> str:
    reason_link = f"([{reason}]({decision_link}))" if decision_link else f"({reason})"
    return (
        f"> ⚠️ **STALE SCORE** — this entry predates the {version} scoring-methodology "
        f"change {reason_link} and is not comparable to current scores. Pending rescore — "
        "see the [staleness registry](../../STALE.md) (path relative to a ticker's entry "
        "file — adjust if nesting differs). _Remove this banner when the ticker is "
        "rescored under the current methodology._"
    )


def _insert_banner(path: Path, banner: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        raise StaleScoreDataError(f"{path} is empty — cannot insert a banner")
    title = lines[0]
    rest = lines[1:]
    while rest and rest[0].strip() == "":
        rest = rest[1:]
    new_lines = [title, "", banner, "", *rest]
    path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


def _remove_banner(path: Path, version: str) -> None:
    lines = path.read_text(encoding="utf-8").splitlines()
    out = []
    skip_blank_before = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("> ⚠️ **STALE SCORE") and f"predates the {version}" in line:
            i += 1
            # also drop one following blank line to avoid a double-blank gap
            if i < len(lines) and lines[i].strip() == "":
                i += 1
            continue
        out.append(line)
        i += 1
    path.write_text("\n".join(out) + "\n", encoding="utf-8")


def _update_stale_md(
    stale_md: Path,
    version: str,
    newly_stale: list[Entry],
    resolvable: list[Entry],
) -> None:
    if not stale_md.is_file():
        raise MissingInputError(f"{stale_md} not found — cannot maintain the stale-score registry")
    text = stale_md.read_text(encoding="utf-8")
    begin = STALE_BLOCK_BEGIN.format(version=version)
    end = STALE_BLOCK_END

    resolved_tickers = {e.ticker for e in resolvable}
    existing_rows: list[str] = []
    if begin in text:
        block = text.split(begin, 1)[1].split(end, 1)[0]
        for line in block.strip().splitlines():
            if not line.strip().startswith("|") or line.strip().startswith("|--"):
                continue
            ticker = line.split("|")[1].strip()
            if ticker and ticker not in resolved_tickers:
                existing_rows.append(line.rstrip())

    new_rows = [
        f"| {e.ticker} | {e.section}/{e.ticker}/{e.path.name} | {e.entry_date} |"
        for e in newly_stale
        if e.ticker not in {r.split("|")[1].strip() for r in existing_rows}
    ]
    all_rows = existing_rows + new_rows

    block_lines = [begin]
    if all_rows:
        block_lines.append("| Ticker | Location | Scored (date) |")
        block_lines.append("|--------|----------|----------------|")
        block_lines.extend(all_rows)
    block_lines.append(end)
    block_text = "\n".join(block_lines)

    if begin in text:
        prefix, remainder = text.split(begin, 1)
        _, suffix = remainder.split(end, 1)
        new_text = prefix + block_text + suffix
    else:
        new_text = text.rstrip("\n") + "\n\n" + block_text + "\n"

    stale_md.write_text(new_text, encoding="utf-8")


def check(
    version: str,
    watchlist_root: Path = DEFAULT_WATCHLIST_ROOT,
) -> dict:
    entries = discover_entries(watchlist_root)
    newly_stale = find_newly_stale(entries, version)
    resolvable = find_resolvable(entries, version)
    mismatches = [e for e in entries if e.filename_mismatch]
    return {
        "version": version,
        "newly_stale": [{"ticker": e.ticker, "path": str(e.path), "entry_date": e.entry_date} for e in newly_stale],
        "resolvable": [{"ticker": e.ticker, "path": str(e.path), "entry_date": e.entry_date} for e in resolvable],
        "filename_mismatches": [
            {"ticker": e.ticker, "path": str(e.path), "filename_date": e.filename_date, "entry_date": e.entry_date}
            for e in mismatches
        ],
    }


def apply(
    version: str,
    reason: str | None,
    decision_link: str | None = None,
    watchlist_root: Path = DEFAULT_WATCHLIST_ROOT,
    stale_md: Path = DEFAULT_STALE_MD,
) -> dict:
    entries = discover_entries(watchlist_root)
    newly_stale = find_newly_stale(entries, version)
    resolvable = find_resolvable(entries, version)

    if newly_stale and not reason:
        raise MissingInputError(
            "Missing required input: 'reason' — inserting a STALE SCORE banner requires "
            "an explicit, human-supplied description of what changed (never invented); "
            "pass --reason"
        )

    for e in newly_stale:
        _insert_banner(e.path, _build_banner(version, reason, decision_link))
    for e in resolvable:
        _remove_banner(e.path, version)

    _update_stale_md(stale_md, version, newly_stale, resolvable)

    return {
        "version": version,
        "newly_stale": [e.ticker for e in newly_stale],
        "resolved": [e.ticker for e in resolvable],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="Report only, no writes (default if --apply not given)")
    parser.add_argument("--apply", action="store_true", help="Actually insert/remove banners and update STALE.md")
    parser.add_argument(
        "--version",
        help="Target methodology version (YYYY-MM-DD). Defaults to the version currently "
        "declared at the top of framework/valuation-scoring.md.",
    )
    parser.add_argument("--reason", help="Human-supplied reason text for a new STALE SCORE banner (required if --apply inserts any)")
    parser.add_argument("--decision-link", help="Relative link to the decisions/ file explaining the version bump")
    parser.add_argument("--valuation-scoring", default=str(DEFAULT_VALUATION_SCORING))
    parser.add_argument("--watchlist-root", default=str(DEFAULT_WATCHLIST_ROOT))
    parser.add_argument("--stale-md", default=str(DEFAULT_STALE_MD))
    args = parser.parse_args(argv)

    if args.apply and args.check:
        print("ERROR: pass either --check or --apply, not both", file=sys.stderr)
        return 2

    try:
        version = args.version or read_current_version(Path(args.valuation_scoring))
        if args.apply:
            result = apply(
                version,
                args.reason,
                decision_link=args.decision_link,
                watchlist_root=Path(args.watchlist_root),
                stale_md=Path(args.stale_md),
            )
        else:
            result = check(version, watchlist_root=Path(args.watchlist_root))
    except MissingInputError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(result, indent=2))
    if not args.apply and (result["newly_stale"] or result["resolvable"] or result.get("filename_mismatches")):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

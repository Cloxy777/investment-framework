from pathlib import Path

import pytest

from scripts.scoring.common import MissingInputError
from scripts.stale_score import (
    StaleScoreDataError,
    apply,
    check,
    discover_entries,
    find_newly_stale,
    find_resolvable,
    read_current_version,
)

REAL_VALUATION_SCORING = Path("framework/valuation-scoring.md")
REAL_WATCHLIST_ROOT = Path("watchlist")


def _write_ticker_file(dir_: Path, ticker: str, date: str, score_row_score: str = "42.3") -> Path:
    ticker_dir = dir_ / ticker
    ticker_dir.mkdir(parents=True, exist_ok=True)
    path = ticker_dir / f"{ticker}-{date}.md"
    path.write_text(
        f"# {ticker} — Test Co.\n\n"
        "**Sector:** Test\n"
        "**Status:** Not held\n\n"
        "| Date | Price | Score | Action (current Action Table) | Key Notes | Session |\n"
        "|---|---|---|---|---|---|\n"
        f"| {date} | $100.00 | {score_row_score} | HOLD | notes | [session](../../x.md) |\n",
        encoding="utf-8",
    )
    return path


def _write_not_scored_file(dir_: Path, ticker: str, date: str) -> Path:
    ticker_dir = dir_ / ticker
    ticker_dir.mkdir(parents=True, exist_ok=True)
    path = ticker_dir / f"{ticker}-{date}.md"
    path.write_text(
        f"# {ticker} — Test Co.\n\n"
        "**Sector:** Test\n"
        "**Status:** Not held\n\n"
        "| Date | Price | Score | Action (current Action Table) | Key Notes | Session |\n"
        "|---|---|---|---|---|---|\n"
        f"| {date} | $100.00 | Phase 01 FAIL | PASS | notes | [session](../../x.md) |\n",
        encoding="utf-8",
    )
    return path


@pytest.fixture
def watchlist_root(tmp_path):
    root = tmp_path / "watchlist"
    not_held = root / "not-in-portfolio"
    held = root / "in-portfolio"
    _write_ticker_file(not_held, "AAA", "2026-06-01", "10.0")
    _write_ticker_file(held, "BBB", "2026-06-15", "20.0")
    _write_not_scored_file(not_held, "CCC", "2026-06-01")
    stale_md = root / "STALE.md"
    stale_md.write_text(
        "# Stale-score registry\n\nSome hand-written narrative that must survive untouched.\n",
        encoding="utf-8",
    )
    return root


def test_read_current_version_from_real_file():
    version = read_current_version(REAL_VALUATION_SCORING)
    assert version == "2026-06-29"


def test_read_current_version_missing_file_hard_fails(tmp_path):
    with pytest.raises(MissingInputError):
        read_current_version(tmp_path / "nope.md")


def test_check_against_real_repo_is_clean():
    """Per the plan's own verification note: no version bump pending right now.

    filename_mismatches is deliberately not asserted empty here — see the PR
    description for a real, live one this test run surfaced (NKE).
    """
    version = read_current_version(REAL_VALUATION_SCORING)
    result = check(version, watchlist_root=REAL_WATCHLIST_ROOT)
    assert result["newly_stale"] == []
    assert result["resolvable"] == []


def test_discover_entries_picks_latest_dated_file_per_ticker(tmp_path):
    root = tmp_path / "watchlist"
    not_held = root / "not-in-portfolio"
    _write_ticker_file(not_held, "AAA", "2026-06-01", "10.0")
    _write_ticker_file(not_held, "AAA", "2026-07-01", "15.0")
    entries = discover_entries(root)
    assert len(entries) == 1
    assert entries[0].entry_date == "2026-07-01"


def test_newly_stale_flags_entries_predating_a_simulated_bump(watchlist_root):
    entries = discover_entries(watchlist_root)
    stale = find_newly_stale(entries, "2026-07-01")
    stale_tickers = {e.ticker for e in stale}
    assert stale_tickers == {"AAA", "BBB"}  # both dated before 2026-07-01, both scored
    assert "CCC" not in stale_tickers  # Phase 01 FAIL / not scored is excluded


def test_check_reports_expected_flags_for_simulated_bump(watchlist_root):
    result = check("2026-07-01", watchlist_root=watchlist_root)
    tickers = {r["ticker"] for r in result["newly_stale"]}
    assert tickers == {"AAA", "BBB"}
    assert result["resolvable"] == []


def test_apply_without_reason_hard_fails_when_insertion_needed(watchlist_root):
    with pytest.raises(MissingInputError, match="reason"):
        apply("2026-07-01", None, watchlist_root=watchlist_root, stale_md=watchlist_root / "STALE.md")


def test_apply_inserts_banners_and_populates_stale_md(watchlist_root):
    stale_md = watchlist_root / "STALE.md"
    result = apply(
        "2026-07-01",
        reason="Simulated methodology change for test purposes",
        watchlist_root=watchlist_root,
        stale_md=stale_md,
    )
    assert set(result["newly_stale"]) == {"AAA", "BBB"}

    aaa_file = watchlist_root / "not-in-portfolio" / "AAA" / "AAA-2026-06-01.md"
    bbb_file = watchlist_root / "in-portfolio" / "BBB" / "BBB-2026-06-15.md"
    ccc_file = watchlist_root / "not-in-portfolio" / "CCC" / "CCC-2026-06-01.md"

    assert "STALE SCORE" in aaa_file.read_text(encoding="utf-8")
    assert "predates the 2026-07-01" in aaa_file.read_text(encoding="utf-8")
    assert "STALE SCORE" in bbb_file.read_text(encoding="utf-8")
    assert "STALE SCORE" not in ccc_file.read_text(encoding="utf-8")  # not scored, never flagged

    stale_text = stale_md.read_text(encoding="utf-8")
    assert "AAA" in stale_text
    assert "BBB" in stale_text
    assert "Some hand-written narrative that must survive untouched." in stale_text


def test_second_check_after_rescore_clears_automatically(watchlist_root):
    stale_md = watchlist_root / "STALE.md"
    version = "2026-07-01"
    apply(version, reason="Simulated methodology change", watchlist_root=watchlist_root, stale_md=stale_md)

    # Simulate /rescore bringing AAA current: a fresh dated file under the new methodology.
    _write_ticker_file(watchlist_root / "not-in-portfolio", "AAA", "2026-07-10", "12.0")

    result = check(version, watchlist_root=watchlist_root)
    stale_tickers = {r["ticker"] for r in result["newly_stale"]}
    assert "AAA" not in stale_tickers  # now current, not flagged again

    resolvable_tickers = {r["ticker"] for r in result["resolvable"]}
    assert resolvable_tickers == set()  # AAA's new file carries no banner to begin with

    # BBB was never rescored — it already carries a banner from the first apply(), so a
    # second check reports no *new* delta for it (nothing left to insert or remove), but
    # it must still be present in the registry (not silently dropped).
    assert all(r["ticker"] != "BBB" for r in result["newly_stale"])
    assert "BBB" in stale_md.read_text(encoding="utf-8")
    bbb_file = watchlist_root / "in-portfolio" / "BBB" / "BBB-2026-06-15.md"
    assert bbb_file.read_text(encoding="utf-8").count("STALE SCORE") == 1  # not duplicated

    # Re-running apply is idempotent: no change for AAA (already current) or BBB (already flagged).
    apply(version, reason="Simulated methodology change", watchlist_root=watchlist_root, stale_md=stale_md)
    assert bbb_file.read_text(encoding="utf-8").count("STALE SCORE") == 1


def test_apply_removes_banner_once_entry_is_current_again(watchlist_root):
    stale_md = watchlist_root / "STALE.md"
    version = "2026-07-01"
    apply(version, reason="Simulated methodology change", watchlist_root=watchlist_root, stale_md=stale_md)

    bbb_dir = watchlist_root / "in-portfolio" / "BBB"
    old_banner_text = (bbb_dir / "BBB-2026-06-15.md").read_text(encoding="utf-8")
    assert "STALE SCORE" in old_banner_text

    # Simulate a rescore: the ticker's *current* file becomes a fresh one dated after the
    # version — but suppose (edge case) it still carries the old banner text on it too,
    # e.g. copy-pasted forward. apply() should strip a same-version banner once the entry
    # is current.
    new_file = _write_ticker_file(watchlist_root / "in-portfolio", "BBB", "2026-07-15", "25.0")
    banner_line = (
        f"> ⚠️ **STALE SCORE** — this entry predates the {version} scoring-methodology "
        "change (test) and is not comparable to current scores."
    )
    lines = new_file.read_text(encoding="utf-8").splitlines()
    new_file.write_text("\n".join([lines[0], "", banner_line, "", *lines[1:]]) + "\n", encoding="utf-8")

    result = apply(version, reason="Simulated methodology change", watchlist_root=watchlist_root, stale_md=stale_md)
    assert "BBB" in result["resolved"]
    assert "STALE SCORE" not in new_file.read_text(encoding="utf-8")


def test_unrecognized_filename_hard_fails(tmp_path):
    root = tmp_path / "watchlist"
    ticker_dir = root / "not-in-portfolio" / "AAA"
    ticker_dir.mkdir(parents=True)
    (ticker_dir / "notes.md").write_text("# stray file\n", encoding="utf-8")
    with pytest.raises(StaleScoreDataError):
        discover_entries(root)


def test_mismatched_filename_and_row_date_is_flagged_not_crashed(tmp_path):
    """Real repo example: watchlist/in-portfolio/NKE/NKE-2026-07-01.md's most recent row is
    dated 2026-09-11 — a rescore appended a new top row instead of creating a fresh dated
    file, drifting from README's documented convention. Surfaced as filename_mismatch
    rather than a hard failure, so one ticker's naming drift doesn't block staleness
    checking for every other ticker."""
    root = tmp_path / "watchlist"
    ticker_dir = root / "not-in-portfolio" / "AAA"
    ticker_dir.mkdir(parents=True)
    (ticker_dir / "AAA-2026-06-01.md").write_text(
        "# AAA\n\n| Date | Price | Score | Action | Notes | Session |\n|---|---|---|---|---|---|\n"
        "| 2026-06-02 | $1 | 10.0 | HOLD | n | [s](x.md) |\n",
        encoding="utf-8",
    )
    entries = discover_entries(root)
    assert len(entries) == 1
    assert entries[0].filename_mismatch is True
    assert entries[0].entry_date == "2026-06-02"
    assert entries[0].filename_date == "2026-06-01"

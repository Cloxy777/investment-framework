import pytest

from scripts.scoring.common import MissingInputError
from scripts.watchlist_diff import build_append_line, build_new_row, decide

# Score/category pairs below are drawn from real recorded watchlist entries:
# ADBE-2026-06-12.md (score 5.0, "BUY") -> ADBE-2026-06-20.md (score 0.0, "BUY")
# and the NOW watchlist history (score 61.3 on 2026-07-05).


def test_score_change_triggers_new_file():
    result = decide(5.0, "BUY", 0.0, "BUY")
    assert result["decision"] == "new_file"
    assert "score changed" in result["reason"]


def test_no_change_appends_no_new_file():
    result = decide(42.3, "BUY", 42.3, "BUY")
    assert result["decision"] == "append"
    assert result["reason"] == "no significant change"


def test_category_change_alone_triggers_new_file():
    result = decide(61.3, "HOLD", 61.3, "TRIM")
    assert result["decision"] == "new_file"
    assert "action category changed" in result["reason"]
    assert "HOLD -> TRIM" in result["reason"]


def test_fundamental_event_forces_new_file_even_without_score_or_category_change():
    # Mirrors ADBE-2026-07-29.md: score 0.0 -> 0.0, category BUY -> BUY unchanged,
    # but a Rule 9 investigation (the 19.5% price move) still produced a new dated file.
    result = decide(0.0, "BUY", 0.0, "BUY", fundamental_event=True)
    assert result["decision"] == "new_file"
    assert "Rule 9" in result["reason"]


def test_position_change_forces_new_file():
    result = decide(50.0, "HOLD", 50.0, "HOLD", position_change=True)
    assert result["decision"] == "new_file"
    assert "position" in result["reason"]


def test_not_scored_to_scored_crossing_is_a_score_change():
    result = decide("Phase 01 FAIL", "PASS", 31.0, "BUY")
    assert result["decision"] == "new_file"


def test_not_scored_sentinel_case_insensitive():
    result = decide("not scored", "PASS", "NOT SCORED", "PASS")
    assert result["decision"] == "append"


def test_unknown_category_hard_fails_rather_than_guessing():
    with pytest.raises(MissingInputError, match="known action categories"):
        decide(50.0, "BUY band (Standard 3-5%) on score", 50.0, "HOLD")


def test_missing_score_hard_fails():
    with pytest.raises(MissingInputError, match="old_score"):
        decide(None, "HOLD", 50.0, "HOLD")


def test_non_numeric_non_sentinel_score_hard_fails():
    with pytest.raises(MissingInputError, match="new_score"):
        decide(50.0, "HOLD", "roughly fifty", "HOLD")


def test_build_new_row_renders_all_fields():
    row = build_new_row(
        "2026-07-05", "$106.32", "61.3", "HOLD, watch only", "Score rose from 42.3", "../../../sessions/x.md"
    )
    assert row == "| 2026-07-05 | $106.32 | 61.3 | HOLD, watch only | Score rose from 42.3 | [session](../../../sessions/x.md) |"


def test_build_new_row_missing_field_hard_fails():
    with pytest.raises(MissingInputError, match="notes"):
        build_new_row("2026-07-05", "$106.32", "61.3", "HOLD", "", "../../../sessions/x.md")


def test_build_append_line():
    line = build_append_line("2026-08-01", "price move within Rule 9 threshold, no rescore")
    assert line == "**Last checked (no significant change):** 2026-08-01 — price move within Rule 9 threshold, no rescore"


def test_build_append_line_missing_note_hard_fails():
    with pytest.raises(MissingInputError, match="note"):
        build_append_line("2026-08-01", "")

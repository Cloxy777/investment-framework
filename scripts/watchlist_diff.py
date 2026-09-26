#!/usr/bin/env python3
"""Watchlist new-file-vs-append-line decision — Stage 4 of scripts/TOKEN-OPTIMIZATION-PLAN.md.

Implements the "Significant change" rule from watchlist/README.md: a new dated
file is created only when the valuation score changes (including crossing the
scored / "Phase 01 FAIL / not scored" boundary), the action category changes,
a Rule 9 fundamental-event trigger fires, or the position is opened/closed.
Otherwise the update is just a line appended to the existing file's
"Last checked (no significant change)" log — no new file.

Categories are passed in explicitly (not parsed out of free-form action prose)
because real action text is often compound and ambiguous (e.g. "BUY band ...
but no entry ... Hold existing") — guessing a category from prose would
violate the framework's no-invent-or-guess rule. Caller must classify the
action into one of the known categories itself.

Hard requirement: never silently default, zero-fill, or guess on missing/
ambiguous input — hard-fail naming exactly what's missing.
"""

from __future__ import annotations

import argparse
import json
import sys

from scripts.scoring.common import MissingInputError

KNOWN_CATEGORIES = {"PASS", "WATCHLIST", "BUY", "HOLD", "TRIM", "EXIT"}
NOT_SCORED_SENTINELS = {"PHASE 01 FAIL", "NOT SCORED"}


def normalize_score(raw, field_name: str):
    if raw is None or (isinstance(raw, str) and raw.strip() == ""):
        raise MissingInputError(f"Missing required input: '{field_name}'")
    if isinstance(raw, (int, float)):
        return float(raw)
    text = str(raw).strip()
    if text.upper() in NOT_SCORED_SENTINELS:
        return text.upper()
    try:
        return float(text)
    except ValueError as exc:
        raise MissingInputError(
            f"'{field_name}' is neither a number nor one of {sorted(NOT_SCORED_SENTINELS)}: {raw!r}"
        ) from exc


def normalize_category(raw, field_name: str) -> str:
    if raw is None or (isinstance(raw, str) and raw.strip() == ""):
        raise MissingInputError(f"Missing required input: '{field_name}'")
    text = str(raw).strip().upper()
    if text not in KNOWN_CATEGORIES:
        raise MissingInputError(
            f"'{field_name}' value {raw!r} is not one of the known action categories "
            f"{sorted(KNOWN_CATEGORIES)} — classify it first rather than passing raw action prose"
        )
    return text


def decide(
    old_score,
    old_category,
    new_score,
    new_category,
    *,
    fundamental_event: bool = False,
    position_change: bool = False,
) -> dict:
    old_score_n = normalize_score(old_score, "old_score")
    new_score_n = normalize_score(new_score, "new_score")
    old_category_n = normalize_category(old_category, "old_category")
    new_category_n = normalize_category(new_category, "new_category")

    if position_change:
        return {"decision": "new_file", "reason": "position opened/closed"}
    if fundamental_event:
        return {"decision": "new_file", "reason": "Rule 9 fundamental-event trigger fired"}
    if old_score_n != new_score_n:
        return {
            "decision": "new_file",
            "reason": f"score changed ({old_score_n!r} -> {new_score_n!r})",
        }
    if old_category_n != new_category_n:
        return {
            "decision": "new_file",
            "reason": f"action category changed ({old_category_n} -> {new_category_n})",
        }
    return {"decision": "append", "reason": "no significant change"}


def build_new_row(date: str, price: str, score_display: str, action_text: str, notes: str, session_link: str) -> str:
    for name, value in (
        ("date", date),
        ("price", price),
        ("score_display", score_display),
        ("action_text", action_text),
        ("notes", notes),
        ("session_link", session_link),
    ):
        if value is None or str(value).strip() == "":
            raise MissingInputError(f"Missing required input: '{name}' (needed to render a new table row)")
    return f"| {date} | {price} | {score_display} | {action_text} | {notes} | [session]({session_link}) |"


def build_append_line(date: str, note: str) -> str:
    if not date or not str(date).strip():
        raise MissingInputError("Missing required input: 'date' (needed to render the append line)")
    if not note or not str(note).strip():
        raise MissingInputError("Missing required input: 'note' (needed to render the append line)")
    return f"**Last checked (no significant change):** {date} — {note}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--old-score", required=True)
    parser.add_argument("--old-category", required=True)
    parser.add_argument("--new-score", required=True)
    parser.add_argument("--new-category", required=True)
    parser.add_argument("--fundamental-event", action="store_true")
    parser.add_argument("--position-change", action="store_true")
    parser.add_argument("--date", help="Date for the rendered row/line (required to render content)")
    parser.add_argument("--price")
    parser.add_argument("--action-text")
    parser.add_argument("--notes")
    parser.add_argument("--session-link")
    parser.add_argument("--check-note", help="Note for an append-line decision")
    args = parser.parse_args(argv)

    try:
        result = decide(
            args.old_score,
            args.old_category,
            args.new_score,
            args.new_category,
            fundamental_event=args.fundamental_event,
            position_change=args.position_change,
        )
        if args.date:
            if result["decision"] == "new_file":
                result["content"] = build_new_row(
                    args.date, args.price, args.new_score, args.action_text, args.notes, args.session_link
                )
            else:
                result["content"] = build_append_line(args.date, args.check_note or "no change")
    except MissingInputError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

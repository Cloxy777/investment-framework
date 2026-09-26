#!/usr/bin/env python3
"""Glossary term lookup — Stage 4 of scripts/TOKEN-OPTIMIZATION-PLAN.md.

framework/glossary.md is 700+ lines and grows every session; the operating
brief requires citing only the terms actually used in a given output, but
nothing previously stopped a full-file read. This prints just the requested
terms' definitions, read fresh from the file every time (never hand-copied/
cached, so it can't go stale relative to the file).

Structure parsed: one or more "## <Group>" sections, each containing a
"| Term | Meaning |" markdown table whose data rows are "| **Term** | meaning |".
A row like "| **A / B** | meaning |" defines both "A / B" as a whole and its
"A" / "B" halves as separately look-up-able exact terms (both point at the
same, single definition already in the file — not a second, invented one).

Per the framework's "never invent or estimate" rule extended to jargon: an
unknown term is never guessed at or silently skipped. It prints an explicit
NOT FOUND flag naming the term and instructing that it be added to
framework/glossary.md first.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from scripts.scoring.common import MissingInputError

DEFAULT_GLOSSARY = Path("framework/glossary.md")
ROW_RE = re.compile(r"^\|\s*\*\*(?P<term>.+?)\*\*\s*\|\s*(?P<meaning>.*?)\s*\|\s*$")


def load_glossary(path: Path = DEFAULT_GLOSSARY) -> dict[str, str]:
    if not path.is_file():
        raise MissingInputError(f"Glossary file not found: {path}")
    index: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = ROW_RE.match(line)
        if not match:
            continue
        term = match.group("term").strip()
        meaning = match.group("meaning").strip()
        if not meaning:
            continue
        _add(index, term, meaning)
        if " / " in term:
            for part in term.split(" / "):
                _add(index, part.strip(), meaning)
    return index


def _add(index: dict[str, str], key: str, meaning: str) -> None:
    lookup_key = key.lower()
    if lookup_key not in index:
        index[lookup_key] = meaning


def lookup(terms: list[str], path: Path = DEFAULT_GLOSSARY) -> list[dict]:
    index = load_glossary(path)
    results = []
    for term in terms:
        meaning = index.get(term.strip().lower())
        if meaning is None:
            results.append({"term": term, "found": False})
        else:
            results.append({"term": term, "found": True, "definition": meaning})
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("terms", nargs="+", help="Exact glossary term(s) to look up")
    parser.add_argument("--glossary", default=str(DEFAULT_GLOSSARY))
    args = parser.parse_args(argv)

    try:
        results = lookup(args.terms, Path(args.glossary))
    except MissingInputError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    any_missing = False
    for r in results:
        if r["found"]:
            print(f"**{r['term']}**: {r['definition']}")
        else:
            any_missing = True
            print(
                f"NOT FOUND: '{r['term']}' — add it to framework/glossary.md first "
                "before using it (per the framework's no-invent-jargon rule)."
            )
    return 1 if any_missing else 0


if __name__ == "__main__":
    raise SystemExit(main())

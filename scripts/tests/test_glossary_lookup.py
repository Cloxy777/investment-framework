from pathlib import Path

import pytest

from scripts.glossary_lookup import lookup
from scripts.scoring.common import MissingInputError

REAL_GLOSSARY = Path("framework/glossary.md")

KNOWN_TERMS = [
    "10-K (Annual Report)",
    "10-Q (Quarterly Report)",
    "52-week range",
    "Adjusted EBITDA",
    "ARR (Annual Recurring Revenue)",
    "AUM (Assets Under Management)",
    "Backlog",
    "Beta",
    "ASP (Average Selling Price)",
    "ADR (American Depositary Receipt)",
]


def _real_definition(term: str) -> str:
    """Read the real, current definition straight from the glossary file (no hand-copying)."""
    text = REAL_GLOSSARY.read_text(encoding="utf-8")
    marker = f"**{term}**"
    idx = text.index(marker)
    line = text[idx : text.index("\n", idx)]
    # line looks like "**Term** | Meaning |" (we started at the ** marker mid-row)
    meaning = line.split("|", 1)[1].strip()
    assert meaning.endswith("|")
    return meaning[:-1].strip()


@pytest.mark.parametrize("term", KNOWN_TERMS)
def test_known_terms_match_file_exactly(term):
    results = lookup([term], REAL_GLOSSARY)
    assert len(results) == 1
    assert results[0]["found"] is True
    assert results[0]["definition"] == _real_definition(term)


def test_unknown_term_gets_explicit_not_found_flag():
    results = lookup(["Definitely Not A Real Glossary Term XYZ"], REAL_GLOSSARY)
    assert results == [{"term": "Definitely Not A Real Glossary Term XYZ", "found": False}]


def test_lookup_preserves_order_and_mixes_found_and_missing():
    results = lookup(["Beta", "Nonexistent Term", "Backlog"], REAL_GLOSSARY)
    assert [r["term"] for r in results] == ["Beta", "Nonexistent Term", "Backlog"]
    assert results[0]["found"] is True
    assert results[1]["found"] is False
    assert results[2]["found"] is True


def test_compound_slash_term_is_lookup_able_by_either_half(tmp_path):
    glossary = tmp_path / "glossary.md"
    glossary.write_text(
        "## Group\n\n| Term | Meaning |\n|---|---|\n"
        "| **Sponsored ADR / Unsponsored ADR** | Some shared definition text. |\n",
        encoding="utf-8",
    )
    results = lookup(["Sponsored ADR", "Unsponsored ADR", "Sponsored ADR / Unsponsored ADR"], glossary)
    for r in results:
        assert r["found"] is True
        assert r["definition"] == "Some shared definition text."


def test_missing_glossary_file_hard_fails(tmp_path):
    with pytest.raises(MissingInputError):
        lookup(["Beta"], tmp_path / "does-not-exist.md")

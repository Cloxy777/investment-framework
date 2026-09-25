"""Shared helpers for the framework's scoring calculators.

See framework/quality-scoring.md, framework/valuation-scoring.md, and
framework/fair-value-methodology.md for the rules these implement.
"""

from decimal import ROUND_HALF_UP, Decimal


class MissingInputError(Exception):
    """Raised when a required input is missing or ambiguous.

    Per CLAUDE.md's "never invent or estimate financial data" non-negotiable,
    every calculator must hard-fail (naming exactly what's missing) rather
    than default, estimate, or silently skip a component.
    """


def require(data: dict, key: str, context: str = "") -> object:
    """Fetch data[key], raising MissingInputError with a precise name if absent or None."""
    if key not in data or data[key] is None:
        suffix = f" ({context})" if context else ""
        raise MissingInputError(f"Missing required input: '{key}'{suffix}")
    return data[key]


def clamp(value: float, lo: float = 0.0, hi: float = 100.0) -> float:
    return max(lo, min(hi, value))


def round_boundary(value: float, decimals: int = 1) -> float:
    """Round to `decimals` places; a value exactly on the half-step rounds UP.

    This is the framework's score-boundary rule (round to nearest 0.1; a
    .X5 rounds up, more conservative than banker's rounding). Python's
    built-in round() uses round-half-to-even, so this uses Decimal with
    ROUND_HALF_UP explicitly.
    """
    quantum = Decimal(1).scaleb(-decimals)
    d = Decimal(str(value)).quantize(quantum, rounding=ROUND_HALF_UP)
    return float(d)


def format_md_table(rows: list, headers: list) -> str:
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for row in rows:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    return "\n".join(lines)

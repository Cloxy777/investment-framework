#!/usr/bin/env python3
"""Composite Score calculator — implements the Composite Score in framework/valuation-scoring.md.

Composite Score = 0.50 x (100 - Quality Score) + 0.50 x Valuation Score

Only computed once Quality Score clears the 80.0+ gate (framework/quality-scoring.md) —
refuses otherwise, matching the gate.

Usage:
    python -m scripts.scoring.composite_score --set quality_score=88.0 --set valuation_score=35.0
    python -m scripts.scoring.composite_score --input path/to/inputs.json

JSON input schema — either:

{ "quality_score": float, "valuation_score": float }

or, to compute both sub-scores from their own raw inputs in one call:

{ "quality": { ...quality_score.py input schema... }, "valuation": { ...valuation_score.py input schema... } }
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from scripts.scoring import quality_score as qs
from scripts.scoring import valuation_score as vs
from scripts.scoring.common import MissingInputError, round_boundary

QUALITY_GATE = 80.0


class GateFailure(Exception):
    def __init__(self, quality_score: float):
        self.quality_score = quality_score
        super().__init__(
            f"Quality Score {quality_score} < {QUALITY_GATE} — fails the gate, "
            "Composite Score is not computed for a company that hasn't cleared Phase 01"
        )


def compute(d: dict) -> dict:
    steps = []

    if "quality_score" in d and "valuation_score" in d:
        quality = float(d["quality_score"])
        valuation = float(d["valuation_score"])
    elif "quality" in d and "valuation" in d:
        q_result = qs.compute(d["quality"])
        if not q_result["passes_gate"]:
            raise GateFailure(q_result["quality_score"])
        quality = q_result["quality_score"]
        valuation = vs.compute(d["valuation"])["valuation_score"]
        steps.append(f"Quality Score computed from raw inputs: {quality}")
        steps.append(f"Valuation Score computed from raw inputs: {valuation}")
    else:
        raise MissingInputError(
            "Provide either {'quality_score': float, 'valuation_score': float} "
            "or {'quality': {...}, 'valuation': {...}} raw-input blocks"
        )

    if quality < QUALITY_GATE:
        raise GateFailure(quality)

    raw = 0.50 * (100 - quality) + 0.50 * valuation
    final = round_boundary(raw)

    steps.append(f"Composite Score = 0.50x(100 - {quality}) + 0.50x{valuation} = {raw:.3f} -> rounds to {final}")

    return {"quality_score": quality, "valuation_score": valuation, "raw": raw, "composite_score": final, "steps": steps}


def render_markdown(result: dict) -> str:
    lines = ["## Composite Score\n", "```"]
    lines.extend(result["steps"])
    lines.append("```")
    lines.append(f"\n# Composite Score = {result['composite_score']}")
    lines.append(f"(Quality Score {result['quality_score']}, Valuation Score {result['valuation_score']})")
    return "\n".join(lines)


def _parse_set_flags(pairs: list[str]) -> dict:
    out = {}
    for pair in pairs:
        if "=" not in pair:
            raise SystemExit(f"--set expects key=value, got: {pair}")
        key, raw = pair.split("=", 1)
        try:
            value = json.loads(raw)
        except json.JSONDecodeError:
            value = raw
        out[key] = value
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", type=Path, help="Path to a JSON input file")
    parser.add_argument("--set", action="append", default=[], metavar="key=value")
    args = parser.parse_args(argv)

    data = {}
    if args.input:
        data = json.loads(args.input.read_text())
    data.update(_parse_set_flags(args.set))

    if not data:
        parser.error("no input provided — pass --input <file.json> and/or --set key=value")

    try:
        result = compute(data)
    except GateFailure as exc:
        print("# Composite Score REFUSED — Quality Score fails the 80.0+ gate")
        print(str(exc))
        return 1
    except MissingInputError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(render_markdown(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

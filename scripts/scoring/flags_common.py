#!/usr/bin/env python3
"""Advisory flags — no score effect, no hard disqualifier.

These flags exist to make a known blind spot visible at analysis time. They never change the
Quality, Valuation or Composite Score; the analyst must address each raised flag in the
session's Known-risks block (see framework/valuation-scoring.md, "Advisory flags").

Flags:
    cycle_peak           trailing GAAP diluted EPS grew > 100% YoY on a positive base — the
                         multiple may be flattered by peak-cycle earnings.
    multiple_ceiling     forward PE >= 30 and EPS growth < 30% — expensive without growth to
                         justify it.
    value_trap_candidate forward PE <= 15 while trailing EPS is falling — cheap because
                         earnings are deteriorating.

Every threshold below is a PLACEHOLDER (†) taken from an external reference system's printed
constants; none is calibrated on this repo's data. Missing inputs -> flag "UNKNOWN" (never
estimated).

Usage:
    python -m scripts.scoring.flags_common --eps-now 4.2 --eps-prior 1.9 --forward-pe 12
    python -m scripts.scoring.flags_common --forward-pe 34 --eps-growth 18
"""

from __future__ import annotations

import argparse
import sys

CYCLE_PEAK_GROWTH_PCT = 100.0  # †
CEILING_FORWARD_PE = 30.0  # †
CEILING_GROWTH_PCT = 30.0  # †
VALUE_TRAP_MAX_FORWARD_PE = 15.0  # †


def eps_growth_ttm_pct(eps_now: float | None, eps_prior: float | None) -> float | None:
    """YoY growth of TTM EPS in %, or None when undefined (missing input or prior <= 0)."""
    if eps_now is None or eps_prior is None or eps_prior <= 0:
        return None
    return (eps_now / eps_prior - 1) * 100


def cycle_peak(eps_ttm_now: float | None, eps_ttm_1y_ago: float | None, threshold_pct: float = CYCLE_PEAK_GROWTH_PCT) -> dict:
    """Flag CYCLE_PEAK_CANDIDATE when TTM EPS grew strictly more than `threshold_pct` on a positive base."""
    if eps_ttm_now is None or eps_ttm_1y_ago is None:
        return {"flag": "UNKNOWN", "growth_pct": None, "explain": "EPS TTM now or 1y ago unavailable"}
    if eps_ttm_1y_ago <= 0 < eps_ttm_now:
        return {
            "flag": "LOSS_TO_PROFIT_BASE",
            "growth_pct": None,
            "explain": "prior-year EPS <= 0: growth undefined; PEG-ineligible base (valuation-scoring.md)",
        }
    if eps_ttm_1y_ago <= 0:
        return {"flag": "NONE", "growth_pct": None, "explain": "loss-making: not a cycle-peak question"}
    g = eps_growth_ttm_pct(eps_ttm_now, eps_ttm_1y_ago)
    if g > threshold_pct:
        return {
            "flag": "CYCLE_PEAK_CANDIDATE",
            "growth_pct": g,
            "explain": f"EPS TTM +{g:.0f}% > {threshold_pct:.0f}%† — state why the multiple is compared with a normalised base",
        }
    return {"flag": "NONE", "growth_pct": g, "explain": f"EPS TTM {g:+.0f}% (<= {threshold_pct:.0f}%†)"}


def multiple_ceiling(forward_pe: float | None, eps_growth_pct: float | None) -> dict:
    """Flag MULTIPLE_CEILING when forward PE >= 30† and forward EPS growth < 30%†."""
    if forward_pe is None or eps_growth_pct is None:
        return {"flag": "UNKNOWN", "explain": "forward PE or EPS growth unavailable"}
    if forward_pe <= 0:
        return {"flag": "NONE", "explain": "no positive forward PE"}
    if forward_pe >= CEILING_FORWARD_PE and eps_growth_pct < CEILING_GROWTH_PCT:
        return {
            "flag": "MULTIPLE_CEILING",
            "explain": (
                f"forward PE {forward_pe:.1f} >= {CEILING_FORWARD_PE:.0f}† with EPS growth "
                f"{eps_growth_pct:.1f}% < {CEILING_GROWTH_PCT:.0f}%† — price needs growth the estimates don't show"
            ),
        }
    return {"flag": "NONE", "explain": f"forward PE {forward_pe:.1f}, EPS growth {eps_growth_pct:.1f}%"}


def value_trap_candidate(forward_pe: float | None, eps_growth_ttm: float | None) -> dict:
    """Flag VALUE_TRAP_CANDIDATE when 0 < forward PE <= 15† and trailing EPS growth is negative."""
    if forward_pe is None or eps_growth_ttm is None:
        return {"flag": "UNKNOWN", "explain": "forward PE or trailing EPS growth unavailable"}
    if 0 < forward_pe <= VALUE_TRAP_MAX_FORWARD_PE and eps_growth_ttm < 0:
        return {
            "flag": "VALUE_TRAP_CANDIDATE",
            "explain": (
                f"forward PE {forward_pe:.1f} <= {VALUE_TRAP_MAX_FORWARD_PE:.0f}† but EPS TTM "
                f"{eps_growth_ttm:+.0f}% — cheap because earnings are falling?"
            ),
        }
    return {"flag": "NONE", "explain": f"forward PE {forward_pe:.1f}, EPS TTM growth {eps_growth_ttm:+.1f}%"}


def render(results: dict) -> str:
    lines = ["Advisory flags (no score effect; † = uncalibrated placeholder threshold)"]
    for name, r in results.items():
        lines.append(f"  {name:<22} {r['flag']:<22} {r['explain']}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--eps-now", type=float, help="GAAP diluted EPS, trailing 12 months")
    p.add_argument("--eps-prior", type=float, help="GAAP diluted EPS, trailing 12 months ending a year earlier")
    p.add_argument("--forward-pe", type=float)
    p.add_argument("--eps-growth", type=float, help="forward (consensus) EPS growth in %%, as used for PEG")
    a = p.parse_args(argv)

    results = {
        "cycle_peak": cycle_peak(a.eps_now, a.eps_prior),
        "multiple_ceiling": multiple_ceiling(a.forward_pe, a.eps_growth),
        "value_trap_candidate": value_trap_candidate(a.forward_pe, eps_growth_ttm_pct(a.eps_now, a.eps_prior)),
    }
    print(render(results))
    return 0


if __name__ == "__main__":
    sys.exit(main())

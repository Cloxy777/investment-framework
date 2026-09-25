#!/usr/bin/env python3
"""Valuation Score calculator — implements framework/valuation-scoring.md.

Computes the 0-100.0 Phase 02 Valuation Score: the four weighted sub-scores
(FCF Yield, EV/EBIT, Forward PE, PEG-or-fallback), the Rate Regime Modifier
(via the Rate Environment Gate in framework/strategy.md), and the
Upside/Downside (Expected-Return) Modifier.

Usage:
    python -m scripts.scoring.valuation_score --input path/to/inputs.json
    python -m scripts.scoring.valuation_score --input inputs.json --set forward_pe=13.93

JSON input schema (all fields required unless noted):

{
  "fcf_yield_pct": float,
  "ev_ebit": float,
  "fast_grower": bool,                 # PEG sub-score applicable (EPS growth >15% for 3+ yrs, clean earnings base)
  "peg": float,                        # required if fast_grower is true
  "forward_pe": float,
  "pe_mode": "range" | "avg" | "none",
  "pe_5yr_low": float,                 # required if pe_mode == "range"
  "pe_5yr_high": float,                # required if pe_mode == "range"
  "pe_5yr_avg": float,                 # required if pe_mode in ("range", "avg")
  "structural_quality_override": bool,           # optional: skip the +10 "expensive" Historical PE Modifier
  "structural_quality_override_evidence": str,   # required (cited) if the override above is true

  "treasury_10y_pct": float,           # feeds the Rate Environment Gate (strategy.md)

  "live_price": float,                 # Rule 0 — fetch live, never infer
  "bull_fair_value": float,
  "base_fair_value": float,
  "bear_fair_value": float,
  "catalyst_within_18_24_months": bool,
  "catalyst_window_years": float,      # optional; Rule 10 default is 2yr if no narrower window documented
  "intrinsic_growth_pct": float,       # FCF or EPS CAGR
  "dividend_yield_pct": float,
  "net_buyback_yield_pct": float
}

Note on the Historical PE Modifier's undocumented middle band: framework/strategy.md's
Upgrade 2 table only defines three buckets (>20% below -> -10, within +-10% -> 0,
>20% above -> +10). A forward PE deviating 10-20% from the 5yr average in either
direction falls into a documented gap with no defined modifier. This script refuses
to guess and raises MissingInputError naming the gap — see the PR description.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from scripts.scoring.common import MissingInputError, clamp, require, round_boundary

HURDLE = 10.0  # H, percentage points


def _fcf_yield(d: dict) -> tuple[float, list]:
    fy = require(d, "fcf_yield_pct")
    score = clamp(100 * (1 - fy / 10))
    return score, [f"FCF_Score = clamp(100x(1 - {fy}/10)) = {score:.3f}"]


def _ev_ebit(d: dict) -> tuple[float, list]:
    ev_ebit = require(d, "ev_ebit")
    score = clamp((ev_ebit - 12) / 23 * 100)
    return score, [f"EV/EBIT_Score = clamp(({ev_ebit} - 12)/23 x 100) = {score:.3f}"]


def _forward_pe(d: dict) -> tuple[float, list]:
    fwd = require(d, "forward_pe")
    mode = require(d, "pe_mode")
    steps = []

    if mode == "none":
        steps.append("No 5yr PE history available (no-history fallback) -> FwdPE_Score = 50.0 (neutral, flagged)")
        return 50.0, steps

    if mode == "avg":
        avg = require(d, "pe_5yr_avg")
        deviation = (fwd - avg) / avg * 100
        score = clamp(50 + deviation * 2.5)
        steps.append(f"Deviation% = ({fwd} - {avg})/{avg} x 100 = {deviation:.3f}%")
        steps.append(f"FwdPE_Score = clamp(50 + {deviation:.3f}x2.5) = {score:.3f} (fallback formula; Historical PE Modifier already folded in)")
        return score, steps

    if mode == "range":
        low = require(d, "pe_5yr_low")
        high = require(d, "pe_5yr_high")
        avg = require(d, "pe_5yr_avg")
        raw = clamp((fwd - low) / (high - low) * 100)
        steps.append(f"FwdPE_Score (raw) = clamp(({fwd} - {low})/({high} - {low}) x 100) = {raw:.3f}")

        deviation = (fwd - avg) / avg * 100
        steps.append(f"Deviation vs 5yr avg ({avg}) = ({fwd} - {avg})/{avg} x 100 = {deviation:.3f}%")

        if deviation <= -20:
            modifier = -10
            steps.append("Historical PE Modifier: >20% below 5yr avg -> -10")
        elif -10 <= deviation <= 10:
            modifier = 0
            steps.append("Historical PE Modifier: within +-10% of 5yr avg -> 0")
        elif deviation >= 20:
            override = d.get("structural_quality_override", False)
            if override:
                evidence = d.get("structural_quality_override_evidence")
                if not evidence:
                    raise MissingInputError(
                        "'structural_quality_override' is true but "
                        "'structural_quality_override_evidence' (cited margin/ROIC/CapEx evidence) is missing"
                    )
                modifier = 0
                steps.append(
                    f"Historical PE Modifier: >20% above 5yr avg, but Structural Quality Override applies "
                    f"({evidence}) -> penalty skipped, modifier 0"
                )
            else:
                modifier = 10
                steps.append("Historical PE Modifier: >20% above 5yr avg -> +10")
        else:
            raise MissingInputError(
                "Forward PE deviation vs 5yr avg is "
                f"{deviation:.2f}%, which falls in the 10-20% band that "
                "framework/strategy.md's Upgrade 2 table does not define a modifier for "
                "(only >20% below, within +-10%, and >20% above are specified). "
                "This is a documented gap in the framework, not a missing data point — "
                "resolve it in framework/strategy.md and record the decision in decisions/ "
                "rather than having this script guess."
            )

        score = clamp(raw + modifier)
        steps.append(f"FwdPE_Score = clamp({raw:.3f} + {modifier}) = {score:.3f}")
        return score, steps

    raise MissingInputError(f"Unknown pe_mode: {mode!r} (expected 'range', 'avg', or 'none')")


def _peg(d: dict) -> tuple[float | None, list]:
    fast_grower = require(d, "fast_grower")
    if not fast_grower:
        return None, ["PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT"]
    peg = require(d, "peg", "PEG required when fast_grower is true")
    score = clamp((peg - 0.5) / 2.0 * 100)
    return score, [f"PEG_Score = clamp(({peg} - 0.5)/2.0 x 100) = {score:.3f}"]


def _rate_environment_gate(d: dict, forward_pe: float) -> tuple[float, list]:
    treasury = require(d, "treasury_10y_pct")
    ey = 1 / forward_pe * 100
    spread = ey - treasury
    step1 = 0 if spread >= 1.5 else 5
    if treasury < 2:
        step2 = -10
    elif treasury < 3.5:
        step2 = 0
    elif treasury <= 5:
        step2 = 5
    else:
        step2 = 10
    total = step1 + step2
    steps = [
        f"EY = 1/{forward_pe} x 100 = {ey:.4f}%",
        f"Spread = EY - 10Y ({treasury}%) = {spread:.4f}pp -> Step 1 = {'+0 (pass, >=1.5pp)' if step1 == 0 else '+5 (fail, <1.5pp)'}",
        f"10Y = {treasury}% -> Step 2 bracket modifier = {'+' if step2 >= 0 else ''}{step2}",
        f"Total Rate Modifier = {step1} + {step2} = {'+' if total >= 0 else ''}{total}",
    ]
    return total, steps


def _upside_downside(d: dict) -> tuple[float, list]:
    bull = require(d, "bull_fair_value")
    base = require(d, "base_fair_value")
    bear = require(d, "bear_fair_value")
    live = require(d, "live_price")
    catalyst_ok = require(d, "catalyst_within_18_24_months")
    window = d.get("catalyst_window_years", 2.0)
    growth = require(d, "intrinsic_growth_pct")
    div_yield = require(d, "dividend_yield_pct")
    buyback_yield = require(d, "net_buyback_yield_pct")

    pw_fv = 0.25 * bull + 0.50 * base + 0.25 * bear
    gap_pct = (pw_fv / live - 1) * 100
    annualized = gap_pct / window
    shareholder_yield = div_yield + buyback_yield
    e = annualized + growth + shareholder_yield

    steps = [
        f"PW Fair Value = 0.25x{bull} + 0.50x{base} + 0.25x{bear} = {pw_fv:.4f}",
        f"Gap Upside % = ({pw_fv:.4f}/{live}) - 1 = {gap_pct:.4f}%",
        f"Annualized gap = {gap_pct:.4f}% / {window}yr = {annualized:.4f}%/yr",
        f"E = {annualized:.4f} (annualized gap) + {growth} (intrinsic growth) + "
        f"{shareholder_yield:.4f} (shareholder yield: {div_yield} div + {buyback_yield} buyback) = {e:.4f}%/yr",
    ]

    if e >= HURDLE:
        m = -15 * clamp((e - HURDLE) / 15, 0, 1)
        steps.append(f"E ({e:.4f}%) >= H ({HURDLE}%) -> M = -15 x clamp(({e:.4f}-{HURDLE})/15, 0, 1) = {m:.4f}")
    elif e >= 0:
        m = 5 * (HURDLE - e) / HURDLE
        steps.append(f"0 <= E ({e:.4f}%) < H -> M = 5 x ({HURDLE}-{e:.4f})/{HURDLE} = {m:.4f}")
    else:
        m = 5 + 10 * clamp((-e) / 10, 0, 1)
        steps.append(f"E ({e:.4f}%) < 0 -> M = 5 + 10 x clamp((-{e:.4f})/10, 0, 1) = {m:.4f}")

    if not catalyst_ok and m < -5:
        steps.append(
            f"Guardrail 1: no catalyst identifiable within 18-24 months -> upside side capped at -5 (was {m:.4f})"
        )
        m = -5.0

    m = clamp(m, -15, 15)
    steps.append(f"Upside/Downside Modifier (bounded [-15, +15]) = {m:.4f}")
    return m, steps


def compute(d: dict) -> dict:
    fcf_score, fcf_steps = _fcf_yield(d)
    ev_ebit_score, ev_ebit_steps = _ev_ebit(d)
    fwd_pe = require(d, "forward_pe")
    fwd_score, fwd_steps = _forward_pe(d)
    peg_score, peg_steps = _peg(d)

    if peg_score is None:
        weights = {"fcf": 0.40, "ev_ebit": 0.40, "fwd_pe": 0.20, "peg": 0.0}
    else:
        weights = {"fcf": 0.40, "ev_ebit": 0.25, "fwd_pe": 0.20, "peg": 0.15}

    raw = (
        fcf_score * weights["fcf"]
        + ev_ebit_score * weights["ev_ebit"]
        + fwd_score * weights["fwd_pe"]
        + (peg_score or 0.0) * weights["peg"]
    )

    rate_modifier, rate_steps = _rate_environment_gate(d, fwd_pe)
    upside_modifier, upside_steps = _upside_downside(d)

    final_raw = raw + rate_modifier + upside_modifier
    final = round_boundary(clamp(final_raw, 0.0, 100.0))

    return {
        "sub_scores": {"FCF": fcf_score, "EV/EBIT": ev_ebit_score, "FwdPE": fwd_score, "PEG": peg_score},
        "weights": weights,
        "steps": {
            "FCF Yield (40%)": fcf_steps,
            "EV/EBIT": ev_ebit_steps,
            "Forward PE": fwd_steps,
            "PEG": peg_steps,
            "Rate Environment Gate": rate_steps,
            "Upside/Downside Modifier": upside_steps,
        },
        "raw_weighted": raw,
        "rate_modifier": rate_modifier,
        "upside_downside_modifier": upside_modifier,
        "final_raw": final_raw,
        "valuation_score": final,
    }


def render_markdown(result: dict) -> str:
    lines = ["## Valuation Score\n"]
    for section, steps in result["steps"].items():
        lines.append(f"**{section}**")
        lines.append("```")
        lines.extend(steps)
        lines.append("```")
    w = result["weights"]
    s = result["sub_scores"]
    lines.append("**Raw Weighted Score**")
    lines.append("```")
    parts = [f"FCF_Score x {w['fcf']}", f"EV/EBIT_Score x {w['ev_ebit']}", f"FwdPE_Score x {w['fwd_pe']}"]
    if w["peg"]:
        parts.append(f"PEG_Score x {w['peg']}")
    lines.append("Raw = " + " + ".join(parts))
    lines.append(f"= {result['raw_weighted']:.3f}")
    lines.append("```")
    lines.append("**Final Valuation Score**")
    lines.append("```")
    lines.append(
        f"Final Score = Raw ({result['raw_weighted']:.3f}) + Rate Modifier ({result['rate_modifier']:+}) + "
        f"Upside/Downside Modifier ({result['upside_downside_modifier']:+.3f})"
    )
    lines.append(f"= {result['final_raw']:.3f} -> rounds to {result['valuation_score']}")
    lines.append("```")
    lines.append(f"\n# Valuation Score = {result['valuation_score']}")
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
    except MissingInputError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(render_markdown(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

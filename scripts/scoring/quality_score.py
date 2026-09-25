#!/usr/bin/env python3
"""Quality Score calculator — implements framework/quality-scoring.md.

Computes the 0-100.0 Quality Score and the strict 80.0+ Phase 02 eligibility
gate, applying the hard disqualifiers BEFORE the weighted calculation.

Usage:
    python -m scripts.scoring.quality_score --input path/to/inputs.json
    python -m scripts.scoring.quality_score --input inputs.json --set net_margin_pct=19.5

JSON input schema (all fields required unless noted):

{
  "net_margin_pct": float,                  # TTM net margin, e.g. 18 for 18%
  "roic_pct": float,                        # TTM ROIC, e.g. 22 for 22%
  "fcf_positive_3yr_or_more": bool,         # FCF positive every year, most recent 3+ FY (rolling window)
  "gross_margin_pct": float,
  "gross_margin_structural_trend": bool,    # 3yr structurally expanding gross margin
  "revenue_cagr_3yr_pct": float,
  "tam_expansion_evidence": bool,
  "tam_expansion_evidence_text": str,       # required (cited source) if tam_expansion_evidence is true
  "growth_decelerating_evidence": bool,
  "growth_decelerating_evidence_text": str, # required (cited source) if growth_decelerating_evidence is true
  "net_debt_to_ebitda": float,
  "asset_light_override": bool,             # Upgrade 5: use /6 denominator + 4x disqualifier threshold
  "asset_light_interest_coverage": float,   # required if asset_light_override is true (must be > 15)
  "asset_light_investment_grade": bool,     # required if asset_light_override is true (must be true)
  "moat_signals": {
      "market_share_stable_or_growing": {"true": bool, "evidence": str},
      "brand_premium":                  {"true": bool, "evidence": str},
      "network_effect":                 {"true": bool, "evidence": str},
      "switching_costs":                {"true": bool, "evidence": str},
      "scale_cost_advantage":           {"true": bool, "evidence": str}
  },
  "fcf_ni_ttm_pct": float,                  # TTM FCF/Net Income ratio, e.g. 82 for 82%, feeds the continuous sub-score
  "fcf_ni_annual_pct": [float, ...],        # trailing fiscal years, OLDEST FIRST, for the hard-disqualifier check
  "fcf_ni_low_conversion_explanation": str  # required only if 2+ CONSECUTIVE annual years are <70%
}
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from scripts.scoring.common import MissingInputError, clamp, format_md_table, require, round_boundary

QUALITY_GATE = 80.0


class FailsGate(Exception):
    def __init__(self, reason: str):
        self.reason = reason
        super().__init__(reason)


def _check_hard_disqualifiers(d: dict) -> None:
    # 1. FCF/NI conversion <70% for 2+ consecutive years, unexplained.
    annual = require(d, "fcf_ni_annual_pct", "hard disqualifier: FCF/NI conversion history")
    if len(annual) < 2:
        raise MissingInputError(
            "'fcf_ni_annual_pct' must contain at least 2 fiscal years to evaluate the "
            "'<70% for 2+ consecutive years' hard disqualifier"
        )
    consecutive_low = any(annual[i] < 70 and annual[i + 1] < 70 for i in range(len(annual) - 1))
    if consecutive_low and not d.get("fcf_ni_low_conversion_explanation"):
        raise FailsGate(
            "FCF/Net Income conversion ratio <70% for 2+ consecutive years "
            f"({annual}) with no documented growth-capex explanation"
        )

    # 2. Net debt/EBITDA over its applicable threshold.
    net_debt_ebitda = require(d, "net_debt_to_ebitda", "hard disqualifier: balance sheet")
    asset_light = bool(d.get("asset_light_override", False))
    if asset_light:
        coverage = require(d, "asset_light_interest_coverage", "asset-light override eligibility")
        ig = require(d, "asset_light_investment_grade", "asset-light override eligibility")
        if not (coverage > 15 and ig):
            raise MissingInputError(
                "asset_light_override=true but eligibility not met: requires "
                "asset_light_interest_coverage > 15 (got "
                f"{coverage}) and asset_light_investment_grade == true (got {ig})"
            )
        threshold = 4.0
    else:
        threshold = 2.5
    if net_debt_ebitda > threshold:
        raise FailsGate(f"Net Debt/EBITDA {net_debt_ebitda}x exceeds the {threshold}x threshold")

    # 3. Not FCF-positive for 3+ consecutive years.
    fcf_positive = require(d, "fcf_positive_3yr_or_more", "hard disqualifier: FCF positivity")
    if not fcf_positive:
        raise FailsGate("Not FCF-positive for 3+ consecutive years")


def _profitability(d: dict) -> tuple[float, list]:
    nm = require(d, "net_margin_pct")
    roic = require(d, "roic_pct")
    fcf_positive = require(d, "fcf_positive_3yr_or_more")
    nm_c = clamp((nm / 30) * 100)
    roic_c = clamp((roic / 30) * 100)
    score = (nm_c + roic_c) / 2
    capped = False
    if not fcf_positive:
        capped = score > 40.0
        score = min(score, 40.0)
    steps = [
        f"NetMargin_Component = clamp(({nm}/30)x100) = {nm_c:.2f}",
        f"ROIC_Component = clamp(({roic}/30)x100) = {roic_c:.2f}",
        f"Profitability_Score = ({nm_c:.2f} + {roic_c:.2f}) / 2 = {(nm_c + roic_c) / 2:.2f}"
        + (" -> capped at 40.0 (not FCF-positive 3yr+)" if capped else ""),
    ]
    return score, steps


def _margins(d: dict) -> tuple[float, list]:
    gm = require(d, "gross_margin_pct")
    trend = require(d, "gross_margin_structural_trend")
    base = clamp((gm / 80) * 100)
    score = base
    steps = [f"GrossMargin_Score = clamp(({gm}/80)x100) = {base:.2f}"]
    if trend:
        score = min(base + 10, 100.0)
        steps.append(f"+10 structural-trend bonus -> clamp({base:.2f}+10, 0, 100) = {score:.2f}")
    return score, steps


def _growth(d: dict) -> tuple[float, list]:
    cagr = require(d, "revenue_cagr_3yr_pct")
    tam = require(d, "tam_expansion_evidence")
    decel = require(d, "growth_decelerating_evidence")
    if tam and not d.get("tam_expansion_evidence_text"):
        raise MissingInputError(
            "'tam_expansion_evidence' is true but 'tam_expansion_evidence_text' (cited source) is missing"
        )
    if decel and not d.get("growth_decelerating_evidence_text"):
        raise MissingInputError(
            "'growth_decelerating_evidence' is true but 'growth_decelerating_evidence_text' (cited source) is missing"
        )
    base = clamp((cagr / 25) * 100)
    score = base
    steps = [f"Growth_Score = clamp(({cagr}/25)x100) = {base:.2f}"]
    if tam:
        score += 10
        steps.append(f"+10 TAM/pricing-power evidence: {d['tam_expansion_evidence_text']}")
    if decel:
        score -= 10
        steps.append(f"-10 structural growth deceleration evidence: {d['growth_decelerating_evidence_text']}")
    score = clamp(score)
    steps.append(f"Growth_Score (final, clamped) = {score:.2f}")
    return score, steps


def _balance_sheet(d: dict) -> tuple[float, list]:
    ratio = require(d, "net_debt_to_ebitda")
    asset_light = bool(d.get("asset_light_override", False))
    denom = 6 if asset_light else 4
    score = clamp(100 * (1 - ratio / denom))
    steps = [
        f"BalanceSheet_Score = clamp(100x(1 - {ratio}/{denom})) = {score:.2f}"
        + (" [asset-light /6 override]" if asset_light else "")
    ]
    return score, steps


MOAT_SIGNALS = [
    "market_share_stable_or_growing",
    "brand_premium",
    "network_effect",
    "switching_costs",
    "scale_cost_advantage",
]


def _moat(d: dict) -> tuple[float, list]:
    signals = require(d, "moat_signals")
    rows = []
    count = 0
    for key in MOAT_SIGNALS:
        if key not in signals:
            raise MissingInputError(f"Missing moat signal: 'moat_signals.{key}'")
        entry = signals[key]
        is_true = require(entry, "true", f"moat_signals.{key}")
        if is_true and not entry.get("evidence"):
            raise MissingInputError(f"moat_signals.{key} marked true but 'evidence' is missing")
        if is_true:
            count += 1
        rows.append((key, is_true, entry.get("evidence", "")))
    score = (count / 5) * 100
    steps = [format_md_table(rows, ["Signal", "True", "Evidence"]), f"Moat_Score = ({count}/5) x 100 = {score:.2f}"]
    return score, steps


def _fcf_quality(d: dict) -> tuple[float, list]:
    ratio_pct = require(d, "fcf_ni_ttm_pct")
    ratio = ratio_pct / 100
    score = clamp(((ratio - 0.40) / 0.60) * 100)
    steps = [f"FCFQuality_Score = clamp((({ratio:.4f} - 0.40)/0.60)x100) = {score:.2f}"]
    return score, steps


def compute(d: dict) -> dict:
    _check_hard_disqualifiers(d)

    profitability, prof_steps = _profitability(d)
    margins, margin_steps = _margins(d)
    growth, growth_steps = _growth(d)
    balance_sheet, bs_steps = _balance_sheet(d)
    moat, moat_steps = _moat(d)
    fcf_quality, fcf_steps = _fcf_quality(d)

    weighted = (
        profitability * 0.25
        + margins * 0.15
        + growth * 0.20
        + balance_sheet * 0.15
        + moat * 0.15
        + fcf_quality * 0.10
    )
    final = round_boundary(clamp(weighted, 0.0, 100.0))
    passes_gate = final >= QUALITY_GATE

    return {
        "sub_scores": {
            "Profitability": profitability,
            "Margins": margins,
            "Growth": growth,
            "BalanceSheet": balance_sheet,
            "Moat": moat,
            "FCFQuality": fcf_quality,
        },
        "steps": {
            "Profitability (25%)": prof_steps,
            "Margins (15%)": margin_steps,
            "Growth (20%)": growth_steps,
            "Balance Sheet (15%)": bs_steps,
            "Moat Signal (15%)": moat_steps,
            "FCF Quality (10%)": fcf_steps,
        },
        "weighted_raw": weighted,
        "quality_score": final,
        "passes_gate": passes_gate,
    }


def render_markdown(result: dict) -> str:
    lines = ["## Quality Score\n"]
    for section, steps in result["steps"].items():
        lines.append(f"**{section}**")
        lines.append("```")
        lines.extend(steps)
        lines.append("```")
    s = result["sub_scores"]
    lines.append("**Quality Score — Final**")
    lines.append("```")
    lines.append(
        f"Quality Score = ({s['Profitability']:.2f}x0.25) + ({s['Margins']:.2f}x0.15) + "
        f"({s['Growth']:.2f}x0.20) + ({s['BalanceSheet']:.2f}x0.15) + ({s['Moat']:.2f}x0.15) + "
        f"({s['FCFQuality']:.2f}x0.10)"
    )
    lines.append(f"= {result['weighted_raw']:.3f} -> rounds to {result['quality_score']}")
    lines.append("```")
    verdict = "PASSES" if result["passes_gate"] else "FAILS"
    lines.append(f"\n# Quality Score = {result['quality_score']} — {verdict} the 80.0+ gate")
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
    parser.add_argument(
        "--set",
        action="append",
        default=[],
        metavar="key=value",
        help="Override/add a single field for an ad hoc run (JSON-parsed value; repeatable)",
    )
    args = parser.parse_args(argv)

    data = {}
    if args.input:
        data = json.loads(args.input.read_text())
    data.update(_parse_set_flags(args.set))

    if not data:
        parser.error("no input provided — pass --input <file.json> and/or --set key=value")

    try:
        result = compute(data)
    except FailsGate as exc:
        print("# FAILS GATE")
        print(f"Reason: {exc.reason}")
        return 1
    except MissingInputError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(render_markdown(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

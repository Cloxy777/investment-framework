# Quality Score Engine

How to compute Phase 01 quality score (0–100.0) for a candidate company, and the **strict 80.0+ quality gate** a company must clear before being eligible for Phase 02 valuation scoring at all. See [strategy.md](strategy.md) for where this fits, and [valuation-scoring.md](valuation-scoring.md) for how it combines with the valuation score into the Composite Score.

> **Scoring methodology version: 2026-06-29.** Same versioning/stale-score rules as [valuation-scoring.md](valuation-scoring.md) — bump this date whenever a sub-score, weight, or the gate threshold changes, and record why in `decisions/`.

## Why Quality Gets Its Own Score

Phase 01 was previously a binary pass/fail screen (margin/ROIC/growth/balance-sheet/moat/FCF thresholds — see "Quantitative Pre-Screen Filters" in [valuation-scoring.md](valuation-scoring.md)). That treats every company clearing the bar as interchangeable, so a 72-quality compounder and a 95-quality juggernaut look identical once both pass — only the valuation score differentiates them. A graded 0–100.0 quality score lets the framework directly compare "cheaper but lower quality" against "pricier but much higher quality" instead of defaulting to whichever is cheaper.

**0 = lowest quality, 100.0 = highest quality** — the opposite orientation from the valuation score (where 0 = cheapest/most attractive). Intentional: each score reads naturally on its own (higher quality = better; lower valuation score = better), and the Composite Score formula below reconciles the two orientations into one consistently-oriented number.

## The Strict 80.0+ Gate

**A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all.** Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks. This replaces the old binary Phase 01 screen as the eligibility gate (the individual hard disqualifiers below still apply *in addition* to the score).

A deliberately high bar, set per explicit user instruction (2026-06-29) — strict on purpose, to be loosened later only if it screens out too much of the investable universe. If it does, lower the threshold here and record why in `decisions/` rather than quietly working around it.

**Hard disqualifiers — fail regardless of weighted score:**
- FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation (existing Phase 01 FCF Quality Check)
- Net debt/EBITDA over its applicable threshold (2.5× standard, or 4× under the Upgrade 5 asset-light override) — see Balance Sheet sub-score
- Not FCF-positive for 3+ consecutive years

These mirror the existing Phase 01 non-negotiables — a weighted average can't average away an outright balance-sheet or cash-flow-quality failure.

## Final Quality Score Formula

```
Quality Score = (Profitability_Score × 0.25) + (Margins_Score × 0.15) + (Growth_Score × 0.20)
               + (BalanceSheet_Score × 0.15) + (Moat_Score × 0.15) + (FCFQuality_Score × 0.10)
```

> Score boundary rule: round to the nearest 0.1; if it falls exactly on a ".X5", round UP (more conservative, consistent with the valuation score's rule). Min 0.0, max 100.0.

## Sub-score Formulas

**Profitability (25% weight)** — blends Net Margin and ROIC, the two Phase 01 profitability criteria:

```
NetMargin_Component = clamp((Net Margin% / 30) × 100, 0, 100)
ROIC_Component       = clamp((ROIC% / 30) × 100, 0, 100)
Profitability_Score  = (NetMargin_Component + ROIC_Component) / 2
```

| Net Margin or ROIC | Component Score |
|---|---|
| 0% | 0.0 |
| 15% | 50.0 |
| 22.5% | 75.0 |
| ≥30% | 100.0 |

If the company isn't FCF-positive for 3+ consecutive years, cap Profitability_Score at 40.0 regardless of margin/ROIC — sustained quality requires sustained cash generation, not just accounting profitability.

**Margins (15% weight)** — gross margin level, with a structural-trend bonus:

```
GrossMargin_Score = clamp((Gross Margin% / 80) × 100, 0, 100)
```

| Gross Margin | Score |
|---|---|
| 0% | 0.0 |
| 40% | 50.0 |
| 60% | 75.0 |
| ≥80% | 100.0 |

If gross margin is structurally expanding (3yr trend, per Phase 01's "High Margins" criterion) even while below 40%, add **+10** (capped at 100.0) — a margin below the static threshold but moving the right direction is still evidence of improving quality.

**Growth (20% weight)** — revenue CAGR, with a qualitative TAM/pricing-power modifier:

```
Growth_Score = clamp((Revenue 3yr CAGR% / 25) × 100, 0, 100)
```

| Revenue CAGR | Score |
|---|---|
| 0% | 0.0 |
| 10% | 40.0 |
| 17.5% | 70.0 |
| ≥25% | 100.0 |

Documented evidence of TAM expansion and/or pricing power (Phase 01's "Growth" criterion) adds **+10**; documented evidence growth is decelerating structurally (not cyclically) subtracts **−10**. Both capped to [0, 100]. Cite the specific evidence in the session log — never infer this modifier without a documented source, consistent with "never invent or estimate financial data."

**Balance Sheet (15% weight)** — Net Debt/EBITDA, lower is better:

```
BalanceSheet_Score = clamp(100 × (1 − NetDebt/EBITDA / 4), 0, 100)
```

| Net Debt/EBITDA | Score |
|---|---|
| 0× | 100.0 |
| 1× | 75.0 |
| 2× | 50.0 |
| ≥4× | 0.0 |

**Asset-light override (Upgrade 5, [strategy.md](strategy.md)):** for payment networks, exchanges, or asset-light businesses where 100% of debt is financial, interest coverage >15×, and investment-grade rated, use a /6 denominator instead of /4 (i.e. the 0.0 floor moves out to 6×) — consistent with that upgrade's 4× (vs. standard 2.5×) pass/fail threshold. **Conglomerate rule** (Phase 01) still applies: consolidate captive financial-subsidiary debt into the ratio before scoring.

**Moat Signal (15% weight)** — qualitative by nature; scored as a checklist rather than invented as a single number. Document the evidence for each signal marked true — never mark a signal true without a cited source:

```
Moat_Score = (count of TRUE signals / 5) × 100
```

| Signal | Evidence required |
|---|---|
| Market share stable or growing | Cited share data (company filings, third-party market-share reports) |
| Brand premium | Pricing power evidence (price increases without volume loss, premium vs. competitors) |
| Network effect | Documented mechanism (e.g. two-sided marketplace dynamics, user-growth-driven value) |
| Switching costs | Documented mechanism (integration depth, contractual lock-in, data/workflow migration cost) |
| Scale cost advantage | Cost-per-unit data showing a gap vs. smaller competitors |

**FCF Quality (10% weight)** — FCF/Net Income conversion ratio (Phase 01's FCF Quality Check, made continuous):

```
FCFQuality_Score = clamp(((FCF/NI Ratio − 0.40) / 0.60) × 100, 0, 100)
```

| FCF/NI Ratio | Score |
|---|---|
| ≤40% | 0.0 |
| 70% | 50.0 |
| 85% | 75.0 |
| ≥100% | 100.0 |

Remember: a ratio below 70% for 2+ consecutive years without a documented growth-capex explanation is a **hard disqualifier** (see above), independent of this continuous score.

## Worked Example

A candidate: Net Margin 18%, ROIC 22%, Gross Margin 55% (flat, no structural trend), Revenue 3yr CAGR 14% (documented TAM expansion), Net Debt/EBITDA 0.8×, 4 of 5 moat signals documented true, FCF/NI ratio 82%, FCF-positive 5 consecutive years.

```
NetMargin_Component = clamp((18/30)×100) = 60.0
ROIC_Component       = clamp((22/30)×100) = 73.3
Profitability_Score  = (60.0 + 73.3) / 2 = 66.7   (no FCF cap — 5yr positive)

GrossMargin_Score = clamp((55/80)×100) = 68.8      (no trend bonus — flat)

Growth_Score = clamp((14/25)×100) = 56.0 + 10 (TAM evidence) = 66.0

BalanceSheet_Score = 100 × (1 − 0.8/4) = 80.0

Moat_Score = (4/5) × 100 = 80.0

FCFQuality_Score = clamp(((0.82 − 0.40)/0.60)×100) = 70.0

Quality Score = 66.7×0.25 + 68.8×0.15 + 66.0×0.20 + 80.0×0.15 + 80.0×0.15 + 70.0×0.10
              = 16.68 + 10.32 + 13.20 + 12.00 + 12.00 + 7.00
              = 71.2
```

71.2 < 80.0 — **fails the gate.** Despite passing every individual Phase 01 threshold, this company doesn't clear the strict 80.0+ bar and doesn't proceed to Phase 02. (This is the intended behaviour of a strict gate — if it screens out too many otherwise-reasonable candidates, lower the threshold per the note above and record why.)

## Quantitative Inputs Needed

Same sourcing discipline as valuation scoring — never invent or estimate a missing input; stop and ask:

```
Net Margin (TTM)
ROIC (TTM)
Gross Margin (TTM + 3yr trend)
Revenue 3yr CAGR
TAM expansion / pricing power evidence (qualitative, cited)
Net Debt/EBITDA (consolidated per conglomerate rule if applicable)
Asset-light override eligibility (if applicable): interest coverage, credit rating
Moat signal evidence (cited, per signal)
FCF/Net Income ratio, 2+ years
FCF positive/negative, 3+ years
```

All available via the same `yfinance` fields already wired up for Phase 01 verification (see "Screening Tools" / `yfinance` sections in [valuation-scoring.md](valuation-scoring.md)) except the qualitative TAM/pricing-power and moat-signal evidence, which require cited sources (filings, third-party reports) — never inferred.

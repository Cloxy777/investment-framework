# RESCORE — Veeva Systems (VEEV) — 2026-08-30

**Task type:** RESCORE — earnings-triggered ([issue #651](https://github.com/Cloxy777/investment-framework/issues/651), Q2 FY2027 results, released 2026-08-26, due 2026-08-31, **P2** — 1.22% weight <5%)
**Date:** 30 Aug 2026 | **10Y Treasury:** 4.72% (live, CBOE TNX) | **Rate Regime Modifier:** +5

> *Jargon on first use: FCF = free cash flow; ROIC = return on invested capital; EV/EBIT = enterprise value ÷ operating profit; PEG = PE ÷ EPS growth rate; PW = probability-weighted; E = expected annual return; MoS = margin of safety.*

## 1. Live Price (Rule 0)

**$276.65** (IBKR live snapshot, contract 136254493, 2026-08-30), down −1.94% vs. prior close $282.13 — up further from issue #651's pre-fill price ($265.00 on 8/26), on top of that day's own +7.38% earnings pop. No Rule 9 price-move trigger on its own; earnings is the trigger here.

## 2. Quality Score (refresh — last computed 85.7 on 2026-07-01)

```
Net Margin 29.3% | ROIC 374.6% (as-reported, near-zero invested-capital artifact — clamps regardless of adjustment method)
Gross Margin 75.0% | Rev 3yr CAGR (FY23→FY26, $2,155M→$3,195M) = (3195/2155)^(1/3)−1 = 14.04%
Net Debt/EBITDA ≈ −46.8x (extreme net cash) | FCF positive: FY24 $885M / FY25 $1,070M / FY26 $1,386M — yes
FCF/NI (FY26): 1,386/908.91 = 152.5%
```

```
Profitability_Score  = (clamp(29.3/30×100) + clamp(374.6/30×100))/2 = (97.67+100.0)/2 = 98.84
GrossMargin_Score    = clamp(75.0/80×100) = 93.75
Growth_Score (raw)   = clamp(14.04/25×100) = 56.16
  + TAM modifier +10: Vault CRM mandatory-migration wave (cited, 07-01 session — runs through 2026–2029) is a
    documented structural growth driver, and FY26 revenue growth accelerated to +16.34% YoY — no deceleration
    evidence. → Growth_Score = 66.16
BalanceSheet_Score   = clamp(100×(1−(−46.8)/4)) = clamp(1270,0,100) = 100.0
Moat_Score           = 60.0  (3/5, carried forward from 07-01 — no new citation found this session to move it:
                        market share TRUE [47 of top 50 pharma; ~80% niche share], network effect TRUE [Veeva
                        Network/OpenData shared reference database], switching costs TRUE [21 CFR Part 11
                        revalidation cost]; brand premium and scale cost advantage remain FALSE, no citation)
FCFQuality_Score     = clamp(((1.525−0.40)/0.60)×100) = clamp(187.5,0,100) = 100.0

Quality Score = 98.84×0.25 + 93.75×0.15 + 66.16×0.20 + 100.0×0.15 + 60.0×0.15 + 100.0×0.10
              = 24.71 + 14.06 + 13.23 + 15.00 + 9.00 + 10.00 = 86.00
```

**Quality Score: 86.0 — passes the 80.0+ gate** (vs. 85.7 prior — essentially unchanged, marginal improvement).

## 3. Valuation Score

**Not a Fast Grower** — carried forward from 07-01: FY2024 NI growth (+7.8%) breaks the "3+ consecutive years >15%" clean-base test within the current trailing window (FY24–FY26), even though FY25 (+35.8%) and FY26 (+27.3%) both clear it individually. PEG's 15% weight redistributed to EV/EBIT (→40%).

```
FCF Yield ≈4.0% (issue's 4.2% at $265.00, price-adjusted to $276.65) → FCF_Score = clamp(100×(1−4.0/10)) = 60.0
EV/EBIT 36.44× (stockanalysis.com, live) → EV/EBIT_Score = clamp((36.44−12)/23×100) = clamp(106.3,0,100) = 100.0
Forward PE 28.68×; 5yr avg PE 43.59× (carried from 07-01, average-only, no range — fallback formula)
  Deviation% = (28.68−43.59)/43.59×100 = −34.19%
  FwdPE_Score = clamp(50 + (−34.19)×2.5, 0, 100) = clamp(−35.5,0,100) = 0.0 (floor)

Raw weighted = 60.0×0.40 + 100.0×0.40 + 0.0×0.20 = 24.0 + 40.0 + 0 = 64.0
+ Rate Regime Modifier (+5) = 69.0
```

**Upside/Downside Modifier:**
```
Bull (25%, analyst high $330) / Base (50%, analyst mean $294.07) / Bear (25%, 15% below analyst low $250 → $212.50,
  per this framework's below-Street-low bear discipline)
PW Fair Value = 0.25×330 + 0.50×294.07 + 0.25×212.50 = $282.66
Gap Upside % = (282.66/276.65) − 1 = +2.17%
Catalyst window: Vault CRM migration runs through 2029 — past the 18–24mo guardrail window, so upside credit is
  capped at −5 magnitude (guardrail 1); using the default 2yr annualization anyway: Annualized gap = 2.17/2 = +1.09%/yr
Intrinsic growth = +12.0%/yr (conservative, below FY26's actual +16.34% YoY)
Shareholder yield = 0% (no dividend; buyback trend not independently re-derived this session — data gap, not invented)
E = 1.09 + 12.0 + 0 = +13.09%/yr
M = −15 × clamp((13.09−10)/15, 0, 1) = −15 × 0.206 = −3.1   (guardrail cap doesn't bind — |−3.1| < 5)
```

```
FINAL VALUATION SCORE = 69.0 − 3.1 = 65.9
```

## 4. Composite Score

```
Composite = 0.50×(100−86.0) + 0.50×65.9 = 7.00 + 32.95 = 39.95 → rounds UP to 40.0
```

**Composite Score: 40.0** ("Standard position, 3–5%" band, 30.0–49.9) — vs. 29.7 on 2026-07-01. Notably more expensive than two months ago (price up, and the EV/EBIT re-rated to the 100.0 ceiling) — a real shift, not noise.

## 5. Order Setup & Action

```
Blended FV (proxy, PW scenario value) ≈ $282.66
Buy Price = FV × (1 − 0.275 MoS midpoint of the 25–30% Score-30-49.9 band) = 282.66 × 0.725 = $204.93
```

Live price **$276.65 is well above the $204.93 buy ceiling** — no entry/add is justified at the current price under this framework's own order-setup discipline, even though the Composite Score nominally sits in the "set limit order" band. VEEV is held at **1.22%**, well under the 3–5% target range for this score band, but the gap between live price and buy ceiling (−26%) means there's no live order to place today.

**Recommendation: HOLD, no add.** Set a mental/limit watch near **~$205** — a pullback of that magnitude would clear the order-setup math and open room to build toward the 3–5% target. No thesis-invalidation trigger fired this quarter (margins, growth, and moat evidence all intact or improved post-earnings).

## Glossary

- **FCF / FCF Yield / FCF/NI** — free cash flow; FCF ÷ EV; FCF ÷ Net Income.
- **ROIC** — Return on Invested Capital.
- **EV/EBIT** — Enterprise Value ÷ operating profit.
- **PEG** — PE ÷ EPS growth rate.
- **PW (Probability-Weighted) Fair Value** — 25% bull + 50% base + 25% bear blend.
- **MoS (Margin of Safety)** — discount below fair value required before buying.
- **Quality Score / Composite Score** — this framework's graded quality score (80.0+ gate) and 50/50 Quality+Valuation blend.

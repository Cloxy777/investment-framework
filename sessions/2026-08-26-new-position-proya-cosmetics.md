# NEW POSITION — Proya Cosmetics (603605.SH) — 2026-08-26

**Task type:** NEW POSITION (candidate evaluation, not currently held)
**Source:** EM screening slice, 2026-08-25 ([issue #630](https://github.com/Cloxy777/investment-framework/issues/630), [session](2026-08-25-screening-emerging-markets.md)) — new candidate this pass, clean 8/8 Phase 01 quantitative pass, but **explicitly flagged there as not a clean qualitative pass** — see below.
**Date:** 26 Aug 2026

> *Jargon decoded on first use: FCF = free cash flow; ROIC = return on invested capital; EV/EBIT = enterprise value ÷ operating profit; CAGR = compound annual growth rate; TAM = total addressable market; PE = price-to-earnings ratio; EPS = earnings per share; CAC = customer acquisition cost.*

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **¥63.26** | stockanalysis.com, 2026-08-26 3:00 PM CST (Shanghai market close) |
| Cross-check | ¥63.26 (Google Finance, timestamp Aug 26 4:30:00 PM GMT+8) — exact match | WebFetch, same day |
| 52-week range | ¥54.30 – ¥92.00 | stockanalysis.com |
| Analyst consensus PT | ¥82.83 (+30.94% upside potential) — bull-case sanity check only, not used in scoring | stockanalysis.com |

Not held in the current portfolio — no broker-position cross-check applicable.

---

## 2. Phase 01 Quality Score ([quality-scoring.md](../framework/quality-scoring.md))

Quantitative inputs (FY2025) carried forward from the 2026-08-25 EM screening session's Step 2 (verified there against stockanalysis.com); qualitative evidence from that session's Step 3, which explicitly flagged this as **"NOT a clean qualitative pass"** despite the clean quantitative gate:

```
Net Margin (FY25):            14.13%
ROIC (FY25):                  67.06%
Gross Margin (FY25):          72.56%  (screening session's qualitative note cites 73.26% for the same period — minor cross-page rounding/basis discrepancy on stockanalysis.com; using the tabulated Phase 01 quantitative figure, 72.56%, for the formula below)
Revenue 3yr CAGR (FY22→FY25): 18.40%  — (10,597/6,385)^(1/3)−1, CNY millions — see §3 below: this trailing figure is flagged as stale, carried by 2022–2024 growth that has since reversed
Net Debt/EBITDA (FY25):       −2.24x  (net cash position)
FCF positive 3yr:             Yes — FY25 CNY 2,024M / FY24 807.26M / FY23 1,289M (all positive)
FCF/NI ratio (FY25):          2,024 / 1,498 = 135.1%
FCF/NI ratio (FY24):          807.26 / 1,552 = 52.0%   ← below 70%
```

**Hard disqualifiers check:** the FCF/NI ratio dipped to 52.0% in FY2024 (below the 70% disqualifier threshold), but FY2023 (107.9%) and FY2025 (135.1%) are both comfortably above it — only **1** of the last several years is below 70%, not the "2+ consecutive years" the hard disqualifier requires. **No hard disqualifier fires**, but the single-year dip is noted as a data point worth watching, not a smooth trend. Net Debt/EBITDA is negative (net cash) — clear. FCF-positive 3+ consecutive years — clear.

### Sub-scores

**Profitability (25% weight):**
```
NetMargin_Component = clamp((14.13/30)×100, 0, 100) = 47.10
ROIC_Component       = clamp((67.06/30)×100, 0, 100) = clamp(223.53, 0, 100) = 100.00
Profitability_Score  = (47.10 + 100.00) / 2 = 73.55   (no FCF cap — 3yr positive)
```

**Margins (15% weight):**
```
GrossMargin_Score = clamp((72.56/80)×100, 0, 100) = 90.70
```
No structural-expansion bonus — that bonus is specifically for margins *below* the 40% threshold that are trending up; Proya's is already well above 40%, so it doesn't apply regardless of the (modestly rising, per the qualitative note) trend.

**Growth (20% weight):**
```
Growth_Score (raw) = clamp((18.40/25)×100, 0, 100) = 73.60
```
**Structural deceleration modifier: −10 (the central finding of this evaluation).** The 2026-08-25 screening session documented, with cited sources (Bloomberg, Global Cosmetics News, Proya's own reported results), that **FY2025 was Proya's first-ever revenue and profit decline as a public company** (revenue −1.68% to RMB 10.597bn, net profit −3.5% to RMB 1.498bn), driven by the flagship brand (>70% of revenue) falling 10.39% — and that **the decline continued into Q1 2026** (revenue −2.29%, net profit −6.05%). This is materially stronger evidence than either PDD's or ANTA's growth-modifier inputs this session: not a deceleration in growth rate, but two consecutive periods of outright decline, explicitly attributed to structural causes (rising CAC on a shrinking base, a domestic rival — KANS — outgrowing Proya sharply via a livestream-content format shift, and ~98.7% revenue concentration in mainland China). The trailing 18.40% 3yr CAGR that cleared the Phase 01 gate is a historical artifact of 2022–2024 growth and does not reflect the current trend.
```
Growth_Score = clamp(73.60 − 10, 0, 100) = 63.60
```

**Balance Sheet (15% weight):**
```
BalanceSheet_Score = clamp(100 × (1 − (−2.24)/4), 0, 100) = clamp(156.0, 0, 100) = 100.0
```

**Moat Signal (15% weight)** — checklist, each signal markable TRUE only against a cited source:

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **FALSE** | Cited evidence points the opposite direction: Proya's flagship brand fell 10.4% in FY2025 while domestic rival KANS took the #1 Douyin beauty ranking through most of 2024 with 80.9% revenue growth — a documented share *loss*, not a stable/growing position. |
| Brand premium | **TRUE** | Cited: gross margin has been rising (a genuine mid-price-tier formulation/brand pricing-power effect, explicitly distinguished in the source from a scale-driven explanation) — pricing-power evidence, even though the gains are being partly consumed by rising distribution cost elsewhere (a Growth/Margins-level issue, not a reason to discount the pricing-power citation itself). |
| Network effect | **FALSE** | Not applicable to this business model; not cited. |
| Switching costs | **FALSE** | Explicitly cited as *absent*: "Consumer switching costs are low — closer to an attention/platform-cycle business than a durable brand-loyalty franchise." |
| Scale cost advantage | **FALSE** | No cost-per-unit citation; the cited trend runs the other way — sales-expense ratio climbed to 49.63% of revenue (from 46.78%), i.e. rising, not falling, customer-acquisition cost. |

```
Moat_Score = (1/5) × 100 = 20.0
```

**FCF Quality (10% weight):**
```
FCF/NI ratio (FY25) = 135.1%
FCFQuality_Score = clamp(((1.351 − 0.40)/0.60)×100, 0, 100) = clamp(158.5, 0, 100) = 100.0
```

### Quality Score

```
Quality Score = (73.55 × 0.25) + (90.70 × 0.15) + (63.60 × 0.20) + (100.0 × 0.15) + (20.0 × 0.15) + (100.0 × 0.10)
              = 18.3875 + 13.605 + 12.720 + 15.000 + 3.000 + 10.000
              = 72.7125 → rounds to 72.7
```

**Quality Score: 72.7 — FAILS the 80.0+ gate**, the widest margin of the three EM candidates evaluated this session (7.3 points, vs. PDD's 1.7 and ANTA's 4.5).

---

## 3. Verdict

Proya is the clearest of this session's three EM fails. It clears the Phase 01 quantitative gate cleanly (8/8), driven mostly by a trailing 3yr revenue CAGR (18.40%) that is now stale — the 2026-08-25 screening session's own qualitative pass found, and this session's Growth-modifier and Moat-signal scoring confirms, that the underlying momentum has already broken: two consecutive periods of outright revenue and profit *decline* (FY2025 and Q1 2026, not just decelerating growth), a documented share loss to a faster-moving domestic rival, and a moat that rests on distribution/content execution within platforms Proya doesn't control rather than durable brand loyalty (only 1 of 5 signals cited true — the pricing-power one, and even that is being partly eroded by rising customer-acquisition cost). Balance sheet and FCF quality remain strong, but they're the two lowest-weighted sub-scores (15% and 10%) and can't offset the combined drag from Growth, Moat, and Profitability.

**Recommendation: PASS — and not a knife-edge one.** Consistent with the screening session's own explicit caution, this name should not be entered off its trailing quantitative numbers. Per the framework's standard "Next review trigger" discipline: watch FY2026 results (due ~April 2027) for whether the flagship brand stabilizes or the decline deepens; a positive resolution of the pending Hong Kong secondary listing (raising capital for the still-unproven ~1.3%-of-revenue international expansion) is the other concrete catalyst that could eventually change this read, but there's no evidence yet that it has.

---

## Glossary

- **FCF** — Free cash flow.
- **ROIC** — Return on Invested Capital.
- **EV/EBIT** — Enterprise Value ÷ operating profit.
- **CAGR** — Compound Annual Growth Rate.
- **TAM** — Total Addressable Market.
- **Moat** / **Moat Signal** — durable competitive advantage; this framework's 5-point checklist scoring it.
- **Quality Score** — this framework's 0.0–100.0 graded score (80.0+ required to proceed to valuation).
- **Net Debt/EBITDA** — leverage ratio; net debt ÷ operating cash profit.
- **EPS** — Earnings Per Share.
- **PE** — Price-to-earnings ratio.
- **CAC** — Customer acquisition cost (marketing/distribution spend needed to win each new customer).

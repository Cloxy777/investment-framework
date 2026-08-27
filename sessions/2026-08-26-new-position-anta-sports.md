# NEW POSITION — ANTA Sports Products (2020.HK) — 2026-08-26

**Task type:** NEW POSITION (candidate evaluation, not currently held)
**Source:** EM screening slice, 2026-08-25 ([issue #630](https://github.com/Cloxy777/investment-framework/issues/630), [session](2026-08-25-screening-emerging-markets.md)) — clean 8/8 Phase 01 quantitative pass, carried forward from the 2026-08-04 EM round.
**Date:** 26 Aug 2026

> *Jargon decoded on first use: FCF = free cash flow; ROIC = return on invested capital; EV/EBIT = enterprise value ÷ operating profit; CAGR = compound annual growth rate; TAM = total addressable market; PE = price-to-earnings ratio; EPS = earnings per share; DTC = direct-to-consumer.*

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **HK$78.75** | stockanalysis.com, close 2026-08-26 4:08 PM HKT (HK market already closed for the session at the time of this evaluation) |
| Cross-check | HK$78.75 (Google Finance, timestamp Aug 26 4:08:03 PM GMT+8) — exact match | WebFetch, same day |
| 52-week range | HK$66.85 – HK$106.30 | stockanalysis.com |
| Analyst consensus PT | HK$102.89 (32 analysts, "Strong Buy") — bull-case sanity check only, not used in scoring | stockanalysis.com |

Not held in the current portfolio (IBKR or Freedom24) — no broker-position cross-check applicable.

---

## 2. Phase 01 Quality Score ([quality-scoring.md](../framework/quality-scoring.md))

Quantitative inputs (FY2025) carried forward from the 2026-08-25 EM screening session's Step 2 (verified there against stockanalysis.com's financials/ratios/cash-flow pages); qualitative evidence from that session's Step 3 (refreshed for developments since the 2026-08-04 round, including resolution of an apparent margin-compression flag as a comparison-base accounting artifact — see that session for detail):

```
Net Margin (FY25):            16.94%
ROIC (FY25):                  22.35%
Gross Margin (FY25):          62.00%  (−0.2pp YoY — genuine mix-shift toward technical/premium product + e-commerce, not compression)
Revenue 3yr CAGR (FY22→FY25): 14.35%  — (80,219/53,651)^(1/3)−1, CNY millions
Net Debt/EBITDA (FY25):       −0.37x  (net cash position)
FCF positive 3yr:             Yes — FY25 CNY 18,491M / FY24 14,483M / FY23 18,473M (all positive)
FCF/NI ratio (FY25):          18,491 / 13,588 = 136.1%
FCF/NI ratio (FY24):          14,483 / 15,596 = 92.9%
```

**Hard disqualifiers check:** FCF/NI ratio comfortably above 70% in both of the last 2 fiscal years — clear. Net Debt/EBITDA is negative (net cash) — clear. FCF-positive 3+ consecutive years — clear. **No hard disqualifier fires.**

### Sub-scores

**Profitability (25% weight):**
```
NetMargin_Component = clamp((16.94/30)×100, 0, 100) = 56.47
ROIC_Component       = clamp((22.35/30)×100, 0, 100) = 74.50
Profitability_Score  = (56.47 + 74.50) / 2 = 65.48   (no FCF cap — 3yr positive)
```

**Margins (15% weight):**
```
GrossMargin_Score = clamp((62.00/80)×100, 0, 100) = 77.50
```
No structural-expansion bonus applies — gross margin is already well above the 40% threshold the bonus is meant to reward when *below* it, and the FY25 move was −0.2pp (essentially flat / a mix-shift artifact per the screening session), not an expansion.

**Growth (20% weight):**
```
Growth_Score (raw) = clamp((14.35/25)×100, 0, 100) = 57.40
```
**TAM expansion modifier: +10.** The 2026-08-25 screening session documented, with cited sources (Bloomberg, ANTA's own IR release), a pending €1.5bn (~$1.8bn) acquisition of a 29.06% stake in Puma SE — a material extension of ANTA's addressable market beyond China into a second, larger global sportswear franchise, funded entirely from internal cash. This is a documented, cited TAM-expansion event, not an inference. No offsetting structural-deceleration evidence was found strong enough to net against it: Arc'teryx's China growth is moderating off a hyper-growth base (still +36% YoY per Amer Sports' own Aug 18, 2026 commentary) but management frames this as expected normalization, not competitive erosion — materially different in kind from PDD's cited 86%→8% deceleration evaluated earlier this session.
```
Growth_Score = clamp(57.40 + 10, 0, 100) = 67.40
```

**Balance Sheet (15% weight):**
```
BalanceSheet_Score = clamp(100 × (1 − (−0.37)/4), 0, 100) = clamp(109.25, 0, 100) = 100.0
```

**Moat Signal (15% weight)** — checklist, each signal markable TRUE only against a cited source:

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | Cited: ANTA holds ~23% of the China sportswear market; ANTA + Li-Ning together account for 28% of sneaker sales; Nike's China sales are cited as continuing to decline over the same period — a documented relative-share gain, not just a level. |
| Brand premium | **TRUE** | Cited: multi-brand pricing power via a premium/technical product mix (Arc'teryx, Salomon) is explicitly identified as the reason margins are high — pricing power evidence, not inferred. |
| Network effect | **FALSE** | No two-sided marketplace or user-growth-driven network dynamic applies to a multi-brand apparel manufacturer/retailer — not cited, not applicable to this business model. |
| Switching costs | **FALSE** | No documented contractual lock-in, integration depth, or migration cost cited for either consumers or retail partners. |
| Scale cost advantage | **TRUE** | Cited: a 12,000+-touchpoint DTC (direct-to-consumer) distribution network — a genuine scale-driven distribution-cost/reach advantage documented in the sourced material, consistent with how this framework has credited analogous distribution-scale evidence elsewhere (e.g. MCD's AUV citation). |

```
Moat_Score = (3/5) × 100 = 60.0
```

**FCF Quality (10% weight):**
```
FCF/NI ratio (FY25) = 136.1%
FCFQuality_Score = clamp(((1.361 − 0.40)/0.60)×100, 0, 100) = clamp(160.2, 0, 100) = 100.0
```

### Quality Score

```
Quality Score = (65.48 × 0.25) + (77.50 × 0.15) + (67.40 × 0.20) + (100.0 × 0.15) + (60.0 × 0.15) + (100.0 × 0.10)
              = 16.371 + 11.625 + 13.480 + 15.000 + 9.000 + 10.000
              = 75.476 → rounds to 75.5
```

**Quality Score: 75.5 — FAILS the 80.0+ gate.**

---

## 3. Verdict

ANTA clears every individual Phase 01 quantitative threshold (8/8, confirmed 2026-08-25) and has the strongest moat evidence of the three EM candidates evaluated this session (3 of 5 signals, all cited, including a genuine documented share gain against Nike) — but the strict 80.0+ gate isn't primarily a moat test. What holds the score back here is **Profitability (65.5)**: net margin of 16.94%, while comfortably above the Phase 01 12% floor, is well short of the 30% level that would score 100 on this sub-score's continuous scale, and it's weighted 25% — the single heaviest input. Growth (67.4, even after the +10 TAM credit for the Puma stake) is the second drag. Balance sheet and FCF quality are both effectively perfect (net cash, FCF/NI well above 100%).

**Recommendation: PASS.** Not eligible for entry under this framework's current methodology, regardless of price. The pending Puma stake (expected to close by end of 2026) is the most concrete forward catalyst — if it closes and begins contributing profit, both the Growth sub-score (a second, larger growth engine) and the Profitability sub-score (assuming margin-accretive integration) could move meaningfully in a future re-check. ANTA's own H1 2026 interim results (board meeting scheduled 2026-08-26, the day of this session — not yet public as of this evaluation) are the nearest-term data point worth pulling into the next pass.

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
- **DTC** — Direct-to-consumer (a distribution channel that bypasses third-party retailers).

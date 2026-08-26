# NEW POSITION — Rightmove plc (RMV.L) — 2026-08-26

**Task type:** NEW POSITION (candidate evaluation, not currently held)
**Source:** EU screening slice, 2026-08-08 ([issue #490](https://github.com/Cloxy777/investment-framework/issues/490), [session](2026-08-08-screening-europe.md)) — new candidate that round, clean 8/8 Phase 01 quantitative pass.
**Date:** 26 Aug 2026

> *Jargon decoded on first use: FCF = free cash flow; ROIC = return on invested capital; ROE = return on equity; EV/EBIT = enterprise value ÷ operating profit; CAGR = compound annual growth rate; TAM = total addressable market; PE = price-to-earnings ratio; EPS = earnings per share; ARPA = average revenue per advertiser; CMA = the UK's Competition and Markets Authority.*

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **511.40p (£5.114)** | Google Finance, LSE, close 2026-08-26 5:30 PM BST — explicitly labelled GBX (pence) |
| Cross-check | 509.00 (stockanalysis.com, 4:49 PM GMT, ~40 min earlier) — labelled "GBP" on that page but this is a unit-labelling artifact, not a real discrepancy: at a literal £509/share the implied market cap (509 × 739.83M shares) would be ~£376.6bn, absurd for a company stockanalysis.com's own page lists at £3.81B market cap; £3.81B ÷ 739.83M shares = £5.15/share, consistent with the pence reading. Both sources agree once read in the same unit (GBX). | WebFetch, same day |
| 52-week range | 391.40p – 775.40p | stockanalysis.com |
| Analyst consensus PT | 546.26p (+7.32% upside), consensus rating "Hold" — bull-case sanity check only, not used in scoring | stockanalysis.com |

Not held in the current portfolio — no broker-position cross-check applicable.

---

## 2. Phase 01 Quality Score ([quality-scoring.md](../framework/quality-scoring.md))

Quantitative inputs (FY2025) carried forward from the 2026-08-08 EU screening session's Step 2 (verified there against stockanalysis.com); qualitative evidence from that session's Step 3.

```
Net Margin (FY25):            51.06%
ROIC (FY25):                  656.40%  (near-zero invested-capital base after years of buybacks — confirmed a real artifact, not a sourcing error, per the screening session)
Gross Margin (FY25):          100.00%  (asset-light portal — stockanalysis.com's "Gross Profit" line equals total revenue, no separately reported COGS; a labelling convention, not a literal 100% margin in the traditional sense — same flag the screening session raised for Adyen)
Revenue 3yr CAGR (FY22→FY25): 8.53%
Net Debt/EBITDA (FY25):       −0.13x   (net cash)
FCF positive:                 Yes — FY25 £235.4M / FY24 £210.22M / FY23 £204.69M (all positive)
FCF/NI ratio (FY25):          235.4 / 217.07 = 108.4%
FCF/NI ratio (FY24):          210.22 / 192.71 = 109.1%
```

**Hard disqualifiers check:** FCF/NI ratio comfortably above 70% — clear. Net Debt/EBITDA is negative (net cash) — clear. FCF-positive multiple consecutive years — clear. **No hard disqualifier fires.**

### Sub-scores

**Profitability (25% weight):**
```
NetMargin_Component = clamp((51.06/30)×100, 0, 100) = clamp(170.2, 0, 100) = 100.0
ROIC_Component       = clamp((656.40/30)×100, 0, 100) = clamp(2188.0, 0, 100) = 100.0
Profitability_Score  = (100.0 + 100.0) / 2 = 100.0   (no FCF cap)
```

**Margins (15% weight):**
```
GrossMargin_Score = clamp((100.00/80)×100, 0, 100) = clamp(125.0, 0, 100) = 100.0
```

**Growth (20% weight):**
```
Growth_Score (raw) = clamp((8.53/25)×100, 0, 100) = 34.12
```
**TAM expansion modifier: +10.** The 2026-08-08 screening session's qualitative pass documented, with cited reasoning, concrete growth vectors beyond the core listings business: continued ARPA (average revenue per advertiser) growth from richer agent data/marketing packages, expansion into new-homes and commercial-property adjacent verticals, and mortgage/financial-services lead-generation cross-sell — genuine, cited TAM-expansion evidence. No offsetting structural-deceleration evidence was found (the bear case centers on housing-cycle *cyclicality*, not a documented structural decline).
```
Growth_Score = clamp(34.12 + 10, 0, 100) = 44.12
```

**Balance Sheet (15% weight):**
```
BalanceSheet_Score = clamp(100 × (1 − (−0.13)/4), 0, 100) = clamp(103.25, 0, 100) = 100.0
```

**Moat Signal (15% weight)** — checklist, each signal markable TRUE only against a cited source. **This is the most consequential judgment call in this evaluation — see §3.**

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | Cited: "highest visitor traffic of any UK property-search site," and "the UK has effectively had the same 2–3 incumbent portals... for over a decade despite well-funded challenges — OnTheMarket was explicitly agent-backed to unseat Rightmove and never did." A decade of unchanged category leadership against a well-funded, purpose-built challenger is real evidence of a stable position, even without a numeric market-share percentage. |
| Brand premium | **FALSE** | No cited pricing-power evidence (a documented price increase sustained without agent attrition, specifically). |
| Network effect | **TRUE** | Explicitly and directly cited: "asset-light... with the highest visitor traffic of any UK property-search site, creating a two-sided network effect: more listings attract more buyers/renters, which attracts more agents." Textbook, sourced network-effect mechanism. |
| Switching costs | **FALSE** | The cited "chicken-and-egg" dynamic is a barrier to new-entrant *acquisition* (already captured under network effect), not a documented lock-in mechanism for existing agents (no contractual/integration-depth/data-migration-cost citation). |
| Scale cost advantage | **FALSE** | No cost-per-unit citation distinct from what's already captured in the Margins/Balance Sheet scores. |

```
Moat_Score = (2/5) × 100 = 40.0
```

**FCF Quality (10% weight):**
```
FCF/NI ratio (FY25) = 108.4%
FCFQuality_Score = clamp(((1.084 − 0.40)/0.60)×100, 0, 100) = clamp(114.0, 0, 100) = 100.0
```

### Quality Score

```
Quality Score = (100.0 × 0.25) + (100.0 × 0.15) + (44.12 × 0.20) + (100.0 × 0.15) + (40.0 × 0.15) + (100.0 × 0.10)
              = 25.000 + 15.000 + 8.824 + 15.000 + 6.000 + 10.000
              = 79.824 → rounds to 79.8
```

**Quality Score: 79.8 — FAILS the 80.0+ gate by 0.2 points — the closest miss of any candidate evaluated this session** (closer even than PDD's 1.7-point miss).

---

## 3. Verdict — and where this call could tip the other way

Rightmove has the strongest overall profile of any candidate evaluated this session: perfect Profitability, Margins, Balance Sheet, and FCF Quality sub-scores (100.0, 100.0, 100.0, 100.0), a genuinely cited two-sided network-effect moat, and a decade-plus track record of fending off both organic and M&A-backed challenges (including four rebuffed takeover approaches from REA Group). What holds it under the gate is almost entirely the **Growth sub-score (44.12)** — an 8.53% 3yr revenue CAGR is real but modest on the 25%-ceiling continuous scale — combined with a **Moat Score (40.0)** that only credits 2 of 5 signals under this session's evidentiary standard.

**This is a 0.2-point miss, and the closest single judgment call is the "Market share stable or growing" signal.** It was marked TRUE on qualitative category-leadership evidence (traffic leadership, a decade of unchanged competitive structure) rather than a numeric share percentage — a slightly looser evidentiary bar than, e.g., this session's ANTA evaluation (which had an explicit ~23%-share citation). Marking it FALSE instead — which would be defensible under the strictest possible reading — drops Moat_Score to 20.0, taking the Quality Score to 76.8 (a bigger miss). Conversely, if a future session can source a genuine numeric UK online-portal market-share/traffic-share figure, or evidence of switching costs specific to agent-side data integration, either would likely push this over the 80.0 line on its own. **Flagged explicitly rather than resolved by picking whichever reading clears the gate — the "never invent" discipline cuts against manufacturing a third moat signal just to cross the line.**

**Recommendation: PASS — but the single closest re-test candidate of this session's six.** Not eligible for entry under the current methodology as computed today. Given the 0.2-point margin, this is worth a fresh, more rigorously sourced moat pass (specifically: a cited numeric market/traffic-share figure) before the next scheduled EU screening rotation, rather than waiting for it by default.

---

## Glossary

- **FCF** — Free cash flow.
- **ROIC** — Return on Invested Capital.
- **ROE** — Return on Equity.
- **EV/EBIT** — Enterprise Value ÷ operating profit.
- **CAGR** — Compound Annual Growth Rate.
- **TAM** — Total Addressable Market.
- **Moat** / **Moat Signal** — durable competitive advantage; this framework's 5-point checklist scoring it.
- **Quality Score** — this framework's 0.0–100.0 graded score (80.0+ required to proceed to valuation).
- **Net Debt/EBITDA** — leverage ratio; net debt ÷ operating cash profit.
- **EPS** — Earnings Per Share.
- **PE** — Price-to-earnings ratio.
- **ARPA** — Average Revenue Per Advertiser (Rightmove's per-agent revenue metric).
- **CMA** — the UK's Competition and Markets Authority (antitrust/competition regulator).

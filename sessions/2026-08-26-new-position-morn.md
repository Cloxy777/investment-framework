# NEW POSITION — Morningstar, Inc. (MORN) — 2026-08-26

**Task type:** NEW POSITION (candidate evaluation, not currently held)
**Source:** NA-2 screening slice, 2026-08-15 ([issue #551](https://github.com/Cloxy777/investment-framework/issues/551), [session](2026-08-15-screening-na2.md)) — clean 8/8 Phase 01 quantitative pass, the only one of 16 valid candidates on that slice to clear the full gate.
**Date:** 26 Aug 2026

> *Jargon decoded on first use: FCF = free cash flow; ROIC = return on invested capital; EV/EBIT = enterprise value ÷ operating profit; CAGR = compound annual growth rate; TAM = total addressable market; PE = price-to-earnings ratio; EPS = earnings per share; AUM = assets under management.*

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$212.22** | Interactive Brokers live snapshot (contract 34415020, NASDAQ), 2026-08-26, −1.3% vs. prior close $215.01 |
| Cross-check | $212.26 (stockanalysis.com, 12:39 PM EDT) / $212.21 (Google Finance, 12:56:34 PM GMT-4) | WebFetch, same day — all three sources agree to within $0.05 |
| 52-week range | $141.49 – $265.73 | stockanalysis.com |
| Analyst consensus PT | $236.67 (+11.5% upside) — bull-case sanity check only, not used in scoring | stockanalysis.com |

Not held in the current portfolio (IBKR or Freedom24) — no live snapshot cross-check against a broker position was applicable beyond the price pull itself.

---

## 2. Phase 01 Quality Score ([quality-scoring.md](../framework/quality-scoring.md))

Quantitative inputs (FY2025) carried forward from the 2026-08-15 NA-2 screening session's Step 2 (verified there against stockanalysis.com); qualitative evidence from that session's Step 3.

```
Net Margin (FY25):            15.30%
ROIC (FY25):                  18.24%
Gross Margin (FY25):          61.03%
Revenue 3yr CAGR (FY22→FY25): 9.34%
Net Debt/EBITDA (FY25):       2.03x   (real leverage — not a net-cash position, unlike this session's 3 EM candidates)
FCF positive:                 Yes, 5 consecutive years (per screening session)
FCF/NI ratio (FY25):          442.6 / 374.2 = 118.3%
FCF/NI ratio (FY24):          448.9 / 369.9 = 121.4%
```

**Hard disqualifiers check:** FCF/NI ratio well above 70% in the last 2 fiscal years (and every year back to FY22: 238.7%, 139.8%) — clear. Net Debt/EBITDA at 2.03x is under the 2.5× standard threshold — clear. FCF-positive 5 consecutive years — clear. **No hard disqualifier fires.**

### Sub-scores

**Profitability (25% weight):**
```
NetMargin_Component = clamp((15.30/30)×100, 0, 100) = 51.00
ROIC_Component       = clamp((18.24/30)×100, 0, 100) = 60.80
Profitability_Score  = (51.00 + 60.80) / 2 = 55.90   (no FCF cap — 5yr positive)
```

**Margins (15% weight):**
```
GrossMargin_Score = clamp((61.03/80)×100, 0, 100) = 76.29
```
No structural-expansion bonus — margin is already above the 40% threshold the bonus targets, and no specific multi-year gross-margin trend was cited (the qualitative pass focused on net-margin recovery from the 2022 dip, not gross margin specifically).

**Growth (20% weight):**
```
Growth_Score (raw) = clamp((9.34/25)×100, 0, 100) = 37.36
```
**TAM expansion modifier: +10.** The 2026-08-15 screening session's qualitative pass documented, with cited detail, continued PitchBook penetration into private-markets research (an explicitly named "secular AUM growth area") plus expansion of Morningstar Indexes and Sustainalytics ESG data — genuine TAM-expansion evidence, not inferred. Unlike this session's PDD and Proya evaluations, revenue grew every year through the cited 2022→2025 recovery window (net margin rose from 3.77% in 2022 to 15.30% now on growing, not shrinking, revenue) — so no offsetting structural-deceleration penalty applies; the active-to-passive fund-shift headwind cited in the bear case is a real risk to one legacy segment, not evidence the *company's* growth trajectory is currently declining.
```
Growth_Score = clamp(37.36 + 10, 0, 100) = 47.36
```

**Balance Sheet (15% weight):**
```
BalanceSheet_Score = clamp(100 × (1 − 2.03/4), 0, 100) = clamp(50.75, 0, 100) = 50.75
```
The one sub-score where MORN reads meaningfully weaker than this session's other three candidates (all net-cash) — real leverage from disciplined-but-real bolt-on M&A (PitchBook 2016, DBRS 2019, Sustainalytics 2020).

**Moat Signal (15% weight)** — checklist, each signal markable TRUE only against a cited source:

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **FALSE** | No cited numeric share or share-trend figure — "industry-standard reference point" is a positioning claim, not a share-trend citation. Not marked true without one. |
| Brand premium | **FALSE** | No cited pricing-power evidence (a price increase sustained without volume loss, or a documented premium vs. competitors) — the qualitative pass describes embeddedness in advisor workflows, which is closer to a switching-cost argument than a pricing-power one. |
| Network effect | **FALSE** | Not applicable to this business model; not cited. |
| Switching costs | **TRUE** | Cited directly: "A challenger would need a multi-decade proprietary fund/security database and a ratings methodology already embedded as the industry-default reference point in advisor and asset-manager workflows and client-facing materials — genuine switching costs." |
| Scale cost advantage | **TRUE** | Cited: "Margins come from software/data economics — the marginal cost of serving one more subscriber against an already-built database and research organization is low" — a documented scale-driven cost-structure mechanism. |

```
Moat_Score = (2/5) × 100 = 40.0
```

**FCF Quality (10% weight):**
```
FCF/NI ratio (FY25) = 118.3%
FCFQuality_Score = clamp(((1.183 − 0.40)/0.60)×100, 0, 100) = clamp(130.5, 0, 100) = 100.0
```

### Quality Score

```
Quality Score = (55.90 × 0.25) + (76.29 × 0.15) + (47.36 × 0.20) + (50.75 × 0.15) + (40.0 × 0.15) + (100.0 × 0.10)
              = 13.975 + 11.4435 + 9.472 + 7.6125 + 6.000 + 10.000
              = 58.503 → rounds to 58.5
```

**Quality Score: 58.5 — FAILS the 80.0+ gate**, by the widest margin of any of the four candidates evaluated this session (21.5 points).

---

## 3. Verdict

MORN was the cleanest Phase 01 quantitative pass of any candidate this session — the only one of 16 valid names on its screening slice to clear all 8 filters — but the graded Quality Score tells a very different story. Two things drive the gap: **Growth (47.36)** — a real, non-cyclical 9.34% 3yr revenue CAGR is respectable but well short of what the continuous scale rewards, and the active-to-passive structural headwind on Morningstar's legacy research business (explicitly named in its own bear case) means the growth outlook isn't a slam dunk even with the PitchBook/ESG/indexes diversification credited above; and **Balance Sheet (50.75)** — MORN is the only one of this session's four candidates carrying real leverage (2.03× Net Debt/EBITDA) rather than a net-cash position, the direct cost of its disciplined-but-real bolt-on M&A strategy (PitchBook, DBRS, Sustainalytics). Moat (40.0, 2/5 — genuine switching costs and scale economics, but no cited pricing-power or market-share evidence) and Profitability (55.9, ROIC 18.24% solid but not exceptional relative to the 30% ceiling) round out a Quality Score that misses the 80.0 bar by a wide margin, not a knife-edge one.

**Recommendation: PASS.** Not eligible for entry under this framework's current methodology. Unlike this session's three EM candidates (all within 1.7–7.3 points of the gate), MORN's 21.5-point miss reflects a genuinely different quality profile — solid, profitable, well-run, but not the kind of high-70s/low-80s Quality Score business this framework's other near-miss candidates represent. A re-check would need real movement on Growth or Balance Sheet (continued deleveraging, or a demonstrable acceleration from the PitchBook/ESG/indexes diversification) rather than a single data point — worth revisiting at the next NA-2 screening rotation rather than on an accelerated timeline.

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
- **AUM** — Assets Under Management (the total value of client capital a fund/investment manager oversees).

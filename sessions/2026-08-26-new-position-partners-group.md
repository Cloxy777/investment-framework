# NEW POSITION — Partners Group Holding AG (PGHN.SW) — 2026-08-26

**Task type:** NEW POSITION (candidate evaluation, not currently held)
**Source:** EU screening slice, 2026-08-08 ([issue #490](https://github.com/Cloxy777/investment-framework/issues/490), [session](2026-08-08-screening-europe.md)) — new candidate that round, clean 8/8 Phase 01 quantitative pass.
**Date:** 26 Aug 2026

> *Jargon decoded on first use: FCF = free cash flow; ROIC = return on invested capital; EV/EBIT = enterprise value ÷ operating profit; CAGR = compound annual growth rate; TAM = total addressable market; PE = price-to-earnings ratio; EPS = earnings per share; AUM = assets under management; LP = limited partner (an institutional investor in a private-markets fund).*

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **CHF 735.60** | stockanalysis.com, 2026-08-26 5:30 PM CET |
| Cross-check | CHF 735.60 (Google Finance, timestamp Aug 26 5:58:21 PM GMT+2) — exact match | WebFetch, same day |
| 52-week range | CHF 632.40 – CHF 1,158.00 | stockanalysis.com |
| Analyst consensus PT | CHF 820.77 (+11.58% upside), consensus "Hold" — bull-case sanity check only, not used in scoring | stockanalysis.com |

Not held in the current portfolio — no broker-position cross-check applicable.

---

## ⚠️ Data-quality correction found this session — Net Debt/EBITDA

The 2026-08-08 EU screening session's Phase 01 table cites Partners Group's Net Debt/EBITDA as **0.30×** (implying a light-leverage, near-net-cash position). Re-pulling the balance sheet directly this session (stockanalysis.com's balance-sheet page) shows:

```
FY2025 (Dec 31, 2025): Cash & ST Investments CHF 328.8M, Total Debt CHF 2,486M
                        → Net Debt = CHF 2,486M − 328.8M = CHF 2,157M  (a real net DEBT position, not net cash)
```

Live ratios page (same source, today): **current Net Debt/EBITDA = 1.37×**, EV/EBIT 13.55×, EV CHF 20,876M. Solving back: EBITDA ≈ 2,157 / 1.37 ≈ CHF 1,574M — consistent with an implied EBIT of ≈ CHF 1,541M from the EV/EBIT figure (20,876/13.55), i.e. the 1.37× figure reconciles internally against two independently-sourced numbers, while the screening session's 0.30× does not reconcile against either. **This session uses the verified 1.37×, not the screening session's 0.30×.** Both values are still comfortably under the Phase 01 <2.5× threshold, so this doesn't change the *quantitative gate* pass/fail call — but it materially changes the graded Quality Score's Balance Sheet sub-score below, since that sub-score is continuous rather than a threshold pass/fail. Flagged for a future correction pass on the 2026-08-08 screening session's own record.

---

## 2. Phase 01 Quality Score ([quality-scoring.md](../framework/quality-scoring.md))

Quantitative inputs (FY2025) carried forward from the 2026-08-08 EU screening session's Step 2 (Net Debt/EBITDA corrected per above); qualitative evidence from that session's Step 3.

```
Net Margin (FY25):            49.19%
ROIC (FY25):                  47.96%
Gross Margin (FY25):          68.18%
Revenue 3yr CAGR (FY22→FY25): 11.05%
Net Debt/EBITDA (FY25):       1.37×   (corrected — see data-quality note above)
FCF positive 3yr:             Yes — FY25 CHF 1,507M / FY24 CHF 819.6M / FY23 CHF 541.1M (all positive)
FCF/NI ratio (FY25):          1,507 / 1,261 = 119.5%
FCF/NI ratio (FY24):          819.6 / 1,128 = 72.7%
FCF/NI ratio (FY23):          541.1 / 1,003 = 53.9%   ← below 70%
```

**Hard disqualifiers check:** FCF/NI ratio dipped to 53.9% in FY2023, but FY2024 (72.7%) and FY2025 (119.5%) are both above 70% — only 1 non-consecutive year below the threshold, not "2+ consecutive years." No disqualifier fires on this basis. Net Debt/EBITDA at 1.37× is under the 2.5× standard threshold — clear. FCF-positive 3+ consecutive years — clear. **No hard disqualifier fires**, though the FY2023 FCF/NI dip is noted as real volatility, consistent with this business's cyclical performance-fee exposure (see qualitative bear case below).

### Sub-scores

**Profitability (25% weight):**
```
NetMargin_Component = clamp((49.19/30)×100, 0, 100) = clamp(163.97, 0, 100) = 100.0
ROIC_Component       = clamp((47.96/30)×100, 0, 100) = clamp(159.87, 0, 100) = 100.0
Profitability_Score  = (100.0 + 100.0) / 2 = 100.0   (no FCF cap — 3yr positive)
```

**Margins (15% weight):**
```
GrossMargin_Score = clamp((68.18/80)×100, 0, 100) = 85.23
```
No structural-expansion bonus — margin is already well above the 40% threshold the bonus targets, and no multi-year expansion trend was cited.

**Growth (20% weight):**
```
Growth_Score (raw) = clamp((11.05/25)×100, 0, 100) = 44.20
```
**TAM expansion modifier: +10.** The 2026-08-08 screening session documented, with cited detail, a concrete and ambitious growth trajectory: AUM targeted to grow from $186B today to $450B by 2033, a record $16B of fresh capital commitments in H1 2026 alone, and expansion into evergreen/semi-liquid private-markets vehicles explicitly aimed at the wealth-management channel — a structural, industry-wide "democratization of private markets" growth vector, not a one-off. This is the most concretely quantified TAM-expansion citation of any candidate evaluated this session. No offsetting deceleration evidence — the bear case centers on performance-fee *cyclicality* (guided to the low end of the 25–40%-of-revenue range for 2026), not a structural growth decline.
```
Growth_Score = clamp(44.20 + 10, 0, 100) = 54.20
```

**Balance Sheet (15% weight):**
```
BalanceSheet_Score = clamp(100 × (1 − 1.37/4), 0, 100) = clamp(65.75, 0, 100) = 65.75
```
Using the corrected 1.37× (see data-quality note) — the screening session's uncorrected 0.30× would have given 92.5 here, a 26.75-point swing on this sub-score alone.

**Moat Signal (15% weight)** — checklist, each signal markable TRUE only against a cited source:

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | Cited, quantitative: AUM at $186B as of 30 June 2026, a record $16B of fresh capital commitments in H1 2026 alone, and a targeted path to $450B by 2033 — real, sourced, growing scale for an asset manager (AUM is the standard scale/market-position metric for this business model). |
| Brand premium | **FALSE** | No cited fee-rate premium vs. peers or pricing-power evidence specifically. |
| Network effect | **FALSE** | Not applicable to this business model; not cited. |
| Switching costs | **TRUE** | Cited directly: "long-duration locked-up private-markets fund structures (typically 8–12yr) reduce redemption risk" — a genuine, documented lock-in mechanism; LP capital cannot easily migrate to a competitor mid-fund. |
| Scale cost advantage | **TRUE** | Cited directly: "high operating leverage since incremental AUM adds little incremental headcount" — a documented mechanism by which the marginal cost of managing additional capital is low, a real scale-driven cost-structure advantage. |

```
Moat_Score = (3/5) × 100 = 60.0
```

**FCF Quality (10% weight):**
```
FCF/NI ratio (FY25) = 119.5%
FCFQuality_Score = clamp(((1.195 − 0.40)/0.60)×100, 0, 100) = clamp(132.5, 0, 100) = 100.0
```

### Quality Score

```
Quality Score = (100.0 × 0.25) + (85.23 × 0.15) + (54.20 × 0.20) + (65.75 × 0.15) + (60.0 × 0.15) + (100.0 × 0.10)
              = 25.000 + 12.7845 + 10.840 + 9.8625 + 9.000 + 10.000
              = 77.487 → rounds to 77.5
```

**Quality Score: 77.5 — FAILS the 80.0+ gate (by 2.5 points).**

Note for the record: had this session used the screening session's uncorrected Net Debt/EBITDA figure (0.30×), the Balance Sheet sub-score would have been 92.5 instead of 65.75, and the Quality Score would have computed to **81.5 — a PASS.** The corrected, verified balance-sheet figure is what's used and reported here — this is exactly the kind of case Rule 0's "never invent or estimate, verify the live data" discipline exists for, and it changed the actual outcome, not just a footnote.

---

## 3. Verdict

Partners Group has the strongest overall fundamentals of any candidate evaluated this session — perfect Profitability (100.0) and FCF Quality (100.0), a strong Margins score (85.23), and the best-supported Moat read across all six candidates (3 of 5 signals, each with a distinct, concrete, cited mechanism: growing AUM, multi-year fund lock-ups, and operating-leverage-driven scale economics). It is genuinely close to the gate — 2.5 points short — and would have cleared it entirely on the (erroneous) leverage figure carried over from the original screening session. With the corrected, verified Net Debt/EBITDA of 1.37×, the real leverage load (funding partly the CHF 46.00/share FY2025 dividend, per the balance sheet) is enough on its own to hold the Quality Score under 80.0.

**Recommendation: PASS, and the closest "real" miss of this session after Rightmove's 0.2-point gap** — but unlike Rightmove, this one isn't a moat-signal judgment call, it's a corrected data input. Not eligible for entry under the current methodology as computed today. The clearest re-check trigger: continued deleveraging (net debt was already lower a year earlier — FY2024's CHF 1,855M vs. FY2025's CHF 2,157M — moved the *wrong* direction this past year, worth understanding why before assuming it reverses) would directly move the Balance Sheet sub-score and could close the gap on its own, without needing any other input to change.

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
- **AUM** — Assets Under Management.
- **LP (Limited Partner)** — an institutional investor (pension fund, endowment, sovereign wealth fund, etc.) that commits capital to a private-markets fund.

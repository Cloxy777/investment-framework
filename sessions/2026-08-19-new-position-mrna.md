# New Position Evaluation — MRNA (Moderna, Inc.)

**Task type:** NEW POSITION
**Date:** 19 Aug 2026
**10Y US Treasury Yield:** 4.70% ([tradingeconomics.com](https://tradingeconomics.com/united-states/government-bond-yield), 2026-08-19)
**Rate Regime Modifier (would apply if scored):** +5 (3.5–5% band) — not applied; evaluation stops at the Quality Gate, see below.

**Trigger:** Routine 6 (Telegram-scan), FinnInvestChannel post #3118, ~14:48 UTC 2026-08-19 — reported Moderna and Merck's Phase 3 melanoma cancer-vaccine data. **The Telegram post text is used only as a trigger, never as financial data (per CLAUDE.md).** All quantitative inputs below were independently pulled live from Yahoo Finance (`quoteSummary` + `fundamentals-timeseries` endpoints, cookie/crumb-authenticated) at the time of this session. The clinical catalyst itself was independently verified via `WebSearch` (see Rule 9 Catalyst Note, below) and is treated strictly as a **qualitative note, not a scored input** — consistent with valuation-scoring.md's "Why Forward Guidance Is Not a Sub-score" principle (self-reported/unaudited topline trial results carry the same discipline as management guidance).

---

## 1. Live Price (Rule 0)

Fetched intraday, 2026-08-19 16:12 UTC, Yahoo Finance real-time quote (NasdaqGS, market state REGULAR):

| Field | Value |
|---|---|
| **Current Price** | **$146.29** |
| Previous Close | $62.96 |
| Regular-session change | +$83.33 (**+132.35%**) |
| Day Range | $114.46 – $163.47 |
| 52-Week Range | $22.28 – $163.47 (new 52-week high set intraday) |
| Volume (intraday, partial session) | 116.6M shares (vs. 6.88M 3-month average — ~17× normal) |
| Market Cap | $58.40B |
| Enterprise Value | $21.28B |

This is a genuine, extreme single-day move (+132%), consistent with the Telegram trigger's characterization of a major positive Phase 3 readout. Cross-checked against 52-week high ($163.47, hit intraday today) and the abnormal volume — internally consistent with a real news-driven repricing, not a data error. Per Rule 0, this live price (not the previous close, not any inferred value) is used throughout.

---

## 2. Phase 01 — Quality Score (quality-scoring.md)

### Quantitative inputs (all live-pulled, Yahoo Finance `fundamentals-timeseries` + `quoteSummary`, sourced 2026-08-19)

| Metric | FY2022 | FY2023 | FY2024 | FY2025 | TTM (through Q2 2026) |
|---|---|---|---|---|---|
| Revenue | $18,875M | $6,754M | $3,199M | $1,922M | $2,228M |
| Net Income | $8,362M | −$4,714M | −$3,561M | −$2,822M | −$3,151M |
| Gross Profit | $13,459M | $2,061M | $1,735M | $1,054M | −$1,471M |
| Gross Margin | 71.3% | 30.5% | 54.2% | 54.8% | **−66.0%** |
| EBIT | $9,420M | −$4,239M | −$3,583M | −$2,758M | n/a (TTM EBIT not separately available) |
| EBITDA | $9,768M | −$3,618M | −$3,394M | −$2,543M | −$2,195M |
| Operating Cash Flow | $4,981M | −$3,118M | −$3,004M | −$1,873M | −$1,073M |
| Free Cash Flow | $4,581M | **−$3,825M** | **−$4,055M** | **−$2,075M** | **−$1,244M** |
| Total Debt | $1,200M | $1,243M | $747M | $1,305M | $1,287M |
| Cash & Equivalents | $3,205M | $2,907M | $1,927M | $2,595M | $5,138M |
| Invested Capital | $19,123M | $13,854M | $10,901M | $9,240M | — |

TTM net margin −141.43%, TTM Net Income −$3,151M, TTM Revenue $2,228M (Yahoo `financialData` module, cross-checked against the timeseries API's `trailingNetIncome`/annual figures — internally consistent).

**Note on the TTM gross-margin anomaly:** the swing from a positive FY2025 gross margin (54.8%) to a negative TTM figure (−66.0%) was independently verified quarter-by-quarter, not assumed — Q1 2026 (period ended 2026-03-31) alone posted a **−$566M** gross loss on just $389M of revenue against $955M of cost of revenue, consistent with an inventory write-down/reserve on unsold COVID-era vaccine doses as demand continues to collapse. This is real, filed data (Yahoo `quarterlyGrossProfit`/`quarterlyCostOfRevenue`), not a data error.

### Hard Disqualifiers ([quality-scoring.md](../framework/quality-scoring.md)) — checked FIRST, rolling window = FY2023–FY2025 (most recent 3 completed fiscal years) + TTM

| Disqualifier | Result |
|---|---|
| **Not FCF-positive for 3+ consecutive years** | **FIRES.** FCF was negative in FY2023 (−$3,825M), FY2024 (−$4,055M), FY2025 (−$2,075M), and remains negative on a TTM basis (−$1,244M) — four consecutive negative readings, not one. No carve-out exists for this disqualifier (per glossary.md: "the FCF-positivity check has none"). |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | **FIRES.** Net Income has been negative for 3 consecutive fiscal years (2023–2025) plus TTM — the ratio is either undefined or, where both numerator and denominator are negative (TTM: −$1,244M / −$3,151M = 39.5%), still far under the 70% bar and reflects sustained cash-burning operations, not merely a timing/working-capital quirk. No documented growth-capex explanation applies — MRNA's capex has actually been *shrinking* (FY2024 $1,051M → FY2025 $202M), the opposite of a growth-investment story. |
| **Net Debt/EBITDA over its applicable threshold** | **Not meaningfully computable** — MRNA holds a net **cash** position (TTM: $5,138M cash vs. $1,287M debt = **$3,851M net cash**), which is a genuine balance-sheet strength, but EBITDA is also negative (TTM −$2,195M; FY2025 −$2,543M), so the ratio (negative ÷ negative) produces a positive number that does **not** carry its normal "years to pay off debt" meaning. Flagged N/M (Not Meaningful) rather than scored either way — see glossary.md's N/M entry. This disqualifier is not the basis for failing the gate; the two above already are. |

**Two independent hard disqualifiers fire.** Per quality-scoring.md: *"A weighted average can't average away an outright balance-sheet or cash-flow-quality failure."* Per operating-brief.md and this session's instructions: **when a hard disqualifier fires, STOP — do not proceed to Phase 02 valuation scoring, regardless of how cheap the stock looks** (and MRNA, at a TTM EV/Revenue of ~9.6x on collapsing revenue, does not look cheap either).

### Full Quality Score calculation (computed anyway, for transparency — "no black-box outputs")

**Profitability (25% weight)** — TTM Net Margin −141.43%, ROIC computed off FY2025 (most recent completed fiscal year) EBIT and Invested Capital:
```
NOPAT (FY2025) = EBIT × (1 − tax rate) = −$2,758M × (1 − 0.21) = −$2,178.8M
ROIC (FY2025)  = NOPAT ÷ Invested Capital = −$2,178.8M ÷ $9,240M = −23.58%

NetMargin_Component = clamp((−141.43/30)×100, 0, 100) = 0.0
ROIC_Component       = clamp((−23.58/30)×100, 0, 100) = 0.0
Profitability_Score  = (0.0 + 0.0) / 2 = 0.0
  (FCF-positive-3yr cap of 40.0 also independently applies here — moot, already at floor)
```

**Margins (15% weight)** — TTM Gross Margin −66.02%:
```
GrossMargin_Score = clamp((−66.02/80)×100, 0, 100) = 0.0
No structural-expansion bonus: margin trend is volatile/declining (71.3% → 30.5% → 54.2% → 54.8% → −66.0%), not a documented structural improvement.
Margins_Score = 0.0
```

**Growth (20% weight)** — Revenue 3yr CAGR, FY2022 ($18,875M) → FY2025 ($1,922M), rolling 3-year window:
```
CAGR = (1,922 / 18,875)^(1/3) − 1 = (0.1019)^(0.333) − 1 = −53.30%
Growth_Score = clamp((−53.30/25)×100, 0, 100) = 0.0
No TAM/pricing-power modifier applied — no cited evidence of expansion; this is a documented structural COVID-vaccine-demand collapse, not TAM growth. (A −10 structural-deceleration modifier would also apply but is moot — already at floor.)
```

**Balance Sheet (15% weight)** — flagged N/M above; shown for completeness only, using the TTM figures (more generous of the two available bases):
```
Net Debt (TTM)     = $1,287M − $5,138M = −$3,851M (net cash)
Net Debt/EBITDA    = −$3,851M ÷ −$2,195M = 1.754×  [NOT MEANINGFUL — both terms negative]
BalanceSheet_Score (literal formula) = clamp(100×(1 − 1.754/4), 0, 100) = 56.1
```

**Moat Signal (15% weight)** — checklist, no signal marked true without cited evidence:
| Signal | True/False | Evidence |
|---|---|---|
| Market share stable/growing | False | COVID-vaccine revenue/share has collapsed (−90% off FY2022 peak); no cited data shows share stable or growing in any product line |
| Brand premium | False | No cited pricing-power evidence (price increases without volume loss) located |
| Network effect | False | Not applicable to a vaccine/therapeutics business model |
| Switching costs | False | Not applicable — no cited lock-in mechanism for patients/payers |
| Scale cost advantage | False | No cited cost-per-dose data vs. competitors |
```
Moat_Score = (0/5) × 100 = 0.0
```

**FCF Quality (10% weight)**:
```
FCF/NI ratio (TTM) = −$1,244M ÷ −$3,151M = 39.48%
FCFQuality_Score = clamp(((39.48−40)/60)×100, 0, 100) = 0.0
```

### Final Quality Score

```
Quality Score = (0.0×0.25) + (0.0×0.15) + (0.0×0.20) + (56.1×0.15) + (0.0×0.15) + (0.0×0.10)
              = 0.0 + 0.0 + 0.0 + 8.42 + 0.0 + 0.0
              = 8.4
```

**Quality Score: 8.4 / 100.0 — fails the 80.0+ gate by a wide margin**, independent of, and in addition to, the two hard disqualifiers already firing above.

---

## 3. STOP — Evaluation Halted at Phase 01

Per [quality-scoring.md](../framework/quality-scoring.md): *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all. Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."* MRNA fails on **three independent grounds**:

1. Hard disqualifier — not FCF-positive for 3+ consecutive years (fired).
2. Hard disqualifier — FCF/Net Income conversion ratio deeply impaired for 2+ consecutive years, no growth-capex carve-out applies (fired).
3. Quality Score 8.4, far below the 80.0+ gate even computed in full.

**No Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order setup is computed.** Doing so would be scoring a company the framework's own gate says is disqualified — not a "cheap but lower quality" trade-off, but a company currently burning cash across every profitability and cash-flow dimension the Quality Score measures, on a business (COVID-era vaccine franchise) in structural, multi-year revenue collapse.

---

## 4. Rule 9 Catalyst Note (qualitative only — NOT a scored input)

Independently verified via `WebSearch` (not taken on the Telegram post's word):

Merck and Moderna announced on **2026-08-19** that the Phase 3 **INTerpath-001** trial of **intismeran autogene** (Moderna's individualized neoantigen therapy) plus **KEYTRUDA** (Merck's pembrolizumab) met both its primary endpoint (**RFS**, Recurrence-Free Survival) and a key secondary endpoint (**DMFS**, Distant Metastasis-Free Survival) in patients with completely resected Stage IIB–IV melanoma, at a pre-specified **interim analysis**. The **topline results** release did not disclose the hazard ratio, p-values, or full underlying data — those are expected at a future medical conference. Safety was described as consistent with prior studies, no new signals. Trial enrolled 1,137 patients, randomized 2:1 to combination vs. KEYTRUDA alone, ~1 year of treatment.

**Why this doesn't change the Phase 01 outcome:** this is a pipeline/regulatory catalyst for a therapy still in Phase 3 (not yet FDA-approved, not yet generating revenue), while the Quality Score and hard disqualifiers are built entirely from MRNA's *current, filed* financials — a currently deeply cash-burning, revenue-collapsing business. A positive Phase 3 readout is genuine good news for the pipeline's long-run optionality, but per valuation-scoring.md's "Why Forward Guidance Is Not a Sub-score" principle, forward-looking / self-reported / not-yet-monetized items are tracked as **triggers for future re-evaluation**, never baked into the current quantitative score. If intismeran autogene is ultimately approved and reaches meaningful revenue, a future re-evaluation (a fresh `/new-position` run, since MRNA is not and will not become a holding from this session) would need to show FCF-positive fundamentals return before the Quality Gate could plausibly be cleared — that is a multi-year, unwritten future, not something to be underwritten today.

**Sources:**
- [Merck and Moderna Announce Phase 3 INTerpath-001 Trial... — Moderna](https://news.modernatx.com/merck-and-moderna-announce-phase-3-interpath-001-trial-of-intismeran-plus-keytruda-met-endpoints-of-rfs-and-dmfs-in-melanoma)
- [Merck and Moderna Announce Phase 3 INTerpath-001 Trial... — Merck.com](https://www.merck.com/news/merck-and-moderna-announce-phase-3-interpath-001-trial-of-intismeran-autogene-plus-keytruda-met-endpoints-of-recurrence-free-survival-rfs-and-distant-metastasis-free-survival-dmfs-in-patient/)
- [Merck, Moderna's personalized cancer vaccine slows recurrence in phase 3 — Fierce Biotech](https://www.fiercebiotech.com/biotech/merck-and-modernas-personalized-cancer-vaccine-slows-recurrence-ph-3-trial)

---

## 5. Recommendation

**PASS — do not enter. Watchlist-only entry created** (per this framework's convention of logging every `/new-position` evaluation, scored or not, in `watchlist/not-in-portfolio/`).

- **Quality Gate: FAILED** (Quality Score 8.4 / 100.0; two independent hard disqualifiers fired: FCF not positive 3+ consecutive years, FCF/NI conversion impaired 2+ consecutive years with no growth-capex carve-out).
- **Composite Score: not computed** — Phase 02 is never reached for a company that fails Phase 01's gate.
- The framework's gate exists precisely to prevent exactly this situation: a name with a loud, real, positive news catalyst and a huge one-day price pop, but fundamentals that are currently the opposite of what the Quality Score is built to reward. See [glossary.md](../framework/glossary.md)'s **Value trap** entry.

**Next review trigger:** No standing trigger set — MRNA is not a holding, so it is not on the quarterly re-score cadence. A future re-evaluation would be warranted on: (a) intismeran autogene / mRNA oncology pipeline reaching FDA approval and material commercial revenue, (b) MRNA returning to FCF-positive operations for a sustained period (the specific hard disqualifier that fired here), or (c) another Telegram-scan / Rule 9 fundamental trigger.

---

## Data Gaps Flagged

None block this evaluation's conclusion (the hard disqualifiers and Quality Score already definitively fail the gate on live, complete data), but for completeness:
- **Hazard ratio / full INTerpath-001 statistical data** — not yet disclosed by Merck/Moderna (topline-only release); not needed for this session's quantitative conclusion, since Phase 3 pipeline data is a qualitative catalyst note only, never a scored input, per valuation-scoring.md.
- **Moat Signal evidence** — all 5 signals scored False for lack of a cited source (not because they're necessarily untrue, but because "never mark a signal true without a cited source" — quality-scoring.md). Immaterial to the outcome since the Quality Score already fails by a wide margin (8.4 vs. 80.0 threshold) on the other four sub-scores plus the hard disqualifiers.
- Phase 02 valuation inputs (5yr PE range, PEG, DCF assumptions, peer multiples) were **not pulled**, consistent with the instruction to stop at the gate rather than proceed to valuation scoring for a disqualified company.

---

## Glossary

*(New terms added to [glossary.md](../framework/glossary.md) in this session are marked accordingly.)*

- **Adjuvant therapy** — cancer treatment given after primary treatment (surgery) to reduce recurrence risk.
- **CAGR (Compound Annual Growth Rate)** *(see glossary.md)* — the smoothed annual growth rate implied by a start and end value over a period.
- **DMFS (Distant Metastasis-Free Survival)** — clinical-trial endpoint measuring time to cancer spreading to a distant body part, or death.
- **EBIT / EBITDA** *(see glossary.md)* — operating profit before interest/tax, and before interest/tax/depreciation/amortization respectively.
- **Enterprise Value (EV)** *(see glossary.md)* — market cap plus net debt; the theoretical takeover cost of a company.
- **FCF (Free Cash Flow) / FCF/NI conversion ratio** *(see glossary.md)* — cash a business generates after capital spending; and the ratio checking whether accounting profit is turning into real cash.
- **Hard disqualifier** *(see glossary.md)* — one of three Quality Score conditions that fails a company regardless of weighted score.
- **Hazard ratio** — a clinical-trial statistic comparing event rates between a treatment and control group.
- **Interim analysis** — a pre-planned early look at trial data before the trial fully matures.
- **INTerpath-001** — the specific Phase 3 trial name for Moderna/Merck's melanoma combination study.
- **Intismeran autogene** — Moderna's individualized, mRNA-based personalized cancer (neoantigen) vaccine.
- **Invested Capital** *(see glossary.md)* — total capital (debt + equity, net of cash) put to work in a business; ROIC's denominator.
- **KEYTRUDA (pembrolizumab)** — Merck's approved PD-1 checkpoint-inhibitor immunotherapy, the combination partner in the trial.
- **N/M (Not Meaningful)** *(see glossary.md)* — this framework's flag for a formula input that's structurally undefined for a given case (here, Net Debt/EBITDA with negative EBITDA).
- **Neoantigen** — a new, tumor-specific protein the immune system can be trained to target.
- **Net Debt/EBITDA** *(see glossary.md)* — leverage ratio; this framework's primary balance-sheet-risk gate.
- **Net Margin / Gross Margin** *(see glossary.md)* — profitability ratios; Net Income or Gross Profit divided by Revenue.
- **NOPAT** *(see glossary.md)* — EBIT × (1 − tax rate); the numerator of this framework's ROIC calculation.
- **Phase 3 (clinical trial)** — the final, large-scale stage of human drug testing before an FDA approval filing.
- **Quality Score / Quality Gate** *(see glossary.md)* — this framework's 0–100.0 Phase 01 score; a company must score 80.0+ to proceed to valuation.
- **RFS (Recurrence-Free Survival)** — clinical-trial endpoint measuring time until a cancer recurs, or death; the trial's primary endpoint here.
- **ROIC (Return on Invested Capital)** *(see glossary.md)* — how efficiently a company turns invested capital into profit.
- **Rolling-window (disqualifier test)** *(see glossary.md)* — this framework's convention of testing hard disqualifiers against the most recently completed fiscal years, not a fixed historical window.
- **Topline results** — the initial, high-level summary of a clinical trial's outcome, released before full underlying data.
- **TTM (Trailing Twelve Months)** *(see glossary.md)* — the most recent 12 months of reported results.
- **Value trap** *(see glossary.md)* — a stock that looks cheap/newsworthy but whose underlying business quality doesn't support it; what this framework's Quality Gate is designed to catch.

# New Position Evaluation — AAOI (Applied Optoelectronics, Inc.)

**Task:** NEW POSITION
**Date:** 14 Aug 2026
**10Y US Treasury Yield:** 4.65% (most recent available close, 13 Aug 2026 — TradingEconomics/FRED-sourced; **informational only**, since Phase 02 is never reached — see below)
**Rate Regime (informational only, not applied):** 3.5–5% band → would be a +5 modifier if a valuation score were computed
**Trigger:** Direct user request — no prior watchlist entry existed for AAOI (checked `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/`, confirmed absent), so this is a first-ever, full end-to-end `/new-position` evaluation.

---

## 1. Data gaps flagged

- **TTM EBITDA could not be fully reconstructed from quarterly operating-income line items** — several individual quarterly GAAP operating-loss figures (Q2 2025, Q3 2025, Q4 2025) were not available from the sources checked (SEC EDGAR blocked WebFetch with 403; some press-release pages timed out). Real, sourced figures **were** obtained for Q1 2025 (−$8.937M), Q1 2026 (−$12.991M) and Q2 2026 (−$24.7M) operating loss, and for full-year FY2025 EBIT (−$54.60M, from FY2025 audited annual data) and FY2025 D&A ($27.7M). The Balance Sheet sub-score below therefore uses the most recent **complete fiscal year** (FY2025 EBITDA) rather than a partially-reconstructed TTM figure, clearly flagged as such — this is a real, sourced number, not an invented one, but is a fiscal-year-lagged rather than fully trailing-twelve-month figure. This does not change the session's outcome (see §3 — the Quality Gate fails by a wide margin and on an independent hard disqualifier regardless of this sub-score's exact value; a sensitivity check with the alternate reading is shown).
- **Moat Signal evidence**: only 1 of 5 signals could be backed by a citable, documented source within this session (the general datacenter-optics supplier-qualification-cycle mechanism, already established for peers LITE/COHR in this framework). The other 4 are marked FALSE for lack of a citation found in this session, not asserted false as fact.
- None of these gaps affect the outcome — the Quality Score fails the 80.0+ gate by a wide margin (43.4 vs. 80.0, or 28.4 under the stricter Balance Sheet reading) and a hard disqualifier fires independently of the weighted score either way.

---

## 2. Live Price (Rule 0)

Fetched directly from IBKR real-time market data (not inferred from multiples), at the time of this session (14 Aug 2026, regular NASDAQ session, live/real-time):

| Field | Value |
|---|---|
| **Live price (intraday, real-time)** | **$149.69** |
| Change vs. prior close | +$19.61 (**+15.08%**) |
| Today's range | $130.34 – $153.39 (open $130.39) |
| 52-week range | $18.50 – $233.67 |
| 52-week high date | 13 May 2026 (all-time high) |
| Today's volume | ~8.96M shares |
| Bid / Ask | $149.50 / $149.73 |
| Analyst consensus PT | ~$147–158 (sources vary; range $109 low – $220 high; B. Riley $109 Neutral, Raymond James $178 raised 11 Aug 2026) |

**Context (not scored, qualitative only):** AAOI reported Q2 2026 results on 6 Aug 2026 (record revenue, return to *non-GAAP* profitability, strong Q3 guidance) and has continued to re-rate sharply higher since — today's +15.08% move extends a multi-week run of analyst price-target increases and continued enthusiasm around its 800G/1.6T AI-datacenter-optics ramp. No single confirmed same-day catalyst beyond continued post-earnings momentum was identified. This is noted for context only — it does not affect the Quality Score gate result below, which is fundamentals-driven, not price-driven, per Rule 9/the "never act on price movement alone" non-negotiable. *(Sources: [StockTitan Q2 2026 release](https://www.stocktitan.net/news/AAOI/applied-optoelectronics-reports-second-quarter-2026-wjz4h91d9ngj.html), [GuruFocus Q2 2026 earnings highlights](https://www.gurufocus.com/news/9015363/applied-optoelectronics-inc-aaoi-q2-2026-earnings-call-highlights-record-revenue-and-aidriven-growth-propel-return-to-profitability).)*

---

## 3. Phase 01 — Quality Score (0–100.0)

Per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29. All figures below are **real, filed GAAP figures** sourced from AAOI's own press releases/8-K exhibits and cross-checked against stockanalysis.com's financial-statement pages — never non-GAAP/adjusted figures, per this framework's "guidance/self-reported non-GAAP metrics are not scored" principle (see [valuation-scoring.md](../framework/valuation-scoring.md) "Why Forward Guidance Is Not a Sub-score").

### Hard disqualifiers — checked first

| Disqualifier | Result | Evidence |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | **FIRES** | Annual FCF (GAAP): FY2021 −$19.63M, FY2022 −$17.23M, FY2023 −$8.59M, FY2024 −$112.93M, FY2025 −$353.58M, TTM (through Q2 2026) −$592.23M. **FCF has never been positive in any of the last 5 fiscal years or the current TTM window** — the disqualifier fires unconditionally, with no partial-window ambiguity of the kind the 2026-08-05 rolling-window clarification addresses. |
| Net Debt/EBITDA over threshold (2.5×) | Not decisive either way — see Balance Sheet sub-score below | Current (Q2 2026) balance sheet shows a **net cash** position (~$235M net cash: $499.74M cash vs. $264.54M total debt), following a ~$382.4M net-proceeds public equity offering completed in H1 2026. But FY2025 EBITDA is negative (−$26.90M = EBIT −$54.60M + D&A $27.70M), which breaks the ratio's usual "leverage" interpretation — flagged, not treated as passing or failing outright (see §3 Balance Sheet). |
| FCF/NI conversion ratio <70% for 2+ consecutive years, no growth-capex explanation | Fires on the literal math for FY2021–FY2024, mitigated by a documented growth-capex explanation | FY2021 ratio 36.3%, FY2022 25.9%, FY2023 15.3%, FY2024 60.5% — all <70% (both FCF and NI negative in each year, so the ratio of two negatives is positive but small). However, there **is** a documented growth-capex explanation: AAOI began a ~$300M, ~400,000 sq ft expansion of its Pearland, TX manufacturing campus in 2026 to ramp 800G/1.6T production, and TTM CapEx of $460.41M is roughly 2.6× FY2025's already-elevated $179.15M — a real, cited capacity buildout. This mitigates the *second* disqualifier specifically, consistent with how the same carve-out was applied in the 2026-07-28 LITE session — but doesn't rescue AAOI, since the *first* disqualifier above fires unconditionally with no such carve-out. *(Source: [Seeking Alpha, "A 60% Reset Opportunity"](https://seekingalpha.com/article/4926728-applied-optoelectronics-a-60-percent-reset-opportunity-rating-upgrade).)* |

**Result: hard disqualifier fires (not FCF-positive 3+ consecutive years — in fact, not FCF-positive in *any* of the last 5 years).** Per [quality-scoring.md](../framework/quality-scoring.md), this fails the company regardless of the weighted score below. The full weighted calculation is still shown in full per "no black-box outputs."

### Sub-score calculations

**Profitability (25% weight)**
```
TTM Revenue (Jul25–Jun26) = $595.97M
TTM Net Income = FY2025 (−38.2M) − Q1'25 (−9.2M) − Q2'25 (−9.1M) + Q1'26 (−14.3M) + Q2'26 (−22.8M) = −$57.0M
TTM Net Margin = −57.0 / 595.97 = −9.57%
TTM ROIC = −1.55% (sourced directly, stockanalysis.com ratios page)

NetMargin_Component = clamp((−9.57/30)×100, 0, 100) = 0.0   (negative, floored)
ROIC_Component       = clamp((−1.55/30)×100, 0, 100)  = 0.0   (negative, floored)
Profitability_Score  = (0.0 + 0.0) / 2 = 0.0
```
The "not FCF-positive 3 years → cap Profitability at 40.0" rule also applies here, but is moot — 0.0 is already below the 40.0 cap.

**Margins (15% weight)**
```
TTM Gross Margin = 28.92%
GrossMargin_Score = clamp((28.92/80)×100, 0, 100) = 36.15
```
No structural-trend bonus applied. Gross margin history: FY2021 17.83% → FY2022 15.09% → FY2023 27.07% → FY2024 24.78% → FY2025 30.04% → TTM 28.92%. The multi-year trend has improved overall, but the **most recent three quarters are contracting sequentially and YoY** (Q2 2025 30.3% → Q1 2026 29.1% → Q2 2026 27.7% GAAP, partly attributed by the company itself to discontinued-product costs) — this is not the clean, sustained structural expansion the +10 modifier requires, so it is not applied. *(Source: [StockTitan Q2 2026 release](https://www.stocktitan.net/news/AAOI/applied-optoelectronics-reports-second-quarter-2026-wjz4h91d9ngj.html).)*

**Growth (20% weight)**
```
Revenue 3yr CAGR (FY2022 $222.82M → FY2025 $455.72M) = (455.72/222.82)^(1/3) − 1 = 26.94%/yr
Growth_Score (raw) = clamp((26.94/25)×100, 0, 100) = 100.0 (already capped)
```
Documented TAM-expansion evidence (would add +10, but already capped at 100.0): AI-datacenter demand for 800G/1.6T optical transceivers is outpacing AAOI's own production capacity — Q2 2026 800G revenue more than doubled sequentially with ~5× sequential growth guided for Q3 2026; the company disclosed over $200M of 1.6T orders as that ramp begins; Q3 2026 revenue guidance of $255–290M implies another large sequential step-up from Q2's $191.9M. *(Sources: [BigGo Finance Q2 2026 earnings recap](https://finance.biggo.com/news/US_AAOI_2026-08-06), [24/7 Wall St.](https://247wallst.com/investing/2026/08/03/aaoi-stock-just-popped-15-3-reasons-applied-optoelectronics-could-keep-climbing/).)*

**Balance Sheet (15% weight)**
```
Current (Q2 2026) Net Debt = Total Debt $264.54M − Cash $499.74M = −$235.20M (net CASH position)
FY2025 EBITDA = EBIT (−$54.60M) + D&A ($27.70M) = −$26.90M   (negative — TTM EBITDA likely similarly negative;
                                                               not fully reconstructable from available quarterly data, see §1)
Net Debt/EBITDA = −235.20 / −26.90 = +8.74×   (both negative → mechanically positive, but not a meaningful "leverage" reading)
BalanceSheet_Score (mechanical formula) = clamp(100×(1 − 8.74/4), 0, 100) = 0.0   (clamped at floor, not ceiling — see below)
```
**Flagged formula caveat:** the standard Net Debt/EBITDA formula is built for positive EBITDA; with **negative** EBITDA it can point either direction depending on the exact ratio, so it is not read mechanically without judgment (consistent with how the 2026-07-14 LCID session treated a negative-EBITDA balance sheet as a real debt-service-capacity concern, not a mechanical pass). Two readings are shown for transparency:
- **Strict reading (used above, 0.0):** negative EBITDA means the business currently generates **zero operating capacity to service any debt**, regardless of debt level — the same logic applied to LCID. AAOI differs from LCID in one important respect (LCID had net *debt* against negative EBITDA; AAOI currently has net *cash*, funded by a ~$382.4M 2026 equity raise, so there is no near-term insolvency risk), but the underlying operating-cash-generation problem the ratio is meant to capture is real either way.
- **Mechanical/net-cash reading (not used, would be 100.0):** if Net Debt/EBITDA is instead read purely on the "is the company levered" axis (it isn't — net cash), the formula would clamp to 100.0.
Given the genuine ambiguity, the **strict (0.0) reading is used** in the Final Quality Score below, and a sensitivity calc with the alternate (100.0) reading is shown alongside it — **neither reading changes the pass/fail outcome** (see Final Quality Score).

**Moat Signal (15% weight)** — checklist, cited evidence only:

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | FALSE | No specific, citable market-share figure for AAOI (vs. peers like Coherent, Lumentum, Innolight) was found in this session. |
| Brand premium | FALSE | No price-increase-without-volume-loss evidence found; AAOI competes in a price-competitive commodity-transceiver market. |
| Network effect | FALSE | Not applicable — component/transceiver manufacturer, not a platform business. |
| Switching costs | **TRUE** | Datacenter-optics customers (hyperscalers) run 12–24 month supplier-qualification cycles before a transceiver design is approved for production — the same documented industry-wide mechanism already established for peers LITE and COHR in this framework (see [glossary.md](../framework/glossary.md) "Qualification cycle (supplier)"). AAOI's own disclosures confirm it is now shipping qualified 800G product in volume to "one of its large hyperscale customers." |
| Scale cost advantage | FALSE | AAOI is a smaller-scale, historically thinner-margin manufacturer than peers (Lumentum, Coherent, Innolight); no cost-per-unit-vs-competitors citation found. |

```
Moat_Score = (1/5) × 100 = 20.0
```

**FCF Quality (10% weight)**
```
TTM FCF = −$592.23M   TTM Net Income = −$57.0M
Literal ratio = FCF/NI = −592.23 / −57.0 = 10.39 (1039%)
Literal FCFQuality_Score = clamp(((10.39 − 0.40)/0.60)×100, 0, 100) = 100.0  (clamped — NOT used, see override below)
```
**Override applied (flagged):** the literal formula produces 100.0 — the *best possible* cash-quality score — because dividing two negative numbers yields a large positive ratio. This is actively misleading: FCF is burning at **more than 10× the rate of the reported net loss**, which is definitionally the *worst*, not the best, cash-conversion outcome. Per "no black-box outputs" this literal result is shown, but **FCFQuality_Score is scored 0.0** rather than the mechanical 100.0, consistent with the sub-score's intent (does reported profit turn into cash — here, the answer is unambiguously no, cash is disappearing faster than the accounting loss shows).
```
FCFQuality_Score (used) = 0.0
```

### Final Quality Score

**Primary (strict Balance Sheet reading, 0.0):**
```
Quality Score = (0.0×0.25) + (36.15×0.15) + (100.0×0.20) + (0.0×0.15) + (20.0×0.15) + (0.0×0.10)
              = 0.000 + 5.4225 + 20.000 + 0.000 + 3.000 + 0.000
              = 28.4225 → rounded 28.4
```

**Sensitivity (mechanical net-cash Balance Sheet reading, 100.0) — shown for completeness, does not change the outcome:**
```
Quality Score = (0.0×0.25) + (36.15×0.15) + (100.0×0.20) + (100.0×0.15) + (20.0×0.15) + (0.0×0.10)
              = 0.000 + 5.4225 + 20.000 + 15.000 + 3.000 + 0.000
              = 43.4225 → rounded 43.4
```

## QUALITY SCORE: 28.4 – 43.4 / 100.0 (depending on Balance Sheet reading) — GATE: FAIL (threshold 80.0)

**Both readings fail the 80.0+ gate by a wide margin, and an independent hard disqualifier (not FCF-positive in any of the last 5 fiscal years, let alone 3+ consecutive) fires regardless.** Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md), the evaluation stops here — **Phase 02 valuation scoring, the Composite Score, the Rate Environment Gate, and the fair-value/order-setup work are not computed.** This is the correct, complete outcome for a gate this strict, not an incomplete session.

---

## 4. Why this matters despite the failing score — qualitative context

The underlying operating story is genuinely strong and independently verified, not hype:
- Q2 2026 revenue $191.9M, +86% YoY, +27% sequentially — the company's **fifth consecutive quarter of record revenue**. *(Source: [StockTitan](https://www.stocktitan.net/news/AAOI/applied-optoelectronics-reports-second-quarter-2026-wjz4h91d9ngj.html).)*
- Returned to **non-GAAP** profitability in Q2 2026 (non-GAAP EPS $0.06, beat guidance) — though GAAP net loss widened to $22.8M the same quarter, and management itself flagged $3.6M of discontinued-product costs weighing on the GAAP gross margin.
- Q3 2026 revenue guidance of $255–290M implies another large sequential step-up, driven by 800G ramping toward hyperscaler demand and early 1.6T order flow (>$200M).
- The company raised ~$382.4M of net equity proceeds in H1 2026 and has a $600M ATM equity program in place — providing real liquidity runway (current net cash ~$235M) for its ~$300M Pearland, TX capacity expansion, but at the cost of material shareholder dilution, a real Quality-relevant negative not itself a formal sub-score input (per Phase 01's "Share issuance pattern" checklist item).

**None of this changes the Quality Score outcome.** AAOI has never once, in the 5 fiscal years of GAAP financials reviewed for this session, generated positive free cash flow, and its TTM net margin (−9.57%) and ROIC (−1.55%) remain solidly negative even amid the current growth surge. This is exactly the kind of "compelling growth story, unproven quality track record" case the 80.0+ gate is designed to keep out until an established multi-year profitability/cash-generation record exists — the same reasoning this framework applied to LITE (2026-07-28/2026-08-14) and LCID (2026-07-14).

---

## 5. Recommendation

**PASS — watchlist only, do not enter a position now.** Quality Score fails the 80.0+ gate by a wide margin under either Balance Sheet reading (28.4–43.4 vs. 80.0), and a hard disqualifier (not FCF-positive in any of the last 5 fiscal years) independently fires. No Composite Score exists to check against the Phase 03 action table ([valuation-scoring.md](../framework/valuation-scoring.md) / [operating-brief.md](../framework/operating-brief.md) Action Table), and no fair-value/order-setup work is produced, per [fair-value-methodology.md](../framework/fair-value-methodology.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md) (both gate that step on a passing Quality Score).

**Next review trigger:** the FCF-positive-3-consecutive-years disqualifier is a track-record problem that resolves only with sustained execution over multiple future fiscal years — re-score at the next quarterly earnings release (Q3 2026, expected ~early November 2026) to check whether the current revenue/margin trajectory is translating into positive operating cash flow (TTM FCF is currently deeply negative, −$592.23M, and CapEx-heavy). Also re-score immediately on any other Rule 9 fundamental trigger (guidance revision, M&A, management change, macro shift, or a >15% unexplained move not already covered by routine earnings).

---

## Glossary

- **800G / 1.6T (optical transceiver)** — speed-grade designations for AI-datacenter optical interconnects; AAOI's next-generation product ramp. *(New term, added this session.)*
- **ATM Program (At-the-Market Offering Program)** — a facility letting a company sell newly issued shares directly into the open market over time; AAOI has a $600M ATM program in place.
- **CAGR (Compound Annual Growth Rate)** — the smoothed yearly growth rate implied by a start and end value over several years; used for the Growth sub-score's 3yr revenue calc.
- **CapEx** — Capital Expenditure; money spent buying or upgrading physical assets (e.g. AAOI's Pearland, TX manufacturing expansion).
- **CATV (Community Antenna Television)** — the cable-TV/broadband industry; one of AAOI's two core product lines. *(New term, added this session.)*
- **Composite Score** — this framework's 50/50 blend of Quality Score and Valuation Score; not computed here since AAOI never clears the Quality Score gate.
- **D&A** — Depreciation & Amortization; the non-cash accounting expense that spreads the cost of long-lived assets over time.
- **EBIT** — Earnings Before Interest and Taxes; operating profit before financing costs and taxes.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization; a rough proxy for cash operating profit, used in the Net Debt/EBITDA balance-sheet check.
- **EPS** — Earnings Per Share; net income divided by shares outstanding.
- **FCF (Free Cash Flow)** — cash generated after running and maintaining the business; the FCF-positive-3-consecutive-years hard disqualifier is the deciding factor in this session.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income; checks whether reported accounting profit is actually turning into cash. AAOI's literal TTM ratio is a misleading 1039% (both figures negative); overridden to a floored FCFQuality_Score for this reason.
- **GAAP** — Generally Accepted Accounting Principles; the standard US accounting rulebook, used for all scored figures in this session (never non-GAAP/adjusted figures).
- **Gross Margin** — Gross Profit ÷ Revenue; one of the Quality Score's Margins sub-score inputs.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company outright regardless of its weighted sub-score total; the "not FCF-positive 3+ consecutive years" disqualifier fires for AAOI.
- **Hyperscaler** — an operator of very-large-scale, globally-distributed cloud/data-center infrastructure; AAOI's primary AI-optics customer base.
- **M&A** — Mergers & Acquisitions.
- **Moat** — a durable competitive advantage protecting a business's profits from competitors; scored here via a 5-signal checklist.
- **Net Debt/EBITDA** — net debt divided by EBITDA; this framework's primary balance-sheet leverage gate. The formula breaks down for AAOI's negative-EBITDA/net-cash combination — both readings are shown and flagged.
- **Net Margin** — Net Income ÷ Revenue; one of the Quality Score's Profitability sub-score inputs.
- **Qualification cycle (supplier)** — the multi-month-to-multi-year process a hyperscaler/AI-hardware customer runs to validate and approve a component supplier before production use; cited as the Switching Costs moat-signal mechanism for AAOI.
- **Quality Score** — this framework's 0.0–100.0 score across profitability, margins, growth, balance sheet, moat, and FCF quality; a company must clear 80.0 to proceed to valuation scoring. AAOI scores 28.4–43.4 and fails the gate.
- **ROIC (Return on Invested Capital)** — how efficiently a company turns invested capital into profit; a core Quality Score input.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported results, as used throughout this session's sub-score calculations.

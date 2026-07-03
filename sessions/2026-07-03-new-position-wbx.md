# New Position Evaluation — WBX (Wallbox N.V.)

**Task type:** NEW POSITION
**Date:** 2026-07-03
**10Y US Treasury yield:** 4.49% (2026-07-02, most recent trading day — TradingEconomics/FRED cross-check; **not actually invoked**, since Phase 01 fails before the Rate Environment Gate is reached — see Section 3)
**Trigger:** Manual `/new-position wbx` request. No prior watchlist entry exists for WBX under `watchlist/` (checked both `in-portfolio/` and `not-in-portfolio/`) and it is not a current holding (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)). Ticker resolved unambiguously via IBKR contract search: NYSE:WBX → "WALLBOX NV" (contract_id 792307606) — an EV (electric vehicle) home/commercial charging-hardware maker, not to be confused with Webull Corporation (ticker **BULL**, already evaluated separately — see [sessions/2026-06-21-new-position-bull.md](2026-06-21-new-position-bull.md)).

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first, before any valuation work.

| Source | Value | Detail |
|---|---|---|
| IBKR real-time snapshot (contract_id 792307606, NYSE) | $3.40, flagged `is_close` | **Discrepancy caught and resolved below — not used as-is.** |
| IBKR daily historical bar, 2026-07-02 | **close $4.16** | Cross-checked against independent vendor |
| stockanalysis.com | close $4.16 (2026-07-02), after-hours $4.54 (+9.13%) | Independent source, matches IBKR's own historical bar exactly |
| IBKR 30-min intraday bars, 2026-07-02 (incl. after-hours) | last print ~$4.46 (23:30 UTC) | Confirms continued after-hours strength consistent with stockanalysis's $4.54 print |
| 52-week range (IBKR `misc_statistics`) | $2.34 – $7.65 | stockanalysis reports $2.30–$7.83 (close enough to be the same window, different vendor rounding/day-of-refresh) |
| Analyst consensus PT (stockanalysis) | $5.50 (Hold, 2 analysts) | For bull-case FV sanity check only |

**Discrepancy note (Rule 0 discipline, per the SPGI lesson):** IBKR's live snapshot tool returned $3.40 flagged `is_close` with zero volume/open/high/low — a stale/frozen quote. Pulling IBKR's own daily historical bars resolved this: $3.40 is actually **2026-07-01's** close, and the stock then jumped +22.4% intraday on 2026-07-02 to close at $4.16 (volume 150,155, more than 4× the prior day) — independently confirmed by stockanalysis.com's identical $4.16 figure. **Live price used throughout this session: $4.16** (2026-07-02 close, the most recent confirmed trade at time of writing; after-hours activity to ~$4.46–4.54 noted as directional context only, not used as a financial input).

No specific news item explaining the +22.4% single-day move was independently verified in this session (Wallbox has been in an active debt-restructuring process since early 2026 — see Section 3.1 — which is a documented, ongoing fundamental situation, not a single dated catalyst for this specific print). This would ordinarily be a Rule 9 ">15% unexplained move" trigger for an existing holding; noted here for completeness even though WBX is not held.

---

## 2. Data Sources

`yfinance` was not attempted this session (per the AAPL/CHTR/CDR/CRCL/OUST-documented `curl_cffi` TLS environment incompatibility). Fundamentals sourced from stockanalysis.com's structured financial-statement tables (income statement, cash flow statement, balance sheet — FY2021–FY2025), cross-checked against independent search summaries of Wallbox's own FY2025 20-F disclosures and contemporaneous news coverage (StockTitan/BusinessWire/Investing.com) of the debt-restructuring process. Every figure used in Section 3 is cited to one of these; no required input is missing or invented.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Hard disqualifiers (checked first — these override the weighted score regardless of outcome)

| Disqualifier | WBX data | Carve-out exists in the text? | Verdict |
|---|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | Annual FCF (stockanalysis cash-flow statement): FY2021 −€80.34M, FY2022 −€174.09M, FY2023 −€76.34M, FY2024 −€59.78M, **FY2025 +€9.37M**. Four straight negative years followed by one narrowly-positive year — **the company has never had a single 3-consecutive-year positive-FCF run.** | **No** — this disqualifier carries no growth-capex carve-out. | **🔴 TRIGGERED — hard FAIL, independent of every other number in this section.** |
| FCF/Net Income conversion <70% for 2+ consecutive years | FY2025: €9.37M / −€103.2M = **−9.1%** (literal ratio); FY2024: −€59.78M / −€151.79M = **39.4%**. Net Income is negative in every year on record — there is no accounting profit for this ratio to meaningfully "convert." | N/A — moot | Not independently assessed (superseded by the FCF-positivity disqualifier above, same treatment as the OUST 2026-07-01 precedent) |
| **Net Debt/EBITDA over threshold (2.5×/4×)** | Total debt €197.77M − cash €4.45M = **net debt €193.32M** (real, substantial debt — not a net-cash position). EBITDA: FY2022 −€119.95M, FY2023 −€78.5M, FY2024 −€95.94M, **FY2025 −€65.11M** — negative in every year on record. Net Debt/EBITDA = 193.32 / −65.11 = a degenerate negative ratio, because **the company cannot service or repay this debt from operations at all** — the opposite, and worse, edge case from OUST's zero-debt/negative-EBITDA situation (net cash there; real debt + no operating cash generation here). | No carve-out applies — this is real leverage with no offsetting operating cash flow, not a formula artifact. | **🔴 TRIGGERED — hard FAIL.** Reinforced by external, independent evidence of balance-sheet distress: Wallbox received a NYSE non-compliance notice (Section 802.01B, average global market cap + stockholders' equity ≥ $50M) on 2026-02-12; entered a standstill agreement with its banking-pool lenders (extended through 2026-03-31); reported **negative shareholders' equity (−€31.46M FY2025, down from +€62.58M FY2024)**; and, per creditors holding >83% of its financial debt, agreed a comprehensive restructuring (signed ~2026-04-08) extending €169.6M of debt maturities to 2030-12-31 via a €57.6M framework loan, a €69.1M PIK bullet instrument, and a €42.8M working-capital framework, alongside a dilutive €10.65M capital increase. |

WBX triggers **two independent hard disqualifiers**, each sufficient on its own to fail the gate outright. Per [new-position.md](../.claude/commands/new-position.md) step 2, this alone is sufficient to stop here — but every sub-score below is still shown in full, per that same step's explicit instruction.

### 3.2 Sub-scores (all six, per the weighted formula)

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | Net margin = −€103.2M / €145.12M = **−71.10%** → NetMargin_Component = clamp(−71.10/30×100, 0, 100) = **0.0**. NOPAT = EBIT × (1 − 0% — no tax benefit assumed on an operating loss) = −€99.29M. Invested Capital = Debt €197.77M + Equity (−€31.46M) − Cash €4.45M = €161.86M. ROIC = −99.29 / 161.86 = **−61.35%** → ROIC_Component = clamp(−61.35/30×100, 0, 100) = **0.0**. Profitability_Score = (0.0+0.0)/2 = **0.0** (the FCF-positivity cap at 40.0 is moot — raw score is already below that). | **0.0** |
| **Margins (15%)** | Gross margin FY2025 = 38.27%, up from 34.17% (FY2024) and 33.57% (FY2023) — a documented 3yr expanding trend (source: stockanalysis income-statement table). GrossMargin_Score = clamp(38.27/80×100, 0, 100) = **47.84**. Margin is below the 40% static threshold but structurally expanding on the cited 3yr trend → **+10** bonus applies = **57.84**. | **57.8** |
| **Growth (20%)** | Revenue: FY2022 €144.19M → FY2023 €143.77M → FY2024 €163.94M → FY2025 €145.12M. 3yr CAGR = (145.12/144.19)^(1/3) − 1 = **+0.21%** → Growth_Score = clamp(0.21/25×100, 0, 100) = **0.86**. No +10 TAM/pricing-power modifier applied — no cited source documents TAM expansion or pricing power for WBX this session. No −10 "structural deceleration" modifier applied either, despite FY2025's −11.48% YoY revenue decline — the framework requires *documented* evidence the deceleration is structural (not cyclical/EV-demand-cycle-driven) before applying that penalty, and no such citation was gathered; flagged as an open question for a future review rather than invented here. | **0.9** |
| **Balance Sheet (15%)** | Net Debt/EBITDA is degenerate as shown in 3.1 (real €193.32M net debt against negative EBITDA in every year on record). Unlike OUST's zero-debt "best case" edge case, this is the **worst-case** leverage profile the formula can encounter: substantial real debt with no operating cash generation to service it, independently corroborated by the NYSE non-compliance notice, standstill agreement, and negative shareholders' equity documented in 3.1. Scored at the floor rather than through the literal (nonsensical) formula output. | **0.0** (flagged judgment call, mirroring the OUST precedent's transparent override — here to the floor rather than the ceiling, given the opposite substantive situation) |
| **Moat Signal (15%)** | No cited evidence was gathered this session establishing any of the 5 signals true (stable/growing market share, brand premium, network effect, switching costs, scale cost advantage) for WBX specifically. Per the framework's rule ("never mark a signal true without a cited source"), the absence of gathered evidence defaults every signal to false rather than crediting any of them speculatively. Moat_Score = (0/5)×100. | **0.0** |
| **FCF Quality (10%)** | FY2025 FCF/NI ratio (literal) = €9.37M / −€103.2M = **−9.1%** → clamp(((−0.091−0.40)/0.60)×100, 0, 100) = clamp(−81.8, 0, 100) = **0.0**. Unlike OUST, the literal formula already produces the defensible (floor) result here — no override needed. | **0.0** |

### 3.3 Final weighted Quality Score

```
Quality Score = (0.0 × 0.25) + (57.8 × 0.15) + (0.9 × 0.20) + (0.0 × 0.15) + (0.0 × 0.15) + (0.0 × 0.10)
              = 0.0 + 8.68 + 0.18 + 0.0 + 0.0 + 0.0
              = 8.85 → 8.8
```

**8.8 < 80.0 — fails the gate**, in addition to two independent hard disqualifiers already firing in Section 3.1. Three independent mechanisms agree on the same verdict.

### Result: **Phase 01 FAIL**

WBX (Wallbox N.V.) is a European EV-charging-hardware maker that priced-in a fresh 22.4% single-day rally on 2026-07-02 but remains deeply unprofitable (net margin −71.1%, ROIC −61.4%), has never sustained 3 consecutive years of positive free cash flow (only turning FCF-positive, narrowly, in FY2025 after four straight negative years), and — most acutely — carries real, substantial net debt (~€193M) against negative EBITDA in every year on record. That last point is independently corroborated by hard external facts, not just a formula artifact: a February 2026 NYSE continued-listing-standard non-compliance notice, a lender standstill agreement, negative shareholders' equity, and an April 2026 comprehensive debt restructuring (extended maturities, PIK bullet instrument, dilutive capital increase). The quality gate's job is exactly to catch "company in active balance-sheet distress" — which this is, regardless of how the stock trades day-to-day.

Per [new-position.md](../.claude/commands/new-position.md) step 2: *"If it's below 80.0, or a hard disqualifier fires, stop and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed.**

---

## 4. Recommendation

**PASS.** Do not open a position. No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails the quality gate this framework uses to define what's even eligible for scoring.

This is not a verdict on whether Wallbox's underlying EV-charging-hardware business could recover — the restructuring plan (extended maturities to 2030, fresh working-capital facility) is specifically designed to buy the company time and could plausibly work. It is a verdict that **the company is currently in active balance-sheet distress with no demonstrated ability to fund itself from operations**, which this framework requires to be resolved (not just announced) before valuation is even attempted. The +22.4% single-day rally that immediately preceded this session is exactly the kind of price action Rule 0/Rule 9 discipline says to never treat as a substitute for the underlying fundamentals.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Mandatory Rule 9 re-check:** Wallbox's next scheduled disclosure — expected H1 2026 interim results (per its investor-relations quarterly-results cadence) or any 6-K update on the restructuring plan's execution/completion.
- **Mechanical trigger:** confirmation that the FY2025 positive-FCF print is sustained for a second and third consecutive year (rather than a single-year restructuring-driven artifact — e.g. from the 28% headcount/opex cuts cited in Wallbox's own disclosures) would meaningfully change the FCF-positivity hard-disqualifier picture; a return to positive shareholders' equity and a resolved (not just signed) restructuring would address the Balance Sheet disqualifier.
- **Other Rule 9 events:** a guidance revision, management change, material M&A, NYSE delisting determination, or a further >15% stock-price move with no identified cause.
- Absent any of the above, future mentions of WBX should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **Continued listing standard** — An exchange's ongoing minimum requirements (market cap, stockholders' equity, share price) a company must keep meeting to remain listed; falling short triggers a compliance notice and cure period, not immediate delisting. NYSE Section 802.01B (average global market cap + stockholders' equity ≥ $50M) is the specific rule WBX was notified against.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and profitability ratios.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; not meaningful when Net Income is itself negative (see Section 3.2's FCF Quality row).
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs.
- **Hard disqualifier** — One of three specific failure conditions in this framework's Quality Score engine (sustained FCF/NI conversion below 70%, excessive Net Debt/EBITDA, or no FCF-positive 3-year run) that fails a company outright regardless of its weighted score.
- **Invested Capital** — The total capital (debt + equity, minus cash) deployed in a business — the denominator of ROIC. Can shrink sharply, or invert in sign, when shareholders' equity turns negative.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate. Degenerate (mathematically meaningless as a "years to repay" figure) when EBITDA is negative — here, real debt plus negative EBITDA is the worst-case version of that edge case, not a favorable one.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT** — Net Operating Profit After Tax — EBIT × (1 − effective tax rate) — the numerator used to compute ROIC.
- **Phase 01–06** — The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **PIK (Payment-in-Kind) interest** — Interest paid by adding to the debt owed rather than in cash — grows total debt over time, common in distressed-company restructurings like Wallbox's.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality) instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. (WBX does not make this list.)
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price (and primary financial data) before any valuation work — never infer or invent it. This session's IBKR-snapshot-vs-historical-bar discrepancy (Section 1) is a direct example of the discipline this rule enforces.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly/interim earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **Standstill agreement** — A temporary agreement between a distressed borrower and its lenders not to demand repayment or enforce default remedies while a longer-term restructuring is negotiated — a signal of active, unresolved balance-sheet distress.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).

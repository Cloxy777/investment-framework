# NEW POSITION (Quality Score Engine addendum) — DASH (DoorDash, Inc.) — 2026-07-07

**Task type:** NEW POSITION — Quality Score Engine addendum (lightweight, per the CCL/CDR precedent), not a full re-evaluation
**Date:** 7 Jul 2026
**Ticker:** DASH (DoorDash, Inc., NASDAQ)
**Prior session:** [2026-06-14-new-position-dash.md](2026-06-14-new-position-dash.md) — Phase 01 FAIL (net margin 6.3–6.8% vs. >15% required, ROIC 4.5–11.1% vs. >15% required), predates the 2026-06-29 Quality Score engine addition — DASH has never had a Quality Score computed until this session
**Current DASH portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session exists

DASH's 06-14 session failed Phase 01 (the binary quality screen that predates the 2026-06-29 Quality Score engine) and was never scored under the new 0–100.0 engine. Per this task's explicit scope, this session does two things only:

1. A Rule 9 check — has DoorDash reported a new quarterly print since 06-14 showing margin acceleration (the 06-14 session's own flagged "trend to watch"), or any other Rule 9 trigger (guidance revision, management change, M&A, macro shift, >15% unexplained price move)?
2. Compute DASH's first-ever Quality Score under the current engine, with every sub-score shown, using the freshest available TTM data.

Per the task's branching instruction, a fuller Phase 01 re-check (or a new dated watchlist file) is only warranted if a Rule 9 trigger fired that changes the Phase 01 verdict. As shown below, no such trigger fired, so this stays an addendum appended to the existing watchlist file.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$188.98** | IBKR `get_price_snapshot`, contract_id 459309417, pre-market snapshot, `ts` 1783394481 → 2026-07-07 03:21:21 UTC, `is_close: false` |
| 52-week range | $143.30 – $285.50 | IBKR `misc_statistics` (unchanged from 06-14) |
| 13-week range | $146.11 – $196.79 | IBKR `misc_statistics` |
| Analyst consensus PT | ~$245–$257 (42–53 analysts), "Buy" | WebSearch (TipRanks, S&P Global aggregation, stockanalysis.com) |
| Baseline (06-14) | $150.58 | Prior session |
| Change since 06-14 | **+25.5%** | Computed |

---

## 2. Rule 9 check — all 6 categories

| Category | Result |
|---|---|
| Earnings | **NO new print.** Q1 FY2026 (quarter ended 2026-03-31) was already reported 2026-05-06, *before* the 06-14 session, and its TTM figures are already what 06-14 used (confirmed: this session's freshly-pulled TTM net margin 6.29% / TTM revenue $14.721B match 06-14's cited stockanalysis.com TTM figures exactly). Q2 FY2026 is scheduled for 2026-08-05 — not yet reported. |
| Guidance revision | None found since 06-14 (no Item 2.02 8-K filed between 05-06 and today). |
| Management change | None — Tony Xu (CEO), Ravi Inukonda (CFO) unchanged. A 2026-06-12 8-K (Items 5.07/8.01) is a routine annual-meeting voting-results filing. |
| M&A | None new. Deliveroo acquisition (completed 2025-10-02, ~$3.9B) predates 06-14 and is already embedded in both sessions' balance-sheet data. |
| Macro shift | A genuine sector-wide tailwind (not adverse, not DASH-specific): a mid-June Strait-of-Hormuz peace-deal announcement drove oil prices and the 10Y Treasury yield down, lifting discretionary/platform-stock valuations broadly (+12.1% for DASH on 2026-06-15); a second leg (+5.6%, 2026-06-24) followed strong Prime Day online-sales data and a further yield dip. Company-specific catalysts cited alongside: a >9,000-store Dollar Tree partnership, FIFA World Cup 2026 marketing tied to DashPass sign-ups, continued DoorDash Ads/AI monetization. |
| >15% unexplained price move | **NO** — the +25.5% move is accounted for by the two dated catalysts above (~18pp combined) plus broader risk-on drift; not "unexplained." |

**Net effect: no Rule 9 trigger fired that bears on the Phase 01 verdict.** No new earnings print exists since 06-14 — the next one (2026-08-05) hasn't happened yet — so there is no new quarterly data to re-run Phase 01 against. The freshest available TTM data (through Q1 FY2026, identical to what 06-14 already used) still shows net margin 6.29% and ROIC ~5.6–5.9%, both far below the >15% thresholds. **This confirms the addendum-only path** — no fuller Phase 01 re-check or new dated file is warranted.

---

## 3. Data sourcing note

`yfinance`'s own HTTP client (`curl_cffi`, browser-impersonation mode) again could not complete a TLS handshake through this session's egress proxy (`curl: (35) Recv failure: Connection reset by peer`) — the same documented issue as the 2026-07-06 CCL session. Worked around it the same way: called Yahoo Finance's public `fundamentals-timeseries` endpoint directly via plain `requests` (`https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/DASH?...`), using the same field names yfinance's own source code uses internally (`trailingTotalRevenue`, `trailingGrossProfit`, `trailingEBIT`, `trailingEBITDA`, `trailingNetIncome`, `trailingTaxRateForCalcs`, `trailingFreeCashFlow`, `quarterlyTotalDebt`, `quarterlyCashAndCashEquivalents`, `quarterlyInvestedCapital`, `annual*` equivalents). Cross-checked internally (the four most recent quarterly EBIT/EBITDA/Net Income figures sum exactly to the reported TTM figures) and against the primary-source FY2025 SEC 8-K (Revenue $13,717M − Cost of Revenue excl. D&A $6,738M = Gross Profit $6,979M, reconciling exactly to Yahoo's `annualGrossProfit` figure).

**Two data discrepancies flagged (neither changes the conclusion):**
- Gross margin: this session's GAAP-reconciled TTM figure (50.89%) is ~0.9–1.0pp below 06-14's cited 51.8% FY2025 figure — likely a different aggregator's cost-of-revenue definition. Both are well above the 40% pass threshold either way.
- Cash: this session's Yahoo-sourced Q1 FY2026 cash figure ($4.575B) differs from 06-14's cited $5.53B ("financecharts/aggregator," unspecified basis) — possibly cash-only vs. cash-plus-short-term-investments. DASH is net-cash under either figure, so the Balance Sheet sub-score (clamped to 100.0) is unaffected.

---

## 4. Quality Score Engine — DASH's first-ever computation

Per [framework/quality-scoring.md](../framework/quality-scoring.md) (methodology version 2026-06-29). Full detail, every sub-score input, and the worked formula are in the [watchlist addendum](../watchlist/not-in-portfolio/DASH/DASH-2026-06-14.md); summarized here:

| Sub-score (weight) | Score |
|---|---|
| Profitability (25%) | 20.29 |
| Margins (15%) | 63.61 |
| Growth (20%) | 100.0 |
| Balance Sheet (15%) | 100.0 |
| Moat (15%) | 80.0 |
| FCF Quality (10%) | 100.0 |

```
Quality Score = 20.29×0.25 + 63.61×0.15 + 100.0×0.20 + 100.0×0.15 + 80.0×0.15 + 100.0×0.10
              = 5.07 + 9.54 + 20.00 + 15.00 + 12.00 + 10.00
              = 71.6
```

**Quality Score = 71.6 / 100.0 — fails the 80.0+ gate.** No hard disqualifier fires independently (DASH is net-cash, FCF-positive every year on record FY2022–FY2025 plus TTM, and its FCF/NI conversion is far above 70% every year) — unlike the CCL precedent, this is a pure weighted-score failure. The shortfall is driven almost entirely by **Profitability (20.29)**: DASH's net margin (6.29% TTM) and ROIC (5.89% TTM) sit well below the 15%/15% thresholds the Profitability sub-score is calibrated against, dragging down an otherwise strong profile (100.0 Growth, 100.0 Balance Sheet, 80.0 Moat, 100.0 FCF Quality). No Composite Score computed (requires clearing the gate first). No Phase 02 valuation work performed (out of scope for this addendum, and moot given the gate result).

### Moat Signal detail (cited evidence required per signal)

| Signal | Result | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | 60.7% US food-delivery share end of 2024 → ~67% by 2025-2026 (vs. Uber Eats ~23%) — third-party transaction-panel research (Second Measure/Earnest Analytics-style sources, via WebSearch), growing not just stable |
| Brand premium (pricing power) | **TRUE** | Net Revenue Margin (take rate) risen from 11.8% (Q1 2022) to 13.5% (Q3 2024), driven mainly by advertising monetization, while GOV/order volume kept growing 27%+ YoY — pricing power without volume loss (note: DashPass's own $9.99/month sticker price has been explicitly held flat since ~2020 per company statements, so this signal rests on the take-rate/ads evidence, not a DashPass price increase) |
| Network effect | **TRUE** | Three-sided marketplace (consumers, merchants, Dashers) — the standard, well-documented mechanism |
| Switching costs | **TRUE** | Merchant-side POS integrations (direct: Toast, Square, Clover; aggregator: Deliverect, Otter, Checkmate) with real-time menu/pricing/inventory sync — migrating platforms requires re-integrating operational workflow; also DashPass annual-plan lock-in |
| Scale cost advantage | **FALSE** | Searched for cost-per-order data showing a quantified gap vs. smaller competitors (Grubhub etc.); found only qualitative commentary (routing-efficiency claims, suburban first-mover positioning), no citable cost-per-unit figures |

Moat_Score = (4/5) × 100 = **80.0**

---

## 5. Recommendation

# **PASS — Quality Score 71.6/100.0, fails the 80.0+ gate (no hard disqualifier independently fires). Do not enter. Watchlist addendum appended, no new file created.**

No new Rule 9 trigger fired since 06-14 that bears on the Phase 01 verdict — the next quarterly print (Q2 FY2026) isn't due until 2026-08-05. DASH's first-ever Quality Score computation reaches the same conclusion as the original Phase 01 FAIL through a different, graded lens: this is a high-growth (100.0 Growth), well-capitalized (100.0 Balance Sheet, net cash), moat-worthy (80.0 Moat) business that has not yet converted its market position into bottom-line profitability commensurate with this framework's bar — Profitability (20.29) is the single sub-score holding it back from the gate, consistent with the 06-14 session's own framing of margin conversion as "the trend to watch."

**No position opened — nothing to log in `decisions/`.**

---

## 6. Files touched this session

- `watchlist/not-in-portfolio/DASH/DASH-2026-06-14.md` — appended the Rule 9 check + Quality Score addendum as a dated note (no new file, per the task's branching instruction — no Phase 01 verdict change)
- `framework/glossary.md` — added **Dasher**, **DashPass**, **GOV (Gross Order Value)**, **Net Revenue Margin (take rate)**, and **Second Measure / Earnest Analytics**
- `sessions/2026-07-07-new-position-dash.md` — this file

`watchlist/STALE.md` was not touched (DASH is not listed there — it predates the Quality Score engine but was never a "stale re-score" case, it was a Phase 01 FAIL that had never been scored at all).

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **8-K** — a US company's "current report" filed with the SEC disclosing a material event between regular filings; used here as the primary source for the FY2025 earnings release used to reconcile gross margin.
- **CAGR** — Compound Annual Growth Rate.
- **Dasher** — DoorDash's term for the independent-contractor courier who fulfills a delivery order on its marketplace.
- **DashPass** — DoorDash's paid subscription program offering $0 delivery fees and reduced service fees on qualifying orders; a switching-cost/loyalty mechanism.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization.
- **Effective tax rate** — the actual share of pretax income paid as tax.
- **FCF** — Free Cash Flow.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income, an earnings-quality check.
- **GAAP** — Generally Accepted Accounting Principles.
- **GOV (Gross Order Value)** — DoorDash's term for the total dollar value of orders transacted through its marketplace before its own revenue/take-rate is deducted.
- **Gross Margin** — Gross Profit ÷ Revenue.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted score; none fire for DASH.
- **Moat** — a durable competitive advantage.
- **Net Revenue Margin (take rate)** — DoorDash's own revenue ÷ Marketplace GOV metric; risen from ~11.8% to ~13.5% (2022–2024), cited here as pricing-power/monetization Moat Signal evidence.
- **NOPAT** — Net Operating Profit After Tax, the numerator of ROIC.
- **Net Debt/EBITDA** — a leverage ratio; this framework's primary balance-sheet-risk gate.
- **Quality Score** — this framework's 0–100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02. DASH scores 71.6 on its first-ever computation.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 9** — this framework's list of events that force an immediate re-valuation: earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move.
- **Second Measure / Earnest Analytics** — independent consumer-transaction-data research firms cited for DoorDash's US food-delivery market-share evidence.
- **TAM (Total Addressable Market)** — the total revenue opportunity available if a company captured 100% of its target market.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results.

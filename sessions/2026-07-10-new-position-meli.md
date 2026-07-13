# NEW POSITION (Quality Score Engine addendum) — MELI (MercadoLibre, Inc.) — 2026-07-10

**Task type:** NEW POSITION — Quality Score Engine addendum (per the CCL 2026-07-06 precedent), not a full re-evaluation
**Date:** 10 Jul 2026
**Ticker:** MELI (MercadoLibre, Inc., NASDAQ)
**Prior session:** [2026-06-14-new-position-meli.md](2026-06-14-new-position-meli.md) — Phase 01 FAIL on net margin (TTM 6.04-7.93% vs >15% required, deliberate reinvestment-driven compression, management guiding H2 2026 recovery). Predates the 2026-06-29 Quality Score engine addition — MELI has never had a Quality Score computed until this session.
**Current MELI portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md).

---

## 0. Why this session exists

MELI's 06-14 session failed Phase 01 (the binary quality gate that predates the 2026-06-29 Quality Score engine) and was never scored under the new 0-100.0 engine. Per this task's explicit scope, this session does two things only:

1. A Rule 9 check — MELI's Q2 2026 earnings were flagged in the 06-14 session as due ~August 2026; confirm the exact date and whether reported, check net margin for sequential recovery, and check all 6 Rule 9 trigger categories since 06-14.
2. Compute MELI's first-ever Quality Score under the current engine, with every sub-score shown.

A fuller Phase 01 re-check (or a new dated watchlist file) is only warranted if a Rule 9 trigger fires that changes the Phase 01 verdict. As shown below, none did, so this stays an addendum appended to the existing watchlist file.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$1,858.07** | IBKR `get_price_snapshot`, contract_id 45602025 (resolved via `search_contracts`), intraday, `ts` 1783695667 (≈2026-07-10), `is_close: false`. Change: +$50.24 / +2.78% on the day. |
| Cross-check | $1,808.93 (WebSearch aggregator, described as "current price," prior close $1,808.03) | Internally consistent with IBKR: $1,858.07 − $50.24 change = $1,807.83 prior close, a ~$0.20 match to the aggregator's independently-derived $1,808.03 prior close — confirms the aggregator's figure is a stale/pre-rally read, not a discrepancy. IBKR used as primary. |
| 52-week range | $1,495.00 – $2,548.50 | IBKR `misc_statistics` |
| Baseline (06-14) | $1,589.60 | Prior session |
| Change since 06-14 | **+16.89%** | Computed — exceeds the 15% Rule 9 numeric threshold; see §2 for why it is not treated as an "unexplained" trigger |
| `yfinance` attempted | Failed — `curl_cffi` TLS `SSLError: Recv failure: Connection reset by peer` before returning any data (same failure class other 2026-07 sessions have logged for this environment) | Not used; IBKR + WebSearch used directly instead |

---

## 2. Rule 9 Trigger Check (2026-06-14 → 2026-07-10)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | **No** | Q2 2026 confirmed for **5 August 2026, after close** (MercadoLibre IR conference-call announcement) — not yet reported. TTM period is unchanged (Q2 2025–Q1 2026, same four quarters the 06-14 session used). |
| Guidance revision | **No new revision** | The Q1 2026 shareholder letter (7 May 2026, predates 06-14) states management does "not anticipate [margin levels] changing materially in the near term" — flagged as a nuance against 06-14's "guidance signals a margin trough with H2 2026 recovery expected" framing (the two read in tension), but it is the same underlying 7-May disclosure, not a fresh event this window. |
| Management change | **No (predates window)** | Ariel Szarfsztejn became CEO / Marcos Galperin moved to Executive Chairman effective 1 January 2026 — before 06-14. |
| M&A | **No** | $4.6B 2026 Mexico investment plan announced 8 June 2026 (predates 06-14) — organic capex, not M&A. |
| Macro shift | **No** | No discrete new company-specific or macro catalyst identified; 10Y UST unchanged bracket (~4.5-4.6%). |
| >15% unexplained price move | **Numerically yes (+16.89%), but explained** | A documented 7-consecutive-day rally (WebSearch: gurufocus, Trefis) driven by continued digestion of the already-known Q1 2026 beat (49% YoY revenue growth, reported 7 May) — no single new dated catalyst found, and analyst sentiment in the window was mixed (Jefferies reiterated a bullish ~$2,230 PT in late June; a Zacks downgrade to "Strong Sell" also occurred in late June). Read as sentiment-driven continuation of an already-known fundamental story, per Rule 9's own "without a fundamental trigger" carve-out — not treated as a fresh unexplained-move trigger, but flagged transparently since it exceeds the numeric threshold. |

**Net margin trend: no new data, no recovery shown yet.** Q1 2026 (4.7%) remains the latest reported quarter — identical to 06-14. Q2 2026 earnings (5 Aug 2026) is the actual first test of the "sequential recovery toward ~9.1%" question the 06-14 session posed.

**Conclusion: no Rule 9 trigger changes the Phase 01 verdict.** No new quarter, no confirmed new fundamental event, and the price move is explained rather than unexplained. Per the task's branching instruction, this stays an **addendum**, not a new dated re-evaluation.

---

## 3. Refreshed TTM financials (through Q1 2026, unchanged period vs. 06-14)

Sourced directly from SEC 8-K/10-Q filings via WebFetch, cross-checked against stockanalysis.com's quarterly tables (one stockanalysis.com "annual" fetch returned internally-inconsistent, unusable figures — e.g. implying FY2025 revenue of $110B against a directly-sourced/WebSearch-confirmed $28.89B — and was discarded in favor of summing the sourced quarterly figures and SEC-filed annual figures directly).

| Metric | TTM (Q2'25–Q1'26) | Source |
|---|---|---|
| Revenue | $31,803M (6,790+7,409+8,759+8,845) | Quarterly figures, stockanalysis.com, cross-checked vs. 06-14's "TTM revenue $31.80B" |
| Net Income | $1,920M | Same quarterly sum; matches stockanalysis.com's independently-reported "TTM Net Income $1,920M" exactly |
| Net Margin | 6.04% | $1,920M / $31,803M — matches 06-14's "6.04%" reading exactly |
| Gross Profit | $13,949M | Quarterly sum |
| Gross Margin | 43.86% | GAAP basis; diverges from 06-14's unsourced "50.68%" reading |
| Operating Income | $3,049M | Quarterly sum |
| D&A | $892M | stockanalysis.com quarterly cash-flow data |
| EBITDA | $3,941M | Op Income + D&A; cross-checks against macrotrends' "~$4.0B FY2025 EBITDA" |
| Effective tax rate | 29.28% | $795M tax / $2,715M pretax income, TTM quarterly sum |

**Balance sheet (2026-03-31 10-Q, primary source):**

| Metric | Value |
|---|---|
| Loans payable and other financial liabilities (current + non-current) | $9,927M ($5,316M + $4,611M) |
| Cash + ST investments + LT investments | $7,346M ($3,677M + $1,973M + $1,696M) |
| Net Debt (company-disclosed basis) | $2,581M |
| Net Debt incl. operating leases (cross-check basis) | $4,999M |
| Stockholders' Equity | $7,281M |
| Total Assets | $46,934M |

Note: excludes "Funds payable to customers" ($14,145M) and "Amounts payable due to credit/debit card transactions" (~$4,495M) from the debt figure — these are fintech customer-float liabilities backed by restricted cash/investments, analogous to a bank's customer deposits, not corporate financing debt. Flagged as a methodology choice, consistent with the CCL session's treatment of company-disclosed "Debt" lines over aggregator "TotalDebt" fields that fold in unrelated liabilities.

**Adjusted Free Cash Flow (MELI's own non-GAAP metric, ex-fintech-funding effects):**

| Period | Adjusted FCF | Net Income | FCF/NI |
|---|---|---|---|
| FY2023 | $1,389M | $987M | 140.7% |
| FY2024 | $1,315M | $1,911M | 68.8% |
| FY2025 | $1,481M | $1,997M | 74.2% |
| TTM (Q2'25 $454M + Q3'25 $206M + Q4'25 $763M + Q1'26 −$56M) | $1,367M | $1,920M | 71.2% |

All company-disclosed, sourced from SEC 8-K earnings releases. GAAP OCF−CapEx basis shown as cross-check only (TTM $11,818M/$1,920M = 615%, would cap the FCF Quality sub-score at 100.0) — not used, since it is heavily inflated by Mercado Pago's credit-portfolio funding dynamics, the exact distortion the 06-14 session already flagged.

---

## 4. MELI — Quality Score (first-ever computation, 2026-06-29 methodology)

See the full sub-score table, formula, and hard-disqualifier check in the [watchlist addendum](../watchlist/not-in-portfolio/MELI/MELI-2026-06-14.md) (not duplicated here in full); summarized:

| Sub-score (weight) | Score |
|---|---|
| Profitability (25%) | 30.95 |
| Margins (15%) | 54.83 |
| Growth (20%) | 100.0 |
| Balance Sheet (15%) | 83.63 |
| Moat (15%) | 80.0 |
| FCF Quality (10%) | 52.0 |

```
Quality Score = 30.95×0.25 + 54.83×0.15 + 100.0×0.20 + 83.63×0.15 + 80.0×0.15 + 52.0×0.10
              = 7.7375 + 8.2245 + 20.00 + 12.5445 + 12.00 + 5.20
              = 65.7
```

**Quality Score = 65.7 / 100.0 — fails the 80.0+ gate.** No hard disqualifier independently fires (FCF/NI conversion only fails 1 of the last 2 complete fiscal years, not 2+ consecutive; Net Debt/EBITDA 0.65x/1.27x is far under 2.5x either basis; FCF-positive every year on record) — this is a pure weighted-score shortfall, driven mainly by weak Profitability (30.95, reflecting sub-threshold net margin and a newly-standardized ROIC of 12.54% — materially below the 06-14 session's unsourced-methodology 20.76% reading) and a middling FCF Quality (52.0) once the fintech-funding distortion is stripped out of the GAAP headline FCF figure. Growth (100.0) and Balance Sheet (83.63) are strong; Moat (80.0, 4 of 5 signals) is solid.

**Moat Signal detail:**

| Signal | Result | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | Dominant #1 e-commerce position in Brazil/Mexico/Argentina, ~25-30% share in core LatAm markets (third-party research), <5% of total LatAm retail spend captured — large runway, not a share-loss risk |
| Brand premium (pricing power) | **FALSE** | Mixed/contradictory: take rate roughly flat near 15%; MELI *cut* commissions selectively in early 2026 to stay price-competitive vs. Shopee/Amazon Brazil — the opposite of "price increases without volume loss." A Brazil logistics-fee increase (March 2026) is the only offsetting data point, insufficient alone |
| Network effect | **TRUE** | Two-sided marketplace dynamics plus a documented 5-service closed-loop ecosystem (Marketplace, Mercado Pago, Mercado Envios, Mercado Ads, Meli+) |
| Switching costs | **TRUE** | Sellers integrate logistics + payments + working-capital credit; >60% of platform SMEs got their first-ever credit access through Mercado Pago (third-party analysis) |
| Scale cost advantage | **TRUE** | Cost-per-unit data: Brazil unit shipping cost −8% QoQ in a cited quarter from Mercado Envios volume scale; 2024 cost-per-package flat-to-down vs. inflation despite +29% YoY items shipped |

Moat_Score = (4/5) × 100 = **80.0**

---

## 5. Recommendation

# **PASS — Quality Score 65.7/100.0, fails the 80.0+ gate. Do not enter. Watchlist addendum appended, no new file created.**

No Rule 9 trigger fired since 06-14 that changes the Phase 01 verdict (Q2 2026 earnings, the actual test of the margin-recovery thesis, are still four weeks out — confirmed 5 August 2026). MELI's first Quality Score computation confirms the same underlying conclusion from a different angle: even setting aside the binary Phase 01 net-margin failure, the graded engine scores MELI at 65.7 — short of the 80.0+ gate — driven by weak Profitability and mid-tier FCF Quality once the fintech-funding distortion is stripped out, only partly offset by strong Growth, Balance Sheet, and Moat sub-scores.

**No position opened — nothing to log in `decisions/`.**

---

## 6. Files touched this session

- `watchlist/not-in-portfolio/MELI/MELI-2026-06-14.md` — appended the Rule 9 check + Quality Score addendum as a dated note (no new file, per the task's branching instruction — no Phase 01 verdict change)
- `framework/glossary.md` — added **Adjusted Free Cash Flow**
- `sessions/2026-07-10-new-position-meli.md` — this file

`watchlist/STALE.md` was not touched (MELI was not listed there — it predates the Quality Score engine but was never a "stale re-score" case; it was a Phase 01 FAIL that had never been scored at all, same situation as CCL's 2026-07-06 precedent).

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **Adjusted Free Cash Flow** — MercadoLibre's own non-GAAP FCF measure, ex-fintech-funding effects; used as the primary FCF Quality basis this session, added to the glossary this session.
- **CAGR** — Compound Annual Growth Rate.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization.
- **Effective tax rate** — the actual share of pretax income paid as tax.
- **FCF / FCF/NI conversion ratio** — Free Cash Flow / Free Cash Flow ÷ Net Income, an earnings-quality check.
- **GAAP** — Generally Accepted Accounting Principles.
- **Gross Margin** — Gross Profit ÷ Revenue.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted score; none fire for MELI this session.
- **Invested Capital** — the total capital (debt + equity) put to work in a business — the denominator of ROIC.
- **Moat** — a durable competitive advantage.
- **NOPAT** — Net Operating Profit After Tax, the numerator of ROIC.
- **Net Debt/EBITDA** — a leverage ratio; this framework's primary balance-sheet-risk gate.
- **Net Margin** — Net Income ÷ Revenue.
- **Quality Score** — this framework's 0-100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02. MELI's first-ever computation this session: 65.7 — fails the gate.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — always fetch a live price before any valuation work.
- **Rule 9** — the framework's list of events that force an immediate re-valuation: earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported results.

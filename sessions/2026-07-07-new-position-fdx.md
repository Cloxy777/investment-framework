# NEW POSITION (Quality Score Engine addendum) — FDX (FedEx Corporation) — 2026-07-07

**Task type:** NEW POSITION — Quality Score Engine addendum (lightweight, per the CCL/BULL/CDR precedent), not a full re-evaluation
**Date:** 7 Jul 2026
**Ticker:** FDX (FedEx Corporation, NYSE)
**Prior session:** [2026-06-21-new-position-fdx.md](2026-06-21-new-position-fdx.md) — Phase 01 FAIL (5 of 8 criteria: gross margin, net margin, ROIC, revenue 3yr CAGR, net debt/EBITDA), predates the 2026-06-29 Quality Score engine addition — FDX has never had a Quality Score computed until this session
**Current FDX portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session exists, and the branching decision

The 06-21 session flagged a material data-consistency gap: FedEx completed the spin-off of FedEx Freight (FDXF) on 1 June 2026, but all financial-statement data available at the time was pre-spinoff (consolidated, including Freight) while the live price/share count were already post-spinoff. That session's dominant "next review trigger" was FedEx's Q4/FY2026 earnings, confirmed for 23 June 2026, flagged as **"the first full post-spinoff quarterly report"** that could finally resolve the mismatch.

This session's task was to check whether that earnings release happened and, if it produced clean post-spinoff restated financials, to do a **full re-evaluation** (new dated session + watchlist file, all 8 Phase 01 criteria re-verified fresh). If clean post-spinoff data was **not** available, the task called for the lighter **Quality Score Engine addendum** treatment instead — refresh the Phase 01 numbers with the best available data, compute FDX's first-ever Quality Score, and append to the existing 06-21 watchlist file rather than creating a new one.

**Finding: Q4/FY2026 earnings were reported on schedule (23 June 2026), but they are the *last* pre-spinoff quarter, not the first post-spinoff one.** The spin-off legally closed 1 June 2026 — one day *after* the FY2026 fiscal year (and Q4) ended 31 May 2026. FedEx's own 8-K confirms FedEx Freight is still fully consolidated in the FY2026 results (segment revenue $8.795B included in the $94.720B FY2026 total), and explicitly states that a Form 8-K with recasted, discontinued-operations-basis financials for calendar 2024/2025 is not expected until **"mid-August 2026."** A second, previously-unknown complication also surfaced: FedEx's board separately approved a **change in fiscal year-end from 31 May to 31 December**, effective 1 June 2026 — meaning the next reporting period is a one-off 7-month "transition year" (June-December 2026), not a normal quarter, pushing a clean, comparable, standard-cadence post-spinoff report even further out.

**This confirms the addendum path, not a full re-evaluation.** No clean, restated, post-spinoff-comparable financial statements exist yet for FedEx as of this session — confirmed via FedEx's own primary-source disclosure, not inferred.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$311.57** | IBKR `get_price_snapshot`, contract_id 5100583, ts 2026-07-07 19:20:54 UTC, `is_close: false` |
| Cross-check | $311.18 (chart, 19:14:41 UTC) / $311.30 (quoteSummary, 19:15:09 UTC) | Yahoo Finance, both live, consistent within ~0.1-0.4% of IBKR |
| 52-week range | $174.13-$345.37 (Yahoo) / $171.32-$345.00 (IBKR, immaterial rounding-vintage difference) | Yahoo `summaryDetail`, IBKR `misc_statistics` |
| Analyst consensus PT | Mean $349.72, median $354.00 (23 analysts, up from 16 on 06-21), "buy" | Yahoo `financialData` |
| 10Y Treasury yield | 4.529% | Yahoo `^TNX`, for the record only — Rate Gate not run, Phase 01 fails first |

Change since 06-21 ($326.20): **-4.49%** — well short of the >15% Rule 9 threshold, and explained regardless by the earnings/guidance event below.

**Data-sourcing note:** `yfinance`'s own HTTP client (`curl_cffi`, browser-impersonation mode) could not complete a TLS handshake through this session's egress proxy (`curl: (35) Recv failure: Connection reset by peer`) — the same known limitation flagged in the 2026-07-06 CCL addendum. Worked around it identically: calling Yahoo Finance's public `quoteSummary` and `fundamentals-timeseries` endpoints directly via plain `requests` (which the proxy handles fine), using the same field names (`TotalRevenue`, `GrossProfit`, `CostOfRevenue`, `EBIT`, `EBITDA`, `NetIncome`, `PretaxIncome`, `TaxRateForCalcs`, `FreeCashFlow`, `OperatingCashFlow`, `CapitalExpenditure`, `TotalDebt`, `InvestedCapital`, `CapitalLeaseObligations`, `StockholdersEquity`, `CashAndCashEquivalents`) that `yfinance` itself uses internally. Same underlying data source as the 06-21 session's `t.financials`/`t.cashflow`/`t.quarterly_*` calls, fetched via a different HTTP path.

**A genuine, material data-source lag discovered this session:** Yahoo's `fundamentals-timeseries` endpoint (both quarterly and annual) still returns **FY2025 as its latest annual period and 2026-02-28 (Q3 FY2026) as its latest quarter** — it has not ingested FedEx's 23 June 2026 earnings release at all, despite that release being public for 2 weeks by this session's date. This is why the freshest FY2026 figures below were sourced directly from FedEx's own SEC 8-K (EX-99.1, filed 2026-06-23) rather than from Yahoo — the primary source, not a data-vendor reconstruction, and unaffected by the vendor lag.

---

## 2. Q4/FY2026 earnings — what was reported, and the two compounding corporate-structure findings

Source: [SEC 8-K EX-99.1, filed 2026-06-23](https://www.sec.gov/Archives/edgar/data/1048911/000104891126000050/fdx-earningsreleasefy2026q4.htm) (primary source, fetched and parsed directly this session; note the CIK must be passed without leading zeros to sec.gov or it 301-redirects, and SEC.gov requires a declared, non-generic `User-Agent` string or it blocks the request with a 200-OK "undeclared automated tool" HTML page rather than a clean HTTP error).

- Revenue FY2026 (full year): **$94.720B** (FY2025: $87.926B, +8% YoY)
- Operating income (GAAP) FY2026: **$5.463B** (FY2025: $5.217B, +5% YoY)
- Net income FY2026: **$4.433B** (FY2025: $4.092B, +8% YoY)
- Diluted EPS FY2026: **$18.55** (FY2025: $16.81, +10% YoY); adjusted diluted EPS $20.24
- Q4 alone: adjusted EPS $6.31 vs. $5.92-5.96 Street estimate (beat); revenue $25.01B vs. ~$24.0B estimate (beat)
- Stock reaction: down ~4-6% on the print despite the beat, on transition-year guidance and stranded-cost concerns tied to the Freight spin-off (per WebSearch/CNBC/Investing.com coverage, used only as market-reaction context, never as a scored input)
- CapEx FY2026 $3.809B, D&A $4.369B, OCF $8.925B → FCF (OCF−CapEx) $5.116B
- Cash and cash equivalents (31 May 2026): **$13.311B**, up from $5.502B a year earlier — the 8-K explicitly discloses this "includes a $4.1 billion cash dividend from the FedEx Freight spin-off" (received pre-close) and "approximately $800 million in IEEPA tariff refunds held for refund to customers" (a pass-through liability, not free corporate cash — flagged, not adjusted for, per "never invent or estimate")
- Total debt (current + long-term): $24.969B; operating lease liabilities (current + long-term): $17.229B; combined (this framework's "include operating leases" convention for capital-intensive businesses): $42.198B
- Effective tax rate FY2026: 23.48% (Provision for Income Taxes $1.360B / Pretax Income $5.793B)

**Finding 1 — the Freight spin-off, confirmed still not reflected in FY2026's reported financials.** FedEx Freight completed its spin-off 1 June 2026, one day after the FY2026 (and Q4) period ended 31 May 2026. The 8-K's own segment-revenue bridge shows "FedEx Freight segment" revenue of $8.795B included within the $94.720B FY2026 total — i.e., **FY2026 as reported is the last fully-consolidated, pre-spinoff fiscal year, not a post-spinoff one.** Footnote 8 of the 8-K states: *"FedEx expects to file a Current Report on Form 8-K including recasted and resegmented financial statements for calendar 2024 and 2025, reflecting FedEx Freight as discontinued operations, by mid-August 2026."* This is a primary-source, dated confirmation that clean post-spinoff comparable financials do not exist yet.

**Finding 2 — a previously-unknown Fiscal Year Change, independent of the spin-off.** The same 8-K discloses: *"In January 2025, the FedEx Board of Directors approved a change in the company's fiscal year end from May 31 to December 31. The fiscal year change became effective for the period beginning June 1, 2026."* FedEx's FY2026 (ended 31 May 2026) was therefore the last "old-calendar" fiscal year; the next reported period is a one-off **7-month "June-through-December 2026 transition year"** (the 8-K's own guidance section is framed as "CY 2026 Outlook" rather than "FY2027," and cites "costs related to the fiscal year change" as a distinct, excluded adjustment item). This compounds the spin-off mismatch: even once Freight is cleanly separated out via the mid-August recast, the next full report on the new calendar-year cadence won't land until early 2027.

**Rule 9 checklist (all 6 categories explicitly checked):**

| Category | Result |
|---|---|
| Earnings | **YES** — Q4/FY2026 reported 2026-06-23 as scheduled. |
| Guidance revision | CY2026 adjusted diluted EPS from continuing operations guided to $16.90-$18.10 (vs. a recast CY2025 baseline of $15.00) — on a basis not yet comparable to any figure this framework has previously scored. |
| Management change | None disclosed. |
| M&A / corporate-structure | **Two events** — the Freight spin-off close (confirmed still not reflected in FY2026 financials) and the newly-surfaced Fiscal Year Change — both detailed above. |
| Macro shift | None separately disclosed beyond fuel-cost pressure (~66% higher YoY in Q4) already absorbed into a beat. |
| >15% unexplained price move | No (-4.49%, and explained regardless). |

---

## 3. Refreshed Phase 01 criteria (best available data)

Full detail, formulas, and the complete 8-criterion table are in the [watchlist addendum](../watchlist/not-in-portfolio/FDX/FDX-2026-06-21.md); summarized here:

| Check | Refreshed Value | Threshold | Result | vs. 06-21 |
|---|---|---|---|---|
| Gross margin | 22.04% — unchanged, could not be refreshed (data gap: FedEx's income statement has no COGS/gross-profit line, and Yahoo's reconstruction hasn't updated past Q3 FY2026) | >40% | FAIL | unchanged |
| Net margin | 4.68% (FY2026 annual, 8-K) | >12% | FAIL | slightly worse (4.88%→4.68%) |
| ROIC | 7.59% (fresh NOPAT ÷ Yahoo's last-published, 3-months-stale Invested Capital — flagged data gap) | >15% | FAIL | worse (9.25%→7.59%), partly a denominator artifact |
| Revenue 3yr CAGR | **+1.66%** (FY2023→FY2026) | >8% | FAIL | crossed from negative to positive (-2.03%→+1.66%) |
| FCF positive 3yr | FY2024-FY2026 all positive, FY2026 strongest at $5.116B | required | PASS | stronger |
| Net debt/EBITDA | 2.94x (31-May-2026 basis, incl. leases) | <2.5x | FAIL | improved (3.08x→2.94x), still fails |
| FCF yield | 6.89% | >4% | PASS | improved (5.62%→6.89%) |
| EV/EBIT | 18.88x | <20x | PASS | slightly worse (16.64x→18.88x), still passes |

**Still 5 of 8 criteria fail — the identical five as 06-21.** The Phase 01 verdict is unchanged; the most notable shift is revenue 3yr CAGR turning positive for the first time in this framework's coverage of FDX, though still well short of the 8% bar.

---

## 4. Quality Score Engine — FDX's first-ever computation

Per [framework/quality-scoring.md](../framework/quality-scoring.md) (methodology version 2026-06-29). Full sub-score detail and moat-signal citations are in the [watchlist addendum](../watchlist/not-in-portfolio/FDX/FDX-2026-06-21.md); summarized here:

| Sub-score (weight) | Score |
|---|---|
| Profitability (25%) | 20.46 |
| Margins (15%) | 27.55 |
| Growth (20%) | 16.64 |
| Balance Sheet (15%) | 26.55 |
| Moat (15%) | 40.0 |
| FCF Quality (10%) | 100.0 |

```
Quality Score = 20.46×0.25 + 27.55×0.15 + 16.64×0.20 + 26.55×0.15 + 40.0×0.15 + 100.0×0.10
              = 5.11 + 4.13 + 3.33 + 3.98 + 6.00 + 10.00
              = 32.6
```

**Quality Score = 32.6 / 100.0 — fails the 80.0+ gate decisively** (more decisively than the CCL precedent's 57.7), and independently a second time via the Net Debt/EBITDA hard disqualifier (2.94x vs. the 2.5x standard threshold). The FCF-positivity and FCF/NI-conversion hard disqualifiers do **not** fire.

### Moat Signal detail (cited evidence required per signal)

| Signal | Result | Evidence |
|---|---|---|
| Market share stable or growing | **FALSE** | FreightWaves (via WebSearch): FedEx and UPS are losing US parcel market share to Amazon Logistics and private retail delivery networks; FedEx held 16.5% of 2024 US package volume, behind USPS (30.8%) and Amazon Logistics (28.2%) — the opposite of "stable or growing" |
| Brand premium (pricing power) | **TRUE** | FedEx 8-K, Federal Express segment highlights: Q4 FY2026 composite package yield $17.90 vs. $16.14 a year earlier (+11% YoY) while total average daily package volume simultaneously grew +2% YoY (17,083K vs. 16,794K) — price increases *with* volume growth; full-year composite yield +6% YoY on +3% YoY volume confirms the pattern held all year |
| Network effect | FALSE | No two-sided marketplace dynamics for a physical parcel/freight network |
| Switching costs | FALSE | No documented contractual-lock-in or integration-depth data found in the time available |
| Scale cost advantage | **TRUE** | Supply Chain Dive (via WebSearch): Network 2.0 rollout has produced "a 10% reduction in pickup and delivery costs in markets it's rolled out in, thanks to the elimination of overlapping routes" |

Moat_Score = (2/5) × 100 = **40.0**

---

## 5. Recommendation

# **PASS — Quality Score 32.6/100.0, fails the 80.0+ gate (also independently failed by the Net Debt/EBITDA hard disqualifier). Do not enter. Watchlist addendum appended, no new dated file created.**

FedEx's Q4/FY2026 earnings beat estimates and full-year revenue/earnings both grew meaningfully, but this remains a fully pre-spinoff, structurally thin-margin, capital-intensive business by every quantitative measure this framework tracks — net margin, ROIC, and gross margin all remain far below threshold, and net debt/EBITDA, while improving, has not crossed under 2.5x. The genuinely new information this session — the Freight spin-off's mid-August 2026 recast commitment and the previously-unknown fiscal year change to a 31 December year-end — both push a clean, comparable post-spinoff data basis further out than the 06-21 session anticipated, not closer. FDX's first Quality Score computation (32.6) confirms the same conclusion from an independent angle, more decisively than the CCL precedent.

**No position opened — nothing to log in `decisions/`.**

---

## 6. Files touched this session

- `watchlist/not-in-portfolio/FDX/FDX-2026-06-21.md` — appended the Rule 9 check, refreshed Phase 01 table, and Quality Score addendum as a dated note (no new file, per this task's branching instruction — Phase 01 verdict unchanged); updated the file's Glossary section
- `framework/glossary.md` — added **Fiscal Year Change**
- `sessions/2026-07-07-new-position-fdx.md` — this file

`watchlist/STALE.md` was not touched (FDX was not listed there — it predates the Quality Score engine but was never a "stale re-score" case, it was a Phase 01 FAIL that had never been scored at all). No `git` commands were run.

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **8-K** — a US company's "current report" filed with the SEC disclosing a material event between regular filings; the primary source for FedEx's Q4/FY2026 earnings release used throughout this session.
- **CAGR** — Compound Annual Growth Rate.
- **CapEx** — Capital Expenditure.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization.
- **EPS** — Earnings Per Share.
- **EV / EV/EBIT** — Enterprise Value / Enterprise Value divided by EBIT.
- **FCF / FCF Yield / FCF/NI conversion ratio** — Free Cash Flow, its ratio to market cap, and its ratio to Net Income (an earnings-quality check).
- **Fiscal Year Change** — a company's formal change of its fiscal year-end date, producing a one-off "transition period" — FedEx moved from 31 May to 31 December, effective 1 June 2026, discovered and documented for the first time in this framework in this session.
- **GAAP** — Generally Accepted Accounting Principles.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted score; FDX's Net Debt/EBITDA fires this one independently of the 32.6 weighted score.
- **Invested Capital** — the total capital (debt + equity, netted for cash) put to work in a business — the ROIC denominator.
- **Moat** — a durable competitive advantage.
- **NOPAT** — Net Operating Profit After Tax, the numerator of the ROIC calculation.
- **Net Debt/EBITDA** — a leverage ratio; this framework's primary balance-sheet-risk gate.
- **PT (Price Target)** — an analyst's forecast of future share price.
- **Quality Score** — this framework's 0.0-100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02. FDX scores 32.6 on its first-ever computation.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 9** — this framework's list of events that force an immediate re-valuation: earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move.
- **Spin-off** — a corporate transaction where a company separates part of its business into a new, independently-traded public company; FedEx's 1 June 2026 spin-off of FedEx Freight (FDXF).
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results.

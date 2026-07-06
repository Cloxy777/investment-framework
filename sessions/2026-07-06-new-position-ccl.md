# NEW POSITION (Quality Score Engine addendum) — CCL (Carnival Corporation & plc) — 2026-07-06

**Task type:** NEW POSITION — Quality Score Engine addendum (lightweight, per the BULL/CDR precedent), not a full re-evaluation
**Date:** 6 Jul 2026
**Ticker:** CCL (Carnival Corporation Ltd., NYSE) — see §1 for a material corporate-structure change affecting how this ticker should be referenced going forward
**Prior session:** [2026-06-21-new-position-ccl.md](2026-06-21-new-position-ccl.md) — Phase 01 FAIL (3 of 8 criteria: net margin, ROIC, net debt/EBITDA), predates the 2026-06-29 Quality Score engine addition — CCL has never had a Quality Score computed until this session
**Current CCL portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session exists

CCL's 06-21 session failed Phase 01 (the binary quality screen that predates the 2026-06-29 Quality Score engine) and was never scored under the new 0-100.0 engine. Per this task's explicit scope, this session does **two things only**:

1. A Rule 9 check — CCL's Q2 FY2026 earnings were confirmed for 2026-06-23 (2 days after the 06-21 session); check whether they were reported, what they showed, and whether any other Rule 9 trigger (guidance revision, management change, M&A, macro shift, >15% unexplained price move) fired since 06-21.
2. Compute CCL's first-ever Quality Score under the current engine, with every sub-score shown.

Per the task's branching instruction, a fuller Phase 01 re-check (or a new dated watchlist file) is only warranted if the Q2 earnings constitute a Rule 9 trigger that flips the verdict on the three previously-failing criteria (net margin, ROIC, net debt/EBITDA) — all three were "trending toward passing" per the 06-21 session's Next Review Trigger notes. As shown below, none of the three actually crossed their thresholds, so this stays an addendum appended to the existing watchlist file, not a new one.

---

## 1. Live Price (Rule 0) and a material corporate-structure finding

| Field | Value | Source |
|---|---|---|
| **Live price used (CCL)** | **$27.95** | IBKR `get_price_snapshot`, contract_id 878372298, pre-market snapshot, `ts` 1783318444 → 2026-07-06 06:14:04 UTC, `is_close: false` |
| 52-week range | $23.45 – $34.03 | Yahoo Finance `summaryDetail` (fetched fresh this session) |
| Analyst consensus PT | Mean $35.86, median $35.00 (24 analysts), "buy" | Yahoo Finance `financialData`/`defaultKeyStatistics` |
| Baseline (06-21) | $30.87 | Prior session |
| Change since 06-21 | **-9.4%** | Computed |

**CUK cross-check attempted and found stale/invalid:** IBKR's snapshot for CUK (contract_id 13796753) returned $27.47 with `is_close: true` and no `change` data — a dead quote. Investigating why turned up a material finding (not from the original Telegram trigger, sourced independently via SEC/WebSearch): **effective 7 May 2026, Carnival completed the unification of its dual-listed-company (DLC) structure.** Carnival plc (CUK) shareholders exchanged their shares/ADSs 1-for-1 into Carnival Corporation Ltd. shares via a UK scheme of arrangement; CUK's separate NYSE and London Stock Exchange listings were cancelled; and the combined entity redomiciled its legal incorporation from Panama to Bermuda as "Carnival Corporation Ltd." Confirmed two ways:
- **Primary source:** the Q2 FY2026 8-K's own consolidated balance sheet shows "Carnival plc ordinary shares... no shares issued at 2026" vs. 217M shares issued at the prior year-end — i.e., CUK's share class had already gone to zero by 2026-05-31.
- **Secondary corroboration:** WebSearch (TipRanks, The Globe and Mail) — unification agreement signed 20 Feb 2026, completed 7 May 2026.

**Practical consequence:** the entire "combine CCL+CUK market caps/shares into one economic entity" methodology that anchored the 06-21 session's Phase 01 inputs is now moot — there is only one listed security. This is also confirmed mechanically: Yahoo's `sharesOutstanding` field for CCL now equals `impliedSharesOutstanding` exactly (1.36965B), whereas on 06-21 the two diverged (1.239B CCL-only vs. 1.385B implied-combined) precisely because the combination hadn't happened in the reporting yet. All financials pulled this session (TTM through Q2 FY2026) already reflect the single, unified consolidated entity — no manual combination needed anymore, which is a genuine simplification over 06-21's methodology.

This DLC unification is treated as a Rule 9 "M&A/corporate-structure" category event — flagged and explained in full above — but it is a **legal/structural simplification of an already-combined economic business**, not a change to the underlying operations, and it does not itself move any Phase 01 quantitative criterion.

**Rule 9 checklist (all 6 categories explicitly checked):**

| Category | Result |
|---|---|
| Earnings | **YES** — Q2 FY2026 (quarter ended 2026-05-31) reported 2026-06-23 as scheduled. See §2. |
| Guidance revision | FY2026 outlook updated (net yields ~+3.2% vs. record 2025; adjusted cruise costs ex-fuel ~+3.7%) — routine post-beat update, not a negative surprise. |
| Management change | None — Josh Weinstein (CEO), David Bernstein (CFO) unchanged. |
| M&A | None directly, but the DLC unification/Bermuda redomiciliation above is the closest-fitting category — flagged in full. |
| Macro shift | Management explicitly disclosed a "prolonged conflict in the Middle East" causing "transitory moderation" in Mediterranean/European bookings, plus ~30% higher YoY fuel prices — real, quantified, company-sourced (not the original 06-21 Telegram post's framing, which was never used as data per that session's Rule 0 discipline). |
| >15% unexplained price move | No — (-9.4%), and explained by the above regardless. |

---

## 2. Q2 FY2026 earnings — what was reported

Source: [SEC 8-K, EX-99.1, filed 2026-06-23](https://www.sec.gov/Archives/edgar/data/0000815097/000081509726000086/a20262qearningsrelease8-k.htm) (primary source, fetched and parsed directly this session).

- Record Q2 revenue: **$6.663B** (vs. $6.328B Q2 FY2025)
- Net income: **$537M**; adjusted net income: **$569M** (+20%+ YoY)
- Adjusted EBITDA: **$1.582B** (record)
- Diluted EPS $0.39, adjusted EPS $0.41 (vs. $0.34 Street estimate)
- 12th consecutive quarter of record net yields; net yields (constant currency) +2.2% YoY
- Occupancy 104% (flat YoY) — i.e., the yield increase came from pricing, not from cramming more passengers per berth
- Debt (current + long-term): **$24.889B** (down from $26.640B at FY2025-end)
- Cash and cash equivalents: **$2.243B**
- Net debt to adjusted EBITDA: **3.1x**, "more than half a point improvement from just one year ago" (management's own words) — Moody's issued a credit-rating upgrade
- Results exceeded the company's own March guidance by $100M despite ~30% higher YoY fuel costs and the Middle East-driven booking headwind noted above

This is genuinely strong operating performance. It does **not**, however, flip any of the three Phase 01 criteria CCL was failing on 06-21 — see §3.

---

## 3. Refreshed TTM financials (through Q2 FY2026, quarter ended 2026-05-31)

**Data-sourcing note:** `yfinance`'s own HTTP client (`curl_cffi`, browser-impersonation mode) could not complete a TLS handshake through this session's egress proxy (`curl: (35) Recv failure: Connection reset by peer` — impersonated TLS fingerprints are one of the proxy's documented unsupported-client classes). Worked around this by calling Yahoo Finance's public `fundamentals-timeseries` and `quoteSummary` endpoints directly via plain `requests` (which the proxy handles fine) using the exact field names (`TotalRevenue`, `GrossProfit`, `EBIT`, `EBITDA`, `NetIncome`, `TaxRateForCalcs`, `FreeCashFlow`, `OperatingCashFlow`, `CapitalExpenditure`, `TotalDebt`, `NetDebt`, `CashAndCashEquivalents`, `StockholdersEquity`, `InvestedCapital`) that `yfinance`'s own source code uses internally — same underlying data source and field definitions as the 06-21 session's `t.financials`/`t.cashflow`/`t.quarterly_*` calls, just fetched via a different HTTP path. Cross-checked figures against the primary-source SEC 8-K wherever the two could diverge (see the Net Debt/EBITDA note below).

### Quarterly income statement (5 most recent)

| Quarter end | Revenue | Gross Profit | EBIT | EBITDA | Net Income | Tax Rate |
|---|---|---|---|---|---|---|
| 2025-05-31 | $6.328B | $2.442B | $0.926B | $1.618B | $0.565B | 2.91% |
| 2025-08-31 | $8.153B | $3.768B | $2.174B | $2.892B | $1.852B | 0.32% |
| 2025-11-30 | $6.330B | $2.421B | $0.719B | $1.445B | $0.422B | 21.0% |
| 2026-02-28 | $6.165B | $2.226B | $0.571B | $1.267B | $0.258B | 6.07% |
| 2026-05-31 | $6.663B | $2.438B | $0.840B | $1.563B | $0.537B | 3.06% |

### TTM (through 2026-05-31, Yahoo's own "trailing" timeseries — sums to the same 4 quarters above)

| Metric | TTM Value |
|---|---|
| Total Revenue | $27.311B |
| Gross Profit | $10.852B |
| EBIT | $4.298B |
| EBITDA (GAAP) | $7.161B |
| EBITDA (adjusted, per company's own Q2 disclosure) | ~$7.302B (implied from the disclosed 3.1x net-debt/EBITDA ratio: $22.646B ÷ 3.1 ≈ $7.305B; also matches `financialData.ebitda` $7.302B) |
| Net Income | $3.069B |
| Pretax Income | $3.090B |
| Tax Provision | $0.022B → effective tax rate 0.71% |
| Operating Cash Flow | $6.794B |
| CapEx | -$3.594B |
| Free Cash Flow (OCF − CapEx) | $3.200B — reconciles exactly to Yahoo's own reported `FreeCashFlow` field |

### Balance sheet (2026-05-31, per the 8-K's own disclosure — the more precise primary source)

| Metric | Value |
|---|---|
| Debt (current + long-term), company's own definition | $24.889B |
| Cash and cash equivalents | $2.243B |
| **Net Debt (company-disclosed basis)** | **$22.646B** |
| Stockholders' equity | $12.984B (total, incl. minority interest $16M) |
| Invested Capital (Yahoo fundamentals-timeseries, quarterly — newly available; not separately reported as of 06-21) | $37.856B |

**A real, flagged data discrepancy:** Yahoo's own `TotalDebt` field for this same quarter reports **$26.170B**, not $24.889B — a $1.281B gap that matches almost exactly the sum of the 8-K's disclosed current + long-term *operating lease* liabilities ($168M + $1.113B = $1.281B). Conclusion: Yahoo's `TotalDebt` field appears to fold in operating-lease liabilities that the company's own "Debt (current and long-term)" line — the one management uses to compute and disclose its own 3.1x net-debt/adjusted-EBITDA ratio — excludes. Per "never invent or estimate financial data," both figures are reported below rather than silently reconciled:

```
Net Debt/EBITDA (company-disclosed basis, matches management's own reported 3.1x exactly):
  Net Debt $22.646B (Debt $24.889B − Cash $2.243B) ÷ TTM adjusted EBITDA $7.302B = 3.10×

Net Debt/EBITDA (yfinance TotalDebt basis, lease-inclusive, for continuity with 06-21's methodology):
  Net Debt $23.927B (TotalDebt $26.170B − Cash $2.243B) ÷ TTM GAAP EBITDA $7.161B = 3.34×
```

Both are reported in the addendum; **the conclusion is unchanged either way** — both sit above the <2.5× standard threshold, both represent an improvement from 06-21's 3.47-3.49× figure, and both still fail the framework's Net Debt/EBITDA gate.

### Annual income statement and cash flow (unchanged from 06-21 — FY2025 is still the latest complete fiscal year; fiscal year ends ~Nov 30)

| FY | Revenue | Gross Profit | EBIT | Net Income | FCF | OCF | CapEx |
|---|---|---|---|---|---|---|---|
| FY2022 | $12.169B | $0.412B | −$4.471B | −$6.093B | −$6.610B | −$1.670B | −$4.940B |
| FY2023 | $21.593B | $7.276B | $2.004B | −$0.074B | $0.997B | $4.281B | −$3.284B |
| FY2024 | $25.021B | $9.383B | $3.670B | $1.916B | $1.297B | $5.923B | −$4.626B |
| FY2025 | $26.621B | $10.674B | $4.121B | $2.760B | $2.607B | $6.218B | −$3.611B |

Gross margin by fiscal year: FY2022 3.39% (COVID trough — this figure was reported as $412M/$12.169B in both the 06-21 and this session's data pulls, unchanged), FY2023 33.70%, FY2024 37.50%, FY2025 40.10% — cited as the structural-expansion evidence for the Quality Score's Margins sub-score bonus (see §4).

FCF/NI conversion ratio by fiscal year (unchanged from 06-21): FY2024 67.7% (fails 70%, no growth-capex explanation on record — CapEx was actually higher in FY2024 than FY2025), FY2025 94.5% (passes). Only 1 of the last 2 complete fiscal years fails — the Quality Score's "2+ consecutive years <70%" hard disqualifier does not fire.

### Recomputed ratios (TTM through Q2 FY2026)

```
Net Margin (TTM)   = $3.069B / $27.311B = 11.24%   (06-21: 11.48% — essentially flat, still fails >12%)
Gross Margin (TTM) = $10.852B / $27.311B = 39.73%  (06-21: 40.25% — essentially flat, a hair below 40%)
ROIC (TTM, latest-qtr IC) = NOPAT $4.267B [EBIT $4.298B × (1 − 0.71% effective tax rate)] / Invested Capital $37.856B = 11.28%
ROIC (TTM, FY2025-annual-IC cross-check, for methodology continuity with 06-21) = $4.267B / $38.924B = 10.96%
  (06-21: 11.22% on the FY2025-annual-IC basis — essentially flat, still fails >15%)
```

**None of the three previously-failing Phase 01 criteria (net margin, ROIC, net debt/EBITDA) crossed their thresholds.** Net debt/EBITDA improved meaningfully (3.47-3.49× → 3.10-3.34×, continuing the deleveraging trend the 06-21 session flagged as the metric "most likely to flip the gate result if the recovery continues") but has not yet crossed under 2.5×. Net margin and ROIC are both essentially flat, within noise of their 06-21 values. **Per this task's explicit branching instruction, this confirms the addendum-only path — no fuller Phase 01 re-check or new dated file is warranted.**

---

## 4. Quality Score Engine — CCL's first-ever computation

Per [framework/quality-scoring.md](../framework/quality-scoring.md) (methodology version 2026-06-29). Full detail and the worked formula are in the [watchlist addendum](../watchlist/not-in-portfolio/CCL/CCL-2026-06-21.md#glossary); summarized here:

| Sub-score (weight) | Score |
|---|---|
| Profitability (25%) | 37.52 |
| Margins (15%) | 59.67 |
| Growth (20%) | 100.0 |
| Balance Sheet (15%) | 22.47 |
| Moat (15%) | 40.0 |
| FCF Quality (10%) | 100.0 |

```
Quality Score = 37.52×0.25 + 59.67×0.15 + 100.0×0.20 + 22.47×0.15 + 40.0×0.15 + 100.0×0.10
              = 9.38 + 8.95 + 20.00 + 3.37 + 6.00 + 10.00
              = 57.7
```

**Quality Score = 57.7 / 100.0 — fails the 80.0+ gate.** CCL fails two independent ways simultaneously:
1. **The weighted score itself** (57.7 < 80.0) — driven mainly by weak Profitability (37.52, reflecting the still-sub-threshold net margin/ROIC) and a middling Moat score (40.0 — only 2 of 5 signals cleared the evidentiary bar).
2. **A hard disqualifier**, independent of the weighted score: Net Debt/EBITDA (3.10-3.34×) sits above the 2.5× standard threshold. Per quality-scoring.md, this "fails regardless of weighted score" — CCL would fail the gate even if the weighted average had cleared 80.0.

The FCF-positivity and FCF/NI-conversion hard disqualifiers do **not** fire (FCF positive 3+ consecutive years including TTM; only 1 of the last 2 complete fiscal years fell below 70% FCF/NI conversion, not 2+ consecutive) — unlike the CD Projekt (CDR) precedent, where the FCF-positivity disqualifier fired independently.

**No Composite Score computed** (requires clearing the 80.0+ gate first). **No Phase 02 valuation work performed** (out of scope for this addendum, and moot given the gate result).

### Moat Signal detail (cited evidence required per signal)

| Signal | Result | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | 41.5% of global cruise passenger volume, 36% of industry revenue (2025) — third-party cruise-market-share research (hoperesearchgroup.com, porteconomicsmanagement.org, via WebSearch); Carnival + Royal Caribbean together hold 62% of the market |
| Brand premium (pricing power) | **TRUE** | Q2 FY2026 8-K: 12th consecutive quarter of record net yields, +2.2% constant-currency, while occupancy held flat at 104% YoY — price increases without volume loss |
| Network effect | FALSE | No two-sided marketplace dynamics for a cruise line |
| Switching costs | FALSE | No documented lock-in mechanism; cruise customers can freely substitute across operators (RCL, NCLH) or entirely different vacation types |
| Scale cost advantage | FALSE | No cost-per-unit data found showing a documented gap vs. smaller competitors (searched; not located in the time available for this lightweight addendum) |

Moat_Score = (2/5) × 100 = **40.0**

---

## 5. Recommendation

# **PASS — Quality Score 57.7/100.0, fails the 80.0+ gate (also independently failed by the Net Debt/EBITDA hard disqualifier). Do not enter. Watchlist addendum appended, no new file created.**

Q2 FY2026 earnings were genuinely strong (record revenue, 12th consecutive quarter of record net yields, continued deleveraging, a Moody's upgrade) and the company completed a significant structural simplification (DLC unification, Bermuda redomiciliation) — but none of this changes the substance of the 06-21 Phase 01 FAIL: net margin and ROIC remain essentially flat and below threshold, and net debt/EBITDA, while improving, has not yet crossed under 2.5×. CCL's first Quality Score computation confirms the same conclusion from a different angle — 57.7 is well short of 80.0, and the balance-sheet leverage alone is a hard disqualifier independent of the weighted score.

**No position opened — nothing to log in `decisions/`.**

---

## 6. Files touched this session

- `watchlist/not-in-portfolio/CCL/CCL-2026-06-21.md` — appended the Rule 9 check + Quality Score addendum as a dated note (no new file, per the task's branching instruction — no Phase 01 verdict change)
- `framework/glossary.md` — added **ADS (American Depositary Share)**, **Redomiciliation**, and **Scheme of arrangement**; updated the existing **DLC (Dual-Listed Company)** entry to record the May 2026 unification
- `sessions/2026-07-06-new-position-ccl.md` — this file

`watchlist/STALE.md` was not touched (CCL was not listed there — it predates the Quality Score engine but was never a "stale re-score" case, it was a Phase 01 FAIL that had never been scored at all).

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **8-K** — a US company's "current report" filed with the SEC disclosing a material event between regular filings; used here as the primary source for the Q2 FY2026 earnings release.
- **ADR / ADS (American Depositary Receipt / Share)** — a US-listed security (and its underlying share) representing a non-US company's stock; Carnival plc's ADSs were cancelled and exchanged 1-for-1 into CCL shares in the May 2026 unification.
- **CAGR** — Compound Annual Growth Rate.
- **CapEx** — Capital Expenditure.
- **DLC (Dual-Listed Company)** — the now-retired structure under which CCL and CUK traded as separate shares of one combined economic business; unified into a single entity 7 May 2026.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization.
- **Effective tax rate** — the actual share of pretax income paid as tax; CCL's remains near-zero (0.71% TTM) due to international cruise-shipping income tax treatment, not an anomaly.
- **EPS** — Earnings Per Share.
- **FCF** — Free Cash Flow.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income, an earnings-quality check.
- **GAAP** — Generally Accepted Accounting Principles.
- **Gross Margin** — Gross Profit ÷ Revenue.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted score; CCL's Net Debt/EBITDA fires this one independently of the 57.7 weighted score.
- **Moat** — a durable competitive advantage.
- **NOPAT** — Net Operating Profit After Tax, the numerator of ROIC.
- **Net Debt/EBITDA** — a leverage ratio; this framework's primary balance-sheet-risk gate.
- **Quality Score** — this framework's 0-100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02. CCL scores 57.7 on its first-ever computation.
- **Redomiciliation** — moving a company's legal incorporation to a new jurisdiction; CCL redomiciled from Panama to Bermuda on 7 May 2026.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 9** — this framework's list of events that force an immediate re-valuation: earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move.
- **Scheme of arrangement** — the UK/Bermuda-law court-approved mechanism used to exchange Carnival plc shares into Carnival Corporation Ltd. shares.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results.

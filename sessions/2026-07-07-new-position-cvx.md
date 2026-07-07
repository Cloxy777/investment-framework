# NEW POSITION (Quality Score Engine addendum) — CVX (Chevron Corporation) — 2026-07-07

**Task type:** NEW POSITION — Quality Score Engine addendum (per the CCL/CDR precedent), not a full re-evaluation
**Date:** 7 Jul 2026
**Ticker:** CVX (Chevron Corporation, NYSE)
**Prior session:** [2026-06-22-new-position-cvx.md](2026-06-22-new-position-cvx.md) — Phase 01 FAIL (4 of 8 criteria: gross margin, net margin, ROIC, revenue 3yr CAGR), predates the 2026-06-29 Quality Score engine addition — CVX has never had a Quality Score computed until this session
**Current CVX portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session exists

CVX's 06-22 session failed Phase 01 (the binary quality screen that predates the 2026-06-29 Quality Score engine) and was never scored under the new 0–100.0 engine. Per this task's explicit scope, this session does two things only:

1. A Rule 9 check — verify whether Chevron's Q2 FY2026 earnings (flagged as "expected late July 2026") have been reported, whether the Microsoft/Chevron West Texas data-center gas-power deal now has a financially-quantified update, whether any confirmed CEO/CFO insider buying has occurred, and whether any other Rule 9 trigger fired.
2. Compute CVX's first-ever Quality Score under the current engine, with every sub-score shown.

Per the task's branching instruction, a fuller Phase 01 re-check (or a new dated watchlist file) is only warranted if a Rule 9 trigger fired that changes the Phase 01 verdict. As shown below, no Rule 9 trigger fired, so this stays an addendum appended to the existing watchlist file, not a new one.

---

## 1. Live price (Rule 0)

- **IBKR `get_price_snapshot`**, contract_id 5684 (confirmed NYSE/USD conid from the 06-22 session): **$168.62**, snapshot ts 1783411581 → 2026-07-07 08:06:21 UTC, `is_close: false` (live quote).
- Baseline (06-22): $175.38.
- Change: **-3.86%** — well short of the >15% Rule 9 unexplained-move threshold, and an ordinary oil-price-linked fluctuation regardless (not "unexplained").
- yfinance was attempted first and failed with a network-level TLS connection reset on every call (`curl: (35) Recv failure: Connection reset by peer`), not a transient rate-limit — confirmed unreachable, not merely "overloaded." Per this task's explicit fallback instruction, SEC EDGAR's XBRL `companyfacts` API (`data.sec.gov/api/xbrl/companyfacts/CIK0000093410.json`) was used for all quantitative inputs below instead. IBKR remained available and was used for the live price.

## 2. Rule 9 check — all 6 categories

| Category | Result |
|---|---|
| Earnings | **NO — not yet reported.** Confirmed via SEC EDGAR: the latest filed 10-Q is still for the quarter ended 2026-03-31 (Q1 FY2026). Third-party earnings-date aggregators disagree (TipRanks: 24 July 2026; others: late-July/early-August window) — Chevron has not published an official date. This is the one still-pending item flagged at 06-22, unchanged. |
| Guidance revision | None identified since 06-22. |
| Management change | None — Mike Wirth (CEO), Eimear Bonner (CFO) unchanged. |
| M&A | None new (Hess remains the last completed deal). |
| Macro shift | No new company-specific disclosure found this session (not separately re-verified in depth, since Rule 9 doesn't require re-litigating an already-flagged ambient backdrop absent new information). |
| >15% unexplained price move | No (-3.86%, and not unexplained regardless). |

**Specifically-flagged watch items from 06-22, checked in detail:**

- **Microsoft/Chevron West Texas data-center deal — now financially quantified, but pre-FID.** The deal ("Project Kilby," a Chevron Energy Forge One / Microsoft 20-year power-purchase agreement for a 2.67 GW gas-fired plant) now has disclosed figures: $7–9B first-phase capital outlay (Bloomberg ~$7B, TD Securities ~$9B), targeting mid-teens returns, first power delivery 2028, long-term expansion target 5 GW into the 2030s. Sources: [Chevron newsroom](https://www.chevron.com/newsroom/2026/q2/chevron-signs-20-year-power-agreement-with-microsoft-for-west-texas-data-center), [Bloomberg](https://www.bloomberg.com/news/articles/2026-06-22/microsoft-chevron-sign-20-year-power-deal-for-texas-data-center), [Global Data Center Hub](https://www.globaldatacenterhub.com/p/chevron-and-microsoft-sign-9b-west). Chevron's own Final Investment Decision (FID) is expected only by end-2026 — not yet a binding capital commitment, no revenue/EBITDA guidance issued, zero trailing revenue impact. Treated as real and cited but too early-stage to count as a Growth sub-score TAM-expansion modifier (see §3).
- **CEO/CFO insider buying — still not confirmed; the one Form 4 event found is a sale.** CFO Eimear Bonner sold ~32,100 shares (~$5.6M) on 30 January 2026 at $175.00–$175.03, via option exercise (strike $132.69) immediately followed by sale, executed under a pre-existing 10b5-1 trading plan adopted 24 February 2025 — scheduled compensation-related selling, not discretionary open-market buying. No CEO (Wirth) Form 4 buying found. Source: [StockTitan](https://www.stocktitan.net/sec-filings/CVX/form-4-chevron-corp-insider-trading-activity-cbb86be04c3a.html). Turnaround Sub-Gate's insider condition remains **NOT MET**.

**Net effect: no Rule 9 trigger fired.** This stays a Quality Score addendum only — no fuller Phase 01 re-check, no new dated watchlist file.

## 3. Quality Score computation (SEC EDGAR XBRL basis)

### 3.1 Data-source notes

yfinance being unreachable required pulling every figure directly from SEC EDGAR's `companyfacts` API (CIK 0000093410). Three things worth flagging:

1. **Cross-validation:** TTM Net Margin (5.92%) and effective tax rate (37.78%) computed independently from SEC EDGAR tags land almost exactly on the 06-22 session's yfinance-derived figures (5.92%, 37.78%) despite a different revenue-tag basis — strong confidence in the Net Income figures on both sides.
2. **Revenue basis change exposed a yfinance inconsistency:** this session uses `RevenueFromContractWithCustomerExcludingAssessedTax` (Chevron's "Sales and other operating revenues" line — core operating revenue, excludes non-operating "other income"). Checking this against 06-22's yfinance-derived revenue found yfinance's own `Total Revenue` field matches this SEC tag exactly for FY2023 ($196,913M) but matches a *different* SEC tag (`Revenues`, i.e. total revenue including other income) for FY2024 ($202,793M ≈ $202,792M) — i.e. yfinance appears to have picked up different revenue-line concepts across filing years for this ticker. The narrower, consistently-defined "sales and other operating revenues" tag is used throughout as the more defensible basis.
3. **Gross margin: three disagreeing sources.** 06-22's reconstructed "Cost of Revenue" basis: 30.23% (TTM). yfinance's separate `info['grossMargins']` summary field: 42.42% (flagged as conflicting at 06-22, not used). This session's SEC EDGAR `CostOfGoodsAndServicesSold` tag: **41.97%** TTM — much closer to yfinance's summary field than to 06-22's own reconstruction. Chevron's GAAP income statement has no single native "Cost of Revenue"/"Gross Profit" line, so this is inherently a reconstruction regardless of source. The EDGAR-tag basis is used as primary (single, government-filed, company-tagged line); the discrepancy is flagged as an open item for the next full Phase 01 re-run, not resolved here (no Rule 9 trigger fired to warrant redoing Phase 01).
4. **Invested Capital now follows the current `framework/glossary.md` convention** (net of cash: Debt + Equity − Cash), added after 06-22. Recomputing with this convention: Invested Capital = $39,600M + $183,715M − $5,300M = $218,015M. Also noted for the record: 06-22's own stated ROIC (5.28%) does not arithmetically follow from its own stated NOPAT ($8,503M) ÷ Invested Capital ($178,664M), which computes to 4.76% — flagged as a data-quality note on the prior session, not corrected retroactively (predates the Quality Score engine; doesn't change 06-22's Phase 01 verdict).

### 3.2 TTM figures (Q2 FY2025 + Q3 FY2025 + Q4 FY2025 + Q1 FY2026 — the freshest window available; Q2 FY2026 not yet filed)

| Metric | $M |
|---|---|
| Revenue | 185,887 |
| Net Income | 11,009 |
| Cost of Goods & Services Sold | 107,869 |
| Pretax income | 18,106 |
| Tax | 6,840 |
| Interest expense | 1,350 |
| D&A | 21,817 |
| OCF | 31,264 |
| CapEx | 17,483 |

Balance sheet as of 2026-03-31 (most recent filed, same reference date as 06-22): Total debt (incl. leases) $39,600M; Cash $5,300M; Stockholders' equity $183,715M.

### 3.3 Sub-scores

| Sub-score (weight) | Value |
|---|---|
| Profitability (25%) | 19.13 (NetMargin_Component 19.74 from 5.92% net margin; ROIC_Component 18.51 from 5.55% ROIC = NOPAT $12,106M ÷ IC $218,015M) |
| Margins (15%) | 52.46 (Gross Margin 41.97%; no structural-trend bonus — 3yr trend non-monotonic: 39.47% → 38.37% → 41.33% → 41.97%, more consistent with oil-price cyclicality than documented structural expansion) |
| Growth (20%) | 0.0 (floored; Revenue 3yr CAGR -1.90%; no TAM modifier — Microsoft deal pre-FID, no current revenue impact) |
| Balance Sheet (15%) | 79.22 (Net Debt/EBITDA 0.83×) |
| Moat (15%) | 40.0 (2 of 5 signals true: switching costs [20yr Microsoft PPA, narrow/single-project]; scale cost advantage [<$50 Brent capex+dividend breakeven per Nov 2025 Investor Day vs. ~$61-67/bbl industry Permian new-well breakevens]. False: market share [Exxon still produces more], brand premium, network effect) |
| FCF Quality (10%) | 100.0 (capped; TTM FCF/NI 125.18%; FY2024 85.18%, FY2025 134.91%, both pass >70%) |

```
Quality Score = 19.13×0.25 + 52.46×0.15 + 0.0×0.20 + 79.22×0.15 + 40.0×0.15 + 100.0×0.10
              = 4.78 + 7.87 + 0.00 + 11.88 + 6.00 + 10.00
              = 40.5
```

**Quality Score = 40.5 / 100.0 — fails the 80.0+ gate decisively.** No hard disqualifier independently fires (FCF/NI passes both trailing fiscal years; Net Debt/EBITDA well under 2.5×; FCF positive every year since at least FY2023) — a pure weighted-score failure driven by weak Profitability and a Growth_Score floored at 0.0.

**Sensitivity check:** even under maximally generous alternative assumptions for the more debatable sub-scores (GrossMargin_Score = 100.0, Growth_Score = 100.0 — both far more generous than the data supports), the Quality Score would only reach ~67.6, still well short of 80.0. The gate verdict is robust to every data-source/modifier judgment call made in this session. No Composite Score computed (requires clearing the gate first).

## 4. Outcome and files touched

- **Outcome:** Quality Score Engine addendum appended to the existing watchlist entry — no Rule 9 trigger fired, so no fuller Phase 01 re-check and no new dated watchlist file.
- **Files modified:**
  - `watchlist/not-in-portfolio/CVX/CVX-2026-06-22.md` — appended Rule 9 check results and the Quality Score Engine addendum; expanded its Glossary section.
  - `framework/glossary.md` — added 5 new terms used in this session: 10b5-1 Trading Plan, Brent (crude), FID (Final Investment Decision), Form 4, PPA (Power Purchase Agreement).
  - `sessions/2026-07-07-new-position-cvx.md` — this file.
- **Not touched:** `watchlist/STALE.md` (CVX was never listed there), no `git` commands run, no `decisions/` entry (no trade/action taken — CVX remains not held, Phase 01 FAIL stands).

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file — all terms used above (CAGR, EBIT/EBITDA, FCF/NI conversion ratio, Hard disqualifier, Invested Capital, Moat, NOPAT, Quality Score, ROIC, Rule 0, Rule 9, Turnaround Sub-Gate, TTM, XBRL, and this session's 5 additions: 10b5-1 Trading Plan, Brent, FID, Form 4, PPA) are defined there.

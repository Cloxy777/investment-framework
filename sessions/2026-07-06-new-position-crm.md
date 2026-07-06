# NEW POSITION (Quality Score Engine addendum) — CRM (Salesforce, Inc.) — 2026-07-06

**Task type:** NEW POSITION — Quality Score Engine addendum (lightweight, per the CCL/CIEN precedent), not a full re-evaluation
**Date:** 6 Jul 2026
**Ticker:** CRM (Salesforce, Inc., NYSE)
**Prior session:** [2026-06-12-new-position-crm.md](2026-06-12-new-position-crm.md) — Phase 01 FAIL (ROIC 6.29-7.31% vs >15%, Revenue CAGR 3yr 9.82% vs >10%), predates the 2026-06-29 Quality Score engine addition — CRM has never had a Quality Score computed until this session
**Current CRM portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session exists

CRM's 06-12 session failed Phase 01 (the binary quality screen that predates the 2026-06-29 Quality Score engine) and was never scored under the new 0-100.0 engine. Per this task's explicit scope, this session does two things only:

1. A Rule 9 check — confirm whether CRM has reported Q2 FY2027 earnings yet (flagged 06-12 as due ~August 2026), whether TTM Revenue CAGR or ROIC have moved, and whether any other Rule 9 trigger fired since 06-12.
2. Compute CRM's first-ever Quality Score under the current engine, with every sub-score shown.

Per the task's branching instruction, a fuller Phase 01 re-check (or a new dated watchlist file) is only warranted if a Rule 9 trigger flips the verdict on the two previously-failing criteria (ROIC, Revenue CAGR 3yr). As shown below, neither crossed its threshold (in fact no new quarter has even been reported), so this stays an addendum appended to the existing watchlist file, not a new one.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$165.79** | IBKR `get_price_snapshot`, contract_id 29624264 (NYSE), intraday snapshot, `ts` 1783321881 → 2026-07-06 07:11:21 UTC, `is_close: false` |
| Cross-check | $166.11 | Yahoo Finance `financialData.currentPrice` |
| 52-week range | $146.32 – $276.80 (Yahoo `summaryDetail`) / $147.60 – $275.17 (IBKR `misc_statistics`) | Both cited — minor source discrepancy, immaterial to this session |
| Analyst consensus PT | Mean $246.44, median $240.00 (53 analysts), "buy" | Yahoo `financialData` |
| Baseline (06-12) | $166.47 | Prior session |
| Change since 06-12 | **-0.41%** | Computed — nowhere near the >15% Rule 9 threshold |

**Data-sourcing note:** `yfinance`'s own HTTP client (`curl_cffi`) again failed the TLS handshake through this session's egress proxy (`curl: (35) Recv failure: Connection reset by peer`), the same documented issue as the 2026-07-06 CCL/CIEN sessions. Worked around it identically: called Yahoo's `quoteSummary` and `fundamentals-timeseries` endpoints directly via `requests` with a manually-fetched crumb/cookie. Cross-checked every material figure against CRM's own SEC filings (10-Q filed 2026-05-28 for the quarter ended 2026-04-30; 8-K EX-99.1 filed 2026-05-27 for the Q1 FY2027 earnings release; 10-K filed 2026-03-02 for FY2026 and business/competition disclosures).

**Tool-availability note:** `WebSearch` returned persistent `529 Overloaded` errors for the entire session (multiple retries across ~10 minutes) and could not be used. This meant no independent third-party market-share research (the kind cited in the CCL/CIEN precedents, e.g. Dell'Oro Group, hoperesearchgroup.com) could be pulled for the Moat signal. All qualitative evidence in this session is therefore SEC-filing-sourced only — flagged explicitly in §4 rather than silently upgraded to third-party-report quality.

---

## 2. Rule 9 checklist — all 6 categories explicitly checked

| Category | Result |
|---|---|
| Earnings | **NO new report since 06-12.** Q1 FY2027 (quarter ended 2026-04-30) was already reported 2026-05-27 — before, and already reflected in, the 06-12 session's TTM figures (TTM Revenue $42.829B and TTM Net Income $8.023B are byte-for-byte identical between the two sessions). Q2 FY2027 is confirmed (not an estimate) for **2026-09-02** per Yahoo's `calendarEvents.earnings.isEarningsDateEstimate: false`. |
| Guidance revision | None since 06-12. FY2027 full-year revenue guidance was raised to $45.9-46.2B (+11% YoY GAAP) in the 2026-05-27 8-K — already reflected pre-06-12. |
| Management change | None found. No 8-K reporting a CEO/CFO change since 06-12. Only routine Form 4s (option exercises + tax withholding for six senior officers, filed 2026-06-22/23) and one Form 3 (Guy Wanger, EVP & Chief Accounting Officer — controller-level, not C-suite). |
| M&A | None new. Informatica was already closed and contributing to revenue ($444M in Q1 FY2027) before 06-12. |
| Macro shift | None CRM-specific found since 06-12. |
| >15% unexplained price move | No (-0.41%). |

**Net effect: no Rule 9 trigger fired since 06-12.** Per this task's branching instruction, this confirms the addendum-only path — no fuller Phase 01 re-check or new dated file is warranted.

---

## 3. Refreshed TTM financials and the two previously-failing Phase 01 criteria

Source: SEC 10-Q (filed 2026-05-28, quarter ended 2026-04-30) and Yahoo `fundamentals-timeseries` (`annualTotalRevenue`, `quarterlyEBIT`, `quarterlyInvestedCapital`, `quarterlyTaxProvision`, `quarterlyPretaxIncome`, `quarterlyTotalDebt`, `quarterlyCashAndCashEquivalents`, etc.), cross-checked against the primary 10-Q/8-K wherever they could diverge.

### Revenue CAGR 3yr — unchanged

```
FY2023 Revenue $31.352B → FY2026 Revenue $41.525B (both unchanged from 06-12)
Revenue CAGR 3yr = (41.525/31.352)^(1/3) − 1 = 9.82%
```

FY2026 remains the latest complete fiscal year (FY2027 doesn't close until 2027-01-31) — this metric is mechanically unable to move again before the January 2027 annual refresh. **Still fails the >10% Phase 01 threshold**, by the same 0.18pp margin as 06-12.

### ROIC — a methodology flag, not a fundamental change

The 06-12 session cited ROIC "6.29% (current) / 7.31% (TTM)" from GuruFocus, with its exact Invested Capital methodology undisclosed. Recomputing directly from primary-sourced NOPAT and Invested Capital for the *same* TTM window (Q2 FY2026 through Q1 FY2027 — unchanged, since no new quarter has been reported since 06-12) gives a materially different figure:

```
TTM EBIT = $9,977M (Q2FY26 $2,336M + Q3FY26 $2,448M + Q4FY26 $2,155M + Q1FY27 $3,038M)
TTM Pretax Income = $10,267M; TTM Tax Provision = $2,244M → effective tax rate 21.86%
NOPAT = $9,977M × (1 − 21.86%) = $7,796M

ROIC (glossary-literal, cash-netted IC — primary):
  IC = Yahoo quarterlyInvestedCapital $73,515M − Cash & Equivalents $8,935M (both 2026-04-30) = $64,580M
  ROIC = $7,796M / $64,580M = 12.07%

ROIC (raw quarterlyInvestedCapital, CCL-precedent convention — cross-check):
  ROIC = $7,796M / $73,515M = 10.61%
```

Both readings (10.61-12.07%) are well above the 06-12 GuruFocus figure **on the identical TTM window** (TTM Revenue and Net Income are unchanged) — a methodology divergence between data sources, not a fundamental improvement in the underlying business. This is the same open framework-consistency question the 2026-07-06 CIEN session raised about glossary.md's Invested Capital convention vs. how it's actually applied — flagged here again rather than silently resolved. **Regardless of which reading is used, ROIC remains well short of the >15% Phase 01 threshold.**

### Net Debt/EBITDA — a data-staleness finding, not a Rule 9 event

06-12 cited "Debt/EBITDA (current) 1.31×" (gross, from GuruFocus). This session's primary-sourced 10-Q balance sheet shows Total Debt jumped from $14,439M (2026-01-31) to **$39,280M (2026-04-30)** — a ~$25B senior-notes issuance across many new tranches (March 2028 through March 2066 maturities, contractual rates 4.26%-6.70%, per the 10-Q's Note 8 "Debt" table) that closed within Q1 FY2027 to fund the $25B ASR the 06-12 session had flagged as "underway." **This had already happened by the 06-12 session date** — the 10-Q disclosing it was filed 2026-05-28, before 06-12 — it just wasn't reflected in the externally-aggregated GuruFocus figure that session cited.

```
Net Debt (cash-only, matches Yahoo's own NetDebt field exactly) = Debt $39,280M − Cash $8,935M = $30,345M
Net Debt (broader, netting cash + marketable securities) = Debt $39,280M − $11,837M = $27,443M
TTM EBITDA (sum of quarterlyNormalizedEBITDA) = $12,742M; Yahoo financialData.ebitda field = $12,895M (cross-check)

Net Debt/EBITDA: 2.13× (broad cash, EBITDA field) to 2.38× (cash-only, EBITDA sum)
```

Both readings sit under the Quality Score's 2.5× standard hard-disqualifier threshold, though above the original Phase 01 gate's <2× pass bar. This doesn't retroactively change the 06-12 verdict (which already failed independently on ROIC and Revenue CAGR), but it's a materially more leveraged balance sheet than the 1.31× headline figure suggested.

**Conclusion: neither previously-failing Phase 01 criterion (ROIC, Revenue CAGR 3yr) crossed its threshold, and no new Rule 9 event occurred. Per this task's explicit branching instruction, this confirms the addendum-only path.**

---

## 4. Quality Score Engine — CRM's first-ever computation

Per [framework/quality-scoring.md](../framework/quality-scoring.md) (methodology version 2026-06-29). Full detail and the worked formula are in the [watchlist addendum](../watchlist/not-in-portfolio/CRM/CRM-2026-06-12.md#quality-score-engine-addendum-2026-07-06--crms-first-ever-quality-score-computed-under-the-2026-06-29-engine); summarized here:

**Hard disqualifiers checked — none fire:** FCF positive 5 consecutive years (FY2023-FY2026 + TTM); FCF/NI conversion ≥193% every year (nowhere near the <70% threshold); Net Debt/EBITDA 2.13-2.38× (under the 2.5× standard threshold in every convention tested).

| Sub-score (weight) | Score |
|---|---|
| Profitability (25%) | 51.34 (primary) / 48.89 (cross-check) |
| Margins (15%) | 97.05 |
| Growth (20%) | 49.28 |
| Balance Sheet (15%) | 40.46 (primary) / 46.80 (cross-check) |
| Moat (15%) | 60.0 (sensitivity: 40.0 if the market-share signal is excluded — see caveat below) |
| FCF Quality (10%) | 100.0 (capped) |

```
Quality Score (primary) =
  51.34×0.25 + 97.05×0.15 + 49.28×0.20 + 40.46×0.15 + 60.0×0.15 + 100.0×0.10
  = 12.835 + 14.5575 + 9.856 + 6.069 + 9.00 + 10.00
  = 62.3

Cross-check (raw-IC ROIC + broader-cash Net Debt + 2/5 Moat) = 59.7
```

**Quality Score = 62.3 / 100.0 (primary) — fails the 80.0+ gate, and fails it under every methodology variant tested (59.7-62.3).** No hard disqualifier fires independently. CRM's strongest sub-scores are Gross Margin (97.05) and FCF Quality (100.0, capped) — genuinely excellent — but Profitability (48.9-51.3, capped by sub-15% ROIC) and Growth (49.28, still reflecting sub-10% revenue CAGR even after the TAM-expansion bonus) pull the weighted average well short of 80.0. This is a meaningfully higher score than the CCL and CIEN precedents (both 57.7), driven by CRM's much stronger margins and FCF conversion, but still not close to clearing the gate.

### Moat Signal detail (cited evidence required per signal)

| Signal | Result | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE (weak evidence — flagged)** | SEC 10-K (filed 2026-03-02), Item 1: "a global leader in customer relationship management (CRM) technology" — a company-filing self-description, an accepted evidence type per quality-scoring.md, but weaker than the CCL/CIEN precedent's independent third-party %-share citations. WebSearch was unavailable this session (persistent 529 errors), so no IDC/Gartner corroboration could be pulled. Flagged for a follow-up session. |
| Brand premium (pricing power) | **TRUE** | 2026-05-27 8-K: current RPO $33.6B up 14% YoY, outpacing total revenue growth of 11% (a forward pricing/demand signal); premium Agentforce One Edition/Agentforce for Apps SKUs; combined Agentforce+Data 360 ARR $3.4B up >200% YoY |
| Network effect | **TRUE** | SEC 10-K, Item 1: AppExchange described as an "enterprise cloud marketplace" enabling ISVs and third-party developers to build and sell apps, with an explicit "leverage our partner ecosystem" growth strategy — a documented two-sided marketplace mechanism |
| Switching costs | **FALSE** | SEC 10-K's own Competition section states the market is "highly competitive, rapidly evolving and fragmented... with low barriers to entry" — working against, not for, a lock-in-based moat claim; no specific migration-cost or contractual lock-in data found |
| Scale cost advantage | **FALSE** | No cost-per-unit data vs. smaller competitors found (WebSearch unavailable to search for this) |

Moat_Score = (3/5) × 100 = **60.0** (sensitivity case: (2/5) × 100 = 40.0 if the market-share signal is excluded for its weaker evidentiary basis — used in the cross-check total above)

---

## 5. Recommendation

# **PASS — Quality Score 62.3/100.0 (59.7-62.3 across methodology cross-checks), fails the 80.0+ gate. Do not enter. Watchlist addendum appended, no new file created.**

No Rule 9 trigger fired since 06-12 — CRM has not reported a new quarter (next due 2026-09-02), issued new guidance, changed management, done new M&A, or moved >15% in price. Both previously-failing Phase 01 criteria (ROIC, Revenue CAGR 3yr) remain on the failing side of their thresholds on the identical TTM window used at 06-12, so the Phase 01 verdict stands unchanged. CRM's first Quality Score computation (62.3) is well below the 80.0 gate but notably higher than the CCL and CIEN precedents (57.7 each), reflecting genuinely excellent gross margins and FCF conversion — the binding constraints are still profitability (sub-15% ROIC under every tested convention) and growth (sub-10% revenue CAGR).

Two findings are worth carrying forward independent of the gate result: (1) a real, cross-cutting ROIC methodology gap between this framework's primary-sourced NOPAT/Invested-Capital calculation and externally-aggregated figures like GuruFocus's, flagged identically in the CIEN session and still unresolved in glossary.md; and (2) CRM's balance sheet is now meaningfully more leveraged (2.1-2.4× net debt/EBITDA) than the 1.31× headline figure the 06-12 session relied on, following the debt-funded $25B ASR — already true as of 06-12, just not reflected in that session's sourcing.

**No position opened — nothing to log in `decisions/`.**

---

## 6. Files touched this session

- `watchlist/not-in-portfolio/CRM/CRM-2026-06-12.md` — appended the Rule 9 check + Quality Score addendum as a dated note and table row, plus a closing Glossary section (the original file had none); no new file created, per the task's branching instruction — no Phase 01 verdict change
- `sessions/2026-07-06-new-position-crm.md` — this file

`watchlist/STALE.md` was not touched (CRM was not listed there — it predates the Quality Score engine but was never a "stale re-score" case, it was a Phase 01 FAIL that had never been scored at all). No `git` commands were run. No files outside the watchlist/sessions directories were modified.

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session (mirrors the addendum's glossary — see the [watchlist entry](../watchlist/not-in-portfolio/CRM/CRM-2026-06-12.md#glossary) for the full list): 8-K, 10-K/10-Q, Agentforce, ARR, ASR, BalanceSheet_Score, CAGR, cRPO, EBIT/EBITDA, Effective tax rate, FCF/NI conversion ratio, GAAP, Gross Margin, Hard disqualifier, Invested Capital, Moat, NOPAT, Net Debt/EBITDA, Quality Score, ROIC, RPO, Rule 0, Rule 9, Senior Notes, TAM, Turnaround Sub-Gate, TTM, WACC.

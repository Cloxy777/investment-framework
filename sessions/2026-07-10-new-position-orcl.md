# NEW POSITION (Quality Score Engine addendum) — ORCL (Oracle Corporation) — 2026-07-10

**Task type:** NEW POSITION — Quality Score Engine addendum (per the CCL/MU precedent), not a full re-evaluation
**Date:** 10 Jul 2026
**Ticker:** ORCL (Oracle Corporation, NYSE)
**Prior session:** [2026-06-12-new-position-orcl.md](2026-06-12-new-position-orcl.md) — Phase 01 FAIL on 4 independent criteria (ROIC 9.05%, FCF-positive-3yrs, Net Debt/EBITDA 2.93x, dilutive share issuance), predating the 2026-06-29 Quality Score engine — ORCL has never had a Quality Score computed until this session.
**Current ORCL portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session exists

Two things, per explicit task scope:
1. Check for any Rule 9 trigger since 06-12 (earnings, guidance revision, management change, M&A/capital-plan revision, macro shift, >15% unexplained price move) and whether the FY2026 10-K has now been filed.
2. Compute ORCL's first-ever Quality Score under the current (2026-06-29) engine, with every sub-score shown, using the freshest TTM data available.

Per the task's branching instruction, a fuller Phase 01 re-check (new dated watchlist file) is only warranted if a Rule 9 trigger flips the Phase 01 gate's verdict. As shown below, several events fired, but none flip the verdict — all four previously-failing criteria remain failing, two of them (FCF-positive-3yrs, Net Debt/EBITDA) now confirmed *worse* than the 06-12 read. This stays an addendum appended to the existing watchlist file.

## 1. Live price (Rule 0)

- **IBKR `get_price_snapshot`**, contract_id 272800 (confirmed via `search_contracts("ORCL")`, NYSE primary listing): **$141.15**, last trade ts 2026-07-10 15:30:05 UTC, `is_close: false` (live, regular session). Bid $141.13 / Ask $141.18.
- Cross-check — Yahoo `regularMarketPrice`: $141.07, ts 15:30:13 UTC (`marketState: REGULAR`) — 0.06% apart, ~8 seconds apart, both genuine live quotes.
- 52-week range (IBKR `misc_statistics`): unchanged at low $134.57 / high $345.72 — no new high or low set since 06-12.
- Baseline (06-12 reference): $182.77. Change to today: **-22.77%** — fires the >15% Rule 9 threshold, explained below (not "unexplained").

## 2. Data-source note

`yfinance`'s `curl_cffi`-based HTTP session hit the same persistent TLS connection-reset issue documented in this framework's 2026-07-10 MU session (not a rate limit — plain `requests` calls to the same Yahoo hosts succeeded immediately). Worked around identically: queried the underlying Yahoo Finance `quoteSummary` and `ws/fundamentals-timeseries` APIs directly via `requests` with a browser User-Agent and a freshly-fetched crumb — the same data source `yfinance` wraps. All annual/TTM financial figures were additionally cross-checked directly against Oracle's own SEC XBRL `companyconcept` API (CIK 0001341439) — the primary-source basis used wherever the two diverged (see §4).

## 3. Rule 9 check — all 6 categories, since 2026-06-12

| Category | Result |
|---|---|
| Earnings | No new earnings event since 06-12 (Q4/FY2026 was reported 2026-06-10, two days *before* the 06-12 session and already its data basis). Next: Q1 FY2027, expected ~mid-September 2026. |
| **10-K status** | **FILED 2026-06-22** — sooner than the 06-12 session's "~Aug-Sept 2026" estimate. [SEC EDGAR, accession 0001193125-26-277521](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm). Resolves the 06-12 session's Gap #1 (year-end balance sheet) and Gap #2 (full FCF detail). |
| Guidance revision | FY2027 capex guided to ~$70B (up from FY2026's actual $55.663B) — an escalation of the same already-known capex super-cycle, not a new direction. [Bloomberg, 2026-07-01](https://www.bloomberg.com/news/newsletters/2026-07-01/oracle-warns-ai-data-center-splurge-may-not-pay-off). |
| Management change | None material — co-CEOs Clay Magouyrk/Mike Sicilia (Sept 2025) and CFO Hilary Maxson (effective 2026-04-06) both predate 06-12. |
| M&A / capital-plan revision | 424B5 filed 2026-06-23 expanded the sales-agent syndicate for the same pre-existing $20B ATM common-stock program — administrative continuation, not a new/larger raise. [SEC EDGAR, accession 0001193125-26-278585](https://www.sec.gov/Archives/edgar/data/1341439/000119312526278585/d120346d424b5.htm). |
| Macro shift / credit event | **S&P Global Ratings downgraded Oracle from BBB to BBB- on 2026-07-09**, projecting FY2027 FCF deficit widening to ~-$42B (from ~-$24B) and adjusted debt/EBITDA reaching the mid-4x range in FY2027; all three major agencies now rate Oracle at the low end of investment grade. [Yahoo Finance/Investing.com](https://finance.yahoo.com/markets/stocks/articles/oracle-stock-shrugs-off-p-185346661.html); [HNGN](https://www.hngn.com/articles/271995/20260709/sp-downgrades-oracle-credit-rating-ai-buildout-deepens-42-billion-cash-deficit.htm). 10Y Treasury 4.56% (FRED, 07-08) vs. 4.46% on 06-12 — same rate bracket, no Rate Regime change (moot; gate fails before Rate Gate is reached). |
| >15% unexplained price move | Fired (-22.77%), but explained — press attributes it to the S&P downgrade, widening FCF-deficit projections, continued dilutive-issuance execution, and OpenAI customer-concentration concerns (~47% of RPO), not a single new discrete catalyst. |

**Net effect: Rule 9 fired (10-K filing + credit downgrade + the large-but-explained price move), refining several previously-failing criteria with audited full-year data — but the Phase 01 gate's verdict does not flip.** Per the task's branching instruction, this stays an addendum, not a full re-evaluation.

## 4. Data correction: FY2024/FY2025 FCF

The 06-12 session's FY2024 (≈+$43.6B) and FY2025 (≈+$26.2B) full-year FCF figures were **erroneous** — they were built by summing four separately-labeled "quarterly" OCF-minus-CapEx figures per fiscal year, but those figures were year-to-date cumulative disclosures, not discrete quarters, so the sums quadruple/triple-counted overlapping periods. Verified directly against SEC XBRL primary data (`NetCashProvidedByUsedInOperatingActivities`, `PaymentsToAcquirePropertyPlantAndEquipment`):

| FY | OCF | CapEx | FCF (corrected) | 06-12 session's figure |
|---|---|---|---|---|
| FY2023 | $17.165B | -$8.695B | **+$8.470B** | not stated |
| FY2024 | $18.673B | -$6.866B | **+$11.807B** | ≈+$43.6B (error) |
| FY2025 | $20.821B | -$21.215B | **-$0.394B** | ≈+$26.2B (error — was already negative) |
| FY2026 | $31.977B | -$55.663B | **-$23.686B** | -$23.7B (correct) |

Net effect: ORCL's FCF has been negative for **two consecutive fiscal years (FY2025, FY2026)**, not one as previously reported — the "FCF positive 3 consecutive years" Phase 01 criterion fails more decisively than 06-12 stated. Corrected transparently per the framework's "never invent or estimate financial data" discipline, which extends to fixing a prior session's arithmetic once primary-source data resolves it.

## 5. Quality Score computation

Full sub-score table, formula, and sourcing are in the addendum appended to [watchlist/not-in-portfolio/ORCL/ORCL-2026-06-12.md](../watchlist/not-in-portfolio/ORCL/ORCL-2026-06-12.md). Summary:

| Sub-score (weight) | Value |
|---|---|
| Profitability (25%) | 40.0 (capped — not FCF-positive 3 consecutive years; would be 60.3 uncapped) |
| Margins (15%) | 82.3 (Gross Margin 65.82%, no trend bonus — margin is contracting, not expanding) |
| Growth (20%) | 51.9 (Revenue 3yr CAGR 10.48% + 10 TAM-expansion modifier, cited RPO $638B/OCI +93% YoY) |
| Balance Sheet (15%) | 0.0 (Net Debt/EBITDA 4.18x primary / 3.73x cross-check — both exceed 2.5x; also independently fires the hard disqualifier) |
| Moat (15%) | 40.0 (2 of 5 signals: Brand premium/pricing power, Switching costs — both cited to Oracle's 8% automatic support-fee escalation and the 2026 Java SE relicensing episode) |
| FCF Quality (10%) | 0.0 (FY2026 FCF/NI = -138.6%) |

```
Quality Score = 40.0×0.25 + 82.3×0.15 + 51.9×0.20 + 0.0×0.15 + 40.0×0.15 + 0.0×0.10 = 38.7
```

**Quality Score = 38.7 / 100.0 — fails the 80.0+ gate**, and independently fires the "not FCF-positive for 3+ consecutive years" hard disqualifier (no carve-out exists for this one) as well as the Net Debt/EBITDA hard disqualifier. Same dual-failure pattern as this framework's CCL and MU Quality Score addenda. No Composite Score computed (requires clearing the gate first).

## 6. Outcome and files touched

- **Outcome:** Quality Score Engine addendum appended to the existing watchlist entry, plus the full Rule 9 check and a correction to a prior-session FCF data error. The Phase 01 gate's overall verdict did not flip (still FAIL on all 4 originally-failing criteria) — so no fuller Phase 01 re-check and no new dated watchlist file, per the task's branching instruction.
- **Files modified:**
  - `watchlist/not-in-portfolio/ORCL/ORCL-2026-06-12.md` — appended the Rule 9 check, the FCF data correction, and the Quality Score Engine addendum; added a Glossary section.
  - `framework/glossary.md` — added 1 new term: DB-Engines ranking.
  - `sessions/2026-07-10-new-position-orcl.md` — this file.
- **Not touched:** `watchlist/STALE.md` (ORCL was never listed there), no `git` commands run, no `decisions/` entry (no trade/action taken — ORCL remains not held, Phase 01 FAIL stands).

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file — all terms used above (10-K, CAGR, EBIT/EBITDA, Effective tax rate, FCF/NI conversion ratio, GAAP, Hard disqualifier, Invested Capital, Investment grade, Moat, NOPAT, Net Debt/EBITDA, Quality Score, ROIC, RPO, Rule 0, Rule 9, TTM, XBRL, and this session's 1 addition: DB-Engines ranking) are defined there.

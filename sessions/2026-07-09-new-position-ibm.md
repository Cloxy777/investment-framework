# NEW POSITION (Quality Score Engine addendum) — IBM (International Business Machines Corporation) — 2026-07-09

**Task type:** NEW POSITION — Quality Score Engine addendum (lightweight, per the CCL precedent), not a full re-evaluation
**Date:** 9 Jul 2026
**Ticker:** IBM (International Business Machines Corp., NYSE)
**Prior session:** [2026-06-25-new-position-ibm.md](2026-06-25-new-position-ibm.md) — Phase 01 FAIL (4 of 8 criteria: ROIC, revenue growth, Net Debt/EBITDA, dilutive share-issuance pattern), predates the 2026-06-29 Quality Score engine addition — IBM has never had a Quality Score computed until this session
**Current IBM portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session exists

IBM's 06-25 session failed Phase 01 (the binary quality screen that predates the 2026-06-29 Quality Score engine) and was never scored under the new 0–100.0 engine. Per this task's explicit scope, this session does two things only:

1. A Rule 9 check — including a specific check on whether IBM's "nanostack" sub-1nm chip commercialization timeline (flagged in the 06-25 session as one thing that would qualify) had materially accelerated — plus the standard 6-category Rule 9 sweep (earnings, guidance, management, M&A, macro, >15% unexplained price move).
2. Compute IBM's first-ever Quality Score under the current engine, with every sub-score shown.

Per the task's branching instruction, a fuller Phase 01 re-check (or a new dated watchlist file) is only warranted if a Rule 9 trigger fired that changes the Phase 01 verdict. As shown below, **no Rule 9 trigger fired at all** — IBM's Q2 FY2026 earnings are not due until 22 July 2026, and the nanostack timeline is explicitly confirmed unchanged (still ~5 years out, no commercialization plan disclosed). This stays an addendum appended to the existing watchlist file, not a new one.

---

## 1. Live Price (Rule 0) and Rule 9 Trigger Check

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$294.55** | IBKR `get_price_snapshot`, contract_id 8314, ts 1783621640 → 2026-07-09 18:27:20 UTC, `is_close: false`, bid/ask $294.45/$294.68 |
| 52-week range | $212.35 – $332.41 (unchanged from 06-25) | IBKR `misc_statistics` |
| Dividend yield | 2.23% (was 2.56% on 06-25) | IBKR snapshot |
| Baseline (06-25) | $270.93 | Prior session |
| Change since 06-25 | **+8.72%** | Computed |

**Rule 9 checklist (all 6 categories explicitly checked, plus the nanostack-specific check called out in this task):**

| Category | Result |
|---|---|
| Earnings | **NO** — Q2 FY2026 results scheduled for 22 July 2026 (confirmed via [IBM Newsroom, 2026-07-08](https://newsroom.ibm.com/2026-07-08-IBM-to-Announce-Second-Quarter-2026-Financial-Results)); not yet reported. |
| Guidance revision | None since 06-25. |
| Management change | None — Krishna (CEO)/Kavanaugh (CFO) unchanged; Laguarta's board election (1 Mar 2026) predates 06-25. |
| M&A | None new — the $11B Confluent acquisition (announced Dec 2025, completed 17 Mar 2026) predates 06-25 and is already embedded in the financials pulled below. |
| Macro shift | None identified specific to IBM since 06-25. |
| Nanostack chip commercialization timeline | **Not materially accelerated.** IBM Research Director Jay Gambetta confirmed the company is not yet disclosing commercialization plans; near-term focus remains 2nm nanosheet scaling; ~5-year (~2031) production estimate unchanged. Sources: [TechWireAsia](https://techwireasia.com/2026/06/ibm-sub-1-nm-chip-technology-nanostack/), [The Register](https://www.theregister.com/systems/2026/06/25/ibm-stacks-up-a-sub-nanometer-chip-future/). |
| >15% unexplained price move | No (+8.72%, and explained by routine, already-identified news — BofA PT raise, z17/LinuxONE 5 launch, a quantum-computing collaboration announcement — regardless). |

**Net effect: no Rule 9 trigger fired.** This confirms the addendum-only path.

---

## 2. Refreshed TTM financials (through Q1 FY2026, quarter ended 2026-03-31)

**Data-sourcing note:** `yfinance` (with `YF_DISABLE_CURL_CFFI=1` / `CURL_CA_BUNDLE=/root/.ccr/ca-bundle.crt`, per 06-25 precedent) supplied quarterly financials through 2026-03-31. TTM = Q2 FY2025 + Q3 FY2025 + Q4 FY2025 + Q1 FY2026.

| Quarter end | Revenue | Gross Profit | EBIT | EBITDA | Net Income | Tax Provision | Pretax Income |
|---|---|---|---|---|---|---|---|
| 2025-03-31 | $14.541B | $8.031B | $1.613B | $2.790B | $1.055B | $0.103B | $1.158B |
| 2025-06-30 | $16.977B | $9.977B | $3.107B | $4.372B | $2.194B | $0.404B | $2.597B |
| 2025-09-30 | $16.331B | $9.360B | $2.922B | $4.205B | $1.744B | $0.686B | $2.430B |
| 2025-12-31 | $19.687B | $11.928B | $4.621B | $5.917B | $5.600B | **−$1.435B** | $4.143B |
| 2026-03-31 | $15.917B | $8.950B | $1.860B | $3.134B | $1.216B | $0.172B | $1.387B |

**TTM (Q2'25–Q1'26):** Revenue $68.912B, Gross Profit $40.215B, EBIT $12.510B, EBITDA $17.628B, Net Income $10.754B, Tax Provision **−$0.173B**, Pretax Income $10.557B → **effective tax rate −1.64%**.

**Flagged anomaly:** the Q4 FY2025 −$1.435B tax provision (a tax *benefit*) is what pulls the TTM rate negative. Per IBM's own FY2025 10-K, this reflects the "resolution of certain tax audit matters" — the same mechanism as [glossary.md](../framework/glossary.md)'s "Uncertain tax position release" entry. This is not a one-quarter fluke: IBM's *annual* effective tax rate was also negative in FY2025 (−2.34%) and FY2022 (−54.15%), near-zero in FY2024 (−3.76%) — a recurring, multi-year IBM characteristic (not invented or estimated). Since NOPAT = EBIT × (1 − tax rate), a negative rate pushes NOPAT ($12.715B) **above** EBIT ($12.510B), inflating ROIC and the Profitability sub-score versus what a more typical historical IBM rate (e.g. FY2023's 13.53%) would produce — flagged prominently in the watchlist addendum since it means the resulting Quality Score is, if anything, mildly generous to IBM.

**Cash flow (TTM):** OCF $13.992B, CapEx −$1.734B, FCF (OCF−CapEx, reconciling to yfinance's own quarterly FCF statement rows) $12.258B. Two flagged, unreconciled cross-check discrepancies (neither changes any conclusion): `yfinance`'s aggregate `info.ebitda` field reads $16.611B (vs. $17.628B used here) and `info.freeCashflow` reads $13.081B (vs. $12.258B used here) — the quarterly-statement-row sums are used as primary throughout, consistent with citing structured statement fields over black-box aggregates.

**Balance sheet (2026-03-31):** Total Debt $69.802B (up from $64.607B at FY2025-end — the increase is consistent with financing the Confluent acquisition, which closed 17 Mar 2026), Cash $10.819B, Net Debt (company-debt-only basis, excl. capital leases, matching yfinance's own `Net Debt` field) **$55.542B**, Invested Capital (latest-quarter) $99.335B, Invested Capital (FY2025-annual, cross-check basis) $93.908B.

```
Net Debt/EBITDA = $55.542B / $17.628B = 3.15x   (cross-check using info.ebitda $16.611B: 3.34x — same conclusion)
Interest coverage = EBIT $12.510B / TTM Interest Expense $1.953B = 6.41x   (06-25: 6.34x, essentially unchanged)
```

Still far above the 2.5x standard Net Debt/EBITDA threshold, and interest coverage remains far below the >15x the Upgrade-5 asset-light override would require — IBM does not qualify for that override (unchanged conclusion from 06-25).

---

## 3. Quality Score Engine — IBM's first-ever computation

Per [framework/quality-scoring.md](../framework/quality-scoring.md) (methodology version 2026-06-29). Full detail and the worked formula are in the [watchlist addendum](../watchlist/not-in-portfolio/IBM/IBM-2026-06-25.md); summarized here:

| Sub-score (weight) | Score |
|---|---|
| Profitability (25%) | 47.34 |
| Margins (15%) | 72.95 |
| Growth (20%) | 24.88 |
| Balance Sheet (15%) | 21.23 |
| Moat (15%) | 60.0 |
| FCF Quality (10%) | 100.0 |

```
Quality Score = 47.34×0.25 + 72.95×0.15 + 24.88×0.20 + 21.23×0.15 + 60.0×0.15 + 100.0×0.10
              = 11.835 + 10.9425 + 4.976 + 3.1845 + 9.0 + 10.0
              = 49.94 ≈ 49.9
```

**Quality Score = 49.9 / 100.0 — fails the 80.0+ gate.** IBM fails two independent ways at once, mirroring the CCL precedent:
1. **The weighted score itself** (49.9 < 80.0) — driven mainly by a still-modest Profitability score (47.34, even after the negative-tax-rate NOPAT inflation described above), a Growth score capped low by the persistent 3.72% revenue 3yr CAGR even after the +10 TAM/pricing-power modifier, and a weak Balance Sheet score (21.23) reflecting the leverage the 06-25 Phase 01 FAIL already flagged.
2. **A hard disqualifier**, independent of the weighted score: Net Debt/EBITDA (3.15–3.34x) sits above the 2.5x standard threshold. Per quality-scoring.md, this "fails regardless of weighted score."

**Cross-check using the FY2025-annual Invested Capital basis** ($93.908B instead of the latest-quarter $99.335B) gives ROIC 13.54%, Profitability_Score 48.58, and a Quality Score of **50.2** — same conclusion either way.

The FCF-positivity and FCF/NI-conversion hard disqualifiers do **not** fire (FCF positive every year FY2022–FY2025 and TTM; FCF/NI conversion 108–516% across all shown years, comfortably above 70%).

**No Composite Score computed** (requires clearing the 80.0+ gate first). **No Phase 02 valuation work performed** (out of scope for this addendum, and moot given the gate result).

### Moat Signal detail (cited evidence required per signal)

| Signal | Result | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | IBM holds >90% of the global mainframe market; Z Systems specifically ~63% of mainframe installations and growing — IBM Z revenue +51% YoY in Q1 FY2026 entering the z17 cycle (Enlyft, Mordor Intelligence market-share research, via WebSearch) |
| Brand premium (pricing power) | **TRUE** | Confirmed 2026 list-price increases: 6% across Distributed SW/SaaS and zMLC/zOTC S&S effective on renewals on/after 1 Jul 2026, FlashSystem hardware +15%, cumulative z16 MIPS pricing +15–20% since 2022 (IT Jungle) — without an offsetting revenue decline (Software revenue +11.3% YoY same period) |
| Network effect | FALSE | No documented two-sided-marketplace mechanism found |
| Switching costs | **TRUE** | Independent analysis of verified mainframe-to-cloud migrations: real costs $2M–$15M+, 2–5yr timelines, 45% failure rate; Gartner forecasts 75% of mainframe-migration service providers will pivot away or disappear by 2030 |
| Scale cost advantage | FALSE | No citable cost-per-unit data vs. smaller competitors found (searched; not located in the time available for this lightweight addendum) |

Moat_Score = (3/5) × 100 = **60.0**

---

## 4. Recommendation

# **PASS — Quality Score 49.9/100.0 (49.9–50.2 across cross-checks), fails the 80.0+ gate (also independently failed by the Net Debt/EBITDA hard disqualifier). Do not enter. Watchlist addendum appended, no new file created, 06-25 Phase 01 FAIL verdict stands unchanged.**

No Rule 9 trigger fired since 06-25 — Q2 FY2026 earnings aren't due until 22 July 2026, and the nanostack chip program (this task's specific flag) is explicitly confirmed *not* to have accelerated. IBM's first Quality Score computation, run independently of the 06-25 Phase 01 criteria, arrives at the same conclusion from a different angle: 49.9 is well short of 80.0, and the balance-sheet leverage — worse than at 06-25 because of debt taken on to fund the March-2026 Confluent acquisition — is a hard disqualifier on its own. A genuinely interesting earnings-quality wrinkle (a negative TTM effective tax rate from a tax-audit resolution) works in IBM's favor in this computation and still isn't enough to clear the gate.

**No position opened — nothing to log in `decisions/`.**

---

## 5. Files touched this session

- `watchlist/not-in-portfolio/IBM/IBM-2026-06-25.md` — appended the Rule 9 check + Quality Score addendum as a dated note (no new file, per the task's branching instruction — no Phase 01 verdict change), plus a small glossary-term addition local to that file (all terms used already exist in the central glossary)
- `sessions/2026-07-09-new-position-ibm.md` — this file

`watchlist/STALE.md` was not touched (IBM was not listed there — it predates the Quality Score engine but was never a "stale re-score" case, it was a Phase 01 FAIL that had never been scored at all).

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **CAGR** — Compound Annual Growth Rate.
- **CapEx** — Capital Expenditure.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization.
- **Effective tax rate** — the actual share of pretax income paid as tax; IBM's TTM figure is unusually negative (−1.64%), driven by a Q4 FY2025 tax-audit-resolution benefit.
- **FCF** — Free Cash Flow.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income, an earnings-quality check.
- **GAAP** — Generally Accepted Accounting Principles.
- **Gross Margin** — Gross Profit ÷ Revenue.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted score; IBM's Net Debt/EBITDA fires this one independently of the 49.9 weighted score.
- **Interest coverage (ratio)** — EBIT ÷ interest expense.
- **Invested Capital** — the total capital (debt + equity, netted for cash) put to work in a business — the denominator in ROIC.
- **Moat** — a durable competitive advantage.
- **NOPAT** — Net Operating Profit After Tax, the numerator of ROIC.
- **Net Debt/EBITDA** — a leverage ratio; this framework's primary balance-sheet-risk gate.
- **Quality Score** — this framework's 0–100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02. IBM scores 49.9 on its first-ever computation.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 9** — this framework's list of events that force an immediate re-valuation: earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results.
- **Uncertain tax position release** — a one-off GAAP event where a company reverses a previously-reserved tax liability after a tax authority resolves the matter in its favor, producing an artificially low or negative effective tax rate — the mechanism behind IBM's FY2025 tax benefit.

# NEW POSITION (Re-trigger) — IBM (International Business Machines Corporation) — 2026-07-17

**Task type:** NEW POSITION (re-opened — Telegram-scan trigger, Routine 6, automated/unattended run)
**Date:** 17 Jul 2026
**10Y US Treasury Yield:** 4.55% (FRED `DGS10`, most recent posted row, 2026-07-15 — 07-16/07-17 not yet posted, normal FRED reporting lag)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket) — **for the record only, not applied — Quality Gate fails first, see §3**
**Current IBM portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)
**Prior coverage:** [2026-06-25-new-position-ibm.md](2026-06-25-new-position-ibm.md) (Phase 01 FAIL, not scored), [2026-07-09-new-position-ibm.md](2026-07-09-new-position-ibm.md) (first Quality Score computation, 49.9/100.0, addendum — no Rule 9 trigger at that time); watchlist [IBM-2026-06-25.md](../watchlist/not-in-portfolio/IBM/IBM-2026-06-25.md) — most recently reconfirmed at live price $294.55 (2026-07-09).
**Sector:** Technology — Information Technology Services (enterprise hardware, software, consulting)

---

## 0. Why this session exists — re-trigger source

Telegram channel `https://t.me/myroslavkorol`, post `myroslavkorol/2580` (~06:40 UTC, 2026-07-17): a repost embedding a YouTube video titled *"№411: Падіння IBM на 25%. Ризики по виробникам чіпів пам'яті: Micron, Sandisk, SK hynix"* ("#411: IBM's 25% Fall. Risks for Memory Chip Manufacturers: Micron, SanDisk, SK hynix"), captioned "Якраз актуальний відос опублікував)" ("Just published a relevant video"). Per the operating brief, **Telegram post/video-title text is never used as financial data** — it is a trigger only, and the claimed "25% fall" must be independently verified, never taken at face value. IBM's existing watchlist file's own standing "Next review trigger" explicitly lists ">15% unexplained price move from $294.55" and "Q2 FY2026 earnings, scheduled 22 July 2026 (not yet due)" as the two things that would fire a fresh Rule 9 check — a claimed 25% fall, if real, is materially new information not yet reflected in that file.

---

## 1. Live Price (Rule 0) and contract reconfirmation

| Field | Value | Source |
|---|---|---|
| Contract reconfirmation | contract_id **8314**, NYSE, symbol IBM, "INTL BUSINESS MACHINES CORP" — unchanged from prior sessions | IBKR `search_contracts` query "IBM" |
| **Live price used** | **$213.25** (last trade) | IBKR `get_price_snapshot`, contract_id 8314, ts 1784275592 → **2026-07-17 08:06:32 UTC**, `is_close: false`, `halted: false`, bid/ask $212.80/$213.16 |
| Today's intraday change | −$5.80 / −2.65% vs. yesterday's close | IBKR `change` field |
| 52-week range | **$204.50 (low) – $332.41 (high)** — low fell from $212.35 (06-25/07-09) to $204.50, consistent with a new 52-week-low print during the 14 Jul crash | IBKR `misc_statistics` |
| Price 52 weeks ago (`open_52w`) | $276.52 | IBKR `misc_statistics` |
| Dividend yield | 3.07% (was 2.23% on 07-09, 2.56% on 06-25 — mechanically higher purely from the lower price, not a dividend increase) | IBKR snapshot |
| Baseline (2026-07-09) | $294.55 | Prior session |
| **Change vs. 07-09 reference** | **(213.25 − 294.55) / 294.55 = −27.60%** | Computed |

**This clears the >15% Rule 9 threshold by a wide margin — nearly double it — and is, unusually, at least as large as the Telegram video's claimed "25% fall."** Independent web verification below confirms this is a real, primary-sourced, well-explained move — not a stale/halted quote, not a data error (bid/ask $212.80/$213.16 bracket the last trade tightly, `halted: false`), and not the clickbait exaggeration this framework has repeatedly found in past Telegram-triggered re-checks (see the 2026-07-08 MU session, where a claimed price was found to be inaccurate even though the magnitude claim was directionally real).

---

## 2. Independent verification — what actually happened

### 2.1 Primary source: IBM's own Form 8-K, filed 14 July 2026

IBM filed a Form 8-K on **14 July 2026** (SEC accession 0000051143-26-000070, Exhibit 99.1, "Arvind Krishna's Letter to IBM Investors") **preannouncing selected preliminary Q2 2026 results** ahead of its regularly scheduled 22 July 2026 full earnings report. CEO Krishna's own words: *"This morning we are releasing selected preliminary second-quarter 2026 financial results. We are still working to close our financial reporting for the quarter and our final results could be slightly different."*

**Preliminary figures disclosed (explicitly non-final):**

| Metric | Value | vs. consensus/prior year |
|---|---|---|
| Revenue | $17.2B | up 1% YoY; ~$660M below the ~$17.86B analysts expected |
| GAAP EPS | $2.27 | down 2% YoY |
| Non-GAAP operating EPS | $2.93 | up 5% YoY, but below the ~$3.02 consensus |
| Software | up 5% | |
| Consulting | flat (+1% constant currency) | |
| Infrastructure | **down 7%** | driven by a shortfall in Z (mainframe) performance and the associated software stack, primarily in Transaction Processing |

**Causes management cited directly:**
1. **Client capex reprioritization:** in the last few weeks of June, clients shifted quarterly capex spend toward servers, storage, and memory purchases to secure supply-constrained infrastructure ahead of expected price increases — the same memory-chip-shortage dynamic the triggering Telegram video's title referenced for Micron/SanDisk/SK hynix. Krishna: IBM "anticipated some supply chain related impact" but "did not anticipate the magnitude of the capex reprioritization."
2. **Execution failure:** "We did not adapt and move quickly enough, and numerous large deals failed to close on the timelines we expected, driving the majority of our shortfall."
3. **Distraction:** clients were reportedly distracted by "rapidly-evolving, industry-wide cybersecurity concerns."

### 2.2 Market reaction (independently corroborated, multiple outlets)

IBM shares fell **25.2% on 14 July 2026** to ~$217 — its **worst single-day drop on record**, surpassing the 23.7% fall on Black Monday, 19 October 1987. Market cap loss ~$67B. Shares have continued drifting down since (to today's live $213.25), for the cumulative −27.60% move computed above.

Sources: [CNBC](https://www.cnbc.com/2026/07/14/ibm-warns-second-quarter-earnings-fell-short-of-expectations.html), [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-14/ibm-says-second-quarter-sales-missed-as-customers-pulled-back), [Forbes](https://www.forbes.com/sites/tylerroush/2026/07/14/ibm-shares-crashed-25-in-worst-day-ever-heres-why/), [Yahoo Finance](https://finance.yahoo.com/news/ibm-stock-plummets-more-than-25-on-q2-earnings-warning-150605880.html), IBM's own 8-K/Ex-99.1 (SEC EDGAR, primary source, linked above).

### 2.3 Resolving the Telegram/video claim

**Verdict: essentially accurate — an unusual case.** The video's "IBM fell 25%" headline matches the actual single-day 14-July move (25.2%) closely, and the cumulative move since the last checked reference (−27.60%) is if anything larger. Unlike prior Telegram-triggered re-checks in this repo (e.g. the 2026-07-08 MU session, where a claimed price/cause was found inaccurate), this is a rare instance where the clickbait-sounding claim holds up under independent, primary-sourced verification. The cause is real, material, and well-documented — a genuine Rule 9 "earnings" category event (a preliminary earnings/guidance warning ahead of the scheduled report), not an unexplained move.

### 2.4 Full 6-category Rule 9 checklist (plus nanostack, matching the 07-09 addendum's structure)

| Category | Result |
|---|---|
| **Earnings** | **YES — fires.** 14 Jul 2026 Form 8-K preliminary Q2 2026 results, materially below expectations (see §2.1). Full results still due 22 Jul 2026. |
| Guidance revision | The preannouncement itself functions as a de facto negative guidance signal for Q2; no explicit FY2026 full-year guidance revision found in the 14 Jul letter — management says more detail comes with the 22 Jul call. |
| Management change | None. Krishna (CEO)/Kavanaugh (CFO) unchanged; Laguarta's board election predates 06-25. Confirmed via WebSearch — no new officer/board changes found for July 2026. |
| M&A | None new since 07-09. WebSearch for "IBM acquisition July 2026" surfaced only older, already-known items (Confluent, HashiCorp, DataStax) predating this window — no fresh announcement found. |
| Macro shift | None IBM-specific beyond the sector-wide memory-chip supply/pricing dynamic already captured under "Earnings" above. |
| Nanostack chip commercialization timeline | No new information found this session; last confirmed (07-09) at ~5 years out (~2031), no acceleration. Not re-verified in depth this session — out of scope given the dominant, obviously-fired Earnings trigger below. |
| **>15% unexplained price move** | **Move confirmed real and large (−27.60%), but it is *explained*, not unexplained** — directly and primarily by the 14 Jul earnings preannouncement above. Still counts as a fired Rule 9 trigger via the Earnings category regardless. |

**Net effect: Rule 9 fires — genuinely, this time.** Per this task's branching instruction, this requires a full Phase 01 Quality Score recomputation (§3) and a new dated watchlist file (per [watchlist/README.md](../watchlist/README.md)'s rule that a fired Rule 9 trigger warrants a fresh dated pointer "even if the score/action ends up unchanged").

---

## 3. Phase 01 — Quality Score recomputation (2026-06-29 methodology)

### 3.1 Data-availability check — is there new complete financial-statement data?

Before recomputing, checked whether a new, complete (audited/reviewed) fiscal quarter has become available since 07-09. Re-pulled `yfinance` (same `YF_DISABLE_CURL_CFFI=1` / `CURL_CA_BUNDLE=/root/.ccr/ca-bundle.crt` setup as prior sessions):

```
quarterly_financials columns:  2026-03-31, 2025-12-31, 2025-09-30, 2025-06-30, 2025-03-31
quarterly_balance_sheet columns: 2026-03-31, 2025-12-31, 2025-09-30, 2025-06-30, 2025-03-31, 2024-12-31
quarterly_cashflow columns:      2026-03-31, 2025-12-31, 2025-09-30, 2025-06-30, 2025-03-31, 2024-12-31
```

**No new quarter has appeared — 2026-03-31 (Q1 FY2026) remains the latest complete, structured financial-statement data.** This is expected: IBM's own 14 July 2026 letter explicitly describes the Q2 2026 figures as **preliminary and non-final** ("we are still working to close our financial reporting for the quarter"), and the preannouncement itself discloses only revenue, EPS, and high-level segment growth rates — not the balance sheet, cash flow statement, tax provision, or invested-capital detail the Quality Score's Profitability/Balance-Sheet/FCF-Quality sub-scores require. Per this framework's standing "never invent or estimate financial data" rule and its established "guidance/self-reported metrics are not scored" convention (see [glossary.md](../framework/glossary.md) — Core, AOI, Benchmark EBIT/EPS entries), the preliminary Q2 figures are used **only as qualitative, dated, primary-sourced context for why the price moved** (§2.1), never plugged into the Quality Score inputs below. A new glossary entry, "Earnings preannouncement (preliminary results)," documents this convention for future sessions.

### 3.2 Recomputation — identical inputs, identical result

Because the underlying trailing TTM financial-statement basis is unchanged (still Q2 FY2025 + Q3 FY2025 + Q4 FY2025 + Q1 FY2026), the Quality Score recomputes to the **exact same figures** as the 2026-07-09 session. Reproduced here in full per this task's "show every calculation" requirement, not merely cross-referenced:

**TTM inputs (unchanged from 07-09):** Revenue $68.912B, Gross Profit $40.215B, EBIT $12.510B, EBITDA $17.628B, Net Income $10.754B, Tax Provision −$0.173B, Pretax Income $10.557B → effective tax rate −1.64%. OCF $13.992B, CapEx −$1.734B, FCF $12.258B. Balance sheet (2026-03-31): Total Debt $69.802B, Cash $10.819B, Net Debt $55.542B, Invested Capital (latest-quarter) $99.335B.

| Sub-score (weight) | Inputs | Value |
|---|---|---|
| Profitability (25%) | NetMargin_Component 52.02 (TTM Net Margin 15.61%), ROIC_Component 42.67 (TTM ROIC 12.80% = NOPAT $12.715B ÷ Invested Capital $99.335B); no FCF-positivity cap | **47.34** |
| Margins (15%) | GrossMargin_Score 72.95 (TTM Gross Margin 58.36%); no structural-trend bonus (margin already >40%) | **72.95** |
| Growth (20%) | Growth_Score base 14.88 (Revenue 3yr CAGR 3.72%, FY2022→FY2025, unchanged — FY2025 still latest closed fiscal year); +10 TAM-expansion/pricing-power modifier (unchanged basis: Q1 FY2026 Software +11.3%/Infrastructure +15.3% YoY, gen-AI book of business, confirmed 2026 list-price increases) | **24.88** |
| Balance Sheet (15%) | Net Debt/EBITDA 3.15x → **fires the hard disqualifier independently** (>2.5x standard threshold; interest coverage 6.41x, far below the >15x the asset-light override would require) | **21.23** |
| Moat (15%) | 3 of 5 signals (market share, brand premium/pricing power, switching costs); network effect and scale cost advantage not credited | **60.0** |
| FCF Quality (10%) | TTM FCF/NI = 114.0%, capped | **100.0** (capped) |

```
Quality Score = 47.34×0.25 + 72.95×0.15 + 24.88×0.20 + 21.23×0.15 + 60.0×0.15 + 100.0×0.10
              = 11.835 + 10.9425 + 4.976 + 3.1845 + 9.0 + 10.0
              = 49.94 → rounds to 49.9
```

**Quality Score = 49.9 / 100.0 — recomputed, unchanged from 2026-07-09.** Fails the 80.0+ gate on the weighted score alone, and independently fails via the Net Debt/EBITDA hard disqualifier (3.15x). No Composite Score computed (requires clearing the gate first). No Phase 02 valuation work performed (moot given the gate result).

### 3.3 Qualitative flag — the Growth modifier's basis is now under pressure

The 07-09 session's +10 Growth modifier rested substantially on Infrastructure/IBM Z momentum (Q1 FY2026: Infrastructure +15.3% YoY, IBM Z +51% YoY). The 14 July preliminary release shows that trend has **sharply reversed**: Infrastructure −7% YoY in the preliminary Q2 read, driven specifically by a Z-performance/Transaction-Processing shortfall — the same product line that drove the prior quarter's bonus. This is flagged here as a **material open question for the 22 July full earnings review**, not pre-judged or scored now (final, complete data isn't available yet, and the preliminary figures aren't sufficiently detailed to recompute the modifier rigorously). If the deceleration is confirmed and sustained in the final Q2 print and 10-Q, the Growth sub-score's TAM/pricing-power bonus would be a strong candidate for removal or reduction at that time.

---

## 4. Recommendation

# **PASS — Quality Score 49.9/100.0 (recomputed, unchanged), fails the 80.0+ gate, also independently failed by the Net Debt/EBITDA hard disqualifier (3.15x). Do not enter.**

The triggering Telegram video's "25% fall" claim is, unusually, essentially accurate: IBM's live price is down 27.60% from the $294.55 (2026-07-09) reference, driven by a real, primary-sourced, materially negative event — a 14 July 2026 preliminary Q2 2026 earnings warning (Form 8-K) that produced the stock's worst single-day decline on record. This is a genuine Rule 9 "Earnings" trigger. A full Phase 01 Quality Score recomputation was run per this task's instructions; because no new complete/audited quarterly financial-statement data exists yet (the preliminary release is explicitly non-final and lacks the detail the score requires), the recomputation reproduces the identical 49.9/100.0 result from 2026-07-09 — Quality Score is a trailing-fundamentals measure and doesn't move on price or on unscored preliminary guidance. IBM's Phase 01 FAIL verdict (originally from 06-25) stands, now reconfirmed a third time from three different angles (binary 8-criterion screen, first Quality Score computation, and this recomputation).

**No position opened — nothing to log in `decisions/`.**

---

## 5. Next review trigger

**IBM's full Q2 FY2026 earnings and 10-Q, scheduled 22 July 2026** — now the primary mandatory Rule 9 point, just 5 days away. This is the point at which: (1) final, audited Q2 FY2026 figures become available and can actually roll into the TTM window (replacing Q2 FY2025), (2) the Growth sub-score's TAM/pricing-power modifier can be properly reassessed against the confirmed Infrastructure/Z deceleration flagged in §3.3, and (3) any formal FY2026 guidance revision (not yet given in the 14 Jul preliminary letter) would appear. Also watch, per the standing 07-09 triggers: sustained deleveraging toward Net Debt/EBITDA <2.5x, ROIC/Net Margin clearing 15% on a normalized tax basis, a reversal to sustained net share buybacks, and any further >15% unexplained move from today's $213.25 reference.

---

## 6. Files touched this session

- `watchlist/not-in-portfolio/IBM/IBM-2026-07-17.md` — **new dated file** (Rule 9 trigger fired, per README's rule that this warrants a fresh dated pointer even with an unchanged score/action)
- `framework/glossary.md` — added "Earnings preannouncement (preliminary results)" term, alphabetically before "EBIT"
- `sessions/2026-07-17-new-position-ibm.md` — this file

`watchlist/STALE.md` not touched (IBM has no STALE.md row — Phase 01 FAIL entries are exempt from the stale-score mechanism).

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **CAGR** — Compound Annual Growth Rate.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization.
- **Earnings preannouncement (preliminary results)** — a company's own disclosure, typically via SEC Form 8-K, of selected results ahead of its full scheduled earnings report; explicitly non-final and not used as a scored input here. IBM's 14 July 2026 preannouncement is the central event this session investigates.
- **EPS** — Earnings Per Share.
- **FCF** — Free Cash Flow.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income, an earnings-quality check.
- **Form 8-K** — a US company's "current report" filed with the SEC to disclose a material event between its regular quarterly/annual filings; the primary source for IBM's 14 Jul 2026 preannouncement.
- **GAAP** — Generally Accepted Accounting Principles.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted score; IBM's Net Debt/EBITDA fires this one independently.
- **Invested Capital** — the total capital (debt + equity, netted for cash) put to work in a business — the denominator in ROIC.
- **Moat** — a durable competitive advantage.
- **NOPAT** — Net Operating Profit After Tax, the numerator of ROIC.
- **Net Debt/EBITDA** — a leverage ratio; this framework's primary balance-sheet-risk gate.
- **Quality Score** — this framework's 0–100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02. IBM scores 49.9, unchanged across two independent computations.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 9** — this framework's list of events that force an immediate re-valuation: earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move. Fires here via the Earnings category.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results.

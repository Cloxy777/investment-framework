# NEW POSITION (Quality Score Engine addendum) — NOK (Nokia Corporation, ADR) — 2026-07-10

**Task type:** NEW POSITION — Quality Score Engine addendum (lightweight, per the CCL precedent), not a full re-evaluation
**Date:** 10 Jul 2026
**Ticker:** NOK (Nokia Corporation, ADR)
**Prior session:** [2026-06-24-new-position-nok.md](2026-06-24-new-position-nok.md) — Phase 01 FAIL (3 of 8 criteria: net margin, ROIC, revenue 3yr CAGR −5.76%), predates the 2026-06-29 Quality Score engine addition — NOK has never had a Quality Score computed until this session
**Current NOK portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session exists

NOK's 06-24 session failed Phase 01 (the binary quality screen that predates the 2026-06-29 Quality Score engine) and was never scored under the new 0-100.0 engine. Per this task's explicit scope, this session does two things only:

1. A Rule 9 check, with a specific focus on whether the AWS Autonomous Network Fabric / Databricks telecom-data-platform AI-networking partnerships (the trigger for the 06-24 look) have converted into delivered/quantified revenue — the specific condition the 06-24 session flagged as capable of flipping the failing growth criterion.
2. Compute NOK's first-ever Quality Score under the current engine, with every sub-score shown, using the freshest TTM data available.

Per the task's branching instruction, a fuller Phase 01 re-check (or a new dated watchlist file) is only warranted if a Rule 9 trigger fired that changes the Phase 01 verdict. As shown below, none did, so this stays an addendum appended to the existing watchlist file, not a new one.

---

## 1. Live price (Rule 0)

| Source | Price | Timestamp |
|---|---|---|
| **IBKR live snapshot** (primary, contract_id 661513, NYSE) | **$12.34** | 2026-07-10 15:14:50 UTC (`is_close: false`, intraday) |
| yfinance `currentPrice` (cross-check) | $12.335 | same session |

Bid/ask $12.33/$12.34. Day change −$0.56 (−4.34%). 52-week range $3.94-$17.45 (high set within the trailing 13 weeks, per IBKR `misc_statistics`). Change since the 06-24 baseline ($13.90): **−11.2%** — below the >15% Rule 9 unexplained-move threshold, and explained rather than unexplained (see §2).

---

## 2. Rule 9 checklist (all 6 categories explicitly checked)

| Category | Result |
|---|---|
| Earnings | **NO** — Q2 2026 results are scheduled for 23 July 2026 (before market open), still 13 days in the future as of this session. Source: [Nokia's 2026 financial calendar](https://www.nokia.com/newsroom/nokia-corporations-financial-calendar-for-2026/). |
| Guidance revision | No *new* revision since 06-24. Nokia raised 2026 growth guidance (Network Infrastructure to 12-14% from 6-8%; Optical+IP to 18-20% from 10-12%) — but at the Q1 2026 print in **April 2026**, before the 06-24 baseline. |
| Management change | None since 06-24 (Justin Hotard remains CEO; last Group Leadership Team change was July 2025). |
| M&A | None since 06-24 (Infinera acquisition closed February 2025). |
| Macro shift | None specific to NOK identified. |
| >15% unexplained price move | No (−11.2%, and explained below). |

### The specific condition flagged in the 06-24 session — checked directly

Did the AWS Autonomous Network Fabric / Databricks AI-networking partnerships convert into delivered/quantified revenue? **No.**

- The AWS Autonomous Network Fabric expansion (announced ~2026-06-25) is pre-commercial: Nokia's own press release states "commercial availability expected **later this year**." [Source](https://www.nokia.com/newsroom/nokia-amazon-web-services-expand-collaboration-to-deliver-autonomous-networks-built-for-the-ai-era/)
- The Databricks work is "the successful completion of a joint **proof of concept**" — a technical validation milestone, not a commercial deployment.
- The headline figure behind this week's stock rally — JPMorgan citing **~€1B in AI/cloud-related, mainly optical, orders**, prompting a price-target hike to $21 from $14 — is explicitly orders/backlog, not recognized revenue. Nokia's FY2025 annual report separately discloses €2.4B in AI & Cloud orders during 2025 and €1.0B in Q1 2026 alone — again, orders, not consolidated revenue recognition.
- TTM revenue through Q1 2026 (€19.996B) is essentially flat with FY2025 (€19.889B); the 3-year revenue CAGR is unchanged at **−5.76%**.

**Net effect: no Rule 9 trigger fired.** This confirms the addendum-only path.

**Sources:** [Nokia AWS press release](https://www.nokia.com/newsroom/nokia-amazon-web-services-expand-collaboration-to-deliver-autonomous-networks-built-for-the-ai-era/); [Nokia 2026 financial calendar](https://www.nokia.com/newsroom/nokia-corporations-financial-calendar-for-2026/); [Nokia 2025 Annual Report, SEC 6-K EX-99.1](https://www.sec.gov/Archives/edgar/data/924613/000110465926024172/tm268130d1_ex99-1.htm); WebSearch coverage (Timothy Sykes news aggregator 2026-07-09 for the JPMorgan PT hike; Investing.com for the Q1 2026 guidance raise).

---

## 3. Refreshed TTM financials (through Q1 2026, quarter ended 2026-03-31)

**Data-sourcing note:** `yfinance` worked via plain `requests` this session (curl_cffi browser-impersonation unavailable in this environment; same fallback path used in the CCL 07-06 session) with `YF_DISABLE_CURL_CFFI=1` and `CURL_CA_BUNDLE=/root/.ccr/ca-bundle.crt` set. No blocking rate-limit encountered.

### Quarterly income statement / cash flow (4 most recent, EUR millions)

| Quarter end | Revenue | Gross Profit | EBIT | EBITDA | Net Income | Pretax | Tax Provision | OCF | FCF |
|---|---|---|---|---|---|---|---|---|---|
| 2025-06-30 | 4,546 | 1,971 | 80 | 365 | 90 | 123 | 40 | 209 | 88 |
| 2025-09-30 | 4,828 | 2,110 | 239 | 525 | 78 | 229 | 150 | 597 | 429 |
| 2025-12-31 | 6,125 | 2,754 | 789 | 1,073 | 542 | 599 | 64 | 375 | 227 |
| 2026-03-31 | 4,497 | 1,988 | 63 | 272 | 86 | 180 | 93 | 783 | 629 |
| **TTM sum** | **19,996** | **8,823** | **1,171** | **2,235** | **796** | **1,131** | **347** | **1,964** | **1,373** |

Balance sheet (2026-03-31): Total Debt €3,325M, Cash & Equivalents €4,951M → **Net Debt = −€1,626M** (net cash); Invested Capital €23,559M.

Annual figures (FY2022-FY2025) re-verified this session and unchanged from 06-24: Revenue €23,761M(22)→€21,138M(23)→€19,220M(24)→€19,889M(25); Net Margin 17.89%(22, tax-benefit artifact)/3.15%(23)/6.64%(24)/3.27%(25); ROIC 7.40%(22)/5.90%(23)/8.06%(24)/3.24%(25); Gross Margin 42.51%(22)/40.43%(23)/46.12%(24)/43.54%(25); Net Debt/EBITDA net-cash all 4 years; FCF/NI 21%(22)/100%(23)/158%(24)/225%(25).

### Recomputed ratios (TTM through Q1 2026)

```
Net Margin (TTM)   = 796 / 19,996 = 3.98%
Gross Margin (TTM) = 8,823 / 19,996 = 44.13%
Effective tax rate (TTM) = 347 / 1,131 = 30.68%
NOPAT (TTM) = EBIT 1,171 × (1 − 0.3068) = 811.7
ROIC (TTM) = 811.7 / 23,559 = 3.45%
Net Debt/EBITDA (TTM) = −1,626 / 2,235 = −0.73× (net cash)
FCF/NI (TTM) = 1,373 / 796 = 172.5%
Revenue 3yr CAGR (FY2022→FY2025, unchanged) = −5.76%
```

None of the three previously-failing Phase 01 criteria (net margin, ROIC, revenue growth) crossed their thresholds — all remain decisively on the failing side, essentially flat to the 06-24 figures. **Confirms the addendum-only path — no fuller Phase 01 re-check or new dated file is warranted.**

---

## 4. Quality Score Engine — NOK's first-ever computation

Per [framework/quality-scoring.md](../framework/quality-scoring.md) (methodology version 2026-06-29). Full detail and the worked formula are in the [watchlist addendum](../watchlist/not-in-portfolio/NOK/NOK-2026-06-24.md); summarized here:

| Sub-score (weight) | Score |
|---|---|
| Profitability (25%) | 12.4 |
| Margins (15%) | 55.2 |
| Growth (20%) | 10.0 |
| Balance Sheet (15%) | 100.0 |
| Moat (15%) | 40.0 |
| FCF Quality (10%) | 100.0 |

```
Quality Score = 12.4×0.25 + 55.2×0.15 + 10.0×0.20 + 100.0×0.15 + 40.0×0.15 + 100.0×0.10
              = 3.10 + 8.28 + 2.00 + 15.00 + 6.00 + 10.00
              = 44.4
```

**Quality Score = 44.4 / 100.0 — fails the 80.0+ gate**, decisively (44.4 points short). Unlike CCL's addendum, **no hard disqualifier independently fires** for NOK — FCF positive 4+ consecutive periods, FCF/NI below 70% only 1 of the last 4 years (not 2+ consecutive), and Net Debt/EBITDA is net-cash (comfortably under any threshold). NOK fails purely on the weighted score, driven overwhelmingly by weak Profitability (12.4 — TTM Net Margin 3.98%/ROIC 3.45%, both far below the 15%+ needed for a mid-range component) and a Growth sub-score that clamps near zero because trailing revenue is still shrinking, even after applying the +10 TAM-expansion modifier for the AI & Cloud segment's documented SAM growth.

**Cross-check on FY2025-annual basis** (matching the 06-24 session's original methodology): Quality Score = 43.9 — same conclusion, within 0.5 points of the TTM-based figure.

### Moat Signal detail (cited evidence required per signal)

| Signal | Result | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | Dell'Oro's Q1 2026 trailing-four-quarter RAN vendor ranking (Huawei, Ericsson, Nokia, ZTE, Samsung) "changed very little" — third-party citation via IEEE ComSoc Technology Blog |
| Switching costs | **TRUE** | Documented mechanism: proprietary RAN integration depth and multi-year telecom-operator contracts create real vendor lock-in — general RAN-industry literature (TelecomFlow, Tanaza) |
| Brand premium (pricing power) | FALSE | The RAN market itself is described by the same sources as "a managed asset, not a growth engine" — flat and commoditizing; no cited NOK-specific price-increase-without-volume-loss evidence |
| Network effect | FALSE | No two-sided marketplace dynamics for a telecom-hardware vendor |
| Scale cost advantage | FALSE | No cost-per-unit data found showing a documented gap vs. smaller competitors |

Moat_Score = (2/5) × 100 = **40.0**

**No Composite Score computed** (requires clearing the 80.0+ gate first). **No Phase 02 valuation work performed** (moot given the gate result).

---

## 5. Recommendation

# **PASS — Quality Score 44.4/100.0, fails the 80.0+ gate outright (no hard disqualifier needed). Do not enter. Watchlist addendum appended, no new file created.**

The AWS/Databricks AI-networking partnerships flagged in the 06-24 session as the specific condition that could flip this name remain in the pre-revenue stage — pre-commercial availability, a completed proof-of-concept, and €1-2.4B of orders (not delivered revenue). Genuinely positive momentum for a strategic sub-segment (reflected here via the Growth sub-score's TAM-expansion modifier), but nowhere close to moving NOK's core profitability and consolidated growth numbers, which remain the dominant drivers of a Quality Score more than 35 points below the gate.

**No position opened — nothing to log in `decisions/`.**

---

## 6. Files touched this session

- `watchlist/not-in-portfolio/NOK/NOK-2026-06-24.md` — appended the Rule 9 check + Quality Score addendum as a dated note (no new file, per the task's branching instruction — no Phase 01 verdict change)
- `framework/glossary.md` — added **RAN (Radio Access Network)** and **SAM (Serviceable Addressable Market)**
- `sessions/2026-07-10-new-position-nok.md` — this file

`watchlist/STALE.md` was not touched (NOK was not listed there — it predates the Quality Score engine but was never a "stale re-score" case, it was a Phase 01 FAIL that had never been scored at all).

No `git` commands were run this session per task instructions.

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **ADR (American Depositary Receipt)** — a US-listed security representing shares of a non-US company; confirmed 1-for-1 for NOK.
- **Backlog** — the dollar value of signed customer orders not yet recognized as revenue; NOK's €1.0-2.4B in disclosed AI & Cloud "orders" falls here, not delivered revenue.
- **CAGR** — Compound Annual Growth Rate.
- **Dell'Oro Group** — an independent telecom/networking-equipment market-research firm; source of the RAN vendor-share ranking cited for NOK's Moat Signal "market share" evidence.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization.
- **Effective tax rate** — the actual share of pretax income paid as tax; NOK's TTM figure (30.68%) is used to compute NOPAT.
- **FCF** — Free Cash Flow.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income; NOK's TTM ratio (172.5%) is inflated by a thin Net Income denominator, not unusually strong cash generation.
- **Hard disqualifier** — one of three Quality Score conditions that fail a company regardless of weighted score; none fire for NOK.
- **Moat** — a durable competitive advantage; NOK scores 2 of 5 cited signals.
- **Net Debt/EBITDA** — a leverage ratio; NOK's TTM figure is net-cash (−0.73×).
- **NOPAT** — Net Operating Profit After Tax, the numerator of ROIC.
- **Quality Score** — this framework's 0-100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02. NOK scores 44.4 on its first-ever computation.
- **RAN (Radio Access Network)** — the base-station/radio hardware connecting mobile devices to a telecom operator's core network; NOK's largest, most commoditized segment.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 9** — this framework's list of events that force an immediate re-valuation: earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move.
- **SAM (Serviceable Addressable Market)** — the subset of a company's TAM its current products/geography can realistically serve; NOK's AI & Cloud segment SAM is €17B (+28% YoY), distinct from consolidated company revenue, which is still shrinking.
- **TAM** — Total Addressable Market.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results.

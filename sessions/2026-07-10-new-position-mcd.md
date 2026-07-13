# NEW POSITION (Quality Score Engine addendum) — MCD (McDonald's Corporation) — 2026-07-10

**Task type:** NEW POSITION — Quality Score Engine addendum (lightweight, per the CCL 2026-07-06 precedent), not a full re-evaluation
**Date:** 10 Jul 2026
**Ticker:** MCD (McDonald's Corporation, NYSE)
**Prior session:** [2026-06-24-new-position-mcd.md](2026-06-24-new-position-mcd.md) — Phase 01 FAIL (2 of 8 criteria: revenue 3yr CAGR 5.06% vs >8-10%, Net Debt/EBITDA 3.56-4.10× vs <2-2.5×), predates the 2026-06-29 Quality Score engine addition — MCD has never had a Quality Score computed until this session
**Current MCD portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session exists

MCD's 06-24 session failed Phase 01 (the binary quality screen that predates the 2026-06-29 Quality Score engine) and was never scored under the new 0-100.0 engine. Per this task's explicit scope, this session does two things only:

1. A Rule 9 check — all 6 trigger categories (earnings, guidance revision, management change, M&A, macro shift, >15% unexplained price move), with specific attention to the two conditions the 06-24 session flagged as what would flip the Phase 01 verdict: a sustained comps/unit-growth re-acceleration, or a credible multi-year deleveraging plan.
2. Compute MCD's first-ever Quality Score under the current engine, with every sub-score shown, using the freshest TTM data available.

Per the task's branching instruction, a fuller Phase 01 re-check (or a new dated watchlist file) is only warranted if a Rule 9 trigger fired that flips the verdict on the two previously-failing criteria. As shown below, no Rule 9 trigger fired at all, so this stays an addendum appended to the existing watchlist file — no new file created.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$277.22** | IBKR `get_price_snapshot`, contract_id 9408 (same contract as the 06-24 session), `ts` 1783695736 → 2026-07-10 15:02:16 UTC, `is_close: false` |
| Cross-check | $277.21 | Yahoo Finance chart API (`regularMarketPrice`, fetched fresh via plain `requests` — see data-sourcing note below) |
| Bid/ask | $277.16 / $277.25 | Same IBKR snapshot |
| 52-week range | $264.53 – $339.85 | IBKR `misc_statistics` |
| Baseline (06-24) | $271.95 | Prior session |
| Change since 06-24 | **+1.94%** | Computed |

Well short of the >15% Rule 9 unexplained-move threshold.

**Data-sourcing note:** `yfinance`'s own HTTP client (`curl_cffi`) again failed the proxy TLS handshake (`curl: (35) Recv failure: Connection reset by peer`) — the same limitation documented in the 2026-07-06 CCL session. Worked around identically: Yahoo Finance's public `chart` and `fundamentals-timeseries` endpoints fetched directly via plain `requests`, using the same field names yfinance itself uses internally. Cross-checked against stockanalysis.com (via WebFetch) for annual ROIC and Net Debt/EBITDA continuity with the 06-24 session's methodology. No required metric was missing or invented — every figure has a cited source.

---

## 2. Rule 9 checklist (all 6 categories)

| Category | Result |
|---|---|
| Earnings | No new earnings since 06-24. Q1 FY2026 (quarter ended 2026-03-31) was reported 2026-05-07 — already public before the 06-24 session. Next earnings (Q2 FY2026) due **2026-08-05**. |
| Guidance revision | None since 06-24 — FY2026 targets reaffirmed at the May 7 Q1 call, before 06-24. |
| Management change | CEO Chris Kempczinski / CFO Ian Borden unchanged (confirmed via WebSearch). A new Chief Development Officer, USA (Bryan Brown, ex-Raising Cane's) was announced 2026-07-01, effective 2026-07-14 — a single-country operational role, not C-suite/board-level. Flagged but not treated as a material Rule 9 trigger. |
| M&A | None found. |
| Macro shift | None new since 06-24 (CEO's cautious consumer-spending remark was made at the same May 7 call, already known). |
| >15% unexplained price move | No — +1.94%. |

**Comps/unit-growth re-acceleration check:** Q1 FY2026 US comps +3.9% (4th consecutive quarter of growth) — essentially the same trajectory already known at 06-24 (+3.8% cited then), no new data point since (Q1 predates 06-24, Q2 isn't out yet). **Credible multi-year deleveraging plan check:** none found — only gradual organic improvement in the equity deficit (−$6,566M peak Sep 2022 → −$1,286M Mar 2026) and debt/capital ratio (1.21→1.03), not a management-announced, targeted deleveraging program.

**Net effect: no Rule 9 trigger fired.** Nothing changes the substance of the 06-24 Phase 01 FAIL — revenue 3yr CAGR is unchanged at 5.06% (same FY2022→FY2025 base, no new complete fiscal year since 06-24) and Net Debt/EBITDA remains in the same 3.5–4.1× band (3.59× TTM / 3.70× FY2025-annual, both far above the 2.5× threshold). **Confirms the addendum-only path.**

---

## 3. Refreshed TTM financials (through Q1 FY2026, quarter ended 2026-03-31 — freshest complete quarter; Q2 not due until 2026-08-05)

| Metric | TTM value | Cross-check |
|---|---|---|
| Total Revenue | $27,447M | Sum of last 4 quarters: $27,445M |
| Gross Profit | $15,741M | Sum of last 4 quarters: $15,739M |
| EBIT | $12,715M | Sum of last 4 quarters: $12,715M (exact) |
| EBITDA | $14,960M | Sum of last 4 quarters: $14,960M (exact) |
| Net Income | $8,678M | Sum of last 4 quarters: $8,678M (exact) |
| Effective tax rate | 21.89% | `trailingTaxRateForCalcs` 0.218922 |
| Operating Cash Flow | $10,535M | Sum of last 4 quarters: $10,535M (exact) |
| CapEx | −$3,496M | Sum of last 4 quarters: −$3,496M (exact) |
| Free Cash Flow | $7,039M | Reconciles exactly to Yahoo's own `FreeCashFlow` field |

**Balance sheet (2026-03-31):** Total Debt $54,881M, Cash $1,170M, Common Equity −$1,285M (still negative, narrowing gradually). **Net Debt (Total Debt − Cash basis) = $53,711M.**

A data-basis discrepancy was flagged and resolved the same way as the CCL 07-06 precedent: Yahoo's own algorithmic `NetDebt` timeseries field ($38,935M) diverges sharply from Total Debt − Cash ($53,711M) and does not reconcile to any documented adjustment. The Total Debt − Cash basis was used throughout because it's the one that reconciles with the 06-24 session's own figures and with stockanalysis.com's independently-sourced annual Net Debt/EBITDA series (FY2025 3.70×, FY2024 3.68×, FY2023 3.56×, FY2022 4.10×, FY2021 3.65× — confirmed via fresh WebFetch this session, unchanged from 06-24).

### Recomputed ratios (TTM through Q1 FY2026)

```
Net Margin (TTM)   = $8,678M / $27,447M = 31.62%   (06-24 FY2025 basis: 31.85% — essentially flat)
Gross Margin (TTM) = $15,741M / $27,447M = 57.35%  (06-24 FY2025 basis: 57.41% — essentially flat)
ROIC (TTM) = NOPAT $9,931.4M [EBIT $12,715M × (1 − 21.89%)] / Invested Capital $52,426M
             [Total Debt $54,881M + Common Equity −$1,285M − Cash $1,170M] = 18.95%
             (06-24 FY2025 basis: 17.98%; stockanalysis.com FY2025 cross-check: 18.29% — corroborates this basis
             over Yahoo's own unreconciled TotalCapitalization-only Invested Capital field, which gives an
             unused 25.59%)
Net Debt/EBITDA (TTM) = $53,711M / $14,960M = 3.59×  (06-24 FY2025 basis: 3.70× — modest improvement, still far
             above 2.5×)
FCF/NI conversion (TTM) = $7,039M / $8,678M = 81.11%  (FY2025 83.92%, FY2024 81.14%, FY2023 85.67% — all >70%)
```

None of the two previously-failing Phase 01 criteria (revenue 3yr CAGR, Net Debt/EBITDA) crossed their thresholds.

---

## 4. Quality Score Engine — MCD's first-ever computation

Per [framework/quality-scoring.md](../framework/quality-scoring.md) (methodology version 2026-06-29). Full detail and citations are in the [watchlist addendum](../watchlist/not-in-portfolio/MCD/MCD-2026-06-24.md); summarized here:

| Sub-score (weight) | Score |
|---|---|
| Profitability (25%) | 81.58 |
| Margins (15%) | 71.69 |
| Growth (20%) | 30.24 |
| Balance Sheet (15%) | 10.25 |
| Moat (15%) | 40.0 |
| FCF Quality (10%) | 68.52 |

```
Quality Score = 81.58×0.25 + 71.69×0.15 + 30.24×0.20 + 10.25×0.15 + 40.0×0.15 + 68.52×0.10
              = 20.395 + 10.7535 + 6.048 + 1.5375 + 6.000 + 6.852
              = 51.586 → rounds to 51.6
```

**Quality Score = 51.6 / 100.0 — fails the 80.0+ gate.** MCD fails two independent ways at once:
1. **The weighted score itself** (51.6 < 80.0) — dragged down primarily by the Balance Sheet sub-score (10.25, reflecting persistent 3.5–4.1× leverage) and a below-average Growth sub-score (30.24, even after the +10 pricing-power modifier).
2. **A hard disqualifier**, independent of the weighted score: Net Debt/EBITDA (3.59–3.70× depending on basis) sits well above the 2.5× standard threshold — no asset-light override applies (MCD is a restaurant franchisor, not a payment network/financial). Per quality-scoring.md, this "fails regardless of weighted score."

FCF-positivity and FCF/NI-conversion hard disqualifiers do **not** fire (FCF positive 5+ consecutive periods; FCF/NI conversion above 70% every period checked). No Composite Score computed (requires clearing the gate first). No Phase 02 valuation work performed (out of scope, and moot given the gate result).

### Moat Signal detail (cited evidence required per signal)

| Signal | Result | Evidence |
|---|---|---|
| Market share stable or growing | **FALSE** | csimarket.com (Restaurants industry-segment revenue share): 14.73% Q1 2026 vs. 15.64% Q4 2025 — a QoQ *decline*, the opposite of "stable or growing" on the only citable recent data found |
| Brand premium (pricing power) | **TRUE** | Q1 FY2026 US comps +3.9%, 4th consecutive quarter of growth, driven "primarily by positive check growth" (price/mix, not just traffic) — [Restaurant Dive](https://www.restaurantdive.com/news/mcdonalds-q1-2026-positive-comp-sales-value-menu-innovation/819554/), McDonald's Q1 2026 results release |
| Network effect | FALSE | No two-sided marketplace dynamics for a restaurant franchisor |
| Switching costs | FALSE | MyMcDonald's Rewards is a marketing/loyalty program, not a documented lock-in mechanism with a switching cost |
| Scale cost advantage | **TRUE** | Largest U.S. purchaser of beef, pork, and potatoes (3.4B lbs of potatoes/year, ~5% of all U.S. egg production); combined-volume procurement runs ~15% below buying items separately — [Chain Store Guide](https://www.chainstoreguide.com/offthechain/2025/09/mcdonalds-extra-value-meals-a-supply-chain-game-changer/) |

Moat_Score = (2/5) × 100 = **40.0**

---

## 5. Recommendation

# **PASS — Quality Score 51.6/100.0, fails the 80.0+ gate (also independently failed by the Net Debt/EBITDA hard disqualifier). Do not enter. Watchlist addendum appended, no new file created.**

No Rule 9 trigger fired since the 06-24 Phase 01 FAIL. MCD's first Quality Score computation independently re-derives the same structural conclusion from a continuous rather than binary angle: strong margins, profitability, and a real (if narrower than initially assumed) moat, capped by persistent 3.5×+ leverage and a mature single-digit growth profile that are structural, multi-year features of the business rather than one-off misses.

**No position opened — nothing to log in `decisions/`.**

---

## 6. Files touched this session

- `watchlist/not-in-portfolio/MCD/MCD-2026-06-24.md` — appended the Rule 9 check + Quality Score addendum as a dated note (no new file, per the task's branching instruction — no Phase 01 verdict change)
- `framework/glossary.md` — added **AUV (Average Unit Volume)**, **Comparable sales (comps / same-store sales)**, and **Systemwide sales**
- `sessions/2026-07-10-new-position-mcd.md` — this file

`watchlist/STALE.md` was not touched (MCD was not listed there — it predates the Quality Score engine but was never a "stale re-score" case, it was a Phase 01 FAIL that had never been scored at all).

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **CAGR** — Compound Annual Growth Rate.
- **CapEx** — Capital Expenditure.
- **Comparable sales (comps)** — Sales growth at locations open at least a year, excluding new-unit growth.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization.
- **Effective tax rate** — the actual share of pretax income paid as tax.
- **FCF** — Free Cash Flow.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income, an earnings-quality check.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted score; MCD's Net Debt/EBITDA fires this one independently of the 51.6 weighted score.
- **Moat** — a durable competitive advantage.
- **NOPAT** — Net Operating Profit After Tax, the numerator of ROIC.
- **Net Debt/EBITDA** — a leverage ratio; this framework's primary balance-sheet-risk gate.
- **Net Margin** — Net Income ÷ Revenue.
- **Quality Score** — this framework's 0-100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02. MCD scores 51.6 on its first-ever computation.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — always fetch a live price before any valuation work.
- **Rule 9** — this framework's list of events that force an immediate re-valuation: earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move.
- **Systemwide sales** — total sales across all restaurants under a chain's brand, franchised and company-operated combined.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported results.

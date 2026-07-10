# NEW POSITION (Quality Score Engine addendum) — PLTR (Palantir Technologies Inc.) — 2026-07-10

**Task type:** NEW POSITION — Quality Score Engine addendum (lightweight, per the CCL 2026-07-06 precedent), not a full re-evaluation
**Date:** 10 Jul 2026
**Ticker:** PLTR (Palantir Technologies Inc., NASDAQ)
**Prior session:** [2026-06-23-new-position-pltr.md](2026-06-23-new-position-pltr.md) — Phase 01 FAIL (2 of 8 criteria: FCF yield, EV/EBIT), predates the 2026-06-29 Quality Score engine addition — PLTR has never had a Quality Score computed until this session
**Current PLTR portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session exists

PLTR's 06-23 session failed Phase 01 (6 of 8 criteria PASS, but decisively failed on FCF yield 0.943% and EV/EBIT 139.15× — both price-denominated cheapness filters) and was never scored under the 0–100.0 Quality Score engine, which was added six days later (2026-06-29). Per this task's explicit scope, this session does two things only:

1. A Rule 9 check — was PLTR's next quarterly earnings (flagged as due 2026-08-03) reported yet? Any quantified, primary-sourced confirmation of the Zeta Data Cloud / US-military-data-layer claims from the original triggering Telegram post, or any other Rule 9 trigger (guidance revision, management change, M&A, macro shift, >15% unexplained price move)?
2. Compute PLTR's first-ever Quality Score under the current engine, with every sub-score shown.

Per the task's branching instruction, a fuller Phase 01 re-check (or a new dated watchlist file) is only warranted if a Rule 9 trigger flips the Phase 01 verdict. As shown below, no trigger fired that changes it — the two failing criteria are, if anything, marginally worse at the new live price — so this stays an addendum appended to the existing watchlist file, not a new one.

---

## 1. Live price (Rule 0) and Rule 9 check

- **Live price used: $126.11** — IBKR `get_price_snapshot`, contract_id 444857009 (NASDAQ, confirmed via `search_contracts`), `ts` 1783697429 → 2026-07-10 15:30:29 UTC, `is_close: false` (live quote, bid $126.13 / ask $126.19). Cross-checked against Yahoo Finance's `chart` endpoint fetched moments later: `regularMarketPrice` $126.04–$126.15 — consistent.
- vs. $118.89 on 06-23 = **+6.07%** — well short of the >15% Rule 9 unexplained-move threshold, and explained regardless (see below).

**Data-sourcing note (same workaround as the CCL 2026-07-06 precedent):** `yfinance`'s own HTTP client (`curl_cffi`) could not complete a TLS handshake through this session's egress proxy. Worked around by calling Yahoo Finance's `ws/fundamentals-timeseries` endpoint directly via plain `requests` (which the proxy handles fine), using the same field names `yfinance` uses internally (`quarterlyTotalRevenue`, `trailingEBIT`, `trailingEBITDA`, `trailingNetIncome`, `quarterlyTaxRateForCalcs`, `trailingFreeCashFlow`, `trailingOperatingCashFlow`, `trailingCapitalExpenditure`, `quarterlyTotalDebt`, `quarterlyCashCashEquivalentsAndShortTermInvestments`, `quarterlyStockholdersEquity`, `quarterlyShareIssued`, `quarterlyGrossMargin`, `annual*` variants). Same underlying data source as the 06-23 session's `t.financials`/`t.cashflow`/`t.quarterly_*` calls.

**Confirmation no new quarter has been reported:** every TTM/quarterly field pulled fresh this session returns figures identical to the 06-23 session's own reconstruction (e.g. TTM Revenue $5,224.174M, TTM EBIT $1,991.965M, TTM FCF $2,688.276M, Cash & ST Investments $8,026.413M at 2026-03-31, Shares Issued 2,397.133M at 2026-03-31) — the latest reported quarter is still Q1 FY2026 (ended 2026-03-31). This independently confirms Q2 FY2026 earnings have not yet been reported.

**All 6 Rule 9 trigger categories checked:**

| Category | Result |
|---|---|
| Earnings | **NO — not yet reported.** Next report date is unconfirmed/inconsistent across sources (Catacal: 3 Aug 2026, unconfirmed; TipRanks: 10 Aug 2026, "confirmed"). Both are still future dates as of 2026-07-10. |
| Guidance revision | None since 06-23 — the last guidance raise (to ~71% FY2026 revenue growth, "largest guidance raise in company history") happened at the Q1 FY2026 report (~early May 2026), already baked into 06-23's TTM figures. |
| Management change | None — Alex Karp (CEO), David Glazer (CFO) unchanged. |
| M&A | None. A commercial partnership (not M&A): Palantir × Zeta Global, announced 2026-06-23 (same day as the prior session) — see §2. |
| Macro shift | None specific to PLTR — CEO Karp's 1 July 2026 CNBC remarks on OpenAI/Anthropic pricing coincided with an ~8% single-day stock move, a company-specific PR event, not a macro/rate-regime shift. |
| >15% unexplained price move | No — +6.07%, and explained by the above regardless. |

---

## 2. Confirming the triggering post's claims (Zeta Data Cloud, US military "data layer")

The 06-23 session's trigger was a Telegram post naming PLTR, whose Foundry/Zeta/military claims were explicitly *not* verified or used as inputs at the time (Phase 01 failed on trailing financials regardless). This session independently checked both via WebSearch:

- **Zeta Data Cloud: CONFIRMED, primary-sourced.** [Businesswire's official press release](https://www.businesswire.com/news/home/20260623062799/en/Palantir-and-Zeta-Global-Announce-Strategic-Partnership-to-Build-a-Unified-Data-and-AI-Infrastructure-for-the-Future-of-Marketing-with-Athena-by-Zeta-at-the-Center) and [Zeta Global's own newsroom](https://zetaglobal.com/news/palantir-and-zeta-global-announce-strategic-partnership/) confirm a strategic partnership announced 2026-06-23: Zeta's Data Cloud is being rearchitected on Palantir Foundry. Quantified only from Zeta's side ("could drive more than $100M in annual revenue in the coming years" — forward-looking, not yet booked revenue).
- **US military "data layer": CONFIRMED, but not new.** [Yahoo Finance/Breaking Defense coverage](https://finance.yahoo.com/technology/ai/articles/palantir-secures-foundational-role-ngc2-200500839.html) of the US Army's Next Generation Command and Control (NGC2) program shows Foundry underpins the program's cloud data layer (jointly with Anduril's Lattice for the edge-to-cloud mesh) — an extension of the pre-existing (July 2025) $10B, 10-year Army Enterprise Agreement, not a new quantified disclosure.

Neither moves trailing FCF/EBIT — both are forward-looking commercial/government developments, consistent with how the 06-23 session and the MU-deal precedent treated similar real-but-forward news: it doesn't retroactively repair a trailing, price-denominated cheapness failure.

---

## 3. Phase 01 verdict — recomputed at the live price, confirmed unchanged

TTM fundamentals are unchanged (§1). Recomputing the two previously-failing criteria at $126.11:

```
Market Cap = 2,397.133M shares × $126.11 = $302,302.4M
EV = Market Cap + Total Debt ($211.977M) − Cash & ST Investments ($8,026.413M) = $294,488.0M

FCF Yield (Market Cap) = $2,688.276M / $302,302.4M = 0.889%   (06-23: 0.943%)
FCF Yield (EV)         = $2,688.276M / $294,488.0M = 0.913%   (06-23: 0.970%)
EV/EBIT                = $294,488.0M / $1,991.965M = 147.84×  (06-23: 139.15×)
```

Both still fail their thresholds (>4% FCF yield, <20× EV/EBIT) — and both are marginally *worse* than 06-23, since price rose ~6% while trailing FCF/EBIT didn't move (no new quarter). **Phase 01 verdict is unchanged: still FAIL on the same 2 of 8 criteria.** Per this task's branching instruction, this confirms the addendum-only path — no fuller Phase 01 re-check, Turnaround Sub-Gate re-evaluation, or new dated file is warranted.

---

## 4. Quality Score Engine — PLTR's first-ever computation

Per [framework/quality-scoring.md](../framework/quality-scoring.md) (methodology version 2026-06-29). Full detail and the worked formula are in the [watchlist addendum](../watchlist/not-in-portfolio/PLTR/PLTR-2026-06-23.md); summarized here:

| Sub-score (weight) | Score |
|---|---|
| Profitability (25%) | 87.85 |
| Margins (15%) | 100.0 |
| Growth (20%) | 100.0 |
| Balance Sheet (15%) | 100.0 |
| Moat (15%) | 40.0 |
| FCF Quality (10%) | 100.0 |

```
Quality Score = 87.85×0.25 + 100.0×0.15 + 100.0×0.20 + 100.0×0.15 + 40.0×0.15 + 100.0×0.10
              = 21.96 + 15.00 + 20.00 + 15.00 + 6.00 + 10.00
              = 87.96 → 88.0
```

**Quality Score = 88.0 / 100.0 — clears the 80.0+ gate comfortably.** No hard disqualifier fires: FCF/NI conversion has stayed far above 70% every fiscal year on record (FY2023 332.3%, FY2024 246.9%, FY2025 129.3%, TTM 117.8%); Net Debt/EBITDA is negative (net cash — the best possible case); FCF has been positive every fiscal year since FY2022 plus TTM. The result is robust to the one genuinely judgment-dependent input (Moat): even at a worst-case Moat score of 0/5, the weighted Quality Score would still be ≈82.0, still above the gate.

This is a materially different read than the binary Phase 01 screen: PLTR fails Phase 01 (and would still fail Phase 02) purely on *price-denominated* cheapness (FCF yield, EV/EBIT), but scores strongly on the Quality Score engine's blend of profitability, margins, growth, balance-sheet strength, and cash-conversion quality. **No Composite Score computed** — that requires a Phase 02 Valuation Score too, and Phase 02 was never reached (Phase 01 FAIL stands unchanged). **No Phase 02 valuation work performed** (out of scope for this addendum, and moot given the Phase 01 gate result).

### Moat Signal detail (cited evidence required per signal)

| Signal | Result | Evidence |
|---|---|---|
| Market share stable or growing | **FALSE** | No quantified, third-party, category-matched market-share citation found. The one third-party figure located (6sense, "big data analytics" market, ~1.67% share) is a mismatched category for Palantir's actual government/enterprise-AI-ontology niche and isn't relied on. Absolute growth (customer count +31% YoY to 1,007 TTM, TCV +61% YoY, US government revenue +84% YoY) measures PLTR's own growth, not market *share* — marked false for lack of a clean matching source, per the framework's citation bar. |
| Brand premium (pricing power) | **TRUE** | Average revenue per top-20 customer +30% YoY to $75M; net dollar retention 150% (Q1 FY2026 earnings release/call) — expansion within existing accounts, not just new-logo growth. |
| Network effect | **FALSE** | No two-sided marketplace dynamic — Foundry/Gotham/AIP are single-tenant operational platforms. |
| Switching costs | **TRUE** | Palantir's proprietary "ontology" embeds an organization's data mappings, business logic, security rules, and decision workflows into the platform; replicating that on a competing platform requires rebuilding years of semantic modeling (cited: SuperML.dev, Pangeanic, and a first-hand Foundry-to-Fabric-IQ migration account documenting the cost). |
| Scale cost advantage | **FALSE** | No cost-per-unit data found showing a positive gap vs. smaller competitors; the only comparison located (DataWalk, a competitor's own marketing claim, treated cautiously) points the other way — 30–60% cost reduction claimed from migrating *off* Palantir. Not confirmed either way, but insufficient to mark true. |

Moat_Score = (2/5) × 100 = **40.0**

---

## 5. Recommendation

**PASS on Phase 01 (unchanged FAIL) — Quality Score 88.0/100.0, clears the 80.0+ gate. Do not enter. Watchlist addendum appended, no new file created.**

No Rule 9 trigger fired that changes the Phase 01 verdict — Q2 FY2026 earnings have not yet been reported (date itself unconfirmed across sources), and both the Zeta Data Cloud and NGC2/US-military claims from the original trigger were independently confirmed as real but don't move trailing FCF/EBIT. Recomputing the two failing Phase 01 criteria at the new live price ($126.11, +6.07% since 06-23) shows them marginally *worse*, not better (FCF yield 0.889% vs 0.943%; EV/EBIT 147.84× vs 139.15×). PLTR's first-ever Quality Score computation shows a genuinely high-quality business (88.0/100.0, robust even under a worst-case Moat assumption) trading at a price this framework's specific cheapness filters reject — the addendum changes *why* PLTR isn't held (quality isn't the problem; price is) without changing the action.

**No position opened — nothing to log in `decisions/`.**

---

## 6. Files touched this session

- `watchlist/not-in-portfolio/PLTR/PLTR-2026-06-23.md` — appended the Rule 9 check + Quality Score addendum as a dated note (no new file, per the task's branching instruction — no Phase 01 verdict change); updated the file's Glossary section and its "Next review trigger" section
- `framework/glossary.md` — added **NGC2 (Next Generation Command and Control)**, **Ontology (Palantir)**, and **TCV (Total Contract Value)**
- `sessions/2026-07-10-new-position-pltr.md` — this file

`watchlist/STALE.md` was not touched (PLTR was not listed there — it predates the Quality Score engine but was never a "stale re-score" case, it was a Phase 01 FAIL that had never been scored at all). No `git` commands were run this session.

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **CAGR** — Compound Annual Growth Rate.
- **EV (Enterprise Value)** — a company's total value to all capital providers: market cap + debt − cash.
- **EV/EBIT** — Enterprise Value divided by EBIT.
- **FCF (Free Cash Flow)** — cash a business generates after running and maintaining itself.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value).
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income, an earnings-quality check.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted score; none fire for PLTR.
- **Moat** — a durable competitive advantage.
- **Net Debt/EBITDA** — a leverage ratio; this framework's primary balance-sheet-risk gate. Negative for PLTR (net cash).
- **Net Retention Rate (NRR)** — the percentage of recurring revenue retained/expanded from an existing customer cohort over 12 months; PLTR's is 150%.
- **NGC2 (Next Generation Command and Control)** — the US Army's data-layer modernization program built on Palantir Foundry.
- **NOPAT** — Net Operating Profit After Tax, the numerator of ROIC.
- **Ontology (Palantir)** — Palantir's proprietary data/logic/decision modeling framework underlying its Switching Costs moat signal.
- **Quality Score** — this framework's 0-100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02. PLTR scores 88.0 on its first-ever computation.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 9** — this framework's list of events that force an immediate re-valuation: earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move.
- **TCV (Total Contract Value)** — the full dollar value of a signed customer contract over its entire term; PLTR's Q1 FY2026 TCV was $2.41B, +61% YoY.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results.

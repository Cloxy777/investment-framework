# NEW POSITION (Quality Score Engine addendum) — MU (Micron Technology, Inc.) — 2026-07-10

**Task type:** NEW POSITION — Quality Score Engine addendum (per the CCL/CVX precedent), not a full re-evaluation
**Date:** 10 Jul 2026
**Ticker:** MU (Micron Technology, Inc., NASDAQ)
**Prior sessions:** [2026-06-20-new-position-mu.md](2026-06-20-new-position-mu.md), [2026-06-22-new-position-mu.md](2026-06-22-new-position-mu.md), [2026-06-24-new-position-mu.md](2026-06-24-new-position-mu.md) — Phase 01 FAIL (4 of 8 criteria as of 06-24: revenue 3yr CAGR, FCF-positive-3-years, FCF yield, EV/EBIT), all predating the 2026-06-29 Quality Score engine — MU has never had a Quality Score computed until this session. The 06-24 entry explicitly flagged that Q3 FY2026 earnings (reported 06-24) had not yet propagated into yfinance/IBKR's structured quarterly data, and named "re-pull once Q3 FY2026 appears" as the primary next-review trigger.
**Current MU portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session exists

Two things, per explicit task scope:
1. Check whether Q3 FY2026 structured financial data has now propagated (over 2 weeks after the 06-24 earnings release), and re-run the four previously-failing Phase 01 criteria with real reported figures if so.
2. Compute MU's first-ever Quality Score under the current (2026-06-29) engine, with every sub-score shown.

Per the task's branching instruction, a fuller Phase 01 re-check (new dated watchlist file) is only warranted if the Phase 01 **gate verdict** itself flips. As shown below, one individual criterion (EV/EBIT) did flip from FAIL to PASS, but the gate's overall PASS/FAIL outcome did not (3 of 8 criteria still fail) — so this stays an addendum appended to the existing watchlist file.

## 1. Data-source note

`yfinance`'s own `curl_cffi`-based HTTP session hit a persistent TLS connection reset (`curl: (35) Recv failure: Connection reset by peer`) on every call through this environment's egress proxy, across 5 retries with backoff — not a rate limit (plain `requests` calls to the same Yahoo hosts succeeded immediately). Worked around by querying the same underlying Yahoo Finance APIs directly via `requests` with a browser User-Agent and a freshly-fetched crumb (`query1.finance.yahoo.com/v1/test/getcrumb` → `.../ws/fundamentals-timeseries/v1/finance/timeseries/MU`) — this is the identical data source `yfinance` wraps, not a substitute source, so the framework's data-sourcing discipline is unaffected. All figures below are traceable to that API and cross-checked against Micron's own SEC 8-K where available.

## 2. Live price (Rule 0)

- **IBKR `get_price_snapshot`**, contract_id 9939 (confirmed via fresh `search_contracts("MU")`, same conid used in all three prior sessions): **$980.50**, last trade ts 2026-07-10 15:19:55 UTC, `is_close: false` (live, regular session).
- Cross-check — yfinance/Yahoo `regularMarketPrice`: $981.8499, ts 2026-07-10 15:17:37 UTC (`marketState: REGULAR`) — 0.14% apart, ~2 minutes apart, both genuine live quotes.
- 52-week range (IBKR `misc_statistics`): low $103.22, **high $1,255.00** (a new all-time high set after 06-24, before today's pullback).
- Baseline (06-24 reference): $1,197.71. Change to today: **-18.14%** — exceeds the >15% Rule 9 threshold but is explained (§3).

## 3. Rule 9 check — all 6 categories, since 2026-06-24

| Category | Result |
|---|---|
| Earnings | Already covered by the 06-24 entry (the release itself). No new earnings event since; Q4 FY2026 due ≈2026-09-23 per yfinance's earnings calendar. |
| Guidance revision | Q4 FY2026 guidance issued at the same 06-24 call, not yet captured by any prior MU session (data hadn't propagated then): Revenue $50.0B ± $1.0B, GAAP gross margin ≈86%, GAAP EPS $30.73 ± $1.00 — a beat-and-raise, not a cut. |
| Management change | None — Sanjay Mehrotra (CEO/Chair), Mark Murphy (CFO) unchanged. |
| M&A / further deal disclosures | **YES.** 16 Strategic Customer Agreements (SCAs) disclosed at the same 06-24 call — binding multi-year take-or-pay contracts, ~20% of DRAM / ~30% of NAND volume, ~$100B floor-price contracted revenue (RPO ≈$100B across 14 of 16 agreements), ~$22B customer cash deposits, margin floors management says will exceed past cycle peaks. Financial substance not captured by the 06-24 session (scoped only to Rule 0 price + TTM ratios, before data propagated). See §5 for sourcing. |
| Macro shift | 10Y Treasury 4.553% (was 4.402% on 06-24) — still in the 3.5-5% bracket, no Rate Regime change. No new MU-specific export-control action since 06-24. |
| >15% unexplained price move | **Fired (-18.14%), but explained**, not unexplained: (a) round-tripped through a new 52-week high of $1,255.00 set in the days after 06-24 on the earnings/SCA news, before pulling back; (b) Michael Burry publicly disclosed a short position in MU on 2026-07-02 at $1,051.87/share, citing extreme extension above the 200-day moving average and MU's cyclical history — a market opinion, not treated as fact, but a documented contributor; (c) an active class-action lawsuit over alleged historical memory-chip price-fixing and recent insider share sales are cited by financial press as sentiment headwinds. No company-specific negative fundamental news; the same week's guidance was a raise. |

**Net effect: Rule 9 fired (M&A-category SCA disclosure + the large-but-explained price move), and it materially improves two TTM-denominated Phase 01 criteria (§4) — but does not flip the gate's overall PASS/FAIL verdict**, since 3 of 8 criteria still fail. Per this task's branching instruction, this stays an addendum, not a full re-evaluation.

## 4. Phase 01 re-run with real Q3 FY2026 data

Confirmed Q3 FY2026 (period end 2026-05-31) is now fully propagated: Revenue $41.456B, Gross Profit $35.056B (84.6% GAAP gross margin — reconciles exactly to the [SEC 8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000013/a2026q3ex991-pressrelease.htm)'s reported figures), EBIT $33.212B, EBITDA $35.576B, Net Income $28.243B, FCF $17.562B (OCF $25.388B − CapEx $7.826B).

| Check | 2026-07-10 (new) | 2026-06-24 (prior) | Threshold | Result |
|---|---|---|---|---|
| Gross margin | 72.57% (TTM) | 58.44% | >40% | PASS |
| Net margin | 55.91% (TTM) | 41.49% | >12% | PASS |
| ROIC/ROE proxy | 48.81% (TTM NOPAT/latest-qtr IC) | 33.28% | >15% | PASS |
| Revenue growth (3yr CAGR) | 6.71% (FY22→FY25, unchanged) | 6.71% | >8% | **FAIL (unchanged)** |
| FCF positive 3 consecutive years | FY2023 = -$6.117B (still in window) | same | required | **FAIL (unchanged)** |
| Net debt/EBITDA | -0.27x (net cash) | -0.084x | <2.5x | PASS (unchanged) |
| FCF yield | 2.36% (TTM FCF $26.172B / mkt cap $1,107.370B) | 0.76% | >4% | **FAIL (unchanged, ~3x less bad)** |
| EV/EBIT | 18.36x (TTM EBIT $59.294B, EV $1,088.751B) | 47.59x | <20x | **PASS — flipped from FAIL** |

**3 of 8 criteria still fail (down from 4). EV/EBIT flipped from FAIL to PASS** now that real Q3 FY2026 EBIT is reflected in the TTM denominator — exactly what the 06-24 entry flagged as plausible. **Overall Phase 01 verdict unchanged: still FAIL.** Revenue CAGR and FCF-positive-3-years remain structurally unaffected by any single quarter; both only resolve once FY2026 itself closes and is filed (≈Aug/Oct 2026), rolling FY2023's loss year out of the window.

## 5. Quality Score computation

| Sub-score (weight) | Inputs | Value |
|---|---|---|
| Profitability (25%) | NetMargin_Component 100.0 (capped, TTM 55.91%), ROIC_Component 100.0 (capped, TTM ROIC 48.81% = NOPAT $50.653B [EBIT $59.294B × (1 − 14.57% TTM effective tax rate)] ÷ latest-quarter Invested Capital $103.776B); **FCF-positivity cap applies** (not FCF-positive 3 consecutive years) | **40.0 (capped; would be 100.0 uncapped)** |
| Margins (15%) | GrossMargin_Score (TTM Gross Margin 72.57%); no structural-trend bonus applicable (already far above the 40% bonus-eligibility ceiling) | **90.7** |
| Growth (20%) | Growth_Score raw 26.8 (Revenue 3yr CAGR 6.71%, unchanged); **+10 documented TAM/pricing-power modifier** (cited: 16 SCAs locking in ~$100B floor-price revenue at margins management states will exceed past cycle peaks, per Q3 FY2026 earnings call; the AI/HBM demand supercycle previously documented via the Micron-Anthropic deal, 06-22 session) | **36.9** |
| Balance Sheet (15%) | Net Debt/EBITDA -0.27x (net cash) | **100.0 (capped)** |
| Moat (15%) | 3 of 5 signals cited true: **Market share** (25.7% global DRAM revenue share, Q3 CY2025, third place, +3.7pp QoQ — [TrendForce](https://www.trendforce.com/presscenter/news/20251126-12802.html)); **Brand premium/pricing power** (SCA floor-price margin guarantees + realized 84.6% GAAP gross margin, a record); **Switching costs** (16 binding take-or-pay SCAs + the Anthropic technical co-design relationship for HBM/storage subsystems, 06-22 session). False: network effect, scale cost advantage (Samsung/SK Hynix cost-structure comparables remain unsourced, per the 06-20 gap) | **60.0** |
| FCF Quality (10%) | TTM FCF/NI = 51.86%. Fiscal-year cross-check: FY2024 15.55%, FY2025 19.53% — both <70%, 2 consecutive years, which would independently fire the FCF/NI hard disqualifier **except** for the documented growth-capex carve-out (FY2024 CapEx -$8.386B, FY2025 -$15.857B, Q3 FY2026 alone -$7.826B, Q4 FY2026 guidance ≈$10B — an explicit, escalating, management-guided capacity-expansion program for HBM/DRAM demand), so this specific hard disqualifier does **not** fire | **19.8** |

```
Quality Score = 40.0×0.25 + 90.7×0.15 + 36.9×0.20 + 100.0×0.15 + 60.0×0.15 + 19.8×0.10
              = 10.00 + 13.61 + 7.38 + 15.00 + 9.00 + 1.98
              = 57.0
```

**Quality Score = 57.0 / 100.0 — fails the 80.0+ gate, two independent ways at once** (same dual-failure pattern as CCL's addendum): the weighted score (57.0 < 80.0) *and* the **"not FCF-positive for 3+ consecutive years" hard disqualifier**, which fires unconditionally (no carve-out exists for this specific disqualifier) because FY2023's outright FCF loss (-$6.117B) is still inside the current FY2023-FY2025 trailing window. This is the same structural fact that has anchored every MU Phase 01 FAIL since 06-20 — it does not resolve until FY2026 closes and is filed (≈Aug/Oct 2026). No Composite Score computed (requires clearing the gate first).

## 6. Outcome and files touched

- **Outcome:** Quality Score Engine addendum appended to the existing watchlist entry, plus the Rule 9/data-propagation check results. One Phase 01 criterion (EV/EBIT) flipped from FAIL to PASS, but the gate's overall verdict did not flip (3 of 8 still fail) — so no fuller Phase 01 re-check and no new dated watchlist file, per the task's branching instruction.
- **Files modified:**
  - `watchlist/not-in-portfolio/MU/MU-2026-06-20.md` — appended the Rule 9/data-propagation check and the Quality Score Engine addendum; added a Glossary section.
  - `framework/glossary.md` — added 2 new terms used in this session: Strategic Customer Agreement (SCA), Take-or-pay.
  - `sessions/2026-07-10-new-position-mu.md` — this file.
- **Not touched:** `watchlist/STALE.md` (MU was never listed there), no `git` commands run, no `decisions/` entry (no trade/action taken — MU remains not held, Phase 01 FAIL stands).

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file — all terms used above (CAGR, EBIT/EBITDA, Effective tax rate, EV/EBIT, FCF/NI conversion ratio, GAAP, Hard disqualifier, Invested Capital, Moat, NOPAT, Quality Score, ROIC, RPO, Rule 0, Rule 9, TTM, and this session's 2 additions: Strategic Customer Agreement (SCA), Take-or-pay) are defined there.

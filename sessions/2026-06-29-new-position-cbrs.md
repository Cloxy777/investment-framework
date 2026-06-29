# NEW POSITION RECHECK — CBRS (Cerebras Systems Inc., Class A)

**Task type:** NEW POSITION (recheck, not a from-scratch re-evaluation)
**Date:** 2026-06-29
**Prior session:** [2026-06-24-new-position-cbrs.md](2026-06-24-new-position-cbrs.md) (Phase 01 FAIL — 1 of 8 criteria pass; PASS/do-not-enter)
**Current portfolio weight:** 0% (not held — absent from [holdings.md](../portfolio/holdings.md); unchanged, not touched in this session)

---

## 0. Why this session exists

This is a **5-day recheck**, not a new trigger-driven evaluation. The prior session (2026-06-24) closed with a documented "Next Review Trigger" (quoted in full in §4 below). This session exists only to confirm whether any of those triggers — or any other Rule 9 fundamental event — fired in the 2026-06-24 → 2026-06-29 window. Per the task brief, this is proportionate to a recheck: the live price is re-pulled (Rule 0) and each Rule 9 category is explicitly checked, but the Phase 01 numbers are not re-derived from scratch — only reconfirmed against anything new.

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$187.00** | IBKR `get_price_snapshot`, contract_id 882732191 (NASDAQ: CBRS, Cerebras Systems Inc. Class A — same contract resolved in the 06-24 session), ts 1782715815 (2026-06-29, live quote, `is_close: false`) |
| Change vs prior close | **+2.98%** (+$5.41) | IBKR `change`/`change_pct`; prior close $181.59 |
| Bid / Ask | $186.57 / $186.99 | IBKR `bid_ask` |
| 52-week range (cached) | $160.81 (low) – $386.34 (high) | IBKR `misc_statistics` |

**Price path since the 06-24 session (for Rule 9 context, not re-scored):** $195.51 (06-24 live print, itself already a new 52w low at the time) → stock continued falling, setting an **all-time/52-week low of $160.81 on 2026-06-26** (per WebSearch cross-check of Yahoo Finance/StockAnalysis/Investing.com coverage) → partial recovery to a $181.59 close on 06-28 → **$187.00 live now (06-29)**. The 52-week-low field itself moved from $196.73 (recorded 06-24) to $160.81 (now), confirming the stock traded materially lower over this window before rebounding. This entire move is continued market digestion of the **same** 2026-06-23 earnings/guidance event already fully captured in the 06-24 session (revenue beat / EPS miss / FY2026 core operating margin guided to −28%/−32%) — see §3 below for why this does not constitute a *new* Rule 9 trigger.

## 2. Phase 01 status — unchanged, not re-derived

No new quarterly filing, 10-Q propagation into yfinance, or other primary disclosure has appeared since 06-24. Per the task scope, the 8-criterion Phase 01 table from the 06-24 session is **not re-run from scratch** — there is no new data that would change any of the eight inputs (gross margin 39.03%, normalized net margin ≈ −24.6%, ROIC undefined, revenue 3yr CAGR 174.6%, FCF negative in 3 of last 4 fiscal years, Net Debt/EBITDA undefined, FCF yield −0.91%/−0.93%, EV/EBIT mechanically negative). **Result stands: 1 of 8 PASS, 7 of 8 FAIL — Phase 01 Quality Gate FAIL.** No Phase 02 valuation score applies; no order setup applies.

## 3. Rule 9 Trigger Check — 2026-06-24 → 2026-06-29 (per fair-value-methodology.md §"Rule 9 — Model Refresh Triggers")

| Trigger category | Checked? | Finding |
|---|---|---|
| **Quarterly earnings release** | Yes | None due in this window. CBRS reported Q1 2026 on 2026-06-23, one day *before* the prior session — already fully captured there. No new earnings release occurred 06-24→06-29. Next quarterly date not yet disclosed in yfinance's calendar (per 06-24 session's note). |
| **Guidance revision (up or down)** | Yes | No new guidance issued in this window. The FY2026 core operating margin guide of −28%/−32% is the same guidance disclosed 2026-06-23 and already reflected in the 06-24 session's recommendation — not a new revision. |
| **Management change** | Yes | WebSearch found no CEO/CFO/board change announced for Cerebras in June 2026. Andrew Feldman remains CEO; the most recent board appointments found (Lantzsch, Dorchak, Auvil) predate this window by well over a year. No management-change trigger. |
| **Material M&A announcement** | Yes | No new M&A found. The OpenAI (~$20B, 750MW multi-year) and AWS partnership figures appearing in current search results are the **same 2026-06-23 earnings-release disclosures** already cited in the 06-24 session (§6 there) — re-circulating in press coverage, not a new incremental announcement. No primary-sourced *quantified update* beyond what was already captured. |
| **Macro shift (central bank policy, commodity price shock)** | Yes | 10Y US Treasury yield: ~4.37% (FRED `DGS10`, most recent available print, 2026-06-26) vs. 4.50% recorded 2026-06-24 — a ~0.13pp drift, consistent with ordinary day-to-day movement, not a central bank policy action or commodity shock. No macro-shift trigger; would not change the Rate Regime Modifier bracket (3.5–5%) even if Phase 02 were reached. |
| **>15% stock-price move without a fundamental trigger** | Yes | The stock did move >15% intraday/multi-day within this window (from $195.51 on 06-24 down to an all-time low of $160.81 on 06-26, before recovering to $187.00 now). **This move has an identified fundamental cause** — it is the market continuing to digest the same 2026-06-23 earnings/guidance print already captured 06-24 (a post-earnings "whipsaw," per contemporaneous coverage of an EPS-miss-driven selloff). Rule 9's >15% trigger is specifically for moves *without* an identified cause; this one has one, and it is not a new one. No trigger. |

**Conclusion: no Rule 9 trigger fired in this window.** All six categories checked explicitly; none independently warrant a re-valuation beyond what 06-24 already captured.

## 4. Next Review Trigger — unchanged, restated from 06-24

Carried forward verbatim (no change warranted):
- Any quarter where CBRS reports a positive EBIT/EBITDA and guidance turns toward operating-margin improvement rather than the −28%/−32% deterioration just guided for FY2026 (mandatory Rule 9 re-check regardless of outcome) — CBRS's first 10-Q propagating into yfinance's quarterly tables would also unlock a cleaner post-IPO TTM recompute.
- CBRS's next quarterly earnings release — date not yet disclosed.
- Any primary-sourced, quantified update on the OpenAI/AWS partnership economics that materially changes the trailing or near-term EBIT/FCF picture (assessed at that time, but could not alone override a Phase 01 failure built on negative absolute profitability — only a realized EBIT/FCF improvement could).
- Sufficient public trading history (5+ years) for the 5yr historical-PE range and Turnaround Sub-Gate's historical-ROIC lookback to become computable — not expected before 2031.

## 5. Recommendation

**PASS — unchanged.** Phase 01 Quality Gate still FAIL (1 of 8 criteria). No Rule 9 trigger fired in the 2026-06-24 → 2026-06-29 window; the post-earnings price volatility (down to a $160.81 low, back up to $187.00) is continued digestion of the same already-captured 2026-06-23 print, not a new fundamental event. No new dated watchlist file is created per `watchlist/README.md`'s "significant change" convention (score/status/action unchanged, no Rule 9 trigger, position not opened/closed) — a "Last checked (no significant change)" line is appended to the existing [CBRS-2026-06-24.md](../watchlist/not-in-portfolio/CBRS/CBRS-2026-06-24.md) entry instead.

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **EV/EBIT** | Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to their operating profit, independent of capital structure. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF Yield** | Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper; negative means the business is consuming cash relative to its market value. |
| **M&A** | Mergers & Acquisitions — one company buying or combining with another. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; undefined/not meaningful when EBITDA is itself negative. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; undefined/not meaningful when both NOPAT and invested capital are negative. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results — still not computable for CBRS; no post-IPO quarterly data has propagated into yfinance as of this recheck. |
| **Turnaround Sub-Gate** | The conditional path (Hybrid Upgrade 4) that lets a company failing 2–4 quality criteria still enter as a small (2–3%) position if it passes 5 specific tests. Not reachable here — CBRS fails 7 of 8 criteria, outside the eligibility window. |

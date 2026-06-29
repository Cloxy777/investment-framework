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

## 6. Quality Score Addendum (2026-06-29 Methodology Update)

**Why this section exists:** the framework's [Quality Score Engine](../framework/quality-scoring.md) (a continuous 0–100.0 grade plus a strict **80.0+ gate** for Phase 02 eligibility) and the [Composite Score](../framework/valuation-scoring.md) were added on 2026-06-29, the same day as this recheck. This addendum applies the new methodology to the underlying data already gathered in the original [2026-06-24 session](2026-06-24-new-position-cbrs.md) — confirmed still current per §2/§3 above (no new filing has appeared) — **no new financial data was fetched.**

### Hard disqualifier check (per quality-scoring.md — fails regardless of weighted score)

| Hard disqualifier | Applies to CBRS? | Basis |
|---|---|---|
| FCF/NI <70% for 2+ consecutive years, no growth-capex carve-out | Not mechanically meaningful, but substantively yes | FCF/NI is not a clean ratio in any year on record — FY2025's literal computation (FCF −$392.8M ÷ normalized NI −$125.5M ≈ +313%) is two negatives producing a misleadingly *high*-looking ratio; FY2024 (FCF +$428.5M ÷ NI −$481.6M) mixes opposite signs entirely. A clean, sustained >70% conversion of positive earnings into cash has never occurred. Not relied upon as the primary citation since the literal ratio breaks down; see the unambiguous disqualifier below instead. |
| Net Debt/EBITDA over threshold (2.5× standard / 4× asset-light) | **No, in substance** (mechanically undefined) | Net debt is *negative* (net cash $846.4M) and EBITDA is also negative (−$110.8M); the literal negative-over-negative arithmetic (+7.64×) would mechanically read as severe over-leverage, but the true balance-sheet substance is a debt-light, net-cash position — see judgment call in the Balance Sheet sub-score below. |
| Not FCF-positive for 3+ consecutive years | **Yes — fires** | FCF negative in 3 of the last 4 fiscal years (FY2022 −$174.9M, FY2023 −$85.6M, FY2025 −$392.8M); only FY2024 (+$428.5M) was positive, surrounded by negative years on both sides. Never three consecutive positive years. |

**Hard disqualifier #3 fires, unambiguously and independently of the weighted score below.**

### Weighted Quality Score

| Sub-score (weight) | Inputs (from the 2026-06-24 session) | Calculation | Result |
|---|---|---|---|
| **Profitability** (25%) | Net margin −24.6% (FY2025, normalized excl. one-off gain); ROIC undefined (NOPAT −$114.8M and Invested Capital −$316.8M both negative) | NetMargin_Component = clamp((−24.6/30)×100) = 0.0. ROIC_Component: the literal negative÷negative arithmetic has no economically meaningful sign — **judgment call:** scored 0.0, since negative operating profit funded by negative invested capital is a quality-negative condition, not a basis for a positive score. Avg | **0.0** |
| **Margins** (15%) | Gross margin 39.03% (FY2025); 3yr trend computed from the FY2022–FY2025 revenue/gross-profit figures in the original session: 11.79% (FY22) → 33.55% (FY23) → 42.27% (FY24) → 39.04% (FY25) | clamp((39.03/80)×100) = 48.8; **+10** structural-expansion bonus (margin is below 40% *and* the multi-year trend is a clear, large expansion despite the FY24→FY25 pullback) | **58.8** |
| **Growth** (20%) | Revenue 3yr CAGR 174.6% (FY2022→FY2025, pre-IPO basis, off a small base — flagged in the original session as not a public-market-disciplined track record) | clamp((174.6/25)×100) = 698.4 → capped | **100.0** |
| **Balance Sheet** (15%) | Net Debt/EBITDA mechanically undefined (negative/negative) | The literal arithmetic (+7.64×) would score 0.0 — mechanically misleading, since it would treat a debt-light, **net-cash** company as severely over-levered. **Judgment call:** scored 100.0, reflecting the true substance ($846.4M net cash, no leverage risk) | **100.0** (override; mechanical formula would read 0.0) |
| **Moat** (15%) | "Largest semiconductor IPO ever," OpenAI/AWS partnerships valued >$20B combined, customer-concentration risk flagged | 0 of 5 signals cited true: the partnership/IPO facts are scale and demand-pipeline evidence, not cited market-share, pricing-power, network-effect, switching-cost, or cost-per-unit data | **0.0** |
| **FCF Quality** (10%) | FCF/NI FY2025 literal ratio ≈+313% (FCF −$392.8M ÷ normalized NI −$125.5M) | The literal ratio would clamp to a perfect 100.0 — mechanically misleading, since it would score CBRS's *worst* cash-burn year as flawless conversion. **Judgment call:** scored 0.0, reflecting true, severe, recurring cash burn (negative FCF in 3 of the last 4 fiscal years) | **0.0** (override; mechanical formula would read 100.0) |

```
Quality Score = 0.0×0.25 + 58.8×0.15 + 100.0×0.20 + 100.0×0.15 + 0.0×0.15 + 0.0×0.10
              = 0.00 + 8.82 + 20.00 + 15.00 + 0.00 + 0.00
              = 43.8
```

**Quality Score: 43.8 — fails the 80.0+ gate**, independently confirmed by hard disqualifier #3 (never FCF-positive 3+ consecutive years). Two sub-scores above (Balance Sheet, FCF Quality) required an explicit, documented judgment call overriding a mechanically-computed ratio that a literal negative-over-negative calculation would otherwise render nonsensical or actively misleading — both overrides are disclosed here rather than silently applied, per this framework's "no black-box outputs" rule. Per quality-scoring.md, **no Composite Score is computed** for a company that fails the Quality Gate. This does not change the Phase 01 FAIL / do-not-enter recommendation already reached above and in the 2026-06-24 original session.

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **Composite Score** | `0.50×(100−Quality Score) + 0.50×Valuation Score` — combines quality and cheapness into one number, computed only for companies that clear the 80.0+ Quality Score gate. Not computed for CBRS (gate fails). |
| **Hard disqualifier** | One of three quality-gate conditions (FCF/NI conversion, Net Debt/EBITDA, FCF positivity) that fails a company outright regardless of its weighted Quality Score. CBRS fails the "FCF-positive for 3+ consecutive years" disqualifier. |
| **Quality Score** | A 0–100.0 grade (0 = lowest quality, 100 = highest) blending profitability, margins, growth, balance sheet, moat, and FCF quality into one number; a company must score ≥80.0 to be eligible for Phase 02 valuation scoring at all. CBRS scores 43.8. |
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

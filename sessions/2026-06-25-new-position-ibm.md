# New Position Evaluation — IBM (International Business Machines Corporation)

**Task type:** NEW POSITION
**Date:** 2026-06-25
**10Y US Treasury yield:** 4.412% (2026-06-25; via yfinance `^TNX`)
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — `t.me/tarasguk`, post #11199, 2026-06-25 12:18:52 UTC, re: IBM unveiling a "nanostack" 0.7nm chip prototype — claimed first sub-1nm chip technology, ~100B transistors on a nail-sized chip, up to 70% better energy efficiency vs. 2nm — with the post itself noting this is **only a mockup/prototype**, with mass production approximately 5 years out per IBM's own statement. This is **explicitly not a Rule 9 fundamental-event trigger** — it is an R&D/lab-prototype announcement, not earnings/guidance/M&A/management-change/macro news, and by IBM's own timeline it is not expected to affect revenue or margins for ~5 years. The post text is used only as the reason to look at the ticker; no information from it is used as financial data anywhere below. IBM has no prior watchlist or session history in this repo — per established precedent (FDX, CCL, CVX, MCD, NOK: first mention of an untracked name gets a full normal evaluation regardless of how thin/speculative the trigger is), this proceeds as a standard `/new-position` run.

IBM is **not** a current holding (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)).

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first, before any valuation work, and cross-checked across two independent sources.

| Source | Price | Timestamp |
|---|---|---|
| **IBKR live snapshot** (primary, contract_id 8314, NYSE, "INTL BUSINESS MACHINES CORP") | **$270.93** | 2026-06-25 12:36:36 UTC (snapshot ts 1782390996) |
| yfinance — prior session close (2026-06-24, cross-check only) | $262.96 | close 2026-06-24 |

**Cross-check note (a deliberate, documented discrepancy — not an error):** yfinance's `t.info["currentPrice"]`/`["regularMarketPrice"]` returned $262.96, which on inspection matches the 2026-06-24 daily-bar close from `t.history()` exactly (Close $262.959991) — i.e. yfinance's "current price" field is serving a **cached prior-session close**, not a live intraday quote, consistent with the curl_cffi-unavailable fallback warning yfinance raised this session. IBKR's snapshot carries today's date/time (2026-06-25 12:36:36 UTC), an explicit `change_pct` of **+3.03%** on the day, and a live bid/ask ($270.80 / $271.00) — all hallmarks of a genuine live quote, consistent with the day's news (the nanostack announcement) moving the stock. Per Rule 0 and the SPGI lesson (never infer or default to a stale number when a live source is available and they disagree), **IBKR's $270.93 is used throughout this session** as the live price; yfinance's historical daily bars (not its `.info` current-price field) are used for all trailing-financials work below, where they are reliable.

52-week range (IBKR `misc_statistics`): low **$212.35** / high **$332.41** — IBM is trading roughly 27.6% above its 52-week low and ~18.5% below its 52-week high. 52-week open: $289.78 (IBM is down ~6.5% over the trailing 52 weeks despite today's pop). Year-to-date change: **−8.01%** ($-23.58). Dividend yield at live price: 2.56%.

Analyst consensus (yfinance, 21 analysts): mean target **$293.89**, median **$291.00**, high **$390.00**, low **$195.00**, consensus rating **"buy"** — noted here per Rule 0 Step 4 as a bull-case sanity check; not used as an input to any score below.

**Live price used throughout this session: $270.93.**

---

## 2. Data Gaps Flagged / Data-Source Note

`yfinance` required `YF_DISABLE_CURL_CFFI=1` and `CURL_CA_BUNDLE=/root/.ccr/ca-bundle.crt` to run without network errors (per prior-session precedent) — once set, it worked normally for all trailing financial statements, the 5-year PE reconstruction, and `^TNX`. The only caveat is the `.info` current-price fields described in Section 1 above, which were **not** used as the live price.

**One data-depth limit, noted but not a blocker:** annual statements (`t.financials`/`t.cashflow`/`t.balance_sheet`) return only FY2022–FY2025 (4 fiscal years); FY2021 is `NaN` across all three statements. This caps the trailing CAGR/ROIC/margin lookback at 4 years (FY2022 base) rather than 5. This does not block Phase 01 (which requires only 3+ years of history) — and as shown below, the available years already produce a decisive, multiply-corroborated Phase 01 FAIL, so an FY2021 data point would not plausibly change the outcome. **No required Phase 01 metric is missing or estimated; all figures below are cited to yfinance's structured statement data or the IBKR live snapshot.**

The 5-year trailing-PE reconstruction (`get_earnings_dates`, see Section 4) returned 46 usable TTM-EPS quarters back to 2020, comfortably covering the required 20-quarter (5yr) window with no fallback needed.

---

## 3. Phase 01 — Universe Screening (Quality Gate)

The framework carries two slightly different Phase 01 threshold sets — [strategy.md](../framework/strategy.md)'s (stricter) and [valuation-scoring.md](../framework/valuation-scoring.md)'s "Quantitative Pre-Screen Filters" (looser on most lines). Both are shown below for completeness; IBM fails decisively under **either** version.

All financial figures sourced from yfinance `t.financials` / `t.cashflow` / `t.balance_sheet` (USD, annual, fiscal years ending 31 Dec), cross-tabulated below FY2022–FY2025 (4 years — see Section 2 data-depth note).

| Criterion | strategy.md threshold | valuation-scoring.md threshold | IBM actual | Result |
|---|---|---|---|---|
| Net margin | >15% | >12% | **15.68%(FY25) / 9.60%(FY24) / 12.13%(FY23) / 2.71%(FY22)** — only the most recent year clears either bar; 3 of 4 years fail strategy.md's >15%, and FY24/FY22 fail even the looser >12% | **FAIL (strategy.md); mixed/mostly-fail (valuation-scoring.md)** |
| **ROIC** | **>15%** | **>15%** | **13.36%(FY25) / 9.47%(FY24) / 11.26%(FY23) / 5.02%(FY22)** — NOPAT = EBIT×(1−effective tax rate), Invested Capital from balance sheet. Never reaches 15% in any of the 4 available years, even in the best (FY25) year | **FAIL (both)** |
| Gross margin | >40% OR structurally expanding | >40% | 58.19%(25) / 56.65%(24) / 55.45%(23) / 54.00%(22) — clears >40% every year, and is on a genuine multi-year expansion trend (+4.2pp over 3 years) | PASS (both) |
| FCF positive | 3+ yrs | 3 consecutive yrs | $11.46B(25) / $11.76B(24) / $12.12B(23) / $8.46B(22) — positive all 4 years | PASS (both) |
| **Revenue growth** | **CAGR >10%** | **CAGR >8% (3yr)** | **3yr CAGR (FY22→FY25) = 3.72%** — Revenue: $60.53B(22) → $61.86B(23) → $62.75B(24) → $67.54B(25) | **FAIL (both)** |
| **Net debt/EBITDA** | **<2×** | **<2.5×** | **2.95×(25) / 3.65×(24) / 3.19×(23) / 6.43×(22) — every year fails both thresholds; FY22's 6.43× was driven by a depressed EBITDA base ($7.17B), but even the best year (FY25, 2.95×) misses the stricter <2× by 48% and the looser <2.5× by 18%** | **FAIL (both, every year)** |
| FCF/NI conversion | >70% for 2+ yrs | (same check, implicit in "FCF positive 3yr") | 108.1%(25) / 195.3%(24) / 161.6%(23) / 516.0%(22) — passes comfortably, though the >100% readings (especially FY22's 516%) reflect FCF running well ahead of a depressed Net Income denominator rather than unusually strong incremental cash conversion | PASS (both), though on a denominator distorted by FY22's weak NI base |
| FCF yield (live price basis) | (not separately gated) | **>4%** | FY25 FCF $11.46B ÷ live market cap $254.64B = **4.50%** | PASS (valuation-scoring.md leg) |
| EV/EBIT (live price basis) | (not separately gated) | **<20×** | Live EV $312.66B ÷ FY25 EBIT $12.26B = **25.50×** | **FAIL (valuation-scoring.md leg)** |
| **Dilutive share issuance pattern** | **none** | **none** | **Shares outstanding (Ordinary Shares Number) rose every year: 906.1M(22) → 915.0M(23) → 926.3M(24) → 937.0M(25), +3.4% over 3 years.** Cash-flow detail: buybacks ($407M/22, $402M/23, $651M/24, $1,018M/25) were smaller than new stock issuance in 2 of 4 years (Issuance of Capital Stock: $279M/22, $414M/23, $745M/24, $710M/25) and "Net Common Stock Issuance" was net-dilutive or roughly flat in 3 of 4 years. **This is a mild net dilution pattern, not a buyback program.** | **FAIL (both)** |
| Moat signal | stable/growing share, brand, network effect | (qualitative, same) | IBM retains a real enterprise-software/mainframe/consulting moat (high switching costs, deep legacy-system entrenchment, Red Hat hybrid-cloud platform) — see qualitative notes below | PASS (qualitative), does not offset the quantitative failures |

### Result: **Phase 01 FAIL**

IBM fails on **three independent, structural criteria** under both threshold sets carried in this framework, plus net margin under the stricter strategy.md threshold:

1. **ROIC.** 13.36% in the best available year (FY2025) and never above that across the 4-year lookback — consistently below the >15% bar this framework treats as the core quality threshold for capital efficiency. The trend (FY22→FY25: 5.02% → 11.26% → 9.47% → 13.36%) is directionally improving but not monotonic, and has not yet cleared the bar in any year shown.

2. **Revenue growth.** 3-year revenue CAGR of **3.72%** is well below both the looser (>8%) and stricter (>10%) thresholds. This is consistent with IBM's well-known profile as a mature, large-cap technology/services company growing in the low-single-digits — closer to MCD's "mature slow grower" Phase 01 profile (5.06% CAGR, also a FAIL) than to a quality-and-growth compounder.

3. **Net debt/EBITDA.** Persistently elevated at **2.95×–6.43×** across all 4 available years — never close to either the strict <2× or the relaxed <2.5× threshold. IBM does not qualify for Hybrid Upgrade 5's asset-light-financial 4× exception (it is an enterprise hardware/software/services hybrid, not a payment network or financial company) — and even if it did, its interest coverage (EBIT ÷ interest expense = $12.26B ÷ $1.935B = **6.34×**, FY25) is far below the >15× the exception requires, so the exception would not apply on either prong even hypothetically.

4. **Dilutive share issuance pattern.** Shares outstanding rose every year FY2022→FY2025 (+3.4% cumulative) — IBM is a net *issuer*, not a net repurchaser, over this window. Buybacks exist but have been smaller than new issuance (stock comp, etc.) in most years.

5. **Net margin** also fails strategy.md's stricter >15% bar in 3 of the last 4 years (only FY2025's 15.68% clears it) — though it does pass valuation-scoring.md's looser >12% bar in that same year and is on a clear improving trend.

**Earnings-quality cross-check (per this evaluation's specific brief — see graveyard-audit.md Case 7):** the historical IBM failure pattern (2012–2018) was *"EPS growing while revenue flat/declining,"* with buybacks identified as the masking mechanism. Checking that pattern directly against current data:

- **Revenue is not flat or declining** — it grew every year FY2022→FY2025 ($60.53B → $61.86B → $62.75B → $67.54B), a 3.72% CAGR. This is slow, but it is **not** the 2012–2018 pattern of outright multi-year revenue contraction.
- **However, a real EPS/revenue divergence still exists and is large:** Diluted EPS grew from $1.80(22) to $11.17(25) — an **83.76% 3yr CAGR**, more than 22× the revenue CAGR. This is **not** buyback-driven in the way the 2012–2018 case was (shares outstanding *rose*, not fell, over the same period — see the dilution finding above). Instead, it is driven by **margin/net-income recovery off a severely depressed FY2022 base**: FY2022 net margin was just 2.71% (net income $1.64B on $60.53B revenue) against FY2025's 15.68% ($10.59B on $67.54B) — a ~13pp margin recovery that mechanically produces a large EPS CAGR even with modest revenue growth and a flat-to-slightly-rising share count. Whether this margin recovery is durable (cost discipline, mix shift toward higher-margin software/Red Hat) or partly cyclical/one-off is a qualitative question this session does not have the data to resolve definitively — but the mechanism is fundamentally different from (and arguably more legitimate than) the 2012-2018 buyback-masking pattern, since it reflects an actual change in reported operating profitability, not EPS engineering via a shrinking share count. **This is flagged for the record, consistent with the brief's instruction to scrutinize the EPS-vs-revenue trend, but it is not by itself a reason to override the Phase 01 FAIL already driven by ROIC, revenue growth, and leverage above.**

Per [new-position.md](../.claude/commands/new-position.md) step 2 and [operating-brief.md](../framework/operating-brief.md): **"if it fails, stop and report why rather than proceeding to scoring."** Accordingly, **no Rate Environment Gate and no Phase 02 valuation score were computed.**

This is not a verdict on the nanostack chip announcement's long-term technical or strategic significance — IBM's claimed sub-1nm prototype, if it holds up and eventually reaches production (by IBM's own estimate, ~5 years away), could be a genuinely important R&D milestone for the semiconductor industry. But this framework scores **trailing, filed financials** at the Phase 01 gate, deliberately before any narrative or forward-looking story is allowed to influence the assessment (Rule 0 / "never invent or estimate," and a 5-year-out production timeline is several review cycles beyond even this framework's most generous 18–24 month catalyst-window guardrail for the Upside/Downside Modifier — which is itself a *Phase 02* tool never reached here). On the numbers that exist today, IBM is a low-growth, sub-hurdle-ROIC, persistently over-levered technology/services company with a real but narrow margin-recovery story — not a quality compounder by this framework's Phase 01 definition.

---

## 4. Recommendation

**PASS.** Do not open a position. No order setup, no fair-value derivation, no position sizing — none of that work is meaningful for a name that fails the quality gate this framework uses to define its investable universe, and doing it anyway would be exactly the "black-box theater" the MCD/NOK precedents explicitly declined to produce.

**Worth flagging for context (not a basis for any action):** Hybrid Upgrade 4 (Turnaround Sub-Gate) exists in this framework for exactly this kind of previously-stumbling, still-moated business, but it requires **all five** of: (1) historical ROIC >15% for ≥5 of the past 10 years (data only goes back to FY2022 in this session and never clears 15% in any available year — fails outright on available evidence), (2) verified CEO/CFO insider buying >$500K in the past 6 months (not checked — moot given condition 1 already fails on available data), (3) an independent FV estimate showing ≥40% margin of safety (not computed — Phase 01 FAIL means no FV work was done), (4) Net Debt/EBITDA <3× (IBM's FY25 figure of 2.95× would pass this specific leg, the only one of the five it would clear), (5) a still-identifiable core moat (yes — enterprise switching costs, mainframe/z-platform lock-in, Red Hat hybrid-cloud positioning). Condition 1 alone (and the broader 10-year data gap) is enough to disqualify the Turnaround path without needing to verify the rest — flagged here as context, not as "almost qualifying."

### 5 Qualitative Questions (per valuation-scoring.md, for context — does not override the quantitative FAIL)

1. **Why are margins high (where they are)?** IBM's gross margin (58.19% FY25) reflects a genuine mix shift toward higher-margin software (Red Hat, automation, data/AI) and consulting away from commodity hardware — a real structural driver, not solely pricing power on a single product.
2. **What would it take to compete with them?** High switching costs in mainframe (z-platform) and entrenched enterprise software are real and durable; cloud/AI infrastructure competition (AWS, Microsoft Azure, Google Cloud) is a genuine and growing threat outside IBM's legacy strongholds.
3. **Capital allocation track record (5–10yr)?** Not fully assessable from the 4-year window available this session; visible behavior in this window is a mix of modest buybacks, a sustained (and growing) dividend, and continued new-share issuance (net dilutive) — not a clean "shareholder-friendly buyback machine" picture.
4. **Where is growth coming from next 3–5 years?** Hybrid cloud (Red Hat), AI/data platforms (watsonx), and consulting — management's own narrative; not independently verified against filed financials in this session per Rule 0.
5. **Best bear case?** The 2012–2018 historical pattern (graveyard-audit.md Case 7) is the standing bear case for this exact name: a legendary-moat enterprise incumbent slowly displaced by a platform shift (then: cloud vs. on-premise; now, potentially: AI-native/cloud-native competitors), with revenue growth structurally capped in the low single digits even when margins recover. Today's data shows revenue growth still capped at 3.72% CAGR and ROIC still below the quality threshold even after 3 years of margin recovery — the underlying growth problem from Case 7 has not been solved, even though the specific EPS-masking mechanism (buybacks shrinking share count) is not currently present.
6. **Disruption vector check:** Generative-AI-driven enterprise software/consulting disintermediation is a plausible 5-year disruption vector for IBM's consulting and integration revenue specifically; the nanostack chip prototype is R&D-stage and, per IBM's own ~5-year production timeline, is not a near-term mitigant either way.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Routine re-screen:** not scheduled — Phase 01 FAILs are not put on a recurring re-check cadence by default (see [watchlist/README.md](../watchlist/README.md): "Phase 01 FAIL / not scored" entries don't carry a numeric score to go stale).
- **Rule 9 fundamental trigger** that would warrant a fresh look regardless of schedule: a quarterly earnings print showing a *sustained* re-acceleration of revenue growth (3yr CAGR moving durably above 8–10%) combined with ROIC clearing 15% and a credible deleveraging path (Net Debt/EBITDA toward 2–2.5×) — or a reversal of the net-issuance pattern into genuine, sustained net buybacks. A material M&A announcement or management change would also qualify under Rule 9 independent of the financials. If the nanostack chip program advances meaningfully faster than IBM's own stated ~5-year timeline (e.g. a credible near-term commercialization announcement), that would also warrant a fresh look, though nothing in today's post suggests that. Absent one of these, future Telegram mentions of IBM should be treated as routine "last checked, no change" pings rather than triggering a full re-evaluation each time, consistent with the MCD/NOK precedent.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and valuation ratios.
- **EPS** — Earnings Per Share — net income divided by number of shares outstanding.
- **EV** — Enterprise Value — a company's total value to all capital providers: market cap + debt − cash.
- **EV/EBIT** — Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to operating profit, independent of capital structure.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **Forward PE** — Price ÷ next twelve months' expected earnings per share.
- **Interest coverage (ratio)** — EBIT ÷ interest expense — how many times over a company could pay its interest bill from operating profit; higher means less balance-sheet risk from debt.
- **Investment grade** — A credit rating (BBB-/Baa3 or higher) signaling a low perceived risk of default.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
- **NI (Net Income)** — accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — operating profit after a tax adjustment but before financing costs; the numerator this framework uses to compute ROIC.
- **PE (Price-to-Earnings) ratio** — Share price ÷ earnings per share — the most common "how expensive is this stock" multiple.
- **Phase 01–06** — the six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **PT (Price Target)** — an analyst's forecast of where a stock's price will be at a future date.
- **Qualified Quality List** — the output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. (IBM does not make this list.)
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9** — this framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — the interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure.
- **Turnaround Sub-Gate** — the conditional path (Hybrid Upgrade 4) that lets a company failing some quality criteria still enter as a small (2–3%) position if it passes 5 specific tests (historical ROIC, insider buying, margin of safety, debt level, identifiable moat).

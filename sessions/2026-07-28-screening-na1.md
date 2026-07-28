# 2026-07-28 — SCREENING: North America — NA-1 (Tech, Communication Services, Consumer Discretionary)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [NA-1](../framework/screening-coverage-log.md) (North America: US + Canada; sector emphasis Tech, Communication Services, Consumer Discretionary). Selected per the rotation rule: **2026-07-07 was the oldest "Last screened" date** on the matrix (all five other rows carry 2026-07-11 or later).

This was run as an **unattended scheduled routine** ("Monthly Universe Screening Slice," first Saturday of the month — markets closed) with no interactive user present. This is a **re-screen of a previously-covered slice**, three weeks after its last pass ([2026-07-07 session](2026-07-07-screening-na1.md)) — the point of the rotation cadence is to catch ETF-composition churn and valuation moves, not just cover new ground.

---

## 0. Methodology

No interactive TIKR/Koyfin screener export was available — there was no user to ask, so per Step 0's documented unattended-session exception, this session went straight to the ETF-holdings fallback.

- **EODHD was NOT used**, despite this run's task prompt again referencing an `EODHD_API_KEY` set in the environment and calling this the "Monthly Universe Screening Slice... for full automation (Path A)." That path was deprecated and removed from the framework on 2026-06-19 ([decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)), which explicitly says to treat that credential as compromised if it's ever needed again. The canonical [screen.md](../.claude/commands/screen.md) and [automation-schedule.md](../framework/automation-schedule.md) have no EODHD path, and automation-schedule.md documents this routine as twice-weekly, not monthly. This is at least the fourth consecutive rotation session (after [2026-06-30 Japan](2026-06-30-screening-japan.md), [2026-07-04 NA-2](2026-07-04-screening-na2.md), and [2026-07-07 NA-1](2026-07-07-screening-na1.md)) to hit this identical stale-prompt mismatch. CLAUDE.md instructs treating `framework/` as the source of truth over a stale prompt, so that's what this session did.
- **`yfinance`/direct Yahoo access was attempted first** (the framework's documented standard per-candidate source) and again failed with the same TLS/connection-reset error (`curl: (35) Recv failure: Connection reset by peer`) seen in every rotation session since 2026-07-07 — a persistent network-level block in this environment, not a rate limit.
- **Fell back to `stockanalysis.com`**, same precedent as every recent rotation session. Confirmed reachable (HTTP 200) before proceeding. Pulled three pages per candidate this round — `/stocks/<ticker>/financials/` (Gross Margin, Net Margin, Revenue history), `/stocks/<ticker>/financials/ratios/` (ROIC proxy via Return on Capital Employed, EV/EBIT, Net Debt/EBITDA, FCF Yield — all TTM/current-price basis), and `/stocks/<ticker>/financials/cash-flow-statement/` (Free Cash Flow history, for the 3-consecutive-year positivity check) — fetched directly via scripted HTTP requests (not a browser tool) and parsed from the page's embedded data tables.
- **Starting universe rebuilt from fresh ETF holdings** (MOAT, QUAL, QGRW top-25 each, pulled fresh via `stockanalysis.com/etf/<ticker>/holdings/`, current as of 2026-07-28). Composition has churned since the 2026-07-07 pass:
  - **New to the top-25 union this round:** BR, WMT (both re-entered top-25 lists), JNJ
  - **Dropped out of the top-25 union this round:** APP, QCOM (both were candidates in the 07-07 pass; no longer appear in any of the three ETFs' current top-25)

---

## 1. Deduplicated starting universe → structural triage (Step 1)

Combining the three fresh ETF lists gives **57 raw names** (same count as 07-07, different composition). After removing current portfolio holdings ([holdings.md](../portfolio/holdings.md): AMZN, AVGO, GOOG, GOOGL, META, MSFT, NFLX, NVDA, V, VEEV — 10 names present in this round's union, tracked via `/rescore` rather than re-discovered here), **47 candidates** remain.

Structural triage eliminated names on the same well-documented business-model grounds established in prior NA-1/NA-2 rotations (flagged transparently so any can be pulled back on request):

| Eliminated | Why (structural, not measured) |
|---|---|
| COST, ROST, TJX, **WMT** *(new this round)* | Large-volume retail — net margins structurally 2–6% |
| XOM | Integrated oil major — commodity-cyclical margins/revenue |
| MAS | Building products — mid-single-digit net margins, cyclical |
| MDLZ, KVUE, CLX, STZ, BF.B | Packaged consumer staples — low-single-digit revenue growth |
| BMY, MRK, **JNJ** *(new this round)* | Large pharma, well-documented patent-cliff cycles |
| DHR, ZBH, GEHC, OTIS | Industrials/medtech stalwarts — mid-teens margins, mid-single-digit growth |
| CAT, GE, GEV | Cyclical industrials |
| EL | Documented margin-compression/turnaround phase |
| LIN | Industrial gases — ~20% margins but historically mid-single-digit growth |
| MU | Memory semiconductor — margin-*stability* failure by category |
| SCHW | Broker-dealer — same thin-margin brokerage-model exclusion as LPLA (which fails the quantitative gate below) |

**25 names eliminated. 22 remain** for the real, sourced quantitative pull: **AAPL, ABNB, ADP, AMAT, AMD, ANET, BR, BRK.B, CSCO, DDOG, FICO, FTNT, KLAC, LLY, LPLA, LRCX, MA, MRVL, ORCL, PANW, PLTR, TYL**.

Of these, 20 were also survivors of the 2026-07-07 triage; **BR** re-enters as a new candidate (back in MOAT's top-25 this round — it was flagged as having "dropped out of the top-25" as of 07-07). **APP and QCOM**, both candidates on 07-07, no longer appear in any of the three ETFs' current top-25 and are not re-tested this round (not a judgment on the businesses — pure ETF-composition churn; either can be pulled back into a future pass on request or evaluated directly via `/new-position`).

---

## 2. Quantitative Phase 01 gate (real, sourced data — stockanalysis.com, 2026-07-28)

Filters per [valuation-scoring.md](../framework/valuation-scoring.md#quantitative-pre-screen-filters-phase-01): Gross margin >40%, Net margin >12%, ROIC >15%, Revenue 3yr CAGR >8%, FCF positive 3 consecutive years, Net Debt/EBITDA <2.5x, FCF yield >4%, EV/EBIT <20x. Basis is TTM (current) for all metrics except where flagged.

| Ticker | Gross M | Net M | ROIC* | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA | FCF Yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 47.86% ✅ | 27.15% ✅ | 65.01% ✅ | 1.81% ❌ | ✅ | 0.10x ✅ | 2.61% ❌ | 33.16x ❌ | FAIL — growth, FCF yield, EV/EBIT miss |
| ABNB | 82.91% ✅ | 19.90% ✅ | 27.25% ✅ | 13.38% ✅ | ✅ | net cash ✅ | 5.24% ✅ | 29.97x ❌ | **FAIL — EV/EBIT only miss (best near-miss)** |
| ADP | 53.20% ✅⚠️ | 19.84% ✅⚠️ | 50.64% ✅⚠️ | 7.63% ❌⚠️ | ✅ | 0.21x ✅⚠️ | 5.19% ✅ | ≈19.04x ✅⚠️ | **FAIL — Revenue CAGR only miss, narrowly (7.63% vs 8%)** |
| AMAT | 48.96% ✅ | 29.31% ✅ | 27.85% ✅ | 3.23% ❌ | ✅ | net cash ✅ | 1.30% ❌ | 49.33x ❌ | FAIL — growth, FCF yield, EV/EBIT all miss (EV/EBIT worsened sharply from 21.64x FY2025) |
| AMD | 50.28% ✅ | 13.37% ✅ | 6.39% ❌ | 13.64% ✅ | ✅ | net cash ✅ | 1.06% ❌ | 182.99x ❌ | FAIL — ROIC, FCF yield, EV/EBIT all miss |
| ANET | 63.53% ✅ | 38.32% ✅ | 28.49% ✅ | 27.15% ✅ | ✅ | net cash ✅ | 2.45% ❌ | 48.78x ❌ | FAIL — FCF yield, EV/EBIT miss |
| BR | 31.32% ❌ | 15.04% ✅ | 18.20% ✅ | 6.46% ❌ | ✅ | 1.66x ✅ | 7.45% ✅ | 16.58x ✅ | **FAIL — Gross Margin & Revenue CAGR miss only (2-filter near-miss, new candidate this round)** |
| BRK.B | 29.58% ❌ | 19.31% ✅ | 5.01% ❌ | 7.14% ❌ | ✅ | net cash ✅ | 2.23% ❌ | 7.73x ✅⚠️ | FAIL — conglomerate; margin/ROIC/growth/FCF-yield all miss |
| CSCO | 64.33% ✅ | 19.69% ✅ | 16.53% ✅ | 3.19% ❌ | ✅ | 0.88x ✅ | 2.61% ❌ | 32.97x ❌ | FAIL — growth, FCF yield, EV/EBIT miss |
| DDOG | 79.87% ✅ | 3.69% ❌ | -0.48% ❌ | 26.95% ✅ | ✅ | net cash ✅⚠️ | 1.18% ❌ | n/m ❌ | FAIL — margin, ROIC, FCF yield miss; EBIT not meaningful |
| FICO | 84.18% ✅ | 33.67% ✅ | 82.78% ✅ | 13.08% ✅ | ✅ | 2.98x ❌ | 3.03% ❌ | 29.16x ❌ | FAIL — leverage, FCF yield, EV/EBIT miss |
| FTNT | 80.30% ✅ | 27.50% ✅ | 41.66% ✅ | 15.47% ✅ | ✅ | net cash ✅ | 2.22% ❌ | 48.38x ❌ | FAIL — FCF yield, EV/EBIT miss (both worse than 07-07: multiple nearly doubled from 27.06x) |
| KLAC | 61.44% ✅ | 35.66% ✅ | 42.22% ✅ | 9.68% ✅ | ✅ | 0.16x ✅ | 1.61% ❌ | 45.92x ❌ | FAIL — FCF yield, EV/EBIT miss (multiple nearly doubled from 25.06x on 07-07) |
| LLY | 82.83% ✅ | 34.99% ✅ | 40.11% ✅ | 31.69% ✅ | ✅ | 1.14x ✅ | 1.11% ❌ | 35.07x ❌ | FAIL — FCF yield, EV/EBIT miss |
| LPLA | 23.43% ❌ | 4.93% ❌ | 10.85% ❌ | 25.47% ✅ | ❌ | 2.66x ❌ | n/m (neg.) ❌ | 19.15x ✅ | FAIL — thin-margin brokerage model; 6 of 8 filters miss |
| LRCX | 49.98% ✅ | 30.94% ✅ | 48.34% ✅ | 2.29% ❌ | ✅ | net cash ✅ | 1.65% ❌ | 48.96x ❌ | FAIL — growth, FCF yield, EV/EBIT miss (multiple more than doubled from 20.58x FY2025) |
| MA | 100.00% ✅⚠️ | 45.88% ✅ | 64.54% ✅ | 13.82% ✅ | ✅ | 0.52x ✅ | 3.65% ❌ | 25.34x ❌ | **FAIL — FCF yield & EV/EBIT both close misses (3.65% vs 4%; 25.34x vs 20x)** |
| MRVL | 51.50% ✅ | 28.99% ✅ | 6.40% ❌ | 11.45% ✅ | ✅ | 0.42x ✅ | 1.01% ❌ | 120.07x ❌ | FAIL — ROIC, FCF yield, EV/EBIT miss |
| ORCL | 65.82% ✅ | 25.21% ✅ | 10.64% ❌ | 10.48% ✅ | ❌ | 4.16x ❌ | n/a (neg.) ❌ | 23.34x ❌ | FAIL — AI/OCI capex surge has pushed FCF further negative (TTM FCF −$23.7B); ROIC, leverage, EV/EBIT also miss |
| PANW | 71.94% ✅ | 7.95% ❌ | 3.82% ❌ | 18.79% ✅ | ✅ | net cash ✅ | 1.47% ❌ | 252.61x ❌ | FAIL — Net margin newly below 12% bar (was 12.30% on 07-07); ROIC, FCF yield, EV/EBIT also miss |
| PLTR | 84.07% ✅ | 43.68% ✅ | 24.09% ✅ | 32.91% ✅ | ✅ | net cash ✅ | 0.85% ❌ | 154.37x ❌ | FAIL — FCF yield, EV/EBIT miss (still the most extreme valuation on the list) |
| TYL | 46.75% ✅ | 13.26% ✅ | 9.64% ❌ | 8.02% ✅⚠️ | ✅ | net cash ✅ | 5.16% ✅ | 35.35x ❌ | **FAIL — ROIC & EV/EBIT miss only (2-filter miss; FCF yield now clears vs. before)** |

*⚠️ = figure carries a data-quality caveat, see Section 4. \*ROIC proxied by stockanalysis.com's "Return on Capital Employed (ROCE)," consistent with the 07-07 session's methodology.*

Source: `stockanalysis.com` financials/ratios/cash-flow-statement pages per ticker, pulled 2026-07-28 by scripted HTTP fetch + parse (22 tickers × 3 pages = 66 page fetches).

---

## ✅ Qualified Quality List — **0 names**

**Zero of the 22 candidates clear the full Phase 01 gate** — third consecutive result of 0 for this slice (07-07 also found 0; the original 2026-06-07 pass likewise found 0). This continues to read as a real, sourced finding rather than a screening gap: every candidate that clears the business-quality filters (margins, ROIC, growth, balance sheet) is stopped by the valuation filters (FCF yield <4%, EV/EBIT <20x). If anything, this round's multiples are **more** stretched, not less — several AI-capex-adjacent semicap/networking names (LRCX, AMAT, KLAC, ANET, FTNT) show EV/EBIT roughly 1.5–2× wider than their 07-07 reading, consistent with a continued AI-driven re-rating in this cohort over the past three weeks rather than a mean-reversion.

**Near-misses worth flagging for a future rotation or a dedicated look regardless:**
- **ABNB** (1 filter) — misses only EV/EBIT (29.97x vs <20x); every quality/growth/balance-sheet filter clears comfortably. Unchanged story since 07-07.
- **ADP** (1 filter) — misses only Revenue 3yr CAGR, and narrowly (7.63% vs the 8% bar, on a corrected basis — see data gaps below); everything else clears, including EV/EBIT (≈19.04x) and FCF yield (5.19%). Consistent with the 07-07 finding.
- **BR** (2 filters, **new candidate this round**) — Broadridge Financial Solutions misses only Gross Margin (31.32% vs >40% — a lower-margin proxy/fintech-services cost structure) and Revenue 3yr CAGR (6.46% vs >8%); every valuation filter (EV/EBIT 16.58x, FCF yield 7.45%, Net Debt/EBITDA 1.66x) clears comfortably. Worth a dedicated `/new-position` look given how cheap it screens on the filters it does clear.
- **TYL** (2 filters) — misses ROIC (9.64% vs >15%) and EV/EBIT (35.35x); FCF yield newly clears (5.16%, was 3.26% on 07-07).
- **MA** (2 filters) — FCF yield 3.65% (vs >4%) and EV/EBIT 25.34x (vs <20x), both near the bar and both slightly worse than 07-07; every quality filter clears strongly.

**Notable changes worth flagging (real events, not screening artifacts):**
- **PANW** — net margin dropped from 12.30% (a 07-07 pass, flagged borderline then) to 7.95% this round, now a clean fail. Plausible driver is integration/acquisition-related costs (Palo Alto Networks closed its CyberArk acquisition in 2025) but this was **not independently confirmed via a dedicated news check this session** — flagged as a real fundamentals move worth investigating if PANW is ever pulled into a `/new-position` evaluation, not asserted as fact.
- **LRCX, AMAT, KLAC, ANET, FTNT** — all show EV/EBIT multiples meaningfully wider than the 07-07 pass (roughly 1.5–2×), consistent with continued semicap/AI-infrastructure-adjacent re-rating rather than a data artifact (each was cross-checked against its own most-recent-fiscal-year EV/EBIT reading, which moved the same direction).
- **APP, QCOM** — both 07-07 candidates, dropped out of all three ETFs' top-25 this round (pure composition churn, not re-tested).

---

## 3. Qualitative pass (Step 3)

**Not applicable this rotation** — zero candidates cleared the quantitative gate to advance to a qualitative review, per Step 3's scope ("For each name that clears the quantitative gate...").

---

## 4. Data gaps and caveats (Step 4)

- **`yfinance`/direct Yahoo access failed with the same TLS connection-reset error** seen in every rotation session since 2026-07-07 — flagged again for `/healthcheck` (Routine 7) to pick up; this now looks like a persistent environment-level network block rather than a transient issue. `stockanalysis.com` covered every metric needed this session; no estimation was used anywhere in the table above (CLAUDE.md Rule 0).
- **ADP's TTM column is internally inconsistent on stockanalysis.com this session** — TTM Revenue ($11,299M) and Operating Income (−$4,698M) are both far out of line with FY2025's $20,561M/$5,412M (ADP's fiscal year ends June 30; TTM should track *above* FY2025, not roughly half of it), and the TTM "Profit Margin" row (47.28%) doesn't even arithmetically match TTM Net Income ÷ TTM Revenue (4,346/11,299 = 38.46%) — internally contradictory, so treated as a stockanalysis.com data artifact rather than real ADP fundamentals. **Substitution made and shown here, not silently absorbed:** Gross Margin, Net Margin, ROIC(ROCE), Revenue 3yr CAGR, Net Debt/EBITDA, and the three-year FCF-positivity check all use **FY2025 (fiscal year ended 2025-06-30)** figures instead of the broken TTM column. EV/EBIT was reconstructed as **live/TTM Enterprise Value ÷ FY2025 EBIT** ($103,094M ÷ $5,412M = 19.04x) since Enterprise Value itself (built from live market cap) looked sound while EBIT did not; FCF Yield was left as the reported TTM figure (5.19%) since it's FCF-based, not EBIT-based, and was internally consistent with the FY2025 FCF trend. All ADP figures above are marked ⚠️ accordingly.
- **MA's Gross Margin (100.00%)** is a data-structure artifact, not a real COGS-based margin — Mastercard's income statement carries no separate Cost-of-Revenue line, same note carried forward from the 07-07 session. Doesn't change the PASS/FAIL verdict (MA fails on FCF yield/EV/EBIT, not margin).
- **BRK.B's EV/EBIT (7.73x)** clears the <20x bar but is not meaningfully comparable — Berkshire's earnings are dominated by an insurance float and investment portfolio, not operating income, same caveat as 07-07. Doesn't change BRK.B's overall FAIL.
- **DDOG's Net Debt/EBITDA (−91.90x)** is a mathematical artifact of a near-zero EBITDA denominator on an asset-light, large-net-cash balance sheet, not a meaningful leverage read — shown as-is (still clearly "net cash," doesn't change the FAIL either way).
- **Stale automation prompt (process note, not a data gap):** this routine's scheduled prompt still describes itself as the "Monthly Universe Screening Slice" running "the first Saturday of each month" and references an `EODHD_API_KEY`/"Path A" that was removed from the framework on 2026-06-19. [automation-schedule.md](../framework/automation-schedule.md) currently documents this as a twice-weekly cadence with no EODHD path at all. This is at least the fourth consecutive rotation session to hit this same stale-prompt mismatch (after [2026-06-30 Japan](2026-06-30-screening-japan.md), [2026-07-04 NA-2](2026-07-04-screening-na2.md), and [2026-07-07 NA-1](2026-07-07-screening-na1.md)) — worth updating whatever schedules the actual cron/trigger for this routine so it matches the current framework docs, since re-discovering and re-explaining the same drift every run is pure overhead.

---

## 5. Coverage log update (Step 5)

[screening-coverage-log.md](../framework/screening-coverage-log.md)'s NA-1 row updated: Last screened → 2026-07-28, Qualified names found → 0 (near-misses flagged: ABNB, ADP, BR, TYL, MA), Sources used → MOAT/QUAL/QGRW ETF holdings + `stockanalysis.com` quantitative gate (yfinance/direct Yahoo access still blocked by a TLS connection-reset error this session, same failure mode since 2026-07-07).

---

## Glossary

- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate between a start and end value.
- **EV/EBIT** — Enterprise Value ÷ EBIT, a multiple measuring how expensive a company is relative to its operating profit; lower is cheaper.
- **FCF (Free Cash Flow)** — cash a business generates after running/maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value); higher means cheaper.
- **Gross Margin** — Gross Profit ÷ Revenue; the share of each revenue dollar left after direct production/delivery costs.
- **Net Debt/EBITDA** — net debt ÷ EBITDA, this framework's primary balance-sheet-leverage gate; lower (or negative, i.e. net cash) is safer.
- **Net Margin** — Net Income ÷ Revenue; the share of each revenue dollar left as accounting profit after every expense.
- **Phase 01** — this framework's Universe Screening / quality-gate stage, the subject of this session.
- **Qualified Quality List** — the output of Phase 01 screening: companies that passed the quality gate and are eligible for Phase 02 valuation scoring.
- **ROIC** — Return on Invested Capital; how efficiently a company turns invested capital (debt + equity) into profit.
- **Rotation Matrix** — the [screening-coverage-log.md](../framework/screening-coverage-log.md) table that tracks which region/sector slice was screened when, so `/screen` systematically rotates through the whole investable universe instead of re-covering familiar names.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of financial results, regardless of fiscal-year boundary; used here as the "current" basis for most ratios.

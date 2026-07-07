# 2026-07-07 — SCREENING: North America — NA-1 (Tech, Communication Services, Consumer Discretionary)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [NA-1](../framework/screening-coverage-log.md) (North America: US + Canada; sector emphasis Tech, Communication Services, Consumer Discretionary). Selected per the rotation rule: **2026-06-07 was the oldest "Last screened" date** on the matrix (all five other rows carry 2026-06-14 or later).

This was run as an **unattended scheduled routine** ("Monthly Universe Screening Slice," first Saturday of the month — markets closed) with no interactive user present. This is a **re-screen of a previously-covered slice**, exactly one month after its first pass ([2026-06-07 session](2026-06-07-screening-broad-quality-universe.md)) — the point of the rotation cadence is to catch ETF-composition churn and valuation moves, not just cover new ground.

---

## 0. Methodology

No interactive TIKR/Koyfin screener export was available — there was no user to ask, so per Step 0's documented unattended-session exception, this session went straight to the ETF-holdings fallback.

- **EODHD was NOT used**, despite this run's task prompt again referencing an `EODHD_API_KEY` set in the environment and calling this "Routine 4... uses EODHD_API_KEY... for full automation (Path A)." That path was deprecated and removed from the framework on 2026-06-19 ([decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)), which explicitly says to treat that credential as compromised (it was committed to git history) if it's ever needed again. The canonical [screen.md](../.claude/commands/screen.md) and [automation-schedule.md](../framework/automation-schedule.md) have no EODHD path — same precedent already set by the [2026-06-30 Japan](2026-06-30-screening-japan.md) and [2026-07-04 NA-2](2026-07-04-screening-na2.md) sessions, both of which made the identical call when handed the same stale prompt. CLAUDE.md instructs treating `framework/` as the source of truth over a stale prompt. (Note for a future prompt/cron cleanup: the scheduled prompt for this routine appears not to have been updated when the framework dropped EODHD and later renamed the cadence from monthly to twice-weekly — see the Data Gaps section below.)
- **`yfinance` was attempted first** (the framework's documented standard per-candidate source). The package wasn't even installed in this environment (`pip install yfinance` succeeded), but every live request failed with a TLS/connection-reset error (`curl_cffi.requests.exceptions.SSLError: ... Connection reset by peer`) against Yahoo's endpoints — a genuine network-level block in this environment, not a rate limit this time. Confirmed `stockanalysis.com` was reachable via direct `curl` before falling back.
- **Fell back to `stockanalysis.com`**, same precedent as the [2026-07-04 NA-2](2026-07-04-screening-na2.md) and [2026-06-14 APAC-ex-Japan](2026-06-14-screening-apac-ex-japan.md) sessions. Pulled two pages per candidate — `/stocks/<ticker>/financials/` (Gross Margin, Net Margin, Revenue history, FCF history) and `/stocks/<ticker>/financials/ratios/` (ROIC, EV/EBIT, Net Debt/EBITDA, FCF Yield) — via 5 parallel research agents (batches of 4–5 tickers each) to keep this within a reasonable session length.
- **Starting universe rebuilt from fresh ETF holdings** (MOAT, QUAL, QGRW — the same three sources as the original 2026-06-07 pass, pulled fresh via `stockanalysis.com/etf/<ticker>/holdings/`, current as of 2026-07-03/07). ETF composition has churned meaningfully in the month since the first pass:
  - **New to the top-25 this round:** ADP, CSCO, FICO, MRVL, QCOM, SCHW, VEEV
  - **Dropped out of the top-25 this round:** BR, CRWD, NXPI, TLT, TRU, TSLA, WMT
  - VEEV is excluded below (already a portfolio holding, tracked via `/rescore`).

---

## 1. Deduplicated starting universe → structural triage (Step 1)

Combining the three fresh ETF lists gives **57 raw names**. After removing current portfolio holdings ([holdings.md](../portfolio/holdings.md): AMZN, AVGO, GOOG, GOOGL, META, MSFT, NFLX, NKE, NVDA, V, VEEV — 11 names, tracked via `/rescore` rather than re-discovered here), **46 candidates** remain.

Structural triage eliminated names on the same well-documented business-model grounds established in the original NA-1 pass and the NA-2 rotation (flagged transparently so any can be pulled back on request):

| Eliminated | Why (structural, not measured) |
|---|---|
| COST, ROST, TJX | Large-volume retail — net margins structurally 2–6% |
| XOM | Integrated oil major — commodity-cyclical margins/revenue |
| MAS | Building products — mid-single-digit net margins, cyclical |
| MDLZ, KVUE, CLX, STZ, BF.B | Packaged consumer staples — low-single-digit revenue growth |
| BMY, MRK, JNJ | Large pharma, well-documented patent-cliff cycles |
| DHR, ZBH, GEHC, OTIS | Industrials/medtech stalwarts — mid-teens margins, mid-single-digit growth |
| CAT, GE, GEV | Cyclical industrials |
| EL | Documented margin-compression/turnaround phase |
| LIN | Industrial gases — ~20% margins but historically mid-single-digit growth |
| MU | Memory semiconductor — margin-*stability* failure by category |
| **SCHW** *(new this round)* | Broker-dealer — same thin-margin brokerage-model exclusion as LPLA (which fails the quantitative gate below) and the NA-2 precedent for IBKR/SCHW |

**24 names eliminated. 23 remain** for the real, sourced quantitative pull: **AAPL, ABNB, ADP, AMAT, AMD, ANET, APP, BRK.B, CSCO, DDOG, FICO, FTNT, KLAC, LLY, LPLA, LRCX, MA, MRVL, ORCL, PANW, PLTR, QCOM, TYL**.

Of these, 18 (AAPL, ABNB, AMAT, AMD, ANET, APP, BRK.B, DDOG, FTNT, KLAC, LLY, LPLA, LRCX, MA, ORCL, PANW, PLTR, TYL) were also survivors of the original 2026-06-07 triage; 5 (ADP, CSCO, FICO, MRVL, QCOM) are new entrants via ETF churn. **FICO** in particular closes the "future IT-sector pass" gap flagged (and deliberately left untested) in the [2026-07-04 NA-2 session](2026-07-04-screening-na2.md#1-structural-triage-step-1).

---

## 2. Quantitative Phase 01 gate (real, sourced data — stockanalysis.com, 2026-07-07)

Filters per [valuation-scoring.md](../framework/valuation-scoring.md#quantitative-pre-screen-filters-phase-01): Gross margin >40%, Net margin >12%, ROIC >15%, Revenue 3yr CAGR >8%, FCF positive 3 consecutive years, Net Debt/EBITDA <2.5x, FCF yield >4%, EV/EBIT <20x.

| Ticker | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA | FCF Yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 47.86% ✅ | 27.15% ✅ | 104.33% ✅ | 1.81% ❌ | ✅ | 0.10x ✅ | 2.81% ❌ | 30.74x ❌ | FAIL — growth, FCF yield, EV/EBIT all miss |
| ABNB | 82.91% ✅ | 19.90% ✅ | 27.25% ✅ | 13.37% ✅ | ✅ | net cash ✅ | 5.15% ✅ | 30.54x ❌ | **FAIL — EV/EBIT only miss (best near-miss)** |
| ADP | 53.28% ✅ | 24.73% ✅ | 67.30% ✅ | 7.62% ❌ | ✅ | 0.17x ✅ | 5.53% ✅ | 16.84x ✅ | **FAIL — Revenue CAGR only miss, narrowly (7.62% vs 8%)** |
| AMAT | 48.96% ✅ | 29.31% ✅ | 32.47% ✅ | 3.23% ❌ | ✅ | net cash ✅ | 1.14% ❌ | 53.46x ❌ | FAIL — growth, FCF yield, EV/EBIT all miss |
| AMD | 50.28% ✅ | 13.17% ✅ | 7.75% ❌ | 13.64% ✅ | ✅ | net cash ✅ | 0.95% ❌ | 202.15x ❌ | FAIL — ROIC, FCF yield, EV/EBIT all miss |
| ANET | 64.06% ✅ | 38.99% ✅ | 245.21% ✅⚠️ | 27.1% ✅ | ✅ | net cash ✅ | 2.42% ❌ | 49.54x ❌ | FAIL — FCF yield, EV/EBIT miss |
| APP | 87.86% ✅ | 60.83% ✅ | 128.46% ✅⚠️ | 24.9% ✅ | ✅ | 0.15x ✅ | 2.43% ❌ | 38.71x ❌ | FAIL — FCF yield, EV/EBIT miss |
| BRK.B | 29.53% ❌ | 18.11% ✅ | 10.47% ❌ | 7.1% ❌ | ✅ | net cash ✅ | 2.19% ❌ | 7.91x ✅⚠️ | FAIL — conglomerate; margin/ROIC/growth/FCF-yield all miss |
| CSCO | 64.94% ✅ | 17.97% ✅ | 19.20% ✅ | 3.2% ❌ | ✅ | 0.88x ✅ | 2.64% ❌ | 32.18x ❌ | FAIL — growth, FCF yield, EV/EBIT miss |
| DDOG | 79.96% ✅ | 3.14% ❌ | −4.12% ❌ | 27.0% ✅ | ✅ | net cash ✅⚠️ | 1.17% ❌ | n/m ❌ | FAIL — margin, ROIC, FCF yield miss; EBIT negative (EV/EBIT not meaningful) |
| FICO | 82.23% ✅ | 32.75% ✅ | 63.76% ✅ | 13.08% ✅ | ✅ | 3.13x ❌ | 2.16% ❌ | 41.63x ❌ | FAIL — leverage, FCF yield, EV/EBIT miss |
| FTNT | 80.46% ✅ | 27.41% ✅ | 158.52% ✅ | 15.47% ✅ | ✅ | net cash ✅ | 3.77% ❌ | 27.06x ❌ | FAIL — FCF yield (just under 4%), EV/EBIT miss |
| KLAC | 60.91% ✅ | 33.41% ✅ | 72.15% ✅ | 9.69% ✅ | ✅ | 0.27x ✅ | 3.17% ❌ | 25.06x ❌ | FAIL — FCF yield, EV/EBIT miss |
| LLY | 83.04% ✅ | 31.67% ✅ | 39.65% ✅ | 31.69% ✅ | ✅ | 1.25x ✅ | 0.93% ❌ | 37.90x ❌ | FAIL — FCF yield, EV/EBIT miss |
| LPLA | 23.67% ❌ | 5.08% ❌ | 12.26% ❌ | 25.46% ✅ | ❌ | 2.82x ❌ | −3.46% ❌ | 22.42x ❌ | FAIL — thin-margin brokerage model; 7 of 8 filters miss |
| LRCX | 49.98% ✅ | 30.94% ✅ | 73.88% ✅ | 2.29% ❌ | ✅ | net cash ✅ | 1.37% ❌ | 58.83x ❌ | FAIL — growth, FCF yield, EV/EBIT miss |
| MA | 100.00% ✅⚠️ | 45.65% ✅ | 94.91% ✅ | 13.81% ✅ | ✅ | 0.52x ✅ | 3.78% ❌ | 23.83x ❌ | **FAIL — FCF yield & EV/EBIT both close misses (3.78% vs 4%; 23.83x vs 20x)** |
| MRVL | 51.02% ✅ | 32.58% ✅ | 6.80% ❌ | 11.45% ✅ | ✅ | 0.42x ✅ | 0.76% ❌ | 153.42x ❌ | FAIL — ROIC, FCF yield, EV/EBIT miss |
| ORCL | 65.82% ✅ | 25.37% ✅ | 11.24% ❌ | 10.47% ✅ | ❌ | 4.16x ❌ | n/a (neg.) ❌ | 24.55x ❌ | FAIL — AI/OCI capex surge has pushed FCF negative; ROIC, leverage, EV/EBIT also miss |
| PANW | 73.41% ✅ | 12.30% ✅⚠️ | 3.86% ❌ | 18.79% ✅ | ✅ | net cash ✅ | 1.30% ❌ | 300.07x ❌ | FAIL — ROIC, FCF yield, EV/EBIT miss |
| PLTR | 82.37% ✅ | 36.52% ✅ | 433.15% ✅⚠️ | 32.9% ✅ | ✅ | net cash ✅ | 0.49% ❌ | 295.75x ❌ | FAIL — FCF yield, EV/EBIT miss (most extreme valuation on the list) |
| QCOM | 55.43% ✅ | 12.51% ✅⚠️ | 20.22% ✅ | 0.06% ❌ | ✅ | 0.33x ✅ | 7.05% ✅ | 15.09x ✅ | **FAIL — Revenue CAGR only miss (revenue essentially flat FY22→FY25 despite a FY23 dip and recovery)** |
| TYL | 46.46% ✅ | 13.53% ✅ | 8.89% ❌ | 8.03% ✅⚠️ | ✅ | net cash ✅ | 3.26% ❌ | 53.46x ❌ | FAIL — ROIC, FCF yield, EV/EBIT miss |

*⚠️ = figure carries a data-quality caveat, see Section 4.*

Source: `stockanalysis.com` financials + ratios pages per ticker, pulled 2026-07-07 by 5 parallel research passes.

---

## ✅ Qualified Quality List — **0 names**

**Zero of the 23 candidates clear the full Phase 01 gate.** This is a real, sourced finding, not a screening gap — it mirrors the [2026-07-04 NA-2](2026-07-04-screening-na2.md) result (1 of 21) and the same underlying story the original [2026-06-07 NA-1 session](2026-06-07-screening-broad-quality-universe.md) already flagged via the Rate Environment Gate: this cohort of quality/growth names is priced for perfection across the board, and the current Phase 01 filter set (which folds EV/EBIT <20x and FCF yield >4% directly into the quality gate, not just into Phase 02 scoring) is unforgiving of that. Every single candidate that clears the *business-quality* filters (margins, ROIC, growth, balance sheet) gets stopped by the *valuation* filters (FCF yield, EV/EBIT) — consistent with a market-wide "wonderful businesses, no margin of safety" read, not a data problem.

**Near-misses worth flagging for a future rotation or a dedicated look regardless (only 1 filter miss each):**
- **ABNB** — misses only EV/EBIT (30.54x vs <20x); every quality/growth/balance-sheet filter clears comfortably.
- **ADP** — misses only Revenue 3yr CAGR, and narrowly (7.62% vs the 8% bar) — everything else, including EV/EBIT (16.84x) and FCF yield (5.53%), clears.
- **QCOM** — misses only Revenue 3yr CAGR, but by a wide margin (revenue essentially flat FY22→FY25 after a FY23 dip and recovery) — the only name on this list that clears **both** valuation filters (EV/EBIT 15.09x, FCF yield 7.05%) outright.

**Two-filter-miss names, both close on both misses — worth a rate-cut/pullback watch:**
- **MA** — FCF yield 3.78% (vs >4%) and EV/EBIT 23.83x (vs <20x), both near the bar; every quality filter clears strongly (ROIC 94.91%, net margin 45.65%).
- **FTNT** and **KLAC** — both miss only on FCF yield (3.77%, 3.17%) and EV/EBIT (27.06x, 25.06x); both were qualified in the original 2026-06-07 pass and remain excellent businesses priced above this framework's cheapness bar.

---

## 3. Qualitative pass (Step 3)

**Not applicable this rotation** — zero candidates cleared the quantitative gate to advance to a qualitative review, per Step 3's scope ("For each name that clears the quantitative gate...").

---

## 4. Data gaps and caveats (Step 4)

- **`yfinance`/direct Yahoo access failed with a TLS connection-reset error** in this environment (not a rate limit this time) — flagged for `/healthcheck` (Routine 7) to pick up if it persists. `stockanalysis.com` covered every metric needed this session; no estimation was used anywhere in the table above (CLAUDE.md Rule 0).
- **ROIC figures for ANET (245%), APP (128%), and PLTR (433%)** are as directly reported by `stockanalysis.com`, not independently re-derived from NOPAT/Invested Capital. These are asset-light, large-net-cash businesses where a small invested-capital denominator mechanically inflates the ratio — flagged, not silently trusted, but shown as-is since re-deriving them wouldn't plausibly flip the PASS on that single filter (all three fail on FCF yield/EV/EBIT regardless).
- **MA's Gross Margin (100.00%)** is a data-structure artifact, not a real COGS-based margin — Mastercard's income statement carries no separate Cost-of-Revenue line (a payment network, same category as the "no conventional gross-margin line" REIT note from the NA-2 session, though MA's underlying economics are nothing like a REIT's). The prior 2026-06-07 session sourced MA's gross margin as 96.57% from Finviz; this session's 100.00% from `stockanalysis.com` reflects a different provider's treatment of the same "no COGS line" reality, not a change in the business. Flagged rather than reconciled — doesn't change the PASS/FAIL verdict either way (MA fails on FCF yield/EV/EBIT, not margin).
- **BRK.B's EV/EBIT (7.91x)** clears the <20x bar, but EBIT/EBITDA-based multiples are a poor fit for a company whose earnings are dominated by an insurance float and investment portfolio, not operating income — flagged as not meaningfully comparable, though it doesn't change BRK.B's overall FAIL (margin, ROIC, growth, and FCF yield all miss independently).
- **PANW's Net Margin (12.30%)** and **QCOM's Net Margin (12.51%)** both sit right at the 12% line — reported as PASS per the sourced figure, flagged as borderline rather than a comfortable clear.
- **Stale automation prompt (process note, not a data gap):** this routine's scheduled prompt still describes itself as the "Monthly Universe Screening Slice" running "the first Saturday of each month" and references an `EODHD_API_KEY`/"Path A" that was removed from the framework on 2026-06-19. [automation-schedule.md](../framework/automation-schedule.md) currently documents this as "Routine 4 — Twice-Weekly Universe Screening Slice" (Tuesday and Saturday) with no EODHD path at all. This is the third consecutive rotation session (after [2026-06-30 Japan](2026-06-30-screening-japan.md) and [2026-07-04 NA-2](2026-07-04-screening-na2.md)) to hit this same stale-prompt mismatch — worth updating whatever schedules the actual cron/trigger for this routine so it matches the current framework docs, since re-discovering and re-explaining the same drift every run is pure overhead.

---

## 5. Coverage log update (Step 5)

[screening-coverage-log.md](../framework/screening-coverage-log.md)'s NA-1 row updated: Last screened → 2026-07-07, Qualified names found → 0 (near-misses flagged: ABNB, ADP, QCOM, MA, FTNT, KLAC), Sources used → MOAT/QUAL/QGRW ETF holdings + `stockanalysis.com` quantitative gate (yfinance/direct Yahoo access blocked by a TLS connection-reset error this session).

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

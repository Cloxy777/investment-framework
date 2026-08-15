# 2026-08-15 — SCREENING: North America — NA-2 (Financials, Healthcare, Industrials, Energy, Materials, Real Estate/Utilities), Round 3

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [NA-2](../framework/screening-coverage-log.md), re-run. Selected per the rotation rule: NA-2's "Last screened" date (2026-07-25) was the oldest of all six rows as of this run (NA-2 07-25 < APAC-EX-JP 08-01 < NA-1 07-28 < EM 08-04 < EU 08-08 < JP 08-11).

This was run as an **unattended scheduled routine** with no interactive user present.

---

## 0. Methodology

- **This run's stored automation prompt again referenced a removed `EODHD_API_KEY` "Path A" and described the cadence as monthly ("first Saturday of the month").** Both are stale: EODHD was removed from the framework on 2026-06-19 ([decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), which explicitly says to treat that credential as compromised — it was committed to git history — if it's ever needed again), and the actual, currently-configured cadence per [automation-schedule.md](../framework/automation-schedule.md) Routine 4 is **twice-weekly (Tuesday and Saturday)**, not monthly. Same discrepancy already identified and handled the same way in the 2026-07-25 NA-2, 2026-08-01 APAC-ex-Japan, and 2026-08-04 EM sessions — followed the current, authoritative [screen.md](../.claude/commands/screen.md) / [automation-schedule.md](../framework/automation-schedule.md) instead of the stale prompt text, per CLAUDE.md's instruction to treat `framework/` as the source of truth.
- **`yfinance`/direct Yahoo Finance was attempted first** (the framework's documented standard per-candidate source). `yfinance` was not even installed in this environment; after installing it, every request failed with the same `curl_cffi` SSL `Connection reset by peer` error seen in every session since 2026-07-07. Confirmed genuine upstream block, not a data point to guess around.
- **Fell back to `stockanalysis.com`**, same source and two-page-per-candidate method as every NA-2 round to date: `/financials/` for gross/net margin, revenue history, and FCF history; `/financials/ratios/` for ROIC, EV/EBIT, Net Debt/EBITDA, and FCF yield.
- **Candidate pool built via structural triage / domain knowledge, not the ETF-holdings fallback** — same call as the 07-04 and 07-25 NA-2 rounds: MOAT/QUAL/QGRW/IQLT skew heavily tech/consumer (NA-1's territory), which doesn't fit NA-2's sector emphasis (Financials ex-bank, Healthcare, Industrials, Energy, Materials, Real Estate/Utilities). This round targeted **18 fresh names not yet tested in either prior NA-2 round** (see [07-04](2026-07-04-screening-na2.md) and [07-25](2026-07-25-screening-na2.md) for the 25 names already covered), spanning asset-light Financials (exchanges/data/credit bureaus), non-patent-cliff Healthcare (medtech, diagnostics, life-science tools), and asset-light/high-margin Industrials.
- **Math check on 3yr revenue CAGR:** the WebFetch extraction tool occasionally mis-computed the compound-growth math on the raw figures it pulled (caught this on CBOE — it initially reported "8.1%" for a span that manually recomputes to 5.99%). Every CAGR figure in the table below was independently recalculated by hand from the raw annual revenue figures the tool extracted, not taken from its own stated CAGR — consistent with "never invent or estimate financial data" extending to not trusting unverified derived arithmetic either.

---

## 1. Candidate pool — this round's 18 new names

No structural eliminations were needed this round — all 18 were pre-selected as plausible asset-light/quality candidates in NA-2's sector scope, distinct from the exclusion categories already established (banks, insurers, broker-dealers, commodity cyclicals, REITs, regulated utilities — see [07-04 NA-2](2026-07-04-screening-na2.md) Section 1). Two names resolved to disqualifying findings during the quantitative pull itself rather than at triage:

| Ticker | Sector | Note |
|---|---|---|
| MASI (Masimo) | Healthcare (patient monitoring) | **Excluded mid-pull — delisted June 2026 following acquisition by Danaher (DHR).** No longer an evaluable standalone public equity; last available TTM data was net-loss (net margin −9.92%) in any case. Not scored. |
| WSO (Watsco) | Industrials (HVAC/plumbing distribution) | Quantified rather than pre-triaged out — turned out to be a thin-margin distribution business (28.05% gross margin, 6.41% net margin), the same profile this framework's structural-triage rule already excludes elsewhere ("thin-margin volume retail/distribution"). Numbers below confirm the call rather than pre-empting it. |

**16 valid candidates quantified**, spanning: Financials/data — NDAQ, CBOE, TW, MKTX, FDS, MORN, TRU, EFX, JKHY; Healthcare — COO, STE, RGEN, MTD, WAT, MASI (excluded); Industrials — FAST, HEI, WSO.

---

## 2. Quantitative Phase 01 gate (real, sourced data — stockanalysis.com, 2026-08-14/15)

Filters per [valuation-scoring.md](../framework/valuation-scoring.md): Gross margin >40%, Net margin >12%, ROIC >15%, Revenue 3yr CAGR >8%, FCF positive 3 consecutive years, Net Debt/EBITDA <2.5x, EV/EBIT <20x, FCF yield >4%. Revenue CAGR computed by hand from raw FY(N−3)→FY(N) figures (see methodology note above); all other figures as reported by stockanalysis.com's ratios page.

| Ticker | Sector | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF (3yr+) | Net Debt/EBITDA | EV/EBIT | FCF Yield | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| NDAQ | Financials (exchange/data) | 100.00% ✅ *(asset-light quirk — no COGS line, same as ICE/MSCI/MCO/CME in prior rounds)* | 34.06% ✅ | 10.43% ❌ | *insufficient data (only FY23–25 pulled)* | + all 3yr ✅ | 2.61 ❌ | 23.31 ❌ | 3.60% ❌ | FAIL — ROIC, leverage, EV/EBIT, FCF yield all miss; decisive regardless of the growth data gap |
| CBOE | Financials (exchange) | 51.53% ✅ | 23.22% ✅ | 26.92% ✅ | **5.99% ❌** *(recalculated — tool's own "8.1%" was arithmetically wrong)* | + all 4yr ✅ | net cash (−0.40) ✅ | 16.56 ✅ | 6.06% ✅ | **FAIL — growth is the only miss, once corrected** |
| TW | Financials (electronic bond trading) | *N/A — no COGS line disclosed (same asset-light quirk)* | 39.61% ✅ | 10.08% ❌ | *insufficient data (only FY23–25 pulled)* | + all 3yr ✅ | *not extracted* | *not extracted* | 4.60% ✅ | FAIL — ROIC misses; leverage/EV-EBIT data gap is moot since ROIC alone is decisive |
| MKTX | Financials (electronic bond trading) | 62.02% ✅ | 29.14% ✅ | 28.40% ✅ | 5.62% ❌ | + all 4yr ✅ | net cash (−0.38) ✅ | 15.55 ✅ | 3.40% ❌ | FAIL — growth and FCF yield miss |
| **FDS** | Financials (research/data — FactSet) | 52.72% ✅ | 25.71% ✅ | 18.41% ✅ | **7.98% ❌** *(razor-thin — 0.02pp below the 8% bar)* | + all 5yr ✅ | 1.36 ✅ | 15.01 ✅ | 7.03% ✅ | **FAIL — growth is the only miss, and by the tightest margin recorded across any NA-2 round to date** |
| **MORN** | Financials (research/data — Morningstar) | 61.03% ✅ | 15.30% ✅ | 18.24% ✅ | 9.34% ✅ | + all 5yr ✅ | 2.03 ✅ | 15.70 ✅ | 6.39% ✅ | **PASS — clears every Phase 01 filter** |
| TRU | Financials (credit bureau) | 59.09% ✅ | 9.95% ❌ | 7.63% ❌ | *not computed — already disqualified* | **FCF near-zero/negative in FY22 (−$1M); net income negative FY23** ❌ | 3.16 ❌ | 21.98 ❌ | 5.11% ✅ | FAIL — hard disqualifier (FCF/earnings history) plus margin, ROIC, leverage, EV/EBIT all miss |
| EFX | Financials (credit bureau) | 56.45% ✅ | 10.87% ❌ | 8.88% ❌ | 5.85% ❌ | + all 5yr ✅ | 2.75 ❌ | 22.55 ❌ | 5.20% ✅ | FAIL — margin, ROIC, growth, leverage, EV/EBIT all miss |
| JKHY | Financials (bank/credit-union core software) | 42.71% ✅ | 19.19% ✅ | 22.45% ✅ | 6.93% ❌ | + all 5yr ✅ | 0.16 ✅ | 16.83 ✅ | 6.68% ✅ | FAIL — growth is the only miss |
| COO | Healthcare (contact lenses/medical devices) | 65.54% ✅ | 9.16% ❌ | 2.63% ❌ | *not computed — already disqualified* | + all 5yr ✅ | 2.92 ❌ | 34.77 ❌ | 3.83% ❌ | FAIL — margin, ROIC, leverage, EV/EBIT, FCF yield all miss |
| STE | Healthcare (sterilization/infection prevention) | 44.24% ✅ | 13.18% ✅ | 9.68% ❌ | 8.94% ✅ | + all 5yr ✅ | 0.95 ✅ | 21.15 ❌ | 4.07% ✅ | FAIL — ROIC and EV/EBIT (narrowly) miss |
| RGEN | Healthcare (bioprocessing tools) | 52.65% ✅ | 6.62% ❌ | 2.60% ❌ | *not computed — already disqualified* | + all 5yr ✅ | net cash (−0.83) ✅ | 142.32 ❌ | 1.19% ❌ | FAIL — margin, ROIC, EV/EBIT, FCF yield all miss badly (post-COVID bioprocessing demand pullback still working through) |
| MTD | Healthcare (precision instruments) | 59.37% ✅ | 21.59% ✅ | 42.28% ✅ | 0.89% ❌ | + all 5yr ✅ | 1.64 ✅ | 25.57 ❌ | 3.04% ❌ | FAIL — growth stalled, priced too rich (EV/EBIT, FCF yield) |
| WAT | Healthcare (analytical instruments) | 59.28% ✅ | 20.30% ✅ | 3.35% ❌ | 2.11% ❌ | + all 5yr ✅ | 3.15 ❌ | 54.16 ❌ | 0.98% ❌ | FAIL — ROIC, growth, leverage, EV/EBIT, FCF yield all miss; likely distorted by the pending debt-funded Becton Dickinson Biosciences/Diagnostics reverse-Morris-trust merger — flagged for context, not treated as an estimate |
| MASI | Healthcare (patient monitoring) | — | — | — | — | — | — | — | — | **Not scored — delisted/acquired by Danaher, June 2026** |
| FAST | Industrials (industrial fastener distribution) | 45.01% ✅ | 15.35% ✅ | 32.06% ✅ | 5.52% ❌ | + all 5yr ✅ | 0.12 ✅ | 33.11 ❌ | 1.97% ❌ | FAIL — growth stalled, priced far too rich |
| HEI | Industrials (aerospace/electronics parts) | 39.83% ❌ *(narrow miss)* | 15.39% ✅ | 12.73% ❌ | 26.66% ✅ | + all 5yr ✅ | 1.73 ✅ | 46.98 ❌ | 1.77% ❌ | FAIL — gross margin narrowly misses; ROIC, EV/EBIT, FCF yield all miss — market has bid the M&A growth story up to an extreme multiple |
| WSO | Industrials (HVAC/plumbing distribution) | 28.05% ❌ | 6.41% ❌ | 15.72% ✅ | −0.16% ❌ | + all 5yr ✅ | 0.10 ✅ | 18.49 ✅ | 5.77% ✅ | FAIL — thin-margin distribution economics (margin, net margin, growth all miss) |

**1 of 16 valid candidates clears the full Phase 01 gate this round: MORN (Morningstar).** Two extremely tight near-misses worth flagging for a future rotation: **FDS** (only Revenue 3yr CAGR misses, by 0.02 percentage points — the tightest miss recorded across any NA-2 round to date, tighter even than 07-25's AON leverage miss) and **JKHY** (only Revenue 3yr CAGR misses, by ~1.1pp). **CBOE** is also a clean single-filter miss (growth only, 5.99% vs. 8%) once the WebFetch tool's own miscalculated CAGR figure is corrected by hand.

---

## 3. Qualitative pass (Step 3) — Morningstar (MORN)

Only one name cleared the quantitative gate, so no batching was needed.

1. **Why are margins high? Pricing power, scale, or lucky cycle?** Morningstar is a subscription/data business: proprietary fund, ETF, and equity research plus its industry-standard "Morningstar Rating" star system, layered with PitchBook (private-capital-markets data, acquired 2016), Morningstar Indexes, and DBRS Morningstar (credit ratings, acquired 2019). Margins come from software/data economics — the marginal cost of serving one more subscriber against an already-built database and research organization is low — not a cyclical or one-off effect.
2. **What would it take to compete with them? (Hard = moat)** A challenger would need a multi-decade proprietary fund/security database and a ratings methodology already embedded as the industry-default reference point in advisor and asset-manager workflows and client-facing materials — genuine switching costs. PitchBook occupies a similar entrenched position in private-markets/VC workflows. Real moat, though not unbreakable — Bloomberg, FactSet, and S&P Capital IQ compete in overlapping segments, and Preqin (now BlackRock-owned) competes directly with PitchBook in private-markets data.
3. **How has management allocated capital over 5–10 years?** Disciplined bolt-on M&A (PitchBook 2016, DBRS 2019, Sustainalytics 2020 for ESG data) funded with moderate leverage (Net Debt/EBITDA 2.03× currently) rather than heavy dilution; net income and FCF both recovered strongly from a 2022 dip (net margin fell to 3.77% that year, tied to acquisition-integration costs) to the current 15.30% — a genuine improvement, not merely a low base effect, since revenue also grew every year in the same window.
4. **Where is growth coming from next 3–5 years?** Continued PitchBook penetration into private-markets research (a secular AUM growth area), expansion of Morningstar Indexes and Sustainalytics ESG data, and Direct platform modernization/international asset-manager subscription growth.
5. **What is the best bear case against owning it?** The multi-decade shift from active to passive fund management structurally reduces demand for active-fund research and ratings — Morningstar has diversified into indexes, ESG data, and private markets partly to offset this, but the core legacy research business faces a real headwind. PitchBook also faces intensifying competition from Preqin/BlackRock. Earnings have shown real volatility in the recent past (2022's margin compression), not a smoothly compounding history.
6. **Disruption vector check.** Generative-AI research copilots could commoditize some of the analyst-driven research and ratings value proposition Morningstar currently charges for, and could also lower the cost for a new entrant to assemble a competing database from public filings — a real, non-trivial vector worth re-checking at each future re-score, not just a hypothetical.

**No valuation score computed** — that's `/new-position`'s job (Step 4 of `/screen` explicitly stops here).

---

## 4. Data gaps (Step 4)

- **NDAQ, TW:** only 3 fiscal years of revenue were extracted (FY2023–FY2025), one year short of the FY(N−3)→FY(N) window needed for a clean 3yr CAGR. Not estimated — flagged as insufficient data rather than computed over a shorter window. Moot for the pass/fail call in both cases since other filters (ROIC, leverage, EV/EBIT, FCF yield) already decisively fail.
- **TW:** no gross profit/gross margin line disclosed — same "asset-light exchange/marketplace, no conventional Cost-of-Revenue line" quirk flagged for ICE/MSCI/MCO/CME/NDAQ/CBOE across every NA-2 round to date, not a data error. Net Debt/EBITDA and EV/EBIT were not present on the ratios-page extraction for this ticker; not re-pulled since ROIC alone already disqualifies it.
- **MASI:** delisted following the Danaher acquisition (completed June 2026) — no longer an evaluable standalone equity. Not scored as a Phase 01 pass/fail; excluded from the candidate count.
- **ROIC methodology not independently re-derived**, same standing caveat as every prior NA-2 round: all ROIC figures are stockanalysis.com's own calculation, not recomputed from raw NOPAT/Invested Capital per [quality-scoring.md](../framework/quality-scoring.md)'s definition. Flagged, not silently trusted.
- **WAT's extreme multiples (EV/EBIT 54.16×, ROIC 3.35%) likely reflect deal-related distortion** from the pending, debt-funded Becton Dickinson Biosciences & Diagnostics Solutions reverse-Morris-trust merger — a real, sourced number, not an estimate, but flagged as probably not representative of Waters' standalone economics; worth a fresh look once/if that transaction closes and reported financials normalize.

---

## 5. Coverage log update (Step 5)

[screening-coverage-log.md](../framework/screening-coverage-log.md)'s NA-2 row updated: Last screened → 2026-08-15, Qualified names found → 2 total (up from 1) — **DOCS** (from 07-04) plus **MORN, new this round**; near-miss list refreshed to lead with **FDS** (Revenue 3yr CAGR only, 0.02pp miss — the tightest ever on this slice) and **JKHY** (Revenue 3yr CAGR only, ~1.1pp miss), ahead of the carried-forward AON (Net Debt/EBITDA, 0.02 miss) and CME (now 3-filter miss); CBOE added as a growth-only near-miss once its CAGR was corrected by hand. Sources used → stockanalysis.com (yfinance/Yahoo still blocked this session — `curl_cffi` SSL connection-reset, same failure mode as every session since 2026-07-07).

---

## Glossary

- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate between a start and end value.
- **EV/EBIT** — Enterprise Value ÷ EBIT, a multiple measuring how expensive a company is relative to its operating profit.
- **FCF (Free Cash Flow)** — cash a business generates after running/maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value); higher means cheaper.
- **Gross Margin** — Gross Profit ÷ Revenue; the share of each revenue dollar left after direct production/delivery costs.
- **Moat** — a durable competitive advantage (brand, network effect, switching costs, scale) protecting a business's profits from competitors.
- **Net Debt/EBITDA** — net debt ÷ EBITDA, this framework's primary balance-sheet-leverage gate.
- **Net Margin** — Net Income ÷ Revenue; the share of each revenue dollar left as accounting profit after every expense.
- **Phase 01** — this framework's Universe Screening / quality-gate stage, the subject of this session.
- **Qualified Quality List** — the output of Phase 01 screening: companies that passed the quality gate and are eligible for Phase 02 valuation scoring.
- **Reverse-Morris-Trust merger** — a tax-free deal structure where a company spins off a business unit and immediately merges it with another company's similar unit; often accompanied by significant new debt at the resulting entity.
- **ROIC** — Return on Invested Capital; how efficiently a company turns invested capital (debt + equity) into profit.

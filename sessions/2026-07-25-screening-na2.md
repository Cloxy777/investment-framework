# 2026-07-25 — SCREENING: North America — NA-2 (Financials, Healthcare, Industrials, Energy, Materials, Real Estate/Utilities), Round 2

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [NA-2](../framework/screening-coverage-log.md), re-run. Selected per the rotation rule: NA-2's "Last screened" date (2026-07-04) was the oldest of all six rows as of this run.

This was run as an **unattended scheduled routine** ("Monthly Universe Screening Slice," first Saturday of the month — markets closed) with no interactive user present.

---

## 0. Methodology

- **EODHD was NOT used**, despite this run's task prompt referencing an `EODHD_API_KEY` set in the environment. That path was deprecated and removed from the framework on 2026-06-19 ([decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)), which explicitly says to treat that credential as compromised (it was committed to git history) if it's ever needed again. The canonical [screen.md](../.claude/commands/screen.md) has no EODHD path — same precedent already set by the [2026-07-04 NA-2](2026-07-04-screening-na2.md) and [2026-06-30 Japan](2026-06-30-screening-japan.md) sessions. CLAUDE.md instructs treating `framework/` as the source of truth over a stale scheduled-task prompt.
- **`yfinance`/direct Yahoo Finance was attempted first** (the framework's documented standard per-candidate source). Failed with the identical `curl_cffi` SSL `Connection reset by peer` error seen in every recent session (07-07 NA-1, 07-11 APAC, 07-18 EU). Confirmed genuine upstream block, not a data point to guess around.
- **Fell back to `stockanalysis.com`**, same source and same two-page-per-candidate method (`/financials/` for margins, revenue, FCF history; `/financials/ratios/` for ROIC, EV/EBIT, Net Debt/EBITDA, FCF yield) as the 07-04 NA-2 session.
- **Scope for this round, since NA-2 was already fully quantified 3 weeks ago:** rather than re-pull all 21 previously-triaged names (multiples don't typically move enough in 3 weeks to change a structural "priced too rich by a wide margin" verdict), this round targeted the highest-value remaining work on this slice:
  1. **Quantified the 4 names the 07-04 session explicitly deferred** as a "follow-up candidate set" to keep that session's scope bounded: **AON, MMC, AJG** (insurance brokers — distinct asset-light commission model from LPLA's brokerage economics, worth verifying on their own numbers) and **FICO** (GICS classification ambiguity, software-like economics).
  2. **Refreshed the two flagged near-misses, DXCM and CME**, to check whether 3 weeks of price movement flipped either into a Phase 01 pass.
  3. **Formalized the IBKR/SCHW question** left open last time (structural elimination, not quantification — see below).
  4. **Left EQIX/DLR deferred** — the 07-04 session flagged these data-center names as needing "a dedicated future look with a bespoke framework" since REIT structure doesn't fit this framework's gross-margin/EV-EBIT model; no such bespoke framework exists yet, and inventing one unilaterally inside a routine screening pass is out of scope. Flagged again as a framework gap worth a `decisions/` entry if a bespoke REIT-adjacent evaluation approach is ever adopted.

---

## 1. Structural triage — this round's additions

| Ticker | Sector | Disposition | Reason |
|---|---|---|---|
| IBKR, SCHW | Financials (broker-dealers) | **Eliminated** (formalized) | Same reasoning as money-center banks: revenue weighted toward net-interest income on a leveraged balance sheet rather than fee-based compounder economics — gross margin/EV-EBIT framing doesn't apply. 07-04 flagged this as an open question rather than a final call; resolved here. |
| EQIX, DLR | Real Estate (data-center infrastructure) | **Still deferred** | REIT tax structure lacks a conventional gross-margin line; genuinely different economics from a conventional REIT, but no bespoke framework exists yet to evaluate them on. Not evaluated numerically. |
| AON, MMC, AJG | Financials (insurance brokers) | **Quantified this round** (see below) | Asset-light commission/fee model, distinct from LPLA's securities-brokerage economics — worth verifying on real numbers rather than lumping in with the broker-dealer exclusion. |
| FICO | Financials/IT boundary | **Quantified this round** (see below) | Software-like licensing economics fit the gross-margin/EV-EBIT model regardless of GICS sector label. |

---

## 2. Quantitative Phase 01 gate — new/refreshed names (stockanalysis.com, 2026-07-24/25)

Filters per [valuation-scoring.md](../framework/valuation-scoring.md): Gross margin >40%, Net margin >12%, ROIC >15%, Revenue 3yr CAGR >8%, FCF positive 3 consecutive years, Net Debt/EBITDA <2.5x, EV/EBIT <20x, FCF yield >4%.

| Ticker | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF (3yr+) | Net Debt/EBITDA | EV/EBIT | FCF Yield | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **AON** | 100.00% ✅ *(service-model gross margin quirk — see note)* | 15.83% ✅ | 15.65% ✅ | 11.2% ✅ | + all 3yr ✅ | **2.52 ❌** | 19.90 ✅ | 4.53% ✅ | **FAIL — leverage misses by 0.02, everything else clears. Closest near-miss this round.** |
| MMC | 42.38% ✅ | 14.56% ✅ | 12.81% ❌ | 7.3% ❌ | + all 3yr ✅ | 2.85 ❌ | 17.70 ✅ | 5.53% ✅ | FAIL — ROIC, growth, and leverage all miss |
| AJG | 43.49% ✅ | 10.80% ❌ | 6.44% ❌ | 17.5% ✅ | + all 4yr ✅ | 2.92 ❌ | 26.13 ❌ | 2.92% ❌ | FAIL — acquisitive, goodwill-heavy model drags ROIC (same pattern as ROP in the 07-04 session); multiple misses |
| FICO | 84.17% ✅ | 33.67% ✅ | 63.69% ✅ | 14.8% ✅ | + all 3yr ✅ | 2.98 ❌ | 28.28 ❌ | 3.14% ❌ | FAIL — aggressive buyback-funded leverage (well-documented negative-equity balance sheet) and priced far too rich |
| DXCM *(refresh)* | 60.10% ✅ *(unchanged from 07-04)* | 17.94% ✅ *(unchanged)* | 40.38% ✅ | 17.1% ✅ *(unchanged)* | + all 3yr ✅ | net cash (−0.84) ✅ | 25.72 ❌ | 5.18% ✅ | FAIL — still only EV/EBIT misses, essentially unchanged from 07-04 (25.61× → 25.72×) |
| CME *(refresh)* | 86.09% ✅ *(unchanged)* | 62.45% ✅ *(unchanged)* | 12.24% ❌ | 9.1% ✅ *(unchanged)* | + all 3yr ✅ | 0.24 ✅ | **21.20 ❌ (was 19.90 ✅)** | **1.22% ❌ (was 5.05% ✅)** | **FAIL — got materially more expensive since 07-04: EV/EBIT crossed above the 20× threshold and FCF yield collapsed on price appreciation. No longer a single-filter near-miss (now 3 misses: ROIC, EV/EBIT, FCF yield).** |

**0 of 6 clear the full Phase 01 gate this round.** AON is now the single closest name across the entire NA-2 slice — misses only on Net Debt/EBITDA, and by 0.02 (2.52 vs the <2.5 threshold), tighter than either of the 07-04 near-misses. CME moved the wrong direction (richer, not cheaper) since 07-04 and is no longer a near-miss in the same sense.

**Gross-margin note (AON, and consistent with ICE/MCO/MSCI/CME in 07-04):** asset-light financial-services/exchange businesses often show ~85–100% "gross margin" on stockanalysis.com because their cost structure has no conventional cost-of-revenue line — flagged the same way the 07-04 session flagged it, not a data error.

---

## 3. Qualitative pass (Step 3)

Not applicable — 0 names cleared the quantitative gate this round (both new candidates and refreshed near-misses fell short). Consistent with Step 3's instruction: qualitative pass runs only on Phase 01 passers.

---

## 4. Data gaps (Step 4)

- No metric was missing outright for any of the 6 names pulled this round — all 8 Phase 01 inputs sourced and shown above for each. No estimation used anywhere (CLAUDE.md Rule 0).
- `yfinance`/direct Yahoo access remains rate-limited/blocked (`curl_cffi` SSL connection reset) — consistent with every session since 07-07. Still flagged for `/healthcheck` to track; stockanalysis.com fully covered this round's needs.
- **MMC ticker label anomaly:** one of the two WebFetch extractions for Marsh & McLennan mislabeled the company as "(MRSH)" in its own summary heading despite being fetched from the `/stocks/MMC/` URL and returning figures consistent with MMC's actual scale (~$28B TTM revenue). Treated as a fetch-tool labeling artifact, not a wrong-company data pull — cross-checked the revenue/FCF figures against the correct ticker's known scale before using them.
- **EQIX/DLR remain unevaluated** pending a bespoke REIT-adjacent framework decision (see Section 1) — flagged again as an open framework gap, not silently dropped.

---

## 5. Coverage log update (Step 5)

[screening-coverage-log.md](../framework/screening-coverage-log.md)'s NA-2 row updated: Last screened → 2026-07-25, Qualified names found → still 1 total for the slice (DOCS, from 07-04; 0 new this round), near-miss list updated to lead with AON (tightest miss, Net Debt/EBITDA only, by 0.02) ahead of DXCM (EV/EBIT only); CME demoted off the near-miss list after re-pricing further from qualifying. Sources used → stockanalysis.com (yfinance/Yahoo still blocked this session, same failure mode as every session since 07-07).

---

## Glossary

- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate between a start and end value.
- **EV/EBIT** — Enterprise Value ÷ EBIT, a multiple measuring how expensive a company is relative to its operating profit.
- **FCF (Free Cash Flow)** — cash a business generates after running/maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value); higher means cheaper.
- **GICS** — Global Industry Classification Standard, the sector/industry taxonomy (e.g. "Financials," "Industrials") used to categorize public companies; some businesses (e.g. FICO) sit ambiguously between categories.
- **Gross Margin** — Gross Profit ÷ Revenue; the share of each revenue dollar left after direct production/delivery costs.
- **Net Debt/EBITDA** — net debt ÷ EBITDA, this framework's primary balance-sheet-leverage gate.
- **Net Margin** — Net Income ÷ Revenue; the share of each revenue dollar left as accounting profit after every expense.
- **Phase 01** — this framework's Universe Screening / quality-gate stage, the subject of this session.
- **Qualified Quality List** — the output of Phase 01 screening: companies that passed the quality gate and are eligible for Phase 02 valuation scoring.
- **REIT (Real Estate Investment Trust)** — a company owning/operating income-producing real estate that must distribute most taxable income as dividends; lacks a conventional gross-margin line, so this framework's Phase 01 filters don't cleanly apply.
- **ROIC** — Return on Invested Capital; how efficiently a company turns invested capital (debt + equity) into profit.

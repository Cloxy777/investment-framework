# 2026-09-05 — SCREENING: North America — NA-2 (Financials, Healthcare, Industrials, Energy, Materials, Real Estate/Utilities), Round 4

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [NA-2](../framework/screening-coverage-log.md). Selected per the rotation rule: as of this run, "Last screened" dates were NA-2 2026-08-15 < NA-1 2026-08-18 < APAC-EX-JP 2026-08-22 < EM 2026-08-25 < EU 2026-08-29 < JP 2026-09-01 — **NA-2 was the oldest**, so it was picked.

This was run as an **unattended scheduled routine** with no interactive user present.

---

## 0. Methodology

- **This run's stored automation prompt again described the routine as monthly ("first Saturday of the month") and referenced a removed `EODHD_API_KEY` "Path A."** Both are stale: EODHD was removed from the framework on 2026-06-19 ([decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), which explicitly says to treat that credential as compromised if it's ever needed again), and the actual, currently-configured cadence per [automation-schedule.md](../framework/automation-schedule.md) Routine 4 is **twice-weekly (Tuesday and Saturday)**. This exact discrepancy has already been identified and handled the same way in every NA-2/APAC-EX-JP/EM session since 2026-07-14 — followed the current, authoritative [screen.md](../.claude/commands/screen.md) / [automation-schedule.md](../framework/automation-schedule.md) instead of the stale prompt text, per CLAUDE.md's instruction to treat `framework/` as the source of truth. Ran the full 7-step Routine 4 (PR + issue + conditional `.ics` + Telegram summary), not the shorter step list in the stale prompt.
- **`yfinance`/direct Yahoo Finance was attempted first.** Not installed in this environment; after `pip install`, every live call failed with the same `curl_cffi` SSL `Connection reset by peer` error seen in every session since 2026-07-07. Confirmed genuine upstream block, not a data point to guess around.
- **Fell back to `stockanalysis.com`**, same source and two/three-page-per-candidate method (`/financials/`, `/financials/ratios/`, `/financials/balance-sheet/`) as every NA-2 round to date.
- **Candidate pool built via structural triage / domain knowledge, not the ETF-holdings fallback** — same call as every prior NA-2 round: MOAT/QUAL/QGRW/IQLT skew heavily tech/consumer (NA-1's territory), which doesn't fit NA-2's sector emphasis. Work was delegated across **4 parallel research agents** (quantitative data-pull only, not the qualitative pass — consistent with the batching policy in [new-position.md](new-position.md), which restricts *qualitative* subagent fan-out, not quantitative sourcing; prior EU/EM rounds used 4-5 parallel agents the same way).
- **Math check on 3yr revenue CAGR:** every CAGR figure below was independently recomputed by hand from raw annual revenue figures, not taken from any tool's own stated growth-rate summary — the same discipline established after the 2026-08-15 CBOE miscalculation was caught. All hand-checks this round confirmed the tool-extracted figures were consistent with the raw numbers (a few, e.g. GGG and ODFL, had non-monotonic revenue across the window, which is exactly the case this check exists to catch).

---

## 1. Candidate pool — this round's 12 new names + 6 refreshes

**Structural eliminations at Step 1** (one-line reasons, consistent with the exclusion categories established since the 2026-07-04 NA-2 round: banks, insurance underwriters, broker-dealers, commodity cyclicals, thin-margin distributors, regulated utilities, patent-cliff pharma):
- **TransDigm (TDG)** — aerospace-parts monopoly pricing power is real, but its capital structure is a chronic, structurally high-leverage LBO-era roll-up (historically 5-6x net debt/EBITDA) — not quantified, same treatment as excluding banks/insurers outright rather than spending a data-pull to confirm the obvious.
- **Pure-play E&P / midstream energy** (no specific tickers selected) — commodity-cyclical economics excluded per Step 1's standing rule; no Energy-sector candidate met even a plausible asset-light/moat bar this round. This is the fourth consecutive NA-2 round with no Energy candidate tested — flagged as a standing coverage gap on this slice, same as the standing Healthcare/Financials/Industrials emphasis to date.
- **Regulated utilities and most REITs** — excluded structurally (rate-regulated returns, capital-intensity) per the standing rule; **EQIX and DLR remain deferred** (need a bespoke REIT-adjacent framework not yet built), unchanged from prior rounds — no new Real Estate candidate added this round either, a second standing coverage gap on this slice.
- **Cencora/McKesson-style pharma distributors** — same thin-margin distribution economics that failed WSO (2026-08-15) and the NA-1 volume-retail exclusion; not quantified.

**18 valid candidates quantified** (12 fresh names + 6 refreshes of prior near-misses), spanning: Financials — SPGI, WTW, FI, CPAY (new), FDS, JKHY, AON, CBOE, CME (refreshes); Healthcare-adjacent — VEEV, CRL, CERT (new), DXCM (refresh); Industrials — WM, ODFL, ITW, MSA, GGG (new).

---

## 2. Quantitative Phase 01 gate (real, sourced data — stockanalysis.com, 2026-09-05)

Filters per [valuation-scoring.md](../framework/valuation-scoring.md): Gross margin >40%, Net margin >12%, ROIC >15%, Revenue 3yr CAGR >8%, FCF positive 3 consecutive years, Net Debt/EBITDA <2.5x, EV/EBIT <20x, FCF yield >4%.

| Ticker | Sector | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF (3yr+) | Net Debt/EBITDA | EV/EBIT | FCF Yield | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| SPGI | Financials (ratings/data) | 70.25% ✅ | 29.15% ✅ | 11.13% ❌ | 11.10% ✅ | + all 5yr ✅ | 1.43x ✅ | 20.52x ❌ | 4.26% ✅ | FAIL — ROIC and EV/EBIT (both narrow) miss |
| WTW | Financials (insurance brokerage) | 41.58% ✅ | 16.53% ✅ | 14.53% ❌ *(narrow)* | **3.07% ❌** *(FY24→FY25 revenue actually declined)* | + all 5yr ✅ *(FY24 net income was a −$98M loss — one-off, flagged)* | 1.93x ✅ | 15.23x ✅ | 5.43% ✅ | FAIL — ROIC narrowly misses; growth is the decisive, non-marginal miss |
| FI (Fiserv) | Financials (payments processing) | 59.36% ✅ | 16.42% ✅ | 6.85% ❌ | 6.11% ❌ | + all 5yr ✅ | 3.54x ❌ | 12.44x ✅ | 13.93% ✅ | FAIL — ROIC, growth, leverage all miss |
| **CPAY** (Corpay) | Financials (payments — commercial/fuel cards) | 79.68% ✅ | 23.59% ✅ | **14.55% ❌** *(narrow)* | 9.73% ✅ | + all 5yr ✅ | **2.70x ❌** *(narrow)* | 14.19x ✅ | 5.99% ✅ | **FAIL — a genuine 2-filter near-miss, both narrow** (ROIC 0.45pp short, leverage 0.20x over) |
| **FDS** (FactSet, refresh) | Financials (data/analytics) | 52.72% ✅ | 25.71% ✅ | 18.41% ✅ | **7.99% ❌** *(0.01–0.02pp short — essentially unchanged from 08-15's 7.98%)* | + all 5yr ✅ | 1.36x ✅ | 15.88x ✅ | 6.60% ✅ | **FAIL — still only Revenue 3yr CAGR misses, by the tightest margin on this slice** |
| **JKHY** (refresh) | Financials (bank/credit-union core software) | 43.90% ✅ | 19.76% ✅ | 22.68% ✅ | **6.98% ❌** *(~1.02pp short — essentially unchanged from 08-15's 6.93%)* | + all 5yr ✅ | 0.09x ✅ | 15.40x ✅ | 5.98% ✅ | **FAIL — still only Revenue 3yr CAGR misses, unchanged** |
| **AON** (refresh) | Financials (insurance brokerage) | 47.20% ✅ *(see quirk note below)* | 21.51% ✅ | 16.05% ✅ | 11.24% ✅ | + all 4yr ✅ | **2.51x ❌** *(0.01x short — still not cleared, was 2.52x on 07-25)* | 16.64x ✅ | 4.74% ✅ | **FAIL — still only Net Debt/EBITDA misses, tightest possible margin, unchanged** |
| **CBOE** (refresh) | Financials (exchange) | 51.53% ✅ | 23.22% ✅ | 22.72% ✅ | **5.99% ❌** *(confirmed unchanged from 08-15's hand-recomputed figure)* | + all 5yr ✅ | net cash ✅ | 17.33x ✅ | 6.40% ✅ | **FAIL — still only Revenue 3yr CAGR misses, confirmed unchanged** |
| **CME** (refresh) | Financials (exchange) | 100% ✅ *(asset-light, no COGS line — same quirk as ICE/MSCI/MCO/NDAQ)* | 61.80% ✅ | **11.78% ❌** | 9.04% ✅ *(now clears; was part of a 3-filter miss set previously)* | + all 5yr ✅ | net cash ✅ | **23.40x ❌** | 4.26% ✅ *(now clears)* | **FAIL — now a 2-filter miss (ROIC, EV/EBIT), improved from 3-filter: growth and FCF yield now pass** |
| VEEV | Healthcare-adjacent SaaS (life-sciences cloud) | 75.53% ✅ | 28.44% ✅ | 95.58%(FY)/363.83%(TTM, anomalous — flagged) ✅ | 14.02% ✅ | + all 5yr ✅ | net cash ✅ | **36.19x(current)/28.48x(FY) ❌** | 3.68%(TTM) ❌ / 4.13%(FY) ✅ *(period-ambiguous, flagged)* | FAIL — EV/EBIT is a clear, non-marginal miss regardless of period |
| CRL | Healthcare (contract research org.) | 34.98% ❌ | **−3.60% ❌** *(FY25 net loss, −$144.3M)* | 8.5% ❌ | 0.33% ❌ | + only 2 full FYs pulled (incomplete history, flagged) | 2.76–3.35x ❌ | 25–34x ❌ | 2.69% ❌ | FAIL — 6 of 8 filters miss; genuine fundamental deterioration, not a narrow miss |
| CERT | Healthcare-adjacent software (biosimulation) | 61.53% ✅ | −0.38% ❌ | −0.41–1.60% ❌ | **7.66% ❌** *(0.34pp short)* | + all 5yr ✅ | 1.20x ✅ *(net debt, corrected — see note)* | 66–74x ❌ | 6.64% ✅ | FAIL — net margin, ROIC, growth (narrowly), and EV/EBIT (badly) all miss |
| **DXCM** (refresh) | Healthcare (continuous glucose monitoring) | 60.10% ✅ | 17.94% ✅ | 44.49%(TTM, anomalous jump — flagged) ✅ | 16.98% ✅ | + all 4yr ✅ | net cash ✅ | **28.64x ❌** *(widened from a near-miss on 07-25 to a clear, non-marginal miss — EV/EBIT moved further from the bar, not closer)* | 4.24% ✅ *(thin, 0.24pp buffer)* | **FAIL — EV/EBIT is now a decisive miss, not a near-miss** |
| WM | Industrials (waste management) | 40.44% ✅ *(narrow)* | 10.74% ❌ | 11.17% ❌ | 8.57% ✅ | + all 5yr ✅ | 3.14x ❌ | 23.79x ❌ | 3.18%(FY)❌/4.08%(TTM)✅ *(mixed)* | FAIL — 4 filters miss (margin, ROIC, leverage, EV/EBIT) |
| ODFL | Industrials (LTL trucking/freight) | 38.95% ❌ *(narrow)* | 18.63% ✅ | 23.70% ✅ | **−4.25% ❌** *(revenue actually declined FY22→FY25)* | + all 5yr ✅ | 0.01x ✅ | 24.12x ❌ | 2.91% ❌ | FAIL — 4 filters miss, growth the most decisive |
| **ITW** | Industrials (diversified manufacturing) | 44.10% ✅ | 19.11% ✅ | 29.88% ✅ | **0.23% ❌** *(near-flat revenue)* | + all 5yr ✅ | 1.80x ✅ | 18.66x ✅ | **3.79% ❌** *(narrow, ~0.21pp short)* | **FAIL — a 2-filter miss, one of them narrow (FCF yield); 6 of 8 filters otherwise clear comfortably** |
| **MSA** (MSA Safety) | Industrials (safety equipment) | 46.46% ✅ | 14.87% ✅ | 19.00% ✅ | **7.06% ❌** *(0.94pp short)* | + all 3yr ✅ | 0.86x ✅ | 16.92x ✅ | 4.87% ✅ | **FAIL — only Revenue 3yr CAGR misses; tightest single-metric gap among this round's new names** |
| GGG (Graco) | Industrials (fluid handling equipment) | 52.45% ✅ | 23.33% ✅ | 24.71% ✅ | **1.43% ❌** *(6.57pp short — a large, non-marginal growth gap, non-monotonic revenue)* | + all 3yr ✅ | net cash ✅ | 19.37x ✅ *(thin buffer, passes only on live-price basis)* | 4.99% ✅ | FAIL — only Revenue 3yr CAGR misses, but by a wide margin (not a near-miss) |

**0 of 18 candidates clear the full Phase 01 gate this round** — no new qualified names. **FDS and AON remain (jointly) the tightest single-filter near-misses ever recorded on this slice** (FDS ~0.01–0.02pp short on Revenue 3yr CAGR; AON 0.01x short on Net Debt/EBITDA), both confirmed unchanged with fresh data. **CBOE and JKHY** are also clean single-filter misses (growth only), essentially unchanged. **MSA** is a new tight single-filter near-miss (Revenue 3yr CAGR, 0.94pp short). **CPAY** and **ITW** are new 2-filter near-misses with at least one narrow gap each. **CME** improved from a 3-filter to a 2-filter miss (growth and FCF yield now clear). **DXCM's** EV/EBIT gap widened materially, moving it out of near-miss territory.

---

## 3. Qualitative pass (Step 3)

**Not run — zero candidates cleared the quantitative gate this round**, so there is nothing to carry into the 5 qualitative questions. (Per Step 3, this step only applies to names that clear Step 2.)

---

## 4. Data gaps (Step 4)

- **VEEV:** ROIC shows a large, unexplained jump from FY2026's 95.58% to a "current"/TTM figure of 363.83% — flagged as a likely stub-period/annualization artifact on stockanalysis.com's end, not independently re-derived, and not carried forward as a trustworthy number (doesn't change the overall FAIL verdict, which rests on EV/EBIT). FCF yield is also period-ambiguous (3.68% TTM fails, 4.13% FY26 passes) — flagged rather than resolved by picking one silently.
- **DXCM:** ROIC similarly jumps from FY2025's 32.94% to a "current" 44.49% — flagged, not independently re-derived.
- **WTW:** FY2024 recorded a −$98M net loss (likely a one-off goodwill/impairment or divestiture charge) inside an otherwise-positive 5-year FCF history — noted for any future qualitative re-visit, though it doesn't change the decisive revenue-CAGR fail.
- **AON:** this round's fetch shows a conventional 47.20% gross margin (COGS line present), inconsistent with the 07-25 session's note of a "100% gross margin, no COGS line" service-model quirk. Flagged as an unreconciled discrepancy (possibly a stockanalysis.com presentation change) rather than silently resolved — moot for the pass/fail call either way since 47.20% clears the >40% bar.
- **CERT, JKHY:** the balance-sheet-page fetch initially returned a "net cash position" characterization with a negative dollar figure for both, but Total Debt minus Cash for both is actually positive (net debt). Corrected by cross-checking against each ticker's ratios-page Net Debt/EBITDA multiple (which is consistent with net debt, not net cash) — flagged as a raw-balance-sheet-page extraction artifact, not an invented number.
- **CRL:** only FY2024, FY2025, and TTM free cash flow were retrievable (no FY2021-23 annual FCF), so the "3 consecutive years positive" check is confirmed only for the years actually pulled (all positive) — not a full independent 3-year lookback. Moot for CRL's overall verdict since it fails 5 other filters outright.
- **ROIC methodology not independently re-derived, standing caveat as every prior NA-2 round:** all ROIC figures are stockanalysis.com's own calculation, not recomputed from raw NOPAT/Invested Capital per [quality-scoring.md](../framework/quality-scoring.md)'s definition.
- **FCF Yield definition not independently cross-checked for every ticker:** confirmed to equal FCF/Market Cap for FDS and DXCM (both matched stockanalysis.com's stated figure to 2-3 decimals); taken as-is from stockanalysis.com's own reported metric for the rest, since Market Cap wasn't separately pulled for every ticker.
- **CPAY's ratios-page "last updated" stamp (May 8, 2026) trailed its financials/balance-sheet pages (Jun 30, 2026 TTM)** — flagged as a mild staleness risk on CPAY's ROIC/EV-EBIT/Net-Debt-EBITDA figures specifically.
- **Standing gaps carried forward, unchanged:** EQIX, DLR remain deferred (no bespoke REIT-adjacent framework yet); no Energy-sector candidate has been tested in 4 consecutive NA-2 rounds (see Section 1); MASI (Masimo) remains excluded as delisted/acquired (Danaher, June 2026), not re-tested.

---

## 5. Coverage log update (Step 5)

[screening-coverage-log.md](../framework/screening-coverage-log.md)'s NA-2 row updated: Last screened → 2026-09-05. Qualified names found → 2 total, unchanged (Doximity DOCS from 07-04, Morningstar MORN from 08-15) — no new passes this round. Near-miss list refreshed: FDS and AON remain the tightest-ever single-filter misses on this slice (both confirmed essentially unchanged with fresh data); JKHY and CBOE also unchanged single-filter (Revenue 3yr CAGR) misses; MSA (new) is a tight single-filter Revenue-CAGR near-miss; CPAY (new) and ITW (new) are 2-filter near-misses with at least one narrow gap each; CME improved to a 2-filter miss (down from 3); DXCM's EV/EBIT gap widened out of near-miss territory. Sources used → stockanalysis.com (yfinance/Yahoo still blocked this session — `curl_cffi` SSL connection-reset, same failure mode as every session since 2026-07-07).

---

## Glossary

- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate between a start and end value.
- **EV/EBIT** — Enterprise Value ÷ EBIT, a multiple measuring how expensive a company is relative to its operating profit.
- **FCF (Free Cash Flow)** — cash a business generates after running/maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value); higher means cheaper.
- **Gross Margin** — Gross Profit ÷ Revenue; the share of each revenue dollar left after direct production/delivery costs.
- **LTL (Less-Than-Truckload)** — freight trucking model that combines multiple shippers' smaller loads onto one truck.
- **Net Debt/EBITDA** — net debt ÷ EBITDA, this framework's primary balance-sheet-leverage gate.
- **Net Margin** — Net Income ÷ Revenue; the share of each revenue dollar left as accounting profit after every expense.
- **Phase 01** — this framework's Universe Screening / quality-gate stage, the subject of this session.
- **Qualified Quality List** — the output of Phase 01 screening: companies that passed the quality gate and are eligible for Phase 02 valuation scoring.
- **ROIC** — Return on Invested Capital; how efficiently a company turns invested capital (debt + equity) into profit.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of financial results, as opposed to a fixed fiscal-year window.

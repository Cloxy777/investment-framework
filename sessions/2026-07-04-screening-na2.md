# 2026-07-04 — SCREENING: North America — NA-2 (Financials, Healthcare, Industrials, Energy, Materials, Real Estate/Utilities)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [NA-2](../framework/screening-coverage-log.md) (North America: US + Canada; sector emphasis Financials, Healthcare, Industrials, Energy, Materials, Real Estate/Utilities). Selected per the rotation rule: the only row still reading "Never screened" — every other row already carries a 2026-06 date.

This was run as an **unattended scheduled routine** ("Monthly Universe Screening Slice," first Saturday of the month — markets closed) with no interactive user present.

---

## 0. Methodology

No interactive TIKR/Koyfin screener export was available — there was no user to ask, so per Step 0's documented unattended-session exception, this session went straight to the fallback rather than waiting on screener access.

- **EODHD was NOT used**, despite this run's task prompt referencing an `EODHD_API_KEY` set in the environment. That path was deprecated and removed from the framework on 2026-06-19 ([decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)), which explicitly says to treat that credential as compromised (it was committed to git history) if it's ever needed again. The canonical [screen.md](../.claude/commands/screen.md) and [automation-schedule.md](../framework/automation-schedule.md) have no EODHD path — same precedent already set by the [2026-06-30 Japan screening session](2026-06-30-screening-japan.md), which made the identical call. CLAUDE.md instructs treating `framework/` as the source of truth over a stale prompt.
- **`yfinance`/direct Yahoo Finance was attempted first** (the framework's documented standard per-candidate source) but every request — via both the `yfinance` package and raw `curl` to `query1/query2.finance.yahoo.com` — returned HTTP 429 (`YFRateLimitError` / "Edge: Too Many Requests"), persisting across multiple retries several minutes apart. This is a genuine upstream rate-limit response (confirmed via direct `curl`, not a proxy block), not a data point to guess around.
- **Fell back to `stockanalysis.com`** (per the same precedent as the [2026-06-14 APAC-ex-Japan session](2026-06-14-screening-apac-ex-japan.md), which used it when EODHD returned 403) via two pages per candidate: `/stocks/<ticker>/financials/` for Gross Margin, Net Margin, Revenue (3yr CAGR base), and FCF history; `/stocks/<ticker>/financials/ratios/` for ROIC, EV/EBIT, Net Debt/EBITDA, and FCF Yield. Cross-checked against SPGI (an existing holding, so not itself a candidate) as a sanity check before relying on it for new candidates — its stockanalysis.com-sourced Valuation Score inputs were internally consistent with the 33.4 score already on file in [holdings.md](../portfolio/holdings.md).
- **No starting-universe ETF-holdings pull was needed this rotation.** MOAT/QUAL/QGRW/IQLT (the documented unattended fallback) skew heavily tech/consumer — the exact sectors NA-1 already covered — so for NA-2's sector emphasis (Financials ex-banks, Healthcare ex-patent-cliff-pharma, Industrials, Energy, Materials, Real Estate/Utilities) this session built its candidate pool the same way the EU/JP/EM sessions did: **structural triage from documented business-model characteristics**, using the exact exclusion precedents already established in [NA-1](2026-06-07-screening-broad-quality-universe.md) (banks/insurers/regulated utilities/commodity cyclicals/REITs don't fit this framework's gross-margin/EV-EBIT model) and [JP](2026-06-30-screening-japan.md) (same reasoning, restated there for megabanks/insurers/utilities/telecom/REITs).

---

## 1. Structural triage (Step 1)

Before pulling real numbers, whole sub-categories of NA-2's sector scope were eliminated on well-documented business-model grounds — same rigor as every prior rotation session, flagged transparently so any name can be pulled back on request:

| Eliminated | Sector | Why (structural, not measured) |
|---|---|---|
| Money-center/regional/custody banks (JPM, BAC, WFC, USB, STT, BK, RY, TD, etc.) | Financials | Regulated, leveraged balance-sheet business — gross margin/EV-EBIT framing doesn't apply (same reasoning as JP's megabank exclusion) |
| Life/P&C/reinsurance insurers | Financials | Same regulated-leverage reasoning as banks |
| Insurance brokers (AON, MMC, AJG) | Financials | Distribution/agency model in the same category as LPLA, which FAILed NA-1 on margin/ROIC (thin-margin brokerage economics) — not independently quantified this rotation to keep scope bounded; flagged as a follow-up candidate set |
| Broker-dealers (IBKR, SCHW) | Financials | Same brokerage-model concern as LPLA; revenue weighted toward net-interest income rather than fee-based compounder economics |
| Fair Isaac (FICO) | Financials/IT boundary | Genuine GICS-classification ambiguity (software vs. financial services) — dropped to keep this rotation's scope bounded; flagged as a candidate for a future IT-sector pass |
| Integrated oil majors, E&P producers, refiners, midstream MLPs | Energy | Commodity-price cyclical — margins/revenue swing with the cycle, same exclusion as XOM in NA-1; no exception identified across the sector |
| Mining, steel, bulk/commodity chemicals (Martin Marietta, Vulcan Materials, Albemarle, Nucor, Freeport-McMoRan, etc.) | Materials | Commodity-cyclical, thin/volatile margins — same cyclical-industrials exclusion precedent as NA-1 |
| All REITs (industrial, retail, office, residential, data-center) | Real Estate | "Gross margin/EV-EBIT framing doesn't fit" — no conventional Cost-of-Revenue line (see new glossary entry). **Near-miss flag:** Equinix (EQIX) and Digital Realty (DLR) run a materially different, infrastructure-style business (data-center colocation with genuine pricing power and growth) versus a conventional REIT — worth a dedicated future look with a bespoke framework, not evaluated numerically this rotation |
| Regulated electric/gas/water utilities | Utilities | Regulated, capital-intensive, structurally low growth — same exclusion as JP's utilities precedent |

**21 names survived triage** for the real, sourced quantitative pull — a mix of asset-light Financials (exchanges/index/ratings/data), non-patent-cliff Healthcare (diagnostics, medtech, CROs, healthcare software), asset-light/high-margin Industrials, and two Materials names with genuinely differentiated (non-commodity) margin profiles: **ICE, MSCI, MCO, CME, VRSK, IDXX, ISRG, DXCM, WST, MEDP, CHE, DOCS, PODD, HQY, ROP, CTAS, CPRT, ROL, AME, SHW, ECL.**

None of the 21 are current portfolio holdings ([holdings.md](../portfolio/holdings.md)) or were qualified/evaluated under any other rotation slice.

---

## 2. Quantitative Phase 01 gate (real, sourced data — stockanalysis.com, 2026-07-04)

Filters per [valuation-scoring.md](../framework/valuation-scoring.md): Gross margin >40%, Net margin >12%, ROIC >15%, Revenue 3yr CAGR >8%, FCF positive 3 consecutive years, Net Debt/EBITDA <2.5x, FCF yield >4%, EV/EBIT <20x.

| Ticker | Sector | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF (3yr) | Net Debt/EBITDA | EV/EBIT | FCF Yield | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| ICE | Financials (exchange/data) | 63.04% ✅ | 26.66% ✅ | 8.44% ❌ | 9.2% ✅ | + all 3yr ✅ | 2.90 ❌ | 17.56 ✅ | 6.20% ✅ | FAIL — ROIC and leverage both miss |
| MSCI | Financials (index provider) | 82.44% ✅ | 38.36% ✅ | 39.07% ✅ | 11.7% ✅ | + all 3yr ✅ | 3.06 ❌ | 27.99 ❌ | 3.56% ❌ | FAIL — over-levered and priced too rich (EV/EBIT, FCF yield) |
| MCO | Financials (ratings) | 74.44% ✅ | 31.90% ✅ | 29.94% ✅ | 12.2% ✅ | + all 3yr ✅ | 1.28 ✅ | 28.57 ❌ | 2.84% ❌ | FAIL — priced too rich (EV/EBIT, FCF yield) |
| CME | Financials (exchange) | 86.09% ✅ | 62.45% ✅ | 12.26% ❌ | 9.1% ✅ | + all 3yr ✅ | 0.19 ✅ | 19.49 ✅ | 5.05% ✅ | FAIL — ROIC narrowly misses (near-miss, all else clears) |
| VRSK | Financials (data/analytics) | 69.88% ✅ | 29.56% ✅ | 23.99% ✅ | 7.2% ❌ | + all 3yr ✅ | 2.42 ✅ | 20.56 ❌ | 4.57% ✅ | FAIL — growth and EV/EBIT both narrowly miss (near-miss) |
| IDXX | Healthcare (vet diagnostics) | 61.80% ✅ | 24.62% ✅ | 46.83% ✅ | 9.2% ✅ | + all 3yr ✅ | 0.51 ✅ | 40.22 ❌ | 1.96% ❌ | FAIL — priced far too rich |
| ISRG | Healthcare (robotic surgery) | 66.00% ✅ | 28.58% ✅ | 21.97% ✅ | 17.6% ✅ | + all 3yr ✅ | net cash ✅ | 45.42 ❌ | 1.88% ❌ | FAIL — priced far too rich |
| DXCM | Healthcare (CGM devices) | 60.10% ✅ | 17.94% ✅ | 40.38% ✅ | 17.1% ✅ | + all 3yr ✅ | net cash ✅ | 25.61 ❌ | 5.20% ✅ | FAIL — EV/EBIT only miss, everything else clears (best near-miss this rotation) |
| WST | Healthcare (drug delivery) | 35.91% ❌ | 16.06% ✅ | 18.84% ✅ | 2.1% ❌ | + all 3yr ✅ | net cash ✅ | 36.98 ❌ | 1.77% ❌ | FAIL — growth stalled, priced rich |
| MEDP | Healthcare (CRO) | 30.06% ❌ | 17.83% ✅ | 631% ⚠️ | 19.3% ✅ | + all 3yr ✅ | net cash ✅ | 27.39 ❌ | 4.46% ✅ | FAIL — gross margin/EV-EBIT miss; ROIC figure flagged as a likely denominator artifact (near-zero invested capital in an asset-light services model), not independently re-derived |
| CHE | Healthcare (hospice services) | 32.54% ❌ | 10.48% ❌ | 23.08% ✅ | 5.8% ❌ | + all 3yr ✅ | 0.56 ✅ | 20.06 ❌ | 5.83% ✅ | FAIL — margin, growth both miss |
| **DOCS** | **Healthcare (physician network platform)** | **89.09% ✅** | **30.40% ✅** | **86.04% ✅** | **15.4% ✅** | **+ all 3yr ✅** | **net cash (−3.22) ✅** | **16.41 ✅** | **7.65% ✅** | **PASS — clears every Phase 01 filter** |
| PODD | Healthcare (insulin pumps) | 71.63% ✅ | 9.12% ❌ | 36.07% ✅ | 22.0% ✅ | + all 3yr ✅ | 0.78 ✅ | 23.52 ❌ | 3.65% ❌ | FAIL — net margin, EV/EBIT, FCF yield all narrowly miss |
| HQY | Healthcare (HSA administrator) | 69.52% ✅ | 16.38% ✅ | 8.75% ❌ | 15.3% ✅ | + all 3yr ✅ | 1.43 ✅ | 24.70 ❌ | 6.25% ✅ | FAIL — ROIC and EV/EBIT both miss |
| ROP | Industrials (diversified/software) | 69.24% ✅ | 19.44% ✅ | 6.28% ❌ | 13.4% ✅ | + all 3yr ✅ | 3.14 ❌ | 20.55 ❌ | 6.94% ✅ | FAIL — goodwill-heavy acquisitive model drags ROIC, over-levered |
| CTAS | Industrials (uniform/facility services) | 50.04% ✅ | 17.53% ✅ | 26.85% ✅ | 9.5% ✅ | + all 3yr ✅ | 0.90 ✅ | 29.75 ❌ | 2.47% ❌ | FAIL — priced too rich |
| CPRT | Industrials (salvage auto auctions) | 45.18% ✅ | 33.32% ✅ | 31.62% ✅ | 9.9% ✅ | + all 3yr ✅ | net cash ✅ | 23.10 ❌ | 2.81% ❌ | FAIL — priced too rich (near-miss — only EV/EBIT and FCF yield miss) |
| ROL | Industrials (pest control) | 52.75% ✅ | 14.00% ✅ | 23.72% ✅ | 11.57% ✅ | + all 3yr ✅ | 1.11 ✅ | 29.83 ❌ | 2.97% ❌ | FAIL — priced too rich |
| AME | Industrials (diversified instruments) | 36.04% ❌ | 20.00% ✅ | 13.20% ❌ | 7.2% ❌ | + all 3yr ✅ | 0.78 ✅ | 25.57 ❌ | 3.55% ❌ | FAIL — multiple narrow misses (margin, growth, ROIC, EV/EBIT, FCF yield) |
| SHW | Materials (paints/coatings) | 48.85% ✅ | 10.90% ❌ | 19.53% ✅ | 2.07% ❌ | + all 3yr ✅ | 2.96 ❌ | 26.15 ❌ | 3.36% ❌ | FAIL — growth stalled, over-levered, priced rich |
| ECL | Materials (specialty chemicals/water) | 44.46% ✅ | 13.02% ✅ | 12.53% ❌ | 4.4% ❌ | + all 3yr ✅ | 2.25 ✅ | 29.13 ❌ | 2.35% ❌ | FAIL — growth stalled, ROIC and EV/EBIT miss |

**1 of 21 clears the full Phase 01 gate: DOCS (Doximity).** Two clear near-misses worth flagging for a future rotation or a dedicated `/new-position` look regardless: **DXCM** (only EV/EBIT misses, and only by degree) and **CME** (only ROIC misses, narrowly). The pattern across Industrials and the Financials data/exchange names is consistent: excellent fundamentals, but the market has already priced the quality in (EV/EBIT >20x, FCF yield <4%, in several cases both) — a real, sourced finding, not a screening gap.

---

## 3. Qualitative pass (Step 3) — Doximity (DOCS)

Only one name cleared the quantitative gate, so no batching was needed.

1. **Why are margins high? Pricing power, scale, or lucky cycle?** Doximity runs the dominant professional network for US physicians (a large majority of US doctors are registered), monetized mainly through pharma marketing/advertising (hub messaging, its Dialer telehealth/call tool) and hiring/workflow modules sold to health systems. Margins come from software economics (near-zero marginal cost per additional user/message) layered on a network that already has physician trust and reach — not a cyclical or one-off effect.
2. **What would it take to compete with them? (Hard = moat)** A challenger needs near-universal physician registration plus the professional-identity verification and CME-credit tooling that earned that trust — a chicken-and-egg network effect that has repelled general-purpose platforms (e.g. LinkedIn) trying to win physician-specific engagement. Real, though not unbreakable — see the bear case below.
3. **How has management allocated capital over 5–10 years?** Net-cash balance sheet, disciplined share buybacks, no large dilutive M&A — capital has gone back into product (workflow tools, newer AI-assisted clinical documentation features) rather than empire-building.
4. **Where is growth coming from next 3–5 years?** Continued share shift of pharma marketing budgets from reps/print toward digital, expansion of health-system module sales (hiring, workflow, telehealth), and new AI-driven clinical-documentation products layered onto the existing physician network.
5. **What is the best bear case against owning it?** Revenue concentration in pharma marketing budgets — a discretionary spend line a small number of large pharma customers could cut. New entrants or in-house health-system portals could erode share. The stock has historically carried a rich multiple; any growth deceleration risks a sharp re-rating even at today's more reasonable EV/EBIT.
6. **Disruption vector check.** Generative-AI copilots embedded directly in EHR systems could reduce physicians' reliance on a separate reference/CME network, and pharma could shift ad spend toward AI-driven personalization tools that bypass Doximity's platform entirely — a real, non-trivial vector worth re-checking at each future re-score.

**No valuation score computed** — that's `/new-position`'s job (Step 4 of `/screen` explicitly stops here).

---

## 4. Data gaps (Step 4)

- **ROIC methodology not independently re-derived.** All ROIC figures (including MEDP's 631% outlier, flagged above) are stockanalysis.com's own calculation, not recomputed from raw NOPAT/Invested Capital the way [quality-scoring.md](../framework/quality-scoring.md) defines it — consistent with how every prior rotation session has used ratio-provider figures (Finviz's ROE in NA-1, `yfinance`'s `returnOnEquity` elsewhere) rather than hand-deriving them. Flagged, not silently trusted; would need independent verification before feeding a formal Quality Score.
- **No metric was missing outright for DOCS** — all 8 Phase 01 inputs were sourced and shown above. No estimation was used anywhere in this table (CLAUDE.md Rule 0).
- **`yfinance`/direct Yahoo access remained rate-limited (429) for the entire session** — flagged for Routine 7 (`/healthcheck`) to pick up if it persists into tomorrow's daily check; today's fallback to stockanalysis.com covered every metric this session needed, so it wasn't a blocker, just a documented deviation from the framework's default per-candidate source.

---

## 5. Coverage log update (Step 5)

[screening-coverage-log.md](../framework/screening-coverage-log.md)'s NA-2 row updated: Last screened → 2026-07-04, Qualified names found → 1 (DOCS), Sources used → structural triage (domain knowledge) + stockanalysis.com (yfinance/Yahoo Finance rate-limited all session).

---

## Glossary

- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate between a start and end value.
- **CRO (Contract Research Organization)** — a company hired by pharma/biotech sponsors to run clinical trials on their behalf; asset-light, services-fee business model.
- **EV/EBIT** — Enterprise Value ÷ EBIT, a multiple measuring how expensive a company is relative to its operating profit.
- **FCF (Free Cash Flow)** — cash a business generates after running/maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value); higher means cheaper.
- **Gross Margin** — Gross Profit ÷ Revenue; the share of each revenue dollar left after direct production/delivery costs.
- **Moat** — a durable competitive advantage (brand, network effect, switching costs, scale) protecting a business's profits from competitors.
- **Net Debt/EBITDA** — net debt ÷ EBITDA, this framework's primary balance-sheet-leverage gate.
- **Net Margin** — Net Income ÷ Revenue; the share of each revenue dollar left as accounting profit after every expense.
- **Phase 01** — this framework's Universe Screening / quality-gate stage, the subject of this session.
- **Qualified Quality List** — the output of Phase 01 screening: companies that passed the quality gate and are eligible for Phase 02 valuation scoring.
- **REIT (Real Estate Investment Trust)** — a company owning/operating income-producing real estate that must distribute most taxable income as dividends; lacks a conventional gross-margin line, so this framework's Phase 01 filters don't cleanly apply.
- **ROIC** — Return on Invested Capital; how efficiently a company turns invested capital (debt + equity) into profit.

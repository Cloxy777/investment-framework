# 2026-07-18 — SCREENING: Europe (EU), Round 2 (deferred names)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [EU](../framework/screening-coverage-log.md) (UK, Eurozone, Switzerland, Nordics), all sectors. Unattended scheduled run (Routine 4 — Universe Screening Slice, markets closed). EU was the oldest "Last screened" row (2026-06-19, unchanged since), so it was picked again this rotation over NA-1/NA-2/JP/APAC-EX-JP/EM (all screened more recently).

This session **completes** the EU slice's first full pass by running the 11 names the [2026-06-19 EU session](2026-06-19-screening-europe.md) explicitly deferred, rather than re-verifying the 22 names already screened last month — same "find new names, don't re-cover familiar ones" rotation logic.

---

## ⚠️ Scheduled-prompt discrepancy flagged

The stored scheduled-task prompt for this run describes a **"Monthly Universe Screening Slice"** (first Saturday of the month) using **`EODHD_API_KEY`** for full automation ("Path A") per `.claude/commands/screen.md`. Neither of those is accurate against the current repo state:

- `automation-schedule.md` currently documents this as **Routine 4 — Twice-Weekly Universe Screening Slice** (Tuesday + Saturday, 14:00 UTC), not monthly.
- `.claude/commands/screen.md` has **no EODHD path at all** — Step 0's only automated option for an unattended run is the quality-factor-ETF-holdings fallback (MOAT/QUAL/QGRW/IQLT).
- [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md) records that EODHD was **removed** from every automation doc on 2026-06-19 — its free-tier screener endpoint was unreliable, and the `EODHD_API_KEY` committed to `.claude/settings.json` on 2026-06-13 was flagged as a **compromised, live credential** (checked into git history) to be rotated, not reused.
- Despite that, an `EODHD_API_KEY` **is** set in this session's environment. Given the removal decision explicitly called the prior key compromised, this session did **not** use it for anything, and did not use EODHD at all — proceeded instead with the current, documented process (structural triage + ETF-holdings-fallback framing + `yfinance`/web-sourced per-candidate verification). **Recommend the user check whether the scheduled-task prompt (cron config) for this routine was updated when the repo moved to the twice-weekly/no-EODHD process, and confirm whether the environment's `EODHD_API_KEY` is the old flagged-compromised key or a newly rotated one that should either be removed (if unused) or have the docs/automation updated to match.**

---

## Step 0 — Starting universe

No user available in this unattended run — per Step 0's exception, the starting universe is the previous EU session's deliberately-deferred candidate list (itself originally sourced from IQLT/structural-triage domain knowledge, same convention as the ETF-holdings fallback): **Nestlé (NESN.SW), Wolters Kluwer (WKL.AS), Dassault Systèmes (DSY.PA), EssilorLuxottica (EL.PA), Genmab (GMAB.CO), Demant (DEMANT.CO), Spirax Group (SPX.L), Geberit (GEBN.SW), Bureau Veritas (BVI.PA), Nemetschek (NEM.DE), Temenos (TEMN.SW)**.

**Data source:** `yfinance` tested at session start — confirmed network-blocked (`curl_cffi.requests.exceptions.SSLError: Connection reset by peer`), the same failure mode hit in the 2026-07-07/07-11 sessions. Used `stockanalysis.com` via WebFetch as the primary source instead, cross-checked with WebSearch where a figure looked inconsistent (flagged individually below). Research delegated to a subagent for the data-gathering step; numbers spot-checked directly against stockanalysis.com by the orchestrator (Genmab Net Debt/EBITDA, Nemetschek EV/EBIT current-vs.-FY2025) before being written up here.

## Step 1 — Structural triage

None of the 11 names were eliminated — all were deliberately deferred as plausible quality candidates last session, and none fits a hard structural exclusion (banks, insurers, commodity cyclicals, regulated utilities, thin-margin volume retail, patent-cliff pharma, airlines, telecom, REITs):

| Ticker | Company | Business model |
|---|---|---|
| NESN.SW | Nestlé | Branded packaged food/beverage manufacturer |
| WKL.AS | Wolters Kluwer | Professional information/software (legal, tax, health, compliance) |
| DSY.PA | Dassault Systèmes | Enterprise 3D design/PLM software (CATIA, SOLIDWORKS) |
| EL.PA | EssilorLuxottica | Vertically integrated eyewear manufacturer + optical retail |
| GMAB.CO | Genmab | Antibody biotech — royalty income + own pipeline |
| DEMANT.CO | Demant | Hearing-aid manufacturer + hearing-care retail/audiology clinics |
| SPX.L | Spirax Group | Specialty industrial engineering (steam systems, peristaltic pumps) |
| GEBN.SW | Geberit | Branded sanitary/plumbing systems manufacturer |
| BVI.PA | Bureau Veritas | Testing, inspection & certification (TIC) services |
| NEM.DE | Nemetschek | AEC (architecture/engineering/construction) design software |
| TEMN.SW | Temenos | Core banking software vendor (not a bank itself) |

One flag carried into Step 2 rather than an outright Step-1 elimination: **Genmab** — ~65% of its revenue is Darzalex royalties from J&J, and per Genmab's own SEC 20-F those royalty rights carry a biologics-exclusivity cliff starting in the late 2020s. That's economically a patent-cliff-pharma risk one layer removed (Genmab doesn't market the drug itself, so it survives Step 1 on a technicality) — treated as a qualitative red flag below rather than a structural exclusion.

## Step 2 — Quantitative Phase 01 gate

Filters: Gross margin >40% · Net margin >12% · ROIC>15% (ROE used as proxy where noted) · Revenue growth >8% (3yr CAGR) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x.

**Period basis:** margins, ROIC/ROE, and revenue CAGR use FY2025 (last completed fiscal year — operating fundamentals); Net Debt/EBITDA, FCF yield, and EV/EBIT use the current/live-price (TTM) column where available, per Rule 0 (live data for price-dependent metrics), else FY2025 is used and noted.

| Ticker | Gross M | Net M | ROIC/ROE | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA | FCF yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Nestlé | 45.83% ✅ | 9.02% ❌ | 10.46% ❌ | −1.75% ❌ | ✅ | 2.92× ❌ | 5.17% ✅ | 18.07× ✅ | **FAIL — 4/8** |
| Wolters Kluwer | 73.47% ✅ | 21.36% ✅ | 20.89% ✅ | 3.95% ❌ | ✅ | 1.83× ✅ | 6.82% ✅ | 13.84× ✅ | **FAIL — growth only (7/8)**, missed by 4.05pp |
| Dassault Systèmes | 83.73% ✅ | 19.05% ✅ | 14.81% ❌ | 3.25% ❌ | ✅ | net cash ✅ | 4.67% ✅ | 22.12× ❌ | **FAIL — 3/8** (ROIC missed by just 0.19pp) |
| EssilorLuxottica | 60.56% ✅ | 8.57% ❌ | 5.05% ❌ | 5.17% ❌ | ✅ | 1.67× ✅ | 4.91% ✅ | 25.37× ❌ | **FAIL — 4/8** |
| Genmab | 93.60% ✅ | 25.89% ✅ | 16.82% ✅ | 21.30% ✅ | ✅ | 2.88× ❌ | 5.85%/4.93%* ✅ | 13.09× ✅ | **FAIL — leverage only (7/8)**, missed by 0.38× ⚠️ see caveat |
| Demant | 75.62% ✅ | 10.30% ❌ | 10.88% ❌ | 5.25% ❌ | ✅ | 5.13× ❌ | 7.05% ✅ | 16.99× ✅ | **FAIL — 4/8** |
| Spirax Group | 15.59% ❌ ⚠️ | 9.61% ❌ | 10.15% ❌ | 1.87% ❌ | ✅ | 1.78× ✅ | 4.94% ✅ | 21.42× ❌ | **FAIL — 5/8** |
| Geberit | 73.64% ✅ | 18.90% ✅ | 27.42% ✅ | −2.30% ❌ | ✅ | 0.83× ✅ | 3.83% ❌ | 23.35× ❌ | **FAIL — 3/8** (FCF yield missed by 0.17pp) |
| Bureau Veritas | 29.12% ❌ ⚠️ | 8.80% ❌ | 20.63% ✅ | 5.74% ❌ | ✅ | 1.40× ✅ | 7.13% ✅ | 13.00× ✅ | **FAIL — 3/8** (growth missed by 2.26pp) |
| Nemetschek | 57.16% ✅ | 18.55% ✅ | 19.20% ✅ | 14.09% ✅ | ✅ | 0.14× ✅ | 6.02% ✅ | 20.73× ❌ | **FAIL — EV/EBIT only (7/8)**, missed by 0.73× |
| Temenos | 73.68% ✅ | 25.72% ✅ | 18.51% ✅ | 4.73% ❌ | ✅ | 1.66× ✅ | 6.18% ✅ | 24.12× ❌ | **FAIL — 2/8** (growth, EV/EBIT) |

\* Genmab FCF yield: subagent-sourced figure was 5.85%; orchestrator's own spot-check re-pull of the same stockanalysis.com page returned 4.93% (likely a same-day live-price/cache difference). Both clear the >4% bar, so the discrepancy doesn't change the verdict, but is flagged rather than silently reconciled.

**No name cleared all 8 filters this round.** Three near-misses (fail exactly 1 filter) flagged below.

### Data gaps / inconsistencies flagged (per CLAUDE.md Rule 0 — none estimated)

- **Spirax Group gross margin (15.59%)**: declined steadily from 23.87% (FY2021) — implausibly low for a specialty-engineering business. Could not independently verify against Spirax's own annual report (Macrotrends 403'd the cross-check). Doesn't change the verdict (fails 4 other filters regardless).
- **Bureau Veritas gross margin (29.12%)**: confirmed structural, not an error — TIC (testing/inspection/certification) businesses carry inspector/engineer labor costs (~50–55% of revenue) directly in cost of sales, mechanically capping gross margin well below product-company norms even with strong ROIC (20.63%), FCF yield (7.13%), and EV/EBIT (13.0×). **Worth a framework discussion**: should the >40% gross-margin Phase 01 filter be adapted for labor-based asset-light service models, the same way ROIC uses an ROE proxy when needed? Not changed here — flagging only, per Rule 0/no-black-box discipline; any filter change is a framework decision, not something this session session should adopt unilaterally.
- **Demant net margin (10.30%)**: includes a DKK −823m discontinued-operations charge in FY2025; underlying continuing-ops margin is likely materially higher but wasn't separately broken out on the fetched page. Doesn't change the verdict (leverage and ROIC also fail independently).
- **Genmab Net Debt/EBITDA (2.88×)**: confirmed real, not an artifact — driven by the **$8.0bn all-cash acquisition of Merus**, closed 2025-12-15 (adding petosemtamab, a late-stage, not-yet-FDA-approved bispecific antibody). This is a fresh, large, integration/clinical-risk-laden event, not a data error.
- **Nemetschek EV/EBIT (current 20.73× vs. FY2025 36.60×)**: confirmed via search, not an artifact — shares are down ~33–56% YTD 2026 despite continued double-digit growth and margin expansion, which is what compressed the multiple between the FY2025 print and the current live-price column.
- **Temenos gross margin (TTM 88.62% vs. FY2025 73.68%)**: the TTM figure on stockanalysis.com looked internally inconsistent with the FY series and couldn't be reconciled from the page alone — used the more reliable FY2025 figure (73.68%); Temenos clears the gross-margin filter either way, so the verdict is unaffected.
- **All UK-listed names (Spirax Group)**: same GBp/GBP unit-convention caveat noted in the 06-19 EU session applies — ratios unaffected (same normalized-source numerator/denominator), absolute figures should not be read at face value.

**Sources:** all stockanalysis.com `financials/ratios`, `financials/`, and `financials/cash-flow-statement/` pages per ticker (exchange codes: swx=Swiss, ams=Amsterdam, epa=Paris, cph=Copenhagen, lon=London, etr=Frankfurt/Xetra). Cross-checks: [Wolters Kluwer 2025 Full-Year Report](https://www.globenewswire.com/news-release/2026/02/25/3244280/0/en/wolters-kluwer-2025-full-year-report.html), [Genmab closes $8bn Merus acquisition](https://www.ddw-online.com/genmab-closes-its-8-billion-acquisition-of-merus-39501-202512/), [Genmab SEC 20-F (Darzalex royalty structure)](https://www.sec.gov/Archives/edgar/data/1434265/000155837025000846/gmab-20241231x20f.htm), [Bureau Veritas cost structure](https://moatsandmarkets.com/bureau-veritas/), [Nemetschek stock decline 2026](https://www.ad-hoc-news.de/boerse/news/ueberblick/nemetschek-s-stock-rout-continues-unabated-despite-dividend-hike-and/69438419).

## Step 3 — Qualitative pass

No name cleared all 8 filters, so **none formally qualifies** for the full qualitative pass (that gate exists precisely so a marginal business doesn't get scored just because it's interesting). Brief supplementary color on the three 1-filter near-misses, for the watchlist / next-rotation re-check — not a formal qualification:

**Wolters Kluwer (WKL.AS)** — fails growth only (3.95% vs. >8%). ~84–85% recurring revenue base, deep workflow integration into legal/tax/healthcare professional practices (CCH, UpToDate) — durable switching-cost moat, but structurally low-single-digit organic growth in a mature market. Growth miss is partly an FX artifact (constant-currency growth ~7% FY2025) but still misses the bar either way. Recent ROIC jump to 20.89% (from 14.3% FY2024) partly reflects a December-2025 divestiture (FRR) and should be re-verified next quarter rather than assumed as a new steady state.

**Genmab (GMAB.CO)** — fails Net Debt/EBITDA only (2.88× vs. <2.5×), but this is the least reassuring of the three: the leverage comes from an $8bn all-cash acquisition adding a not-yet-approved clinical asset, and ~65% of revenue is still Darzalex royalties carrying a biologics-exclusivity cliff starting late-2020s (flagged in Step 1). Recommend re-testing next quarter once Merus integration and post-deal leverage trajectory are clearer, not treating this as an imminent pass.

**Nemetschek (NEM.DE)** — fails EV/EBIT only (20.73× vs. <20×, closing fast). Top-3 global AEC software vendor (Allplan, Vectorworks, Bluebeam) with high switching costs from proprietary file formats; the EV/EBIT gap has compressed sharply as shares fell 33–56% YTD 2026 even as fundamentals improved — may already clear 20× by the next check. Competitive bear case: Autodesk is ~6× Nemetschek's revenue and dominant in BIM authoring (Revit/AutoCAD).

## ✅ Qualified Quality List — 0 names this round

No new PASSes. Combined with the 2026-06-19 session, the **EU slice's full first pass (33 names total)** now stands at:

- **2 clean passes** (unchanged): Experian (EXPN.L), Deutsche Börse (DB1.DE) — see [2026-06-19 session](2026-06-19-screening-europe.md) for full qualitative writeups; both already recommended for `/new-position`.
- **Near-misses (fail exactly 1 filter, watchlist, re-check next rotation or on a pullback/data refresh):** LVMH, SAP, RELX, Assa Abloy (from 06-19) **+ Wolters Kluwer, Genmab, Nemetschek (new this session)**.
- **Data-gap cases needing live `/new-position` resolution regardless:** Novo Nordisk, Adyen (from 06-19).

## Next steps

- No new `/new-position` candidates from this round (both clean EU passes were already surfaced last session).
- Watchlist re-check next EU rotation (or sooner on a pullback): Wolters Kluwer, Genmab (contingent on Merus integration clarity), Nemetschek (contingent on further multiple compression or a rebound).
- **Framework discussion flagged, not resolved here:** whether the >40% gross-margin Phase 01 filter needs a documented proxy/exception for labor-based TIC-style service models (Bureau Veritas is the clean example — fails only on gross margin and revenue growth, passes ROIC/FCF yield/EV/EBIT comfortably).
- **Automation-config discrepancy flagged, not resolved here:** see the box at the top of this session — the scheduled-task prompt for this routine describes a monthly/EODHD process that no longer matches the repo's documented twice-weekly/no-EODHD process.
- Coverage log updated below. EU's first full pass is now complete — no further deferred names remain for this slice.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate.
- **EV/EBIT** — Enterprise Value ÷ EBIT; how expensive a company is relative to operating profit, independent of capital structure.
- **FCF** — Free Cash Flow.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value); higher is cheaper.
- **Fast Grower** — a company growing EPS >15%/year for 3+ years (Lynch); this framework's trigger for the PEG sub-score (not reached this session, since no name passed Phase 01).
- **Gross Margin** — Gross Profit ÷ Revenue.
- **Moat** — a durable competitive advantage protecting a business's profits from competitors.
- **Net Debt/EBITDA** — leverage ratio; net debt ÷ EBITDA.
- **Net Margin** — Net Income ÷ Revenue.
- **ROE** — Return on Equity; Net Income ÷ shareholder equity.
- **ROIC** — Return on Invested Capital; a core quality signal in this framework.
- **TIC (Testing, Inspection & Certification)** — asset-light services industry (Bureau Veritas, SGS, Intertek) verifying products/facilities meet safety/quality/regulatory standards; labor-heavy cost structure mechanically compresses gross margin below product-company norms even with strong ROIC/cash generation.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported results.

# 2026-08-08 — SCREENING: Europe (EU), Round 3

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [EU](../framework/screening-coverage-log.md) (UK, Eurozone, Switzerland, Nordics), all sectors. Unattended scheduled run (no live user to ask questions of).

Verified against the current [screening-coverage-log.md](../framework/screening-coverage-log.md) before starting: EU's "Last screened" (2026-07-18) is still the single oldest date in the Rotation Matrix (NA-1 2026-07-28, NA-2 2026-07-25, JP 2026-07-21, APAC-EX-JP 2026-08-01, EM 2026-08-04 are all more recent) — no switch needed, EU is the correct slice for this round.

This round does **not** re-run the 33 names already covered across the [2026-06-19](2026-06-19-screening-europe.md) and [2026-07-18](2026-07-18-screening-europe.md) EU sessions. Instead it (1) re-checks the 7 flagged near-misses and (2) the 2 flagged data-gap cases from those two rounds with refreshed live numbers, and (3) adds a fresh pool of new European candidates not previously screened.

---

## Step 0 — Starting universe

No user available in this unattended run — per `screen.md` Step 0's documented exception, this session skips straight to the ETF-holdings-fallback-equivalent: structural-triage domain knowledge (the same convention used by every EU/APAC/EM session to date), rather than a live TIKR/Koyfin screener export.

**Candidate pool (18 names):**

1. **7 near-miss re-checks** (numbers/prices move quarter to quarter): LVMH (MC.PA), SAP (SAP.DE), RELX (REL.L), Assa Abloy (ASSA-B.ST), Wolters Kluwer (WKL.AS), Genmab (GMAB.CO), Nemetschek (NEM.DE).
2. **2 deferred data-gap cases**: Novo Nordisk (NOVO-B.CO), Adyen (ADYEN.AS).
3. **8 new European candidates** (structural triage from a longer 20-name idea list; see Step 1 for which were deferred/excluded): VAT Group (VACN.SW), Interroll Holding (INRN.SW), Partners Group (PGHN.SW), Rightmove (RMV.L), Games Workshop (GAW.L), Diploma (DPLM.L), Novonesis (NSIS-B.CO), IMCD (IMCD.AS).

**Data source tested at session start:** `pip install --quiet yfinance lxml` succeeded, but `yf.Ticker("SAP.DE").info` failed immediately with `curl_cffi.requests.exceptions.SSLError: Connection reset by peer` — the same network-blocked failure mode every EU/APAC/EM session has hit since 2026-07-07. Used **`stockanalysis.com` via WebFetch** instead (per-ticker `/financials/` and `/financials/ratios/` pages), cross-checked against WebSearch where a figure needed independent corroboration (flagged individually below).

---

## Step 1 — Structural triage

**Re-checks and data-gap cases (9 names):** all previously cleared structural triage in the 2026-06-19/2026-07-18 sessions — not re-derived here. One flag carried forward without re-deriving it: **Genmab** — ~65% of revenue is Darzalex royalties from J&J, and those royalty rights carry a biologics-exclusivity cliff starting in the late 2020s per Genmab's own SEC 20-F. This is economically patent-cliff-adjacent (Genmab doesn't market the drug itself, so it survives Step 1 on a technicality) — treated as a qualitative red flag in Step 3/near-miss commentary, not a hard Step-1 exclusion, matching round 2's treatment exactly.

**New candidates — starting idea list and triage disposition:**

| Company | Disposition | Reason |
|---|---|---|
| VAT Group | **Tested** | Semicap vacuum-valve maker — asset-light, high-margin, no hard exclusion |
| Interroll Holding | **Tested** | Material-handling components (conveyor rollers/drives) — niche industrial, no hard exclusion |
| Partners Group | **Tested** | Private-markets (PE/infrastructure/credit) alternative-asset manager — fee-based, no balance-sheet risk-taking like a bank/insurer, so doesn't fit the bank/insurer exclusion (same logic this framework already applies to insurance brokers Aon/MMC/AJG) |
| Rightmove | **Tested** | UK online property portal — asset-light two-sided marketplace, no hard exclusion |
| Games Workshop | **Tested** | Miniatures wargaming manufacturer + IP licensing — branded, high-margin manufacturing, not thin-margin volume retail |
| Diploma | **Tested** | Specialty technical distribution (seals, controls, life sciences) — no hard exclusion, though see Step 2 gross-margin flag |
| Novonesis | **Tested** | Industrial biotech (enzymes, microbial solutions) — no hard exclusion |
| IMCD | **Tested** | Specialty chemical distribution — no hard exclusion, though see Step 2 gross-margin flag |
| Sika, Straumann, Halma, Coloplast | **Excluded — already covered** | All 4 already quantitatively screened (and failed) in the 2026-06-19 round-1 session; re-testing would defeat the "find new names" rotation logic |
| Lonza Group | **Deferred, not tested** | Capital-intensive CDMO (bioreactor buildout) — plausible candidate, out of this round's scope |
| Amplifon | **Deferred, not tested** | Hearing-aid retail/audiology chain — borderline specialty-retail model, out of scope this round |
| Kerry Group | **Deferred, not tested** | Food ingredients/flavors manufacturer — out of scope this round |
| DSV | **Deferred, not tested** | Freight forwarding — capital-intensive, structurally thin operating margins on largely pass-through revenue; likely a difficult gross-margin fit (same pattern this round's IMCD/Diploma results confirm for distribution-type models), lower priority to test |
| Croda International | **Deferred, not tested** | Specialty chemicals — recent (2023–2024) margin pressure, out of scope this round |
| Rotork | **Deferred, not tested** | Industrial flow-control actuators — plausible candidate, out of scope this round |
| Ambu | **Deferred, not tested** | Single-use endoscope medtech — still mid-turnaround on margins, out of scope this round |
| Beijer Ref | **Deferred, not tested** | HVAC/refrigeration wholesale distribution — same thin-margin-distribution concern as DSV, lower priority to test |
| Indutrade | **Deferred, not tested** | Decentralized industrial-components acquirer (Constellation-Software-style roll-up) — plausible candidate, out of scope this round |

None of the 8 new names tested hit a hard Step-1 exclusion (no banks/insurers, commodity cyclicals, regulated utilities, thin-margin volume retail, patent-cliff pharma, airlines, telecom, or REITs among them).

---

## Step 2 — Full Phase 01 quantitative gate

Filters: Gross margin >40% · Net margin >12% · ROIC >15% (ROE proxy acceptable if noted) · Revenue growth >8% (3yr CAGR) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x.

**Period basis (same convention as the 2026-07-18 round):** margins, ROIC/ROE, and revenue CAGR use **FY2025** (last completed fiscal year — operating fundamentals); Net Debt/EBITDA, FCF yield, and EV/EBIT use the **current/live-price (TTM, as of 2026-08-07)** column, per Rule 0 (live data for price-dependent metrics).

### 2a. Near-miss re-checks (7 names)

| Ticker | Gross M (FY25) | Net M (FY25) | ROIC/ROE (FY25) | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA (current) | FCF yield (current) | EV/EBIT (current) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| LVMH | 66.24% ✅ | 13.89% ✅ | ROE 16.24% ✅ (ROIC 11.67% ❌, see flag) | 0.68% ❌ | ✅ | 1.00× ✅ | 6.07% ✅ | 15.65× ✅ | **FAIL — growth only (7/8)** |
| SAP | 73.76% ✅ | 19.46% ✅ | ROIC 16.82% ✅ | 7.63% ❌ | ✅ | net cash (−0.14×) ✅ | 4.25% ✅ | 18.58× ✅ | **FAIL — growth only, by 0.37pp (7/8)** |
| RELX | 66.29% ✅ | 21.53% ✅ | ROE 70.51% ✅ | 3.89% ❌ | ✅ | **2.64× ❌** (FY25: 2.23× ✅, see flag) | 6.23% ✅ | 17.47× ✅ | **FAIL — growth + leverage (6/8)** ⚠️ worsened |
| Assa Abloy | 42.63% ✅ | 9.65% ❌ | ROE 14.09% ❌ / ROIC 10.05% ❌ | 8.06% ✅ | ✅ | 2.18× ✅ | 5.30% ✅ | 18.97× ✅ | **FAIL — net margin + ROIC/ROE (6/8)** ⚠️ worsened |
| Wolters Kluwer | 73.47% ✅ | 21.36% ✅ | ROIC 20.89% ✅ ⚠️ divestiture-boosted | 3.95% ❌ | ✅ | 1.79× ✅ | 8.90% ✅ | 10.99× ✅ | **FAIL — growth only, by 4.05pp (7/8)** |
| Genmab | 93.60% ✅ | 25.89% ✅ | ROIC 16.82% ✅ (current TTM ROIC 12.07% ❌, see flag) | 21.30% ✅ | ✅ | 2.73× ❌ | 4.77% ✅ | 16.49× ✅ | **FAIL — leverage only (7/8)** |
| Nemetschek | 57.16% ✅ | 18.55% ✅ | ROIC 19.20% ✅ | 14.10% ✅ | ✅ | 0.40× ✅ | 5.19% ✅ | **22.21× ❌** | **FAIL — EV/EBIT only (7/8)**, wider miss than round 2 |

### 2b. Data-gap re-checks (2 names)

| Ticker | Gross M (FY25) | Net M (FY25) | ROIC/ROE (FY25) | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA (current) | FCF yield (current) | EV/EBIT (current) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **Novo Nordisk** | 82.41% ✅ | 33.14% ✅ | ROIC 42.60% ✅ | 20.43% ✅ | ✅ all 3yr positive | 1.25× ✅ | **5.62% ✅** | 8.95× ✅ | **✅ PASS — all 8 filters (data gap resolved)** |
| Adyen | 100.00% ✅ ⚠️ (service business, no separate COGS) | 44.94% ✅ | ROE 22.33% ✅ / ROCE 22.47% ✅ | **21.09% ✅** (data gap resolved) | ✅ | net cash (−8.49×) ✅ | 3.09% ❌ | 16.93× ✅ | **FAIL — FCF yield only (7/8)** |

### 2c. New candidates (8 names)

| Ticker | Gross M (FY25) | Net M (FY25) | ROIC/ROE (FY25) | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA (current) | FCF yield (current) | EV/EBIT (current) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| VAT Group | 63.52% ✅ | 19.96% ✅ | ROIC 23.53% ✅ | −2.11% ❌ | ✅ | 0.92× ✅ | 1.26% ❌ | **76.14× ❌** | **FAIL — 3/8** (growth, FCF yield, EV/EBIT) |
| Interroll Holding | 66.81% ✅ | 10.88% ❌ | ROIC 19.87% ✅ | −8.19% ❌ | ✅ | −2.19× (net cash) ✅ | 4.65% ✅ | 14.24× ✅ | **FAIL — net margin + growth (6/8)** |
| **Partners Group** | 68.18% ✅ | 49.19% ✅ | ROIC 47.96% ✅ | 11.05% ✅ | ✅ | 0.30× ✅ | 7.98% ✅ | 13.65× ✅ | **✅ PASS — all 8 filters** |
| **Rightmove** | 100.00% ✅ ⚠️ (asset-light portal, no COGS) | 51.06% ✅ | ROE 266.08% ✅ ⚠️ (ROIC 656.40%, both distorted by near-zero capital base) | 8.53% ✅ | ✅ | net cash (−0.13×) ✅ | 6.81% ✅ | 11.94× ✅ | **✅ PASS — all 8 filters** |
| Games Workshop | 72.06% ✅ | 31.76% ✅ | ROIC 101.45% ✅ ⚠️ (minimal capital base) | 14.17% ✅ | ✅ | −0.54× (net cash) ✅ | **3.78% ❌** (FY25: 4.42% ✅) | **22.23× ❌** (FY25: 19.01× ✅) | **FAIL — FCF yield + EV/EBIT, both current-basis-only (6/8)** ⚠️ borderline, see flag |
| Diploma | 18.61% ❌ | 12.17% ✅ | ROIC 15.31% ✅ | 14.61% ✅ | ✅ | 1.33× ✅ | 2.60% ❌ | **34.79× ❌** | **FAIL — gross margin + FCF yield + EV/EBIT (5/8)** |
| Novonesis | 53.91% ✅ | 14.04% ✅ | **ROIC 4.88% ❌** | 20.86% ✅ ⚠️ merger-inflated | ✅ | 3.53× ❌ | 3.15% ❌ | 36.04× ❌ | **FAIL — ROIC, leverage, FCF yield, EV/EBIT (4/8)** |
| IMCD | 24.98% ❌ | 4.55% ❌ | ROIC 7.82% ❌ | 1.27% ❌ | ✅ | 2.94× ❌ | 6.23% ✅ | 19.53× ✅ | **FAIL — gross margin, net margin, ROIC, growth, leverage (3/8)** |

---

## ✅ Qualified Quality List — 3 new names this round

**Novo Nordisk (NOVO-B.CO)**, **Partners Group (PGHN.SW)**, and **Rightmove (RMV.L)** all clear the full 8-filter Phase 01 gate. Combined with the 2 existing qualifiers, the **EU slice now has 5 qualified names on file**: Experian (EXPN.L), Deutsche Börse (DB1.DE), Novo Nordisk (NOVO-B.CO), Partners Group (PGHN.SW), Rightmove (RMV.L).

### Step 3 — Qualitative pass (the 3 new PASSes)

Per new-position.md's batch-processing policy, this Step 3 pass was done sequentially in the orchestrator's own reasoning (no subagents needed for a 3-name qualitative writeup, per the task's explicit instruction).

#### Novo Nordisk (NOVO-B.CO)

1. **Why are margins high?** Global leader in GLP-1 diabetes/obesity drugs (semaglutide: Ozempic, Wegovy, Rybelsus) — patent-protected molecules, a first-mover oral Wegovy pill (launched Jan 2026), and a century of insulin/diabetes-care manufacturing scale and payer relationships.
2. **What would it take to compete?** A rival needs its own approved, differentiated GLP-1/dual-agonist molecule (multi-year, multi-billion-dollar late-stage trial program) plus manufacturing scale for injectable/oral biologics-adjacent production — Eli Lilly (tirzepatide/Mounjaro/Zepbound) has cleared that bar and is the only credible peer; no other company has.
3. **Capital allocation (5–10yr):** Heavy reinvestment in GLP-1 fill-finish manufacturing capacity funded from internally generated cash, consistent dividend growth, opportunistic bolt-on M&A in diabetes/obesity-adjacent assets, and active IP defense (suing Eli Lilly in July 2026 over allegedly misleading comparative-efficacy advertising).
4. **Where's growth coming from (3–5yr)?** Oral Wegovy pill ramp (2 million prescriptions in Q1 2026, though Q2 fell just short of estimates), continued international obesity-drug rollout, and the pipeline beyond semaglutide.
5. **Best bear case:** Losing share to Lilly's tirzepatide/Zepbound on efficacy, now compounded by Lilly's own oral-GLP-1 candidate ("Foundayo"); US list-price cuts (Wegovy pill priced $149–299/month) are compressing realized pricing industry-wide; the CagriSema pipeline candidate underperformed tirzepatide in a head-to-head Type 2 diabetes trial, raising pipeline-execution doubts. The shares are down ~70% from their mid-2024 peak — direct, well-documented evidence of exactly this repricing (cross-checked via [TIKR: "Novo Nordisk Has Fallen 56% From Its High"](https://www.tikr.com/blog/novo-nordisk-has-fallen-56-from-its-high-is-nvo-finally-cheap-enough-to-buy-in-2026) and Gurufocus, which independently puts current EV/EBITDA 51% below its 10-year median).
6. **Disruption vector:** Real and *present*, not a hypothetical 5-year-out risk — this is an active two-horse (Lilly/Novo) efficacy and pricing race playing out in real time, and multiple developers besides Lilly are pursuing oral small-molecule GLP-1s that could commoditize the category further.

**Reason for the mispricing:** the market has re-rated Novo Nordisk hard (EV/EBIT compressed from 10.2× in the 2026-06-19 session to 8.95× now) on real, documented competitive and pipeline setbacks — not a data artifact. That repricing is precisely what pushed FCF yield from 2.23% (round 1's only failing filter) to 5.62% today, resolving the data gap as a genuine pass rather than a data-quality fix.

#### Partners Group (PGHN.SW)

1. **Why are margins high?** Fee-based alternative-asset-management model (management fees on $186B AUM as of 30 June 2026, plus performance fees) — no balance-sheet risk-taking like a bank/insurer, high operating leverage since incremental AUM adds little incremental headcount, and long-duration locked-up private-markets fund structures (typically 8–12yr) reduce redemption risk relative to a mutual-fund manager.
2. **What would it take to compete?** A decades-long track record and deep LP (limited partner — institutional investor) relationships to raise successive fund vintages, plus a global deal-sourcing network across private equity, infrastructure, real estate, and private credit — the private-markets industry has consolidated around a small number of scaled platforms (Blackstone, KKR, Partners Group, etc.) built up over decades, not something a new entrant replicates quickly.
3. **Capital allocation (5–10yr):** 17 consecutive years of dividend increases (CHF 46.00/share proposed for FY2025), a newly launched "Total Return Strategy" income vehicle (mid-teens target return, 5–8% yield) diversifying beyond traditional drawdown funds, and reinvestment concentrated in deal-sourcing/underwriting talent rather than empire-building M&A.
4. **Where's growth coming from (3–5yr)?** Targeting AUM growth to $450B by 2033 from $186B today — a record $16B of fresh capital commitments in H1 2026 alone — plus expansion into evergreen/semi-liquid private-markets vehicles aimed at the wealth-management channel, a structural industry-wide growth vector (the "democratization" of private markets).
5. **Best bear case:** Performance fees (targeted at 25–40% of revenue) are inherently cyclical and tied to realized fund exits — guided to land at the *low end* of that range for 2026, and a trade-press report flagged evergreen-vehicle outflows alongside the AUM headline, worth monitoring. Private-markets exit conditions (IPO/M&A activity) directly drive realization timing and therefore performance-fee recognition.
6. **Disruption vector:** Low near-term — private-markets fundraising and deal execution are relationship/track-record businesses, not easily disintermediated by new technology. The more relevant long-term risk is fee compression as the industry scales and LPs negotiate harder, not a new delivery mechanism displacing the model outright.

**Reason for the mispricing:** EV/EBIT of 13.65× and a 7.98% FCF yield for a business compounding AUM at double-digit rates with 48% ROIC looks cheap relative to its own growth — likely reflects generalist-investor caution around private-markets managers' cyclical performance-fee exposure and 2026's guided low-end performance-fee mix, rather than any deterioration in the core fee-earning franchise.

#### Rightmove (RMV.L)

1. **Why are margins high?** UK's dominant online property portal — asset-light (subscription fees from estate agents/new-home developers for listings, no inventory, minimal physical capex) with the highest visitor traffic of any UK property-search site, creating a two-sided network effect: more listings attract more buyers/renters, which attracts more agents.
2. **What would it take to compete?** A new entrant must simultaneously win over both estate agents (who pay to list) and home-searchers (who visit to browse) — a classic chicken-and-egg two-sided-market problem. The UK has effectively had the same 2–3 incumbent portals (Rightmove, Zoopla, OnTheMarket) for over a decade despite well-funded challenges — OnTheMarket was explicitly agent-backed to unseat Rightmove and never did.
3. **Capital allocation (5–10yr):** Consistent, large share buybacks and dividend growth given minimal reinvestment needs of the asset-light model; management rebuffed four separate takeover approaches from Rupert Murdoch's REA Group (Australia's dominant portal, majority-owned by News Corp) through 2024, up to a final rejected bid implying ~781p/share plus a special dividend — judged the standalone business worth more than the offer ([The Daily Upside](https://www.thedailyupside.com/industries/media-entertainment/murdochs-rea-group-abandons-takeover-bid-for-rightmove/)).
4. **Where's growth coming from (3–5yr)?** Continued ARPA (average revenue per advertiser) growth from richer agent data/marketing packages, expansion into new-homes and commercial-property adjacent verticals, and mortgage/financial-services lead-generation cross-sell.
5. **Best bear case:** UK housing-transaction volumes (and therefore agent listing budgets) are cyclical and rate-sensitive. A well-capitalized strategic acquirer has already shown willingness to pay a large premium for the business, meaning some of today's "cheap" entry point may reflect deal-failure-risk being priced back out rather than pure organic mispricing. The UK's Competition and Markets Authority has a standing interest in dominant online-marketplace practices, given Rightmove's outright category leadership.
6. **Disruption vector:** Moderate, monitored — a scaled property portal is defensible but not immune to a well-funded structural challenger (as REA's repeated approaches demonstrated, via M&A rather than organic competition). AI-driven property search/agents bypassing traditional portals is a plausible multi-year vector worth tracking, though no incumbent has yet meaningfully disrupted a scaled portal business anywhere globally.

**Reason for the mispricing:** EV/EBIT of 11.94× for a near-monopoly, ~100%-gross-margin UK portal with a stable net-cash balance sheet looks anomalously cheap in isolation — plausibly explained by residual investor caution after the year-long REA/News Corp takeover saga (deal-failure-risk repricing) and UK housing-cycle sentiment rather than any franchise deterioration; the extreme ROE/ROIC figures (266%/656%) reflect a near-zero invested-capital base from years of buybacks, not a data error, and should be read qualitatively rather than compared directly against businesses with a normal capital base.

**Conclusion:** All three are genuine additions to the qualified list — a repriced GLP-1 pharma leader (Novo Nordisk), a scaled private-markets fee compounder (Partners Group), and a near-monopoly UK property portal (Rightmove) — each clearing all 8 filters with real, sourced numbers, not data patches. **Recommend `/new-position NOVO-B` (or `NVO`), `/new-position PGHN`, and `/new-position RMV`** for full Phase 02 scoring with live pricing.

---

## Step 4 — Data gaps and inconsistencies flagged (per CLAUDE.md Rule 0 — none estimated)

- **RELX Net Debt/EBITDA**: current/TTM (2.64×) is *worse* than the FY2025 year-end figure (2.23×) — a genuine change, not extraction noise (both come from the same ratios table, computed consistently with every other name here). Not investigated further this session; worth checking RELX's H1 2026 results for a debt-funded buyback or acquisition before the next rotation.
- **Assa Abloy ROIC/ROE**: both dropped below the 15% bar this round (ROE 14.09%, ROIC 10.05%) versus round 1's ROE of 15.04% (barely passing) — a real deterioration in return metrics, not a data artifact; worth a closer look at margin/capital-intensity trend before the next rotation.
- **Genmab ROIC**: FY2025 (16.82%, used for the verdict per this session's period-basis convention) diverges sharply from the current/TTM figure (12.07%) — consistent with the Merus acquisition (closed 2025-12-15) diluting near-term invested-capital returns before the acquired asset earns its way in. Flagged, not used to change the verdict.
- **Rightmove and Games Workshop ROE/ROIC**: both show triple-digit percentages (Rightmove ROE 266%/ROIC 656%; Games Workshop ROIC 101%) — confirmed as a real artifact of a near-zero invested-capital/book-equity base after years of aggressive buybacks, not a sourcing error; both companies' >15% pass is not in doubt regardless of which exact figure is used.
- **Rightmove TTM net margin**: the ratios extraction returned 24.40% for the TTM column, inconsistent with the raw TTM revenue/net-income figures on the same page (218.37/439.25 = 49.71%) and with FY2025's 51.06% — treated as a same-page extraction inconsistency; used the FY2025 figure, cross-checked against the recomputed TTM figure, which agree.
- **IMCD TTM gross margin**: extraction returned 13.30% for the TTM column, inconsistent with FY2021–FY2025's tight 24–25% band — treated as an extraction artifact; used FY2025 (24.98%), which does not change IMCD's verdict (fails 5/8 regardless).
- **Diploma FY2021 gross margin (36.63%)**: inconsistent with the FY2022–FY2025 range (14–19%) — likely a reporting-basis change (Diploma's own reported "gross profit" may have been redefined around the FY2022 transition); does not change the verdict, since Diploma fails the >40% gross-margin filter on every year in the FY2022–FY2025 range regardless.
- **Games Workshop FCF yield and EV/EBIT — current vs. FY2025 basis disagree on the verdict**: current/TTM shows FCF yield 3.78% (❌) and EV/EBIT 22.23× (❌), while FY2025 (fiscal year ended ~June 2025) shows 4.42% (✅) and 19.01× (✅) — i.e. Games Workshop would have cleared all 8 filters on a FY2025-basis reading. This isn't a data error; it reflects the stock trading up and trailing earnings dipping slightly between the FY2025 print and today. Used the current/TTM basis per this session's stated convention (consistent with every other price-dependent metric here), but flagging this explicitly as the closest borderline case in the whole pool — worth a very close re-check next rotation or on any pullback.
- **VAT Group EV/EBIT — current (76.14×) vs. FY2025 (43.49×)**: a large divergence, most likely explained by continued AI-capex-driven semicap-sector re-rating (the same phenomenon flagged for AI-capex-adjacent NA-1 names — LRCX/AMAT/KLAC/ANET — in the 2026-07-28 session). Not investigated further, since VAT fails on growth and FCF yield independently of this figure.
- **Adyen and Rightmove gross margin (100.00%)**: both are asset-light service/platform businesses where stockanalysis.com's "Gross Profit" line simply equals total revenue (no separately reported cost-of-goods-sold) — flagged as a labeling convention, not a real 100% margin in the traditional sense, consistent with the same flag raised for Adyen in round 1.
- **Novonesis revenue 3yr CAGR (20.86%)**: inflated by the November 2023 Novozymes/Chr Hansen merger roughly doubling the revenue base between FY2023 and FY2024 (2,402 → 3,834 EUR M) — not organic growth. Flagged; doesn't change the verdict, since Novonesis fails 3 other filters (ROIC, leverage, EV/EBIT) independently, all plausibly tied to the same not-yet-fully-digested merger.

---

## Step 5 — Coverage log updated

See [screening-coverage-log.md](../framework/screening-coverage-log.md) — EU row's "Last screened" bumped to 2026-08-08, "Qualified names found" updated to 5 total (Experian, Deutsche Börse, **Novo Nordisk, Partners Group, Rightmove — all 3 new this round**), and "Sources used" appended with this round's methodology summary.

---

## Next steps

- `/new-position NOVO-B` (Novo Nordisk, NOVO-B.CO / NVO) — full Phase 02 scoring with live price; note the framework already holds prior NVO sessions per the glossary's GLP-1 entry — reconcile against any existing position/watchlist state before proceeding.
- `/new-position PGHN` (Partners Group, PGHN.SW) — full Phase 02 scoring with live price.
- `/new-position RMV` (Rightmove, RMV.L) — full Phase 02 scoring with live price.
- Watchlist re-check next EU rotation (near-misses, fail exactly 1 filter): **SAP, Wolters Kluwer, Genmab, Nemetschek, LVMH** (LVMH only if ROE, not ROIC, is used as the metric — flag this explicitly if re-tested), **Adyen** (FCF yield only, now with the growth data gap fully resolved as a clean pass).
- Watchlist — worsened to 2-filter fails this round, still worth tracking given how recently they were single-filter misses: **RELX** (growth + leverage), **Assa Abloy** (net margin + ROIC/ROE).
- Watchlist — borderline/basis-dependent, closest re-check candidate in the whole pool: **Games Workshop** (fails FCF yield + EV/EBIT on current/TTM basis only; would have cleared all 8 on a FY2025 basis).
- Deferred, not yet quantitatively screened (candidates from this round's idea list not tested for scope reasons): Lonza Group, Amplifon, Kerry Group, DSV, Croda International, Rotork, Ambu, Beijer Ref, Indutrade.
- Coverage log updated below. Per the rotation rule, the next-oldest slice after this update will be **JP (Japan, last screened 2026-07-21)** — confirm against the live coverage log at that time in case another slice has since aged further.

---

## Glossary

- **AUM (Assets Under Management)** — the total market value of client capital a fund manager or private-markets firm manages on clients' behalf; the primary scale metric for an asset manager like Partners Group.
- **CAGR** — Compound Annual Growth Rate.
- **CMA (Competition and Markets Authority)** — the UK's competition/antitrust regulator, with a standing interest in dominant online-marketplace practices such as Rightmove's category leadership.
- **EV/EBIT** — Enterprise Value ÷ EBIT; how expensive a company is relative to operating profit, independent of capital structure.
- **FCF** — Free Cash Flow.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value); higher is cheaper.
- **GLP-1 (Glucagon-Like Peptide-1)** — a hormone that stimulates insulin release and suppresses appetite; "GLP-1 drugs" (Novo Nordisk's semaglutide-based Ozempic/Wegovy, Eli Lilly's tirzepatide-based Mounjaro/Zepbound) mimic it to treat diabetes and obesity.
- **Gross Margin** — Gross Profit ÷ Revenue.
- **LP (Limited Partner)** — an institutional or high-net-worth investor who commits capital to a private-markets fund (private equity, infrastructure, credit) without taking part in day-to-day fund management, in exchange for a share of the fund's returns.
- **Moat** — a durable competitive advantage protecting a business's profits from competitors.
- **Net Debt/EBITDA** — leverage ratio; net debt ÷ EBITDA.
- **Net Margin** — Net Income ÷ Revenue.
- **Patent cliff** — the steep drop in a drugmaker's revenue when a blockbuster drug's patent or regulatory exclusivity expires and generic/biosimilar competition enters; this framework's structural Step-1 exclusion for pharma names overly reliant on one soon-to-expire asset.
- **ROE** — Return on Equity; Net Income ÷ shareholder equity.
- **ROIC** — Return on Invested Capital; a core quality signal in this framework.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported results.

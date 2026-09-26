# 2026-09-26 — SCREENING: Japan (JP) — Round 5 (fresh candidate pool)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [JP](../framework/screening-coverage-log.md) (Japan, all sectors). Selected per the rotation rule: oldest "Last screened" date in the matrix (2026-09-01, ahead of NA-2 09-05, NA-1 09-08, APAC-ex-JP 09-12, EM 09-15, EU 09-22).

This was run as an **unattended scheduled routine** (Routine 4, twice-weekly universe screening slice — see [automation-schedule.md](../framework/automation-schedule.md)) with no interactive user present.

The four prior JP sessions ([2026-06-30](2026-06-30-screening-japan.md), [2026-07-21](2026-07-21-screening-japan.md), [2026-08-11](2026-08-11-screening-japan.md), [2026-09-01](2026-09-01-screening-japan.md)) together screened 61 distinct tickers across three prior candidate pools. This session builds a **fresh 15-name candidate pool** (1 structurally excluded, 14 quantitatively tested) from sectors/niches not yet covered in JP — fintech/accounting SaaS, smaller-cap gaming publishers, niche medtech-device manufacturers, online marketplaces, and semiconductor-equipment component suppliers — rather than re-testing already-screened names.

---

## 0. Methodology and stale-instruction flags

- **The scheduled task prompt for this run again referenced the deprecated `EODHD_API_KEY`-based "Path A" automation and a "monthly" cadence.** Both are stale, per the same standing issue flagged in every JP-adjacent session since 2026-06-30 (this is at least the sixth consecutive occurrence): EODHD was removed from the framework on 2026-06-19 ([decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)), which instructs treating that exact credential as **compromised** if it's ever needed again — it was **not used**. The actual configured cadence per [automation-schedule.md](../framework/automation-schedule.md) Routine 4 is **twice-weekly (Tuesday and Saturday)** — today (2026-09-26) is a Saturday, consistent with the real cadence, not the stale "first Saturday of the month" text. Per CLAUDE.md, `framework/` (the current, canonical [screen.md](../.claude/commands/screen.md) and automation-schedule.md) is the source of truth over a stored scheduler prompt. **Recommend the automation owner update the scheduler's stored prompt text directly** — this has now been re-flagged in six straight sessions without the underlying prompt being fixed.
- **Step 0/1**: no interactive TIKR/Koyfin screener session was available (unattended run) — went straight to the documented unattended-session exception. Continued the same **structural-triage-from-domain-knowledge** approach the four prior JP rounds used (built around sectors not yet tested in this slice), rather than the literal ETF-holdings fallback (MOAT/QUAL/QGRW/IQLT), which would mostly resurface the same large-cap names already covered in Round 1. **Flagging prominently per the task's Step 0 instruction: this manual/structural-triage sourcing approach — like the ETF-holdings fallback it substitutes for — has the same fundamental limitation of missing names that a live TIKR/Koyfin screener export would surface systematically; it is not a substitute for that screener access.**
- **Step 2 data source**: `python -m scripts.fetch_fundamentals` (the documented yfinance wrapper) was tried first per the current automation-schedule.md text. It worked for a liquid large-cap sanity check (7203.T Toyota, not part of this round's pool) but **failed with `MissingInputError: yfinance field missing from TTM EBIT` on all 14 of this round's smaller/mid-cap candidates** (plus one `marketCap`/`forwardPE`-missing case) — yfinance's `quarterly_financials` simply doesn't populate an "EBIT" row for these tickers, a genuine field-coverage gap, not a rate limit this time. Per Rule 0 / the script's own documented behavior, this is the "flag the gap, don't estimate" signal — rather than guess at EBIT, fell back to `stockanalysis.com` (via WebFetch: `/financials/ratios/`, `/financials/`, `/financials/cash-flow-statement/` pages per ticker, exchange code `tyo`), the same fallback used in every JP/EU/NA/APAC/EM session since 07-07. Work was delegated across **4 parallel research agents** (batches of 3-4 tickers each), consistent with the batch-processing policy referenced in screen.md.
- **All 3-year revenue CAGRs were independently recomputed by each research agent from raw annual revenue figures**, per the standing process note added in the 2026-09-01 session (a WebFetch-summarization arithmetic error was caught that round) — every CAGR below is shown with its own arithmetic, not a page-stated growth %.
- **A ticker-identity mismatch was caught and not silently resolved**: the candidate pool intended "Works Human Intelligence Group" at 4373.T, but stockanalysis.com's own quote page for TYO:4373 identifies that ticker as **Simplex Holdings, Inc.** (an IT-solutions/systems-consulting company), not Works Human Intelligence. The research agent could not confirm a verified ticker for Works Human Intelligence Group and did not guess one. **Simplex Holdings' data is reported below under its real name** — treat it as Simplex Holdings, not Works Human Intelligence, and resolve/re-source Works Human Intelligence's correct ticker (if it has one) before any future round.
- **A second recurring data-quality issue surfaced**: on two tickers (Asahi Intecc 7747.T, Rorze 6323.T) the `financials/cash-flow-statement/` page's own "Net Income" row diverged materially from the `financials/` (income-statement) page's Net Income for every year except the most recent — likely a different net-income definition (e.g., pretax/pre-minority-interest) rather than an extraction error, since it recurred consistently in both cases. **Not used for any filter** — margins and FCF were taken from internally self-consistent figures (margin % × revenue reproduces the stated net income; OCF − Capex = FCF exactly) instead. Flagged for future sessions sourcing these two tickers, or others from the same page family.

### Structurally excluded (Step 1, before any quantitative pull)

| Ticker | Company | Why excluded |
|---|---|---|
| 4819.T | Digital Garage Inc | Internet/fintech holding company whose reported earnings blend operating-business results with gains/losses on a venture-equity investment portfolio — the same blended-conglomerate/investment-holding exclusion logic used for Sony Group/Panasonic Holdings (08-11) and Konami Group (09-01) in prior JP sessions |

### Candidate pool this round (14 names, after the above exclusion)

| Ticker | Company | Sector |
|---|---|---|
| 4478.T | freee K.K. | Cloud accounting/HR SaaS |
| 4373.T | *(intended: Works Human Intelligence — see mismatch flag; actual: Simplex Holdings, Inc.)* | IT solutions/systems consulting |
| 4443.T | Sansan, Inc. | Business-card/sales-intelligence SaaS |
| 3994.T | Money Forward, Inc. | Fintech/accounting SaaS |
| 2412.T | Benefit One Inc | Corporate benefits outsourcing platform |
| 7844.T | Marvelous Inc | Video games/content IP |
| 3668.T | Colopl Inc | Mobile gaming |
| 7747.T | Asahi Intecc Co | Medical devices (catheters/guidewires) |
| 7716.T | Nakanishi Inc | Dental/medical precision equipment |
| 2371.T | Kakaku.com Inc | Online price-comparison/marketplace platform |
| 6323.T | Rorze Corporation | Semiconductor wafer-handling automation robots |
| 4385.T | Mercari Inc | C2C e-commerce marketplace |
| 6383.T | Daifuku Co | Material-handling/logistics automation |
| 4686.T | Justsystems Corp | Software (ATOK input engine, Ichitaro, enterprise document mgmt) |

---

## Step 2 — Quantitative Phase 01 gate (real, sourced data — stockanalysis.com, pulled 2026-09-26)

Filters: Gross margin >40% · Net margin >12% · ROIC>15% · Revenue growth >8% (3yr CAGR, independently recomputed) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x. The **current/TTM** column was used as the primary basis for margin/ROIC/leverage/valuation figures.

| Company (Ticker) | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA | FCF yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **Rorze Corporation (6323.T)** | 41.57% ✅ ⚠️ narrow | 16.55% ✅ | 26.04% ✅ | 10.87% ✅ | ✅ (FY24-26) | -1.38× ✅ | 4.13% ✅ ⚠️ narrow | 18.54× ✅ | **PASS — 8/8** ✅ |
| Simplex Holdings (4373.T) *(see identity flag)* | 44.28% ✅ | 17.32% ✅ | 17.83% ✅ | 18.9% ✅ | ✅ (5 yrs) | 0.71× ✅ | 3.44% ❌ | 18.31× ✅ | **FAIL — FCF yield only (7/8)** ⚠️ near-miss (-0.56pp) |
| Justsystems Corp (4686.T) | 80.35% ✅ | 29.95% ✅ | 550.44% ✅ ⚠️ very high | 7.09% ❌ | ✅ (5 yrs) | -4.66× ✅ | 6.70% ✅ | 7.26× ✅ | **FAIL — Rev CAGR only (7/8)** ⚠️ near-miss (-0.91pp) |
| Asahi Intecc Co (7747.T) | 70.45% ✅ | 22.06% ✅ | 27.30% ✅ | 17.31% ✅ | ✅ (5 yrs) | -1.03× ✅ | 3.55% ❌ | 18.61× ✅ | **FAIL — FCF yield only (7/8)** ⚠️ near-miss (-0.45pp) |
| Marvelous Inc (7844.T) | 38.82% ❌ ⚠️ narrow | 7.51% ❌ | 29.07% ✅ | 14.4% ✅ | ✅ (FY22-24) | -2.76× ✅ | 32.99% ✅ | 5.12× ✅ | **FAIL — 6/8** (Gross M near-miss + Net M) |
| Daifuku Co (6383.T) | 25.28% ❌ | 12.12% ✅ ⚠️ narrow | 28.12% ✅ | ~8.85% ✅ ⚠️ FY-end-change caveat | ✅ | -1.88× ✅ | 3.05% ❌ | 17.31× ✅ | **FAIL — 6/8** (Gross M + FCF yield near-miss) |
| Mercari Inc (4385.T) | 73.66% ✅ | 15.44% ✅ | 15.77% ✅ ⚠️ narrow | 10.04% ✅ | ❌ (never positive in 5yr window) | 1.93× ✅ | -1.82% ❌ | 15.75× ✅ | **FAIL — 6/8** (FCF-3yr + FCF yield, both outright) |
| Sansan Inc (4443.T) | 87.91% ✅ | 12.61% ✅ ⚠️ narrow | **data gap** ⚠️ | 28.2% ✅ | ✅ (5 yrs) | -3.72× ✅ | 3.65% ❌ | 27.39× ❌ | **FAIL — 6/8 confirmed + 1 indeterminate** (FCF yield near-miss, EV/EBIT, ROIC unscored) |
| Kakaku.com Inc (2371.T) | 27.35% ❌ ⚠️ data anomaly, see note | 18.89% ✅ | 78.59% ✅ | 15.7% ✅ | ✅ (5 yrs) | -1.27× ✅ | 3.08% ❌ | 26.56× ❌ | **FAIL — 5/8** (Gross M + FCF yield near-miss + EV/EBIT) |
| Nakanishi Inc (7716.T) | 56.47% ✅ | 2.51% ❌ | 5.08% ❌ | 18.59% ✅ | ✅ (6 yrs) | -1.03× ✅ | 3.52% ❌ | 13.71× ✅ | **FAIL — 5/8** (Net M, ROIC — both FY2025-net-loss-driven — + FCF yield near-miss) |
| freee K.K. (4478.T) | 81.05% ✅ | 2.54% ❌ | 4.30% ❌ ⚠️ ROCE proxy | 30.2% ✅ | ❌ (only 2 consec.) | -8.82× ✅ | 0.42% ❌ | 200.65× ❌ | **FAIL — 3/8** |
| Colopl Inc (3668.T) | 28.45% ❌ | 7.95% ❌ | 9.01% ❌ | -7.3% ❌ (declining) | ✅ (3 consec.) | -28.85× ✅ ⚠️ | 0.69% ❌ | 1.68× ✅ ⚠️ | **FAIL — 3/8** |
| Money Forward Inc (3994.T) | 68.85% ✅ | 7.73% ❌ | -2.34% ❌ | 32.8% ✅ | ❌ (never 3 consec.) | 0.35× ✅ | 2.37% ❌ | not meaningful ❌ (neg. EBIT) | **FAIL — 3/8** |
| Benefit One Inc (2412.T) | — | — | — | — | — | — | — | — | **N/A — delisted May 2024** (Dai-ichi Life Holdings acquisition); removed from active screening universe |

---

## ✅ Qualified Quality List — 1 new name

### Rorze Corporation (6323.T) — passes 8/8

Founded 1980, headquartered in Hiroshima, Japan — a leading global supplier of automation systems for the semiconductor and flat-panel-display industry: atmospheric and vacuum wafer-handling robots, aligners, load ports, EFEMs/sorters, stockers, and mask/reticle-handling systems. Clears every filter, though **2 of 8 filters pass narrowly** (Gross margin 41.57% vs. the 40% bar; FCF yield 4.13% vs. the 4% bar) — flagged as worth re-verifying at the next data refresh, consistent with how the framework flagged CPRT's narrow FCF-yield pass on the NA-1 slice.

### Near-misses flagged for the watchlist (fail only 1 filter)

- **Simplex Holdings, Inc. (4373.T)** — passes 7/8, fails only FCF yield (3.44% vs. >4%, a 0.56pp miss). **Caveat: this ticker was intended to be "Works Human Intelligence Group" in the candidate brief but is actually Simplex Holdings per stockanalysis.com's own listing** — an IT-solutions/systems-consulting company, not an HR/payroll SaaS vendor. Treat this near-miss as belonging to Simplex Holdings; Works Human Intelligence's correct ticker (if listed) remains unresolved and should be re-sourced before any future round references it.
- **Asahi Intecc Co (7747.T)** — passes 7/8, fails only FCF yield (3.55% vs. >4%, a 0.45pp miss). World-leading medical guidewire/catheter manufacturer (70.45% gross margin, 22.06% net margin, 27.30% ROIC, net-cash balance sheet, 17.31% revenue CAGR) — quality is unambiguous, priced slightly too richly on a cash-flow basis right now.
- **Justsystems Corp (4686.T)** — passes 7/8, fails only Revenue 3yr CAGR (7.09% vs. >8%, a 0.91pp miss). Japanese software company (ATOK input engine, Ichitaro word processor, enterprise document/content management) with an unusually high 550.44% ROIC — flagged as a genuinely sourced but very small-invested-capital-base outlier, not a data error.

No other candidate came within 1 filter of qualifying. Two names deserve a standing note for 2-filter misses with a narrow component: **Marvelous Inc (7844.T)** fails Gross margin by only 1.18pp (38.82% vs. 40%) alongside a wider Net margin miss — worth re-checking if margins recover from the FY2024-25 dip; **Daifuku Co (6383.T)** fails Gross margin outright (systems-integrator hardware economics, 25.28%) but its FCF yield miss is narrow (3.05% vs. 4%, a 0.95pp gap), and its data series carries a fiscal-year-end-change caveat (Mar→Dec transition in 2024) that affects the CAGR calculation's precision.

---

## Step 3 — Qualitative pass (Rorze Corporation, the 1 clean PASS)

Handled directly (1 name, within the "small batch, no subagent needed" threshold per [new-position.md](../.claude/commands/new-position.md)'s batch-processing policy referenced in [screen.md](../.claude/commands/screen.md) Step 3).

### Rorze Corporation (6323.T)

1. **Why are margins high?** Rorze designs and manufactures the precision robotics (wafer-handling arms, aligners, load ports, EFEMs/sorters) that move silicon wafers inside semiconductor fabs without contamination or breakage — a specialized, IP-protected niche within the broader fab-equipment supply chain where reliability and sub-micron precision command a real engineering premium over generic industrial robotics. 41.57% gross margin is real but only narrowly above this framework's 40% bar, and TTM net margin (16.55%) recently compressed from Q2 2025's 23% to Q2 2026's 17% on higher expenses — a real, sourced signal that pricing power here is good but not unlimited.
2. **What would it take to compete?** A rival needs years of qualification cycles with fab customers (semiconductor tool qualification is notoriously slow and conservative — fabs rarely swap a proven wafer-handling supplier mid-process) plus the vacuum/cleanroom engineering expertise to avoid particle contamination that ruins wafers; Rorze faces established competitors (Daihen Corp, Nidec Corp, Brooks Automation, Yaskawa, Kawasaki Heavy Industries) in a market Rorze holds "lion's share" of alongside those names, not a monopoly — a live patent dispute (Kawasaki Heavy Industries vs. Rorze Corporation, in U.S. federal court) underscores that IP boundaries in this space are actively contested, not settled.
3. **Capital allocation (5-10yr):** Conservative shareholder-return posture — ¥17/share dividend, ~0.7% yield, only a 16% payout ratio (9% on a cash basis) — consistent with a reinvestment-heavy strategy funding continued R&D and capacity for the current AI/semiconductor-capex upcycle rather than aggressive buybacks or high payout. No confirmed buyback program found in this pass.
4. **Where's growth coming from (3-5yr)?** The broader semiconductor-equipment capex supercycle: TSMC, Samsung, and other foundries are expanding advanced-node and AI-chip capacity aggressively (TSMC alone held ~73% of Q2 2026 foundry share with CoWoS advanced-packaging lines reported fully booked into 2027), and every incremental wafer fab built or expanded needs wafer-handling automation — a direct, structural tailwind for Rorze's core business, though this pass did not find Rorze-specific order/backlog disclosure confirming customer-level demand.
5. **Best bear case:** Q2 2026 already shows the risk in miniature — revenue grew only 5.2% YoY while net income fell 21% and margin compressed from 23% to 17% on rising expenses, meaning even in an up-cycle, cost growth can outpace revenue growth. Semiconductor capital equipment is a famously cyclical, capex-driven end market: a downturn in fab construction (which has happened repeatedly in this industry's history) would hit order volume directly, and Rorze's own two of eight passing filters (gross margin, FCF yield) are narrow enough that a modest deterioration would flip this name back to a FAIL.
6. **Disruption vector:** Low-to-moderate. Wafer-handling automation is a durable, structurally necessary part of semiconductor manufacturing — not a category at risk of software-style disruption — but it is fully exposed to the cyclicality and customer-concentration risk inherent in supplying a small number of very large fab operators (TSMC, Samsung, and similar), and a live IP dispute with a major competitor (Kawasaki Heavy Industries) is worth monitoring for any outcome that could constrain Rorze's product line.

**Sources:** [Rorze Corp company profile — stockanalysis.com](https://stockanalysis.com/quote/tyo/6323/company/), [Wafer Handling Robots Market — competitor list](https://www.verifiedmarketresearch.com/blog/top-wafer-handling-robot-manufacturers/), [Kawasaki Jukogyo Kabushiki Kaisha v. Rorze Corporation — CourtListener](https://www.courtlistener.com/opinion/9612267/kawasaki-jukogyo-kabushiki-kaisha-v-rorze-corporation/), [Rorze Q2 2026 earnings/dividend — Digrin](https://www.digrin.com/stocks/detail/6323.T/earnings), [TSMC Q2 2026 foundry share/CoWoS booking — BigGo Finance](https://finance.biggo.com/news/56363fff-cb20-4342-98df-488964d16ab2)

**Conclusion:** A genuine niche-quality business (specialized semiconductor wafer-handling automation, real IP-protected engineering moat, net-cash balance sheet) trading at a reasonable 18.54× EV/EBIT and riding a structural AI/semiconductor-capex tailwind — but two of its eight passing filters are narrow, and Q2 2026's margin compression (23%→17% YoY) is a real signal worth re-checking at the next refresh, not dismissed. **Recommend `/new-position Rorze` (6323.T)** for full Phase 02 scoring with live pricing, flagging the narrow-pass filters and the recent margin trend for extra scrutiny at that stage.

---

## Data gaps flagged (per CLAUDE.md Rule 0 — none estimated)

- **4373.T ticker-identity mismatch (material)**: the candidate brief intended "Works Human Intelligence Group" at this ticker; stockanalysis.com identifies 4373.T as **Simplex Holdings, Inc.** instead. No verified ticker for Works Human Intelligence Group was found — not guessed. All data reported under 4373.T in this session belongs to Simplex Holdings.
- **`fetch_fundamentals.py` / yfinance — systemic EBIT-field gap on this round's pool**: all 14 candidates hit `MissingInputError` on `quarterly_financials` lacking an "EBIT" row (one also missing `marketCap`, one missing `forwardPE`) — a genuine field-coverage gap for these tickers in yfinance 0.2.66, not a rate limit. Flagged rather than worked around by estimating EBIT from other line items; fell back to stockanalysis.com per the established JP-slice process instead.
- **Sansan Inc (4443.T) — ROIC**: blank/dash on the source ratios page for the current period and every year except FY2022 (58.23%, too stale to use as "current"). Left unscored rather than assumed pass or fail — Sansan is otherwise a 6/8 confirmed name, so this gap is the deciding factor between a possible 7/8 near-miss and a confirmed 6/8 FAIL; worth re-sourcing from a primary filing (EDINET/company IR) before this name is referenced again.
- **Kakaku.com Inc (2371.T) — annual Gross Profit data anomaly**: the source's annual income-statement columns (FY2022-FY2026) show Gross Profit exactly equal to Revenue (implying a 100% margin) for every year, inconsistent with the TTM column's distinct, plausible figure (27.35%). Re-fetched twice to confirm this wasn't a one-off summarization error — it persisted. Only the TTM figure was used; the annual 100%-margin figures were not used anywhere.
- **Daifuku Co (6383.T) — fiscal-year-end transition**: Daifuku changed its fiscal year-end from March to December during 2024, producing overlapping/restated columns both labeled "FY2024." The 3-year revenue CAGR calculation spans roughly 3.75 elapsed years rather than a clean 3 as a result — reported with this caveat attached rather than silently treated as a standard 3-year window.
- **Asahi Intecc (7747.T) and Rorze (6323.T) — cash-flow-page Net Income mismatch**: on both tickers, the `financials/cash-flow-statement/` page's own "Net Income" row diverges from the `financials/` (income-statement) page's Net Income for every year but the most recent, likely a different net-income definition (pretax/pre-minority-interest). Not used for any filter; margins/FCF were computed from internally self-consistent figures instead (documented in each research agent's report). Flagged as a standing data-quality note for future sessions sourcing either ticker.
- **Money Forward Inc (3994.T) — EV/EBIT not directly published**: omitted by the source page because TTM operating income is negative; computed manually from sourced EV/EBIT components (≈ -263×) and treated as a FAIL on economic substance rather than left unscored, since a negative-EBIT company cannot clear a "<20x" valuation gate under any reasonable interpretation.
- **Benefit One Inc (2412.T) — delisted**: confirmed via a JPX delisting notice that Benefit One became a wholly-owned subsidiary of Dai-ichi Life Holdings and was delisted from the TSE around May 2024. No financial-statement pages remain on stockanalysis.com; recommend removing 2412.T from the active screening universe going forward rather than re-testing it in a future JP round.

---

## Next steps

- **One `/new-position` candidate from this rotation: `/new-position Rorze` (6323.T)** — full Phase 02 valuation scoring with live pricing, with extra scrutiny on the two narrow-pass filters (gross margin, FCF yield) and the Q2 2026 margin-compression trend flagged in the qualitative pass.
- Watchlist (no formal entry created by `/screen`; re-check on next JP rotation or a fresher print): **Simplex Holdings (4373.T)** — FCF yield only, 3.44% vs. >4% (0.56pp short) — note the identity-mismatch caveat above before acting on this; **Asahi Intecc (7747.T)** — FCF yield only, 3.55% vs. >4% (0.45pp short); **Justsystems (4686.T)** — Revenue 3yr CAGR only, 7.09% vs. >8% (0.91pp short).
- **Remove Benefit One Inc (2412.T) from the active screening universe** — confirmed delisted (Dai-ichi Life Holdings acquisition, ~May 2024).
- **Resolve Works Human Intelligence Group's correct TSE ticker** (if it has one) before it's referenced again in a future JP candidate pool — 4373.T is Simplex Holdings, not Works Human Intelligence.
- Standing note carried forward: Japan's highest-quality asset-light franchises across all five JP rounds so far (Keyence, Advantest, Disco, Tokyo Electron from Round 1; Sanrio, Rakus from Round 3; BayCurrent Consulting from Round 4) keep clearing quality/growth filters but fail specifically on valuation (FCF yield, EV/EBIT) — **Rorze Corporation now joins the small group of names that clear valuation too**, though narrowly.
- **Process flag for the automation owner (sixth consecutive occurrence):** the scheduled Routine 4 prompt still references a monthly cadence and the deprecated EODHD `Path A` automation, despite the actual configured cadence being twice-weekly (Tuesday/Saturday) per `automation-schedule.md`. Recommend updating the scheduler's stored prompt text directly rather than continuing to re-flag it per run.
- Deferred for a future JP deep-dive (not yet screened in any of the 5 rounds): remaining smaller gaming publishers beyond Nexon/Capcom/Marvelous/Colopl now tested; Works Human Intelligence Group once its correct ticker is confirmed; further semiconductor-equipment component suppliers beyond Rorze (e.g. peers named as Rorze's competitors — Daihen Corp, Nidec Corp — not yet independently screened on this slice).
- Coverage log updated below.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **EBIT** — Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit.
- **EV** — Enterprise Value — a company's total value to all capital providers: market cap + debt − cash.
- **EV/EBIT** — Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to their operating profit, independent of capital structure.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
- **pp (percentage points)** — A direct difference between two percentages, distinct from a "%" change.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring.
- **ROCE** — Return on Capital Employed — a close cousin of ROIC (profit ÷ capital employed in the business); used here only as a flagged proxy when a source didn't publish ROIC directly.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to never invent or estimate financial data — if a metric is missing, flag it and stop rather than infer it; also covers always fetching a live price before valuation work.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure.

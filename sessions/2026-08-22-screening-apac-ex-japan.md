# 2026-08-22 — SCREENING: Developed Asia-Pacific ex-Japan (APAC-EX-JP)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [APAC-EX-JP](../framework/screening-coverage-log.md) (Australia, Hong Kong, Singapore, South Korea, Taiwan), all sectors. Unattended scheduled run (Routine 4). Selected per the rotation rule: oldest "Last screened" date (2026-08-01) among all rows.

**Process note on this run's stored scheduled-task prompt:** the prompt that fired this session describes itself as a "Monthly Universe Screening Slice" and references an `EODHD_API_KEY`-based "Path A" full-automation path via `.claude/commands/screen.md`. Neither matches the current repo state — consistent with every prior rotation session since 2026-06-30 hitting this identical mismatch:
- The canonical [screen.md](../.claude/commands/screen.md) has no EODHD path at all — the only automated Step 0 option for an unattended run is the quality-factor-ETF-holdings fallback (MOAT/QUAL/QGRW/IQLT), and in practice (see Methodology below) that resolves to structural-triage-driven candidate sourcing for this slice, same as every prior session on it.
- [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md) records that EODHD was removed from every automation doc on 2026-06-19 — its free-tier screener endpoint was unreliable, and the `EODHD_API_KEY` committed to `.claude/settings.json` on 2026-06-13 was flagged as a **compromised, live credential** to be rotated, not reused.
- [framework/automation-schedule.md](../framework/automation-schedule.md) documents this as "Routine 4 — Twice-Weekly Universe Screening Slice" (Tuesday and Saturday), not monthly.

An `EODHD_API_KEY` **is** present in this session's environment. Per the removal decision's explicit instruction and the unbroken precedent set by every prior screening session, it was **not used**. This session followed the current, canonical `screen.md`/`framework/` process instead, per CLAUDE.md's instruction to treat `framework/` as the source of truth over a stale stored prompt — the same handling as [sessions/2026-08-01-screening-apac-ex-japan.md](2026-08-01-screening-apac-ex-japan.md) and every rotation session before it. The fired prompt also did not request the Telegram/`.ics` calendar-invite steps that `automation-schedule.md`'s current Routine 4 prompt includes; consistent with prior sessions' handling of the same discrepancy, this run did not add that scope on its own initiative and stuck to the fired prompt's explicit 5 steps (screen, complete Steps 0-5, save session, open PR, open summary issue).

---

## 0. Methodology

**Unattended session — no user to ask for a TIKR/Koyfin export**, so per screen.md's documented exception this run skips straight to the ETF-holdings fallback. **IQLT's holdings table is client-rendered and not scrapeable via plain fetch** (confirmed again this session, consistent with every prior APAC-EX-JP round), and its visible/free holdings carry negligible APAC-ex-Japan weight anyway. In practice this resolves to sourcing the candidate pool from **documented structural/business-model knowledge**, the same approach the 06-14, 07-11, and 08-01 sessions on this slice used — explicitly reaching for **new names not covered in any of the three prior APAC-EX-JP sessions**, across Australia, Hong Kong, Singapore, South Korea, and Taiwan, in sectors/niches not yet deeply covered (fintech/wrap-administration platforms, enterprise govtech SaaS, premium luggage/branded consumer goods, semiconductor test/precision-tooling equipment, biologics CDMO manufacturing, entertainment IP, subscription-appliance rental, optics/fabless IC design).

**A specific push into Hong Kong** was made this round per the 08-01 session's flagged standing gap (non-financial, non-property HK quality names beyond HKEX/Techtronic/ASMPT/Prada have been hard to find in prior rounds): Samsonite International, Vitasoy International, and VTech Holdings were sourced and fully quantified. None clears all 8 filters, but the push itself — and *why* each name falls short — is documented below rather than skipped.

**Data sourcing:** `yfinance` was tested once before this task began — `pip install --quiet yfinance` succeeded, but the first live call failed with the same `curl_cffi.requests.exceptions.SSLError: ...Recv failure: Connection reset by peer` error seen in every session since 2026-07-07. Not retried further, per the standing precedent. All quantitative figures below are sourced from **stockanalysis.com** via WebFetch (confirmed reachable, HTTP 200 on every ticker successfully resolved), cited inline with numbered footnotes.

**Live-price discipline (Rule 0):** every candidate's price-sensitive ratios (EV/EBIT, FCF yield, Net Debt/EBITDA) are shown on a **current/live-price basis** below, with the latest full-fiscal-year (FY) figure alongside for comparability, exactly as prior sessions have done. Two names this round show a **large, basis-flipping divergence between the two**, in *opposite* directions from each other — flagged prominently in Step 2 and Data Gaps rather than silently resolved:
- **Objective Corporation (ASX:OCL)** — share price fell from an FY2025-close of 18.85 AUD to a **current 7.11 AUD, a −62.3% decline** — turning an FY-basis 5/8 FAIL into a current-basis 7/8 NEAR-MISS on valuation alone. The magnitude of this one-year decline is itself the most notable single data point of this session and is flagged as a caution, not an endorsement — per CLAUDE.md's "act only on documented triggers, never on price movement alone," this session did not investigate *why* the price fell (no primary-source news access this session) and that cause is an open question before treating the near-miss as actionable.
- **Largan Precision (TPE:3008)** and **Realtek Semiconductor (TPE:2379)** — both moved the *other* way: current market caps are up +121.7% (Largan) and +46.8% (Realtek) versus FY2025 year-end, turning FY-basis clean valuation passes into current-basis EV/EBIT and (for Largan) FCF-yield misses.

**Two Singapore candidates from the original 13-name idea list turned out unavailable at this data source and were swapped out before quantitative testing** (see Data Gaps): **Silverlake Axis** (SEA banking-core software vendor) does not appear in stockanalysis.com's own search index under any plausible ticker — replaced with **Micro-Mechanics Holdings (SGX:5DD)**, a semiconductor precision-tooling manufacturer, which does resolve and was fully quantified.

**Candidate pool this session (13 new names quantified, spanning 5 markets):**

| Ticker | Company | Country | Sector |
|---|---|---|---|
| ASX:OCL | Objective Corporation | Australia | Govtech enterprise content management SaaS |
| ASX:HUB | HUB24 | Australia | Investment/wrap administration platform |
| HKG:1910 | Samsonite International | Hong Kong | Premium luggage brand (manufacture + retail) |
| HKG:0345 | Vitasoy International Holdings | Hong Kong | Branded soy/dairy-alternative beverages |
| HKG:0303 | VTech Holdings | Hong Kong | Consumer electronics (own-brand + contract mfg) |
| SGX:AWX | AEM Holdings | Singapore | Semiconductor test handler equipment |
| SGX:5DD | Micro-Mechanics Holdings | Singapore | Semiconductor precision tooling |
| KRX:207940 | Samsung Biologics | South Korea | Biologics CDMO (contract manufacturing) |
| KRX:352820 | HYBE Co., Ltd. | South Korea | Entertainment/K-pop IP management |
| KRX:021240 | Coway | South Korea | Water/air purifier subscription rental |
| TPE:3008 | Largan Precision | Taiwan | Smartphone camera optics (fabless design/mfg) |
| TPE:2379 | Realtek Semiconductor | Taiwan | Fabless IC design (networking/PC peripherals) |
| TPEX:4966 | Parade Technologies | Taiwan | Fabless analog/mixed-signal IC design |

---

## Step 1 — Structural triage (business-model eliminations, no quantitative pull)

Building on all three prior sessions' Step 1 eliminations (Singapore/HK banks, AIA, Macquarie, Goodman Group REIT, Wesfarmers/JB Hi-Fi, Sea Limited, Grab, Wilmar, ComfortDelGro, Venture Corp, various REITs, Samsung SDI/LG Energy Solution, Melco/Sands China/Galaxy Entertainment, Hyundai/Kia/Hyundai Mobis, Silergy, ST Engineering, Riverstone Holdings, Coupang, Yangzijiang Shipbuilding, Keppel Corporation, Genting Singapore, LG Household & Health Care, Amorepacific, Kakao Corp, Kakao Games — all still structurally excluded, not re-litigated), this pass adds:

| Eliminated | Country | Why |
|---|---|---|
| China Resources Beer, Budweiser APAC, Vinda International | Hong Kong | Commodity beverage/tissue-paper manufacturing — thin, cyclical margins typical of consumer-staples manufacturing without a differentiated brand-pricing-power story |
| Café de Coral | Hong Kong | Fast-casual restaurant chain — thin-margin volume food service |
| Sinopharm, Sino Biopharmaceutical | Hong Kong | Pharma distribution / generics manufacturing — patent-cliff and thin-distribution-margin exposure, same reasoning as prior sessions' pharma exclusions |
| Thai Beverage | Singapore | Diversified alcohol/beverage conglomerate — thin, regulated-adjacent margins |
| Sats Ltd, Singtel, CapitaLand Investment | Singapore | Regulated/capital-intensive/property-adjacent (airport ground handling, regulated telecom, real-estate asset management) — same reasoning as prior REIT/telecom exclusions |
| LG Chem, Lotte Chemical | South Korea | Commodity petrochemicals — capital-intensive, cyclical margins |
| LG Uplus, SK Telecom | South Korea | Regulated telecom — thin, capped-margin utility-like model |
| Wiwynn, Quanta Computer, Hon Hai/Foxconn, King Yuan Electronics, Sinbon Electronics | Taiwan | Contract manufacturing / semiconductor packaging-and-testing services (EMS/OSAT) — structurally thin-margin, same reasoning as the prior sessions' Venture Corp/Foxconn exclusions |
| Frencken Group | Singapore | Electronics Manufacturing Services (EMS) — same reasoning |

**Considered but unavailable at this data source (not a business-model exclusion — see Data Gaps):** Silverlake Axis.

---

## Step 2 — Full Phase 01 quantitative gate (real, sourced data — stockanalysis.com, pulled 2026-08-21/22)

Filters: Gross margin >40% · Net margin >12% · ROIC>15% (ROE proxy only when ROIC isn't disclosed) · Revenue growth >8% (3yr CAGR) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x

Gross margin, net margin, and ROE/ROIC are shown on the latest full-fiscal-year basis (revenue-growth CAGR spans the 3 most recent complete fiscal years); Net Debt/EBITDA, FCF yield, and EV/EBIT are shown on a **current/live-price basis** per Rule 0, with the latest-FY figure alongside for comparability.

| Ticker | Gross M (FY) | Net M (FY) | ROIC / ROE (FY, current) | Rev 3yr CAGR | FCF 3yr positive? | Net Debt/EBITDA (current / FY) | FCF yield (current / FY) | EV/EBIT (current / FY) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **Objective Corporation (ASX:OCL)** [[1]](#src1) | 94.17% ✅ | 28.70% ✅ | ROIC 138.36% (degenerate, flagged) / ROE 35.80% ✅ | 6.57% ❌ (current vs. FY22) / 5.05% ❌ (FY25 vs. FY22) | ✅ (FY23–25: 22.86/54.78/45.67 AUD M) | −1.98 ✅ (net cash) / −2.08 ✅ | **8.05% ✅ (current) / 2.49% ❌ (FY25)** | **13.62x ✅ (current) / 43.11x ❌ (FY25)** | **NEAR-MISS on current basis — 7/8, only Rev CAGR fails — but see the −62.3% price-decline caution above** |
| **HUB24 (ASX:HUB)** [[2]](#src2) | **data gap** (no COGS breakout — platform/administration model, same caveat class as Computershare/AUB/Steadfast) | 24.19% ✅ | ROIC 19.25% ✅ / ROE 22.20% ✅ | 21.44% ✅ (FY23→FY26) | ✅ (FY22–26 all positive, 36.34→171.81 AUD M) | ≈0.00x ✅ (net debt only 0.67M AUD vs. large EBITDA — negligible) | 2.77% ❌ | 42.9x ❌ (computed: EV 6,212M ÷ EBIT 144.83M) | **FAIL — 5/7 determinable + 1 gap, both misses valuation** — excellent quality, priced rich |
| **Samsonite International (HKG:1910)** [[3]](#src3) | 59.60% ✅ | 8.26% ❌ | ROIC 11.04% ❌ / ROE 18.28% | 6.70% ❌ | ✅ (FY23–25: 434.9/460.9/420.7 USD M) | 2.85x ❌ (current) / 2.74x ❌ (FY25) | 22.38% ✅ / 11.86% ✅ | 8.08x ✅ / 10.11x ✅ | **FAIL — 4/8** (net margin, ROIC, growth, leverage all miss) — cheap on valuation, weak on quality/leverage |
| **Vitasoy International (HKG:0345)** [[4]](#src4) | 50.83% ✅ | 4.53% ❌ | ROIC 10.13% ❌ / ROE 9.09% ❌ | −1.50% ❌ (declining) | ✅ (FY24–26: 644.25/734.33/560.58 HKD M) | −1.04x ✅ (net cash) | 8.61% ✅ | 17.74x ✅ | **FAIL — 5/8** (margin, returns, growth all miss) — recovering from FY2022 losses, still thin-margin |
| **VTech Holdings (HKG:0303)** [[5]](#src5) | 32.72% ❌ | 6.61% ❌ | ROIC 26.98% ✅ / ROE 20.76% ✅ | −3.29% ❌ (declining) | ✅ (FY24–26, declining trend: 322.8/195.8/92.6 USD M) | −0.67x ✅ (net cash) | 5.50% ✅ | 9.04x ✅ | **FAIL — 5/8** (margin, growth miss; strong returns/valuation/leverage) — legacy cordless-phone/EMS segment drags margin and revenue |
| **AEM Holdings (SGX:AWX)** [[6]](#src6) | 25.67% ❌ | 4.25% ❌ | ROIC 8.80% ❌ / ROE 8.74% ❌ | −29.7% ❌ (severe decline from FY22 cyclical peak) | ❌ (FY24 negative: −23.41 SGD M) | −1.01x ✅ (net cash) | 3.12% ❌ | 56.93x ❌ | **FAIL — 1/8** — extreme cyclical downturn + massive re-rating on customer-concentration (Intel-dependent) AI-cycle optimism |
| **Micro-Mechanics Holdings (SGX:5DD)** [[7]](#src7) | 49.41% ✅ | 19.01% ✅ | ROIC 49.00% ✅ (flagged high) / ROE 27.77% ✅ | −7.53% ❌ (FY22 cyclical-peak base year) | ✅ (FY23–25: 14.36/12.12/16.83 SGD M) | −0.96x ✅ (net cash) | 4.24% ✅ | 18.83x ✅ | **NEAR-MISS — 7/8, only Rev CAGR fails** |
| **Samsung Biologics (KRX:207940)** [[8]](#src8) | 54.88% ✅ | 39.16% ✅ (flagged high) | ROIC 23.35% ✅ / ROE 18.25% ✅ | 14.94% ✅ | ✅ (FY23–25: 671,158/355,682/856,067 KRW M) | −0.16x ✅ (net cash) | 2.27% ❌ | 30.36x ❌ | **NEAR-MISS — 6/8, both misses valuation** |
| **HYBE Co., Ltd. (KRX:352820)** [[9]](#src9) | 35.32% ❌ (declining) | −8.95% ❌ (FY25 net loss) | ROIC −6.15% ❌ / ROE −12.96% ❌ | 14.26% ✅ | ✅ (FY23–25, declining: 287,887/118,558/76,121 KRW M) | 35.51x ❌ (degenerate, near-zero EBITDA) | 3.14% ❌ | undefined/"—" ❌ | **FAIL — 2/8** — FY2025 net loss |
| **Coway (KRX:021240)** [[10]](#src10) | 64.00% ✅ | 12.45% ✅ (narrow) | ROIC 12.16% ❌ (narrow) / ROE 19.32% | 8.78% ✅ | ❌ (FY25 turned negative: −188,385 KRW M) | 1.62x ✅ | −3.10% ❌ | 9.96x ✅ | **FAIL — 5/8** (3 misses: ROIC narrow, FCF-positive, FCF yield) — capex-heavy rental model, see Data Gaps |
| **Largan Precision (TPE:3008)** [[11]](#src11) | 50.43% ✅ | 34.79% ✅ | ROIC 38.90% ✅ (flagged high) / ROE 13.33% | 8.65% ✅ (narrow) | ✅ (FY23–25: 9,962/20,446/13,740 TWD M) | −4.38x ✅ (net cash) | **2.80% ❌ (current) / 4.15% ✅ (FY25)** | **25.33x ❌ (current) / 8.89x ✅ (FY25)** | **NEAR-MISS — 6/8 on current basis, both misses valuation-only and price-driven (see caution above)** |
| **Realtek Semiconductor (TPE:2379)** [[12]](#src12) | 50.02% ✅ | 12.02% ✅ (narrow) | ROIC "—"/405.74% (degenerate, flagged) / ROE 30.34% ✅ | 3.16% ❌ | ✅ (FY23–25: 15,730/21,587/20,926 TWD M) | −3.68x ✅ (net cash) | 4.57% ✅ | **22.99x ❌ (current, narrow) / 13.25x ✅ (FY25)** | **NEAR-MISS — 6/8, misses growth + a narrow price-driven EV/EBIT miss** |
| **Parade Technologies (TPEX:4966)** [[13]](#src13) | 42.55% ✅ (narrow) | 16.49% ✅ | ROIC 20.88% ✅ / ROE 12.27% | −6.28% ❌ (FY22 cyclical-peak base year) | ✅ (FY23–25: 3,577/3,178/3,280 TWD M) | −3.15x ✅ (net cash, FY25 basis — current data gap) | 7.20% ✅ (FY25) / 6.98% (current) | 13.35x ✅ (FY25 basis — current data gap) | **NEAR-MISS — 7/8 on FY basis, only Rev CAGR fails — see current-basis data gap below** |

---

## ✅ Qualified Quality List — 0 new clean passes this session

No candidate cleared all 8 Phase 01 filters this round (0/13). The prior sessions' list is **unchanged and carried forward**: **iFAST Corporation (AIY.SG)** remains the one clean Phase 01 pass on this slice, with **KRAFTON, ResMed, and CSL** still flagged pending `/new-position` confirmation — none of those four were re-touched this session.

However, this round produced **five near-misses at the 6-7/8 level** — the strongest single-round near-miss haul on this slice to date — plus one prominent basis-flip caution (Objective Corporation). All are added to the watchlist below.

### Near-misses flagged for the watchlist (headline)

- **Micro-Mechanics Holdings (SGX:5DD)** — 7/8 clear; only Revenue 3yr CAGR (−7.53%) fails, entirely a base-year artifact (FY2022 was a semiconductor-tooling cyclical peak; the TTM trend is already recovering).
- **Parade Technologies (TPEX:4966)** — 7/8 clear on an FY2025 basis; only Revenue 3yr CAGR (−6.28%, same FY2022 cyclical-peak base-year pattern) fails. **Current-basis EV/EBIT, Net Debt/EBITDA, ROE, and ROIC could not be pulled** (see Data Gaps) — the FY2025 basis used is only ~8 months old.
- **Samsung Biologics (KRX:207940)** — 6/8 clear; both misses are pure valuation (FCF yield 2.27%, EV/EBIT 30.36x) — a genuinely strong-quality CDMO business priced for its growth.
- **Largan Precision (TPE:3008)** and **Realtek Semiconductor (TPE:2379)** — both 6/8 clear, both driven by the price run-up flagged above (market caps +121.7% and +46.8% respectively since FY2025 year-end) turning FY-basis passes into current-basis misses.
- **Objective Corporation (ASX:OCL)** — 7/8 on a current-price basis (only Revenue 3yr CAGR fails, at 5–7% depending on basis) but flagged as a **caution, not a clean near-miss**, given the −62.3% one-year price decline behind the reclassification — see the Methodology box above and Data Gaps.

### Additional watchlist flag — real quality gap, not just valuation

- **Coway (KRX:021240)** — 5/8, but unlike the "priced rich" pattern above, its misses are **not narrow valuation-only ones**: ROIC (12.16% vs. 15%) is a moderate miss, and FCF turned outright negative in FY2025 despite a strong 64% gross margin — a genuine capex-heavy-rental-model characteristic (see Data Gaps), not a pure valuation block. Flagged for awareness, not given a full qualitative write-up this round.

### Confirmed structural misses (no watchlist value)

- **Samsonite International, Vitasoy International, VTech Holdings** (the Hong Kong push) — all fail on 4-5 of 8 filters (margin, returns, and/or growth), confirming rather than closing the HK standing gap: none is a genuine quality-gate pass, though all three screen statistically cheap (single-digit-to-teens EV/EBIT).
- **AEM Holdings, HYBE** — both severe fails (1/8 and 2/8) driven by real, current business deterioration (AEM: post-2022 cyclical collapse + speculative re-rating; HYBE: FY2025 net loss) rather than a narrow miss.

---

## Step 3 — Qualitative pass

Per screen.md's batch-processing policy (default batch size 2, from [new-position.md](../.claude/commands/new-position.md)), the six near-miss/caution names were walked through the 6 qualitative questions in three conceptual batches of 2, with the growing session log committed and pushed after each batch.

### Batch 1 — Micro-Mechanics Holdings & Samsung Biologics

#### Micro-Mechanics Holdings (SGX:5DD)

1. **Why are margins high?** Micro-Mechanics designs and manufactures precision tooling and consumable parts (collets, wafer chucks, cutting/grinding tools) used inside semiconductor back-end assembly and test equipment — high-precision, low-volume, engineered-to-spec components where reliability directly affects a customer fab's yield, supporting premium pricing over commodity tooling.
2. **What would it take to compete?** A rival needs deep, accumulated precision-engineering know-how across many chip-packaging tool geometries plus multi-year qualification relationships with semiconductor OEMs and fabs — qualification cycles for tooling that touches yield-critical processes are slow and conservative, favoring an incumbent with a long qualified track record.
3. **Capital allocation (5–10yr):** Organic reinvestment in manufacturing capacity across its Singapore/Malaysia/China/Philippines/USA plants; consistently positive FCF and a long-standing dividend policy — no major disclosed M&A in the sourced financials, a disciplined, non-acquisitive compounder profile.
4. **Where's growth coming from (3–5yr)?** Direct leverage to the semiconductor capital-equipment cycle (its own tooling revenue tracks fab utilization and back-end assembly/test capacity additions) — the AI/advanced-packaging capex cycle is the most likely near-term tailwind given its customer base.
5. **Best bear case:** Small-cap, single-industry (semiconductor back-end) concentration means its revenue is directly cyclical with the chip-equipment capex cycle — the FY2022 revenue peak (82.46M SGD) followed by a two-year decline to FY2024 (57.89M SGD) before recovering is exactly that cyclicality showing up in the numbers, and the reason this round's Revenue 3yr CAGR reads negative despite a real TTM recovery already underway.
6. **Disruption vector:** Low — precision mechanical tooling for chip packaging/test is not a software-substitutable category; the more relevant long-run risk is share loss to a larger, better-capitalized precision-tooling competitor, not technological obsolescence of the category itself.

**Conclusion:** A genuine near-miss where the single failing filter (Revenue 3yr CAGR) is a well-understood base-year artifact of semiconductor-equipment cyclicality rather than a structural growth problem — worth a re-check next rotation once the TTM recovery (70.64M SGD vs. FY2025's 65.21M) shows up in a full fiscal year.

#### Samsung Biologics (KRX:207940)

1. **Why are margins high?** Samsung Biologics is a CDMO (contract development and manufacturing organization) — it manufactures biologic drugs (antibodies, vaccines, cell/gene therapies) under contract for pharma/biotech clients who don't want to build their own large-scale biomanufacturing capacity. Its FY2025 net margin (39.16%) is unusually high even for a CDMO — flagged explicitly as a data point worth further scrutiny (a possible one-off gain, tax item, or FX effect not investigated further this session) rather than assumed to be the new sustainable run-rate.
2. **What would it take to compete?** A rival needs multi-billion-dollar, multi-year biomanufacturing plant construction (bioreactor capacity is the scarce, capital-intensive resource) plus the regulatory-approval track record (FDA/EMA facility inspections) that large pharma clients require before committing a drug's manufacturing to a new CDMO — both are slow, capital-intensive barriers, though WuXi Biologics (evaluated in the EM slice, [sessions/2026-08-04-screening-emerging-markets.md](2026-08-04-screening-emerging-markets.md)) and several Western CDMOs are direct global competitors.
3. **Capital allocation (5–10yr):** Continuous, large-scale reinvestment in bioreactor capacity (capex has run 900,000–1,400,000M KRW annually against operating cash flow of 450,000–2,250,000M KRW) — a genuinely capital-intensive growth model, not asset-light, funded so far without net debt (net cash position throughout).
4. **Where's growth coming from (3–5yr)?** Continued biologics-manufacturing capacity build-out (new plant phases) and biosimilar pipeline expansion through its Samsung Bioepis affiliate/joint venture relationship.
5. **Best bear case:** As a contract manufacturer, its growth is a function of large pharma clients' own drug-development pipelines and manufacturing-outsourcing decisions rather than owned IP — a client's in-sourcing decision, drug-trial failure, or CDMO price competition (there are credible global competitors) all sit outside Samsung Biologics' own control. The FY2025 net-margin spike (vs. 30.98% FY2024) is worth resolving before trusting the current profitability level as durable.
6. **Disruption vector:** Low-moderate — biologics manufacturing requires physical, regulator-inspected capacity that can't be disintermediated by software, but AI-driven drug-discovery efficiency gains could eventually compress the addressable manufacturing volume per approved drug, a longer-horizon consideration.

**Conclusion:** Strong, broad-based quality (6/8, both misses pure valuation) — this is the "great business, priced for it" pattern seen repeatedly across prior APAC-EX-JP rounds (Chroma ATE, eMemory, Fisher & Paykel Healthcare in 08-01), with the added flag that the FY2025 margin spike should be sanity-checked against FY2026 results before being treated as the new baseline.

### Batch 2 — Largan Precision & Realtek Semiconductor

#### Largan Precision (TPE:3008)

1. **Why are margins high?** Largan designs and manufactures precision optical lens modules primarily for smartphone cameras (Apple and leading China-Android OEMs are its largest customer concentration), commanding premium pricing through multi-generation optical-design IP (lens-element count, aperture, autofocus/OIS integration) that lags competitors by design cycles.
2. **What would it take to compete?** A rival needs comparable multi-year optical-design and precision-molding manufacturing know-how plus the scale to serve flagship-tier smartphone camera specs at acceptable yield — a small number of credible global competitors exist (Sunny Optical, Genius Electronic Optical), meaning this is a real but not unassailable moat; margin compression from rising competition and customer negotiating power has been a known multi-year theme (gross margin declined from 59.94% FY2021 to 50.43% FY2025).
3. **Capital allocation (5–10yr):** Organic reinvestment in precision-molding/optical R&D capacity; consistently positive FCF and net-cash balance sheet (Net Debt/EBITDA −4.38x, one of the strongest in this session's pool) — no major disclosed M&A.
4. **Where's growth coming from (3–5yr)?** Continued high-end smartphone camera-spec upgrades (higher lens-element counts, periscope/telephoto modules) and diversification into automotive/AR-VR optics as a second growth leg beyond smartphone-camera cyclicality.
5. **Best bear case:** Heavy customer concentration in smartphone-camera-module supply (implicitly Apple-adjacent) means unit/spec-mix decisions by a small number of large customers drive results; the multi-year gross-margin compression trend (59.94%→50.43%) suggests some structural pricing-power erosion, not purely cyclical.
6. **Disruption vector:** Low-moderate — computational photography (software-driven image enhancement) has structurally reduced how much marginal camera hardware quality matters to end-user photo quality at the margin, a long-running theme that has already partly played out in the margin-compression trend above.

**Conclusion:** Real quality (ROIC 38.90%, strong balance sheet), but the current-basis 6/8 near-miss is driven almost entirely by the +121.7% market-cap run-up since FY2025 year-end — worth explicitly checking whether that reflects a genuine re-rating of AI/optics-adjacent demand or a speculative overshoot before treating this as a standard "priced rich" quality name; the FY2025-basis EV/EBIT (8.89x) would have been a clean pass.

#### Realtek Semiconductor (TPE:2379)

1. **Why are margins high?** Realtek is a fabless IC designer supplying networking chips (Wi-Fi, Ethernet, Bluetooth controllers) and PC-peripheral/audio-codec chips — the fabless model (no owned fab capex) plus a broad, sticky design-win base across PC/networking OEMs supports consistent 50%+ gross margins.
2. **What would it take to compete?** A rival needs multi-generation RF/networking chip design expertise plus an installed design-win base across PC and networking-equipment OEMs — real technical barriers, though the networking-chip space has several credible global competitors (Broadcom, MediaTek, Qualcomm at the high end).
3. **Capital allocation (5–10yr):** Organic R&D reinvestment; consistent, sizeable dividend payout (3.56–5.11% yield across the period shown) alongside continued positive FCF — a mature, shareholder-return-oriented capital allocation profile rather than an aggressive-growth one.
4. **Where's growth coming from (3–5yr)?** Wi-Fi 7/next-gen networking-standard chip upgrade cycles and continued PC-peripheral design-win share — a steadier, more mature growth profile than the AI-capex-driven names in this pool, consistent with its modest (3.16%) 3yr revenue CAGR.
5. **Best bear case:** Revenue growth has been essentially flat-to-cyclical over the trailing 3 years (FY2022 111,790M TWD → FY2023 95,179M → FY2025 122,706M) — a mature networking/PC-peripheral chip supplier with limited structural growth catalysts beyond the standards-upgrade cycle; the modest revenue CAGR miss reflects this rather than a data artifact.
6. **Disruption vector:** Low — networking/connectivity silicon is a durable, non-substitutable category, though continued industry consolidation among networking-chip suppliers is a competitive (not technological) risk to watch.

**Conclusion:** A genuine, if modest, 6/8 near-miss — one real (not artifact-driven) growth-rate miss plus a narrow, price-driven EV/EBIT miss (22.99x current vs. 20x cap, would clear at the FY2025-basis 13.25x). Worth a re-check if the market-cap run-up (+46.8% since FY2025 year-end) partially reverses.

### Batch 3 — Parade Technologies & Objective Corporation

#### Parade Technologies (TPEX:4966)

1. **Why are margins high?** Parade is a fabless analog/mixed-signal IC designer specializing in display-interface chips (used in notebook/monitor display timing controllers and related interfaces) — a narrow, technically demanding niche where design-win relationships with display-panel and notebook OEMs are sticky once qualified into a product generation.
2. **What would it take to compete?** A rival needs comparable analog/mixed-signal display-interface design expertise plus existing OEM qualification — a real, if narrow, moat; the company's revenue trajectory (FY2022 20,055M TWD → FY2024 trough 16,246M → FY2025 16,531M recovering) shows this is a cyclical, PC/notebook-demand-linked niche rather than a structurally growing one.
3. **Capital allocation (5–10yr):** Organic R&D reinvestment; consistently positive FCF across every year shown (FY2021–2025) and a meaningful dividend payout — disciplined, non-acquisitive.
4. **Where's growth coming from (3–5yr)?** Recovery in PC/notebook unit demand from its FY2022–2024 downturn, plus potential design-win expansion into adjacent display-interface categories (automotive displays, higher-resolution panels).
5. **Best bear case:** Revenue is directly linked to PC/notebook OEM demand cycles — the FY2022→FY2024 33% revenue decline shows how exposed this niche is to a PC-demand downturn, and the FY2025 recovery (16,531M vs. 16,246M FY2024) is still well below the FY2022 peak, meaning the Revenue 3yr CAGR miss reflects real cyclicality, not a one-off base-year artifact in the same clean sense as Micro-Mechanics'.
6. **Disruption vector:** Low-moderate — display-interface silicon is a durable category tied to display-panel evolution, but a narrower addressable market than broader networking/analog peers means less diversification if PC-demand growth stays structurally soft.

**Conclusion:** A near-miss (7/8 on the FY2025 basis) worth flagging, but the **current-basis data gap is real** (see Data Gaps) — the "current" column on stockanalysis.com returned no value for PE, EV ratios, Net Debt/EBITDA, ROE, or ROIC for this ticker, an unusual pattern versus every other candidate this session. FY2025 (ended Dec 2025, ~8 months old) was used instead and flagged explicitly rather than treated as a live figure.

#### Objective Corporation (ASX:OCL)

1. **Why are margins high?** Objective Corporation sells enterprise content-management/records-management/governance SaaS software specifically to government and regulated public-sector customers (councils, government departments, regulators) in Australia/NZ/UK — a niche where compliance/records-retention requirements are mandatory, contracts are typically multi-year, and switching costs are high once an agency's records/workflow processes are built around the platform. 94%+ gross margin is consistent with a mature, largely-amortized software platform sold to a sticky government-customer base.
2. **What would it take to compete?** A rival needs government-specific compliance/records-management domain expertise plus the track record and security/compliance certifications public-sector procurement processes require — a real, if narrow, moat given how conservative government IT procurement typically is once a vendor is embedded.
3. **Capital allocation (5–10yr):** Organic R&D reinvestment plus a rising dividend payout (67.90% current payout ratio) — no major disclosed M&A in the sourced financials, a mature, cash-generative profile.
4. **Where's growth coming from (3–5yr)?** Continued government-sector digital-transformation/compliance-modernization spending and international expansion (UK) of the existing platform — but the reported growth rate itself (5–7% depending on basis) is genuinely modest, well under the 8% bar, not a data artifact.
5. **Best bear case:** Growth has structurally slowed (FY2021's 35.72% YoY growth vs. FY2025's 5.11%) as the customer base matures — government-sector software adoption cycles are inherently slow and lumpy, and a −62.3% one-year share-price decline (18.85→7.11 AUD) is a significant enough move that it should be treated as a documented trigger warranting investigation (a guidance cut, contract loss, or accounting issue are all plausible explanations this session could not confirm or rule out) before any capital-allocation decision, not simply read as "got cheaper."
6. **Disruption vector:** Low — government records/compliance software is a mature, non-trend-sensitive category; the more relevant risk is competitive share loss to another entrenched govtech vendor, not technological disruption.

**Conclusion:** The Revenue 3yr CAGR miss is real and consistent across both bases (not a data artifact) — this is genuinely a mature, slow-growth SaaS business, not a hidden fast grower. The current-basis 7/8 near-miss classification is real by the numbers, but the **−62.3% price decline behind it is flagged as a caution requiring investigation**, not treated as confirmation of a buying opportunity — consistent with the framework's "act only on documented triggers, never on price movement alone" principle. **Recommended next step: investigate the cause of the price decline (via `/new-position` or a dedicated news check) before any further action, rather than defaulting to a near-miss watchlist add on the numbers alone.**

---

## Step 4 / Data gaps flagged (per CLAUDE.md Rule 0 — none estimated)

- **HUB24 (ASX:HUB) — no gross margin.** stockanalysis.com's income-statement view for HUB24 shows no separate Cost-of-Revenue/COGS line — same data-source limitation class as Computershare (07-11), AUB Group, and Steadfast Group (08-01), all asset-light fee/platform-administration businesses. Not assumed; the other 7 filters were still evaluated (5 pass, 2 fail).
- **HUB24 — EV/EBIT not directly published.** stockanalysis.com's ratios page for HUB24 omitted its "EV Ratios" section entirely (present for every other ticker this session) even after two separate targeted re-fetches. **Derived manually and shown, not invented:** Enterprise Value (Market Cap 6,211M AUD + Net Debt 0.67M AUD ≈ 6,212M AUD) ÷ EBIT (FY2026 144.83M AUD) = 42.9x — both inputs independently sourced from the ratios and balance-sheet pages respectively, the division shown explicitly.
- **Objective Corporation (ASX:OCL) — large basis-flipping price move.** See the Methodology box and Step 3 write-up above: a −62.3% one-year share-price decline (18.85→7.11 AUD) makes the current-basis classification (NEAR-MISS, 7/8) very different from the FY2025-basis one (FAIL, 5/8). Per Rule 0 the current/live-price basis is used for the headline verdict, but the cause of the decline was not investigated this session (no primary-source news access) and is flagged as an open question, not resolved.
- **Largan Precision (TPE:3008) and Realtek Semiconductor (TPE:2379) — reverse-direction basis moves.** Both saw current market caps run up materially versus FY2025 year-end (+121.7% and +46.8% respectively), turning FY-basis EV/EBIT (and for Largan, FCF yield) passes into current-basis misses. Flagged as the mirror image of the OCL case above — a live price *increase*, not decrease, driving the reclassification.
- **Parade Technologies (TPEX:4966) — current-basis data gap.** stockanalysis.com's ratios page returned "—" (no value) for the Current column's PE, PS, EV/Sales, EV/EBITDA, EV/EBIT, Net Debt/EBITDA, ROE, and ROIC — an unusual pattern versus every other ticker this session (all of which populated a Current column). FY2025 figures (fiscal year ended Dec 2025, ~8 months old as of this session) were used instead and flagged explicitly rather than treated as live.
- **Silverlake Axis (Singapore) — unavailable at this data source.** No match returned by stockanalysis.com's own search endpoint under this name or any plausible ticker guess; not evaluated. Replaced in the candidate pool with Micro-Mechanics Holdings (SGX:5DD), which did resolve.
- **Samsung Biologics (KRX:207940) — FY2025 net-margin spike.** 39.16% vs. FY2024's already-strong 30.98% — flagged as unusually high even for a CDMO business; cause (one-off gain, tax item, FX) not investigated further this session, not assumed to be the sustainable run-rate.
- **HYBE (KRX:352820) — degenerate Net Debt/EBITDA and undefined EV/EBIT.** FY2025's near-zero EBITDA (operating income compressed to 45,898M KRW against a still-large enterprise value) produces a Net Debt/EBITDA reading of 35.51x and an EV/EBIT ratio stockanalysis.com itself shows as "—" (undefined) — both are denominator artifacts of the FY2025 profit collapse, not meaningful leverage/valuation signals, and are not used at face value; HYBE fails independently on margin/returns/FCF-yield regardless.
- **Several extreme ROIC readings** (Objective Corp 138.36%, Micro-Mechanics 49.00%, Largan Precision 38.90%, Realtek 405.74% FY2025/240.50% FY2024) are flagged as small-invested-capital-denominator artifacts typical of asset-light software/precision-manufacturing businesses, consistent with the TechnologyOne/Pro Medicus/eMemory precedent from prior APAC-EX-JP rounds. ROE is shown alongside as the cross-check in each case.
- **Coway (KRX:021240) — FY2025 FCF turned negative despite strong margins.** −188,385M KRW FY2025 FCF against a 64.00% gross margin and 12.45% net margin is flagged as a genuine business-model characteristic, not a data error: Coway's subscription/rental appliance model requires heavy recurring capex (leased purifier units replaced/maintained on an ongoing basis) — capex has stayed elevated (213,000–276,000M KRW annually) even as operating cash flow declined sharply in FY2025 (35,544M KRW vs. FY2024's 330,339M KRW).
- **AEM Holdings (SGX:AWX) — FY2024 net-cash-to-leverage swing (−1.74x FY25 vs. +2.04x FY24) and a P/FCF "—" for FY2024.** Both reflect the severe FY2022→FY2024 cyclical earnings/cash-flow trough (net income briefly negative in FY2023) common to semiconductor-test-equipment suppliers with customer concentration — same reasoning flagged for ASMPT in the 07-11 session.

---

## Sources

<a id="src1"></a>[1] Objective Corporation: https://stockanalysis.com/quote/asx/OCL/financials/ratios/ , https://stockanalysis.com/quote/asx/OCL/financials/ , https://stockanalysis.com/quote/asx/OCL/financials/cash-flow-statement/
<a id="src2"></a>[2] HUB24: https://stockanalysis.com/quote/asx/HUB/financials/ratios/ , https://stockanalysis.com/quote/asx/HUB/financials/ , https://stockanalysis.com/quote/asx/HUB/financials/cash-flow-statement/ , https://stockanalysis.com/quote/asx/HUB/financials/balance-sheet/ , https://stockanalysis.com/quote/asx/HUB/ (EV-ratio confirmation attempts)
<a id="src3"></a>[3] Samsonite International: https://stockanalysis.com/quote/hkg/1910/financials/ratios/ , https://stockanalysis.com/quote/hkg/1910/financials/ , https://stockanalysis.com/quote/hkg/1910/financials/cash-flow-statement/
<a id="src4"></a>[4] Vitasoy International Holdings: https://stockanalysis.com/quote/hkg/0345/financials/ratios/ , https://stockanalysis.com/quote/hkg/0345/financials/ , https://stockanalysis.com/quote/hkg/0345/financials/cash-flow-statement/
<a id="src5"></a>[5] VTech Holdings: https://stockanalysis.com/quote/hkg/0303/financials/ratios/ , https://stockanalysis.com/quote/hkg/0303/financials/ , https://stockanalysis.com/quote/hkg/0303/financials/cash-flow-statement/
<a id="src6"></a>[6] AEM Holdings: https://stockanalysis.com/quote/sgx/AWX/financials/ratios/ , https://stockanalysis.com/quote/sgx/AWX/financials/ , https://stockanalysis.com/quote/sgx/AWX/financials/cash-flow-statement/
<a id="src7"></a>[7] Micro-Mechanics Holdings: https://stockanalysis.com/quote/sgx/5DD/financials/ratios/ , https://stockanalysis.com/quote/sgx/5DD/financials/ , https://stockanalysis.com/quote/sgx/5DD/financials/cash-flow-statement/
<a id="src8"></a>[8] Samsung Biologics: https://stockanalysis.com/quote/krx/207940/financials/ratios/ , https://stockanalysis.com/quote/krx/207940/financials/ , https://stockanalysis.com/quote/krx/207940/financials/cash-flow-statement/
<a id="src9"></a>[9] HYBE Co., Ltd.: https://stockanalysis.com/quote/krx/352820/financials/ratios/ , https://stockanalysis.com/quote/krx/352820/financials/ , https://stockanalysis.com/quote/krx/352820/financials/cash-flow-statement/
<a id="src10"></a>[10] Coway: https://stockanalysis.com/quote/krx/021240/financials/ratios/ , https://stockanalysis.com/quote/krx/021240/financials/ , https://stockanalysis.com/quote/krx/021240/financials/cash-flow-statement/
<a id="src11"></a>[11] Largan Precision: https://stockanalysis.com/quote/tpe/3008/financials/ratios/ , https://stockanalysis.com/quote/tpe/3008/financials/ , https://stockanalysis.com/quote/tpe/3008/financials/cash-flow-statement/
<a id="src12"></a>[12] Realtek Semiconductor: https://stockanalysis.com/quote/tpe/2379/financials/ratios/ , https://stockanalysis.com/quote/tpe/2379/financials/ , https://stockanalysis.com/quote/tpe/2379/financials/cash-flow-statement/
<a id="src13"></a>[13] Parade Technologies: https://stockanalysis.com/quote/tpex/4966/financials/ratios/ , https://stockanalysis.com/quote/tpex/4966/financials/ , https://stockanalysis.com/quote/tpex/4966/financials/cash-flow-statement/

Data-gap/availability confirmation fetches: https://stockanalysis.com/api/search?q=Silverlake%20Axis (no relevant match); https://stockanalysis.com/api/search?q=Micro-Mechanics (confirmed sgx/5DD); https://stockanalysis.com/api/search?q=Parade%20Technologies (confirmed tpex/4966).

---

## Next steps

- **No `/new-position` recommendation on a clean pass this round** — no candidate cleared all 8 Phase 01 filters.
- **Investigate Objective Corporation's −62.3% price decline before any watchlist action** — the framework's live-price discipline surfaced a genuine 7/8 near-miss on the numbers, but a documented-trigger check (guidance, news, a possible accounting issue) is needed before treating it as an opportunity rather than a value trap. This is this session's single most important open item.
- **Watchlist adds:** Micro-Mechanics Holdings (SGX:5DD) and Parade Technologies (TPEX:4966) — both 7/8, single narrow-to-moderate growth-rate misses tied to semiconductor/PC-demand cyclicality; Samsung Biologics (KRX:207940) — 6/8, valuation-only misses, flag the FY2025 margin spike for a follow-up check; Largan Precision (TPE:3008) and Realtek Semiconductor (TPE:2379) — both 6/8, worth re-checking if their recent market-cap run-ups partially reverse; Coway (KRX:021240) — 5/8 but a real (not narrow) quality gap, lower-priority watchlist flag.
- **Parade Technologies' current-basis data gap** should be re-checked next rotation — if stockanalysis.com's live pricing populates for this ticker, a fresh current-basis verdict (rather than the FY2025-basis one used here) should replace it.
- **Hong Kong push:** Samsonite International, Vitasoy International, and VTech Holdings were fully quantified this round per the 08-01 session's flagged gap — none clears the quality gate, but the search itself is now documented; worth trying a different HK sector (e.g., healthcare services, education) on a future rotation rather than repeating consumer-goods/electronics.
- **Silverlake Axis** — unavailable at stockanalysis.com; revisit with a different data source if one becomes available, or drop from future candidate lists.
- Coverage log updated below.

---

## Glossary

- **ADR (American Depositary Receipt)** — a US-exchange-listed security representing shares of a non-US company.
- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate between a start and end value over several years.
- **CDMO (Contract Development and Manufacturing Organization)** — a company that manufactures drugs (often complex biologics) under contract for pharmaceutical/biotech clients who don't own their own large-scale manufacturing capacity — Samsung Biologics' core business model.
- **EBIT** — Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
- **EV/EBIT, EV/EBITDA** — Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure.
- **Fabless** — a chip company that designs semiconductors but outsources manufacturing to a foundry — Realtek and Parade Technologies are both fabless designers; Largan Precision designs and manufactures its own optical (non-semiconductor) components.
- **FCF (Free Cash Flow)** — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper.
- **Gross Margin** — Gross Profit (Revenue − Cost of Revenue) ÷ Revenue.
- **Net Debt/EBITDA** — net debt (total debt minus cash) divided by EBITDA — a leverage ratio; "net cash" means the figure is negative (more cash than debt).
- **Net Margin** — Net Income ÷ Revenue.
- **Qualified Quality List** — the output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring.
- **ROE** — Return on Equity — Net Income ÷ shareholder equity.
- **ROIC** — Return on Invested Capital — a core quality signal in this framework; can be distorted (pushed to extreme values) for asset-light businesses with a very small invested-capital denominator.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results, used here to pair a live/current price with recent trailing fundamentals.

# 2026-09-12 — SCREENING: Developed Asia-Pacific ex-Japan (APAC-EX-JP)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [APAC-EX-JP](../framework/screening-coverage-log.md) (Australia, Hong Kong, Singapore, South Korea, Taiwan), all sectors. Unattended scheduled run (Routine 4). Selected per the rotation rule: oldest "Last screened" date among all rows (APAC-EX-JP: 2026-08-22, older than EM 08-25, EU 08-29, JP 09-01, NA-2 09-05, NA-1 09-08).

**Process note on this run's stored scheduled-task prompt:** the prompt that fired this session describes itself as a "Monthly Universe Screening Slice" running "the first Saturday of each month" and references an `EODHD_API_KEY`-based "Path A" full-automation path via `.claude/commands/screen.md`. Neither matches the current repo state — this is the same identical mismatch every rotation session has hit since 2026-06-30:

- The canonical [screen.md](../.claude/commands/screen.md) has no EODHD path at all — the only automated Step 0 option for an unattended run is the quality-factor-ETF-holdings fallback (MOAT/QUAL/QGRW/IQLT), which for this slice resolves in practice to structural-triage-driven candidate sourcing, same as every prior session on it (IQLT's holdings table is client-rendered, not scrapeable).
- [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md) records that EODHD was removed from every automation doc on 2026-06-19 — its free-tier screener endpoint was unreliable, and the `EODHD_API_KEY` committed to `.claude/settings.json` on 2026-06-13 was flagged as a **compromised, live credential**, not to be reused.
- [framework/automation-schedule.md](../framework/automation-schedule.md) documents this as "Routine 4 — Twice-Weekly Universe Screening Slice" (Tuesday and Saturday, 14:00 UTC), not monthly.

An `EODHD_API_KEY` **is** present in this session's environment. Per the removal decision's explicit instruction and the unbroken precedent set by every prior screening session, it was **not used**. This session followed the current, canonical `screen.md`/`framework/` process instead, per CLAUDE.md's instruction to treat `framework/` as the source of truth over a stale stored prompt — the same handling as every APAC-EX-JP rotation session before it (most recently [sessions/2026-08-22-screening-apac-ex-japan.md](2026-08-22-screening-apac-ex-japan.md)) and every EM/NA/EU/JP session since. This run stuck to the fired prompt's explicit 5 steps (screen, complete Steps 0-5, save session, open PR, open summary issue) and did not add scope (e.g. Telegram/`.ics` calendar steps) beyond that.

---

## 0. Methodology

**Unattended session — no user to ask for a TIKR/Koyfin export**, so per screen.md's documented exception this run skips straight to the ETF-holdings fallback, which (as in every prior APAC-EX-JP round) resolves to a candidate pool built from **documented structural/business-model knowledge**, since IQLT's holdings are not scrapeable and carry negligible APAC-ex-Japan weight regardless.

**Data sourcing:** `yfinance` was tested once before this session began — `pip install --quiet yfinance` succeeded, but the first live call failed with `curl_cffi.requests.exceptions.SSLError: ...Recv failure: Connection reset by peer`, the same failure mode seen in every session since 2026-07-07. Not retried further, per standing precedent. All quantitative figures below are sourced from **stockanalysis.com** via `WebFetch`, delegated across **4 parallel research agents** (one per AU / HK / SG+TW / KR) to keep this session's own context bounded, matching the delegation pattern used in the 09-08 NA-1, 09-05 NA-2, and 08-25 EM sessions.

**Candidate pool — 15 new names, explicitly not covered in any prior APAC-EX-JP session** (06-14, 07-11, 08-01, 08-22), spanning sectors not yet deeply covered on this slice: AU wealth-platform/wrap-administration and fiduciary/IP-services niches, HK enterprise software/healthcare-services/education (a deliberate pivot away from 08-22's exhausted HK consumer-goods push, per that session's own flagged next step), SG healthcare/real-estate-brokerage services, TW AI-server-supply-chain component makers, and KR aesthetics-biologics/content-IP/licensed-apparel-brand niches:

| Ticker | Company | Country | Sector |
|---|---|---|---|
| ASX:AD8 | Audinate Group | Australia | Audio-over-IP networking IP/hardware (Dante) |
| ASX:PNI | Pinnacle Investment Management | Australia | Multi-affiliate boutique asset manager |
| ASX:NWL | Netwealth Group | Australia | Wrap/investment-platform administration |
| ASX:EQT | EQT Holdings | Australia | Corporate/superannuation trustee services |
| ASX:IPH | IPH Limited | Australia | IP (patent/trademark) attorney-services roll-up |
| HKG:0268 | Kingdee International Software Group | Hong Kong (mainland-China-domiciled) | Enterprise ERP/cloud software |
| HKG:6078 | Hygeia Healthcare Holdings | Hong Kong (mainland-China-domiciled) | Private oncology-hospital operator |
| HKG:9901 | New Oriental Education & Technology | Hong Kong (mainland-China-domiciled; dual NYSE:EDU) | Education services / livestream e-commerce |
| SGX:BSL | Raffles Medical Group | Singapore | Private integrated healthcare |
| SGX:OYY | PropNex | Singapore | Residential real-estate brokerage |
| TPE:2059 | King Slide Works | Taiwan | Precision server-rail kits (AI-server supply chain) |
| TPE:2383 | Elite Material Co | Taiwan | High-speed PCB laminate materials (AI-server supply chain) |
| KOSDAQ:145020 | Hugel Inc | South Korea | Botulinum-toxin/aesthetics biologics manufacturer |
| KOSDAQ:253450 | Studio Dragon | South Korea | K-drama content production/IP |
| KRX:383220 | F&F Co., Ltd. (operating entity — see Data Gaps) | South Korea | Licensed fashion apparel (MLB, Discovery Expedition) |

**Categorization flag (new this round):** three of the HK-listed names (Kingdee, Hygeia, New Oriental) are **mainland-China-domiciled businesses that happen to be HK-listed**, distinct from the genuinely Hong-Kong-domiciled or global-brand names APAC-EX-JP has tested to date (HKEX, ASMPT, Techtronic, Prada, Samsonite, Vitasoy, VTech). This creates boundary ambiguity with the **EM** slice, which also covers Chinese companies (Tencent, PDD, ANTA, Moutai, Proya — all HK/mainland-listed). The rotation matrix doesn't currently resolve this split explicitly. Flagged here as a coverage-log open item rather than silently decided; results below stand regardless of which slice "owns" them going forward.

---

## Step 1 — Structural triage

Carrying forward all four prior sessions' eliminations (Singapore/HK banks, AIA, Macquarie, Goodman Group REIT, Wesfarmers/JB Hi-Fi, Sea Limited, Grab, Wilmar, ComfortDelGro, Venture Corp, various REITs, Samsung SDI/LG Energy Solution, Melco/Sands China/Galaxy Entertainment, Hyundai/Kia/Hyundai Mobis, Silergy, ST Engineering, Riverstone Holdings, Coupang, Yangzijiang Shipbuilding, Keppel Corporation, Genting Singapore, LG Household & Health Care, Amorepacific, Kakao Corp, Kakao Games, China Resources Beer, Budweiser APAC, Vinda International, Café de Coral, Sinopharm, Sino Biopharmaceutical, Thai Beverage, Sats Ltd, Singtel, CapitaLand Investment, LG Chem, Lotte Chemical, LG Uplus, SK Telecom, Wiwynn, Quanta Computer, Hon Hai/Foxconn, King Yuan Electronics, Sinbon Electronics, Frencken Group) — not re-litigated.

This round's 15-name pool was hand-selected via domain knowledge to avoid these categories from the outset (no bank, REIT, telecom, commodity-cyclical, or EMS/OSAT names proposed), so no additional Step 1 eliminations were needed — every proposed name went straight to the Step 2 quantitative gate. This is a change in process from prior rounds (which triaged a larger raw pool down); flagged for transparency, not treated as skipping a required step, since the framework's Step 1 exists to save analysis budget on names that plainly fail on business-model grounds, and none in this pre-filtered pool fell into an excluded category.

---

## Step 2 — Full Phase 01 quantitative gate (real, sourced data — stockanalysis.com, pulled 2026-09-12)

Filters: Gross margin >40% · Net margin >12% · ROIC>15% (ROE proxy only when ROIC isn't disclosed) · Revenue growth >8% (3yr CAGR, **strictly FY-anchored**: `(latest complete FY revenue / FY-3-years-earlier revenue)^(1/3) − 1`, per the methodology fix documented in [sessions/2026-09-08-screening-na1.md](2026-09-08-screening-na1.md)) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x.

Gross margin, net margin, and ROE/ROIC are shown on the latest full-fiscal-year basis; Net Debt/EBITDA, FCF yield, and EV/EBIT are shown on a **current/live-price basis** per Rule 0, with the latest-FY figure alongside for comparability — never inferred from a multiple, per the SPGI lesson.

| Ticker | Gross M (FY) | Net M (FY) | ROIC/ROE (FY, current) | Rev 3yr CAGR (FY-anchored) | FCF 3yr+ positive? | Net Debt/EBITDA (current / FY) | FCF yield (current / FY) | EV/EBIT (current / FY) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **Hugel Inc (KOSDAQ:145020)** [[1]](#src1) | 78.45% ✅ | 33.14% ✅ | ROIC 31.36% (current) / 32.38% (FY25) ✅ | **+14.70%** ✅ | ✅ (FY22–25 all positive, 47.8B→94.0B→136.7B→136.7B KRW) | −2.51 ✅ (net cash) / −2.31 ✅ | 5.94% ✅ / 5.49% ✅ | ~9.2x ✅ / ~9.6x ✅ | **✅ PASS — clears all 8 filters** |
| **New Oriental Education (HKG:9901)** [[2]](#src2) | 54.64% ✅ | **8.39% ❌** (vs. >12%, ~3.6pp short) | ROIC 193.17% (current, degenerate) / 388.90% (FY26) ✅⚠️ | +23.6% ✅ (flagged: FY23 base year itself a still-recovering post-crackdown low) | ✅ (FY24–26 all positive) | −5.40 ✅ (net cash) | 14.09% ✅ / 11.56% ✅ | 5.63x ✅ / 7.93x ✅ | **NEAR-MISS — 7/8, only Net Margin fails** |
| **Netwealth Group (ASX:NWL)** [[3]](#src3) | 65.33% ✅ | 15.57% ✅ | ROIC 296.99% (current) / 249.09% (FY26) ✅⚠️ degenerate | **+22.0%** ✅ | ✅ (4/4 yrs) | −0.55 ✅ (net cash) | **1.15% ❌ / 1.24% ❌** | **26.22x ❌ / 24.57x ❌** | **NEAR-MISS — 6/8, both misses pure valuation** ("priced for perfection") |
| **IPH Limited (ASX:IPH)** [[4]](#src4) | 62.72% ✅ | **11.32% ❌** (vs. >12%, 0.68pp short) | ROIC 9.65% (current) / 10.30% (FY26) ❌ | +13.7% ✅ | ✅ (5/5 yrs) | 1.92 ✅ | 15.01% ✅ / 18.04% ✅ | 10.37x ✅ / 8.89x ✅ | **NEAR-MISS — 6/8, misses Net Margin (narrow) + ROIC** |
| **King Slide Works (TPE:2059)** [[5]](#src5) | 76.05% ✅ | 56.21% ✅ | ROIC 254.87% (current) / 168.98% (FY25) ✅⚠️ degenerate | **+30.92%** ✅ | ✅ | −1.44 ✅ (net cash) / −1.81 ✅ | **1.01% ❌ (current) / 2.91% ❌ (FY25)** | **59.30x ❌ (current) / 28.06x ❌ (FY25)** | **NEAR-MISS — 6/8, both misses pure valuation, AI-server re-rating** |
| **F&F Co Ltd (KRX:383220)** [[6]](#src6) | 66.73% ✅ | 20.61% ✅ | ROIC 20.82% (current) / 18.58% (FY25) ✅ | **+2.25% ❌** (vs. >8%, 5.75pp short — wide, not narrow) | **❌** (FY24 FCF −35.8B, large capex spike) | 0.07 ✅ (current) / −0.44 ✅ (FY25) | 19.75% ✅ / 12.88% ✅ | 4.3x ✅ / 4.6x ✅ | **NEAR-MISS — 6/8, misses Rev CAGR (wide) + FCF-3yr streak** |
| **Pinnacle Investment Mgmt (ASX:PNI)** [[7]](#src7) | 44.56% ✅⚠️(flagged unreliable — see gaps) | 161.10% ✅⚠️(flagged unreliable — see gaps) | **ROIC 3.15% (current) / 2.36% (FY26) ❌** | **+34.0%** ✅ | **❌** (FY25 FCF −$145.5M) | −0.27 ✅ (net cash) | 8.65% ✅ / 10.72% ✅ | **19.66x ✅ (current, narrow)** / 129.13x ❌⚠️ (FY, NCI-accounting artifact) | **NEAR-MISS — 6/8 clear, misses ROIC + FCF-streak** (margin figures data-quality-flagged, not face-value) |
| **EQT Holdings (ASX:EQT)** [[8]](#src8) | **35.87% ❌** (vs. >40%, narrow) | 15.82% ✅ | **9.88% (current) / 9.86% (FY26) ❌** | **+5.7% ❌** (vs. >8%) | ✅ (5/5 yrs) | −0.17 ✅ (net cash) | 12.36% ✅ / 9.63% ✅ | 6.88x ✅ / 10.36x ✅ | **FAIL — 3/8 miss, but all three narrow** |
| **Kingdee International (HKG:0268)** [[9]](#src9) | 67.14% ✅ | **1.33% ❌** | **ROIC 0.55% (current) / −4.40% (FY25) ❌** | +12.92% ✅ | ✅ (3 consecutive positive) | −20.02 ✅⚠️ degenerate | 4.71% ✅ (current, flagged) / 2.27% ❌ (FY25) | **N/A ❌** (EBIT negative every FY21–25) | **FAIL — 3/8** (Net Margin, ROIC, EV/EBIT) |
| **Raffles Medical Group (SGX:BSL)** [[10]](#src10) | 45.37% ✅ | **9.22% ❌** | **7.95% (current) / 7.76% (FY25) ❌** | **−2.46% ❌** (COVID-era FY22 base-year artifact, flagged) | ✅ | −1.91 ✅ (net cash) | 4.98% ✅ / 6.55% ✅ | 19.16x ✅ / 15.95x ✅ | **FAIL — 3/8** (Net Margin, ROIC, Rev CAGR) |
| **PropNex (SGX:OYY)** [[11]](#src11) | **10.30% ❌** | **6.30% ❌** | ROE (proxy, ROIC n/d) 61.40% ✅⚠️ | **+2.74% ❌** | ✅ | −2.15 ✅ (net cash) | 6.53% ✅ / 5.99% ✅ | 16.77x ✅ / 16.26x ✅ | **FAIL — 3/8** (Gross Margin, Net Margin, Rev CAGR) |
| **Elite Material Co (TPE:2383)** [[5]](#src5) | **29.83% ❌** | 15.54% ✅ | 33.74% (current) / 39.86% (FY25) ✅ | **+34.57%** ✅ | **❌** (FY23 and TTM both negative — AI-capex ramp) | 0.01 ✅ (FY25) / 0.19 ✅ | **0.42% ❌ (FY25) / −0.08% ❌ (current)** | **30.98x ❌ (FY25) / 64.74x ❌ (current)** | **FAIL — 4/8** (Gross Margin, FCF-3yr, FCF Yield, EV/EBIT) |
| **Hygeia Healthcare Holdings (HKG:6078)** [[2]](#src2) | **25.53% ❌** | **4.10% ❌** | **4.19% (current) / 3.89% (FY25) ❌** | **7.85% ❌** (narrow, near-miss on this one filter alone) | **❌** (FY23 FCF negative) | 1.84 ✅ (FY25) | 6.94% ✅ (FY25, current is a data gap) | 12.94x ✅ (FY25) / 9.82x ✅ (current) | **FAIL — 5/8** (Gross Margin, Net Margin, ROIC, Rev CAGR, FCF-3yr) |
| **Audinate Group (ASX:AD8)** [[12]](#src12) | 81.86% ✅ | **−9.57% ❌** | **−33.66% (current) / −27.80% (FY26) ❌** | **−0.9% ❌** | ✅ (4/4 yrs, real operating FCF despite net loss) | **10.28 ❌⚠️ degenerate** (real net cash, negative-EBITDA artifact) | **0.27% ❌** | **N/A ❌** (EBIT negative) | **FAIL — 6/8** (Net Margin, ROIC, Rev CAGR, leverage-ratio artifact, FCF Yield, EV/EBIT) |
| **Studio Dragon (KOSDAQ:253450)** [[6]](#src6) | **10.74% ❌** | **1.94% ❌** | **5.63% (current) / 4.09% (FY25) ❌** | **−8.73% ❌** | **❌** (FY22 and FY25 both negative) | −0.28 ✅ (current, only pass) | **−0.84% ❌ (current) / −11.42% ❌ (FY25)** | ~13.0x ✅ (current/TTM basis) / ~21.8x ❌ (FY basis, basis-flip flagged) | **FAIL — 6/8** |

---

## ✅ Qualified Quality List — **1 new clean pass: Hugel Inc (KOSDAQ:145020)**

**Hugel clears all 8 Phase 01 filters** — a botulinum-toxin (Botox-equivalent)/aesthetics biologics manufacturer with genuine regulatory/manufacturing moat economics: 78.45% gross margin, 33.14% net margin, net-cash balance sheet, consistent FCF across all 4 fiscal years shown, and an EV/EBIT (~9x) that leaves real headroom versus the 20x cap — none of the eight filters is a knife-edge pass. This is the **first genuinely new clean 8/8 pass on this slice since 08-01** (iFAST, the slice's only other clean pass, dates to 07-04/07-21).

**Qualified-name count vs. prior round: 1 (iFAST) → 2 (iFAST, Hugel)**, plus KRAFTON/ResMed/CSL still flagged pending `/new-position` confirmation from prior rounds (untouched again this round).

**Strongest near-misses this round — a 6-name haul, the second-largest on this slice after 08-22's 5-name round:**
- **New Oriental Education (HKG:9901)** — 7/8, tightest of the round, only Net Margin fails (8.39% vs >12%). Real business-quality caveat: a post-2021-regulatory-shock recovery story in a single-country, policy-sensitive sector, not a steady-state compounder yet.
- **Netwealth Group (ASX:NWL)**, **IPH Limited (ASX:IPH)**, **Pinnacle Investment Management (ASX:PNI)** — three of five AU candidates near-missed, all 6/8. NWL is a clean "priced for perfection" case (valuation-only misses); IPH's misses are narrow (Net Margin by 0.68pp); PNI's headline margin numbers are flagged as unreliable pending segment-level data (see Data Gaps).
- **King Slide Works (TPE:2059)** — 6/8, real business quality (30.9% FY-anchored revenue CAGR, strong balance sheet) but both misses are wide, driven by an AI-server-supply-chain valuation re-rating (EV/EBIT 59.30x current) — the mirror image of 08-22's Largan/Realtek finding on this same slice.
- **F&F Co Ltd (KRX:383220)** — 6/8, but the growth miss (2.25% vs 8%) is wide, not narrow — flagged as a maturing/decelerating licensed-apparel-brand business rather than a genuine near-miss on business quality.

**Confirmed fails (no watchlist value, misses 3+ filters):** EQT Holdings (3 narrow misses — worth a future re-check if any one closes), Kingdee International (3 misses — negative-EBIT software transition), Raffles Medical Group (3 misses — COVID-era base-year distortion), PropNex (3 misses — structurally thin brokerage margins), Elite Material Co (4 misses — AI-capex-driven negative FCF), Hygeia Healthcare (5 misses — real quality gap, not just valuation), Audinate Group (6 misses — currently loss-making), Studio Dragon (6 misses — hit-driven, volatile content business).

---

## Step 3 — Qualitative pass

Per screen.md's batch-processing policy (default batch size 2), the 7 names that cleared or near-missed with real business-quality signal (excluding EQT/Kingdee/Raffles/PropNex/Elite Material/Hygeia/Audinate/Studio Dragon, all either 3+ real misses or flagged as not-genuinely-near) were walked through the 6 qualitative questions in [valuation-scoring.md](../framework/valuation-scoring.md#5-qualitative-questions-before-scoring) across four batches.

### Batch 1 — Hugel Inc & New Oriental Education

#### Hugel Inc (KOSDAQ:145020)

1. **Why are margins high?** Hugel manufactures botulinum-toxin injectables (Botulax) and dermal fillers — a regulated biologic-drug category where GMP manufacturing certification and country-by-country regulatory approval (China already secured; US/EU expansion in progress) create real pricing power, supporting a 78.45% gross margin.
2. **What would it take to compete?** A rival needs years of biologic-manufacturing capability plus separate regulatory approval in every export market it wants to sell into — genuine barriers, though credible global (Allergan/AbbVie's Botox, Ipsen's Dysport, Merz's Xeomin) and domestic (Medytox, Daewoong's Nabota/Jeuveau) competitors already exist, so this is a real but contested moat, not a monopoly.
3. **Capital allocation (5–10yr):** Reinvestment in manufacturing capacity and international regulatory filings; consistently positive FCF across all 4 fiscal years shown, funded from a net-cash balance sheet — no major disclosed M&A in the sourced data.
4. **Where's growth coming from (3–5yr)?** Continued international market expansion (China already approved; pursuing further US/EU approvals) plus filler/aesthetics-adjacent product-line growth.
5. **Best bear case:** Korea's botulinum-toxin industry has a well-documented history of strain-origin and trade-secret litigation between domestic manufacturers (Medytox's disputes with Daewoong/Evolus over toxin-strain provenance played out in US ITC proceedings and courts in the early 2020s) — an industry-structural risk, not one this session independently re-verified against Hugel specifically, but worth flagging as a real qualitative due-diligence item before sizing any position. Single-category (aesthetics/toxin) concentration also makes results sensitive to any one major market's regulatory setback.
6. **Disruption vector:** Low — injectable biologics require physical manufacturing and regulatory approval, not software-substitutable; the more relevant long-run risk is pricing compression as more toxin makers gain approval in more markets over time.

**Conclusion:** A genuine, clean 8/8 pass with real underlying business quality (biologic-manufacturing moat, strong recurring margins, net-cash balance sheet, consistent FCF) — the standout finding of this round. The Korean botulinum-toxin industry's litigation history is a real qualitative flag that should be checked directly against Hugel (not just the industry generally) in any `/new-position` follow-up, per Rule 0's spirit of not assuming away known risks.

#### New Oriental Education & Technology (HKG:9901)

1. **Why are margins high (recovering)?** Originally China's dominant K-12 after-school tutoring franchise; forced to exit core-subject tutoring under the 2021 "double reduction" policy and has spent four-plus years rebuilding around non-subject tutoring, adult/study-abroad education, and a newer livestream e-commerce arm (Dongfang Zhenxuan) — the 54.64% gross margin and still-recovering 8.39% net margin reflect a business still normalizing post-pivot, not a mature steady state.
2. **What would it take to compete?** A three-decade brand-trust relationship with Chinese parents plus (now) a second distinct capability in livestream retail — a real but narrower moat than pre-2021, since the prior protected-category scale advantage was regulated away by policy, not competition.
3. **Capital allocation (5–10yr):** Reinvestment into rebuilding the tutoring-center footprint and building out the livestream e-commerce platform; net-cash balance sheet, no major disclosed M&A.
4. **Where's growth coming from (3–5yr)?** Continued tutoring-center-footprint recovery, adult-education/study-abroad growth, and scaling the livestream e-commerce business as a second leg — though the flagged +23.6% 3yr revenue CAGR anchors off a FY2023 base year that was itself a still-depressed, still-recovering post-crackdown figure, so the headline growth rate likely overstates durability.
5. **Best bear case:** Single-country (China), policy-sensitive-sector concentration is the central risk — the 2021 shock is the entire reason this is a "recovering" story rather than a steady compounder, and further regulatory shifts (education policy, or livestream/e-commerce regulation, an increasingly scrutinized category in China) sit outside what trailing financials can show. The 388.90%/193.17% ROIC print is also a small-invested-capital-denominator artifact (heavy net-cash, light fixed-asset base for an education-services model), not literal capital efficiency.
6. **Disruption vector:** Moderate — the pivot into livestream e-commerce is itself a bet that this newer distribution channel remains durable and un-regulated; competition in Chinese livestream retail is intense and platform algorithm/policy-dependent.

**Conclusion:** The tightest near-miss of the round (7/8, only Net Margin fails by ~3.6pp) — genuinely worth tracking as the net margin normalizes further, but this is a single-country, post-regulatory-shock recovery story, not (yet) a standard "great business" quality name in the sense CSL or ResMed are on this same slice.

### Batch 2 — Netwealth Group & IPH Limited

#### Netwealth Group (ASX:NWL)

1. **Why are margins high?** A wrap/investment-platform administration business for financial advisers and SMSFs — client assets sit off-balance-sheet, so fee revenue scales against a very small invested-capital base, producing high operating margins and the (degenerate) triple-digit ROIC print.
2. **What would it take to compete?** Platform licensing plus adviser-network distribution relationships and a reliability/functionality track record — HUB24 (tested and FAIL on valuation in the 08-22 APAC-EX-JP session) is the direct domestic competitor; real but more a scale/distribution race between a small number of incumbent platforms than a hard technical moat.
3. **Capital allocation (5–10yr):** Organic reinvestment in platform functionality; no major disclosed M&A; net-cash balance sheet.
4. **Where's growth coming from (3–5yr)?** Continued adviser/platform market-share gains as Australian financial advisers consolidate onto fewer wrap platforms — a structurally growing category, though increasingly a two-horse race with HUB24.
5. **Best bear case:** FY26 net income fell sharply ($116.5M → $60.7M, margin 35.9%→15.6%) with no driver identified in the sourced data — a real, unresolved data gap worth checking before trusting the current profitability level; separately, with Netwealth and HUB24 already commanding most of this market, the "easy" multi-year share-gain phase may be largely behind it, consistent with both filter misses here being pure valuation rather than a business-quality problem.
6. **Disruption vector:** Low-moderate — adviser platform-switching costs are real, but a large bank or fund-manager-affiliated platform could still contest share on price/features.

**Conclusion:** A genuine "great business, priced for it" case — 6/8 clear, both misses pure valuation (FCF yield 1.15–1.24%, EV/EBIT 24.57–26.22x) — but the unexplained FY26 net-income drop is a real data gap that should be resolved (via a direct IR/annual-report pull) before treating this purely as a "wait for a better price" story.

#### IPH Limited (ASX:IPH)

1. **Why are margins moderate-high?** An intellectual-property (patent/trademark) attorney-services roll-up spanning ANZ, Asia, Canada, and Europe — mandatory, sticky, low-churn renewal-fee revenue supports the 62.72% gross margin, but professional-services labor costs and acquisition-related amortization compress net margin (11.32%, narrowly missing the >12% bar).
2. **What would it take to compete?** Licensed patent/trademark attorneys (a credentialed profession) plus multi-jurisdiction scale — a real professional-licensing barrier, though a determined competitor could build this organically over time; not a technology moat.
3. **Capital allocation (5–10yr):** A debt-funded acquisition roll-up strategy across multiple attorney-firm brands — net debt (1.92x Net Debt/EBITDA, moderate) reflects this M&A funding rather than distress.
4. **Where's growth coming from (3–5yr)?** Continued bolt-on IP-services-consolidation acquisitions plus organic filing/renewal-volume growth tied to global patent activity.
5. **Best bear case:** Growth has been substantially acquired rather than organic, and integration/acquisition-amortization costs are a recurring, not one-off, drag on ROIC (10.30%, missing the >15% bar by a meaningful margin) and net margin — a roll-up-discipline risk (paying too much for the next acquisition) is the structural concern here, not business-model quality.
6. **Disruption vector:** Low — patent/trademark filing and renewal is a mandatory, regulator-governed process, though AI-assisted patent drafting/search tools could compress labor-hours-per-filing over time without eliminating the category.

**Conclusion:** A narrow 6/8 near-miss (Net Margin misses by only 0.68pp; ROIC by a wider ~4.7pp) — real recurring-revenue quality (mandatory IP renewals) sitting inside a roll-up-driven, not organic-compounder, profitability profile. Worth a re-check next rotation as acquisition-integration costs season.

### Batch 3 — Pinnacle Investment Management & King Slide Works

#### Pinnacle Investment Management (ASX:PNI)

1. **Why do the reported margins look unusual?** Pinnacle is a multi-affiliate asset-management holding company — it takes minority/majority equity stakes in boutique fund managers and earns management/performance fees plus an equity-accounted share of affiliate profit. Large non-controlling-interest and equity-accounted line items sit below revenue, which is why the reported "net margin" (161.10%) isn't a standard operating metric — flagged by this session's research as a genuine data-quality gap rather than a real 161% revenue-to-profit conversion.
2. **What would it take to compete?** A demonstrated track record of identifying and backing successful boutique managers, plus adviser/institutional distribution relationships to raise assets into those affiliates — a relationship- and reputation-based moat, not a statutory one.
3. **Capital allocation (5–10yr):** An ongoing strategy of taking equity stakes in boutique managers (not a classic buyback/dividend-only capital-return profile); net-cash balance sheet.
4. **Where's growth coming from (3–5yr)?** Continued organic AUM growth at existing affiliates plus potential new-affiliate stake acquisitions.
5. **Best bear case:** FY25 FCF turned negative (−$145.5M), breaking the 3-consecutive-year filter; more structurally, active-management-affiliated revenue (management and performance fees together) is directly levered to both markets and manager performance, so a downturn compresses two revenue lines simultaneously. The true quality picture is obscured by the NCI/equity-accounting structure until segment-level (underlying-NPAT) data is examined.
6. **Disruption vector:** Moderate — the decades-long structural shift from active to passive/index investing is a standing headwind for any active-manager-affiliated model, even a diversified multi-boutique one.

**Conclusion:** A near-miss by filter count (misses ROIC and the FCF-streak) but the headline margin figures are unreliable at face value given the NCI/equity-accounting structure — this needs Pinnacle's own segment-level investor-relations disclosures, not just stockanalysis.com's consolidated ratios, before it can be scored with real confidence.

#### King Slide Works (TPE:2059)

1. **Why are margins high?** A precision ball-bearing server-rail-kit manufacturer that has become a key supplier into the AI/GPU hyperscaler server buildout — years of precision-manufacturing know-how plus multi-year OEM/hyperscaler qualification cycles support the 76.05% gross margin, amplified by being positioned exactly where AI-capex demand is currently concentrated.
2. **What would it take to compete?** Comparable precision-manufacturing capability plus the multi-year qualification relationships that server OEMs and hyperscalers require before committing a rail-kit design to production — a real moat, though the extraordinary current margin/ROIC level is partly a "lucky cycle" effect (AI capex supercycle) layered on top of genuine engineering capability, per the framework's own qualitative-question framing.
3. **Capital allocation (5–10yr):** Organic capacity reinvestment; large net-cash balance sheet; no major disclosed M&A.
4. **Where's growth coming from (3–5yr)?** Continued AI/GPU server buildout demand — the +30.92% FY-anchored 3yr revenue CAGR is a real current-cycle number, not a base-year artifact (unlike some of this slice's other near-misses).
5. **Best bear case:** A cyclical, customer-concentrated hardware-supply-chain business riding a capex supercycle — this framework's own prior findings on this exact slice (Largan Precision and Realtek Semiconductor in the 08-22 session, which saw the *opposite* move: FY-basis passes turning into current-basis misses on large price run-ups) show these AI-supply-chain re-ratings can move fast in either direction. King Slide's valuation has already run well ahead of even its strong current fundamentals (EV/EBIT 59.30x current vs. 28.06x on an already-rich FY2025 basis).
6. **Disruption vector:** Low on the underlying mechanical-precision category itself; the more relevant near-term risk is customer-concentration/cycle risk (a hyperscaler capex slowdown, or a shift to a different rail/chassis design standard) rather than technological obsolescence.

**Conclusion:** Genuine business-quality near-miss (6/8, only valuation-side filters fail) — but both misses are wide, driven by an AI-capex-cycle re-rating, not narrow price noise. A name to re-check for a better entry point if the re-rating partially reverses, not a current buy candidate under this framework's valuation discipline.

### Batch 4 — F&F Co Ltd

#### F&F Co Ltd (KRX:383220)

1. **Why are margins high?** A licensed-brand fashion company (MLB and MLB KIDS under license from MLB Properties, plus owned/licensed DISCOVERY Expedition, DUVETICA, SUPRA, SERGIO TACCHINI, and BANILA CO skincare) — brand/IP-licensing economics, not manufacturing scale, drive the 66.73% gross margin.
2. **What would it take to compete?** The underlying brand license itself (which MLB Properties could in principle decline to renew or re-license to a competitor) plus retail/distribution execution across Korea and China — a real but licensing-contract-dependent moat, meaningfully weaker than an owned-IP business like Hugel's biologic manufacturing.
3. **Capital allocation (5–10yr):** A large, unexplained FY2024 capex spike (−434,641M KRW vs. a normal ~17–24B KRW annual run-rate) drove that year's FCF negative — the specific driver (a facility build, a brand investment, a JV) is a genuine, unresolved data gap from this session's sourced data.
4. **Where's growth coming from (3–5yr)?** Continued MLB-brand expansion in Korea/China plus BANILA CO skincare and other brand growth — though the +2.25% 3yr revenue CAGR (vs. the >8% bar) shows deceleration, not acceleration, over the trailing period.
5. **Best bear case:** Single-brand-license concentration (MLB is the dominant profit driver) plus heavy Korea/China market concentration shows up directly in the numbers — ROIC decelerated from 40.78% (FY22) to 18.58% (FY25), consistent with either Chinese consumer-discretionary softness or a normalizing licensing-economics cycle, not a one-off. A license non-renewal, or renegotiation on worse terms, is a structural risk unique to a licensed-brand model that an owned-IP business doesn't carry.
6. **Disruption vector:** Low-moderate — fashion/apparel brand relevance can fade for reasons entirely unrelated to technology (shifting consumer taste, or a licensor choosing a different local partner at contract renewal) — a real long-run risk specific to single-brand-license dependence.

**Conclusion:** A near-miss by filter count (misses only Rev CAGR and the FCF-streak) but the growth miss is wide (2.25% vs. 8%, not a graze), and the ROIC deceleration trend plus the unexplained capex spike are real quality flags, not just data noise. Reads as a maturing/decelerating licensed-brand business rather than a fast-growing compounder despite clearing 6/8 filters.

---

## Step 4 — Data gaps flagged (per CLAUDE.md Rule 0 — none estimated)

- **F&F Co Ltd — ticker ambiguity resolved, not assumed.** The initial guess (KRX:007700) is actually **F&F Holdings Co., Ltd.**, the post-2022-split holding company; the operating apparel business (MLB, Discovery Expedition, etc.) trades separately as **KRX:383220**. All figures above are for 383220, confirmed via `stockanalysis.com`'s search endpoint before pulling financials.
- **Pinnacle Investment Management — Gross Margin (44.56%) and Net Margin (161.10%) flagged as unreliable, not face-value.** Pinnacle's multi-affiliate structure books large non-controlling-interest and equity-accounted-affiliate items below the revenue line; a >100% net margin cannot be a genuine operating conversion ratio. Neither figure was invented — both are as reported by stockanalysis.com — but they are flagged as needing segment-level/underlying-NPAT data (not available from this source) before being trusted for scoring.
- **Kingdee International — EV/EBIT undefined, not estimated.** Operating Income (EBIT) has been negative every fiscal year 2021–2025; stockanalysis.com's ratio table omits the multiple entirely for this reason. Treated as a fail on this filter rather than backed into a number.
- **Audinate Group — EV/EBIT undefined (negative EBIT) and Net Debt/EBITDA numerically degenerate.** The company holds a genuine ~$62.8M net-cash position, but with negative EBITDA the ratio computes to a nominal +10.28x that reads as dangerous leverage when the actual balance-sheet risk is low — shown per the literal filter definition but flagged as not meaningful.
- **Audinate — revenue path unusually volatile** (FY23 $69.7M → FY24 $91.5M → FY25 $62.1M → FY26 $67.8M, a ~32% single-year drop then partial recovery) — sourced, not invented, but flagged as worth independent corroboration against Audinate's own filings before further reliance.
- **Netwealth Group — FY26 net-income decline ($116.5M → $60.7M) has no identified driver** in the sourced income-statement/cash-flow data. Flagged as a genuine open item for a follow-up `/new-position` pull of the FY26 annual report or investor presentation, not assumed to be a one-off.
- **New Oriental — FY2026 free-cash-flow line-item inconsistency.** The cash-flow fetch returned FY2026 FCF identical to Operating Cash Flow ($1,027M) despite a disclosed capex of −$241.94M, which arithmetically should reduce FCF to ~$785M — likely a data-extraction artifact. Not used for the pass/fail determination since FY2024/FY2025 FCF (both clean, positive, and internally consistent) already establish the 3-year-positive result independent of this figure.
- **New Oriental / Hugel / King Slide / Netwealth / Studio Dragon — extreme or degenerate ROIC readings** (New Oriental 193–389%, King Slide 169–255%, Netwealth 249–297%) are flagged as small-invested-capital-denominator artifacts typical of asset-light or net-cash-heavy businesses, consistent with the TechnologyOne/Pro Medicus/eMemory precedent from prior APAC-EX-JP rounds — ROE or a qualitative cross-check is used alongside rather than treating the raw ROIC number as literal capital efficiency.
- **Elite Material Co — FCF trend currently negative**, both historically (FY23: −391.22M TWD) and on a trailing basis (TTM: −1,486M TWD), driven by a heavy AI-driven capex ramp (TTM capex −15,172M TWD) even as operating cash flow remains strong and growing (TTM 13,685M TWD) — a capex-timing story, not an operating-profitability problem, but it fails the filter as literally defined.
- **King Slide Works & Elite Material Co — confirmed large AI-supply-chain price run-ups flipping valuation verdicts more severely on a current-price basis than an already-rich FY2025 basis** — EV/EBIT for both names is worse on the current/live-price basis (59.30x and 64.74x) than on the FY2025 basis (28.06x and 30.98x, both already failing). Checked explicitly per the task brief; live price is not inferred from any multiple, per Rule 0.
- **Studio Dragon — genuine current-vs-FY basis flip on EV/EBIT** (current-EV/TTM-EBIT ~13.0x, a nominal pass, vs. current-EV/FY2025-EBIT ~21.8x, a fail) because TTM EBIT recovered materially versus a weak FY2025 — doesn't change the overall FAIL verdict, since 5 other filters miss outright regardless of this one filter's basis sensitivity.
- **Hygeia Healthcare — current-basis FCF yield is a data gap** (stockanalysis.com's ratio table returns "—" for this cell); FY2025's 6.94% figure was used instead and flagged, not treated as a live figure. Balance-sheet "Net Cash/Debt" also doesn't cleanly reconcile against Total Debt − Cash on the same page (likely a lease-liability treatment difference) — the directly-disclosed Net Debt/EBITDA ratio was used rather than a manual recomputation, to avoid compounding the discrepancy.
- **Raffles Medical Group — FY2022 revenue spike and FY2021 gross-margin outlier**, both consistent with extraordinary COVID-19 testing/vaccination revenue that has since rolled off. Because the FY-anchored 3yr CAGR anchors off this inflated FY2022 base, the computed growth rate reads as negative (−2.46%) even though revenue has been flat-to-slightly-growing since (708→752→765M SGD, FY23–25) — correct per the strict FY-anchored rule, but the underlying growth story likely reads differently ex-COVID.
- **PropNex — ROIC not disclosed; ROE used as the framework's proxy**, per the explicit fallback rule. The resulting 56.90–61.40% figure reflects a thin required equity base in an asset-light brokerage model, not comparable capital efficiency to a manufacturer or franchise business — flagged, not treated as a genuine quality signal.
- **Cross-currency ratio sourcing (Kingdee/Hygeia report in CNY, New Oriental in USD, all three quoted in HKD; F&F/Studio Dragon/Hugel report and quote in KRW):** all ratio figures were taken directly from stockanalysis.com's own pre-computed, currency-reconciled ratio pages rather than manually recombining local-currency financials against foreign-currency price/EV data, to avoid an FX-conversion error of the kind flagged in this framework's SPGI lesson.

---

## Sources

<a id="src1"></a>[1] Hugel Inc: https://stockanalysis.com/quote/kosdaq/145020/financials/ratios/ , https://stockanalysis.com/quote/kosdaq/145020/financials/ , https://stockanalysis.com/quote/kosdaq/145020/financials/cash-flow-statement/ , https://stockanalysis.com/quote/kosdaq/145020/financials/balance-sheet/
<a id="src2"></a>[2] New Oriental Education (HKG:9901) / Hygeia Healthcare (HKG:6078): https://stockanalysis.com/quote/hkg/9901/financials/ratios/ , https://stockanalysis.com/quote/hkg/9901/financials/ , https://stockanalysis.com/quote/hkg/9901/financials/cash-flow-statement/ , https://stockanalysis.com/quote/hkg/9901/financials/balance-sheet/ , https://stockanalysis.com/quote/hkg/6078/financials/ratios/ , https://stockanalysis.com/quote/hkg/6078/financials/ , https://stockanalysis.com/quote/hkg/6078/financials/cash-flow-statement/ , https://stockanalysis.com/quote/hkg/6078/financials/balance-sheet/
<a id="src3"></a>[3] Netwealth Group: https://stockanalysis.com/quote/asx/NWL/financials/ratios/ , https://stockanalysis.com/quote/asx/NWL/financials/ , https://stockanalysis.com/quote/asx/NWL/financials/cash-flow-statement/ , https://stockanalysis.com/quote/asx/NWL/financials/balance-sheet/
<a id="src4"></a>[4] IPH Limited: https://stockanalysis.com/quote/asx/IPH/financials/ratios/ , https://stockanalysis.com/quote/asx/IPH/financials/ , https://stockanalysis.com/quote/asx/IPH/financials/cash-flow-statement/ , https://stockanalysis.com/quote/asx/IPH/financials/balance-sheet/
<a id="src5"></a>[5] King Slide Works (TPE:2059) / Elite Material Co (TPE:2383): https://stockanalysis.com/quote/tpe/2059/financials/ratios/ , https://stockanalysis.com/quote/tpe/2059/financials/ , https://stockanalysis.com/quote/tpe/2059/financials/cash-flow-statement/ , https://stockanalysis.com/quote/tpe/2383/financials/ratios/ , https://stockanalysis.com/quote/tpe/2383/financials/ , https://stockanalysis.com/quote/tpe/2383/financials/cash-flow-statement/
<a id="src6"></a>[6] F&F Co Ltd (KRX:383220) / Studio Dragon (KOSDAQ:253450): https://stockanalysis.com/quote/krx/383220/financials/ratios/ , https://stockanalysis.com/quote/krx/383220/financials/ , https://stockanalysis.com/quote/krx/383220/financials/cash-flow-statement/ , https://stockanalysis.com/quote/kosdaq/253450/financials/ratios/ , https://stockanalysis.com/quote/kosdaq/253450/financials/ , https://stockanalysis.com/quote/kosdaq/253450/financials/cash-flow-statement/
<a id="src7"></a>[7] Pinnacle Investment Management: https://stockanalysis.com/quote/asx/PNI/financials/ratios/ , https://stockanalysis.com/quote/asx/PNI/financials/ , https://stockanalysis.com/quote/asx/PNI/financials/cash-flow-statement/ , https://stockanalysis.com/quote/asx/PNI/financials/balance-sheet/
<a id="src8"></a>[8] EQT Holdings: https://stockanalysis.com/quote/asx/EQT/financials/ratios/ , https://stockanalysis.com/quote/asx/EQT/financials/ , https://stockanalysis.com/quote/asx/EQT/financials/cash-flow-statement/ , https://stockanalysis.com/quote/asx/EQT/financials/balance-sheet/
<a id="src9"></a>[9] Kingdee International Software Group: https://stockanalysis.com/quote/hkg/0268/financials/ratios/ , https://stockanalysis.com/quote/hkg/0268/financials/ , https://stockanalysis.com/quote/hkg/0268/financials/cash-flow-statement/ , https://stockanalysis.com/quote/hkg/0268/financials/balance-sheet/
<a id="src10"></a>[10] Raffles Medical Group: https://stockanalysis.com/quote/sgx/BSL/financials/ratios/ , https://stockanalysis.com/quote/sgx/BSL/financials/ , https://stockanalysis.com/quote/sgx/BSL/financials/cash-flow-statement/
<a id="src11"></a>[11] PropNex: https://stockanalysis.com/quote/sgx/OYY/financials/ratios/ , https://stockanalysis.com/quote/sgx/OYY/financials/ , https://stockanalysis.com/quote/sgx/OYY/financials/cash-flow-statement/
<a id="src12"></a>[12] Audinate Group: https://stockanalysis.com/quote/asx/AD8/financials/ratios/ , https://stockanalysis.com/quote/asx/AD8/financials/ , https://stockanalysis.com/quote/asx/AD8/financials/cash-flow-statement/ , https://stockanalysis.com/quote/asx/AD8/financials/balance-sheet/

Ticker-verification fetches: `https://stockanalysis.com/api/search?q=Raffles%20Medical`, `?q=PropNex`, `?q=King%20Slide`, `?q=Elite%20Material`, `?q=Hugel`, `?q=Studio%20Dragon`, `?q=F%26F%20Co` (the last confirmed the 007700-holding-company vs. 383220-operating-company split).

---

## Next steps

- **Recommend `/new-position` on Hugel Inc (KOSDAQ:145020)** — the clean 8/8 pass, subject to a direct check of the Korean botulinum-toxin industry's litigation history against Hugel specifically (flagged in Step 3, not independently verified this session) before sizing any position.
- **Watchlist adds (near-misses):** New Oriental Education (HKG:9901, 7/8 — track Net Margin normalization and China ed-policy risk); Netwealth Group (ASX:NWL, 6/8 — valuation-only, also resolve the unexplained FY26 net-income drop); IPH Limited (ASX:IPH, 6/8 — narrow Net Margin/ROIC miss); Pinnacle Investment Management (ASX:PNI, 6/8 — needs segment-level data before real scoring); King Slide Works (TPE:2059, 6/8 — real quality, priced for an AI-capex cycle that may not persist); F&F Co Ltd (KRX:383220, 6/8 — wide growth miss, decelerating licensed-brand story).
- **Categorization open item:** resolve whether mainland-China-domiciled-but-HK-listed names (this round: Kingdee, Hygeia, New Oriental) belong under APAC-EX-JP or EM going forward — flagged in the Methodology section above, not resolved unilaterally this session.
- **EQT Holdings and Kingdee International** — both 3-filter FAILs where every miss is comparatively narrow; worth a re-check next rotation rather than dropping outright.
- Coverage log updated below.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate between a start and end value over several years.
- **CDMO** — Contract Development and Manufacturing Organization (referenced for comparison in prior sessions; not directly applicable here).
- **EBIT** — Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
- **EV/EBIT, EV/EBITDA** — Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure.
- **FCF (Free Cash Flow)** — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper.
- **Fiduciary/trustee services** — professional services (e.g. EQT Holdings) where a firm is legally obligated to act in a client's best interest, typically for estates, trusts, or superannuation funds.
- **Gross Margin** — Gross Profit (Revenue − Cost of Revenue) ÷ Revenue.
- **NCI (Non-Controlling Interest)** — the portion of a subsidiary's (or affiliate's) profit or equity that belongs to other shareholders, not the parent company — relevant to Pinnacle's multi-affiliate accounting structure.
- **Net Debt/EBITDA** — net debt (total debt minus cash) divided by EBITDA — a leverage ratio; "net cash" means the figure is negative (more cash than debt).
- **Net Margin** — Net Income ÷ Revenue.
- **Qualified Quality List** — the output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring.
- **ROE** — Return on Equity — Net Income ÷ shareholder equity.
- **ROIC** — Return on Invested Capital — a core quality signal in this framework; can be distorted (pushed to extreme values) for asset-light or net-cash-heavy businesses with a very small invested-capital denominator.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results, used to pair a live/current price with recent trailing fundamentals.
- **Wrap platform** — an investment-administration platform (e.g. Netwealth, HUB24) that financial advisers use to hold, trade, and report on client investment portfolios in one consolidated account.

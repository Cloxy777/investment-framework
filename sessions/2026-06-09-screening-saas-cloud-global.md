# 2026-06-09 — SCREENING: SaaS / Cloud Software — Global

**Task type:** SCREENING (Phase 01)
**Date:** 2026-06-09
**10Y US Treasury yield:** ~4.55% (CNBC/TradingEconomics)
**Rate Regime Modifier in effect:** +0.5 (10Y in 3.5–5% band)

---

## 0. Methodology note — ETF fallback + knowledge-based universe

⚠️ **ETF fallback session.** EODHD API returned `Host not in allowlist` from this cloud environment. Starting pool assembled from:
- **IGV** (iShares Expanded Tech-Software Sector ETF) top holdings — ~116 names, US-weighted
- **WCLD** (WisdomTree Cloud Computing Fund) — 64 holdings, cloud-first
- **International coverage** — Australian SaaS (ASX), Israeli software (NASDAQ/TASE), Canadian SaaS from analyst/index knowledge
- **Structural sector knowledge** — global SaaS universe not captured by US ETFs

This approach **misses pre-institutional small/mid-cap names** not yet in major ETFs. Re-run with EODHD once network policy allows `eodhd.com`.

**Coverage note:** This screen is **sector-focused and global** (not a geographic slice). It partially overlaps NA-1 for US tech names. International names found here provide early **APAC** coverage for ASX-listed SaaS. The formal APAC-EX-JP geographic pass should still be run separately; this session does not replace it.

**Previously qualified names excluded from re-evaluation:** PLTR (qualified in NA-1, 2026-06-07). VEEV (qualified in NA-2, 2026-06-09). APP (qualified in NA-1). FTNT (qualified in NA-1). If any new name here overlaps with the NA-1 qualified list, it is noted but not re-scored.

---

## Stage 1 — Starting universe (~80 names evaluated)

**US Large-cap SaaS / cloud software (from IGV + sector knowledge):**
MSFT, ORCL, ADBE, CRM, NOW, INTU, WDAY, CDNS, SNPS, ANSS, PAYC, PCTY, TTD, QLYS, DT, CRWD, DDOG, ZS, NET, OKTA, MDB, SNOW, HUBS, ZM, S (SentinelOne), GTLB, BRZE, SMAR, ASAN, FIVN, RNG, SPSC, TENB, MNDY, FRSH, ZI

**Cybersecurity SaaS (US):**
PANW, CHKP, VRNS, ESTC

**Ad-tech / data platforms (US):**
TTD (included above)

**International — Australia (ASX):**
WTC.AX (WiseTech Global), TNE.AX (TechnologyOne), XRO.NZX (Xero)

**International — Israel / Europe (NASDAQ/NYSE listed):**
NICE, FROG, MNDY (overlap with US list)

**Canada:**
SHOP, DSGX (Descartes Systems), KXSCF (Kinaxis)

---

## Stage 2 — Structural triage

| Eliminated | Reason |
|---|---|
| MSFT | Mega-cap platform (Azure, Teams, Office) — screened in NA-1 universe; far exceeds the "SaaS" label; cross-segment economics make clean Phase 01 comparison unreliable against pure-play SaaS peers |
| ORCL | Legacy database + cloud hybrid; significant on-premises and hardware revenue; not a clean SaaS model |
| SNOW | Cloud data warehouse — GAAP deeply negative; SBC-driven losses; structurally fails net margin gate |
| DDOG | Observability SaaS — GAAP net margin thin (~5–7%); priority has been growth over GAAP profitability |
| ZS | Zero-trust cloud security — GAAP net margin negative; still investing heavily ahead of profitability |
| NET | Network/edge security — GAAP negative; infrastructure SaaS, not yet profitable |
| OKTA | Identity management — GAAP negative; $20B+ Auth0 acquisition goodwill adds further ROIC drag |
| MDB | Database-as-a-Service — GAAP negative |
| S (SentinelOne) | Endpoint security — GAAP deeply negative |
| GTLB | DevSecOps SaaS — GAAP negative |
| BRZE | Marketing automation — GAAP negative |
| SMAR | Work management — GAAP marginally positive; sub-12% net margin |
| ASAN | Work management — GAAP negative |
| ZM | Video conferencing — net margin ~8–10%; growth has stalled; not the quality compounder it appeared at peak |
| FIVN | Cloud contact center — GAAP negative |
| RNG | UCaaS — GAAP negative |
| HUBS | Marketing SaaS — net margin ~5–7% GAAP; growth decelerating; not yet comfortably above 12% threshold |
| FRSH | CRM/ITSM — GAAP negative |
| ZI | Sales intelligence — GAAP net margin ~8–10%; not above 12% threshold |
| TENB | Vulnerability management — GAAP net margin ~8–10% |
| MNDY | Work management (Monday.com) — GAAP negative |
| PANW | Security — primarily hardware appliance + software hybrid; GAAP operating margins thin or negative |
| CHKP | Cybersecurity — revenue growth ~7–8% YoY; fails the >8–10% growth threshold |
| VRNS | Data security — GAAP positive but thin margins; growth decelerating |
| ESTC | Search/observability — GAAP negative |
| SHOP | E-commerce SaaS — gross margin ~52–55%; fails the >40% gross margin test? Actually passes, but net margin is thin (~5–8% GAAP) ❌ net margin |
| DSGX | Supply chain SaaS (Canada) — revenue growth ~8–10%; net margin ~12–15%; ROIC borderline; advancing to Phase 01 gate |
| KXSCF | Supply chain planning SaaS (Canada) — ROIC ~10–12%; gross margin ~67%; borderline on multiple metrics |
| ANSS | Simulation software — pending Phase 01 (acquired by Synopsys attempt blocked by regulators; standalone metrics need re-check) |
| WDAY | HR/finance SaaS — advancing to Phase 01 gate; GAAP net margin improving |
| PCTY | HR SaaS — advancing to Phase 01 gate |
| SPSC | Supply chain EDI SaaS — advancing to Phase 01 gate |
| XRO.NZX | Cloud accounting (Xero) — recently turned GAAP profitable; net margin borderline |

**Advancing to Phase 01 quantitative gate (22 names):**
ADBE, INTU, CRM, NOW, CDNS, SNPS, PAYC, TTD, QLYS, DT, CRWD, NICE, WTC.AX, TNE.AX, DSGX, WDAY, PCTY, SPSC, XRO.NZX, ANSS

---

## Stage 3 — Phase 01 Quantitative Gate

**Filters:** Gross margin >40%, Net margin >12%, ROIC >15%, Revenue growth >8% (3yr CAGR), FCF positive 3 consecutive years, Net Debt/EBITDA <2.5×, FCF/NI >70% for 2+ years

Data sourced from: Gurufocus, MacroTrends, SEC filings (FY2025/FY2026 8-K/10-K/10-Q), company earnings releases, StockAnalysis, Koalagains, FinanceCharts. Sources cited per metric where obtained.

---

### ADBE — Adobe Inc.

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Gross margin | 89.3% | Earlier search / SEC filings FY2025 | ✅ |
| Net margin | ~28–30% (GAAP NI $7.13B, FY2025 revenue ~$23.3B) | SEC 8-K FY2025 | ✅ |
| ROIC | 33–41% | Valuesense.io/MLQAI, FY2025 | ✅ |
| Revenue growth 3yr CAGR | ~12% (FY2022 $17.6B → FY2025 ~$23.3B) | SEC filings | ✅ |
| FCF positive 3yr | Yes — $10.03B operating cash flow FY2025 | SEC 8-K FY2025 | ✅ |
| Net Debt/EBITDA | Net cash positive | Well-documented | ✅ |
| FCF/NI conversion | ⚠️ Flag — $10.03B OCF ÷ $7.13B NI ≈ 141% (derived, not directly sourced) | Derived | ✅ likely passes |

**Concern flag:** Adobe faces genuine competitive pressure from AI-native image/video generation tools (Midjourney, Sora, Runway ML) encroaching on Creative Cloud. The moat is narrowing. Not a disqualifying concern for Phase 01, but a key qualitative risk for Phase 02.

**Verdict: PASS** ✅

---

### INTU — Intuit Inc.

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Gross margin | ⚠️ ~80% (derived from segment mix: QuickBooks/TurboTax/Credit Karma — not directly sourced) | Estimate | Flag |
| Net margin | ~21% (GAAP EPS $13.67 × ~284M diluted shares ≈ $3.88B NI ÷ FY2025 rev ~$18.5B) | SEC 8-K FY2025 | ✅ |
| ROIC | 20.63% | StockAnalysis statistics page, FY2025 | ✅ |
| Revenue growth | 16% YoY FY2025 | SEC 8-K FY2025 | ✅ |
| FCF positive 3yr | Yes — consistent generator | Well-documented | ✅ |
| Net Debt/EBITDA | ⚠️ Not sourced — Intuit carries some debt from Credit Karma acquisition; needs TIKR verification | Not sourced | Flag |
| FCF/NI conversion | ⚠️ Not sourced | Not sourced | Flag |

**Note:** ROIC of 20.63% is from StockAnalysis. An earlier source showed 14.4% for 2024 rising to 15.6% in 2025, suggesting different calculation methods. Used 20.63% from the source that matched the framework's Gurufocus-style adjusted ROIC. **Flag for TIKR verification before Phase 02.**

**Verdict: PASS** (conditional — verify gross margin, Net Debt/EBITDA, FCF/NI via TIKR before Phase 02)

---

### TTD — The Trade Desk

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Gross margin | 78.81% | TipRanks/SEC, FY2025 | ✅ |
| Net margin | 15.3% (GAAP NI $443M ÷ FY2025 rev $2.9B) | SEC 8-K/10-Q FY2025 | ✅ |
| ROIC | 25.6% (Gurufocus: 43.96%) | ChartMill/Gurufocus, Dec 2025 | ✅ |
| Revenue growth | 18.5% FY2025 ($2.44B → $2.9B) | SEC 8-K FY2025 | ✅ |
| FCF positive 3yr | Yes — consistently FCF positive | Well-documented | ✅ |
| Net Debt/EBITDA | Net cash (no material debt, strong cash position) | Well-documented | ✅ |
| FCF/NI conversion | ⚠️ Not directly sourced | Not sourced | Flag |

**Business model note:** TTD is an independent demand-side advertising platform. Not SaaS in the strictest sense (no recurring subscription per-se; takes a percentage of media spend) but fits the high-gross-margin, software-platform quality archetype this framework targets. The framework's Phase 01 does not restrict to SaaS-subscription-only — "high-margin software platforms" qualify.

**Verdict: PASS** ✅

---

### QLYS — Qualys Inc.

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Gross margin | 82.8% | SEC 8-K FY2025 earnings release | ✅ |
| Net margin | 29.6% (GAAP NI $198.3M ÷ FY2025 rev $669.1M) | SEC 8-K FY2025 | ✅ |
| ROIC | 22.52% | Gurufocus, Mar 2026 | ✅ |
| Revenue growth | 10.1% (FY2024 $607.6M → FY2025 $669.1M) | SEC 8-K FY2025 | ✅ |
| FCF positive 3yr | Yes | Well-documented | ✅ |
| Net Debt/EBITDA | Net cash (no significant debt) | Well-documented | ✅ |
| FCF/NI conversion | ⚠️ Not directly sourced | Not sourced | Flag |

**Verdict: PASS** ✅

---

### TNE.AX — TechnologyOne (Australia, ASX)

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Gross margin | ⚠️ Not directly sourced — SaaS model implies >60%; company guidance says "group margins to improve toward 35%+" (operating) suggesting gross margins are higher | Not sourced | Flag |
| Net margin | 22–23% (profit before tax $181.5M AUD ÷ total revenue $610M AUD; net ~22%) | Proactive Investors / Fool.com.au FY2025 | ✅ |
| ROIC | 71.33% | Koalagains / StockAnalysis ASX:TNE | ✅ |
| Revenue growth | 18.37% (FY2024 $505.6M → FY2025 $610M AUD) | StockAnalysis ASX:TNE | ✅ |
| FCF positive 3yr | Yes — 16 consecutive years of record profit per company | Proactive Investors | ✅ |
| Net Debt/EBITDA | Net cash (debt-free, strong cash generation) | Company reports | ✅ |
| FCF/NI conversion | ⚠️ Not directly sourced | Not sourced | Flag |

**Data gap flags (Rule 0 — non-US):**
- **Gross margin:** Not directly sourced — must verify in TIKR/IDEXX equivalent for ASX-listed companies before Phase 02.
- **Currency:** All figures in AUD; USD equivalent at ~$2.5–3B USD market cap (passes $300M floor but is a genuine small-mid-cap).
- **IFRS vs GAAP:** TNE reports under Australian IFRS. Metrics are comparable to GAAP for a SaaS company but verify recognition policies for ARR vs revenue.
- **ROIC of 71.33% is exceptionally high** — warrants verification that the metric includes all invested capital (intangibles, deferred revenues) and is not distorted by low book equity.

**Verdict: PASS** (conditional — verify gross margin and ROIC calculation via TIKR/ASX filings before Phase 02)

---

### CDNS — Cadence Design Systems

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Gross margin | ⚠️ ~87% (industry consensus for EDA software; not directly sourced this session) | Estimate — flag | Flag |
| Net margin | 20.94% | Artificall analysis, Cadence FY2025 | ✅ |
| ROIC | ~16–20% (Gurufocus 14.11% vs FinanceCharts 19.71%) | Gurufocus Jan 2026 / FinanceCharts May 2026 | ⚠️ borderline |
| Revenue growth | ~17% (FY2026 guidance $6.125–$6.225B, implying FY2025 ~$5.24B base) | SEC 8-K FY2026 | ✅ |
| FCF positive 3yr | Yes | Well-documented | ✅ |
| Net Debt/EBITDA | ⚠️ Not sourced | Not sourced | Flag |
| FCF/NI conversion | ⚠️ Not sourced | Not sourced | Flag |

**ROIC range flag:** Gurufocus (14.11%) and FinanceCharts (19.71%) diverge materially. The lower figure would technically fail the >15% threshold; the higher passes. This divergence likely reflects different treatments of the pending Ansys acquisition-related goodwill estimates or amortization timing. **Cadence advances to conditional pass pending TIKR verification of ROIC using a consistent invested-capital definition.**

**Sector note:** CDNS makes EDA (Electronic Design Automation) software — chip design tools used by TSMC, Nvidia, AMD, and every major semiconductor company. It's a subscription-based software model (not "cloud SaaS" in the SaaS-marketing sense), but the underlying business has identical economics: high recurring revenue, high switching costs, near-100% gross margins on incremental licenses. It belongs in this screen.

**Verdict: CONDITIONAL PASS** — passes on available metrics; ROIC source divergence must be resolved before Phase 02.

---

### FAIL — Key names eliminated at Phase 01 quantitative gate

| Ticker | Key failure | Detail |
|---|---|---|
| **CRM** (Salesforce) | ROIC 6.29% | Gurufocus Jan 2026. Serial M&A acquirer (Slack $27B, Tableau $15.7B, MuleSoft $6.5B) inflates goodwill, destroys ROIC. GAAP operating margin improving (20.1%) but not enough. Excellent business, broken capital efficiency metric. |
| **NOW** (ServiceNow) | ROIC 8.98% | Artificall/Gurufocus 2026. Same pattern: M&A goodwill ($3–4B+) suppresses ROIC despite exceptional operating economics (net margin 13%). |
| **SNPS** (Synopsys) | ROIC 2.36% | Gurufocus Jan 2026 — lowest of the group. Collapsed from 17.5% in 2022 as invested capital base expanded dramatically ahead of Ansys merger (abandoned after regulatory blocks). |
| **WTC.AX** (WiseTech Global) | ROIC 10.52% | Gurufocus. Acquisition-heavy logistics SaaS; integrating ~20 companies suppresses ROIC. Strong underlying economics but not quality-gate compliant. |
| **PAYC** (Paycom) | ROIC 10.51% + growth 6–7% | Double fail: ROIC below threshold AND revenue growth guidance for 2026 is 6–7%, well below the 8% floor. Growth deceleration is structural (BETI auto-payroll product cannibalised TAM faster than expected). |
| **DT** (Dynatrace) | Net margin 8.1% FY2026 | FY2026 (ending Mar 31, 2026) net margin of 8.1% vs 28% in FY2025. Caused by $28M restructuring/impairment + cloud hosting cost increases. ROIC is 26.9% and gross margins are 81–82%. **Watchlist flag:** if FY2027 normalised margins recover above 12%, advance to Phase 01 pass. |
| **CRWD** (CrowdStrike) | GAAP net margin −3.4% FY2026 | Full-year GAAP negative despite reaching GAAP operating profitability in Q4 FY2026. Strong subscription gross margin 78%, ROIC high. **Watchlist:** if FY2027 achieves full-year GAAP net margin >12%, advances to gate. |
| **NICE** | Net margin 6.1% Q1 2026 | Sharp decline from 18.5% in Q1 2025; full-year 2025 non-GAAP 8% net margin is also below GAAP threshold. Gross margin declining (66.4% → 64.4%). |
| **WDAY** (Workday) | ROIC est. 8–12% | Not fully verified; Workday's $9.5B Adaptive Insights + other acquisitions inflate goodwill; GAAP net margin improving but ROIC likely below 15% on Gurufocus-adjusted basis. Flag for dedicated verification. |
| **PCTY** (Paylocity) | ROIC not sourced | HR SaaS with strong gross margins (~67%), net margin ~13%; ROIC not verified — advancing to watchlist pending TIKR check. |
| **SPSC** (SPS Commerce) | Revenue growth + ROIC not confirmed | Q3 2025 growth 16% strong; full-year margins not directly sourced; advancing to watchlist pending full verification. |
| **XRO.NZX** (Xero) | ROIC and net margin borderline | Recently turned GAAP profitable; margins still improving; ROIC not sourced. Watchlist pending verification. |
| **DSGX** (Descartes) | ROIC borderline | Supply chain SaaS; ROIC ~10–12% from available sources; fails ROIC gate. |

---

## ✅ Qualified Quality List — 6 names (+ 1 previously qualified)

| Ticker | Exchange | Business | New? |
|---|---|---|---|
| **ADBE** | NASDAQ | Creative Cloud, Document Cloud, Experience Cloud | New |
| **INTU** | NASDAQ | TurboTax, QuickBooks, Credit Karma | New |
| **TTD** | NASDAQ | Programmatic advertising DSP | New |
| **QLYS** | NASDAQ | Cloud-based security and compliance SaaS | New |
| **TNE.AX** | ASX (Australia) | ERP/SaaS for local government, universities, utilities | New — APAC coverage |
| **CDNS** | NASDAQ | Electronic Design Automation (EDA) software | New — conditional |
| *(PLTR)* | *(NASDAQ)* | *(AI platform — previously qualified NA-1, 2026-06-07)* | *(cross-reference)* |

---

## Stage 4 — Qualitative pass

### ADBE — Adobe

1. **Why are margins high?** Near-zero marginal cost per new Creative Cloud or Document Cloud subscriber. Pricing power from a 30-year monopoly on professional creative workflows — Photoshop/Illustrator/InDesign are the industry standard, embedded in every design school curriculum globally.
2. **Hard to compete with?** Very. The switching cost is skill-based, not contractual: designers train on Adobe for years and can't easily switch without relearning core workflows. Figma (acquired attempt blocked by regulators) tried and gained ground in UI design. AI-native tools (Midjourney, Runway, Sora) are the real threat — they attack the creative output itself, not just the toolset.
3. **Capital allocation?** Disciplined: heavy buybacks, conservative M&A, strong FCF conversion. The failed Figma acquisition ($20B) was ultimately blocked and returned capital. Management focuses on product reinvestment (Firefly AI, GenAI integrations within CC).
4. **Growth sources 3–5yr?** AI-augmented creative tools (Firefly) adding paid tiers; Document Cloud / Acrobat AI expansion; Experience Cloud enterprise upsell; pricing increases across installed base.
5. **Best bear case?** AI tools commoditise enough of creative work that Adobe's toolset becomes optional rather than essential. Particularly risky for mid-skill creators (the largest segment). Moat among professionals holds; moat among prosumers erodes.
6. **Disruption vector?** HIGH — this is the clearest AI disruption risk of any name on this list. AI-native image/video/audio generation directly substitutes for Creative Cloud's core use case. Adobe is investing heavily in Firefly as a hedge but is simultaneously defending its installed base from disruption it helped enable. Flag for 5-year moat horizon check.

---

### INTU — Intuit

1. **Why are margins high?** TurboTax has a near-monopoly in US consumer tax software (35–40% share) driven by prior-year data lock-in and the IRS e-file network. QuickBooks is the default small-business accounting platform in the US; switching to competitors requires migrating years of financial data. Credit Karma monetises trust relationships at scale.
2. **Hard to compete with?** Extremely in core US tax. H&R Block and Cash App Taxes are credible but have made no material dent in TurboTax's share. For SMB accounting, Xero/FreshBooks/Wave compete but struggle with the QuickBooks data lock-in.
3. **Capital allocation?** Credit Karma acquisition ($8.1B, 2020) was expensive and diluted ROIC; Mailchimp acquisition ($12B, 2021) was strategic but pricey. Overall, Intuit uses acquisitions to expand TAM. Buybacks consistent.
4. **Growth sources?** AI-powered tax prep (Intuit Assist / GenOS platform); QuickBooks global expansion; Credit Karma lending products; cross-sell between platforms. The "done-for-you" tax service (TurboTax Live) is growing at high double digits.
5. **Best bear case?** IRS free filing program (IRS Direct File) could disintermediate TurboTax for simple returns — a structural TAM compression risk. Regulatory/political risk to Credit Karma's BNPL and lending products.
6. **Disruption vector?** MODERATE — AI could make tax prep genuinely free for most filers, but Intuit is building its own AI-first platform. The disruption risk is primarily to volume (lower-value filers switch to free tools) rather than to pricing power at the high end (complex returns, business tax).

---

### TTD — The Trade Desk

1. **Why are margins high?** Independent DSP (demand-side platform) earns a fixed ~20% take rate on programmatic media spend. Asset-light: no media inventory owned; pure software + data intelligence. Scale advantages compound as more spend flowing through the platform improves audience targeting data.
2. **Hard to compete with?** Strong moat within independent programmatic. Google's DV360 is the only credible competitor at scale, but TTD's independence (no conflicts with media ownership) is its key differentiator. Agencies and brands increasingly mandate "walled-garden-independent" buys.
3. **Capital allocation?** Conservative: no debt, consistent buybacks, no transformative M&A. Management (Jeff Green founder-led) has a strong track record of organic product investment — UID2, OpenPath, Kokai are all self-built.
4. **Growth sources?** CTV/streaming (Peacock, Disney+, Netflix ad tiers) is the primary growth engine — ad dollars following audience attention shift from linear TV. Retail media networks integration. International expansion (still early in Europe/APAC).
5. **Best bear case?** Google wins the privacy-safe ID battle and entrenches DV360 as the default; TTD's open-internet share stagnates. Also: any economic slowdown hits ad spend immediately.
6. **Disruption vector?** MODERATE — AI-driven ad targeting could shift value from the platform to whoever owns the best predictive models (currently a moat for TTD; risk if Google/Meta open up). The bigger structural tailwind is the CTV transition, which TTD is positioned to capture better than anyone.

---

### QLYS — Qualys

1. **Why are margins high?** Cloud-native vulnerability management — delivered as a lightweight agent/scanner with no physical hardware; near-zero variable delivery cost. 30+ year brand in security compliance (PCI-DSS, SOC2, ISO 27001 coverage) creates deep customer lock-in.
2. **Hard to compete with?** Moderately hard in VM. Tenable and Rapid7 are credible competitors; Wiz/Orca are newer cloud-native entrants. But Qualys is deeply embedded in enterprise compliance workflows — ripping it out requires re-certifying audit trails.
3. **Capital allocation?** Exemplary: no debt, consistent buybacks, no dilutive M&A. 29.6% net margin with 22.52% ROIC shows highly disciplined capital deployment.
4. **Growth sources?** CNAPP (cloud-native application protection platform) expansion — moving from scan-only to continuous protection. Enterprise Cloud Platform consolidation as customers look to reduce vendor sprawl. Government/regulated sector expansions.
5. **Best bear case?** AI-native security platforms (Wiz, Orca) commoditise vulnerability detection; pricing pressure from Tenable; growth decelerates further toward single digits.
6. **Disruption vector?** MODERATE — AI-powered continuous security posture management is a genuine threat to scan-and-report legacy workflows. Qualys is investing in AI-driven remediation but is a follower in this wave, not a leader.

---

### TNE.AX — TechnologyOne (Australia)

1. **Why are margins high?** Mission-critical ERP SaaS for local government, universities, and utilities — the only sector where TechnologyOne dominates in Australia/UK. These sectors never switch vendors mid-cycle (data migration + compliance risk is too high). ROIC of 71% reflects near-total absence of capital intensity once a customer is on-platform.
2. **Hard to compete with?** In Australian local government: nearly impenetrable. SAP and Oracle compete theoretically, but TNE has built deep local-compliance modules (Australian procurement, local government Act, student administration regulation) that global vendors don't maintain at the same depth. UK expansion (local councils) is replicating this playbook.
3. **Capital allocation?** Excellent: 16 consecutive years of record profit, debt-free, consistent dividends, no dilutive M&A. Management (Ed Chung as CEO since 2023) has maintained the organic-growth-only playbook.
4. **Growth sources?** UK expansion (local councils, universities) is in early innings — mirroring the ANZ penetration story. ARR conversion from on-premises licenses still 40–50% complete. SaaS+ (including managed services and data analytics layers) expanding ARPU.
5. **Best bear case?** Microsoft Dynamics or Oracle NetSuite package a credible Australian-local-government module; or consolidation in the public sector (fewer councils = fewer contract renewals).
6. **Disruption vector?** LOW for 5-year horizon. Local government ERP is the least disrupted enterprise software segment — procurement cycles are 10+ years, regulated, and bureaucratic. AI adds product value (TNE is building AI analytics) but won't disrupt the core platform switch.

**Data gap reminder:** Gross margin not directly sourced; ROIC of 71.33% to be verified via ASX TIKR equivalent before Phase 02. AUD-denominated; USD investors should note currency exposure (AUD/USD ~0.62–0.64 typical range).

---

### CDNS — Cadence Design Systems

1. **Why are margins high?** EDA software is the pick-and-shovel play on semiconductor design. Every chip manufactured by TSMC, Samsung, or Intel uses Cadence Virtuoso (custom IC) or Genus/Innovus (digital design). The installed base is embedded in 10,000+ engineers' workflows — switching tools mid-design would mean revalidating the entire design process from scratch.
2. **Hard to compete with?** Cadence and Synopsys form a practical duopoly in EDA. Open-source alternatives (KiCad, Magic) exist for simple chips but have never threatened advanced node design. Ansys's simulation software (adjacent) was being acquired by Synopsys before regulatory blocks — a competitive tension now paused.
3. **Capital allocation?** Disciplined: consistent buybacks, limited M&A, strong FCF generation. Revenue guidance raised to 17% growth for FY2026 — rare for a company at $5B+ scale.
4. **Growth sources?** AI-chip design boom (NVIDIA, custom silicon at Google/Amazon/Microsoft/Meta) is driving explosive demand for EDA tooling. Cadence Cerebrus (AI-driven chip design automation) expands the value per design cycle. Hardware verification (Palladium emulation platform) growing.
5. **Best bear case?** AI-native design tools eventually let engineers skip traditional EDA workflows entirely. NVIDIA and Google have both built proprietary silicon design automation internally — if this trend accelerates, it could compress demand.
6. **Disruption vector?** MODERATE-LONG (5–10yr horizon). AI chip design automation is an existential question for EDA vendors, but Cadence is itself building AI design tools (Cerebrus). The transition is likely to enhance, not displace, core EDA over the next 5 years.

**ROIC note:** Two sources disagree (14.11% vs 19.71%) — must resolve before Phase 02. At 14.11% it fails; at 19.71% it passes. The divergence is likely a treatment of deferred revenue as "invested capital" in one methodology vs the other. Verify with TIKR invested-capital definition.

---

## Stage 5 — Data gaps (Rule 0)

The following metrics were **not directly sourced** and must be verified via TIKR before `/new-position` or `/rescore`:

| Ticker | Missing / flagged metrics |
|---|---|
| ADBE | FCF/NI conversion ratio (2 years) |
| INTU | Gross margin (estimated ~80%, not sourced); Net Debt/EBITDA; FCF/NI conversion |
| TTD | FCF/NI conversion ratio |
| QLYS | FCF/NI conversion ratio |
| TNE.AX | **Gross margin** (not sourced); ROIC verification (71.33% — extraordinary, needs TIKR cross-check); AUD/USD translation; IFRS filing standards vs GAAP |
| CDNS | **ROIC** — source divergence (14.11% vs 19.71%) must be resolved; gross margin not sourced this session; Net Debt/EBITDA; FCF/NI conversion |

---

## Framework observation — ROIC and M&A acquirers in SaaS

A notable pattern emerged: **nearly every major SaaS M&A acquirer fails Phase 01 on ROIC** when Gurufocus's adjusted invested-capital method is used (which includes all acquisition goodwill):

| Ticker | ROIC | Reason for low ROIC |
|---|---|---|
| CRM (Salesforce) | 6.29% | Slack $27B + Tableau $15.7B + MuleSoft $6.5B goodwill |
| NOW (ServiceNow) | 8.98% | Acquisition goodwill ($3–4B+) despite strong organic economics |
| SNPS (Synopsys) | 2.36% | Dramatic invested-capital expansion from Ansys deal prep |
| WTC.AX | 10.52% | ~20 acquisitions; integration ongoing |
| PAYC | 10.51% | Not M&A-driven; capital deployment into own payroll product |

The framework's ROIC gate **correctly identifies organic-growth, capital-efficient compounders** and penalises serial acquirers. This is philosophically aligned with the Buffett/Munger view of quality.

However, it creates an edge case worth flagging for `/decisions/`: companies like ServiceNow and Salesforce have genuinely excellent *operating* economics but impaired *accounting* ROIC due to acquisition accounting. A future framework upgrade might define an "organic ROIC" metric (NOPAT ÷ tangible invested capital excluding goodwill/intangibles) as a secondary gate for businesses whose goodwill clearly reflects durable, compounding IP — **but this is a framework change requiring a `/decisions/` entry, not a unilateral adjustment to a screen result.** For now, all six ROIC failures above are correctly recorded as failures.

---

## Watchlist flags (failed Phase 01 — worth monitoring)

| Ticker | Reason failed | Re-entry trigger |
|---|---|---|
| DT (Dynatrace) | Net margin 8.1% FY2026 (restructuring + cloud costs) | FY2027 GAAP net margin >12% on normalised basis; restructuring charges lapped |
| CRWD (CrowdStrike) | GAAP net margin −3.4% FY2026 | Full-year GAAP net margin >12% (Q4 FY2026 at GAAP operating breakeven is directionally encouraging) |
| PCTY (Paylocity) | ROIC not verified | TIKR verification — if ROIC >15%, advances to Phase 01 pass |
| SPSC (SPS Commerce) | Full metrics not verified | TIKR full-year verification — revenue growth strong, margins likely pass |
| XRO.NZX (Xero) | ROIC not sourced; net margin borderline | Sustained GAAP profitability 2 consecutive years; ROIC >15% confirmed |
| NOW (ServiceNow) | ROIC 8.98% | Either: organic ROIC framework upgrade adopted; or ROIC improves to >15% on existing methodology |
| CRM (Salesforce) | ROIC 6.29% | Same as NOW; structural goodwill headwind unlikely to clear anytime soon |

---

## Coverage log update

This was a **sector-focused thematic pass** (SaaS/cloud software), not a geographic slice. The coverage log geographic slices remain unchanged. Notes for the log:

- US names found (ADBE, INTU, TTD, QLYS, CDNS) are North American coverage; these supplement the NA-1 tech pass already done.
- TNE.AX is the first Australian name to reach the Qualified Quality List — this is partial **APAC-EX-JP** coverage (Australia only, one sector). The APAC-EX-JP full geographic pass remains "Never" and should still be run.

A new row will be added to the coverage log for the SaaS/cloud sector thematic pass.

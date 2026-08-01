# 2026-08-01 — SCREENING: Developed Asia-Pacific ex-Japan (APAC-EX-JP)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [APAC-EX-JP](../framework/screening-coverage-log.md) (Australia, Hong Kong, Singapore, South Korea, Taiwan), all sectors. Unattended scheduled run. Selected per the rotation rule: oldest "Last screened" date (2026-07-11) versus all other rows (2026-07-14 through 2026-07-28).

**Process note on this run's stored scheduled-task prompt:** the prompt that fired this session describes itself as the "Monthly Universe Screening Slice" (first Saturday of the month) and references an `EODHD_API_KEY`-based "Path A" full-automation path via `.claude/commands/screen.md`. Neither matches the current repo state — consistent with every prior rotation session since 2026-06-30 hitting this identical mismatch:
- The canonical [screen.md](../.claude/commands/screen.md) has no EODHD path at all — the only automated Step 0 option for an unattended run is the quality-factor-ETF-holdings fallback (MOAT/QUAL/QGRW/IQLT), and in practice (see Methodology below) that resolves to structural-triage-driven candidate sourcing for this slice, same as the two prior sessions on it.
- [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md) records that EODHD was removed from every automation doc on 2026-06-19 — its free-tier screener endpoint was unreliable, and the `EODHD_API_KEY` committed to `.claude/settings.json` on 2026-06-13 was flagged as a **compromised, live credential** to be rotated, not reused.
- [framework/automation-schedule.md](../framework/automation-schedule.md) documents this as "Routine 4 — Twice-Weekly Universe Screening Slice" (Tuesday and Saturday), not monthly.

An `EODHD_API_KEY` **is** present in this session's environment. Per the removal decision's explicit instruction and the unbroken precedent set by every prior screening session (NA-1, NA-2, EU, JP, EM, and both prior APAC-EX-JP rounds), it was **not used**. This session followed the current, canonical `screen.md`/`framework/` process instead, per CLAUDE.md's instruction to treat `framework/` as the source of truth over a stale stored prompt. This is at least the eighth consecutive rotation session to hit this same mismatch — worth updating whatever schedules the actual cron/trigger for this routine so it matches current docs, since re-flagging it every run is pure overhead. The fired prompt also did not request the Telegram/`.ics` calendar-invite steps that `automation-schedule.md`'s current Routine 4 prompt includes; consistent with prior sessions' handling of the same discrepancy, this run did not add that scope on its own initiative and stuck to the fired prompt's explicit 5 steps (screen, complete Steps 0-5, save session, open PR, open summary issue).

---

## 0. Methodology

**Unattended session — no user to ask for a TIKR/Koyfin export**, so per screen.md's documented exception this run skips straight to the ETF-holdings fallback. **IQLT's full holdings list is not scrapeable via plain curl** (confirmed again this session — the holdings table is client-side rendered and absent from the static HTML), consistent with both prior APAC-EX-JP sessions' finding that IQLT's visible/free holdings are dominated by Japan/Europe with negligible APAC-ex-Japan weight anyway. Per screen.md's unattended-session instruction, this run instead builds its candidate pool from **documented business-model/structural knowledge** — the same approach the 2026-07-11 and 2026-06-14 sessions on this slice used — explicitly reaching for **new names not covered in either prior APAC-EX-JP session**, across Australia, Hong Kong, Singapore, South Korea, and Taiwan, spanning sectors not yet deeply covered (insurance broking, international education services, medtech, advanced materials, ERP/SaaS, gaming, biosimilars, industrial automation/test equipment, semiconductor IP licensing/ASIC design, power electronics).

**Data sourcing:** `yfinance`/direct Yahoo access was tested and confirmed blocked before this task began (`SSLError('...curl: (35) Recv failure: Connection reset by peer...')` on a direct `yfinance` call, and HTTP 429 from `query1.finance.yahoo.com`) — consistent with every session since 2026-07-07. All quantitative figures below are sourced from **stockanalysis.com** (confirmed reachable, HTTP 200), cited inline.

**A genuine finding this session: the 2026-07-11 session's "`twse` exchange-code path returns 404" data gap was actually a wrong-exchange-code guess, not a broken data source.** stockanalysis.com's Taiwan Stock Exchange path is `tpe` (e.g. `stockanalysis.com/quote/tpe/2330/`), not `twse` — confirmed by cross-checking TSMC (`tpe/2330`, HTTP 200) and via stockanalysis.com's own search endpoint, which returned `tpe/...` and `tpex/...` (Taipei Exchange, the OTC-equivalent board) paths for every Taiwan candidate this session. This resolves the 07-11 session's flagged **Novatek Microelectronics** data gap (now quantified below). New Zealand's exchange code is similarly `nze`, not `nzx` as guessed in 07-11 — this resolves that session's **Fisher & Paykel Healthcare** 404 as well.

**Two names could not be located under any resolvable ticker this session and are flagged unavailable rather than guessed at** (CLAUDE.md Rule 0): **Altium Limited** (its former ASX ticker `ALU` now belongs to an unrelated company, "Alurion Resources"; a plausible alternate ticker `ALTM` resolves to the separately-delisted Arcadium Lithium; stockanalysis.com's search returns no match for "Altium") and **L'Occitane International** (`0973.HK` no longer resolves; consistent with the company's known 2024 go-private transaction). Neither was evaluated. See Data Gaps below.

**Live-price discipline (Rule 0):** every candidate's price-sensitive ratios (EV/EBIT, FCF yield, Net Debt/EBITDA) below are shown on a **current/TTM basis** (drawn from stockanalysis.com's live market cap/enterprise value) alongside the latest full-fiscal-year figure for comparability. Per-ticker quote timestamps were checked individually; all were dated 2026-07-31 (one trading day before this session) **except Douzone Bizon, whose quote was stale at "Jun 25, 2026"** — flagged explicitly in that row and in Data Gaps.

**Candidate pool this session (15 new names quantified, spanning 5 markets):**

| Ticker | Company | Country | Sector |
|---|---|---|---|
| ASX:AUB | AUB Group | Australia | Insurance broking network |
| ASX:SDF | Steadfast Group | Australia | Insurance broking network |
| ASX:IEL | IDP Education | Australia | International education services |
| ASX:NAN | Nanosonics | Australia | Medtech (infection-control devices) |
| NZE/ASX:FPH | Fisher & Paykel Healthcare | Australia/NZ | Medtech (respiratory care, OSA) |
| SGX:MZH | Nanofilm Technologies | Singapore | Advanced materials/nanotech coatings |
| KRX:012510 | Douzone Bizon | South Korea | ERP/accounting SaaS |
| KRX:036570 | NC Corporation (formerly "NCSOFT") | South Korea | Gaming |
| KRX:068270 | Celltrion | South Korea | Biopharma (biosimilars) |
| TPE:2360 | Chroma ATE | Taiwan | Test & measurement equipment |
| TPE:1590 | Airtac International | Taiwan | Industrial automation (pneumatics) |
| TPEX:3529 | eMemory Technology | Taiwan | Semiconductor IP licensing |
| TPE:3443 | Global Unichip | Taiwan | ASIC/IC design services (TSMC-affiliated) |
| TPE:6409 | Voltronic Power Technology | Taiwan | Power electronics (UPS) |
| TPE:3034 | Novatek Microelectronics | Taiwan | Fabless IC design |

---

## Step 1 — Structural triage (business-model eliminations, no quantitative pull)

Building on both prior sessions' Step 1 eliminations — **Singapore/HK banks, AIA, Macquarie, Goodman Group REIT, Wesfarmers/JB Hi-Fi, Sea Limited, Grab, Wilmar, ComfortDelGro, Venture Corp, various REITs, Samsung SDI/LG Energy Solution, Melco/Sands China/Galaxy Entertainment, Hyundai/Kia/Hyundai Mobis, Silergy** — all still structurally excluded, not re-litigated — this pass adds:

| Eliminated | Country | Why |
|---|---|---|
| ST Engineering | Singapore | Defense/aerospace/government-linked conglomerate — capital-intensive, thin margins typical of contract manufacturing + government-program mix |
| Riverstone Holdings | Singapore | Nitrile glove manufacturer — commodity, COVID-cycle-driven margin history, thin-margin manufacturing |
| Coupang | South Korea (NYSE-listed) | E-commerce/logistics — thin-to-negative historical margins, same reasoning as the carried-forward Sea Limited/Grab exclusion |
| Yangzijiang Shipbuilding | Singapore | Commodity cyclical shipbuilding |
| Keppel Corporation | Singapore | Diversified infrastructure/property conglomerate — capital-intensive, doesn't fit an asset-light quality model |
| Genting Singapore | Singapore | Regulated casino gaming — same reasoning as the carried-forward Melco/Sands China/Galaxy Entertainment exclusion |
| LG Household & Health Care, Amorepacific | South Korea | Korean cosmetics majors — both show well-documented multi-year margin compression from China market-share losses; deprioritized this round in favor of Celltrion/Douzone Bizon to diversify sector coverage rather than add a second name with the same known structural headwind |
| Kakao Corp, Kakao Games | South Korea | Complex multi-segment messaging/gaming/fintech conglomerate structure plus an ongoing governance/legal overhang (2024 founder prosecution) — poor fit for a clean quantitative read this round |

**Unavailable/delisted (not a business-model exclusion — flagged separately, see Methodology and Data Gaps):** Altium Limited, L'Occitane International (0973.HK).

---

## Step 2 — Full Phase 01 quantitative gate (real, sourced data — stockanalysis.com, pulled 2026-08-01)

Filters: Gross margin >40% · Net margin >12% · ROIC>15% (ROE proxy) · Revenue growth >8% (3yr CAGR) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x

Gross margin, net margin, ROIC/ROE, and revenue CAGR are shown on the latest full-fiscal-year basis; Net Debt/EBITDA, FCF yield, and EV/EBIT are shown on a **current/TTM (live-price) basis**, per Rule 0, with the latest-FY figure alongside for comparability.

| Ticker | Gross M | Net M | ROIC / ROE (latest FY) | Rev 3yr CAGR | FCF 3yr positive? | Net Debt/EBITDA (current / FY) | FCF yield (current / FY) | EV/EBIT (current / FY) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **AUB Group (ASX:AUB)** [[1]](#src1) | 49.44% ✅ | 15.35% ✅ | 9.81% ❌ / 11.28% ❌ | 46.55% ✅ (M&A-driven — see note) | ✅ | 2.44x ✅ / 1.87x ✅ | 7.33% ✅ / 9.23% ✅ | 15.31x ✅ / 17.20x ✅ | **NEAR-MISS — only ROIC/ROE fails**, 7/8 clear |
| **Steadfast Group (ASX:SDF)** [[2]](#src2) | 52.93% ✅ | 16.22% ✅ | 14.64% ❌ / 14.96% ❌ | 20.96% ✅ | ✅ | 1.84x ✅ / 1.51x ✅ | 9.25% ✅ / 7.43% ✅ | 9.93x ✅ / 11.37x ✅ | **NEAR-MISS — only ROIC/ROE narrowly fails** (14.64%/14.96% vs. 15% bar), 7/8 clear — narrowest miss this session |
| **IDP Education (ASX:IEL)** [[3]](#src3) | 24.83% ❌ | 5.04% ❌ (TTM: 0.12%) | 8.03% ❌ / 8.61% ❌ | 3.60% ❌ (revenue declining FY25 vs FY24) | ✅ | 5.09x ❌ / 2.43x ✅ | 17.37% ✅ (price-driven) / 12.08% ✅ | 21.46x ❌ / 14.06x ✅ | **FAIL — 6/8**, structural downturn (international-student visa-policy headwinds); high FCF yield is a value-trap signal, not cheapness |
| **Nanosonics (ASX:NAN)** [[4]](#src4) | 78.22% ✅ | 10.41% ❌ (narrow) | 28.27% ✅ / 10.55% ❌ | 18.19% ✅ | ✅ | 6.21x ✅ (net cash) / 6.75x ✅ (net cash) | 2.64% ❌ / 2.87% ❌ | 39.16x ❌ / 60.91x ❌ | **FAIL — 3/8** (net margin narrow miss, FCF yield, EV/EBIT) — quality/growth strong, priced rich |
| **Fisher & Paykel Healthcare (NZE:FPH)** [[5]](#src5) | 63.69% ✅ | 20.29% ✅ | 26.38% ✅ / 23.39% ✅ | 13.44% ✅ | ✅ | 0.41x ✅ (net cash) / 0.41x ✅ (net cash) | 2.05% ❌ / 2.23% ❌ | 37.06x ❌ / 34.27x ❌ | **FAIL — only 2/8** (both valuation) — pristine quality, priced for it |
| **Nanofilm Technologies (SGX:MZH)** [[6]](#src6) | 36.16% ❌ (close) | 4.83% ❌ | 3.42% ❌ / 2.65% ❌ | 1.00% ❌ | ❌ (FY24/23 negative) | 0.46x ✅ / 0.46x ✅ | 0.25% ❌ / 0.46% ❌ | 43.00x ❌ / 24.74x ❌ | **FAIL — 7/8**, sharp margin compression across the board since 2021 |
| **Douzone Bizon (KRX:012510)** [[7]](#src7) | 49.89% ✅ | 19.49% ✅ | 13.41% ❌ (narrow) / 15.55% ✅ | 13.62% ✅ | ✅ | 0.57x ✅ / 0.71x ✅ | 3.25% ❌ (narrow) / 4.60% ✅ | 22.06x ❌ (narrow) / 20.16x ❌ (narrow) | **NEAR-MISS — 3 narrow misses** (ROIC, FCF yield, EV/EBIT) — **live-price data gap, see below** |
| **NC Corporation / NCSOFT (KRX:036570)** [[8]](#src8) | 99.19% ✅ (genuine digital-distribution model, not a data gap) | 23.00% ✅ | 0.33% ❌ / 10.80% ❌ | −16.32% ❌ (revenue declining) | ✅ (shrinking) | 7.92x ✅ (net cash) / 15.81x ✅ (net cash) | 5.35% ✅ (price-driven) / 1.50% ❌ | 29.24x ❌ / 273.17x ❌ | **FAIL — 4/8**, confirms the franchise-fatigue concern flagged qualitatively in the 07-11 KRAFTON write-up; company officially renamed "NC Corporation" on this data source |
| **Celltrion (KRX:068270)** [[9]](#src9) | 59.27% ✅ | 24.73% ✅ (FY24 dipped to 11.88% — flagged) | 5.41% ❌ / 5.91% ❌ | 22.15% ✅ | ✅ | 1.50x ✅ / 1.72x ✅ | 1.53% ❌ / 1.36% ❌ | 34.18x ❌ / 35.80x ❌ | **FAIL — 4/8**, weak returns on capital despite strong margins/growth; rich valuation |
| **Chroma ATE (TPE:2360)** [[10]](#src10) | 61.55% ✅ | 41.30% ✅ (anomalous jump — flagged) | 30.07% ✅ (TTM 52.60%, flagged) / 41.12% ✅ | 8.66% ✅ | ✅ | 0.33x ✅ (net cash) / 0.45x ✅ (net cash) | 0.22% ❌ / 0.91% ❌ | 56.72x ❌ / 35.45x ❌ | **FAIL — only 2/8** (both valuation) — "great business, too expensive" again; FY25 margin/return jump flagged as a probable one-off |
| **Airtac International (TPE:1590)** [[11]](#src11) | 45.97% ✅ | 24.47% ✅ | 17.29% ✅ / 16.72% ✅ | 9.60% ✅ | ✅ | 0.49x ✅ (net cash) / 0.29x ✅ (net cash) | 2.29% ❌ / 2.61% ❌ | 22.76x ❌ (narrow, passes on FY-only basis at 17.52x) / 17.52x ✅ | **FAIL — only 2/8** (both valuation) — excellent quality (ROIC/ROE both clear 15%, net cash); live price pushed EV/EBIT just over cap |
| **eMemory Technology (TPEX:3529)** [[12]](#src12) | 100.00% ✅ (genuine — pure IP-licensing model) | 49.67% ✅ | 595.47% ✅ (degenerate, flagged) / 51.47% ✅ | 6.16% ❌ (narrow) | ✅ | 1.67x ✅ (net cash) / 1.52x ✅ (net cash) | 1.22% ❌ / 1.55% ❌ | 71.76x ❌ / 56.16x ❌ | **FAIL — 3/8**, extreme valuation despite an ARM-like licensing moat |
| **Global Unichip (TPE:3443)** [[13]](#src13) | 24.76% ❌ | 11.04% ❌ (narrow) | 292.41% ✅ (degenerate, flagged) / 31.14% ✅ | 12.40% ✅ | ❌ (TTM negative) | 1.67x ✅ (net cash) / 1.87x ✅ (net cash) | 0.56% ❌ / −0.70% ❌ | 86.00x ❌ / 63.27x ❌ | **FAIL — 5/8** |
| **Voltronic Power (TPE:6409)** [[14]](#src14) | 29.04% ❌ | 17.16% ✅ | 86.07% ✅ (flagged high) / 36.14% ✅ | −3.34% ❌ | ✅ | 1.50x ✅ (net cash) / 1.24x ✅ (net cash) | 4.35% ✅ / 5.35% ✅ | 19.28x ✅ / 18.61x ✅ | **FAIL — only 2/8** (gross margin, revenue CAGR) — unusual profile: passes valuation + returns, fails on margin structure/growth |
| **Novatek Microelectronics (TPE:3034)** [[15]](#src15) | 37.66% ❌ (narrow) | 16.24% ✅ | 67.12% ✅ (flagged high) / 24.10% ✅ | −2.90% ❌ | ✅ | 2.72x ✅ (net cash) / 2.15x ✅ (net cash) | 4.27% ✅ / 5.46% ✅ | 16.14x ✅ / 10.34x ✅ | **FAIL — only 2/8** (narrow gross-margin miss + cyclical revenue decline) — resolves 07-11's data gap |

---

## ✅ Qualified Quality List — 0 new clean passes this session

No candidate cleared all 8 Phase 01 filters this round. The prior session's list is **unchanged and carried forward**: **iFAST Corporation (AIY.SG)** remains the one clean Phase 01 pass on this slice, with **KRAFTON, ResMed, and CSL** still flagged pending `/new-position` confirmation (see [sessions/2026-07-11-screening-apac-ex-japan.md](2026-07-11-screening-apac-ex-japan.md)) — none of those four were re-touched this session.

### Near-misses flagged for the watchlist (headline)

- **Steadfast Group (ASX:SDF)** — the narrowest miss this session: 7/8 filters clear cleanly, only ROIC (14.64%) and ROE (14.96%) fall just short of the 15% bar.
- **AUB Group (ASX:AUB)** — same insurance-broking-network niche as Steadfast, also 7/8 clear on only a ROIC/ROE miss, but a wider one (9.81%/11.28%) — worth comparing the two on returns-on-capital discipline before any future `/new-position` pass. Revenue 3yr CAGR (46.55%) is heavily M&A-driven (roll-up acquisitions), not organic — flagged as a caveat on that filter despite it passing.
- **Douzone Bizon (KRX:012510)** — 3 narrow misses (ROIC 13.41% vs. 15%; FCF yield 3.25% vs. 4%; EV/EBIT 22.06x vs. 20x cap) with everything else clearing cleanly — but see the live-price data gap below before treating the current-basis figures as reliable.

### Additional watchlist flags — quality clears comfortably, blocked mainly by valuation (or a cyclical dip)

- **Fisher & Paykel Healthcare (FPH)** — only 2/8 fail, both valuation (FCF yield 2.05%, EV/EBIT 37.06x); ROIC 26.38%, ROE 23.39%, net cash, 13.44% 3yr revenue CAGR.
- **Airtac International (TPE:1590)** — only 2/8 fail, both valuation; ROIC 17.29%, ROE 16.72%, net cash — EV/EBIT clears on a FY-only basis (17.52x) and only fails on the live-price current basis (22.76x).
- **Chroma ATE (TPE:2360)** and **eMemory Technology (TPEX:3529)** — both only 2-3/8 fail, all valuation-related; both show extremely high (likely asset-light-distorted) ROIC readings flagged rather than trusted at face value.
- **Novatek Microelectronics (TPE:3034)** and **Voltronic Power (TPE:6409)** — both only 2/8 fail (a narrow-to-moderate gross-margin/growth miss tied to a cyclical revenue dip), while clearing all three valuation/leverage filters comfortably — an unusual "cheap and returns-strong, but structurally low-margin or currently shrinking" profile worth a re-check once the cycle turns.
- **Nanosonics (ASX:NAN)** — 3/8 fail (narrow net-margin miss, FCF yield, EV/EBIT); ROIC 28.27% and 18.19% 3yr revenue CAGR are both strong.

---

## Step 3 — Qualitative pass

Per screen.md's batch-processing policy (default batch size 2, from [new-position.md](../.claude/commands/new-position.md)), the four names below were walked through the 5 qualitative questions in two conceptual batches of 2 (Steadfast Group + Douzone Bizon, then Airtac International + Fisher & Paykel Healthcare).

### Batch 1

#### Steadfast Group (ASX:SDF)

1. **Why are margins high?** Steadfast is Australia's largest general-insurance broking network — it holds equity stakes in a network of 100+ independent insurance brokerages plus a portfolio of underwriting agencies, earning commission/fee revenue on premiums placed without retaining underwriting risk itself. Margins reflect an asset-light, fee-based model plus scale advantages (network-wide preferential insurer terms and volume rebates that an individual broker couldn't negotiate alone).
2. **What would it take to compete?** A rival would need to replicate a comparable network of broker equity relationships across Australia/NZ built up over many years, plus insurer relationships deep enough to secure preferential terms — slow and capital-intensive to build from scratch; Steadfast's branded network technology platform (comparative rating/placement tools) also creates switching costs for member brokers.
3. **Capital allocation (5–10yr):** Continuous bolt-on M&A — acquiring equity stakes in independent brokers and underwriting agencies — is the primary growth lever and the main driver of the reported 20.96% revenue CAGR (not purely organic). A reasonable adjacent-market roll-up strategy, though it carries integration and overpaying risk if pursued too aggressively.
4. **Where's growth coming from (3–5yr)?** Continued bolt-on acquisitions, cross-selling underwriting-agency products through the broker network, and organic commission growth if the current "hard" P&C insurance-pricing cycle (rising premiums) persists.
5. **Best bear case:** Heavy reliance on continued *accretive* M&A to sustain the growth rate — if targets dry up or get bid up, organic growth alone looks far more modest. A "soft" pricing cycle (falling premiums) would directly compress commission revenue. ROIC (14.64%, just under the 15% bar) suggests the roll-up isn't yet clearly value-accretive at the margin — worth monitoring whether it trends up or down as the strategy continues.
6. **Disruption vector:** Low-moderate — digital/direct insurer distribution is a real long-run threat to broker economics, but Steadfast's core is complex commercial-lines insurance (not personal lines), where the advisory/claims-management value a broker provides is more insulated from disintermediation.

**Conclusion:** A genuine near-miss with an unusually narrow gap (ROIC/ROE both within ~0.4pp of the 15% bar) — worth re-checking on the next rotation or if either return metric ticks up. AUB Group is the closest domestic peer and also a near-miss this session, but with a notably wider ROIC/ROE gap (9.81%/11.28%) despite similar gross/net margins — a difference worth investigating (M&A pricing discipline, majority-vs-minority stake mix) before choosing between the two.

#### Douzone Bizon (KRX:012510)

1. **Why are margins high?** Douzone Bizon is South Korea's dominant SME accounting/ERP software vendor. High recurring-revenue mix and low marginal cost of serving an existing customer once the core platform is built; Korea's historical e-tax-invoicing integration requirements pushed SME adoption of compliant accounting software, entrenching Douzone as the default choice for many Korean small/mid businesses.
2. **What would it take to compete?** A challenger needs deep, continuously-updated Korean tax/regulatory-compliance engineering plus an installed base large enough to amortize that cost — a real, if not insurmountable, moat. Global ERP vendors (SAP, Oracle) compete at the large-enterprise end, not Douzone's SME core.
3. **Capital allocation (5–10yr):** Ongoing investment migrating the historical on-premise installed base to a cloud-subscription model, plus early AI-assisted bookkeeping/tax features — a necessary transition still in progress. No unusual M&A pattern in the sourced financials.
4. **Where's growth coming from (3–5yr)?** Continued cloud migration (higher ARPU per migrated customer) and AI-assisted upsell features layered onto the existing base.
5. **Best bear case:** Korea's SME software market is a relatively mature, saturated domestic market — 13.62% 3yr revenue CAGR is respectable but not explosive, and international expansion beyond Korea is largely unproven. A slower-than-expected cloud-migration pace leaves growth dependent mainly on price increases within an already-penetrated base.
6. **Disruption vector:** Low-moderate — accounting software is historically sticky (data-migration risk deters switching), but a well-funded domestic cloud-native challenger or global horizontal SaaS entrant could erode share at the margin among younger, digital-first SMEs with no legacy attachment to Douzone's on-premise heritage.

**Conclusion:** A real 3-filter near-miss, but **the live-price data gap matters here**: Douzone's quote on stockanalysis.com was stale at "Jun 25, 2026" (over a month old as of this 2026-08-01 session) — its current-basis EV/EBIT (22.06x) and FCF yield (3.25%) are anchored to that stale price, not a live one. The FY-basis figures (EV/EBIT 20.16x, FCF yield 4.60% — the latter actually *passing* the 4% bar) are drawn from FY2025 annual results and are more recent in spirit but still not a live price. **A fresh live-price check is needed before treating this as a firm near-miss.**

### Batch 2

#### Airtac International (TPE:1590)

1. **Why are margins high?** Airtac designs and manufactures pneumatic automation components (cylinders, valves, fittings) primarily for mainland China's factory-automation market. Margins reflect a broad product catalog (extensive SKU count enabling one-stop sourcing for factory integrators) plus a dense China distributor network giving faster delivery than smaller domestic rivals or imports from Japan's SMC or Germany's Festo.
2. **What would it take to compete?** A rival needs a comparably broad catalog plus China-wide distribution density — SMC (the global category leader) and Festo compete at the premium/precision end; the harder-to-replicate piece is Airtac's combination of cost-competitive manufacturing with China-specific distribution reach that neither global incumbent has matched at Airtac's price point.
3. **Capital allocation (5–10yr):** Reinvestment in manufacturing capacity and expansion into electric-automation components alongside core pneumatics — organic, no major disclosed M&A in the sourced financials.
4. **Where's growth coming from (3–5yr)?** China's ongoing factory-automation capex cycle (labor-cost-driven automation adoption) plus a new electric-actuator product line as a second growth leg.
5. **Best bear case:** Heavy geographic concentration in mainland China's industrial capex cycle — a China manufacturing slowdown (a live macro concern) hits Airtac's core market directly, alongside the China-market regulatory/geopolitical exposure common to Taiwan-listed, China-revenue-dependent industrials.
6. **Disruption vector:** Low — pneumatic automation is a mature, well-understood technology category; the more relevant long-run risk is margin compression from share loss to SMC/Festo at the premium end or lower-cost domestic Chinese makers at the budget end, not technological obsolescence.

**Conclusion:** Genuinely strong quality profile (ROIC 17.29%, ROE 16.72%, net cash, 9.60% 3yr revenue CAGR) disqualified purely by valuation — EV/EBIT clears on a FY-only basis (17.52x) and only fails on the live current-price basis (22.76x), meaning the price has simply run ahead of the cap this session. Worth a pullback watch.

#### Fisher & Paykel Healthcare (NZE:FPH)

1. **Why are margins high?** FPH designs and manufactures humidified respiratory-care devices (hospital nasal high-flow therapy — Optiflow/Airvo) and OSA (sleep apnea) masks/devices. Consumables (masks, tubing, breathing circuits) are recurring, razor-and-blade-style repeat purchases once a hospital or patient standardizes on FPH's platform, backed by a deep patent portfolio around its humidification technology.
2. **What would it take to compete?** A rival needs both regulatory clearance and years of clinical-evidence-backed clinician trust, plus a device-plus-consumables installed base. ResMed is the most direct global competitor in the OSA segment; hospital respiratory care is a smaller, more specialized field with few credible competitors.
3. **Capital allocation (5–10yr):** Continued R&D in next-generation humidification/flow-therapy devices and a large, multi-year manufacturing-capacity build-out in Auckland, NZ — organic reinvestment, no major disclosed M&A.
4. **Where's growth coming from (3–5yr)?** Structurally growing hospital nasal high-flow therapy adoption (increased clinical evidence post-COVID) and continued OSA-device/mask share competition against ResMed.
5. **Best bear case:** A concentrated two-player OSA market (FPH vs. ResMed) means FPH's growth is partly a share-shift game against a larger, well-capitalized rival. Hospital capital-equipment purchasing cycles can be lumpy, and NZD-reporting against largely USD global revenue adds currency-driven earnings volatility unrelated to the underlying business.
6. **Disruption vector:** Low-moderate — respiratory-device technology evolves incrementally (better sensors, more comfortable masks) rather than facing an entirely new delivery mechanism; the more relevant risk is ResMed's own innovation cadence.

**Conclusion:** Near-pristine quality (ROIC 26.38%, ROE 23.39%, net cash, 13.44% 3yr revenue CAGR, 3 consecutive years FCF-positive), disqualified purely on valuation richness (FCF yield 2.05%, EV/EBIT 37.06x). This is the same "excellent business, priced for it" pattern seen repeatedly this session (Chroma ATE, eMemory, Nanosonics) and in the 07-11 session's Pro Medicus/WiseTech/TechnologyOne trio — a recurring finding worth flagging at the session level: several of this region's highest-quality medtech/tech names are currently priced well outside this framework's Phase 01 valuation caps.

---

## Data gaps flagged (per CLAUDE.md Rule 0 — none estimated)

- **Douzone Bizon (KRX:012510) — stale live price.** stockanalysis.com's quote for this ticker was dated "At close: Jun 25, 2026" — over a month stale as of this 2026-08-01 session — while every other Korean/Taiwanese/Australian/NZ/Singaporean ticker this session quoted within one trading day (2026-07-31). Its current-basis EV/EBIT (22.06x) and FCF yield (3.25%) rest on that stale price; flagged explicitly rather than treated as a live Rule-0-compliant figure.
- **Altium Limited** — could not be located under any resolvable ticker on stockanalysis.com. Its former ASX ticker (`ALU`) now belongs to an unrelated company ("Alurion Resources"); a plausible alternate ticker (`ALTM`) resolves to the separately-delisted Arcadium Lithium (delisted 6 March 2025, acquired by Rio Tinto, per that ticker's own page metadata). Not evaluated.
- **L'Occitane International (0973.HK)** — ticker no longer resolves on stockanalysis.com (confirmed via the site's own search); consistent with the company's known 2024 go-private transaction. Not evaluated.
- **NC Corporation (KRX:036570) — FY2022 Net Debt/EBITDA outlier.** The multi-year series contains one extreme artifact value (6366.024x) for an intermediate fiscal year, almost certainly a near-zero-EBITDA-denominator distortion — not used; only the current/TTM and latest-FY values feed the verdict.
- **Chroma ATE (TPE:2360) — FY2025 margin/return jump.** Net margin (41.30%), ROIC (30.07%, TTM 52.60%), and ROE (41.12%) all jumped sharply versus FY2021–24 (roughly 21–25% / 13–22% / 18–26%) — flagged as a probable one-off item (cause unconfirmed, not investigated further this session) rather than a new sustainable profitability level.
- **Celltrion (KRX:068270) — FY2024 net-margin dip.** 11.88% versus 20–31% in adjacent years — plausibly related to accounting effects of the 2023 Celltrion/Celltrion Healthcare merger; not investigated further.
- **Several extreme ROIC readings** (Chroma ATE TTM 52.60%, eMemory 595.47%, Global Unichip 292.41%, Novatek 67.12%, Voltronic 86.07%) are flagged as small-invested-capital-denominator artifacts typical of asset-light manufacturers/IP licensors, consistent with the TechnologyOne/Pro Medicus precedent from the 07-11 session. ROE is shown alongside as the more interpretable cross-check in each case; it doesn't change any verdict here since ROE tells a consistent (high) story throughout.
- **AUB Group / Steadfast Group "gross margin"** — flagged as a less-standard concept for a fee/commission-based insurance-broking business (same caveat class as Aon/AJG/MMC in the NA-2 precedent). The sourced figures (49–53%) are non-degenerate (not equal to net revenue, unlike the NAVER/KRAFTON gross-margin data gap from 07-11), so used without a hard data-gap flag, but the underlying cost-of-revenue line wasn't independently verified against a primary filing.
- **Hong Kong candidate search.** Beyond L'Occitane's unavailability, this session — like both prior APAC-EX-JP rounds — continued to struggle to find non-financial, non-property Hong Kong-domiciled quality-factor candidates beyond the names already triaged/quantified (HKEX, Techtronic, ASMPT, Prada). Flagged as a standing observation for future rotations, not a specific per-ticker gap.

---

## Sources

<a id="src1"></a>[1] AUB Group: https://stockanalysis.com/quote/asx/AUB/financials/ , https://stockanalysis.com/quote/asx/AUB/financials/ratios/
<a id="src2"></a>[2] Steadfast Group: https://stockanalysis.com/quote/asx/SDF/financials/ , https://stockanalysis.com/quote/asx/SDF/financials/ratios/
<a id="src3"></a>[3] IDP Education: https://stockanalysis.com/quote/asx/IEL/financials/ , https://stockanalysis.com/quote/asx/IEL/financials/ratios/
<a id="src4"></a>[4] Nanosonics: https://stockanalysis.com/quote/asx/NAN/financials/ , https://stockanalysis.com/quote/asx/NAN/financials/ratios/
<a id="src5"></a>[5] Fisher & Paykel Healthcare: https://stockanalysis.com/quote/nze/FPH/financials/ , https://stockanalysis.com/quote/nze/FPH/financials/ratios/
<a id="src6"></a>[6] Nanofilm Technologies: https://stockanalysis.com/quote/sgx/MZH/financials/ , https://stockanalysis.com/quote/sgx/MZH/financials/ratios/
<a id="src7"></a>[7] Douzone Bizon: https://stockanalysis.com/quote/krx/012510/financials/ , https://stockanalysis.com/quote/krx/012510/financials/ratios/ , https://stockanalysis.com/quote/krx/012510/ (quote-staleness check)
<a id="src8"></a>[8] NC Corporation (NCSOFT): https://stockanalysis.com/quote/krx/036570/financials/ , https://stockanalysis.com/quote/krx/036570/financials/ratios/
<a id="src9"></a>[9] Celltrion: https://stockanalysis.com/quote/krx/068270/financials/ , https://stockanalysis.com/quote/krx/068270/financials/ratios/
<a id="src10"></a>[10] Chroma ATE: https://stockanalysis.com/quote/tpe/2360/financials/ , https://stockanalysis.com/quote/tpe/2360/financials/ratios/
<a id="src11"></a>[11] Airtac International: https://stockanalysis.com/quote/tpe/1590/financials/ , https://stockanalysis.com/quote/tpe/1590/financials/ratios/
<a id="src12"></a>[12] eMemory Technology: https://stockanalysis.com/quote/tpex/3529/financials/ , https://stockanalysis.com/quote/tpex/3529/financials/ratios/
<a id="src13"></a>[13] Global Unichip: https://stockanalysis.com/quote/tpe/3443/financials/ , https://stockanalysis.com/quote/tpe/3443/financials/ratios/
<a id="src14"></a>[14] Voltronic Power: https://stockanalysis.com/quote/tpe/6409/financials/ , https://stockanalysis.com/quote/tpe/6409/financials/ratios/
<a id="src15"></a>[15] Novatek Microelectronics: https://stockanalysis.com/quote/tpe/3034/financials/ , https://stockanalysis.com/quote/tpe/3034/financials/ratios/

Data-gap/availability confirmation fetches: https://stockanalysis.com/api/search?q=Altium (no relevant match); https://stockanalysis.com/stocks/altm/financials/ratios/ (resolves to the unrelated, delisted Arcadium Lithium); https://stockanalysis.com/api/search?q=0973 (no L'Occitane match); https://stockanalysis.com/quote/hkg/0973/financials/ratios/ (404); Taiwan exchange-code fix confirmed via https://stockanalysis.com/quote/tpe/2330/financials/ratios/ (TSMC, HTTP 200) and https://stockanalysis.com/api/search?q=Novatek%20Microelectronics.

---

## Next steps

- **No `/new-position` recommendation this round** — no candidate cleared all 8 Phase 01 filters.
- **Watchlist adds:** Steadfast Group (ASX:SDF) and AUB Group (ASX:AUB) — Australian insurance-broking-network niche, both 7/8-clear near-misses blocked only by ROIC/ROE; Douzone Bizon (KRX:012510) — 3 narrow misses, but re-check its live price first (data gap above); Fisher & Paykel Healthcare (FPH), Airtac International (TPE:1590), Chroma ATE (TPE:2360), eMemory Technology (TPEX:3529), Novatek Microelectronics (TPE:3034), Voltronic Power (TPE:6409), Nanosonics (ASX:NAN) — quality clears comfortably on most filters, blocked mainly by rich valuation (or, for Novatek/Voltronic, a cyclical revenue dip) — worth a re-check on a pullback or the next rotation.
- **Re-fetch Douzone Bizon's live price** specifically before relying on its current-basis EV/EBIT and FCF yield for any watchlist decision.
- **Altium Limited and L'Occitane International** — both appear unavailable/delisted at this data source; revisit only if independent confirmation of current listing status surfaces.
- Coverage log updated below — after this update, **EM (Emerging Markets, 2026-07-14)** becomes the oldest-screened row and is next in rotation.
- **Process flag for the automation owner** (see box at top of this session): the scheduled Routine 4 prompt still describes a monthly/EODHD process that doesn't match `framework/automation-schedule.md`'s current twice-weekly/no-EODHD documentation, and omits the Telegram/`.ics` steps that doc's current Routine 4 prompt includes — worth reconciling the actual cron/routine configuration against the current docs so this doesn't need re-flagging every run.

---

## Glossary

- **ADR (American Depositary Receipt)** — a US-exchange-listed security representing shares of a non-US company.
- **Biosimilar** — a biologic drug approved as highly similar (not identical, unlike a small-molecule generic) to an already-approved reference biologic, sold at a discount once the reference product's patent/exclusivity expires — Celltrion's core business line.
- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate between a start and end value over several years.
- **EBIT** — Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
- **ERP (Enterprise Resource Planning)** — integrated software that manages a company's core back-office processes (accounting, inventory, procurement, payroll) in one system — Douzone Bizon's core product category, dominant among South Korean SMEs.
- **EV/EBIT** — Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to operating profit, independent of capital structure.
- **Fabless** — a chip company that designs semiconductors but outsources manufacturing to a foundry — Novatek Microelectronics and Global Unichip are both fabless designers.
- **FCF (Free Cash Flow) / FCF Yield** — cash a business generates after running and maintaining itself; FCF Yield is FCF ÷ Market Cap (or Enterprise Value), a measure of cheapness.
- **Gross Margin** — Gross Profit (Revenue − Cost of Revenue) ÷ Revenue.
- **Insurance broking network** — a business model (Steadfast Group, AUB Group) built around holding equity stakes in a network of independent insurance brokerages plus underwriting agencies, earning commission/fee revenue on premiums placed without retaining the underlying insurance (underwriting) risk itself — distinct from an insurer, which does retain that risk on its own balance sheet.
- **IP (Intellectual Property) licensing** — a business model where a company earns royalty/licensing revenue from third parties using its patented technology, rather than manufacturing or selling a product itself — eMemory Technology licenses its non-volatile-memory semiconductor IP to chipmakers, similar in structure to ARM Holdings' processor-design licensing model.
- **Net Debt/EBITDA** — net debt (total debt minus cash) divided by EBITDA — a leverage ratio; "net cash" means the figure is negative (more cash than debt).
- **Net Margin** — Net Income ÷ Revenue.
- **OSA (Obstructive Sleep Apnea)** — a sleep disorder involving repeated airway blockage during sleep, treated with devices like CPAP machines and masks — the core market for Fisher & Paykel Healthcare's and ResMed's sleep-therapy device lines.
- **Pneumatics / pneumatic automation** — industrial components (cylinders, valves, fittings) that use compressed air to power motion in automated manufacturing equipment — Airtac International's core product category.
- **Qualified Quality List** — the output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring.
- **Razor-and-blade model** — a business model where a durable device is sold once (often at low margin) while recurring, higher-margin consumables are repurchased over the device's lifetime — the dynamic behind Fisher & Paykel Healthcare's mask/tubing/circuit consumables revenue.
- **ROE** — Return on Equity — Net Income ÷ shareholder equity.
- **ROIC** — Return on Invested Capital — a core quality signal in this framework; can be distorted (pushed to extreme values) for asset-light businesses with a very small invested-capital denominator.
- **Roll-up (M&A strategy)** — a growth strategy built on repeated, often small, acquisitions of similar businesses (e.g. independent insurance brokerages) consolidated under one parent to capture scale/network benefits — Steadfast Group's and AUB Group's primary growth engine, and the reason their reported revenue CAGR is flagged as largely inorganic.
- **SaaS (Software-as-a-Service)** — a software delivery model where customers pay a recurring subscription to access hosted software.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results, used here to pair a live/current price with recent trailing fundamentals.

# 2026-08-11 — SCREENING: Japan (JP) — Round 3 (fresh candidate pool)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [JP](../framework/screening-coverage-log.md) (Japan, all sectors). Selected per the rotation rule: oldest "Last screened" date in the matrix (2026-07-21, ahead of NA-2 07-25, NA-1 07-28, APAC-ex-JP 08-01, EM 08-04, EU 08-08).

This was run as an **unattended scheduled routine** (Routine 4, twice-weekly universe screening slice — see [automation-schedule.md](../framework/automation-schedule.md)) with no interactive user present.

The [2026-06-30](2026-06-30-screening-japan.md) and [2026-07-21](2026-07-21-screening-japan.md) JP sessions together screened 31 names (21 + 9 quantitatively tested, 1 structurally excluded) and explicitly closed out both rounds of that candidate pool. This session builds a **fresh 15-name candidate pool** from sectors not yet covered in JP (industrial robotics, gaming/entertainment IP, enterprise SaaS, security services, cosmetics) rather than re-testing already-screened names.

---

## 0. Methodology and a stale-instruction flag

- **The scheduled task prompt for this run again referenced a "Monthly Universe Screening Slice" cadence and the deprecated `EODHD_API_KEY`-based "Path A" automation.** Both are stale: the actual configured cadence per [automation-schedule.md](../framework/automation-schedule.md) Routine 4 is **twice-weekly (Tuesday and Saturday)**, not monthly — today (2026-08-11) is a Tuesday, consistent with the real cadence, not the prompt's claimed "first Saturday of each month." EODHD was removed from the framework on 2026-06-19 ([decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)), which explicitly instructs treating that exact credential as **compromised** if it's ever needed again. `EODHD_API_KEY` is present in this environment but was **not used**, per CLAUDE.md's instruction that `framework/` (the current, canonical [screen.md](../.claude/commands/screen.md)) is the source of truth over a stored prompt — consistent with how the 2026-06-30, 2026-07-21, and 2026-08-04 sessions each handled this identical stale-prompt situation. **Recommend updating the scheduler's stored Routine 4 prompt text** to match the current cadence and data-source process so this stops needing to be re-flagged every run.
- **Step 0/1**: no interactive TIKR/Koyfin screener session was available (unattended run) — went straight to the documented unattended-session exception. Rather than the ETF-holdings fallback (which would just resurface the same large-cap names already in MOAT/QUAL/QGRW/IQLT, most already screened in Round 1), this round continued the same **structural-triage-from-domain-knowledge** approach the two prior JP rounds used, built around sectors not yet tested in this slice.
- **Step 2 data source**: `yfinance` was tested first (`pip install yfinance` succeeded) but failed immediately with `yfinance.exceptions.YFRateLimitError: Too Many Requests` on the cookie/crumb endpoint for a test ticker (6954.T) — a genuine 429, not a proxy/TLS failure. Switched to `stockanalysis.com` (via WebFetch: `/financials/ratios/`, `/financials/`, `/financials/cash-flow-statement/`, `/statistics/` pages per ticker, exchange code `tyo` confirmed against a live fetch), the same fallback used in every JP/EU/NA-1/APAC-ex-Japan session since 07-07. Data-gathering was delegated to 5 batches of research subagents (3 tickers each), run 2 concurrent at a time per the batch-processing policy in [new-position.md](../.claude/commands/new-position.md) — each agent's raw sourced figures are reflected directly in the table below.

### Structurally excluded categories (Step 1, before any quantitative pull)

Building on the exclusion categories already established in the 2026-06-30 JP session (megabanks, insurers, sogo shosha trading companies, mainstream automakers, steel/commodity majors, regulated utilities, telecom, airlines, railways, thin-margin retail, J-REITs), this round additionally screened out:

| Category | Examples | Why excluded |
|---|---|---|
| Diversified conglomerates with regulated/thin-margin segments blended in | Sony Group (gaming hardware + financial services + music/pictures), Panasonic Holdings | Segment-blended margins don't fit a single-business quality screen, same reasoning as the sogo shosha exclusion |
| Mature/lower-margin consumer & office electronics | Canon, Nikon, Ricoh, Konica Minolta, Casio, Kyocera, TDK | Structurally thin/moderate margins from hardware manufacturing, low structural growth |
| Commodity-cyclical semiconductor/component names | Renesas Electronics, Rohm Co | More commodity-cyclical than the semicap-equipment names already tested (Tokyo Electron, Advantest, Disco, Lasertec) |
| Commodity chemicals | Toray Industries, Asahi Kasei, Mitsubishi Chemical, Sumitomo Chemical | Commodity cyclical, same reasoning as prior chemical exclusions elsewhere in the framework |
| Beverages | Kirin Holdings, Asahi Group Holdings, Suntory | Mature, moderate-margin, regulated distribution networks |
| Diversified financial conglomerates / heavy-loss segments | ORIX Corp, SBI Holdings, GMO Internet Group (parent), Rakuten Group | Diversified financial-services structure doesn't fit the model; Rakuten specifically carries a persistently loss-making mobile segment |
| Unprofitable/thin-margin enterprise SaaS | Mercari, Money Forward, freee K.K. | Structurally fail the net-margin filter — still investing through losses/thin profitability, not yet quality-screen candidates |
| Thin-margin staffing/retail | Persol Holdings, Kobe Bussan, Cosmos Pharmaceutical | Same reasoning as prior thin-margin retail/staffing exclusions |
| Cyclical machinery/homebuilders | Kubota Corp, Yamaha Motor, Open House Group | Commodity-cyclical or interest-rate-sensitive cyclicals |

### Candidate pool this round (15 names)

| Ticker | Company | Sector |
|---|---|---|
| 6954.T | Fanuc Corp | Industrial robotics/factory automation |
| 6506.T | Yaskawa Electric | Industrial robotics |
| 6268.T | Nabtesco Corp | Precision reduction gears (robotics components) |
| 9962.T | Misumi Group | Factory automation supply/distribution |
| 4307.T | Nomura Research Institute | IT consulting/systems (financial-sector focus) |
| 4704.T | Trend Micro | Cybersecurity software |
| 7832.T | Bandai Namco Holdings | Entertainment/toys/games IP |
| 9684.T | Square Enix Holdings | Video games IP |
| 8136.T | Sanrio Co | Character licensing (Hello Kitty) |
| 3064.T | MonotaRO Co | Industrial supplies e-commerce |
| 9735.T | Secom Co | Security services |
| 4922.T | Kose Corp | Premium cosmetics |
| 3923.T | Rakus Co | Cloud/SaaS for SMEs |
| 6754.T | Anritsu Corp | Test & measurement equipment |
| 7951.T | Yamaha Corp | Musical instruments/audio |

---

## Step 2 — Quantitative Phase 01 gate (real, sourced data — stockanalysis.com, pulled 2026-08-11)

Filters: Gross margin >40% · Net margin >12% · ROIC>15% · Revenue growth >8% (3yr CAGR) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x. Where the "current/TTM" column and the last-completed-fiscal-year column diverged materially, the **current/TTM** column was used as the primary basis (consistent with the framework's TTM convention), with the FY figure noted for context.

| Company (Ticker) | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA | FCF yield (TTM) | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Fanuc Corp (6954.T) | 38.43% ❌ | 20.13% ✅ | 12.81% ❌ | 0.23% ❌ | ✅ | -3.14× ✅ | 3.78% ❌ | 23.16× ❌ | **FAIL — 3/8** |
| Yaskawa Electric (6506.T) | 35.01% ❌ | 6.07% ❌ | 5.87% ❌ | -0.84% ❌ | ✅ (3 consec.) | 0.94× ✅ | 1.08% ❌ | 31.58× ❌ | **FAIL — 2/8** |
| Nabtesco Corp (6268.T) | 32.36% ❌ | 6.97% ❌ | 7.04% ❌ | -0.08% ❌ | ✅ (2 consec. only ⚠️) | -0.97× ✅ | 4.53% ✅ | 17.86× ✅ | **FAIL — 3/8** (FCF-3yr also fails — only 2 consecutive positive years, not 3) |
| Misumi Group (9962.T) | 46.93% ✅ | 9.49% ❌ | 16.18% ✅ | 5.76% ❌ | ✅ | -1.40× ✅ | 4.42% ✅ | 15.53× ✅ | **FAIL — Net margin + Rev CAGR (6/8)** |
| Nomura Research Institute (4307.T) | 37.05% ❌ | 2.23% ❌ | 3.59% ❌ | 5.59% ❌ | ✅ | 0.91× ✅ | 5.46% ✅ | 46.06× ❌ | **FAIL — 3/8** ⚠️ FY2026 net income stepped down sharply vs. FY2022–25 — flagged as likely one-off charge |
| **Trend Micro (4704.T)** | 77.33% ✅ | 13.26% ✅ | 45.70% ✅ | 7.24% ❌ | ✅ (≥3 known) | -2.68× ✅ | N/A ⚠️ data gap | 11.57× ✅ | **FAIL — Rev CAGR only (6/8 known, 1 gap)** ⚠️ near-miss |
| Bandai Namco Holdings (7832.T) | 39.40% ❌ (narrow) | 10.43% ❌ (narrow) | 31.26% ✅ | 10.84% ✅ | ✅ | -1.51× ✅ | 3.70% ❌ (narrow) | 14.71× ✅ | **FAIL — 5/8** (3 narrow misses) |
| Square Enix Holdings (9684.T) | 53.40% ✅ | 9.95% ❌ | 39.22% ✅ | -4.64% ❌ | ✅ | -4.35× ✅ | 4.38% ✅ | 13.88× ✅ | **FAIL — 6/8** (net margin + declining revenue) |
| Sanrio Co (8136.T) | 77.32% ✅ | 28.14% ✅ | 123.21%/112.95% ✅ ⚠️ data flag | 38.77% ✅ | ✅ | -1.32× ✅ | 2.84% ❌ | 21.07× ❌ | **FAIL — Valuation only (6/8)** — very expensive |
| MonotaRO Co (3064.T) | 29.84% ❌ | 9.71% ❌ | 39.01% ✅ | 13.90% ✅ | ✅ | -0.63× ✅ | 2.61% ❌ | 18.34× ✅ | **FAIL — 5/8** |
| Secom Co (9735.T) | 31.73% ❌ | 8.96% ❌ | 11.86% ❌ | 4.51% ❌ | ✅ | -2.14× ✅ | 5.23% ✅ | 13.05× ✅ | **FAIL — 4/8** |
| Kose Corp (4922.T) | 69.04% ✅ | 4.58% ❌ | 4.10%/6.23% ❌ | 4.53% ❌ | ❌ (FY24–25 negative) | -2.54× ✅ | 0.17% ❌ | 21.04× ❌ | **FAIL — 2/8** |
| Rakus Co (3923.T) | 75.34% ✅ | 22.05% ✅ | 106.03%/92.06% ✅ ⚠️ data flag | 30.07% ✅ | ✅ | -0.75× ✅ | 3.21% ❌ | 21.35× ❌ | **FAIL — Valuation only (6/8)** |
| Anritsu Corp (6754.T) | 51.14% ✅ | 9.94% ❌ | 15.17% ✅ (TTM, narrow) | 1.93% ❌ | ✅ | -1.97× ✅ | 3.44% ❌ | 23.21× ❌ | **FAIL — 4/8** |
| Yamaha Corp (7951.T) | 37.60% ❌ | 5.10% ❌ | 6.66% ❌ | 1.02% ❌ | ✅ (3 consec., FY23 negative) | -1.96× ✅ | 7.00% ✅ | 13.92× ✅ | **FAIL — 4/8** |

---

## ✅ Qualified Quality List — 0 names

No candidate in this fresh 15-name pool cleared all 8 Phase 01 filters. The clearest pattern: Japan's highest-quality asset-light franchises in this pool (Sanrio, Rakus) have exceptional margins/ROIC/growth but are priced too richly (FCF yield <4%, EV/EBIT >20×) — the same "quality is real, valuation gate is the blocker" pattern already flagged for Keyence/Advantest/Disco/Tokyo Electron in Round 1. Elsewhere, margin/ROIC/growth shortfalls (not valuation) are the binding constraint — several industrial-automation and mature-franchise names (Fanuc, Yaskawa, Nabtesco, Secom, Kose, Anritsu, Yamaha) show flat-to-negative multi-year revenue growth, which is the single most common failure mode in this round.

### Near-miss flagged for the watchlist (fails only 1 filter, or 1 known filter with 1 data gap)

- **Trend Micro (4704.T)** — passes 6/8 known filters cleanly: exceptional margins (77.33% gross, 13.26% net), very strong ROIC (45.70%), FCF positive across all known years, net-cash balance sheet, and a cheap 11.57× EV/EBIT. Fails only Revenue 3yr CAGR (7.24% vs. the >8% bar — a narrow 0.76pp miss) computed from FY2022–FY2025 revenue (¥223,795M → ¥275,984M). **FCF yield (TTM) is a genuine data gap** — the statistics/ratios pages showed "N/A"/"–" for the current period despite FY2024/FY2023 values of 4.05%/5.38% being available, so the filter could not be scored either way this round; the most recently known annual figure (FY2024: 4.05%) would clear the >4% bar if used, but was not substituted per Rule 0. Worth a re-check next JP rotation once a fresher revenue print is available (a modest acceleration would clear the CAGR bar) and once the FCF-yield data gap resolves.

No other candidate in this round came within 1 filter of qualifying — Bandai Namco is the next-closest at 3 narrow misses (gross margin, net margin, FCF yield, each within ~1.5pp of its bar), but 3 simultaneous narrow misses doesn't meet the single-filter near-miss bar this framework uses for a watchlist flag.

---

## Step 3 — Qualitative pass

**Skipped.** Per [screen.md](../.claude/commands/screen.md) Step 3, the qualitative 5-question pass applies to clean Phase 01 PASSes (all 8 filters) — there were none this rotation. Trend Micro (the one near-miss) is flagged for the watchlist instead of receiving a full qualitative write-up, consistent with how prior JP/EU sessions have handled 6-7/8-filter near-misses without a clean pass.

---

## Data gaps flagged (per CLAUDE.md Rule 0 — none estimated)

- **Trend Micro (4704.T)**: FY2025 free cash flow and TTM FCF yield are both unavailable — the cash-flow-statement page had not been updated past FY2024 as of the fetch, even though the income-statement page already carries FY2025/TTM figures. The FCF-positive-3-years check was confirmed only through FY2024 (3 straight years: FY2022–FY2024); the TTM FCF yield filter could not be scored and is shown as a gap, not estimated from the older annual figure.
- **Nomura Research Institute (4307.T)**: FY2026 net income (¥15,257M, 1.87% margin) is a sharp step-down from FY2022–FY2025 (¥71–94B, 10.8–12.3% margin), with the same discontinuity visible in ROIC (17.63%→7.70%→3.59%) and EV/EBIT (16.84→46.06). Flagged as likely a one-time charge/write-off rather than a data error, but not verified against NRI's actual disclosures — the FAIL verdict is unaffected regardless (NRI fails on margin/ROIC/CAGR either way).
- **Sanrio (8136.T)**: ROIC shown as 123.21% (ratios page, FY2026) vs. 112.95% (statistics page) — an unreconciled internal inconsistency between the site's own pages; both values clear the >15% bar by a wide margin, so the PASS call on this one filter is unaffected.
- **Rakus Co (3923.T)**: ROIC of 92–106% is unusually high for a SaaS business — genuinely sourced (not blank/implausible enough to require an ROE substitution per the framework's stated trigger), but flagged for analyst judgment given how far outside typical ranges it sits; ROE (55.38%, current) was pulled as an independent cross-check and is directionally consistent (also very high).
- **Yaskawa Electric (6506.T), Nabtesco (6268.T), MonotaRO (3064.T), Secom (9735.T), Kose (4922.T), Anritsu (6754.T), Yamaha Corp (7951.T)**: all seven showed a recurring discrepancy where the **statistics page's** headline "Net Debt/EBITDA" figure used **gross** Debt/EBITDA (ignoring cash) or otherwise contradicted the page's own stated net-cash/net-debt figure, while the **ratios page** figure correctly netted cash against debt and matched an independent manual recomputation from the same page's raw Total Debt/Cash/EBITDA components in every case. The ratios-page (or manually recomputed net) figure was used as authoritative throughout this session, consistent with the same sign/labeling issue first flagged in the 2026-07-21 JP session for Yaskawa/Nabtesco specifically — this now looks like a systematic stockanalysis.com statistics-page artifact rather than a per-ticker anomaly, worth carrying forward as a standing caveat for any future stockanalysis.com-sourced screening session.
- **Kose Corp (4922.T)**: FCF turned negative in FY2024 (-¥382M) and FY2025 (-¥5,924M) after a capex spike (¥17–19B/yr vs. ¥3–4B/yr in FY2022–23) — not confirmed whether this is a one-off capital project or a structural shift; Kose fails independently on margin/ROIC/growth regardless, so this doesn't change the verdict.
- **Anritsu (6754.T) and Yamaha Corp (7951.T)**: ROIC/ROE diverged materially between the "current/TTM" and last-annual-FY columns for both (Anritsu: 15.17% TTM vs. 12.52% FY; Yamaha ROE blank for FY2024 entirely). Both fail independently on other filters regardless of which column is used.

---

## Next steps

- No `/new-position` candidates from this rotation — zero clean Phase 01 PASSes.
- Watchlist (no formal entry created by `/screen`; re-check on next JP rotation or a fresher print): **Trend Micro (4704.T)** — Revenue 3yr CAGR the only known blocker (7.24% vs. >8%, a narrow 0.76pp miss), plus an unresolved FCF-yield-TTM data gap to re-verify.
- Standing note carried forward: Japan's highest-quality asset-light franchises across all three JP rounds so far (Keyence, Advantest, Disco, Tokyo Electron from Round 1; now Sanrio and Rakus from this round) keep clearing quality/growth filters comfortably but fail specifically on valuation (FCF yield, EV/EBIT) — worth a standing watch for a future rotation if multiples compress.
- Deferred for a future JP deep-dive (not yet screened in any of the 3 rounds): further gaming names (Capcom, Konami Group, Nexon), diagnostics/pharma adjacent names beyond Chugai/Sysmex/Terumo already tested, and a dedicated look at Japan's smaller-cap SaaS/software names beyond Rakus/SHIFT/Obic already tested (e.g. Infomart, Cybozu, freee once profitable).
- **Process flag for the automation owner:** the scheduled Routine 4 prompt still references a monthly cadence and the deprecated EODHD `Path A` automation, despite the actual configured cadence being twice-weekly (Tuesday/Saturday) per `automation-schedule.md`. This is the fourth consecutive JP-adjacent session flagging this same stale-prompt issue (06-30, 07-21, 08-04 EM session, now this one) — recommend updating the scheduler's stored prompt text directly rather than continuing to re-flag it per run.
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
- **ROE** — Return on Equity — Net Income ÷ shareholder equity; how efficiently a company generates profit from shareholders' capital.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to never invent or estimate financial data — if a metric is missing, flag it and stop rather than infer it; also covers always fetching a live price before valuation work.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure.

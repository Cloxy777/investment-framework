# 2026-06-30 — SCREENING: Japan (JP)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [JP](../framework/screening-coverage-log.md) (Japan, all sectors). Selected per the rotation rule: tied for "Never screened" with NA-2, first alphabetically among those (independently cross-checked against the EU session's own forward-pointer, which named JP as the next slice).

This was run as an **unattended scheduled routine** (Routine 4, twice-weekly universe screening slice — see [automation-schedule.md](../framework/automation-schedule.md)) with no interactive user present.

---

## 0. Methodology

No interactive TIKR/Koyfin screener export was available — there was no user to ask, so per Step 0's documented unattended-session exception, this session went straight to the structural-triage fallback rather than waiting on screener access.

- **Step 0/1 used structural triage from domain knowledge** (same precedent as the EU/APAC-ex-Japan/EM sessions): built a 21-name candidate pool of well-known, large/mid-cap Japanese businesses, skipping categories that structurally don't fit this framework's model.
- **Step 2 used `yfinance`** per-candidate to pull real, sourced numbers — `t.info`, `t.financials`, `t.cashflow`, `t.balance_sheet` — for every survivor, exactly as documented in [valuation-scoring.md](../framework/valuation-scoring.md).
- **EODHD was NOT used.** This session's original task prompt referenced an `EODHD_API_KEY`-based automation path, but that path was deprecated and removed from the framework on 2026-06-19 ([decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)), which explicitly instructs treating that credential as compromised if it's ever needed again. The current canonical [screen.md](../.claude/commands/screen.md) and [automation-schedule.md](../framework/automation-schedule.md) have no EODHD path at all — `yfinance` is the sole automated data source. This session followed the current, canonical process per CLAUDE.md's instruction that `framework/` is the source of truth.
- **Network/TLS note:** `yfinance` v1.5.1's default `curl_cffi` transport failed TLS negotiation through this environment's mandatory proxy. Fixed by passing a plain `requests.Session()` into `yf.Ticker(ticker, session=sess)`, forcing standard-`requests` transport — verified working before the full pull (test ticker: 7203.T / Toyota, excluded from the final candidate pool as a mainstream automaker, but used only to confirm connectivity). The proxy itself was never bypassed or disabled.
- Yahoo Finance rate-limited (HTTP 429) the sequential per-ticker pulls increasingly heavily as the run progressed; the pull script's retry/backoff logic (up to 6 retries, 8s→60s exponential backoff) absorbed this without data loss — all 21 candidates were successfully retrieved, just slowly (total pull time approached the session's planned ceiling).

### Structurally excluded categories (Step 1, before any quantitative pull)

| Category | Examples | Why excluded |
|---|---|---|
| Megabanks | MUFG, Sumitomo Mitsui Financial Group, Mizuho | Gross margin doesn't apply; regulated balance-sheet businesses don't fit this framework's model |
| Insurers | Tokio Marine, MS&AD Insurance, Dai-ichi Life | Same reasoning as banks |
| Trading companies (sogo shosha) | Mitsubishi Corp, Mitsui & Co, Itochu, Sumitomo Corp, Marubeni | Diversified commodity/trading conglomerates — margin/ROIC structure doesn't fit a single-business quality screen |
| Mainstream automakers | Toyota, Honda, Nissan, Subaru | Thin-margin cyclical (same precedent as VW/Mercedes/Stellantis in the EU session) |
| Steel/commodity majors | Nippon Steel, JFE Holdings | Commodity cyclical |
| Regulated utilities | TEPCO, Kansai Electric Power | Regulated utility — doesn't fit framework |
| Telecom | NTT, KDDI, SoftBank Corp | Capital-intensive, regulated, structurally low growth/margin |
| Airlines | ANA Holdings, Japan Airlines | Commodity cyclical (fuel/labor), thin margins |
| Railways | JR East, JR Central, JR West | Regulated, capital-intensive, low structural growth |
| Thin-margin retail | Seven & I Holdings, Aeon | Thin-margin retail (NA-1 precedent: WMT/COST/TJX) |
| J-REITs | Nippon Building Fund, Japan Real Estate Investment Corp | REIT — gross margin/EV-EBIT framing doesn't fit |

### Candidate pool (21 names, structural-triage survivors)

| Ticker | Company | Sector |
|---|---|---|
| 6861.T | Keyence | Factory automation sensors |
| 7974.T | Nintendo | Video games/entertainment |
| 6098.T | Recruit Holdings | HR tech/job listings (Indeed) |
| 8035.T | Tokyo Electron | Semicap equipment |
| 6857.T | Advantest | Semicap test equipment |
| 6146.T | Disco Corp | Semicap precision tools (dicing/grinding) |
| 2413.T | M3 Inc | Medical/healthcare platform |
| 3697.T | SHIFT Inc | Software QA/testing services |
| 4684.T | Obic | Enterprise ERP software |
| 9983.T | Fast Retailing | Apparel retail (Uniqlo) |
| 4519.T | Chugai Pharmaceutical | Pharma (Roche-affiliated) |
| 6869.T | Sysmex | Medtech (diagnostics) |
| 4543.T | Terumo | Medtech (devices) |
| 7733.T | Olympus | Medtech (endoscopy) |
| 7741.T | Hoya Corp | Optics/medtech/semicap components |
| 7309.T | Shimano | Bicycle components |
| 6981.T | Murata Manufacturing | Electronic components |
| 6594.T | Nidec | Precision motors |
| 6367.T | Daikin Industries | HVAC equipment |
| 6273.T | SMC Corp | Pneumatic automation components |
| 8697.T | Japan Exchange Group | Exchange/clearing |

Not exhaustive of Japanese quality businesses — deferred names for a future deep-dive are listed under Next Steps.

---

## Step 2 — Quantitative Phase 01 gate (real, sourced data — `yfinance`, pulled 2026-06-30)

Filters: Gross margin >40% · Net margin >12% · ROIC>15% (ROE used as proxy, per EU/APAC/EM precedent) · Revenue growth >8% (3yr CAGR) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x

FCF yield uses `info["freeCashflow"]` (TTM) ÷ market cap, the same TTM-basis field documented in [valuation-scoring.md](../framework/valuation-scoring.md). Net Debt uses the balance-sheet "Cash And Cash Equivalents" line specifically (falling back to "Total Debt" / 0 where a debt line wasn't reported, i.e. net-cash companies), applied consistently across all names. EV/EBIT uses the most recent annual EBIT from `t.financials` — `info["ebit"]` returned `None` for every one of the 21 candidates this session (a `yfinance` field-coverage gap on the JP exchange, not a per-company anomaly), so the annual income-statement EBIT series was used instead, consistent with the framework's documented fallback.

| Company (Ticker) | Gross M | Net M | ROE | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA | FCF yield (TTM) | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Keyence (6861.T) | 83.02% ✅ | 38.07% ✅ | 13.53% ❌ | 8.23% ✅ | ✅ | -0.97× ✅ | 1.57% ❌ | 29.33× ❌ | **FAIL — 5/8** |
| Nintendo (7974.T) | 39.30% ❌ | 18.33% ✅ | 14.93% ❌ (barely) | 13.03% ✅ | ❌ (FY25 negative) | -4.77× ✅ | 3.53% ❌ | 10.17× ✅ | **FAIL — 4/8** |
| Recruit Holdings (6098.T) | 59.18% ✅ | 13.44% ✅ | 30.83% ✅ | 2.54% ❌ | ✅ | -0.77× ✅ | 2.70% ❌ | 23.15× ❌ | **FAIL — 5/8** |
| Tokyo Electron (8035.T) | 45.34% ✅ | 23.51% ✅ | 29.27% ✅ | 3.42% ❌ | ✅ | -0.64× ✅ | 0.65% ❌ | 53.56× ❌ | **FAIL — 5/8** |
| Advantest (6857.T) | 64.34% ✅ | 33.26% ✅ | 57.65% ✅ | 26.30% ✅ | ✅ | -0.62× ✅ | 1.02% ❌ | 43.96× ❌ | **FAIL — 6/8** — valuation only, but very expensive |
| Disco Corp (6146.T) | 70.15% ✅ | 31.02% ✅ | 25.09% ✅ | 15.42% ✅ | ✅ | -1.43× ✅ | 0.84% ❌ | 45.11× ❌ | **FAIL — 6/8** — valuation only, but very expensive |
| **M3 Inc (2413.T)** | 50.05% ✅ | 13.97% ✅ | 12.58% ❌ | 15.03% ✅ | ✅ | -1.39× ✅ | 5.17% ✅ | 14.71× ✅ | **FAIL — ROE only (7/8)** ⚠️ near-miss |
| SHIFT Inc (3697.T) | 34.18% ❌ | 6.03% ❌ | 22.63% ✅ | 26.02% ✅ | ✅ | -0.66× ✅ | 5.47% ✅ | 12.15× ✅ | **FAIL — 6/8** |
| **Obic (4684.T)** | 78.15% ✅ | 55.61% ✅ | 15.83% ✅ | 10.52% ✅ | ✅ | -2.27× ✅ | 3.58% ❌ | 16.26× ✅ | **FAIL — FCF yield only (7/8)** ⚠️ near-miss |
| Fast Retailing (9983.T) | 54.17% ✅ | 13.06% ✅ | 20.62% ✅ | 13.90% ✅ | ✅ | -0.54× ✅ | 1.87% ❌ | 36.83× ❌ | **FAIL — 6/8** |
| Chugai Pharmaceutical (4519.T) | 71.45% ✅ | 35.02% ✅ | 23.71% ✅ | -0.05% ❌ | ✅ | -0.67× ✅ | 2.49% ❌ | 19.42× ✅ | **FAIL — 6/8** |
| Sysmex (6869.T) | 51.14% ✅ | 7.09% ❌ | 7.29% ❌ | 11.82% ✅ | ✅ | -0.23× ✅ | -0.08% ❌ ⚠️ | 11.01× ✅ | **FAIL — 5/8** |
| Terumo (4543.T) | 52.74% ✅ | 12.01% ❌ (0.01pp short) | 9.21% ❌ | 11.33% ✅ | ✅ | 0.37× ✅ | 2.12% ❌ | 19.07× ✅ | **FAIL — 5/8** |
| Olympus (7733.T) | 64.72% ✅ | 6.74% ❌ | 8.72% ❌ | 4.65% ❌ | ❌ (FY24 negative) | 0.25× ✅ | 0.14% ❌ | 18.23× ✅ | **FAIL — 3/8** |
| Hoya Corp (7741.T) | 54.97% ✅ | 26.70% ✅ | 25.06% ✅ | 10.70% ✅ | ✅ | -1.46× ✅ | 1.96% ❌ | 24.62× ❌ | **FAIL — 6/8** |
| Shimano (7309.T) | 34.73% ❌ | 7.87% ❌ | 4.37% ❌ | -9.49% ❌ | ✅ | -6.42× ✅ | N/A ⚠️ data gap | 18.63× ✅ | **FAIL — 3/8** |
| Murata Manufacturing (6981.T) | 42.32% ✅ | 12.78% ✅ | 8.83% ❌ | 2.77% ❌ | ✅ | -1.17× ✅ | 0.55% ❌ | 60.77× ❌ | **FAIL — 4/8** |
| Nidec (6594.T) | 19.37% ❌ | 4.59% ❌ | 6.31% ❌ | 10.78% ✅ | ❌ (FY23 negative) | 1.59× ✅ | 1.83% ❌ | 13.14× ✅ | **FAIL — 3/8** |
| Daikin Industries (6367.T) | 34.55% ❌ | 5.49% ❌ | 9.26% ❌ | 7.99% ❌ (barely — 0.005pp short) | ✅ | 0.23× ✅ | 1.80% ❌ | 16.69× ✅ | **FAIL — 3/8** |
| SMC Corp (6273.T) | 45.27% ✅ | 19.86% ✅ | 8.27% ❌ | 0.71% ❌ | ❌ (FY24 negative) | -2.80× ✅ | -0.82% ❌ ⚠️ | 15.75× ✅ | **FAIL — 4/8** |
| Japan Exchange Group (8697.T) | 100.00% ✅ ⚠️ data flag | 39.82% ✅ | 22.97% ✅ | 6.87% ❌ | ✅ | -0.44× ✅ | 4.14% ✅ | 22.65× ❌ | **FAIL — 6/8** |

---

## ✅ Qualified Quality List — 0 names

No candidate in this slice cleared all 8 Phase 01 filters this rotation. The two closest are flagged below as near-misses for the watchlist; everything else fails on 2 or more filters, most commonly valuation (EV/EBIT, FCF yield) on the semicap/automation names — Japan's highest-quality industrial/tech franchises (Keyence, Advantest, Disco, Tokyo Electron) are priced well above this framework's value discipline right now — or growth/margin softness elsewhere (Sysmex, Terumo, Olympus, Murata, Nidec, Daikin).

### Near-misses flagged for the watchlist (fail only 1 filter — re-check on next rotation or a pullback/data refresh)

- **M3 Inc (2413.T)** — passes 7/8; fails only ROE (12.58%, vs. the 15% bar — proxy for ROIC). Gross margin (50.05%), net margin (13.97%), revenue 3yr CAGR (15.03%), FCF-positive 3yr, leverage (net cash), FCF yield (5.17%) and EV/EBIT (14.71×) are all comfortably inside the gate. A genuinely attractive name on valuation and growth; the ROE shortfall is the only thing keeping it out.
- **Obic (4684.T)** — passes 7/8; fails only FCF yield (3.58%, vs. the 4% bar), and only by 0.42pp. Margins are exceptional (78.15% gross, 55.61% net), ROE (15.83%) and revenue growth (10.52%) both clear, balance sheet is net-cash, and EV/EBIT (16.26×) is reasonable. The closest miss in this slice.

---

## Step 3 — Qualitative pass

**Skipped.** Per [screen.md](../.claude/commands/screen.md) Step 3, the qualitative 5-question pass applies to clean Phase 01 PASSes (all 8 filters) — there were none this rotation. The two near-misses above (M3 Inc, Obic) are flagged for the watchlist instead of receiving a full qualitative write-up, consistent with how prior screening sessions (e.g. EU, 2026-06-19) have handled 7/8-filter near-misses.

---

## Data gaps flagged (per CLAUDE.md Rule 0 — none estimated)

- **`info["ebit"]` returned `None` for all 21 candidates** — a `yfinance` field-coverage gap specific to (at least) the Tokyo Stock Exchange this session; not a per-company data issue. Worked around by using the most recent annual EBIT from `t.financials` instead, per the framework's documented fallback — this is a methodology note, not an unresolved gap.
- **Shimano (7309.T)**: `info["freeCashflow"]` (TTM) was `None` — FCF yield could not be computed and was not estimated; marked N/A rather than scored. Shimano fails on 5 other filters regardless (gross margin, net margin, ROE, revenue CAGR all fail), so this gap did not affect the overall verdict.
- **Sysmex (6869.T)**: TTM `freeCashflow` (-¥748M) is negative while the annual cash-flow statement shows 3 consecutive positive years (most recent ¥38.3B) — both `yfinance`-sourced, not reconciled here. FCF-positive-3yr check used the annual series (passes); FCF yield used the TTM figure (fails) per the framework's stated TTM convention — flagged as an internal inconsistency worth resolving via a live `/new-position` pull if this name is ever revisited.
- **SMC Corp (6273.T)**: same TTM-vs-annual FCF inconsistency as Sysmex — TTM `freeCashflow` is negative (-¥37.1B) while FY2026 annual FCF is positive (¥34.5B); FY2024 annual FCF was negative (-¥6.1B), so SMC fails the FCF-positive-3yr check independently of this discrepancy.
- **Japan Exchange Group (8697.T)**: `grossMargins` reported as exactly 100.00% — the same data-artifact pattern flagged for Halma in the EU session (likely a missing cost-of-revenue line in the source filing format for an exchange/clearing business with no traditional COGS). Not used to inflate the verdict; JXG fails independently on revenue 3yr CAGR (6.87%) and EV/EBIT (22.65×).
- **Terumo (4543.T)**: net margin (12.01%) clears the >12% bar by only 0.01 percentage points — flagged as effectively a coin-flip precision case rather than a clean pass; shown as a fail above per the strict ">" (not "≥") threshold, consistent with the framework's literal filter definitions, but worth a live re-check given how close it is.
- **Daikin Industries (6367.T)**: revenue 3yr CAGR computed at 7.9957% — technically below the 8% bar by 0.0043pp, displayed as "7.99% (barely)" above. Daikin fails 4 other filters regardless (gross margin, net margin, ROE all fail), so this near-zero margin of failure on growth alone did not change the overall verdict.

---

## Next steps

- No `/new-position` candidates from this rotation — zero clean Phase 01 PASSes.
- Watchlist (no new formal entry, re-check on next JP rotation or a pullback): **M3 Inc (2413.T)** — ROE the only blocker; **Obic (4684.T)** — FCF yield the only blocker, and the closer of the two misses by margin.
- Japan's highest-quality factory-automation/semicap franchises (Keyence, Advantest, Disco Corp, Tokyo Electron) are real quality businesses on every metric except valuation — all four clear 5-6 of 8 filters and fail specifically on FCF yield and/or EV/EBIT, reflecting how richly the AI/semicap supply-chain theme is currently priced in Japan. Worth a standing note for a future rotation if multiples compress.
- Deferred to a future JP deep-dive (not yet quantitatively screened this pass): Shin-Etsu Chemical, Kao Corp, Unicharm, Lasertec, Tokyo Ohka Kogyo, GMO Payment Gateway, Pigeon Corp, Pan Pacific International (Don Quijote), Nihon M&A Center, en Japan.
- Coverage log updated below — next "Never screened" slice in the rotation is **NA-2**.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **EBIT** — Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit.
- **EV** — Enterprise Value — a company's total value to all capital providers: market cap + debt − cash.
- **EV/EBIT** — Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to their operating profit, independent of capital structure.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap — how much free cash a company throws off relative to its price; higher is cheaper.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
- **pp (percentage points)** — A direct difference between two percentages (e.g. 8.23% vs. an 8% bar is +0.23pp), distinct from a "%" change.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring.
- **ROE** — Return on Equity — Net Income ÷ shareholder equity; how efficiently a company generates profit from shareholders' capital.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to never invent or estimate financial data — if a metric is missing, flag it and stop rather than infer it.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure.

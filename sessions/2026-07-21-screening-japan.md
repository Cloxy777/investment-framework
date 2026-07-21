# 2026-07-21 — SCREENING: Japan (JP) — Round 2 (deferred names)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [JP](../framework/screening-coverage-log.md) (Japan, all sectors). Selected per the rotation rule: oldest "Last screened" date in the matrix (2026-06-30, ahead of NA-2 07-04, NA-1 07-07, APAC-ex-JP 07-11, EM 07-14, EU 07-18).

This was run as an **unattended scheduled routine** (Routine 4, monthly universe screening slice — see [automation-schedule.md](../framework/automation-schedule.md)) with no interactive user present.

This round completes the JP slice by covering the **10 names deferred** from the [2026-06-30 JP session](2026-06-30-screening-japan.md)'s "Next steps" (Shin-Etsu Chemical, Kao Corp, Unicharm, Lasertec, Tokyo Ohka Kogyo, GMO Payment Gateway, Pigeon Corp, Pan Pacific International, Nihon M&A Center, en Japan) — the same "Round 2, deferred names" pattern used for the EU slice on 2026-07-18.

---

## 0. Methodology and a stale-instruction flag

- **The scheduled task prompt for this run referenced an `EODHD_API_KEY`-based automation path ("Path A") that no longer exists.** That path was deprecated and removed from the framework on 2026-06-19 ([decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)), which explicitly instructs treating that exact credential as **compromised** if it's ever needed again (it was a live key committed to git history, since scrubbed from the framework's docs). The current canonical [screen.md](../.claude/commands/screen.md) has no EODHD/Path-A branch at all — `yfinance` (or its documented fallback) is the sole automated data source. Per CLAUDE.md, `framework/` is the source of truth over a stored prompt, so this session did **not** use EODHD_API_KEY, consistent with how the 2026-06-30 JP session handled the identical stale-prompt situation. Flagging this again here since the scheduler is still firing the outdated prompt text every month — worth updating the schedule's stored prompt to stop referencing EODHD.
- **Step 0/1**: no interactive TIKR/Koyfin screener session was available (unattended run). Rather than re-running a fresh ETF-holdings pass (which would just resurface the same large/mega-cap names already covered 2026-06-30), this round continued that session's own structural-triage candidate pool — the 10 names it explicitly deferred for a future deep-dive.
- **Step 2 data source**: `yfinance` was not used this round. `pip install yfinance` succeeded, but a live test against `7203.T` returned `yfinance.exceptions.YFRateLimitError: Too Many Requests` directly from Yahoo's cookie/crumb endpoint (not a TLS/proxy failure this time — a genuine 429). Switched to `stockanalysis.com` (via WebFetch: `/financials/ratios/`, `/financials/`, `/financials/cash-flow-statement/`, `/statistics/` pages per ticker), the same fallback used in the NA-1/APAC-ex-Japan/EU-round-2 sessions. Data-gathering was delegated to 4 batches of research subagents (2–3 tickers each) to keep the fetch volume manageable; each agent's raw sourced figures and PASS/FAIL calls are reflected directly in the table below.

### Structurally excluded (Step 1, before any quantitative pull)

- **Pan Pacific International Holdings (7532.T, Don Quijote)** — thin-margin volume discount retail, same exclusion rationale applied to Seven & I/Aeon in the 2026-06-30 JP session and WMT/COST/TJX in the NA-1 session. Not quantitatively screened.

### Candidate pool this round (9 names, after the above exclusion)

| Ticker | Company | Sector |
|---|---|---|
| 4063.T | Shin-Etsu Chemical | Specialty/semiconductor-materials chemicals |
| 4452.T | Kao Corp | Consumer personal care/cosmetics |
| 8113.T | Unicharm | Consumer hygiene products |
| 6920.T | Lasertec | Semicap (EUV mask inspection) equipment |
| 4186.T | Tokyo Ohka Kogyo | Semiconductor materials (photoresist) |
| 3769.T | GMO Payment Gateway | Payment processing/fintech |
| 7956.T | Pigeon Corp | Baby/infant care products |
| 2127.T | Nihon M&A Center Holdings | M&A advisory services |
| 4849.T | en Japan | HR/recruitment |

---

## Step 2 — Quantitative Phase 01 gate (real, sourced data — stockanalysis.com, pulled 2026-07-21)

Filters: Gross margin >40% · Net margin >12% · ROIC>15% · Revenue growth >8% (3yr CAGR) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x. ROIC is used directly (stockanalysis.com reports it), not the ROE proxy the yfinance-based sessions needed — except GMO Payment Gateway, flagged below.

| Company (Ticker) | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA | FCF yield (TTM) | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Shin-Etsu Chemical (4063.T) | 34.22% ❌ | 18.43% ✅ | 14.07% ❌ | -2.87% ❌ | ✅ | -1.62× ✅ | 2.68% ❌ | 19.13× ✅ | **FAIL — 4/8** |
| Kao Corp (4452.T) | 39.57% ❌ (narrow) | 7.11% ❌ | 12.21% ❌ | 2.87% ❌ | ✅ | -0.14× ✅ | 4.65% ✅ | 16.13× ✅ | **FAIL — 4/8** |
| Unicharm (8113.T) | 39.10% ❌ (narrow) | 6.90% ❌ | 11.14% ❌ | 1.73% ❌ | ✅ | -1.40× ✅ | 6.35% ✅ | 13.86× ✅ | **FAIL — 4/8** |
| Lasertec (6920.T) | 58.95% ✅ | 33.66% ✅ | 59.77% ✅ | 40.65% ✅ | ✅ | -0.63× ✅ | 1.81% ❌ | 30.76× ❌ | **FAIL — 6/8** — valuation only, but very expensive |
| Tokyo Ohka Kogyo (4186.T) | 37.73% ❌ | 14.07% ✅ | 20.37% ✅ | 10.54% ✅ | ✅ | -0.61× ✅ | N/A ⚠️ data gap | 22.10× ❌ | **FAIL — ≥6/7 known (1 gap)** |
| **GMO Payment Gateway (3769.T)** | 67.27% ✅ | 26.46% ✅ | 21.79% ✅ ⚠️ ROE proxy | 17.94% ✅ | ✅ | -4.12× ✅ | 6.07% ✅ | 16.90× ✅ | **PASS — 8/8** ✅ |
| Pigeon Corp (7956.T) | 50.23% ✅ | 7.85% ❌ | 18.42% ✅ | 4.77% ❌ | ✅ | -2.15× ✅ | N/A ⚠️ data gap | 15.48× ✅ | **FAIL — ≥5/7 known (1 gap)** |
| **Nihon M&A Center (2127.T)** | 60.25% ✅ | 24.85% ✅ | 87.58% ✅ | 6.75% ❌ | ✅ | -2.00× ✅ | 7.13% ✅ | 9.49× ✅ | **FAIL — CAGR only (7/8)** ⚠️ near-miss |
| en Japan (4849.T) | 83.96% ✅ | 4.43% ❌ | 19.70%–25.01% ✅ ⚠️ internal inconsistency | -4.44% ❌ | ✅ | -2.41× ✅ | 7.20% ✅ | 7.33× ✅ | **FAIL — 6/8** |

---

## ✅ Qualified Quality List — 1 name

### GMO Payment Gateway (3769.T) — passes 8/8

Japan's #1-market-share independent payment gateway/processor (~23% of Japan's electronic-payment market, per third-party estimates), processing >¥17T in annual transaction volume across 150,000+ merchants as of 2024. Clears every filter cleanly except a data-quality caveat on ROIC (see below).

**⚠️ Data-quality flag (ROIC):** the stockanalysis.com ratios page reported ROIC as "–" (blank) for nearly every recent period except one outlier (FY2023: 424.76%, implausible on its face — almost certainly an invested-capital-denominator artifact, not a real figure). Rather than use that outlier, the sourcing agent substituted **ROE (21.79% current / 20.30% FY2025)** as a labeled proxy, consistent with the framework's ROE-proxy precedent from earlier yfinance-based sessions. Both figures clear the >15% bar, but this should be re-verified against a primary-source ROIC calculation (not proxied) before finalizing a Phase 02 valuation score — flagging per Rule 0 rather than treating the proxy as settled.

### Near-miss flagged for the watchlist (fails only 1 filter)

- **Nihon M&A Center Holdings (2127.T)** — passes 7/8; fails only Revenue 3yr CAGR (6.75% vs. the >8% bar, 1.25pp short). Every other filter is comfortably clear: 60.25% gross margin, 24.85% net margin, 87.58% ROIC (genuinely exceptional, not a proxy), 4 consecutive years of positive FCF, net-cash balance sheet, 7.13% FCF yield, and a cheap 9.49× EV/EBIT. The valuation looks unusually attractive for a business this profitable — worth a re-check next JP rotation or if a fresher revenue print moves the CAGR over the bar (FY2025 was roughly flat before FY2026's 14% jump, so this could resolve either direction on the next annual print).

---

## Step 3 — Qualitative pass (GMO Payment Gateway, the one clean PASS)

1. **Why are margins high?** GMO-PG is the largest independent payment gateway in Japan, providing back-end payment infrastructure to both private-sector giants (e.g. Amazon Japan) and public-sector bodies (e.g. the National Tax Agency). Over 70% of revenue is "stock-type" (recurring) — subscription/transaction-based fees from deep, sticky integrations with merchants and financial institutions, including a white-label platform ("Ginko Pay") used by major banks. High operating leverage on top of a largely fixed processing/infrastructure cost base.
2. **What would it take to compete?** A new entrant would need to replicate years of direct integrations with Japan's major banks, card networks, and large merchants, plus the trust/compliance track record needed to process government and enterprise payment flows. GMO-PG's scale (17T+ yen annual transaction volume, 150,000+ merchants) gives it cost and reliability advantages a smaller processor can't easily match — consistent with how payment-network/processor moats are treated elsewhere in this framework (cf. Visa/Mastercard-style analyses).
3. **Capital allocation (5–10yr):** Diversifying beyond core payment processing into structured/specialty finance — e.g. the 2026 partnership with Mesirow Alternative Credit providing investment capital for specialty-finance transactions — alongside continued reinvestment in the core gateway business and stated overseas-expansion ambitions (leadership has explicitly called out wanting international growth). Also raising capital via euro-yen convertible bonds (¥20B face value, due 2026) to fund this expansion, which modestly dilutes/adds leverage optionality worth tracking.
4. **Where's growth coming from (3–5yr)?** Continued e-commerce/cashless-payment penetration in Japan (still has room to grow vs. more cashless-mature markets), expansion of adjacent fintech services (transaction lending, BNPL, structured/specialty credit), and stated overseas expansion into other Asian fintech markets. Management has reiterated a ¥100B operating-profit target for FY2030–2031, with H1 FY2026 operating and after-tax profit both up ~22–23% YoY.
5. **Best bear case:** Revenue is ultimately tied to Japanese e-commerce/card-payment transaction volume — a slowdown in Japanese consumer spending or a shift toward alternative rails (bank-to-bank instant payment schemes, QR-code wallets bypassing card rails) could compress the core business's growth. The move into specialty/structured finance is a genuine departure from the asset-light payment-processing model that built the moat — a credit-underwriting misstep there is a different, less-understood risk than anything in the core gateway business, and bears direct watching given it's a stated growth priority rather than a side experiment.
6. **Disruption vector:** Moderate. Japan's cashless-payment penetration is a multi-year structural tailwind, not a threat, and GMO-PG's incumbency/integration depth is a real moat against new processors. The more relevant risk is strategic drift — capital and management attention shifting toward credit/structured-finance activities that carry a different risk profile than the core payments moat this Qualified pass is based on.

**Conclusion:** A genuine, well-established quality business (dominant domestic market share, high recurring-revenue mix, strong balance sheet) trading at a reasonable 16.90× EV/EBIT for its growth/profitability profile. **Recommend `/new-position GMO-PG` (3769.T)** for full Phase 02 scoring with live pricing — and re-verify ROIC from a primary source (not the ROE proxy used here) as part of that pull, per the data-quality flag above.

---

## Data gaps flagged (per CLAUDE.md Rule 0 — none estimated)

- **GMO Payment Gateway (3769.T)**: ROIC unavailable/implausible on stockanalysis.com's ratios page (blank for most periods, one 424.76% outlier) — substituted ROE as a labeled proxy rather than using or estimating a fabricated ROIC figure. See the Qualified Quality List entry above.
- **Tokyo Ohka Kogyo (4186.T)** and **Pigeon Corp (7956.T)**: FCF Yield / FCF (TTM) reported as "n/a" on the statistics page for both, despite annual FCF being populated on the cash-flow-statement page — not estimated or substituted with the annual figure as a TTM proxy. Both names fail independently on other filters (Tokyo Ohka Kogyo on gross margin and EV/EBIT; Pigeon on net margin and revenue CAGR), so this gap does not change either verdict.
- **Shin-Etsu Chemical (4063.T)**: ROIC shown as 14.07% ("current") vs. 14.50% (FY2026 column) on the same ratios page — an unreconciled internal inconsistency; both values fail the >15% bar regardless, so the verdict is unaffected.
- **en Japan (4849.T)**: ROIC shown as 19.70% ("current") vs. 25.01% (FY2026 column) on the same ratios page — same type of unreconciled inconsistency as Shin-Etsu; both values clear the >15% bar, so this particular filter's PASS call is unaffected, but en Japan fails independently on net margin and revenue CAGR (revenue has declined for 3 consecutive fiscal years).
- **Kao Corp (4452.T)**: cash-flow-statement TTM period is labeled "Mar '26" despite Kao's fiscal year ending in December (FY2023–FY2025 labeled by calendar year) — the underlying FCF figure is internally consistent with the statistics-page TTM number, only the period label looks misaligned; not reconciled here.
- **Unicharm (8113.T)** and **Nihon M&A Center (2127.T)/GMO-PG**: minor (~3–9%) TTM-vs-most-recent-annual-period FCF discrepancies between the statistics page and cash-flow-statement page, plausibly explained by non-aligned trailing windows rather than a data error — flagged, not reconciled, and immaterial to every affected verdict (all cleared the FCF-yield filter either way except Lasertec, addressed separately below).
- **Lasertec (6920.T)**: statistics-page FCF (TTM, ¥69.06B) is ~9% *lower* than the FY2025 (fiscal year ended June 2025) annual FCF (¥75.76B) — an unusual direction of divergence for a fast-growing business, worth a primary-source check if this name is ever revisited. FCF yield (1.81%) is the closer of Lasertec's two valuation misses; even the higher FY2025-based FCF wouldn't clear the >4% bar at this market cap, so the discrepancy doesn't change the FAIL verdict.

---

## Next steps

- **One `/new-position` candidate from this rotation: `/new-position GMO-PG` (3769.T)** — full Phase 02 valuation scoring with live pricing, and re-verify ROIC from a primary source per the flag above.
- Watchlist (no formal entry created by `/screen`; re-check on next JP rotation or a fresher annual print): **Nihon M&A Center Holdings (2127.T)** — Revenue 3yr CAGR the only blocker (6.75% vs. >8%), everything else comfortably clears, including an exceptional 87.58% ROIC and a cheap 9.49× EV/EBIT.
- This completes both rounds of the JP slice (2026-06-30 large/mega-cap pass + this deferred-names pass) — 31 total names quantitatively screened across the two rounds, 1 Qualified Quality List name found.
- Deferred from this round (not screened, structurally excluded): Pan Pacific International Holdings (7532.T) — thin-margin discount retail, same category as prior exclusions.
- **Process flag for the automation owner:** the scheduled Routine 4 prompt still references the deprecated EODHD `Path A` automation. Recommend updating the schedule's stored prompt text to match the current `screen.md`/`yfinance`-or-fallback process, so this doesn't need re-flagging every month.
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
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
- **pp (percentage points)** — A direct difference between two percentages, distinct from a "%" change.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring.
- **ROE** — Return on Equity — Net Income ÷ shareholder equity; how efficiently a company generates profit from shareholders' capital.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to never invent or estimate financial data — if a metric is missing, flag it and stop rather than infer it; also covers always fetching a live price before valuation work.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure.

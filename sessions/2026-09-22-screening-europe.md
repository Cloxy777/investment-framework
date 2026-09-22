# 2026-09-22 — SCREENING: Europe (EU), Round 5

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [EU](../framework/screening-coverage-log.md) (UK, Eurozone, Switzerland, Nordics), all sectors. Unattended scheduled run (no live user to ask questions of — Tuesday, informational/research-only per Routine 4).

Verified against the current [screening-coverage-log.md](../framework/screening-coverage-log.md) before starting: EU's "Last screened" (2026-08-29) was the single oldest date in the Rotation Matrix (NA-2 2026-09-05, JP 2026-09-01, NA-1 2026-09-08, APAC-EX-JP 2026-09-12, EM 2026-09-15 all more recent) — EU is the correct slice for this round.

## ⚠️ Scheduled-prompt discrepancy flagged (same pattern as every rotation session since 2026-06-30)

This run's stored scheduled-task prompt describes a **"Monthly Universe Screening Slice"** using an **`EODHD_API_KEY`** ("set in this environment") for full automation ("Path A") per `.claude/commands/screen.md`. Both are stale:

- [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md) removed EODHD from every framework/automation doc back in June. `.claude/commands/screen.md` has no EODHD path today — Step 0's only automated option for an unattended run is the quality-factor-ETF-holdings fallback (or, as used by every EU round to date, structural-triage domain knowledge as its practical equivalent).
- The authoritative [automation-schedule.md](../framework/automation-schedule.md) documents this as **Routine 4 — Twice-Weekly Universe Screening Slice** (Tuesday + Saturday, 14:00 UTC), not monthly.
- A fresh `EODHD_API_KEY` is indeed present in this environment (confirmed via `env`), but no current framework doc references or uses it — it was not called this session.

Followed the current, authoritative `screen.md` / `automation-schedule.md` process instead, exactly as every EU/NA/JP/EM/APAC-EX-JP session has done since 2026-06-30.

This round does **not** re-run the 37 names already covered across the [2026-06-19](2026-06-19-screening-europe.md), [2026-07-18](2026-07-18-screening-europe.md), [2026-08-08](2026-08-08-screening-europe.md), and [2026-08-29](2026-08-29-screening-europe.md) EU sessions — round 4 exhausted the deferred-candidate and near-miss backlog, so this round builds a **genuinely fresh 14-name candidate pool** from domain knowledge, deliberately avoiding sectors/countries already heavily covered (French/Swiss luxury, Nordic industrials, Dutch/German enterprise software, UK data/exchanges).

---

## Step 0 — Starting universe

No user available in this unattended run — per `screen.md` Step 0's documented exception, skipped straight to the ETF-holdings-fallback-equivalent used by every EU session to date: structural-triage domain knowledge.

**Data source:** `yfinance` re-tested at session start — not installed in this environment (`ModuleNotFoundError: No module named 'yfinance'`); `stockanalysis.com` (HTTP 301, reachable) used instead via WebFetch, exactly as every EU round since 07-07 has done. Delegated across **4 parallel research agents** (3–4 tickers each) to keep this round's wall-clock/token cost bounded, same pattern as 08-08/08-29.

**Candidate pool (14 names, none previously tested on this slice):**

| Ticker | Company | Country | Sector |
|---|---|---|---|
| GIVN.SW | Givaudan | Switzerland | Flavors & fragrances |
| SY1.DE | Symrise | Germany | Flavors & fragrances / specialty ingredients |
| LISN.SW | Lindt & Sprüngli | Switzerland | Premium chocolate/confectionery |
| MONC.MI | Moncler | Italy | Luxury apparel |
| REC.MI | Recordati | Italy | Specialty pharmaceuticals (rare disease + primary care, diversified — not patent-cliff-concentrated) |
| BC.MI | Brunello Cucinelli | Italy | Luxury apparel (cashmere) |
| GNS.L | Genus plc | UK | Animal genetics (bovine/porcine breeding IP) |
| RSW.L | Renishaw | UK | Precision metrology/engineering instruments |
| JDG.L | Judges Scientific | UK | Scientific instruments (acquisitive roll-up) |
| SXS.L | Spectris | UK | Precision instrumentation/measurement |
| ITRK.L | Intertek Group | UK | Testing/inspection/certification |
| AUTO.L | Auto Trader Group | UK | Online automotive classifieds marketplace |
| SCT.L | Softcat | UK | IT infrastructure reseller/services |
| EPI-A.ST | Epiroc AB | Sweden | Mining/infrastructure equipment |

---

## Step 1 — Structural triage

None of the 14 hit a hard structural exclusion (banks, insurers, commodity cyclicals, regulated utilities, thin-margin volume retail, patent-cliff pharma, airlines, telecom, REITs):

| Ticker | Disposition | Reason |
|---|---|---|
| GIVN.SW | Tested | Asset-light specialty ingredients — no hard exclusion |
| SY1.DE | Tested | Same category as Givaudan |
| LISN.SW | Tested | Branded premium consumer goods, not commodity food — no hard exclusion |
| MONC.MI | Tested | Luxury apparel, same category as LVMH/Hermès/Richemont/Ferrari already tested |
| REC.MI | Tested | Diversified specialty pharma — not concentrated patent-cliff risk (no single blockbuster nearing exclusivity loss); kept structurally distinct from the "patent-cliff pharma" exclusion the same way Novo Nordisk was |
| BC.MI | Tested | Luxury apparel |
| GNS.L | Tested | IP-licensing-driven agri-genetics, asset-light — no hard exclusion |
| RSW.L | Tested | Precision instruments manufacturer — no hard exclusion |
| JDG.L | Tested | Scientific instruments — no hard exclusion |
| SXS.L | Tested | Precision instrumentation — no hard exclusion (flag: possible stale/take-private-related data, see Step 4) |
| ITRK.L | Tested | Testing/certification services, asset-light — same category as Bureau Veritas/SGS already tested (BVI.PA failed in round 2) |
| AUTO.L | Tested | Asset-light online marketplace, not thin-margin volume retail (it's a listings/SaaS-like model, not a retailer) |
| SCT.L | Tested | IT reseller — considered borderline vs. "thin-margin distribution" exclusion category, but not a volume-retail business (higher-margin value-added reseller model); tested rather than pre-excluded, quantitative gate is the actual arbiter here |
| EPI-A.ST | Tested | Capital-goods manufacturer, not a regulated utility or commodity producer itself (sells equipment *to* miners) — no hard exclusion |

---

## Step 2 — Full Phase 01 quantitative gate

Filters: Gross margin >40% · Net margin >12% · ROIC >15% (ROE proxy acceptable if noted) · Revenue growth >8% (3yr CAGR) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x.

**Period basis:** margins, ROIC, and revenue CAGR use the latest completed fiscal year (varies by company's own FYE — noted per row); Net Debt/EBITDA, FCF yield, and EV/EBIT use the current/live-price (TTM, as of 2026-09-22) column, per every prior round's convention.

### Group A — Luxury / specialty ingredients

| Ticker | FY basis | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA | FCF yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| GIVN.SW | FY2025 | 43.52% ✅ | 14.33% ✅ | 13.34% ❌ | 1.64% ❌ | ✅ | 2.91× ❌ | 3.78% ❌ | 26.79× ❌ | **FAIL — 3/8** |
| SY1.DE | FY2025 | 37.63% ❌ | 5.06% ❌ | 6.92% ❌ | 2.20% ❌ | ✅ | 2.52× ❌ (marginal) | 5.61% ✅ | 30.85× ❌ | **FAIL — 2/8** |
| LISN.SW | FY2025 | 62.78% ✅ | 12.22% ✅ (marginal) | 13.36% ❌ | 5.98% ❌ | ✅ | 1.22× ✅ | 3.86% ❌ (marginal) | 22.01× ❌ | **FAIL — 4/8** |
| MONC.MI | FY2025 | 78.10% ✅ | 20.01% ✅ | 19.03% ✅ | **6.36% ❌** | ✅ | ~0.10× ✅ (net-cash/net-debt crossover, see Step 4) | 6.76% ✅ | 12.87× ✅ | **FAIL — Revenue CAGR only (7/8)** — tight near-miss, 1.64pp short |

### Group B — Italy pharma/luxury + UK animal genetics

| Ticker | FY basis | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA | FCF yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| REC.MI | FY2025 | 70.82% ✅ | 16.94% ✅ | **14.95% ❌** (current/TTM basis 15.35% ✅ — see Step 4) | 12.21% ✅ | ✅ | 1.90× ✅ | 5.54% ✅ | 15.46× ✅ | **FAIL — ROIC only (7/8)** — tightest near-miss of the round, 0.05pp short on FY basis |
| BC.MI | FY2025 | 54.06% ✅ | 9.59% ❌ | 11.86% ❌ | 15.25% ✅ | ✅ | 3.43× ❌ (see Step 4 data-gap flag) | 3.07% ❌ | 26.10× ❌ | **FAIL — 3/8** |
| GNS.L | FY2026 | 40.19% ✅ (FY2025 basis, see Step 4 gap) | 43.35% ⚠️ (likely one-off-inflated, see Step 4) | 9.64% ❌ | **−1.55% ❌** | ✅ | 0.62× ✅ | 4.36% ✅ | 12.94× ✅ | **FAIL — ROIC + Revenue CAGR at minimum (Net M unreliable)** |

### Group C — UK instruments/testing

| Ticker | FY basis | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA | FCF yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| RSW.L | FY2025 | 46.40% ✅ | 11.75% ❌ (marginal) | 11.46% ❌ | 2.04% ❌ | ✅ | −1.85× ✅ (net cash) | 1.57% ❌ | 36.75× ❌ | **FAIL — 3/8** |
| JDG.L | FY2025 | 68.31% ✅ | 3.77% ❌ | 6.16% ❌ | 8.81% ✅ | ✅ | 1.57× ✅ | 9.57% ✅ | 24.08× ❌ | **FAIL — 5/8** |
| SXS.L | FY2024 | 55.12% ✅ | 17.99% ✅ | 4.81% ❌ | 3.76% ❌ | ✅ | ~3.34× ❌ (derived, see Step 4) | 2.03% ❌ | 42.75× ❌ | **FAIL — 3/8** (data-currency flag, Step 4) |
| ITRK.L | FY2025 | 56.91% ✅ | 10.01% ❌ (marginal) | 18.37% ✅ | 2.44% ❌ | ✅ | 1.86× ✅ | 4.96% ✅ | 16.93× ✅ | **FAIL — Net M + Revenue CAGR (6/8)** |

### Group D — UK tech/services + Nordic industrial

| Ticker | FY basis | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA | FCF yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| AUTO.L | FY2026 | 79.13% ✅ | 47.08% ✅ | 50.76% ✅ | **7.67% ❌** | ✅ | 0.48× ✅ | 7.58% ✅ | 10.42× ✅ | **FAIL — Revenue CAGR only (7/8)** — tightest margin-miss of the round, 0.33pp short |
| SCT.L | FY2025 | 33.89% ❌ | 9.12% ❌ | 78.71% ✅ | 10.61% ✅ ⚠️ (revenue-recognition-change flag, see Step 4) | ✅ | −0.82× ✅ (net cash) | 4.94% ✅ | 17.86× ✅ | **FAIL — Gross M + Net M (6/8)** — structurally thin-margin reseller economics |
| EPI-A.ST | FY2025 | 37.06% ❌ | 13.88% ✅ | 17.12% ✅ | 7.66% ❌ (marginal) | ✅ | 0.81× ✅ | 2.87% ❌ | 24.15× ❌ | **FAIL — 4/8** |

---

## ✅ Qualified Quality List — 0 new names this round

**None of the 14 candidates tested clear all 8 Phase 01 filters.** The EU slice's qualified list stays at **5 names, unchanged**: Experian (EXPN.L), Deutsche Börse (DB1.DE), Novo Nordisk (NOVO-B.CO), Partners Group (PGHN.SW), Rightmove (RMV.L).

This round did turn up the **two tightest single-filter revenue-growth misses recorded on this slice to date** — Auto Trader Group (0.33pp short, 7.67% vs. 8%) and Moncler (1.64pp short) — plus **Recordati's ROIC miss (14.95% vs. 15%, 0.05pp short on the FY-basis convention this framework uses, though its current/TTM ROIC of 15.35% would clear)**, arguably the single tightest miss of any kind found on the EU slice across all 5 rounds. All three are flagged for a priority refresh on the next EU rotation.

### Step 3 — Qualitative pass

Not applicable this round — no candidate cleared the Step 2 quantitative gate.

---

## Step 4 — Data gaps and inconsistencies flagged (per CLAUDE.md Rule 0 — none estimated)

- **Recordati ROIC basis dependency**: FY2025 (14.95%) fails the >15% bar by 0.05 percentage points; the current/TTM figure (15.35%) would pass. This round's convention (and every prior round's) uses the latest-completed-FY basis for ROIC, so the verdict is reported as FAIL — but flagged as the tightest, most basis-sensitive miss found on this slice to date, worth an immediate re-check on the next EU rotation rather than waiting a full cycle.
- **Moncler Net Debt/EBITDA**: the ratios page reports current Net Debt/EBITDA as 0.10×, while the statistics page separately shows a small net-cash position (−€93.4M). Moncler has run net cash every year FY2021–FY2024 and is right at the net-debt/net-cash crossover currently — reported as "~0.10×, effectively net-cash-to-slightly-net-debt" rather than picking one page's figure as authoritative. Doesn't change the verdict (this filter already passes either way).
- **Symrise net margin**: FY2025 net margin (5.06%) is roughly half FY2024's (9.57%) on essentially flat revenue — a real, sourced figure (not a data error, confirmed against both the income-statement and ratios pages), but the underlying driver (likely a below-the-line impairment or one-off) isn't visible from stockanalysis.com's pages. Reported as-is; doesn't change the verdict (Symrise fails multiple other filters regardless).
- **Lindt & Sprüngli FCF swing**: FY2025 FCF (CHF 248.9M) dropped sharply from FY2024 (CHF 913.0M), tracking a similar drop in operating cash flow — flagged as a real, likely cocoa-cost/working-capital-driven swing rather than a data inconsistency; still positive all 3 years so the FCF-3yr-positive filter still passes.
- **Brunello Cucinelli Net Debt/EBITDA conflict**: the ratios page shows two different figures for what should be the same metric — a "Net Debt/EBITDA" row (3.43×) and a "Debt/EBITDA" row (2.79×) — while the statistics page separately labels a figure "Net Debt/EBITDA: 2.79", identical to the ratios page's *gross*-debt figure, suggesting a mislabel on the statistics page. Reported using the ratios page's own labeled Net Debt/EBITDA figure (3.43×) as the more internally consistent source; doesn't change the verdict either way (BC fails multiple other filters regardless).
- **Genus plc FY2026 gross margin — unresolved data gap**: stockanalysis.com's FY2026 financials column shows Gross Profit exactly equal to Revenue (an unpopulated Cost-of-Revenue field, confirmed via a repeat fetch), not a genuine 100% gross margin. The FY2025 figure (40.19%) is reported as the last reliable gross-margin data point instead, flagged as a data gap rather than treated as a computed FY2026 number.
- **Genus plc FY2026 net margin — likely non-recurring, flagged not corrected**: net income jumped +1,378% YoY (£19.3M → £285.3M) while operating income grew a normal ~17% (£68.3M → £79.9M), strongly suggesting a large one-off (e.g. a disposal gain) below the operating line. Reported as-is (43.35%) per Rule 0 rather than adjusted or excluded, but flagged as unreliable for judging recurring earnings quality; ROIC (EBIT-based, 9.64%) is far less distorted and is the metric the verdict relies on. Doesn't change the verdict — Genus fails on ROIC and Revenue CAGR regardless of how the net-margin figure is read.
- **Spectris data-currency flag**: the statistics page is stamped "As of: December 3, 2025" and the balance-sheet TTM column "Jun 30, 2025" — both roughly 9 months stale relative to today (2026-09-22), unlike every other name in this round's pool which pulled current-dated figures. Spectris was the subject of a take-private bid in 2025; **not independently confirmed this session whether the stock has since delisted or is still publicly trading** — flagged as a genuine open question rather than assumed either way, and its Net Debt/EBITDA (~3.34×) was itself derived (EV ÷ EV/EBITDA, back-solved) rather than a directly reported line item, adding a second layer of uncertainty. Does not change the verdict (Spectris fails on ROIC, revenue CAGR, and EV/EBIT regardless), but this name should not be re-tested on a future rotation until its current listing status is confirmed.
- **Intertek "Net Cash" sign convention**: the statistics page labels a balance-sheet row "Net Cash" but reports it as a *negative* number (−£1.46B TTM), which actually denotes a net-debt position of ~£1.46B, not net cash — cross-checked against EV − market cap (≈£1.51B, consistent) and against the directly reported Net Debt/EBITDA (1.86×, which would be nonsensical for a true net-cash company). Reported as net debt (positive 1.86×) in the table above; flagging the sign-convention trap for any future ITRK re-pull.
- **Softcat revenue-recognition discontinuity**: revenue moved −8.59% (FY23), −2.30% (FY24), then +51.50% (FY25) — an unusually volatile pattern for a steady IT reseller, most likely an IFRS 15 gross-vs-net revenue-recognition presentation change rather than genuine demand swings (confirmed consistent across two independently fetched pages, so not a fetch error). The Revenue-3yr-CAGR figure (10.61% ✅) should be treated with caution and re-verified against Softcat's own annual report before being relied on in any future re-test — though it does not change this round's verdict, since Softcat fails on gross margin and net margin regardless.
- **URL pattern note for future EU sessions** (stockanalysis.com): the generic `/stocks/TICKER.EXCHANGE/` path 404'd for every UK/Italian/Swedish ticker this round; the working pattern is `/quote/{exchange-code}/{TICKER}/` — `lon` for LSE (not `lse`), `bit` for Borsa Italiana, `sto` for Stockholm (ticker written with a dot, e.g. `EPI.A`, dropping the `.ST` suffix), `swx` for SIX Swiss Exchange, `etr` for Xetra (consistent with the `etr`-not-`xetr` correction already noted from the 08-29 round).

---

## Step 5 — Coverage log updated

See [screening-coverage-log.md](../framework/screening-coverage-log.md) — EU row's "Last screened" bumped to 2026-09-22, "Qualified names found" unchanged at 5 total (no new names), and "Sources used" appended with this round's methodology summary.

---

## Next steps

- No new `/new-position` candidates from this round.
- **Priority re-check next EU rotation** (ranked closest-to-clearing): **Recordati** (ROIC only, 14.95% vs. 15% FY-basis — 0.05pp short, and its own current/TTM figure already clears — the single most basis-sensitive miss on this slice to date), **Auto Trader Group** (Revenue CAGR only, 7.67% vs. 8% — 0.33pp short), **Moncler** (Revenue CAGR only, 6.36% vs. 8% — 1.64pp short), **Intertek** (Net Margin + Revenue CAGR, 2-filter miss but both only moderately wide).
- **Spectris (SXS.L) listing-status flag**: possible take-private in progress based on stale stockanalysis.com data (~9 months old) — confirm whether it's still independently listed before including it in any future rotation pool.
- **Softcat's revenue-recognition discontinuity** and **Genus plc's FY2026 one-off-inflated net income** both need primary-source confirmation before either name is re-tested — neither changes this round's FAIL verdict, but both make the underlying trend data unreliable as reported.
- 14 new names now off the "not yet screened" list for this slice, all FAIL.
- Coverage log updated below. Per the rotation rule, the next-oldest slice after this update will be **NA-2 (North America, Financials/Healthcare/Industrials/Energy/Materials/Real Estate/Utilities, last screened 2026-09-05)** — confirm against the live coverage log at that time in case another slice has since aged further.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate.
- **EV/EBIT** — Enterprise Value ÷ EBIT; how expensive a company is relative to operating profit, independent of capital structure.
- **FCF** — Free Cash Flow.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value); higher is cheaper.
- **Gross Margin** — Gross Profit ÷ Revenue.
- **IFRS 15** — the international accounting standard governing how and when companies recognize revenue; a change in gross-vs-net presentation under it can make reported revenue jump or drop without any real change in the underlying business.
- **Net Debt/EBITDA** — leverage ratio; net debt ÷ EBITDA.
- **Net Margin** — Net Income ÷ Revenue.
- **ROE** — Return on Equity; Net Income ÷ shareholder equity.
- **ROIC** — Return on Invested Capital; a core quality signal in this framework.
- **Take-private** — a transaction in which a public company is bought out and delisted from public stock exchanges, typically by a private equity firm.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported results.

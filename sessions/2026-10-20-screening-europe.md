# 2026-10-20 — SCREENING: Europe (EU), Round 6

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [EU](../framework/screening-coverage-log.md) (UK, Eurozone, Switzerland, Nordics), all sectors. Unattended scheduled run (Routine 4, Tuesday; research-only).

**Slice selection:** EU's "Last screened" (2026-09-22) was the oldest in the Rotation Matrix (JP 09-26, NA-2 09-29, APAC-EX-JP 10-06, NA-1 10-10, EM 10-17).

## Scheduled-prompt discrepancy (same as every rotation session since 2026-06-30)

The stored prompt describes a "Monthly" run using `EODHD_API_KEY` for "Path A" full automation. Neither matches the repo: `screen.md` has no EODHD path (removed per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)), and Routine 4 is twice-weekly. The key *is* present, so I re-tested it: `/eod` works (HTTP 200) but `/fundamentals` returns **403 "Only EOD data allowed for free users"** — it cannot supply any quality-gate metric, so it was not used. I followed the current `screen.md`.

## Step 0 — Starting universe

Unattended → domain-knowledge structural-triage pool (the ETF-fallback equivalent used by every EU round). 12 fresh names, none in the 51 names covered by the 06-19 → 09-22 EU sessions (checked by grep).

**Data source:** `scripts.fetch_fundamentals` was attempted (REC.MI); dependencies installed, but Yahoo returned `YFRateLimitError` (429) on the cookie/crumb endpoint. Fell back to stockanalysis.com via WebFetch (4 parallel research agents, 3 tickers each; all statistics pages stamped 2026-10-20 except Craneware, which 404'd).

## Step 1 — Structural triage

No hard exclusions applied. Tested: Scout24, Belimo, Bachem, Rational, BESI, ASM International, Amadeus, Edenred, Bytes Technology, Craneware, Lifco, Oxford Instruments. (Edenred and Amadeus are float/network businesses, not volume retail — gate is the arbiter.)

## Step 2 — Phase 01 quantitative gate

Filters: Gross margin >40% · Net margin >12% · ROIC >15% · Rev 3yr CAGR >8% · FCF positive 3 yrs · ND/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x. Margins/ROIC/CAGR on latest completed FY; ND/EBITDA, FCF yield, EV/EBIT current (2026-10-20).

| Ticker | FY | Gross M | Net M | ROIC | Rev CAGR | FCF 3y | ND/EBITDA | FCF yld | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| **G24 Scout24** (EUR) | FY25 | 74.3% ✅ | 37.0% ✅ | 15.55% ✅ (0.55pp buffer) | 13.2% ✅ | ✅ | 1.78× ✅ | 4.90% ✅ | 17.82× ✅ | **PASS 8/8** |
| **AMS Amadeus** (EUR) | FY25 | 43.95% ✅ | 20.50% ✅ | 19.53% ✅ | 13.2% ✅ | ✅ | ~1.06× ✅ (derived) | 9.39% ✅ | 14.00× ✅ | **PASS 8/8** |
| **EDEN Edenred** (EUR) | FY25 | 43.78% ✅ | 19.07% ✅ | 18.06% ✅ | 12.0% ✅ | ✅ | 1.65× ✅ | 15.18% ✅ | 10.81× ✅ | **PASS 8/8 (formally; see flags)** |
| BEAN Belimo (CHF) | FY25 | 60.4% ✅ | 16.2% ✅ | 37.10% ✅ | 9.8% ✅ | ✅ | 0.10× ✅ | 0.98% ❌ | 36.21× ❌ | FAIL 6/8 (valuation only) |
| BYIT Bytes (GBP) | FY26 | 75.86% ✅ | 23.25% ✅ | data gap | 6.1% ❌ | ✅ | −0.99× ✅ | 5.95% ✅ | 14.97× ✅ | FAIL — Rev CAGR only (1.9pp); ROIC unreliable |
| LIFCO.B Lifco (SEK) | FY25 | 43.69% ✅ | 12.86% ✅ | 14.49% ❌ (current 15.03%) | 9.4% ✅ | ✅ | 1.48× ✅ | 3.20% ❌ | 29.01× ❌ | FAIL 5/8 |
| RAA Rational | FY25 | 59.0% ✅ | 20.2% ✅ | 61.50% ✅ | 7.24% ❌ | ✅ | −1.13× ✅ | 3.77% ❌ | 19.67× ✅ | FAIL 6/8 |
| ASM ASM Intl | FY25 | 51.8% ✅ | 22.8% ✅ | 25.09% ✅ | 9.59% ✅ | ✅ | −0.96× ✅ | 1.99% ❌ | 34.14× ❌ | FAIL 6/8 (valuation only) |
| BESI | FY25 | 63.3% ✅ | 22.3% ✅ | 38.52% ✅ | −6.5% ❌ | ✅ | −0.54× ✅ | 1.86% ❌ | 48.85× ❌ | FAIL 5/8 |
| OXIG Oxford Instr. | FY26 | 55.77% ✅ | 11.39% ❌ | 17.22% ✅ | −1.65% ❌ | ✅ | −0.76× ✅ | 3.17% ❌ | 20.89× ❌ | FAIL 4/8 |
| BANB Bachem (CHF) | FY25 | 28.7% ❌ | 21.4% ✅ | 11.43% ❌ | 9.3% ✅ | ❌ | 0.74× ✅ | −0.75% ❌ | 41.51× ❌ | FAIL 3/8 |
| CRW Craneware | — | DATA GAP | | | | | | | | Not scored — all stockanalysis.com URLs 404 |

## Step 3 — Qualitative pass (3 survivors, batches of 2 + 1)

Web-sourced by research agents; items they could not source are "not found" (not estimated).

- **Amadeus — PASS (with data-gap flag).** Margins = network scale/per-booking fees (est. 40–50% GDS share), with real cyclicality (COVID losses). Moat: two-sided airline/agency network. Capital allocation disciplined (FY25: €1.3bn buyback done, new €500m, ~0.9× leverage). Growth: guided high-single-digit revenue, low-double-digit EPS. Bear: travel shock, NDC bypass. Disruption: NDC/AI agents — unproven. To verify before scoring: FY20/21 losses, segment drivers, customer concentration.
- **Scout24 — FLAG.** #1 German property portal, ooEBITDA margin 62.5%, structural network-effect margin. Flags: (1) FY25 reported EPS +50.2% vs adjusted EPS +19.6% — the FY25 net-income jump is likely partly one-off, so the 37% net margin is inflated (still passes by a wide margin); (2) ROIC rose from ~11% (FY23/24) to 15.55% — driver not found, and Spain acquisition (~€153m for ~€11m EBITDA) will dilute it; (3) 1.78× ND/EBITDA (stockanalysis TTM) could not be reconciled with company-reported 0.99× at Q2 2026; (4) AI-agent disintermediation concern (analyst notes, shares at two-month low Sept 2026), antitrust blocked Austria deal. 2026 margin guided lower (≤61%).
- **Edenred — FLAG (serious).** Regulation is hitting the model: Brazil merchant-fee cap (guidance cut Nov 2025, stock fell to lowest since 2017), Italy 5% cap + abuse-of-dominance probe (Mar 2026), France scrutiny; CEO cited ~€230m regulatory shortfall. 2026 EBITDA guided −7% to −10%. The 15.18% FCF yield is **not sustainable free cash** — float/working-capital driven (FY25 FCF conversion 82% vs FY26 guide ≥35%; H1 2026 FCF negative). Net-debt definition (client cash) unverified; the agent found FY25 net debt ≈ €1.24bn / 0.9× versus the €1.76bn mid-2026 figure on stockanalysis. Treat the quant pass as formal only; ROIC was 10.02% in FY23.

## Step 4 — Data gaps (nothing estimated)

- yfinance 429-blocked this session; all figures stockanalysis.com-derived.
- Craneware: not scored (404; listing status unknown — check RNS before re-testing).
- Bytes: ROIC unusable (statistics page 1,485.75%; ROCE 82% as proxy only). Verdict unaffected (fails CAGR).
- Amadeus ND/EBITDA derived (statistics page lacks it); matches EV − market cap.
- Scout24/Edenred/Amadeus qualitative figures conflict across secondary sources (see above); verify from annual reports before `/new-position`.
- Bachem gross margin is definition-dependent (costs by function) — verdict still FAIL on FCF/ROIC/valuation.
- Lifco ROIC basis-sensitive (14.49% FY vs 15.03% current); Q3 report due 2026-10-23.

## ✅ Qualified Quality List — 3 new names (all pending `/new-position` verification)

1. **Amadeus (AMS.MC)** — cleanest (qual PASS).
2. **Scout24 (G24.DE)** — qual FLAG (one-off earnings, thin ROIC buffer, AI risk).
3. **Edenred (EDEN.PA)** — qual FLAG (regulatory earnings decline; FCF yield unreliable) — lowest priority.

EU qualified total: 5 → **8**.

Near-misses to re-check: Bytes (Rev CAGR 6.1%, ROIC data gap), Lifco (ROIC basis), Belimo/ASM (quality clears; valuation only), Rational (Rev CAGR 7.24% + FCF yield 3.77%).

## Step 5 — Coverage log updated

EU row: Last screened → 2026-10-20; qualified total 8; sources appended.

## Glossary

- **CAGR** — Compound Annual Growth Rate.
- **EBIT / EV/EBIT** — operating profit; enterprise value ÷ EBIT (lower = cheaper).
- **FCF / FCF yield** — free cash flow; FCF ÷ market cap.
- **Float** — client money (e.g. prepaid vouchers) a company holds and earns interest on before paying merchants.
- **GDS / NDC** — Global Distribution System (airline booking network); NDC is the airlines' direct-booking standard that can bypass it.
- **Net Debt/EBITDA** — leverage ratio.
- **ooEBITDA** — Scout24's "ordinary operating" EBITDA (excludes one-offs).
- **ROIC** — Return on Invested Capital.
- **Take-private / Moat** — see [glossary.md](../framework/glossary.md).

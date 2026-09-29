# 2026-09-29 — SCREENING: North America — NA-2 (Financials, Healthcare, Industrials, Energy, Materials, Real Estate/Utilities), Round 5

**Task type:** SCREENING (Phase 01), rotation slice [NA-2](../framework/screening-coverage-log.md). Picked by the rotation rule: oldest "Last screened" date was NA-2 (2026-09-05), ahead of NA-1 09-08, APAC-EX-JP 09-12, EM 09-15, EU 09-22, JP 09-26. Unattended scheduled run.

## 0. Methodology / source notes

- **EODHD (stored prompt's "Path A") tested and does not work.** `EODHD_API_KEY` is set, but `/fundamentals` and `/screener` return HTTP 403 "Only EOD data allowed for free users"; only `exchange-symbol-list` works, which gives no fundamentals. Consistent with [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md). No bulk-screener automation is therefore available; Step 0 used a hand-built structural-triage pool (same as every NA-2 round; the ETF-holdings fallback skews tech/consumer, i.e. NA-1's territory).
- **`yfinance` works again this session** (blocked by SSL connection-reset since 2026-07-07). `python -m scripts.fetch_fundamentals <TICKER>` ran for all 58 tickers (8 concurrent). Note: yfinance-derived figures differ from the stockanalysis.com figures used in prior rounds (e.g. AON Net Debt/EBITDA 2.38x here vs 2.51x on 09-05), so cross-round comparisons carry a source-change caveat.
- Gate per [valuation-scoring.md](../framework/valuation-scoring.md): Gross margin >40%, Net margin >12%, ROIC >15%, Rev 3yr CAGR >8%, FCF positive 3 yrs, Net Debt/EBITDA <2.5x, EV/EBIT <20x, FCF yield >4%.

## 1. Pool

58 tickers: 8 refreshes of prior near-misses (FDS, AON, CBOE, JKHY, MSA, CPAY, ITW, CME) + 50 tickers, mostly new to this slice. Deliberately included Energy (EOG, CNQ, CTRA, TPL), Materials (SHW, ECL, LIN, NEU, BCPC) and Real Estate-adjacent (CSGP) to address the standing coverage gaps.

**Tool errors (data gaps — not estimated, not tested):** ISRG (no "Net Income" row), ICLR (TTM pretax income ≤ 0, tax rate undefined), BCPC (NaN EBIT in TTM), CTRA/MMC (`marketCap` missing), PGR/EXPO (no "Gross Profit" row — PGR is an insurer, structurally excluded anyway).

## 2. Quantitative results — 4 clear all 8 filters

| Ticker | Business | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF+ 3yr | ND/EBITDA | EV/EBIT | FCF Yld | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| **AON** | Insurance brokerage | 48.57% | 22.27% | 18.57% | 11.25% | ✅ | **2.38x** (thin, 0.12x buffer) | 12.44x | 5.64% | **PASS** |
| **PAYX** | Payroll/HCM software & services | 74.29% | 27.03% | 23.70% | 9.16% | ✅ | 1.13x | 15.13x | 6.63% | **PASS** |
| **RMD** | Sleep-apnea/respiratory devices | 61.06% | 26.95% | 20.91% | 10.21% | ✅ | net cash | 16.45x | 5.10% | **PASS** |
| **TW** | Electronic fixed-income/derivatives trading | 68.52% | 40.66% | **15.66%** (thin, 0.66pp) | 19.97% | ✅ | net cash | 15.41x | 4.97% | **PASS** |

**Near-misses (≤2 filters failing):**

| Ticker | Misses |
|---|---|
| FDS | Rev CAGR 7.98% (vs 8%) — unchanged, 0.02pp short |
| MSA | Rev CAGR 7.06% |
| JKHY | Rev CAGR 6.99% |
| CBOE | Rev CAGR 6.00% |
| VRSK | Rev CAGR 7.16% (new) |
| CME | ROIC 13.75% |
| BRO | ROIC 7.64% (new) |
| PODD | FCF yield 2.91% (new) |
| ROL | EV/EBIT 21.46x (new) |
| MCO | EV/EBIT 22.25x + FCF yield 3.77% |
| ITW | Rev CAGR 0.23% + FCF yield 3.81% |
| CPAY | ROIC 10.45% + ND/EBITDA 2.71x |
| ICE | ROIC 9.72% + ND/EBITDA 2.80x |
| ROP | ROIC 9.72% + ND/EBITDA 2.78x |
| TRI | ROIC 13.35% + Rev CAGR 4.10% |
| AOS | Gross margin 38.59% + Rev CAGR 0.67% |

All other tickers fail 3+ filters (e.g. MSCI ND/EBITDA 2.90x + EV/EBIT 24.7x; IDXX/CTAS/HEI valuation; WAT/TECH/WST/COO/MTD multiple misses; Energy names EOG/CNQ fail growth and CNQ gross margin — no Energy name qualifies).

## 3. Qualitative pass (5 questions + disruption vector)

Done from domain knowledge with no new numeric claims; items needing live verification are flagged. Run as one pass (4 names, not fanned out to subagents).

**AON** — (1) Margins: scale + relationships in commercial brokerage, fee-based, low capital need. (2) Compete: global placement network and data are hard to replicate; only Marsh McLennan/WTW/Gallagher are peers. (3) Capital: heavy M&A (NFP acquisition) financed with debt; buybacks; leverage is the watch item. (4) Growth: organic ~mid-to-high single digit, pricing, plus M&A. (5) Bear: ND/EBITDA buffer of 0.12x is fragile and yfinance vs stockanalysis differ (2.38x vs 2.51x on 09-05) — **it may not truly clear; re-verify before any action**; softening P&C pricing cycle; FCF/NI fell to 83% TTM from 106–124%. (6) Disruption: AI/insurtech disintermediation is a low but real risk. **Flag: fragile pass.**

**PAYX** — (1) Sticky payroll/HR with float income; pricing power on small-business base. (2) Compete: switching costs, compliance breadth; ADP, Workday, Rippling, Gusto are alternatives. (3) Capital: dividend-focused; large debt-funded Paycor acquisition (2025) — Rev CAGR likely includes inorganic growth, unverified. (4) Growth: Paycor integration, HCM cross-sell, pricing. (5) Bear: float income falls with rates; small-business employment cycle; integration risk. (6) Disruption: AI/agentic HR-payroll tools and low-cost SMB entrants. **Flag: separate organic from acquired growth before scoring.**

**RMD** — (1) Brand/installed base, recurring mask/supply revenue at high margin. (2) Compete: regulatory clearances, sleep-clinic channel; Philips exit/recall helped. (3) Capital: net cash, dividends and buybacks, modest M&A. (4) Growth: under-diagnosis of sleep apnea, international, software/digital. (5) Bear: GLP-1 weight-loss drugs reducing apnea prevalence/severity (unresolved debate); reimbursement/tariff pressure; Philips' return. (6) Disruption: GLP-1 and oral/implant alternatives are the real vector. **Flag: GLP-1 thesis risk is the key qualitative question.**

**TW** — (1) Network effects in dealer-to-client electronic fixed income; high incremental margins. (2) Compete: liquidity network is hard to replicate; MarketAxess, Bloomberg, Trumid, and big-bank venues compete. (3) Capital: net cash, acquisitions (ICD, r8fin), buybacks. (4) Growth: electronification of credit/rates, US Treasuries, ETFs, international, data. (5) Bear: revenue is volume-linked and cyclical; ROIC (15.66%) sits just above the bar, dragged by acquired goodwill; 19.97% CAGR includes the ICD acquisition (inorganic share unverified). (6) Disruption: all-to-all/anonymous trading, Treasury central clearing rule changes, and bank/venue consolidation. **Flag: ROIC and CAGR both need cross-source verification.**

## 4. Data gaps (Step 4)

- ISRG, ICLR, BCPC, CTRA, MMC, PGR, EXPO: yfinance field gaps — untested, not estimated. ISRG, ICLR, MMC are worthwhile follow-ups via stockanalysis.com.
- All four passes rest on a single source (yfinance-derived); none was cross-checked against stockanalysis.com this run. Rev CAGR for PAYX and TW likely includes acquired revenue (unverified). CSGP shows FCF+ = False (fails outright).
- Standing: EQIX/DLR REIT framework not built; fundamentals-tool ROIC is a recomputation and differs from stockanalysis.com's ROIC (e.g. CPAY 10.4% vs 14.55%, FDS 17.1% vs 18.4%), so ROIC verdicts near 15% are source-sensitive.

## 5. Coverage log update

NA-2 row: Last screened → 2026-09-29; qualified total 2 → 6 candidates (DOCS, MORN + AON, PAYX, RMD, TW, all pending `/new-position` verification); near-miss list refreshed; source: yfinance via `fetch_fundamentals` (EODHD 403 on free plan).

## Glossary

- **CAGR** — Compound Annual Growth Rate: smoothed yearly growth between two points.
- **EV/EBIT** — Enterprise Value ÷ operating profit; lower means cheaper.
- **FCF / FCF Yield** — free cash flow (cash left after running the business); yield = FCF ÷ market cap.
- **Gross / Net Margin** — share of revenue left after direct costs / after all expenses.
- **Net Debt/EBITDA** — leverage: debt minus cash relative to earnings before interest, taxes, depreciation, amortization.
- **NOPAT** — operating profit after tax; the numerator for ROIC.
- **Phase 01** — this framework's quality-gate screening stage.
- **ROIC** — Return on Invested Capital: profit earned per dollar of capital deployed.
- **TTM** — trailing twelve months.
- **GLP-1** — class of weight-loss/diabetes drugs (semaglutide etc.); a bear-case for sleep-apnea devices.
- **Float** — client funds a payroll firm holds briefly and earns interest on.

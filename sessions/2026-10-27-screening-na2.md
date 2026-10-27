# 2026-10-27 — SCREENING: North America — NA-2, Round 6 (small data-gap run)

**Task type:** SCREENING (Phase 01), slice [NA-2](../framework/screening-coverage-log.md). Picked by the rotation rule: oldest "Last screened" date (2026-09-29; next oldest APAC-EX-JP 10-06). Unattended scheduled run.

## 0. Methodology / source notes

- **EODHD (Path A) not usable:** `EODHD_API_KEY` is set but `/fundamentals` returns HTTP 403 on the free plan (same as 09-29/10-10/10-17/10-20/10-24; see [decision](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)). No bulk screener is available, so Step 0 used a hand-built pool.
- **yfinance rate-limited:** `scripts.fetch_fundamentals` fails with `YFRateLimitError` (429) on the crumb endpoint, so figures come from stockanalysis.com (WebFetch of ratios + financials pages). Not directly comparable to the yfinance-based 09-29 round.
- **Pool = the 6 names left untested on 09-29 for tool/data gaps** (ISRG, ICLR, BCPC, CTRA, MMC, EXPO). Scope is deliberately small; no full-slice refresh was attempted.
- Gate: Gross margin >40%, Net margin >12%, ROIC >15%, Rev 3yr CAGR >8% (FY2022→FY2025), FCF positive 3 yrs, ND/EBITDA <2.5x, EV/EBIT <20x, FCF yield >4%.

## 1. Results — 0 of 6 qualify

| Ticker | Gross M | Net M | ROIC | Rev 3yr CAGR | ND/EBITDA | EV/EBIT | FCF Yld | Verdict |
|---|---|---|---|---|---|---|---|---|
| ISRG | not shown (GP/Rev FY25 66.0%) | 28.4% | 23.97% | 17.4% | net cash | **41.55x** | **2.30%** | FAIL (2: valuation) |
| MRSH (ex-MMC) | 43.6% | 15.4% | **14.96%** (FY25: 15.77%) | 9.2% | **2.60x** (FY25: 2.40x) | 16.22x | 4.49% | **FAIL, near-miss (2, both marginal)** |
| EXPO | **36.3%** | 19.8% | 30.32% | **4.98%** | 0.10x | **28.61x** | **2.99%** | FAIL (4) |
| ICLR | 26.4% | **2.6%** | **0.67%** | **2.2%** | **4.96x** | **66.28x** | 7.17% | FAIL (5+) |
| BCPC | **35.7%** | 14.9% | **12.67%** | **3.2%** | 0.27x | **23.85x** | **3.30%** | FAIL (5) |
| CTRA | — | — | — | — | — | — | — | **Delisted 2026-05-07 (merged into DVN)** — remove from universe |

Calculations (FY, $M): ISRG CAGR (10,065/6,222)^(1/3)−1 = 17.4%; net margin 2,856/10,065; MRSH CAGR (26,981/20,720)^(1/3)−1 = 9.2%, gross 11,772/26,981 = 43.6%, net 4,160/26,981 = 15.4%, FCF positive FY22–25 (2,995 / 3,842 / 3,986 / 5,001); EXPO CAGR (536.76/463.82)^(1/3)−1 = 4.98%, gross 194.77/536.76; ICLR CAGR (8,251/7,741)^(1/3)−1 = 2.2%, net 214/8,251; BCPC CAGR (1,037/942.36)^(1/3)−1 = 3.2%, gross 370.63/1,037.

**Data gaps (not estimated):** ISRG gross/net margin not shown on the ratios page (derived above from the financials page); ISRG/EXPO/ICLR/BCPC FCF history taken from stockanalysis.com only, not cross-checked.

## 2. Qualitative pass

No names cleared the quantitative gate, so no qualitative pass was run. **MRSH** is the one to watch: insurance broker (same business model as AON), fails ROIC by 0.04pp and leverage by 0.10x on the current basis but clears both on FY2025; re-test after next earnings.

## 3. Outcome

NA-2 "Last screened" → 2026-10-27; qualified total unchanged at 6 (DOCS, MORN, AON, PAYX, RMD, TW — not re-tested, still pending `/new-position`). **0 new qualified names.**

## Glossary

- **CAGR** — Compound Annual Growth Rate: smoothed yearly growth between two points.
- **EV/EBIT** — Enterprise Value ÷ operating profit; lower means cheaper.
- **FCF / FCF Yield** — free cash flow (cash left after running the business); yield = FCF ÷ market cap.
- **Gross / Net Margin** — share of revenue left after direct costs / after all expenses.
- **Net Debt/EBITDA** — leverage: debt minus cash relative to pre-interest/tax/depreciation earnings.
- **Phase 01** — this framework's quality-gate screening stage.
- **ROIC** — Return on Invested Capital: profit earned per dollar of capital deployed.
- **TTM** — trailing twelve months.
- **Rate limit (429)** — the data provider temporarily refusing requests for being too frequent.

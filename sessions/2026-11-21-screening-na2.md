# 2026-11-21 — SCREENING: North America — NA-2, Round 7 (fresh 18-name pool)

**Task type:** SCREENING (Phase 01), slice [NA-2](../framework/screening-coverage-log.md). Picked by the rotation rule: oldest "Last screened" date (2026-10-27; next oldest NA-1 11-03). Unattended scheduled run (monthly routine).

## 0. Methodology / source notes

- **EODHD (Path A) not usable:** `EODHD_API_KEY` is set but `/fundamentals` returns HTTP 403 on the free plan (unchanged since 09-29; see [decision](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)). No bulk screener, so Step 0 used a hand-built pool (screener access unavailable in an unattended session).
- **yfinance reachable** after `pip install yfinance pandas` in-session; `python3 -m scripts.fetch_fundamentals <T> --json` run per ticker. Figures are yfinance-derived (TTM; ROIC on the script's NOPAT/invested-capital basis), not directly comparable to the stockanalysis.com rounds.
- **Pool (18, none previously tested on NA-2):** BR, ERIE, WRB, NDSN, TT, POOL, LII, ZTS, A, EW, ALGN, RSG, EXPD, AMT, SBAC, HLI, WDFC, RLI — asset-light Financials/Healthcare/Industrials plus Real Estate (towers), Materials-adjacent (WDFC).
- **Structural triage:** none eliminated up front (script output used as the gate); AMT/SBAC (REITs, leverage-heavy) and EXPD/RSG (thin-margin logistics/waste) were expected fails and confirmed.
- Gate: Gross margin >40%, Net margin >12%, ROIC >15%, Rev 3yr CAGR >8%, FCF positive 3 yrs, ND/EBITDA <2.5x, EV/EBIT <20x, FCF yield >4%.

## 1. Results — 0 of 15 scored qualify

| Ticker | Gross M | Net M | ROIC | Rev CAGR | FCF 3y+ | ND/EBITDA | EV/EBIT | FCF Yld | Misses |
|---|---|---|---|---|---|---|---|---|---|
| ZTS | 71.35 | 26.15 | 21.65 | **5.42** | yes | 1.67 | 11.88 | 7.09 | **1 (Rev CAGR)** |
| HLI | **38.49** | 15.78 | 18.24 | 13.10 | yes | -1.13 | 15.35 | 4.38 | **1 (Gross margin)** |
| TT | **34.99** | 13.56 | 25.82 | 10.06 | yes | 0.63 | **21.14** | 4.51 | 2 |
| BR | **31.52** | 13.95 | 18.75 | **7.25** | yes | 1.59 | 16.39 | 6.32 | 2 |
| LII | **33.10** | 14.12 | 33.16 | **3.26** | yes | 1.09 | 12.80 | 7.30 | 2 |
| SBAC | 75.66 | 34.54 | 17.62 | **2.25** | yes | **6.93** | 19.85 | 5.81 | 2 |
| ALGN | 69.14 | **11.83** | **13.52** | **2.61** | yes | -1.02 | 13.86 | 5.51 | 3 |
| WDFC | 55.31 | **11.97** | 23.53 | 8.59 | yes | 0.13 | **27.08** | **3.33** | 3 |
| POOL | **29.42** | **7.27** | 18.17 | **-5.05** | yes | 1.72 | 15.40 | 5.94 | 3 |
| NDSN | 55.29 | 18.63 | **12.50** | **2.53** | yes | 1.97 | **24.59** | 4.23 | 3 |
| A | 53.83 | 19.53 | 15.18 | **0.48** | yes | 0.75 | **28.59** | **2.64** | 3 |
| RSG | 42.01 | 12.92 | **10.72** | **7.08** | yes | **2.51** | **27.54** | **3.41** | 5 |
| AMT | 73.52 | 30.10 | **11.28** | **3.34** | yes | **5.05** | **25.48** | 4.64 | 4 |
| EXPD | **12.90** | **7.86** | 43.16 | **-13.45** | yes | -0.52 | 18.16 | **3.73** | 4 |

(Bold = fails that filter. Values straight from `fetch_fundamentals --json`; no hand-estimated inputs.)

**Data gaps (unscored, not estimated):** ERIE (no TTM EBIT row), WRB and RLI (no Gross Profit row — insurers), EW (NaN in TTM Pretax Income). Insurers report no gross profit, so the gross-margin filter is structurally not computable for them — flag for a possible framework note, not resolved here.

## 2. Qualitative pass

No names cleared the quantitative gate, so no qualitative pass was run. Watch items: **ZTS** (animal-health leader; cheap at 11.9x EV/EBIT, only the growth filter fails — recent growth has slowed); **HLI** (advisory/M&A fee business; "gross margin" is not a natural metric, so the 38.5% miss is partly definitional, and revenue is cyclical with deal markets).

## 3. Outcome

NA-2 "Last screened" → 2026-11-21; qualified total unchanged at 6 (DOCS, MORN, AON, PAYX, RMD, TW — not re-tested, still pending `/new-position`). **0 new qualified names.**

## Glossary

- **CAGR** — Compound Annual Growth Rate: smoothed yearly growth between two points.
- **EV/EBIT** — Enterprise Value ÷ operating profit; lower means cheaper.
- **FCF / FCF Yield** — free cash flow (cash left after running the business); yield = FCF ÷ market cap.
- **Gross / Net Margin** — share of revenue left after direct costs / after all expenses.
- **Net Debt/EBITDA** — leverage: debt minus cash relative to pre-interest/tax/depreciation earnings.
- **Phase 01** — this framework's quality-gate screening stage.
- **ROIC** — Return on Invested Capital: profit earned per dollar of capital deployed.
- **TTM** — trailing twelve months.
- **REIT** — real-estate investment trust; typically carries heavy debt.

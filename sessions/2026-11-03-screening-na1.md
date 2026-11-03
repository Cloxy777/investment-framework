# 2026-11-03 — SCREENING: North America — NA-1 (Tech, Communication Services, Consumer Discretionary)

**Task type:** SCREENING (Phase 01), slice [NA-1](../framework/screening-coverage-log.md). Picked by rotation: NA-1's "Last screened" (2026-10-10) was the oldest on the matrix (NA-2 10-27, EU 10-20, JP 10-24, APAC-EX-JP 10-31, EM 10-17). Unattended scheduled run.

## 0. Methodology
- **Stale-prompt note:** the prompt says "monthly" and "EODHD Path A". `screen.md` has no EODHD path (removed 2026-06-19, [decision](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)). Key re-tested: `/fundamentals` returns **403** (free plan); only `/eod` prices work. Not used for screening.
- **Universe:** unattended → ETF-holdings fallback (MOAT/QUAL/QGRW); approximate, misses small/mid-caps outside those ETFs. ETF composition not re-pulled; the 24-name post-triage pool from 2026-09-08/10-10 was reused (limitation).
- **Data:** `scripts.fetch_fundamentals`/yfinance fails with `YFRateLimitError` 429 (pandas/yfinance also had to be installed). Direct curl to stockanalysis.com is 403, but WebFetch works. **Partial refresh**: only the names that were single-filter near-misses on 10-10 and could plausibly flip were re-fetched (ADP, CPRT, CRM). GOOGL and ABNB were **not** refreshed (their misses were FCF yield 1.24% / EV/EBIT 30.3x; price-driven change large enough to flip is implausible but unverified). The other 19 pool names were **not refreshed** — their 10-10 results stand, flagged as stale, not estimated (Rule 0).

## 1. Refresh results (stockanalysis.com "statistics", 2026-11-03)
| Ticker | GM | NM | ROIC | FCF yld | EV/EBIT | Revenue 3yr CAGR | Status |
|---|---|---|---|---|---|---|---|
| ADP | 48.83 | 20.33 | 62.49 | 4.45 | **20.16 ❌** | 6.81 ❌ (10-10, not re-derived) | **2 misses** (EV/EBIT just above 20; was 17.6x on yfinance basis — source difference) |
| CPRT | 45.29 | 31.81 | 28.38 | 4.28 | 15.24 | 6.43 ❌ (FY2023→FY2026, unchanged) | **1 miss** (CAGR −1.57pp) |
| CRM | 77.28 | 21.99 | **10.96 ❌** | 8.14 | **22.96 ❌** | 9.82 (10-10) | **2 misses** (stockanalysis basis; yfinance basis was ROIC-only on 10-10) |

Net debt/EBITDA is not shown by stockanalysis.com (Debt/EBITDA: ADP 0.83, CPRT 0.05, CRM 3.14 — CRM's gross-debt figure is not a net-debt reading; unverified).

## ✅ Qualified Quality List — **0 names** (unchanged)
No name clears all 8 filters on the data obtained. CPRT remains the closest (growth only). Nothing advanced to the qualitative pass (Step 3 not run — no quantitative passers).

## 2. Data gaps
- yfinance rate-limited; 21 of 24 pool names not refreshed this run. GOOGL (TTM net margin 54.8% suspected one-off) and ABNB not re-fetched.
- ADP/CRM figures differ materially between yfinance and stockanalysis.com bases (EV/EBIT, ROIC) — not directly comparable to the 10-10 round.
- Net debt/EBITDA unavailable on stockanalysis.com page; Revenue CAGR not re-derived for ADP/CRM.

## 3. Coverage log
NA-1 row: Last screened 2026-11-03; qualified names 0 (unchanged); sources appended.

## Glossary
- **CAGR** — compound annual growth rate: smoothed yearly growth between two points.
- **EV/EBIT** — enterprise value ÷ operating profit; lower = cheaper.
- **FCF yield** — free cash flow ÷ market value.
- **Gross / Net margin** — share of revenue left after direct costs / after all expenses.
- **Net Debt/EBITDA** — leverage gauge; negative means net cash.
- **ROIC** — return on invested capital.
- **Phase 01 / Qualified Quality List** — the framework's quality-gate stage and its list of passers.
- **Rotation Matrix** — [screening-coverage-log.md](../framework/screening-coverage-log.md), which slice was screened when.
- **TTM** — trailing twelve months.

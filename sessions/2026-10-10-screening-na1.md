# 2026-10-10 — SCREENING: North America — NA-1 (Tech, Communication Services, Consumer Discretionary)

**Task type:** SCREENING (Phase 01), rotation slice [NA-1](../framework/screening-coverage-log.md). Picked by the rotation rule: NA-1's "Last screened" date (2026-09-08) was the oldest on the matrix (NA-2 09-29, EU 09-22, JP 09-26, EM 09-15, APAC-EX-JP 10-06). Unattended scheduled run.

## 0. Methodology

- **Stale-prompt note:** the stored prompt says "monthly" and "EODHD Path A". `screen.md` has no EODHD path; EODHD was removed on 2026-06-19 ([decision](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)). I checked the key anyway: `/fundamentals` returns **403** on the current plan, so it is unusable regardless. Not used.
- **Starting universe:** no screener paste is possible unattended, so this is the ETF-holdings fallback (MOAT/QUAL/QGRW) — **approximate, misses small/mid-caps outside those ETFs' top-25**. This run reused the 24-name post-triage survivor pool from [2026-09-08](2026-09-08-screening-na1.md) (ETF composition and structural-triage eliminations unchanged; not re-pulled this run — a limitation, new ETF entrants since 09-08 would be missed).
- **Data:** `python3 -m scripts.fetch_fundamentals` (yfinance **reachable again**). 21/24 returned data. CPRT, ANET, BRK.B failed with missing TTM EBIT / total debt (genuine field gaps) and were checked against stockanalysis.com via WebFetch. No values estimated (Rule 0). yfinance and stockanalysis.com bases differ (ROIC especially), so figures aren't strictly comparable to the 09-08 round.

## 1. Phase 01 gate (8 filters: GM>40, NM>12, ROIC>15, Rev 3yr CAGR>8, FCF+ 3yr, ND/EBITDA<2.5, FCF yield>4, EV/EBIT<20)

| Ticker | GM | NM | ROIC | CAGR | FCF3y | ND/EBITDA | FCF yld | EV/EBIT | Misses |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 48.7 | 27.6 | 74.3 | 1.81 ❌ | ✅ | 0.37 | 2.78 ❌ | 31.9 ❌ | 3 |
| ABNB | 82.9 | 20.5 | 22.9 | 13.4 | ✅ | -1.63 | 4.89 | 30.3 ❌ | **1** |
| ADP | 46.4 | 20.1 | 43.4 | 6.81 ❌ | ✅ | 0.11 | 4.45 | 17.6 | **1** |
| AMAT | 49.4 | 30.1 | 35.6 | 3.23 ❌ | ✅ | -0.02 | 1.40 ❌ | 36.1 ❌ | 3 |
| AMD | 53.2 | 15.6 | 9.9 ❌ | 13.6 | ✅ | -0.18 | 0.85 ❌ | 127.9 ❌ | 3 |
| ANET* | n/a | n/a | 284.8 | n/a | n/a | -2.88 | 1.89 ❌ | 57.2 ❌ | ≥2 |
| BR | 31.8 ❌ | 15.0 | 19.9 | 7.25 ❌ | ✅ | 1.58 | 6.60 | 14.1 | 2 |
| BRK.B* | structural (conglomerate) | | 19.3 | | | -1.81 | 2.19 ❌ | 7.45 | ≥1 (prior rounds: GM, CAGR) |
| CPRT* | 45.3 | 31.8 | 28.4 | **6.43 ❌** | ✅ (prior) | -2.36 | 5.01 | 12.65 | **1** |
| CRM | 77.3 | 22.0 | 13.4 ❌ | 9.82 | ✅ | 0.55 | 8.04 | 17.3 | **1** |
| CSCO | 64.5 | 21.0 | 18.1 | 3.57 ❌ | ✅ | 1.20 | 2.74 ❌ | 27.6 ❌ | 3 |
| DDOG | 79.5 | 4.5 ❌ | 4.0 ❌ | 26.95 | ✅ | 7.02 ❌ | 1.02 ❌ | 477.8 ❌ | 5 |
| FTNT | 80.2 | 28.2 | 95.6 | 15.5 | ✅ | -0.58 | 2.18 ❌ | 52.8 ❌ | 2 |
| GOOGL | 60.9 | 54.8⚠️ | 53.3 | 12.5 | ✅ | 0.09 | 1.24 ❌ | 13.9 | **1** |
| KLAC | 61.3 | 35.6 | 41.5 | 8.97 | ✅ | 0.70 | 1.48 ❌ | 43.6 ❌ | 2 |
| LLY | 83.4 | 33.5 | 47.5 | 31.7 | ❌⚠️ | 0.85 | 1.29 ❌ | 26.6 ❌ | 3 |
| LPLA | 23.3 ❌ | 5.1 ❌ | 10.4 ❌ | 25.5 | ❌ | 2.51 ❌ | -3.57 ❌ | 17.4 | 6 |
| LRCX | 50.5 | 31.3 | 45.7 | 10.1 | ✅ | -0.21 | 1.23 ❌ | 47.2 ❌ | 2 |
| MA | 78.1 | 46.3 | 63.1 | 13.8 | ✅ | 0.38 | 3.10 ❌ | 25.3 ❌ | 2 |
| MRVL | 52.2 | 27.9 | 16.1 | 11.45 | ✅ | 0.64 | 0.70 ❌ | 69.4 ❌ | 2 |
| ORCL | 64.0 | 26.4 | 14.0 ❌ | 10.5 | ❌ | 2.85 ❌ | -6.70 ❌ | 21.1 ❌ | 5 |
| PANW | 70.4 | 2.7 ❌ | 1.0 ❌ | 18.5 | ✅ | -0.01 | 1.20 ❌ | 638 ❌ | 4 |
| PLTR | 84.8 | 49.0 | 35.2 | 32.9 | ✅ | -0.45 | 0.67 ❌ | 187 ❌ | 2 |
| TYL | 47.2 | 13.4 | 7.7 ❌ | 8.03 | ✅ | -0.81 | 5.23 | 32.8 ❌ | 2 |

*Starred rows: yfinance had a field gap; values from stockanalysis.com ("Current" column, 2026-10-09). CPRT revenue: FY2026 4,666 / FY2023 3,870 → (4666/3870)^(1/3)−1 = 6.43%; CPRT 3yr-FCF-positive not re-pulled (positive in all prior rounds). "n/a" = not retrieved; ANET/BRK.B fail regardless on the FCF-yield and growth/margin points shown.

## ✅ Qualified Quality List — **0 names**

No name clears all 8 filters. **CPRT, last round's sole pass, drops out**: with FY2026 now reported, the FY-anchored CAGR window is FY2023→FY2026 (6.43%), consistent with the 07-28/08-18 figures; 09-08's 9.90% used FY2022→FY2025. The business is unchanged and now far cheaper (market cap ~$25B vs ~$44B at FY2025; FCF yield 5.01%, EV/EBIT 12.65x) — the only blocker is growth, 1.57pp short.

**Single-filter near-misses:** CPRT (CAGR), ADP (CAGR, −1.19pp, unchanged), CRM (ROIC 13.40% vs 15%; valuation now clear — stockanalysis.com's 10.96% on 09-08 used a different ROIC basis), GOOGL (FCF yield 1.24%; capex-heavy, FCF/NI only 22%; TTM net margin 54.8% a suspected one-off), ABNB (EV/EBIT 30.3x).

## 2. Qualitative pass (Step 3)
Not run — no name cleared the quantitative gate (nothing to walk through the 5 questions). Near-misses above are not advanced; they can be sent to `/new-position` on request, where a growth/ROIC judgment call belongs.

## 3. Data gaps (Step 4)
- yfinance: no TTM EBIT for CPRT, ANET, BRK.B (BRK.B/ANET also missing total debt/other) — stockanalysis.com used for those; ANET GM/NM/CAGR not re-fetched.
- LLY: yfinance shows a negative-FCF year (FCF/NI −60.2%) → FCF3y ❌, which contradicted 09-08's stockanalysis.com ✅; unreconciled, doesn't change FAIL (FCF yield, EV/EBIT).
- GOOGL net margin 54.8% outlier (same flag since 08-18); yfinance ROIC figures differ from stockanalysis.com's throughout (e.g. AAPL 74 vs 102, CRM 13.4 vs 11.0).
- ETF composition not re-pulled this run (reused 09-08 list).

## 4. Coverage log
NA-1 row updated: Last screened 2026-10-10; qualified names 0 (down from 1); sources appended.

## Glossary
- **CAGR** — compound annual growth rate: smoothed yearly growth between two points.
- **EV/EBIT** — enterprise value ÷ operating profit; lower = cheaper.
- **FCF / FCF yield** — free cash flow (cash left after running and maintaining the business) and that figure ÷ market value.
- **Gross / Net margin** — share of revenue left after direct costs / after all expenses.
- **Net Debt/EBITDA** — leverage gauge; negative means net cash.
- **ROIC** — return on invested capital.
- **Phase 01 / Qualified Quality List** — the framework's quality-gate stage and its list of passers.
- **TTM** — trailing twelve months.
- **Rotation Matrix** — [screening-coverage-log.md](../framework/screening-coverage-log.md), tracking which slice was screened when.

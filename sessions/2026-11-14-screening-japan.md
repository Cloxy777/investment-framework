# 2026-11-14 — SCREENING: Japan (JP) — Round 7 (fresh candidate pool)

**Task type:** SCREENING (Phase 01) — rotation slice [JP](../framework/screening-coverage-log.md). Picked per the rotation rule: oldest "Last screened" date (JP 2026-10-24, ahead of NA-2 10-27, APAC-ex-JP 10-31, NA-1 11-03, EM 11-07, EU 11-10). Unattended scheduled run (Routine, monthly slice).

## 0. Methodology and flags

- **Step 0:** no user available, so the unattended exception applies. A fresh pool was built by structural triage from domain knowledge (not ETF holdings, which would resurface already-covered names). **Flag: not an exhaustive screen**; it can miss names.
- **EODHD (Path A) not used.** `EODHD_API_KEY` is set, but `/fundamentals` and `/screener` both return **403** (free plan) on this run. EODHD was removed from the framework on 2026-06-19 ([decision](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)); same stale-prompt precedent as earlier JP rounds.
- **Data source:** `python -m scripts.fetch_fundamentals` fails with `MissingInputError` ("EBIT" row not found) on JP tickers (same systemic gap as 2026-09-26 / 10-24). Fallback: yfinance **annual statements, latest FY (not TTM)** via an ad-hoc script. Basis: Revenue CAGR = latest FY vs 3 FY earlier; ROIC = EBIT × (1 − 30% assumed tax) ÷ yfinance "Invested Capital" (**tax rate assumed**, ROIC approximate); EV = market cap + total debt − cash & ST investments; FCF yield = latest FY FCF ÷ current market cap. **Sanity check:** re-running Insource (6200.T) reproduced the 2026-10-24 figures exactly.
- Gate (valuation-scoring.md): gross >40%, net >12%, ROIC >15%, Rev 3y CAGR >8%, FCF positive 3 FY, ND/EBITDA <2.5×, FCF yield >4%, EV/EBIT <20×.

## Step 1 — Pool and structural triage

19 names, none previously screened in JP: Visional, Dip, Dentsu Soken, IR Japan, Otsuka Corp, TIS, Appier, CARTA (3688), Plaid, Brainpad (3655), Wantedly, Soliton (6553), System Support, eBASE, ID Holdings, 3938, 4726, 4739 (+ Insource as control). No structural exclusions (hand-picked asset-light/software/services names). Low-margin IT distributors/SIers (Otsuka, TIS, Dentsu Soken, ID Holdings) were included deliberately as a test and fail on margin as expected.

## Step 2 — Quantitative gate (yfinance annual, latest FY)

| Company | FY end | Gross M | Net M | ROIC* | Rev 3y CAGR | FCF last 3 FY (¥bn) | ND/EBITDA | FCF yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| **Visional (4194.T)** | 2026-07 | 89.2% ✅ | 18.7% ✅ | 21.2% ✅ | 31.2% ✅ | 22.3 / 17.4 / 10.4 ✅ | −2.84× ✅ | 5.47% ✅ | 12.4× ✅ | **PASS 8/8** |
| Dip (2379.T) | 2026-02 | 88.5% ✅ | 10.9% ❌ | 17.2% ✅ | 3.6% ❌ | 4.7 / 11.0 / 5.4 ✅ | −1.33× ✅ | 5.76% ✅ | 6.9× ✅ | FAIL 6/8 |
| Plaid (4165.T) | 2025-09 | 73.1% ✅ | 8.2% ❌ | 14.5% ❌ | 22.5% ✅ | 1.3 / 0.8 / −0.4 ❌ | −3.29× ✅ | 4.03% ✅ | 19.5× ✅ | FAIL 5/8 |
| ID Holdings (4709.T) | 2026-03 | 25.7% ❌ | 7.4% ❌ | 18.3% ✅ | 8.2% ✅ | ✅ | −1.21× ✅ | 8.54% ✅ | 6.8× ✅ | FAIL 6/8 (margins) |
| System Support (4396.T) | 2026-06 | 29.4% ❌ | 6.0% ❌ | 21.3% ✅ | 17.3% ✅ | ✅ | −1.30× ✅ | 6.56% ✅ | 7.8× ✅ | FAIL 6/8 (margins) |
| eBASE (3835.T) | 2026-03 | 51.7% ✅ | 19.5% ✅ | 13.6% ❌ | 3.7% ❌ | ✅ | −3.38× ✅ | 6.31% ✅ | 7.1× ✅ | FAIL 6/8 (ROIC, CAGR) |
| Wantedly (3991.T) | 2026-08 | 33.5% ❌ | 22.1% ✅ | 23.4% ✅ | 3.0% ❌ | ✅ | −3.77× ✅ | 26.8% ⚠ | 0.8× ⚠ | FAIL 5/8 (valuation figures look implausible for a ¥8bn cap — likely cash-heavy balance sheet/data artifact; not relied on) |
| IR Japan (6035.T) | 2026-03 | 79.4% ✅ | 14.6% ✅ | 14.4% ❌ | 0.7% ❌ | ✅ | −2.94× ✅ | 9.38% ✅ | 6.3× ✅ | FAIL 6/8 |
| Dentsu Soken (4812.T) | 2025-12 | 36.6% ❌ | 9.9% ❌ | 16.5% ✅ | 8.5% ✅ | ✅ | −0.22× ✅ | 2.91% ❌ | 23.5× ❌ | FAIL 4/8 |
| Otsuka Corp (4768.T) | 2025-12 | 19.1% ❌ | 4.9% ❌ | 15.8% ✅ | 15.4% ✅ | ✅ | −2.45× ✅ | 5.08% ✅ | 13.0× ✅ | FAIL 6/8 (margins) |
| TIS (3626.T) | 2026-03 | 28.2% ❌ | 7.8% ❌ | 13.5% ❌ | 5.5% ❌ | ✅ | −0.67× ✅ | 5.91% ✅ | 12.2× ✅ | FAIL 4/8 |
| Appier (4180.T) | 2025-12 | 53.8% ✅ | 5.8% ❌ | 4.7% ❌ | 31.1% ✅ | ❌ (all negative) | −1.32× ✅ | −1.2% ❌ | 44.3× ❌ | FAIL 3/8 |
| Insource (6200.T) — control | 2025-09 | 76.9% | 28.5% | 33.5% | 15.5% | ✅ | −1.33× | 7.83% | 7.9× | already on list (reproduced) |

*ROIC uses an assumed 30% tax rate (see §0). **No single-filter near-misses this round.**

## Qualified Quality List — 1 new name (pending `/new-position`)

**Visional (4194.T)** — HR-tech (BizReach direct-recruiting platform, HRMOS HR SaaS). **Not valuation-scored.**

## Step 3 — Qualitative pass (1 name, handled directly — below batch threshold)

Sources are one web search plus quantitative data; secondary aggregators, so unverified against company filings.

### Visional (4194.T)
1. **Why margins high?** Platform/subscription model; 89.2% gross margin. FY2026 operating profit ¥24.6bn (+14.6%) on revenue ¥99.3bn (+23.9%) ([Gyokai Digest](https://www.gyokaidigest.com/en/companies/visional), [Quartr](https://quartr.com/events/visional-inc-4194-q4-2026_FeNHgmWb)). Whether margins reflect pricing power vs. scale — *not verified*.
2. **Competing:** BizReach competitors include JAC Recruitment and other recruiters; the peer comparison found shows Visional leading on operating profit while JAC grew revenue +17.7% vs Visional +23.9% ([Gyokai Digest](https://www.gyokaidigest.com/en/industry/hr-tech/2026-FY)). Moat width (network effects, candidate/recruiter database) — *not verified*.
3. **Capital allocation:** net cash (ND/EBITDA −2.84×); FCF up from ¥10.4bn to ¥22.3bn over 3 FY. Buyback/dividend history *not sourced*.
4. **Growth:** FY26 revenue +23.9%; BizReach ¥80.1bn (+16.8%); HRMOS revenue +77.7% in first three quarters; FY27 guide revenue ¥119.9bn, operating profit ¥26.6bn (secondary sources).
5. **Bear case:** BizReach generates most segment profit (single-product concentration); operating profit growing slower than revenue (+14.6% vs +23.9%) on growth investment; HRMOS FY loss forecast revised to ¥0.6bn; incubation segment loses ¥2.4bn; market cap ~¥407bn means the 5.5% FCF yield is on a recently re-rated base.
6. **Disruption:** AI-driven matching/LinkedIn-style platforms and Japan's labour-market cycle (hiring demand is cyclical) are live risks. **Verdict: PASS with FLAGS (concentration, margin dilution from investments, unverified moat, cyclical hiring demand).**

## Step 4 — Data gaps (none estimated)

- 3688.T, 3655.T, 6553.T, 3938.T, 4726.T, 4739.T: yfinance returned no data → unscored (ticker validity for some may also be wrong).
- All metrics latest-FY, not TTM; ROIC uses assumed 30% tax.
- Wantedly valuation outputs (FCF yield 26.8%, EV/EBIT 0.8×) look anomalous; not relied on (fails on gross margin and CAGR regardless).
- Visional: moat, buyback/dividend history and filing-level numbers not verified (secondary sources only).

## Next steps

`/new-position 4194.T` (live price, TTM data, filings). Untested JP ideas: retry the six data-gap tickers.

## Glossary

- **Phase 01 / quality gate** — the 8 quantitative filters a company must pass before valuation scoring ([strategy.md](../framework/strategy.md)).
- **Gross / Net margin** — share of revenue left after direct costs / after all costs.
- **ROIC** — return on invested capital: profit earned on the money tied up in the business.
- **Revenue 3yr CAGR** — compound annual revenue growth over three years.
- **FCF (free cash flow) / FCF yield** — cash left after capex; yield = FCF ÷ market cap.
- **Net Debt/EBITDA** — debt minus cash relative to operating cash earnings; negative = net cash.
- **EV/EBIT** — enterprise value (market cap + debt − cash) ÷ operating profit; a valuation multiple.
- **Moat** — durable competitive advantage.
- **TTM** — trailing twelve months. **FY** — fiscal year.
- **Near-miss** — fails exactly one filter.

# 2026-10-31 — SCREENING: Developed Asia-Pacific ex-Japan (APAC-EX-JP)

**Task type:** SCREENING (Phase 01), slice [APAC-EX-JP](../framework/screening-coverage-log.md), unattended scheduled run (Routine 4). Picked per rotation rule: oldest "Last screened" (APAC-EX-JP 2026-10-06; next oldest EM 2026-10-17).

**Process note:** the stored prompt again asks for EODHD "Path A". `screen.md` has no such path and [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md) marks that key as a compromised credential, so it was **not used** (same precedent as every run since 2026-06-30). Step 0 = unattended fallback → hand-picked pool from domain knowledge. **Flag:** this approach misses names not hand-selected.

**Data source:** `python3 -m scripts.fetch_fundamentals` (yfinance, after `pip install -r scripts/requirements.txt`). Yahoo was reachable but hit `YFRateLimitError` 429 mid-run, and yfinance has **no TTM EBIT row for ASX tickers** (systemic, same pattern as Japan). stockanalysis.com fallback was **not attempted** this run (budget) — the gaps below stay open.

## Step 1 — Structural triage
Pool of 15 = 3 carried data-gap names from 10-06 + 12 fresh quality franchises (ASX software/marketplaces/healthcare IT, TW/HK/SG large caps). No eliminations.

## Step 2 — Quantitative gate (2026-10-31)
Filters: GM>40 · NM>12 · ROIC>15 · RevCAGR>8 · FCF+3yr · ND/EBITDA<2.5 · FCF yld>4 · EV/EBIT<20.

| Ticker | Company | GM | NM | ROIC | Rev CAGR | FCF 3yr+ | ND/EBITDA | FCF yld | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 2330.TW | TSMC | 65.85 | 51.12 | 39.24 | 18.94 | Yes | −0.47 | 2.38 | 19.24 | **FAIL (FCF yield only, −1.62pp)** — quality clears, valuation marginal |

**Data gaps — not scored, not estimated (Rule 0):**
- No TTM EBIT row in yfinance: LOV.AX Lovisa, OCL.AX Objective, PME.AX Pro Medicus, TNE.AX Technology One, XRO.AX Xero, WTC.AX WiseTech, CAR.AX CAR Group, REA.AX REA Group, ALQ.AX ALS, 2382.HK Sunny Optical.
- NaN in trailing-4Q cash flow/EBIT: 3293.TWO Gamania, 1810.HK Xiaomi (EBIT).
- Yahoo 429 rate limit: S68.SI SGX, 6415.TWO Silergy.
- Pattern: **ASX and several HK tickers cannot be run through `fetch_fundamentals` at all** — need the stockanalysis.com route (as in 2026-09-12) or an ASX-aware fallback in the script.

## Step 3 — Qualitative pass
No name cleared the quantitative gate; nothing to walk through.

## Result
**0 new qualified.** Slice total unchanged (prior qualified names pending `/new-position`: Classys, PharmaResearch, ASMedia, Hugel, iFAST). TSMC is a single-filter near-miss (FCF yield 2.38% vs >4%). 10 of 15 names unscored due to data gaps — recommend a follow-up round via stockanalysis.com for the ASX names (highest-quality unscored: Pro Medicus, Technology One, REA, CAR).

## Glossary
- **Phase 01 gate** — the 8 quantitative quality/value filters a company must clear first.
- **ROIC** — profit earned per dollar of capital invested.
- **EV/EBIT** — whole-business price divided by operating profit; lower = cheaper.
- **EBIT** — earnings before interest and tax, i.e. operating profit.
- **FCF yield** — free cash flow divided by market value.
- **Net Debt/EBITDA** — debt net of cash relative to annual operating cash earnings; negative = net cash.
- **CAGR** — compound annual growth rate.
- **TTM** — trailing twelve months.

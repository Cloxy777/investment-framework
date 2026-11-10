# 2026-11-10 — SCREENING: Europe (EU), Round 7

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [EU](../framework/screening-coverage-log.md) (UK, Eurozone, Switzerland, Nordics), all sectors. Unattended scheduled run (Routine 4; research-only).

**Slice selection:** EU's "Last screened" (2026-10-20) was the oldest in the Rotation Matrix (NA-2 10-27, APAC-EX-JP 10-31, NA-1 11-03, EM 11-07, JP 10-24 is newer than EU).

## Scheduled-prompt discrepancy (same as prior rotation sessions)

The stored prompt describes a "Monthly" run using `EODHD_API_KEY` "Path A". `screen.md` has no EODHD path (removed per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)). Key re-tested: `/eod` HTTP 200, `/fundamentals` **403 "Only EOD data allowed for free users"** (free plan) — cannot supply any gate metric, not used. Followed `screen.md`.

## Step 0 — Starting universe

Unattended → domain-knowledge structural-triage pool. 12 fresh names, none covered by earlier EU sessions (grep-checked). **Data source:** `scripts.fetch_fundamentals` could not run (pip install of pandas/yfinance hung in this environment), so stockanalysis.com via WebFetch, 4 parallel research agents (3/3/3/2 tickers).

## Step 1 — Structural triage

Dunelm (DNLM.L) excluded: volume home-furnishings retail. 11 tested: Fortnox, Atoss, Lagercrantz, Addtech, Vitec, Inficon, Sensirion, Medistim, Technogym, Sdiptech, Kone.

## Step 2 — Phase 01 quantitative gate

Margins/ROIC/CAGR on latest completed FY; ND/EBITDA, FCF yield, EV/EBIT current (2026-11-10).

| Ticker | FY | Gross M | Net M | ROIC | Rev CAGR | FCF 3y | ND/EBITDA | FCF yld | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| **AOF Atoss Software** (EUR) | FY25 | 78.4% ✅ | 25.6% ✅ | 57.53% ✅ | 18.4% ✅ | ✅ | ≈−1.45× ✅ (derived) | 4.88% ✅ (TTM) | 16.71× ✅ | **PASS 8/8** |
| MEDI Medistim (NOK) | FY25 | 81.7% ✅ | 22.8% ✅ | 54.24% ✅ | 12.9% ✅ | ✅ | −0.61× ✅ | 3.46% ❌ | 24.96× ❌ | FAIL 6/8 (valuation only) |
| TGYM Technogym (EUR) | FY25 | 46.9% ✅ | 11.3% ❌ | 55.92% ✅ | 12.2% ✅ | ✅ | −0.46× ✅ | 3.96% ❌ | 17.46× ✅ | FAIL 6/8 (net margin 0.7pp, FCF yield 0.04pp) |
| FNOX Fortnox | FY24 | 62.9% ✅ | 34.7% ✅ | 24.36% ✅ | 29.9% ✅ | ✅ | −0.74× ✅ | 1.50% ❌ | 57.55× ❌ | **Delisted** (EQT take-private; last trade 2025-07-24) — remove from universe |
| IFCN Inficon (reports USD) | FY25 | 44.9% ✅ | 12.7% ✅ | 28.78% ✅ | 5.0% ❌ | ✅ | −0.51× ✅ | 2.16% ❌ | 36.02× ❌ | FAIL 5/8 |
| KNEBV Kone | FY25 | 56.5% ✅ | 8.6% ❌ | 51.2% ✅ | 1.0% ❌ | ✅ | −0.44× ✅ | 4.08% ✅ | 21.57× ❌ | FAIL 5/8 |
| SENS Sensirion (CHF) | FY25 | 52.3% ✅ | 5.9% ❌ | 13.46% ❌ | 2.1% ❌ | ❌ | net cash ✅ | 2.24% ❌ | 34.32× ❌ | FAIL 2/8 |
| LAGR-B Lagercrantz | — | DATA GAP (404) | | | | | | | | Not scored |
| ADDT-B Addtech | — | DATA GAP (404) | | | | | | | | Not scored |
| VIT-B Vitec | — | DATA GAP (404) | | | | | | | | Not scored |
| SDIP-B Sdiptech | — | DATA GAP (404) | | | | | | | | Not scored |

## Step 3 — Qualitative pass (1 survivor)

**Atoss — PASS (with flags).** Workforce-management software (Germany/DACH), 20 consecutive record years per company release; Cloud & Subscriptions growing >10%/yr; H1 2026 revenue +12% (€103.2m), EBIT +17%; FY26 guidance EBIT margin ≥34% (one source reports a raise to ~37% — unconfirmed), FY27 revenue €235–245m guided. Net-cash balance sheet. Flags: (1) FCF yield pass is thin and TTM-based — FY25 annual FCF (€46.2m) gives ≈3.3% yield on current cap (agent arithmetic), which would fail; (2) sources conflict on exact FY26 guidance; (3) competitive position vs SAP/Workday/UKG and AI-disruption risk **not sourced this session** — verify before `/new-position`; (4) no one-off items identified, but line items were not audited.

## Step 4 — Data gaps (nothing estimated)

- Lagercrantz, Addtech, Vitec, Sdiptech: all stockanalysis.com `/quote/sto/<TICKER>/` URLs return 404 (pattern or slug problem; not confirmed delisted). Retry with another source/slug next round.
- Fortnox: delisted (EQT X / First Kraft, last trading day 2025-07-24); stale data discarded.
- ND/EBITDA for Atoss/Medistim/Technogym derived (pages show gross debt/EBITDA only); Sensirion EBITDA not shown (net cash only).
- Inficon quote currency CHF vs USD reporting — mixed-currency figures taken from stockanalysis.com as shown.
- Kone gross margin 56.5% (statistics, TTM) vs 57.7% (FY25 income statement) not reconciled; verdict unaffected.
- yfinance not used (install hung); EODHD fundamentals 403.

## ✅ Qualified Quality List — 1 new name (pending `/new-position`)

1. **Atoss Software (AOF.DE)** — quant 8/8; qualitative PASS with flags above.

EU qualified total: 8 → **9**. Near-misses: Medistim (valuation only), Technogym (net margin 11.3%, FCF yield 3.96%).

## Step 5 — Coverage log updated

EU row: Last screened → 2026-11-10; qualified total 9; sources appended.

## Glossary

- **CAGR** — Compound Annual Growth Rate.
- **EBIT / EV/EBIT** — operating profit; enterprise value ÷ EBIT (lower = cheaper).
- **FCF / FCF yield** — free cash flow; FCF ÷ market cap.
- **Net Debt/EBITDA** — leverage ratio; negative = net cash.
- **ROIC** — Return on Invested Capital.
- **TTM** — trailing twelve months.
- **Take-private** — a buyer (here EQT) acquires all shares and delists the company.
- **SaaS** — software sold by subscription.

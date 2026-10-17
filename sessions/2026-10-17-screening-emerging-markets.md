# 2026-10-17 — SCREENING: Emerging Markets (EM)

**Task type:** SCREENING (Phase 01) — rotation slice [EM](../framework/screening-coverage-log.md). Picked as the oldest "Last screened" date in the matrix (2026-09-15; next oldest NA-2 09-29, JP 09-26, EU 09-22, APAC-EX-JP 10-06, NA-1 10-10).

**Unattended scheduled routine** (Monthly Universe Screening Slice). The stored prompt again says "EODHD Path A"; EODHD was removed on 2026-06-19 ([decision](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)). This run **tested the key anyway**: `/fundamentals` still returns **HTTP 403** and `/user` shows a free plan (20 calls/day) — no bulk screener available. Falling back to the documented unattended path (carry-over pool, no ETF re-pull needed: the 21-name pool from 09-15 is the current EM pool).

## Sourcing and its limits (this round is a PARTIAL refresh)

- `scripts.fetch_fundamentals` (yfinance reachable; needed `pip install pandas yfinance`): returned data for only **6 of 20** names (PDD, NTES, INFY, MELI, B3, YMM). The rest failed with field gaps (no `EBIT` row / NaN TTM / missing `marketCap` / missing FCF row). Per Rule 0 these are **not estimated**.
- For ADRs (PDD, NTES, YMM) the script mixes USD market cap with CNY financials, so its FCF yield (96%, 62%, 58%) and EV/EBIT (negative) are **currency-mismatch artifacts, discarded** (same issue documented 09-15). Its margin, ROIC and CAGR lines are single-currency and usable.
- stockanalysis.com (WebFetch, live TTM) used for ROIC / FCF yield / EV/EBIT on Tencent, PDD, ANTA, YMM, Trip.com. **Not refreshed (404 URL / no data): Proya, Moutai, and the 9 other India/WuXi names** — last round's figures stand, marked stale.
- Revenue 3yr CAGR and FCF-3yr-positive are **carried from 09-15** where the script failed (Tencent, ANTA); no new filings in-between except possibly interim results.

## Step 1 — Triage
Pool unchanged from [2026-09-15](2026-09-15-screening-emerging-markets.md); same categorical exclusions (banks, commodity cyclicals, telecom, thin-margin retail, etc.). No new names added.

## Step 2 — Quantitative gate (refreshed names)

| Ticker | Gross M | Net M | ROIC | Rev 3y CAGR | FCF 3y+ | ND/EBITDA | FCF yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **Tencent (0700.HK)** | 56.70% ✅ | 29.87% ✅ | 18.27% ✅ | 10.67%† ✅ | ✅† | net cash ✅ | 5.17% ✅ | 12.39x ✅ | **PASS 8/8** (SA TTM; CAGR carried) |
| **ANTA (2020.HK)** | 62.34% ✅ | 18.83% ✅ | 23.30% ✅ | 14.35%† ✅ | ✅† | net cash ✅ | 10.81% ✅ | 8.27x ✅ | **PASS 8/8** (CAGR carried) |
| **PDD** | 56.32% ✅ | 20.43% ✅ | **14.92% SA / 23.83% script** ⚠️ | 49.00% ✅ | ✅ | −1.05x ✅ | 14.36% ✅ | 3.36x ✅ | **PASS but ROIC source conflict**: stockanalysis.com is 0.08pp under the 15% bar, yfinance NOPAT/InvCap is well above. Not a clean pass — verify from 20-F before `/new-position` |
| **Full Truck Alliance (YMM)** | 87.26% SA / 65.68% script ⚠️ | 32.99% ✅ (treasury-income inflated, see 09-15) | **16.66% SA / 8.54% script** ⚠️ | 22.87% ✅ | ✅ | net cash ✅ | 10.82% ✅ | 8.88x ✅ | **PASS but source conflict on ROIC and gross margin** (gross margin passes either way; ROIC fails on the script's basis). Verify before acting |
| Trip.com (TCOM) | 80.05% ✅ | 36.90% ✅ | **7.57%** ❌ | 46.04%† | ✅† | Debt/EBITDA 2.31 (gross) | 8.06% ✅ | 11.20x ✅ | **FAIL — ROIC only**, worse than 10.87% last round |
| NetEase (NTES) | 67.15% ✅ | 27.88% ✅ | 20.08% (script; ROIC distorted by net cash) | **5.29%** ❌ | ✅ | −0.93x ✅ | n/m (currency artifact) | n/m | **FAIL — Rev CAGR** (5th straight round) |
| Infosys (INFY) | **30.32%** ❌ | 16.38% ✅ | 34.37% ✅ | **3.44%** ❌ | ✅ | −0.31x ✅ | 7.67% ✅ | 21.18x ❌ | **FAIL — GM, CAGR, EV/EBIT** |
| MercadoLibre (MELI) | 42.68% ✅ | **5.30%** ❌ | **12.74%** ❌ | 38.91% ✅ | ✅ | 1.39x ✅ | 13.35% ✅ | **35.66x** ❌ | **FAIL — NM, ROIC, EV/EBIT** |
| B3 (B3SA3.SA) | 73.27% ✅ | 49.46% ✅ | 21.51% ✅ | **3.47%** ❌ | ✅ | 1.90x ✅ | 5.16% ✅ | 10.88x ✅ | **FAIL — Rev CAGR only** (unchanged) |

† carried from 2026-09-15 (not re-derivable this round).

**Not refreshed (data gap, last result stands, stale since 09-15):** Proya (603605.SH; qualitative FAIL on 09-15 regardless), Kweichow Moutai, WuXi Biologics, TCS, Asian Paints, Pidilite, Divi's, ITC, Info Edge, Persistent, WEG, XP Inc — yfinance field gaps and no stockanalysis.com page retrieved.

## Step 3 — Qualitative pass
Not redone: no new names reached the gate and the Tencent / ANTA / PDD / YMM qualitative reads from 09-15 stand. The two source-conflicted names need a primary-filing ROIC check first.

## Qualified Quality List — 4 names (2 clean, 2 source-contested)
1. **Tencent (0700.HK)** — clean
2. **ANTA Sports (2020.HK)** — clean
3. **PDD Holdings (PDD)** — ROIC 14.92% vs 23.83% across sources; resolve from 20-F
4. **Full Truck Alliance (YMM)** — ROIC/gross margin conflict; net margin inflated by treasury income

Proya carried as quant-pass / qualitative FAIL (09-15), excluded from the count.

**Near-misses:** Trip.com (ROIC only, 7.57%), B3 (Rev CAGR only), Moutai (FCF yield only, stale).

## Step 4 — Data gaps (flagged, not estimated)
Listed above: 14 names without refreshed data; ADR currency artifacts; PDD/YMM cross-source conflicts. SBC / buyback fields UNKNOWN from the script (not needed for Phase 01).

## Glossary
- **ADR** — US-listed certificate for a foreign company's shares (glossary: ADR).
- **CAGR** — smoothed annual growth rate over several years.
- **ROIC** — after-tax operating profit ÷ capital invested in the business; the >15% bar tests capital efficiency.
- **FCF yield** — free cash flow ÷ market cap; the >4% bar tests cheapness.
- **EV/EBIT** — enterprise value ÷ operating profit; <20x bar.
- **Net Debt/EBITDA** — debt net of cash relative to operating cash earnings; <2.5x bar.
- **TTM** — trailing twelve months.
- **Net cash** — cash exceeds debt (negative net debt).

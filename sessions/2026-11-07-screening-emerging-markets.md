# 2026-11-07 — SCREENING: Emerging Markets (EM)

**Task type:** SCREENING (Phase 01) — rotation slice [EM](../framework/screening-coverage-log.md), picked as the oldest "Last screened" date (EM 2026-10-17; next oldest NA-1 11-03, NA-2 10-27, JP 10-24, EU 10-20).

**Unattended scheduled routine** (Monthly Universe Screening Slice). The stored prompt references EODHD Path A; EODHD was removed 2026-06-19 ([decision](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)). Key tested again: `/fundamentals` still **HTTP 403** (free plan). Used the documented unattended fallback: carry-over 20-name EM pool (no new names added — no ETF re-pull), `scripts.fetch_fundamentals`/yfinance, plus stockanalysis.com (WebFetch) for the four qualifiers. **Partial refresh.**

## Sourcing and limits
- yfinance returned usable data for PDD, YMM, NTES, INFY, MELI, B3, WEGE3, XP. Field gaps (not estimated, Rule 0): Tencent (NaN TTM EBIT), ANTA, 2269.HK WuXi Bio (no EBIT row), TCOM (NaN net income), Moutai and TCS (no marketCap), ITC/Divi's/Asian Paints/Pidilite/Info Edge/Persistent (no FCF row).
- ADR script outputs for PDD/YMM/NTES (FCF yield 94%/56%/60%, negative EV/EBIT) are CNY-vs-USD currency artifacts — discarded. Margin/ROIC/CAGR lines are single-currency.
- Net Debt/EBITDA from stockanalysis.com was *derived by the fetch summarizer* (not a listed field); the YMM figure (-5.3x) mixes currencies and is unreliable — only "net cash ✅" is relied on.
- Rev 3yr CAGR / FCF-3yr-positive for Tencent and ANTA carried from 2026-09-15.

## Step 1 — Triage
Pool unchanged from [2026-10-17](2026-10-17-screening-emerging-markets.md); same categorical exclusions.

## Step 2 — Quantitative gate (refreshed)
| Ticker | Gross M | Net M | ROIC | Rev CAGR | ND/EBITDA | FCF yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|
| Tencent 0700.HK (SA) | 56.70% ✅ | 29.87% ✅ | 18.27% ✅ | 10.67%† ✅ | net-debt ~0.04x ✅ | 5.15% ✅ | 12.44x ✅ | **PASS 8/8** |
| ANTA 2020.HK (SA) | 62.34% ✅ | 18.83% ✅ | 23.30% ✅ | 14.35%† ✅ | net cash ✅ | 10.58% ✅ | 8.45x ✅ | **PASS 8/8** |
| PDD (SA / script) | 56.32% ✅ | 20.43% ✅ | **14.92% SA / 23.83% script** ⚠️ | 49.00% ✅ | net cash ✅ | 14.04% ✅ | 3.56x ✅ | **Source-contested** (SA 0.08pp under bar) — unchanged |
| YMM (SA / script) | 87.26% SA / 65.68% ✅ | 32.99% ✅ (treasury-income inflated) | **16.66% SA / 8.54% script** ⚠️ | 22.87% ✅ | net cash ✅ | 10.36% ✅ | 9.55x ✅ | **Source-contested** — unchanged |
| NetEase | 67.15% ✅ | 27.88% ✅ | 20.08% ✅ | **5.29%** ❌ | -0.93x ✅ | n/m | n/m | FAIL — Rev CAGR (6th round) |
| Infosys | **30.40%** ❌ | 16.21% ✅ | 34.15% ✅ | **3.44%** ❌ | -0.28x ✅ | 7.17% ✅ | **21.49x** ❌ | FAIL (3 filters) |
| MercadoLibre | 42.02% ✅ | **4.91%** ❌ | **13.05%** ❌ | 38.91% ✅ | 1.37x ✅ | 16.01% ✅ | **30.42x** ❌ | FAIL (3 filters) |
| B3 | 73.27% ✅ | 49.46% ✅ | 21.51% ✅ | **3.47%** ❌ | 1.90x ✅ | 7.93% ✅ | 7.08x ✅ | FAIL — Rev CAGR only |
| WEG (WEGE3.SA) | **32.96%** ❌ | 15.40% ✅ | 34.16% ✅ | 10.91% ✅ | -0.10x ✅ | **1.49%** ❌ | **22.34x** ❌ | FAIL (3 filters; valuation) |
| XP Inc | 27.63% ❌ | 63.12%* | 4.52% ❌ | 10.28% | 14.3x ❌ | artifact | artifact | FAIL — financial structure (should be triaged out) |

† carried from 2026-09-15. *Net margin inflated by financial-services revenue definition.

**Not refreshed (data gap, last result stands, stale):** Trip.com, Moutai, WuXi Biologics, TCS, Asian Paints, Pidilite, Divi's, ITC, Info Edge, Persistent, Proya (qualitative FAIL since 09-15).

## Step 3 — Qualitative pass
No new names reached the gate; the 09-15 qualitative reads for Tencent / ANTA / PDD / YMM stand. Nothing to batch.

## Qualified Quality List — 4 names (unchanged: 2 clean, 2 source-contested)
1. Tencent (0700.HK) — clean
2. ANTA Sports (2020.HK) — clean
3. PDD Holdings (PDD) — ROIC 14.92% vs 23.83% across sources; verify from 20-F
4. Full Truck Alliance (YMM) — ROIC/gross-margin conflict; net margin treasury-income inflated

Near-misses: B3 (Rev CAGR only), NetEase (Rev CAGR only), Moutai (FCF yield, stale).

## Step 4 — Data gaps (flagged, not estimated)
10 names unrefreshed as above; ADR currency artifacts; PDD/YMM cross-source conflicts; SBC/buyback fields UNKNOWN (not needed for Phase 01).

## Glossary
- **ADR** — US-listed certificate representing a foreign company's shares.
- **CAGR** — smoothed annual growth rate over several years.
- **ROIC** — after-tax operating profit ÷ capital invested; bar >15%.
- **FCF yield** — free cash flow ÷ market cap; bar >4%.
- **EV/EBIT** — enterprise value ÷ operating profit; bar <20x.
- **Net Debt/EBITDA** — debt net of cash relative to cash earnings; bar <2.5x.
- **TTM** — trailing twelve months.
- **Net cash** — cash exceeds debt.

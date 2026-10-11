# 2026-10-06 — SCREENING: Developed Asia-Pacific ex-Japan (APAC-EX-JP)

**Task type:** SCREENING (Phase 01), slice [APAC-EX-JP](../framework/screening-coverage-log.md) (AU/HK/SG/KR/TW), unattended scheduled run (Routine 4). Picked per rotation rule: oldest "Last screened" (APAC-EX-JP 2026-09-12; next oldest EM 09-15).

**Process note:** as in every rotation session since 2026-06-30, the stored prompt references an `EODHD_API_KEY` "Path A" and a monthly cadence. `screen.md` has no such path, and [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md) flags that key as a compromised credential. It was **not used** (a single unauthenticated-style probe of one fundamentals endpoint was made at setup and returned "Symbol not found"; no data taken). Step 0 = unattended ETF-fallback → hand-picked pool from domain knowledge (IQLT holdings not scrapeable; negligible APAC-ex-JP weight). **Flag:** this approach misses names not hand-selected.

**Data source:** `python3 -m scripts.fetch_fundamentals` (yfinance) — **reachable this round** (note: use `python3`, `python` resolves to a different interpreter without pandas here; deps installed via `python3 -m pip`). Figures are yfinance-derived, local currency, not directly comparable to prior stockanalysis.com rounds.

## Step 1 — Structural triage
13-name pool pre-selected to avoid already-excluded categories (banks, REITs, EMS/OSAT, commodity). No further eliminations.

## Step 2 — Quantitative gate (fetch_fundamentals output, 2026-10-06)
Filters: GM>40 · NM>12 · ROIC>15 · RevCAGR>8 · FCF+3yr · ND/EBITDA<2.5 · FCF yld>4 · EV/EBIT<20.

| Ticker | Company | GM | NM | ROIC | Rev CAGR | FCF 3yr+ | ND/EBITDA | FCF yld | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 214150.KQ | Classys | 75.13 | 37.29 | 21.70 | 33.43 | Yes | 0.26 | 5.40 | 10.94 | **PASS 8/8** |
| 214450.KQ | PharmaResearch | 77.71 | 30.77 | 27.41 | 40.16 | Yes | −0.65 | 4.29 | 11.29 | **PASS 8/8** (yield buffer 0.29pp) |
| 5269.TW | ASMedia | 50.90 | 50.63 | 19.25 | 36.73 | Yes | −1.26 | 4.54 | 13.37 | **PASS 8/8** (see NM flag) |
| 042700.KS | Hanmi Semiconductor | 57.35 | 40.27 | 32.19 | 20.75 | Yes | −1.11 | 0.39 | 87.68 | FAIL (FCF yld, EV/EBIT) |
| 140860.KQ | Park Systems | 66.98 | 11.91 | 8.07 | 18.20 | No | 0.01 | −3.43 | 66.69 | FAIL (NM, ROIC, FCF, yld, EV/EBIT) |
| 5274.TWO | ASPEED | 69.97 | 48.06 | 74.99 | 20.36 | Yes | −0.84 | 0.65 | 114.53 | FAIL (FCF yld, EV/EBIT) — quality, priced for AI |
| 3661.TW | Alchip | 37.20 | 25.42 | 14.43 | 31.10 | Yes (volatile) | −3.92 | −0.67 | 40.20 | FAIL (GM, ROIC, yld, EV/EBIT) |

**Data gaps (not estimated, Rule 0):** 3293.TWO Gamania, 3443.TW GUC (TTM FCF NaN); 558.SI UMS (TTM EBIT NaN); LOV.AX Lovisa, OCL.AX Objective, MZH.SI Nanofilm (no EBIT row). Deferred to a future round via stockanalysis.com. Also: 5yr-PE history <20 quarters for Classys/PharmaResearch/Hanmi/Park (valuation scoring will need no-history fallback — not scored here).

## Step 3 — Qualitative pass (web-sourced, brief; full 6-question pass deferred to `/new-position`)
- **Classys:** HIFU/RF devices, >55% Korean HIFU share, 80+ countries, ~45k installed base; 2025 op. margin 50.6%; FY26 guidance ~KRW 490bn (+45%). Moat = installed base + recurring consumables. Bear: device-cycle/competition in a crowded energy-device market (searches did not detail risks — open item). Sources: [GeneOnline](https://www.geneonline.com/classys-emerges-as-a-global-leader-in-medical-aesthetics-beyond-k-beauty-highlighting-45-growth-50-margins-and-recurring-revenue-model/), [Classys AR 2025](https://classys.com/wp-content/uploads/sites/2/2026/04/CLASSYS_AR-2025_eng_v2-1_0422-1.pdf).
- **PharmaResearch:** Rejuran (salmon-DNA PN skin booster) + Conjuran. **Flag:** one report says domestic medical-device growth fell from 93.5% to 6.2% in a recent quarter, with total growth (+27.1%) coming from cosmetics — a possible Rejuran deceleration. Source: [Edaily](https://en.edaily.co.kr/news/eda202608215081/). Single-product concentration.
- **ASMedia:** USB/PCIe controller chips. **Flag:** FY2025 net income TWD 5.43bn includes ~TWD 2.10bn equity-investment earnings (revenue 13.41bn) — the 50.6% net margin is inflated by non-core holdings; ex-equity earnings margin is roughly 25% (rough, pre-tax-treatment check, needs verification) — still above 12%. Source: [stockanalysis.com](https://stockanalysis.com/quote/tpe/5269/financials/income-statement/).

## Result
**3 qualified** (Classys, PharmaResearch, ASMedia), all pending `/new-position` verification with live prices. Korean aesthetics names correlate with existing qualified Hugel (sector concentration note).

## Glossary
- **Phase 01 gate** — the 8 quantitative quality/value filters a company must clear first.
- **ROIC** — profit earned per dollar of capital invested in the business.
- **EV/EBIT** — price of the whole business (incl. debt) divided by operating profit; lower = cheaper.
- **FCF yield** — free cash flow divided by market value.
- **Net Debt/EBITDA** — debt (net of cash) relative to annual operating cash earnings; negative = net cash.
- **CAGR** — compound annual growth rate.
- **HIFU** — high-intensity focused ultrasound, a non-surgical skin-lifting technology.
- **Equity-method earnings** — profit share from companies a firm partly owns, not from its own operations.

# 2026-10-13 — SCREENING: Emerging Markets (EM)

**Task type:** SCREENING (Phase 01), rotation slice [EM](../framework/screening-coverage-log.md) (China, India, Brazil, Mexico, other major EM; all sectors). Picked as the oldest "Last screened" date in the matrix (2026-09-15; next oldest NA-2 09-29). Prior round: [2026-09-15](2026-09-15-screening-emerging-markets.md).

**Unattended scheduled routine** (Monthly Universe Screening Slice). No user to paste a TIKR/Koyfin export, so Step 0 used the documented fallback: the 21-name pool carried over from 2026-09-15 (itself derived from the EM quality-name universe; same structural exclusions, unchanged). Flag: this misses small/mid-cap EM names not already in the pool.

**Stale-prompt note (recurring):** the routine prompt referenced EODHD "Path A". Tested live this session: the key is present but EODHD `/screener` and `/fundamentals` return **403 "Only EOD data allowed for free users"**, so Path A is unusable. EODHD was removed from the framework on 2026-06-19 ([decision](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)); the key was not used for data.

## Sourcing
- `scripts.fetch_fundamentals` (yfinance reachable): returned output for 6 names (PDD, NTES, INFY, MELI, B3SA3, YMM) but **failed with missing/NaN EBIT, FCF or marketCap fields for the other 13 names, including Tencent**. For the names that returned data, ADR/CNY currency mismatch distorts its price-based ratios (e.g. PDD FCF yield 95%, EV negative), so it was not used for verdicts. Flagged as a data gap, not estimated.
- Quantitative gate therefore taken from stockanalysis.com (WebFetch, 2026-10-13) via 3 parallel research agents; CAGR and FCF yields recalculated from sourced figures with market cap and FCF in the same currency. Net Debt/EBITDA is derived from net cash/debt and EBITDA on the page (all names but MELI net cash, so the <2.5x test is not decisive).
- Per the 09-15 convention, ROIC and EV/EBIT are stockanalysis.com "Current" values.
- **Not done this round:** a fresh qualitative (5-question) pass. Qualitative conclusions for the survivors are carried forward from [2026-09-15 Step 3](2026-09-15-screening-emerging-markets.md); no new news/filings search was performed, so any event since 09-15 is unchecked.

## Step 2 — Phase 01 gate
Filters: GM >40 · NM >12 · ROIC >15 · Rev 3yr CAGR >8 (FY-anchored) · FCF+ 3 yrs · ND/EBITDA <2.5 · FCF yield >4 · EV/EBIT <20.

| Ticker | GM | NM | ROIC | Rev CAGR | FCF+3y | ND/EBITDA | FCF yld | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Tencent 0700.HK | 56.70 | 29.87 | 18.27 | 10.7 | ✅ | −0.04 | 5.08 | 12.60 | **PASS 8/8** |
| ANTA 2020.HK | 62.34 | 18.83 | 23.30 | 14.4 | ✅ | net cash | 11.85 | 7.52 | **PASS 8/8** |
| Full Truck Alliance YMM | 87.26 | 32.99◊ | 16.66 | 22.9 | ✅ | −5.3 | 10.96 | 8.68 | **PASS 8/8** (net margin inflated by treasury income, per 09-15) |
| Kweichow Moutai 600519.SH | 90.26 | 47.86 | 37.31 | 10.8 | ✅ | −0.49 | **7.32** | 14.11 | **PASS 8/8 on stockanalysis basis** — basis-dependent: 09-15's yfinance-basis yield was 3.67% (fail). FY25 revenue −1.2%, FCF −33% YoY. Not independently reconciled |
| Proya 603605.SH | 73.11 | 17.60 | 57.81 | 18.4 | ✅ | −3.20 | 7.66 | 11.39 | Quant PASS; **qualitative FAIL carried from 09-15 — not investable**. FY25 revenue −1.7%; TTM NI > TTM operating income (non-operating gain suspected) |
| PDD | 56.32 | 20.43 | **14.92** | 49.0 | ✅ | −4.56 | 14.36 | 3.36 | **FAIL — ROIC only, by 0.08pp.** Basis-dependent: 09-15 used ROE 22.75% as proxy (net-cash denominator distortion). FY25 growth slowed to +9.6%, FCF −12% |
| NetEase NTES | 67.15 | 27.88 | 368†| **5.3** | ✅ | −3.76 | 9.50 | 9.34 | FAIL — Rev CAGR only (5th round) |
| Trip.com TCOM | 80.05 | 36.90 | **7.57** | 46.1‡ | ✅ | −4.61 | 8.32 | 10.69 | FAIL — ROIC only (declining: 10.87→7.57) |
| WuXi Biologics 2269.HK | 47.47 | 21.20 | **13.88** | 12.6 | ✅ (thin) | −1.14 | **2.35** | **23.31** | FAIL — ROIC, FCF yield, EV/EBIT |
| Infosys INFY | **29.68** | 16.37 | 41.69 | **3.4** | ✅ | −0.49 | 8.31 | 9.93 | FAIL — GM, Rev CAGR |
| TCS TCS.NS | 40.65 | 18.22 | 66.26 | **5.8** | ✅ | −0.54 | 5.99 | 10.49 | FAIL — Rev CAGR only (GM narrow: 40.31% on FY26) |
| Asian Paints | 43.53 | 12.81 | 25.49 | **1.1** | ✅ | −0.68 | **2.47** | **36.16** | FAIL — Rev CAGR, FCF yield, EV/EBIT |
| Pidilite | 54.79 | 17.20 | 34.88 | **7.4** | ✅ | −1.03 | **1.49** | **43.22** | FAIL — Rev CAGR, FCF yield, EV/EBIT |
| Divi's Labs | 61.24 | 26.05 | 19.67 | 10.8§ | ✅ | −0.81 | **0.09** | **70.77** | FAIL — FCF yield, EV/EBIT (CAGR flattered by FY23 trough) |
| ITC ITC.NS | 58.28 | 25.94 | 35.59 | **3.6** | ✅ | −0.87 | 4.98 | 12.38 | FAIL — Rev CAGR only (unchanged) |
| Info Edge NAUKRI.NS | 56.39 | 47.40◊ | **2.56** | 11.9 | ✅ | −3.6 | **1.26** | **67.21** | FAIL — ROIC, FCF yield, EV/EBIT |
| Persistent PERSISTENT.NS | **31.68** | 12.24 | 29.80 | 20.9 | ✅ | −0.49 | **1.34** | **33.18** | FAIL — GM, FCF yield, EV/EBIT |
| MercadoLibre MELI | 47.75 | **5.30** | **14.20** | 38.9 | ✅ | 1.92 | 12.93 | **35.57** | FAIL — NM, ROIC, EV/EBIT (FCF likely inflated by credit/payables float) |
| WEG WEGE3.SA | **33.14** | 15.58 | 38.28 | 10.9 | ✅ | −0.35 | **1.92** | **27.66** | FAIL — GM, FCF yield, EV/EBIT |
| B3 B3SA3.SA | 95.10 | 49.45 | 26.47 | **3.46** | ✅ (lumpy) | −0.03 | 5.10 | 16.39 | FAIL — Rev CAGR only (unchanged) |

† NetEase ROIC is a net-cash-denominator artifact. ‡ Trip.com CAGR uses COVID-depressed FY22 base. § Divi's FY23 base is a trough. ◊ Net margin inflated by non-operating items (Info Edge stake gains; YMM treasury income).

## ✅ Qualified Quality List — 5 quantitative passes, 4 actionable
- **Tencent (0700.HK)** — clean 8/8, continuing.
- **ANTA Sports (2020.HK)** — clean 8/8, continuing.
- **Full Truck Alliance (YMM)** — clean 8/8, continuing; net-margin quality flag.
- **Kweichow Moutai (600519.SH)** — *re-entered* on stockanalysis.com FCF yield (7.32%); fragile, since the yfinance-basis figure failed on 09-15. Reconcile the FCF definition before `/new-position`.
- ~~Proya (603605.SH)~~ — quant pass but qualitative FAIL; excluded.
- **PDD dropped out** (ROIC 14.92%, 0.08pp miss; ROE-proxy basis would pass). Treat as a priority re-check, not a clear fail.

**Near-misses (single filter):** PDD (ROIC), NetEase, TCS, ITC, B3 (Rev CAGR), Trip.com (ROIC, worsening).

## Step 4 — Data gaps
- yfinance `fetch_fundamentals`: missing EBIT/FCF/marketCap rows on most names (above); SBC/buyback fields UNKNOWN on all (not needed for Phase 01).
- Net Debt/EBITDA derived, not site-published. TTM FCF on Asian Paints / Divi's / ITC pages shows "-"; statistics-page figure equals FY26 FCF.
- Red flags (delisting, restatement, acquisition, one-offs) not searched beyond stockanalysis.com pages.
- Moutai FCF-yield basis conflict and PDD ROIC-vs-ROE basis conflict unresolved.

## Glossary
Terms (see [glossary.md](../framework/glossary.md)): ROIC, FCF yield, EV/EBIT, Net Debt/EBITDA, Revenue CAGR, Gross/Net margin, ADR, Phase 01 gate, near-miss, stockanalysis.com basis vs yfinance basis (two data providers computing the same metric differently).

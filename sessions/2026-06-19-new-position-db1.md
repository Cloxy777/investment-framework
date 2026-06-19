# NEW POSITION — Deutsche Börse AG (DB1.DE) — 2026-06-19

**Task type:** NEW POSITION
**Date:** 19 Jun 2026
**10Y US Treasury Yield:** 4.451% (`^TNX` close, 18 Jun 2026 — most recent trading day; `^TNX`'s own `regularMarketPrice` and `previousClose` agree exactly, both internally consistent)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current DB1 portfolio weight:** 0% — not currently held (confirmed against [holdings.md](../portfolio/holdings.md))
**Sector:** Germany/EU Market Infrastructure — cash-equities exchange (Xetra), derivatives exchange and clearing (Eurex), post-trade settlement/custody (Clearstream), investment-management software and indices (SimCorp, STOXX, ISS — "Investment Management Solutions" segment)
**Currency:** All calculations in EUR. The Rate Environment Gate benchmarks against the **US** 10Y Treasury per framework convention; the DCF WACC uses the **German 10Y Bund** as risk-free rate for currency-consistent valuation of EUR cash flows (same convention as the SGE session's UK Gilt choice).

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **EUR 244.00** | `yfinance` `Ticker('DB1.DE').info['currentPrice']`, cross-checked against `regularMarketPrice` (244.00) and `previousClose` (243.10) — internally consistent small day-over-day move; intraday range 242.00–244.70 |
| 52-week range | EUR 200.10 – 279.10 | `yfinance` `fiftyTwoWeekLow`/`fiftyTwoWeekHigh` |
| Analyst consensus PT (12-month) | Mean **286.08**, median 296.50, range 240–310, 12 analysts; rating: "buy" | `yfinance` `targetMeanPrice`/`targetMedianPrice`/`targetLowPrice`/`targetHighPrice`/`recommendationKey` |
| Shares outstanding | **182,105,935** | `yfinance` `sharesOutstanding` |
| Market cap (computed) | **EUR 44,433.8M** | 182,105,935 × €244.00 = €44,433,847,940, matches `yfinance`'s own `marketCap` field (€44,433,850,368) to within rounding |
| Beta (info field, raw) | **0.28** | `yfinance` `info['beta']` — structurally low, flagged below; not used directly for WACC (see §8) |
| EUR/USD | 1.1469204 | `yfinance` `Ticker('EURUSD=X').info['regularMarketPrice']` |
| German 10Y Bund | 2.93% | WebSearch (TradingEconomics, 19 Jun 2026) — used as DCF risk-free rate |

No price-staleness issue this session — `currentPrice`, `regularMarketPrice`, and the intraday day-range are mutually consistent and dated today.

---

## 2. Data Gathered (Phase 01 + Phase 02 Inputs) & Gaps Flagged

### FY2025 results (year ended 31 Dec 2025) — `yfinance` annual financials/cashflow/balance sheet, pulled fresh this session

| Metric | FY2025 | FY2024 | FY2023 | FY2022 |
|---|---|---|---|---|
| Total Revenue | €7,381.0M | €7,023.0M | €6,096.1M | €5,225.3M |
| Gross Profit | €4,204.0M | €4,096.0M | €3,607.1M | €2,995.3M |
| **EBIT** | **€3,049.0M** | €2,928.0M | €2,565.4M | €2,190.2M |
| EBITDA | €3,550.0M | €3,424.0M | €2,983.9M | €2,545.8M |
| Net Income | €1,995.0M | €1,948.0M | €1,724.0M | €1,494.4M |
| Basic EPS | €10.90 | €10.60 | €9.35 | €8.14 |
| **Free Cash Flow** | **€2,430.0M** | €2,050.0M | €2,281.2M | €2,158.4M |
| Operating Cash Flow | €2,810.0M | €2,411.0M | €2,549.1M | €2,483.6M |
| CapEx | €380.0M | €361.0M | €267.9M | €325.2M |

### Margin basis — judgment call carried forward from the screening session

`yfinance`'s `info` snapshot fields (`grossMargins` 81.23%, `profitMargins` 27.26%, TTM basis) diverge sharply from a naive `Gross Profit / Total Revenue` computed off the annual financials statement (€4,204M / €7,381M = **56.96%**, not 81.23%). Investigated this session: Deutsche Börse's own FY2025 results press release describes **"net revenue" of €6,026M** (2024: €5,829M) as the operative management metric — distinct from the gross "Total Revenue" line in the income statement, consistent with an exchange/CCP business where reported revenue includes pass-through items (Clearstream collateral/treasury flows) that a "net revenue" framing strips out, the same pattern as the balance-sheet cash-bucket artifact below. This is the same basis the screening session already used (its 81.23%/27.26% figures match `info` exactly). **Per Rule 6 ("value the underlying business, not the accounting statements") and consistency with the already-completed Phase 01 pass, the `info` TTM-basis margins are retained as primary.** Flagged transparently — not fully reconciled to a precise net-revenue-based gross margin calculation, since DB1's segment-level cost-of-net-revenue breakdown was not sourced (Rule 0: not invented).

### Net debt — balance sheet cash-bucket artifact (same DB1-specific pattern flagged in the screening session, re-verified)

`yfinance`'s "Cash, Cash Equivalents And Short Term Investments" balance sheet line (€205,142M for FY2025) is a CCP/client-settlement-balance figure, not company cash — confirmed again this session (same order of magnitude as the screening session's €205.1B reading). The narrower **"Cash And Cash Equivalents"** line (€2,078M) is used instead, consistent with the HKEX/DB1 precedent.

```
Net Debt (narrow cash basis) = Total Debt − Cash And Cash Equivalents
                              = €8,136.0M − €2,078.0M = €6,058.0M
```

Cross-check: `yfinance`'s own pre-computed "Net Debt" balance-sheet line shows €5,537.0M for FY2025 — likely netting against a different (broader, but not the €205B CCP-bucket) cash/investment figure. The narrow, manually-computed €6,058.0M is used as primary for consistency with the explicit "Cash And Cash Equivalents"-only convention; the €5,537.0M figure is shown as a cross-check, not used (would make Net Debt/EBITDA only 1.56×, even more comfortably inside the gate — using the more conservative €6,058.0M figure throughout).

No more-current quarterly balance sheet was available — `quarterly_balance_sheet` shows `NaN` for Net Debt, Total Debt, and Total Debt-adjacent lines at the most recent quarter (2026-03-31); only "Cash And Cash Equivalents" has a Q2-2025 data point (€1,710.7M) and nothing more recent. **FY2025 year-end (31 Dec 2025) is therefore the most current net debt figure available** and is used throughout this session for the EV bridge and DCF equity bridge — flagged as a data gap (no H1 FY26 balance sheet to refresh against, unlike the SGE session which had one).

### Revenue history (3yr CAGR) — re-verified

```
3yr CAGR = (7,381.0 / 5,225.3)^(1/3) − 1 = 12.20%   (FY2022 €5,225.3M → FY2025 €7,381.0M)
```
Matches the screening session's figure exactly.

### EPS history (Fast Grower / PEG test) — re-verified with fresh annual financials

| Year | Basic EPS | YoY growth | >15%? |
|---|---|---|---|
| FY2022 → FY2023 | €8.14 → €9.35 | +14.86% | ❌ No |
| FY2023 → FY2024 | €9.35 → €10.60 | +13.37% | ❌ No |
| FY2024 → FY2025 | €10.60 → €10.90 | +2.83% | ❌ No |

None of the last 3 years clears 15% — **not a Fast Grower**. PEG's 15% weight redistributes to EV/EBIT (40% total).

### Forward PE — the `0y`-vs-`+1y` trap (same issue the SGE session flagged, re-verified independently for DB1)

```
yfinance fiscal-year fields:
  lastFiscalYearEnd  = 2025-12-31  (already reported — FY2025 actual EPS 10.90)
  nextFiscalYearEnd  = 2026-12-31  (next FY — this is what "Forward PE" should use)

yfinance eps_trend (Ticker('DB1.DE').eps_trend):
  0y  (FY2026E, next fiscal year)        EPS estimate = 12.39925  <- correct "Forward PE" basis
  +1y (FY2027E, fiscal year after next)  EPS estimate = 13.30862  <- what yfinance's raw forwardPE field actually uses

Forward PE = 244.00 / 12.39925 = 19.68×
(yfinance's own `forwardPE` field gives 18.33× = 244.00/13.30862 — this is the +1y-basis figure, NOT used)
```

Verified the `info['forwardEps']` field (13.30862) matches the `+1y` row exactly, confirming the trap: yfinance's pre-computed `forwardPE` (18.33×) is one fiscal year too far out. The `0y`-basis Forward PE (**19.68×**) is used throughout this session, including for all 8 peer comparables in §8 (each independently checked the same way — see below).

### Net margin, ROIC, gross margin — re-verified

| Metric | Value | Threshold | Source |
|---|---|---|---|
| Gross margin | 81.23% | >40% | `yfinance` `info['grossMargins']` (TTM) |
| Net margin | 27.26% | >12% | `yfinance` `info['profitMargins']` (TTM) |
| ROE (ROIC proxy) | 19.21% | >15% | `yfinance` `info['returnOnEquity']` |

All three essentially unchanged from the screening session (small drift from intervening days of trading/FX, not a material change).

### Peer comparables (Rule 5) — 8 candidates pulled, 5 pass the revenue-scale band

Exchanges/clearinghouses pulled via `yfinance`: LSEG (London Stock Exchange Group), ICE (Intercontinental Exchange), CME (CME Group), NDAQ (Nasdaq Inc), HKEX (0388.HK), SGX (S68.SI), Euronext (ENX.PA), Cboe (CBOE).

**Currency/unit check (Rule 0 discipline):** LSEG's price (`info['currency']` = GBp, pence) and its `financialCurrency` (GBP, pounds) are different units — the same trap flagged in the SGE session. Revenue (£9,346M) and EBIT are in GBP; price (8,460.0) is in GBp. Naively dividing price by a GBP-denominated EPS would overstate LSEG's PE by 100×; corrected by converting price to GBP (÷100) before computing. All 7 other peers have matching `currency`/`financialCurrency` fields — no unit mismatch.

| Company | EV/EBIT | Forward PE (0y basis, verified) | Revenue (local) | Revenue (EUR-equiv) | % of DB1's €7,381M | In Rule-5 ±50% band? |
|---|---|---|---|---|---|---|
| LSEG (LSEG.L) | 24.25× | 17.83× | £9,346M | €10,784.2M | 146% | ✅ |
| ICE (ICE) | 19.44× | 16.45× | $10,435M | €9,098.3M | 123% | ✅ |
| CME Group (CME) | 17.45× | 20.07× | $6,743.6M | €5,879.7M | 80% | ✅ |
| Nasdaq (NDAQ) | 23.80× | 20.86× | $5,419M | €4,724.8M | 64% | ✅ |
| Cboe (CBOE) | 16.81× | 18.12× | $4,792M | €4,178.1M | 57% | ✅ |
| HKEX (0388.HK) | 7.03× | 24.80× | HK$30,151M | €3,354.7M | 45% | ❌ too small |
| Euronext (ENX.PA) | 16.85× | 18.45× | €1,887.2M | €1,887.2M | 26% | ❌ too small |
| SGX (S68.SI) | 30.52× | 35.14× | S$1,424.6M | €962.2M | 13% | ❌ too small |
| **Median (5 in-band peers)** | **19.44×** | **18.12×** | | | | |
| Median (all 8, cross-check) | 18.45× | 19.26× | | | | |

FX cross rates used: EUR/USD 1.1469204, EUR/GBP 0.86664, EUR/HKD 8.9878, EUR/SGD 1.4805 (all `yfinance`, live).

**Rule 5 compliance:** exactly 5 peers (LSEG, ICE, CME, NDAQ, CBOE) sit within ±50% of DB1's revenue scale — the framework's stated minimum. HKEX, Euronext, and SGX are all materially smaller (13–45% of DB1's revenue) and excluded from the primary median, shown only as a transparency cross-check (the all-8 median is close to the in-band median regardless — 18.45× vs 19.44× EV/EBIT, 19.26× vs 18.12× Forward PE — so this exclusion is not a major swing factor here, unlike the SGE session's Workday-driven distortion).

### 10-year historical PE range (WebSearch — not as time-sensitive as live price, per the task brief)

| Source | Low | High | Average |
|---|---|---|---|
| wisesheets.io (year-by-year table, 2016–2025) | **11.21×** (2016) | **25.60×** (2019) | **20.82×** |

Cross-checked directionally against a macrotrends-derived WebSearch summary (2016 low ~8.8–17.6×, 2019/2020 high ~24–25×, recent years clustering 18–25×) — broadly consistent in shape (2016 as the trough year, 2019–2020 as the peak years), though the two sources don't agree to the decimal. The wisesheets table is used as primary since it provides one clean PE-per-year reading across exactly 10 years (2016–2025) rather than a search-engine-summarized range. **Flagged explicitly:** 2016's reading (11.21×) is a clear outlier against every other year in the series (18–26×) — not adjusted or excluded per Rule 0 ("never invent or estimate"; the as-reported number is used as-is), but it does pull the 10-year average down somewhat versus what a "normal year" average would show.

### WACC inputs

| Input | Value | Source |
|---|---|---|
| Risk-free rate (German 10Y Bund) | 2.93% | WebSearch (TradingEconomics, 19 Jun 2026) |
| DB1's own beta (raw, `yfinance`) | 0.28 | Too low to use directly — see §8 judgment call |
| Peer-set average beta (6 exchanges) | 0.626 | `yfinance` betas: LSEG 0.381, ICE 0.922, CME 0.244, NDAQ 0.974, ENX.PA 0.84, CBOE 0.395 |
| Beta actually used in WACC (see §8) | **0.92** (ICE-comparable) | Judgment call — see §8 |
| Equity Risk Premium | 5.0% (standard framework assumption) | Standard convention |
| Cost of debt (pre-tax, estimate basis) | ~3.5% (AA-rated issuer, consistent with disclosed bond coupons ~3.875%) | WebSearch |
| German corporate tax rate (combined) | ~26.4% | Standard convention |
| Capital structure (market-based) | Equity 84.52% / Debt 15.48% | Computed from market cap (€44,433.8M) and total debt (€8,136.0M) |
| Credit rating | **S&P AA−**, short-term A-1+ | Deutsche Börse IR website — very high quality, low credit risk |

### Data Gaps flagged

1. **Gross margin basis** — `info`'s TTM `grossMargins` (81.23%) vs. a naive computation off the annual financials statement (56.96%) diverge because DB1's own disclosed "net revenue" concept (€6,026M FY2025) differs from the income statement's gross "Total Revenue" line (€7,381M); the precise segment-level cost-of-net-revenue breakdown needed to fully reconcile this was not sourced. `info`-basis figures used as primary per Rule 6 and for consistency with the already-passed Phase 01 screening session.
2. **No more-current balance sheet than FY2025 year-end (31 Dec 2025)** — `quarterly_balance_sheet` returns `NaN` for Net Debt/Total Debt at the most recent quarter (31 Mar 2026); only a single, isolated Cash-and-equivalents data point exists for an earlier interim quarter. FY2025 year-end net debt is used throughout — flagged as 5.5 months stale relative to the live price.
3. **TTM EBIT could not be cleanly computed** — `quarterly_financials` is missing the Q3 2025 EBIT data point entirely (gap in the series), so a true trailing-twelve-month EBIT (which would have included Q1 2026's stronger €882M quarter) was not built; FY2025 full-year EBIT (€3,049.0M, all 4 quarters complete) used as the most reliable available basis instead.
4. **10-year historical PE range** sourced via WebSearch (wisesheets.io) rather than a primary financial database — cross-checked directionally against a second source (macrotrends-derived) but the two don't agree to the decimal; flagged per Rule 0 since this figure was not independently verified against DB1's own filings.
5. **Cost of debt** (pre-tax ~3.5%) is an estimate anchored to DB1's disclosed bond coupon range, not a directly observed effective rate on the FY2025 balance sheet — flagged as the least precisely sourced WACC input (see §8 for how this is mitigated).

---

## 3. Phase 01 — Quality Gate (re-verified with fresh data)

| Check | DB1 Value | Threshold | Result |
|---|---|---|---|
| Gross margin | 81.23% (TTM, `info` basis — see Data Gap 1) | >40% | ✅ PASS |
| Net margin | 27.26% (TTM, `info` basis) | >12% (valuation-scoring.md) | ✅ PASS |
| ROE (ROIC proxy) | 19.21% | >15% | ✅ PASS |
| Revenue CAGR 3yr | 12.20% | >8% (valuation-scoring.md) | ✅ PASS |
| FCF positive 3+ consecutive years | Yes — €2,158.4M / €2,281.2M / €2,050.0M / €2,430.0M (FY2022–25, all positive) | required | ✅ PASS |
| **Net debt/EBITDA** | **1.706×** (€6,058.0M narrow-cash-basis net debt ÷ €3,550.0M FY2025 EBITDA) | <2.5× (valuation-scoring.md) | ✅ PASS |
| FCF yield | 5.469% (€2,430.0M ÷ €44,433.8M market cap) | >4% | ✅ PASS |
| EV/EBIT | 16.56× (EV €50,491.8M [= mkt cap + net debt] ÷ EBIT €3,049.0M) | <20× | ✅ PASS |

**Gate result: PASS — 8/8 metrics pass cleanly, no judgment calls required to reach a pass** (a cleaner outcome than the SGE precedent, which needed three explicit judgment calls). All figures sit comfortably inside their thresholds rather than at the margin, and are consistent with — slightly improved from, in the case of Net Debt/EBITDA (1.706× now vs 1.86× in the screening session, reflecting the lower current EUR debt level) — the screening session's numbers. **Proceeding to Rate Environment Gate and Phase 02.**

---

## 4. Fast Grower (Upgrade 3 — PEG) Determination

EPS growth was +14.86% (FY22→23), +13.37% (FY23→24), and +2.83% (FY24→25) — **none** of the last 3 years clears the >15% bar, let alone 3 consecutive years. **Not a Fast Grower.** PEG's 15% weight redistributes to EV/EBIT (40% total) per the Final Score Formula.

---

## 5. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**

```
Forward PE = 19.68×   (0y / FY2026E basis — see §2 for the 0y-vs-+1y resolution)
EY     = 1 ÷ 19.68 = 5.082%
Spread = EY − 10Y Treasury = 5.082% − 4.451% = +0.631%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.631% falls well short of the threshold) → **+5 additive** (Step 1).

**Step 2 — Rate Regime Modifier**
10Y = 4.451% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for DB1 = 5 (Step 1) + 5 (Step 2) = +10**

---

## 6. Phase 02 — Full Score Calculation

**FCF Yield — 40% weight**

```
FCF Yield = FCF / Market Cap = €2,430.0M / €44,433.8M = 5.469%

FCF_Score = clamp(100 × (1 − 5.469/10), 0, 100) = clamp(100 × 0.4531, 0, 100) = 45.31
```
→ Contribution: 45.31 × 0.40 = **18.124**

**EV/EBIT — 40% weight (PEG not applicable, redistributed from 25%)**

```
Market Cap = €44,433.8M
Net Debt   = €6,058.0M  (narrow cash basis, FY2025 — see §2)
EV         = €44,433.8M + €6,058.0M = €50,491.8M

EV/EBIT = €50,491.8M / €3,049.0M (FY2025 EBIT) = 16.56×

EV/EBIT_Score = clamp((16.56 − 12) / 23 × 100, 0, 100) = clamp(19.83, 0, 100) = 19.83
```
→ Contribution: 19.83 × 0.40 = **7.930**

**Forward PE (PRIMARY formula — 10yr low/high range available) — 20% weight**

```
Forward PE   = 19.68×
10yr Low PE  = 11.21×
10yr High PE = 25.60×

FwdPE_Score (raw) = clamp((19.68 − 11.21) / (25.60 − 11.21) × 100, 0, 100)
                  = clamp(8.47/14.39 × 100, 0, 100) = clamp(58.85, 0, 100) = 58.85
```

**Historical PE Modifier (Upgrade 2)**

```
Deviation from 10yr avg = (19.68 − 20.82) / 20.82 = −5.48%
```
Within ±10% → modifier = **0** (no adjustment).

```
FwdPE_Score (adjusted) = clamp(58.85 + 0, 0, 100) = 58.85
```
→ Contribution: 58.85 × 0.20 = **11.770**

**PEG — not applicable (redistributed to EV/EBIT)**

### Final Score

```
Raw weighted score = (45.31 × 0.40) + (19.83 × 0.40) + (58.85 × 0.20)
                    = 18.124 + 7.930 + 11.770
                    = 37.824

+ Rate Regime Modifier (5 + 5) = 37.824 + 10 = 47.824
```

Boundary rule: 47.824 → nearest 0.1 → **Final Score = 47.8**

---

## 7. Final Score & Action

# Final Score: 47.8 → Action Table band: 30.0–49.9 (Cheap) → BUY — Standard position 3–5% of portfolio

DB1 sits in the upper-middle of the "Cheap" band — meaningfully cheaper than Fair Value (50.0–69.9) but not deep enough to clear into "Very Cheap" (0.0–29.9). Two of the three sub-scores (FCF yield 45.31, EV/EBIT 19.83) pull the score down toward cheap; the Forward PE sub-score (58.85) is the main drag, sitting almost exactly at the midpoint of DB1's own 10-year PE range — i.e., today's multiple isn't unusually cheap *or* expensive relative to DB1's own trading history, even though the absolute EV/EBIT and FCF yield levels look attractive against the framework's universal thresholds. The full +10 Rate Modifier (both Step 1 and Step 2 firing) also pulls the score up materially from what the raw fundamentals alone would suggest (37.8 raw vs. 47.8 final).

### Sanity check

A regulated, AA−-rated, 19.2%-ROE exchange/clearing network with five-decade-plus liquidity moats trading at a Forward PE (19.68×) almost exactly at its own 10-year average (20.82×) is a reasonably priced, not a deeply mispriced, security — consistent with landing in "Cheap" rather than "Very Cheap." This is a materially different signal than Sage's (FwdPE sub-score 0.0, sitting *below* its own 10-year low) — DB1's cheapness case rests more on its absolute multiples (EV/EBIT, FCF yield) clearing the framework's universal thresholds comfortably than on being unusually cheap by its own historical standard.

---

## 8. Fair Value & Order Setup

### Step 1 — Fair Value (Blended)

**Method A: DCF (3 scenarios, Rule 2/7)**

**WACC — judgment call, flagged explicitly.** DB1's own raw beta (0.28) is structurally too low to use directly: combined with the low German risk-free rate (2.93%), it produces a Cost of Equity near 4% and a WACC near 5.5%, which — tested explicitly — fails Rule 4's sanity checks badly. At WACC 5.52–5.94% (DB1's own beta, and separately the AlphaSpread-published 5.94% WACC, were both tested), even the **Bear** case DCF EV comes out at 1.6–1.7× DB1's actual current EV (€50,491.8M), and Base/Bull cases reach 2.4–4.2× — clearly outside a defensible range, and Terminal Value weight in the Bull case breaches 75–85%, which Rule 4 flags as requiring remediation. Extending the Stage 2 fade period (Rule 4's stated remedy for high TV weight) was tested and made the *absolute* EV problem worse, not better, because more years compounding at a still-too-low discount rate before the terminal fade only adds more present value. The root cause is mathematical, not a Stage-2-length issue: a WACC this close to the 2.5% terminal growth rate makes the Gordon Growth terminal multiple (`1/(WACC−g)`) explode.

**Resolution:** rather than DB1's own raw beta (0.28) or the peer-set simple average (0.626) — both tested and found to still fail sanity at the Base case — this session uses **beta = 0.92**, matching ICE (Intercontinental Exchange), the most business-model-comparable large global derivatives-exchange-and-clearing peer in the comp set (also the second-most revenue-scale-comparable peer at 123% of DB1's revenue). This is the same kind of explicit, flagged judgment call the SGE session made (sector-average beta over the company's own too-low raw beta) — here taken one step further, to a specific high-beta-end peer rather than a simple sector average, because even the simple average (0.626 → WACC ~5.5%) still failed the sanity check.

```
Cost of Equity (beta=0.92) = 2.93% + 0.92×5.0% = 7.53%
WACC = 0.8452×7.53% + 0.1548×2.576%(after-tax cost of debt) = 6.76%
```

Base FCF = €2,430.0M (FY2025). 3-stage DCF: Stage 1 (yrs 1–5) explicit growth; Stage 2 (yrs 6–10) growth fades linearly from the Stage-1 rate to the 2.5% terminal rate; Stage 3 Gordon-growth terminal value off year-10 FCF. Stage-1 growth rates are anchored to DB1's own disclosed medium-term guidance: management's "Horizon 2026" strategy targets ~10% net revenue CAGR (7% organic + ~3% from the SimCorp acquisition) and ~11% EBITDA CAGR — this session uses the **organic-only** component (7% Base case) rather than the full inorganic-inclusive guidance, to avoid assuming continued successful M&A as a base-case input (Rule 6: normalize, don't assume future deal-making).

| Scenario | WACC | Yrs 1–5 growth | PV(FCF Yrs 1–10) | PV(Terminal Value) | EV | TV weight |
|---|---|---|---|---|---|---|
| Bear | 7.76% | +5% | €20,977.2M | €33,792.6M | **€54,803.0M** | 62.0% |
| Base | 6.76% | +7% | €23,889.1M | €52,609.7M | **€76,498.8M** | 68.8% |
| Bull | 5.76% | +9% | €27,520.9M | €86,044.3M | **€113,565.2M** | 75.8% |

Bear case passes the <75% terminal-value-weight sanity check comfortably (62.0%); Base is moderately elevated (68.8%); **Bull sits right at the 75% threshold (75.8%)** — flagged per Rule 4, though not remediated further since the scenario-weighting (25% Bull) limits its influence on the final blend, and pushing growth any lower for Bull would compress the Bull/Base/Bear spread to the point of not reflecting genuine scenario dispersion.

```
PW DCF EV = 0.25×113,565.2 + 0.50×76,498.8 + 0.25×54,803.0 = 80,341.5M

DCF Equity Value = €80,341.5M − Net Debt €6,058.0M (FY2025 year-end, see §2) = €74,283.5M
DCF FV/share = €74,283.5M / 182.105935M shares = €407.91
```

Even the Bear-case EV (€54,803.0M) sits modestly above the current EV (€50,491.8M, +8.5%) — the DCF supports mild undervaluation even under conservative assumptions, though by a much narrower margin than typically seen in a "Very Cheap" name (compare the SGE precedent, where even Bear-case EV cleared current EV by a wide margin).

**Method B: Comparable Multiples — using the 5 in-band peers (Rule 5)**

```
EV/EBIT reversion: median in-band peer EV/EBIT (19.44×, between ICE 19.44x... actually the median of
                    {24.25, 19.44, 17.45, 23.80, 16.81} = 19.44×, i.e. ICE itself) × DB1 EBIT (€3,049.0M)
                  = implied EV €59,272.6M − Net Debt €6,058.0M = Equity €53,214.6M
                  ÷ 182.105935M shares = €292.22

Forward PE reversion: median in-band peer Forward PE (18.12×, Cboe, 0y basis) × DB1's own Forward EPS (€12.39925)
                     = €224.67

Multiples avg = (€292.22 + €224.67) / 2 = €258.45
```

```
Blended FV = 40% × DCF FV/share + 60% × Multiples avg
           = 0.40 × €407.91 + 0.60 × €258.45
           = €163.16 + €155.07
           = €318.23
```

**Cross-check vs external estimates.** Blended FV (€318.23) sits **+11.2%** above the `yfinance`-sourced analyst consensus mean (€286.08) and **+7.3%** above the consensus median (€296.50) — a moderate, not extreme, divergence (narrower than the SGE re-run's +20.9% gap), giving reasonable external corroboration for the blended figure without being a near-exact match.

---

### Step 2 — Buy Price & R/R Gate

Score 47.8 falls in the **30.0–49.9 (Cheap)** band → MoS 25–30%; DB1's ROIC (19.21%, "ROE" proxy) sits in Rule 8's **"Standard quality business (ROIC 15–20%)" tier** (not the ">20yr ROIC>15%, proven compounder" tier, which DB1's specific multi-decade ROIC history was not separately verified to confirm) → **30% MoS** used, the higher/more conservative end of Rule 8's mapping for this tier:

```
Buy Price ceiling = Blended FV × (1 − 0.30) = €318.23 × 0.70 = €222.76
```

**Current price (€244.00) is ABOVE the Buy Price ceiling (€222.76)** — implied MoS at current price = 1 − (244.00/318.23) = **23.33%**, below the 25–30% required band (checked across the full band: even at the loosest 25% MoS, the ceiling is €238.67, still below the current price). Per Step 2: Score 30.0–49.9 → "Approaching buy price → **Set limit order**," not enter-now.

**Step 6 (Risk/Reward) — tested at the limit-order entry price (€222.76)**

```
Primary Sell Target = Blended FV = €318.23   (per Step 3 — base-case blended FV, not the bull-case trim target)

R/R = (Sell Target − Entry) / (Entry − Stop Loss)
```

| Stop band (Score 30.0–49.9: 25–30% max loss) | Stop price | R/R |
|---|---|---|
| 25% (tight end) | €167.07 | 1.71:1 |
| 27.5% (midpoint) | €161.50 | 1.56:1 |
| 30% (loose end) | €155.93 | 1.43:1 |

**None of the three points in the standard stop band clear the 2:1 minimum.** Solved algebraically: hitting exactly 2:1 from the €222.76 entry would require a stop at €175.02 — a 21.4% max loss, *tighter* than even the aggressive end of the standard 25–30% band, and there is no DB1-specific risk characteristic (unlike SGE's genuinely low, well-corroborated beta) that would justify tightening the stop below the standard band. The binding constraint here is the **numerator** (upside to target is only +42.9% from this entry, €95.47 on a €222.76 base), not the stop placement — DB1's blended FV simply isn't far enough above a defensible entry price to generate a 2:1 setup at any reasonable stop.

**Per fair-value-methodology.md Step 6: "If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely."** Tighter-stop and lower-entry options were both tested and do not resolve this (see below) — **R/R gate FAILS. Do not enter.**

**Supplementary checks performed (all confirm the R/R gate failure is robust, not an artifact of one input choice):**
- At the current price (€244.00, informational only — already established as above the MoS ceiling): R/R ranges 1.22–1.52:1 across the 20–25% stop band typically used for higher-conviction entries — still fails.
- At the loosest MoS entry (25%, €238.67): R/R ranges 1.11–1.33:1 across the standard stop band — still fails, and worse than the 30%-MoS entry, because the lower MoS narrows the gap to the sell target even though the entry itself is slightly cheaper than the current price.
- Using the **Bull-Case Trim Target** (€352.09 = 90% of Bull Blended FV €391.21) instead of the Primary Sell Target as the basis for R/R would produce a passing 1.94–2.32:1 — **not used**, since the framework's Step 6 explicitly pairs R/R against the *Primary* Sell Target (base-case Blended FV), and substituting the bull-case number to manufacture a pass would be exactly the kind of black-box rule-bending the framework's "no black-box outputs" rule prohibits.

---

### Order Setup Checklist

```
[x] Valuation Score:                         47.8   (Cheap band — 30.0-49.9, upper-middle)
[x] DCF Fair Value (PW, scenario-weighted):  EUR 407.91
[x] Multiples-Based Fair Value:              EUR 258.45
[x] Blended Fair Value:                      EUR 318.23
[x] Margin of Safety %:                      30% (Rule 8, Standard quality ROIC 15-20% tier) -> Buy Price ceiling EUR 222.76;
                                              current price (EUR 244.00) is ABOVE the ceiling (23.33% implied MoS, below the
                                              25-30% required band) -> Set limit order indicated, NOT enter-now
[x] BUY PRICE (limit order, if placed):      EUR 222.76
[x] PRIMARY SELL TARGET (at FV):             EUR 318.23
[x] BULL-CASE TRIM TARGET:                   EUR 352.09  (shown for completeness; NOT used for the R/R gate)
[ ] STOP LOSS:                               FAILS GATE -- no stop in the standard 25-30% band clears 2:1 (see below)
[ ] Risk/Reward Ratio:                       1.43-1.71:1 across the standard stop band -- FAILS the 2:1 minimum
[ ] Max $ Risk / POSITION SIZE:              NOT COMPUTED -- order setup does not proceed past the R/R gate
[x] Thesis invalidation triggers:            see SS9 (not applicable to sizing since no entry is recommended)
```

**Per Rule 6 of fair-value-methodology.md ("R/R Ratio... Minimum acceptable: 2:1... If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely"), this session does not proceed to position sizing.** A hypothetical position size was computed for transparency only (not a recommendation):

```
[Hypothetical, NOT a recommendation] At buy price EUR 222.76, stop EUR 161.50 (27.5% midpoint):
  Risk per share = EUR 61.26
  Max $ Risk (1.5% of $53,659.11 portfolio) = $804.89 -> EUR 701.78 (at EUR/USD 1.1469204)
  Shares (risk-based) = 701.78 / 61.26 = 11.5 shares
  Position size = 11.5 x EUR 222.76 = EUR 2,551.93 = $2,926.86 (~5.45% of portfolio)
```
This would sit within the Score 30.0–49.9 band's 3–5% allocation cap (at the very top of it) and far inside the Upgrade 7 15% hard cap — **but is not actionable, since the R/R gate that gates entry into position sizing in the first place has already failed.**

---

## 9. Recommendation

# **WATCHLIST ONLY — DO NOT ENTER. Score 47.8 (Cheap) clears the bar for a Standard position (3–5%) on valuation alone, but the Risk/Reward gate fails (1.43–1.71:1 across the full standard stop band, vs. the framework's hard 2:1 minimum) at every entry price tested, including the MoS-implied limit-order price (EUR 222.76) and the current live price (EUR 244.00). Per fair-value-methodology.md Step 6, a failing R/R ratio means "pass on the trade entirely" regardless of the valuation score — this is exactly that case.**

**Why this is a "fails the R/R gate" outcome rather than a straightforward BUY, despite a passing Phase 02 score:**

1. **The valuation score and the R/R gate are testing different things, and they disagree here.** DB1 clears Phase 01 cleanly (8/8, no judgment calls) and scores 47.8 — solidly "Cheap" — on the back of attractive absolute FCF yield (5.47%) and EV/EBIT (16.56×) versus the framework's universal thresholds. But the **Forward PE sub-score (58.85)** is telling a different story: DB1's multiple sits almost exactly at its own 10-year average, meaning the stock isn't trading unusually cheap *relative to its own history* — it just looks cheap against the framework's absolute yardsticks. That combination (cheap on absolute multiples, fairly valued on own-history multiples) produces a real but **modest** valuation gap, and a modest gap is mathematically incompatible with a 2:1 R/R once a realistic stop-loss distance is applied — there simply isn't enough room between a disciplined entry and the fair-value target to clear the bar.

2. **A genuine, non-trivial WACC judgment call was required for the DCF, and is flagged prominently rather than smoothed over.** DB1's own raw beta (0.28) — and even a simple peer-average beta (0.626) — produce a WACC too low to generate a sane DCF output (Bear-case EV 1.6–1.7× the actual current EV, a clear Rule 4 sanity-check failure). This session resolved it by anchoring to ICE's beta (0.92) as the most comparable large peer, the same kind of explicit substitution the SGE session made for its own too-low beta — but taken further (a specific peer rather than a sector average), because the sector average still wasn't enough here. This is the most judgment-laden number in the session and the one most likely to move if revisited.

3. **The comparables-based fair value is built on a clean, in-band peer set** (5 of 8 candidate exchanges pass Rule 5's ±50% revenue-scale band on the first pass, no Workday-style outlier distortion this time) — giving more confidence in the Multiples-Based FV (€258.45) component than the DCF component, and the modest (+11.2%/+7.3%) gap to analyst consensus mean/median corroborates the blended figure (€318.23) as reasonable rather than aggressive.

4. **The R/R failure is robust to the obvious objections** — tested and ruled out: using the current price instead of a limit order (still fails, worse), loosening MoS to the bottom of the 25–30% band (still fails, in fact worse), and substituting the bull-case trim target for the primary sell target (would pass, but is explicitly not how Step 6 is defined — using it here would be exactly the rule-bending the framework prohibits).

**What would change this call (per Phase 06 / Rule 9):**
- **A lower entry price** — since the binding constraint is the numerator (upside), a price decline with the fundamental thesis intact would mechanically both improve the valuation score *and* widen the R/R gap simultaneously (the SGE precedent's "Rule 0 lesson" in reverse: here it's not a stale-price error, but a real future price move that would change the calculus).
- **A materially de-risked WACC judgment** — if a more clearly DB1-specific (rather than ICE-proxy) beta becomes available or defensible, narrowing the WACC uncertainty band could shift the DCF component of the blended FV meaningfully in either direction.
- Margin compression — gross margin (81.23% TTM basis) falling >3pp structurally, or ROIC (19.21%) falling toward cost of capital.
- EU regulatory action against Eurex/Clearstream's clearing-monopoly economics (the historical EMIR open-access threat) re-emerging as a live policy risk.
- Net debt/EBITDA (currently 1.706×, comfortable) rising materially — would also require monitoring the H1 FY26 balance sheet once `yfinance` carries it (currently a data gap, see §2).
- FY2026 full-year results (expected ~Feb 2027) — mandatory re-score; Q1 2026 already showed EBIT acceleration (€882M vs €796M in Q4 2025), worth re-checking at the next interim report.
- >15% unexplained move from €244.00 (Rule 9) — immediate re-score.

**Qualitative notes** (carried forward from the 2026-06-19 screening session, restated here per task instructions — not re-derived from scratch, lightly re-verified for currency):
- **Why margins are high:** Xetra (German cash equities), Eurex (Europe's largest derivatives exchange), and Clearstream (post-trade settlement/custody) are regulated, liquidity-network-effect businesses — an already-listed/cleared instrument's liquidity is destroyed by moving it elsewhere, locking in incumbency. High operating leverage on trading/clearing volume against near-fixed infrastructure costs.
- **Competitive moat:** replicating decades of accumulated trading liquidity, EU-wide regulatory licensing, and clearing-member relationships is not feasible organically. EU market-infrastructure competition has historically come via consolidation (LSEG/Refinitiv, Euronext's roll-up), not de novo entrants.
- **Capital allocation (5–10yr):** active consolidator via M&A (ISS, SimCorp, Qontigo/STOXX, Crypto Finance), funded by a debt/equity mix, alongside a consistent dividend. The Horizon 2026 strategy explicitly blends ~7%/yr organic growth with ~3%/yr from the SimCorp acquisition — management itself frames growth as part-organic, part-M&A, consistent with this session's choice to use only the organic component for the DCF base case.
- **Growth drivers (3–5yr):** Eurex derivatives volume (including an EU policy tailwind toward EU-based clearing as an alternative to US/UK CCPs), the new Investment Management Solutions segment (SimCorp, STOXX, ISS, Axioma) targeting recurring SaaS-like revenue, and Clearstream's collateral/securities-financing expansion.
- **Bear case:** revenue is volume/volatility-dependent — a prolonged low-volatility, low-rate environment compresses both trading fees and net interest income on client collateral balances. EU regulatory/political risk (EMIR open-access rules have historically threatened clearing-monopoly economics) and M&A integration risk (SimCorp, ISS) are real, ongoing risks.
- **Disruption vector:** low near-term risk — post-2008 regulation mandates central clearing for derivatives, reinforcing rather than threatening centralized clearinghouses. The dominant long-term dynamic (EU building clearing alternatives to US/UK CCPs) is more plausibly a tailwind than a threat specifically for Deutsche Börse.

**Process note:** this session documents the analytical recommendation only. No broker order has been placed and nothing has been logged in `decisions/` or `portfolio/holdings.md` — those steps follow only once a trade is actually executed, and in this case the R/R gate means no trade is being recommended regardless.

---

## 10. Next Review Trigger

- **A price decline toward or below the EUR 222.76 MoS-implied limit price** — would need a fresh R/R check at the lower entry (mechanically more likely to clear 2:1, since the numerator widens while a proportionally-scaled stop keeps the denominator roughly constant in percentage terms).
- **FY2026 full-year results** (expected ~Feb 2027) — mandatory re-score (Rule 9). Re-check: (a) FCF trend, (b) net debt/EBITDA trend (currently 1.706×, comfortable headroom), (c) organic vs. total (incl. SimCorp) revenue growth vs. Horizon 2026 guidance, (d) whether Q1 2026's EBIT acceleration (€882M) continues through the year.
- **If a future re-score's blended FV widens materially** (e.g., from updated peer multiples, a revised WACC judgment, or a lower entry price) such that R/R clears 2:1 → triggers a full position-sizing pass.
- **>15% unexplained price move from €244.00** (Rule 9) — immediate re-score.
- **EU regulatory signal** specific to Eurex/Clearstream clearing-monopoly economics (EMIR-style open-access risk).
- **Quarterly Rate Environment Gate update** (next: ~Sep 2026).
- **H1 FY26 balance sheet becoming available in `yfinance`** — would close the net-debt data gap flagged in §2 and allow a more current EV/Net-Debt-EBITDA cross-check, consistent with the SGE session's use of an H1-FY26-vintage balance sheet.

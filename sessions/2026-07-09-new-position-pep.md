# NEW POSITION — PEP (PepsiCo, Inc.) — 2026-07-09

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6)
**Date:** 9 Jul 2026
**10Y US Treasury Yield:** 4.55% (FRED `DGS10`, most recent posted row, 2026-07-07 — 07-08/07-09 not yet posted, normal FRED reporting lag)
**Rate Regime Modifier (Step 2, for the record only, not applied):** +5 (10Y in the 3.5–5% bracket)
**Current PEP portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. Confirmed absent from `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — this is PEP's first-ever `/new-position` evaluation under this framework.
**Sector:** Consumer Staples — packaged foods & beverages (snacks, salty/sweet snacks, carbonated soft drinks, sports drinks, juices).

---

## 0. Why this session exists — trigger source

A Telegram post on **FinnInvestChannel** (post ID 2908, ~15:16 UTC 2026-07-09) claimed PepsiCo reported weak earnings — declining snack/soft-drink volumes on inflation pressure, dividend yield ~4.15%. Per the operating brief, **Telegram post text is never used as financial data** — it is a trigger only. Independent verification below.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$137.11** | IBKR `get_price_snapshot`, contract_id **11017** (NASDAQ, "PEPSICO INC", exact-symbol US primary listing confirmed via `search_contracts`), last trade ts 2026-07-09 16:06:18 UTC |
| Bid / Ask | $137.02 / $137.08 (2 × 8 board lots) | IBKR `bid_ask` |
| Mark price (plprice) | $137.05 | IBKR `plprice` |
| Today's change | **−$5.40 / −3.79%** vs. prior close (implied prior close ≈ $142.51) | IBKR `change` |
| 52-week range | $129.861 (low) – $169.964 (high) | IBKR `misc_statistics` |
| Dividend yield (trailing, live) | **4.03%** | IBKR `dividend_yield` |
| Dividend yield (forward, cross-check) | 4.15% | Yahoo Finance `summaryDetail.dividendYield` — near-exact match to the Telegram post's cited ~4.15% |

**Two independent feeds (IBKR live snapshot, Yahoo Finance) agree the stock is down materially today and the dividend yield is genuinely elevated (~4.0–4.2%)** — the Telegram post's yield figure checks out. **$137.11 is used as the live price for all arithmetic below.**

### 1.1 What actually happened — independently verified via SEC EDGAR

Rather than take the Telegram post's causal claim at face value, SEC EDGAR was checked directly: PepsiCo filed an **8-K (Item 2.02, Results of Operations) on 2026-07-09**, together with a **10-Q**, both for the quarter ended 2026-06-13 (Q2 FY2026) — [8-K index](https://www.sec.gov/Archives/edgar/data/77476/000007747626000037/0000077476-26-000037-index.htm), exhibit [q220268-kxexhibit991.htm](https://www.sec.gov/Archives/edgar/data/77476/000007747626000037/q220268-kxexhibit991.htm). **This is a same-day earnings release — the price move is a real, fundamental (Rule 9) trigger, not noise, and this session independently confirms it rather than relying on the Telegram post's framing.**

**The "weak earnings" claim needs nuance — it is partially right and partially misleading:**
- **Headline GAAP EPS actually rose sharply**: $2.18 vs. $0.92 a year ago (+137%), and GAAP Operating Profit rose 125% ($4,023M vs. $1,789M) — but this is almost entirely an **easy comp**: Q2 2025 included **$1,860M of impairment charges** on the Rockstar and Be Cheery brands that did not recur this quarter. This is not organic strength.
- **Core (non-GAAP) EPS — the cleaner read — grew only 4%**, and **Core constant-currency EPS grew just 1%** — a soft underlying quarter, consistent with the Telegram post's characterization once the one-off comp is stripped out.
- **North America volumes did decline**, confirming the specific claim: **PFNA (Frito-Lay/Quaker convenient foods) organic volume −2%**, **PBNA (Pepsi/Gatorade beverages) organic volume −6%** in Q2 2026. PBNA's *reported* revenue still grew (+7%) only because of 2025 acquisitions and pricing, masking the underlying volume decline. Management explicitly cites "lower effective net pricing" and "affordability initiatives" in North America — consistent with the Telegram post's "inflation pressure" framing.
- **International segments grew organically** (Europe/Middle East/Africa, Asia Pacific Foods, International Beverages Franchise, Latin America Foods all posted volume growth) — the volume weakness is a North-America-specific problem, not global.
- **Guidance was affirmed, not cut.**

**Verdict: the Telegram post's dividend-yield figure is accurate, and its qualitative claim (declining NA snack/beverage volumes, inflation/affordability pressure) is independently confirmed by the company's own 8-K — but "weak earnings" oversimplifies a quarter where the GAAP headline actually beat sharply on an easy comp while Core (like-for-like) performance was merely soft, not a miss.** Treated as a real, cited Rule 9 fundamental trigger, not as financial data in itself.

---

## 2. Data Gathered

### 2.1 Data source note

`yfinance`'s bundled HTTP client (`curl_cffi`) failed via this session's proxy (`SSLError: Connection reset by peer`), the same documented issue as prior sessions. Worked around identically: queried Yahoo Finance's `quoteSummary` and `ws/fundamentals-timeseries` JSON endpoints directly via `requests` with a manually-obtained cookie/crumb. **All figures used in scoring below are cross-checked against PepsiCo's own primary filings** — the 2026-07-09 8-K/10-Q exhibit (Q2 FY2026 GAAP income statement, cash flow statement, balance sheet) and SEC EDGAR's XBRL `companyconcept`/`companyfacts` API (`data.sec.gov`, CIK 0000077476) for precise quarterly figures (`OperatingIncomeLoss`, `Revenues`, `NetIncomeLoss`, `IncomeTaxExpenseBenefit`, `DepreciationDepletionAndAmortization`, `PaymentsToAcquireProductiveAssets`, `EarningsPerShareDiluted`) — the primary, Rule-0-compliant source, not just a data vendor.

### 2.2 TTM reconstruction (Q3 FY2025 + Q4 FY2025 + Q1 FY2026 + Q2 FY2026)

PepsiCo's fiscal quarters (12-week Q1–Q3, ~16-week Q4) ending 2025-09-06, 2025-12-27, 2026-03-21, 2026-06-13 respectively. Q4 FY2025 derived as FY2025 (10-K) minus the sum of the first three 10-Q quarters (standard, unavoidable for a company that doesn't separately file a "Q4" 10-Q).

```
                    Q3 FY25   Q4 FY25   Q1 FY26   Q2 FY26   TTM
Revenue ($M)         23,937    29,343    19,443    24,181    96,904
Gross Profit ($M)    12,824    15,620    10,731    13,111    52,286
Operating Profit/EBIT 3,569     3,557     3,213     4,023    14,362
Net Income ($M)       2,603     2,540     2,327     2,981    10,451
Tax provision ($M)      713       445       632       848     2,638
Pretax income ($M)    3,331     3,000     2,970     3,852    13,153
D&A ($M)                824     1,136       742       897     3,599
Operating CF ($M)     4,472     6,619        41     2,324    13,456
CapEx ($M)              992     1,916       447       819     4,174
```
Sources: Q3/Q4 FY25 and Q1/Q2 FY26 EBIT, Revenue, Net Income, Tax, Pretax — SEC XBRL `us-gaap:OperatingIncomeLoss`/`Revenues`/`NetIncomeLoss`/`IncomeTaxExpenseBenefit`/`IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest`. D&A — `us-gaap:DepreciationDepletionAndAmortization` (Q1 FY26 $742M and H1 FY26 $1,639M reported directly; Q2 FY26 = $1,639M − $742M = $897M; FY2025 annual $3,451M less 9-month cumulative $2,315M = Q4 FY25 $1,136M). CapEx — `us-gaap:PaymentsToAcquireProductiveAssets`. Operating CF — `us-gaap:NetCashProvidedByUsedInOperatingActivities` (quarterly derived from YTD cumulative figures the same way).

```
EBITDA TTM = EBIT TTM + D&A TTM = 14,362 + 3,599 = 17,961M
FCF TTM    = OCF TTM − CapEx TTM = 13,456 − 4,174 = 9,282M
Effective tax rate TTM = 2,638 / 13,153 = 20.06%
Gross Margin TTM = 52,286 / 96,904 = 53.96%
Net Margin TTM   = 10,451 / 96,904 = 10.78%
FCF/NI TTM       = 9,282 / 10,451 = 88.81%
```

### 2.3 Balance sheet (as of 2026-06-13, from the Q2 FY2026 10-Q balance sheet)

```
Short-term debt        $10,602M
Long-term debt          $42,612M
Total Debt              $53,214M
Cash & equivalents      $10,251M
Total Equity (incl. NCI) $22,270M
Net Debt = 53,214 − 10,251 = $42,963M
Net Debt / EBITDA (TTM) = 42,963 / 17,961 = 2.392×
```

**Flagged finding — this ratio is sensitive to data freshness.** Using only the closed FY2025 annual figures (Net Debt $40,742M ÷ EBITDA $15,543M) gives **2.62×**, which would **fail** the standard <2.5× Debt Gate threshold. Using the fresher TTM reconstruction through today's just-filed Q2 FY2026 (above), it comes in at **2.39×, which passes**. This is exactly why Rule 0 / "always use the freshest available filed data" matters — reported here transparently rather than picking whichever number is more convenient.

### 2.4 Invested Capital / ROIC

```
NOPAT = EBIT TTM × (1 − effective tax rate) = 14,362 × (1 − 0.2006) = $11,481.6M
Invested Capital = Total Debt + Total Equity (incl. NCI) − Cash = 53,214 + 22,270 − 10,251 = $65,233M
ROIC = NOPAT / Invested Capital = 11,481.6 / 65,233 = 17.60%
```

### 2.5 Revenue 3yr CAGR (FY-anchored, structural — not TTM)

```
FY2022 Revenue $86,392M -> FY2025 Revenue $93,925M (both from 10-K filings)
CAGR = (93,925 / 86,392)^(1/3) − 1 = 2.83%
```
Well below this framework's Growth criteria at every threshold (>8% pre-screen, 25% = 100.0 on the Quality Score's Growth sub-score). FY2025 vs. FY2024 alone was +2.25% — consistent, not a one-year anomaly.

### 2.6 Market cap / EV / multiples at live price

```
Shares outstanding = 1,366,768,315 (Yahoo `defaultKeyStatistics`, matches 10-Q balance sheet's "1,366 shares issued net of repurchases")
Market Cap = $137.11 × 1,366,768,315 = $187,397.6M
EV = Market Cap + Total Debt − Cash = 187,397.6 + 53,214 − 10,251 = $230,360.6M
EV/EBIT (TTM) = 230,360.6 / 14,362 = 16.04×
FCF Yield (TTM FCF / Market Cap) = 9,282 / 187,397.6 = 4.95%
```

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Legacy 8-criterion table (context only — the binding gate is the weighted Quality Score below)

| Check | TTM Value | Threshold | Result |
|---|---|---|---|
| Gross margin | 53.96% | >40% | ✅ PASS |
| Net margin | 10.78% | >12% | ❌ FAIL |
| ROIC | 17.60% | >15% | ✅ PASS |
| Revenue growth (3yr CAGR, FY-anchored) | 2.83% | >8% | ❌ FAIL |
| FCF positive 3 consecutive years | FY2023 $7,924M / FY2024 $7,189M / FY2025 $7,672M — all positive | required | ✅ PASS |
| Net debt/EBITDA | 2.392× (TTM) | <2.5× | ✅ PASS (barely — see §2.3 freshness flag) |
| FCF yield | 4.95% | >4% | ✅ PASS (barely) |
| EV/EBIT | 16.04× | <20× | ✅ PASS |

6 of 8 legacy criteria pass — but the two failures (net margin, revenue growth) are exactly the inputs the Quality Score weights most heavily (Profitability 25%, Growth 20%), and the binding gate here is the continuous 80.0+ score, not this binary table.

### 3.2 Hard disqualifier check (fails regardless of weighted score)

- **FCF/NI conversion <70% for 2+ consecutive years:** FY2024 75.06% ($7,189M/$9,578M), FY2025 93.11% ($7,672M/$8,240M), TTM 88.81% — all comfortably above 70%. **Does not fire.**
- **Net Debt/EBITDA over threshold (2.5× standard — PepsiCo is a physical-asset consumer-staples business, not eligible for the Upgrade 5 asset-light override):** TTM 2.392× is under 2.5×. **Does not fire** — but see §2.3: this is a close, freshness-sensitive call, not a comfortable pass.
- **Not FCF-positive for 3+ consecutive years:** FY2023–FY2025 all positive. **Does not fire.**

**No hard disqualifier fires.** The gate outcome below is driven entirely by the weighted score.

### 3.3 Quality Score — full computation

```
Profitability (25%):
  NetMargin_Component = clamp(10.78/30 × 100) = 35.95
  ROIC_Component       = clamp(17.60/30 × 100) = 58.67
  Profitability_Score  = (35.95 + 58.67) / 2 = 47.31
  (no FCF-positivity cap — FCF-positive all 3 of the last 3 fiscal years)

Margins (15%):
  GrossMargin_Score = clamp(53.96/80 × 100) = 67.45
  (no structural-trend bonus — already well above the 40% threshold this bonus targets)
  Margins_Score = 67.45

Growth (20%):
  Growth_Score = clamp(2.83/25 × 100) = 11.30
  TAM/pricing-power modifier: NOT applied. Q2 2026 does show North America volume softness
    (PFNA −2%, PBNA −6%, §1.1) that could argue for the −10 "structurally decelerating" modifier,
    but this is a single quarter's data point — the framework requires "documented evidence growth
    is decelerating structurally (not cyclically)," which needs a multi-quarter pattern, not one
    print. Flagged here as an open item for the next re-check rather than scored without stronger
    evidence, consistent with "never infer without a documented source."
  Growth_Score = 11.30

Balance Sheet (15%):
  BalanceSheet_Score = clamp(100 × (1 − 2.392/4)) = 40.20

Moat Signal (15%) — checklist, only cited-evidence signals marked true:
  Market share stable/growing: MARKED TRUE — Gatorade holds ~65–70% of the US sports-drink
    category (BeverageDaily/Statista-sourced reporting, 2025–2026) and Frito-Lay holds a
    dominant (~50–60%, varying by source/region) share of US salty snacks (market reports,
    Feb 2026) — both large, multi-year-consistent #1 positions across independent sources.
  Brand premium: NOT marked true — the opposite signal is actually documented this quarter:
    PepsiCo's own 8-K cites "lower effective net pricing" in North America convenient foods,
    and a separate Feb 2026 press report ("PepsiCo slashes prices on snacks to boost sales")
    confirms active price-cutting for volume, not pricing power.
  Network effect: NOT marked true — not applicable to a packaged food/beverage CPG business model.
  Switching costs: NOT marked true — no lock-in mechanism; a consumer switches snack/soda brands
    at zero cost.
  Scale cost advantage: NOT marked true — plausible (PepsiCo's owned Direct-Store-Delivery
    network is a real structural asset) but no cost-per-unit citation was pulled this session —
    not invented per "never mark true without cited source."
  Moat_Score = (1/5) × 100 = 20.00

FCF Quality (10%):
  FCFQuality_Score = clamp(((0.8881 − 0.40)/0.60) × 100) = 81.36

Quality Score = 47.31×0.25 + 67.45×0.15 + 11.30×0.20 + 40.20×0.15 + 20.00×0.15 + 81.36×0.10
              = 11.828 + 10.118 + 2.260 + 6.030 + 3.000 + 8.136
              = 41.37  →  rounds to 41.4
```

**Quality Score = 41.4 / 100.0 — well below the 80.0 gate.** No hard disqualifier independently fires, but the weighted score fails decisively — driven primarily by the Growth sub-score (2.83% 3yr revenue CAGR vs. the framework's 25% ceiling) and a middling Profitability sub-score (net margin under 11%, ROIC a respectable but not exceptional 17.6%).

**Gate result: FAIL.** Per operating-brief.md / quality-scoring.md: stop here — do not proceed to the Rate Environment Gate or Phase 02 valuation scoring, regardless of how the dividend yield or price drop look on their own.

---

## 4. Rate Environment Gate — NOT RUN (for the record only)

```
0y (FY2026E) consensus EPS estimate = $8.63621 (Yahoo earningsTrend, "0y" row ending 2026-12-31 —
  NOT the raw `forwardPE` field, which reads the wrong "+1y"/FY2027E row — same correction
  documented in prior sessions, e.g. the 2026-07-08 MU session)
Forward PE = $137.11 / $8.63621 = 15.88×
Earnings Yield = 1 / 15.88 = 6.30%
Spread vs. 10Y (4.55%) = +1.75%  (>= +1.5% threshold — would PASS Step 1, no yellow flag)
Rate Regime Modifier (Step 2) = +5 (10Y in the 3.5–5% bracket)
```
Neither is applied — the Quality Gate stops the process first.

---

## 5. Phase 02 — Valuation Score / Composite Score — NOT RUN

Not applicable — Quality Gate failed (§3.3). No FCF Yield, EV/EBIT, Forward PE, or PEG sub-scores are combined into a valuation score; no Composite Score exists. (FCF Yield 4.95%, EV/EBIT 16.04× and Forward PE 15.88× were computed above only as inputs to the Rate Environment Gate/§2 cross-checks — they are not scored, since scoring never begins without a Quality Score ≥80.0.)

No fair value, buy/sell/stop levels, R/R, or position size were computed — per fair-value-methodology.md, order setup only runs for a BUY or TRIM action, neither of which applies here.

---

## 6. Qualitative Notes

1. **The Telegram trigger was directionally useful but imprecise.** The dividend-yield claim (~4.15%) checks out almost exactly against Yahoo's own figure. The "weak earnings" framing oversimplifies: GAAP EPS actually beat sharply on an easy prior-year impairment comp, while the *cleaner* Core EPS read (+4%, +1% constant-currency) was merely soft — and the specific claim of declining NA snack/beverage volumes is real and independently confirmed (PFNA −2%, PBNA −6% organic volume) via PepsiCo's own 2026-07-09 8-K.
2. **The Quality Gate fails on fundamentals that have nothing to do with today's earnings print** — this is a structural, multi-year finding (3yr revenue CAGR 2.83%, TTM net margin 10.78%), not a one-quarter blip. Today's earnings release doesn't change that conclusion; it's simply what triggered this session.
3. **Net Debt/EBITDA is a genuinely close call and materially data-freshness-sensitive** (2.39× on TTM through today's filing vs. 2.62× on FY2025-only) — flagged transparently in §2.3 rather than silently picking the more favorable number.
4. **Moat evidence is thin and mostly uncreditable under this framework's cited-evidence bar** — only "market share" clears it (Gatorade/Frito-Lay's large, durable share positions); "brand premium" is actually contradicted by this quarter's own disclosed price-cutting in North America.
5. **International growth is real and healthy** (EMEA, Asia Pacific Foods, International Beverages Franchise, Latin America Foods all show organic volume growth) — the weak spot is specifically the North America core business, PepsiCo's largest market.
6. **Guidance was affirmed, not cut** — this is not a "growth thesis broken" situation per fair-value-methodology.md's Full Exit triggers (moot here anyway, since PEP is not and was not a position).

---

## 7. Recommendation

# **PASS — Quality Gate FAIL (Quality Score 41.4 < 80.0). Do not enter.**

PepsiCo does not clear this framework's 80.0+ Quality Score gate — no hard disqualifier independently fires, but the weighted score fails decisively, driven by a 2.83% 3-year revenue CAGR (Growth sub-score 11.3/100) and a sub-11% net margin (Profitability sub-score 47.3/100). No Phase 02 valuation score or Composite Score was computed, and no fair value, order setup, or position sizing was produced. **No position should be opened.** This is a clean quality-driven pass — it does not depend on whether today's earnings print or the current ~4.0–4.2% dividend yield look individually attractive.

---

## 8. Next Review Trigger

- **A sustained (multi-quarter) reacceleration in revenue CAGR or improvement in net margin** — the two sub-scores actually driving the gate failure. A single strong quarter would not be sufficient on its own (Rule 9 still requires the trigger to be re-evaluated with fresh data, but the Growth sub-score is explicitly FY-anchored/structural, not one-quarter-reactive).
- **Q3 FY2026 earnings** (expected ~October 2026, standard Rule 9 quarterly trigger) — to see whether North America PFNA/PBNA volume softness (§1.1, §3.3) is a one-quarter blip or a genuine structural deceleration (which would also resolve the Growth sub-score's currently-unapplied −10 modifier question).
- Any guidance revision, management change, or M&A (Rule 9 standard triggers).
- Any further >15% unexplained move from today's $137.11 reference.

**No position opened — nothing to log in `decisions/`.**

---

## Glossary

- **8-K** — A US company's "current report" filed with the SEC to disclose a material event between regular filings; earnings press releases are typically furnished as an exhibit to one.
- **10-Q (Quarterly Report)** — The quarterly financial-disclosure report a US public company files with the SEC, containing unaudited financial statements for the most recent fiscal quarter.
- **BalanceSheet_Score / Net Debt/EBITDA** — See Net Debt/EBITDA below; the Quality Score's balance-sheet sub-score is derived from it.
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate between a start and end value.
- **CapEx** — Capital Expenditure — money spent buying or upgrading physical assets.
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every company that files with EDGAR; used to construct the API/URL paths this session's SEC filings and XBRL data were pulled from.
- **Composite Score** — This framework's blended Quality + Valuation ranking number; not computed here since the Quality Gate failed first.
- **Core (non-GAAP measure)** — PepsiCo's own non-GAAP operating-profit/EPS measure, stripping out items management deems non-recurring; used here to show GAAP EPS growth (+137%) was an easy-comp artifact while Core EPS growth (+4%) reflects the softer underlying quarter.
- **D&A** — Depreciation & Amortization — the non-cash accounting expense that spreads the cost of long-lived assets over time.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating profit before financing/accounting effects.
- **Effective tax rate** — The actual percentage of pretax income paid as tax (tax provision ÷ pretax income) in a given period.
- **EPS** — Earnings Per Share, net income divided by shares outstanding.
- **EV** — Enterprise Value, a company's total value to all capital providers (market cap + debt − cash).
- **EV/EBIT** — Enterprise Value divided by EBIT — a multiple measuring how expensive a company is relative to its operating profit.
- **EY (Earnings Yield)** — 1 ÷ Forward PE, expressed as a yield comparable to bond yields.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself.
- **FCF Yield** — Free Cash Flow ÷ Market Cap; higher means cheaper.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income; checks whether reported accounting profit is turning into real cash.
- **Forward PE** — Price ÷ next-twelve-months expected earnings per share.
- **GAAP** — Generally Accepted Accounting Principles — the standard US accounting rulebook.
- **Hard disqualifier** — A Quality Score condition that fails a company regardless of its weighted score; none fired for PEP.
- **Invested Capital** — The total capital (debt + equity, netted for cash) put to work in a business; the denominator of ROIC.
- **Moat** — A durable competitive advantage protecting a business's profits from competitors.
- **Net Debt/EBITDA** — A leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
- **Net Margin** — Net Income ÷ Revenue.
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate); the numerator used to compute ROIC.
- **Organic revenue growth** — Revenue growth excluding acquisitions, disposals, and currency effects — isolates underlying demand from M&A/FX noise.
- **PE (Price-to-Earnings) ratio** — Share price ÷ earnings per share.
- **PFNA / PBNA** — PepsiCo's North America convenient-foods and beverages reporting segments respectively; both showed organic volume declines in Q2 2026.
- **Quality Score** — This framework's 0.0–100.0 continuous score grading Phase 01 criteria; 80.0+ required to proceed to valuation scoring. PEP scored 41.4.
- **Rate Environment Gate** — The mandatory pre-check before Phase 02 scoring, comparing Earnings Yield to the 10-Year Treasury yield; computed for the record only here since the Quality Gate stopped the process first.
- **Rate Regime Modifier** — An additive score adjustment based on the current 10-Year Treasury yield bracket.
- **ROIC** — Return on Invested Capital — how efficiently a company turns invested capital into profit.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 9** — Fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results.
- **XBRL (eXtensible Business Reporting Language)** — The structured, machine-readable format the SEC requires financial-statement figures to be tagged in; used here to pull precise quarterly figures directly from PepsiCo's own filings via SEC EDGAR's API.

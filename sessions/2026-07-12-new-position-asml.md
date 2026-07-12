# NEW POSITION — ASML (ASML Holding N.V.) — 2026-07-12

**Task type:** NEW POSITION (Telegram-scan trigger)
**Date:** 12 Jul 2026 (Sunday — US/European equity markets closed; see §1)
**10Y US Treasury Yield:** 4.54% (FRED `DGS10`, most recent posted row, 2026-07-09 — 07-10 not yet posted at query time, normal FRED reporting lag)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current ASML portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. Confirmed absent from `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — this is ASML's first-ever `/new-position` evaluation under this framework.
**Sector:** Technology / Semiconductor capital equipment — sole global manufacturer of EUV (Extreme Ultraviolet) lithography systems, the equipment used to print the most advanced chip nodes (5nm/3nm/2nm logic, advanced DRAM/HBM).
**Ticker / listing:** NASDAQ **ASML** ("ASML HOLDING NV-NY REG SHS"), contract_id **117902840** (confirmed via `search_contracts`) — a **NY Registry Share**, not a conventional ADR: it represents the underlying Dutch ordinary share (also listed on Euronext Amsterdam, "AEB", contract_id 117589399) directly, without a depositary-bank ratio conversion. Financial statements are filed in **EUR**; the NASDAQ listing trades in **USD** — this mixed-currency setup is handled explicitly throughout this session (see §2.5).

---

## 0. Why this session exists — trigger source

A Telegram post (**tarasguk channel, post #11357, ~10:03 UTC 2026-07-12, edited**) named ASML as one of three companies (ASML, TSM, NFLX) of particular interest heading into the upcoming earnings season. Per the operating brief, **Telegram post text is never used as financial data** — it is a trigger only. Independent verification below.

**Verified independently:** ASML has not yet reported Q2 2026 earnings. The last 6-K filed with the SEC is the 23 Apr 2026 AGM-results filing; the last *earnings* 6-K is 15 Apr 2026 (Q1 2026 results). Public reporting (e.g. a 10 Jul 2026 TechTimes article headlined "ASML Earnings Wednesday") indicates Q2 2026 results are expected in the coming days — consistent with ASML's historical mid-July reporting cadence (Q2 2025 was reported 16 Jul 2025). This confirms the Telegram post's "heading into earnings season" framing is directionally accurate, independent of anything else in the post.

---

## 1. Live Price (Rule 0)

Today (2026-07-12) is a **Sunday** — US and European equity markets are closed. Per this framework's established weekend/holiday convention (see e.g. the 2026-07-04 AMZN/MSFT/AVGO sessions), the most recent completed trading session's close is used as the live price, fetched fresh this session (not reused from any prior snapshot).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$1,797.32** | IBKR `get_price_history` (contract_id 117902840, NASDAQ), most recent daily bar close = **2026-07-10** (Friday, last completed session before the weekend) |
| Cross-check 1 | $1,797.32 | Yahoo Finance `regularMarketPrice` (direct `quoteSummary` pull, see §2.1) — exact match |
| Cross-check 2 | "$1797.32" (close, -0.4%) | WebSearch — GuruFocus article dated around 2026-07-10/11 citing ASML shares closing at $1797.32 |
| ⚠️ Tooling flag | IBKR `get_price_snapshot`'s `last` field returned **$1,804.25** (flagged `is_close: true`) — this is **stale by one session** (it's Thursday 2026-07-09's close, not Friday's). Same documented issue as the 2026-07-04 AVGO session. `plprice` (mark price) correctly showed $1,797.32, matching `get_price_history` and Yahoo. **$1,797.32 used throughout this session.** |
| 52-week range | $679.84 – $1,999.96 (IBKR `misc_statistics`) | ASML made a new all-time high of $1,999.96 in the days before this pullback |
| Trailing dividend yield | 0.49% | IBKR `dividend_yield`, matches Yahoo `summaryDetail.dividendYield` exactly |
| Shares outstanding | 385,417,665 | SEC XBRL `dei:EntityCommonStockSharesOutstanding` (FY2025 20-F cover page) — matches Yahoo `sharesOutstanding` exactly |
| Live EUR/USD FX rate | **1.143** (1 EUR = $1.143) | IBKR `get_price_snapshot` (EUR/USD, contract_id 12087792), `prior_close` (Friday) — cross-checked against WebSearch (ECB/valutafx reporting 1.1411–1.143 for 2026-07-10). **Used throughout for all EUR→USD conversions below.** |

---

## 2. Data Gathered

### 2.1 Data source note

`yfinance`'s bundled HTTP client (`curl_cffi`) failed via this session's proxy (`SSLError: Connection reset by peer`), the same documented issue as prior sessions (PEP, MU). Worked around identically: queried Yahoo Finance's `quoteSummary` JSON endpoint directly via `requests` with a fetched cookie/crumb. Because ASML is a **foreign private issuer**, it files a **Form 20-F** (annual) and **Form 6-K** (interim/other) with the SEC rather than a 10-K/10-Q. All fundamental figures below are sourced primarily from **SEC EDGAR** — the FY2025 20-F (filed 2026-02-25, accession 0001628280-26-011378) via its XBRL `companyconcept` API, and the Q1 2026 and Q1 2025 6-Ks (financial-statement exhibits) for quarterly figures, since **ASML's 6-K interim filings are not XBRL-tagged** (confirmed: querying `companyconcept` for `RevenueFromContractWithCustomerExcludingAssessedTax` and other tags returns only 20-F annual data points, no quarterly ones) — this is a genuine data-availability gap, not a lookup failure, and is why the TTM reconstruction below uses full-year 20-F figures adjusted by the two most recent quarterly 6-Ks rather than four independently-tagged quarters.

### 2.2 TTM reconstruction (Q2 2025 + Q3 2025 + Q4 2025 + Q1 2026, EUR millions)

Method: **FY2025 (20-F, full year) − Q1 2025 (6-K) + Q1 2026 (6-K)**, since ASML's fiscal year = calendar year and this is the only way to isolate a trailing-twelve-month window through the most recent quarter without XBRL-tagged quarterly data.

```
                         FY2025 (20-F)   Q1 2025 (6-K)   Q1 2026 (6-K)   TTM (Q2'25–Q1'26)
Net sales                  32,667.3         7,741.5         8,766.9         33,692.7
Gross profit                17,258.0         4,179.7         4,645.0         17,723.3
EBIT (income from ops)      11,301.4         2,737.9         3,157.8         11,721.3
Net income                   9,609.4         2,355.0         2,756.7         10,011.1
Income tax expense           2,013.4           465.1           546.6          2,094.9
Operating cash flow          12,658.5           (58.6)       (2,185.6)        10,531.5
CapEx (PP&E purchases)        1,573.6           415.0           402.4          1,561.0
D&A                           1,025.9           241.3           259.4          1,044.0
```
Sources: FY2025 figures — SEC XBRL `companyconcept` API, CIK 0000937966, tags `RevenueFromContractWithCustomerExcludingAssessedTax`, `GrossProfit`, `OperatingIncomeLoss`, `NetIncomeLoss`, `IncomeTaxExpenseBenefit`, `NetCashProvidedByUsedInOperatingActivities`, `PaymentsToAcquirePropertyPlantAndEquipment`, `DepreciationDepletionAndAmortization` (all form 20-F, fp=FY, filed 2026-02-25). Q1 2025 and Q1 2026 figures — the respective quarter's 6-K financial-statement exhibit (`financialstatementsusgaapq.htm` filed 2025-04-16; `financialstatementsusgaa.htm` filed 2026-04-15), both US-GAAP condensed statements.

```
EBITDA TTM = EBIT + D&A = 11,721.3 + 1,044.0 = 12,765.3M EUR
FCF TTM    = OCF − CapEx = 10,531.5 − 1,561.0 = 8,970.5M EUR
Effective tax rate TTM = 2,094.9 / (10,011.1 + 2,094.9) = 2,094.9 / 12,106.0 = 17.31%
Gross Margin TTM = 17,723.3 / 33,692.7 = 52.60%
Net Margin TTM   = 10,011.1 / 33,692.7 = 29.71%
FCF/NI TTM       = 8,970.5 / 10,011.1 = 89.60%
```

**Cross-check against Yahoo Finance's own `financialData` module** (queried same session): `totalRevenue` $33,692,700,672 (exact match, in EUR despite the module otherwise mixing currencies — see §2.5), `operatingCashflow` $10,531,500,032 (exact match), `profitMargins` 29.713% (matches 29.71% above to 2dp). Independent cross-check confirms the reconstruction.

### 2.3 Balance sheet

| Field | Q1 2026 (2026-03-29, freshest) | FY2025 (2025-12-31, fully itemized) | Source |
|---|---|---|---|
| Cash + short-term investments | €8,376.3M | Cash €12,916.0M (no ST investments line broken out in 20-F pull) | Q1 2026 6-K balance sheet; FY2025 20-F XBRL `CashAndCashEquivalentsAtCarryingValue` |
| Long-term debt (noncurrent) | €2,705.6M (single line — see flag below) | €2,709.0M | Q1 2026 6-K; FY2025 20-F XBRL `LongTermDebtNoncurrent` |
| Current portion of LT debt | *not separately itemized* | €1,681.9M | FY2025 20-F XBRL `LongTermDebtCurrent` |
| Total debt | €2,705.6M (as disclosed) | €4,390.9M | — |
| Stockholders' equity | €20,829.5M | €19,612.2M | Q1 2026 6-K; FY2025 20-F XBRL `StockholdersEquity` |

⚠️ **Flagged data gap:** the Q1 2026 6-K's abbreviated financial-statement exhibit presents only a single "Long-term debt" line and an un-itemized "Total current liabilities" total — it does **not** separately break out a current-portion-of-long-term-debt line the way the full FY2025 20-F does. Both Yahoo's `financialData.totalDebt` ($2,705,600,000) and my own extraction of the Q1 2026 6-K agree on €2,705.6M as "the" debt figure, but it's possible a current-maturities tranche exists within the €20,288.0M "Total current liabilities" figure that isn't visible in this abbreviated statement. Given ASML's debt is tiny relative to its cash pile either way (see below), this does not change the qualitative Balance Sheet conclusion (deep net cash), but is disclosed rather than silently reconciled.

```
Net Debt (Q1 2026, freshest) = 2,705.6 − 8,376.3 = −5,670.7M EUR (net cash)
Net Debt (FY2025, fully itemized, cross-check) = 4,390.9 − 12,916.0 = −8,525.1M EUR (net cash)
Net Debt/EBITDA (Q1 2026 balance ÷ TTM EBITDA) = −5,670.7 / 12,765.3 = −0.444×
```
Either balance-sheet date gives the same qualitative result: **ASML holds substantially more cash than total debt** — a deep net-cash position by a wide margin under either figure.

### 2.4 Invested Capital / ROIC / NOPAT

```
NOPAT = EBIT_TTM × (1 − effective tax rate) = 11,721.3 × (1 − 0.1731) = 9,693.4M EUR
Invested Capital (Q1 2026 balance) = Total Debt + Equity − Cash = 2,705.6 + 20,829.5 − 8,376.3 = 15,158.8M EUR
ROIC = 9,693.4 / 15,158.8 = 63.95%
```
This is a genuinely very high ROIC, driven by ASML's unusually small invested-capital base relative to its earnings power (a large cash balance funded substantially by customer prepayments/deposits against its multi-year backlog nets *against* debt+equity in this framework's formula). Shown transparently rather than smoothed — it comfortably clears the Profitability sub-score's 30% ceiling regardless of exact precision.

### 2.5 Market Cap / EV / multiples — currency handling

**Flagged and resolved explicitly:** ASML's underlying financials (revenue, EBIT, debt, cash, FCF, etc., pulled above from SEC filings and Yahoo's `financialData` module) are denominated in **EUR** — confirmed because Yahoo's own `totalCash`/`totalDebt`/`totalRevenue` fields for this USD-quoted ticker return figures numerically identical to the EUR SEC filing amounts (no FX conversion applied by the vendor), while `currentPrice`/`marketCap` are genuinely in **USD** (the NASDAQ trading price). Mixing these directly would understate EV materially. All EUR figures below are converted to USD at the live 1.143 rate (§1) before combining with USD market cap.

```
Market Cap (USD) = $1,797.32 × 385,417,665 = $692,718.9M   (matches Yahoo marketCap $692,718,862,336 exactly)

Total Debt (USD)  = €2,705.6M × 1.143 = $3,092.7M
Cash (USD)        = €8,376.3M × 1.143 = $9,574.1M
EV = Market Cap + Total Debt − Cash = 692,718.9 + 3,092.7 − 9,574.1 = $686,237.5M

EBIT_TTM (USD)  = €11,721.3M × 1.143 = $13,397.6M
FCF_TTM (USD)   = €8,970.5M × 1.143  = $10,253.3M

EV/EBIT (TTM)   = 686,237.5 / 13,397.6 = 51.22×
FCF Yield (TTM) = 10,253.3 / 692,718.9 = 1.480%
```

### 2.6 Revenue 3yr CAGR (FY-anchored, structural — not TTM)

```
FY2022 Revenue €21,173.4M → FY2025 Revenue €32,667.3M (both SEC XBRL, form 20-F)
CAGR = (32,667.3 / 21,173.4)^(1/3) − 1 = 15.55%
```

### 2.7 FCF/NI ratio history (hard-disqualifier check)

| FY | OCF | CapEx | FCF | Net Income | FCF/NI |
|---|---|---|---|---|---|
| 2022 | 8,486.8 | 1,281.8 | 7,205.0 | 5,624.2 | 128.1% |
| 2023 | 5,443.4 | 2,155.6 | 3,287.8 | 7,839.0 | **41.9%** |
| 2024 | 11,166.2 | 2,067.2 | 9,099.0 | 7,571.6 | 120.2% |
| 2025 | 12,658.5 | 1,573.6 | 11,084.9 | 9,609.4 | 115.4% |
| TTM | 10,531.5 | 1,561.0 | 8,970.5 | 10,011.1 | 89.6% |

FY2023 is an isolated below-70% year (heaviest CapEx year of the five shown, €2.16B, coinciding with the High-NA EUV ramp) — **not** a 2+ consecutive-year run, so the hard disqualifier's trigger condition is not met regardless of the growth-capex carve-out.

### 2.8 Consensus / forward estimates (Yahoo `earningsTrend`, direct `quoteSummary` pull)

Per this framework's established correction (documented in the PEP/MU sessions): use the dated **"0y" row**, not the raw `forwardPE`/`defaultKeyStatistics.forwardEps` fields, which read a different (next-FY, "+1y") base and materially overstate/understate the true forward year.

| Row | Period end | Consensus EPS (USD) |
|---|---|---|
| 0y | 2026-12-31 | **$31.948** |
| +1y | 2027-12-31 | $43.619 |

```
Forward PE = $1,797.32 / $31.948 = 56.26×
```
Analyst price targets (15 analysts, Yahoo `financialData`): mean $1,877.31, median $1,871.60, high $2,618.51, low $883.45, consensus rating "strong_buy" — discussed as qualitative context in §6, never as a scored input (sell-side price targets are not part of this framework's valuation score).

### 2.9 5-year historical PE range (reconstruction method, flagged as coarser than the framework's preference)

The framework's documented `get_earnings_dates`-based quarterly TTM-PE reconstruction (valuation-scoring.md) is **not usable for ASML** — it requires quarterly reported EPS, and ASML's interim 6-Ks aren't XBRL-tagged (§2.1). **Fallback used:** 5 annual year-end snapshots, pairing each fiscal year's own SEC-filed diluted EPS against that same fiscal year-end's EUR closing price (AEB listing, contract_id 117589399, via IBKR `get_price_history`) — same-currency, dimensionless PE ratio, so no FX conversion is needed for this specific calculation.

| FY | Diluted EPS (EUR) | Year-end price (EUR, AEB) | Trailing PE |
|---|---|---|---|
| 2021 | 14.34 | 706.7 | 49.28× |
| 2022 | 14.13 | 502.8 | 35.58× |
| 2023 | 19.89 | 681.2 | 34.25× |
| 2024 | 19.24 | 678.7 | 35.27× |
| 2025 | 24.71 | 921.4 | 37.29× |

```
5yr Low PE  = 34.25×  (FY2023)
5yr High PE = 49.28×  (FY2021)
5yr Avg PE  = (49.28+35.58+34.25+35.27+37.29)/5 = 38.33×
```
⚠️ **Flagged:** this is 5 annual points, not ~20 quarterly points — coarser than the framework's preferred method. As shown in §4.3, the conclusion it drives (Forward PE sits *above* the 5-year high) is unambiguous regardless of this precision gap.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Legacy 8-criterion table (context only — the binding gate is the weighted Quality Score below)

| Check | TTM Value | Threshold | Result |
|---|---|---|---|
| Gross margin | 52.60% | >40% | ✅ PASS |
| Net margin | 29.71% | >12% | ✅ PASS |
| ROIC | 63.95% | >15% | ✅ PASS |
| Revenue growth (3yr CAGR, FY-anchored) | 15.55% | >8% | ✅ PASS |
| FCF positive 3 consecutive years | FY2023 €3.29B / FY2024 €9.10B / FY2025 €11.08B — all positive | required | ✅ PASS |
| Net debt/EBITDA | −0.44× (net cash) | <2.5× | ✅ PASS |
| FCF yield | 1.48% | >4% | ❌ **FAIL** |
| EV/EBIT | 51.22× | <20× | ❌ **FAIL** |

6 of 8 pass — the two failures are both **valuation** metrics (FCF yield, EV/EBIT), not quality ones. This is exactly the split this framework's Quality/Valuation separation is designed to surface: ASML looks set to score very well on quality fundamentals while being priced extremely richly — two different questions, scored separately below.

### 3.2 Hard disqualifier check (fails regardless of weighted score)

- **FCF/NI conversion <70% for 2+ consecutive years:** only FY2023 (41.9%) falls below 70% — a single, non-consecutive year (heaviest CapEx year of the period, High-NA ramp). **Does not fire.**
- **Net Debt/EBITDA over threshold:** −0.44× (net cash) is far under 2.5×. **Does not fire.**
- **Not FCF-positive for 3+ consecutive years:** all of FY2021–FY2025 positive. **Does not fire.**

**No hard disqualifier fires.**

### 3.3 Quality Score — full computation

```
Profitability (25%):
  NetMargin_Component = clamp(29.71/30 × 100) = 99.04
  ROIC_Component       = clamp(63.95/30 × 100) = 100.00 (capped)
  Profitability_Score  = (99.04 + 100.00) / 2 = 99.52
  (no FCF-positivity cap — FCF-positive all 5 of the last 5 fiscal years)

Margins (15%):
  GrossMargin_Score = clamp(52.60/80 × 100) = 65.75
  (no structural-trend bonus — already far above the 40% bonus-eligibility ceiling)
  Margins_Score = 65.75

Growth (20%):
  Growth_Score raw = clamp(15.55/25 × 100) = 62.20
  TAM/pricing-power modifier: +10 APPLIED. Documented evidence: ASML's Nov 2024 Investor Day
    reaffirmed (and press coverage through mid-2026 confirms still-standing) a 2030 revenue
    scenario of €44–60B (vs. FY2025 actual €32.7B), a guided double-digit EUV lithography
    spending CAGR 2025–2030 for both Logic and DRAM, and FY2026 guidance of €36–40B — already
    implying growth above the trailing 3yr CAGR. Backlog stood at a record €38.8B entering 2026.
    All company-sourced (Investor Day materials, quarterly guidance), cross-reported by
    multiple independent outlets (Yahoo Finance, ad-hoc-news.de, TechInsights, Evertiq).
  Growth_Score = 62.20 + 10 = 72.20

Balance Sheet (15%):
  BalanceSheet_Score = clamp(100 × (1 − (−0.444)/4)) = clamp(111.1) = 100.00 (capped, net cash)

Moat Signal (15%) — checklist, only cited-evidence signals marked true:
  Market share stable/growing: MARKED TRUE — ASML holds 100% share of the global EUV
    lithography equipment market (sole manufacturer; Nikon/Canon only produce older DUV tools)
    and ~83% of all worldwide lithography-equipment sales as of 2025, per multiple independent
    analyst/press sources (Motley Fool Dec 2025, EveryTicker, TechMarketBriefs) — a large,
    multi-year-stable #1/monopoly position, not a single-source claim.
  Brand premium / pricing power: MARKED TRUE — gross margin at/near record levels (52.8% FY2025,
    guided 51–53% for FY2026) even as newer High-NA EUV systems are priced substantially above
    prior-generation EUV tools (~$380M/unit for High-NA vs. ~$200M-class for standard EUV, per
    third-party industry reporting) — an ASP increase reflecting technology leadership, not
    merely cost pass-through.
  Network effect: NOT marked true — not applicable to a capital-equipment business selling to a
    small, concentrated customer base; no two-sided-market dynamic identified.
  Switching costs: MARKED TRUE — no alternative EUV supplier exists at all (Canon/Nikon serve
    only the lower-end DUV segment); customers (TSMC, Samsung, Intel) must co-develop each new
    process node with ASML over multi-year qualification cycles, and the €38.8B backlog
    represents multi-year committed capacity slots — an unusually strong, well-documented
    lock-in mechanism.
  Scale cost advantage: NOT marked true — no cost-per-unit comparison against a comparable EUV
    competitor exists (none is being made), so this signal is left uncredited per "never mark
    true without cited source," consistent with how this framework has treated the same gap for
    other names lacking a same-category cost comp (e.g. PEP, MU sessions).
  Moat_Score = (3/5) × 100 = 60.00

FCF Quality (10%):
  FCFQuality_Score = clamp(((0.8960 − 0.40)/0.60) × 100) = 82.68

Quality Score = 99.52×0.25 + 65.75×0.15 + 72.20×0.20 + 100.00×0.15 + 60.00×0.15 + 82.68×0.10
              = 24.880 + 9.863 + 14.440 + 15.000 + 9.000 + 8.268
              = 81.450  →  rounds to 81.5 (raw value sits at the ".X5" boundary; > 81.450 exactly,
                so rounds up under both plain rounding and this framework's explicit tie-break rule)
```

**Quality Score = 81.5 / 100.0 — clears the 80.0 gate.** ASML's first-ever evaluation under this framework **passes** the Quality Gate — driven by exceptional Profitability, a fully net-cash Balance Sheet, and a strong (3-of-5) Moat reading, offset somewhat by a middling Margins sub-score (52.6% gross margin, well below the 80% ceiling this component scales against) and a Moat score capped at 60 for lack of a citable scale-cost-advantage comparison.

⚠️ **Flagged, not resolved:** Hybrid Upgrade 1 (Owner Earnings) asks whether Growth CapEx exceeds 30% of total CapEx, in which case FCF should be replaced by Owner Earnings for scoring purposes. ASML does not disclose a maintenance-vs-growth CapEx split in its filings, and it is not one of the four companies (MSFT/GOOGL/META/AMZN) for which this framework mandates the substitution regardless. **Standard FCF is used throughout this session** rather than inventing a split — flagged as an open item, not resolved.

---

## 4. Rate Environment Gate

```
Step 1 — Earnings Yield Spread Test:
  Forward PE (0y, FY2026E) = $1,797.32 / $31.948 = 56.26×
  EY = 1 / 56.26 = 1.7775%
  Spread = EY − 10Y (4.54%) = 1.7775% − 4.54% = −2.7625pp
  Spread < +1.5% → Step 1 FAILS → additive +5 (yellow flag, not a hard block per the
    2026-06-07 change)

Step 2 — Rate Regime Modifier:
  10Y = 4.54% → within the 3.5–5% bracket → +5

Combined Rate Environment Gate contribution = +5 + 5 = +10
```

---

## 5. Phase 02 — Valuation Score

### 5.1 PEG applicability (Fast Grower test)

```
Diluted EPS: FY2021 14.34 → FY2022 14.13 (−1.5%) → FY2023 19.89 (+40.8%) →
             FY2024 19.24 (−3.3%) → FY2025 24.71 (+28.4%)
```
EPS growth is **lumpy/cyclical**, not a sustained >15%/yr run over 3+ consecutive years (two of the last four years were *declines*) — ASML does **not** qualify as a Fast Grower under this framework's definition. **PEG is not applicable; its 15% weight is redistributed to EV/EBIT** (making EV/EBIT 40% instead of 25%), per valuation-scoring.md's redistribution rule.

### 5.2 Sub-scores

```
FCF Yield (40%):
  FCF_Score = clamp(100 × (1 − 1.480/10)) = 85.20

EV/EBIT (40%, redistributed from 25%+15% PEG):
  EV/EBIT_Score = clamp((51.22 − 12)/23 × 100) = clamp(170.5) = 100.00 (capped)

Forward PE (20%):
  Primary formula (5yr low/high range available, §2.9):
    FwdPE_Score = clamp((56.26 − 34.25)/(49.28 − 34.25) × 100) = clamp(146.4) = 100.00 (capped)
  Historical PE Modifier (Upgrade 2, vs. 5yr avg 38.33×):
    Forward PE 56.26× is +46.8% above the 5yr avg → >20% above → +10 (already at ceiling; no
    net effect since FwdPE_Score is already capped at 100)

Raw weighted score = 85.20×0.40 + 100.00×0.40 + 100.00×0.20
                   = 34.08 + 40.00 + 20.00
                   = 94.08
```

Forward PE (56.26×) sits **above even the 5-year historical high (49.28×)** — regardless of the acknowledged coarseness of the 5-annual-point reconstruction (§2.9), this conclusion (currently priced above its own trailing 5-year peak multiple) is not sensitive to that imprecision.

### 5.3 Fair Value work (feeds the Upside/Downside Modifier)

**Method A — 3-scenario DCF** (Rule 7). WACC built from CAPM: risk-free rate = 10Y UST 4.54%, Equity Risk Premium ≈5.5% (standard assumption), Beta 1.394 (Yahoo) → Cost of equity ≈ 4.54% + 1.394×5.5% ≈ 12.2%; used as base-case WACC since ASML carries negligible net debt (WACC ≈ cost of equity). Bull/Bear WACC varied ±1pp per Rule 2. FCF base year = FY2025 actual (€11.08B). Stage 1 = 2026–2030 (aligned with ASML's own 2030 Investor Day framework), Stage 2 = Gordon-growth terminal.

| Scenario | WACC | Terminal g | Stage-1 FCF growth/yr | DCF EV (EUR) | + Net cash | Equity value/share (EUR) | (USD @1.143) |
|---|---|---|---|---|---|---|---|
| Bull | 11.0% | 3.0% | 18% (aligned with 2030 €60B high end) | €260.5B | +€5.67B | €690.6 | **$789.3** |
| Base | 12.0% | 2.5% | 10% (aligned with 2030 ~€52B midpoint) | €161.8B | +€5.67B | €434.6 | **$496.8** |
| Bear | 13.0% | 2.0% | 3% (cyclical pause, ~2022–23 pattern repeat) | €107.0B | +€5.67B | €292.4 | **$334.2** |

**Method B — Comparable multiples:**
```
Historical PE (trailing) = 5yr avg PE 38.33× × trailing diluted EPS (EUR 24.71 → $28.24) = $1,082.6
Historical PE (forward)  = 5yr avg PE 38.33× × consensus FY2026 EPS $31.948            = $1,224.6
EV/EBIT @ 25× = (13,397.6×25 + net cash 6,481.4)/385.418 shares                        = $885.9
EV/EBIT @ 30× = (13,397.6×30 + net cash 6,481.4)/385.418 shares                        = $1,059.6
Base multiples value (avg of above 4)                                                  = $1,063.2

Bull multiples: EV/EBIT @ 35× ($1,233.5) + Historical-PE-at-5yr-high 49.28×EPS ($1,574.5), avg  = $1,404.0
Bear multiples: EV/EBIT @ 17.75× ($634.2) + Historical-PE-at-5yr-low 34.25×EPS ($967.2), avg    = $800.7
```

**Triangulation (40% DCF / 60% Multiples, per fair-value-methodology.md):**
```
Bull blended FV = 0.40×789.3 + 0.60×1,404.0 = $1,158.1
Base blended FV = 0.40×496.8 + 0.60×1,063.2 = $836.7
Bear blended FV = 0.40×334.2 + 0.60×800.7   = $614.1

PW Fair Value = 0.25×1,158.1 + 0.50×836.7 + 0.25×614.1 = $861.4
```

⚠️ Both the DCF (even the bull case, at $789–$1,158/share range) and the blended PW Fair Value ($861.4) sit **well below** the current live price ($1,797.32) — and also well below the sell-side analyst mean target ($1,877.31, "strong buy" consensus, 15 analysts). This divergence between a bottom-up, cash-flow-anchored fair value and prevailing sell-side sentiment is flagged explicitly and discussed in §6 — it is not treated as a contradiction to be smoothed over.

### 5.4 Upside/Downside Modifier

```
Gap Upside% = (861.4 / 1,797.32) − 1 = −52.07%
Catalyst window: no specific 18–24mo re-rating catalyst identified (guardrail applies to the
  upside side only, per fair-value-methodology.md — this is a downside gap, so the guardrail's
  cap does not apply here); default 2yr window used.
Annualized gap = −52.07% / 2 = −26.04%/yr

Intrinsic growth rate = diluted EPS 3yr CAGR (FY2022→FY2025) = (24.71/14.13)^(1/3) − 1 = +20.48%/yr
Shareholder yield = dividend yield 0.49% + net buyback yield
  (shares outstanding: 394,589,411 FY2022 → 385,417,665 FY2025, a 2.32% reduction over 3 years
  ≈ 0.775%/yr average) = 0.49% + 0.775% = 1.265%/yr

E = −26.04% + 20.48% + 1.265% = −4.30%/yr

E < 0 → M = 5 + 10 × clamp((−E)/10pp, 0, 1) = 5 + 10 × clamp(4.30/10, 0, 1) = 5 + 4.30 = +9.30
```

### 5.5 Final Valuation Score

```
Final Score = Raw weighted (94.08) + Rate Environment Gate (+10) + Upside/Downside Modifier (+9.30)
            = 113.38  →  clamp to 100.0 maximum
```

**Valuation Score = 100.0 / 100.0 — the maximum on this framework's scale (most expensive).** This conclusion is **robust to reasonable variation** in the Fair Value assumptions above: the raw weighted score plus the Rate Environment Gate alone (94.08 + 10 = 104.08) already exceeds 100 before the Upside/Downside Modifier is even applied — the modifier would need to swing to roughly **−4.1 or more negative** (requiring an implausibly strong E, ≥ ~14%/yr) to pull the final score below 100.0 at all. Every current-multiple sub-score (FCF Yield, EV/EBIT, Forward PE) independently confirms extreme richness.

---

## 6. Composite Score (Quality + Valuation)

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 81.5) + 0.50 × 100.0
                = 0.50 × 18.5 + 50.0
                = 9.25 + 50.0
                = 59.25  →  rounds to 59.3 (exact ".X5" boundary — rounds up per the framework's
                  explicit tie-break rule)
```

**Composite Score = 59.3 — falls in the 50.0–69.9 band: HOLD — watch only, no new entry, no trim (per the current Phase 03/05 Action Table, read against the Composite Score as valuation-scoring.md directs once a Quality Score exists).**

This is a genuinely interesting outcome to spell out plainly: ASML clears the Quality Gate comfortably and would, on quality alone, be one of the stronger companies this framework has scored — but its Valuation Score sits at the absolute maximum (100.0, most expensive). The 50/50 blend is specifically designed to weigh these equally rather than let either axis dominate, and here it lands the combined number in the **middle "Fair Value / Hold" band**, not in the "cheap enough to buy" bands nor pinned at the "extremely expensive" end the raw valuation number alone would suggest. **This is the mechanism working as designed, not a coincidence to be second-guessed** — see valuation-scoring.md's own Company A/C worked example, which shows the same dynamic.

---

## 7. Order Setup

**Not applicable.** Per fair-value-methodology.md, the buy/sell/stop/position-sizing order setup is only produced for a BUY or TRIM action. A Composite Score of 59.3 (50.0–69.9 band) maps to **"Watchlist only — no new entry, no trim"** — there is no order to set up. The Blended (PW) Fair Value estimate ($861.4, §5.3) and its scenario range ($614.1 bear – $1,158.1 bull) are recorded above for reference and for the Upside/Downside Modifier calculation, not as an actionable buy price.

---

## 8. Qualitative Notes

1. **Trigger accuracy:** the Telegram post's framing ("heading into earnings season") is independently confirmed — ASML has not yet reported Q2 2026 results as of this session, with reporting expected within days (historical mid-July cadence, corroborated by contemporaneous press coverage). The post named no financial figures that needed verifying beyond that framing.
2. **Quality is genuinely strong but narrowly clears the bar (81.5 vs. an 80.0 gate).** The two components holding it back from a much higher score are (a) Margins (65.75/100 — a 52.6% gross margin is strong in absolute terms but well below the 80% ceiling this sub-score scales against, unlike a pure-software company), and (b) Moat (60/100 — capped by the framework's strict "cited source or the signal doesn't count" rule; ASML's scale advantage is real and widely discussed but no citable cost-per-unit comparison against a same-category competitor exists, because none is being made in EUV).
3. **Every current-valuation metric is stretched to or past this framework's most expensive bucket:** FCF yield 1.48% (framework ceiling is ≤0% → 100), EV/EBIT 51.2× (ceiling ≥35× → 100), Forward PE 56.3× above even its own 5-year historical high (49.3×). The stock made a fresh all-time high ($1,999.96) in the days before this session before pulling back roughly 10% to $1,797.32.
4. **Bottom-up fair value vs. sell-side sentiment — a real, disclosed divergence.** This session's scenario-weighted DCF+multiples work puts fair value around $861 (range $614 bear–$1,158 bull), well below both the current price and the sell-side analyst mean target ($1,877, "strong buy" consensus across 15 analysts). Sell-side targets are typically anchored to prevailing multiples and forward narrative rather than a standalone cash-flow build — this framework's own discipline (Rule 7's scenario-weighted, bear-underwritten approach) is why the two diverge, and that divergence is reported rather than reconciled away.
5. **AI/advanced-node demand is the real growth story here**, and it is well-documented (not invented): ASML's own November 2024 Investor Day 2030 framework (€44–60B revenue, 56–60% gross margin), a record €38.8B backlog, and FY2026 guidance of €36–40B all support the +10 Growth modifier applied in §3.3. Whether that translates into a valuation currently supported by cash flows is a separate question — this session's answer is "not yet, on the numbers as they stand today."
6. **Data gaps flagged (not invented around):** (a) Owner Earnings maintenance-vs-growth CapEx split unavailable — standard FCF used; (b) 5yr historical PE range built from 5 annual snapshots rather than ~20 quarterly points, since ASML's 6-Ks aren't XBRL-tagged — flagged as coarser, though directionally unambiguous; (c) Q1 2026's abbreviated balance sheet doesn't itemize current-vs-noncurrent debt — doesn't change the net-cash conclusion either way.

---

## 9. Recommendation

# **WATCHLIST ONLY — Composite Score 59.3 (Hold / no new entry, no trim band). Do not enter now.**

ASML clears this framework's 80.0+ Quality Score gate (81.5/100.0) — a strong quality read anchored in exceptional profitability, a deep net-cash balance sheet, and a well-documented (though not maximal) monopoly moat in EUV lithography. Its Valuation Score, however, sits at the scale's maximum (100.0/100.0) — every current multiple (FCF yield, EV/EBIT, Forward PE) reads as extremely expensive, and this framework's own scenario-weighted fair-value work (~$861, vs. a $1,797.32 live price) does not support the current price even under a fairly generous bull case. The 50/50 Composite Score blend lands at **59.3**, squarely in the **50.0–69.9 "Hold — watch only, no new entry, no trim"** band. **No order setup, no entry, no position opened.**

---

## 10. Next Review Trigger

- **Q2 2026 earnings** (Rule 9 mandatory trigger) — expected within days of this session per historical cadence and contemporaneous press coverage; will refresh the TTM window this session had to reconstruct from FY2025+Q1 2026, and may move both the Growth sub-score (if backlog/guidance move materially) and the Upside/Downside Modifier's E calculation.
- **Any subsequent pullback toward this session's PW Fair Value (~$861) or bull-case DCF (~$1,158)** — would meaningfully move the Valuation Score (and thus Composite) toward a more attractive band even with an unchanged Quality Score, since the current Valuation Score is pinned at its 100.0 ceiling with real headroom to fall.
- Any guidance revision, management change, or M&A (Rule 9 standard triggers).
- Any >15% unexplained move from today's $1,797.32 reference (distinct from a >15% move *explained* by earnings, which is Rule 9's earnings trigger, not this one).

**No position opened — nothing to log in `decisions/`.**

---

## Glossary

- **20-F (Form 20-F)** — The annual report US-listed foreign private issuers (like ASML, a Dutch company) file with the SEC — the international equivalent of a US company's 10-K.
- **6-K (Form 6-K)** — A report foreign private issuers furnish to the SEC to disclose material information (results, press releases) between annual 20-F filings — roughly the international equivalent of a US company's 8-K.
- **ADR (American Depositary Receipt)** — A US-exchange-listed security representing shares of a non-US company; ASML's NASDAQ listing is technically a NY Registry Share (see below), a related but distinct structure.
- **AGM (Annual General Meeting)** — A public company's yearly shareholder meeting; ASML's April 2026 AGM results were among the SEC 6-Ks reviewed this session.
- **Backlog** — The dollar value of signed customer orders not yet recognized as revenue; ASML's stood at a record €38.8 billion entering 2026.
- **Beta** — A stock's sensitivity to overall market moves; used here (1.394, Yahoo) as an input to estimating ASML's cost of equity/WACC.
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate between a start and end value.
- **CapEx** — Capital Expenditure — money spent buying or upgrading physical assets.
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every company that files with EDGAR; used to construct this session's SEC filing/XBRL API paths.
- **Composite Score** — This framework's blended Quality + Valuation ranking number (0.50 × (100 − Quality Score) + 0.50 × Valuation Score); ASML's is 59.3.
- **D&A** — Depreciation & Amortization — the non-cash accounting expense that spreads the cost of long-lived assets over time.
- **DCF (Discounted Cash Flow)** — A valuation method estimating a company's worth today by projecting future cash flow and discounting it back to present value.
- **DUV (Deep Ultraviolet Lithography)** *(new — not yet in glossary.md)* — An older chip-lithography technology using longer-wavelength UV light than EUV, suitable for less advanced chip nodes; ASML's nominal lithography competitors (Nikon, Canon) manufacture only DUV tools, not EUV, which is why ASML's EUV market share is effectively 100%.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating profit before financing/accounting effects.
- **Effective tax rate** — The actual percentage of pretax income paid as tax in a given period.
- **EPS** — Earnings Per Share, net income divided by shares outstanding.
- **Equity Risk Premium (ERP)** — The extra return equity investors demand over the risk-free rate, on average, for holding stocks; an assumed input (here ~5.5%) to estimating cost of equity via CAPM.
- **EUV (Extreme Ultraviolet Lithography)** *(new — not yet in glossary.md)* — The most advanced chip-manufacturing lithography technology, using 13.5-nanometer-wavelength light to print the smallest, most advanced transistor patterns (5nm/3nm/2nm nodes). ASML is the sole global manufacturer of EUV lithography systems — the central fact behind its Moat Signal findings and Growth-modifier evidence in this session.
- **EV** — Enterprise Value — a company's total value to all capital providers (market cap + debt − cash).
- **EV/EBIT** — Enterprise Value divided by EBIT — a multiple measuring how expensive a company is relative to its operating profit.
- **EY (Earnings Yield)** — 1 ÷ Forward PE, expressed as a yield comparable to bond yields.
- **Fast Grower** — Peter Lynch's term for a company growing EPS faster than 15%/year for 3+ years; ASML does not qualify (lumpy, cyclical EPS history), so PEG was not scored.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself.
- **FCF Yield** — Free Cash Flow ÷ Market Cap; higher means cheaper.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income; checks whether reported accounting profit is turning into real cash.
- **Forward PE** — Price ÷ next-twelve-months expected earnings per share.
- **FX (foreign exchange) rate** — The price of converting one currency into another; this session used IBKR's own live EUR/USD rate (1.143) to convert ASML's EUR-denominated financials for comparison against its USD market price.
- **GAAP** — Generally Accepted Accounting Principles — the standard US accounting rulebook; ASML files its 20-F under US GAAP.
- **Hard disqualifier** — A Quality Score condition that fails a company regardless of its weighted score; none fired for ASML.
- **High-NA (High Numerical Aperture) EUV** *(new — not yet in glossary.md)* — ASML's next-generation EUV lithography platform, using a larger lens numerical aperture to print even smaller chip features than standard ("Low-NA") EUV tools; priced substantially higher per unit (~$380M) than prior-generation EUV systems, cited as pricing-power/Brand-premium Moat Signal evidence in this session.
- **Hurdle rate** — The minimum acceptable annual return for an investment to be worth making; this framework uses 10% as the Upside/Downside Modifier's hurdle.
- **Invested Capital** — The total capital (debt + equity, netted for cash) put to work in a business; the denominator of ROIC.
- **Moat** — A durable competitive advantage protecting a business's profits from competitors.
- **Net Debt/EBITDA** — A leverage ratio measuring how many years of operating cash profit it would take to pay off all debt (negative = net cash); this framework's primary balance-sheet-risk gate. ASML is at −0.44×.
- **Net Margin** — Net Income ÷ Revenue.
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate); the numerator used to compute ROIC.
- **NY Registry Share** *(new — not yet in glossary.md)* — A form of direct US stock-exchange listing used by some non-US companies (including ASML), in which the New York-listed shares represent the underlying home-market ordinary shares one-for-one, without the depositary-bank structure of a conventional ADR.
- **PE (Price-to-Earnings) ratio** — Share price ÷ earnings per share.
- **PEG ratio** — PE ratio ÷ earnings growth rate — not scored for ASML (not a Fast Grower).
- **pp (percentage points)** — A direct difference between two percentages.
- **PT (Price Target)** — An analyst's forecast of where a stock's price will be at a future date; ASML's sell-side mean target ($1,877.31) is discussed qualitatively, never as a scored input.
- **PW (Probability-Weighted) Fair Value** — This framework's blended fair value estimate (25% bull + 50% base + 25% bear); ASML's is $861.4/share.
- **Quality Score** — This framework's 0.0–100.0 continuous score grading Phase 01 criteria; 80.0+ required to proceed to valuation scoring. ASML scored 81.5.
- **R&D (Research & Development)** *(new — not yet in glossary.md)* — Company spending on developing new products/technology, expensed on the income statement (as distinct from CapEx, spent on physical assets); ASML's R&D costs (~€1.18–1.2B/quarter) are a major driver of the sustained technology lead behind its EUV moat.
- **Rate Environment Gate** — The mandatory pre-check before Phase 02 scoring, comparing Earnings Yield to the 10-Year Treasury yield.
- **Rate Regime Modifier** — An additive score adjustment based on the current 10-Year Treasury yield bracket.
- **ROIC** — Return on Invested Capital — how efficiently a company turns invested capital into profit.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 7** — This framework's mandatory 3-scenario (bull/base/bear) valuation approach, probability-weighted 25/50/25.
- **Rule 9** — Fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move.
- **Shareholder yield** — Cash returned to shareholders as a percentage of share price — dividend yield plus net buyback yield.
- **Terminal Value** — In a multi-stage DCF, the lump-sum value assigned to all cash flows beyond the explicit forecast period.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results.
- **Upside/Downside Modifier** — An additive ±15 adjustment to the valuation score based on expected annual return; ASML's computed at +9.30 (expected mild annual loss).
- **Valuation score** — This framework's 0.0–100.0 continuous score (0 = cheapest, 100.0 = most expensive); ASML scored 100.0, the maximum.
- **WACC** — Weighted Average Cost of Capital — the blended discount rate used in a DCF; ~12% (base case) for ASML, derived via CAPM.
- **XBRL (eXtensible Business Reporting Language)** — The structured, machine-readable format the SEC requires financial-statement figures to be tagged in; used here to pull ASML's 20-F figures directly, though its 6-K interim filings are not XBRL-tagged (a flagged data gap).

# NEW POSITION — MCO (Moody's Corporation, NYSE) — 2026-07-19

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, first-ever evaluation)
**Date:** 19 Jul 2026 (Sunday)
**10Y US Treasury Yield:** 4.10% (FRED `DGS10`, most recent posted observation dated 2026-07-16 — normal FRED reporting lag)
**Current MCO portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None — first-ever `/new-position` or `/rescore` pass on this ticker (no existing file in `watchlist/in-portfolio/MCO/` or `watchlist/not-in-portfolio/MCO/`, confirmed before this session)
**Sector:** Financials — Credit rating agency (Moody's Investors Service, "MIS") and data/analytics/software provider (Moody's Analytics, "MA")
**First-use jargon decode:** see closing Glossary (§11)

---

## 0. Why this session exists — trigger source

A post on **bolshegold** (Telegram, post bolshegold/9795, ~09:46 UTC 2026-07-19) named several tickers including "$MCO" among "финансы, инвестиции и кредитный карты" (finance/investment/credit-card) companies worth reading earnings reports from for a market-health read, with no specific claim about MCO's fundamentals. Per this repo's standing convention, a first-ever mention of a name with no watchlist entry triggers a full `/new-position` evaluation regardless of the mention's substance. MCO has no existing watchlist entry and is not a current holding, so this session is that evaluation, built entirely from independently-sourced primary data. **The Telegram post's text is not used as a financial input anywhere below.**

Confirmed via SEC EDGAR (CIK 0001059556): MCO's most recent 10-Q was filed 2026-04-23 (Q1 2026); no Q2 2026 earnings 8-K has been filed as of this session. MCO's Q2 2025 10-Q was filed 2026-07-24 last year — by that same-week pattern, Q2 2026 results are due this coming week, consistent with the Telegram post's framing. **Q2 2026 results are not yet available and are not used anywhere in this session.**

---

## 1. Live Price (Rule 0)

Contract confirmed via `search_contracts("MCO")`: contract_id **6497**, exchange **NYSE**, description "MOODY'S CORP" (other results — a Mexican cross-listing, an unrelated Australian company also ticker "MCO," various unrelated bond/fund tickers — not used).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$510.86** | IBKR `get_price_snapshot`, `last` field, contract_id **6497**. `is_close: true` — last completed-session close, since today (Sunday 2026-07-19) markets are closed; per Rule 0 this is still the most recent price obtainable via a live fetch, flagged as a close rather than an intraday quote. |
| 52-week high | $545.44 | IBKR `misc_statistics` `high_52w` |
| 52-week low | $401.90 | IBKR `misc_statistics` `low_52w` |
| 13-week high | $523.18 | IBKR `misc_statistics` |
| 26-week high | $532.90 | IBKR `misc_statistics` |
| Open 52 weeks ago | $499.82 | IBKR `misc_statistics` `open_52w` |
| Dividend yield | 0.77% | IBKR `get_price_snapshot` `dividend_yield` |
| US 10Y Treasury yield | 4.10% | FRED `DGS10`, as-of 2026-07-16 |

$510.86 sits well below the 52-week high ($545.44, −6.3%) and well above the 52-week low ($401.90, +27.1%) — context only, not scored.

Current shares outstanding: **174.7M** (dei:EntityCommonStockSharesOutstanding, Q1 2026 10-Q cover page, as of 2026-03-31 — most recent confirmed count; likely modestly lower today given the Q1 2026 buyback pace noted in §3.5). Market cap = 174.7M × $510.86 = **$89,247M**, cross-checked against stockanalysis.com's independently-reported $89.24B (exact match).

---

## 2. Data Gathered — Sources & Method

`yfinance` failed in this session's environment with the same `curl_cffi` TLS/connection-reset error documented in prior sessions (JPM, C, SOFI, AXP, etc.). **Fallback used:** SEC EDGAR XBRL `companyconcept` API (`data.sec.gov/api/xbrl/companyconcept/CIK0001059556/...`) for every primary financial figure below, MCO's own FY2025 10-K (filed 2026-02-18, accession 0001628280-26-009136) for narrative/MD&A evidence, and stockanalysis.com / third-party sources (cross-verified, never relied on alone) for market-facing figures (forward PE, consensus estimates, analyst price targets, 5-year historical PE reconstruction). MCO's CIK is **1059556**.

Unlike the JPM/Citigroup/SOFI/AXP financial-company sessions, **MCO discloses a clean, standard GAAP EBIT/EBITDA and Cost-of-Revenue line** — it is a fee-based services/data company, not a deposit-funded lender, so none of that structural "N/M" gap applies here. All Quality Score sub-scores are directly computable from filed financials.

### 2.1 Income statement, cash flow, balance sheet (FY2021–FY2025, SEC XBRL, all in $M)

| FY | Revenue | Net Income | EBIT (Op. Income) | D&A | EBITDA | Cost of Revenue | OCF | CapEx | FCF | FCF/NI |
|---|---|---|---|---|---|---|---|---|---|---|
| 2021 | 6,218 | 2,214 | 2,844 | 257 | 3,101 | 1,637 | 2,005 | 139 | 1,866 | 84.3% |
| 2022 | 5,468 | 1,374 | 1,883 | 331 | 2,214 | 1,613 | 1,474 | 283 | 1,191 | 86.7% |
| 2023 | 5,916 | 1,607 | 2,137 | 373 | 2,510 | 1,687 | 2,151 | 271 | 1,880 | 117.0% |
| 2024 | 7,088 | 2,058 | 2,875 | 431 | 3,306 | 1,945 | 2,838 | 317 | 2,521 | 122.5% |
| 2025 | 7,718 | 2,459 | 3,351 | 480 | 3,831 | 1,973 | 2,901 | 326 | 2,575 | 104.7% |

**FCF positive all 5 years, FCF/NI conversion >70% every year** — clears both cash-flow hard disqualifiers with a wide margin.

FY2025 balance sheet: Total debt $6,994M (all long-term, no current portion at year-end), Cash $2,384M, Equity $4,054M → Net debt $4,610M, Invested Capital (Debt+Equity−Cash) $8,664M.

Effective tax rate FY2025 = Income tax expense $668M ÷ Pretax income $3,130M = **21.34%**.

### 2.2 A Q1 2026 sensitivity worth flagging up front

Q1 2026 (ended 2026-03-31, most recent 10-Q) shows a sharp one-quarter swing: Equity fell to $2,994M (from $4,054M at FY2025-end), Cash fell to $1,469M, and Total debt rose to $7,539M ($6,963M long-term + $576M reclassified current). **Cause, confirmed via XBRL:** Q1 2026 share buybacks alone were **$1,471M** — exceeding the *entire* FY2025 full-year buyback total ($1,607M) in a single quarter — plus a $185M dividend, against only $661M of Q1 net income. This is an unusually large, one-quarter capital-return event, not a leverage/credit deterioration signal (MCO remains solidly investment-grade with a low Net Debt/EBITDA under any reading — see §3.4). It matters here because it happens to sit right at the Quality Score's 80.0 gate — see §3.5.

### 2.3 Growth, moat, and TAM evidence (MCO's own FY2025 10-K, MD&A section)

- **Segment revenue growth (actual, reported FY2025 vs FY2024):** MIS (ratings) revenue $4,119M, **+9% YoY** ("strong investor demand and tight credit spreads supported revenue growth in all ratings LOBs"); MA (analytics) revenue $3,599M, **+9% YoY**, organic constant-currency growth +7%, **ARR +8%**, recurring-revenue organic cc growth +8%.
- **Pricing power (actual, reported, not guidance):** "Recurring revenue increased $38 million, primarily reflecting the impact of **annual price increases** and higher monitored credits" (MIS Corporate Finance Group commentary, FY2025 vs FY2024) — a price increase realized *and* accompanied by higher (not lower) monitored-credit volume, i.e. no visible customer loss from the increase.
- **Structural TAM-expansion drivers cited (MD&A "Prospects for Growth"):** Private Credit ratings demand, expansion of the market for "integrated data and analytics solutions," Decision Solutions growth (Insurance +15%, KYC +19% revenue in FY2025, both driven by new-product/subscription demand, not just price).
- **Recurring revenue base:** For MA, "subscription-based revenue and software maintenance revenue"; for MIS, "recurring monitoring fees... programs such as commercial paper, medium-term notes and shelf registrations" — both segments run on a substantially recurring-revenue model (own 10-K definition, §11 Glossary).
- **Disruption-vector risk (own 10-K, Item 1A):** Moody's explicitly flags Gen AI/agentic AI as a competitive risk — competitors "may use these tools to deliver solutions at lower prices," and customers may increasingly use "free or lower-cost information... from alternative sources" or build "alternative, proprietary systems for assessing credit risk." A real, company-acknowledged disruption vector, not dismissed here — but not yet visible in the actual, reported growth numbers above.

### 2.4 Market share and moat (third-party, cross-checked)

Independent citation (Council on Foreign Relations, via Wikipedia's "Big Three" summary): the three dominant global credit rating agencies (Moody's, S&P Global, Fitch) have collectively held **~95% combined global market share** for well over a decade, with **Moody's and S&P each around 40%**, Fitch around 15% — a long-running, stable oligopoly/duopoly structure, not a recent or fragile one. NRSRO status (SEC-designated, held by only a handful of firms, referenced by name in bond covenants and regulatory capital rules) is the regulatory mechanism underpinning this stability (own 10-K, §2.3 above).

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI <70% for 2+ consecutive years w/o growth-capex explanation | 84.3% / 86.7% / 117.0% / 122.5% / 104.7% (FY2021–FY2025) — every year above 70% | disqualify if 2+ consecutive years sub-70% | ✅ **PASS** |
| Net Debt/EBITDA over threshold | 1.20× (FY2025-end) / 1.55× (Q1-2026-end, see §3.5) | disqualify if >2.5× (or >4× asset-light) | ✅ **PASS** on either basis |
| FCF-positive 3+ consecutive years | All 5 of the last 5 fiscal years positive | disqualify if not | ✅ **PASS** |

**No hard disqualifier fires**, under either balance-sheet basis discussed in §3.5.

### 3.2 Profitability (25% weight)

```
Net Margin (FY2025) = 2,459 / 7,718 = 31.86%
NetMargin_Component = clamp((31.86/30)×100, 0, 100) = 100.0   (clamped — above the 30% ceiling)

NOPAT (FY2025) = EBIT × (1 − effective tax rate) = 3,351 × (1 − 0.2134) = 2,635.8
Invested Capital (FY2025-end) = Debt 6,994 + Equity 4,054 − Cash 2,384 = 8,664
ROIC = 2,635.8 / 8,664 = 30.42%
ROIC_Component = clamp((30.42/30)×100, 0, 100) = 100.0   (clamped)

Profitability_Score = (100.0 + 100.0) / 2 = 100.0   (no FCF-positivity cap — 5yr positive, §3.1)
```

### 3.3 Margins (15% weight)

```
Gross Margin analog = (Revenue − Cost of Revenue) / Revenue = (7,718 − 1,973) / 7,718 = 74.44%
GrossMargin_Score = clamp((74.44/80)×100, 0, 100) = 93.05
```
No structural-trend bonus applies — margin is already well above the 40% threshold the +10 bonus is gated on (trend itself is roughly flat: 73.7% FY2021 → 74.4% FY2025).

### 3.4 Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $5,468M → FY2025 $7,718M) = (7,718/5,468)^(1/3) − 1 = 12.17%
Growth_Score (raw) = clamp((12.17/25)×100, 0, 100) = 48.70
```
**TAM/pricing-power modifier (+10):** documented, actual (not guidance) evidence — FY2025 revenue growth of 9% in *both* segments, MA's ARR +8% and recurring-revenue organic cc growth +8%, MIS's "annual price increases" realized alongside higher (not lower) monitored-credit volume, and Decision Solutions' Insurance (+15%) and KYC (+19%) product-line growth (§2.3). Guidance (MCO's own FY2026 EPS guidance) is **not** used as evidence here, per this framework's standing rule that self-issued guidance is a re-valuation trigger, not a scored input.

**No deceleration modifier:** YoY revenue growth ran +8.2% (FY22→23), +19.8% (FY23→24, a rebound from the 2022 rate-hike-driven bond-issuance trough), +8.9% (FY24→25) — choppy, cyclically tied to bond-issuance volume, but not a clean *structural* deceleration trend (the opposite of DUOL's guided, secular DAU-growth slowdown, for contrast).
```
Growth_Score = 48.70 + 10 = 58.70
```

### 3.5 Balance Sheet (15% weight) — two computable bases, a genuine sensitivity

Net Debt/EBITDA is fully computable here (unlike the JPM/C/SOFI/AXP bank-model gap) — but which balance-sheet snapshot to pair with which EBITDA figure is a real judgment call, given the unusually large Q1 2026 buyback (§2.2):

```
FY2025-end basis (primary — see reasoning below):
  Net Debt = 6,994 − 2,384 = 4,610      EBITDA (FY2025) = 3,831
  Net Debt/EBITDA = 4,610 / 3,831 = 1.203×
  BalanceSheet_Score = clamp(100×(1 − 1.203/4), 0, 100) = 69.92

Q1-2026-end basis (sensitivity — most current available quarter):
  Net Debt = 7,539 − 1,469 = 6,070      EBITDA (TTM Apr2025–Mar2026) = 3,916
  Net Debt/EBITDA = 6,070 / 3,916 = 1.550×
  BalanceSheet_Score = clamp(100×(1 − 1.550/4), 0, 100) = 61.25
```

**Basis used: FY2025 fiscal year-end** (complete, fully audited 10-K figures) — the cleanest, most defensible data point, and unaffected by a single quarter's unusually large, one-off-sized buyback. The Q1 2026 sensitivity is shown transparently because it is real, computable, and — as §3.6 shows — it is close enough to the 80.0 gate to matter. Neither basis is remotely close to the 2.5× standard (or 4× asset-light) hard-disqualifier threshold — this is a scoring-precision sensitivity, not a leverage-risk finding. *(Upgrade 5's asset-light /6-denominator override was considered but not applied — MCO's "net" interest expense figure bundles tax-related interest and interest income, so a clean gross interest-coverage ratio for the >15× test isn't independently derivable from the data available this session; not needed regardless, since the standard 2.5× threshold already clears comfortably either way.)*

### 3.6 Moat Signal (15% weight)

| Signal | Evidence | Result |
|---|---|---|
| Market share stable/growing | Big Three (Moody's/S&P/Fitch) ~95% combined global share, Moody's ~40%, a stable multi-decade duopoly/oligopoly (CFR, third-party, §2.4); MIS revenue +9% YoY FY2025 | ✅ TRUE |
| Brand premium (pricing power) | "Annual price increases" realized in MIS recurring revenue FY2025, accompanied by *higher* monitored-credit volume, not lower (§2.3) — actual, reported, not guidance | ✅ TRUE |
| Network effect | No documented two-sided-marketplace or user-growth-driven-value mechanism found this session for the ratings/analytics business model | ❌ not established |
| Switching costs | NRSRO regulatory status — only a handful of SEC-designated NRSROs, ratings referenced by name in bond covenants and institutional/regulatory capital mandates (own 10-K, §2.3; NRSRO glossary entry) | ✅ TRUE |
| Scale cost advantage | No cost-per-unit citation vs. smaller CRAs/analytics vendors found this session | ❌ not established |

```
Moat_Score = (3/5) × 100 = 60.0
```

### 3.7 FCF Quality (10% weight)

```
FCF/NI (FY2025) = 2,575 / 2,459 = 104.72%
FCFQuality_Score = clamp(((1.0472 − 0.40)/0.60)×100, 0, 100) = clamp(107.87) = 100.0   (clamped)
```

### 3.8 Quality Score — final, and the gate margin

```
Quality Score = 0.25×Profitability + 0.15×Margins + 0.20×Growth + 0.15×BalanceSheet + 0.15×Moat + 0.10×FCFQuality

FY2025 basis (primary):
= 0.25×100.0 + 0.15×93.05 + 0.20×58.70 + 0.15×69.92 + 0.15×60.0 + 0.10×100.0
= 25.00 + 13.9575 + 11.740 + 10.488 + 9.00 + 10.00
= 80.18  →  rounded 80.2

Q1-2026 sensitivity basis (Balance Sheet + Profitability recomputed on that snapshot):
= 78.70  →  rounded 78.7
```

**Quality Score used: 80.2 — clears the 80.0+ gate, but by only 0.2 points**, and the margin is entirely attributable to which balance-sheet snapshot is paired with the score (§3.5). This is flagged prominently and carried through to the final recommendation (§8) — it is not treated as a comfortable pass.

---

## 4. Rate Environment Gate

```
Forward PE = Live Price / Consensus FY2026 EPS = 510.86 / 16.76 = 30.48×
  (Consensus EPS $16.76, 21 analysts, stockanalysis.com — falls within MCO's own guided range
   $16.40–$17.00, cross-consistent; guidance itself not used as the scored figure)

Step 1 — Earnings Yield Spread Test:
  EY = 1/30.48 = 3.28%
  Spread = EY − 10Y Treasury = 3.28% − 4.10% = −0.82pp
  Spread < +1.5% → +5 additive (yellow flag, not a veto)

Step 2 — Rate Regime Modifier:
  10Y yield 4.10% falls in the 3.5–5% bracket → +5

Total Rate Environment Gate modifier = +10
```

---

## 5. Phase 02 — Valuation Score

### 5.1 FCF Yield (40% weight)

```
FCF Yield = TTM FCF / Market Cap = 2,747 / 89,247 = 3.08%
  (TTM FCF, Apr 2025–Mar 2026 = FY2025 FCF 2,575 − Q1 2025 FCF 672 + Q1 2026 FCF 844,
   using OCF−CapEx for each quarter: Q1'25 OCF 757−CapEx 85=672; Q1'26 OCF 939−CapEx 95=844)
FCF_Score = clamp(100×(1 − 3.08/10), 0, 100) = 69.22
```

### 5.2 EV/EBIT (25% weight — redistributed to 40%, see §5.4)

```
EV = Market Cap + Net Debt (Q1 2026-end, most current — a valuation "as of today" input, unlike
     the Quality Score's balance-sheet basis choice in §3.5) = 89,247 + 6,070 = 95,317
EBIT (TTM, Apr 2025–Mar 2026) = 3,427
EV/EBIT = 95,317 / 3,427 = 27.82×
EV/EBIT_Score = clamp((27.82 − 12)/23 × 100, 0, 100) = 68.75
```

### 5.3 Forward PE (20% weight)

5-year trailing PE reconstructed via the `valuation-scoring.md`-documented method (`yfinance` unavailable, so IBKR 5-year daily closes paired with a TTM-EPS series built directly from 20 quarters of SEC XBRL-reported diluted EPS, 2021-06-30 through 2026-03-31; earliest data point uses a price ~3 weeks after the exact quarter-end since IBKR's history begins 2021-07-22, flagged as a minor approximation):

```
5yr avg PE = 37.79×   5yr low = 29.05×   5yr high = 44.81×   (n=20 quarters)

FwdPE_Score = clamp((30.48 − 29.05)/(44.81 − 29.05) × 100, 0, 100) = 9.08

Historical PE Modifier (Upgrade 2): Forward PE vs 5yr avg = (30.48 − 37.79)/37.79 = −19.34%
  — close to, but not past, the "−20% or more" threshold for the −10 discount. Treated as
  falling in the undefined gray zone between ±10% and ±20% and left at 0 (no modifier), the
  more conservative reading rather than crediting an extra discount right at the edge.

FwdPE_Score (final) = 9.08
```

### 5.4 PEG — not applied (redistributed to EV/EBIT)

EPS growth exceeded 15% in each of the last 3 fiscal years (FY2023 +17.3%, FY2024 +29.0%, FY2025 +21.4%; 3yr CAGR 22.5%) — mechanically a Fast Grower. **Not applied, per Upgrade 3's explicit "never apply to cyclicals" carve-out**: FY2022 EPS *fell* 36.8% YoY, a rate-hike-driven bond-issuance trough (own 10-K risk factor: "economics of the Company's business is dependent on the volume of debt securities issued... in global capital markets"). The subsequent 3 years of >15% growth are materially a recovery/mean-reversion off that depressed base, not a clean structural growth pattern — the same "unreliable earnings base" concern the 2026-06-20 PEG clarification was written for, here from cyclicality rather than a one-off item. PEG's 15% weight is redistributed to EV/EBIT (→ 40%), per the Final Score Formula note.

### 5.5 Raw weighted score

```
Raw Score = 0.40×FCF_Score + 0.40×EV/EBIT_Score + 0.20×FwdPE_Score
          = 0.40×69.22 + 0.40×68.75 + 0.20×9.08
          = 27.688 + 27.500 + 1.816
          = 57.00
```

### 5.6 Upside/Downside Modifier

**Fair value (blended, per fair-value-methodology.md Step 1 / Rule 7)** — full DCF scenario build in §7.1:

```
Bull-case blended FV  = $581.60   Base-case blended FV = $402.10   Bear-case blended FV = $294.60

PW Fair Value = 0.25×581.60 + 0.50×402.10 + 0.25×294.60 = 145.40 + 201.05 + 73.65 = $420.10

Gap Upside % = (420.10 / 510.86) − 1 = −17.77%    (a negative gap — priced above, not below, PW FV)
Catalyst window: no specific re-rating catalyst identified within 18–24 months this session
  (default 2yr window per Rule 10)
Annualized gap = −17.77% / 2 = −8.88%/yr

Intrinsic growth = 8.0%/yr   (normalized 4yr FCF CAGR, FY2021 $1,866M → FY2025 $2,575M = 8.37%,
                              rounded)
Shareholder yield = Dividend yield 0.77% (IBKR, §1) + Net buyback yield 2.5%
  (realized share-count decline, 180.0M Jan-2025 10-K cover → 174.7M Mar-2026 10-Q cover,
   −2.94% over 14 months ≈ −2.5%/yr annualized — the "net" figure, already reflecting any
   offsetting stock-comp issuance)

E = −8.88 + 8.0 + 0.77 + 2.5 = 2.39%/yr
```

`E` (2.39%) sits between 0% and the 10% hurdle `H`:
```
M = +5 × (H − E)/H = +5 × (10 − 2.39)/10 = +5 × 0.761 = +3.81
```

### 5.7 Final Valuation Score

```
Final Score = Raw Score + Rate Environment Gate modifier + Upside/Downside Modifier
            = 57.00 + 10.0 + 3.81
            = 70.81  →  rounded 70.8
```

**70.8 alone (Phase 03's raw-score table) would read "Expensive — do not buy, trim protocol if held."** It is the Composite blend with the Quality Score (§6) that changes the picture — shown transparently, not smoothed over.

---

## 6. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 80.2) + 0.50 × 70.8
                = 0.50 × 19.8 + 0.50 × 70.8
                = 9.90 + 35.40
                = 45.30
```

**Composite Score = 45.3 → "Cheap" band (30.0–49.9) per the Phase 03 table** — driven mainly by the high Quality Score pulling the blend down, even though the raw Valuation Score alone signals "Expensive." This is the documented, intended mechanic of the Composite Score (see the worked example in `valuation-scoring.md`, where a 22-point-cheaper-on-raw-score name loses to a much-higher-quality one once blended) — not a computation anomaly. It is flagged here precisely because the Quality Score input driving it is itself a 0.2-point photo finish (§3.8), so this Composite reading deserves real caution rather than mechanical execution — see §8.

---

## 7. Fair Value & Order Setup

### 7.1 DCF (3-scenario, per Rule 7)

Assumptions (modeling judgment calls, distinct from the sourced financial data above — flagged as such):

| | Bull | Base | Bear |
|---|---|---|---|
| WACC | 8.0% | 9.0% | 10.0% |
| Years 1–5 FCF growth | 9% | 8% | 7% |
| Years 6–10 fade | 9%→4% | 7%→3.5% | 6%→2% |
| Terminal growth | 3.5% | 3.0% | 2.5% |

Starting FCF: TTM $2,747M. WACC built from risk-free rate 4.10% + assumed beta 1.1 × assumed equity risk premium 5% ≈ 9.6% cost of equity, WACC set modestly below that given MCO's light leverage (base case 9.0%; ±1% for bull/bear per Rule 2's DCF standard).

```
DCF Enterprise Value → Equity Value (− Net Debt $6,070M, Q1 2026-end) → ÷ 174.7M shares:

Bull:  EV $88,222.7M  →  Equity $82,152.7M  →  $470.25/share
Base:  EV $62,857.0M  →  Equity $56,787.0M  →  $325.06/share
Bear:  EV $47,678.5M  →  Equity $41,608.5M  →  $238.17/share
```

### 7.2 Multiples-based value

```
Method A — Historical-PE cross-check (Rule 3): TTM EPS 13.95 × 5yr avg PE 37.79 = $527.20
Method B — Normalized EV/EBIT (20x, below the current elevated 27.8x, per Rule 4's sanity check)
  applied to an estimated next-12mo EBIT (~FY2025 EBIT × 1.08 ≈ $3,619M):
  EV $72,380M → Equity $66,310M → $379.60/share

Multiples-Based Value (Base) = ($527.20 + $379.60) / 2 = $453.40
```
Bull/Bear multiples values scaled proportionally to the DCF bull/bear ratios (1.4467× / 0.7327×): **Bull $655.90, Bear $332.20.**

### 7.3 Blended Fair Value (40% DCF / 60% Multiples, per Triangulation Formula)

```
Bull:  0.40×470.25 + 0.60×655.90 = $581.60
Base:  0.40×325.06 + 0.60×453.40 = $402.10
Bear:  0.40×238.17 + 0.60×332.20 = $294.60

PW Fair Value (0.25/0.50/0.25) = $420.10   (as used in §5.6)
```

**Sanity check (Rule 0 Step 4 / bull-case FV check):** independent analyst consensus 12-month price target is **~$536** (range ~$489–610, 20–27 analysts, per stockanalysis.com/MarketBeat-sourced aggregation) — above this session's own Bull-case blended FV ($581.60 is actually above it; Base is well below it). Notably, the sell-side's own average PT of $536 implies only **~5% upside** from the $510.86 live price on a 12-month view — even the more optimistic external view isn't pricing dramatic near-term upside. This corroborates (rather than contradicts) a "richly valued, thin expected return" read, even where this session's own bottom-up Base FV sits lower than consensus.

### 7.4 Order setup

Composite Score 45.3 falls in the 30.0–49.9 band → Margin of Safety 25–30% (midpoint 27.5% used), Max Acceptable Loss 25–30% (midpoint 27.5% used):

```
[X] Composite Score (incl. Upside/Downside Mod):  45.3   (≤49.9 — clears the entry-eligible range)
[X] Expected annual return E / catalyst window:   2.39% / 2yr (default, no specific catalyst identified)
[X] Upside/Downside Modifier applied:             +3.81
[X] DCF Fair Value (base):                        $325.06
[X] Multiples-Based Fair Value (base):             $453.40
[X] Blended Fair Value (PW, bull/base/bear):        $420.10
[X] Margin of Safety %:                            27.5%
[X] BUY PRICE (limit order):                       $304.57
[X] PRIMARY SELL TARGET (= PW Fair Value):          $420.10
[X] BULL-CASE TRIM TARGET (Bull FV × 0.90):         $523.44
[X] STOP LOSS (Buy Price × (1−27.5%)):              $220.82
[X] Risk/Reward Ratio (Primary Sell Target basis):  1.38 : 1   ❌ below the 2:1 minimum
[X] Risk/Reward Ratio (Bull-Case Trim Target basis):2.61 : 1   (clears 2:1, but is the optimistic case)
[ ] Position size — not computed; see §8, R/R gate fails before sizing is reached
```

**Risk/Reward fails the 2:1 minimum on the primary (baseline) sell target.** Per fair-value-methodology.md Step 6: *"If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely."* This is the deciding factor in §8's recommendation — not a discretionary override of the Composite Score's "Cheap" reading, but the framework's own next mechanical step after that reading.

---

## 8. Recommendation: **WATCHLIST ONLY — do not enter, do not place an order this session**

Three independent reasons converge, each sufficient on its own to counsel against entry despite the Composite Score's "Cheap / standard position" reading:

1. **The Quality Score gate is a 0.2-point photo finish** (80.2 vs. an equally legitimate 78.7 reading, §3.5/§3.8), and the entire Composite/Fair-Value/order-setup chain below it is downstream of that number. A basis choice this close shouldn't, by itself, greenlight a real position.
2. **Risk/Reward fails the framework's own 2:1 minimum** (1.38:1 on the primary sell target, §7.4) — fair-value-methodology.md's explicit instruction for this outcome is to wait or pass, not to place the naive MoS-derived limit order anyway.
3. **Q2 2026 earnings are due this week** (~2026-07-24, per last year's same-week filing pattern) — a Rule 9 mandatory-revaluation trigger that will update the Growth/Profitability inputs, and will show whether the Q1 2026 buyback pace (§2.2) continues or reverses, directly resolving the §3.5 balance-sheet sensitivity.

**No order placed, no position opened.** This reads as a name worth tracking, not one worth sizing into today — a considerably more qualified conclusion than the raw Composite Score number alone would suggest. Full re-run recommended immediately once Q2 2026 results are filed.

---

## 9. Next Review Trigger

- **MCO's Q2 2026 earnings**, expected ~2026-07-24 (not yet SEC-filed as of this session) — the actual event the triggering Telegram post referenced. A full re-score should follow immediately, given the §3.5/§3.8 sensitivity this earnings release will help resolve.
- Confirmation of whether the Q1 2026 buyback pace ($1.47B in one quarter) continued, paused, or reversed — directly resolves the Balance Sheet sub-score basis question.
- Standard Rule 9 triggers: guidance revision, management change, material M&A, macro/rate shift, or a >15% unexplained price move.

**No position opened — nothing to log in `decisions/`.**

---

## 10. Data Gaps Flagged

1. **None of the sub-scores were blocked by a missing metric** — MCO's clean GAAP EBIT/EBITDA/Cost-of-Revenue disclosure meant every Quality Score input was directly computable (a materially different situation from the JPM/C/SOFI/AXP financial-company sessions).
2. **The Quality Score's Balance Sheet sub-score is genuinely sensitive to which balance-sheet snapshot is used** (FY2025-end vs. Q1-2026-end), swinging the final Quality Score between 78.7 (FAIL) and 80.2 (PASS) — flagged prominently throughout (§3.5, §3.8, §8), not silently resolved.
3. **Interest coverage for the Upgrade 5 asset-light override wasn't independently derivable** this session — MCO's disclosed "Interest expense, net" bundles interest income and tax-related interest, not a clean gross interest-expense figure. Not needed for the pass/fail outcome (standard 2.5× threshold clears easily either way), but flagged as an unresolved input if the override were ever needed for a future, closer case.
4. **The earliest 5yr-PE-reconstruction data point (2021-06-30) uses a price ~3 weeks after the exact quarter-end** (IBKR's daily history begins 2021-07-22), a minor approximation not expected to materially move the 20-quarter average/range.
5. **DCF WACC/beta/growth-fade assumptions are modeling judgment calls**, explicitly flagged as such in §7.1 — distinct from the sourced financial data in §2–§6, and the single largest source of uncertainty in the Fair Value / Upside-Downside Modifier chain.

None of these gaps were silently patched around — each is the explicit reason this session's recommendation is "watchlist," not "buy," despite a Composite Score that on its face reads "Cheap."

---

## 11. Glossary

| Term | Meaning |
|---|---|
| **ARR (Annual Recurring Revenue)** | See [glossary.md](../framework/glossary.md). Here, MA's own supplemental metric for the estimated value of its recurring-revenue contracts at a point in time; MA's ARR grew 8% in FY2025 (§2.3). |
| **Big Three (credit rating agencies)** | Full entry in [glossary.md](../framework/glossary.md). Moody's, S&P Global, and Fitch's ~95% combined global market share — Moat Signal "market share" evidence (§2.4, §3.6). |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate between a start and end value. |
| **Composite Score** | This framework's 0.0–100.0 blend of Quality Score and Valuation Score (50/50), used against the Phase 03/05 action tables instead of the raw valuation score alone (§6). |
| **CRA (Credit Rating Agency)** | Full entry in [glossary.md](../framework/glossary.md). A firm issuing creditworthiness opinions on debt issuers/instruments; Moody's Investors Service is one of a handful of SEC-registered NRSRO CRAs. |
| **DCF** | Discounted Cash Flow — a valuation method projecting future cash flows and discounting them to present value (§7.1). |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / — before Interest, Taxes, Depreciation, and Amortization — operating-profit measures, cleanly disclosed by MCO (unlike several recent bank/financial sessions). |
| **EPS** | Earnings Per Share — net income divided by shares outstanding. |
| **EV / EV/EBIT** | Enterprise Value (market cap + debt − cash) and Enterprise Value ÷ EBIT — a whole-company price relative to operating profit (§5.2). |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10Y Treasury yield in the Rate Environment Gate's Step 1 (§4). |
| **Fast Grower** | Peter Lynch's term for EPS growth >15%/year for 3+ years — this framework's trigger for the PEG sub-score, deliberately *not* applied here (§5.4) since MCO's qualifying growth is a recovery off a cyclical trough, not clean structural growth. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check). MCO's FCF/NI ran 84–123% across FY2021–FY2025 (§2.1, §3.1). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted score. None fired for MCO (§3.1). |
| **Moat Signal** | This framework's 5-point qualitative checklist (market share, brand premium, network effect, switching costs, scale cost advantage) feeding 15% of the Quality Score. MCO scored 3 of 5 (§3.6). |
| **NRSRO (Nationally Recognized Statistical Rating Organization)** | Full entry in [glossary.md](../framework/glossary.md). The SEC-designated status underpinning MIS's regulatory-entrenchment Moat Signal evidence (§2.3, §3.6). |
| **Owner Earnings** | Warren Buffett's adjusted cash-flow measure — not applicable here (Upgrade 1 targets moat-building reinvestors like MSFT/GOOGL/META/AMZN, not MCO). |
| **PEG** | PE ÷ EPS growth rate — a Fast-Grower valuation sub-score, deliberately not applied to MCO this session (§5.4). |
| **PW (Probability-Weighted) Fair Value** | Full entry in [glossary.md](../framework/glossary.md). This session's 25%/50%/25% bull/base/bear blend, $420.10/share (§5.6, §7.3). |
| **Quality Score** | This framework's 0.0–100.0 continuous score; 80.0+ required to proceed to valuation scoring. MCO scored 80.2 on the primary basis used — a 0.2-point margin (§3.8). |
| **Rate Environment Gate / Rate Regime Modifier** | The mandatory pre-Phase-02 check comparing Earnings Yield to the 10Y Treasury and applying a regime-based additive modifier; contributed +10 to MCO's valuation score (§4). |
| **R/R (Risk/Reward Ratio)** | (Sell Target − Entry) ÷ (Entry − Stop Loss) — must clear 2:1 to enter; MCO's failed at 1.38:1 on the primary target (§7.4), the deciding factor in this session's recommendation. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ (Debt + Equity − Cash); MCO's FY2025 ROIC was 30.42%, clamped at the Quality Score formula's 100.0 ceiling (§3.2). |
| **Shareholder yield** | Dividend yield plus net buyback yield, a component of the Upside/Downside Modifier's expected-return calculation (§5.6). |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results — this session used Apr 2025–Mar 2026 (FY2025 minus Q1 2025 plus Q1 2026) for valuation-score inputs where more current than the full fiscal year (§5.2, §5.6). |
| **Upside/Downside (Expected-Return) Modifier** | The ±15-bounded additive modifier folding expected forward return into the valuation score; MCO's thin, near-zero expected return (E=2.39%, below the 10% hurdle) added a modest +3.81 (§5.6). |
| **WACC** | Weighted Average Cost of Capital — the DCF discount rate; assumed 8–10% across MCO's bull/base/bear scenarios (§7.1), a modeling judgment call distinct from sourced financial data. |

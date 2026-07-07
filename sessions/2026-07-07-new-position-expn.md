# NEW POSITION (Refresh) — Experian plc (LON:EXPN) — 2026-07-07

**Task type:** NEW POSITION (full re-evaluation of a stale not-in-portfolio entry)
**Date:** 07 Jul 2026
**10Y US Treasury Yield:** 4.48% (2026-07-06, Treasury.gov daily par yield curve — most recent published rate; see §5)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current EXPN portfolio weight:** 0% — not currently held (confirmed against [holdings.md](../portfolio/holdings.md))
**Sector:** Global consumer/commercial credit bureau & data analytics — one of the leading incumbents alongside Equifax and TransUnion
**Currency:** Experian trades in **GBX (pence)** on the LSE but **reports its financial statements in USD**. This session re-applies the same GBX/USD currency-consistency discipline the 2026-06-19 session established (see [that session](2026-06-19-new-position-expn.md) §0) — every ratio mixing price with a USD-denominated financial-statement line is converted to a single, consistent currency before the ratio is computed.
**Why this session exists:** the 2026-06-19 entry (score 32.0) was flagged stale on **two** counts — the 2026-06-20 Upside/Downside Modifier + PEG clean-earnings change, and the 2026-06-29 Quality Score/Composite Score addition (see [watchlist/STALE.md](../watchlist/STALE.md)). This is a full re-evaluation under the **current** methodology: fresh Phase 01 verification, a first-ever Quality Score, a full Phase 02 Valuation Score (including the Upside/Downside Modifier), and the Composite Score.

---

## 0. Data Gaps Flagged (up front, per operating-brief.md step 2)

1. **FY2026 diluted EPS / diluted share count** — not available from the Yahoo fundamentals feed (last diluted EPS on file: FY2025 $1.265). Net income YoY growth used as a same-period proxy for the Fast Grower test (§4) — does not change the conclusion (chain already broken by FY2025's −2.8%).
2. **Gross margin annual-statement re-derivation is noisy/unusable** — re-deriving gross margin from annual Gross Profit ÷ Total Revenue gives an implausibly swinging series (47.9%/55.6%/47.9%/55.5% across FY2023–26). `grossMargins` snapshot field (42.013%) retained as primary, consistent with the 2026-06-19 session's treatment of the same issue.
3. **5-year historical PE range is a same-session reconstruction, not a vendor-native series** — Experian reports semi-annually (no quarterly EPS series exists for the standard `yfinance`-style quarterly-TTM-PE reconstruction method in valuation-scoring.md). This session instead pairs each fiscal-year-end (31 Mar) closing price with that year's diluted EPS for FY2022–FY2025 (4 data points; FY2026 excluded, EPS gap per #1). Flagged as a coarser-than-usual basis — see §6.
4. **Company-specific FICO direct-license earnings impact is not separately quantified** — the "10–15% credit-bureau earnings pressure" figure found via WebSearch is an industry-wide analyst estimate (covering all three national bureaus collectively), not a EXPN-specific disclosed figure. Not built into the DCF as a discrete adjustment (would require inventing a number); instead treated as a qualitative bear-case/disruption-vector flag and as the basis for capping the Upside/Downside Modifier (§7).
5. **UK 10Y Gilt yield sourced via WebSearch (Trading Economics), not a UK DMO primary filing** — used for the DCF's cost-of-equity input; not as time-sensitive as live price, consistent with this repo's established precedent for macro inputs.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price (GBX, trading currency)** | **2,701.00p** (£27.01) | Yahoo Finance quote data (`regularMarketPrice`), fetched 2026-07-07 ~15:51 UTC (16:51 BST) — 15-min-delayed LSE feed, market state POSTPOST (session closed); previous close 2,653.00p, +48.00p / +1.81% on the day |
| **Live price (USD, financial-statement-consistent basis)** | **$36.1016** | = 2,701.00p ÷ 100 × GBPUSD 1.3366 — used for every ratio mixing price with a USD-denominated statement line |
| 52-week range | GBX 2,203.00 – 4,101.00 | Yahoo Finance `fiftyTwoWeekLow`/`fiftyTwoWeekHigh` |
| Analyst consensus PT (12-month) | Mean **3,872.39p**, 18 analysts, recommendation "Strong Buy" | Yahoo Finance `targetMeanPrice`/`recommendationKey` |
| Shares outstanding | **886,863,284** | Yahoo Finance `sharesOutstanding` |
| Market cap (GBP) | **£23,954.18M** | = 27.01 × 886,863,284 |
| Market cap (USD, FX-corrected) | **$32,017.15M** | = £23,954.18M × 1.3366 |
| Beta (5yr) | **0.831** | Yahoo Finance — near-market, not a volatility outlier |
| GBP/USD | **1.3366** | Yahoo Finance `GBPUSD=X`, live spot, 2026-07-07 |

**Data source note:** `yfinance`'s own crumb/cookie flow hit a rate limit (HTTP 429) via this session's proxy on first attempt. Per this session's task instructions and the "don't retry indefinitely" rule, this session instead queried Yahoo Finance's underlying quoteSummary/fundamentals-timeseries JSON endpoints directly (same data Yahoo/`yfinance` itself serves, same fields used throughout this repo's other sessions — `financialData`, `defaultKeyStatistics`, `summaryDetail`, `earningsTrend`, and the `fundamentals-timeseries` annual/quarterly series) via an authenticated session (cookie + crumb), cross-checked against stockanalysis.com (trailing PE 21.44 vs. this session's 21.78; forward PE 17.55 vs. this session's 17.88 — consistent to within normal cross-vendor snapshot-timing noise). Not a WebSearch/WebFetch fallback in the "estimated from prose" sense — this is the same primary quantitative feed, reached via a different transport.

---

## 2. Phase 01 — Fresh Data & Re-Verification (currency-consistent)

### FY2022–FY2026 financials (fiscal year ends 31 March), USD basis

| Metric | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| Total revenue | — | $6,619M | $7,097M | $7,523M | $8,445M |
| EBIT (GAAP/statutory) | — | $1,311M | $1,703M | $1,726M | $2,178M |
| EBITDA | — | $1,985M | $2,417M | $2,484M | $3,054M |
| Net income | — | $770M | $1,199M | $1,166M | $1,502M |
| Free cash flow | — | $1,090M | $1,107M | $1,354M | $1,513M |
| Net debt | — | $3,749M | $3,803M | $4,512M | $5,104M |
| Total debt | — | $4,099M | $4,266M | $5,016M | $5,565M |
| Stockholders' equity | — | $3,929M | $4,634M | $5,054M | $5,545M |
| Diluted EPS | $1.265 | $0.836 | $1.302 | $1.265 | n/a (gap, §0) |
| Interest expense | — | $137M | $152M | $177M | $227M |
| Tax rate (effective, calc basis) | — | 34.2% | 22.44% | 24.47% | 22.7% |

Source: Yahoo Finance `fundamentals-timeseries` (`annualTotalRevenue`, `annualEBIT`, `annualEBITDA`, `annualNetIncome`, `annualFreeCashFlow`, `annualNetDebt`, `annualTotalDebt`, `annualStockholdersEquity`, `annualDilutedEPS`, `annualInterestExpense`, `annualTaxRateForCalcs`). **Every figure in this table matches the 2026-06-19 session's independently-sourced table exactly** — a useful internal consistency check that the FY2026 figures haven't been revised since.

Company's own FY26 results announcement ([experianplc.com](https://www.experianplc.com/newsroom/press-releases/2026/full-year-results-fy26), verified via WebFetch): total revenue growth 13% actual / 11% constant-currency; organic revenue growth 8% full year (9% in Q4); **Benchmark EBIT** (Experian's own non-GAAP basis) $2,407M, margin 28.6%; **company-disclosed ROCE 17.2%**; Benchmark EPS growth 15% actual / 13% constant-currency; dividend +11% to USc 69.25/share; $725M buybacks executed in FY26, new $1bn program (through 30 Jun 2027); $792M in acquisitions; Consumer Services 9% organic growth (215M+ free members); B2B 8% organic growth. **Note:** the $2,407M "Benchmark EBIT" figure is Experian's own non-GAAP measure (excludes acquisition amortization and exceptional items) and is *not* the $2,178M GAAP/statutory EBIT figure used in this session's EV/EBIT and DCF work (consistent with the 2026-06-19 session's basis, and with `financialData.operatingMargins` × revenue: 25.029% × $8,445M ≈ $2,114M, in the same statutory ballpark as $2,178M, not the Benchmark figure) — see the **Benchmark EBIT / Benchmark EPS** glossary entry. This likely also explains most of the gap between the company's own 17.2% ROCE and this session's 15.61% NOPAT/Invested-Capital ROIC (§3) — a Benchmark-EBIT-based NOPAT would be larger.

### Revenue 3yr CAGR — re-verified

```
3yr CAGR = (8,445 / 6,619)^(1/3) − 1 = 8.466%   (FY2023 $6,619M → FY2026 $8,445M)
```
Matches the 2026-06-19 session (8.46%) — unaffected by the interim methodology changes (ratio math, not currency-dependent).

### Net margin — re-verified

```
Net margin FY2026 = 1,502 / 8,445 = 17.785%
```

### FCF/Net Income conversion ratio — re-verified, still comfortably above 70%

| FY | FCF | NI | Conversion |
|---|---|---|---|
| 2023 | $1,090M | $770M | 141.6% |
| 2024 | $1,107M | $1,199M | 92.3% |
| 2025 | $1,354M | $1,166M | 116.1% |
| 2026 | $1,513M | $1,502M | 100.7% |

✅ Comfortably clears >70% every year, including the required "2+ consecutive years." No hard disqualifier here.

### Net debt/EBITDA — re-verified

```
Net Debt/EBITDA (FY2026) = $5,104M / $3,054M = 1.6712×   (<2.5× required — comfortably passes)
```

### Fast Grower (Upgrade 3 — PEG) determination — re-verified, same conclusion

| Period | Diluted EPS | YoY EPS growth | NI YoY growth (proxy) | >15%? |
|---|---|---|---|---|
| FY2024 | $1.302 | +55.7% | +55.7% | ✅ Yes |
| FY2025 | $1.265 | **−2.8%** | −2.8% | ❌ No |
| FY2026 | n/a (gap) | n/a | +28.8% | ✅ Yes (NI basis) |

The FY2025 dip still breaks the "3 consecutive years >15%" chain. **Not a Fast Grower.** PEG's 15% weight redistributes to EV/EBIT (→ 40% total), unchanged from 2026-06-19.

### Phase 01 gate table (legacy binary criteria, for continuity with the 06-19 session)

| Check | Value | Threshold | Result |
|---|---|---|---|
| Gross margin | 42.013% | >40% | ✅ PASS |
| Net margin | 17.785% | >12% | ✅ PASS |
| ROE | 28.258% (Yahoo `returnOnEquity`, TTM basis) | >15% | ✅ PASS |
| Revenue CAGR 3yr | 8.466% | >8% | ✅ PASS |
| FCF positive 3+ consecutive years | Yes (FY24 $1.107B, FY25 $1.354B, FY26 $1.513B) | required | ✅ PASS |
| FCF/NI conversion ratio | FY26 100.7%, FY25 116.1% | >70% | ✅ PASS |
| Net Debt/EBITDA | 1.6712× | <2.5× | ✅ PASS |
| EV/EBIT | 17.044× (§6) | <20× | ✅ PASS |
| Share issuance pattern | Net buyback ($725M executed FY26, new $1bn program) | non-dilutive required | ✅ PASS |

**Gate result: PASS — 8/8 legacy binary criteria still pass.** EV/EBIT has drifted further from the screening-era mixed-currency read (13.00×) toward the ceiling (now 17.044×, up from 16.13× on 06-19, purely a price-appreciation effect — see §6) but still clears 20×. **Under the current methodology this legacy pass/fail table is superseded by the graded Quality Score gate below — passing here is necessary but not sufficient.**

---

## 3. Phase 01 (Current Methodology) — Quality Score

Per [quality-scoring.md](../framework/quality-scoring.md), a company needs **80.0+** on the graded Quality Score to proceed to Phase 02 at all. This is EXPN's **first-ever** Quality Score (the metric didn't exist on 2026-06-19).

**Hard disqualifier check (all must pass regardless of weighted score):** FCF/NI ≥70% for 2+ years ✅ (100.7%/116.1%) · Net Debt/EBITDA under 2.5× ✅ (1.6712×) · FCF-positive 3+ years ✅. **No hard disqualifier fires.**

### Profitability (25% weight)

```
Net Margin (FY2026)   = 17.785%
NetMargin_Component    = clamp((17.785/30)×100, 0, 100) = 59.28

ROIC (framework convention — NOPAT ÷ Invested Capital, Invested Capital = Total Debt + Equity − Cash):
  NOPAT = EBIT × (1 − tax rate) = $2,178M × (1 − 0.227) = $1,683.6M
  Invested Capital = Total Debt $5,565M + Equity $5,545M − Cash $328M = $10,782M
  ROIC = $1,683.6M / $10,782M = 15.615%
ROIC_Component = clamp((15.615/30)×100, 0, 100) = 52.05

Sensitivity / cross-check: Experian's own FY2026 disclosed ROCE = 17.2% (likely computed on the
Benchmark, not statutory, EBIT basis — see §2) → ROIC_Component (alt) = clamp((17.2/30)×100) = 57.33.
Primary reading below uses the framework's own NOPAT/Invested-Capital convention (15.615%), per this
repo's established practice (see the DOCS 2026-07-07 session) of using the framework's own formula as
primary and a company-disclosed figure as a cross-check, not a substitute.

Profitability_Score = (59.28 + 52.05) / 2 = 55.665   (no FCF cap — FCF-positive every year on file)
```
→ Contribution: 55.665 × 0.25 = **13.916**

*(Sensitivity: using the company's own 17.2% ROCE instead → Profitability_Score = 58.31, contribution 14.58 — a +0.66 swing, immaterial to the gate conclusion; see §3 sensitivity check below.)*

### Margins (15% weight)

```
Gross Margin = 42.013%   (Yahoo snapshot field, retained primary — see §0 data-gap note)
GrossMargin_Score = clamp((42.013/80)×100, 0, 100) = 52.52
```
No structural-trend bonus applies (only available when gross margin is *below* 40% but trending up — 42.013% is already above the threshold).
→ Contribution: 52.52 × 0.15 = **7.878**

### Growth (20% weight)

```
Revenue 3yr CAGR = 8.466%
Growth_Score (raw) = clamp((8.466/25)×100, 0, 100) = 33.86
```
**TAM-expansion/pricing-power modifier (+10):** documented evidence — FY26 Consumer Services 9% organic growth on a 215M+ free-member base; B2B 8% organic growth; FY27 guidance reaffirmed at 6–8% organic / 8–11% total (same range as FY26's initial guidance, not a downgrade); continued emerging-market penetration (Latin America +8% organic in FY26). Source: Experian FY26 results announcement (§2). No structural-deceleration evidence found (organic growth *accelerated* into Q4 FY26 at 9%, and FY27 guidance is unchanged/reaffirmed, not cut) — so the −10 "decelerating" modifier does **not** apply, despite the FICO disruption-vector risk discussed in §8 (that risk is a documented *margin/earnings* threat in one specific US-mortgage-reselling niche, not a documented *revenue-growth-deceleration* signal at the consolidated-company level; kept separate rather than folded into this sub-score, consistent with "never invent" — there is no company-level revenue-growth-deceleration citation to point to).

```
Growth_Score = 33.86 + 10 = 43.86
```
→ Contribution: 43.86 × 0.20 = **8.772**

### Balance Sheet (15% weight)

```
Net Debt/EBITDA = 1.6712×   (standard threshold applies — EXPN is not a payment network/exchange asset-light business, Upgrade 5 override not applicable)
BalanceSheet_Score = clamp(100 × (1 − 1.6712/4), 0, 100) = 58.22
```
→ Contribution: 58.22 × 0.15 = **8.733**

### Moat Signal (15% weight) — checklist, cited evidence only

| Signal | Result | Evidence |
|---|---|---|
| Market share stable/growing | ✅ TRUE | Experian Information Solutions cited as holding ~46.7% of the (US) credit-agency market, part of a five-player oligopoly (Equifax, Experian, TransUnion, Dun & Bradstreet, LexisNexis) with entrenched, decades-stable positioning. Third-party market-research aggregation via WebSearch (americanbanker.com/mordorintelligence-sourced summary), not a company filing — flagged as secondary-source, consistent with this framework's treatment of comparable third-party share citations elsewhere (e.g. Dell'Oro for CIEN). |
| Brand premium / pricing power | ✅ TRUE | B2B customer retention >80% even against competitor price discounts; Experian able to raise B2B prices ~2–3% annually without material churn (daveahern.substack.com credit-bureau-economics analysis, WebSearch-sourced). **Flagged as a single-source, non-institutional citation** — weaker sourcing tier than a market-research firm; retained because it is a specific, falsifiable, cited claim (not invented), but noted transparently as a data-quality caveat. |
| Network effect | ✅ TRUE | Documented two-sided data-network mechanism: businesses (lenders) both consume Experian's credit-file data *and* furnish their own loan-performance data back into it, compounding the depth/value of the dataset with each new furnisher and user (same source as above). Structurally the same "furnisher network" mechanism as the other two national bureaus, a standard, well-documented feature of the credit-bureau business model. |
| Switching costs | ✅ TRUE | Same source: banks that integrate Experian's risk/scoring models into live underwriting workflows face real IT integration, re-validation, and retraining costs to switch, plus operational risk if a switch degrades decisioning quality — consistent with the >80% B2B retention figure above. |
| Scale cost advantage | ❌ **NOT credited** | Found citations describing Experian's *data scale* (1.1B+ consumer and 250M+ business records globally) but **no cost-per-unit figure showing a processing-cost gap vs. smaller competitors**, which is what this framework's Moat Signal checklist specifically requires for this signal (per [quality-scoring.md](../framework/quality-scoring.md): "Cost-per-unit data showing a gap vs. smaller competitors"). Declined to credit, consistent with this repo's conservative precedent on this exact signal (e.g. NVDA's CoWoS/PUE citations similarly declined in the 2026-07-05 session for lacking cost-per-unit specificity). |

```
Moat_Score = (4/5) × 100 = 80.0
```
→ Contribution: 80.0 × 0.15 = **12.00**

### FCF Quality (10% weight)

```
FCF/NI (FY2026) = 1,513 / 1,502 = 100.73%
FCFQuality_Score = clamp(((1.0073 − 0.40)/0.60)×100, 0, 100) = clamp(101.2, 0, 100) = 100.0
```
→ Contribution: 100.0 × 0.10 = **10.00**

### Quality Score — final

```
Quality Score = (55.665×0.25) + (52.52×0.15) + (43.86×0.20) + (58.22×0.15) + (80.0×0.15) + (100.0×0.10)
              = 13.916 + 7.878 + 8.772 + 8.733 + 12.00 + 10.00
              = 61.299
```

Boundary rule (round to nearest 0.1, ".X5" rounds up): **Quality Score = 61.3**

# **61.3 < 80.0 — fails the gate, decisively** (18.7 points short of the 80.0 threshold).

**Sensitivity check (robustness of the gate verdict):** even stacking every debatable judgment call in Experian's favor simultaneously — the company's own 17.2% ROCE instead of the framework's 15.615% NOPAT/IC ROIC (Profitability_Score → 58.31, +0.66 to the weighted score), *and* crediting the 5th Moat signal despite the missing cost-per-unit citation (Moat_Score → 100.0, +3.00 to the weighted score) — the Quality Score reaches only **≈65.0**, still more than 15 points short of 80.0. **The gate result is not sensitive to any of this session's individual judgment calls.**

No hard disqualifier independently fires either — this is a pure weighted-score gate failure, driven mainly by Growth (43.86, well below the ~70+ a "clear pass" name typically shows) and the moderate Balance-Sheet/Margins/Profitability scores (all in the high-50s), none individually alarming but none exceptional either — consistent with a solid, real, profitable oligopoly business that simply doesn't clear this framework's deliberately strict 80.0+ bar, not a distressed or broken one.

---

## 4. What the Quality Gate Failure Means for the Rest of This Session

Per [quality-scoring.md](../framework/quality-scoring.md): *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all. Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."* Under a strict reading, this session would stop here (as the 2026-07-06/07 CVX, HNHPF, and DOCS sessions did for decisive gate failures).

**This session's specific task instructions direct otherwise for this ticker:** compute the full Rate Environment Gate, Phase 02 Valuation Score, and Composite Score anyway, **as a reference-only exercise**, explicitly to illustrate why a superficially attractive Composite Score would be a **false green light** here — i.e., a reader skimming only the bottom-line Composite number could be misled into thinking this is a "Cheap, buy" situation, when the Quality Score gate says the opposite. Everything from here through §9 is therefore **reference/illustrative, not adopted** — the binding recommendation is set by §3's gate failure, confirmed independently by §9's R/R-gate failure.

---

## 5. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**

Forward PE, recomputed on a currency-consistent, 0y (next-fiscal-year, FY2027E) basis — replicating the exact correction the 2026-06-19 session applied (Yahoo's raw `forwardPE`/`defaultKeyStatistics` fields mix currency/period bases and are not used directly):

```
Live price (USD)        = $36.1016
Forward EPS (0y basis, FY2027E, USD, 17 analysts) = $2.01878   (Yahoo earningsTrend — identical
                                                                   to the figure the 06-19 session
                                                                   used, confirming this consensus
                                                                   estimate hasn't moved)
Forward PE = $36.1016 / $2.01878 = 17.883×

EY     = 1 ÷ 17.883 = 5.592%
Spread = EY − 10Y Treasury = 5.592% − 4.48% = +1.112%
```

**Result: FAIL** (below the +1.5% threshold) → **+5 additive** (Step 1).

**This flips from the 06-19 session's result** — that session found a narrow +0.05pp *pass* (spread +1.550% vs. threshold +1.5%, with Forward PE 16.67× and 10Y 4.45%). Re-verifying carefully as this session's task instructions flagged: the flip is driven by Forward PE rising from 16.67× to 17.883× (price up ~6.3% GBX-terms, EPS estimate unchanged) combined with the 10Y Treasury edging up slightly (4.45%→4.48%) — both moves push the spread the same direction. **Sensitivity check:** even using the alternative 10Y figure found during this session's WebSearch cross-check (4.47%, vs. the 4.48% Treasury.gov primary figure used above), the spread is 5.592%−4.47%=+1.122%, still <1.5% — the FAIL result is not sensitive to which of the two very-close 10Y readings is used.

**Step 2 — Rate Regime Modifier**
10Y = 4.48% → "3.5–5%" bracket → **+5**

**Total Rate Modifier = +5 (Step 1) + 5 (Step 2) = +10**

---

## 6. Phase 02 (Reference Only) — Full Valuation Score Calculation

**FCF Yield — 40% weight**

```
FCF Yield = FCF(FY2026, USD) / Market Cap (USD) = $1,513M / $32,017.15M = 4.7256%
FCF_Score = clamp(100 × (1 − 4.7256/10), 0, 100) = 52.744
```
→ Contribution: 52.744 × 0.40 = **21.098**

**EV/EBIT — 40% weight (PEG not applicable, redistributed from 25%)**

```
EV (USD) = Market Cap (USD) $32,017.15M + Net Debt (FY2026, USD) $5,104M = $37,121.15M
EV/EBIT  = $37,121.15M / $2,178M (FY2026 EBIT) = 17.044×
EV/EBIT_Score = clamp((17.044 − 12) / 23 × 100, 0, 100) = 21.929
```
→ Contribution: 21.929 × 0.40 = **8.772**

**Forward PE (PRIMARY formula — a genuine 5yr low/high range is reconstructable) — 20% weight**

Experian reports semi-annually — no quarterly EPS series exists for the standard `yfinance` quarterly-TTM-reconstruction method (§0 data gap). This session instead pairs each fiscal-year-end (31 Mar) closing price with that fiscal year's diluted EPS:

| Fiscal year end | Price (GBX) | GBPUSD (same date) | Price (USD) | Diluted EPS (USD) | Trailing PE |
|---|---|---|---|---|---|
| 2022-03-31 | 2,951.00p | 1.3147 | $38.797 | $1.265 | 30.669× |
| 2023-03-31 | 2,660.00p | 1.2387 | $32.950 | $0.836 | 39.414× |
| 2024-04-02* | 3,393.00p | 1.2637 | $42.878 | $1.302 | 32.933× |
| 2025-03-31 | 3,568.00p | 1.2921 | $46.102 | $1.265 | 36.444× |
| 2026-03-31 | 2,598.00p | 1.3243 | $34.406 | n/a (gap) | n/a |

*First trading day on/after the fiscal year end (31 Mar 2024 was a non-trading day).

```
5yr Low PE  = 30.669×  (FY2022)
5yr High PE = 39.414×  (FY2023)
5yr Avg PE  = (30.669+39.414+32.933+36.444)/4 = 34.865×

Forward PE = 17.883×  (§5)

FwdPE_Score (raw) = clamp((17.883 − 30.669) / (39.414 − 30.669) × 100, 0, 100) = clamp(−146.3, 0, 100) = 0.0
```
Forward PE sits far below even the 5-year low — the cheapest possible reading on this axis.

**Historical PE Modifier (Upgrade 2)**
```
Deviation from 5yr avg = (17.883 − 34.865) / 34.865 = −48.71%
```
>20% below average → modifier = **−10** (no further effect; already at the 0.0 floor).
```
FwdPE_Score (adjusted) = clamp(0.0 − 10, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.000**

**Robustness check against alternate PE-range sources:** WebSearch-sourced third-party figures for EXPN's PE history vary considerably by methodology (GuruFocus 10yr quarterly-TTM range 19.54×–57.47×, mean 30.39×; wisesheets.io annual-basis 5yr figures 2021–2025 averaging ~31.90–35.55×). Every one of these alternate ranges, if substituted, still leaves Forward PE (17.883×) below the low end — **FwdPE_Score stays clamped at 0.0 regardless of which historical-PE source is used.** This robustness is what makes the coarser 4-point annual reconstruction (§0 gap #3) an acceptable basis here — the conclusion doesn't turn on the exact range chosen.

**PEG — not applicable** (redistributed to EV/EBIT, §2)

### Raw weighted score

```
Raw weighted score = (52.744×0.40) + (21.929×0.40) + (0.0×0.20)
                    = 21.098 + 8.772 + 0.000
                    = 29.869 (technically 29.8693, see full precision above)

+ Rate Regime Modifier (+10, §5) = 39.869
```

---

## 7. Upside/Downside Modifier — full calc shown

**Step 1 — Fair Value (bull/base/bear), via DCF + Multiples (Rule 1)**

*WACC:*
```
Cost of Equity = UK 10Y Gilt (4.86%, 2026-07-07, Trading Economics — see §0 gap #5) + Beta (0.831) × ERP (5.0%)
               = 4.86% + 4.155% = 9.015%
Cost of Debt (pre-tax) = Interest Expense $227M / Total Debt $5,565M = 4.079%
Cost of Debt (after-tax) = 4.079% × (1 − 22.7% tax rate) = 3.153%
Capital structure (market-value weights): Equity $32,017.15M / (Equity + Debt $5,565M) = 85.19% equity, 14.81% debt
WACC = 0.8519×9.015% + 0.1481×3.153% = 7.682% + 0.467% = 8.149% ≈ 8.15%
```

*3-stage DCF (Yrs 1–5 explicit, Yrs 6–10 fade to 2.5% terminal, WACC ±1% and growth ±2pp across scenarios, per Rule 2/7), base FCF $1,513M (FY2026):*

| Scenario | WACC | Yrs 1–5 growth | PV(FCF Yrs 1–10) | PV(Terminal Value) | EV | TV weight |
|---|---|---|---|---|---|---|
| Bear | 9.15% | +5% | $12,127.7M | $14,737.3M | **$26,865.0M** | 54.9% |
| Base | 8.15% | +7% | $13,882.9M | $21,716.0M | **$35,598.8M** | 61.0% |
| Bull | 7.15% | +9% | $15,942.2M | $32,991.6M | **$48,933.9M** | 67.4% |

All three pass the <75% terminal-value-weight sanity check (Rule 4). Growth assumptions anchored to Experian's own FY27 guidance (organic 6–8%, total 8–11%, reaffirmed — §3).

```
PW DCF EV = 0.25×48,933.9 + 0.50×35,598.8 + 0.25×26,865.0 = $36,749.1M
DCF Equity Value = $36,749.1M − Net Debt $5,104M = $31,645.1M
DCF FV/share (USD, PW) = $31,645.1M / 886,863,284 shares = $35.6821
```

*Comparable Multiples (Rule 5) — peer set: Equifax (EFX), TransUnion (TRU), Verisk Analytics (VRSK), Moody's (MCO), S&P Global (SPGI), RELX (REL.L). Dun & Bradstreet still excluded (taken private Aug 2025). All Forward PE figures recomputed on the same 0y-basis correction as EXPN and RELX (both GBP/GBX-consistency-corrected):*

| Company | Forward PE (0y basis) | EV/EBIT | Revenue ($B, latest FY/TTM) | In Rule 5 ±50% band of EXPN's $8.445B? |
|---|---|---|---|---|
| Equifax (EFX) | 20.588× | 23.25× | $6.28B | ✅ |
| TransUnion (TRU) | 16.601× | 23.21× | $4.73B | ✅ |
| Verisk Analytics (VRSK) | 25.147× | 21.39× | $3.10B | ❌ below band ($4.22B floor) |
| Moody's (MCO) | 30.135× | 27.31× | $7.87B | ✅ |
| S&P Global (SPGI) | 23.494× | 22.95× | $15.73B | ❌ above band ($12.67B ceiling) |
| RELX (REL.L) | 17.440× | 16.77× | $9.59B | ✅ |
| **Median (all 6, per 06-19 precedent)** | **22.041×** | **23.08×** | | |

Same two Rule 5 band-breach flags as the 2026-06-19 session (VRSK below floor, SPGI above ceiling) — shown transparently, not trimmed, per this repo's precedent.

```
EV/EBIT reversion: 23.08× × EXPN EBIT $2,178M = implied EV $50,268.2M − Net Debt $5,104M
                  = Equity $45,164.2M ÷ 886,863,284 shares = $50.9258/share (USD)

Forward PE reversion: 22.041× × EXPN's own Forward EPS (0y, $2.01878) = $44.4959/share (USD)

Multiples avg = ($50.9258 + $44.4959) / 2 = $47.7109/share (USD)
```

```
Blended FV (USD) = 0.40 × $35.6821 (PW DCF) + 0.60 × $47.7109 (Multiples avg)
                  = $14.2728 + $28.6265
                  = $42.8994/share

Convert to GBX: $42.8994 / 1.3366 × 100 = 3,209.59p
```

This is also, by construction, the **PW Fair Value** for the modifier below (the DCF leg is already probability-weighted per Rule 7 before blending with the — scenario-invariant — Multiples leg; linear algebra confirms the scenario-by-scenario blended-FV approach gives the identical $42.8994 figure, cross-checked).

**Sanity check (Rule 4):** Blended FV (3,209.59p) sits well below the analyst consensus mean (3,872.39p, −17.1%) but above the 06-19 session's own Blended FV (3,052.50p, +5.1%) — a reasonable, price/EPS-consistent drift given both live price and consensus estimates moved modestly since. Not an outlier read.

**Step 2 — Expected annual return `E`**

```
Gap Upside % = (Blended FV $42.8994 / Live Price $36.1016) − 1 = +18.830%
```

**Catalyst window — guardrail assessment.** No single, dated, resolution-specific catalyst was identified for this gap within 18–24 months. Considered and rejected as insufficiently specific: the 16 Jul 2026 Q1 FY27 trading update (routine, not a re-rating resolution event); H1 FY27 results (~Nov 2026, routine); a macro rate-cut-driven lending-volume recovery (plausible but no dated basis). **Materially, this session surfaced a documented, currently-*unresolved* structural risk (FICO's Mortgage Direct License Program, effective Oct 2025, projected by industry analysts to pressure credit-bureau earnings by ~10–15% industry-wide — §8) that argues the multiple compression may be at least partly a legitimate, ongoing repricing of risk rather than pure temporary mispricing.** Per the Guardrail ("no catalyst within 18–24 months → cap upside side at −5"), this session applies the cap:

```
Catalyst window = 2yr (default, no narrower dated catalyst)
Annualized gap = 18.830% / 2 = 9.415%

Intrinsic growth (FCF 3yr CAGR, FY2023→FY2026) = (1,513/1,090)^(1/3) − 1 = 11.550%
Shareholder yield = Dividend yield (1.95%, Yahoo summaryDetail) + Net buyback yield
                     ($725M FY26 buybacks / $32,017.15M market cap = 2.264%)
                   = 4.214%

E = 9.415% + 11.550% + 4.214% = 25.180%
```

**Step 3 — Map to modifier**

```
Uncapped: E (25.18%) ≥ H (10%) → M = −15 × clamp((25.18−10)/15, 0, 1) = −15 × clamp(1.012, 0, 1) = −15.0
Capped (Guardrail 1, no dated catalyst within 18–24mo): M = −5.0
```

**Upside/Downside Modifier applied = −5.0 (capped; −15.0 uncapped alternative shown for transparency)**

---

## 8. Qualitative Case (5 Questions + Disruption Vector) — reaffirmed and updated

1. **Why are margins high?** Regulatory-accreditation + data-scale moat in an oligopoly bureau structure — not a lucky cycle.
2. **What would it take to compete?** Decades of proprietary credit-file depth, lender-furnisher relationships, and FCRA-equivalent regulatory accreditation — practically impossible for a new entrant to replicate from scratch (§3 Moat evidence).
3. **Capital allocation (5–10yr):** Consistent bolt-on M&A ($792M in FY26 alone), steady dividend growth (+11% FY26) plus buybacks ($725M executed, new $1bn program), organic reinvestment in cloud data platforms and consumer/fraud/ID products.
4. **Where is growth coming from next 3–5yr?** Consumer Services (215M+ free members, 9% organic growth), B2B decisioning/fraud/identity analytics (8% organic), continued under-bureaued emerging-market penetration (Latin America +8% organic FY26).
5. **Best bear case?** Two converge here: (a) **cyclicality** — meaningful revenue exposure to consumer-lending origination volumes (mortgage, auto), sensitive to the credit/rate cycle; UK&I organic growth was just 2% in FY26 vs. 10% in North America, evidence this isn't uniform; (b) **FICO's Mortgage Direct License Program** (effective 1 Oct 2025) — a **new, material, and NOT present in the 06-19 session's analysis** structural threat: FICO now licenses its mortgage credit score directly to lenders/tri-merge resellers, bypassing the historical bureau-resale channel. Projected by industry analysts (WebSearch-sourced, not company-confirmed) to pressure the three national bureaus' collective earnings by ~10–15%; FICO's own launch-day stock move (+32%) vs. the three bureaus' (−5% to −12%) is a real, market-priced signal this risk is taken seriously. Also newly found: EXPN is wind­ing down two large (unnamed) breach-notification contracts, a real near-term revenue headwind flagged by sell-side commentary.

**Disruption vector check (Q6):** Moderate-to-elevated, and **actively in progress**, not merely monitored — a meaningful change from the 06-19 session's "moderate, monitored" characterization. This is the single most important qualitative update this session makes to the EXPN thesis. It does not change the Quality Score (§3, no company-level revenue-deceleration evidence yet) but it is the primary reason this session applies the Upside/Downside Modifier's guardrail cap (§7) rather than crediting the full uncapped upside.

**Governance note (not a Rule 9 trigger, but monitored):** Board Chair Mike Rogers is stepping down effective 22 Jul 2026. This is a non-executive board-level transition, not a CEO/CFO operational management change — distinguished from the Rule 9 "management change" trigger, which this session interprets as executive leadership. Flagged for monitoring, not treated as invalidating this session's fundamentals.

---

## 9. Final Valuation Score & Composite Score (Reference Only)

```
Final Valuation Score = Raw weighted (29.869) + Rate Modifier (+10) + Upside/Downside Modifier (−5.0, capped)
                       = 34.869 → rounds to 34.9

Uncapped alternative = 29.869 + 10 − 15.0 = 24.869 → rounds to 24.9
```

**Final Valuation Score = 34.9** (30.0–49.9 band = "Cheap") — capped-modifier reading. Uncapped alternative (24.9) would sit in the 0.0–29.9 "Very Cheap" band.

### Composite Score (Quality + Valuation, 50/50) — reference only, per §4

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 61.3) + 0.50 × 34.9
                = 0.50 × 38.7 + 17.45
                = 19.35 + 17.45
                = 36.8   (capped-modifier valuation input)

Uncapped alternative = 0.50×38.7 + 0.50×24.9 = 19.35 + 12.45 = 31.8
```

# **Composite Score = 36.8 (reference only — NOT adopted). This is a false green light.**

Read in isolation, 36.8 sits squarely in the Phase 03 "Cheap — Standard position 3–5%" band, and would look like a straightforward buy signal. **It is not one.** Per [quality-scoring.md](../framework/quality-scoring.md), the Composite Score is not computed for, and does not rescue, a company that fails the 80.0+ Quality Score gate — and EXPN's Quality Score (61.3) fails that gate decisively, by 18.7 points, with a sensitivity-check ceiling of ~65.0 even under every generous judgment call stacked in its favor (§3). **The cheapness of this stock is real (it trades meaningfully below its own reconstructed 5-year PE range and below this session's DCF+Multiples fair-value estimate), but cheapness alone has never been what this framework buys — quality is the gate, and Experian doesn't clear it under the current, deliberately strict 80.0+ bar.** This is exactly the scenario the Quality Score/Composite Score addition (2026-06-29) was designed to catch: a name that looks statistically attractive on valuation alone but is a lower-conviction business than the framework's highest-conviction holdings.

---

## 10. Risk/Reward Gate (independent second reason not to enter)

Even setting the Quality gate aside entirely and treating the reference Valuation Score (34.9, Cheap band) as if it were binding, the R/R gate is checked exactly as it would be for a real BUY candidate — and **still fails**, exactly as it did on 2026-06-19.

Score 34.9 falls in 30.0–49.9 (Cheap) → MoS 25–30% required.

```
Buy Price ceiling (25% MoS) = 3,209.59p × 0.75 = 2,407.19p
Buy Price ceiling (27.5% MoS) = 3,209.59p × 0.725 = 2,326.95p
Buy Price ceiling (30% MoS) = 3,209.59p × 0.70 = 2,246.71p
```

**Current price (2,701.00p) sits ABOVE every point in the 25–30% MoS buy-ceiling band** — implied MoS at current price = 1 − (2,701.00/3,209.59) = **15.85%**, well short of even the loosest 25% requirement.

**Full 3×3 MoS × stop-loss R/R sensitivity grid:**

| Buy Price (MoS) | Stop Loss (max loss %) | Stop price | R/R |
|---|---|---|---|
| 2,407.19p (25%) | 25% | 1,805.39p | 1.33:1 |
| 2,407.19p (25%) | 27.5% | 1,745.21p | 1.21:1 |
| 2,407.19p (25%) | 30% | 1,685.03p | 1.11:1 |
| 2,326.95p (27.5%) | 25% | 1,745.21p | 1.52:1 |
| 2,326.95p (27.5%) | 27.5% | 1,687.04p | 1.38:1 |
| 2,326.95p (27.5%) | 30% | 1,628.87p | 1.26:1 |
| **2,246.71p (30%, best case)** | **25% (tightest, best case)** | **1,685.03p** | **1.71:1** |
| 2,246.71p (30%) | 27.5% | 1,628.87p | 1.56:1 |
| 2,246.71p (30%) | 30% | 1,572.70p | 1.43:1 |

**All 9 combinations fail the 2:1 minimum.** Best case across the entire grid — 30% MoS combined with the tightest 25% stop — reaches only **1.71:1**, essentially unchanged from the 06-19 session's identical 1.71:1 (both price and fair value moved up by similar proportions, preserving the ratio structure).

**Could a justified stop-tightening close the gap?** Beta remains near-market (0.831, vs. 0.824 on 06-19) — no volatility-based justification for a non-standard tighter stop (contrast the SGE precedent's outlier-low 0.293 beta). Solving for the stop that would clear 2:1 at the most favorable entry (2,246.71p, 30% MoS) requires a ~21.4% max-loss band — tighter than the entire standard 25–30% band, with no evidentiary basis to go there. **Same conclusion as 06-19: no combination clears 2:1, and no defensible adjustment closes the gap.**

**Reference-only order-setup checklist (not actioned — both the Quality gate and the R/R gate independently fail):**

```
[x] Quality Score:                            61.3 / 100.0 — FAILS the 80.0+ gate (binding reason not to enter)
[x] Composite Score (reference only):         36.8 (capped) / 31.8 (uncapped) — a false green light, not adopted
[x] Valuation Score (incl. Upside/Downside Mod, reference): 34.9 (capped) / 24.9 (uncapped)
[x] Expected annual return E / catalyst window: 25.18% / 2yr (guardrail-capped — no dated catalyst)
[x] DCF Fair Value (PW):                      $35.6821/share (≈2,669.65p)
[x] Multiples-Based Fair Value:                $47.7109/share (≈3,570.03p)
[x] Blended Fair Value:                        3,209.59p
[x] Margin of Safety %:                        25–30% required → buy-ceiling range 2,246.71p–2,407.19p;
                                                current price (2,701.00p) is ABOVE this entire range
                                                (implied MoS only 15.85%) → NOT at buy price
[ ] BUY PRICE (limit order):                   not placed — Quality gate fails AND R/R gate fails at every grid point
[x] PRIMARY SELL TARGET (reference, for monitoring): 3,209.59p
[x] BULL-CASE TRIM TARGET (reference):         3,258.68p (Bull Blended FV 3,620.76p × 0.90)
[ ] STOP LOSS:                                 not applicable — no position being opened
[x] Risk/Reward Ratio:                         best case across full grid = 1.71:1 — FAILS the 2:1 minimum
[ ] Max $ Risk / POSITION SIZE:                not applicable — no position being opened
[x] Thesis invalidation / re-trigger conditions: see §11
```

---

## 11. Recommendation

# **PASS — Quality Score 61.3/100.0 fails the 80.0+ gate decisively (18.7 points short, robust to every generous sensitivity check run). Do not enter, regardless of how the reference Valuation/Composite work reads. Independently, the R/R gate also fails at every point in the standard grid (best case 1.71:1 < 2:1) — a second, self-sufficient reason not to enter even if the Quality gate had passed.**

**Why this is a genuine, examined "no," not a hasty pass:**

1. **The Quality gate failure is the primary, binding reason.** Experian is a real, profitable, oligopoly business with a documented moat (4 of 5 signals credited with cited evidence) — but the current framework's 80.0+ Quality Score bar is deliberately strict, and Experian's Growth (43.86), Balance Sheet (58.22), Margins (52.52), and Profitability (55.665) sub-scores are all solidly mid-range rather than exceptional. No single number is alarming; the gate simply requires more than "solid across the board" to clear 80.0.
2. **The Composite Score (36.8, reference only) is a textbook false green light.** It would read as an attractive "Cheap, buy standard position" signal in isolation — precisely the failure mode the 2026-06-29 Quality Score/Composite addition was built to close. Do not act on this number.
3. **The R/R gate fails independently**, by essentially the same margin as 06-19 (1.71:1 best case, unchanged) — the market has re-rated the stock and this framework's fair-value estimate in roughly the same proportion since June, leaving the entry math no better than it was.
4. **A material new qualitative finding this session:** FICO's Mortgage Direct License Program (effective Oct 2025) is an active, ongoing structural threat to bureau economics not present in the 06-19 analysis. It doesn't move the Quality Score (no company-level revenue-deceleration evidence yet) but it is the reason this session applied the Upside/Downside Modifier's guardrail cap rather than crediting the full computed upside, and it materially strengthens the bear case going forward.
5. **What would change this call:** (a) a Quality Score improvement — most plausibly via Growth (organic growth re-accelerating meaningfully above the current 6–8% guided band with continued TAM-expansion evidence) or Balance Sheet (continued deleveraging below ~1.0× Net Debt/EBITDA); this is a multi-quarter, fundamentals-driven path, not something a single re-score will move; (b) independently, price falling into the 2,247–2,407p buy-ceiling band would improve the R/R math, but per point 1, that alone still would not clear the Quality gate.

**What would trigger a re-score (Rule 9):**
- H1 FY27 results (~Nov 2026) — mandatory.
- Q1 FY27 trading update (16 Jul 2026) — imminent; not itself a full re-score trigger unless it reveals a guidance change or is a >15% price mover.
- Any quantified, company-specific disclosure of the FICO direct-license program's earnings impact on Experian specifically (currently only an industry-wide estimate exists).
- Board Chair succession announcement (governance monitoring, not itself a Rule 9 trigger per §8's management-change scoping).
- >15% unexplained price move from 2,701.00p in either direction.
- Quarterly Rate Environment Gate update (~Oct 2026) — Step 1 has now flipped from a narrow pass to a clear-but-not-extreme fail (+1.112pp short); worth rechecking as the 10Y moves.

**Process note:** this session documents the analytical recommendation only. No broker order has been placed and nothing has been logged in `decisions/` or `portfolio/holdings.md`.

---

## 12. Next Review Trigger

- **H1 FY27 results** (~Nov 2026) — mandatory re-score (Rule 9).
- **Q1 FY27 trading update** (16 Jul 2026) — near-term; re-score if it moves guidance or price >15%.
- **FICO direct-license program** — any EXPN-specific quantification of earnings impact, or evidence of the threat expanding beyond US mortgage tri-merge into other product lines.
- **>15% unexplained price move** from 2,701.00p (Rule 9).
- **Quality Score improvement path** — watch Growth (organic growth trend vs. the 6–8% FY27 guided band) and Balance Sheet (Net Debt/EBITDA trend) most closely, as the two sub-scores with the most plausible near-term upward mobility toward the 80.0 gate.
- **Board Chair transition** (effective 22 Jul 2026) — monitor successor announcement.

---

## Glossary

- **ADR** — not used this session (EXPN is a direct LSE listing, not a US ADR)
- **Beta** — a stock's sensitivity to overall market moves, used in the DCF's cost-of-equity calc.
- **Benchmark EBIT / Benchmark EPS** — Experian's own non-GAAP operating-profit/EPS basis, distinct from the GAAP/statutory EBIT this session uses for EV/EBIT and the DCF.
- **bps / pp** — basis points / percentage points, used throughout the Rate Gate and modifier math.
- **CAGR** — Compound Annual Growth Rate, used for revenue and FCF growth.
- **Catalyst window** — the 18–24-month (or default 2yr) timeframe within which a documented event must be expected to close the price/fair-value gap before the Upside/Downside Modifier can credit full upside.
- **Composite Score** — this framework's 50/50 blend of Quality Score and Valuation Score; computed here only as an explicitly-flagged reference number since Experian fails the Quality gate.
- **DCF** — Discounted Cash Flow, one of the two required fair-value methods.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **ERP (Equity Risk Premium)** — the extra return equity investors demand over the risk-free rate, an input to cost of equity.
- **EV / EV/EBIT** — Enterprise Value / the multiple of EV to operating profit used as a cheapness gauge.
- **EY (Earnings Yield)** — 1 ÷ Forward PE, compared against the 10Y Treasury in the Rate Environment Gate.
- **Fast Grower** — Peter Lynch's term for EPS growth >15%/yr for 3+ years; EXPN does not currently qualify (chain broken FY2025).
- **FCF / FCF Yield / FCF/NI conversion ratio** — Free Cash Flow and the two ratios built from it used in scoring and quality-gating.
- **FICO Score** — the US consumer credit score at the center of this session's new disruption-vector finding (direct-license program bypassing bureau resale).
- **Forward PE** — price ÷ next-twelve-months expected EPS.
- **GAAP** — Generally Accepted Accounting Principles, the standard basis for EXPN's statutory EBIT figures used here.
- **GBX / pence (GBp)** — one-hundredth of one British pound; EXPN trades in GBX on the LSE but reports financials in USD, the central currency-consistency issue in this session.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of weighted score; none fire for EXPN.
- **Historical PE Modifier** — Upgrade 2's ±10 additive adjustment based on Forward PE's position vs. the 5-year average PE.
- **Hurdle rate** — the 10% minimum acceptable annual return the Upside/Downside Modifier measures expected return against.
- **Invested Capital / NOPAT** — this framework's ROIC-calculation convention (NOPAT ÷ [Total Debt + Equity − Cash]).
- **Moat** — a durable competitive advantage; EXPN credited 4 of 5 documented signals.
- **MoS (Margin of Safety)** — how far below fair value the buy price is set.
- **Organic revenue growth** — revenue growth excluding M&A, disposals, and FX effects.
- **PEG ratio** — PE ÷ earnings growth rate; not applicable to EXPN this session (not a Fast Grower).
- **PW (Probability-Weighted) Fair Value** — the 25% bull / 50% base / 25% bear blended fair-value estimate.
- **Quality Score** — this framework's 0–100.0 graded quality metric; EXPN scores 61.3, failing the 80.0+ gate.
- **Rate Environment Gate / Rate Regime Modifier** — the mandatory pre-Phase-02 check comparing earnings yield to the 10Y Treasury, plus the yield-bracket-based additive modifier.
- **ROCE (Return on Capital Employed)** — Experian's own disclosed profitability metric (17.2% FY26), used as a cross-check against this framework's computed ROIC.
- **ROE / ROIC** — Return on Equity / Return on Invested Capital, both used in the legacy Phase 01 table and the Quality Score respectively.
- **Rule 0 / Rule 4 / Rule 5 / Rule 6 / Rule 7 / Rule 9 / Rule 10** — this framework's standing instructions on live pricing, sanity checks, comparable-company standards, normalization, mandatory scenario analysis, re-valuation triggers, and separating intrinsic value from market price.
- **Shareholder yield** — dividend yield plus net buyback yield.
- **Terminal Value** — the DCF's lump-sum value for all cash flows beyond the explicit forecast period.
- **Tri-merge (credit report)** — the mortgage-industry practice of combining all three bureaus' reports, the distribution channel FICO's direct-license program partially bypasses.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported results.
- **Turnaround Sub-Gate** — not applicable this session (EXPN is not a turnaround candidate; it fails the new graded Quality gate, not the legacy binary screen).
- **Upside/Downside Modifier** — the ±15-bounded additive adjustment based on expected annual return; applied here at the guardrail-capped −5.0.
- **WACC** — Weighted Average Cost of Capital, the DCF's discount rate.

# NEW POSITION — Wise Group plc (Nasdaq: WSE / LSE secondary: WISE) — 2026-08-27

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, automated/unattended run)
**Date:** 27 Aug 2026
**10Y US Treasury Yield:** 4.65% (TradingEconomics via WebSearch — "eased to 4.65%... from the 20-month high of 4.75% on August 21," reading dated 2026-08-26, most recent published as of this session)
**Rate Regime Modifier in effect:** +5 (yield in the 3.5–5% bracket) — see §3
**WISE portfolio weight:** 0% — not held, no row in [holdings.md](../portfolio/holdings.md)
**Prior coverage:** None. No `watchlist/` entry for WISE anywhere in the repo prior to this session (confirmed by direct search before this run) — first-ever `/new-position` pass for this ticker, per the repo's "no watchlist entry exists" decision rule.
**Sector:** Financial Technology — cross-border consumer/business money transfer and payments infrastructure

*Jargon decoded on first use (non-finance reader) — full definitions in §8 Glossary: OCC = the US bank-charter regulator; AML = anti-money-laundering; MTL = money-transmission license (the license Wise actually operates under in the US, distinct from the bank charter it was denied); TTM = trailing twelve months; NOPAT = net operating profit after tax; ROIC = return on invested capital; EBIT/EBITDA = operating profit (before/also before depreciation & amortization); CAGR = compound annual growth rate; FCF = free cash flow; DCF = discounted cash flow; WACC = discount rate used in a DCF; UFCF = Wise's own "Underlying Free Cash Flow" metric.*

---

## 0. Trigger — Telegram post and independent verification

**Source:** Telegram channel `bolshegold`, post `bolshegold/10051` (2026-08-27) — claimed Wise plc "lost its US license" and was "blocked for US LLC banking." Per this framework's non-negotiable rule, **the post text is never used as financial data below — it is only the signal to run this evaluation.** Since no watchlist entry exists anywhere in the repo for WISE, this evaluation runs regardless of whether the claim itself checks out (per the repo's documented decision rule).

**Independent verification (WebSearch, not the Telegram post):**

**Confirmed, with an important correction to the claim's framing.** Wise was **denied**, not stripped of, a national trust bank charter:
- On **2026-07-24**, the US Office of the Comptroller of the Currency (OCC) **denied** Wise's application for a national trust bank charter, citing "significant supervisory and compliance concerns" — specifically deficiencies in Wise's anti-money-laundering (AML) controls and a lack of banking-law/fiduciary expertise on management's part. [The Paypers; MLex; CityAM; AMLintelligence; PaymentExpert; Forbes — all 2026-07-24/07-25]
- **This was a denial of a new application, not a loss of an existing license.** Wise never held a national trust bank charter — the claim "lost its license" overstates what happened. Wise's US business continues operating under its existing patchwork of **state-level money-transmission licenses (MTLs)**, unaffected by the OCC decision. Wise stated it will file a revised application, and separately plans to reapply under the 2025 US stablecoin framework (the **GENIUS Act**), which it believes offers a clearer path. [Same sources]
- On the news, Wise's Nasdaq-listed shares (WSE) fell **6.2%, from $12.08 to $11.33**, on 2026-07-24. [PRNewswire/GlobeNewswire law-firm releases, sourced below]

**A materially bigger story than the Telegram post captured.** The OCC denial is one piece of a larger, live regulatory/legal cluster:
- **Brussels criminal investigation:** Reuters reported on **2026-06-01** that the Brussels Public Prosecutor's Office is investigating Wise's European entity over **more than €500M (~$582.5M)** in transactions flagged as suspicious, with **alleged links to fraud, corruption, and drug trafficking**. [Cited in multiple 2026-08 law-firm press releases summarizing the securities complaint, e.g. GlobeNewswire/PRNewswire]
- **Active securities-fraud class action:** A federal securities class action was filed against Wise Group plc, covering the class period **2026-05-11 to 2026-07-23** (i.e., from the Nasdaq listing through the day before the OCC denial), alleging Wise "failed to maintain appropriate anti-money laundering procedures" and understated the resulting regulatory risk to investors. **Lead-plaintiff deadline: 2026-09-29** — the litigation is open and unresolved as of this session. [Multiple law-firm PRNewswire/GlobeNewswire notices, 2026-08-17 through 2026-08-21]

**Net verdict on the trigger:** the underlying regulatory concern is real, dated, and ongoing — but it is a **new-charter denial plus an open AML/criminal investigation and securities litigation**, not a "license loss / US banking blocked" event in the literal sense the Telegram post implied. Both framings point toward the same underlying risk (AML control weaknesses), so this is treated as **confirmed-with-correction**, not "not found." This risk cluster is unresolved and directly relevant to today's evaluation — see §5 and §7.

---

## 1. Live Price (Rule 0)

Wise's **primary listing moved from the London Stock Exchange to Nasdaq on 2026-05-11** (scheme of arrangement effective 2026-05-08), retaining a **secondary LSE listing**. This is itself a correction to this session's brief, which assumed the old OTC ADR ticker "WPLCF" was still current — **it is not**. WPLCF was Wise's pre-2026 unsponsored US OTC ADR; since the May 2026 direct Nasdaq listing, Wise's ordinary shares trade natively on Nasdaq under **WSE**, and WPLCF is defunct/superseded. This repo's holdings are USD-denominated, so **WSE (Nasdaq, USD) is used as the primary price and currency for every calculation below.**

| Field | Value | Source |
|---|---|---|
| **Live price used (WSE, Nasdaq)** | **$13.23** | Yahoo Finance chart API, `regularMarketPrice`, `regularMarketTime` epoch 1787774400 = **2026-08-26 20:00:00 UTC** (Nasdaq's 16:00 ET close — the most recent live trade at the time of this session; Nasdaq had not yet opened for 2026-08-27 as of data pull ~12:40 UTC) |
| Prior close (2026-08-25) | $12.51 | Same source, `chartPreviousClose` |
| Day range (08-26) | $13.14 – $13.31 | Same source |
| 52-week range | $10.36 – $17.47 | Same source |
| Cross-check: LSE secondary listing (WISE.L) | **992.99 GBp** (£9.9299) | Yahoo Finance chart API, live intraday, timestamp 2026-08-27 12:38:42 UTC |
| GBP/USD spot (for the cross-check only — not used in any downstream calc, all calcs are USD-native) | ≈1.362 | WebSearch (XE.com/Investing.com aggregation), 2026-08-27 |
| Cross-check result | £9.9299 × 1.362 ≈ **$13.52** vs. WSE's $13.23 — a ~2.2% cross-listing basis, explained by the one-day lag (yesterday's US close vs. today's live UK intraday reading), not a data error | Computed |
| Analyst consensus (Rule 0 Step 4 bull-case sanity check) | Mean target **$17.16**, median $16.90, range $15.00–$19.50, 13 analysts | Yahoo Finance `financialData`, 2026-08-27 pull |
| Shares outstanding | 983,729,421 | Yahoo Finance `defaultKeyStatistics` |
| Market cap | **$13,014.7M** | Computed (983.729M × $13.23), cross-checked against Yahoo's own `marketCap` field ($13,014,739,968) |

**Flag:** the $17.16 analyst consensus target sits well above this session's own fair-value work (§4) — a material divergence discussed explicitly in §5.

---

## 2. Quality Score — Phase 01 (methodology version 2026-06-29)

### 2.1 Data sourcing and a real structural data gap

Wise's FY2026 20-F (filed with the SEC 2026-06-25, accession 0001193125-26-282911) is prepared under **US GAAP** (not IFRS) following the Nasdaq primary listing — confirmed directly against the SEC XBRL `companyfacts` API (`data.sec.gov/api/xbrl/companyfacts/CIK0002099039.json`), which tags the filing under the `us-gaap` taxonomy. `yfinance` itself failed with a persistent TLS/`curl_cffi` connection-reset error this session (same documented failure mode as prior sessions, e.g. 2026-08-27 CRWD) — worked around by pulling Yahoo Finance's underlying chart/quoteSummary JSON APIs directly via a plain `requests` session (crumb-authenticated), and primary financial-statement data directly from SEC EDGAR (XBRL companyfacts + the RNS-published full income statement/balance sheet/cash-flow statement text) and Wise's own investor-relations PDFs, per Rule 0/Rule 6 sourcing discipline.

**Genuine, disclosed data-structure gap (flagged, not invented around):** Wise's US-GAAP income statement does **not** present a discrete "cost of revenue"/"gross profit" line (confirmed: no `CostOfRevenue` or `GrossProfit` XBRL tag exists anywhere in the filing). Wise's UK-era IFRS "underlying basis" reports (used through FY2025) *did* disclose "Cost of sales" and "Underlying gross profit," but that non-GAAP presentation — along with "Underlying Free Cash Flow (UFCF)" — **appears to have been discontinued** in the FY2026 US-GAAP release (confirmed: neither term appears anywhere in the 735,897-character stripped text of the full 20-F). This session builds an explicit, documented convention from the disclosed GAAP line items rather than inventing a number — shown in full below, with the discontinued prior-year UK metric shown alongside as a directional cross-check.

### 2.2 FY2026 income statement (USD millions, year ended 31 March 2026, vs. FY2025)

Sourced from the RNS full text of the FY26 Results announcement (SEC 6-K, filed 2026-06-25) — the audited Consolidated Statement of Comprehensive Income:

| Line | FY2026 | FY2025 |
|---|---|---|
| Transaction revenue | 1,893.6 | 1,546.3 |
| Interest income on customer balances | 806.1 | 758.3 |
| Interest expense on customer liabilities | (196.9) | (205.7) |
| **Net revenue** | **2,502.8** | **2,098.9** |
| Transaction expense | (513.6) | (378.0) |
| Transaction and credit losses | (13.9) | (11.6) |
| Technology and development | (434.3) | (314.1) |
| Servicing | (396.6) | (287.5) |
| Marketing and sales | (171.8) | (106.1) |
| General and administrative | (381.9) | (273.4) |
| **Total operating expenses** | **(1,912.1)** | **(1,370.7)** |
| **Operating income (EBIT)** | **590.7** | **728.2** |
| Other income/(loss), net | 69.7 | (10.7) |
| **Income before tax** | **660.4** | **717.5** |
| Income tax expense | (161.7) | (167.2) |
| **Net income** | **498.7** | **550.3** |
| EPS, basic (cents) | 48.92 | 53.31 |

Cross-checked against SEC XBRL `companyfacts` (`OperatingIncomeLoss`, `NetIncomeLoss`, `RevenuesNetOfInterestExpense`) — exact match. FY2024 comparative (also from XBRL): Net revenue $1,776.1M, Operating income $650.1M, Net income $501.5M.

**A real, material finding: operating income fell 18.9% YoY despite 19% revenue growth** — operating margin compressed from 34.7% (FY25) to 23.6% (FY26). Per management's own FY26 earnings call and guidance materials (WebSearch, Investing.com transcript): the decline is **deliberate reinvestment**, not deterioration — marketing spend +60% to $172M, servicing costs +38% to $397M (headcount +26%), technology +38% to $434M (headcount +22%, transactional-volume-driven infra costs). Income-before-tax margin: 37% (FY24) → 34% (FY25) → 26.4% (FY26). **FY27 guidance reiterated:** net revenue growth "around the middle" of 15–20%, income-before-tax margin "around the top" of 20–25% — i.e., management expects the margin decline to **stabilize, not continue** near-term, while explicitly flagging a **lower "15–20%" medium-term target margin** once Wise pays out 80% of interest income above the first 1% yield to customers (a deliberate, structural, multi-year strategy of returning more economics to customers, not a one-off). Q1 FY27 (reported 2026-07-16): net revenue +25% YoY to $714.0M — top-line momentum has if anything accelerated. [Investing.com, StockTitan, GlobeNewswire — all 2026-07/08]

### 2.3 Balance sheet (30 March 2026, USD millions)

| Item | FY2026 | FY2025 |
|---|---|---|
| Cash and cash equivalents | 27,802.2 | 18,066.3 |
| AFS debt securities | 4,582.7 | 6,013.6 |
| **Total assets** | **33,259.8** | **24,781.1** |
| Funds payable and amounts due to customers | 30,254.2 | 22,279.9 |
| Short-term debt | 6.0 | 128.4 |
| Long-term debt | 328.7 | 0.0 |
| **Total liabilities** | **31,334.6** | **23,043.7** |
| **Total shareholders' equity** | **1,925.2** | **1,737.4** |

**Customer-float distortion, explicitly handled, not ignored:** $30,254.2M of the $31,334.6M in total liabilities (96.5%) is "Funds payable and amounts due to customers" — segregated, safeguarded customer money in transit, not Wise's own obligation in any economic sense, and the matching $27.8B+$4.6B in cash/AFS securities on the asset side is predominantly the corresponding safeguarded asset, not "excess corporate cash." **Convention used throughout this session:** Net Debt = **gross debt only, no cash netting** ($334.7M = $328.7M long-term + $6.0M short-term) — the most conservative reading, since Wise does not separately disclose a clean "own funds vs. customer-safeguarded" cash split precise enough to net with confidence (never invent/estimate a missing split). Total debt is small enough relative to EBITDA that this conservative choice doesn't change any pass/fail conclusion below (see §2.6). Confirmed investment-grade: **S&P and Fitch both rate Wise BBB (stable)** [S&P Global Ratings, 2026], consistent with a £250M, 5.10%-coupon bond outstanding (issued via Wise Financing plc, Nov 2025) whose USD-converted balance ($328.7M) matches the disclosed long-term debt figure.

### 2.4 Profitability (25% weight)

```
TTM basis = FY2026 (year ended 31 Mar 2026) — Wise's fiscal year end is the most recent complete
  reporting period; a true quarterly-reconstructed TTM (through Jun 2026) was not attempted given
  the added complexity of the FY2026 USD/GAAP reporting-regime transition — flagged as a minor
  limitation (FY2026 is ~5 months stale as of this session), not a blocking gap.

Net Margin = 498.7 / 2,502.8 = 19.926%
Effective tax rate = 161.7 / 660.4 = 24.485%
NOPAT = EBIT × (1 − tax) = 590.7 × 0.75515 = 446.07
Invested Capital = Total Debt (334.7) + Stockholders' Equity (1,925.2) = 2,259.9
  (no-cash-netting convention, consistent with §2.3 and the 2026-08-25 LLY session's precedent)
ROIC = 446.07 / 2,259.9 = 19.738%

NetMargin_Component = clamp((19.926/30)×100, 0, 100) = 66.419
ROIC_Component       = clamp((19.738/30)×100, 0, 100) = 65.794
Profitability_Score (uncapped) = (66.419 + 65.794) / 2 = 66.107
```

FCF-positivity cap check (§2.9 below): Wise is FCF-positive every year on record — **no cap applies**. **Profitability_Score = 66.107**

### 2.5 Margins (15% weight)

```
Gross Profit (this session's convention) = Net revenue − Transaction expense − Transaction and
  credit losses = 2,502.8 − 513.6 − 13.9 = 1,975.3
  (the two GAAP line items most directly analogous to "cost of sales" for a payments company —
  the same conceptual boundary as Wise's own discontinued IFRS "Cost of sales + Net credit losses"
  split, cross-checked below)
Gross Margin = 1,975.3 / 2,502.8 = 78.924%
GrossMargin_Score = clamp((78.924/80)×100, 0, 100) = 98.655
```

No trend-bonus applicable (already far above the 40% bonus-eligibility ceiling). **Cross-check against Wise's own (discontinued) IFRS "Underlying gross profit" metric**, for directional consistency only (different revenue base — "Underlying income" excludes interest income above the first 1% yield, so not directly comparable): FY2024 72.7%, FY2025 75.25% [Wise plc FY2025 Results PDF, 5 June 2025, "Financials – underlying basis" table]. Both readings show gross margin flat-to-improving and comfortably clear of any threshold this framework tests — the convention choice doesn't affect the outcome. **Margins_Score = 98.655**

### 2.6 Balance Sheet (15% weight)

```
Net Debt (conservative, gross debt only — see §2.3) = 334.7
EBITDA = Operating Income (590.7) + D&A (14.4, per XBRL DepreciationDepletionAndAmortization) = 605.1
Net Debt/EBITDA = 334.7 / 605.1 = 0.553×
BalanceSheet_Score = clamp(100×(1 − 0.553/4), 0, 100) = 86.172
```

Comfortably clear of the 2.5× standard hard-disqualifier threshold — no need to invoke the Upgrade 5 asset-light /6-denominator override (payment-network eligible given BBB investment-grade rating, but doesn't change the conclusion). **BalanceSheet_Score = 86.172**

### 2.7 Growth (20% weight)

```
Revenue: FY2023 $1,197M → FY2026 $2,502.8M
  (FY2023 figure from stockanalysis.com's USD-converted annual series, cross-checked: its FY2024
  ($1,776M), FY2025 ($2,099M), and FY2026 ($2,503M) figures match SEC XBRL exactly to the nearest
  $1M, giving confidence in the FY2023 figure it reports on the same consistent basis)
3yr CAGR = (2,502.8/1,197.0)^(1/3) − 1 = 27.873%
Growth_Score (base) = clamp((27.873/25)×100, 0, 100) = 100.0 (capped)
```

**TAM-expansion modifier (+10, documented, capped — no numeric effect at the ceiling):** Wise's own investor materials frame the cross-border payments opportunity at **$43 trillion**; FY2026 cross-border volume grew 31% YoY to $243B against an overall cross-border-payments-market growth estimate of ~7.9% CAGR (Grand View Research industry report) — a large, cited, multi-year share-gain differential. Wise **passed Western Union's transfer volumes in 2022** [Bloomberg Second Measure, via secondmeasure.com], and Q1 FY27 (Jul 2026) revenue growth accelerated further to +25% YoY. **No growth-deceleration penalty applies** — if anything, growth has re-accelerated into FY27. **Growth_Score = 100.0**

### 2.8 Moat Signal (15% weight)

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | Wise passed Western Union's cross-border transfer volume in 2022 [Bloomberg Second Measure]; among Wise/Xoom/Western Union/MoneyGram, Wise's share of transacted volume rose to 47% by Sept 2021 (dated, but a real, cited milestone establishing the trajectory) [secondmeasure.com]; FY2026 volume growth (31% YoY) far outpaces total-market growth (~7.9% CAGR, Grand View Research) — continued share gain into the present. |
| Brand premium (pricing power) | **FALSE** | Evidence runs the opposite direction: Wise's blended cross-border take rate has been **cut** in successive years — 0.67% (FY24) → 0.62% → 0.58% (FY25) → 0.52% (FY26), with guidance for a further 1–2bps/quarter decline in FY27. Management explicitly states it "does not set a floor on pricing" and treats price cuts as a **deliberate competitive weapon to starve out competitors** [Investing.com FY26 slides commentary, thepursuitofcompounding.substack.com] — the clean opposite of "price increases without volume loss." |
| Network effect | **TRUE** | Documented mechanism: Wise's core infrastructure nets/matches currency-corridor flows internally via direct connections to 8 domestic payment systems (UK, EU, Singapore, Australia, India, Philippines, Brazil, Japan) rather than moving money cross-border on every transaction — more volume in a corridor deepens matching liquidity, and instant-settlement rates have risen with scale (up to 90% instant on some newly-integrated rails per Wise's own FY24/FY25 results commentary) — a genuine "more users → better outcome for all users" dynamic, not merely a cost-scale story. |
| Switching costs | **TRUE, but segment-caveated** | Wise Platform — the B2B infrastructure-as-a-service arm — counts Morgan Stanley, Standard Chartered, Nubank, and Monzo among banks that have integrated Wise's payments rails into their own products [wise.com/platform; FinTech press]. Deep technical/compliance integration of this kind carries real, documented bank-side switching costs. **Caveat, shown transparently:** this applies to the smaller enterprise/Platform segment, not Wise's dominant retail/personal segment, where the entire value proposition is explicitly LOW switching friction (customers are meant to switch away from expensive banks *to* Wise) — the opposite dynamic. |
| Scale cost advantage | **FALSE — not credited** | Wise's own CEO letter states unit costs fall as the business scales, translating into lower prices (consistent with the pricing-cut evidence above), and third-party commentary cites an "eightfold" cost-per-transaction drop following the Philippines InstaPay integration — but **no cost-per-unit figure benchmarked against a smaller/specific competitor was found**, the same evidentiary gap that sank this signal for LLY (2026-08-25 session) and for the same reason it is not credited here, applying the same strict bar. |

```
Moat_Score = (3/5) × 100 = 60.0
```

**Sensitivity, shown transparently (this is the most judgment-laden sub-score and the one closest to flipping the gate outcome):** crediting only 2/5 signals (dropping "switching costs" given its retail-segment caveat) would produce Moat_Score = 40.0 and a Quality Score of **80.3** — still, barely, clearing the gate. Crediting only 1/5 (also dropping "network effect" on a stricter reading) would produce Moat_Score = 20.0 and Quality Score **77.3** — *failing* the gate. The 3/5 reading used above (each signal backed by a specific, dated, cited mechanism, consistent with the evidentiary standard applied in the LLY/CRWD precedent sessions) is this session's considered call, but the reader should know the gate outcome is genuinely close and moat-signal-sensitive, not a wide margin.

### 2.9 FCF Quality (10% weight) — including the "own-funds" FCF construction

**A second genuine data-structure issue, handled explicitly:** Wise's raw GAAP "Net cash from operating activities" ($7,553.9M FY26) is **not usable as FCF** for this framework — it is overwhelmingly driven by the year-over-year change in "Funds payable and amounts due to customers" ($6,999.7M of the $7,553.9M total, per the full Consolidated Statement of Cash Flows below), i.e., customer money flowing through the balance sheet, not Wise's own economic cash generation. Using it unadjusted would produce a nonsensical FCF Yield.

**Full cash flow statement (USD millions, FY2026 vs. FY2025), sourced from the RNS text:**

| Line | FY2026 | FY2025 |
|---|---|---|
| Net income | 498.7 | 550.3 |
| D&A | 14.4 | 9.7 |
| Other operating adjustments (SBC, impairment, FX, deferred tax, leases, other) | 213.1 | 108.9 |
| Working-capital items (receivables, prepaid, payables, lease liabilities) | (172.6) | (91.2) |
| **Funds payable and amounts due to customers (change)** | **6,999.7** | **5,138.4** |
| **Net cash from operating activities** | **7,553.9** | **5,719.5** |
| Purchase of PP&E | (19.6) | (44.1) |
| Purchase of intangible assets | (1.8) | (1.2) |

**This session's "own-funds FCF" construction:** Adjusted OCF = Net cash from operating activities − change in funds payable to customers; FCF = Adjusted OCF − CapEx (PP&E + intangibles):

```
FY2026: Adjusted OCF = 7,553.9 − 6,999.7 = 554.2; FCF = 554.2 − 21.4 = 532.8
FY2025: Adjusted OCF = 5,719.5 − 5,138.4 = 581.1; FCF = 581.1 − 45.3 = 535.8
```

**Cross-check against Wise's own (discontinued) UFCF metric:** FY2025 UFCF = £332.7m (≈$422M at an average FY2025 GBP/USD rate) [Wise plc FY2025 Results PDF] — same order of magnitude as this session's $535.8M construction; the residual gap plausibly reflects definitional differences (Wise's UFCF nets a few additional items this session's simpler two-line construction doesn't) and FX-rate timing. Given the same order of magnitude and same sign, this session's construction is treated as a reasonable, transparent proxy — not a precise restatement of Wise's discontinued non-GAAP figure.

```
FCF/NI Ratio (FY2026) = 532.8 / 498.7 = 106.838%
FCFQuality_Score = clamp(((1.06838 − 0.40)/0.60)×100, 0, 100) = 100.0 (capped)
```

**FCFQuality_Score = 100.0**

### 2.10 Hard disqualifier check (all three)

| Check | Value | Result |
|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years | FY2026 106.8%, FY2025 97.4% (own-funds basis) — both comfortably above 70% | ✅ PASS |
| Net Debt/EBITDA over threshold | 0.553× vs. 2.5× standard | ✅ PASS, comfortably |
| Not FCF-positive for 3+ consecutive years | FY2023 (£156.0m FCF), FY2024 (£247.0m–£486.6m depending on which year's report's definition), FY2025 (£332.7m UFCF / $535.8M own-funds), FY2026 ($532.8M own-funds) — **every year on record is positive** under every definition Wise or this session has used | ✅ PASS |

**No hard disqualifier fires.**

### 2.11 Final Quality Score

```
Quality Score = (66.107×0.25) + (98.655×0.15) + (100.0×0.20) + (86.172×0.15) + (60.0×0.15) + (100.0×0.10)
              = 16.527 + 14.798 + 20.000 + 12.926 + 9.000 + 10.000
              = 83.251 → rounds to 83.3
```

**Quality Score = 83.3 / 100.0 — CLEARS the 80.0+ gate** (see §2.8 for the moat-signal sensitivity — this outcome is genuine but not a wide margin). Proceeding to Phase 02.

---

## 3. Rate Environment Gate

```
Forward PE = 19.064× (live price $13.23 ÷ forward EPS $0.694, Yahoo Finance)
Earnings Yield = 1/19.064 = 5.246%
Spread vs. 10Y Treasury (4.65%) = 5.246% − 4.65% = +0.596pp
```

Spread < +1.5% → **Step 1 fails, +5 additive flag.** 10Y yield (4.65%) sits in the 3.5–5% bracket → **Step 2 Rate Regime Modifier = +5.** **Combined Rate Gate adjustment: +10.**

---

## 4. Valuation Score — Phase 02 (methodology version 2026-06-29)

### 4.1 PEG / Fast-Grower eligibility

**Not applicable.** Net income *fell* 9.4% YoY (FY26 $498.7M vs. FY25 $550.3M) — EPS growth was negative in the most recent year, decisively failing the ">15% EPS growth for 3+ years" Fast-Grower test regardless of any earlier-year reconstruction. Per the Final Score Formula note, **PEG's 15% weight redistributes to EV/EBIT (→ 40% weight).**

### 4.2 Sub-scores

```
FCF Yield (40%): FCF (own-funds, $532.8M) / Market Cap ($13,014.7M) = 4.094%
  FCF_Score = clamp(100×(1 − 4.094/10), 0, 100) = 59.062

EV/EBIT (40%, PEG redistributed): EV = Market Cap + Debt (no cash netting, §2.3) = 13,014.7 + 334.7 = 13,349.4
  EV/EBIT = 13,349.4 / 590.7 = 22.599×
  EV/EBIT_Score = clamp((22.599−12)/23×100, 0, 100) = 46.084

Forward PE (20%): no-history fallback used, explicitly flagged.
  Wise's earnings base has changed reporting regime THREE times inside the trailing 5-year
  window (legacy pre-2024 IFRS presentation → 2024–2026 "underlying basis" IFRS → 2026+ US-GAAP
  post-Nasdaq-listing), on top of the underlying currency changing (GBP→USD). A reconstructed
  5yr trailing-PE series across these discontinuities would be noisy to the point of misleading,
  squarely the "GAAP earnings base too distorted to be meaningful" case the framework's own
  no-history fallback is written for.
  FwdPE_Score = 50.0 (neutral, flagged)
```

```
Raw weighted score = (59.062×0.40) + (46.084×0.40) + (50.0×0.20)
                    = 23.625 + 18.434 + 10.000 = 52.058

Plus Rate Gate (+10) = 62.058 before the Upside/Downside Modifier
```

### 4.3 Upside/Downside Modifier — full calc shown

**Fair Value — DCF (3-stage per Rule 2), bull/base/bear.** WACC built from CAPM: risk-free 4.65% (10Y UST) + beta (0.513, Yahoo) × 5% equity risk premium ≈ 7.2% cost of equity — a base WACC of **8.5%** is used instead (deliberately above the raw CAPM output, reflecting the real, currently-materializing regulatory/AML risk documented in §0/§5 that a historical-beta-only estimate doesn't capture), varied ±1% for bull/bear per Rule 2. Terminal growth 2.5% base (2.8% bull, 2.0% bear, all ≤ the Rule 2 GDP cap). Tax rate 24.5% throughout; D&A and CapEx held at their FY2026 ratios to revenue (0.58% and 0.85% respectively).

**Explicitly modeled, not sourced consensus (flagged, per the same convention the LLY session used):** Stage 1 (FY27–31) growth/margin assumptions below directly incorporate management's own FY27 guidance (net revenue growth "around the middle" of 15–20%; income-before-tax margin "around the top" of 20–25%, glide-path toward a **lower** "15–20%" medium-term target) — i.e., the base case does **not** assume margin reverts to FY24's 36.6% peak; it assumes the structural compression management itself has guided to.

| Scenario | Stage-1 revenue growth (FY27→31) | Stage-1 operating margin | Stage-2 fade | WACC | Terminal g | **DCF FV/share** |
|---|---|---|---|---|---|---|
| Bull | 20%→12% | 26%→25% (stabilizes near current) | 10%→3% | 7.5% | 2.8% | **$20.65** |
| Base | 17.5%→10% | 24%→17% (glides to guided medium-term band) | 8.5%→2.5% | 8.5% | 2.5% | **$9.88** |
| Bear | 12%→5% | 20%→14% (compliance-cost-pressured, per §0/§5) | 4%→2% | 9.5% | 2.0% | **$4.59** |

**Multiples-Based Value.** Two peer groupings computed, per Rule 5's requirement (min 5 peers, trim outliers on business-model/scale grounds):

- **Full 5-peer set** (PYPL, RELY, PAYO, EEFT, WU — via Yahoo Finance): median EV/EBIT 9.64×, median forward PE 10.67× → implied $5.45/sh and $7.40/sh. **Flag:** PYPL is >13× Wise's revenue scale (violates Rule 5's ±50% scale guideline outright); WU and EEFT are legacy, structurally-declining money-transfer networks (low-single-digit or negative volume growth vs. Wise's 19–31%) — a real business-model/growth-profile mismatch, not a like-for-like comp.
- **Growth-comparable subset** (RELY, PAYO, NU — digital-native, high-growth fintech/payments peers, Rule 5's "similar business model" trimming applied): median EV/EBIT 18.57×, median forward PE 15.47×, median EV/Revenue 2.66× → **$10.81/sh, $10.74/sh, $6.43/sh, averaged = $9.33/sh.** This subset converges much more closely with the DCF base case ($9.88) than the full-peer median does — used as this session's **primary Multiples-Based Value ($9.33/sh)**, with the full-peer figure shown as context, not used in the blend.

```
Blended FV (40% DCF + 60% Multiples, per scenario):
  Bull = 0.40×20.65 + 0.60×9.33 = 13.858
  Base = 0.40×9.88  + 0.60×9.33 = 9.550
  Bear = 0.40×4.59  + 0.60×9.33 = 7.434

PW Fair Value (25/50/25) = 0.25×13.858 + 0.50×9.550 + 0.25×7.434 = $10.10/share
```

**Sanity-check flag (Rule 4):** this $10.10 PW Fair Value sits **well below** the $17.16 mean analyst target (§1) — a large, genuine divergence. Not reconciled away: this session's model leans on management's own guided margin glide-down (a real, disclosed input most sell-side one-line summaries may not fully price in) and a stricter peer-comp screen; the analyst consensus may reflect a more optimistic margin-recovery view, or simply less weight on the still-unresolved AML/regulatory overhang (§0/§5). **Both figures are shown — the reader should weigh this divergence, not take either as settled.**

```
Gap Upside % = (10.10/13.23) − 1 = −23.673%
Catalyst window: no specific 18–24mo re-rating catalyst identified (Rule 10) — the live catalysts
  in view are negative/unresolved (OCC re-application timeline unknown, Brussels investigation
  outcome unknown, securities litigation runs at least through the 2026-09-29 lead-plaintiff
  deadline and likely well beyond). Per the modifier's guardrail, a missing catalyst caps only the
  UPSIDE (negative-modifier) side — this reading has negative E, so the guardrail does not apply;
  shown for completeness.
Annualized gap (2yr default window, Rule 10) = −23.673%/2 = −11.837%/yr
Intrinsic growth = Base-case Stage-1 FCF CAGR = ($601.5M / $524.6M)^(1/5) − 1 = +2.774%/yr
  (deliberately modest — reflects the base case's margin-compression assumption, not revenue growth)
Shareholder yield = net buybacks only (no dividend — payoutRatio 0.0, Yahoo) =
  FY26 share repurchases $473.4M / Market Cap $13,014.7M = +3.637%
E = −11.837 + 2.774 + 3.637 = −5.426%
```

```
E < 0 → M = 5 + 10×clamp((−E)/10pp, 0, 1) = 5 + 10×clamp(5.426/10, 0, 1) = 5 + 5.426 = 10.426
```

### 4.4 Final Valuation Score

```
Valuation Score = 52.058 (raw) + 10 (Rate Gate) + 10.426 (Upside/Downside Modifier)
                = 72.484 → rounds to 72.5
```

---

## 5. Composite Score

```
Composite Score = 0.50×(100 − Quality Score) + 0.50×Valuation Score
                = 0.50×(100 − 83.3) + 0.50×72.5
                = 8.35 + 36.25
                = 44.60 → rounds to 44.6
```

**Composite Score = 44.6/100.0.** Per the Action Table, a score of 30.0–49.9 mechanically maps to **"BUY — Standard position 3–5%."** This is presented faithfully below, but the order-setup discipline in §6 does not support acting on it — read that section before the recommendation in §7.

**A genuine, important tension, surfaced rather than smoothed over:** the Composite Score lands in a "buy" band primarily because the **Quality Score is high (83.3)** — the Composite formula weights quality and cheapness equally, and a high-quality business earns a lower (more attractive) Composite even at a valuation this session's own fair-value work treats as somewhat rich. The Valuation Score and Upside/Downside Modifier, computed independently in §4, already point the other way (modest *negative* expected return, E = −5.4%/yr). Both are shown in full — the Composite Score formula is applied exactly as written, not overridden by this session's own view.

---

## 6. Fair Value & Order Setup — and why it fails the R/R gate

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Steps 2–6, run for every score-band that could support a BUY:

```
Blended (PW) Fair Value = $10.10/share (§4.3)
MoS band for Score 30.0–49.9: 25–30%
Buy Price = FV × (1 − MoS): range $7.07 (30% MoS) – $7.57 (25% MoS)
Max Acceptable Loss band for Score 30.0–49.9: 25–30%
Stop Loss = Buy Price × (1 − Max Loss)
Sell Target = Fair Value (baseline) = $10.10
```

**R/R computed across the full prescribed parameter grid** (per "show every calculation" — no single cherry-picked combination):

| MoS | Buy Price | Max Loss | Stop Loss | R/R |
|---|---|---|---|---|
| 25% | $7.57 | 25% | $5.68 | 1.33:1 |
| 25% | $7.57 | 30% | $5.30 | 1.11:1 |
| 30% | $7.07 | 25% | $5.30 | **1.71:1 (best case)** |
| 30% | $7.07 | 30% | $4.95 | 1.43:1 |

**Every combination inside the prescribed 25–30% / 25–30% bands falls short of the mandatory 2:1 minimum** — the best case (widest MoS, tightest stop) reaches only 1.71:1. Per fair-value-methodology.md Step 6: *"If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely."*

**Important, and worth stating precisely: "wait for a lower entry" does not fix this here.** Buy Price, Stop Loss, and Sell Target are all anchored to the modeled Fair Value and the score-band percentages — not to today's live price. A falling market price doesn't change any of those three anchors; it only changes how close the live price is to the (already R/R-failing) Buy Price. What *would* fix the R/R math is either a materially higher Sell Target (i.e., a more bullish fair-value read this session doesn't independently support) or the score improving into the 0.0–29.9 band (tighter, more favorable MoS/stop %). Neither applies today. **The correct reading of this framework's own rule is: pass on the trade, not "set a limit order and wait."**

**Position sizing, shown for completeness though moot given the R/R fail:** Portfolio value ≈$61,101.28 (per [holdings.md](../portfolio/holdings.md), 2026-08-23 sync). Max $ Risk (1.5%) ≈ $916.52. Not carried further — no order is being sized or placed.

---

## 7. Recommendation

# **WATCHLIST ONLY — do not enter. Composite Score (44.6) mechanically qualifies for "BUY — Standard position 3–5%," but the mandatory Risk/Reward gate fails (best case 1.71:1, requirement ≥2:1) across every combination of the prescribed Margin-of-Safety and Stop-Loss parameters. No position opened.**

This is not a marginal, close-call rejection at the scoring stage — Wise clears the Quality Gate (83.3, though see the moat-signal sensitivity in §2.8) on the strength of a genuinely strong underlying business: profitable, FCF-generative every year on record, net-cash balance sheet, and revenue still compounding at 20%+ even after five years of scale. The reasons **not** to enter today are specific and worth restating plainly:

1. **The R/R math fails on this session's own fair-value work**, independent of the Composite Score band (§6).
2. **A live, unresolved regulatory/legal risk cluster** sits directly on top of the position: an OCC national-trust-charter denial (2026-07-24, AML-control deficiencies cited), a Brussels criminal investigation into >€500M of flagged transactions at Wise's European entity (Reuters, 2026-06-01), and an active US securities-fraud class action with a 2026-09-29 lead-plaintiff deadline still open. None of this is resolved as of this session.
3. **A large, unreconciled valuation divergence** from sell-side consensus ($10.10 PW Fair Value here vs. $17.16 mean analyst target) — flagged explicitly (§4.3), not papered over, but real enough that a human reviewer should weigh it before treating either number as settled.
4. **Real, ongoing margin compression** (34.7% → 23.6% operating margin YoY) that management frames as deliberate reinvestment with FY27 stabilization guidance — plausible, but unproven, and this session's base-case DCF already gives management the benefit of guided margin stabilization (not full reversion to FY24 peak levels).

None of this is a case against the underlying business quality — it is a case against entering **at today's price, under today's unresolved regulatory overhang, with an R/R profile that doesn't clear this framework's own bar.**

**Next review trigger:** any of the following, per Rule 9 — (a) resolution (in either direction) of the OCC's national-trust-charter re-application, (b) any update on the Brussels Public Prosecutor's investigation, (c) the 2026-09-29 lead-plaintiff deadline and any subsequent securities-litigation development, (d) Wise's Q2 FY27 earnings (quarter ended 30 Sep 2026, expected ~November 2026) — specifically watch whether operating margin has begun stabilizing per FY27 guidance, and (e) the standard >15% unexplained price move / guidance revision / management change triggers.

---

## 8. Glossary

*(Pulled from [glossary.md](../framework/glossary.md); new terms added this session, marked below)*

| Term | Meaning |
|---|---|
| **Form 20-F** | The annual report US-listed foreign private issuers (non-US companies) file with the SEC — the international equivalent of a US company's Form 10-K. Wise Group plc (Jersey-incorporated) filed its FY2026 Form 20-F with the SEC on 2026-06-25, the primary source for this session's US-GAAP financial statements. |
| **Form 6-K** | A furnished report foreign private issuers file with the SEC to disclose material information between annual Form 20-F filings — roughly the international equivalent of a US company's Form 8-K. |
| **AML (Anti-Money Laundering)** | Laws and internal controls designed to stop criminal proceeds from moving through legitimate financial channels — the specific deficiency the OCC cited in denying Wise's national trust bank charter application, and the subject of the ongoing Brussels criminal investigation into Wise's European entity. |
| **Beta** | A stock's sensitivity to overall market moves — used as a CAPM input to estimate cost of equity for a DCF's WACC. Wise's beta (0.513, Yahoo Finance) implies low systematic risk historically, though this session used a higher WACC than a pure-CAPM output to reflect the currently-materializing regulatory risk a backward-looking beta doesn't capture. |
| **CAGR** | Compound Annual Growth Rate. |
| **Class A Ordinary Shares** | Wise Group plc's publicly-traded share class (ticker WSE on Nasdaq, WISE on the LSE secondary listing) — distinct from Class B shares, which carry enhanced voting rights and are held by Wise's founders, giving them outsized control relative to their economic ownership. *(New term.)* |
| **Customer float / Funds payable and amounts due to customers** | The segregated, safeguarded balance representing customer money in transit through Wise's platform — a large pass-through liability (and matching asset, mostly cash/AFS securities) on Wise's balance sheet that is not Wise's own economic capital. Distorts a naive reading of Wise's cash position, operating cash flow, and net debt if not explicitly excluded — this session builds an "own-funds" FCF and a no-cash-netting Net Debt convention specifically to handle this (see §2.9, §2.3). *(New term.)* |
| **DCF (Discounted Cash Flow)** | A valuation method that estimates a company's worth as the present value of its projected future free cash flows. |
| **EBIT / EBITDA** | Operating profit, before/also-before depreciation & amortization. |
| **Effective tax rate** | Tax provision ÷ pretax income for the period. |
| **FCF / FCF-NI conversion ratio** | Free Cash Flow; FCF ÷ Net Income, a cash-quality check on accounting profit. |
| **GENIUS Act** | The Guiding and Establishing National Innovation for U.S. Stablecoins Act, signed into law 2025-07-18 — US federal legislation creating a licensing/regulatory framework for USD-backed stablecoin issuers. Wise has stated it plans to reapply for a form of US banking access under this framework, viewing it as offering a clearer path than the national trust bank charter route the OCC denied. *(New term.)* |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of its weighted score. |
| **Invested Capital** | Debt + equity put to work in a business — this session's convention (no cash netting) follows the 2026-08-25 LLY session's precedent given Wise's customer-float-dominated balance sheet makes a clean "own cash" figure unavailable without estimation. |
| **Investment grade** | A credit rating (BBB-/Baa3 or higher) signaling low perceived default risk — Wise is rated BBB (stable) by both S&P and Fitch. |
| **Money-transmission license (MTL)** | A US state-level license authorizing a company to transmit money on customers' behalf — the license type Wise actually operates under across US states, distinct from (and unaffected by) the national bank/trust charter the OCC denied. Confirms the Telegram trigger's "US banking blocked" framing overstated what happened: Wise's existing US money-transfer operations continue under MTLs. *(New term.)* |
| **National trust bank charter** | A federal bank charter, granted and supervised by the OCC, that would let a company operate as a nationally-chartered trust institution rather than relying on a patchwork of state money-transmission licenses. The OCC denied Wise's application for this charter on 2026-07-24, citing AML-control deficiencies — the event underlying this session's trigger. *(New term.)* |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the ROIC numerator. |
| **OCC (Office of the Comptroller of the Currency)** | The US federal regulator that charters and supervises national banks and national trust companies — denied Wise's national trust bank charter application on 2026-07-24. |
| **PW (Probability-Weighted)** | The bull/base/bear scenario blend (25%/50%/25%) used to compute a single Fair Value estimate. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02 valuation scoring. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0** | Always fetch a live price first — never infer from multiples or stale data. |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **Scheme of arrangement** | A UK/Jersey-law court-approved procedure restructuring shareholders' rights with a binding class vote — the mechanism Wise used to move its primary listing from the LSE to Nasdaq (effective 2026-05-08). |
| **Take rate** | The percentage of gross transaction value a platform keeps as revenue — Wise's blended cross-border take rate has fallen from 0.67% (FY24) to 0.52% (FY26), central to the "brand premium" Moat Signal finding in §2.8. |
| **TTM (Trailing Twelve Months)** | The most recent four reported quarters combined; this session used FY2026 (Wise's most recent complete fiscal year) rather than a reconstructed TTM, flagged in §2.4. |
| **UFCF (Underlying Free Cash Flow)** | Wise's own (apparently discontinued in the FY2026 US-GAAP presentation) non-GAAP free cash flow metric, disclosed for FY2023–FY2025. Used in §2.9 as a directional cross-check against this session's own "own-funds FCF" construction. *(New term.)* |
| **Underlying basis (Wise)** | Wise's pre-FY2026 non-GAAP IFRS reporting framework (Underlying income, Underlying gross profit, Underlying operating profit, Underlying profit before tax) that excluded interest income above the first 1% customer-balance yield. Not present in the FY2026 US-GAAP filing — a genuine reporting-regime discontinuity flagged throughout §2. *(New term.)* |
| **WACC** | Weighted Average Cost of Capital — the discount rate used in a DCF. |
| **WPLCF** | Wise's former, unsponsored US OTC ADR ticker — **superseded** since Wise's ordinary shares began trading directly on Nasdaq under **WSE** on 2026-05-11. This session's brief assumed WPLCF was still current; it is not, and WSE was used throughout instead. *(New term.)* |

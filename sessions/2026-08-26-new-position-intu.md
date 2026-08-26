# NEW POSITION — INTU (Intuit Inc.) — post-earnings re-evaluation

**Task type:** NEW POSITION (post-earnings; INTU is not currently held)
**Date:** 2026-08-26
**10Y US Treasury Yield:** 4.66% (TradingEconomics, 2026-08-26 print — same level cited in this framework's 2026-08-25 LLY session).

**Trigger:** Automated Telegram-scan (Routine 6) flagged a post today (`FinnInvestChannel`) referring to "Intuit's weak report," about Intuit's Q4/FY2026 earnings (reported 2026-08-25). **Per Rule 0 and this framework's standing rule, the Telegram post's text is not used as data anywhere below** — it is only the signal to check whether a mandatory Rule 9 re-valuation is overdue. It is: Intuit reported Q4/full-year FY2026 results after market close on 2026-08-25, and per the explicit "Next Review Trigger" flagged in both prior INTU files — [2026-08-23 new-position session](2026-08-23-new-position-intu.md) and the [2026-08-24 rescore deferral](2026-08-24-rescore-intu.md) — this earnings release is a mandatory, already-due Rule 9 re-valuation that had not yet been run. This session is that re-valuation, independently sourced from SEC filings, Intuit's own IR press release, and live market data — not from the triggering post.

**Bottom line up front (flagged here, derived in full below):** the Telegram characterization ("weak report") doesn't match the primary-source numbers — Q4 revenue and EPS both **beat** consensus — but the stock still sold off sharply because FY2027 guidance calls for a real, company-wide growth deceleration (14% → 9–10%) that management frames as a deliberate strategic reset, not a beat/miss story. Both things are true simultaneously, and both are carried through explicitly below.

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

IBKR `get_price_snapshot` (contract_id 270662, NASDAQ, resolved and verified in the 2026-08-23 session):

| Field | Value |
|---|---|
| **Last trade price** | **$348.40** |
| Change vs. prior close | −$9.06 (−2.53%) |
| Prior close (reconciled) | $357.46 (348.40 + 9.06 — independently cross-checked against a live web search citing "previous close of $357.46," which matches exactly) |
| 52-week high / low | $700.30 / $252.84 |
| 13-week high / low | $372.98 / $252.84 |
| 26-week high | $481.70 |
| Bid/Ask | $348.01 / $349.57 |
| Dividend yield (live) | 1.34% |

**Live Price used throughout this session: $348.40.** Not inferred from any multiple — fetched directly. Down 5.19% from the 2026-08-23 session's $367.50 and now trading through the prior 13-week low/high band that had been forming just under $370 — the post-earnings move (see §2) is what broke that sideways range. Note the stock's first reaction to the 2026-08-25 after-hours print was sharper still (briefly down ~10–11% after-hours per Rule-0-independent news coverage cited in §2) before settling to today's −2.53% intraday move off the (already-lower) 2026-08-25 regular-session close.

**Analyst PT context (Rule 0 Step 4, bull-case sanity check):** consensus 12-month price target **$425.78** (stockanalysis.com, 35 analysts, post-earnings), a separate source's average **$444.50** — both used only as a sanity check against §5's independently-derived fair value, never as an input.

---

## 2. Q4 & Full-Year FY2026 Earnings — primary sources only

Intuit's fiscal year runs 1 August–31 July; **FY2026 (ended 31 July 2026) is now the latest complete audited fiscal year**, reported via 8-K on 2026-08-25. Sourced directly from the SEC 8-K exhibit (Intuit's own earnings press release, financial statement tables) — [sec.gov 8-K filing](https://www.sec.gov/Archives/edgar/data/0000896878/000089687826000029/fy26q4earningspressrelease.htm) — not from any secondary aggregator for the headline GAAP figures.

### Q4 FY2026 results (quarter ended 31 July 2026)

| Metric | Value | YoY |
|---|---|---|
| Total revenue | $4.4B | +14% |
| Non-GAAP diluted EPS | $4.03 | +47% (beat consensus $3.59) |
| Revenue vs. consensus | beat ($4.4B vs. ~$4.27B consensus) | — |

**Segment revenue (Q4):**

| Segment | Revenue | YoY |
|---|---|---|
| Global Business Solutions (GBS) | $3.4B | +14% |
| — QuickBooks Online Accounting | (component of GBS) | +20% |
| — Online Services (ex-Mailchimp) | (component of GBS) | +21% |
| Consumer | $930M | +14% |
| — TurboTax | $153M | +3% |
| — Credit Karma | $743M | +16% |
| — ProTax | $34M | +6% |
| Online Ecosystem (company's own cross-segment grouping) | $2.6B | +17% |

### Full-year FY2026 results (12 months ended 31 July 2026) — from Table A/B1/B2 of the 8-K

| Metric | FY2026 | FY2025 | YoY |
|---|---|---|---|
| Total net revenue | $21,448M | $18,831M | +13.90% |
| **GAAP operating income** | **$5,884M** | **$4,923M** | +19.5% |
| Non-GAAP operating income | $8,935M | — | — |
| GAAP net income | $4,566M | $3,869M | +18.0% |
| Non-GAAP net income | $6,732M | — | — |
| GAAP diluted EPS | $16.46 | $13.67 | +20.4% |
| Non-GAAP diluted EPS | $24.27 | — | +20% |

**Data-quality flag (Rule 0/4):** stockanalysis.com's income-statement page independently pulled shows FY2026 "Operating Income" as **$6,177M**, which does not reconcile with the SEC 8-K's own stated **$5,884M** GAAP figure (a ~5% gap). Per this framework's "never invent, verify against the primary source" discipline, **the SEC 8-K figure ($5,884M) is used throughout this session** wherever GAAP EBIT enters a calculation (EV/EBIT, EBITDA, Net Debt/EBITDA) — stockanalysis.com is used only for the historical (FY2022–2025) trend context and the 5-year PE series, where no primary-source discrepancy was found. GAAP net income ($4,566M) and revenue ($21,448M) *do* reconcile exactly between the two sources, so only the operating-income line is affected.

### FY2027 guidance (the actual driver of the post-earnings selloff)

| Metric | FY2027 guide | vs. FY2026 actual |
|---|---|---|
| Revenue | $23.28–23.51B | +9–10% (down from +14%) |
| GAAP diluted EPS | $20.12–20.36 | +22–24% |
| Non-GAAP diluted EPS | $22.88–23.12 | +23–24% |
| GBS segment growth | +13–14% | ≈ flat vs. FY2026's +14% |
| Consumer (TurboTax) growth | +2–3% | ≈ flat vs. Q4's +3% |
| Credit Karma growth | +11–13% | down from Q4's +16% |

**Other disclosed items, cited but not scored (per "Why Forward Guidance Is Not a Sub-score," valuation-scoring.md):**
- Full-year stock repurchases: $5.5B (+96% YoY); this **more than offset** dilution from stock-based compensation, producing a **net 2% reduction in weighted-average diluted shares outstanding** for FY2026 (company's own disclosed figure — used directly in §5.5's shareholder-yield calc rather than a gross-buyback-÷-market-cap estimate).
- Dividend raised 15% to $1.38/share (quarterly).
- Q4 restructuring charge: $293M (a GAAP-only, non-recurring item; already embedded in the $5,884M GAAP operating income figure used above — not separately added back, consistent with scoring off reported GAAP).
- Total online paying customers grew 3% YoY to 8.9M — roughly 2 points slower than the prior year's pace. TurboTax units fell 2% YoY to 39.0M.
- "Big Bets" (QuickBooks Online Advanced + Intuit Enterprise Suite mid-market bundle, assisted tax, money-services products) grew 34% and now represent 30% of total revenue. Combined QBO Advanced + Intuit Enterprise Suite customer count grew 28% YoY.
- Mailchimp: Q4 revenue down slightly YoY; becomes its own separate reportable segment starting FY2027 (a reporting-structure change to note for the next re-score, not itself a valuation input).
- QuickBooks Online list prices raised again effective 1 August 2026 — Essentials $75→$85, Plus $115→$140 (some sources cite the effective increase reaching 41% once bundled add-ons are included), Advanced $275→$340 — a materially steeper round of increases than the prior year's.
- Management's own framing (CEO Sasan Goodarzi, earnings call): the FY2027 deceleration is **deliberate** — trading near-term revenue-per-customer for faster customer/volume growth, particularly in TurboTax, where "price is now the top reason customers leave." *"We are creating the pressure. We are not being pressured to make the change."*
- Guide-down attributed by coverage to three factors: sluggish TurboTax customer growth, continued generative-AI tax-prep competition, and softer Mailchimp/desktop trends.

[SEC 8-K / earnings press release](https://www.sec.gov/Archives/edgar/data/0000896878/000089687826000029/fy26q4earningspressrelease.htm) · [TIKR: "the cost of winning back TurboTax customers"](https://www.tikr.com/blog/what-intuits-q4-earnings-call-reveals-about-the-cost-of-winning-back-turbotax-customers) · [TradingKey: "Intuit Tumbles 11% Pre-Market"](https://www.tradingkey.com/analysis/stocks/us-stocks/262133075-intu-intuit-q4-mailchimp-turbotax-tradingkey)

---

## 3. Phase 01 Quality Score

Per [quality-scoring.md](../framework/quality-scoring.md) (methodology version 2026-06-29, unchanged). **TTM = FY2026** (the fiscal year that just closed 31 July 2026 — the rolling TTM window now includes the just-reported Q4).

### Updated raw financial data (FY2022–FY2026)

| Metric | FY2022 | FY2023 | FY2024 | FY2025 | **FY2026 (TTM)** |
|---|---|---|---|---|---|
| Revenue | $12,726M | $14,368M | $16,285M | $18,831M | **$21,448M** |
| Revenue growth | 32.11% | 12.90% | 13.34% | 15.63% | **13.90%** |
| Gross Profit / Margin | $10,460M / 82.19% | $11,388M / 79.26% | $12,966M / 79.62% | $15,139M / 80.39% | **$17,369M / 80.98%** |
| GAAP Operating Income (EBIT) | — | — | — | $4,923M (8-K) | **$5,884M (8-K)** |
| Net Income / Margin | $2,066M / 16.23% | $2,384M / 16.59% | $2,963M / 18.20% | $3,869M / 20.55% | **$4,566M / 21.29%** |
| Diluted EPS (GAAP) | $7.28 | $8.42 | $10.43 | $13.67 | **$16.46** |
| EPS growth YoY | −3.70% | +15.66% | +23.87% | +31.06% | **+20.41%** |
| Operating Cash Flow | $3,889M | $5,046M | $4,884M | $6,207M | **$8,838M** |
| CapEx | −$157M | −$210M | −$191M | −$84M | **−$221M** |
| Free Cash Flow | $3,732M | $4,836M | $4,693M | $6,123M | **$8,617M** |
| FCF/NI conversion | 180.6% | 202.9% | 158.4% | 158.3% | **188.7%** |

*(FY2022–2025 figures per stockanalysis.com, unchanged from the 2026-08-23 session; FY2026 revenue/net income/EPS/FCF figures reconciled against the SEC 8-K, GAAP EBIT taken from the 8-K directly per the §2 data-quality flag.)*

**Balance sheet (as of 31 July 2026, stockanalysis.com, cross-checked internally below):** Total Debt $8,336M, Cash & Short-Term Investments $7,200M, **Net Debt = $1,136M**, Total Equity $18,992M, Total Assets $36,786M.

**Statistics (stockanalysis.com):** ROE 23.60%, ROIC 22.93%, ROA 10.47%, Debt/Equity 0.44 (= 8,336/18,992 = 0.439, reconciles), Current Ratio 1.51, Shares Outstanding 273.54M.

**Internal cross-checks (not invented):**
- Market Cap (live) = 273.54M × $348.40 = **$95,301.3M**. EV (live) = 95,301.3 + 1,136 = **$96,437.3M**.
- D&A (FY2026, stockanalysis.com cash-flow statement) = $846M → **EBITDA = GAAP EBIT ($5,884M) + D&A ($846M) = $6,730M**.
- Net Debt/EBITDA = $1,136M / $6,730M = **0.1688×**.
- EV/EBITDA (live) = 96,437.3/6,730 = 14.33× — reasonably close to stockanalysis.com's own (stale-priced, pre-earnings-consistent) 13.55× stat, cross-check passes within the expected price-timing gap.

**Hard disqualifier check (rolling window, per quality-scoring.md's 2026-08-05 clarification):**
- FCF/NI conversion <70% for 2+ consecutive years: **No** — every year FY2022–FY2026 is 158%–203%.
- Net Debt/EBITDA over threshold (2.5× standard): **No** — 0.169×, far under.
- Not FCF-positive for 3+ consecutive years: **No** — FCF positive and growing every year shown.

**No hard disqualifier fires.**

### 3a. Profitability (25% weight)

```
NetMargin_Component = clamp((21.29/30)×100, 0, 100) = 70.97   (TTM = FY2026 net margin)
ROIC_Component       = clamp((22.93/30)×100, 0, 100) = 76.43
Profitability_Score  = (70.97 + 76.43) / 2 = 73.70   (no FCF cap — FCF-positive every year shown)
```

### 3b. Margins (15% weight)

```
GrossMargin_Score = clamp((80.98/80)×100, 0, 100) = 100.0   (clamped)
```
Gross margin drifted down slightly from FY2022's 82.19% peak to 80.98% — not a structural expansion (moot regardless, already clamped).

### 3c. Growth (20% weight) — the most consequential judgment call this session

```
Revenue 3yr CAGR (FY2023 $14,368M → FY2026 $21,448M) = (21,448/14,368)^(1/3) − 1 = 14.29%
Growth_Score (base) = clamp((14.29/25)×100, 0, 100) = 57.15
```

**This is the swing input relative to the 2026-08-23 session, because the underlying facts genuinely changed.** The prior session applied a clean +10 TAM-expansion modifier (consolidated growth was accelerating, not decelerating). Post-earnings, **both** conditions in quality-scoring.md's modifier are now independently, concretely documented — not a repeat of the same call:

**For the +10 TAM-expansion/pricing-power modifier — evidence unchanged or strengthened:**
- "Big Bets" (mid-market QBO Advanced + Intuit Enterprise Suite, assisted tax, money-services) grew **34%** and now represent **30% of total revenue** (§2) — genuine, ongoing TAM expansion beyond the traditional small-business base, a company-disclosed figure, not inferred.
- Combined QBO Advanced + Intuit Enterprise Suite **customer count** grew **28% YoY** — volume growth, not just pricing.

**For the −10 structural-deceleration penalty — now fires, and at the consolidated level (it explicitly did *not* in the 08-23 session):**
- FY2027 **guided, company-wide** revenue growth is **9–10%**, down from FY2026's actual **13.90%** — a guided, quantified, forward deceleration spanning the *entire* company, not one segment. Every reporting segment's FY2027 guide is flat-to-down versus its FY2026 actual (GBS ≈ flat, Consumer ≈ flat, **Credit Karma down** from +16% to +11–13%) — this is no longer the "TurboTax-only, doesn't apply at the consolidated level" pattern the 08-23 session correctly declined to penalize.
- Management's own framing ("we are creating the pressure") makes this an explicit, deliberate, multi-quarter guided reset — not a one-quarter cyclical miss, which is the bar quality-scoring.md sets for this penalty to apply.

**Judgment applied:** both conditions are independently true, concretely quantified, and separately cited — quality-scoring.md's wording ("adds +10... subtracts −10... and/or") does not instruct picking one narrative over the other when both are genuinely documented. Applying **both** and showing the net arithmetic is the least cherry-picked treatment, and is shown as the primary reading; the sensitivity table below (§3h) shows what happens under each single-modifier alternative instead, exactly as the 08-23 session did for its own swing input.

```
Growth_Score = 57.15 + 10 (TAM/Big Bets) − 10 (guided consolidated deceleration) = 57.15   (net zero)
```

### 3d. Balance Sheet (15% weight)

```
BalanceSheet_Score = clamp(100 × (1 − 0.1688/4), 0, 100) = 100 × 0.9578 = 95.78
```
No asset-light override needed — still far under even the standard 2.5× threshold.

### 3e. Moat Signal (15% weight) — the Brand-premium swing signal, revisited with new post-earnings evidence

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | QuickBooks still holds an estimated ~80% US small-business-accounting-software share (AceCloudHosting, 2026 data); Xero remains the main international challenger but has not displaced QuickBooks domestically — same evidence basis as 08-23, unaffected by earnings. |
| Brand premium | **TRUE** (see caveat) | **Stronger, more dramatic pricing evidence than 08-23:** QuickBooks Online list prices raised again effective 1 Aug 2026 — Plus +22% headline (some effective-price estimates reaching 41% once add-ons compound), Advanced +24% — while GBS/QBO Online Accounting revenue still grew +20%/+14% respectively in the same quarter and US QBO customer count kept growing. Price increases *with* continued volume/customer growth in the segment carrying ~77% of Q4 revenue is a direct match to the signal's definition. **Explicit counter-evidence, more starkly disclosed this quarter than before:** management and coverage now state plainly that "**price is now the top reason customers leave TurboTax**" — not an inference this time, a direct, quoted finding — and management is *lowering* TurboTax's average revenue per customer specifically to win volume back. |
| Network effect | **TRUE** | Unaffected by earnings — QuickBooks Online App Store (2.5M+ users, third-party integrations) and Credit Karma's two-sided marketplace (100+ financial-service partners), same mechanism as 08-23. |
| Switching costs | **TRUE** | Unaffected by earnings — multi-party lock-in (business + accountant + integrations all on QuickBooks Online), same mechanism as 08-23. |
| Scale cost advantage | **FALSE** | Still no cost-per-unit citation vs. smaller competitors — not marked true without one. |

```
Moat_Score = (4/5) × 100 = 80.0
```

**This remains the single most decisive, judgment-dependent input, now with sharper evidence on *both* sides of the same tension flagged in the 08-23 session.** The QBO pricing-power evidence is more dramatic this quarter (steeper list-price hikes, still absorbed with continued growth); the TurboTax counter-evidence is now an explicit, quoted finding rather than an inference from a guidance-cut headline. I score Brand premium **TRUE** on the strength of the (larger-revenue, more dramatically-priced) QBO evidence — the same call as 08-23, on a comparably strong basis — but this is flagged with maximum transparency, and the sensitivity table below shows the gate result if a stricter reader marks it FALSE.

### 3f. FCF Quality (10% weight)

```
FCF/NI (TTM = FY2026) = $8,617M / $4,566M = 188.72%
FCFQuality_Score = clamp(((1.8872 − 0.40)/0.60)×100, 0, 100) = clamp(248.0, 0, 100) = 100.0   (capped)
```

### 3g. Full Quality Score — primary computation

```
Quality Score = (73.70×0.25) + (100.0×0.15) + (57.15×0.20) + (95.78×0.15) + (80.0×0.15) + (100.0×0.10)
              = 18.425 + 15.000 + 11.430 + 14.367 + 12.000 + 10.000
              = 81.222
              → rounds to 81.2
```

### 3h. Sensitivity table — same discipline as the 08-23 session, now a 2-factor grid

| Scenario | Moat_Score | Growth modifier | Quality Score | Gate result |
|---|---|---|---|---|
| **Primary (as scored above)** | 80.0 (4/5) | net 0 (+10 −10) | **81.2** | **PASS** (+1.2) |
| Conservative Moat (Brand premium → FALSE) | 60.0 (3/5) | net 0 | **78.2** | **FAIL** (−1.8) |
| Growth: deceleration only (−10, no TAM offset) | 80.0 (4/5) | −10 only | **79.2** | **FAIL** (−0.8) |
| Both conservative (Moat FALSE + decel-only) | 60.0 (3/5) | −10 only | **76.2** | **FAIL** (−3.8) |
| Growth: TAM only (+10, no deceleration penalty) | 80.0 (4/5) | +10 only | **83.2** | PASS (+3.2) |

**This is a narrower pass than the 08-23 session's (81.2 vs. 80.0 floor, +1.2 cushion, down from +2.8 pre-earnings).** Three of five plausible readings in the table fail the gate. The primary reading (Moat TRUE, Growth net-zero) is the one I stand behind for the reasons shown in §3e/§3c — but this is explicitly flagged as the top-priority item for the next re-score, exactly as the equivalent flag was carried in the 08-23 session.

### Gate Result: ✅ **PASS** (81.2 ≥ 80.0, narrow) — proceeding to Phase 02.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test** (Forward PE computed in §5.2 below — shown here since Step 1 needs it):
```
Forward PE = 15.15× (live price ÷ FY2027 non-GAAP EPS guidance midpoint — see §5.2 for why this basis is used)
EY = 1 / 15.15 = 6.60%
Spread = EY − 10Y = 6.60% − 4.66% = 1.94%
```
Spread ≥ +1.5% → **passes Step 1, no additive flag.**

**Step 2 — Rate Regime Modifier:** 10Y = 4.66% falls in the 3.5–5% bracket → **+5.**

**Combined Rate Modifier = +5.**

---

## 5. Phase 02 — Valuation Score

### 5.1 PEG eligibility (Fast Grower check — rolling window)

EPS growth over the last 3 consecutive complete fiscal years (rolling forward by one year from the 08-23 session): FY2024 +23.87%, FY2025 +31.06%, FY2026 +20.41% — all >15%, on a clean, non-distorted GAAP earnings base (no one-off gains, no recent IPO). **Still qualifies as a Fast Grower — PEG applies at 15% weight.**

### 5.2 A required data-quality flag before computing Forward PE — the stale-consensus problem

The first analyst-consensus FY2027 EPS figure surfaced (via aggregator search, "$27.30") was **essentially unchanged from the pre-earnings figure cited in the 2026-08-23 session ($27.28)** — despite FY2026 actuals, a guidance cut, and a >10% stock move having intervened. That is a strong signal the figure is stale/uncached rather than freshly revised. Independently cross-checked: a separate, dated source explicitly states **"Intuit sees FY2027 EPS of $22.88–$23.12 versus the analyst consensus of $23.83"** (i.e. the *pre-earnings* consensus was $23.83, not $27+) — confirming the $27.30 figure was not the correct pre- or post-print consensus for FY2027 non-GAAP EPS.

**Resolution: this session uses Intuit's own FY2027 non-GAAP EPS guidance midpoint — $23.00 (= (22.88+23.12)/2)** — for every calculation below that needs a forward EPS (Forward PE, PEG, multiples-based fair value). This is a directly disclosed, primary-source figure (not invented or estimated), and — per the Rule 4 sanity check the 08-05 pre-earnings consensus ($23.83) sat just above it — a defensibly conservative-to-neutral choice, not a cherry-picked low number.

### 5.3 Sub-score inputs

```
FCF Yield = FCF(TTM) / Market Cap(live) = $8,617M / $95,301.3M = 9.042%
EV/EBIT (live, GAAP EBIT per §2/§3 data-quality flag) = $96,437.3M / $5,884M = 16.390×
Forward PE = Live Price / FY2027 guidance-midpoint EPS = $348.40 / $23.00 = 15.148×
5yr PE (proxy — same FY-end-snapshot caveat as 08-23): FY2022–FY2026 fiscal-year-end PE
  = 62.28× / 60.11× / 61.08× / 56.61× / 21.01×  (stockanalysis.com "financials/ratios")
  → Avg = 52.22×, Low = 21.01×, High = 62.28×   (FY2026's 21.01× reflects the ~$345.8 price at
     31 July 2026 — the last trading day *before* the 25 Aug earnings report and its selloff, not
     today's live price)
PEG = Forward PE / long-term EPS growth estimate = 15.148 / 14.3% = 1.059
  (14.3%/yr — Simply Wall St's multi-year smoothed EPS-growth consensus, same source/figure basis as
  the 08-23 session; deliberately not the FY2027-guided +23–24% spike, which is inflated by this
  year's unusually large buyback and isn't representative of a normalized multi-year rate)
```

**Caveat on the 5yr PE range (unchanged from 08-23):** five annual fiscal-year-end snapshots, not a true reconstructed intra-year range — treated as the **Fallback (average-only) formula**.

### 5.4 Sub-scores

```
FCF_Score      = clamp(100×(1 − 9.042/10), 0, 100) = 9.58
EV/EBIT_Score  = clamp((16.390 − 12)/23×100, 0, 100) = 19.09
FwdPE_Score    = Deviation% = (15.148 − 52.22)/52.22×100 = −70.99%
               = clamp(50 + (−70.99×2.5), 0, 100) = clamp(50 − 177.5, 0, 100) = 0.0
PEG_Score      = clamp((1.059 − 0.5)/2.0×100, 0, 100) = 27.96

Raw weighted = (9.58×0.40) + (19.09×0.25) + (0.0×0.20) + (27.96×0.15)
             = 3.833 + 4.772 + 0.000 + 4.194
             = 12.80
```

**Note on the FwdPE_Score = 0.0 extreme (same structural flag as 08-23, still applies):** INTU's 56–70× multiples through FY2022–2025 were a rich, high-growth-SaaS-era band; today's 15.1× forward multiple reflects both the AI-disruption-driven de-rating and real earnings growth. Comparing today's multiple to that old average is as much a statement about a sector-wide structural re-rating as about INTU specifically — shown transparently, no discretionary override exists in the framework for this case.

### 5.5 Fair Value (Rule 7 — scenario analysis, bull/base/bear) — rebuilt post-earnings

**Method A — 3-stage DCF** (Rule 2: unlevered FCF via the FCF-margin route, base year = FY2026 actuals; WACC = Rf + β×ERP = 4.66% + 0.96×5.0% ≈ 9.46% base, ±1% per scenario; terminal growth ≤3% per Rule 2's GDP cap). Growth/margin paths explicitly rebuilt to reflect the FY2027 guided deceleration (§2) rather than reused from 08-23:

| | Bull (WACC 8.46%, term. g 3.0%) | Base (WACC 9.46%, term. g 2.5%) | Bear (WACC 10.46%, term. g 2.0%) |
|---|---|---|---|
| Rev growth Y1→Y5 | 10%→12% (guide top end, reaccelerating as reset succeeds) | 9.5%→7.5% (guide midpoint, gradual fade) | 8%→4% (guide low end, deceleration proves structural) |
| FCF margin Y1→Y5 | 39%→41% | 38%→39% | 34%→28% |
| Y5 Revenue | $36,137.5M | $32,247.0M | $28,420.7M |
| Y5 FCF | $14,816.4M | $12,576.3M | $7,957.8M |
| Terminal Value | $279,502.7M | $185,211.8M | $95,945.2M |
| PV(FCFs) + PV(TV) | $45,624.5M + $186,225.0M | $40,579.8M + $117,866.8M | $29,941.5M + $58,344.2M |
| Enterprise Value | $231,849.5M | $158,446.6M | $88,285.7M |
| Equity Value (− net debt $1,136M) | $230,713.5M | $157,310.6M | $87,149.7M |
| **DCF FV/share** (÷273.54M shares) | **$843.44** | **$575.09** | **$318.60** |

*Sanity checks (Rule 4):* Bear-case FV ($318.60) sits above the actual 52-week low ($252.84) — the market's most pessimistic moment priced in something worse than this bear case, consistent with a panic/overshoot read rather than this bear case being too lenient. Bull-case implied terminal FCF multiple = $279,502.7M/$14,816.4M = 18.9× — not an unreasonable exit multiple for a wide-moat software franchise.

**Method B — Peer comparable multiples** (Rule 5: 5 peers, median not mean; refreshed live, 2026-08-26): ADP 25.9×, PAYX 15.85×, WDAY 17.81×, MSCI 27.91×, HRB 6.80× forward PE → **median = 17.81× (WDAY)** — down from 08-23's 20.81× median, reflecting the broader software-multiple compression over the past few trading days.

```
Base:  FY2027 guidance-midpoint EPS $23.00 × peer median 17.81×          = $409.63
Bull:  $23.00 × highest-quality peer multiple (MSCI 27.91×)               = $641.93
Bear:  $23.00 × lowest peer multiple (HRB 6.80× — "market re-rates INTU
       to a legacy tax-software multiple despite unchanged EPS")          = $156.40
```
*(Historical-PE cross-check excluded from the blend for the same Rule 4 multiple-sanity reason as 08-23 — 5yr avg PE 52.22× reflects a structurally different rate/growth regime.)*

**Blended FV per scenario** (40% DCF + 60% Multiples):

```
Bull:  0.40×843.44 + 0.60×641.93 = 337.38 + 385.16 = $722.53
Base:  0.40×575.09 + 0.60×409.63 = 230.04 + 245.78 = $475.81
Bear:  0.40×318.60 + 0.60×156.40 = 127.44 +  93.84 = $221.28

PW Blended Fair Value = 0.25×722.53 + 0.50×475.81 + 0.25×221.28 = 180.63 + 237.91 + 55.32 = $473.86
```

**Base-Case Blended Fair Value (for order setup) = $475.81. PW Blended Fair Value (for the modifier below) = $473.86.**

*(For comparison: 08-23's Base-Case FV was $551.91. The ~14% drop is driven almost entirely by the corrected, lower EPS basis used post-earnings — $23.00 guidance midpoint vs. the stale $27.28/27.30 pre-earnings consensus figure both sessions' multiples-based leg depends on — not by any change to the DCF leg, which is actually slightly higher than 08-23's despite the more conservative growth path, because the FY2026 actual base year is materially larger than the FY2025 base year 08-23 started from.)*

### 5.6 Upside/Downside Modifier

```
Gap Upside % = (PW FV / Live Price) − 1 = (473.86 / 348.40) − 1 = +36.01%

Catalyst & timeline (Rule 10): unchanged 18-month window from 08-23 — the next 2-3 quarterly prints,
  spanning FY2027 execution proof-points (does the deliberate reset reaccelerate customer growth) and
  the full Jan–Apr 2027 tax season (reported ~May 2027). Catalyst window = 18 months.
Annualized gap = 36.01% / 1.5yr = 24.01%/yr

Intrinsic growth rate = 14.3%/yr (same Simply Wall St multi-year estimate as §5.3's PEG denominator)

Shareholder yield = dividend yield 1.34% (IBKR, live) + net buyback yield 2.0% (Intuit's own disclosed
  FY2026 figure — "share repurchases... drove a 2% reduction in weighted-average diluted shares
  outstanding," §2 — used directly rather than a gross-$-buyback-over-market-cap estimate, a more
  precise, already-net figure than the 08-23 session had available) = 3.34%

E = 24.01% + 14.30% + 3.34% = 41.65%/yr
```

`E` ≥ H(10%) → strong-upside band:
```
M = −15 × clamp((41.65−10)/15, 0, 1) = −15 × clamp(2.11, 0, 1) = −15 × 1.0 = −15.0
```

**Guardrail/sanity flag (shown, not hidden — same posture as 08-23):** E = 41.65%/yr again fully saturates the ±15 cap well past the +25%/yr threshold where the clamp binds regardless of the exact figure. Catalyst exists within the 18–24mo guardrail window, so no additional cap applies. This is the same "forecast informs but never overrides" mechanism working as designed.

**Upside/Downside Modifier = −15.0** (maximum attractive).

### 5.7 Final Valuation Score

```
Final Score = 12.80 (raw weighted, §5.4) + 5 (Rate Modifier, §4) + (−15.0) (Upside/Downside Modifier, §5.6)
            = 2.80 → rounds to 2.8
```

**Valuation Score = 2.8** — within the 0.0–29.9 "Very Cheap" band. Slightly higher (less extreme) than 08-23's 8.7 → 2.8 is actually *lower*/cheaper — the corrected GAAP EBIT figure ($5,884M vs. the erroneous $6,177M) pulls EV/EBIT_Score up a little, but the sharply higher FCF Yield (9.04% vs. 7.71%) and continued PEG<1 more than offset it. **Mechanically, the stock is cheaper on this framework's multiples today than it was pre-earnings, despite the "weak report" framing — real revenue/EPS/FCF growth outpaced the ~5% price decline.**

---

## 6. Composite Score

```
Composite Score = 0.50×(100 − Quality Score) + 0.50×Valuation Score
                = 0.50×(100 − 81.2) + 0.50×2.8
                = 0.50×18.8 + 0.50×2.8
                = 9.40 + 1.40
                = 10.80 → rounds to 10.8
```

**Composite Score = 10.8** → per the Composite/Phase 03 Action Table: **Score 0.0–29.9 → BUY — Full position 6–8%** (nominal — see §7 for why the actual order-setup gate does not support entry).

*(Sensitivity carried from §3h: if the Moat brand-premium call, or the growth-modifier treatment, had gone a stricter way, Quality Score falls to 76.2–79.2 and the gate fails outright — the entire Composite/order-setup section below would not exist under those readings.)*

---

## 7. Fair Value + Order Setup — computed per the operating brief, but see the R/R finding below

**MoS / Max-Loss band for Composite Score 10.8 (the 0.0–29.9 tier): MoS 15–20%, Max Acceptable Loss 20–25%.**

### 7.1 Entry-price reading (same convention as 08-23, applied consistently)

Live Price ($348.40) is below the Buy-Price ceiling computed from Fair Value × (1−MoS) — at 20% MoS, $475.81 × 0.80 = $380.65; at 15% MoS, $404.44. This is again the **"Score 0.0–29.9 → Stock at or below buy price → Enter now"** case, not "Set limit order." Following the 08-23 session's established, explicitly-reasoned convention for this exact situation, **Entry Price = Live Price ($348.40)** — the price an actual order placed today would fill at, not a ceiling nobody would pay.

Live Price implies **26.77% below Base-Case Fair Value** (1 − 348.40/475.81) — comfortably exceeds the 15–20% MoS floor for this tier on its own terms.

### 7.2 Risk/Reward Ratio — checked across the full Max-Loss range, and it fails

```
Numerator (Primary Sell Target − Entry) = 475.81 − 348.40 = 127.41

Stop @ 20% loss: 348.40×0.80 = $278.72 → R/R = 127.41/(348.40−278.72) = 127.41/69.68  = 1.829:1
Stop @ 22% loss: 348.40×0.78 = $271.75 → R/R = 127.41/(348.40−271.75) = 127.41/76.65  = 1.662:1
Stop @ 25% loss: 348.40×0.75 = $261.30 → R/R = 127.41/(348.40−261.30) = 127.41/87.10  = 1.463:1
```

**Every Max-Loss value allowed for this score band (20–25%) produces a base-case R/R between 1.46:1 and 1.83:1 — below the 2:1 minimum across the entire range.** Solving algebraically for the loss% that would exactly hit 2:1 gives ≈18.28% — tighter than even the most conservative (lowest-loss) end of the 20–25% band this score tier allows, so no valid stop within the framework's own rules for this tier clears the gate. This is the same failure mode, and the same resolution, as the 2026-08-13 SNDK session (`sessions/2026-08-13-new-position-sndk.md`): a Composite Score that nominally lands in the Buy band, blocked by an independent Risk/Reward gate.

**Why this happened, in one line:** the stock fell ~5% since 08-23, but the corrected, primary-source-grounded Sell Target (Base-Case Blended FV) fell further (~14%, mostly from replacing a stale $27+ consensus EPS with Intuit's own $23.00 guidance midpoint, §5.2) — so the achievable reward shrank faster than the achievable risk did.

*(For completeness, the Bull-Case Trim Target R/R clears easily — 0.40×843.44+0.60×641.93=722.53 → ×0.90 = $650.28 trim target → R/R @20% stop = (650.28−348.40)/69.68 = 4.33:1 — but per this framework's convention (established in the 08-23 and SNDK sessions), the **Primary** Sell Target is the gating figure, not the Bull-Case Trim Target.)*

### 7.3 Order setup checklist — shown in full per "no black-box outputs," even though it fails the gate

```
[x] Composite Score (nominal action band):        10.8   (0.0–29.9 → Full-position entry, nominally)
[x] Raw Valuation Score (incl. Upside/Downside):  2.8
[x] Expected annual return E / catalyst window:   +41.65% / 1.5yr
[x] Upside/Downside Modifier applied:             −15.0
[x] Base-Case Blended Fair Value:                 $475.81
[x] PW Blended Fair Value (for E, above):         $473.86
[x] Implied discount to Fair Value at live price: 26.77% (exceeds the 15–20% MoS floor for this tier)
[x] ENTRY PRICE (live, would-be "enter now"):     $348.40
[x] PRIMARY SELL TARGET:                          $475.81
[x] BULL-CASE TRIM TARGET:                        $650.28
[ ] STOP LOSS (illustrative, 22% below entry):    $348.40 × 0.78 = $271.75
[✗] Risk/Reward Ratio (Primary Sell Target):      1.46:1 – 1.83:1 across the allowed 20–25% Max-Loss
                                                     range — FAILS the 2:1 minimum in every case
[x] Risk/Reward Ratio (Bull-Case Trim Target):    4.33:1 — clears, but is not the gating figure
[x] Max $ Risk (1.5% of portfolio ≈$61,101.28, per holdings.md's 2026-08-23 combined-broker sync —
     the most recent snapshot on file; informational only, no order placed):    $916.52
[x] Position sizing (informational, not acted on): 11 shares × $348.40 = $3,832.40 (≈6.27% of portfolio
     — would fall inside the 6–8% cap band for this score tier, had the R/R gate passed)
```

**No order is set up or placed.** Per fair-value-methodology.md: *"If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely."* This is a hard, independent gate per operating-brief.md's BUY/SELL ORDER SETUP rule.

---

## 8. Recommendation

# **WATCHLIST ONLY — do not enter.** The Composite Score (10.8) nominally supports a Full-position Buy signal (6–8%), and the Quality Gate narrowly passes (81.2, +1.2 cushion), but the Risk/Reward Ratio against the Primary Sell Target (1.46:1–1.83:1 across the entire allowed Max-Loss range) independently fails the 2:1 minimum gate. No position opened.

**This is a materially different bottom line from the 2026-08-23 session's "BUY — Enter now."** Both are correct for the information available at the time — this is exactly what Rule 9's mandatory post-earnings re-valuation is *for*. The path here:

1. **The earnings themselves were not weak** — Q4 revenue and non-GAAP EPS both beat consensus, and the stock is mechanically *cheaper* on this framework's valuation sub-scores today than pre-earnings (Valuation Score 2.8 vs. 8.7). The Telegram trigger's "weak report" framing doesn't match the primary-source numbers (§2), and this session did not treat it as data at any point — only as the signal to check the (already-overdue) Rule 9 trigger.
2. **What actually changed the outcome is the Sell Target, not the cheapness score.** Once the stale $27+ EPS figure (unchanged across two sessions despite a full earnings cycle intervening — a red flag caught and resolved in §5.2) is replaced with Intuit's own $23.00 FY2027 guidance midpoint, the multiples-based leg of Fair Value drops materially, and the achievable reward-to-risk ratio compresses below the framework's 2:1 floor — even though the live price is lower and the valuation multiples are cheaper than before.
3. **The Quality Gate pass is narrower than 08-23 (81.2 vs. 82.8), and remains single-signal-sensitive** (§3h) — three of five plausible sensitivity readings fail the 80.0 floor. The Brand-premium Moat call and the Growth structural-deceleration treatment are both judgment calls with real evidence on each side, laid out in full in §3c/§3e for the human investor to weigh independently.
4. **This does not mean the thesis is broken** — nothing here is a Full Exit trigger (this framework doesn't hold a position to exit) or a "the company is deteriorating" finding. QuickBooks Online and the Big Bets bundle are still growing, pricing power in the core business is arguably stronger evidence than before, and the FY2027 deceleration is explicitly a deliberate strategic choice, not (per the disclosed facts) a demand collapse. It is a **price/reward math** conclusion: the fair-value estimate this framework is willing to underwrite doesn't leave enough room above the entry price, relative to the downside risked, to clear this framework's own minimum bar.

**No order is placed by this session** (recommendation only, per repo convention).

---

## 9. Next Review Trigger

**Standing Rule 9 triggers:** guidance revision (up or down), M&A, management change, macro shift, or a >15% unexplained move. Given the R/R failure is driven primarily by the sell-target/EPS-basis gap (§7.2), **a further price decline toward the effective ~$285–300 zone (where the algebraic 2:1 breakeven sits under the current fair-value estimate) would independently re-open the entry case and should be checked when/if it occurs** — not an automatic entry, a fresh full recheck per SNDK precedent.

**Also flagged for the next scheduled re-score:** Q1 FY2027 earnings (expected ~November 2026) — the first print under the new deliberate-reset strategy and the first quarter reporting Mailchimp as its own segment; the single most useful near-term evidence on whether the customer-growth reacceleration bet is working.

---

## 10. Watchlist Entry

Updated `watchlist/not-in-portfolio/INTU/INTU-2026-08-23.md` with a new dated row (2026-08-26) — the valuation/action category changed materially (BUY Enter-now → WATCHLIST ONLY) and a Rule 9 fundamental trigger (earnings) fired, both independently qualifying for a new row per watchlist/README.md. Ticker stays in `not-in-portfolio/` (no position opened, none held).

---

## Glossary

| Term | Meaning |
|---|---|
| **8-K** | The SEC "current report" filing a US public company must submit within days of a material event — Intuit's Q4/FY2026 earnings press release was furnished this way. |
| **Big Bets (Intuit)** | Intuit's own label for a bundle of newer, faster-growing offerings — mid-market QuickBooks Online Advanced/Intuit Enterprise Suite, assisted tax, money-services products — called out separately because it's growing much faster (34% in FY2026, ~30% of revenue) than the base business. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **Composite Score** | This framework's single ranking number blending the Quality Score and the Valuation Score 50/50 (0 = most attractive, 100.0 = least). INTU scores 10.8. |
| **Consensus (analyst consensus)** | The average/median of individual sell-side analysts' published estimates for a company's future revenue, earnings, etc. — can lag a fresh earnings report by hours to days before every source has updated it, as flagged in §5.2 of this session. |
| **DCF (Discounted Cash Flow)** | A valuation method that estimates a company's value today as the sum of its future cash flows, discounted back to present value at a required rate of return (WACC). |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **EV** | Enterprise Value — a company's total value to all capital providers: market cap + debt − cash. |
| **EV/EBIT, EV/EBITDA** | Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE — the inverse of the PE ratio, expressed as a yield so it can be compared directly against bond yields (e.g. the 10-Year Treasury). |
| **Fast Grower** | Peter Lynch's term for a company growing earnings per share faster than 15%/year for 3+ years — INTU's FY2024–2026 pattern (+23.9%, +31.1%, +20.4%) qualifies. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. |
| **Fiscal Year (FY)** | A company's 12-month accounting year, which doesn't have to align with the calendar year. Intuit's runs 1 August–31 July; FY2026 just closed. |
| **Forward PE** | Price ÷ next twelve months' expected earnings per share. |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook companies use for their official financial statements; this framework scores off GAAP figures. |
| **Gross Margin** | Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted sub-score total; none fire for INTU. |
| **Market Cap (Market Capitalization)** | Share price × total shares outstanding — the total value the market currently assigns to a company's equity. |
| **Moat** / **Moat Signal** | A durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors; this framework's 5-point scored checklist version of the concept. |
| **MoS (Margin of Safety)** | How far below fair value the buy price is set, as a cushion against being wrong. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt. |
| **Net Margin** | Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax. |
| **Non-GAAP** | A company's own adjusted presentation of a financial measure that strips out items management deems non-recurring — self-reported, not independently audited the same way as GAAP. This session uses Intuit's Non-GAAP EPS *guidance figure* only as the least-bad available forward-EPS input (§5.2), while still scoring off GAAP throughout for the Quality Score. |
| **PEG ratio** | PE ratio ÷ earnings growth rate — a PE adjusted for growth, used to judge whether a fast grower's multiple is justified by its growth rate. |
| **PW (Probability-Weighted) Fair Value** | This framework's blended fair value estimate — 25% bull + 50% base + 25% bear (Rule 7) — used as the single fair-value input to both the order setup and the Upside/Downside Modifier. |
| **QuickBooks Online (QBO)** | Intuit's cloud-based small-business accounting product — its largest growth engine. |
| **Quality Score** | This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading profitability, margins, growth, balance sheet, moat, and FCF quality. A company must score 80.0+ to proceed to Phase 02. INTU scores 81.2 — a narrow pass (see §3h). |
| **Rate Environment Gate** | The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier. |
| **R/R (Risk/Reward Ratio)** | (Sell Target − Entry) ÷ (Entry − Stop Loss) — how much upside is on offer per unit of downside risked; this framework requires at least 2:1. INTU's R/R (1.46:1–1.83:1) is the gate that blocks entry this session. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 4** | This framework's sanity-check protocol — implied-return reasonableness, multiple sanity vs. comps, margin mean-reversion checks — applied here to catch the stale-EPS data-quality issue in §5.2. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **Shareholder yield** | Cash returned to owners as a % of price — dividend yield plus net buyback yield combined. |
| **TAM** | Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market. |
| **Treasury yield (10Y)** | The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results — here, Intuit's full FY2026 (ended 31 July 2026). |
| **Upside/Downside Modifier** | An additive, ±15-bounded adjustment to the valuation score based on expected annual return (E) — strong expected upside lowers the score, an expected loss raises it. |
| **WACC (Weighted Average Cost of Capital)** | The discount rate used in a DCF — the blended required return of a company's debt and equity holders. |

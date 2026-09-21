# NEW POSITION — APP (AppLovin Corporation, Class A) — 2026-09-21

**Task type:** NEW POSITION
**Date:** 21 Sep 2026
**10Y US Treasury Yield:** 4.94% (FRED `DGS10`, last published observation 2026-09-17 — most recent value available as of this session)
**Rate Regime Modifier:** +5 (10Y in the 3.5–5% bracket)
**Current APP portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md))
**Sector:** Technology — Mobile AdTech (AI-driven ad-mediation/ad-network, AXON engine)
**Scoring methodology in force:** Quality Score + 80.0+ gate + Composite Score, version 2026-06-29 ([quality-scoring.md](../framework/quality-scoring.md), [valuation-scoring.md](../framework/valuation-scoring.md))
**Trigger:** [Telegram Stock-Mention Scan](../portfolio/snapshots/telegram-watch.md), `t.me/tarasguk` post `#11996` (2026-09-21T19:09:18 UTC) — "Is there anyone who became an investor in $APP after watching [video]" — a discovery trigger only, no financial claim, per Rule 0.

---

## 0. Data-gap resolution — the 2026-09-07 blocker no longer applies

`/new-position APP` was previously attempted on **2026-09-07** ([telegram-watch.md row](../portfolio/snapshots/telegram-watch.md)) and got through Phase 01 — Quality Score **84.6** on a conservative floor (Moat_Score left at 0.0, unresearched that pass), clearing the 80.0+ gate — but was **blocked at Phase 02**: the Rate Environment Gate and Forward-PE sub-score both need a live analyst-consensus forward-EPS figure, served only via Yahoo Finance's crumb-gated `quoteSummary`/`earningsTrend` endpoints, and the crumb-issuing cookie flow (`fc.yahoo.com` → `query1.finance.yahoo.com/v1/test/getcrumb`) was not reachable in that session's network environment.

**This session re-tested that flow directly and it now works.** `fc.yahoo.com` returns a valid session cookie (HTTP 404 page body, but a real `Set-Cookie: A3=...` header), `query1.finance.yahoo.com/v1/test/getcrumb` returns a valid crumb using that cookie, and `query2.finance.yahoo.com/v10/finance/quoteSummary/APP?modules=earningsTrend,defaultKeyStatistics,financialData,summaryDetail&crumb=...` returns full data (forward EPS, analyst estimates, PEG, analyst price targets). This session's proxy status (`__agentproxy/status`) shows `"selective": false` — no host-level allowlist restriction — confirming the earlier block was an environment-specific network-policy limitation that has since been lifted, not a change on Yahoo's end. **Phase 02 proceeds this session using this live-fetched data — no forward metric is invented or estimated.**

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$328.88** | IBKR `get_price_snapshot`, contract_id 481863646 (NASDAQ: APP, "APPLOVIN CORP-CLASS A"), last trade |
| Change | +6.76% intraday (prior close $308.06 per Yahoo) | IBKR `change` field |
| Bid / Ask | $328.00 / $329.54 | IBKR live snapshot |
| 52-week high / low | $745.61 / $297.50 | IBKR `misc_statistics` |
| 13-week high | $576.46 | IBKR `misc_statistics` |
| Cross-check | Yahoo Finance `quoteSummary` snapshot: $330.17 (regular-session, ~same timestamp) | query2.finance.yahoo.com, consistent with IBKR to within 0.4% |

Contract confirmed via `search_contracts` (exact `symbol == "APP"` match, NASDAQ, US primary listing) before pricing, per this framework's option-selection discipline. Live IBKR price ($328.88) used as price of record throughout; no price inferred from multiples.

---

## 2. TTM Fundamentals (Phase 01 / Quality Score inputs)

TTM computed as Q3 FY2025 + Q4 FY2025 + Q1 FY2026 + Q2 FY2026 (period ending 2026-06-30, the most recently completed quarter — confirmed via Yahoo's own `mostRecentQuarter` field). Source: `yfinance` quarterly financials/cashflow/balance-sheet (Yahoo's own reported figures, sourced from APP's 10-Q/10-K filings) — same methodology and same TTM window as the 2026-09-07 attempt (no new quarter has reported since), used here as a fresh, independently re-fetched cross-check rather than carried forward unchecked.

| Quarter | Revenue | Gross Profit | EBIT | Net Income | Pretax Income | Tax Provision |
|---|---|---|---|---|---|---|
| Q2 FY2025 | $1,258.75M | $1,103.68M | $935.41M | $819.53M | $884.00M | $112.15M |
| Q3 FY2025 | $1,405.05M | $1,230.19M | $1,072.38M | $835.55M | $1,020.95M | $185.40M |
| Q4 FY2025 | $1,657.94M | $1,474.42M | $1,304.64M | $1,102.27M | $1,253.35M | $151.10M |
| Q1 FY2026 | $1,842.45M | $1,638.82M | $1,482.57M | $1,205.61M | $1,431.41M | $225.80M |
| Q2 FY2026 | $1,923.69M | $1,697.89M | $1,556.68M | $1,266.54M | $1,505.53M | $238.99M |

**TTM (Q3 FY2025 → Q2 FY2026):**

| Metric | TTM Value | Computation |
|---|---|---|
| **TTM Revenue** | **$6,829.12M** | 1,405.05+1,657.94+1,842.45+1,923.69 — matches Yahoo's own `totalRevenue` (6,829,124,096) exactly |
| **TTM Net Income (to common)** | **$4,409.85M** | Yahoo `netIncomeToCommon` (sum of quarterly Net Income ≈$4,409.97M, immaterial ~$0.1M rounding vs. the minority-interest-adjusted figure) |
| **TTM Net Margin** | **64.57%** | 4,409.85 / 6,829.12 — matches Yahoo `profitMargins` (0.64576) exactly |
| **TTM Gross Profit** | **$6,041.31M** | 1,230.19+1,474.42+1,638.82+1,697.89 — matches Yahoo `grossProfits` exactly |
| **TTM Gross Margin** | **88.46%** | 6,041.31 / 6,829.12 — matches Yahoo `grossMargins` (0.88464) exactly |
| **TTM EBIT** | **$5,416.27M** | 1,072.38+1,304.64+1,482.57+1,556.68 |
| **TTM D&A** | **$134.07M** | 35.10+32.74+33.67+32.56 (quarterly cashflow) |
| **TTM EBITDA** | **$5,550.33M** | EBIT + D&A |
| **TTM effective tax rate** | **15.38%** | Tax Provision TTM $801.28M ÷ Pretax Income TTM $5,211.23M |
| **TTM OCF** | **$4,527.59M** | 772.23+1,053.42+1,313.73+869.04 (Yahoo `operatingCashflow` matches exactly: 4,527,588,864) |
| **TTM FCF** | **$4,499.27M** | Sum of quarterly "Free Cash Flow" (≈OCF − minimal CapEx, ~$28M/yr per FY2025 annual CapEx) — 772.23+1,053.42+1,285.42+869.04. *(Yahoo's own summary `freeCashflow` field showed $3,179.96M, a stale/differently-dated figure inconsistent with its own quarterly cash-flow statements; this session uses the quarter-by-quarter roll-forward, which reconciles exactly with Yahoo's own `operatingCashflow` TTM figure and independently cross-checks against the FCF/NI ratio below — not invented, and consistent with the FCF/NI ratio the 2026-09-07 session also found ≈102%.)* |
| **TTM FCF/NI conversion** | **102.03%** | 4,499.27 / 4,409.85 |

**Other inputs:**

| Metric | Value | Source |
|---|---|---|
| FY2022 Revenue | $2,817.06M | `yfinance` annual financials |
| FY2023 Revenue | $1,841.76M (**−34.6% YoY** — reflects APP's 2025 divestiture of its mobile-apps/games business, a documented corporate action, not a data error) | `yfinance` annual financials |
| FY2024 Revenue | $3,224.06M | `yfinance` annual financials |
| FY2025 Revenue | $5,480.72M | `yfinance` annual financials |
| **Revenue CAGR 3yr (FY2022→FY2025)** | **24.84%** | (5,480.72/2,817.06)^(1/3) − 1 |
| Net Debt (2026-06-30) | $461.77M | Total Debt $3,515.07M − Cash $3,053.31M |
| Invested Capital (net of cash, 2026-06-30) | $3,624.78M | Total Debt $3,515.07M + Stockholders Equity $3,163.02M − Cash $3,053.31M |
| **ROIC (TTM)** | **126.44%** | NOPAT (EBIT×(1−15.38%) = $4,583.24M) ÷ Invested Capital (net of cash) $3,624.78M |
| Ordinary shares outstanding (all classes, 2026-06-30) | 335,291,521 | `yfinance` balance sheet — matches Yahoo's `impliedSharesOutstanding` (335,939,521 at a slightly later snapshot date) |
| Diluted average shares (Q2 FY2026) | 337,031,000 | `yfinance` quarterly financials — used for DCF/multiples per-share output |
| Shares outstanding trend | 373.87M (FY2022) → 339.89M (FY2023) → 340.04M (FY2024) → 338.31M (FY2025) → 335.29M (Q2 FY2026) | Net reduction, consistent with active buybacks (no dividend) |
| Analyst consensus (31 analysts) | Mean target $501.94, median $476.00, low $325.00, high $790.00, mean recommendation 1.58 ("buy") | Yahoo `financialData` (crumb-gated `quoteSummary`) |
| FY2026 consensus EPS / growth | $15.66 / +60.6% | Yahoo `earningsTrend` "0y" period (endDate 2026-12-31) |
| FY2027 consensus EPS / growth | $20.00 / +27.7% | Yahoo `earningsTrend` "+1y" period (endDate 2027-12-31) |
| FY2026 consensus Revenue | $8,101.4M (+47.8%) | Yahoo `earningsTrend` "0y" |
| FY2027 consensus Revenue | $10,263.9M (+26.7%) | Yahoo `earningsTrend` "+1y" |
| Forward EPS (NTM, Yahoo's own blended figure) | $20.98 | Yahoo `defaultKeyStatistics.forwardEps` |
| PEG ratio (Yahoo-reported) | 0.67 | Yahoo `defaultKeyStatistics.pegRatio` |
| Beta | 2.488 | Yahoo `defaultKeyStatistics` |

### Data gaps / flags

1. **Revenue 3yr CAGR is distorted by the 2025 mobile-apps-business divestiture** (documented corporate action — FY2023 revenue fell −34.6% YoY on this basis). The 24.84% CAGR is the correct trailing 3yr figure per the framework's rolling-window convention, but it does not represent organic like-for-like growth of the current (ads-only) business — flagged for a human sanity check, as the 2026-09-07 session also flagged.
2. **This same divestiture, plus loss-making/near-breakeven quarters in FY2022–early FY2023** (`get_earnings_dates` shows negative or near-zero quarterly EPS through mid-2023), make a trailing 5-year historical PE range **not meaningful** — see §4 (No-history fallback applied to FwdPE_Score).
3. **No metric in this session was invented or estimated.** Every TTM figure is a direct roll-forward of individually-sourced quarterly figures, cross-checked against Yahoo's own reported summary fields (which matched exactly for Revenue, Gross Profit, Net Margin, Gross Margin, and OCF) with one flagged exception (Yahoo's summary `freeCashflow` field, addressed above).

---

## 3. Quality Score (Phase 01) — Full Calculation

### Hard disqualifier check

| Disqualifier | APP Status | Fires? |
|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years | TTM 102.0%; FY2023 279.3%, FY2024 131.3%, FY2025 118.3% — comfortably above 70% every measurable year | ❌ No |
| Net Debt/EBITDA over threshold (2.5× standard) | 0.083× | ❌ No |
| Not FCF-positive for 3+ consecutive years | FCF positive every fiscal year FY2022–FY2025 and TTM | ❌ No |

**No hard disqualifier fires.**

### Sub-scores

**Profitability (25% weight)**
```
NetMargin_Component = clamp((64.57 / 30) × 100, 0, 100) = 100.0   (clamped)
ROIC_Component       = clamp((126.44 / 30) × 100, 0, 100) = 100.0  (clamped)
Profitability_Score  = (100.0 + 100.0) / 2 = 100.0   (no FCF cap — FCF-positive every year)
```

**Margins (15% weight)**
```
GrossMargin_Score = clamp((88.46 / 80) × 100, 0, 100) = 100.0   (clamped)
```
3yr trend (55.4% FY2022 → 80.7% FY2023 → 83.9% FY2024 → 87.9% FY2025) is structurally expanding, but the bonus is moot — already at the 100.0 ceiling.

**Growth (20% weight)**
```
Growth_Score(base) = clamp((24.84 / 25) × 100, 0, 100) = 99.35
```
**Modifier — TAM expansion, +10.** Documented evidence: AppLovin's self-serve AXON advertising platform is being rolled out to all advertisers in 2026 (previously invite-only), explicitly targeting expansion beyond mobile-gaming into general e-commerce advertising and positioning Google/Meta/Amazon ("the Big Three") as its new competitive frame rather than mobile-gaming peers; independently, a Jefferies advertiser survey found AppLovin's share of e-commerce advertising budgets rose 169 bps between Q4 2025 and full-year 2026 to 11% of total spend — the largest gain among networks surveyed. No documented structural deceleration evidence exists (growth is accelerating, not decelerating). Sources: [AppLovin: The AI Giant Dominating the Mobile Ad-Tech Frontier](https://markets.chroniclejournal.com/chroniclejournal/article/finterra-2026-2-5-applovin-app-the-ai-giant-dominating-the-mobile-ad-tech-frontier), [AppLovin gains e-commerce ad share as advertisers expand platform use, Jefferies survey finds](https://www.proactiveinvestors.com/companies/news/1095274/applovin-gains-e-commerce-ad-share-as-advertisers-expand-platform-use-jefferies-survey-finds-1095274.html).
```
Growth_Score = clamp(99.35 + 10, 0, 100) = 100.0   (clamped)
```

**Balance Sheet (15% weight)**
```
BalanceSheet_Score = clamp(100 × (1 − 0.083/4), 0, 100) = 97.92 → 97.9
```

**Moat Signal (15% weight)** — researched this session (the 2026-09-07 attempt left this at a conservative 0.0 floor, flagged as a manual follow-up item; this session closes that gap with cited web research)

| Signal | APP | Cited evidence | TRUE? |
|---|---|---|---|
| Market share stable or growing | Documented, **growing** | Tenjin's *Ad Monetization Benchmark Report 2026*: AppLovin's iOS ad-revenue share rose from 39% (Q1 2026) to 44% (Q2 2026) — the next-largest competitor (Mintegral) at 16%, a 28pp gap; Android share rose 19%→23% over the same period. Separately, AppLovin's ad-mediation platform (MAX) holds 80%+ mediation market share. [Source](https://tenjin.com/blog/ad-mon-gaming-2026/) | ✅ TRUE |
| Brand premium | **Not demonstrated** | Searched specifically for pricing-power evidence (price increases without volume loss). Found the opposite framing: advertisers are described as "ruthless ROAS optimizers who will move budget instantly when the math improves" — AppLovin's edge is framed as *better measured performance* (ROAS) driving budget reallocation, not the ability to charge more for the same result. This does not meet the "price increases without volume loss" evidentiary bar this framework's Moat Signal checklist requires. [Source](https://gabgrowth.com/p/applovin-deep-dive) | ❌ FALSE |
| Network effect | Documented | AXON is explicitly a two-sided "data flywheel": "every auction improves model quality, which improves advertiser ROAS, which attracts more advertisers, which generates more data" — processes 2M+ ad auctions/second across 1B+ devices via the MAX mediation platform. [Source](https://capitalblueprint.substack.com/p/applovin-corporation-nasdaq-app-deep) | ✅ TRUE |
| Switching costs | Documented | Publishers embed AppLovin's MAX SDK for mediation/monetization — "deep MAX integration creates high exit friction," with switching costs quantified in one analysis at "5% to 20% of revenue due to integration complexity, data dependency, and contractual terms." AppLovin also holds 536 global patents. [Source](https://capitalblueprint.substack.com/p/applovin-corporation-nasdaq-app-deep) | ✅ TRUE |
| Scale cost advantage | Documented | AppLovin's TTM gross margin (88.5%, up from 80.8% two years ago) sits well above peers operating similar ad-network/mediation businesses — Unity Software's overall gross margin ≈74% (Q1 2026), with Unity/Digital Turbine's ads businesses described as "near breakeven" on a gross-margin basis — a cost-per-unit-of-revenue gap consistent with AppLovin's greater platform scale (AXON serves $10B+ in annual media spend). [Sources](https://capitalblueprint.substack.com/p/applovin-corporation-nasdaq-app-deep), [Unity Q1 2026 gross margin](https://www.gurufocus.com/) | ✅ TRUE |

```
Moat_Score = (4 / 5) × 100 = 80.0
```

**FCF Quality (10% weight)**
```
FCFQuality_Score = clamp(((1.0203 − 0.40) / 0.60) × 100, 0, 100) = 100.0   (clamped)
```

### Final Quality Score

```
Quality Score = (100.0 × 0.25) + (100.0 × 0.15) + (100.0 × 0.20) + (97.9 × 0.15) + (80.0 × 0.15) + (100.0 × 0.10)
              = 25.00 + 15.00 + 20.00 + 14.685 + 12.00 + 10.00
              = 96.685 → rounds to 96.7
```

## **Quality Score: 96.7 — CLEARS the 80.0+ gate comfortably** (vs. the 2026-09-07 attempt's conservative-floor 84.6, computed with Moat_Score=0; this session's cited Moat research adds 12.0 points, and the TAM modifier resolves the Growth sub-score to its ceiling as well).

**Sensitivity note (shown per "no black-box outputs"):** the extremely high Profitability sub-score (100.0, clamped) is driven by an unusually thin Invested-Capital-net-of-cash denominator ($3.62B) relative to AppLovin's earnings power — a real, if somewhat mechanical, feature of a company whose equity base was thinned by historical losses/buybacks even as current-period profitability is very high. This is not a calculation error, but it is a large driver of the final score and is flagged for the human reviewer's awareness, consistent with the same convention this framework used for MCO/TTD's ROIC sensitivity notes.

---

## 4. Rate Environment Gate

```
Forward PE (live) = $328.88 / $20.98 (Yahoo NTM forwardEps) = 15.675×
Earnings Yield (EY) = 1 / 15.675 = 6.379%
Spread = EY − 10Y = 6.379% − 4.94% = 1.439%
```
Spread (1.439%) < +1.5% threshold → **Step 1 fires: +5** (yellow flag, not a veto, per the 2026-06-07 softening).
10Y yield 4.94% falls in the 3.5–5% bracket → **Step 2: +5**.

**Combined Rate Modifier: +10.**

---

## 5. Valuation Score (Phase 02) — Full Calculation

**PEG not applicable — redistribute 15% to EV/EBIT (40% total).** Per the Upgrade 3 clean-earnings clarification: "3+ years" requires a reliable, non-distorted earnings base. AppLovin does not qualify — FY2022 was a net loss, and the 2025 mobile-apps divestiture is a documented one-off structural change to the earnings base within the trailing window.

**FCF Yield (40% weight)**
```
Market Cap = 335,291,521 shares × $328.88 = $110.271B
FCF Yield = $4,499.27M / $110,271M = 4.080%
FCF_Score = clamp(100 × (1 − 4.080/10), 0, 100) = 59.2
```

**EV/EBIT (40% weight, PEG redistributed)**
```
EV = Market Cap $110.271B + Total Debt $3.515B − Cash $3.053B = $110.732B
EV/EBIT = $110,732M / $5,416.27M = 20.44×
EV/EBIT_Score = clamp((20.44 − 12) / 23 × 100, 0, 100) = 36.7
```

**Forward PE (20% weight) — No-history fallback applied, flagged**
```
FwdPE_Score = 50.0 (neutral, flagged)
```
Reasoning: a trailing 5-year PE series would span FY2021–2026, a window containing (a) multiple loss-making/near-breakeven quarters (2022–early 2023, per `get_earnings_dates`, where TTM PE is undefined or economically meaningless) and (b) the 2025 mobile-apps divestiture, which fundamentally changed the earnings base (gross margin 55%→88%) partway through the window. Per valuation-scoring.md's explicit "GAAP earnings base too distorted to be meaningful" criterion, this session does not force a 5yr average/range calculation over a window that doesn't represent the current business — using the flagged neutral fallback instead of inventing a range.

**Raw weighted score**
```
Raw = (59.2 × 0.40) + (36.7 × 0.40) + (50.0 × 0.20) = 23.68 + 14.68 + 10.00 = 48.36
```

**Rate Modifier: +10** (§4)

### Upside/Downside Modifier

**Step 1 — Fair Value (Rules 1, 2, 3, 7).** Sector: Technology/Growth → DCF primary, EV/Revenue & Forward-PE secondary (Rule 1). WACC built from CAPM: risk-free 4.94% + beta 2.488 × 5% ERP = cost of equity 17.38%; debt is <3.2% of capital structure, so WACC ≈ 17.0% (base), shifted ±1pp for bull/bear per Rule 2.

*(All growth/fade/multiple assumptions below are explicit modeling judgment calls, clearly distinct from the sourced financial data above — flagged per Rule 2/6 discipline, not invented financial facts.)*

**DCF — 3 scenarios, 10yr explicit fade + terminal value**

| | Bull | Base | Bear |
|---|---|---|---|
| WACC | 16.0% | 17.0% | 18.0% |
| Yr1–5 FCF growth | 30%,24%,19%,15%,12% | 25.2%,18%,14%,11%,9% | 15%,8%,5%,3%,2% |
| Yr6–10 fade | 10.3%→3.5% | 7.8%→3.0% | flat 2.0% |
| Terminal growth | 3.0% | 2.75% | 2.0% |

Starting FCF = TTM $4,499.27M; discounted 10yr explicit cash flows + Gordon-growth terminal value; Equity = EV − Net Debt ($461.77M); ÷ 337.03M diluted shares:

```
Base: DCF EV=$56,771M → Equity=$56,309M → $167.07/share
Bull: DCF EV=$76,111M → Equity=$75,649M → $224.46/share
Bear: DCF EV=$34,959M → Equity=$34,497M → $102.35/share
```

**Multiples-Based Value** (Rule 1 secondary methods for Tech/Growth: Forward PE + EV/Revenue)
```
Forward-PE basis (NTM EPS $20.98): Base 20× → $419.62   Bull 28× → $587.46   Bear 14× → $293.73
EV/Revenue basis (FY2027 consensus rev $10,263.9M): Base 12× → $364.08/sh   Bull 16× → $485.89/sh   Bear 8× → $242.26/sh
Multiples-Based Value = average of the two: Base $391.85   Bull $536.68   Bear $268.00
```

**Blended Fair Value (40% DCF / 60% Multiples, Triangulation Formula)**
```
Bull: 0.40×224.46 + 0.60×536.68 = $411.79
Base: 0.40×167.07 + 0.60×391.85 = $301.94
Bear: 0.40×102.35 + 0.60×268.00 = $201.74
```

**PW Fair Value (Rule 7, 0.25/0.50/0.25)**
```
PW FV = 0.25×411.79 + 0.50×301.94 + 0.25×201.74 = $304.35
```

**Sanity check (Rule 0 Step 4 / bull-case FV check):** independent analyst consensus mean target is **$501.94** (median $476.00, range $325–$790, 31 analysts) — materially more bullish than this session's bottom-up PW Fair Value ($304.35, ~7% *below* the live price). Shown transparently rather than reconciled away, consistent with the MCO 2026-09-11 precedent: the sell-side's own bull case ($790 high) sits above even this session's own Bull-case Blended FV ($411.79), while this session's Base case ($301.94) sits well below the analyst median. This is a case where a bottom-up, mean-reversion-disciplined DCF (Rule 6) lands meaningfully more conservative than sell-side consensus, largely because of the punitive 17% WACC implied by AppLovin's beta (2.488) and this session's deliberate fade of the currently very high (57–70%) trailing growth rates toward more sustainable long-run rates (Rule 6: "growth vs. reinvestment," never extrapolate a post-divestiture growth spike indefinitely).

**Step 2 — Expected annual return E**
```
Gap Upside % = (304.35 / 328.88) − 1 = −7.46%
Catalyst window: 2yr default (no single narrower-than-2yr re-rating catalyst with a specific date identified; the self-serve AXON rollout and e-commerce ad-share expansion are ongoing 2026 initiatives, not a single dated catalyst)
Annualized gap = −7.46% / 2 = −3.73%
Intrinsic growth = average of Base-case Yr1–5 FCF growth (25.2,18,14,11,9)/5 = 15.44%
Shareholder yield = 0% dividend + ~1.8% net buyback (from the share-count trend in §2: ~1.8%/yr trailing net reduction, no dividend)
E = −3.73% + 15.44% + 1.8% = 13.51%
```
**Guardrail check:** E ≥ H, so this is the "upside" side of the mapping; no catalyst-cap issue arises regardless of catalyst-window judgment, since the resulting M (below) doesn't approach the −5 cap.
```
M = −15 × clamp((13.51 − 10)/15, 0, 1) = −15 × 0.234 = −3.51
```

### Final Valuation Score
```
Final Score = 48.36 (raw weighted) + 10.00 (Rate Modifier) + (−3.51) (Upside/Downside Modifier)
            = 54.85 → rounds to 54.9
```

**Valuation Score: 54.9** (50.0–69.9 band → nominally HOLD/Fair Value on the raw valuation score alone — but see §6, the Composite Score is what governs).

---

## 6. Composite Score

```
Composite Score = 0.50 × (100 − 96.7) + 0.50 × 54.9
                = 0.50 × 3.3 + 0.50 × 54.9
                = 1.65 + 27.45
                = 29.1
```

**Composite Score: 29.1 — lands in the 0.0–29.9 → "BUY, Full position 6–8%" band.**

**Sensitivity flag (shown per "no black-box outputs"):** because Quality Score is so high (96.7), `100 − Quality Score` contributes only 3.3 of the 50-point-weighted Quality half — meaning the Composite Score here is overwhelmingly driven by the Valuation Score half, and would stay in a "BUY"-adjacent band even if the Valuation Score were considerably higher (e.g. a Valuation Score of 90 would still produce a Composite of ~46.65, "BUY Standard 3–5%"). This is a mechanical consequence of the Composite Score formula when Quality Score is this extreme, not an error — but it means the ultimate BUY-tier finding here is much more sensitive to the Quality Score's own sensitivity (§3's note on the thin invested-capital denominator) than to the DCF/multiples judgment calls in §5. Flagged for the human reviewer.

---

## 7. Fair Value & Order Setup

Per fair-value-methodology.md, Composite Score 29.1 sits in the 0.0–29.9 band: MoS 15–20%, Max Acceptable Loss 20–25%, Position cap 6–8% of portfolio, Risk up to 2%. Given AppLovin's shorter operating history as a pure-ads business (post-2025 divestiture) and the flagged SEC/FTC scrutiny of mobile-ad data-collection practices industry-wide (a qualitative risk surfaced during moat research, not yet a company-specific enforcement action against APP specifically — flagged for Phase 04 monitoring), this session uses the **more conservative end of each range**: 20% MoS, 25% max loss.

```
[X] Valuation Score (incl. Upside/Downside Mod):    54.9
[X] Composite Score:                                29.1  (BUY Full 6–8% band)
[X] Expected annual return E / catalyst window:     13.51% / 2yr (default, no single dated re-rating catalyst identified)
[X] Upside/Downside Modifier applied:               −3.51
[X] DCF Fair Value (base):                          $167.07
[X] Multiples-Based Fair Value (base):               $391.85
[X] Blended Fair Value (PW, bull/base/bear):         $304.35
[X] Margin of Safety %:                              20%
[X] BUY PRICE (limit order):                         $304.35 × 0.80 = $243.48
[X] PRIMARY SELL TARGET (= PW Fair Value):           $304.35
[X] BULL-CASE TRIM TARGET (Bull FV × 0.90):          $411.79 × 0.90 = $370.61
[X] STOP LOSS (25% max loss from Buy Price):         $243.48 × 0.75 = $182.61
[X] Risk/Reward Ratio (primary/baseline basis):      (304.35 − 243.48) / (243.48 − 182.61) = 60.87 / 60.87 = 1.00 : 1   ❌ FAILS 2:1 minimum
[X] Risk/Reward Ratio (Bull-Case Trim Target basis): (370.61 − 243.48) / (243.48 − 182.61) = 127.13 / 60.87 = 2.09 : 1  (clears 2:1, but is the optimistic case)
[ ] Position size — not computed further; R/R gate fails on the primary (baseline) basis before sizing is meaningful
```

**Risk/Reward fails the 2:1 minimum on the primary (baseline) sell target — 1.00:1.** This is a structural feature of this Composite Score band's MoS/Stop-Loss geometry, consistent with the MCO 2026-09-11 precedent: for *any* MoS in [15%, 20%] combined with *any* max-loss in [20%, 25%] — the ranges this framework specifies for the 0.0–29.9 band — Risk/Reward on the primary Sell Target (= PW Fair Value) works out to `MoS / [(1−MoS) × MaxLoss]`, which peaks at 1.25:1 (MoS=20%, loss=20%) and is never able to reach 2:1 within the stated ranges when Buy Price and Sell Target both derive from the same Fair Value figure. This is not specific to APP's numbers — it is a mechanical property of the framework's own parameter ranges at this score band, flagged here as it was for MCO, not re-litigated as an APP-specific finding.

Per fair-value-methodology.md Step 6: **"If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely."** This session does not place an order.

---

## 8. Recommendation: **WATCHLIST ONLY — do not enter, do not place an order this session**

Despite a Composite Score (29.1) that nominally lands in the "BUY, Full position 6–8%" band, **Risk/Reward on the primary (baseline) basis fails the framework's own 2:1 minimum (1.00:1)** — fair-value-methodology.md's explicit instruction for this outcome is to wait, tighten the stop, or pass, not to place the naive MoS-derived limit order anyway (§7). **No order placed, no position opened.**

Two additional reasons argue for caution alongside the R/R failure, both flagged transparently rather than papered over:

1. **The Composite Score is unusually Quality-Score-dominated** (§6) — because Quality Score is 96.7, the Composite Score would stay BUY-adjacent across a wide range of Valuation Score outcomes, meaning this session's BUY-tier signal says more about AppLovin's extreme trailing profitability (§3's sensitivity note on the thin invested-capital denominator) than about the stock being cheap on a forward basis.
2. **This session's own bottom-up PW Fair Value ($304.35) sits below the live price ($328.88)** — a small (~7%) but real negative expected gap before adding intrinsic growth — while Wall Street's own analyst consensus ($501.94 mean) is considerably more bullish. Both reads are shown; this framework's own bottom-up build, using a mean-reversion-disciplined growth fade (Rule 6) and a WACC reflecting AppLovin's high beta, does not currently support "enter now" even setting the R/R mechanics aside.

**What would change this call:** a lower entry price (the mechanical R/R ceiling means no entry price fully resolves this within the stated MoS/stop ranges, but a materially lower price would still improve the risk-adjusted setup and is worth rechecking opportunistically — as the MCO precedent notes) or a tighter, evidence-based stop-loss below the stated 20-25% range for an exceptionally high-quality name. Neither is applied here, consistent with using the framework's stated ranges rather than ad hoc overrides.

**Recommended next steps:**
1. **Q3 FY2026 earnings** (expected ~November 2026, per APP's quarterly filing pattern) — mandatory Rule 9 re-score. Watch specifically whether revenue growth continues decelerating on schedule (consensus already prices in a fade from 57% → 28% → single digits over the next few years) and whether the self-serve AXON rollout/e-commerce expansion delivers evidence that could support crediting the Brand Premium Moat Signal (currently FALSE) or extending the TAM modifier further.
2. **SEC/FTC data-collection-practices scrutiny** (industry-wide, flagged during moat research, not yet a confirmed APP-specific enforcement action) — worth an explicit, dedicated web-search pass next session to determine whether this has become a company-specific Rule 9 trigger.
3. **Immediate re-score trigger** if a >15% unexplained price move occurs from $328.88 in either direction (Rule 9) — APP's beta (2.488) and 52-week range ($297.50–$745.61) make this a realistic possibility in either direction.
4. **Revenue CAGR distortion (§2, flag #1)** — worth a cleaner like-for-like organic growth reconstruction (e.g. ads-segment-only revenue pre/post divestiture) next session, rather than relying on the divestiture-distorted FY2022→FY2025 headline CAGR indefinitely.

---

## 9. Next Review Trigger

- **APP's Q3 FY2026 earnings** (expected ~November 2026) — mandatory Rule 9 re-score.
- **>15% unexplained price move from $328.88 in either direction** — immediate re-score per Rule 9.
- **Any company-specific SEC/FTC enforcement development** on data-collection practices — immediate re-score per Rule 9 (balance-sheet-crisis/moat-erosion class trigger, if it materializes).
- **No position opened by this session — nothing to log in `decisions/`.**

---

## 10. Data Gaps Flagged (summary)

1. **Revenue 3yr CAGR (24.84%) is divestiture-distorted** — a documented corporate action, not invented, but not directly comparable to a "clean" organic growth rate (§2, §3).
2. **No usable trailing 5-year PE range/average exists** (loss-making years + business-model transformation) — the framework's own no-history fallback (FwdPE_Score = 50.0) was applied rather than forcing an estimate (§5).
3. **DCF WACC/beta/growth-fade assumptions are explicit modeling judgment calls**, clearly distinct from the sourced financial data, shown in full per "no black-box outputs" (§5).
4. **Yahoo's own summary `freeCashflow` field was internally inconsistent** with its own quarterly cash-flow statements; this session used the quarter-by-quarter roll-forward instead, cross-checked against the FCF/NI ratio (§2, flag notes).
5. **The Composite Score's sensitivity to the Quality Score's own thin-invested-capital-denominator effect** is flagged explicitly (§3, §6) rather than silently accepted.
6. **No metric in this session was invented or estimated.** Every hard financial figure traces to a live-fetched source (IBKR live price, Yahoo Finance TTM financials/analyst consensus, cross-checked internally); every valuation assumption (WACC, growth fade, multiples) is explicitly labeled as a modeling judgment call, not a sourced fact.

---

## Glossary

- **AXON / AXON 2.0**, **MAX (AppLovin)**, **SDK (Software Development Kit)**, **ROAS (Return on Ad Spend)** — AppLovin-specific/adtech terms, added to [glossary.md](../framework/glossary.md) this session.
- **Quality Score**, **Composite Score**, **Rate Environment Gate**, **Rate Regime Modifier**, **Earnings Yield Spread Test**, **PW (Probability-Weighted) Fair Value**, **Upside/Downside Modifier (Expected-Return Modifier)**, **Hard disqualifier**, **Historical PE Modifier**, **Rule 0**, **Rule 1–8, Rule 10**, **Rule 9** — all defined in [glossary.md](../framework/glossary.md).
- **TTM (Trailing Twelve Months)** — the most recent four reported quarters combined, used throughout this session's Quality/Valuation Score inputs.
- **ROIC** — Return on Invested Capital: NOPAT ÷ Invested Capital (debt + equity, net of cash) — 126.44% TTM here, clamped at the Quality Score's 100.0 ceiling.
- **NOPAT** — Net Operating Profit After Tax: EBIT × (1 − effective tax rate).
- **Invested Capital** — debt + equity, net of cash, the ROIC denominator this framework uses.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / — before Interest, Taxes, Depreciation, and Amortization.
- **FCF (Free Cash Flow)** — Operating Cash Flow minus Capital Expenditures.
- **EV / EV/EBIT / EV/Revenue** — Enterprise Value and its multiples versus operating profit / revenue.
- **DCF** — Discounted Cash Flow.
- **WACC** — Weighted Average Cost of Capital, the DCF discount rate.
- **CAGR** — Compound Annual Growth Rate.
- **PEG ratio** — PE ÷ earnings growth rate.
- **Forward PE** — Price ÷ next-twelve-months expected EPS.
- **MoS (Margin of Safety)** — how far below fair value the buy price is set.
- **R/R (Risk/Reward ratio)** — expected gain ÷ expected loss; this framework requires ≥2:1.
- **Shareholder yield** — dividend yield plus net buyback yield.
- **Fast Grower** — Peter Lynch's term (EPS growth >15%/yr for 3+ years) — not applied to APP here (unreliable earnings base, see §5).
- **Moat Signal** — this framework's 5-point Quality Score checklist; APP scored 4 of 5 this session.
- **bps (basis points)** — 1 bps = 0.01 percentage points.
- **YoY** — Year-over-Year.

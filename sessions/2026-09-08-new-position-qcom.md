# New Position Evaluation — QCOM (Qualcomm Incorporated)

**Task type:** NEW POSITION
**Date:** 2026-09-08
**10Y US Treasury yield:** ~4.79% intraday (CNBC, 2026-09-08); FRED's most recently published official value is 4.77% (2026-09-03, publication lag) — noted for completeness only. **Not used this session** — the evaluation stops at the Phase 01 Quality Score gate (Section 4) before the Rate Environment Gate would otherwise apply, same precedent as the 2026-07-24 QCOM session and the 2026-07-19 SCHW session.

**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — a `tarasguk` post (tarasguk/11868, 2026-09-08 14:27:31 UTC), Ukrainian text translating to: *"Amazon will order custom chips from Qualcomm, and Qualcomm will sell chips and additionally its own shares at a fixed price of $161."* Per Rule 0, **this post's text is used only as the reason to look at QCOM today — never as a financial input.** QCOM is **not currently held** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)) and has one prior `/new-position` entry — [watchlist/not-in-portfolio/QCOM/QCOM-2026-07-24.md](../watchlist/not-in-portfolio/QCOM/QCOM-2026-07-24.md) — which **FAILed** the Quality Score gate at 60.3 (sensitivity range 58.2–72.3, all below 80.0), driven by weak Growth (10.25 — flat 3yr revenue CAGR, a documented-but-unproven data-center-AI diversification story, zero disclosed AI200/AI250 revenue at the time) and weak Moat (20.0 — only 1/5 signals). Its stated next-review trigger was fiscal Q3 2026 earnings (reported 2026-07-29, since covered) **or** a guidance revision/M&A/management change/>15% unexplained price move. A new, large Amazon customer relationship for custom AI/data-center chips — if verified real — speaks directly to the two previously-weakest sub-scores, which is why this re-evaluation was triggered now rather than logged as "no change."

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first, via Interactive Brokers MCP tools, before any other work.

| Source | Value | Detail |
|---|---|---|
| **IBKR live snapshot** (contract_id 273544, NASDAQ — "QUALCOMM INC") | **$174.47** | Last trade at ts 1788883862 (2026-09-08, US regular session), `is_close: false`, `halted: false` — a genuine live intraday print. |
| Day change (same snapshot) | **+$5.73 (+3.4%)** on the day | Directional context only — **not treated as an independent Rule-9 trigger**, since it is directly explained by the verified Amazon/AWS announcement below (news outlets reported an intraday pop as high as ~7–10% the same morning; IBKR's snapshot, taken later in the session, shows +3.4%, both consistent with the same real news event, not an "unexplained" move). |
| Bid/ask | $174.38 / $174.59 | Live NBBO at fetch time. |
| 52-week range (IBKR `misc_statistics`) | low **$121.51** / high **$258.95** | Current price is ~32.6% below the 52-week high and +43.6% above the 52-week low. Context only, not a scoring input. |
| Dividend yield (IBKR) | 2.15% | Not used as a scoring input this session (gate fails before any valuation-stage shareholder-yield component would matter). |
| Year-to-date change (IBKR) | +3.05% | Context only. |

**Live price used throughout this session: $174.47.**

---

## 2. Independent Verification of the Telegram Post's Claim (Rule 0 — never treat the post as a financial input)

The triggering post claimed: "Amazon will order custom chips from Qualcomm, and Qualcomm will sell chips and additionally its own shares at a fixed price of $161." This was checked against SEC filings, Qualcomm's own press materials, and reputable financial news — **not** against the Telegram post itself — following the same verification discipline as the AMZN-OpenAI check in [watchlist/in-portfolio/AMZN/AMZN-2026-08-01.md](../watchlist/in-portfolio/AMZN/AMZN-2026-08-01.md).

### 2.1 Verdict: **Verified as real, and materially accurate**, via a primary-source SEC filing

**Primary source — Qualcomm's own SEC Form 8-K**, filed 2026-09-08, report date 2026-09-03, Item 3.02 ("Unregistered Sales of Equity Securities"), accession no. 0001104659-26-105718 ([full text](https://www.sec.gov/Archives/edgar/data/0000804328/000110465926105718/tm2623289d1_8k.htm)):

- Qualcomm granted Amazon.com, Inc. a **warrant** to purchase **up to 25,000,000 shares of QCOM common stock** at an exercise price of **$161.26 per share**, expiring **2036-09-03**.
- The warrant **vests in tranches** tied to Amazon's execution of commercial arrangements, placement of binding purchase orders, and actual purchases of "QTI server chip products, technology, systems and manufacturing services" — up to a cumulative **$60 billion** in payments by Amazon over the term.
- 3,750,000 shares vested immediately on issuance, based on initial purchase commitments already made.
- Cashless exercise permitted; no voting rights while unexercised; resale to be registered via a prospectus supplement.

**Corroborating secondary sources** (same-day reporting, consistent with the filing): [CNBC](https://www.cnbc.com/2026/09/08/qualcomm-amazon-data-center-infrastructure-deal.html), [Bloomberg](https://www.bloomberg.com/news/articles/2026-09-08/qualcomm-signs-deal-to-provide-amazon-with-custom-ai-chips), [Reuters via Investing.com](https://au.investing.com/news/stock-market-news/qualcomm-strikes-ai-chip-deal-with-amazon-offers-right-to-buy-about-4-billion-in-stock-4632724), and Qualcomm's own press release ([StockTitan mirror](https://www.stocktitan.net/news/QCOM/qualcomm-announces-multi-generational-product-collaboration-with-r10nzgxe989j.html)):
- A **multi-generational product collaboration**: custom Qualcomm silicon for **AI inference workloads in AWS data centers**, plus joint development of **optical connectivity solutions scaling to 1.6T** and beyond.
- Qualcomm will also expand its own use of AWS infrastructure (including Amazon Bedrock) for chip-design EDA workloads, aiming to shorten design cycles.
- Framed by outlets as giving Qualcomm a **second major data-center anchor customer alongside Meta**, as it tries to establish a foothold against Nvidia in AI accelerators.
- The press release itself (per the StockTitan-sourced summary) explicitly frames this as a "**planned-collaboration stage**" announcement — no shipped product, no disclosed revenue yet, and it states "no current change to existing common holders' ownership or cash position" (the warrant is a contingent future issuance, not an immediate dilution).
- QCOM shares gained as much as ~7–10% intraday on the news before settling to +3.4% by the time of this session's IBKR price fetch (Section 1).

### 2.2 What is **not yet established** (flagged, not silently assumed)

- **No disclosed revenue** yet from this collaboration — it is a forward commercial framework (warrant vesting schedule, purchase-order structure) tied to *future* purchases, not booked business. The $60B figure is a **ceiling on warrant-vesting triggers**, not a revenue guide or backlog figure — none of the sources found this session characterize it as guaranteed revenue.
- No specific chip architecture, volume, unit pricing, or delivery-timeline detail beyond "multiple generations," "AI inference," and "optical connectivity to 1.6T" was disclosed in the 8-K or the press materials reviewed.
- **Conclusion:** the post's core claim — Amazon ordering custom chips from Qualcomm, and Qualcomm issuing shares to Amazon at a fixed ~$161 price — is **verified as real and closely accurate** (actual exercise price $161.26, essentially the "$161" cited). Treated in Section 3 below strictly as a **documented growth-modifier input** (Rule 0-compliant), not as an assumed revenue or moat fact.

### 2.3 Also folded in: fiscal Q3 2026 earnings (reported 2026-07-29), not yet reflected in the last QCOM session

Per Rule 9 and per this session's brief, Qualcomm's fiscal Q3 2026 results (quarter ended 2026-06-28) were pulled fresh, since the last evaluation (2026-07-24) predates them by 5 days. **Primary source: Qualcomm's own Q3 FY2026 earnings release** (Exhibit 99.1, `s204.q4cdn.com/.../FY2026-3rd-Quarter-Earnings-Release.pdf`, read directly in full — GAAP income statement, balance sheet, and cash-flow statement), cross-checked against `stockanalysis.com`'s TTM aggregates. Headline results: revenue $9.947B (−4% YoY), GAAP net income $2.002B (−25% YoY), driven by **industry-wide input-cost inflation** (wafer, assembly, packaging, memory) compressing GAAP operating income to $1.626B (down from $2.762B in Q3 FY2025, a 41% YoY decline) — management is raising Snapdragon chip prices (5–10%, called "double-digit" in some contexts) effective September 1, 2026 to offset this, framed explicitly as a **cost pass-through**, not a pricing-power move. [CNBC](https://www.cnbc.com/2026/07/29/qualcomm-qcom-earnings-report-q3-2026-.html), [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/qualcomm-q3-2026-earnings-profit-120521329.html), [AndroidAuthority](https://www.androidauthority.com/qualcomm-chip-price-increase-3691444/). This is a real, filed, negative fundamental development not reflected in the 2026-07-24 session and is folded into the TTM figures in Section 3 below.

Automotive and IoT continued to grow briskly: Automotive revenue **+61% YoY to $1.588B** (its 23rd consecutive quarter of double-digit YoY growth); IoT **+9% YoY to $1.830B**; combined Automotive+IoT +28% YoY — while Handsets fell **−20% YoY to $5.086B**. Management reiterated a target of $40B non-handset revenue by FY2029 and guided non-handset revenue growth to accelerate from 24% (FY2026) to >60% (FY2027).

---

## 3. Data Source Note

Qualcomm Incorporated is a US SEC filer (**CIK 0000804328**). This session's fundamentals were sourced from, and cross-validated across:

- **Qualcomm's own Q3 FY2026 earnings release** (Exhibit 99.1, primary source, read in full) — GAAP income statement, balance sheet, cash-flow statement for the quarter and nine months ended 2026-06-28, plus GAAP comparatives for the equivalent 2025 periods.
- **`stockanalysis.com`** (`/stocks/QCOM/financials/`) — used to cross-check TTM aggregates and to source FY2022–FY2025 annual figures not independently re-derived this session (reused, with the prior 2026-07-24 session's own SEC-XBRL cross-checks of those same annual figures, since they haven't changed).
- **The prior 2026-07-24 session's SEC-XBRL-reconstructed Q3 FY2025, Q4 FY2025, Q1 FY2026, and Q2 FY2026 quarterly figures** — reused as building blocks for this session's rolled-forward TTM window (these are historical, already-filed quarters that don't change between sessions; only Q3 FY2026 is new data this session, sourced fresh from the earnings release).
- **Qualcomm's SEC Form 8-K** (Item 3.02, filed 2026-09-08) — the Amazon warrant terms (Section 2.1).
- **Independent web search** (non-Telegram sources) — Amazon deal verification (Section 2.1–2.2), Q3 FY2026 earnings commentary, and updated moat-signal evidence (Section 4.2).

No required Phase 01 input was invented, estimated, or inferred from the triggering post.

### 3.1 TTM reconstruction (Q4 FY2025 → Q3 FY2026, rolled forward one quarter from the 2026-07-24 session)

The last evaluation's TTM window was Q3 FY2025 → Q2 FY2026. This session rolls the window forward to **Q4 FY2025 → Q3 FY2026** — replacing Q3 FY2025 (a strong quarter, GAAP operating income $2,762M) with Q3 FY2026 (the newly-reported, materially weaker quarter, GAAP operating income $1,626M, per Section 2.3). This is a genuine rolling-window effect, not a calculation error — flagged explicitly since it is the main driver of this session's lower Profitability/Margins sub-scores versus 2026-07-24.

| Line item ($M) | Q4 FY2025 (derived, from 2026-07-24 session's SEC-XBRL reconstruction) | Q1 FY2026 (from same) | Q2 FY2026 (from same) | Q3 FY2026 (fresh, this session's primary-source earnings release) | **TTM total** | Cross-check |
|---|---|---|---|---|---|---|
| Revenue | 11,271 | 12,252 | 10,599 | 9,947 | **44,069** | Matches `stockanalysis.com` TTM revenue ($44,069M) exactly ✓ |
| Operating Income (EBIT) | 2,918 | 3,366 | 2,309 | 1,626 | **10,219** | `stockanalysis.com` shows $10,426M TTM Op. Income — a $207M (~2%) discrepancy, likely a differing treatment of the "Other" opex line; this session uses the fully-reconciled SEC-primary build (below) as the figure of record, same precedent as the 2026-07-24 session preferring SEC XBRL over a discrepant vendor aggregate. |
| Pretax Income (EBT) | 2,971 | 3,547 | 2,232 | 2,462 | **11,212** | Internally consistent — see Net Income cross-check below. |
| Income Tax Expense (Benefit) | 6,088 | 543 | (5,138) | 460 | **1,953** | — |
| Net Income | (3,117) | 3,004 | 7,370 | 2,002 | **9,259** | Matches `stockanalysis.com` TTM net income ($9,260M) to within $1M rounding ✓ |
| D&A | 371 | 393 | 413 | 396 (derived: 9mo FY2026 D&A $1,202M − Q1+Q2 FY2026 $806M) | **1,573** | — |
| Gross Profit | 6,237 (derived: FY2025 annual $24,546M − 9mo-FY2025 $18,309M) | — | — | — (built from 9mo totals, see below) | **23,897** | Matches `stockanalysis.com` TTM Gross Profit ($23,897M) exactly ✓ |

**Internal consistency check:** TTM Pretax Income $11,212M − TTM Tax Expense $1,953M = **$9,259M**, exactly matching TTM Net Income built independently from the same quarterly rows. TTM effective tax rate = 1,953/11,212 = **17.42%**. TTM EBITDA = 10,219 + 1,573 = **$11,792M**.

**Gross Profit build:** 9-month FY2026 gross profit (from this session's primary-source income statement: Revenue $32,798M − Cost of Revenues $15,138M) = $17,660M. Q4 FY2025 gross profit (derived: FY2025 annual $24,546M − 9mo-FY2025 $18,309M, where 9mo-FY2025 = Revenue $33,013M − Cost of Revenues $14,704M, both primary-sourced from this release's prior-year comparison columns) = $6,237M. TTM Gross Profit = 17,660 + 6,237 = **$23,897M** — exact match to `stockanalysis.com`'s independently-reported TTM figure, strong cross-validation.

**FCF build:** 9-month FY2026 FCF (primary source: OCF $8,405M − CapEx $1,578M) = $6,827M. 9-month FY2025 FCF (OCF $10,016M − CapEx $785M) = $9,231M. FY2025 annual FCF (from `stockanalysis.com`, cross-checked in the 2026-07-24 session against its own FCF/NI-ratio internal consistency) = $12,820M. Q4 FY2025 FCF (derived) = 12,820 − 9,231 = $3,589M. **TTM FCF = 3,589 + 6,827 = $10,416M.**

**Balance sheet (as of 2026-06-28, most recent filed):** Cash $4,533M + Marketable securities (current) $3,771M = **liquid assets $8,304M**. Short-term debt $2,489M + Long-term debt $12,781M = **total debt $15,270M**. **Net debt = 15,270 − 8,304 = $6,966M.** Total stockholders' equity = **$27,658M**.

---

## 4. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29 — unchanged since the last session, no stale-score issue)

### 4.1 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | QCOM data (this session, rolling window) | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF by year: FY2022 $6,834M, FY2023 $9,849M, FY2024 $11,161M, FY2025 $12,820M, TTM (through 2026-06-28) **$10,416M** — positive every period shown. | **PASS** |
| **Net debt/EBITDA over threshold (2.5× standard)** | Net debt $6,966M ÷ TTM EBITDA $11,792M = **0.591×**. | **PASS — well under threshold.** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | FCF/NI by year: FY2022 **52.83%** (below 70%), FY2023 **136.2%**, FY2024 **110.0%**, FY2025 **231.4%**, TTM **112.5%** ($10,416M/$9,259M). Per the 2026-08-05 rolling-window clarification, the most recently completed fiscal years (FY2023–FY2025) plus TTM are all ≥70% — only the older FY2022 year falls below, not 2 consecutive recent years. | **PASS — does not fire.** |

No hard disqualifier fires — same as 2026-07-24.

### 4.2 Sub-scores (all six)

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | Net Margin (TTM) = 9,259/44,069 = **21.01%** → NetMargin_Component = clamp((21.01/30)×100) = **70.03**. NOPAT = TTM EBIT × (1 − eff. tax rate) = 10,219 × (1 − 0.1742) = **$8,438.8M**. Invested Capital = Total Debt ($15,270M) + Equity ($27,658M) − liquid assets ($8,304M) = **$34,624M**. ROIC = 8,438.8/34,624 = **24.37%** → ROIC_Component = clamp((24.37/30)×100) = **81.23**. Profitability_Score = (70.03+81.23)/2 = **75.63** (no FCF-positivity cap — 5 years positive). | **75.63** |
| **Margins (15%)** | Gross Margin (TTM) = 23,897/44,069 = **54.23%**. GrossMargin_Score = clamp((54.23/80)×100) = **67.79**. No +10 trend bonus — gross margin has been well above the 40% threshold throughout the lookback (FY2022 57.84% → TTM 54.23%, a continued mild multi-year *decline* driven by the input-cost inflation discussed in Section 2.3, not a below-threshold expansion). | **67.79** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $44,200M → FY2025 $44,284M, unchanged from the last session — FY2026 has not yet completed, fiscal year-end late September) = (44,284/44,200)^(1/3) − 1 = **+0.063%** → base = clamp((0.063/25)×100) = **0.25**. **Documented TAM-expansion/diversification evidence, now materially stronger and independently verified this session (not from the trigger post):** (1) the **Amazon/AWS multi-generational custom AI-inference-chip and optical-connectivity collaboration**, confirmed via Qualcomm's own SEC Form 8-K (Item 3.02, filed 2026-09-08) — a real, primary-source-verified new anchor-customer relationship in data-center AI, addressing exactly the "unproven diversification" gap flagged in the 2026-07-24 session (see Section 2.1–2.2). (2) **Automotive revenue +61% YoY** to $1.588B in Q3 FY2026 (23rd consecutive quarter of double-digit YoY growth) and **IoT +9% YoY** to $1.830B, even as handsets fell −20% YoY (Section 2.3) — an acceleration versus the figures cited in the prior session. Company guidance: non-handset revenue to $40B by FY2029, growth accelerating from 24% (FY2026) to >60% (FY2027). **+10 applied** (same modifier as 2026-07-24, now resting on stronger, more concrete evidence — the Amazon relationship is no longer merely a company narrative but an SEC-filed commercial commitment). *Flagged judgment call, same category as before: the AI200/AI250/AWS collaboration still has **zero disclosed revenue** to date (Section 2.2) — a reasonable reader could still argue for 0 instead of +10. Sensitivity check in Section 4.4 shows this does not change the gate outcome either way.* Growth_Score = 0.25 + 10 = **10.25**. | **10.25** |
| **Balance Sheet (15%)** | Net Debt/EBITDA = $6,966M / $11,792M = **0.591×** (Section 4.1). BalanceSheet_Score = clamp(100×(1−0.591/4)) = clamp(85.23) = **85.23**. | **85.23** |
| **Moat Signal (15%)** | See evidence table below — **1 of 5 signals** cleared the cited-evidence bar, unchanged from 2026-07-24 despite the new Amazon news (see reasoning below). (1/5)×100 | **20.00** |
| **FCF Quality (10%)** | FCF/NI (TTM) = 10,416/9,259 = **112.5%** → clamp(((1.125−0.40)/0.60)×100) = clamp(120.8) = **100.0**. | **100.00** |

**Moat signal evidence (re-checked this session, cited):**

| Signal | This session's check | Verdict |
|---|---|---|
| Market share stable/growing | **Freshly re-checked and still declining.** Counterpoint Research: Qualcomm's global smartphone chipset share fell from 27% (Q1 2025) to **23%** (Q1 2026), still behind MediaTek's 32% (down from 38%) — driven partly by rising memory costs and some flagship OEMs (Samsung) using in-house Exynos silicon instead of Snapdragon. [Counterpoint / phoneworld.com.pk, thetechoutlook.com]. No reversal of the erosion documented in the 2026-07-24 session. | **FALSE (unchanged)** |
| Brand premium | Qualcomm's own September 1, 2026 chip price increase (5–10%, called "double-digit" in some coverage) is explicitly framed by multiple outlets as a **pass-through of Qualcomm's own rising supply-chain costs** (wafer/packaging/memory), not evidence of volume-loss-free pricing power from brand strength — consistent with the framework's evidentiary bar (must show ASP-without-volume-loss or premium-vs-competitor pricing, not a cost pass-through). [AndroidAuthority, igorslab.de] | **FALSE (unchanged)** |
| Network effect | No two-sided marketplace/user-growth-driven-value mechanism applies to a chip design/licensing and (now) custom-silicon-supply business. | **FALSE (unchanged)** |
| Switching costs | **Unchanged, still TRUE.** The SEP ("no license, no chips") patent-licensing model remains the well-documented mechanism (Ninth Circuit, 2020). The new Amazon warrant structure (vesting tied to Amazon's continued purchases) is a *contractual incentive for Amazon to keep buying*, not a second independent moat signal — it reinforces the same "switching costs / lock-in" category already credited TRUE, rather than adding a new one. | **TRUE (unchanged)** |
| Scale cost advantage | MediaTek remains the larger unit-volume leader (32% vs. Qualcomm's 23%, Q1 2026) — the framework's bar (a documented per-unit cost gap *in the subject company's favor*) is still not met. | **FALSE (unchanged)** |

**Why the verified Amazon deal doesn't move the Moat score:** the new AWS relationship is real, SEC-confirmed, and directly relevant to the *Growth* sub-score's TAM-expansion evidence (credited above) — but Qualcomm's own press materials describe it as a "**planned-collaboration stage**" arrangement with no shipped product and no disclosed revenue yet. A moat signal requires a *durable, already-demonstrated* competitive advantage (stable share, proven switching costs, etc.) — a first-year, not-yet-revenue-generating customer win is evidence of a growth opportunity, not yet of a moat. This distinction is made explicitly rather than silently defaulting the new news into every favorable sub-score.

### 4.3 Final weighted Quality Score

```
Quality Score = (75.63 × 0.25) + (67.79 × 0.15) + (10.25 × 0.20) + (85.23 × 0.15) + (20.00 × 0.15) + (100.00 × 0.10)
              = 18.9075 + 10.1685 + 2.0500 + 12.7845 + 3.0000 + 10.0000
              = 56.9105 → 56.9 (rounded to nearest 0.1)
```

**56.9 < 80.0 — fails the gate**, by **23.1 points** — a decisive miss, and in fact a slightly *wider* miss than the 2026-07-24 session's 60.3 (19.7-point miss). This is not because the new Amazon/AWS news is unfavorable — it is real, verified, and the strongest documented Growth-modifier evidence QCOM has had in any session to date — but because the **same earnings cycle that produced this news also rolled a materially weaker quarter (Q3 FY2026, hit by industry-wide input-cost inflation) into the TTM window**, pulling Profitability (86.18→75.63) and Margins (68.50→67.79) down by more than the unchanged Growth/Moat scores could offset. Both effects are shown in full above — no black-box netting.

### 4.4 Sensitivity check (per the flagged judgment calls in 4.2)

- **Growth modifier removed** (0 instead of +10, i.e. treating the Amazon deal as still too early-stage to credit): Quality Score = 56.9105 − 2.00 = **54.9**. Still fails decisively.
- **Moat generously re-graded** (crediting 3 of 5 signals instead of 1): Moat_Score = 60.0, contributing 9.0 instead of 3.0 → Quality Score = **62.9**. Still fails.
- **Maximally generous Moat** (5 of 5 signals credited, the theoretical ceiling — e.g. crediting the still-declining Market-share signal and the cost-driven price increase as Brand-premium evidence, neither of which the evidence this session actually supports): Moat_Score = 100.0, contributing 15.0 → Quality Score = **68.9**. **Still fails the 80.0 gate even under the single most generous defensible reading of every discretionary call in this session** — and this ceiling (68.9) is itself *lower* than the 2026-07-24 session's most-generous ceiling (72.3), because of the Q3 FY2026 profitability rolldown described above.

**The Phase 01 FAIL outcome is robust to every discretionary call made in this session, including the maximally favorable treatment of the newly-verified Amazon/AWS news.**

### Result: **Phase 01 FAIL**

Per [operating-brief.md](../framework/operating-brief.md) and [quality-scoring.md](../framework/quality-scoring.md): a company scoring below 80.0 does not proceed to Phase 02. Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed this session.**

---

## 5. Recommendation

**PASS — does not clear the Quality Score gate.** No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — consistent with [fair-value-methodology.md](../framework/fair-value-methodology.md), none of that work is meaningful for a name that misses this framework's 80.0+ quality bar by more than 20 points. No position is opened; no limit order is recommended.

The triggering Telegram post's claim checks out — Qualcomm and Amazon have in fact struck a real, SEC-filed, multi-generational custom-AI-chip and optical-connectivity collaboration, with a warrant for Amazon to buy up to 25M QCOM shares at $161.26 (essentially the "$161" cited), vesting against up to $60B of future purchases. This is exactly the kind of new, verifiable, fundamentally-relevant information Rule 9 exists to catch, and it materially strengthens the Growth-modifier evidence this framework can cite for QCOM's data-center diversification story (now a filed commercial commitment, not just a company narrative). But the framework's Quality Score gate is not solely about the growth narrative — Qualcomm's core profitability took a real, filed hit in the same earnings cycle (Q3 FY2026 GAAP operating income fell 41% YoY on industry-wide input-cost inflation, with a price increase now underway that is explicitly a cost pass-through rather than pricing power), and its moat picture remains thin (1 of 5 signals, with the Market-share signal *still declining* per fresh Counterpoint data pulled this session). The combined effect is a Quality Score of **56.9 — actually a wider miss of the 80.0 gate than the prior session's 60.3**, robust across every sensitivity check run (54.9–68.9). QCOM remains **watchlist-only**: worth continued attention given the real strategic significance of an AWS anchor-customer relationship, but not yet a name this framework's quality bar supports evaluating for entry.

---

## 6. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 7. Next Review Trigger

- **Mandatory Rule 9 re-check:** Qualcomm's fiscal Q4 FY2026 earnings (guided revenue $9.7–10.5B), expected in the company's standard late-October/early-November reporting window (exact date not yet confirmed) — the first quarter to show whether the September 1 price increases are recovering margin, and whether any AWS-collaboration milestones (binding purchase orders, further warrant-vesting tranches, or early Data Center revenue) are disclosed.
- **Mechanical trigger:** Growth (10.25) and Moat (20.00) remain the dominant gaps to the gate, but this session shows **Profitability and Margins are not static tailwinds either** — a further margin/ROIC deterioration next quarter would widen the gap further even if Growth/Moat hold steady. The most direct paths to a materially different result: (1) the September price increases visibly restoring GAAP operating margin next quarter; (2) a binding AWS purchase order or disclosed Data Center revenue (would likely also newly support a Moat signal, once genuinely demonstrated rather than "planned-stage"); or (3) independently verifiable evidence of stabilizing (not just slowing-decline) overall smartphone-chipset unit share.
- **Other Rule 9 events:** a further guidance revision, management change, additional material M&A, or a >15% stock move with no identified cause (today's +3.4%–10% pop is a known, explained move, not an unexplained one).
- Absent any of the above, future Telegram mentions of QCOM should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## Glossary

- **8-K** — The "current report" a US public company must file with the SEC within days of a material event (e.g. an earnings release or, as in this session, a new securities issuance). Qualcomm's Amazon warrant was disclosed via an 8-K (Item 3.02) filed 2026-09-08.
- **10-K / 10-Q** — The annual / quarterly financial-disclosure report a US public company must file with the SEC.
- **CAGR (Compound Annual Growth Rate)** — The smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx (Capital Expenditure)** — Money a business spends on physical or capitalized long-lived assets.
- **CIK (Central Index Key)** — The SEC's unique numeric identifier for each EDGAR filer (Qualcomm's is 0000804328).
- **Composite Score** — This framework's 0.0–100.0 blend of Quality Score and Valuation Score (50/50); not computed this session since QCOM fails the Quality gate first.
- **D&A (Depreciation & Amortization)** — A non-cash expense spreading the cost of long-lived assets over time.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and profitability ratios.
- **Effective tax rate** — The actual percentage of pretax income paid as tax in a period — used here to convert TTM EBIT into NOPAT for the ROIC calculation.
- **EPS (Earnings Per Share)** — Net income divided by number of shares outstanding.
- **FCF (Free Cash Flow)** — Cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score — none fired for QCOM this session.
- **Invested Capital** — The total capital (debt + equity, netted for cash) deployed in a business — the denominator of this session's ROIC calculation.
- **Moat** — A durable competitive advantage (brand, network effect, switching costs, scale) protecting a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest, 100.0 = highest quality) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. QCOM scores 56.9 this session.
- **Rate Environment Gate** — The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield; not run this session since the Quality gate fails first.
- **ROIC (Return on Invested Capital)** — How efficiently a company turns the capital invested in it (debt + equity) into profit.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **SEP (Standard-Essential Patent)** — A patent covering technology unavoidably used by anyone implementing an industry standard; the basis of Qualcomm's "no license, no chips" model, credited as this session's one TRUE Moat Signal (switching costs).
- **TAM (Total Addressable Market)** — The total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used in this framework's Rate Environment Gate (fetched for completeness this session but not used, since Phase 01 failed first).
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure.
- **Warrant (commercial/vendor-incentive)** — A security giving its holder (here, a customer) the right to buy the issuer's stock at a fixed exercise price, tied to a commercial supply agreement. Qualcomm's SEC 8-K (2026-09-08) disclosed a warrant letting Amazon buy up to 25M QCOM shares at $161.26, vesting against up to $60B of future purchases of Qualcomm server-chip products.
- **XBRL (eXtensible Business Reporting Language)** — The SEC's structured, machine-readable data-tagging format for filed financial statements — the source of the SEC-reconstructed TTM building-block figures reused/extended in this session.

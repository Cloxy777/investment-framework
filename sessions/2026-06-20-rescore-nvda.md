# RESCORE — NVDA — 2026-06-20

**Task type:** RESCORE
**Date:** 20 Jun 2026
**10Y US Treasury Yield:** 4.46% (18 Jun 2026 — TradingEconomics/CNBC via web search)
**Rate Regime Modifier in effect:** +5 (10Y in the 3.5–5% bracket)
**Last review on record:** Score 62.2, Jun 2026 (the 2026-06-11 recompute onto the 0–100.0 scale of the 2026-06-07 baseline). Prior full data pull: [sessions/2026-06-07-rescore-nvda.md](2026-06-07-rescore-nvda.md).
**Purpose of this run:** first NVDA re-score applying the new **Upside/Downside Modifier** (Expected-Return Modifier), added to the valuation score 2026-06-20.

> Jargon decoded on first use throughout: FCF (free cash flow — cash left after operating costs and capital spending), NI (net income — accounting profit), EV/EBIT (enterprise value ÷ earnings before interest & tax — a debt-neutral earnings multiple), Fwd PE (forward price-to-earnings — price ÷ next-year expected earnings per share), PEG (PE ÷ earnings growth rate), MoS (margin of safety — discount to fair value), DCF (discounted cash flow), PW (probability-weighted), CAGR (compound annual growth rate), pp (percentage points), EY (earnings yield), R/R (reward-to-risk ratio), IRR (internal rate of return — the annualized return an investment implies).

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$210.69** | `yfinance` `regularMarketPrice` (intraday, 20 Jun 2026) |
| Prior close | $204.65 | `yfinance` |
| 52-week range | $142.03 – $236.54 | `yfinance` `fiftyTwoWeekLow/High` |
| Analyst consensus PT | mean **$298.93** / median $288 / high $500 / low $180 (59 analysts, "Strong Buy") | `yfinance` `targetMeanPrice` etc. |

**Source note:** the framework's preferred Rule 0 source — Interactive Brokers `get_price_snapshot` (conid 4815747, the US NASDAQ primary listing, resolved via `search_contracts`) — was **permission-denied** this session. Fell back to `yfinance` per the task's fallback chain. $210.69 is up +2.95% from the prior close of $204.65; this is well inside the day's normal range and not a Rule 9 (>15% move) event. NVDA sits ~11% below its 52-week high.

---

## 2. Data Gaps / Variance Flagged

| Item | Note |
|---|---|
| IBKR price snapshot | Permission-denied — used `yfinance` fallback (stated above). No data invented. |
| `yfinance` `info.freeCashflow` = $46.3B | This is a divergent/TTM figure and conflicts with the FY2026 cash-flow-statement FCF of **$96.7B** (which ties to the prior session and NVDA's reported numbers). Used the **statement** figure ($96.7B), not the `info` field. Flagged rather than silently picked. |
| 5yr PE reconstruction | Reconstructed from `t.get_earnings_dates` TTM-EPS × contemporaneous price (the auto method in valuation-scoring.md). n=20 quarters — full 5-year window, primary method available. |
| Fair-value scenarios | Bull/base/bear are my scenario construction anchored on **sourced** consensus targets (mean $298.93, median $288, 59 analysts) and the framework's multiples — not invented point forecasts. Bear is deliberately underwritten *below* the Street low (see §6). |

---

## 3. Inputs Collected (Standard Re-Score template)

**Sector:** Technology / Semiconductors — AI compute & data-center GPUs
**Current portfolio weight:** 5.47% (≈ $2,935 of $53,659 combined book — `holdings.md`, synced 2026-06-15)

| Item | Value | Source |
|---|---|---|
| Revenue (FY2026, ended Jan 2026) | $215.9B | `yfinance` `financials` |
| Operating income | $130.4B | `yfinance` |
| EBIT | $141.7B | `yfinance` `financials` |
| Net income | $120.1B | `yfinance` |
| Free cash flow (FY2026) | $96.7B | `yfinance` `cashflow` |
| Gross margin | 74.1% | `yfinance` `grossMargins` |
| Net margin | 63.0% | `yfinance` `profitMargins` |
| Operating margin | 65.6% | `yfinance` |
| ROIC (proxy: ROE) | 114% | `yfinance` `returnOnEquity` (far above 15% threshold) |
| Cash / Total debt | $53.2B / $12.8B → **net cash $40.4B** | `yfinance` |
| Shares outstanding | 24.221B | `yfinance` |
| Market cap | $5,103B | $210.69 × 24.221B |
| Enterprise value | $5,063B (= mktcap − net cash) | derived |
| Forward PE | 16.55× | `yfinance` `forwardPE` |
| Trailing PE | 32.26× | `yfinance` |
| 5yr avg PE | 56.5× (range 36.3×–122.3×, n=20 qtrs) | `yfinance` reconstruction |
| PEG (trailing) | 0.65 | `yfinance` `trailingPegRatio` |
| EV/EBITDA | 30.6× | `yfinance` |
| Revenue CAGR 3yr | ~100% (FY23 $27.0B → FY26 $215.9B; (215.9/27.0)^(1/3)−1 ≈ 100%) | derived from `yfinance` |
| FCF/NI conversion (FY26) | 80.5% (= $96.7B ÷ $120.1B); 4yr trend 80.5 / 83.5 / 90.8 / 87.2% | `yfinance` — passes >70% quality check |
| Dividend / yield | $1.00 / 0.47% | `yfinance` |
| FY26 buybacks | $40.1B | `yfinance` `cashflow` |
| 10Y Treasury | 4.46% | web search |

**Fundamental changes since last review (2026-06-07/11):** NVDA reported **Q1 FY2027 on 20 May 2026** (the latest earnings, captured in the PE series). The most visible change is that the **forward PE has compressed to ~16.5×** (from ~22.5× at the 2026-06-07 read) — earnings have grown into the price; the multiple is now near the *bottom* of the 5-year range. The China AI-chip-share narrative from the prior session has not re-escalated into a Rule 9 trigger. Next earnings: **Q2 FY2027 on 26 Aug 2026** (confirmed, after close).

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 16.55 = 6.04%
Spread = EY − 10Y Treasury = 6.04% − 4.46% = +1.58 pp
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** (+1.58 pp, just clears). → No +5 yellow-flag additive. This is an *improvement* vs 2026-06-07, when the test **failed** at −0.11 pp — driven entirely by the forward-PE compression to 16.5×.

**Step 2 — Rate Regime Modifier**
10Y = 4.46% → "3.5–5%" bracket → **Modifier = +5**

---

## 5. Full Score Calculation (raw weighted)

**FCF Yield — 40% weight**
```
FCF Yield = $96.7B ÷ $5,103B (mktcap) = 1.89%
FCF_Score = clamp(100 × (1 − 1.89/10), 0, 100) = 81.1
```
→ Contribution: 81.1 × 0.40 = **32.42**

**EV/EBIT — 25% weight**
```
EV      = $5,103B − $40.4B net cash = $5,062.8B
EV/EBIT = $5,062.8B ÷ $141.7B = 35.7×
EV/EBIT_Score = clamp((35.7 − 12)/23 × 100, 0, 100) = 100.0  (≥35× → cap)
```
→ Contribution: 100.0 × 0.25 = **25.00**

**Forward PE — 20% weight (fallback formula, 5yr avg available; folds in the Historical PE Modifier)**
```
Deviation% = (16.55 − 56.5) / 56.5 × 100 = −70.7%
FwdPE_Score = clamp(50 + (−70.7) × 2.5, 0, 100) = clamp(−126.7, 0, 100) = 0.0  (floor)
```
Forward PE 16.55× is ~71% below the 5-year average of 56.5× and below even the 5yr low of 36.3× — deepest possible "cheap" reading. (Do **not** add the ±10 Historical PE Modifier separately — the fallback formula already folds it in.)
→ Contribution: 0.0 × 0.20 = **0.00**

**PEG — 15% weight (Fast Grower — EPS growth >15% for 3+ yrs, Upgrade 3 applies)**
Fast-Grower test: EPS growth ran ~+145% then ~+65% over the last several years — clears the gate, PEG slot applies (no redistribution).
```
PEG = 0.65
PEG_Score = clamp((0.65 − 0.5)/2.0 × 100, 0, 100) = 7.5
```
→ Contribution: 7.5 × 0.15 = **1.12**

**Raw weighted score:**
```
= 32.42 + 25.00 + 0.00 + 1.12 = 58.55
```
**+ Rate Regime Modifier (+5) = 63.55** (before the Upside/Downside Modifier)

---

## 6. Upside/Downside Modifier (Expected-Return Modifier) — REQUIRED

**Step 1 — Scenario fair values (Rule 7), bear underwritten honestly for a peak-earnings cyclical-growth name:**

| Scenario | Wt | Fair Value | Rationale |
|---|---|---|---|
| Bull | 25% | **$380** | AI data-center capex super-cycle continues, modest multiple re-rating off the now-depressed 16.5× forward PE. Below the $500 analyst outlier. |
| Base | 50% | **$288** | Consensus-anchored (analyst median PT $288; mean $298.93, 59 analysts, Strong Buy). |
| Bear | 25% | **$135** | **Honest downside (Klarman: "what do I lose if I'm wrong" first).** AI-capex *digestion*: hyperscaler spend plateaus, forward earnings cut ~30–40% off the current trajectory **and** the multiple compresses to a cyclical-trough ~16×. This is set **below the Street low of $180** deliberately — a name this leveraged to peak-cycle earnings deserves a downside the sell-side won't print. Still ~36% below today's price. |

```
PW Fair Value = 0.25×380 + 0.50×288 + 0.25×135 = $272.75
Gap Upside %  = (272.75 ÷ 210.69) − 1 = +29.5%
```

**Step 2 — Annualize over catalyst window (Rule 10):**
Catalyst: Q2 FY2027 earnings 26 Aug 2026 (near-term data-center-trajectory read) within the broader ~2-year AI-capex-digestion question. No single catalyst closes the full gap, so use the **2-year** default.
```
Annualized gap = 29.5% ÷ 2 = +14.7%/yr
```

**Step 3 — Build E (expected annual return):**
```
Intrinsic growth   = +10.0%/yr   (DELIBERATELY CONSERVATIVE forward FCF/EPS CAGR — well below
                                   Street's mid-20s%/yr — to (a) honor the peak-cyclical-downside
                                   discipline this run demands, and (b) avoid double-counting the
                                   growth already embedded in the gap-to-fair-value above)
Shareholder yield  = +1.26%      (dividend 0.47% + net buyback yield 0.79% = $40.1B ÷ $5,103B)
E = 14.7 + 10.0 + 1.26 = +25.96%/yr
```

> **Double-count guard (shown explicitly):** the annualized gap (14.7%) is the *re-rating / mean-reversion* return as price moves to fair value; intrinsic growth is the business *compounding* fair value beyond that. They are conceptually distinct, so additive is correct per the spec — but because the base-case fair value ($288) is itself growth-driven, I used a conservative 10% intrinsic-growth input (vs ~25%+ Street) so I am not paying twice for the same growth. **Sensitivity:** even at 10%, E = 26% already exceeds the +25% full-credit threshold, so the modifier pins to its floor; at 15% or 20% intrinsic growth E = 31–36% and the modifier is unchanged. The result is robust to this input.

**Step 4 — Map E to modifier (hurdle H = 10%):**
```
E = 25.96% ≥ H → M = −15 × clamp((25.96 − 10)/15, 0, 1) = −15 × clamp(1.06, 0, 1) = −15 × 1.0 = −15.0
```
**Catalyst guardrail:** a documented catalyst + timeline exists within 18–24 months (Q2 earnings 26 Aug 2026; the 2-yr data-center-trajectory thesis) → upside credit is **not** capped at −5. Full upside applies.

**Upside/Downside Modifier = −15.0** (floor — strongly attractive expected return).

> **Why this fires, and why it's the point of this run:** the four raw sub-scores are 65–80% anchored on *current/trailing* valuation, and they net to 58.55 ("Hold / no new entry") — chiefly because EV/EBIT (35.7×) and FCF yield (1.89%) read rich on the *trailing* earnings base. But the **forward** picture is very different: forward PE has collapsed to 16.5× (bottom of the 5-year range) as earnings caught up to price, and 59 analysts still see ~37% upside to a $288 median. The Upside/Downside Modifier is exactly the forward dimension the raw score ignores — and even with an honest sub-Street bear case ($135), the probability-weighted expected return clears the hurdle decisively, so the modifier pulls the score down a full band.

---

## 7. Final Score & Action

```
Final Score = 58.55 (raw weighted) + 5 (Rate Regime) + (−15.0) (Upside/Downside) = 48.55 → 48.5
```

# Final Score: 48.5  →  Action band: BUY — Standard position (30.0–49.9, 3–5%)

**Prior score: 62.2 (HOLD — watch only). Action category CHANGED: HOLD → BUY-band.**

The move is entirely driven by (a) the forward-PE compression to 16.5× flipping the Rate Gate from fail to pass and (b) the new Upside/Downside Modifier crediting the strong forward expected return the trailing-multiple sub-scores miss.

---

## 8. Order Setup (BUY-band → required) — and why the practical action is still HOLD/no-add

**Fair value (Rule 3 triangulation, 40% DCF-style / 60% multiples):**
```
DCF-style (scenario PW FV)  = $272.75
Multiples (consensus mean/median avg) = $293.47
Blended Fair Value = 0.40 × 272.75 + 0.60 × 293.47 = $285.18
```
Fair value range **~$135 (bear) – $380 (bull), base case ~$285** (Rule 10 — a range, not a point).

| Order Setup item | Value |
|---|---|
| Valuation Score (incl. U/D modifier) | **48.5** (≤49.9 — qualifies to enter) |
| Expected annual return E / catalyst | **+26%/yr / 2-yr (Q2 earnings 26 Aug 2026)** |
| Upside/Downside Modifier applied | **−15.0** |
| Blended Fair Value | $285.18 |
| Margin of Safety (Score 30–49.9 band → 25–30%; used 28%) | 28% |
| **BUY PRICE (limit)** | **$205.33** |
| Primary Sell Target (= blended FV) | $285.18 |
| Bull-Case Trim Target ($380 × 0.90) | $342.00 |
| Stop Loss (Buy × (1 − 28%)) | $147.84 |
| **R/R at buy price** | **(285.18 − 205.33) ÷ (205.33 − 147.84) = 1.39:1** |
| R/R at live price $210.69 | 1.19:1 |
| Max $ risk (1.5% × $53,659) | $804.89 |
| Risk-based size | 14 sh ≈ $2,875 (5.36% of book) |
| Allocation cap (Score 30–49.9 band → 3–5%) | $2,683 (5%) |

> ### ⚠️ R/R gate fails — do NOT add at current levels
> Both R/R figures are **below the 2:1 minimum** (1.39:1 at the buy price, 1.19:1 at live). The reason is structural: an honest bear case ($135) forces a wide stop ($147.84, ~30% below the buy price and near the 52-week low of $142), while the upside to blended fair value ($285) is only ~$80 from a ~$205–211 entry. To reach 2:1 at the live price the stop would have to be at **$173.44** (−17.7%) — tighter than the 25–30% loss band this score allows, i.e. it would mean over-tightening the stop to manufacture the ratio. Per the order-setup rule ("R/R below 2:1 → wait for lower entry, find tighter stop, or pass"), **the correct response is to wait for a lower entry, not to enter here.**
>
> Separately, NVDA is **already at 5.47% of the book** — at/above the 3–5% standard-position cap for this score band. There is no room to add even if R/R cleared.

**Practical action: HOLD the existing 5.47% position — no add, no trim.**
- No **add**: R/R < 2:1 at current price *and* already at the band's allocation cap.
- No **trim**: score 48.5 is in the BUY band, nowhere near the 70+ trim bands; "fair value alone is not a sell" (Phase 05 anti-turnover posture).
- A buy-the-dip **limit at ~$205.33** would only become R/R-attractive (≥2:1) if price falls further (toward ~$190 or below); not actionable at today's $210.69.

This is the framework behaving as designed: the score *reclassifies* NVDA as a name worth owning/accumulating (BUY-band, strong forward expected return), but the entry-discipline gates (R/R, position cap) correctly stop a chase at today's price.

---

## 9. Next Review Trigger

Re-score NVDA on **whichever comes first**:
- **Next earnings — Q2 FY2027, 26 Aug 2026** (confirmed, after close) — the key data-center-trajectory read.
- **Quarterly Rate Environment Gate refresh** — July 2026 (10Y / regime modifier).
- **Rule 9 events:** any >15% move without a fundamental cause, a guidance revision, management change, material M&A, a credible short report, or a pullback toward the ~$190s that would make the $205.33 buy-limit R/R-attractive (≥2:1).

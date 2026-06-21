# RESCORE — NOW (ServiceNow, Inc.)

## 1. Session header
- **Task type:** RESCORE (single ticker)
- **Date:** 2026-06-20
- **10Y US Treasury yield:** 4.46% (last trading close 2026-06-18; markets closed Sat 2026-06-20) — source: CNBC / TradingEconomics via web search, cross-checked `^TNX` 4.451 via `yfinance`
- **Rate Regime Modifier in effect:** +5 (10Y in the 3.5–5% bracket — "capital has real cost")
- **Purpose of this run:** first NOW rescore applying the new **Upside/Downside Modifier** (Expected-Return Modifier) added to the valuation score on 2026-06-20.

**Live data (Rule 0 — fetched first, never inferred):**
| Item | Value | Source |
|---|---|---|
| Live price | **$95.04** | `yfinance` `currentPrice`, 2026-06-20 (prior close $95.48) — IBKR `get_price_snapshot` was permission-denied this session |
| 52-week range | **$81.24 – $211.48** | `yfinance` |
| Analyst consensus PT | mean **$141.98**, median **$137.50**, high $236, low $85 (44 analysts) | `yfinance` `targetMeanPrice` |
| Market cap | $98.0B | `yfinance` |
| Enterprise value (EV) | $95.26B | `yfinance` |

> **Rule 9 event flagged:** NOW has **de-rated ~55% from its 52-week high of $211** to $95.04, and is down from $110.90 at the 2026-06-07 baseline (a >15% move). This is itself a mandatory re-valuation trigger — which this session satisfies. Forward PE (price-to-earnings, the price you pay per $1 of next-year profit) has collapsed from 24.6× to **18.9×**.

## 2. Data gaps flagged
- **Portfolio $ value not freshly pulled** this session — position sizing below is expressed as a % cap, not a share count. (Orchestrator handles `holdings.md`.)
- **Net buyback %** not precisely sourced; ServiceNow pays no dividend and its modest repurchases are largely offset by stock-based-compensation dilution, so shareholder yield is taken as ~0% (conservative). Flag for precise sourcing at next touch.
- Prior 2026-06-07 NOW row carried a citation-recovery gap (items 5–12). This session **re-sources all scoring inputs fresh from `yfinance`**, closing that gap for the scored metrics.
- Jargon decoded on first use: FCF = free cash flow (cash left after running and reinvesting in the business); EV/EBIT = enterprise value to earnings before interest & tax (a debt-neutral profit multiple); PEG = price/earnings-to-growth (a P/E divided by the earnings growth rate — Lynch's "fair price for a grower" gauge); MoS = margin of safety (discount to fair value); R/R = risk/reward; CAGR = compound annual growth rate; pp = percentage points.

## 3. Rate Environment Gate
- **Step 1 — Earnings Yield Spread Test:** Earnings Yield (EY) = 1 ÷ 18.9 = **5.29%**. Spread = 5.29% − 4.46% (10Y) = **+0.83%**. +0.83% < +1.5% → **FAIL → +5 to score** (yellow flag, not a veto).
- **Step 2 — Rate Regime Modifier:** 10Y 4.46% → 3.5–5% bracket → **+5**.

## 4. Full score calculation

| Input | Value | Sub-score | Weight |
|---|---|---|---|
| FCF Yield | $5.108B ÷ $98.0B = **5.21%** | `100×(1−5.21/10)` = **47.88** | 40% |
| EV/EBIT | $95.26B ÷ $2.402B TTM EBIT = **39.7×** (FY2025 41.7×) | `(39.7−12)/23×100` → saturates → **100.0** | 25% |
| Forward PE | **18.9×** vs 5yr avg **67.8×** (range 23.1–122.8×) | dev −72.1% → `50+(−72.1)×2.5` → floors → **0.0** | 20% |
| PEG | **0.92** (Fast Grower confirmed — see below) | `(0.92−0.5)/2.0×100` = **21.0** | 15% |

- **Fast Grower check (Upgrade 3):** revenue 3yr CAGR = (13.278/7.245)^(1/3)−1 = **22.4%**; forward EPS growth ~17.5% (FY2026) and ~21.9% (FY2027) — comfortably >15% for 3+ years → **PEG sub-score applies** (15% weight retained).
- **EV/EBIT note:** TTM EBIT (sum of last 4 quarters) = $2.402B; the score saturates at 35× regardless — the underlying 39.7× remains informative (NOW is still richly priced on trailing operating profit even after the de-rating; GAAP operating margin is held down by heavy stock-based compensation, while FCF margin is ~37%).
- **FCF/NI conversion:** FCF consistently exceeds GAAP net income (ratio 1.6–2.6× over 2022–2025) — high-quality, cash-generative, no red flag.

**Raw weighted score** = 47.88×0.40 + 100.0×0.25 + 0.0×0.20 + 21.0×0.15
= 19.15 + 25.0 + 0.0 + 3.15 = **47.30**

## 5. Upside/Downside Modifier (Expected-Return Modifier) — REQUIRED

**Scenario-weighted fair value (Rule 7), anchored on FY2027 consensus EPS ~$5.03 (catalyst window ~2yr):**
| Scenario | Weight | EPS | Justified fwd PE | Fair value |
|---|---|---|---|---|
| Bull (AI/Now Assist monetization re-accelerates growth, re-rating) | 25% | $5.40 | 28× | $151 |
| Base (consensus ~20% grower, PEG ~1.0) | 50% | $5.03 | 22× | $111 |
| Bear (growth decelerates to mid-teens, de-rating persists) | 25% | $4.80 | 17× | $82 |

`PW Fair Value` = 0.25×151 + 0.50×111 + 0.25×82 = **$113.5**
(Sanity vs analyst median PT $137.50 / mean $141.98 — our PW FV sits **below** consensus, i.e. conservative. Bear case underwritten per Klarman/Guardrail 2.)

**Expected annual return `E`:**
- Gap Upside % = $113.5 ÷ $95.04 − 1 = **+19.5%**
- Annualized gap (Rule 10 catalyst window 2yr) = +19.5% ÷ 2 = **+9.7%/yr**
- Intrinsic growth (forward EPS/FCF CAGR, conservative) = **+18%/yr**
- Shareholder yield (no dividend; net buyback ≈ SBC dilution) = **+0%**
- `E` = 9.7% + 18% + 0% = **+27.7%/yr**

**Catalyst guardrail:** documented catalysts exist within 18–24 months (Now Assist / generative-AI monetization ramp, FY2027 earnings step-up, enterprise-workflow consolidation) → **full upside credit allowed** (no −5 cap).

**Map E → M** (hurdle H = 10%): E = 27.7% ≥ H, and (E−H) = 17.7pp > 15pp →
`M = −15 × clamp((27.7−10)/15, 0, 1) = −15 × 1.0 =` **−15.0** (floored at the bound).

> **Honesty note (forecast discipline):** the modifier saturates at the −15 bound because the de-rating (forward PE 18.9× vs 67.8× 5yr average, price down 55% from the high) plus ~18% intrinsic growth produce an E far above the 25%/yr full-credit threshold even before the re-rating gap. Because the base/bull/bear fair values are built on **forward (FY2027) EPS**, the +9.7% annualized gap and the +18% intrinsic-growth term carry a small element of overlap (both reflect forward earnings). Even applying a conservative haircut to intrinsic growth, E stays well above 25%/yr, so the floored −15 holds. The ±15 bound is doing exactly its designed job: it pulls a beaten-down, still-growing compounder down toward the entry bands but cannot, on its own, override the bottom-up cheapness gate.

## 6. Final valuation score + action

**Final Score** = raw 47.30 + Rate Regime +5 + EY-Spread Step 1 +5 + Upside/Downside −15.0 = **42.3**

- **Prior score:** 59.3 (2026-06-11 recalc; 2026-06-07 baseline on old 1–10 scale = "6")
- **Band:** 30.0–49.9 → **BUY — Standard position 3–5% / set limit order** (Cheap band; the de-rating + the new forward-aware modifier moved NOW out of the 50–69.9 "Hold, watch only" band it sat in at 59.3).
- **Action CHANGED:** YES — from "Hold, watch only" to the Standard-BUY band on the score. **BUT the order setup does not clear the entry gates at the current price (see below) — so no buy is executed; this is a limit-order/watch outcome, not a buy-now.**

## 6b. Order setup (BUY band → required)

| Item | Value |
|---|---|
| Valuation score (incl. modifiers) | 42.3 (≤49.9 ✔) |
| Expected annual return E / catalyst window | +27.7%/yr / ~2yr |
| Upside/Downside Modifier applied | −15.0 |
| Blended (PW) Fair Value | **$113.5** |
| Margin of Safety (Score 30–49.9 band) | 28% |
| **BUY PRICE (limit)** | **$81.72** |
| Primary Sell Target | $113.50 |
| Bull-case Trim Target | $135.90 (bull FV $151 × 0.90) |
| Stop Loss (28% below buy) | $58.84 |
| R/R at limit entry $81.72 | (113.5−81.72)/(81.72−58.84) = **1.39:1** ❌ below 2:1 |
| R/R at live price $95.04 | 0.51:1 ❌ (live price is *above* the buy limit — no MoS yet) |
| Position cap (band) | 3–5%; current weight 2.47% |

**Order decision:** Per Step 6 (R/R must be ≥ 2:1) the trade **does not clear the risk/reward gate** at either the live price or the $81.72 limit — the gap to a *scenario-weighted* fair value of $113.5 simply isn't wide enough to support 2:1 against a disciplined stop. **Do not initiate or add.** The buy limit ($81.72) also sits right at the 52-week low ($81.24), so even a fill there would not satisfy 2:1. 

**Net:** Hold the existing 2.47% position (thesis intact — 22% revenue growth, 76% gross margin, strong FCF conversion). The score has moved into the BUY band, but the order math caps action at "watch for a wider-margin entry." Revisit sizing only if price falls enough to restore ≥2:1 R/R against the $113.5 FV, or if a higher PW fair value is justified by FY2026/27 results.

## 7. Portfolio rebalancing summary
Not applicable (single-ticker rescore). No trim — score 42.3 is well below the 70.0 trim band. `holdings.md` update handled by orchestrator.

## 8. Next review trigger
- Next quarterly earnings release (Q2 FY2026, ~late July 2026) → standard rescore.
- Any further >15% move, guidance revision, or a price drop restoring ≥2:1 R/R against $113.5 FV → re-evaluate entry.
- Re-source precise net buyback % to refine the shareholder-yield term of the Upside/Downside Modifier.

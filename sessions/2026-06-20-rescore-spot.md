# RESCORE — SPOT (Spotify Technology S.A.)

## 1. Session Header
- **Task type:** RESCORE (single ticker)
- **Date:** 20 Jun 2026
- **10Y US Treasury yield:** 4.46% (CNBC/TradingEconomics, 18 Jun 2026) → **Rate Regime Modifier = +5** (3.5–5% bracket; "capital has a real cost")
- **Prior score:** 82.0 (Very Expensive, 80.0–89.9 → Trim to 50%), from [2026-06-11 new-scale rescore](2026-06-11-rescore-holdings-new-scale.md), itself derived from the [2026-06-07 full-portfolio baseline](2026-06-07-rescore-full-portfolio.md).
- **What's new this pass:** (a) Rule 0 fresh live price; (b) a **clean enterprise-value / net-cash figure** (the prior pass flagged EV≈market-cap as an approximation — now resolved); (c) first application of the **Upside/Downside Modifier** (Expected-Return Modifier) added to the score engine 2026-06-20.
- **Current portfolio weight:** 0.92% (per holdings.md / prior pass — not re-synced this session).

Jargon decoded on first use throughout: FCF (free cash flow — operating cash flow minus capital spending), EV/EBIT (enterprise value ÷ earnings before interest and tax), Forward PE (price ÷ next-12-months expected earnings per share), PEG (PE ÷ earnings growth rate), GAAP (the standard US/IFRS accounting basis), pp (percentage points), MoS (margin of safety), PW (probability-weighted), CAGR (compound annual growth rate), SBC (stock-based compensation), TTM (trailing twelve months), IRR (internal rate of return — the annualized return an investment implies).

## 2. Live Data First (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$468.08** | yfinance `currentPrice` (intraday, 20 Jun 2026). IBKR `get_price_snapshot` was attempted first per the prompt but the tool permission was denied, so the documented yfinance fallback was used. |
| Prior close | $455.60 | yfinance |
| **52-week range** | **$405.00 – $785.00** | yfinance `fiftyTwoWeekLow/High` |
| **Analyst consensus PT** | mean **$599.46** / median $600.92 (range $391.79–$721.86, 38 analysts) | yfinance `targetMeanPrice` etc. — consistent with the prior pass's $609–751 hand-sourced range; used only as a bull-case sanity check, never as fair value. |
| 10Y Treasury | 4.46% | CNBC / TradingEconomics, 18 Jun 2026 |

> Live price has **fallen ~5.4%** since the prior pass ($495.00 → $468.08), and sits in the lower third of its 52-week range (the stock is well off its $785 high). Per Rule 0 / the framework's non-negotiables, **price movement alone is not a trigger and does not by itself change the action** — the score below is what drives the recommendation.

## 3. Data Gaps & Flags (stated up front)
1. **PEG sub-score is NOT used (flagged).** SPOT only turned GAAP-profitable in **FY2024**; net income was **negative in FY2022 (−$430M) and FY2023 (−$532M)**, positive in FY2024 ($1,138M) and FY2025 ($2,212M) — only **~2 years of clean positive earnings**, not the 3+ years on a clean base the clarified Fast-Grower rule requires. The reconstructed trailing-PE series confirms the distortion: only 8 quarters of positive TTM EPS exist and the PE ranges wildly (41×–168×), far short of the 20 quarters (5 years) needed. **Per the clarified PEG-eligibility rule (2026-06-20) and the no-history FwdPE fallback, PEG's 15% weight is redistributed to EV/EBIT (→ 40%), and FwdPE_Score uses the neutral 50.0 placeholder.** No PE average is invented off the distorted short series.
2. **Gross margin 32.3% is below the Phase 01 >40% gate** — but this is a *known, long-standing structural feature* of music streaming (label royalties dominate cost of revenue), not a new deterioration. SPOT qualified historically on the "structurally expanding margins (3yr trend)" alternative limb of the gross-margin gate: gross margin has climbed from ~25% (FY2021/22) toward ~32% now. **The entire bull thesis — and the rich multiple — rests on this expansion continuing.** That is precisely the assumption the bear case below stresses.
3. **No metric invented.** EV/EBIT now uses a clean enterprise value (net **cash** of $5.82B = $6.29B cash − $0.48B debt), resolving the prior EV≈market-cap flag. FY2025 figures are USD as reported by yfinance (prior pass used EUR-converted figures; the EV/EBIT read is consistent at ~40×).

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
- Earnings Yield = 1 ÷ Forward PE = 1 ÷ 25.72 = **3.89%**
- Spread = 3.89% − 4.46% (10Y) = **−0.57%** → below the +1.5% threshold → **FAIL** → this is a yellow flag (a +5 add was the 2026-06-07 softening), but note: as a *held* position being scored for a trim/hold decision (not a new entry), the Step-1 flag raises the bar rather than blocking — and the score is already deep in the trim band. Per the prior pass's convention only the Step-2 Rate Regime Modifier (+5) is applied to the numeric score here; the Step-1 fail is recorded as context.

**Step 2 — Rate Regime Modifier:** 10Y 4.46% → 3.5–5% bracket → **+5** (applied to the score below).

## 5. Full Score Calculation (every sub-score shown)

**Inputs (all live / FY2025 filed, USD):**
- Live price $468.08 · Market cap $96.25B · Enterprise value $90.43B (net cash $5.82B)
- FCF (FY2025) = $2,872M → **FCF yield = 2,872 / 96,247 = 2.984%**
- EBIT (FY2025) = $2,255M → **EV/EBIT = 90,430 / 2,255 = 40.1×**
- Forward PE = 25.72× · Trailing PE = 31.25× · Forward EPS = $18.20
- Revenue: FY2025 $17.19B; 3yr CAGR (FY22→FY25) = 13.6% (decelerating — TTM growth 8.2%)
- ROIC proxy (ROE) ~38%; Net margin 15.4%; Net debt/EBITDA: negative (net cash) — Debt Gate passes trivially.

```
FCF_Score    = clamp(100 × (1 − 2.984/10), 0, 100)        = 100 × 0.7016   = 70.16
EV/EBIT_Score= clamp((40.1 − 12)/23 × 100, 0, 100)         = 122.18 → clamp = 100.00
FwdPE_Score  = 50.00   (no-history fallback — <20 quarters of clean TTM EPS; flagged)
PEG_Score    = n/a — redistributed (recently-profitable, distorted base; see §3)

Raw weighted (PEG's 15% → EV/EBIT, so EV/EBIT carries 40%):
   = (70.16 × 0.40) + (100.00 × 0.40) + (50.00 × 0.20)
   = 28.064 + 40.000 + 10.000
   = 78.064
+ Rate Regime Modifier (+5)                              = 83.064  (before Upside/Downside Modifier)
```

> The raw weighted score is **78.064** — essentially unchanged from the prior 77.04 raw (the cleaner net-cash EV slightly lowered EV/EBIT but it still clamps at 100; FCF yield ticked from 3.24% → 2.98% as FCF/market-cap moved). The pure-cheapness engine still reads SPOT as Expensive→Very Expensive.

## 6. Upside/Downside Modifier (Expected-Return Modifier) — REQUIRED

Built entirely from fair-value work (no new data source). **Scenario-weighted, downside underwritten honestly per the brief.**

**Scenario fair values** (anchored on forward EPS $18.20, with a justified exit PE per scenario; horizon ~2 years per Rule 10):

| Scenario | Wt | Assumption | EPS | Exit PE | Fair Value |
|---|---|---|---|---|---|
| **Bull** | 25% | Gross-margin expansion continues, price hikes stick, ad/marketplace monetization scales → EPS beats (~+15%), multiple holds premium | $20.93 | 32× | **$670** |
| **Base** | 50% | Steady, moderate margin gains; EPS ≈ forward consensus; still a premium growth multiple | $18.20 | 28× | **$510** |
| **Bear** | 25% | **Gross-margin gains STALL** (royalty cost leverage caps out, price-hike fatigue) → EPS misses (~−15%) **and** the growth multiple de-rates hard to a mature-platform 18× | $15.47 | 18× | **$278** |

```
PW Fair Value = 0.25×670 + 0.50×510 + 0.25×278 = 167.5 + 255.0 + 69.5 = $491.8
Gap Upside %  = (491.8 / 468.08) − 1 = +5.07%
Annualized gap (÷ 2yr catalyst window) = +2.53%/yr
Intrinsic growth rate = +10%/yr  (central estimate: TTM revenue growth has decelerated to 8.2%,
   3yr revenue CAGR 13.6%, near-term EPS growth high but normalizing — 10% is a defensible
   mid-cycle rate that does NOT lean on the rosy point)
Shareholder yield = 0%  (no dividend; recent buyback authorization roughly offsets historical
   SBC-driven dilution → treat as ~0%)

E = 2.53% (annualized gap) + 10% (intrinsic growth) + 0% (shareholder yield) = +12.53%/yr
```

**Catalyst & timeline (Rule 10):** documented catalyst exists — continued subscription **price increases** plus **ad-tier / marketplace monetization** driving the gross-margin expansion, realized over the next ~4–8 earnings reports (**18–24 months**). Because a catalyst is identifiable within the window, the **upside-side −5 guardrail cap does NOT bind** — the modifier may use the full computed value.

**Map E to M** (hurdle H = 10%, E ≥ H branch):
```
M = −15 × clamp((E − H)/15pp, 0, 1) = −15 × clamp((12.53 − 10)/15, 0, 1) = −15 × 0.1687 = −2.53
```

> **Sensitivity (honesty check, since the thesis rests on margin expansion the bear case challenges):** at intrinsic growth 8% → E = 10.53% → M = −0.5 → final 82.5; at 12% → E = 14.53% → M = −4.5 → final 78.5. **SPOT remains in the 70.0+ trim band across the entire plausible range.** This is exactly the behaviour the ±15 cap is designed for: a genuinely expensive name with a *decent* (~12.5%) forward expected return is **not** rescued out of the trim zone — because the honest bear case (FV $278, a ~−41% drawdown if margin gains stall) drags the probability-weighted fair value down to roughly today's price, so the gap-to-fair-value contribution to E is small (+2.5%/yr) and nearly all of E is just ordinary intrinsic growth, which a −2.5 modifier cannot offset against a 78-raw score.

## 7. Final Score & Action

```
FINAL = 78.064 (raw weighted) + 5 (Rate Regime) + (−2.53) (Upside/Downside) = 80.534 → round 0.1 → 80.5
```

**FINAL SCORE = 80.5 → Very Expensive (80.0–89.9) → TRIM to 50% of original size (Phase 05).**

- **Prior score 82.0 → now 80.5.** Same band (80.0–89.9), **same action category (Trim to 50%)** — **action UNCHANGED.** The 1.5-point dip is driven almost entirely by the new −2.5 Upside/Downside Modifier (the decent forward return earns a small discount) partly offset by the slightly lower FCF yield; the raw cheapness engine barely moved.

### Trim plan (Phase 05 — Score 80.0–89.9 → trim to 50% of original position)
- **Action:** reduce the SPOT position to **50% of its original size**. At a current ~0.92% portfolio weight, this is a small absolute trim (toward ~0.46%).
- **Recycle proceeds** into current Score 0.0–29.9 names only (per Phase 05 capital-recycling rule) — none identified in this single-ticker session; route to the next `/rebalance`.
- **Buy Price / Stop Loss / R-R / Position Size: not computed** — these are entry-risk constructs for *opening* a position; manufacturing them for a position being *reduced* would be a meaningless template fill (same reasoning as prior trim logs, consistent with the no-black-box rule).
- **Fundamental-trigger watch (would override the valuation read):** gross margin falling >3pp structurally, or 2+ consecutive quarters of guidance cuts on the margin-expansion path — either would escalate from "trim on valuation" toward a Phase 06 thesis review.

## 8. Next Review Trigger
- **Next SPOT quarterly earnings release** (standard re-score), **or** any Rule 9 event sooner: guidance revision, a structural gross-margin move (>3pp), management change, material M&A, or a >15% unexplained price move.
- At next pass, refresh the analyst PT and re-test whether SPOT has accumulated enough quarters of clean positive EPS (≥20 quarters of positive TTM EPS) to bring a real Forward-PE history (and possibly PEG) online instead of the 50.0 neutral placeholder.

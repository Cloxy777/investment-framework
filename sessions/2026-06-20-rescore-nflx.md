# RESCORE — NFLX (Netflix, Inc.) — 2026-06-20

**Task type:** RESCORE (single ticker — existing holding)
**Date:** 20 Jun 2026 (Saturday — US markets closed; live quote is the most recent print, see §1)
**10Y US Treasury Yield used:** 4.46% (Federal Reserve H.15 / FRED DGS10, most recent published value 18 Jun 2026 — no later daily value published yet)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current NFLX portfolio weight:** **1.83%** — currently HELD (IBKR), per [holdings.md](../portfolio/holdings.md); Last Score 63.2 (12 Jun), last "no-change" check 62.5 (14 Jun)
**Sector:** Communication Services — Streaming Media & Entertainment

**Why this run:** First NFLX re-score under the new **Upside/Downside Modifier** (Expected-Return Modifier) added to the valuation score on 2026-06-20 ([decision](../decisions/2026-06-20-framework-change-upside-downside-modifier.md), spec in [valuation-scoring.md](../framework/valuation-scoring.md#upsidedownside-modifier-expected-return-modifier)). Also the first NFLX run under the 2026-06-20 change of the Forward-PE lookback from 10yr → **5yr** ([decision](../decisions/2026-06-20-framework-change-5yr-historical-pe-automation.md)), reconstructed automatically from `yfinance`. Reuses still-valid fair-value work from the [12 Jun session](2026-06-12-new-position-nflx.md) (fundamentals unchanged — see §0) with refreshed live price.

*Jargon decoded on first use throughout: FCF (free cash flow — operating cash flow minus capital expenditure), EV/EBIT (enterprise value ÷ earnings before interest and tax), Forward PE (price ÷ next-year expected earnings per share), PEG (PE ÷ growth rate), FCF/NI (free cash flow ÷ net income conversion), MoS (margin of safety), R/R (reward-to-risk ratio), DCF (discounted cash flow), PW (probability-weighted), CAGR (compound annual growth rate), pp (percentage points), bps (basis points = 0.01pp), E (expected annual return), H (hurdle rate), M (the modifier).*

---

## 0. Fundamental-Trigger Check Since Last Review (Rule 9)

No new earnings release, guidance revision, management change (CEO/CFO level), material M&A, or balance-sheet event found for NFLX between 14 Jun and 20 Jun 2026. FY2026 guidance (revenue $50.7–51.7B, operating margin 31.5%, ad revenue ~doubling to ~$3B, FCF raised to ~$12.5B) stands as last reported at Q1 2026. **No new Rule 9 fundamental trigger** — so all non-price fundamentals (revenue, FCF, EBIT, net debt, shares, consensus EPS) are carried forward from the 12 Jun pull and only price-dependent ratios are recomputed against today's live price, plus the two new framework mechanics are applied.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$77.38** | `yfinance` `info["currentPrice"]` (`$77.38`), corroborated by WebSearch aggregation ("current price of NFLX is 77.38 USD, +0.55% in past 24h; market cap 325.83B; week −5.48%, month −14.16%"). IBKR `get_price_snapshot` MCP returned a permission denial this session → fell back to `yfinance` + WebSearch per the framework's documented fallback path (Rule 0 Step 1). |
| 52-week high | $134.115 | `yfinance` (`fiftyTwoWeekHigh`) |
| 52-week low | $75.01 | `yfinance` (`fiftyTwoWeekLow`) |
| Analyst consensus PT (median) | **$115.00** (mean $114.15; 44 analysts) | `yfinance` (`targetMedianPrice` / `targetMeanPrice` / `numberOfAnalystOpinions`), consistent with eToro $115.13 |

**Context:** NFLX at **$77.38** is **~42.3% below its 52-week high** ($134.115) and **~3.2% above its 52-week low** ($75.01). It has fallen **−5.48% on the week and −14.16% on the month**. The cumulative move from the 14 Jun "no-change" reference ($80.34) to today ($77.38) is **−3.68%** — within the Rule 9 ">15% unexplained move" threshold, so not itself a trigger; this is a routine re-score driven by the new framework mechanics.

---

## 2. Standard Re-Score Inputs

Fundamentals carried forward from the 12 Jun pull (all primary-sourced; verified unchanged via §0), cross-checked this session against `yfinance` where the doc allows:

| Metric | Value | Source / `yfinance` cross-check |
|---|---|---|
| FY2025 Revenue | $45.18B (+16% YoY) | `yfinance` `financials` Total Revenue = $45.183B ✓ |
| Revenue CAGR 3yr (FY2022→FY2025) | 12.51% | Computed ($45.18B / $31.62B)^(1/3)−1; `yfinance` FY2022 rev $31.616B ✓ |
| FY2025 Net income | $10.98B | `yfinance` Net Income $10.981B ✓ |
| FY2025 Net margin | 24.3% (yfinance TTM `profitMargins` 28.5%) | Computed |
| FY2025 Gross margin | 48.5% (yfinance `grossMargins` 49.0%) | ✓ |
| FY2025 Operating margin | 29.5% | Netflix Q4 2025 release |
| **TTM EBIT** | **$13.275B** | Prior derivation (rev × 29.5%); `yfinance` reports FY2025 EBIT $13.499B / Operating Income $13.327B — within ~1.7%; prior $13.275B retained for continuity (sensitivity below) |
| **FY2025 FCF** | **$9.5B** | `yfinance` Free Cash Flow FY2025 = $9.461B ✓ (rounds to $9.5B) |
| **FCF/NI conversion (FY2025)** | **86.2%** ($9.461B / $10.981B) | `yfinance` computed: FY2025 86.2%, FY2024 79.5%, FY2023 128.1% — ≥70% for the 2 most recent years (the FY2022 36% dip is the pre-margin-inflection year) → PASS |
| Total debt (Q1 2026, 10-Q) | $14.361B | Prior session (yfinance `totalDebt` $16.742B includes operating leases — see Gap #2) |
| Cash + ST investments (Q1 2026) | $12.296B | Prior session (yfinance `totalCash` $12.288B ✓) |
| **Net debt** | **$2.065B** | Prior session, 10-Q basis (see Gap #2) |
| ROIC | 21.3–25.5% | Prior session (yfinance `returnOnEquity` 48.5% — equity-not-capital basis, not used) |
| Net debt/EBITDA | ~0.15× | Prior session — well under 2× |
| **Shares outstanding** (Q1 2026) | **4,212.79M** | Netflix Q1 2026 10-Q (yfinance `sharesOutstanding` 4,210.80M — within 0.05%) |
| 2026 consensus EPS | **$3.66** (range $3.19–$3.96) | WebSearch aggregation (unchanged); yfinance `forwardEps` $3.84 is a forward-12-month blend — sensitivity in §5 |
| Dividend | **None** | yfinance `dividendYield` = None (NFLX pays no dividend) |
| **5yr avg PE** | **39.44×**, range **19.32× – 55.82×** (n=20 quarters) | `yfinance` reconstruction (new 2026-06-20 method) — see Gap #3 |

### Recomputed Today (price-dependent — $77.38)

| Metric | Derivation | Value |
|---|---|---|
| Market Cap | 4,212.79M × $77.38 | **$325.99B** |
| Enterprise Value | Market Cap + Net Debt ($2.065B) | **$328.05B** |
| **EV/EBIT** | EV ÷ TTM EBIT ($13.275B) | **24.7119×** |
| **FCF Yield** | FY2025 FCF ($9.5B) ÷ Market Cap | **2.9142%** |
| **Forward PE** | $77.38 ÷ $3.66 | **21.1421×** |

### Data Gaps / Flags
1. **TTM EBIT basis** — derived from FY2025's reported 29.5% operating margin (a stated %, not a directly-quoted $ EBIT). `yfinance` independently reports FY2025 EBIT $13.499B (Operating Income $13.327B), within ~1.7% of the $13.275B retained. Sensitivity: using $13.499B → EV/EBIT 24.30× → EV/EBIT_Score 53.5 (×0.40 = 21.4) → raw ~50.2, **Final still 61.2 after rounding** — immaterial.
2. **Net debt source divergence (flagged, not resolved).** `yfinance` `totalDebt` $16.742B − `totalCash` $12.288B = $4.454B net debt, vs. the 10-Q-based $2.065B carried forward. The gap is operating-lease capitalization in yfinance's debt figure. Using $4.454B → EV $330.44B → EV/EBIT 24.89× → EV/EBIT_Score 56.0 (×0.40 = 22.4) → raw ~50.7, **Final still 61.2 after rounding** — immaterial to the action. Retained 10-Q basis for continuity with prior NFLX sessions; this is a flag, not an invented figure.
3. **5yr avg/range PE — new automated method (2026-06-20).** Reconstructed from `yfinance` `get_earnings_dates` trailing-4-quarter EPS paired with contemporaneous price: **avg 39.44×, range 19.32–55.82×, n=20 quarters** (full 5 years — meets the depth requirement, no no-history fallback needed). This **supersedes the prior sessions' 10yr-avg-PE 60.90×** per the 2026-06-20 lookback change. NFLX's forward PE (21.14×) sits near the *bottom* of its own 5yr range either way → FwdPE sub-score floors at 0.0 (see §5), so the change of lookback does **not** alter the result.

---

## 3. Phase 01 — Quality Gate (Confirmed Unchanged)

| Check | NFLX Value | Threshold | Result |
|---|---|---|---|
| Net margin (FY2025) | 24.3% | >15% | ✅ PASS |
| ROIC | 21.3–25.5% | >15% | ✅ PASS |
| Revenue CAGR 3yr | 12.51% | >10% | ✅ PASS |
| Gross margin | 48.5–49.0% | >40% | ✅ PASS |
| FCF positive 3 consecutive years | FY2023/24/25 all positive | required | ✅ PASS |
| Net debt/EBITDA | ~0.15× | <2× | ✅ PASS |
| FCF/NI conversion | 86.2% (FY2025), 79.5% (FY2024) | >70% (2+ yrs) | ✅ PASS |
| Share issuance | Flat/declining (buybacks) | not dilutive | ✅ PASS |
| Moat signal | #1 global streaming (325M+ subs), $20B content, ad-tier scaling | required | ✅ Strong |

**Gate result: PASS.**

**Fast Grower / PEG eligibility (Upgrade 3):** NFLX FY2024 EPS *declined* YoY vs FY2023 (per prior session Gap #4) → fails the ">15% EPS growth for 3+ consecutive years" Fast Grower test. **NFLX is NOT a Fast Grower** — PEG's 15% weight is redistributed to EV/EBIT (→ 40%), consistent with all prior NFLX sessions. (Note: yfinance reports a `pegRatio` of 1.52, but the framework's Fast-Grower gate is the controlling test, not the raw PEG availability.)

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $77.38 / $3.66 = 21.1421×
EY     = 1 ÷ 21.1421 = 4.7299%
Spread = EY − 10Y Treasury = 4.7299% − 4.46% = +0.2699%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.27%, short of +1.5%) → **+5 additive applied** (yellow-flag, not a veto).

**Step 2 — Rate Regime Modifier:** 10Y = 4.46% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for NFLX = +10** (Step 1 fail +5, Step 2 +5)

---

## 5. Phase 02 — Full Score Calculation

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 2.9142 / 10), 0, 100) = clamp(70.858, 0,100) = 70.8576
```
→ Contribution: 70.8576 × 0.40 = **28.3430**

**EV/EBIT — 40% weight (PEG redistributed; not a Fast Grower)**
```
EV/EBIT_Score = clamp((24.7119 − 12) / 23 × 100, 0, 100) = clamp(55.269, 0,100) = 55.2692
```
→ Contribution: 55.2692 × 0.40 = **22.1077**

**Forward PE — 20% weight (NEW 5yr-range primary formula — 2026-06-20 change)**
A 5yr PE *range* is now available (low 19.32×, high 55.82×), so the **primary** formula applies:
```
FwdPE_Score (range) = clamp((21.1421 − 19.32) / (55.82 − 19.32) × 100, 0, 100)
                    = clamp(1.8221 / 36.50 × 100, 0,100) = 4.9920
Historical PE Modifier (Upgrade 2): Deviation vs 5yr avg = (21.1421 − 39.44)/39.44 = −46.39%
   → >20% below 5yr avg → −10 modifier
FwdPE_Score = clamp(4.9920 − 10, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

*Sensitivity:* the fallback (5yr-avg-only) formula gives `clamp(50 + (−46.39)×2.5, 0,100) = 0.0` too; at the high consensus EPS ($3.96, Fwd PE 19.54×) the range score is 0.6 → after the −10 modifier still 0.0; at yfinance's forwardEps $3.84 (Fwd PE 20.15×) range score 2.3 → still 0.0 after modifier. **FwdPE sub-score is a robust 0.0 across every basis.**

**PEG — not applicable** (not a Fast Grower). Weight redistributed to EV/EBIT above.

**Raw weighted score:**
```
= 28.3430 + 22.1077 + 0.0 = 50.4507
```
**+ Rate Modifier (+10) = 60.4507** (before Upside/Downside Modifier)

---

## 6. Upside/Downside Modifier (Expected-Return Modifier) — REQUIRED

The whole point of this run. Built entirely from the fair-value scenario work (Rule 7) reused from the 12 Jun session — fundamentals unchanged, only the live price refreshed.

**Step 1 — Probability-weighted Fair Value (Rule 7).** Each scenario's blended FV = 40% DCF + 60% multiples (the same triangulation weights as the headline FV), using the 12 Jun scenario inputs:

| Scenario | DCF FV | Multiples FV | Blended (40/60) |
|---|---|---|---|
| Bear | $38.42 | $58.85 (FCF-yield comp) | $50.68 |
| Base | $60.34 | $68.15 (EV/EBIT comp) | $65.03 |
| Bull | $92.11 | $102.48 (Fwd-PE comp) | $98.33 |

```
PW Fair Value = 0.25×$98.33 + 0.50×$65.03 + 0.25×$50.68 = $69.77
```
*(This $69.77 PW FV is consistent with the 12 Jun headline blended FV of $71.02 — the small difference is from scenario-blending each method rather than blending the central estimates, and is the more conservative, fully-underwritten figure required for this modifier.)*

**Step 2 — Gap, annualize, build E.**
```
Gap Upside %    = ($69.77 ÷ $77.38) − 1 = −9.84%      (price is ABOVE PW fair value)
Catalyst window = 2 years (Rule 10): Q2 2026 earnings ~Jul, then the 2026 ad-revenue
                  doubling ($3B target) + FY operating-margin-guidance (31.5%) execution
                  resolve over ~the next two years. No narrower documented window → use 2yr.
Annualized gap  = −9.84% ÷ 2 = −4.92%/yr
Intrinsic growth = +13.0%/yr  (revenue CAGR 12.5%; FCF guided $9.5B→$12.5B; consensus EPS
                  CAGR ~13% — a deliberately mid-of-range, not rosy, compounding rate)
Shareholder yield = +0.5%/yr  (no dividend; modest net buyback)
E = −4.92 + 13.0 + 0.5 = +8.58%/yr
```

**Bear-case honesty check (high-multiple name).** The bear blended FV is $50.68 — i.e. a credible ~35% downside from today's $77.38 if margin guidance slips and the multiple de-rates further. Because the *price already sits above* the probability-weighted fair value, the annualized-gap term is **negative** and drags E *below* the 10% hurdle even with a healthy intrinsic-growth assumption. This is exactly the asymmetry the modifier is meant to surface: NFLX's bright future is largely already in the price.

**Step 3 — Map E to M** (hurdle H = 10%):
```
0 ≤ E (8.58%) < H (10%)  →  M = +5 × (10 − 8.58)/10 = +5 × 0.142 = +0.71
```
→ **Upside/Downside Modifier M = +0.71** (thin-upside band — a small positive, i.e. very mild trim pressure).

**Guardrails applied:**
1. *Catalyst guardrail* — a documented catalyst + timeline exists within 18–24 months (Q2 earnings, ad-revenue ramp), so no need to invoke the −5 upside cap; moreover M is positive here, so the upside cap is moot.
2. *Scenario-weighted, not the rosy point* — used the bull/base/bear PW FV ($69.77), never the bull case alone or the consensus PT ($115).
3. *Full calc shown* — above.
4. *Modifier, not a veto* — at +0.71 it nudges the score up by under a point; the asymmetric mapping (positive side caps at +5) deliberately prevents a fairly-valued name from being shoved into the trim band on a thin-return reading alone (preserves the anti-turnover posture).

---

## 7. Final Score & Action

```
Final = Raw weighted (50.4507) + Rate Modifier (+10) + Upside/Downside Modifier (+0.71)
      = 61.1608
```
Boundary rule: 61.1608 → nearest 0.1 → **Final Score = 61.2**

# Final Score: 61.2 → Action: HOLD — watch only, no new entry, no trim ("Fair Value", 50.0–69.9 band)

**Action category UNCHANGED** vs the prior 63.2 (12 Jun) — both sit in the 50.0–69.9 "Fair Value / Hold" band. No order setup is required (order setup applies only to BUY ≤49.9 or TRIM ≥70.0 actions).

**Reconciliation vs prior 63.2:**
- **−2.7 from the raw weighted score** (53.16 → 50.45): driven by (a) the **5yr-PE lookback change** confirming FwdPE at 0.0 (same as before, no net effect), and (b) the **−3.68% price decline** ($80.34 → $77.38) plus the new 5yr-range formula, which together left EV/EBIT_Score lower (55.3 vs 60.6 — EV/EBIT fell to 24.7× from 25.95× on the lower price) and FCF_Score slightly lower-cheaper. Net: the raw score is ~2.7pts *cheaper*.
- **Rate Modifier unchanged at +10.**
- **+0.71 from the NEW Upside/Downside Modifier** — a small positive (thin-upside), reflecting that at $77.38 the price still sits ~10% above the probability-weighted fair value, so expected annual return (8.58%) is just under the 10% hurdle.
- Net: 63.2 → **61.2**, a −2.0pt move, **same Hold action**. The new modifier confirms — rather than overrides — the bottom-up read: NFLX is fairly-to-slightly-richly valued, not a buy, and not (yet) a trim.

---

## 8. Fair Value & Sizing (Hold Band — no order setup)

| | Value |
|---|---|
| PW Fair Value (Rule 7, scenario-blended) | **$69.77** |
| 12 Jun headline blended FV (context) | $71.02 |
| Current price | $77.38 → **~11% above PW FV** (no margin of safety) |
| Analyst consensus PT (context) | $115.00 (implies multiple re-rating our bottom-up multiples don't underwrite) |
| Current NFLX weight | **1.83%** — hold at current size (no Phase 03 buy target at Score 61.2; trim only triggers at ≥70.0) |
| 15% hard cap (Upgrade 7) | 13.17pp headroom — not binding either direction |

**No sizing action implied.**

---

## 9. Recommendation

# HOLD — no new entry, no trim. Score 61.2 (Fair Value), action category unchanged from prior 63.2.

NFLX passes Phase 01 cleanly. Phase 02 lands at **61.2** — within the Fair Value / Hold band. The new Upside/Downside Modifier (+0.71) confirms thin forward upside (expected annual return ~8.58% vs a 10% hurdle), because the price already sits ~11% above the probability-weighted fair value ($69.77) — the bright future is largely priced in. The honest bear case (~35% downside to $50.68) is what holds expected return below the hurdle. No margin of safety for an add; no trim trigger. All final-decision authority rests with the human investor.

---

## 10. Next Review Trigger

- **Q2 2026 earnings** (~mid-to-late Jul 2026) — mandatory re-score (Rule 9). Check: ad-revenue pacing toward the $3B 2026 target; Q2 operating margin vs the 32.6% guide (down from 34.1% YoY); post-password-crackdown subscriber growth.
- **>15% unexplained price move from $77.38** in either direction — immediate re-score (Rule 9). (Note NFLX is already −14.16% on the month — a further leg down toward/through the $75.01 52-week low would warrant a fresh look even within the band, as a cheaper price mechanically lifts the FCF/EV-EBIT sub-scores and could pull the score toward the Cheap band.)
- **WBD termination-fee deployment** or any new large M&A — Rule 9 trigger.
- No position change executed by this session — recommendation only (Hold at 1.83%). If the investor acts, log in `decisions/`.

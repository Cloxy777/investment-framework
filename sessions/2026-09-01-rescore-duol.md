# RESCORE — DUOL (Duolingo, Inc.) — 2026-09-01

**Task type:** RESCORE (mode `--both`)
**Date:** 01 Sep 2026
**10Y US Treasury Yield:** 4.75% — U.S. Treasury daily par yield curve, most recent published business-day close (2026-08-31; 2026-09-01 is Labor Day, a US market holiday, so no newer print exists yet).
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current DUOL portfolio weight:** 8.94% per [holdings.md](../portfolio/holdings.md) (as of the most recent sync, predating today's price move — a precise updated weight requires the next `/sync-portfolio` pass, out of scope for this rescore; today's price move mechanically raises DUOL's true current share of the portfolio above 8.94%).
**Sector:** Technology — Education Software (EdTech / Language Learning)
**Last review:** 06 Aug 2026 (Valuation Score 72.2, Quality Score 83.2, Composite Score 44.5).

**Why this session fired:** Hourly `/telegram-scan` (Routine 6) flagged a new top post on the tarasguk channel (#11812, 2026-09-01T11:06:59 UTC): *"👅 Марк Махейні підвищив таргет по $DUOL до $210"* ("Mark Mahaney raised his price target on $DUOL to $210"). Per Rule 0, this post's claim was **never used as a scoring input or independently relied upon** — a general web check for corroborating coverage of this specific analyst call was inconclusive (no independent article surfaced this session), so it is logged here purely as the *reason the ticker was looked at*, not as a verified fact. What actually triggers this rescore is independent: DUOL's live price, fetched fresh via IBKR (Rule 0), is **$158.50** — a **+28.44%** move from the $123.42 price last used in the 08-06 review. This clears both (a) DUOL's own documented "Next review trigger" (*">15% unexplained price move from $123.42 in either direction"*) and (b) [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 9's standing trigger (*">15% move in stock price without a fundamental trigger"*) — a **mandatory re-valuation**, independent of whatever the Telegram post said. No new earnings/8-K has been filed since 08-06 (next print, Q3 FY2026, is expected ~early November 2026) — so this is a **price-only, market-drift-driven re-score**, not a fundamentals re-score.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$158.50** | IBKR `get_price_snapshot` (contract_id 505002183), real-time last trade, 2026-09-01 12:17:16 UTC. Change field: +$10.14 (+6.83%) vs. prior close — today's own move is meaningfully positive on top of the multi-week run since 08-06. |
| Cumulative move since last review | **+28.44%** ($123.42 → $158.50) | Computed this session. |
| 52-week range | $87.89 – $468.00 (as of 08-06; not refreshed this session — today's high may extend the 13/26-week range but doesn't change the 52-week extremes materially) | Carried forward from 08-06 IBKR `misc_statistics`; not re-pulled this session (price-only trigger, no new fundamental data needed for this field). |

**No price-inference shortcuts taken** — live price fetched first per Rule 0, before any valuation math.

---

## 2. Data Gathered — Sources & Gaps

**Tooling note:** `yfinance` was again **non-functional this session** — `t.info` failed with the same `SSLError('Failed to perform, curl: (35) Recv failure: Connection reset by peer')` through the environment's egress proxy seen in the 08-06 session (confirmed via the proxy's own status endpoint: repeated `ws_closed_mid_exchange` failures against `query2.finance.yahoo.com`, `fc.yahoo.com`, `guce.yahoo.com` — this looks like a persistent, recurring block on Yahoo's endpoints specifically, not a one-off). No fundamentals were re-pulled from Yahoo this session as a result.

**Why that's acceptable this session:** no new SEC filing/quarter has been reported since the 08-06 rescore (confirmed: DUOL's own next-earnings date remains ~early November 2026, unreached). Every trailing-twelve-month fundamental input (TTM Revenue, Gross Profit, EBIT, EBITDA, FCF, Net Income, diluted shares, Net Debt, Total Equity, Revenue 3yr CAGR, moat-signal evidence) is therefore **identical to the 08-06 session's independently SEC-XBRL-sourced figures** and is carried forward unchanged rather than re-fetched or re-estimated — consistent with "never invent or estimate financial data" (there is nothing to re-estimate; the underlying filed numbers have not changed). Only the **market-price-dependent quantities** (market cap, FCF yield, EV/EBIT, Forward PE spread, WACC weights, and every Upside/Downside Modifier component that depends on live price) are recomputed below against today's $158.50.

**10Y Treasury yield** — refreshed this session (was stale-fetch-blocked in prior attempts against FRED/CNBC/MarketWatch, all returning 403s through the proxy): U.S. Treasury's own daily par-yield-curve CSV (`home.treasury.gov`) fetched directly, most recent row **2026-08-31: 10 Yr = 4.75%** (up from 4.63% on 08-06, roughly flat/modestly higher — not a regime change).

No data gaps that block this session — every input needed is either carried forward (unchanged fundamentals) or freshly fetched (price, 10Y yield) this session.

---

## 3. Quality Score

**Carried forward unchanged from 08-06: Quality Score = 83.2.** No new fiscal quarter has reported since that session, so every sub-score input (profitability, margins, growth, balance sheet, moat evidence, FCF quality) is identical — recomputing would reproduce the same arithmetic against the same numbers. Hard disqualifier checks re-confirmed as still passing on the same (unchanged) rolling TTM window:

| Check | Value (unchanged since 08-06) | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs? | FY2023 870%, FY2024 298%, FY2025 87.1% | disqualify if <70% for 2+ yrs w/o growth-capex explanation | ✅ PASS |
| Net Debt/EBITDA over threshold? | −6.33× (net cash) | disqualify if >2.5× (standard) | ✅ PASS |
| FCF-positive 3+ consecutive years? | FY2022–FY2025 all positive, FY2026 TTM $397.5M | disqualify if not | ✅ PASS |

**Quality Score = 83.2 — clears the 80.0+ gate**, comfortably. No Phase 04 Quality Watch escalation.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test.** DUOL's Forward PE remains a **no-history fallback** for scoring purposes (§5) — same structural, ticker-specific data-depth limitation established in every prior DUOL session (short public history, GAAP-loss years 2021–2022 breaking the 5yr reconstruction). For Step 1 only, the same sourcing convention as 08-06 is used: the last independently-fetched Yahoo forward-EPS estimate (~$6.18, implied from 08-06's Yahoo forward PE of 19.96× at the then-price of $123.42) is held constant — a reasonable assumption since analyst forward-EPS estimates don't mechanically reprice with the stock the way the PE ratio itself does — and re-divided into today's live price:

```
Implied forward EPS (held constant) = $123.42 / 19.96 = $6.183
New forward PE = $158.50 / $6.183 = 25.63×
EY = 1 / 25.63 = 3.90%
Spread = 3.90% − 4.75% (10Y) = −0.85%   (< +1.5% threshold)
```

**FAILS Step 1 → +5 additive.** (Every candidate forward-PE reading already failed this test in 08-06 at a lower price; a 28% price increase against a roughly-flat EPS estimate only pushes the earnings yield further below the 10Y — this conclusion doesn't depend on exactly which vendor's EPS figure is used.)

**Step 2 — Rate Regime Modifier.** 10Y = 4.75% → 3.5–5% bracket → **+5**

**Combined Rate Modifier: +10**

---

## 5. Valuation Score (Phase 02)

### FCF Yield (40% weight)

```
Market Cap = $158.50 × 50,031,000 diluted shares = $7,929,913,500
FCF Yield  = $397,504,000 (TTM, unchanged) / $7,929,913,500 = 5.013%
FCF_Score  = clamp(100×(1 − 5.013/10), 0, 100) = 49.87
```

### EV/EBIT (weight 25% base, redistributed to 40% — PEG still not applicable, see below)

```
EV = Market Cap $7,929,913,500 + Net Debt (−$1,094,751,000, unchanged) = $6,835,162,500
EV/EBIT = $6,835,162,500 / $157,085,000 (TTM EBIT, unchanged) = 43.51×
EV/EBIT_Score = clamp((43.51 − 12)/23 × 100, 0, 100) = 137.0 → capped at 100.0
```

DUOL's EV/EBIT has moved from 32.34× (08-06, at the then-price) to 43.51× today, purely on the price move — now above the score curve's own 35× cap, so this sub-score sits at its maximum regardless of the exact multiple.

### Forward PE + Historical PE Modifier (20% weight)

**No-history fallback again applied** (see §4) — same structural limitation reconfirmed, not re-tested this session (tooling to rebuild the 5yr PE series, `yfinance`, was unavailable — see §2):
```
FwdPE_Score = 50.0 (neutral midpoint, flagged)
```

### PEG (15% weight) — Fast-Grower eligibility unchanged

No new quarter has reported since 08-06, so the EPS-distortion/short-history reasoning that disqualified DUOL from Fast-Grower PEG treatment is unchanged. **PEG's 15% weight is again redistributed to EV/EBIT (→ 40%).**

### Raw Weighted Score

```
Raw = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.40) + (FwdPE_Score × 0.20)
    = (49.87 × 0.40) + (100.0 × 0.40) + (50.0 × 0.20)
    = 19.95 + 40.00 + 10.00
    = 69.95
```

---

## 6. Upside/Downside Modifier (Expected-Return Modifier)

**Methodology note:** same EV/EBIT scenario-ladder basis as 08-06 (Method B, unambiguous filed GAAP multiple), reusing the **same Bull (40×) and Bear (18×) scenario multiples** against the **same, unchanged TTM EBIT ($157,085,000) and Net Debt (−$1,094,751,000)** — since no new quarter has reported, the dollar fair-value outputs of the Bull and Bear scenarios are numerically identical to 08-06's. The Base case, by this method's construction, is always "today's actual multiple" — which by definition equals the live price.

| Scenario | Wt | EV/EBIT multiple | FV/share | Note |
|---|---|---|---|---|
| Bull | 25% | 40× | **$147.47** | Unchanged from 08-06 — same EBIT/net debt/shares |
| Base | 50% | 43.51× (= today's actual) | **$158.50** | = live price, by construction |
| Bear | 25% | 18× | **$78.40** | Unchanged from 08-06 — same EBIT/net debt/shares |

```
PW Fair Value = 0.25×147.47 + 0.50×158.50 + 0.25×78.40 = $135.72
Gap Upside % = 135.72 / 158.50 − 1 = −14.37%   (now a materially negative gap — the price run-up has moved
                                                  DUOL from modestly rich (08-06: −4.25%) to more clearly rich
                                                  on this scenario-weighted basis)
```

**Step 2 — catalyst & annualization (Rule 10).** Same 2-year (24-month) default catalyst window as 08-06 (no narrower, newly-documented catalyst this session — the triggering post is an analyst price-target note, not a dated company event):
```
Annualized gap = −14.37% / 2 = −7.19%
```

**Step 3 — expected annual return E.** Same judgment inputs as 08-06, carried forward unchanged since no new fundamental evidence has emerged this session to revise them:
```
E = annualized gap (−7.19%) + intrinsic growth (8%, unchanged judgment) + shareholder yield (−1%, unchanged judgment)
  = −7.19 + 8.0 − 1.0 = −0.19%
```

**Step 4 — map E to M** (hurdle H = 10%): E is (barely) negative:
```
E < 0 → M = +5 + 10 × clamp((0.19)/10, 0, 1) = 5 + 10×0.0187 = +5.19
```
**Upside/Downside Modifier M = +5.19.**

---

## 7. Final Valuation Score

```
Final Score = Raw Weighted (69.95) + Rate Modifier (+10) + Upside/Downside Modifier (+5.19)
            = 85.14 → rounds to 85.1
```

**Valuation Score = 85.1 — standalone "TRIM to 50% of original size" band** (80.0–89.9), two full bands worse than 08-06's 72.2 ("Trim 25–30%") and three bands worse than 07-04's 56.6 ("Fair Value") — entirely a live-market-drift effect (the +28.44% price move), not a fundamentals change. This raw-score read is superseded by the Composite Score below, per the framework's standing instruction to act on Composite once a Quality Score exists — shown next.

---

## 8. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 83.2) + 0.50 × 85.1
                = 8.40 + 42.55
                = 50.95 → rounds to 51.0
```

**Composite Score = 51.0 — "HOLD" band** (50.0–69.9), a **band change** from 08-06's 44.5 ("Cheap") — DUOL's blend has crossed out of the buy-eligible Cheap band into Hold, driven entirely by the price run-up (raw Valuation Score's move), since the Quality Score half of the blend hasn't moved.

**⚠️ Flagged: this result sits close to the Cheap/Hold boundary (49.9/50.0) and is worth a robustness check**, per "no black box." Re-running §6's Step 3 judgment inputs across a reasonable range:

| Sensitivity | E | M | Final Valuation Score | Composite Score | Band |
|---|---|---|---|---|---|
| Primary (8% growth, −1% shareholder yield, 2yr window) | −0.19% | +5.19 | 85.1 | **51.0** | Hold |
| Conservative growth (6% growth) | −2.19% | +7.19 | 87.1 | 52.0 | Hold |
| Optimistic growth (10% growth) | +1.81% | +4.10 | 84.0 | 50.4 | Hold |
| Flat shareholder yield (0% instead of −1%) | +0.81% | +4.60 | 84.5 | 50.7 | Hold |
| Narrower catalyst window (18mo instead of 24mo) | −2.58% | +7.58 | 87.5 | 52.2 | Hold |

**Every disclosed sensitivity stays inside the 50.0–69.9 Hold band** — the boundary-crossing conclusion (Cheap → Hold) is robust to reasonable variation in the modifier's judgment inputs, even though the exact Composite number (50.4–52.2) moves around some. None of the tested variations comes close to re-entering the Cheap band (would require Composite <49.95, i.e. Valuation Score <83.1 — a materially different price or EBIT read than anything tested here).

---

## 9. Action Recommendation

Composite Score 51.0 falls in the **50.0–69.9 "HOLD — watch only, no new entry, no trim"** band.

**No add:** already true at 08-06 (position >>1.6× the "Cheap" band's 3–5% target) and more true now — the price move alone increases DUOL's actual current portfolio weight above the recorded 8.94%, and the Composite Score no longer even reads Cheap. No margin of safety exists in the Hold band by definition (per [fair-value-methodology.md](../framework/fair-value-methodology.md) Step 2's integration table: Score 50.0–69.9 → "No MoS → Watchlist only").

**No trim:** despite the raw Valuation Score (85.1) sitting deep in the standalone Trim-to-50% band, the Composite Score — which the framework is explicit governs the action table once a Quality Score exists — stays inside Hold (50.0–69.9, below the 70.0 Trim threshold), and this conclusion is robust across the sensitivity table above. DUOL's strong, unchanged Quality Score (83.2) is doing the work keeping the blend out of Trim territory even as the raw cheapness read has deteriorated sharply.

**No exit trigger:** no fundamental deterioration this session (nothing has changed since 08-06's clean read — margins intact, ROIC far above WACC, pristine net-cash balance sheet, no dilutive raise, no covenant breach, no management change, no M&A). Today's move is a pure re-rating on sentiment (an analyst PT note, per the triggering post), not a fundamental Rule 9 event in its own right — only the *price magnitude* itself is the Rule 9 trigger, and that trigger's job (forcing a fresh look) is discharged by this session, not by any action.

### Fair Value reference (not gating an order — action is HOLD, not BUY/TRIM)

Shown for transparency per "no black box," not because an order is contemplated:

```
DCF Fair Value (Method A, WACC updated to 9.09% — 10Y 4.75% + Beta 0.88 × ERP 5.0% = 9.15% cost of equity,
  blended with unchanged 3.95% after-tax cost of debt at today's market-cap-based weights):        $188.69
Multiples-Based Fair Value (Method B, PW Fair Value, §6):                                           $135.72
Blended Fair Value (40% DCF / 60% Multiples, Rule 3 Tech/Growth weights):                            $156.91
```

**Notable: live price ($158.50) is now within ~1% of the framework's own Blended Fair Value ($156.91)** — a striking change from 08-06, when the blended FV ($147.83) sat well below the then-price ($123.42 relationship was inverted the other way — price below blended FV at that time only on the DCF side, itself a tension flagged in that session). The stock has moved from "modestly rich on Method B, cheap on Method A" (08-06) to "essentially at the framework's own blended estimate" today. No order setup (Buy Price / Stop Loss / R/R) is computed, consistent with the Hold action and fair-value-methodology.md's Step 2 rule that a Score 50.0–69.9 read gets no Margin-of-Safety-based order at all.

### Net Action: **HOLD** — maintain the current DUOL position as-is (no add, no trim)

---

## 10. Next Review Trigger

**Date/event:** DUOL's Q3 FY2026 earnings release (expected ~early November 2026) — mandatory Rule 9 re-score, unchanged from 08-06's checkpoints: **Q3 revenue growth vs. the 11.1% YoY guide**, **DAU growth staying above 20%**, **gross margin ~71.0% in Q3**, and whether the **buyback pace begins to net-offset dilution**. Also standard triggers: any further guidance revision, management change, M&A, or a **>15% unexplained price move from today's $158.50** in either direction (this session's own trigger — a fresh 15% band reset from the new reference price, per the same Rule 9 mechanism that fired this session).

---

## Glossary

- **Beta**: A stock's sensitivity to overall market moves; an input to DUOL's cost-of-equity/WACC calculation, unchanged (0.88) from prior sessions.
- **Composite Score**: This framework's blended 0.0–100.0 ranking number — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — computed only after a company clears the 80.0+ Quality Score gate. Governs the action table over the raw Valuation Score once both exist; this session it crossed from the Cheap band into the Hold band.
- **DCF (Discounted Cash Flow)**: A valuation method estimating a company's worth today by projecting future cash flows and discounting them back to the present.
- **EBIT**: Earnings Before Interest and Taxes.
- **EV**: Enterprise Value — market cap + debt − cash.
- **EV/EBIT**: Enterprise Value ÷ EBIT, a valuation multiple independent of capital structure; this session's primary Method B basis.
- **EY (Earnings Yield)**: 1 ÷ Forward PE, compared against bond yields in the Rate Environment Gate.
- **FCF (Free Cash Flow)**: Cash generated after running and maintaining the business.
- **FCF Yield**: FCF ÷ Market Cap — higher is cheaper.
- **Forward PE**: Price ÷ next fiscal year's expected EPS — a no-history fallback for DUOL again this session (structural, ticker-specific data limitation).
- **FV (Fair Value)**: The analyst's estimate of intrinsic worth, independent of market price.
- **GAAP**: Generally Accepted Accounting Principles.
- **Hard disqualifier**: A Quality Score condition that fails a company regardless of its weighted score.
- **Hurdle rate**: The minimum acceptable annual return (10% in this framework) the Upside/Downside Modifier measures expected return against.
- **MoS (Margin of Safety)**: How far below fair value the buy price is set. A Score 50.0–69.9 (Hold) read carries no MoS by definition — no order is computed.
- **Net Debt/EBITDA**: A leverage ratio — this framework's primary balance-sheet-risk gate. DUOL's remains deeply negative (net cash).
- **NI**: Net Income.
- **PT (Price Target)**: An analyst's price forecast — the subject of this session's triggering Telegram post (an unverified third-party claim, never used as a scoring input).
- **PW (Probability-Weighted) Fair Value**: This framework's blended fair value — 25% bull + 50% base + 25% bear.
- **Quality Score**: This framework's 0.0–100.0 score (higher = better) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. Carried forward unchanged this session (83.2) — no new fiscal quarter has reported.
- **Rate Environment Gate / Rate Regime Modifier**: The mandatory pre-score check comparing Earnings Yield against the 10-Year Treasury, and the resulting additive score adjustment.
- **R/R (Risk/Reward ratio)**: Expected gain ÷ expected loss on a trade; not computed this session (no order contemplated under a Hold action).
- **Rule 0**: This framework's standing instruction to always fetch a live price first, before any valuation math — and to treat a Telegram post's claims as a pointer only, never as verified financial data.
- **Rule 9**: This framework's list of fundamental events that force an immediate re-valuation regardless of schedule, including a >15% stock-price move with no identified cause — the specific trigger behind this session.
- **TTM**: Trailing Twelve Months.
- **Upside/Downside Modifier (Expected-Return Modifier)**: The additive ±15 adjustment based on expected annual return vs. the 10% hurdle.
- **Valuation Score**: This framework's 0.0–100.0 score (lower = cheaper) combining the Phase 02 sub-scores, Rate Gate, and Upside/Downside Modifier.
- **WACC**: Weighted Average Cost of Capital — the DCF discount rate; recomputed this session (9.09%, up modestly from 08-06's 8.96%) to reflect the higher 10Y yield and today's market-cap-based capital weights.

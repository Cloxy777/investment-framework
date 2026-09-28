# RESCORE — DUOL (Duolingo, Inc.) — 2026-09-28

**Task type:** RESCORE (mode `--both`)
**Date:** 28 Sep 2026
**10Y US Treasury Yield:** 5.24% — U.S. Treasury daily par yield curve, most recent published row, 2026-09-28.
**Rate Regime Modifier (Step 2):** +10 (10Y now in the >5% bracket — up sharply from 4.75% at the 09-01 review)
**Current DUOL portfolio weight:** 8.86% per [holdings.md](../portfolio/holdings.md) (last synced ahead of today's price move).
**Sector:** Technology — Education Software (EdTech / Language Learning)
**Last review:** 01 Sep 2026 (Valuation Score 85.1, Quality Score 83.2, Composite Score 51.0, HOLD).

**Why this session fired:** DUOL's live price, fetched fresh via IBKR (Rule 0), is **$134.33** — a **−15.25%** move from the $158.50 price last used in the 09-01 review ((134.33/158.50) − 1 = −15.25%). This clears both (a) DUOL's own documented "Next review trigger" (*">15% unexplained price move from $158.50 in either direction"*) and (b) [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 9's standing trigger — a **mandatory re-valuation**. No new earnings/8-K has been filed since 08-06 (Q2 FY2026) — next print, Q3 FY2026, is still expected ~early November 2026 and has **not yet been reported** (confirmed via web search this session) — so, like 09-01, this is a **price/rate-driven re-score**, not a fundamentals re-score. Context gathered this session (not used as a scored input, per Rule 0/"never act on price movement alone"): (1) the 10Y Treasury has jumped from 4.75% (09-01) to 5.24% today — a market-wide move (US media report the 10Y near its highest level since mid-2007 on hawkish Fed commentary and rising inflation expectations), which mechanically pressures growth-stock valuations broadly, not a DUOL-specific event; (2) sustained negative sentiment and continued insider selling (CEO Luis von Ahn sold 28,292 shares on 2026-09-16 per Motley Fool/SEC Form 4 reporting; other Section 16 officers/directors also sold in September) amid the stock's ~51% one-year decline; (3) management publicly reaffirmed its strategy of prioritizing DAU growth and engagement over near-term monetization at Citi's 2026 Global TMT Conference (mid-September) — consistent with, not a change from, the deceleration already reflected in Q2 FY2026 guidance and already captured in the Growth sub-score's −10 modifier. None of this is a new hard fundamental trigger (no earnings, no guidance revision, no M&A, no management change) — it is flagged here as Phase 04 monitoring context, not scored.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$134.33** | IBKR `get_price_snapshot` (contract_id 505002183), real-time last trade, timestamp 2026-09-28 19:58:45 UTC. Bid $133.50 / Ask $137.75. |
| Cross-check | $134.30 | yfinance `t.info["currentPrice"]` / `regularMarketPrice`, fetched same session — agrees to $0.03 (0.02%). |
| Cumulative move since last review | **−15.25%** ($158.50 → $134.33) | Computed this session. |
| 52-week range | $87.89 – $468.00 (carried forward from 08-06 IBKR `misc_statistics`; not re-pulled this session — price-only trigger) | — |

**No price-inference shortcuts taken** — live price fetched first per Rule 0, before any valuation math.

---

## 2. Data Gathered — Sources & Gaps

**`yfinance` was functional this session** (unlike 08-06/09-01). `python -m scripts.fetch_fundamentals DUOL` output:

```
Market Cap            = 6,257,455,616
Enterprise Value      = 5,486,567,424
Shares Outstanding    = 40,237,065
Forward PE            = 17.581
FCF Yield %           = 6.352
EV/EBIT               = 34.927
Net Margin %          = 35.875
Gross Margin %        = 72.717
ROIC % (NOPAT/InvCap) = 23.730  [tax_rate=-1.0348, NOPAT=319,641,222, InvestedCapital=1,347,006,000]
Revenue 3yr CAGR %    = 41.082
Net Debt/EBITDA       = -5.265  [EBITDA_ttm=179,031,008]
FCF/NI TTM %          = 96.771
FCF/NI annual (oldest first) = [-73.1%, 870.9%, 298.5%, 87.0%]
FCF positive 3yr+     = True
5yr PE history        = NO-HISTORY FALLBACK (n=16 usable quarters)
```

**⚠️ Two data-quality findings this session, both worked around rather than blindly used — flagged for the orchestrator/future script fix, per "no black box":**

1. **Shares Outstanding (`sharesOutstanding` = 40,237,065) is the same known dual-class undercount flagged in the 07-04 session** — DUOL's SEC-filed diluted weighted-average share count for Q2 FY2026 (confirmed fresh this session via web search of the Q2 FY2026 10-Q) is **50,031,000** (three months ended 2026-06-30), unchanged from the 08-06/09-01 sessions since no new quarter has reported. **Used 50,031,000 (diluted) for every share-count-dependent calculation below**, not the vendor's 40,237,065 field.
2. **`fetch_fundamentals.py`'s `net_debt_to_ebitda` is computed off the *annual* balance sheet (FY2025-end, 2025-12-31), not the latest quarter** — a script bug (confirmed by reading `scripts/fetch_fundamentals.py`'s `_net_debt_to_ebitda()`, which reads `ticker.balance_sheet` — annual — not `ticker.quarterly_balance_sheet`). This produces a *stale* Net Debt of Total Debt $93,779,000 − Cash $1,036,389,000 = **−$942,610,000** (as of 2025-12-31), materially different from the correct, latest-quarter figure. Pulled `t.quarterly_balance_sheet` directly this session: at **2026-06-30** (the latest completed quarter, matching every other TTM figure used this session), Total Debt = $86,136,000, Cash = $1,180,887,000 → **Net Debt = −$1,094,751,000** — this **exactly matches** the SEC-XBRL-sourced figure the 08-06 session established directly from the primary filing and that 09-01 carried forward, an independent cross-check confirming the corrected number is right. **Used −$1,094,751,000 (Net Debt) for every calculation below**, not the script's raw `net_debt_to_ebitda` field. Recommend `scripts/fetch_fundamentals.py`'s `_net_debt_to_ebitda()` be pointed at `quarterly_balance_sheet` in a future fix — out of scope to patch in this session.

**Why the rest is acceptable to carry forward:** no new SEC filing/quarter has been reported since 08-06/09-01 (Q3 FY2026 still expected ~early November 2026, confirmed unreached via web search). Every other trailing-twelve-month fundamental (TTM EBIT $157,085,000, TTM FCF $397,504,000, moat-signal evidence, Growth-modifier evidence) is therefore identical to the 08-06 session's SEC-XBRL-sourced figures, carried forward unchanged (consistent with the 09-01 session's own precedent) — only price-, rate-, and share-count-dependent quantities are recomputed against today's $134.33 / 5.24% / 50,031,000-share inputs.

**10Y Treasury yield** — U.S. Treasury's own daily par-yield-curve CSV (`home.treasury.gov`), most recent row **2026-09-28: 10 Yr = 5.24%**.

**Forward EPS** — `yfinance` `t.info["forwardEps"]` = **$7.63905** (a vendor consensus estimate, used directly rather than back-deriving an implied EPS from a stale price/PE pair as the 08-06/09-01 sessions had to when Forward-PE data was unstable). At today's live price: Forward PE = $134.33 / $7.63905 = **17.58×** — consistent with the script's own fresh `forward_pe` field (17.581, computed off a slightly earlier cached price), cross-checking cleanly.

No data gaps that block this session — every input needed is either carried forward (unchanged TTM fundamentals) or freshly fetched (price, 10Y yield, forward EPS, corrected shares/net debt) this session.

---

## 3. Quality Score

No new fiscal quarter has reported since 08-06, so every Quality Score input is identical to that session's SEC-XBRL-sourced figures — re-run through `scripts.scoring.quality_score` this session (not merely asserted) to reproduce the number under full script verification, consistent with "show every calculation":

```
## Quality Score

**Profitability (25%)**
NetMargin_Component = clamp((13.44/30)x100) = 44.80
ROIC_Component = clamp((38.03/30)x100) = 100.00
Profitability_Score = (44.80 + 100.00) / 2 = 72.40

**Margins (15%)**
GrossMargin_Score = clamp((72.72/80)x100) = 90.90

**Growth (20%)**
Growth_Score = clamp((41.08/25)x100) = 100.00
-10 structural growth deceleration evidence: FY2026 full-year revenue growth guided to 16.3%
(down from FY2025 actual 38.7%); Q3 FY2026 revenue growth specifically guided to 11.1% (down
from Q2 actual 18.3%) -- Duolingo Q2 FY2026 shareholder letter / Form 8-K, filed with the SEC
2026-08-05. Reaffirmed unchanged, no new quarter reported since (and reaffirmed qualitatively
by management's own Citi TMT Conference remarks, mid-September 2026, that growth is being
managed for DAU/engagement over near-term monetization).
Growth_Score (final, clamped) = 90.00

**Balance Sheet (15%)**
BalanceSheet_Score = clamp(100x(1 - -6.33/4)) = 100.00

**Moat Signal (15%)**
| Signal | True | Evidence |
|---|---|---|
| market_share_stable_or_growing | True | DAU 58.7M (+23% YoY), MAU 140.6M (+10% YoY), paid subscribers 12.7M (+17% YoY) -- Q2 FY2026 shareholder letter (SEC 8-K, filed 2026-08-05). |
| brand_premium | False | No cited pricing-power evidence found (unchanged across sessions). |
| network_effect | False | No documented two-sided-marketplace mechanism (unchanged). |
| switching_costs | True | Streak/XP/League gamification lock-in; Streak Revival campaign revived 15.4M streaks, evidence users value accumulated streak history -- Q2 FY2026 shareholder letter. |
| scale_cost_advantage | True | Company-cited 'AI cost trends' enabling lower per-unit content-generation cost as AI feature delivery scales -- Q2 FY2026 shareholder letter, 2026-08-05. |
Moat_Score = (3/5) x 100 = 60.00

**FCF Quality (10%)**
FCFQuality_Score = clamp(((0.9677 - 0.40)/0.60)x100) = 94.62

**Quality Score — Final**
Quality Score = (72.40x0.25) + (90.90x0.15) + (90.00x0.20) + (100.00x0.15) + (60.00x0.15) + (94.62x0.10)
= 83.197 -> rounds to 83.2

# Quality Score = 83.2 — PASSES the 80.0+ gate
```

**Hard disqualifiers re-confirmed on the same unchanged rolling TTM window** (FCF/NI conversion 87.0–870.9% across FY2023–FY2026 TTM, well above 70%; Net Debt/EBITDA −6.33× standard denominator, deeply net-cash; FCF-positive every year FY2022–FY2026 TTM) — all ✅ PASS, no hard disqualifier triggers.

**Quality Score = 83.2 — clears the 80.0+ gate, comfortably.** Unchanged from 09-01/08-06. No Phase 04 Quality Watch escalation.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test:**
```
Forward PE (live price / vendor consensus forward EPS) = $134.33 / $7.63905 = 17.583x
EY = 1 / 17.583 = 5.6873%
Spread = 5.6873% − 5.24% (10Y) = +0.4473%   (< +1.5% threshold)
```
**FAILS Step 1 → +5 additive.**

**Step 2 — Rate Regime Modifier.** 10Y = 5.24% → **>5% bracket → +10** (up from +5 at 09-01's 4.75% — the 10Y has crossed the top bracket boundary since the last review).

**Combined Rate Modifier: +15**

---

## 5. Valuation Score (Phase 02)

Inputs fed to `scripts.scoring.valuation_score` (fresh FCF Yield / EV/EBIT off today's $134.33 and the corrected 50,031,000 diluted shares / −$1,094,751,000 Net Debt; unchanged TTM EBIT $157,085,000 and TTM FCF $397,504,000; PEG not applicable — same clean-earnings-base disqualification as every prior DUOL session, redistributed to EV/EBIT):

```
## Valuation Score

**FCF Yield (40%)**
FCF_Score = clamp(100x(1 - 5.9147/10)) = 40.853
  [Market Cap = $134.33 x 50,031,000 = $6,720,664,230; FCF Yield = $397,504,000 / $6,720,664,230 = 5.9147%]

**EV/EBIT**
EV/EBIT_Score = clamp((35.8145 - 12)/23 x 100) = 100.000
  [EV = $6,720,664,230 + (-$1,094,751,000) = $5,625,913,230; EV/EBIT = $5,625,913,230 / $157,085,000 = 35.81x]

**Forward PE**
No 5yr PE history available (no-history fallback) -> FwdPE_Score = 50.0 (neutral, flagged)

**PEG**
PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT

**Rate Environment Gate**
EY = 1/17.583 x 100 = 5.6873%
Spread = EY - 10Y (5.24%) = 0.4473pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 5.24% -> Step 2 bracket modifier = +10
Total Rate Modifier = 5 + 10 = +15

**Upside/Downside Modifier**
PW Fair Value = 0.25x147.47 + 0.50x134.33 + 0.25x78.4 = 123.6325
Gap Upside % = (123.6325/134.33) - 1 = -7.9636%
Annualized gap = -7.9636% / 2yr = -3.9818%/yr
E = -3.9818 (annualized gap) + 8 (intrinsic growth) + -1.0000 (shareholder yield: 0 div + -1 buyback) = 3.0182%/yr
0 <= E (3.0182%) < H -> M = 5 x (10.0-3.0182)/10.0 = 3.4909
Upside/Downside Modifier (bounded [-15, +15]) = 3.4909

**Raw Weighted Score**
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2
= 66.341

**Final Valuation Score**
Final Score = Raw (66.341) + Rate Modifier (+15) + Upside/Downside Modifier (+3.491)
= 84.832 -> rounds to 84.8

# Valuation Score = 84.8
```

**Bull/Base/Bear Fair Value basis (Method B, EV/EBIT scenario ladder — same multiples as 08-06/09-01, unchanged TTM EBIT/Net Debt/shares):**

| Scenario | Wt | EV/EBIT multiple | FV/share |
|---|---|---|---|
| Bull | 25% | 40× | $147.47 (unchanged — same EBIT/net debt/shares as prior sessions) |
| Base | 50% | 35.81× (= today's actual) | $134.33 (= live price, by construction) |
| Bear | 25% | 18× | $78.40 (unchanged) |

**Intrinsic growth (8%) and shareholder yield (−1%, dilution net of buyback)** carried forward unchanged — same judgment inputs as every DUOL session since 08-06, no new evidence this session to revise them. Catalyst window: no new dated, narrower catalyst documented this session → default 2yr (Rule 10).

**Valuation Score = 84.8** — standalone "TRIM to 50% of original size" band (80.0–89.9), a modest deterioration from 09-01's 85.1 read (nearly flat — the price drop and the EV/EBIT-cheapening it implies is almost exactly offset by the Rate Modifier jumping +5 as the 10Y crossed into the >5% bracket). This raw-score read is superseded by the Composite Score below.

---

## 6. Composite Score

```
python -m scripts.scoring.composite_score --set quality_score=83.2 --set valuation_score=84.8

## Composite Score
Composite Score = 0.50x(100 - 83.2) + 0.50x84.8 = 50.800 -> rounds to 50.8

# Composite Score = 50.8
(Quality Score 83.2, Valuation Score 84.8)
```

**Composite Score = 50.8 — "HOLD" band** (50.0–69.9), essentially flat vs. 09-01's 51.0 (a 0.2-point move) — despite the stock falling 15.25% and the 10Y jumping 49bp, the two effects roughly cancel in the blend (cheaper EV/EBIT and a smaller Upside/Downside Modifier penalty, offset by a bigger Rate Regime Modifier). DUOL remains inside Hold, not re-entering Cheap and not crossing into Trim.

**⚠️ Flagged: this result again sits close to the Cheap/Hold boundary (49.9/50.0)** — closer, in fact, than 09-01's 51.0 (0.85pp from the boundary vs. 1.05pp). Robustness check on the Upside/Downside Modifier's three judgment inputs (same method as 09-01):

| Sensitivity | E | M | Final Valuation Score | Composite Score | Band |
|---|---|---|---|---|---|
| Primary (8% growth, −1% shareholder yield, 2yr window) | +3.02% | +3.49 | 84.8 | **50.8** | Hold |
| Conservative growth (6% growth) | +1.02% | +4.49 | 85.8 | 51.3 | Hold |
| Optimistic growth (10% growth) | +5.02% | +2.49 | 83.8 | 50.3 | Hold |
| Flat shareholder yield (0% instead of −1%) | +4.02% | +2.99 | 84.3 | 50.6 | Hold |
| Narrower catalyst window (18mo instead of 24mo) | +1.69% | +4.16 | 85.5 | 51.2 | Hold |

**Every disclosed sensitivity stays inside the 50.0–69.9 Hold band** (range 50.3–51.3) — the conclusion is robust to reasonable variation in the modifier's judgment inputs. None comes close to re-entering Cheap (would require Composite <49.95, i.e. Valuation Score <83.1) or Trim (Composite ≥70.0, far outside any tested range).

---

## 7. Action Recommendation

Composite Score 50.8 falls in the **50.0–69.9 "HOLD — watch only, no new entry, no trim"** band.

**No add:** position already sits well above the "Cheap"-band 3–5% sizing target (8.86% recorded weight, itself likely understated relative to true current weight given the price drop's effect on other holdings' relative weights — precise reconciliation is a `/sync-portfolio` task, out of scope here). No margin of safety exists in the Hold band by definition (per [fair-value-methodology.md](../framework/fair-value-methodology.md) Step 2's integration table: Score 50.0–69.9 → "No MoS → Watchlist only").

**No trim:** the raw Valuation Score (84.8) sits deep in the standalone Trim-to-50% band, but the Composite Score — governing per framework rule once a Quality Score exists — stays inside Hold (50.0–69.9, below the 70.0 Trim threshold), robust across the sensitivity table above. DUOL's unchanged, strong Quality Score (83.2) is doing the work keeping the blend out of Trim territory even as the raw cheapness read stays weak.

**No exit trigger:** no fundamental deterioration this session — margins intact, ROIC far above WACC, pristine net-cash balance sheet, no dilutive raise, no covenant breach, no new management change (insider *selling* is not itself an exit trigger under this framework's rules, which require fundamental deterioration/broken thesis/balance-sheet crisis/sustained 90+ score — flagged as a Phase 04 monitoring item, not acted on), no M&A. Today's move is a combination of a broad rate-driven re-rating (10Y +49bp) and continued sentiment deterioration (insider selling, ongoing multi-month drawdown) — explicitly **NOT** a valid exit trigger per the operating brief's own list ("price dropped on intact thesis, macro fear... NOT valid").

### Fair Value reference (not gating an order — action is HOLD, not BUY/TRIM)

```
Multiples-Based Fair Value (Method B, PW Fair Value, §5):                                    $123.63
```
DCF Fair Value (Method A) was not recomputed this session — no order is contemplated under the Hold action and the operating brief's Step 2 of order setup only requires Blended Fair Value when a BUY/TRIM order is actually being sized; shown as multiples-only reference. **Live price ($134.33) is now ~8.6% above the multiples-based PW Fair Value** — a reversal from 09-01, when price sat within ~1% of the (DCF-blended) Fair Value; today's price/PW-FV gap is driven mechanically by the Rate Regime jump (a higher 10Y raises the effective hurdle/discount rate context) more than by any change in the underlying EBIT-multiple scenario ladder, which is unchanged.

No order setup (Buy Price / Stop Loss / R/R / Position Size) computed — consistent with the Hold action and `scripts.scoring.order_setup`'s own refusal to compute one outside the 0.0–49.9 score bands.

### Net Action: **HOLD** — maintain the current DUOL position as-is (no add, no trim)

---

## 8. Next Review Trigger

**Date/event:** DUOL's Q3 FY2026 earnings release (expected ~early November 2026, still unreported as of this session) — mandatory Rule 9 re-score. Specifically check: **Q3 revenue growth vs. the 11.1% YoY guide ($302M)**, **Q3 bookings vs. the $307M / 8.9% YoY guide**, **Q3 adjusted EBITDA vs. the $76M / 25.2%-margin guide**, **DAU growth relative to management's ~100M-DAU-by-2028 trajectory**, and whether the diluted share count (50.03M at Q2) shows buybacks beginning to net-offset dilution. Also standard triggers: any further guidance revision, management change, M&A, or a **>15% unexplained price move from today's $134.33** in either direction (a fresh 15% band reset from today's reference price). Given the continued insider-selling pattern flagged this session, also worth a qualitative check at the next review of whether Section 16 filings show any acceleration or new 10b5-1 plan disclosures.

---

## Glossary

- **Composite Score**: This framework's single ranking number (0.0–100.0, 0.0 = most attractive) blending the Quality Score and the Valuation Score 50/50 — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — computed only for companies that have already cleared the 80.0+ Quality Score gate. Used against the Phase 03/05 action tables instead of the raw valuation score.
- **DCF**: Discounted Cash Flow — a valuation method that estimates a company's worth today by projecting its future cash and discounting it back to present-day value.
- **EBIT**: Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
- **EV**: Enterprise Value — a company's total value to all capital providers: market cap + debt − cash.
- **EV/EBIT, EV/EBITDA**: Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure.
- **EY (Earnings Yield)**: 1 ÷ Forward PE — the inverse of the PE ratio, expressed as a yield so it can be compared directly against bond yields.
- **FCF**: Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield**: Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper.
- **Forward PE**: Price ÷ next twelve months' expected earnings per share.
- **FV (Fair Value)**: The analyst's estimate of what a company is intrinsically worth, independent of its current market price.
- **GAAP**: Generally Accepted Accounting Principles.
- **Hard disqualifier**: One of three Quality Score conditions that fails a company regardless of its weighted sub-score total.
- **Hurdle rate**: The minimum acceptable annual return (10%) the Upside/Downside Modifier measures expected return against.
- **MoS (Margin of Safety)**: How far below fair value the buy price is set. A Score 50.0–69.9 (Hold) read carries no MoS — no order is computed.
- **Net Debt/EBITDA**: Net debt divided by EBITDA — a leverage ratio, this framework's primary balance-sheet-risk gate.
- **NI (Net Income)**: Accounting profit after all expenses, interest, and taxes.
- **PT (Price Target)**: An analyst's forecast of where a stock's price will be at a future date.
- **PW (Probability-Weighted) Fair Value**: This framework's blended fair value — 25% bull + 50% base + 25% bear.
- **Quality Score**: This framework's 0.0–100.0 score (higher = better) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required for the Composite Score. Carried forward unchanged this session (83.2), re-verified via script.
- **Rate Environment Gate / Rate Regime Modifier**: The mandatory pre-score check comparing Earnings Yield against the 10-Year Treasury, and the resulting additive score adjustment (−10 to +10).
- **R/R (Risk/Reward ratio)**: Expected gain ÷ expected loss on a trade; not computed this session (no order contemplated under a Hold action).
- **Rule 0**: This framework's standing instruction to always fetch a live price first, before any valuation math.
- **Rule 9**: This framework's list of fundamental events that force an immediate re-valuation regardless of schedule, including a >15% stock-price move — the trigger behind this session.
- **TTM (Trailing Twelve Months)**: The most recent four reported quarters combined.
- **Upside/Downside Modifier (Expected-Return Modifier)**: The additive ±15 adjustment based on expected annual return vs. the 10% hurdle.
- **WACC**: Weighted Average Cost of Capital — the DCF discount rate; not recomputed this session (no DCF order-setup work performed under a Hold action).
- **ROIC**: Return on Invested Capital.
- **DAU (Daily Active Users)** / **MAU (Monthly Active Users)**: Usage/reach engagement metrics; DAU is DUOL's primary growth KPI.
- **10-Q**: The quarterly financial-disclosure report a US public company files with the SEC — the primary source for DUOL's diluted share count this session.
- **8-K**: The SEC "current report" filed within days of a material event, commonly used to furnish an earnings press release.
- **Earnings Yield Spread Test**: Step 1 of the Rate Environment Gate — Earnings Yield minus the 10-Year Treasury yield.

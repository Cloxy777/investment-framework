# RESCORE — ADBE (Adobe Inc.) — 2026-07-29

## 1. Session header

- **Task type:** RESCORE (single ticker, `--both` mode — Quality + Valuation)
- **Date:** 2026-07-29
- **10Y US Treasury yield:** 4.65% (FRED `DGS10`, most recent posted value, 2026-07-27 — 07-28/07-29 not yet posted at time of session). Cross-checked against real-time market reporting for 2026-07-29 itself (CNBC: yield rose to ~4.641%; TradingEconomics: ~4.63%) — both land in the same 3.5–5% band as the FRED-posted figure, so the Rate Regime Modifier is unaffected either way.
- **Rate Regime Modifier in effect:** +5 (10Y in the 3.5–5% band)
- **Prior scores (2026-07-04 rescore):** Valuation 0.0 (floor) | Quality 83.9 | Composite 8.1
- **Current ADBE weight:** 3.88% of portfolio per the last sync (2026-07-26); position remains a **partial fill** (10 of a ~14–16-share target — see §9)
- **Sector:** Technology — Software (Creative/Document Cloud, Digital Media & Digital Experience)
- **This session's job:** routine re-score plus a Rule 9 investigation — ADBE's price has moved **+19.5%** since the 2026-07-04 review ($219.72 → $262.61), which crosses the 15%-unexplained-move trigger in [operating-calendar.md](../framework/operating-calendar.md). §2 documents the investigation.

## 2. Data gaps flagged (before proceeding)

1. **No new fundamental data since 2026-07-04.** ADBE's fiscal Q3 FY2026 earnings aren't due until ~mid-September 2026 (Rule 9 calendar trigger, not yet reached) — no new 10-Q, guidance revision, M&A, or newly-resolved management change since the last session. **All FY-level financial inputs (revenue, EBIT, FCF, net income, margins, net debt, FY26 EPS guidance, 5yr avg/low/high PE range, shares outstanding) are carried forward unchanged from the verified 2026-07-04 session** — this is a documented absence of a new data point, not a guess. Only the live price, the 10Y yield, and everything mechanically derived from price (FCF yield, EV/EBIT, Forward PE, the Upside/Downside gap/E calc, order-setup levels) are refreshed this session.
2. **Rule 9 ">15% unexplained move" investigation (required before treating this as routine):** ADBE closed at $219.72 on 2026-07-02 (last session's live price) and trades at $262.61 intraday today, +19.5%. WebSearch attributes the move to (a) a strong Q2 FY26 earnings beat and raised guidance already known and priced into the 07-04 session, (b) an HSBC analyst upgrade to Buy with a $308 price target (2026-07-2x), and (c) a broader enterprise-software sentiment rebound after IBM's late-July profit-warning scare was reframed as a timing issue and ServiceNow/SAP posted strong results. **No new company-specific fundamental event fired** (no new earnings, no new guidance revision, no M&A, no new management change) — this is a **sentiment/re-rating move**, not a fundamental trigger, so per the "NOT valid: price... macro fear... short-term earnings miss" guardrail it does **not** on its own change the fair-value inputs. It does, however, mechanically move the valuation sub-scores (denominator effects) and the order-setup levels, which is exactly what this re-score recalculates. CEO Shantanu Narayen's planned retirement (announced 2026-03-12, successor search ongoing) and CFO Dan Durn's departure (effective 2026-06-15, Steven Day still interim) are both **pre-existing, already-known** items, not new since 07-04.
3. **Permanent CFO still not named** — Steven Day remains interim CFO as of this session (unchanged since 06-15). Still an open item to watch (management-change Rule 9 trigger once resolved).
4. **D&A** for the Balance Sheet sub-score's EBITDA remains the FY2025 annual audited proxy ($818M) — carried forward, same caveat as 07-04 (no fresher quarterly D&A breakdown available).
5. Live price cross-check: IBKR `get_price_snapshot` (`last`, live intraday quote, not close) shows **$262.61**, +$13.43 / +5.39% on the day. An independent WebSearch aggregator snapshot (captured earlier in the session) showed a $248.54–$260.61 intraday range — consistent with a fast-moving rally day; the IBKR broker-direct quote is used as the Rule-0 live price per the framework's own sourcing hierarchy.

## 3. Live data (Rule 0 — fetched first)

| Item | Value | Source |
|---|---|---|
| **Live price used** | **$262.61** | IBKR `get_price_snapshot` (contract_id 265768, NASDAQ), live intraday quote, 2026-07-29. Cross-checked via WebSearch (independent aggregator range $248.54–$260.61 earlier in session; consistent with a fast intraday rally). |
| 52-week high / low | $370.86 / $190.12 | IBKR `get_price_snapshot` `misc_statistics` |
| 13-week high / low | $275.44 / $190.12 | IBKR `get_price_snapshot` `misc_statistics` |
| Change (today) | +$13.43 / +5.39% | IBKR `get_price_snapshot` `change` |
| Shares outstanding | 397.50M (carried forward — no new quarter) | Carried from 2026-07-04 session |
| Market Cap (computed) | 397.50M × $262.61 = **$104,387.5M** | Computed |

## 4. Quality Score (recomputed — no fundamental inputs changed since 07-04)

```
Profitability (25% weight):
  NetMargin_Component = clamp((30.00/30)×100) = 100.0   (Net Margin FY2025, carried)
  ROIC_Component       = clamp((38.9/30)×100) = 100.0   (carried; cross-check 59.35% also clamps to 100.0)
  Profitability_Score  = (100.0 + 100.0) / 2 = 100.0   (no FCF-positive cap — positive every year on record)

Margins (15% weight): Gross margin FY2025 = 89.27% (carried)
  GrossMargin_Score = clamp((89.27/80)×100) = clamp(111.6) = 100.0

Growth (20% weight): Revenue 3yr CAGR (FY2022→FY2025, carried) = 10.52%
  Growth_Score = clamp((10.52/25)×100) = 42.08
  TAM-expansion / pricing-power bonus (+10, carried — Adobe's own Q2 FY26 earnings call, 11 Jun 2026):
    AI-first ARR 3x YoY to >$500M; Firefly ARR ~$300M, +50% QoQ; GenStudio ARR +25%+ YoY;
    Creative Cloud Freemium MAU 50M→90M. FY26 guidance (+11.5–11.9% YoY) still a step up from
    FY25's realized 10.53% — consistent with acceleration, no −10 penalty.
  Growth_Score (with bonus) = 42.08 + 10 = 52.08

Balance Sheet (15% weight): Net Debt $1,451M (carried) / EBITDA (TTM EBIT $9,372M + FY25 D&A proxy $818M) = $10,190M
  Net Debt/EBITDA = 1,451 / 10,190 = 0.1424×
  BalanceSheet_Score = clamp(100×(1 − 0.1424/4)) = 96.44

Moat Signal (15% weight) — checklist, unchanged evidence (no new quarter to re-cite):
  ✓ Market share stable/growing — TRUE (~58.2% content-creation-tools share; Creative Cloud paid membership ~41M, +1M/quarter run-rate)
  ✓ Brand premium — TRUE (12–25% list-price increases for 2026 sustained alongside subscriber growth and Freemium MAU near-doubling)
  ✗ Network effect — FALSE (no cited two-sided-marketplace mechanism with concrete adoption data)
  ✓ Switching costs — TRUE (Creative Cloud Libraries/Brand Kit cross-product lock-in; net revenue retention 130%+)
  ✗ Scale cost advantage — FALSE (R&D budget size ≠ a cited cost-per-unit gap)
  Moat_Score = (3/5) × 100 = 60.0

FCF Quality (10% weight): FCF/NI conversion (TTM, carried) = 10,280/7,229 = 142.2%
  FCFQuality_Score = clamp(((1.422 − 0.40)/0.60)×100) = 100.0

Quality Score = 100.0×0.25 + 100.0×0.15 + 52.08×0.20 + 96.44×0.15 + 60.0×0.15 + 100.0×0.10
              = 25.0 + 15.0 + 10.416 + 14.466 + 9.0 + 10.0
              = 83.882 → rounds to 83.9
```

**Hard disqualifier check** — none fire (unchanged): FCF/NI conversion comfortably >70%; Net Debt/EBITDA 0.14× far under threshold; FCF positive every year on record.

**Quality Score = 83.9 — PASSES the 80.0+ gate** (unchanged from 07-04 — no fundamental inputs moved between sessions).

## 5. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $262.61 / $24.40 (FY2026 non-GAAP EPS guidance midpoint, carried) = 10.763×
EY = 1 / 10.763 = 9.291%
Spread = 9.291% − 4.65% (10Y) = +4.641%
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** (+4.641%) → no +5 additive.

**Step 2 — Rate Regime Modifier**
10Y = 4.65% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for ADBE = +5**

## 6. Phase 02 — Valuation Score (every sub-score shown)

**FCF Yield — 40% weight**
```
FCF (TTM, carried forward) = $10,280M
FCF Yield = 10,280 / 104,387.5 = 9.848%
FCF_Score = clamp(100 × (1 − 9.848/10), 0, 100) = clamp(1.52, 0, 100) = 1.52
```
→ Contribution: 1.52 × 0.40 = **0.608**

**EV/EBIT — 40% weight** (PEG not applicable — see below — its 15% weight redistributed here, same as every prior ADBE session)
```
EV = Market Cap $104,387.5M + Net Debt $1,451M (carried) = $105,838.5M
EV/EBIT = 105,838.5 / 9,372 (TTM EBIT, carried) = 11.293×
EV/EBIT_Score = clamp((11.293 − 12)/23 × 100, 0, 100) = clamp(−3.07, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.40 = **0.0**

**Forward PE (fallback formula, 5yr avg) — 20% weight**
```
5yr avg PE (carried forward, unchanged — slow-moving statistic) = 27.2×
Deviation% = (10.763 − 27.2) / 27.2 × 100 = −60.43%
FwdPE_Score = clamp(50 + (−60.43 × 2.5), 0, 100) = clamp(−101.1, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — not applicable.** Non-GAAP EPS growth FY2024 +14.6% / FY2025 +13.7% — both below the 15% Fast-Grower threshold (carried forward finding, unchanged). **Classified NOT a Fast Grower** → weight redistributed to EV/EBIT (40%, above).

```
Raw weighted score = 0.608 + 0.0 + 0.0 = 0.608
+ Rate Regime Modifier (+5) = 5.608
```

## 7. Upside/Downside Modifier (Expected-Return Modifier) — full calc

Fair-value scenario inputs (bull/base/bear DCF, multiples) carried forward from 2026-06-20/07-04 — no fundamental change to justify revising WACC, growth, or terminal assumptions (Data Gap #1). Only the live price and the resulting gap/annualization are refreshed. (HSBC's $308 analyst price target, noted in Data Gap #2, is context — not a scored input; this framework's own scenario-weighted DCF/multiples blend already sits above that figure and isn't overridden by a single analyst call.)

```
Blended Fair Value (40% DCF PW $449.03 / 60% Multiples $352.74, carried forward) = $391.26
Gap Upside % = (391.26 / 262.61) − 1 = +48.99%
Catalyst window = 2.0 yr (Rule 10, unchanged — catalyst = Digital Media segment growth holding ≥~10% through
  Q3 FY26 [~Sept 2026, ~1.5 months out] and Q4 FY26 [~Dec 2026, ~4.5 months out], both inside the 18–24mo window)
Annualized gap = 48.99% / 2.0 = 24.49%/yr
Intrinsic growth = +10%/yr (unchanged)
Shareholder yield = +2%/yr (unchanged)

E = 24.49% + 10% + 2% = +36.49%/yr
```

**Map E → M** (hurdle H = 10%, E ≥ H branch):
```
M = −15 × clamp((36.49 − 10)/15, 0, 1) = −15 × clamp(1.766, 0, 1) = −15 × 1 = −15.0
```
**Modifier M = −15.0** (hits the −15 floor).

**Guardrails check:**
- Catalyst within 18–24mo? **Yes** — window is now even closer (Q3 FY26 ~1.5 months out) than at 07-04.
- Scenario-weighted (not the rosy point)? **Yes** — same bull/base/bear DCF blend as prior sessions.
- **Robustness note:** even zeroing the annualized-gap component entirely, E = 10% + 2% = 12% > hurdle → M would still be negative. The modifier's sign is not sensitive to the gap estimate, and the gap has actually *narrowed* materially (78.1% → 49.0%) as the price rallied — the mechanism is behaving exactly as designed: price appreciation shrinks the modifier's magnitude, not its direction, until the gap closes enough to flip it.

## 8. Final Valuation Score + Composite Score

```
FINAL VALUATION SCORE = 5.608 (raw + rate gate) + (−15.0) (Upside/Downside) = −9.392 → clamped to the 0.0 floor
```

| | Value |
|---|---|
| Raw weighted | 0.608 |
| Rate Regime Modifier | +5.0 |
| Upside/Downside Modifier | −15.0 (E = +36.49%/yr) |
| **FINAL VALUATION SCORE** | **0.0** (floor) |
| Prior valuation score (07-04) | 0.0 |
| **Quality Score (recomputed, unchanged)** | **83.9 — PASSES 80.0+ gate** |

```
Composite Score = 0.50 × (100 − 83.9) + 0.50 × 0.0 = 0.50 × 16.1 + 0.0 = 8.05
  → exactly on a ".X5" boundary → round UP (conservative) → 8.1
```

**Composite Score = 8.1 — unchanged from 07-04.** Falls in the **0.0–29.9 "Very Cheap"** band → **BUY — Full position 6–8%** (Phase 03 action table). Despite the +19.5% price rally, the score didn't move: the valuation sub-scores were already floored, the Rate Regime Modifier is unchanged, and the Upside/Downside Modifier — while its magnitude inputs shifted (gap narrowed from +78.1% to +49.0%) — still comfortably clears the −15 floor. The action call is therefore identical, but every order-setup level below has moved because they're tied to the (higher) live price.

## 9. Fair Value & Order Setup (BUY action — full setup required)

### Fair Value (carried forward, no fundamental change to justify a revision)
```
Bear DCF $251.40 | Base DCF $443.72 | Bull DCF $657.30  (unchanged scenario assumptions)
PW DCF FV = 0.25×657.30 + 0.50×443.72 + 0.25×251.40 = $449.03
Multiples-based FV = $352.74 (unchanged)
Blended FV = 0.40×449.03 + 0.60×352.74 = $391.26
```

### Order setup
```
Margin of Safety = 17.5% (midpoint, 15–20% band for Score 0.0–29.9)
Buy Price (ceiling) = $391.26 × (1 − 0.175) = $322.79
Live price $262.61 is still below the ceiling → ENTER NOW (effective entry = live price)
  — note the gap has narrowed materially: live price is now ~81% of the ceiling (was ~68% at 07-04)
Primary Sell Target = Blended FV = $391.26
Bull-Case Trim Target = Bull DCF $657.30 × 0.90 = $591.57
Stop Loss = Live Price × (1 − 0.225) = $262.61 × 0.775 = $203.52   (22.5%, midpoint of 20–25% band)
R/R = (391.26 − 262.61) / (262.61 − 203.52) = 128.65 / 59.09 = 2.18 : 1   (≥ 2:1 ✓ — but has compressed
  from 3.47:1 at 07-04, the natural consequence of the price rally narrowing the gap to target
  while the stop, a % of the now-higher price, also rose)
```

### Position sizing — top-up toward the partial-fill target
```
Portfolio Value (combined, holdings.md last sync 2026-07-26) = $57,832.61
Max $ Risk (1.5%) = $867.49
Risk/share = $59.09
Risk-based size = 867.49 / 59.09 = 14.68 shares
Allocation cap (6–8% band): 6% → 13.21 sh | 8% → 17.62 sh — risk-based size (14.68) sits inside the
  cap band, so it governs (min rule)
Full target (rounded down, conservative) = 14 shares
Held = 10 shares → TOP-UP = 4 shares
Top-up cost = 4 × $262.61 = $1,050.44
Resulting position = 14 × $262.61 = $3,676.54 = 6.36% of portfolio
```
**Cap cross-check:** 6.36% sits inside the 6–8% Very Cheap band and far under the 15% hard cap (Upgrade 7). Note the target share count has come down again (16 → 14) for the same mechanical reason flagged at 07-04: risk-per-share rises with price faster than the portfolio's fixed risk budget grows — not a conviction change.

### Order Setup Checklist
```
[x] Composite Score (Quality 83.9 + Valuation 0.0):  8.1   (≤ 49.9 ✓)
[x] Expected annual return E / catalyst window:      +36.49% / 2 yr
[x] Upside/Downside Modifier applied:                −15.0
[x] DCF Fair Value (PW):                             $449.03
[x] Multiples-Based Fair Value:                      $352.74
[x] Blended Fair Value:                              $391.26
[x] Margin of Safety %:                              17.5%
[x] BUY PRICE (ceiling; live already below):         $322.79
[x] PRIMARY SELL TARGET:                             $391.26
[x] BULL-CASE TRIM TARGET:                            $591.57
[x] STOP LOSS:                                        $203.52
[x] Risk/Reward Ratio:                                2.18:1  (≥ 2:1 ✓)
[x] Max $ Risk:                                       $867.49
[x] POSITION SIZE (top-up shares):                    4 (to reach a 14-sh target)
[x] POSITION SIZE ($):                                $1,050.44 top-up → 6.36% total
[x] Thesis invalidation triggers:                     see §10
```

## 10. Action, Thesis Status & Recommendation

**Recommendation: CONFIRMED BUY — top up ~4 shares (~$1,050, to reach a 14-share / 6.36% target). Composite Score 8.1 ("Very Cheap"), unchanged from 07-04.**

The +19.5% rally since 2026-07-04 was investigated under Rule 9 and traced to sentiment (an HSBC upgrade, a sector-wide software re-rating after IBM's profit-warning scare eased) rather than any new company-specific fundamental — no new earnings, guidance, M&A, or management change has occurred since the last session. The Composite Score is unchanged (8.1) because the valuation sub-scores were already at the 0.0 floor and the Upside/Downside Modifier, though its underlying gap narrowed from +78.1% to +49.0% as the price rose, still comfortably clears the −15 floor (robust even under a zero-gap stress test, §7). What *has* moved is the order-setup math: the Buy Price ceiling is unchanged ($322.79) but the live price is now materially closer to it, R/R has compressed from 3.47:1 to 2.18:1 (still passing the 2:1 minimum), and the risk-based position-sizing target has shrunk from 16 to 14 shares — a mechanical consequence of a fixed-$-risk budget divided by a now-larger risk-per-share, not a change in conviction.

**Thesis invalidation triggers (Phase 06 / stop), unchanged from prior sessions:**
- Digital Media revenue growth decelerates toward mid-single-digits without a non-AI one-off cause (2 consecutive quarters) → thesis broken
- Gross margin falls >3pp structurally, or FCF/NI conversion <70% for 2 consecutive quarters
- Net debt/EBITDA rising materially on debt-funded buybacks while growth slows
- Price through the $203.52 stop

All final-decision authority rests with the human investor; funding is the investor's call.

## 11. Watchlist disposition

A new dated watchlist entry ([watchlist/in-portfolio/ADBE/ADBE-2026-07-29.md](../watchlist/in-portfolio/ADBE/ADBE-2026-07-29.md)) is created rather than an appended "last checked" line — while the numeric scores are unchanged, a Rule 9 fundamental-event trigger fired (the >15% unexplained move) and was investigated, which per [watchlist/README.md](../watchlist/README.md#significant-change--when-does-a-new-dated-entry-get-created) warrants a fresh pointer even when the score/action end up unchanged. No stale-score mark to clear — ADBE's stale flag was already cleared at the 07-04 session and the scoring methodology hasn't changed again since.

## 12. Next review trigger

- **Q3 FY2026 earnings (~mid-September 2026)** — mandatory re-score (Rule 9). Check Digital Media segment growth ≥~10% (the catalyst underlying the Upside/Downside Modifier).
- **A permanent CFO appointment** — still open (interim Steven Day since 2026-06-15); watch for a strategy/cost-discipline signal when resolved (management-change Rule 9 trigger).
- **>15% unexplained move from $262.61** in either direction — immediate re-score (Rule 9).
- **If the top-up is executed**, log it in [decisions/](../decisions/) and reflect it at the next `/sync-portfolio` (holdings.md is handled by the orchestrator, not this session).

## 13. Glossary

- **ARR (Annual Recurring Revenue):** the annualized run-rate of subscription/recurring revenue at a point in time — used here to track Adobe's fast-growing AI product lines (Firefly, GenStudio) before they're large enough to be their own reported segment.
- **CAGR:** Compound Annual Growth Rate.
- **Composite Score:** this framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50.
- **D&A:** Depreciation & Amortization.
- **EBIT / EBITDA:** operating profit before interest and taxes / before interest, taxes, depreciation and amortization.
- **EPS:** Earnings Per Share.
- **EV / EV/EBIT:** Enterprise Value (market cap + debt − cash) / EV divided by EBIT, a valuation multiple.
- **EY (Earnings Yield):** 1 ÷ Forward PE, compared against the 10-Year Treasury yield.
- **Fast Grower:** a company growing EPS >15%/yr for 3+ years — triggers the PEG sub-score.
- **FCF / FCF Yield / FCF/NI conversion ratio:** Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality).
- **Forward PE:** price ÷ next year's expected EPS.
- **FV / PW Fair Value:** Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear).
- **Hard disqualifier:** one of three Quality Score conditions that fails a company regardless of weighted score.
- **Hurdle rate:** the minimum acceptable annual return (10% in this framework).
- **MAU (Monthly Active Users):** unique users engaging with a product at least once in a given month — a reach metric distinct from paying-subscriber counts.
- **Moat:** a durable competitive advantage protecting a business's profits.
- **MoS (Margin of Safety):** the discount below fair value demanded before buying.
- **Net Debt/EBITDA:** a leverage ratio; this framework's primary balance-sheet-risk gate.
- **NOPAT:** Net Operating Profit After Tax — EBIT × (1 − effective tax rate).
- **PE (Price-to-Earnings) ratio / PEG ratio:** price ÷ earnings; PE ÷ growth rate.
- **pp (percentage points):** a direct difference between two percentages.
- **Quality Score:** this framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02.
- **Rate Environment Gate / Rate Regime Modifier:** the pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band.
- **R/R (Risk/Reward ratio):** (expected gain) ÷ (expected loss); this framework requires ≥2:1.
- **ROIC:** Return on Invested Capital — NOPAT ÷ Invested Capital.
- **Shareholder yield:** dividend yield plus net buyback yield.
- **TAM:** Total Addressable Market.
- **Treasury yield (10Y):** the US government's 10-year borrowing rate, this framework's risk-free-rate benchmark.
- **TTM:** Trailing Twelve Months.
- **Upside/Downside Modifier:** an additive ±15 valuation-score adjustment based on expected annual return.

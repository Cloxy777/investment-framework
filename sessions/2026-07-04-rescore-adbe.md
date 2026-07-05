# RESCORE — ADBE (Adobe Inc.) — 2026-07-04

## 1. Session header

- **Task type:** RESCORE (single ticker, `--both` mode — Quality + Valuation)
- **Date:** 2026-07-04
- **10Y US Treasury yield:** 4.48% (FRED `DGS10`, most recent posted value, 2026-07-01 — 07-02/07-03/07-04 not yet posted)
- **Rate Regime Modifier in effect:** +5 (10Y in the 3.5–5% band)
- **Prior valuation score:** 0.0 (2026-06-20 rescore, floored) — Quality Score and Composite Score had never been computed for ADBE (both `?` in [holdings.md](../portfolio/holdings.md), and ADBE carried a `⚠️ STALE SCORE` banner + row in [watchlist/STALE.md](../watchlist/STALE.md) pending the 2026-06-29 Quality Score/Composite Score methodology addition)
- **Current ADBE weight:** 3.69% of portfolio per the last sync (2026-06-28); position is a **partial fill** (10 of a ~17-share target)
- **Sector:** Technology — Software (Creative/Document Cloud — Digital Media — and Digital Experience / marketing cloud)
- **This session's job:** (1) compute ADBE's **first-ever Quality Score** under the 2026-06-29 methodology, (2) refresh the Valuation Score with a live price, (3) compute the Composite Score for the first time, (4) clear the stale-score mark.

## 2. Data gaps flagged (before proceeding)

1. **IBKR `get_price_snapshot`'s `last` field returned a stale value.** It returned `$210.98` (`is_close: true`, `volume: 0`), which matches **2026-07-01's** close, not the most recent trading session. Markets were closed 2026-07-03 (observed Independence Day holiday, since 4 July falls on a Saturday) and 2026-07-04 (weekend/holiday) — no trading occurred either day, so a fresh intraday quote isn't available. Resolved by calling IBKR's `get_price_history` instead (also Rule-0-compliant, same broker), which shows the **2026-07-02 close of $219.72** as the most recent completed session — cross-checked against an independent WebSearch aggregator (stockanalysis.com-sourced), which also reported "$219.71–219.72, as of July 4, 2026." **$219.72 is used as the live price.**
2. **`yfinance` unreachable** — the same recurring `curl_cffi` TLS-impersonation `SSLError` already documented across this repo's session history (AAPL, CHTR, WSE, AMD, CDR, CRCL, NKE). Fallback per Rule 0's documented contingency: a third-party financial-data aggregator (stockanalysis.com) cross-checked against figures already verified in the 2026-06-20 ADBE session (e.g. FY2025 FCF $9.852B matched exactly), plus Adobe's own Q2 FY2026 earnings-call transcript for qualitative moat/growth evidence.
3. **No new fundamental data since the 2026-06-20 rescore.** ADBE's fiscal Q3 2026 earnings aren't due until ~mid-September 2026 — no earnings, guidance revision, M&A, or a *newly resolved* management change occurred between 06-20 and 07-04 (the CFO seat remains **interim** — Steven Day, effective since 2026-06-15, with Adobe still searching for a permanent CFO — the same unresolved state already known as of the 06-20 session). The price move since 06-20 (+12.6%, $195.16→$219.72) is well under the 15% unexplained-move Rule 9 threshold. **All FY-level financial inputs (revenue, EBIT, FCF, net income, margins, net debt, FY26 EPS guidance, 5yr avg/low/high PE range) are therefore carried forward unchanged from the verified 2026-06-20 session** rather than re-derived from a data source that has nothing new to report — this is a documented absence of a new data point, not a guess.
4. **D&A used for the Balance Sheet sub-score's EBITDA is FY2025's annual audited figure ($818M)**, used as a TTM proxy — a quarterly D&A breakdown wasn't retrievable this session (yfinance down). D&A is a slow-moving line (FY22–FY25 range: $856M/$872M/$857M/$818M), so this is a reasonable proxy; flagged for transparency rather than invented.
5. **ROIC** was computed two ways for cross-check: this framework's own NOPAT ÷ Invested Capital methodology (Invested Capital = Total Debt + Shareholders' Equity, no cash netting, consistent with the 2026-07-01 NKE session's method) gives **38.9%** (FY2025); the third-party aggregator's own ROIC figure (a different invested-capital definition) gives **59.35%** (FY2025). Both **far exceed the 30% clamp ceiling** for the Profitability sub-score, so the exact figure doesn't change the sub-score result (100.0 either way) — flagged for transparency, not resolved.
6. **Moat Signal checklist** — see §4 for the full cited evidence per signal. One candidate signal (Scale cost advantage) was considered and **not** marked true: Adobe's absolute R&D budget ($4.378B TTM) dwarfs smaller rivals like Figma (~$1.0B total *revenue* run-rate), but this is a budget-size comparison, not a cited **cost-per-unit** figure showing a quantified gap — the framework's evidentiary bar for this signal specifically requires the latter, so it is marked FALSE rather than stretched to TRUE on suggestive-but-imprecise evidence.

## 3. Live data (Rule 0 — fetched first)

| Item | Value | Source |
|---|---|---|
| **Live price used** | **$219.72** | IBKR `get_price_history` (contract_id 265768, NASDAQ), close of 2026-07-02 — the last completed trading session before the 07-03 holiday closure and 07-04 weekend. Cross-checked via WebSearch (independent aggregator, $219.71–72). See Data Gap #1 for why `get_price_snapshot`'s own `last` field wasn't used directly. |
| 52-week high / low | $386.60 / $190.12 | IBKR `get_price_snapshot` `misc_statistics` |
| 13-week high / low | $275.44 / $190.12 | IBKR `get_price_snapshot` `misc_statistics` |
| Shares outstanding | 397.50M (unchanged vs. 06-20 — no new quarter to reflect further buybacks) | stockanalysis.com, cross-checked against carried-forward 06-20 figure |
| Market Cap (computed) | 397.50M × $219.72 = **$87,338.7M** | Computed |

## 4. Quality Score (first-ever computation for ADBE — 2026-06-29 methodology)

ADBE has never been scored under the Quality Score / Composite Score engine (`holdings.md` shows `?` for both columns) — this is its first pass. All financial inputs carried forward from the verified 2026-06-20 session (Data Gap #3); moat/growth qualitative evidence gathered fresh this session.

```
Profitability (25% weight):
  Net Margin (FY2025) = 7,130 / 23,769 = 30.00%
  ROIC (FY2025, framework's own NOPAT/IC method):
    NOPAT = EBIT (FY2025 operating income $8,706M) × (1 − eff. tax rate 18.37%) = 8,706 × 0.8163 = $7,108M
    Invested Capital = Total Debt ($6,648M, FY2025) + Shareholders' Equity ($11,623M, FY2025) = $18,271M
    ROIC = 7,108 / 18,271 = 38.9%   (cross-check: third-party aggregator's own ROIC calc = 59.35% FY2025 — both clamp identically, Data Gap #5)
  NetMargin_Component = clamp((30.00/30)×100) = 100.0
  ROIC_Component       = clamp((38.9/30)×100) = clamp(129.7) = 100.0
  Profitability_Score  = (100.0 + 100.0) / 2 = 100.0   (no FCF-positive cap — FCF-positive every year on record)

Margins (15% weight): Gross margin FY2025 = 21,218/23,769 = 89.27% (consistent with 06-20's 89.4% t.info figure)
  GrossMargin_Score = clamp((89.27/80)×100) = clamp(111.6) = 100.0
  (Already at the clamp ceiling — the 3yr-trend structural-expansion bonus is moot; FY2024 89.03% → FY2025 89.27%, flat-to-slightly-up, not a material trend either way.)

Growth (20% weight): Revenue 3yr CAGR (FY2022 $17,606M → FY2025 $23,769M, carried forward from 06-20) = 10.52%
  Growth_Score = clamp((10.52/25)×100) = 42.08
  TAM-expansion / pricing-power evidence (+10, per Adobe's own Q2 FY2026 earnings call, 11 Jun 2026):
    - "AI-first ARR" grew 3x year-over-year to >$500M
    - Firefly (generative AI) ARR ≈ $300M, growing ~50% quarter-over-quarter
    - GenStudio (enterprise AI workflow) ARR grew >25% year-over-year
    - Creative Cloud Freemium MAU grew from 50M to 90M
    These are Adobe's own disclosed figures (primary source, earnings call), documenting a genuine new revenue surface (usage-based AI monetization) layered on top of the legacy subscription base — real TAM expansion, not asserted. FY2026 revenue guidance ($26.5–26.6B, +11.5–11.9% YoY) is also a step up from FY2025's realized 10.53% — consistent with acceleration, not deceleration, so no −10 penalty considered.
  Growth_Score (with bonus) = 42.08 + 10 = 52.08

Balance Sheet (15% weight): Net Debt = Total Debt ($7,077M) − Cash & ST inv ($5,626M) = +$1,451M (carried forward, most recent available — Q2 FY26 quarter-end, 06-20 session; no fresher balance sheet exists yet, Data Gap #3)
  EBITDA (TTM) = EBIT (TTM, carried) $9,372M + D&A (FY2025 proxy, Data Gap #4) $818M = $10,190M
  Net Debt/EBITDA = 1,451 / 10,190 = 0.1424×
  BalanceSheet_Score = clamp(100×(1 − 0.1424/4)) = clamp(100×0.9644) = 96.44

Moat Signal (15% weight) — checklist, cited evidence only:
  ✓ Market share stable/growing — TRUE. Adobe holds ~58.2% share across content-creation tools (2025); Photoshop alone ~41.74% of the graphic-design-software category; Adobe-branded products collectively >81% of the tracked market; used by 90%+ of creative professionals globally (multiple 2026 market-share trackers, cross-cited via WebSearch). Creative Cloud paid membership grew to ~41M by year-end 2025, with a run-rate of >1M new subscriptions per quarter — share is not just high, it is still growing in absolute terms.
  ✓ Brand premium — TRUE. Adobe raised Creative Cloud/Acrobat Pro/Experience Cloud list prices 12–25% for 2026 (multiple pricing-tracker sources) while the paid subscriber base kept growing (~41M, +1M/quarter run-rate) and Freemium MAU nearly doubled (50M→90M per Adobe's own Q2 FY26 earnings call, cited above) — price increases sustained without documented volume loss is direct pricing-power evidence.
  ✗ Network effect — FALSE. No sufficiently well-documented two-sided-marketplace or user-growth-driven-value mechanism found with real, specific supporting data for Adobe's core Creative Cloud business (a subscription SaaS tool, not a marketplace). Adobe Sign's e-signature workflow (sender → external signer exposure) is a plausible candidate but wasn't found cited with concrete conversion/adoption figures — not marked true on a plausible-but-unquantified mechanism.
  ✓ Switching costs — TRUE. Documented: "a tightly integrated stack from ideation to pro production, creating high switching costs and workflow lock-in"; Creative Cloud Libraries, linked assets across products, and Brand Kit create cross-product lock-in; Adobe's net revenue retention rate is cited at 130%+ — a quantified retention proxy for genuine switching-cost friction (multiple analyst/deep-dive sources, cross-cited via WebSearch).
  ✗ Scale cost advantage — FALSE. Adobe's absolute R&D budget ($4.378B TTM) is far larger than smaller rivals' (e.g. Figma's ~$1.0B total revenue run-rate), but no cited **cost-per-unit** figure (e.g. cost-to-serve, cloud infrastructure cost per user) quantifies an actual gap — a budget-size comparison isn't the same evidentiary bar as the framework requires here (see Data Gap #6). Not marked true.
  Moat_Score = (3/5) × 100 = 60.0

FCF Quality (10% weight): FCF/NI conversion (TTM, carried forward from 06-20) = 10,280/7,229 = 142.2%
  FCFQuality_Score = clamp(((1.422 − 0.40)/0.60)×100) = clamp(170.3) = 100.0

Quality Score = 100.0×0.25 + 100.0×0.15 + 52.08×0.20 + 96.44×0.15 + 60.0×0.15 + 100.0×0.10
              = 25.0 + 15.0 + 10.416 + 14.466 + 9.0 + 10.0
              = 83.882 → rounds to 83.9
```

**Hard disqualifier check** — none fire: FCF/NI conversion is 128–156% across FY2022–2025 (comfortably >70%); Net Debt/EBITDA is 0.14× (far under the 2.5×/4× Debt Gate thresholds); FCF has been positive every year on record (no 3-year-negative disqualifier).

**Quality Score = 83.9 — PASSES the 80.0+ gate** (first-ever computation; comfortably clears, driven by best-in-class profitability, margins, and FCF quality, moderated by only-moderate revenue growth and a moat checklist that is strong but not maximal — 3 of 5 signals cited true).

## 5. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $219.72 / $24.40 (FY2026 non-GAAP EPS guidance midpoint, carried forward — unchanged since 06-20) = 9.005×
EY = 1 / 9.005 = 11.105%
Spread = 11.105% − 4.48% (10Y) = +6.625%
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** (+6.625%) → no +5 additive.

**Step 2 — Rate Regime Modifier**
10Y = 4.48% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for ADBE = +5**

## 6. Phase 02 — Valuation Score (every sub-score shown)

**FCF Yield — 40% weight**
```
FCF (TTM, carried forward) = $10,280M
FCF Yield = 10,280 / 87,338.7 = 11.774%
FCF_Score = clamp(100 × (1 − 11.774/10), 0, 100) = clamp(−17.74, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.40 = **0.0**

**EV/EBIT — 40% weight** (PEG not applicable this session — see below — its 15% weight redistributed here, same as every prior ADBE session)
```
EV = Market Cap $87,338.7M + Net Debt $1,451M = $88,789.7M
EV/EBIT = 88,789.7 / 9,372 (TTM EBIT, carried) = 9.475×
EV/EBIT_Score = clamp((9.475 − 12)/23 × 100, 0, 100) = clamp(−10.98, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.40 = **0.0**

**Forward PE (fallback formula, 5yr avg) — 20% weight**
```
5yr avg PE (auto-computed, carried forward from 06-20 — slow-moving statistic, yfinance unavailable to refresh) = 27.2×
Deviation% = (9.005 − 27.2) / 27.2 × 100 = −66.89%
FwdPE_Score = clamp(50 + (−66.89 × 2.5), 0, 100) = clamp(−117.2, 0, 100) = 0.0
```
(Fallback formula already folds in the Historical PE Modifier — no separate ±10 applied.)
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — not applicable.** Non-GAAP EPS growth FY2024 +14.6% / FY2025 +13.7% — both most-recently-completed years are below the 15% Fast-Grower threshold (carried forward finding, unchanged; FY2026E guidance of +16.6% is a forward projection, not a completed year, so doesn't establish the "3+ years" clean trailing base). **Classified NOT a Fast Grower** → weight redistributed to EV/EBIT (40%, above).

```
Raw weighted score = 0.0 + 0.0 + 0.0 = 0.0
+ Rate Regime Modifier (+5) = 5.0
```

## 7. Upside/Downside Modifier (Expected-Return Modifier) — full calc

Fair-value scenario inputs (bull/base/bear DCF, multiples) carried forward from the 2026-06-20 session — no fundamental change to justify revising WACC, growth, or terminal assumptions (Data Gap #3). Only the live price and the resulting gap/annualization are refreshed.

```
Blended Fair Value (40% DCF PW $449.03 / 60% Multiples $352.74, carried forward) = $391.26
Gap Upside % = (391.26 / 219.72) − 1 = +78.08%
Catalyst window = 2.0 yr (Rule 10 default, unchanged — catalyst = Digital Media segment growth holding ≥~10% through Q3 FY26 [~Sept 2026, ~2.2 months out] and Q4 FY26 [~Dec 2026, ~5 months out], both comfortably inside the 18–24mo window)
Annualized gap = 78.08% / 2.0 = 39.04%/yr
Intrinsic growth = +10%/yr (unchanged, conservative — anchored to revenue CAGR ~10.5%, below the richer EPS growth rate)
Shareholder yield = +2%/yr (unchanged — no dividend; net buyback ≈ 1.6–2%/yr)

E = 39.04% + 10% + 2% = +51.04%/yr
```

**Map E → M** (hurdle H = 10%, E ≥ H branch):
```
M = −15 × clamp((51.04 − 10)/15, 0, 1) = −15 × clamp(2.736, 0, 1) = −15 × 1 = −15.0
```
**Modifier M = −15.0** (hits the −15 floor).

**Guardrails check:**
- Catalyst within 18–24mo? **Yes** — the annual gap didn't widen because the story changed; it widened because the *price* fell relative to an unchanged fair-value estimate over the same catalyst window. Upside-side credit not capped.
- Scenario-weighted (not the rosy point)? **Yes** — same bull/base/bear DCF blend as 06-20, bear case ($251.40) still underwritten with structural AI-disruption assumptions.
- **Robustness note:** even zeroing the annualized-gap component entirely, E = 10% + 2% = 12% > hurdle → M would still be negative. The modifier's sign is not sensitive to the (large) gap estimate.

## 8. Final Valuation Score + Composite Score

```
FINAL VALUATION SCORE = 5.0 (raw + rate gate) + (−15.0) (Upside/Downside) = −10.0 → clamped to the 0.0 floor
```

| | Value |
|---|---|
| Raw weighted | 0.0 |
| Rate Regime Modifier | +5.0 |
| Upside/Downside Modifier | −15.0 (E = +51.04%/yr) |
| **FINAL VALUATION SCORE** | **0.0** (floor) |
| Prior valuation score (06-20) | 0.0 |
| **Quality Score (first computation)** | **83.9 — PASSES 80.0+ gate** |

```
Composite Score = 0.50 × (100 − 83.9) + 0.50 × 0.0 = 0.50 × 16.1 + 0.0 = 8.05
  → exactly on a ".X5" boundary → round UP (conservative) → 8.1
```

**Composite Score = 8.1** — falls in the **0.0–29.9 "Very Cheap"** band → **BUY — Full position 6–8%** (Phase 03 action table). This is ADBE's first Composite Score; the raw valuation score alone (0.0, unchanged from 06-20) would have implied the same action band on its own, and the newly-computed Quality Score (83.9, strong) reinforces rather than overrides that conclusion — the Quality axis was the open unknown, and it resolves favorably.

## 9. Fair Value & Order Setup (BUY action — full setup required)

### Fair Value (carried forward, no fundamental change to justify a revision)
```
Bear DCF $251.40 | Base DCF $443.72 | Bull DCF $657.30  (unchanged scenario assumptions, 06-20)
PW DCF FV = 0.25×657.30 + 0.50×443.72 + 0.25×251.40 = $449.03
Multiples-based FV = $352.74 (Forward-PE comp $366.00 / EV-EBIT comp $326.43 / FCF-yield comp $365.80, avg)
Blended FV = 0.40×449.03 + 0.60×352.74 = $391.26
```

### Order setup
```
Margin of Safety = 17.5% (midpoint, 15–20% band for Score 0.0–29.9)
Buy Price (ceiling) = $391.26 × (1 − 0.175) = $322.79
Live price $219.72 is far below the ceiling → ENTER NOW (effective entry = live price, not the ceiling)
Primary Sell Target = Blended FV = $391.26
Bull-Case Trim Target = Bull DCF $657.30 × 0.90 = $591.57
Stop Loss = Live Price × (1 − 0.225) = $219.72 × 0.775 = $170.28   (22.5%, midpoint of 20–25% band)
R/R = (391.26 − 219.72) / (219.72 − 170.28) = 171.54 / 49.44 = 3.47 : 1   (≥ 2:1 ✓)
```

### Position sizing — top-up toward the partial-fill target
```
Portfolio Value (combined, holdings.md last sync 2026-06-28) = $54,891.48
Max $ Risk (1.5%) = $823.37
Risk/share = $49.44
Risk-based size = 823.37 / 49.44 = 16.66 shares
Allocation cap (6–8% band): 6% → 15.0 sh | 8% → 20.0 sh — risk-based size (16.66) sits inside the cap band, so it governs (min rule)
Full target (rounded down, conservative) = 16 shares
Held = 10 shares → TOP-UP = 6 shares
Top-up cost = 6 × $219.72 = $1,318.32
Resulting position = 16 × $219.72 = $3,515.52 = 6.40% of portfolio
```
**Cap cross-check:** 6.40% sits inside the 6–8% Very Cheap band and far under the 15% hard cap (Upgrade 7). Note this is a **smaller** target than the 06-20 session's ~17-share figure — not because ADBE got less attractive, but because the risk-based calc (fixed $ risk ÷ risk-per-share) tightens as price rises faster than portfolio value: risk-per-share grew +12.6% (with the price) while the risk budget only grew ~2.3% (with the portfolio). This is the position-sizing formula behaving as designed, not a change in conviction.

### Order Setup Checklist
```
[x] Composite Score (Quality 83.9 + Valuation 0.0):  8.1   (≤ 49.9 ✓)
[x] Expected annual return E / catalyst window:      +51.04% / 2 yr
[x] Upside/Downside Modifier applied:                −15.0
[x] DCF Fair Value (PW):                             $449.03
[x] Multiples-Based Fair Value:                      $352.74
[x] Blended Fair Value:                              $391.26
[x] Margin of Safety %:                              17.5%
[x] BUY PRICE (ceiling; live already far below):     $322.79
[x] PRIMARY SELL TARGET:                             $391.26
[x] BULL-CASE TRIM TARGET:                            $591.57
[x] STOP LOSS:                                        $170.28
[x] Risk/Reward Ratio:                                3.47:1  (≥ 2:1 ✓)
[x] Max $ Risk:                                       $823.37
[x] POSITION SIZE (top-up shares):                    6 (to reach a 16-sh target)
[x] POSITION SIZE ($):                                $1,318.32 top-up → 6.40% total
[x] Thesis invalidation triggers:                     see §10
```

## 10. Action, Thesis Status & Recommendation

**Recommendation: CONFIRMED BUY — top up ~6 shares (~$1,318, to reach a 16-share / 6.40% target). Composite Score 8.1 ("Very Cheap").**

ADBE clears its **first-ever Quality Score gate decisively** (83.9 vs. the 80.0 bar) — this was the open question this session was designed to resolve, since the ticker had a numeric valuation score but no quality read on file. The result confirms the qualitative case made in the 06-12 and 06-20 sessions (best-in-class margins, ROIC, and FCF conversion; a real, cited moat on 3 of 5 checklist signals) rather than surfacing a new concern. Combined with the unchanged-floor Valuation Score (0.0) and a still-large expected annual return (E = +51.0%/yr, driven by a ~78% gap to a conservatively-blended fair value even after ADBE's price already rose +12.6% since 06-20), the Composite Score (8.1) sits deep in the Very Cheap / Full-position band.

**Thesis invalidation triggers (Phase 06 / stop), unchanged from 06-20:**
- Digital Media revenue growth decelerates toward mid-single-digits without a non-AI one-off cause (2 consecutive quarters) → thesis broken
- Gross margin falls >3pp structurally, or FCF/NI conversion <70% for 2 consecutive quarters
- Net debt/EBITDA rising materially on debt-funded buybacks while growth slows
- Price through the $170.28 stop

All final-decision authority rests with the human investor; funding is the investor's call.

## 11. Watchlist & stale-score disposition

- **Watchlist:** a new dated entry ([watchlist/in-portfolio/ADBE/ADBE-2026-07-04.md](../watchlist/in-portfolio/ADBE/ADBE-2026-07-04.md)) was created rather than an appended "last checked" line — this is ADBE's first-ever Quality Score and Composite Score computation, which changes what actually governs the Phase 03/05 action tables going forward (the Composite Score, not the raw valuation score) — a materially different reasoning basis even though the raw valuation-score number (0.0) is numerically unchanged from 06-20.
- **Stale-score mark:** this rescore computes ADBE's Quality Score and Composite Score under the current (2026-06-29) methodology for the first time, so **ADBE's row in [watchlist/STALE.md](../watchlist/STALE.md) should be deleted and its `⚠️ STALE SCORE` banner removed** — done in the watchlist entry file itself (no banner carried into the new dated file); the STALE.md registry row deletion is deferred to the orchestrator per this session's scope.

## 12. Next review trigger

- **Q3 FY2026 earnings (~mid-September 2026)** — mandatory re-score (Rule 9). Check Digital Media segment growth ≥~10% (the catalyst underlying the Upside/Downside Modifier).
- **A permanent CFO appointment** — still open (interim Steven Day as of 2026-06-15); watch for a strategy/cost-discipline signal when resolved (management-change Rule 9 trigger).
- **>15% unexplained move from $219.72** in either direction — immediate re-score (Rule 9).
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

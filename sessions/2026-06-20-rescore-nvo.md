# RESCORE — NVO (Novo Nordisk A/S, US-listed ADR) — 2026-06-20

**Task type:** RESCORE (single ticker)
**Date:** 20 Jun 2026 (Saturday — markets closed; most recent completed-session close used as the live price)
**10Y US Treasury Yield:** 4.45% (2026-06-18 close — TradingEconomics/CNBC; the Fed held rates, 10Y hovering ~4.44–4.46%)
**Rate Regime Modifier in effect:** +5 (10Y in the 3.5–5% bracket)
**Prior score:** 35.8 (2026-06-11 recompute on the 0–100 scale; band: Cheap → BUY) — itself a rescale of the 2026-06-07 baseline "Score 4" under a value-trap/broken-thesis override.
**This rescore applies the new Upside/Downside Modifier (Expected-Return Modifier), added 2026-06-20.**

ADR note: NVO is a Danish ADR — an American Depositary Receipt, i.e. a US-traded proxy share for the foreign (Copenhagen-listed) stock. All figures below are in USD, with the underlying audited financials (reported in Danish kroner, DKK) converted at the live USD/DKK rate. One NVO ADR = one Novo Nordisk B-share.

---

## 1. Live Data First (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price (NVO ADR)** | **$43.19** | yfinance daily close 2026-06-18 (most recent completed session). Web cross-check: Investing.com quoted $42.91 intraday / $43.52 prior close on 18 Jun. ⚠️ IBKR `get_price_snapshot` (conid 10611, NYSE) was **permission-denied** this session, so the yfinance/web close is the fallback per the prompt's fallback chain. |
| 52-week range | **$35.12 – $74.38** | yfinance / Investing.com (yfinance `fiftyTwoWeekHigh` showed a stale $71.8; the web $74.38 is used) |
| Analyst consensus PT | **mean $47.36** (low $39.92 / high $63.57; 12 analysts, "Buy", 5 buy / 0 sell) | Investing.com / yfinance `targetMeanPrice` $47.18 |
| US 10Y Treasury yield | **4.45%** | TradingEconomics/CNBC, 2026-06-18 |
| USD/DKK FX | **6.5157** | yfinance `USDDKK=X`, 2026-06-19 close |

**Decode (plain English, first use):** *FCF* = free cash flow (operating cash flow minus capital spending — the cash a business actually generates after maintaining/expanding itself). *EV/EBIT* = enterprise value ÷ earnings before interest & tax (a takeover-style price tag on operating profit). *Forward PE* = price ÷ next-12-months earnings per share. *PEG* = PE ÷ earnings growth rate (a Fast-Grower yardstick — under ~1 is cheap-for-the-growth, over ~2 is expensive). *MoS* = margin of safety (discount to fair value demanded before buying). *R/R* = reward-to-risk ratio. *pp* = percentage points. *ROIC* = return on invested capital. *GLP-1* = the obesity/diabetes drug class (Wegovy/Ozempic) that is Novo's core franchise.

---

## 2. Data Gaps Flagged (never invent)

1. **IBKR live snapshot denied** — used yfinance/web close as the Rule 0 price (fallback chain followed). Flagged.
2. **yfinance currency-mixing** — `t.info` reports DKK-denominated financials (enterpriseValue, totalDebt, ebitda, a *negative* `freeCashflow`) against the USD ADR market cap, producing nonsensical composites (e.g. EV/EBITDA 1.82×). **Ignored.** All ratios below were rebuilt by hand from the audited DKK statements (`t.financials`/`t.cashflow`/`t.balance_sheet`) converted at USD/DKK 6.5157 — internally consistent.
3. **5yr-avg-PE auto-reconstruction failed** — the `get_earnings_dates` method returns "Reported EPS" in **DKK** for NVO while price history is in **USD**, so the reconstructed PE series (1.9–6.0×) is a currency artifact and was discarded. Used a **sourced** 5yr-avg PE instead: ~26.8× (fullratio) to ~31.2× (intellectia); midpoint **~28×** adopted, range shown as sensitivity. Not invented — externally sourced and cross-checked against the prior pass's ~23× (10yr) and the current trailing PE ~10.2–12.2×.
4. **Owner-Earnings maintenance/growth CapEx split not available** — FY2025 FCF is depressed by a CapEx surge (see §4 FCF). No audited maintenance-vs-growth split exists, so I did **not** invent one; scored on reported FCF (conservative) and showed a normalized sensitivity.
5. **Share count** — yfinance `sharesOutstanding` 3.353B is a float/ADR-equivalent artifact; market cap reconciles only on the **total** ordinary share count 4.443B ($43.19 × 4.443B = $191.9B, matching yfinance `marketCap` $191.2B). Total-share basis used throughout.

---

## 3. Standard Re-Score Inputs (USD-consistent, FY2025 audited)

| Metric | Value | Note |
|---|---|---|
| Market cap | **$191.9B** | $43.19 × 4.443B total shares |
| Net debt | **$14.7B** (DKK 95.9B) | rose sharply (Catalent acquisition + buybacks); was near-zero pre-2024 |
| Enterprise value | **$206.6B** | mcap + net debt |
| EBIT (FY2025) | $20.68B (DKK 134.75B) | |
| **EV/EBIT** | **9.99×** | ≤12× → cheapest band |
| FCF (FY2025) | $4.45B (DKK 28.99B) | **collapsed** from DKK 69.7B (2024) / 70.0B (2023) — CapEx surged DKK 51B→**90B** (GLP-1 capacity build); operating cash flow held at DKK 119B |
| **FCF yield (reported FY2025)** | **2.32%** | scored input (conservative) |
| FCF yield (3yr avg) | 4.50% | normalized sensitivity — the representative cash-generation read |
| **Forward PE** | **~13.0×** | sourced (financecharts 12.87×, yfinance 13.07×) |
| Trailing PE | ~12.2× | EPS DKK 23.05 → $3.54 ADR |
| **5yr avg PE** | **~28×** | sourced range 26.8–31.2× |
| **Rev CAGR 3yr** | **20.4%** | DKK 177.0B→309.1B (2022→2025) |
| **EPS CAGR 3yr** | **23.5%** | DKK 12.22→23.05 |
| ROIC | very high (~70%+; ROE 71.4%) | qualitative — wide moat intact |
| Gross margin | **83.2%** | |
| Net margin | **33.1%** | |
| Net debt / EBITDA | **0.61×** | well inside the 2.5× gate |
| FCF/NI conversion | 2025 **28.3%** / 2024 69.0% / 2023 83.7% | 2025 dip is the CapEx surge, not earnings quality |
| Dividend yield | ~4.17% | |
| Current weight | 0.40% | per holdings.md |

**Fundamental context since last review:** The franchise economics are **intact** (83% gross margin, 44% EBIT margin, ~70% ROIC, 0.61× net-debt/EBITDA). What has changed is the **growth trajectory**: a former 20%+ grower has inflected to a flat-to-slightly-down 2026 (first-ever guided revenue decline flagged in the prior pass), driven by (a) GLP-1 share loss to Eli Lilly (tirzepatide/Zepbound), (b) US net-pricing pressure, and (c) the CagriSema (next-gen obesity candidate) disappointment. This is the crux the rescore must judge: **a genuine de-rating of a still-excellent business, or structural impairment.** Read: **de-rating with stalled — not broken — fundamentals.** Margins, returns and balance sheet show no structural damage; the question is purely forward growth, and the bear case (continued Lilly share loss + price erosion) is underwritten explicitly in §5.

---

## 4. Rate Environment Gate

```
EY = 1 ÷ Forward PE = 1 ÷ 13.0 = 7.69%
Spread = EY − 10Y = 7.69% − 4.45% = +3.24%   (threshold ≥ +1.5%)
```
- **Step 1 — Earnings Yield Spread: PASS** (+3.24%, comfortably clear) → no +5 yellow-flag. NVO remains the rare name in the book that clears this bar.
- **Step 2 — Rate Regime Modifier: +5** (10Y 4.45% in the 3.5–5% bracket).

---

## 5. Full Valuation Score — every sub-score

```
FCF_Score    = clamp(100 × (1 − 2.32/10), 0, 100)              = 76.80   (weight 40%)
EV/EBIT_Score= clamp((9.99 − 12)/23 × 100, 0, 100)             =  0.00   (weight 25%)
FwdPE_Score  = clamp(50 + ((13.0 − 28)/28 × 100) × 2.5, 0,100) =  0.00   (dev −53.6%; weight 20%)
PEG_Score    = clamp((3.13 − 0.5)/2.0 × 100, 0, 100)           = 100.00  (weight 15%)
```

**PEG eligibility (the deliberate call):** NVO has clean, non-distorted EPS growth >15% for well over 3 years (3yr EPS CAGR 23.5%) on real audited earnings → it **DOES qualify as a Fast Grower**, so the PEG sub-score goes **live** (15% weight retained, not redistributed). The *live forward* PEG is **3.13** (yfinance — forward PE ÷ the now-collapsed forward growth estimate). That high PEG is the **correct economic signal**: when a former Fast Grower's growth inflects to flat/negative, PEG should blow out and *penalize* the score — that is exactly what a forward-looking PEG is for. Using the *trailing* 23.5% CAGR would give PEG ≈ 0.55 (sub-score 2.7), but valuing a *forward* price against *backward* growth is the textbook value-trap error, so it is shown only as a sensitivity, **not** the scored input.

```
Raw weighted = (76.80 × 0.40) + (0.00 × 0.25) + (0.00 × 0.20) + (100.00 × 0.15)
             = 30.72 + 0.00 + 0.00 + 15.00
             = 45.72
```

*Sensitivities (not the scored figure):* FCF on the normalized 3yr-avg yield (4.50%) → FCF_Score 55.0 → raw 37.0. PEG redistributed to EV/EBIT (if treated as non-Fast-Grower) → raw 30.72. The chosen treatment (forward PEG live) is the most conservative reading and the one that honestly lets stalled growth flow into the score.

---

## 6. Upside/Downside Modifier (Expected-Return Modifier) — REQUIRED

**Fair-value scenarios (multiples-based, ADR USD; Rule 7 weighting; bear underwritten honestly).** Forward ADR EPS base ≈ $3.45 (2026 flat-to-slight-decline):

| Scenario | Wt | Assumption | EPS | PE | FV |
|---|---|---|---|---|---|
| Bull | 25% | GLP-1 share stabilizes; oral semaglutide (Wegovy pill) US ramp + CagriSema reposition revive growth; re-rate | $3.65 | 18× | **$65.70** |
| Base | 50% | Low-single-digit growth; multiple holds | $3.45 | 14× | **$48.30** |
| Bear | 25% | **Structural-impairment underwrite** — continued Lilly share loss + US net-price erosion; de-rate | $3.00 | 9× | **$27.00** |

```
PW Fair Value = 0.25×65.70 + 0.50×48.30 + 0.25×27.00 = $47.33
```
Sanity (Rule 4 / Rule 0 cross-check): PW FV $47.33 lands essentially **on the analyst consensus mean ($47.36)** and inside the $39.9–$63.6 PT range — the scenario weights are not rosy; the bull is below the Street high, the bear sits below the Street low.

```
Gap Upside %  = (47.33 ÷ 43.19) − 1                     = +9.6%
Catalyst window = 2 yr (oral-semaglutide US launch ramp, CagriSema repositioning data,
                  2027 growth re-acceleration vs. comps — all inside 18–24 months → upside credit allowed, no −5 cap)
Annualized gap = 9.6% ÷ 2                                = +4.8%/yr
Intrinsic growth = +4.0%/yr   (former 20%+ grower now inflected; conservative low-single-digit forward)
Shareholder yield = +4.3%      (dividend ~4.17% + minimal net buyback — buybacks largely paused for Catalent/CapEx)

E = 4.8 + 4.0 + 4.3 = +13.1%/yr
```

**Map to M (hurdle H = 10%):** E ≥ H, so `M = −15 × clamp((13.1 − 10)/15, 0, 1) = −15 × 0.207 = −3.09`.

So the modifier is a **modest −3.1** — expected return only slightly clears the 10% hurdle. The honestly-weighted bear case ($27, 25% weight) deliberately keeps E from being large, so the modifier informs but does not manufacture a strong buy. (Catalyst guardrail satisfied: documented catalyst within window; bull/base/bear used, not the rosy point; full calc shown.)

---

## 7. Final Score & Action

```
Final = Raw 45.72 + Rate Regime +5 + Upside/Downside −3.09 = 47.63 → round 47.6
```

| | |
|---|---|
| **FINAL SCORE** | **47.6** |
| Prior score | 35.8 |
| Band | **Cheap (30.0–49.9) → BUY, standard 3–5%** (per Action Table) |
| Action category | **HOLD existing 0.40% — NO ADD at current price** (see order-setup discipline below) |
| Changed vs prior? | Score moved up 35.8 → 47.6 (still same Cheap/BUY band); **action category unchanged** (no add) |

**Why the score rose 35.8 → 47.6 but the conclusion is still "no add":** the prior score omitted PEG entirely (redistributed it away on a "broken thesis" call); applying the live forward PEG (100.0 sub-score) correctly adds the stalled-growth penalty (+15.0 raw → +5.7 net of the new modifier). The Upside/Downside Modifier then nets out small (−3.1) because the bear case is underwritten honestly. Net effect: NVO reads as **cheap with only modest expected upside**, not a screaming buy — which is the correct, non-value-trap reading of a de-rated-but-stalled compounder.

---

## 8. Order Setup (BUY-band name)

| Item | Value |
|---|---|
| Blended / PW Fair Value | **$47.33** |
| Margin of Safety | **30%** (Score 30–49.9 band; top of range given elevated thesis risk) |
| **Buy (limit) Price** | **$33.13** (= 47.33 × 0.70) |
| Primary Sell Target (FV) | **$47.33** |
| Bull-case Trim Target (bull × 0.90) | **$59.13** |
| Stop Loss (Buy × (1 − 28%)) | **$23.85** |
| Live price vs buy price | $43.19 is **~30% ABOVE** the $33.13 buy price |
| **R/R at buy price** | (47.33 − 33.13) ÷ (33.13 − 23.85) = **1.53:1** — **below the 2:1 minimum** |
| R/R at live price (enter now) | 0.21:1 — far below minimum |

**Order discipline conclusion:** Per fair-value Step 2, a Score-30–49.9 name is "approaching buy price → set limit order," **not** "enter now" — and the live price ($43.19) is well above the disciplined buy price ($33.13). Worse, the R/R *even at the limit price* is only 1.53:1, below the 2:1 gate, so the framework says **do not enter** (wait for a lower entry / tighter stop, or pass). **Therefore: no new capital; HOLD the existing 0.40% tracking position.** No limit order placed — it would not clear R/R. Position size methodology (3–5% cap, 1.5% risk) is moot until price approaches a level where R/R ≥ 2:1 (roughly ≤ $37 against this FV/stop, worth re-checking on the next print).

---

## 9. Next Review Trigger

- **Next quarterly earnings release** — standard re-score; specifically watch (a) GLP-1 US script share vs. Lilly, (b) US net-price/rebate trajectory, (c) oral-semaglutide launch ramp, (d) any further guidance revision (Rule 9 trigger). These resolve the de-rating-vs-impairment question.
- **Rule 9 fundamental triggers** in the interim: guidance revision, CagriSema/pipeline data readout, management change, or a material M&A/regulatory (US pricing/IRA) shock.
- **Price trigger:** if NVO falls toward ~$37 or below, re-run the order setup — R/R may clear 2:1 and convert the standing "no-add" into an actionable limit entry.
- This name remains a candidate for an `override-log.md` note: the score-band ("BUY") and the order-discipline action ("no add") diverge, which is worth tracking.

*Session complete. No live IBKR snapshot available (permission denied) — Rule 0 satisfied via yfinance close + web cross-check, flagged. portfolio/holdings.md intentionally NOT edited (orchestrator owns it).*

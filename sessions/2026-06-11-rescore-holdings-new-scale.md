# RESCORE — Holdings recomputed under the new 0.0–100.0 continuous score (no new live prices) — 2026-06-11

**Task type:** RESCORE (re-computation under new formulas, not a fresh data pull)
**Date:** 11 Jun 2026
**Trigger:** Framework change — Phase 02 valuation score moved from a 1–10 integer scale to a continuous 0.0–100.0 scale (see [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md)). After an initial mechanical placeholder conversion of `holdings.md`'s "Last Score" column, this session replaces those placeholders with **real computations** of every sub-score and the final score, run against the same underlying metrics already gathered on 2026-06-07.

**⚠️ Not a fresh Rule 0 pull.** No new live prices, market caps, or fundamentals were sourced in this session — every input below is taken verbatim from [sessions/2026-06-07-rescore-full-portfolio.md](2026-06-07-rescore-full-portfolio.md) (AMZN, CSGP, DUOL, GOOG, META, MSFT, NFLX, NKE, NOW, NVO, SPGI, SPOT, UBER, V, ZS) and [sessions/2026-06-07-rescore-nvda.md](2026-06-07-rescore-nvda.md) (NVDA). All caveats and low-confidence flags from those sessions still apply and are carried forward below. A full `/rescore` with fresh Rule 0 prices remains the next step, especially for **CSGP, GOOG, and SPOT** (see flags at the end).

**Rate Regime Modifier:** +5 (10Y Treasury 4.55%, 2026-06-05 close, in the 3.5–5% bracket) — applied identically to every ticker below, per [framework/strategy.md](../framework/strategy.md).

**Formulas used** (full detail in [framework/valuation-scoring.md](../framework/valuation-scoring.md)):

```
FCF_Score      = clamp(100 × (1 − FCF_Yield% / 10), 0, 100)
EV/EBIT_Score  = clamp((EV/EBIT − 12) / 23 × 100, 0, 100)
PEG_Score      = clamp((PEG − 0.5) / 2.0 × 100, 0, 100)

FwdPE_Score (primary, 10yr Low/High range available):
  clamp((FwdPE − 10yrLow) / (10yrHigh − 10yrLow) × 100, 0, 100), then ±10 Historical PE Modifier

FwdPE_Score (fallback, only a single 10yr avg PE available):
  Deviation% = (FwdPE − 10yrAvgPE) / 10yrAvgPE × 100
  FwdPE_Score = clamp(50 + Deviation% × 2.5, 0, 100)
  (folds in the Historical PE Modifier — do not also apply ±10)

FwdPE_Score (no usable 10yr PE history at all): = 50.0 (neutral, flagged)

Final Score = (FCF_Score × 0.40) + (EV/EBIT_Score × W_evebit) + (FwdPE_Score × 0.20)
              + (PEG_Score × 0.15, if Fast Grower) + Rate Regime Modifier (+5)

  where W_evebit = 0.25 if PEG_Score applies, else 0.40 (PEG's 15% redistributed to EV/EBIT)

Rounding: nearest 0.1, .X5 rounds up, min 0.0 max 100.0
```

No metric below was re-derived, estimated, or invented — every number is either quoted directly from the 2026-06-07 sessions or is a mechanical application of the formulas above to those quoted numbers.

---

## AMZN — current weight 10.49%

**Inputs** (from [2026-06-07 full-portfolio session](2026-06-07-rescore-full-portfolio.md), AMZN section):
- FCF yield = 0.292%
- EV/EBIT = 32.7×
- Forward PE ≈ 29.3×, 10-yr avg PE ≈ 70× (midpoint of a wide 42.07×/73.82×/97.13× spread)
- Not a confirmed Fast Grower (revenue CAGR ~12.1%) → PEG redistributed to EV/EBIT (40%)

**Calculations:**
```
FCF_Score     = clamp(100 × (1 − 0.292/10), 0, 100)        = 100 × 0.9708       = 97.08
EV/EBIT_Score = clamp((32.7 − 12)/23 × 100, 0, 100)         = (20.7/23) × 100    = 90.0
FwdPE: Deviation% = (29.3 − 70)/70 × 100 = −58.14%
       FwdPE_Score = clamp(50 + (−58.14 × 2.5), 0, 100)     = clamp(−95.36,…)    = 0.0
PEG_Score = n/a (redistributed)

Raw = (97.08 × 0.40) + (90.0 × 0.40) + (0.0 × 0.20) + 0
    = 38.832 + 36.0 + 0.0
    = 74.832
+ Rate Regime Modifier (+5) = 79.832
```

**Final Score = 79.8 → Expensive (70.0–79.9) → Trim 25–30%** (band unchanged from placeholder)

🚩 **Owner Earnings flag (Upgrade 1, carried forward):** AMZN's raw FCF cratered 76.6% YoY on an AI-capex surge — the FCF_Score of 97.08 (the single largest input here) is likely overstated, but no maintenance-vs-growth-capex split was sourced to compute an Owner-Earnings-adjusted figure. Flagged, not patched.

---

## CSGP — current weight 1.57%

**Inputs** (from [2026-06-07 full-portfolio session](2026-06-07-rescore-full-portfolio.md), CSGP section):
- FCF yield = 0.879%
- EV/EBITDA (proxy for EV/EBIT, GAAP operating loss) = 30.3×
- Forward PE / 10-yr avg PE: both built on a near-zero, distorted GAAP earnings base — **no usable reference** → no-history fallback
- PEG (0.13) flagged as not trustworthy, ambiguous Fast-Grower status → redistributed to EV/EBIT (40%)

**Calculations:**
```
FCF_Score     = clamp(100 × (1 − 0.879/10), 0, 100)         = 100 × 0.9121       = 91.21
EV/EBIT_Score = clamp((30.3 − 12)/23 × 100, 0, 100)          = (18.3/23) × 100    = 79.5652
FwdPE_Score   = 50.0 (no-history fallback, neutral, flagged)
PEG_Score = n/a (redistributed)

Raw = (91.21 × 0.40) + (79.5652 × 0.40) + (50.0 × 0.20) + 0
    = 36.484 + 31.82608 + 10.0
    = 78.31008
+ 5 = 83.31008
```

**Final Score = 83.3 → Very Expensive (80.0–89.9) → Trim to 50%**

🚩 **Band change: was Expensive (77.7, Trim 25–30%) → now Very Expensive (83.3, Trim to 50%).** Three of four inputs here are substitutes/neutral placeholders (EV/EBITDA proxy, neutral FwdPE) on top of a distorted near-zero GAAP earnings base — low confidence. Recommend a fresh Rule 0 pull and earnings-base sanity check before executing this trim.

---

## DUOL — current weight 7.60%

**Inputs** (from [2026-06-07 full-portfolio session](2026-06-07-rescore-full-portfolio.md), DUOL section):
- FCF yield = 7.36%
- EV/EBIT = 26.79×
- Forward PE ≈ 34.74×; only ~5 years of public history → no usable 10yr PE reference → no-history fallback
- Fast Grower confirmed (revenue CAGR 29.8%) → PEG = 1.49 → PEG_Score applies, EV/EBIT stays 25%

**Calculations:**
```
FCF_Score     = clamp(100 × (1 − 7.36/10), 0, 100)          = 100 × 0.264        = 26.4
EV/EBIT_Score = clamp((26.79 − 12)/23 × 100, 0, 100)         = (14.79/23) × 100   = 64.2957
FwdPE_Score   = 50.0 (no-history fallback, neutral, flagged)
PEG_Score     = clamp((1.49 − 0.5)/2.0 × 100, 0, 100)        = (0.99/2.0) × 100   = 49.5

Raw = (26.4 × 0.40) + (64.2957 × 0.25) + (50.0 × 0.20) + (49.5 × 0.15)
    = 10.56 + 16.073925 + 10.0 + 7.425
    = 44.058925
+ 5 = 49.058925
```

**Final Score = 49.1 → Cheap (30.0–49.9) → Standard position 3–5%** (band unchanged from placeholder)

🚩 **Sizing flag (carried forward):** a Cheap-band BUY signal, but DUOL is already at 7.60% — within a hair of the 8% hard cap. No add recommended; HOLD.

---

## GOOG — current weight 0.68%

**Inputs** (from [2026-06-07 full-portfolio session](2026-06-07-rescore-full-portfolio.md), GOOG section — ⚠️ citation-recovery gap, figures recovered from prior research notes, URLs not retained, flagged for re-verification):
- FCF yield = 1.65%
- EV/EBIT ≈ 34.5×
- Forward PE = 25.86×, 10-yr avg PE ≈ 28×
- PEG NOT FOUND → redistributed to EV/EBIT (40%)

**Calculations:**
```
FCF_Score     = clamp(100 × (1 − 1.65/10), 0, 100)          = 100 × 0.835        = 83.5
EV/EBIT_Score = clamp((34.5 − 12)/23 × 100, 0, 100)          = (22.5/23) × 100    = 97.8261
FwdPE: Deviation% = (25.86 − 28)/28 × 100 = −7.6429%
       FwdPE_Score = clamp(50 + (−7.6429 × 2.5), 0, 100)     = clamp(30.893,…)    = 30.893
PEG_Score = n/a (redistributed)

Raw = (83.5 × 0.40) + (97.8261 × 0.40) + (30.893 × 0.20) + 0
    = 33.4 + 39.13044 + 6.1786
    = 78.70904
+ 5 = 83.70904
```

**Final Score = 83.7 → Very Expensive (80.0–89.9) → Trim to 50%**

🚩 **Band change: was Expensive (77.7, Trim 25–30%) → now Very Expensive (83.7, Trim to 50%).** Position is tiny (0.68%) so the practical impact is small, but several inputs here carry the citation-recovery flag — re-verify EV/EBIT and market cap at next touch before executing.

---

## META — current weight 5.47%

**Inputs** (from [2026-06-07 full-portfolio session](2026-06-07-rescore-full-portfolio.md), META section — ⚠️ citation-recovery gap, entire data table recovered from prior research notes):
- FCF: two readings recovered, $46.0B and $43.6B, against market cap ≈ $1,506.2B
- EV/EBIT = 18.09×
- Forward PE ≈ 18.22×, 10-yr avg PE ≈ 29×
- Fast-Grower status not confirmed (one-off tax effects distort EPS growth) → redistributed to EV/EBIT (40%)

**Calculations:**
```
FCF yield 1 = 46.0 / 1506.2  = 3.0542%
FCF yield 2 = 43.6 / 1506.2  = 2.8952%
avg FCF yield = (3.0542 + 2.8952) / 2 = 2.9747%
FCF_Score = clamp(100 × (1 − 2.9747/10), 0, 100)            = 100 × 0.70253     = 70.253

EV/EBIT_Score = clamp((18.09 − 12)/23 × 100, 0, 100)         = (6.09/23) × 100   = 26.4783
FwdPE: Deviation% = (18.22 − 29)/29 × 100 = −37.1724%
       FwdPE_Score = clamp(50 + (−37.1724 × 2.5), 0, 100)    = clamp(−42.93,…)   = 0.0
PEG_Score = n/a (redistributed)

Raw = (70.253 × 0.40) + (26.4783 × 0.40) + (0.0 × 0.20) + 0
    = 28.1012 + 10.59132 + 0.0
    = 38.69252
+ 5 = 43.69252
```

**Final Score = 43.7 → Cheap (30.0–49.9) → Standard position 3–5%** (band unchanged from placeholder)

🚩 **Owner Earnings flag (Upgrade 1, carried forward):** same maintenance/growth-capex-split data gap as AMZN — raw FCF used as proxy, no Owner-Earnings adjustment computed. **Rate Environment Gate flag (carried forward):** gate FAILs at +0.94% (just short of +1.5%), so even though this is a Cheap-band score, no fresh capital should be added at current pricing — HOLD at current size.

---

## MSFT — current weight 16.84% (🚨 >2× the 8% hard cap)

**Inputs** (from [2026-06-07 full-portfolio session](2026-06-07-rescore-full-portfolio.md), MSFT section):
- Owner Earnings ≈ $95B vs. market cap ≈ $3,071B (primary, per Upgrade 1 — see flag below)
- Raw FCF $71.611B vs. same market cap (alternate reading, shown for completeness)
- EV/EBIT = 23.63×
- Forward PE ≈ 22.5×, 10-yr avg PE ≈ 31.5×
- Not treated as a Fast Grower at this scale → redistributed to EV/EBIT (40%)

**Calculations (Owner Earnings primary, per Upgrade 1):**
```
FCF_Score (Owner Earnings) = clamp(100 × (1 − (95/3071 × 100)/10), 0, 100)
  95/3071 = 3.09345% → 100 × (1 − 0.309345) = 69.0655

EV/EBIT_Score = clamp((23.63 − 12)/23 × 100, 0, 100)         = (11.63/23) × 100  = 50.5652
FwdPE: Deviation% = (22.5 − 31.5)/31.5 × 100 = −28.5714%
       FwdPE_Score = clamp(50 + (−28.5714 × 2.5), 0, 100)    = clamp(−21.43,…)   = 0.0
PEG_Score = n/a (redistributed)

Raw = (69.0655 × 0.40) + (50.5652 × 0.40) + (0.0 × 0.20) + 0
    = 27.6262 + 20.22608 + 0.0
    = 47.85228
+ 5 = 52.85228
```

**Final Score = 52.9 → Fair Value (50.0–69.9) → Hold, watch only** (band unchanged from placeholder)

*Alternate (raw FCF, not used as primary):* FCF_Score = 100 × (1 − 2.332/10) = 76.68 → Raw = (76.68×0.40) + (50.5652×0.40) + 0 = 30.672 + 20.22608 = 50.89808 → +5 = 55.9 → still Fair Value. Both readings land in the same band, so the choice doesn't change the action.

🚩 **🚨 Structural cap breach (carried forward, independent of valuation):** MSFT is 16.84% of the portfolio vs. an 8% hard cap (Upgrade 7) — more than double. The valuation score itself says HOLD/watch-only, but the position size alone is a standing compliance issue that needs a dedicated REBALANCE/structural-reduction plan, as flagged in the 2026-06-07 session.

---

## NFLX — current weight 1.82%

**Inputs** (from [2026-06-07 full-portfolio session](2026-06-07-rescore-full-portfolio.md), NFLX section):
- FCF yield = 2.74%
- EV/EBIT = 26.32×
- Forward PE ≈ 24.6×, single-sourced 10-yr avg PE = 93.64× (flagged as likely distorted by hyper-growth-era multiples and the Nov 2025 10-for-1 split)
- Not a confirmed Fast Grower (revenue CAGR ~12.9%, split distorts EPS comparability) → redistributed to EV/EBIT (40%)

**Calculations:**
```
FCF_Score     = clamp(100 × (1 − 2.74/10), 0, 100)          = 100 × 0.726        = 72.6
EV/EBIT_Score = clamp((26.32 − 12)/23 × 100, 0, 100)         = (14.32/23) × 100   = 62.2609
FwdPE: Deviation% = (24.6 − 93.64)/93.64 × 100 = −73.738%
       FwdPE_Score = clamp(50 + (−73.738 × 2.5), 0, 100)     = clamp(−134.35,…)   = 0.0
PEG_Score = n/a (redistributed)

Raw = (72.6 × 0.40) + (62.2609 × 0.40) + (0.0 × 0.20) + 0
    = 29.04 + 24.90436 + 0.0
    = 53.94436
+ 5 = 58.94436
```

**Final Score = 58.9 → Fair Value (50.0–69.9) → Hold, watch only** (band unchanged from placeholder)

🚩 **Low-confidence FwdPE floor (carried forward):** the 93.64× 10-yr avg PE benchmark is single-sourced and likely distorted (hyper-growth-era multiples + 10-for-1 split breaking cross-period comparison). The 2026-06-07 session manually softened this to a sub-score of 2/10 rather than the mechanical floor of 1/10. The new continuous fallback formula produces **0.0 either way** (the deviation is so large it floors regardless), so no separate judgment call changes the outcome here — but the underlying 93.64× figure itself remains flagged for re-sourcing.

---

## NKE — current weight 1.59%

**Inputs** (from [2026-06-07 full-portfolio session](2026-06-07-rescore-full-portfolio.md), NKE section):
- FCF yield = 5.16%
- EV/EBIT = 17.60×
- Forward PE = 24×, 10-yr avg PE ≈ 35.5×
- Revenue CAGR ≈ −0.29% (flat-to-declining) → not a Fast Grower → redistributed to EV/EBIT (40%)

**Calculations:**
```
FCF_Score     = clamp(100 × (1 − 5.16/10), 0, 100)          = 100 × 0.484        = 48.4
EV/EBIT_Score = clamp((17.60 − 12)/23 × 100, 0, 100)         = (5.6/23) × 100     = 24.3478
FwdPE: Deviation% = (24 − 35.5)/35.5 × 100 = −32.394%
       FwdPE_Score = clamp(50 + (−32.394 × 2.5), 0, 100)     = clamp(−30.99,…)    = 0.0
PEG_Score = n/a (redistributed)

Raw = (48.4 × 0.40) + (24.3478 × 0.40) + (0.0 × 0.20) + 0
    = 19.36 + 9.73912 + 0.0
    = 29.09912
+ 5 = 34.09912
```

**Final Score = 34.1 → Cheap (30.0–49.9) → Standard position 3–5%** *(score; action overridden — see flag)* (band unchanged from placeholder)

🚩 **Value-trap override (carried forward, do NOT mechanically act on this score):** ROIC has cratered from ~20% (FY21–25 avg) to 7.84–9.00% TTM — **fails Phase 01's >15% ROIC quality gate**. Revenue down ~9.8% YoY with continued decline guided. GuruFocus flags "Possible Value Trap." HOLD existing 1.59% position; do not add. Candidate for the Upgrade 4 Turnaround Sub-Gate (insider buying by CEO Elliott Hill is one supporting data point) — needs a dedicated qualitative review and an `override-log.md` entry.

---

## NOW — current weight 2.47%

**Inputs** (from [2026-06-07 full-portfolio session](2026-06-07-rescore-full-portfolio.md), NOW section — ⚠️ partial citation-recovery gap):
- FCF yield = 3.89%
- EV/EBIT = 62.4×
- Forward PE = 24.57×; 10-yr avg PE not numerically sourced — original research flagged "VERY LARGE DISAGREEMENT … driven by hyper-growth-era multiples," concluding current valuation sits "far below those inflated norms"
- Fast Grower confirmed (revenue CAGR ~22.2%, forward EPS growth 23–26%) → PEG = 1.15 → PEG_Score applies, EV/EBIT stays 25%

**Calculations:**
```
FCF_Score     = clamp(100 × (1 − 3.89/10), 0, 100)          = 100 × 0.611        = 61.1
EV/EBIT_Score = clamp((62.4 − 12)/23 × 100, 0, 100)          = (50.4/23) × 100    = 219.1304 → clamp → 100.0
FwdPE_Score   = 0.0 (flagged floor placement — see note below)
PEG_Score     = clamp((1.15 − 0.5)/2.0 × 100, 0, 100)        = (0.65/2.0) × 100   = 32.5

Raw = (61.1 × 0.40) + (100.0 × 0.25) + (0.0 × 0.20) + (32.5 × 0.15)
    = 24.44 + 25.0 + 0.0 + 4.875
    = 54.315
+ 5 = 59.315
```

**Final Score = 59.3 → Fair Value (50.0–69.9) → Hold, watch only** (band unchanged from placeholder)

🚩 **EV/EBIT clamp:** raw EV/EBIT_Score = 219.13 (EV/EBIT 62.4× is far past the 35× ceiling) → clamped to 100.0. 🚩 **FwdPE floor placement (no numeric benchmark):** no numeric 10-yr avg PE was sourced, only the qualitative finding that current FwdPE sits "far below" history — directionally that means cheap (low sub-score), so 0.0 is assigned as a flagged floor placeholder pending a sourced numeric 10-yr avg PE (same treatment as NFLX above, but here the benchmark figure itself is missing entirely rather than just low-confidence).

---

## NVDA — current weight 5.30%

**Inputs** (from [2026-06-07 NVDA session](2026-06-07-rescore-nvda.md)):
- FCF yield = 1.95% ($96.6B ÷ $4,963.4B)
- EV/EBIT = 37.7× (EV $4,909.3B ÷ EBIT $130.4B)
- Forward PE ≈ 22.5×, 10-yr avg PE ≈ 60× (midpoint of 53.3×–66.6× range)
- Fast Grower confirmed (EPS growth ~145% then ~65%) → PEG ≈ 0.30 (trailing) / 0.43 (forward) → PEG_Score applies, EV/EBIT stays 25%

**Calculations:**
```
FCF_Score     = clamp(100 × (1 − 1.95/10), 0, 100)          = 100 × 0.805        = 80.5
EV/EBIT_Score = clamp((37.7 − 12)/23 × 100, 0, 100)          = (25.7/23) × 100    = 111.7391 → clamp → 100.0
FwdPE: Deviation% = (22.5 − 60)/60 × 100 = −62.5%
       FwdPE_Score = clamp(50 + (−62.5 × 2.5), 0, 100)       = clamp(−106.25,…)   = 0.0
PEG_Score (trailing 0.30) = clamp((0.30 − 0.5)/2.0 × 100, 0, 100) = clamp(−10.0,…) = 0.0
PEG_Score (forward 0.43)  = clamp((0.43 − 0.5)/2.0 × 100, 0, 100) = clamp(−3.5,…)  = 0.0  (same result either way)

Raw = (80.5 × 0.40) + (100.0 × 0.25) + (0.0 × 0.20) + (0.0 × 0.15)
    = 32.2 + 25.0 + 0.0 + 0.0
    = 57.2
+ 5 = 62.2
```

**Final Score = 62.2 → Fair Value (50.0–69.9) → Hold, watch only** (band unchanged from placeholder)

🚩 **EV/EBIT clamp:** raw EV/EBIT_Score = 111.74 (EV/EBIT 37.7× exceeds the 35× ceiling) → clamped to 100.0.

---

## NVO — current weight 0.40%

**Inputs** (from [2026-06-07 full-portfolio session](2026-06-07-rescore-full-portfolio.md), NVO section — ⚠️ citation-recovery gap, entire data table recovered from prior research notes):
- FCF yield = 2.29%
- EV/EBIT ≈ 9.69–10.51× (two close recovered figures, both <12)
- Forward PE = 12.86×, 10-yr avg PE ≈ 23×
- Growth thesis actively breaking (CagriSema failure) → not treated as a Fast Grower → redistributed to EV/EBIT (40%)

**Calculations:**
```
FCF_Score     = clamp(100 × (1 − 2.29/10), 0, 100)          = 100 × 0.771        = 77.1
EV/EBIT_Score (9.69×)  = clamp((9.69 − 12)/23 × 100, 0, 100)  = clamp(−10.04,…)   = 0.0
EV/EBIT_Score (10.51×) = clamp((10.51 − 12)/23 × 100, 0, 100) = clamp(−6.48,…)    = 0.0  (same result either way)
FwdPE: Deviation% = (12.86 − 23)/23 × 100 = −44.087%
       FwdPE_Score = clamp(50 + (−44.087 × 2.5), 0, 100)     = clamp(−60.22,…)    = 0.0
PEG_Score = n/a (redistributed)

Raw = (77.1 × 0.40) + (0.0 × 0.40) + (0.0 × 0.20) + 0
    = 30.84 + 0.0 + 0.0
    = 30.84
+ 5 = 35.84
```

**Final Score = 35.8 → Cheap (30.0–49.9) → Standard position 3–5%** *(score; action overridden — see flag)* (band unchanged from placeholder)

🚩 **Value-trap / broken-thesis override (carried forward, do NOT mechanically act on this score):** CagriSema trial failure, first-ever guided revenue *decline* for 2026, continuing GLP-1 share loss to Eli Lilly (a fundamental "key market lost" sell trigger). NVO is also the only name that passes the Rate Environment Gate (+3.23% spread) — a passing gate plus a cratering growth story is a screen-breaking combination, not a green light. Candidate for a dedicated EXIT REVIEW / Phase 06 assessment, not a buy.

---

## SPGI — current weight 0.79%

**Inputs** (from [2026-06-07 full-portfolio session](2026-06-07-rescore-full-portfolio.md), SPGI section):
- FCF yield = 4.34%
- EV/EBIT ≈ 21×
- Forward PE = 20.93×, 10-yr avg PE ≈ 35×
- Mature financial-data/ratings business → not a Fast Grower → redistributed to EV/EBIT (40%)

**Calculations:**
```
FCF_Score     = clamp(100 × (1 − 4.34/10), 0, 100)          = 100 × 0.566        = 56.6
EV/EBIT_Score = clamp((21 − 12)/23 × 100, 0, 100)            = (9/23) × 100       = 39.1304
FwdPE: Deviation% = (20.93 − 35)/35 × 100 = −40.2%
       FwdPE_Score = clamp(50 + (−40.2 × 2.5), 0, 100)       = clamp(−50.5,…)     = 0.0
PEG_Score = n/a (redistributed)

Raw = (56.6 × 0.40) + (39.1304 × 0.40) + (0.0 × 0.20) + 0
    = 22.64 + 15.65216 + 0.0
    = 38.29216
+ 5 = 43.29216
```

**Final Score = 43.3 → Cheap (30.0–49.9) → Standard position 3–5%** (band unchanged from placeholder)

🚩 **Rate Environment Gate flag (carried forward):** the cleanest fundamentals-based BUY candidate in the book, meaningfully underweight at 0.79% — but the gate FAILs here too (+0.23%, short of +1.5%), so per Step 2 of the FV methodology this is "approaching buy price → set limit order," not "enter now."

---

## SPOT — current weight 0.92%

**Inputs** (from [2026-06-07 full-portfolio session](2026-06-07-rescore-full-portfolio.md), SPOT section):
- FCF yield = 3.24%
- EV/EBIT ≈ 40.35× (EV ≈ market cap, no clean net-debt/cash sourced — flagged approximation)
- Forward PE = 33.39×; only recently sustainably profitable → no usable 10yr PE reference → no-history fallback
- Ambiguous Fast-Grower status (revenue CAGR 13.6%, just under 15% threshold) → redistributed to EV/EBIT (40%)

**Calculations:**
```
FCF_Score     = clamp(100 × (1 − 3.24/10), 0, 100)          = 100 × 0.676        = 67.6
EV/EBIT_Score = clamp((40.35 − 12)/23 × 100, 0, 100)         = (28.35/23) × 100   = 123.2609 → clamp → 100.0
FwdPE_Score   = 50.0 (no-history fallback, neutral, flagged)
PEG_Score = n/a (redistributed)

Raw = (67.6 × 0.40) + (100.0 × 0.40) + (50.0 × 0.20) + 0
    = 27.04 + 40.0 + 10.0
    = 77.04
+ 5 = 82.04
```

**Final Score = 82.0 → Very Expensive (80.0–89.9) → Trim to 50%**

🚩 **Band change: was Expensive (77.7, Trim 25–30%) → now Very Expensive (82.0, Trim to 50%).** 🚩 **EV/EBIT clamp:** raw EV/EBIT_Score = 123.26 (EV/EBIT 40.35× exceeds the 35× ceiling) → clamped to 100.0 — but note EV≈MCap is itself an approximation (no net-debt/cash figure sourced); if SPOT carries meaningful net cash, true EV/EBIT would be modestly lower (though almost certainly still ≥35×, i.e. still clamped to 100.0). Recommend a fresh Rule 0 pull (price, net cash) before executing this trim.

---

## UBER — current weight 0.39%

**Inputs** (from [2026-06-07 full-portfolio session](2026-06-07-rescore-full-portfolio.md), UBER section):
- FCF yield = 6.77%
- EV/EBIT = 26.36×
- Forward PE ≈ 20×; IPO'd 2019, no decade-long PE history → no-history fallback
- Ambiguous Fast-Grower read (recent EPS growth distorted by one-off tax effects) → redistributed to EV/EBIT (40%)

**Calculations:**
```
FCF_Score     = clamp(100 × (1 − 6.77/10), 0, 100)          = 100 × 0.323        = 32.3
EV/EBIT_Score = clamp((26.36 − 12)/23 × 100, 0, 100)         = (14.36/23) × 100   = 62.4348
FwdPE_Score   = 50.0 (no-history fallback, neutral, flagged)
PEG_Score = n/a (redistributed)

Raw = (32.3 × 0.40) + (62.4348 × 0.40) + (50.0 × 0.20) + 0
    = 12.92 + 24.97392 + 10.0
    = 47.89392
+ 5 = 52.89392
```

**Final Score = 52.9 → Fair Value (50.0–69.9) → Hold, watch only**

🚩 **Band change vs. the 2026-06-07 session's own discrete score (not vs. the 1st-pass placeholder):** that session's discrete Score 6 (rounded up from exactly 5.50 via the boundary rule) placed UBER in TRIM 25-30%. The continuous formula's 52.9 lands in Fair Value instead — the boundary-rounding artifact that pushed the discrete score from 5 to 6 doesn't recur in the continuous formula (52.89 rounds normally to 52.9, nowhere near a band edge). The 1st-pass placeholder (55.5, also Fair Value) already reflected the discrete Score 6 → 0.0–100.0 conversion, so **vs. the placeholder this is not a band change** — flagged here only for completeness since the underlying discrete-vs-continuous read differs.

---

## V (Visa) — current weight 0.60%

**Inputs** (from [2026-06-07 full-portfolio session](2026-06-07-rescore-full-portfolio.md), V section):
- FCF yield = 3.544%
- EV/EBIT = 25.82× (using the more conservative of two disagreeing net-debt figures)
- Forward PE ≈ 24.1×, 10-yr avg PE ≈ 33.7×
- Mature payments-network stalwart, not a Fast Grower → redistributed to EV/EBIT (40%)

**Calculations:**
```
FCF_Score     = clamp(100 × (1 − 3.544/10), 0, 100)         = 100 × 0.6456       = 64.56
EV/EBIT_Score = clamp((25.82 − 12)/23 × 100, 0, 100)         = (13.82/23) × 100   = 60.08696
FwdPE: Deviation% = (24.1 − 33.7)/33.7 × 100 = −28.4866%
       FwdPE_Score = clamp(50 + (−28.4866 × 2.5), 0, 100)    = clamp(−21.22,…)    = 0.0
PEG_Score = n/a (redistributed)

Raw = (64.56 × 0.40) + (60.08696 × 0.40) + (0.0 × 0.20) + 0
    = 25.824 + 24.034784 + 0.0
    = 49.858784
+ 5 = 54.858784
```

**Final Score = 54.9 → Fair Value (50.0–69.9) → Hold, watch only** (band unchanged from placeholder)

🚩 **Debt Gate passes cleanly (carried forward, positive):** ~40.7× interest coverage, Aa3/AA- ratings — no balance-sheet concern, this is purely a multiples-driven read.

---

## ZS — current weight 0.24% (low-confidence)

**Inputs** (from [2026-06-07 full-portfolio session](2026-06-07-rescore-full-portfolio.md), ZS section):
- FCF yield = 3.467%
- EV/EBIT: GAAP operating loss, undefined, and no clean net-debt/cash figure sourced either → neutral placeholder
- Forward PE = 30.28×; loss-making history → no usable 10yr PE reference → no-history fallback
- PEG = 34.55, explicitly flagged as not meaningful (near-zero/negative earnings base) → treated as a data-quality override, redistributed to EV/EBIT (40%)

**Calculations:**
```
FCF_Score     = clamp(100 × (1 − 3.467/10), 0, 100)         = 100 × 0.6533       = 65.33
EV/EBIT_Score = 50.0 (neutral placeholder — GAAP operating loss, no net-debt/cash figure)
FwdPE_Score   = 50.0 (no-history fallback, neutral, flagged)
PEG_Score = n/a (redistributed)

Raw = (65.33 × 0.40) + (50.0 × 0.40) + (50.0 × 0.20) + 0
    = 26.132 + 20.0 + 10.0
    = 56.132
+ 5 = 61.132
```

**Final Score = 61.1 (low-confidence) → Fair Value (50.0–69.9) → Hold, watch only** (band unchanged from placeholder)

🚩 **Low-confidence flag (carried forward):** two of four inputs (EV/EBIT, FwdPE) are neutral placeholders for genuinely un-computable metrics. ZS also **fails the Phase 01 Quality Gate** (negative net margin ≈ −1.6%, negative ROIC ≈ −2.3% to −3.1%), though less severely than RBRK — three consecutive years of strong, growing positive FCF ($333.6M → $585.0M → $726.7M) with narrowing GAAP losses. Flagged for `override-log.md` review alongside RBRK.

---

## Summary — Old Placeholder vs. New Real Score

| Ticker | Placeholder (1st pass, 0.0–100.0) | Real score (this session) | Band | Action | Band changed vs. placeholder? |
|---|---|---|---|---|---|
| AMZN | 77.7 | **79.8** | Expensive | Trim 25–30% | No |
| CSGP | 77.7 | **83.3** | Very Expensive | Trim to 50% | **Yes** |
| DUOL | 33.3 | **49.1** | Cheap | Standard 3–5% (no add — near cap) | No |
| GOOG | 77.7 | **83.7** | Very Expensive | Trim to 50% | **Yes** |
| META | 44.4 | **43.7** | Cheap | Standard 3–5% (gate-fail — no add) | No |
| MSFT | 55.5 | **52.9** | Fair Value | Hold (+ structural cap-breach plan) | No |
| NFLX | 66.6 | **58.9** | Fair Value | Hold, watch only | No |
| NKE | 33.3 | **34.1** | Cheap | *(score; value-trap override — HOLD)* | No |
| NOW | 55.5 | **59.3** | Fair Value | Hold, watch only | No |
| NVDA | 55.5 | **62.2** | Fair Value | Hold, watch only | No |
| NVO | 33.3 | **35.8** | Cheap | *(score; value-trap override — HOLD)* | No |
| SPGI | 44.4 | **43.3** | Cheap | Standard 3–5% (gate-fail — limit order) | No |
| SPOT | 77.7 | **82.0** | Very Expensive | Trim to 50% | **Yes** |
| UBER | 55.5 | **52.9** | Fair Value | Hold, watch only | No |
| V | 55.5 | **54.9** | Fair Value | Hold, watch only | No |
| ZS | 55.5 (low-confidence) | **61.1** (low-confidence) | Fair Value | Hold, watch only | No |

RBRK, STIM, TLT, XEON, and both CASH rows remain unscored (out of scope, per `holdings.md`).

---

## Flags Requiring Follow-Up

1. **Band changes — CSGP, GOOG, SPOT** (Expensive → Very Expensive, Trim 25–30% → Trim to 50%): all three carry stacked low-confidence flags (citation-recovery gaps for GOOG, distorted near-zero earnings base for CSGP, EV≈MCap approximation for SPOT). **Recommend a fresh Rule 0 `/rescore` for these three before executing any trim** off the back of this recalculation.
2. **EV/EBIT clamps to 100.0 — NOW (219.13→100.0), NVDA (111.74→100.0), SPOT (123.26→100.0):** the formula correctly saturates at the defined ceiling (35×); the underlying multiples remain informative (NOW 62.4×, NVDA 37.7×, SPOT 40.35×) even though the score itself can't distinguish "very expensive" from "extremely expensive" beyond 35×.
3. **Neutral/no-history FwdPE placeholders (50.0) — CSGP, DUOL, SPOT, UBER, ZS:** none of these have a usable 10-yr PE reference; the neutral midpoint avoids asserting a direction the data can't support, but each is a candidate for sourcing a real benchmark (sector-median forward PE, where available) at the next full rescore.
4. **Low-confidence FwdPE floor placements (0.0) — NFLX, NOW:** NFLX's 93.64× 10-yr-avg benchmark is single-sourced/likely distorted; NOW has no numeric 10-yr-avg benchmark at all, only a qualitative "far below historical norms" finding. Both floor to 0.0 under the new formula — directionally consistent with the source session's own (manual) judgment calls, but the underlying benchmarks should be re-sourced.
5. **Owner Earnings (Upgrade 1) — MSFT used the Owner-Earnings FCF figure (~$95B) as primary; AMZN, GOOG, META did NOT** (no maintenance-vs-growth-capex split was ever sourced for these three, despite all four being named under Upgrade 1). AMZN and META's FCF_Scores in particular (97.08 and ~70.25) are likely overstated/understated respectively if a true Owner-Earnings figure were used — flagged, not patched.
6. **Value-trap / broken-thesis overrides — NKE, NVO:** both compute to Cheap-band scores (34.1, 35.8) that would normally trigger a standard BUY, but both are under documented qualitative overrides (NKE: ROIC collapse, fails Phase 01 gate; NVO: CagriSema failure, broken growth thesis). Do not act on the numeric score alone for either.

**Next step:** a full `/rescore` with fresh Rule 0 live prices, prioritising CSGP, GOOG, and SPOT (band changes) and MSFT/AMZN (structural cap breaches independent of valuation).

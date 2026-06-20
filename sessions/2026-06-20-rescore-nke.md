# RESCORE — NKE (NIKE, Inc.)

## 1. Session header
- **Task type:** RESCORE (single ticker)
- **Date:** 2026-06-20
- **10Y US Treasury yield:** 4.46% (latest available — Fed H.15 / TradingEconomics, 18 Jun 2026; US bond market closed Fri 20 Jun for holiday)
- **Rate Regime Modifier in effect:** +5 (10Y in the 3.5–5% band)
- **Prior score:** 34.1 (2026-06-11 rescale of the 2026-06-07 pass) — Cheap band, but under a documented value-trap override (HOLD, do not add)
- **First-use jargon decode:** FCF = free cash flow (cash left after running and maintaining the business). EV/EBIT = enterprise value ÷ earnings before interest and taxes (whole-company price vs operating profit). Fwd PE = forward price-to-earnings (price ÷ next-year expected earnings per share). PEG = PE ÷ growth rate. ROIC = return on invested capital (profit earned per dollar of capital put to work). MoS = margin of safety (discount to fair value demanded before buying). PW FV = probability-weighted fair value (bull/base/bear blend). R/R = reward-to-risk ratio. TTM = trailing twelve months. pp = percentage points. bps = basis points (1bp = 0.01%). E = expected annual return.

## 2. Live data (Rule 0 — fetched first)
| Item | Value | Source |
|---|---|---|
| Live price | **$45.20** | yfinance `currentPrice`/`regularMarketPrice` (IBKR `get_price_snapshot` was permission-denied this session; yfinance fallback per Rule 0 chain) |
| 52-week range | **$41.35 – $80.17** | yfinance |
| Market cap | $66.94B | yfinance `marketCap` (implies 1.481B shares — see share-count note) |
| Enterprise value | $70.06B | yfinance `enterpriseValue` |
| Analyst consensus PT | **mean $59.58, median $55.00, range $23–$120 (33 analysts), rec "buy"** | yfinance |
| 10Y Treasury | 4.46% | Fed H.15 / TradingEconomics (18 Jun 2026) |

**⚠️ Share-count data-quality note:** yfinance `sharesOutstanding` returned 1.199B, which is inconsistent with `marketCap`/$price (1.481B) and with the balance sheet (`Ordinary Shares Number` 1,476M) and the prior session (1.476B). The 1.199B field is stale/wrong; **all calcs use the 1.481B-share consistent set (marketCap $66.94B, EV $70.06B)**, which matches the filed share count.

## 3. Data gaps flagged
- No live IBKR snapshot (tool denied) — price sourced from yfinance fallback, which Rule 0 permits.
- `sharesOutstanding` field unreliable (handled above by using the marketCap/balance-sheet-consistent count).
- No invented data: where trailing earnings are depressed, the normalization basis is stated explicitly below rather than guessed.

## 4. Rate Environment Gate
- **Step 1 — Earnings Yield Spread:** EY = 1 ÷ Fwd PE = 1 ÷ 24.89 = **4.02%**. Spread = 4.02% − 4.46% = **−0.44%**, which is **< +1.5% → FAIL → +5** (yellow flag, additive; not a veto since 2026-06-07).
- **Step 2 — Rate Regime Modifier:** 10Y 4.46% sits in the 3.5–5% band → **+5**.
- Combined Rate-Gate additions: **+10**.

## 5. Re-Score inputs (Standard Re-Score template)

NKE reported **FY2026 Q3 (qtr ended 28 Feb 2026)** on 31 Mar 2026. The turnaround is mid-stream and trailing earnings are **deeply depressed**, so the Rule 6 ("normalize before you value") basis is stated for every input.

| Metric | TTM (trough) | FY2025 (scored base) | FY23–25 avg (peak-incl.) |
|---|---|---|---|
| FCF | $1.048B | $3.268B | $4.919B |
| FCF yield | 1.57% | **4.88%** | 7.35% |
| EBIT | $2.807B | $3.702B | $5.309B |
| EV/EBIT | 24.96× | **18.92×** | 13.20× |
| ROIC (NOPAT/IC) | ~11.0% | 14.5% | — |

- **Rule 6 normalization decision:** I scored on the **FY2025 full-year base**, not the depressed TTM and not the FY23–25 average. Rationale (honest, no snap-back assumed): TTM ($1.0B FCF / 1.6% yield) is the turnaround trough and would over-penalize; the FY23–25 average leans on the FY2024 peak ($6.6B FCF, $6.3B EBIT) that **pre-dates** the turnaround and management has explicitly guided *declines through FY2026 with margin inflection only in Q2 FY2027* — so the peak is not a fair forward normal. FY2025 is the most recent *complete* year, already well into the decline, and is the conservative midpoint. TTM and FY23–25 are carried as the bear/bull anchors in the modifier (§7).
- **5yr PE range** (reconstructed via yfinance TTM-EPS × price, 20 quarters, per valuation-scoring.md auto-method): **low 18.2×, high 40.3×, avg 29.5×**. Forward PE 24.89×.
- **Fast Grower? No** — revenue flat/declining (Q3 FY26 −3% currency-neutral; FY25 rev −9.8% YoY). PEG **not applicable → its 15% weight redistributed to EV/EBIT (→40%)**, per Upgrade 3 clarification.

### Fundamental changes since last review
- Q3 FY2026: revenue $12.4B (flat reported / **−3% currency-neutral**); diluted EPS **$0.35** (beat the $0.31 estimate). Gross margin **40.2%, −130bps** (300bps of tariff drag).
- **Greater China −10%**, with management **guiding ~−20% for the current quarter**; China inventory down mid-teens, units down >20%.
- Nike Direct −7% (Digital −9%, stores −5%); Wholesale +1% (NA wholesale +11%).
- **Q4 FY2026 guided down 2–4%**; management projects **margin inflection in Q2 FY2027** (the named catalyst).
- **Buybacks effectively paused:** Q3 FY2026 repurchases **$0** (TTM ~$0.15B vs ~$3.0B in FY2025) — cash conservation during the turnaround. Dividend maintained (~3.6% yield).
- ROIC TTM ~11% — recovering off the 7.84–9.00% trough flagged on 2026-06-07, but **still below Phase 01's >15% gate**.

## 6. Full score calculation (every sub-score shown)

```
FCF Yield (40%)   base FY2025 yield 4.88%
   FCF_Score = clamp(100×(1 − 4.88/10),0,100) = 51.18
   contribution = 51.18 × 0.40 = 20.472

EV/EBIT (40% — PEG redistributed)  base FY2025 EV/EBIT 18.92×
   EV/EBIT_Score = clamp((18.92 − 12)/23 × 100,0,100) = 30.10
   contribution = 30.10 × 0.40 = 12.040

Forward PE (20%)  5yr range available → PRIMARY range method
   FwdPE_Score = clamp((24.89 − 18.2)/(40.3 − 18.2) × 100,0,100) = 30.27
   Historical PE Modifier (Upgrade 2): dev vs 5yr avg = (24.89−29.5)/29.5 = −15.6%
     → not >20% below, not >20% above → modifier 0
   contribution = 30.27 × 0.20 = 6.054

PEG (15%)  n/a (not a Fast Grower) → redistributed to EV/EBIT above

Raw weighted = 20.472 + 12.040 + 6.054 = 38.566
+ Rate Gate Step 1 (EY spread fail)  +5
+ Rate Gate Step 2 (Rate Regime)     +5
= 48.566  (before Upside/Downside Modifier)
```

## 7. Upside/Downside Modifier (REQUIRED) — full calc

**Scenario fair values** (Rule 7; bear underwritten honestly — turnaround may stall):
| Scenario | FV | Assumption |
|---|---|---|
| Bull (25%) | $72 | Turnaround works, margin inflection lands Q2 FY27 + multiple re-rate; sits below the $120 street outlier, near the high cluster |
| Base (50%) | $52 | Modest recovery; slightly below street median $55 for execution/China risk |
| Bear (25%) | $33 | China keeps bleeding (−20%+), margins stay compressed, inflection slips; above the $23 street low |

```
PW Fair Value = 0.25×72 + 0.50×52 + 0.25×33 = $52.25
   (cross-check: street mean $59.58 / median $55 — my PW FV is more conservative than both)
Gap Upside %  = (52.25 ÷ 45.20) − 1 = +15.60%
Catalyst window = 2.0 yr  (mgmt names margin inflection Q2 FY2027 ≈ late CY2026, but guides
   declines through FY2026 — timing genuinely uncertain, so the conservative 2yr per Rule 10)
Annualized gap = 15.60% ÷ 2.0 = +7.80%

Intrinsic growth = +4.0%/yr  (conservative normalized — near-term declining, recovering later;
   NOT a snap-back assumption)
Shareholder yield = dividend 3.63% + net buyback 0.0% = 3.63%
   (net buyback set to ZERO — repurchases are PAUSED in FY2026, not the ~2%/yr of prior years)

E = 7.80 + 4.0 + 3.63 = +15.43%   (expected annual return)
```

**Map E → M** (hurdle H = 10%, E ≥ H branch):
```
M = −15 × clamp((15.43 − 10)/15, 0, 1) = −15 × 0.3620 = −5.43
```
**Catalyst guardrail:** a catalyst (margin inflection) is identifiable within 18–24 months → the −5 upside cap does **not** bind; M = −5.43 stands. Modifier is within the [−15, +15] bound.

## 8. Final score + action

```
FINAL = 48.566 (raw + rate gate) + (−5.43) (Upside/Downside) = 43.137 → 43.1
```

| | Value |
|---|---|
| Raw weighted | 38.566 |
| Rate Gate Step 1 (EY spread) | +5 |
| Rate Regime Modifier (Step 2) | +5 |
| Upside/Downside Modifier | **−5.43** (E = +15.43%) |
| **FINAL SCORE** | **43.1** |
| Prior score | 34.1 |
| Band | **Cheap (30.0–49.9) → Standard position 3–5%** |

**Action: HOLD existing position — do NOT add. Action category UNCHANGED vs prior (HOLD/do-not-add).**

Why the *score* rose (34.1 → 43.1) even though the business deteriorated:
1. **FwdPE sub-score** moved from 0.0 → 30.27. The prior pass anchored deviation against a *10yr* average of ~35.5× (which made NKE look artificially cheap on the PE axis). The framework now uses a **5yr** lookback (changed 2026-06-20); NKE's real 5yr PE range is 18.2–40.3× (avg 29.5×), and forward PE 24.89× sits mid-range, not at the floor. This is a methodology refresh, not an improvement in NKE.
2. The full Rate Gate (+10) is now applied (Step 1 **+5** *and* Step 2 +5); the prior pass applied only the legacy +0.5 single modifier.
3. The Upside/Downside Modifier (−5.43) partially offsets, reflecting only modest (+15.4%) expected return — not enough to pull it into the Very Cheap band.

**Qualitative override still in force (carried forward):** ROIC ~11% TTM remains **below Phase 01's >15% quality gate**; revenue still declining; buybacks paused. The numeric Cheap-band score does **not** by itself license adding — the value-trap/turnaround flags persist. NKE remains a candidate for a formal Upgrade 4 Turnaround Sub-Gate review (CEO Elliott Hill insider buying is 1 of the 5 conditions) and an `override-log.md` entry.

## 9. Order setup (score is in BUY band → run it; result is a hard PASS on adding)

Treated as **Turnaround** for MoS/stop (Rule 8 + Upgrade 4), given ROIC < gate and guided declines.

| Field | Value |
|---|---|
| Valuation score (incl. modifier) | 43.1 (≤49.9 → entry-eligible on score alone) |
| Expected annual return E / catalyst | +15.43% / ~2 yr (margin inflection Q2 FY2027) |
| Upside/Downside Modifier applied | −5.43 |
| Blended Fair Value (PW) | $52.25 |
| Margin of Safety (turnaround) | 35% |
| **Buy price (limit)** | **$33.96** |
| Primary sell target | $52.25 |
| Bull-case trim target | $64.80 (= $72 × 0.90) |
| Stop loss (buy × 0.70) | $23.77 |
| **R/R at buy price** | (52.25 − 33.96)/(33.96 − 23.77) = **1.79:1 — BELOW the 2:1 minimum** |
| R/R at live $45.20 | (52.25 − 45.20)/(45.20 − 23.77) = **0.33:1** |

**Order-setup verdict: DO NOT ADD.** Live price $45.20 is far above the disciplined turnaround buy price of $33.96, and even *at* that buy price the reward-to-risk is 1.79:1 — under the 2:1 floor. The trade fails the order-setup gate independently of the qualitative override. No order placed. (Per Phase 05, the existing position is a HOLD — fair-value/Cheap-band names are not trimmed, and there is no Phase 06 exit trigger: this is a single-segment weakness and macro/turnaround story, not structurally broken margins or a covenant crisis.)

## 10. Next review trigger
- **Next earnings (FY2026 Q4, ~late June 2026 — imminent; then FY2027 Q1 ~Sept 2026):** watch (a) **gross-margin trajectory vs the guided Q2 FY2027 inflection**, (b) **Greater China revenue** (guided ~−20%), (c) **ROIC** — if it keeps climbing back toward 15% the turnaround thesis firms; if it stalls in single digits the "possible value trap" hardens into Phase 06 thesis-broken territory, (d) any **resumption of buybacks** (would lift shareholder yield and E).
- **Rule 9 triggers:** guidance revision, the named margin-inflection catalyst landing or slipping, or a >15% unexplained price move.

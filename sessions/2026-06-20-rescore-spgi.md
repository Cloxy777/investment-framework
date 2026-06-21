# RESCORE — SPGI (S&P Global Inc.) — 2026-06-20

**Task type:** RESCORE (single ticker)
**Date of record:** 20 Jun 2026
**10Y US Treasury yield:** 4.45% (source: yfinance `^TNX` last, 2026-06-20) → Rate Regime Modifier bracket 3.5–5% → **+5**
**Trigger:** Quarterly re-score + first application of the new **Upside/Downside Modifier** (added to the valuation score 2026-06-20). Prior score 43.3 (Cheap → BUY band, computed 2026-06-11 off 2026-06-07 data).

> **Jargon, plain English on first use:** FCF = free cash flow (cash left after running and maintaining the business). EV/EBIT = enterprise value ÷ earnings before interest and tax (whole-company price vs. operating profit). Fwd PE = forward price-to-earnings (price ÷ next-year expected earnings per share). PEG = PE ÷ growth rate. ROIC = return on invested capital. MoS = margin of safety (discount to fair value demanded before buying). PW = probability-weighted (the bull/base/bear blend). CAGR = compound annual growth rate. R/R = risk/reward. pp = percentage points. E = expected annual return. NOPAT = net operating profit after tax.

---

## 1. Live data first (Rule 0 — never infer SPGI's price from a multiple)

> **Why this matters for SPGI specifically:** SPGI is the exact ticker behind the framework's costliest documented error — the "SPGI Price Inference Error" (May 2026), where a price of ~$450 was *inferred* from "29% below 5yr avg PE" when the real price was $411, throwing off MoS, stop, size and R/R downstream. Every price below is an explicitly fetched live quote, not derived from any multiple.

| Item | Value | Source |
|---|---|---|
| **Live price** | **$410.92** | yfinance `fast_info.last_price`, fetched 2026-06-20. (Interactive Brokers `get_price_snapshot` was attempted first per the preferred path — conid 229629397, NYSE primary — but the tool call was permission-denied this session, so the documented yfinance fallback was used. Still a live fetch, not inferred.) |
| Prior close | $418.02 / $419.50 | yfinance (info / fast_info) |
| **52-week range** | **$381.61 – $579.05** | yfinance |
| **Analyst consensus PT** | mean **$532.81**, high $575, low $480 (n=21) | yfinance `targetMeanPrice` |
| Market cap | $121.63B | yfinance |
| Enterprise value | $138.75B | yfinance |
| TTM EPS | $18.43 | yfinance (reconstructed) |
| Forward EPS (implied) | ~$22.23 | price ÷ forward PE 18.49× (used only as the FV earnings base, not as a price) |
| Dividend yield / rate | ~0.94% / $3.88 | yfinance |

Live price ($410.92) sits ~29% below the consensus mean PT and just ~7.7% above the 52-week low — i.e. near the bottom of its 1-year range, consistent with the "cheapest clean name in the book" read carried since 2026-06-07.

## 2. Standard Re-Score inputs (FY2025 latest reported, computed from yfinance)

| Metric | Value | Note |
|---|---|---|
| Sector | Financials — financial data, ratings & analytics | Mature wide-moat duopoly (with Moody's), not a Fast Grower |
| FCF yield | **4.49%** | FY2025 FCF $5,456M ÷ market cap $121,632M |
| EV/EBIT | **21.30×** | EV $138,754M ÷ FY2025 EBIT $6,514M |
| Forward PE | **18.49×** | yfinance |
| 5yr PE — avg / low / high | **30.11× / 21.81× / 34.05×** | yfinance reconstruction, n=20 quarters (full 5yr range available → primary FwdPE formula) |
| Revenue CAGR 3yr | **11.1%** | $11.181B (FY22) → $15.336B (FY25) |
| ROIC | ~11.4% | NOPAT $5,042M ÷ invested capital $44,215M. *Below the 15% Phase-01 gate on a reported basis — depressed by the large IHS Markit acquisition goodwill/intangibles in the invested-capital base; core operating returns on the ratings/indices franchise remain very high. Flagged, not a fresh exit trigger (already a held position).* |
| Gross margin | 70.5% | yfinance |
| Net margin | 30.4% (FY25 NI $4,471M / rev $15,336M = 29.2%) | yfinance / computed |
| Net debt / EBITDA | **1.53×** | (Total debt $13,582M − cash $1,801M) ÷ EBITDA $7,693M. Well inside even the standard 2.5× gate. |
| Interest coverage | 22.7× | EBIT $6,514M ÷ interest $287M |
| FCF/NI conversion | 122% (FY25); 144%, 136%, 77% prior 3yr | Consistently >100% — high earnings quality, no red flag |
| Current weight | 0.79% | per holdings.md (meaningfully underweight) |
| Last score / review | 43.3 / Jun 2026 | 2026-06-11 recompute |

**Data gaps flagged:** none material. ROIC <15% on a reported basis is flagged above (acquisition-distorted, not a fundamental break). No metric was invented or estimated.

**Fundamental changes since last review:** FY2025 results in hand show continued double-digit revenue growth (+11% CAGR), margin strength (gross 70.5%, EBIT margin ~42%), and clean cash conversion. No guidance cut, management change, M&A, or balance-sheet event. The bear case (below) is cyclical, not structural.

## 3. Rate Environment Gate

- **Step 1 — Earnings Yield Spread Test:** EY = 1 ÷ 18.49 = **5.41%**. Spread = 5.41% − 4.45% = **+0.96%**, which is **< +1.5% → FAIL → additive +5** (yellow flag, not a veto, per the 2026-06-07 change). *Note: the prior 43.3 did NOT include this Step 1 additive (only Step 2's +5) — the watchlist flagged this as an open inconsistency for the next rescore. It is now applied per current strategy.md.*
- **Step 2 — Rate Regime Modifier:** 10Y 4.45% → 3.5–5% bracket → **+5**.

## 4. Full valuation score (every sub-score shown)

PEG: SPGI is a **mature stalwart, not a Lynch Fast Grower** (Upgrade 3 explicitly excludes stalwarts/cyclicals) → PEG's 15% weight **redistributed to EV/EBIT (→ 40%)**.

```
FCF_Score      = clamp(100 × (1 − 4.49/10), 0, 100)              = 55.14
EV/EBIT_Score  = clamp((21.30 − 12)/23 × 100, 0, 100)            = 40.44
FwdPE_Score (primary, 5yr range available):
   = clamp((18.49 − 21.81)/(34.05 − 21.81) × 100, 0, 100)        = 0.0  (forward PE below the 5yr low → floors)
   Historical PE Modifier: deviation vs 5yr avg = (18.49−30.11)/30.11 = −38.6% (>20% below) → −10
   FwdPE_final = clamp(0.0 − 10, 0, 100)                          = 0.0
PEG_Score      = n/a (redistributed)

Raw = (55.14 × 0.40) + (40.44 × 0.40) + (0.0 × 0.20)
    = 22.06 + 16.18 + 0.0
    = 38.23  (raw weighted score)
```

## 5. Upside/Downside Modifier (REQUIRED — full calc)

**Scenario fair value (Rule 7, forward EPS ~$22.23 base; multiples grounded in the 5yr PE band 21.8–34.1× and sanity-checked against the consensus PT range $480–$575):**

| Scenario | Wt | Exit PE | Fair value | Assumption |
|---|---|---|---|---|
| Bull | 25% | 26.0× | **$578** | Ratings issuance recovers + Vitality/private-markets/indices growth re-rates toward upper band (≈ street high $575) |
| Base | 50% | 24.0× | **$534** | Consensus: double-digit growth, stable margins (≈ consensus mean $532.81) |
| Bear | 25% | 17.5× | **$389** | **Ratings-segment cyclicality underwritten honestly** — debt-issuance volumes fall in a higher-for-longer / recession scenario, ratings revenue (the most cyclical segment, tied to bond/loan issuance) drops, and the multiple de-rates to a trough below the 5yr low |

```
PW Fair Value = 0.25×578 + 0.50×534 + 0.25×389              = $509
Gap Upside %  = (509 ÷ 410.92) − 1                          = +23.75%
Catalyst window (Rule 10) = 2 years                          (issuance normalization over next ~2 earnings cycles)
Annualized gap = 23.75% ÷ 2                                  = +11.87%/yr
Intrinsic growth = +10%/yr        (conservative vs 11.1% rev CAGR and management mid-teens EPS algo; FY25 +32.5% earnings growth treated as partly one-off, not used)
Shareholder yield = 0.94% dividend + ~2.0% net buyback       = +2.94%/yr
E = 11.87 + 10.0 + 2.94                                      = +24.81%/yr
```

**Catalyst guardrail check:** a documented catalyst + timeline exists (debt-issuance volume normalization within the 18–24mo window) → upside credit is NOT capped at −5; full mapping applies.

**Map E to M** (hurdle H = 10%; E ≥ H branch):
```
M = −15 × clamp((24.81 − 10)/15, 0, 1) = −15 × clamp(0.987, 0, 1) = −15 × 0.987 = −14.81
```

**Upside/Downside Modifier = −14.8** (near the floor — strong, catalyst-backed expected return).

## 6. Final Score & action band

```
Final = Raw 38.23  + Rate Regime (Step 2) +5  + Earnings-Yield-Spread (Step 1) +5  + Upside/Downside −14.81
      = 33.42  → round → 33.4
```

**FINAL SCORE = 33.4 → Cheap (30.0–49.9) → BUY, standard position (3–5%)**

**Prior score 43.3 → now 33.4 (−9.9).** The drop is driven by the new **Upside/Downside Modifier (−14.8)** rewarding the large catalyst-backed expected return, partly offset by newly-applying the Step 1 gate additive (+5) that the prior number omitted. **Action band did NOT change** — it was BUY (Cheap) at 43.3 and remains BUY (Cheap, deeper in the band) at 33.4. The position remains meaningfully underweight (0.79%).

### Order setup (BUY action → required)

| Item | Value |
|---|---|
| Blended (PW) Fair Value | **$509** |
| Margin of Safety (score 30.0–49.9 band → 25–30%) | 25% → buy $381.75 · 30% → buy $356.30 |
| **Buy limit price** | **$381.75 (25% MoS)** — note this is *below* live $410.92, so this is a **limit-order watch, not enter-now** |
| Primary sell target (= FV) | $509 |
| Bull-case trim target (bull × 0.90) | $520.20 |
| Stop loss (25–30% below buy) | $286.31 (−25%) to $267.23 (−30%) |
| **R/R at the $381.75 buy with −25% stop** | **1.33:1 — FAILS the 2:1 minimum** |
| R/R that clears 2:1 | only at 30% MoS (buy $356.30) + 20% stop ($285.04) → **2.14:1** |
| Position size if filled (buy $381.75, −30% stop $267.23, 1.5% risk) | 7 shares ≈ $2,683 ≈ **5.0% of $53,659 portfolio** (hits the 5% Cheap-band cap exactly; cap binds) |

**Order-setup conclusion:** SPGI scores firmly in the BUY band and is the cleanest underweight in the book, but at the live price of $410.92 the disciplined entry is a **limit order, not a chase**. The standard 25% MoS buy ($381.75) does not clear the 2:1 R/R gate; the trade only clears 2:1 at a deeper 30% MoS entry ($356.30) with a 20% stop. **Recommended: set a limit-order watch in the ~$356–$382 zone** (a level the stock traded at within its 52-week range — low $381.61); enter on a fill there, sized to the 5% cap. Do not enter at $410.92.

## 7. Bear case underwritten (per the brief)

SPGI's Ratings segment is its most cyclical: revenue is tied to the *volume* of new debt issuance (corporate bonds, structured finance, bank loans). In a higher-for-longer rate regime or a recession, issuance volumes contract sharply, and Ratings revenue (and margin) fall with them — this is the documented historical pattern (e.g. 2022's issuance slump). The bear scenario above ($389, 17.5× trough multiple) prices in exactly this: a meaningful issuance-driven revenue decline *and* a multiple de-rate below the 5yr low. The PW fair value of $509 already carries this 25%-weighted downside; the expected return is computed net of it. The offsetting structural strength is the recurring, less-cyclical mix (Market Intelligence, Indices, Mobility, Commodity Insights) that now makes up the majority of revenue and dampens the ratings cycle relative to a decade ago.

## 8. Next review trigger

- Next quarterly earnings release (Rule 9 standard re-score), or
- Quarterly Rate Environment Gate refresh (Jul 2026), or
- A fill of the ~$356–$382 limit-order watch (re-confirm R/R and size at execution), or
- Any Rule 9 event: guidance revision, management change, material M&A, or a >15% unexplained price move.
- **Priority redeployment candidate:** still the cleanest underweight BUY in the book; if proceeds are recycled from trims, SPGI is a primary destination — but via the limit-order discipline above, not a market chase.

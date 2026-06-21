# RESCORE — GOOG (Alphabet Inc., Class C)

## 1. Session header
- **Task type:** RESCORE (single ticker)
- **Date:** 2026-06-20
- **10Y US Treasury yield:** 4.46% (latest close, 2026-06-18; US bond market holiday 2026-06-19 — source: Federal Reserve H.15 / TradingEconomics via web search)
- **Rate Regime Modifier in effect:** +5 (10Y in the 3.5–5% band — "capital has real cost")
- **Prior score:** 83.7 (Very Expensive band → "Trim to 50%"), set 2026-06-07. This rescore re-derives from refreshed FY2025 statements and **applies the new Upside/Downside Modifier** (added 2026-06-20).

*Plain-English note: GOOG = Alphabet's Class C share. This is the parent of Google Search, YouTube, and Google Cloud. "Class C" (GOOG) has no voting rights; "Class A" (GOOGL) does — the economics are effectively identical and the framework treats them interchangeably for scoring.*

## 2. Data gaps flagged
- **Owner Earnings — maintenance-CapEx split not separately disclosed.** Alphabet does not break "maintenance CapEx" out from "growth CapEx" in its filings. Per Upgrade 1 the standard maintenance proxy is **Depreciation & Amortization (D&A** = the non-cash charge for wearing-out of existing assets, $21.1B FY2025). Used as the proxy and flagged here — not invented; it is the cleanest available stand-in. (Consequence: Owner Earnings collapses to Net Income — see §4.)
- **yfinance `info` snapshot fields were stale/mixed** (`totalRevenue` 422B, `freeCashflow` 27.9B looked like a forward/partial figure). I used the **audited annual statement values** from `t.financials`/`t.cashflow` (FY2025: Revenue $402.8B, EBIT $159.6B, Net Income $132.2B, FCF $73.3B) for all sub-scores, not the `info` snapshot. Market cap / EV / forward PE / PEG taken from the live `info` snapshot.
- **Net buyback %** estimated at ~1.2% of market cap from the FY2025 repurchase line; flagged as approximate (feeds only the small shareholder-yield component of E).

## 3. Rate Environment Gate
- **Step 1 — Earnings Yield Spread:** EY (earnings yield = 1 ÷ forward P/E) = 1 ÷ 25.35 = **3.94%**. Spread vs 10Y = 3.94% − 4.46% = **−0.52pp** (percentage points). < +1.5% → **FAIL → +5** to the score (yellow flag, not a veto).
- **Step 2 — Rate Regime Modifier:** 10Y 4.46% is in the 3.5–5% band → **+5**.

## 4. Full score calculation

**Live data first (Rule 0):**
- **Live price: $367.46** (source: `yfinance` intraday, 2026-06-20). *(IBKR `get_price_snapshot` was attempted first per the brief but permission was denied; fell back to yfinance.)*
- **52-week range:** $163.33 – $404.47 (yfinance). Price sits ~9% off the 52-wk high.
- **Analyst consensus PT (price target):** mean $426.62 / median $430.00, range $340–$475, n=13 (yfinance). Used only as a bull-case sanity anchor — bull FV $434 sits right at the median, so the bull case is not stretched beyond the Street.

**Inputs (FY2025 audited statements unless noted):**

| Metric | Value | Source |
|---|---|---|
| Market cap | $4.484T | yfinance info |
| Enterprise Value (EV) | $4.421T | yfinance info |
| Net Income | $132.2B | financials |
| D&A | $21.1B | cashflow |
| Total CapEx | $91.4B (2023 $32B → 2024 $53B → 2025 $91B) | cashflow |
| Reported FCF | $73.3B | cashflow |
| EBIT (earnings before interest & tax) | $159.6B | financials |
| Forward P/E | 25.35× ; forward EPS $14.50 | yfinance info |
| 5yr P/E avg / range | 24.5× / 18.2–30.6× (n=20 quarters, reconstructed) | yfinance |
| Trailing PEG | 1.45 | yfinance info |
| FCF/NI conversion | 100% / 94% / 73% / 55% (2022→2025) | computed |
| Gross / Net margin | 60.4% / 37.9% | yfinance |
| ROE | 38.9% | yfinance |
| Revenue growth | ~15% (FY25 $402.8B vs FY24 $350.0B) | financials |

**Owner Earnings adjustment (Upgrade 1) — REQUIRED for Alphabet:**
- Growth CapEx test: Maintenance proxy = D&A $21.1B. Growth CapEx = $91.4B − $21.1B = $70.3B = **76.9% of total CapEx** (» 30% threshold) → Owner Earnings **applies**.
- Owner Earnings = Net Income + D&A − Maintenance CapEx = $132.2B + $21.1B − $21.1B = **$132.2B**.
- **Owner Earnings yield = $132.2B ÷ $4,484B = 2.95%** (vs reported FCF yield 1.63% — the adjustment correctly avoids penalising the $70B AI/datacenter growth build-out, which depressed reported FCF). This 2.95% is the FCF sub-score input.

**Sub-scores** (0 = cheapest, 100 = most expensive):

- **FCF Yield (40%)** — Owner-Earnings yield 2.95%: `clamp(100 × (1 − 2.95/10)) = ` **70.5** → ×0.40 = **28.21**
- **EV/EBIT (25%)** — EV/EBIT = $4,421B ÷ $159.6B = **27.7×**: `clamp((27.7 − 12)/23 × 100) = ` **68.3** → ×0.25 = **17.07**
- **Forward P/E (20%)** — 5yr *range* available, so primary formula: `clamp((25.35 − 18.2)/(30.6 − 18.2) × 100) = ` **57.7** → ×0.20 = **11.53**. *(Fallback-vs-avg cross-check: forward PE 25.35 is +3.5% vs 5yr avg 24.5 → fallback score 58.7, essentially identical. Within ±10% of avg → no separate Historical-PE ±10 modifier.)*
- **PEG (15%)** — **Fast Grower eligible:** EPS grew >15%/yr for 3+ years on a clean GAAP base (NI $60.0B→$73.8B→$100.1B→$132.2B, 2022→2025; no one-off distortion). PEG 1.45: `clamp((1.45 − 0.5)/2.0 × 100) = ` **47.5** → ×0.15 = **7.12**

**Raw weighted = 28.21 + 17.07 + 11.53 + 7.12 = 63.94**

## 5. Upside/Downside Modifier (Expected-Return Modifier) — REQUIRED

*Plain-English: this folds the forward dimension — how much the position is actually expected to earn per year — into the score. Strong expected upside lowers the score; thin/negative expected return raises it toward trim. Bounded ±15.*

**Scenario fair values (Rule 7 — bull/base/bear, downside underwritten):**

| Scenario | Weight | Assumption | EPS × multiple | FV |
|---|---|---|---|---|
| Bull | 25% | AI monetization proves out, Cloud margins inflect, ad share defended; multiple holds | $15.5 × 28.0× | $434 |
| Base | 50% | Consensus fwd EPS, multiple = own 5yr avg | $14.50 × 24.5× | $355 |
| Bear | 25% | **AI-search disruption** erodes core query/ad share, EPS pressured, de-rate | $13.0 × 19.0× | $247 |

- **PW (probability-weighted) Fair Value = 0.25×434 + 0.50×355 + 0.25×247 = $348**
- **Gap Upside % = $348 ÷ $367.46 − 1 = −5.3%** (the blended FV is *below* the live price — GOOG is modestly above fair value even before the bear haircut)
- **Catalyst & timeline (Rule 10):** AI monetization proof-points + Google Cloud sustained profitability + demonstrated defense of search/ad share against generative-AI answer engines. Identifiable within **2 years** → annualized gap = −5.3% ÷ 2 = **−2.7%/yr**. Catalyst exists within 18–24mo → upside-side guardrail (−5 cap) does **not** bind.
- **Intrinsic growth:** forward EPS CAGR (compound annual growth rate), held conservatively at **+12%/yr** (Street ~13–15%; haircut for AI-disruption risk to the core).
- **Shareholder yield:** dividend 0.24% + net buyback ~1.2% = **+1.44%/yr**.

**E (expected annual return) = −2.7% + 12.0% + 1.44% = +10.8%/yr**

**Map to M** (hurdle H = 10%): E ≥ H → `M = −15 × clamp((10.8 − 10)/15, 0, 1) = −15 × 0.052 = ` **−0.8**

*Honest read: the modifier is near-neutral and barely negative. Almost the entire expected return is carried by intrinsic compounding — the valuation gap is actually negative (you are paying slightly above the scenario-blended fair value), and the bear case (AI search disruption → 33% drawdown to $247) is genuinely underwritten, not waved away. The ±15 cap is not even close to binding; a richly-priced name with only hurdle-level expected return correctly gets essentially no rescue and stays in the trim zone. This is the modifier working as intended in the "expensive" direction.*

## 6. Final score + action

**Final = 63.94 (raw) + 5 (Rate Step 1) + 5 (Rate Regime) + (−0.8) (Upside/Downside) = 73.14 → rounds to 73.1**

- **FINAL VALUATION SCORE: 73.1**
- **Action band: Score 70.0–79.9 → Expensive → TRIM 25–30%** (Phase 05)
- **Action CHANGED:** prior 83.7 was in the 80.0–89.9 band ("Trim to 50%"); 73.1 is now the milder 70.0–79.9 band ("Trim 25–30%"). The de-rate is *not* a price move — it is driven by (a) the Owner Earnings adjustment lifting the FCF sub-score off its prior near-max read, and (b) EV/EBIT compressing to 27.7× as FY2025 EBIT grew into the multiple. Still firmly expensive.

### Trim plan (order setup)
- **Blended (PW) Fair Value:** $348 | Base $355 | Bull $434
- **Primary Sell Target:** ~$355 (base/blended FV) — live price $367.46 is **above** blended FV, so there is **no margin of safety**; consistent with the trim signal.
- **Bull-Case Trim Target:** Bull FV $434 × 0.90 = **$391**
- **Trim sizing:** current weight **0.68%** → trim 25–30% of the position = **−0.17 to −0.20pp**, leaving ~**0.48–0.51%**.
- **Practical note:** the position is *de-minimis* (0.68% of portfolio). The trim is signal-consistent but tiny in dollar terms; recycle proceeds into a current Score 0.0–29.9 name per Phase 05. No stop/R-R setup is produced (this is a trim of a held name, not a new entry).
- **No fundamental sell trigger** is tripped (margins intact, ROIC 38.9% » cost of capital, no balance-sheet stress, score not in the 90+ sustained-exit zone). This is valuation-driven trimming only.

## 7. Portfolio rebalancing summary
Not applicable (single-ticker rescore). Trim feeds the next monthly rebalance / capital-recycling pass.

## 8. Next review trigger
- **Next quarterly earnings** (Alphabet Q2 FY2026, ~late July 2026) → Standard re-score.
- **Earlier if Rule 9 fires:** guidance revision, material M&A, a credible AI-search-disruption data point on core query/ad share, or a >15% unexplained price move.
- **Re-examine the Owner Earnings maintenance-CapEx proxy** at next touch — if Alphabet's CapEx normalizes off the FY2025 AI-build peak, the D&A proxy and the FCF sub-score will move.

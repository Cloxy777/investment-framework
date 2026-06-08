# NEW POSITION — ABNB (Airbnb Inc) — 2026-06-07

**Task type:** NEW POSITION
**Date:** 07 Jun 2026
**10Y US Treasury Yield:** 4.55% (close, 05 Jun 2026 — TradingEconomics/CNBC aggregation)
**Rate Regime Modifier in effect:** +0.5 (10Y in the 3.5–5% bracket)
**Current ABNB portfolio weight:** 0% — not currently held (not on `holdings.md`)
**Context:** flagged in this morning's [broad-quality-universe screening](2026-06-07-screening-broad-quality-universe.md) as the other "genuinely undetermined" name (score range 5–8) worth a dedicated full pull — this session resolves that.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$133.72** | IBKR `get_price_snapshot`, last completed-session close (`is_close: true`) |
| 52-week range | $110.81 – $147.25 | IBKR `get_price_snapshot` `misc-statistics` |
| Analyst consensus PT | ~$145–162 cluster (most sources ~$150, "Buy"/"Moderate Buy" from 25–36 analysts) | [MarketBeat](https://www.marketbeat.com/stocks/NASDAQ/ABNB/forecast/) / [StockAnalysis](https://stockanalysis.com/stocks/abnb/forecast/) / [WallStreetZen](https://www.wallstreetzen.com/stocks/us/nasdaq/abnb/stock-forecast) |

$133.72 sits roughly in the **middle of the 52-week range** — about 9% below the 52-week high ($147.25) and 21% above the 52-week low ($110.81); roughly 9–11% below the analyst PT cluster.

---

## 2. Data Gaps / Source Variance Flagged — *(more consequential here than for MA)*

| Issue | What I found | How I handled it |
|---|---|---|
| **No real 10-year PE history exists** | ABNB IPO'd Dec 2020 — only ~5.5 years of public trading. The only "historical average" sources report is a **4-year average ≈ 37×**, built from a PE range that swung from **16× to 132×** across the company's unprofitable→profitable transition and the 2021–22 high-multiple/meme-stock period. | Treated as a **genuine data gap, not a usable input** — see Historical PE Modifier discussion in §5. Forcing a mean-reversion read off a statistically non-representative 5-year window would itself be a form of "inventing" a signal the framework's Rule 0/non-negotiables warn against. |
| **Headline EPS-growth figures are contaminated by one-time items** | Q3 2023 net income included a **one-time $2.8B tax valuation-allowance release** that spiked that year's EPS to ~$8.53 in a single quarter — the very thing driving the "20%+ 5yr EPS CAGR" headline numbers aggregators report. 2024 diluted EPS was $4.11; 2025 (~$2.5B NI ÷ ~600M diluted shares) comes out to roughly **flat, ~$4.15–4.20** — a sharp deceleration from the headline growth story. | Used the **cleaner, non-contaminated growth reads** instead (recomputed revenue CAGR from primary filings; forward consensus EPS growth from analyst estimates) — see PEG discussion in §5. |
| **Screening session's "29.50% revenue CAGR" proxy was a 5-year metric distorted by COVID base effects** | I recomputed the actual 3-year CAGR directly from reported annual revenue ($8.4B → $9.9B → ~$11.1B → $12.2B, 2022–2025): **≈13.2%**, not 29.5%. | Used the recomputed 13.2× figure — still clears the >10% gate, but it changes the "fast grower" read materially (see §5). |

No metric was *missing* outright — every input was sourced from primary filings or cross-checked aggregators — but two of the four genuinely matter for the score (Historical PE Modifier, Fast-Grower/PEG classification), and I want that visible rather than buried in a single point estimate.

---

## 3. Phase 01 — Quality Gate

| Check | ABNB Value | Threshold | Result |
|---|---|---|---|
| Net margin | ~20.5% (FY2025: $2.5B NI ÷ $12.2B revenue) | >15% | ✅ PASS |
| ROIC | ~24.89% | >15% | ✅ PASS |
| Revenue CAGR (3yr, recomputed from primary filings) | ~13.2% — $8.4B (2022) → $12.2B (2025): (12.2/8.4)^(1/3)−1 | >10% | ✅ PASS (correcting the screening's COVID-distorted 29.5% proxy) |
| Gross margin | 72.38% | >40% or expanding | ✅ PASS |
| FCF positive 3+ consecutive years | Yes — $3.4B (2022) → $3.8B (2023) → $4.5B (2024) → ~$4.5B TTM (2025) | required | ✅ PASS |
| Net debt/EBITDA | **Net cash** position (debt $2.07B vs. cash $9.63B → ~−$7.56B net cash) | <2× | ✅ PASS — trivially, by holding *more cash than debt* |
| FCF/NI conversion ratio | ~180% (TTM FCF $4.5B ÷ FY2025 NI $2.5B) | >70% for 2+ years | ✅ PASS — but flagged: this *gap* (FCF running ~1.8× GAAP earnings) is float-driven (guest payments collected before host payouts) plus heavy stock-based-comp add-backs, not "clean" owner-earnings-style conversion. Worth remembering FCF here runs structurally richer than GAAP profit suggests — a real strength for cash generation, but SBC is a real economic cost that GAAP net income (correctly) captures and FCF does not. |
| Share issuance pattern | Actively repurchasing ($3.8B in 2025) against meaningful SBC issuance; share count roughly flat-to-modestly-up over recent years | not dilutive | ✅ PASS (not a concerning dilutive *pattern*) — though SBC remains large enough to be worth tracking under Phase 04's "earnings quality" lens going forward |
| Moat signal | Two-sided marketplace network effects, brand, host/guest trust system | required | ✅ PASS (qualitative — see §6) |

**Gate result: PASS.** ABNB clears every quantitative bar — comfortably on profitability/margins/balance-sheet, more narrowly (but still clearly) on growth once the COVID-base-effect distortion is corrected for. Proceeding to Phase 02.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $133.72 ÷ $5.10 (2026 consensus EPS, midpoint of $5.05–5.20 estimates) ≈ 26.0×
EY         = 1 ÷ 26.0 = 3.85%
Spread     = EY − 10Y Treasury = 3.85% − 4.55% = −0.70%
```
Spread (−0.70%) < +1.5% → **fails** the spread test → **+0.5 additive modifier** (yellow flag, not a veto — per the now-corrected [strategy.md](../framework/strategy.md) / [operating-brief.md](../framework/operating-brief.md) rule).

**Step 2 — Rate Regime Modifier**
10Y yield = 4.55% → **3.5–5% bracket → +0.5**

**Combined Rate-related additive modifier: +0.5 + 0.5 = +1.0** (identical to MA's — same macro backdrop, same day)

---

## 5. Phase 02 — Full Valuation Score

### FCF Yield (40% weight)
```
TTM FCF    ≈ $4.5B (39% TTM FCF margin, per multiple cross-checked sources)
Market cap  = 593.5M shares × $133.72 ≈ $79.36B
FCF Yield   = $4.5B ÷ $79.36B ≈ 5.67%
```
Falls solidly in the **"4–6% → sub-score 4–5"** band, toward its higher-yield (cheaper) end → **sub-score = 4**

*No Owner Earnings adjustment (Upgrade 1) applies — ABNB is an asset-light marketplace; its FCF/CapEx profile shows essentially no traditional CapEx (FCF ≈ OCF), so there's no growth-CapEx distortion to correct for.*

**FCF sub-score: 4**

### EV/EBIT (25% weight, → 40% after PEG redistribution — see below)
```
EV       = Market cap $79.36B + Net debt (−$7.56B net cash) ≈ $71.80B
EBIT TTM = FY2025 $2,544M − Q1'25 $38M + Q1'26 $86M = $2,592M
EV/EBIT  = $71.80B ÷ $2.592B ≈ 27.7×
```
Falls in the **"22–28× → sub-score 6–7"** band, near its top (expensive) end → **sub-score = 7**

### Forward PE + Historical PE Modifier (20% weight)
```
Forward PE  ≈ 26.0× (computed above)
```
- Raw sub-score vs. sector norms: ABNB sits roughly mid-pack to moderately-rich among consumer-internet/travel-marketplace peers (BKNG ~22–24× fwd, EXPE ~12–14×, UBER/META in the 20–28× range for asset-light platforms) → **raw sub-score ≈ 5** (moderate)
- **Historical PE Modifier: NOT APPLIED.** As flagged in §2, no real 10-year history exists for a company that's been public ~5.5 years, and the only available average (~37×, "last 4 years") is built from a 16×–132× range spanning the company's unprofitable→profitable inflection and 2021–22 high-multiple period — using it as a mean-reversion anchor would be statistically closer to manufacturing a signal than reading one. This is a genuine "the data this rule needs doesn't actually exist in usable form" case, distinct from MA's (which had a clean, stable decade of trading history to anchor on).

**Adjusted FwdPE sub-score: 5** (no modifier — flagged data gap, not a zero-modifier judgment)

### PEG Modifier (15% weight) — Fast Grower classification: genuinely contaminated data
EPS-growth evidence found:
- **Headline "fast grower" figures are statistical artifacts**: the ~20%+ 5yr EPS CAGR cited by aggregators is driven substantially by (a) the 2021–22 unprofitable→profitable inflection (huge % growth off a near-zero/negative base) and (b) the **one-time $2.8B tax-valuation-allowance release in Q3 2023** that briefly spiked EPS to ~$8.53/quarter
- **Cleaner reads tell a different story**: 2024 diluted EPS $4.11 → 2025 ~$4.15–4.20 (roughly **flat**, low-single-digit growth); recomputed revenue 3yr CAGR ≈ **13.2%** (below the >15% Fast-Grower bar); forward consensus EPS growth ≈ **15.6%/yr** (right at the boundary, and consensus estimates for 3-5yr-out growth tend to run optimistic)

**Judgment call: NOT classifying ABNB as a clean Fast Grower.** The headline ">15% for 3+ years" read is an artifact of base effects and a one-time tax item, not a real sustained trend — and every *clean* growth signal I can construct (recomputed revenue CAGR, actual 2024→2025 EPS trajectory) sits at or below the 15% bar.

→ **PEG not applied.** Per [valuation-scoring.md](../framework/valuation-scoring.md): redistribute its 15% weight to EV/EBIT (making EV/EBIT weight 40%).

> ⚠️ **Separate framework inconsistency worth fixing regardless of this ticker** (also surfaced in this morning's screening session): [valuation-scoring.md](../framework/valuation-scoring.md) treats PEG as a **15%-weighted 1–10 sub-score** in the final-score formula, while [strategy.md](../framework/strategy.md) Upgrade 3's table maps PEG values to **small additive modifiers (−1 to +1)**. These two scales can't both be right in the same formula — multiplying a ±1 modifier by 15% produces a ~7–15× smaller effect than a 1–10 sub-score would. Worth resolving in a framework-cleanup pass (I didn't fix it here because it wasn't load-bearing for *this* ticker once the Fast-Grower question resolved to "no" — but it will be load-bearing the next time a clean Fast Grower comes up for evaluation).

### Final Score Calculation
```
Final Score = (FCF × 0.40) + (EV/EBIT × 0.40) + (FwdPE_adj × 0.20) + Rate Modifiers
            = (4 × 0.40)  + (7 × 0.40)        + (5 × 0.20)         + 1.0
            = 1.6         + 2.8               + 1.0                + 1.0
            = 6.4
```
6.4 → rounds to **6** (not on a .5 boundary; standard rounding)

### Robustness check — does this hold up against the close judgment calls?
| If I'd instead chosen... | Final Score | Action zone |
|---|---|---|
| FCF sub-score 5 (not 4) | 6.8 → **7** | Fair Value / Watchlist |
| EV/EBIT sub-score 6 (not 7) | 6.0 → **6** | Fair Value / Watchlist |
| FwdPE_adj = 4 (forcing the noisy −1 historical modifier anyway) | 6.2 → **6** | Fair Value / Watchlist |

**Every plausible resolution of the genuinely-close calls lands in the 6–7 band.** Unlike MA (where the data gap was the *entire* swing factor between "Cheap — buy" and "Fair Value — watch"), ABNB's verdict is **robust to its data gaps** — it's squarely in Fair Value territory regardless of how the close calls resolve.

---

## 6. Final Valuation Score & Action

# **Final Score: 6 — "Fair Value"**

| Score | Label | Action (Phase 03 / strategy.md Action Table) |
|---|---|---|
| **6–7** | **Fair Value** | **HOLD / Watchlist only — no new entry, no trim** |

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Step 2 integration table: *"Score 6–7 → No MoS → Watchlist only."*

### Qualitative cross-check (5 questions)
1. **Why are margins high?** Asset-light two-sided marketplace — connects ~5M+ hosts with guests globally, captures a take-rate on each booking with minimal incremental cost.
2. **What would it take to compete?** Building trust and liquidity on *both* sides simultaneously (hosts won't list without guest demand, guests won't book without host supply) — a genuine network-effect moat, though one that newer entrants (Vrbo/Expedia, regional players, hotel-chain alternative-stay programs) continue to chip at on the margins.
3. **Capital allocation:** $3.8B in buybacks in 2025, funded entirely from FCF, against a net-cash balance sheet — disciplined. Counterpoint: SBC issuance is large enough that it's effectively funding a meaningful share of those buybacks just to hold the count flat — a real (if non-cash) cost worth tracking under Phase 04.
4. **Growth sources next 3–5 years:** International expansion (still under-penetrated vs. US/Europe), the "Experiences" vertical, loyalty/repeat-guest programs — though revenue growth has visibly decelerated from the high-20s% (post-COVID recovery years) to low-double-digits now, a maturing-platform profile rather than an accelerating one.
5. **Best bear case / disruption vector:** (a) **Regulatory crackdowns on short-term rentals** — an active, well-documented, multi-jurisdiction trend (NYC, Barcelona, Paris, and others have all tightened rules in recent years) that directly constrains supply in ABNB's most valuable markets; (b) **growth deceleration as core markets mature** — the 29%→13% CAGR compression is real, not a data artifact; (c) **a live, open disruption question**: could an AI travel-agent/booking-assistant layer (the kind hyperscalers are actively building) disintermediate the marketplace itself, routing bookings around the ABNB brand/app entirely?

This is a good business with a real (if more contested) moat than MA's — but it's also a *visibly maturing* one, trading at a price that already reflects "good," not "cheap."

---

## 7. Order Setup — NOT PRODUCED (by design)

Same logic as the MA session: the full FV/DCF/buy-sell-stop workup is reserved for **BUY or TRIM** actions (the order-setup checklist itself gates on *"Valuation Score: ___ (must be ≤ 5 to enter)"*). A Score of 6 is neither — building a speculative DCF here would mean inventing forward assumptions to justify a trade the framework says not to make.

**For watchlist-tracking purposes only** (not a standing order, not a trigger): a decline toward roughly the **$100–112** zone (≈16–25% below today, i.e., toward/through the 52-week low of $110.81) would lift FCF yield toward ~6.7–7.5% (sub-score ~2–3) and pull EV/EBIT toward ~21–23× (sub-score ~5–6) — which, even without resolving the PEG/historical-PE data gaps, would plausibly pull the blended score into the 4–5 ("Cheap — standard position") band. **This is a level worth a fresh, full re-score if reached** — not a commitment to act on touch.

---

## 8. Recommendation

# **WATCHLIST ONLY — pass on entry now.**

ABNB clears the Phase 01 quality gate cleanly — strong margins, a genuine (if more contested than MA's) network-effect moat, a net-cash balance sheet, and best-in-class FCF generation for a consumer-internet name. But the Phase 02 valuation score of **6 ("Fair Value")** — and importantly, a score that's **robust to every genuinely-close judgment call in this analysis** — means there's currently no margin of safety. This isn't a coin-flip verdict resting on one shaky number (as MA's nearly was); it's a name that's priced for the "good, maturing platform" it currently is.

**Add ABNB to the watchlist** with a re-score trigger at:
- **Next earnings release** (Rule 9 quarterly trigger — ABNB typically reports early-to-mid August for Q2)
- **Any move >15%** without a known fundamental driver (Rule 9 automatic trigger), particularly a decline toward/through the 52-week low ($110.81) and into the ~$100–112 zone sketched above
- **Any fundamental event**: regulatory action on short-term rentals in a major market, guidance revision, M&A, management change, or a credible short thesis

---

## 9. Next Review Trigger

**Date/event:** ABNB's next quarterly earnings release (expected early-to-mid August 2026), OR any >15% price move without a documented fundamental driver, OR a material regulatory/fundamental event (especially short-term-rental regulation in a top-5 market), whichever comes first.

**No position opened — nothing to log in `decisions/`.**

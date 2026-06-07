# NEW POSITION — MA (Mastercard Inc) — 2026-06-07

**Task type:** NEW POSITION
**Date:** 07 Jun 2026
**10Y US Treasury Yield:** 4.55% (close, 05 Jun 2026 — TradingEconomics/CNBC aggregation)
**Rate Regime Modifier in effect:** +0.5 (10Y in the 3.5–5% bracket)
**Current MA portfolio weight:** 0% — not currently held (not on `holdings.md`)

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$481.76** | IBKR `get_price_snapshot`, last completed-session close (`is_close: true`) |
| 52-week range | $464.58 – $599.81 | IBKR `get_price_snapshot` `misc-statistics` |
| Analyst consensus PT | ~$640–650 cluster (median $665, range $550–735, "Strong Buy" from 39–53 analysts) | [MarketBeat](https://www.marketbeat.com/stocks/NYSE/MA/forecast/) / [WallStreetZen](https://www.wallstreetzen.com/stocks/us/nyse/ma/stock-forecast) / [TIKR](https://www.tikr.com/blog/mastercard-stock-heres-why-analysts-target-655-in-2026) |

Note: $481.76 sits in the **bottom third of the 52-week range** ($464.58–$599.81) — roughly 20% below the 52-week high and consistent with the "20% below GF Value ($637.81)" read independently reported by GuruFocus.

---

## 2. Data Gaps / Source Variance Flagged

| Metric | Range found | What I used & why |
|---|---|---|
| ROIC | 41.36% (GuruFocus) – 50.04% (FinanceCharts), 20yr avg ~48.75% | Used ~41–50% range — all land far above the >15% gate threshold, so the precise figure doesn't change the qualitative read |
| 10-yr average PE | 37.53× (FullRatio) – 38.13× (FinanceCharts) – 37.87× (Wisesheets) | Used midpoint **~37.8×** |
| Forward EPS growth (the input PEG conventionally uses) | Near-term consensus: +15.1% (2026, $16.54→$19.58) and +15.7% (2027, $19.58→$22.65); but separately-cited longer-run consensus: ~10.9–13%/yr | Flagged explicitly below — this spread is the crux of the Fast-Grower classification call |
| "Gross margin" | Reported as ~100% by data aggregators | Payment-network revenue-recognition quirk (no traditional COGS) — not a meaningful read; used **operating margin (59.17%)** as the cleaner profitability proxy. Either way the >40% gate clears trivially. |

No metric was missing outright — all required Phase 01/02 inputs were obtainable from primary filings (10-Q, 8-K earnings releases) or cross-checked aggregators.

---

## 3. Phase 01 — Quality Gate

| Check | MA Value | Threshold | Result |
|---|---|---|---|
| Net margin | 45.65% (TTM: $14.97B NI ÷ $32.79B revenue) | >15% | ✅ PASS |
| ROIC | ~41–50% | >15% | ✅ PASS |
| Revenue CAGR (3yr) | ~13.8% — $22.24B (2022) → $32.79B (2025): (32.79/22.24)^(1/3)−1 | >10% | ✅ PASS |
| Gross margin | ~100% reported (operating margin 59.17% as cleaner proxy) | >40% or expanding | ✅ PASS |
| FCF positive 3+ consecutive years | Yes — FCF-positive every year for over a decade | required | ✅ PASS |
| Net debt/EBITDA | ~0.49× ($11.1B net debt ÷ ~$22.5B EBITDA) | <2× (core) / <2.5× (pre-screen) / <4× (Upgrade 5 asset-light networks) | ✅ PASS — clears even the *strictest* threshold by 4–5× margin |
| FCF/NI conversion ratio | ~114.6% ($17.16B FCF ÷ $14.97B NI) | >70% for 2+ years | ✅ PASS |
| Share issuance pattern | Non-dilutive — aggressive multi-year buyback program (892.4M shares out, declining trend) | not dilutive | ✅ PASS |
| Moat signal | Duopoly network effect (Visa/Mastercard), brand, switching costs, regulatory moat | required | ✅ PASS (qualitative — see §6) |

**Gate result: PASS, comfortably.** MA is a textbook "wonderful business" by this framework's own quality criteria — high, durable margins; minimal leverage; near-total FCF conversion; long buyback history. Proceeding to Phase 02.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $481.76 ÷ $19.58 (2026 consensus EPS) ≈ 24.6×
EY         = 1 ÷ 24.6 = 4.07%
Spread     = EY − 10Y Treasury = 4.07% − 4.55% = −0.48%
```
Spread (−0.48%) < +1.5% threshold → **fails** the spread test.

> Per [strategy.md](../framework/strategy.md) (updated 2026-06-07, see [decisions/2026-06-07-framework-fixes-investor-philosophy-alignment.md](../decisions/2026-06-07-framework-fixes-investor-philosophy-alignment.md)), this is **no longer a hard veto** — it converts to an **additive +0.5 to the valuation score** (a yellow flag that raises the bar rather than blocking the name outright).
>
> ⚠️ **Documentation inconsistency flagged:** [operating-brief.md](../framework/operating-brief.md) (the reproduced system-prompt text) still reads *"Pass threshold ≥ +1.5%. Fail = no new entry"* — it was not updated alongside strategy.md's 2026-06-07 revision. I followed **strategy.md** (the dated, rationale-bearing canonical source) rather than the stale brief text. Worth syncing operating-brief.md to match.

**Step 2 — Rate Regime Modifier**
10Y yield = 4.55% → falls in the **3.5–5% bracket → +0.5**

**Combined Rate-related additive modifier: +0.5 (spread fail) + 0.5 (regime) = +1.0**

---

## 5. Phase 02 — Full Valuation Score

### FCF Yield (40% weight)
```
TTM FCF      = OCF $17.65B − CapEx $0.489B = $17.16B
Market cap   = 892.44M shares × $481.76 ≈ $429.94B
FCF Yield    = $17.16B ÷ $429.94B ≈ 3.99% (~4.0%)
```
Lands almost exactly on the boundary between "2–4% → 6–7" and "4–6% → 4–5." Per the framework's stated bias toward conservatism at score boundaries, I read this as the high (cheap) edge of the **2–4% band → sub-score = 6**.

*No Owner Earnings adjustment (Upgrade 1) applies — MA is asset-light; CapEx ($489M) is just ~3% of OCF, nowhere near the 30%-of-total-CapEx growth-CapEx trigger.*

**FCF sub-score: 6**

### EV/EBIT (25% weight, → 40% after PEG redistribution — see below)
```
EV       = Market cap $429.94B + Net debt $11.1B ≈ $441.0B
EBIT TTM = $19.3B
EV/EBIT  = $441.0B ÷ $19.3B ≈ 22.85×
```
Falls in the "22–28× → sub-score 6–7" band, near its low (cheap) end → **sub-score = 6**

### Forward PE + Historical PE Modifier (20% weight)
```
Forward PE     ≈ 24.6× (computed above)
10yr avg PE    ≈ 37.8× (midpoint of 37.5–38.1× sources)
Δ vs 10yr avg  = (24.6 − 37.8) ÷ 37.8 ≈ −34.9%
```
- Raw sub-score vs sector norms (1=very low, 10=very high): MA's 24.6× sits roughly mid-pack among payment-network/financial peers (V ~27–29×, AXP ~18–20×, PYPL ~13–15×) → **raw sub-score ≈ 5** (moderate)
- Historical PE Modifier (Upgrade 2): **>20% below 10yr average → −1**
- *Structural Quality Override check:* the override only ever **blocks** a +1 "expensive" penalty when multiple expansion reflects genuine quality improvement — it's not invoked here, since this is a −1 "cheap" signal already running in MA's favor.

**Adjusted FwdPE sub-score: 5 − 1 = 4**

### PEG Modifier (15% weight) — Fast Grower classification call
EPS growth data found:
- Trailing 3yr CAGR ≈ 17.3%, trailing 5yr ≈ 20.9–23.6% → *technically* clears the ">15% for 3+ years" quantitative bar
- **But** forward consensus is decelerating: 2026E +15.1% ($16.54→$19.58), 2027E +15.7% ($19.58→$22.65), and separately-cited longer-run (multi-year) consensus growth sits at **~10.9–13%/yr** — the figure a forward-looking PEG ratio should really be measured against
- EPS growth (18.9%) only modestly outpaces revenue growth (16.4%) — gap of 2.5pp, well under the 10pp "buyback-masking" flag in Phase 04

**Judgment call: I am classifying MA as a Stalwart, not a Fast Grower**, despite its trailing 3yr EPS growth technically clearing the >15% threshold:
1. A $430B mega-cap with growth visibly decelerating toward low-double-digits is exactly Lynch's definition of a Stalwart, not a Fast Grower (Lynch's Fast Growers are the smaller, longer-runway compounders)
2. The PEG ratio is fundamentally forward-looking, and the forward-looking consensus growth rate (~11–15%, trending toward the low end) is below the framework's own >15% bar
3. [fair-value-methodology.md](../framework/fair-value-methodology.md) explicitly instructs: *"Do not apply [PEG] to cyclicals, mature stalwarts, or turnarounds"*

→ **PEG not applied.** Per [valuation-scoring.md](../framework/valuation-scoring.md): *"If PEG is not applicable (non-Fast Grower), redistribute its 15% weight to EV/EBIT (making EV/EBIT weight 40%)."*

*(For transparency: had I instead treated MA as a Fast Grower, PEG = Forward PE ÷ growth ≈ 24.6 ÷ 13–15 ≈ 1.6–1.9, landing in the "1.2–1.8 → +0.5" / "borderline >2.0" zone — i.e., even the alternate path would not have meaningfully changed the final action band.)*

### Final Score Calculation
```
Final Score = (FCF × 0.40) + (EV/EBIT × 0.40) + (FwdPE_adj × 0.20) + Rate Modifiers
            = (6 × 0.40)  + (6 × 0.40)        + (4 × 0.20)         + 1.0
            = 2.4         + 2.4               + 0.8                + 1.0
            = 6.6
```
6.6 is not exactly on a .5 boundary, so standard rounding applies → **rounds to 7**

---

## 6. Final Valuation Score & Action

# **Final Score: 7 — "Fair Value"**

| Score | Label | Action (Phase 03 / strategy.md Action Table) |
|---|---|---|
| **6–7** | **Fair Value** | **HOLD / Watchlist only — no new entry, no trim** |

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Step 2 integration table: *"Score 6–7 → No MoS → Watchlist only."*

### Qualitative cross-check (5 questions)
1. **Why are margins high?** Two-sided network effect + scale — MA earns a toll on a duopoly rail (with Visa) that merchants and banks can't easily route around.
2. **What would it take to compete?** Building trust with billions of cardholders, tens of millions of merchants, and thousands of issuing/acquiring banks simultaneously — a multi-decade chicken-and-egg problem. Hard moat.
3. **Capital allocation:** Consistent buybacks (shrinking float for years) + growing dividend + disciplined bolt-on M&A (e.g., the BVNK stablecoin-infrastructure deal, ~$1.5B, announced alongside Q1 2026 results) funded from FCF, not debt.
4. **Growth sources next 3–5 years:** Continued cross-border volume growth (+15% in 2025, +13% in Q1 2026), and accelerating Value-Added Services & Solutions revenue (+26% in 2025, +22% in Q1 2026) — a genuine second growth engine diversifying away from pure transaction-toll economics.
5. **Best bear case / disruption vector:** Real-time payment rails (e.g., FedNow, Pix, UPI) and stablecoin/crypto settlement rails could disintermediate card networks over a long horizon — though MA's BVNK acquisition reads as a hedge (own a piece of the disruption rather than be run over by it). Regulatory/interchange-fee pressure (EU, US merchant litigation) is the more near-term risk to monitor.

None of this changes the **quantitative** verdict — MA is an excellent business, just not currently a *cheap* one.

---

## 7. Order Setup — NOT PRODUCED (by design)

Per the operating brief, the full Fair-Value/DCF/buy-sell-stop workup is run **"for every BUY or TRIM action."** A Score of 7 is neither — it's Hold/Watchlist. The order-setup checklist itself gates on *"Valuation Score: ___ (must be ≤ 5 to enter)."* Building a full 3-scenario DCF here would mean inventing forward growth/WACC assumptions to justify a trade the framework explicitly says not to make — so I'm not doing that.

**What I can say without inventing numbers:** $481.76 sits ~27% below the analyst consensus PT cluster (~$640–650) and ~24% below GuruFocus's independently-modeled FV ($637.81) — those are *other parties'* fair-value reads, cited as context (per Rule 0 Step 4's "note analyst consensus PT for bull-case sanity check"), not this framework's own blended FV. The valuation-score engine — which is what this framework actually trades on — currently reads "fairly valued," not "cheap," because EV/EBIT (~22.9×) and FCF yield (~4.0%) sit in the middle of their respective bands even though the *PE-relative-to-history* signal is favorable (−1 modifier).

**Rough sense of what would flip this to a BUY** (scenario sketch only — not a trigger to act on, just a level to watch): a decline toward roughly the **$390–420** zone (≈15–20% below today, i.e., toward/through the 52-week low of $464.58 and below) would lift FCF yield toward ~4.5–5% and pull EV/EBIT toward ~18–19×, which combined with the existing −1 historical-PE modifier could plausibly pull the blended score into the 4–5 ("Cheap — standard position") band. **This is not a standing order or a commitment — it's a level worth a fresh, full re-score if reached**, consistent with Rule 9 (>15% move triggers re-score regardless).

---

## 8. Recommendation

# **WATCHLIST ONLY — do not open a position now.**

MA passes the Phase 01 quality gate about as cleanly as any name in this framework's universe — exceptional margins, minimal leverage, near-total FCF conversion, durable network-effect moat, intelligently-run capital allocation. But the Phase 02 valuation score of **7 ("Fair Value")** means there is currently **no margin of safety** to justify a new entry; per the framework's own rules, Score 6–7 = hold-and-watch, not buy. Acting now would mean paying a fair price for a wonderful business rather than a wonderful price — exactly the trap Rule 0 / the non-negotiables exist to prevent ("act only on documented triggers — a valuation-score change or a fundamental event, never on price movement alone").

**Add MA to the watchlist** with a re-score trigger at:
- **Next earnings release** (standard Rule 9 quarterly trigger — MA reports late July/early Aug 2026 for Q2)
- **Any move >15%** without a known fundamental driver (Rule 9 automatic trigger) — particularly a decline toward/through the 52-week low ($464.58) and into the ~$390–420 zone sketched above
- **Any fundamental event**: guidance revision, M&A (the BVNK stablecoin deal bears watching for integration progress/impact), management change, or a credible short thesis

---

## 9. Next Review Trigger

**Date/event:** Mastercard's next quarterly earnings release (expected late July/early August 2026), OR any >15% price move without a documented fundamental driver, OR a fundamental event (guidance change, M&A developments — esp. BVNK), whichever comes first.

**No position opened — nothing to log in `decisions/`.**

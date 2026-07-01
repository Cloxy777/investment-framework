# NEW POSITION — PDD (PDD Holdings Inc.) — 2026-07-01

**Task type:** NEW POSITION
**Date:** 01 Jul 2026
**10Y US Treasury Yield:** 4.45% (mid of 4.44–4.46% range, TradingEconomics/YCharts, 30 Jun 2026 — same figure used in today's VEEV session)
**Rate Regime Modifier (Step 2):** +5 (3.5–5% bracket)
**Current PDD portfolio weight:** 0% — not held
**Sector:** China E-commerce — asset-light marketplace/social-commerce (Pinduoduo domestic) + cross-border discount retail (Temu international)

> **Context:** PDD was scored once before, [14 Jun 2026](2026-06-14-new-position-pdd.md), at 5.0 ("Very Cheap," BUY) — but that score predates **three** methodology changes since (5yr auto-PE reconstruction, the Upside/Downside Modifier, both 2026-06-20; and the Quality Score + 80.0+ gate + Composite Score, 2026-06-29). It's been flagged stale in [watchlist/STALE.md](../watchlist/STALE.md) since 2026-06-20. This session was originally requested as `/rescore PDD`, but PDD isn't a holding — redirected to `/new-position` per the user's choice. This is a full re-run, not an update: fresh live price, fresh Quality Score (first time under the current methodology), and a fresh Valuation Score.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price** | **$82.51** | IBKR `get_price_snapshot`, contract 326398585 (NASDAQ) |
| Today's change | +$6.23 / **+8.17%** | IBKR snapshot |
| 52-week range | $71.94 – $139.41 | IBKR snapshot |
| Shares outstanding | 1.4234B | `yfinance` |
| Market Cap | $117.44B | 1.4234B × $82.51 |

**Today's +8.17% jump is a real, identified, non-price-action trigger — not acted on alone, but relevant context.** WebSearch attributes it to (a) broader Chinese-equities rebound, (b) an Arete upgrade to Buy ($121 PT, citing improving earnings outlook and Temu share gains), and (c) continued relief that China's State Administration for Market Regulation resolved its "Ghost Takeaway" food-safety probe with a RMB1.5B fine back in **April 2026** (predates the 06-14 session; not new information, just still working through the market's re-rating). **One genuinely new item since 06-14:** the EU fined Temu **€200M (~$232M)** under the Digital Services Act on 28 May 2026 for failing to police unsafe products (baby toys, chargers) sold on the platform — small relative to PDD's scale (net cash alone is ~$63B) but a real, incremental regulatory-risk data point, folded into the bear case below.

---

## 2. Data Gathered — Quality Score inputs (TTM = 4 quarters ending 31 Mar 2026, `yfinance`, financial-statement currency **CNY/RMB** — confirmed via `financialCurrency` field; converted at **6.79 CNY/USD**, TradingEconomics/Wise, 01 Jul 2026)

| Metric | Value (RMB) | Value (USD) | Source |
|---|---|---|---|
| Revenue (TTM) | ¥442.40B | $65.16B | `yfinance` quarterly financials |
| Operating Income / GAAP EBIT (TTM) | ¥96.58B | $14.22B | `yfinance` (used over the `EBIT` field, which includes a large Q4 2025 one-off gain — see Gap #1) |
| Net Income (TTM) | ¥95.65B | $14.09B | `yfinance` |
| FCF (TTM, ≈ OCF, capex immaterial) | ¥106.72B | $15.72B | `yfinance` |
| Cash + ST Investments (31 Mar 2026) | ¥436.07B | $64.23B | `yfinance` balance sheet |
| Total Debt | ¥5.12B | $0.75B | `yfinance` |
| Stockholders' Equity (31 Mar 2026) | ¥423.43B | $62.36B | `yfinance` |
| Net Margin (TTM) | — | **21.6%** | Computed (currency-neutral ratio; matches `yfinance` `profitMargins` 21.62% exactly) |
| Gross Margin | — | **56.0%** | `yfinance` |
| Revenue 3yr CAGR (FY2022→FY2025) | ¥130.56B → ¥431.85B | **49.0%** | Computed — matches prior session's figure exactly |
| FCF/NI ratio (TTM) | — | **111.6%** | Computed |
| Effective tax rate (FY2025) | 18.2% | | `yfinance` |

**Hard disqualifiers check:** FCF/NI never below 70% in any of the last 4 years (108–156% range, FY2022–2025) — pass. Net Debt/EBITDA — deep net cash — pass. FCF positive every year FY2022–2025 — pass. **No disqualifiers.**

### Data Gaps / Flags

1. **`EBIT` vs `Operating Income` — used Operating Income.** `yfinance`'s `EBIT` field for Q4 2025 (¥52.54B) is roughly double `Operating Income` for the same quarter (¥26.20B) — looks like a one-off gain (likely an equity-investment fair-value mark) folded into `EBIT` but excluded from `Operating Income`. Used `Operating Income` throughout as the cleaner GAAP-operating-profit read, consistent with the 06-14 session's own approach (its RMB94.6B FY2025 figure lines up almost exactly with this session's ¥96.58B TTM Operating Income once the extra 3 months are added — good cross-check).
2. **ROIC — the same gate-critical judgment call flagged in today's VEEV session, but worse here: the standard cash-adjusted formula is mathematically undefined for PDD.** Cash-adjusted Invested Capital = Debt + Equity − Cash&ST-Investments = ¥5.12B + ¥423.43B − ¥436.07B = **−¥7.52B — negative.** PDD's cash-and-investments pile *exceeds its entire book capitalization* (debt+equity combined), so there's no meaningful cash-adjusted ROIC to compute (division by a negative/near-zero denominator is not a real number). **Used unadjusted ROIC = NOPAT ÷ Equity = (¥96.58B × (1−18.2%)) ÷ ¥423.43B = ¥79.00B ÷ ¥423.43B = 18.66%** as the only internally-consistent, computable figure — not a preference between two valid options like the VEEV case, closer to a forced choice given the alternative is undefined. **This is still gate-critical**: the 06-14 session separately cross-checked external ROE estimates ranging 9.28%–35.89% (GuruFocus/DBS/FinanceCharts, various dates/definitions) for the same "equity-heavy structure" reason. Quality Score sensitivity to this single input:

   | ROIC input used | Quality Score | Gate (80.0+)? |
   |---|---|---|
   | 9.28% (low external estimate — nominal ROE) | 77.4 | **FAILS** |
   | **18.66% (primary — NOPAT/Equity, this session)** | **81.3** | **PASSES** |
   | 35.89% (high external estimate) | 86.0 | PASSES |

   Two of three plausible readings clear the gate; the lowest doesn't. Flagged with the same weight as VEEV's equivalent issue — this determines whether PDD gets a Composite Score at all.
3. **5yr auto-PE reconstruction (the framework's standard `yfinance` method) produced an implausible range for PDD** — avg 6.49×, low 1.18×, high 64.79× (n=20 quarters) — the 1.18× low in particular isn't a believable trading multiple for a profitable company. Likely an artifact of PDD's genuinely volatile earnings history (per-ADS EPS swung from ~$3 to ~$10 and back down over 4 years) breaking the rolling-TTM-EPS reconstruction at one or more points. **Distrusted and not used** — fell back to the 06-14 session's externally-sourced 5yr avg PE (**19.22×**, GuruFocus), carried forward since a 5-year average multiple doesn't move materially over 2.5 weeks. Flagged per Rule 0's "never estimate" spirit — this is a documented fallback, not an invented number.
4. **Moat signals — sourced fresh this session** (the 06-14 session's moat commentary was qualitative-only, not individually cited per quality-scoring.md's checklist standard): see §4.

---

## 3. Quality Score — full calc

**Profitability (25%):**
```
NetMargin_Component = clamp((21.62/30)×100) = 72.1
ROIC_Component (primary, 18.66%) = clamp((18.66/30)×100) = 62.2
Profitability_Score = (72.1 + 62.2)/2 = 67.1
```
(No FCF-positivity cap — 4/4 years positive.)

**Margins (15%):**
```
GrossMargin_Score = clamp((56.0/80)×100) = 70.0
```

**Growth (20%):**
```
Growth_Score (raw) = clamp((49.0/25)×100) = clamp(196) = 100.0
```
Modifiers: documented TAM expansion (+10 — Temu international, 300M+ users/50+ countries, "Temu Global" factory-direct launch Oct 2025) *and* documented structural deceleration (−10 — revenue growth fell from +89.7% (FY22→23) to +59.0% (FY23→24) to +9.6% (FY24→25), confirmed continuing at +11% YoY in Q1 2026; this is a multi-year trend, not one quarter, so it's structural not cyclical). **Both apply, netting to 0 — but it's moot either way**, since raw Growth_Score is already clamped at the 100.0 ceiling (49% CAGR is ~2× the formula's 25% cap) before any modifier. Worth flagging as a formula quirk: **a name with real, well-documented decelerating growth still can't lose Growth Score credit once its trailing CAGR is far enough above the 25% ceiling** — the modifier has no headroom to bite. `Growth_Score = 100.0`.

**Balance Sheet (15%):**
```
Net Debt = ¥5.12B − ¥436.07B = −¥430.95B (deep net cash)
NetDebt/EBITDA ≈ −4.44×  (EBITDA TTM ≈ ¥97.16B, `yfinance`)
BalanceSheet_Score = clamp(100×(1−(−4.44)/4)) = clamp(211.1) = 100.0
```

**Moat Signal (15%) — cited evidence:**

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | 900M+ annual active buyers in China (largest e-commerce platform by buyer count, up from 19% share in 2023 vs. 7.2% in 2019); Temu 300M+ registered users across 50+ countries (Statista/Business of Apps aggregation) |
| Brand premium | FALSE | Business model is explicitly discount/low-price positioning — no pricing-power evidence exists or would fit the thesis |
| Network effect | **TRUE** | Group-buying mechanic: users recruit others via social platforms (WeChat) to unlock discounts — a documented Reed's-law-style group-forming network effect, distinct from a simple two-sided marketplace |
| Switching costs | FALSE | No documented lock-in mechanism found — e-commerce marketplace switching is generally low-friction |
| Scale cost advantage | **TRUE** | C2M (consumer-to-manufacturer) direct-factory-sourcing model, documented to eliminate distribution/inventory intermediary layers versus traditional retail — a real, cited structural cost advantage, not just a claim |

```
Moat_Score = (3/5) × 100 = 60.0
```

**FCF Quality (10%):**
```
FCFQuality_Score = clamp(((1.116 − 0.40)/0.60)×100) = clamp(119.3) = 100.0
```

**Quality Score:**
```
Quality Score = 67.1×0.25 + 70.0×0.15 + 100.0×0.20 + 100.0×0.15 + 60.0×0.15 + 100.0×0.10
              = 16.775 + 10.50 + 20.00 + 15.00 + 9.00 + 10.00
              = 81.28 → 81.3
```

**Result: Quality Score = 81.3 — clears the 80.0+ gate, by 1.3pt.** See Gap #2 above: under the low end of the external ROE sensitivity range, this fails at 77.4. **Read this gate pass as marginal, not comfortable**, same caveat as VEEV earlier today.

---

## 4. Fast Grower (PEG) Determination — unchanged from 06-14

EPS history (USD, diluted, per-ADS): 2022 ~$3.16 → 2023 $5.80 (+83.5%) → 2024 $10.41 (+79.5%) → 2025 $9.92 (**−4.7%**) → 2026E $9.38 (**−5.5%**, revised down post-Q1-2026 miss). Two most recent years both negative — **not a Fast Grower.** PEG's 15% weight redistributed to EV/EBIT (→40%). No new data changes this determination since 06-14.

---

## 5. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test:**
```
Forward PE = $82.51 / $12.297 (yfinance consensus FY EPS) = 6.71×
EY = 1 ÷ 6.71 = 14.90%
Spread = 14.90% − 4.45% = +10.45%
```
Pass threshold: ≥+1.5%. **Result: PASS** (+10.45%, far above) → no additive.

**Step 2 — Rate Regime Modifier:** 10Y = 4.45% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for PDD = +5**

---

## 6. Phase 02 — Valuation Score, full calc

| Metric | Value |
|---|---|
| Market Cap | $117.44B |
| Net Cash | $63.47B |
| Enterprise Value | $53.98B |
| EV/EBIT | **3.79×** |
| FCF Yield | **13.38%** |
| Forward PE | **6.71×** |
| 5yr avg PE (fallback, external — see Gap #3) | **19.22×** |

**FCF Yield — 40% weight:**
```
FCF_Score = clamp(100×(1 − 13.38/10)) = clamp(−33.8) = 0.0
```
→ 0.0 × 0.40 = **0.0**

**EV/EBIT — 40% weight (PEG redistributed here):**
```
EV/EBIT_Score = clamp((3.79 − 12)/23 × 100) = clamp(−35.7) = 0.0
```
→ 0.0 × 0.40 = **0.0**

**Forward PE (fallback formula, 5yr avg only) — 20% weight:**
```
Deviation% = (6.71 − 19.22)/19.22 × 100 = −65.1%
FwdPE_Score = clamp(50 + (−65.1×2.5)) = clamp(−112.7) = 0.0
```
(Fallback formula already folds in the Historical PE Modifier — no separate ±10.)
→ 0.0 × 0.20 = **0.0**

**Raw weighted score = 0.0** (all three sub-scores independently clamp to the floor — same as 06-14. EV/EBIT of 3.79× values PDD's entire *operating* business, after backing out $63.5B net cash from a $117.4B market cap, at under 4× a >20%-net-margin business still growing revenue double-digits.)

**+ Rate Modifier (+5) = 5.0** (pre-Upside/Downside Modifier)

---

## 7. Upside/Downside Modifier — full calc

**Step 1 — Fair Value (Blended).** Base FCF: TTM $15.72B. Net cash $63.47B. Shares 1.4234B.

*Method A — DCF (3-stage, 3 scenarios, Rule 2/7). Deliberately conservative growth assumptions — NOT PDD's historical ~49% hyper-growth rate:*

| Scenario | WACC | Yrs1–5 FCF growth | Yrs6–10 fade | Terminal | TV weight | **FV/share** |
|---|---|---|---|---|---|---|
| **Bear** (Temu-subsidy drag + EU/China regulatory overhang persists, FCF keeps shrinking) | 12% | −5.0% | −2.0%→2.0% | 2.0% | 35.2% | **$124.37** |
| **Base** (near-flat FCF as first-party-brand reinvestment offsets underlying growth) | 11% | +2.0% | 2.0%→2.5% | 2.5% | 44.7% | **$174.02** |
| **Bull** (Temu/New-Pinmu investment phase matures, margins recover) | 10% | +8.0% | 6.0%→3.0% | 3.0% | 54.4% | **$255.51** |

```
PW DCF FV = 0.25×255.51 + 0.50×174.02 + 0.25×124.37 = $181.98
```
Consistent with the 06-14 session's $184.21 (fresh TTM base is slightly higher, offset by a slightly larger net-cash figure — directionally the same conclusion). **Even the Bear case ($124.37) sits ~51% above live price ($82.51)** — same finding as 06-14, unchanged by 2.5 weeks of data.

*Method B — Comparable Multiples (conservative reversion multiples, well below PDD's own historical richer multiples):*

| Approach | Fair multiple | FV/share |
|---|---|---|
| EV/EBIT reversion | 8× × EBIT $14.22B, + net cash | $124.51 |
| Forward PE reversion | 12.5× × $12.297 | $153.72 |
| FCF-yield reversion | 8% yield on FCF $15.72B | $138.05 |
| **Multiples avg** | | **$138.76** |

**Triangulation:**
```
Blended FV = 0.40 × $181.98 + 0.60 × $138.76 = $156.05
```
Gap Upside% = ($156.05 / $82.51) − 1 = **+89.1%**

**Step 2 — Expected annual return `E`:**

Catalyst: Q2 2026 earnings (~Aug 2026, ~2 months out) is the nearest dated event that would confirm whether the margin-recovery thesis (first-party-brand/New-Pinmu reinvestment starting to show through) is on track — within the 18–24mo Rule 10 window, so **no guardrail cap applied this time** (unlike VEEV earlier today, where the nearest catalyst ran past 24mo). That said, fully closing an 89% gap plausibly needs several quarters of confirming prints, not one — flagged as a real judgment call, see the sensitivity note below.
```
Annualized gap (2yr default, no narrower single-event window) = 89.1% / 2 = 44.6%
Intrinsic growth = 10.0%  (most recent quarterly revenue growth, Q1 2026 — used over the 49% trailing
   3yr CAGR, which reflects PDD's now-decelerated-away hyper-growth phase, not a sustainable forward rate)
Shareholder yield = 0%  (no dividend; no documented net-buyback program found)

E = 44.6% + 10.0% + 0% = +54.6%
```
```
M (uncapped, E ≥ H=10%) = −15 × clamp((54.6−10)/15, 0, 1) = −15 × 1.0 = −15.0  (full cap — E far exceeds the 25%/yr full-credit threshold)
```
**Sensitivity flag:** if the Rule 10 guardrail were applied anyway (treating "several quarters of confirming earnings" as not a crisp enough single catalyst — the same call made for VEEV), M would cap at −5.0 instead. **It doesn't matter for the final score either way** — see §8: raw (0.0) + Rate (+5) is only 5.0 before this modifier, so both −15.0 and −5.0 push it below the 0.0 floor and it clamps there regardless. Flagged for honesty about the calc, not because it changes the outcome here.

---

## 8. Final Valuation Score & Composite Score

```
Final Valuation Score = 0.0 (raw) + 5 (Rate Modifier) − 15.0 (Upside/Downside Modifier, uncapped)
                       = clamp(−10.0, 0, 100) = 0.0
```

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 81.3) + 0.50 × 0.0
                = 9.35 + 0 = 9.35 → 9.4  (.X5 boundary rounds up, per the score rounding rule)
```

**Composite Score = 9.4 → Action Table band 0.0–29.9 → BUY — Full position 6–8%.**

Unlike VEEV's 29.7 (a boundary case), **9.4 sits deep inside the Very Cheap band** — the gate itself (Gap #2, Quality Score 81.3) is the fragile part of this result, not the composite banding. If the gate passes at all, the valuation side of this call is not close to the line.

---

## 9. Order Setup (BUY — Full position, per Composite Score 9.4)

```
Margin of Safety = 17.5% (midpoint, Score 0.0–29.9 band)
Buy Price (ceiling)   = $156.05 × (1 − 0.175) = $128.74   → live $82.51 is far below → ENTER NOW
Primary Sell Target   = Blended FV = $156.05
Bull-Case Trim Target = Bull DCF $255.51 × 0.90 = $229.96
Stop Loss             = $82.51 × (1 − 0.225) = $63.95   (22.5% max loss, midpoint 20–25% band)
R/R = ($156.05 − $82.51) ÷ ($82.51 − $63.95) = $73.54 ÷ $18.56 = 3.96 : 1   (≥ 2:1 ✓, comfortable)
```

**Position sizing** (using the operating brief's flat 1.5% risk-per-trade rule as primary; fair-value-methodology.md's per-band table separately allows "up to 2%" for this score band — flagged as a minor doc inconsistency, not resolved here, 1.5% used for consistency with today's VEEV session):
```
Portfolio Value (combined, holdings.md) = $54,891.48
Max $ Risk (1.5%) = $823.37 ; Risk/share = $18.56 → risk-based size = 44.35 sh ($3,659.45 = 6.67% of portfolio)
6–8% allocation cap = $3,293.49–$4,391.32 → risk-based size falls inside the cap band, governs directly
```
*(At the fair-value-methodology.md's "up to 2%" alternative: 59.15 sh / $4,880 = 8.89%, which would exceed the 8% cap and get capped down to ~53 sh / $4,391 = 8.00% — the 06-14 session used this 2% convention. Either convention keeps the position well under the 15% hard cap either way.)*

### Order Setup Checklist
```
[x] Valuation Score (incl. Upside/Downside Mod): 0.0
[x] Composite Score (Quality 81.3 + Valuation 0.0): 9.4   (≤ 29.9 ✓, deep in-band — see §8)
[x] Expected annual return E / catalyst window:  +54.6% / 2yr (Q2 2026 earnings ~Aug as nearest dated signal)
[x] Upside/Downside Modifier applied:            −15.0 (uncapped; −5.0 alternative doesn't change final score)
[x] DCF Fair Value (PW):                         $181.98
[x] Multiples-Based Fair Value:                  $138.76
[x] Blended Fair Value:                          $156.05
[x] Margin of Safety %:                          17.5%
[x] BUY PRICE:                                   $128.74  (live $82.51 already below — enter now)
[x] PRIMARY SELL TARGET:                         $156.05
[x] BULL-CASE TRIM TARGET:                        $229.96
[x] STOP LOSS:                                   $63.95
[x] Risk/Reward Ratio:                           3.96:1  (≥ 2:1, comfortable)
[x] Max $ Risk (1.5%):                           $823.37
[x] POSITION SIZE (shares):                      ~44 (fresh entry, no existing PDD position)
[x] POSITION SIZE ($):                           $3,659.45 (6.67% of portfolio)
[x] Thesis invalidation triggers:                margin trajectory fails to stabilize over 2+ more quarters
    (Phase 04 Quality Watch); confirmed US/EU tariff or de-minimis policy change materially impairing Temu's
    cross-border model (Phase 06 growth-thesis-broken); net-cash position impaired/trapped/redirected into
    value-destructive uses; ROIC (any reasonable reading) falls durably below WACC (~11%); stock falls
    to/through the $63.95 stop
```

---

## 10. Recommendation

**BUY — Full new position, ~44 shares (~$3,659, ~6.67% of portfolio), entered at the live price ($82.51) since it already sits far below the buy-price ceiling ($128.74).**

**Why this clears the bar, with the caveats made explicit:**

1. **The valuation gap is, if anything, even more extreme than the 06-14 read** — all three sub-scores independently clamp to the floor again, EV/EBIT (3.79×) is essentially unchanged from 06-14's 3.87×, and the Blended FV ($156.05) implies +89% upside, up from +81% previously (net cash and TTM cash generation both grew faster than the stock price over the 2.5 weeks).
2. **The Quality Score gate is the fragile part of this call, not the valuation side** (Gap #2) — a defensible-but-not-certain ROIC treatment is the difference between Quality 81.3 (passes) and 77.4 (fails, no Composite Score at all, this session stops). The framework's own precedent (06-14's equity-heavy-structure exception, applied to the *old* Phase 01 binary gate) supports treating this generously, but it's flagged with the same weight as VEEV's equivalent issue earlier today — **this is not a comfortable pass.**
3. **R/R (3.96:1) and MoS (effective ~47% vs. the 15–20% required band) are both comfortably past their minimums** — materially stronger risk-adjusted setup than VEEV's 2.16:1 today.
4. **New, incremental information since 06-14 (the €200M EU Temu fine) doesn't change the picture** — small relative to PDD's scale, already reflected in a stock that's up modestly (not down) since that session.
5. **Unchanged since 06-14:** not a Fast Grower (declining recent EPS), Rate Gate favorable, thesis-invalidation triggers unchanged.

**Net: this reads as a stronger valuation case than VEEV's marginal 29.7 today, but a comparably fragile quality gate.** The human investor should weigh Gap #2 specifically before sizing — if the lower ROIC reading is the "true" one, this position shouldn't be entered under this framework's own rules at all.

---

## 11. Next Review Trigger

- **Q2 2026 earnings** (~Aug 2026) — mandatory Rule 9 re-score; specifically check whether margin trajectory has stabilized and whether the EU DSA fine triggers any follow-on EU regulatory action (the DSA allows fines up to 6% of global revenue — this one was far below that ceiling, but the precedent matters).
- Any confirmed US/EU tariff or de-minimis policy change targeting low-value China-direct e-commerce shipments (Rule 9).
- >15% unexplained price move from $82.51 in either direction (Rule 9) — already demonstrated today (+8.17% intraday).
- **If entered**, add to `portfolio/holdings.md` (Last Score 0.0 / Quality Score 81.3 / Composite Score 9.4 / Last Review 01 Jul 2026) at the next `/sync-portfolio` pass, and move the watchlist entry from `not-in-portfolio/` to `in-portfolio/`.

---

## Sources (WebSearch, per tool requirements)

- [USD to CNY Exchange Rate — exchangerates.org.uk](https://www.exchangerates.org.uk/USD-CNY-spot-exchange-rates-history-2026.html)
- [Why PDD Holdings Stock Is Surging Right Now — TipRanks](https://www.tipranks.com/news/catalyst/why-pdd-holdings-stock-is-surging-right-now)
- [PDD Holdings (PDD) Stock Flagged as Tactical Buy Following China Regulatory Fine — Parameter](https://parameter.io/pdd-holdings-pdd-stock-flagged-as-tactical-buy-following-china-regulatory-fine/)
- [Commission fines Temu €200 million for breaching the Digital Services Act — European Commission](https://digital-strategy.ec.europa.eu/en/news/commission-fines-temu-eu200-million-breaching-digital-services-act)
- [Pinduoduo and The Rise of Social E-Commerce — anuhariharan.substack.com](https://anuhariharan.substack.com/p/pinduoduo-and-the-rise-of-social)
- [Pinduoduo — statistics & facts — Statista](https://www.statista.com/topics/7462/pinduoduo/)
- [Temu Revenue and Usage Statistics — Business of Apps](https://www.businessofapps.com/data/temu-statistics/)

---

## Glossary

- **C2M (Consumer-to-Manufacturer)** — a business model that connects buyers directly with factories/manufacturers, skipping traditional distribution/inventory intermediaries — the basis of PDD's cost-advantage moat signal. *(New — added to [glossary.md](../framework/glossary.md) this session.)*
- **CAGR, DCF, EBIT/EBITDA, EV/EBIT, EY, Fast Grower, FCF/FCF Yield/FCF-NI ratio, Forward PE, FV, Hard disqualifier, Moat, MoS, Net Debt/EBITDA, NOPAT, PEG, PT, PW Fair Value, Quality Score, Rate Environment Gate/Rate Regime Modifier, R/R, ROIC, Rule 0/9/10, Shareholder yield, TAM, TTM, Upside/Downside Modifier, WACC** — see [glossary.md](../framework/glossary.md) (all cited in today's VEEV session too).
- **DSA (Digital Services Act)** — an EU regulation requiring online platforms to police illegal/unsafe content and products, with fines up to 6% of global annual revenue for breaches — the basis of Temu's €200M May 2026 fine. *(New — added to [glossary.md](../framework/glossary.md) this session.)*
- **Group buying (social commerce)** — an e-commerce model where buyers form a group (often via social-media sharing) to unlock a lower per-unit price once a minimum number join — Pinduoduo's core viral-growth/network-effect mechanic. *(New — added to [glossary.md](../framework/glossary.md) this session.)*

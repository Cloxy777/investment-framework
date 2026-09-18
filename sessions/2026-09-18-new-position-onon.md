# New Position Evaluation — ONON (On Holding AG, NYSE)

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6)
**Date:** 18 Sep 2026
**10Y US Treasury Yield:** 5.004% (WebSearch cross-check of multiple financial-news sources — Treasury yields "climbed back above the 5% level, rising more than 5bp at 5.004% on Friday, September 18, 2026"; consistent with the week's reported 5.00–5.04% range after the FOMC's first hike in 3 years)
**Rate Regime Modifier (active):** +10 (>5% bracket)
**Current ONON portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. No `watchlist/in-portfolio/ONON/` or `watchlist/not-in-portfolio/ONON/` folder existed before this session — first-ever `/new-position` or `/rescore` pass on ONON in this repo. Not applicable to [watchlist/STALE.md](../watchlist/STALE.md) (no prior score exists to go stale).
**Sector:** Consumer Discretionary — Premium Athletic Footwear & Apparel (Swiss, NYSE-listed foreign private issuer, files Form 20-F annually, not a 10-K)
**First-use jargon:** none new — all terms used below already exist in [glossary.md](../framework/glossary.md) (checked before writing).

---

## 0. Trigger — why this session exists, and why the post is not used as data

**FinnInvestChannel**, post `#3238` (2026-09-18 18:49 UTC, Ukrainian):

> "💡 Kylian Mbappé йде від Nike і переходить до On Holding ✅ Mbappé співпрацював з Nike ще з 2006 року, але тепер підписав угоду зі швейцарським брендом On ✅ On планує випустити свої перші футбольні бутси вже у 2027 році ✅ Mbappé стане глобальним амбасадором бренду і допомагатиме розробляти футбольне взуття та одяг ✅ Угода включає не лише гроші, а й частку в On"

(Translation: Kylian Mbappé is leaving Nike for Swiss brand On Holding; the deal — which includes an equity stake for Mbappé — makes him a global ambassador who will help develop football boots/apparel, with On's first football boots planned for 2027.)

Per CLAUDE.md Rule 0 and the operating brief, this post is a **trigger only**, never a financial-data source. It names ONON unambiguously. **Decision to trigger this session:** neither `watchlist/in-portfolio/ONON/` nor `watchlist/not-in-portfolio/ONON/` existed, and ONON is not in [holdings.md](../portfolio/holdings.md). Per `/telegram-scan` step 4's first rule — "No watchlist entry exists at all → `/new-position <TICKER>`" — this triggers a full evaluation regardless of whether the sponsorship-deal post itself would independently qualify as a Rule 9 fundamental event. It would not: Rule 9's list is earnings/guidance revision/management change/M&A/macro shift/>15% unexplained move, and a celebrity-endorsement switch is not on that list. No dollar figures, deal term, or financial impact are disclosed in the post or in On's own newsroom as of this session, so the deal is treated below only as qualitative color on the Moat/Growth discussion (§2, §7) — never as a scored financial input.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$27.32** | IBKR `get_price_snapshot` (contract_id **513880603**, NYSE, "ON HOLDING AG-CLASS A"), `last` field, fetched 2026-09-18 (`is_close: false`, `halted: false`) |
| Cross-check | **$27.25** (close), prior close **$27.33** | stockanalysis.com, "as of September 18, 2026, at market close" — within 7¢ of the IBKR intraday print, consistent |
| Bid / Ask | $27.30 (500) / $27.44 (1,000) | IBKR `get_price_snapshot` |
| Change | −$0.01 / −0.04% (IBKR); −$0.08 / −0.29% (stockanalysis, close vs. prior close) | Both sources |
| 52-week range | Low **$26.37** (also the 13w and 26w low) · High $51.05 · Open (52w ago) $44.41 | IBKR `misc_statistics` |
| YTD change | **−41.22%** | IBKR `get_price_snapshot` |
| Market cap | ≈ $9.11B | stockanalysis.com |
| Shares outstanding | 334.21M | stockanalysis.com balance sheet / statistics |
| US 10Y Treasury yield | 5.004% | See header |

I used the **IBKR $27.32** print as the price of record throughout (Rule 0), cross-checked against stockanalysis.com's independently-sourced $27.25 close — the two agree to within 0.3%, no red flags. The stock sits essentially at its 52-week low, roughly 6 weeks after an August 2026 post-earnings selloff (see §5).

---

## 2. Quality Score — Phase 01 (methodology version 2026-06-29)

All financial data fetched fresh this session, primarily via stockanalysis.com's financial-statement pages (income statement, balance sheet, cash-flow, ratios/statistics), cross-checked internally (e.g. Net Debt/EBITDA independently recomputed from balance-sheet lines ties to the site's own stated ratio). ONON is a Swiss foreign private issuer — files Form 20-F, not a 10-K.

### 2.1 Hard disqualifiers (checked first)

| Disqualifier | Test window | Result |
|---|---|---|
| Not FCF-positive for 3+ consecutive years | FY2023 CHF 189.3M, FY2024 CHF 450.1M, FY2025 CHF 286.6M — all positive (rolling window per the 2026-08-05 clarification, most recent 3 completed fiscal years) | **Does not fire.** (FY2022 was negative, −CHF 287.3M, but falls outside the current rolling window.) |
| Net Debt/EBITDA over threshold (2.5× standard) | Net Debt (Q2 2026, most recent quarter): Total Debt CHF 562.5M − (Cash CHF 1,206M + ST Investments CHF 33.8M) = **−CHF 677.3M** (net cash) ÷ TTM EBITDA (≈CHF 485.8M, back-solved from stockanalysis's own stated EV/EBITDA 13.79× and EV ≈$8.27B) → Net Debt/EBITDA **≈ −1.38×** (stockanalysis.com's own directly-stated ratio, matches independent back-solve) | **Does not fire** — well under 2.5×, and unlike a negative-EBITDA edge case, EBITDA here is genuinely positive, so the negative ratio is a real, meaningful "net cash, low leverage" read, not a formula artifact. |
| FCF/NI conversion <70% for 2+ years w/o growth-capex explanation | TTM: FCF CHF 437.9M ÷ NI CHF 396.2M = 110.5%; FY2025: 286.6/203.7 = 140.7%; FY2024: 450.1/242.3 = 185.8% | **Does not fire** — ratio well above 70% every year shown. |

**No hard disqualifier fires.** Proceed to the weighted score.

### 2.2 Sub-score computation

**Profitability (25%)**
```
Net Margin (TTM) = 396.2 / 3,220 = 12.30%        (stockanalysis.com income statement)
ROIC (TTM)        = 32.30%                         (stockanalysis.com statistics page)
NetMargin_Component = clamp((12.30/30)×100) = 41.0
ROIC_Component       = clamp((32.30/30)×100) = 107.7 → capped 100.0
Profitability_Score  = (41.0 + 100.0) / 2 = 70.5     (no FCF cap — 3yr positive, see §2.1)
```

**Margins (15%)**
```
Gross Margin TTM = 64.82%   (trend: FY2022 56.04% → FY2023 59.56% → FY2024 60.63% → FY2025 62.83% → TTM 64.82% — steadily expanding)
GrossMargin_Score = clamp((64.82/80)×100) = 81.0     (already >40% — no below-40%-expansion bonus applicable)
```

**Growth (20%)**
```
Revenue 3yr CAGR = (FY2025 / FY2022)^(1/3) − 1 = (3,014 / 1,222)^(1/3) − 1 = 35.1%
  (stockanalysis.com income statement: FY2022 CHF 1,222M → FY2025 CHF 3,014M)
Growth_Score base = clamp((35.1/25)×100) = 140.4 → capped 100.0
Documented TAM-expansion/pricing-power evidence (moot — already capped, shown for audit trail):
  market-share gains in running footwear (YipitData, "Footwear Market Trends 2026" — On gained share
  alongside Hoka/New Balance/Adidas while Nike lost share; On "maintained lower discount rates... while
  gaining share"), DTC mix rising to 45.7% of sales (Q2 2026 release), and the new football-boot category
  entry (2027 launch, this session's trigger event) — a genuine new-TAM vector, though too early/undisclosed
  to be a scored financial input today.
Growth_Score = 100.0
```

**Balance Sheet (15%)**
```
BalanceSheet_Score = clamp(100×(1 − (−1.38)/4)) = 100×1.345 = 134.5 → capped 100.0
```

**Moat Signal (15%)** — checklist, cited evidence required per signal:

| Signal | Verdict | Evidence (cited) |
|---|---|---|
| Market share stable/growing | **TRUE** | YipitData "Footwear Market Trends 2026": "On gained market share in the running segment alongside Hoka, New Balance, and Adidas, while Nike lost share across both channels." |
| Brand premium / pricing power | **TRUE** | Same source: On "maintained lower discount rates relative to peers and sustained premium pricing while gaining share" — price increases/discipline without share loss. Corroborated by TTM gross margin of 64.82%, well above mass-market footwear norms, and proprietary CloudTec® cushioning technology underpinning the premium positioning. |
| Network effect | **FALSE** | No two-sided marketplace or user-growth-driven mechanism documented for a footwear/apparel retailer of this kind. |
| Switching costs | **FALSE** | No documented lock-in mechanism — footwear purchases carry no meaningful switching cost. |
| Scale cost advantage | **FALSE** | No cost-per-unit data found showing an advantage vs. larger incumbents (Nike, Adidas); On is smaller-scale than both. |

```
Moat_Score = (2/5) × 100 = 40.0
```

**FCF Quality (10%)**
```
FCFQuality_Score = clamp(((1.105 − 0.40)/0.60)×100) = clamp(117.5) → capped 100.0
```

### 2.3 Final Quality Score

```
Quality Score = 70.5×0.25 + 81.0×0.15 + 100.0×0.20 + 100.0×0.15 + 40.0×0.15 + 100.0×0.10
              = 17.625 + 12.150 + 20.000 + 15.000 + 6.000 + 10.000
              = 80.775 → rounds to 80.8
```

**Quality Score = 80.8 / 100.0 — clears the 80.0+ gate**, though narrowly. The gate is passed almost entirely on strong profitability/growth/balance-sheet/FCF-quality sub-scores (all capped at or near 100.0); the weak link is the Moat Signal (2 of 5, 40.0) — On has real, evidenced pricing power and share gains, but no network effect, switching cost, or scale advantage yet. Proceed to Phase 02.

---

## 3. Rate Environment Gate

- **Step 1 — Earnings Yield Spread Test:** EY = 1 ÷ Forward PE = 1 ÷ 15.11 = **6.62%**. Spread = 6.62% − 5.004% = **+1.61pp** — at/above the +1.5pp threshold → **no additive flag.**
- **Step 2 — Rate Regime Modifier:** 10Y yield 5.004% is in the >5% bracket → **+10.**

**Total Rate Environment Gate modifier: +10**

---

## 4. Phase 02 — Valuation Score

### PEG / Fast Grower eligibility — not applicable

Quarterly reported EPS (yfinance `get_earnings_dates`, 2021-2026) is lumpy and includes three negative quarters (2022-03, 2024-03, 2025-08); reconstructed TTM EPS grew from $0.21 (Aug 2022) to $1.40 (Aug 2026) — a >6.5× swing driven by a company scaling up from a near-zero post-IPO earnings base (IPO Sept 2021), not steady >15%/yr compounding on a reliable base. Per the 2026-06-20 clean-earnings clarification ("recent IPO... does not yet qualify"), **PEG is not applicable — its 15% weight is redistributed to EV/EBIT (→ 40%).**

### FCF Yield (40% weight)
```
FCF Yield (TTM) = 5.78%   (stockanalysis.com ratios page; independently consistent with
                            TTM FCF CHF 437.9M ÷ Market Cap, converted at spot FX)
FCF_Score = clamp(100×(1 − 5.78/10)) = 42.2
```

### EV/EBIT (40% weight, PEG-redistributed)
```
EV/EBIT = 15.25×   (stockanalysis.com ratios page)
EV/EBIT_Score = clamp((15.25 − 12)/23 × 100) = 14.1
```

### Forward PE (20% weight) — no-history fallback

Forward PE = **15.11×** (stockanalysis.com). A trailing 5-year PE range/average was tested via `yfinance`'s quarterly `get_earnings_dates` (TTM-EPS reconstruction methodology): of 20 quarterly TTM-EPS points since 2022, 17 had positive TTM EPS, giving PE readings ranging from **114.62× down to 22.15×** as TTM EPS scaled ~6.5× from a near-zero post-IPO base — not a case of genuine multiple mean-reversion, but of an earnings base normalizing from close to zero. Independent third-party providers corroborate this is not a usable anchor: reported "5-year average PE" figures range from 114× to 126× depending on provider/date, and the reported 10-year mean PE is **−1,021** (reflecting extended loss-making periods). This is exactly the framework's **"GAAP earnings base too distorted to be meaningful"** case.
```
FwdPE_Score = 50.0 (neutral, flagged — no-history fallback)
```

### Raw weighted score
```
Raw Score = FCF_Score×0.40 + EV/EBIT_Score×0.40 + FwdPE_Score×0.20
          = 42.2×0.40 + 14.1×0.40 + 50.0×0.20
          = 16.88 + 5.64 + 10.00
          = 32.53
```

### Upside/Downside Modifier

**Fair Value work (Step 1, fair-value-methodology.md) — DCF + comparable multiples, 3 scenarios, 40%/60% blend, all figures in CHF unless noted, converted to USD at spot FX (1 USD = 0.81 CHF, WebSearch cross-check, mid-September 2026):**

*DCF — WACC via CAPM (flagged as analyst judgment, not fetched data, per repo precedent):*
```
Cost of equity = Rf + Beta × ERP = 5.004% + 2.10 × 5.0% = 15.50%
  (Beta 2.10: WebSearch cross-check, multiple providers converge 1.42–2.12, most cluster 2.09–2.12,
   consistent with ONON's own documented volatility — 52wk range $26.37–$51.05, −41.2% YTD, a
   ~19–22% single-day drop on the Aug 2026 earnings miss)
Weights: Equity $9,110M / (Equity $9,110M + Debt $694.2M[CHF 562.5M @ spot FX]) = 92.9% equity / 7.1% debt
After-tax cost of debt ≈ 4.0% × (1 − 22%) = 3.12%
WACC (base) = 92.9%×15.50% + 7.1%×3.12% = 14.6%   (Bull 13.6%, Bear 15.6%, per Rule 2's ±1% instruction)
```

3-stage structure not required — Stage-1-only (Years 1–5) terminal value weight stays under Rule 4's 75% cap in every scenario (Base 65.6%, Bull 68.0%, Bear 61.3% — computed below), so no extension to a 10-year model was needed.

| Scenario | WACC | Revenue growth (Y1→Y5) | FCF margin (Y1→Y5) | Terminal g | DCF FV/share |
|---|---|---|---|---|---|
| Bull | 13.6% | 20%→17%→15%→13%→11% (base ×1.15 on FCF) | scaled with revenue | 3.0% | **$31.22** |
| Base | 14.6% | 18%→15%→13%→11%→9% | 12%→13%→14%→15%→16% | 3.0% | **$25.13** |
| Bear | 15.6% | base ×0.85 on FCF | scaled with revenue | 2.0% | **$19.15** |

(Base case: FCF Y1 CHF 426.8M → Y5 CHF 894.7M off FY2025's CHF 3,014M revenue base; PV of Stage-1 FCF CHF 2,105.9M + PV of Terminal Value CHF 4,018.5M = EV CHF 6,124.4M; + net cash CHF 677.3M = Equity CHF 6,801.7M ÷ 334.21M shares = CHF 20.35/share × spot FX = $25.13.)

*Comparable multiples — forward PE, current sector peers (all "have plunged" through 2026, per contemporaneous coverage):*

| Peer | Forward PE |
|---|---|
| Nike (NKE) | 23.7× |
| Adidas (ADDYY) | 15.3× |
| Deckers (DECK) | ~12.5× |
| Lululemon (LULU) | ~12.5× |
| **Peer median (ex-ONON)** | **13.9×** |

NTM EPS used: **$1.80**, back-solved from stockanalysis.com's own stated Forward PE (15.11×) against the $27.25 close — used for internal consistency with the Forward PE figure already scored above, rather than the site's separately-listed "FY2026 EPS $1.42" forecast, which is flagged as internally inconsistent (its paired "FY2026 revenue $3.51B" forecast sits *below* TTM revenue of ~$3.98B-equivalent, suggesting a stale/differently-scoped estimate — not used).

| Scenario | Multiple | Multiples FV/share |
|---|---|---|
| Bull | 20.0× (partial re-rating toward Nike) | **$36.00** |
| Base | 13.9× (peer median) | **$25.02** |
| Bear | 11.0× (peer low, DECK/LULU) | **$19.80** |

**Triangulation (40% DCF + 60% Multiples):**
```
Bull FV = 0.40×31.22 + 0.60×36.00 = $34.09
Base FV = 0.40×25.13 + 0.60×25.02 = $25.06
Bear FV = 0.40×19.15 + 0.60×19.80 = $19.54

PW Fair Value = 0.25×34.09 + 0.50×25.06 + 0.25×19.54 = $25.94
```

**Sanity check (Rule 4) against sell-side analyst consensus:** analyst average price target is materially higher, **$43.08** (31 analysts, stockanalysis.com; range across providers $43–$64 average, high $72.66). This is a real, flagged divergence — my Bull case ($34.09) sits below even the Street *average*. The gap is attributable to (a) a genuinely high, CAPM-derived WACC driven by ONON's own well-documented beta (~2.1), which sell-side models likely do not weight as heavily, and (b) using *current*, already-compressed 2026 peer multiples (the whole premium-footwear group has de-rated this year) rather than a re-rating assumption. Shown transparently rather than silently reconciled — this is a legitimate output of the framework's own explicit CAPM/current-multiples methodology, not an error.

**Step 1 — Expected annual return E:**
```
Gap Upside % = (PW FV ÷ Live Price) − 1 = (25.94 / 27.32) − 1 = −5.05%
Catalyst window = 2yr (default — see catalyst note below)
Annualized gap = −5.05% / 2 = −2.53%
Intrinsic growth = 20.3% (base-case FCF CAGR, Y1→Y5: (894.7/426.8)^(1/4) − 1 = 20.3%)
Shareholder yield = −1.9% (no dividend; shares outstanding grew 331.0M FY2025 → 334.21M TTM,
  +0.97% over ~2 quarters, annualized ≈ +1.9% dilution)
E = −2.53% + 20.3% − 1.9% = 15.9%
```

**Catalyst:** management has announced a Zurich Investor Day to outline its vision through 2030 (date not yet confirmed); nearer-term, continued DTC-mix execution (45.7% of Q2 2026 sales, +34.3% cc) and the upcoming Q3 2026 earnings report are dated, real catalysts within the 18–24mo window, so the upside-side guardrail cap does not apply. The football-category launch (2027, this session's trigger event) falls just outside a tight 18–24mo window and is not credited here.

**Step 2 — Map E to modifier (H = 10%):**
```
E (15.9%) ≥ H (10%) → M = −15 × clamp((15.9 − 10)/15, 0, 1) = −15 × 0.393 = −5.9
```

### Final Valuation Score
```
Final Score = Raw Score + Rate Environment Gate + Upside/Downside Modifier
            = 32.53 + 10.00 + (−5.9)
            = 36.63 → rounds to 36.6
```

**Valuation Score = 36.6 / 100.0** (30.0–49.9 band = "Cheap" per the raw-score Action Table)

---

## 5. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 80.8) + 0.50 × 36.6
                = 0.50 × 19.2 + 0.50 × 36.6
                = 9.6 + 18.3
                = 27.9
```

**Composite Score = 27.9 / 100.0 — nominally "Very Cheap" (0.0–29.9 band)**, which would map to Full Position (6–8%) / "Enter now" per the Phase 03 table read on the score alone. **§6 shows this doesn't survive the concrete Buy-Price / Risk-Reward gate.**

---

## 6. Fair value & order setup

> **Result up front: the R/R gate blocks entry at any authorized price, and live price already sits slightly above this session's own blended Fair Value — despite the attractive nominal Composite Score.**

Per fair-value-methodology.md's 0.0–29.9-band tables: MoS 15–20%, Max Acceptable Loss 20–25%. Used **MoS = 20%** (top of range) and **Max Loss = 20%** (tight end) — the most R/R-favorable combination this score band authorizes — deliberately chosen to show the *best possible* case, not to bias toward a fail.

```
[x] Composite Score (incl. Quality blend):        27.9  (Very Cheap band, 0.0–29.9, nominal)
[x] Valuation Score (incl. Upside/Downside Mod):   36.6
[x] Expected annual return E / catalyst window:    15.9% / 2yr
[x] Upside/Downside Modifier applied:              −5.9
[x] DCF Fair Value (base case):                     $25.13
[x] Multiples-Based Fair Value (base case):          $25.02
[x] Blended Fair Value (PW, bull/base/bear):         $25.94
[x] Margin of Safety %:                              20% (top of 15–20% range)
[x] BUY PRICE (limit order):                         $20.75   (= $25.94 × 0.80)
[x] PRIMARY SELL TARGET:                              $25.94   (= Blended/PW Fair Value)
[x] BULL-CASE TRIM TARGET:                            $30.68   (= $34.09 × 0.90)
[x] STOP LOSS:                                        $16.60   (= $20.75 × 0.80, 20% max loss — tightest authorized)
[x] Risk/Reward Ratio:                                1.25:1   ← FAILS the 2:1 minimum
[x] Max $ Risk (1.5% of $61,192.89 combined portfolio): $917.89
[x] POSITION SIZE (shares, if it cleared R/R):         222.2 shares
[x] POSITION SIZE ($, if it cleared R/R):               $4,611 (≈7.53% of portfolio — within the 6–8% cap)
[x] Thesis invalidation triggers:                       see §8
```

**R/R math:**
```
R/R = (Sell Target − Entry) ÷ (Entry − Stop Loss)
    = (25.94 − 20.75) ÷ (20.75 − 16.60)
    = 5.19 ÷ 4.15
    = 1.25:1
```

**This structurally cannot reach 2:1 within this score band's authorized parameters.** As in the BKNG 2026-08-05 precedent, R/R as a function of MoS and Max-Loss% simplifies to `MoS / [(1 − MoS) × MaxLoss%]`, independent of the Fair Value level. Even at the most favorable *authorized* combination for a 0.0–29.9-Composite-Score position (MoS 20% / Max Loss 20%), R/R = 0.20/(0.80×0.20) = **1.25:1** — this is the ceiling for this band, not a result specific to ONON's particular FV number. Solving for the entry price that would clear 2:1 at the tightest 20% stop: Entry = Sell Target / 1.40 = $25.94 / 1.40 = **$18.53** — implying a **28.6% Margin of Safety**, outside the 15–20% range authorized for a non-Turnaround position (28–40% MoS is reserved for the Turnaround Sub-Gate/cyclical-trough case, which doesn't apply — ONON isn't a turnaround, it's a growth compounder trading near its 52-week low, not in balance-sheet distress).

**A second, independent reason to pass at the live price:** the live price ($27.32) already sits **above** this session's Blended/PW Fair Value ($25.94) — a −5.05% "gap," not a positive one. Buying at market here means paying above this session's own best fair-value estimate, which the order-setup math above correctly refuses to authorize (the computed Buy Price, $20.75, sits ~24% below the live price).

**Cross-check against the 15% position cap:** the reference position size above (≈7.53% of the combined $61,192.89 portfolio) is well under the 15% hard cap — not the binding constraint here.

---

## 7. Recommendation

**WATCHLIST ONLY — do not enter, despite a Composite Score (27.9) that nominally qualifies for a Full Position (6–8%).**

Two independent, mandatory gates both block entry at the current live price:
1. **Risk/Reward gate (Step 6):** the best achievable R/R within this score band's authorized MoS/stop parameters is 1.25:1 — structurally short of the 2:1 minimum, the same "cannot reach 2:1 within this band" finding as the BKNG 2026-08-05 session.
2. **Fair value gate:** the live price ($27.32) sits modestly *above*, not below, this session's own Blended Fair Value ($25.94) — this is not a "cheap and just needs a tighter stop" case; it's a case where the price hasn't yet fallen enough for the framework's own fair-value math to call it cheap.

This is a **"wait for a lower entry," not a "quality/thesis problem"** case. The Quality Score clears the 80.0+ gate (80.8/100.0) — real pricing power and share gains (YipitData-cited), strong ROIC (32.3%), strong FCF conversion (110%+), a fast-growing top line (35% 3yr revenue CAGR), and a genuinely improving margin trajectory (gross margin up every year since FY2022). The gate is narrowly cleared specifically because the Moat Signal is weak (2/5 — no network effect, switching cost, or scale advantage yet), which is also the framework's honest read of *why* this isn't (yet) an exceptional, wide-moat compounder like BKNG.

**Action:** set a price alert at **≤$18.53** (the level at which 2:1 R/R clears using the tightest authorized stop) or revisit on the next Rule 9 trigger — most likely ONON's Q3 2026 earnings release (based on the historical quarterly cadence observed in this session's `yfinance` earnings-date pull, roughly mid-November), the announced-but-undated Zurich Investor Day, or a guidance revision. The Mbappé/football-boot deal that triggered this session (§0) is a genuine, real brand-building development, but discloses no financial terms and is not itself a re-valuation trigger — revisit once/if the football-category launch (2027) produces disclosed revenue or margin data.

**No position opened. Nothing logged in `decisions/` or `portfolio/holdings.md`.**

---

## 8. Qualitative notes (5 questions + disruption vector check)

1. **Why are margins high?** Premium pricing sustained through disciplined DTC/wholesale channel management (lower discount rates than peers per YipitData) and proprietary CloudTec® cushioning technology — not a lucky cycle; gross margin has expanded every year since FY2022 (56.0% → 64.8% TTM) through an actual mix shift toward DTC (45.7% of Q2 2026 sales).
2. **What would it take to compete with them?** Proprietary cushioning IP, credible athlete/ambassador relationships, and DTC infrastructure — real but not insurmountable barriers (reflected in the Moat Score of only 2/5: no network effect, switching cost, or demonstrated scale-cost edge over Nike/Adidas).
3. **Capital allocation track record:** Growth-stage reinvestment — rising capex (CHF 42.8M FY2023 → CHF 87.5M TTM), no dividend, modest net share-count growth (~2%/yr, largely equity comp) rather than buybacks. Not yet a mature capital-return story.
4. **Growth sources next 3–5 years:** Continued DTC mix shift, geographic expansion, and — the trigger for this session — a brand-new football-boot/apparel category launching 2027 behind a marquee ambassador (Kylian Mbappé), a genuine incremental TAM vector, though undisclosed financially today.
5. **Best bear case:** ONON's extreme measured volatility (beta ~2.1, −41% YTD, a ~19–22% single-day drop on the Aug 2026 earnings miss driven by wholesale-channel softness) signals real execution/consumer-discretionary sensitivity; a further pullback or a soft Q3 print could easily reopen the 2:1 R/R entry window flagged above, but could equally reflect genuine demand softening rather than a buying opportunity — worth re-verifying fundamentals, not just price, at the next trigger.
6. **Disruption vector check:** the football-boot category is entirely new ground for On — a category historically dominated by Nike/Adidas/Puma with decades-deep athlete relationships and cleat-specific manufacturing expertise. Execution risk is real even with Mbappé's star power; success is not guaranteed and shouldn't be underwritten in the score until disclosed.

---

## 9. Next review trigger

ONON's Q3 2026 earnings release (historical cadence suggests ~mid-November 2026, per this session's `yfinance` earnings-date history — not yet company-confirmed), the announced-but-undated Zurich Investor Day (2030 targets), a >15% unexplained price move, or the price alert at ≤$18.53 flagged in §7.

---

## 10. Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used above, all already defined there: **Quality Score**, **Composite Score**, **Valuation Score**, **Hard disqualifier**, **FCF** / **FCF/NI conversion ratio**, **EBIT**, **EBITDA**, **Net Debt/EBITDA**, **Net Margin**, **Gross Margin**, **ROIC**, **CAGR**, **TTM**, **NTM**, **Moat Signal**, **Fast Grower**, **PEG**, **Rate Environment Gate** / **Rate Regime Modifier**, **Earnings Yield Spread Test**, **Upside/Downside Modifier (Expected-Return Modifier)**, **PW (Probability-Weighted) Fair Value**, **Rule 1–8, Rule 10 (10-Rule Fair Value Framework)**, **WACC**, **CAPM**, **Beta**, **Equity Risk Premium (ERP)**, **Terminal Value**, **Shareholder yield**, **Buyback yield**, **DTC (Direct-to-Consumer)**, **Form 20-F**, **52-week range**, **Margin of Safety (MoS)**, **Risk/Reward Ratio (R/R)**.

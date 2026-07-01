# RESCORE — VEEV (Veeva Systems Inc.)

**Date:** 01 Jul 2026
**10Y US Treasury Yield:** 4.45% (mid of 4.44–4.46% range reported by TradingEconomics/YCharts for 30 Jun 2026 — see Sources)
**Rate Regime Modifier (active):** +5 (3.5–5% bracket)
**Mode:** `--both` (full Quality + Valuation re-score — first-ever score for VEEV; previously "not scored" on [holdings.md](../portfolio/holdings.md))

VEEV has been held since before this framework's scoring conventions existed (3 shares, avg cost $171.36, IBKR) but had never been run through Phase 01/02. This session computes both scores from scratch.

---

## 1. Data Gaps / Flags (read before the numbers below)

1. **ROIC methodology — gate-critical judgment call.** External sources disagree wildly on VEEV's ROIC (13.9%–115.95% depending on vendor/definition — GuruFocus and Finbox pages were both inaccessible this session, 403). Rather than pick an unsourced vendor number, ROIC was computed directly from `yfinance` financials: NOPAT = EBIT(TTM) × (1 − effective tax rate) = $955.749M × (1 − 23.9%) = $727.19M. The denominator (Invested Capital) is where the disagreement lives:
   - **Cash-adjusted (used below):** Invested Capital = Total Debt + Equity − Cash&ST-Investments = $95.859M + $7,214.752M − $6,560.814M = **$749.797M** → **ROIC = 97.0%**. This nets out VEEV's large non-operating cash/investments pile ($6.56B against $7.21B total equity — the business itself carries almost no net capital), matching standard NOPAT/IC practice and consistent with how this framework already nets cash in the Balance Sheet sub-score.
   - **Unadjusted:** Invested Capital = Total Equity only = $7,214.752M (yfinance's own "Invested Capital" field, which doesn't net cash) → **ROIC = 10.1%**.
   - **This changes the Quality Score gate outcome:** cash-adjusted → **Quality Score 85.7 (passes the 80.0+ gate)**; unadjusted → **Quality Score 77.4 (fails the gate, no Composite Score, no action recommendation)**. Full parallel calc in §3. The cash-adjusted figure is used as primary because it's the standard finance convention (McKinsey/Damodaran NOPAT/IC methodology) and the closest match to the higher external estimates (21–116%), but this is flagged as the single highest-leverage judgment call in this session — reasonable people could pick the other one.
2. **Moat signals — 2 of 5 left unmarked, not because they're false, but because no citable evidence was found this session** (brand-premium pricing power, scale cost advantage). Per quality-scoring.md, a signal is only marked TRUE with a cited source — never inferred. Worth a deeper look in a future session before treating Moat_Score (60.0) as final.
3. **"Fair" comp multiples in the Multiples-Based FV (§5) are a discretionary anchor**, not a sourced figure — 25× forward PE, 22× EV/EBIT, 4.25% FCF yield, chosen as a discount to VEEV's own 5yr-avg multiples to reflect quality but decelerating growth. Reasonable analysts could pick materially different anchors; shown in full so the user can substitute their own.
4. **Upside/Downside Modifier capped at −5 (not the uncapped −15)** under the Rule 10 guardrail — see §6. VEEV's clearest growth driver (the Vault CRM migration wave) runs through 2026–2029, past the 18–24mo window the guardrail requires for full upside credit.
5. **Composite Score lands at 29.7 — just 0.3pt inside the 0.0–29.9 "Buy Full" band, and R/R clears the 2:1 floor by only 0.16:1.** This is a marginal, boundary-sitting result, not a robust one. Given Gaps #1, #3, #4 above, a modestly different (and equally defensible) set of judgment calls could easily move this into the 30.0–49.9 "Standard position" band or even back to Hold. Flagged explicitly — treat this as a marginal Buy signal, not a high-conviction one.
6. **Today's price is up +4.60% intraday** (see §2) — checked for a Rule 9 trigger; no company-specific news found (last earnings were 04 Jun 2026 / next is 02 Sept 2026, no guidance revision, M&A, or management change identified). Appears to be general market/momentum action, not a fundamental trigger — noted, not acted on, consistent with "never act on price movement alone."

---

## 2. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price** | **$185.63** | IBKR `get_price_snapshot`, contract 136254493 (NYSE) |
| Today's change | +$8.16 / +4.60% | IBKR snapshot |
| 52-week range | $148.12 – $310.24 | IBKR snapshot (`misc_statistics`) |
| Cross-check | $185.36–$188.25 same-day range reported by stockanalysis.com / Google Finance | WebSearch, consistent |

---

## 3. Quality Score — full calc (both ROIC methodologies shown per Gap #1)

**Inputs (TTM = trailing four quarters ending 30 Apr 2026, via `yfinance` quarterly statements):**

| Metric | Value |
|---|---|
| Revenue (TTM) | $3,319.216M |
| Net Income (TTM) | $941.652M → Net Margin **28.37%** |
| EBIT (TTM) | $955.749M |
| FCF (TTM, = OCF; capex immaterial) | $1,665.183M |
| Gross Margin (FY2026, latest annual) | 75.53% (up from 71.35% FY2024 — expanding) |
| Revenue 3yr CAGR (FY2023→FY2026) | 14.0% ($2,155.06M → $3,195.311M) |
| Net Debt | **−$6,464.955M** (net cash: debt $95.859M − cash&ST-investments $6,560.814M) |
| EBITDA (TTM, `yfinance`) | $1,026.113M |
| FCF/NI ratio (TTM) | 176.8% ($1,665.183M / $941.652M) |
| FCF-positive years | FY2022–FY2026, all 5 years positive — no cap trigger |

**Hard disqualifiers check:** FCF/NI never <70% (176.8% TTM, 152–177% every year FY2023–26) — pass. Net Debt/EBITDA — net cash, pass. FCF-positive 5 consecutive years — pass. **No disqualifiers.**

**Profitability (25%):**
```
NetMargin_Component = clamp((28.37/30)×100) = 94.6
ROIC (cash-adj)  = NOPAT $727.19M / IC $749.797M = 97.0%  → ROIC_Component = clamp(97.0/30×100) = 100.0
ROIC (unadj)     = NOPAT $727.19M / IC $7,214.752M = 10.1% → ROIC_Component = clamp(10.1/30×100) = 33.6

Profitability_Score (cash-adj) = (94.6 + 100.0)/2 = 97.3
Profitability_Score (unadj)    = (94.6 + 33.6)/2 = 64.1
```

**Margins (15%):**
```
GrossMargin_Score = clamp((75.53/80)×100) = 94.4   (no trend bonus needed — already above 40% floor for that rule)
```

**Growth (20%):**
```
Growth_Score = clamp((14.0/25)×100) = 56.0 + 10 (documented TAM expansion: Copli acquisition,
   Veeva Falcon MLR AI platform, Veeva EHS new product line — WebSearch) = 66.0
```

**Balance Sheet (15%):**
```
NetDebt/EBITDA = −$6,464.955M / $1,026.113M = −6.30×  (net cash)
BalanceSheet_Score = clamp(100×(1−(−6.30)/4)) = clamp(257.5) = 100.0
```

**Moat Signal (15%) — checklist, cited evidence only (Gap #2):**

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | Serves 47 of top 50 pharma companies; 9 of top 20 pharma committed to Vault CRM vs. Salesforce's 3; ~80% niche share (koalagains.com, ainvest.com) |
| Brand premium | FALSE (no citable evidence this session) | No documented price-increase-without-volume-loss data found |
| Network effect | **TRUE** | Veeva Network/OpenData: shared reference database improves as customers update records — documented crowdsourced-data mechanism (veeva.com) |
| Switching costs | **TRUE** | 21 CFR Part 11 compliance — replacing Veeva means revalidating regulated systems, retraining teams, compliance risk (intuitionlabs.ai) |
| Scale cost advantage | FALSE (no citable evidence this session) | No cost-per-unit-vs-competitor data found |

```
Moat_Score = (3/5) × 100 = 60.0
```

**FCF Quality (10%):**
```
FCFQuality_Score = clamp(((1.768 − 0.40)/0.60)×100) = clamp(228.0) = 100.0
```

**Quality Score:**
```
Quality Score = Profitability×0.25 + Margins×0.15 + Growth×0.20 + BalanceSheet×0.15 + Moat×0.15 + FCFQuality×0.10

Cash-adj ROIC:  97.3×0.25 + 94.4×0.15 + 66.0×0.20 + 100.0×0.15 + 60.0×0.15 + 100.0×0.10
              = 24.32 + 14.16 + 13.20 + 15.00 + 9.00 + 10.00 = 85.68 → 85.7

Unadj ROIC:     64.1×0.25 + 94.4×0.15 + 66.0×0.20 + 100.0×0.15 + 60.0×0.15 + 100.0×0.10
              = 16.02 + 14.16 + 13.20 + 15.00 + 9.00 + 10.00 = 77.38 → 77.4
```

**Result (primary, cash-adjusted ROIC): Quality Score = 85.7 — clears the 80.0+ gate.** Proceeding to Phase 02. (Under the unadjusted alternative, VEEV would score 77.4 and stop here — see Gap #1.)

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test:**
```
EY = 1 ÷ Forward PE = 1 ÷ 18.50 = 5.41%
Spread = 5.41% − 4.45% = +0.96pp
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL (+0.96pp)** → **+5 additive.**

**Step 2 — Rate Regime Modifier:** 10Y = 4.45% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for VEEV = +10**

---

## 5. Phase 02 — Valuation Score, full calc

**Inputs (live price $185.63; TTM basis; shares 162.443M):**

| Metric | Value | Basis |
|---|---|---|
| Market Cap | $30,154.35M | 162.443M × $185.63 |
| Enterprise Value | $23,689.39M | Market Cap + Debt $95.859M − Cash&ST-Inv $6,560.814M |
| EV/EBIT | **24.79×** | EV / EBIT(TTM) $955.749M |
| FCF Yield | **5.52%** | FCF(TTM) $1,665.183M / Market Cap |
| Forward PE | **18.50×** | $185.63 / forward EPS $10.035 (`yfinance` consensus) |
| 5yr PE range (auto, `yfinance` TTM-EPS reconstruction, n=20 quarters of 46 available) | avg **43.59×**, low **21.44×**, high **92.65×** | Per valuation-scoring.md auto-calc method |
| PEG / Fast Grower test | **NOT a Fast Grower** | NI growth FY2024 was +7.8% (<15%) — fails "3+ consecutive years >15%" on a clean base. PEG's 15% redistributed to EV/EBIT (→40%) |

**FCF Yield — 40% weight:**
```
FCF_Score = clamp(100 × (1 − 5.52/10)) = 44.8
```
→ Contribution: 44.8 × 0.40 = **17.9**

**EV/EBIT — 40% weight (PEG redistributed here):**
```
EV/EBIT_Score = clamp((24.79 − 12)/23 × 100) = 55.6
```
→ Contribution: 55.6 × 0.40 = **22.2**

**Forward PE (primary/range formula — 5yr range available) — 20% weight:**
```
FwdPE_Score = clamp((18.50 − 21.44)/(92.65 − 21.44) × 100) = clamp(−4.1) = 0.0
```
Historical PE Modifier (Upgrade 2): deviation from 5yr avg = (18.50 − 43.59)/43.59 = **−57.6%** (>20% below avg) → −10 modifier, but sub-score already at the 0.0 floor → **no change.**
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — not applicable** (not a Fast Grower). Weight redistributed to EV/EBIT above.

**Raw weighted score = 17.9 + 22.2 + 0.0 = 40.1**
**+ Rate Modifier (+10) = 50.1**

---

## 6. Upside/Downside Modifier — full calc

**Step 1 — Fair Value (Blended), Rule 1–8:**

*Method A — DCF (3-stage, 3 scenarios, Rule 2/7). Base FCF: TTM $1,665.183M. Net cash $6,464.955M. Shares 162.443M.*

| Scenario | WACC | Yrs1–5 FCF growth | Yrs6–10 fade | Terminal | TV weight | **FV/share** |
|---|---|---|---|---|---|---|
| **Bear** (Salesforce Life Sciences Cloud erodes share — 6 of top 20 pharma already chose alternatives; migration stalls) | 10.5% | 6.0% | 5.0%→2.0% | 2.0% | 47.3% | **$192.01** |
| **Base** (consensus — Vault CRM migration continues, ~14% growth in line with 3yr CAGR) | 9.5% | 14.0% | 11.0%→5.0% | 3.0% | 60.7% | **$344.82** |
| **Bull** (AI/Falcon MLR + Data Cloud expansion re-accelerate growth) | 8.5% | 18.0% | 15.0%→7.0% | 3.5% | 70.3% | **$553.90** |

```
PW DCF FV = 0.25×553.90 + 0.50×344.82 + 0.25×192.01 = $358.89
```
TV weight 47–70%, under the 75% Rule-4 trigger. **Even the bear case ($192.01) sits marginally above live price ($185.63)** — though by a much thinner margin (+3.4%) than a name like ADBE, so this is a weak, not strong, signal on its own.

*Method B — Comparable Multiples (discretionary anchors, Gap #3):*

| Approach | Fair multiple | FV/share |
|---|---|---|
| Forward PE comp | 25× × $10.035 | $250.88 |
| EV/EBIT comp | 22× × EBIT $955.749M, + net cash, / shares | $169.24 |
| FCF-yield comp | 4.25% yield on FCF $1,665.183M | $241.20 |
| **Multiples avg** | | **$220.44** |

**Triangulation:**
```
Blended FV = 0.40 × DCF(PW) $358.89 + 0.60 × Multiples $220.44 = $275.82
```
Cross-check: analyst consensus PT ≈$244.59 (29 analysts, "Buy" consensus per stockanalysis.com) sits between the multiples-avg and blended FV — directionally consistent.

**Step 2 — Expected annual return `E`:**
```
Gap Upside% = ($275.82 / $185.63) − 1 = +48.6%
```
Catalyst: Vault CRM migration wave (documented, industry-wide deadline window 2026–2029 — ainvest.com) — **but this runs well past the 18–24mo Rule 10 window**, so no crisp near-term catalyst qualifies for full credit. **Guardrail applied: cap upside (negative M) side at −5** (Gap #4).
```
Annualized gap (2yr default) = 48.6% / 2 = 24.3%
Intrinsic growth = 14.0% (revenue 3yr CAGR — used over the higher 22–23% FCF/NI 3yr CAGR, which is inflated by
   one-off margin expansion rather than representing a sustainable growth rate)
Shareholder yield = −0.75% (net dilution — SBC-driven share issuance exceeds buybacks; no dividend)

E = 24.3% + 14.0% − 0.75% = +37.5%
```
Uncapped mapping (E ≥ H=10%): M = −15 × clamp((37.5−10)/15, 0, 1) = **−15.0** (would clamp to full −15 if uncapped)
**Guardrail-capped M = −5.0** (Gap #4 — no catalyst within 18–24mo)

---

## 7. Final Valuation Score & Composite Score

```
Final Valuation Score = 40.1 (raw) + 10 (Rate Modifier) − 5.0 (capped Upside/Downside Modifier) = 45.1
```

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 85.7) + 0.50 × 45.1
                = 7.15 + 22.55 = 29.7
```

**Composite Score = 29.7 → Action Table band 0.0–29.9 → BUY — Full position 6–8%.**

**This is a marginal result — see Gap #5.** It sits 0.3pt inside the boundary, driven by a stack of judgment calls (ROIC treatment, comp-multiple selection, catalyst-window guardrail) each individually defensible but collectively capable of moving the number across the 30.0 line, or — under the alternate ROIC methodology — disqualifying VEEV from a Composite Score entirely.

---

## 8. Order Setup (BUY — Full position, per Composite Score 29.7)

```
Margin of Safety = 17.5% (midpoint of 15–20% band for Score 0.0–29.9)
Buy Price (ceiling)   = $275.82 × (1 − 0.175) = $227.55   → live $185.63 is below ceiling → ENTER NOW
Primary Sell Target   = Blended FV = $275.82
Bull-Case Trim Target = Bull DCF $553.90 × 0.90 = $498.51
Stop Loss             = $185.63 × (1 − 0.225) = $143.86   (22.5% max loss, midpoint 20–25% band)
R/R = ($275.82 − $185.63) ÷ ($185.63 − $143.86) = $90.19 ÷ $41.77 = 2.16 : 1   (≥ 2:1 ✓, but thin)
```

**Position sizing:**
```
Portfolio Value (combined, holdings.md) = $54,891.48
Max $ Risk (1.5%) = $823.37 ; Risk/share = $41.77 → risk-based size = 19.71 sh ($3,659.43 = 6.67% of portfolio)
6–8% allocation cap = $3,293.49–$4,391.32 → risk-based size falls inside the cap band, governs directly
Currently held: 3 sh ($556.89 at live price, 1.01% of portfolio)
TOP-UP = 16.71 sh (~$3,102.54)
Resulting position: ~19.71 sh × $185.63 = $3,659.43 = 6.67% of portfolio
```
**Cap cross-check:** 6.67% is within the 6–8% Very Cheap band and far under the 15% hard cap (Upgrade 7). No breach.

### Order Setup Checklist
```
[x] Valuation Score (incl. Upside/Downside Mod): 45.1
[x] Composite Score (Quality 85.7 + Valuation 45.1): 29.7   (≤ 29.9 ✓, marginal — see Gap #5)
[x] Expected annual return E / catalyst window:  +37.5% / 2yr (guardrail-capped, no crisp <24mo catalyst)
[x] Upside/Downside Modifier applied:            −5.0 (capped; uncapped would be −15.0)
[x] DCF Fair Value (PW):                         $358.89
[x] Multiples-Based Fair Value:                  $220.44
[x] Blended Fair Value:                          $275.82
[x] Margin of Safety %:                          17.5%
[x] BUY PRICE (limit order / already below):     $227.55  (live $185.63 already below — enter now)
[x] PRIMARY SELL TARGET:                         $275.82
[x] BULL-CASE TRIM TARGET:                        $498.51
[x] STOP LOSS:                                   $143.86
[x] Risk/Reward Ratio:                           2.16:1  (≥ 2:1, thin)
[x] Max $ Risk:                                  $823.37
[x] POSITION SIZE (shares):                      ~19.71 (top up 16.71 from current 3)
[x] POSITION SIZE ($):                           $3,659.43 (6.67% of portfolio)
[x] Thesis invalidation triggers:                Salesforce Life Sciences Cloud materially displaces Vault CRM
    at top-20 pharma accounts beyond the 6 already lost; FCF/NI conversion breaks down; gross margin
    compresses >3pp structurally; ROIC (either methodology) falls below WACC (~9.2%)
```

**Given Gap #5's boundary sensitivity and the thin 2.16:1 R/R, this reads as a marginal Buy signal, not a high-conviction one — the human investor should weigh the judgment calls in §1 before sizing a full 6–8% position.**

---

## 9. Next Review Trigger

- **Scheduled:** Next earnings release, 02 Sept 2026 (Q2 FY2027) — standard Rule 9 quarterly re-score.
- **Event-triggered:** Guidance revision, management change, M&A, or a >15% unexplained price move from $185.63 (Rule 9).
- **Specific to this session's flags:** any credible reporting on Vault CRM migration losses at additional top-20 pharma accounts (thesis-relevant — watch the "6 of 20 opted for other solutions" figure for further deterioration), or resolution of the ROIC-methodology question (Gap #1) if the human investor wants to settle it before sizing the position.

---

## Sources (WebSearch/WebFetch, per tool requirements)

- [US 10 Year Treasury Note Yield — TradingEconomics](https://tradingeconomics.com/united-states/government-bond-yield)
- [10 Year Treasury Rate — YCharts](https://ycharts.com/indicators/10_year_treasury_rate)
- [Veeva Systems (VEEV) Statistics & Valuation — stockanalysis.com](https://stockanalysis.com/stocks/veev/statistics/)
- [Veeva Vaults into CRM Lock-In as Migration Window Narrows to 2026–2029 — ainvest.com](https://www.ainvest.com/news/veeva-vaults-crm-lock-migration-window-narrows-2026-2029-2604/)
- [Veeva Systems Inc. (VEEV) Business & Moat Analysis — koalagains.com](https://koalagains.com/stocks/NYSE/VEEV/business-and-moat)
- [Veeva OpenData Partner Ecosystem Expands to Include More Than 100 Companies — veeva.com](https://www.veeva.com/resources/veeva-opendata-partner-ecosystem-expands-to-include-more-than-100-companies/)
- [Veeva Systems: A High-Growth Play in Life Sciences Cloud Amid Strategic Momentum — ainvest.com](https://www.ainvest.com/news/veeva-systems-high-growth-play-life-sciences-cloud-strategic-momentum-2508/)
- [Veeva Systems Set to Join S&P 500 — press.spglobal.com](https://press.spglobal.com/2026-04-30-Veeva-Systems-Set-to-Join-S-P-500)

---

## Glossary

- **CAGR** — Compound Annual Growth Rate.
- **Composite Score** — this framework's blended Quality + Valuation ranking number; see [glossary.md](../framework/glossary.md).
- **DCF** — Discounted Cash Flow.
- **EBIT / EBITDA** — Earnings Before Interest & Taxes / + Depreciation & Amortization.
- **EV / EV/EBIT** — Enterprise Value / the multiple of it to operating profit.
- **EY (Earnings Yield)** — 1 ÷ Forward PE.
- **Fast Grower** — Lynch's term for EPS growth >15%/yr for 3+ years; this framework's PEG-eligibility trigger.
- **FCF / FCF Yield / FCF/NI conversion ratio** — Free Cash Flow and its two standard ratios used here.
- **Forward PE** — Price ÷ next-twelve-months expected EPS.
- **FV (Fair Value)** — the analyst's intrinsic-value estimate.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company outright regardless of weighted score.
- **Moat** — Buffett's term for a durable competitive advantage.
- **MoS (Margin of Safety)** — cushion below fair value at which the buy price is set.
- **Net Debt/EBITDA** — leverage ratio; this framework's balance-sheet gate.
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate); numerator of ROIC.
- **PEG ratio** — PE ÷ earnings growth rate.
- **PT (Price Target)** — an analyst's price forecast.
- **PW (Probability-Weighted) Fair Value** — 25% bull + 50% base + 25% bear blended FV (Rule 7).
- **Quality Score** — this framework's 0–100.0 grading of Phase 01 criteria; 80.0+ required to proceed to valuation scoring.
- **Rate Environment Gate / Rate Regime Modifier** — the pre-Phase-02 Treasury-yield check and its additive score adjustment.
- **R/R (Risk/Reward ratio)** — expected gain ÷ expected loss; 2:1 minimum to enter.
- **ROIC** — Return on Invested Capital.
- **Rule 0 / Rule 9 / Rule 10** — this framework's standing rules on live pricing, mandatory re-valuation triggers, and separating intrinsic value from market price.
- **SaaS (Software-as-a-Service)** — a software delivery model where customers subscribe to access hosted software (rather than buying and installing it), generating recurring subscription revenue — VEEV's core business model. *(New — added to [glossary.md](../framework/glossary.md) this session.)*
- **Shareholder yield** — dividend yield + net buyback yield.
- **TAM** — Total Addressable Market.
- **TTM (Trailing Twelve Months)** — most recent 12 months of reported results.
- **Upside/Downside Modifier (Expected-Return Modifier)** — the additive ±15 score adjustment based on expected annual return.
- **WACC** — Weighted Average Cost of Capital.
- **21 CFR Part 11** — the FDA regulation governing electronic records/signatures in regulated life-sciences workflows; compliance with it is a major source of VEEV's customer switching costs, since replacing a Part-11-validated system requires re-validating the replacement. *(New — added to [glossary.md](../framework/glossary.md) this session.)*

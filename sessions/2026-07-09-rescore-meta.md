# RESCORE — META — 2026-07-09

**Task type:** RESCORE (single ticker) — **Telegram-triggered** (Routine 6 / `/telegram-scan`)
**Trigger:** New top post [t.me/tarasguk/11337](https://t.me/tarasguk/11337) (~19:35 UTC, 2026-07-09): "Zuckerberg indicated that Meta's computational capacity is 'so advantageous that it might make sense' to lease it rather than use it exclusively internally. The plans could involve selling access to deployed AI models or raw computing power." META is a current holding (7.04% weight) and this claims a candidate Rule 9 event — the exact "Meta Compute confirmation" watch item flagged in [watchlist/in-portfolio/META/META-2026-07-01.md](../watchlist/in-portfolio/META/META-2026-07-01.md)'s Next Review Trigger. Per CLAUDE.md Rule 0, the post's text is used only as a trigger — every figure below is independently re-pulled from IBKR/live web sources, not from the post.
**Date:** 9 Jul 2026
**10Y US Treasury Yield:** 4.56% (FRED `DGS10`, last posted value, dated 2026-07-08 — up from 4.46% used 07-01; still inside the "3.5–5%" bracket → Rate Regime Modifier Step 2 unchanged at +5)
**Rate Regime Modifier (Step 2):** +5
**Last review on record:** META **35.6** (2026-07-01, Composite 22.8, BUY — Full position 6–8% — [sessions/2026-07-01-rescore-meta.md](2026-07-01-rescore-meta.md))
**Gap since last review:** 8 days.

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EV/EBIT = enterprise value ÷ operating profit; PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; D&A = depreciation and amortization; capex = capital expenditure; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; CAGR = compound annual growth rate; pp = percentage points; EY = earnings yield (1 ÷ PE); NOPAT = net operating profit after tax; ROIC = return on invested capital; TTM = trailing twelve months; NTM = next twelve months.*

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$638.45** | IBKR `get_price_snapshot` (contract_id 107113386, META Class A / NASDAQ), pulled this session (ts 1783640442 → 2026-07-09 23:40:42 UTC) |
| Session change | **+$35.33 / +5.86%** | IBKR `change` field — a large one-day move, same day as the triggering post |
| 52-week range | **$520.26 – $794.42** | IBKR `misc_statistics` |
| Year-to-date change | **−3.26%** | IBKR `year_to_date_change` |
| Analyst consensus PT | **$827.91** (63 analysts, S&P Global via stockanalysis.com, updated 8 Jul 2026) | Web search — bull-case sanity check only (Rule 0 Step 4) |

Price vs 07-01 session: $624.70 → $638.45 = **+2.20%** over 8 days — but today alone accounts for +5.86% of that. Under the 15% Rule 9 unexplained-move threshold, and (per §2 below) explained by the same recurring "Meta Compute" story, not unexplained.

---

## 2. Rule 9 Trigger Check (2026-07-01 → 2026-07-09)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No | Still scheduled for **29 Jul 2026** (after close) — unchanged, ~3 weeks out |
| Guidance revision | No | No new guidance since the Q1 2026 call figures already on record (Q2 revenue $58–61B, FY26 capex $125–145B, FY26 opex $162–169B) |
| M&A | No | No new M&A found since prior sessions |
| Management change | No | No change found |
| Macro shift | No | 10Y ticked 4.46%→4.56%, still inside the "3.5–5%" bracket |
| **>15% unexplained price move** | **No** | +5.86% today, +2.20% over 8 days — both well under 15%, and both attributable to the item below |

**The triggering post's claim, independently verified.** A Bloomberg exclusive interview published **2026-07-09** ("Meta's Zuckerberg Says Exploring AI Cloud Business Makes Sense") quotes Zuckerberg directly: *"The offers that you get for using the compute are so high that it may make sense, in some cases, to rent out or consider those kind of deals instead of your own internal uses."* This is the real, primary-sourced event behind the Telegram post (confirmed independently via WebSearch — Bloomberg, TechRadar, TipRanks, TheNextWeb all carry the same 07-09 interview) — the post's text was not used as a financial input, only as the trigger pointing at this search.

**Classification: still does NOT meet the Rule 9 bar.** Compared to the language already assessed and excluded in the 07-01 session ("definitely on the table," reported second-hand) and the 06-30 Bloomberg report ("Meta is building..."), this is a *direct, on-the-record* CEO quote — a meaningfully higher-confidence source than an anonymously-sourced report — but the substance is still identical hedge language: **"may make sense," "in some cases," "consider."** No business has been launched, no contract signed, no revenue guidance issued, no 8-K filed. Applying the same bar consistently (a company-confirmed strategic announcement, formal guidance revision, or M&A — not exploratory CEO commentary, however directly attributed), **this remains a qualitative watch item, elevated in confidence but not yet a scored input or Rule 9 trigger.**

**Conclusion: no Rule 9 trigger fired.** This is a Telegram-triggered *check*, not a Rule-9-confirmed re-score — consistent with the framework's Rule 0 discipline (never treat a report, or even a direct quote reported by a single interview, as company-confirmed data until it clears the bar of an actual disclosed business decision). The price move itself is small and explained. Proceeding with a full re-score anyway since 8 days have passed and price/consensus inputs have moved — same practice as every routine 3-day check in this ticker's history.

---

## 3. META — Inputs Collected

**Sector:** Communication Services — Internet & Digital Advertising / Social Platforms
**Current portfolio weight:** 7.04% (per [holdings.md](../portfolio/holdings.md) — not recomputed this session)

### Carried unchanged from the 07-01 session (no new quarter reported — Q2 2026 not out until 29 Jul)

| Item | Value | Why carried |
|---|---|---|
| TTM EBIT | $88.621B | No new quarter |
| TTM FCF (raw — scored input) | $45.65B | Same — Owner Earnings (Upgrade 1) still unresolved, Data Gap #1 (8th consecutive session) |
| TTM Net Income | $70.629B | Same |
| TTM Revenue | $214.963B | Same |
| TTM D&A | $20.719B | Same |
| Cash + marketable securities | $81.180B | Same (Q1 2026 balance sheet) |
| Senior-note debt (excl. operating leases) | $58.748B | Same |
| Net cash | **$22.432B** | Unchanged |
| Shares outstanding | ≈2.196B | Same |
| Gross margin | 81.9% | Carried — `yfinance` still unavailable in this environment (Data Gap #3, 8th consecutive session — module not installed / TLS issue persists) |
| FCF/NI conversion | **64.6%** | Unchanged |
| Net Debt/EBITDA | −0.205× (net cash) | Unchanged |
| 5yr avg PE (auto-reconstructed) | 23.589× (range 9.255×–36.014×, n=20q) | Carried — `yfinance` unreachable this session too |
| ROIC tax-rate normalization | 14.5% (Meta's own guided forward rate) | Unchanged basis |

### Refreshed this session (price/consensus-dependent)

| Item | 07-01 value | 07-09 value (fresh) | Computation |
|---|---|---|---|
| Live price | $624.70 | **$638.45** | IBKR snapshot (§1) |
| Market Cap | $1,371.8412B | **2.196B × $638.45 = $1,402.0362B** | Computed |
| EV | $1,349.4092B | **$1,402.0362B − $22.432B = $1,379.6042B** | Computed |
| **EV/EBIT** | 15.2268× | **$1,379.6042B ÷ $88.621B = 15.5675×** | Computed |
| **FCF Yield** | 3.3277% | **$45.65B ÷ $1,402.0362B = 3.2560%** | Computed |
| Forward EPS (NTM/CY2026 consensus) | $32.81 | **$32.59** | S&P Global consensus via stockanalysis.com, updated 2026-07-08 — down slightly, ordinary drift |
| Forward PE | 19.0399× | **$638.45 ÷ $32.59 = 19.5905×** | Computed at fresh price and fresh consensus |

### Fast-Grower (PEG eligibility) test — re-verified, still fails

No new fiscal year has reported since 07-01. **Still FAILS** ">15% EPS growth for 3+ consecutive years on a clean base" (FY2024 +59.5% low-comp rebound, FY2025 −3.0%). **PEG not applicable; its 15% weight redistributed to EV/EBIT** — unchanged from every prior META session.

---

## 4. Data Gaps / Flags

1. **Upgrade 1 (Owner Earnings) — still unresolved; raw FCF used (8th consecutive session).** No new information this window.
2. **5yr PE reconstruction — still not re-runnable.** `yfinance` is not available in this session's environment (module not installed) — same standing gap documented across recent sessions under a TLS/`curl_cffi` error. Carrying forward 23.589×/9.255×/36.014× (n=20 quarters) — defensible since Q2 2026 (29 Jul) hasn't landed, so the trailing 20-quarter window is unchanged regardless.
3. **Gross margin (81.9%) still carried, not re-collected live** — same Data Gap #3 root cause. Directionally stable for a business this size over 8 weeks.
4. **"Meta Compute" cloud-business — qualitative watch item, elevated confidence, still not a scored input (§2).** The CEO's own direct quote (Bloomberg, 07-09) raises confidence this eventually happens, but it is still hedge language ("may," "in some cases") with no disclosed business launch, contract, or revenue guidance. Excluded from the Quality Score's Growth-modifier bonus basis (which already stands independently on cited ad-market-share data) and from the Upside/Downside Modifier's scenario assumptions this session, same as 07-01. **Will be incorporated with real numbers the moment Meta discloses an actual launch, contract, or guidance change** — the natural next checkpoint is the 29 Jul Q2 earnings call, now only ~3 weeks out.

---

## 5. META — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 19.5905 = 5.1045%
Spread = EY − 10Y Treasury = 5.1045% − 4.56% = +0.5445%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.5445%, ~0.96pp short) → **+5 additive.**

> Still FAILS, and by a slightly wider margin than 07-01 (+0.79pp short → +0.96pp short) — price rose while the consensus EPS estimate ticked down slightly and the 10Y rose, all three working in the same (fail-widening) direction.

**Step 2 — Rate Regime Modifier**
10Y = 4.56% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for META = +10** (unchanged from 07-01).

---

## 6. META — Quality Score (recomputed, unchanged inputs)

No new quarter, no margin/balance-sheet/moat change this window — every underlying input (§3, carried) is identical to 07-01, so the Quality Score recomputes to the same result rather than being merely copied forward:

```
Profitability (25%): Net Margin 32.86%, ROIC 25.05% (unchanged basis)
  Profitability_Score = 91.75
Margins (15%): Gross margin 81.9% (carried) → 100.0
Growth (20%): Revenue 3yr CAGR 19.89% → 79.57
  + 10 (TAM-expansion bonus — ad-market-share data alone independently supports it, per 07-01;
    Meta Compute still excluded from this basis per Data Gap #4/§2 above) → 89.57
Balance Sheet (15%): Net Debt/EBITDA −0.205× → 100.0
Moat Signal (15%): 5/5 signals unchanged (market share, brand premium, network effect,
  switching costs, scale cost advantage) → 100.0
FCF Quality (10%): FCF/NI 64.6% (carried) → 41.0 (growth-capex explanation still stands, no
  hard-disqualifier fire)

Quality Score = 91.75×0.25 + 100.0×0.15 + 89.57×0.20 + 100.0×0.15 + 100.0×0.15 + 41.0×0.10
              = 22.9375 + 15.0 + 17.914 + 15.0 + 15.0 + 4.10
              = 89.9515 → rounds to 90.0
```

**Quality Score = 90.0 — unchanged, PASSES the 80.0+ gate.** No quality drift this window (expected — no new fundamentals reported).

**Hard disqualifier check:** none fire, same as 07-01.

---

## 7. META — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 3.2560/10), 0, 100) = 67.440
```
→ Contribution: 67.440 × 0.40 = **26.976**

**EV/EBIT — 40% weight** (PEG not applicable → 15% redistributed here)
```
EV/EBIT_Score = clamp((15.5675 − 12)/23 × 100, 0, 100) = 15.5109
```
→ Contribution: 15.5109 × 0.40 = **6.20435**

**Forward PE (fallback formula) — 20% weight**
```
Deviation% = (19.5905 − 23.589)/23.589 × 100 = −16.951%
FwdPE_Score = clamp(50 + (−16.951) × 2.5, 0, 100) = clamp(7.622, 0, 100) = 7.622
```
→ Contribution: 7.622 × 0.20 = **1.5244**

**PEG — Fast-Grower test: FAIL** (re-verified §3). Weight redistributed to EV/EBIT (used above).

**Raw weighted score:**
```
= 26.976 + 6.20435 + 1.5244 = 34.70475
```
**+ Rate Modifier (+10) = 44.70475** *(before the Upside/Downside Modifier)*

---

## 8. META — Upside/Downside Modifier (Expected-Return Modifier)

**Decision: update Base-case EPS to the fresh $32.59 consensus; Bull/Bear EPS and both exit multiples carried unchanged** — same practice as 07-01, and nothing in this window (§2/§4) changes the underlying bull/bear narrative (Meta Compute still excluded until confirmed).

**Step 1 — Scenario fair values**

| Scenario | Weight | EPS assumption | Exit PE | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | $40.0 (carried) | 24× | **$960.00** |
| **Base** | 50% | $32.59 (fresh consensus) | 20× | **$651.80** |
| **Bear** | 25% | $28.0 (carried) | 13× | **$364.00** |

```
PW Fair Value = 0.25×960.00 + 0.50×651.80 + 0.25×364.00 = $656.90
```
(Down slightly from 07-01's $659.10 — the Base-case consensus EPS ticked down $32.81→$32.59.)

Sanity check (Rule 0 Step 4 / Rule 4): PW FV $656.90 remains below the $827.91 analyst consensus PT.

**Step 2 — Gap, annualization, components**
```
Gap Upside %    = ($656.90 ÷ $638.45) − 1                  = +2.8898%
Catalyst window = 2 years (unchanged — AI ad-monetization proof points at Q2 2026 earnings,
                   capex-ROI demonstration; both ~18–24mo out. Meta Compute still NOT counted as
                   a named catalyst per §2/§4.)
Annualized gap  = 2.8898% ÷ 2                               = +1.4449%/yr
Intrinsic growth = +12.0%/yr   (carried, unchanged basis)
Shareholder yield = buyback yield + dividend yield (recomputed at fresh market cap $1,402.0362B)
                  = $26.25B/$1,402.0362B + $5.32B/$1,402.0362B  = 1.8724% + 0.3794% = +2.2518%/yr
```
```
E (expected annual return) = 1.4449 + 12.0 + 2.2518 = +15.6967%/yr
```

**Step 3 — Catalyst/timeline (Rule 10 + Guardrail 1).** Same two catalysts as prior sessions, both inside the 18–24-month window (Q2 earnings now ~3 weeks out). **Upside credit fully allowed; the −5 catalyst cap does NOT apply.**

**Step 4 — Map E to the modifier** (hurdle H = 10%):
```
E = 15.6967% ≥ H → M = −15 × clamp((15.6967 − 10)/15, 0, 1)
                      = −15 × clamp(0.37978, 0, 1)
                      = −5.6967
```
**Upside/Downside Modifier M = −5.6967** — a further step down from 07-01's −7.0545, continuing the trend as the price keeps closing the gap to a roughly flat fair value.

---

## 9. META — Final Valuation Score, Quality Score, Composite Score

```
FINAL VALUATION SCORE = Raw weighted (34.70475) + Rate Modifier (+10) + Upside/Downside (−5.6967)
                       = 39.00805
```
Boundary rule: not a ".X5" → standard rounding → **Final Valuation Score = 39.0**

| | Value |
|---|---|
| Raw weighted | 34.70475 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | −5.6967 (E = +15.70%) |
| **FINAL VALUATION SCORE** | **39.0** |
| Prior valuation score | 35.6 (07-01) |
| **Quality Score** | **90.0 (unchanged, PASSES 80.0+ gate)** |

```
Composite Score = 0.50 × (100 − 90.0) + 0.50 × 39.0 = 0.50×10.0 + 0.50×39.0 = 5.0 + 19.5 = 24.5
```

**Composite Score = 24.5** (up from 22.8 on 07-01 — small, mechanical move from the price/consensus drift, not from any new catalyst).

---

## 10. META — Action & Category Change

**Valuation Score alone: 35.6 → 39.0** — stays inside the same BUY-Standard band (30.0–49.9). **No band change**, a small mechanical drift only.

**Composite Score: 22.8 → 24.5 → Action band: BUY — Full position 6–8% (Score 0.0–29.9), unchanged.** No action-category change at either the raw or blended level.

**Practical recommendation: HOLD — no automatic fresh capital.** META is an existing holding at **7.04%**, inside the 6–8% full-position band, well under the 15% hard cap.

---

## 11. META — Order Setup (Composite Score in BUY-Full band → required)

Confidence: wide-moat proven compounder (Quality Score 90.0, unchanged) with heavy in-flight AI capex — same conservative 20% MoS used every prior session.

```
[x] Composite Score (drives action band):        24.5   (≤29.9 ✓ — Full-position entry permitted)
[x] Raw Valuation Score (incl. Upside/Downside):  39.0
[x] Expected annual return E / catalyst window:   +15.70% / 2yr
[x] Upside/Downside Modifier applied:             −5.6967
[x] Blended Fair Value (PW, Rule 7):              $656.90  (down slightly from $659.10 — consensus EPS drift)
[x] Margin of Safety %:                           20%
[x] BUY PRICE (limit):     $656.90 × (1 − 0.20)        = $525.52
[x] PRIMARY SELL TARGET:   = Blended FV                = $656.90
[x] BULL-CASE TRIM TARGET: $960.00 × 0.90               = $864.00
[x] STOP LOSS:             $525.52 × (1 − 0.25)        = $394.14   (25% max loss, high-conviction bracket)
[x] Risk/Reward Ratio (base-case target):  ($656.90 − $525.52) ÷ ($525.52 − $394.14) = $131.38 ÷ $131.38 = 1.00:1
[x] Risk/Reward Ratio (bull-case trim target): ($864.00 − $525.52) ÷ $131.38 = $338.48 ÷ $131.38 = 2.58:1
```

Live price ($638.45) remains **$112.93 (21.5%) above** the $525.52 buy-price limit — the gap has widened slightly from 07-01's 18.5%. **Base-case R/R still exactly 1.00:1 (fails the 2:1 minimum)**, same recurring shape as every prior META session. **Net: no automatic qualifying entry** — both the price-limit condition and the R/R condition fail.

**Position sizing:** META is at **7.04%**, inside the 6–8% band. Room to the 8% ceiling: **0.96pp**. No forced trim or top-up.

---

## 12. Portfolio Note

META at 7.04% is comfortably under the 15% hard cap (Upgrade 7) and sits within the 6–8% full-position band its Composite Score points to. No portfolio-level action is forced by this score (no trim signal — nowhere near the 70+ trim bands; no forced top-up — R/R and price-limit both fail). This session does not change the `holdings.md` weight itself, only Last Score/Quality Score/Composite Score/Last Review.

---

## 13. Next Review Triggers

- **Next earnings — META Q2 2026, expected 29 Jul 2026 (after close)** → routine post-earnings re-score; refreshes all carried TTM fundamentals, and is the natural checkpoint for Meta to either confirm the "Meta Compute" business with real numbers or let the watch item lapse.
- **"Meta Compute" cloud-business — still an elevated watch item, still not confirmed (§2/§4).** Even a direct CEO quote in an exclusive Bloomberg interview does not clear the bar without an actual disclosed launch, contract, or guidance change. If that clears before the next scheduled review, it is a genuine Rule 9-qualifying development warranting an immediate re-score, including folding real numbers into the Quality Score's Growth modifier and the Upside/Downside Modifier's Bull-case assumptions.
- **Rule 9 fundamental triggers (standing):** any guidance revision, management change, material M&A, or a >15% unexplained price move (currently the closest daily move on record was today's +5.86%, explained).
- **Rate Gate watch:** Step 1 FAILED again this session, by a slightly wider margin (+0.54% cushion, down from +0.79%) — worth rechecking if price continues to run or the 10Y moves either direction.
- **Buy-price watch:** live price ($638.45) is now 21.5% above the $525.52 limit — worth a fresh check if the price pulls back materially before Q2 earnings.
- **5yr PE reconstruction (Data Gap #2, formerly #3)** and **Owner Earnings methodology decision (Data Gap #1)** — both still open, 8th consecutive session; `yfinance` is not installed in this session's sandbox environment at all (a different symptom than the previously-documented TLS/`curl_cffi` error, but the same practical effect — worth a `/healthcheck` note if this persists).

---

## 14. Glossary

(Pulled from [glossary.md](../framework/glossary.md) — terms actually used in this output; no new terms this session)

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year. |
| **8-K (Form 8-K)** | A US company's "current report" disclosing a material event between regular filings. |
| **bps / pp (percentage points)** | A direct difference between two percentages, distinct from a "%" change. |
| **Buyback yield** | The rate at which a company's share count shrinks per year from repurchases, net of new issuance. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; drives Phase 03/05 action-table lookups once a Quality Score exists. |
| **D&A** | Depreciation & Amortization. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years — this framework's PEG-eligibility trigger. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted score. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **NTM** | Next Twelve Months. |
| **Owner Earnings** | Net Income + D&A − maintenance capex only — used instead of raw FCF for moat-building reinvestors (Upgrade 1; unresolved for META, Data Gap #1). |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0** | Always fetch a live price first — never infer from multiples. |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |

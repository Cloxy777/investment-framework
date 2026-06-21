# RESCORE — ADBE (Adobe Inc.) — 2026-06-20

**Task type:** RESCORE (single ticker)
**Date of record:** 20 Jun 2026
**10Y US Treasury Yield:** 4.46% (TradingEconomics/CNBC, 18 Jun 2026)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket — "capital has real cost")
**Current ADBE weight:** 3.64% of portfolio (10 of a ~17-share target filled — partial fill; see [holdings.md](../portfolio/holdings.md))
**Prior score:** 5.0 ("Very Cheap", BUY band — [2026-06-12 new-position session](2026-06-12-new-position-adbe.md))
**Sector:** Technology — Software (Creative/Document Cloud — Digital Media — and Digital Experience / marketing cloud)

This rescore applies the new **Upside/Downside Modifier** (Expected-Return Modifier, added to the valuation score 2026-06-20) for the first time on ADBE, and uses the new **automated 5-year average PE** (framework change 2026-06-20) in place of the prior session's manually-sourced 10-year GAAP PE.

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$195.16** | `yfinance` `currentPrice`/`regularMarketPrice`, intraday 20 Jun 2026 (−$1.12 / −0.57% vs prior close $196.28). IBKR `get_price_snapshot` was attempted first per Rule 0 but the tool call was **permission-denied** this session, so the documented `yfinance` fallback was used. |
| 52-week high / low | $392.58 / $190.12 | `yfinance` (`fiftyTwoWeekHigh`/`fiftyTwoWeekLow`); today's low $190.12 = the 52-wk low (fresh low intraday) |
| Today open / high / low | $193.60 / $196.78 / $190.12 | `yfinance` |
| Analyst consensus PT | ~$282 mean / ~$250 median (range $190–$487; "Hold"/"Neutral" consensus, 22–55 analysts depending on source) | `yfinance` `targetMeanPrice` $282.27 / `targetMedianPrice` $250.00; cross-checked via WebSearch (MarketBeat, stockanalysis, S&P Global) |

**Context:** ADBE is down a further ~5.9% from the prior rescore's $207.30 (12 Jun) and is making fresh 52-week lows (~50% below the 52-wk high $392.58). No new fundamental trigger was reported between 12 Jun and 20 Jun — the drift lower is a continuation of the same AI-disruption-narrative + CFO-departure overhang already documented on 12 Jun, not a new Rule 9 event. Per the framework, price drift on an intact thesis is **not** itself an action trigger; this rescore is driven by the new modifier and refreshed multiples, not the price move.

---

## 2. Data Gathered (Standard Re-Score inputs) & Gaps Flagged

All figures from `yfinance` (`t.financials`, `t.cashflow`, `t.quarterly_financials`, `t.quarterly_cashflow`, `t.info`, `t.get_earnings_dates`) pulled 2026-06-20 — fiscal year ends late November.

| Metric | Value | Source / Derivation |
|---|---|---|
| FY2025 Revenue (FY ended 30 Nov 2025) | $23.769B (+10.5% YoY) | `t.financials` |
| FY2024 / FY2023 / FY2022 Revenue | $21.505B / $19.409B / $17.606B | `t.financials` |
| **Revenue CAGR 3yr** (FY22→FY25) | **10.52%** = (23.769/17.606)^(1/3) − 1 | Computed |
| **TTM Revenue** (Q3 FY25→Q2 FY26) | $25.198B | Sum of 4 latest reported quarters ($6.618 + 6.398 + 6.194 + 5.988B) |
| FY2025 EBIT (operating profit before interest & tax) | $8.997B (directly reported) | `t.financials` — *cleaner than 12-Jun's derived $8.70B* |
| **TTM EBIT** | **$9.372B** | Sum Q3 FY25–Q2 FY26 ($2.254 + 2.330 + 2.485 + 2.303B) |
| FY2025 Net Income / Net margin | $7.130B / 30.0% | `t.financials` |
| FY2025 Gross margin | 89.4% | `t.info` `grossMargins` |
| FY2025 Operating margin | 36.6% (TTM `operatingMargins` 35.3%) | `t.financials` / `t.info` |
| TTM Net Income | $7.229B | Sum of 4 latest quarters |
| ROE | 63.0% (`returnOnEquity`) — buyback-shrunk equity base inflates this; ROIC well >15% on any basis (26–41% range across sources, 12-Jun session) | `t.info` |
| FY2025 FCF (free cash flow = cash from operations − capex) | $9.852B | `t.cashflow` |
| **TTM FCF** | **$10.280B** | Sum Q3 FY25–Q2 FY26 ($2.126 + 3.126 + 2.921 + 2.107B) |
| **FCF/NI conversion (TTM)** | **142.2%** ($10.28B / $7.229B) — well above 70% gate; FY22–25 all 128–156% | Computed; `t.cashflow`/`t.financials` |
| Total debt / Cash & ST inv | $7.077B / $5.626B | `t.info` (`totalDebt`/`totalCash`) |
| **Net debt** | **+$1.451B (net debt)** | Computed — **changed sign vs 12-Jun (was −$0.672B net cash).** See Gap #2 |
| Shares outstanding | ~397.5M (was ~404.2M on 12-Jun — buybacks continuing) | `t.info` `sharesOutstanding` |
| **Market Cap** | **$77.58B** (397.5M × $195.16; `t.info` $77.576B) | Computed / `t.info` |
| **Enterprise Value** | **$79.03B** ($77.58B + $1.451B net debt; `t.info` $79.03B) | Computed / `t.info` |
| **EV/EBIT (TTM)** | **8.43×** ($79.03B / $9.372B) | Computed |
| **FCF Yield (TTM)** | **13.25%** ($10.28B / $77.58B) | Computed |
| FY2026 non-GAAP EPS guidance (raised 11 Jun) | $24.35–24.45 (mid $24.40) | Adobe Q2 FY2026 release (carried from 12-Jun session) |
| **Forward PE** | **8.00×** ($195.16 / $24.40 FY26 non-GAAP mid) | Computed. (yfinance `forwardEps` $27.54 = FY27 consensus → 7.09×, even cheaper; doesn't change score — see Gap #3) |
| **5yr Avg PE (auto)** | **27.2×** (range 8.9–51.8×, n=20 quarters) | `t.get_earnings_dates` TTM-EPS reconstruction per [valuation-scoring.md](../framework/valuation-scoring.md) auto-calc method |
| Non-GAAP EPS growth: FY23/FY24/FY25/FY26E | +17% / +14.6% / +13.7% / +16.6% | 12-Jun session (carried) |

### Data Gaps / Flags

1. **IBKR price snapshot permission-denied** — Rule 0 prefers IBKR `get_price_snapshot`; the call was blocked this session, so the documented `yfinance` fallback was used. `yfinance` intraday last ($195.16) is a live (not prior-close) figure and is consistent with the WebSearch context (fresh 52-wk lows). Flagged for transparency; does not change the conclusion.
2. **Net cash → net debt sign flip.** 12-Jun used net cash −$0.672B; current `yfinance` balance sheet shows net debt +$1.451B (total debt rose $6.23B→$7.08B, cash fell $6.9B→$5.63B). This *raises* EV by ~$2.1B. Even so, EV/EBIT is 8.43× — still far below the 12× scoring floor → EV/EBIT_Score still clamps to 0.0. **Does not change the score.** Worth noting as a monitoring item (buybacks may be partly debt-funded), but the balance sheet remains very strong (net debt/EBITDA ≈ 0.15×).
3. **Forward PE basis.** Used FY2026 non-GAAP guidance midpoint ($24.40) for consistency with the 12-Jun session. The yfinance next-fiscal-year consensus EPS ($27.54 → Fwd PE 7.09×) is even cheaper. Either way the deviation vs the 5yr avg is far past −20%, so FwdPE_Score clamps to 0.0. **Does not change the score.**
4. **5yr-avg PE replaces 10yr-GAAP PE.** Per the 2026-06-20 framework change (Upgrade 2 lookback shortened 10yr→5yr for automation), this rescore uses the auto-computed 5yr avg PE of **27.2×** (vs the 12-Jun session's manually-sourced 10yr GAAP avg of 44.58×). The 5yr window deliberately captures the multiple's recent compression, so it is the more conservative/relevant anchor. Forward PE (8.0×) is still 70.6% below it. **Does not change the sub-score** (clamps to 0.0 either way).
5. **PEG / Fast Grower test:** non-GAAP EPS growth was +14.6% (FY24) and +13.7% (FY25) — the two most-recently-completed years are both **below 15%**, so ADBE does **not** satisfy ">15% for 3+ consecutive years." **Classified NOT a Fast Grower** → PEG's 15% weight is redistributed to EV/EBIT (→ 40%), per the Final Score Formula note. (Note: `yfinance` reports a `pegRatio` of 0.53, shown only as a sensitivity datapoint — not the scored input, per the clean-earnings/Fast-Grower clarification.)

---

## 3. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test** (EY = earnings yield = 1 ÷ Forward PE)
```
EY     = 1 ÷ 8.00 = 12.50%
Spread = EY − 10Y Treasury = 12.50% − 4.46% = +8.04%
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** (+8.04%) → **no +5 additive.**

**Step 2 — Rate Regime Modifier**
10Y = 4.46% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for ADBE = +5**

---

## 4. Phase 02 — Full Score Calculation (every sub-score shown)

**FCF Yield — 40% weight** (FCF = free cash flow; yield = FCF ÷ market cap)
```
FCF_Score = clamp(100 × (1 − 13.25 / 10), 0, 100) = clamp(−32.5, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.40 = **0.0**

**EV/EBIT — 40% weight** (EV = enterprise value; EBIT = operating profit; PEG redistributed here — Gap #5)
```
EV/EBIT_Score = clamp((8.43 − 12) / 23 × 100, 0, 100) = clamp(−15.5, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.40 = **0.0**

**Forward PE (fallback formula, 5yr avg) — 20% weight**
```
Deviation% = (8.00 − 27.2) / 27.2 × 100 = −70.6%
FwdPE_Score = clamp(50 + (−70.6) × 2.5, 0, 100) = clamp(−126.5, 0, 100) = 0.0
```
(This fallback already folds in the Historical PE Modifier — no separate ±10 applied.)
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — not applicable** (not a Fast Grower — Gap #5). Weight redistributed to EV/EBIT above.

**Raw weighted score = 0.0 + 0.0 + 0.0 = 0.0**
**+ Rate Regime Modifier (+5) = 5.0**

---

## 5. Upside/Downside Modifier (Expected-Return Modifier) — REQUIRED, full calc

This folds the **forward** dimension (how much the position is actually expected to make) into the score. Built entirely from the fair-value work in §6 below (no new data source). Bear case underwritten honestly for AI disruption (see §7).

**Step 1 — Expected annual return `E`:**
```
PW Fair Value  = 0.25×Bull + 0.50×Base + 0.25×Bear
               = 0.25×$657.30 + 0.50×$443.72 + 0.25×$251.40  (DCF scenarios, §6)
               = $449.03   (DCF-only PW)
Blended FV (40% DCF / 60% multiples, §6) = $391.26   ← used as the PW fair-value anchor for the gap
Gap Upside %   = ($391.26 ÷ $195.16) − 1 = +100.5%
Catalyst window = 2.0 yr (Rule 10 default; catalyst = Digital Media growth holding ≥~10% over Q3/Q4 FY26 + multiple normalization — within the 18–24mo window)
Annualized gap = 100.5% ÷ 2 = +50.2%/yr
Intrinsic growth = +10%/yr  (conservative: rev CAGR 10.5%, non-GAAP EPS +14–16%, FCF growth strong — anchored to the lower revenue rate, not the rosier EPS rate)
Shareholder yield = +2%/yr  (no dividend; net buyback ≈ 1.6–2%/yr, share count 404M→397.5M)
E = 50.2% + 10% + 2% = +62.2%/yr
```

**Step 2 — Map `E` to modifier `M`** (hurdle H = 10%):
```
E (62.2%) ≥ H (10%)  →  M = −15 × clamp((62.2 − 10) / 15, 0, 1) = −15 × clamp(3.48, 0, 1) = −15 × 1 = −15.0
```
**Modifier M = −15.0** (hits the −15 floor — the annualized gap alone (+50%/yr) clears the +25% "full −15" threshold five-fold).

**Guardrails check:**
- Catalyst within 18–24mo? **Yes** (Q3 FY26 ~Sept-2026 / Q4 FY26 ~Dec-2026 Digital Media growth prints) → upside-side credit **not** capped at −5.
- Scenario-weighted (not the rosy point)? **Yes** — bear case ($251.40) underwritten with structural AI impairment (FCF growth ~1–2% fading toward zero, WACC 11.5%, de-rated terminal).
- **Robustness note:** even if the gap were ignored entirely (set annualized gap to 0), E = 10% + 2% = 12% > hurdle → M would still be negative. The modifier's sign is not sensitive to the (admittedly large) gap estimate.

---

## 6. Fair Value & Order Setup

### Step 1 — Fair Value (Blended), refreshed

Base FCF: TTM $10.28B (bear anchored to FY25 actual $9.9B, conservative). Net debt +$1.451B. Shares 397.5M.

**Method A: DCF (3-stage, 3 scenarios — Rule 2/7). Bear case hardened vs 12-Jun to test the melting-ice-cube hypothesis.**

| Scenario | WACC | Yrs1–5 FCF growth | Yrs6–10 fade | Terminal | TV weight | **FV/share** |
|---|---|---|---|---|---|---|
| **Bear** (AI structurally impairs moat) | 11.5% | ~2% | 1.5%→0.5% | 1.5% | 39% | **$251.40** |
| **Base** (consensus, moat holds) | 10.5% | ~7% | 6%→4% | 3.0% | 52% | **$443.72** |
| **Bull** (Firefly/AI monetization re-rates) | 9.5% | ~9% | 7.5%→5.5% | 4.0% | 63% | **$657.30** |

```
PW DCF FV = 0.25×657.30 + 0.50×443.72 + 0.25×251.40 = $449.03
```
TV (terminal value) weight is 39–63% — under the 75% Rule-4 trigger to extend Stage 2. **Key finding: even the hardened bear case ($251.40) sits ABOVE the live price ($195.16).** A DCF that has to assume near-zero perpetual FCF growth *and a de-rate* to approach today's price is the signature of a cheap compounder being priced as a melting ice cube — not of a business whose fundamentals are actually melting (FY26 revenue guided to *accelerate*, FCF at record TTM $10.28B, margins near record).

**Method B: Comparable Multiples** (all "fair" multiples deliberately discounted well below ADBE's own 5yr-avg 27.2×)

| Approach | Fair multiple | FV/share |
|---|---|---|
| Forward PE comp | 15× × $24.40 | $366.00 |
| EV/EBIT comp | 14× × TTM EBIT $9.372B, less net debt | $326.43 |
| FCF-yield comp | 7% yield (≈14.3× EV/FCF) on TTM FCF $10.28B | $365.80 |
| **Multiples avg** | | **$352.74** |

**Triangulation:**
```
Blended FV = 0.40 × DCF(PW) $449.03 + 0.60 × Multiples $352.74 = $391.26
```
Cross-check vs external: blended FV ($391) is above the analyst mean PT ($282) and median ($250) — expected, since 12-month PTs embed near-term sentiment/multiple caution on the AI overhang, while a DCF reflects longer-run cash generation. Directionally consistent (consensus PT < blended intrinsic FV). The blend is also slightly *below* 12-Jun's $401.06, reflecting the harder bear case and the lower 5yr-avg multiple anchor — i.e. this rescore is more conservative on FV than the entry, yet the gap is *larger* because price fell.

### Step 2–6 — Order setup (MoS = margin of safety; R/R = reward-to-risk)
```
Margin of Safety = 17.5% (midpoint of 15–20% band for Score 0.0–29.9)
Buy Price (ceiling)   = $391.26 × (1 − 0.175) = $322.79   → live $195.16 is far below → ENTER NOW
Primary Sell Target   = Blended FV            = $391.26
Bull-Case Trim Target = Bull DCF $657.30 × 0.90 = $591.57
Stop Loss             = $195.16 × (1 − 0.225) = $151.25   (22.5% max loss, midpoint 20–25% band)
R/R = (391.26 − 195.16) ÷ (195.16 − 151.25) = 196.10 ÷ 43.91 = 4.47 : 1   (≥ 2:1 ✓)
```

### Position sizing — top-up toward the partial-fill target
```
Portfolio Value (combined, holdings.md) = $53,659.11
Max $ Risk (1.5%) = $804.89 ; Risk/share = $43.91 → risk-based full size = 18.3 sh
Target (12-Jun) = ~17 sh ; held = 10 sh → TOP-UP = 7 sh
Top-up cost = 7 × $195.16 = $1,366.12  (+2.55% of portfolio)
Resulting position: 17 sh × $195.16 = $3,317.72 = 6.18% of portfolio
```
**Cap cross-check:** full 17-sh position = 6.18% → within the 6–8% Very Cheap band, far under the 15% hard cap (Upgrade 7). Risk-based size (18.3 sh) ≥ target (17 sh), so the 17-sh target governs. **No cap breach.**

### Order Setup Checklist
```
[x] Valuation Score (incl. Upside/Downside Mod): 0.0   (≤ 49.9 ✓)
[x] Expected annual return E / catalyst window:  +62.2% / 2 yr
[x] Upside/Downside Modifier applied:            −15.0
[x] DCF Fair Value (PW):                         $449.03
[x] Multiples-Based Fair Value:                  $352.74
[x] Blended Fair Value:                          $391.26
[x] Margin of Safety %:                          17.5%
[x] BUY PRICE (ceiling; live already far below):  $322.79
[x] PRIMARY SELL TARGET:                          $391.26
[x] BULL-CASE TRIM TARGET:                         $591.57
[x] STOP LOSS:                                     $151.25
[x] Risk/Reward Ratio:                             4.47:1  (≥ 2:1 ✓)
[x] Max $ Risk:                                    $804.89
[x] POSITION SIZE (top-up shares):                 7 (to reach ~17-sh target)
[x] POSITION SIZE ($):                             $1,366.12 top-up → 6.18% total
[x] Thesis invalidation triggers:                  see §8
```

---

## 7. Bear Case — Cheap Compounder vs Melting Ice Cube (the central question)

The whole ADBE thesis rests on one question: **does generative AI structurally impair the Creative Cloud moat?** Underwriting it honestly:

**The bear (melting ice cube) case:** Free/cheap GenAI image & video tools (Midjourney, Sora, Canva, OpenAI native generation) commoditize core creative functionality. New creators never enter the Adobe ecosystem; prosumers/SMBs churn out; pricing power erodes; seat growth stalls. In the DCF this is the $251 bear scenario — FCF growth collapses to ~1–2% then fades toward zero, with a de-rate (WACC 11.5%, terminal 1.5%).

**Why the evidence still points to cheap-compounder, not melting ice cube:**
1. **Fundamentals are not melting.** FY26 revenue is *guided to accelerate* (~+12%); TTM FCF is at a record $10.28B; gross margin 89.4%, net margin 30%, FCF/NI conversion 142% — none of these is what a disrupted franchise looks like *yet*.
2. **The bear DCF still clears the price.** It takes near-zero perpetual FCF growth *plus* a de-rate to drag fair value ($251) anywhere near today's $195 — and even that doesn't get below it. The market is pricing in something worse than the honest bear case.
3. **Firefly is a moat-extension, not just a victim.** Adobe's enterprise AI traction is built on what raw GenAI tools can't offer — commercially-safe training data, IP indemnification, native integration into existing professional workflows. That is precisely the defensible layer.
4. **Capital discipline intact** — continuing net buybacks (404M→397.5M shares), walked away from the $20B Figma deal rather than overpay.

**The honest caveat:** this is a *live, unsettled* debate, not a closed case — which is exactly why (a) the bear scenario carries a real 25% weight and was hardened this session, (b) MoS and stop were set at band midpoints not the aggressive ends, and (c) the catalyst below is a *falsifiable* fundamental test, not a vibe. **Monitoring item:** the net-cash→net-debt flip (buybacks may be partly debt-funded) — benign at 0.15× net debt/EBITDA, but watch it doesn't become a way to flatter EPS while the business decelerates.

**Catalyst & timeline (Rule 10):** the gap closes — or the thesis breaks — on whether **Digital Media segment revenue growth holds ≥~10%** over Q3 FY2026 (~Sept 2026) and Q4 FY2026 (~Dec 2026). Holding ≥10% → multiple normalizes off distressed levels (re-rate, the main driver of the +50%/yr annualized gap). Decelerating toward mid-single-digits without a non-AI explanation → converts narrative risk into fundamental risk → Rule 9 immediate re-score and likely Phase 06 review.

---

## 8. Final Score, Action & Recommendation

# Final Score: 0.0 (raw 0.0 + Rate +5 + Upside/Downside −15 = −10, clamped to the 0.0 floor)

| | Prior (12-Jun) | This rescore (20-Jun) |
|---|---|---|
| Raw weighted | 0.0 | 0.0 |
| Rate Regime Modifier | +5 | +5 |
| Upside/Downside Modifier | (did not exist) | **−15.0** |
| **Final Score** | **5.0** | **0.0** |
| Action band | BUY — Very Cheap (0.0–29.9) | BUY — Very Cheap (0.0–29.9) |

**Action band: UNCHANGED** — both 5.0 and 0.0 fall in the 0.0–29.9 "Very Cheap → Full position 6–8%" BUY band. The new Upside/Downside Modifier pushed the score from 5.0 to the absolute 0.0 floor: ADBE is not merely cheap on trailing multiples, it carries a very large expected forward return (E = +62%/yr, dominated by a ~100% gap to a *conservatively-blended* fair value). This is the modifier behaving exactly as designed — confirming a genuine cheap compounder rather than re-rating it down.

**Thesis invalidation triggers (Phase 06 / stop):**
- Digital Media revenue growth decelerates toward mid-single-digits without a non-AI one-off cause (2 consecutive quarters) → thesis broken
- Gross margin falls >3pp structurally, or FCF/NI conversion <70% for 2 consecutive quarters
- Net debt/EBITDA rising materially on debt-funded buybacks while growth slows
- Price through the $151.25 stop

---

## 9. Recommendation

# **CONFIRMED BUY — top up ~7 shares (~$1,366, to reach the ~17-sh / 6.18% target). Score 0.0 ("Very Cheap").**

ADBE is a **partially-filled** position (10 of ~17 target shares), so unlike the already-full holdings this is **actionable**: a fresh buy toward the target is warranted. R/R is 4.47:1 (well clear of 2:1), the full 17-sh position (6.18%) sits inside the 6–8% band and far under the 15% cap, and live price ($195.16) is far below even the discounted buy ceiling ($322.79). The buy rests on bottom-up cheapness (every sub-score clamps to 0) plus a large, catalyst-backed expected return — **not** on the price drop since 12-Jun (price drift on an intact thesis is not an action trigger). All final-decision authority rests with the human investor; funding is the investor's call (combined cash + XEON comfortably covers a ~$1.4K top-up).

---

## 10. Next Review Trigger

- **Q3 FY2026 earnings (~mid-Sept 2026)** — mandatory re-score (Rule 9). Check Digital Media segment growth ≥~10% (the §7 catalyst).
- **Permanent CFO appointment** — watch for strategy/cost-discipline signal (management-change Rule 9 trigger).
- **>15% unexplained move from $195.16** in either direction — immediate re-score (Rule 9).
- **If the top-up is executed**, log it in [decisions/](../decisions/) and reflect at the next `/sync-portfolio` (holdings.md is handled by the orchestrator, not this session).

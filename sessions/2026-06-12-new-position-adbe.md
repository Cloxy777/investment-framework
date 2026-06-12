# NEW POSITION — ADBE (Adobe Inc.) — 2026-06-12

**Task type:** NEW POSITION
**Date:** 12 Jun 2026
**10Y US Treasury Yield:** 4.52% (TradingEconomics/CNBC, 11–12 Jun 2026)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current ADBE portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md))
**Sector:** Technology — Software (Creative/Content Applications — Digital Media segment — and Digital Experience / marketing cloud)

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$207.30** | IBKR `get_price_snapshot`, intraday last trade (`is_close: false`), **−$11.50 / −5.26%** vs prior close |
| 52-week high / open-52w-ago | $405.00 / $411.43 | IBKR `misc-statistics` |
| 52-week low (per IBKR stats) | $218.09 | IBKR `misc-statistics` — **note: today's $207.30 is *below* this figure**, i.e. today's drop appears to have pushed ADBE to a fresh 52-week low that the snapshot's daily-refreshed stats haven't caught up to yet |
| Analyst consensus PT | ~$329 ("Buy", 38 analysts, S&P Global aggregation via GuruFocus) | WebSearch |
| Independent model target (context) | ~$392 (TIKR intrinsic-value model, cited vs. analyst $327 consensus) | [TIKR blog](https://www.tikr.com/blog/adobe-stock-analysis-why-analysts-priced-it-at-327-while-tikr-model-targets-392) |

**Context:** ADBE is down ~50% from its 52-week high ($405) and ~50% from where it traded a year ago (open-52w $411.43), despite **beating Q2 FY2026 estimates and raising full-year guidance** the same day. The −5.26% drop today is attributed in financial press to the **CFO's announced departure** (Dan Durn), compounding an already-depressed multiple driven by a year-long "AI disruption" narrative around Adobe's Creative Cloud franchise. This is a textbook case for Rule 0 — the price action and the fundamentals are telling different stories, and only a live price pull (not an inferred one) lets us see the gap.

---

## 2. Data Gathered (Phase 01 + Phase 02 Inputs) & Gaps Flagged

| Metric | Value | Source / Derivation |
|---|---|---|
| FY2025 Revenue (FY ended 28 Nov 2025) | $23.77B (+11% YoY) | Adobe FY2025 results (WebSearch aggregation of 10-K/8-K coverage) |
| FY2024 Revenue | $21.51B | Same |
| FY2023 Revenue | $19.41B | Same |
| FY2022 Revenue | $17.61B | Same |
| **Revenue CAGR 3yr** (FY2022→FY2025) | **10.52%** = (23.77/17.61)^(1/3) − 1 | Computed |
| FY2025 Net income | $7.13B (+28% YoY) | WebSearch aggregation |
| FY2025 Net margin | **30.0%** (7.13/23.77) | Computed |
| FY2025 Gross margin | **89.3%** | WebSearch aggregation |
| FY2025 GAAP Operating margin | **36.6%** → GAAP EBIT (FY2025) ≈ **$8.70B** (23.77 × 36.6%) | WebSearch aggregation; EBIT figure derived |
| ROIC | 26.07% (GuruFocus, Feb 2026 snapshot) / TTM 41.1% / 3yr avg 33.4% / 5yr avg 34.4% (ValueSense) | WebSearch — wide range but **all well above 15%** |
| FY2025 OCF | $10.03B | WebSearch aggregation |
| FY2025 CapEx | $0.179B | WebSearch aggregation |
| **FY2025 FCF** | **$9.9B** = $10.03B − $0.179B | Computed |
| FCF/NI conversion (FY2025) | **138.8%** ($9.9B / $7.13B) | Computed — well above 70% threshold |
| Total debt (Q1 FY2026, 10-Q) | $6.228B | WebSearch aggregation |
| Cash + ST investments | $6.9B | WebSearch aggregation |
| **Net debt** | **−$0.672B** (net cash position) | Computed |
| Shares outstanding (~mid-Jun 2026) | ~404.2M | WebSearch aggregation |
| **Market Cap** | 404.2M × $207.30 = **$83.79B** | Computed |
| **Enterprise Value** | $83.79B + (−$0.672B) = **$83.118B** | Computed |
| Q1 FY2025 GAAP operating income | $2.16B | WebSearch (8-K) |
| Q2 FY2025 GAAP operating income | $2.11B | WebSearch (8-K) |
| Q1 FY2026 GAAP operating income | $2.42B | WebSearch (8-K) |
| Q2 FY2026 GAAP operating income | $2.24B | WebSearch (8-K, 11 Jun 2026) |
| **TTM EBIT** | $8.70B − $2.16B − $2.11B + $2.42B + $2.24B = **$9.09B** | Computed (roll-forward) |
| **EV/EBIT** | $83.118B / $9.09B = **9.14×** | Computed |
| **FCF Yield** | $9.9B / $83.79B = **11.81%** | Computed |
| FY2026 guidance (raised today) | Revenue $26.50–26.60B, non-GAAP EPS $24.35–24.45 | Adobe Q2 FY2026 earnings release, 11 Jun 2026 |
| **Forward PE** | $207.30 / $24.40 (FY26 guidance midpoint) = **8.50×** | Computed |
| Non-GAAP EPS: FY2023→24 | +14.6% ($16.07 → $18.42) | WebSearch aggregation |
| Non-GAAP EPS: FY2024→25 | +13.7% ($18.42 → $20.94) | WebSearch aggregation |
| Non-GAAP EPS: FY2025→26 (guided) | +16.6% ($20.94 → $24.40 midpoint) | Computed from above |
| 10yr avg PE (trailing, GAAP basis) | **44.58×** (primary) / 35.72× (alt source) — both internally consistent with "current PE 13.58× = ~70% below historical avg" | WebSearch (fullratio/wisesheets-style aggregation) |

### Data Gaps / Flags

1. **EBIT and FCF are FY2025-actual + a quarterly roll-forward, not a single clean TTM source** — every component (FY2025 totals, Q1/Q2 FY25, Q1/Q2 FY26) is individually sourced from Adobe's own 8-K earnings releases, but the FY2025 EBIT figure itself is *derived* from a reported 36.6% operating-margin figure rather than a directly-stated $ EBIT. Sensitivity: even at a 10% haircut to TTM EBIT ($8.18B), EV/EBIT = 10.16× — still under the 12× floor → EV/EBIT_Score still 0.0. **Doesn't change the score.**
2. **10yr avg PE has a source discrepancy (44.58× vs 35.72×).** Both are GAAP-basis. Used 44.58× as primary (cross-checked against GuruFocus's "current PE 13.58× is ~70% below historical avg" → implied avg ≈45.3×, closest to 44.58×). Sensitivity at 35.72×: Deviation% = (8.50−35.72)/35.72×100 = −76.2% → FwdPE_Score still clamps to 0.0. **Doesn't change the score.**
3. **Forward PE basis: used FY2026 (current-FY) guidance midpoint, not a "next fiscal year" consensus.** FY2027 consensus EPS estimates found ranged wildly ($21.63–$25.96, a >20% spread across sources) — too inconsistent to use without effectively guessing. FY2026 guidance ($24.35–24.45) was raised *today* and is the freshest, most authoritative figure available, even though >50% of FY2026 is still unreported. Sensitivity: the pre-raise "Forward PE 10.03×" figure (from GuruFocus, ~9 Jun) gives Deviation% = (10.03−44.58)/44.58×100 = −77.5% → FwdPE_Score still 0.0. **Doesn't change the score.**
4. **FCF positive "3 consecutive years"** — FY2025 ($9.9B) is directly sourced. FY2023/FY2024 FCF were not individually re-pulled this session, but Adobe's OCF has been described as "record" in every annual release for several years running, and its capex (~$180–200M/yr on ~$20–24B revenue) is immaterial — there is no plausible scenario in which FY2023/24 FCF were negative. Treated as a pass on the weight of this evidence rather than inventing specific figures.
5. **PEG / Fast Grower test:** non-GAAP EPS growth was +17% (FY2023), +14.6% (FY2024), +13.7% (FY2025), and is guided to +16.6% for FY2026. This does **not** satisfy ">15% for 3+ *consecutive* years" (the two most-recently-completed years are both <15%) — **ADBE classified as NOT a Fast Grower**. PEG's 15% weight is redistributed to EV/EBIT (→ 40%), per the Final Score Formula note.

---

## 3. Phase 01 — Quality Gate

| Check | ADBE Value | Threshold | Result |
|---|---|---|---|
| Net margin (FY2025) | 30.0% | >15% | ✅ PASS |
| ROIC | 26–41% (range across sources) | >15% | ✅ PASS |
| Revenue CAGR 3yr (FY2022→FY2025) | 10.52% | >10% | ✅ PASS (modest margin) |
| Gross margin | 89.3% | >40% | ✅ PASS |
| FCF positive 3 consecutive years | FY2025 $9.9B confirmed; FY2023/24 inferred (see Gap #4) | required | ✅ PASS |
| Net debt/EBITDA | Net **cash** position (−$0.672B) | <2x | ✅ PASS |
| FCF/NI conversion ratio | 138.8% (FY2025) | >70% | ✅ PASS |
| Share issuance pattern | Net buybacks (shares outstanding declining), non-dilutive | not dilutive | ✅ PASS |
| Moat signal | ~90%+ share in professional creative software (Photoshop/Premiere/Illustrator), high switching costs, expanding Digital Experience (marketing cloud) | required | ✅ Qualitatively strong |

**Gate result: PASS — proceeding to Rate Environment Gate and Phase 02.**

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 8.50 = 11.7647%
Spread = EY − 10Y Treasury = 11.7647% − 4.52% = +7.2447%
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** (+7.24%, comfortably clear) → **no +5 additive**.

**Step 2 — Rate Regime Modifier**
10Y = 4.52% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for ADBE = +5**

---

## 5. Phase 02 — Full Score Calculation

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 11.81 / 10), 0, 100)
          = clamp(100 × (1 − 1.181), 0, 100)
          = clamp(−18.1, 0, 100)
          = 0.0
```
→ Contribution: 0.0 × 0.40 = **0.0**

**EV/EBIT — weight 40% (PEG not applicable, redistributed — see Gap #5)**
```
EV/EBIT_Score = clamp((9.14 − 12) / 23 × 100, 0, 100)
              = clamp(−12.43, 0, 100)
              = 0.0
```
→ Contribution: 0.0 × 0.40 = **0.0**

**Forward PE (fallback formula) — 20% weight**
```
Deviation% = (8.50 − 44.58) / 44.58 × 100 = −80.93%
FwdPE_Score = clamp(50 + (−80.93) × 2.5, 0, 100)
            = clamp(50 − 202.32, 0, 100)
            = clamp(−152.32, 0, 100)
            = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — not applicable (not a Fast Grower, see Gap #5).** Weight redistributed to EV/EBIT above.

**Raw weighted score:**
```
= 0.0 + 0.0 + 0.0 = 0.0
```
**+ Rate Modifier (+5) = 5.0**

Boundary rule: not a ".X5" → standard rounding → **Final Score = 5.0**

---

## 6. Final Score & Action

# Final Score: 5.0 → Action: BUY — Full position 6–8% ("Very Cheap")

Every sub-score independently clamps to its cheapest extreme (0.0):
- FCF yield (11.81%) is above the ≥10% "free" threshold — Adobe is generating cash at nearly 12 cents per dollar of market cap.
- EV/EBIT (9.14×) is below the 12× floor of the scoring scale entirely.
- Forward PE (8.50×) sits ~81% below Adobe's own 10-year average PE (44.58×) — the steepest discount-to-history of any name evaluated under this framework so far.

A score of **5.0** is among the lowest (cheapest) this framework has produced. This is **not** a case of a deteriorating business trading at a "deserved" discount — Phase 01 passes cleanly across the board, revenue grew +11% YoY with **raised** guidance announced *the same day* the stock fell 5.26%. The gap between price and fundamentals is the entire story here (see §8, Qualitative Assessment, for the disruption-narrative discussion that explains *why* this gap exists).

---

## 7. Fair Value & Order Setup

### Step 1 — Fair Value (Blended)

**Method A: DCF (3 scenarios, Rule 2/7)**

Base FCF: $9.9B (FY2025 actual). Net cash: +$0.672B. Shares: 404.2M.

| Scenario | WACC | Yrs 1–5 FCF growth (avg) | Yrs 6–10 fade | Terminal growth | PV Stage 1 | PV Stage 2 | PV Terminal | Total EV | Equity Value | **FV/share** |
|---|---|---|---|---|---|---|---|---|---|---|
| Bear | 11.5% | ~6% (7→5%) | 4.5%→2.5% | 2.0% | $43.04B | $31.20B | $56.85B | $131.09B | $131.76B | **$326.04** |
| Base | 10.5% | ~7% (8→6%) | 5.5%→3.5% | 3.0% | $45.42B | $36.12B | $87.57B | $169.11B | $169.78B | **$420.04** |
| Bull | 9.5% | ~8% (9→7%) | 6.5%→4.5% | 4.0% | $46.93B | $41.74B | $144.92B | $233.59B | $234.26B | **$579.59** |

WACC base = risk-free (4.52%) + β≈1.3 × ERP≈4.5% ≈ 10.4%, rounded to 10.5%; bull/bear vary WACC ∓1% and growth ±1pp per Rule 2. Terminal value is 52–62% of total EV across scenarios — under the 75% trigger for extending Stage 2 (Rule 4).

```
PW DCF FV = 0.25 × Bull + 0.50 × Base + 0.25 × Bear
          = 0.25×579.59 + 0.50×420.04 + 0.25×326.04
          = 144.90 + 210.02 + 81.51
          = $436.43
```

**Method B: Comparable Multiples**

| Approach | "Fair" multiple (heavily discounted from ADBE's own 10yr history) | Calculation | FV/share |
|---|---|---|---|
| Forward PE comp | 17× (vs current 8.50×, vs 10yr avg 44.58×) | 17 × $24.40 | **$414.80** |
| EV/EBIT comp | 15× TTM EBIT $9.09B (vs current 9.14×) | EV $136.35B + net cash → equity $137.02B ÷ 404.2M | **$339.04** |
| FCF-yield comp | 6.5% yield (≈15.4× EV/FCF) on FCF $9.9B (vs current 11.81%/8.5×) | EV $152.31B + net cash → equity $152.98B ÷ 404.2M | **$378.62** |
| **Multiples avg** | | | **$377.49** |

**Historical PE cross-check (Rule 3, context only — not weighted into blend):**
```
Historical PE FV = Current GAAP TTM EPS ($17.18) × 10yr avg PE (44.58) ≈ $766
```
This implies the market is paying ~4.5× less per dollar of GAAP earnings than its own 10-year norm — confirms the scale of the discount but is too extreme to be a usable point estimate (would imply >270% upside; fails Rule 4's "reasonable IRR" sanity check as a standalone number). Shown for context only, **0% weight**.

**Triangulation:**
```
Blended FV = 40% × DCF(PW) + 60% × Multiples(avg)
           = 0.40 × $436.43 + 0.60 × $377.49
           = $174.57 + $226.49
           = $401.06
```

**Cross-check vs. external estimates:** Blended FV ($401) sits close to the independent TIKR intrinsic-value model (~$392) and above the current analyst-consensus 12-month PT (~$329) — consensus PTs typically embed near-term sentiment/multiple assumptions, while a DCF/intrinsic model reflects longer-run fundamentals. The ordering (consensus PT < TIKR model < our blended FV) is directionally consistent.

**Reverse-DCF sanity check (Rule 10 — "why does the gap exist?"):** at WACC 10.5%, the current $207.30 price is roughly consistent with the market pricing in **perpetually *declining* FCF (~−2%/yr forever)** — i.e., the market is pricing ADBE as a structurally-impaired business, not merely a slower-growing one. Given FY2025 revenue +11% and FY2026 guidance just *raised*, this looks like a case where the bearish AI-disruption **narrative** has outrun the **fundamentals** — see §8.

---

### Step 2 — Buy Price

```
Buy Price = Blended FV × (1 − MoS%)
MoS = 17.5% (midpoint of the 15–20% band for Score 0.0–29.9)
Buy Price = $401.06 × (1 − 0.175) = $330.87
```

Current price ($207.30) is **far below** the buy price ($330.87) → **Enter now** (Score 0.0–29.9 + price at/below buy price).

### Step 3 — Sell Targets

```
Primary Sell Target   = Blended FV = $401.06
Bull-Case Trim Target = Bull DCF FV × 0.90 = $579.59 × 0.90 = $521.63
```

### Step 4 — Stop Loss

```
Stop Loss = Entry Price × (1 − Max Acceptable Loss%)
Max Acceptable Loss = 22.5% (midpoint of 20–25% band for Score 0.0–29.9)
Stop Loss = $207.30 × (1 − 0.225) = $160.66
```

### Step 5 — Position Size

```
Portfolio Value (combined, per holdings.md) = $53,855.83
Max $ Risk = Portfolio × 1.5% = $807.84
Risk Per Share = Entry − Stop = $207.30 − $160.66 = $46.64
Shares (risk-based) = $807.84 ÷ $46.64 = 17.32 → 17 shares
Position Size ($) = 17 × $207.30 = $3,524.10
Position Size (% of portfolio) = $3,524.10 ÷ $53,855.83 = 6.54%
```

**Cross-check against caps:** 6.54% falls within the 6–8% allocation cap for Score 0.0–29.9, and far under the 15% hard cap (Upgrade 7). **No cap breach.**

### Step 6 — Risk/Reward

```
R/R = (Sell Target − Entry) ÷ (Entry − Stop Loss)
    = ($401.06 − $207.30) ÷ ($207.30 − $160.66)
    = $193.76 ÷ $46.64
    = 4.16 : 1
```
Well above the 2:1 minimum. ✅

### Order Setup Checklist

```
[x] Valuation Score:                         5.0   (≤ 49.9 ✓)
[x] DCF Fair Value (PW):                     $436.43
[x] Multiples-Based Fair Value:              $377.49
[x] Blended Fair Value:                      $401.06
[x] Margin of Safety %:                      17.5%
[x] BUY PRICE (ceiling; current price already below):  $330.87
[x] PRIMARY SELL TARGET:                     $401.06
[x] BULL-CASE TRIM TARGET:                   $521.63
[x] STOP LOSS:                               $160.66
[x] Risk/Reward Ratio:                       4.16:1  (≥ 2:1 ✓)
[x] Max $ Risk:                              $807.84
[x] POSITION SIZE (shares):                  17
[x] POSITION SIZE ($):                       $3,524.10 (6.54% of portfolio)
[x] Thesis invalidation triggers:            see §9
```

---

## 8. Qualitative Assessment (5 Questions + Disruption Vector Check)

1. **Why are margins high?** Dominant (~90%+) share of professional creative-software workflows (Photoshop, Premiere, Illustrator, InDesign), nearly all-subscription (Creative Cloud) revenue, extremely high switching costs (file formats, plugin ecosystems, institutional training/certification), and a second growing profit pool in Digital Experience (enterprise marketing/analytics — higher-touch, higher-margin).

2. **What would it take to compete?** A challenger would need a comparably deep professional tool suite, an integrated plugin/ecosystem, enterprise trust (security, compliance, IP indemnification), and to dislodge workflows/training embedded across the entire creative industry — historically a multi-year, capital-intensive undertaking (Adobe has out-competed or absorbed prior challengers like Macromedia, Corel).

3. **Capital allocation track record:** Disciplined — consistent net share buybacks (share count declining toward ~404M), no dividend (cash redeployed into buybacks/R&D, ~17–18% of revenue), and notably **walked away** from the $20B Figma acquisition in 2023 once the regulatory environment turned, rather than fighting an unwinnable battle — a positive discipline signal.

4. **Growth sources, next 3–5 years:** (a) Firefly/GenAI monetization — 6M+ monthly active users, enterprise contracts ~61% of Firefly revenue, AI-credit upsell layered on existing subscriptions; (b) continued Digital Experience (marketing cloud) expansion; (c) AI-agent-based enterprise products recently announced; (d) FY2026 guidance of $26.5–26.6B implies growth *accelerating* slightly to ~11.7% from FY2025's 11%.

5. **Best bear case:** Generative AI tools (Midjourney, Sora, Canva, OpenAI's native image/video tools, and free/cheap alternatives) commoditize core creative-tool functionality, allowing prosumers/SMBs and especially **new** creators who never adopted Adobe's ecosystem to bypass Creative Cloud entirely — pressuring seat counts and pricing power over time. The same-day CFO departure adds leadership-transition uncertainty on top of this.

6. **Disruption vector check (the central question for ADBE right now):** This is genuinely the most contested "is the moat structurally impaired by a new technology" debate in large-cap tech, and it is the documented reason ADBE trades at ~81% below its own 10-year average multiple. The evidence gathered this session leans toward "narrative has outrun fundamentals so far": Firefly's enterprise traction is built specifically around the things raw GenAI tools *can't* offer (commercial-safe training data, IP indemnification, native integration into existing professional workflows) — exactly the moat-extension Adobe would need. Revenue growth has **not** decelerated (it's guided to *accelerate* slightly), margins remain near record highs, and FCF continues to grow. **However**, this is a real, live thesis-risk — not a settled question — and the position sizing/MoS/stop-loss choices above (midpoint of each range, not the most aggressive end) reflect that genuine uncertainty.

**Catalyst & timeline (Rule 10):** the gap should close — or the thesis should be revisited — based on whether **Digital Media segment revenue growth holds at or above ~10%** over the next 2–3 quarters (Q3 FY2026 ~Sept 2026, Q4 FY2026 ~Dec 2026, Q1 FY2027 ~Mar 2027). If Firefly/AI monetization continues to show up as a net *retention and upsell* tool (current trajectory), the multiple has room to normalize meaningfully even without reverting anywhere near the 10-year average. If Digital Media growth instead decelerates materially (e.g., toward mid-single-digits) without a clear non-AI explanation, that would convert the "narrative" risk into a "fundamental" one — a Rule 9 trigger for an immediate re-score.

---

## 9. Recommendation

# **ENTER NOW — BUY ~17 shares (~$3,524.10, ~6.54% of portfolio)**

This is a **Score 5.0 ("Very Cheap")** — Phase 01 passes cleanly (30% net margins, 26–41% ROIC, net-cash balance sheet, 89% gross margins, FCF/NI conversion >138%), and every Phase 02 sub-score independently lands at its cheapest extreme: FCF yield 11.81% (clamps the 40%-weighted FCF score to 0), EV/EBIT 9.14× (below the 12× floor, clamps the 40%-weighted score to 0), and Forward PE 8.50× sitting ~81% below ADBE's own 10-year average PE (clamps the 20%-weighted score to 0). The +5 Rate Regime Modifier is the *only* nonzero contributor to the final score.

Current price ($207.30) is far below even the discounted Buy Price ceiling ($330.87), and R/R is 4.16:1 — well clear of the 2:1 minimum.

The size of this gap is driven almost entirely by a **narrative** (AI-disruption fear for Creative Cloud, compounded today by a CFO departure) rather than by any **fundamental** deterioration — FY2026 guidance was *raised* on the same day the stock fell. Per the framework's own non-negotiables ("price dropped on intact thesis... NOT valid [as a reason not to act]," and "act only on documented triggers — a valuation-score change or fundamental event, never price movement alone"), a 5.26% single-day drop driven by a leadership change, against a backdrop of accelerating guidance, is not in itself a reason to *avoid* an entry that the bottom-up numbers otherwise strongly support.

**That said — this is flagged as the most extreme reading this framework has produced, sitting on top of a genuinely live "is the moat AI-proof" debate (§8.6).** The MoS (17.5%) and stop-loss (22.5%) were set at the midpoints of their respective ranges rather than the most aggressive ends, in recognition of that real uncertainty. All final-decision authority rests with the human investor per the operating brief.

**Funding:** combined cash (IBKR $2,326.77 + Freedom24 $106.85 ≈ $2,433.62, ~4.5% of portfolio) plus XEON (cash-equivalent, $1,722.12, ~3.2%) ≈ $4,155.74 (~7.7%) — sufficient to fund the ~6.54% position ($3,524.10) without requiring a trim of any existing holding. No portfolio rebalancing action proposed in this session; funding-source choice is the human investor's call.

---

## 10. Next Review Trigger

- **Q3 FY2026 earnings** (expected ~mid-September 2026) — mandatory re-score (Rule 9). Specifically check whether **Digital Media segment revenue growth** holds ≥~10% (per §8.6 catalyst/timeline).
- **CFO transition** — watch for the permanent CFO appointment and any associated strategy/cost-discipline commentary (management-change Rule 9 trigger — re-score + thesis review if a new CFO signals a strategic shift).
- **>15% unexplained price move from $207.30 in either direction** — immediate re-score per Rule 9.
- **If a position is opened, log it in [decisions/](../decisions/)** per CLAUDE.md Rule 10.

**No position opened by this session — recommendation only.** If the human investor executes this trade, log it in `decisions/2026-06-12-...-adbe.md` and update [holdings.md](../portfolio/holdings.md) at the next `/sync-portfolio`.

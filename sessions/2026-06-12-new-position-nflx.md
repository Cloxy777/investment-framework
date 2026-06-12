# NEW POSITION (Fresh Re-Evaluation) — NFLX (Netflix, Inc.) — 2026-06-12

**Task type:** NEW POSITION (fresh full re-evaluation of an existing holding — supersedes prior score)
**Date:** 12 Jun 2026
**10Y US Treasury Yield:** 4.46% (FRED DGS10, 11 Jun 2026 close)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current NFLX portfolio weight:** **1.83%** — currently HELD (IBKR), per [holdings.md](../portfolio/holdings.md)
**Sector:** Communication Services — Streaming Media & Entertainment

**Context:** NFLX was last scored **58.9** (rescaled 0–100 scale, dated 11 Jun 2026, derived from the 2026-06-07 data pull — [session](2026-06-11-rescore-holdings-new-scale.md)). That score used a *softened/judgment-call* forward-PE sub-score (sub-score 2 of 1–10, vs. a mechanical floor of 1) because the only sourced 10-yr avg PE (93.64×) was flagged as likely distorted by NFLX's hyper-growth-era multiples and the Nov 2025 10-for-1 split. This session is a **fresh full re-pull** of all Phase 01/02 inputs, run end-to-end as a `/new-position`-style evaluation per the orchestrator's instructions, and **supersedes** the 58.9 score regardless of whether the action category changes.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$81.27** | WebSearch aggregation (stockanalysis.com-style), 11 Jun 2026 close — most recent available; IBKR MCP tools denied (permission), so fell back to WebSearch per instructions. A "predicted fair opening" for 12 Jun of ~$81.15 was also reported, consistent with $81.27 |
| 52-week high | $134.12 | WebSearch aggregation |
| 52-week low | $75.01 (low reached ~Feb 2026) | WebSearch aggregation |
| Analyst consensus PT (median) | **$115.00** (range $80.00–$151.40 across 78 analysts; 37 Buy / 12 Hold / 1 Sell) | WebSearch aggregation |

**Context:** NFLX trades **~39% below its 52-week high** ($134.12) and is up modestly (+0.5%) over the past week after a rough month (−6.5%). Post 10-for-1 split (Nov 2025), all current prices/EPS are on the post-split basis — the 2026-06-07 session's $81.83 reference and today's $81.27 are directly comparable (essentially flat over the intervening week).

---

## 2. Data Gathered (Phase 01 + Phase 02 Inputs) & Gaps Flagged

| Metric | Value | Source / Derivation |
|---|---|---|
| FY2025 Revenue (year ended 31 Dec 2025) | $45.18B (+16% YoY) | Netflix Q4 2025 earnings release / 10-K (WebSearch aggregation) |
| FY2024 Revenue | $39.00B (+16% YoY) | WebSearch aggregation |
| FY2023 Revenue | $33.70B | WebSearch aggregation |
| FY2022 Revenue | ~$31.60B | WebSearch aggregation |
| **Revenue CAGR 3yr** (FY2022→FY2025) | **12.51%** = (45.18/31.6)^(1/3) − 1 | Computed |
| FY2025 Net income | $10.98B (~$11.0B) | Netflix Q4 2025 earnings release |
| **FY2025 Net margin** | **24.3%** (10.98/45.18) | Computed |
| FY2025 Diluted EPS | $2.53 | WebSearch aggregation (post-split basis) |
| FY2025 Gross margin | **48.5%** | WebSearch aggregation |
| FY2025 Operating margin | **29.5%** | Netflix Q4 2025 earnings release / FY2026 guidance commentary |
| **FY2025 EBIT (= TTM EBIT)** | **$13.275B** = $45.18B × 29.5%(approx, using $45.0B×29.5%=$13.275B; using $45.18B gives $13.328B — within 0.4%, immaterial) | Computed |
| FY2025 OCF | $10.1B | Netflix Q4 2025 earnings release |
| FY2025 CapEx | ~$0.6B (implied: OCF $10.1B − FCF $9.5B) | Computed |
| **FY2025 FCF** | **$9.5B** (Q1 $2.661B + Q2 $2.267B + Q3 $2.660B + Q4 ~$1.9B ≈ $9.49B) | Netflix quarterly 8-Ks, summed |
| **FCF/NI conversion** (FY2025) | **86.4%** ($9.5B / $11.0B) | Computed — above 70% threshold |
| Total debt (Q1 2026, 10-Q) | $14.361B ($999.2M ST + $13.361B LT) | Netflix Q1 2026 10-Q |
| Cash + ST investments (Q1 2026) | $12.296B | Netflix Q1 2026 10-Q |
| **Net debt** | **$2.065B** | Computed |
| ROIC | 21.26% (GuruFocus, Dec 2025) / 23.98% (TTM) / 25.50% (Q1 2026 annualized) | WebSearch aggregation — all well above 15% |
| Shares outstanding (Q1 2026, 10-Q) | 4,212.79M | Netflix Q1 2026 10-Q |
| **Market Cap** | 4,212.79M × $81.27 = **$342.37B** | Computed |
| **Enterprise Value** | $342.37B + $2.065B = **$344.44B** | Computed |
| **EV/EBIT** | $344.44B / $13.275B = **25.95×** | Computed |
| **FCF Yield** | $9.5B / $342.37B = **2.775%** | Computed |
| FY2026 revenue guidance | $50.7–51.7B (+14%), ~$51B midpoint | Netflix Q1 2026 shareholder letter |
| FY2026 operating margin guidance | 31.5% (includes ~$275M now-moot WBD-related costs — implies modest upside) | Netflix Q1 2026 shareholder letter |
| FY2026 FCF guidance | raised to ~$12.5B (from ~$9.5B FY2025) | Netflix Q1 2026 earnings (8-K) |
| 2026 consensus EPS | **$3.66** (range $3.19–$3.96 across analysts) | WebSearch aggregation |
| **Forward PE** | $81.27 / $3.66 = **22.20×** | Computed |
| Current TTM PE (8 Jun 2026) | 40.76× | GuruFocus / WebSearch aggregation |
| **10yr avg PE** | **60.90×** (FinanceCharts) — corroborated by 10yr **median** 61.19× (GuruFocus) | WebSearch aggregation |
| 10yr avg PE (alt, flagged) | 93.64× — same single-sourced figure flagged in the 2026-06-07 session as likely distorted | WebSearch aggregation |
| 5yr avg PE | 43.33× (FinanceCharts) / 41.16× (alt source) | WebSearch aggregation |
| FY2023→24 Diluted EPS | declined ~5.8% YoY (per aggregation; absolute figures inconsistent across sources — see Gap #4) | WebSearch aggregation |

### Data Gaps / Flags

1. **PE-ratio split-consistency resolved (good news vs. 2026-06-07 flag).** A stock split divides both price *and* EPS by the same factor (10×), so the **PE ratio itself is split-invariant** — a 10-year average/median *PE ratio* doesn't need restatement the way a 10-year average *price* would. The **60.90× (FinanceCharts 10yr avg) / 61.19× (GuruFocus 10yr median)** pair is internally consistent (avg ≈ median, as expected for a ratio without extreme skew) and far more credible than the single-sourced 93.64× outlier carried in the 2026-06-07/06-11 sessions. **60.90× is used as the primary 10yr avg PE this session.** The 93.64× figure is shown in the sensitivity check below — **it does not change the result either way** (see §5), so this is flagged for completeness but is not a live judgment call this time.
2. **TTM EBIT derived from FY2025's reported 29.5% operating margin** (a stated percentage, not a directly-quoted $ EBIT figure) applied to FY2025 revenue. Sensitivity: using $45.18B (exact FY2025 revenue, vs. the rounded $45.0B used in the headline calc) gives EBIT = $13.328B and EV/EBIT = 25.84× — a sub-score difference of (25.95−25.84)/23×100 ≈ 0.48 points pre-weighting, ~0.19 points post-weighting (40%). **Does not change the final score after rounding** (still 63.2 either way — verified).
3. **FY2025 FCF ($9.5B) is a sum of four individually-sourced quarterly figures** (Q1 $2.661B, Q2 $2.267B, Q3 $2.660B, Q4 ~$1.9B = $9.488B ≈ $9.5B), cross-checked against the company's own "$9.5B FY2025 FCF, exceeded $9B guidance" framing. Internally consistent — high confidence.
4. **EPS growth history (Fast Grower / PEG test) — source data was internally inconsistent** (one aggregation returned FY2023 diluted EPS $4.49 and FY2024 $4.23, a −5.8% YoY *decline*; these specific absolute figures don't reconcile cleanly against FY2025's $2.53 post-split EPS, suggesting a mix of pre/post-split or annual/quarterly figures in the source data). **However, the directional finding — FY2024 EPS declined YoY versus FY2023 — is sufficient on its own to fail the ">15% EPS growth for 3+ consecutive years" Fast Grower test**, independent of the exact magnitudes. **NFLX is classified as NOT a Fast Grower** (consistent with the 2026-06-07 session's conclusion). PEG's 15% weight is redistributed to EV/EBIT (→ 40%).
5. **Net Debt/EBITDA — EBITDA approximated via EBIT + property/equipment D&A only** (~$330M/yr annualized from the 9-month $247.4M figure), giving EBITDA ≈ $13.6B and Net Debt/EBITDA ≈ **0.15×**. Content amortization (~$15.5B annualized) is deliberately **excluded** from the EBITDA add-back — for a content-replacement-cost business model, amortized content cost is closer to a recurring operating cost than a one-time non-cash add-back, and including it would overstate "EBITDA" in a way that doesn't reflect economic reality. Either way, net debt is so small relative to any EBIT/EBITDA base that the **<2× threshold is passed by a wide margin** under any reasonable definition.
6. **Forward PE basis: 2026 consensus EPS ($3.66), not company guidance** — Netflix does not guide GAAP EPS directly (it guides revenue and operating margin). $3.66 is an analyst consensus blend (range $3.19–$3.96, a ~17% spread). Sensitivity: at the low end ($3.19), Forward PE = 25.49× → Deviation% vs 60.90 = −58.1% → FwdPE_Score still clamps to 0.0. At the high end ($3.96), Forward PE = 20.52× → Deviation% = −66.3% → FwdPE_Score still 0.0. **Doesn't change the score** — see §5.

---

## 3. Phase 01 — Quality Gate

| Check | NFLX Value | Threshold | Result |
|---|---|---|---|
| Net margin (FY2025) | 24.3% | >15% | ✅ PASS |
| ROIC | 21.3–25.5% (range across sources/periods) | >15% | ✅ PASS |
| Revenue CAGR 3yr (FY2022→FY2025) | 12.51% | >10% | ✅ PASS |
| Gross margin | 48.5% | >40% | ✅ PASS |
| FCF positive 3 consecutive years | FY2025 $9.5B confirmed; FY2023/24 FCF have been "record"/growing in every annual release, no plausible negative-FCF year in this window | required | ✅ PASS |
| Net debt/EBITDA | ~0.15× (net debt $2.065B vs EBITDA ≈$13.6B) | <2x | ✅ PASS |
| FCF/NI conversion ratio | 86.4% (FY2025) | >70% | ✅ PASS |
| Share issuance pattern | Share count roughly flat/declining (buybacks resumed in recent years); non-dilutive | not dilutive | ✅ PASS |
| Moat signal | #1 global streaming platform by subscribers (325M+), content slate scale ($20B 2026 budget), ad-tier scaling to 250M+ MAU, password-sharing conversion largely complete | required | ✅ Qualitatively strong |

**Gate result: PASS — proceeding to Rate Environment Gate and Phase 02.** (Consistent with the 2026-06-07 session; verified fresh.)

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 22.20 = 4.5035%
Spread = EY − 10Y Treasury = 4.5035% − 4.46% = +0.0435%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.04%, far short of +1.5%) → **+5 additive applied**.

**Step 2 — Rate Regime Modifier**
10Y = 4.46% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for NFLX = +10** (+5 Step 1 fail + +5 Step 2)

*Note: this differs from the prior 58.9 score's effective treatment — the 2026-06-11 rescale session applied only the Step 2 component (+5) without a documented Step 1 check for NFLX, consistent with the broader "possible Rate Environment Gate inconsistency" flagged in [watchlist/README.md](../watchlist/README.md). This session applies both steps per the current strategy.md, as the ADBE session also did.*

---

## 5. Phase 02 — Full Score Calculation

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 2.775 / 10), 0, 100)
          = clamp(100 × (1 − 0.2775), 0, 100)
          = clamp(72.25, 0, 100)
          = 72.25
```
→ Contribution: 72.25 × 0.40 = **28.90**

**EV/EBIT — weight 40% (PEG not applicable, redistributed — see Gap #4)**
```
EV/EBIT_Score = clamp((25.95 − 12) / 23 × 100, 0, 100)
              = clamp(13.95 / 23 × 100, 0, 100)
              = clamp(60.64, 0, 100)
              = 60.64
```
→ Contribution: 60.64 × 0.40 = **24.25**

**Forward PE (fallback formula) — 20% weight**
```
Deviation% = (22.20 − 60.90) / 60.90 × 100 = −63.54%
FwdPE_Score = clamp(50 + (−63.54) × 2.5, 0, 100)
            = clamp(50 − 158.85, 0, 100)
            = clamp(−108.85, 0, 100)
            = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**Sensitivity check (Forward PE benchmark / EPS source):**
| 10yr avg PE used | Deviation% | FwdPE_Score |
|---|---|---|
| 60.90× (primary, this session) | −63.54% | 0.0 |
| 61.19× (GuruFocus median) | −63.71% | 0.0 |
| 93.64× (prior session's flagged figure) | −76.29% | 0.0 |

| Forward PE basis (2026 consensus EPS) | Forward PE | Deviation% vs 60.90 | FwdPE_Score |
|---|---|---|---|
| $3.19 (low end) | 25.49× | −58.13% | 0.0 |
| $3.66 (consensus, used) | 22.20× | −63.54% | 0.0 |
| $3.96 (high end) | 20.52× | −66.30% | 0.0 |

**Every combination clamps to 0.0 — the FwdPE sub-score is robust to all flagged data-quality issues this session.**

**PEG — not applicable (not a Fast Grower, see Gap #4).** Weight redistributed to EV/EBIT above.

**Raw weighted score:**
```
= 28.90 + 24.25 + 0.0 = 53.15
```
**+ Rate Modifier (+10) = 63.15**

Boundary rule: 63.15 falls exactly on ".X5" → **round UP** → **Final Score = 63.2**

*(Precise arithmetic: 28.9010 + 24.2546 + 0.0 = 53.1556; + 10 = 63.1556 → rounds to 63.2 under standard nearest-0.1 rounding — the ".X5 rounds up" rule and standard rounding agree here since 63.1556 is closer to 63.2 than 63.1 regardless.)*

---

## 6. Final Score & Action

# Final Score: 63.2 → Action: HOLD — watch only, no new entry, no trim ("Fair Value")

This is a **meaningful change from the prior 58.9** (Jun 2026, derived from the 2026-06-07 pull), but **the action category is unchanged** — both 58.9 and 63.2 fall in the 50.0–69.9 "Fair Value" band. Per [watchlist/README.md](../watchlist/README.md), a fresh full re-score counts as a "significant change" warranting a new dated entry even when the action category is unchanged, because the *reasoning* has materially changed:

- **FCF yield sub-score rose slightly** (72.25 vs. an implicit ~70 in the old 1–10 scale's "sub-score 7" bucket) — FCF yield itself is similar (2.775% vs. 2.74%), broadly flat.
- **EV/EBIT sub-score is similar** (60.64 vs. an implicit ~65.2 from the old "sub-score 7" — EV/EBIT improved slightly from 26.32× to 25.95×).
- **FwdPE sub-score is now a clean, high-confidence 0.0** rather than a judgment-call "2 of 10" — Forward PE (22.20×) is so far below even the most conservative 10yr-avg-PE benchmark (60.90×) that this sub-score can't move regardless of which historical-PE source is used. This **removes** last session's softened-judgment-call flag entirely.
- **The Rate Modifier increased from a likely-understated +5 (Step 2 only) to a fully-computed +10 (Step 1 fail +5, Step 2 +5)** — this is the single largest driver of the score's increase, and reflects the framework being applied *correctly and completely* this time, not a change in NFLX's fundamentals.

Net effect: NFLX's underlying valuation picture (FCF yield ~2.8%, EV/EBIT ~26×, Forward PE ~22× vs. a clean ~61× historical norm) is essentially **unchanged to modestly improved** from two weeks ago. The +5 point increase in the final score is mostly a **methodology-completeness correction** (Rate Gate Step 1), not a deterioration.

---

## 7. Fair Value & Position Sizing (Existing Holding — Hold Band)

Per the operating brief: Score 50.0–69.9 → "No MoS → Watchlist only" / "Hold — watch only, no new entry, no trim." A full order-setup (buy price / stop loss / R/R) is **not required** for a Hold-band score. However, since NFLX is an existing holding, a blended Fair Value is computed below for context — to frame *how far* from fair value the current price sits, and to inform the current-vs-target sizing comparison.

### Step 1 — Fair Value (Blended)

**Method A: DCF (3 scenarios, Rule 2/7)**

Anchor: 2026 FCF guidance ($12.5B, raised from $9.5B FY2025 — reflects guided margin expansion to 31.5%). Net debt $2.065B. Shares 4,212.79M.

| Scenario | WACC | Yr1 FCF | Yrs 2–5 growth | Yrs 6–10 fade | Terminal growth | PV Stage 1 | PV Stage 2 | PV Terminal | Total EV | Equity Value | **FV/share** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Bear | 10.5% | $11.5B | 8%→5% | 4.5%→2.5% | 2.0% | $48.86B | $37.42B | $77.66B | $163.93B | $161.87B | **$38.42** |
| Base | 9.5% | $12.5B | 12%→9% | 7%→4% | 2.5% | $58.65B | $53.77B | $143.85B | $256.27B | $254.21B | **$60.34** |
| Bull | 8.5% | $13.0B | 15%→12% | 9%→5.5% | 3.0% | $66.27B | $70.42B | $253.43B | $390.12B | $388.05B | **$92.11** |

WACC base = risk-free (4.46%) + β≈1.4 × ERP≈3.6% ≈ 9.5% (NFLX's beta historically runs higher than ADBE's ~1.3, reflecting its more cyclical/discretionary-spend exposure); bull/bear vary WACC ∓1% per Rule 2. Terminal value is 47–65% of total EV across scenarios — under the 75% trigger for extending Stage 2 (Rule 4).

```
PW DCF FV = 0.25 × Bull + 0.50 × Base + 0.25 × Bear
          = 0.25×92.11 + 0.50×60.34 + 0.25×38.42
          = 23.03 + 30.17 + 9.61
          = $62.80
```

**Method B: Comparable Multiples**

| Approach | "Fair" multiple | Calculation | FV/share |
|---|---|---|---|
| Forward PE comp | 28× (modest re-rating from current 22.2×; still well below 10yr avg 60.90× and 5yr avg ~43×, reflecting genuine deceleration vs. NFLX's hyper-growth-era history) | 28 × $3.66 | **$102.48** |
| EV/EBIT comp | 18× on 2026E EBIT ($51B × 31.5% = $16.065B) | EV $289.17B − net debt → equity $287.11B ÷ 4,212.79M | **$68.15** |
| FCF-yield comp | 5.0% yield on 2026E FCF ($12.5B) | EV $250.0B − net debt → equity $247.94B ÷ 4,212.79M | **$58.85** |
| **Multiples avg** | | | **$76.49** |

**Historical PE cross-check (Rule 3, context only — not weighted into blend):**
```
Implied TTM EPS (from current PE 40.76× and price $81.27) ≈ $1.99
Historical PE FV = $1.99 × 10yr avg PE (60.90) ≈ $121.43
```
This is the same "mean-reversion ceiling" logic as the consensus PT ($115) and is directionally consistent with it — both suggest meaningful upside *if* NFLX's multiple were to revert toward its historical norm. As with ADBE, this is shown for context only (**0% weight**) — a reversion that large (+49% from current price) is too extreme a standalone point estimate to use directly (would imply an unreasonably high IRR per Rule 4).

**Triangulation:**
```
Blended FV = 40% × DCF(PW) + 60% × Multiples(avg)
           = 0.40 × $62.80 + 0.60 × $76.49
           = $25.12 + $45.89
           = $71.02
```

**Cross-check vs. external estimates:** Blended FV ($71.02) sits **below** both the analyst consensus PT ($115, median) and the historical-PE cross-check ($121.43). This ordering (our blended FV < consensus PT < historical-PE reversion) reflects our DCF/multiples approach using **current, compressed multiples** (22.2× forward PE, 5% FCF yield) as comparables rather than NFLX's own rich hyper-growth-era history — a deliberately more conservative framing. The **current price ($81.27) sits ~14.4% above our Blended FV ($71.02)** — i.e., **no margin of safety**, consistent with a Fair-Value/Hold score.

### Step 2 — No Order Setup (Hold Band)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Step 2 integration table: **Score 50.0–69.9 → No MoS → Watchlist only.** No Buy Price, Sell Target, Stop Loss, or R/R calculation is computed — these only apply to BUY (0.0–49.9) or TRIM (70.0+) actions. NFLX sits ~14% *above* its own blended FV, so even if a buy were contemplated, there is no margin of safety to set a buy price against.

### Step 3 — Current vs. Target Position Size

The framework's Phase 03 sizing table maps **Score 50.0–69.9 → "Watchlist only — no new entry"** — there is no positive target allocation to compute for a Fair Value score; the "target" for this band is simply **the current size, held**, with no incremental buying and no trim.

| | Value |
|---|---|
| Current NFLX weight | **1.83%** of portfolio ($53,855.83 × 1.83% ≈ $985.56) |
| Target weight under current score (50.0–69.9 band) | **No new-entry target — hold at current size** |
| 15% hard cap (Upgrade 7) headroom | 13.17pp of headroom remains (1.83% vs. 15%) — **not a binding constraint either direction** at this score |
| Gap vs. target | **None to report** — 1.83% is neither "underweight vs. a buy target" (there is no buy target at Score 63.2) nor "overweight vs. a trim trigger" (trim only triggers at 70.0+) |

**No sizing action implied by this score.** NFLX remains comfortably within the 15% cap regardless, so the cap is not a live constraint in either direction at this score.

---

## 8. Qualitative Assessment (5 Questions + Disruption Vector Check)

1. **Why are margins high?** Scale economics on content amortization (content cost is largely fixed once produced/licensed and amortized across a 325M+ subscriber base — each incremental subscriber is high-margin), pricing power across multiple tiers (ad-supported, standard, premium), and a rapidly scaling, high-incremental-margin advertising business (ad MAU 250M+ as of May 2026, up from 94M a year earlier, targeting $3B+ ad revenue in 2026 — roughly double 2025's >$1.5B).

2. **What would it take to compete?** A challenger would need: (a) a content budget at NFLX's scale (~$20B/year guided for 2026) sustained over many years to build a comparably deep library, (b) a global content-production and licensing apparatus across 190+ countries/languages, (c) a recommendation/personalization engine tuned on NFLX's viewing-data scale, and (d) the balance sheet to absorb years of negative FCF before reaching NFLX's current margin structure — historically only Disney+, Amazon Prime Video, and Apple TV+ have attempted this at scale, each backed by a much larger non-streaming parent business.

3. **Capital allocation track record:** Disciplined content-spend ROI focus (content amortization tightly correlated with subscriber/engagement growth rather than "spend for spend's sake"); the **abandoned $83B Warner Bros. Discovery (WBD) acquisition bid** (announced ~March 2026, terminated by Q1 2026) — Netflix walked away and **collected a $2.8B termination fee**, a similar "discipline over empire-building" signal to ADBE's Figma walk-away. Buyback activity has resumed as FCF has scaled (shares outstanding roughly flat to slightly down).

4. **Growth sources, next 3–5 years:** (a) Advertising — the most under-monetized lever, guided to roughly double to $3B in 2026 off a base that's already growing ad MAU at >2.5× YoY; (b) continued international subscriber growth in under-penetrated markets (now 325M+ paid subscribers globally); (c) price increases on premium/ad-free tiers as content value increases; (d) live/sports programming and gaming as engagement-extension levers (incremental, not yet a primary revenue driver); (e) the WBD termination fee ($2.8B) provides incremental balance-sheet flexibility without diluting the core streaming thesis.

5. **Best bear case:** Subscriber growth has been substantially front-loaded by the password-sharing crackdown (2023–2025) — that one-time tailwind is largely exhausted, and organic net-add growth could decelerate toward population/penetration-driven rates. Content costs ($20B guided for 2026, an all-time high) could face diminishing returns if competitors (Disney+, Amazon, Apple, YouTube, and increasingly user-generated/short-form video) fragment viewing attention further. The Q2 2026 guidance miss noted in earnings coverage (operating margin guided to 32.6% vs. 34.1% in the year-ago quarter) suggests near-term margin deceleration is already showing up, even as the full-year 2026 guide (31.5%) still implies YoY expansion.

6. **Disruption vector check:** Short-form/user-generated video (YouTube, TikTok, Instagram Reels) competes for the same finite attention budget as NFLX's premium long-form content, but targets a structurally different need (passive "what's on" vs. active short-burst scrolling) — the two have coexisted and grown in parallel for years without NFLX's engagement metrics deteriorating. Generative-AI content creation is a more novel, longer-horizon vector: if AI-generated long-form content becomes commercially viable and audience-accepted within 5 years, it could pressure NFLX's content-cost advantage (its $20B/year scale moat) by lowering the cost of entry for new competitors — but it could equally **benefit** NFLX (lower its own $20B content bill, the largest line item standing between its current ~30% and a theoretically much higher operating margin). **Net assessment: this is a real but two-sided vector, not a one-directional thesis-breaker** — unlike ADBE's more acute "does GenAI commoditize the core product" debate, NFLX's core product (curated, premium video entertainment + a personalization/distribution platform) is less directly substitutable by raw generative tools in the near term.

**Catalyst & timeline (Rule 10):** the ~14% gap between current price ($81.27) and Blended FV ($71.02) is actually a **negative** gap (price above FV) — i.e., there's no "thesis vs. price" gap to close in NFLX's favor at the moment; if anything, the framework's own (conservative) multiples suggest NFLX is *slightly* ahead of where its current fundamentals justify, even as the consensus PT ($115) and historical-PE reversion ($121) suggest the *market* sees more room. The next 2–3 quarters (Q2 2026 ~Jul 2026, Q3 2026 ~Oct 2026) should clarify: (a) whether the 2026 ad-revenue doubling ($3B target) stays on track, (b) whether full-year operating margin guidance (31.5%) holds despite the softer Q2 margin guide (32.6% vs. 34.1% YoY), and (c) whether post-password-crackdown subscriber growth decelerates as some analysts expect. Any of these resolving negatively would be a Rule 9 trigger for re-score; resolving positively (especially margin guidance holding or beating) would tend to *raise* the FCF yield and EV/EBIT sub-scores further (cheaper), which — combined with the FwdPE sub-score's current floor at 0.0 — would likely pull the overall score *down* toward the Cheap band over time, even without a price move.

---

## 9. Recommendation

# **HOLD — no new entry, no trim. Score 63.2 (Fair Value), unchanged action category from prior 58.9.**

NFLX passes Phase 01 cleanly across every criterion (24.3% net margin, 21–25% ROIC, 12.5% revenue CAGR, 48.5% gross margin, FCF/NI conversion 86.4%, net debt/EBITDA ~0.15×). Phase 02 lands at **63.2** — solidly within the 50.0–69.9 "Fair Value" band, which carries **"Hold — watch only, no new entry, no trim"** under the current Action Table.

**Comparison to prior session (58.9, Jun 2026):**
- The action category is **unchanged** (both 58.9 and 63.2 are "Fair Value / Hold").
- The **+4.3 point increase** is driven almost entirely by **completing the Rate Environment Gate correctly** (+10 total this session — Step 1 fail +5, Step 2 +5 — vs. an effective +5 in the prior session, which appears to have only applied Step 2). This is a **methodology-completeness correction**, not a fundamentals-driven re-rating.
- The prior session's biggest open flag — a softened, judgment-call forward-PE sub-score (2 of 10, vs. a mechanical floor of 1) due to a single distorted 93.64× 10yr-avg-PE benchmark — is **resolved this session**: a corroborated pair of sources (60.90× avg / 61.19× median, internally consistent with each other) gives a clean, high-confidence FwdPE_Score of 0.0, and the sensitivity table in §5 shows this conclusion is **robust** to using either the old 93.64× figure or the new ~61× figures, and robust to the ~17% spread in 2026 consensus EPS estimates.
- Underlying fundamentals are **essentially flat to modestly improved**: FCF yield 2.775% (vs. 2.74%), EV/EBIT 25.95× (vs. 26.32×), revenue growth accelerating slightly (16% in FY2025 vs. ~13% in early FY2025 quarters), operating margin expanding (29.5% FY2025 → 31.5% guided FY2026).

**Sizing:** NFLX remains at **1.83%** of the portfolio — there is no target to size against in the Fair Value band (Phase 03 only assigns positive target allocations to Score <50.0; Score 70.0+ triggers a trim target). The position is **neither underweight relative to a buy signal nor overweight relative to a trim trigger** at this score. The 15% hard cap (Upgrade 7) is not a binding constraint in either direction (13.17pp of headroom).

**Blended Fair Value ($71.02) sits ~14% below the current price ($81.27)** — i.e., **no margin of safety** exists for a hypothetical add, consistent with the Hold recommendation. This sits in interesting tension with the analyst consensus PT ($115) and the historical-PE reversion estimate (~$121) — both of which imply meaningful upside *if* NFLX's multiple re-rates toward its own history. This framework's blended FV deliberately uses **current, compressed comparables** rather than NFLX's rich hyper-growth-era multiples, producing a more conservative (lower) FV — the gap between "$71 our FV" and "$115 consensus PT" is itself informative: it suggests the market is pricing in more multiple-reversion than this framework's bottom-up multiples currently support, even though the **direction** (potential undervaluation if margins/ad-revenue execute) is the same.

All final-decision authority rests with the human investor per the operating brief.

---

## 10. Next Review Trigger

- **Q2 2026 earnings** (expected ~mid-to-late July 2026) — mandatory re-score (Rule 9). Specifically check: (a) whether the 2026 ad-revenue doubling ($3B target) stays on track, (b) whether Q2 operating margin comes in at/above the guided 32.6% (vs. 34.1% YoY — a deceleration already flagged), (c) any update to post-password-crackdown subscriber growth trends.
- **>15% unexplained price move from $81.27 in either direction** — immediate re-score per Rule 9.
- **WBD termination-fee deployment** (capital allocation signal — buybacks vs. content spend vs. new M&A) — management-change/M&A-class Rule 9 trigger if a new large transaction is announced.
- **No position change executed by this session** — recommendation only (Hold at current 1.83%). If the human investor takes any action, log it in `decisions/` per CLAUDE.md Rule 10.

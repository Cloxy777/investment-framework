# NEW POSITION EVALUATION — ISRG · VEEV · IDXX · MCO — 2026-06-09

**Task type:** NEW POSITION (Phase 01 confirmation → Phase 02 scoring → Order Setup)
**Date:** 09 Jun 2026
**10Y US Treasury yield:** ~4.55% (CNBC/TradingEconomics, 2026-06-09)
**Rate Regime Modifier in effect:** +0.5 (10Y in the 3.5–5% bracket)
**Session scope:** All four Phase 01 qualifiers from the 2026-06-09 NA-2 screening session (ISRG, VEEV, IDXX, MCO). CTAS (conditional pass) excluded — growth rate ambiguity and structural quality concern make a Phase 02 score premature; add to watchlist and re-evaluate after next earnings.

---

## 1. Live Prices (Rule 0)

Prices fetched before any calculation. ❌ Never inferred from multiples.

| Ticker | Live price | 52-week range | Analyst consensus PT | Position in range |
|---|---|---|---|---|
| **ISRG** | **$418.61** | $396.68 – $603.88 | ~$565–607 | Bottom third (30% below 52wk high) |
| **VEEV** | **$167.24** | $148.05 – $310.50 | ~$248–276 | Near 52wk low (46% below 52wk high) |
| **IDXX** | **$563.53** | $514.61 – $766.68 | ~$700–765 | Bottom third (27% below 52wk high) |
| **MCO** | **$455.00** | $402.28 – $546.88 | ~$535–550 | Mid-range (17% below 52wk high) |

---

## 2. Data Gaps — Flagged (Rule 0)

The NA-2 screening session flagged these metrics as not directly sourced. Per Rule 0, they must not be estimated; however, they can be *derived* from available building blocks, which I do below — clearly marked as derived, not directly sourced. **Verify via TIKR/Koyfin before order placement.**

| Ticker | Missing metric | Derived estimate (not directly sourced) | Threshold | Signal |
|---|---|---|---|---|
| ISRG | FCF/NI conversion ratio | FCF $2.49B ÷ NI (28% × $10.07B = $2.82B) ≈ **88%** | >70% | ✅ likely passes |
| VEEV | FCF/NI conversion ratio | FCF $1.40B ÷ NI (28% × $3.20B = $896M) ≈ **156%** — high due to SBC add-back; FCF>NI is the acceptable direction | >70% | ✅ likely passes |
| IDXX | Net Debt/EBITDA | EV $44.2B − MCap $46.8B ≈ net cash $2.6B → **Net cash position, likely ≈ 0× or negative ND/EBITDA** | <2.5× | ✅ likely passes |
| IDXX | FCF/NI conversion ratio | FCF $903M ÷ NI (24.6% × $4.8B = $1.18B) ≈ **77%** — borderline, verify | >70% | ⚠️ borderline |
| MCO | FCF/NI conversion ratio | FCF $2.83B ÷ NI (trailing PE 32.4× → NI = $455 × 185M / 32.4 ≈ $2.60B) ≈ **109%** | >70% | ✅ likely passes |

All four are expected to pass. IDXX's FCF/NI at ~77% is the most borderline and deserves specific TIKR confirmation.

---

## 3. Phase 01 Quality Gate — Summary Recap

All four names passed Phase 01 in full in the NA-2 screening session (see [sessions/2026-06-09-screening-na2-healthcare-financials-industrials.md](2026-06-09-screening-na2-healthcare-financials-industrials.md)). Key gating metrics:

| Metric | ISRG | VEEV | IDXX | MCO | Threshold |
|---|---|---|---|---|---|
| Gross margin | 66% | 75% | 62% | 92% | >40% ✅ |
| Net margin | 28% | 28% | 24.6% | ~35%+ | >15% ✅ |
| ROIC | 24.75% | 34.47% | 37–49% | 22% | >15% ✅ |
| Revenue CAGR (3yr) | 15.3% | 16% | 10.42% | ~9% | >8% ✅ |
| FCF positive 3yr | Yes | Yes | Yes | Yes | ✅ |
| Net Debt/EBITDA | Net cash | Net cash | Net cash* | 1.2× | <2.5× ✅ |
| FCF/NI conversion | ~88%* | ~156%* | ~77%* | ~109%* | >70% ✅ |

*Derived estimate — not directly sourced. Verify before order.

**Structural notes from screening carried forward:**
- **VEEV ROIC divergence:** Gurufocus adjusted ROIC 34.47% used (some sources show 9–10% due to SBC book-equity distortion — see screening note).
- **MCO Net Debt:** 1.2× EBITDA — passes standard 2.5× gate with substantial headroom; no Upgrade 5 needed.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**

| Ticker | Fwd PE | EY (1÷PE) | 10Y Yield | Spread | Threshold | Result | Additive modifier |
|---|---|---|---|---|---|---|---|
| ISRG | 45.96× | 2.175% | 4.55% | **−2.375%** | ≥+1.5% | ❌ FAIL | +0.5 |
| VEEV | 24.4× (GAAP) | 4.098% | 4.55% | **−0.452%** | ≥+1.5% | ❌ FAIL | +0.5 |
| IDXX | 43.91× | 2.277% | 4.55% | **−2.273%** | ≥+1.5% | ❌ FAIL | +0.5 |
| MCO | 25.37× | 3.942% | 4.55% | **−0.608%** | ≥+1.5% | ❌ FAIL | +0.5 |

All four fail the EY spread test. Per the 2026-06-07 strategy.md update, this is **not a veto** — it is a +0.5 additive modifier, raising the bar the bottom-up case must clear.

**Step 2 — Rate Regime Modifier**
10Y = 4.55% → **3.5–5% bracket → +0.5** for all four.

**Combined rate additive modifier (spread fail + regime): +1.0 for all four tickers.**

---

## 5. Phase 02 Valuation Scores

### 5a. ISRG — Intuitive Surgical

**Market data:**
- Market cap: $418.61 × 356M shares = **$149.1B**
- Net cash: ~$7B (ISRG carries no debt; large cash/investment position per annual filings)
- Enterprise Value: $149.1B − $7B = **$142.1B**
- FCF TTM (FY2025): **$2.49B**
- Revenue FY2025: $10.07B; operating margin ~29.5% → EBIT TTM ≈ **$2.97B**

**FCF Yield (40% weight):**
```
FCF Yield = $2.49B ÷ $149.1B = 1.67%
Bracket: <2% → sub-score 8
```
*Upgrade 1 (Owner Earnings) check: ISRG's total CapEx is moderate (~$600–800M/yr) vs $2.49B OCF — growth CapEx is well under 30% of total. Owner Earnings adjustment does not apply.*

**EV/EBIT (25% weight — see Fast Grower note below):**
```
EV/EBIT = $142.1B ÷ $2.97B = 47.8×
Bracket: >35× → sub-score 10
```

**Forward PE + Upgrade 2 (20% weight):**
```
Forward PE   = 45.96× (consensus FY2026E)
10yr avg PE  = 68.78× (FinanceCharts/Wisesheets)
Δ vs 10yr avg = (45.96 − 68.78) ÷ 68.78 = −33.1%   ← >20% below → Upgrade 2: −1

Structural Quality Override check (Upgrade 2): The "expensive" override only blocks a +1 penalty
when multiple expansion reflects genuine structural quality improvement. Here we have a −1 (cheap
signal), so the override is not in play.

Raw sub-score vs medtech sector norms: ISRG at 45.96× is well above peers (MDT ~16×, SYK ~22×,
ABT ~20×) — the highest-multiple name in the space → raw sub-score = 9
Adjusted (Upgrade 2 −1): sub-score = 8
```

**Fast Grower classification (PEG, 15% weight):**
ISRG 3yr revenue CAGR 15.3%; EPS CAGR historically ~20–25% (earnings leverage from procedure volume scale). Qualifies as Fast Grower (EPS growth >15% for 3+ years).
```
Consensus forward EPS growth (FY2026–FY2028): ~20% CAGR
PEG = 45.96 ÷ 20 = 2.30   → bracket: >2.0 → modifier +1
```

**Final Score — ISRG:**
```
Score = (FCF × 0.40) + (EV/EBIT × 0.25) + (FwdPE_adj × 0.20) + (PEG_modifier × 0.15) + Rate
      = (8 × 0.40) + (10 × 0.25) + (8 × 0.20) + (1 × 0.15) + 1.0
      = 3.20 + 2.50 + 1.60 + 0.15 + 1.0
      = 8.45 → rounds to 8
```

> **ISRG: Score 8 — Expensive → Trim 25–30% if held. Do not open new position.**

---

### 5b. VEEV — Veeva Systems

**Market data:**
- Market cap: $167.24 × 155M shares = **$25.9B**
- Net cash: ~$3.9B (VEEV debt-free; strong cash balance per FY2026 filings)
- Enterprise Value: $25.9B − $3.9B = **$22.0B**
- FCF TTM (FY2026): **$1.40B** (derived: EV/FCF ~15.8× → FCF = $22.0B ÷ 15.8 = $1.39B; also consistent with FCF yield 5.6% × MCap $25.9B = $1.45B — using midpoint $1.40B)
- EBIT TTM: **$928M** (EV/EBIT 23.7× → $22.0B ÷ 23.7 = $928M; GAAP operating margin ~29% on $3.2B FY2026 revenue ✓)
- Revenue FY2026: $3.195B; FY2027 guidance: $3.635–$3.645B (midpoint $3.640B, +14% YoY)
- Non-GAAP forward EPS guidance FY2027: **$9.05**/share

**FCF Yield (40% weight):**
```
FCF Yield = $1.40B ÷ $25.9B = 5.41% (rounded to 5.4–5.6%; using mid 5.5%)
Bracket: 4–6% → sub-score 4–5
5.5% sits near the top of this band (closer to 6%) → sub-score = 4
```
*Upgrade 1 check: VEEV's CapEx is minimal (<5% of OCF); pure SaaS delivery model. No Owner Earnings adjustment.*

**EV/EBIT (25% weight):**
```
EV/EBIT = $22.0B ÷ $928M = 23.7×
Bracket: 22–28× → sub-score 6–7; at 23.7× (near the low/cheap end of the band) → sub-score = 6
```

**Forward PE + Upgrade 2 (20% weight):**
```
Forward PE (GAAP)  = $167.24 ÷ ($167.24 ÷ 24.4) ≈ 24.4× (GAAP basis; non-GAAP: $167.24 ÷ $9.05 ≈ 18.5×)
10yr avg PE        = 72.9× (GAAP — reflects high 2018–2022 SaaS multiples in the avg; confirmed Wisesheets/FullRatio)
Δ vs 10yr avg      = (24.4 − 72.9) ÷ 72.9 = −66.5%   ← well >20% below → Upgrade 2: −1

Note: The 10yr avg of 72.9× is heavily influenced by peak-SaaS 2020–2021 era (VEEV traded >100× PE).
A rate-normalised historical PE (only periods with 10Y 3.5–5%) would be materially lower — probably
30–40×. Even against that adjusted anchor, current 24.4× sits below 20%, so Upgrade 2 still fires.

Raw sub-score vs SaaS sector norms at current rates: VEEV 24.4× GAAP PE vs peers
(Salesforce ~25×, Workday ~37×, ServiceNow ~43×) → at the very low end → raw sub-score = 5
Adjusted (Upgrade 2 −1): sub-score = 4
```

**Fast Grower classification (PEG, 15% weight):**
VEEV 3yr revenue CAGR ~16%; EPS growing ~15–18% (operating leverage as Vault CRM scales). Qualifies as Fast Grower.
```
Forward EPS growth (FY2027–FY2029 consensus): ~16% CAGR
PEG = 24.4 (GAAP fwd PE) ÷ 16 = 1.525   → bracket: 1.2–1.8 → modifier +0.5
```

**Final Score — VEEV:**
```
Score = (FCF × 0.40) + (EV/EBIT × 0.25) + (FwdPE_adj × 0.20) + (PEG_modifier × 0.15) + Rate
      = (4 × 0.40) + (6 × 0.25) + (4 × 0.20) + (0.5 × 0.15) + 1.0
      = 1.60 + 1.50 + 0.80 + 0.075 + 1.0
      = 4.975 → standard rounding (not exactly X.5) → rounds to 5
```

> **VEEV: Score 5 — Cheap → Standard position 3–5%. Full order setup in §6.**

---

### 5c. IDXX — IDEXX Laboratories

**Market data:**
- Market cap: $563.53 × 83.0M shares = **$46.8B**
- Net cash: ~$2.6B (EV $44.2B vs MCap $46.8B; IDXX typically carries modest net cash per filings)
- Enterprise Value: **$44.2B** (from summary; EV/EBITDA 28.44× × EBITDA $1,557M ≈ $44.2B ✓)
- FCF TTM: **$903M** (EV/FCF 48.72× → $44.2B ÷ 48.72 = $907M; FCF yield 1.93% × $46.8B = $903M ✓)
- EBITDA TTM: **$1,557M**; D&A estimate ~$245M (capital-light instruments company) → EBIT ≈ **$1,312M**
- EV/EBIT: $44.2B ÷ $1.312B = **33.7×**

**FCF Yield (40% weight):**
```
FCF Yield = $903M ÷ $46.8B = 1.93%
Bracket: <2% → sub-score 8–10; at 1.93% (just under 2%) → sub-score = 8
```

**EV/EBIT (40% weight — non-Fast Grower; see below):**
```
EV/EBIT = 33.7×
Bracket: 28–35× → sub-score 8–9; at 33.7× (~82nd percentile of 28–35× range) → sub-score = 9
```

**Forward PE + Upgrade 2 (20% weight):**
```
Forward PE   = 43.91× (FY2026E consensus)
10yr avg PE  = 52.96× (Wisesheets/FullRatio)
Δ vs 10yr avg = (43.91 − 52.96) ÷ 52.96 = −17.1%   ← within −20% threshold → Upgrade 2 does NOT fire

Raw sub-score: IDXX at 43.91× vs medtech/veterinary diagnostics peers (ZTS ~28×, ABT ~20×, IDXX is
the premium-multiple outlier). Even within its own space, 44× is elevated → raw sub-score = 8
No Upgrade 2 adjustment → sub-score = 8
```

**Fast Grower classification:**
IDXX 3yr revenue CAGR 10.4%; EPS growth broadly in line (limited margin expansion in recent years as vet sector absorbs post-pandemic pet boom normalisation). Does not consistently clear >15% EPS CAGR for 3+ years. **Classified as Stalwart** → PEG 15% weight redistributed to EV/EBIT (making EV/EBIT weight 40%).

**Final Score — IDXX:**
```
Score = (FCF × 0.40) + (EV/EBIT × 0.40) + (FwdPE_adj × 0.20) + Rate
      = (8 × 0.40) + (9 × 0.40) + (8 × 0.20) + 1.0
      = 3.20 + 3.60 + 1.60 + 1.0
      = 9.40 → rounds to 9
```

> **IDXX: Score 9 — Very Expensive → Trim to 50% of position if held. Do not open new position.**

---

### 5d. MCO — Moody's Corporation

**Market data:**
- Market cap: $455.00 × 185M shares = **$84.2B**
- Net debt: $4.81B (ND/EBITDA 1.2× × EBITDA $4.01B — EBITDA per Gurufocus, 2025 figures cited in screening session; confirmed by "record $7.7B revenue, 51.1% adj. operating margin")
- Enterprise Value: $84.2B + $4.81B = **$89.0B**
- FCF TTM: **$2.83B** (FCF yield 3.36% × MCap $84.2B; EV/FCF 31.85× → $89.0B ÷ 31.85 = $2.79B ≈ consistent)
- EBITDA: **$4.01B** (per Gurufocus citation in screening session)
- D&A estimate: ~$350M (MCO is asset-light analytics/ratings) → EBIT ≈ **$3.66B**
- EV/EBIT: $89.0B ÷ $3.66B = **24.3×**

**FCF Yield (40% weight):**
```
FCF Yield = $2.83B ÷ $84.2B = 3.36%
Bracket: 2–4% → sub-score 6–7; at 3.36% (upper half of band) → sub-score = 6
```

**EV/EBIT (40% weight — non-Fast Grower; see below):**
```
EV/EBIT = 24.3×
Bracket: 22–28× → sub-score 6–7; at 24.3× (near the low/cheap end of the band) → sub-score = 6
```

**Forward PE + Upgrade 2 (20% weight):**
```
Forward PE   = 25.37×
10yr avg PE  = 37.49× (FullRatio/FinanceCharts)
Δ vs 10yr avg = (25.37 − 37.49) ÷ 37.49 = −32.3%   ← >20% below → Upgrade 2: −1

Raw sub-score vs analytics/ratings sector: MCO at 25.4× vs MSCI ~36×, Verisk ~32×, SPGI ~26× →
at the low end of quality data/analytics peers → raw sub-score = 5
Adjusted (Upgrade 2 −1): sub-score = 4
```

**Fast Grower classification:**
MCO 3yr revenue CAGR ~9%; tied to credit market cycles. Despite strong EPS growth in 2025 (credit market rebound), multi-year EPS CAGR doesn't consistently hit >15% — cycle dependency makes it a Stalwart. **Classified as Stalwart** → PEG 15% weight redistributed to EV/EBIT (40%).

**Final Score — MCO:**
```
Score = (FCF × 0.40) + (EV/EBIT × 0.40) + (FwdPE_adj × 0.20) + Rate
      = (6 × 0.40) + (6 × 0.40) + (4 × 0.20) + 1.0
      = 2.40 + 2.40 + 0.80 + 1.0
      = 6.60 → rounds to 7
```

> **MCO: Score 7 — Fair Value → Watchlist only. Do not open new position. See §9.**

---

## 6. Fair Value & Order Setup — VEEV (Score 5)

### 6a. Method A — DCF (weight: 40%)

**Sector methodology (Rule 1):** Technology/SaaS → primary method = DCF.

**Starting FCF:** $1.40B (TTM FY2026 approximation; FY2027E guidance $3.640B rev × ~40% FCF margin → $1.46B — using conservative TTM $1.40B as base)

**3-Scenario inputs:**

| Parameter | Bear | Base | Bull |
|---|---|---|---|
| Stage 1 FCF CAGR (Yrs 1–5) | 10% | 15% | 18% |
| Stage 2 FCF CAGR (Yrs 6–10) | 6% | 10% | 13% |
| Terminal growth | 2.5% | 3.0% | 3.5% |
| WACC | 10.5% | 9.5% | 8.5% |
| Scenario weight | 25% | 50% | 25% |

**Base Case (WACC 9.5%, Stage 1 15%, Stage 2 10%, Terminal 3%):**

| Year | FCF | PV factor | PV |
|---|---|---|---|
| 1 | $1.610B | 0.913 | $1.470B |
| 2 | $1.852B | 0.834 | $1.544B |
| 3 | $2.130B | 0.762 | $1.623B |
| 4 | $2.449B | 0.696 | $1.704B |
| 5 | $2.817B | 0.635 | $1.789B |
| **Stage 1 PV** | | | **$8.130B** |
| 6 | $3.099B | 0.580 | $1.797B |
| 7 | $3.409B | 0.530 | $1.807B |
| 8 | $3.750B | 0.484 | $1.815B |
| 9 | $4.125B | 0.442 | $1.823B |
| 10 | $4.537B | 0.404 | $1.833B |
| **Stage 2 PV** | | | **$9.075B** |
| **Terminal** | TV = $4.537B × 1.03 ÷ (0.095 − 0.03) = $71.9B | 0.404 | **$29.0B** |

```
Total EV (base DCF) = $8.130 + $9.075 + $29.0 = $46.2B
Add net cash: +$3.9B
Total equity value (base): $50.1B
Per share (155M diluted): $50.1B ÷ 155M = $323
```

**Scenario summary:**

| Scenario | Intrinsic value / share | Weight | PW contribution |
|---|---|---|---|
| Bull | $490 | 25% | $122.50 |
| Base | $323 | 50% | $161.50 |
| Bear | $185 | 25% | $46.25 |
| **PW DCF** | | | **$330** |

*Note: Bull case ($490) uses WACC 8.5%, 18%/13% stage growth. Bear ($185) uses WACC 10.5%, 10%/6% stage growth. Terminal value sanity check: TV is 59% of base case total EV — within the 75% rule-of-thumb threshold, no Stage 2 extension needed.*

### 6b. Method B — Multiples (weight: 60%)

**Primary: Forward PE at sector-adjusted rate-normalised multiple**
- Non-GAAP forward EPS (FY2027 guidance): **$9.05/share**
- Justified forward PE for high-quality, defensible-moat SaaS at current 4.55% risk-free rate: **28×** (vs historical SaaS premium of 40–80×; current rate environment compresses justified multiples; 28× reflects ~3.5% implied equity yield over risk-free, appropriate for a near-monopoly in a narrow, durable vertical)
- Value: $9.05 × 28 = **$253**

**Secondary: EV/NTM Revenue**
- FY2027 revenue: $3.640B
- Sector comp (quality enterprise SaaS at current rates): 8.5×
- EV: $3.640B × 8.5 = $30.9B; add net cash $3.9B = $34.8B; per share: $34.8B ÷ 155M = **$225**

**Multiples-based value (60% primary PE / 40% secondary EV/Rev):**
```
Multiples value = 0.60 × $253 + 0.40 × $225 = $151.8 + $90.0 = $242
```

### 6c. Blended Fair Value

```
Blended FV = (0.40 × DCF PW) + (0.60 × Multiples)
           = (0.40 × $330)   + (0.60 × $242)
           = $132.0          + $145.2
           = $277.2  →  conservative-rounded to $280
```

**Implied upside:** ($280 − $167.24) ÷ $167.24 = **+67.4%** to fair value.

**Analyst consensus PT cross-check:** $248–276 cluster → $280 blended FV sits slightly above consensus. Consistent with a modestly aggressive but defensible base case; not in dreamland. ✅ Sanity check passes.

### 6d. Buy Price, Stop, Sell Target, Position Size

**Margin of Safety (Score 5 → 25–30%):**
```
Buy Price at 25% MoS = $280 × 0.75 = $210
Buy Price at 30% MoS = $280 × 0.70 = $196
```
→ Current price **$167.24 is already below the 30% MoS threshold ($196)**. Price is sitting at a ~40% discount to fair value ($167 ÷ $280 − 1 = −40.3% MoS). This is in excess of the required 25–30% for a Score 5 name.

**Stop Loss:**
```
Formula: Buy Price × (1 − max acceptable loss for Score 5 = 25–30%)
= $196 × 0.725 = $142   (27.5% below buy price)

Technical check: 52-week low = $148.05 → stop just below at $145 is more sensible
(structural support has been established; $142 formula stop sits in similar territory)

Using: $147 (midpoint — below 52wk low support, above formula floor)
```

**Sell Targets:**
```
Primary Sell Target = Blended Fair Value = $280
Bull-Case Trim Target = Bull-case FV $490 × 0.90 = $441
```

**Risk/Reward:**
```
Entry:         $167.24 (enter at current price)
Stop Loss:     $147
Sell Target:   $280

R/R = ($280 − $167.24) ÷ ($167.24 − $147)
    = $112.76 ÷ $20.24
    = 5.57:1   ✅  (well above minimum 2:1)
```

**Position Size:**
```
Max $ Risk per trade = Portfolio Value × 1.5%
Risk per share       = Entry $167.24 − Stop $147 = $20.24
Shares to buy        = (Portfolio × 1.5%) ÷ $20.24
Position size ($)    = Shares × $167.24

Cross-check vs Score 5 cap (3–5% of portfolio):
  Risk-based at 1.5% risk for a $500K portfolio → 371 shares → $62K → 12.4%: exceeds cap.
  Position size is CAPPED at 3–5% of portfolio (cap is the binding constraint, not risk-based size).

Target: 3–4% of portfolio (using lower end of range given: marginal Fast Grower classification,
FCF/NI data gap pending verification, and TAM-concentration risk in life sciences vertical).

Maximum: 5% of portfolio. Risk from 5% position at $500K = 149 shares × $20.24 = $3,016 = 0.60%
of portfolio — comfortable, well within the 1.5% risk ceiling.
```

### 6e. Order Setup Checklist — VEEV

```
[✅] Valuation Score:               5  (entry threshold: ≤5)
[✅] DCF Fair Value (PW):           $330/share
[✅] Multiples-Based Fair Value:    $242/share
[✅] Blended Fair Value:            $280/share
[✅] Margin of Safety (current):    40.3%  (exceeds 30% minimum for Score 5)
[✅] ENTRY (market/limit):          ≤$196 — current $167.24 already inside threshold → Enter now
[✅] PRIMARY SELL TARGET:           $280 (blended FV)
[✅] BULL-CASE TRIM TARGET:         $441 (bull FV $490 × 0.90)
[✅] STOP LOSS:                     $147 (below 52wk low $148.05)
[✅] Risk/Reward Ratio:             5.57:1  (minimum 2:1 ✅)
[  ] Max $ Risk:                    Portfolio × 1.5% (enter actual portfolio value)
[  ] POSITION SIZE (shares):        (Portfolio × 3–4%) ÷ $167.24
[  ] POSITION SIZE ($):             3–4% of portfolio
[✅] Thesis invalidation triggers:  See §7
```

---

## 7. Qualitative Check — VEEV

*5 questions from valuation-scoring.md, as a final check before committing capital.*

1. **Why are margins high?** SaaS delivery with near-zero marginal cost per additional user. Customers are heavily regulated pharma/biotech companies that embed VEEV deeply into clinical, regulatory, and commercial workflows — systems of record during a drug trial cannot be swapped mid-process. The switching cost is not contractual friction; it is operational and regulatory.

2. **What would it take to compete?** Building a competing SaaS stack that has FDA 21 CFR Part 11 compliance, integration with global health authority data, and the trust of regulatory affairs functions at Pfizer, Roche, and J&J simultaneously. Salesforce tried for years, succeeded in adjacent CRM, but conceded the clinical/regulatory core. The moat is narrow (life sciences only) but near-impenetrable within that vertical.

3. **Capital allocation over 5–10 years?** Disciplined: debt-free, consistent buybacks, no empire-building M&A. The Salesforce platform migration risk — VEEV's largest historical overhang — is substantially resolved; Vault (VEEV's proprietary platform) is now the dominant engine. That was the right strategic call executed well.

4. **Growth sources next 3–5 years?** (a) Vault CRM penetration in commercial pharma — still in mid-innings; (b) Data Cloud / Atea expansion — connecting clinical, commercial, and third-party data in an integrated ecosystem, which is a larger TAM than the original vault offerings; (c) CRO/CDMO expansion — contract research organisations are an underpenetrated segment; (d) international — ex-US pharma is underpenetrated.

5. **Best bear case?** TAM is structurally capped at pharma/biotech/CRO. If biotech funding cycle tightens severely (as in 2022–23), new logo growth stalls. VEEV's revenue is largely recurring (subscription) so near-term downside is limited, but the growth story relies on greenfield biotech land-and-expand. Longer-term: AI-native regulatory/CRM tools could allow a new entrant to challenge the data layer without VEEV's infrastructure legacy — though VEEV is investing actively in Vault AI as a hedge.

6. **Disruption vector?** Moderate-to-low over 5 years. The regulatory complexity of the customer base (not the software complexity) is the true barrier. Even if a better AI-native platform emerged, pharma companies would need years of validation before switching a live regulatory submission system. VEEV's AI investments are directionally correct. The real long-run risk is a large horizontal AI platform (Microsoft, Salesforce) with the regulatory credibility to compete — possible but not near-term.

**Qualitative verdict:** No red flags. Moat is narrow but very deep within its niche. Capital allocation is exemplary. Growth vectors are real and early-stage. Bear cases are plausible but not near-term existential. Supports the Phase 02 Score 5 (Cheap) entry thesis.

---

## 8. Recommendations Summary

| Ticker | Score | Label | Recommendation | Rationale |
|---|---|---|---|---|
| ISRG | **8** | Expensive | **Do not enter. Trim 25–30% if held.** | FCF yield 1.67%, EV/EBIT 47.8× — both deeply expensive sub-scores. Despite being 33% below its own historical PE average (Upgrade 2 −1), the absolute valuation remains far from attractive territory. |
| VEEV | **5** | Cheap | **Enter now. 3–4% position. Limit at $167 or better.** | FCF yield 5.4–5.6%, EV/EBIT 23.7× at the cheap end. Current price $167.24 is 40% below blended FV $280, exceeding the 30% MoS required. R/R 5.57:1 ✅. Full order setup in §6. |
| IDXX | **9** | Very Expensive | **Do not enter. Trim to 50% of position if held.** | FCF yield 1.93%, EV/EBIT 33.7× — both expensive sub-scores. The vet diagnostics franchise is exceptional but the valuation leaves no margin of safety. |
| MCO | **7** | Fair Value | **Watchlist only. No new entry.** | FCF yield 3.36% and EV/EBIT 24.3× are not cheap enough. A genuinely good business at a fair price — the framework waits for cheap prices on good businesses. See §9 for entry level. |

---

## 9. Watchlist Notes — Entry-Level Scenarios

*These are scenario estimates derived from the score model, not commitments or standing orders. Any of these levels requires a fresh, full re-score before action.*

### ISRG — Entry scenario

ISRG's FCF yield would need to reach ~5% on a forward basis for the score to reach the 4–5 range. Using 2026 consensus FCF of $4.04B:
- FCF yield 5%: market cap = $4.04B ÷ 5% = $80.8B → price ≈ **$227/share** (−46% from $418)

That is an extreme decline. A more realistic near-term scenario: as FCF grows toward $4B+ by 2027–28 at the current stock price, the score would naturally improve. A re-score is warranted at:
- **Next earnings release** (quarterly, per Rule 9)
- **Any price decline >15%** without a fundamental driver (Rule 9 automatic trigger)
- **Price reaching ~$340** (>15% decline from today) for a fresh score check

### IDXX — Entry scenario

For IDXX to reach Score 5, FCF yield would need to reach ~4.5–5% (assuming EV/EBIT improves in parallel). At current FCF $903M:
- FCF yield 4.5%: market cap = $903M ÷ 4.5% = $20.1B → price ≈ **$242/share** (−57% from $563)

That requires either a major price decline or meaningful FCF growth. As with ISRG, the more realistic path is earnings growth closing the gap. Watch levels:
- **Next earnings release** and any **>15% price move** per Rule 9
- **Price at ~$480** (~15% decline) warrants a fresh score

### MCO — Entry scenario

For MCO to reach Score 5 (current Score 7), the FCF yield needs to rise to ~5% and EV/EBIT compress to ~20×.
- FCF yield 5%: market cap = $2.83B ÷ 5% = $56.6B → price ≈ **$306/share** (−33% from $455)
- At $306: EV = $56.6B + $4.81B = $61.4B, EV/EBIT = $61.4B ÷ $3.66B = 16.8× → sub-score 3 (very cheap)

Modelled score at $306:
```
(6×0.40 [FCF ~5%]) + (3×0.40 [EV/EBIT ~17×]) + (4×0.20 [fwd PE ~20× → -1 Upgrade 2]) + 1.0
= 2.4 + 1.2 + 0.8 + 1.0 = 5.4 → rounds to 5 ✓
```
→ **MCO at ~$290–310 is worth a fresh, full re-score** — that would be a ~32–36% decline from today, roughly the 2022 trough level.

Re-score triggers:
- **Next quarterly earnings** (MCO reports late July 2026 for Q2)
- **Any >15% move** per Rule 9
- **Credit market conditions** shift materially (rating issuance volumes, MA segment growth)

---

## 10. Next Review Triggers

| Ticker | Primary trigger | Secondary trigger |
|---|---|---|
| ISRG | Q2 2026 earnings (exp. late July) | Any price decline >15% from $418; FCF growth toward $4B |
| VEEV | Q2 FY2027 earnings (exp. Aug/Sep 2026) | Fundamental: FY2027 guidance revision, competitive news, Vault AI launch |
| IDXX | Q2 2026 earnings (exp. late July) | Vet visit frequency data points — any sign of sector re-acceleration |
| MCO | Q2 2026 earnings (exp. late July) | Credit market issuance volumes, MA segment growth rate |

**For VEEV (position held):** After entry, scheduled quarterly re-scores per operating-calendar.md. Model refresh mandatory upon: guidance revision, management change, Vault AI announcement, M&A, or any >15% price move (Rule 9).

**If VEEV position opened:** Log in `decisions/2026-06-09-new-position-veev.md` using the New Position Decision template in [operating-calendar.md](../framework/operating-calendar.md).

---

## 11. Open Items Before Order Placement

1. **TIKR verification** — FCF/NI conversion ratios for all four names (derived estimates in §2; confirm actual figures especially IDXX at ~77%).
2. **IDXX Net Debt/EBITDA** — derived as net cash; cross-check versus IDXX annual balance sheet for any off-balance-sheet obligations or lease-adjusted debt.
3. **Portfolio value** — needed to compute exact position size (shares) for VEEV entry per the 3–4% cap calculation in §6d.

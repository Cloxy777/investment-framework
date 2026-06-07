# Investment Framework Knowledge Base
**Quality Value + Dynamic Trimming — May 2026 Edition**
*Compiled from Notion · Last updated: June 2026*

---

## 📋 Document Index

1. [Main Strategy — 6-Phase Framework](#1-main-strategy--6-phase-framework)
2. [7 Hybrid Upgrades (40-Year Stress Test)](#2-7-hybrid-upgrades)
3. [Valuation Score Engine](#3-valuation-score-engine)
4. [Buy & Sell Price Methodology](#4-buy--sell-price-methodology)
5. [Professional Fair Value — 10-Rule Framework](#5-professional-fair-value--10-rule-framework)
6. [Claude Operating Brief — System Prompt](#6-claude-operating-brief--system-prompt)
7. [Routine Operating Calendar](#7-routine-operating-calendar)

---

## 1. Main Strategy — 6-Phase Framework

**Core Insight:** Buy profitable, high-margin, high-growth companies when cheap. Trim dynamically as valuation expands using the same metrics that identified the entry. Exit only on fundamental breakdown or extreme overvaluation.

> If you can define cheap, you can define expensive. The same valuation methodology drives both entry sizing and trim triggers.

### Phase 01 — Universe Screening

Filter the investable universe to only high-quality businesses.

- **Profitability:** Net margin >15%, ROIC >15%, positive FCF for 3+ years
- **High Margins:** Gross margin >40% OR structurally expanding margins (3yr trend)
- **Growth:** Revenue CAGR >10%, TAM expansion, pricing power evident
- **Balance Sheet:** Net debt/EBITDA <2x, no dilutive share issuance pattern
  - ⚠️ Conglomerate rule: consolidate captive financial subsidiary debt into ratio
- **Moat Signal:** Market share stable/growing, brand, network effect, switching costs
- **FCF Quality Check:** FCF/Net Income conversion ratio >70% for 2+ consecutive years. If below 70% without growth capex explanation, do not proceed to Phase 02.

**Output:** Qualified Quality List — ~50–150 companies

---

### 🌡️ Rate Environment Gate — Run Before Every Score

**Mandatory pre-check before Phase 02 scoring.**

**Step 1 — Earnings Yield Spread Test (per company)**
- Earnings Yield (EY) = 1 ÷ Forward PE
- Spread = EY − 10Y US Treasury Yield
- **Pass threshold: Spread ≥ +1.5%**
- If Spread < +1.5%: do not open a new position

**Step 2 — Rate Regime Modifier (updated quarterly)**

| 10Y Treasury Yield | Modifier | Rationale |
|--------------------|----------|-----------|
| < 2% | −1 | Easy money; valuations can stretch |
| 2–3.5% | 0 | Neutral / historical norm |
| 3.5–5% | +0.5 | Capital has real cost |
| > 5% | +1 | Strong competition from risk-free rate |

**Step 3 — Rate-Normalised Historical PE** (annual task, January, top 5 holdings only)
Recalculate using only periods where the 10Y was within ±1% of today's yield. If materially lower than raw average, apply +0.5 to that company's score for the year.

---

### Phase 02 — Valuation Scoring

Assign a valuation score (1–10) to each qualified company.

**Final Score Formula:**
```
Final Score = (FCF × 0.40) + (EV/EBIT × 0.25) + (FwdPE_adjusted × 0.20) + (PEG_or_fallback × 0.15) + Rate Regime Modifier
```

> If PEG is not applicable (non-Fast Grower), redistribute its 15% weight to EV/EBIT (making EV/EBIT weight 40%).
> Score boundary rule: if result falls on exactly X.5, round UP (more conservative). Min 1, max 10.

**FCF Yield Sub-scores:**
| FCF Yield | Sub-score |
|-----------|-----------|
| >8% | 1 |
| 6–8% | 2–3 |
| 4–6% | 4–5 |
| 2–4% | 6–7 |
| <2% | 8–10 |

**EV/EBIT Sub-scores:**
| EV/EBIT | Sub-score |
|---------|-----------|
| <12× | 1–2 |
| 12–18× | 3–4 |
| 18–22× | 5 |
| 22–28× | 6–7 |
| 28–35× | 8–9 |
| >35× | 10 |

**Forward PE sub-score:** Score 1–10 relative to sector historical norms, then apply Historical PE Modifier (Upgrade 2).

**PEG sub-score (Fast Growers with EPS growth >15% only):**
| PEG | Modifier |
|-----|----------|
| <0.8 | −1 |
| 0.8–1.2 | 0 |
| 1.2–1.8 | +0.5 |
| >2.0 | +1 |

---

### Phase 03 — Entry & Position Sizing

| Score | Label | Position Size |
|-------|-------|---------------|
| 1–3 | Very Cheap | Full position — 6–8% of portfolio |
| 4–5 | Cheap | Standard position — 3–5% of portfolio |
| 6–7 | Fair Value | Watchlist only — no new entry |
| 8–10 | Expensive | Do not buy. Begin trim protocol if held. |

**Rule:** Max 10–15 names. High conviction over diversification.

---

### Phase 04 — Continuous Monitoring

- **Quarterly review:** Re-score after each earnings report
- **Quality watch:** Flag if margins compress >3pp, ROIC drops below threshold, debt rises
- **Narrative check:** Is the growth thesis (TAM, moat, pricing power) still intact?
- **FCF quality monitor:** If FCF/Net Income drops below 70% for 2 consecutive quarters without capex explanation, flag immediately. Do not add until resolved.
- **Organic revenue check:** If acquisitions made, recalculate organic revenue CAGR separately.
- **Short thesis engagement:** If credible short thesis published, engage with specific argument independently before maintaining position.
- **Earnings quality check:** If EPS growth exceeds revenue growth by >10pp for 2+ consecutive years, verify operational performance is not masked by buybacks.

---

### Phase 05 — Dynamic Trimming (Valuation-Driven)

- **Score 6–7:** Trim 25–30% of position. Recycle into Score 1–3 names.
- **Score 8:** Trim to half-position (50% of original size)
- **Score 9–10:** Trim to tracking position — 1–2%
- **2x price milestone:** Trigger valuation re-score. If score also 7+, accelerate trim.
- **Capital recycling:** Proceeds always reinvested into current Score 1–3 names only.

---

### Phase 06 — Full Exit Triggers

✅ Valid exit reasons:
- Fundamental deterioration — margins structurally broken, ROIC falls below cost of capital
- Growth thesis broken — TAM shrinking, disruption visible, pricing power lost
- Extreme overvaluation — Score 10 sustained for 2+ quarters
- Balance sheet crisis — leverage spikes, dilutive capital raise

❌ NOT valid exit reasons:
- Price dropped (if quality intact = buy more)
- Macro fear
- Short-term earnings miss

---

### Action Table Summary

| Score Range | Status | Action |
|-------------|--------|--------|
| 1–3 | Very Cheap | Full position (6–8%) |
| 4–5 | Cheap | Standard position (3–5%) |
| 6–7 | Fair / Rich | Trim 25–30% |
| 8 | Expensive | Trim to 50% |
| 9–10 | Very Expensive | Trim to 1–2% tracking |
| 10 (2+ qtrs) | Extreme | Full Exit |

---

## 2. 7 Hybrid Upgrades

*Evidence-based upgrades from 40-year cross-framework stress test vs Buffett · Munger · Lynch · Fisher · Marks.*

### 🔴 Upgrade 1 — Owner Earnings Adjustment (CRITICAL)

Raw FCF yield penalises moat-building CapEx businesses. For businesses where **Growth CapEx > 30% of total CapEx**, replace reported FCF with:

> Owner Earnings = Net Income + D&A − Maintenance CapEx only

**Affected businesses:** MSFT (Azure), Alphabet, Meta, Amazon.

Practical impact: MSFT Owner Earnings ~$95B vs reported FCF ~$72B — a 32% difference that materially changes fair value output.

---

### 🔴 Upgrade 2 — Historical PE Relative Modifier (CRITICAL)

Add modifier to valuation score:

| Forward PE vs 10yr Avg | Adjustment |
|------------------------|------------|
| > 20% below average | −1 |
| Within ±10% | No change |
| > 20% above average | +1 |

May 2026 examples: MSFT 24.9× vs 31× avg (−20%) → Score −1. AAPL 37× vs 24.5× avg (+51%) → Score +1.

---

### 🟠 Upgrade 3 — PEG Ratio for Fast Growers (HIGH)

Apply ONLY to Lynch Fast Grower category (EPS growth > 15% for 3+ years). ⚠️ Never apply to cyclicals or stalwarts.

| PEG | Modifier |
|-----|----------|
| < 0.8 | −1 |
| 0.8–1.2 | No change |
| 1.2–1.8 | +0.5 |
| > 2.0 | +1 |

---

### 🟠 Upgrade 4 — Turnaround Sub-Gate / Fallen Angel Path (HIGH)

Businesses failing 2–4 quality criteria may enter as **Conditional Watch (2–3% max)** if ALL five conditions met:
1. ROIC historically >15% for ≥5 years in past decade
2. CEO/CFO insider buying >$500K in past 6 months (Form 4 verified)
3. Independent FV estimate showing ≥40% MOS
4. Net Debt/EBITDA <3×
5. Core moat still identifiable

Mandatory 2-quarter review. Full position only after quality gate fully re-passes.

---

### 🟡 Upgrade 5 — Debt Gate Context Adjustment (MEDIUM)

For payment networks, exchanges, asset-light businesses where 100% of debt is financial: threshold → **Net Debt/EBITDA <4×**, provided interest coverage >15× and investment grade rated. Standard 2.5× unchanged for all other business models.

---

### 🟡 Upgrade 6 — Momentum Filter: Entry Confirmation (MEDIUM)

Soft modifier — does not override quality gate.
- Above 200-day MA → proceed with scored entry
- Below 200-day MA → require ONE of: earnings beat >5%, new insider buy >$250K, or analyst upgrade with >30% target upside

---

### 🔵 Upgrade 7 — Position Cap Validated at 8% (HIGH)

Hard cap: never exceed 8% in a single position under any circumstances. Empirically validated by Verdad research (10,000 simulated portfolios).

---

### Updated Valuation Score Weighting

| Input | Weight | Notes |
|-------|--------|-------|
| FCF Yield (Owner Earnings adjusted) | 40% | Primary signal |
| EV/EBIT (<15× cheap · >30× expensive) | 25% | Unchanged |
| Forward PE + Historical PE Modifier | 20% | Adds mean-reversion signal |
| PEG Modifier (Fast Growers only) | 15% | Lynch filter |
| Rate Regime Modifier (post-score) | Additive | −1 / 0 / +0.5 / +1 based on 10Y Treasury |

---

## 3. Valuation Score Engine

**Quantitative Pre-Screen Filters:**
```
Gross margin       > 40%
Net margin         > 12%
ROIC               > 15%
Revenue growth     > 8% (3yr CAGR)
FCF positive       3 consecutive years
Net debt/EBITDA    < 2.5x
FCF yield          > 4%
EV/EBIT            < 20x
```

**Screening Tools:**
- **TIKR** — 100k+ global stocks, 335+ metrics, best for EV/EBIT, ROIC, FCF yield
- **Koyfin** — 10+ years historical financials, consistency analysis
- **Finviz** — Fast US market pre-filter, 60+ fundamental filters
- **Gurufocus** — Quality/value combo screens, Magic Formula, Buffett-style filters

**5 Qualitative Questions Before Scoring:**
1. Why are margins high? Pricing power, scale, or lucky cycle?
2. What would it take to compete with them? (Hard = moat)
3. How has management allocated capital over 5–10 years?
4. Where is growth coming from next 3–5 years?
5. What is the best bear case against owning it?
6. Could a new delivery mechanism, platform, or technology make this moat irrelevant within 5 years? *(Disruption vector check)*

---

## 4. Buy & Sell Price Methodology

### Overview

Three numbers needed before placing any order:

| Number | What it answers |
|--------|-----------------|
| **Buy Price** | Maximum price willing to pay (Fair Value × Margin of Safety) |
| **Sell Target** | Price at which to take profits |
| **Stop Loss** | Price at which to admit the thesis is wrong and exit |

---

### Step 1 — Determine Fair Value (Blended)

Always use **two methods** and triangulate. Never rely on a single valuation.

**Method A: DCF (Discounted Cash Flow)**
Best for: companies with predictable free cash flow.
- Always run 3 scenarios — base, bull, bear — varying WACC ±1% and growth ±1%
- Fair value is a *range*, not a point

**Method B: Comparable Multiples**

| Multiple | Best for |
|----------|----------|
| P/E (forward) | Profitable, stable businesses |
| EV/EBIT | Standard quality check |
| EV/EBITDA | Capital-intensive businesses |
| FCF Yield | Cash-generative compounders |
| PEG Ratio | Fast Growers (EPS growth >15%) |
| EV/Revenue | High-growth / pre-profit only |

**Triangulation Formula:**
```
Fair Value = (40% × DCF Intrinsic Value) + (60% × Multiples-Based Value)
```

---

### Step 2 — Set the Buy Price

**Margin of Safety Rule:**
```
Buy Price = Fair Value × (1 − Margin of Safety %)
```

| Company type | Margin of Safety |
|-------------|------------------|
| High quality, predictable FCF (Score 1–3) | 15–20% |
| Good quality, moderate uncertainty (Score 4–5) | 25–30% |
| Turnaround / Fallen Angel sub-gate | 35–40% |
| Speculative / pre-profit | 40–50% |

**Integration with Valuation Score:**
- Score 1–3 → Stock at or below buy price → **Enter now**
- Score 4–5 → Approaching buy price → **Set limit order**
- Score 6–7 → No MoS → **Watchlist only**
- Score 8–10 → Do not buy → **Trim or exit protocol**

---

### Step 3 — Set the Sell Target

```
Primary Sell Target = Fair Value (baseline)
Bull-Case Trim Target = Bull-Case Fair Value × 0.90
```

**Fundamental Sell Triggers (override price target):**
- ❌ Thesis broken — moat eroded, management change, key market lost
- ❌ Margin compression — gross margin falls >3pp structurally
- ❌ ROIC falls below cost of capital
- ❌ Valuation Score 10 sustained for 2+ quarters
- ❌ Balance sheet crisis — leverage spikes, dilutive capital raise
- ❌ Better opportunity — Score 1–2 name exists

---

### Step 4 — Set the Stop Loss

```
Stop Loss = Buy Price × (1 − Max Acceptable Loss %)
```

| Position type | Max loss from buy price |
|---------------|-------------------------|
| High conviction, quality (Score 1–3) | 20–25% |
| Standard position (Score 4–5) | 25–30% |
| Turnaround / Fallen Angel | 30–35% |

---

### Step 5 — Calculate Position Size

**Risk-Based Formula:**
```
Max $ Risk per trade  = Portfolio Value × 1.5%   (range: 1–2%)
Risk Per Share        = Buy Price − Stop Loss
Shares to Buy         = Max $ Risk ÷ Risk Per Share
Position Size ($)     = Shares × Buy Price
```

**Cross-check Against Allocation Caps:**

| Valuation Score | Max Position Size | Risk % |
|-----------------|-------------------|--------|
| Score 1–3 | 6–8% of portfolio | up to 2% |
| Score 4–5 | 3–5% of portfolio | 1.5% |
| Turnaround sub-gate | 2–3% of portfolio | 1% |

Take the **lower** of risk-based size and allocation cap.

---

### Step 6 — Verify Risk/Reward

```
R/R Ratio = (Sell Target − Entry Price) ÷ (Entry Price − Stop Loss)
```

**Minimum acceptable: 2:1** | Ideal: 3:1 or better

If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely.

---

### Order Setup Checklist

```
[ ] Valuation Score:                         ____  (must be ≤ 5 to enter)
[ ] DCF Fair Value:                          $______
[ ] Multiples-Based Fair Value:              $______
[ ] Blended Fair Value:                      $______
[ ] Margin of Safety %:                      ____%
[ ] BUY PRICE (limit order):                 $______
[ ] PRIMARY SELL TARGET:                     $______
[ ] BULL-CASE TRIM TARGET:                   $______
[ ] STOP LOSS:                               $______
[ ] Risk/Reward Ratio:                       ____:1  (must be ≥ 2:1)
[ ] Max $ Risk:                              $______
[ ] POSITION SIZE (shares):                  ______
[ ] POSITION SIZE ($):                       $______
[ ] Thesis invalidation triggers:            ______________________
```

---

### ⚡ RULE 0 — Always Fetch Live Prices First

> Before any order setup calculation, run a web search for each ticker. This is mandatory.

**Required steps before every analysis session:**
- **Step 1:** Search `[TICKER] stock price today` for every ticker
- **Step 2:** Record intraday price (not a prior-session close, not a portfolio snapshot)
- **Step 3:** Note 52-week range for stop placement context
- **Step 4:** Note analyst consensus PT for bull-case FV sanity check
- **Step 5:** Only then begin calculations

**What NOT to do:**
- ❌ Do not infer price from `PE × EPS` — that gives fair value, not market price
- ❌ Do not use a price from a framework note written on a prior date
- ❌ Do not use cost-basis prices as current prices
- ❌ Do not assume a price is "approximately right" without verifying

*Rule added: May 2026 — following SPGI price inference error ($450 inferred vs $411 actual → $39 error flipped verdict from limit order to buy now)*

---

## 5. Professional Fair Value — 10-Rule Framework

### Rule 1 — Sector-First Methodology Selection

| Sector | Primary Method | Secondary Method |
|--------|----------------|------------------|
| Technology / Growth | DCF (high growth) | EV/Revenue, PEG |
| Financials | P/B, DDM | P/E |
| Utilities / REITs | DDM, DCF | EV/EBITDA |
| Industrials / Manufacturing | EV/EBITDA | DCF |
| Consumer Staples | DCF, P/E | EV/EBITDA |
| Energy / Commodities | EV/EBITDA, NAV | DCF (cycle-adjusted) |
| Early-stage / Pre-profit | EV/Revenue, TAM-based | Scenario DCF |

Always run at least 2 methods. Never rely on a single model.

---

### Rule 2 — The 3-Stage DCF Standard

- **Stage 1 (Years 1–5):** Explicit detailed forecast (revenue, margins, FCF)
- **Stage 2 (Years 6–10):** Fade period — growth decelerates toward terminal rate
- **Stage 3 (Terminal):** Stable perpetuity growth (never exceed long-run GDP ~2.5–3%)

**Non-negotiable DCF inputs:**
- Discount Rate (WACC): Must reflect current risk-free rate + equity risk premium + beta
- Terminal Growth Rate: Must be ≤ long-term nominal GDP growth
- FCF Definition: Use unlevered FCF (EBIT × (1-tax) + D&A − CapEx − ΔNWC)
- **Never use net income as a proxy for FCF**

---

### Rule 3 — Weighted Valuation ("Football Field")

```
Fair Value = (W1 × DCF Value) + (W2 × Peer Multiple Value) + (W3 × DDM Value) + (W4 × Historical PE FV)
```

Suggested weights for quality large-caps: W1=40%, W2=30%, W3=20%, W4=10%

**Always output a valuation range, not a single price target.** Example: *"Fair value: $85–$102, base case $93."*

**Historical PE Cross-Check:**
```
Historical PE Fair Value = Current EPS × 10yr Average PE
```
If current price is >20% below Historical PE Fair Value → flag mean-reversion upside.

---

### Rule 4 — Sanity Check Protocol

- Implied Returns Check: Does FV imply a reasonable IRR (8–15%)?
- Multiple Sanity: Do implied exit multiples make sense vs current trading comps?
- Margin Mean-Reversion: Projecting margins above the company's 10-year peak? Justify explicitly.
- Growth vs. Reinvestment: Higher growth must come with higher reinvestment.
- Terminal Value Weight: If terminal value >75% of total DCF value, extend Stage 2.

---

### Rule 5 — Comparable Company Analysis Standards

1. Minimum 5 peers, maximum 10. Trim outliers.
2. Peers must share: similar business model, revenue scale (±50%), and geography.
3. Use **median**, not mean.
4. Apply conglomerate discount (10–20%) or size premium where appropriate.
5. Always use EV-based multiples, then back out net debt.

---

### Rule 6 — Normalize Before You Value

- **Earnings:** Strip out one-time items (restructuring, litigation, asset sales)
- **Margins:** Use 3-year average or cycle-normalized margins for cyclicals
- **Revenue:** Adjust for M&A (pro-forma), FX effects, discontinued operations
- **Debt:** Include operating leases, pension obligations, off-balance-sheet items

**Rule:** Value the *underlying business*, not the accounting statements.

---

### Rule 7 — Scenario Analysis is Mandatory

| Scenario | Weight | Key Assumption |
|----------|--------|----------------|
| Bull Case | 25% | Revenue beats, margin expansion, multiple re-rating |
| Base Case | 50% | Consensus estimates, stable margins |
| Bear Case | 25% | Revenue miss, margin compression, de-rating |

```
PW Fair Value = (0.25 × Bull) + (0.50 × Base) + (0.25 × Bear)
```

---

### Rule 8 — Margin of Safety Discipline

| Confidence Level | Required Margin of Safety |
|------------------|---------------------------|
| Wide-moat, proven compounder (>20yr ROIC >15%) | 20% below blended FV |
| Standard quality business (ROIC 15–20%) | 30% below blended FV |
| Turnaround / Fallen Angel | 40% below blended FV |
| Cyclical near trough | 35% below normalised FV |

---

### Rule 9 — Model Refresh Triggers

Mandatory re-valuation upon:
- Quarterly earnings release
- Guidance revision (up or down)
- Management change
- Material M&A announcement
- Macro shift (central bank policy, commodity price shock)
- >15% move in stock price without a fundamental trigger

---

### Rule 10 — Separate Intrinsic Value from Market Price

- Document **why** the gap exists (sentiment, macro, temporary earnings dip)
- Assign a **catalyst** and **timeline** for the gap to close
- If no catalyst identifiable within 18–24 months, revisit thesis
- Track **valuation accuracy** over time — audit your own calls

**PEG Sanity Check for Fast Growers (addition):**
- PEG <0.8 → FV may be conservative; consider increasing blended FV by 10–15%
- PEG >2.0 → FV may be generous; consider reducing blended FV by 10–15%
- ⚠️ Do not apply to cyclicals, mature stalwarts, or turnarounds.

---

## 6. Claude Operating Brief — System Prompt

> Paste this at the start of every Claude session before investment analysis.

```
You are a professional investment analyst executing the Quality Value + Dynamic Trimming framework (May 2026 edition). Your role is to assist with stock screening, valuation scoring, entry sizing, trim decisions, and portfolio rebalancing — strictly following the 6-phase framework and 7 hybrid upgrades.

ROLE & HARD CONSTRAINTS
- You are an analyst assistant, not a financial advisor. All final decisions belong to the human investor.
- You NEVER invent, estimate, or assume financial data. If a required metric is missing, stop and ask for it before proceeding.
- You NEVER act on price movements alone. Every action requires a valuation score change or a documented fundamental trigger.
- You ALWAYS show your full calculation — every sub-score, every modifier, every step. No black-box outputs.
- Score boundary rule: if the raw weighted score falls exactly on a .5, round UP (more conservative).

FRAMEWORK STRUCTURE
You operate under six phases:
  Phase 01 — Universe Screening (quality gate)
  Phase 02 — Valuation Scoring (1–10 score engine)
  Phase 03 — Entry & Position Sizing
  Phase 04 — Continuous Monitoring
  Phase 05 — Dynamic Trimming
  Phase 06 — Full Exit Triggers

Before every Phase 02 score, run the Rate Environment Gate:
  Step 1 — Earnings Yield Spread Test: EY = 1 ÷ Forward PE. Spread = EY − 10Y Treasury. Pass threshold ≥ +1.5%. Fail = no new entry.
  Step 2 — Rate Regime Modifier (apply after raw score): <2% yield → −1 | 2–3.5% → 0 | 3.5–5% → +0.5 | >5% → +1
  Step 3 — Rate-Normalised PE (annual task, top 5 holdings only, January)

HYBRID UPGRADES IN FORCE
  Upgrade 1 — Owner Earnings: if Growth CapEx >30% of total CapEx, replace FCF with Owner Earnings = Net Income + D&A − Maintenance CapEx only. Required for MSFT, GOOGL, META, AMZN.
  Upgrade 2 — Historical PE Modifier: >20% below 10yr avg PE → −1 to score | within ±10% → 0 | >20% above → +1
  Upgrade 3 — PEG (Fast Growers only, EPS growth >15% for 3+ yrs): PEG <0.8 → −1 | 0.8–1.2 → 0 | 1.2–1.8 → +0.5 | >2.0 → +1. Never apply to cyclicals.
  Upgrade 4 — Turnaround Sub-Gate: max 2–3% position. Requires all 5 conditions (historical ROIC, insider buy, 40% MOS, debt <3×, moat identifiable). 2-quarter mandatory review.
  Upgrade 5 — Debt Gate: payment networks and asset-light financials use Net Debt/EBITDA <4× if interest coverage >15× and investment grade. All others use <2.5×.
  Upgrade 6 — Momentum Filter: below 200-day MA requires one of — earnings beat >5%, insider buy >$250K, analyst upgrade with >30% target upside.
  Upgrade 7 — Hard 8% single-position cap. Never exceed under any circumstances.

VALUATION SCORE — CALCULATION RULES
Weight each input, sum to raw score, then apply modifiers:

  FCF Yield (40% weight) — use Owner Earnings yield where applicable:
    >8%       → sub-score 1
    6–8%      → sub-score 2–3
    4–6%      → sub-score 4–5
    2–4%      → sub-score 6–7
    <2%       → sub-score 8–10

  EV/EBIT (25% weight):
    <12×      → sub-score 1–2
    12–18×    → sub-score 3–4
    18–22×    → sub-score 5
    22–28×    → sub-score 6–7
    28–35×    → sub-score 8–9
    >35×      → sub-score 10

  Forward PE + Historical PE Modifier (20% weight):
    Score forward PE vs sector norms (1=very low, 10=very high), then apply Upgrade 2 modifier.

  PEG Modifier (15% weight — Fast Growers only, else use EV/EBIT for this 15%):
    Apply Upgrade 3 table.

  Rate Regime Modifier — additive, applied after raw weighted score.

Final Score = (FCF×0.40) + (EV/EBIT×0.25) + (FwdPE_adjusted×0.20) + (PEG_or_fallback×0.15) + Rate Modifier
Round to nearest integer. Minimum 1, Maximum 10.

ACTION TABLE
  Score 1–3  → BUY — Full position 6–8%
  Score 4–5  → BUY — Standard position 3–5%
  Score 6–7  → TRIM 25–30% | Watchlist only if not held
  Score 8    → TRIM to 50% of original size
  Score 9–10 → TRIM to 1–2% tracking position
  Score 10 sustained 2+ quarters → FULL EXIT

BUY/SELL ORDER SETUP (run for every BUY or TRIM action)
  Buy Price = Blended Fair Value × (1 − MoS%)
  MoS: Score 1–3 → 15–20% | Score 4–5 → 25–30% | Turnaround → 35–40%
  Stop Loss = Buy Price × (1 − Max Acceptable Loss%): Score 1–3 → 20–25% | Score 4–5 → 25–30%
  R/R = (Sell Target − Entry) ÷ (Entry − Stop Loss). Minimum 2:1. Below 2:1 = do not enter.
  Position Size = min(risk-based size, allocation cap). Risk per trade = Portfolio × 1.5%.

FULL EXIT — ONLY THESE TRIGGERS
  Fundamental deterioration: margins structurally broken, ROIC below cost of capital
  Growth thesis broken: TAM shrinking, moat eroded, pricing power lost
  Balance sheet crisis: leverage spike, dilutive raise, covenant breach
  Extreme overvaluation: Score 10 sustained for 2+ consecutive quarters
  NOT valid: price dropped on intact thesis, macro fear, short-term earnings miss

INPUT FORMAT EXPECTED
For every session, provide at minimum:
  - Task type: [SCREENING | RESCORE | NEW POSITION | TRIM REVIEW | EXIT REVIEW | REBALANCE]
  - Date and current 10Y US Treasury yield
  - Per ticker: sector, FCF yield (or Owner Earnings yield), EV/EBIT, forward PE, 10yr avg PE,
    revenue CAGR 3yr, ROIC, gross margin, net margin, net debt/EBITDA, FCF/NI conversion ratio
  - For existing holdings: current weight %, last valuation score, last review date
  - Any fundamental changes since last review (earnings, guidance, M&A, management)

OUTPUT FORMAT — ALWAYS PRODUCE IN THIS ORDER
  1. Session header: task type, date, 10Y yield, Rate Regime Modifier in effect
  2. Data gaps flagged (if any — request before proceeding)
  3. Rate Environment Gate result per ticker (Earnings Yield Spread pass/fail)
  4. Full score calculation per ticker (show every sub-score and modifier)
  5. Final valuation score + action recommendation
  6. For BUY/TRIM: full order setup (Fair Value, Buy Price, Sell Target, Stop Loss, R/R, Position Size)
  7. Portfolio rebalancing summary (if applicable)
  8. Next review trigger: date or event that requires re-score

If you do not have the data needed to complete any step, say so explicitly and list exactly what is missing.
```

---

## 7. Routine Operating Calendar

### Schedule at a Glance

| Frequency | Task | Trigger | Claude Needed? |
|-----------|------|---------|----------------|
| Daily (market days) | News & alert scan | Price move >5% intraday | No — human monitors |
| Weekly (Monday) | Earnings calendar check | Calendar-based | No — human prep |
| **After every earnings release** | **Quarterly Re-score** | Company reports earnings | **Yes — core task** |
| **Quarterly (Jan, Apr, Jul, Oct)** | **Rate Environment Gate update** | Quarter begins | **Yes** |
| **Annually (January)** | **Rate-Normalised PE recalc** | Year begins | **Yes** |
| **Annually (January)** | **Full universe re-screen** | Year begins | **Yes** |
| **Event-triggered** | **Rule 9 model refresh** | See triggers | **Yes** |
| **Event-triggered** | **Short thesis engagement** | Short report published | **Yes** |
| **Event-triggered** | **Turnaround sub-gate review** | Every 2 quarters after entry | **Yes** |

---

### Quarterly Post-Earnings Re-Score (Core Claude Task)

**When:** Within 3 business days of each holding's earnings release.
**Session type:** `RESCORE`

**Data to Pull Before the Session:**

| Metric | Where to Get It |
|--------|-----------------|
| FCF (or Owner Earnings for MSFT/META/GOOGL/AMZN) | TIKR — Cash Flow statement |
| EV/EBIT (trailing and forward) | TIKR or Koyfin |
| Forward PE | Koyfin or Finviz |
| 10-year average PE | Macrotrends.net |
| Revenue CAGR 3yr | TIKR — Income statement |
| ROIC | Koyfin or Gurufocus |
| Gross margin (current + 3yr trend) | TIKR |
| Net debt / EBITDA | TIKR or Koyfin |
| FCF / Net Income conversion ratio | Calculate: FCF ÷ Net Income (TIKR) |
| Current 10Y Treasury yield | TradingEconomics.com or CNBC |
| Current holding weight in portfolio | Your broker |

---

### Event-Triggered Rule 9 Model Refresh

| Trigger | Action Required |
|---------|-----------------|
| Stock moves >15% without known fundamental trigger | Re-score immediately. Investigate reason. |
| Quarterly earnings release | Standard re-score |
| Guidance revision (up or down) | Re-score + update fair value |
| Management change (CEO, CFO) | Re-score + thesis review + moat re-evaluation |
| Material M&A announcement | Re-score + recalculate debt ratios + moat impact |
| Macro shift (central bank policy, commodity shock) | Update Rate Environment Gate + re-score |
| Credible short report published | Short thesis engagement protocol |

---

### Data Input Template — Standard Re-Score

```
Task: RESCORE
Date: [DD MMM YYYY]
10Y US Treasury Yield: [X.XX%]
Rate Regime Modifier (active): [e.g. +0.5]

Ticker | Sector | FCF Yield (OE-adj?) | EV/EBIT | Fwd PE | 10yr Avg PE | Rev CAGR 3yr | ROIC | Gross Margin | Net Margin | Net Debt/EBITDA | FCF/NI Conv | Current Weight% | Last Score | Last Review
[TICK] | [...]  | [X.X%] (OE: Y/N)   | [XX×]  | [XX×]  | [XX×]  | [X%] | [X%] | [X%] | [X%] | [X×] | [X%] | [X%] | [X] | [MMM YYYY]

Fundamental changes since last review:
[List any: earnings beat/miss, guidance revision, M&A, management change, margin trend, organic revenue check, EPS vs revenue gap]
```

---

### Data Input Template — New Position Evaluation

```
Task: NEW POSITION
Date: [DD MMM YYYY]
10Y US Treasury Yield: [X.XX%]

Ticker: [TICK]
Sector: [sector]
Current Price: $[X]

Quality Gate (Phase 01):
  Net margin: [X%]  (threshold: >15%)
  ROIC: [X%]  (threshold: >15%)
  Revenue CAGR 3yr: [X%]  (threshold: >10%)
  Gross margin: [X%]  (threshold: >40% or expanding)
  FCF positive 3 consecutive years: [Y/N]
  Net debt/EBITDA: [X×]  (threshold: <2x)
  FCF/NI conversion ratio 2yr: [X%]  (threshold: >70%)
  Share issuance pattern: [dilutive Y/N]

Valuation Inputs (Phase 02):
  FCF Yield (Owner Earnings adjusted if applicable): [X%]
  EV/EBIT: [X×]
  Forward PE: [X×]
  10yr average PE: [X×]
  PEG (if EPS growth >15%): [X]

Fair Value Inputs:
  Last 12m FCF (or Owner Earnings): $[X]M
  FCF growth rate estimate: [X%]
  WACC: [X%]
  Shares outstanding: [X]M
  Net debt: $[X]M
  3–5 peer multiples: [list]

Qualitative Notes:
  Why are margins high?
  Moat assessment:
  Capital allocation track record:
  Growth sources next 3–5 years:
  Best bear case:
  Disruption vector check:
```

---

## Key Lessons Learned

### SPGI Price Inference Error (May 2026)
SPGI was inferred at ~$450 from "29% below 5yr avg PE." Actual price: $411. The $39 error caused MoS to read 23% (below 25% threshold → limit order) when the real MoS was 30% (above threshold → buy now). Stop loss, position size, and R/R ratio were all wrong downstream.

**Lesson:** Never infer current market price from valuation metrics. Always search for live price first.

---

## Current Portfolio Holdings (as of May 2026)

MSFT, NVDA, AMZN, META, AVGO, GOOG, DUOL, NFLX, NOW, SPOT, TLT, NKE, CSGP, CSCO, SPGI

---

*Compiled: June 2026 · Source: Notion Investment Framework Pages · Quality Value + Dynamic Trimming Framework*

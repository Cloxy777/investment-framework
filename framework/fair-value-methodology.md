# Fair Value & Buy/Sell Price Methodology

Three numbers needed before placing any order:

| Number | What it answers |
|--------|-----------------|
| **Buy Price** | Maximum price willing to pay (Fair Value × Margin of Safety) |
| **Sell Target** | Price at which to take profits |
| **Stop Loss** | Price at which to admit the thesis is wrong and exit |

---

## ⚡ Rule 0 — Always Fetch Live Prices First

> Before any order setup calculation, search for each ticker's live price. This is mandatory.

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

> **Lesson — SPGI Price Inference Error (May 2026):** SPGI was inferred at ~$450 from "29% below 5yr avg PE." Actual price: $411. The $39 error caused MoS to read 23% (below 25% threshold → limit order) when the real MoS was 30% (above threshold → buy now). Stop loss, position size, and R/R ratio were all wrong downstream. *Rule added following this incident.*

---

## Step 1 — Determine Fair Value (Blended)

Always use **two methods** and triangulate. Never rely on a single valuation.

**Method A: DCF (Discounted Cash Flow)** — best for predictable-FCF companies.
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

## Step 2 — Set the Buy Price

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

## Step 3 — Set the Sell Target

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

## Step 4 — Set the Stop Loss

```
Stop Loss = Buy Price × (1 − Max Acceptable Loss %)
```

| Position type | Max loss from buy price |
|---------------|-------------------------|
| High conviction, quality (Score 1–3) | 20–25% |
| Standard position (Score 4–5) | 25–30% |
| Turnaround / Fallen Angel | 30–35% |

---

## Step 5 — Calculate Position Size

```
Max $ Risk per trade  = Portfolio Value × 1.5%   (range: 1–2%)
Risk Per Share        = Buy Price − Stop Loss
Shares to Buy         = Max $ Risk ÷ Risk Per Share
Position Size ($)     = Shares × Buy Price
```

**Cross-check against allocation caps — take the lower of risk-based size and cap:**

| Valuation Score | Max Position Size | Risk % |
|-----------------|-------------------|--------|
| Score 1–3 | 6–8% of portfolio | up to 2% |
| Score 4–5 | 3–5% of portfolio | 1.5% |
| Turnaround sub-gate | 2–3% of portfolio | 1% |

---

## Step 6 — Verify Risk/Reward

```
R/R Ratio = (Sell Target − Entry Price) ÷ (Entry Price − Stop Loss)
```

**Minimum acceptable: 2:1** | Ideal: 3:1 or better

If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely.

---

## Order Setup Checklist

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

# Professional Fair Value — 10-Rule Framework

## Rule 1 — Sector-First Methodology Selection

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

## Rule 2 — The 3-Stage DCF Standard

- **Stage 1 (Years 1–5):** Explicit detailed forecast (revenue, margins, FCF)
- **Stage 2 (Years 6–10):** Fade period — growth decelerates toward terminal rate
- **Stage 3 (Terminal):** Stable perpetuity growth (never exceed long-run GDP ~2.5–3%)

**Non-negotiable DCF inputs:**
- Discount Rate (WACC): Must reflect current risk-free rate + equity risk premium + beta
- Terminal Growth Rate: Must be ≤ long-term nominal GDP growth
- FCF Definition: Use unlevered FCF (EBIT × (1-tax) + D&A − CapEx − ΔNWC)
- **Never use net income as a proxy for FCF**

## Rule 3 — Weighted Valuation ("Football Field")

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

## Rule 4 — Sanity Check Protocol

- Implied Returns Check: Does FV imply a reasonable IRR (8–15%)?
- Multiple Sanity: Do implied exit multiples make sense vs current trading comps?
- Margin Mean-Reversion: Projecting margins above the company's 10-year peak? Justify explicitly.
- Growth vs. Reinvestment: Higher growth must come with higher reinvestment.
- Terminal Value Weight: If terminal value >75% of total DCF value, extend Stage 2.

## Rule 5 — Comparable Company Analysis Standards

1. Minimum 5 peers, maximum 10. Trim outliers.
2. Peers must share: similar business model, revenue scale (±50%), and geography.
3. Use **median**, not mean.
4. Apply conglomerate discount (10–20%) or size premium where appropriate.
5. Always use EV-based multiples, then back out net debt.

## Rule 6 — Normalize Before You Value

- **Earnings:** Strip out one-time items (restructuring, litigation, asset sales)
- **Margins:** Use 3-year average or cycle-normalized margins for cyclicals
- **Revenue:** Adjust for M&A (pro-forma), FX effects, discontinued operations
- **Debt:** Include operating leases, pension obligations, off-balance-sheet items

**Rule:** Value the *underlying business*, not the accounting statements.

## Rule 7 — Scenario Analysis is Mandatory

| Scenario | Weight | Key Assumption |
|----------|--------|----------------|
| Bull Case | 25% | Revenue beats, margin expansion, multiple re-rating |
| Base Case | 50% | Consensus estimates, stable margins |
| Bear Case | 25% | Revenue miss, margin compression, de-rating |

```
PW Fair Value = (0.25 × Bull) + (0.50 × Base) + (0.25 × Bear)
```

## Rule 8 — Margin of Safety Discipline

| Confidence Level | Required Margin of Safety |
|------------------|---------------------------|
| Wide-moat, proven compounder (>20yr ROIC >15%) | 20% below blended FV |
| Standard quality business (ROIC 15–20%) | 30% below blended FV |
| Turnaround / Fallen Angel | 40% below blended FV |
| Cyclical near trough | 35% below normalised FV |

## Rule 9 — Model Refresh Triggers

Mandatory re-valuation upon:
- Quarterly earnings release
- Guidance revision (up or down)
- Management change
- Material M&A announcement
- Macro shift (central bank policy, commodity price shock)
- >15% move in stock price without a fundamental trigger

## Rule 10 — Separate Intrinsic Value from Market Price

- Document **why** the gap exists (sentiment, macro, temporary earnings dip)
- Assign a **catalyst** and **timeline** for the gap to close
- If no catalyst identifiable within 18–24 months, revisit thesis
- Track **valuation accuracy** over time — audit your own calls

**PEG Sanity Check for Fast Growers (addition):**
- PEG <0.8 → FV may be conservative; consider increasing blended FV by 10–15%
- PEG >2.0 → FV may be generous; consider reducing blended FV by 10–15%
- ⚠️ Do not apply to cyclicals, mature stalwarts, or turnarounds.

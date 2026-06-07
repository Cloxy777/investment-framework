# 💰 Buy & Sell Price Methodology — Order Setup Rules

# Overview

After evaluating a company against the Quality Value framework, you need **three concrete numbers** before placing any order. This page defines how to derive them.

| Number | What it answers |
| --- | --- |
| **Buy Price** | Maximum price you're willing to pay (Fair Value × Margin of Safety) |
| **Sell Target** | Price at which you take profits (Fair Value or bull-case FV) |
| **Stop Loss** | Price at which you admit the thesis is wrong and exit |

These three numbers also determine **Position Size** — how much capital to deploy.

> **Core principle:** If you can define cheap, you can define expensive. The same valuation methodology that sets your entry also sets your exit.
> 

---

# Step 1 — Determine Fair Value (Blended)

Always use **two methods** and triangulate. Never rely on a single valuation.

## Method A: DCF (Discounted Cash Flow) — Intrinsic Value

Best for: companies with predictable free cash flow (mature, profitable businesses)

**Inputs needed:**

- Last 12-month Free Cash Flow (FCF) — use Owner Earnings for capex-heavy platforms
- FCF growth rate (historical CAGR or conservative estimate)
- Discount rate / WACC (use 8–10%)
- Terminal growth rate (use 2–3%)
- Shares outstanding, net debt

**Process:**

1. Project FCF for 5–10 years at your growth rate
2. Discount each year back to present using WACC
3. Add Terminal Value: `FCF_final × (1 + g) / (WACC − g)`
4. Sum discounted values → Enterprise Value
5. Subtract net debt, divide by shares → **Intrinsic Value Per Share**

> ⚠️ **Always run 3 scenarios** — base, bull, bear — by varying WACC ±1% and growth ±1%. Your fair value is a *range*, not a point.
> 

## Method B: Comparable Multiples — Relative Value

Best for: cross-checking DCF, fast-growing companies, sector pricing

| Multiple | Best for |
| --- | --- |
| P/E (forward) | Profitable, stable businesses |
| EV/EBIT | Standard quality check — matches QV framework |
| EV/EBITDA | Capital-intensive businesses |
| FCF Yield | Cash-generative compounders (invert for FV) |
| PEG Ratio | Fast Growers (EPS growth >15%) — matches Upgrade 3 |
| EV/Revenue | High-growth / pre-profit only |

**Process:**

1. Identify 3–5 true peers (same industry, similar growth/margin profile)
2. Calculate the **median multiple** of the peer group
3. Apply to your company's metric → Relative Fair Value Per Share
4. Cross-check against your DCF result

## Triangulation Formula

```
Fair Value = (40% × DCF Intrinsic Value) + (60% × Multiples-Based Value)
```

Adjust weights based on confidence in FCF predictability. For high-growth companies with lumpy FCF, lean more on multiples.

---

# Step 2 — Set the Buy Price

## The Margin of Safety Rule

```
Buy Price = Fair Value × (1 − Margin of Safety %)
```

| Company type | Margin of Safety |
| --- | --- |
| High quality, predictable FCF (Score 1–3) | 15–20% |
| Good quality, moderate uncertainty (Score 4–5) | 25–30% |
| Turnaround / Fallen Angel sub-gate | 35–40% |
| Speculative / pre-profit | 40–50% |

**What the MoS protects against:**

- Errors in your model assumptions
- Unforeseen competitive threats
- Macro deterioration
- Management execution failure

> If you miss the entry because the stock never dips to your buy price — that's fine. Discipline beats FOMO. Move to the next candidate.
> 

### Integration with Valuation Score

The MoS directly maps to the framework's **Valuation Score**:

- Score 1–3 (Very Cheap) → Stock is already at or below your buy price → **Enter now**
- Score 4–5 (Cheap) → Stock is approaching buy price → **Set limit order**
- Score 6–7 (Fair Value) → No MoS → **Watchlist only, no new entry**
- Score 8–10 (Expensive) → Do not buy → **Trim or exit protocol**

---

# Step 3 — Set the Sell Target

## Primary Sell Target: Fair Value

When the market price reaches your Fair Value estimate, the margin of safety has been consumed. At Fair Value, risk/reward is neutral.

```
Primary Sell Target = Fair Value (baseline)
```

This corresponds to the framework reaching **Valuation Score 6–7** → trigger 25–30% trim.

## Bull-Case Trim Target

If your bull-case DCF (optimistic growth, lower WACC) gives a significantly higher value:

```
Bull-Case Trim Target = Bull-Case Fair Value × 0.90
```

Sell 30–50% of the position at the primary target. Hold the rest to the bull-case target.

## Fundamental Sell Triggers (override price target)

Exit the entire position if **any** of the following occur — regardless of current price:

- ❌ **Thesis broken** — core moat eroded, management change, key market lost
- ❌ **Margin compression** — gross margin falls >3pp structurally (not one-quarter noise)
- ❌ **ROIC falls below cost of capital** — the business is destroying value
- ❌ **Valuation Score 10 sustained for 2+ quarters** — extreme overvaluation
- ❌ **Balance sheet crisis** — leverage spikes, dilutive capital raise, covenant breach
- ❌ **Better opportunity** — a Score 1–2 name exists; recycle capital

> ✅ Valid reason to hold despite price drop: thesis fully intact, quality metrics unchanged, valuation score improving.
> 

---

# Step 4 — Set the Stop Loss

A stop loss defines the point where you admit the thesis is wrong and exit to preserve capital.

## Valuation-Based Stop (recommended for fundamental investors)

Set stop at a price that implies the business is *clearly* impaired:

```
Stop Loss = Buy Price × (1 − Max Acceptable Loss %)
```

| Position type | Max loss from buy price |
| --- | --- |
| High conviction, quality (Score 1–3) | 20–25% |
| Standard position (Score 4–5) | 25–30% |
| Turnaround / Fallen Angel | 30–35% |

## Technical Confirmation (optional refinement)

For timing precision, place stop below a key structural level:

- Below the 52-week low
- Below a major prior consolidation base
- Below the 200-day moving average (also used in Upgrade 6 — Momentum Filter)

> Hard stops (automatic sell orders) are preferred — they remove emotion and enforce the rule.
> 

---

# Step 5 — Calculate Position Size

Never size a position based on conviction alone. Size it based on **how much you're willing to lose**.

## Risk-Based Formula

```
Max $ Risk per trade  = Portfolio Value × 1.5%   (range: 1–2%)
Risk Per Share        = Buy Price − Stop Loss
Shares to Buy         = Max $ Risk ÷ Risk Per Share
Position Size ($)     = Shares × Buy Price
```

## Cross-check Against Framework Allocation Caps

| Valuation Score | Max Position Size | Risk % |
| --- | --- | --- |
| Score 1–3 (Very Cheap) | 6–8% of portfolio | up to 2% |
| Score 4–5 (Cheap) | 3–5% of portfolio | 1.5% |
| Turnaround sub-gate | 2–3% of portfolio | 1% |

Take the **lower** of the risk-based size and the allocation cap. Never exceed 8% in a single position (Upgrade 7 — empirically validated).

---

# Step 6 — Verify Risk/Reward Before Placing Order

```
R/R Ratio = (Sell Target − Entry Price) ÷ (Entry Price − Stop Loss)
```

**Minimum acceptable: 2:1**

Ideal: 3:1 or better

If R/R is below 2:1:

- Wait for a lower entry price, OR
- Find a tighter/more precise stop level, OR
- Pass on the trade entirely

---

# Order Setup Checklist

Fill this in **before placing any order**:

```
[ ] Valuation Score (from QV framework):     ____  (must be ≤ 5 to enter)
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

# Methodology by Company Type

| Company Type | Primary Valuation Method | Key Multiples | MoS | Notes |
| --- | --- | --- | --- | --- |
| Quality compounder | DCF (Owner Earnings) + Multiples | FCF Yield, EV/EBIT | 15–25% | Core of QV framework |
| High-growth tech | Multiples > DCF | EV/EBIT, PEG | 25–35% | Use PEG modifier (Upgrade 3) |
| Fallen Angel / Turnaround | DCF (normalised earnings) | EV/EBIT vs history | 35–40% | Requires Turnaround Sub-Gate (Upgrade 4) |
| Cyclical / industrial | Normalised earnings DCF | EV/EBITDA mid-cycle | 30–40% | Never value at peak earnings |
| Financial (bank/insurer) | DDM or P/BV | P/BV, P/E | 20–30% | Debt context (Upgrade 5) |
| Pre-profit / early stage | Revenue multiples | EV/Revenue | 40–50% | Must have path to profitability |

---

# What NOT To Do

- ❌ Don't use a single valuation method — always triangulate with at least two
- ❌ Don't skip the MoS — paying fair value means everything must go right to earn a return
- ❌ Don't place an order with R/R below 2:1 — even great businesses can disappoint
- ❌ Don't size by conviction alone — always tie position size to risk per share and stop placement
- ❌ Don't ignore fundamental sell triggers — a stop loss and a thesis-break rule are different things
- ❌ Don't hold through a 3× gain without trimming — use the Dynamic Trimming protocol (Phase 05)

---

> *Created: May 2026 · Part of Quality Value + Dynamic Trimming Framework · Apply after every evaluation against the 6-Phase Framework*
>
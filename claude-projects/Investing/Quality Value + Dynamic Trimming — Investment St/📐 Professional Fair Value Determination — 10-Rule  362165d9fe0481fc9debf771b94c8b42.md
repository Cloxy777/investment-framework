# 📐 Professional Fair Value Determination — 10-Rule Framework

## Overview

A professional, repeatable framework for determining the intrinsic fair value of any publicly traded stock. Built May 2026. Apply before every new position.

---

## Rule 1 — Sector-First Methodology Selection

Never apply a one-size-fits-all model. The sector dictates the primary valuation method.

| Sector | Primary Method | Secondary Method |
| --- | --- | --- |
| Technology / Growth | DCF (high growth) | EV/Revenue, PEG |
| Financials (Banks, Insurance) | P/B, DDM | P/E |
| Utilities / REITs | DDM, DCF | EV/EBITDA |
| Industrials / Manufacturing | EV/EBITDA | DCF |
| Consumer Staples | DCF, P/E | EV/EBITDA |
| Energy / Commodities | EV/EBITDA, NAV | DCF (cycle-adjusted) |
| Early-stage / Pre-profit | EV/Revenue, TAM-based | Scenario DCF |

**Rule:** Always run at least 2 methods and weight them by relevance. Never rely on a single model.

---

## Rule 2 — The 3-Stage DCF Standard

A professional DCF must use 3 stages, not a simple perpetuity.

- **Stage 1 (Years 1–5):** Explicit detailed forecast (revenue, margins, FCF)
- **Stage 2 (Years 6–10):** Fade period — growth decelerates toward terminal rate
- **Stage 3 (Terminal):** Stable perpetuity growth (never exceed long-run GDP ~2.5–3%)

**Non-negotiable DCF inputs:**

- **Discount Rate (WACC):** Must reflect current risk-free rate + equity risk premium + beta
- **Terminal Growth Rate:** Must be ≤ long-term nominal GDP growth
- **FCF Definition:** Use unlevered FCF (EBIT × (1-tax) + D&A − CapEx − ΔNWC)
- **Never use net income as a proxy for FCF**

---

## Rule 3 — Weighted Valuation ("Football Field")

Assign weights to each method based on reliability for that company.

**Formula:** Fair Value = (W1 × DCF Value) + (W2 × Peer Multiple Value) + (W3 × DDM Value)

**Always output a valuation range, not a single price target.** Quote: *"Fair value: $85–$102, base case $93."*

---

## Rule 4 — Sanity Check Protocol

Every valuation must pass these checks before being finalized:

- Implied Returns Check: Does fair value imply a reasonable IRR (8–15%) for an equity investor?
- Multiple Sanity: Do implied exit multiples make sense vs. current trading comps?
- Margin Mean-Reversion: Are you projecting margins above the company's 10-year peak? If yes, justify explicitly.
- Growth vs. Reinvestment: Higher growth must come with higher reinvestment (CapEx + NWC).
- Terminal Value Weight: If terminal value > 75% of total DCF value, extend Stage 2.

---

## Rule 5 — Comparable Company Analysis (Comps) Standards

1. Minimum 5 peers, maximum 10. Trim outliers (highest & lowest multiple).
2. Peers must share: similar business model, revenue scale (±50%), and geography.
3. Use **median**, not mean — means are distorted by outliers.
4. Apply a conglomerate discount (10–20%) or size premium where appropriate.
5. Always use EV-based multiples, then back out net debt to get equity value.

---

## Rule 6 — Normalize Before You Value

Raw financials are never used directly.

- **Earnings:** Strip out one-time items (restructuring, litigation, asset sales)
- **Margins:** Use 3-year average or cycle-normalized margins for cyclicals
- **Revenue:** Adjust for M&A (pro-forma), FX effects, discontinued operations
- **Debt:** Include operating leases, pension obligations, off-balance-sheet items

**Rule:** Value the *underlying business*, not the accounting statements.

---

## Rule 7 — Scenario Analysis is Mandatory

A single-point estimate is not professional. Always build 3 scenarios:

| Scenario | Weight | Key Assumption |
| --- | --- | --- |
| Bull Case | 25% | Revenue beats, margin expansion, multiple re-rating |
| Base Case | 50% | Consensus estimates, stable margins |
| Bear Case | 25% | Revenue miss, margin compression, de-rating |

**Formula:** PW Fair Value = (0.25 × Bull) + (0.50 × Base) + (0.25 × Bear)

Identify the 2–3 key value drivers that most impact the output and stress-test those specifically.

---

## Rule 8 — Margin of Safety Discipline

| Confidence Level | Required Margin of Safety |
| --- | --- |
| High (stable business, predictable FCF) | 10–15% below fair value |
| Medium (some uncertainty in projections) | 20–30% below fair value |
| Low (high uncertainty, early-stage) | 40–50% below fair value |

**Never recommend a stock trading at or above fair value**, regardless of narrative.

---

## Rule 9 — Model Refresh Triggers

A fair value estimate has an **expiry**. Mandatory re-valuation upon:

- Quarterly earnings release
- Guidance revision (up or down)
- Management change
- Material M&A announcement
- Macro shift (central bank policy, commodity price shock)
- 
    
    > 15% move in stock price without a fundamental trigger
    > 

---

## Rule 10 — Separate Intrinsic Value from Market Price

Intrinsic Value ≠ Market Price (in the short run)

- Document **why** the gap exists (sentiment, macro, temporary earnings dip)
- Assign a **catalyst** and **timeline** for the gap to close
- If you cannot identify a catalyst within 18–24 months, revisit your thesis
- Track your **valuation accuracy** over time — good analysts audit their own calls

---

## Professional Output Template

Every valuation should produce:

1. Company Overview & Business Model Summary
2. Key Value Drivers (top 3)
3. Financial Model (normalized, 3-stage)
4. Valuation Bridge (DCF + Comps + DDM with weights)
5. Football Field Chart (range of outcomes by method)
6. Scenario Analysis (Bull / Base / Bear)
7. Catalysts & Risks
8. Final Fair Value Range + Buy/Hold/Sell vs. Current Price

---

## Applied Examples (May 2026)

| Ticker | Current Price | Fair Value (Base) | PW Fair Value | Discount | Verdict |
| --- | --- | --- | --- | --- | --- |
| ADBE | $245 | $520 | $508 | 53% | Strong Buy |
| DUOL | $108 | $265 | $273 | 59% | High Conv. Buy |
| CRWV | $107 | $145 | $142 | 26% | Hold / Wait |

---

> ⚠️ This framework is for analytical purposes only. Not financial advice.
> 

---

# 🔬 Hybrid Upgrades — Fair Value Methodology (May 2026)

> Additions to Rule 3 (Weighted Valuation) and Rule 8 (Margin of Safety) from 40-year cross-framework stress test.
> 

## Addition to Rule 3 — Owner Earnings DCF (Critical Fix)

For businesses where Growth CapEx > 30% of total CapEx (cloud infra, AI platforms, network businesses), the standard FCF figure **understates true earnings power**. Use Owner Earnings as the DCF numerator:

> Owner Earnings = Net Income + D&A − Maintenance CapEx only
> 

Growth CapEx (moat-building investment) is excluded from the deduction — it is an asset, not an expense.

Businesses requiring this adjustment: Microsoft, Alphabet, Meta, Amazon, Salesforce.

Practical impact: MSFT Owner Earnings ~$95B vs reported FCF ~$72B — a 32% difference that materially changes fair value output.

## Addition to Rule 3 — Historical PE Cross-Check

Add a fourth column to the Football Field after DCF, Peer Multiple, and DDM:

**Historical PE Fair Value = Current EPS × 10yr Average PE**

If current price is > 20% below this Historical PE Fair Value → add a note flagging mean-reversion upside. Weight it at 10% in the final blended fair value formula:

> FV = (W1 × DCF) + (W2 × Peer Multiple) + (W3 × DDM) + (W4 × Historical PE FV)
> 

Suggested weights for quality large-caps: W1 = 40%, W2 = 30%, W3 = 20%, W4 = 10%.

May 2026 example — MSFT: Historical PE FV = $16.86 EPS × 31× = **$522**. Current price $419 = 20% discount to own history → strong mean-reversion signal.

## Addition to Rule 8 — Margin of Safety by Category

| Business Category | Minimum MOS Required |
| --- | --- |
| Wide-moat, proven compounder (>20yr ROIC >15%) | 20% below blended FV |
| Standard quality business (ROIC 15–20%) | 30% below blended FV |
| Turnaround / Fallen Angel (Upgrade 4 path) | 40% below blended FV |
| Cyclical near trough | 35% below normalised FV |

Previously Rule 8 applied a single 30% MOS floor. Differentiated by category to prevent both overpaying for quality and over-discounting turnarounds.

## Addition to Rule 10 — PEG Sanity Check for Fast Growers

Before finalising Buy/Hold/Sell, add a PEG check for businesses with EPS growth > 15%:

- PEG < 0.8 → Fair value estimate may be conservative; consider increasing blended FV by 10–15%
- PEG > 2.0 → Fair value estimate may be generous; consider reducing blended FV by 10–15%

⚠️ Do not apply to cyclicals, mature stalwarts, or turnarounds.

---

## Updated Output Table Format

Add two columns to the standard output table:

| Ticker | Price | FV Base | FV w/ Hist PE | MOS | PEG | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| META | $638 | $900 | $820 | 29% | 0.90 | BUY |
| MSFT | $419 | $520 | $522 | 20% | 1.40 | BUY |
| MA | $568 | $645 | $600 | 12% | 1.59 | HOLD |
| V | $336 | $400 | $390 | 14% | 1.79 | WAIT |
| NKE | $44 | $75 | $68 | 42% | N/A | Conditional Watch |

*Updated: May 24, 2026 · Source: 40-year stress test vs Master Investor Framework*
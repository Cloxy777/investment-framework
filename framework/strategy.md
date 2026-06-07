# Quality Value + Dynamic Trimming — Strategy
*May 2026 Edition*

**Core Insight:** Buy profitable, high-margin, high-growth companies when cheap. Trim dynamically as valuation expands using the same metrics that identified the entry. Exit only on fundamental breakdown or extreme overvaluation.

> If you can define cheap, you can define expensive. The same valuation methodology drives both entry sizing and trim triggers.

---

## Phase 01 — Universe Screening

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

## Rate Environment Gate — Run Before Every Score

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

## Phase 02 — Valuation Scoring

Assign a valuation score (1–10) to each qualified company. Full scoring mechanics (formula, sub-score tables, pre-screen filters, tools) live in [valuation-scoring.md](valuation-scoring.md).

> Score boundary rule: if result falls on exactly X.5, round UP (more conservative). Min 1, max 10.

---

## Phase 03 — Entry & Position Sizing

| Score | Label | Position Size |
|-------|-------|---------------|
| 1–3 | Very Cheap | Full position — 6–8% of portfolio |
| 4–5 | Cheap | Standard position — 3–5% of portfolio |
| 6–7 | Fair Value | Watchlist only — no new entry |
| 8–10 | Expensive | Do not buy. Begin trim protocol if held. |

**Rule:** Max 10–15 names. High conviction over diversification.

---

## Phase 04 — Continuous Monitoring

- **Quarterly review:** Re-score after each earnings report
- **Quality watch:** Flag if margins compress >3pp, ROIC drops below threshold, debt rises
- **Narrative check:** Is the growth thesis (TAM, moat, pricing power) still intact?
- **FCF quality monitor:** If FCF/Net Income drops below 70% for 2 consecutive quarters without capex explanation, flag immediately. Do not add until resolved.
- **Organic revenue check:** If acquisitions made, recalculate organic revenue CAGR separately.
- **Short thesis engagement:** If credible short thesis published, engage with specific argument independently before maintaining position.
- **Earnings quality check:** If EPS growth exceeds revenue growth by >10pp for 2+ consecutive years, verify operational performance is not masked by buybacks.

---

## Phase 05 — Dynamic Trimming (Price-Target-Driven)

Trims are triggered by **price reaching a fair-value-derived target**, not by the valuation score crossing a band. The two trigger prices are the Primary Sell Target and Bull-Case Trim Target already defined in [fair-value-methodology.md](fair-value-methodology.md) Step 3:

- **Price reaches Primary Sell Target** (= Fair Value, baseline): Trim 50% of the position. Recycle into Score 1–3 names.
- **Price reaches Bull-Case Trim Target** (= Bull-Case Fair Value × 0.90): Trim the remainder to a tracking position — 1–2%.
- **2x price milestone:** Trigger valuation re-score. If price has also crossed a Sell Target, accelerate the trim.
- **Capital recycling:** Proceeds always reinvested into current Score 1–3 names only.

The 1–10 valuation score still governs **BUY** sizing (Score 1–3 / 4–5 bands below) and is still refreshed on the 2x price milestone — it no longer mechanically triggers a trim on its own. Phase 06's "Score 10 sustained 2+ quarters" remains a separate, rarer full-**exit** backstop (see below), distinct from routine trimming.

---

## Phase 06 — Full Exit Triggers

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

## Action Table Summary

| Score / Price Signal | Status | Action |
|-------------|--------|--------|
| Score 1–3 | Very Cheap | Full position (6–8%) |
| Score 4–5 | Cheap | Standard position (3–5%) |
| Price ≥ Primary Sell Target (Fair Value) | Fairly Valued | Trim 50% |
| Price ≥ Bull-Case Trim Target (Bull-Case FV × 0.90) | Richly Valued | Trim remainder to 1–2% tracking |
| Score 10 (2+ qtrs) | Extreme | Full Exit |

---

## 7 Hybrid Upgrades

*Evidence-based upgrades from a 40-year cross-framework stress test vs Buffett · Munger · Lynch · Fisher · Marks.*

### 🔴 Upgrade 1 — Owner Earnings Adjustment (CRITICAL)

Raw FCF yield penalises moat-building CapEx businesses. For businesses where **Growth CapEx > 30% of total CapEx**, replace reported FCF with:

> Owner Earnings = Net Income + D&A − Maintenance CapEx only

**Affected businesses:** MSFT (Azure), Alphabet, Meta, Amazon.

Practical impact: MSFT Owner Earnings ~$95B vs reported FCF ~$72B — a 32% difference that materially changes fair value output.

### 🔴 Upgrade 2 — Historical PE Relative Modifier (CRITICAL)

| Forward PE vs 10yr Avg | Adjustment |
|------------------------|------------|
| > 20% below average | −1 |
| Within ±10% | No change |
| > 20% above average | +1 |

May 2026 examples: MSFT 24.9× vs 31× avg (−20%) → Score −1. AAPL 37× vs 24.5× avg (+51%) → Score +1.

### 🟠 Upgrade 3 — PEG Ratio for Fast Growers (HIGH)

Apply ONLY to Lynch Fast Grower category (EPS growth > 15% for 3+ years). ⚠️ Never apply to cyclicals or stalwarts.

| PEG | Modifier |
|-----|----------|
| < 0.8 | −1 |
| 0.8–1.2 | No change |
| 1.2–1.8 | +0.5 |
| > 2.0 | +1 |

### 🟠 Upgrade 4 — Turnaround Sub-Gate / Fallen Angel Path (HIGH)

Businesses failing 2–4 quality criteria may enter as **Conditional Watch (2–3% max)** if ALL five conditions met:
1. ROIC historically >15% for ≥5 years in past decade
2. CEO/CFO insider buying >$500K in past 6 months (Form 4 verified)
3. Independent FV estimate showing ≥40% MOS
4. Net Debt/EBITDA <3×
5. Core moat still identifiable

Mandatory 2-quarter review. Full position only after quality gate fully re-passes.

### 🟡 Upgrade 5 — Debt Gate Context Adjustment (MEDIUM)

For payment networks, exchanges, asset-light businesses where 100% of debt is financial: threshold → **Net Debt/EBITDA <4×**, provided interest coverage >15× and investment grade rated. Standard 2.5× unchanged for all other business models.

### 🟡 Upgrade 6 — Momentum Filter: Entry Confirmation (MEDIUM)

Soft modifier — does not override quality gate.
- Above 200-day MA → proceed with scored entry
- Below 200-day MA → require ONE of: earnings beat >5%, new insider buy >$250K, or analyst upgrade with >30% target upside

### 🔵 Upgrade 7 — Hard Position Cap at 15%

Hard cap: never exceed 15% in a single position under any circumstances. (Note: Verdad research empirically validated 8% across 10,000 simulated portfolios; 15% is a deliberate user override of that backing — see [decisions/2026-06-07-framework-change-cap-and-trim-rule.md](../decisions/2026-06-07-framework-change-cap-and-trim-rule.md) for the rationale.)

---

## Updated Valuation Score Weighting

| Input | Weight | Notes |
|-------|--------|-------|
| FCF Yield (Owner Earnings adjusted) | 40% | Primary signal |
| EV/EBIT (<15× cheap · >30× expensive) | 25% | Unchanged |
| Forward PE + Historical PE Modifier | 20% | Adds mean-reversion signal |
| PEG Modifier (Fast Growers only) | 15% | Lynch filter |
| Rate Regime Modifier (post-score) | Additive | −1 / 0 / +0.5 / +1 based on 10Y Treasury |

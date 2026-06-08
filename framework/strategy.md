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
- Spread ≥ +1.5%: no adjustment
- Spread < +1.5%: apply **+0.5 to the valuation score** — a yellow flag that raises the bar the bottom-up case must clear, rather than an outright veto

*Changed 2026-06-07 from a hard "do not open a new position" block to an additive modifier — see [investor-philosophy-alignment.md](investor-philosophy-alignment.md). Buffett treats interest rates as "gravity" on asset values — a valuation anchor, not a binary switch — and Lynch/Munger both warn against letting a macro read override a strong bottom-up case. This keeps the rate-sensitivity (the bar gets harder to clear) without letting it veto an exceptional company outright, and now mirrors how Step 2's Rate Regime Modifier already works.*

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

## Phase 05 — Dynamic Trimming (Valuation-Driven)

*Trim trigger raised 2026-06-07 from Score 6–7 to Score 8+ — see [investor-philosophy-alignment.md](investor-philosophy-alignment.md). Trimming the moment a position crosses from "Cheap" into merely "Fair Value" was a materially higher-turnover posture than Buffett ("favorite holding period is forever"), Munger ("sit on your ass investing" / the "croupier's take" on trading friction), or Terry Smith (~3–4% annual turnover, "do nothing") actually practice. Score 6–7 is now hold-and-watch only — it already carries a "Watchlist only, no new entry" label in Phase 03; there's no reason for it to also be a trim trigger. The framework keeps its teeth at the extremes, where even these long-term compounders do trim (e.g., Buffett's 2024 Apple cut once it became dramatically oversized and rich).*

- **Score 6–7:** Hold. No new entry (Watchlist only — Phase 03). No trim — fair value alone is not a sell signal.
- **Score 8:** Trim 25–30% of position. Recycle into Score 1–3 names.
- **Score 9:** Trim to half-position (50% of original size)
- **Score 10:** Trim to tracking position — 1–2%
- **2x price milestone:** Trigger valuation re-score. If score also 8+, accelerate trim.
- **Capital recycling:** Proceeds always reinvested into current Score 1–3 names only.

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

| Score Range | Status | Action |
|-------------|--------|--------|
| 1–3 | Very Cheap | Full position (6–8%) |
| 4–5 | Cheap | Standard position (3–5%) |
| 6–7 | Fair Value | Hold — watch only, no new entry, no trim |
| 8 | Expensive | Trim 25–30% |
| 9 | Very Expensive | Trim to 50% |
| 10 | Extreme | Trim to 1–2% tracking |
| 10 (2+ qtrs) | Sustained Extreme | Full Exit |

---

## 7 Hybrid Upgrades

*Evidence-based upgrades from a 40-year cross-framework stress test vs Buffett · Munger · Lynch · Fisher · Marks. See [investor-philosophy-alignment.md](investor-philosophy-alignment.md) for a high-level summary of each investor's core tenets and the alignment checklist used to keep these upgrades from drifting away from the philosophies they're built on.*

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

**Structural Quality Override (added 2026-06-07 — see [investor-philosophy-alignment.md](investor-philosophy-alignment.md)):** Before applying the **+1 "expensive"** adjustment, check whether the multiple expansion is accompanied by a genuine *structural* improvement — margin expansion, ROIC improvement, or qualifying growth-CapEx reinvestment per Upgrade 1. If yes, do not apply the penalty: a higher multiple may simply reflect a better business, not euphoria. This is Howard Marks' "second-level thinking" (a historical average is only a useful anchor if the business hasn't structurally changed) — and it closes a quiet contradiction with Upgrade 1, which already concedes that raw multiples *understate* quality for moat-building reinvestment. Without this override, Upgrade 2 would mechanically penalize the very reinvestment Upgrade 1 credits.

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

### ⚪ Upgrade 6 — *(Retired 2026-06-07)* ~~Momentum Filter: Entry Confirmation~~

Retired — see [decisions/2026-06-07-framework-fixes-investor-philosophy-alignment.md](../decisions/2026-06-07-framework-fixes-investor-philosophy-alignment.md) and [investor-philosophy-alignment.md](investor-philosophy-alignment.md). The original rule gated new-position entries on whether price sat above or below the 200-day moving average — a price-action/technical signal that (a) directly contradicted this framework's own non-negotiable Rule 0, *"act only on documented triggers — a valuation-score change or a fundamental event, never on price movement alone"* ([CLAUDE.md](../CLAUDE.md)), and (b) sits squarely against Buffett/Munger/Graham's lifelong, explicit rejection of chart-based decision triggers ("technical analysis is a bunch of nonsense" — Munger).

Its protective intent — don't buy into a deteriorating situation — is already served by Phase 04's Quality Watch, Narrative Check, and Short Thesis Engagement, all of which are fundamentals-based. No replacement rule was added; the heading and number are kept (rather than renumbered) so existing references to Upgrade 7 (and any future ones) stay stable.

### 🔵 Upgrade 7 — Hard Position Cap at 15%

Hard cap: never exceed 15% in a single position under any circumstances. (Note: Verdad research empirically validated 8% across 10,000 simulated portfolios; 15% is a deliberate user override of that backing — see [decisions/2026-06-07-framework-change-position-cap.md](../decisions/2026-06-07-framework-change-position-cap.md) for the rationale.)

---

## Updated Valuation Score Weighting

| Input | Weight | Notes |
|-------|--------|-------|
| FCF Yield (Owner Earnings adjusted) | 40% | Primary signal |
| EV/EBIT (<15× cheap · >30× expensive) | 40% | Always 40% — no separate PEG "slot" to redistribute from |
| Forward PE + Historical PE Modifier | 20% | Adds mean-reversion signal |
| PEG Modifier (Fast Growers only) | Additive (−1…+1) | Lynch filter — small bolt-on adjustment, same form/placement as the Historical PE Modifier and Rate Regime Modifier; not a weighted 1–10 sub-score (corrected 2026-06-08, see [decisions/2026-06-08-framework-fix-peg-weighting-inconsistency.md](../decisions/2026-06-08-framework-fix-peg-weighting-inconsistency.md)) |
| Rate Regime Modifier (post-score) | Additive | −1 / 0 / +0.5 / +1 based on 10Y Treasury |

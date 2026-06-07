# 📈 Quality Value + Dynamic Trimming — Investment Strategy

> ud83dudd17 **Quick Navigation**
> 

> • [🤖 Claude Operating Brief — System Prompt](%F0%9F%93%88%20Quality%20Value%20+%20Dynamic%20Trimming%20%E2%80%94%20Investment%20St/%F0%9F%A4%96%20Claude%20Operating%20Brief%20%E2%80%94%20System%20Prompt%2036d165d9fe04810abc24e303d3f16228.md) — Paste this at the start of every Claude session
> 

> • [📅 Routine Operating Calendar](%F0%9F%93%88%20Quality%20Value%20+%20Dynamic%20Trimming%20%E2%80%94%20Investment%20St/%F0%9F%93%85%20Routine%20Operating%20Calendar%20%E2%80%94%20When%20&%20How%20to%20Run%20t%2036d165d9fe0481108506df82c632d4f2.md) — When to run each task, what data to prepare, input templates
> 

---

# Strategy Overview

Buy profitable, high-margin, high-growth companies when cheap. Trim dynamically as valuation expands using the same metrics that identified the entry. Exit only on fundamental breakdown or extreme overvaluation.

> **Core Insight:** If you can define cheap, you can define expensive. The same valuation methodology drives both entry sizing and trim triggers.
> 

---

# The 6-Phase Framework

## Phase 01 — Universe Screening

Filter the investable universe to only high-quality businesses.

- **Profitability:** Net margin >15%, ROIC >15%, positive FCF for 3+ years
- **High Margins:** Gross margin >40% OR structurally expanding margins (3yr trend)
- **Growth Perspective:** Revenue CAGR >10%, TAM expansion, pricing power evident
- **Balance Sheet:** Net debt/EBITDA <2x, no dilutive share issuance pattern. ⚠️ *Conglomerate rule: if a captive financial subsidiary exists, consolidate its debt into the ratio — parent-only figures are insufficient.*
- **Moat Signal:** Market share stable/growing, brand, network effect, switching costs
- **FCF Quality Check:** FCF/Net Income conversion ratio >70% for 2+ consecutive years. If below 70% without a clear growth capex explanation, flag and do not proceed to Phase 02 scoring.

**Output:** Qualified Quality List — ~50–150 companies

---

## 🌡️ Rate Environment Gate — Run Before Every Score

> **Mandatory pre-check applied before Phase 02 scoring.** Anchors valuations to the current risk-free rate. Prevents the framework from treating “cheap vs. its own history” as cheap in absolute terms when the rate regime has shifted.
> 

**Step 1 — Earnings Yield Spread Test (per company)**

Before computing a valuation score, calculate:

- Earnings Yield (EY) = 1 ÷ Forward PE
- Spread = EY − 10Y US Treasury Yield
- **Pass threshold: Spread ≥ +1.5%**

If Spread < +1.5%: the equity does not offer adequate return over the risk-free rate. Do not open a new position. For existing holdings, re-score and apply trim protocol if score has risen.

**Step 2 — Rate Regime Modifier (updated each quarter, applied globally)**

After computing a raw valuation score, apply this modifier based on the current 10Y Treasury yield:

| 10Y Treasury Yield | Modifier | Rationale |
| --- | --- | --- |
| < 2% | −1 to all scores | Easy money; valuations can stretch further |
| 2–3.5% | No change | Neutral / historical norm |
| 3.5–5% | +0.5 to all scores | Capital has real cost; discount rates elevated |
| > 5% | +1 to all scores | Strong competition from risk-free rate |

Record the active modifier in each quarterly screening update. All entry, trim, and exit decisions use the modifier-adjusted final score.

**Step 3 — Rate-Normalised Historical PE (annual task, top 5 holdings only)**

The Historical PE Modifier in Upgrade 2 uses a 5–10yr average built partly in near-zero rate conditions (2012–2022). Once per year, recalculate each top-5 holding’s “rate-normalised PE average” using only periods where the 10Y was within ±1% of today’s yield. If this normalised average is materially lower than the raw average, apply +0.5 to that company’s score for the year.

---

## Phase 02 — Valuation Scoring

Assign a valuation score (1–10) to each qualified company. This score is the core engine of all decisions.

- **FCF Yield** — FCF / Market Cap. >5% = attractive, >8% = compelling
- **EV/EBIT** — <15x = cheap for quality, >30x = expensive
- **PEG Ratio** — P/E ÷ Growth rate. <1.0 = undervalued relative to growth
- **P/S vs. Margin** — For high-growth: P/S <(gross margin % × 0.5) = reasonable
- **Historical Percentile** — Where is current valuation vs. own 5yr history? <25th pct = cheap

## 🧮 Scoring Calculation Formula

Final Score = (FCF_sub × 0.40) + (EV/EBIT_sub × 0.25) + (FwdPE_adj_sub × 0.20) + (PEG_sub × 0.15) + Rate Regime Modifier

> If PEG is not applicable (non-Fast Grower), redistribute its 15% weight to EV/EBIT (making EV/EBIT weight 40%) and drop PEG sub-score.
> 

> Score boundary rule: if result falls on exactly X.5, round UP (more conservative). Minimum 1, maximum 10.
> 

**FCF Yield sub-score table:**

| FCF Yield | Sub-score |
| --- | --- |
| >8% | 1 |
| 6–8% | 2–3 |
| 4–6% | 4–5 |
| 2–4% | 6–7 |
| <2% | 8–10 |

**EV/EBIT sub-score table:**

| EV/EBIT | Sub-score |
| --- | --- |
| <12× | 1–2 |
| 12–18× | 3–4 |
| 18–22× | 5 |
| 22–28× | 6–7 |
| 28–35× | 8–9 |
| >35× | 10 |

**Forward PE sub-score:** Score 1–10 relative to sector historical norms, then apply Upgrade 2 Historical PE Modifier (−1 / 0 / +1).

**PEG sub-score (Fast Growers with EPS growth >15% only):**

| PEG | Sub-score modifier |
| --- | --- |
| <0.8 | −1 to raw score |
| 0.8–1.2 | 0 |
| 1.2–1.8 | +0.5 |
| >2.0 | +1 |

**Output:** Valuation Score 1–10 per company (1 = extremely cheap, 10 = extremely expensive)

## Phase 03 — Entry & Position Sizing

Position size is a direct function of valuation score — cheaper = larger bet.

| Score | Label | Position Size |
| --- | --- | --- |
| 1–3 | Very Cheap | Full position — 6–8% of portfolio |
| 4–5 | Cheap | Standard position — 3–5% of portfolio |
| 6–7 | Fair Value | Watchlist only — no new entry |
| 8–10 | Expensive | Do not buy. Begin trim protocol if held. |

**Rule:** Max 10–15 names. High conviction over diversification.

## Phase 04 — Continuous Monitoring

Track both fundamental quality AND valuation score — both can trigger action.

- **Quarterly review:** Re-score valuation after each earnings report
- **Quality watch:** Flag if margins compress >3pp, ROIC drops below threshold, debt rises
- **Narrative check:** Is the growth thesis (TAM, moat, pricing power) still intact?
- **Sector rotation signal:** Is money fleeing the sector for macro reasons? (opportunity, not threat)
- **Relative cheapness:** Better opportunity elsewhere? Compare scores across qualified list
- **FCF quality monitor:** If FCF/Net Income conversion drops below 70% for 2 consecutive quarters without capex explanation, flag for immediate thesis review. Do not add to position until resolved. *(Valeant + Wirecard signal)*
- **Organic revenue check:** If the company has made acquisitions in the past 12 months, recalculate organic revenue CAGR separately. Declining organic growth masked by M&A is a quality deterioration signal, not growth.
- **Short thesis engagement:** If a credible short thesis exists (major short fund, investigative journalism, regulatory filing), engage with the specific argument independently before maintaining or adding to the position. Disagreeing with a short thesis without documented rebuttal is not due diligence. *(Wirecard signal)*
- **Earnings quality check:** If EPS growth exceeds revenue growth by >10pp for 2+ consecutive years, recalculate EPS on a flat share count basis. Verify that operational performance is not being masked by buybacks. *(IBM signal)*

**Output:** Live score dashboard. Action triggered only by score changes, not price noise.

## Phase 05 — Dynamic Trimming (Valuation-Driven)

If we can define cheap, we can define expensive. Trim as valuation expands — not by price target.

- **Score reaches 6–7:** Trim 25–30% of position. Recycle into Score 1–3 names.
- **Score reaches 8:** Trim to half-position (50% of original size)
- **Score reaches 9–10:** Trim to tracking position — 1–2%. Keep skin in the game.
- **2x price milestone:** Trigger valuation re-score. If score also 7+, accelerate trim.
- **Capital recycling:** Proceeds always reinvested into current Score 1–3 names only.

**Output:** Portfolio continuously rebalanced toward highest value/quality ratio

## Phase 06 — Full Exit Triggers

Two and only two reasons to sell completely — valuation extreme OR fundamental break.

- ✅ Fundamental deterioration — margins structurally broken, ROIC falls below cost of capital
- ✅ Growth thesis broken — TAM shrinking, disruption visible, pricing power lost
- ✅ Extreme overvaluation — Score 10 sustained for 2+ quarters
- ✅ Balance sheet crisis — leverage spikes, dilutive capital raise
- ❌ **NOT a valid exit reason:** Price dropped (if quality intact = buy more). Macro fear. Short-term miss.

---

# The Valuation Score — Core Decision Engine

One unified score drives all decisions. The same methodology that identifies cheap also identifies expensive.

| Score Range | Status | Action |
| --- | --- | --- |
| 1–3 | Very Cheap | Full position (6–8%) |
| 4–5 | Cheap | Standard position (3–5%) |
| 6–7 | Fair / Rich | Trim 25–30% |
| 8–10 | Expensive | Trim to tracking or full exit |

---

# Core Principles

1. **Valuation is Symmetric** — The same metrics that tell you something is cheap tell you when it's expensive. Use them both ways.
2. **Trim ≠ Sell** — Dynamic trimming keeps exposure to great compounders while locking in margin of safety gains.
3. **Quality is the Filter, Value is the Trigger** — Never buy cheap junk. Never overpay for quality. Both conditions must be met.
4. **Capital Recycling is the Engine** — Trim proceeds always flow to the cheapest high-quality names. The portfolio self-optimizes.
5. **Conviction Over Diversification** — 10–15 deeply understood positions outperform 50 positions held on weak thesis.
6. **Price is Not the Thesis** — A falling price on an intact business is an opportunity. A broken thesis at any price is an exit.

---

# Screening Workflow

## Tools

- **TIKR** — 100k+ global stocks, 335+ metrics, best for EV/EBIT, ROIC, FCF yield
- **Koyfin** — 10+ years historical financials, consistency analysis
- **Finviz** — Fast US market pre-filter, 60+ fundamental filters
- **Gurufocus** — Quality/value combo screens, Magic Formula, Buffett-style filters

## Quantitative Pre-Screen Filters

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

## Parallel Idea Generation

- Earnings call transcripts — listen for margin/pricing power language
- 13F filings — what are Fundsmith, Akre, Constellation, Baillie Gifford adding?
- Spin-offs & demergers — structurally undervalued, temporarily ignored
- Sector rotation moments — whole sectors sold off on macro fear = hunting window
- Insider buying — corroborating signal ([OpenInsider.com](http://OpenInsider.com))

## 5 Qualitative Questions Before Scoring

1. Why are margins high? Pricing power, scale, or lucky cycle?
2. What would it take to compete with them? (Hard = moat)
3. How has management allocated capital over 5–10 years?
4. Where is growth coming from next 3–5 years?
5. What is the best bear case against owning it?
6. Could a new delivery mechanism, platform, or technology make this moat irrelevant within 5 years? *(Disruption vector check — added from Nokia/Kodak graveyard cases)*

---

# May 2026 Screening Results

| Ticker | Name | Valuation Score | Quality Score | Signal | Key Note |
| --- | --- | --- | --- | --- | --- |
| CSCO | Cisco Systems | 3 | 7 | ✅ BUY ZONE | FCF yield 6.2%, 35% below 5yr avg PE |
| SPGI | S&P Global | 3 | 7 | ✅ BUY ZONE | 29% below 5yr avg PE, ROIC below threshold |
| V | Visa | 4 | 9 | ✅ BUY ZONE | All quality boxes checked, fwd PE 22x |
| META | Meta Platforms | 4 | 9 | ✅ BUY ZONE | ROIC 28%, EV/EBITDA 16x, AI monetization |
| MA | Mastercard | 5 | 10 | 🟡 WATCHLIST | Elite quality, wait for fwd PE <25x |
| GOOGL | Alphabet | 6 | 9 | 🟡 WATCHLIST | Good quality, FCF distorted by AI capex |
| NVO | Novo Nordisk | 2 ⚠️ | 6 | ⚠️ THESIS RISK | Cheapest valuation but ROIC -41% YoY |
| ASML | ASML Holding | 8 | 10 | 🔴 AVOID | Extraordinary biz, fwd PE 37x too rich |

> **NVO Note:** Valuation score 2 (extremely cheap) but quality score declining. ROIC down 41% YoY, revenue growth slowing 31% → 6%. Verify thesis before any entry.
> 

---

# The Strategy Loop

**SCREEN → SCORE → ENTER → MONITOR → TRIM → RECYCLE → SCREEN**

The screener never stops running. Every earnings season re-score all holdings and watchlist names. Trim proceeds flow immediately to the highest-scoring (cheapest) qualified names. The portfolio self-optimizes continuously.

---

*Strategy developed: May 2026*

[🔬 Hybrid Framework Upgrades — 40-Year Stress Test (May 2026)](%F0%9F%93%88%20Quality%20Value%20+%20Dynamic%20Trimming%20%E2%80%94%20Investment%20St/%F0%9F%94%AC%20Hybrid%20Framework%20Upgrades%20%E2%80%94%2040-Year%20Stress%20Test%20%2036a165d9fe0481da906ef3b35ba1a79e.md)

---

# 🔬 Hybrid Upgrades — 40-Year Stress Test (May 2026)

> 7 evidence-based upgrades from cross-framework stress test vs Buffett · Munger · Lynch · Fisher · Marks. Core Quality Gate and Dynamic Trimming logic preserved unchanged.
> 

## 🔴 Upgrade 1 — Owner Earnings Adjustment (CRITICAL)

Raw FCF yield penalises moat-building CapEx businesses (cloud, AI infra, platforms). For businesses where **Growth CapEx > 30% of total CapEx**, replace reported FCF with:

> Owner Earnings = Net Income + D&A − Maintenance CapEx only
> 

Apply Owner Earnings figure to FCF Yield scoring. Flag adjustment in analysis notes.

Affected businesses: MSFT (Azure), Alphabet, Meta, Amazon.

Scoring impact:

- MSFT: 2.3% FCF yield → ~4.0% Owner Earnings yield → Score 6 → **Score 5**
- META: 3.1% → ~3.8% → partial improvement toward Score 4

## 🔴 Upgrade 2 — Historical PE Relative Modifier (CRITICAL)

Add modifier to valuation score after quality gate passes:

| Forward PE vs 10yr Avg | Adjustment |
| --- | --- |
| > 20% below average | −1 |
| Within ±10% | No change |
| > 20% above average | +1 |

May 2026: MSFT 24.9× vs 31× avg (−20%) → Score −1. AAPL 37× vs 24.5× avg (+51%) → Score +1.

## 🟠 Upgrade 3 — PEG Ratio for Fast Growers (HIGH)

Apply ONLY to Lynch Fast Grower category (EPS growth > 15% for 3+ years). ⚠️ Never apply to cyclicals or stalwarts.

| PEG | Modifier |
| --- | --- |
| < 0.8 | −1 |
| 0.8–1.2 | No change |
| 1.2–1.8 | +0.5 |
| > 2.0 | +1 |

May 2026: META PEG 0.90 → Score −1 → Full position 6–8%.

## 🟠 Upgrade 4 — Turnaround Sub-Gate / Fallen Angel Path (HIGH)

Businesses failing 2–4 quality criteria may enter as **Conditional Watch (2–3% max)** if ALL five conditions met:

1. ROIC historically > 15% for ≥ 5 years in past decade
2. CEO/CFO insider buying > $500K in past 6 months (Form 4 verified)
3. Independent FV estimate showing ≥ 40% MOS
4. Net Debt/EBITDA < 3×
5. Core moat still identifiable

Mandatory 2-quarter review. Full position only after quality gate fully re-passes.

May 2026 — NKE: qualifies on all 5 → **Conditional Watch 2–3%**. Exit if gross margin < 43% by Q2 FY2027.

## 🟡 Upgrade 5 — Debt Gate Context Adjustment (MEDIUM)

For payment networks, exchanges, asset-light businesses where 100% of debt is financial (not operational): threshold → **Net Debt/EBITDA < 4×**, provided interest coverage > 15× and investment grade rated. Standard 2.5× unchanged for all other business models.

May 2026: MA 2.5× → borderline FAIL → **clean PASS**.

## 🟡 Upgrade 6 — Momentum Filter: Entry Confirmation (MEDIUM)

Soft modifier — does not override quality gate.

- Above 200-day MA → proceed with scored entry
- Below 200-day MA → require one of: earnings beat > 5%, new insider buy > $250K, or analyst upgrade with > 30% target upside

May 2026: V below 200MA → await $275–285 AND one trigger. NKE below 200MA → turnaround triggers already apply.

## 🔵 Upgrade 7 — Position Cap Validated at 8% (HIGH)

This framework's 6–8% single-position cap is empirically correct. Verdad research (10,000 simulated portfolios): hyper-concentrated 5–10 stock portfolios trail diversified quality portfolios by 1–2%/yr due to volatility drag. Do not increase beyond 8% under any circumstances.

---

## Updated Valuation Score Weighting

| Input | Weight | Notes |
| --- | --- | --- |
| FCF Yield (Owner Earnings adjusted) | 40% | Primary signal — unchanged |
| EV/EBIT (<15× cheap · >30× expensive) | 25% | Unchanged |
| Forward PE + Historical PE Modifier | 20% | New: adds mean-reversion signal |
| PEG Modifier (Fast Growers only) | 15% | New: Lynch filter |
| Rate Regime Modifier (global, post-score) | Additive | New: −1 / 0 / +0.5 / +1 based on 10Y Treasury. Applied after raw score is calculated. Updated quarterly. |

Position sizing bands unchanged: Score 1–3 → 6–8%, Score 4–5 → 3–5%, Score 6–7 → Trim 25–30%, Score 8–10 → Exit.

---

## Updated Verdicts — May 2026

| Ticker | Old Verdict | New Hybrid Verdict | Driver |
| --- | --- | --- | --- |
| META | BUY 3–5% (Score 5) | **BUY 6–8%** (Score 3–4) | PEG 0.90 + Hist PE discount |
| MSFT | HOLD/TRIM (Score 7) | **BUY 6–8%** (Score 5) | Owner Earnings + Hist PE −20% |
| MA | HOLD/TRIM (Score 6) | **HOLD + Add $480–500** | Debt context → clean pass |
| V | No Add (Score 6) | **WAIT $275–285 + 200MA** | Convergent entry signal |
| NKE | REJECT | **Conditional Watch 2–3%** | Turnaround sub-gate qualifies |

---

## 40-Year Stress Test Results

| Period | Master | Notion QV | Hybrid | S&P 500 | Winner |
| --- | --- | --- | --- | --- | --- |
| 1985–1990 | +29.1% | +16.8% | +24.2% | +13.2% | Master |
| 1991–2000 | +26.4% | +21.3% | +25.8% | +18.1% | Master |
| 2000–2010 | +8.9% | +11.2% | +12.4% | −1.0% | Notion QV |
| 2010–2020 | +13.9% | +12.1% | +15.8% | +13.7% | Neither |
| 2020–2026 | +15.1% | +13.8% | +17.9% | +14.2% | Master |
| **Avg/yr** | **+18.7%** | **+15.0%** | **+19.2%** | **+11.6%** | **Hybrid** |

Both frameworks missed intangible-moat tech in 2010–2020 (Amazon, Netflix, early Google). Notion QV won the critical capital-preservation decade (2000–2010) via FCF yield and dynamic trimming. Hybrid closes both gaps.

*Updated: May 24, 2026 · Source: 40-year stress test vs Master Investor Framework (Buffett · Munger · Lynch · Fisher · Marks)*

[📐 Professional Fair Value Determination — 10-Rule Framework](%F0%9F%93%88%20Quality%20Value%20+%20Dynamic%20Trimming%20%E2%80%94%20Investment%20St/%F0%9F%93%90%20Professional%20Fair%20Value%20Determination%20%E2%80%94%2010-Rule%20%20362165d9fe0481fc9debf771b94c8b42.md)

[💰 Buy & Sell Price Methodology — Order Setup Rules](%F0%9F%93%88%20Quality%20Value%20+%20Dynamic%20Trimming%20%E2%80%94%20Investment%20St/%F0%9F%92%B0%20Buy%20&%20Sell%20Price%20Methodology%20%E2%80%94%20Order%20Setup%20Rules%2036c165d9fe0481a79320cf0000c92985.md)

[🪦 Framework Validation — Graveyard Audit](%F0%9F%93%88%20Quality%20Value%20+%20Dynamic%20Trimming%20%E2%80%94%20Investment%20St/%F0%9F%AA%A6%20Framework%20Validation%20%E2%80%94%20Graveyard%20Audit%2036d165d9fe0481ed94e1cc09ddace73c.md)

[📊 Benchmark Comparison — MSCI Quality Index](%F0%9F%93%88%20Quality%20Value%20+%20Dynamic%20Trimming%20%E2%80%94%20Investment%20St/%F0%9F%93%8A%20Benchmark%20Comparison%20%E2%80%94%20MSCI%20Quality%20Index%2036d165d9fe0481e4bc43d847155c3347.md)

[📋 Human Override Log](%F0%9F%93%88%20Quality%20Value%20+%20Dynamic%20Trimming%20%E2%80%94%20Investment%20St/%F0%9F%93%8B%20Human%20Override%20Log%2036d165d9fe0481c2872fcf6cad8833f0.md)

[🤖 Claude Operating Brief — System Prompt](%F0%9F%93%88%20Quality%20Value%20+%20Dynamic%20Trimming%20%E2%80%94%20Investment%20St/%F0%9F%A4%96%20Claude%20Operating%20Brief%20%E2%80%94%20System%20Prompt%2036d165d9fe04810abc24e303d3f16228.md)

[📅 Routine Operating Calendar — When & How to Run the Framework](%F0%9F%93%88%20Quality%20Value%20+%20Dynamic%20Trimming%20%E2%80%94%20Investment%20St/%F0%9F%93%85%20Routine%20Operating%20Calendar%20%E2%80%94%20When%20&%20How%20to%20Run%20t%2036d165d9fe0481108506df82c632d4f2.md)
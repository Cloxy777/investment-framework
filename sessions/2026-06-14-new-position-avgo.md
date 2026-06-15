# NEW POSITION — AVGO (Broadcom Inc.) — 2026-06-14

**Task type:** NEW POSITION
**Date:** 14 Jun 2026
**10Y US Treasury Yield:** 4.49% (CNBC/TradingEconomics, market close Fri 12 Jun 2026 — most recent available; markets closed Sun 14 Jun)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current AVGO portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md))
**Sector:** Semiconductors (fabless, AI infrastructure — custom AI accelerators/ASICs, networking) + Infrastructure Software (VMware)

> **Note on stale placeholder:** `holdings.md` carries an old comment claiming "AVGO and CSCO no longer appear in either broker account" from a superseded placeholder list. No prior AVGO session or decision exists anywhere in this repo's history — that comment is **not** backed by any actual prior position. This session treats AVGO as a fresh, first-time evaluation.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$382.07** | WebSearch: "AVGO closed at $382.07 on June 12, 2026" (stockanalysis.com / aggregator history). IBKR `get_price_snapshot` / `search_contracts` MCP tools were denied permission in this session — WebSearch is the available Rule-0 source and is internally consistent (see 52-week range below). |
| 52-week range | $241.11 – $495.00 | WebSearch (aggregator) |
| Analyst consensus PT | ~$501–522 cluster (S&P Global 48-analyst avg $522.06; another 45-analyst avg $517.61, range $215.88–$650); consensus rating "Strong Buy" (44 buy / 0 sell / 4 hold of 45) | WebSearch (S&P Global / aggregator) |

**Context:** $382.07 sits roughly **23% below the 52-week high** ($495.00) and **~58% above the 52-week low** ($241.11) — mid-to-upper part of the 52-week range, well below the analyst consensus PT cluster (~$501–522, i.e. ~31–37% upside implied by consensus).

⚠️ **Tooling flag:** The IBKR `get_price_snapshot` and `search_contracts` MCP tools (used for Rule 0 in prior sessions, e.g. PYPL same-day) returned "Permission denied" in this session. Price was cross-checked via two independent WebSearch queries returning the same figure ($382.07, 12 Jun 2026 close) with an internally-consistent 52-week range, so I'm treating it as reliable — but flagging the tooling gap explicitly per "never invent or estimate."

---

## 2. Data Gathered (Phase 01 & 02 Inputs) & Gaps Flagged

### Revenue / Earnings history (fiscal year ends ~late Oct/early Nov)

| Fiscal Year | Revenue | YoY | GAAP Net Income | GAAP Diluted EPS (post-split) |
|---|---|---|---|---|
| FY2022 | $33,203M | +21% | — | — |
| FY2023 | $35,819M | +7.9% | $14,082M | — |
| FY2024 | $51,574M | +44.0% | $5,895M | $1.23 |
| FY2025 | $63,887M | +23.9% | $23,126M (sum of quarters: 5,503+4,965+4,140+8,518) | $1.95 (Q4 alone) — full-year diluted EPS not independently located; derivable as NI/shares ≈ $4.74 |

Source: Broadcom 8-K quarterly/annual earnings releases (SEC EDGAR), cross-checked against prnewswire/investor relations releases.

### TTM (Q3 FY2025 – Q2 FY2026, i.e. trailing 4 quarters as of latest reported quarter ended 3 May 2026)

| Metric | Value | Derivation |
|---|---|---|
| TTM Revenue | $75,470M | stockanalysis.com TTM figure (32.3% YoY growth cited) |
| TTM GAAP Net Income | $29,317M = FY2025 NI ($23,126M) − Q1 FY25 ($5,503M) − Q2 FY25 ($4,965M) + Q1 FY26 ($7,349M) + Q2 FY26 ($9,310M) | Computed rollforward from quarterly 8-Ks |
| TTM GAAP Operating Income (EBIT) | $30,443M = Q3 FY25 ($7,508M) + Q4 FY25 ($5,887M) + Q1 FY26 ($6,260M) + Q2 FY26 ($10,788M) | Computed rollforward from quarterly 8-Ks |

⚠️ **Flag:** stockanalysis.com separately reported a "TTM EPS of $5.29" which, at ~4,876M diluted shares, implies TTM NI ≈ $25.79B — about $3.5B below my $29.32B rollforward. This discrepancy likely reflects stockanalysis.com's TTM window being computed before the Q2 FY2026 release (3 Jun 2026) was incorporated, or a different non-GAAP adjustment basis. I used the **rollforward from primary-source quarterly 8-K GAAP figures** ($29,317M) as the more directly traceable number, and flag both for the record.

### Gross Margin trend (GAAP)

| FY | Gross Profit | Revenue | Gross Margin % |
|---|---|---|---|
| FY2023 | $24,690M | $35,819M | 68.9% |
| FY2024 | $32,509M | $51,574M | 63.0% |
| FY2025 | $43,294M | $63,887M | 67.8% |

Source: Broadcom 8-K annual results (GAAP gross margin reported directly as "% of net revenue" in FY2025 release: 68% vs 63% prior year, matching the computed figures above).

### Balance sheet / leverage (as of most recent 10-Q, period ended 3 May 2026)

| Metric | Value | Source |
|---|---|---|
| Cash & cash equivalents | $19,628M | AVGO 10-Q (Q2 FY2026) |
| Short-term debt | $2,252M | AVGO 10-Q (Q2 FY2026) |
| Long-term debt | $62,655M | AVGO 10-Q (Q2 FY2026) |
| Total debt | $64,907M | Computed |
| **Net debt** | **$45,279M** | Computed: $64,907M − $19,628M |
| Adjusted EBITDA (FY2025, non-GAAP) | $43,000M (+35% YoY) | Broadcom FY2025 earnings release |
| **Net Debt / EBITDA** | **≈1.05×** | $45,279M ÷ $43,000M |

⚠️ Adjusted EBITDA is non-GAAP. Net Debt/EBITDA on this basis is ~1.05×, comfortably under both the strategy.md <2× and pre-screen <2.5× thresholds (Upgrade 5's <4× asset-light test isn't even needed here).

### Free Cash Flow / FCF-NI conversion

| FY | Operating Cash Flow | CapEx | FCF | FCF % of revenue | Net Income | FCF/NI |
|---|---|---|---|---|---|---|
| FY2023 | — | — | ~$17.6B (49% of $35.8B rev, per earnings release) | 49% | $14,082M | 125% |
| FY2024 | $19,962M | $548M | $19,414M | 37.6% | $5,895M | **329%** |
| FY2025 | (Q1 $6,113 + Q2 $6,555 + Q3 $7,166 + Q4 $7,703 = $27,537M) | (Q1 $100 + Q2 $144 + Q3 $142 + Q4 $237 = $623M) | $26,914M (≈$26.9B as reported) | 42.1% | $23,126M | **116%** |

FCF/NI conversion is **well above 70%** for both of the last two fiscal years (329% and 116%) — the FY2024 figure is extreme because GAAP net income that year was severely depressed by VMware acquisition-related charges (see "GAAP distortion" note below), while operating cash flow was largely unaffected (non-cash add-backs).

### Capital expenditure composition (Upgrade 1 / Owner Earnings check)

Total CapEx is tiny relative to revenue: **$623M in FY2025 (~1% of $63.9B revenue)**. No public breakdown of "growth capex vs. maintenance capex" is disclosed — Broadcom is a **fabless** semiconductor company (manufacturing outsourced to TSMC and other foundries), so it does not build its own fabs; its AI-driven growth investment flows primarily through **R&D operating expense** (already reflected in GAAP/cash earnings) and **M&A** (VMware), not capex.

**Determination: Upgrade 1 (Owner Earnings) does NOT apply.** This is not because growth capex is provably <30% of a number I can't break down — it's because **total capex is immaterial** (~1% of revenue), so raw FCF is not meaningfully understated by capex treatment in the way Upgrade 1 was designed to correct for MSFT/GOOGL/META/AMZN (where capex runs 10-15%+ of revenue on AI data-center buildouts). Using raw FCF for the FCF Yield sub-score is appropriate here.

### GAAP earnings distortion — VMware purchase-accounting amortization (flagged for Rule 6 "normalize before you value")

FY2025 amortization of VMware-acquisition-related intangible assets: **$6,031M** (in cost of revenue) + **$3,244M** (in G&A) ≈ **$9.3B/year**, non-cash. This is the primary driver of the gap between:
- GAAP operating income (EBIT) FY2025: $25,484M (margin 39.9%)
- Non-GAAP / Adjusted EBITDA FY2025: $43,000M (margin 67.3%)

This distortion is material to the **EV/EBIT** sub-score below — flagged explicitly rather than silently adjusted, since substituting a "normalized EBIT" figure would require estimating an add-back not directly computable from the inputs gathered (the framework's prescribed EV/EBIT formula uses reported/GAAP EBIT). See §5 for how this plays out in the score.

### EV/EBIT inputs

| Input | Value | Source/Derivation |
|---|---|---|
| Diluted weighted-avg shares (Q2 FY2026) | 4,876M | AVGO 10-Q (Q2 FY2026) |
| Market Cap | $382.07 × 4,876M ≈ **$1,862,973M ($1,863.0B)** | Computed |
| Net debt | $45,279M | Computed above |
| **Enterprise Value** | **≈ $1,908,252M ($1,908.3B)** | Market Cap + Net Debt |
| GAAP EBIT, TTM | $30,443M | Computed above |
| GAAP EBIT, FY2025 | $25,484M | Broadcom FY2025 earnings release |
| **EV/EBIT (TTM)** | **≈62.7×** | $1,908.3B ÷ $30.443B |
| **EV/EBIT (FY2025)** | **≈74.9×** | $1,908.3B ÷ $25.484B |

### Forward PE / 10yr Avg PE / ROIC / PEG

| Metric | Value | Source |
|---|---|---|
| Forward PE | 24.50× | stockanalysis.com |
| Trailing PE | 64.20–93.60× (varies by date/source) | stockanalysis.com / fullratio.com |
| **10yr Avg PE** | **68.51×** (15yr avg 65.80×, 5yr avg 69.31×, 3yr avg 78.28×) | macrotrends / fullratio (only an *average*, not a low/high range — fallback formula applies) |
| ROIC | 24.22% | stockanalysis.com |
| ROE | 37.28% | stockanalysis.com |
| PEG (reported) | 0.53 | stockanalysis.com |

### Non-GAAP diluted EPS history (for Fast Grower / PEG cross-check) — post-split-equivalent ($), computed from quarterly 8-K figures

| FY | Non-GAAP diluted EPS (sum of quarters, pre-split years ÷10) | YoY growth |
|---|---|---|
| FY2022 | (8.39+9.07+9.73+10.45)/10 = $3.764 | — |
| FY2023 | (10.33+10.32+10.54+11.06)/10 = $4.225 | +12.2% |
| FY2024 | (10.99+10.96)/10 + 1.24 + 1.42 = $4.855 | +14.9% |
| FY2025 | 1.60+1.58+1.69+1.95 = $6.82 | +40.5% |

3yr CAGR (FY2022→FY2025): (6.82/3.764)^(1/3) − 1 = **+21.9%**

### Share issuance pattern

VMware acquisition (completed Nov 2023) was funded ~$30.8B cash + **54.4M pre-split shares** (= 544M post-split shares, ≈11% increase to share count at the time) — a **one-time, M&A-related issuance**, not an ongoing dilutive pattern. Post-acquisition, Broadcom has been **actively buying back stock** (new $10B repurchase program announced with Q1 FY2026 results, Feb 2026) and paying down VMware-deal debt. **Not classified as dilutive.**

### Data Gaps / Flags Summary

1. IBKR price-snapshot/contract-search MCP tools denied — used WebSearch as Rule-0 source (internally consistent across two queries + 52-week range sanity check).
2. TTM net income has a ~$3.5B discrepancy between two derivation methods (rollforward $29.32B vs. EPS-implied $25.79B) — used the rollforward from primary-source quarterly figures, flagged the alternate.
3. GAAP EBIT is severely depressed (~35-40%) by ~$9.3B/yr of non-cash VMware-related intangible amortization — this is **not** adjusted out of the EV/EBIT calculation below (the framework's formula uses reported EBIT), but is flagged as a major driver of the EV/EBIT sub-score result.
4. Fast Grower classification is borderline — see §5 PEG discussion.
5. No metric was invented or estimated; all figures trace to Broadcom 8-K/10-Q/10-K filings (SEC EDGAR) or named aggregators (stockanalysis.com, macrotrends, fullratio), with derivations shown explicitly.

---

## 3. Phase 01 — Quality Gate

| Check | AVGO Value | Threshold | Result |
|---|---|---|---|
| Net margin | FY2025 36.2% ($23,126M/$63,887M); TTM 38.9% ($29,317M/$75,470M) | >15% (strategy.md) / >12% (pre-screen) | ✅ PASS — clears by >2x |
| ROIC | 24.22% | >15% | ✅ PASS |
| Revenue CAGR 3yr (FY2022→FY2025) | **24.38%** = (63,887/33,203)^(1/3) − 1 | >10% (strategy.md) / >8% (pre-screen) | ✅ PASS — clears by >2x |
| Gross margin | FY2025 67.8% (FY2023 68.9% → FY2024 63.0% → FY2025 67.8%) | >40% or structurally expanding | ✅ PASS — well above 40%, and rebounding from the FY2024 VMware-integration dip |
| FCF positive 3 consecutive years | FY2023 ~$17.6B / FY2024 $19.4B / FY2025 $26.9B — all positive and growing | required | ✅ PASS |
| Net debt/EBITDA | ≈1.05× ($45,279M / $43,000M adj. EBITDA) | <2× (strategy.md) / <2.5× (pre-screen) | ✅ PASS |
| FCF/NI conversion ratio 2yr | FY2024 329% / FY2025 116% — both far above 70% | >70% for 2+ consecutive years | ✅ PASS |
| Share issuance pattern | One-time M&A issuance (VMware, Nov 2023), followed by active buybacks ($10B program, Feb 2026) | not dilutive | ✅ PASS |
| Moat signal | Dominant custom-ASIC/AI-accelerator partner (Google TPU, Meta, ByteDance, others), networking silicon leadership (Tomahawk/Jericho), VMware enterprise virtualization franchise | required | ✅ present — see §6 |

**Gate result: PASS — comfortably and decisively on all 8 quantitative criteria.** Several metrics (Net margin, Revenue CAGR, FCF/NI conversion) clear their thresholds by more than 2x. Proceeding to the Rate Environment Gate and Phase 02 scoring.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = 24.50×
EY         = 1 ÷ 24.50 = 4.08%
Spread     = EY − 10Y Treasury = 4.08% − 4.49% = −0.41%
```
Spread (−0.41%) < +1.5% threshold → **fails** the spread test → **+5 additive** (yellow flag, not a veto, per the 2026-06-07 revision).

**Step 2 — Rate Regime Modifier**
10Y yield = 4.49% → falls in the **3.5–5% bracket → +5**

**Combined Rate Modifier: +5 (Step 1) + 5 (Step 2) = +10**

---

## 5. Phase 02 — Full Valuation Score

### FCF Yield (40% weight)

```
FCF (FY2025)  = $26,914M (≈$26.9B, 42.1% of revenue)
Market Cap    = $382.07 × 4,876M ≈ $1,862,973M
FCF Yield     = $26,914M ÷ $1,862,973M ≈ 1.44%
```

```
FCF_Score = clamp(100 × (1 − FCF_Yield% / 10), 0, 100)
          = clamp(100 × (1 − 1.44/10), 0, 100)
          = clamp(100 × 0.856, 0, 100)
          = 85.60
```

No Owner Earnings adjustment (Upgrade 1) applies — see §2, total capex is ~1% of revenue, immaterial.

**FCF_Score = 85.60**

### EV/EBIT (25% weight initially — see PEG discussion for final weighting)

```
EV       = Market Cap $1,862,973M + Net Debt $45,279M ≈ $1,908,252M
EBIT TTM = $30,443M
EV/EBIT  = $1,908,252M ÷ $30,443M ≈ 62.68×
```

```
EV/EBIT_Score = clamp((EV/EBIT − 12) / 23 × 100, 0, 100)
              = clamp((62.68 − 12) / 23 × 100, 0, 100)
              = clamp(220.3, 0, 100)
              = 100.00
```

⚠️ Using FY2025 EBIT ($25,484M) instead of TTM gives EV/EBIT ≈ 74.9×, which clamps to the same 100.0 — **the result is insensitive to this choice**, both are far past the 35× = 100.0 ceiling. As flagged in §2, GAAP EBIT here is depressed ~35-40% by non-cash VMware amortization (~$9.3B/yr); even adding that back would only bring EV/EBIT toward the high-40×/low-50× range — still well past 35×. **EV/EBIT_Score = 100.00 either way.**

**EV/EBIT_Score = 100.00**

### Forward PE + Historical PE Modifier (20% weight)

Only a 10yr **average** PE is available (68.51×) — no documented low/high range — so the **fallback formula** applies:

```
Forward PE    = 24.50×
10yr Avg PE   = 68.51×
Deviation%    = (24.50 − 68.51) / 68.51 × 100 = −64.24%
FwdPE_Score   = clamp(50 + Deviation% × 2.5, 0, 100)
              = clamp(50 + (−64.24 × 2.5), 0, 100)
              = clamp(50 − 160.6, 0, 100)
              = clamp(−110.6, 0, 100)
              = 0.00
```

This formula already folds in the Historical PE Modifier (Upgrade 2) — no separate ±10 applied. The −64% deviation is dramatic, but driven by AVGO's PE ratio nearly halving from a 10yr average heavily weighted toward its smaller pre-VMware/pre-AI-supercycle self, set against forward earnings that have just stepped up sharply (FY2025 non-GAAP EPS +40.5% YoY).

**FwdPE_Score = 0.00**

### PEG (15% weight) — Fast Grower classification

Non-GAAP diluted EPS growth (computed §2): FY22→23 **+12.2%**, FY23→24 **+14.9%**, FY24→25 **+40.5%**. 3yr CAGR **+21.9%**.

**Classification call:** The strategy.md test reads "EPS growth >15% for 3+ years." Read literally year-by-year, 2 of the last 3 years (12.2%, 14.9%) fall just *short* of 15% — though both are within ~3pp of the line, and the trend is sharply **accelerating** (not decelerating, unlike e.g. the MA 2026-06-07 session where a Stalwart classification was driven by *decelerating* growth toward ~11-15%). The 3yr CAGR (21.9%) clears 15% comfortably, and the forward trajectory is unambiguously hyper-growth: Q1 FY2026 AI semiconductor revenue +106% YoY, Q2 FY2026 AI semiconductor revenue +143% YoY, overall Q2 FY2026 revenue +48% YoY.

Given the framework's intent — distinguishing genuinely fast-growing compounders (where PEG is informative) from mature Stalwarts (where it isn't) — and AVGO's currently-accelerating, AI-driven growth profile, **I classify AVGO as a Fast Grower** for this session. This is a judgment call on a borderline case; flagged explicitly for review at the next re-score, where another 1-2 quarters of EPS growth data will make the 3yr trailing window cleaner.

```
PEG (reported, stockanalysis.com) = 0.53
PEG_Score = clamp((PEG − 0.5) / 2.0 × 100, 0, 100)
          = clamp((0.53 − 0.5) / 2.0 × 100, 0, 100)
          = clamp(1.50, 0, 100)
          = 1.50
```

**PEG_Score = 1.50**

*(Cross-check: using Forward PE ÷ FY24→25 EPS growth as an alternate PEG estimate = 24.50/40.5 ≈ 0.61 → PEG_Score ≈ 5.50. Either figure rounds the final score to essentially the same place — see Final Score below.)*

### Final Score Calculation

PEG applies (Fast Grower) → weights are FCF 40% / EV-EBIT 25% / FwdPE 20% / PEG 15%.

```
Final Score = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.25) + (FwdPE_Score × 0.20) + (PEG_Score × 0.15) + Rate Modifier
            = (85.60 × 0.40)     + (100.00 × 0.25)        + (0.00 × 0.20)        + (1.50 × 0.15)      + 10
            = 34.24              + 25.00                  + 0.00                 + 0.225               + 10
            = 69.465 + 10
            = 69.465
```

Wait — recomputing cleanly:
```
Raw weighted score = 34.24 + 25.00 + 0.00 + 0.225 = 59.465
Final Score = 59.465 + 10 (Rate Modifier) = 69.465
```

Round to nearest 0.1 → **69.5** (69.465 rounds to 69.5 under standard rounding; not exactly on a ".X5" boundary so the round-up rule doesn't additionally apply)

*(Cross-check using alternate PEG=0.61 → PEG_Score=5.50: raw = 34.24+25.00+0.00+0.825 = 60.065; +10 = 70.065 → rounds to 70.1. Both PEG readings land the score either just below or just above the 70.0 Hold/Trim boundary — see §6 for why this doesn't change the action recommendation.)*

---

## 6. Final Valuation Score & Action

# **Final Score: 69.5 — "Fair Value" (upper edge, bordering "Expensive")**

| Score | Label | Action (Phase 03/05 — strategy.md Action Table) |
|---|---|---|
| **50.0–69.9** | Fair Value | HOLD — watch only, no new entry, no trim |
| **70.0–79.9** | Expensive | Trim 25–30% (n/a — not held) |

At **69.5**, AVGO falls just inside the top of the "Fair Value / Hold-watch" band — one of the two PEG readings (0.61 instead of 0.53) would push it to 70.1, just over the line into "Expensive." **Either way, the action recommendation for a *new position* is identical**: Score ≥50.0 means **no new entry** per Phase 03 ("50.0–69.9 → Fair Value → Watchlist only, no new entry" / "70.0–100.0 → Expensive → Do not buy"). The 69.5-vs-70.1 distinction would matter for trim decisions on an *existing* holding, but is moot for a new-position evaluation.

### What's driving this score

- **FCF Yield (85.6, expensive)** and **EV/EBIT (100.0, maximally expensive)** both say "richly valued" — AVGO trades at ~1.4% FCF yield and ~63-75× EV/EBIT, both far past this framework's "cheap" zones.
- **Forward PE vs 10yr history (0.0, cheapest possible)** and **PEG (1.5, very cheap)** say the opposite — AVGO's forward PE (24.5×) is ~64% *below* its own 10yr average (68.5×), and at a 0.53 PEG it looks statistically cheap relative to its (accelerating) growth rate.
- This is a genuinely **bifurcated** valuation picture, and it's traceable to a specific structural cause: **AVGO's GAAP EBIT is depressed ~35-40% by non-cash VMware-acquisition amortization** (~$9.3B/yr against a ~$25.5B GAAP EBIT base), which inflates EV/EBIT mechanically without reflecting the underlying cash-generative or earnings reality — while FCF, non-GAAP EPS, and the PEG ratio are comparatively unaffected by this purchase-accounting artifact.
- The **+10 Rate Modifier** (the maximum combined Step 1 + Step 2 contribution under current rules) pushes what would otherwise be a sub-60 raw score into the high-60s.

### Qualitative cross-check (5 questions + disruption vector)

1. **Why are margins high?** Custom-silicon design leadership (TSMC-fabbed, Broadcom-designed AI accelerators for Google TPU, Meta, ByteDance and others) commands premium pricing on IP/design value-add; VMware adds a high-margin enterprise software franchise with strong renewal economics post-acquisition repricing.
2. **What would it take to compete?** Multi-year, multi-billion-dollar custom-ASIC design relationships with hyperscalers, deep networking-silicon IP (Tomahawk/Jericho switch chips), and an enterprise virtualization installed base (VMware) that's costly to migrate off — a combination of switching-cost and technical/scale moats.
3. **Capital allocation:** VMware acquisition (~$61B cash+stock, completed Nov 2023) was the dominant capital-allocation event of the past 3 years; post-deal, the company has prioritized debt paydown and resumed buybacks ($10B program announced Feb 2026) plus a maintained/growing dividend.
4. **Growth sources next 3–5 years:** AI semiconductor revenue (custom XPUs/ASICs + AI networking) is the dominant growth driver — Q2 FY2026 AI semis revenue +143% YoY; VMware/infrastructure software provides a steadier, high-margin complement.
5. **Best bear case:** Customer concentration risk in AI semis (a handful of hyperscaler customers represent the bulk of AI revenue — loss of or reduced spend by any one is a meaningful swing factor); GAAP earnings will remain depressed by VMware amortization for years, which could keep traditional earnings-based multiples looking "expensive" even if the cash economics are fine — a persistent source of valuation-methodology noise for this name.
6. **Disruption vector check:** In-house silicon programs at the largest hyperscaler customers (some of whom Broadcom currently designs custom chips *for*) could eventually internalize more of this design work; more broadly, any slowdown in the AI capex supercycle (which Broadcom's most recent growth has been almost entirely dependent on) would hit this name hard and fast given how much of the recent re-rating is AI-driven.

---

## 7. Order Setup — NOT PRODUCED (by design)

Per the operating brief, the full Fair-Value/DCF/buy-sell-stop workup is run **"for every BUY or TRIM action."** A Score of 69.5 is neither a BUY (requires ≤49.9) nor a TRIM (n/a for a non-held name; and TRIM only triggers at ≥70.0 for *held* positions anyway). The order-setup checklist gates on *"Valuation Score: ___ (must be ≤ 49.9 to enter)."* Building a full 3-scenario DCF here would mean producing buy/sell/stop levels for a trade the framework explicitly says not to make — consistent with the MA 2026-06-07 session's same convention at a similar score.

**What can be said without inventing numbers:** $382.07 sits ~24-27% below the analyst consensus PT cluster (~$501-522) — that's *other parties'* fair-value reads, cited per Rule 0 Step 4, not this framework's own blended FV. The valuation-score engine reads "fair value, upper edge" (69.5) because EV/EBIT and FCF yield — both heavily weighted (65% combined) — are at or near their most-expensive readings, even though the PE-relative-to-history and PEG signals are at the opposite (cheapest) extreme.

**Rough sense of what could move this toward a BUY** (scenario sketch only, not a standing order or trigger to act on): the EV/EBIT sub-score is the single largest contributor to the current score (25.0 of the 59.5 raw points) and is structurally elevated by VMware amortization that will *mechanically decline* over the amortization schedule's remaining life, gradually lifting reported GAAP EBIT even with no change in the underlying business. Separately, continued AI-semiconductor revenue growth at anywhere near the current ~100-150% YoY pace would also lift TTM EBIT materially over the next few quarters, pulling EV/EBIT down toward the 35-45× range (still elevated vs. the 35× = 100.0 ceiling, but materially better) without any price decline at all. **This is a name where the score could improve meaningfully on fundamentals alone (EBIT recovery) even at a flat-to-higher price** — worth a fresh re-score every quarter regardless of price action.

---

## 8. Recommendation

# **WATCHLIST ONLY — do not open a position now.**

AVGO passes the Phase 01 quality gate **decisively and on every one of the 8 quantitative criteria** — several (net margin, revenue CAGR, FCF/NI conversion) by more than 2x their thresholds. It is, by the numbers, one of the cleanest Phase 01 passes seen in this framework's recent sessions. But the Phase 02 valuation score of **69.5 ("Fair Value," upper edge)** means there is currently **no margin of safety** for a new entry — Score ≥50.0 means watchlist-only per Phase 03, regardless of which side of the 69.9/70.0 line the PEG-sensitivity lands on.

The score is a genuine **tug-of-war between two valuation lenses**: FCF yield and EV/EBIT (both saturated at "maximally expensive") vs. forward-PE-vs-history and PEG (both at "maximally cheap"). The EV/EBIT reading in particular is **structurally distorted** by ~$9.3B/yr of non-cash VMware amortization depressing GAAP EBIT — a genuine "is this multiple a real signal or an accounting artifact?" question that Rule 6 (normalize before you value) flags but that this framework's prescribed EV/EBIT formula (using reported GAAP EBIT) doesn't currently resolve. This is worth tracking as the amortization schedule runs off over the next several years and GAAP EBIT mechanically recovers toward cash-economic reality.

**Add AVGO to the watchlist** (`not-in-portfolio/AVGO/`) with a re-evaluation trigger at:
- **Next earnings release** (AVGO reports Q3 FY2026 results ~September 2026) — re-run Phase 02 with refreshed TTM EBIT (watch for the EV/EBIT sub-score moving off its 100.0 ceiling as VMware amortization runs off and/or AI-semi revenue growth lifts TTM EBIT).
- A cleaner **3-year EPS growth window** (one more quarter resolves the FY22→23/FY23→24 borderline-15% ambiguity in the Fast Grower classification).
- A **>15% unexplained price move** from $382.07 (Rule 9) — particularly a *decline* toward the 52-week low ($241.11) would meaningfully improve FCF yield and could shift the action band.
- Any **guidance revision, M&A, or management change** (Rule 9).

---

## 9. Next Review Trigger

**Date/event:** AVGO's Q3 FY2026 earnings release (expected ~September 2026) — re-run Phase 02 with refreshed TTM EBIT, TTM FCF, and a cleaner 3yr EPS-growth window for the Fast Grower classification. Earlier trigger if a >15% unexplained price move from $382.07 occurs (Rule 9), or any guidance/M&A/management-change event.

**No position opened — nothing to log in `decisions/`.**

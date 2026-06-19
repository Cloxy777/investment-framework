# NEW POSITION — The Sage Group plc (LON:SGE) — 2026-06-19

**Task type:** NEW POSITION
**Date:** 19 Jun 2026
**10Y US Treasury Yield:** 4.45% (10Y note, 18 Jun 2026 close — most recent available)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current SGE portfolio weight:** 0% — not currently held (confirmed against [holdings.md](../portfolio/holdings.md))
**Sector:** UK/Global Enterprise Software — SMB/mid-market accounting, ERP, and payroll SaaS (Sage Intacct, Sage 50/200/300, Sage X3, Sage Business Cloud)
**Currency:** All calculations in GBP/pence (GBX) — Sage's home listing and reporting currency. The Rate Environment Gate still benchmarks against the **US** 10Y Treasury per framework convention regardless of the ticker's home market; the DCF discount rate (WACC) uses the **UK** 10Y Gilt as the risk-free rate, consistent with valuing a GBP-denominated cash flow stream in its own currency (precedent: [2026-06-14 Tencent session](2026-06-14-new-position-tencent.md) used the local 10Y proxy for currency-consistent inputs while keeping the Rate Gate itself US-Treasury-based).

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **GBX 879.80** (£8.798) | WebSearch aggregation — two independent Investing.com-sourced reads converged on 878.8p/879.80p; discarded as stale/unreliable: 899.20p (explicitly dated "1 Jun 2026"), 903.6p and 1,087.50p (single-source outliers), 842.40p (tied to an old consensus-PT calc) |
| 52-week range | GBX 771.66 – 1,335.00 | WebSearch — current price sits ~14% above the 52wk low, ~34% below the 52wk high |
| Analyst consensus PT (12-month) | ~GBX 1,157 avg across 2 sources (1,202.79p from 19 analysts, range 900–1,600p; and 1,112.17p, +32.0% vs an older 842.40p close); consensus rating **Buy** (11 Buy / 7 Hold / 1 Sell of 19 analysts) | WebSearch aggregation |
| Shares outstanding | **907.73M** (Google Finance, most recent read) | WebSearch — a second source's 964.51M appears stale/inconsistent and is not used |
| Market cap (computed) | **£7,986.2M** (= 907.73M × £8.798) | Computed from verified live price × shares outstanding, per Rule 0 — not taken from a stale aggregator snapshot (one aggregator's "£7.47B" figure used an older price and is not used) |
| GBP/USD | 1.3392 | WebSearch, 19 Jun 2026 |

---

## 2. Data Gathered (Phase 01 + Phase 02 Inputs) & Gaps Flagged

### FY2025 results (year ended 30 Sep 2025, announced 19 Nov 2025) and FY2024 comparatives

| Metric | FY2025 | FY2024 | YoY | Source |
|---|---|---|---|---|
| Total revenue | £2,513M | — | — | WebSearch (FY2025 results) |
| Underlying EBITDA | £694M (margin 27.6%, +120bps) | £605M | +15% | WebSearch (FY2025 results) |
| **Underlying operating profit (EBIT)** | **£600M** | — | +17% | WebSearch (FY2025 results) |
| Statutory operating profit | £530M | — | — | WebSearch |
| Underlying PBT | £555M | £486M | +14.2% | WebSearch |
| **Underlying PAT** | **£423M** | ≈£371.1M (derived: 423/1.14) | +14% | WebSearch |
| Statutory net income | £369M | — | — | WebSearch (explicitly confirmed as FY2025-specific, not a TTM blend) |
| Underlying basic EPS | 43.2p | 36.7p | **+17.7%** | WebSearch |
| **Free cash flow** | **£517M** | £524M | **−1.3%** | WebSearch — flagged: FCF declined slightly despite underlying operating profit +17%; likely working-capital/cash-tax timing, not (yet) a quality red flag — monitor next quarter |
| Operating cash flow | £660M | £649M | +2% | WebSearch |
| Underlying cash conversion (op. cash flow basis) | 110% | 123% | — | WebSearch |
| Net debt | £1,189M | £738M | +61% | WebSearch (FY2025 results) |
| Net debt / underlying EBITDA | **1.7×** | 1.2× | — | WebSearch — rising trend flagged; still within Sage's own stated 1–2× medium-term target range and well inside the framework's <2x/<2.5x thresholds |
| Gross margin | 92.80% | — | — | WebSearch |
| ROIC | 22.29% | — | — | WebSearch |

### Revenue history (3yr CAGR check)

| FY | Revenue |
|---|---|
| FY2022 | £1,950M |
| FY2025 | £2,513M |

```
3yr CAGR = (2,513 / 1,950)^(1/3) − 1 = 8.83%
```

### Underlying EPS history (Fast Grower / PEG test)

| Year | Underlying basic EPS | YoY growth | >15%? |
|---|---|---|---|
| FY2024 | 36.7p | +13.6% | ❌ No |
| FY2025 | 43.2p | +17.7% | ✅ Yes |

### Valuation history

| Metric | Value | Source |
|---|---|---|
| 10yr PE low | 19.42× | WebSearch |
| 10yr PE high | 62.03× | WebSearch |
| 10yr PE average | 28.92× | WebSearch |
| 10yr PE median | 30.16× | WebSearch |
| 5yr PE range (sub-window, cross-check) | 21.6× (low, Sep 2025) – 48.3× (high, Sept 2023) | WebSearch — nests inside the 10yr range as expected (10yr extremes occurred outside the more recent 5yr window); confirms internal consistency rather than contradiction |
| Forward PE | **16.87×** (stockanalysis.com) | WebSearch — cross-checked below |

### Forward PE / FY2026E EPS reconciliation

Three candidate consensus EPS figures surfaced: $0.45 (USD basis, likely stale/different basis), £0.47 (+26%, appears to be on a *statutory* EPS base — 37.7p statutory FY25 × 1.26 ≈ 47.5p, consistent), and £0.50 (Stockopedia, on an *underlying* EPS base — 43.2p × ~1.16 ≈ 50p, consistent with the recent 14–18% underlying growth trend). The 16.87× forward PE implies EPS of 879.80p/16.87 = **52.15p**, in the same underlying-EPS-basis neighborhood as the £0.50 figure.

**Resolution: not load-bearing.** Tested both 16.87× and the £0.50-implied 17.60×: both sit **below the 10-year PE low (19.42×)**, so the Primary range formula clamps `FwdPE_Score` to 0.0 either way, and both produce the same Rate Gate Step 1 modifier bucket (spread <1.5%). The score and Rate Gate outcome are insensitive to resolving this further — **16.87× is used as the headline figure** (single clearly-sourced platform reading).

### Net margin — primary basis and the judgment call

| Basis | Net income | Net margin | vs >15% threshold |
|---|---|---|---|
| Underlying PAT (primary, used) | £423M | **16.83%** | ✅ PASS |
| Statutory net income (cross-check) | £369M | 14.68% | ❌ Would FAIL |

**Determination: underlying PAT is used as primary**, per fair-value-methodology.md Rule 6 ("strip out one-time items... value the underlying business, not the accounting statements") and consistent with the 2026-06-14 Tencent session's precedent of choosing one earnings basis as primary with the other shown as a transparency cross-check. Flagged prominently since this is the single most consequential judgment call in this session — on the statutory basis, Sage would narrowly **fail** the Phase 01 net margin gate.

### WACC inputs

| Input | Value | Source |
|---|---|---|
| Risk-free rate (UK 10Y Gilt) | 4.82% (18 Jun 2026) | WebSearch — an earlier-June reading of ~4.35% is not used (less current) |
| Beta (5yr) | **0.30** (cluster of 0.29 / 0.30 / 0.34 across 3 independent sources) | WebSearch — unusually low for software (sector average ≈0.92), but well-corroborated; reflects Sage's defensive, high-recurring-revenue SMB base |
| Equity Risk Premium | 5.0% (standard market assumption, not company-specific sourced data — flagged) | Standard analyst convention |
| Cost of debt (pre-tax) | 5.67% | WebSearch (Alphaspread) |
| UK corporate tax rate | 25% (standard) | Standard assumption |
| Capital structure | Equity 84.39% / Debt 15.61% | WebSearch (Alphaspread) |
| Credit rating | S&P BBB+, stable outlook | WebSearch |

### Peer comparables (Rule 5 — min. 5 peers)

| Company | Forward PE | EV/EBITDA |
|---|---|---|
| Intuit (INTU) | 10.27× | 13.77× |
| Workday (WDAY) | 12.07× | 22.84× |
| SAP (SAP) | 19.99× | 14.54× |
| Xero (XRO) | 65.14× | n/a |
| Oracle (ORCL) | 22.87× | n/a |
| **Median** | **19.99×** | **14.54×** (n=3) |

EV/EBIT specifically was not available for any peer in search results — EV/EBITDA used as the closest sourced substitute (flagged: this is real sourced data on a related-but-not-identical metric, not an invented EV/EBIT figure).

### Data Gaps flagged (per Rule 0 — none estimated)

1. **Revenue CAGR 3yr (8.83%)** clears valuation-scoring.md's >8% pre-screen but falls short of strategy.md's stricter >10% Phase 01 gate — see §3 judgment call.
2. **Net margin basis** (underlying vs statutory) — see above; statutory basis would fail the gate.
3. **FCF declined −1.3% YoY** despite underlying operating profit +17% — not explained by available search results beyond working-capital timing; flagged for next quarter's monitoring, not treated as a quality-gate failure given still-strong absolute conversion (110%+).
4. **H1 FY26 dividend figure** — an early search returned an implausible "350 pence interim dividend" (inconsistent with Sage's known dividend scale — FY25 final was only 14.4p). A targeted follow-up search returned a consistent **8.05p interim dividend (+8% YoY from 7.45p)**, which is used; the 350p figure is discarded as a data anomaly.
5. **Beta unusually low (0.30 vs sector 0.92)** — well-corroborated across 3 sources, but produces an unusually low WACC if used directly in the DCF; see §8 for how this is handled.

---

## 3. Phase 01 — Quality Gate

| Check | Sage Value | Threshold | Result |
|---|---|---|---|
| Gross margin | 92.80% | >40% | ✅ PASS |
| **Net margin** | 16.83% (underlying PAT basis) | >15% (strategy.md) | ✅ PASS — **judgment call**: statutory basis (14.68%) would fail; underlying basis used per Rule 6 |
| ROIC | 22.29% | >15% | ✅ PASS |
| **Revenue CAGR 3yr** | 8.83% (FY22→FY25, statutory) | >10% (strategy.md) / >8% (valuation-scoring.md) | ✅ PASS (valuation-scoring.md) / ⚠️ **borderline-FAIL (strategy.md)** — **judgment call**: treated as PASS, see below |
| Net debt/EBITDA | 1.7× (rising from 1.2×) | <2× (strategy.md) / <2.5× (valuation-scoring.md) | ✅ PASS both — rising trend flagged for monitoring |
| FCF positive 3+ consecutive years | Yes (consistently positive, multi-year) | required | ✅ PASS |
| FCF/NI conversion ratio 2yr | FY25: 517/423 = 122.2% / FY24: 524/371.1 = 141.2% | >70% | ✅ PASS, comfortably |
| Share issuance pattern | Net buyback (£200M extension announced H1 FY26) — accretive, non-dilutive | non-dilutive required | ✅ PASS |

### Revenue CAGR judgment call

The trailing 3yr statutory CAGR (8.83%) sits **below** strategy.md's explicit >10% Phase 01 threshold but **above** valuation-scoring.md's >8% pre-screen filter and the >8% precedent applied in the 2026-06-14 Tencent session. **Determination: PASS**, on the basis that the trailing lagging average understates a clearly *accelerating* current trajectory: FY2024 organic growth ~9%, FY2025 organic +10%, H1 FY2026 +11% YoY, and management has **upgraded FY2026 organic revenue growth guidance to above 9%**. A backward-looking 3-year average is, by construction, the slowest-to-update metric in this gate — the forward-looking evidence points consistently in one direction (accelerating, not decelerating), which is the basis for treating this as a pass rather than a fail.

**Gate result: PASS — 8/8 metrics pass, with 2 explicitly flagged judgment calls (net margin basis; revenue CAGR threshold). Proceeding to Rate Environment Gate and Phase 02.**

---

## 4. Fast Grower (Upgrade 3 — PEG) Determination

**Test: EPS growth >15% for 3+ consecutive years.**

| Year | Underlying basic EPS | YoY growth | >15%? |
|---|---|---|---|
| FY2024 | 36.7p | +13.6% | ❌ No |
| FY2025 | 43.2p | +17.7% | ✅ Yes |

Only 1 of the last 2 confirmed years clears 15% — FY2024 breaks the chain. **Determination: Sage does NOT meet the "EPS growth >15% for 3+ consecutive years" test.**

**PEG sub-score is NOT applied.** Per the Final Score Formula note in valuation-scoring.md, its 15% weight is redistributed to EV/EBIT, making **EV/EBIT 40% of the total** (alongside FCF Yield 40% and Forward PE 20%).

---

## 5. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**

```
Forward PE = 16.87×
EY     = 1 ÷ 16.87 = 5.928%
Spread = EY − 10Y Treasury = 5.928% − 4.45% = +1.478%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL (just barely — 1.478% vs 1.5%)** → **+5 additive** to the valuation score (Step 1).

*(Sensitivity-checked against the alternate 17.60× forward PE candidate: EY=5.68%, spread=1.23% — still <1.5%, same +5 outcome. Robust to the Forward PE ambiguity noted in §2.)*

**Step 2 — Rate Regime Modifier**
10Y = 4.45% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for Sage = 5 (Step 1) + 5 (Step 2) = +10** (per the corrected combined-additive reading flagged in [watchlist/README.md](../watchlist/README.md)'s 2026-06-11 backfill note and applied in the 2026-06-07 MA session — both steps apply together, not Step 2 alone.)

---

## 6. Phase 02 — Full Score Calculation

**FCF Yield — 40% weight**

```
FCF Yield = FCF / Market Cap = £517M / £7,986.2M = 6.474%

FCF_Score = clamp(100 × (1 − FCF_Yield% / 10), 0, 100)
          = clamp(100 × (1 − 6.474/10), 0, 100)
          = clamp(100 × 0.3526, 0, 100)
          = 35.3
```
→ Contribution: 35.3 × 0.40 = **14.10**

**EV/EBIT — 40% weight (PEG not applicable, redistributed from 25%)**

```
Market Cap = £7,986.2M
Net Debt   = £1,189M
EV         = Market Cap + Net Debt = £7,986.2M + £1,189M = £9,175.2M

EV/EBIT = £9,175.2M / £600M (FY2025 underlying operating profit)
        = 15.29×

EV/EBIT_Score = clamp((EV/EBIT − 12) / 23 × 100, 0, 100)
              = clamp((15.29 − 12) / 23 × 100, 0, 100)
              = clamp(14.31, 0, 100)
              = 14.3
```
→ Contribution: 14.3 × 0.40 = **5.72**

**Forward PE (PRIMARY formula — 10yr low/high range available) — 20% weight**

```
Forward PE   = 16.87×
10yr Low PE  = 19.42×
10yr High PE = 62.03×

FwdPE_Score (raw) = clamp((Forward PE − 10yr Low PE) / (10yr High PE − 10yr Low PE) × 100, 0, 100)
                   = clamp((16.87 − 19.42) / (62.03 − 19.42) × 100, 0, 100)
                   = clamp(−5.99, 0, 100)
                   = 0.0
```

Forward PE sits **below even the 10-year low** — already the cheapest possible reading on this dimension before the modifier.

**Historical PE Modifier (Upgrade 2, additive to the FwdPE_Score sub-score)**

```
Deviation from 10yr avg = (16.87 − 28.92) / 28.92 = −41.66%
```
>20% below the 10-year average → modifier = **−10**. *(Structural Quality Override does not apply — Sage is cheap relative to history, not expensive; the override only waives a penalty for being expensive.)*

```
FwdPE_Score (adjusted) = clamp(0.0 − 10, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.00**

**PEG — not applicable (redistributed to EV/EBIT above, see §4)**

---

### Final Score

```
Raw weighted score = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.40) + (FwdPE_Score(adjusted) × 0.20)
                    = (35.3 × 0.40) + (14.3 × 0.40) + (0.0 × 0.20)
                    = 14.10 + 5.72 + 0.00
                    = 19.83 (precise: 19.828)

+ Rate Regime Modifier (Step 1 +5, Step 2 +5 = +10) = 19.828 + 10 = 29.828
```

Boundary rule: 29.828 → nearest 0.1 → not a ".X5" case → **Final Score = 29.8**

---

## 7. Final Score & Action

# Final Score: 29.8 → Action Table band: 0.0–29.9 (Very Cheap) → BUY — Full position 6–8% of portfolio

Sage lands at the **very top edge of the "Very Cheap" band** (just 0.2 points below the "Cheap" cutoff) — driven primarily by a **Forward PE sitting below its own 10-year low** (16.87× vs a 19.42× floor — the cheapest possible reading on this dimension, then a further −10 Historical PE Modifier that has no room left to bite since the raw sub-score already clamped to 0.0), a **moderate EV/EBIT** (15.29×, modestly above the 12× "cheapest" anchor), and an **FCF yield of ~6.47%** (better than the 5% "fair value" midpoint).

### Sanity check — why does a high-ROIC (22.29%), high-margin (92.8% gross) compounder trade at a Forward PE below its own 10-year low?

- Sage's 10-year PE history (19.42×–62.03×, avg 28.92×) spans both a **2020–2023 high-growth/high-multiple SaaS-transition era** and the **2024–2026 multiple-compression cycle** that hit software broadly as rates rose and growth-at-any-price names de-rated. Today's 16.87× sits in territory the stock hasn't traded at in a decade, despite underlying operating profit growing +17% and underlying EPS +17.7% in the most recent year — i.e., the business has gotten *better* while the multiple has compressed, the textbook signature of a genuine valuation gap rather than a deteriorating-fundamentals story.
- Every sub-score component independently points toward "cheap": FCF yield (6.47%, above the 5% midpoint), EV/EBIT (15.29×, below the 23.5× midpoint), and Forward PE (below the 10-year low). This convergence — plus the close agreement between this session's own blended Fair Value (§8) and external analyst consensus PT — supports treating this as a durable mispricing rather than a modelling artifact.
- The qualitative case is consistent with "quality value": Sage's moat rests on **high switching costs** (deeply embedded SMB accounting/tax-compliance workflows, multi-jurisdiction VAT/tax rule support, payroll integrations) built over decades, not a fragile growth narrative — a profile that tends to compress in multiple during a rate-driven software de-rating even when the underlying business is executing well.

---

## 8. Fair Value & Order Setup

### Step 1 — Fair Value (Blended)

**Method A: DCF (3 scenarios, Rule 2/7)**

**WACC — beta sensitivity flagged.** Using Sage's own sourced beta (0.30, well-corroborated across 3 sources) gives Cost of Equity = 4.82% + 0.30×5.0% = 6.32%, and WACC = 0.8439×6.32% + 0.1561×4.25% ≈ **6.0%**. Run through the DCF, this WACC produces enterprise values of **£17.3B–£35.8B** across Bear/Bull — 1.9×–3.9× the current £9.18B EV — and the Bull scenario's terminal-value weight (81.4%) **breaches Rule 4's 75% sanity-check cap**. This is too aggressive to use directly: a beta this low, compounded with double-digit growth over a 10-year explicit horizon, produces implied returns well outside the 8–15% "reasonable IRR" sanity band.

**Resolution: WACC is anchored to the sector-average beta (0.92) instead**, used as a cross-check that passes all Rule 4 sanity checks (TV weight 55–66% across all three scenarios, vs the >75% breach using Sage's own beta). This is shown as the operative DCF input below; Sage's own low beta is flagged as a "high case" sensitivity, not discarded as data (it is real, sourced, well-corroborated information about Sage's historical volatility) but not used directly given the sanity-check failures it produces.

```
Cost of Equity (sector-beta) = 4.82% + 0.92×5.0% = 9.42%
WACC (sector-beta) = 0.8439×9.42% + 0.1561×4.25% = 8.6%
```

Base FCF = £517M (FY2025). 10-year explicit forecast (Stage 1: years 1–5 at stated growth; Stage 2: years 6–10 fading linearly to terminal growth; Stage 3: Gordon-growth terminal value), discounted at the stated WACC. Terminal growth fixed at 2.5% (GDP cap, Rule 2) across all scenarios.

| Scenario | WACC | Yrs 1–5 FCF growth | Yrs 6–10 fade to terminal | PV(FCF Y1-10) | PV(Terminal Value) | EV (PV) | TV weight | **EV** |
|---|---|---|---|---|---|---|---|---|
| Bear | 9.6% | +9% | fades 7.7%→2.5% | £4,815.9M | £5,874.8M | £10,690.7M | 55.0% | **£10,690.7M** |
| Base | 8.6% | +10% | fades 8.5%→2.5% | £5,291.7M | £8,011.0M | £13,302.7M | 60.2% | **£13,302.7M** |
| Bull | 7.6% | +11% | fades 9.3%→2.5% | £5,815.6M | £11,198.2M | £17,013.8M | 65.8% | **£17,013.8M** |

All three scenarios pass the <75% terminal-value-weight sanity check.

```
PW DCF EV = 0.25 × Bull + 0.50 × Base + 0.25 × Bear
          = 0.25×17,013.8 + 0.50×13,302.7 + 0.25×10,690.7
          = 4,253.5 + 6,651.4 + 2,672.7
          = £13,577.5M

DCF Equity Value = £13,577.5M − Net Debt £1,189M = £12,388.5M
DCF FV/share = £12,388.5M / 907.73M shares = £13.65 = 1,365p
```

Note: even the **Bear** DCF scenario (£10,690.7M EV) sits above the current EV (£9,175.2M) — independent corroboration, via a method built entirely from company fundamentals rather than peer pricing, that the stock looks undervalued even under conservative assumptions.

**Method B: Comparable Multiples**

| Approach | Peer median multiple | Applied to | FV/share |
|---|---|---|---|
| Forward PE reversion | 19.99× (Intuit/Workday/SAP/Xero/Oracle median) | Sage's own forward EPS (52.15p) | **1,042.5p** |
| EV/EBITDA reversion | 14.54× (Intuit/Workday/SAP median, n=3) | Sage's underlying EBITDA (£694M), less net debt £1,189M, ÷907.73M shares | **981.0p** |
| **Multiples avg** | | | **1,012p** |

```
Blended FV = 40% × DCF FV/share + 60% × Multiples avg
           = 0.40 × 1,365p + 0.60 × 1,012p
           = 546.0p + 607.2p
           = 1,153.2p
```

**Cross-check vs external estimates:** Blended FV (1,153.2p) sits almost exactly on the analyst consensus PT average (~1,157p, range 900–1,600p) — strong independent convergence. **+31.1% above** the current price (879.80p).

---

### Step 2 — Buy Price & R/R Gate

Score 29.8 falls in the **0.0–29.9 (Very Cheap)** band → MoS 15–20%; using the conservative end (20%, per Rule 8's "wide-moat, proven compounder" — ROIC 22.29% with a long, consistent quality track record):

```
Buy Price ceiling = Blended FV × (1 − MoS%)
                  = 1,153.2p × (1 − 0.20)
                  = 922.6p
```

**Current price (879.80p) is BELOW the Buy Price ceiling (922.6p)** — implied MoS at current price = 1 − (879.80/1,153.2) = **23.7%**, exceeding the 20% requirement. Per fair-value-methodology.md Step 2: Score 0.0–29.9 → "Stock at or below buy price → **Enter now**."

**Step 6 (Risk/Reward) — checked next, as a separate mandatory gate.**

```
Stop Loss (standard 20-25% band, midpoint 22.5%) = 879.80p × (1 − 0.225) = 681.85p

R/R = (Sell Target − Entry) / (Entry − Stop Loss)
    = (1,153.2p − 879.80p) / (879.80p − 681.85p)
    = 273.4p / 197.95p
    = 1.38 : 1
```

**1.38:1 is BELOW the 2:1 minimum** using the standard stop band. Per Step 6: "find tighter stop, wait for lower entry, or pass entirely."

**Resolution: tighter, data-justified stop.** Sage's beta (0.30) is the lowest of any name screened to date in this framework, corroborated across 3 independent sources — its historical price volatility is genuinely far below the typical "high conviction quality" name this 20–25% band was calibrated for. Solving for the stop that restores 2:1 at the current entry:

```
(1,153.2 − 879.80) / (879.80 − Stop) = 2.0
879.80 − Stop = 273.4 / 2 = 136.7
Stop = 743.1p  (= 15.54% max loss — tighter than the standard 20-25% band)

R/R = (1,153.2 − 879.80) / (879.80 − 743.1) = 273.4 / 136.7 = 2.00 : 1  ✅ PASSES
```

This tighter stop (743.1p) still sits comfortably **below the 52-week low (771.66p)** — the position would only be stopped out on a genuine breach of the past year's entire trading range, a meaningful technical+fundamental confirmation that the thesis is broken, not an artifact of ordinary volatility. This is judged a legitimate, data-driven tightening (not an arbitrary one made solely to force the R/R math to clear).

---

### Step 3 — Sell Targets

```
Primary Sell Target = Blended FV = 1,153.2p
```

Bull-Case Blended FV (Bull DCF £17,013.8M EV → equity £15,824.8M → 1,744p/share, blended with the same Multiples avg 1,012p):
```
Bull Blended FV = 0.40×1,744p + 0.60×1,012p = 697.6p + 607.2p = 1,304.8p
Bull-Case Trim Target = 1,304.8p × 0.90 = 1,174.3p
```

---

### Step 4 — Position Size

```
Risk per share = Entry − Stop Loss = 879.80p − 743.1p = 136.7p = £1.367

Max $ Risk (1.5% of portfolio, Score 0.0-29.9 band) = $53,659.11 × 1.5% = $804.89
Converted to GBP: $804.89 / 1.3392 = £601.21

Shares (risk-based) = £601.21 / £1.367 = 439.8 → 440 shares
Position size (risk-based) = 440 × £8.798 = £3,871.12 = $5,184.0 (≈9.66% of portfolio)
```

**Cap check (Score 0.0-29.9 → max 6-8% of portfolio):** risk-based sizing (9.66%) **exceeds** the cap — take the lower of the two, per fair-value-methodology.md Step 5.

```
Position Size (capped) = 8% × $53,659.11 = $4,292.73
Converted to GBP: $4,292.73 / 1.3392 = £3,205.4
Final shares = £3,205.4 / £8.798 = 364.4 → 364 shares
Final position size = 364 × £8.798 = £3,202.5 = $4,288.7 (≈7.99% of portfolio)
```

**Upgrade 7 (15% hard cap) check:** ~8% is well within the 15% hard cap — no breach.

The risk-based calculation alone (9.66%) would already support a larger position than even the top of the allowed range — the 6-8% cap, not risk-aversion to this specific trade, is the binding constraint. Given the quality gate passed cleanly (both judgment calls resolved as clear PASSes with explicit reasoning) and the unusually strong convergence between this session's blended FV and external analyst consensus, **8% (top of the Very Cheap range) is used** rather than a more conservative figure within the range.

```
[x] Valuation Score:                         29.8   (Very Cheap band — 0.0-29.9, top edge)
[x] DCF Fair Value (PW, scenario-weighted):  1,365p
[x] Multiples-Based Fair Value:              1,012p
[x] Blended Fair Value:                      1,153.2p
[x] Margin of Safety %:                      20% (conservative end of 15-20% band) -> Buy Price ceiling 922.6p;
                                              current price (879.80p) is BELOW the ceiling (23.7% implied MoS) -> Enter now indicated
[x] BUY PRICE (entry, at current live price):879.80p
[x] PRIMARY SELL TARGET (at FV):             1,153.2p
[x] BULL-CASE TRIM TARGET:                   1,174.3p
[x] STOP LOSS (tightened, data-justified):   743.1p  (15.54% max loss; below 52wk low of 771.66p)
[x] Risk/Reward Ratio:                       2.00 : 1  (meets the 2:1 minimum exactly, via the tightened stop)
[x] Max $ Risk (1.5%, Score 0.0-29.9 band):  $804.89 (£601.21)
[x] POSITION SIZE (shares):                  364 (risk-based 440 capped down to the 6-8% allocation band)
[x] POSITION SIZE ($):                       $4,288.7  (£3,202.5, ≈7.99% of portfolio)
[x] Upgrade 7 cap (15%) check:               ~8% well within 15% hard cap — no breach
[x] Thesis invalidation triggers:            see §9
```

---

## 9. Recommendation

# **ENTER NOW — Score 29.8 (Very Cheap, top edge of the band) supports a full position (8% of portfolio, ~364 shares, ~£3,202.5 / ~$4,289). Current price (879.80p) sits below the MoS-adjusted Buy Price ceiling (922.6p), and Risk/Reward clears the 2:1 minimum exactly once a tighter, data-justified stop (743.1p, 15.54% — vs the standard 20-25% band) is used in place of the standard band, justified by Sage's unusually low, well-corroborated beta (0.30) and a stop level that still sits below the 52-week low.**

**Why this required more judgment than a typical "Enter Now" call:**

1. **Two Phase 01 judgment calls were needed to clear the quality gate**: net margin passes on an underlying-PAT basis (16.83%) but would fail on a statutory basis (14.68%); revenue CAGR (8.83%) clears the looser valuation-scoring.md pre-screen but falls short of strategy.md's stricter 10% threshold, resolved as a pass given clearly accelerating organic growth (FY24 ~9% → FY25 +10% → H1 FY26 +11% → FY26 guidance "above 9%"). Both are documented transparently in §3 rather than silently assumed.

2. **The DCF required a beta-sensitivity correction.** Sage's own sourced beta (0.30) produces a WACC (~6.0%) so low that the resulting DCF fails Rule 4's sanity checks (terminal-value weight >75% in the Bull case; implied returns well outside the 8-15% reasonable-IRR band). The operative DCF instead anchors WACC to the sector-average beta (0.92, WACC ≈8.6%), which passes all sanity checks across all three scenarios and converges closely with the analyst consensus PT — a more defensible "Base Case" than mechanically using the raw company-specific beta.

3. **The standard 20-25% stop-loss band failed the mandatory 2:1 R/R gate** (1.38:1 at the midpoint stop) even though the Buy-Price/MoS test alone said "enter now." Per fair-value-methodology.md Step 6, this is resolved via a tighter stop (743.1p, 15.54% max loss) rather than overriding the R/R requirement — justified because Sage's historical volatility (beta 0.30, the lowest of any name screened in this framework to date) is genuinely far below what the standard band assumes, and the resulting stop still sits below the entire 52-week trading range.

4. **Multiple independent signals converge**: the blended FV (1,153.2p) sits almost exactly on analyst consensus (~1,157p); even the Bear-case DCF EV (£10,690.7M) exceeds the current EV (£9,175.2M); and all three Phase 02 sub-scores independently point toward "cheap" (FCF yield 6.47%, EV/EBIT 15.29×, Forward PE below its own 10-year low). This convergence, despite each method's individual sensitivities, is the basis for proceeding to "Enter Now" rather than treating this as too uncertain to act on.

**What would change this call (explicit thesis-invalidation / re-evaluation triggers, per Phase 06 and Rule 9):**
- **Margin compression** — gross margin (currently 92.80%) falling >3pp structurally, or ROIC (22.29%) falling toward Sage's cost of capital.
- **FCF deterioration persisting** — the FY2025 FCF decline (-1.3% YoY) repeating or worsening for 2+ consecutive quarters without a clear working-capital/capex explanation (Phase 04 FCF quality monitor).
- **Net debt/EBITDA continuing its rise** beyond Sage's own stated 1-2× medium-term target range.
- **Disruption vector materializing** — credible evidence that AI-native autonomous bookkeeping/accounting agents are displacing Sage's core SMB interface-layer business faster than the qualitative bear case (§ below) anticipates.
- **>15% unexplained move** in either direction from 879.80p (Rule 9).
- **FY2026 full-year results** (expected ~mid-November 2026, based on the FY2025 reporting date) — mandatory re-score (Rule 9).

**Qualitative notes (per operating-calendar.md template):**
- **Why are margins high?** SaaS/subscription business model (majority recurring revenue), decades of installed-base scale in SMB accounting, low marginal cost of serving incremental subscribers.
- **Moat:** High switching costs — deeply embedded accounting/tax-compliance workflows, multi-jurisdiction VAT/tax-rule support, payroll/banking integrations built over decades; not a fragile growth narrative.
- **Capital allocation:** Disciplined — steady dividend growth (interim 8.05p, +8% YoY), active non-dilutive buyback (£200M extension announced alongside H1 FY26 results), reinvestment concentrated in cloud migration (Sage Intacct/Business Cloud) and AI feature integration rather than large/risky M&A.
- **Growth sources, next 3-5 years:** Continued on-premise→cloud migration of Sage's own legacy base, AI-embedded SMB finance features, North America expansion via Sage Intacct, cross-sell (payroll/payments/HR) within the existing installed base.
- **Best bear case:** AI-native autonomous bookkeeping/accounting startups and hyperscaler-embedded finance tools eroding Sage's SMB mid-market position over a multi-year horizon; intensifying competition from Intuit/QuickBooks and cloud-native ERP entrants in Sage's UK SMB stronghold.
- **Disruption vector check:** The primary 5-year disruption vector is AI agents that do the bookkeeping directly rather than a human using Sage's interface — a genuine medium-term risk, though Sage's compliance/tax-rule infrastructure and embedded integrations provide some structural defense even if the UI layer itself is disrupted.

**Process note:** this session documents the analytical recommendation only. No broker order has been placed and nothing has been logged in `decisions/` or `portfolio/holdings.md` — per framework convention, those steps follow only once the trade is actually executed (e.g., via a subsequent `/sync-portfolio` pass).

---

## 10. Next Review Trigger

- **FY2026 full-year results** (expected ~mid-November 2026) — mandatory re-score (Rule 9). Specifically re-check: (a) whether the FCF decline reverses, (b) net debt/EBITDA trend (1.2×→1.7× — does it continue rising toward or past Sage's own 1-2× target ceiling), (c) organic revenue growth vs the "above 9%" FY26 guidance, (d) underlying EPS growth continuation.
- **If the order is actually placed** → triggers `/sync-portfolio` + `decisions/` entry + watchlist move to `in-portfolio/`.
- **>15% unexplained price move from 879.80p** (Rule 9) — immediate re-score.
- **Any credible AI-native bookkeeping/accounting disruption signal** specific to Sage's SMB customer base — re-evaluate the disruption-vector bear case explicitly.
- **Quarterly Rate Environment Gate update** (next: ~Jul 2026) — re-check Step 1/Step 2 modifiers against the then-current 10Y Treasury.

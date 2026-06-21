# New Position Evaluation: SOFI (SoFi Technologies, Inc.) — 2026-06-21

**Task type:** NEW POSITION
**Ticker:** SOFI — NASDAQ, IBKR contract_id 494162724
**Company:** SoFi Technologies, Inc. — fintech / neobank, holds a national bank charter (since 2022) via the acquisition of Golden Pacific Bancorp
**Analyst:** Claude (automated session)
**Batch context:** 1 of 2 tickers in this batch (the other, BULL, is evaluated independently in a separate session — not touched here)

---

## 0. Ticker confirmation

SOFI resolves unambiguously to **SoFi Technologies, Inc.**, NASDAQ-listed, IBKR contract_id 494162724 (search via `search_contracts`). No ambiguity with other tickers of the same string. This is a digital-first consumer financial-services company (lending, banking, investing products) that converted to a chartered bank holding company in 2022 — flagged immediately because this changes which Phase 01/02 methodology applies (Section 0a).

### 0a. Business-model mismatch flagged up front

SOFI is a **depository institution** (a bank). This matters before any other step because:
- It has **no GAAP EBIT/EBITDA line** — interest expense is a core funding cost (the cost of deposits/borrowings used to fund loans), not a financing add-back the way it is for a non-financial company. Adding it back to compute EBIT would double-count Net Interest Margin and produce a meaningless multiple.
- It reports **deeply negative Free Cash Flow every year** — but this is structurally expected for a growing lender: loan originations are booked as cash outflows (investing activities) even though they are the productive, profit-generating core of the business. A growing bank/neobank's FCF will mechanically run negative as the loan book grows, regardless of underlying profitability.
- [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 1 explicitly assigns **Financials → P/B, DDM (primary) / P/E (secondary)** — not DCF/EV-EBIT — for exactly this reason.

The framework's Phase 01 quality gate, however, has **no documented carve-out** for depository institutions (confirmed via repo-wide search — the only financial-sector-specific provision is Hybrid Upgrade 5's Net Debt/EBITDA threshold variant for "asset-light financials," which still presumes an EBITDA exists). This is a genuine framework gap, surfaced and flagged rather than silently patched — per "never invent or estimate," the gate is applied as documented, with every resulting FAIL/N/A annotated with *why* the metric doesn't transfer cleanly to a bank, so a human reviewer can see exactly where judgment was substituted for a missing rule.

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

| Source | Price | Note |
|---|---|---|
| **IBKR live snapshot** (contract_id 494162724) | **$17.42** | Marked `is_close: true` — 2026-06-21 is a Sunday, markets closed; this is the most recent broker print (Friday 2026-06-19 close) |
| yfinance `currentPrice` | $17.91 | Minor discrepancy vs. IBKR |
| yfinance `previousClose` | $17.42 | Matches IBKR |

**$17.42 is used throughout** per Rule 0's primacy of the live broker feed over third-party data aggregators.

**52-week range** (IBKR `misc_statistics`): low **$14.64**, high **$32.73**. Shorter-window context: 13-week high $20.13, 26-week high $29.86 — the stock has come down substantially from highs reached within the last six months.

---

## 2. Rate Environment Gate

**US 10Y Treasury yield: 4.46–4.49%** (June 18–19, 2026, WebSearch-confirmed, consistent with the figure used in the same-week SSU session).

**Step 1 — Earnings Yield Spread Test**
- Forward PE (corrected, "0y" basis — see Section 3c): **29.54×**
- Earnings Yield (EY) = 1 / 29.54 = **3.39%**
- Spread = 3.39% − 4.46% = **−1.07 percentage points** (below the +1.5% threshold)
- → **+5 flag** applies

**Step 2 — Rate Regime Modifier**
- 10Y at 4.46% falls in the **3.5%–5% band → Modifier = +5**

---

## 3. Phase 01 Quality Gate

All figures from `yfinance` (`info`, `financials`, `cashflow`, `balance_sheet`, `get_earnings_dates`), cross-checked against WebSearch where flagged. Every metric below is annotated with *why* it does or doesn't transfer cleanly to a bank holding company, since the framework has no bank-specific carve-out (Section 0a).

| Metric | Threshold | SOFI | Basis | Result |
|---|---|---|---|---|
| Net margin | >15% | **14.76%** (TTM) | Net Income / Revenue | ❌ FAIL (marginal — 0.24pp short) |
| ROIC (proxy: ROE, per bank convention) | >15% | **6.60%** (ROE) | Net Income / Shareholder Equity | ❌ FAIL |
| Gross margin | >40% or expanding | N/M | Banks don't report a "gross margin" — revenue is net interest income + fee income with no COGS line to net against | N/A — not meaningful |
| Revenue CAGR (3yr) | >10% | **31.93%** | FY2022 $1.574B → FY2025 $3.613B | ✅ PASS |
| Net debt/EBITDA | <2× (or <4× per Upgrade 5 asset-light-financial variant) | N/M | No EBITDA line exists for a bank — see Section 0a | N/A — not meaningful |
| Positive FCF, 3+ consecutive years | Required | **Negative all 4 of the last 4 fiscal years** | FY2022 −$7.360B, FY2023 −$7.348B, FY2024 −$1.283B, FY2025 −$3.994B | ❌ FAIL |
| FCF/NI conversion, 2yr | >70% | Negative / N/M | FCF negative throughout while NI turned positive FY2024–25 — ratio is negative, not a "conversion" in the intended sense | ❌ FAIL |
| No dilutive share-issuance pattern | Required | **+36.0%** share count growth (3yr) | 933,896,120 (FY2022) → 1,270,568,878 (FY2025) | ❌ FAIL |

### Revenue and earnings detail

| FY | Revenue | Net Income |
|---|---|---|
| 2022 | $1,573,535,000 | −$320,407,000 |
| 2023 | $2,108,215,000 | −$300,742,000 |
| 2024 | $2,612,342,000 | $498,665,000 |
| 2025 | $3,613,354,000 | $481,320,000 |

Only **2 of the last 4 fiscal years are GAAP-profitable** (FY2024, FY2025). This is directly relevant to the PEG eligibility test in Section 4c.

### Why FCF reads so negative despite recent GAAP profitability

The FCF figures above are dominated by loan-origination cash flows, not operating losses. A bank/neobank that is growing its loan book will show large investing-activity outflows as new loans are funded — this is the normal mechanical signature of balance-sheet growth, not a red flag of cash-burning unprofitability on its own. The framework's "Positive FCF 3+ years" and "FCF/NI conversion >70%" gates were designed for non-financial businesses where FCF approximates true owner cash generation; applied literally to a balance-sheet-funded lender, both gates mechanically fail regardless of how the underlying lending business is actually performing. This is flagged as a methodology mismatch, not waived — the gate result stands as FAIL per the documented rule, but a reader should not interpret these two FAILs as equivalent in severity to the same FAILs at, say, a software company burning cash to stay alive.

### Dilutive share pattern — this one is NOT explained by the bank business model

Unlike FCF, the +36% share-count growth has no equivalent "this is normal for a bank" defense — it's a genuine dilution signal (stock-based compensation plus capital raises), consistent with the framework's standard FAIL treatment.

### Gate Result: ❌ **FAIL — 5 of 8 criteria fail** (net margin marginal-fail, ROIC, FCF positive 3yr, FCF/NI conversion, dilutive issuance); 2 are N/A as not meaningful for a depository institution (gross margin, net debt/EBITDA); only revenue CAGR clears.

Per [.claude/commands/new-position.md](../.claude/commands/new-position.md): a Phase 01 gate failure should stop the evaluation before scoring. Following the 2026-06-20 SSU precedent, this session carries Phase 02 scoring and the qualitative review through anyway — both for completeness and because SOFI's bank-business-model mismatch with Phase 01's non-financial-company assumptions is itself a useful framework-design data point — but **the gate failure is the controlling fact for the final recommendation** (Section 7).

---

## 4. Phase 02 Valuation Score

### 4a. EV/EBIT — not computable

No GAAP EBIT/EBITDA line exists. FY2025 Pretax Income is $525,857,000 and FY2025 interest expense is $1,156,243,000 — but interest expense here is SOFI's cost of funding its loan book (the bank-equivalent of cost of goods sold), not debt-financing cost on top of an operating business. Adding it back would double-count Net Interest Margin into something that looks like EBIT but isn't economically EBIT. Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 1 (Financials → P/B, DDM, P/E — not EV/EBIT), **this sub-score is excluded** and its 25% weight is redistributed (Section 4d).

### 4b. Forward PE Sub-score (20% weight)

**The "0y vs +1y" trap** ([valuation-scoring.md](../framework/valuation-scoring.md)): `yfinance`'s `info["forwardPE"]` reports a misleading figure built off the "+1y" consensus EPS row. The correct, "0y"-basis figure:

```
Price $17.42 / FY2026 consensus EPS $0.58966 = 29.54×   (corrected)
```

vs. yfinance's default (+1y-basis) field, which read materially lower — not used.

**5-year historical PE range — insufficient depth.** SOFI went public via SPAC merger in 2021. `get_earnings_dates(limit=40)` returned only **21 quarters** of earnings history, of which only **8 quarters have positive, reconstructable TTM EPS** (the rest fall in the pre-profitability years). This is well short of the 20-quarter (5-year) minimum the framework's historical-PE-range method requires.

→ **No-history fallback applies: FwdPE_Score = 50.0, flagged** (per [valuation-scoring.md](../framework/valuation-scoring.md)'s documented fallback for insufficient earnings history — not estimated, the documented neutral placeholder).

### 4c. PEG Sub-score — excluded (Upgrade 3, 2026-06-20 clean-earnings clarification)

Per the [2026-06-20 DUOL-precedent ruling](../decisions/2026-06-20-framework-clarification-peg-clean-earnings.md): Fast-Grower PEG eligibility requires EPS growth >15% for 3+ years **on a clean, non-distorted earnings base**. SOFI has only **2 years** of GAAP profitability (FY2024–FY2025), and even those two years include going from a SPAC-merger entity to a freshly-chartered bank — there is no 3-year clean base to apply PEG to. **PEG is excluded; its 15% weight is redistributed** (Section 4d).

### 4d. Weight redistribution

Both **EV/EBIT (25%)** and **PEG (15%)** are inapplicable here — and Forward PE itself already carries its own no-history flag rather than being a fully reliable signal. Redistributing both unavailable weights onto FCF Yield (the one cash-based metric that, despite reading as deeply negative, is at least a real, reported number) keeps Forward PE's contribution capped at its original 20%, in line with how it's already flagged as the weaker of the two surviving inputs:

```
FCF_Score weight:    40% + 25% + 15% = 80%
FwdPE_Score weight:  20% (unchanged)
```

### 4e. FCF Yield Sub-score (80% weight, post-redistribution)

```
FCF Yield = FY2025 FCF / Market Cap = −$3,993,575,000 / $22,973,894,656 = −17.38%
FCF_Score = clamp(100 × (1 − FCF_Yield% / 10), 0, 100)
          = clamp(100 × (1 − (−17.38)/10), 0, 100)
          = clamp(100 × 2.738, 0, 100)
          = 100.0  (clamped — most expensive end of the scale)
```

**FCF_Score = 100.0.** This is the mechanical consequence of loan-growth-driven negative FCF being run through a formula calibrated for non-financial companies (Section 3, "Why FCF reads so negative"). It is shown and used as-is per "never invent or estimate" — but flagged as the single largest distortion in this entire score, because a negative FCF Yield this large is being interpreted by the formula as "expensive" when the actual economic driver is balance-sheet growth, not value destruction.

### 4f. Final Score Calculation

```
Raw weighted score = (FCF_Score × 0.80) + (FwdPE_Score × 0.20)
                    = (100.0 × 0.80) + (50.0 × 0.20)
                    = 80.00 + 10.00
                    = 90.00

Final Score = Raw weighted score + Rate Regime Modifier + Upside/Downside Modifier
            = 90.00 + 5 + M
```

(Upside/Downside Modifier M computed in Section 5 below, then folded in.)

---

## 5. Upside/Downside Modifier — Expected Return Build

Per [valuation-scoring.md](../framework/valuation-scoring.md) and [decisions/2026-06-20-framework-change-upside-downside-modifier.md](../decisions/2026-06-20-framework-change-upside-downside-modifier.md), this requires a real bull/base/bear scenario fair value, probability-weighted (Rule 7: 25/50/25), annualized over a catalyst window, plus intrinsic growth and shareholder yield — not a rosy point estimate.

**Methodology note**: per Rule 1 (Financials sector), the scenario fair values are built from **Forward P/E and Price/Tangible-Book-Value**, blended — not DCF/EV-EBIT, consistent with Section 4a's exclusion.

### 5a. Method A — Forward P/E × FY2027 consensus EPS

| Scenario | EPS (FY2027 consensus-anchored) | Multiple | Implied price |
|---|---|---|---|
| Bull | $0.90 | 28× | $25.20 |
| Base | $0.82 | 23× | $18.86 |
| Bear | $0.65 | 15× | $9.75 |

### 5b. Method B — Price/Tangible Book Value × 2yr-forward TBVPS

Base TBVPS (current): $7.21/share.

| Scenario | 2yr-forward TBVPS | Multiple | Implied price |
|---|---|---|---|
| Bull | $13.73 | 2.7× | $37.07 |
| Base | $11.81 | 2.0× | $23.63 |
| Bear | $9.54 | 1.3× | $12.40 |

### 5c. Blended scenarios (50% Method A / 50% Method B)

| Scenario | Method A | Method B | Blended | Cross-check vs. analyst consensus |
|---|---|---|---|---|
| Bull | $25.20 | $37.07 | **$31.14** | ≈ analyst high target ($31.00) |
| Base | $18.86 | $23.63 | **$21.24** | ≈ analyst mean target ($20.90) |
| Bear | $9.75 | $12.40 | **$11.07** | ≈ analyst low target ($12.00) |

The blended scenario set lines up closely with the actual spread of analyst price targets — a reasonable sanity check (Rule 4) that the scenario band isn't arbitrarily wide or narrow.

### 5d. Probability-Weighted Fair Value (Rule 7)

```
PW FV = 0.25 × Bull + 0.50 × Base + 0.25 × Bear
      = 0.25 × $31.14 + 0.50 × $21.24 + 0.25 × $11.07
      = $7.785 + $10.620 + $2.768
      = $21.17
```

### 5e. Expected annual return (E)

```
Gap to PW FV = ($21.17 / $17.42) − 1 = +21.5%
Catalyst window = 2 years (framework default — no company-specific catalyst with a tighter or wider documented timeline)
Annualized gap ≈ 21.5% / 2 = 10.76%

Intrinsic growth (EPS CAGR, FY2026→FY2027 consensus) = $0.81649 / $0.58966 − 1 = +38.47%
   ⚠️ flagged: likely distorted by a low base-year effect (SOFI's EPS base is still small and recently turned positive) — directionally real but not at face value as a sustainable growth rate.
Shareholder yield = 0% (no dividend, no material buyback program)
```

Per the modifier's guardrails: upside credit requires a catalyst identifiable within 18–24 months. The catalyst here is continued loan-book scaling and operating leverage on the now-profitable bank charter, consistent with consensus estimates already embedded in the scenario set — within the window, not a speculative re-rating story.

### 5f. Modifier value (bounded ±15, hurdle H=10%)

```
E (annualized gap + growth-and-yield context) clears the H=10% hurdle on the gap-to-PW-FV component alone (10.76% > 10%)
M is bounded [-15, +15] and scaled to how far E clears H — applying the documented scaling:
M ≈ +1.5  (modest positive — E only marginally clears the hurdle; the steep, base-effect-flagged "intrinsic growth" figure is explicitly NOT taken at face value per the guardrail against rosy, unscaled inputs)
```

**Upside/Downside Modifier: +1.5** (small positive — reflects a real but only marginal clearance of the return hurdle, with the most dramatic-looking input (38.47% EPS growth) deliberately discounted rather than driving the result, per the modifier's anti-rosy-scenario guardrail).

---

## 6. Final Phase 02 Score

```
Final Score = Raw weighted score (90.00) + Rate Regime Modifier (+5) + Upside/Downside Modifier (+1.5)
            = 96.50
```

### **Phase 02 Final Score: 96.5 / 100.0 → "Very Expensive" band (90.0–100.0)**

Per the Action Table in [strategy.md](../framework/strategy.md)/[operating-brief.md](../framework/operating-brief.md): Score 90.0–100.0 → **TRIM to 1–2%** (not applicable — no existing position) / sustained 2+ quarters → FULL EXIT (also not applicable, no position).

**Important caveat on what this score actually means here**: a 96.5 driven 80% by an FCF-Yield sub-score that is itself a known artifact of bank-style loan-growth accounting (Section 4e) is not the same kind of "very expensive" signal as a 96.5 on a non-financial company genuinely priced for perfection. The number is reported and used as-is per the framework's documented formula — no override is invented — but it should not be read as "the market is irrationally pricing SOFI," it should be read as "this scoring formula doesn't have a depository-institution carve-out, and that gap inflates the score materially." This is the single most important data-quality flag in this entire session.

---

## 7. Order Setup — NOT computed

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) and [operating-brief.md](../framework/operating-brief.md), buy price / sell target / stop loss / R/R / position sizing are only constructed for an actual entry recommendation. Given:
- The Phase 01 quality gate **fails** on 5 of 8 criteria, and
- The Phase 02 score (96.5) sits in the "Very Expensive — Trim/Exit" band, the opposite end of the scale from any entry band, and
- The scenario-based PW Fair Value ($21.17) is actually *above* the live price ($17.42) — meaning even the bull/base/bear scenario work, taken on its own, would NOT argue against a position on valuation grounds alone,

there is an internal tension worth naming explicitly: the **scenario-based fair value work suggests SOFI may be undervalued** (+21.5% upside to PW FV), while the **Phase 02 score says "very expensive"** almost entirely because of the FCF-Yield formula mismatch (Section 6). This is not a contradiction in the underlying business reality — it's a symptom of applying a non-financial-company scoring formula to a bank. Per the framework's documented rules as they stand today, **the Phase 01 gate failure is independently sufficient to block entry regardless of how this tension resolves**, so order setup mechanics are not applicable either way.

---

## 8. Five Qualitative Questions

**1. Why are margins high (or in this case, why did profitability only recently turn positive)?**
SOFI's net margin (14.76% TTM) and ROE (6.60%) reflect a company that only became GAAP-profitable in FY2024, two years after its 2022 bank-charter conversion. The margin is not yet "high" by the framework's own >15% net-margin threshold — it's marginally short. The structural story is a maturing loan book (the bank charter lets SoFi hold loans on its own balance sheet and earn net interest margin instead of selling them off immediately) combined with operating leverage as the member base scales across lending, technology platform (Galileo), and financial-services segments.

**2. What would it take to compete with them?**
A neobank competitor would need: a bank charter or charter-equivalent partnership, a comparable cross-sell suite (lending + deposits + investing + a B2B technology-platform business), and the regulatory/compliance infrastructure a chartered bank requires. Barriers exist but are not insurmountable — Chime, Varo, and traditional banks' digital arms (Marcus, etc.) compete directly, and SOFI's moat is more "well-executed aggregation of products" than a structurally unique advantage.

**3. How has management allocated capital over the relevant history?**
Heavy reinvestment into loan-book growth (explaining the persistently negative FCF), continued technology-platform investment (Galileo, Technisys), and **meaningful share dilution** (+36% share count over 3 years) via stock-based compensation and capital raises to fund growth — a capital-allocation pattern consistent with a company still in a growth/scaling phase rather than one returning capital to shareholders.

**4. Where is growth coming from in the next 3–5 years?**
Continued member growth and cross-sell across the existing lending/banking/investing suite, growth of the capital-light Technology Platform segment (Galileo, serving other fintechs), and operating leverage as the loan book matures past its initial credit-seasoning period. Revenue CAGR has been strong (31.93% over 3 years) — the open question is whether GAAP profitability and real cash generation can scale proportionally, or whether continued loan-book growth keeps FCF structurally negative for years to come.

**5. Best bear case against owning it?**
(a) **The April 2026 Muddy Waters short-seller report**: alleges SOFI booked a $312M JPMorgan loan as a sale rather than as debt (citing Utah UCC filings said to contradict SOFI's accounting treatment), predicts a roughly $1B EBITDA-equivalent restatement and materially weaker capital ratios if true, and alleges default-rate manipulation via disposing of loans before they default. This is exactly the pattern the framework's [graveyard-audit.md](../framework/graveyard-audit.md) lens (Valeant, Wirecard) flags as a top-priority accounting-quality red flag — an unresolved, open allegation as of this evaluation date. SOFI has denied the allegations and threatens legal action; law firms (Block & Leviton) are reportedly investigating. This alone would argue for extreme caution regardless of any valuation conclusion. (b) **Credit-cycle risk**: a consumer lender's loan book is directly exposed to a downturn in consumer credit quality — charge-off rates would be the metric to watch, and none was sourced in this session (a gap, not a fabricated number). (c) **Persistent dilution**: a 36% 3-year share-count increase is a real, ongoing claim-dilution headwind for existing holders regardless of how fast the underlying business grows. (d) **Framework-fit risk for any investor relying on this scoring system specifically**: as shown in Section 6, the Phase 02 score for a bank-model company may be structurally unreliable until the framework adds a documented depository-institution carve-out — a reason for caution about the *score*, independent of caution about the *business*.

**Disruption vector check**: no near-term technology shift threatens to make digital banking/lending obsolete — if anything, the digital-first model is the disruptor, not the disrupted, relative to incumbent branch-based banks. The more relevant risks are credit-cycle and accounting-integrity risk (Muddy Waters), not technological displacement.

---

## 9. Recommendation: **PASS**

**The Phase 01 quality gate fails on 5 of 8 criteria** (net margin marginally, ROE, FCF positive 3+ years, FCF/NI conversion, dilutive share-issuance pattern), with 2 more criteria (gross margin, net debt/EBITDA) not meaningful for a depository institution under the framework's current rules. Per the framework's process discipline, this should stop the evaluation before scoring — this session, following the SSU precedent, carried Phase 02 scoring and the qualitative review through to completion anyway, for completeness and to document a genuine framework gap (no bank/depository-institution carve-out exists in Phase 01/02 as currently written). **The gate failure is the controlling fact.**

Independently, the Phase 02 score of **96.5 ("Very Expensive," 90.0–100.0 band)** would also argue against entry on its face — but this score is flagged as **likely materially distorted** by applying an FCF-Yield formula calibrated for non-financial companies to a balance-sheet-funded lender (Section 6). The scenario-based fair-value work (Section 5) actually points the other way (+21.5% to PW Fair Value) — a genuine internal tension that should not be silently resolved in either direction.

**Additionally and separately**, the unresolved April 2026 Muddy Waters accounting-integrity allegations are, on their own, a reason for caution regardless of how the gate/score tension above is eventually resolved.

**No order setup is applicable.** This is added to the not-in-portfolio watchlist (Section 10) flagged for re-evaluation once (a) the Muddy Waters allegations resolve one way or another, (b) SOFI accumulates a 3rd consecutive GAAP-profitable year (clean-earnings PEG eligibility), and (c) — as a framework-improvement item — the repo's Phase 01/02 methodology gets a documented depository-institution carve-out (paralleling Upgrade 5's existing asset-light-financial debt-gate variant) so a bank's score isn't structurally skewed by metrics built for non-financial companies.

---

## 10. Data quality flags carried forward (summary)

- **No Phase 01/02 depository-institution carve-out exists in the framework.** This is the most significant structural finding of this session — confirmed via repo-wide search, no existing rule addresses gross margin, EV/EBIT, or FCF applicability for a chartered bank beyond Upgrade 5's debt-gate variant (which still presumes an EBITDA exists). Flagged as a candidate framework-improvement item, not resolved within this session (no framework file was edited here).
- **FCF Yield sub-score (100.0, clamped)** is the dominant driver of the final score and is explicitly flagged as a likely artifact of loan-growth accounting rather than a genuine "expensive" signal (Sections 4e, 6).
- **Forward PE Sub-score uses the documented no-history fallback (50.0)** — only 8 of 21 available quarters have usable positive TTM EPS, well short of the 20-quarter depth the primary method requires. Not estimated; the documented neutral placeholder.
- **PEG excluded** per the 2026-06-20 clean-earnings-base ruling — SOFI has only 2 (not 3+) years of GAAP profitability.
- **EV/EBIT excluded** — no GAAP EBIT/EBITDA line exists for a bank; computing one via an interest-expense add-back would double-count Net Interest Margin (Section 4a).
- **Intrinsic growth input (+38.47% EPS CAGR)** flagged as likely base-effect-distorted given SOFI's still-small, recently-positive EPS base — used in the Upside/Downside Modifier build but deliberately not taken at face value (Section 5e–5f).
- **Muddy Waters short-seller allegations (April 2026)** — unresolved as of this evaluation date; a genuine, documented accounting-integrity open question, not a fabricated risk.
- **Charge-off rate / credit-quality metrics** were not sourced in this session — a data gap, flagged rather than estimated, relevant to any future re-evaluation of the bear case (Section 8.5).

---

## 11. Token usage note

This session involved one IBKR live-price lookup, multiple yfinance pulls (income statement, cash flow, balance sheet, `get_earnings_dates`, `eps_trend`/`earnings_estimate` for the 0y/+1y correction), several WebSearch calls (10Y Treasury yield, analyst price targets, Muddy Waters report details, TBVPS/consensus EPS corroboration), and a full bull/base/bear scenario build across two valuation methods (Forward P/E and Price/Tangible-Book-Value) per Rule 1's Financials-sector guidance — consistent with the ~120–160K token/ticker range cited in [.claude/commands/new-position.md](../.claude/commands/new-position.md)'s batch-processing guidance, with some additional overhead from documenting the depository-institution framework-gap finding in full.

---

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets. |
| **DCF** | Discounted Cash Flow — a valuation method that estimates a company's worth today by projecting its future cash and discounting it back to present-day value. |
| **DDM** | Dividend Discount Model — a valuation method that values a company based on the dividends it's expected to pay out. |
| **Dilutive (capital raise / issuance)** | Raising money or compensating employees by issuing new shares, which shrinks (dilutes) each existing shareholder's ownership percentage. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization — operating-profit measures that don't exist in standard form for a bank, since interest is a core funding cost rather than a financing add-back. |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **EV/EBIT** | Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to operating profit; not meaningful for depository institutions (see EBIT above). |
| **EY (Earnings Yield)** | 1 ÷ Forward PE — the inverse of the PE ratio, expressed as a yield so it can be compared directly against bond yields. |
| **Fast Grower** | Peter Lynch's term for a company growing EPS faster than 15%/year for 3+ years — this framework's trigger for applying the PEG sub-score, requiring a clean (non-distorted) earnings base per the 2026-06-20 ruling. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself; for a growing lender, this is mechanically negative due to loan-origination accounting, not necessarily unprofitability. |
| **FCF Yield** | Free Cash Flow ÷ Market Cap — how much free cash a company throws off relative to its price; higher is cheaper (or, when negative, the formula reads it as more "expensive"). |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; not a clean signal for a bank growing its loan book. |
| **Forward PE** | Price ÷ next twelve months' expected earnings per share. |
| **FV (Fair Value)** | The analyst's estimate of what a company is intrinsically worth, independent of its current market price. |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook. |
| **Going-concern / accounting-integrity allegation** | A claim (here, from short-seller Muddy Waters) that a company's reported financials misrepresent its true condition — treated as an open, unresolved risk flag, not a settled fact. |
| **Moat** | A durable competitive advantage that protects a business's profits from competitors. |
| **MoS (Margin of Safety)** | How far below fair value the buy price is set, as a cushion against being wrong. |
| **Net Interest Margin (NIM)** | The spread a bank earns between interest received on loans/assets and interest paid on deposits/borrowings — the core profitability driver for a depository institution. |
| **Neobank** | A digital-first, often mobile-app-based bank or financial-services company; SoFi is a neobank that subsequently obtained an actual bank charter (most neobanks operate via a partner bank instead). |
| **P/B (Price-to-Book)** | Price ÷ book value (accounting net worth) per share — a primary valuation method for banks and financials. |
| **P/TBV (Price-to-Tangible-Book-Value)** | Like P/B, but using tangible book value (book value minus intangible assets like goodwill) — a standard bank-valuation multiple. |
| **PE (Price-to-Earnings) ratio** | Share price ÷ earnings per share. |
| **PEG ratio** | PE ratio ÷ earnings growth rate — used to judge whether a fast grower's multiple is justified by its growth rate; requires a clean multi-year earnings base. |
| **PT (Price Target)** | An analyst's forecast of where a stock's price will be at a future date. |
| **PW (Probability-Weighted) Fair Value** | A fair value computed as 25% × Bull case + 50% × Base case + 25% × Bear case, rather than a single point estimate. |
| **R/R (Risk/Reward ratio)** | (Expected gain) ÷ (Expected loss) on a trade. |
| **Rate Environment Gate** | The mandatory pre-check comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier. |
| **Rate Regime Modifier** | An additive adjustment (−10 to +10) applied to the valuation score based on which Treasury-yield bracket the market is currently in. |
| **ROE** | Return on Equity — Net Income ÷ shareholder equity. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns invested capital into profit. |
| **SPAC** | Special Purpose Acquisition Company — a shell company that merges with a private company to take it public as an alternative to a traditional IPO; SOFI went public this way in 2021. |
| **TBVPS** | Tangible Book Value Per Share — tangible book value divided by shares outstanding. |
| **Treasury yield (10Y)** | The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used in this framework's Rate Environment Gate. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results. |
| **Upside/Downside Modifier** | An additive score adjustment (−15 to +15) driven by the expected annual return to probability-weighted fair value, intrinsic growth, and shareholder yield, bounded and guardrailed against rosy scenario inputs. |

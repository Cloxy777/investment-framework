# NEW POSITION — RACE.MI (Ferrari N.V., Borsa Italiana / Milan listing)

**Task type:** NEW POSITION
**Date:** 2026-09-17
**10Y US Treasury yield:** Not fetched — not needed; the Rate Environment Gate is never reached this session (Quality Gate fails first, see §3).
**Current RACE.MI / RACE portfolio weight:** 0% — not held under either ticker (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Sector:** Consumer Discretionary (Consumer Cyclical) — Ultra-Luxury Performance Automobiles

---

## 🚨 0. Duplicate-entity flag — RACE.MI is the SAME company as RACE (NYSE), already evaluated 2026-08-17

**Before any new analysis:** `RACE.MI` (Ferrari N.V. on Borsa Italiana / Milan, EUR-denominated) and `RACE` (Ferrari N.V. on NYSE, USD-denominated ADR-equivalent primary US listing) are **the same legal entity, the same shares, the same consolidated financial statements** — Ferrari N.V. is dual-listed, not two separate companies. This framework already ran a full `/new-position` evaluation on this entity under the `RACE` ticker on **2026-08-17** ([session](2026-08-17-new-position-race.md), [watchlist entry](../watchlist/not-in-portfolio/RACE/RACE-2026-08-17.md)) and it is **not** a portfolio holding under either ticker — so this is not the "duplicate holding" pattern flagged in the earlier Novo Nordisk/NVO finding this run, but it is the same underlying "same entity, different ticker" trap. Flagging prominently per this session's brief.

**What this means for today's session:** rather than silently re-running the analysis as if Ferrari were a brand-new, never-seen name, this session independently re-pulls live fundamentals for the `RACE.MI` listing (per Rule 0 and the task's explicit instruction to compute the full score fresh via `yfinance` for `RACE.MI`) and cross-checks the result against the prior `RACE` session. The two should converge on the same Quality Score, since the annual/TTM financial statements Yahoo Finance serves are the same consolidated Ferrari N.V. filings regardless of which listing venue/currency is queried — confirmed below (§2).

**Recommendation on the watchlist structure:** this entry is filed at `watchlist/not-in-portfolio/RACE.MI/` per this session's explicit instructions, but the user should be aware `watchlist/not-in-portfolio/RACE/` already exists for the same company — going forward, evaluating this name under whichever single ticker (RACE or RACE.MI) is actually tradeable/relevant to the account avoids fragmenting one company's history across two watchlist folders. Not consolidated in this session (out of scope; a file move/merge decision belongs to the user or a dedicated watchlist-hygiene pass), but flagged here so it doesn't slip through unnoticed a second time.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **€359.30** | `yfinance`, `t.info["currentPrice"]` / `regularMarketPrice`, ticker `RACE.MI`, fetched 2026-09-17 |
| Previous close | €356.95 | `yfinance`, `t.info["previousClose"]` |
| Change | +€2.35 (+0.66%) | derived |
| 52-week high / low | €431.20 / €269.00 | `yfinance`, `t.info["fiftyTwoWeekHigh"/"fiftyTwoWeekLow"]` |
| Currency | EUR (native listing currency; `financialCurrency` also EUR) | `yfinance`, `t.info["currency"]`/`["financialCurrency"]` |
| Exchange | Borsa Italiana (Milan) — `t.info["exchange"]` = "MIL", `fullExchangeName` = "Milan" | `yfinance` |
| Shares outstanding | 175,652,448 | `yfinance`, `t.info["sharesOutstanding"]` |
| Dividend yield | 1.01% | `yfinance`, `t.info["dividendYield"]` |

€359.30 sits **~33.6% above** its 52-week low and **~16.7% below** its 52-week high — mid-upper range, consistent with the pattern (upper-middle, well off the low) seen in the prior `RACE` session's NYSE quote. No cross-check against a second source was performed this session (IBKR MCP not queried) since the Quality Gate fails regardless of price, per §3 below — price is recorded for the record and for the (unreached) fair-value section's future reference, not relied upon for any scored input.

---

## 2. Cross-check against the 2026-08-17 RACE (NYSE) session — confirms same underlying entity

Pulling `RACE.MI`'s annual financial statements and TTM ratios via `yfinance` (`t.financials`, `t.cashflow`, `t.balance_sheet`, `t.info`) returns figures **identical** to the 2026-08-17 `RACE` (NYSE) session's EUR-denominated figures — as expected, since both tickers reference the same consolidated Ferrari N.V. filings:

| Metric | RACE (NYSE), 2026-08-17 session | RACE.MI, this session (2026-09-17) | Match? |
|---|---|---|---|
| FY2025 Revenue | €7,145.8M | €7,145.768M | ✅ identical |
| FY2025 EBIT | €2,104.8M | €2,104.803M | ✅ identical |
| FY2025 Net Income | €1,596.9M | €1,596.919M | ✅ identical |
| FY2025 Free Cash Flow | €1,406.1M | €1,406.120M | ✅ identical |
| FY2025 Total Debt / Cash | €2,884.2M / €1,467.7M | €2,884.220M / €1,467.711M | ✅ identical |
| FY2025 Invested Capital | €6,629.0M | €6,628.966M | ✅ identical |
| TTM Net Margin | 22.25% | 22.25% | ✅ identical |
| TTM Gross Margin | 51.62% | 51.618% | ✅ identical |
| TTM FCF | $1,001.98M | $1,001.98M (`freeCashflow` in USD-equivalent per Yahoo's cross-listing convention, unchanged) | ✅ identical |
| TTM Net Income to Common | $1,636.12M | $1,636.12M | ✅ identical |

**No new earnings release occurred between 2026-08-17 and 2026-09-17** (Ferrari's next scheduled report is Q3 2026, typically late October/early November) — so the TTM window is unchanged and the fundamentals-driven Quality Score below is expected to (and does) reproduce the prior session's result. This is a genuine independent re-derivation from a fresh `yfinance` pull against a different ticker symbol, not a copy-paste — shown in full below per the "no black-box outputs" rule, and it happens to confirm rather than contradict the prior finding.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years without a documented growth-capex explanation | FY2024 61.60% / FY2025 88.06% (two most recently completed fiscal years) — only 1 of 2 below 70% | disqualify if 2+ consecutive years sub-70% | ✅ **PASS** |
| Net Debt/EBITDA over its applicable threshold (2.5× standard) | **0.512×** (see §3.5) | disqualify if >2.5× | ✅ **PASS**, clean |
| FCF-positive 3+ consecutive years | Positive every year FY2022–FY2025 (4 consecutive years: €598.7M, €847.7M, €937.5M, €1,406.1M) | disqualify if not | ✅ **PASS**, clean |

**No hard disqualifier fires.**

### 3.2 Profitability (25% weight)

```
Net Margin (TTM) = 22.25%   (yfinance t.info["profitMargins"])
NetMargin_Component = clamp((22.25/30)×100, 0, 100) = 74.17

Effective tax rate (FY2025) = Tax Provision / Pretax Income = €464.119M / €2,063.635M = 22.489%
NOPAT (FY2025) = EBIT × (1 − 0.22489) = €2,104.803M × 0.77511 = €1,631.75M
Average Invested Capital (FY2024–FY2025) = (€6,759.564M + €6,628.966M) / 2 = €6,694.265M
ROIC = €1,631.75M / €6,694.265M = 24.377%
ROIC_Component = clamp((24.377/30)×100, 0, 100) = 81.26

Profitability_Score = (74.17 + 81.26) / 2 = 77.71   (no FCF-positivity cap — clean 4yr positive FCF)
```

### 3.3 Margins (15% weight)

```
Gross Margin (TTM) = 51.618%   (yfinance t.info["grossMargins"])
GrossMargin_Score = clamp((51.618/80)×100, 0, 100) = 64.52
```
No +10 structural-trend bonus: gross margin is already well above the 40% threshold and trending up (48.0% FY2022 → 49.8% FY2023 → 50.1% FY2024 → 51.7% FY2025) — the bonus is reserved for a margin *below* 40% that's structurally improving.

`Margins_Score = 64.52`

### 3.4 Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 €5,095.254M → FY2025 €7,145.768M):
  = (7,145.768 / 5,095.254)^(1/3) − 1 = 11.933%
Growth_Score (raw) = clamp((11.933/25)×100, 0, 100) = 47.73
```
**+10 TAM/pricing-power modifier applied** — same documented, cited evidence as the 2026-08-17 session (unchanged company facts, one month later): FY2025 revenue grew +7% and EBIT +12% while unit shipments *fell* ~1% (mix/personalization-driven, not volume-driven growth); order book extended to cover all of 2027 (from 2026 a year earlier); 84% of 2025 new-car sales went to existing owners. See the 2026-08-17 session §3.4 for full sourcing — re-cited, not re-verified with new sources this session, since these are structural, slow-moving facts about FY2025 results and Ferrari's allocation model, not something that could have changed in a month with no earnings release in between.

No −10 deceleration modifier: the visible YoY revenue-growth deceleration (17.2% → 11.8% → 7.0%) is attributed to Ferrari's deliberate unit-shipment cap (scarcity strategy), corroborated by the lengthening order book — not treated as structural growth-thesis erosion.

```
Growth_Score = 47.73 + 10 = 57.73
```

### 3.5 Balance Sheet (15% weight)

```
Net Debt (FY2025) = Total Debt − Cash & Equivalents = €2,884.220M − €1,467.711M = €1,416.509M
Net Debt/EBITDA = €1,416.509M / €2,766.740M = 0.512×
BalanceSheet_Score = clamp(100 × (1 − 0.512/4), 0, 100) = 87.20
```
*Note: `yfinance`'s own pre-computed `"Net Debt"` balance-sheet field for FY2025 (€1,254.362M) differs from this manual Total-Debt-minus-Cash calculation (€1,416.509M) — likely a different debt/cash-equivalents basis in Yahoo's own derived field. This session uses the manual calculation for consistency with the framework's documented methodology and with the 2026-08-17 RACE session (which used the same manual approach and got the identical 0.512× result) — never substituting a vendor-derived convenience field without checking it against the framework's own formula.*

Ferrari is **not** treated under the Upgrade 5 asset-light override — its debt isn't 100% financial-only in the payment-network/exchange sense — so the standard 4× denominator applies. Interest coverage = EBIT/Interest Expense = €2,104.803M/€41.168M = **51.1×**, noted for completeness though the override doesn't apply.

`BalanceSheet_Score = 87.20`

### 3.6 Moat Signal (15% weight)

Same cited evidence as the 2026-08-17 session (unchanged company facts):

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | 24% of the global Luxury Performance Car segment (2025, self-reported) — no evidence of share erosion. |
| Brand premium | **TRUE** | FY2025 revenue +7% / EBIT +12% on unit shipments down ~1% — price/mix increase without volume gain; brand value +43% to $10.6B (2024), AAA+ rated. |
| Network effect | **FALSE** | No two-sided-marketplace mechanism — Ferrari is a manufacturer, not a platform business. |
| Switching costs | **TRUE** | Documented relationship-based allocation system: 84% of 2025 sales to existing owners, 56% to repeat multi-Ferrari owners. |
| Scale cost advantage | **FALSE** | No cited cost-per-unit data vs. a named competitor; Ferrari deliberately caps production for scarcity, not to achieve scale economics. |

```
Moat_Score = (3/5) × 100 = 60.0
```

### 3.7 FCF Quality (10% weight)

```
TTM FCF/NI = $1,001.98M / $1,636.12M = 61.257%
FCFQuality_Score = clamp(((0.61257 − 0.40)/0.60)×100, 0, 100) = 35.43
```
`FCFQuality_Score = 35.43` — flagged (as in the prior session): this TTM figure is meaningfully weaker than FY2025's own audited annual ratio (88.06%), likely tied to capex/working-capital timing around the F80/Elettrica model changeover — not a hard disqualifier (§3.1), but the single largest drag on the continuous score.

### 3.8 Quality Score — final calculation

```
Quality Score = (Profitability × 0.25) + (Margins × 0.15) + (Growth × 0.20)
              + (BalanceSheet × 0.15) + (Moat × 0.15) + (FCFQuality × 0.10)

              = (77.71 × 0.25) + (64.52 × 0.15) + (57.73 × 0.20)
              + (87.20 × 0.15) + (60.0 × 0.15) + (35.43 × 0.10)

              = 19.4275 + 9.678 + 11.546 + 13.08 + 9.00 + 3.543

              = 66.27  →  rounds to 66.3
```

### 3.9 Gate result: **FAIL — 66.3 < 80.0 (13.7 points short)**

This reproduces the 2026-08-17 `RACE` (NYSE) session's result (66.3, also 13.7 points short) to within immaterial rounding — confirming these are genuinely the same underlying financials, not a coincidence. The same sensitivity check applies: stacking every individually-defensible generous assumption (Moat 5-of-5 instead of 3-of-5: +6.0; FCFQuality using FY2025's own 88.06% instead of TTM's 61.26%: +4.47) reaches at most **66.27 + 6.0 + 4.47 = 76.74 — still 3.26 points below the 80.0 gate.** No combination of defensible generous readings closes the gap.

**This session stops here per the command specification: no Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is performed.** Ferrari (under either ticker) does not clear the 80.0+ Quality Score gate.

Per the task's advance note that Ferrari looked "expensive on rough prescreen" (EV/EBITDA ~26×, ROE ~45%) and valuation would likely be rich if reached: confirmed directionally from this session's own data (`enterpriseToEbitda` = 26.12×, `returnOnEquity` = 45.44%, `forwardPE` = 32.6×, `pegRatio` = 3.51) — but this is now moot, since the Quality Gate fails before any valuation scoring is performed. Recorded here only to show the underlying prescreen numbers were directionally accurate, not because they factor into the gate outcome.

---

## 4. Why this reads as a genuine (structural) miss, not a framework gap

Unchanged from the 2026-08-17 finding: Ferrari is a genuinely high-quality business by conventional standards — strong ROIC (24.4%), low leverage (0.51× Net Debt/EBITDA), documented pricing power, and a moat resting on genuine scarcity/relationship dynamics (3 of 5 signals) — but this framework's strict 80.0+ bar is missed on:

1. **FCF Quality (35.43/100, 10% weight)** — the single biggest drag; TTM FCF/NI conversion (61.26%) is weaker than FY2025's own audited 88.06%, plausibly capex/working-capital timing tied to the F80/Elettrica changeover.
2. **Margins (64.52/100, 15% weight)** — a genuinely strong 51.6% gross margin by normal standards, but the framework's Margins sub-score is calibrated with an 80% ceiling (software/platform economics); a physical-goods luxury manufacturer structurally can't approach that ceiling.
3. **Growth (57.73/100, 20% weight)** — even with the +10 pricing-power credit, an 11.9% 3yr revenue CAGR sits well short of the sub-score's 25% ceiling; Ferrari's own deliberate volume discipline caps how fast reported revenue can grow.

Same pattern the framework has now documented across several genuinely strong, real-economy, physical-goods businesses whose structural profile doesn't fit a scoring scale calibrated primarily around software/platform/asset-light compounders — flagged per the quality-scoring.md instruction to note (not silently patch) cases like this, not a framework bug.

---

## 5. Recommendation: **PASS (no entry) — Quality Gate FAIL at 66.3 (need 80.0+)**

**Do not enter Ferrari (under either RACE or RACE.MI) this session.** Quality Score 66.3 is 13.7 points below the strict 80.0+ gate; even the most generous defensible sensitivity reading only reaches 76.74, still short. **No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup was computed**, consistent with the command specification's instruction to stop at the Quality Gate. No position opened — nothing to log in `decisions/`.

---

## 6. Next Review Trigger

No routine numeric re-check is scheduled (Phase 01 FAILs don't carry a numeric score to go stale — per [watchlist/README.md](../watchlist/README.md)). A future re-look is warranted on:
- Ferrari's next earnings release (Q3 2026, expected late October/early November) — clarifies whether the TTM FCF/NI weakness persists or was a one-off capex/working-capital timing item.
- A sustained improvement in FCF/NI conversion back toward FY2025's own 88% level.
- Standard Rule 9 triggers: guidance revision, management change, material M&A, macro/rate shift, or a >15% unexplained price move.

Absent any of the above, a future mention of either RACE or RACE.MI should be logged as "last checked, no change" against **both** watchlist entries — not just the one triggering the re-check — given §0's duplicate-entity finding.

---

## 7. Data Gaps Flagged

1. **No IBKR live-price cross-check performed this session** (unlike the 2026-08-17 RACE session, which cross-checked IBKR vs. Yahoo pre-market quotes) — since the Quality Gate fails regardless of price, and Rule 0's live-price requirement is satisfied via the direct `yfinance` pull, this wasn't treated as blocking. Flagged so a future session that actually reaches valuation scoring performs the full two-source cross-check.
2. **Moat signal and TAM/pricing-power evidence re-cited, not re-verified with fresh sources this session** (§3.4, §3.6) — carried forward from the 2026-08-17 session's citations since no earnings release occurred in the intervening month and the underlying facts (FY2025 results, allocation-system mechanics) are not time-sensitive at a one-month granularity. Flagged as a methodology choice, not a data gap being silently patched.
3. **`RACE.MI` vs. `RACE` — one entity, two watchlist folders** (§0) — not consolidated this session; a housekeeping item for the user or a future watchlist-hygiene pass.

None of these gaps is silently patched around or outcome-determinative for the gate result (§3.9's sensitivity check already shows the conclusion is robust to every defensible generous reading).

---

## 8. Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used throughout this session's Balance Sheet and Profitability sub-scores. |
| **Effective tax rate** | The actual share of pretax income paid as tax in a period — 22.489% for Ferrari's FY2025 (§3.2), used to convert EBIT into NOPAT for the ROIC calculation. |
| **FCF (Free Cash Flow) / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Net Income (a cash-quality check). Ferrari's FCF/NI ratio ran 61–88% across FY2022–FY2025 (§3.7) — the framework's single biggest drag on this session's Quality Score. |
| **Hard disqualifier** | One of three Quality Score conditions ([quality-scoring.md](../framework/quality-scoring.md)) that fails a company regardless of its weighted sub-score total. None fires for Ferrari (§3.1). |
| **Interest coverage (ratio)** | EBIT ÷ interest expense — how many times over a company could pay its interest bill from operating profit. Ferrari's is 51.1× (§3.5), far above the asset-light-override threshold, though that override doesn't apply to Ferrari's business model. |
| **Invested Capital** | The total capital (debt + equity, netted for cash) deployed in a business — the denominator of this session's ROIC calculation, an average of €6,694.265M across FY2024–FY2025 (§3.2). |
| **Moat / Moat Signal** | A durable competitive advantage protecting profits from competitors; this framework's 5-point checklist version scored Ferrari 3 of 5 TRUE this session (§3.6). |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC (§3.2). |
| **Quality Score** | This framework's 0.0–100.0 continuous score grading the Phase 01 criteria; a company must score 80.0+ to proceed to Phase 02 valuation scoring at all. Ferrari scores 66.3 this session, matching the 2026-08-17 RACE (NYSE) session's result (§3.8–3.9). |
| **Rate Environment Gate** | The Phase 02 pre-check (Earnings Yield Spread Test + Rate Regime Modifier) run before every valuation score; never reached this session since the Quality Score gate fails first. |
| **ROIC (Return on Invested Capital)** | How efficiently a company turns invested capital into profit; a core quality signal in this framework. Ferrari's ROIC (24.377%) is strong despite the overall gate failure (§3.2). |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work, and never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% unexplained stock-price move. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results; the primary basis for several of this session's sub-score inputs, per `yfinance`'s own trailing-window fields. |

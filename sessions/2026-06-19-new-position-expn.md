# NEW POSITION — Experian plc (LON:EXPN) — 2026-06-19

**Task type:** NEW POSITION
**Date:** 19 Jun 2026
**10Y US Treasury Yield:** 4.45%
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current EXPN portfolio weight:** 0% — not currently held (confirmed against [holdings.md](../portfolio/holdings.md))
**Sector:** Global consumer/commercial credit bureau & data analytics — one of three global incumbents (alongside Equifax and TransUnion)
**Currency:** Experian trades in **GBX (pence)** on the LSE (primary listing) but **reports its financial statements in USD** (`yfinance` `financialCurrency` = USD, confirmed against FY2026 results). This dual-currency structure is the central methodological issue of this session — see §0.

---

## 0. Critical data-quality finding: a GBP/USD currency-mixing bug in the Phase 01 screening session's numbers

Before any new calculation, this session re-verified every Phase 01 metric from the 2026-06-19 screening session ([sessions/2026-06-19-screening-europe.md](2026-06-19-screening-europe.md)) against raw `yfinance` data, per the task instructions. **Two of the eight screening-session metrics (EV/EBIT and FCF yield) were computed from internally currency-inconsistent inputs and are materially wrong.** This is the same family of error as the SPGI stale-price lesson in [fair-value-methodology.md](../framework/fair-value-methodology.md) — a unit/basis error propagating silently through every downstream calculation — just on the currency axis instead of the staleness axis.

**Root cause:** Experian's `yfinance.Ticker('EXPN.L').info` snapshot mixes currencies without flagging it:
- `info['currentPrice']`, `info['marketCap']` → **GBP/GBX** (pence/pounds) — tied to the LSE listing
- `info['totalDebt']`, `info['totalCash']`, `info['ebitda']`, `t.financials`, `t.cashflow`, `t.balance_sheet` → **USD** — tied to `financialCurrency`
- `info['enterpriseValue']` (28.305B) = GBP-denominated market cap (22.68B, treated as if USD) + USD-denominated debt (5.6B) − USD-denominated cash (0.337B) ≈ 27.95B — **adds two different currencies together without converting either.**
- `info['forwardPE']` (14.73×) = price in **pence** ÷ EPS in **USD**, divided by 100 — not a real currency conversion, just a coincidental near-miss because pence-to-pounds (÷100) and GBP→USD (×1.32) partially offset. Same trap as the `0y`/`+1y` issue flagged in the SGE precedent, but one layer deeper.

| Metric | Screening session (mixed currency, wrong) | This session (FX-corrected) | Why it changed |
|---|---|---|---|
| EV/EBIT | 13.00× | **16.13×** | EV recomputed as (Market Cap in USD, via live GBPUSD rate) + (Net Debt, USD) — both legs now genuinely USD |
| FCF yield | 6.67% | **5.04%** | FCF (USD, FY2026 annual) ÷ Market Cap converted to USD (was ÷ GBP-labeled-as-USD market cap) |
| Net Debt/EBITDA | 2.06× | 1.67× (FY2026) | Both legs (`info` net debt, `info` EBITDA) were already USD/USD — internally consistent; the small change is from using FY2026 (latest annual) instead of whatever period `info`'s trailing EBITDA blends, not a currency fix |
| Gross margin, net margin, ROE, revenue 3yr CAGR | unaffected | unaffected | These are ratios computed from same-currency numerator/denominator either way (margins) or don't touch price/market cap at all (CAGR) |

**This re-verification still passes Phase 01 (see §3), but at a different, more demanding EV/EBIT than originally screened, and it changes the Phase 02 score materially (see §6) — this is not a case where the conclusion is unaffected, unlike some other corrected sessions in this repo's history.** All calculations below use FX-corrected, currency-consistent figures throughout; the procedure used (convert price to USD via the live `GBPUSD=X` rate, then keep every ratio numerator/denominator in USD) is applied consistently to Experian and to the GBP-reporting peer (RELX) in §8.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price (GBX, trading currency)** | **2542.00p** (£25.42) | `yfinance` `Ticker('EXPN.L').info['currentPrice']`, cross-checked against `regularMarketPrice` (2542.00) and `previousClose` (2509.00) — consistent intraday move, and consistent with the prior 10 trading days' close-to-close pattern (2600→2619→2556→2497→2569→2563→2558→2558→2509→2542), so this is a genuine 19 Jun 2026 quote, not stale data |
| **Live price (USD, financial-statement-consistent basis)** | **$33.6488** | = 2542.00p ÷ 100 × GBPUSD 1.3237144 — used for every ratio that mixes price with a USD-denominated financial-statement line (see §0) |
| 52-week range | GBX 2,203.00 – 4,101.00 | `yfinance` `fiftyTwoWeekLow`/`fiftyTwoWeekHigh`. Stock is down ~32% from where it traded a year ago (1yr-ago close ≈3,767p; verified via `t.history(period="1y")`) — a real, large decline, not a data artifact |
| Analyst consensus PT (12-month) | Mean **3,912.19p**, median 4,014.30p, range 2,387.00–4,774.32p, 18 analysts; recommendation: Strong Buy | `yfinance` `targetMeanPrice`/`targetMedianPrice`/`recommendationKey` |
| Shares outstanding | **892,391,389** | `yfinance` `sharesOutstanding` |
| Market cap (GBP) | **£22,684.6M** | = 2542.00p/100 × 892,391,389 shares — matches `yfinance`'s own `marketCap` field (£22,684,590,080) almost exactly |
| Market cap (USD, FX-corrected) | **$30,027.9M** | = £22,684.6M × 1.3237144 |
| Beta (5yr) | **0.824** | `yfinance` `info['beta']` — close to market, no outlier-volatility case for a non-standard stop band (contrast with the SGE session's beta 0.293) |
| GBP/USD | **1.3237144** | `yfinance` `Ticker('GBPUSD=X').info['regularMarketPrice']` |

---

## 2. Data Gathered (Phase 01 + Phase 02 Inputs) & Gaps Flagged

### FY2026 results (year ended 31 March 2026) — latest annual report, USD basis

Experian's fiscal year ends 31 March; FY2026 results (covering the year to 31 Mar 2026) were already published by results-announcement date and are the latest annual data available via `yfinance` (`t.financials`/`t.cashflow`/`t.balance_sheet` all show `2026-03-31` as the most recent column). Confirmed externally: Experian's FY26 results press release reports 13% total revenue growth and 8% organic growth, "topping forecasts," with a new $1bn buyback announced — consistent with the strong growth shown in the raw data below.

| Metric | FY2026 | FY2025 | FY2024 | FY2023 |
|---|---|---|---|---|
| Total revenue | $8,445M | $7,523M | $7,097M | $6,619M |
| EBIT | $2,178M | $1,726M | $1,703M | $1,311M |
| EBITDA | $3,054M | $2,484M | $2,417M | $1,985M |
| Net income | $1,502M | $1,166M | $1,199M | $770M |
| Free cash flow | $1,513M | $1,354M | $1,107M | $1,090M |
| Net debt (FY-end) | $5,104M | $4,512M | $3,803M | $3,749M |
| Stockholders' equity | $5,545M | $5,054M | $4,634M | $3,929M |

Source: `yfinance` `t.financials`, `t.cashflow`, `t.balance_sheet` (`Ticker('EXPN.L')`). All figures USD per `financialCurrency`.

### Revenue 3yr CAGR — re-verified, matches screening session exactly

```
3yr CAGR = (8,445 / 6,619)^(1/3) − 1 = 8.46%   (FY2023 $6,619M → FY2026 $8,445M)
```

### Net margin — re-verified

```
Net margin FY2026 = 1,502 / 8,445 = 17.79%
```
Matches the screening session's 17.79% exactly — this metric was not affected by the currency-mixing issue (same-currency numerator and denominator either way).

### Gross margin — data-quality note (judgment call, not a new error)

`info['grossMargins']` = 42.01% (matches the screening session). Re-deriving gross margin from `t.financials`' "Gross Profit" / "Total Revenue" annual rows gives a noisy, inconsistent series (47.8% FY25, 55.6% FY24, 47.9% FY23) that swings implausibly year to year — almost certainly an artifact of how Yahoo's data vendor auto-splits cost-of-revenue vs. SG&A for a services business like Experian, which doesn't report a clean statutory COGS line. **`info['grossMargins']` (42.01%) is retained as primary**, consistent with the screening session, because it is Yahoo's own standardized TTM computation rather than a noisy re-derivation from inconsistently-classified annual line items. Flagged transparently per Rule 6 ("value the underlying business, not the accounting statements" — the annual P&L's auto-split COGS line is the less reliable of the two here, not the underlying business).

### FCF/Net Income conversion ratio — re-verified, comfortably above 70%

| FY | FCF | NI | Conversion |
|---|---|---|---|
| 2023 | $1,090M | $770M | 141.6% |
| 2024 | $1,107M | $1,199M | 92.3% |
| 2025 | $1,354M | $1,166M | 116.1% |
| 2026 | $1,513M | $1,502M | 100.7% |

✅ Comfortably clears >70% for every year shown, including the required "2+ consecutive years."

### EPS / Fast Grower history — re-verified with a data gap flagged

`t.financials`' "Diluted EPS" row is **missing (NaN) for FY2026** — `yfinance` does not provide a FY2026 diluted share count, so FY2026 diluted EPS cannot be computed from this source without estimating a share count (not done, per Rule 0). Net income growth is used as a same-period proxy where the EPS figure itself is unavailable:

| Period | Diluted EPS | YoY EPS growth | Net Income YoY growth (proxy) | >15%? |
|---|---|---|---|---|
| FY2023 | $0.836 | — | — | — |
| FY2024 | $1.302 | +55.7% | +55.7% | ✅ Yes |
| FY2025 | $1.265 | **−2.8%** | −2.8% | ❌ No |
| FY2026 | n/a (data gap) | n/a | +28.8% | ✅ Yes (NI basis) |

The FY2025 dip breaks the "3 consecutive years >15%" chain regardless of which metric is used for FY2026 — **not a Fast Grower**. PEG's 15% weight redistributes to EV/EBIT (40% total) per the Final Score Formula.

### Forward PE — recomputed on a verified, currency-consistent, FY-correct basis

```
yfinance eps_trend (Ticker('EXPN.L').eps_trend), all figures in USD:
  0y  (FY2027E, next fiscal year ending Mar 2027) EPS estimate = $2.01878   <- correct "Forward PE" basis
  +1y (FY2028E, fiscal year after next) EPS estimate           = $2.31637  <- what a naive currency-uncorrected forwardPE field would lean toward

Forward PE = Price(USD) / EPS(0y, USD) = $33.6488 / $2.01878 = 16.67×

For contrast, yfinance's raw `info['forwardPE']` field gives 14.73× — this figure is neither
a clean 0y nor a clean +1y read; it is Price(pence)/100 ÷ EPS(USD) with no GBP→USD step at all,
i.e. doubly wrong (wrong EPS-period leaning AND missing FX conversion). Not used.
```

This `0y`-vs-`+1y` check, and the broader GBp/USD correction, was applied consistently to Experian and to the one GBP-reporting peer (RELX) in §8's comparables table; the five USD-reporting US peers (EFX, TRU, VRSK, MCO, SPGI) don't have this issue since price and EPS are already same-currency for them.

### 10-year historical PE — sourced via WebSearch (not time-sensitive, multiple corroborating sources)

| Metric | Value | Source |
|---|---|---|
| 10yr low | 19.54× | GuruFocus (LSE:EXPN PE Ratio TTM) |
| 10yr high | 57.47× | GuruFocus |
| 10yr median | 35.58× | GuruFocus |
| 10yr **mean/average** | **30.39×** | cited via stockanalysis.com aggregation in WebSearch results |

A genuine low/high range is available, so the **primary** Forward-PE-score formula (position within the range) is used, with the 30.39× average used for the Upgrade 2 Historical PE Modifier test.

### Net debt/EBITDA — re-verified on FY2026 (latest annual) basis

```
Net Debt/EBITDA = $5,104M / $3,054M = 1.67×   (<2.5× required — comfortably passes)
```

### WACC inputs

| Input | Value | Source |
|---|---|---|
| Risk-free rate (UK 10Y Gilt) | 4.82% (17 Jun 2026) | WebSearch — same figure independently used in the same-day SGE session, not re-fetched as it is a 2-day-old, non-time-critical macro input |
| Experian's own beta (5yr) | 0.824 | `yfinance` |
| Equity Risk Premium | 5.0% | Standard convention |
| Credit rating | Moody's A3 / S&P A- (Experian Finance US, Inc.); company targets BBB+/Baa1-or-better at the group level | WebSearch |
| Gross interest expense FY2026 | $227M | `yfinance` `t.financials.loc['Interest Expense Non Operating']` |
| Total debt FY2026 | $5,565M | `yfinance` `t.balance_sheet` |
| Cost of debt (pre-tax) | $227M / $5,565M = **4.08%** | Computed |
| Effective tax rate FY2026 | $443M / $1,951M = **22.71%** | Computed from `t.financials` Tax Provision / Pretax Income |
| Cost of debt (after-tax) | 4.08% × (1−0.2271) = **3.15%** | Computed |
| Capital structure (market-value weights) | Equity 84.36% / Debt 15.64% | Market cap (USD) $30,027.9M vs. total debt $5,565M |

### Peer comparables (Rule 5)

Credit bureau / data-analytics peers per the task brief: Equifax (EFX), TransUnion (TRU), Verisk Analytics (VRSK), Moody's (MCO), S&P Global (SPGI), RELX (REL.L). **Dun & Bradstreet (DNB) is no longer usable as a public-market comparable** — confirmed via WebSearch that Clearlake Capital completed a take-private acquisition of D&B in August 2025 ($9.15/share cash), and the stock was delisted from the NYSE in September 2025; `yfinance` returns a 404 for the ticker, consistent with this.

| Company | Forward PE (0y basis) | EV/EBIT | Revenue (latest FY, $B) | In Rule 5 ±50% band of EXPN's $8.445B? |
|---|---|---|---|---|
| Equifax (EFX) | 17.89× | 22.73× | $6.28B | ✅ |
| TransUnion (TRU) | 13.52× | 20.94× | $4.73B | ✅ |
| Verisk Analytics (VRSK) | 22.67× | 20.59× | $3.10B | ❌ below band ($4.22B floor) |
| Moody's (MCO) | 26.99× | 25.76× | $7.87B | ✅ |
| S&P Global (SPGI) | 20.93× | 22.32× | $15.73B | ❌ above band ($12.67B ceiling) |
| RELX (REL.L) | 16.81× | 16.17× | $9.59B | ✅ |
| **Median** | **19.41×** | **21.63×** | | |

**Flagged per Rule 5:** VRSK and SPGI both breach the ±50% revenue-scale guideline (VRSK is a much smaller, more specialized analytics business; SPGI is ~86% larger, with a broader ratings/indices/market-intelligence mix than Experian's pure-play bureau model). Shown transparently rather than trimmed, consistent with this repo's no-outlier-trimming precedent (see the SGE session's treatment of Workday) — but the median here is comfortably anchored by the four in-band names (EFX, TRU, MCO, REL.L) clustering closely around both medians, so this is a less consequential flag than in the SGE case.

RELX required the same GBp/GBP currency correction as Experian (price in pence, financials in GBP) — its `info['forwardPE']` raw field (15.20×) is wrong for the same reason as Experian's; the corrected 16.81× uses price-in-GBP ÷ EPS-in-GBP, both currency-consistent.

### Data Gaps flagged

1. **FY2026 diluted EPS / diluted share count** — `yfinance` does not provide this; net income growth used as a same-period proxy for the Fast Grower YoY test where needed (does not change the conclusion either way — chain is already broken by FY2025's −2.8%).
2. **Gross margin annual-statement re-derivation is noisy/unusable** (see above) — `info['grossMargins']` retained as primary, consistent with the screening session.
3. **10-year PE range/average are WebSearch-sourced** (GuruFocus/stockanalysis.com aggregation), not pulled directly from a primary data vendor with full underlying-data transparency — retained per the task brief's explicit allowance ("WebSearch acceptable for historical PE range/average since it's not as time-sensitive as live price").
4. **Dun & Bradstreet excluded from the peer set** — taken private August 2025, no longer a public-market comparable; one fewer peer (6 instead of the up-to-7 originally suggested) but still clears Rule 5's minimum of 5.

---

## 3. Phase 01 — Quality Gate (re-verified, FX-corrected)

| Check | Experian Value | Threshold | Result |
|---|---|---|---|
| Gross margin | 42.01% | >40% (valuation-scoring.md) | ✅ PASS |
| Net margin | 17.79% | >12% (valuation-scoring.md) | ✅ PASS |
| ROE (ROIC proxy) | 28.26% (per screening session `info['returnOnEquity']`, re-verified unchanged) | >15% | ✅ PASS |
| Revenue CAGR 3yr | 8.46% | >8% (valuation-scoring.md) | ✅ PASS |
| FCF positive 3+ consecutive years | Yes — FY24 $1.107B, FY25 $1.354B, FY26 $1.513B | required | ✅ PASS |
| FCF/NI conversion ratio | FY26: 100.7%, FY25: 116.1% | >70% | ✅ PASS, comfortably |
| **Net Debt/EBITDA** | **1.67×** (FY2026, currency-consistent) | <2.5× | ✅ PASS — improved from the screening session's 2.06× (that figure mixed `info`'s TTM-ish EBITDA basis with `info`'s net debt; this session uses FY2026 annual EBITDA, which is internally consistent and the more current figure) |
| **EV/EBIT** | **16.13×** (FX-corrected — see §0) | <20× | ✅ PASS — but materially higher than the screening session's mixed-currency 13.00×; still clears the gate but with much less room |
| Share issuance pattern | Net buyback (new $1bn buyback announced with FY26 results) | non-dilutive required | ✅ PASS |

**Gate result: PASS — 8/8 metrics pass.** The two metrics affected by the §0 currency-mixing correction (EV/EBIT, Net Debt/EBITDA) both still clear their respective thresholds, but EV/EBIT in particular is now meaningfully closer to the 20× ceiling (16.13× vs. the previously-believed 13.00×) than the screening session suggested. **Proceeding to Rate Environment Gate and Phase 02** — nothing here triggers a "stop and report" per the task's instruction to halt only if something that previously passed now fails.

---

## 4. Fast Grower (Upgrade 3 — PEG) Determination

EPS/NI growth chain: FY24 +55.7% → FY25 **−2.8%** → FY26 +28.8% (NI proxy). The FY2025 dip breaks the "3 consecutive years >15%" requirement regardless of which year's figure is used as the anchor. **Not a Fast Grower.** PEG's 15% weight redistributes to EV/EBIT, making EV/EBIT 40% of the total score.

---

## 5. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**

```
Forward PE = 16.67× (FX-corrected, 0y basis — see §2)
EY     = 1 ÷ 16.67 = 6.000%
Spread = EY − 10Y Treasury = 6.000% − 4.45% = +1.550%
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** (by a thin but clear margin of +0.05pp) → **0 additive** (Step 1).

This is a knife-edge pass — if the Forward PE basis had instead used the uncorrected `info['forwardPE']` (14.73×, the doubly-wrong currency/period mix), EY would be 6.79% and the spread would widen to +2.34% (still a pass, just by more); if it had instead leaned on the `+1y` figure even with correct FX (14.53×), EY would be 6.88% and spread +2.43%. **All plausible bases here pass Step 1** — the FX correction does not flip this particular gate, unlike in the SGE precedent — but it is close enough to the 1.5% line that this is worth a closer look at the next quarterly Rate Gate update if the 10Y moves materially.

**Step 2 — Rate Regime Modifier**
10Y = 4.45% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for Experian = 0 (Step 1) + 5 (Step 2) = +5**

---

## 6. Phase 02 — Full Score Calculation

**FCF Yield — 40% weight**

```
FCF Yield = FCF(FY2026, USD) / Market Cap (USD) = $1,513M / $30,027.9M = 5.039%

FCF_Score = clamp(100 × (1 − 5.039/10), 0, 100) = clamp(49.61, 0, 100) = 49.61
```
→ Contribution: 49.61 × 0.40 = **19.844**

**EV/EBIT — 40% weight (PEG not applicable, redistributed from 25%)**

```
Market Cap (USD) = $30,027.9M
Net Debt (USD, FY2026)  = $5,104M
EV (USD, FX-corrected) = $30,027.9M + $5,104M = $35,131.9M

EV/EBIT = $35,131.9M / $2,178M (FY2026 EBIT) = 16.130×

EV/EBIT_Score = clamp((16.130 − 12) / 23 × 100, 0, 100) = clamp(17.957, 0, 100) = 17.957
```
→ Contribution: 17.957 × 0.40 = **7.183**

**Forward PE (PRIMARY formula — 10yr low/high range available) — 20% weight**

```
Forward PE   = 16.67×
10yr Low PE  = 19.54×
10yr High PE = 57.47×

FwdPE_Score (raw) = clamp((16.67 − 19.54) / (57.47 − 19.54) × 100, 0, 100) = clamp(−7.57, 0, 100) = 0.0
```

Forward PE sits below the 10-year low — cheapest possible reading on this dimension.

**Historical PE Modifier (Upgrade 2)**

```
Deviation from 10yr avg = (16.67 − 30.39) / 30.39 = −45.15%
```
>20% below average → modifier = **−10** (no further effect; already at the 0.0 floor).

```
FwdPE_Score (adjusted) = clamp(0.0 − 10, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.000**

**PEG — not applicable (redistributed to EV/EBIT)**

### Final Score

```
Raw weighted score = (49.61 × 0.40) + (17.957 × 0.40) + (0.0 × 0.20)
                    = 19.844 + 7.183 + 0.000
                    = 27.027

+ Rate Regime Modifier (0 + 5) = 27.027 + 5 = 32.027
```

Boundary rule: 32.027 → nearest 0.1 → **Final Score = 32.0**

---

## 7. Final Score & Action

# Final Score: 32.0 → Action Table band: 30.0–49.9 (Cheap) → BUY — Standard position 3–5% of portfolio (subject to clearing the R/R gate — see §8)

Experian lands in the **Cheap**, not **Very Cheap**, band. This is a direct, material consequence of the §0 currency correction: under the screening session's mixed-currency EV/EBIT (13.00×) and FCF yield (6.67%), the FCF and EV/EBIT sub-scores would have been meaningfully lower (cheaper), likely landing the raw score closer to the Very Cheap boundary. The FX-corrected, internally-consistent inputs (EV/EBIT 16.13×, FCF yield 5.04%) push both of the two highest-weighted sub-scores up, and the Forward PE sub-score — though still at its 0.0 floor — isn't enough to offset that on its own.

### Sanity check

The qualitative case (oligopoly bureau moat, 28%+ ROE, double-digit growth) is unchanged and strong — Experian's Forward PE (16.67×) sitting below its own 10-year low (19.54×) and 45% below its 10-year average (30.39×) is a genuinely striking signal, and is consistent with both peer comparables (median Forward PE 19.41×, EV/EBIT 21.63× — Experian trades at a discount to both) and the stock's own 32% decline from a year ago. The qualitative pass from the screening session (oligopoly moat, regulatory accreditation barrier, consistent bolt-on M&A, alternative-data disruption risk monitored-not-acute) is reaffirmed without material change.

---

## 8. Fair Value & Order Setup

### Step 1 — Fair Value (Blended)

**Method A: DCF (3 scenarios, Rule 2/7)**

```
Cost of Equity = 4.82% (UK 10Y Gilt) + 0.824 (beta) × 5.0% (ERP) = 8.940%
Cost of Debt (after-tax) = 4.08% × (1 − 22.71%) = 3.154%
WACC = 0.8436 × 8.940% + 0.1564 × 3.154% = 8.035% ≈ 8.0%
```

Base FCF = $1,513M (FY2026). 3-stage DCF: Stage 1 (yrs 1–5) explicit growth; Stage 2 (yrs 6–10) growth fades linearly to the 2.5% terminal rate; Stage 3 Gordon-growth terminal value off year-10 FCF. Growth assumptions are anchored to Experian's own FY2027 guidance (total revenue +8–11%, organic +6–8%, double-digit Benchmark EPS growth) and FY2026 actuals (13% total / 8% organic) — confirmed via WebSearch of the FY26 results announcement:

| Scenario | WACC | Yrs 1–5 growth | PV(FCF Yrs 1–10) | PV(Terminal Value) | EV | TV weight |
|---|---|---|---|---|---|---|
| Bear | 9.04% | +5% | $12,189M | $15,126M | **$27,315M** | 55.4% |
| Base | 8.04% | +7% | $13,956M | $22,356M | **$36,312M** | 61.6% |
| Bull | 7.04% | +9% | $16,030M | $34,108M | **$50,138M** | 68.0% |

All three pass the <75% terminal-value-weight sanity check (Rule 4).

```
PW DCF EV = 0.25×50,138 + 0.50×36,312 + 0.25×27,315 = $37,519M

DCF Equity Value = $37,519M − Net Debt $5,104M = $32,415M
DCF FV/share (USD) = $32,415M / 892,391,389 shares = $36.324
```

**Method B: Comparable Multiples**

```
EV/EBIT reversion: median peer EV/EBIT (21.63×) × Experian EBIT ($2,178M)
                  = implied EV $47,110M − Net Debt $5,104M = Equity $42,006M
                  ÷ 892,391,389 shares = $47.071/share (USD)

Forward PE reversion: median peer Forward PE (19.41×, 0y basis) × Experian's own Forward EPS ($2.01878)
                     = $39.185/share (USD)

Multiples avg = ($47.071 + $39.185) / 2 = $43.128/share (USD)
```

```
Blended FV (USD) = 40% × DCF FV/share + 60% × Multiples avg
                  = 0.40 × $36.324 + 0.60 × $43.128
                  = $14.530 + $25.877
                  = $40.406/share

Convert to GBX: $40.406 / 1.3237144 (GBPUSD) = £30.525 = 3,052.50p
```

**Cross-check vs external estimates.** Blended FV (3,052.50p) sits **−22.0% below** the `yfinance`-sourced analyst consensus mean (3,912.19p). This divergence runs in the opposite direction to what a simple "is our number reasonable" check might expect from a Very-Cheap-screening name — but it's explainable: sell-side consensus targets are typically anchored closer to current trading multiples and recent guidance momentum (Experian just raised FY26 guidance and beat), while this framework's blended FV deliberately reverts the multiple toward both a DCF-implied intrinsic value and a peer-median multiple that is itself below where Experian currently trades on a trailing basis. The DCF (Base case, $34.97/share ≈ 2,801p) and the Forward-PE-reversion figure ($39.185 ≈ 3,136p) bracket the Blended FV reasonably tightly; the EV/EBIT-reversion figure ($47.071 ≈ 3,766p) is the highest of the three components and is the main reason the multiples-based half of the blend sits above the DCF half — but unlike the SGE precedent, this isn't being driven by a single scale-mismatched outlier peer (the median EV/EBIT of 21.63× is set by names within Rule 5's revenue-scale band).

---

### Step 2 — Buy Price & R/R Gate

Score 32.0 falls in the **30.0–49.9 (Cheap)** band → MoS 25–30%.

```
Buy Price ceiling (25% MoS, tight end)    = 3,052.50p × 0.75 = 2,289.38p
Buy Price ceiling (27.5% MoS, midpoint)   = 3,052.50p × 0.725 = 2,213.06p
Buy Price ceiling (30% MoS, loose end)    = 3,052.50p × 0.70 = 2,136.75p
```

**Current price (2,542.00p) is ABOVE every point in the 25–30% MoS buy-ceiling band.**

```
Implied MoS at current price = 1 − (2,542.00 / 3,052.50) = 16.72%
```

16.72% does not clear even the loosest end of the required 25–30% MoS band. Per Step 2 of fair-value-methodology.md: Score 30.0–49.9 → "Approaching buy price → **Set limit order**" — *if* the R/R gate (Step 6) also clears. It does not, as shown next.

**Step 6 (Risk/Reward) — full sensitivity, all combinations checked**

```
R/R = (Blended FV − Entry) / (Entry − Stop Loss)
```

| Buy Price (MoS) | Stop Loss (max loss %) | Stop price | R/R |
|---|---|---|---|
| 2,289.38p (25%) | 25% | 1,717.03p | 1.33:1 |
| 2,289.38p (25%) | 27.5% | 1,659.80p | 1.21:1 |
| 2,289.38p (25%) | 30% | 1,602.56p | 1.11:1 |
| 2,213.06p (27.5%) | 25% | 1,659.80p | 1.52:1 |
| 2,213.06p (27.5%) | 27.5% | 1,604.47p | 1.38:1 |
| 2,213.06p (27.5%) | 30% | 1,549.14p | 1.26:1 |
| **2,136.75p (30%, best case)** | **25% (tightest, best case)** | **1,602.56p** | **1.71:1** |
| 2,136.75p (30%) | 27.5% | 1,549.14p | 1.56:1 |
| 2,136.75p (30%) | 30% | 1,495.72p | 1.43:1 |

**No combination within the standard 25–30% MoS / 25–30% stop-loss bands clears the 2:1 minimum.** The best case across the entire grid (30% MoS buy price combined with the tightest 25% stop) reaches only **1.71:1**.

**Could a justified stop-tightening close the gap, per the SGE precedent?** The SGE session tightened its stop band beyond the standard range, but only because Sage's beta (0.293) was an extreme outlier — clearly less volatile than the market, which is an evidence-based justification for a tighter-than-standard stop. Experian's beta is **0.824** — close to market average, not an outlier in either direction. There is no beta- or volatility-based justification here for a non-standard tightened stop. Solving for the stop that *would* clear 2:1 at the most favorable entry (2,136.75p, 30% MoS) requires a max-loss band of only ~21.4% (stop at 1,678.88p) — tighter than the entire standard 25–30% band for this score tier, with no fundamentals-based justification to go there.

**Per fair-value-methodology.md Step 6: "If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely."** A lower entry is the only one of those three options with a clear evidentiary basis here (no justified tighter stop exists), and that just restates "wait" — i.e., **do not enter at current levels.**

---

### Step 3 — Sell Targets (for reference / future re-trigger)

```
Primary Sell Target = Blended FV = 3,052.50p
```

Bull-Case Blended FV (Bull DCF EV $50,138M → equity $45,034M → $50.464/share ≈ $46.063 blended with the same Multiples avg $43.128):
```
Bull Blended FV (USD) = 0.40×$50.464 + 0.60×$43.128 = $46.063/share = 3,479.80p
Bull-Case Trim Target = 3,479.80p × 0.90 = 3,131.82p
```

### Step 4 — Position Size (reference only — not actioned, gate not cleared)

For documentation completeness, sizing at the hypothetical limit-order entry (2,213.06p, 27.5% MoS midpoint) and its corresponding stop (1,604.47p, 27.5% midpoint band) — **shown for reference; this trade is not being entered, so this size is not actionable today:**

```
Risk per share = 2,213.06p − 1,604.47p = 608.59p = £6.0859

Max $ Risk (1.5% of $53,659.11 portfolio, Score 30.0-49.9 band) = $804.89
Converted to GBP: $804.89 / 1.3237144 = £608.05

Shares (risk-based) = £608.05 / £6.0859 = 99.9 → 100 shares
Position size = 100 × £22.1306 = £2,211.06 = $2,926.87 (at GBP/USD 1.3237144)
% of portfolio = $2,926.87 / $53,659.11 = 5.45%
```

This would sit just above the 3–5% allocation band for this score tier (would need slight capping to 5%, i.e. ~92 shares) — moot, since the R/R gate is the binding constraint, not position sizing.

```
[x] Valuation Score:                         32.0   (Cheap band — 30.0-49.9)
[x] DCF Fair Value (PW, scenario-weighted):  $36.324/share (≈2,907.46p)
[x] Multiples-Based Fair Value:              $43.128/share (≈3,257.66p)
[x] Blended Fair Value:                      3,052.50p
[x] Margin of Safety %:                      25-30% required -> Buy Price ceiling range 2,136.75p-2,289.38p;
                                              current price (2,542.00p) is ABOVE every point in this range
                                              (implied MoS only 16.72%) -> NOT at buy price
[ ] BUY PRICE (limit order):                  not placed — R/R gate fails at every point in the standard MoS/stop grid (see below)
[x] PRIMARY SELL TARGET (at FV):             3,052.50p  (reference, for monitoring)
[x] BULL-CASE TRIM TARGET:                   3,131.82p  (reference, for monitoring)
[ ] STOP LOSS:                                not applicable — no position being opened
[x] Risk/Reward Ratio:                       best case across full grid = 1.71:1 — FAILS the 2:1 minimum
[ ] Max $ Risk:                               not applicable — no position being opened
[ ] POSITION SIZE (shares):                   not applicable — no position being opened (reference calc above: ~100 sh / 5.45% if it had cleared)
[ ] POSITION SIZE ($):                        not applicable
[x] Thesis invalidation / re-trigger conditions: see §9/§10
```

---

## 9. Recommendation

# **WATCHLIST ONLY — DO NOT ENTER. Score 32.0 (Cheap) supports a standard 3–5% position in principle, but the order-setup math fails the framework's hard 2:1 Risk/Reward gate at every point in the standard 25–30% MoS / 25–30% stop-loss grid (best case 1.71:1). Per fair-value-methodology.md Step 6, this is a "wait for a lower entry or pass" outcome, not an "enter now" or "set limit order" outcome.**

**Why this is a genuine, examined "no" rather than a hasty pass:**

1. **A real, material data-quality finding drove the score itself**: the prior screening session's EV/EBIT (13.00×) and FCF yield (6.67%) were computed from currency-inconsistent `yfinance` fields — GBP-denominated market cap mixed with USD-denominated debt/EBIT/FCF, with no FX conversion applied anywhere in the chain. The economically correct, currency-consistent figures (EV/EBIT 16.13×, FCF yield 5.04%) are both meaningfully less cheap. This single correction is the difference between what might have screened as "Very Cheap" and what this session's rigorous recomputation finds to be "Cheap" — a real, not cosmetic, difference in conclusion.

2. **The qualitative case remains genuinely strong** — three-incumbent global bureau oligopoly, 28%+ ROE, 8%+ revenue CAGR, raised and beaten FY26 guidance, a new $1bn buyback, a stock down 32% from a year ago, and a Forward PE (16.67×) sitting below its own 10-year low and 45% below its 10-year average. This is not a marginal or low-quality name being correctly screened out — it's a quality compounder that simply isn't at a price that clears this framework's explicit, non-negotiable Risk/Reward bar today.

3. **The R/R shortfall is not close enough to fudge.** Even the single most favorable combination in the entire standard grid (30% MoS, 25% stop) reaches only 1.71:1 — about 15% short of the 2:1 minimum, and there's no quality- or low-beta-based justification (Experian's beta, 0.824, is near-market, unlike Sage's 0.293 in the precedent session) for tightening the stop beyond the standard band to force a pass. Per the framework's own explicit instruction at this exact decision point, the correct action is to wait for a better entry, not to relax the gate.

4. **What would change this call**: either (a) the price falls toward the 2,136–2,289p buy-ceiling band (a further ~10–16% decline from today's 2,542p, which would also naturally improve the R/R given the unchanged Sell Target), or (b) the Blended FV itself moves up materially on a fundamental trigger (upward EPS/FCF revision at the next results, multiple re-rating in the peer set) without the price moving up in lockstep. Neither requires a new framework rule — both are just the existing Buy Price / R/R mechanics resolving favorably on their own.

**What would change this call (Phase 06 / Rule 9 triggers):**
- Price decline toward the 2,136–2,289p buy-ceiling band on an intact thesis (✅ valid per the framework — "price dropped on intact thesis" is explicitly not a reason to avoid buying, only a reason to avoid *selling*).
- Margin compression — gross margin (42.01%) falling structurally, or ROE (28.26%) falling toward cost of capital (~8%).
- FCF deterioration for 2+ consecutive quarters without explanation.
- Net Debt/EBITDA rising materially above 1.67× toward the 2.5× ceiling.
- Disruption vector materializing — credible evidence of alternative-data/cash-flow underwriting displacing the traditional credit-file model faster than Experian's own data-analytics build-out can offset.
- >15% unexplained move from 2,542.00p (Rule 9) in either direction — re-score immediately.
- Next quarterly results (Experian reports H1 FY27 results around November 2026) — mandatory re-score regardless of price action.

**Qualitative notes (reaffirmed from the 2026-06-19 screening session, [sessions/2026-06-19-screening-europe.md](2026-06-19-screening-europe.md)):**
- **Margins**: one of only three global consumer/commercial credit bureaus (with Equifax and TransUnion) — an oligopoly built on decades of proprietary credit-file data, regulatory accreditation (FCRA and equivalents), and exclusive data-furnisher relationships with lenders.
- **Moat**: replicating decades of credit-file depth, lender relationships, and regulatory accreditation is practically impossible for a new entrant; the bureau industry has had the same three incumbents for decades.
- **Capital allocation**: consistent bolt-on M&A in data/analytics (Serasa/LatAm, fraud/ID analytics), steady dividend growth plus buybacks (new $1bn buyback with FY26 results), organic reinvestment in cloud data platforms (Ascend).
- **Growth drivers**: consumer services (credit monitoring/identity protection), fraud/identity analytics, B2B decisioning software, continued penetration of under-bureaued emerging markets (Brazil, India). FY27 guidance: 6-8% organic, 8-11% total revenue growth, double-digit Benchmark EPS growth.
- **Bear case**: meaningful revenue tracks consumer-lending origination volumes (mortgage, auto) — cyclical to the credit cycle and rate environment; alternative-data/cash-flow underwriting and open-banking regimes are a longer-term threat to the traditional credit-file model; privacy/data-use regulation is a perpetual tail risk.
- **Disruption vector**: moderate, monitored — Experian is itself acquiring/building alternative-data capabilities rather than being disrupted from outside.

**Process note:** this session documents the analytical recommendation only. No broker order has been placed and nothing has been logged in `decisions/` or `portfolio/holdings.md` — those steps follow only once a trade is actually executed. IBKR access in this environment is read-only in any case.

---

## 10. Next Review Trigger

- **H1 FY27 results** (expected ~November 2026) — mandatory re-score (Rule 9). Re-check: (a) organic revenue growth vs. the 6-8% FY27 guidance, (b) FCF trend and FCF/NI conversion, (c) Net Debt/EBITDA trend (now 1.67×, plenty of headroom to the 2.5× ceiling), (d) EPS growth continuation (watch for whether FY27 breaks or extends the Fast Grower 3-year chain).
- **Price decline into the 2,136–2,289p buy-ceiling band** — would flip the recommendation toward "set limit order" or "enter now," subject to a fresh R/R check at that price (which would also improve mechanically as entry falls toward an unchanged Sell Target).
- **>15% unexplained price move from 2,542.00p** (Rule 9) — immediate re-score in either direction.
- **Quarterly Rate Environment Gate update** (next: ~Jul 2026) — the Step 1 Earnings Yield Spread Test is currently a thin pass (+1.55% vs. the +1.5% threshold); a 10Y Treasury move upward of even ~0.1pp combined with no offsetting EPS movement could flip this to a fail (+5 additive), which would push the score to ~37.0 — still within the Cheap band, not a action-changing move, but worth tracking given how close to the line it sits.
- **Any credible alternative-data/cash-flow-underwriting disruption signal** specific to Experian's bureau model.
- **If the order is actually placed** (after a future price decline) → triggers `/sync-portfolio` + `decisions/` entry + watchlist move to `in-portfolio/`.

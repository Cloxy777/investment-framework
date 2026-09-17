# NEW POSITION Session — ASML.AS (ASML Holding N.V.)

**Task type:** NEW POSITION
**Date:** 2026-09-17
**10Y US Treasury yield:** 4.955% (`^TNX` close, 2026-09-17)
**Rate Regime Modifier in effect:** +5 (3.5–5% bracket) — see Rate Environment Gate below for the combined +10 total (Step 1 + Step 2).

---

## 🚨 Prominent duplicate-entity flag — ASML.AS is the SAME legal entity as the already-tracked "ASML" ticker

Before treating this as a fresh independent candidate, the required holdings/duplicate check surfaced a significant finding, flagged here exactly as instructed (parallel to the Novo Nordisk/NVO duplicate-entity finding from an earlier session in this batch):

- **`ASML.AS` (Euronext Amsterdam, EUR) and `ASML` (Nasdaq, USD) are the identical global ordinary share of ASML Holding N.V.** — not a parent/subsidiary relationship, and not even a conventional depositary-receipt structure. ASML's Nasdaq listing trades via a **NY Registry Share**, which represents the underlying Amsterdam-listed ordinary share 1-for-1 with no separate depositary-bank certificate — arguably an even tighter "same instrument, two tickers" case than a typical ADR/ordinary pair (see the existing **NY Registry Share** glossary entry).
- **This exact company already has an active, current watchlist entry** at `watchlist/not-in-portfolio/ASML/` (ticker `ASML`, Nasdaq/USD), most recently updated **2026-09-11 — six days before this session** — with a full fresh re-run: Quality Score 82.4, Valuation Score 94.6, Composite Score 56.1, **WATCHLIST ONLY** (Hold band). Two earlier entries (2026-07-12, 2026-07-15) are also on file. `ASML` is **not held** in `portfolio/holdings.md`.
- Live-price cross-check confirms this is the same instrument: `ASML.AS` closed today at **€1,418.00**; at today's live EUR/USD rate (1.147974) that converts to **≈$1,628** on the Nasdaq leg — a plausible ~5% pullback from the $1,717.30 print recorded in the 2026-09-11 `ASML` session, consistent with ordinary cross-listing price action, not a different company.
- **Recommendation to the user:** consolidate tracking under a single ticker (`ASML`, the existing Nasdaq folder, already has three dated entries and richer history) rather than maintaining two parallel `ASML` / `ASML.AS` watchlist folders for the same company going forward. This session still completes a full, independently-sourced evaluation per the task's explicit instructions (below), but the sub-score drift versus the six-day-old `ASML` session (detailed inline) is itself evidence of why duplicate tracking under two tickers is undesirable — it invites two independently-computed, slightly-inconsistent "current" scores for one company.

This session proceeds with the full evaluation as instructed, using freshly fetched `ASML.AS` (EUR-denominated) data throughout, and cross-references the existing `ASML` entries only where explicitly noted.

**Holdings check:** `portfolio/holdings.md` confirmed — no `ASML`, `ASML.AS`, or any ASML Holding N.V. entity appears in current holdings. Not a live position under any ticker.

---

## Step 1 — Live Price (Rule 0)

Fetched via `yf.Ticker("ASML.AS").info` at session time, 2026-09-17:

- **Live price: €1,418.00** (`currentPrice` / `regularMarketPrice`, EUR, Euronext Amsterdam)
- Previous close: €1,396.20
- 52-week range: €747.10 – €1,741.00
- Analyst mean price target: €2,044.69 (consensus "buy," per `info`)
- Market Cap: €544,653.8M | Enterprise Value: €530,683.3M
- Shares outstanding: 384.1M

No price was inferred from multiples — fetched live and first, per Rule 0.

---

## Step 2 — Phase 01 Quality Score

All inputs pulled live via `yfinance` (`t.info`, `t.financials`, `t.quarterly_financials`, `t.cashflow`, `t.quarterly_cashflow`, `t.balance_sheet`, `t.quarterly_balance_sheet`) for `ASML.AS`. TTM window = Q3 2025–Q2 2026 (most recent 4 reported quarters) for income-statement figures.

**Data gap flagged:** `t.quarterly_cashflow` for `ASML.AS` currently returns data only through Q1 2026 (2026-03-31) — Q2 2026 cash-flow-statement data has not yet been posted to Yahoo's dataset, even though the income-statement quarterly data (`t.quarterly_financials`) already includes Q2 2026. Rather than invent or backfill the missing quarter, this session computes all cash-flow-derived figures (FCF, FCF/NI ratio, FCF Yield) on the most recent **fully available** TTM cash-flow window, **Q2 2025–Q1 2026** — one quarter lagged versus the income-statement TTM window. This is disclosed explicitly wherever it applies below, and is the reason this session's FCF/NI and FCF-yield figures differ somewhat from the six-days-prior `ASML` (Nasdaq) session, which evidently had access to a fresher cash-flow quarter at its data-pull time.

### Revenue / Income TTM (Q3 2025–Q2 2026)
| Quarter | Revenue (€M) | EBIT (€M) | EBITDA (€M) | Net Income (€M) | Gross Profit (€M) |
|---|---|---|---|---|---|
| Q3 2025 | 7,516.0 | 2,468.4 | 2,743.0 | 2,124.5 | 3,880.3 |
| Q4 2025 | 9,718.1 | 3,431.1 | 3,686.3 | 2,839.6 | 5,068.6 |
| Q1 2026 | 8,766.9 | 3,157.8 | 3,157.8 | 2,756.7 | 4,645.0 |
| Q2 2026 | 9,326.5 | 3,456.1 | 3,456.1 | 2,917.6 | 5,035.4 |
| **TTM** | **35,327.5** | **12,513.4** | **13,043.2** | **10,638.4** | **18,629.3** |

### Cash flow TTM (Q2 2025–Q1 2026, most recent fully-available window — see data-gap note)
| Quarter | FCF (€M) | Net Income (€M) |
|---|---|---|
| Q2 2025 | 318.8 | 2,290.3 |
| Q3 2025 | 243.7 | 2,124.5 |
| Q4 2025 | 10,939.9 | 2,839.6 |
| Q1 2026 | −2,607.9 | 2,756.7 |
| **TTM** | **8,894.5** | **10,011.1** |

### Balance sheet (most recent quarter, Q2 2026)
Total Debt €1,984.4M · Cash €6,671.9M → **Net Debt = −€4,687.5M (net cash)**
Stockholders' Equity €21,825.4M

### Effective tax rate (TTM, Q3 2025–Q2 2026)
Tax Provision €2,217.1M ÷ Pretax Income €12,614.9M = **17.58%**

### ROIC
NOPAT = EBIT × (1 − tax rate) = 12,513.4 × (1 − 0.1758) = **€10,312.5M**
Invested Capital = Total Debt + Stockholders' Equity − Cash = 1,984.4 + 21,825.4 − 6,671.9 = **€17,137.9M**
**ROIC = 10,312.5 / 17,137.9 = 60.16%**

### Sub-score calculations

**Profitability (25% weight):**
```
NetMargin_Component = clamp((30.12/30)×100, 0, 100) = 100.0  (net margin 10,638.4/35,327.5 = 30.12%)
ROIC_Component       = clamp((60.16/30)×100, 0, 100) = 100.0
Profitability_Score  = (100.0 + 100.0)/2 = 100.0
```
No FCF-positive-3yr cap applies — FCF positive in FY2022, FY2024, FY2025 (and materially positive TTM despite one weak quarter); see hard-disqualifier check below.

**Margins (15% weight):**
```
GrossMargin_Score = clamp((52.73/80)×100, 0, 100) = 65.91   (gross margin 18,629.3/35,327.5 = 52.73%)
```
No structural-trend bonus applied — gross margin has been broadly flat (52–55% range) over the trailing years, not a clear expansion trend from a sub-40% base.

**Growth (20% weight):**
```
Revenue 3yr CAGR = (32,667.3M FY2025 ÷ 21,173.4M FY2022)^(1/3) − 1 = 15.54%
Growth_Score = clamp((15.54/25)×100, 0, 100) = 62.16
```
**+10 TAM/pricing-power modifier applied** — documented evidence: ASML's own 2030 Investor Day framework (€44–60B revenue target vs. current €35.3B TTM), the FY2026 guidance raise to €43–45B (from €36–40B, disclosed 2026-07-15, unchanged since), record order backlog, and continued High-NA EUV ASP premium pricing (same evidence base cited in the prior `ASML` sessions, re-verified here against ASML's own investor-relations materials — no contradicting evidence found).
```
Growth_Score = 62.16 + 10 = 72.16
```

**Balance Sheet (15% weight):**
```
Net Debt/EBITDA = −4,687.5 / 13,043.2 = −0.359×   (net cash)
BalanceSheet_Score = clamp(100 × (1 − (−0.359)/4), 0, 100) = clamp(108.99, 0, 100) = 100.0
```

**Moat Signal (15% weight)** — checklist, cited evidence only:
| Signal | True/False | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | Sole global supplier of EUV lithography systems (~100% share of the EUV segment) — third-party industry coverage (SEMI, TechInsights) and ASML's own disclosures. |
| Brand premium | **TRUE** | Documented ASP premium for High-NA EUV systems over standard EUV, disclosed in ASML's own investor materials. |
| Network effect | FALSE | No documented two-sided-market mechanism. |
| Switching costs | **TRUE** | Fabs are architected around ASML's specific tool specifications; multi-year system installation/qualification cycles create extreme switching costs — documented mechanism, consistent with prior sessions. |
| Scale cost advantage | FALSE | No citable cost-per-unit comparison exists — no competitor operates at comparable scale in EUV to compare against. |
```
Moat_Score = (3/5) × 100 = 60.0
```

**FCF Quality (10% weight):**
```
FCF/NI ratio (TTM, Q2 2025–Q1 2026) = 8,894.5 / 10,011.1 = 88.85%
FCFQuality_Score = clamp(((0.8885 − 0.40)/0.60) × 100, 0, 100) = 81.42
```

### Hard disqualifier check
- FCF/NI < 70% for 2+ consecutive years? **No** — annual FCF/NI: FY2022 127.4%, FY2023 41.4% (single isolated dip, not 2 consecutive years), FY2024 120.0%, FY2025 114.8%. **Does not fire.**
- Net Debt/EBITDA over threshold? **No** — net cash (−0.359×), far under the 2.5× standard threshold. **Does not fire.**
- Not FCF-positive 3+ consecutive years? **No** — FCF positive every fiscal year FY2022–FY2025. **Does not fire.**

**No hard disqualifier fires.**

### Final Quality Score
```
Quality Score = (100.0×0.25) + (65.91×0.15) + (72.16×0.20) + (100.0×0.15) + (60.0×0.15) + (81.42×0.10)
              = 25.00 + 9.8865 + 14.432 + 15.00 + 9.00 + 8.142
              = 81.4605 → rounds to 81.5
```

**Quality Score: 81.5 — clears the 80.0+ gate.** Proceeding to Phase 02.

*(Cross-reference: the 2026-09-11 `ASML` session computed Quality Score 82.4 off a slightly different FCF/NI figure — a fresher cash-flow quarter than was available to this session, per the data-gap note above. The ~0.9-point difference is fully explained by that one-quarter cash-flow lag; every other sub-score matches closely.)*

---

## Step 3 — Rate Environment Gate + Phase 02 Valuation Score

### Rate Environment Gate
**Step 1 — Earnings Yield Spread Test:**
Forward PE uses the FY2026 ("0y") consensus EPS estimate, **not** `yfinance`'s raw `forwardEps`/`forwardPE` fields — those returned the FY2027 ("+1y") consensus (€51.72) rather than the correct next-fiscal-year estimate (€38.325, "0y", 31 analysts), a known `yfinance` field-mapping quirk on this ticker (cross-checked via `t.earnings_estimate`).
```
Forward PE = €1,418.00 / €38.325 = 37.00×
EY = 1 / 37.00 = 2.703%
Spread = 2.703% − 4.955% (10Y) = −2.252pp < +1.5% → Step 1 FAILS → +5
```
**Step 2 — Rate Regime Modifier:** 10Y = 4.955%, in the 3.5–5% bracket → **+5**
**Combined Rate Environment Gate modifier: +10**

### Phase 02 sub-scores

**FCF Yield (40% weight):**
```
FCF Yield = €8,894.5M (TTM, Q2 2025–Q1 2026) / €544,653.8M market cap = 1.633%
FCF_Score = clamp(100 × (1 − 1.633/10), 0, 100) = 83.67
```

**EV/EBIT (weight 40% — see PEG note below):**
```
EV/EBIT = €530,683.3M / €12,513.4M (TTM EBIT) = 42.41×
EV/EBIT_Score = clamp((42.41 − 12)/23 × 100, 0, 100) = clamp(132.2, 0, 100) = 100.0  (capped)
```

**Forward PE + Historical PE Modifier (20% weight):**
5-year trailing PE series reconstructed via `t.get_earnings_dates(limit=40)` + rolling TTM EPS + contemporaneous price (per valuation-scoring.md method), 20 quarters (2021-07 through 2026-07):
```
5yr Avg PE = 39.35× | 5yr Low PE = 25.18× | 5yr High PE = 56.38×
FwdPE_Score (primary, range available) = clamp((37.00 − 25.18)/(56.38 − 25.18) × 100, 0, 100) = 37.88
Deviation from 5yr avg = (37.00 − 39.35)/39.35 = −5.97% → within ±10% → Historical PE Modifier = 0
FwdPE_Score = 37.88 + 0 = 37.88
```
*(Note: this session's independently-reconstructed 5yr PE range (39.35× avg / 25.18–56.38× range) differs somewhat from the 2026-09-11 `ASML` session's cited 38.33× avg / 49.28× high — expected, since the rolling 20-quarter window shifts slightly with each day's new price data and the reconstruction is sensitive to which trading day's close pairs with each earnings date. Both are legitimately "current" reconstructions; this is exactly the kind of drift the duplicate-entity flag above warns about.)*

**PEG (Fast Grower eligibility check):** EPS growth >15%/yr for 3+ years on a *clean, reliable* base is required. Diluted EPS: FY2022 €16.07 → FY2023 €20.59 (+28.1%) → FY2024 €19.24 (**−6.6%**) → FY2025 €24.71 (+28.4%). The FY2024 decline breaks a reliable, monotonic >15%/yr pattern — **ASML does not qualify as a Fast Grower under the "reliable base" clarification** (2026-06-20), despite a 3yr CAGR (15.4%) that nominally clears 15%. **PEG's 15% weight is redistributed to EV/EBIT** (EV/EBIT weight → 40%, as used above).

**Upside/Downside Modifier:**

PW Fair Value: rather than re-derive an independent DCF+multiples blend for the same legal entity from scratch six days after the `ASML` (Nasdaq) session already built one (per the duplicate-entity flag above — re-deriving a second, inconsistent fair-value estimate for the identical company within the same week is exactly the fragmentation risk that flag warns about), this session converts that session's PW Fair Value to EUR at the live exchange rate and confirms no Rule 9 trigger has fired in the interim to invalidate it:
```
2026-09-11 ASML session PW Fair Value = $951.70/share (unchanged inputs: no earnings, no guidance
  revision, no M&A, no management change since; next earnings confirmed 14 Oct 2026)
Live EUR/USD = 1.147974 (2026-09-17)
PW Fair Value (EUR) = $951.70 / 1.147974 = €829.14
```
```
Gap Upside % = (€829.14 / €1,418.00) − 1 = −41.53%
Catalyst window: no narrower catalyst identified within the window → use 2yr default (Rule 10)
Annualized gap = −41.53% / 2 = −20.77%
```
Intrinsic growth (EPS CAGR) — computed independently from this session's own verified annual diluted EPS (FY2022 €16.07 → FY2025 €24.71), **not** imported from the prior session's +20.48% figure, which could not be reconciled against publicly available annual EPS data within this session's data access:
```
Intrinsic growth = (24.71/16.07)^(1/3) − 1 = 15.42%
```
Shareholder yield, computed from FY2025 actuals:
```
Dividend yield = €7.78 (dividendRate) / €1,418.00 = 0.549%
Net buyback yield = €5,807.7M (FY2025 net common stock issuance, buybacks net of issuance) / €544,653.8M market cap = 1.066%
Shareholder yield = 0.549% + 1.066% = 1.615%
```
```
E = Annualized gap + intrinsic growth + shareholder yield
  = −20.77% + 15.42% + 1.615% = −3.735%/yr
```
E < 0 (expected annual loss):
```
M = +5 + 10 × clamp((−E)/10pp, 0, 1) = +5 + 10 × clamp(3.735/10, 0, 1) = +5 + 3.735 = +8.735
```

### Final Valuation Score
```
Final Score = (FCF_Score×0.40) + (EV/EBIT_Score×0.40) + (FwdPE_Score×0.20) + Rate Modifier + Upside/Downside Modifier
            = (83.67×0.40) + (100.0×0.40) + (37.88×0.20) + 10 + 8.735
            = 33.47 + 40.00 + 7.58 + 10 + 8.735
            = 99.78 → rounds to 99.8
```

**Valuation Score: 99.8** (near the 100.0 ceiling — expensive across nearly every lens; confirms the pre-screen expectation given ASML's ~39–42× EV/EBIT).

### Composite Score
```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 81.5) + 0.50 × 99.8
                = 0.50 × 18.5 + 0.50 × 99.8
                = 9.25 + 49.90
                = 59.15 → falls exactly on a ".X5" boundary → round UP (conservative) → 59.2
```

**Composite Score: 59.2** — falls in the **50.0–69.9 "Fair Value" band**. Consistent (same Hold band) with the `ASML` (Nasdaq) session's 56.1 despite the sub-score-level drift documented above — the two independent evaluations of the same company reach the same qualitative conclusion.

---

## Step 4 — Fair Value / Order Setup

**Not applicable.** Composite Score 59.2 sits in the 50.0–69.9 band — per fair-value-methodology.md's Buy Price integration table, this band carries **"No MoS → Watchlist only"** and per strategy.md Phase 03, **no new entry**. No Buy Price, Sell Target, Stop Loss, R/R, or position size are computed — none of that machinery activates outside the Buy/Trim bands, and producing one here would imply an action this score doesn't support.

---

## Step 5 — Recommendation

**WATCHLIST ONLY — no new entry, no order setup.**

Composite Score 59.2 falls in the Phase 03 "Fair Value" band (50.0–69.9): *"Watchlist only — no new entry."* ASML clears the Quality Score gate comfortably (81.5, exceptional Profitability/Balance-Sheet/Growth fundamentals — sole-supplier EUV monopoly, net cash, ~60% ROIC) but is priced for that quality: Valuation Score 99.8, near the ceiling, driven by a saturated EV/EBIT (42.4×, capped), a rich Forward PE relative to its own 5-year range, and an Upside/Downside Modifier that adds rather than subtracts (expected annual return of roughly **−3.7%/yr** against the framework's 10% hurdle — the current price already exceeds even the bull-case scenario-weighted fair value by a wide margin). This matches the task's own pre-screen expectation (EV/EBITDA ~39× flagged as expensive) and is directionally identical to the existing `ASML` (Nasdaq) watchlist entries, which have never left the Hold band across three sessions since 2026-07-12.

**No trade placed or recommended.** This is a paper evaluation only — no IBKR order has been created, and no action is required in `decisions/`.

---

## Next review trigger

Q3 2026 earnings, confirmed for **14 October 2026** (Rule 9 mandatory trigger) — will refresh the TTM window for both `ASML` and `ASML.AS` for the first time since Q2 2026, and by then `t.quarterly_cashflow` should have caught up with the Q2 2026 cash-flow statement, closing this session's one-quarter cash-flow lag. Any guidance revision, management change, M&A, or >15% unexplained move from €1,418.00. **Recommend consolidating future `/rescore`/`/new-position` runs on this company under a single ticker** (the existing `ASML` folder) rather than continuing to maintain both `ASML` and `ASML.AS` as parallel, independently-scored entries.

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Every term below is already defined there (no new terms required this session):

| Term | Meaning |
|---|---|
| **Composite Score** | This framework's single ranking number (0.0–100.0, 0.0 = most attractive) blending the Quality Score and the Valuation Score 50/50. |
| **CAPM (Capital Asset Pricing Model)** | A formula estimating a stock's required return as the risk-free rate plus Beta times the Equity Risk Premium. |
| **DCF (Discounted Cash Flow)** | A valuation method estimating a company's worth today by projecting future cash flow and discounting it back to present value. |
| **EUV (Extreme Ultraviolet Lithography)** | The most advanced chip-manufacturing lithography technology; ASML is the sole global manufacturer of EUV systems. |
| **EV/EBIT** | Enterprise Value divided by EBIT — a multiple measuring how expensive a company is relative to its operating profit. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, expressed as a yield so it can be compared against bond yields. |
| **Earnings Yield Spread Test** | Step 1 of the Rate Environment Gate: EY minus the 10-Year Treasury yield. |
| **Fast Grower** | Peter Lynch's term for a company growing EPS faster than 15%/year for 3+ years — this framework's trigger for applying the PEG sub-score. ASML does not currently qualify (a down year breaks the "reliable base" requirement). |
| **FCF Yield** | Free Cash Flow ÷ Market Cap; higher means cheaper. |
| **Forward PE** | Price ÷ next-twelve-months expected earnings per share. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of its weighted score; none fired for ASML. |
| **Historical PE Modifier** | Hybrid Upgrade 2: an additive adjustment to the Forward PE sub-score based on where the current multiple sits versus the trailing 5-year PE. |
| **MoS (Margin of Safety)** | How far below fair value the buy price is set — not applicable this session (Hold band, no order setup). |
| **Moat** | A durable competitive advantage protecting a business's profits from competitors. |
| **Net Debt/EBITDA** | A leverage ratio; negative means net cash. ASML is at −0.359×. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate); the numerator used to compute ROIC. |
| **NY Registry Share** | A form of direct US listing (used by ASML on Nasdaq) representing the underlying home-market ordinary share 1-for-1, without a conventional ADR's depositary-bank structure — central to this session's duplicate-entity flag. |
| **PEG ratio** | PE ratio ÷ earnings growth rate. |
| **Quality Score** | This framework's 0.0–100.0 continuous quality grade; 80.0+ required to proceed to valuation scoring. ASML.AS scores 81.5. |
| **Rate Environment Gate** | The mandatory pre-check before Phase 02 scoring. |
| **Rate Regime Modifier** | An additive adjustment (−10 to +10) based on the current Treasury-yield bracket. |
| **ROIC** | Return on Invested Capital. ASML.AS computes at 60.16% this session. |
| **Rule 9** | Fundamental events that force an immediate re-valuation. |
| **Shareholder yield** | Dividend yield plus net buyback yield combined. |
| **TAM (Total Addressable Market)** | The total revenue opportunity a company could capture if it fully served its market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results. |
| **Upside/Downside Modifier** | An additive ±15 adjustment to the valuation score based on expected annual return; ASML.AS computes at +8.735 this session (expected annual loss ≈ −3.7%/yr). |
| **Valuation score** | This framework's 0.0–100.0 continuous score (0 = cheapest, 100.0 = most expensive). ASML.AS scores 99.8. |
| **WACC (Weighted Average Cost of Capital)** | The discount rate used in a DCF. |

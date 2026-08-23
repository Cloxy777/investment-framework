# NEW POSITION — CTAS (Cintas Corporation)

**Task type:** NEW POSITION
**Date:** 2026-08-23 (a Sunday — US markets closed; per Rule 0, the price below is the most recent available live trade, not a stale multi-day-old figure)
**10Y US Treasury Yield:** 4.74% (2026-08-22 close, most recent trading day — TradingEconomics/CNBC, "yield rose to 4.74% on Friday," testing 20-month highs). Recorded for completeness per the standard session header — **not applied**, since this evaluation stops before the Rate Environment Gate (see below). For reference, 4.74% would fall in the 3.5–5% Rate Regime Modifier bracket (+5) if this session reached Phase 02.

**Trigger:** Automated Telegram-scan (Routine 6) flagged a first-time mention of Cintas Corporation — a post reporting that Trump reportedly bought CTAS shares in June 2026. No watchlist entry existed for CTAS in either `in-portfolio/` or `not-in-portfolio/`, so per `telegram-scan.md` step 4 this is a mandatory first-ever `/new-position` evaluation regardless of the triggering post's substance. **The Telegram post is used only as the trigger — it is not a financial data input.** Every figure below was independently fetched from IBKR, stockanalysis.com, and SEC EDGAR.

---

## Step 1 — Live Price (Rule 0)

Fetched via IBKR **before** any calculation:

- `search_contracts("CTAS")` → contract_id **268149**, NASDAQ, "CINTAS CORP", US primary listing (the MEXI-listed row was excluded as a foreign secondary listing).
- `get_price_snapshot(268149)`:

| Field | Value |
|---|---|
| **Last trade price** | **$203.79** |
| Prior close | $203.52 |
| Change | +$0.27 (+0.13%) |
| 52-week high / low | $219.16 / $160.73 |
| Dividend yield | 0.92% |

**Live Price used throughout this session: $203.79.** Not inferred from any multiple — fetched directly.

---

## Step 2 — Phase 01 Quality Score

Per [quality-scoring.md](../framework/quality-scoring.md) (methodology version 2026-06-29). All inputs sourced from stockanalysis.com (financials/balance-sheet/cash-flow/ratios pages, WebFetch) and cross-checked internally (see cross-checks below); qualitative moat/TAM evidence additionally checked against Cintas's FY2026 Form 10-K (filed 2026-07-29, SEC EDGAR, accession 0000723254-26-000028) and third-party sources, cited individually.

Cintas's fiscal year runs 1 June–31 May. **FY2026 (ended 31 May 2026)** is the latest complete, audited fiscal year — used as the TTM basis throughout (no newer quarter has been reported; fiscal Q1 FY2027 is due in late September).

### Raw financial data (FY2022–FY2026, stockanalysis.com)

| Metric | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| Revenue | $7,854M | $8,816M | $9,597M | $10,340M | $11,265M |
| Gross Profit / Margin | $3,632M / 46.24% | $4,173M / 47.34% | $4,686M / 48.83% | $5,174M / 50.04% | $5,708M / 50.67% |
| Operating Income (EBIT) | $1,587M | $1,803M | $2,069M | $2,360M | $2,622M |
| Net Income / Margin | $1,230M / 15.65% | $1,343M / 15.23% | $1,566M / 16.31% | $1,806M / 17.46% | $1,994M / 17.70% |
| Operating Cash Flow | $1,538M | $1,586M | $2,069M | $2,166M | $2,276M |
| CapEx | −$241M | −$331M | −$409M | −$409M | −$395M |
| Free Cash Flow | $1,297M | $1,255M | $1,659M | $1,757M | $1,881M |
| FCF/NI conversion | 105.4% | 93.4% | 105.9% | 97.3% | 94.3% |
| Total Debt | $2,968M | $2,668M | $2,668M | $2,654M | $2,706M |
| Cash | $90M | $124M | $342M | $264M | $289M |
| Net Debt | $2,878M | $2,544M | $2,326M | $2,391M | $2,417M |
| Shares Outstanding | 406.8M | 406.9M | 405.0M | 403.0M | 400.2M |
| ROIC | 21.53% | 22.79% | 25.24% | 27.54% | 27.76% |
| Net Debt/EBITDA | 1.53× | 1.21× | 0.97× | 0.88× | 0.81× |

**Cross-checks (internal consistency, not invented):**
- EV = Market Cap + Net Debt = (400.17M × $203.79 = $81,550.6M) + $2,417M = **$83,967.6M** — matches stockanalysis.com's independently-stated EV ($83.97B) to the dollar.
- EBITDA implied by EV/EBITDA 28.04× = $83,967.6M / 28.04 = $2,994.6M → Net Debt/EBITDA = $2,417M/$2,994.6M = 0.807× — matches the site's stated 0.81× (rounding).
- EV/EBIT = $83,967.6M / $2,622M = 32.02×, matches the site's independently-stated 32.03× (rounding).

**Hard disqualifier check (quality-scoring.md):**
- FCF/NI conversion <70% for 2+ consecutive years: **No** — every year FY2022–FY2026 is 93.4%–105.9%, comfortably above 70%.
- Net Debt/EBITDA over threshold (2.5× standard): **No** — 0.81×, far below.
- Not FCF-positive for 3+ consecutive years: **No** — FCF positive all 5 years shown.
- Share issuance pattern: **Not dilutive** — shares outstanding declined 406.8M → 400.2M (net buybacks).

**No hard disqualifier fires.**

### Sub-score calculations

**Profitability (25% weight)**
```
NetMargin_Component = clamp((17.70/30)×100, 0, 100) = 59.00
ROIC_Component       = clamp((27.76/30)×100, 0, 100) = 92.53
Profitability_Score  = (59.00 + 92.53) / 2 = 75.77   (no FCF-positivity cap — 5yr positive)
```

**Margins (15% weight)**
```
GrossMargin_Score = clamp((50.67/80)×100, 0, 100) = 63.34
```
Gross margin has expanded every year for 5 straight years (46.24% → 50.67%) — a genuine structural trend. The Margins formula's trend bonus (+10) only applies when margin is *below* 40% but trending up; CTAS is already at 50.67%, so no bonus applies (the expansion is instead captured directly in the higher base score).

**Growth (20% weight)**
```
Revenue 3yr CAGR (FY2023 $8,816M → FY2026 $11,265M) = (11,265/8,816)^(1/3) − 1 = 8.52%
Growth_Score (base) = clamp((8.52/25)×100, 0, 100) = 34.10
```
**TAM/pricing-power modifier — evidence and judgment call shown in full:**
- *For a +10 modifier:* Third-party sources (Yahoo Finance/Barchart-sourced analysis, "Wall Street's Favorite Uniform Rental Stock Just Proved Why It Commands a 55% Valuation Premium," and Investing.com's "Building a Juggernaut: The Cintas-UniFirst Merger") document Cintas holding roughly 27–31% of the ~$20B US uniform rental market — nearly 3× its largest public rival (UniFirst, ~12–14%) — and a pending $5.5B UniFirst acquisition (closing H2 2026) that would push combined share toward ~45%, expanding Cintas's addressable share of the market. The same Yahoo Finance analysis attributes Cintas's 55% P/E premium over UniFirst (41.65× vs 26.83×) to a "premium pricing strategy," "customers who value reliability and pay for it," and 20 consecutive quarters of beating earnings estimates.
- *Against it:* Cintas's own FY2026 10-K (primary source) uses materially more conservative language — it describes its markets as "highly fragmented," does **not** claim market leadership, and explicitly lists limited pricing power as a risk factor ("competitive conditions or contractual arrangements may limit our ability to pass increased costs on to customers in a timely manner, or at all").
- **Judgment applied:** the 10-K's language is standard risk-factor boilerplate (SEC filings routinely disclaim pricing power as a legal hedge, not as an empirical claim that pricing power is absent), while the market-share/consolidation and premium-multiple facts above are corroborated across multiple independent third-party sources and are the more specific, falsifiable claims. **+10 modifier applied**, with this tension disclosed rather than hidden.
```
Growth_Score = 34.10 + 10 = 44.10
```
*(Sensitivity: without the modifier, Growth_Score = 34.10 and the final Quality Score would be 68.3 instead of 70.3 — see bottom line below. Either way the gate result is unchanged.)*

**Balance Sheet (15% weight)**
```
BalanceSheet_Score = clamp(100 × (1 − 0.81/4), 0, 100) = 100 × (1 − 0.2025) = 79.75
```
No asset-light override needed (Cintas is far under even the standard 2.5× threshold).

**Moat Signal (15% weight)** — checklist, each signal cited:

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | ~27–31% US uniform-rental market share, ~3× nearest public rival (UniFirst); expanding further via pending $5.5B UniFirst acquisition (H2 2026 close) — Yahoo Finance/Barchart analysis; Investing.com merger analysis |
| Brand premium | **TRUE** | 55% P/E premium vs. UniFirst (41.65× vs 26.83×) attributed to a "premium pricing strategy" and "customers who value reliability and pay for it," plus 20 consecutive quarters of earnings beats — Yahoo Finance analysis |
| Network effect | **FALSE** | No two-sided marketplace dynamic exists in this business — uniform/facility-services rental is a linear service model. No evidence found or claimed anywhere. |
| Switching costs | **TRUE** | Documented mechanism: national-scale-plus-local-route-density model (12,500 local delivery routes, 484 operational facilities, 12 distribution centers per the FY2026 10-K) combined with a broad integrated product catalog (uniforms, mats, first aid, restroom supplies) creates logistical/contractual switching friction for a customer to replicate elsewhere |
| Scale cost advantage | **TRUE** | Route density reduces per-customer logistics cost — a documented mechanism given Cintas's disclosed national route/facility scale (10-K) versus smaller regional competitors; corroborated by third-party competitive analysis |

```
Moat_Score = (4/5) × 100 = 80.0
```

**FCF Quality (10% weight)**
```
FCF/NI (FY2026) = $1,881M / $1,994M = 94.33%
FCFQuality_Score = clamp(((0.9433 − 0.40)/0.60)×100, 0, 100) = 90.56
```

### Final Quality Score

```
Quality Score = (75.77 × 0.25) + (63.34 × 0.15) + (44.10 × 0.20) + (79.75 × 0.15) + (80.0 × 0.15) + (90.56 × 0.10)
              = 18.9417 + 9.5006 + 8.8192 + 11.9625 + 12.0000 + 9.0557
              = 70.2797
              → rounds to 70.3
```

**Quality Score = 70.3 / 100.0 — FAILS the 80.0+ gate by 9.7 points.** (Sensitivity check: even crediting the more conservative reading of the Growth modifier — i.e. no +10 — the score is 68.3, still well short of 80.0. The gate result does not depend on that judgment call.)

No hard disqualifier independently fires — this is a pure weighted-score failure, not a balance-sheet or cash-flow-quality breakdown. The drag comes primarily from the Growth sub-score (34.10–44.10, reflecting real but moderate ~8.5% revenue growth well under the framework's 25% reference ceiling) and, secondarily, the Margins sub-score (63.34 — solid but not exceptional gross margin relative to the 80% reference ceiling).

---

## Step 3 — Stop: Not Proceeding to Phase 02

Per [quality-scoring.md](../framework/quality-scoring.md) and `.claude/commands/new-position.md` step 2: **a company must score 80.0+ to be eligible for Phase 02 valuation scoring at all.** CTAS scores 70.3 (or 68.3 under the more conservative growth-modifier reading) — below the gate. **This session stops here.** No Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work is performed or attempted, consistent with how this framework has handled every other Phase 01 FAIL (e.g. MCD 2026-06-24/2026-07-10, HNHPF 2026-07-06).

### Reference data gathered (not scored — for completeness / future re-evaluation only)

These Phase 02 inputs were already pulled as part of due-diligence and are recorded here for transparency and to save re-fetching if CTAS is ever re-evaluated, but **none of them were used in any calculation** since the gate wasn't cleared:

| Metric | Value | Source |
|---|---|---|
| Forward PE | 37.13× | stockanalysis.com |
| Trailing PE | 41.51× (cross-check: $203.79/$4.91 EPS = 41.50×) | stockanalysis.com |
| Trailing PE by fiscal year-end (FY22–FY26) | 33.15× / 35.77× / 43.94× / 50.64× / 41.51× | stockanalysis.com |
| 5yr avg / low / high PE (proxy from above) | ~41.0× / 33.15× / 50.64× | Derived from above |
| EV/EBIT | 32.02–32.03× | Computed + stockanalysis.com |
| EV/EBITDA | 28.04× | stockanalysis.com |
| PEG ratio | 3.19× | stockanalysis.com |
| EPS growth (FY23→FY26) | 11.59% / 16.61% / 16.10% / 11.59% | stockanalysis.com — **not** a Fast Grower (needs >15% for 3+ *consecutive* years; only 2 of the last 4 years clear 15%, and the most recent year is 11.59%) — PEG would not have applied even if Phase 02 were reached |
| Market Cap | ~$81.55B | 400.17M shares × $203.79 |
| Enterprise Value | ~$83.97B | Market Cap + Net Debt |
| Analyst consensus | Buy (20 analysts), PT $216.31 (+6.1% from live price) | stockanalysis.com |

---

## Recommendation

**PASS.** Cintas is a genuinely high-quality, well-run business (94–106% FCF/Net-Income conversion every year for 5 years, 27–28% ROIC, steadily expanding gross margin, minimal leverage, real evidence of market dominance and pricing power), but this framework's strict 80.0+ Quality Score gate — set deliberately high on 2026-06-29 — is built to screen for exceptional growth alongside quality, and CTAS's real but moderate ~8.5% revenue growth is the main thing keeping it from clearing that bar. **No position is opened. No valuation score is computed. No order setup is produced.** This is not a rejection of Cintas as a business — it is a statement that it doesn't meet this specific framework's quality bar as currently calibrated.

**Next review trigger:** No routine re-check scheduled (Phase 01 FAIL — no numeric Phase 02 score to go stale). Re-evaluate on a Rule 9-style fundamental trigger: (a) a sustained re-acceleration in revenue growth (3yr CAGR materially above the current ~8.5%, e.g. from the pending UniFirst acquisition closing and being consolidated — a material M&A event in its own right, warranting re-evaluation once closed); (b) Cintas's fiscal Q1 FY2027 earnings release (expected late September 2026); (c) a management change; (d) a >15% unexplained stock-price move. Absent any of the above, future Telegram mentions of Cintas/CTAS should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CIK (Central Index Key)** | The unique numeric identifier the SEC assigns to every company that files with EDGAR. |
| **Composite Score** | This framework's single ranking number blending the Quality Score and the Valuation Score 50/50 — not computed here, since CTAS never clears the Quality Score gate needed to reach it. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **EDGAR** | The SEC's free public online database of every US-registered company's filings (10-K, 10-Q, 8-K) — used here to pull Cintas's FY2026 10-K directly as a primary-source cross-check. |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **EV** | Enterprise Value — a company's total value to all capital providers: market cap + debt − cash. |
| **EV/EBIT, EV/EBITDA** | Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure. |
| **Fast Grower** | Peter Lynch's term for a company growing earnings per share faster than 15%/year for 3+ years — CTAS's uneven 11.6%/16.6%/16.1%/11.6% pattern does not qualify. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. |
| **Fiscal Year (FY)** | A company's 12-month accounting year, which doesn't have to align with the calendar year. Cintas's runs 1 June–31 May. |
| **Forward PE** | Price ÷ next twelve months' expected earnings per share. |
| **Gross Margin** | Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted sub-score total; none fire for CTAS. |
| **Market Cap (Market Capitalization)** | Share price × total shares outstanding — the total value the market currently assigns to a company's equity. |
| **Moat** / **Moat Signal** | A durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors; this framework's 5-point scored checklist version of the concept. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt. |
| **Net Margin** | Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax. |
| **PEG ratio** | PE ratio ÷ earnings growth rate — a PE adjusted for growth, used to judge whether a fast grower's multiple is justified by its growth rate. |
| **Quality Score** | This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading profitability, margins, growth, balance sheet, moat, and FCF quality. A company must score 80.0+ to proceed to Phase 02 valuation scoring. CTAS scores 70.3. |
| **Rate Environment Gate** | The mandatory pre-check run before every Phase 02 valuation score — not reached in this session. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule. |
| **TAM** | Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market. |
| **10-K (Annual Report)** | The annual financial-disclosure report a US public company must file with the SEC, containing full audited financial statements, MD&A, and risk factors. |
| **Treasury yield (10Y)** | The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results — here, CTAS's FY2026 (ended 31 May 2026), the latest complete fiscal year. |

# NEW POSITION — INTU (Intuit Inc.)

**Task type:** NEW POSITION
**Date:** 2026-08-23
**10Y US Treasury Yield:** 4.74% (TradingEconomics, "rose to 4.74% on Friday" 2026-08-21 close — testing 20-month highs; most recent available print, markets closed over the weekend).

**Trigger:** Automated Telegram-scan (Routine 6) flagged a first-time mention of Intuit — the channel author's own earnings-week watchlist commentary naming INTU among "SaaS names recovering from this year's downturn, expecting continued growth." **Checked both `watchlist/in-portfolio/INTU/` and `watchlist/not-in-portfolio/INTU/` directly (`ls` + a repo-wide `find`) before doing anything else** — neither exists; no prior INTU entry anywhere. Per `telegram-scan.md` step 4's first bullet, this is a mandatory first-ever `/new-position` evaluation regardless of the triggering post's substance. **The Telegram post is used only as the trigger — it is not a financial data input.** Every figure below was independently fetched from IBKR, stockanalysis.com, SEC/company earnings sources, and general web search, cited individually.

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

- `search_contracts("INTU")` → contract_id **270662**, NASDAQ, "INTUIT INC", US primary listing (Mexican/Canadian/German secondary listings and the unrelated Intuitive Surgical/Intuitive Machines/Intu Properties matches excluded).
- `get_price_snapshot(270662)`:

| Field | Value |
|---|---|
| **Last trade price** | **$367.50** |
| Prior close | $361.87 |
| Change | +$5.63 (+1.56%) |
| 52-week high / low | $700.30 / $252.84 |
| 13-week high / low | $371.70 / $252.84 |
| 26-week high | $481.70 |
| Dividend yield | 1.31% |

**Live Price used throughout this session: $367.50.** Not inferred from any multiple — fetched directly. Note the 13-week low equals the 52-week low ($252.84) — the trough was recent — and the 13-week high ($371.70) is barely above today's price, meaning the stock has mostly traded sideways just under $370 for the last quarter after a sharp prior decline (52-week high to low is a ~63.9% drawdown; today's price is still ~47.5% below the 52-week high).

---

## 2. Why the stock is down so much — required context before scoring moat/quality

A ~48-64% drawdown from 52-week highs is exactly the kind of move that demands a documented cause (Rule 9 / Rule 10) before any qualitative moat assessment can be trusted. Web search findings (cited):

- Intuit shares fell as much as ~51% in 2026 and ~62% off the July 2025 all-time high (~$813.70), erasing over $131B of market value — driven by a market-wide **AI-disruption narrative** hitting software/SaaS stocks broadly: once AI can explain deductions, classify expenses, and prep filing answers on demand, "guided software" business models look less defensible. [[FinancialContent](https://markets.financialcontent.com/stocks/article/marketminute-2026-4-10-intuit-erases-four-years-of-gains-as-ai-disruptors-and-regulatory-shifts-drive-stock-to-technical-lows)] [[SaaSRise](https://www.saasrise.com/news/intuit-shares-slide-over-50-ytd-as-ai-concerns-cloud-turbotax-and-quickbooks-outlook-0881d6fd-5766-4630-a0f1-d96f8d23d610)]
- **TurboTax-specific headwind:** the IRS's free **IRS Direct File** tool expanded for the 2026 filing season; Intuit **lowered** TurboTax revenue guidance (to $5.277–5.282B from $5.305–5.330B) as total US tax filings fell industry-wide (~30bps, the steepest contraction since COVID). [[TIKR](https://www.tikr.com/blog/intuit-stock-is-down-38-in-2026-analysts-see-42-upside-to-553-target)]
- **Corporate response:** a 17%/~3,000-role global workforce reduction announced with Q3 FY2026 earnings (May 2026); management also accelerated share buybacks (~$3.37B over 9 months, +60% YoY) and halted insider stock sales — both read as a confidence signal, not distress. [[CNBC](https://www.cnbc.com/2026/05/20/intuit-intu-q3-earnings-report-2026-company-cutting-17percent-of-staff.html)] [[Forbes](https://www.forbes.com/sites/tylerroush/2026/06/02/intuit-becomes-sp-500s-worst-performer-this-year-heres-why/)]
- **Despite this, Q3 FY2026 (reported May 2026) beat and Intuit *raised* full-year guidance:** non-GAAP EPS $12.80 (+2.56% vs. estimate), revenue +10.4% YoY; **FY2026 revenue guidance raised to $21.341–21.374B (13–14% growth)**. QuickBooks Online Accounting revenue +22% YoY (driven by "higher effective prices, customer growth and mix shift" — all three simultaneously); QBO Advanced/Intuit Enterprise Suite ("online ecosystem") +~38%; Credit Karma +15% YoY, guided ~19% for FY2026. [[GuruFocus](https://www.gurufocus.com/news/8872871/intuit-intu-reports-strong-q3-earnings-raises-fy-2026-guidance)] [[Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/intuits-earnings-beat-consumer-172700003.html)]

**Bottom line:** the crash is a real, live, unresolved structural debate (AI disrupting tax-prep/bookkeeping software + a specific TurboTax/IRS Direct File headwind) layered on top of a broader software-sector de-rating — **not** a single fundamental break. The core QuickBooks/Credit Karma engine is still accelerating; TurboTax is the segment under genuine pressure. This is carried through explicitly into the Moat signals (§3e), the Growth modifier (§3c), and the DCF bear case (§5.4).

**Next earnings: August 25, 2026 — 2 days from today.** This will report full FY2026 (fiscal year ended July 31, 2026) actuals and initial FY2027 guidance — a mandatory Rule 9 re-valuation trigger, flagged prominently in §8.

---

## 3. Phase 01 Quality Score

Per [quality-scoring.md](../framework/quality-scoring.md) (methodology version 2026-06-29). Intuit's fiscal year runs **1 August – 31 July**; FY2025 (ended 31 July 2025) is the latest complete audited fiscal year, and TTM (through the fiscal quarter ended 30 April 2026) is used for the TTM-specified inputs. All figures from stockanalysis.com (financials/balance-sheet/cash-flow/ratios/statistics pages, WebFetch, 2026-08-23).

### Raw financial data (FY2021–FY2025 + TTM)

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | TTM (Apr '26) |
|---|---|---|---|---|---|---|
| Revenue | $9,633M | $12,726M | $14,368M | $16,285M | $18,831M | $20,925M |
| Revenue growth | 25.45% | 32.11% | 12.90% | 13.34% | 15.63% | 15.07% |
| Gross Profit / Margin | $8,000M / 83.05% | $10,460M / 82.19% | $11,388M / 79.26% | $12,966M / 79.62% | $15,139M / 80.39% | $16,906M / 80.79% |
| Operating Income (EBIT) | $2,531M | $2,634M | $3,141M | $3,853M | $4,938M | $5,749M |
| Net Income / Margin | $2,062M / 21.41% | $2,066M / 16.23% | $2,384M / 16.59% | $2,963M / 18.20% | $3,869M / 20.55% | $4,584M / 21.91% |
| Diluted EPS | $7.56 | $7.28 | $8.42 | $10.43 | $13.67 | $16.35 |
| EPS growth YoY | — | −3.70% | +15.66% | +23.87% | +31.06% | — |
| Operating Cash Flow | — | $3,889M | $5,046M | $4,884M | $6,207M | $7,888M |
| CapEx | — | −$157M | −$210M | −$191M | −$84M | −$133M |
| Free Cash Flow | — | $3,732M | $4,836M | $4,693M | $6,123M | $7,755M |
| FCF margin | — | 29.33% | 33.66% | 28.82% | 32.52% | 37.06% |
| FCF/NI conversion | — | 180.6% | 202.9% | 158.4% | 158.3% | 169.2% |

**Balance sheet (most recent, Apr 30 2026, stockanalysis.com):** Total Debt $6,900M, Cash & Short-Term Investments $6,780M, **Net Debt = $120M**, Total Equity $20,629M, Total Assets $39,330M. (An earlier fetch of this page mislabeled "Net Debt" using only Cash & Equivalents [$4,681M] rather than Cash & Short-Term Investments [$6,780M], producing an erroneous $2,219M figure — re-fetched and reconciled: $6,900M − $6,780M = $120M, matching the site's own explicitly-labeled "Net Cash (Debt): −120" line exactly.)

**Statistics (stockanalysis.com):** ROE 22.50%, ROIC 20.63%, ROA 9.47%, EV/EBITDA 15.68×, EV/EBIT 17.48×, Debt/Equity 0.33, Current Ratio 1.45, Shares Outstanding 273.54M.

**Cross-checks (internal consistency, not invented):**
- Market Cap (live) = 273.54M × $367.50 = **$100,526.2M**. EV (live) = Market Cap + Net Debt = 100,526.2 + 120 = **$100,646.2M**.
- EBITDA implied by EV/EBITDA 15.68× = $100,646.2M / 15.68 = **$6,417.7M** → Net Debt/EBITDA = $120M / $6,417.7M = **0.0187×** (≈0.02×) — the statistics page's own "Net Debt/EBITDA: 1.05" figure does not reconcile with the balance-sheet net-debt figure above; back-solving shows 1.05× actually matches **gross Debt/EBITDA** ($6,900M/$6,417.7M = 1.075×, ≈1.05× within rounding/timing) — i.e. that page mislabeled a gross-debt ratio as net-debt. **Net Debt/EBITDA = 0.0187× is used below**, derived transparently from two independently-sourced figures (Net Debt from the balance sheet page, EBITDA backed out of EV/EBITDA), not invented.
- EV/EBIT recomputed at live price = $100,646.2M / $5,749M = 17.51× — matches the site's independently-stated 17.48× (rounding/stale-price difference, negligible).

**Hard disqualifier check (quality-scoring.md):**
- FCF/NI conversion <70% for 2+ consecutive years: **No** — every year FY2022–TTM is 158%–203%, far above 70%.
- Net Debt/EBITDA over threshold (2.5× standard): **No** — 0.019×, effectively net-cash.
- Not FCF-positive for 3+ consecutive years: **No** — FCF positive and growing every year shown.

**No hard disqualifier fires.**

### 3a. Profitability (25% weight)

```
NetMargin_Component = clamp((21.91/30)×100, 0, 100) = 73.03   (TTM net margin, per quality-scoring.md's "Net Margin (TTM)" spec)
ROIC_Component       = clamp((20.63/30)×100, 0, 100) = 68.77
Profitability_Score  = (73.03 + 68.77) / 2 = 70.90   (no FCF-positivity cap — FCF-positive every year shown)
```

### 3b. Margins (15% weight)

```
GrossMargin_Score = clamp((80.79/80)×100, 0, 100) = 100.0   (clamped — TTM gross margin exceeds the 80% ceiling)
```
Gross margin has actually drifted slightly *down* from its FY2021 peak (83.05% → 80.79% TTM) — not a structural expansion, so no trend bonus applies (moot regardless, since the score is already clamped at 100.0).

### 3c. Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $12,726M → FY2025 $18,831M) = (18,831/12,726)^(1/3) − 1 = 13.94%
Growth_Score (base) = clamp((13.94/25)×100, 0, 100) = 55.77
```

**TAM/pricing-power modifier — evidence and judgment shown in full:**
- *For a +10 modifier:* Intuit's "online ecosystem" (QBO Advanced + Intuit Enterprise Suite) — a documented **upmarket TAM expansion** into mid-market/enterprise accounting, beyond QuickBooks' traditional small-business base — grew ~38% in Q3 FY2026, and management explicitly cited "QuickBooks pricing and mix gains" as an ongoing growth driver on the earnings call. [[GuruFocus](https://www.gurufocus.com/news/8872871/intuit-intu-reports-strong-q3-earnings-raises-fy-2026-guidance)]
- *Against a −10 penalty (structural deceleration):* **Does not apply at the consolidated level** — revenue growth has been *accelerating*, not decelerating (12.90% → 13.34% → 15.63% → 15.07% TTM, FY2023→TTM), and FY2026 guidance was *raised* mid-year. The one segment genuinely decelerating (TurboTax, per §2) is a real, disclosed headwind, but it is segment-specific, not the "structurally decelerating" company-wide pattern the modifier is written for — flagged qualitatively in the bear case (§5.4) and disruption-vector check (§7) instead of forcing an ill-fitting −10 here.
- **+10 modifier applied.**

```
Growth_Score = 55.77 + 10 = 65.77
```
*(Sensitivity: without the modifier, Growth_Score = 55.77 and Quality Score would be 80.8 instead of 82.8 — still clears the gate either way; see §3h.)*

### 3d. Balance Sheet (15% weight)

```
BalanceSheet_Score = clamp(100 × (1 − 0.0187/4), 0, 100) = 100 × 0.99533 = 99.53
```
No asset-light override needed — INTU is already far under even the standard 2.5× threshold on a near-net-cash balance sheet.

### 3e. Moat Signal (15% weight)

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | QuickBooks holds a dominant ~62–82% share of the small-business-accounting-software market (estimates vary by methodology/segment definition), next-largest rival (ADP) at ~14% — third-party market-share data, AceCloudHosting/ElectroIQ [[link](https://www.acecloudhosting.com/blog/quickbooks-market-share/)]. Watch item: Xero (a real international competitor) "continues to expand globally," per the same source — a share-erosion risk outside the US, not yet evidenced domestically. |
| Brand premium | **TRUE** | Documented price increases *without* volume loss in the largest segment: "QuickBooks Online Accounting revenues grew 22% in the quarter, supported by **higher effective prices, customer growth** and mix shift" (Q3 FY2026 earnings) — price increases and customer/volume growth occurring simultaneously is a direct match to the signal's definition. [[GuruFocus](https://www.gurufocus.com/news/8872871/intuit-intu-reports-strong-q3-earnings-raises-fy-2026-guidance)] **Caveat:** this evidence is QBO-specific; TurboTax shows the opposite pattern (guidance cut, IRS Direct File price competition) — see sensitivity note below. |
| Network effect | **TRUE** | QuickBooks Online App Store: 2.5M+ users can install third-party integrations, a documented indirect-network-effect mechanism (more users → more valuable third-party app ecosystem → more users), reinforced by the 2025 App Partner Program tiering [[amminvest.com](https://www.amminvest.com/intuit-business-moat/)] [[Intuit investor press release](https://investors.intuit.com/news-events/press-releases/detail/1261/intuit-launches-new-app-partner-program-to-drive-growth-for-third-party-developers-and-enhance-customer-experiences)]. Separately, Credit Karma operates a two-sided marketplace connecting users with 100+ financial-service-provider partners. |
| Switching costs | **TRUE** | Documented mechanism: "High switching costs exist when businesses, accountants, and integrated software all rely on QuickBooks Online, making switching unlikely unless drastic changes occur" [[amminvest.com](https://www.amminvest.com/intuit-business-moat/)] — multi-party lock-in (business + its accountant + its app integrations all on the same books). |
| Scale cost advantage | **FALSE** | No cost-per-unit data found comparing Intuit's per-customer cost structure against smaller competitors — not marked true without a citation, per quality-scoring.md's rule. |

```
Moat_Score = (4/5) × 100 = 80.0
```

**This is the single most decisive, most judgment-dependent input in this entire session — shown with maximum transparency because of it.** The "Brand premium" call is the swing signal: scored TRUE above on the strength of the QBO price/volume evidence, but a stricter reader could reasonably mark it FALSE given the *contradictory* TurboTax evidence (guidance cut under direct free-filing competition) sitting in the same company. **Sensitivity: if Brand premium is scored FALSE instead (Moat_Score = 60.0), Quality Score drops to 79.8 — a 0.2-point FAIL of the 80.0+ gate.** See the full sensitivity table in §3h before relying on the pass result.

### 3f. FCF Quality (10% weight)

```
FCF/NI (TTM) = $7,755M / $4,584M = 169.18%
FCFQuality_Score = clamp(((1.6918 − 0.40)/0.60)×100, 0, 100) = clamp(215.3, 0, 100) = 100.0   (capped)
```

### 3g. Full Quality Score — primary computation

```
Quality Score = (70.90×0.25) + (100.0×0.15) + (65.77×0.20) + (99.53×0.15) + (80.0×0.15) + (100.0×0.10)
              = 17.724 + 15.000 + 13.154 + 14.930 + 12.000 + 10.000
              = 82.808
              → rounds to 82.8
```

### 3h. Sensitivity table — how fragile is the 80.0+ pass?

| Scenario | Moat_Score | Growth TAM modifier | Quality Score | Gate result |
|---|---|---|---|---|
| **Primary (as scored above)** | 80.0 (4/5) | +10 | **82.8** | **PASS** (+2.8) |
| Conservative Moat (Brand premium → FALSE) | 60.0 (3/5) | +10 | **79.8** | **FAIL** (−0.2) |
| Conservative Growth (no TAM bonus) | 80.0 (4/5) | 0 | **80.8** | PASS (+0.8) |
| Both conservative | 60.0 (3/5) | 0 | **77.8** | FAIL (−2.2) |

**This is a genuinely narrow pass, not a comfortable clearance.** The primary reading (Moat TRUE on cited QBO price/volume evidence) is the one I stand behind — it's a direct, dated, quoted match to the signal's own definition, not an inference — but a reasonable reviewer weighing the TurboTax counter-evidence more heavily could flip the gate. **Flagged explicitly in §8 as the top-priority item to re-confirm at the very next re-score** (which, given the Aug 25 earnings date, is two days away).

### Gate Result: ✅ **PASS** (82.8 ≥ 80.0) — proceeding to Phase 02, with the above sensitivity carried forward as an open flag.

---

## 4. Rate Environment Gate

Per [strategy.md](../framework/strategy.md) / [valuation-scoring.md](../framework/valuation-scoring.md).

**Step 1 — Earnings Yield Spread Test:**
```
Forward PE = 13.73× (stockanalysis.com's own "Forward PE" statistic; cross-checked against FY2027 consensus EPS
             $27.28 at live price: $367.50/$27.28 = 13.47× — both land in the same ~13.5–13.7× range)
EY = 1 / 13.73 = 7.284%
Spread = EY − 10Y = 7.284% − 4.74% = 2.544%
```
Spread ≥ +1.5% → **passes Step 1, no additive flag.**

**Step 2 — Rate Regime Modifier:** 10Y = 4.74% falls in the 3.5–5% bracket → **+5**.

**Combined Rate Modifier = +5.**

---

## 5. Phase 02 — Valuation Score

### 5.1 PEG eligibility (Fast Grower check)

EPS growth over the last 3 consecutive complete fiscal years: FY2023 +15.66%, FY2024 +23.87%, FY2025 +31.06% — all >15%, on a clean, non-distorted earnings base (Intuit has been GAAP-profitable for decades; no recent IPO, no one-off gain in this window). **Qualifies as a Fast Grower — PEG applies at 15% weight.**

### 5.2 Sub-score inputs

```
FCF Yield = FCF(TTM) / Market Cap(live) = $7,755M / $100,526.2M = 7.7145%
EV/EBIT (live) = $100,646.2M / $5,749M = 17.51×
Forward PE = 13.73× (see §4)
5yr PE (proxy — see caveat below): FY2021–FY2025 fiscal-year-end PE = 70.23× / 62.28× / 60.11× / 61.08× / 56.61×
  → Avg = 62.06×, Low = 56.61×, High = 70.23× (stockanalysis.com "financials/ratios" page)
PEG = Forward PE / long-term EPS growth estimate = 13.73 / 14.0% = 0.981
  (long-term growth: Simply Wall St's "EPS expected to grow by 14% per annum" — chosen over a stale,
  differently-dated GuruFocus PEG snapshot of 0.66–0.67 computed off a different, unverified EPS base;
  both land well below 1.0 either way, so the PEG_Score conclusion is directionally robust to this choice)
```

**Caveat on the 5yr PE range:** these are five annual (fiscal-year-end) snapshots, not a true intra-year low/high range reconstructed from quarterly TTM EPS (the yfinance-based method in valuation-scoring.md — unusable since yfinance has been broken with SSL errors since 2026-07-07, per repo precedent). Treated as the **Fallback (average-only) formula**, not the Primary (range) formula, since 5 point-in-time snapshots don't constitute a verified continuous range.

### 5.3 Sub-scores

```
FCF_Score      = clamp(100×(1 − 7.7145/10), 0, 100) = 22.86
EV/EBIT_Score  = clamp((17.51 − 12)/23×100, 0, 100)  = 23.96
FwdPE_Score    = Deviation% = (13.73 − 62.06)/62.06×100 = −77.87%
               = clamp(50 + (−77.87×2.5), 0, 100) = clamp(50 − 194.68, 0, 100) = 0.0
               (fallback formula — already folds in the Historical PE Modifier, no separate ±10 applied)
PEG_Score      = clamp((0.981 − 0.5)/2.0×100, 0, 100) = 24.05

Raw weighted = (22.86×0.40) + (23.96×0.25) + (0.0×0.20) + (24.05×0.15)
             = 9.144 + 5.990 + 0.000 + 3.608
             = 18.74
```

**Note on the FwdPE_Score = 0.0 extreme:** a −77.9% deviation from the 5yr average PE is unusually large — reflecting that INTU traded at a 56–70× earnings multiple through FY2021–2025 (a rich, ZIRP/high-growth-SaaS-era multiple) and now trades at ~13.7× forward earnings after both the AI-disruption de-rating (§2) and genuine earnings growth. Applying the old high-multiple average mechanically to today's price is a real Rule 4 "multiple sanity" flag — the *comparison itself* may be as much a statement about a structural sector re-rating as about INTU being newly mispriced. Shown transparently rather than hidden or overridden (the framework provides no discretionary override for this case).

### 5.4 Fair Value (Rule 7 — scenario analysis, bull/base/bear)

**Method A — 3-stage DCF** (Rule 2: unlevered FCF, WACC = Rf + β×ERP = 4.74% + 0.96×5.0% ≈ 9.5% base case, varied ±1% per scenario; terminal growth ≤3% per Rule 2's GDP cap):

| | Bull (WACC 8.5%, terminal g 3.0%) | Base (WACC 9.5%, terminal g 2.5%) | Bear (WACC 10.5%, terminal g 2.0%) |
|---|---|---|---|
| Rev growth Y1→Y5 | 15%→11% | 12%→8% | 6%→4% |
| FCF margin Y1→Y5 | 35%→37.5% | 33%→34.5% | 30%→27% |
| Y5 FCF | $14,452M | $11,621M | $7,142M |
| Terminal Value | $270,655M | $170,157M | $85,706M |
| PV(FCFs) + PV(TV) | $43,892M + $180,006M | $36,498M + $108,092M | $25,570M + $52,024M |
| Enterprise Value | $223,898M | $144,590M | $77,594M |
| Equity Value (− net debt $120M) | $223,778M | $144,470M | $77,474M |
| **DCF FV/share** (÷273.54M shares) | **$818.03** | **$528.13** | **$283.24** |

*Sanity checks (Rule 4):* Bear-case FV ($283.24) lands close to (just above) the actual 52-week low ($252.84) — consistent with where the market actually priced the stock at its most pessimistic. Bull-case implied terminal FCF multiple = $270,655M/$14,452M = 18.7× — not an absurd exit multiple for a wide-moat software franchise.

**Method B — Peer comparable multiples** (Rule 5: 5 peers, median not mean): ADP 22.91×, PAYX 20.81×, WDAY 17.99×, MSCI 26.61×, HRB 8.73× forward PE (all live, stockanalysis.com, 2026-08-21 close) → **median = 20.81×**.

```
Base:  FY2027 consensus EPS $27.28 × peer median 20.81×        = $567.76
Bull:  FY2027 EPS $27.28 × highest-quality peer multiple (MSCI 26.61×) = $726.06
Bear:  FY2027 EPS $27.28 × lowest peer multiple (HRB 8.73× — a "market re-rates INTU
       to a legacy tax-software multiple despite unchanged EPS" scenario)             = $238.13
```
*(The historical-PE cross-check in Rule 3's "W4" — Current EPS × 5yr avg PE = 27.28×62.06 = $1,693 — is deliberately **excluded** from this blend: it fails Rule 4's multiple-sanity check outright, for the same structural-re-rating reason flagged in §5.3. Shown, not hidden, then discarded.)*

**Blended FV per scenario** (Fair Value = 40% DCF + 60% Multiples, per fair-value-methodology.md Step 1):

```
Bull:  0.40×818.03 + 0.60×726.06 = 327.21 + 435.64 = $762.85
Base:  0.40×528.13 + 0.60×567.76 = 211.25 + 340.66 = $551.91
Bear:  0.40×283.24 + 0.60×238.13 = 113.30 + 142.88 = $256.18

PW Blended Fair Value = 0.25×762.85 + 0.50×551.91 + 0.25×256.18 = 190.71 + 275.96 + 64.05 = $530.71
```

**Base-Case Blended Fair Value (for order setup) = $551.91. PW Blended Fair Value (for the modifier below) = $530.71.**

### 5.5 Upside/Downside Modifier

```
Gap Upside % = (PW FV / Live Price) − 1 = (530.71 / 367.50) − 1 = +44.41%

Catalyst & timeline (Rule 10): the next 2-3 quarterly earnings prints, spanning the imminent Aug 25 2026
  FY2026 close/FY2027 guidance and the full Jan-Apr 2027 tax-filing season (reported ~May 2027) — the
  window in which the AI-disruption/IRS-Direct-File bear thesis for TurboTax and the QBO/Credit Karma
  bull thesis both get real evidence. Catalyst window = 18 months (within Rule 10's 18-24mo band).
Annualized gap = 44.41% / 1.5yr = 29.61%/yr

Intrinsic growth rate = 14%/yr (Simply Wall St long-term EPS growth consensus, §5.2 — the more
  conservative of the available estimates, chosen deliberately)
Shareholder yield = dividend yield 1.31% (IBKR, live) + net buyback yield 3.4% (TradingKey/Investing.com,
  FY2026 trailing buyback data) = 4.71%

E = 29.61% + 14.00% + 4.71% = 48.32%/yr
```

`E` ≥ H(10%) → strong-upside band:
```
M = −15 × clamp((E−10)/15, 0, 1) = −15 × clamp(38.32/15, 0, 1) = −15 × clamp(2.55, 0, 1) = −15 × 1.0 = −15.0
```

**Guardrail/sanity flag (shown, not hidden):** E = 48.3%/yr is an extreme value — well past the +25%/yr level that already fully saturates the modifier at its ±15 cap. It's the arithmetic sum of three separately-optimistic inputs (a large re-rating gap annualized over a fairly short 1.5yr window, a punchy 14%/yr growth rate, and a real 4.71% shareholder yield), each individually defensible but compounding into a number that shouldn't be read as a literal 48%/yr forecast. This is exactly the scenario the ±15 cap (rather than an uncapped modifier) is designed for — per valuation-scoring.md's own rationale, "forecast informs but never overrides" — and the clamp does its job here regardless of how far past 25% the raw E lands.

**Upside/Downside Modifier = −15.0** (maximum attractive).

### 5.6 Final Valuation Score

```
Final Score = 18.74 (raw weighted, §5.3) + 5 (Rate Modifier, §4) + (−15.0) (Upside/Downside Modifier, §5.5)
            = 8.74 → rounds to 8.7
```

**Valuation Score = 8.7** — within the 0.0–29.9 "Very Cheap" band.

---

## 6. Composite Score

```
Composite Score = 0.50×(100 − Quality Score) + 0.50×Valuation Score
                = 0.50×(100 − 82.8) + 0.50×8.7
                = 0.50×17.2 + 0.50×8.7
                = 8.60 + 4.35
                = 12.95 → exactly on a ".X5" boundary → rounds UP (more conservative) → 13.0
```

**Composite Score = 13.0** → per the Composite/Phase 03 Action Table: **Score 0.0–29.9 → BUY — Full position 6–8%.**

*(Sensitivity carried from §3h: if the Moat brand-premium call had gone the other way, Quality Score would be 79.8 — the gate fails and this entire Composite/order-setup section would not exist. The valuation math above is real and independently robust; whether it's reached at all hinges on the one judgment call flagged in §3e/§3h.)*

---

## 7. Fair Value + Order Setup

**MoS / Max-Loss band for Composite Score 13.0 (the 0.0–29.9 tier): MoS 15–20%, Max Acceptable Loss 20–25%.**

### 7.1 A framework-application note on "Entry Price" — read before the numbers below

Live Price ($367.50) is already **below** the Buy-Price ceiling computed from Fair Value × (1−MoS) (~$441.53 at 20% MoS) — i.e. this is the "Score 0.0–29.9 → Stock at or below buy price → **Enter now**" case (fair-value-methodology.md's Integration table), not the "Set limit order" case. This matters for how Stop Loss / R/R / position sizing should be anchored:

- **Formula-literal reading (Buy Price as Entry, as used in the 2026-08-13 SNDK session's precedent):** that session's Buy Price *was* its live-tradeable limit — the stock hadn't reached the buy zone yet, so Buy Price = the real order price. Checking the same reading here for completeness: across the entire 0.0–29.9 band's allowed MoS/Max-Loss combinations, `R/R = MoS/[(1−MoS)×MaxLoss]` ranges from **0.71:1 (MoS 15%, Loss 25%) to 1.25:1 (MoS 20%, Loss 20%)** against the Primary Sell Target — **below the 2:1 minimum in every case**, structurally, the same failure mode SNDK hit.
- **Why that reading doesn't fit *this* case:** SNDK's Buy Price was the actual order price because the stock was still above it. Here, the stock is already *below* the ceiling — nobody would place a resting limit order at $441.53 when the market already trades at $367.50; the real transaction, if made today, executes at $367.50. Anchoring Stop-Loss/R-R/position-sizing to a ceiling price nobody would actually pay produces an artificially pessimistic, economically unrealistic R/R for an "Enter now" case.
- **Reading used below: Entry Price = Live Price ($367.50)**, since that is what an actual order placed today would fill at. This is flagged explicitly as an interpretive choice for the audit trail, not silently substituted.

Live Price already implies **33.4% below Base-Case Fair Value** (1 − 367.50/551.91), wider than even the top of this tier's 15–20% MoS requirement — confirming "Enter now" is appropriate on its own terms, independent of which entry-price reading is used.

### 7.2 Order setup (Entry = Live Price $367.50)

R/R checked across the full Max-Loss range for robustness (MoS is moot here since Entry ≠ the MoS-derived ceiling):

```
Stop @ 20% loss: $367.50×0.80 = $294.00 → R/R = ($551.91−367.50)/(367.50−294.00) = 184.41/73.50  = 2.509:1
Stop @ 25% loss: $367.50×0.75 = $275.63 → R/R = ($551.91−367.50)/(367.50−275.63) = 184.41/91.875 = 2.008:1
```
**R/R clears the 2:1 minimum across the entire allowed Max-Loss range (2.01:1–2.51:1)** — robust, not choice-sensitive. Headline numbers use **22% Max Loss** (mid-range, leaning conservative given the imminent Aug 25 earnings event risk, §2):

```
[x] Composite Score (drives action band):        13.0   (0.0–29.9 → Full-position entry)
[x] Raw Valuation Score (incl. Upside/Downside):  8.7
[x] Expected annual return E / catalyst window:   +48.32% / 1.5yr
[x] Upside/Downside Modifier applied:             −15.0
[x] Base-Case Blended Fair Value:                 $551.91
[x] PW Blended Fair Value (for E, above):         $530.71
[x] Implied discount to Fair Value at live price: 33.4% (exceeds the 15–20% MoS floor for this tier)
[x] ENTRY PRICE (live, "enter now"):              $367.50
[x] PRIMARY SELL TARGET (= Base Blended FV):      $551.91
[x] BULL-CASE TRIM TARGET (Bull Blended FV × 0.90): $762.85 × 0.90 = $686.57
[x] STOP LOSS (22% below entry):                  $367.50 × 0.78 = $286.65
[x] Risk/Reward Ratio (primary target):            ($551.91−367.50)/(367.50−286.65) = 184.41/80.85 = 2.28:1  — PASSES
[x] Risk/Reward Ratio (bull-case trim target):     ($686.57−367.50)/80.85 = 319.07/80.85 = 3.95:1  — clears comfortably
[x] Max $ Risk (1.5% of portfolio ≈$61,101.89, per holdings.md's 2026-08-22 combined-broker sync — informational
                                    only, no order placed this session):        $916.53
[x] Shares at that risk budget: $916.53 / $80.85 = 11.34 → 11 shares (risk-based, rounded down)
[x] Position Size cap check: 6–8% of portfolio = $3,666.11–$4,888.15 → risk-based size ($4,042.50) already
                                    falls inside this band — no cap override needed
[x] POSITION SIZE ($) — informational only, no order placed: 11 × $367.50 = $4,042.50 (≈6.62% of portfolio)
[x] Hard 15% single-position cap (Upgrade 7): 6.62% — far under, no breach
```

---

## 8. Recommendation

**BUY — Enter now, full position sizing indicated (≈6.62% of portfolio, 11 shares at $367.50, within the 6–8% band for Composite Score 13.0).** The mechanical framework output across every stage — Quality Gate (82.8), Rate Environment Gate, Valuation Score (8.7, very cheap), Composite Score (13.0), and Order Setup (R/R 2.28:1, clearing 2:1 across the full Max-Loss range) — supports entry.

**However, three things should weigh heavily on the human investor's actual decision, and are not something the mechanical score can resolve on its own:**

1. **The Quality Gate pass is narrow and single-signal-sensitive (§3h).** 82.8 vs. the 80.0 floor rests materially on reading Intuit's QuickBooks pricing/volume evidence as "Brand premium: TRUE" — a well-cited but genuinely debatable call given TurboTax's simultaneous, opposite evidence. A more conservative reading fails the gate at 79.8.
2. **Earnings are 2 days away (Aug 25, 2026).** Per fair-value-methodology.md Rule 9, this is a mandatory re-valuation trigger regardless of today's outcome — nearly every input above (FY2026 actuals replacing estimates, FY2027 initial guidance, updated Forward PE, confirmation or refutation of the AI-disruption bear case) will be refreshed within 48 hours. The framework has no rule instructing a delay ahead of a known catalyst, so this is surfaced as a judgment call for the human investor, not an override of the score-driven action.
3. **The Upside/Downside Modifier hit its −15 floor from an unusually large computed E (48.3%/yr, §5.5)** — the clamp is doing real work here, and the underlying assumption stack (a 1.5yr catalyst window, a 14%/yr growth rate, and shareholder yield, all summed) is more optimistic in combination than any one piece looks alone.

**No order is placed by this session** (per the task's explicit instruction — this produces a score/recommendation only).

---

## 9. Next Review Trigger

**Mandatory, near-term:** Intuit's Q4/full-year FY2026 earnings release, **2026-08-25** (2 days from this session) — a Rule 9 trigger regardless of outcome. Re-score immediately after, with particular attention to (a) whether QuickBooks Online pricing/volume evidence persists into FY2027 guidance (resolves the §3e/§3h Moat sensitivity), and (b) whether TurboTax's decline stabilizes or deepens.

**Standing triggers (Rule 9):** guidance revision, M&A, management change, macro shift, or a >15% unexplained move outside the above.

---

## 10. Watchlist Entry

Created `watchlist/not-in-portfolio/INTU/INTU-2026-08-23.md` — first-ever entry for this ticker (see §0/trigger). Full detail in that file; per watchlist/README.md convention it points back to this session as the canonical derivation record.

---

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **Composite Score** | This framework's single ranking number blending the Quality Score and the Valuation Score 50/50 (0 = most attractive, 100.0 = least). INTU scores 13.0. |
| **DCF (Discounted Cash Flow)** | A valuation method that estimates a company's value today as the sum of its future cash flows, discounted back to present value at a required rate of return (WACC). |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **EV** | Enterprise Value — a company's total value to all capital providers: market cap + debt − cash. |
| **EV/EBIT, EV/EBITDA** | Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE — the inverse of the PE ratio, expressed as a yield so it can be compared directly against bond yields (e.g. the 10-Year Treasury). |
| **Fast Grower** | Peter Lynch's term for a company growing earnings per share faster than 15%/year for 3+ years — INTU's FY2023–2025 pattern (+15.7%, +23.9%, +31.1%) qualifies. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. |
| **Fiscal Year (FY)** | A company's 12-month accounting year, which doesn't have to align with the calendar year. Intuit's runs 1 August–31 July. |
| **Forward PE** | Price ÷ next twelve months' expected earnings per share. |
| **Gross Margin** | Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted sub-score total; none fire for INTU. |
| **IRS Direct File** | The IRS's free government-run tax-filing tool, expanded for the 2026 season — a documented competitive threat to TurboTax. |
| **Market Cap (Market Capitalization)** | Share price × total shares outstanding — the total value the market currently assigns to a company's equity. |
| **Moat** / **Moat Signal** | A durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors; this framework's 5-point scored checklist version of the concept. |
| **MoS (Margin of Safety)** | How far below fair value the buy price is set, as a cushion against being wrong. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt. |
| **Net Margin** | Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax. |
| **PEG ratio** | PE ratio ÷ earnings growth rate — a PE adjusted for growth, used to judge whether a fast grower's multiple is justified by its growth rate. |
| **PW (Probability-Weighted) Fair Value** | This framework's blended fair value estimate — 25% bull + 50% base + 25% bear (Rule 7) — used as the single fair-value input to both the order setup and the Upside/Downside Modifier. |
| **QuickBooks Online (QBO)** | Intuit's cloud-based small-business accounting product — its largest growth engine, with a developer-app ecosystem (network effect) and multi-party lock-in (switching costs). |
| **Quality Score** | This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading profitability, margins, growth, balance sheet, moat, and FCF quality. A company must score 80.0+ to proceed to Phase 02. INTU scores 82.8 — a narrow pass (see §3h). |
| **Rate Environment Gate** | The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier. |
| **R/R (Risk/Reward Ratio)** | (Sell Target − Entry) ÷ (Entry − Stop Loss) — how much upside is on offer per unit of downside risked; this framework requires at least 2:1. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule. |
| **Shareholder yield** | Cash returned to owners as a % of price — dividend yield plus net buyback yield combined. |
| **TAM** | Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market. |
| **Treasury yield (10Y)** | The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results — here, through Intuit's fiscal quarter ended 30 April 2026. |
| **Upside/Downside Modifier** | An additive, ±15-bounded adjustment to the valuation score based on expected annual return (E) — strong expected upside lowers the score, an expected loss raises it. |
| **WACC (Weighted Average Cost of Capital)** | The discount rate used in a DCF — the blended required return of a company's debt and equity holders. |

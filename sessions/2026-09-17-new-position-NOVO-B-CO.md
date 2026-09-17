# NEW POSITION Evaluation — NOVO-B.CO (Novo Nordisk A/S, Copenhagen B-shares)

**Date:** 2026-09-17
**10Y US Treasury Yield:** 4.943% (2026-09-17, post-FOMC; source: CNBC/TradingEconomics — see Sources)
**Task type:** NEW POSITION

---

## ⚠️ Critical flag before scoring: this is not a new company to the framework

`NOVO-B.CO` (Copenhagen, OMXCOP, DKK) is the **B-share local listing of Novo Nordisk A/S** — the exact same legal entity, consolidated financial statements, and business as **NVO**, the NYSE ADR **already held** in this portfolio (0.35% weight per [holdings.md](../portfolio/holdings.md), last reviewed 09 Aug 2026, see [watchlist/in-portfolio/NVO/NVO-2026-08-09.md](../watchlist/in-portfolio/NVO/NVO-2026-08-09.md)). This is a **Dual-listing** situation (see Glossary), not two independent candidates. The Quality Score computed below is therefore a Quality Score for *Novo Nordisk the company*, not something specific to the Copenhagen share class — it will (and should) track NVO's own Quality Score closely, since both derive from the same DKK-denominated consolidated financials.

This was run through as a full, independent, current-data NEW POSITION session per the task instructions (not simply copied from the NVO file), but the conclusion should be read as **reconfirming Novo Nordisk's existing gate status**, not as an unrelated new discovery. Buying NOVO-B.CO in addition to NVO would not diversify this portfolio — it would concentrate the same single-company risk under a second ticker, working against the framework's 15% single-position cap (Upgrade 7) if ever scaled up. **Recommendation below is a PASS regardless of listing.**

---

## Step 1 — Live Price (Rule 0)

Fetched via `yfinance` at analysis time (2026-09-17):

```python
import yfinance as yf
t = yf.Ticker("NOVO-B.CO")
t.info["currentPrice"]   # 279.35
```

| Field | Value |
|---|---|
| **Live price** | **DKK 279.35** (CPH, previous close DKK 272.60) |
| 52-week range | DKK 224.25 – 409.95 |
| Exchange / currency | Copenhagen (CPH/OMXCOP) / DKK |
| Market cap | DKK 1,234.1B |
| Sector / Industry | Healthcare / Drug Manufacturers – General |

Cross-checked against an independent web search (Investing.com/aggregator, quoting DKK 275.90 close on 2026-09-15, two trading days prior) — consistent, no discrepancy. Live price is **not** inferred from any multiple; fetched directly per Rule 0.

---

## Step 2 — Phase 01 Quality Score

Per [quality-scoring.md](../framework/quality-scoring.md), methodology version **2026-06-29** (current — no bump since). All inputs sourced live via `yfinance` (`t.info`, `t.financials`, `t.cashflow`, `t.balance_sheet`) for Novo Nordisk A/S, most recent 4 fiscal years (FY2022–FY2025, fiscal year end 31 Dec). No metric estimated or invented; qualitative Moat/Growth-modifier claims are all cited to a source below.

### Raw financials pulled (DKK millions, annual)

| | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| Total Revenue | 176,954 | 232,261 | 290,403 | 309,064 |
| Gross Profit | 148,506 | 196,496 | 245,881 | 250,276 |
| EBIT | 69,440 | 105,216 | 128,831 | 134,747 |
| EBITDA | 76,802 | 114,629 | 137,376 | 149,413 |
| Pretax Income | 69,062 | 104,674 | 127,191 | 130,540 |
| Tax Provision | 13,537 | 20,991 | 26,203 | 28,106 |
| Net Income | 55,525 | 83,683 | 100,988 | 102,434 |
| Free Cash Flow | 64,134 | 70,012 | 69,659 | 28,989 |
| Operating Cash Flow | 78,887 | 108,908 | 120,968 | 119,102 |
| CapEx | (14,753) | (38,896) | (51,309) | (90,113) |
| Total Debt | 25,784 | 27,006 | 102,787 | 130,958 |
| Cash & Equivalents | 12,653 | 14,392 | 15,655 | 26,464 |
| Net Debt | 8,602 | 6,888 | 80,366 | 95,922 |
| Invested Capital | 104,741 | 127,841 | 239,507 | 316,433 |

TTM snapshot fields (`t.info`, blended trailing-quarter basis, more current than FY2025 annual): Net Margin 35.35%, Gross Margin 81.99%, ROE 59.82%, Revenue Growth (TTM y/y) 2.1%, Earnings Growth (TTM y/y) −20.6%.

### Profitability (25% weight)

```
NetMargin_Component = clamp((35.35/30)×100, 0, 100) = 100.0   (TTM net margin, capped)
ROIC (FY2025, most recent complete FY):
  Effective tax rate = 28,106 / 130,540 = 21.53%
  NOPAT = EBIT × (1 − tax rate) = 134,747 × 0.7847 = 105,733
  ROIC = NOPAT / Invested Capital = 105,733 / 316,433 = 33.42%
ROIC_Component = clamp((33.42/30)×100, 0, 100) = 100.0   (capped)
Profitability_Score = (100.0 + 100.0) / 2 = 100.0
```
FCF-positive 3+ consecutive years? Yes — all 4 years (FY2022–FY2025) positive. No cap applies.

*(Data gap flagged: true TTM ROIC would use trailing-4-quarter EBIT/invested capital; `yfinance`'s free tier doesn't expose a ready-made TTM EBIT series, so FY2025 — the most recent complete, audited fiscal year — is used instead, consistent with "never estimate a missing input.")*

### Margins (15% weight)

```
GrossMargin_Score = clamp((81.99/80)×100, 0, 100) = 100.0   (TTM, capped)
```
3yr trend check: 83.9% (FY22) → 84.6% (FY23) → 84.7% (FY24) → 81.0% (FY25) — **compressing**, not expanding, in the most recent year (consistent with the documented US price cuts below). No structural-expansion bonus applies (also moot at the 100.0 cap).

### Growth (20% weight)

```
Revenue 3yr CAGR = (309,064 / 176,954)^(1/3) − 1 = 20.41%
Growth_Score (raw) = clamp((20.41/25)×100, 0, 100) = 81.6
```
**Modifier — documented structural deceleration, −10:** Novo's own GLP-1/obesity franchise — its core growth driver — has visibly lost competitive ground to Eli Lilly:
- Eli Lilly overtook Novo Nordisk in **ex-US GLP-1 market share** (GxP News, May 2026)
- Novo's **US GLP-1 share** fell to roughly 39–40% vs. Lilly's ~60% (CNBC, Aug 2026 reporting; consistent with the 60.1%/39.4% split already cited in NVO's own 09 Aug 2026 watchlist entry)
- Novo guided to a **US sales decline in 2026**, citing "intensifying competition," reduced Medicaid obesity-drug coverage, and lower realized US prices under a "most-favored-nation" pricing deal (CNBC, Feb & Aug 2026)
- Repeated **GLP-1 price cuts** (BioSpace, 2026)
- CagriSema (next-gen pipeline asset) **failed to beat Lilly's tirzepatide** in a head-to-head Type 2 diabetes trial (CNBC, Feb 2026)

This is a company-specific, **competitive** (structural) deceleration, not a cyclical one — the −10 modifier applies. The **+10 TAM/pricing-power bonus is deliberately not applied**: while the broader obesity/diabetes market is genuinely still expanding, the bonus requires evidence *Novo itself* is capturing that expansion or holds pricing power, and the cited evidence above shows the opposite (share loss, price cuts, guided decline) — crediting +10 here would double-count a market-level tailwind against company-level facts pointing the other way.

```
Growth_Score = 81.6 − 10 = 71.6
```

### Balance Sheet (15% weight)

```
Net Debt/EBITDA (FY2025) = 95,922 / 149,413 = 0.642×
BalanceSheet_Score = 100 × (1 − 0.642/4) = 83.95 → 84.0
```
Not an asset-light business (pharma manufacturer) — standard /4 denominator, no Upgrade 5 override. Well inside the 2.5× standard hard-disqualifier threshold — passes. (Leverage did rise sharply in FY2024–25 — Net Debt/EBITDA was ~0.10× in FY2022/23 — driven by debt-funded capacity expansion, discussed below; still comfortably within threshold.)

### Moat Signal (15% weight) — checklist, cited evidence only

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **FALSE** | Eli Lilly overtook Novo in ex-US GLP-1 share (GxP News, May 2026); Novo's US GLP-1 share fell to ~39–40% vs. Lilly's ~60% (CNBC, Aug 2026) |
| Brand premium | **FALSE** | Repeated GLP-1 price cuts reported ("Novo Slashes GLP-1 Prices Again," BioSpace 2026) — evidence of eroding, not premium, pricing power; no cited price-increase-without-volume-loss evidence found |
| Network effect | **FALSE** | No documented two-sided-marketplace/network mechanism — not applicable to a pharmaceutical manufacturer's business model |
| Switching costs | **FALSE** | No cited source found this session documenting a specific switching-cost mechanism for Novo's GLP-1 franchise (data gap — not invented) |
| Scale cost advantage | **FALSE** | No cited cost-per-unit data vs. smaller competitors found this session; Novo's manufacturing scale is real (world's largest insulin/GLP-1 manufacturer) but the specific evidentiary bar ("cost-per-unit data showing a gap") wasn't met with a citable source |

```
Moat_Score = (0/5) × 100 = 0.0
```
Consistent with NVO's own existing watchlist finding — its 09 Aug 2026 entry independently records "Moat_Score 0.0 (0/5 signals) — the most severe moat reading of any holding in this repo."

### FCF Quality (10% weight)

```
FCF/NI ratio:
  FY2025: 28,989 / 102,434 = 28.31%
  FY2024: 69,659 / 100,988 = 69.00%
  FY2023: 70,012 / 83,683  = 83.66%
  FY2022: 64,134 / 55,525  = 115.51%

FCFQuality_Score = clamp(((0.2831 − 0.40)/0.60)×100, 0, 100) = clamp(−19.5, 0, 100) = 0.0
```

**Hard disqualifier check (FCF/NI <70% for 2+ consecutive years):** FY2024 (69.0%) and FY2025 (28.3%) are both under 70% — this pattern *would* fire the hard disqualifier **unless a documented growth-capex explanation exists**. One does: Novo's own FY2025 Annual Report states PP&E capital expenditure rose to **DKK 60.1B** (2025) from **DKK 47.2B** (2024), "primarily reflecting investments in additional capacity for active pharmaceutical ingredient (API) production and fill-finish capacity" — separately corroborated by Pharma Manufacturing (Novo to spend ~$9B in 2025 on additional capacity) and the Catalent fill-finish-site acquisition (2024, expanding Novo's global fill-and-finish footprint from 11 to 14 sites). This is genuine, sourced growth CapEx (manufacturing capacity, not maintenance), so **the hard disqualifier does not fire**. The continuous FCFQuality_Score is still scored at 0.0, though — the documented explanation excuses the binary disqualifier, not the weighted sub-score, per the framework's design.

### Other hard disqualifiers

- Net Debt/EBITDA over threshold? No — 0.642× vs. 2.5× standard threshold. **Passes.**
- Not FCF-positive for 3+ consecutive years? No — FCF positive all 4 years shown. **Passes.**

**No hard disqualifier fires.** The company proceeds to the weighted-score gate check below on its own merits.

### Final Quality Score

```
Quality Score = (100.0 × 0.25) + (100.0 × 0.15) + (71.6 × 0.20) + (84.0 × 0.15) + (0.0 × 0.15) + (0.0 × 0.10)
              = 25.00 + 15.00 + 14.32 + 12.60 + 0.00 + 0.00
              = 66.92 → rounds to 66.9
```

**Quality Score: 66.9 — FAILS the 80.0+ gate.**

### Cross-check against the existing NVO record

NVO (the NYSE ADR, same company) was independently scored **Quality Score 67.2** as of its 09 Aug 2026 rescore. This session's fresh, independently-derived **66.9** (five weeks later, using the Copenhagen listing's data feed but the same consolidated DKK financials) is closely consistent — the small ~0.3pt delta is fully explained by this session using full FY2025 annual figures for the ROIC/Profitability sub-score versus a more current TTM/quarterly-rolled figure in the 09 Aug session, and by continued incremental moat/competitive deterioration in the intervening five weeks. Both sessions agree: **Moat_Score 0.0**, Profitability/Margins saturated at 100.0, and an overall score meaningfully below the 80.0 gate. This is strong corroboration that the gate-fail is a real, stable reading of the underlying business — not a data artifact of which listing was queried.

---

## STOP — Quality Gate Fails

Per [.claude/commands/new-position.md](../.claude/commands/new-position.md) Step 2 and [quality-scoring.md](../framework/quality-scoring.md): **a Quality Score below 80.0 means the evaluation stops here.** Phase 02 (Rate Environment Gate + Valuation Score) and the Composite Score are **not computed** — a Composite Score is only meaningful for companies that have already cleared the quality gate, and computing one here would risk exactly the kind of "false green light" already flagged in NVO's own watchlist history (where a nominally cheap-looking reference Composite Score was explicitly called out as **not** a buy signal because the Quality Score fails).

No fair-value/order-setup work (Step 4 of the procedure) is performed, and no order of any kind is placed or recommended — consistent with this session's mandate as a paper recommendation exercise only.

---

## Step 5 — Recommendation

**PASS. Do not open a NOVO-B.CO position.**

Reasoning:
1. **Quality Score 66.9 < 80.0 — fails the framework's Phase 01 gate**, driven almost entirely by a Moat_Score of 0.0/100 (competitive share loss to Eli Lilly, price cuts, no cited pricing-power/network-effect/switching-cost/scale evidence) and a depressed, though not-disqualifying, FCF/NI conversion ratio (28.3% TTM-equivalent, explained by genuine growth CapEx).
2. Profitability, Margins, and Balance Sheet sub-scores are all excellent (100.0, 100.0, 84.0) — this is **not** a business in financial distress. The failure is specifically a **moat/competitive-position** problem, consistent with the framework's own prior, independent finding on the same company via NVO.
3. **This would also be a duplicate-exposure trade.** The portfolio already holds Novo Nordisk via NVO (0.35% weight) — adding NOVO-B.CO would not diversify anything; it would add a second ticker for the same single-company risk, working against the spirit of the 15% single-position cap (Upgrade 7) and complicating position-sizing math across two listings of one company.
4. This reconfirms, rather than newly discovers, the framework's standing read on this company (see NVO's watchlist history: HOLD existing position, no new capital, unresolved candidate for a formal EXIT REVIEW / override-log entry since 2026-06-07 — outside this session's NEW POSITION scope to action).

No buy price, sell target, stop loss, position size, or R/R ratio is computed — none of that fair-value work applies once the quality gate fails.

---

## Data gaps flagged

- True TTM ROIC (trailing-4-quarter EBIT ÷ trailing invested capital) was not directly available via `yfinance`'s free-tier `t.info`; FY2025 annual figures (the most recent complete, audited fiscal year) were used instead. Flagged, not estimated around.
- No cited source was found this session for a Novo-specific switching-cost mechanism or cost-per-unit scale data vs. smaller competitors — both Moat signals scored FALSE for lack of evidence rather than assumed true or false from general knowledge.

## Next review trigger

No standing review is opened for NOVO-B.CO specifically, since it is not a position and is the same underlying entity as NVO. Continue watching **NVO's own** existing next-review trigger (Q3 2026 earnings, expected early-to-mid November 2026 — see [watchlist/in-portfolio/NVO/NVO-2026-08-09.md](../watchlist/in-portfolio/NVO/NVO-2026-08-09.md)) rather than tracking a second, redundant trigger under this ticker.

---

## Sources

- [Novo Nordisk Annual Report 2025 — Financial performance](https://annualreport.novonordisk.com/2025/strategic-aspirations/financial-performance.html)
- [Novo Nordisk to spend about $9 billion in 2025 to create additional capacity — Pharma Manufacturing](https://www.pharmamanufacturing.com/industry-news/news/55266180/novo-nordisk-to-spend-about-9-billion-in-2025-to-create-additional-capacity)
- [Catalent paves the way for Novo's US GLP-1 expansion — BioProcess International](https://www.bioprocessintl.com/facilities-capacity/catalent-paves-the-way-for-novo-s-us-glp-1-expansion)
- [Eli Lilly's GLP-1 growth is only getting started as Novo Nordisk braces for a decline in 2026 — CNBC](https://www.cnbc.com/2026/02/04/eli-lilly-novo-nordisk-earnings-glp1-market.html)
- [Novo Nordisk shares slide after guidance disappoints investors — CNBC](https://www.cnbc.com/2026/08/04/novo-nordisk-releases-earnings-and-guidance.html)
- [Eli Lilly overtakes Novo Nordisk in GLP-1 market share outside US — GxP News](https://gxpnews.net/en/2026/05/eli-lilly-overtakes-novo-nordisk-in-glp-1-market-share-outside-us/)
- [These 4 charts show the scale of Novo Nordisk's woes — CNBC](https://www.cnbc.com/2026/02/25/novo-nordisk-stock-nvo-lly-eli-lilly-ozempic-weight-loss-obesity.html)
- [Novo Slashes GLP-1 Prices Again — BioSpace](https://www.biospace.com/drug-delivery/novo-slashes-glp-1-prices-again-touts-new-weight-loss-data-on-heels-of-lilly-loss)
- [Treasury yields move lower after Fed kicks off hiking cycle — CNBC](https://www.cnbc.com/2026/09/17/treasury-yields-move-lower-after-fed-kicks-off-hiking-cycle.html)
- [Novo Nordisk A/S Class B Stock Price Today — Investing.com](https://www.investing.com/equities/novo-nordisk)

---

## Glossary

- **ADR (American Depositary Receipt):** A US-exchange-listed security representing shares of a non-US company, letting US investors trade it in USD without using a foreign exchange directly. NVO is Novo Nordisk's ADR.
- **CAGR (Compound Annual Growth Rate):** The smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx (Capital Expenditure):** Money spent buying or upgrading physical assets (factories, equipment).
- **D&A (Depreciation & Amortization):** The non-cash accounting expense that spreads the cost of long-lived assets over time.
- **DKK (Danish Krone):** Denmark's currency, in which Novo Nordisk reports its financials and in which its Copenhagen listing (NOVO-B.CO) trades.
- **Dual-listing:** When the same company's shares trade on two separate stock exchanges — the two listings represent the same underlying business and financials, just quoted in different currencies/venues. NOVO-B.CO (Copenhagen) and NVO (NYSE ADR) are a dual-listing of Novo Nordisk A/S.
- **EBIT / EBITDA:** Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization — proxies for operating and cash operating profit.
- **FCF/NI conversion ratio:** Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. A low ratio without a CapEx explanation is a red flag for earnings-quality games.
- **GLP-1 (Glucagon-Like Peptide-1):** A hormone that stimulates insulin release and suppresses appetite; "GLP-1 drugs" (Novo's Ozempic/Wegovy, Lilly's Mounjaro/Zepbound) mimic it to treat diabetes and obesity — the core competitive battleground here.
- **Gross Margin / Net Margin:** The percentage of each revenue dollar left after direct production costs (gross) or after every expense, interest, and tax (net).
- **Hard disqualifier:** One of three Quality Score conditions that fails a company regardless of its weighted sub-score total, unless a documented exception applies.
- **Moat / Moat Signal:** A durable competitive advantage (brand, network effect, switching costs, scale); this framework's 5-point checklist scores it as `(TRUE signals ÷ 5) × 100`.
- **Most-Favored-Nation (MFN) pricing:** A drug-pricing policy requiring a manufacturer to charge a government payer no more than its lowest price elsewhere — part of the US pricing pressure cited above.
- **Net Debt/EBITDA:** Net debt divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt.
- **Quality Score:** This framework's 0.0–100.0 continuous score (0 = lowest quality, 100.0 = highest) grading profitability, margins, growth, balance sheet, moat, and FCF quality; a company must score 80.0+ to proceed to valuation scoring at all.
- **ROIC (Return on Invested Capital):** How efficiently a company turns the capital invested in it (debt + equity) into profit.
- **TAM (Total Addressable Market):** The total revenue opportunity available if a company captured 100% of its target market.
- **TTM (Trailing Twelve Months):** The most recent 12 months of financial data, as opposed to a fixed fiscal-year period.

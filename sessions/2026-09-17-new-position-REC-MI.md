# NEW POSITION — REC.MI (Recordati Industria Chimica e Farmaceutica S.p.A.)

**Date:** 2026-09-17
**Task type:** NEW POSITION
**Sector:** Healthcare — Drug Manufacturers, General (specialty/rare-disease pharma)
**Exchange:** Borsa Italiana (Milan), EUR-denominated
**Sourced from:** EU quality+value screening candidate (not an existing holding — confirmed absent from [portfolio/holdings.md](../portfolio/holdings.md) as of this session)

---

## 1. Live Price (Rule 0)

Fetched via `yfinance` (`yf.Ticker("REC.MI").info`), not inferred from multiples:

| Field | Value |
|---|---|
| **Live price** | **€52.75** |
| Previous close | €52.75 |
| 52-week range | €43.76 – €54.45 (price sits near the top of its 52-week range) |
| Market cap | €10.80B |
| Enterprise Value | €12.73B |
| Analyst mean target | €60.10 (8 analysts, consensus "buy") |

---

## 2. Phase 01 — Quality Score (full sub-score arithmetic)

All figures from `yfinance` (`t.info`, `t.financials`, `t.cashflow`, `t.balance_sheet`), fiscal years ending 31 Dec. Most recently completed FY = **FY2025**. No metric was estimated or invented; where a figure required computation (ROIC, CAGR, Net Debt/EBITDA, Owner Earnings) the inputs and formula are shown below.

### Hard disqualifier checks (run first)

| Disqualifier | FY2025 | FY2024 | FY2023 | FY2022 | Fires? |
|---|---|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs w/o documented growth-capex explanation | 115.4% | **−67.5%** | **26.2%** | 117.0% | **No — see below** |
| Net Debt/EBITDA over threshold (2.5× standard) | 2.30× | — | — | — | No (2.30× < 2.5×) |
| Not FCF-positive 3+ consecutive years | See Owner Earnings substitution below | | | | **No — see below** |

**Why the FCF/NI and FCF-positive disqualifiers don't fire despite the ugly raw numbers:** Recordati's `Capital Expenditure` line in `yfinance`'s cashflow statement is `Purchase of PPE + Purchase of Intangibles`. Breaking that down:

| FY | Purchase of PPE (maintenance) | Purchase of Intangibles (growth) | Total CapEx | Growth CapEx % of total |
|---|---|---|---|---|
| 2025 | €39.4M | €45.7M | €85.1M | 53.7% |
| 2024 | €36.6M | **€814.5M** | €851.2M | **95.7%** |
| 2023 | €29.7M | €353.6M | €383.3M | 92.3% |
| 2022 | €23.9M | €72.5M | €96.3M | 75.2% |

Growth CapEx (in-licensing/product-rights purchases, booked as intangible asset purchases) exceeds the **Hybrid Upgrade 1** 30% threshold in *every* disclosed year — confirmed as Recordati's core growth model (specialty-pharma licensing roll-up), not a one-off. The FY2024 spike specifically corresponds to Recordati's **October 2024 acquisition of global rights to Enjaymo** (a rare-disease drug, ~$820M deal), independently confirmed via web search (Recordati's own investor-relations transcript, "Acquisition of Global Rights to Enjaymo Conference Call," 04.10.2024). This is a documented, filed growth-capex explanation, not an assumption.

Per Upgrade 1, **Owner Earnings replaces reported FCF** for the FCF-quality tests:

```
Owner Earnings = Net Income + D&A − Maintenance CapEx only (PPE purchases)
```

| FY | Net Income | D&A | Maintenance CapEx | Owner Earnings | OE/NI ratio |
|---|---|---|---|---|---|
| 2025 | €443.6M | €206.4M | €39.4M | **€610.6M** | 137.6% |
| 2024 | €416.5M | €167.0M | €36.6M | **€546.9M** | 131.3% |
| 2023 | €389.2M | €142.7M | €29.7M | **€502.2M** | 129.0% |
| 2022 | €312.3M | €125.8M | €23.9M | **€414.2M** | 132.6% |

Owner Earnings is positive and comfortably above Net Income in all 4 disclosed years — **FCF-positive-3-years disqualifier does not fire**, and the FCF/NI ratio (on this substituted basis) never comes close to the 70% floor, so that disqualifier doesn't fire either. **No hard disqualifier fires.**

### Sub-score 1 — Profitability (25% weight)

```
Net Margin (TTM, info.profitMargins) = 18.38%
ROIC = NOPAT ÷ Invested Capital (FY2025)
     NOPAT = EBIT × (1 − effective tax rate) = €680.56M × (1 − 0.237) = €519.27M
     Invested Capital (yfinance balance sheet, FY2025) = €1,943.62M
     ROIC = 519.27 / 1,943.62 = 26.72%

NetMargin_Component = clamp((18.38/30)×100, 0, 100) = 61.26
ROIC_Component       = clamp((26.72/30)×100, 0, 100) = 89.05
Profitability_Score  = (61.26 + 89.05) / 2 = 75.16
```
(No FCF-positive-3yr cap applies — passed above on the Owner Earnings basis.)

### Sub-score 2 — Margins (15% weight)

```
Gross Margin (TTM, info.grossMargins) = 71.48%
GrossMargin_Score = clamp((71.48/80)×100, 0, 100) = 89.35
```
4-year annual trend (from `t.financials`, FY2022→FY2025: 69.4% → 68.3% → 68.4% → 68.3%) is flat-to-slightly-declining, not structurally expanding — **no +10 trend bonus applied.**

### Sub-score 3 — Growth (20% weight)

```
Revenue 3yr CAGR = (Revenue FY2025 / Revenue FY2022)^(1/3) − 1
                 = (€2,618.4M / €1,853.3M)^(1/3) − 1 = 12.21%
Growth_Score (raw) = clamp((12.21/25)×100, 0, 100) = 48.84
```
**TAM-expansion evidence (documented, cited):** Recordati's FY2026 guidance and Q2 2026 results (Investing.com, "Recordati H1 2026 slides: rare diseases fuel 17% growth, margins expand," and TipRanks H1 2026 coverage) show rare-disease revenue growing high-teens organically, a new Ionis Pharmaceuticals license (zilganersen, Alexander disease) signed in 2026, and sutimlimab advancing into Phase III (ITP) — active pipeline/TAM expansion beyond the current product base. **+10 applied.**

No documented structural deceleration evidence found — no −10 applied.

```
Growth_Score = 48.84 + 10 = 58.84
```

### Sub-score 4 — Balance Sheet (15% weight)

```
Total Debt (FY2025) = €2,467.5M
Cash (FY2025)        = €428.8M
Net Debt             = €2,038.7M
EBITDA (FY2025, t.financials) = €887.0M
Net Debt/EBITDA = 2,038.7 / 887.0 = 2.30×
```
Recordati is not a payment network/exchange/asset-light financial — **standard /4 denominator applies** (no Upgrade 5 override).
```
BalanceSheet_Score = clamp(100×(1 − 2.30/4), 0, 100) = 42.54
```
2.30× sits under the 2.5× hard-disqualifier threshold, but is a middling leverage level for the quality score itself — reflects the debt taken on to fund the Enjaymo/EUSA-style licensing acquisitions discussed above.

### Sub-score 5 — Moat Signal (15% weight)

Checklist scored only against cited evidence — evidence gathered via web search this session (see Sources below):

| Signal | True/False | Evidence |
|---|---|---|
| Market share stable or growing | **False** | No third-party market-share % citation found for Recordati's specific therapeutic niches (Cushing's disease, etc.) — revenue growth (Isturisa +58% YoY) is not the same as a documented share figure, and a 2020 FDA-approval-era article on Isturisa specifically noted "competition aplenty" in that indication. Not marked true without a specific share citation, per framework rule. |
| Brand premium / pricing power | **True** | Investing.com/TipRanks H1 2026 coverage: rare-disease segment carries a 43.1% EBITDA margin vs. 34.7% for specialty/primary care, explicitly attributed to "a defensible niche with limited competition and premium pricing" vs. larger peers (Alexion/AstraZeneca, Chiesi). |
| Network effect | **False** | Not applicable to this business model (specialty pharma manufacturing/licensing) — no documented mechanism found. |
| Switching costs | **False** | No documented contractual-lock-in or workflow-migration-cost evidence found specific to Recordati's products this session (orphan-drug *patent/regulatory exclusivity* exists — e.g. Isturisa patent to 2031, prior 7-year FDA orphan exclusivity — but that is a legal/registration barrier to new entrants, not a customer switching-cost mechanism as this checklist defines the signal, so not counted here). |
| Scale cost advantage | **False** | No cost-per-unit-vs-competitor data found this session. |

```
Moat_Score = (1/5) × 100 = 20.0
```

### Sub-score 6 — FCF Quality (10% weight)

Using the Owner Earnings/NI ratio (Upgrade 1 substitution, justified above), FY2025 basis:
```
OE/NI ratio = 137.6%
FCFQuality_Score = clamp(((1.376 − 0.40)/0.60)×100, 0, 100) = 162.7 → clamped to 100.0
```

### Final Quality Score

```
Quality Score = (75.16×0.25) + (89.35×0.15) + (58.84×0.20) + (42.54×0.15) + (20.0×0.15) + (100.0×0.10)
             = 18.79 + 13.40 + 11.77 + 6.38 + 3.00 + 10.00
             = 63.34 → rounds to 63.3
```

**Quality Score: 63.3 / 100.0 — fails the 80.0+ gate.**

---

## STOP — Gate Failure, No Phase 02 Scoring Performed

Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md), a Quality Score below 80.0 halts the process here — **no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, no fair-value/order-setup work was performed**, regardless of how the stock's multiples might otherwise look (forward PE 14.0×, PEG 1.1, dividend yield 2.69% all look superficially reasonable — irrelevant, since the gate is checked first).

**No hard disqualifier fired** — the gate failure is driven entirely by the weighted score, primarily:
- **Moat_Score (20.0)** — only 1 of 5 signals cleared the cited-evidence bar this session; the framework's discipline against marking a signal true without a citation is the single largest drag (a 65-point sub-score points from the ceiling, at 15% weight, costs ~9.75 raw points relative to a hypothetical fully-evidenced moat).
- **Balance Sheet (42.54)** — 2.30× Net Debt/EBITDA, middling leverage from the licensing-driven acquisition strategy, though comfortably under the 2.5× hard-disqualifier line.
- **Growth (58.84)** and **Profitability (75.16)** are moderate-to-good but not exceptional.

**Recommendation: PASS.** Do not open a position. Add to watchlist (not-in-portfolio) for future re-evaluation — the Moat signal in particular is a swing factor that could change with better market-share data (a specific % of the Cushing's-disease or orphan-endocrinology market, e.g.) or with a subsequent earnings/pipeline update.

## Next review trigger

No routine re-check scheduled (Phase 01 FAIL, no numeric Phase 02 score to go stale). Re-evaluate on any of:
- **Q4/FY2026 earnings** (next full-year report) — refreshes all financial sub-scores with a new most-recently-completed fiscal year.
- **Third-party market-share data** for Recordati's key rare-disease franchises (Isturisa/Cushing's, Signifor, sutimlimab/ITP once launched) becoming available — the single most likely lever to move the Moat_Score.
- Any Rule 9 fundamental trigger (earnings, guidance revision, M&A, management change, macro shift, >15% unexplained price move).

---

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. A low ratio without a CapEx explanation is a red flag for earnings-quality games. |
| **Gross Margin** | Gross Profit (Revenue − Cost of Revenue) ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted sub-score total: not FCF-positive for 3+ consecutive years, Net Debt/EBITDA over its applicable threshold, or an FCF/Net Income conversion ratio under 70% for 2+ consecutive years without a documented growth-capex explanation. |
| **Invested Capital** | The total capital (debt + equity, netted for cash) put to work in a business — the denominator in a Return on Invested Capital (ROIC) calculation. |
| **Moat** | Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors. |
| **Moat Signal** | This framework's 5-point Quality Score checklist that turns the general "Moat" concept into a scored input, each markable TRUE only against a cited source. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt. |
| **Net Margin** | Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **Orphan drug / Orphan drug exclusivity** | A drug developed to treat a rare disease, for which regulators grant development incentives including a period of market exclusivity (e.g. 7 years under the FDA's Orphan Drug Act) blocking competing versions. A legal barrier to entry, distinct from this framework's Moat Signal checklist categories. |
| **Owner Earnings** | Warren Buffett's adjusted cash-flow measure: Net Income + D&A − *Maintenance* CapEx only (excludes growth CapEx) — used instead of raw FCF for moat-building reinvestors (Hybrid Upgrade 1), applied here because Recordati's growth CapEx (in-licensing deals) exceeds 30% of total CapEx in every disclosed year. |
| **Quality Score** | This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. REC.MI scores 63.3. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule. |
| **TAM** | Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market. |

**Sources (web search, this session):**
- [Recordati H1 2026 slides: rare diseases fuel 17% growth, margins expand — Investing.com](https://www.investing.com/news/company-news/recordati-h1-2026-slides-rare-diseases-fuel-17-growth-margins-expand-93CH-4820180)
- [Recordati extends rare disease-led growth, lifts profitability in H1 2026 — TipRanks](https://www.tipranks.com/news/company-announcements/recordati-extends-rare-disease-led-growth-lifts-profitability-in-h1-2026)
- [Recordati S.P.A "Acquisition of Global Rights to Enjaymo Conference Call" transcript (04.10.2024)](https://recordati.com/wp-content/uploads/2024/10/Recordati-Transcript-04.10.2024.pdf)
- [Recordati scores FDA nod for Cushing's disease med — Isturisa — Fierce Pharma](https://www.fiercepharma.com/pharma/recordati-scores-fda-nod-for-cushing-s-disease-med-isturisa)
- [Competition aplenty as Novartis' Isturisa is FDA-approved to treat Cushing's disease — BioWorld](https://www.bioworld.com/articles/433589-competition-aplenty-as-novartis-isturisa-is-fda-approved-to-treat-cushings-disease)

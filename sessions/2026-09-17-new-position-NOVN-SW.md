# NEW POSITION — NOVN.SW (Novartis AG)

**Date:** 2026-09-17
**Task type:** NEW POSITION
**Sector:** Healthcare — Drug Manufacturers, General (large-cap diversified pharma)
**Exchange:** SIX Swiss Exchange (EBS), CHF-denominated
**Sourced from:** ad-hoc candidate evaluation (not an existing holding)

**Duplicate-entity check:** [portfolio/holdings.md](../portfolio/holdings.md) was checked in full for Novartis AG under any ticker before starting this evaluation. **No match found** — Novartis does not appear as NOVN.SW, NVS (its US ADR), or under any other listing. This is a genuinely new candidate, unlike this run's earlier Novo Nordisk finding (NOVO-B.CO vs. the already-held NVO ADR, same legal entity — see [sessions/2026-09-17-new-position-NOVO-B-CO.md](2026-09-17-new-position-NOVO-B-CO.md)). Novartis and Novo Nordisk are separate, unrelated companies despite the similar names, so no duplicate-entity flag applies here.

---

## 1. Live Price (Rule 0)

Fetched via `yfinance` (`yf.Ticker("NOVN.SW").info` / `.fast_info`), not inferred from multiples:

| Field | Value |
|---|---|
| **Live price** | **CHF 116.02** |
| Previous close | CHF 114.28 |
| 52-week range | CHF 96.23 – CHF 132.68 (price sits in the lower half of its 52-week range) |
| Market cap | CHF 220.52B |
| Enterprise Value | CHF 259.01B |

**Recent price context (not a scored input, informational only):** the stock fell sharply from CHF 129.58 (2026-09-04) to CHF 111.80 (2026-09-08), a ~13.7% single-day-adjacent drop, coinciding with the pelacarsen trial failure reported 2026-09-04/05 (see Rule 9 note below). Below the framework's 15% unexplained-move threshold, and the cause is identified (not "unexplained"), so this alone would not trigger a Rule 9 re-valuation on its own — noted here for context since this is a fresh evaluation, not a re-score.

---

## 2. Phase 01 — Quality Score (full sub-score arithmetic)

All figures from `yfinance` (`t.info`, `t.financials`, `t.cashflow`, `t.balance_sheet`, `t.quarterly_financials`, `t.quarterly_cashflow`, `t.quarterly_balance_sheet`). Fiscal year ends 31 December; most recently completed FY = **FY2025**. Where a metric benefits from the most current available data rather than the stale FY2025 year-end snapshot (see Balance Sheet sub-score below — Novartis closed a $12B debt-funded acquisition in Feb 2026, a Rule 9 material-M&A event that post-dates FY2025's close), the **TTM (trailing twelve months through 2026-06-30, the latest reported quarter)** basis is used instead and both bases are shown for transparency. No metric was estimated or invented; every figure below traces to a specific `yfinance` field.

### Hard disqualifier checks (run first)

| Disqualifier | Result | Fires? |
|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years w/o documented growth-capex explanation | FY2023 78.8%, FY2024 115.6%, FY2025 109.0%, TTM 117.4% — all comfortably above 70% | **No** |
| Net Debt/EBITDA over its applicable threshold (2.5× standard — Novartis is not a payment network/exchange/asset-light financial, so no Upgrade 5 override) | FY2025 year-end 1.05×; **TTM (current) 1.84×** — both under 2.5× | **No** |
| Not FCF-positive for 3+ consecutive years | FCF positive every year FY2022–FY2025 (CHF 11.997B, 11.705B, 13.805B, 15.244B) | **No** |

**No hard disqualifier fires.**

### Sub-score 1 — Profitability (25% weight)

```
Net Margin (TTM, info.profitMargins)  = 22.50%
ROIC = NOPAT ÷ Invested Capital (TTM basis, quarter ended 2026-06-30)
     EBIT (TTM, sum of last 4 quarters: Sep-25 4,477 + Dec-25 3,522 + Mar-26 4,182 + Jun-26 4,731) = CHF 16,912M
     Effective tax rate (TTM) = Tax Provision TTM 2,775 ÷ Pretax Income TTM 15,522 = 17.88%
     NOPAT = 16,912 × (1 − 0.1788) = CHF 13,890M
     Invested Capital (latest quarter, 2026-06-30) = Total Debt 49,014 + Stockholders Equity 41,542 − Cash 7,616 = CHF 82,940M
     ROIC = 13,890 / 82,940 = 16.75%

NetMargin_Component = clamp((22.50/30)×100, 0, 100) = 75.01
ROIC_Component       = clamp((16.75/30)×100, 0, 100) = 55.83
Profitability_Score  = (75.01 + 55.83) / 2 = 65.42
```
No FCF-positive-3yr cap applies (FCF positive every year FY2022–FY2025 — see above).

*Reference (FY2025 year-end basis, for comparison): EBIT 17,496 × (1 − 14.59% tax) = NOPAT 14,943; Invested Capital (FY2025) 79,586 → ROIC 18.78% → ROIC_Component 62.6 → Profitability_Score 68.81. Either basis is used below is noted; the TTM basis (65.42) is carried forward as the primary figure since it reflects the current balance sheet rather than a stale pre-acquisition snapshot.*

### Sub-score 2 — Margins (15% weight)

```
Gross Margin (TTM, info.grossMargins) = 74.98%
GrossMargin_Score = clamp((74.98/80)×100, 0, 100) = 93.72
```
4-year annual trend (`t.financials`, FY2022→FY2025): 73.4% → 73.3% → 73.3% → 75.8% — mildly expanding, but the +10 structural-trend bonus in [quality-scoring.md](../framework/quality-scoring.md) only applies to a margin still **below the 40% static threshold** trending up; Novartis is already well above 40%, so **no bonus applies** (per the rule as written, not a discretionary call).

### Sub-score 3 — Growth (20% weight)

```
Revenue 3yr CAGR = (Revenue FY2025 / Revenue FY2022)^(1/3) − 1
                 = (CHF 56,674M / CHF 43,461M)^(1/3) − 1 = 9.25%
Growth_Score (raw) = clamp((9.25/25)×100, 0, 100) = 37.00
```

**TAM-expansion evidence (documented, cited via web search this session):**
- Novartis dominates the radioligand-therapy oncology market with its two approved products, Pluvicto and Lutathera, which generated a combined **$2.8B in FY2025 net sales**; Pluvicto alone grew 43% YoY to ~$1.99B and management guides to **$5B in Pluvicto sales alone by 2030**, against a radioligand-therapy market projected to grow from $4.23B (2026) to $29.54B (2034) ([DelveInsight](https://www.delveinsight.com/blog/novartis-in-radioligand-therapies), [GuruFocus/Yahoo Finance](https://finance.yahoo.com/healthcare/articles/novartis-eyes-5-billion-pluvicto-133414369.html)).
- Priority brands are growing well ahead of the company average: Kisqali +44% cc (constant currency) FY2025 / +55% cc Q1 2026, Kesimpta +27% cc FY2025 / +32% (to $1.4B) Q2 2026, Scemblix +87% cc FY2025 / +79% cc Q1 2026 ([Novartis FY2025 media release](https://www.novartis.com/news/media-releases/novartis-delivered-high-single-digit-sales-growth-achieved-40-core-margin-and-further-advanced-pipeline-2025), [BiotechReality Q2 2026 coverage](https://www.biotechreality.com/2026/07/novartis-q2-2026-results.html)).

**+10 applied** for documented TAM expansion (a growing addressable market in radioligand oncology plus multiple priority brands scaling well above the group average).

**Structural-deceleration check (considered, not applied):** Novartis's own 2026 guidance calls for "low single-digit" net sales growth and a low-single-digit **decline** in core operating income, a marked step-down from the trailing 9.25% 3yr CAGR, following a December 2025 US government agreement to lower medicine prices ([market.us](https://market.us/statistics/pharmaceutical-industry/novartis/)). This is real and documented, but reads as a **one-year compression** tied to a specific, dated pricing settlement and to Entresto's 2025 patent-cliff (Loss of Exclusivity) drag — not a structurally decelerating growth trajectory (management's own 2025–2030 guidance is 5–6% CAGR, i.e. an acceleration back above the 2026 trough). Per [quality-scoring.md](../framework/quality-scoring.md)'s requirement that the deceleration be "structural (not cyclical)," **no −10 applied** — flagged here as a genuine near-term risk worth watching, not ignored.

```
Growth_Score = 37.00 + 10 = 47.00
```

### Sub-score 4 — Balance Sheet (15% weight)

```
Total Debt (latest quarter, 2026-06-30) = CHF 49,014M
Cash (latest quarter, 2026-06-30)        = CHF 7,616M
Net Debt                                  = CHF 41,398M
EBITDA (TTM, sum of last 4 quarters: Sep-25 5,841 + Dec-25 5,073 + Mar-26 5,410 + Jun-26 6,131) = CHF 22,455M
Net Debt/EBITDA (TTM) = 41,398 / 22,455 = 1.84×
```
Novartis is not a payment network/exchange/asset-light financial — standard /4 denominator applies (no Upgrade 5 override).
```
BalanceSheet_Score = clamp(100×(1 − 1.84/4), 0, 100) = 53.90
```

**Why TTM, not FY2025 year-end:** Novartis's debt jumped from CHF 35.4B (FY2025 year-end) to CHF 49.0B (2026-06-30) because it financed the **$12B acquisition of Avidity Biosciences** (a rare-disease/RNA-therapeutics pipeline deal) with an $11B bridge loan (closed 27 Feb 2026), refinanced 18 March 2026 via an $11B, seven-tranche **investment-grade** bond offering ([Novartis media release](https://www.novartis.com/news/media-releases/novartis-successfully-completes-acquisition-avidity-biosciences-strengthening-late-stage-neuroscience-pipeline-and-advancing-xrna-strategy), [Bloomberg](https://www.bloomberg.com/news/articles/2026-03-16/novartis-offers-high-grade-debt-to-fund-12-billion-avidity-deal)). This is a documented, material, Rule 9 M&A event that post-dates the FY2025 balance sheet — using the stale year-end figure (1.05×, which would score 73.78) would materially understate current leverage. The TTM figure (1.84×) is used as the primary basis; it remains comfortably under the 2.5× hard-disqualifier threshold, but the near-doubling of debt in two quarters is flagged as a genuine, ongoing balance-sheet-risk item to monitor (Phase 04 Quality Watch).

### Sub-score 5 — Moat Signal (15% weight)

Checklist scored only against cited evidence gathered via web search this session:

| Signal | True/False | Evidence |
|---|---|---|
| Market share stable or growing | **True** | Novartis holds both of the only two currently-approved radioligand therapies (Pluvicto, Lutathera), described as market-dominant: "the market is dominated by Novartis AG, due to the presence of the top two approved radioligand therapies in its product portfolio" ([DelveInsight](https://www.delveinsight.com/blog/novartis-in-radioligand-therapies)). |
| Brand premium / pricing power | **False** | No documented price-increase-without-volume-loss evidence found this session; the opposite is documented — Novartis agreed (19 Dec 2025) to a US government deal to **lower** medicine prices, and 2026 guidance reflects margin/growth compression from that agreement ([market.us](https://market.us/statistics/pharmaceutical-industry/novartis/)). Not marked true. |
| Network effect | **False** | Not applicable to this business model (branded pharmaceutical manufacturing) — no documented mechanism found. |
| Switching costs | **False** | Patent/regulatory exclusivity on individual drugs is a legal barrier to entry, not a customer switching-cost mechanism as this checklist defines the signal (consistent with how this framework treated Recordati's orphan-drug exclusivity in the 2026-09-17 REC.MI session) — no documented patient/prescriber switching-cost mechanism found this session. |
| Scale cost advantage | **False** | Novartis's radioligand manufacturing network (commercial-scale production sites) is frequently cited as a capacity/entry barrier relative to smaller competitors facing a "CDMO crunch" ([IntuitionLabs](https://intuitionlabs.ai/articles/radioligand-therapy-manufacturing-capacity)), but no specific **cost-per-unit** figure vs. a named competitor was found this session — the framework requires cost-per-unit data for this specific signal, not capacity/entry-barrier evidence alone. Not marked true. |

```
Moat_Score = (1/5) × 100 = 20.0
```

### Sub-score 6 — FCF Quality (10% weight)

```
FCF/NI ratio (TTM) = FCF TTM 14,980 / NI TTM 12,757 = 117.4%
FCFQuality_Score = clamp(((1.174 − 0.40)/0.60)×100, 0, 100) = clamp(129.0, 0, 100) = 100.0
```

### Final Quality Score

```
Quality Score = (65.42×0.25) + (93.72×0.15) + (47.00×0.20) + (53.90×0.15) + (20.0×0.15) + (100.0×0.10)
             = 16.355 + 14.058 + 9.400 + 8.085 + 3.000 + 10.000
             = 60.898 → rounds to 60.9
```

**Quality Score: 60.9 / 100.0 — fails the 80.0+ gate.**

*(Reference: using the FY2025 year-end balance-sheet/ROIC basis instead of TTM, the score would be 64.7 — still a clear gate failure either way; the choice of basis does not change the outcome.)*

---

## STOP — Gate Failure, No Phase 02 Scoring Performed

Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md), a Quality Score below 80.0 halts the process here — **no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, no fair-value/order-setup work was performed**, regardless of how the stock's headline multiples look (forward PE 14.4×, PEG 3.28 — irrelevant, since the gate is checked first).

**No hard disqualifier fired** — the gate failure is driven entirely by the weighted score, primarily:
- **Moat_Score (20.0)** — only 1 of 5 signals cleared the cited-evidence bar (radioligand-therapy market dominance); the other four either don't apply to this business model or lack a specific citable data point this session. The single largest drag on the total score.
- **Balance Sheet (53.9 on the current TTM basis)** — leverage nearly doubled in two quarters (1.05× → 1.84×) funding the $12B debt-financed Avidity Biosciences acquisition; still safely under the 2.5× hard-disqualifier line, but a real drag on quality vs. a company with a cleaner balance sheet.
- **Growth (47.0)** — decent trailing 3yr revenue CAGR (9.25%) with credited TAM-expansion evidence, but well short of the 25% ceiling, and clouded by 2026 guidance for a sharp near-term slowdown (flagged, not penalized — see reasoning above).
- **Profitability (65.42)** is solid but not exceptional; **Margins (93.72)** and **FCF Quality (100.0, clamped)** are both strong.

**Fundamental context (Rule 9-relevant, not itself the reason for the gate failure):** on 2026-09-04/05, Novartis's Lp(a)-lowering drug **pelacarsen** (partnered with Ionis Pharmaceuticals) failed to reduce cardiovascular events in the 8,000+-patient Lp(a)HORIZON late-stage trial, despite successfully lowering Lp(a) levels as designed — a "biomarker moved, clinical outcome didn't" result that raises questions about pelacarsen's commercial prospects and, more broadly, about the entire emerging Lp(a)-lowering drug class Novartis had bet on ([CNBC](https://www.cnbc.com/2026/09/08/novartis-cholesterol-setback-drug-race-eli-lilly-amgen.html), [BioPharma Dive](https://www.biopharmadive.com/news/novartis-ionis-pelacarsen-lpa-horizon-study-results-fail/829736/)). This is a real, dated pipeline setback and a legitimate growth-thesis risk, but is **not** what drove today's gate failure — the Quality Score above is built entirely from filed financials and cited market-position evidence, not from pipeline-outcome speculation, consistent with "never invent or estimate financial data."

**Recommendation: PASS.** Do not open a position. Add to watchlist (not-in-portfolio) for future re-evaluation.

## Next review trigger

No routine re-check scheduled (Phase 01 FAIL, no numeric Phase 02 score to go stale). Re-evaluate on any of:
- **Q4/FY2026 earnings** (next full-year report, expected ~January 2027) — refreshes all financial sub-scores with a new most-recently-completed fiscal year and settles whether the 2026 guidance slowdown was in fact temporary.
- **Third-party market-share or pricing-power data** for Novartis's priority brands (Cosentyx, Kisqali, Kesimpta) becoming available — the single most likely lever to move the Moat_Score beyond the one radioligand-therapy signal currently credited.
- Any further Rule 9 fundamental trigger (additional pipeline readouts, further debt issuance/M&A, management change, macro shift, >15% unexplained price move).

---

## Glossary

| Term | Meaning |
|---|---|
| **Bridge Loan** | A short-term loan taken to cover immediate financing needs (e.g. an acquisition) ahead of a planned, larger permanent-financing takeout (typically a bond offering). Novartis used an $11.0B bridge loan to fund the Avidity Biosciences acquisition, repaid via a subsequent bond offering. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. A low ratio without a CapEx explanation is a red flag for earnings-quality games. |
| **Gross Margin** | Gross Profit (Revenue − Cost of Revenue) ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted sub-score total: not FCF-positive for 3+ consecutive years, Net Debt/EBITDA over its applicable threshold, or an FCF/Net Income conversion ratio under 70% for 2+ consecutive years without a documented growth-capex explanation. |
| **Investment grade** | A credit rating (BBB-/Baa3 or higher) signaling a low perceived risk of default — as opposed to "junk"/high-yield ratings below that line. Novartis's Avidity-acquisition bonds were issued at investment grade. |
| **Invested Capital** | The total capital (debt + equity, netted for cash) put to work in a business — the denominator in a Return on Invested Capital (ROIC) calculation. |
| **Lipoprotein(a) / Lp(a)** | A genetically-determined, cholesterol-carrying particle independently linked to cardiovascular risk — the target of Novartis/Ionis's pelacarsen, which lowered Lp(a) levels in its late-stage trial but failed to reduce actual cardiovascular events. |
| **Loss of Exclusivity (LOE)** | The point at which a drug's patent/regulatory exclusivity expires, opening the door to generic/biosimilar competition and typically causing a sharp revenue decline — Novartis's Entresto faced this in 2025, contributing to 2026's growth slowdown. |
| **Moat** | Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors. |
| **Moat Signal** | This framework's 5-point Quality Score checklist that turns the general "Moat" concept into a scored input, each markable TRUE only against a cited source. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt. |
| **Net Margin** | Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **Quality Score** | This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. NOVN.SW scores 60.9. |
| **Radioligand therapy** | A cancer treatment that delivers targeted radiation directly to cancer cells via a molecule engineered to bind specific tumor targets. Novartis holds the two currently-approved products (Pluvicto, Lutathera) and is credited with Moat Signal "market share" evidence on this basis. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **TAM** | Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market. |
| **TTM (Trailing Twelve Months)** | The most recent four reported quarters summed together — used as the "current" basis for a metric instead of the last full fiscal year, especially useful when something material has changed partway through the fiscal year. |

**Sources (web search, this session):**
- [Dominance of Novartis in Radioligand Therapies — DelveInsight](https://www.delveinsight.com/blog/novartis-in-radioligand-therapies)
- [Novartis Eyes $5 Billion Pluvicto Opportunity — GuruFocus/Yahoo Finance](https://finance.yahoo.com/healthcare/articles/novartis-eyes-5-billion-pluvicto-133414369.html)
- [Radioligand Therapy Manufacturing Capacity: The CDMO Crunch — IntuitionLabs](https://intuitionlabs.ai/articles/radioligand-therapy-manufacturing-capacity)
- [Novartis delivered high single-digit sales growth, achieved 40% core margin and further advanced the pipeline in 2025 — Novartis media release](https://www.novartis.com/news/media-releases/novartis-delivered-high-single-digit-sales-growth-achieved-40-core-margin-and-further-advanced-pipeline-2025)
- [Novartis Q2 2026 Results: Kisqali, Kesimpta, and Pluvicto Drive Return to Sales Growth — BiotechReality](https://www.biotechreality.com/2026/07/novartis-q2-2026-results.html)
- [Novartis Statistics and Facts — market.us](https://market.us/statistics/pharmaceutical-industry/novartis/)
- [Ionis, Novartis' key experimental heart drug fails in late-stage trial — Yahoo Finance](https://finance.yahoo.com/healthcare/articles/ionis-novartis-key-experimental-heart-212036998.html)
- [Novartis trial failure raises stakes for Amgen and Eli Lilly in Lp(a) drug race — CNBC](https://www.cnbc.com/2026/09/08/novartis-cholesterol-setback-drug-race-eli-lilly-amgen.html)
- [Novartis, Ionis drug failure spurs questions about an emerging class of heart medicines — BioPharma Dive](https://www.biopharmadive.com/news/novartis-ionis-pelacarsen-lpa-horizon-study-results-fail/829736/)
- [Novartis agrees to acquire Avidity Biosciences — Novartis media release](https://www.novartis.com/news/media-releases/novartis-agrees-acquire-avidity-biosciences-innovator-rna-therapeutics-strengthening-its-late-stage-neuroscience-pipeline)
- [Novartis successfully completes acquisition of Avidity Biosciences — Novartis media release](https://www.novartis.com/news/media-releases/novartis-successfully-completes-acquisition-avidity-biosciences-strengthening-late-stage-neuroscience-pipeline-and-advancing-xrna-strategy)
- [Novartis Sells $11 Billion Bonds to Fund Avidity Acquisition — Bloomberg](https://www.bloomberg.com/news/articles/2026-03-16/novartis-offers-high-grade-debt-to-fund-12-billion-avidity-deal)

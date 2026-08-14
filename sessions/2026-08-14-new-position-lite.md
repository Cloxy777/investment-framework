# New Position Evaluation — LITE (Lumentum Holdings Inc.)

**Task:** NEW POSITION
**Date:** 14 Aug 2026
**10Y US Treasury Yield:** 4.65% (13 Aug 2026 close — most recent available)
**Rate Regime (informational only — Phase 02 not reached, see below):** 3.5–5% band → would be +5 modifier if scored
**Trigger:** Routine re-check of an existing not-in-portfolio watchlist entry ([watchlist/not-in-portfolio/LITE/LITE-2026-07-28.md](../watchlist/not-in-portfolio/LITE/LITE-2026-07-28.md)), whose own "next review trigger" pointed to Q4 FY2026 earnings. Those results were released 11 Aug 2026 — a Rule 9 mandatory re-valuation trigger (quarterly earnings release) — independent of the fact that the score last time already failed the gate. This is therefore a fresh full evaluation, not a routine no-change check.

---

## 1. Data gaps flagged

- **Free cash flow / operating cash flow / capex for FY2026** were not broken out in Lumentum's own Q4/FY2026 earnings press release (confirmed via direct fetch — the release covers income statement and balance sheet detail but not the full cash-flow statement). Sourced instead from stockanalysis.com's cash-flow-statement page, which is consistent with the same figures reported in Lumentum's other quarterly filings this year; the underlying 10-K (not yet fetchable — SEC EDGAR blocked automated fetch with an HTTP 403 on this session) would be the fully authoritative source once filed. Flagged, not invented — a specific numeric source is cited for every figure below.
- **Effective tax rate for FY2026 GAAP results** is not cleanly computable from the release (a GAAP net loss driven by a below-the-line, non-operating item makes "tax ÷ pretax income" not a meaningful ratio this year). NOPAT/ROIC below uses the same 21% statutory-rate convention as the 2026-07-28 LITE session for like-for-like comparability, flagged as an approximation.
- **Moat Signal evidence** — as in the 2026-07-28 session, only 2 of 5 signals could be backed by a specific citation within this session (market share, switching costs). The other 3 are marked FALSE for lack of a citable source, not asserted false as fact.
- **Net income normalization judgment call** (see §2, Profitability) — FY2026 GAAP net income is dominated by a one-time, non-cash $7,756.6M loss on debt extinguishment from equitizing convertible notes as the stock price surged. Per this framework's existing precedent (the **Gain on debt extinguishment** glossary entry, applied to DigitalOcean: "reflects a capital-structure transaction, not an improvement in the underlying business, and should be normalized out (Rule 6) before assessing sustainable profitability" — the identical logic applies in the loss direction here), the Profitability sub-score below adds back only this one specific, quantified, company-disclosed one-time item to GAAP net income — not the company's broader non-GAAP adjustment set (which also strips stock-based comp, intangible amortization, and other recurring items this framework doesn't substitute for GAAP by default, per the **Non-GAAP** glossary entry). Both the raw GAAP figure and the company's own full non-GAAP net income are shown alongside for cross-check.
- None of these gaps affect the outcome below — the Quality Score fails the 80.0+ gate by a wide margin (56.4 vs. 80.0) and a hard disqualifier fires independently of the weighted score, exactly as in the prior session.

---

## 2. Live Price (Rule 0)

Fetched directly via IBKR live market-data snapshot (not inferred from multiples), intraday, 14 Aug 2026:

| Field | Value |
|---|---|
| **Live price (intraday, most current)** | **$933.70** |
| Change vs. prior close | +$53.29 (+6.05%) |
| Prior close | $880.41 |
| Bid / Ask | $932.41 / $934.02 |
| 13-week high | $1,049.53 |
| 26-week / 52-week high | $1,085.68 |
| 52-week low | $111.20 |
| Market cap (live price × ~88.60M shares outstanding) | ~$82.7B |
| Beta (5yr) | 1.51 |

**Context (not scored, qualitative only):** LITE has risen from $676.53 (pre-market, 28 Jul 2026 — the prior session's price) to $933.70 today, a ~38% move over roughly two weeks, driven overwhelmingly by the 11 Aug 2026 Q4/full-year FY2026 earnings release (Q4 revenue $1.01B, +109% YoY, beating consensus; non-GAAP EPS $3.23 vs. $2.97 consensus) and press coverage of a possible FCC move to restrict Chinese-made optical transceivers, which would redirect hyperscaler demand toward Western suppliers including Lumentum. *(Sources: [StocksToTrade](https://stockstotrade.com/news/lumentum-holdings-inc-lite-news-2026_08_12-2/), [TradingKey](https://www.tradingkey.com/news/earnings/262097070-tradingkey), [Lumentum IR](https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-Fourth-Quarter-and-Full-Fiscal-Year-2026-Results/default.aspx).)*

---

## 3. Phase 01 — Quality Score (0–100.0)

Per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29 (unchanged since the 28 Jul session). All inputs below are **full fiscal year 2026** (ended 27 Jun 2026, the most recently completed fiscal year, reported 11 Aug 2026) unless otherwise marked.

### Hard disqualifiers — checked first

| Disqualifier | Result | Evidence |
|---|---|---|
| Not FCF-positive for 3+ consecutive years | **FIRES** | Annual FCF: FY2023 +$51.3M, **FY2024 −$108.3M, FY2025 −$104.7M**, FY2026 +$114.0M. Current rolling window (FY2024–FY2026, per the 2026-08-05 rolling-window clarification) has only 1 of 3 years positive — two consecutive negative years remain inside the window. No 3-consecutive-year positive streak exists yet. *(Source: [stockanalysis.com cash flow statement](https://stockanalysis.com/stocks/lite/financials/cash-flow-statement/).)* |
| Net Debt/EBITDA over threshold (2.5×) | Passes | Total debt (27 Jun 2026) $1,671M vs. cash & short-term investments $2,738.9M ($2,044.0M cash + $694.9M ST investments, matching the company's own disclosed "$2.7 billion total cash, cash equivalents, and short-term investments") → **Net Debt = −$1,067.9M (net cash)**. Negative net debt clamps this sub-score to its ceiling regardless of the EBITDA denominator. *(Source: [stockanalysis.com balance sheet](https://stockanalysis.com/stocks/lite/financials/balance-sheet/); company FY2026 cash figure confirmed via [earnings release](https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-Fourth-Quarter-and-Full-Fiscal-Year-2026-Results/default.aspx).)* |
| FCF/NI conversion ratio <70% for 2+ consecutive years, no growth-capex explanation | Ratio fails, but **carve-out applies** | FY2025 ratio: FCF −$104.7M / non-GAAP NI $146.4M = **−71.5%**. FY2026 ratio: FCF $114.0M / normalized NI $821.5M (see Profitability below) = **13.9%**. Both well under 70% — but there **is** a documented growth-capex explanation: FY2026 capex rose to $338.4M from $231.0M in FY2025 (+46.5%), tied to the newly acquired Greensboro, NC indium-phosphide fab (Lumentum's fifth InP fab) and a company-stated plan to raise InP output ~50% from Q4 CY2025 through Q4 CY2026. *(Sources: [Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/lumentum-ceo-says-the-indium-phosphide-shortage-will-become-worse-than-memory), [Yahoo Finance — Greensboro InP fab expansion](https://finance.yahoo.com/sectors/technology/articles/lumentum-lite-expands-greensboro-inp-230552387.html).)* Not independently decisive given the carve-out — but moot regardless, since the disqualifier above fires unconditionally with no such carve-out. |

**Result: hard disqualifier fires (not FCF-positive 3+ consecutive years).** Per quality-scoring.md, this fails the company regardless of the weighted score below. The full weighted calculation is still shown in full per "no black-box outputs."

### Sub-score calculations

**Profitability (25% weight)**
```
FY2026 Revenue = $3,014.0M
FY2026 GAAP Net Loss = −$6,935.1M, driven by a $7,756.6M one-time, non-cash loss on
  debt extinguishment (equitization of convertible notes as the share price surged)
Normalized Net Income (GAAP NI + specific one-time item add-back only)
  = −6,935.1 + 7,756.6 = $821.5M
  (cross-check: company's own full non-GAAP FY2026 net income = $782.3M — consistent)
Net Margin (normalized) = 821.5 / 3,014.0 = 27.26%

FY2026 GAAP EBIT (Operating Income) = $524.8M  (not distorted — the debt-extinguishment
  loss sits below the operating line)
NOPAT = EBIT × (1 − 21% statutory tax rate) = 524.8 × 0.79 = $414.6M
Invested Capital (27 Jun 2026, period-end) = Total Debt + Total Equity − (Cash + ST Investments)
  = 1,671.0 + 4,644.0 − 2,738.9 = $3,576.1M
ROIC = NOPAT / Invested Capital = 414.6 / 3,576.1 = 11.59%
  (cross-check: stockanalysis.com's own computed TTM ROIC = 15.17% — same direction, both
  well above the 28-Jul-session's 3.76%)

NetMargin_Component = clamp((27.26/30)×100) = 90.9
ROIC_Component       = clamp((11.59/30)×100) = 38.6
Profitability_Score (uncapped) = (90.9 + 38.6) / 2 = 64.8
```
**FCF-positive-3-years cap (40.0) binds** — the hard disqualifier above caps this sub-score at **40.0** regardless of the uncapped 64.8, per quality-scoring.md's explicit cap rule.

**Margins (15% weight)**
```
FY2026 GAAP Gross Margin = 41.7% (company-disclosed)
GrossMargin_Score = clamp((41.7/80)×100) = 52.1
```
No sub-40%-and-improving bonus applies (gross margin is already above the 40% threshold). Trend for context: 24.7% (FY2024) → 32.9% (FY2025) → 41.7% (FY2026) — a clear structural expansion, consistent with the operating-leverage story management describes, but the formula's bonus clause is specifically for names still below 40% and moving up.

**Growth (20% weight)**
```
Revenue 3yr CAGR (FY2023 $1,767.0M → FY2026 $3,014.0M, annual basis)
  = (3,014.0/1,767.0)^(1/3) − 1 = 19.49%/yr
Growth_Score (raw) = clamp((19.49/25)×100) = 78.0
+10 documented TAM-expansion evidence = 88.0
```
TAM-expansion evidence (independently verified): the global optical-transceiver market is estimated by LightCounting to grow to ~$26B in 2026 (+60% YoY from $16.5B in 2025), driven by AI-datacenter buildouts; Lumentum's own Q1 FY2027 guidance ($1.225B–$1.275B revenue) implies continued strong sequential growth on top of the just-reported 109% YoY quarter; the company is expanding InP laser capacity (fifth wafer fab, Greensboro NC) specifically to meet demand it says it cannot currently fully supply. *(Sources: [TradingKey](https://www.tradingkey.com/news/earnings/262097070-tradingkey), [Yahoo Finance — Greensboro fab](https://finance.yahoo.com/sectors/technology/articles/lumentum-lite-expands-greensboro-inp-230552387.html).)*

**Balance Sheet (15% weight)**
```
Net Debt (27 Jun 2026) = $1,671.0M − $2,738.9M = −$1,067.9M (net cash)
BalanceSheet_Score = clamp(100×(1 − NetDebt/EBITDA/4)) → negative NetDebt/EBITDA
  clamps the score to its ceiling regardless of the exact EBITDA denominator
BalanceSheet_Score = 100.0
```

**Moat Signal (15% weight)** — checklist, cited evidence only (unchanged from 28 Jul session — same underlying business, no new moat-relevant evidence surfaced this session):

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | Lumentum holds an estimated 50–60% share of the global EML (electro-absorption modulated laser) market and remains the only supplier shipping 200G-per-lane EMLs at volume — the component needed for next-gen 1.6T transceivers. *(Source: [MLQ.ai industry research](https://mlq.ai/research/lumentum-ai-optical-laser-supercycle/), consistent with the same citation used 28 Jul 2026.)* |
| Brand premium | FALSE | No specific price-increase-without-volume-loss data found for LITE in this session. |
| Network effect | FALSE | Not applicable — component/laser supplier, not a platform business. |
| Switching costs | **TRUE** | Hyperscaler/AI-infrastructure customers run 12–18 month supplier qualification cycles before a component is designed into production; once qualified in, switching to a re-qualified alternate supplier is a real, multi-quarter operational cost and risk — a documented industry-wide mechanism applying to Lumentum's own hyperscale customer base (Google, Amazon, Microsoft, Meta). *(Source: [Simply Wall St / industry analysis](https://simplywall.st/community/narratives/us/tech/nasdaq-lite/lumentum-holdings/3lr2sd1h-lumentum-an-ai-fueled-recovery-that-has-not-yet-earned-its-dollar74-billion-tag), [BeyondSPX](https://beyondspx.com/quote/LITE/news/lumentums-r300-optical-circuit-switch-sampling-with-hyperscale-customers-for-ai-data-centers).)* |
| Scale cost advantage | FALSE | Capacity leadership is documented (5th InP fab, 50%+ output expansion), but no cost-per-unit-vs-smaller-competitors citation was found in this session — the checklist's specific evidentiary bar. |

```
Moat_Score = (2/5) × 100 = 40.0
```

**FCF Quality (10% weight)**
```
FY2026 FCF = $114.0M   Normalized Net Income = $821.5M
FCF/NI Ratio = 114.0 / 821.5 = 13.87%
FCFQuality_Score = clamp(((0.1387 − 0.40)/0.60)×100) = 0.0 (floored)
```
(Using GAAP net income instead would make the ratio deeply negative and still floor to 0.0 — the conclusion is robust to this choice.)

### Final Quality Score

```
Quality Score = (40.0 × 0.25) + (52.1 × 0.15) + (88.0 × 0.20) + (100.0 × 0.15) + (40.0 × 0.15) + (0.0 × 0.10)
              = 10.000 + 7.815 + 17.600 + 15.000 + 6.000 + 0.000
              = 56.415 → rounded 56.4
```

## QUALITY SCORE: 56.4 / 100.0 — GATE: FAIL (threshold 80.0)

**Both an independent hard disqualifier (not FCF-positive 3+ consecutive years) and the weighted score (56.4, well under the 80.0 bar) fail LITE at Phase 01.** Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md), this stops the evaluation here — **Phase 02 valuation scoring, the Composite Score, and the fair-value/order-setup work are not computed.**

The score has improved substantially since the 28 Jul 2026 session (34.5 → 56.4), driven mechanically by: the Profitability sub-score's uncapped value rising from 35.7 to 64.8 (though still capped at 40.0 either way), the Growth sub-score rising from 10.0 to 88.0 as the FY2026 annual CAGR base finally captures the AI-driven revenue surge instead of pre-inflection years, and the Balance Sheet sub-score rising from 69.9 to 100.0 as the company moved to a net-cash position. **None of this changes the gate outcome** — the FCF-positive-3-year hard disqualifier is unaffected by any of these, and is structurally the last piece to clear: FY2026 is now confirmed FCF-positive, but FY2024 and FY2025 remain negative inside the rolling 3-year window until FY2027 also closes positive.

---

## 4. Why this matters despite the failing score — qualitative context

The Q4/FY2026 results are a genuine, large, verified operating inflection, not noise:
- Q4 FY2026 revenue $1.01B (+109% YoY), full FY2026 revenue $3.01B (+83.2% YoY), non-GAAP EPS $3.23 (Q4, +8.79% vs. consensus). Non-GAAP gross margin expanded to 50.4% in Q4, +1,260bps YoY. *(Source: [TradingKey](https://www.tradingkey.com/news/earnings/262097070-tradingkey).)*
- The GAAP headline net loss (−$6.9B, −$92.96/share) is not an operating problem — it is a one-time, non-cash accounting consequence of converting a large tranche of convertible notes into equity at a share price roughly 8–9× higher than when those notes were issued, which GAAP requires recognizing as a loss on debt extinguishment. It mechanically reduced outstanding debt (~$2.6B → ~$1.7B) and materially increased share count and equity — a real capital-structure shift, but not a signal of deteriorating business fundamentals. *(Sources: [StockTitan](https://www.stocktitan.net/news/LITE/lumentum-announces-fourth-quarter-and-full-fiscal-year-2026-k3q8m0wxnl6c.html), [TradingView](https://www.tradingview.com/news/tradingview:e5d72b4438190:0-lumentum-posts-1-01b-q4-revenue-3-01b-fy-revenue-gaap-loss-driven-by-7-8b-debt-extinguishment/).)*
- Guidance for Q1 FY2027 ($1.225B–$1.275B revenue, non-GAAP EPS $4.05–$4.35) implies the AI-optics demand cycle is not yet peaking, per management's own commentary that this "brings the company to its target operating model more than a quarter ahead of schedule." *(Source: [TradingKey](https://www.tradingkey.com/news/earnings/262097070-tradingkey).)* Guidance is cited here only as qualitative Rule 9 trigger context, never as a scored input, per [valuation-scoring.md](../framework/valuation-scoring.md#why-forward-guidance-is-not-a-sub-score).

**None of this changes the Quality Score gate outcome.** The framework's strict 80.0+ gate — and specifically the "3+ consecutive years FCF-positive" hard disqualifier, which carries no growth-capex or narrative exception — is deliberately designed to require an *established* multi-year track record before a name like this can be sized as a core position, however compelling the current trajectory looks. FY2026 being FCF-positive is real progress toward eventually clearing the gate, but it is one year, not three.

---

## 5. Recommendation

**PASS — watchlist only, do not enter a position now.** Quality Score 56.4 fails the 80.0+ gate, and a hard disqualifier (FCF not positive 3+ consecutive years) independently fires. No Composite Score exists to check against the Phase 03 action table, and no fair-value/order-setup work is produced, per [fair-value-methodology.md](../framework/fair-value-methodology.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md) (both gate that step on a passing Quality Score).

**Next review trigger:** the FCF-positive-3-consecutive-years disqualifier now resolves on a clear, trackable schedule — it requires FY2027 (ending ~June 2027) to also close FCF-positive, which would make FY2025–FY2027 the first fully-qualifying rolling window (FY2025 itself would still need to roll out of the window, so realistically the earliest possible gate-clear on this disqualifier alone is after FY2027's results are reported, likely August 2027, assuming FY2027 is positive). Re-score at each quarterly earnings release in the interim (Q1 FY2027 expected ~November 2026) to track the FCF trajectory and re-run the full weighted score, and immediately on any other Rule 9 fundamental trigger (guidance revision, M&A, management change, macro shift, or a >15% unexplained move).

---

## Glossary

- **CAGR (Compound Annual Growth Rate)** — the smoothed yearly growth rate implied by a start and end value over several years; used for the Growth sub-score's 3yr revenue calc.
- **Composite Score** — this framework's 50/50 blend of Quality Score and Valuation Score; not computed here since LITE never clears the Quality Score gate.
- **EBIT** — Earnings Before Interest and Taxes; operating profit before financing costs and taxes.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization; a rough proxy for cash operating profit, used in the Net Debt/EBITDA balance-sheet check.
- **EML (Electro-absorption Modulated Laser)** — a high-speed indium-phosphide laser component used in optical transceivers; Lumentum's ~50–60% share and sole-volume-supplier position in this component is the cited Market Share moat-signal evidence.
- **EPS** — Earnings Per Share; net income divided by shares outstanding.
- **FCF (Free Cash Flow)** — cash generated after running and maintaining the business; the FCF-positive-3-consecutive-years hard disqualifier is the deciding factor in this session.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income; checks whether reported accounting profit is actually turning into cash.
- **GAAP** — Generally Accepted Accounting Principles; the standard US accounting rulebook. Contrasted throughout this session with the company's own non-GAAP figures.
- **Gain on debt extinguishment / Loss on debt extinguishment** — a one-off, non-cash accounting gain or loss recognized when a company retires or converts its own debt (e.g. convertible notes) for less, or more, than its carrying value on the balance sheet — reflects a capital-structure transaction, not an improvement or deterioration in the underlying business, and is normalized out (Rule 6) before assessing sustainable profitability. Lumentum's FY2026 GAAP results were dominated by a $7,756.6M **loss** of this kind (the mirror-image case of DigitalOcean's previously-documented **gain**), from converting convertible notes into equity at a share price far above the notes' original conversion terms.
- **Gross Margin** — Gross Profit ÷ Revenue; one of the Quality Score's Margins sub-score inputs.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company outright regardless of its weighted sub-score total; the "not FCF-positive 3+ consecutive years" disqualifier fires for LITE.
- **Hyperscaler** — an operator of very-large-scale, globally-distributed cloud/data-center infrastructure (e.g. Microsoft Azure, AWS, Google Cloud); Lumentum's primary customer base.
- **Indium phosphide (InP)** — the compound semiconductor material used to make the lasers/photodetectors central to Lumentum's product line and the industry-wide AI-optics supply shortage.
- **Invested Capital** — the total capital (debt + equity, net of cash) put to work in a business; the denominator of the ROIC calculation.
- **M&A** — Mergers & Acquisitions.
- **Moat** — a durable competitive advantage protecting a business's profits from competitors; scored here via a 5-signal checklist.
- **Net Debt/EBITDA** — net debt divided by EBITDA; this framework's primary balance-sheet leverage gate. LITE passes this one (net cash position).
- **Net Margin** — Net Income ÷ Revenue; one of the Quality Score's Profitability sub-score inputs.
- **Non-GAAP** — a company's own adjusted presentation of a financial measure that strips out items management deems non-recurring or non-operational; self-reported and not independently audited to the same standard as GAAP. This framework scores off GAAP by default, with narrow, specifically-cited one-time-item add-backs (Rule 6) where a single quantified event (like this session's debt-extinguishment loss) would otherwise make the GAAP figure not meaningfully reflect the underlying business.
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate); the numerator used to compute ROIC.
- **Qualification cycle (supplier)** — the multi-month-to-multi-year process a hyperscaler/AI-hardware customer runs to validate and approve a component supplier before production use; cited as the Switching Costs moat-signal mechanism for LITE.
- **Quality Score** — this framework's 0.0–100.0 score across profitability, margins, growth, balance sheet, moat, and FCF quality; a company must clear 80.0 to proceed to valuation scoring. LITE scores 56.4 and fails the gate.
- **Rate Environment Gate** — the mandatory pre-check run before every Phase 02 valuation score; not reached in this session since Phase 01 fails first.
- **ROIC (Return on Invested Capital)** — how efficiently a company turns invested capital into profit; a core Quality Score input, computed here as NOPAT ÷ Invested Capital.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported results; superseded this session by full FY2026 annual figures now that the fiscal year has closed and been reported.

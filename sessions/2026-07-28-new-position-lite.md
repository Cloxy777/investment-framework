# New Position Evaluation — LITE (Lumentum Holdings Inc.)

**Task:** NEW POSITION
**Date:** 28 Jul 2026
**10Y US Treasury Yield:** 4.69% (FRED DGS10, 24 Jul 2026 close — most recent available)
**Rate Regime (informational only — Phase 02 not reached, see below):** 3.5–5% band → would be +5 modifier if scored
**Trigger:** Telegram channel `t.me/FinnInvestChannel`, post FinnInvestChannel/2999 (~10:31 UTC 2026-07-28) reporting CEO Michael Hurlston's comments that an indium-phosphide (InP) laser shortage for AI could exceed the memory-chip shortage, and that NVIDIA has invested in both Lumentum and competitor Coherent Corp (COHR). No prior watchlist entry existed for LITE, so per the telegram-scan trigger rule this is a full `/new-position` evaluation. **The Telegram post itself was used only as the trigger — every figure below was independently fetched from Yahoo Finance (yfinance-equivalent quoteSummary/fundamentals-timeseries endpoints) and cross-checked against primary-source press releases/SEC filings, never taken from the post's text.**

---

## 1. Data gaps flagged

- **5yr historical PE range/average** was not computed — moot, since the Quality Score gate fails before Phase 02 (valuation scoring) is reached; not fetched to avoid unnecessary API load.
- **TTM effective tax rate is distorted by a one-off item** (see §2, Profitability): TTM Net Income ($439.9M) exceeds TTM Pretax Income ($274.1M), implying a **net tax benefit of ~$165.8M** over the trailing twelve months. Drilling into the quarterly breakdown, essentially all of this benefit landed in the quarter ended 2025-06-30 (Q4 FY2025: Net Income $213.3M vs. Pretax Income −$11.4M — a ~$224.7M gap). This is consistent with the pattern this framework already documents under **Deferred tax valuation allowance release** (glossary) — a company just turning durably profitable after loss years releasing a prior write-down on its deferred tax assets — but I have **not** read the actual 10-K/10-Q tax-footnote language confirming that specific mechanism, so I'm flagging this as a plausible, not confirmed, explanation. Either way, the real, verified numbers (NI, pretax income, per-quarter breakdown) are not invented — only the causal label is a flagged hypothesis. Net effect: TTM Net Margin and ROIC below are likely **overstated**, not understated, by this one-off.
- **Moat Signal evidence** — only 2 of 5 signals could be backed by a specific citation within this session (see §2, Moat). The other 3 (brand premium, network effect, scale cost advantage) are marked FALSE for lack of a citable source, not asserted false as a matter of fact — a deeper company-specific search could change this in a future re-score.
- None of these gaps affect the outcome below — the Quality Score fails the 80.0+ gate by a wide margin (34.5 vs. 80.0) and a hard disqualifier fires independently of the weighted score.

---

## 2. Live Price (Rule 0)

Fetched directly from Yahoo Finance quote/chart endpoints (not inferred from multiples), at 12:22 UTC 2026-07-28 — market was in **pre-market** (NASDAQ regular session opens 13:30 UTC):

| Field | Value |
|---|---|
| **Live price (pre-market, most current)** | **$676.53** (−4.98% vs. prior regular close) |
| Prior regular-session close (27 Jul 2026) | $711.96 (−6.69% vs. 24 Jul 2026 close) |
| Close before that (24 Jul 2026) | $762.99 |
| Regular-session day range (27 Jul) | $697.97 – $770.30 |
| 52-week range | $101.61 – $1,085.68 |
| Analyst consensus PT (25 analysts) | Mean $1,104.89 / Median $1,100.00 / High $1,400.00 / Low $600.00 / Consensus "Buy" |
| Market cap (at $711.96 close) | ~$55.4B |
| Beta | 1.48 |

**Context (not scored, qualitative only):** LITE has fallen ~11.3% cumulatively over the two most recent sessions plus pre-market (from $762.99 to $676.53), continuing a pullback that has taken the stock ~38% off its 52-week high of $1,085.68 — this despite Q3 FY2026 results (reported 5 May 2026) beating on both revenue and EPS, with no guidance cut, lost customer, or fundamental deterioration identified in press coverage searched for this session. This reads as a valuation-driven "priced-for-perfection" pullback on an intact operating thesis, not a Rule 9 fundamental trigger — flagged for context only, since it does not affect the Quality Score gate result below either way. *(Sources: [GuruFocus](https://www.gurufocus.com/news/8981496/lumentum-holdings-inc-lite-stock-down-67-but-still-overvalued-gf-score-61100), [TIKR](https://www.tikr.com/blog/lumentum-stock-has-fallen-33-from-its-high-is-the-optics-selloff-a-gift-or-a-warning).)*

---

## 3. Phase 01 — Quality Score (0–100.0)

Per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29. All inputs below are TTM (trailing twelve months ended 2026-03-31, the most recent reported quarter) unless marked "annual" (fiscal year ends late June).

### Hard disqualifiers — checked first

| Disqualifier | Result | Evidence |
|---|---|---|
| Not FCF-positive for 3+ consecutive years | **FIRES** | Annual FCF: FY2022 +$368.1M, FY2023 +$51.3M, **FY2024 −$112.3M, FY2025 −$104.7M** (2 consecutive negative years), TTM (Mar26) +$114.0M. The most recent 3 full/partial years (FY2024, FY2025, TTM) show only 1 of 3 positive — no 3-consecutive-year positive track record exists, even counting the current recovery. |
| Net Debt/EBITDA over threshold (2.5×) | Passes | Net Debt (2026-03-31) $664.0M ÷ TTM EBITDA $552.2M = **1.20×** — well under 2.5×. (Net debt fell sharply this quarter due to the NVIDIA cash injection — see §4.) |
| FCF/NI conversion ratio <70% for 2+ consecutive years, no growth-capex explanation | Fires on the ratio math, but **mitigated** | FY2024 ratio 20.5% (both FCF and NI negative), FY2025 ratio −404.2% (FCF negative, NI barely positive) — both under 70%. However, there **is** a documented growth-capex explanation: CapEx roughly doubled from $91.2M (FY2022) to $231.0M (FY2025), tied to InP wafer-fab capacity expansion and a new Thailand transceiver facility (see §4, cited sources). Given the exception clause, I'm not treating this one as independently decisive — but note it doesn't rescue the company either, since the first disqualifier above fires unconditionally with no such carve-out. |

**Result: hard disqualifier fires (not FCF-positive 3+ consecutive years).** Per quality-scoring.md, this fails the company regardless of the weighted score below. The full weighted calculation is still shown in full per "no black-box outputs."

### Sub-score calculations

**Profitability (25% weight)**
```
TTM Revenue = $2,488.4M   TTM Net Income = $439.9M   Net Margin = 439.9 / 2,488.4 = 17.68%
TTM EBIT = $297.7M   NOPAT = EBIT × (1 − 21% statutory tax rate) = 297.7 × 0.79 = $235.2M
Invested Capital (2026-03-31, period-end) = $6,255.2M
ROIC = NOPAT / Invested Capital = 235.2 / 6,255.2 = 3.76%

NetMargin_Component = clamp((17.68/30)×100) = 58.9
ROIC_Component       = clamp((3.76/30)×100)  = 12.5
Profitability_Score  = (58.9 + 12.5) / 2 = 35.7
```
*Sensitivity: using average invested capital across the trailing 4 quarters ($4,530.3M, since the $2B NVIDIA cash injection landed only at period-end and isn't yet productively deployed) gives ROIC 5.19% and Profitability_Score 38.1 — doesn't change the conclusion.*
FCF-positive-3-years cap (40.0) does not bind — 35.7 is already below it.

**Margins (15% weight)**
```
TTM Gross Profit = $938.5M   Gross Margin = 938.5 / 2,488.4 = 37.71%
GrossMargin_Score = clamp((37.71/80)×100) = 47.1
```
No structural-trend bonus applied: annual gross margin went 46.0% (FY22) → 32.2% (FY23) → 18.5% (FY24) → 28.0% (FY25) → 37.7% (TTM) — a deep cyclical trough-and-recovery (industry inventory correction/downturn, then AI-driven demand snap-back), not a steady multi-year structural expansion as the modifier requires.

**Growth (20% weight)**
```
Revenue 3yr CAGR (FY2022 $1,712.6M → FY2025 $1,645.0M, annual basis) = (1,645.0/1,712.6)^(1/3) − 1 = −1.33%/yr
Growth_Score (raw) = clamp((−1.33/25)×100) = 0.0 (floored)
+10 documented TAM-expansion evidence (see below) = 10.0
```
TAM-expansion evidence (independently verified, not from the Telegram post): NVIDIA's $2B strategic equity investment plus multi-year purchase commitments and capacity-access rights (SEC 8-K, 2 Mar 2026; [Nvidia Newsroom](https://nvidianews.nvidia.com/news/nvidia-announces-strategic-partnership-with-lumentum-to-develop-state-of-the-art-optics-technology); [Wilson Sonsini](https://www.wsgr.com/en/insights/wilson-sonsini-advises-lumentum-on-strategic-partnership-and-related-dollar2-billion-equity-investment-from-nvidia.html)); quarterly revenue accelerating from $425.2M (Mar25) → $480.7M → $533.8M → $665.5M → $808.4M (Mar26), +90.1% YoY in the most recent quarter ([Q3 FY2026 results](https://www.businesswire.com/news/home/20260505865570/en/Lumentum-Announces-Third-Quarter-of-Fiscal-Year-2026-Financial-Results)). **Note:** this large recent acceleration is exactly why the fiscal-year-CAGR formula (which ends at FY2025, before the current supercycle) reads as flat-to-declining — the +10 modifier is the mechanism by which the framework credits the current trajectory without overriding the multi-year, non-cherry-picked base calculation.

**Balance Sheet (15% weight)**
```
Net Debt (2026-03-31) = $664.0M   TTM EBITDA = $552.2M
Net Debt/EBITDA = 664.0 / 552.2 = 1.20×
BalanceSheet_Score = clamp(100×(1 − 1.20/4)) = 69.9
```

**Moat Signal (15% weight)** — checklist, cited evidence only:

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | Lumentum holds an estimated 50–60% share of EML (electro-absorption modulated laser) components and is currently the only supplier shipping 200G-per-lane EMLs at volume — the part needed for next-gen 1.6T transceivers. *(Source: [MLQ.ai industry research](https://mlq.ai/research/lumentum-ai-optical-laser-supercycle/).)* |
| Brand premium | FALSE | No specific price-increase-without-volume-loss data found for LITE in this session. |
| Network effect | FALSE | Not applicable — component/laser supplier, not a platform business. |
| Switching costs | **TRUE** | Datacenter-optics customers (hyperscalers, AI-infrastructure vendors) run 12–24 month supplier qualification cycles before a component can be designed into production; once qualified in, re-qualifying an alternate supplier is a real operational cost/risk. This is a documented industry-wide mechanism (already cited for peer Coherent Corp in this framework's same-day 2026-07-28 COHR session) that applies equally to Lumentum, whose own business description confirms it supplies "cloud data center operators, AI/ML infrastructure providers, and network equipment manufacturer customers" — the identical qualification-heavy customer base. |
| Scale cost advantage | FALSE | Fab capacity expansion is documented (see §4), but no cost-per-unit-vs-smaller-competitors citation was found in this session. |

```
Moat_Score = (2/5) × 100 = 40.0
```

**FCF Quality (10% weight)**
```
TTM FCF = $114.0M   TTM Net Income = $439.9M
FCF/NI Ratio = 114.0 / 439.9 = 25.91%
FCFQuality_Score = clamp(((0.2591 − 0.40)/0.60)×100) = 0.0 (floored)
```

### Final Quality Score

```
Quality Score = (35.7 × 0.25) + (47.1 × 0.15) + (10.0 × 0.20) + (69.9 × 0.15) + (40.0 × 0.15) + (0.0 × 0.10)
              = 8.925 + 7.065 + 2.000 + 10.485 + 6.000 + 0.000
              = 34.475 → rounded 34.5
```

## QUALITY SCORE: 34.5 / 100.0 — GATE: FAIL (threshold 80.0)

**Both an independent hard disqualifier (not FCF-positive 3+ consecutive years) and the weighted score (34.5, less than half the 80.0 bar) fail LITE at Phase 01.** Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md), this stops the evaluation here — **Phase 02 valuation scoring, the Composite Score, and the fair-value/order-setup work are not computed.** This is the correct, complete outcome for a gate this strict, not an incomplete session.

---

## 4. Why this matters despite the failing score — qualitative context

The Telegram trigger's underlying claim is independently verified as real and material, not hype:
- NVIDIA announced (2 Mar 2026) a **$2 billion strategic equity investment** in Lumentum via a private placement of 2,876,415 shares of Series A Convertible Preferred Stock at $695.31/share, alongside multi-year purchase commitments and future capacity-access rights, to secure InP laser supply for AI infrastructure. *(Sources: [SEC 8-K](https://www.sec.gov/Archives/edgar/data/1633978/000119312526085412/d41019dex991.htm), [Nvidia Newsroom](https://nvidianews.nvidia.com/news/nvidia-announces-strategic-partnership-with-lumentum-to-develop-state-of-the-art-optics-technology), [CNBC](https://www.cnbc.com/2026/03/02/nvidia-investment-coherent-lumentum.html).)*
- This shows up directly in the verified balance-sheet data pulled for this session: cash & short-term investments jumped **+$2.02B** in the quarter ended 2026-03-31 (to $3.17B total), which the company's own Q3 FY2026 release attributes to "proceeds from the issuance of Series A Convertible Preferred Stock in March 2026." Net debt fell from $2.63B (Dec-25) to $0.66B (Mar-26) as a direct result.
- The CEO's indium-phosphide shortage comments and the industry-wide demand/supply imbalance (demand outpacing InP laser supply by an estimated 25–30%) are corroborated by independent industry research, not just the Telegram post. *(Source: [MLQ.ai](https://mlq.ai/research/lumentum-ai-optical-laser-supercycle/).)*
- Revenue and margins are genuinely inflecting: quarterly revenue +90.1% YoY, GAAP operating margin 21.6% in the most recent quarter — a real, fast-moving business improvement.

**None of this changes the Quality Score outcome.** The framework's strict 80.0+ gate — and specifically the flat "3+ consecutive years FCF-positive" hard disqualifier, which carries no growth-capex or narrative exception — is deliberately designed to keep a story this compelling from bypassing the requirement for an *established* multi-year quality track record. LITE's FY2024–FY2025 FCF-negative stretch is a real, recent fact; the current recovery (driven by a single strategic customer's capital injection and a fast-moving demand cycle) has not yet run long enough to satisfy it. This is exactly the kind of case the gate exists to catch, per its own stated design rationale in quality-scoring.md.

---

## 5. Recommendation

**PASS — watchlist only, do not enter a position now.** Quality Score 34.5 fails the 80.0+ gate by a wide margin, and a hard disqualifier (FCF not positive 3+ consecutive years) independently fires. No Composite Score exists to check against the Phase 03 action table, and no fair-value/order-setup work is produced, per [fair-value-methodology.md](../framework/fair-value-methodology.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md) (both gate that step on a passing Quality Score).

**Next review trigger:** the FCF-positive-3-consecutive-years disqualifier is a track-record problem that resolves only with time and continued execution — re-score at the next quarterly earnings release (Q4 FY2026, expected early-to-mid September 2026) once a full additional quarter of the post-NVIDIA-investment trajectory is reported, to see whether FY2026 closes as a full FCF-positive fiscal year (which would still leave FY2024/FY2025 as the disqualifying pair until FY2027 closes positive too, extending the earliest possible gate-clear date). Also re-score immediately on any Rule 9 fundamental trigger (further NVIDIA/Coherent-related guidance revision, M&A, or a >15% unexplained move).

---

## Glossary

- **10-Q (Quarterly Report)** — the quarterly SEC financial filing used here to source TTM/quarterly figures between annual reports.
- **CAGR (Compound Annual Growth Rate)** — the smoothed yearly growth rate implied by a start and end value over several years; used for the Growth sub-score's 3yr revenue calc.
- **Composite Score** — this framework's 50/50 blend of Quality Score and Valuation Score; not computed here since LITE never clears the Quality Score gate.
- **Deferred tax valuation allowance release** — a one-off accounting event where a company reverses a prior write-down on its deferred tax assets once it judges them usable again, producing an artificially low (or negative) effective tax rate and inflated net income in the recognition period — flagged as the likely (not confirmed) explanation for LITE's TTM net income exceeding its TTM pretax income.
- **EBIT** — Earnings Before Interest and Taxes; operating profit before financing costs and taxes.
- **EML (Electro-absorption Modulated Laser)** — a high-speed indium-phosphide laser component used in optical transceivers; Lumentum's ~50–60% share and sole-volume-supplier position in this component is the cited Market Share moat-signal evidence.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization; a rough proxy for cash operating profit, used in the Net Debt/EBITDA balance-sheet check.
- **EPS** — Earnings Per Share; net income divided by shares outstanding.
- **FCF (Free Cash Flow)** — cash generated after running and maintaining the business; the FCF-positive-3-consecutive-years hard disqualifier is the deciding factor in this session.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income; checks whether reported accounting profit is actually turning into cash. LITE's TTM ratio (25.9%) and prior-two-year ratios are both well under the 70% quality threshold.
- **Gross Margin** — Gross Profit ÷ Revenue; one of the Quality Score's Margins sub-score inputs.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company outright regardless of its weighted sub-score total; the "not FCF-positive 3+ consecutive years" disqualifier fires for LITE.
- **Indium phosphide (InP)** — the compound semiconductor material used to make the lasers/photodetectors at the center of the AI-optics supply shortage referenced in the Telegram trigger and central to Lumentum's product line.
- **Invested Capital** — the total capital (debt + equity, net of cash) put to work in a business; the denominator of the ROIC calculation.
- **M&A** — Mergers & Acquisitions.
- **Moat** — a durable competitive advantage protecting a business's profits from competitors; scored here via a 5-signal checklist.
- **Net Debt/EBITDA** — net debt divided by EBITDA; this framework's primary balance-sheet leverage gate. LITE passes this one (1.20× vs. 2.5× threshold).
- **Net Margin** — Net Income ÷ Revenue; one of the Quality Score's Profitability sub-score inputs.
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate); the numerator used to compute ROIC.
- **Qualification cycle (supplier)** — the multi-month-to-multi-year process a hyperscaler/AI-hardware customer runs to validate and approve a component supplier before production use; cited as the Switching Costs moat-signal mechanism for LITE.
- **Quality Score** — this framework's 0.0–100.0 score across profitability, margins, growth, balance sheet, moat, and FCF quality; a company must clear 80.0 to proceed to valuation scoring. LITE scores 34.5 and fails the gate.
- **ROIC (Return on Invested Capital)** — how efficiently a company turns invested capital into profit; a core Quality Score input, computed here as NOPAT ÷ Invested Capital.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported results, as used throughout this session's sub-score calculations.

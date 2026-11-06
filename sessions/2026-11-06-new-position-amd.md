# NEW POSITION — Advanced Micro Devices (AMD) — 2026-11-06

**Task type:** NEW POSITION (3rd evaluation; prior: 06-30, 07-20 — both Phase 01 FAIL) · **Not held**
**Outcome in one line:** Quality Score **57.3** (was 58.7) — **FAILS the 80.0+ gate** → **PASS**, no Phase 02 / Composite / order setup.
**10Y Treasury / Rate Regime Modifier:** not needed — the Rate Gate belongs to Phase 02, which is not reached.

## 1. Why this ran
Q3 FY2026 earnings (reported 2026-11-03) are the first new quarterly filing since the prior AMD sessions and the named review trigger (a) in [the watchlist entry](../watchlist/not-in-portfolio/AMD/AMD-2026-06-30.md).

## 2. Live price (Rule 0)
| Item | Value |
|---|---|
| **Live price** | **$424.05** (bid 424.05 / ask 424.55, REALTIME, IBKR contract 4391), +$19.65 / +4.86% today |
| 52-week range | $188.22 – $658.52 → live price is **−35.6% below the 52-week high** |
| vs 07-20 session | $517.86 → $424.05 (−18.1%) |

**Open item — cause of the drawdown is NOT verified.** Two searches returned no 2026 coverage explaining it; the only 2026 reaction headline found (Stocktwits, unopened) mentions an ~8% post-Q3 slide despite record revenue. Not used as an input; the framework does not act on price alone.

**Data caveat:** `fetch_fundamentals` priced the market cap at the **prior close ($404.40)**, not the live $424.05. This affects only price-based outputs (FCF yield, EV/EBIT, forward PE), which are Phase 02 inputs and are **not used** here. The Quality inputs below are price-independent.

## 3. Fundamentals script output (verbatim)
```
Market Cap            = 663,251,320,832
Enterprise Value      = 656,686,252,032
Shares Outstanding    = 1,640,087,251
Forward PE            = 24.100
FCF Yield %           = 1.064
EV/EBIT               = 79.415
Net Margin %          = 16.769
Gross Margin %        = 53.715
ROIC % (NOPAT/InvCap) = 11.886  [tax_rate=0.0482, NOPAT=7,870,715,450, InvestedCapital=66,221,000,000]
Revenue 3yr CAGR %    = 13.644
Net Debt/EBITDA       = -0.152  [EBITDA_ttm=11,143,000,064]
FCF/NI TTM % (plain)  = 92.611
(FCF - SBC)/NI TTM %  = 66.374  [reported NI]
SBC yield %           = 0.301
Gross buyback yield % = 0.334
FCF/NI annual (oldest first) = [236.0%, 131.3%, 146.6%, 155.4%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 47.173 / 15.552 / 92.007  (n=20 quarters)

SBC block (TTM, advisory — no score effect)
  SBC 1,999,000,000.0   FCF 7,056,000,000.0   Market cap 663,251,320,832.0
  SBC/FCF = 28.3%
  FCF yield (reported)  = 1.06%
  FCF yield after SBC   = 0.76%
Advisory flags (no score effect)
  cycle_peak             UNKNOWN   EPS TTM now or 1y ago unavailable
  value_trap_candidate   UNKNOWN   forward PE or trailing EPS growth unavailable
```
**Advisory flags handling:** no flag was raised. Both `UNKNOWN` results are logged as **data gaps** (yfinance lacks 8 consecutive quarters of diluted EPS). `MULTIPLE_CEILING` was not run: it needs the forward PE and consensus EPS growth, which only matter once a name clears the gate. SBC/FCF 28.3% is well under the 100% hard disqualifier.

Notes on the inputs: ROIC rose from 6.71% (07-20, hand-reconstructed, normalised-tax) to 11.89% (script, effective tax 4.82%) — a methodology/tax-rate difference, **not** a like-for-like improvement; TTM net income carries large non-operating items (see §4). Net Debt/EBITDA −0.152 is the script's value; the Q3 balance sheet shows $15.8B cash + short-term investments vs $7.1B debt (net cash either way, so the Balance Sheet sub-score is 100 regardless).

## 4. Q3 FY2026 facts used (AMD press release 2026-11-03, [ir.amd.com](https://ir.amd.com/news-events/press-releases/detail/1303/amd-reports-third-quarter-2026-financial-results); cross-checked by search summaries)
- Revenue $13,377M (+45% YoY); GAAP gross margin 54%; GAAP operating income $2,832M; GAAP net income $2,428M; GAAP diluted EPS $1.46.
- **Data Center revenue $8,546M, +97% YoY** (segment operating income $2,882M); Q4 revenue guidance ~$17B ±3% (~+66% YoY). Instinct/MI450 revenue not broken out.
- Anthropic, Meta, Microsoft, OpenAI and Oracle Cloud Infrastructure run workloads on first Helios systems.
- **Non-operating items inside GAAP net income:** income-tax *benefit* of $555M and a $1,097M warrant fair-value charge (other expense $(902)M). These are not normalised here (no full-TTM amounts sourced; `ni_normalised` = false). Net effect on the verdict: none — see §5 sensitivity.
- Q3 FCF only $554M (capex $648M; inventories up to $11.5B from $7.9B at Dec-2025; debt up to $7.1B from $3.2B in Q2). Worth watching, not scored here.

## 5. Phase 01 — Quality Score (script output, verbatim)
Moat evidence: Mercury Research Q2 2026 (via HotHardware, cloudnews.tech, TechSpot, TweakTown) — AMD x86 share 34.1% incl. IoT/SoC (30.7% ex-IoT; Intel below 70% for the first time since 1995), server units 34.5%, client 30.3% (up from 29.6% in Q1). Credited as the one TRUE signal; AI-accelerator share vs NVIDIA is still not evidenced as gaining. The other four signals have no cited evidence (Helios customer wins are not documented lock-in).

```
Profitability: NetMargin 55.90, ROIC 39.62 → 47.76
Margins: 67.14
Growth: clamp(13.644/25×100)=54.58 +10 (TAM evidence: Data Center +97%, Q4 guide) = 64.58
Balance Sheet: 100.00
Moat: 1/5 → 20.00
FCF Quality: (FCF−SBC)/NI = 66.37% → 43.96
Quality Score = 47.76×0.25 + 67.14×0.15 + 64.58×0.20 + 100×0.15 + 20×0.15 + 43.96×0.10 = 57.322 → 57.3
```
**FAILS the 80.0+ gate.** No hard disqualifier fires (FCF/NI annual 131–236%; FCF-positive 3+ years; net cash; SBC/FCF 28.3%).

**Sensitivity:** even crediting all five moat signals (Moat 100 → +12.0 points) the score would be ~69.3, still below 80. The gap is structural: ROIC (39.6 component), moat evidence, and the SBC-adjusted FCF conversion. Score fell 1.4 pts vs 07-20 mainly because FCF Quality now deducts SBC (methodology 2026-10-12, which postdates the 07-20 session) — 07-20 scored 100.00 on plain FCF/NI.

## 6. Recommendation
**PASS — do not open a position.** No Rate Gate, valuation score, Composite Score, fair value or order setup were computed (the strict gate stops here). Business momentum is genuinely strong (Data Center nearly doubled), but the framework scores quality on ROIC, moat evidence and cash conversion, and growth momentum doesn't compensate.

## 7. Next review trigger
(a) Q4 FY2026 earnings (~Feb 2027): ROIC trend, Data Center growth vs NVIDIA, FCF recovery from the Q3 dip; (b) cited AI-accelerator share evidence (realized, not projected); (c) sustained ROIC improvement on a like-for-like basis; (d) management change / material M&A; (e) the unexplained −36% drawdown from the 52-week high — if a cause is verified as fundamental, treat it as a Rule 9 event. No stale-score mark exists (Phase 01 FAIL entries aren't flagged).

## Glossary
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality) instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. See [quality-scoring.md](quality-scoring.md).
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **SBC (Stock-Based Compensation)** — Employee pay in the form of company shares or stock options rather than cash. A non-cash expense added back in cash-flow statements (inflating FCF relative to GAAP net income), but a real economic cost to existing shareholders through ongoing dilution — worth tracking alongside FCF/NI conversion and share-count trend, not just the headline FCF figure. Since the 2026-10-12 methodology it is treated as a cost in both the FCF yield (Valuation) and FCF Quality (Quality).
- **Data Center segment (AMD)** — AMD's reporting segment covering EPYC server CPUs and Instinct AI accelerator GPUs sold to cloud/enterprise data centers — the part of the business driving AMD's growth (Q3 FY2026 revenue $8,546M, +97% YoY). *(New term.)*
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Mercury Research** — An independent semiconductor-industry market-research firm publishing quarterly x86 CPU market-share estimates (split by client/desktop and server/data-center) — a third-party (non-company-sourced) citation basis for Moat Signal "market share" evidence in this framework, e.g. AMD's Q1 2026 x86 share gains against Intel cited in this framework's 2026-07-20 INTC session. *(New term.)*
- **Hard disqualifier** — One of three Quality Score conditions ([quality-scoring.md](quality-scoring.md)) that fails a company regardless of its weighted sub-score total: not FCF-positive for 3+ consecutive years, Net Debt/EBITDA over its applicable threshold, or an FCF/Net Income conversion ratio under 70% for 2+ consecutive years without a documented growth-capex explanation. A weighted average can't average away an outright balance-sheet or cash-flow-quality failure.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **x86** — The dominant CPU instruction set architecture (ISA) originally developed by Intel, also licensed/cross-licensed to AMD — the software-compatibility ecosystem (Windows and most enterprise Linux software run natively on it) underlying the Network Effect and Switching Costs moat-signal discussion in this framework's 2026-07-20 INTC session. Distinct from the competing ARM ISA. *(New term.)*
- **Helios** — AMD's first rack-scale AI system (announced 2026-07-20), integrating 72 AMD Instinct MI455X GPUs, 6th-gen AMD EPYC "Venice" CPUs, Pensando DPUs, and the ROCm software stack into one product, positioned to compete with NVIDIA's rack-scale AI systems. Microsoft Azure is its first publicly announced customer, with shipments targeted for H2 2026 — the news that triggered this framework's 2026-07-20 AMD re-evaluation session. *(New term.)*
- **Warrant (fair-value adjustment)** — A security giving its holder the right to buy stock at a preset price, commonly issued to SPAC sponsors/investors as a sweetener. When GAAP requires a warrant to be classified as a liability rather than equity (common in SPAC-era capital structures), it must be marked to fair value every reporting period, and the resulting gain/loss (larger when the stock is more volatile) runs through the income statement as a non-cash item unrelated to operating performance. Trump Media & Technology Group's (DJT) FY2024 results included a $225.9M non-cash `FairValueAdjustmentOfWarrants` loss, a legacy of its March 2024 de-SPAC merger structure — cited in this framework's 2026-07-17 DJT session as one reason GAAP net income has run far more negative than actual cash burn (FCF) in some periods. *(New term.)*
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. A low ratio without a CapEx explanation is a red flag for earnings-quality games (see the Valeant/Wirecard cases in [graveyard-audit.md](graveyard-audit.md)).
- **Forward PE** — Price ÷ next twelve months' *expected* earnings per share (vs. Trailing PE, which uses the last twelve months' actual earnings).
- **Composite Score** — This framework's single ranking number (0.0–100.0, 0.0 = most attractive) blending the Quality Score and the Valuation Score 50/50 — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — computed only for companies that have already cleared the 80.0+ Quality Score gate. Used against the Phase 03/05 action tables instead of the raw valuation score. See [valuation-scoring.md](valuation-scoring.md).
- **EV/EBIT, EV/EBITDA** — Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure.

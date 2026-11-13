# NEW POSITION — Advanced Micro Devices (AMD) — 2026-11-13

**Task type:** NEW POSITION (4th evaluation; prior: 06-30, 07-20, 11-06 — all Phase 01 FAIL) · **Not held**
**Outcome in one line:** Quality Score **57.3** (unchanged vs 11-06) — **FAILS the 80.0+ gate** → **PASS**. No Phase 02 / Composite / order setup.
**10Y Treasury / Rate Regime Modifier:** not needed — the Rate Gate belongs to Phase 02, which is not reached.

## 1. Why this ran
User invoked `/new-position AMD`. No new filing since the 11-06 session (Q3 FY2026 reported 2026-11-03; Q4 due ~Feb 2027). The only change is price.

## 2. Live price (Rule 0)
| Item | Value |
|---|---|
| **Live price** | **$570.64** (bid 570.50 / ask 570.99, REALTIME, IBKR contract 4391), −$14.66 / −2.5% today |
| 52-week range | $188.22 – $658.52 → −13.3% below the 52-week high |
| vs 11-06 session | $424.05 → $570.64 (**+34.6% in 7 days**) |

**Open item — cause of the +34.6% move is NOT verified** (and the earlier −36% drawdown cause is still unverified). This exceeds Rule 9's >15% unexplained-move threshold, but a Rule 9 re-score only re-runs the same inputs: no new financials exist, so the Quality Score cannot change. The cause is not searched here because it cannot move a Phase 01 sub-score; flagged for the next review. Price is not used as a Quality input.

## 3. Fundamentals script output (verbatim, `python -m scripts.fetch_fundamentals AMD`)
```
Market Cap            = 959,943,081,984
Enterprise Value      = 953,378,078,720
Shares Outstanding    = 1,640,087,251
Forward PE            = 33.085
FCF Yield %           = 0.735
EV/EBIT               = 115.295
Net Margin %          = 16.769
Gross Margin %        = 53.715
ROIC % (NOPAT/InvCap) = 11.886  [tax_rate=0.0482, NOPAT=7,870,715,450, InvestedCapital=66,221,000,000]
Revenue 3yr CAGR %    = 13.644
Net Debt/EBITDA       = -0.152  [EBITDA_ttm=11,143,000,064]
FCF/NI TTM % (plain)  = 92.611
(FCF - SBC)/NI TTM %  = 66.374  [reported NI]
SBC yield %           = 0.208
Gross buyback yield % = 0.231
FCF/NI annual (oldest first) = [236.0%, 131.3%, 146.6%, 155.4%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 47.173 / 15.552 / 92.007  (n=20 quarters)

SBC block (TTM, advisory — no score effect)
  SBC 1,999,000,000.0   FCF 7,056,000,000.0   Market cap 959,943,081,984.0
  SBC/FCF = 28.3%
  FCF yield (reported)  = 0.74%
  FCF yield after SBC   = 0.53%
Advisory flags (no score effect)
  cycle_peak             UNKNOWN   EPS TTM now or 1y ago unavailable
  value_trap_candidate   UNKNOWN   forward PE or trailing EPS growth unavailable
```
Every quality input is identical to 11-06 (price-independent); only price-based outputs moved.

**Advisory flags handling:** none raised. `cycle_peak` and `value_trap_candidate` are `UNKNOWN` → logged as **data gaps** (yfinance lacks 8 consecutive quarters of diluted EPS). `MULTIPLE_CEILING` **not run**: it needs a sourced consensus EPS-growth figure, none was gathered, and I did not guess one. Moot while the gate fails. SBC/FCF 28.3% is well under the 100% disqualifier.

Note: the script's market cap here uses ~$585 (prior close); live is $570.64. Only Phase 02 inputs are affected, and they are not used.

## 4. Phase 01 — Quality Score (script output, verbatim)
Inputs: fundamentals above; TAM evidence = AMD Q3 FY2026 press release 2026-11-03 (Data Center $8,546M +97% YoY; Q4 guide ~$17B); Moat = Mercury Research Q2 2026 (x86 share 34.1%) as the one TRUE signal, same as 11-06. No new moat evidence found (no new data since).

```
## Quality Score

Profitability (25%)
NetMargin_Component = clamp((16.769/30)x100) = 55.90
ROIC_Component = clamp((11.886/30)x100) = 39.62
Profitability_Score = (55.90 + 39.62) / 2 = 47.76
Margins (15%)
GrossMargin_Score = clamp((53.715/80)x100) = 67.14
Growth (20%)
Growth_Score = clamp((13.644/25)x100) = 54.58
+10 TAM/pricing-power evidence (AMD Q3 FY2026 release 2026-11-03)
Growth_Score (final, clamped) = 64.58
Balance Sheet (15%)
BalanceSheet_Score = clamp(100x(1 - -0.152/4)) = 100.00
Moat Signal (15%)
market_share_stable_or_growing True (Mercury Research Q2 2026); other four False
Moat_Score = (1/5) x 100 = 20.00
FCF Quality (10%)
FCFQuality_Score = clamp(((0.6637 - 0.40)/0.60)x100) = 43.96  [ratio = (FCF - SBC)/NI]
Quality Score — Final
Quality Score = (47.76x0.25) + (67.14x0.15) + (64.58x0.20) + (100.00x0.15) + (20.00x0.15) + (43.96x0.10)
= 57.322 -> rounds to 57.3

# Quality Score = 57.3 — FAILS the 80.0+ gate
```
No hard disqualifier fires. Sensitivity (from 11-06): crediting all five moat signals adds 12.0 pts → ~69.3, still below 80.

## 5. Recommendation
**PASS — do not open a position, no limit order.** The +34.6% rally does not change a Quality Score built from ROIC, moat evidence and cash conversion. No Rate Gate, valuation score, Composite, fair value or order setup computed (strict gate).

## 6. Next review trigger
Unchanged from the watchlist entry: Q4 FY2026 earnings (~Feb 2027), realized AI-accelerator share evidence, sustained like-for-like ROIC improvement, management change/M&A. Add: verify the cause of the −36% then +35% price swings if it points to a fundamental event.

## Glossary
- **Quality Score** — This framework's 0.0–100.0 continuous score grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality). A company must score 80.0+ to proceed to Phase 02 valuation scoring. See [quality-scoring.md](../framework/quality-scoring.md).
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself.
- **SBC (Stock-Based Compensation)** — Employee pay in shares/options rather than cash; a real cost to shareholders through dilution, deducted from FCF in this framework's FCF yield and FCF Quality.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether accounting profit turns into real cash.
- **Hard disqualifier** — A Quality Score condition that fails a company regardless of its weighted total.
- **Moat** — Durable competitive advantage that protects profits from competitors.
- **Mercury Research** — Independent firm publishing quarterly x86 CPU market-share estimates; third-party citation for the market-share moat signal.
- **Data Center segment (AMD)** — AMD's EPYC server CPU and Instinct AI GPU segment (Q3 FY2026 revenue $8,546M, +97% YoY).
- **Net Debt/EBITDA** — Leverage ratio; negative means net cash.
- **Forward PE / EV/EBIT** — Price or enterprise value relative to expected earnings / operating profit; Phase 02 inputs, not used here.
- **Rule 0 / Rule 9** — Always fetch a live price first; fundamental events (incl. a >15% unexplained move) force a re-valuation.

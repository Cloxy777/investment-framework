# New Position Evaluation — TTMI (TTM Technologies)

**Task type:** NEW POSITION (first evaluation; no prior session or watchlist entry)
**Date:** 2026-10-29
**Trigger:** Manual `/new-position TTMI`.
**10Y US Treasury yield:** 4.99% (FRED `DGS10`, 2026-10-27). Header only: the Rate Gate is not reached because Phase 01 fails.

## 1. Live price (Rule 0)

IBKR snapshot, contract 10311716 (NASDAQ): last **$89.58**, bid 89.46 / ask 89.77, status `REALTIME`. 52-week range $55.44 – $223.83; 13-week high $149.94, 13-week low $71.71. The price is about 60% below the 52-week high. No cause for the drop was identified in this session, and price movement is not an input to any framework decision.

## 2. Tooling fix needed first

`python -m scripts.fetch_fundamentals TTMI` initially stopped with `ERROR: TTM EBIT: NaN found in trailing 4 quarters of 'EBIT'`. Cause: yfinance emits a column for the quarter ending 2026-09-30 (ended, not yet reported). That column carries only stray per-share lines (Diluted EPS 0.79, share counts) while revenue, EBIT, net income and cash-flow lines are NaN, so the "latest 4 quarters" window included it. No data was estimated.

Patch (this PR): `_drop_unreported_quarters` in [fetch_fundamentals.py](../scripts/fetch_fundamentals.py) drops only the *leading* (newest) quarter columns whose anchor row (`Total Revenue` for income statement, `Free Cash Flow` for cash flow) is NaN. A gap in the middle of history still raises, and a genuinely missing line item still raises (existing test kept). New test `test_unreported_all_nan_quarter_column_is_ignored`; full suite 185 passed.

## 3. Fundamentals

`python -m scripts.fetch_fundamentals TTMI` output (after patch; window = Q3'25–Q2'26 reported quarters):

```
Market Cap            = 9,439,539,200
Enterprise Value      = 10,360,850,432
Shares Outstanding    = 105,375,520
Forward PE            = 10.746
FCF Yield %           = -0.160
EV/EBIT               = 33.698
Net Margin %          = 7.011
Gross Margin %        = 21.191
ROIC % (NOPAT/InvCap) = 10.311  [tax_rate=0.1017, NOPAT=276,182,556, InvestedCapital=2,678,404,000]
Revenue 3yr CAGR %    = 5.218
Net Debt/EBITDA       = 0.710  [EBITDA_ttm=584,139,008]
FCF/NI TTM % (plain)  = -6.394
(FCF - SBC)/NI TTM %  = -32.301  [reported NI]
SBC yield %           = 0.650
Gross buyback yield % = 0.000
FCF/NI annual (oldest first) = [179.7%, -144.5%, 90.9%, -0.4%]
FCF positive 3yr+     = False
5yr PE avg/low/high   = 18.112 / 6.805 / 58.600  (n=20 quarters)

SBC block (TTM, advisory - no score effect)
  SBC 61,341,000.0   FCF -15,139,000.0   Market cap 9,439,539,200.0
  SBC/FCF = n/a - FCF <= 0  -> SEVERE: SBC consumes all (or more than all) of FCF
  FCF yield (reported)  = -0.16%
  FCF yield after SBC   = -0.81%
Advisory flags (no score effect)
  cycle_peak             UNKNOWN   EPS TTM now or 1y ago unavailable
  value_trap_candidate   UNKNOWN   forward PE or trailing EPS growth unavailable
```

Advisory flags: `cycle_peak` and `value_trap_candidate` are `UNKNOWN` (data gap: yfinance lacks 8 consecutive quarters of Diluted EPS). Not resolved, because Phase 01 fails and no valuation is run. `MULTIPLE_CEILING` not run for the same reason.

Supporting yfinance figures (annual FCF, FY2022–FY2025): +$170.0M, +$27.0M, +$51.2M, **−$0.7M**. FY2025 operating cash flow $291.9M less capex $292.6M. Last four reported quarters of FCF: +$42.4M, −$6.5M, −$85.1M, +$34.1M (sum −$15.1M). Capex has risen every year ($102.9M FY2022 → $292.6M FY2025).

## 4. Phase 01 — Quality Score

Inputs built from the output above. Moat, TAM and margin-trend fields were **not researched** and are entered as `false` with that stated in the evidence text. They cannot change the result: hard disqualifiers are applied before the weighted calculation. `python -m scripts.scoring.quality_score --input ttmi_q.json`, verbatim:

```
# FAILS GATE
Reason: SBC 61,341,000 is >= 100% of TTM FCF -15,139,000 (or FCF <= 0) with no documented one-off explanation
```

A second hard disqualifier also applies on the same data: not FCF-positive for 3+ consecutive years (FY2025 FCF −$0.7M; `fcf_positive_3yr_or_more` = False). The script reports only the first one it hits.

Not triggered: FCF/NI <70% for 2+ *consecutive* years (annual ratios 179.7%, −144.5%, 90.9%, −0.4% — the two sub-70% years are not adjacent); Net debt/EBITDA 0.71× is under 2.5×.

No SBC one-off is documented, so the SBC disqualifier has no carve-out here. The FCF-positivity disqualifier has none either. The weighted Quality Score was not computed.

**Result: Phase 01 FAIL. Stopped per the command.** No Rate Gate, valuation score, Composite Score or order setup.

## 5. Recommendation

**PASS.** The profile is not poor on every line: leverage is low (0.71×), ROIC is 10.3%, forward PE 10.7 against a 5-year average of 18.1. But it is a capex-heavy ramp: FCF has been roughly zero for a year while SBC runs at $61.3M, and net margin (7.0%) and gross margin (21.2%) are thin. The framework does not let a cheap multiple override a cash-flow-quality failure.

## 6. Portfolio

Not a holding. No position opened, no `decisions/` entry.

## 7. Next review trigger

- Q3 FY2026 results (period ending 2026-09-30), expected early November 2026 — Rule 9 re-check (earnings).
- Mechanically, the FCF-positivity disqualifier clears on a window of fiscal years once FY2026 reports a positive FCF and the 3-year rolling window is all positive (FY2026 earliest, ~Feb/Mar 2027). The SBC disqualifier clears as soon as TTM FCF exceeds TTM SBC.
- Before any future scoring, source moat/TAM evidence from primary filings.

## Glossary

| Term | Meaning |
|---|---|
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **SBC (Stock-Based Compensation)** | Employee pay in the form of company shares or stock options rather than cash. A non-cash expense added back in cash-flow statements (inflating FCF relative to GAAP net income), but a real economic cost to existing shareholders through ongoing dilution — worth tracking alongside FCF/NI conversion and share-count trend, not just the headline FCF figure. Since the 2026-10-12 methodology it is treated as a cost in both the FCF yield (Valuation) and FCF Quality (Quality). |
| **Hard disqualifier** | One of three Quality Score conditions ([quality-scoring.md](quality-scoring.md)) that fails a company regardless of its weighted sub-score total: not FCF-positive for 3+ consecutive years, Net Debt/EBITDA over its applicable threshold, or an FCF/Net Income conversion ratio under 70% for 2+ consecutive years without a documented growth-capex explanation. A weighted average can't average away an outright balance-sheet or cash-flow-quality failure. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate. |
| **Quality Score** | This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality) instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. See [quality-scoring.md](quality-scoring.md). |
| **Forward PE** | Price ÷ next twelve months' *expected* earnings per share (vs. Trailing PE, which uses the last twelve months' actual earnings). |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |

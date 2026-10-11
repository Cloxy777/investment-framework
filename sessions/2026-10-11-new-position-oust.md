# New Position Evaluation — OUST (Ouster, Inc.)

**Task type:** NEW POSITION (re-evaluation; first run was [2026-07-01](2026-07-01-new-position-oust.md), result PASS)
**Date:** 2026-10-11
**Trigger:** Manual `/new-position oust`. Rule 9 re-check: Q1 and Q2 FY2026 results have been reported since the last run, and the price has moved from $61.09 to $39.85.
**10Y US Treasury yield:** 5.22% (FRED `DGS10`, 2026-10-08). Shown for the header only. The Rate Gate is not reached because Phase 01 fails.

## 1. Live price (Rule 0)

IBKR snapshot, contract 625287738 (NASDAQ): last **$39.85**, prior close $39.53 (+0.81%). Status `FROZEN` (the market is closed, today is a Sunday). 52-week range $16.40 – $63.79. The price is −37.5% from the 52-week high and −34.8% from the 2026-07-01 price of $61.09. No cause for the drop has been identified in this session.

## 2. Fundamentals

`python -m scripts.fetch_fundamentals OUST` stopped with:

```
ERROR: TTM Pretax Income is <= 0 — effective tax rate for ROIC/NOPAT is undefined
```

This is the script's intended stop for a loss-making company. Its output is not available, so the inputs below were pulled directly from yfinance (quarterly and annual statements, as of the 2026-06-30 balance sheet) and hand-computed. Every figure is shown.

| Metric | Calculation | Result |
|---|---|---|
| TTM revenue (Q3'25–Q2'26) | 39.525 + 62.178 + 48.578 + 54.626 | $204.907M |
| TTM net income | −21.733 + 3.985 − 17.465 − 18.114 | −$53.327M |
| **Net margin** | −53.327 / 204.907 | **−26.02%** (July: −35.65%) |
| TTM EBIT | −21.661 + 4.399 − 19.212 − 20.045 | −$56.519M |
| Invested capital (6/30/26) | Debt 16.397 + Equity 371.308 − Cash & ST investments 261.081 | $126.624M |
| **ROIC** | NOPAT (EBIT, no tax shield assumed, same convention as July) / invested capital = −56.519 / 126.624 | **−44.63%** |
| TTM gross profit | 16.659 + 37.452 + 20.838 + 26.685 = 101.634 | **Gross margin 49.60%** (July: 49.27%) |
| 3yr revenue CAGR FY2022→FY2025 | (169.384 / 41.029)^(1/3) − 1 | **+60.41%** |
| TTM FCF | −15.406 − 9.842 − 37.176 − 20.044 | **−$82.468M** |

Annual FCF (yfinance): FY2022 −$116.112M, FY2023 −$140.896M, FY2024 −$37.450M, FY2025 −$64.849M. The July session found FY2019–FY2021 also negative from SEC EDGAR data, and I did not re-check those. Quarterly FCF was negative in each of the last five quarters.

Quarterly pattern: Q4'25 showed a one-off positive net income of $3.985M, with EBIT of $4.399M. The two quarters since are back to losses (Q1'26 −$17.465M, Q2'26 −$18.114M).

Balance sheet: total debt $16.4M against cash and short-term investments of $261.1M, so OUST is in a net-cash position. EBITDA is negative, so Net Debt/EBITDA is entered as 0.0 on the same judgment call as July (no meaningful financial debt to service).

## 3. Phase 01 — Quality Score

Inputs file built from the figures above. Moat signals are all `false`, carried over from the July session's reading of the FY2025 10-K (no third-party share data; ASP declines disclosed; larger, lower-cost rivals Hesai and RoboSense). I did not re-read the Q2 10-Q, so the Moat evidence is not refreshed. FCF/NI: TTM 154.6% (−82.468 / −53.327); annual FY2022–FY2025 83.8%, 37.7%, 38.6%, 107.4% (both numerator and denominator negative every year, so the ratio carries no meaning here).

Script output, verbatim (`python -m scripts.scoring.quality_score --input oust_q.json`):

```
# FAILS GATE
Reason: Not FCF-positive for 3+ consecutive years
```

The script exits at the hard-disqualifier check and does not print sub-scores. The FCF-positivity disqualifier has no carve-out in [quality-scoring.md](../framework/quality-scoring.md). Result: **Phase 01 FAIL**.

For context only, the July hand calculation gave Quality Score 44.2. With net margin now −26.02% (still clamped to 0.0 in Profitability) and ROIC −44.6% (also 0.0), the Profitability sub-score stays at 0.0, and the Moat and FCF Quality sub-scores stay at 0.0 on the same inputs. The weighted score would be roughly unchanged, well below 80.0. I did not compute it formally because the script stops at the disqualifier.

## 4. Recommendation

**PASS.** Per the command, no Rate Gate, valuation score, Composite Score, or order setup is run. Nothing has changed that clears the gate:

- OUST has not had a positive-FCF year in any fiscal year on record. The trailing-twelve-month cash burn ($82.5M) is larger than FY2024's ($37.5M) and FY2025's ($64.8M).
- The business is improving at the margin (net margin −35.7% → −26.0%, gross margin ~49.6%, revenue still growing fast) and holds $261M of cash, so the near-term funding risk looks low. That is a reason to keep watching, not a reason to enter.
- The 37.5% drop from the 52-week high is not an input. The framework acts on documented triggers, not price movement.

## 5. Portfolio

Not a holding. No position opened, nothing to rebalance. No `decisions/` entry.

## 6. Next review trigger

- Q3 FY2026 Form 10-Q (period ending 2026-09-30), expected ~early November 2026.
- Mechanically, the disqualifier clears only with a positive full fiscal-year FCF print (FY2026 earliest, reported ~Feb/Mar 2027). TTM FCF is currently going the wrong way.
- Also: a documented, primary-sourced Moat signal, guidance revision, management change, material M&A, or a >15% price move with an identified cause.

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate between a start and end value. |
| **FCF** | Free Cash Flow — cash left after running and maintaining the business. |
| **Gross Margin** | Gross Profit ÷ Revenue — what's left of each revenue dollar after direct production costs. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of its weighted score; the FCF-positivity check has no carve-out. |
| **Invested Capital** | Debt + equity − cash: the capital put to work in the business, the denominator of ROIC. |
| **Lidar** | "Light Detection and Ranging" — a laser-based distance sensor used in robotics and self-driving vehicles; Ouster makes them. |
| **Moat** | A durable competitive advantage that protects a business's profits. |
| **Net Margin** | Net Income ÷ Revenue — accounting profit per revenue dollar. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − tax rate), the numerator of ROIC. |
| **Quality Score** | This framework's 0.0–100.0 Phase 01 score; 80.0+ is required to proceed to valuation scoring. |
| **ROIC** | Return on Invested Capital — profit generated per dollar of capital invested. |
| **Rule 0** | Always fetch a live price first; never infer it. |
| **Rule 9** | The list of fundamental events (earnings, guidance, management change, M&A, >15% unexplained price move) that force a re-check. |
| **TTM** | Trailing Twelve Months — the latest four reported quarters combined. |

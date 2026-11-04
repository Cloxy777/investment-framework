# NEW POSITION — SRRK (Scholar Rock Holding Corp) — 2026-11-04

**Task type:** NEW POSITION (manual `/new-position SRRK`)
**Result:** **Phase 01 FAIL — PASS, do not open a position.** Two hard disqualifiers fire (FCF negative 4 straight years; SBC > 0 with FCF ≤ 0). Phase 02, Composite and order setup not computed (gate fails first).
**Portfolio weight:** 0% — not held. No prior watchlist/session coverage.

## 1. Live price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Last** | **$46.13** | IBKR `get_price_snapshot`, contract 319099332 (NASDAQ) |
| Bid / Ask | $43.00 / $47.68 | same call (wide, thin quote) |
| Cross-check | $46.09 | `yfinance` `fast_info.lastPrice` |

Market cap (yfinance) ≈ $5.61B.

## 2. Data sourcing

```
$ python -m scripts.fetch_fundamentals SRRK
ERROR: yfinance field missing from TTM Gross Profit: row 'Gross Profit' not found
```

Cause: Scholar Rock is pre-revenue (Total Revenue = 0 every quarter since 2023), so no gross profit row exists. Gross margin, net margin and revenue CAGR are undefined, not missing. Nothing estimated; the figures below are read directly from `yfinance` statements (a manual stand-in for the script's inputs).

| Item ($M) | FY2022 | FY2023 | FY2024 | FY2025 | TTM (Q3'25–Q2'26) |
|---|---|---|---|---|---|
| Revenue | 33.2 | 0 | 0 | 0 | 0 |
| Net income | −134.5 | −165.8 | −246.3 | −377.9 | **−408.6** |
| Free cash flow | −133.8 | −145.3 | −201.0 | −300.6 | **−297.0** (−69.0 −75.5 −82.2 −70.3) |
| SBC | 27.7 | 27.1 | 36.6 | 75.6 | **75.7** (18.3 +19.4 +18.2 +19.7) |
| EBITDA | −131.4 | −168.5 | −237.5 | −369.4 | −396.4 |

Balance sheet (FY2025): cash $323.5M, debt $108.9M. Latest `yfinance` summary: cash $492.1M, debt $203.8M (net cash ~$288M) — net debt/EBITDA is negative (net cash) so passes, but EBITDA is negative so the ratio is not meaningful.

Advisory flags (SBC/FCF, cycle_peak, value_trap, multiple_ceiling): not run — need EPS/PE/FCF-yield on positive earnings; none exist. Recorded as data gaps, no score effect.

## 3. Phase 01 — Quality Score

Per [quality-scoring.md](../framework/quality-scoring.md), hard disqualifiers apply before the weighted score:

| Disqualifier | Test | Result |
|---|---|---|
| Not FCF-positive for 3+ consecutive years | FCF FY2023 −145.3, FY2024 −201.0, FY2025 −300.6, TTM −297.0 | **FIRES** |
| SBC ≥ 100% of TTM FCF (or FCF ≤ 0 with SBC > 0) | TTM FCF −$297.0M, SBC $75.7M | **FIRES** (no one-off documented; SBC rising 4 years) |
| FCF/NI <70% 2+ yrs | FCF/NI ≈ 72.7% TTM (−297.0 / −408.6); ratio of two negatives, not meaningful | not relied on |
| Net debt/EBITDA > 2.5× | net cash; EBITDA negative | not meaningful |

**Weighted score not computed.** `quality_score.py` needs gross margin and a 3-yr revenue CAGR; with zero revenue both are undefined and I will not invent a value. The gate is failed on the disqualifiers alone (the script's `FAILS GATE` path runs before the weighted math). Net margin and ROIC are deeply negative, so the weighted score would be near-floor on Profitability/Margins/Growth in any case; no input choice could reach 80.0.

## 4. Recommendation

**PASS — do not open a position.** Phase 02 / Composite / order setup skipped. The cheapness or catalyst story (apitegromab SMA data/approval) is irrelevant: this framework does not underwrite binary clinical outcomes. Revisit only if SRRK achieves sustained positive FCF (3+ fiscal years).

**Next review trigger:** FY2026 10-K (Feb–Mar 2027) for Rule 9 re-check; not expected to clear within 3 years.

## Glossary

From [framework/glossary.md](../framework/glossary.md): **Clinical-stage biotech** (new), **Pre-revenue (company)**, **Hard disqualifier**, **Quality Score**, **SBC (Stock-Based Compensation)**, **Net Debt/EBITDA**, **Phase 01 (Universe Screening / quality gate)**, **Rule 0**.

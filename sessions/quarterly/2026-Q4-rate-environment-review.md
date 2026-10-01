# Quarterly Rate Environment Gate Review — 2026 Q4

- **Date:** 2026-10-01 (first weekday of October)
- **Task type:** Quarterly Rate Environment Gate Review (Routine)

## 1. Current 10Y US Treasury yield

Source: FRED `DGS10` — https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10

Most recent non-blank value: **5.26%** on **2026-09-29** (2026-09-30 and 2026-10-01 not yet posted at time of fetch).

## 2. Band determination

Per [framework/strategy.md](../../framework/strategy.md) "Rate Environment Gate — Step 2 — Rate Regime Modifier":

| 10Y Treasury Yield | Modifier |
|---|---|
| < 2% | −10 |
| 2–3.5% | 0 |
| 3.5–5% | +5 |
| > 5% | +10 |

5.26% falls in the **>5%** band → **Rate Regime Modifier = +10**.

## 3. Most recent RESCORE/rebalance session's active modifier

Most recent RESCORE session: [sessions/2026-09-28-rescore-avgo.md](../2026-09-28-rescore-avgo.md) — Step 2 Rate Regime Modifier **+10** (10Y 5.21%, >5% bracket, unchanged from 2026-09-15). (The 2026-09-27 rebalance session does not record a modifier value.)

## 4. Comparison and outcome

**No change.** Band this quarter (+10) matches the value in active use (+10). No GitHub issue or decision-log PR required.

Context: the 10Y has risen from 4.38% (Q3 review) to 5.26%, so it sits only ~26 bp above the 5% boundary; a fall back under 5% would revert the modifier to +5.

## 5. January annual tasks

Not applicable — current month is October, not January.

## Glossary

- **10Y Treasury yield**: Annual interest rate on 10-year US government bonds; the benchmark "risk-free" rate used by the Rate Environment Gate.
- **Rate Regime Modifier**: Additive score adjustment (−10 to +10) based on which band the 10Y yield falls in.
- **Rate Environment Gate**: The mandatory pre-score check comparing stock earnings yield against the 10Y yield.
- **FRED**: Federal Reserve Economic Data, the public source of the yield series.
- **bp (basis point)**: 0.01 percentage point.
- **RESCORE**: Quarterly post-earnings re-computation of a holding's scores.

# Quarterly Rate Environment Gate Review — 2026 Q3

- **Date:** 2026-07-01 (first weekday of July)
- **Task type:** Quarterly Rate Environment Gate Review (Routine)

## 1. Current 10Y US Treasury yield

Source: FRED `DGS10` — https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10

Most recent non-blank value: **4.38%** on **2026-06-29** (2026-06-30 and 2026-07-01 not yet posted at time of fetch).

## 2. Band determination

Per [framework/strategy.md](../../framework/strategy.md) "Rate Environment Gate — Step 2 — Rate Regime Modifier":

| 10Y Treasury Yield | Modifier |
|---|---|
| < 2% | −10 |
| 2–3.5% | 0 |
| 3.5–5% | +5 |
| > 5% | +10 |

4.38% falls in the **3.5–5%** band → **Rate Regime Modifier = +5**.

## 3. Most recent RESCORE/rebalance session's active modifier

Most recent RESCORE session: [sessions/2026-07-01-rescore-nke.md](../2026-07-01-rescore-nke.md).

That session recorded: **Rate Regime Modifier in effect: +5** (10Y 4.38%, same 2026-06-29 print — 2026-06-30/07-01 not yet posted at that session's fetch time either).

## 4. Comparison and outcome

**No change.** Step 2 band this quarter (+5) matches the value already in active use in the most recent RESCORE session (+5). Both derive from the same underlying 10Y print (4.38%, 2026-06-29), since no newer daily value had posted at either fetch time.

No GitHub issue or PR required — the Rate Regime Modifier has not shifted bands since the last RESCORE.

## 5. January annual tasks

Not applicable — current month is July, not January.

## 6. Summary

| Item | Value |
|---|---|
| 10Y Treasury yield | 4.38% (2026-06-29) |
| Band | 3.5–5% |
| Rate Regime Modifier | +5 |
| Prior modifier (last RESCORE) | +5 |
| Changed? | No |
| Action taken | None — modifier unchanged, no issue/PR opened |

## Glossary

- **10Y (10-Year Treasury yield):** see **Treasury yield (10Y)** below.
- **Treasury yield (10Y):** The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate.
- **Rate Environment Gate:** The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier.
- **Rate Regime Modifier:** An additive adjustment (−10 to +10) applied to the valuation score based on which Treasury-yield bracket the market is currently in.
- **FRED:** Federal Reserve Economic Data — the St. Louis Fed's public database of economic time series, including the `DGS10` (10-Year Treasury) series used here.
- **RESCORE:** The framework's task type for a quarterly (or trigger-driven) post-earnings re-score of an existing holding.

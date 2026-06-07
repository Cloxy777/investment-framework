# Freedom Finance Portfolio Snapshot

**Account:** Freedom24
**Last synced:** 2026-06-07 (from two user-provided screenshots of the Freedom24 app — Portfolio → Opened Positions view, and Portfolio → top-level Net Asset Valuation/Cash view)

**Summary:** Net Asset Valuation: $15,123.54 · Opened Positions Value: $15,016.69 · Cash: $106.85 · Period Return: -$416.55 (-2.70%) · Securities in USD: -$416.55 (-2.70%)

> **Note:** $15,016.69 (Opened Positions) + $106.85 (Cash) = $15,123.54 (Net Asset Valuation) — ties out exactly, confirming both screenshots are reading the same account at the same moment and nothing is double-counted or missing.

| Ticker | Company | Qty | Avg Price | Current Value | Return % | Product Type | Currency |
|--------|---------|-----|-----------|---------------|----------|--------------|----------|
| MSFT | Microsoft Corp | 2 | 413.12 | 825.00 | -0.15% | Stock | USD |
| META | Meta Platforms Inc | 1 | 620.21 | 589.65 | -4.93% | Stock | USD |
| DUOL | Duolingo Inc | 8 | 155.76 | 863.44 | -30.71% | Stock | USD |
| AMZN | Amazon.com Inc | 11 | 228.97 | 2,702.70 | +7.31% | Stock | USD |
| TLT | iShares 20+ Year Treasury Bond ETF | 118 | 86.63 | 10,035.90 | -1.82% | ETF | USD |

> **Note:** the 5 positions shown sum exactly to the reported total opened-positions value ($15,016.69), confirming this is the complete position list — no scrolling/truncation. Current prices read from the screenshot (MSFT 412.50, META 589.65, DUOL 107.93, AMZN 245.70, TLT 85.05) cross-check against `qty × price = current value` for every row.

## Cash Balance

| Currency | Cash Balance |
|----------|--------------|
| USD | 106.85 |
| **Total** | **106.85** |

Source: second screenshot, Portfolio top-level view ("Net asset valuation $15,123.54" → "Cash" card → "USD 106.85"). Single-currency (USD), so no FX conversion needed. This is now folded into `holdings.md` as the `CASH (Freedom24)` row, and the broker's total account value used for weighting is the **Net Asset Valuation ($15,123.54)** — positions + cash — matching how the IBKR side uses Net Liquidation Value.

*This file is overwritten on every Freedom Finance sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

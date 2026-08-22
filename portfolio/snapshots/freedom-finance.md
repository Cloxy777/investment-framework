# Freedom Finance Portfolio Snapshot

**Account:** Freedom24
**Last synced:** 2026-08-22 (from one user-provided screenshot of the Freedom24 app, Portfolio tab — combined Cash card + Opened Positions view, no separate top-level Net Asset Valuation screenshot provided this round)

**Summary:** Cash: $44.98 · Opened Positions Value: $10,844.98 · Implied total (cash + positions, not broker-labeled "Net Asset Valuation" this round): **$10,889.96**

| Ticker | Company | Qty | Avg Price | Current Value | Return % | Product Type | Currency |
|--------|---------|-----|-----------|---------------|----------|--------------|----------|
| DUOL | Duolingo Inc | 8 | 155.76 | 1,165.44 | -6.47% | Stock | USD |
| TLT | iShares 20+ Year Treasury Bond ETF | 118 | 86.63 | 9,679.54 | -5.31% | Stock/ETF | USD |

> **Note:** the 2 positions shown sum exactly to the reported total opened-positions value ($1,165.44 + $9,679.54 = $10,844.98), and each row's `qty × current price` cross-checks against the per-share prices visible in the screenshot (DUOL $145.68/sh, TLT $82.03/sh) — internally consistent, and the screenshot's footer ("Service is provided by Freedom24") was visible below the TLT row, indicating this is the full list, not a scrolled/truncated view.

## MSFT, META, AMZN confirmed sold out of Freedom24 — user-confirmed 2026-08-22

The **2026-06-07 snapshot** (last full sync) showed **5 positions**: MSFT (2 sh, $825.00), META (1 sh, $589.65), DUOL (8 sh, $863.44), AMZN (11 sh, $2,702.70), TLT (118 sh, $10,035.90), totaling $15,016.69 in opened positions + $106.85 cash = $15,123.54 NAV.

This sync's screenshot shows only DUOL and TLT ($10,844.98 total, ties out exactly to those two). **User confirmed directly (2026-08-22): MSFT, META, and AMZN were sold** — the screenshot is complete, not truncated. No fill dates, prices, or realized P&L are available (Freedom24 has no trade-history API, only screenshots) — **not on record anywhere** as an authorized trade; no `sessions/`, `decisions/`, or prior `override-log.md` entry covers it. Logged to [override-log.md](../override-log.md).

**Cash still doesn't reconcile:** cash *fell* $106.85 → $44.98 despite what should have been a ~$4,000+ proceeds event. Not explained by this data — possible withdrawal, or the sale happened before the last cash figure and proceeds were since moved out. Flagged, not resolved.

**MSFT/META/AMZN are now IBKR-only holdings** — `holdings.md` updated accordingly.

## Cash Balance

| Currency | Cash Balance |
|----------|--------------|
| USD | 44.98 |
| **Total** | **44.98** |

Source: same screenshot, "Cash" card at the top of the Portfolio tab. Single-currency (USD), so no FX conversion needed. No separate "Net Asset Valuation" top-level figure was visible in this screenshot (unlike the two-screenshot flow used in the 2026-06-07 sync) — the $10,889.96 implied total above is cash + opened positions computed here, not a broker-labeled figure.

*This file is overwritten on every Freedom Finance sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

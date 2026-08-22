# Freedom Finance Portfolio Snapshot

**Account:** Freedom24
**Last synced:** 2026-08-22 (from one user-provided screenshot of the Freedom24 app, Portfolio tab — combined Cash card + Opened Positions view, no separate top-level Net Asset Valuation screenshot provided this round)

**Summary:** Cash: $44.98 · Opened Positions Value: $10,844.98 · Implied total (cash + positions, not broker-labeled "Net Asset Valuation" this round): **$10,889.96**

| Ticker | Company | Qty | Avg Price | Current Value | Return % | Product Type | Currency |
|--------|---------|-----|-----------|---------------|----------|--------------|----------|
| DUOL | Duolingo Inc | 8 | 155.76 | 1,165.44 | -6.47% | Stock | USD |
| TLT | iShares 20+ Year Treasury Bond ETF | 118 | 86.63 | 9,679.54 | -5.31% | Stock/ETF | USD |

> **Note:** the 2 positions shown sum exactly to the reported total opened-positions value ($1,165.44 + $9,679.54 = $10,844.98), and each row's `qty × current price` cross-checks against the per-share prices visible in the screenshot (DUOL $145.68/sh, TLT $82.03/sh) — internally consistent, and the screenshot's footer ("Service is provided by Freedom24") was visible below the TLT row, indicating this is the full list, not a scrolled/truncated view.

## ⚠️ MSFT, META, and AMZN are absent from this sync — unconfirmed whether sold or a screenshot gap

The **2026-06-07 snapshot** (last full sync) showed **5 positions**: MSFT (2 sh, $825.00), META (1 sh, $589.65), DUOL (8 sh, $863.44), AMZN (11 sh, $2,702.70), TLT (118 sh, $10,035.90), totaling $15,016.69 in opened positions + $106.85 cash = $15,123.54 NAV.

This sync's screenshot shows **only DUOL and TLT** — MSFT, META, and AMZN are nowhere in the list, and the positions total ($10,844.98) ties out exactly to just those two, with no room for the other three. The value gap ($15,016.69 → $10,844.98 = **-$4,171.71**) is in the same ballpark as the three missing tickers' last-known combined value (**$4,117.35**), which is *consistent with* those three having been sold — but this account has no API/trade-history access, only screenshots, so **that cannot be confirmed from this data alone**. Cash also dropped ($106.85 → $44.98), which cuts against a simple "sold and cash is sitting there" story (proceeds from a $4,171-ish sale would be expected to show up as cash, not a cash *decrease*) — worth asking about directly.

**Not treated as a confirmed exit.** MSFT, META, and AMZN weights in `holdings.md` this sync use the **IBKR-only** portion of each (Freedom24 leg marked unconfirmed, not zeroed and not carried forward as stale-but-current) — see the flag there. **Action needed: confirm directly in the Freedom24 app (Trades/Orders history tab, if available) whether these three were sold, transferred out, or if this screenshot is incomplete, and re-sync.**

## Cash Balance

| Currency | Cash Balance |
|----------|--------------|
| USD | 44.98 |
| **Total** | **44.98** |

Source: same screenshot, "Cash" card at the top of the Portfolio tab. Single-currency (USD), so no FX conversion needed. No separate "Net Asset Valuation" top-level figure was visible in this screenshot (unlike the two-screenshot flow used in the 2026-06-07 sync) — the $10,889.96 implied total above is cash + opened positions computed here, not a broker-labeled figure.

*This file is overwritten on every Freedom Finance sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

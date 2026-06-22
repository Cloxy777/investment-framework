# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-06-22 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-positions`)
**Cash balances last synced:** 2026-06-22 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-balances`)
**Account summary:** Net Liquidation $40,689.53 (broker-reported, BASE) · Gross Position Value $40,233.26 (sum of positions below, XEON converted at live FX) · Total Cash (USD-equiv) $255.99 · Unrealized P&L –$1,497.85 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 23 positions resolved directly from the MCP's `contract_description` field. 22 are already clean ticker symbols (e.g. `AMZN`, `DUOL`, `VEEV`, `ADBE`, `AVGO`); `XEON @IBIS2` is normalized to `XEON` (exchange suffix stripped) for consistency with `holdings.md`. No `CONID_XXXXXXX` placeholders were needed, so the live/fallback ticker-lookup CSV fetch was not required for this sync.

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 10 | 195.12 | 1,951.20 | 202.07 | -69.50 | -3.44% | USD | 265768 |
| AMZN | 12 | 241.23 | 2,894.76 | 210.59 | +367.70 | +14.55% | USD | 3691937 |
| AVGO | 6 | 404.53 | 2,427.18 | 382.44 | +132.53 | +5.78% | USD | 313130367 |
| CSGP | 25 | 30.02 | 750.50 | 35.04 | -125.50 | -14.33% | USD | 6726677 |
| DUOL | 30 | 124.88 | 3,746.40 | 168.25 | -1,301.04 | -25.78% | USD | 505002183 |
| GOOG | 1 | 361.39 | 361.39 | 295.70 | +65.69 | +22.22% | USD | 208813720 |
| META | 6 | 573.20 | 3,439.20 | 597.81 | -147.63 | -4.12% | USD | 107113386 |
| MSFT | 20 | 377.53 | 7,550.60 | 402.62 | -501.87 | -6.23% | USD | 272093 |
| NFLX | 12 | 77.00 | 924.00 | 87.79 | -129.49 | -12.29% | USD | 15124833 |
| NKE | 20 | 45.01 | 900.20 | 43.31 | +34.00 | +3.92% | USD | 10291 |
| NOW | 12 | 94.00 | 1,128.00 | 92.80 | +14.41 | +1.29% | USD | 109911821 |
| NVDA | 14 | 208.61 | 2,920.54 | 179.20 | +411.68 | +16.41% | USD | 4815747 |
| NVO | 5 | 44.23 | 221.15 | 42.54 | +8.45 | +3.97% | USD | 10611 |
| RBRK | 3 | 70.00 | 210.00 | 58.10 | +35.71 | +20.49% | USD | 699030013 |
| SPGI | 1 | 412.76 | 412.76 | 411.00 | +1.76 | +0.43% | USD | 229629397 |
| SPOT | 1 | 468.08 | 468.08 | 509.00 | -40.92 | -8.04% | USD | 312496724 |
| STIM | 345 | 1.23 | 424.35 | 1.75 | -178.95 | -29.66% | USD | 324062325 |
| TLT | 77 | 86.53 | 6,662.81 | 88.79 | -173.82 | -2.54% | USD | 15547841 |
| UBER | 3 | 71.32 | 213.96 | 82.02 | -32.11 | -13.05% | USD | 365207014 |
| V | 1 | 327.24 | 327.24 | 319.51 | +7.73 | +2.42% | USD | 49462172 |
| VEEV | 3 | 153.50 | 460.50 | 164.83 | -34.00 | -6.88% | USD | 136254493 |
| XEON | 10 | 149.43 | 1,494.33 | 149.03 | +4.08 | +0.27% | EUR | 46041702 |
| ZS | 1 | 124.25 | 124.25 | 157.16 | -32.91 | -20.93% | USD | 310621426 |

> ⚠️ **New position since the last sync (2026-06-15) — AVGO (Broadcom Inc.):** 6 shares @ avg cost $382.44. `get_account_trades` confirms the fill: **BUY 6 AVGO @ $382.275 limit, 2026-06-16T14:19:43Z** (order ID 652254142), funded in part by an EUR→USD conversion the same week (2026-06-18). **This is a portfolio override, not a framework-driven buy.** The only AVGO evaluation on record — the [2026-06-14 new-position session](../../sessions/2026-06-14-new-position-avgo.md) — scored AVGO **69.5 (WATCHLIST, "no new entry")**, explicitly recommending against opening a position at that price. The buy happened two days later at essentially the same price ($382.28 vs. the $382.07 evaluated), with no `decisions/` entry documenting why the recommendation was overridden. Per [override-log.md](../override-log.md)'s own rule ("log it here at time of entry"), this sync adds the entry retroactively — see that file. No framework action taken as part of this sync; flagged for the user to supply the missing rationale, confirm intent to hold, and/or request a fresh `/rescore` given the override.
>
> **No other position-size changes since 2026-06-15** — all 22 previously-held tickers show identical share counts; market-value/P&L changes reflect price movement only. ADBE remains a partial fill (10 of the ~17-share target toward the [2026-06-12 new-position](../../sessions/2026-06-12-new-position-adbe.md) BUY recommendation) — still no ADBE order visible in `get_account_orders`, so the remaining ~7 shares have still not been purchased.

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value (sum of live position market values above, $40,233.26) plus Total Cash ($255.99) = $40,489.25, ~$200.28 **below** broker-reported Net Liquidation ($40,689.53) — the opposite direction from the gap flagged in the prior sync. This mirrors the same `get_account_positions` (live/intraday) vs. `get_account_balances` (settled; BASE `stock_market_value` = $40,417.61) timing mismatch noted before; not a calculation error, flagged for transparency. It's why the `holdings.md` weight column sums to slightly *under* 100% this time (previously slightly over).

> **Currency note:** all positions are USD except **XEON** (EUR-denominated, market value €1,494.33). Its USD-equivalent (used for `holdings.md` weighting) is computed using the live EUR→USD rate below — fetched directly from `get_account_balances`, not assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|----------------|
| USD | 250.05 | 250.05 | 1.000000 | 250.05 |
| EUR | 5.18 | 5.18 | 1.147130 | 5.94 |
| **Total (USD-equiv)** | | | | **255.99** |

*The same EUR→USD rate (1.147130) applied to XEON's €1,494.33 market value gives its USD-equivalent: **$1,714.19** — used in `holdings.md` for weighting.*

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

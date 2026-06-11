# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-06-11 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-positions`)
**Cash balances last synced:** 2026-06-11 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-balances`)
**Account summary:** Net Liquidation $38,732.29 (broker-reported, BASE) · Gross Position Value $36,400.39 (sum of positions below, XEON converted at live FX) · Total Cash (USD-equiv) $2,326.77 · Unrealized P&L –$1,230.54 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 21 positions resolved directly from the MCP's `contract_description` field. 20 are already clean ticker symbols (e.g. `AMZN`, `DUOL`, `VEEV`); `XEON @IBIS2` is normalized to `XEON` (exchange suffix stripped) for consistency with `holdings.md`. No `CONID_XXXXXXX` placeholders were needed, so the live/fallback ticker-lookup CSV fetch was not required for this sync.

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| AMZN | 12 | 240.24 | 2,882.89 | 210.59 | +355.83 | +14.08% | USD | 3691937 |
| CSGP | 25 | 34.23 | 855.75 | 35.04 | -20.25 | -2.31% | USD | 6726677 |
| DUOL | 30 | 123.02 | 3,690.60 | 168.25 | -1,356.84 | -26.88% | USD | 505002183 |
| GOOG | 1 | 356.08 | 356.08 | 295.70 | +60.38 | +20.42% | USD | 208813720 |
| META | 6 | 575.60 | 3,453.60 | 597.81 | -133.23 | -3.71% | USD | 107113386 |
| MSFT | 20 | 399.00 | 7,980.00 | 402.62 | -72.47 | -0.90% | USD | 272093 |
| NFLX | 12 | 82.00 | 984.00 | 87.79 | -69.49 | -6.60% | USD | 15124833 |
| NKE | 20 | 44.30 | 886.02 | 43.31 | +19.82 | +2.29% | USD | 10291 |
| NOW | 12 | 105.35 | 1,264.20 | 92.80 | +150.61 | +13.53% | USD | 109911821 |
| NVDA | 14 | 203.24 | 2,845.36 | 179.20 | +336.50 | +13.41% | USD | 4815747 |
| NVO | 5 | 43.00 | 215.00 | 42.54 | +2.30 | +1.08% | USD | 10611 |
| RBRK | 3 | 71.00 | 213.00 | 58.10 | +38.71 | +22.21% | USD | 699030013 |
| SPGI | 1 | 426.95 | 426.95 | 411.00 | +15.95 | +3.88% | USD | 229629397 |
| SPOT | 1 | 503.00 | 503.00 | 509.00 | -6.00 | -1.18% | USD | 312496724 |
| STIM | 345 | 1.24 | 427.80 | 1.75 | -175.50 | -29.09% | USD | 324062325 |
| TLT | 77 | 85.00 | 6,545.00 | 88.79 | -291.63 | -4.27% | USD | 15547841 |
| UBER | 3 | 69.22 | 207.66 | 82.02 | -38.41 | -15.61% | USD | 365207014 |
| V | 1 | 324.68 | 324.68 | 319.51 | +5.17 | +1.62% | USD | 49462172 |
| VEEV | 3 | 163.76 | 491.28 | 164.83 | -3.22 | -0.65% | USD | 136254493 |
| XEON | 10 | 149.34 | 1,493.39 | 149.03 | +3.14 | +0.21% | EUR | 46041702 |
| ZS | 1 | 125.40 | 125.40 | 157.16 | -31.76 | -20.21% | USD | 310621426 |

> **New position since the last sync (2026-06-07) — VEEV (Veeva Systems):** 3 shares @ avg cost $164.83. This corresponds to the `BUY 3 VEEV @ 164.50 GTC` limit order that was active as of the 2026-06-10 orders snapshot — it has now filled and no longer appears in `get_account_orders`.
>
> **Position size change — META:** 4 → 6 shares since 2026-06-07 (avg cost moved from $605.98 to $597.81, implying ~2 additional shares bought around $581/share). Data refresh only — no framework action taken as part of this sync.

> **Currency note:** all positions are USD except **XEON** (EUR-denominated, market value €1,493.39). Its USD-equivalent (used for `holdings.md` weighting) is computed using the live EUR→USD rate below — fetched directly from `get_account_balances`, not assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|----------------|
| USD | 2,317.34 | 2,317.34 | 1.000000 | 2,317.34 |
| EUR | 8.18 | 8.18 | 1.153162 | 9.43 |
| **Total (USD-equiv)** | | | | **2,326.77** |

*The same EUR→USD rate (1.153162) applied to XEON's €1,493.39 market value gives its USD-equivalent: **$1,722.12** — used in `holdings.md` for weighting.*

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

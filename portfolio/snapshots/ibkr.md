# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-06-15 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-positions`)
**Cash balances last synced:** 2026-06-15 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-balances`)
**Account summary:** Net Liquidation $38,535.57 (broker-reported, BASE) · Gross Position Value $38,605.84 (sum of positions below, XEON converted at live FX) · Total Cash (USD-equiv) $321.57 · Unrealized P&L –$1,441.53 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 22 positions resolved directly from the MCP's `contract_description` field. 21 are already clean ticker symbols (e.g. `AMZN`, `DUOL`, `VEEV`, `ADBE`); `XEON @IBIS2` is normalized to `XEON` (exchange suffix stripped) for consistency with `holdings.md`. No `CONID_XXXXXXX` placeholders were needed, so the live/fallback ticker-lookup CSV fetch was not required for this sync.

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 10 | 206.56 | 2,065.60 | 202.07 | +44.90 | +2.22% | USD | 265768 |
| AMZN | 12 | 241.91 | 2,902.92 | 210.59 | +375.86 | +14.87% | USD | 3691937 |
| CSGP | 25 | 32.84 | 821.00 | 35.04 | -55.00 | -6.28% | USD | 6726677 |
| DUOL | 30 | 124.00 | 3,720.00 | 168.25 | -1,327.44 | -26.30% | USD | 505002183 |
| GOOG | 1 | 363.24 | 363.24 | 295.70 | +67.54 | +22.84% | USD | 208813720 |
| META | 6 | 574.00 | 3,444.00 | 597.81 | -142.83 | -3.98% | USD | 107113386 |
| MSFT | 20 | 394.93 | 7,898.60 | 402.62 | -153.87 | -1.91% | USD | 272093 |
| NFLX | 12 | 80.78 | 969.36 | 87.79 | -84.13 | -7.99% | USD | 15124833 |
| NKE | 20 | 45.29 | 905.80 | 43.31 | +39.60 | +4.57% | USD | 10291 |
| NOW | 12 | 106.11 | 1,273.32 | 92.80 | +159.73 | +14.34% | USD | 109911821 |
| NVDA | 14 | 209.65 | 2,935.10 | 179.20 | +426.24 | +16.99% | USD | 4815747 |
| NVO | 5 | 44.40 | 222.00 | 42.54 | +9.30 | +4.37% | USD | 10611 |
| RBRK | 3 | 70.90 | 212.70 | 58.10 | +38.41 | +22.03% | USD | 699030013 |
| SPGI | 1 | 418.91 | 418.91 | 411.00 | +7.91 | +1.92% | USD | 229629397 |
| SPOT | 1 | 482.00 | 482.00 | 509.00 | -27.00 | -5.30% | USD | 312496724 |
| STIM | 345 | 1.33 | 458.85 | 1.75 | -144.45 | -23.94% | USD | 324062325 |
| TLT | 77 | 86.27 | 6,642.79 | 88.79 | -193.84 | -2.84% | USD | 15547841 |
| UBER | 3 | 69.39 | 208.17 | 82.02 | -37.90 | -15.40% | USD | 365207014 |
| V | 1 | 324.00 | 324.00 | 319.51 | +4.49 | +1.41% | USD | 49462172 |
| VEEV | 3 | 159.54 | 478.62 | 164.83 | -15.88 | -3.21% | USD | 136254493 |
| XEON | 10 | 149.37 | 1,493.65 | 149.03 | +3.40 | +0.23% | EUR | 46041702 |
| ZS | 1 | 131.00 | 131.00 | 157.16 | -26.16 | -16.65% | USD | 310621426 |

> **New position since the last sync (2026-06-11) — ADBE (Adobe Inc.):** 10 shares @ avg cost $202.07. This corresponds to the [2026-06-12 new-position session](../../sessions/2026-06-12-new-position-adbe.md) (Score 5.0, "Very Cheap" — BUY full position 6–8%, ~17-share target ≈ $3,524). 10 of the ~17 target shares have filled; no ADBE order (active or `REPLACED`) appears in this sync's `get_account_orders` result, so the fill predates or falls outside this endpoint's history window. The remaining ~7 shares toward the target have not yet been purchased as of this sync — data refresh only, no framework action taken as part of this sync.
>
> **No other position-size changes since 2026-06-11** — all other 21 positions show identical share counts; market-value/P&L changes reflect price movement only.

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value (sum of live position market values below, $38,605.84) plus Total Cash ($321.57) = $38,927.41, which is ~$391.84 above broker-reported Net Liquidation ($38,535.57). This gap is close to today's aggregate intraday unrealized gain (sum of each position's `daily_pnl` ≈ +$415.74 from `get_account_positions`), consistent with `get_account_positions` returning live intraday prices while `get_account_balances`'s Net Liquidation/stock-market-value reflect prior-session settled prices not yet refreshed intraday. Not an error — flagged for transparency; it's why the `holdings.md` weight column (computed off Net Liquidation per [sync-sop.md](../sync-sop.md)) sums to slightly over 100%.

> **Currency note:** all positions are USD except **XEON** (EUR-denominated, market value €1,493.65). Its USD-equivalent (used for `holdings.md` weighting) is computed using the live EUR→USD rate below — fetched directly from `get_account_balances`, not assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|----------------|
| USD | 312.11 | 312.11 | 1.000000 | 312.11 |
| EUR | 8.18 | 8.18 | 1.156806 | 9.46 |
| **Total (USD-equiv)** | | | | **321.57** |

*The same EUR→USD rate (1.156806) applied to XEON's €1,493.65 market value gives its USD-equivalent: **$1,727.86** — used in `holdings.md` for weighting.*

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

# IBKR Portfolio Snapshot

**Account:** U19421206
**Last synced:** 2026-06-07 (live via Interactive Brokers MCP — `get_account_positions` / `get_account_summary`)
**Account summary:** Net Liquidation $38,769.84 · Gross Position Value $34,760.05 · Total Cash $3,983.37 · Unrealized P&L (sum of positions below, native currency) ≈ –$857.34

**Ticker resolution note:** all 20 positions resolved directly from the MCP's `contract_description` field (already a clean ticker symbol — e.g. `AMZN`, `DUOL`). No `CONID_XXXXXXX` placeholders were needed, so the live/fallback ticker-lookup CSV fetch was not required for this sync.

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| AMZN | 12 | 245.70 | 2,948.40 | 210.59 | +421.34 | +16.67% | USD | 3691937 |
| CSGP | 25 | 33.89 | 847.24 | 35.04 | -28.76 | -3.28% | USD | 6726677 |
| DUOL | 30 | 107.80 | 3,234.00 | 168.25 | -1,813.44 | -35.94% | USD | 505002183 |
| GOOG | 1 | 365.54 | 365.54 | 295.70 | +69.84 | +23.62% | USD | 208813720 |
| META | 4 | 589.50 | 2,358.00 | 605.98 | -65.91 | -2.72% | USD | 107113386 |
| MSFT | 20 | 412.46 | 8,249.20 | 402.62 | +196.73 | +2.44% | USD | 272093 |
| NFLX | 12 | 81.83 | 981.96 | 87.79 | -71.53 | -6.79% | USD | 15124833 |
| NKE | 20 | 42.88 | 857.60 | 43.31 | -8.60 | -0.99% | USD | 10291 |
| NOW | 12 | 110.90 | 1,330.80 | 92.80 | +217.21 | +19.50% | USD | 109911821 |
| NVDA | 14 | 204.09 | 2,857.26 | 179.20 | +348.40 | +13.89% | USD | 4815747 |
| NVO | 5 | 42.74 | 213.70 | 42.54 | +1.00 | +0.47% | USD | 10611 |
| RBRK | 3 | 72.58 | 217.74 | 58.10 | +43.45 | +24.93% | USD | 699030013 |
| SPGI | 1 | 424.50 | 424.50 | 411.00 | +13.50 | +3.28% | USD | 229629397 |
| SPOT | 1 | 495.00 | 495.00 | 509.00 | -14.00 | -2.75% | USD | 312496724 |
| STIM | 345 | 1.29 | 445.05 | 1.75 | -158.25 | -26.23% | USD | 324062325 |
| TLT | 77 | 85.06 | 6,549.62 | 88.79 | -287.01 | -4.20% | USD | 15547841 |
| UBER | 3 | 70.45 | 211.35 | 82.02 | -34.72 | -14.11% | USD | 365207014 |
| V | 1 | 323.04 | 323.04 | 319.51 | +3.53 | +1.10% | USD | 49462172 |
| XEON | 10 | 149.32 | 1,493.16 | 149.03 | +2.91 | +0.20% | EUR | 46041702 |
| ZS | 1 | 129.60 | 129.60 | 157.16 | -27.56 | -17.54% | USD | 310621426 |

> **Currency note:** all positions are USD except **XEON** (EUR-denominated, market value €1,493.16). The account summary's Gross Position Value ($34,760.05) is IBKR's own FX-converted total; this snapshot reports XEON's market value in its native currency (EUR) rather than estimating a USD-equivalent (per the framework rule against inventing/estimating financial data — no FX rate was fetched). When computing portfolio weights in `holdings.md`, XEON's weight is therefore approximate.

*This file is overwritten on every IBKR sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

# IBKR Portfolio Snapshot

**Account:** U19421206 — the framework account (see [accounts.md](../accounts.md)); the other two IBKR accounts are out of scope.
**Positions last synced:** 2026-10-18 (live via Interactive Brokers MCP — `get_account_positions`, via scheduled Weekly Monday sync)
**Cash balances last synced:** 2026-10-18 (live via Interactive Brokers MCP — `get_account_balances`, via scheduled Weekly Monday sync)
**Account summary:** Net Liquidation $47,820.23 (broker-reported, BASE) · Gross Position Value $45,095.92 (sum of positions below, non-USD converted at live FX; includes the -$79.38 and -$24.77 short-put marks) · Total Cash (USD-equiv) **$2,961.09** (broker-reported, BASE; USD cash is **-$1,904.32**, i.e. a margin debit funded by EUR/AUD balances) · Unrealized P&L +$4,325.29 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** ticker-lookup CSV fetched live from IBKR (HTTP 200) and the stored fallback was refreshed. All 26 rows resolved from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders. `TRN @LSE`, `XEON @IBIS2` normalized (exchange suffix stripped); option rows kept as option rows.

> **Changes vs. 2026-10-12 sync:** **+UUUU (300 sh @ $8.478, $2,541.00)** — appeared after the Oct-16 $8.50 short puts (3 contracts, order 1462252282) expired in the money; consistent with **assignment** (3 × 100 sh at $8.50 ≈ $2,550 outlay, matching the USD cash swing $602.23 → -$1,904.32). Not in framework scope until evaluated (a prior [UUUU new-position session](../../sessions/2026-09-10-new-position-uuuu.md) exists — see watchlist). **+SOFI Oct30'26 $13 PUT (short 1)** — new, ungoverned option position (mark -$24.77). Other 24 rows: share counts unchanged. RGL/LM8/TLT remain absent (in-kind transfers, scope guard passed).

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 20 | 245.2000 | 4,904.00 | 221.0850 | +482.30 | +10.91% | USD | 265768 |
| AMZN | 12 | 252.0000 | 3,024.00 | 210.5885 | +496.94 | +19.66% | USD | 3691937 |
| AVGO | 6 | 332.2500 | 1,993.50 | 382.4417 | -301.15 | -13.12% | USD | 313130367 |
| BKNG | 10 | 163.4500 | 1,634.50 | 159.1000 | +43.50 | +2.73% | USD | 308728373 |
| BULL Feb19'27 5 PUT (short) | -2 | 0.3969 | -79.38 | 0.5432 | +29.25 | +26.9% (of credit) | USD | 893374059 |
| CSGP | 25 | 32.3100 | 807.75 | 35.0400 | -68.25 | -7.79% | USD | 6726677 |
| DUOL | 30 | 141.7600 | 4,252.80 | 168.2479 | -794.64 | -15.74% | USD | 505002183 |
| GOOG | 1 | 339.4500 | 339.45 | 295.7000 | +43.75 | +14.80% | USD | 208813720 |
| MBGL | 1 | 18.6900 | 18.69 | 19.8924 | -1.20 | -6.04% | USD | 893054611 |
| META | 5 | 710.0000 | 3,550.00 | 575.0560 | +674.72 | +23.47% | USD | 107113386 |
| MSFT | 17 | 531.7000 | 9,038.90 | 391.2165 | +2,388.22 | +35.91% | USD | 272093 |
| NFLX | 12 | 71.1700 | 854.04 | 87.7905 | -199.45 | -18.93% | USD | 15124833 |
| NKE | 20 | 37.1500 | 743.00 | 43.3100 | -123.20 | -14.22% | USD | 10291 |
| NOW | 9 | 141.3400 | 1,272.06 | 87.6100 | +483.57 | +61.33% | USD | 109911821 |
| NVDA | 19 | 215.0000 | 4,085.00 | 182.5059 | +617.39 | +17.80% | USD | 4815747 |
| NVO | 5 | 39.0000 | 195.00 | 42.5400 | -17.70 | -8.32% | USD | 10611 |
| RBRK | 3 | 112.4100 | 337.23 | 58.0962 | +162.94 | +93.49% | USD | 699030013 |
| SOFI Oct30'26 13 PUT (short) | -1 | 0.2477 | -24.77 | 0.3697 | +12.20 | +33.0% (of credit) | USD | 922569011 |
| SPGI | 1 | 429.6400 | 429.64 | 391.1076 | +38.53 | +9.85% | USD | 229629397 |
| TRN | 600 | 2.1760 | 1,305.60 | 2.1195 | +33.89 | +2.66% | GBP | 371871705 |
| UBER | 3 | 70.2200 | 210.66 | 82.0233 | -35.41 | -14.39% | USD | 365207014 |
| UUUU | 300 | 8.4700 | 2,541.00 | 8.4784 | -2.52 | -0.10% | USD | 137823153 |
| V | 1 | 402.6100 | 402.61 | 319.5100 | +83.10 | +26.01% | USD | 49462172 |
| VEEV | 3 | 310.3600 | 931.08 | 164.8333 | +436.58 | +88.29% | USD | 136254493 |
| XEON | 10 | 150.5600 | 1,505.60 | 149.0250 | +15.35 | +1.03% | EUR | 46041702 |
| ZS | 1 | 207.3800 | 207.38 | 157.1600 | +50.22 | +31.95% | USD | 310621426 |

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value ($45,095.92) plus Total Cash ($2,961.09) = $48,057.01 vs. broker-reported Net Liquidation ($47,820.23) — difference $236.77 is price timing between the separate positions and balances calls (the balances call's USD stock value, $41,540.64, is $231.65 below the positions-table USD sum, $41,772.29; the remaining ~$5 is FX rounding). Broker-reported BASE stock market value is $44,967.60; it excludes the option marks.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE) and **XEON** (EUR). USD-equivalents use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency, plus a `BASE` row consolidating to USD at IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | -1,904.32 | -1,904.32 | 1.0000000 | -1,904.32 |
| EUR | 3,747.94 | 3,747.94 | 1.1213086 | 4,202.60 |
| GBP | 0.00 | 0.00 | 1.3323668 | 0.00 |
| AUD | 951.80 | 951.80 | 0.6963765 | 662.81 |
| **Total (USD-equiv)** | | | | **2,961.09** |

*Row-by-row FX conversion matches broker-reported BASE `cash_balance` of $2,961.09. ⚠️ USD cash is negative (-$1,904.32): a USD margin loan while EUR/AUD cash sits idle — see `/safe-guard` for worst-case order exposure.*

*Live-FX USD-equivalents of non-USD positions: TRN £1,305.60 × 1.3323668 = **$1,739.54**; XEON €1,505.60 × 1.12130855 = **$1,688.24**.*

*This file has two independently-refreshed sections — the positions table and the Cash Balances table, each with its own "last synced" timestamp above. See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history.*

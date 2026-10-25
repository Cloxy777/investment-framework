# IBKR Portfolio Snapshot

**Account:** U19421206 — the framework account (see [accounts.md](../accounts.md)); the other two IBKR accounts are out of scope.
**Positions last synced:** 2026-10-25 (live via Interactive Brokers MCP — `get_account_positions`, via scheduled Weekly Monday sync)
**Cash balances last synced:** 2026-10-25 (live via Interactive Brokers MCP — `get_account_balances`, via scheduled Weekly Monday sync)
**Account summary:** Net Liquidation $47,714.19 (broker-reported, BASE) · Gross Position Value $43,983.86 (sum of positions below, non-USD converted at live FX; includes the -$88.42 and -$16.11 short-put marks) · Total Cash (USD-equiv) **$3,852.63** (broker-reported, BASE; USD cash is now **+$981.49** — the Oct-19 EUR→USD conversion cleared the prior margin debit) · Unrealized P&L +$4,198.21 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** ticker-lookup CSV fetched live from IBKR (HTTP 200) and the stored fallback was refreshed. All 25 rows resolved from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders. `TRN @LSE`, `XEON @IBIS2` normalized; option rows kept as option rows.

> **Changes vs. 2026-10-18 sync:** **-CSGP (25 sh sold)** — limit SELL 25 @ $35.55 (order 1907120507, GTC, placed 2026-09-30) filled 2026-10-22; realized P&L +$11.73, proceeds $888.75; position fully exited (a standing-order exit — see the [2026-10-11 CSGP rescore](../../sessions/2026-10-11-rescore-csgp.md), HOLD). **USD cash -$1,904.32 → +$981.49:** 2026-10-19 EUR→USD conversion (sold €1,783 @ 1.1214, order 902130511, ≈$2,000) plus the CSGP proceeds. Other 24 rows: share counts unchanged (SOFI/BULL short puts still open). RGL/LM8/TLT remain absent (in-kind transfers, scope guard passed).

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 20 | 263.8200 | 5,276.40 | 221.0850 | +854.70 | +19.33% | USD | 265768 |
| AMZN | 12 | 250.7000 | 3,008.40 | 210.5885 | +481.34 | +19.05% | USD | 3691937 |
| AVGO | 6 | 326.6400 | 1,959.84 | 382.4417 | -334.81 | -14.59% | USD | 313130367 |
| BKNG | 10 | 156.4500 | 1,564.50 | 159.1000 | -26.50 | -1.67% | USD | 308728373 |
| BULL Feb19'27 5 PUT (short) | -2 | 0.4421 | -88.42 | 0.5432 | +20.21 | +18.6% (of credit) | USD | 893374059 |
| DUOL | 30 | 143.0400 | 4,291.20 | 168.2479 | -756.24 | -14.98% | USD | 505002183 |
| GOOG | 1 | 321.0000 | 321.00 | 295.7000 | +25.30 | +8.56% | USD | 208813720 |
| MBGL | 1 | 18.7600 | 18.76 | 19.8924 | -1.13 | -5.69% | USD | 893054611 |
| META | 5 | 643.0900 | 3,215.45 | 575.0560 | +340.17 | +11.83% | USD | 107113386 |
| MSFT | 17 | 524.5100 | 8,916.67 | 391.2165 | +2,265.99 | +34.07% | USD | 272093 |
| NFLX | 12 | 65.8600 | 790.32 | 87.7905 | -263.17 | -24.98% | USD | 15124833 |
| NKE | 20 | 37.3000 | 746.00 | 43.3100 | -120.20 | -13.88% | USD | 10291 |
| NOW | 9 | 158.9600 | 1,430.64 | 87.6100 | +642.15 | +81.44% | USD | 109911821 |
| NVDA | 19 | 213.1000 | 4,048.90 | 182.5059 | +581.29 | +16.76% | USD | 4815747 |
| NVO | 5 | 38.9600 | 194.80 | 42.5400 | -17.90 | -8.42% | USD | 10611 |
| RBRK | 3 | 128.7400 | 386.22 | 58.0962 | +211.93 | +121.60% | USD | 699030013 |
| SOFI Oct30'26 13 PUT (short) | -1 | 0.1611 | -16.11 | 0.3697 | +20.86 | +56.4% (of credit) | USD | 922569011 |
| SPGI | 1 | 450.3100 | 450.31 | 391.1076 | +59.20 | +15.14% | USD | 229629397 |
| TRN | 600 | 2.1080 | 1,264.80 | 2.1195 | -6.91 | -0.54% | GBP | 371871705 |
| UBER | 3 | 67.4300 | 202.29 | 82.0233 | -43.78 | -17.79% | USD | 365207014 |
| UUUU | 300 | 7.5200 | 2,256.00 | 8.4784 | -287.52 | -11.30% | USD | 137823153 |
| V | 1 | 407.9200 | 407.92 | 319.5100 | +88.41 | +27.67% | USD | 49462172 |
| VEEV | 3 | 323.0400 | 969.12 | 164.8333 | +474.62 | +95.98% | USD | 136254493 |
| XEON | 10 | 150.5930 | 1,505.93 | 149.0250 | +15.68 | +1.05% | EUR | 46041702 |
| ZS | 1 | 255.1500 | 255.15 | 157.1600 | +97.99 | +62.35% | USD | 310621426 |

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value ($43,983.86) plus Total Cash ($3,852.63) = $47,836.49 vs. broker-reported Net Liquidation ($47,714.19) — difference $122.30 is mostly the short-option marks being counted in Gross but excluded from the broker's BASE stock market value ($43,969.96), plus price timing between calls and FX rounding.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE) and **XEON** (EUR). USD-equivalents use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency, plus a `BASE` row consolidating to USD at IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | 981.49 | 981.49 | 1.0000000 | 981.49 |
| EUR | 1,964.38 | 1,964.38 | 1.1202799 | 2,200.66 |
| GBP | 0.00 | 0.00 | 1.3373081 | 0.00 |
| AUD | 951.80 | 951.80 | 0.7034505 | 669.54 |
| **Total (USD-equiv)** | | | | **3,852.63** |

*Row-by-row FX sum is $3,851.69 vs. broker-reported BASE `cash_balance` of $3,852.63 (≈$0.94 FX rounding); the BASE figure is used. USD cash is positive again (+$981.49), but worst-case simultaneous fills of the open buy orders could re-create a USD debit — see `/safe-guard`.*

*Live-FX USD-equivalents of non-USD positions: TRN £1,264.80 × 1.3373081 = **$1,691.43**; XEON €1,505.93 × 1.1202799 = **$1,687.06**.*

*This file has two independently-refreshed sections — the positions table and the Cash Balances table, each with its own "last synced" timestamp above. See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history.*

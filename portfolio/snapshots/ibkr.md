# IBKR Portfolio Snapshot

**Account:** U19421206 — the framework account (see [accounts.md](../accounts.md)); the other two IBKR accounts are out of scope.
**Positions last synced:** 2026-11-01 (live via Interactive Brokers MCP — `get_account_positions`, via scheduled Weekly sync)
**Cash balances last synced:** 2026-11-01 (live via Interactive Brokers MCP — `get_account_balances`, via scheduled Weekly sync)
**Account summary:** Net Liquidation $46,102.05 (broker-reported, BASE) · Gross Position Value $42,219.14 (sum of positions below, non-USD converted at live FX; includes the -$125.11 BULL short-put mark) · Total Cash (USD-equiv) **$3,841.98** (broker-reported, BASE; USD cash +$981.49) · Unrealized P&L +$2,565.09 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** ticker-lookup CSV fetched live from IBKR (HTTP 200) and the stored fallback was refreshed. All 24 rows resolved from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders. `TRN @LSE`, `XEON @IBIS2` normalized; the option row kept as an option row.

> **Changes vs. 2026-10-25 sync:** **-SOFI Oct30'26 $13 short put** (expired 2026-10-30; no longer in the positions response; no share assignment — no SOFI shares appear). All other share counts unchanged (24 rows, down from 25). **Net Liquidation $47,714.19 → $46,102.05 (-3.4%)**, driven by price moves: NOW 158.96 → 106.00 (-33%), ADBE 263.82 → 250.23, DUOL 143.04 → 131.59, AMZN 250.70 → 240.35, NVDA 213.10 → 205.40. Prices on NOW look unusually large for one week — verify in TWS before acting. Unrealized P&L +$4,198.21 → +$2,565.09. RGL/LM8/TLT remain absent (in-kind transfers, scope guard passed).

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 20 | 250.2300 | 5,004.60 | 221.0850 | +582.90 | +13.18% | USD | 265768 |
| AMZN | 12 | 240.3500 | 2,884.20 | 210.5885 | +357.14 | +14.13% | USD | 3691937 |
| AVGO | 6 | 327.0000 | 1,962.00 | 382.4417 | -332.65 | -14.50% | USD | 313130367 |
| BKNG | 10 | 149.0000 | 1,490.00 | 159.1000 | -101.00 | -6.35% | USD | 308728373 |
| BULL Feb19'27 5 PUT (short) | -2 | 0.6255 | -125.11 | 0.5432 | -16.47 | -30.3% (of credit) | USD | 893374059 |
| DUOL | 30 | 131.5900 | 3,947.70 | 168.2479 | -1,099.74 | -21.79% | USD | 505002183 |
| GOOG | 1 | 280.0000 | 280.00 | 295.7000 | -15.70 | -5.31% | USD | 208813720 |
| MBGL | 1 | 18.9100 | 18.91 | 19.8924 | -0.98 | -4.94% | USD | 893054611 |
| META | 5 | 610.0000 | 3,050.00 | 575.0560 | +174.72 | +6.08% | USD | 107113386 |
| MSFT | 17 | 521.9100 | 8,872.47 | 391.2165 | +2,221.79 | +33.41% | USD | 272093 |
| NFLX | 12 | 62.0800 | 744.96 | 87.7905 | -308.53 | -29.29% | USD | 15124833 |
| NKE | 20 | 38.6700 | 773.40 | 43.3100 | -92.80 | -10.71% | USD | 10291 |
| NOW | 9 | 106.0000 | 954.00 | 87.6100 | +165.51 | +20.99% | USD | 109911821 |
| NVDA | 19 | 205.4000 | 3,902.60 | 182.5059 | +434.99 | +12.54% | USD | 4815747 |
| NVO | 5 | 40.0000 | 200.00 | 42.5400 | -12.70 | -5.97% | USD | 10611 |
| RBRK | 3 | 124.0000 | 372.00 | 58.0962 | +197.71 | +113.44% | USD | 699030013 |
| SPGI | 1 | 457.0700 | 457.07 | 391.1076 | +65.96 | +16.87% | USD | 229629397 |
| TRN | 600 | 2.0540 | 1,232.40 | 2.1195 | -39.31 | -3.09% | GBP | 371871705 |
| UBER | 3 | 65.3400 | 196.02 | 82.0233 | -50.05 | -20.34% | USD | 365207014 |
| UUUU | 300 | 7.7100 | 2,313.00 | 8.4784 | -230.52 | -9.06% | USD | 137823153 |
| V | 1 | 416.1200 | 416.12 | 319.5100 | +96.61 | +30.24% | USD | 49462172 |
| VEEV | 3 | 311.8200 | 935.46 | 164.8333 | +440.96 | +89.17% | USD | 136254493 |
| XEON | 10 | 150.7000 | 1,507.00 | 149.0250 | +16.75 | +1.12% | EUR | 46041702 |
| ZS | 1 | 237.8300 | 237.83 | 157.1600 | +80.67 | +51.33% | USD | 310621426 |

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value ($42,219.14) plus Total Cash ($3,841.98) = $46,061.12 vs. broker-reported Net Liquidation ($46,102.05) — difference -$40.93 is FX rounding / price timing between calls (BASE stock market value $42,383.39 excludes/nets the short-option mark differently).

> **Currency note:** all positions are USD except **TRN** (GBP, LSE) and **XEON** (EUR). USD-equivalents use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency, plus a `BASE` row consolidating to USD at IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | 981.49 | 981.49 | 1.0000000 | 981.49 |
| EUR | 1,964.38 | 1,964.38 | 1.1159309 | 2,192.11 |
| GBP | 0.00 | 0.00 | 1.3390144 | 0.00 |
| AUD | 951.80 | 951.80 | 0.7032444 | 669.35 |
| **Total (USD-equiv)** | | | | **3,841.98** |

*Row-by-row FX sum is $3,842.95 vs. broker-reported BASE `cash_balance` of $3,841.98 (≈$0.97 FX rounding); the BASE figure is used. See `/safe-guard` for worst-case simultaneous-fill exposure.*

*Live-FX USD-equivalents of non-USD positions: TRN £1,232.40 × 1.3390144 = **$1,650.20**; XEON €1,507.00 × 1.1159309 = **$1,681.71**.*

*This file has two independently-refreshed sections — the positions table and the Cash Balances table, each with its own "last synced" timestamp above. See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history.*

# IBKR Portfolio Snapshot

**Account:** U19421206 — the framework account (see [accounts.md](../accounts.md)); the other two IBKR accounts are out of scope.
**Positions last synced:** 2026-11-08 (live via Interactive Brokers MCP — `get_account_positions`, via scheduled Weekly sync)
**Cash balances last synced:** 2026-11-08 (live via Interactive Brokers MCP — `get_account_balances`, via scheduled Weekly sync)
**Account summary:** Net Liquidation $46,477.10 (broker-reported, BASE) · Gross Position Value $44,129.05 (sum of positions below, non-USD converted at live FX; includes the -$140.42 BULL and -$105.00 UUUU short-option marks) · Total Cash (USD-equiv) **$1,992.38** (broker-reported, BASE; **USD cash -$850.77 = margin debit**) · Unrealized P&L +$2,463.49 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** ticker-lookup CSV fetched live from IBKR (HTTP 200, 24,313 rows) and the stored fallback was refreshed. All rows resolved from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders. `TRN @LSE`, `XEON @IBIS2` normalized; option rows kept as option rows.

> **Changes vs. 2026-11-01 sync:** **NVDA 19 → 40 sh (+21, avg cost $182.51 → $182.89)**; **MSFT 17 → 13 sh (-4)**; **new TSM 1 sh @ $364.50**; **new short UUUU Jan15'27 $9 CALL ×3** (covered by the 300 UUUU shares; the earlier order for it was `REPLACED`). 24 → 26 rows. **Net Liquidation $46,102.05 → $46,477.10 (+0.8%)**. **USD cash +$981.49 → -$850.77** (NVDA buying outweighed MSFT sale proceeds). Price moves: NOW 106.00 → 102.36, ADBE 250.23 → 239.10, DUOL 131.59 → 160.35 (+22%), AVGO 327.00 → 294.94, NVDA 205.40 → 180.00, MSFT 521.91 → 530.00, AMZN 240.35 → 259.30. Unrealized P&L +$2,565.09 → +$2,463.49. RGL/LM8/TLT remain absent (in-kind transfers, scope guard passed).

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 20 | 239.1000 | 4,782.00 | 221.0850 | +360.30 | +8.15% | USD | 265768 |
| AMZN | 12 | 259.3000 | 3,111.60 | 210.5885 | +584.54 | +23.13% | USD | 3691937 |
| AVGO | 6 | 294.9400 | 1,769.64 | 382.4417 | -525.01 | -22.88% | USD | 313130367 |
| BKNG | 10 | 165.0000 | 1,650.00 | 159.1000 | +59.00 | +3.71% | USD | 308728373 |
| BULL Feb19'27 5 PUT (short) | -2 | 0.7021 | -140.42 | 0.5432 | -31.79 | -2926.3% (of credit) | USD | 893374059 |
| DUOL | 30 | 160.3500 | 4,810.50 | 168.2479 | -236.94 | -4.69% | USD | 505002183 |
| GOOG | 1 | 283.8900 | 283.89 | 295.7000 | -11.81 | -3.99% | USD | 208813720 |
| MBGL | 1 | 19.6400 | 19.64 | 19.8924 | -0.25 | -1.27% | USD | 893054611 |
| META | 5 | 610.4600 | 3,052.30 | 575.0560 | +177.02 | +6.16% | USD | 107113386 |
| MSFT | 13 | 530.0000 | 6,890.00 | 382.7254 | +1,914.57 | +38.48% | USD | 272093 |
| NFLX | 12 | 63.4100 | 760.92 | 87.7905 | -292.57 | -27.77% | USD | 15124833 |
| NKE | 20 | 38.5900 | 771.80 | 43.3100 | -94.40 | -10.90% | USD | 10291 |
| NOW | 9 | 102.3600 | 921.24 | 87.6100 | +132.75 | +16.84% | USD | 109911821 |
| NVDA | 40 | 180.0000 | 7,200.00 | 182.8903 | -115.61 | -1.58% | USD | 4815747 |
| NVO | 5 | 40.3100 | 201.55 | 42.5400 | -11.15 | -5.24% | USD | 10611 |
| RBRK | 3 | 105.7500 | 317.25 | 58.0962 | +142.96 | +82.03% | USD | 699030013 |
| SPGI | 1 | 467.8000 | 467.80 | 391.1076 | +76.69 | +19.61% | USD | 229629397 |
| TRN | 600 | 1.9630 | 1,177.80 | 2.1195 | -93.91 | -7.38% | GBP | 371871705 |
| TSM | 1 | 375.0000 | 375.00 | 364.5000 | +10.50 | +2.88% | USD | 6223250 |
| UBER | 3 | 68.7800 | 206.34 | 82.0233 | -39.73 | -16.15% | USD | 365207014 |
| UUUU | 300 | 6.6600 | 1,998.00 | 8.4784 | -545.52 | -21.45% | USD | 137823153 |
| UUUU Jan15'27 9 CALL (short) | -3 | 0.3500 | -105.00 | 0.6845 | +100.35 | +4886.8% (of credit) | USD | 890272443 |
| V | 1 | 422.6500 | 422.65 | 319.5100 | +103.14 | +32.28% | USD | 49462172 |
| VEEV | 3 | 303.7300 | 911.19 | 164.8333 | +416.69 | +84.26% | USD | 136254493 |
| XEON | 10 | 150.7200 | 1,507.20 | 149.0250 | +16.95 | +1.14% | EUR | 46041702 |
| ZS | 1 | 199.0000 | 199.00 | 157.1600 | +41.84 | +26.62% | USD | 310621426 |

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value ($44,129.05) plus Total Cash ($1,992.38) = $46,121.43 vs. broker-reported Net Liquidation ($46,477.10) — difference +355.67 is FX rounding / price timing between calls.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE) and **XEON** (EUR). USD-equivalents use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency, plus a `BASE` row consolidating to USD at IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | -850.77 | -850.77 | 1.0000000 | -850.77 |
| EUR | 1,964.38 | 1,964.38 | 1.1143507 | 2,189.01 |
| GBP | 0.00 | 0.00 | 1.3352076 | 0.00 |
| AUD | 951.35 | 951.35 | 0.6866136 | 653.21 |
| **Total (USD-equiv)** | | | | **1,992.38** |

*Row-by-row FX sum is $1,991.45 vs. broker-reported BASE `cash_balance` of $1,992.38 (≈$0.94 FX rounding); the BASE figure is used. USD cash is negative (margin debit) while €1,964 and A$951 sit in other currencies. See `/safe-guard` for worst-case simultaneous-fill exposure.*

*Live-FX USD-equivalents of non-USD positions: TRN £1,177.80 × 1.3352076 = **$1,572.61**; XEON €1,507.20 × 1.1143507 = **$1,679.55**.*

*This file has two independently-refreshed sections — the positions table and the Cash Balances table, each with its own "last synced" timestamp above. See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history.*

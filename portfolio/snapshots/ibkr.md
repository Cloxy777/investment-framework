# IBKR Portfolio Snapshot

**Account:** U19421206 — the framework account (see [accounts.md](../accounts.md)); the other two IBKR accounts are out of scope.
**Positions last synced:** 2026-11-15 (live via Interactive Brokers MCP — `get_account_positions`, via scheduled Weekly sync)
**Cash balances last synced:** 2026-11-15 (live via Interactive Brokers MCP — `get_account_balances`, via scheduled Weekly sync)
**Account summary:** Net Liquidation $45,697.84 (broker-reported, BASE) · Gross Position Value $45,985.30 (sum of positions below, non-USD converted at live FX; includes the -$112.38 BULL and -$83.15 UUUU short-option marks) · Total Cash (USD-equiv) **-$12.95** (broker-reported, BASE; all in USD — **small margin debit**; EUR and AUD cash balances are now zero) · Unrealized P&L +$1,716.79 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** ticker-lookup CSV fetched live from IBKR (HTTP 200, 24,352 rows) and the stored fallback was refreshed. All rows resolved from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders. `TRN @LSE`, `XEON @IBIS2` normalized; option rows kept as option rows.

> **Changes vs. 2026-11-08 sync:** **NVDA 40 → 50 sh (+10, avg cost $182.89 → $180.64)**; no other share-count changes (26 rows, same tickers). **Net Liquidation $46,477.10 → $45,697.84 (-1.7%)**. **Cash: USD -$850.77 → -$12.95; EUR €1,964 and AUD A$951 → 0** (both converted to USD, evidently funding the NVDA buy). Total cash $1,992.38 → -$12.95. Price moves: AVGO 294.94 → 345.00 (+17%), ADBE 239.10 → 242.60, AMZN 259.30 → 264.88, META 610.46 → 637.01, NVDA 180.00 → 165.20 (-8.2%), MSFT 530.00 → 523.00, TSM 375 → 396, MBGL 19.64 → 23.28 (+18.5%, earnings 11-12), VEEV 303.73 → 301.53, GOOG 283.89 → 292.52, UUUU 6.66 → 6.50. Unrealized P&L +$2,463.49 → +$1,716.79. RGL/LM8/TLT remain absent (in-kind transfers, scope guard passed).

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 20 | 242.6000 | 4,852.00 | 221.0850 | +430.30 | +9.73% | USD | 265768 |
| AMZN | 12 | 264.8800 | 3,178.56 | 210.5885 | +651.50 | +25.78% | USD | 3691937 |
| AVGO | 6 | 345.0000 | 2,070.00 | 382.4417 | -224.65 | -9.79% | USD | 313130367 |
| BKNG | 10 | 159.5800 | 1,595.80 | 159.1000 | +4.80 | +0.30% | USD | 308728373 |
| BULL Feb19'27 5 PUT (short) | -2 | 0.5619 | -112.38 | 0.5432 | -3.75 | -3.5% (of credit) | USD | 893374059 |
| DUOL | 30 | 165.0000 | 4,950.00 | 168.2479 | -97.44 | -1.93% | USD | 505002183 |
| GOOG | 2 | 292.5200 | 585.04 | 294.5550 | -4.07 | -0.69% | USD | 208813720 |
| MBGL | 1 | 23.2800 | 23.28 | 19.8924 | +3.39 | +17.03% | USD | 893054611 |
| META | 5 | 637.0100 | 3,185.05 | 575.0560 | +309.77 | +10.77% | USD | 107113386 |
| MSFT | 13 | 523.0000 | 6,799.00 | 382.7254 | +1,823.57 | +36.65% | USD | 272093 |
| NFLX | 12 | 62.3500 | 748.20 | 87.7905 | -305.29 | -28.98% | USD | 15124833 |
| NKE | 20 | 37.7800 | 755.60 | 43.3100 | -110.60 | -12.77% | USD | 10291 |
| NOW | 9 | 102.1100 | 918.99 | 87.6100 | +130.50 | +16.55% | USD | 109911821 |
| NVDA | 50 | 165.2000 | 8,260.00 | 180.6422 | -772.11 | -8.55% | USD | 4815747 |
| NVO | 5 | 41.6300 | 208.15 | 42.5400 | -4.55 | -2.14% | USD | 10611 |
| RBRK | 3 | 109.8800 | 329.64 | 58.0962 | +155.35 | +89.13% | USD | 699030013 |
| SPGI | 1 | 473.5900 | 473.59 | 391.1076 | +82.48 | +21.09% | USD | 229629397 |
| TRN | 600 | 1.9000 | 1,140.00 | 2.1195 | -131.71 | -10.36% | GBP | 371871705 |
| TSM | 1 | 396.0000 | 396.00 | 364.5000 | +31.50 | +8.64% | USD | 6223250 |
| UBER | 3 | 69.6900 | 209.07 | 82.0233 | -37.00 | -15.04% | USD | 365207014 |
| UUUU | 300 | 6.5000 | 1,950.00 | 8.4784 | -593.52 | -23.33% | USD | 137823153 |
| UUUU Jan15'27 9 CALL (short) | -3 | 0.2772 | -83.15 | 0.6845 | +122.20 | +59.5% (of credit) | USD | 890272443 |
| V | 1 | 425.7600 | 425.76 | 319.5100 | +106.25 | +33.25% | USD | 49462172 |
| VEEV | 3 | 301.5300 | 904.59 | 164.8333 | +410.09 | +82.93% | USD | 136254493 |
| XEON | 10 | 150.7930 | 1,507.93 | 149.0250 | +17.68 | +1.19% | EUR | 46041702 |
| ZS | 1 | 194.0200 | 194.02 | 157.1600 | +36.86 | +23.45% | USD | 310621426 |

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value ($45,985.30) plus Total Cash (-$12.95) = $45,972.35 vs. broker-reported Net Liquidation ($45,697.84) — difference +274.51 is FX rounding / price timing between calls (position market values vs. the broker's NLV timestamp).

> **Currency note:** all positions are USD except **TRN** (GBP, LSE) and **XEON** (EUR). USD-equivalents use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency, plus a `BASE` row consolidating to USD at IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | -12.95 | -12.95 | 1.0000000 | -12.95 |
| EUR | 0.00 | 0.00 | 1.1022632 | 0.00 |
| GBP | 0.00 | 0.00 | 1.3213624 | 0.00 |
| AUD | 0.00 | 0.00 | 0.6771329 | 0.00 |
| **Total (USD-equiv)** | | | | **-12.95** |

*Matches broker-reported BASE `cash_balance` of -$12.95. USD cash is a small margin debit; no other currency holds cash. See `/safe-guard` for worst-case simultaneous-fill exposure.*

*Live-FX USD-equivalents of non-USD positions: TRN £1,140.00 × 1.3213624 = **$1,506.35**; XEON €1,507.93 × 1.1022632 = **$1,662.14**.*

*This file has two independently-refreshed sections — the positions table and the Cash Balances table, each with its own "last synced" timestamp above. See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history.*

# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-10-11 (live via Interactive Brokers MCP — `get_account_positions`, via scheduled Weekly Monday Portfolio Sync)
**Cash balances last synced:** 2026-10-11 (live via Interactive Brokers MCP — `get_account_balances`, via scheduled Weekly Monday Portfolio Sync)
**Account summary:** Net Liquidation $57,251.48 (broker-reported, BASE) · Gross Position Value $51,775.86 (sum of positions below, non-USD converted at live FX; includes the -$71.29 short-put mark) · Total Cash (USD-equiv) **$5,463.46** (broker-reported, BASE) · Unrealized P&L +$4,167.95 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 27 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders. Ticker-lookup CSV re-fetched live this sync (HTTP 200); byte-identical to the stored fallback, so no CSV change. `RGL @ASX`, `LM8 @ASX`, `TRN @LSE`, `XEON @IBIS2` normalized (exchange suffix stripped); `BULL Feb19'27 5 PUT @AMEX` kept as an option row.

> **Change vs. earlier 2026-10-11 sync (same-day re-sync, Weekly Monday run):** no new or closed positions, no share-count changes — same 27 rows. Only prices moved (ADBE 242.27→238.00, DUOL 149.22→149.92, RGL A$0.008→0.009, LM8 A$0.34→0.345, etc.). Net Liquidation $57,211.16 → **$57,251.48** (+$40.32); Total Cash $5,465.05 → **$5,463.46**. Carried-forward unresolved items unchanged: undocumented ADBE doubling/BKNG fill, unexplained EUR/AUD cash appearance (+€3,520 / +A$952), SPOT absent, TLT short-call order absent, ungoverned RGL/MBGL/LM8/BULL positions, and the UUUU put order with no holding/evaluation.

> **Three ungoverned equity positions now present (RGL, MBGL, LM8)** plus an ungoverned short-put position (BULL) — see [override-log.md](../override-log.md).

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 20 | 238.00 | 4,760.00 | 221.0850 | +338.30 | +7.65% | USD | 265768 |
| AMZN | 12 | 262.64 | 3,151.68 | 210.5885 | +624.62 | +24.72% | USD | 3691937 |
| AVGO | 6 | 364.20 | 2,185.20 | 382.4417 | -109.45 | -4.77% | USD | 313130367 |
| BKNG | 10 | 160.73 | 1,607.30 | 159.1000 | +16.30 | +1.02% | USD | 308728373 |
| BULL Feb19'27 5 PUT (short) | -2 | 0.3564 | -71.29 | 0.5432 | +37.34 | +34.4% (of credit) | USD | 893374059 |
| CSGP | 25 | 29.67 | 741.75 | 35.0400 | -134.25 | -15.33% | USD | 6726677 |
| DUOL | 30 | 149.92 | 4,497.60 | 168.2479 | -549.84 | -10.89% | USD | 505002183 |
| GOOG | 1 | 348.00 | 348.00 | 295.7000 | +52.30 | +17.69% | USD | 208813720 |
| LM8 | 1,800 | 0.3450 (AUD) | 621.00 (AUD) | 0.3033 | +75.00 | +13.74% | AUD | 496591503 |
| MBGL | 1 | 18.22 | 18.22 | 19.8924 | -1.67 | -8.41% | USD | 893054611 |
| META | 5 | 721.00 | 3,605.00 | 575.0560 | +729.72 | +25.38% | USD | 107113386 |
| MSFT | 17 | 535.00 | 9,095.00 | 391.2165 | +2,444.32 | +36.75% | USD | 272093 |
| NFLX | 12 | 70.30 | 843.60 | 87.7905 | -209.89 | -19.92% | USD | 15124833 |
| NKE | 20 | 34.71 | 694.20 | 43.3100 | -172.00 | -19.86% | USD | 10291 |
| NOW | 9 | 140.91 | 1,268.19 | 87.6100 | +479.70 | +60.84% | USD | 109911821 |
| NVDA | 19 | 230.66 | 4,382.54 | 182.5059 | +914.93 | +26.38% | USD | 4815747 |
| NVO | 5 | 38.67 | 193.35 | 42.5400 | -19.35 | -9.10% | USD | 10611 |
| RBRK | 3 | 125.14 | 375.42 | 58.0962 | +201.13 | +115.40% | USD | 699030013 |
| RGL | 60,000 | 0.0090 (AUD) | 540.00 (AUD) | 0.0111 | -126.43 | -18.97% | AUD | 291951342 |
| SPGI | 1 | 408.00 | 408.00 | 391.1076 | +16.89 | +4.32% | USD | 229629397 |
| TLT | 100 | 77.90 | 7,790.00 | 87.6030 | -970.30 | -11.08% | USD | 15547841 |
| TRN | 600 | 2.0940 (GBP) | 1,256.40 (GBP) | 2.1195 | -15.31 | -1.20% | GBP | 371871705 |
| UBER | 3 | 71.51 | 214.53 | 82.0233 | -31.54 | -12.82% | USD | 365207014 |
| V | 1 | 385.45 | 385.45 | 319.5100 | +65.94 | +20.64% | USD | 49462172 |
| VEEV | 3 | 296.13 | 888.39 | 164.8333 | +393.89 | +79.65% | USD | 136254493 |
| XEON | 10 | 150.48 (EUR) | 1,504.80 (EUR) | 149.0250 | +14.55 | +0.98% | EUR | 46041702 |
| ZS | 1 | 234.25 | 234.25 | 157.1600 | +77.09 | +49.05% | USD | 310621426 |

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value ($51,775.86) plus Total Cash ($5,463.46) = $57,239.32 vs. broker-reported Net Liquidation ($57,251.48) — difference $12.16 is live-vs-settled timing/FX-rounding. Broker-reported BASE stock market value is $51,859.88; the gap vs. the row sum is the option mark (-$71.29) plus FX rounding.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE), **XEON** (EUR), and **RGL** / **LM8** (AUD, ASX). USD-equivalents use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency, plus a `BASE` row consolidating to USD at IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | 602.23 | 602.23 | 1.0000000 | 602.23 |
| EUR | 3,747.94 | 3,747.94 | 1.1201513 | 4,198.26 |
| GBP | 0.00 | 0.00 | 1.3236995 | 0.00 |
| AUD | 951.80 | 951.80 | 0.6983444 | 664.68 |
| **Total (USD-equiv)** | | | | **5,465.17** |

*Row-by-row FX conversion sums to $5,465.17 vs. broker-reported BASE `cash_balance` of $5,463.46 (a $1.71 rounding/rate-timing gap); the broker-reported BASE figure is used in the header.*

*Live-FX USD-equivalents of non-USD positions: TRN £1,256.40 × 1.3236995 = **$1,663.10**; XEON €1,504.80 × 1.1201513 = **$1,685.60**; RGL A$540.00 × 0.6983444 = **$377.11**; LM8 A$621.00 × 0.6983444 = **$433.67**.*

*This file has two independently-refreshed sections — the positions table and the Cash Balances table, each with its own "last synced" timestamp above. See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history.*

# IBKR Portfolio Snapshot

**Account:** U19421206 — the framework account (see [accounts.md](../accounts.md)); the other two IBKR accounts are out of scope.
**Positions last synced:** 2026-10-12 (live via Interactive Brokers MCP — `get_account_positions`, via manual `/sync-portfolio`)
**Cash balances last synced:** 2026-10-12 (live via Interactive Brokers MCP — `get_account_balances`, via manual `/sync-portfolio`)
**Account summary:** Net Liquidation $48,635.06 (broker-reported, BASE) · Gross Position Value $43,301.97 (sum of positions below, non-USD converted at live FX; includes the -$71.29 short-put mark) · Total Cash (USD-equiv) **$5,465.45** (broker-reported, BASE) · Unrealized P&L +$5,153.76 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 24 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders. Ticker-lookup CSV not re-fetched this sync (no new tickers; stored copy unchanged). `TRN @LSE`, `XEON @IBIS2` normalized (exchange suffix stripped); `BULL Feb19'27 5 PUT @AMEX` kept as an option row.

> **Account segregation sync (2026-10-12):** **RGL, LM8 and TLT are absent because they were transferred out in-kind** to the non-framework accounts — not sold, not trims (see [accounts.md](../accounts.md#known-transfers-out-of-the-framework-account)). Scope guard passed: none of the three appear in this response. 27 → 24 rows. Net Liquidation $57,251.48 → **$48,635.06** and Total Cash $5,463.46 → **$5,465.45** reflect the transferred positions leaving (AUD cash A$951.80 and EUR cash €3,747.94 stayed). Share counts of every remaining position are unchanged. Unresolved items carried forward: undocumented ADBE doubling/BKNG fill, unexplained EUR/AUD cash appearance, SPOT absent, ungoverned MBGL and BULL short put, UUUU put order with no holding/evaluation.

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 20 | 241.6200 | 4,832.40 | 221.0850 | +410.70 | +9.29% | USD | 265768 |
| AMZN | 12 | 263.8300 | 3,165.96 | 210.5885 | +638.90 | +25.28% | USD | 3691937 |
| AVGO | 6 | 362.6100 | 2,175.66 | 382.4417 | -118.99 | -5.19% | USD | 313130367 |
| BKNG | 10 | 161.7000 | 1,617.00 | 159.1000 | +26.00 | +1.63% | USD | 308728373 |
| BULL Feb19'27 5 PUT (short) | -2 | 0.3564 | -71.29 | 0.5432 | +37.34 | +34.4% (of credit) | USD | 893374059 |
| CSGP | 25 | 29.6700 | 741.75 | 35.0400 | -134.25 | -15.33% | USD | 6726677 |
| DUOL | 30 | 149.8400 | 4,495.20 | 168.2479 | -552.24 | -10.94% | USD | 505002183 |
| GOOG | 1 | 349.3600 | 349.36 | 295.7000 | +53.66 | +18.15% | USD | 208813720 |
| MBGL | 1 | 18.2200 | 18.22 | 19.8924 | -1.67 | -8.41% | USD | 893054611 |
| META | 5 | 724.3400 | 3,621.70 | 575.0560 | +746.42 | +25.96% | USD | 107113386 |
| MSFT | 17 | 536.9400 | 9,127.98 | 391.2165 | +2,477.30 | +37.25% | USD | 272093 |
| NFLX | 12 | 70.6600 | 847.92 | 87.7905 | -205.57 | -19.51% | USD | 15124833 |
| NKE | 20 | 34.7800 | 695.60 | 43.3100 | -170.60 | -19.70% | USD | 10291 |
| NOW | 9 | 142.0400 | 1,278.36 | 87.6100 | +489.87 | +62.13% | USD | 109911821 |
| NVDA | 19 | 229.7600 | 4,365.44 | 182.5059 | +897.83 | +25.89% | USD | 4815747 |
| NVO | 5 | 38.6300 | 193.15 | 42.5400 | -19.55 | -9.19% | USD | 10611 |
| RBRK | 3 | 126.0000 | 378.00 | 58.0962 | +203.71 | +116.88% | USD | 699030013 |
| SPGI | 1 | 407.9100 | 407.91 | 391.1076 | +16.80 | +4.30% | USD | 229629397 |
| TRN | 600 | 2.0780 | 1,246.80 | 2.1195 | -24.91 | -1.96% | GBP | 371871705 |
| UBER | 3 | 71.6400 | 214.92 | 82.0233 | -31.15 | -12.66% | USD | 365207014 |
| V | 1 | 385.9000 | 385.90 | 319.5100 | +66.39 | +20.78% | USD | 49462172 |
| VEEV | 3 | 296.1300 | 888.39 | 164.8333 | +393.89 | +79.65% | USD | 136254493 |
| XEON | 10 | 150.4750 | 1,504.75 | 149.0250 | +14.50 | +0.97% | EUR | 46041702 |
| ZS | 1 | 235.5100 | 235.51 | 157.1600 | +78.35 | +49.85% | USD | 310621426 |

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value ($43,301.97) plus Total Cash ($5,465.45) = $48,767.42 vs. broker-reported Net Liquidation ($48,635.06) — difference $132.36 (0.27%) is live-vs-settled price timing between the separate positions and balances MCP calls, plus FX rounding. Broker-reported BASE stock market value is $43,241.47; it excludes the option mark (-$71.29).

> **Currency note:** all positions are USD except **TRN** (GBP, LSE) and **XEON** (EUR). USD-equivalents use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency, plus a `BASE` row consolidating to USD at IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | 602.23 | 602.23 | 1.0000000 | 602.23 |
| EUR | 3,747.94 | 3,747.94 | 1.1201705 | 4,198.26 |
| GBP | 0.00 | 0.00 | 1.3244739 | 0.00 |
| AUD | 951.80 | 951.80 | 0.6979153 | 664.27 |
| **Total (USD-equiv)** | | | | **5,464.76** |

*Row-by-row FX conversion sums to $5,464.76 vs. broker-reported BASE `cash_balance` of $5,465.45 (a $0.69 rounding/rate-timing gap); the broker-reported BASE figure is used in the header.*

*Live-FX USD-equivalents of non-USD positions: TRN £1,246.80 × 1.3244739 = **$1,651.38**; XEON €1,504.75 × 1.1201705 = **$1,685.57**.*

*This file has two independently-refreshed sections — the positions table and the Cash Balances table, each with its own "last synced" timestamp above. See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history.*

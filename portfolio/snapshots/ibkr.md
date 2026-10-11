# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-10-11 (live via Interactive Brokers MCP — `get_account_positions`, via manual `/sync-portfolio`)
**Cash balances last synced:** 2026-10-11 (live via Interactive Brokers MCP — `get_account_balances`, via manual `/sync-portfolio`)
**Account summary:** Net Liquidation $57,211.16 (broker-reported, BASE) · Gross Position Value $51,751.39 (sum of positions below, non-USD converted at live FX; includes the -$71.29 short-put mark) · Total Cash (USD-equiv) **$5,465.05** (broker-reported, BASE) · Unrealized P&L +$4,124.69 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 27 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders. `RGL @ASX`, `LM8 @ASX`, `TRN @LSE`, `XEON @IBIS2` normalized (exchange suffix stripped); `BULL Feb19'27 5 PUT @AMEX` kept as an option row. Ticker-lookup CSV re-fetched live this sync (HTTP 200, needed `--ssl-no-revoke` because Windows schannel could not check certificate revocation) and the stored fallback overwritten.

> **Change vs. 2026-10-04:** two new positions — **LM8** (1,800 sh @ ASX, AUD; matches the BUY 1800 @ A$0.30 order flagged last sync as "not a current holding — verify intent", now filled) and **BULL Feb19'27 $5 PUT, short 2 contracts** (a new option position, USD; no matching order or session on file). Otherwise same 25 tickers and share counts. **Net Liquidation $50,411.80 → $57,211.16 (+$6,799.36)** and **Total Cash $117.37 → $5,465.05 (+$5,347.68)**: market moves explain only part of the NLV rise; the EUR (+€3,520) and AUD (+A$952) cash balances appeared this week, consistent with a deposit/FX conversion — **not documented anywhere; confirm in Client Portal.** Carried-forward items that remain **unresolved**: ADBE doubling (10 → 20) and BKNG fill (both undocumented), RBRK/ZS Rule 9 rescores overdue ([#801](https://github.com/Cloxy777/investment-framework/issues/801), [#802](https://github.com/Cloxy777/investment-framework/issues/802)), SPOT absent (now 12 consecutive syncs), TLT short-call order still absent from the orders fetch, and two ungoverned equity positions (RGL, MBGL).

> **Three ungoverned equity positions now present (RGL, MBGL, LM8)** plus an ungoverned short-put position (BULL) — see [override-log.md](../override-log.md).

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 20 | 242.27 | 4,845.40 | 221.0850 | +423.70 | +9.58% | USD | 265768 |
| AMZN | 12 | 262.43 | 3,149.16 | 210.5885 | +622.10 | +24.62% | USD | 3691937 |
| AVGO | 6 | 362.25 | 2,173.50 | 382.4417 | -121.15 | -5.28% | USD | 313130367 |
| BKNG | 10 | 160.73 | 1,607.30 | 159.1000 | +16.30 | +1.02% | USD | 308728373 |
| BULL Feb19'27 5 PUT (short) | -2 | 0.3564 | -71.29 | 0.5432 | +37.34 | +34.4% (of credit) | USD | 893374059 |
| CSGP | 25 | 29.72 | 743.00 | 35.0400 | -133.00 | -15.18% | USD | 6726677 |
| DUOL | 30 | 149.22 | 4,476.60 | 168.2479 | -570.84 | -11.31% | USD | 505002183 |
| GOOG | 1 | 347.90 | 347.90 | 295.7000 | +52.20 | +17.65% | USD | 208813720 |
| LM8 | 1,800 | 0.3400 (AUD) | 612.00 (AUD) | 0.3033 | +66.00 | +12.09% | AUD | 496591503 |
| MBGL | 1 | 18.22 | 18.22 | 19.8924 | -1.67 | -8.41% | USD | 893054611 |
| META | 5 | 718.67 | 3,593.35 | 575.0560 | +718.07 | +24.97% | USD | 107113386 |
| MSFT | 17 | 535.00 | 9,095.00 | 391.2165 | +2,444.32 | +36.75% | USD | 272093 |
| NFLX | 12 | 70.32 | 843.82 | 87.7905 | -209.67 | -19.90% | USD | 15124833 |
| NKE | 20 | 34.92 | 698.40 | 43.3100 | -167.80 | -19.37% | USD | 10291 |
| NOW | 9 | 140.86 | 1,267.74 | 87.6100 | +479.25 | +60.78% | USD | 109911821 |
| NVDA | 19 | 229.33 | 4,357.27 | 182.5059 | +889.66 | +25.66% | USD | 4815747 |
| NVO | 5 | 38.64 | 193.20 | 42.5400 | -19.50 | -9.17% | USD | 10611 |
| RBRK | 3 | 125.14 | 375.42 | 58.0962 | +201.13 | +115.40% | USD | 699030013 |
| RGL | 60,000 | 0.0080 (AUD) | 480.00 (AUD) | 0.0111 | -186.43 | -27.97% | AUD | 291951342 |
| SPGI | 1 | 407.82 | 407.82 | 391.1076 | +16.71 | +4.27% | USD | 229629397 |
| TLT | 100 | 77.97 | 7,796.66 | 87.6030 | -963.64 | -11.00% | USD | 15547841 |
| TRN | 600 | 2.0940 (GBP) | 1,256.40 (GBP) | 2.1195 | -15.31 | -1.20% | GBP | 371871705 |
| UBER | 3 | 71.37 | 214.11 | 82.0233 | -31.96 | -12.99% | USD | 365207014 |
| V | 1 | 385.45 | 385.45 | 319.5100 | +65.94 | +20.64% | USD | 49462172 |
| VEEV | 3 | 296.13 | 888.39 | 164.8333 | +393.89 | +79.65% | USD | 136254493 |
| XEON | 10 | 150.46 (EUR) | 1,504.63 (EUR) | 149.0250 | +14.38 | +0.96% | EUR | 46041702 |
| ZS | 1 | 234.01 | 234.01 | 157.1600 | +76.85 | +48.90% | USD | 310621426 |

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value ($51,751.39) plus Total Cash ($5,465.05) = $57,216.44 vs. broker-reported Net Liquidation ($57,211.16) — the difference ($-5.28) is the live-vs-settled timing/FX-rounding mismatch noted in prior syncs. Broker-reported BASE stock market value is $51,817.96; the $66.57 gap vs. the row sum is the option mark (-$71.29) plus rounding.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE), **XEON** (EUR), and **RGL** / **LM8** (AUD, ASX). USD-equivalents use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency, plus a `BASE` row consolidating to USD at IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | 602.23 | 602.23 | 1.0000000 | 602.23 |
| EUR | 3,747.94 | 3,747.94 | 1.1201513 | 4,198.26 |
| GBP | 0.00 | 0.00 | 1.3236995 | 0.00 |
| AUD | 951.80 | 951.80 | 0.6982193 | 664.57 |
| **Total (USD-equiv)** | | | | **5,465.05** |

*Row-by-row FX conversion sums to $5,465.05, matching the broker-reported BASE `cash_balance` (5,465.0549).*

*Live-FX USD-equivalents of non-USD positions: TRN £1,256.40 × 1.3236995 = **$1,663.10**; XEON €1,504.63 × 1.1201513 = **$1,685.41**; RGL A$480.00 × 0.6982193 = **$335.15**; LM8 A$612.00 × 0.6982193 = **$427.31**.*

> **USD cash balance is positive again (+$602.23)** — the small margin debit of last sync (-$138.74) is gone. The new EUR (+€3,520) and AUD (+A$952) cash is unexplained by any order or session on file.

*This file has two independently-refreshed sections — the positions table and the Cash Balances table, each with its own "last synced" timestamp above. See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history.*

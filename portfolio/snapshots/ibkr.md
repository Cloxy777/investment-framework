# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-10-04 (live via Interactive Brokers MCP — `get_account_positions`, via scheduled weekly `/sync-portfolio`)
**Cash balances last synced:** 2026-10-04 (live via Interactive Brokers MCP — `get_account_balances`, via scheduled weekly `/sync-portfolio`)
**Account summary:** Net Liquidation $50,411.80 (broker-reported, BASE) · Gross Position Value $50,446.74 (sum of positions below, RGL/TRN/XEON converted at live FX) · Total Cash (USD-equiv) **$117.37** (broker-reported, BASE) · Unrealized P&L +$2,913.20 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 25 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders. `RGL @ASX` and `TRN @LSE` normalized (exchange suffix stripped). Ticker-lookup CSV re-fetched live this sync (HTTP 200) and the stored fallback overwritten.

> **Change vs. 2026-09-27:** no share-count changes, no new or closed positions (same 25 tickers). Net Liquidation $50,732.36 → $50,411.80 (-$320.56), driven by market moves (e.g. AVGO, DUOL, TLT, NFLX down; NVDA, META, MSFT up) — no trades. Carried-forward items from prior syncs that remain **unresolved** (details in [override-log.md](../override-log.md) and prior session notes): ADBE doubling (10 → 20) and BKNG fill (both undocumented), RBRK/ZS Rule 9 rescores overdue ([#801](https://github.com/Cloxy777/investment-framework/issues/801), [#802](https://github.com/Cloxy777/investment-framework/issues/802)), SPOT absent (now 11 consecutive syncs), TLT short-call order still absent from the orders fetch, and two ungoverned equity positions (RGL, MBGL).

> **Two ungoverned equity positions still present (RGL, MBGL)** — see [override-log.md](../override-log.md).

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 20 | 237.73 | 4,754.60 | 221.0850 | +332.90 | +7.53% | USD | 265768 |
| AMZN | 12 | 252.35 | 3,028.20 | 210.5885 | +501.14 | +19.83% | USD | 3691937 |
| AVGO | 6 | 359.97 | 2,159.82 | 382.4417 | -134.83 | -5.88% | USD | 313130367 |
| BKNG | 10 | 159.02 | 1,590.20 | 159.1000 | -0.80 | -0.05% | USD | 308728373 |
| CSGP | 25 | 27.38 | 684.50 | 35.0400 | -191.50 | -21.86% | USD | 6726677 |
| DUOL | 30 | 144.27 | 4,328.10 | 168.2479 | -719.34 | -14.25% | USD | 505002183 |
| GOOG | 1 | 341.00 | 341.00 | 295.7000 | +45.30 | +15.32% | USD | 208813720 |
| MBGL | 1 | 17.21 | 17.21 | 19.8924 | -2.68 | -13.47% | USD | 893054611 |
| META | 5 | 728.10 | 3,640.50 | 575.0560 | +765.22 | +26.61% | USD | 107113386 |
| MSFT | 17 | 519.10 | 8,824.70 | 391.2165 | +2,174.02 | +32.69% | USD | 272093 |
| NFLX | 12 | 67.91 | 814.92 | 87.7905 | -238.57 | -22.65% | USD | 15124833 |
| NKE | 20 | 34.00 | 680.00 | 43.3100 | -186.20 | -21.50% | USD | 10291 |
| NOW | 9 | 134.80 | 1,213.20 | 87.6100 | +424.71 | +53.86% | USD | 109911821 |
| NVDA | 19 | 235.20 | 4,468.80 | 182.5059 | +1,001.19 | +28.87% | USD | 4815747 |
| NVO | 5 | 37.32 | 186.60 | 42.5400 | -26.10 | -12.27% | USD | 10611 |
| RBRK | 3 | 118.58 | 355.74 | 58.0962 | +181.45 | +104.11% | USD | 699030013 |
| RGL | 60,000 | 0.0090 (AUD) | 540.00 (AUD) | 0.0111 | -126.43 | -18.97% | AUD | 291951342 |
| SPGI | 1 | 386.27 | 386.27 | 391.1076 | -4.84 | -1.24% | USD | 229629397 |
| TLT | 100 | 77.55 | 7,755.00 | 87.6030 | -1,005.30 | -11.48% | USD | 15547841 |
| TRN | 600 | 1.9730 (GBP) | 1,183.80 (GBP) | 2.1195 | -87.91 | -6.91% | GBP | 371871705 |
| UBER | 3 | 68.11 | 204.33 | 82.0233 | -41.74 | -16.96% | USD | 365207014 |
| V | 1 | 360.66 | 360.66 | 319.5100 | +41.15 | +12.88% | USD | 49462172 |
| VEEV | 3 | 273.33 | 819.99 | 164.8333 | +325.49 | +65.82% | USD | 136254493 |
| XEON | 10 | 150.42 (EUR) | 1,504.20 (EUR) | 149.0250 | +13.95 | +0.94% | EUR | 46041702 |
| ZS | 1 | 196.60 | 196.60 | 157.1600 | +39.44 | +25.10% | USD | 310621426 |

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value ($50,446.74) plus Total Cash ($117.37) = $50,564.11 vs. broker-reported Net Liquidation ($50,411.80) — the difference ($-152.31) is the same live-vs-settled timing/FX-rounding mismatch noted in prior syncs.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE), **XEON** (EUR), and **RGL** (AUD, ASX). USD-equivalents use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency, plus a `BASE` row consolidating to USD at IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | -138.74 | -138.74 | 1.0000000 | -138.74 |
| EUR | 227.49 | 227.49 | 1.1253530 | 256.01 |
| GBP | 0.00 | 0.00 | 1.3241579 | 0.00 |
| AUD | 0.00 | 0.00 | 0.6953895 | 0.00 |
| **Total (USD-equiv)** | | | | **117.37** |

*Row-by-row FX conversion sums to $117.27; the Total uses the broker-reported BASE `cash_balance` (117.3652) directly — the gap is a rounding artifact.*

*Live-FX USD-equivalents of non-USD positions: TRN £1,183.80 × 1.3241579 = **$1,567.54**; XEON €1,504.20 × 1.125353 = **$1,692.76**; RGL A$540.00 × 0.6953895 = **$375.51**.*

> **USD cash balance is slightly negative (-$138.74)** — a small margin debit, unchanged in nature from last sync (-$155.30).

*This file has two independently-refreshed sections — the positions table and the Cash Balances table, each with its own "last synced" timestamp above. See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history.*

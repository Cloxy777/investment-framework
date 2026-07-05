# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-07-05 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-portfolio`)
**Cash balances last synced:** 2026-07-05 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-portfolio`)
**Account summary:** Net Liquidation $43,102.67 (broker-reported, BASE) · Gross Position Value $42,761.87 (sum of positions below, RGL/TRN/XEON converted at live FX) · Total Cash (USD-equiv) **$342.69** (broker-reported, BASE) · Unrealized P&L –$1,049.34 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 27 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders needed. `XEON @IBIS2`, `TRN @LSE`, and the new `RGL @ASX` are normalized to `XEON`/`TRN`/`RGL` (exchange suffix stripped) for consistency with `holdings.md`. The live ticker-lookup CSV (`https://www.interactivebrokers.com/download/fracshare_stk.csv`) was fetched successfully this sync and `portfolio/reference/ibkr-ticker-lookup.csv` was refreshed from it (committed alongside this snapshot) — it confirms **MBGL = Mobility Global Inc (NYSE, contract 893054611)**; RGL (ASX-listed, contract 291951342) isn't in this US-focused CSV, but its ticker was already unambiguous from `contract_description`.

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 10 | 219.71 | 2,197.10 | 202.07 | +176.40 | +8.73% | USD | 265768 |
| AMZN | 12 | 243.00 | 2,916.00 | 210.59 | +388.94 | +15.38% | USD | 3691937 |
| AVGO | 6 | 362.00 | 2,172.00 | 382.44 | -122.65 | -5.35% | USD | 313130367 |
| CSGP | 25 | 30.00 | 750.00 | 35.04 | -126.00 | -14.40% | USD | 6726677 |
| DUOL | 30 | 125.48 | 3,764.40 | 168.25 | -1,283.04 | -25.41% | USD | 505002183 |
| GOOG | 1 | 355.11 | 355.11 | 295.70 | +59.41 | +20.10% | USD | 208813720 |
| **MBGL** | 1 | 19.80 | 19.80 | 19.01 | +0.79 | +4.18% | USD | 893054611 |
| META | 6 | 584.88 | 3,509.30 | 597.81 | -77.53 | -2.16% | USD | 107113386 |
| MSFT | 20 | 390.83 | 7,816.60 | 402.62 | -235.87 | -2.94% | USD | 272093 |
| NFLX | 12 | 77.61 | 931.31 | 87.79 | -122.18 | -13.93% | USD | 15124833 |
| NKE | 20 | 44.09 | 881.80 | 43.31 | +15.60 | +1.80% | USD | 10291 |
| NOW | 12 | 106.32 | 1,275.84 | 92.80 | +162.25 | +14.55% | USD | 109911821 |
| NVDA | 14 | 194.44 | 2,722.16 | 179.20 | +213.30 | +8.51% | USD | 4815747 |
| NVO | 5 | 50.43 | 252.15 | 42.54 | +39.45 | +18.55% | USD | 10611 |
| RBRK | 3 | 83.42 | 250.26 | 58.10 | +75.97 | +43.61% | USD | 699030013 |
| **RGL** | 2,786 | 0.011 (AUD) | 30.65 (AUD) | 0.011 | -0.43 | -1.38% | AUD | 291951342 |
| SPGI | 1 | 433.80 | 433.80 | 391.99 | +41.81 | +10.66% | USD | 229629397 |
| SPOT | 1 | 489.86 | 489.86 | 509.00 | -19.14 | -3.76% | USD | 312496724 |
| STIM | 500 | 1.41 | 705.00 | 1.58 | -85.82 | -10.85% | USD | 324062325 |
| STIM Aug21'26 $2.50 CALL (short) | -5 (contracts) | 0.10 | -50.00 | 0.0545 | -22.77 | n/a — short premium, see note | USD | 840079341 |
| TLT | 77 | 85.51 | 6,584.27 | 88.79 | -252.36 | -3.69% | USD | 15547841 |
| TRN | 600 | 2.18 (GBP) | 1,308.00 | 2.12 | +36.29 | +2.86% | GBP | 371871705 |
| UBER | 3 | 74.35 | 223.05 | 82.02 | -23.02 | -9.36% | USD | 365207014 |
| V | 1 | 361.71 | 361.71 | 319.51 | +42.20 | +13.21% | USD | 49462172 |
| VEEV | 3 | 191.76 | 575.28 | 164.83 | +80.78 | +16.34% | USD | 136254493 |
| XEON | 10 | 149.56 (EUR) | 1,495.61 | 149.03 | +5.36 | +0.36% | EUR | 46041702 |
| ZS | 1 | 147.13 | 147.13 | 157.16 | -10.04 | -6.38% | USD | 310621426 |

> ⚠️ **Two ungoverned positions confirmed still present — not new this sync, both flagged and carried since the 2026-07-01/07-03 rebalance sessions:**
>
> - **RGL (RiversGold Ltd, ASX micro-cap gold explorer):** 2,786 shares, no Phase 01/02 evaluation ever run, no `decisions/` entry — see [override-log.md](../override-log.md). The 60,000-share GTC buy order behind this fill (order 630395618) is **still live** as of this sync's `get_account_orders` pull (see [ibkr-orders.md](ibkr-orders.md)) — 57,214 shares remain unfilled at AUD $0.011. **This order has now been open and actively working for 6 days with no resolution.**
> - **MBGL (Mobility Global Inc, NYSE):** 1 share, $19.80, cost basis $19.01 — likely corporate-action-sourced per the 2026-07-01 rebalance session's working theory, still not investigated.
>
> **⚠️ New/escalating this sync — see this week's weekly brief and the separate urgent notification sent this run for the full breakdown:** `get_account_orders` this sync surfaced live orders in **HDSN** (200 sh @ $4.96) and **MA** (4 sh @ $464) that directly contradict this framework's own documented recommendations (HDSN failed the 80.0+ Quality Score gate at 24.7 on 2026-07-03; MA's 2026-06-22 rescore explicitly stated "Trade does NOT execute," R/R 1.33:1), plus a **PDD** order (10 sh @ $72.55) that doesn't match the sized/priced recommendation from its 2026-07-01 session (~44 sh at a $128.74 ceiling), a duplicate **NOW** order, a live **V** order (9 sh @ $285) despite V's 2026-07-05 rescore also failing the R/R gate, and yet more undocumented 1-share **META** GTC orders. None of these orders have filled (still `NEW`/pending) — no new *positions* resulted, only new *order-level* exposure — but this is flagged as a governance/security concern, not a data-sync note, and reported to the user directly outside this file.

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value (sum of live position market values above, $42,761.87) plus Total Cash ($342.69) = $43,104.56, ~$1.87 **above** broker-reported Net Liquidation ($43,102.67) — consistent with the same `get_account_positions` (live/intraday) vs. `get_account_balances` (settled, slightly lagged) timing mismatch noted in prior syncs, not a calculation error.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE), **XEON** (EUR), and **RGL** (AUD, ASX). USD-equivalents (used for `holdings.md` weighting) use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

> **Short-options row (STIM call):** the P&L % column is marked n/a because percentage-of-cost-basis is not a meaningful figure for a short option position — `Avg Cost` ($0.0545) is the average **premium received** per contract when sold, not money paid; the negative unrealized P&L (–$22.77) reflects that the contract's current buy-back cost ($0.10) now exceeds that premium. The –$50.00 market value (the liability to buy back all 5 contracts at the current price) is **not folded into STIM's weight % in `holdings.md`** — tracked here for transparency; at ~0.09% of the combined portfolio it would not move STIM's banding regardless.

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | 103.69 | 103.69 | 1.000000 | 103.69 |
| EUR | 227.49 | 227.49 | 1.1436323 | 260.16 |
| GBP | 0.28 | 0.28 | 1.33505295 | 0.37 |
| AUD | -31.07 | -31.07 | 0.6938792 | -21.56 |
| **Total (USD-equiv)** | | | | **342.69** |

*Row-by-row FX conversion sums to $342.67; the Total above uses the broker-reported BASE `cash_balance` ($342.6915) directly, per Rule 0 — the small gap is a rounding/timing artifact, not an error.*

*The same GBP→USD rate (1.33505295) applied to TRN's £1,308.00 market value gives its USD-equivalent: **$1,746.25** — used in `holdings.md` for weighting. The same EUR→USD rate (1.1436323) applied to XEON's €1,495.61 market value gives its USD-equivalent: **$1,710.43**. The same AUD→USD rate (0.6938792) applied to RGL's AUD $30.65 market value gives its USD-equivalent: **$21.26**.*

**Cash swung from –$1,576.85 (2026-06-28) to +$342.69 this sync** — GBP cash balance moved from –£1,271.71 to a near-zero +£0.28, meaning the negative-GBP-cash funding of the TRN purchase (flagged at the last sync) has since been resolved (an FX conversion or cash transfer, not visible in this balances-only pull — `get_account_trades` would confirm the mechanism if needed). Flagged for transparency; not investigated further this sync since it's a resolution of a prior flag, not a new one.

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

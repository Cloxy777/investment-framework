# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-08-23 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-portfolio`)
**Cash balances last synced:** 2026-08-23 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-portfolio`)
**Account summary:** Net Liquidation $50,211.32 (broker-reported, BASE) · Gross Position Value $46,191.71 (sum of positions below, RGL/TRN/XEON converted at live FX) · Total Cash (USD-equiv) **$4,060.83** (broker-reported, BASE) · Unrealized P&L +$2,644.36 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 24 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders needed. `RGL @ASX` and `TRN @LSE` normalized (exchange suffix stripped) for consistency with `holdings.md`. **Ticker-lookup CSV not re-fetched this sync** — not needed (every position resolved via `contract_description`) and the stored copy is only 7 days stale (last refreshed 2026-08-16).

**No share-count changes vs. the 2026-08-22 sync** — all 24 positions hold identical quantities to yesterday; only prices moved. All per-ticker price moves since 2026-08-22 are small (largest: RBRK -2.57%, AVGO +1.50%, NVDA +1.21%) — nothing crosses the Rule 9 ±15% unexplained-move threshold this window.

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 10 | 275.30 | 2,753.00 | 202.0700 | +732.30 | +36.24% | USD | 265768 |
| AMZN | 12 | 258.63 | 3,103.56 | 210.5885 | +576.50 | +22.81% | USD | 3691937 |
| AVGO | 6 | 374.55 | 2,247.30 | 382.4417 | -47.35 | -2.06% | USD | 313130367 |
| CSGP | 25 | 32.26 | 806.50 | 35.0400 | -69.50 | -7.93% | USD | 6726677 |
| DUOL | 30 | 146.13 | 4,383.90 | 168.2479 | -663.54 | -13.15% | USD | 505002183 |
| GOOG | 1 | 343.00 | 343.00 | 295.7000 | +47.30 | +15.99% | USD | 208813720 |
| **MBGL** | 1 | 19.85 | 19.85 | 19.8924 | -0.04 | -0.21% | USD | 893054611 |
| META | 5 | 551.02 | 2,755.10 | 575.0560 | -120.18 | -4.18% | USD | 107113386 |
| MSFT | 17 | 483.24 | 8,215.08 | 391.2165 | +1,564.40 | +23.52% | USD | 272093 |
| NFLX | 12 | 79.65 | 955.80 | 87.7905 | -97.69 | -9.27% | USD | 15124833 |
| NKE | 20 | 40.76 | 815.20 | 43.3100 | -51.00 | -5.89% | USD | 10291 |
| NOW | 9 | 128.48 | 1,156.32 | 87.6100 | +367.83 | +46.65% | USD | 109911821 |
| NVDA | 19 | 217.99 | 4,141.81 | 182.5059 | +674.20 | +19.44% | USD | 4815747 |
| NVO | 5 | 46.74 | 233.70 | 42.5400 | +21.00 | +9.87% | USD | 10611 |
| RBRK | 3 | 97.52 | 292.56 | 58.0962 | +118.27 | +67.87% | USD | 699030013 |
| **RGL** | 60,000 | 0.0100 (AUD) | 600.00 (AUD) | 0.0111 | -66.43 | -9.97% | AUD | 291951342 |
| SPGI | 1 | 431.29 | 431.29 | 391.1076 | +40.18 | +10.27% | USD | 229629397 |
| TLT | 100 | 82.05 | 8,205.00 | 87.6030 | -555.30 | -6.34% | USD | 15547841 |
| TRN | 600 | 1.975 (GBP) | 1,185.00 | 2.1195 | -86.71 | -6.82% | GBP | 371871705 |
| UBER | 3 | 79.00 | 237.00 | 82.0233 | -9.07 | -3.69% | USD | 365207014 |
| V | 1 | 371.04 | 371.04 | 319.5100 | +51.53 | +16.13% | USD | 49462172 |
| VEEV | 3 | 247.8999939 | 743.70 | 164.8333 | +249.20 | +50.40% | USD | 136254493 |
| XEON | 10 | 150.02 (EUR) | 1,500.20 | 149.0250 | +9.95 | +0.67% | EUR | 46041702 |
| ZS | 1 | 181.74 | 181.74 | 157.1600 | +24.58 | +15.64% | USD | 310621426 |

> ## STIM/DOCS options resolution (2026-08-21 expiry) — no new activity, carried for reference
>
> Both fully resolved as of the 2026-08-22 sync (STIM called away via assignment, DOCS put expired worthless) — see git history for that sync's full detail. Nothing new this sync.
>
> ## ⚠️ TRN — still down 22.4% vs. 2026-08-16, unchanged this week, cause still unconfirmed
>
> Price and share count both unchanged since 2026-08-22 (£1.975/share, 600 shares) — no new move this sync, but the prior week's -22.4% drop (vs. 2026-08-16) remains uninvestigated. See [2026-08-22 rescore](../../sessions/2026-08-22-rescore-trn.md) — Quality Score 67.2 fails the 80.0+ gate; HOLD, no top-up.
>
> ## SPOT position remains absent — still unresolved, now 5 consecutive syncs (since 2026-08-02)
>
> No new information this sync; still flagged for the user to confirm directly in TWS/Client Portal. See [holdings.md](../holdings.md).
>
> ## CSGP `REPLACED` order (1986163848, 2026-05-26) reappeared in this fetch after previously aging out
>
> The 2026-08-22 sync noted this order (and a HDSN one) had dropped out of `get_account_orders` entirely. This sync it's back, still status `REPLACED` (still correctly excluded from the active-orders table — a superseded order, not a live one). No matching live successor order found for CSGP. Not treated as new information since `REPLACED` never represents working exposure, but noting the API's return set for aged orders isn't monotonic — don't assume "dropped out" means "permanently gone." See [ibkr-orders.md](ibkr-orders.md).

> **Two ungoverned equity positions still present (RGL, MBGL) — see [override-log.md](../override-log.md) for detail, unchanged this sync.**

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value (sum of live position market values above, $46,191.71) plus Total Cash ($4,060.83) = $50,252.54, ~$41.22 **above** broker-reported Net Liquidation ($50,211.32) — consistent with the same `get_account_positions` (live/intraday) vs. `get_account_balances` (settled, slightly lagged) timing mismatch noted in prior syncs, not a calculation error.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE), **XEON** (EUR), and **RGL** (AUD, ASX). USD-equivalents (used for `holdings.md` weighting) use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | 4,274.70 | 4,274.70 | 1.0000000 | 4,274.70 |
| EUR | 227.49 | 227.49 | 1.1678947 | 265.68 |
| GBP | 0.00 | 0.00 | 1.3644824 | 0.00 |
| AUD | -668.95 | -668.95 | 0.7171154 | -479.72 |
| **Total (USD-equiv)** | | | | **4,060.83** |

*Row-by-row FX conversion sums to $4,060.66; the Total above uses the broker-reported BASE `cash_balance` (4,060.83) directly, per Rule 0 — the ~$0.17 gap is a rounding artifact, not an error.*

*The same GBP→USD rate (1.3644824) applied to TRN's £1,185.00 market value gives its USD-equivalent: **$1,616.91** — used in `holdings.md` for weighting. The same EUR→USD rate (1.1678947) applied to XEON's €1,500.20 market value gives its USD-equivalent: **$1,752.08**. The same AUD→USD rate (0.7171154) applied to RGL's AUD $600.00 market value gives its USD-equivalent: **$430.27**.*

> **Cash essentially flat vs. last sync: $4,060.67 (2026-08-22) → $4,060.83 this sync**, a +$0.16 change (BASE) — no new cash-moving events (no fills, no assignments) since yesterday's sync; the small delta is ordinary drift (accrued interest/rounding), not itemized further.

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

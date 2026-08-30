# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-08-30 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-portfolio`)
**Cash balances last synced:** 2026-08-30 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-portfolio`)
**Account summary:** Net Liquidation $51,491.57 (broker-reported, BASE) · Gross Position Value $47,449.94 (sum of positions below, RGL/TRN/XEON converted at live FX) · Total Cash (USD-equiv) **$4,061.27** (broker-reported, BASE) · Unrealized P&L +$3,952.77 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 24 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders needed. `RGL @ASX` and `TRN @LSE` normalized (exchange suffix stripped) for consistency with `holdings.md`. **Ticker-lookup CSV not re-fetched this sync** — not needed (every position resolved via `contract_description`) and the stored copy is 14 days stale (last refreshed 2026-08-16).

**No share-count changes vs. the 2026-08-23 sync** — all 24 positions hold identical quantities to a week ago; only prices moved over this 7-day window. Largest moves: NOW +12.07%, VEEV +11.62%, MSFT +6.56%, ADBE +5.90%, META +4.90%, RBRK -4.58%. **Nothing crosses the Rule 9 ±15% unexplained-move threshold** — NOW and VEEV are the ones to watch if this trend continues, but neither triggers a mandatory re-score on price alone this sync.

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 10 | 291.52 | 2,915.20 | 202.0700 | +894.50 | +44.27% | USD | 265768 |
| AMZN | 12 | 266.10 | 3,193.20 | 210.5885 | +666.14 | +26.32% | USD | 3691937 |
| AVGO | 6 | 369.48 | 2,216.88 | 382.4417 | -77.77 | -3.40% | USD | 313130367 |
| CSGP | 25 | 32.22 | 805.50 | 35.0400 | -70.50 | -8.04% | USD | 6726677 |
| DUOL | 30 | 146.98 | 4,409.40 | 168.2479 | -638.04 | -12.65% | USD | 505002183 |
| GOOG | 1 | 342.49 | 342.49 | 295.7000 | +46.79 | +15.82% | USD | 208813720 |
| **MBGL** | 1 | 20.24 | 20.24 | 19.8924 | +0.35 | +1.75% | USD | 893054611 |
| META | 5 | 578.02 | 2,890.10 | 575.0560 | +14.82 | +0.51% | USD | 107113386 |
| MSFT | 17 | 514.94 | 8,753.98 | 391.2165 | +2,103.30 | +26.98% | USD | 272093 |
| NFLX | 12 | 81.00 | 972.00 | 87.7905 | -81.49 | -7.73% | USD | 15124833 |
| NKE | 20 | 39.60 | 792.00 | 43.3100 | -74.20 | -8.57% | USD | 10291 |
| NOW | 9 | 143.99 | 1,295.91 | 87.6100 | +507.42 | +64.36% | USD | 109911821 |
| NVDA | 19 | 218.20 | 4,145.80 | 182.5059 | +678.19 | +19.55% | USD | 4815747 |
| NVO | 5 | 45.61 | 228.05 | 42.5400 | +15.35 | +7.19% | USD | 10611 |
| RBRK | 3 | 93.05 | 279.15 | 58.0962 | +104.86 | +60.34% | USD | 699030013 |
| **RGL** | 60,000 | 0.0110 (AUD) | 660.00 (AUD) | 0.0111 | -6.43 | -0.97% | AUD | 291951342 |
| SPGI | 1 | 442.89 | 442.89 | 391.1076 | +51.78 | +13.24% | USD | 229629397 |
| TLT | 100 | 82.88 | 8,288.00 | 87.6030 | -472.30 | -5.39% | USD | 15547841 |
| TRN | 600 | 1.991 (GBP) | 1,194.60 | 2.1195 | -77.11 | -6.06% | GBP | 371871705 |
| UBER | 3 | 78.20 | 234.60 | 82.0233 | -11.47 | -4.66% | USD | 365207014 |
| V | 1 | 381.60 | 381.60 | 319.5100 | +62.09 | +19.43% | USD | 49462172 |
| VEEV | 3 | 276.69 | 830.07 | 164.8333 | +335.57 | +67.85% | USD | 136254493 |
| XEON | 10 | 150.06 (EUR) | 1,500.60 | 149.0250 | +10.35 | +0.69% | EUR | 46041702 |
| ZS | 1 | 184.50 | 184.50 | 157.1600 | +27.34 | +17.40% | USD | 310621426 |

> ## STIM/DOCS options resolution (2026-08-21 expiry) — no new activity, carried for reference
>
> Both fully resolved as of the 2026-08-22 sync (STIM called away via assignment, DOCS put expired worthless) — see git history for that sync's full detail. Nothing new this sync.
>
> ## ⚠️ TRN — still down vs. the 08-16 drop, cause still unconfirmed; price ticked up slightly this week
>
> £1.975 → £1.991/share (+0.81%) this week, share count unchanged at 600 — the prior week's -22.4% drop (vs. 2026-08-16) remains uninvestigated and this small bounce doesn't change that. See [2026-08-22 rescore](../../sessions/2026-08-22-rescore-trn.md) — Quality Score 67.2 fails the 80.0+ gate; HOLD, no top-up.
>
> ## SPOT position remains absent — still unresolved, now 6 consecutive syncs (since 2026-08-02)
>
> No new information this sync; still flagged for the user to confirm directly in TWS/Client Portal. See [holdings.md](../holdings.md).
>
> ## CSGP `REPLACED` order (1986163848, 2026-05-26) — still present, still excluded
>
> Still status `REPLACED` this sync (correctly excluded from the active-orders table — a superseded order, not a live one). No matching live successor order found for CSGP. See [ibkr-orders.md](ibkr-orders.md).
>
> ## ⚠️ New order this sync: BKNG BUY 10 @ $159.00 LIMIT GTC (order 483688084, placed 2026-08-24)
>
> Not present in the 2026-08-23 sync — first appearance this week. No corresponding `sessions/` or `decisions/` entry exists for this order. Notably, it sits almost exactly at the **$159.94 ad hoc re-check trigger** flagged in BKNG's only prior evaluation ([watchlist/not-in-portfolio/BKNG/BKNG-2026-08-05.md](../../watchlist/not-in-portfolio/BKNG/BKNG-2026-08-05.md)) — the price at which 2:1 Risk/Reward would mechanically clear and flip the recommendation from "watchlist only" to "set limit order." Whether this order was placed deliberately at that level or is otherwise unauthorized/undocumented, per Rule 10 it needs a `sessions/` or `decisions/` entry (or cancellation) — flagged for the user, not resolved by this sync. See [ibkr-orders.md](ibkr-orders.md).

> **Two ungoverned equity positions still present (RGL, MBGL) — see [override-log.md](../override-log.md) for detail, unchanged this sync.**

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value (sum of live position market values above, $47,449.94) plus Total Cash ($4,061.27) = $51,511.21, ~$19.64 **above** broker-reported Net Liquidation ($51,491.57) — consistent with the same `get_account_positions` (live/intraday) vs. `get_account_balances` (settled, slightly lagged) timing mismatch noted in prior syncs, not a calculation error.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE), **XEON** (EUR), and **RGL** (AUD, ASX). USD-equivalents (used for `holdings.md` weighting) use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | 4,276.74 | 4,276.74 | 1.0000000 | 4,276.74 |
| EUR | 227.49 | 227.49 | 1.1584620 | 263.54 |
| GBP | 0.00 | 0.00 | 1.3535939 | 0.00 |
| AUD | -668.95 | -668.95 | 0.7166480 | -479.40 |
| **Total (USD-equiv)** | | | | **4,061.27** |

*Row-by-row FX conversion sums to $4,060.88; the Total above uses the broker-reported BASE `cash_balance` (4,061.27) directly, per Rule 0 — the ~$0.39 gap is a rounding artifact, not an error.*

*The same GBP→USD rate (1.3535939) applied to TRN's £1,194.60 market value gives its USD-equivalent: **$1,617.00** — used in `holdings.md` for weighting. The same EUR→USD rate (1.1584620) applied to XEON's €1,500.60 market value gives its USD-equivalent: **$1,738.39**. The same AUD→USD rate (0.7166480) applied to RGL's AUD $660.00 market value gives its USD-equivalent: **$472.99**.*

> **Cash essentially flat vs. last sync: $4,060.83 (2026-08-23) → $4,061.27 this sync**, a +$0.44 change (BASE) over the 7-day window — no new cash-moving events (no fills, no assignments); the small delta is ordinary drift (accrued interest/rounding), not itemized further. **The still-unresolved +$2,523.36 cash jump flagged 2026-08-09 remains open and uninvestigated.**

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

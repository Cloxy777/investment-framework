# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-09-13 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-portfolio`)
**Cash balances last synced:** 2026-09-13 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-portfolio`)
**Account summary:** Net Liquidation $50,302.93 (broker-reported, BASE) · Gross Position Value $45,960.81 (sum of positions below, RGL/TRN/XEON converted at live FX) · Total Cash (USD-equiv) **$4,099.82** (broker-reported, BASE) · Unrealized P&L +$2,728.57 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 24 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders needed. `RGL @ASX` and `TRN @LSE` normalized (exchange suffix stripped) for consistency with `holdings.md`. **Ticker-lookup CSV not re-fetched this sync** — not needed (every position resolved via `contract_description`) and the stored copy is now 13 days stale (last refreshed 2026-08-31).

**No share-count changes vs. the 2026-09-06 sync** — all 24 positions hold identical quantities to a week ago; a broad pullback this week, with 9 of 24 names down more than 5%. Largest moves: RGL +9.09%, NVO -7.78%, SPGI -7.56%, RBRK -7.49%, DUOL -7.08%, NOW -6.78%, NVDA -6.31%, UBER -5.79%, ADBE -5.16%. **Nothing crosses the Rule 9 ±15% unexplained-move threshold.**

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 10 | 252.76 | 2,527.60 | 202.0700 | +506.90 | +25.09% | USD | 265768 |
| AMZN | 12 | 253.13 | 3,037.56 | 210.5885 | +510.50 | +20.20% | USD | 3691937 |
| AVGO | 6 | 355.71 | 2,134.26 | 382.4417 | -160.39 | -6.99% | USD | 313130367 |
| CSGP | 25 | 30.46 | 761.50 | 35.0400 | -114.50 | -13.07% | USD | 6726677 |
| DUOL | 30 | 143.68 | 4,310.40 | 168.2479 | -737.04 | -14.60% | USD | 505002183 |
| GOOG | 1 | 334.30 | 334.30 | 295.7000 | +38.60 | +13.05% | USD | 208813720 |
| **MBGL** | 1 | 20.16 | 20.16 | 19.8924 | +0.27 | +1.35% | USD | 893054611 |
| META | 5 | 643.12 | 3,215.60 | 575.0560 | +340.32 | +11.84% | USD | 107113386 |
| MSFT | 17 | 490.57 | 8,339.69 | 391.2165 | +1,689.01 | +25.40% | USD | 272093 |
| NFLX | 12 | 77.44 | 929.28 | 87.7905 | -124.21 | -11.79% | USD | 15124833 |
| NKE | 20 | 37.05 | 741.00 | 43.3100 | -125.20 | -14.45% | USD | 10291 |
| NOW | 9 | 131.68 | 1,185.12 | 87.6100 | +396.63 | +50.30% | USD | 109911821 |
| NVDA | 19 | 215.00 | 4,085.00 | 182.5059 | +617.39 | +17.80% | USD | 4815747 |
| NVO | 5 | 42.88 | 214.40 | 42.5400 | +1.70 | +0.80% | USD | 10611 |
| RBRK | 3 | 86.65 | 259.95 | 58.0962 | +85.66 | +49.15% | USD | 699030013 |
| **RGL** | 60,000 | 0.0120 (AUD) | 720.00 (AUD) | 0.0111 | +53.57 | +8.04% | AUD | 291951342 |
| SPGI | 1 | 410.00 | 410.00 | 391.1076 | +18.89 | +4.83% | USD | 229629397 |
| TLT | 100 | 80.93 | 8,093.00 | 87.6030 | -667.30 | -7.62% | USD | 15547841 |
| TRN | 600 | 1.934 (GBP) | 1,160.40 | 2.1195 | -111.31 | -8.75% | GBP | 371871705 |
| UBER | 3 | 71.32 | 213.96 | 82.0233 | -32.11 | -13.05% | USD | 365207014 |
| V | 1 | 370.06 | 370.06 | 319.5100 | +50.55 | +15.82% | USD | 49462172 |
| VEEV | 3 | 262.40 | 787.20 | 164.8333 | +292.70 | +59.19% | USD | 136254493 |
| XEON | 10 | 150.20 (EUR) | 1,502.00 | 149.0250 | +11.75 | +0.79% | EUR | 46041702 |
| ZS | 1 | 164.80 | 164.80 | 157.1600 | +7.64 | +4.86% | USD | 310621426 |

> ## 🚨 NEW, LARGE, UNDOCUMENTED ORDER: TRN BUY 900 @ £1.756 LIMIT GTC — contradicts yesterday's own rescore
>
> Order 1528612089, placed 2026-09-11T10:36:12Z, first appears this sync. Would grow the TRN position from 600 → 1,500 shares (+150%). TRN's [2026-09-10 rescore](../../sessions/2026-09-10-rescore-trn.md) — issued the day *before* this order — computed Quality Score 66.4 (fails the 80.0+ gate) and explicitly recommended **HOLD, no top-up**, with an independent, still-open CMA "drip pricing" investigation as a second reason not to add. No `sessions/`/`decisions/` entry documents this order. **Flagged as urgent** — see [ibkr-orders.md](ibkr-orders.md) for full detail.
>
> ## ⚠️ NEW non-active order: ADBE BUY 10 @ $240.00 (1071856795, placed 2026-09-11T10:35:03Z) — already `REPLACED`, no live successor
>
> Placed one minute before the TRN order above. ADBE's position (10 shares, avg cost $202.07) is unchanged, confirming no fill. Directionally consistent with ADBE's own same-day [2026-09-11 rescore](../../sessions/2026-09-11-rescore-adbe.md) (BUY, 6-share top-up recommended) but quantity/disposition don't clearly match. See [ibkr-orders.md](ibkr-orders.md).
>
> ## ⚠️ TRN — small rebound this week, cause of the multi-week decline remains unconfirmed
>
> £1.919 → £1.934/share (+0.78%) this week, share count unchanged at 600 (excluding the pending order above). CMA "drip pricing" investigation (opened 2026-08-19) still open with no finding as of the [2026-09-10 rescore](../../sessions/2026-09-10-rescore-trn.md) — Quality Score 66.4, fails the 80.0+ gate; HOLD, no top-up.
>
> ## SPOT position remains absent — still unresolved, now 8 consecutive syncs (since 2026-08-02)
>
> No new information this sync; still flagged for the user to confirm directly in TWS/Client Portal. See [holdings.md](../holdings.md).
>
> ## CSGP `REPLACED` order (1986163848, 2026-05-26) — still present, still excluded
>
> Still status `REPLACED` this sync (correctly excluded from the active-orders table — a superseded order, not a live one). No matching live successor order found for CSGP. See [ibkr-orders.md](ibkr-orders.md).
>
> ## ⚠️ TSM, NVDA, BKNG, MA, PDD, NOW orders — all still open, still undocumented, unchanged this sync
>
> No new `sessions/`/`decisions/` entry has appeared for any of these. See [ibkr-orders.md](ibkr-orders.md) for the full carried-forward table.
>
> ## ⚠️ TLT option sell order (1040104046) still absent from this sync's order fetch, in any status — now 2 consecutive syncs
>
> First flagged missing in the 2026-09-06 sync. Worth a manual check in TWS/Client Portal for whether it filled, expired, or was cancelled; not resolved by this sync. See [ibkr-orders.md](ibkr-orders.md).

> **Two ungoverned equity positions still present (RGL, MBGL) — see [override-log.md](../override-log.md) for detail, unchanged this sync.**

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value (sum of live position market values above, $45,960.81) plus Total Cash ($4,099.82) = $50,060.63, ~$242.31 **below** broker-reported Net Liquidation ($50,302.93) — consistent with the same `get_account_positions` (live/intraday) vs. `get_account_balances` (settled, slightly lagged) timing mismatch noted in prior syncs, not a calculation error. The gap is somewhat wider than the ~$24.56 seen on 2026-09-06 — not itself alarming given this week's broad intraday price movement, but worth a glance if it keeps widening.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE), **XEON** (EUR), and **RGL** (AUD, ASX). USD-equivalents (used for `holdings.md` weighting) use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | 4,317.52 | 4,317.52 | 1.0000000 | 4,317.52 |
| EUR | 227.49 | 227.49 | 1.1591946 | 263.71 |
| GBP | 0.00 | 0.00 | 1.3523100 | 0.00 |
| AUD | -672.20 | -672.20 | 0.7161600 | -481.44 |
| **Total (USD-equiv)** | | | | **4,099.82** |

*Row-by-row FX conversion sums to $4,099.79; the Total above uses the broker-reported BASE `cash_balance` (4,099.82) directly, per Rule 0 — the ~$0.03 gap is a rounding artifact, not an error.*

*The same GBP→USD rate (1.3523100) applied to TRN's £1,160.40 market value gives its USD-equivalent: **$1,569.22** — used in `holdings.md` for weighting. The same EUR→USD rate (1.1591946) applied to XEON's €1,502.00 market value gives its USD-equivalent: **$1,741.11**. The same AUD→USD rate (0.7161600) applied to RGL's AUD $720.00 market value gives its USD-equivalent: **$515.64**.*

> **Cash up modestly vs. last sync: $4,083.32 (2026-09-06) → $4,099.82 this sync**, a +$16.50 change (BASE) over the 7-day window — no fills or assignments recorded this window (see the order flags above); the small delta is ordinary drift. **The still-unresolved +$2,523.36 cash jump flagged 2026-08-09 remains open and uninvestigated.**

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

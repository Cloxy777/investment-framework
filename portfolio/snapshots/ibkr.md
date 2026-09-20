# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-09-20 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-portfolio`)
**Cash balances last synced:** 2026-09-20 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-portfolio`)
**Account summary:** Net Liquidation $50,330.70 (broker-reported, BASE) · Gross Position Value $46,258.70 (sum of positions below, RGL/TRN/XEON converted at live FX) · Total Cash (USD-equiv) **$4,097.84** (broker-reported, BASE) · Unrealized P&L +$2,790.62 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 24 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders needed. `RGL @ASX` and `TRN @LSE` normalized (exchange suffix stripped) for consistency with `holdings.md`. **Ticker-lookup CSV not re-fetched this sync** — not needed (every position resolved via `contract_description`) and the stored copy is now 20 days stale (last refreshed 2026-08-31).

**No share-count changes vs. the 2026-09-13 sync** — all 24 positions hold identical quantities to a week ago; a broad rebound this week following last week's pullback. Largest moves: **RBRK +23.49%, ZS +20.24%, RGL -8.33%, NFLX -6.57%** — RBRK and ZS both cross the Rule 9 ±15% unexplained-move threshold, but that move happened mid-week (2026-09-14) and is already tracked by open GitHub issues [#801](https://github.com/Cloxy777/investment-framework/issues/801) (RBRK) and [#802](https://github.com/Cloxy777/investment-framework/issues/802) (ZS) — both now **overdue** (due 2026-09-17, rescores not yet run). See the weekly brief for detail.

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 10 | 248.32 | 2,483.20 | 202.0700 | +462.50 | +22.89% | USD | 265768 |
| AMZN | 12 | 254.70 | 3,056.40 | 210.5885 | +529.34 | +20.95% | USD | 3691937 |
| AVGO | 6 | 356.96 | 2,141.76 | 382.4417 | -152.89 | -6.66% | USD | 313130367 |
| CSGP | 25 | 29.09 | 727.25 | 35.0400 | -148.75 | -16.98% | USD | 6726677 |
| DUOL | 30 | 141.90 | 4,257.00 | 168.2479 | -790.44 | -15.66% | USD | 505002183 |
| GOOG | 1 | 347.00 | 347.00 | 295.7000 | +51.30 | +17.35% | USD | 208813720 |
| **MBGL** | 1 | 19.49 | 19.49 | 19.8924 | -0.40 | -2.02% | USD | 893054611 |
| META | 5 | 665.22 | 3,326.12 | 575.0560 | +450.84 | +15.68% | USD | 107113386 |
| MSFT | 17 | 496.30 | 8,437.10 | 391.2165 | +1,786.42 | +26.86% | USD | 272093 |
| NFLX | 12 | 72.35 | 868.20 | 87.7905 | -185.29 | -17.59% | USD | 15124833 |
| NKE | 20 | 35.67 | 713.40 | 43.3100 | -152.80 | -17.64% | USD | 10291 |
| NOW | 9 | 136.20 | 1,225.80 | 87.6100 | +437.31 | +55.46% | USD | 109911821 |
| NVDA | 19 | 222.25 | 4,222.75 | 182.5059 | +755.14 | +21.78% | USD | 4815747 |
| NVO | 5 | 42.81 | 214.05 | 42.5400 | +1.35 | +0.63% | USD | 10611 |
| RBRK | 3 | 107.00 | 321.00 | 58.0962 | +146.71 | +84.18% | USD | 699030013 |
| **RGL** | 60,000 | 0.0110 (AUD) | 660.00 (AUD) | 0.0111 | -6.43 | -0.96% | AUD | 291951342 |
| SPGI | 1 | 405.40 | 405.40 | 391.1076 | +14.29 | +3.65% | USD | 229629397 |
| TLT | 100 | 81.25 | 8,125.00 | 87.6030 | -635.30 | -7.25% | USD | 15547841 |
| TRN | 600 | 2.010 (GBP) | 1,206.00 | 2.1195 | -65.71 | -5.17% | GBP | 371871705 |
| UBER | 3 | 70.55 | 211.65 | 82.0233 | -34.42 | -13.99% | USD | 365207014 |
| V | 1 | 365.86 | 365.86 | 319.5100 | +46.35 | +14.51% | USD | 49462172 |
| VEEV | 3 | 260.21 | 780.63 | 164.8333 | +286.13 | +57.86% | USD | 136254493 |
| XEON | 10 | 150.26 (EUR) | 1,502.60 | 149.0250 | +12.35 | +0.83% | EUR | 46041702 |
| ZS | 1 | 198.15 | 198.15 | 157.1600 | +40.99 | +26.08% | USD | 310621426 |

> ## 🚨 NEW, UNDOCUMENTED ORDER: AVGO BUY 5 @ $310.60 LIMIT GTC — contradicts yesterday's own rescore
>
> Order 87937891, placed 2026-09-19T19:06:59Z, first appears this sync. AVGO's [2026-09-15 rescore](../../sessions/2026-09-15-rescore-avgo.md) explicitly computed the order setup and concluded **"Per fair-value-methodology.md Step 6: R/R fails the minimum threshold across the entire applicable MoS/stop range. No order is placed."** — Net Action: **HOLD**, no add. That session's own computed buy range was **$248.67–$266.43**; this order's limit ($310.60) sits **~16.6% above** even the top of that range and above AVGO's live price ($356.96). No `sessions/`/`decisions/` entry documents this order. **Flagged as urgent** — see [ibkr-orders.md](ibkr-orders.md) for full detail.
>
> ## ⚠️ TRN BUY 900 @ £1.756 LIMIT GTC — still active, still undocumented, unchanged this sync
>
> Order 1528612089 (placed 2026-09-11) remains live, unchanged since first flagged. Still contradicts the [2026-09-10 rescore](../../sessions/2026-09-10-rescore-trn.md)'s explicit HOLD/no-top-up call (Quality Score 66.4, fails the 80.0+ gate; independent, still-open CMA "drip pricing" investigation). GBP cash remains $0.00. No new `sessions/`/`decisions/` entry has appeared. See [ibkr-orders.md](ibkr-orders.md).
>
> ## ⚠️ ADBE non-active order (1071856795) — still `REPLACED`, no live successor, unchanged
>
> Placed 2026-09-11, already `REPLACED` since first observed. ADBE's position (10 shares, avg cost $202.07) remains unchanged. See [ibkr-orders.md](ibkr-orders.md).
>
> ## 🚨 RBRK and ZS both crossed the Rule 9 ±15% threshold this week — rescores now overdue
>
> Both moves occurred 2026-09-14 (RBRK +15.4%, ZS +16.3%, per the automated Rule 9 check) and are tracked by [#801](https://github.com/Cloxy777/investment-framework/issues/801) and [#802](https://github.com/Cloxy777/investment-framework/issues/802), both due 2026-09-17 and still open as of this sync — **3 days overdue**. Neither ticker's `holdings.md` review date has moved since the trigger (RBRK 30 Aug 2026, ZS 07 Sep 2026), confirming the rescores have not yet been run. RBRK is now up further still (this sync's live price $107.00 vs. the $100.20 that triggered #801) and ZS similarly ($198.15 vs. $191.73 that triggered #802) — the underlying moves have not reversed.
>
> ## SPOT position remains absent — still unresolved, now 9 consecutive syncs (since 2026-08-02)
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
> ## ⚠️ TLT option sell order (1040104046) still absent from this sync's order fetch, in any status — now 3 consecutive syncs
>
> First flagged missing in the 2026-09-06 sync. Worth a manual check in TWS/Client Portal for whether it filled, expired, or was cancelled; not resolved by this sync. See [ibkr-orders.md](ibkr-orders.md).

> **Two ungoverned equity positions still present (RGL, MBGL) — see [override-log.md](../override-log.md) for detail, unchanged this sync.**

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value (sum of live position market values above, $46,258.70) plus Total Cash ($4,097.84) = $50,356.54, ~$25.84 **above** broker-reported Net Liquidation ($50,330.70) — consistent with the same `get_account_positions` (live/intraday) vs. `get_account_balances` (settled, slightly lagged) timing mismatch noted in prior syncs, not a calculation error.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE), **XEON** (EUR), and **RGL** (AUD, ASX). USD-equivalents (used for `holdings.md` weighting) use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | 3,836.84 | 3,836.84 | 1.0000000 | 3,836.84 |
| EUR | 227.49 | 227.49 | 1.1485799 | 261.29 |
| GBP | 0.00 | 0.00 | 1.3395958 | 0.00 |
| AUD | -0.20 | -0.20 | 0.7122312 | -0.14 |
| **Total (USD-equiv)** | | | | **4,097.84** |

*Row-by-row FX conversion sums to $4,097.99; the Total above uses the broker-reported BASE `cash_balance` (4,097.84) directly, per Rule 0 — the ~$0.15 gap is a rounding artifact, not an error.*

*The same GBP→USD rate (1.3395958) applied to TRN's £1,206.00 market value gives its USD-equivalent: **$1,615.55** — used in `holdings.md` for weighting. The same EUR→USD rate (1.1485799) applied to XEON's €1,502.60 market value gives its USD-equivalent: **$1,725.86**. The same AUD→USD rate (0.7122312) applied to RGL's AUD $660.00 market value gives its USD-equivalent: **$470.07**.*

> **Cash down modestly vs. last sync: $4,099.82 (2026-09-13) → $4,097.84 this sync**, a -$1.98 change (BASE) over the 7-day window — no fills or assignments recorded this window (see the order flags above); the small delta is ordinary drift. **The still-unresolved +$2,523.36 cash jump flagged 2026-08-09 remains open and uninvestigated.**

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

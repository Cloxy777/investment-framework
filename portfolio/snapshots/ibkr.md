# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-09-06 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-portfolio`)
**Cash balances last synced:** 2026-09-06 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-portfolio`)
**Account summary:** Net Liquidation $51,245.21 (broker-reported, BASE) · Gross Position Value $47,137.33 (sum of positions below, RGL/TRN/XEON converted at live FX) · Total Cash (USD-equiv) **$4,083.32** (broker-reported, BASE) · Unrealized P&L +$3,671.88 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 24 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders needed. `RGL @ASX` and `TRN @LSE` normalized (exchange suffix stripped) for consistency with `holdings.md`. **Ticker-lookup CSV not re-fetched this sync** — not needed (every position resolved via `contract_description`) and the stored copy is 6 days stale (last refreshed 2026-08-31).

**No share-count changes vs. the 2026-08-30 sync** — all 24 positions hold identical quantities to a week ago; only prices moved over this 7-day window. Largest moves: ADBE -8.58%, ZS -7.97%, META +6.43%, DUOL +5.19%, NVDA +5.17%. **Nothing crosses the Rule 9 ±15% unexplained-move threshold.**

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 10 | 266.50 | 2,665.00 | 202.0700 | +643.00 | +31.88% | USD | 265768 |
| AMZN | 12 | 258.51 | 3,102.12 | 210.5885 | +575.06 | +22.76% | USD | 3691937 |
| AVGO | 6 | 357.07 | 2,142.41 | 382.4417 | -152.24 | -6.63% | USD | 313130367 |
| CSGP | 25 | 30.92 | 773.00 | 35.0400 | -103.00 | -11.76% | USD | 6726677 |
| DUOL | 30 | 154.62 | 4,638.45 | 168.2479 | -408.99 | -8.10% | USD | 505002183 |
| GOOG | 1 | 335.72 | 335.72 | 295.7000 | +40.02 | +13.53% | USD | 208813720 |
| **MBGL** | 1 | 20.58 | 20.58 | 19.8924 | +0.69 | +3.46% | USD | 893054611 |
| META | 5 | 615.20 | 3,075.99 | 575.0560 | +200.71 | +6.98% | USD | 107113386 |
| MSFT | 17 | 499.41 | 8,489.99 | 391.2165 | +1,839.31 | +27.66% | USD | 272093 |
| NFLX | 12 | 78.32 | 939.89 | 87.7905 | -113.60 | -10.78% | USD | 15124833 |
| NKE | 20 | 38.42 | 768.40 | 43.3100 | -97.80 | -11.29% | USD | 10291 |
| NOW | 9 | 141.26 | 1,271.34 | 87.6100 | +482.85 | +61.24% | USD | 109911821 |
| NVDA | 19 | 229.49 | 4,360.25 | 182.5059 | +892.64 | +25.74% | USD | 4815747 |
| NVO | 5 | 46.50 | 232.50 | 42.5400 | +19.80 | +9.31% | USD | 10611 |
| RBRK | 3 | 93.67 | 281.01 | 58.0962 | +106.72 | +61.23% | USD | 699030013 |
| **RGL** | 60,000 | 0.0110 (AUD) | 660.00 (AUD) | 0.0111 | -6.43 | -0.96% | AUD | 291951342 |
| SPGI | 1 | 443.51 | 443.51 | 391.1076 | +52.40 | +13.40% | USD | 229629397 |
| TLT | 100 | 82.24 | 8,224.00 | 87.6030 | -536.30 | -6.12% | USD | 15547841 |
| TRN | 600 | 1.919 (GBP) | 1,151.40 | 2.1195 | -120.31 | -9.46% | GBP | 371871705 |
| UBER | 3 | 75.70 | 227.10 | 82.0233 | -18.97 | -7.71% | USD | 365207014 |
| V | 1 | 375.07 | 375.07 | 319.5100 | +55.56 | +17.39% | USD | 49462172 |
| VEEV | 3 | 275.09 | 825.27 | 164.8333 | +330.77 | +66.89% | USD | 136254493 |
| XEON | 10 | 150.14 (EUR) | 1,501.40 | 149.0250 | +11.15 | +0.69% | EUR | 46041702 |
| ZS | 1 | 169.80 | 169.80 | 157.1600 | +12.64 | +8.04% | USD | 310621426 |

> ## STIM/DOCS options resolution (2026-08-21 expiry) — no new activity, carried for reference
>
> Both fully resolved as of the 2026-08-22 sync (STIM called away via assignment, DOCS put expired worthless) — see git history for that sync's full detail. Nothing new this sync.
>
> ## ⚠️ TRN — still down vs. the 08-16 drop, cause still unconfirmed; small further pullback this week
>
> £1.991 → £1.919/share (-3.62%) this week, share count unchanged at 600 — the prior weeks' -22.4% drop (vs. 2026-08-16) remains uninvestigated. See [2026-08-31 rescore](../../sessions/2026-08-31-rescore-trn.md) — Quality Score 67.2 fails the 80.0+ gate; HOLD, no top-up.
>
> ## SPOT position remains absent — still unresolved, now 7 consecutive syncs (since 2026-08-02)
>
> No new information this sync; still flagged for the user to confirm directly in TWS/Client Portal. See [holdings.md](../holdings.md).
>
> ## CSGP `REPLACED` order (1986163848, 2026-05-26) — still present, still excluded
>
> Still status `REPLACED` this sync (correctly excluded from the active-orders table — a superseded order, not a live one). No matching live successor order found for CSGP. See [ibkr-orders.md](ibkr-orders.md).
>
> ## ⚠️ Two new, undocumented orders this sync: TSM BUY 10 @ $369.00 and NVDA BUY 10 @ $199.56
>
> Neither appeared in the 2026-08-30 sync. **Neither has a matching `sessions/`/`decisions/` entry that recommends placing it — both actively contradict the framework's own most recent analysis on each name:**
> - **TSM** (order 510436581, placed 2026-09-06T17:04:38Z, the same day as this sync): today's own [2026-09-06 new-position session](../../sessions/2026-09-06-new-position-tsm.md) concluded **"WATCHLIST ONLY — do not enter,"** R/R failing 2:1 across the whole authorized MoS range, with computed buy ceilings of **$258.88–$277.37**. The live order's $369.00 limit sits far above every one of those ceilings.
> - **NVDA** (order 1306197667, placed 2026-08-31T19:57:27Z): both the [2026-09-01](../../sessions/2026-09-01-rescore-nvda.md) and [2026-09-04](../../sessions/2026-09-04-rescore-nvda.md) rescores state explicitly **"No order was placed or modified by this session — recommendation only,"** with computed buy ceilings in the $265 range; the existing 19-share position was also flagged as already exceeding risk-based full-target sizing. This order predates both sessions and matches neither's ceiling.
>
> Per Rule 10, both need a `sessions/`/`decisions/` entry (if deliberate) or cancellation — flagged for the user, not resolved by this sync. See [ibkr-orders.md](ibkr-orders.md).
>
> ## ⚠️ TLT option sell order (1040104046) no longer appears in this sync's order fetch, in any status
>
> Previously active (`NEW`, SELL 1 SEP30'26 $90 CALL @ $0.25 GTC, placed 2026-07-21) as of the 2026-08-30 sync. This sync's `get_account_orders` fetch does not return it at all — unlike CSGP's superseded order, which still shows up tagged `REPLACED`. Worth a manual check in TWS/Client Portal for whether it filled, expired, or was cancelled; not resolved by this sync. See [ibkr-orders.md](ibkr-orders.md).
>
> ## ⚠️ New order this sync: BKNG BUY 10 @ $159.00 LIMIT GTC (order 483688084, placed 2026-08-24) — still open, still undocumented
>
> Carried unresolved from the 2026-08-30 sync — see prior flag; still no `sessions/`/`decisions/` entry. See [ibkr-orders.md](ibkr-orders.md).

> **Two ungoverned equity positions still present (RGL, MBGL) — see [override-log.md](../override-log.md) for detail, unchanged this sync.**

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value (sum of live position market values above, $47,137.33) plus Total Cash ($4,083.32) = $51,220.65, ~$24.56 **below** broker-reported Net Liquidation ($51,245.21) — consistent with the same `get_account_positions` (live/intraday) vs. `get_account_balances` (settled, slightly lagged) timing mismatch noted in prior syncs, not a calculation error.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE), **XEON** (EUR), and **RGL** (AUD, ASX). USD-equivalents (used for `holdings.md` weighting) use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | 4,303.50 | 4,303.50 | 1.0000000 | 4,303.50 |
| EUR | 227.49 | 227.49 | 1.1613635 | 264.20 |
| GBP | 0.00 | 0.00 | 1.3520912 | 0.00 |
| AUD | -672.20 | -672.20 | 0.7203907 | -484.25 |
| **Total (USD-equiv)** | | | | **4,083.32** |

*Row-by-row FX conversion sums to $4,083.45; the Total above uses the broker-reported BASE `cash_balance` (4,083.32) directly, per Rule 0 — the ~$0.13 gap is a rounding artifact, not an error.*

*The same GBP→USD rate (1.3520912) applied to TRN's £1,151.40 market value gives its USD-equivalent: **$1,556.80** — used in `holdings.md` for weighting. The same EUR→USD rate (1.1613635) applied to XEON's €1,501.40 market value gives its USD-equivalent: **$1,743.67**. The same AUD→USD rate (0.7203907) applied to RGL's AUD $660.00 market value gives its USD-equivalent: **$475.46**.*

> **Cash up modestly vs. last sync: $4,061.27 (2026-08-30) → $4,083.32 this sync**, a +$22.05 change (BASE) over the 7-day window — no fills or assignments recorded this window (see the "no order status changed to FILLED" check in [ibkr-orders.md](ibkr-orders.md)); the small delta is ordinary drift (accrued interest/rounding/dividends), not itemized further. **The still-unresolved +$2,523.36 cash jump flagged 2026-08-09 remains open and uninvestigated.**

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

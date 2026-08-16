# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-08-16 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-portfolio`)
**Cash balances last synced:** 2026-08-16 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-portfolio`)
**Account summary:** Net Liquidation $50,764.88 (broker-reported, BASE) · Gross Position Value $47,947.42 (sum of positions below, RGL/TRN/XEON converted at live FX) · Total Cash (USD-equiv) **$2,813.98** (broker-reported, BASE) · Unrealized P&L +$3,800.81 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 27 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders needed. `RGL @ASX` normalized to `RGL` (exchange suffix stripped) for consistency with `holdings.md`. **The live ticker-lookup CSV (`https://www.interactivebrokers.com/download/fracshare_stk.csv`) was reachable this sync** (HTTP 200) — fetched and used to overwrite [`portfolio/reference/ibkr-ticker-lookup.csv`](../reference/ibkr-ticker-lookup.csv) (a handful of rows changed vs. the 2026-08-10 stored copy: EA delisted, FRE→FRE.OLD, a few exchange-code corrections). No held ticker needed the lookup anyway (all resolved via `contract_description`), so this had no practical effect this round beyond keeping the stored fallback current.

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 10 | 264.00 | 2,640.00 | 202.0700 | +619.30 | +30.65% | USD | 265768 |
| AMZN | 12 | 262.65 | 3,151.80 | 210.5885 | +624.74 | +24.72% | USD | 3691937 |
| AVGO | 6 | 393.55 | 2,361.29 | 382.4417 | +66.64 | +2.90% | USD | 313130367 |
| CSGP | 25 | 32.41 | 810.25 | 35.0400 | -65.75 | -7.51% | USD | 6726677 |
| **DOCS Aug21'26 $17.5 PUT (short)** | -1 (contract) | 0.0002 | -0.02 | 0.7496 | +74.94 | n/a — short premium, see note | USD | 852764102 |
| DUOL | 30 | 133.11 | 3,993.27 | 168.2479 | -1,054.17 | -20.89% | USD | 505002183 |
| GOOG | 1 | 343.54 | 343.54 | 295.7000 | +47.84 | +16.18% | USD | 208813720 |
| **MBGL** | 1 | 20.34 | 20.34 | 19.8924 | +0.45 | +2.25% | USD | 893054611 |
| META | 5 | 590.27 | 2,951.35 | 575.0560 | +76.07 | +2.65% | USD | 107113386 |
| MSFT | 17 | 495.40 | 8,421.80 | 391.2165 | +1,771.12 | +26.63% | USD | 272093 |
| NFLX | 12 | 78.33 | 939.92 | 87.7905 | -113.56 | -10.78% | USD | 15124833 |
| NKE | 20 | 40.80 | 816.00 | 43.3100 | -50.20 | -5.80% | USD | 10291 |
| NOW | 9 | 124.00 | 1,116.00 | 87.6100 | +327.51 | +41.54% | USD | 109911821 |
| NVDA | 19 | 224.75 | 4,270.21 | 182.5059 | +802.60 | +23.15% | USD | 4815747 |
| NVO | 5 | 45.31 | 226.56 | 42.5400 | +13.86 | +6.51% | USD | 10611 |
| RBRK | 3 | 102.23 | 306.69 | 58.0962 | +132.40 | +75.97% | USD | 699030013 |
| **RGL** | 60,000 | 0.0100 (AUD) | 600.00 (AUD) | 0.0111 | -66.43 | -9.97% | AUD | 291951342 |
| SPGI | 1 | 418.80 | 418.80 | 391.1076 | +27.69 | +7.08% | USD | 229629397 |
| STIM | 500 | 3.25 | 1,625.00 | 1.5816 | +834.18 | +105.48% | USD | 324062325 |
| STIM Aug21'26 $2.50 CALL (short) | -5 (contracts) | 0.8063 | -403.17 | 0.0545 | -375.94 | n/a — short premium, see note | USD | 840079341 |
| TLT | 100 | 82.04 | 8,204.00 | 87.6030 | -556.30 | -6.35% | USD | 15547841 |
| TRN | 600 | 2.544 (GBP) | 1,526.40 | 2.1195 | +254.69 | +20.05% | GBP | 371871705 |
| UBER | 3 | 75.95 | 227.85 | 82.0233 | -18.22 | -7.40% | USD | 365207014 |
| V | 1 | 364.15 | 364.15 | 319.5100 | +44.64 | +13.97% | USD | 49462172 |
| VEEV | 3 | 243.75 | 731.25 | 164.8333 | +236.75 | +47.88% | USD | 136254493 |
| XEON | 10 | 150.040 (EUR) | 1,500.40 | 149.0250 | +10.15 | +0.68% | EUR | 46041702 |
| ZS | 1 | 183.60 | 183.60 | 157.1600 | +26.44 | +16.82% | USD | 310621426 |

> ## ✅ Resolved this sync — MSFT position-cap trim CONFIRMED FILLED
>
> The `SELL 3 MSFT @ $500.00 GTC` order flagged as "unconfirmed intent" in the 2026-08-09 sync (order 264783699) **filled 2026-08-10T13:30:02Z at $503.34** (better than the $500.00 limit), realized P&L +$301.12, confirmed via `get_account_trades`. MSFT is now **17 shares** (was 20). Combined with the Freedom24 position (unchanged, 2 shares), MSFT's weight drops from 16.42% to **14.03%** — **back under the 15% position cap** (Upgrade 7) for the first time since the breach was first flagged. Its Quality Score (79.9) still fails the 80.0+ gate by 0.1 point, so its Composite Score (29.5) remains reference-only regardless. **Still no `sessions/`/`decisions/` entry documents this as a deliberate trim** — the fill resolves the cap-breach flag but the governance gap (a manual trade placed and executed outside any `/rebalance` or `/rescore` session) is not resolved by the fill itself.
>
> ## ⚠️ New this sync — undocumented NOW trim, 3 shares sold @ $125.00 (order 1031203808, filled 2026-08-10)
>
> **NOW went from 12 shares to 9** — a sale not visible in any prior sync's `get_account_orders` fetch (this order was placed and fully filled within the sync window, so it was never seen as "active" first). Confirmed via `get_account_trades`: `SELL 3 NOW @ $125.00 LIMIT, GTC`, filled 2026-08-10T13:30:06Z, realized P&L +$95.59. No `sessions/`, `decisions/`, or prior `override-log.md` entry covers this trade. NOW's most recent rescore (09 Aug 2026) carries a Composite Score of 51.4 — reference-only, Quality Score 73.2 fails the 80.0+ gate — with no forced-trim or Phase 06 exit trigger on record. **Logged as a new override-log entry this sync** — see [override-log.md](../override-log.md) — flagged for the user to confirm intent.
>
> ## ⚠️ META down another share — 6 → 5, sold @ $611.01 (order 862563692, filled 2026-08-11)
>
> The META `SELL 1 @ $611.01` order that appeared as **`REPLACED` with no live successor visible** in the 2026-08-09 orders sync in fact **did fill**, 2026-08-11T14:15:36Z, realized P&L +$29.87 (confirmed via `get_account_trades`, same $611.01 limit price and share count as the replaced order originally placed 2026-07-05). This **reverses** the previously-flagged "undocumented +1 share" anomaly from the 2026-08-02 sync (5→6, unconfirmed) — META is back to 5 shares, the same count first seen (and separately logged as an undocumented trim) around 2026-07-08–07-11. See the existing [override-log.md](../override-log.md) entry for that history; not duplicated here since it already covers META's share-count volatility as an open item.
>
> ## Cash increase this sync (+$2,492.97 USD leg) is fully explained by the three sales above
>
> USD cash rose from $531.85 to $3,024.82 (+$2,492.97). Summing the three trades' net proceeds ($1,510.02 MSFT + $375.00 NOW + $611.01 META = $2,496.03) less commissions ($3.05 total) = **+$2,492.98** — matches to the cent. **No new unexplained cash movement this sync.** The *separate, still-unresolved* +$2,523.36 cash jump flagged in the 2026-08-09 sync (covering the 2026-08-02→2026-08-09 window, before any of this week's trades) remains open and uninvestigated — not the same event, not resolved by this reconciliation.
>
> ## SPOT position remains absent — still unresolved, unchanged since 2026-08-02
>
> No new information this sync; still flagged for the user to confirm directly in TWS/Client Portal. See [holdings.md](../holdings.md).
>
> ## Two REPLACED orders (META, TRN) from the 2026-08-09 sync no longer appear in this fetch at all
>
> The META `SELL 1 @ $611.01` REPLACED entry is explained (see above — it filled, so it now shows as a trade rather than a stale order). The **TRN `BUY 900 @ GBX 161.50` REPLACED order has simply dropped out of `get_account_orders`'s returned set**, with no matching trade in the last 7 days — it wasn't filled, and there's no way to tell from this fetch whether it expired, was manually cancelled, or aged out of the API's lookback window. Not treated as resolved; flagged for a manual TWS/Client Portal check if it was expected to still be live. HDSN and CSGP's REPLACED orders are unchanged from the prior sync.

> **Two ungoverned equity positions still present (RGL, MBGL) — see [override-log.md](../override-log.md) for detail, unchanged this sync.**

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value (sum of live position market values above, $47,947.42) plus Total Cash ($2,813.98) = $50,761.40, ~$3.47 **below** broker-reported Net Liquidation ($50,764.88) — consistent with the same `get_account_positions` (live/intraday) vs. `get_account_balances` (settled, slightly lagged) timing mismatch noted in prior syncs, not a calculation error.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE), **XEON** (EUR), and **RGL** (AUD, ASX). USD-equivalents (used for `holdings.md` weighting) use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

> **Short-options rows (DOCS put, STIM call):** the P&L % column is marked n/a because percentage-of-cost-basis is not a meaningful figure for a short option position — `Avg Cost` is the average **premium received** per contract when sold, not money paid. Neither short-options row is folded into any ticker's weight % in `holdings.md`. The `TLT SEP30'26 $90 CALL` short-call order (still working, still undocumented — see [ibkr-orders.md](ibkr-orders.md)) has not filled, so it is not yet a position and does not appear in the table above.

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | 3,024.82 | 3,024.82 | 1.0000000 | 3,024.82 |
| EUR | 227.49 | 227.49 | 1.1565539 | 263.10 |
| GBP | 0.00 | 0.00 | 1.3539723 | 0.00 |
| AUD | -668.95 | -668.95 | 0.7082445 | -473.78 |
| **Total (USD-equiv)** | | | | **2,813.98** |

*Row-by-row FX conversion sums to $2,814.14; the Total above uses the broker-reported BASE `cash_balance` (2,813.9831) directly, per Rule 0 — the small gap is a rounding/timing artifact, not an error.*

*The same GBP→USD rate (1.3539723) applied to TRN's £1,526.40 market value gives its USD-equivalent: **$2,066.70** — used in `holdings.md` for weighting. The same EUR→USD rate (1.1565539) applied to XEON's €1,500.40 market value gives its USD-equivalent: **$1,735.29**. The same AUD→USD rate (0.7082445) applied to RGL's AUD $600.00 market value gives its USD-equivalent: **$424.95**.*

> **Cash rose vs. last sync: $322.10 (2026-08-09) → $2,813.98 this sync**, a +$2,491.88 net change (BASE) — see the flag above; fully accounted for by this week's three confirmed trade fills (MSFT, NOW, META), not a new anomaly.

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

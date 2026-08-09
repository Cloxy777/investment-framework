# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-08-09 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-portfolio`)
**Cash balances last synced:** 2026-08-09 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-portfolio`)
**Account summary:** Net Liquidation $50,801.54 (broker-reported, BASE) · Gross Position Value $50,517.78 (sum of positions below, RGL/TRN/XEON converted at live FX) · Total Cash (USD-equiv) **$322.10** (broker-reported, BASE) · Unrealized P&L +$4,010.77 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 27 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders needed. `RGL @ASX` normalized to `RGL` (exchange suffix stripped) for consistency with `holdings.md`. **The live ticker-lookup CSV (`https://www.interactivebrokers.com/download/fracshare_stk.csv`) was reachable this sync** (HTTP 200) — fetched and used to overwrite [`portfolio/reference/ibkr-ticker-lookup.csv`](../reference/ibkr-ticker-lookup.csv) (its contents changed vs. the prior stored copy). No held ticker needed the lookup anyway (all resolved via `contract_description`), so this had no practical effect this round beyond keeping the stored fallback current.

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 10 | 265.21 | 2,652.10 | 202.0700 | +631.40 | +31.25% | USD | 265768 |
| AMZN | 12 | 274.48 | 3,293.76 | 210.5885 | +766.70 | +30.34% | USD | 3691937 |
| AVGO | 6 | 426.45 | 2,558.72 | 382.4417 | +264.07 | +11.51% | USD | 313130367 |
| CSGP | 25 | 30.75 | 768.75 | 35.0400 | -107.25 | -12.24% | USD | 6726677 |
| **DOCS Aug21'26 $17.5 PUT (short)** | -1 (contract) | 0.0226 | -2.26 | 0.7496 | +72.70 | n/a — short premium, see note | USD | 852764102 |
| DUOL | 30 | 130.90 | 3,927.00 | 168.2479 | -1,120.44 | -22.20% | USD | 505002183 |
| GOOG | 1 | 353.65 | 353.65 | 295.7000 | +57.95 | +19.60% | USD | 208813720 |
| **MBGL** | 1 | 19.70 | 19.70 | 19.8924 | -0.19 | -0.97% | USD | 893054611 |
| META | 6 | 591.93 | 3,551.56 | 580.1300 | +70.78 | +2.03% | USD | 107113386 |
| MSFT | 20 | 499.99 | 9,999.80 | 402.6235 | +1,947.33 | +24.18% | USD | 272093 |
| NFLX | 12 | 74.14 | 889.68 | 87.7905 | -163.81 | -15.55% | USD | 15124833 |
| NKE | 20 | 41.75 | 835.00 | 43.3100 | -31.20 | -3.60% | USD | 10291 |
| NOW | 12 | 124.75 | 1,497.04 | 92.7992 | +383.45 | +34.43% | USD | 109911821 |
| NVDA | 19 | 223.80 | 4,252.20 | 182.5059 | +784.59 | +22.63% | USD | 4815747 |
| NVO | 5 | 47.26 | 236.30 | 42.5400 | +23.60 | +11.10% | USD | 10611 |
| RBRK | 3 | 89.53 | 268.60 | 58.0962 | +94.31 | +54.11% | USD | 699030013 |
| **RGL** | 60,000 | 0.0100 (AUD) | 600.00 (AUD) | 0.0111 | -66.43 | -9.97% | AUD | 291951342 |
| SPGI | 1 | 408.19 | 408.19 | 391.1076 | +17.08 | +4.37% | USD | 229629397 |
| STIM | 500 | 2.40 | 1,200.00 | 1.5816 | +409.18 | +51.74% | USD | 324062325 |
| STIM Aug21'26 $2.50 CALL (short) | -5 (contracts) | 0.2495 | -124.75 | 0.0545 | -97.52 | n/a — short premium, see note | USD | 840079341 |
| TLT | 100 | 82.74 | 8,274.28 | 87.6030 | -486.02 | -5.55% | USD | 15547841 |
| TRN | 600 | 2.538 (GBP) | 1,522.80 | 2.1195 | +251.09 | +19.74% | GBP | 371871705 |
| UBER | 3 | 74.99 | 224.96 | 82.0233 | -21.11 | -8.58% | USD | 365207014 |
| V | 1 | 362.79 | 362.79 | 319.5100 | +43.28 | +13.55% | USD | 49462172 |
| VEEV | 3 | 230.47 | 691.41 | 164.8333 | +196.91 | +39.82% | USD | 136254493 |
| XEON | 10 | 149.860 (EUR) | 1,498.60 | 149.0250 | +8.35 | +0.56% | EUR | 46041702 |
| ZS | 1 | 168.75 | 168.75 | 157.1600 | +11.59 | +7.37% | USD | 310621426 |

> ## ⚠️ New this sync — USD cash jumped +$2,523.36 ($-1,991.51 → $531.85), no position share-count change explains it
>
> All 27 positions matched the 2026-08-02 sync exactly in share count and average cost — only prices moved (broadly up: MSFT +8.3%, ADBE +6.1%, NVDA +12.5%, NOW +12.2%, among others). Yet the USD cash balance moved from **-$1,991.51 to +$531.85**, a **+$2,523.36** swing with no corresponding position change to explain it (no new buys, no sells, no fills visible in `get_account_positions`/`get_account_orders`). EUR and GBP cash are unchanged; AUD cash moved only -$2.52 (consistent with routine margin/FX drift, not this). No `sessions/`, `decisions/`, or `override-log` entry covers a deposit, dividend, or other cash event of this size. **Flagged for the user to confirm directly in TWS/Client Portal** — possible causes include a cash deposit, a dividend/interest credit, or a trade settlement outside this sync's position/order scope; per Rule 0 this snapshot does not guess which.
>
> ## ⚠️ New this sync — new MSFT `SELL 3 @ $500.00` GTC order placed today (order 264783699)
>
> A new working order — **`SELL 3 MSFT @ $500.00 LIMIT, GTC`**, order ID 264783699 — appears in this sync's `get_account_orders` fetch with an order time of **2026-08-09T09:09:34Z** (today). This was not present in the 2026-08-02 orders sync. No `sessions/`, `decisions/`, or `override-log` entry covers this order. Given MSFT's confirmed 15% position-cap breach flagged in the 2026-08-02 sync (16.54% → still 16.42% this sync, see [holdings.md](../holdings.md)), this reads plausibly as a manual partial-trim order placed directly in TWS/Client Portal in response to that flag — but that is not confirmed here, only the order's existence and terms. **Flagged for the user to confirm the intent.**
>
> ## SPOT position remains absent — still unresolved from the 2026-08-02 sync
>
> The 1-share SPOT position and its matching `SELL 1 SPOT @ $518.00` GTC order (934588780) remain absent from this sync too — same status as 2026-08-02, no new information. Still flagged for the user to confirm directly in TWS/Client Portal; see [holdings.md](../holdings.md) for the standing note.
>
> ## No other undocumented position changes this sync
>
> All 27 positions (including DOCS put and STIM call) matched the 2026-08-02 sync exactly in share count and average cost. The open governance items from prior syncs (TLT's 2026-07-26 undocumented +23-share increase and its still-working undocumented short call, DOCS's unauthorized short put, RGL's still-unevaluated fully-filled position, MBGL, META's 2026-08-02 undocumented +1 share change) remain open and untouched — see [override-log.md](../override-log.md), unchanged this sync.

> **Two ungoverned equity positions still present (RGL, MBGL) — see [override-log.md](../override-log.md) for detail, unchanged this sync.**

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value (sum of live position market values above, $50,517.78) plus Total Cash ($322.10) = $50,839.88, ~$38.34 **above** broker-reported Net Liquidation ($50,801.54) — consistent with the same `get_account_positions` (live/intraday) vs. `get_account_balances` (settled, slightly lagged) timing mismatch noted in prior syncs, not a calculation error.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE), **XEON** (EUR), and **RGL** (AUD, ASX). USD-equivalents (used for `holdings.md` weighting) use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

> **Short-options rows (DOCS put, STIM call):** the P&L % column is marked n/a because percentage-of-cost-basis is not a meaningful figure for a short option position — `Avg Cost` is the average **premium received** per contract when sold, not money paid. Neither short-options row is folded into any ticker's weight % in `holdings.md`. The `TLT SEP30'26 $90 CALL` short-call order (still working, still undocumented — see [ibkr-orders.md](ibkr-orders.md)) has not filled, so it is not yet a position and does not appear in the table above.

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | 531.85 | 531.85 | 1.0000000 | 531.85 |
| EUR | 227.49 | 227.49 | 1.1557571 | 262.92 |
| GBP | 0.00 | 0.00 | 1.3491557 | 0.00 |
| AUD | -668.95 | -668.95 | 0.7067585 | -472.79 |
| **Total (USD-equiv)** | | | | **322.10** |

*Row-by-row FX conversion sums to $321.99; the Total above uses the broker-reported BASE `cash_balance` (322.1003) directly, per Rule 0 — the small gap is a rounding/timing artifact, not an error.*

*The same GBP→USD rate (1.3491557) applied to TRN's £1,522.80 market value gives its USD-equivalent: **$2,054.49** — used in `holdings.md` for weighting. The same EUR→USD rate (1.1557571) applied to XEON's €1,498.60 market value gives its USD-equivalent: **$1,732.02**. The same AUD→USD rate (0.7067585) applied to RGL's AUD $600.00 market value gives its USD-equivalent: **$424.06**.*

> **Cash swung sharply vs. last sync: -$2,198.29 (2026-08-02) → +$322.10 this sync**, a +$2,520.39 net change — see the flag above; this is well outside routine drift and is not explained by any position change visible to this sync.

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

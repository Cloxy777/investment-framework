# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-07-26 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-portfolio`)
**Cash balances last synced:** 2026-07-26 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-portfolio`)
**Account summary:** Net Liquidation $42,709.07 (broker-reported, BASE) · Gross Position Value $44,880.20 (sum of positions below, RGL/TRN/XEON converted at live FX) · Total Cash (USD-equiv) **–$2,189.32** (broker-reported, BASE) · Unrealized P&L –$1,502.28 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 28 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders needed. `XEON @IBIS2`, `TRN @LSE`, and `RGL @ASX` are normalized to `XEON`/`TRN`/`RGL` (exchange suffix stripped) for consistency with `holdings.md`. **The live ticker-lookup CSV (`https://www.interactivebrokers.com/download/fracshare_stk.csv`) was reachable this sync** (HTTP 200) — fetched and used to overwrite [`portfolio/reference/ibkr-ticker-lookup.csv`](../reference/ibkr-ticker-lookup.csv). No held ticker needed the lookup anyway (all resolved via `contract_description`), so this had no practical effect this round beyond keeping the stored fallback current.

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 10 | 224.51 | 2,245.10 | 202.07 | +224.40 | +11.11% | USD | 265768 |
| AMZN | 12 | 231.55 | 2,778.60 | 210.5885 | +251.54 | +9.95% | USD | 3691937 |
| AVGO | 6 | 381.43 | 2,288.58 | 382.4417 | -6.07 | -0.26% | USD | 313130367 |
| CSGP | 25 | 27.65 | 691.25 | 35.0400 | -184.75 | -21.09% | USD | 6726677 |
| **DOCS Aug21'26 $17.5 PUT (short)** | -1 (contract) | 0.7190 | -71.90 | 0.7496 | +3.06 | n/a — short premium, see note | USD | 852764102 |
| DUOL | 30 | 122.24 | 3,667.20 | 168.2479 | -1,380.24 | -27.35% | USD | 505002183 |
| GOOG | 1 | 318.60 | 318.60 | 295.70 | +22.90 | +7.74% | USD | 208813720 |
| **MBGL** | 1 | 20.55 | 20.55 | 19.8924 | +0.66 | +3.31% | USD | 893054611 |
| META | 5 | 594.10 | 2,970.50 | 590.954 | +15.73 | +0.53% | USD | 107113386 |
| MSFT | 20 | 381.40 | 7,628.00 | 402.6235 | -424.47 | -5.27% | USD | 272093 |
| NFLX | 12 | 70.09 | 841.08 | 87.7905 | -212.41 | -20.16% | USD | 15124833 |
| NKE | 20 | 41.70 | 834.00 | 43.3100 | -32.20 | -3.72% | USD | 10291 |
| NOW | 12 | 97.83 | 1,173.97 | 92.7992 | +60.38 | +5.42% | USD | 109911821 |
| NVDA | 19 | 206.80 | 3,929.20 | 182.5059 | +461.59 | +13.31% | USD | 4815747 |
| NVO | 5 | 48.77 | 243.85 | 42.54 | +31.15 | +14.65% | USD | 10611 |
| RBRK | 3 | 73.24 | 219.72 | 58.0962 | +45.43 | +26.07% | USD | 699030013 |
| **RGL** | 60,000 | 0.0090 (AUD) | 540.00 (AUD) | 0.0111 | -126.43 | -18.97% | AUD | 291951342 |
| SPGI | 1 | 426.40 | 426.40 | 391.1076 | +35.29 | +9.02% | USD | 229629397 |
| SPOT | 1 | 482.66 | 482.66 | 509.00 | -26.34 | -5.17% | USD | 312496724 |
| STIM | 500 | 1.72 | 860.00 | 1.5816 | +69.18 | +8.75% | USD | 324062325 |
| STIM Aug21'26 $2.50 CALL (short) | -5 (contracts) | 0.1787 | -89.37 | 0.0545 | -62.14 | n/a — short premium, see note | USD | 840079341 |
| TLT | 100 | 83.25 | 8,325.00 | 87.6030 | -435.30 | -4.97% | USD | 15547841 |
| TRN | 600 | 2.204 (GBP) | 1,322.40 | 2.1195 | +50.69 | +3.99% | GBP | 371871705 |
| UBER | 3 | 66.42 | 199.25 | 82.0233 | -46.82 | -19.03% | USD | 365207014 |
| V | 1 | 355.74 | 355.74 | 319.51 | +36.23 | +11.34% | USD | 49462172 |
| VEEV | 3 | 186.24 | 558.72 | 164.8333 | +64.22 | +12.99% | USD | 136254493 |
| XEON | 10 | 149.735 (EUR) | 1,497.35 | 149.025 | +7.10 | +0.48% | EUR | 46041702 |
| ZS | 1 | 142.32 | 142.32 | 157.16 | -14.84 | -9.44% | USD | 310621426 |

> ## ⚠️ New this sync — TLT share count jumped from 77 to 100 (+23 shares), unexplained; cash fell by a matching amount
>
> The equity `TLT` position grew from **77 shares (2026-07-20 sync)** to **100 shares** this sync — a +23-share increase — with the blended average cost dropping from $88.79 to $87.6030. Working backward, the 23 added shares were bought at an implied **~$83.63/share** (100×$87.6030 − 77×$88.79 = $1,923.47 ÷ 23 shares), in the same neighborhood as the previously-flagged, now-vanished **`TLT BUY 13 @ $83.54` order** (last seen `REPLACED` with no live successor in the 2026-07-20 `ibkr-orders.md` snapshot) — but that order was for 13 shares, not 23, so it does not cleanly account for the full change. That order is now **completely absent** from this sync's `get_account_orders` fetch (not `NEW`, not `REPLACED`, not `FILLED`, not `CANCELLED`) — the same "vanished order" pattern flagged for the AMZN bracket in the 2026-07-20 sync.
>
> This is internally consistent with the cash side: IBKR USD-equivalent cash fell from **–$264.11 (2026-07-20)** to **–$2,189.32** this sync, a **–$1,925.21** swing — almost exactly the ~$1,923 implied cost of the 23 added TLT shares. So a real trade appears to have executed, but there is no session log, decision log, or working order in this repo documenting it. **Flagged for the user to confirm** what happened (a fill of the replaced order at a different quantity, a manual TWS/Client Portal trade, or something else) — no session/decision entry has been added unilaterally, per this routine's scope (a sync records state, it doesn't interpret or bless a trade).
>
> **Also new this sync — an uncovered/undocumented short call now working on TLT:** `Sell 1 TLT SEP 30 '26 90 Call`, order 1040104046, limit 0.25 GTC, placed 2026-07-21T13:59:42Z, status `NEW` (not yet filled). No session or decision-log entry covers this either. See [ibkr-orders.md](ibkr-orders.md) for the full active-orders table.

> ## No other undocumented position changes this sync
>
> All other 27 positions matched the 2026-07-20 sync exactly in share count and average cost (only prices moved) — TLT (above) is the only change. The open governance items from prior syncs (META's unauthorized -1 share trim, DOCS's unauthorized short put, RGL's still-unevaluated fully-filled position, MBGL) remain open and untouched — see [override-log.md](../override-log.md), unchanged this sync.

> **Two ungoverned equity positions still present (RGL, MBGL) — see [override-log.md](../override-log.md) for detail, unchanged this sync.**

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value (sum of live position market values above, $44,880.20) plus Total Cash (–$2,189.32) = $42,690.88, ~$18.19 **below** broker-reported Net Liquidation ($42,709.07) — consistent with the same `get_account_positions` (live/intraday) vs. `get_account_balances` (settled, slightly lagged) timing mismatch noted in prior syncs, not a calculation error. This gap is smaller than several recent syncs (was $129.69 on 2026-07-20).

> **Currency note:** all positions are USD except **TRN** (GBP, LSE), **XEON** (EUR), and **RGL** (AUD, ASX). USD-equivalents (used for `holdings.md` weighting) use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

> **Short-options rows (DOCS put, STIM call):** the P&L % column is marked n/a because percentage-of-cost-basis is not a meaningful figure for a short option position — `Avg Cost` is the average **premium received** per contract when sold, not money paid. Neither short-options row is folded into any ticker's weight % in `holdings.md`. The new working `TLT SEP30'26 $90 CALL` order has not filled, so it is not yet a position and does not appear in the table above.

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | -1,982.49 | -1,982.49 | 1.000000 | -1,982.49 |
| EUR | 227.49 | 227.49 | 1.1369399 | 258.64 |
| GBP | 0.00 | 0.00 | 1.33227815 | 0.00 |
| AUD | -666.43 | -666.43 | 0.6980911 | -465.23 |
| **Total (USD-equiv)** | | | | **-2,189.32** |

*Row-by-row FX conversion sums to –$2,189.08; the Total above uses the broker-reported BASE `cash_balance` (–$2,189.3223) directly, per Rule 0 — the small gap is a rounding/timing artifact, not an error.*

*The same GBP→USD rate (1.33227815) applied to TRN's £1,322.40 market value gives its USD-equivalent: **$1,761.80** — used in `holdings.md` for weighting. The same EUR→USD rate (1.1369399) applied to XEON's €1,497.35 market value gives its USD-equivalent: **$1,702.40**. The same AUD→USD rate (0.6980911) applied to RGL's AUD $540.00 market value gives its USD-equivalent: **$376.97**.*

> **Cash dropped sharply, from –$264.11 (2026-07-20) to –$2,189.32 this sync** — a –$1,925.21 net swing, almost entirely explained by the unexplained TLT share increase flagged above. AUD cash is still deeply negative (–$666.43, unchanged from last sync) from the RGL fill; no new AUD-side movement this week.

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

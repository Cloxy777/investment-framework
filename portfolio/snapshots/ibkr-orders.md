# IBKR Active Orders Snapshot

**Account:** U19421206
**Last synced:** 2026-09-06 (live via Interactive Brokers MCP — `get_account_orders`)
**Active orders:** 9 working (status `NEW`) · 1 non-active order shown in this fetch (CSGP, `REPLACED` — excluded, see below).

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 483688084 | BUY | BKNG | 10 | LIMIT | 159.00 | GTC | NEW | 2026-08-24T05:30:46Z |
| 934588783 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-06-07T18:27:18Z |
| 862563682 | BUY | MA | 4 | LIMIT | 464.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1872552219 | SELL | NKE | 20 | LIMIT | 54.20 | GTC | NEW | 2026-06-01T20:06:50Z |
| 862563683 | BUY | NOW | 20 | LIMIT | 80.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1306197667 | BUY | NVDA | 10 | LIMIT | 199.56 | GTC | NEW | 2026-08-31T19:57:27Z |
| 1150965513 | BUY | PDD | 10 | LIMIT | 72.55 | GTC | NEW | 2026-07-02T09:28:52Z |
| 510436581 | BUY | TSM | 10 | LIMIT | 369.00 | GTC | NEW | 2026-09-06T17:04:38Z |
| 862563681 | BUY | V | 9 | LIMIT | 285.00 | GTC | NEW | 2026-07-05T19:17:13Z |

**7 of 9 active orders identical to the 2026-08-30 sync — no fills, no cancellations found among the carried orders. Two new orders this week: NVDA BUY 10 @ $199.56 (placed 2026-08-31, between last sync and this one) and TSM BUY 10 @ $369.00 (placed 2026-09-06, today, hours before this sync). One previously-active order (TLT short call, 1040104046) no longer appears in this fetch at all — see below.**

> ## ⚠️ New order: TSM BUY 10 @ $369.00 LIMIT GTC (510436581, placed 2026-09-06T17:04:38Z)
>
> Placed the same day as this sync. TSM's own [2026-09-06 new-position session](../../sessions/2026-09-06-new-position-tsm.md) — run earlier the same day — concludes **"WATCHLIST ONLY — do not enter,"** R/R failing the 2:1 minimum across the entire authorized MoS range (1.33–1.43:1), with computed buy ceilings of **$258.88 (30% MoS) to $277.37 (25% MoS)**. This order's $369.00 limit sits far above every one of those ceilings — not a marginal deviation. No `sessions/` or `decisions/` entry documents placing this order. Flagged for the user: either cancel it, or log the reasoning that overrides today's own analysis, per Rule 10.
>
> ## ⚠️ New order: NVDA BUY 10 @ $199.56 LIMIT GTC (1306197667, placed 2026-08-31T19:57:27Z)
>
> Not present in the 2026-08-30 sync — first appearance this week, placed the day after. Both the [2026-09-01](../../sessions/2026-09-01-rescore-nvda.md) and [2026-09-04](../../sessions/2026-09-04-rescore-nvda.md) NVDA rescores state explicitly that **"No order was placed or modified by this session — recommendation only,"** with computed buy ceilings around $265 (25% MoS off the then-live price) and note the existing 19-share position already exceeds risk-based full-target sizing (a second, independent reason no add would follow even where R/R clears). This order predates both sessions and its $199.56 limit doesn't match either one's ceiling. No `sessions/` or `decisions/` entry documents it. Flagged for the user, not resolved by this sync.
>
> ## ⚠️ TLT short call (1040104046, SELL 1 SEP30'26 $90 CALL @ $0.25 GTC) no longer appears in this fetch, in any status
>
> Active (`NEW`) as of the 2026-08-30 sync. This sync's raw `get_account_orders` response contains no entry for this order ID at all — unlike CSGP's superseded order, which still shows up tagged `REPLACED`. Its disappearance could mean it filled, expired unexercised, or was cancelled — none of which this sync can distinguish from the orders feed alone. Worth a manual check in TWS/Client Portal; if it filled, confirm whether the resulting short position (or assignment) is reflected in `ibkr.md`'s positions table (no unexplained new position appeared this sync, which would be consistent with expiry or cancellation rather than assignment, but isn't conclusive). Not resolved by this sync.
>
> ## CSGP `REPLACED` order (1986163848, placed 2026-05-26) — still present, still excluded
>
> Excluded from the active-orders table above per this file's filtering rule (`REPLACED` = superseded, not live). Still `REPLACED` this sync, with no matching live successor order for CSGP. See [ibkr.md](ibkr.md).
>
> ## ⚠️ BKNG BUY 10 @ $159.00 LIMIT GTC (483688084, placed 2026-08-24) — still open, still undocumented
>
> Carried unresolved from the 2026-08-30 sync (and the sync before it) — still no `sessions/` or `decisions/` entry. See [ibkr.md](ibkr.md) for the full flag (this order sits almost exactly at BKNG's $159.94 ad hoc re-check trigger from its only prior evaluation).

> **Carried, still unresolved from prior syncs — no new session/decision/override-log entry has appeared for any of these:**

| Ticker | Order | Contradicts | Detail |
|---|---|---|---|
| **MA** | BUY 4 @ $464.00 | [2026-06-22 rescore](../../watchlist/not-in-portfolio/MA/MA-2026-06-22.md) | "Trade does NOT execute" — R/R 1.33:1, below the 2:1 minimum. |
| **PDD** | BUY 10 @ $72.55 | [2026-07-01 new-position session](../../sessions/2026-07-01-new-position-pdd.md) | Session recommended ~44 shares at a $128.74 ceiling — size/price don't match. |
| **NOW** | BUY 20 @ $80.00 | — | Still live, unchanged since 2026-07-05 — sits alongside NOW's undocumented 3-share sell logged in [override-log.md](../override-log.md), an odd combination worth the user's attention. |

> **None of the active orders above have filled** (all still `NEW`). **No tool in this repo places, modifies, or cancels a broker order** — flagged for the user to resolve directly in TWS/Client Portal.

> ## SPOT `SELL 1 @ $518.00` order (934588780) — still absent, unchanged from prior syncs
>
> Still does not appear in this fetch in any status, coincident with the SPOT equity position also still being absent — now 7 consecutive syncs. See [ibkr.md](ibkr.md).

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

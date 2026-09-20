# IBKR Active Orders Snapshot

**Account:** U19421206
**Last synced:** 2026-09-20 (live via Interactive Brokers MCP — `get_account_orders`)
**Active orders:** 11 working (status `NEW`) · 2 non-active orders shown in this fetch (ADBE and CSGP, both `REPLACED` — excluded, see below).

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| **87937891** | **BUY** | **AVGO** | **5** | **LIMIT** | **310.60** | **GTC** | **NEW** | **2026-09-19T19:06:59Z** |
| 483688084 | BUY | BKNG | 10 | LIMIT | 159.00 | GTC | NEW | 2026-08-24T05:30:46Z |
| 934588783 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-06-07T18:27:18Z |
| 862563682 | BUY | MA | 4 | LIMIT | 464.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1872552219 | SELL | NKE | 20 | LIMIT | 54.20 | GTC | NEW | 2026-06-01T20:06:50Z |
| 862563683 | BUY | NOW | 20 | LIMIT | 80.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1306197667 | BUY | NVDA | 10 | LIMIT | 199.56 | GTC | NEW | 2026-08-31T19:57:27Z |
| 1150965513 | BUY | PDD | 10 | LIMIT | 72.55 | GTC | NEW | 2026-07-02T09:28:52Z |
| 1528612089 | BUY | TRN | 900 | LIMIT | 1.756 | GTC | NEW | 2026-09-11T10:36:12Z |
| 510436581 | BUY | TSM | 10 | LIMIT | 369.00 | GTC | NEW | 2026-09-06T17:04:38Z |
| 862563681 | BUY | V | 9 | LIMIT | 285.00 | GTC | NEW | 2026-07-05T19:17:13Z |

**One new active order this sync — AVGO BUY 5 @ $310.60 GTC. All other 10 active orders identical to the 2026-09-13 sync — no fills, no cancellations found among the carried orders. The two non-active orders (ADBE, CSGP, both `REPLACED`) are unchanged.**

> ## 🚨 NEW, UNDOCUMENTED ORDER: AVGO BUY 5 @ $310.60 LIMIT GTC (87937891, placed 2026-09-19T19:06:59Z)
>
> Not present in the 2026-09-13 sync — first appearance this week. AVGO's own most recent rescore, [2026-09-15](../../sessions/2026-09-15-rescore-avgo.md), ran a full order-setup pass and explicitly concluded: **"Per fair-value-methodology.md Step 6: R/R fails the minimum threshold across the entire applicable MoS/stop range. No order is placed."** — Net Action **HOLD**, no add (Composite Score 42.3, "Cheap" band, nominally BUY-eligible on paper but the computed order setup fails R/R). That session's computed buy range was **$248.67 (30% MoS) – $266.43 (25% MoS)**. This order's limit price, **$310.60, sits ~16.6% above the top of that range** and is itself above AVGO's live price ($356.96) — not immediately marketable, but real, live, and GTC. No `sessions/` or `decisions/` entry documents this order. **Flagged for the user as urgent: either cancel this order or log the reasoning that overrides the session's own explicit "No order is placed" conclusion, per Rule 10.**
>
> ## ⚠️ TRN BUY 900 @ £1.756 LIMIT GTC (1528612089, placed 2026-09-11T10:36:12Z) — still active, still undocumented
>
> Unchanged since first flagged 2026-09-13. Would grow the TRN position from 600 → 1,500 shares (**+150%**) — contradicts the [2026-09-10 rescore](../../sessions/2026-09-10-rescore-trn.md)'s explicit **HOLD, no top-up** (Quality Score 66.4, fails the 80.0+ gate; independent, still-open CMA "drip pricing" investigation). GBP cash remains $0.00. Limit price £1.756 sits below TRN's live £2.010 (~12.6% below market) — not immediately marketable, but real, live, and GTC. Still no `sessions/`/`decisions/` entry.
>
> ## ⚠️ ADBE non-active order (1071856795, placed 2026-09-11T10:35:03Z) — still `REPLACED`, no live successor
>
> Unchanged since first flagged. ADBE's position (10 shares, avg cost $202.07) remains unchanged, confirming no fill. Not resolved by this sync.
>
> ## ⚠️ TLT short call order (1040104046) still absent from this fetch, in any status — now 3 consecutive syncs
>
> First flagged missing in the 2026-09-06 sync; still absent this sync (2026-08-30 → 2026-09-06 → 2026-09-13 → 2026-09-20). Worth a manual TWS/Client Portal check for whether it filled, expired, or was cancelled. Not resolved by this sync.
>
> ## CSGP `REPLACED` order (1986163848, placed 2026-05-26) — still present, still excluded
>
> Excluded from the active-orders table above per this file's filtering rule (`REPLACED` = superseded, not live). Still `REPLACED` this sync, with no matching live successor order for CSGP. See [ibkr.md](ibkr.md).
>
> ## ⚠️ TSM, NVDA, BKNG, MA, PDD, NOW — all still open, still undocumented, unchanged this sync
>
> Carried unresolved from prior syncs — no new `sessions/`/`decisions/` entry has appeared for any of these:

| Ticker | Order | Contradicts | Detail |
|---|---|---|---|
| **TSM** | BUY 10 @ $369.00 | [2026-09-06 new-position session](../../sessions/2026-09-06-new-position-tsm.md) | "WATCHLIST ONLY — do not enter," ceilings $258.88–$277.37. |
| **NVDA** | BUY 10 @ $199.56 | [2026-09-01](../../sessions/2026-09-01-rescore-nvda.md) / [2026-09-04](../../sessions/2026-09-04-rescore-nvda.md) rescores | Both state no order was placed by that session. |
| **BKNG** | BUY 10 @ $159.00 | — | Sits near BKNG's only prior ad hoc re-check trigger ($159.94); no session/decision entry. |
| **MA** | BUY 4 @ $464.00 | [2026-06-22 rescore](../../watchlist/not-in-portfolio/MA/MA-2026-06-22.md) | "Trade does NOT execute" — R/R 1.33:1, below the 2:1 minimum. |
| **PDD** | BUY 10 @ $72.55 | [2026-07-01 new-position session](../../sessions/2026-07-01-new-position-pdd.md) | Session recommended ~44 shares at a $128.74 ceiling — size/price don't match. |
| **NOW** | BUY 20 @ $80.00 | — | Still live, unchanged since 2026-07-05 — sits alongside NOW's undocumented 3-share sell logged in [override-log.md](../override-log.md). |

> **None of the active orders above have filled** (all still `NEW`). **No tool in this repo places, modifies, or cancels a broker order** — flagged for the user to resolve directly in TWS/Client Portal.
>
> ## SPOT `SELL 1 @ $518.00` order (934588780) — still absent, unchanged from prior syncs
>
> Still does not appear in this fetch in any status, coincident with the SPOT equity position also still being absent — now 9 consecutive syncs. See [ibkr.md](ibkr.md).

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

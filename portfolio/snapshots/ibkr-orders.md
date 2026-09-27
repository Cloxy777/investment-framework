# IBKR Active Orders Snapshot

**Account:** U19421206
**Last synced:** 2026-09-27 (live via Interactive Brokers MCP — `get_account_orders`)
**Active orders:** 5 working (status `NEW`) · 2 non-active orders shown in this fetch (TRN `PENDING_CANCEL`, CSGP `REPLACED` — both excluded, see below).

| Order ID | Side | Ticker | Qty | Order Type | Limit Price | Time in Force | Status | Order Placed (UTC) |
|----------|------|--------|-----|------------|--------------|---------------|--------|---------------------|
| 934588783 | SELL | GOOG | 1 | LIMIT | 389.00 | GTC | NEW | 2026-06-07T18:27:18Z |
| 862563682 | BUY | MA | 4 | LIMIT | 464.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 1872552219 | SELL | NKE | 20 | LIMIT | 54.20 | GTC | NEW | 2026-06-01T20:06:50Z |
| 862563683 | BUY | NOW | 20 | LIMIT | 80.00 | GTC | NEW | 2026-07-05T19:17:13Z |
| 862563681 | BUY | V | 9 | LIMIT | 285.00 | GTC | NEW | 2026-07-05T19:17:13Z |

**This fetch returned only 7 total records, versus 13 (11 active + 2 non-active) last sync — see the coverage note in [ibkr.md](ibkr.md).** Confirmed changes among tracked orders:
- **BKNG (483688084) — FILLED.** No longer appears in the fetch; BKNG is now a 10-share position (avg cost ~$159.10, vs. the order's $159.00 limit). See [ibkr.md](ibkr.md).
- **AVGO (87937891), NVDA (1306197667), PDD (1150965513), TSM (510436581), ADBE (1071856795, `REPLACED`) — no longer appear in this fetch, in any status.** Positions confirm none of AVGO/NVDA filled (share counts and avg costs unchanged); no PDD or TSM position exists. Reads as cancellation for all four, but "every order on record" not holding this sync means it isn't certain from this fetch alone — see the coverage note in [ibkr.md](ibkr.md).
- **TRN (1528612089) — status changed NEW → `PENDING_CANCEL`.** Excluded from the active table above (see below).
- **CSGP (1986163848) — still `REPLACED`,** unchanged.

> ## 🚨 ADBE — undocumented fill, no order ever tracked (10 → 20 shares)
>
> No ADBE order other than the long-`REPLACED` 1071856795 (no live successor since 2026-09-11) has ever appeared in this file, yet ADBE's position doubled this sync. This is not traceable to any order this snapshot has recorded. See [ibkr.md](ibkr.md) and [override-log.md](../override-log.md).
>
> ## 🚨 BKNG (483688084, placed 2026-08-24T05:30:46Z) — FILLED, still undocumented by any session/decision
>
> Filled ~10 shares @ ~$159.10 (limit was $159.00). BKNG's only evaluation, the [2026-08-05 new-position session](../../sessions/2026-08-05-new-position-bkng.md), concluded **"WATCHLIST ONLY — do not enter"** (R/R fails 2:1 at every authorized MoS/stop). No `sessions/`/`decisions/` entry overrides that call. **Flagged as urgent.** Logged in [override-log.md](../override-log.md).
>
> ## ⚠️ TRN (1528612089, originally placed 2026-09-11T10:36:12Z) — now `PENDING_CANCEL` as of 2026-09-26T14:25:58Z
>
> A cancel request appears to be in flight for this order (BUY 900 TRN @ 1.756, GTC) — the status changed from `NEW` (last 5 syncs) to `PENDING_CANCEL` the day before this sync. Not one of [sync-sop.md](../sync-sop.md)'s named active/inactive statuses (glossary entry added this sync — see [glossary.md](../../framework/glossary.md#pending_cancel-order-status)); excluded from the active table above since it's headed toward cancellation, but not yet confirmed complete. Would be good news if it finishes cancelling — this order has contradicted TRN's [2026-09-10 rescore](../../sessions/2026-09-10-rescore-trn.md) (HOLD, no top-up) since 2026-09-11.
>
> ## MA, NOW, GOOG, NKE, V — five orders still open, still undocumented, unchanged this sync
>
> Carried unresolved from prior syncs — no new `sessions/`/`decisions/` entry has appeared for any of these:

| Ticker | Order | Contradicts | Detail |
|---|---|---|---|
| **MA** | BUY 4 @ $464.00 | [2026-06-22 rescore](../../watchlist/not-in-portfolio/MA/MA-2026-06-22.md) | "Trade does NOT execute" — R/R 1.33:1, below the 2:1 minimum. |
| **NOW** | BUY 20 @ $80.00 | — | Still live, unchanged since 2026-07-05 — sits alongside NOW's undocumented 3-share sell logged in [override-log.md](../override-log.md). |
| **GOOG** | SELL 1 @ $389.00 | — | Unchanged since 2026-06-07; no documented sell trigger on record. |
| **NKE** | SELL 20 @ $54.20 | — | Unchanged since 2026-06-01; no documented sell trigger on record. |
| **V** | BUY 9 @ $285.00 | — | Unchanged since 2026-07-05; no documented buy trigger on record. |

> **None of the active orders above have filled** (all still `NEW`). **No tool in this repo places, modifies, or cancels a broker order** — flagged for the user to resolve directly in TWS/Client Portal.
>
> ## SPOT `SELL 1 @ $518.00` order (934588780) — still absent, unchanged from prior syncs
>
> Still does not appear in this fetch in any status, coincident with the SPOT equity position also still being absent — now 10 consecutive syncs. See [ibkr.md](ibkr.md).
>
> ## ⚠️ TLT short call order (1040104046) still absent from this fetch, in any status — now 4 consecutive syncs
>
> First flagged missing in the 2026-09-06 sync; still absent this sync. Worth a manual TWS/Client Portal check for whether it filled, expired, or was cancelled. Not resolved by this sync.
>
> ## CSGP `REPLACED` order (1986163848, placed 2026-05-26) — still present, still excluded
>
> Excluded from the active-orders table above per this file's filtering rule (`REPLACED` = superseded, not live). Still `REPLACED` this sync, with no matching live successor order for CSGP. See [ibkr.md](ibkr.md).

*This file is overwritten on every IBKR active-orders sync — see [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

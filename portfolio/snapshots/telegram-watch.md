# Telegram Stock-Mention Watch

> State file for [Routine 6 — Telegram Stock-Mention Scan](../../framework/automation-schedule.md#routine-6--telegram-stock-mention-scan) (`/telegram-scan`). Overwritten in place each run — git history preserves prior state, same convention as [ibkr.md](ibkr.md) and [ibkr-orders.md](ibkr-orders.md). Tracks the last-seen post per monitored channel (so no post is reprocessed or silently skipped) plus a running log of every company mention the command has evaluated, whether or not it triggered an action.

## Monitored channels

| Channel | Last-seen post (UTC) | Last checked |
|---|---|---|
| https://t.me/tarasguk | tarasguk/11146 (~15:54 UTC, 2026-06-21) | 2026-06-21 16:36 UTC |
| https://t.me/FinnInvestChannel | FinnInvestChannel/2807 (~16:23, 2026-06-21) | 2026-06-21 16:36 UTC |
| https://t.me/myroslavkorol | myroslavkorol/2471 (~10:38 UTC, 2026-06-21) | 2026-06-21 16:36 UTC |
| https://t.me/bolshegold | bolshegold/9601 (~15:25 UTC, 2026-06-21) | 2026-06-21 16:36 UTC |

## Mention log

*(most recent first — one row per ticker mention evaluated, whether or not it triggered an action)*

| Date | Channel | Ticker | Action | Note |
|---|---|---|---|---|
| 2026-06-21 | https://t.me/bolshegold | — | baseline seeded | First run for this channel — no prior marker to diff against (per command step 2). Marker set to bolshegold/9601. Post itself is generic "market opens tomorrow, chill" commentary — no company/ticker named, would not have actioned even outside baseline pass. |
| 2026-06-21 | https://t.me/myroslavkorol | — | baseline seeded | First run for this channel. Marker set to myroslavkorol/2471. Post is a one-line joke ("чим би дитя не тішилось") — no company/ticker named. |
| 2026-06-21 | https://t.me/FinnInvestChannel | — | baseline seeded | First run for this channel. Marker set to FinnInvestChannel/2807. Post is macro commentary on AI data-center electricity demand (citing Yahoo Finance) — no specific company/ticker named, generic macro theme only. |
| 2026-06-21 | https://t.me/tarasguk | — | baseline seeded | First run for this channel. Marker set to tarasguk/11146. Post is political commentary (Trump/Johnson) — unrelated to any company. |

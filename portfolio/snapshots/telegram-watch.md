# Telegram Stock-Mention Watch

> State file for [Routine 6 — Telegram Stock-Mention Scan](../../framework/automation-schedule.md#routine-6--telegram-stock-mention-scan) (`/telegram-scan`). Overwritten in place each run — git history preserves prior state, same convention as [ibkr.md](ibkr.md) and [ibkr-orders.md](ibkr-orders.md). Tracks the last-seen post per monitored channel (so no post is reprocessed or silently skipped) plus a running log of every company mention the command has evaluated, whether or not it triggered an action.

## Monitored channels

| Channel | Last-seen post (UTC) | Last checked |
|---|---|---|
| https://t.me/tarasguk | 2026-06-21 17:04 UTC (post 11148) | 2026-06-21 17:36 UTC |
| https://t.me/FinnInvestChannel | 2026-06-21 16:23 UTC (post 2807) | 2026-06-21 17:36 UTC |
| https://t.me/myroslavkorol | 2026-06-20 10:38 UTC (post 2471) | 2026-06-21 17:36 UTC |
| https://t.me/bolshegold | 2026-06-21 15:25 UTC (post 9601) | 2026-06-21 17:36 UTC |

## Mention log

*(most recent first — one row per ticker mention evaluated, whether or not it triggered an action)*

| Date | Channel | Ticker | Action | Note |
|---|---|---|---|---|
| 2026-06-21 | t.me/tarasguk | — | no action — baseline seeded | First run for this channel (marker was "not yet run"); per telegram-scan.md step 2, no prior post to diff against. Top post (#11148, 17:04 UTC) is a video-announcement teaser (chip-makers vs. hyperscalers, no specific ticker named) — marker set to it, not evaluated. |
| 2026-06-21 | t.me/FinnInvestChannel | — | no action — baseline seeded | First run for this channel. Top post (#2807, 16:23 UTC) discusses AI power-demand constraints, mentions Nvidia only as historical context ("the AI race started with Nvidia's chips, but..."), not a Rule-9 event about NVDA — marker set to it, not evaluated per the baseline-seeding rule regardless. |
| 2026-06-21 | t.me/myroslavkorol | — | no action — baseline seeded | First run for this channel. Top post (#2471, 20 Jun 10:38 UTC) is a one-line personal remark, no company/ticker named — marker set to it. |
| 2026-06-21 | t.me/bolshegold | — | no action — baseline seeded | First run for this channel. Top post (#9601, 15:25 UTC) is a generic "market opens tomorrow, relax" remark, no company/ticker named — marker set to it. |

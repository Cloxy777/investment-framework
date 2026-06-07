# Current Holdings

> Source of truth for what's actually owned. Update after every [portfolio sync](sync-sop.md) or trade. Each entry should carry the last valuation score and review date so [/rescore](../.claude/commands/rescore.md) knows what's due.

**As of 2026-06-07 — live sync from [IBKR](snapshots/ibkr.md) + [Freedom Finance](snapshots/freedom-finance.md) snapshots, now including cash balances (IBKR side).**

Combined total ≈ **$53,786.53** = IBKR Net Liquidation Value $38,769.84 (positions **+** cash, broker-reported) + Freedom24 Opened-Positions Value $15,016.69 (**positions only — Freedom24 cash not yet captured**, see note below). Weight % = each row's combined USD-equivalent value ÷ this total. *Score and review-date columns are intentionally blank — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.*

| Ticker | Weight % | Last Score | Last Review | Broker |
|--------|----------|------------|-------------|--------|
| AMZN | 10.51% | | | IBKR + Freedom24 |
| CASH (IBKR) | 7.41% | | | IBKR |
| CASH (Freedom24) | pending† | | | Freedom24 |
| CSGP | 1.58% | | | IBKR |
| DUOL | 7.62% | | | IBKR + Freedom24 |
| GOOG | 0.68% | | | IBKR |
| META | 5.48% | | | IBKR + Freedom24 |
| MSFT | 16.87% | | | IBKR + Freedom24 |
| NFLX | 1.83% | | | IBKR |
| NKE | 1.59% | | | IBKR |
| NOW | 2.47% | | | IBKR |
| NVDA | 5.31% | | | IBKR |
| NVO | 0.40% | | | IBKR |
| RBRK | 0.40% | | | IBKR |
| SPGI | 0.79% | | | IBKR |
| SPOT | 0.92% | | | IBKR |
| STIM | 0.83% | | | IBKR |
| TLT | 30.83% | | | IBKR + Freedom24 |
| UBER | 0.39% | | | IBKR |
| V | 0.60% | | | IBKR |
| XEON | 3.20% | | | IBKR |
| ZS | 0.24% | | | IBKR |

**XEON is EUR-denominated** (€1,493.16 market value). Its USD-equivalent (**$1,720.46**, used for the weight above) comes from the *live* EUR→USD rate (1.152226) returned by IBKR's `get_account_balances` — broker-reported, not assumed. (This also happens to confirm the $1,720.45 figure I'd back-derived by subtraction last sync, before `get_account_balances` was added to the SOP — nice cross-check, but the live-rate method is now the standard going forward.)

**`CASH (IBKR)`** = $3,983.37 USD-equivalent (per-currency breakdown — $3,973.94 USD + €8.18 EUR — in the [IBKR snapshot](snapshots/ibkr.md)).

† **`CASH (Freedom24)`** is *pending* — not a typo or omission. The Freedom24 screenshot synced this round only covered the "Opened Positions" view, which doesn't surface cash / available-for-withdrawal / total account value. Until a screenshot of that view is provided (see [sync-sop.md](sync-sop.md)), Freedom24's cash is **excluded from the combined total above** — meaning every weight % in this table is *very slightly* overstated, and will shift down a touch (and a `CASH (Freedom24)` figure will appear) once that gap is closed on the next sync. This isn't invented or estimated; it's left blank on purpose.

**Combined positions across both brokers:** AMZN, DUOL, META, MSFT, and TLT are each held in both IBKR and Freedom Finance — their weights above are the *sum* of both brokers' USD-equivalent market values. All other equity tickers are IBKR-only.

*Note: the previous placeholder list here (MSFT, NVDA, AMZN, META, AVGO, GOOG, DUOL, NFLX, NOW, SPOT, TLT, NKE, CSGP, CSCO, SPGI — "from framework knowledge base, needs refresh via sync") has been superseded by this live sync. AVGO and CSCO no longer appear in either broker account (positions likely exited prior to this sync — worth a quick gut-check against [decisions/](../decisions/) and [override-log.md](override-log.md) the next time you're reviewing the book), and several tickers not on that old list are now held (CSGP, GOOG, NOW, NVDA, NVO, RBRK, SPGI, STIM, UBER, V, XEON, ZS).*

*Run `/sync-portfolio` (see [sync-sop.md](sync-sop.md)) to refresh weights/cash/brokers from the live [snapshots](snapshots/); run `/rescore` to populate score and review-date columns.*

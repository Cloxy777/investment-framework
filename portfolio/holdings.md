# Current Holdings

> Source of truth for what's actually owned. Update after every [portfolio sync](sync-sop.md) or trade. Each entry should carry the last valuation score and review date so [/rescore](../.claude/commands/rescore.md) knows what's due.

**As of 2026-06-07 — live sync from [IBKR](snapshots/ibkr.md) + [Freedom Finance](snapshots/freedom-finance.md) snapshots.**

Combined portfolio value ≈ **$49,776.74** (IBKR Gross Position Value $34,760.05 + Freedom24 Total Value $15,016.69, both broker-reported in USD). Weight % below = each ticker's combined market value across both brokers ÷ this total. *Score and review-date columns are intentionally blank — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.*

| Ticker | Weight % | Last Score | Last Review | Broker |
|--------|----------|------------|-------------|--------|
| AMZN | 11.35% | | | IBKR + Freedom24 |
| CSGP | 1.70% | | | IBKR |
| DUOL | 8.23% | | | IBKR + Freedom24 |
| GOOG | 0.73% | | | IBKR |
| META | 5.92% | | | IBKR + Freedom24 |
| MSFT | 18.23% | | | IBKR + Freedom24 |
| NFLX | 1.97% | | | IBKR |
| NKE | 1.72% | | | IBKR |
| NOW | 2.67% | | | IBKR |
| NVDA | 5.74% | | | IBKR |
| NVO | 0.43% | | | IBKR |
| RBRK | 0.44% | | | IBKR |
| SPGI | 0.85% | | | IBKR |
| SPOT | 0.99% | | | IBKR |
| STIM | 0.89% | | | IBKR |
| TLT | 33.32% | | | IBKR + Freedom24 |
| UBER | 0.42% | | | IBKR |
| V | 0.65% | | | IBKR |
| XEON | 3.46%* | | | IBKR |
| ZS | 0.26% | | | IBKR |

\* **XEON is EUR-denominated** (€1,493.16 market value per the IBKR snapshot). Its USD-equivalent value (~$1,720.45) was *not* independently estimated — it was derived by subtraction from two figures IBKR itself reports: Gross Position Value ($34,760.05) minus the sum of all USD-denominated IBKR position values ($33,039.60). That arithmetic uses only broker-reported totals, consistent with the "never invent or estimate financial data" rule — no FX rate was assumed.

**Combined positions across both brokers:** AMZN, DUOL, META, MSFT, and TLT are each held in both IBKR and Freedom Finance — their weights above are the *sum* of both brokers' market values. All other tickers are IBKR-only.

*Note: the previous placeholder list here (MSFT, NVDA, AMZN, META, AVGO, GOOG, DUOL, NFLX, NOW, SPOT, TLT, NKE, CSGP, CSCO, SPGI — "from framework knowledge base, needs refresh via sync") has been superseded by this live sync. AVGO and CSCO no longer appear in either broker account (positions likely exited prior to this sync — worth a quick gut-check against [decisions/](../decisions/) and [override-log.md](override-log.md) the next time you're reviewing the book), and several tickers not on that old list are now held (CSGP, GOOG, NOW, NVDA, NVO, RBRK, SPGI, STIM, UBER, V, XEON, ZS).*

*Run `/sync-portfolio` (see [sync-sop.md](sync-sop.md)) to refresh weights/brokers from the live [snapshots](snapshots/); run `/rescore` to populate score and review-date columns.*

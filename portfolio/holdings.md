# Current Holdings

> Source of truth for what's actually owned. Update after every [portfolio sync](sync-sop.md) or trade. Each entry should carry the last valuation score and review date so [/rescore](../.claude/commands/rescore.md) knows what's due.

**As of 2026-06-07 — live sync from [IBKR](snapshots/ibkr.md) + [Freedom Finance](snapshots/freedom-finance.md) snapshots, including cash balances on both sides.**

Combined total ≈ **$53,893.38** = IBKR Net Liquidation Value $38,769.84 + Freedom24 Net Asset Valuation $15,123.54 (both broker-reported, **positions + cash**, in USD). Weight % = each row's combined USD-equivalent value ÷ this total. *Score and review-date columns are intentionally blank — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.*

**Score scale (2026-06-11):** Valuation scores now run **0.0–99.9** (continuous, 0 = cheapest, 99.9 = most expensive) instead of the old 1–10 integers — see [valuation-scoring.md](../framework/valuation-scoring.md) and [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md). The `Last Score` values above are mechanical conversions of the prior 1–10 scores via `(Old − 1) × 11.1`, **not** fresh recomputations under the new continuous sub-score formulas — treat them as placeholders and refresh via `/rescore` at the next review for full precision.

| Ticker | Weight % | Last Score | Last Review | Broker |
|--------|----------|------------|-------------|--------|
| AMZN | 10.49% | 77.7 | Jun 2026 | IBKR + Freedom24 |
| CASH (Freedom24) | 0.20% | | | Freedom24 |
| CASH (IBKR) | 7.39% | | | IBKR |
| CSGP | 1.57% | 77.7 | Jun 2026 | IBKR |
| DUOL | 7.60% | 33.3 | Jun 2026 | IBKR + Freedom24 |
| GOOG | 0.68% | 77.7 | Jun 2026 | IBKR |
| META | 5.47% | 44.4 | Jun 2026 | IBKR + Freedom24 |
| MSFT | 16.84% | 55.5 | Jun 2026 | IBKR + Freedom24 |
| NFLX | 1.82% | 66.6 | Jun 2026 | IBKR |
| NKE | 1.59% | 33.3 | Jun 2026 | IBKR |
| NOW | 2.47% | 55.5 | Jun 2026 | IBKR |
| NVDA | 5.30% | 55.5 | Jun 2026 | IBKR |
| NVO | 0.40% | 33.3 | Jun 2026 | IBKR |
| RBRK | 0.40% | not scored — fails quality gates | Jun 2026 | IBKR |
| SPGI | 0.79% | 44.4 | Jun 2026 | IBKR |
| SPOT | 0.92% | 77.7 | Jun 2026 | IBKR |
| STIM | 0.83% | not scored — going-concern override | Jun 2026 | IBKR |
| TLT | 30.77% | not scored — non-equity, framework gap | Jun 2026 | IBKR + Freedom24 |
| UBER | 0.39% | 55.5 | Jun 2026 | IBKR |
| V | 0.60% | 55.5 | Jun 2026 | IBKR |
| XEON | 3.19% | not scored — cash-equivalent, out of scope | Jun 2026 | IBKR |
| ZS | 0.24% | 55.5 (low-confidence) | Jun 2026 | IBKR |

**XEON is EUR-denominated** (€1,493.16 market value). Its USD-equivalent (**$1,720.46**, used for the weight above) comes from the *live* EUR→USD rate (1.152226) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**`CASH (IBKR)`** = $3,983.37 USD-equivalent ($3,973.94 USD + €8.18 EUR — full per-currency breakdown in the [IBKR snapshot](snapshots/ibkr.md)).

**`CASH (Freedom24)`** = $106.85 (single-currency, USD — no FX conversion needed). Sourced from a second screenshot of the Freedom24 app's top-level Portfolio view (Net Asset Valuation → Cash card), requested specifically to close this gap. It ties out exactly: $15,016.69 (positions) + $106.85 (cash) = $15,123.54 (Net Asset Valuation) — see the [Freedom Finance snapshot](snapshots/freedom-finance.md) for the cross-check. Both brokers' cash is now captured, so the combined total above is the *true* whole-portfolio figure (positions + cash, both accounts) — no more "pending" caveat.

**Combined positions across both brokers:** AMZN, DUOL, META, MSFT, and TLT are each held in both IBKR and Freedom Finance — their weights above are the *sum* of both brokers' USD-equivalent market values. All other equity tickers are IBKR-only; both `CASH` rows are naturally broker-specific.

*Note: the previous placeholder list here (MSFT, NVDA, AMZN, META, AVGO, GOOG, DUOL, NFLX, NOW, SPOT, TLT, NKE, CSGP, CSCO, SPGI — "from framework knowledge base, needs refresh via sync") has been superseded by this live sync. AVGO and CSCO no longer appear in either broker account (positions likely exited prior to this sync — worth a quick gut-check against [decisions/](../decisions/) and [override-log.md](override-log.md) the next time you're reviewing the book), and several tickers not on that old list are now held (CSGP, GOOG, NOW, NVDA, NVO, RBRK, SPGI, STIM, UBER, V, XEON, ZS).*

*Run `/sync-portfolio` (see [sync-sop.md](sync-sop.md)) to refresh weights/cash/brokers from the live [snapshots](snapshots/); run `/rescore` to populate score and review-date columns.*

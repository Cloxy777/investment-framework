# Current Holdings

> Source of truth for what's actually owned. Update after every [portfolio sync](sync-sop.md) or trade. Each entry should carry the last valuation score and review date so [/rescore](../.claude/commands/rescore.md) knows what's due.

**As of 2026-06-11 — live sync from [IBKR](snapshots/ibkr.md) (positions, cash balances, and active orders all refreshed 2026-06-11) + [Freedom Finance](snapshots/freedom-finance.md) snapshot (last synced 2026-06-07, unchanged this run), including cash balances on both sides.**

Combined total ≈ **$53,855.83** = IBKR Net Liquidation Value $38,732.29 + Freedom24 Net Asset Valuation $15,123.54 (both broker-reported, **positions + cash**, in USD). Weight % = each row's combined USD-equivalent value ÷ this total. *Score and review-date columns are intentionally blank — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.*

> **Portfolio changes since the 2026-06-07 sync (flagged here, no framework action taken — see [ibkr.md](snapshots/ibkr.md) for details):**
>
> - **New position — VEEV** (3 sh @ avg cost $164.83, IBKR): the previously-active `BUY 3 VEEV @ 164.50 GTC` limit order has filled. Added below with blank Last Score/Last Review — needs `/new-position` or `/rescore` to populate.
> - **META position size increased 4 → 6 shares** on IBKR (avg cost $605.98 → $597.81). Its existing Last Score (43.7, Jun 2026) was computed on the prior share count; share count alone doesn't change a per-share valuation score, but a `/rescore` refresh is worth doing at the next opportunity given the position has grown.

**Score scale (2026-06-11):** Valuation scores run **0.0–100.0** (continuous, 0 = cheapest, 100.0 = most expensive) instead of the old 1–10 integers — see [valuation-scoring.md](../framework/valuation-scoring.md) and [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md). The `Last Score` values above are now **real computations** under the new continuous sub-score formulas (FCF Yield, EV/EBIT, Forward PE, PEG) plus the +5 Rate Regime Modifier, applied to the underlying metrics already gathered in the [2026-06-07 full-portfolio rescore](../sessions/2026-06-07-rescore-full-portfolio.md) and [NVDA rescore](../sessions/2026-06-07-rescore-nvda.md) — full per-ticker arithmetic is in [sessions/2026-06-11-rescore-holdings-new-scale.md](../sessions/2026-06-11-rescore-holdings-new-scale.md). This is **not** a fresh data pull (no new Rule 0 live prices) — it recomputes the same underlying dataset under the new formulas. A full `/rescore` with fresh live prices remains the next step for true freshness, especially for CSGP, GOOG, and SPOT, whose recomputed scores moved from "Expensive" into "Very Expensive" (Trim 25–30% → Trim to 50%) under the new formulas.

| Ticker | Weight % | Last Score | Last Review | Broker |
|--------|----------|------------|-------------|--------|
| AMZN | 10.37% | 79.8 | Jun 2026 | IBKR + Freedom24 |
| CASH (Freedom24) | 0.20% | | | Freedom24 |
| CASH (IBKR) | 4.32% | | | IBKR |
| CSGP | 1.59% | 83.3 | Jun 2026 | IBKR |
| DUOL | 8.46% | 49.1 | Jun 2026 | IBKR + Freedom24 |
| GOOG | 0.66% | 83.7 | Jun 2026 | IBKR |
| META | 7.51% | 43.7 | Jun 2026 | IBKR + Freedom24 |
| MSFT | 16.35% | 52.9 | Jun 2026 | IBKR + Freedom24 |
| NFLX | 1.83% | 58.9 | Jun 2026 | IBKR |
| NKE | 1.65% | 34.1 | Jun 2026 | IBKR |
| NOW | 2.35% | 59.3 | Jun 2026 | IBKR |
| NVDA | 5.28% | 62.2 | Jun 2026 | IBKR |
| NVO | 0.40% | 35.8 | Jun 2026 | IBKR |
| RBRK | 0.40% | not scored — fails quality gates | Jun 2026 | IBKR |
| SPGI | 0.79% | 43.3 | Jun 2026 | IBKR |
| SPOT | 0.93% | 82.0 | Jun 2026 | IBKR |
| STIM | 0.79% | not scored — going-concern override | Jun 2026 | IBKR |
| TLT | 30.79% | not scored — non-equity, framework gap | Jun 2026 | IBKR + Freedom24 |
| UBER | 0.39% | 52.9 | Jun 2026 | IBKR |
| V | 0.60% | 54.9 | Jun 2026 | IBKR |
| VEEV | 0.91% | | | IBKR |
| XEON | 3.20% | not scored — cash-equivalent, out of scope | Jun 2026 | IBKR |
| ZS | 0.23% | 61.1 (low-confidence) | Jun 2026 | IBKR |

**XEON is EUR-denominated** (€1,493.39 market value). Its USD-equivalent (**$1,722.12**, used for the weight above) comes from the *live* EUR→USD rate (1.153162) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**`CASH (IBKR)`** = $2,326.77 USD-equivalent ($2,317.34 USD + €8.18 EUR — full per-currency breakdown in the [IBKR snapshot](snapshots/ibkr.md)).

**`CASH (Freedom24)`** = $106.85 (single-currency, USD — no FX conversion needed). Sourced from a second screenshot of the Freedom24 app's top-level Portfolio view (Net Asset Valuation → Cash card), requested specifically to close this gap. It ties out exactly: $15,016.69 (positions) + $106.85 (cash) = $15,123.54 (Net Asset Valuation) — see the [Freedom Finance snapshot](snapshots/freedom-finance.md) for the cross-check. Both brokers' cash is now captured, so the combined total above is the *true* whole-portfolio figure (positions + cash, both accounts) — no more "pending" caveat.

**Combined positions across both brokers:** AMZN, DUOL, META, MSFT, and TLT are each held in both IBKR and Freedom Finance — their weights above are the *sum* of both brokers' USD-equivalent market values. All other equity tickers are IBKR-only; both `CASH` rows are naturally broker-specific.

*Note: the previous placeholder list here (MSFT, NVDA, AMZN, META, AVGO, GOOG, DUOL, NFLX, NOW, SPOT, TLT, NKE, CSGP, CSCO, SPGI — "from framework knowledge base, needs refresh via sync") has been superseded by this live sync. AVGO and CSCO no longer appear in either broker account (positions likely exited prior to this sync — worth a quick gut-check against [decisions/](../decisions/) and [override-log.md](override-log.md) the next time you're reviewing the book), and several tickers not on that old list are now held (CSGP, GOOG, NOW, NVDA, NVO, RBRK, SPGI, STIM, UBER, V, XEON, ZS).*

*Run `/sync-portfolio` (see [sync-sop.md](sync-sop.md)) to refresh weights/cash/brokers from the live [snapshots](snapshots/); run `/rescore` to populate score and review-date columns (including the new VEEV position).*

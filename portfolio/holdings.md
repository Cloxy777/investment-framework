# Current Holdings

> Source of truth for what's actually owned. Update after every [portfolio sync](sync-sop.md) or trade. Each entry should carry the last valuation score and review date so [/rescore](../.claude/commands/rescore.md) knows what's due.

**As of 2026-06-15 — live sync from [IBKR](snapshots/ibkr.md) (positions, cash balances, and active orders all refreshed 2026-06-15) + [Freedom Finance](snapshots/freedom-finance.md) snapshot (last synced 2026-06-07, unchanged this run), including cash balances on both sides.**

Combined total ≈ **$53,659.11** = IBKR Net Liquidation Value $38,535.57 + Freedom24 Net Asset Valuation $15,123.54 (both broker-reported, **positions + cash**, in USD). Weight % = each row's combined USD-equivalent value ÷ this total. *Score and review-date columns are intentionally blank — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.*

> **Portfolio changes since the 2026-06-11 sync (flagged here, no framework action taken — see [ibkr.md](snapshots/ibkr.md) for details):**
>
> - **New position — ADBE** (10 sh @ avg cost $202.07, IBKR): partial fill toward the [2026-06-12 new-position](../sessions/2026-06-12-new-position-adbe.md) BUY recommendation (Score 5.0, "Very Cheap" — full position 6–8%, ~17-share target). Added below with Last Score 5.0 / 12 Jun 2026 carried over from that session (the score that justified the buy); remaining ~7 shares toward the target not yet purchased. Moved from `watchlist/not-in-portfolio/ADBE/` to `watchlist/in-portfolio/ADBE/`.
> - **No other position-size changes** — all 21 previously-held tickers show identical share counts; only prices moved.

> **Weight column sums to ~100.7%, not 100%** — see the "Note on Gross Position Value vs. Net Liquidation" in [ibkr.md](snapshots/ibkr.md). Weights below are computed per [sync-sop.md](sync-sop.md) (position value ÷ Net Liquidation Value), and IBKR's broker-reported Net Liquidation is currently ~$392 below the live sum of position values + cash (today's intraday gains not yet reflected in NLV). Not a calculation error — flagged for transparency rather than silently rescaled.

**Score scale (2026-06-11):** Valuation scores run **0.0–100.0** (continuous, 0 = cheapest, 100.0 = most expensive) instead of the old 1–10 integers — see [valuation-scoring.md](../framework/valuation-scoring.md) and [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md). The `Last Score` values above are now **real computations** under the new continuous sub-score formulas (FCF Yield, EV/EBIT, Forward PE, PEG) plus the +5 Rate Regime Modifier, applied to the underlying metrics already gathered in the [2026-06-07 full-portfolio rescore](../sessions/2026-06-07-rescore-full-portfolio.md) and [NVDA rescore](../sessions/2026-06-07-rescore-nvda.md) — full per-ticker arithmetic is in [sessions/2026-06-11-rescore-holdings-new-scale.md](../sessions/2026-06-11-rescore-holdings-new-scale.md). This is **not** a fresh data pull (no new Rule 0 live prices) — it recomputes the same underlying dataset under the new formulas. A full `/rescore` with fresh live prices remains the next step for true freshness, especially for CSGP, GOOG, and SPOT, whose recomputed scores moved from "Expensive" into "Very Expensive" (Trim 25–30% → Trim to 50%) under the new formulas.

**Boundary-name rescore (2026-06-20):** the 8 holdings sitting in the 50–63 "Hold/watchlist" band were re-scored with fresh Rule 0 live prices under the new **Upside/Downside Modifier** (see [decisions/2026-06-20-framework-change-upside-downside-modifier.md](../decisions/2026-06-20-framework-change-upside-downside-modifier.md) and the per-ticker `sessions/2026-06-20-rescore-*.md` logs). Seven of the eight dropped a full band into the BUY zone once expected forward return was folded in (MSFT 51.2→35.0, UBER 52.9→34.8, V 54.9→39.2, NOW 59.3→42.3, ZS 61.1→36.3, NVDA 62.2→48.5); DUOL (55.6→50.7) and NFLX (63.2→61.2) stayed in HOLD. **Important:** a BUY-band *score* is not a BUY *order* — every one of the seven is currently blocked from adding by an independent gate (sub-2:1 risk/reward, the 15% position cap, or a Phase 01 quality-gate fail for ZS). No trades were executed; these are score/action-band updates only. The remaining scored equities (AMZN, CSGP, GOOG, SPOT, NKE, NVO, META, SPGI, ADBE) have **not** yet been rescored under the modifier.

| Ticker | Weight % | Last Score | Last Review | Broker |
|--------|----------|------------|-------------|--------|
| ADBE | 3.85% | 5.0 | 12 Jun 2026 | IBKR |
| AMZN | 10.45% | 79.8 | Jun 2026 | IBKR + Freedom24 |
| CASH (Freedom24) | 0.20% | | | Freedom24 |
| CASH (IBKR) | 0.60% | | | IBKR |
| CSGP | 1.53% | 83.3 | Jun 2026 | IBKR |
| DUOL | 8.54% | 53.7 | 20 Jun 2026 | IBKR + Freedom24 |
| GOOG | 0.68% | 83.7 | Jun 2026 | IBKR |
| META | 7.52% | 38.5 | 12 Jun 2026 | IBKR + Freedom24 |
| MSFT | 16.26% | 35.0 | 20 Jun 2026 | IBKR + Freedom24 |
| NFLX | 1.81% | 61.2 | 20 Jun 2026 | IBKR |
| NKE | 1.69% | 34.1 | Jun 2026 | IBKR |
| NOW | 2.37% | 42.3 | 20 Jun 2026 | IBKR |
| NVDA | 5.47% | 48.5 | 20 Jun 2026 | IBKR |
| NVO | 0.41% | 35.8 | Jun 2026 | IBKR |
| RBRK | 0.40% | not scored — fails quality gates | Jun 2026 | IBKR |
| SPGI | 0.78% | 43.3 | Jun 2026 | IBKR |
| SPOT | 0.90% | 82.0 | Jun 2026 | IBKR |
| STIM | 0.86% | not scored — going-concern override | Jun 2026 | IBKR |
| TLT | 31.08% | not scored — non-equity, framework gap | Jun 2026 | IBKR + Freedom24 |
| UBER | 0.39% | 34.8 | 20 Jun 2026 | IBKR |
| V | 0.60% | 39.2 | 20 Jun 2026 | IBKR |
| VEEV | 0.89% | | | IBKR |
| XEON | 3.22% | not scored — cash-equivalent, out of scope | Jun 2026 | IBKR |
| ZS | 0.24% | 36.3 | 20 Jun 2026 | IBKR |

**XEON is EUR-denominated** (€1,493.65 market value). Its USD-equivalent (**$1,727.86**, used for the weight above) comes from the *live* EUR→USD rate (1.156806) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**`CASH (IBKR)`** = $321.57 USD-equivalent ($312.11 USD + €8.18 EUR — full per-currency breakdown in the [IBKR snapshot](snapshots/ibkr.md)).

**`CASH (Freedom24)`** = $106.85 (single-currency, USD — no FX conversion needed). Sourced from a second screenshot of the Freedom24 app's top-level Portfolio view (Net Asset Valuation → Cash card), requested specifically to close this gap. It ties out exactly: $15,016.69 (positions) + $106.85 (cash) = $15,123.54 (Net Asset Valuation) — see the [Freedom Finance snapshot](snapshots/freedom-finance.md) for the cross-check. Both brokers' cash is now captured, so the combined total above is the *true* whole-portfolio figure (positions + cash, both accounts) — no more "pending" caveat.

**Combined positions across both brokers:** AMZN, DUOL, META, MSFT, and TLT are each held in both IBKR and Freedom Finance — their weights above are the *sum* of both brokers' USD-equivalent market values. All other equity tickers are IBKR-only; both `CASH` rows are naturally broker-specific.

*Note: the previous placeholder list here (MSFT, NVDA, AMZN, META, AVGO, GOOG, DUOL, NFLX, NOW, SPOT, TLT, NKE, CSGP, CSCO, SPGI — "from framework knowledge base, needs refresh via sync") has been superseded by this live sync. AVGO and CSCO no longer appear in either broker account (positions likely exited prior to this sync — worth a quick gut-check against [decisions/](../decisions/) and [override-log.md](override-log.md) the next time you're reviewing the book), and several tickers not on that old list are now held (CSGP, GOOG, NOW, NVDA, NVO, RBRK, SPGI, STIM, UBER, V, XEON, ZS).*

*Run `/sync-portfolio` (see [sync-sop.md](sync-sop.md)) to refresh weights/cash/brokers from the live [snapshots](snapshots/); run `/rescore` to populate score and review-date columns (including the new VEEV position).*

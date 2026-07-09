# Current Holdings

> Source of truth for what's actually owned. Update after every [portfolio sync](sync-sop.md) or trade. Each entry should carry the last valuation score and review date so [/rescore](../.claude/commands/rescore.md) knows what's due.

**As of 2026-07-05 — live sync from [IBKR](snapshots/ibkr.md) (positions, cash balances, and active orders all refreshed 2026-07-05) + [Freedom Finance](snapshots/freedom-finance.md) snapshot (last synced 2026-06-07, unchanged this run), including cash balances on both sides.**

Combined total ≈ **$58,226.21** = IBKR Net Liquidation Value $43,102.67 + Freedom24 Net Asset Valuation $15,123.54 (both broker-reported, **positions + cash**, in USD). Weight % = each row's combined USD-equivalent value ÷ this total. *Score and review-date columns are intentionally blank — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.*

> ## ⚠️⚠️ URGENT — unauthorized live orders found this sync, flagged directly to the user
>
> `get_account_orders` this sync surfaced six live orders with no `sessions/`/`decisions/`/`override-log.md` authorization anywhere in this repo — two of them (**HDSN**, **MA**) directly contradict this framework's own explicit "do not trade" recommendations. Full breakdown, per-ticker detail, and dollar exposure in [ibkr-orders.md](snapshots/ibkr-orders.md) and this week's [weekly brief](../sessions/weekly-briefs/2026-07-05-weekly-brief.md). **No position actually changed as a result (none of the six have filled) — this is a live-order/governance risk, not a realized trade**, but it needs the user's attention in TWS/Client Portal directly, since no tool in this repo can cancel an order.

> ⚠️ **Portfolio changes since the 2026-06-28 sync:**
>
> - **Two ungoverned positions confirmed present, added below as tracked rows (not new — first surfaced in the 2026-07-01 rebalance session, this is the first `/sync-portfolio` pass since):**
>   - **RGL** (RiversGold Ltd, ASX micro-cap gold explorer): 2,786 shares, no Phase 01/02 evaluation ever run — see [override-log.md](override-log.md). Its underlying 60,000-share GTC order is still live (57,214 sh unfilled) — see [ibkr-orders.md](snapshots/ibkr-orders.md).
>   - **MBGL** (Mobility Global Inc, NYSE — confirmed via this sync's ticker-lookup CSV refresh): 1 share, $19.80, likely corporate-action-sourced, still not investigated.
> - **Total Cash (IBKR) swung from –$1,576.85 to +$342.69** — the prior sync's negative-GBP-cash funding of the TRN purchase has resolved (GBP cash is now near-zero, +£0.28); mechanism not independently confirmed this sync (a balances-only pull doesn't show the underlying trade), flagged as a resolved-not-investigated note.
> - **AVGO's 2026-06-16 override has since been resolved via a full rescore** (2026-07-04, Quality 82.1 / Composite 43.1) — `override-log.md`'s "Open — under review" line is now stale text; the score itself is current. Not corrected in this pass since override-log rationale-backfill is outside `/sync-portfolio`'s scope — flagged for a future housekeeping pass.
> - **No other position-size changes among previously-tracked tickers** — all other holdings (including ADBE and TRN, still partial fills) show identical share counts; only prices moved.

> **Weight column sums to ~100.1%, not 100%** — see the "Note on Gross Position Value vs. Net Liquidation" in [ibkr.md](snapshots/ibkr.md) for the small live-vs-settled timing gaps, plus the STIM short-call market value (–$50.00) which is intentionally excluded from STIM's weight below. Not a calculation error — flagged for transparency rather than silently rescaled.

**Score scale (2026-06-11):** Valuation scores run **0.0–100.0** (continuous, 0 = cheapest, 100.0 = most expensive) instead of the old 1–10 integers — see [valuation-scoring.md](../framework/valuation-scoring.md) and [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md).

**Boundary-name rescore (2026-06-20):** the 8 holdings sitting in the 50–63 "Hold/watchlist" band were re-scored with fresh Rule 0 live prices under the new **Upside/Downside Modifier** (see [decisions/2026-06-20-framework-change-upside-downside-modifier.md](../decisions/2026-06-20-framework-change-upside-downside-modifier.md) and the per-ticker `sessions/2026-06-20-rescore-*.md` logs). Seven of the eight dropped a full band into the BUY zone once expected forward return was folded in (MSFT 51.2→35.0, UBER 52.9→34.8, V 54.9→39.2, NOW 59.3→42.3, ZS 61.1→36.3, NVDA 62.2→48.5); DUOL (55.6→50.7) and NFLX (63.2→61.2) stayed in HOLD. **Important:** a BUY-band *score* is not a BUY *order* — every one of the seven is currently blocked from adding by an independent gate (sub-2:1 risk/reward, the 15% position cap, or a Phase 01 quality-gate fail for ZS). No trades were executed; these are score/action-band updates only.

**Full scored-book rescore complete (2026-06-20).** The remaining 9 scored equities were also rescored under the modifier (per-ticker `sessions/2026-06-20-rescore-*.md`): ADBE 5.0→0.0, META 38.5→19.6, SPGI 43.3→33.4, NKE 34.1→43.1, NVO 35.8→47.6, AMZN 79.8→73.4, GOOG 83.7→73.1, CSGP 83.3→79.0, SPOT 82.0→80.5. The four richly-valued names (AMZN, GOOG, CSGP, SPOT) stayed in the trim bands — the modifier correctly did **not** rescue them (their forward return only modestly cleared the hurdle), confirming the bounded asymmetry. **The only currently actionable trade across the whole book is ADBE** (score 0.0): a partial-fill position with R/R 4.47:1 and room to its 6–8% target — top up ~7 shares (~$1,366). All other BUY-band names are gated by R/R, the position cap, or a quality-gate fail. Not rescored under the modifier: TLT, XEON, RBRK, STIM (non-equity / cash-equivalent / fails gates) and VEEV (never scored). **AVGO (new this week) is also not yet rescored under the modifier** — its 69.5 score predates the 2026-06-20 framework change.

**Quality Score / Composite Score columns added 2026-06-29** (see [decisions/2026-06-29-framework-change-quality-score-and-composite.md](../decisions/2026-06-29-framework-change-quality-score-and-composite.md) and [quality-scoring.md](../framework/quality-scoring.md)) — every row that carries a numeric Last Score predates this change and does not yet have a Quality Score computed, so both new columns are marked **`?`** (never invented/backfilled) until that ticker's next `/rescore` pass fills them in. Rows already "not scored" (cash, non-equity, quality-gate fail, overrides) are left blank — there is nothing for the new columns to invalidate.

| Ticker | Weight % | Last Score | Quality Score | Composite Score | Last Review | Broker |
|--------|----------|------------|----------------|------------------|-------------|--------|
| ADBE | 3.77% | 0.0 | 83.9 | 8.1 | 04 Jul 2026 | IBKR |
| AMZN | 9.65% | 81.8 | 57.6 | 62.1 | 04 Jul 2026 | IBKR + Freedom24 |
| AVGO | 3.73% | 68.2 | 82.1 | 43.1 | 04 Jul 2026 | IBKR |
| CASH (Freedom24) | 0.18% | | | | | Freedom24 |
| CASH (IBKR) | 0.59% | | | | | IBKR |
| CSGP | 1.29% | 80.5 | 68.4 | 56.1 | 04 Jul 2026 | IBKR |
| DUOL | 7.95% | 56.6 | 83.8 | 36.4 | 04 Jul 2026 | IBKR + Freedom24 |
| GOOG | 0.61% | 67.4 | 73.7 | 46.9 | 04 Jul 2026 | IBKR |
| **MBGL** | 0.03% | not scored — ungoverned position, see note above | | | n/a | IBKR |
| META | 7.04% | 39.0 | 90.0 | 24.5 | 9 Jul 2026 | IBKR + Freedom24 |
| MSFT | 14.84% | 35.5 | 78.3 | 28.6 | 05 Jul 2026 | IBKR + Freedom24 |
| NFLX | 1.60% | 59.9 | 74.0 | 43.0 | 05 Jul 2026 | IBKR |
| NKE | 1.51% | 13.9 | 44.4 | 34.8 | 1 Jul 2026 | IBKR |
| NOW | 2.19% | 61.3 | 78.7 | 41.3 | 05 Jul 2026 | IBKR |
| NVDA | 4.68% | 34.3 | 91.7 | 21.3 | 05 Jul 2026 | IBKR |
| NVO | 0.43% | 61.4 | 66.2 | 47.6 | 05 Jul 2026 | IBKR |
| RBRK | 0.43% | not scored — fails quality gates | | | Jun 2026 | IBKR |
| **RGL** | 0.04% | not scored — ungoverned position, see note above | | | n/a | IBKR |
| SPGI | 0.75% | 36.3 | 67.1 | 34.6 | 05 Jul 2026 | IBKR |
| SPOT | 0.84% | 84.2 | 73.2 | 55.5 | 05 Jul 2026 | IBKR |
| STIM | 1.21% | not scored — going-concern override | | | Jun 2026 | IBKR |
| TLT | 28.54% | not scored — non-equity, framework gap | | | Jun 2026 | IBKR + Freedom24 |
| TRN | 3.00% | 10.0 | 67.2 | 21.4 | 05 Jul 2026 | IBKR |
| UBER | 0.38% | 41.6 | 61.0 | 40.3 | 05 Jul 2026 | IBKR |
| V | 0.62% | 44.5 | 85.9 | 29.3 | 05 Jul 2026 | IBKR |
| VEEV | 0.99% | 45.1 | 85.7 | 29.7 | 01 Jul 2026 | IBKR |
| XEON | 2.94% | not scored — cash-equivalent, out of scope | | | Jun 2026 | IBKR |
| ZS | 0.25% | 43.1 | 59.4 | 41.9 | 05 Jul 2026 | IBKR |

**XEON is EUR-denominated** (€1,495.61 market value). Its USD-equivalent (**$1,710.43**, used for the weight above) comes from the *live* EUR→USD rate (1.1436323) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**TRN is GBP-denominated** (£1,308.00 market value, LSE). Its USD-equivalent (**$1,746.25**, used for the weight above) comes from the *live* GBP→USD rate (1.33505295) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**RGL is AUD-denominated** (AUD $30.65 market value, ASX). Its USD-equivalent (**$21.26**, used for the weight above) comes from the *live* AUD→USD rate (0.6938792) returned by IBKR's `get_account_balances` — broker-reported, not assumed. See the ungoverned-position note above — no Phase 01/02 evaluation exists for this ticker.

**STIM's weight above (1.21%) reflects the 500-share equity position only** ($705.00). A short 5-contract covered call (`STIM Aug21'26 $2.50 CALL`, market value –$50.00) is also held against this position — see [ibkr.md](snapshots/ibkr.md) for detail. Not folded into the weight % here; at ~0.09% of the combined total it would not change STIM's banding either way.

**`CASH (IBKR)`** = **$342.69** USD-equivalent ($103.69 USD + €227.49 EUR ≈ $260.16 + £0.28 GBP ≈ $0.37 − AUD $31.07 ≈ −$21.56, net of rounding — full per-currency breakdown in the [IBKR snapshot](snapshots/ibkr.md)). Swung from –$1,576.85 last sync — see the portfolio-changes note above.

**`CASH (Freedom24)`** = $106.85 (single-currency, USD — no FX conversion needed; unchanged since the 2026-06-07 Freedom Finance sync, no new screenshot this round). It ties out exactly: $15,016.69 (positions) + $106.85 (cash) = $15,123.54 (Net Asset Valuation) — see the [Freedom Finance snapshot](snapshots/freedom-finance.md) for the cross-check.

**Combined positions across both brokers:** AMZN, DUOL, META, MSFT, and TLT are each held in both IBKR and Freedom Finance — their weights above are the *sum* of both brokers' USD-equivalent market values. All other equity tickers are IBKR-only; both `CASH` rows are naturally broker-specific.

**AVGO has a prior, untracked history on this account:** `get_account_trades` shows a 1-share AVGO position sold on 2026-05-26 (predating this framework's records), which is what the now-superseded "AVGO no longer appears in either broker account" placeholder note (removed this sync) was referring to. The 6-share position now held is a fresh, separate buy from 2026-06-16 — see the override flag above.

*Run `/sync-portfolio` (see [sync-sop.md](sync-sop.md)) to refresh weights/cash/brokers from the live [snapshots](snapshots/); run `/rescore` to populate score and review-date columns (VEEV scored 2026-07-01 — see [session](../sessions/2026-07-01-rescore-veev.md); AVGO rescored 2026-07-04, current — see [session](../sessions/2026-07-04-rescore-avgo.md)).*

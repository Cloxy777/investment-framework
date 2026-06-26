# Current Holdings

> Source of truth for what's actually owned. Update after every [portfolio sync](sync-sop.md) or trade. Each entry should carry the last valuation score and review date so [/rescore](../.claude/commands/rescore.md) knows what's due.

**As of 2026-06-22 — live sync from [IBKR](snapshots/ibkr.md) (positions, cash balances, and active orders all refreshed 2026-06-22) + [Freedom Finance](snapshots/freedom-finance.md) snapshot (last synced 2026-06-07, unchanged this run), including cash balances on both sides.**

Combined total ≈ **$55,813.07** = IBKR Net Liquidation Value $40,689.53 + Freedom24 Net Asset Valuation $15,123.54 (both broker-reported, **positions + cash**, in USD). Weight % = each row's combined USD-equivalent value ÷ this total. *Score and review-date columns are intentionally blank — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.*

> ⚠️ **Portfolio changes since the 2026-06-15 sync — headline item is a governance gap, not just a data refresh:**
>
> - **New position — AVGO** (6 sh @ avg cost $382.44, IBKR, bought 2026-06-16): **this is an override, not a framework-driven buy.** The only AVGO evaluation on record, the [2026-06-14 new-position session](../sessions/2026-06-14-new-position-avgo.md), scored it **69.5 — WATCHLIST, explicit "no new entry"** recommendation. The buy went in two days later at essentially the same price, with no [`decisions/`](../decisions/) entry explaining why. Logged retroactively in [override-log.md](override-log.md) (rationale: not on record — flagged for the user to supply). Added below with Last Score 69.5 / 14 Jun 2026 carried over from that session, same convention used for ADBE's partial fill. Moved `watchlist/not-in-portfolio/AVGO/` → `watchlist/in-portfolio/AVGO/`.
> - **No other position-size changes** — all 22 previously-held tickers (including ADBE, still a partial fill at 10 of ~17 target shares) show identical share counts; only prices moved.

> **Weight column sums to ~99.7%, not 100%** — see the "Note on Gross Position Value vs. Net Liquidation" in [ibkr.md](snapshots/ibkr.md): broker-reported Net Liquidation is currently ~$200 *above* the live sum of position values + cash (the reverse of the prior sync's gap direction). Not a calculation error — flagged for transparency rather than silently rescaled.

**Score scale (2026-06-11):** Valuation scores run **0.0–100.0** (continuous, 0 = cheapest, 100.0 = most expensive) instead of the old 1–10 integers — see [valuation-scoring.md](../framework/valuation-scoring.md) and [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md).

**Boundary-name rescore (2026-06-20):** the 8 holdings sitting in the 50–63 "Hold/watchlist" band were re-scored with fresh Rule 0 live prices under the new **Upside/Downside Modifier** (see [decisions/2026-06-20-framework-change-upside-downside-modifier.md](../decisions/2026-06-20-framework-change-upside-downside-modifier.md) and the per-ticker `sessions/2026-06-20-rescore-*.md` logs). Seven of the eight dropped a full band into the BUY zone once expected forward return was folded in (MSFT 51.2→35.0, UBER 52.9→34.8, V 54.9→39.2, NOW 59.3→42.3, ZS 61.1→36.3, NVDA 62.2→48.5); DUOL (55.6→50.7) and NFLX (63.2→61.2) stayed in HOLD. **Important:** a BUY-band *score* is not a BUY *order* — every one of the seven is currently blocked from adding by an independent gate (sub-2:1 risk/reward, the 15% position cap, or a Phase 01 quality-gate fail for ZS). No trades were executed; these are score/action-band updates only.

**Full scored-book rescore complete (2026-06-20).** The remaining 9 scored equities were also rescored under the modifier (per-ticker `sessions/2026-06-20-rescore-*.md`): ADBE 5.0→0.0, META 38.5→19.6, SPGI 43.3→33.4, NKE 34.1→43.1, NVO 35.8→47.6, AMZN 79.8→73.4, GOOG 83.7→73.1, CSGP 83.3→79.0, SPOT 82.0→80.5. The four richly-valued names (AMZN, GOOG, CSGP, SPOT) stayed in the trim bands — the modifier correctly did **not** rescue them (their forward return only modestly cleared the hurdle), confirming the bounded asymmetry. **The only currently actionable trade across the whole book is ADBE** (score 0.0): a partial-fill position with R/R 4.47:1 and room to its 6–8% target — top up ~7 shares (~$1,366). All other BUY-band names are gated by R/R, the position cap, or a quality-gate fail. Not rescored under the modifier: TLT, XEON, RBRK, STIM (non-equity / cash-equivalent / fails gates) and VEEV (never scored). **AVGO (new this week) is also not yet rescored under the modifier** — its 69.5 score predates the 2026-06-20 framework change.

| Ticker | Weight % | Last Score | Last Review | Broker |
|--------|----------|------------|-------------|--------|
| ADBE | 3.50% | 0.0 | 20 Jun 2026 | IBKR |
| AMZN | 10.03% | 73.4 | 20 Jun 2026 | IBKR + Freedom24 |
| AVGO | 4.35% | 69.5 | 14 Jun 2026 | IBKR |
| CASH (Freedom24) | 0.19% | | | Freedom24 |
| CASH (IBKR) | 0.46% | | | IBKR |
| CSGP | 1.35% | 79.0 | 20 Jun 2026 | IBKR |
| DUOL | 8.26% | 53.7 | 20 Jun 2026 | IBKR + Freedom24 |
| GOOG | 0.65% | 73.1 | 20 Jun 2026 | IBKR |
| META | 7.22% | 18.0 | 23 Jun 2026 | IBKR + Freedom24 |
| MSFT | 15.01% | 33.9 | 26 Jun 2026 | IBKR + Freedom24 |
| NFLX | 1.66% | 61.2 | 20 Jun 2026 | IBKR |
| NKE | 1.61% | 43.1 | 20 Jun 2026 | IBKR |
| NOW | 2.02% | 42.3 | 20 Jun 2026 | IBKR |
| NVDA | 5.23% | 48.5 | 20 Jun 2026 | IBKR |
| NVO | 0.40% | 47.6 | 20 Jun 2026 | IBKR |
| RBRK | 0.38% | not scored — fails quality gates | Jun 2026 | IBKR |
| SPGI | 0.74% | 33.4 | 20 Jun 2026 | IBKR |
| SPOT | 0.84% | 80.5 | 20 Jun 2026 | IBKR |
| STIM | 0.76% | not scored — going-concern override | Jun 2026 | IBKR |
| TLT | 29.91% | not scored — non-equity, framework gap | Jun 2026 | IBKR + Freedom24 |
| UBER | 0.38% | 34.8 | 20 Jun 2026 | IBKR |
| V | 0.59% | 39.2 | 20 Jun 2026 | IBKR |
| VEEV | 0.83% | | | IBKR |
| XEON | 3.07% | not scored — cash-equivalent, out of scope | Jun 2026 | IBKR |
| ZS | 0.22% | 36.3 | 20 Jun 2026 | IBKR |

**XEON is EUR-denominated** (€1,494.33 market value). Its USD-equivalent (**$1,714.19**, used for the weight above) comes from the *live* EUR→USD rate (1.147130) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**`CASH (IBKR)`** = $255.99 USD-equivalent ($250.05 USD + €5.18 EUR — full per-currency breakdown in the [IBKR snapshot](snapshots/ibkr.md)).

**`CASH (Freedom24)`** = $106.85 (single-currency, USD — no FX conversion needed; unchanged since the 2026-06-07 Freedom Finance sync, no new screenshot this round). It ties out exactly: $15,016.69 (positions) + $106.85 (cash) = $15,123.54 (Net Asset Valuation) — see the [Freedom Finance snapshot](snapshots/freedom-finance.md) for the cross-check.

**Combined positions across both brokers:** AMZN, DUOL, META, MSFT, and TLT are each held in both IBKR and Freedom Finance — their weights above are the *sum* of both brokers' USD-equivalent market values. All other equity tickers are IBKR-only; both `CASH` rows are naturally broker-specific.

**AVGO has a prior, untracked history on this account:** `get_account_trades` shows a 1-share AVGO position sold on 2026-05-26 (predating this framework's records), which is what the now-superseded "AVGO no longer appears in either broker account" placeholder note (removed this sync) was referring to. The 6-share position now held is a fresh, separate buy from 2026-06-16 — see the override flag above.

*Run `/sync-portfolio` (see [sync-sop.md](sync-sop.md)) to refresh weights/cash/brokers from the live [snapshots](snapshots/); run `/rescore` to populate score and review-date columns (including VEEV, never scored, and AVGO, due for a rescore under the current Upside/Downside Modifier).*

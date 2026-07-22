# Current Holdings

> Source of truth for what's actually owned. Update after every [portfolio sync](sync-sop.md) or trade. Each entry should carry the last valuation score and review date so [/rescore](../.claude/commands/rescore.md) knows what's due.

**As of 2026-07-20 — live sync from [IBKR](snapshots/ibkr.md) (positions, cash balances, and active orders all refreshed 2026-07-20) + [Freedom Finance](snapshots/freedom-finance.md) snapshot (last synced 2026-06-07, unchanged this run), including cash balances on both sides.**

Combined total ≈ **$59,142.82** = IBKR Net Liquidation Value $44,019.28 + Freedom24 Net Asset Valuation $15,123.54 (both broker-reported, **positions + cash**, in USD). Weight % = each row's combined USD-equivalent value ÷ this total. *Score and review-date columns are intentionally blank — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.*

> ## No new undocumented position changes this sync
>
> All 28 IBKR positions matched the 2026-07-12 sync exactly in share count — only prices moved. The open governance items from 2026-07-12 (META's unauthorized -1 share trim, DOCS's unauthorized short put, RGL's still-unevaluated fully-filled position, MBGL) remain open and untouched — see [override-log.md](override-log.md), unchanged this sync.
>
> **New this sync:** the AMZN bracket orders (SELL 10 @ $259.25 / BUY 10 @ $210.25, flagged as undocumented 2026-07-12) have disappeared from `get_account_orders` entirely — not filled (AMZN position unchanged at 12 shares), not `REPLACED`, just absent. Likely a direct TWS/Client Portal cancellation, unconfirmed. IBKR cash is essentially flat (–$261.96 → –$264.11). Full detail in [ibkr.md](snapshots/ibkr.md) and [ibkr-orders.md](snapshots/ibkr-orders.md).
>
> This week's [weekly brief](../sessions/weekly-briefs/2026-07-20-weekly-brief.md) has the full summary.

> **AVGO's 2026-06-16 override is still marked "Open — under review" in [override-log.md](override-log.md)** despite having been resolved via the 2026-07-04 full rescore — carried forward as an open housekeeping item, not corrected this pass (outside `/sync-portfolio`'s scope).

> **Weight column sums to ~100.4%, not 100%** — see the "Note on Gross Position Value vs. Net Liquidation" in [ibkr.md](snapshots/ibkr.md) for the live-vs-settled timing gaps, plus the STIM short-call market value (–$48.15) and the DOCS short-put market value (–$65.00), both intentionally excluded from any weight below. Not a calculation error — flagged for transparency rather than silently rescaled.

**Score scale (2026-06-11):** Valuation scores run **0.0–100.0** (continuous, 0 = cheapest, 100.0 = most expensive) instead of the old 1–10 integers — see [valuation-scoring.md](../framework/valuation-scoring.md) and [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md).

**Boundary-name rescore (2026-06-20):** the 8 holdings sitting in the 50–63 "Hold/watchlist" band were re-scored with fresh Rule 0 live prices under the new **Upside/Downside Modifier** (see [decisions/2026-06-20-framework-change-upside-downside-modifier.md](../decisions/2026-06-20-framework-change-upside-downside-modifier.md) and the per-ticker `sessions/2026-06-20-rescore-*.md` logs). Seven of the eight dropped a full band into the BUY zone once expected forward return was folded in (MSFT 51.2→35.0, UBER 52.9→34.8, V 54.9→39.2, NOW 59.3→42.3, ZS 61.1→36.3, NVDA 62.2→48.5); DUOL (55.6→50.7) and NFLX (63.2→61.2) stayed in HOLD. **Important:** a BUY-band *score* is not a BUY *order* — every one of the seven is currently blocked from adding by an independent gate (sub-2:1 risk/reward, the 15% position cap, or a Phase 01 quality-gate fail for ZS). No trades were executed; these are score/action-band updates only.

**Full scored-book rescore complete (2026-06-20).** The remaining 9 scored equities were also rescored under the modifier (per-ticker `sessions/2026-06-20-rescore-*.md`): ADBE 5.0→0.0, META 38.5→19.6, SPGI 43.3→33.4, NKE 34.1→43.1, NVO 35.8→47.6, AMZN 79.8→73.4, GOOG 83.7→73.1, CSGP 83.3→79.0, SPOT 82.0→80.5. The four richly-valued names (AMZN, GOOG, CSGP, SPOT) stayed in the trim bands — the modifier correctly did **not** rescue them (their forward return only modestly cleared the hurdle), confirming the bounded asymmetry. **The only currently actionable trade across the whole book is ADBE** (score 0.0): a partial-fill position with R/R 4.47:1 and room to its 6–8% target — top up ~7 shares (~$1,366). All other BUY-band names are gated by R/R, the position cap, or a quality-gate fail. Not rescored under the modifier: TLT, XEON, RBRK, STIM (non-equity / cash-equivalent / fails gates) and VEEV (never scored). **AVGO (new this week) is also not yet rescored under the modifier** — its 69.5 score predates the 2026-06-20 framework change.

**Quality Score / Composite Score columns added 2026-06-29** (see [decisions/2026-06-29-framework-change-quality-score-and-composite.md](../decisions/2026-06-29-framework-change-quality-score-and-composite.md) and [quality-scoring.md](../framework/quality-scoring.md)) — every row that carries a numeric Last Score predates this change and does not yet have a Quality Score computed, so both new columns are marked **`?`** (never invented/backfilled) until that ticker's next `/rescore` pass fills them in. Rows already "not scored" (cash, non-equity, quality-gate fail, overrides) are left blank — there is nothing for the new columns to invalidate.

| Ticker | Weight % | Last Score | Quality Score | Composite Score | Last Review | Broker |
|--------|----------|------------|----------------|------------------|-------------|--------|
| ADBE | 4.01% | 0.0 | 83.9 | 8.1 | 04 Jul 2026 | IBKR |
| AMZN | 9.60% | 81.8 | 57.6 | 62.1 | 04 Jul 2026 | IBKR + Freedom24 |
| AVGO | 3.80% | 68.2 | 82.1 | 43.1 | 04 Jul 2026 | IBKR |
| CASH (Freedom24) | 0.18% | | | | | Freedom24 |
| CASH (IBKR) | -0.45% | | | | | IBKR |
| CSGP | 1.26% | 80.5 | 68.4 | 56.1 | 04 Jul 2026 | IBKR |
| **DOCS (short put)** | n/a — not an equity position, see note above | not scored — ungoverned position | | | n/a | IBKR |
| DUOL | 8.25% | 56.6 | 83.8 | 36.4 | 04 Jul 2026 | IBKR + Freedom24 |
| GOOG | 0.59% | 64.2 | 71.4 | 46.4 | 22 Jul 2026 | IBKR |
| **MBGL** | 0.03% | not scored — ungoverned position, see note above | | | n/a | IBKR |
| META | 6.45% | 45.0 | 90.0 | 27.5 | 13 Jul 2026 | IBKR + Freedom24 |
| MSFT | 14.74% | 35.5 | 78.3 | 28.6 | 05 Jul 2026 | IBKR + Freedom24 |
| NFLX | 1.40% | 49.3 | 69.8 | 39.8 | 17 Jul 2026 | IBKR |
| NKE | 1.48% | 13.9 | 44.4 | 34.8 | 1 Jul 2026 | IBKR |
| NOW | 2.11% | 61.3 | 78.7 | 41.3 | 05 Jul 2026 | IBKR |
| NVDA | 6.56% | 34.3 | 91.7 | 21.3 | 05 Jul 2026 | IBKR |
| NVO | 0.43% | 61.4 | 66.2 | 47.6 | 05 Jul 2026 | IBKR |
| RBRK | 0.40% | not scored — fails quality gates | | | Jun 2026 | IBKR |
| **RGL** | 0.53% | not scored — ungoverned position, see note above | | | n/a | IBKR |
| SPGI | 0.76% | 36.3 | 67.1 | 34.6 | 05 Jul 2026 | IBKR |
| SPOT | 0.81% | 84.2 | 73.2 | 55.5 | 05 Jul 2026 | IBKR |
| STIM | 1.37% | not scored — going-concern override | | | Jun 2026 | IBKR |
| TLT | 27.93% | not scored — non-equity, framework gap | | | Jun 2026 | IBKR + Freedom24 |
| TRN | 3.06% | 10.0 | 67.2 | 21.4 | 05 Jul 2026 | IBKR |
| UBER | 0.37% | 39.4 | 61.0 | 39.2 | 14 Jul 2026 | IBKR |
| V | 0.61% | 44.5 | 85.9 | 29.3 | 05 Jul 2026 | IBKR |
| VEEV | 0.99% | 45.1 | 85.7 | 29.7 | 01 Jul 2026 | IBKR |
| XEON | 2.89% | not scored — cash-equivalent, out of scope | | | Jun 2026 | IBKR |
| ZS | 0.25% | 43.1 | 59.4 | 41.9 | 05 Jul 2026 | IBKR |

**XEON is EUR-denominated** (€1,496.73 market value). Its USD-equivalent (**$1,712.15**, used for the weight above) comes from the *live* EUR→USD rate (1.14392485) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**TRN is GBP-denominated** (£1,346.40 market value, LSE). Its USD-equivalent (**$1,811.55**, used for the weight above) comes from the *live* GBP→USD rate (1.34547875) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**RGL is AUD-denominated** (AUD $450.00 market value, ASX — down slightly from AUD $480.00 last sync, price -6.25%, share count unchanged at 60,000). Its USD-equivalent (**$313.96**, used for the weight above) comes from the *live* AUD→USD rate (0.6977) returned by IBKR's `get_account_balances` — broker-reported, not assumed. No Phase 01/02 evaluation exists for this ticker.

**STIM's weight above (1.37%) reflects the 500-share equity position only** ($810.00). A short 5-contract covered call (`STIM Aug21'26 $2.50 CALL`, market value –$48.15) is also held against this position — see [ibkr.md](snapshots/ibkr.md) for detail. Not folded into the weight % here; at ~0.08% of the combined total it would not change STIM's banding either way.

**DOCS's short put (`DOCS Aug21'26 $17.5 PUT`, market value –$65.00) has no equity position to attach a weight to** — see [override-log.md](override-log.md). Tracked in full in [ibkr.md](snapshots/ibkr.md).

**`CASH (IBKR)`** = **–$264.11** USD-equivalent (–$58.82 USD + €227.49 EUR ≈ +$260.23 + £0.00 GBP ≈ $0.00 − AUD $666.43 ≈ −$464.97, net of rounding — full per-currency breakdown in the [IBKR snapshot](snapshots/ibkr.md)). Essentially flat vs. last sync (–$261.96 → –$264.11) — no new large swing this week.

**`CASH (Freedom24)`** = $106.85 (single-currency, USD — no FX conversion needed; unchanged since the 2026-06-07 Freedom Finance sync, no new screenshot this round). It ties out exactly: $15,016.69 (positions) + $106.85 (cash) = $15,123.54 (Net Asset Valuation) — see the [Freedom Finance snapshot](snapshots/freedom-finance.md) for the cross-check.

**Combined positions across both brokers:** AMZN, DUOL, META, MSFT, and TLT are each held in both IBKR and Freedom Finance — their weights above are the *sum* of both brokers' USD-equivalent market values. All other equity tickers are IBKR-only; both `CASH` rows are naturally broker-specific.

**AVGO has a prior, untracked history on this account:** `get_account_trades` shows a 1-share AVGO position sold on 2026-05-26 (predating this framework's records), which is what the now-superseded "AVGO no longer appears in either broker account" placeholder note (removed this sync) was referring to. The 6-share position now held is a fresh, separate buy from 2026-06-16 — see the override flag above.

*Run `/sync-portfolio` (see [sync-sop.md](sync-sop.md)) to refresh weights/cash/brokers from the live [snapshots](snapshots/); run `/rescore` to populate score and review-date columns (VEEV scored 2026-07-01 — see [session](../sessions/2026-07-01-rescore-veev.md); AVGO rescored 2026-07-04, current — see [session](../sessions/2026-07-04-rescore-avgo.md)).*

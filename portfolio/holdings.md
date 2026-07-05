# Current Holdings

> Source of truth for what's actually owned. Update after every [portfolio sync](sync-sop.md) or trade. Each entry should carry the last valuation score and review date so [/rescore](../.claude/commands/rescore.md) knows what's due.

**As of 2026-06-28 — live sync from [IBKR](snapshots/ibkr.md) (positions, cash balances, and active orders all refreshed 2026-06-28) + [Freedom Finance](snapshots/freedom-finance.md) snapshot (last synced 2026-06-07, unchanged this run), including cash balances on both sides.**

Combined total ≈ **$54,891.48** = IBKR Net Liquidation Value $39,767.94 + Freedom24 Net Asset Valuation $15,123.54 (both broker-reported, **positions + cash**, in USD). Weight % = each row's combined USD-equivalent value ÷ this total. *Score and review-date columns are intentionally blank — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.*

> ⚠️ **Portfolio changes since the 2026-06-22 sync:**
>
> - **New position — TRN** (Trainline plc, LSE: 600 sh @ avg cost GBP 2.1195 ≈ GBX 211.95, IBKR, bought 2026-06-24): **framework-compliant partial-fill BUY, not an override.** [watchlist/in-portfolio/TRN/TRN-2026-06-24.md](../watchlist/in-portfolio/TRN/TRN-2026-06-24.md) carries a score of **10.0 — BUY, Full position 6–8%**, from a Rule 9 management-change re-run (Trainline CEO succession). Target size from [sessions/2026-06-24-new-position-trn.md](../sessions/2026-06-24-new-position-trn.md) is ≈1,553 shares (≈$4,191.30); 600 filled so far — same partial-fill pattern already established for ADBE. Added below with Last Score 10.0 / 24 Jun 2026 carried over from that session. Moved `watchlist/not-in-portfolio/TRN/` → `watchlist/in-portfolio/TRN/`.
> - **Total Cash (IBKR) swung from +$255.99 to –$1,576.85** — the TRN purchase was funded by letting **GBP cash go negative** (–£1,271.71, GBP-side NLV now slightly negative) rather than via an explicit FX conversion; see [ibkr.md](snapshots/ibkr.md) for detail. Flagged for transparency — not a framework violation, but worth a deliberate decision on whether to convert USD→GBP to cover it.
> - **STIM grew (345→500 shares) and a new 5-contract short covered call appeared** (`STIM Aug21'26 $2.50 CALL`, –5 contracts): both fills resolve order-window flags already on record from the 2026-06-22 sync and are consistent with the ongoing covered-call income strategy (fully covered by the 500-share position). Not a new governance flag — see the STIM note below and [ibkr.md](snapshots/ibkr.md).
> - **AVGO's 2026-06-16 override remains open and unresolved** (no rationale supplied yet) — see [override-log.md](override-log.md). Carried forward, not re-litigated this sync.
> - **No other position-size changes** — all other previously-held tickers (including ADBE, still a partial fill at 10 of ~17 target shares) show identical share counts; only prices moved.

> **Weight column sums to ~100.1%, not 100%** — see the "Note on Gross Position Value vs. Net Liquidation" in [ibkr.md](snapshots/ibkr.md) for the small live-vs-settled timing gaps, plus the STIM short-call market value (–$45.55) which is intentionally excluded from STIM's weight below. Not a calculation error — flagged for transparency rather than silently rescaled.

**Score scale (2026-06-11):** Valuation scores run **0.0–100.0** (continuous, 0 = cheapest, 100.0 = most expensive) instead of the old 1–10 integers — see [valuation-scoring.md](../framework/valuation-scoring.md) and [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md).

**Boundary-name rescore (2026-06-20):** the 8 holdings sitting in the 50–63 "Hold/watchlist" band were re-scored with fresh Rule 0 live prices under the new **Upside/Downside Modifier** (see [decisions/2026-06-20-framework-change-upside-downside-modifier.md](../decisions/2026-06-20-framework-change-upside-downside-modifier.md) and the per-ticker `sessions/2026-06-20-rescore-*.md` logs). Seven of the eight dropped a full band into the BUY zone once expected forward return was folded in (MSFT 51.2→35.0, UBER 52.9→34.8, V 54.9→39.2, NOW 59.3→42.3, ZS 61.1→36.3, NVDA 62.2→48.5); DUOL (55.6→50.7) and NFLX (63.2→61.2) stayed in HOLD. **Important:** a BUY-band *score* is not a BUY *order* — every one of the seven is currently blocked from adding by an independent gate (sub-2:1 risk/reward, the 15% position cap, or a Phase 01 quality-gate fail for ZS). No trades were executed; these are score/action-band updates only.

**Full scored-book rescore complete (2026-06-20).** The remaining 9 scored equities were also rescored under the modifier (per-ticker `sessions/2026-06-20-rescore-*.md`): ADBE 5.0→0.0, META 38.5→19.6, SPGI 43.3→33.4, NKE 34.1→43.1, NVO 35.8→47.6, AMZN 79.8→73.4, GOOG 83.7→73.1, CSGP 83.3→79.0, SPOT 82.0→80.5. The four richly-valued names (AMZN, GOOG, CSGP, SPOT) stayed in the trim bands — the modifier correctly did **not** rescue them (their forward return only modestly cleared the hurdle), confirming the bounded asymmetry. **The only currently actionable trade across the whole book is ADBE** (score 0.0): a partial-fill position with R/R 4.47:1 and room to its 6–8% target — top up ~7 shares (~$1,366). All other BUY-band names are gated by R/R, the position cap, or a quality-gate fail. Not rescored under the modifier: TLT, XEON, RBRK, STIM (non-equity / cash-equivalent / fails gates) and VEEV (never scored). **AVGO (new this week) is also not yet rescored under the modifier** — its 69.5 score predates the 2026-06-20 framework change.

**Quality Score / Composite Score columns added 2026-06-29** (see [decisions/2026-06-29-framework-change-quality-score-and-composite.md](../decisions/2026-06-29-framework-change-quality-score-and-composite.md) and [quality-scoring.md](../framework/quality-scoring.md)) — every row that carries a numeric Last Score predates this change and does not yet have a Quality Score computed, so both new columns are marked **`?`** (never invented/backfilled) until that ticker's next `/rescore` pass fills them in. Rows already "not scored" (cash, non-equity, quality-gate fail, overrides) are left blank — there is nothing for the new columns to invalidate.

| Ticker | Weight % | Last Score | Quality Score | Composite Score | Last Review | Broker |
|--------|----------|------------|----------------|------------------|-------------|--------|
| ADBE | 3.69% | 0.0 | 83.9 | 8.1 | 04 Jul 2026 | IBKR |
| AMZN | 9.99% | 81.8 | 57.6 | 62.1 | 04 Jul 2026 | IBKR + Freedom24 |
| AVGO | 4.01% | 68.2 | 82.1 | 43.1 | 04 Jul 2026 | IBKR |
| CASH (Freedom24) | 0.19% | | | | | Freedom24 |
| CASH (IBKR) | -2.87% | | | | | IBKR |
| CSGP | 1.38% | 80.5 | 68.4 | 56.1 | 04 Jul 2026 | IBKR |
| DUOL | 8.20% | 56.6 | 83.8 | 36.4 | 04 Jul 2026 | IBKR + Freedom24 |
| GOOG | 0.61% | 67.4 | 73.7 | 46.9 | 04 Jul 2026 | IBKR |
| META | 7.10% | 35.6 | 90.0 | 22.8 | 1 Jul 2026 | IBKR + Freedom24 |
| MSFT | 15.09% | 35.5 | 78.3 | 28.6 | 05 Jul 2026 | IBKR + Freedom24 |
| NFLX | 1.61% | 59.9 | 74.0 | 43.0 | 05 Jul 2026 | IBKR |
| NKE | 1.49% | 13.9 | 44.4 | 34.8 | 1 Jul 2026 | IBKR |
| NOW | 2.16% | 61.3 | 78.7 | 41.3 | 05 Jul 2026 | IBKR |
| NVDA | 4.92% | 34.3 | 91.7 | 21.3 | 05 Jul 2026 | IBKR |
| NVO | 0.44% | 61.4 | 66.2 | 47.6 | 05 Jul 2026 | IBKR |
| RBRK | 0.40% | not scored — fails quality gates | | | Jun 2026 | IBKR |
| SPGI | 0.74% | 36.3 | 67.1 | 34.6 | 05 Jul 2026 | IBKR |
| SPOT | 0.84% | 80.5 | ? | ? | 20 Jun 2026 | IBKR |
| STIM | 1.20% | not scored — going-concern override | | | Jun 2026 | IBKR |
| TLT | 30.53% | not scored — non-equity, framework gap | | | Jun 2026 | IBKR + Freedom24 |
| TRN | 3.04% | 10.0 | ? | ? | 24 Jun 2026 | IBKR |
| UBER | 0.42% | 34.8 | ? | ? | 20 Jun 2026 | IBKR |
| V | 0.61% | 39.2 | ? | ? | 20 Jun 2026 | IBKR |
| VEEV | 0.94% | 45.1 | 85.7 | 29.7 | 01 Jul 2026 | IBKR |
| XEON | 3.10% | not scored — cash-equivalent, out of scope | | | Jun 2026 | IBKR |
| ZS | 0.24% | 36.3 | ? | ? | 20 Jun 2026 | IBKR |

**XEON is EUR-denominated** (€1,494.81 market value). Its USD-equivalent (**$1,701.88**, used for the weight above) comes from the *live* EUR→USD rate (1.138523) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**TRN is GBP-denominated** (£1,263.60 market value, LSE). Its USD-equivalent (**$1,667.60**, used for the weight above) comes from the *live* GBP→USD rate (1.319719) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**STIM's weight above (1.20%) reflects the 500-share equity position only** ($660.00). A short 5-contract covered call (`STIM Aug21'26 $2.50 CALL`, market value –$45.55) is also held against this position — see [ibkr.md](snapshots/ibkr.md) for detail. Not folded into the weight % here; at ~0.08% of the combined total it would not change STIM's banding either way.

**`CASH (IBKR)`** = **–$1,576.85** USD-equivalent ($95.41 USD + €5.18 EUR + **–£1,271.71 GBP**, the last currently negative — full per-currency breakdown and the funding explanation in the [IBKR snapshot](snapshots/ibkr.md)).

**`CASH (Freedom24)`** = $106.85 (single-currency, USD — no FX conversion needed; unchanged since the 2026-06-07 Freedom Finance sync, no new screenshot this round). It ties out exactly: $15,016.69 (positions) + $106.85 (cash) = $15,123.54 (Net Asset Valuation) — see the [Freedom Finance snapshot](snapshots/freedom-finance.md) for the cross-check.

**Combined positions across both brokers:** AMZN, DUOL, META, MSFT, and TLT are each held in both IBKR and Freedom Finance — their weights above are the *sum* of both brokers' USD-equivalent market values. All other equity tickers are IBKR-only; both `CASH` rows are naturally broker-specific.

**AVGO has a prior, untracked history on this account:** `get_account_trades` shows a 1-share AVGO position sold on 2026-05-26 (predating this framework's records), which is what the now-superseded "AVGO no longer appears in either broker account" placeholder note (removed this sync) was referring to. The 6-share position now held is a fresh, separate buy from 2026-06-16 — see the override flag above.

*Run `/sync-portfolio` (see [sync-sop.md](sync-sop.md)) to refresh weights/cash/brokers from the live [snapshots](snapshots/); run `/rescore` to populate score and review-date columns (VEEV scored 2026-07-01 — see [session](../sessions/2026-07-01-rescore-veev.md); AVGO still due for a rescore under the current Upside/Downside Modifier).*

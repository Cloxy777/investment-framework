# Current Holdings

> Source of truth for what's actually owned. Update after every [portfolio sync](sync-sop.md) or trade. Each entry should carry the last valuation score and review date so [/rescore](../.claude/commands/rescore.md) knows what's due.

**As of 2026-08-23 — live sync from [IBKR](snapshots/ibkr.md) (positions, cash balances, and active orders all refreshed 2026-08-23) + [Freedom Finance](snapshots/freedom-finance.md) snapshot (last refreshed 2026-08-22, not resynced this round — no screenshot provided; Freedom24 sync is manual/screenshot-based, not part of this IBKR sync), including cash balances on both sides.**

Combined total ≈ **$61,101.28** = IBKR Net Liquidation Value $50,211.32 + Freedom24 implied total $10,889.96 (unchanged from 2026-08-22, positions + cash, **not** a broker-labeled "Net Asset Valuation", see prior flag in [freedom-finance.md](snapshots/freedom-finance.md)). Weight % = each row's combined USD-equivalent value ÷ this total. *Score and review-date columns are intentionally blank/unchanged — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.*

> ## Quiet sync — no share-count changes, no new fills, no cancellations
>
> All 24 IBKR positions hold identical quantities to the 2026-08-22 sync; the 7 active orders are unchanged. Only prices moved (largest since yesterday: RBRK -2.57%, AVGO +1.50%, NVDA +1.21%) — nothing crosses the Rule 9 ±15% unexplained-move threshold this window. Full detail: [ibkr.md](snapshots/ibkr.md), [ibkr-orders.md](snapshots/ibkr-orders.md).
>
> ## ⚠️ TRN still down 22.4% vs. the 08-16 sync — unchanged this week, cause remains unconfirmed
>
> Price and share count both flat since 2026-08-22 (£1.975/share, 600 shares) — no new move this sync. Already rescored 2026-08-22 (Quality Score 67.2, fails the 80.0+ gate) — HOLD, no top-up. See [ibkr.md](snapshots/ibkr.md).
>
> ## SPOT position and its sell order remain absent — now 5 consecutive syncs, still unresolved since 2026-08-02
>
> No new information this sync; still flagged for the user to confirm directly in TWS/Client Portal. Full detail in [ibkr.md](snapshots/ibkr.md) and [ibkr-orders.md](snapshots/ibkr-orders.md).
>
> ## Cash essentially flat this sync (+$0.16)
>
> IBKR USD-equiv cash: $4,060.67 → $4,060.83. No new cash-moving events (no fills, no assignments) since yesterday's sync. **The still-unresolved +$2,523.36 cash jump flagged 2026-08-09** remains open and uninvestigated.
>
> **AVGO's 2026-06-16 override is still marked "Open — under review" in [override-log.md](override-log.md)** despite having been resolved via the 2026-07-04 full rescore — carried forward as an open housekeeping item, not corrected this pass (outside `/sync-portfolio`'s scope).
>

**Score scale (2026-06-11):** Valuation scores run **0.0–100.0** (continuous, 0 = cheapest, 100.0 = most expensive) instead of the old 1–10 integers — see [valuation-scoring.md](../framework/valuation-scoring.md) and [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md).

**Quality Score / Composite Score columns added 2026-06-29** (see [decisions/2026-06-29-framework-change-quality-score-and-composite.md](../decisions/2026-06-29-framework-change-quality-score-and-composite.md) and [quality-scoring.md](../framework/quality-scoring.md)) — every row that carries a numeric Last Score predates this change and does not yet have a Quality Score computed, so both new columns are marked **`?`** (never invented/backfilled) until that ticker's next `/rescore` pass fills them in. Rows already "not scored" (cash, non-equity, quality-gate fail, overrides) are left blank — there is nothing for the new columns to invalidate.

| Ticker | Weight % | Last Score | Quality Score | Composite Score | Last Review | Broker |
|--------|----------|------------|----------------|------------------|-------------|--------|
| ADBE | 4.51% | 0.0 | 83.9 | 8.1 | 29 Jul 2026 | IBKR |
| AMZN | 5.08% | 82.7 | 56.7 | 63.0 | 01 Aug 2026 | IBKR (Freedom24 leg sold — see note above) |
| AVGO | 3.68% | 68.5 | 82.1 | 43.2 | 28 Aug 2026 | IBKR |
| CASH (Freedom24) | 0.07% | | | | | Freedom24 |
| CASH (IBKR) | 6.65% | | | | | IBKR |
| CSGP | 1.32% | 84.8 | 69.2 | 57.8 | 09 Aug 2026 | IBKR |
| **DOCS (short put)** | n/a — expired worthless 2026-08-21, position closed | n/a | | | n/a | IBKR |
| DUOL | 9.08% | 72.2 | 83.2 | 44.5 | 06 Aug 2026 | IBKR + Freedom24 |
| GOOG | 0.56% | 64.2 | 71.4 | 46.4 | 22 Jul 2026 | IBKR |
| **MBGL** | 0.03% | not scored — fails quality gates | 51.0 | | 09 Aug 2026 | IBKR |
| META | 4.51% | 39.4 | 87.5 | 26.0 | 26 Aug 2026 (PM) | IBKR (Freedom24 leg sold — see note above) |
| MSFT | 13.45% | 38.9 | 79.9 | 29.5 (ref only, gate fail) | 30 Jul 2026 | IBKR (Freedom24 leg sold — see note above) |
| NFLX | 1.56% | 49.3 | 69.8 | 39.8 | 17 Jul 2026 | IBKR |
| NKE | 1.33% | 13.9 | 44.4 | 34.8 | 1 Jul 2026 | IBKR |
| NOW | 1.89%⚠️ | 75.9 | 73.2 | 51.4 (ref only, gate fail) | 09 Aug 2026 | IBKR |
| NVDA | 6.78% | 41.2 | 90.3 | 25.5 | 27 Aug 2026 | IBKR |
| NVO | 0.38% | 51.4 | 67.2 | 42.1 (ref only, gate fail) | 09 Aug 2026 | IBKR |
| RBRK | 0.48% | not scored — fails quality gates | | | Jun 2026 | IBKR |
| **RGL** | 0.70% | not scored — ungoverned position, see note above | | | n/a | IBKR |
| SPGI | 0.71% | 31.3 | 67.7 | 31.8 | 09 Aug 2026 | IBKR |
| TLT | 29.27% | not scored — non-equity, framework gap | | | Jun 2026 | IBKR + Freedom24 |
| TRN | 2.65%⚠️ | 10.0 | 67.2 | 21.4 (ref only, gate fail) | 22 Aug 2026 | IBKR |
| UBER | 0.39% | 43.6 | 55.5 | 44.1 | 07 Aug 2026 | IBKR |
| V | 0.61% | 54.5 | 85.6 | 34.5 | 29 Jul 2026 | IBKR |
| VEEV | 1.22% | 65.9 | 86.0 | 40.0 | 30 Aug 2026 | IBKR |
| XEON | 2.87% | not scored — cash-equivalent, out of scope | | | Jun 2026 | IBKR |
| ZS | 0.30% | 43.1 | 59.4 | 41.9 | 05 Jul 2026 | IBKR |

**STIM (previously 2.47%) removed this sync** — position fully exited via forced option assignment, see flag above. Moved to `watchlist/not-in-portfolio/STIM/`.

**SPOT (previously 0.83%) remains absent from this table** — its 1-share position has now been missing for four consecutive syncs (2026-08-02, 08-09, 08-16, 08-22), undocumented; see the flag above and [ibkr.md](snapshots/ibkr.md).

**MSFT's weight (13.45%) is now IBKR-only** — the 2-share Freedom24 leg was sold (confirmed, see flag above). Composite Score for MSFT remains a reference figure only (not adopted) — its Quality Score (79.9) fails the 80.0+ gate by 0.1 point.

**NOW's weight (⚠️) still carries the 2026-08-10 undocumented 3-share trim** — unresolved, see [override-log.md](override-log.md).

**TRN's weight (⚠️) still reflects the 22.4% price drop from the 08-16→08-22 window** — caused by a CMA "drip pricing" investigation opened 2026-08-19 (see [2026-08-22 rescore](../sessions/2026-08-22-rescore-trn.md)); price unchanged this sync. Quality Score 67.2 still fails the 80.0+ gate, Composite 21.4 reference-only. **HOLD, no top-up** — Quality Gate already blocked adding before this news; the CMA probe adds a second, independent reason.

**XEON is EUR-denominated** (€1,500.20 market value). Its USD-equivalent (**$1,752.08**, used for the weight above) comes from the *live* EUR→USD rate (1.1678947) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**TRN is GBP-denominated** (£1,185.00 market value, LSE — unchanged from last sync, share count unchanged at 600). Its USD-equivalent (**$1,616.91**, used for the weight above) comes from the *live* GBP→USD rate (1.3644824) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**RGL is AUD-denominated** (AUD $600.00 market value, ASX — unchanged from last sync, share count unchanged at 60,000). Its USD-equivalent (**$430.27**, used for the weight above) comes from the *live* AUD→USD rate (0.7171154) returned by IBKR's `get_account_balances` — broker-reported, not assumed. No Phase 01/02 evaluation exists for this ticker.

**`CASH (IBKR)`** = **$4,060.83** USD-equivalent ($4,274.70 USD + €227.49 EUR ≈ +$265.68 + £0.00 GBP ≈ $0.00 − AUD $668.95 ≈ −$479.72, net of rounding — full per-currency breakdown in the [IBKR snapshot](snapshots/ibkr.md)). Essentially flat vs. $4,060.67 last sync (+$0.16) — no new cash-moving events.

**`CASH (Freedom24)`** = $44.98 (unchanged — not resynced this round, no screenshot provided; single-currency USD, no FX conversion needed).

**Combined positions across both brokers:** DUOL and TLT are held in both IBKR and Freedom Finance (weights = sum of both, using the last-synced Freedom24 figures from 2026-08-22: DUOL $1,165.44, TLT $9,679.54). AMZN, META, and MSFT are IBKR-only (Freedom24 legs sold, confirmed 2026-08-22). All other equity tickers are IBKR-only; both `CASH` rows are naturally broker-specific.

**AVGO has a prior, untracked history on this account:** `get_account_trades` shows a 1-share AVGO position sold on 2026-05-26 (predating this framework's records), which is what the now-superseded "AVGO no longer appears in either broker account" placeholder note (removed in a prior sync) was referring to. The 6-share position now held is a fresh, separate buy from 2026-06-16 — see the override flag in [override-log.md](override-log.md).

*Run `/sync-portfolio` (see [sync-sop.md](sync-sop.md)) to refresh weights/cash/brokers from the live [snapshots](snapshots/); run `/rescore` to populate score and review-date columns (VEEV scored 2026-07-01 — see [session](../sessions/2026-07-01-rescore-veev.md); AVGO rescored 2026-07-04, current — see [session](../sessions/2026-07-04-rescore-avgo.md)).*

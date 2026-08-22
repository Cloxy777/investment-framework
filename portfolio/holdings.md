# Current Holdings

> Source of truth for what's actually owned. Update after every [portfolio sync](sync-sop.md) or trade. Each entry should carry the last valuation score and review date so [/rescore](../.claude/commands/rescore.md) knows what's due.

**As of 2026-08-22 — live sync from [IBKR](snapshots/ibkr.md) (positions, cash balances, and active orders all refreshed 2026-08-22) + [Freedom Finance](snapshots/freedom-finance.md) snapshot (refreshed 2026-08-22, but incomplete — see flag below), including cash balances on both sides.**

Combined total ≈ **$61,101.89** = IBKR Net Liquidation Value $50,211.93 + Freedom24 implied total $10,889.96 (positions + cash, cash+positions only — **not** a broker-labeled "Net Asset Valuation" this round, see flag below). Weight % = each row's combined USD-equivalent value ÷ this total. *Score and review-date columns are intentionally blank/unchanged — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.*

> ## ⚠️ STIM exited via forced option assignment, 2026-08-21 expiry — not a deliberate sale, [issue #522](https://github.com/cloxy777/investment-framework/issues/522) now moot
>
> The 500-share equity position and the -5 short covered calls (Aug21'26 $2.50 strike) both closed 2026-08-22T05:46:02Z via IBKR's expiry-assignment processing: the calls were deep ITM (stock ~$3.02–3.25 vs. $2.50 strike after the 08-11 earnings beat), so the shares were called away at $2.50 — roughly $0.52–0.75/share below live market. Net proceeds $1,250.00. **This mechanically resolves the open [2026-08-09 EXIT recommendation](../sessions/2026-08-09-exit-review-stim.md) by elimination, not by execution** — no `decisions/` entry authorized it. STIM is removed from the table below and moved to `watchlist/not-in-portfolio/`. Full detail and the governance note: [ibkr.md](snapshots/ibkr.md), [override-log.md](override-log.md).
>
> ## ✅ DOCS short put expired worthless 2026-08-21 — full premium kept
>
> No assignment; DOCS traded well above the $17.50 strike. Resolves the open `override-log.md` DOCS entry cleanly. See [ibkr.md](snapshots/ibkr.md).
>
> ## ⚠️ TRN down 22.4% since the 08-16 sync (£2.544 → £1.975/share) — Rule 9 threshold breached, cause unconfirmed
>
> Share count unchanged (600); this is a price move, not a trade. Past the ±15% Rule 9 "unexplained move" trigger — this sync didn't pull news, so the cause is unverified. **Flagging for investigation/rescore**, not diagnosing here. See [ibkr.md](snapshots/ibkr.md).
>
> ## ✅ Freedom24: MSFT, META, AMZN confirmed sold — user-confirmed 2026-08-22, undocumented trade
>
> The account's Freedom24 positions dropped from 5 tickers ($15,016.69) to 2 (DUOL, TLT — $10,844.98). User confirmed directly this sync that MSFT, META, and AMZN were sold — not a screenshot gap. No fill dates/prices/P&L available (no trade-history API), and **no `sessions/`/`decisions/`/`override-log` entry authorized it** — logged to [override-log.md](override-log.md) as an undocumented trade, same pattern as the IBKR NOW/META trims. **MSFT/META/AMZN weights below are now IBKR-only** (Freedom24 leg exited, not a data gap). Cash still doesn't reconcile with the implied ~$4,000+ proceeds — see [freedom-finance.md](snapshots/freedom-finance.md).
>
> ## SPOT position and its sell order remain absent — unchanged, still unresolved since 2026-08-02
>
> No new information this sync; still flagged for the user to confirm directly in TWS/Client Portal. Full detail in [ibkr.md](snapshots/ibkr.md) and [ibkr-orders.md](snapshots/ibkr-orders.md).
>
> ## Cash rose $1,246.69 this sync — mostly the STIM assignment proceeds
>
> IBKR USD cash: $3,024.82 → $4,274.70. The $1,250.00 STIM assignment (see above) accounts for nearly all of it; the small remainder isn't itemized. **The separate, still-unresolved +$2,523.36 cash jump flagged 2026-08-09** remains open and uninvestigated — not the same event.
>
> **AVGO's 2026-06-16 override is still marked "Open — under review" in [override-log.md](override-log.md)** despite having been resolved via the 2026-07-04 full rescore — carried forward as an open housekeeping item, not corrected this pass (outside `/sync-portfolio`'s scope).
>

**Score scale (2026-06-11):** Valuation scores run **0.0–100.0** (continuous, 0 = cheapest, 100.0 = most expensive) instead of the old 1–10 integers — see [valuation-scoring.md](../framework/valuation-scoring.md) and [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md).

**Quality Score / Composite Score columns added 2026-06-29** (see [decisions/2026-06-29-framework-change-quality-score-and-composite.md](../decisions/2026-06-29-framework-change-quality-score-and-composite.md) and [quality-scoring.md](../framework/quality-scoring.md)) — every row that carries a numeric Last Score predates this change and does not yet have a Quality Score computed, so both new columns are marked **`?`** (never invented/backfilled) until that ticker's next `/rescore` pass fills them in. Rows already "not scored" (cash, non-equity, quality-gate fail, overrides) are left blank — there is nothing for the new columns to invalidate.

| Ticker | Weight % | Last Score | Quality Score | Composite Score | Last Review | Broker |
|--------|----------|------------|----------------|------------------|-------------|--------|
| ADBE | 4.50% | 0.0 | 83.9 | 8.1 | 29 Jul 2026 | IBKR |
| AMZN | 5.10% | 82.7 | 56.7 | 63.0 | 01 Aug 2026 | IBKR (Freedom24 leg sold — see note above) |
| AVGO | 3.62% | 68.2 | 82.1 | 43.1 | 04 Jul 2026 | IBKR |
| CASH (Freedom24) | 0.07% | | | | | Freedom24 |
| CASH (IBKR) | 6.65% | | | | | IBKR |
| CSGP | 1.34% | 84.8 | 69.2 | 57.8 | 09 Aug 2026 | IBKR |
| **DOCS (short put)** | n/a — expired worthless 2026-08-21, position closed | n/a | | | n/a | IBKR |
| DUOL | 9.06% | 72.2 | 83.2 | 44.5 | 06 Aug 2026 | IBKR + Freedom24 |
| GOOG | 0.56% | 64.2 | 71.4 | 46.4 | 22 Jul 2026 | IBKR |
| **MBGL** | 0.03% | not scored — fails quality gates | 51.0 | | 09 Aug 2026 | IBKR |
| META | 4.52% | 41.2 | 87.5 | 26.9 | 05 Aug 2026 | IBKR (Freedom24 leg sold — see note above) |
| MSFT | 13.45% | 38.9 | 79.9 | 29.5 (ref only, gate fail) | 30 Jul 2026 | IBKR (Freedom24 leg sold — see note above) |
| NFLX | 1.56% | 49.3 | 69.8 | 39.8 | 17 Jul 2026 | IBKR |
| NKE | 1.33% | 13.9 | 44.4 | 34.8 | 1 Jul 2026 | IBKR |
| NOW | 1.88%⚠️ | 75.9 | 73.2 | 51.4 (ref only, gate fail) | 09 Aug 2026 | IBKR |
| NVDA | 6.70% | 34.3 | 91.7 | 21.3 | 05 Jul 2026 | IBKR |
| NVO | 0.38% | 51.4 | 67.2 | 42.1 (ref only, gate fail) | 09 Aug 2026 | IBKR |
| RBRK | 0.49% | not scored — fails quality gates | | | Jun 2026 | IBKR |
| **RGL** | 0.70% | not scored — ungoverned position, see note above | | | n/a | IBKR |
| SPGI | 0.71% | 31.3 | 67.7 | 31.8 | 09 Aug 2026 | IBKR |
| TLT | 29.27% | not scored — non-equity, framework gap | | | Jun 2026 | IBKR + Freedom24 |
| TRN | 2.65%⚠️ | 10.0 | 67.2 | 21.4 | 05 Jul 2026 | IBKR |
| UBER | 0.39% | 43.6 | 55.5 | 44.1 | 07 Aug 2026 | IBKR |
| V | 0.61% | 54.5 | 85.6 | 34.5 | 29 Jul 2026 | IBKR |
| VEEV | 1.22% | 45.1 | 85.7 | 29.7 | 01 Jul 2026 | IBKR |
| XEON | 2.87% | not scored — cash-equivalent, out of scope | | | Jun 2026 | IBKR |
| ZS | 0.30% | 43.1 | 59.4 | 41.9 | 05 Jul 2026 | IBKR |

**STIM (previously 2.47%) removed this sync** — position fully exited via forced option assignment, see flag above. Moved to `watchlist/not-in-portfolio/STIM/`.

**SPOT (previously 0.83%) remains absent from this table** — its 1-share position has now been missing for four consecutive syncs (2026-08-02, 08-09, 08-16, 08-22), undocumented; see the flag above and [ibkr.md](snapshots/ibkr.md).

**MSFT's weight (13.45%) is now IBKR-only** — the 2-share Freedom24 leg was sold (confirmed, see flag above). Composite Score for MSFT remains a reference figure only (not adopted) — its Quality Score (79.9) fails the 80.0+ gate by 0.1 point.

**NOW's weight (⚠️) still carries the 2026-08-10 undocumented 3-share trim** — unresolved, see [override-log.md](override-log.md).

**TRN's weight (⚠️) reflects a 22.4% price drop since the last sync** — see flag above, not a share-count change.

**XEON is EUR-denominated** (€1,499.83 market value). Its USD-equivalent (**$1,751.64**, used for the weight above) comes from the *live* EUR→USD rate (1.1678947) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**TRN is GBP-denominated** (£1,185.00 market value, LSE — down from £1,526.40 last sync, price -22.4%, share count unchanged at 600). Its USD-equivalent (**$1,616.91**, used for the weight above) comes from the *live* GBP→USD rate (1.3644824) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**RGL is AUD-denominated** (AUD $600.00 market value, ASX — unchanged from last sync, share count unchanged at 60,000). Its USD-equivalent (**$430.27**, used for the weight above) comes from the *live* AUD→USD rate (0.7171154) returned by IBKR's `get_account_balances` — broker-reported, not assumed. No Phase 01/02 evaluation exists for this ticker.

**`CASH (IBKR)`** = **$4,060.67** USD-equivalent ($4,274.70 USD + €227.49 EUR ≈ +$265.68 + £0.00 GBP ≈ $0.00 − AUD $668.95 ≈ −$479.72, net of rounding — full per-currency breakdown in the [IBKR snapshot](snapshots/ibkr.md)). Up from $2,813.98 last sync (+$1,246.69) — mostly the STIM assignment proceeds, see flag above.

**`CASH (Freedom24)`** = $44.98 (single-currency, USD — no FX conversion needed). Down from $106.85 last sync (-$61.87) — see the Freedom24 anomaly flag above; this drop is part of what makes a simple "MSFT/META/AMZN were sold" explanation incomplete (sale proceeds would be expected to raise cash, not lower it).

**Combined positions across both brokers:** DUOL and TLT are held in both IBKR and Freedom Finance (weights = sum of both). AMZN, META, and MSFT were combined-broker through the 2026-08-16 sync but their Freedom24 legs were sold (confirmed 2026-08-22, see flag above) — now IBKR-only. All other equity tickers are IBKR-only; both `CASH` rows are naturally broker-specific.

**AVGO has a prior, untracked history on this account:** `get_account_trades` shows a 1-share AVGO position sold on 2026-05-26 (predating this framework's records), which is what the now-superseded "AVGO no longer appears in either broker account" placeholder note (removed in a prior sync) was referring to. The 6-share position now held is a fresh, separate buy from 2026-06-16 — see the override flag in [override-log.md](override-log.md).

*Run `/sync-portfolio` (see [sync-sop.md](sync-sop.md)) to refresh weights/cash/brokers from the live [snapshots](snapshots/); run `/rescore` to populate score and review-date columns (VEEV scored 2026-07-01 — see [session](../sessions/2026-07-01-rescore-veev.md); AVGO rescored 2026-07-04, current — see [session](../sessions/2026-07-04-rescore-avgo.md)).*

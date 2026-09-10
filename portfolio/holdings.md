# Current Holdings

> Source of truth for what's actually owned. Update after every [portfolio sync](sync-sop.md) or trade. Each entry should carry the last valuation score and review date so [/rescore](../.claude/commands/rescore.md) knows what's due.

**As of 2026-09-06 — live sync from [IBKR](snapshots/ibkr.md) (positions, cash balances, and active orders all refreshed 2026-09-06) + [Freedom Finance](snapshots/freedom-finance.md) snapshot (last refreshed 2026-08-22, not resynced this round — no screenshot provided; Freedom24 sync is manual/screenshot-based, not part of this IBKR sync), including cash balances on both sides.**

Combined total ≈ **$62,135.17** = IBKR Net Liquidation Value $51,245.21 + Freedom24 implied total $10,889.96 (unchanged from 2026-08-22, positions + cash, **not** a broker-labeled "Net Asset Valuation", see prior flag in [freedom-finance.md](snapshots/freedom-finance.md)). Weight % = each row's combined USD-equivalent value ÷ this total. *Score and review-date columns are intentionally blank/unchanged — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.*

> ## No share-count changes, no fills, no cancellations — but two new, undocumented orders this week, and one order vanished
>
> All 24 IBKR positions hold identical quantities to the 2026-08-30 sync. Only prices moved over the 7-day window (largest: ADBE -8.58%, ZS -7.97%, META +6.43%) — nothing crosses the Rule 9 ±15% unexplained-move threshold. **Two new active orders appeared, both with no `sessions/`/`decisions/` entry and both contradicting the framework's own most recent analysis on the name:** TSM BUY 10 @ $369.00 GTC (placed 2026-09-06, the same day today's own [new-position session](../watchlist/not-in-portfolio/TSM/TSM-2026-09-06.md) said "WATCHLIST ONLY — do not enter" with buy ceilings of $258.88–$277.37), and NVDA BUY 10 @ $199.56 GTC (placed 2026-08-31, predating both the [2026-09-01](../sessions/2026-09-01-rescore-nvda.md) and [2026-09-04](../sessions/2026-09-04-rescore-nvda.md) rescores, each of which states no order was placed by that session). **Separately, the previously-active TLT short call order (1040104046) no longer appears in the orders fetch at all** — worth a manual TWS check for whether it filled, expired, or was cancelled. The BKNG BUY 10 @ $159.00 GTC order flagged in the prior two syncs also remains open and undocumented. Flagged for the user on all four items — none resolved by this sync. Full detail: [ibkr.md](snapshots/ibkr.md), [ibkr-orders.md](snapshots/ibkr-orders.md).
>
> ## ⚠️ TRN — small further pullback this week, cause remains unconfirmed
>
> £1.991 → £1.919/share (-3.62%) this week, share count unchanged (600). Already rescored 2026-08-31 (Quality Score 67.2, fails the 80.0+ gate) — HOLD, no top-up. See [ibkr.md](snapshots/ibkr.md).
>
> ## SPOT position and its sell order remain absent — now 7 consecutive syncs, still unresolved since 2026-08-02
>
> No new information this sync; still flagged for the user to confirm directly in TWS/Client Portal. Full detail in [ibkr.md](snapshots/ibkr.md) and [ibkr-orders.md](snapshots/ibkr-orders.md).
>
> ## Cash up modestly this sync (+$22.05 over 7 days)
>
> IBKR USD-equiv cash: $4,061.27 → $4,083.32. No fills or assignments recorded this window (see order flags above) — the small delta is ordinary drift. **The still-unresolved +$2,523.36 cash jump flagged 2026-08-09** remains open and uninvestigated.
>
> **AVGO's 2026-06-16 override is still marked "Open — under review" in [override-log.md](override-log.md)** despite having been resolved via the 2026-07-04 full rescore — carried forward as an open housekeeping item, not corrected this pass (outside `/sync-portfolio`'s scope).
>

**Score scale (2026-06-11):** Valuation scores run **0.0–100.0** (continuous, 0 = cheapest, 100.0 = most expensive) instead of the old 1–10 integers — see [valuation-scoring.md](../framework/valuation-scoring.md) and [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md).

**Quality Score / Composite Score columns added 2026-06-29** (see [decisions/2026-06-29-framework-change-quality-score-and-composite.md](../decisions/2026-06-29-framework-change-quality-score-and-composite.md) and [quality-scoring.md](../framework/quality-scoring.md)) — every row that carries a numeric Last Score predates this change and does not yet have a Quality Score computed, so both new columns are marked **`?`** (never invented/backfilled) until that ticker's next `/rescore` pass fills them in. Rows already "not scored" (cash, non-equity, quality-gate fail, overrides) are left blank — there is nothing for the new columns to invalidate.

| Ticker | Weight % | Last Score | Quality Score | Composite Score | Last Review | Broker |
|--------|----------|------------|----------------|------------------|-------------|--------|
| ADBE | 4.29% | 0.0 | 83.9 | 8.1 | 29 Jul 2026 | IBKR |
| AMZN | 4.99% | 82.7 | 56.7 | 63.0 | 01 Aug 2026 | IBKR (Freedom24 leg sold — see note above) |
| AVGO | 3.45% | 66.6 | 86.3 | 40.2 | 03 Sep 2026 | IBKR |
| CASH (Freedom24) | 0.07% | | | | | Freedom24 |
| CASH (IBKR) | 6.57% | | | | | IBKR |
| CSGP | 1.24% | 84.8 | 69.2 | 57.8 | 09 Aug 2026 | IBKR |
| **DOCS (short put)** | n/a — expired worthless 2026-08-21, position closed | n/a | | | n/a | IBKR |
| DUOL | 9.34% | 85.1 | 83.2 | 51.0 | 01 Sep 2026 | IBKR + Freedom24 |
| GOOG | 0.54% | 64.2 | 71.4 | 46.4 | 22 Jul 2026 | IBKR |
| **MBGL** | 0.03% | not scored — fails quality gates | 51.0 | | 09 Aug 2026 | IBKR |
| META | 4.95% | 39.4 | 87.5 | 26.0 | 26 Aug 2026 (PM) | IBKR (Freedom24 leg sold — see note above) |
| MSFT | 13.66% | 38.9 | 79.9 | 29.5 (ref only, gate fail) | 30 Jul 2026 | IBKR (Freedom24 leg sold — see note above) |
| NFLX | 1.51% | 49.3 | 69.8 | 39.8 | 17 Jul 2026 | IBKR |
| NKE | 1.24% | 13.9 | 44.4 | 34.8 | 1 Jul 2026 | IBKR |
| NOW | 2.05%⚠️ | 75.9 | 73.2 | 51.4 (ref only, gate fail) | 09 Aug 2026 | IBKR |
| NVDA | 7.02% | 38.5 | 90.3 | 24.1 | 04 Sep 2026 | IBKR |
| NVO | 0.37% | 51.4 | 67.2 | 42.1 (ref only, gate fail) | 09 Aug 2026 | IBKR |
| RBRK | 0.45% | not scored — fails quality gates | | | 30 Aug 2026 | IBKR |
| **RGL** | 0.77% | not scored — ungoverned position, see note above | | | n/a | IBKR |
| SPGI | 0.71% | 31.3 | 67.7 | 31.8 | 09 Aug 2026 | IBKR |
| TLT | 28.81% | not scored — non-equity, framework gap | | | Jun 2026 | IBKR + Freedom24 |
| TRN | 2.51%⚠️ | 10.0 | 66.4 | 21.8 (ref only, gate fail) | 10 Sep 2026 | IBKR |
| UBER | 0.37% | 43.6 | 55.5 | 44.1 | 07 Aug 2026 | IBKR |
| V | 0.60% | 54.5 | 85.6 | 34.5 | 29 Jul 2026 | IBKR |
| VEEV | 1.33% | 65.9 | 86.0 | 40.0 | 30 Aug 2026 | IBKR |
| XEON | 2.81% | not scored — cash-equivalent, out of scope | | | Jun 2026 | IBKR |
| ZS | 0.27% | 47.9 | 59.4 | 44.3 | 07 Sep 2026 | IBKR |

**STIM (previously 2.47%) removed this sync** — position fully exited via forced option assignment, see flag above. Moved to `watchlist/not-in-portfolio/STIM/`.

**SPOT (previously 0.83%) remains absent from this table** — its 1-share position has now been missing for seven consecutive syncs (2026-08-02, 08-09, 08-16, 08-22, 08-23, 08-30, 09-06), undocumented; see the flag above and [ibkr.md](snapshots/ibkr.md).

**MSFT's weight (13.66%) is now IBKR-only** — the 2-share Freedom24 leg was sold (confirmed, see flag above). Composite Score for MSFT remains a reference figure only (not adopted) — its Quality Score (79.9) fails the 80.0+ gate by 0.1 point.

**NOW's weight (⚠️) still carries the 2026-08-10 undocumented 3-share trim** — unresolved, see [override-log.md](override-log.md).

**TRN's weight (⚠️) still reflects the 22.4% price drop from the 08-16→08-22 window** — caused by a CMA "drip pricing" investigation opened 2026-08-19, still open with no finding as of the [2026-09-10 rescore](../sessions/2026-09-10-rescore-trn.md) (see also [2026-08-31](../sessions/2026-08-31-rescore-trn.md) and [2026-08-22](../sessions/2026-08-22-rescore-trn.md) sessions). **HOLD, no top-up** — Quality Gate already blocked adding before this news; the CMA probe adds a second, independent reason. Quality Score moved 67.2 → 66.4 this session (Composite 21.4 → 21.8) — a data-quality correction to the Net Debt/EBITDA sub-score (a lease-liability inconsistency in the leverage figure used since TRN's original evaluation, now resolved per Rule 6), **not** a fundamentals decline. New CEO Ian Brown started 7 Sept 2026 (full handover 28 Sept) — the trigger for this rescore; too early for any Moat evidence to move. FY2026 FCF fell −17.0% YoY (£79.5M vs £95.9M FY2025) — flagged, not yet explained by disclosed management commentary. Friday 11 Sept 2026 brings a sales/KPI trading update only, not full financials — won't resolve either open item.

**XEON is EUR-denominated** (€1,501.40 market value). Its USD-equivalent (**$1,743.67**, used for the weight above) comes from the *live* EUR→USD rate (1.1613635) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**TRN is GBP-denominated** (£1,151.40 market value, LSE — share count unchanged at 600). Its USD-equivalent (**$1,556.80**, used for the weight above) comes from the *live* GBP→USD rate (1.3520912) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**RGL is AUD-denominated** (AUD $660.00 market value, ASX — share count unchanged at 60,000). Its USD-equivalent (**$475.46**, used for the weight above) comes from the *live* AUD→USD rate (0.7203907) returned by IBKR's `get_account_balances` — broker-reported, not assumed. No Phase 01/02 evaluation exists for this ticker.

**`CASH (IBKR)`** = **$4,083.32** USD-equivalent ($4,303.50 USD + €227.49 EUR ≈ +$264.20 + £0.00 GBP ≈ $0.00 − AUD $672.20 ≈ −$484.25, net of rounding — full per-currency breakdown in the [IBKR snapshot](snapshots/ibkr.md)). Up modestly vs. $4,061.27 last sync (+$22.05 over 7 days) — no fills or assignments recorded this window (see the order flags above).

**`CASH (Freedom24)`** = $44.98 (unchanged — not resynced this round, no screenshot provided; single-currency USD, no FX conversion needed).

**Combined positions across both brokers:** DUOL and TLT are held in both IBKR and Freedom Finance (weights = sum of both, using the last-synced Freedom24 figures from 2026-08-22: DUOL $1,165.44, TLT $9,679.54). AMZN, META, and MSFT are IBKR-only (Freedom24 legs sold, confirmed 2026-08-22). All other equity tickers are IBKR-only; both `CASH` rows are naturally broker-specific.

**AVGO has a prior, untracked history on this account:** `get_account_trades` shows a 1-share AVGO position sold on 2026-05-26 (predating this framework's records), which is what the now-superseded "AVGO no longer appears in either broker account" placeholder note (removed in a prior sync) was referring to. The 6-share position now held is a fresh, separate buy from 2026-06-16 — see the override flag in [override-log.md](override-log.md).

*Run `/sync-portfolio` (see [sync-sop.md](sync-sop.md)) to refresh weights/cash/brokers from the live [snapshots](snapshots/); run `/rescore` to populate score and review-date columns (VEEV scored 2026-07-01 — see [session](../sessions/2026-07-01-rescore-veev.md); AVGO rescored 2026-09-03 post-Q3-FY2026-earnings, current — see [session](../sessions/2026-09-03-rescore-avgo.md)).*

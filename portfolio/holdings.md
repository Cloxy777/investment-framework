# Current Holdings

> Source of truth for what's actually owned. Update after every [portfolio sync](sync-sop.md) or trade. Each entry should carry the last valuation score and review date so [/rescore](../.claude/commands/rescore.md) knows what's due.

**As of 2026-09-13 — live sync from [IBKR](snapshots/ibkr.md) (positions, cash balances, and active orders all refreshed 2026-09-13) + [Freedom Finance](snapshots/freedom-finance.md) snapshot (last refreshed 2026-08-22, not resynced this round — no screenshot provided; Freedom24 sync is manual/screenshot-based, not part of this IBKR sync), including cash balances on both sides.**

Combined total ≈ **$61,192.89** = IBKR Net Liquidation Value $50,302.93 + Freedom24 implied total $10,889.96 (unchanged from 2026-08-22, positions + cash, **not** a broker-labeled "Net Asset Valuation", see prior flag in [freedom-finance.md](snapshots/freedom-finance.md)). Weight % = each row's combined USD-equivalent value ÷ this total. *Score and review-date columns are intentionally blank/unchanged — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.*

> ## 🚨 New, large, undocumented order this week: TRN BUY 900 @ £1.756 GTC — contradicts yesterday's own rescore
>
> Placed 2026-09-11 (order 1528612089), one day **after** TRN's own [2026-09-10 rescore](../sessions/2026-09-10-rescore-trn.md) explicitly recommended **HOLD, no top-up** (Quality Score 66.4, fails the 80.0+ gate; independent, still-open CMA "drip pricing" probe). This order would grow the TRN position from 600 → 1,500 shares (**+150%**) — no `sessions/`/`decisions/` entry documents it, and GBP cash on the account is currently $0.00. **Flagged as urgent for the user: cancel or document.** Full detail: [ibkr-orders.md](snapshots/ibkr-orders.md).
>
> ## ⚠️ Second new order the same morning: ADBE BUY 10 @ $240.00 — already superseded, no live successor
>
> Placed one minute before the TRN order above (2026-09-11, order 1071856795), already shown `REPLACED` by this sync with no live follow-on order found. ADBE's own share count/avg cost are unchanged, confirming no fill. Directionally not inconsistent with ADBE's own same-day [2026-09-11 rescore](../sessions/2026-09-11-rescore-adbe.md) (BUY, 6-share top-up recommended), but the quantity and disposition don't clearly match — worth a manual TWS check for what it was replaced with, if anything. See [ibkr-orders.md](snapshots/ibkr-orders.md).
>
> ## No share-count changes this week; broad pullback across the book
>
> All 24 IBKR positions hold identical quantities to the 2026-09-06 sync. 9 of 24 names moved more than 5% this week (largest: RGL +9.09%, NVO -7.78%, SPGI -7.56%, RBRK -7.49%, DUOL -7.08%) — nothing crosses the Rule 9 ±15% unexplained-move threshold. **The five previously-flagged, still-undocumented orders (TSM, NVDA, BKNG, MA, PDD, NOW) remain open, unchanged, and unresolved** — see [ibkr-orders.md](snapshots/ibkr-orders.md) for the full carried-forward table. **The TLT short call order (1040104046) remains absent from the orders fetch, in any status, for a second consecutive sync** — still worth a manual TWS check.
>
> ## ⚠️ TRN — small rebound this week, cause of the multi-week decline remains unconfirmed
>
> £1.919 → £1.934/share (+0.78%) this week, share count unchanged at 600 (before the pending order above). Already rescored 2026-09-10 (Quality Score 66.4, fails the 80.0+ gate) — HOLD, no top-up. See [ibkr.md](snapshots/ibkr.md).
>
> ## SPOT position and its sell order remain absent — now 8 consecutive syncs, still unresolved since 2026-08-02
>
> No new information this sync; still flagged for the user to confirm directly in TWS/Client Portal. Full detail in [ibkr.md](snapshots/ibkr.md) and [ibkr-orders.md](snapshots/ibkr-orders.md).
>
> ## Cash up modestly this sync (+$16.50 over 7 days)
>
> IBKR USD-equiv cash: $4,083.32 → $4,099.82. No fills or assignments recorded this window (see order flags above) — the small delta is ordinary drift. **The still-unresolved +$2,523.36 cash jump flagged 2026-08-09** remains open and uninvestigated.
>
> **AVGO's 2026-06-16 override is still marked "Open — under review" in [override-log.md](override-log.md)** despite having been resolved via the 2026-07-04 full rescore — carried forward as an open housekeeping item, not corrected this pass (outside `/sync-portfolio`'s scope).
>

**Score scale (2026-06-11):** Valuation scores run **0.0–100.0** (continuous, 0 = cheapest, 100.0 = most expensive) instead of the old 1–10 integers — see [valuation-scoring.md](../framework/valuation-scoring.md) and [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md).

**Quality Score / Composite Score columns added 2026-06-29** (see [decisions/2026-06-29-framework-change-quality-score-and-composite.md](../decisions/2026-06-29-framework-change-quality-score-and-composite.md) and [quality-scoring.md](../framework/quality-scoring.md)) — every row that carries a numeric Last Score predates this change and does not yet have a Quality Score computed, so both new columns are marked **`?`** (never invented/backfilled) until that ticker's next `/rescore` pass fills them in. Rows already "not scored" (cash, non-equity, quality-gate fail, overrides) are left blank — there is nothing for the new columns to invalidate.

| Ticker | Weight % | Last Score | Quality Score | Composite Score | Last Review | Broker |
|--------|----------|------------|----------------|------------------|-------------|--------|
| ADBE | 4.13% | 0.0 | 83.3 | 8.4 | 11 Sep 2026 | IBKR |
| AMZN | 4.96% | 82.7 | 56.7 | 63.0 | 01 Aug 2026 | IBKR (Freedom24 leg sold — see note above) |
| AVGO | 3.49% | 66.6 | 86.3 | 40.2 | 03 Sep 2026 | IBKR |
| CASH (Freedom24) | 0.07% | | | | | Freedom24 |
| CASH (IBKR) | 6.70% | | | | | IBKR |
| CSGP | 1.24% | 84.8 | 69.2 | 57.8 | 09 Aug 2026 | IBKR |
| **DOCS (short put)** | n/a — expired worthless 2026-08-21, position closed | n/a | | | n/a | IBKR |
| DUOL | 8.95% | 85.1 | 83.2 | 51.0 | 01 Sep 2026 | IBKR + Freedom24 |
| GOOG | 0.55% | 64.2 | 71.4 | 46.4 | 22 Jul 2026 | IBKR |
| **MBGL** | 0.03% | not scored — fails quality gates | 51.0 | | 09 Aug 2026 | IBKR |
| META | 5.25% | 39.4 | 87.5 | 26.0 | 26 Aug 2026 (PM) | IBKR (Freedom24 leg sold — see note above) |
| MSFT | 13.63% | 38.9 | 79.9 | 29.5 (ref only, gate fail) | 30 Jul 2026 | IBKR (Freedom24 leg sold — see note above) |
| NFLX | 1.52% | 49.3 | 69.8 | 39.8 | 17 Jul 2026 | IBKR |
| NKE | 1.21% | 34.4 | 39.5 | 47.5 (ref only, gate fail) | 11 Sep 2026 | IBKR |
| NOW | 1.94%⚠️ | 75.9 | 73.2 | 51.4 (ref only, gate fail) | 09 Aug 2026 | IBKR |
| NVDA | 6.68% | 38.5 | 90.3 | 24.1 | 04 Sep 2026 | IBKR |
| NVO | 0.35% | 51.4 | 67.2 | 42.1 (ref only, gate fail) | 09 Aug 2026 | IBKR |
| RBRK | 0.42% | not scored — fails quality gates | | | 30 Aug 2026 | IBKR |
| **RGL** | 0.84% | not scored — ungoverned position, see note above | | | n/a | IBKR |
| SPGI | 0.67% | 31.3 | 67.7 | 31.8 | 09 Aug 2026 | IBKR |
| TLT | 29.04% | not scored — non-equity, framework gap | | | Jun 2026 | IBKR + Freedom24 |
| TRN | 2.56%⚠️ | 10.0 | 66.4 | 21.8 (ref only, gate fail) | 10 Sep 2026 | IBKR |
| UBER | 0.35% | 43.6 | 55.5 | 44.1 | 07 Aug 2026 | IBKR |
| V | 0.60% | 54.5 | 85.6 | 34.5 | 29 Jul 2026 | IBKR |
| VEEV | 1.29% | 65.9 | 86.0 | 40.0 | 30 Aug 2026 | IBKR |
| XEON | 2.85% | not scored — cash-equivalent, out of scope | | | Jun 2026 | IBKR |
| ZS | 0.27% | 47.9 | 59.4 | 44.3 | 07 Sep 2026 | IBKR |

**STIM (previously 2.47%) removed this sync** — position fully exited via forced option assignment, see flag above. Moved to `watchlist/not-in-portfolio/STIM/`.

**SPOT (previously 0.83%) remains absent from this table** — its 1-share position has now been missing for eight consecutive syncs (2026-08-02, 08-09, 08-16, 08-22, 08-23, 08-30, 09-06, 09-13), undocumented; see the flag above and [ibkr.md](snapshots/ibkr.md).

**MSFT's weight (13.66%) is now IBKR-only** — the 2-share Freedom24 leg was sold (confirmed, see flag above). Composite Score for MSFT remains a reference figure only (not adopted) — its Quality Score (79.9) fails the 80.0+ gate by 0.1 point.

**NOW's weight (⚠️) still carries the 2026-08-10 undocumented 3-share trim** — unresolved, see [override-log.md](override-log.md).

**TRN's weight (⚠️) still reflects the 22.4% price drop from the 08-16→08-22 window** — caused by a CMA "drip pricing" investigation opened 2026-08-19, still open with no finding as of the [2026-09-10 rescore](../sessions/2026-09-10-rescore-trn.md) (see also [2026-08-31](../sessions/2026-08-31-rescore-trn.md) and [2026-08-22](../sessions/2026-08-22-rescore-trn.md) sessions). **HOLD, no top-up** — Quality Gate already blocked adding before this news; the CMA probe adds a second, independent reason. Quality Score moved 67.2 → 66.4 this session (Composite 21.4 → 21.8) — a data-quality correction to the Net Debt/EBITDA sub-score (a lease-liability inconsistency in the leverage figure used since TRN's original evaluation, now resolved per Rule 6), **not** a fundamentals decline. New CEO Ian Brown started 7 Sept 2026 (full handover 28 Sept) — the trigger for this rescore; too early for any Moat evidence to move. FY2026 FCF fell −17.0% YoY (£79.5M vs £95.9M FY2025) — flagged, not yet explained by disclosed management commentary. Friday 11 Sept 2026 brings a sales/KPI trading update only, not full financials — won't resolve either open item.

**XEON is EUR-denominated** (€1,502.00 market value). Its USD-equivalent (**$1,741.11**, used for the weight above) comes from the *live* EUR→USD rate (1.1591946) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**TRN is GBP-denominated** (£1,160.40 market value, LSE — share count unchanged at 600, before the pending 900-share buy order flagged above). Its USD-equivalent (**$1,569.22**, used for the weight above) comes from the *live* GBP→USD rate (1.3523100) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**RGL is AUD-denominated** (AUD $720.00 market value, ASX — share count unchanged at 60,000). Its USD-equivalent (**$515.64**, used for the weight above) comes from the *live* AUD→USD rate (0.7161600) returned by IBKR's `get_account_balances` — broker-reported, not assumed. No Phase 01/02 evaluation exists for this ticker.

**`CASH (IBKR)`** = **$4,099.82** USD-equivalent ($4,317.52 USD + €227.49 EUR ≈ +$263.71 + £0.00 GBP ≈ $0.00 − AUD $672.20 ≈ −$481.44, net of rounding — full per-currency breakdown in the [IBKR snapshot](snapshots/ibkr.md)). Up modestly vs. $4,083.32 last sync (+$16.50 over 7 days) — no fills or assignments recorded this window (see the order flags above).

**`CASH (Freedom24)`** = $44.98 (unchanged — not resynced this round, no screenshot provided; single-currency USD, no FX conversion needed).

**Combined positions across both brokers:** DUOL and TLT are held in both IBKR and Freedom Finance (weights = sum of both, using the last-synced Freedom24 figures from 2026-08-22: DUOL $1,165.44, TLT $9,679.54). AMZN, META, and MSFT are IBKR-only (Freedom24 legs sold, confirmed 2026-08-22). All other equity tickers are IBKR-only; both `CASH` rows are naturally broker-specific.

**AVGO has a prior, untracked history on this account:** `get_account_trades` shows a 1-share AVGO position sold on 2026-05-26 (predating this framework's records), which is what the now-superseded "AVGO no longer appears in either broker account" placeholder note (removed in a prior sync) was referring to. The 6-share position now held is a fresh, separate buy from 2026-06-16 — see the override flag in [override-log.md](override-log.md).

*Run `/sync-portfolio` (see [sync-sop.md](sync-sop.md)) to refresh weights/cash/brokers from the live [snapshots](snapshots/); run `/rescore` to populate score and review-date columns (VEEV scored 2026-07-01 — see [session](../sessions/2026-07-01-rescore-veev.md); AVGO rescored 2026-09-03 post-Q3-FY2026-earnings, current — see [session](../sessions/2026-09-03-rescore-avgo.md)).*

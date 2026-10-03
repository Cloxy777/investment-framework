# Current Holdings

> Source of truth for what's actually owned. Update after every [portfolio sync](sync-sop.md) or trade. Each entry should carry the last valuation score and review date so [/rescore](../.claude/commands/rescore.md) knows what's due.

**As of 2026-09-27 — live sync from [IBKR](snapshots/ibkr.md) (positions, cash balances, and active orders all refreshed 2026-09-27) + [Freedom Finance](snapshots/freedom-finance.md) snapshot (last refreshed 2026-08-22, not resynced this round — no screenshot provided; Freedom24 sync is manual/screenshot-based, not part of this IBKR sync), including cash balances on both sides.**

Combined total ≈ **$61,622.32** = IBKR Net Liquidation Value $50,732.36 + Freedom24 implied total $10,889.96 (unchanged from 2026-08-22, positions + cash, **not** a broker-labeled "Net Asset Valuation", see prior flag in [freedom-finance.md](snapshots/freedom-finance.md)). Weight % = each row's combined USD-equivalent value ÷ this total. *Score and review-date columns are intentionally blank/unchanged — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.*

> ## 🚨 URGENT — two undocumented trades this week: ADBE add (10 → 20 shares) and BKNG fill (new 10-share position)
>
> **ADBE:** position doubled with no matching order ever tracked in [ibkr-orders.md](snapshots/ibkr-orders.md) and no `sessions/`/`decisions/` entry. Implied purchase price ~$240.10/share for the added 10 shares.
>
> **BKNG:** the order flagged as undocumented for five consecutive syncs (483688084, BUY 10 @ $159.00 GTC) has filled. BKNG's only evaluation on file, the [2026-08-05 new-position session](../sessions/2026-08-05-new-position-bkng.md), explicitly concluded **"WATCHLIST ONLY — do not enter"** (R/R fails the 2:1 minimum at every authorized MoS/stop). No override or decision documents this fill.
>
> Both logged in [override-log.md](override-log.md) this sync. **Flagged as urgent for the user: confirm both trades in TWS/Client Portal and either document the rationale (Rule 10) or treat as errors to unwind.** Full detail: [ibkr.md](snapshots/ibkr.md).
>
> ## ✅ AVGO's previously-flagged urgent order appears resolved
>
> The AVGO BUY 5 @ $310.60 GTC order (87937891) no longer appears in this sync's order fetch, and the AVGO position is unchanged — consistent with a manual cancellation. See [ibkr.md](snapshots/ibkr.md) for the caveat on this sync's order-fetch coverage.
>
> ## 🚨 RBRK and ZS Rule 9 rescores now 10 days overdue
>
> [#801](https://github.com/Cloxy777/investment-framework/issues/801) (RBRK) and [#802](https://github.com/Cloxy777/investment-framework/issues/802) (ZS) were due 2026-09-17 and remain open — **10 days overdue** as of this sync. Neither ticker's Last Review date below has moved since the trigger. Both names have moved further since: RBRK now $110.00, ZS now $193.01.
>
> ## ⚠️ TRN BUY 900 @ £1.756 GTC — status changed to `PENDING_CANCEL`, not yet confirmed complete
>
> Order 1528612089 now shows `PENDING_CANCEL` (as of 2026-09-26) rather than `NEW` — a cancel appears to be in flight for the order that has contradicted TRN's HOLD/no-top-up rescore since 2026-09-11. Not yet confirmed resolved. See [ibkr-orders.md](snapshots/ibkr-orders.md).
>
> ## Five previously-flagged, still-undocumented orders (GOOG, MA, NKE, NOW, V) remain open, unchanged
>
> See [ibkr-orders.md](snapshots/ibkr-orders.md) for the full carried-forward table. **The TLT short call order (1040104046) remains absent from the orders fetch, in any status, for a fourth consecutive sync** — still worth a manual TWS check.
>
> ## SPOT position and its sell order remain absent — now 10 consecutive syncs, still unresolved since 2026-08-02
>
> No new information this sync; still flagged for the user to confirm directly in TWS/Client Portal. Full detail in [ibkr.md](snapshots/ibkr.md) and [ibkr-orders.md](snapshots/ibkr-orders.md).
>
> ## Cash swung sharply this sync (-$3,994.33 over 7 days), reconciled by this week's two undocumented trades
>
> IBKR USD-equiv cash: $4,097.84 → $103.51. The ADBE add (~$2,401 outlay) and BKNG fill (~$1,591 outlay) combined (~$3,992) reconcile essentially all of the swing — not unexplained drift, but a direct consequence of the two flagged trades above. **The still-unresolved +$2,523.36 cash jump flagged 2026-08-09** remains open and uninvestigated.
>
> **This sync's `get_account_orders` fetch returned notably fewer records than usual (7 vs. 13 last sync)** — several previously-tracked order IDs are absent in any status, not just excluded as inactive. See the coverage note in [ibkr.md](snapshots/ibkr.md).
>
> **AVGO's 2026-06-16 override is still marked "Open — under review" in [override-log.md](override-log.md)** despite having been resolved via the 2026-07-04 full rescore — carried forward as an open housekeeping item, not corrected this pass (outside `/sync-portfolio`'s scope).

**Score scale (2026-06-11):** Valuation scores run **0.0–100.0** (continuous, 0 = cheapest, 100.0 = most expensive) instead of the old 1–10 integers — see [valuation-scoring.md](../framework/valuation-scoring.md) and [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md).

**Quality Score / Composite Score columns added 2026-06-29** (see [decisions/2026-06-29-framework-change-quality-score-and-composite.md](../decisions/2026-06-29-framework-change-quality-score-and-composite.md) and [quality-scoring.md](../framework/quality-scoring.md)) — every row that carries a numeric Last Score predates this change and does not yet have a Quality Score computed, so both new columns are marked **`?`** (never invented/backfilled) until that ticker's next `/rescore` pass fills them in. Rows already "not scored" (cash, non-equity, quality-gate fail, overrides) are left blank — there is nothing for the new columns to invalidate.

| Ticker | Weight % | Last Score | Quality Score | Composite Score | Last Review | Broker |
|--------|----------|------------|----------------|------------------|-------------|--------|
| **ADBE** | **7.65%🚨** | 0.0 | 83.3 | 8.4 | 11 Sep 2026 | IBKR |
| AMZN | 4.85% | 82.7 | 56.7 | 63.0 | 01 Aug 2026 | IBKR (Freedom24 leg sold — see note above) |
| AVGO | 3.43% | 71.4 | 86.3 | 42.6 | 3 Oct 2026 | IBKR |
| **BKNG** | **2.67%🚨 (new)** | not scored — "WATCHLIST ONLY, do not enter" per [2026-08-05 session](../sessions/2026-08-05-new-position-bkng.md) | 89.6 | 21.6 | n/a (no `/new-position` re-run) | IBKR |
| CASH (Freedom24) | 0.07% | | | | | Freedom24 |
| CASH (IBKR) | 0.17% | | | | | IBKR |
| CSGP | 1.14% | 84.8 | 69.2 | 57.8 | 09 Aug 2026 | IBKR |
| **DOCS (short put)** | n/a — expired worthless 2026-08-21, position closed | n/a | | | n/a | IBKR |
| DUOL | 8.88% | 85.1 | 83.2 | 51.0 | 01 Sep 2026 | IBKR + Freedom24 |
| GOOG | 0.55% | 64.2 | 71.4 | 46.4 | 22 Jul 2026 | IBKR |
| **MBGL** | 0.03% | not scored — fails quality gates | 51.0 | | 09 Aug 2026 | IBKR |
| META | 6.07% | 39.4 | 87.5 | 26.0 | 26 Aug 2026 (PM) | IBKR (Freedom24 leg sold — see note above) |
| MSFT | 14.24% | 38.9 | 79.9 | 29.5 (ref only, gate fail) | 30 Jul 2026 | IBKR (Freedom24 leg sold — see note above) |
| NFLX | 1.38% | 55.2 | 69.9 | 42.7 | 3 Oct 2026 | IBKR |
| NKE | 1.17% | 34.4 | 39.5 | 47.5 (ref only, gate fail) | 11 Sep 2026 | IBKR |
| NOW | 1.98%⚠️ | 75.9 | 73.2 | 51.4 (ref only, gate fail) | 09 Aug 2026 | IBKR |
| NVDA | 6.92% | 36.2 | 90.3 | 23.0 | 17 Sep 2026 | IBKR |
| NVO | 0.31% | 51.4 | 67.2 | 42.1 (ref only, gate fail) | 09 Aug 2026 | IBKR |
| RBRK | 0.54%🚨 | not scored — fails quality gates | | | 30 Aug 2026 | IBKR |
| **RGL** | 0.68% | not scored — ungoverned position, see note above | | | n/a | IBKR |
| SPGI | 0.65% | 31.3 | 67.7 | 31.8 | 09 Aug 2026 | IBKR |
| TLT | 28.52% | not scored — non-equity, framework gap | | | Jun 2026 | IBKR + Freedom24 |
| TRN | 2.51%⚠️ | 10.0 | 66.4 | 21.8 (ref only, gate fail) | 10 Sep 2026 | IBKR |
| UBER | 0.34% | 37.4 | 59.3 | 39.1 (ref only, gate fail) | 15 Sep 2026 | IBKR |
| V | 0.59% | 54.5 | 85.6 | 34.5 | 29 Jul 2026 | IBKR |
| VEEV | 1.37% | 65.9 | 86.0 | 40.0 | 30 Aug 2026 | IBKR |
| XEON | 2.78% | not scored — cash-equivalent, out of scope | | | Jun 2026 | IBKR |
| ZS | 0.31%🚨 | 47.9 | 59.4 | 44.3 | 07 Sep 2026 | IBKR |

**🚨 RBRK and ZS weights above are pre-Rule-9-rescore** — see the flag at the top of this file; both are overdue for `/rescore` per [#801](https://github.com/Cloxy777/investment-framework/issues/801) and [#802](https://github.com/Cloxy777/investment-framework/issues/802).

**🚨 ADBE and BKNG rows above carry the undocumented trades flagged at the top of this file** — ADBE's Last Score/Quality Score/Composite Score predate this week's undocumented share add (no rescore has run since); BKNG's figures are carried from its 2026-08-05 "WATCHLIST ONLY — do not enter" evaluation, now contradicted by an actual fill.

**STIM (previously 2.47%) removed prior sync** — position fully exited via forced option assignment; unchanged this round. Moved to `watchlist/not-in-portfolio/STIM/`.

**SPOT (previously 0.83%) remains absent from this table** — its 1-share position has now been missing for ten consecutive syncs (2026-08-02 through 2026-09-27), undocumented; see the flag above and [ibkr.md](snapshots/ibkr.md).

**MSFT's weight (14.24%) is now IBKR-only** — the 2-share Freedom24 leg was sold (confirmed, see flag above). Composite Score for MSFT remains a reference figure only (not adopted) — its Quality Score (79.9) fails the 80.0+ gate by 0.1 point.

**NOW's weight (⚠️) still carries the 2026-08-10 undocumented 3-share trim** — unresolved, see [override-log.md](override-log.md).

**TRN's weight (⚠️) still reflects the 22.4% price drop from the 08-16→08-22 window** — caused by a CMA "drip pricing" investigation opened 2026-08-19, still open with no finding as of the [2026-09-10 rescore](../sessions/2026-09-10-rescore-trn.md). **HOLD, no top-up** — Quality Gate already blocked adding before this news; the CMA probe adds a second, independent reason. New CEO Ian Brown started 7 Sept 2026 (full handover 28 Sept). FY2026 FCF fell −17.0% YoY (£79.5M vs £95.9M FY2025) — flagged, not yet explained by disclosed management commentary.

**XEON is EUR-denominated** (€1,503.40 market value). Its USD-equivalent (**$1,712.52**, used for the weight above) comes from the *live* EUR→USD rate (1.1391001) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**TRN is GBP-denominated** (£1,165.80 market value, LSE — share count unchanged at 600). Its USD-equivalent (**$1,544.09**, used for the weight above) comes from the *live* GBP→USD rate (1.3244900) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**RGL is AUD-denominated** (AUD $600.00 market value, ASX — share count unchanged at 60,000). Its USD-equivalent (**$421.41**, used for the weight above) comes from the *live* AUD→USD rate (0.7023521) returned by IBKR's `get_account_balances` — broker-reported, not assumed. No Phase 01/02 evaluation exists for this ticker.

**`CASH (IBKR)`** = **$103.51** USD-equivalent (-$155.30 USD + €227.49 EUR ≈ +$259.14 + £0.00 GBP + AUD $0.00, net of rounding — full per-currency breakdown in the [IBKR snapshot](snapshots/ibkr.md)). Down sharply vs. $4,097.84 last sync (-$3,994.33 over 7 days) — reconciled almost entirely by this week's ADBE add and BKNG fill (see flag above), not unexplained drift.

**`CASH (Freedom24)`** = $44.98 (unchanged — not resynced this round, no screenshot provided; single-currency USD, no FX conversion needed).

**Combined positions across both brokers:** DUOL and TLT are held in both IBKR and Freedom Finance (weights = sum of both, using the last-synced Freedom24 figures from 2026-08-22: DUOL $1,165.44, TLT $9,679.54). AMZN, META, and MSFT are IBKR-only (Freedom24 legs sold, confirmed 2026-08-22). All other equity tickers are IBKR-only; both `CASH` rows are naturally broker-specific.

**AVGO has a prior, untracked history on this account:** `get_account_trades` shows a 1-share AVGO position sold on 2026-05-26 (predating this framework's records). The 6-share position now held is a fresh, separate buy from 2026-06-16 — see the override flag in [override-log.md](override-log.md).

*Run `/sync-portfolio` (see [sync-sop.md](sync-sop.md)) to refresh weights/cash/brokers from the live [snapshots](snapshots/); run `/rescore` to populate score and review-date columns (VEEV scored 2026-07-01 — see [session](../sessions/2026-07-01-rescore-veev.md); AVGO rescored 2026-09-28, current — see [session](../sessions/2026-09-28-rescore-avgo.md)).*

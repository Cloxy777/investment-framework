# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-09-27 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-portfolio`)
**Cash balances last synced:** 2026-09-27 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-portfolio`)
**Account summary:** Net Liquidation $50,732.36 (broker-reported, BASE) · Gross Position Value $50,511.22 (sum of positions below, RGL/TRN/XEON converted at live FX) · Total Cash (USD-equiv) **$103.51** (broker-reported, BASE) · Unrealized P&L +$3,237.89 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 25 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders needed. `RGL @ASX` and `TRN @LSE` normalized (exchange suffix stripped) for consistency with `holdings.md`. **Ticker-lookup CSV not re-fetched this sync** — not needed (every position resolved via `contract_description`); the stored copy is now 27 days stale (last refreshed 2026-08-31).

> ## 🚨 URGENT — ADBE position doubled (10 → 20 shares) with no matching order or session on record
>
> ADBE's share count jumped from 10 (2026-09-20 sync) to 20 this sync. The blended average cost (now $221.09, up from $202.07) implies the added 10 shares were bought at **~$240.10/share**. No active-order entry for ADBE appeared in any prior `ibkr-orders.md` sync (the only ADBE order on file, 1071856795, has been `REPLACED` with no live successor since 2026-09-11) — there is no order this fill could be tracing back to, and no `sessions/`/`decisions/` entry documents an ADBE add. **Flagged as urgent for the user: confirm this trade in TWS/Client Portal and either document the rationale (Rule 10) or investigate how it happened.** Logged in [override-log.md](../override-log.md).
>
> ## 🚨 NEW POSITION — BKNG filled: 10 shares @ ~$159.10 avg cost
>
> This is the fill of the order flagged as undocumented for five consecutive syncs (483688084, BUY 10 @ $159.00 GTC, placed 2026-08-24) — see [ibkr-orders.md](ibkr-orders.md). BKNG's only evaluation on file, the [2026-08-05 new-position session](../../sessions/2026-08-05-new-position-bkng.md), explicitly concluded **"WATCHLIST ONLY — do not enter"** (Composite Score 21.6 — nominally a "Very Cheap" band that would authorize a 6–8% position, but Risk/Reward fails the 2:1 minimum at every authorized MoS/stop combination, best case 1.25:1). No `sessions/`/`decisions/` entry overrides that call. **Flagged as urgent for the user: document the reasoning or treat as an error to unwind.** Logged in [override-log.md](../override-log.md). Watchlist entry moved `not-in-portfolio/` → `in-portfolio/` per [watchlist/README.md](../../watchlist/README.md).
>
> ## ✅ AVGO's previously-flagged urgent order appears resolved — no longer live, position unchanged
>
> The AVGO BUY 5 @ $310.60 GTC order (87937891), flagged urgent for two consecutive syncs as contradicting AVGO's own 2026-09-15 rescore ("No order is placed"), **no longer appears in this sync's order fetch in any status**, and the AVGO position is unchanged (still 6 shares, avg cost unchanged at $382.4417) — confirming it did not fill. Reads as a manual cancellation in TWS/Client Portal, consistent with "no tool in this repo places, modifies, or cancels a broker order." Not confirmed with certainty (see order-fetch coverage note below); worth a quick TWS check to be sure.
>
> ## ⚠️ TRN BUY 900 @ £1.756 GTC — status changed NEW → `PENDING_CANCEL`
>
> Order 1528612089 (originally placed 2026-09-11, still contradicting the [2026-09-10 rescore](../../sessions/2026-09-10-rescore-trn.md)'s explicit HOLD/no-top-up call) now shows status `PENDING_CANCEL` as of 2026-09-26 — a cancel request appears to be in flight but not yet confirmed complete. `PENDING_CANCEL` isn't one of [sync-sop.md](../sync-sop.md)'s named active/inactive statuses; conservatively excluded from the active-orders table below (see [glossary.md](../../framework/glossary.md#pending_cancel-order-status) — new term added this sync) since it's headed toward cancellation, but not yet confirmed resolved. GBP cash remains $0.00. Worth a TWS check to confirm the cancel completed.
>
> ## 🚨 RBRK and ZS Rule 9 rescores now 10 days overdue
>
> Both [#801](https://github.com/Cloxy777/investment-framework/issues/801) (RBRK) and [#802](https://github.com/Cloxy777/investment-framework/issues/802) (ZS) were due 2026-09-17 and remain open. Neither ticker's `holdings.md` review date has moved. RBRK is now $110.00 (vs. $100.20 that triggered #801); ZS is now $193.01 (vs. $191.73 that triggered #802).
>
> ## SPOT position remains absent — now 10 consecutive syncs (since 2026-08-02)
>
> No new information this sync; still flagged for the user to confirm directly in TWS/Client Portal. See [holdings.md](../holdings.md).
>
> ## Order-fetch coverage note — this sync's `get_account_orders` returned only 7 total records (11 active + 2 non-active last sync)
>
> Per [sync-sop.md](../sync-sop.md), this call is documented to return "every order on record," but several previously-tracked order IDs (AVGO 87937891, ADBE 1071856795 `REPLACED`, NVDA 1306197667, PDD 1150965513, TSM 510436581) are absent from this fetch in **any** status, not just excluded as inactive. Positions confirm no fills occurred for NVDA (unchanged share count/avg cost), and no PDD/TSM position exists — consistent with cancellation, not a fill silently missed. But this is the first sync where "every order on record" hasn't held in practice; worth noting in case the MCP's returned window has a retention limit, which would affect how much this repo can rely on that claim going forward.
>
> ## ⚠️ TLT short call order (1040104046) still absent from this sync's order fetch, in any status — now 4 consecutive syncs
>
> First flagged missing in the 2026-09-06 sync. Worth a manual TWS/Client Portal check for whether it filled, expired, or was cancelled; not resolved by this sync.

> **Two ungoverned equity positions still present (RGL, MBGL) — see [override-log.md](../override-log.md) for detail, unchanged this sync.**

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| **ADBE** | **20** | 235.62 | 4,712.40 | 221.0850 | +290.70 | +6.58% | USD | 265768 |
| AMZN | 12 | 248.98 | 2,987.76 | 210.5885 | +460.70 | +18.23% | USD | 3691937 |
| AVGO | 6 | 352.30 | 2,113.80 | 382.4417 | -180.85 | -7.88% | USD | 313130367 |
| **BKNG** | **10 (new)** | 164.60 | 1,646.00 | 159.1000 | +55.00 | +3.46% | USD | 308728373 |
| CSGP | 25 | 28.09 | 702.25 | 35.0400 | -173.75 | -19.83% | USD | 6726677 |
| DUOL | 30 | 143.51 | 4,305.30 | 168.2479 | -742.14 | -14.71% | USD | 505002183 |
| GOOG | 1 | 339.80 | 339.80 | 295.7000 | +44.10 | +14.91% | USD | 208813720 |
| **MBGL** | 1 | 17.87 | 17.87 | 19.8924 | -2.02 | -10.17% | USD | 893054611 |
| META | 5 | 747.60 | 3,738.00 | 575.0560 | +862.72 | +30.01% | USD | 107113386 |
| MSFT | 17 | 516.18 | 8,775.06 | 391.2165 | +2,124.38 | +31.94% | USD | 272093 |
| NFLX | 12 | 71.07 | 852.84 | 87.7905 | -200.65 | -19.05% | USD | 15124833 |
| NKE | 20 | 35.99 | 719.80 | 43.3100 | -146.40 | -16.90% | USD | 10291 |
| NOW | 9 | 135.60 | 1,220.40 | 87.6100 | +431.91 | +54.77% | USD | 109911821 |
| NVDA | 19 | 224.50 | 4,265.50 | 182.5059 | +797.89 | +23.01% | USD | 4815747 |
| NVO | 5 | 38.67 | 193.35 | 42.5400 | -19.35 | -9.10% | USD | 10611 |
| RBRK | 3 | 110.00 | 330.00 | 58.0962 | +155.71 | +89.34% | USD | 699030013 |
| **RGL** | 60,000 | 0.0100 (AUD) | 600.00 (AUD) | 0.0111 | -66.43 | -9.97% | AUD | 291951342 |
| SPGI | 1 | 403.30 | 403.30 | 391.1076 | +12.19 | +3.12% | USD | 229629397 |
| TLT | 100 | 79.00 | 7,900.00 | 87.6030 | -860.30 | -9.82% | USD | 15547841 |
| TRN | 600 | 1.943 (GBP) | 1,165.80 | 2.1195 | -105.91 | -8.33% | GBP | 371871705 |
| UBER | 3 | 69.66 | 208.98 | 82.0233 | -37.09 | -15.07% | USD | 365207014 |
| V | 1 | 365.98 | 365.98 | 319.5100 | +46.47 | +14.54% | USD | 49462172 |
| VEEV | 3 | 280.60 | 841.80 | 164.8333 | +347.30 | +70.21% | USD | 136254493 |
| XEON | 10 | 150.34 (EUR) | 1,503.40 | 149.0250 | +13.15 | +0.88% | EUR | 46041702 |
| ZS | 1 | 193.01 | 193.01 | 157.1600 | +35.85 | +22.81% | USD | 310621426 |

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value (sum of live position market values above, $50,511.22) plus Total Cash ($103.51) = $50,614.73, ~$117.63 **below** broker-reported Net Liquidation ($50,732.36) — consistent with the same `get_account_positions` (live/intraday) vs. `get_account_balances` (settled, slightly lagged) timing mismatch noted in prior syncs, widened this week by the BKNG fill and ADBE add landing between the two calls; not a calculation error.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE), **XEON** (EUR), and **RGL** (AUD, ASX). USD-equivalents (used for `holdings.md` weighting) use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | -155.30 | -155.30 | 1.0000000 | -155.30 |
| EUR | 227.49 | 227.49 | 1.1391001 | 259.14 |
| GBP | 0.00 | 0.00 | 1.3244900 | 0.00 |
| AUD | 0.00 | 0.00 | 0.7023521 | 0.00 |
| **Total (USD-equiv)** | | | | **103.51** |

*Row-by-row FX conversion sums to $103.84; the Total above uses the broker-reported BASE `cash_balance` (103.5054) directly, per Rule 0 — the ~$0.33 gap is a rounding artifact, not an error.*

*The same GBP→USD rate (1.3244900) applied to TRN's £1,165.80 market value gives its USD-equivalent: **$1,544.09** — used in `holdings.md` for weighting. The same EUR→USD rate (1.1391001) applied to XEON's €1,503.40 market value gives its USD-equivalent: **$1,712.52**. The same AUD→USD rate (0.7023521) applied to RGL's AUD $600.00 market value gives its USD-equivalent: **$421.41**.*

> **USD cash balance is negative (-$155.30)** — a small margin debit, consistent with this week's BKNG fill (~$1,591 cash outlay) and ADBE add (~$2,401 cash outlay) exceeding available settled cash between syncs. Not flagged as an error; the two undocumented trades above are the far more material issue this week.
>
> **Cash swung from +$4,097.84 (2026-09-20) to +$103.51 this sync**, a -$3,994.33 change (BASE) over the 7-day window — consistent with the ADBE add (~$2,401) and BKNG fill (~$1,591) cash outlays identified above (~$3,992 combined), which reconciles the swing. **The still-unresolved +$2,523.36 cash jump flagged 2026-08-09 remains open and uninvestigated.**

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

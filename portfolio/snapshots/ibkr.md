# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-08-22 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-portfolio`)
**Cash balances last synced:** 2026-08-22 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-portfolio`)
**Account summary:** Net Liquidation $50,211.93 (broker-reported, BASE) · Gross Position Value $46,132.81 (sum of positions below, RGL/TRN/XEON converted at live FX) · Total Cash (USD-equiv) **$4,060.67** (broker-reported, BASE) · Unrealized P&L +$2,644.34 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 25 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders needed. `RGL @ASX` and `TRN @LSE` normalized (exchange suffix stripped) for consistency with `holdings.md`. **Ticker-lookup CSV not re-fetched this sync** — not needed (every position resolved via `contract_description`) and the stored copy is only 6 days stale (last refreshed 2026-08-16).

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 10 | 275.00 | 2,750.00 | 202.0700 | +729.30 | +36.09% | USD | 265768 |
| AMZN | 12 | 259.59 | 3,115.08 | 210.5885 | +588.02 | +23.27% | USD | 3691937 |
| AVGO | 6 | 369.00 | 2,214.00 | 382.4417 | -80.65 | -3.52% | USD | 313130367 |
| CSGP | 25 | 32.6654 | 816.64 | 35.0400 | -59.37 | -6.78% | USD | 6726677 |
| DUOL | 30 | 145.7720 | 4,373.16 | 168.2479 | -674.28 | -13.36% | USD | 505002183 |
| GOOG | 1 | 342.15 | 342.15 | 295.7000 | +46.45 | +15.71% | USD | 208813720 |
| **MBGL** | 1 | 19.85 | 19.85 | 19.8924 | -0.04 | -0.21% | USD | 893054611 |
| META | 5 | 552.95 | 2,764.75 | 575.0560 | -110.53 | -3.84% | USD | 107113386 |
| MSFT | 17 | 483.60 | 8,221.20 | 391.2165 | +1,570.52 | +23.61% | USD | 272093 |
| NFLX | 12 | 79.59 | 955.08 | 87.7905 | -98.41 | -9.34% | USD | 15124833 |
| NKE | 20 | 40.75 | 815.00 | 43.3100 | -51.20 | -5.91% | USD | 10291 |
| NOW | 9 | 127.94 | 1,151.46 | 87.6100 | +362.97 | +46.03% | USD | 109911821 |
| NVDA | 19 | 215.38 | 4,092.22 | 182.5059 | +624.61 | +18.01% | USD | 4815747 |
| NVO | 5 | 46.74 | 233.70 | 42.5400 | +21.00 | +9.87% | USD | 10611 |
| RBRK | 3 | 100.09 | 300.27 | 58.0962 | +125.98 | +72.28% | USD | 699030013 |
| **RGL** | 60,000 | 0.0100 (AUD) | 600.00 (AUD) | 0.0111 | -66.43 | -9.97% | AUD | 291951342 |
| SPGI | 1 | 431.29 | 431.29 | 391.1076 | +40.18 | +10.27% | USD | 229629397 |
| TLT | 100 | 82.05 | 8,205.00 | 87.6030 | -555.30 | -6.34% | USD | 15547841 |
| TRN | 600 | 1.975 (GBP) | 1,185.00 | 2.1195 | -86.71 | -6.82% | GBP | 371871705 |
| UBER | 3 | 78.80 | 236.40 | 82.0233 | -9.67 | -3.93% | USD | 365207014 |
| V | 1 | 371.04 | 371.04 | 319.5100 | +51.53 | +16.13% | USD | 49462172 |
| VEEV | 3 | 247.8999939 | 743.70 | 164.8333 | +249.20 | +50.40% | USD | 136254493 |
| XEON | 10 | 149.983 (EUR) | 1,499.83 | 149.0250 | +9.58 | +0.64% | EUR | 46041702 |
| ZS | 1 | 182.00 | 182.00 | 157.1600 | +24.84 | +15.81% | USD | 310621426 |

> ## ⚠️ STIM position and covered call BOTH closed via option assignment at 2026-08-21 expiry — not a deliberate sale
>
> `get_account_trades` (DAYS_7) shows two linked trades, both timestamped **2026-08-22T05:46:02Z** (overnight expiry-cleanup processing), order 1811922406:
> - **BUY 5 STIM Aug21'26 $2.50 CALL @ $0** — the short covered call closed out at zero (option assignment mechanics, not a market buy).
> - **SELL 500 STIM STK @ $2.50** — the 500-share equity position called away at the $2.50 strike, net proceeds $1,250.00.
>
> Since the call was struck at $2.50 and STIM's live price is ~$3.02–3.25 (well above strike after the 08-11 earnings beat — see [issue #522](https://github.com/cloxy777/investment-framework/issues/522)), this is a **textbook ITM assignment at expiry**: IBKR forced the shares out at $2.50, roughly **$0.52–0.75/share below current market** (~$260–375 of foregone value on 500 shares), even though the *position itself* still nets a gain vs. the original $1.5816 avg cost (+$459.20 on the equity leg alone, plus whatever premium was collected when the call was originally written).
>
> **This resolves the open [2026-08-09 EXIT recommendation](../../sessions/2026-08-09-exit-review-stim.md) by elimination — STIM is no longer held — but not by execution.** No `decisions/` entry authorized this exit; it happened mechanically because the call was left open through expiry while deep ITM, not because anyone acted on the exit call. **[Issue #522](https://github.com/cloxy777/investment-framework/issues/522) (RESCORE: STIM) is now moot** — there's nothing left to rescore. Logged to [override-log.md](../override-log.md) as a governance item (assignment outcome, not a rationale gap).
>
> ## ✅ DOCS short put expired worthless 2026-08-21 — full premium kept, no assignment
>
> Same trade batch: **BUY 1 DOCS Aug21'26 $17.50 PUT @ $0**, order 1811922407 — the contract expired out-of-the-money (DOCS traded well above $17.50) and was bought back at zero to close the books. The ~$74.96 premium originally received is kept in full. **Resolves the open [override-log.md](../override-log.md) DOCS entry** — the ungoverned options trade is now closed with a clean, favorable outcome; no further action needed on this position.
>
> ## ⚠️ TRN — price down 22.4% since 2026-08-16 sync (2.544 → 1.975 GBP/share), no earnings/news confirmed this sync
>
> 600 shares unchanged, but market price dropped from £2.544 to £1.975/share (market value £1,526.40 → £1,185.00). That's a **-22.4% move** since the last sync 6 days ago — well past the ±15% Rule 9 "unexplained move" threshold this framework uses to trigger an immediate re-score. This sync didn't pull news/earnings data (out of scope for `/sync-portfolio`), so the cause is unconfirmed — **flagging for a Rule 9 investigation / rescore-due issue**, not diagnosing it here.
>
> ## SPOT position remains absent — still unresolved, unchanged since 2026-08-02
>
> No new information this sync; still flagged for the user to confirm directly in TWS/Client Portal. See [holdings.md](../holdings.md).
>
> ## Two previously-flagged REPLACED orders (CSGP, HDSN) have aged out of this fetch entirely
>
> Both no longer appear in `get_account_orders` in any status, and neither has a matching trade in `get_account_trades` (DAYS_7). Consistent with the same "REPLACED orders eventually drop out of the API's returned set" pattern already seen with TRN's order in the prior sync — not treated as new information, just no longer trackable from this data source. See [ibkr-orders.md](ibkr-orders.md).

> **Two ungoverned equity positions still present (RGL, MBGL) — see [override-log.md](../override-log.md) for detail, unchanged this sync.**

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value (sum of live position market values above, $46,132.81) plus Total Cash ($4,060.67) = $50,193.48, ~$18.45 **below** broker-reported Net Liquidation ($50,211.93) — consistent with the same `get_account_positions` (live/intraday) vs. `get_account_balances` (settled, slightly lagged) timing mismatch noted in prior syncs, not a calculation error.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE), **XEON** (EUR), and **RGL** (AUD, ASX). USD-equivalents (used for `holdings.md` weighting) use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | 4,274.70 | 4,274.70 | 1.0000000 | 4,274.70 |
| EUR | 227.49 | 227.49 | 1.1678947 | 265.68 |
| GBP | 0.00 | 0.00 | 1.3644824 | 0.00 |
| AUD | -668.95 | -668.95 | 0.7171154 | -479.72 |
| **Total (USD-equiv)** | | | | **4,060.67** |

*Row-by-row FX conversion sums to $4,060.66; the Total above uses the broker-reported BASE `cash_balance` (4,060.67) directly, per Rule 0 — the ~$0.01 gap is a rounding artifact, not an error.*

*The same GBP→USD rate (1.3644824) applied to TRN's £1,185.00 market value gives its USD-equivalent: **$1,616.91** — used in `holdings.md` for weighting. The same EUR→USD rate (1.1678947) applied to XEON's €1,499.83 market value gives its USD-equivalent: **$1,751.64**. The same AUD→USD rate (0.7171154) applied to RGL's AUD $600.00 market value gives its USD-equivalent: **$430.27**.*

> **Cash rose vs. last sync: $2,813.98 (2026-08-16) → $4,060.67 this sync**, a +$1,246.69 net change (BASE) — largely explained by the $1,250.00 STIM assignment proceeds (see flag above), with the small remainder ($3.31) likely ordinary drift (dividends, FX). Not fully itemized — flagging as accounted-for-in-substance rather than penny-matched.

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

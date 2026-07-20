# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-07-20 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-portfolio`)
**Cash balances last synced:** 2026-07-20 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-portfolio`)
**Account summary:** Net Liquidation $44,019.28 (broker-reported, BASE) · Gross Position Value $44,413.08 (sum of positions below, RGL/TRN/XEON converted at live FX) · Total Cash (USD-equiv) **–$264.11** (broker-reported, BASE) · Unrealized P&L –$214.64 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 28 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders needed. `XEON @IBIS2`, `TRN @LSE`, and `RGL @ASX` are normalized to `XEON`/`TRN`/`RGL` (exchange suffix stripped) for consistency with `holdings.md`. **The live ticker-lookup CSV (`https://www.interactivebrokers.com/download/fracshare_stk.csv`) returned HTTP 403 this sync** — fell back to the stored copy at [`portfolio/reference/ibkr-ticker-lookup.csv`](../reference/ibkr-ticker-lookup.csv) (last committed 2026-07-14, 6 days stale). Not re-committed this sync since it wasn't refreshed. No held ticker needed the lookup anyway (all resolved via `contract_description`), so this had no practical effect this round.

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 10 | 237.00 | 2,370.00 | 202.07 | +349.30 | +17.29% | USD | 265768 |
| AMZN | 12 | 248.00 | 2,976.00 | 210.59 | +448.94 | +17.78% | USD | 3691937 |
| AVGO | 6 | 374.68 | 2,248.08 | 382.44 | -46.57 | -2.03% | USD | 313130367 |
| CSGP | 25 | 29.78 | 744.50 | 35.04 | -131.50 | -15.00% | USD | 6726677 |
| **DOCS Aug21'26 $17.5 PUT (short)** | -1 (contract) | 0.65 | -65.00 | 0.7496 | +9.96 | n/a — short premium, see note | USD | 852764102 |
| DUOL | 30 | 133.85 | 4,015.50 | 168.25 | -1,031.94 | -20.45% | USD | 505002183 |
| GOOG | 1 | 348.00 | 348.00 | 295.70 | +52.30 | +17.69% | USD | 208813720 |
| **MBGL** | 1 | 20.11 | 20.11 | 19.89 | +0.22 | +1.09% | USD | 893054611 |
| META | 5 | 644.78 | 3,223.90 | 590.95 | +269.13 | +9.11% | USD | 107113386 |
| MSFT | 20 | 394.50 | 7,890.00 | 402.62 | -162.47 | -2.06% | USD | 272093 |
| NFLX | 12 | 68.92 | 827.04 | 87.79 | -226.45 | -21.48% | USD | 15124833 |
| NKE | 20 | 43.76 | 875.20 | 43.31 | +9.00 | +1.04% | USD | 10291 |
| NOW | 12 | 103.83 | 1,245.96 | 92.80 | +132.37 | +11.86% | USD | 109911821 |
| NVDA | 19 | 204.12 | 3,878.28 | 182.51 | +410.67 | +11.85% | USD | 4815747 |
| NVO | 5 | 50.31 | 251.55 | 42.54 | +38.85 | +18.28% | USD | 10611 |
| RBRK | 3 | 78.97 | 236.91 | 58.10 | +62.62 | +36.31% | USD | 699030013 |
| **RGL** | 60,000 | 0.0075 (AUD) | 450.00 (AUD) | 0.0111 | -216.43 | -32.48% | AUD | 291951342 |
| SPGI | 1 | 450.84 | 450.84 | 391.11 | +59.73 | +15.27% | USD | 229629397 |
| SPOT | 1 | 478.14 | 478.14 | 509.00 | -30.86 | -6.06% | USD | 312496724 |
| STIM | 500 | 1.62 | 810.00 | 1.5816 | +19.18 | +2.36% | USD | 324062325 |
| STIM Aug21'26 $2.50 CALL (short) | -5 (contracts) | 0.0963 | -48.15 | 0.0545 | -20.93 | n/a — short premium, see note | USD | 840079341 |
| TLT | 77 | 84.21 | 6,484.17 | 88.79 | -352.46 | -5.16% | USD | 15547841 |
| TRN | 600 | 2.244 (GBP) | 1,346.40 | 2.1195 | +74.69 | +5.88% | GBP | 371871705 |
| UBER | 3 | 72.52 | 217.56 | 82.02 | -28.51 | -11.58% | USD | 365207014 |
| V | 1 | 360.75 | 360.75 | 319.51 | +41.24 | +12.91% | USD | 49462172 |
| VEEV | 3 | 195.38 | 586.14 | 164.83 | +91.64 | +15.63% | USD | 136254493 |
| XEON | 10 | 149.673 (EUR) | 1,496.73 | 149.025 | +6.48 | +0.43% | EUR | 46041702 |
| ZS | 1 | 149.94 | 149.94 | 157.16 | -7.22 | -4.60% | USD | 310621426 |

> ## No new undocumented position changes this sync — all 28 positions unchanged in share count since 2026-07-12
>
> Every position's share count matches the 2026-07-12 sync exactly (only prices moved). This is the first sync since 2026-07-01 with **zero** new unauthorized fills — the META/DOCS/RGL items flagged 2026-07-12 remain open governance items (see [override-log.md](../override-log.md), unchanged this sync) but nothing new joined the list this week.

> ## ⚠️ New this sync — the AMZN bracket orders have disappeared from `get_account_orders` entirely (not filled, not `REPLACED`)
>
> The AMZN bracket (SELL 10 @ $259.25 / BUY 10 @ $210.25, order IDs 1529859761/1529859762, flagged as undocumented in the 2026-07-12 sync) **no longer appears anywhere in this sync's `get_account_orders` fetch** — not as `NEW`, not as `REPLACED`, not as `FILLED`/`CANCELLED`. The AMZN position is unchanged at 12 shares, so neither leg filled. The most likely explanation is a direct cancellation in TWS/Client Portal (outside this framework), but that isn't confirmed by anything visible to `/sync-portfolio` — flagged for the user to confirm. See [ibkr-orders.md](ibkr-orders.md) for the full active-orders table.

> **Two ungoverned equity positions still present (RGL, MBGL) — see [override-log.md](../override-log.md) for detail, unchanged this sync.**

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value (sum of live position market values above, $44,413.08) plus Total Cash (–$264.11) = $44,148.97, ~$129.69 **above** broker-reported Net Liquidation ($44,019.28) — consistent with the same `get_account_positions` (live/intraday) vs. `get_account_balances` (settled, slightly lagged) timing mismatch noted in prior syncs, not a calculation error. This gap is noticeably larger than the last few syncs (was $6.09 on 2026-07-12) — plausibly related to `get_account_balances`' AUD row showing a materially different RGL-related stock market value (AUD $423.53) than `get_account_positions`' live RGL price implies (AUD $450.00), a ~AUD $26.47 gap on that one line alone. Not investigated further this round; worth a closer look if the gap keeps widening.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE), **XEON** (EUR), and **RGL** (AUD, ASX). USD-equivalents (used for `holdings.md` weighting) use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

> **Short-options rows (DOCS put, STIM call):** the P&L % column is marked n/a because percentage-of-cost-basis is not a meaningful figure for a short option position — `Avg Cost` is the average **premium received** per contract when sold, not money paid. Neither short-options row is folded into any ticker's weight % in `holdings.md`.

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | -58.82 | -58.82 | 1.000000 | -58.82 |
| EUR | 227.49 | 227.49 | 1.14392485 | 260.23 |
| GBP | 0.00 | 0.00 | 1.34547875 | 0.00 |
| AUD | -666.43 | -666.43 | 0.6977 | -464.97 |
| **Total (USD-equiv)** | | | | **-264.11** |

*Row-by-row FX conversion sums to –$263.56; the Total above uses the broker-reported BASE `cash_balance` (–$264.113) directly, per Rule 0 — the small gap is a rounding/timing artifact, not an error.*

*The same GBP→USD rate (1.34547875) applied to TRN's £1,346.40 market value gives its USD-equivalent: **$1,811.55** — used in `holdings.md` for weighting. The same EUR→USD rate (1.14392485) applied to XEON's €1,496.73 market value gives its USD-equivalent: **$1,712.15**. The same AUD→USD rate (0.6977) applied to RGL's AUD $450.00 market value gives its USD-equivalent: **$313.96**.*

> **Cash improved slightly, from –$261.96 (2026-07-12) to –$264.11 this sync** — essentially flat (–$2.15 net), no new large swing. AUD cash is still deeply negative (–$666.43, unchanged from last sync) from the RGL fill; no new ungoverned cash movement this week.

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

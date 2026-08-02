# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-08-02 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-portfolio`)
**Cash balances last synced:** 2026-08-02 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-portfolio`)
**Account summary:** Net Liquidation $45,705.49 (broker-reported, BASE) · Gross Position Value $47,855.09 (sum of positions below, RGL/TRN/XEON converted at live FX) · Total Cash (USD-equiv) **–$2,198.29** (broker-reported, BASE) · Unrealized P&L +$1,413.29 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 26 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders needed. `RGL @ASX` normalized to `RGL` (exchange suffix stripped) for consistency with `holdings.md`. **The live ticker-lookup CSV (`https://www.interactivebrokers.com/download/fracshare_stk.csv`) was reachable this sync** (HTTP 200) — fetched and used to overwrite [`portfolio/reference/ibkr-ticker-lookup.csv`](../reference/ibkr-ticker-lookup.csv). No held ticker needed the lookup anyway (all resolved via `contract_description`), so this had no practical effect this round beyond keeping the stored fallback current.

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 10 | 250.00 | 2,500.00 | 202.0700 | +479.30 | +23.72% | USD | 265768 |
| AMZN | 12 | 270.32 | 3,243.84 | 210.5885 | +716.78 | +28.36% | USD | 3691937 |
| AVGO | 6 | 387.45 | 2,324.70 | 382.4417 | +30.05 | +1.31% | USD | 313130367 |
| CSGP | 25 | 28.80 | 720.00 | 35.0400 | -156.00 | -17.81% | USD | 6726677 |
| **DOCS Aug21'26 $17.5 PUT (short)** | -1 (contract) | 0.6293 | -62.93 | 0.7496 | +12.03 | n/a — short premium, see note | USD | 852764102 |
| DUOL | 30 | 134.50 | 4,035.00 | 168.2479 | -1,012.44 | -20.06% | USD | 505002183 |
| GOOG | 1 | 354.25 | 354.25 | 295.7000 | +58.55 | +19.80% | USD | 208813720 |
| **MBGL** | 1 | 20.38 | 20.38 | 19.8924 | +0.49 | +2.45% | USD | 893054611 |
| META | 6 | 553.80 | 3,322.80 | 580.1300 | -157.98 | -4.54% | USD | 107113386 |
| MSFT | 20 | 461.81 | 9,236.20 | 402.6235 | +1,183.73 | +14.70% | USD | 272093 |
| NFLX | 12 | 71.76 | 861.10 | 87.7905 | -192.39 | -18.26% | USD | 15124833 |
| NKE | 20 | 41.71 | 834.20 | 43.3100 | -32.00 | -3.69% | USD | 10291 |
| NOW | 12 | 111.23 | 1,334.76 | 92.7992 | +221.17 | +19.86% | USD | 109911821 |
| NVDA | 19 | 198.95 | 3,780.05 | 182.5059 | +312.44 | +9.01% | USD | 4815747 |
| NVO | 5 | 46.92 | 234.60 | 42.5400 | +21.90 | +10.30% | USD | 10611 |
| RBRK | 3 | 72.36 | 217.08 | 58.0962 | +42.79 | +24.55% | USD | 699030013 |
| **RGL** | 60,000 | 0.0100 (AUD) | 600.00 (AUD) | 0.0111 | -66.43 | -9.97% | AUD | 291951342 |
| SPGI | 1 | 411.93 | 411.93 | 391.1076 | +20.82 | +5.32% | USD | 229629397 |
| STIM | 500 | 1.98 | 990.00 | 1.5816 | +199.18 | +25.19% | USD | 324062325 |
| STIM Aug21'26 $2.50 CALL (short) | -5 (contracts) | 0.1684 | -84.18 | 0.0545 | -56.95 | n/a — short premium, see note | USD | 840079341 |
| TLT | 100 | 81.7004 | 8,170.04 | 87.6030 | -590.27 | -6.74% | USD | 15547841 |
| TRN | 600 | 2.372 (GBP) | 1,423.20 | 2.1195 | +151.49 | +11.91% | GBP | 371871705 |
| UBER | 3 | 70.45 | 211.35 | 82.0233 | -34.72 | -14.11% | USD | 365207014 |
| V | 1 | 366.13 | 366.13 | 319.5100 | +46.62 | +14.59% | USD | 49462172 |
| VEEV | 3 | 203.78 | 611.34 | 164.8333 | +116.84 | +23.63% | USD | 136254493 |
| XEON | 10 | 149.783 (EUR) | 1,497.83 | 149.0250 | +7.58 | +0.51% | EUR | 46041702 |
| ZS | 1 | 150.12 | 150.12 | 157.1600 | -7.04 | -4.48% | USD | 310621426 |

> ## ⚠️ SPOT position has vanished from this sync — no longer appears in `get_account_positions`
>
> The **1-share SPOT position** held as of the 2026-07-26 sync (avg cost $509.00, market value ~$482.66) is **completely absent** from this sync's `get_account_positions` fetch — not a zero-share row, not flagged any other way, simply gone. The matching **`SELL 1 SPOT @ $518.00` GTC order (order 934588780)**, which showed `NEW` status as of the 2026-07-26 orders sync, is **also completely absent** from this sync's `get_account_orders` fetch — not `FILLED`, not `CANCELLED`, not `REPLACED`, just gone. This is the same "vanished order" anomaly pattern flagged for the AMZN bracket (2026-07-20) and the TLT `BUY 13 @ $83.54` order (2026-07-26). Total account cash (BASE, –$2,198.29) is only ~$9 lower than last sync — **not** consistent with a straightforward ~$483–518 cash sale, so the mechanism is not confirmed. No `sessions/`, `decisions/`, or `override-log` entry covers this exit. **Flagged for the user to confirm directly in TWS/Client Portal** — was SPOT sold, and if so at what price/date, or is this a data anomaly?

> ## ⚠️ META share count changed 5 → 6 (+1 share), avg cost $590.954 → $580.13, undocumented
>
> META grew from **5 shares (2026-07-26 sync)** to **6 shares** this sync, with the blended average cost moving from $590.954 to $580.13. Working backward, the added share implies a cost of ~$526.01 (6×$580.13 − 5×$590.954 = $526.01). Coincident with this: the long-flagged **`SELL 1 META @ $611.01` GTC order (order 862563692)**, which had shown `NEW` status in every sync since 2026-07-04, has this sync flipped to **`REPLACED` with no live successor visible** in the current `get_account_orders` fetch. Whether these two facts are mechanically related (the sell order being replaced by a fill of some kind) is **not confirmed** — that would require `get_account_trades`, out of `/sync-portfolio`'s scope, per the same convention applied to the still-open 2026-07-12 META -1-share anomaly below. No `sessions/`, `decisions/`, or `override-log` entry covers this change. **Flagged for the user to confirm.**

> ## No other undocumented position changes this sync
>
> All other 24 non-flagged positions matched the 2026-07-26 sync exactly in share count and average cost (only prices moved). The open governance items from prior syncs (META's earlier unauthorized -1 share trim from 2026-07-08–11, DOCS's unauthorized short put, RGL's still-unevaluated fully-filled position, MBGL, TLT's 2026-07-26 undocumented +23-share increase and its still-working undocumented short call) remain open and untouched — see [override-log.md](../override-log.md), unchanged this sync except where noted above.

> **Two ungoverned equity positions still present (RGL, MBGL) — see [override-log.md](../override-log.md) for detail, unchanged this sync.**

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value (sum of live position market values above, $47,855.09) plus Total Cash (–$2,198.29) = $45,656.80, ~$48.71 **below** broker-reported Net Liquidation ($45,705.49) — consistent with the same `get_account_positions` (live/intraday) vs. `get_account_balances` (settled, slightly lagged) timing mismatch noted in prior syncs, not a calculation error.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE), **XEON** (EUR), and **RGL** (AUD, ASX). USD-equivalents (used for `holdings.md` weighting) use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

> **Short-options rows (DOCS put, STIM call):** the P&L % column is marked n/a because percentage-of-cost-basis is not a meaningful figure for a short option position — `Avg Cost` is the average **premium received** per contract when sold, not money paid. Neither short-options row is folded into any ticker's weight % in `holdings.md`. The `TLT SEP30'26 $90 CALL` short-call order (still working, still undocumented — see [ibkr-orders.md](ibkr-orders.md)) has not filled, so it is not yet a position and does not appear in the table above.

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | -1,991.51 | -1,991.51 | 1.0000000 | -1,991.51 |
| EUR | 227.49 | 227.49 | 1.1545948 | 262.66 |
| GBP | 0.00 | 0.00 | 1.3492781 | 0.00 |
| AUD | -666.43 | -666.43 | 0.7044125 | -469.44 |
| **Total (USD-equiv)** | | | | **-2,198.29** |

*Row-by-row FX conversion sums to –$2,198.29; the Total above uses the broker-reported BASE `cash_balance` (–$2,198.2929) directly, per Rule 0 — the small gap (if any) is a rounding/timing artifact, not an error.*

*The same GBP→USD rate (1.3492781) applied to TRN's £1,423.20 market value gives its USD-equivalent: **$1,920.29** — used in `holdings.md` for weighting. The same EUR→USD rate (1.1545948) applied to XEON's €1,497.83 market value gives its USD-equivalent: **$1,729.39**. The same AUD→USD rate (0.7044125) applied to RGL's AUD $600.00 market value gives its USD-equivalent: **$422.65**.*

> **Cash roughly flat vs. last sync: –$2,189.32 (2026-07-26) → –$2,198.29 this sync**, a –$8.97 net change — small and unremarkable on its own, but notably **not** large enough to reflect a ~$483–518 SPOT sale, per the flag above. AUD cash unchanged (–$666.43) from the RGL fill, no new AUD-side movement.

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

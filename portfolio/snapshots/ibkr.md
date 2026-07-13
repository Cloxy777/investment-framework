# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-07-12 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-portfolio`)
**Cash balances last synced:** 2026-07-12 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-portfolio`)
**Account summary:** Net Liquidation $44,058.60 (broker-reported, BASE) · Gross Position Value $44,326.65 (sum of positions below, RGL/TRN/XEON converted at live FX) · Total Cash (USD-equiv) **–$261.96** (broker-reported, BASE) · Unrealized P&L –$159.62 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 28 positions resolved directly from the MCP's `contract_description` field — no `CONID_XXXXXXX` placeholders needed. `XEON @IBIS2`, `TRN @LSE`, and `RGL @ASX` are normalized to `XEON`/`TRN`/`RGL` (exchange suffix stripped) for consistency with `holdings.md`. The live ticker-lookup CSV (`https://www.interactivebrokers.com/download/fracshare_stk.csv`) was fetched successfully this sync — no changes affecting held tickers, not re-committed since the stored copy is already current.

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 10 | 223.65 | 2,236.50 | 202.07 | +215.80 | +10.68% | USD | 265768 |
| AMZN | 12 | 245.34 | 2,944.08 | 210.59 | +417.02 | +16.50% | USD | 3691937 |
| AVGO | 6 | 400.39 | 2,402.34 | 382.44 | +107.69 | +4.69% | USD | 313130367 |
| CSGP | 25 | 28.30 | 707.50 | 35.04 | -168.50 | -19.24% | USD | 6726677 |
| **DOCS Aug21'26 $17.5 PUT (short)** | -1 (contract) | 0.60 | -60.21 | 0.7496 | +14.75 | n/a — short premium, see note | USD | 852764102 |
| DUOL | 30 | 124.76 | 3,742.95 | 168.25 | -1,304.49 | -25.85% | USD | 505002183 |
| GOOG | 1 | 355.05 | 355.05 | 295.70 | +59.35 | +20.07% | USD | 208813720 |
| **MBGL** | 1 | 20.80 | 20.80 | 19.89 | +0.91 | +4.56% | USD | 893054611 |
| META | 5 | 669.21 | 3,346.05 | 590.95 | +391.28 | +13.24% | USD | 107113386 |
| MSFT | 20 | 385.36 | 7,707.20 | 402.62 | -345.27 | -4.29% | USD | 272093 |
| NFLX | 12 | 73.40 | 880.80 | 87.79 | -172.69 | -16.39% | USD | 15124833 |
| NKE | 20 | 44.37 | 887.40 | 43.31 | +21.20 | +2.45% | USD | 10291 |
| NOW | 12 | 107.71 | 1,292.52 | 92.80 | +178.93 | +16.07% | USD | 109911821 |
| NVDA | 19 | 210.58 | 4,001.02 | 182.51 | +533.41 | +15.38% | USD | 4815747 |
| NVO | 5 | 49.49 | 247.43 | 42.54 | +34.73 | +16.33% | USD | 10611 |
| RBRK | 3 | 84.38 | 253.14 | 58.10 | +78.85 | +45.24% | USD | 699030013 |
| **RGL** | 60,000 | 0.008 (AUD) | 480.00 (AUD) | 0.0111 | -186.43 | -27.98% | AUD | 291951342 |
| SPGI | 1 | 430.50 | 430.50 | 391.11 | +39.39 | +10.07% | USD | 229629397 |
| SPOT | 1 | 479.77 | 479.77 | 509.00 | -29.23 | -5.74% | USD | 312496724 |
| STIM | 500 | 1.75 | 875.00 | 1.58 | +84.18 | +10.65% | USD | 324062325 |
| STIM Aug21'26 $2.50 CALL (short) | -5 (contracts) | 0.109 | -54.68 | 0.0545 | -27.45 | n/a — short premium, see note | USD | 840079341 |
| TLT | 77 | 84.55 | 6,510.35 | 88.79 | -326.28 | -4.77% | USD | 15547841 |
| TRN | 600 | 2.24 (GBP) | 1,344.00 | 2.12 | +72.29 | +5.68% | GBP | 371871705 |
| UBER | 3 | 74.54 | 223.62 | 82.02 | -22.45 | -9.12% | USD | 365207014 |
| V | 1 | 348.97 | 348.97 | 319.51 | +29.46 | +9.22% | USD | 49462172 |
| VEEV | 3 | 190.12 | 570.36 | 164.83 | +75.86 | +15.34% | USD | 136254493 |
| XEON | 10 | 149.61 (EUR) | 1,496.06 | 149.03 | +5.81 | +0.39% | EUR | 46041702 |
| ZS | 1 | 139.27 | 139.27 | 157.16 | -17.89 | -11.38% | USD | 310621426 |

> ## ⚠️⚠️ URGENT — new undocumented position changes surfaced this sync, flagged directly to the user
>
> `get_account_positions` this sync shows **four real, executed changes** since the 2026-07-05 sync — not just order-level exposure this time:
>
> | Ticker | Change | Documented? | Detail |
> |---|---|---|---|
> | **NVDA** | 14 → 19 shares (+5) | **Consistent with a session** | The [2026-07-05 rescore](../../sessions/2026-07-05-rescore-nvda.md) recommended a top-up of ~4 shares to an 18-share/6.39% target (CONFIRMED BUY, R/R 2.13:1). Actual fill (+5, to 19 shares) is 1 share past that target — a minor overshoot, not a governance concern. |
> | **META** | 6 → 5 shares (-1) | **No — unauthorized** | No `sessions/`, `decisions/`, or `override-log.md` entry authorizes a sale. The most recent [2026-07-09 rescore](../../sessions/2026-07-09-rescore-meta.md) explicitly recommends **HOLD — no forced trim** (Composite Score 24.5, well inside the 6–8% band, no trim signal). Mechanism not visible from `get_account_positions`/`get_account_orders` alone (no matching filled order appears in this sync's order fetch) — `get_account_trades` would confirm if investigated further. |
> | **RGL** | 2,786 → 60,000 shares (+57,214) | **No — pre-existing ungoverned order, now fully filled** | The 60,000-share GTC buy order (630395618) flagged as live/unauthorized in every sync since 2026-07-01 has fully filled. Still **no Phase 01/02 evaluation exists for RGL anywhere in this repo** — see [override-log.md](../override-log.md), updated this sync. |
> | **DOCS** | New: -1 short PUT contract (Aug21'26 $17.50 strike) | **No — unauthorized, and doesn't match the session it's closest to** | The only DOCS analysis on file, the [2026-07-07 new-position session](../../sessions/2026-07-07-new-position-docs.md), recommended a **stock limit BUY order at $20.50** (not entering at the time due to a sub-2:1 R/R) — it says nothing about writing options. A cash-secured/naked short put at the $17.50 strike is a materially different risk profile (assignment risk, no upside participation) that was never evaluated under this framework. No `override-log.md` entry exists for this position — added this sync. |
>
> **Net effect:** two of these four (NVDA, RGL) trace to already-known, already-flagged activity (NVDA closely matches its own session; RGL is the same standing override maturing from partial to full fill). **META and DOCS are new, unexplained, unauthorized changes** — flagged to the user directly this sync, same convention as the 2026-07-05 order-level flags.

> ## ⚠️⚠️ Also new this sync — an AMZN options-style bracket and a new HDSN options order, both undocumented
>
> Two new **NEW**-status orders appeared this sync with no matching session: **SELL 10 AMZN @ $259.25** and **BUY 10 AMZN @ $210.25** (both GTC, placed 2026-07-10T11:44:32Z — a bracket around the live price, ~245). No `sessions/`/`decisions/` entry discusses resizing the AMZN position. See [ibkr-orders.md](ibkr-orders.md) for the full active-orders table and the persisting HDSN/MA/V/PDD/NOW/META flags carried from prior syncs (largely unchanged, except the original 200-share HDSN stock buy order (569919342) is no longer present in this fetch — no HDSN stock position exists either, consistent with it having been cancelled — but a **new** HDSN options order (SELL 1 AUG21'26 $5 PUT, `REPLACED`, no live successor) appeared instead, continuing undocumented activity on this ticker despite its 24.7 Quality Score gate failure).

> **Two ungoverned equity positions still present (RGL, MBGL) — see the urgent box above and [override-log.md](../override-log.md) for detail.**

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value (sum of live position market values above, $44,326.65) plus Total Cash (–$261.96) = $44,064.69, ~$6.09 **above** broker-reported Net Liquidation ($44,058.60) — consistent with the same `get_account_positions` (live/intraday) vs. `get_account_balances` (settled, slightly lagged) timing mismatch noted in prior syncs, not a calculation error. The gap is somewhat larger than the prior sync's $1.87 — plausibly related to the RGL fill settling — not investigated further this round.

> **Currency note:** all positions are USD except **TRN** (GBP, LSE), **XEON** (EUR), and **RGL** (AUD, ASX). USD-equivalents (used for `holdings.md` weighting) use the live FX rates below, fetched directly from `get_account_balances` — never assumed.

> **Short-options rows (DOCS put, STIM call):** the P&L % column is marked n/a because percentage-of-cost-basis is not a meaningful figure for a short option position — `Avg Cost` is the average **premium received** per contract when sold, not money paid. Neither short-options row is folded into any ticker's weight % in `holdings.md` — DOCS has no equity position to attach a weight to at all (see the urgent box above), and STIM's –$54.68 market value is excluded from STIM's weight below per the same convention as every prior sync (~0.09% of the combined portfolio either way).

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | -58.82 | -58.82 | 1.000000 | -58.82 |
| EUR | 227.49 | 227.49 | 1.1403668 | 259.42 |
| GBP | 0.00 | 0.00 | 1.3388201 | 0.00 |
| AUD | -666.43 | -666.43 | 0.694767 | -463.01 |
| **Total (USD-equiv)** | | | | **-261.96** |

*Row-by-row FX conversion sums to –$262.41; the Total above uses the broker-reported BASE `cash_balance` (–$261.9568) directly, per Rule 0 — the small gap is a rounding/timing artifact, not an error.*

*The same GBP→USD rate (1.3388201) applied to TRN's £1,344.00 market value gives its USD-equivalent: **$1,799.37** — used in `holdings.md` for weighting. The same EUR→USD rate (1.1403668) applied to XEON's €1,496.06 market value gives its USD-equivalent: **$1,706.06**. The same AUD→USD rate (0.694767) applied to RGL's AUD $480.00 market value gives its USD-equivalent: **$333.49**.*

> **Cash swung from +$342.69 (2026-07-05) to –$261.96 this sync** — driven almost entirely by AUD cash moving from –$31.07 to –$666.43, consistent with the RGL order's remaining 57,214 shares fully filling this week (see the urgent box above) — a ~$629 AUD-equivalent purchase. Mechanism not independently confirmed via `get_account_trades` this sync (a `/sync-portfolio` pass doesn't call it), but the size and direction line up with the RGL fill and no other explanation. **This is the second time in three syncs that IBKR cash has gone meaningfully negative, both times traced to ungoverned trading activity (GBP/TRN on 2026-06-28, now AUD/RGL) — worth flagging as a pattern, not just a one-off, when the user reviews the RGL/DOCS/META items above.**

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

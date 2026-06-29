# IBKR Portfolio Snapshot

**Account:** U19421206
**Positions last synced:** 2026-06-28 (live via Interactive Brokers MCP — `get_account_positions`, via `/sync-portfolio`)
**Cash balances last synced:** 2026-06-28 (live via Interactive Brokers MCP — `get_account_balances`, via `/sync-portfolio`)
**Account summary:** Net Liquidation $39,767.94 (broker-reported, BASE) · Gross Position Value $41,334.34 (sum of positions below, TRN/XEON converted at live FX) · Total Cash (USD-equiv) **–$1,576.85** (broker-reported, BASE) · Unrealized P&L –$2,406.48 (broker-reported, BASE/USD-consolidated)

**Ticker resolution note:** all 25 positions resolved directly from the MCP's `contract_description` field. 23 are already clean ticker symbols; `XEON @IBIS2` and `TRN @LSE` are normalized to `XEON`/`TRN` (exchange suffix stripped) for consistency with `holdings.md`; the new options position resolves to `STIM Aug21'26 2.5 CALL @AMEX`. No `CONID_XXXXXXX` placeholders were needed, so the live/fallback ticker-lookup CSV fetch was not required for this sync. **TRN's contract_id (371871705) matches the disambiguation already on record** in [watchlist/in-portfolio/TRN/TRN-2026-06-24.md](../../watchlist/in-portfolio/TRN/TRN-2026-06-24.md) — confirms this is Trainline plc (LSE), not one of the three other listed companies sharing the "TRN" ticker.

| Ticker | Shares | Market Price | Market Value | Avg Cost | Unrealized P&L | P&L % | Currency | Contract ID |
|--------|--------|--------------|--------------|----------|----------------|-------|----------|-------------|
| ADBE | 10 | 202.73 | 2,027.30 | 202.07 | +6.60 | +0.33% | USD | 265768 |
| AMZN | 12 | 231.90 | 2,782.80 | 210.59 | +255.74 | +10.12% | USD | 3691937 |
| AVGO | 6 | 366.50 | 2,199.00 | 382.44 | -95.65 | -4.17% | USD | 313130367 |
| CSGP | 25 | 30.20 | 755.00 | 35.04 | -121.00 | -13.81% | USD | 6726677 |
| DUOL | 30 | 121.28 | 3,638.40 | 168.25 | -1,409.04 | -27.91% | USD | 505002183 |
| GOOG | 1 | 336.15 | 336.15 | 295.70 | +40.45 | +13.68% | USD | 208813720 |
| META | 6 | 551.11 | 3,306.66 | 597.81 | -280.17 | -7.81% | USD | 107113386 |
| MSFT | 20 | 372.73 | 7,454.60 | 402.62 | -597.87 | -7.43% | USD | 272093 |
| NFLX | 12 | 73.85 | 886.20 | 87.79 | -167.29 | -15.88% | USD | 15124833 |
| NKE | 20 | 40.92 | 818.35 | 43.31 | -47.85 | -5.52% | USD | 10291 |
| NOW | 12 | 98.75 | 1,184.95 | 92.80 | +71.36 | +6.41% | USD | 109911821 |
| NVDA | 14 | 192.75 | 2,698.50 | 179.20 | +189.64 | +7.56% | USD | 4815747 |
| NVO | 5 | 48.07 | 240.35 | 42.54 | +27.65 | +13.00% | USD | 10611 |
| RBRK | 3 | 72.33 | 216.99 | 58.10 | +42.70 | +24.50% | USD | 699030013 |
| SPGI | 1 | 408.16 | 408.16 | 411.00 | -2.84 | -0.69% | USD | 229629397 |
| SPOT | 1 | 460.02 | 460.02 | 509.00 | -48.98 | -9.62% | USD | 312496724 |
| STIM | 500 | 1.32 | 660.00 | 1.58 | -130.82 | -16.55% | USD | 324062325 |
| STIM Aug21'26 $2.50 CALL (short) | -5 (contracts) | 0.0911 | -45.55 | 0.0545 | -18.32 | n/a — short premium, see note | USD | 840079341 |
| TLT | 77 | 87.36 | 6,726.72 | 88.79 | -109.91 | -1.61% | USD | 15547841 |
| TRN | 600 | 2.11 (GBP) | 1,263.60 | 2.12 | -8.11 | -0.64% | GBP | 371871705 |
| UBER | 3 | 76.00 | 228.00 | 82.02 | -18.07 | -7.34% | USD | 365207014 |
| V | 1 | 336.23 | 336.23 | 319.51 | +16.72 | +5.23% | USD | 49462172 |
| VEEV | 3 | 171.36 | 514.08 | 164.83 | +19.58 | +3.96% | USD | 136254493 |
| XEON | 10 | 149.48 | 1,494.81 | 149.03 | +4.56 | +0.31% | EUR | 46041702 |
| ZS | 1 | 131.96 | 131.96 | 157.16 | -25.20 | -16.03% | USD | 310621426 |

> ⚠️ **New position since the last sync (2026-06-22) — TRN (Trainline plc, LSE):** 600 shares @ avg cost GBP 2.1195 (≈ GBX 211.95). `get_account_trades` confirms a single fill: **BUY 600 TRN @ GBX 210.40 limit, 2026-06-24T07:08:04Z** (order ID 1551402853, commission £9.31, net cost £1,271.71). **This is a framework-compliant partial-fill BUY, not an override** — see [watchlist/in-portfolio/TRN/TRN-2026-06-24.md](../../watchlist/in-portfolio/TRN/TRN-2026-06-24.md) (score 10.0, "BUY — Full position 6–8%", triggered by a Rule 9 management-change re-run) and [sessions/2026-06-24-new-position-trn.md](../../sessions/2026-06-24-new-position-trn.md) (target sizing ≈1,553 shares / ≈$4,191.30; 600 filled so far, same partial-fill pattern as ADBE). A larger `REPLACED` order for the remaining shares (BUY 900 @ GBX 161.50) shows no live successor in this sync's orders fetch — see [ibkr-orders.md](ibkr-orders.md).
>
> ⚠️ **Total Cash swung from +$255.99 to –$1,576.85 — funded via negative GBP cash (margin), not an FX conversion:** the GBP cash balance is now **–£1,271.71** (vs. a small positive balance implied previously), which exactly matches the net cost of the TRN fill above. No GBP-buying FX conversion trade appears in `get_account_trades` (`DAYS_7`) — the TRN purchase was funded by letting GBP cash go negative (effectively margin in that currency) rather than converting USD→GBP first. GBP-side Net Liquidation Value is now slightly negative (–$8.34, broker-reported) as a result. Flagged transparently for the user's awareness; not a framework violation (cash management/FX timing is outside the scope of the valuation/position-sizing rules), but worth a deliberate decision on whether to convert USD→GBP to cover this rather than carrying a negative balance.
>
> **STIM growth resolves last sync's order-window flags — both already-known, already-flagged orders filled:** stock position grew 345→500 shares (+155, order 1808588943, two fills: BUY 136 @ $1.20 on ISLAND + BUY 19 @ $1.215 on DARK, both 2026-06-22T14:56–15:13Z) and a new short-options position appeared (–5 contracts, `STIM Aug21'26 $2.50 CALL`, order 1248362620, SELL 5 @ $0.06 on CBOE, 2026-06-22T15:14:16Z, net credit $27.23 after commission). This 5-contract sale **supersedes** the 3-contract `Sell 3 STIM Aug21'26 2.5 Call` order that was still showing `NEW` in the 2026-06-22 orders snapshot — it was evidently replaced with a larger order before filling. Both fills are consistent with the ongoing covered-call income strategy already on record for STIM (500 shares fully covers the 5 written contracts, no naked exposure). Not a new governance flag.
>
> **No other position-size changes since 2026-06-22** — every other ticker's share count is identical to the prior sync; `get_account_trades` (`DAYS_7`) shows no other trades. Market-value/P&L changes elsewhere reflect price movement only.

> **Note on Gross Position Value vs. Net Liquidation:** Gross Position Value (sum of live position market values above, $41,334.34) plus Total Cash (–$1,576.85) = $39,757.49, ~$10.45 **below** broker-reported Net Liquidation ($39,767.94). Separately, the broker's own consolidated `stock_market_value` (BASE) is $41,377.24 — about $42.90 **above** this file's summed Gross Position Value. Both gaps are consistent with the same `get_account_positions` (live/intraday) vs. `get_account_balances` (settled, slightly lagged) timing mismatch noted in prior syncs — not a calculation error, flagged for transparency.

> **Currency note:** all positions are USD except **TRN** (GBP-denominated, LSE) and **XEON** (EUR-denominated). USD-equivalents (used for `holdings.md` weighting) are computed using the live FX rates below, fetched directly from `get_account_balances` — never assumed.

> **Short-options row (STIM call):** the P&L % column is marked n/a because percentage-of-cost-basis is not a meaningful figure for a short option position — `Avg Cost` ($0.0545) is the average **premium received** per contract when sold, not money paid; the negative unrealized P&L (–$18.32) reflects that the contract's current buy-back cost ($0.0911) now exceeds that premium. The –$45.55 market value (the liability to buy back all 5 contracts at the current price) is **not folded into STIM's weight % in `holdings.md`** — tracked here for transparency; at ~0.08% of the combined portfolio it would not move STIM's banding regardless.

## Cash Balances

Source: `get_account_balances` (one entry per currency the account holds, plus a `BASE` row consolidating everything to USD using IBKR's live FX rates).

| Currency | Cash Balance | Settled Cash | FX Rate → USD | USD Equivalent |
|----------|--------------|--------------|----------------|-----------------|
| USD | 95.41 | 95.41 | 1.000000 | 95.41 |
| EUR | 5.18 | 5.18 | 1.138523 | 5.90 |
| GBP | -1,271.71 | -1,271.71 | 1.319719 | -1,678.29 |
| **Total (USD-equiv)** | | | | **-1,576.85** |

*Row-by-row FX conversion sums to –$1,576.98; the Total above uses the broker-reported BASE `cash_balance` (–$1,576.8503) directly, per Rule 0 — the ~$0.13 gap is a rounding/timing artifact, not an error.*

*The same GBP→USD rate (1.319719) applied to TRN's £1,263.60 market value gives its USD-equivalent: **$1,667.60** — used in `holdings.md` for weighting. The same EUR→USD rate (1.138523) applied to XEON's €1,494.81 market value gives its USD-equivalent: **$1,701.88** — used in `holdings.md` for weighting.*

*This file has two independently-refreshed sections — the positions table (via `/sync-positions`) and the Cash Balances table (via `/sync-balances`), each with its own "last synced" timestamp above. `/sync-portfolio` runs both together (plus `/sync-orders`). See [sync-sop.md](../sync-sop.md). Prior snapshots live in git history, not as separate files.*

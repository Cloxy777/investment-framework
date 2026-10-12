# Framework-account performance statistics

Daily / weekly / month-to-date / N-month / YTD / N-year **time-weighted return (TWR)** of the framework account **`U19421206`**, rebuilt as if **RGL, LM8 and TLT had never been in it** — in the past as well as after their in-kind transfer out on 2026-10-12 (see [accounts.md](../accounts.md)).

Run: [`/performance`](../../.claude/commands/performance.md) (or `python -m scripts.performance report`).

## Why a rebuild is needed
IBKR PortfolioAnalyst (PA) already treats the transfer-out as a withdrawal, so the transfer day is not a loss. But PA still contains the three positions' returns **before** the transfer (TLT fell ~14% over the year; it was ~80% of the account when the history starts). "As if never existed" means removing them from every day, not just from the transfer date.

## Method (all arithmetic is in [scripts/performance.py](../../scripts/performance.py))
For every PA date *t*:

| Symbol | Meaning | Source |
|--------|---------|--------|
| `NAV_t` | account Net Liquidation Value | `nav-history.csv` (PA `get_pa_performance_all_periods`) |
| `f_t` | external deposit/withdrawal implied by PA: `NAV_t − NAV_{t−1}·(1 + r_PA,t)` | derived |
| `E_t` | market value of the excluded positions: ledger quantity × frozen close × FX | `excluded-ledger.csv` + `excluded-prices.csv` |
| `x_t` | capital moved between the framework sleeve and the excluded sleeve (buy `+cost`, sell `−proceeds`, transfer-out `−market value`) | ledger |
| `F_t` | framework value `NAV_t − E_t − cumulative excluded income` | derived |

Daily framework return: `r_t = (F_t − (f_t − x_t)) / F_{t−1} − 1` (flows treated as end-of-day, same convention as PA). Windows chain the daily returns geometrically. Because the excluded sleeve is zero from 2026-10-12, later days equal PA's own daily return.

**Window definitions** (from the last close on or before the start date to the `as-of` close): `1D` previous close · `1W` 7 calendar days · `MTD` last close of the prior month · `1M/3M/6M/N months` calendar-month offsets · `YTD` last close of the prior year · `1Y/N years` 12·N months · `Since start` first history date. A window that begins before the history (2025-10-13) shows `n/a`, or is clamped to the first date (marked `*`) when it overshoots by ≤ 7 days.

## Checks built in
- **Ledger ↔ transfer:** the script hard-fails if the ledger quantity on 2026-10-12 differs from the transferred quantity (TLT 100, RGL 60,000, LM8 1,800). It passes: 82 − 5 + 23 = 100 for TLT; RGL and LM8 reconcile fully to their buys.
- **Ledger ↔ PA:** the ledger's market value of the three positions (~$8,554 on 2026-10-09) matches PA's −$8,550 withdrawal on 2026-10-12 to within $10 — an independent confirmation that quantities and prices are right (a unit test asserts it).

## Known limitations (read before quoting a number)
1. **TLT's opening 82 shares are inferred**, not read from a trade record: `get_account_trades` only goes back to 2025-10-17 and shows no purchase, and PA shows no transfer-in spike, so they must have been in the account on the first PA date. The reconciliation above supports this.
2. **Dividends/interest on the excluded positions are not removed yet** (TLT paid roughly $25–30 a month on ~82–100 shares). The MCP exposes no dividend history. They sit in `F` as framework cash — negligible for YTD and later windows, but material for windows starting before ~Dec 2025 when the framework base was only ~$1.8k–$3k. To fix: add the amounts from the IBKR Activity Statement (Dividends section) to `excluded-income.csv` (`date,ticker,usd,note`); the script then removes them.
3. **Tiny early base.** From 2025-10-13 to mid-Nov 2025 the framework sleeve was ~$1.8k–$3.5k, so *since-start / 1Y* figures are dominated by that period's percentage swings. Prefer YTD, 6M and shorter windows for decisions.
4. **PA covers only ~1 year** of history per call; this repo stores it (`nav-history.csv`) and extends it on each run, so `N years` windows fill in over time.
5. PA's TWR is accurate to its own rounding (8 decimals) and its own valuation timing; ASX closes are mapped to the next US date.
6. Cash interest, fees and FX gains remain in the framework figures — they belong to the account, not to the excluded names.

## Files
| File | What | Maintained by |
|------|------|---------------|
| `nav-history.csv` | PA daily NAV, return, implied flow | `ingest` (each `/performance` run) |
| `excluded-ledger.csv` | quantity ledger of RGL/LM8/TLT incl. the transfer-out | frozen (history) |
| `excluded-prices.csv` | frozen daily closes for TLT, RGL, LM8, AUD/USD (to 2026-10-12) | frozen (history) |
| `excluded-income.csv` | dividends on excluded names (USD) | by hand from the Activity Statement |
| `latest.md` | last generated report | `/performance` |

## Glossary
Terms are defined in [framework/glossary.md](../../framework/glossary.md): **TWR**, **NLV**, **Max drawdown**, **Excluded sleeve**, **In-kind transfer**, **Framework account**.

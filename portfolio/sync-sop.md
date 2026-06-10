# Portfolio Sync — Standard Operating Procedure

Two brokers, two sync methods (IBKR has an API, Freedom Finance does not). Both now sync **directly into this repo** as snapshot files under [`portfolio/snapshots/`](snapshots/) — no external system (Notion or otherwise) involved. Each snapshot file is overwritten in place on every run; git history is the archive, so nothing is lost and the working tree always shows just the latest. After the snapshot is written, [holdings.md](holdings.md) is refreshed from it.

| Broker | Sync Method | Trigger Phrase |
|--------|-------------|----------------|
| **IBKR** | Automated via MCP (Interactive Brokers) + a public IBKR ticker-lookup CSV | *"Re-sync my IBKR portfolio"* |
| **IBKR (active orders)** | Automated via MCP (Interactive Brokers) — `get_account_orders` | *"Sync my active IBKR orders"* (or `/sync-orders`) |
| **Freedom Finance** | Manual — screenshot-based | *"Re-sync my Freedom Finance portfolio"* + attach screenshot |

> **Syncs commit straight to `main`** — no branch, no PR. They're low-risk, frequent, machine-generated data refreshes (a snapshot file, `holdings.md`, occasionally the lookup CSV), and `main`'s branch protection isn't actually enforced on this private repo anyway (GitHub requires a paid plan — Pro/Team/Enterprise — for branch protection on private repos; it was silently dropped when this repo went private). A PR-per-sync would just be ceremony without a real guard rail behind it. Each sync still lands as one clean, descriptive commit (`Sync IBKR portfolio — 2026-06-07`), so `git log` / `git revert` is always there if a sync needs undoing.
>
> **Framework and process changes are different** — those still go through a feature branch + PR by convention (it's the audit trail for *why* the framework evolved, not a data refresh, and worth a review pass even without enforced protection). See [CLAUDE.md](../CLAUDE.md).

---

## IBKR Portfolio Sync

### Key Resources

| Resource | Value |
|----------|-------|
| IBKR Account | U19421206 |
| Ticker Lookup CSV (live source) | `https://www.interactivebrokers.com/download/fracshare_stk.csv` — IBKR's own public download, no auth/MCP needed |
| Ticker Lookup CSV (stored fallback) | [`portfolio/reference/ibkr-ticker-lookup.csv`](../portfolio/reference/ibkr-ticker-lookup.csv) — last-known-good copy, committed to this repo |
| CSV columns | `#SYMBOL, MAIN_EXCHANGE, DESCRIPTION, IB_CONTRACT_ID, SCHEDULED_INELIGIBILTY_DATE` |
| Snapshot file | [`portfolio/snapshots/ibkr.md`](snapshots/ibkr.md) |

### Steps Claude Performs

1. **Fetch live positions** — `get_account_positions` via the Interactive Brokers MCP for account U19421206 (contract IDs, shares, market prices, avg cost, unrealized P&L).
2. **Fetch cash balances** — `get_account_balances` via the same MCP. It returns one entry per currency (`cash_balance`, `settled_cash`, `net_liquidation_value`, `stock_market_value`, `unrealized_pnl`, `exchange_rate`), plus a `BASE` row that's the whole account consolidated into USD. This is also the *correct* way to get a live, broker-reported FX rate for any non-USD currency the account holds (e.g. EUR) — use the `exchange_rate` field directly to convert that currency's cash and position values to USD-equivalents. Never assume or look up an FX rate elsewhere; if `get_account_balances` doesn't return a rate for a currency you need, say so rather than estimating one (per the "never invent or estimate financial data" rule).
3. **Resolve tickers** — fetch the ticker lookup CSV from the live source (`https://www.interactivebrokers.com/download/fracshare_stk.csv`).
   - **If the live fetch succeeds:** use it to resolve contract IDs → tickers via the `IB_CONTRACT_ID` column, *and* overwrite [`portfolio/reference/ibkr-ticker-lookup.csv`](../portfolio/reference/ibkr-ticker-lookup.csv) with the freshly fetched copy so it stays the up-to-date fallback (commit it alongside the snapshot in the same direct-to-`main` commit).
   - **If the live fetch fails** (network error, IBKR changes/removes the URL, etc.): fall back to the stored copy at `portfolio/reference/ibkr-ticker-lookup.csv`, note in the snapshot file and the commit message that the live source was unreachable and the stored copy was used (and how stale it is, per its last commit date), and don't overwrite it with anything.
   - Anything still unmatched after lookup gets flagged `CONID_XXXXXXX`.
4. **Write the snapshot** — overwrite [`portfolio/snapshots/ibkr.md`](snapshots/ibkr.md) with:
   - a header (account, sync timestamp, account-summary headline figures: net liquidation, gross position value, total cash);
   - the positions table: Ticker · Shares · Market Price · Market Value · Avg Cost · Unrealized P&L · P&L % · Currency · Contract ID;
   - a **Cash Balances** table, one row per currency the account holds: Currency · Cash Balance · Settled Cash · FX Rate → USD · USD Equivalent (the last column = `cash_balance × exchange_rate`, computed directly from `get_account_balances` — not estimated), plus a totals row.
5. **Refresh holdings.md** — recompute portfolio weights (now over the *whole* account — positions **and** cash — using each broker's net liquidation value as the denominator) and update [holdings.md](holdings.md):
   - the relevant ticker rows (weight %, broker; leave score/last-review columns untouched — those come from `/rescore`);
   - a **`CASH (IBKR)`** row with its USD-equivalent total (sum of the USD-equivalent column from the Cash Balances table) and weight %.
6. **Commit straight to `main`** — stage the snapshot, `holdings.md`, and (if refreshed) the lookup CSV, and commit directly to `main` with the message `Sync IBKR portfolio — YYYY-MM-DD`. No branch, no PR — see the note at the top of this file for why.

**Required MCP connections:** Interactive Brokers only — the ticker lookup is now a plain HTTP fetch (with a repo-stored fallback), no longer dependent on Google Drive or Notion.

### Troubleshooting

- **"No approval received" (IBKR):** disconnect/reconnect the MCP in Settings → Connections, complete OAuth. Verify consent at Client Portal → Settings → Manage Third-Party Consents (should list Anthropic + U19421206).
- **Ticker lookup URL unreachable or returns something unexpected:** use the stored fallback CSV (`portfolio/reference/ibkr-ticker-lookup.csv`), flag it clearly in the snapshot and commit message ("live source unavailable, used fallback dated [last commit date]"), and consider opening a `decisions/` note if the URL appears to have permanently changed — that's a framework-infrastructure change worth tracking (and would go through the normal branch + PR convention, since it's a process change, not a data sync).
- **New position shows `CONID_XXXXXXX`:** ticker missing from both the live and stored CSV — look it up in IBKR Client Portal or TWS Positions tab and add it to the snapshot manually, noting the gap.

---

## IBKR Active Orders Sync

### Key Resources

| Resource | Value |
|----------|-------|
| IBKR Account | U19421206 |
| Snapshot file | [`portfolio/snapshots/ibkr-orders.md`](snapshots/ibkr-orders.md) |

### Steps Claude Performs

1. **Fetch all orders** — `get_account_orders` via the Interactive Brokers MCP for account U19421206. This returns *every* order on record (order ID, side, symbol, order type, status, quantity, fill quantities, limit price, time in force, order time) — not just the ones still live.
2. **Filter to active/working orders** — keep only orders whose status means the order is still live and could fill (e.g. `NEW`, `SUBMITTED`, `PRESUBMITTED`, `PARTIALLY_FILLED`). Exclude:
   - `REPLACED` — this specific order ID was superseded by a later modification (price/qty change creates a new order ID). If the replacement is still live, it appears separately with its own order ID and an active status.
   - `CANCELLED`, `FILLED`, `EXPIRED`, `INACTIVE` — no longer working.
   - If a status shows up that doesn't clearly fall into either bucket, don't guess — ask, then record the resolution here so future syncs handle it automatically.
3. **Resolve tickers** — no separate lookup needed; each order's `primary_description` (e.g. `"Sell 20 NKE"`) already names the ticker.
4. **Write the snapshot** — overwrite [`portfolio/snapshots/ibkr-orders.md`](snapshots/ibkr-orders.md) with:
   - a header (account, sync timestamp, count of active orders, count of non-active orders excluded);
   - the active-orders table: Order ID · Side · Ticker · Qty · Order Type · Limit Price · Time in Force · Status · Order Placed (UTC), sorted alphabetically by ticker (matching the positions table convention);
   - a brief flag for any ticker whose only order(s) in the raw fetch are non-active (e.g. `REPLACED` with no live successor) — that's a signal a previously-placed order may no longer be working, worth a manual check in TWS/Client Portal if one was expected.
5. **Commit straight to `main`** — same rationale as the portfolio sync (low-risk, frequent, machine-generated data refresh, no enforced branch protection on this private repo): commit message `Sync IBKR active orders — YYYY-MM-DD`. See the note at the top of this file.

**Required MCP connections:** Interactive Brokers only.

### Troubleshooting

- **"No approval received" (IBKR):** same fix as the portfolio sync — disconnect/reconnect the MCP in Settings → Connections, complete OAuth.
- **Unfamiliar order status:** don't classify it as active or inactive by guessing — ask the user, then add it to the active/non-active lists in step 2 above so it's handled automatically next time.

---

## Freedom Finance Portfolio Sync

### Key Resources

| Resource | Value |
|----------|-------|
| Account | Freedom24 |
| Screenshot source | User-provided image (Freedom24 app or web) |
| Snapshot file | [`portfolio/snapshots/freedom-finance.md`](snapshots/freedom-finance.md) |

### Steps Claude Performs

1. **Read the positions screenshot** — extract Ticker · Company · Qty · Avg Price · Current Value · Return. If unclear/incomplete, ask for a re-send rather than guess.
2. **Get the cash balance too** — the "Opened positions" view only shows equity positions, not cash. Ask the user for a second screenshot of the account/balance view (e.g. the **Accounts** tab, or wherever Freedom24 shows "Available for withdrawal" / cash / total account value) so cash isn't silently dropped from the sync. If the user can't provide one, write the snapshot and `holdings.md` with positions only and **clearly flag that cash wasn't captured this round** — don't estimate or carry forward a stale figure.
3. **Parse the portfolio summary** — Total Value, Period Return, structured-product labels if visible, plus whatever the balance screenshot shows (cash balance, total account value, currency).
4. **Match tickers** — normalize format (`MSFT.US` → `MSFT`); flag unrecognized ones `UNKNOWN_TICKER`.
5. **Write the snapshot** — overwrite [`portfolio/snapshots/freedom-finance.md`](snapshots/freedom-finance.md) with a header (account, sync timestamp), the summary block, the positions table (Ticker · Company · Qty · Avg Price · Current Value · Return % · Product Type · Currency), and a **Cash Balance** line/table (currency, amount, and — if the app shows it — total account value including cash). If cash wasn't captured this round, say so explicitly here rather than leaving it ambiguous.
6. **Refresh holdings.md** — update the relevant ticker rows (weight %, broker — same method as IBKR, weight = value ÷ broker's total account value including cash), and add/update a **`CASH (Freedom24)`** row with its amount and weight %. If cash wasn't captured this sync, leave that row's figures as they were and note the staleness rather than guessing.
7. **Commit straight to `main`** — stage the snapshot and `holdings.md`, and commit directly to `main` with the message `Sync Freedom Finance portfolio — YYYY-MM-DD`. No branch, no PR — see the note at the top of this file for why.

**Required setup:** a clear screenshot of the Freedom24 portfolio. No MCP connections needed beyond what the session already has.

### Troubleshooting

- **Blurry/cut-off screenshot:** ask for a clearer one. Never guess values.
- **Unrecognized ticker:** flag `UNKNOWN_TICKER` in the snapshot, ask the user to confirm manually.
- **Freedom24 UI changes layout:** update the extraction logic in steps 1–2 and note the change in the sync commit message.

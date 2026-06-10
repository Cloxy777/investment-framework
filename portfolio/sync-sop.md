# Portfolio Sync — Standard Operating Procedure

IBKR has three independent automated syncs — **positions**, **cash balances**, and **active orders** — each with its own granular command and its own commit, since they're refreshed at different cadences and from different MCP calls. `/sync-portfolio` runs all three IBKR syncs in one pass with a single combined commit, and/or runs the Freedom Finance manual flow (which has no API and stays screenshot-based regardless). All syncs write **directly into this repo** as snapshot files under [`portfolio/snapshots/`](snapshots/) — no external system (Notion or otherwise) involved. Snapshot files (or the relevant section within them) are overwritten in place on every run; git history is the archive, so nothing is lost and the working tree always shows just the latest. After a snapshot section is written, [holdings.md](holdings.md) is refreshed from it.

| Sync | Method | Trigger Phrase |
|------|--------|----------------|
| **IBKR positions** (`/sync-positions`) | Automated via MCP (Interactive Brokers) — `get_account_positions` + ticker-lookup CSV | *"Sync my IBKR positions"* |
| **IBKR cash balances** (`/sync-balances`) | Automated via MCP (Interactive Brokers) — `get_account_balances` | *"Sync my IBKR cash balances"* |
| **IBKR active orders** (`/sync-orders`) | Automated via MCP (Interactive Brokers) — `get_account_orders` | *"Sync my active IBKR orders"* |
| **IBKR full sync** (`/sync-portfolio`) | Runs the three IBKR syncs above, one combined commit | *"Re-sync my IBKR portfolio"* |
| **Freedom Finance** (`/sync-portfolio`) | Manual — screenshot-based | *"Re-sync my Freedom Finance portfolio"* + attach screenshots |

> **Syncs commit straight to `main`** — no branch, no PR. They're low-risk, frequent, machine-generated data refreshes (a snapshot file or section, `holdings.md`, occasionally the lookup CSV), and `main`'s branch protection isn't actually enforced on this private repo anyway (GitHub requires a paid plan — Pro/Team/Enterprise — for branch protection on private repos; it was silently dropped when this repo went private). A PR-per-sync would just be ceremony without a real guard rail behind it. Each sync lands as one clean, descriptive commit — `Sync IBKR positions — YYYY-MM-DD`, `Sync IBKR cash balances — YYYY-MM-DD`, `Sync IBKR active orders — YYYY-MM-DD`, the combined `Sync IBKR portfolio — YYYY-MM-DD` (from `/sync-portfolio`), or `Sync Freedom Finance portfolio — YYYY-MM-DD` — so `git log` / `git revert` is always there if a sync needs undoing.
>
> **Framework and process changes are different** — those still go through a feature branch + PR by convention (it's the audit trail for *why* the framework evolved, not a data refresh, and worth a review pass even without enforced protection). See [CLAUDE.md](../CLAUDE.md).

---

## IBKR Positions Sync

### Key Resources

| Resource | Value |
|----------|-------|
| IBKR Account | U19421206 |
| Ticker Lookup CSV (live source) | `https://www.interactivebrokers.com/download/fracshare_stk.csv` — IBKR's own public download, no auth/MCP needed |
| Ticker Lookup CSV (stored fallback) | [`portfolio/reference/ibkr-ticker-lookup.csv`](../portfolio/reference/ibkr-ticker-lookup.csv) — last-known-good copy, committed to this repo |
| CSV columns | `#SYMBOL, MAIN_EXCHANGE, DESCRIPTION, IB_CONTRACT_ID, SCHEDULED_INELIGIBILTY_DATE` |
| Snapshot file | [`portfolio/snapshots/ibkr.md`](snapshots/ibkr.md) — updates the positions table and the position-derived header fields (Gross Position Value, Unrealized P&L, "Positions last synced") |

### Steps Claude Performs

1. **Fetch live positions** — `get_account_positions` via the Interactive Brokers MCP for account U19421206 (contract IDs, shares, market prices, avg cost, unrealized P&L).
2. **Resolve tickers** — fetch the ticker lookup CSV from the live source (`https://www.interactivebrokers.com/download/fracshare_stk.csv`).
   - **If the live fetch succeeds:** use it to resolve contract IDs → tickers via the `IB_CONTRACT_ID` column, *and* overwrite [`portfolio/reference/ibkr-ticker-lookup.csv`](../portfolio/reference/ibkr-ticker-lookup.csv) with the freshly fetched copy so it stays the up-to-date fallback (commit it alongside the snapshot in the same commit).
   - **If the live fetch fails** (network error, IBKR changes/removes the URL, etc.): fall back to the stored copy at `portfolio/reference/ibkr-ticker-lookup.csv`, note in the snapshot file and the commit message that the live source was unreachable and the stored copy was used (and how stale it is, per its last commit date), and don't overwrite it with anything.
   - Anything still unmatched after lookup gets flagged `CONID_XXXXXXX`.
3. **Update the snapshot** — in [`portfolio/snapshots/ibkr.md`](snapshots/ibkr.md), overwrite:
   - the positions table: Ticker · Shares · Market Price · Market Value · Avg Cost · Unrealized P&L · P&L % · Currency · Contract ID;
   - the position-derived header fields: Gross Position Value, Unrealized P&L, and the "Positions last synced" timestamp.
   - Leave the Cash Balances table and the cash-derived header fields (Net Liquidation, Total Cash, "Cash balances last synced") untouched — those reflect the most recent `/sync-balances` run, which may be a different date.
4. **Refresh holdings.md** — update the relevant ticker rows (weight %, broker; leave score/last-review columns untouched — those come from `/rescore`). Weight = position market value ÷ Net Liquidation Value, using the Net Liquidation figure currently in `ibkr.md` (from the most recent `/sync-balances` run). If that figure isn't from today, note its date so the weight isn't read as fresher than it is.
5. **Commit straight to `main`** — stage `ibkr.md`, `holdings.md`, and (if refreshed) the lookup CSV, with the message `Sync IBKR positions — YYYY-MM-DD`. No branch, no PR — see the note at the top of this file.

**Required MCP connections:** Interactive Brokers only — the ticker lookup is now a plain HTTP fetch (with a repo-stored fallback), no longer dependent on Google Drive or Notion.

### Troubleshooting

- **"No approval received" (IBKR):** disconnect/reconnect the MCP in Settings → Connections, complete OAuth. Verify consent at Client Portal → Settings → Manage Third-Party Consents (should list Anthropic + U19421206).
- **Ticker lookup URL unreachable or returns something unexpected:** use the stored fallback CSV (`portfolio/reference/ibkr-ticker-lookup.csv`), flag it clearly in the snapshot and commit message ("live source unavailable, used fallback dated [last commit date]"), and consider opening a `decisions/` note if the URL appears to have permanently changed — that's a framework-infrastructure change worth tracking (and would go through the normal branch + PR convention, since it's a process change, not a data sync).
- **New position shows `CONID_XXXXXXX`:** ticker missing from both the live and stored CSV — look it up in IBKR Client Portal or TWS Positions tab and add it to the snapshot manually, noting the gap.

---

## IBKR Cash Balances Sync

### Key Resources

| Resource | Value |
|----------|-------|
| IBKR Account | U19421206 |
| Snapshot file | [`portfolio/snapshots/ibkr.md`](snapshots/ibkr.md) — updates the Cash Balances table and the cash-derived header fields (Net Liquidation, Total Cash, "Cash balances last synced") |

### Steps Claude Performs

1. **Fetch cash balances** — `get_account_balances` via the Interactive Brokers MCP. It returns one entry per currency (`cash_balance`, `settled_cash`, `net_liquidation_value`, `stock_market_value`, `unrealized_pnl`, `exchange_rate`), plus a `BASE` row that's the whole account consolidated into USD. This is also the *correct* way to get a live, broker-reported FX rate for any non-USD currency the account holds (e.g. EUR) — use the `exchange_rate` field directly to convert that currency's cash and position values to USD-equivalents. Never assume or look up an FX rate elsewhere; if `get_account_balances` doesn't return a rate for a currency you need, say so rather than estimating one (per the "never invent or estimate financial data" rule).
2. **Update the snapshot** — in [`portfolio/snapshots/ibkr.md`](snapshots/ibkr.md), overwrite:
   - the Cash Balances table: one row per currency the account holds — Currency · Cash Balance · Settled Cash · FX Rate → USD · USD Equivalent (the last column = `cash_balance × exchange_rate`, computed directly from `get_account_balances` — not estimated), plus a totals row;
   - the cash-derived header fields: Net Liquidation, Total Cash (USD-equiv), and the "Cash balances last synced" timestamp;
   - the USD-equivalent of any non-USD position (e.g. XEON), recomputed using the freshly fetched FX rate.
   - Leave the positions table and the position-derived header fields (Gross Position Value, Unrealized P&L, "Positions last synced") untouched — those reflect the most recent `/sync-positions` run.
3. **Refresh holdings.md** — update the `CASH (IBKR)` row (USD-equivalent total = sum of the USD-equivalent column from the Cash Balances table, and weight %), and **recompute weight % for every row** — Net Liquidation Value, the shared denominator, just changed — using position market values from the most recent `/sync-positions` run. If that sync isn't from today, note its date.
4. **Commit straight to `main`** — stage `ibkr.md` and `holdings.md`, with the message `Sync IBKR cash balances — YYYY-MM-DD`. No branch, no PR — see the note at the top of this file.

**Required MCP connections:** Interactive Brokers only.

### Troubleshooting

- **"No approval received" (IBKR):** same fix as the positions sync — disconnect/reconnect the MCP in Settings → Connections, complete OAuth.
- **Currency missing from `get_account_balances`:** don't estimate its USD value — flag it explicitly in the snapshot and ask rather than guessing a rate.

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
5. **Commit straight to `main`** — same rationale as the other syncs (low-risk, frequent, machine-generated data refresh, no enforced branch protection on this private repo): commit message `Sync IBKR active orders — YYYY-MM-DD`. See the note at the top of this file.

**Required MCP connections:** Interactive Brokers only.

### Troubleshooting

- **"No approval received" (IBKR):** same fix as the positions sync — disconnect/reconnect the MCP in Settings → Connections, complete OAuth.
- **Unfamiliar order status:** don't classify it as active or inactive by guessing — ask the user, then add it to the active/non-active lists in step 2 above so it's handled automatically next time.

---

## Full IBKR Sync (`/sync-portfolio`)

`/sync-portfolio`, called with no argument or with "IBKR"/"both", runs all three IBKR syncs above **in one pass with a single combined commit** (rather than three separate ones), since they touch overlapping files (`ibkr.md`, `holdings.md`):

1. Run **IBKR Positions Sync** steps 1–3 — fetch positions, resolve tickers, update the positions table and position-derived header fields in `ibkr.md`.
2. Run **IBKR Cash Balances Sync** steps 1–2 — fetch balances, update the Cash Balances table, cash-derived header fields, and any non-USD position conversions in `ibkr.md`.
3. Run **IBKR Active Orders Sync** steps 1–4 — fetch orders, filter to active, write `ibkr-orders.md`.
4. **Refresh holdings.md once**, using the just-fetched positions and balances together (no staleness caveats needed — both are fresh): the ticker weight%/broker columns and the `CASH (IBKR)` row.
5. **Commit straight to `main`** — stage `ibkr.md`, `ibkr-orders.md`, `holdings.md`, and the lookup CSV if refreshed, in **one** commit: `Sync IBKR portfolio — YYYY-MM-DD`. No branch, no PR — see the note at the top of this file.

If the user only wants part of this refreshed (e.g. *"just check my orders"* or *"how much cash do I have"*), use the relevant granular command (`/sync-positions`, `/sync-balances`, `/sync-orders`) instead — each is self-contained and commits independently.

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

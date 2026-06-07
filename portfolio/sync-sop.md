# Portfolio Sync — Standard Operating Procedure

Two brokers, two sync methods (IBKR has an API, Freedom Finance does not). Both now sync **directly into this repo** as snapshot files under [`portfolio/snapshots/`](snapshots/) — no external system (Notion or otherwise) involved. Each snapshot file is overwritten in place on every run; git history is the archive, so nothing is lost and the working tree always shows just the latest. After the snapshot is written, [holdings.md](holdings.md) is refreshed from it.

| Broker | Sync Method | Trigger Phrase |
|--------|-------------|----------------|
| **IBKR** | Automated via MCP (Interactive Brokers + Google Drive) | *"Re-sync my IBKR portfolio"* |
| **Freedom Finance** | Manual — screenshot-based | *"Re-sync my Freedom Finance portfolio"* + attach screenshot |

> Because `main` is protected, every sync lands as a commit on a short-lived branch with a PR opened against `main` (e.g. `sync/ibkr-2026-06-07`, titled `Sync IBKR portfolio — 2026-06-07`). Merge it once you've sanity-checked the numbers — it's a fast review since it's pure data refresh.

---

## IBKR Portfolio Sync

### Key Resources

| Resource | Value |
|----------|-------|
| IBKR Account | U19421206 |
| Ticker Lookup CSV (Google Drive) | File ID: `1qXn-oQCMGIHemmzssoR4Eckw3xvXzugf` |
| CSV columns | `#SYMBOL, MAIN_EXCHANGE, DESCRIPTION, IB_CONTRACT_ID, SCHEDULED_INELIGIBILITY_DATE` |
| Snapshot file | [`portfolio/snapshots/ibkr.md`](snapshots/ibkr.md) |

### Steps Claude Performs

1. **Fetch live positions** — `get_account_positions` via the Interactive Brokers MCP for account U19421206 (contract IDs, shares, market prices, avg cost, unrealized P&L).
2. **Resolve tickers** — download the ticker lookup CSV from Google Drive (`download_file_content`, file `1qXn-oQCMGIHemmzssoR4Eckw3xvXzugf`) and match contract IDs via the `IB_CONTRACT_ID` column. Anything unmatched gets flagged `CONID_XXXXXXX`.
3. **Write the snapshot** — overwrite [`portfolio/snapshots/ibkr.md`](snapshots/ibkr.md) with a header (account, sync timestamp) and a full positions table: Ticker · Shares · Market Price · Market Value · Avg Cost · Unrealized P&L · P&L % · Currency · Contract ID.
4. **Refresh holdings.md** — recompute portfolio weights from the new snapshot and update the relevant rows in [holdings.md](holdings.md) (ticker, weight %, broker; leave score/last-review columns untouched — those come from `/rescore`).
5. **Open a PR** — commit both files on a branch named `sync/ibkr-YYYY-MM-DD`, push, and open a PR titled `Sync IBKR portfolio — YYYY-MM-DD` against `main`.

**Required MCP connections:** Interactive Brokers, Google Drive.

### Troubleshooting

- **"No approval received" (IBKR or Google Drive):** disconnect/reconnect the MCP, complete OAuth. For IBKR, verify consent at Client Portal → Settings → Manage Third-Party Consents (should list Anthropic + U19421206).
- **New position shows `CONID_XXXXXXX`:** ticker missing from the CSV — look it up in IBKR Client Portal or TWS Positions tab and add it to the snapshot manually, noting the gap.

---

## Freedom Finance Portfolio Sync

### Key Resources

| Resource | Value |
|----------|-------|
| Account | Freedom24 |
| Screenshot source | User-provided image (Freedom24 app or web) |
| Snapshot file | [`portfolio/snapshots/freedom-finance.md`](snapshots/freedom-finance.md) |

### Steps Claude Performs

1. **Read the screenshot** — extract Ticker · Company · Qty · Avg Price · Current Value · Return. If unclear/incomplete, ask for a re-send rather than guess.
2. **Parse the portfolio summary** — Total Value, Period Return, structured-product labels if visible.
3. **Match tickers** — normalize format (`MSFT.US` → `MSFT`); flag unrecognized ones `UNKNOWN_TICKER`.
4. **Write the snapshot** — overwrite [`portfolio/snapshots/freedom-finance.md`](snapshots/freedom-finance.md) with a header (account, sync timestamp), the summary block, and the positions table: Ticker · Company · Qty · Avg Price · Current Value · Return % · Product Type · Currency.
5. **Refresh holdings.md** — same as IBKR: update weights/broker for the relevant rows.
6. **Open a PR** — branch `sync/freedom-finance-YYYY-MM-DD`, PR titled `Sync Freedom Finance portfolio — YYYY-MM-DD`.

**Required setup:** a clear screenshot of the Freedom24 portfolio. No MCP connections needed beyond what the session already has.

### Troubleshooting

- **Blurry/cut-off screenshot:** ask for a clearer one. Never guess values.
- **Unrecognized ticker:** flag `UNKNOWN_TICKER` in the snapshot, ask the user to confirm manually.
- **Freedom24 UI changes layout:** update the extraction logic in steps 1–2 and note the change in the PR description.

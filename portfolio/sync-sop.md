# Portfolio Sync — Standard Operating Procedures

Two brokers, two sync methods (IBKR has an API, Freedom Finance does not). Both sync into Notion; update [holdings.md](holdings.md) from the resulting snapshot afterward.

| Broker | Sync Method | Trigger Phrase |
|--------|-------------|----------------|
| **IBKR** | Automated via MCP (Interactive Brokers + Google Drive + Notion) | *"Re-sync my IBKR portfolio to Notion"* |
| **Freedom Finance** | Manual — screenshot-based | *"Re-sync my Freedom Finance portfolio to Notion"* + attach screenshot |

---

## IBKR Portfolio Sync

### Key Resources

| Resource | Value |
|----------|-------|
| IBKR Account | U19421206 |
| Notion Portfolio DB | `https://app.notion.com/p/12625679411d4af3b8e609ae210ceefa` |
| Ticker Lookup CSV (Google Drive) | File ID: `1qXn-oQCMGIHemmzssoR4Eckw3xvXzugf` |
| CSV columns | `#SYMBOL, MAIN_EXCHANGE, DESCRIPTION, IB_CONTRACT_ID, SCHEDULED_INELIGIBILITY_DATE` |

### Steps Claude Performs

1. **Fetch live positions** — `get_account_positions` via the Interactive Brokers MCP for account U19421206 (contract IDs, shares, market prices, avg cost, unrealized P&L).
2. **Download ticker lookup CSV** from Google Drive (`download_file_content`, file `1qXn-oQCMGIHemmzssoR4Eckw3xvXzugf`); resolve contract IDs → tickers via `IB_CONTRACT_ID` column. Anything unmatched gets flagged `CONID_XXXXXXX`.
3. **Update the Notion database** — clear existing rows, recreate one row per position: Ticker · Shares · Market Price · Market Value · Avg Cost · Unrealized P&L · P&L % · Currency · Contract ID.
4. **Create a snapshot page** titled `IBKR Portfolio Snapshot — [Month Day, Year]`, parent `📊 IBKR Portfolio Sync — SOP`, icon 📸, containing the full positions table.
5. **Remove old snapshots** — delete all `IBKR Portfolio Snapshot — *` pages except the new one. On failure, log under `⚠️ Cleanup Notes` and continue. Max 1 snapshot retained.

**Required MCP connections:** Interactive Brokers, Google Drive, Notion (Settings → Connections).

### Troubleshooting

- **"No approval received" (IBKR or Google Drive):** Disconnect/reconnect the MCP in Settings → Connections, complete OAuth. For IBKR, verify consent at Client Portal → Settings → Manage Third-Party Consents (should list Anthropic + U19421206).
- **New position shows `CONID_XXXXXXX`:** ticker missing from CSV — look it up in IBKR Client Portal or TWS Positions tab and update the Notion row manually.
- **Notion DB URL changed:** update the Key Resources table above and tell Claude the new URL on next sync.

---

## Freedom Finance Portfolio Sync

### Key Resources

| Resource | Value |
|----------|-------|
| Account | Freedom24 |
| Screenshot source | User-provided image (Freedom24 app or web) |
| Notion Portfolio DB | To be linked (create FF DB or reuse IBKR structure) |

### Steps Claude Performs

1. **Read the screenshot** — extract Ticker · Company · Qty · Avg Price · Current Value · Return. If unclear/incomplete, ask for a re-send rather than guess.
2. **Parse portfolio summary** — Total Value, Period Return, structured-product labels if visible.
3. **Match tickers** — normalize format (`MSFT.US` → `MSFT`); flag unrecognized ones `UNKNOWN_TICKER`.
4. **Update Notion DB** — clear & recreate rows: Ticker · Company · Qty · Avg Price · Current Value · Return % · Product Type · Currency.
5. **Create snapshot page** titled `Freedom Finance Portfolio Snapshot — [Month Day, Year]`, parent `📋 Freedom Finance Portfolio Sync — SOP`, icon 📸, with summary block + positions table.
6. **Remove old snapshots**, same rule as IBKR (max 1 retained).

**Required setup:** Notion MCP connected + a clear screenshot of the Freedom24 portfolio. No other MCP needed.

### Troubleshooting

- **Blurry/cut-off screenshot:** ask for a clearer one. Never guess values.
- **Unrecognized ticker:** flag `UNKNOWN_TICKER`, ask user to confirm manually.
- **Freedom24 UI changes layout:** update the extraction logic in steps 1–2 and note the change in the snapshot page.

---

## Notion Page IDs — Sync Infrastructure

| Page | ID |
|------|----|
| Portfolio Sync — SOP (root) | `374165d9-fe04-8069-b092-f830383490ea` |
| 📊 IBKR Portfolio Sync — SOP | `36e165d9-fe04-81c8-962a-c11fd6013c89` |
| 📋 Freedom Finance Portfolio Sync — SOP | `374165d9-fe04-81aa-85b1e0e5b47efe49` |
| IBKR Portfolio Snapshot — June 3, 2026 | `374165d9-fe04-812b-bdb4-ef924580c1f1` |
| Freedom Finance Snapshot — May 2025 | `374165d9-fe04-8162-92a3-d2bd69a89641` |

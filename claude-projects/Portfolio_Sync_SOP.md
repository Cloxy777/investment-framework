# Portfolio Sync — Standard Operating Procedures
**Both brokers: IBKR + Freedom Finance**
*Compiled from Notion · Last updated: June 2026*

---

## 📋 Overview

There are two portfolios to sync. They use different methods because IBKR has an API and Freedom Finance does not.

| Broker | Sync Method | Trigger |
|--------|-------------|---------|
| **IBKR** | Automated via MCP (Interactive Brokers + Google Drive + Notion) | Say: *"Re-sync my IBKR portfolio to Notion"* |
| **Freedom Finance** | Manual — screenshot-based | Say: *"Re-sync my Freedom Finance portfolio to Notion"* + attach screenshot |

---

## 📊 IBKR Portfolio Sync SOP

### ⚡ Trigger Phrase
Send Claude exactly:
> **"Re-sync my IBKR portfolio to Notion"**

No other input needed. Claude handles every step automatically.

---

### 🔗 Key Resources

| Resource | Value |
|----------|-------|
| IBKR Account | U19421206 |
| Notion Portfolio DB | `https://app.notion.com/p/12625679411d4af3b8e609ae210ceefa` |
| Ticker Lookup CSV (Google Drive) | File ID: `1qXn-oQCMGIHemmzssoR4Eckw3xvXzugf` |
| CSV columns | `#SYMBOL, MAIN_EXCHANGE, DESCRIPTION, IB_CONTRACT_ID, SCHEDULED_INELIGIBILITY_DATE` |

---

### 🔄 Steps Claude Performs

**Step 1 — Fetch live positions from IBKR**
Calls `get_account_positions` via the Interactive Brokers MCP. Returns contract IDs, share counts, market prices, average costs, and unrealized P&L for account U19421206.

**Step 2 — Download ticker lookup CSV from Google Drive**
Fetches file `1qXn-oQCMGIHemmzssoR4Eckw3xvXzugf` via Google Drive MCP (`download_file_content`). Greps contract IDs against the `IB_CONTRACT_ID` column to resolve tickers.

**Step 3 — Match contract IDs to tickers**
For any contract ID found in the CSV → uses that ticker. For any not found → flags as `CONID_XXXXXXX` for manual review.

**Step 4 — Update Notion database**
Opens the IBKR Portfolio database, clears existing rows, and re-creates one row per position with:
Ticker · Shares · Market Price · Market Value · Avg Cost · Unrealized P&L · P&L % · Currency · Contract ID

**Step 5 — Create snapshot page**
Creates a new child page under the IBKR Sync SOP page with:
- **Title format:** `IBKR Portfolio Snapshot — [Full date, e.g. June 3, 2026]`
- **Parent:** `📊 IBKR Portfolio Sync — SOP`
- **Icon:** 📸
- **Content:** Full positions table with all columns

**Step 6 — Remove old snapshot pages**
Deletes all child pages matching `IBKR Portfolio Snapshot — *` except the one just created.
If deletion fails → logs under `⚠️ Cleanup Notes` in the snapshot page and continues.

---

### ✅ Required MCP Connections

All three must be connected in Claude Settings → Connections:
- **Interactive Brokers** — live position data
- **Google Drive** — ticker lookup CSV
- **Notion** — portfolio database updates

---

### 🛠 Troubleshooting

**"No approval received" from IBKR**
Go to Settings → Connections → Interactive Brokers → Disconnect → Reconnect. Complete full OAuth flow. Verify consent at IBKR Client Portal → Settings → Manage Third-Party Consents (should show Anthropic + account U19421206).

**"No approval received" from Google Drive**
Same fix: Disconnect and reconnect Google Drive MCP in Claude Settings.

**New position shows as CONID_XXXXXXX**
The CSV may not include that ticker. Look it up manually in IBKR Client Portal or TWS Positions tab, then update the Notion row directly.

**Notion database URL changed**
Update the URL in Key Resources above, then tell Claude the new URL on next sync.

---

### 🗂 Snapshot Spec

| Field | Rule |
|-------|------|
| Title | `IBKR Portfolio Snapshot — [Month Day, Year]` |
| Parent page | `📊 IBKR Portfolio Sync — SOP` |
| Icon | 📸 |
| Table columns | Ticker, Shares, Market Price, Market Value, Avg Cost, Unrealized P&L, P&L %, Currency, Contract ID |
| Max snapshots | 1 at a time — old ones deleted on each sync |

---

## 📋 Freedom Finance Portfolio Sync SOP

### ⚡ Trigger Phrase
Send Claude exactly this **plus a screenshot** of your Freedom24 portfolio:
> **"Re-sync my Freedom Finance portfolio to Notion"**

Claude reads the screenshot and handles every step without further input.

---

### 🔗 Key Resources

| Resource | Value |
|----------|-------|
| Freedom Finance Account | Freedom24 |
| Screenshot source | User-provided image (Freedom24 app or web) |
| Notion Portfolio DB | To be linked (create FF DB or reuse IBKR structure) |

---

### 🔄 Steps Claude Performs

**Step 1 — Read the screenshot**
Extracts all visible positions: Ticker · Company · Qty · Avg Price · Current Value · Return.
If the screenshot is unclear or missing fields, asks user to re-send before proceeding.

**Step 2 — Parse portfolio summary**
Extracts top-level metrics if visible: Total Value · Period Return · Structured product labels (capital protection type, fixed/potential return %).

**Step 3 — Match tickers**
Normalises ticker format (e.g. `MSFT.US` → `MSFT`). Flags any unrecognised tickers for manual review.

**Step 4 — Update Notion database**
Opens the Freedom Finance Portfolio database, clears existing rows, and re-creates one row per position with:
Ticker · Company · Qty · Avg Price · Current Value · Return % · Product Type · Currency

**Step 5 — Create snapshot page**
Creates a new child page under the Freedom Finance Sync SOP page with:
- **Title format:** `Freedom Finance Portfolio Snapshot — [Full date, e.g. June 3, 2026]`
- **Parent:** `📋 Freedom Finance Portfolio Sync — SOP`
- **Icon:** 📸
- **Content:** Portfolio summary (Total Value, Period Return) + full positions table

**Step 6 — Remove old snapshot pages**
Deletes all child pages matching `Freedom Finance Portfolio Snapshot — *` except the one just created.
If deletion fails → logs under `⚠️ Cleanup Notes` in the snapshot page and continues.

---

### ✅ Required Setup

- **Notion** MCP connected
- **User screenshot** of Freedom24 portfolio (no API available)
- No other MCP connections required

---

### 🛠 Troubleshooting

**Screenshot blurry or fields cut off**
Ask the user to re-send a clearer screenshot. Do not guess values.

**Ticker not recognised**
Flag as `UNKNOWN_TICKER` in the snapshot page and Notion row. Ask user to confirm the correct ticker manually.

**Notion database URL changed**
Update the URL in Key Resources above, then tell Claude the new URL on next sync.

**Freedom24 changes its UI layout**
Update the field extraction logic in Steps 1–2 to match the new layout. Note the change in the snapshot page body.

---

### 🗂 Snapshot Spec

| Field | Rule |
|-------|------|
| Title | `Freedom Finance Portfolio Snapshot — [Month Day, Year]` |
| Parent page | `📋 Freedom Finance Portfolio Sync — SOP` |
| Icon | 📸 |
| Table columns | Ticker, Company, Qty, Avg Price, Current Value, Return %, Product Type, Currency |
| Summary block | Total Value + Period Return at top of page (if visible in screenshot) |
| Max snapshots | 1 at a time — old ones deleted on each sync |

---

## 🗂 Notion Page IDs — Sync Infrastructure

| Page | ID |
|------|----|
| Portfolio Sync — SOP (root) | `374165d9-fe04-8069-b092-f830383490ea` |
| 📊 IBKR Portfolio Sync — SOP | `36e165d9-fe04-81c8-962a-c11fd6013c89` |
| 📋 Freedom Finance Portfolio Sync — SOP | `374165d9-fe04-81aa-85b1e0e5b47efe49` |
| IBKR Portfolio Snapshot — June 3, 2026 | `374165d9-fe04-812b-bdb4-ef924580c1f1` |
| Freedom Finance Snapshot — May 2025 | `374165d9-fe04-8162-92a3-d2bd69a89641` |

---

*Compiled: June 7, 2026 · Source: Notion Portfolio Sync SOP Pages*

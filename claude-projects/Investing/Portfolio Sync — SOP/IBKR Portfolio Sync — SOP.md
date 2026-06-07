# 📊 IBKR Portfolio Sync — SOP

This page documents the full process for syncing live IBKR positions into the Notion portfolio database. Just send Claude the trigger phrase and everything runs automatically.

## ⚡ Trigger phrase

Send Claude exactly this:

> **"Re-sync my IBKR portfolio to Notion"**
> 

That's it. Claude will handle every step below without further input.

---

## 🔗 Key resources

| Resource | Link / ID |
| --- | --- |
| Notion Portfolio DB | [IBKR Portfolio](https://www.notion.so/12625679411d4af3b8e609ae210ceefa?pvs=21) |
| Ticker Lookup CSV (Google Drive) | [https://drive.google.com/file/d/1qXn-oQCMGIHemmzssoR4Eckw3xvXzugf/view](https://drive.google.com/file/d/1qXn-oQCMGIHemmzssoR4Eckw3xvXzugf/view) |
| Drive File ID | `1qXn-oQCMGIHemmzssoR4Eckw3xvXzugf` |
| IBKR Account | `U19421206` |
| CSV columns | `#SYMBOL, MAIN_EXCHANGE, DESCRIPTION, IB_CONTRACT_ID, SCHEDULED_INELIGIBILITY_DATE` |

---

## 🔄 What Claude does — step by step

**Step 1 — Fetch live positions from IBKR**

Calls `get_account_positions` via the IBKR MCP. Returns contract IDs, share counts, market prices, average costs, and unrealized P&L for account U19421206.

**Step 2 — Download ticker lookup CSV from Google Drive**

Fetches file `1qXn-oQCMGIHemmzssoR4Eckw3xvXzugf` via Google Drive MCP (`download_file_content`). Greps contract IDs against the `IB_CONTRACT_ID` column to resolve tickers.

**Step 3 — Match contract IDs to tickers**

For any contract ID found in the CSV → uses that ticker. For any not found → flags as `CONID_XXXXXXX` for manual review.

**Step 4 — Update Notion**

Opens the IBKR Portfolio database, clears existing rows, and re-creates one row per position with: Ticker, Shares, Market Price, Market Value, Avg Cost, Unrealized P&L, P&L %, Currency, Contract ID.

**Step 5 — Create snapshot page**

Creates a new child page under this SOP titled **"IBKR Portfolio Snapshot — [Today's Date]"** (e.g. `IBKR Portfolio Snapshot — June 3, 2026`). The page contains a full table of all synced positions including: Ticker, Shares, Market Price, Market Value, Avg Cost, Unrealized P&L, P&L %, Currency, Contract ID. See **📄 Snapshot Page Creation** section below for exact spec.

**Step 6 — Remove old snapshot pages**

After the new snapshot page is confirmed created, searches for and deletes all previously existing pages matching the pattern `IBKR Portfolio Snapshot — *` that are **not** the one just created. See **🗑️ Old Snapshot Removal** section below for scope rules.

---

## ✅ Required MCP connections

All three must be connected in Claude Settings → Connections before the trigger phrase works:

- **Interactive Brokers** — live position data
- **Google Drive** — ticker lookup CSV
- **Notion** — portfolio database updates

---

## 🗂 Known positions (last synced: 2026-06-03 19:08 UTC)

| Ticker | Contract ID | Last P&L |
| --- | --- | --- |
| AMZN | 3691937 | +$549.74 ✅ |
| CSGP | 6726677 | -$31.00 🔴 |
| DUOL | 505002183 | -$1,756.44 🔴 |
| FSLY | 366131373 | 0 shares — excluded |
| GOOG | 208813720 | +$62.84 ✅ |
| KYIV | 807386041 | +$38.00 ✅ |
| META | 107113386 | -$23.51 🔴 |
| MSFT | 272093 | +$716.13 ✅ |
| NFLX | 15124833 | -$52.81 🔴 |
| NKE | 10291 | +$8.00 ✅ |
| NOW | 109911821 | +$397.21 ✅ |
| NVDA | 4815747 | +$596.20 ✅ |
| NVO | 10611 | +$2.00 ✅ |
| RBRK | 699030013 | +$72.70 ✅ |
| SPGI | 229629397 | +$7.01 ✅ |
| SPOT | 312496724 | -$7.32 🔴 |
| STIM | 324062325 | -$65.10 🔴 |
| TLT | 15547841 | -$249.28 🔴 |
| UBER | 365207014 | -$31.42 🔴 |
| V | 49462172 | -$1.51 🔴 |
| XEON | 46041702 | +€2.41 ✅ |
| ZS | 310621426 | -$14.40 🔴 |

---

## 📄 Snapshot Page Creation

This subsection governs how Claude creates the current-state portfolio page during a sync.

- **Title format:** `IBKR Portfolio Snapshot — [Full date, e.g. June 3, 2026]`
- **Parent:** This SOP page (`📊 IBKR Portfolio Sync — SOP`)
- **Timing:** Created during Step 5, after the Notion database has been updated in Step 4
- **Content:** A full table of all synced positions with columns — Ticker, Shares, Market Price, Market Value, Avg Cost, Unrealized P&L, P&L %, Currency, Contract ID
- **Icon:** 📸
- One snapshot page per sync — never accumulate more than one current page

---

## 🗑️ Old Snapshot Removal

This subsection governs how Claude removes stale portfolio snapshot pages during a sync.

- **Scope:** Only pages titled `IBKR Portfolio Snapshot — *` that are children of this SOP page
- **Trigger:** Runs immediately after Step 5 confirms the new snapshot page is created
- **Rule:** Delete **all** matching pages **except** the one just created in the current sync
- **Safety check:** Never delete the SOP page itself or any other child pages (e.g. this page, the Human Override Log, etc.)
- **If deletion fails:** Log the failure in the snapshot page body under a `⚠️ Cleanup Notes` section and continue — do not abort the sync

---

## 🛠 Troubleshooting

**IBKR returns "No approval received"**

Go to Settings → Connections → Interactive Brokers → Disconnect → Reconnect. Complete the full OAuth flow. Verify consent is active at Client Portal → Settings → Manage Third-Party Consents (should show Anthropic + account U19421206).

**Google Drive returns "No approval received"**

Same fix: Disconnect and reconnect Google Drive MCP in Claude Settings.

**New positions show as CONID_XXXXXXX**

The CSV may not include newer/less common tickers. Use IBKR Client Portal or TWS Positions tab to look up the ticker manually, then update the Notion row directly.

**Notion database URL changed**

Update the URL in the Key Resources table above, then tell Claude the new URL on next sync.

[IBKR Portfolio Snapshot — June 3, 2026](%F0%9F%93%8A%20IBKR%20Portfolio%20Sync%20%E2%80%94%20SOP/IBKR%20Portfolio%20Snapshot%20%E2%80%94%20June%203,%202026%20374165d9fe04812bbdb4ef924580c1f1.md)
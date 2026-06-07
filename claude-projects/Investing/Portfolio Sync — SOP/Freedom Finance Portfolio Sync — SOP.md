# 📋 Freedom Finance Portfolio Sync — SOP

This page documents the full process for syncing Freedom Finance (Freedom24) positions into the Notion portfolio database. Unlike IBKR, there is no API connection — sync is triggered by sending a screenshot of your Freedom24 portfolio.

## ⚡ Trigger phrase

Send Claude exactly this, along with a **screenshot** of your Freedom24 portfolio view:

> **"Re-sync my Freedom Finance portfolio to Notion"**
> 

Claude will read the screenshot and handle every step below without further input.

---

## 🔗 Key resources

| Resource | Link / ID |
| --- | --- |
| Freedom Finance Account | Freedom24 |
| Screenshot source | User-provided image (Freedom24 app or web) |
| Notion Portfolio DB | (to be linked — create Freedom Finance DB or reuse IBKR structure) |

---

## 🔄 What Claude does — step by step

**Step 1 — Read the screenshot**

Claude reads the Freedom24 screenshot provided by the user. Extracts all visible positions including: Ticker, Company, Qty, Avg Price, Current Value, Return. If the screenshot is unclear or missing fields, Claude asks the user to re-send before proceeding.

**Step 2 — Parse portfolio summary**

Extracts top-level portfolio metrics if visible: Total value, Period return, and any structured product labels (e.g. capital protection type, fixed/potential return %).

**Step 3 — Match tickers**

Normalises ticker format (e.g. `MSFT.US` → `MSFT`). Flags any unrecognised tickers for manual review.

**Step 4 — Update Notion**

Opens the Freedom Finance Portfolio database (see Key Resources), clears existing rows, and re-creates one row per position with: Ticker, Company, Qty, Avg Price, Current Value, Return %, Product Type, Currency.

**Step 5 — Create snapshot page**

Creates a new child page under this SOP titled **"Freedom Finance Portfolio Snapshot — [Today's Date]"** (e.g. `Freedom Finance Portfolio Snapshot — June 3, 2026`). The page contains a full table of all synced positions. See **📄 Snapshot Page Creation** section below.

**Step 6 — Remove old snapshot pages**

After the new snapshot page is confirmed created, searches for and deletes all previously existing pages matching the pattern `Freedom Finance Portfolio Snapshot — *` that are **not** the one just created. See **🗑️ Old Snapshot Removal** section below.

---

## ✅ Required setup

- **Notion** — portfolio database updates
- **User screenshot** — Freedom24 does not have an API; all data comes from a user-supplied image
- No other MCP connections required

---

## 📄 Snapshot Page Creation

This subsection governs how Claude creates the current-state portfolio page during a sync.

- **Title format:** `Freedom Finance Portfolio Snapshot — [Full date, e.g. June 3, 2026]`
- **Parent:** This SOP page (`📋 Freedom Finance Portfolio Sync — SOP`)
- **Timing:** Created during Step 5, after the Notion database has been updated in Step 4
- **Content:** A full table of all synced positions with columns — Ticker, Company, Qty, Avg Price, Current Value, Return %, Product Type, Currency. Include portfolio-level summary (Total Value, Period Return) at the top if available from screenshot.
- **Icon:** 📸
- One snapshot page per sync — never accumulate more than one current page

---

## 🗑️ Old Snapshot Removal

This subsection governs how Claude removes stale portfolio snapshot pages during a sync.

- **Scope:** Only pages titled `Freedom Finance Portfolio Snapshot — *` that are children of this SOP page
- **Trigger:** Runs immediately after Step 5 confirms the new snapshot page is created
- **Rule:** Delete **all** matching pages **except** the one just created in the current sync
- **Safety check:** Never delete the SOP page itself or any other child pages
- **If deletion fails:** Log the failure in the snapshot page body under a `⚠️ Cleanup Notes` section and continue — do not abort the sync

---

## 🗂 Known positions (last synced: May 2025)

| Ticker | Product Type | Last Return |
| --- | --- | --- |
| [MSFT.US](http://MSFT.US) | Structured — NASDAQ growth drivers | +0.47% |
| [META.US](http://META.US) | Structured — NASDAQ growth drivers | −1.72% |
| [DUOL.US](http://DUOL.US) | Structured — NASDAQ growth drivers | −30.66% |
| [AMZN.US](http://AMZN.US) | Structured — NASDAQ growth drivers | +19.10% |
| [TLT.US](http://TLT.US) | Structured — NASDAQ growth drivers | −0.53% |

---

## 🛠 Troubleshooting

**Screenshot is blurry or fields are cut off**

Ask the user to re-send a clearer screenshot before proceeding. Do not guess values.

**Ticker not recognised**

Flag as `UNKNOWN_TICKER` in the snapshot page and Notion row. Ask user to confirm the correct ticker manually.

**Notion database URL changed**

Update the URL in the Key Resources table above, then tell Claude the new URL on next sync.

**Freedom24 changes its UI layout**

Update the field extraction logic described in Step 1–2 above to match the new layout. Note the change in the snapshot page body.

[Freedom Finance Portfolio Snapshot — May 2025](%F0%9F%93%8B%20Freedom%20Finance%20Portfolio%20Sync%20%E2%80%94%20SOP/Freedom%20Finance%20Portfolio%20Snapshot%20%E2%80%94%20May%202025%20374165d9fe04816292a3d2bd69a89641.md)
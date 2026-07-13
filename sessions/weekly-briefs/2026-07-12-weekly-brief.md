# Weekly Portfolio Brief — week of 2026-07-12

**Task type:** Weekly Monday Portfolio Sync & Brief (Routine)
**Date:** 12 Jul 2026

---

## 1. Portfolio Sync Summary

Full IBKR sync (positions + cash balances + active orders) completed for account U19421206. Freedom Finance unchanged (last synced 2026-06-07 — no new screenshot provided this round). See [holdings.md](../../portfolio/holdings.md), [ibkr.md](../../portfolio/snapshots/ibkr.md), and [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md) for full detail.

**Combined portfolio total: $59,182.14** (IBKR Net Liquidation $44,058.60 + Freedom24 NAV $15,123.54), up from $58,226.21 on 2026-07-05.

### ⚠️⚠️ Primary finding — real, undocumented position changes (not just order-level exposure this time)

| Ticker | Change | Status |
|---|---|---|
| **META** | 6 → 5 shares (-1) | **Unauthorized.** No session/decision/override authorizes a sale; the 2026-07-09 rescore explicitly said HOLD, no trim. Mechanism not confirmed. |
| **DOCS** | New: -1 short PUT (Aug21'26 $17.50 strike) | **Unauthorized, and mismatched.** The only DOCS session on file recommended a stock limit buy at $20.50 — not writing options. Added to override-log. |
| **RGL** | 2,786 → 60,000 shares (order fully filled) | Pre-existing ungoverned order (flagged every sync since 2026-07-01) has now completed. Still no Phase 01/02 evaluation exists. |
| **NVDA** | 14 → 19 shares (+5) | Closely matches the 2026-07-05 rescore's CONFIRMED BUY (target 18 shares) — 1 share over, not a governance concern. |

**Also new:** an undocumented AMZN bracket (SELL 10 @ $259.25 / BUY 10 @ $210.25, placed 2026-07-10) and a new HDSN options order (SELL 1 $5 PUT, already `REPLACED`) — the original 200-share HDSN stock buy order is gone from this sync's fetch entirely and no HDSN stock position exists, consistent with a cancellation. The MA/V/PDD/NOW/META order-level flags from prior syncs persist largely unchanged — full detail in [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md).

**Cash:** IBKR cash swung from +$342.69 to **–$261.96**, traced to AUD cash moving to –$666.43 — consistent with the RGL fill. This is the second sync in three where cash went meaningfully negative from ungoverned trading activity (GBP/TRN on 2026-06-28, now AUD/RGL).

Full per-ticker detail, evidence, and links are in [ibkr.md](../../portfolio/snapshots/ibkr.md)'s urgent boxes and [override-log.md](../../portfolio/override-log.md) (RGL entry updated; DOCS and META entries added this sync).

---

## 2. Upcoming Earnings (next 7 days)

**Not available this sync.** `EODHD_API_KEY` is set, but the account is on EODHD's free tier, which does not permit the earnings-calendar endpoint (`Only EOD data allowed for free users`). No earnings-calendar data could be pulled for any holding. Worth a `/healthcheck` note if this persists — flagged here rather than guessing at dates.

Known from prior sessions (not re-verified this sync): META Q2 2026 earnings expected 29 Jul 2026 (after close).

---

## 3. Overdue `rescore-due` Issues

**None.** No open GitHub issues labeled `rescore-due` at time of this sync.

---

## 4. Quarterly / Annual Items Due

**None due this week.** Today (12 Jul 2026) falls outside the first-7-days-of-quarter window (1–7 Jul) that triggers the Quarterly Rate Environment Gate Review — that review's window for Q3 2026 has already passed (or run) earlier this month.

---

## Glossary

See [framework/glossary.md](../../framework/glossary.md) for the standing definitions file. Terms used in this brief: Composite Score, GTC (Good-Till-Cancelled order), NAV (Net Asset Valuation), Net Liquidation Value, Override, Quality Score, R/R (Risk/Reward ratio), Rescore, Valuation Score.

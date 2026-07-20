# Weekly Portfolio Brief — week of 2026-07-20

**Task type:** Weekly Monday Portfolio Sync & Brief (Routine)
**Date:** 20 Jul 2026

---

## 1. Portfolio Sync Summary

Full IBKR sync (positions + cash balances + active orders) completed for account U19421206. Freedom Finance unchanged (last synced 2026-06-07 — no new screenshot provided this round). See [holdings.md](../../portfolio/holdings.md), [ibkr.md](../../portfolio/snapshots/ibkr.md), and [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md) for full detail.

**Combined portfolio total: $59,142.82** (IBKR Net Liquidation $44,019.28 + Freedom24 NAV $15,123.54), down slightly from $59,182.14 on 2026-07-12 (–$39.32, essentially flat — price moves, no new capital in/out).

### Quiet sync — no new undocumented position changes

All 28 IBKR positions matched the 2026-07-12 sync exactly in share count; only prices moved. This is the first sync since 2026-07-01 with zero new unauthorized fills. **The open governance items from 2026-07-12 remain open and unresolved** — none of them have been addressed yet:

| Ticker | Issue | Status |
|---|---|---|
| **META** | 6 → 5 shares (-1), unauthorized sale | Still open — no session/decision/override explains the mechanism |
| **DOCS** | Unauthorized short PUT (Aug21'26 $17.50 strike) | Still open — logged in override-log.md, expires 2026-08-21 |
| **RGL** | 60,000-share position, no Phase 01/02 evaluation ever run | Still open — a sub-cent ASX gold explorer with no quality-gate screen |
| **MBGL** | Ungoverned position, no evaluation on file | Still open |

**New this sync:** the undocumented AMZN bracket (SELL 10 @ $259.25 / BUY 10 @ $210.25, flagged 2026-07-12) has **disappeared from `get_account_orders` entirely** — not filled (AMZN position unchanged at 12 shares), not `REPLACED`, just absent from the fetch. Most likely a direct TWS/Client Portal cancellation, but that isn't confirmed by anything visible to this sync. The carried MA/V/PDD/NOW/META order-level flags persist unchanged — full detail in [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md).

**Cash:** IBKR cash essentially flat, –$261.96 → –$264.11 (–$2.15). No new large swing.

**Notable price move (informational, not a Rule 9 trigger):** RGL (RiversGold, ASX) fell another ~6% in AUD terms this week (AUD $0.008 → $0.0075/share); still well under the 15% unexplained-move threshold, but worth keeping an eye on given no evaluation exists for this ticker at all.

**Ticker lookup CSV:** the live source (`interactivebrokers.com/download/fracshare_stk.csv`) returned HTTP 403 this sync — fell back to the stored copy (last committed 2026-07-14, 6 days stale). No held ticker actually needed the lookup this round (all resolved via `contract_description`), so no practical impact.

Full per-ticker detail is in [ibkr.md](../../portfolio/snapshots/ibkr.md) and [override-log.md](../../portfolio/override-log.md) (unchanged this sync — all four items above still need the user's input to close out).

---

## 2. Upcoming Earnings (next 7 days)

**Not available this sync — same underlying data-source problem flagged by Routine 1 twice this month, not re-attempted here.**

- `EODHD_API_KEY` is present in the environment, but [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md) records this specific key as a **compromised credential** (it was committed to git history on 2026-06-13 and should be rotated before any reuse) — **not used this sync**, consistent with the same call made by Routine 1's 2026-07-16 and 2026-07-18 runs (see [issue #294](https://github.com/Cloxy777/investment-framework/issues/294)).
- The documented replacement, `yfinance`'s earnings-date lookup, was confirmed broken as of 2026-07-18 (same issue #294): Yahoo's `finance.yahoo.com/calendar/earnings?symbol=X` page now ignores the `symbol` parameter entirely and returns generic, non-ticker-specific content for every symbol tested. This isn't specific to one holding — it silently breaks the documented method for the whole framework. Not re-tested this sync since the finding is only 2 days old and nothing suggests it's since recovered.

**Known from prior sessions (not re-verified this sync):** META Q2 2026 earnings expected 29 Jul 2026 (after close).

Worth flagging to the user directly if this data-source gap isn't already on their radar: earnings-calendar automation has now been non-functional for at least two consecutive weekly cycles.

---

## 3. Overdue `rescore-due` Issues

**None technically overdue, but one is due tomorrow and blocked:** [issue #294](https://github.com/Cloxy777/investment-framework/issues/294) — "RESCORE: NFLX - earnings released 2026-07-16" — opened 2026-07-16, still open. Per [operating-calendar.md](../../framework/operating-calendar.md)'s "within 3 business days of earnings release" rule, the deadline is **2026-07-21 (tomorrow)**, so this is not yet overdue as of today (20 Jul). The issue itself documents why it's stuck: EV/EBIT, FCF Yield, Net Debt/EBITDA, and 5yr Avg PE can't be reliably filled — the same Yahoo/`yfinance` breakage noted in section 2 above (Yahoo's income-statement/cash-flow modules are returning zeroed fields) means a manual TIKR/Koyfin/Macrotrends pull is needed to actually close this out.

---

## 4. Quarterly / Annual Items Due

**None due this week.** Today (20 Jul 2026) falls outside the first-7-days-of-quarter window (1–7 Jul) that triggers the Quarterly Rate Environment Gate Review for Q3 2026 — that window has already passed.

---

## Glossary

See [framework/glossary.md](../../framework/glossary.md) for the standing definitions file. Terms used in this brief: Composite Score, GTC (Good-Till-Cancelled order), NAV (Net Asset Valuation), Net Liquidation Value, Override, Quality Score, R/R (Risk/Reward ratio), Rescore, Valuation Score.

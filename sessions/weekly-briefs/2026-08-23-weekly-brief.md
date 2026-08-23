# Weekly Portfolio Brief — week of 2026-08-23

**Task type:** Weekly Monday Portfolio Sync & Brief (Routine)
**Date:** 23 Aug 2026 (Sunday — this week's scheduled firing)

---

## 0. Process notes — this run's stored prompt vs. the current framework

Two pieces of drift in this run's stored routine prompt, both already flagged in prior weeks' briefs:

1. **"Commit straight to main"** — the stored prompt again instructed a direct push to `main`. [`sync-sop.md`](../../portfolio/sync-sop.md) is unambiguous that no sync should ever push directly to `main`; the documented, current process (since [decisions/2026-06-22-automation-routine-auto-merge-pr.md](../../decisions/2026-06-22-automation-routine-auto-merge-pr.md)) is a `claude/`-prefixed branch + PR, auto-merge attempted, falling back to a direct squash-merge of that PR when there's no CI to gate on ([decisions/2026-06-22-automation-routine-auto-merge-fallback.md](../../decisions/2026-06-22-automation-routine-auto-merge-fallback.md)). This run followed the current, documented SOP instead of the stale literal instruction.
2. **EODHD earnings calendar** — the stored prompt again instructed pulling earnings from EODHD if `EODHD_API_KEY` is set (it is, in this environment). Per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), EODHD was **deliberately removed** from this framework's process on 2026-06-19 — the free plan was unreliable (repeated 403s), and the key that had been in this environment is documented as a **compromised credential that should be rotated before any reuse, never just reused**. Attempting the call this run reproduced exactly that failure mode: `HTTP 403 — "Only EOD data allowed for free users."` **No EODHD data was used.** Earnings dates below came from the current documented method instead (`yfinance`-equivalent — see §2 for the technical note on why raw `yfinance` itself needed a workaround this run).

Both of these match the same "stored routine prompt hasn't been re-pasted since `automation-schedule.md` changed" root cause flagged in the 2026-08-16, -09, and earlier briefs. Recommend re-pasting the current Routine 2 prompt from `automation-schedule.md` into the scheduled routine config, and removing `EODHD_API_KEY` from the `investment-automation` environment's variables entirely so a future run can't reach for it by accident.

---

## 1. Portfolio Sync Summary

Full IBKR sync (positions + cash balances + active orders) completed for account U19421206. Freedom Finance **not** resynced this round — no screenshot provided; that side stays at its 2026-08-22 snapshot (manual/screenshot-based, outside this routine's scope). See [holdings.md](../../portfolio/holdings.md), [ibkr.md](../../portfolio/snapshots/ibkr.md), and [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md) for full detail.

**Combined portfolio total: $61,101.28** (IBKR Net Liquidation $50,211.32 + Freedom24 implied total $10,889.96 unchanged), essentially flat vs. $61,101.89 on 2026-08-22 (-$0.61).

### A quiet sync — no share-count changes, no fills, no cancellations

All 24 IBKR positions hold identical quantities to the 2026-08-22 sync; all 7 active orders are unchanged (GOOG SELL 1, MA BUY 4, NKE SELL 20, NOW BUY 20, PDD BUY 10, TLT SELL 1 call contract, V BUY 9). IBKR cash is essentially flat (+$0.16). Only prices moved this week — largest since yesterday: RBRK -2.57%, AVGO +1.50%, NVDA +1.21%. **Nothing crosses the Rule 9 ±15% unexplained-move threshold this window.**

**Carried, still open from prior syncs (unchanged this sync):**

| Ticker | Issue | Status |
|---|---|---|
| **SPOT** | Position + matching sell order both vanished (2026-08-02) | Still open — now absent for **5 consecutive syncs** |
| **TRN** | -22.4% price drop (08-16→08-22 window), CMA "drip pricing" probe, cause not independently confirmed by this sync | Still open — price unchanged this week; already rescored 2026-08-22 (Quality Score 67.2, fails gate) — HOLD, no top-up |
| **NOW** | 2026-08-10 undocumented 3-share trim | Still open, see [override-log.md](../../portfolio/override-log.md) |
| **RGL** | 60,000-share position, no Phase 01/02 evaluation ever run | Still open |
| **MBGL** | Ungoverned position — Quality Score 51.0, fails quality gates overall | Still open |
| **AVGO** | Override log still shows "Open — under review" despite being resolved 2026-07-04 | Housekeeping only |
| **CSGP** | `REPLACED` order (1986163848, 2026-05-26) reappeared in `get_account_orders` after aging out of the 2026-08-22 fetch | New observation — still correctly excluded as non-active; no live successor order found |
| **Cash** | +$2,523.36 unexplained jump flagged 2026-08-09 | Still open and uninvestigated |

**Ticker lookup CSV:** not re-fetched this sync — every position resolved directly via `contract_description`, and the stored copy is only 7 days stale (last refreshed 2026-08-16).

---

## 2. Upcoming Earnings (next 7 days: 23–30 Aug 2026)

**Data source note:** per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), EODHD was not used (see §0). Raw `yfinance` itself failed this run with the same recurring `curl_cffi` TLS/connection-reset error seen in prior weeks (its browser-TLS-impersonation layer appears incompatible with this environment's outbound proxy) — worked around with a direct-`requests` Yahoo Finance `quoteSummary`/`calendarEvents` call (cookie + crumb handshake, no browser-TLS impersonation), the same technique used in prior weeks. Checked against all 22 current equity holdings (excluding CASH, XEON, TLT — non-equity/cash-equivalent, out of Rule 9 scope).

**Three current holdings report earnings in this window:**

| Ticker | Earnings Date | Current Weight |
|---|---|---|
| **NVDA** | 2026-08-26 | 6.78% |
| **VEEV** | 2026-08-26 | 1.22% |
| **RBRK** | 2026-08-27 | 0.48% |

NVDA is the one to watch — at 6.78% weight, an earnings-driven RESCORE trigger on this holding would be **P1** priority (≥5% weight) per `automation-schedule.md`'s priority rule once Routine 1 detects the release and opens the `rescore-due` issue. This routine (Routine 2) only surfaces the date for visibility; it does not open the issue itself.

RGL (ASX) and TRN (LSE) returned no earnings-date data from this source — a data gap, not confirmation of "no earnings due."

Nearest outside the window: AVGO (2026-09-02), ZS (2026-09-03), ADBE (2026-09-10), NKE (2026-09-29).

---

## 3. Overdue `rescore-due` Issues

**None.** No open GitHub issues are currently labeled `rescore-due`.

---

## 4. Quarterly / Annual Items Due

**None due this week.** Today (23 Aug 2026) falls outside the first-7-days-of-quarter window that triggers the Quarterly Rate Environment Gate Review (Q3's window, 1–7 Jul, already passed; Q4's, 1–7 Oct, hasn't started).

---

## Glossary

See [framework/glossary.md](../../framework/glossary.md) for the standing definitions file. Terms used in this brief: Composite Score, GTC (Good-Till-Cancelled order), NLV (Net Liquidation Value), Override, Phase 01/02 (the framework's quantitative quality-gate and valuation-scoring passes), Quality Score, RESCORE, Rule 0 (never invent or estimate a missing metric — fetch live data or stop and ask), Rule 9 (mandatory immediate re-score trigger on an unexplained >15% move or an earnings release), Valuation Score.

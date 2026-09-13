# Weekly Portfolio Brief — week of 2026-09-13

**Task type:** Weekly Monday Portfolio Sync & Brief (Routine)
**Date:** 13 Sep 2026 (Sunday — this week's scheduled firing)

---

## 0. Process notes — this run's stored prompt vs. the current framework

Same two pieces of drift flagged in every weekly brief since 2026-08-09 — still recommend re-pasting the current Routine 2 prompt from `automation-schedule.md` into the scheduled routine config:

1. **"Commit straight to main"** — the stored prompt again instructed a direct push to `main`. [`sync-sop.md`](../../portfolio/sync-sop.md) is unambiguous that no sync should ever push directly to `main`; the documented, current process is a `claude/`-prefixed branch + PR, auto-merge attempted, falling back to a direct squash-merge when there's no CI to gate on. This run followed the current, documented SOP instead of the stale literal instruction.
2. **EODHD earnings calendar** — the stored prompt again instructed pulling earnings from EODHD if `EODHD_API_KEY` is set (it is, in this environment). Per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), EODHD was **deliberately removed** from this framework's process on 2026-06-19, and that decision record documents the key checked into this repo's history as a **compromised credential — rotate before any reuse, never just reuse it.** This run did **not** call the EODHD API. Earnings dates below came from `yfinance` instead (the current documented method).

Recommend removing `EODHD_API_KEY` from the `investment-automation` environment's variables entirely so a future run can't reach for it by accident.

---

## 1. Portfolio Sync Summary

Full IBKR sync (positions + cash balances + active orders) completed for account U19421206. Freedom Finance **not** resynced this round — no screenshot provided; that side stays at its 2026-08-22 snapshot (manual/screenshot-based, outside this routine's scope). See [holdings.md](../../portfolio/holdings.md), [ibkr.md](../../portfolio/snapshots/ibkr.md), and [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md) for full detail.

**Combined portfolio total: $61,192.89** (IBKR Net Liquidation $50,302.93 + Freedom24 implied total $10,889.96 unchanged), down from $62,135.17 on 2026-09-06 (-$942.28, -1.5%) — driven by a broad price pullback, not new capital or fills.

### 🚨 Most important item this week: a new, large, undocumented TRN order directly contradicts the framework's own rescore from the day before

**TRN BUY 900 @ £1.756 LIMIT GTC** (order 1528612089, placed **2026-09-11**, one day *after* TRN's own [2026-09-10 rescore](../../sessions/2026-09-10-rescore-trn.md) explicitly recommended **HOLD, no top-up** — Quality Score 66.4, fails the 80.0+ gate, plus a still-open CMA "drip pricing" investigation as an independent second reason not to add). If filled, this would grow the TRN position from 600 → 1,500 shares — **a +150% increase** on a name the framework says not to add to. No `sessions/`/`decisions/` entry documents it. GBP cash on the account is currently $0.00, so filling it would require an FX conversion or margin draw. The order isn't immediately marketable (limit £1.756 vs. live £1.934, ~9.2% below market) but it is real, live, and GTC. **Recommend the user cancel this order or log the reasoning that overrides both no-buy signals, per Rule 10 — this is the one item in this brief that shouldn't wait for the next sync.**

A second, smaller order appeared the same morning: **ADBE BUY 10 @ $240.00** (order 1071856795, placed 2026-09-11, one minute *before* the TRN order), already shown `REPLACED` by this sync with no live successor found. ADBE's position/avg cost are unchanged, confirming no fill. Its direction is not inconsistent with ADBE's own same-day [2026-09-11 rescore](../../sessions/2026-09-11-rescore-adbe.md) (BUY, 6-share top-up recommended, ceiling $333.13) but the quantity and "replaced with nothing live" disposition don't clearly match it — worth a manual TWS check for what it was replaced with, if anything.

### No share-count changes; broad pullback across the book

All 24 IBKR positions hold identical quantities to the 2026-09-06 sync. 9 of 24 names moved more than 5% this week — largest: **RGL +9.09%, NVO -7.78%, SPGI -7.56%, RBRK -7.49%, DUOL -7.08%, NOW -6.78%, NVDA -6.31%, UBER -5.79%, ADBE -5.16%**. **Nothing crosses the Rule 9 ±15% unexplained-move threshold.**

**Carried, still open from prior syncs (unchanged this sync):**

| Ticker | Issue | Status |
|---|---|---|
| **TSM** | BUY 10 @ $369.00 GTC, contradicts the 2026-09-06 new-position "WATCHLIST ONLY" call | Still open, unresolved |
| **NVDA** | BUY 10 @ $199.56 GTC, predates and contradicts both September rescores | Still open, unresolved |
| **BKNG** | BUY 10 @ $159.00 GTC (placed 2026-08-24), no `sessions/`/`decisions/` entry | Still open, unresolved |
| **MA / PDD** | Active BUY orders that don't match their own sessions' recommended size/price/R-R gate | Still open, see [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md) |
| **NOW** | Undocumented BUY 20 @ $80.00 order, alongside the 2026-08-10 undocumented 3-share trim | Still open, see [override-log.md](../../portfolio/override-log.md) |
| **TLT** | Short call order (1040104046) absent from the orders fetch, in any status | Still open — now **2 consecutive syncs** missing |
| **SPOT** | Position + matching sell order both vanished (2026-08-02) | Still open — now absent for **8 consecutive syncs** |
| **TRN** | Multi-week price decline, CMA "drip pricing" probe, cause not independently confirmed | Small rebound this week (+0.78%); already rescored 2026-09-10 — HOLD, no top-up (see the order flag above) |
| **RGL** | 60,000-share position, no Phase 01/02 evaluation ever run | Still open |
| **MBGL** | Ungoverned position — Quality Score 51.0, fails quality gates overall | Still open |
| **AVGO** | Override log still shows "Open — under review" despite being resolved 2026-07-04 | Housekeeping only |
| **Cash** | +$2,523.36 unexplained jump flagged 2026-08-09 | Still open and uninvestigated |

**Ticker lookup CSV:** not re-fetched this sync — every position resolved directly via `contract_description`; stored copy is now 13 days stale (last refreshed 2026-08-31).

---

## 2. Upcoming Earnings (next 7 days: 13 Sep – 20 Sep 2026)

**Data source note:** per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), EODHD was not used (see §0). Checked via `yfinance` (with the `requests.Session()` TLS-passthrough workaround used in recent rescore sessions) against all 22 current equity holdings (excluding `CASH`, `XEON`, `TLT` — non-equity/cash-equivalent, out of Rule 9 scope).

**No current holding reports earnings in this window.** The nearest upcoming dates are all well outside the 7-day window: NKE (2026-10-01), V/CSGP (2026-10-27), GOOG/META/MSFT/NOW/AMZN/SPGI (2026-10-28–29), NFLX (2026-10-20).

RGL (ASX) returned no earnings-date data from this source (a data gap, not confirmation of "no earnings due"). RBRK's returned date (2026-08-27) is stale/in the past — the source hasn't rolled to its next date yet.

---

## 3. Overdue `rescore-due` Issues

**None remain open.** Two `rescore-due` issues existed at the start of this check:

- **[#709, ZS](https://github.com/Cloxy777/investment-framework/issues/709)** — earnings-triggered 2026-09-03, due 2026-09-08. **Was overdue** (5 days past due) — but the rescore had actually already been completed on **2026-09-07**, ahead of the due date ([session](../../sessions/2026-09-07-rescore-zs.md)); the issue simply hadn't been closed. Closed this run with a note.
- **[#770, ADBE](https://github.com/Cloxy777/investment-framework/issues/770)** — earnings-triggered 2026-09-10, due 2026-09-15. Not yet overdue, but likewise already completed on **2026-09-11** ([session](../../sessions/2026-09-11-rescore-adbe.md)). Closed this run with a note.

Both closures are pure housekeeping (the underlying work was already done); flagged here so the pattern of rescore sessions not closing their own tracking issue is visible — worth checking whether `/rescore` should close its own `rescore-due` issue automatically as part of Rule 10.

---

## 4. Quarterly / Annual Items Due

**None due this week.** Today (13 Sep 2026) falls outside the first-7-days-of-quarter window that triggers the Quarterly Rate Environment Gate Review (Q3's window, 1–7 Jul, already passed; Q4's, 1–7 Oct, hasn't started).

---

## Glossary

See [framework/glossary.md](../../framework/glossary.md) for the standing definitions file. Terms used in this brief: Composite Score, GTC (Good-Till-Cancelled order), MoS (Margin of Safety), NLV (Net Liquidation Value), Override, Phase 01/02 (the framework's quantitative quality-gate and valuation-scoring passes), Quality Score, R/R (Risk/Reward ratio), RESCORE, Rule 0 (never invent or estimate a missing metric — fetch live data or stop and ask), Rule 9 (mandatory immediate re-score trigger on an unexplained >15% move or an earnings release), Rule 10 (every session saved to `sessions/`, every actual trade logged in `decisions/`), Valuation Score.

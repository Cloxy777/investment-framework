# Weekly Portfolio Brief — week of 2026-09-20

## 0. Process notes — this run's stored prompt vs. the current framework

Same two pieces of drift flagged in every weekly brief since 2026-08-09 — still recommend re-pasting the current Routine 2 prompt from `automation-schedule.md` into the scheduled routine config:

1. **"Commit straight to main"** — the stored prompt again instructed a direct push to `main`. [`sync-sop.md`](../../portfolio/sync-sop.md) is unambiguous that no sync should ever push directly to `main`; the documented, current process is a `claude/`-prefixed branch + PR, auto-merge attempted, falling back to a direct squash-merge when there's no CI to gate on (see [decisions/2026-06-22-automation-routine-auto-merge-fallback.md](../../decisions/2026-06-22-automation-routine-auto-merge-fallback.md)). This run followed the current, documented SOP instead of the stale literal instruction.
2. **EODHD earnings calendar** — the stored prompt again instructed pulling earnings from EODHD if `EODHD_API_KEY` is set (it is, in this environment). Per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), EODHD was **deliberately removed** from this framework's process on 2026-06-19, and that decision record documents the key checked into this repo's history as a **compromised credential — rotate before any reuse, never just reuse it.** This run did **not** call the EODHD API. Earnings dates below came from `yfinance` instead (the current documented method).

Recommend removing `EODHD_API_KEY` from the `investment-automation` environment's variables entirely so a future run can't reach for it by accident — this has now been flagged in six consecutive weekly briefs plus [#582](https://github.com/Cloxy777/investment-framework/issues/582) (open since 2026-08-19).

---

## 1. Portfolio Sync Summary

Full IBKR sync (positions + cash balances + active orders) completed for account U19421206. Freedom Finance **not** resynced this round — no screenshot provided; that side stays at its 2026-08-22 snapshot (manual/screenshot-based, outside this routine's scope). See [holdings.md](../../portfolio/holdings.md), [ibkr.md](../../portfolio/snapshots/ibkr.md), and [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md) for full detail.

**Combined portfolio total: $61,220.66** (IBKR Net Liquidation $50,330.70 + Freedom24 implied total $10,889.96 unchanged), up modestly from $61,192.89 on 2026-09-13 (+$27.77, +0.05%) — a broad rebound this week largely offset the prior week's pullback.

### 🚨 Most important item this week: a new, undocumented AVGO order directly contradicts the framework's own rescore from four days earlier

**AVGO BUY 5 @ $310.60 LIMIT GTC** (order 87937891, placed **2026-09-19**). AVGO's own most recent rescore, [2026-09-15](../../sessions/2026-09-15-rescore-avgo.md), ran a full order-setup pass and explicitly concluded **"No order is placed"** — the computed Risk/Reward ratio failed the framework's 2:1 minimum across the entire applicable Margin-of-Safety/stop range, so Net Action was **HOLD**, no add. That session's own computed buy range was **$248.67–$266.43**; this order's limit price sits **~16.6% above the top of that range** and above AVGO's live price ($356.96) — not immediately marketable, but real, live, and GTC. No `sessions/`/`decisions/` entry documents it. **Recommend the user cancel this order or log the reasoning that overrides the session's own explicit "no order" conclusion, per Rule 10.**

The previously-flagged **TRN BUY 900 @ £1.756 LIMIT GTC** (order 1528612089, placed 2026-09-11, contradicting the [2026-09-10 rescore](../../sessions/2026-09-10-rescore-trn.md)'s HOLD/no-top-up call) remains live and unresolved — still worth cancelling or documenting.

### 🚨 Second most important item: RBRK and ZS both crossed the Rule 9 threshold last week — their re-scores are now 3 days overdue

See §3 below for full detail — issues [#801](https://github.com/Cloxy777/investment-framework/issues/801) and [#802](https://github.com/Cloxy777/investment-framework/issues/802) were opened 2026-09-14 and are still open, past their 2026-09-17 due date. Both names have moved further since (RBRK $100.20 → $107.00; ZS $191.73 → $198.15).

### No share-count changes; broad rebound across the book

All 24 IBKR positions hold identical quantities to the 2026-09-13 sync. Only 4 of 24 names moved more than 5% this week — **RBRK +23.49%, ZS +20.24%, RGL -8.33%, NFLX -6.57%** (RBRK/ZS already covered by the open Rule 9 issues above; the underlying move happened mid-week on 2026-09-14, not new information this sync).

**Carried, still open from prior syncs (unchanged this sync):**

| Ticker | Issue | Status |
|---|---|---|
| **TSM** | BUY 10 @ $369.00 GTC, contradicts the 2026-09-06 new-position "WATCHLIST ONLY" call | Still open, unresolved |
| **NVDA** | BUY 10 @ $199.56 GTC, predates and contradicts both September rescores | Still open, unresolved |
| **BKNG** | BUY 10 @ $159.00 GTC (placed 2026-08-24), no `sessions/`/`decisions/` entry | Still open, unresolved |
| **MA / PDD** | Active BUY orders that don't match their own sessions' recommended size/price/R-R gate | Still open, see [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md) |
| **NOW** | Undocumented BUY 20 @ $80.00 order, alongside the 2026-08-10 undocumented 3-share trim | Still open, see [override-log.md](../../portfolio/override-log.md) |
| **TLT** | Short call order (1040104046) absent from the orders fetch, in any status | Still open — now **3 consecutive syncs** missing |
| **SPOT** | Position + matching sell order both vanished (2026-08-02) | Still open — now absent for **9 consecutive syncs** |
| **TRN** | Undocumented 900-share buy order, contradicts 2026-09-10 rescore | Still open, unresolved (see above) |
| **RGL** | 60,000-share position, no Phase 01/02 evaluation ever run | Still open |
| **MBGL** | Ungoverned position — Quality Score 51.0, fails quality gates overall | Still open |
| **AVGO** | Override log still shows "Open — under review" despite being resolved 2026-07-04 | Housekeeping only |
| **Cash** | +$2,523.36 unexplained jump flagged 2026-08-09 | Still open and uninvestigated |

**Ticker lookup CSV:** not re-fetched this sync — every position resolved directly via `contract_description`; stored copy is now 20 days stale (last refreshed 2026-08-31).

---

## 2. Upcoming Earnings (next 7 days: 20 Sep – 27 Sep 2026)

**Data source note:** per [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md), EODHD was not used (see §0). Checked via `yfinance` against all 22 current equity holdings (excluding `CASH`, `XEON`, `TLT` — non-equity/cash-equivalent, out of Rule 9 scope).

**No current holding reports earnings in this window.** The nearest upcoming dates: NKE (2026-10-01), V/CSGP (2026-10-27), GOOG/META/MSFT/NOW/AMZN/SPGI (2026-10-28–29), NFLX (2026-10-20), UBER (2026-11-03), DUOL/NVO/TRN/MBGL (2026-11-04–05), NVDA (2026-11-17), VEEV (2026-11-25), AVGO/RBRK (2026-12-03/09), ZS (2026-11-24).

RGL (ASX) returned no earnings-date data from this source (a data gap, not confirmation of "no earnings due").

---

## 3. Overdue `rescore-due` Issues

**Two issues are open and both are overdue:**

- **[#801, RBRK](https://github.com/Cloxy777/investment-framework/issues/801)** — Rule 9 trigger, +15.4% move on 2026-09-14 with no known catalyst, due 2026-09-17. **3 days overdue.** RBRK has moved further since (now $107.00 vs. the $100.20 that triggered the issue); not scored (fails quality gates), last reviewed 30 Aug 2026.
- **[#802, ZS](https://github.com/Cloxy777/investment-framework/issues/802)** — Rule 9 trigger, +16.3% move on 2026-09-14 with no known catalyst, due 2026-09-17. **3 days overdue.** ZS has moved further since (now $198.15 vs. the $191.73 that triggered the issue); Valuation 47.9 / Quality 59.4 / Composite 44.3, last reviewed 07 Sep 2026.

Both issues note that neither move was explained by an earnings release (checked via `yfinance`) — a human/analyst still needs to look for a news/M&A/analyst-action catalyst at `/rescore` time. Recommend running `/rescore RBRK ZS` promptly given the overdue status.

---

## 4. Quarterly / Annual Items Due

**None due this week.** Today (20 Sep 2026) falls outside the first-7-days-of-quarter window that triggers the Quarterly Rate Environment Gate Review (Q3's window, 1–7 Jul, already passed; Q4's, 1–7 Oct, hasn't started yet — due next week's brief to flag as approaching).

---

## Glossary

See [framework/glossary.md](../../framework/glossary.md) for the standing definitions file. Terms used in this brief: Composite Score, GTC (Good-Till-Cancelled order), MoS (Margin of Safety), NLV (Net Liquidation Value), Override, Phase 01/02 (the framework's quantitative quality-gate and valuation-scoring passes), Quality Score, R/R (Risk/Reward ratio), RESCORE, Rule 0 (never invent or estimate a missing metric — fetch live data or stop and ask), Rule 9 (mandatory immediate re-score trigger on an unexplained >15% move or an earnings release), Rule 10 (every session saved to `sessions/`, every actual trade logged in `decisions/`), Valuation Score.

# Human Override Log

## Purpose

Every position entered outside the framework's rules is a human override. Overrides are a primary source of underperformance in systematic strategies — not because intuition is always wrong, but because overrides are untracked, unreviewed, and therefore never corrected.

This log tracks every override, its outcome, and the cumulative cost. **Reviewed annually in Q1.**

> **Rule:** If a position was opened when the valuation score was 50.0+ (Watchlist or Expensive), or if any Phase 01 quality criterion was waived, it is an override. Log it here at time of entry — and record the reasoning in `decisions/` too.

## What Counts as an Override

| Type | Description |
| --- | --- |
| Valuation override | Bought at Score 50.0–100.0 (outside the entry zone) |
| Quality waiver | Entered despite failing 1+ Phase 01 criteria |
| Size override | Position sized above the score-band maximum |
| Exit delay | Held a Score 70.0–100.0 position beyond the trim protocol timeline |
| Re-entry override | Re-bought a previously exited position without re-running Phase 01–02 |
| Thesis extension | Continued holding after a Phase 06 exit signal was triggered |

## Override Log

| Date | Ticker | Override Type | Rule Broken | Rationale Given | Score at Entry | Outcome (fill at exit or annually) | Lesson |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-06-16 | AVGO | Valuation override | Bought at Score 50.0–100.0 (outside the entry zone) | **Not on record.** The only AVGO evaluation in this repo — the [2026-06-14 new-position session](../sessions/2026-06-14-new-position-avgo.md) — scored it 69.5 (WATCHLIST, explicit "no new entry"). 6 shares were bought 2 days later @ $382.275 (essentially the same price evaluated, $382.07) with no `decisions/` entry. Logged retroactively by the [2026-06-22 weekly sync](../sessions/weekly-briefs/2026-06-22-weekly-brief.md) — flagged for the user to supply the missing rationale. | 69.5 | Open — under review | TBD; revisit once rationale is supplied and at the 2027 Q1 annual review |
| 2026-06-30 (discovered 2026-07-01; order fully filled by 2026-07-12) | RGL (RiversGold Ltd, ASX) | Quality waiver — no Phase 01/02 evaluation exists at all | Bought with no quality-gate screen, no valuation score, no `sessions/` entry | **Not on record.** No `/new-position` session, no `override-log` entry, and no `watchlist/` file exist for this ticker anywhere in this repo. Discovered live via `get_account_positions`/`get_account_orders` during the [2026-07-01 rebalance session](../sessions/2026-07-01-rebalance.md) §0: 2,786 shares filled (of a 60,000-share GTC limit order @ AUD $0.009, `order_id 630395618`) between 2026-06-30 23:59 UTC and 2026-07-01 05:25 UTC. RiversGold is an ASX-listed micro-cap gold exploration company — a sub-cent, pre-revenue explorer is close to a worst-case fit against this framework's Phase 01 criteria (net margin >15%, ROIC >15%, positive FCF 3+ years), consistent with no evaluation ever having been run. **The order has since fully filled** (confirmed via the 2026-07-12 `/sync-portfolio` sync — position now 60,000 shares, order no longer appears in `get_account_orders`) — logged retroactively per the same pattern as AVGO above, flagged for the user to confirm whether this was intentional and to formally close out (or evaluate) the position now that it's complete. | n/a — no Phase 02 score computed | **Open — order fully filled 60,000/60,000 shares, still no Phase 01/02 evaluation, review recommended** | TBD; revisit once rationale is supplied or a Phase 01/02 evaluation is run |
| 2026-07-10 (discovered 2026-07-12) | DOCS (Doximity, Inc.) | Quality waiver / instrument mismatch — a short-put options position with no evaluation of that specific instrument | Sold 1 `DOCS Aug21'26 $17.50 PUT` contract (premium received ~$74.96) with no `sessions/`, `decisions/`, or `override-log` entry authorizing an options trade | **Not on record.** The only DOCS analysis in this repo, the [2026-07-07 new-position session](../sessions/2026-07-07-new-position-docs.md), scored DOCS 84.4 Quality / 20.7 Composite (BUY band) but recommended a **stock limit BUY order at $20.50** specifically because the R/R gate failed at the live price ($22.87) — it says nothing about writing options. A short put has a materially different risk profile (assignment risk if DOCS falls below $17.50 by expiry, capped upside to the premium, no participation in a rally) that was never evaluated under this framework. Discovered live via `get_account_positions` during the 2026-07-12 `/sync-portfolio` sync. | n/a — Quality Score 84.4 exists for the *stock*, but no evaluation of a short-put strategy exists | **Open — position live, expires 2026-08-21, review recommended** | TBD; revisit once rationale is supplied or at expiry |
| 2026-07-08–07-11 (discovered 2026-07-12) | META (Meta Platforms, Inc.) | Exit delay / undocumented trim — 1 share sold with no exit trigger on record | Sold 1 of 6 META shares with no `sessions/`, `decisions/`, or `override-log` entry authorizing a sale | **Not on record.** The most recent META rescore ([2026-07-09](../sessions/2026-07-09-rescore-meta.md)) explicitly recommends **HOLD — no forced trim** (Composite Score 24.5, comfortably inside the 6–8% band, 0.96pp of headroom to the cap). No Phase 06 exit signal, no Rule 9 trigger, and no order in `get_account_orders` shows this fill — mechanism not confirmed (would need `get_account_trades`, out of `/sync-portfolio`'s scope). Discovered via the 2026-07-12 sync's position-count comparison against the 2026-07-05 snapshot (6 → 5 shares). | Composite 24.5 (BUY band — no exit/trim signal) | **Open — mechanism unconfirmed, review recommended** | TBD; revisit once rationale or trade confirmation is supplied |

## Historical Override Audit — Existing Portfolio

Starting-point audit based on the May 2026 portfolio snapshot — verify with actual entry prices/scores and update.

| Ticker | Override Type | Estimated Score at Entry | Current Status | Action |
| --- | --- | --- | --- | --- |
| DUOL | Quality waiver (FCF negative at entry) | Score 77.7–88.8 est. | Under review | Run Phase 06 analysis |
| STIM | Quality waiver (micro-cap, no FCF) | N/A | Monitoring | Exit at next review unless thesis documented |
| RLYB | Quality waiver (pre-profit biotech) | N/A | Monitoring | Exit at next review unless thesis documented |
| FSLY | Quality waiver (FCF borderline) | Score 66.6–77.7 est. | Monitoring | Run Phase 01 re-screen |
| SOFI | Quality waiver (fintech, borderline) | Score 66.6+ est. | Monitoring | Run Phase 01 re-screen |
| TLT | Asset class override (not an equity) | N/A | No exit criteria defined | Define exit rules or divest |

## Annual Override Review

Each Q1, answer for the prior year's overrides:

1. **Win rate of overrides vs framework positions** — did overrides outperform or underperform the rule-following positions?
2. **Most common override type** — which rule is broken most often? Is the rule wrong, or is discipline failing?
3. **Cumulative override cost** — total P&L from override positions vs. what the framework-compliant alternative (smaller or no position) would have generated?

If overrides consistently underperform: tighten the process — remove the mental permission to override.
If a specific override type consistently *outperforms*: consider whether it reflects a genuine framework gap that should be formalised as a new rule (the way the Turnaround Sub-Gate was added).

## The Core Discipline

The override log is not a shame register — it's a calibration tool. Every investor overrides their system occasionally. The difference between a durable process and a gradually degrading one is whether overrides are tracked and reviewed, or quietly forgotten.

A position that follows the framework and loses money is a good process with a bad outcome. A position that breaks the framework and makes money is a bad process with a good outcome. Only the log tells you which is which over time.

*Added: May 2026 · Review and update annually in Q1*

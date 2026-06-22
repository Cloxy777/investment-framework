# Watchlist

A quick-glance index of every ticker this framework has evaluated via `/new-position` or `/rescore` — separate from the full, detailed audit trail in [`sessions/`](../sessions/), which remains the canonical record of *how* each number was derived. Think of this as the "current state" pointer; `sessions/` is the append-only history.

## Structure

```
watchlist/
  in-portfolio/<TICKER>/<TICKER>-YYYY-MM-DD.md      — currently held (per holdings.md)
  not-in-portfolio/<TICKER>/<TICKER>-YYYY-MM-DD.md  — evaluated, not (or no longer) held
```

One file per ticker, most of the time. The date in the filename is the date of the **last significant update** (see below) — not every screening produces a new file.

## What goes in an entry

Short and scannable:
- Ticker, company name, sector
- Status (held + weight, or not held)
- A one-row table per *significant* update: date, live price at the time, valuation score (or "Phase 01 FAIL" / "not scored"), action per the **current** [Action Table](../framework/strategy.md#action-table-summary), a one-line key-metrics/why summary, and a link to the full session in `sessions/`
- A "Last checked (no change)" line for routine re-checks that didn't warrant a new row
- Next review trigger

**Entries reflect the current framework Action Table given the recorded score** — if a strategy.md rule changes after an entry was written (e.g. the 2026-06-07 removal of the Score 6–7 trim trigger), read the *Action* column against **current** `strategy.md`, not necessarily the literal text of the linked session (which is a frozen historical record of the as-computed reasoning at the time).

## "Significant change" — when does a new dated entry get created?

A new file (new date in the filename — git history preserves the prior version) is created only when:
- The valuation score changes, or moves between "scored" and "Phase 01 FAIL / not scored", **or**
- The action recommendation category changes (e.g. WATCHLIST → BUY, HOLD → TRIM, PASS → WATCHLIST), **or**
- A Rule 9 fundamental-event trigger fires (earnings, guidance revision, M&A, management change, macro shift, >15% unexplained move) — even if the score/action ends up unchanged, the *reasoning* has changed and is worth a fresh pointer, **or**
- The position is opened or closed (this also triggers the in-portfolio ⇄ not-in-portfolio move below).

Otherwise — re-screened, nothing material changed — just append a line to the existing file's "Last checked (no change)" log. **No new file.**

## in-portfolio ⇄ not-in-portfolio

Maintained by `/sync-portfolio`: for each ticker now in [holdings.md](../portfolio/holdings.md) that has a `not-in-portfolio/<TICKER>/` folder, `git mv` it to `in-portfolio/`. For each ticker in `in-portfolio/` no longer in holdings.md (position exited), `git mv` it to `not-in-portfolio/` and add a one-line "exited" note to its entry.

## Stale scores — when the scoring methodology changes

A general, repeatable mechanism (not tied to any one change): when the **scoring methodology version** changes, scores computed under an older version are no longer comparable to new ones, so they are flagged stale until rescored.

- **Methodology version:** stamped at the top of [valuation-scoring.md](../framework/valuation-scoring.md) (a date). Bump it whenever a change materially alters how the score is computed (a new/changed sub-score, modifier, weight, or eligibility rule), and record why in `decisions/`.
- **Mark (on a version bump):** every watchlist entry that carries a *numeric* score computed under an older version gets (1) a one-line `⚠️ STALE SCORE` banner at the top of its file, and (2) a row in the central registry [STALE.md](STALE.md). Entries that are "Phase 01 FAIL / not scored" are **not** marked — there is no Phase 02 score for the change to invalidate.
- **Clear (on rescore):** when `/rescore` (held) or `/new-position` (not held) writes a fresh entry under the current methodology, it **removes that ticker's banner and deletes its row in STALE.md** as part of the same update. So the registry is self-emptying as the book is brought current.

This keeps the per-ticker `<TICKER>/<TICKER>-YYYY-MM-DD.md` paths intact (no folder renames), so links from `holdings.md`, `sessions/`, and the commands never break.

## Maintained by

- **`/new-position`** — creates/updates the `not-in-portfolio/<TICKER>/` entry (or `in-portfolio/` if the ticker turns out to already be held).
- **`/rescore`** — creates/updates the `in-portfolio/<TICKER>/` entry.
- **`/sync-portfolio`** — reconciles the in-portfolio/not-in-portfolio split (see above).
- **`/screen`** is **not** mirrored here — the Qualified Quality List (50–150 names) stays in `sessions/` + [screening-coverage-log.md](../framework/screening-coverage-log.md), to keep this index limited to names that have actually had a `/new-position` or `/rescore` pass.

## Backfilled 2026-06-11

`in-portfolio/` was seeded from the 2026-06-07 portfolio-wide rescore baseline ([sessions/2026-06-07-rescore-full-portfolio.md](../sessions/2026-06-07-rescore-full-portfolio.md)) and the same-day NVDA rescore ([sessions/2026-06-07-rescore-nvda.md](../sessions/2026-06-07-rescore-nvda.md)). `not-in-portfolio/` was seeded with CIEN, the first `/new-position` run after this convention was introduced.

Several Score 6–7 names in the backfill (MSFT, NFLX, NOW, NVDA, UBER, V, ZS) were computed in sessions written the same day as — and reading against the *prior* version of — the Score 6–7 trim-trigger rule. Their **Action** field below has been updated to reflect the **current** Action Table (Score 6–7 = HOLD/watch, no trim); the linked sessions still show "TRIM 25–30%" as their as-computed output under the old rule. This is noted individually where it applies.

**Score 8 names (AMZN, CSGP, GOOG, SPOT)** — the same 2026-06-07 session computed these as "TRIM to 50%," but strategy.md's current Action Table maps **Score 8 → Trim 25–30%** and reserves "Trim to 50%" for Score 9. Following the same "current Action Table given the recorded score" principle as the Score 6–7 case above, these four entries show **Trim 25–30%**.

**Position cap (Upgrade 7) raised 8% → 15%** the same day as the full-portfolio rescore (see [decisions/2026-06-07-framework-change-position-cap.md](../decisions/2026-06-07-framework-change-position-cap.md)) — *after* that session's text was written. Several of its cap-related flags were computed against the old 8% cap: AMZN's "structural 8% cap breach" and DUOL's "already near the 8% cap" no longer hold under the current 15% cap (both now have meaningful headroom); MSFT's breach (16.84%) persists but is now ~1.84pp over rather than >2x over. Re-read against the current cap individually in each entry.

**Possible Rate Environment Gate inconsistency (flagged during this 2026-06-11 backfill, not corrected):** the 2026-06-07 full-portfolio rescore applied only the Step 2 Rate Regime Modifier (+0.5) uniformly across all 19 names. But strategy.md, updated that same day, also makes Step 1 (Earnings Yield Spread Test) failure a **separate** +0.5 additive — and the same-day MA new-position session correctly applied *both* (+1.0 combined). 18 of the 19 portfolio names failed Step 1 (only NVO passed), so those 18 scores may be understated by ~0.5 relative to the current rule. Re-deriving 18 scores is out of scope for this backfill — flagged here as an open item for the next `/rescore` pass.

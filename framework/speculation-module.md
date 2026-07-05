# Speculation Module (Satellite Sleeve)

> **Status: v1 draft, proposed 2026-07-01.** Numeric parameters (bucket cap, per-trade cap, time-stop default) are proposed defaults from the 2026-07-01 design discussion — adjust directly in this file and confirm before treating them as binding. Rationale for the module's existence and its deliberate divergence from the core framework's philosophy tests is recorded in [decisions/2026-07-01-framework-change-speculation-module.md](../decisions/2026-07-01-framework-change-speculation-module.md).
>
> **Operationalized 2026-07-04** via [speculation-strategies.md](speculation-strategies.md) (the evidence-graded strategy/technique menu this module's rules feed into) and the [`/speculate`](../.claude/commands/speculate.md) command (live data + news → regime read → strategy pick → levels → gated IBKR order recommendation). See [decisions/2026-07-04-framework-change-speculation-strategies-and-speculate-command.md](../decisions/2026-07-04-framework-change-speculation-strategies-and-speculate-command.md).

## Relationship to the core framework

Phases 01–06 ([strategy.md](strategy.md)) govern multi-year holds and are, by design, fundamentals-only: no chart pattern, no price level, no momentum ever triggers a core decision. This module governs a small, separate satellite sleeve for short-horizon (days/weeks/months) speculative trades — modeled on Benjamin Graham's "mad money account" (*The Intelligent Investor*: a small, strictly separate speculative sub-account, never mingled with the core, capped at roughly 10% of total wealth) and standard institutional core-satellite portfolio construction.

The core discipline this module exists to protect: **the impulse to trade on a price move or a hot rumor must have a sanctioned, bounded outlet — otherwise it leaks into the core book undocumented**, exactly the pattern already visible in [override-log.md](../portfolio/override-log.md) (AVGO, DUOL, STIM). This sleeve gives that impulse somewhere small and walled to go instead.

## Rule 1 — Eligibility gate

Only tickers carrying a **current, non-stale Quality Score ≥ 80.0** (per [quality-scoring.md](quality-scoring.md)) may be traded in this sleeve. Check the ticker's entry under `watchlist/` for the current score and its date before entering.

The **Valuation Score / action band is irrelevant to entry** — you may speculate on a name even while its core score says "trim" or "expensive." This is the gate's entire purpose: it bounds this sleeve's worst-case name-specific risk to "good business, badly timed trade," never "junk stock, badly timed trade."

If a candidate ticker has no current Quality Score on file (shown as `?` in `holdings.md` or not yet run through `/screen`/`/new-position`), it is **not eligible** until `/rescore` produces one — no exceptions, no estimating it.

## Rule 2 — Bucket cap

**5% of total portfolio value** (combined broker NLV), hard ceiling. Never exceed **10%** (Graham's own limit) without a deliberate, logged decision at the Q1 annual review — not an in-the-moment call. Checked at every `/sync-portfolio`; trim the sleeve back to cap if winners push it over (reuse the existing Dynamic Trimming discipline from Phase 05, applied here as a hard % rule rather than a score-based trigger).

## Rule 3 — Per-trade cap

Max **20% of the sleeve** per position (≈1% of total portfolio at the 5% default) — keeps 5+ concurrent names for diversification within the sleeve. Size off **maximum loss**, not notional exposure:
- Options (long only): max loss = premium paid × contracts
- Shares: max loss = (entry price − stop-loss) × shares

If a single instrument's cost already exceeds the per-trade cap (common with high-priced megacaps and single options contracts — see the 2026-07-01 META worked example in [sessions/](../sessions/2026-07-01-speculation-module-worked-example-meta.md)), the disciplined answer is to **pass on that trade**, not to loosen the cap.

## Rule 4 — Funding

Up to **10% of each new monthly contribution** may route to the sleeve, bounded by Rule 2 regardless — take whichever constraint is lower, same pattern as the core framework's Step 5 position sizing.

## Rule 5 — Separate tracking

Tracked in its own file, [portfolio/speculation-log.md](../portfolio/speculation-log.md) — never commingled with `holdings.md` rows. Use a true separate IBKR sub-account if practical; at minimum, every position in the sleeve must be tagged and excluded from core-portfolio weight/score calculations.

## Rule 6 — Entry requires a documented catalyst and window

No trade without a **written, dated, falsifiable catalyst** — a specific event (earnings print, a company confirmation/denial of a reported plan, a product launch, a regulatory decision), not "seems to be going up" or "momentum looks good." Pair it with a **time window** (days to a few months). This is the short-horizon analog of the core framework's [catalyst window](glossary.md) concept and Rule 9 — it's what keeps this sleeve from becoming plain momentum-chasing.

An **unconfirmed** report (analyst rumor, unverified media report) is not itself a catalyst — it's a reason to watch for the actual confirming or denying event, which *is* the catalyst. Treat unconfirmed reports the same way the framework already treats unconfirmed going-concern allegations: an open flag to monitor, never a settled fact to trade on.

### Strategy & instrument selection (between Rules 6 and 7, doesn't renumber either)

Once Rules 1 and 6 clear, [speculation-strategies.md](speculation-strategies.md) supplies the "which technique" layer: classifying the ticker's trend/volatility/participation regime from live data, then selecting from an evidence-graded menu (momentum/breakout, post-earnings drift, catalyst binary event, mean-reversion bounce). That file never overrides any number in this one — it only decides direction and instrument (shares, or a single long call/put per Rule 8) before Rules 7–9 size and bound the trade.

## Rule 7 — Estimating the move (upside), using live market data only

Short-horizon trades aren't priced by DCF/multiple convergence — the question isn't "what's this worth," it's "how far could this move by a specific date." Never guess a percentage. Use what the options market is already pricing:

```
1-SD expected move (%) = Implied Volatility (annualized) × √(days in your window ÷ 365)
1-SD expected move ($) = Stock price × the above
```

Cross-check with the **ATM straddle price** (call + put at the nearest strike to spot, same expiration) ÷ stock price — for near-dated options this runs close to (slightly under) the 1-SD figure above; a wide gap between the two methods means check the specific option's own implied vol (`option_midpoint_iv`) rather than a blended underlying figure.

Also compare current implied vol to trailing 30-day **historical** (realized) volatility:
- IV well above historical vol → the market is pricing real event/uncertainty risk (an open rumor, an upcoming print) — expect the premium to be rich.
- IV near or below historical vol → no special event priced in; a "big move coming" thesis isn't shared by the market.

This band is **what the market already thinks is possible, not a prediction** — it tells you the going odds, so you can judge whether your own view is more aggressive than consensus or just restating it.

## Rule 8 — Downside is estimated the same way, before entry, every time

- **Options (long calls/puts only, defined-risk):** max loss = premium paid. A known, capped dollar figure before you enter — no stop-loss guesswork, can't gap through it.
- **Shares:** stop-loss set at the price level that specifically **invalidates the catalyst thesis**, not an arbitrary round number. Default band 15–20% (tighter than core positions' calculated stops). State explicitly: a stop-loss is not a guaranteed floor — it can gap through on overnight/pre-market confirm-or-deny news, exactly the kind of event this sleeve trades.
- **IV crush (options-specific):** once the catalyst resolves — confirmed or denied — implied volatility typically drops sharply regardless of which way the stock moves. A long option can lose value even on a correct directional call, because the uncertainty premium you paid for evaporates. Factor this into sizing, not just direction.
- **Portfolio-level worst case:** the Rule 2 bucket cap is the hard ceiling — full sleeve wipeout costs no more than 5% of total portfolio, by construction.

## Rule 9 — Exit discipline, pre-committed in writing at entry

- Hard **time-stop**, default 90 days (adjustable per catalyst, but fixed before entry) — thesis hasn't resolved, exit regardless of P&L, no extensions.
- **No averaging down on losers.** Ever. This single rule is the one most directly tied to the retail blowups in the Barber & Odean / day-trading research behind this module (see the 2026-07-01 chat session that proposed it).
- No naked/uncovered options, no margin leverage beyond the sleeve's own cash.
- Minimum **2:1 risk/reward** at entry — same bar as the core framework's Step 6. Short horizon is not an excuse for worse odds.

## Rule 10 — Promotion path: sleeve → core

If a speculative thesis matures into genuine multi-year conviction: re-run full Phase 02 valuation scoring plus the Rate Environment Gate, fresh. If it clears normal core entry rules (action band, R/R, position cap), reclassify the existing shares into `holdings.md` — logged in `decisions/` as a **reclassification, not a new buy** (no sale occurs, so no forced tax event, but confirm local tax treatment before relying on that). Good short-term P&L is never itself a green light to skip Phase 02 — a name that traded well can still fail the entry rules that matter for a multi-year hold.

## Rule 11 — Logging and the kill switch

Every trade recorded in [portfolio/speculation-log.md](../portfolio/speculation-log.md): thesis, catalyst, entry/exit, size, stop, time-stop, outcome. **Review monthly**, not annually — horizon is weeks, not years. Track win rate and **expectancy** net of costs (avg win × win rate − avg loss × loss rate). If the sleeve underperforms a passive benchmark (S&P 500, or simply holding the same names long-term) over a rolling sample (20+ trades or 6–12 months), that is a **documented trigger** to shrink the cap or pause new entries — the same self-correcting audit loop [graveyard-audit.md](graveyard-audit.md) and [benchmark-comparison.md](benchmark-comparison.md) already run for the core side.

## Open items

- Confirm bucket cap (default proposed: 5%) and per-trade cap (default proposed: 20% of sleeve) — adjust in Rules 2–3 above once confirmed.
- Confirm whether a true separate IBKR sub-account is practical, or whether tagged tracking in `portfolio/speculation-log.md` is sufficient (Rule 5).
- Confirm tax jurisdiction/treatment for short-term gains before relying on Rule 4/10's cost assumptions — not something this framework can infer.
- ~~No slash command exists yet for this module~~ — [`/speculate`](../.claude/commands/speculate.md) added 2026-07-04, at the user's explicit request, ahead of the sequencing originally suggested above (rules confirmed + a few real trades first). The command reads the bucket/per-trade cap percentages live from Rules 2–3 rather than hardcoding them, so it stays correct once those numbers are actually confirmed.

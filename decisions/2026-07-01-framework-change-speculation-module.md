# 2026-07-01 — Framework change: Speculation Module (satellite sleeve) added

**What prompted it:**

The user observed that some existing holdings were entered outside the core framework's long-term rules — for speculation, or before the framework existed — and that this leakage already shows up in [override-log.md](../portfolio/override-log.md) (AVGO bought outside the valuation entry zone, DUOL/STIM on waived quality criteria). Rather than let the speculative impulse keep contaminating the core long-term book undocumented, the user wanted a formal, bounded module for short-horizon (days/weeks/months) speculative trades — with the core framework's Quality Gate acting as the entry gate, so speculation is only ever done on businesses the user would be happy to hold long-term anyway.

Before drafting rules, researched whether this is destructive/less profitable, per the user's explicit request: Barber & Odean (2000) and the Brazil/Taiwan day-trading studies confirm frequent, unstructured, cost-heavy trading reliably underperforms — but that research indicts *unbounded* speculation (any name, no size cap, no exit discipline), not a small, quality-gated, capped sleeve specifically. Benjamin Graham's own "mad money account" (a strictly separate speculative sub-account, ≤10% of total wealth) is the direct precedent for the bounded version, and core-satellite portfolio construction is standard institutional practice. Full research discussion is in this session's chat log (not separately filed — see git blame on this commit for the conversation date).

**The decision:**

1. **Eligibility = existing Quality Score gate, reused as-is.** A ticker must already clear the 80.0+ Quality Score bar (quality-scoring.md) to be speculation-eligible — no separate, weaker bar for the sleeve. Valuation score/action band is explicitly irrelevant to sleeve entry.
2. **Bucket cap 5% of total portfolio, hard ceiling 10%.** Proposed default from Graham's own ceiling, sized conservatively (institutional core-satellite satellites run 10–30%, but that's typically for tactical *quality* tilts, not raw speculation) — flagged as adjustable, not yet a fully confirmed number.
3. **Separate tracking required, true sub-account preferred.** Mirrors Graham's "never mingle the funds" rule; mechanically prevents speculative options/margin approval from touching core-book collateral.
4. **A documented catalyst + time window is mandatory for every trade** (Rule 6) — the short-horizon analog of Rule 9, specifically to prevent this sleeve from becoming plain momentum-chasing.
5. **Move-sizing method = live options-market data (implied volatility → expected move), never a guessed percentage** — extends Rule 0's "never invent or estimate financial data" discipline to short-term price forecasts, which this framework had no prior methodology for.

**What was added:**

- **`framework/speculation-module.md`** (new file) — full ruleset: eligibility gate, bucket/per-trade caps, funding rule, catalyst requirement, upside/downside estimation methodology (implied-vol-based expected move, ATM straddle cross-check, IV-crush risk), exit discipline (time-stop, no averaging down, minimum 2:1 R/R), promotion path back to the core book, and a monthly-reviewed log with its own kill-switch trigger (expectancy underperforming a passive benchmark).
- **`portfolio/speculation-log.md`** (new file) — the sleeve's own tracking log, mirroring `override-log.md`'s structure (currently empty — no trade has been entered yet; see the 2026-07-01 META worked example below for why).
- **`sessions/2026-07-01-speculation-module-worked-example-meta.md`** (new file) — a live worked example using META's real 2026-07-01 intraday move (+10.07% on an unconfirmed Bloomberg report of Meta considering selling excess AI compute capacity) to demonstrate Rules 1, 6, 7, and 8 end-to-end. Outcome: no trade — META's Quality Score is not yet confirmed under the current methodology (Rule 1 fails until `/rescore` runs), the report is unconfirmed so no catalyst is yet documented (Rule 6 fails), and at current portfolio size a single properly-sized options contract already exceeds the proposed per-trade cap (Rule 3 fails). All three gates independently said "not yet" — recorded as the module's first working test, not a missed opportunity.
- **`framework/glossary.md`** — added a "Behavioral-finance & speculation terms" section: barbell strategy, core-satellite, disposition effect, expectancy, house money effect, mad money account, mental accounting, time-stop, turnover.
- **`framework/investor-philosophy-alignment.md`** — added a second "conscious divergence on record" entry (see below).
- **`CLAUDE.md`** — added the new file to the Orientation list.

**Alignment check (per [investor-philosophy-alignment.md](../framework/investor-philosophy-alignment.md)):**

- **Price-action test: FAILS, by design — conscious divergence.** Individual trades inside the sleeve are explicitly triggered by price/news moves and options-market pricing, not fundamentals. This is the one test the module cannot pass and isn't trying to — see the divergence note below.
- **Turnover test: FAILS, by design — conscious divergence.** The sleeve exists specifically to increase trading frequency without a fundamental change at each trade. Bounded by the bucket cap, per-trade cap, and the Rule 11 kill switch rather than avoided outright.
- **Mean-reversion test: PASS.** Move-sizing (Rule 7) uses live, forward-looking, market-implied volatility — not a stale historical multiple or average — so it doesn't fall into the "assumes the old anchor still holds" trap Marks warns about.
- **Macro-veto test: N/A.** The module is entirely name-and-catalyst-specific; no macro/rate view enters it.
- **Concentration test: not in tension.** The Rule 3 "5+ names within the sleeve" guidance isn't diversification-as-a-substitute-for-conviction (the core test's target) — it bounds single-event/binary-news risk *within* an already-capped, non-core sleeve where multi-year conviction was never the basis for sizing in the first place.
- **Guidance test: PASS.** Rule 6 explicitly treats unconfirmed reports/rumors as open flags to monitor, never tradeable facts — the same treatment the framework already gives unconfirmed going-concern allegations, just applied in the bullish direction.

**Conscious divergence on record — the Speculation Module (added 2026-07-01).** This module knowingly fails the price-action and turnover tests that every core-framework rule is otherwise checked against. That is deliberate, not an oversight: Benjamin Graham — Buffett's own teacher — explicitly carved out this exact exception (a small, separate "mad money" account, capped, never mingled with the core book), and the fence around it here is tighter than Graham's original (a 5% proposed cap vs. his 10%, plus a quality-gated universe he didn't require). The core book's 100%-fundamentals discipline is preserved *because* the sleeve is walled off and capped — the point is not that price-action decisions never happen anywhere in the portfolio, it's that they can never contaminate the core book's scoring or sizing. Recorded here, like the 15% position cap and the Upside/Downside Modifier, as a bounded tradeoff rather than an unflagged inconsistency.

**Open item:** bucket cap (5%), per-trade cap (20% of sleeve), and default time-stop (90 days) are proposed defaults pending the user's confirmation — see the "Open items" section at the bottom of `framework/speculation-module.md`. No slash command exists yet for this module.

**Files touched:**
- `framework/speculation-module.md` (new)
- `framework/investor-philosophy-alignment.md`
- `framework/glossary.md`
- `portfolio/speculation-log.md` (new)
- `sessions/2026-07-01-speculation-module-worked-example-meta.md` (new)
- `CLAUDE.md`
- `decisions/` — this file.

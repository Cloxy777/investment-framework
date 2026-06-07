# 2026-06-07 — Framework change: single-position hard cap raised from 8% to 15%

**What changed:**

**Upgrade 7 (single-position hard cap):** raised from **8% → 15%** in [strategy.md](../framework/strategy.md) and [operating-brief.md](../framework/operating-brief.md). Nothing else in the framework changed.

**Why:**

8% felt too tight for the level of concentration the user is comfortable carrying in high-conviction names. 15% is a deliberate, recorded override of the Verdad-research-backed 8% figure (empirically validated across 10,000 simulated portfolios) — noted explicitly here so a future reviewer understands this is a conscious choice to trade some of that empirical backing for more concentration latitude, not an oversight.

**What stays the same (intentionally):**

- **Phase 05 Dynamic Trimming remains valuation-score-band-driven**, exactly as originally specified: Score 6–7 → trim 25–30%, Score 8 → trim to 50%, Score 9–10 → trim to 1–2% tracking position. *(An earlier draft of this change also proposed switching the trim trigger from score-bands to fair-value-derived price targets — the user explicitly did not want that part changed, so it has been reverted and is not part of this decision. Trims continue to fire off the 1–10 valuation score crossing a band, as before.)*
- **BUY sizing remains score-driven** (Score 1–3 → full position 6–8%, Score 4–5 → standard position 3–5%) — unaffected either way, since this was never in scope for either version of the change.
- **Phase 06's "Score 10 sustained 2+ quarters → Full Exit"** backstop is untouched.
- The **Fundamental Sell Triggers** (thesis broken, margin compression, ROIC below cost of capital, etc.) in `fair-value-methodology.md` Step 3 are unaffected.

**Files touched:**
- `framework/strategy.md` — Upgrade 7 heading and cap figure (8% → 15%)
- `framework/operating-brief.md` — Upgrade 7 line (8% → 15%)

**Revision note:** this entry supersedes and replaces `decisions/2026-06-07-framework-change-cap-and-trim-rule.md`, which bundled the cap raise together with a Dynamic-Trimming mechanism change the user did not actually want. That combined change was reverted in full (commit reverting the merge that introduced it) and the cap-only change re-applied cleanly on top, so the trim mechanic is back to its original score-band form. Lesson for future framework-change sessions: land independent changes as independent, separately-reviewable commits/PRs rather than bundling them — it makes a partial revert like this one a non-event instead of a small surgical operation.

**Follow-up:** the `/rebalance` session should be run against the new 15% cap. Under it, MSFT (16.84%) and AMZN (10.49%) are no longer forced trims by the cap alone (though MSFT's 16.84% would *still* breach even the relaxed 15% cap and remains a compliance issue in its own right); TLT (30.77%) would breach either cap figure and remains the documented framework gap (no fixed-income sizing methodology exists — see the full-portfolio rescore session log for detail).

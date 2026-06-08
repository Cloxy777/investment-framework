# 2026-06-08 — Framework fix: PEG weighting inconsistency

**What changed:**

`framework/valuation-scoring.md` framed PEG as a weighted component of the raw score — `Final Score = (FCF × 0.40) + (EV/EBIT × 0.25) + (FwdPE_adjusted × 0.20) + (PEG_or_fallback × 0.15) + Rate Regime Modifier`, with a note instructing that "if PEG is not applicable (non-Fast Grower), redistribute its 15% weight to EV/EBIT (making EV/EBIT weight 40%)." This treats PEG as a 1–10 sub-score multiplied by a 15% weight, exactly like FCF, EV/EBIT, and Forward PE.

But `strategy.md`'s Upgrade 3 (and `operating-brief.md`'s reproduction of it) defines PEG purely as a small additive modifier table — PEG <0.8 → −1, 0.8–1.2 → 0, 1.2–1.8 → +0.5, >2.0 → +1 — identical in form and placement to the Historical PE Modifier (Upgrade 2) and the Rate Regime Modifier. A −1…+1 additive value cannot coherently be "scored 1–10 and multiplied by 0.15"; the two framings are mathematically incompatible, and the "redistribute the weight" instruction only makes sense under the (wrong) weighted-sub-score framing.

This was not a hypothetical found by audit — it surfaced live, mid-session, while scoring MA and ABNB: both were judged Stalwarts (not Fast Growers), both sessions had to explicitly choose one framing over the other to even produce a number, and both flagged the contradiction inline rather than silently picking a side.

**Resolution chosen:** treat PEG strictly as the additive modifier that `strategy.md`/`operating-brief.md` already define (the form that appears identically in two of the three docs, and the only form that's dimensionally consistent with the −1…+1 table). EV/EBIT is now permanently 40%-weighted — there is no separate PEG "slot" to redistribute from, so the conditional redistribution language is removed entirely. Fast Growers receive the PEG modifier as a bolt-on after the raw weighted score, exactly like the Historical PE and Rate Regime modifiers; non-Fast-Growers simply don't receive it.

```
Final Score = (FCF × 0.40) + (EV/EBIT × 0.40) + (FwdPE_adjusted × 0.20) + Rate Regime Modifier [+ PEG Modifier — Fast Growers only]
```

**Why this framing over the alternative:**
The other way to resolve the contradiction would have been to keep PEG as a weighted 1–10 sub-score and rewrite Upgrade 3's table into score-band form. That would have meant inventing a PEG → 1–10 mapping that doesn't exist anywhere in the framework's history, on top of redefining what "Fast Grower only" means for the other 85% of the universe (the redistribution problem doesn't go away — it just moves). The additive-modifier framing requires no invention: it's already fully specified, already dimensionally consistent with how Upgrade 2 and the Rate Regime Modifier work, and already the form actually applied in the MA and ABNB sessions before this fix (both sessions independently converged on "PEG not applied → EV/EBIT effectively 40%" as the only coherent reading).

**Files touched:**
- `framework/valuation-scoring.md` — Final Score formula, EV/EBIT weight (25% → 40%), PEG section reframed from "15% weight" to "additive modifier"
- `framework/strategy.md` — "Updated Valuation Score Weighting" table: EV/EBIT row (25% → 40%), PEG Modifier row reframed as additive (−1…+1), not a percentage weight
- `framework/operating-brief.md` — EV/EBIT weight heading (25% → 40%), PEG Modifier description reframed as additive (matching Upgrade 3's table directly instead of "(PEG_or_fallback × 0.15)"), Final Score formula line

**Follow-up:**
- Any prior session that scored a Fast Grower using the old `(PEG × 0.15)` weighted framing should be revisited if it materially changed the action band — the additive modifier (max swing ±1) moves the final score far less than a 15%-weighted 1–10 sub-score could (max swing up to 1.5). No such session exists yet in `sessions/` as of this fix.
- This closes the second of two internal contradictions surfaced during the 2026-06-07/08 MA and ABNB `/new-position` sessions; the first (Rate Environment Gate Step 1 veto-vs-modifier wording drift) was fixed the same way in `operating-brief.md` on 2026-06-08 (see the MA session for the original flag).

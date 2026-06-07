# 2026-06-07 — Framework change: position cap raised to 15%, Dynamic Trimming switched from score-bands to price-targets

**What changed:**

1. **Upgrade 7 (single-position hard cap):** raised from **8% → 15%** in [strategy.md](../framework/strategy.md) and [operating-brief.md](../framework/operating-brief.md).
2. **Phase 05 (Dynamic Trimming):** the trim trigger changed from **valuation-score bands** (Score 6–7 → trim 25–30%, Score 8 → trim to 50%, Score 9–10 → trim to 1–2%) to **fair-value-derived price targets**, reusing the Primary Sell Target / Bull-Case Trim Target levels already defined in [fair-value-methodology.md](../framework/fair-value-methodology.md) Step 3:
   - Price ≥ **Primary Sell Target** (Fair Value) → trim 50% of the position
   - Price ≥ **Bull-Case Trim Target** (Bull-Case Fair Value × 0.90) → trim the remainder to a 1–2% tracking position

**Why:**

- **Cap:** 8% felt too tight for the level of concentration the user is comfortable carrying in high-conviction names. 15% is a deliberate, recorded override of the Verdad-research-backed 8% figure (validated across 10,000 simulated portfolios) — noted explicitly here so a future reviewer understands this is a conscious choice to trade some of that empirical backing for more concentration latitude, not an oversight.
- **Trim trigger:** the user does not want trims to fire mechanically off a score crossing a threshold. They want to take profits when the **price itself** has reached a level that's "good enough" relative to the business's worth — i.e., still valuation-grounded, just expressed as a price level (Fair Value / Bull-Case Fair Value) rather than a 1–10 score band. This keeps trimming disciplined and fair-value-anchored (consistent with the framework's "never act on price movement alone" principle — the trigger is still tied to a calculated fair value, not a raw price move) while removing the score-band mechanic the user found too rigid.

**What stays the same (intentionally):**

- **BUY sizing remains score-driven** (Score 1–3 → full position 6–8%, Score 4–5 → standard position 3–5%). Only the *sell* side moved to a price basis — the asymmetry is deliberate: "is this cheap enough to buy" and "is this rich enough to sell" are being judged on different, complementary bases by design.
- **Phase 06's "Score 10 sustained 2+ quarters → Full Exit"** remains a score-based backstop. It's a rare, extreme-overvaluation trigger for a full exit — categorically different from routine trimming, and left untouched.
- The **Fundamental Sell Triggers** (thesis broken, margin compression, ROIC below cost of capital, etc.) that override price targets in `fair-value-methodology.md` Step 3 are unaffected — they were already event-based, not score-based.

**Files touched:**
- `framework/strategy.md` — Phase 05 block, Action Table Summary (TRIM rows), Upgrade 7
- `framework/operating-brief.md` — Upgrade 7 line, ACTION TABLE (TRIM rows)
- `framework/fair-value-methodology.md` — added a cross-reference noting Step 3's Sell Target / Bull-Case Trim Target levels now also serve as the Phase 05 ongoing-trim triggers (single source of truth, not redefined)

**Follow-up:** the `/rebalance` session originally requested should be re-run against these new rules. Under a 15% cap, MSFT (16.84%) and AMZN (10.49%) are no longer forced trims by the cap alone; TLT (30.77%) would still breach even the relaxed cap and remains a framework gap (no fixed-income sizing methodology exists). Trim recommendations for richly-valued names (e.g. AMZN, CSGP, GOOG, SPOT — all Score 8) now require calculating each holding's Fair Value and Bull-Case Fair Value first, since the trigger is price-based rather than score-based.

# 2026-06-11 — Framework change: valuation score rescaled from 1–10 to 0.0–99.9

**What changed:**

The Phase 02 valuation score — and all four of its weighted sub-scores (FCF Yield, EV/EBIT, Forward PE, PEG) — moved from the original **1–10 integer scale** to a continuous **0.0–99.9 scale** (one decimal place), at the user's request for more precision. 0 = cheapest/most attractive, 99.9 = most expensive, preserving the original direction.

**Sub-scores are now formulas, not buckets:**

- **FCF Yield (40%):** `clamp(99.9 × (1 − FCF_Yield% / 10), 0, 99.9)` — replaces the old 5-row discrete table.
- **EV/EBIT (25%):** `clamp((EV/EBIT − 12) / 23 × 99.9, 0, 99.9)` — replaces the old 6-row discrete table.
- **Forward PE (20%):** `clamp((FwdPE − 10yr Low PE) / (10yr High PE − 10yr Low PE) × 99.9, 0, 99.9)`, then the Historical PE Modifier (Upgrade 2), now ±10/0 instead of ±1/0.
- **PEG (15%, Fast Growers only):** `clamp((PEG − 0.5) / 2.0 × 99.9, 0, 99.9)` — see "Fix folded in" below.

Full formulas and reference tables live in [valuation-scoring.md](../framework/valuation-scoring.md).

**Modifiers rescaled ×10:** Rate Regime Modifier (−1/0/+0.5/+1 → −10/0/+5/+10), Earnings Yield Spread flag (+0.5 → +5), Rate-Normalised PE annual adjustment (+0.5 → +5), Historical PE Modifier (±1 → ±10).

**Action bands proportionally rescaled** (each old integer band's share of the 1–10 range is preserved exactly):

| Old (1–10) | New (0.0–99.9) | Label | Action |
|---|---|---|---|
| 1–3 | 0.0–29.9 | Very Cheap | Full position 6–8% |
| 4–5 | 30.0–49.9 | Cheap | Standard position 3–5% |
| 6–7 | 50.0–69.9 | Fair Value | Hold, watch only |
| 8 | 70.0–79.9 | Expensive | Trim 25–30% |
| 9 | 80.0–89.9 | Very Expensive | Trim to 50% |
| 10 | 90.0–99.9 | Extreme | Trim to 1–2% / Full Exit if sustained 2+ qtrs |

This is a clean 30/20/20/10/10/10 split of the 0–99.9 range, identical in proportion to the original 1–10 bands.

**Rounding rule:** "round to nearest integer, .5 rounds up, min 1 max 10" → "round to nearest 0.1, .X5 rounds up, min 0.0 max 99.9" (the same conservative tie-break, one decimal place finer).

**Fix folded in — PEG was scale-inconsistent:** The original Final Score Formula treated `PEG_or_fallback × 0.15` as a weighted sub-score parallel to FCF/EV-EBIT/FwdPE (each 1–10), but `valuation-scoring.md` defined PEG as a **modifier** ranging only −1 to +1 — an order of magnitude smaller than the other three terms it was being averaged with at the same weight. The new `PEG_Score` formula gives PEG a proper 0–99.9 sub-score on equal footing with the other three, removing this latent inconsistency. Its anchor points (PEG 0.5→0, 1.5→≈50, 2.5→99.9) preserve the original table's direction (low PEG = cheap = "good", high PEG = expensive = "trim bias").

**Existing holdings.md scores converted, not re-derived:** `portfolio/holdings.md` "Last Score" values were on the old 1–10 scale. Per user direction, these were mechanically converted via:

```
New Score = (Old Score − 1) × 11.1
```

(1→0.0, 2→11.1, 3→22.2, 4→33.3, 5→44.4, 6→55.5, 7→66.6, 8→77.7, 9→88.8, 10→99.9 — all clean one-decimal values, and each lands inside its corresponding new action band above, so no holding's action classification changes as a side effect of the rescale alone.)

These converted values are **placeholders** — they reflect the old discrete bucket the company was in, not a fresh computation under the new continuous formulas. holdings.md is flagged accordingly; full precision requires re-running `/rescore` per holding.

**What stays the same (intentionally):**

- Sub-score weights: FCF 40% / EV-EBIT 25% / FwdPE 20% / PEG 15% (or EV-EBIT 40% if PEG n/a) — unchanged.
- All metric definitions, the Rate Environment Gate structure, Upgrades 1, 4, 5, 7, the Quantitative Pre-Screen Filters (Phase 01, which are absolute thresholds, not scores), and position-sizing percentages (6–8% / 3–5% / etc.) — unchanged.
- Investment philosophy and trim/exit logic — unchanged, only re-expressed on the new scale.

**Files touched:**
- `framework/valuation-scoring.md` — full rewrite of Final Score Formula + sub-score section, added legacy-conversion table
- `framework/strategy.md` — Rate Environment Gate, Phase 02/03/05/06, Action Table Summary, Upgrade 2, Upgrade 3, weighting table
- `framework/operating-brief.md` — calculation rules, action table, order setup, full-exit trigger
- `framework/fair-value-methodology.md` — MoS table, score-integration table, sell triggers, stop-loss table, position-size table, order checklist
- `framework/graveyard-audit.md` — illustrative score references in Cisco/Peloton case studies
- `portfolio/holdings.md` — converted Last Score column + explanatory note
- `portfolio/override-log.md` — score-band references in override definitions and historical audit
- `.claude/commands/rebalance.md` — Phase 05/06 score-band references

**Not touched (historical record, left on old scale):** `sessions/*` and prior `decisions/*` entries — these are dated logs of what was decided at the time under the 1–10 scale. Use the conversion formula above (also in `valuation-scoring.md`) if comparing them against current scores.

**Follow-up:** Run `/rescore` on each current holding to replace the converted placeholder scores in `holdings.md` with fresh values computed under the new continuous formulas — this is where the added precision actually starts paying off (e.g. distinguishing two "Score 6" names that previously looked identical).

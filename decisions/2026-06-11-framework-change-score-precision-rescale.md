# 2026-06-11 — Framework change: valuation score rescaled from 1–10 to 0.0–100.0

**What changed:**

The Phase 02 valuation score — and all four of its weighted sub-scores (FCF Yield, EV/EBIT, Forward PE, PEG) — moved from the original **1–10 integer scale** to a continuous **0.0–100.0 scale** (one decimal place), at the user's request for more precision. 0 = cheapest/most attractive, 100.0 = most expensive, preserving the original direction.

**Cap set to 100.0, not 99.9 (same-day refinement):** the rescale was first drafted with a 99.9 cap (mirroring "1–10" → "0–9.9"-style thinking), then revised same-day to a clean **100.0** cap at the user's request. 100.0 makes two of the sub-score formulas land on round numbers at their defined extremes — EV/EBIT hits exactly 100.0 at 35×, and PEG hits exactly 100.0 at PEG=2.5 — rather than 99.9 at those same inputs. All formulas, tables, and bands below reflect the final 100.0-cap version.

**Sub-scores are now formulas, not buckets:**

- **FCF Yield (40%):** `clamp(100 × (1 − FCF_Yield% / 10), 0, 100)` — replaces the old 5-row discrete table.
- **EV/EBIT (25%):** `clamp((EV/EBIT − 12) / 23 × 100, 0, 100)` — replaces the old 6-row discrete table.
- **Forward PE (20%):** primary formula `clamp((FwdPE − 10yr Low PE) / (10yr High PE − 10yr Low PE) × 100, 0, 100)`, then the Historical PE Modifier (Upgrade 2), now ±10/0 instead of ±1/0. Where only a single-point 10yr average PE is available (no range), a new **fallback formula** applies instead — see "Forward PE fallback formulas" below.
- **PEG (15%, Fast Growers only):** `clamp((PEG − 0.5) / 2.0 × 100, 0, 100)` — see "Fix folded in" below.

Full formulas and reference tables live in [valuation-scoring.md](../framework/valuation-scoring.md).

**Forward PE fallback formulas (new, added when populating real holdings.md scores):** most holdings only have a single-point "10yr average PE," not a 10yr Low/High range, so the primary formula above can't be applied directly. Two fallbacks were added to `valuation-scoring.md`:

- **Avg-only fallback:** `Deviation% = (FwdPE − 10yr Avg PE) / 10yr Avg PE × 100`, then `FwdPE_Score = clamp(50 + Deviation% × 2.5, 0, 100)`. This generalises the old discrete "vs. 10yr avg PE" bucket table into a continuous function: centers at 50 when FwdPE = avg, reaches 0 at −20% deviation (cheap) and 100 at +20% deviation (expensive). It **folds in the Historical PE Modifier (Upgrade 2) directly** — do not also apply the separate ±10 modifier on top of this fallback.
- **No-history fallback:** where no usable 10yr PE reference exists at all, `FwdPE_Score = 50.0` (neutral, flagged as low-confidence/placeholder until a real 10yr PE history is sourced).

**Modifiers rescaled ×10:** Rate Regime Modifier (−1/0/+0.5/+1 → −10/0/+5/+10), Earnings Yield Spread flag (+0.5 → +5), Rate-Normalised PE annual adjustment (+0.5 → +5), Historical PE Modifier (±1 → ±10).

**Action bands proportionally rescaled** (each old integer band's share of the 1–10 range is preserved exactly, with the top band extended to the clean 100.0 cap):

| Old (1–10) | New (0.0–100.0) | Label | Action |
|---|---|---|---|
| 1–3 | 0.0–29.9 | Very Cheap | Full position 6–8% |
| 4–5 | 30.0–49.9 | Cheap | Standard position 3–5% |
| 6–7 | 50.0–69.9 | Fair Value | Hold, watch only |
| 8 | 70.0–79.9 | Expensive | Trim 25–30% |
| 9 | 80.0–89.9 | Very Expensive | Trim to 50% |
| 10 | 90.0–100.0 | Extreme | Trim to 1–2% / Full Exit if sustained 2+ qtrs |

This is a clean 30/20/20/10/10/10 split of the 0–100.0 range (the top band is 101 values wide vs. 100 for the others — negligible), identical in proportion to the original 1–10 bands.

**Rounding rule:** "round to nearest integer, .5 rounds up, min 1 max 10" → "round to nearest 0.1, .X5 rounds up, min 0.0 max 100.0" (the same conservative tie-break, one decimal place finer).

**Fix folded in — PEG was scale-inconsistent:** The original Final Score Formula treated `PEG_or_fallback × 0.15` as a weighted sub-score parallel to FCF/EV-EBIT/FwdPE (each 1–10), but `valuation-scoring.md` defined PEG as a **modifier** ranging only −1 to +1 — an order of magnitude smaller than the other three terms it was being averaged with at the same weight. The new `PEG_Score` formula gives PEG a proper 0–100.0 sub-score on equal footing with the other three, removing this latent inconsistency. Its anchor points (PEG 0.5→0, 1.5→50, 2.5→100.0) preserve the original table's direction (low PEG = cheap = "good", high PEG = expensive = "trim bias").

**Legacy 1–10 → 0.0–100.0 conversion formula** (for any historical scores still on the old scale, e.g. in `sessions/` or prior `decisions/` entries):

```
New Score = (Old Score − 1) × 100/9
```

(1→0.0, 2→11.1, 3→22.2, 4→33.3, 5→44.4, 6→55.6, 7→66.7, 8→77.8, 9→88.9, 10→100.0 — all clean one-decimal values.)

**Existing holdings.md scores: real recalculation (same day, second pass):** an initial pass mechanically converted `holdings.md` "Last Score" values from the old 1–10 scale via the formula above, as a placeholder. Per user follow-up direction ("the existing holdings should be recalculated according to the formulas"), those placeholders were replaced with **real computations** under the new continuous sub-score formulas (FCF Yield 40% / EV-EBIT 25% / FwdPE 20% / PEG 15% or EV-EBIT 40% fallback) plus the +5 Rate Regime Modifier (10Y Treasury 4.55%, in the 3.5–5% bracket). Inputs are the underlying metrics already gathered in [sessions/2026-06-07-rescore-full-portfolio.md](../sessions/2026-06-07-rescore-full-portfolio.md) and [sessions/2026-06-07-rescore-nvda.md](../sessions/2026-06-07-rescore-nvda.md) — **no new Rule 0 live-price pull was performed**, so this recomputes the existing dataset under the new formulas rather than refreshing it. Full per-ticker arithmetic (every sub-score, the raw weighted sum, the modifier, and the rounded final score) is in [sessions/2026-06-11-rescore-holdings-new-scale.md](../sessions/2026-06-11-rescore-holdings-new-scale.md).

| Ticker | Placeholder (1st pass) | Real score (2nd pass) | Band | Band changed vs. placeholder? |
|---|---|---|---|---|
| AMZN | 77.7 | 79.8 | Expensive | No |
| CSGP | 77.7 | 83.3 | Very Expensive | **Yes — was Expensive (Trim 25–30%), now Very Expensive (Trim to 50%)** |
| DUOL | 33.3 | 49.1 | Cheap | No |
| GOOG | 77.7 | 83.7 | Very Expensive | **Yes — was Expensive (Trim 25–30%), now Very Expensive (Trim to 50%)** |
| META | 44.4 | 43.7 | Cheap | No |
| MSFT | 55.5 | 52.9 | Fair Value | No |
| NFLX | 66.6 | 58.9 | Fair Value | No |
| NKE | 33.3 | 34.1 | Cheap | No |
| NOW | 55.5 | 59.3 | Fair Value | No |
| NVDA | 55.5 | 62.2 | Fair Value | No |
| NVO | 33.3 | 35.8 | Cheap | No |
| SPGI | 44.4 | 43.3 | Cheap | No |
| SPOT | 77.7 | 82.0 | Very Expensive | **Yes — was Expensive (Trim 25–30%), now Very Expensive (Trim to 50%)** |
| UBER | 55.5 | 52.9 | Fair Value | No |
| V | 55.5 | 54.9 | Fair Value | No |
| ZS | 55.5 (low-confidence) | 61.1 (low-confidence) | Fair Value | No |

RBRK, STIM, TLT, XEON, and both CASH rows remain unscored (out of scope per the existing notes in `holdings.md`).

**Three band changes flagged — CSGP, GOOG, SPOT** moved from "Expensive" (Trim 25–30%) to "Very Expensive" (Trim to 50%) once recomputed under the continuous formulas. These should be prioritised in the next `/rebalance`, but a fresh Rule 0 live-price `/rescore` is recommended first given the staleness of the underlying price data (see Follow-up below).

**What stays the same (intentionally):**

- Sub-score weights: FCF 40% / EV-EBIT 25% / FwdPE 20% / PEG 15% (or EV-EBIT 40% if PEG n/a) — unchanged.
- All metric definitions, the Rate Environment Gate structure, Upgrades 1, 4, 5, 7, the Quantitative Pre-Screen Filters (Phase 01, which are absolute thresholds, not scores), and position-sizing percentages (6–8% / 3–5% / etc.) — unchanged.
- Investment philosophy and trim/exit logic — unchanged, only re-expressed on the new scale.

**Files touched:**
- `framework/valuation-scoring.md` — full rewrite of Final Score Formula + sub-score section (cap=100.0), Forward PE primary/fallback/no-history formulas, legacy-conversion table
- `framework/strategy.md` — Rate Environment Gate, Phase 02/03/05/06, Action Table Summary, Upgrade 2, Upgrade 3, weighting table (all 99.9→100.0)
- `framework/operating-brief.md` — calculation rules, Forward PE fallback formulas, action table, order setup, full-exit trigger
- `framework/fair-value-methodology.md` — MoS table, score-integration table, sell triggers, stop-loss table, position-size table, order checklist
- `framework/graveyard-audit.md` — illustrative score references in Cisco/Peloton case studies
- `portfolio/holdings.md` — Last Score column replaced with real recomputed scores (see table above) + explanatory note + link to new session log
- `portfolio/override-log.md` — score-band references in override definitions and historical audit
- `.claude/commands/rebalance.md` — Phase 05/06 score-band references
- `CLAUDE.md` — score-range reference in Orientation section
- `sessions/2026-06-11-rescore-holdings-new-scale.md` — **new**, full per-ticker arithmetic for the holdings.md recalculation

**Not touched (historical record, left on old scale):** prior `sessions/*` and `decisions/*` entries from before 2026-06-11 — these are dated logs of what was decided at the time under the 1–10 scale. Use the conversion formula above (also in `valuation-scoring.md`) if comparing them against current scores.

**Follow-up:** Run a full `/rescore` with fresh Rule 0 live prices on each current holding — this recalculation reused the 2026-06-07 dataset's underlying metrics, so it reflects the new formulas but not new market data. Prioritise **CSGP, GOOG, and SPOT**, whose recomputed scores crossed an action-band boundary (Expensive → Very Expensive) and should be re-verified with current prices before any trim is executed off the back of this rescale.

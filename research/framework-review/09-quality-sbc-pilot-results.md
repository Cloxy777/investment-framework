# Part 9 — Quality-side SBC pilot (2026-10-12)

**Read-only analysis; nothing in the framework changed.** Follow-up to [08-phase-b-pilot-results.md](08-phase-b-pilot-results.md), which tested the Valuation-side SBC change. This tests the Quality side. Reproduce: `python research/framework-review/pilot/pilot_quality_sbc.py` (raw: [pilot/pilot-quality-sbc-2026-10-12.json](pilot/pilot-quality-sbc-2026-10-12.json)).

## What was tested

[quality-scoring.md](../../framework/quality-scoring.md) scores **FCF Quality** (10% weight) as `clamp((FCF/NI − 0.40) / 0.60 × 100)`. Proposed: replace FCF/NI with **(FCF − SBC)/NI**, giving `ΔQuality = 0.10 × (FCFQ_after − FCFQ_before)`. Also re-ran the existing hard disqualifier (FCF/NI < 70% for 2+ consecutive years) on the after-SBC ratio, and combined the result with the Valuation-side change for names that pass the 80.0 gate.

**Why this is not double counting.** GAAP net income already *deducts* SBC as an expense, while free cash flow *adds it back*. So today's FCF/NI compares cash before SBC with profit after SBC — an inconsistent pair that flatters any company paying heavily in shares. (FCF − SBC)/NI compares like with like. (NOW shows it: FCF/NI 274% reported vs 143% after SBC.)

**Coverage:** 16 of 20 holdings. AMZN (net income missing), NVO (SBC missing), TRN (no data), ZS (loss-making, ratio undefined). Same method limits as 08: today's live data against scores recorded at each holding's own review date; no manual inputs re-scored.

## Results

| Ticker | Quality (recorded) | FCF/NI → after SBC | FCF Quality sub-score | Δ Quality | New Quality | Gate crossed? |
|---|---|---|---|---|---|---|
| **DUOL** | 83.2 | 97% → 62% | 94.6 → 35.9 | **−5.9** | **77.3** | **yes — falls below 80.0** |
| CSGP | 69.2 | 308% → 48% | 100 → 12.6 | −8.7 | 60.5 | no (already fails) |
| NKE | 39.1 | 70% → 47% | 50.5 → 12.1 | −3.8 | 35.3 | no (already fails) |
| META | 87.5 | 60% → 23% | 33.6 → 0 | −3.4 | 84.1 | no |
| AVGO | 86.3 | 103% → 81% | 100 → 68.0 | −3.2 | 83.1 | no |
| UBER | 59.3 | 106% → 85% | 100 → 75.6 | −2.4 | 56.9 | no (already fails) |
| MSFT | 79.9 | 50% → 41% | 16.8 → 1.3 | −1.5 | 78.4 | no (already fails; moves further away) |
| NFLX, NVDA | 69.8 / 90.3 | small shifts | — | −0.6 / −0.6 | 69.2 / 89.7 | no |
| ADBE, BKNG, NOW, SPGI, VEEV, MBGL | — | stay at or above 100% after SBC (108–180%) | 100 → 100 | 0.0 | unchanged | no |
| GOOG | 71.4 | 22% → 10% | 0 → 0 | 0.0 | 71.4 | no |

**Combined with the Valuation-side change (gate passers only):** AVGO Composite 42.6 → 45.2, META 26.0 → 27.6, NVDA 23.0 → 23.5, VEEV 40.0 → 42.0, BKNG 14.4 → 15.4, ADBE 8.4 → 10.0. **No band changes.**

## Findings

1. **The effect is real and explainable, not noise.** The big movers are the companies that pay heavily in shares (DUOL, CSGP, NOW, AVGO, META). Nine of the 16 move less than 1 point.
2. **One decision-relevant consequence: DUOL.** It is 9.24% of the book. On the Quality side alone it drops from 83.2 to 77.3 and falls below the 80.0 gate; its after-SBC FCF/NI has been shrinking (FY2023 278%, FY2024 174%, FY2025 54%). Under the strict-gate rule, a name below 80.0 gets no Composite and no adds. This is the only gate flip among current gate-passers (MSFT is already below and only moves further away; AVGO and META stay above).
3. **The hard disqualifier must NOT use after-SBC FCF.** Re-run that way it would disqualify MSFT, META, GOOG and CSGP — the AI-capex hyperscalers, whose FCF is depressed by growth capex rather than by SBC. The existing rule already carries a growth-capex exception and Upgrade 1 covers Owner Earnings; stacking SBC on top would punish those names for the wrong reason. Keep the disqualifier on the current FCF/NI definition, and keep the separate SBC ≥ 100% of FCF tripwire from the Valuation plan.
4. **Unstable denominators.** When net income is tiny or depressed (CSGP: ratios of 586% and −2186% in FY2025) FCF/NI is meaningless either way. A fix is needed regardless: a floor on net income, or a 3-year average, or use net income before SBC for the denominator. Not decided here.
5. **Sub-score calibration is a placeholder.** The 40%–100% scale was built for a world where FCF/NI is mostly above 70%. After SBC many good businesses sit at 60–80%, in the steep part of the curve. The pilot used the scale unchanged.

## Recommendation

- **Valuation side (B1 + B2): proceed** — passed in 08.
- **Quality side: supported in principle, but gate it on a decision about DUOL.** The change is consistent and fixes a real inconsistency, yet it moves one 9%-of-book holding across the gate. Suggest: (a) before adopting, re-check DUOL's SBC and net income against its filings, and (b) decide the net-income-floor rule from finding 4.
- **Do not touch the FCF/NI hard disqualifier** (finding 3).
- If adopted, bundle the Quality and Valuation SBC changes into the single methodology bump and one stale-score run, then rescore DUOL first.

## Glossary

From [framework/glossary.md](../../framework/glossary.md): **SBC (Stock-Based Compensation)**, **FCF/NI conversion ratio**, **Quality Score**, **Composite Score**, **Hard disqualifier**, **Owner Earnings**, **FCF yield**.

New terms: **Apples-to-apples (like with like)** — comparing two figures that have been treated the same way; **Denominator** — the bottom number in a ratio (here net income); when it is near zero the ratio blows up; **Gate flip** — a company moving from passing to failing the 80.0 Quality gate because of a rule change rather than a business change.

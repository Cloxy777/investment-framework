# 2026-06-20 — Framework change: Upside/Downside Modifier added to the valuation score

**What prompted it:**

The user surfaced a real gap (see the "great company never gets cheap" analysis earlier this session): the four weighted sub-scores (FCF Yield 40%, EV/EBIT 25%, Forward PE 20%, PEG 15%) are 65–80% anchored on *current/trailing* valuation. A wonderful business correctly priced for a bright future can therefore sit permanently in the 50.0–69.9 "Fair Value" band and never drop to the ≤49.9 entry gate — so the framework would never let you open it, no matter how much it's expected to earn.

The user's request: fold expected return into the *single* score, so that (a) "just look at the score and pick the lowest" is a complete ranking, and (b) when upside is thin or a downside is expected, the score rises and the framework recommends trimming/selling.

**The decision (two user choices, asked before implementing):**

1. **Downside reach → Bounded.** The modifier nudges, but a quality name near fair value is only pushed toward trimming when expected return is genuinely *negative*. This preserves the 2026-06-07 "fair value alone is not a sell" anti-turnover rule (Phase 05).
2. **Modifier weight → ±15 (stronger).** The forecast can move the score meaningfully — up to a full band — but still cannot override the bottom-up cheapness gate.

**What was added** — an additive **Upside/Downside Modifier**, bounded **[−15, +15]**, applied after the raw weighted score alongside the Rate Regime Modifier:

```
PW Fair Value  = 0.25×Bull + 0.50×Base + 0.25×Bear         (Rule 7 — downside underwritten)
Gap Upside %   = (PW Fair Value ÷ Live Price) − 1          (Live Price per Rule 0)
Annualized gap = Gap Upside % ÷ catalyst-timeline (yrs)    (Rule 10; default 2yr)
E              = Annualized gap + intrinsic growth (FCF/EPS CAGR) + shareholder yield
Hurdle H       = 10%  (midpoint of Rule 4's 8–15% implied-IRR sanity band)

If E ≥ H:      M = −15 × clamp((E−H)/15pp, 0, 1)    # strong upside → 0 … −15
If 0 ≤ E < H:  M = +5  × (H−E)/H                    # thin upside   → 0 … +5
If E < 0:      M = +5 + 10 × clamp((−E)/10pp, 0, 1) # expected loss → +5 … +15
```

The mapping is **deliberately asymmetric** to honour the Bounded choice: thin-but-positive upside adds at most +5 (cannot by itself move a held name from the 50–69.9 Hold band into the 70+ trim band), while a genuine expected *loss* reaches the full +15. That is what delivers "downside → trim/sell" without reopening the higher-turnover posture the 2026-06-07 change closed.

**Guardrails (because this is the most discretionary input in the score):**
- No catalyst within 18–24 months (Rule 10) → cap the upside side at −5; downside side unaffected.
- Always use the bull/base/bear PW Fair Value, never a single rosy point (Klarman — underwrite downside first).
- Show the full `E` calc and the mapping in every session log (operating-brief.md non-negotiable).
- Bounded ±15 by design — a modifier, not a veto, in both directions (mirrors the 2026-06-07 softening of the Rate Environment Gate Step 1 from a hard block to an additive flag).

**Alignment check (run per [investor-philosophy-alignment.md](../framework/investor-philosophy-alignment.md) before adopting):**

- **Price-action test:** PASS — driven by fair value and fundamentals, no chart/price-level trigger.
- **Turnover test:** PASS (by construction) — the asymmetric cap means only a genuine expected loss moves a held name toward trimming; modest upside cannot. Anti-turnover (Munger's "croupier's take," Terry Smith "do nothing") preserved.
- **Mean-reversion test:** PASS — improves on it. The pure backward-looking sub-scores were the source of the gap; this adds Marks' "what's different this time" forward dimension explicitly.
- **Macro-veto test:** PASS — bounded ±15, informs not vetoes.
- **Concentration test:** N/A — doesn't touch sizing/diversification.
- **Guidance test:** PARTIAL — flagged as a **conscious, bounded divergence**. The modifier injects forecast discretion (DCF/growth assumptions) into a score that was otherwise built on audited/observable inputs (Greenblatt's Magic-Formula discipline; the "Why Forward Guidance Is Not a Sub-score" principle). Mitigated, *not* eliminated, by: using the analyst's own scenario-weighted DCF rather than management's self-reported guidance; the ±15 bound; the catalyst requirement; and full show-your-work auditing. Recorded here explicitly (as with the 15% position-cap divergence) rather than left as an unflagged inconsistency. The supporting tenet is Buffett's "wonderful business at a *fair* price" — which the prior entry gate (cheap-only) contradicted in spirit; this change resolves that contradiction.

**Files touched:**
- `framework/valuation-scoring.md` — Final Score Formula updated; new "Upside/Downside Modifier" section (formula, mapping table, guardrails, worked example).
- `framework/strategy.md` — "Updated Valuation Score Weighting" table (new row); Phase 05 note on anti-turnover preservation.
- `framework/operating-brief.md` — calculation rules + Final Score line updated with the modifier.
- `framework/fair-value-methodology.md` — "Integration with Valuation Score" note; Order Setup Checklist lines for `E`, catalyst window, and the modifier.
- `framework/investor-philosophy-alignment.md` — conscious-divergence note added.
- `decisions/` — this file.

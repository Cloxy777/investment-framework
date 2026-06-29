# 2026-06-29 — Framework change: Quality Score, 80.0+ gate, and Composite Score added

**What prompted it:**

The user pointed out a real gap: Phase 01 ("quality gate") was a simple pass/fail screen, so any two companies that both cleared it looked identical to the framework — only the Phase 02 valuation score differentiated them. That meant a company trading slightly cheaper could win out over a company that is a much better business but a touch more expensive, even when the user would rather own the higher-quality name. The user wanted quality itself graded (not just pass/fail), the two numbers blended into one ranking, and a strict quality bar (80.0+) since "cheaper but much lower quality than another option" should not win.

**The decision (two user choices, asked before implementing):**

1. **Composite weighting → 50/50.** Quality and valuation are treated as equally important in the final ranking, rather than valuation dominating (40/60 was the alternative offered and declined).
2. **Quality sub-scores → reuse the existing Phase 01 categories as-is.** Profitability, Margins, Growth, Balance Sheet, Moat Signal, FCF Quality — graded instead of pass/fail, rather than collapsing into fewer categories.
3. **Gate threshold → 80.0+, strict by explicit instruction.** The user asked for a deliberately high bar, to be lowered later only if it screens out too much of the universe — not derived from any backtest, a conscious starting point.

**What was added:**

- **`framework/quality-scoring.md`** (new file) — full Quality Score methodology, mirroring the structure of `valuation-scoring.md`:
  - 6 weighted sub-scores: Profitability 25%, Margins 15%, Growth 20%, Balance Sheet 15%, Moat Signal 15%, FCF Quality 10% — each a continuous 0–100.0 formula derived from the existing Phase 01 thresholds.
  - Moat Signal is checklist-based (5 cited yes/no signals → score), since it has no single objective metric — explicitly requires documented evidence per signal rather than inventing a number.
  - The existing hard disqualifiers (FCF/NI <70% for 2+ years without explanation, balance sheet over threshold, not FCF-positive 3+ years) remain in force *on top of* the weighted score — a high average cannot launder past one of those failures.
  - **The 80.0+ gate**: below 80.0, a company does not proceed to Phase 02 at all, regardless of valuation.
- **`framework/valuation-scoring.md`** — new "Composite Score" section: `Composite = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score`, computed only for companies that cleared the 80.0+ gate. The `(100 − Quality)` inversion keeps the composite's orientation consistent with the existing valuation score and the Phase 03/05 action tables (0 = most attractive). Methodology version bumped 2026-06-20 → 2026-06-29.
- **`framework/strategy.md`** — Phase 01 now references the graded Quality Score and the 80.0+ gate explicitly; Phase 02 directs use of the Composite Score (not the raw valuation score) against the Phase 03/05 tables; weighting table gets a Quality Score row.
- **`framework/glossary.md`** — added **Quality Score** and **Composite Score** entries.
- **`watchlist/STALE.md`** — methodology version bumped to 2026-06-29; blanket note added flagging every numeric-scored watchlist entry as pending a Quality Score / Composite Score addition (not individually backfilled here — that requires sourced fundamentals per ticker, which is `/rescore`'s job, not a bulk edit without data; "never invent or estimate financial data" applies here too).

**Alignment check (per [investor-philosophy-alignment.md](../framework/investor-philosophy-alignment.md)):**

- **Price-action test:** PASS — entirely fundamentals-derived (margins, ROIC, growth, balance sheet, moat evidence), no chart/price trigger.
- **Turnover test:** N/A — this changes eligibility and ranking, not trim/exit cadence; Phase 05's anti-turnover rules are untouched.
- **Mean-reversion test:** N/A.
- **Macro-veto test:** N/A.
- **Concentration test:** N/A — doesn't touch position sizing/diversification mechanics directly (the action tables it feeds are unchanged).
- **Guidance test:** PASS — Moat Signal and the TAM/pricing-power growth modifier require *cited* evidence (filings, third-party reports), not management's self-reported guidance; consistent with "never invent or estimate financial data."

This is squarely aligned with Buffett/Munger's "a wonderful company at a fair price beats a fair company at a wonderful price" — the prior pass/fail gate gave no way to express *how much* better one wonderful company is than another when ranking against valuation.

**Open item:** every existing watchlist entry (all current holdings + previously-scored not-in-portfolio names) now needs a Quality Score and Composite Score computed before it's fully current under this version — to be done incrementally as `/rescore` and `/new-position` touch each ticker, per the existing stale-score mechanism.

**Files touched:**
- `framework/quality-scoring.md` (new)
- `framework/valuation-scoring.md`
- `framework/strategy.md`
- `framework/glossary.md`
- `watchlist/STALE.md`
- `decisions/` — this file.

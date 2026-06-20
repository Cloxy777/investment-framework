# 2026-06-20 — Framework change: guidance discipline check added, quantitative guidance sub-score rejected

**What changed:**

The user asked whether the valuation score should have a dedicated sub-score for management's forward guidance (the company's own prediction of next quarter's/year's results), after a prior session noted this as a gap. Ran it through the [investor-philosophy-alignment.md](../framework/investor-philosophy-alignment.md) checklist before deciding:

- **Buffett:** publicly campaigned (with JPMorgan's Jamie Dimon, 2018 WSJ op-ed) to end quarterly EPS guidance altogether, on the grounds it pressures management toward short-term earnings smoothing.
- **Greenblatt:** the Magic Formula deliberately scores only audited, filed-financials inputs (Return on Capital, Earnings Yield) — no self-reported number gets a vote.
- **Munger:** "show me the incentive and I'll show you the outcome" — guidance is a number management has both the means and the incentive to manage.
- **Lynch:** treats forward outlook as part of the qualitative "story" to verify, not a number to plug into a formula.
- **Marks:** "second-level thinking" — take consensus/guidance as something to interrogate, not as ground truth.

All five point the same direction: guidance is not the kind of audited, hard-to-manipulate input the four existing weighted sub-scores (FCF Yield, EV/EBIT, Forward PE, PEG) are built from. Adding it as a fifth weighted score would reopen exactly the self-reported-number risk that the FCF/Net Income conversion check (Valeant, Wirecard) was built to close.

**What was added instead** — guidance as a *trigger*, not a *score*:
- `framework/strategy.md` Phase 04: new **Guidance discipline check** — track guidance delivered vs. promised each quarter; 2+ consecutive cuts without a one-off cause (FX, one-time charge) escalates to a Growth-thesis-broken candidate under Phase 06, independent of the valuation score.
- `framework/strategy.md` Phase 06: "Growth thesis broken" valid-exit bullet now explicitly names the guidance-cut pattern; added a symmetric NOT-valid bullet so a single guidance cut with a clear one-off cause isn't an overreaction trigger (mirrors the existing "short-term earnings miss" exclusion).
- `framework/valuation-scoring.md`: new "Why Forward Guidance Is Not a Sub-score" section explaining the exclusion and pointing to the existing Rule 9 (mandatory re-valuation on guidance revision) as where guidance actually plugs into the system.
- `framework/investor-philosophy-alignment.md`: added the guidance-skepticism tenets to Buffett and Greenblatt's bullet lists, plus a 6th **Guidance test** item in the "Quick alignment check" so future rule changes get checked against this reasoning too.

**Why not just add it as a 5th weighted input anyway:**

Every other input in the score is verifiable against a filing or a market price. Guidance is the one number in the entire pipeline that the subject company writes itself — scoring it quantitatively would weight the model toward whoever manages their guidance best, not whoever runs the best business. The credibility *pattern* (does this management's guidance track reality over time) is a legitimate signal — which is what the new Phase 04 check captures — but the raw guidance number itself is not.

**Files touched:**
- `framework/strategy.md` — Phase 04 (new bullet), Phase 06 (edited valid + NOT-valid bullets)
- `framework/valuation-scoring.md` — new section after the Final Score Formula
- `framework/investor-philosophy-alignment.md` — Buffett/Greenblatt bullets, new alignment-check item 6

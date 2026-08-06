# 2026-08-05 — Framework clarification: the FCF-positivity hard disqualifier is a rolling window, not a permanent scar

**What prompted it:**

SNDK's 2026-07-15 `/new-position` session failed the Quality Score gate on two independent grounds: a weighted score of 51.3 (well below 80.0), and the hard disqualifier "not FCF-positive for 3+ consecutive years" firing on FY2023 (−$932M), FY2024 (−$475M), FY2025 (−$120M) — three straight FCF-negative fiscal years immediately following SanDisk's spin-off from Western Digital. That session's own "Next review trigger" section stated the disqualifier "cannot mechanically resolve before the FY2028 10-K at the earliest (assuming the current NAND pricing supercycle persists that long)" — reading the rule as requiring a *fresh 3-consecutive-positive-year streak* to ever clear it.

SanDisk's FY2026 10-K-equivalent results (8-K/Exhibit 99.1, filed 2026-08-05) reported FY2026 FCF of **+$11,494M** — a dramatic, complete-fiscal-year reversal (not a single hot quarter) driven by a genuine NAND pricing supercycle. This session (2026-08-05 `/new-position` re-run, triggered by that same earnings print) needed to determine, for the first time under live data, what "the correct rolling 3-year window" actually means once a new fiscal year prints after a disqualifying streak.

**The ambiguity:**

`quality-scoring.md`'s literal text — "Not FCF-positive for 3+ consecutive years" — supports two readings:

1. **Permanent-scar / streak-must-be-replaced reading** (the 2026-07-15 session's implicit assumption): once a 3-consecutive-negative-year streak has fired the disqualifier, it stays fired until a *fresh* run of 3 consecutive *positive* years exists to replace it. Under this reading, FY2026 alone doesn't clear anything — resolution requires FY2026, FY2027, *and* FY2028 to all be positive.
2. **Rolling-window reading** (adopted here): the condition is tested fresh each session against the **current** most-recently-completed 3 fiscal years. If that window is no longer uniformly negative, the disqualifier does not fire this session — even though an *older* window (FY2023–FY2025) was uniformly negative.

**The ruling:** reading 2 (rolling window) is adopted, for three reasons:

- **Structural parallel to the sibling disqualifier.** The FCF/NI conversion disqualifier ("<70% for 2+ consecutive years") is already applied this way — the MELI 2026-08-05 session explicitly reasoned "this is a TTM-rolling-window comparison, not two distinct fiscal years, so the '2+ consecutive years' hard-disqualifier language is not triggered on its own terms," re-testing fresh each session rather than treating a past dip as a permanent mark. Reading the two disqualifiers inconsistently — one rolling, one a permanent scar — has no textual basis in `quality-scoring.md`, which uses parallel "N+ consecutive years" phrasing for both.
- **Consistency with every other metric in the framework.** 3yr revenue CAGR, TTM ratios, and Net Debt/EBITDA are all evaluated on the current trailing window, refreshed as new fiscal years/quarters report — never as a cumulative all-time check. A permanent-scar reading would make this one disqualifier the sole exception to that convention, with no stated rationale for the inconsistency.
- **The permanent-scar reading produces an indefensible edge case.** Taken literally, any company with *any* 3-consecutive-year bad patch anywhere in its history — even a decade-old one, even one followed by 15 years of strong performance — would be permanently and irrecoverably disqualified. That is a materially different (and more punitive) rule than what the plain disqualifier language states, and is not how any other "N+ consecutive years" check in this framework works.

**What this does *not* do:** it does not make the disqualifier toothless. A single strong quarter still cannot clear it — the test still requires the **entire most-recently-completed fiscal year** to be genuinely positive, and the window still contains 2 of the 3 most recent years negative (FY2024, FY2025) alongside the 1 positive year (FY2026) — so a single bad year in FY2027 would put the disqualifier back in play (FY2025–FY2027 would again be checked fresh). The protection against "one hot quarter masking chronic burn" is preserved; the protection against "one hot *year* is permanently disqualifying regardless of how strong or complete it is" is removed, which is the part of the prior reading this clarification rejects.

**Alignment check ([investor-philosophy-alignment.md](../framework/investor-philosophy-alignment.md)):**
- **Greenblatt / "never invent or estimate financial data":** both readings use only real, filed FY2026 figures — this is a scoring-rule interpretation question, not a data-quality one.
- **Klarman ("downside always underwritten"):** the rolling-window reading is not adopted as pure leniency — see the Upside/Downside Modifier and R/R gate in the same session's order setup, which independently blocked any actual SNDK entry regardless of the Quality Score gate's outcome. The practical, capital-at-risk consequence of this clarification was nil in the case that prompted it.
- **Munger ("invert, always invert"):** the permanent-scar reading, inverted, implies no company could ever recover from a 3-year rough patch under this framework, no matter how completely or durably. That is a stronger and stranger claim than "sustained quality requires sustained cash generation" (the disqualifier's own stated rationale) was ever meant to assert.

**Impact:**

- SNDK's 2026-08-05 `/new-position` re-run applies this rolling-window reading: the FY2024–FY2026 window is not uniformly negative (FY2026 is positive), so the disqualifier does not fire this session. Full computation, and the alternative (permanent-scar) reading's resulting Quality Score, are both shown side-by-side in [sessions/2026-08-05-new-position-sndk.md](../sessions/2026-08-05-new-position-sndk.md) for transparency.
- No other watchlist entry in this repo currently carries a live "not FCF-positive for 3+ consecutive years" disqualifier flag, so no other ticker's recorded score changes as a result of this clarification.

**Files touched:**
- `framework/quality-scoring.md` — added the rolling-window clarification note under the Hard Disqualifiers section.
- `sessions/2026-08-05-new-position-sndk.md` — full worked application, both readings shown.
- `watchlist/not-in-portfolio/SNDK/SNDK-2026-08-05.md` — updated entry reflecting the ruling.
- `decisions/` — this file.

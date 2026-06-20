# 2026-06-20 — Framework change: decode jargon on first use instead of a glossary block

**What changed:**

Added a communication-style rule to [operating-brief.md](../framework/operating-brief.md) (ROLE & HARD CONSTRAINTS) and a one-line pointer to it in [CLAUDE.md](../CLAUDE.md): the first time a financial jargon term, abbreviation, or unit shorthand (e.g. FCF/NI, TAM, ROIC, EV/EBIT, pp, bps, MoS, WACC, DCF) appears in any output, expand it in plain English in parentheses on that first use only. Applies to chat responses, session logs, decision logs, and GitHub PR descriptions/comments — anywhere the human investor reads output.

**Why:**

The user flagged that responses assumed finance fluency (FCF/NI, TAM, ">3pp") they don't have memorized. Two options were considered: (1) a glossary block appended at the end of every output, or (2) inline parenthetical expansion the first time each term appears in the body.

Chose inline-first-use over a glossary because it wins on both criteria the user asked to optimize for:
- **Readability:** the definition sits next to the term where it's needed, instead of requiring a scroll-down-and-match-back exercise for a reader who doesn't already know which terms to look up.
- **Token cost:** a term used once costs the same either way; a term used multiple times in one output is *cheaper* inline (defined once, used bare afterward) than in a glossary, which still has to enumerate every distinct term used plus a heading regardless of frequency.

**What stays the same (intentionally):**

- No change to any scoring, valuation, or trim/exit logic — this is a communication-style rule only.
- "Show every calculation" (CLAUDE.md, operating-brief.md) is unaffected — full sub-scores and modifiers are still always shown, just with jargon decoded alongside them.

**Files touched:**
- `framework/operating-brief.md` — new bullet under ROLE & HARD CONSTRAINTS
- `CLAUDE.md` — new bullet under "How to behave in analysis sessions"

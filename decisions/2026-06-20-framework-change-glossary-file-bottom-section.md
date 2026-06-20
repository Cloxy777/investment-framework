# 2026-06-20 — Framework change: switch jargon decoding from inline first-use to a glossary.md file + closing Glossary section

**What changed:**

Reverses the approach adopted earlier today in [2026-06-20-framework-change-plain-language-glossary.md](2026-06-20-framework-change-plain-language-glossary.md) (PR #35). That change asked Claude to expand jargon inline, in parentheses, the first time each term appeared in an output's body. The user reported it wasn't actually happening in subsequent sessions.

New mechanism:
- [framework/glossary.md](../framework/glossary.md) — a standing, growing reference of plain-English definitions, split into general financial/valuation terms and this framework's own vocabulary (e.g. Rate Environment Gate, Hybrid Upgrade, Turnaround Sub-Gate).
- [operating-brief.md](../framework/operating-brief.md) ROLE & HARD CONSTRAINTS and OUTPUT FORMAT (new step 9): every output — chat response, session log, decision log, PR description — ends with a "Glossary" section listing the terms *that output actually used*, defined from glossary.md. Terms not yet in glossary.md get added there first, then cited.
- `CLAUDE.md`: orientation list now points to glossary.md, and the "decode jargon" bullet under "How to behave in analysis sessions" was updated to describe the closing-section mechanism instead of inline expansion.

**Why:**

Inline first-use expansion asks Claude to track, mid-generation, which terms have already been defined somewhere earlier in a long, structured output (8-step OUTPUT FORMAT: header, data gaps, gate results, full score calc, action, order setup, rebalancing summary, next trigger) — an easy rule to silently drop, and apparently one that was getting dropped. A fixed, numbered closing step ("step 9: Glossary") is mechanical rather than a prose reminder to remember partway through: it's the same kind of structural enforcement the OUTPUT FORMAT checklist already uses for "show every calculation," and it's checkable after the fact (a response missing a Glossary section is visibly incomplete, the way one missing a score calculation would be).

A standalone glossary.md file also gives the definitions a single canonical source that accumulates over sessions (rather than being re-derived/rephrased ad hoc each time a term is expanded inline), and a place to fix or extend a definition once for every future session.

The token-cost tradeoff noted in the prior decision (glossary block pays for a heading + enumeration regardless of frequency) is accepted here in exchange for actually working.

**What stays the same (intentionally):**

- No change to any scoring, valuation, or trim/exit logic — still a communication-style rule only.
- "Show every calculation" is unaffected.
- The underlying intent (user is not a finance professional, every jargon term gets a plain-English definition) is unchanged — only the mechanism moved from inline-per-term to a sourced closing section.

**Files touched:**
- `framework/glossary.md` — new file
- `framework/operating-brief.md` — ROLE & HARD CONSTRAINTS bullet rewritten; OUTPUT FORMAT step 9 added
- `CLAUDE.md` — orientation list entry added; "decode jargon" bullet rewritten

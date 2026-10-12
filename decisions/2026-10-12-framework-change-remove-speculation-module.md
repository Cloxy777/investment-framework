# 2026-10-12 — Framework change: Speculation Module removed

**What prompted it:**

User reviewed the framework at a high level and, after discussing whether the sleeve should be widened (Quality 60–80, extreme valuations), decided to remove it entirely. Facts on record at the time:

- The module (added 2026-07-01, operationalized 2026-07-04 with `/speculate`) had **zero trades** in [speculation-log.md](../portfolio/speculation-log.md) after ~3 months; its only evaluation (META, 2026-07-01) failed three gates.
- The gates (Quality 80+, documented catalyst, per-trade cap of ~1% of portfolio) were strict enough that the sleeve rarely, if ever, fires; loosening them risked recreating the override leak the sleeve was built to contain.
- Short-horizon trading cuts against the core philosophy (it knowingly failed the price-action and turnover tests in [investor-philosophy-alignment.md](../framework/investor-philosophy-alignment.md)).

**The decision:** remove the module. Core framework (Phases 01–06) and the override log are unchanged and remain the only outlets/records for off-framework positions.

**Removed:**
- `framework/speculation-module.md`
- `framework/speculation-strategies.md`
- `portfolio/speculation-log.md`
- `.claude/commands/speculate.md` (`/speculate`)

**Edited:**
- `CLAUDE.md` — orientation entries, `portfolio/` description and `/speculate` command line removed.
- `framework/investor-philosophy-alignment.md` — "Conscious divergence" note for the Speculation Module removed.
- `framework/glossary.md` — speculation-only sections and rows removed (barbell, core-satellite, expectancy, house money, mad money, time-stop, ADX/ATR/Bollinger/Donchian/PEAD/RSI/RVOL/momentum/MA/support-resistance); generic behavioral terms (disposition effect, mental accounting, turnover) and the RSU row kept; speculation-module wording dropped from the IV and ATM straddle rows.

**Deliberately left alone:**
- Historical records (`sessions/`, `decisions/2026-07-01…`, `decisions/2026-07-04…`, `watchlist/` entries) that mention the module — they are the audit trail and stay as written. Links from them into the removed files now resolve only in git history (commit before this one).
- The core "Speculative / pre-profit" special category in `fair-value-methodology.md` and `scripts/scoring/order_setup.py` — a different concept (position sizing for pre-profit companies), unrelated to the sleeve.
- Monitored-channel text in `telegram-watch.md` using the word "speculation".

**Revival:** `git show <commit-before-this>:framework/speculation-module.md` (and the other removed files) restores the full design if wanted later.

## Glossary
- **Speculation sleeve:** the small, separate bucket (5% of portfolio) for short-term trades that this change removes.
- **Override log:** the record of every position entered outside the framework's rules; still active.
- **Special category (Speculative / pre-profit):** the core framework's sizing treatment for pre-profit companies; unrelated to the removed sleeve.

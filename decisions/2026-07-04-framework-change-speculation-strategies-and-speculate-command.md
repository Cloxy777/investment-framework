# 2026-07-04 — Framework change: Speculation Strategies playbook + `/speculate` command added

**What prompted it:**

The 2026-07-01 [Speculation Module](../framework/speculation-module.md) defined the sleeve's *risk rules* (eligibility gate, caps, sizing, exit discipline) but explicitly left "which strategy, and why" and the command itself as open items — its closing note said to wait until the numeric defaults were confirmed and the module had run a few real trades. The user asked directly to operationalize it now: research proven short-horizon strategies/techniques and the criteria for choosing between them, add a `/speculate <TICKER>` command that pulls live price/options/news data, picks a strategy, computes levels, and produces an IBKR order recommendation. This proceeds ahead of the originally suggested sequencing, at explicit user request — noted here rather than silently overridden.

**The decision:**

1. **A separate strategies file, not new module rules.** [speculation-strategies.md](../framework/speculation-strategies.md) holds the strategy menu and regime-classification method; it explicitly never overrides any number in speculation-module.md (caps, stop bands, time-stop, minimum R/R) — it only picks direction, instrument, and price levels once the module's own gates (Rule 1 eligibility, Rule 6 catalyst) already passed.
2. **Evidence-graded, "proven only" curation.** Every technique is tagged **Academic** (a cited, peer-reviewed, replicated factor/anomaly) or **Practitioner-established** (long-documented professional use for timing/risk-framing, weaker standalone evidence — used only as a filter or level-setting tool, never alone). Chart-pattern reading, Fibonacci levels, Elliott Wave, and candlestick-pattern naming were deliberately excluded — none has robust out-of-sample predictive evidence, and the user asked for proven techniques only.
3. **Four strategies, one regime-classification layer, three level-setting techniques:**
   - Momentum/Donchian Breakout (Jegadeesh & Titman 1993 momentum factor + the Turtle Trading entry rule)
   - Post-Earnings Announcement Drift / PEAD (Bernard & Thomas 1989)
   - Catalyst Binary Event — defined-risk long option (practitioner-standard, reuses the module's own Rule 7/8 IV methodology)
   - Oversold Mean-Reversion Bounce (weaker, mixed evidence — deliberately the narrowest-scoped entry, shares only, still requires a Rule 6 catalyst)
   - Regime classification: trend (SMA50/200 + ADX14), volatility (IV percentile vs. historical vol, read directly from live snapshot fields rather than recomputed), participation (Relative Volume)
   - Level-setting: Rule 7's expected move (unchanged), ATR-based stop distance (refines, never overrides, Rule 8's 15–20% band), Donchian/52-week support-resistance for targets
4. **Instrument constraint carried through unchanged.** Every strategy maps only to shares (long) or a single long call/put, per the module's existing Rule 8/9 wording — no short shares, no multi-leg spreads, no margin. A long straddle for genuinely two-sided binary events was considered (B3) but flagged as *not currently authorized* rather than assumed — Rule 8's "long calls/puts" wording doesn't clearly cover buying both legs, and that's a call for the user to make, not this session.
5. **`/speculate` reads the module's numbers live, never hardcodes them.** Since Rules 2–3's percentages are themselves flagged "proposed, not yet confirmed," the command is written to read those values out of speculation-module.md at run time so it can't silently go stale if the user changes them later.
6. **No order-submission capability exists or was added.** Checked directly: this environment's IBKR MCP connection exposes `get_order_instructions` (read-only, lists saved instructions) but no order-creation/submission tool. `/speculate`'s final step produces a human-readable order ticket only, explicitly labeled as a recommendation the user enters themselves — consistent with the existing repo-wide rule (see telegram-scan.md) that no routine ever submits or modifies a broker order.

**What was added:**

- **`framework/speculation-strategies.md`** (new) — the strategy/technique playbook described above.
- **`.claude/commands/speculate.md`** (new) — the `/speculate <TICKER>` command: Rule 1 gate → live data pull → news/catalyst scan (with a hard stop for user confirmation of the catalyst) → regime classification → strategy selection → levels → position sizing against live-read caps → gate summary → IBKR order recommendation → session log + speculation-log.md update.
- **`framework/speculation-module.md`** — added a cross-reference section ("Strategy & instrument selection," between Rules 6 and 7, deliberately not renumbering existing rules since several other files cite them by number) pointing to the new strategies file, and closed the "no slash command yet" open item.
- **`framework/glossary.md`** — added a "Technical-analysis & speculation-strategy terms" section: ADX, ATR, Bollinger Bands, Donchian Channel, momentum factor, moving average (SMA/EMA), PEAD, RSI, RVOL, support/resistance.
- **`CLAUDE.md`** — added speculation-strategies.md to the Orientation list and `/speculate` to the routine-tasks list.

**Alignment check:** this operationalizes the divergence already recorded and accepted in the [2026-07-01 decision](2026-07-01-framework-change-speculation-module.md) (the sleeve knowingly fails the core framework's price-action and turnover tests, by deliberate design, bounded by caps). Nothing here widens that divergence — the strategies file governs *within* the already-fenced sleeve, and every instrument/sizing/exit constraint from the original module carries through unchanged.

**Open items (carried forward, not resolved by this change):**

- Bucket cap (5%), per-trade cap (20% of sleeve), and default time-stop (90 days) in speculation-module.md are still proposed defaults pending the user's confirmation.
- Whether to authorize a long straddle for two-sided binary events (flagged under Strategy B3) is an open question for the user, not decided here.
- The ADX/RSI/ATR thresholds in speculation-strategies.md are standard textbook (Wilder) defaults, not back-tested against any specific universe — flagged as a starting point to revisit once the sleeve has real trade history.

**Files touched:**
- `framework/speculation-strategies.md` (new)
- `.claude/commands/speculate.md` (new)
- `framework/speculation-module.md`
- `framework/glossary.md`
- `CLAUDE.md`
- `decisions/` — this file.

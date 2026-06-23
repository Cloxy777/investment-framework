# 2026-06-22 — Rebalance Session

**Task type:** REBALANCE
**Scope:** Portfolio-wide trim/hold/exit review across all rows in [holdings.md](../portfolio/holdings.md) (combined total ≈ **$55,813.07**), applying Phase 05 (Dynamic Trimming) and Phase 06 (Exit Triggers) from [strategy.md](../framework/strategy.md) to the **current 0.0–100.0 scores** (the bulk of the book was rescored 2026-06-20 under the new Upside/Downside Modifier), plus the Upgrade 7 15% single-position cap and an Upgrade 4 Turnaround Sub-Gate review-due check. This is the third monthly run of Routine 5 ([decisions/2026-06-13-automation-routine-schedule.md](../decisions/2026-06-13-automation-routine-schedule.md)), following [2026-06-07](2026-06-07-rebalance.md) and [2026-06-15](2026-06-15-rebalance.md).

**No trades executed. This is a proposal for human review only.**

---

## 1. Holdings pull & staleness check

Source: [holdings.md](../portfolio/holdings.md), live-synced 2026-06-22 from IBKR (full sync) + Freedom24 (unchanged since 2026-06-07). Per [sessions/weekly-briefs/2026-06-22-weekly-brief.md](weekly-briefs/2026-06-22-weekly-brief.md) §2, **no earnings occurred in the 7 days to 2026-06-22**, and 21 of 22 scored equities were rescored just two days ago (2026-06-20) under the Upside/Downside Modifier. Nearest upcoming earnings is NKE (2026-06-30) — outside this window. **No holding is stale by the earnings-based criterion in [operating-calendar.md](../framework/operating-calendar.md).**

| Ticker | Weight % | USD value | Score | Last Review | Band (Phase 03/05) |
|---|---|---|---|---|---|
| ADBE | 3.50% | $1,951.20 | 0.0 | 20 Jun 2026 | 0.0–29.9 Very Cheap |
| AMZN | 10.03% | $5,597.46 | 73.4 | 20 Jun 2026 | 70.0–79.9 Expensive |
| AVGO | 4.35% | $2,427.18 | 69.5 (**stale**) | 14 Jun 2026 | predates 2026-06-20 modifier — see §7 |
| CSGP | 1.35% | $750.50 | 79.0 | 20 Jun 2026 | 70.0–79.9 Expensive |
| DUOL | 8.26% | $4,609.84 | 53.7 | 20 Jun 2026 | 50.0–69.9 Fair Value |
| GOOG | 0.65% | $361.39 | 73.1 | 20 Jun 2026 | 70.0–79.9 Expensive |
| META | 7.22% | $4,028.85 | 19.6 | 20 Jun 2026 | 0.0–29.9 Very Cheap |
| MSFT | 15.01% | $8,375.60 | 35.0 | 20 Jun 2026 | 30.0–49.9 Cheap |
| NFLX | 1.66% | $924.00 | 61.2 | 20 Jun 2026 | 50.0–69.9 Fair Value |
| NKE | 1.61% | $900.20 | 43.1 | 20 Jun 2026 | 30.0–49.9 Cheap (override) |
| NOW | 2.02% | $1,128.00 | 42.3 | 20 Jun 2026 | 30.0–49.9 Cheap |
| NVDA | 5.23% | $2,920.54 | 48.5 | 20 Jun 2026 | 30.0–49.9 Cheap |
| NVO | 0.40% | $221.15 | 47.6 | 20 Jun 2026 | 30.0–49.9 Cheap — thesis flag resolved (see §7) |
| RBRK | 0.38% | $210.00 | not scored | Jun 2026 | special — see §7 |
| SPGI | 0.74% | $412.76 | 33.4 | 20 Jun 2026 | 30.0–49.9 Cheap |
| SPOT | 0.84% | $468.08 | 80.5 | 20 Jun 2026 | 80.0–89.9 Very Expensive |
| STIM | 0.76% | $424.35 | not scored | Jun 2026 | special — see §7 |
| TLT | 29.91% | $16,698.71 | not scored | Jun 2026 | special — see §4 |
| UBER | 0.38% | $213.96 | 34.8 | 20 Jun 2026 | 30.0–49.9 Cheap |
| V | 0.59% | $327.24 | 39.2 | 20 Jun 2026 | 30.0–49.9 Cheap |
| VEEV | 0.83% | $460.50 | **blank** | **blank** | needs `/rescore` — see §7 |
| XEON | 3.07% | $1,714.19 | not scored | Jun 2026 | out of scope |
| ZS | 0.22% | $124.25 | 36.3 | 20 Jun 2026 | 30.0–49.9 Cheap |
| CASH (IBKR) | 0.46% | $255.99 | — | — | liquidity |
| CASH (Freedom24) | 0.19% | $106.85 | — | — | liquidity |

**Live-price drift check:** AMZN, CSGP, GOOG, and SPOT sit closest to Phase 05 band edges. Comparing the 2026-06-20 rescore prices against today's live IBKR snapshot: CSGP $30.12→$30.02 (flat), SPOT $468.08→$468.08 (identical), AMZN $244.39→$241.23 (−1.3%), GOOG $367.46→$361.39 (−1.65%). None of this drift is large enough to flip any of the four across a band boundary, and the 2026-06-20 scores are only two days old and were themselves sourced from live Rule-0 prices. **Unlike last month, this session does not carry a "refresh before executing" caveat** for the trims below.

**Flag — AVGO is the one exception to "current":** AVGO's 69.5 score is from the 2026-06-14 new-position session, two days before the 2026-06-20 Upside/Downside Modifier went in. See §7 for the data-integrity note (it also contradicts `watchlist/STALE.md`'s own claim).

**Flag — needs `/rescore`:** **VEEV** (3 sh, $460.50, 0.83%) still carries no score and no `Last Review` date — second consecutive month flagged (first in [2026-06-15 rebalance](2026-06-15-rebalance.md) §1). No entry session exists for it in `sessions/` or `decisions/`.

---

## 2. Phase 05 — Dynamic Trimming (applied to current scores)

### Trim 25–30% (Score 70.0–79.9)

| Ticker | Score | Value | 25% | 30% | Reasoning |
|---|---|---|---|---|---|
| **AMZN** | 73.4 | $5,597.46 (12 sh IBKR @ $241.23 + 11 sh Freedom24, 23 sh total) | $1,399.37 | $1,679.24 | "Expensive" band, pure valuation-driven trim, no fundamental break. In whole shares from the IBKR leg: 25% ≈ 5.75 sh → **6 sh** ($1,447.38, 25.85% of position value); 30% ≈ 6.9 sh → **7 sh** ($1,688.61, 30.16%). Recommend trimming the IBKR leg only (live-executable via MCP); Freedom24's 11 sh are screenshot-only. |
| **CSGP** | 79.0 | $750.50 (25 sh, IBKR) | $187.63 | $225.15 | "Expensive" — still in the 25–30% band, not the 80s (moved 83.3→79.0 on the 2026-06-20 rescore, the opposite direction of last month's recompute-driven move into the 80s). In whole shares: 25% = 6.25 sh → **6 sh** ($180.12, 24%); 30% = 7.5 sh → **8 sh** ($240.16, 32%, the closer whole-share fit). |
| **GOOG** | 73.1 | $361.39 (1 sh, IBKR) | $90.35 | $108.42 | "Expensive." **Not executable**: 1 share cannot be partially trimmed. See execution-mechanics note below. |

### Trim to 50% (Score 80.0–89.9)

| Ticker | Score | Value | Trim to 50% | Reasoning |
|---|---|---|---|---|
| **SPOT** | 80.5 | $468.08 (1 sh, IBKR) | $234.04 | "Very Expensive" — the one name that moved *into* this deeper band this cycle (was 82.0 last month, now 80.5, still ≥80.0). **Not executable**: 1 share cannot be halved. See execution-mechanics note below. |

### Trim to tracking (1–2%) — Score 90.0–100.0

None. No holding scores ≥90.0.

**⚠️ Execution-mechanics note — GOOG & SPOT:** both are single-share IBKR positions where the indicated trim cannot be executed in whole shares — the same structural tension flagged in both prior rebalances. Both already carry standing GTC sell-limit orders **above** current market: GOOG SELL 1 @ $389.00 (current $361.39) and SPOT SELL 1 @ $518.00 (current $468.08). If either fills, the result is a 100% exit, more aggressive than the trim trigger calls for. Flagging for awareness only — no change to standing orders recommended (an execution-mechanics judgment call, not a valuation one).

---

## 3. Phase 06 — Full Exit Triggers

**None fired on valuation grounds.** No holding is in the 90.0–100.0 band this month, let alone for the 2+ consecutive quarters Phase 06 requires for a valuation-driven exit.

No new fundamental-deterioration, thesis-broken, or balance-sheet-crisis triggers identified **from this session's inputs**. STIM and RBRK carry pre-existing, carried-forward exit-review flags from fundamentals (not from this session — see §7), now in their **third consecutive month** unaddressed.

---

## 4. Upgrade 7 — 15% Single-Position Cap Check

15% of $55,813.07 = **$8,371.96**.

| Ticker | Weight | Value | Breach? | Action required |
|---|---|---|---|---|
| **MSFT** | 15.01% | $8,375.60 (20 sh IBKR @ $377.53 = $7,550.60 + 2 sh Freedom24 ≈ $825.00) | **Yes — by $3.64** | This breach has shrunk sharply from last month's $674.73 (the 2026-06-20 rescore put MSFT in the Cheap band at 35.0, so there's no valuation trim trigger either way). $3.64 is below the value of even one IBKR share ($377.53) — trimming the smallest possible unit (1 sh) would overshoot to $7,998.07 / 14.33%, a 0.68pp overcorrection for a breach worth 0.007pp. Given the position is also sitting inside the broker's own ~$200 NLV-vs-gross-position-value timing noise (see [ibkr.md](../portfolio/snapshots/ibkr.md)), this reads as data-precision noise rather than an actionable concentration breach. **No trim recommended this cycle; flag for re-check next sync** rather than force a whole-share trim that materially overshoots the target. |
| **TLT** | 29.91% | $16,698.71 (77 sh IBKR + 118 sh Freedom24) | **Yes — by $8,326.75** | **No new finding — third consecutive month carried forward** (2026-06-07, 2026-06-15, now 2026-06-22). Still the same structural gap logged in [override-log.md](../portfolio/override-log.md) ("No exit criteria defined / Define exit rules or divest"); more than half the position would need to move to clear the cap, and the framework still has no fixed-income valuation/sizing methodology. See §7 — recommend this graduate from a routine carry-forward line to a dedicated framework-development session given the recurrence count. |
| All others | ≤ 10.03% | — | No | — |

---

## 5. Recycling Plan

Per Phase 05 — "proceeds always reinvested into current Score 0.0–29.9 names only." Two held names now sit in that band: **ADBE (0.0)** and, newly since 2026-06-20, **META (19.6)**.

**META has zero executable headroom.** META's combined value is $4,028.85 (7.22% of $55,813.07). Its own Phase 03 sizing ceiling for a Very Cheap score is 6–8% of the book; 8% = $4,465.05, leaving only **$436.20** of room — less than the cost of a single additional IBKR share at $573.20. [sessions/2026-06-20-rescore-meta.md](2026-06-20-rescore-meta.md) flagged this directly: META "is already at the top of (indeed at) the 6-8% full-position band." **META is not a usable recycling destination this cycle**, despite qualifying on score alone — a useful distinction to keep making explicit, since "Score 0.0–29.9" and "has room to add" are not the same test.

**ADBE remains the only practically executable destination.** ADBE sits at 3.50% vs. its documented ~17-share / ~8% target ([2026-06-12 new-position session](2026-06-12-new-position-adbe.md)): 10 of ~17 target shares filled, **7 shares (= $1,365.84 at the current $195.12 price) remain** to reach target.

### Proceeds available (using whole-share-executable trims only; MSFT excluded per §4)

| Source | Amount | Driver |
|---|---|---|
| AMZN trim (6–7 sh, IBKR) | $1,447.38 – $1,688.61 | Phase 05 (valuation) |
| CSGP trim (6–8 sh, IBKR) | $180.12 – $240.16 | Phase 05 (valuation) |
| **Subtotal** | **$1,627.50 – $1,928.77** | |
| GOOG / SPOT (illustrative, not executable — §2) | +$90.35 / +$234.04 | Phase 05 (valuation) |

### Allocation

1. **First $1,365.84 → ADBE**, completing the documented ~17-share target (10 → 17 sh). Already-documented, unambiguous use of proceeds.
2. **Remainder (~$262 – $563, before GOOG/SPOT) → cash**, joining the existing combined cash position (CASH IBKR $255.99 + CASH Freedom24 $106.85 = $362.84, 0.65% combined). Projected combined cash after this allocation: **≈$625 – $926**, roughly **1.1%–1.7%** of the $55,813.07 total. No Cheap-band name (30.0–49.9 — NKE, NVO, NOW, NVDA, SPGI, UBER, V, ZS) qualifies as a Phase 05 destination; recycling into one would itself be an undocumented-trigger override.

**Note — PDD still not a confirmed destination.** [watchlist/STALE.md](../watchlist/STALE.md) lists PDD at a stale score of 5.0 (Very Cheap), scored 2026-06-14, flagged stale 2026-06-20 (pre-modifier) — and PDD still does not appear in `holdings.md`, so it isn't held. Even if it were, the score predates the current methodology and would need a fresh `/rescore` before counting as a recycling destination. Carried forward from the 2026-06-15 session, unchanged.

---

## 6. Upgrade 4 — Turnaround Sub-Gate Review Check

Searched [override-log.md](../portfolio/override-log.md) and `decisions/` for any position **entered** under the Turnaround Sub-Gate ("Conditional Watch, 2–3% max," mandatory 2-quarter review).

**Result: none found** — same conclusion as both prior months. The Override Log table in `override-log.md` carries exactly one entry (AVGO, 2026-06-16, a *valuation* override, not a Turnaround Sub-Gate entry — see §7). No `decisions/` entry records a Turnaround Sub-Gate entry; a targeted grep of `decisions/` for "Turnaround"/"Upgrade 4" returns only unrelated automation/glossary decision files.

Two holdings remain **evaluated against** Upgrade 4's criteria without being formally entered under it:
- **NKE** ([watchlist/in-portfolio/NKE/NKE-2026-06-20.md](../watchlist/in-portfolio/NKE/NKE-2026-06-20.md)) — 1 of 5 Upgrade 4 conditions met (insider buying reported); ROIC ~11% TTM still fails the Phase 01 >15% gate. Still only a "candidate," never a formal entry.
- **RBRK** — explicitly fails the Upgrade 4 Turnaround Sub-Gate (IPO 2024, no profitability track record).

**No turnaround-review-due items this month.**

---

## 7. Other open items carried forward (no new action triggered this session)

| Ticker | Status | Carried from | This session's note |
|---|---|---|---|
| **AVGO** | Score 69.5, predates 2026-06-20 modifier, 4.35% | New flag this session | **Data-integrity inconsistency found:** [watchlist/STALE.md](../watchlist/STALE.md) states "All in-portfolio holdings + AVGO were rescored under the current methodology on 2026-06-20 and are current" — but AVGO's own watchlist entry ([watchlist/in-portfolio/AVGO/AVGO-2026-06-22.md](../watchlist/in-portfolio/AVGO/AVGO-2026-06-22.md)) and `holdings.md` both say the 69.5 score predates the modifier and a rescore is overdue. Not resolved either way in this session — flagging the contradiction for the user/maintainer to correct, since silently editing `STALE.md` is outside this rebalance's scope. Separately, the override rationale for the 2026-06-16 buy is still **not on record** in `decisions/` (per [override-log.md](../portfolio/override-log.md) and the [2026-06-22 weekly brief](weekly-briefs/2026-06-22-weekly-brief.md)). |
| **STIM** | "Not scored — going-concern override," 0.76% | [2026-06-07](2026-06-07-rebalance.md) §6, [2026-06-15](2026-06-15-rebalance.md) §7 | **Third consecutive month unaddressed.** Still flagged as an immediate Phase 06 ("balance sheet crisis") EXIT REVIEW trigger, independent of the monthly cycle. No STIM session exists in `sessions/`. Recommend prioritizing before the recurrence count grows further. |
| **RBRK** | "Not scored — fails quality gates," 0.38% | [2026-06-07](2026-06-07-rebalance.md) §6, [2026-06-15](2026-06-15-rebalance.md) §7 | **Third consecutive month unaddressed.** Still needs an `override-log.md` entry explaining how a name failing Phase 01 outright got into the book. Low urgency given size ($210.00).|
| **VEEV** | Blank score/review, 0.83% | [2026-06-15](2026-06-15-rebalance.md) §1/§7 | **Second consecutive month unaddressed.** Still needs `/rescore`; no entry record found in `sessions/` or `decisions/`. |
| **NVO** | Score 47.6 (Cheap band — no Phase 05 trigger), 0.40% | [2026-06-07](2026-06-07-rebalance.md) §3, [2026-06-15](2026-06-15-rebalance.md) §7 | **Resolved, closing this flag.** The "growth thesis possibly broken" qualitative flag carried for two months was directly investigated in [sessions/2026-06-20-rescore-nvo.md](2026-06-20-rescore-nvo.md): conclusion was a "de-rating with stalled — not broken — fundamentals," i.e. not a Phase 06 trigger. No further carry-forward needed unless new evidence emerges. |
| **ZS** | Score 36.3 (Cheap band — no Phase 05 trigger), 0.22% | [2026-06-15](2026-06-15-rebalance.md) §7 | Rescored 2026-06-20 (61.1 low-confidence Fair Value → 36.3 Cheap) along with the rest of the boundary-name batch. The earlier "low-confidence, post-acquisition GAAP distortion" data flag isn't confirmed resolved by this session — not re-investigated here — but the position is immaterial (0.22%) and carries no trim/exit trigger either way. |
| **TLT** | 29.91%, non-equity, no methodology | [2026-06-07](2026-06-07-rebalance.md) §6, [2026-06-15](2026-06-15-rebalance.md) §4 | See §4 — unresolved structural gap, now **three consecutive months** carried forward. Recommend a dedicated framework-development session rather than continuing to carry this as a routine rebalance line item. |

---

## 8. Summary table — proposed actions

| Ticker | Score | Weight | Proposed action | Driven by |
|---|---|---|---|---|
| **AMZN** | 73.4 | 10.03% | Trim 6–7 sh from IBKR leg (~$1,447–$1,689, ~26–30%) → recycle | Valuation (Phase 05) |
| **CSGP** | 79.0 | 1.35% | Trim 6–8 sh (~$180–$240, ~25–30%) → recycle | Valuation (Phase 05) |
| **GOOG** | 73.1 | 0.65% | Trim 25–30% triggered but **not executable** (1 sh); standing sell-limit @ $389 noted, no change recommended | Valuation (Phase 05) — execution gap |
| **SPOT** | 80.5 | 0.84% | Trim-to-50% triggered but **not executable** (1 sh); standing sell-limit @ $518 noted, no change recommended | Valuation (Phase 05) — execution gap |
| **MSFT** | 35.0 | 15.01% | Hold on valuation (Cheap band); cap breach is $3.64 (data-precision noise) — **no trim recommended**, re-check next sync | Concentration (Upgrade 7) — immaterial |
| **TLT** | n/a | 29.91% | No action — unresolved structural gap, 3rd consecutive month carried forward | Framework gap |
| **ADBE** | 0.0 | 3.50% | Recycling destination: $1,365.84 of trim proceeds completes the 17-sh target | Recycling (Phase 05) |
| **META** | 19.6 | 7.22% | Qualifies on score (0.0–29.9) but **zero executable headroom** to its own 8% sizing ceiling — not a usable destination this cycle | Recycling (Phase 05) — sizing-ceiling gap |
| **AVGO** | 69.5 (stale) | 4.35% | No action this session — flagged: methodology-stale score, `STALE.md` inconsistency, and missing override rationale (§7) | Data integrity / governance |
| **VEEV** | blank | 0.83% | Needs `/rescore` — no score, no entry record (2nd consecutive month) | Data gap |
| DUOL, NFLX, NOW, NVDA, UBER, V, ZS | 30.0–69.9 | 18.34% combined | Hold — Cheap/Fair Value, no trim under current rule | Valuation (Phase 05) |
| NKE, NVO, SPGI | 30.0–49.9 | 2.75% combined | Hold, do not add (Cheap band, not Very Cheap recycling destinations); NKE carries an active Phase 01 ROIC-gate override flag (see [NKE-2026-06-20.md](../watchlist/in-portfolio/NKE/NKE-2026-06-20.md)) | Valuation (Phase 03/05) |
| STIM, RBRK | not scored | 1.14% combined | Open items carried forward (§7), now 3rd consecutive month — no new action this session | Fundamental (Phase 06) / Quality-gate compliance |
| XEON, CASH | n/a | 3.72% combined | No action | Out of scope / liquidity |

**Recommended sequencing:**
1. Execute (or re-propose) the AMZN/CSGP trims, recycling the proceeds into ADBE per §5. No MSFT trim this cycle (§4).
2. Resolve the AVGO data-integrity flag: reconcile `watchlist/STALE.md` with AVGO's own entry, run a fresh `/rescore AVGO`, and supply the missing override rationale for `decisions/`.
3. Run the still-open STIM exit review (going-concern, Phase 06) and the RBRK override-log entry — both now 3 consecutive months overdue; recommend prioritizing ahead of next month's cycle.
4. `/rescore VEEV` (2nd consecutive month with no score at all).
5. TLT's structural gap (29.91% vs. the 15% cap) remains a standalone framework-development item, not a routine rebalance line item.

*Session complete. No trades executed — this is a proposal for human review. Log any executed trims/exits in `decisions/` and refresh `holdings.md` via `/sync-portfolio` once they settle.*

---

## Glossary

- **GTC (Good-Til-Cancelled)** — an order instruction telling the broker to keep a limit order open indefinitely until it fills or is manually cancelled.
- **MoS (Margin of Safety)** — how far below fair value the buy price is set, as a cushion against being wrong.
- **NLV (Net Liquidation Value)** — a broker's headline account value: all positions at current market price, plus cash, minus liabilities.
- **Phase 01–06** — the six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **R/R (Risk/Reward ratio)** — (expected gain) ÷ (expected loss) on a trade; this framework requires at least 2:1 before entering.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Turnaround Sub-Gate** — the conditional path (Hybrid Upgrade 4) that lets a company failing some quality criteria still enter as a small (2–3%) position if it passes 5 specific tests (historical ROIC, insider buying, margin of safety, debt level, identifiable moat).
- **Valuation score** — this framework's 0.0–100.0 continuous score (0 = cheapest, 100.0 = most expensive) combining quality and valuation sub-scores plus the Rate Environment Gate.
- **Human Override** — a position opened or held outside the framework's own rules (e.g. bought at a valuation score of 50.0+). Tracked for life in `override-log.md`.

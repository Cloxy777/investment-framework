# 2026-06-29 — Rebalance Session

**Task type:** REBALANCE
**Scope:** Portfolio-wide trim/hold/exit review across all rows in [holdings.md](../portfolio/holdings.md) (combined total ≈ **$54,891.48**, per the 2026-06-28 sync), applying Phase 05 (Dynamic Trimming) and Phase 06 (Exit Triggers) from [strategy.md](../framework/strategy.md) to the **current 0.0–100.0 scores**, plus the Upgrade 7 15% single-position cap and an Upgrade 4 Turnaround Sub-Gate review-due check. This is the fourth monthly run of Routine 5 ([decisions/2026-06-13-automation-routine-schedule.md](../decisions/2026-06-13-automation-routine-schedule.md)), following [2026-06-07](2026-06-07-rebalance.md), [2026-06-15](2026-06-15-rebalance.md), and [2026-06-22](2026-06-22-rebalance.md).

**No trades executed. This is a proposal for human review only.**

---

## 1. Holdings pull & staleness check

Source: [holdings.md](../portfolio/holdings.md), live-synced 2026-06-28 from IBKR (full sync) + Freedom24 (unchanged since 2026-06-07). Per [sessions/weekly-briefs/2026-06-28-weekly-brief.md](weekly-briefs/2026-06-28-weekly-brief.md) §2, the only earnings date in the 7 days to 2026-06-28 across all 22 equity holdings was **NKE (2026-06-30)** — still one calendar day in the future as of this session, so results aren't out yet and there is **no Rule 9 trigger to act on**. No other holding has had earnings since its last review. **By the earnings-based staleness criterion in [operating-calendar.md](../framework/operating-calendar.md), no holding is stale this session.**

| Ticker | Weight % | USD value | Score | Last Review | Band (Phase 03/05) |
|---|---|---|---|---|---|
| ADBE | 3.69% | $2,027.30 | 0.0 | 20 Jun 2026 | 0.0–29.9 Very Cheap |
| AMZN | 9.99% | $5,485.50 | 73.4 | 20 Jun 2026 | 70.0–79.9 Expensive |
| AVGO | 4.01% | $2,199.00 | 69.5 (**stale**) | 14 Jun 2026 | predates 2026-06-20 modifier — see §7 |
| CSGP | 1.38% | $755.00 | 79.0 | 20 Jun 2026 | 70.0–79.9 Expensive |
| DUOL | 8.20% | $4,501.84 | 53.7 | 20 Jun 2026 | 50.0–69.9 Fair Value |
| GOOG | 0.61% | $336.15 | 73.1 | 20 Jun 2026 | 70.0–79.9 Expensive |
| META | 7.10% | $3,896.31 | 17.2 | 26 Jun 2026 | 0.0–29.9 Very Cheap |
| MSFT | 15.09% | $8,279.60 | 33.9 | 26 Jun 2026 | 30.0–49.9 Cheap |
| NFLX | 1.61% | $886.20 | 61.2 | 20 Jun 2026 | 50.0–69.9 Fair Value |
| NKE | 1.49% | $818.35 | 43.1 | 20 Jun 2026 | 30.0–49.9 Cheap (override flag, see [NKE-2026-06-20.md](../watchlist/in-portfolio/NKE/NKE-2026-06-20.md)) |
| NOW | 2.16% | $1,184.95 | 42.3 | 20 Jun 2026 | 30.0–49.9 Cheap |
| NVDA | 4.92% | $2,698.50 | 48.5 | 20 Jun 2026 | 30.0–49.9 Cheap |
| NVO | 0.44% | $240.35 | 47.6 | 20 Jun 2026 | 30.0–49.9 Cheap |
| RBRK | 0.40% | $216.99 | not scored | Jun 2026 | special — see §7 |
| SPGI | 0.74% | $408.16 | 33.4 | 20 Jun 2026 | 30.0–49.9 Cheap |
| SPOT | 0.84% | $460.02 | 80.5 | 20 Jun 2026 | 80.0–89.9 Very Expensive |
| STIM | 1.20% | $660.00 | not scored | Jun 2026 | special — see §7 |
| TLT | 30.53% | $16,762.62 | not scored | Jun 2026 | special — see §4 |
| TRN | 3.04% | $1,667.60 | 10.0 | 24 Jun 2026 | 0.0–29.9 Very Cheap (partial fill) |
| UBER | 0.42% | $228.00 | 34.8 | 20 Jun 2026 | 30.0–49.9 Cheap |
| V | 0.61% | $336.23 | 39.2 | 20 Jun 2026 | 30.0–49.9 Cheap |
| VEEV | 0.94% | $514.08 | **blank** | **blank** | needs `/rescore` — see §7 |
| XEON | 3.10% | $1,701.88 | not scored | Jun 2026 | out of scope |
| ZS | 0.24% | $131.96 | 36.3 | 20 Jun 2026 | 30.0–49.9 Cheap |
| CASH (IBKR) | -2.87% | -$1,576.85 | — | — | liquidity (negative — see [ibkr.md](../portfolio/snapshots/ibkr.md)) |
| CASH (Freedom24) | 0.19% | $106.85 | — | — | liquidity |

**Live-price drift check (today, 2026-06-29, via IBKR `get_price_snapshot`, Rule 0):** AMZN $231.90→$235.05 (+1.36%), CSGP $30.20→$30.42 (+0.73%), GOOG $336.15→$338.91 (+0.82%), SPOT $460.02→$464.00 (+0.87%), MSFT $372.73→$379.15 (+1.72%), AVGO $366.50→$372.11 (+1.53%), ADBE $202.73→$204.36 (+0.80%), META $551.11→$560.00 (+1.61%), TRN GBX 210.6→213.0 (+1.14%), NKE $40.92→$41.20 (+0.68%). This reads as a broad, market-wide Monday gain (every name up 0.7–1.7%), not a name-specific move — none of it is remotely close to the 10–20pt score-band swing needed to flip a Phase 05 band. **No band flips; no "refresh before executing" caveat this session**, same as 2026-06-22. Dollar figures in §2, §4, and §5 below use these live prices (today) for every actionable calculation, kept explicitly separate from the §1 table above (which reports the official 2026-06-28 sync, per `/rebalance`'s own data-sourcing convention).

**Flag — AVGO, now 2nd consecutive rebalance session flagged stale (06-22, 06-29):** AVGO's 69.5 score is from the 2026-06-14 new-position session, predating the 2026-06-20 Upside/Downside Modifier. See §7 for the still-unresolved `watchlist/STALE.md` contradiction and the still-missing override rationale.

**Flag — VEEV, now 3rd consecutive rebalance session flagged (06-15, 06-22, 06-29):** still carries no score and no `Last Review` date. No entry session exists anywhere in `sessions/`, and no `watchlist/` directory exists for VEEV at all (checked both `in-portfolio/` and `not-in-portfolio/`) — this is a complete record gap, not just a stale one.

---

## 2. Phase 05 — Dynamic Trimming (applied to current scores, dollar figures at today's live prices)

### Trim 25–30% (Score 70.0–79.9)

| Ticker | Score | Position | 25% | 30% | Reasoning |
|---|---|---|---|---|---|
| **AMZN** | 73.4 | $5,485.50 combined (12 sh IBKR @ live $235.05 = $2,820.60 + 11 sh Freedom24 @ $245.70 screenshot = $2,702.70; 23 sh total) | — | — | "Expensive" band, pure valuation-driven trim, no fundamental break — unchanged from 2026-06-20. In whole shares, 25–30% of the 23-share combined position ≈ 5.75–6.9 sh → **6 sh** ($1,410.30, 25.5% of combined value) to **7 sh** ($1,645.35, 30.0%). Recommend trimming the IBKR leg only (live-executable via MCP); Freedom24's 11 sh are screenshot-only. |
| **CSGP** | 79.0 | $760.50 (25 sh, IBKR, live $30.42) | $190.13 | $228.15 | "Expensive," same band as 2026-06-22 (no rescore since). In whole shares: 25% = 6.25 sh → **6 sh** ($182.52, 24.0%); 30% = 7.5 sh → **8 sh** ($243.36, 32.0%, the closer whole-share fit, same rounding choice as last month). |
| **GOOG** | 73.1 | $338.91 (1 sh, IBKR, live) | $84.73 | $101.67 | "Expensive." **Not executable**: 1 share cannot be partially trimmed. See execution-mechanics note below. |

### Trim to 50% (Score 80.0–89.9)

| Ticker | Score | Position | Trim to 50% | Reasoning |
|---|---|---|---|---|
| **SPOT** | 80.5 | $464.00 (1 sh, IBKR, live) | $232.00 | "Very Expensive," unchanged band since 2026-06-20. **Not executable**: 1 share cannot be halved. See execution-mechanics note below. |

### Trim to tracking (1–2%) — Score 90.0–100.0

None. No holding scores ≥90.0.

**⚠️ Execution-mechanics note — GOOG & SPOT (unchanged from the last two sessions):** both remain single-share IBKR positions where the indicated trim cannot be executed in whole shares. Both still carry standing GTC sell-limit orders **above** today's live price: GOOG SELL 1 @ $389.00 (live $338.91) and SPOT SELL 1 @ $518.00 (live $464.00). If either fills, the result is a 100% exit, more aggressive than the trim trigger calls for. Flagging for awareness only — no change to standing orders recommended (an execution-mechanics judgment call, not a valuation one).

---

## 3. Phase 06 — Full Exit Triggers

**None fired on valuation grounds.** No holding is in the 90.0–100.0 band this month, let alone for the 2+ consecutive quarters Phase 06 requires for a valuation-driven exit.

No new fundamental-deterioration, thesis-broken, or balance-sheet-crisis triggers identified **from this session's inputs**. STIM and RBRK carry pre-existing, carried-forward exit-review flags from fundamentals (not from this session — see §7), now in their **fourth consecutive month** unaddressed.

---

## 4. Upgrade 7 — 15% Single-Position Cap Check

15% of $54,891.48 = **$8,233.72**.

| Ticker | Weight | Value (sync, 06-28) | Breach? | Action required |
|---|---|---|---|---|
| **MSFT** | 15.09% | $8,279.60 (20 sh IBKR @ $372.73 = $7,454.60 + 2 sh Freedom24 @ $412.50 = $825.00) | **Yes — by $45.88** | This breach has **grown ~12.6× from last month's $3.64** (2026-06-22). It is still well below the value of even one IBKR share (live today, $379.15) — trimming 1 share would overshoot to ≈$7,900–8,030 combined, a multi-percentage-point overcorrection for a breach worth 0.08pp. **Live-price sensitivity check (today):** repricing only the IBKR leg at today's live $379.15 (20 × $379.15 = $7,583.00, Freedom24 leg held at its last-known $825.00) puts MSFT's combined value at ≈$8,408.00 — a ≈$174 gap above the cap on this single-name basis. This is a directional sensitivity check only, not a recomputed weight (the other 24 positions also moved today and aren't being repriced here), but it's directionally consistent with the breach widening: MSFT's live move today (+1.72%) outpaced the broad ~0.7–1.7% market-wide gain seen across the rest of the book (§1). **No trim recommended this cycle** — the gap is still smaller than one tradable unit — but this is now two consecutive months of growth in the same direction, no longer purely attributable to the ~$10–43 NLV-timing noise flagged in prior syncs. Recommend re-verifying at the next official sync and revisiting if the trend continues into next month. |
| **TLT** | 30.53% | $16,762.62 (77 sh IBKR + 118 sh Freedom24) | **Yes — by $8,528.90** | **No new finding — fourth consecutive month carried forward** (2026-06-07, 2026-06-15, 2026-06-22, now 2026-06-29). Same structural gap logged in [override-log.md](../portfolio/override-log.md) ("No exit criteria defined / Define exit rules or divest"); the framework still has no fixed-income valuation/sizing methodology. See §7 — recommend this graduate from a routine carry-forward line to a dedicated framework-development session, now overdue by any reasonable measure given the recurrence count. |
| All others | ≤ 9.99% | — | No | — |

---

## 5. Recycling Plan

Per Phase 05 — "proceeds always reinvested into current Score 0.0–29.9 names only." Three held names sit in that band: **ADBE (0.0)**, **META (17.2)**, and **TRN (10.0)**.

**META still has zero executable headroom.** META's combined value is $3,896.31 (6 sh IBKR @ sync $551.11 = $3,306.66 + 1 sh Freedom24 @ $589.65 screenshot). Its Phase 03 sizing ceiling for a Very Cheap score is 6–8% of the book; 8% of $54,891.48 = $4,391.32, leaving only **$495.01** of room — less than the cost of one additional IBKR share at today's live $560.00. Same conclusion as 2026-06-22: **not a usable recycling destination this cycle**, despite qualifying on score alone.

**ADBE remains a fully-documented, unambiguous destination.** ADBE sits at 3.69% (10 sh IBKR) vs. its documented ~17-share target ([2026-06-12 new-position session](2026-06-12-new-position-adbe.md)): **7 shares remain**, valued at today's live $204.36 = **$1,430.52**.

**TRN is a new, much larger destination this month — its first appearance in a rebalance recycling plan.** TRN entered the portfolio 2026-06-24 (score 10.0) and is a documented partial fill: 600 of ≈1,553 target shares filled ([sessions/2026-06-24-new-position-trn.md](2026-06-24-new-position-trn.md), target ≈$4,191.30). The remaining **953 shares**, at today's live price (GBX 213.0 = £2.130/share) and today's live GBP→USD rate (1.32294, via `get_account_balances`): 953 × £2.130 × 1.32294 = **≈$2,685.42** — substantially larger than ADBE's gap.

**⚠️ TRN order-status caveat carried forward from the 2026-06-28 weekly brief, unresolved 5 days later:** order 1551402669 (`Buy 900 TRN` @ GBX 161.50, placed 2026-06-24) shows `REPLACED` with `cum_shares_qty: 0` (never filled) and no live successor visible in the 2026-06-28 orders fetch ([ibkr-orders.md](../portfolio/snapshots/ibkr-orders.md)). Whether a fresh order is already working toward the remaining ~953 shares, or whether this attempt was simply abandoned, **cannot be determined from this data alone** — this session did not re-pull live orders (out of scope for `/rebalance`; that's `/sync-orders`'s job), so this flag is exactly as old as the last sync, not freshly re-verified.

### Proceeds available (whole-share-executable trims only; MSFT excluded per §4, GOOG/SPOT excluded per §2)

| Source | Amount | Driver |
|---|---|---|
| AMZN trim (6–7 sh, IBKR, live $235.05) | $1,410.30 – $1,645.35 | Phase 05 (valuation) |
| CSGP trim (6–8 sh, IBKR, live $30.42) | $182.52 – $243.36 | Phase 05 (valuation) |
| **Subtotal** | **$1,592.82 – $1,888.71** | |

### Allocation — two options, flagged for explicit human sign-off rather than a unilateral pick

Both options agree on the first step; they differ only on the remainder, because of the open TRN order-status question above.

1. **First $1,430.52 → ADBE** in both options, completing the documented 17-share target (10 → 17 sh). Unambiguous, smallest, already a known quantity.
2. **Remainder (≈$162.30 – $458.19) — two options:**
   - **Option A (conservative):** remainder → cash, joining the existing (currently negative — see [ibkr.md](../portfolio/snapshots/ibkr.md)) cash position. No new TRN allocation until the `REPLACED` 900-share order is manually verified in TWS/Client Portal — avoids risking a double-up if an order is already quietly working toward the same target.
   - **Option B (continue the pattern):** apply the remainder as a further small TRN top-up (≈76–215 GBP-equivalent shares at GBX 213.0), consistent with the partial-fill-then-top-up pattern already used for both ADBE and TRN itself. The remainder is small enough relative to TRN's full ≈$2,685 gap that it wouldn't meaningfully prejudge the larger question either way, but it does add exposure before the order-status ambiguity is resolved.

Recommend resolving the TWS/Client Portal check **first**, independent of which option is chosen — it determines whether TRN's much larger ≈$2,685 gap is already being addressed by a live order or is fully open.

**Watchlist sweep — no new destinations found.** Checked every `not-in-portfolio` watchlist entry evaluated since the last rebalance (CVX, MU, PLTR, CBRS, MCD, NOK, TTWO, IBM, WSE) for a qualifying Score 0.0–29.9: **none qualify.** All eight of CVX/MU/PLTR/CBRS/MCD/NOK/TTWO/IBM fail the Phase 01 quality gate outright (not scored), and WSE — which did carry a 27.3 score on 2026-06-21 — flipped back to a Phase 01 gate-fail on its 2026-06-26 re-check (two valuation filters turned FAIL after a post-earnings price pop outran a margin-compression result). **PDD** (watchlist-only, never held) still carries a stale 5.0 score from 2026-06-14, pre-modifier, per [watchlist/STALE.md](../watchlist/STALE.md) — would need a fresh `/rescore` before it could count as a destination even if it were held. Unchanged from prior sessions.

---

## 6. Upgrade 4 — Turnaround Sub-Gate Review Check

Searched [override-log.md](../portfolio/override-log.md) and `decisions/` for any position **entered** under the Turnaround Sub-Gate ("Conditional Watch, 2–3% max," mandatory 2-quarter review).

**Result: none found** — same conclusion as all three prior months. The Override Log table in `override-log.md` carries exactly one entry (AVGO, 2026-06-16, a *valuation* override, not a Turnaround Sub-Gate entry — see §7). A grep of `decisions/` for "Turnaround" returns only unrelated automation/glossary decision files and the override-log's own description of how Upgrade 4 came to exist — no actual entry record.

**No turnaround-review-due items this month.**

---

## 7. Other open items carried forward (no new action triggered this session)

| Ticker | Status | Carried from | This session's note |
|---|---|---|---|
| **AVGO** | Score 69.5, predates 2026-06-20 modifier, 4.01% | [2026-06-22](2026-06-22-rebalance.md) §7 | **2nd consecutive month.** [watchlist/STALE.md](../watchlist/STALE.md) still states "All in-portfolio holdings + AVGO were rescored under the current methodology on 2026-06-20 and are current" — unresolved, same contradiction as last month. The 2026-06-16 override rationale is still **not on record** in `decisions/`. |
| **STIM** | "Not scored — going-concern override," 1.20% | [2026-06-07](2026-06-07-rebalance.md) §6, [2026-06-15](2026-06-15-rebalance.md) §7, [2026-06-22](2026-06-22-rebalance.md) §7 | **4th consecutive month unaddressed.** Still flagged as an immediate Phase 06 ("balance sheet crisis") EXIT REVIEW trigger, independent of the monthly cycle. No STIM session exists in `sessions/`. The position itself grew (345→500 sh) and added a covered-call leg this month (per the 2026-06-28 weekly brief) — that growth is a separate, already-resolved order-tracking matter, not a resolution of this governance flag. |
| **RBRK** | "Not scored — fails quality gates," 0.40% | [2026-06-07](2026-06-07-rebalance.md) §6, [2026-06-15](2026-06-15-rebalance.md) §7, [2026-06-22](2026-06-22-rebalance.md) §7 | **4th consecutive month unaddressed.** Still needs an `override-log.md` entry explaining how a name failing Phase 01 outright got into the book. Low urgency given size ($216.99). |
| **VEEV** | Blank score/review, 0.94% | [2026-06-15](2026-06-15-rebalance.md) §1/§7, [2026-06-22](2026-06-22-rebalance.md) §1/§7 | **3rd consecutive month unaddressed.** Still needs `/rescore`; no entry record found anywhere in `sessions/` or `watchlist/`. |
| **TLT** | 30.53%, non-equity, no methodology | [2026-06-07](2026-06-07-rebalance.md) §6, [2026-06-15](2026-06-15-rebalance.md) §4, [2026-06-22](2026-06-22-rebalance.md) §4 | See §4 — unresolved structural gap, now **four consecutive months** carried forward. Recommend a dedicated framework-development session rather than continuing to carry this as a routine rebalance line item. |
| **MA** (not held — new finding) | Watchlist-only, not a holdings.md row | New this session | `watchlist/STALE.md`'s central registry still lists MA at its **pre-modifier score (53.3, scored 2026-06-14)**, but a fresh rescore exists and supersedes it: [sessions/2026-06-22-rescore-ma.md](2026-06-22-rescore-ma.md) and [watchlist/not-in-portfolio/MA/MA-2026-06-22.md](../watchlist/not-in-portfolio/MA/MA-2026-06-22.md) carry a current final score of **38.0** with no stale banner. The per-ticker file was correctly updated; the central `STALE.md` row simply wasn't removed — a registry-maintenance gap distinct from AVGO's "marked current but isn't" issue (this is the mirror case: marked stale but isn't anymore). Separately, an active GTC order (`BUY MA 4 @ $464.00`, unchanged since 2026-06-16) is still working in the IBKR account for this same, not-held name — that order predates and is unrelated to this registry finding, noted only for completeness since MA isn't a `holdings.md` row and is otherwise outside this rebalance's scope. |

---

## 8. Summary table — proposed actions

| Ticker | Score | Weight | Proposed action | Driven by |
|---|---|---|---|---|
| **AMZN** | 73.4 | 9.99% | Trim 6–7 sh from IBKR leg (~$1,410–$1,645, ~25.5–30%) → recycle | Valuation (Phase 05) |
| **CSGP** | 79.0 | 1.38% | Trim 6–8 sh (~$183–$243, ~24–32%) → recycle | Valuation (Phase 05) |
| **GOOG** | 73.1 | 0.61% | Trim 25–30% triggered but **not executable** (1 sh); standing sell-limit @ $389 noted, no change recommended | Valuation (Phase 05) — execution gap |
| **SPOT** | 80.5 | 0.84% | Trim-to-50% triggered but **not executable** (1 sh); standing sell-limit @ $518 noted, no change recommended | Valuation (Phase 05) — execution gap |
| **MSFT** | 33.9 | 15.09% | Hold on valuation (Cheap band); cap breach is $45.88 and **growing** (12.6× last month) — still below 1 share's value, **no trim recommended**, but flagged as a trend to watch, not noise | Concentration (Upgrade 7) — watch |
| **TLT** | n/a | 30.53% | No action — unresolved structural gap, 4th consecutive month carried forward | Framework gap |
| **ADBE** | 0.0 | 3.69% | Recycling destination: $1,430.52 of trim proceeds completes the 17-sh target | Recycling (Phase 05) |
| **TRN** | 10.0 | 3.04% | New, much larger recycling destination (~$2,685.42 gap to target); allocation deferred pending TWS verification of the open `REPLACED` order — see §5 Options A/B | Recycling (Phase 05) — order-status caveat |
| **META** | 17.2 | 7.10% | Qualifies on score but **zero executable headroom** to its 8% sizing ceiling — not usable this cycle | Recycling (Phase 05) — sizing-ceiling gap |
| **AVGO** | 69.5 (stale) | 4.01% | No action — methodology-stale score, `STALE.md` contradiction, missing override rationale (§7), 2nd consecutive month | Data integrity / governance |
| **VEEV** | blank | 0.94% | Needs `/rescore` — no score, no entry record anywhere (3rd consecutive month) | Data gap |
| DUOL, NFLX, NOW, NVDA, UBER, V, ZS | 30.0–69.9 | 17.95% combined | Hold — Cheap/Fair Value, no trim under current rule | Valuation (Phase 05) |
| NKE, NVO, SPGI | 30.0–49.9 | 2.67% combined | Hold, do not add (Cheap band, not Very Cheap); NKE carries an active Phase 01 ROIC-gate override flag | Valuation (Phase 03/05) |
| STIM, RBRK | not scored | 1.60% combined | Open items carried forward (§7), now 4th consecutive month — no new action this session | Fundamental (Phase 06) / Quality-gate compliance |
| MA (not held) | 38.0 (current, not stale) | n/a | `STALE.md` registry-cleanup flag only — no position held, no trade implication | Data integrity (§7) |
| XEON, CASH | n/a | 0.42% combined | No action | Out of scope / liquidity |

**Recommended sequencing:**
1. Execute (or re-propose) the AMZN/CSGP trims; route the first $1,430.52 of proceeds to ADBE per §5. No MSFT trim this cycle (§4).
2. **Verify the TRN `REPLACED` 900-share order in TWS/Client Portal** before deciding between Option A/B for the trim remainder — this also resolves whether TRN's ~$2,685 gap is already being worked.
3. Resolve the AVGO data-integrity flag: reconcile `watchlist/STALE.md` with AVGO's own entry, run a fresh `/rescore AVGO`, and supply the missing override rationale for `decisions/`. Also clean up `STALE.md`'s stale MA row (§7) — a smaller, unrelated registry fix.
4. Run the still-open STIM exit review (going-concern, Phase 06) and the RBRK override-log entry — both now 4 consecutive months overdue; recommend prioritizing ahead of next month's cycle.
5. `/rescore VEEV` (3rd consecutive month with no score at all, and no entry record anywhere).
6. TLT's structural gap (30.53% vs. the 15% cap) remains a standalone framework-development item, not a routine rebalance line item — now 4 consecutive months carried forward.

*Session complete. No trades executed — this is a proposal for human review. Log any executed trims/exits in `decisions/` and refresh `holdings.md` via `/sync-portfolio` once they settle.*

---

## Glossary

- **FX (foreign exchange) rate** — the price of converting one currency into another; this framework only uses live, broker-reported FX rates (here, IBKR's `get_account_balances`) to convert TRN's GBP-denominated position to USD, never an assumed rate, per Rule 0.
- **GBX / pence (GBp)** — one-hundredth of one British pound; most LSE-listed stocks (here, TRN) quote in GBX rather than whole pounds, and this framework converts explicitly to avoid a 100x error.
- **GTC (Good-Til-Cancelled)** — an order instruction telling the broker to keep a limit order open indefinitely until it fills or is manually cancelled.
- **Human Override** — a position opened or held outside the framework's own rules (e.g. bought at a valuation score of 50.0+). Tracked for life in `override-log.md`.
- **Hybrid Upgrade** — one of 7 framework-specific rule additions layered on the base 6-phase strategy (Upgrade 4 = Turnaround Sub-Gate, Upgrade 7 = the 15% position cap, both used in this session).
- **Margin (brokerage)** — borrowing against an account's own assets rather than funding a purchase with cash on hand; relevant here because TRN's purchase was funded by letting GBP cash go negative.
- **NLV (Net Liquidation Value)** — a broker's headline account value: all positions at current market price, plus cash, minus liabilities.
- **Partial fill** — when a limit order executes for less than its full requested quantity, leaving a position below its full target size until a follow-up order completes it (the case for both ADBE and TRN this session).
- **R/R (Risk/Reward ratio)** — (expected gain) ÷ (expected loss) on a trade; this framework requires at least 2:1 before entering (relevant to the MA note in §7).
- **REPLACED (order status)** — an IBKR order-lifecycle status meaning the order was superseded by a new order; the original order ID stops being live, but that alone doesn't confirm whether the replacement itself filled, is still working, or was cancelled.
- **Turnaround Sub-Gate** — the conditional path (Hybrid Upgrade 4) that lets a company failing some quality criteria still enter as a small (2–3%) position if it passes 5 specific tests. No entries exist under it in this portfolio.
- **Upside/Downside Modifier (Expected-Return Modifier)** — an additive ±15 adjustment to the valuation score based on expected annual return; the reason several names (e.g. MA, in §7) moved bands when rescored after 2026-06-20.
- **Valuation score** — this framework's 0.0–100.0 continuous score (0.0 = cheapest, 100.0 = most expensive) combining the Phase 02 valuation sub-scores, the Rate Environment Gate, and the Upside/Downside Modifier into a single number that maps to an action band.
- **Watchlist (action band)** — the framework's recommendation for a valuation score of 50.0–69.9: fairly-to-fully valued, rule is "no new entry." (Distinct from the repo's `watchlist/` directory, which tracks every scored ticker, held or not.)

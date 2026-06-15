# 2026-06-15 — Rebalance Session

**Task type:** REBALANCE
**Scope:** Portfolio-wide trim/hold/exit review across all rows in [holdings.md](../portfolio/holdings.md) (combined total ≈ **$53,659.11**), applying Phase 05 (Dynamic Trimming) and Phase 06 (Exit Triggers) from [strategy.md](../framework/strategy.md) to the **current 0.0–100.0 scores** (rescaled 2026-06-11, see [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md)), plus the Upgrade 7 15% single-position cap. This is the first run of the new monthly Routine 5 cadence ([decisions/2026-06-13-automation-routine-schedule.md](../decisions/2026-06-13-automation-routine-schedule.md)).

**No trades executed.** Proposal only, per the operating brief.

---

## 1. Holdings pull & staleness check

Source: [holdings.md](../portfolio/holdings.md), live-synced 2026-06-15 from IBKR (full sync) + Freedom24 (unchanged since 2026-06-07). Per [sessions/weekly-briefs/2026-06-15-weekly-brief.md](weekly-briefs/2026-06-15-weekly-brief.md) §2, **no earnings occurred in the 7 days to 2026-06-15** across the 20 equity holdings, and the two most recent reporters (RBRK 2026-06-04, ZS 2026-05-26) are already reflected in their current `Last Review` dates. **No holding is stale by the earnings-based criterion in [operating-calendar.md](../framework/operating-calendar.md).**

| Ticker | Weight % | USD value | Score | Last Review | Band (Phase 03/05) |
|---|---|---|---|---|---|
| ADBE | 3.85% | $2,065.60 | 5.0 | 12 Jun 2026 | 0.0–29.9 Very Cheap |
| AMZN | 10.45% | $5,605.62 | 79.8 | Jun 2026 | 70.0–79.9 Expensive |
| CSGP | 1.53% | $821.00 | 83.3 | Jun 2026 | 80.0–89.9 Very Expensive |
| DUOL | 8.54% | $4,583.44 | 55.6 | 12 Jun 2026 | 50.0–69.9 Fair Value |
| GOOG | 0.68% | $363.24 | 83.7 | Jun 2026 | 80.0–89.9 Very Expensive |
| META | 7.52% | $4,033.65 | 38.5 | 12 Jun 2026 | 30.0–49.9 Cheap |
| MSFT | 16.26% | $8,723.60 | 51.2 | 12 Jun 2026 | 50.0–69.9 Fair Value |
| NFLX | 1.81% | $969.36 | 63.2 | 12 Jun 2026 | 50.0–69.9 Fair Value |
| NKE | 1.69% | $905.80 | 34.1 | Jun 2026 | 30.0–49.9 Cheap (override) |
| NOW | 2.37% | $1,273.32 | 59.3 | Jun 2026 | 50.0–69.9 Fair Value |
| NVDA | 5.47% | $2,935.10 | 62.2 | Jun 2026 | 50.0–69.9 Fair Value |
| NVO | 0.41% | $222.00 | 35.8 | Jun 2026 | 30.0–49.9 Cheap (thesis flag) |
| RBRK | 0.40% | $212.70 | not scored | Jun 2026 | special — see §7 |
| SPGI | 0.78% | $418.91 | 43.3 | Jun 2026 | 30.0–49.9 Cheap |
| SPOT | 0.90% | $482.00 | 82.0 | Jun 2026 | 80.0–89.9 Very Expensive |
| STIM | 0.86% | $458.85 | not scored | Jun 2026 | special — see §7 |
| TLT | 31.08% | $16,678.69 | not scored | Jun 2026 | special — see §4 |
| UBER | 0.39% | $208.17 | 52.9 | Jun 2026 | 50.0–69.9 Fair Value |
| V | 0.60% | $324.00 | 54.9 | Jun 2026 | 50.0–69.9 Fair Value |
| VEEV | 0.89% | $478.62 | **blank** | **blank** | needs `/rescore` — see §7 |
| XEON | 3.22% | $1,727.86 | not scored | Jun 2026 | out of scope |
| ZS | 0.24% | $128.78 | 61.1 (low-conf) | Jun 2026 | 50.0–69.9 Fair Value |
| CASH (IBKR) | 0.60% | $321.57 | — | — | liquidity |
| CASH (Freedom24) | 0.20% | $106.85 | — | — | liquidity |

**Flag — needs `/rescore` before it can be reliably rebalanced:** **VEEV** (3 sh, $478.62, 0.89%) carries no score and no `Last Review` date at all, and no entry session exists for it (it doesn't appear in `sessions/` or `decisions/` — likely a pre-framework legacy position, similar to the AVGO/CSCO gap noted in `holdings.md`). It cannot be assessed under Phase 05/06 until scored. Recommend prioritizing VEEV in the next `/rescore` batch.

**Data-freshness caveat carried from [sessions/2026-06-11-rescore-holdings-new-scale.md](2026-06-11-rescore-holdings-new-scale.md):** CSGP (83.3), GOOG (83.7), and SPOT (82.0) are recomputed-formula scores, not fresh Rule-0 live-price rescores — these are the names whose **band changed** (Trim 25–30% → Trim to 50%) purely from the formula recompute. AMZN (79.8) sits 0.2 points below the 80.0 cutoff into the same deeper band. None of these fail the earnings-staleness test, but given how close AMZN sits to a band edge and how much CSGP/GOOG/SPOT's recommended action changed on a recompute alone, **a fresh `/rescore` for these four before executing any trim below is the prudent sequencing** — consistent with the same caveat the 2026-06-07 rebalance carried forward.

---

## 2. Phase 05 — Dynamic Trimming (applied to current scores)

### Trim 25–30% (Score 70.0–79.9)

| Ticker | Score | Value | 25% | 30% | Reasoning |
|---|---|---|---|---|---|
| **AMZN** | 79.8 | $5,605.62 (12 sh IBKR + 11 sh Freedom24, 23 sh total) | $1,401.41 | $1,681.69 | "Expensive" band, no fundamental break reported — pure valuation-driven trim. In whole shares: 25% ≈ 5.75 sh → **6 sh** ($1,451.46, 25.9%); 30% ≈ 6.9 sh → **7 sh** ($1,693.37, 30.2%). Recommend trimming from the **IBKR leg** (12 sh, live-executable via MCP); Freedom24's 11 sh are screenshot-only and untouched either way. |

### Trim to 50% (Score 80.0–89.9)

| Ticker | Score | Value | Trim to 50% | Reasoning |
|---|---|---|---|---|
| **CSGP** | 83.3 | $821.00 (25 sh, IBKR) | ~$410.50 | "Very Expensive" — formula recompute moved this from the 70s into the 80s band (§1 caveat). In whole shares: 50% = 12.5 sh → **12 sh** ($394.08, leaves 13 sh ≈ 52% of original) or **13 sh** ($426.92, leaves 12 sh ≈ 48%). Either is a reasonable "roughly half" execution. |
| **GOOG** | 83.7 | $363.24 (1 sh, IBKR) | ~$181.62 | "Very Expensive" — same recompute story. **Not executable**: 1 share cannot be halved. See execution-mechanics note below. |
| **SPOT** | 82.0 | $482.00 (1 sh, IBKR) | ~$241.00 | "Very Expensive" — same recompute story. **Not executable**: 1 share cannot be halved. See execution-mechanics note below. |

**⚠️ Execution-mechanics note — GOOG & SPOT:** Both are single-share IBKR positions where "trim to 50%" cannot be executed in whole shares. Both already carry **standing GTC sell-limit orders above current market** ([ibkr-orders.md](../portfolio/snapshots/ibkr-orders.md)): GOOG SELL 1 @ $389.00 (current $363.24) and SPOT SELL 1 @ $518.00 (current $482.00). If either fills, the result is a **100% exit**, not a 50% trim — more aggressive than the Score 80.0–89.9 trigger calls for (Score 90.0–100.0 territory would justify a "trim to tracking" that's closer to a full exit, but neither name is there). This is a pre-existing tension, not new this month — flagging for awareness rather than recommending a change to standing orders (that's an execution-mechanics judgment call, not a valuation one).

### Trim to tracking (1–2%) — Score 90.0–100.0

None. No holding scores ≥90.0.

---

## 3. Phase 06 — Full Exit Triggers

**None fired on valuation grounds.** The only purely valuation-driven exit trigger is "Score 90.0–100.0 sustained 2+ quarters" — no holding is even in the 90s this month, let alone for 2+ quarters.

No fundamental-deterioration, thesis-broken, or balance-sheet-crisis triggers identified **from this session's inputs** for any scored holding. (STIM and RBRK carry pre-existing, carried-forward exit-review flags from fundamentals, not from this session — see §7.)

---

## 4. Upgrade 7 — 15% Single-Position Cap Check

15% of $53,659.11 = **$8,048.87**.

| Ticker | Weight | Value | Breach? | Action required |
|---|---|---|---|---|
| **MSFT** | 16.26% | $8,723.60 (20 sh IBKR @ $394.93 = $7,898.60 + 2 sh Freedom24 ≈ $825.00) | **Yes — by $674.73** | This is a **hold on valuation** (Score 51.2, Fair Value, no trim trigger) but a **forced trim on concentration** — both can be true simultaneously, same as the June 7 precedent. Recommend trimming **3 sh from the IBKR leg** (20 → 17 sh): 3 × $394.93 = $1,184.79, landing the position at $7,538.81 ≈ **14.05%** — a buffer below the 15% line (vs. landing exactly at 15%) to absorb passive drift, consistent with the [2026-06-07 rebalance](2026-06-07-rebalance.md)'s approach. |
| **TLT** | 31.08% | $16,678.69 (77 sh IBKR + 118 sh Freedom24) | **Yes — by $8,629.82** | **No new finding.** This is the same structural gap flagged in the [2026-06-07 rebalance](2026-06-07-rebalance.md) §6 and still open in [override-log.md](../portfolio/override-log.md) ("No exit criteria defined / Define exit rules or divest"). More than half the position would need to move to clear the cap, and the framework has no fixed-income valuation/sizing methodology. **Carried forward again, unresolved** — see §7. |
| All others | ≤ 10.45% | — | No | — |

---

## 5. Recycling Plan

Per Phase 05 — "proceeds always reinvested into current Score 0.0–29.9 names only." **ADBE (Score 5.0) is the only such name currently held**, and it sits at **3.85% vs. its documented ~17-share / ~8% target** ([2026-06-12 new-position session](2026-06-12-new-position-adbe.md)): 10 of ~17 target shares filled, **~7 shares (≈$1,445.92 at the current $206.56 price) remain to reach target.**

### Proceeds available (using whole-share-executable trims + MSFT cap trim)

| Source | Amount | Driver |
|---|---|---|
| AMZN trim (6–7 sh) | $1,451.46 – $1,693.37 | Phase 05 (valuation) |
| CSGP trim (12–13 sh) | $394.08 – $426.92 | Phase 05 (valuation) |
| MSFT trim (3 sh) | $1,184.79 | Upgrade 7 (concentration) |
| **Subtotal** | **$3,030.33 – $3,305.08** | |
| GOOG / SPOT (illustrative, not executable — §2) | +$181.62 / +$241.00 | Phase 05 (valuation) |

### Allocation

1. **First ~$1,445.92 → ADBE**, completing the documented ~17-share target (10 → ~17 sh). This is the only Score 0.0–29.9 destination in the book, and ADBE is already below its own target size — a clean, already-documented use of proceeds.
2. **Remainder (~$1,584 – $1,859, before GOOG/SPOT) → cash**, joining the existing combined cash position (CASH IBKR $321.57 + CASH Freedom24 $106.85 = $428.42, 0.80% combined). Projected combined cash after this allocation: **≈$2,012 – $2,287**, or roughly **3.7%–4.3%** of the $53,659.11 total — a modest liquidity buffer, same "no other Score 0.0–29.9 destination exists" rationale as the June 7 session. Recycling into a Cheap-band name (30.0–49.9 — NKE, NVO, META, SPGI) would not satisfy Phase 05's "0.0–29.9 only" rule and would itself be an undocumented-trigger override.

**Note — possible additional Very-Cheap destination not yet reflected here:** [sessions/2026-06-14-new-position-pdd.md](2026-06-14-new-position-pdd.md) scored **PDD at 5.0** ("Very Cheap," BUY ~8%, ~53 sh ≈ $4,325) on 2026-06-14, one day before this sync — but PDD does not appear in `holdings.md`, and the Freedom Finance snapshot is still dated 2026-06-07 (unchanged). If that BUY was executed via Freedom24, the next `/sync-portfolio` (Freedom Finance leg) would surface it as a second Score 0.0–29.9 destination and this recycling plan should be revisited. Not assumed here — flagging only.

---

## 6. Upgrade 4 — Turnaround Sub-Gate Review Check

Searched [override-log.md](../portfolio/override-log.md) and `decisions/` for any position **entered** under the Turnaround Sub-Gate ("Conditional Watch, 2–3% max," mandatory 2-quarter review).

**Result: none found.** The Override Log table in `override-log.md` is empty (placeholder row only), and no `decisions/` entry records a Turnaround Sub-Gate entry. [automation-schedule.md](../framework/automation-schedule.md) itself notes this check produces "nothing, once `override-log.md` records entry dates for turnaround positions" — it currently doesn't record any.

Two holdings have been **evaluated against** Upgrade 4's criteria (not entered under it):
- **NKE** ([watchlist/in-portfolio/NKE/NKE-2026-06-07.md](../watchlist/in-portfolio/NKE/NKE-2026-06-07.md)) — value-trap flag (ROIC cratered to 7.84–9.00% vs. ~20% historical, fails Phase 01's own ROIC gate retroactively); 1 of 5 Upgrade 4 conditions (insider buying) reportedly met, but not a formal Upgrade-4 entry.
- **RBRK** ([watchlist/in-portfolio/RBRK/RBRK-2026-06-07.md](../watchlist/in-portfolio/RBRK/RBRK-2026-06-07.md)) — explicitly **fails** the Upgrade 4 Turnaround Sub-Gate (IPO 2024, no profitability track record).

**No turnaround-review-due items this month.**

---

## 7. Other open items carried forward (no new action triggered this session)

| Ticker | Status | Carried from | This session's note |
|---|---|---|---|
| **STIM** | "Not scored — going-concern override," 0.86% | [2026-06-07 rebalance](2026-06-07-rebalance.md) §6 | Still flagged as an immediate Phase 06 ("balance sheet crisis") EXIT REVIEW trigger, independent of the monthly cycle. **Still not run** — no STIM session exists in `sessions/`. Recommend prioritizing before next earnings. |
| **RBRK** | "Not scored — fails quality gates," 0.40% | [2026-06-07 rebalance](2026-06-07-rebalance.md) §6 | Still flagged for an `override-log.md` entry (how a name failing Phase 01 outright got into the book). **Still not logged.** Low urgency given size ($212.70). |
| **VEEV** | Blank score/review, 0.89% | New this session | See §1 — needs `/rescore`, no entry record found. |
| **NVO** | Score 35.8 (Cheap band — no Phase 05 trigger), 0.41% | [2026-06-07 rebalance](2026-06-07-rebalance.md) §3 | Carried qualitative flag: growth thesis (GLP-1 share vs. Lilly) flagged as possibly broken — a Phase 06 "growth thesis broken" candidate independent of score. No new evidence gathered this session; still an open watch item for the next `/rescore`. |
| **TLT** | 31.08%, non-equity, no methodology | [2026-06-07 rebalance](2026-06-07-rebalance.md) §6 | See §4 — unresolved structural gap, recommend a dedicated framework-development session (not a routine rebalance line item). |
| **ZS** | Score 61.1 (low-confidence), 0.24% | [2026-06-07 rebalance / rescore](2026-06-07-rescore-full-portfolio.md) | Fair Value band — no Phase 05 trigger. Low-confidence flag (post-acquisition GAAP distortion) not yet resolved; immaterial weight, low urgency. |

---

## 8. Summary table — proposed actions

| Ticker | Score | Weight | Proposed action | Driven by |
|---|---|---|---|---|
| **AMZN** | 79.8 | 10.45% | Trim 6–7 sh from IBKR leg (~$1,451–$1,693, ~26–30%) → recycle | Valuation (Phase 05) |
| **CSGP** | 83.3 | 1.53% | Trim 12–13 sh (~$394–$427, ~half position) → recycle | Valuation (Phase 05) |
| **GOOG** | 83.7 | 0.68% | Trim-to-50% triggered but **not executable** (1 sh); standing sell-limit @ $389 noted, no change recommended | Valuation (Phase 05) — execution gap |
| **SPOT** | 82.0 | 0.90% | Trim-to-50% triggered but **not executable** (1 sh); standing sell-limit @ $518 noted, no change recommended | Valuation (Phase 05) — execution gap |
| **MSFT** | 51.2 | 16.26% | Hold on valuation; **trim 3 sh from IBKR (~$1,185) for cap compliance** → cash | Concentration (Upgrade 7) |
| **TLT** | n/a | 31.08% | No action — unresolved structural gap, carried forward again | Framework gap |
| **ADBE** | 5.0 | 3.85% | Recycling destination: ~$1,446 of trim proceeds completes the ~17-sh target | Recycling (Phase 05) |
| **VEEV** | blank | 0.89% | Needs `/rescore` — no score, no entry record | Data gap |
| DUOL, NFLX, NOW, NVDA, UBER, V, ZS | 50.0–69.9 | 19.32% combined | Hold — Fair Value, no trim under current rule | Valuation (Phase 05) |
| META, NKE, NVO, SPGI | 30.0–49.9 | 10.40% combined | Hold, do not add (Cheap band, but not Very Cheap recycling destinations); NKE/NVO carry qualitative override flags | Valuation (Phase 03/05) |
| STIM, RBRK | not scored | 1.26% combined | Open items carried forward (§7) — no new action this session | Fundamental (Phase 06) / Quality-gate compliance |
| XEON, CASH | n/a | 4.02% combined | No action | Out of scope / liquidity |

**Recommended sequencing:**
1. `/rescore` AMZN, CSGP, GOOG, SPOT with fresh live prices before executing any of the above trims (§1 caveat) — and prioritize VEEV in the same batch (no score at all).
2. Execute (or re-propose) AMZN/CSGP trims + MSFT cap trim, recycling per §5.
3. Run the still-open STIM exit review (going-concern, Phase 06) and the RBRK override-log entry, independent of this cycle.
4. TLT structural-gap discussion remains a standalone framework-development item.

*Session complete. No trades executed — this is a proposal for review. Log any executed trims/exits in `decisions/` and refresh `holdings.md` via `/sync-portfolio` once they settle.*

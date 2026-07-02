# 2026-07-02 — Rebalance Session

**Task type:** REBALANCE
**Scope:** Portfolio-wide trim/hold/exit review across [holdings.md](../portfolio/holdings.md), applying Phase 05 (Dynamic Trimming) and Phase 06 (Exit Triggers) from [strategy.md](../framework/strategy.md) to current scores, the Upgrade 7 15% single-position cap, and the Upgrade 4 Turnaround Sub-Gate review-due check. This is the sixth run of Routine 5 ([decisions/2026-06-13-automation-routine-schedule.md](../decisions/2026-06-13-automation-routine-schedule.md)), following [2026-06-07](2026-06-07-rebalance.md), [2026-06-15](2026-06-15-rebalance.md), [2026-06-22](2026-06-22-rebalance.md), [2026-06-29](2026-06-29-rebalance.md), and [2026-07-01](2026-07-01-rebalance.md).

**No trades executed. This is a proposal for human review only.**

---

## 0. Carryforward check — RGL / MBGL (first flagged 2026-07-01)

Per Rule 0, live data was pulled directly (`get_account_positions`, `get_account_balances`, `get_account_orders`, `get_account_trades`) rather than relying on `holdings.md` (still showing its 2026-06-28 sync, unchanged since).

- **RGL (RiversGold Ltd, ASX) — still unresolved, 2nd consecutive session.** The GTC order (`order_id 630395618`, BUY 60,000 @ AUD $0.009) is still `PARTIALLY_FILLED`: 2,786 shares held, **57,214 shares still remaining** — no new fills since the last one on 2026-07-01T05:25:12Z (checked via `get_account_trades DAYS_7`). Market value **AUD $27.86 (≈USD $19.21** at today's live 0.6894698 AUD→USD rate). Still no Phase 01/02 evaluation, `override-log.md` entry (added 2026-07-01, still open — see [override-log.md](../portfolio/override-log.md)), or resolution recorded. **This order has now been live and unresolved for 3 calendar days — recommend the human investor verify in TWS/Client Portal today** whether it's intentional; every day it stays open is another day it could keep filling.
- **MBGL (Mobility Global Inc) — still unresolved, 2nd consecutive session.** 1 share, market value **$20.93** (live), average cost $0.00 (unchanged). No source investigation has been run yet. Low urgency given size.
- **New today — a live BUY order for PDD (not yet a holding):** `order_id 1150965513`, BUY 10 PDD @ $72.55 limit, GTC, placed **2026-07-02T09:28:52Z** (today). This traces to a documented, framework-compliant evaluation — [sessions/2026-07-01-new-position-pdd.md](2026-07-01-new-position-pdd.md) scored PDD Quality 81.3 / Valuation 0.0 / **Composite 9.4** ("Very Cheap," BUY — Full position). Unlike RGL, **this is not a governance flag** — noted here only for completeness since it surfaced in the live orders pull; it has 0 shares filled and isn't a `holdings.md` row, so it carries no weight/cap/trim implications this session.

Both RGL and MBGL are carried in the table below as unscored, ungoverned rows — no action bands applied, same convention as RBRK/STIM/TLT.

---

## 1. Holdings pull & staleness check

`holdings.md` still states its last full sync as 2026-06-28 — **now 4 calendar days stale**, same gap flagged 2026-07-01. Live data was pulled directly for this session's own calculations (Rule 0), consistent with 07-01. **Recommend running `/sync-portfolio` before the next scheduled routine.**

**Score changes since 2026-07-01:** none. NKE (rescored 07-01: Composite 34.8), META (rescored 07-01: Composite 22.8), and VEEV (first-ever score, 07-01: Composite 29.7) remain the only holdings with a Quality Score / Composite Score computed under the 2026-06-29 methodology; every other holding still carries only a raw Valuation Score (marked `?` for Quality/Composite in `holdings.md`) — per the framework's own stated fallback (use Composite where it exists, raw Valuation Score otherwise, per [decisions/2026-06-29-framework-change-quality-score-and-composite.md](../decisions/2026-06-29-framework-change-quality-score-and-composite.md)).

**Combined total (broker-reported, live):** IBKR Net Liquidation Value **$42,687.05** (`get_account_balances`, BASE row — up $719.20 from 07-01's $41,967.85, mostly broad price gains) + Freedom24 Net Asset Valuation **$15,123.54** (last screenshot sync, 2026-06-07, unchanged) = **$57,810.59**.

| Ticker | Weight % | USD value (live, 2026-07-02) | Score | Quality / Composite | Last Review | Band (Phase 03/05) |
|---|---|---|---|---|---|---|
| ADBE | 3.69% | $2,135.40 | 0.0 | ? / ? | 20 Jun 2026 | 0.0–29.9 Very Cheap |
| AMZN | 9.69% | $5,602.93 | 73.4 | ? / ? | 20 Jun 2026 | 70.0–79.9 Expensive |
| AVGO | 3.86% | $2,233.80 | 69.5 (**stale**) | ? / ? | 14 Jun 2026 | predates 2026-06-20 modifier — see §7 |
| CSGP | 1.29% | $745.00 | 79.0 | ? / ? | 20 Jun 2026 | 70.0–79.9 Expensive |
| DUOL | 7.68% | $4,438.84 | 53.7 | ? / ? | 20 Jun 2026 | 50.0–69.9 Fair Value |
| GOOG | 0.62% | $355.58 | 73.1 | ? / ? | 20 Jun 2026 | 70.0–79.9 Expensive |
| **MBGL** | **0.04%** | **$20.93** | **not scored — ungoverned, see §0** | — | n/a | special |
| META | 7.31% | $4,223.85 | 35.6 | 90.0 / **22.8** | 1 Jul 2026 | 0.0–29.9 Very Cheap (by Composite) |
| MSFT | 14.63% | $8,455.00 | 33.9 | ? / ? | 26 Jun 2026 | 30.0–49.9 Cheap |
| NFLX | 1.54% | $891.00 | 61.2 | ? / ? | 20 Jun 2026 | 50.0–69.9 Fair Value |
| NKE | 1.49% | $863.04 | 13.9 | 44.4 (fails gate) / **34.8** | 1 Jul 2026 | 30.0–49.9 Cheap (override — do NOT add) |
| NOW | 2.16% | $1,247.88 | 42.3 | ? / ? | 20 Jun 2026 | 30.0–49.9 Cheap |
| NVDA | 4.81% | $2,779.84 | 48.5 | ? / ? | 20 Jun 2026 | 30.0–49.9 Cheap |
| NVO | 0.43% | $247.50 | 47.6 | ? / ? | 20 Jun 2026 | 30.0–49.9 Cheap |
| RBRK | 0.43% | $246.00 | not scored | — | Jun 2026 | special — see §7 |
| **RGL** | **0.03%** | **$19.21** | **not scored — ungoverned, see §0** | — | n/a | special |
| SPGI | 0.72% | $418.50 | 33.4 | ? / ? | 20 Jun 2026 | 30.0–49.9 Cheap |
| SPOT | 0.82% | $472.50 | 80.5 | ? / ? | 20 Jun 2026 | 80.0–89.9 Very Expensive |
| STIM | 1.18% | $680.20 | not scored | — | Jun 2026 | special — see §7 |
| TLT | 28.75% | $16,620.17 | not scored | — | Jun 2026 | special — see §4 |
| TRN | 3.05% | $1,763.58 | 10.0 | ? / ? | 24 Jun 2026 | 0.0–29.9 Very Cheap (partial fill) |
| UBER | 0.38% | $219.00 | 34.8 | ? / ? | 20 Jun 2026 | 30.0–49.9 Cheap |
| V | 0.61% | $352.16 | 39.2 | ? / ? | 20 Jun 2026 | 30.0–49.9 Cheap |
| VEEV | 0.96% | $555.99 | 45.1 | 85.7 / **29.7** | 1 Jul 2026 | 0.0–29.9 Very Cheap (by Composite, marginal — see §5) |
| XEON | 2.96% | $1,712.20 | not scored | — | Jun 2026 | out of scope |
| ZS | 0.25% | $145.25 | 36.3 | ? / ? | 20 Jun 2026 | 30.0–49.9 Cheap |
| CASH (IBKR) | 0.59% | $343.02 | — | — | — | liquidity (now positive) |
| CASH (Freedom24) | 0.18% | $106.85 | — | — | — | liquidity |

*STIM's weight excludes the −$36.95 short covered-call market value (5 contracts, `STIM Aug21'26 $2.50 CALL`), same convention as prior sessions — see [ibkr.md](../portfolio/snapshots/ibkr.md).*

*Weight column sums to ~100.15%, not 100% — the recurring Gross-Position-Value-vs-Net-Liquidation-Value timing gap documented in every prior sync/rebalance, not a calculation error.*

---

## 2. Phase 05 — Dynamic Trimming (applied to current scores/Composite where available, live prices)

### Trim 25–30% (Score 70.0–79.9)

| Ticker | Score | Position | Trim (25–30%) | Reasoning |
|---|---|---|---|---|
| **AMZN** | 73.4 (no Composite yet — raw score governs) | $5,602.93 combined (12 sh IBKR @ live $241.6861 = $2,900.23 + 11 sh Freedom24 @ $245.70 last-known = $2,702.70; 23 sh total) | **6–7 sh** ($1,450.12, 25.9% — $1,691.80, 30.2%) | "Expensive" band, pure valuation-driven trim, unchanged since 2026-06-20. Recommend trimming the IBKR leg (live-executable); Freedom24's 11 sh are screenshot-only. |
| **CSGP** | 79.0 (no Composite yet) | $745.00 (25 sh, IBKR, live $29.80) | **7 sh** ($208.60, **28.0%** — inside the 25–30% band) | "Expensive," unchanged band since 2026-06-22. |
| **GOOG** | 73.1 (no Composite yet) | $355.58 (1 sh, IBKR, live) | **Not executable** (1 sh) | "Expensive." See execution-mechanics note below. |

### Trim to 50% (Score 80.0–89.9)

| Ticker | Score | Position | Trim to 50% | Reasoning |
|---|---|---|---|---|
| **SPOT** | 80.5 (no Composite yet) | $472.50 (1 sh, IBKR, live) | **Not executable** (1 sh) | "Very Expensive," unchanged since 2026-06-20. |

### Trim to tracking (1–2%) — Score 90.0–100.0

None. No holding scores ≥90.0 on either raw score or Composite.

**⚠️ Execution-mechanics note — GOOG & SPOT (unchanged, now 5th consecutive session):** both remain single-share positions where the trim can't be executed in whole shares. Standing GTC sell-limits confirmed still live this session (`get_account_orders`): GOOG SELL 1 @ $389.00 (live $355.58) and SPOT SELL 1 @ $518.00 (live $472.50). No change recommended to either order.

**No new trim triggers from META, NKE, or VEEV** — all three now carry a Composite Score, and all three land in Cheap-or-better bands (META 22.8, NKE 34.8, VEEV 29.7) — none of these are trim candidates; META and VEEV are recycling **destinations** instead (§5).

---

## 3. Phase 06 — Full Exit Triggers

**None fired on valuation grounds.** No holding sits in the 90.0–100.0 band, let alone for 2+ consecutive quarters.

No new fundamental-deterioration, thesis-broken, or balance-sheet-crisis triggers from this session's inputs. STIM and RBRK carry pre-existing, carried-forward exit-review flags (now **6th consecutive session** unaddressed — see §7). **RGL and MBGL (§0) are not treated as Phase 06 exit cases** — neither entered under Phase 01–03, so there's no framework-compliant position to "exit" from; the correct lens is override/governance review.

---

## 4. Upgrade 7 — 15% Single-Position Cap Check

15% of $57,810.59 = **$8,671.59**.

| Ticker | Weight | Value (live) | Breach? | Action required |
|---|---|---|---|---|
| **MSFT** | 14.63% | $8,455.00 (20 sh IBKR @ live $381.50 = $7,630.00 + 2 sh Freedom24 @ $412.50 last-known = $825.00) | **No** | Still under the cap, by **$216.59** — a wider margin than 07-01's $168.51, the portfolio total growing faster than MSFT's own price this session. No trim needed. Continue monitoring — this line has bounced between breach and no-breach three times in the last four sessions purely on live-price noise. |
| **TLT** | 28.75% | $16,620.17 (77 sh IBKR + 118 sh Freedom24) | **Yes — by $7,948.58** | **No new finding — 6th consecutive session carried forward** (2026-06-07, 06-15, 06-22, 06-29, 07-01, now 07-02). Same structural gap logged in [override-log.md](../portfolio/override-log.md); framework still has no fixed-income valuation/sizing methodology. Recommend this graduate from a routine carry-forward line to a dedicated framework-development session — now overdue by any reasonable measure. |
| All others | ≤ 9.69% | — | No | — |

---

## 5. Recycling Plan

Per Phase 05 — "proceeds always reinvested into current Score 0.0–29.9 names only." Four held, scored names now qualify: **ADBE (0.0)**, **META (Composite 22.8)**, **TRN (10.0)**, and **VEEV (Composite 29.7, new this session)**.

**ADBE remains the fully-documented, unambiguous destination.** ADBE sits at 3.69% (10 sh IBKR) vs. its ~17-share target ([2026-06-12 new-position session](2026-06-12-new-position-adbe.md)): **7 shares remain**, at today's live $213.5400 = **$1,494.78**.

**META still has essentially zero executable headroom.** Combined value $4,223.85 vs. its 8% Phase 03 ceiling of $4,624.85 (8% × $57,810.59) leaves only **$401.00** of room — less than one additional IBKR share at today's live $605.70. **Not a usable destination this cycle.**

**VEEV is a new, cleaner destination this session — no order-status ambiguity, unlike TRN.** Its own [2026-07-01 rescore session](2026-07-01-rescore-veev.md) computed a full order setup: risk-based position size ≈19.71 sh (6.67% of portfolio, inside the 6–8% Very Cheap band), currently held at 3 sh (0.96%). **Top-up gap ≈16.71 sh ≈ $3,097** at today's live $185.33. **Caveat carried from that session: this is flagged as a "marginal, not high-conviction" signal** — Composite Score sits 0.3pt inside the 0.0–29.9 boundary, R/R clears the 2:1 floor by only 0.16:1, and the result depends on several individually-defensible-but-swingy judgment calls (ROIC treatment, comp-multiple anchors, catalyst-window guardrail). Worth weighing that against TRN's cleaner (if smaller) documented thesis before committing meaningful capital here.

**TRN's gap remains open, order-status question still unresolved — now 5th consecutive session.** 953 shares remain toward the ~1,553-share target ([sessions/2026-06-24-new-position-trn.md](2026-06-24-new-position-trn.md)). At today's live price (GBX 220.40/share) and live FX (1.333624): 953 × £2.2040 × 1.333624 ≈ **$2,801.15**. Order 1551402669 (`Buy 900 TRN` @ GBX 161.50, placed 2026-06-24) is still confirmed `REPLACED`, `cum_shares_qty: 0`, with **no live successor** in this session's `get_account_orders` fetch — unresolved for a 5th consecutive session.

### Proceeds available (whole-share-executable trims only)

| Source | Amount | Driver |
|---|---|---|
| AMZN trim (6–7 sh, IBKR, live $241.6861) | $1,450.12 – $1,691.80 | Phase 05 (valuation) |
| CSGP trim (7 sh, IBKR, live $29.80) | $208.60 | Phase 05 (valuation) |
| **Subtotal** | **$1,658.72 – $1,900.40** | |

### Allocation

1. **First $1,494.78 → ADBE**, completing the documented 17-share target (10 → 17 sh). Unambiguous, smallest, already a known quantity.
2. **Remainder (≈$163.94 – $405.62) — three options, flagged for explicit human sign-off:**
   - **Option A (conservative):** remainder → cash. No new TRN or VEEV allocation until open questions are resolved.
   - **Option B (continue the TRN pattern):** remainder → a further small TRN top-up, consistent with the partial-fill-then-top-up pattern already used for ADBE and TRN — but this doesn't resolve the standing order-status ambiguity, and risks a double-up if a hidden live order is already working toward the same target.
   - **Option C (new — start the VEEV top-up):** remainder → a small VEEV top-up. Cleaner mechanically (no order-status ambiguity like TRN), but VEEV's own session explicitly flags the underlying signal as marginal/boundary-sitting (§ above) — a smaller first tranche rather than committing toward the full ~$3,097 gap immediately would let the thesis prove out at the next rescore (02 Sept 2026 earnings) before sizing further.

**Watchlist sweep — no new destinations found beyond VEEV.** No `not-in-portfolio` evaluation has been run since the 2026-07-01 rebalance's sweep (PDD is the only new evaluation since then, and it isn't held — see §0). Re-checked [watchlist/STALE.md](../watchlist/STALE.md): no other in-portfolio ticker crossed into a Composite Score of 0.0–29.9 this session.

---

## 6. Upgrade 4 — Turnaround Sub-Gate Review Check

Searched [override-log.md](../portfolio/override-log.md) and `decisions/` (fresh `grep -i turnaround` across the repo this session) for any position **entered** under the Turnaround Sub-Gate ("Conditional Watch, 2–3% max," mandatory 2-quarter review).

**Result: none found — same conclusion as all five prior months.** The Override Log carries two entries (AVGO — valuation override; RGL — quality waiver), neither a Turnaround Sub-Gate entry.

**No turnaround-review-due items this month** under the strict "entered via Upgrade 4" reading. **Note carried forward, now spanning three consecutive rescores (2026-06-07, 2026-06-20, 2026-07-01):** NKE's [2026-07-01 rescore](2026-07-01-rescore-nke.md) / [watchlist entry](../watchlist/in-portfolio/NKE/NKE-2026-07-01.md) recommends formally converting NKE's standing value-trap override into a documented Upgrade 4 Turnaround Sub-Gate entry + `override-log.md` row. This has still not been done — flagged again, now overdue.

---

## 7. Other open items carried forward

| Ticker | Status | Carried from | This session's note |
|---|---|---|---|
| **RGL** | Ungoverned position, live order still open | [2026-07-01](2026-07-01-rebalance.md) §0 | **2nd consecutive session, unresolved 3 calendar days.** No new fills since 07-01; order still `PARTIALLY_FILLED`, 57,214 sh remaining. Recommend immediate TWS/Client Portal review. |
| **MBGL** | Ungoverned position, likely corporate-action-sourced | [2026-07-01](2026-07-01-rebalance.md) §0 | **2nd consecutive session.** Still needs source investigation ($20.93, low urgency). |
| **AVGO** | Score 69.5, predates 2026-06-20 modifier, 3.86% | [2026-07-01](2026-07-01-rebalance.md) §7 | **4th consecutive session.** [watchlist/STALE.md](../watchlist/STALE.md) contradiction and missing 2026-06-16 override rationale both still unresolved. |
| **STIM** | "Not scored — going-concern override," 1.18% | [2026-06-07](2026-06-07-rebalance.md) §6 | **6th consecutive session unaddressed.** Standing Phase 06 exit-review trigger, independent of the monthly cycle. |
| **RBRK** | "Not scored — fails quality gates," 0.43% | [2026-06-07](2026-06-07-rebalance.md) §6 | **6th consecutive session unaddressed.** Needs an `override-log.md` entry. |
| **TLT** | 28.75%, non-equity, no methodology | [2026-06-07](2026-06-07-rebalance.md) §6 | See §4 — 6 consecutive sessions carried forward. |
| **NKE — Turnaround Sub-Gate formalization** | Recommendation overdue | [2026-07-01](2026-07-01-rescore-nke.md) | Still not converted to a formal Upgrade 4 entry, now 3 consecutive rescores overdue (§6). |

*(VEEV, previously carried forward 4 consecutive sessions needing `/rescore`, is now resolved — first-ever score computed 2026-07-01, and is a recycling destination this session, §5.)*

---

## 8. Summary table — proposed actions

| Ticker | Score | Weight | Proposed action | Driven by |
|---|---|---|---|---|
| **RGL** | not scored | 0.03% | **Urgent: verify/cancel the live 60,000-share GTC order in TWS/Client Portal — 3 days open, 2nd consecutive session flagged** | Governance — ungoverned position (§0) |
| **MBGL** | not scored | 0.04% | Investigate source (likely corporate action); no action pending that | Governance — ungoverned position (§0) |
| **AMZN** | 73.4 | 9.69% | Trim 6–7 sh from IBKR leg (~$1,450–$1,692, ~26–30%) → recycle | Valuation (Phase 05) |
| **CSGP** | 79.0 | 1.29% | Trim 7 sh (~$209, 28%) → recycle | Valuation (Phase 05) |
| **GOOG** | 73.1 | 0.62% | Trim triggered but not executable (1 sh); standing sell-limit @ $389 unchanged | Valuation (Phase 05) — execution gap |
| **SPOT** | 80.5 | 0.82% | Trim triggered but not executable (1 sh); standing sell-limit @ $518 unchanged | Valuation (Phase 05) — execution gap |
| **MSFT** | 33.9 | 14.63% | Hold — under cap by $216.59, no trim needed | Concentration (Upgrade 7) — watch |
| **TLT** | n/a | 28.75% | No action — unresolved structural gap, 6th consecutive session | Framework gap |
| **ADBE** | 0.0 | 3.69% | Recycling destination: $1,494.78 completes the 17-sh target | Recycling (Phase 05) |
| **TRN** | 10.0 | 3.05% | Recycling destination (~$2,801 gap); allocation deferred pending TWS order verification, 5th consecutive session | Recycling (Phase 05) — order-status caveat |
| **VEEV** | Composite 29.7 | 0.96% | **New recycling destination** (~$3,097 gap to risk-based target); flagged marginal/boundary-sitting signal — consider a smaller first tranche | Recycling (Phase 05) — new, marginal signal |
| **META** | Composite 22.8 | 7.31% | Qualifies on Composite, zero executable headroom to 8% ceiling | Recycling (Phase 05) — sizing gap |
| **AVGO** | 69.5 (stale) | 3.86% | No action — methodology-stale, missing override rationale, 4th consecutive session | Data integrity / governance |
| DUOL, NFLX, NOW, NVDA, UBER, V, ZS, NKE, NVO, SPGI | 30.0–69.9 | ~19.5% combined | Hold — Cheap/Fair Value bands, no trim | Valuation (Phase 05) |
| STIM, RBRK | not scored | 1.61% combined | Carried forward, 6th consecutive session | Fundamental (Phase 06) / governance |

**Recommended sequencing:**
1. **Resolve RGL first** — verify the live 60,000-share order in TWS/Client Portal; cancel if unintended, or supply rationale — now 3 calendar days open.
2. Run `/sync-portfolio` to bring `holdings.md` current (onboards or removes RGL/MBGL, refreshes cash/FX; now 4 days stale).
3. Execute (or re-propose) the AMZN/CSGP trims; route $1,494.78 of proceeds to ADBE; decide Option A/B/C for the ≈$164–406 remainder (§5).
4. Verify the TRN `REPLACED` 900-share order in TWS/Client Portal (now 5 sessions overdue).
5. Resolve the AVGO data-integrity flag and the RBRK override-log gap (both overdue 4–6 sessions).
6. Formalize NKE's Turnaround Sub-Gate entry (§6, overdue 3 consecutive rescores).
7. TLT's structural gap remains a standalone framework-development item (6 consecutive sessions carried forward).

*Session complete. No trades executed — this is a proposal for human review. Log any executed trims/exits in `decisions/` and refresh `holdings.md` via `/sync-portfolio` once they settle.*

---

## Glossary

- **Composite Score:** this framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50, computed only once a company clears the 80.0+ Quality Score gate; drives Phase 03/05 action-table lookups once it exists — see [quality-scoring.md](../framework/quality-scoring.md).
- **FX (foreign exchange) rate:** the price of converting one currency into another; this framework only uses live, broker-reported FX rates, never an assumed rate, per Rule 0.
- **GBX / pence (GBp):** one-hundredth of one British pound; TRN (LSE) quotes in GBX.
- **GTC (Good-Til-Cancelled):** an order instruction telling the broker to keep a limit order open indefinitely until it fills or is manually cancelled — the mechanism by which the RGL order (§0) keeps buying unattended.
- **Human Override:** a position opened or held outside the framework's own rules. Tracked for life in `override-log.md`.
- **Hybrid Upgrade:** one of 7 framework-specific rule additions layered on the base 6-phase strategy (Upgrade 4 = Turnaround Sub-Gate, Upgrade 7 = the 15% position cap).
- **NLV (Net Liquidation Value) / NAV (Net Asset Valuation):** a broker's headline account value — all positions at current market price, plus cash, minus liabilities (IBKR calls this NLV, Freedom24 calls it NAV).
- **Partial fill:** when a limit order executes for less than its full requested quantity — the mechanism behind RGL's 2,786-of-60,000 fill, TRN's 600-of-1,553 fill, and ADBE's 10-of-17 fill.
- **Quality Score:** this framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02.
- **R/R (Risk/Reward ratio):** (expected gain) ÷ (expected loss) on a trade; this framework requires at least 2:1 before entering.
- **REPLACED (order status):** an IBKR order-lifecycle status meaning the order was superseded by a new order; doesn't by itself confirm whether a replacement filled, is still working, or was cancelled.
- **Turnaround Sub-Gate:** the conditional path (Hybrid Upgrade 4) letting a company failing some quality criteria still enter as a small (2–3%) position if it passes 5 specific tests.
- **Valuation score:** this framework's 0.0–100.0 continuous score (0.0 = cheapest, 100.0 = most expensive).
- **Watchlist (action band):** the framework's recommendation for a valuation score of 50.0–69.9: fairly-to-fully valued, "no new entry." (Distinct from the repo's `watchlist/` directory.)

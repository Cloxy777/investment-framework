# 2026-07-06 — Rebalance Session (Monthly Rebalance / Trim Review)

**Task type:** REBALANCE
**Scope:** Portfolio-wide trim/hold/exit review across [holdings.md](../portfolio/holdings.md), applying Phase 05 (Dynamic Trimming) and Phase 06 (Exit Triggers) from [strategy.md](../framework/strategy.md) to current scores, the Upgrade 7 15% single-position cap, and the Upgrade 4 Turnaround Sub-Gate review-due check. **This is Routine 5's first-Monday-of-the-month Monthly Rebalance / Trim Review** ([automation-schedule.md](../framework/automation-schedule.md)), following a run of daily ad hoc sessions ([2026-07-01](2026-07-01-rebalance.md) through [2026-07-04](2026-07-04-rebalance.md)).

**No trades executed. This is a proposal for human review only.**

---

## 0. Rule 0 — live data pull, and two new developments since the 2026-07-05 sync

Per Rule 0, this session pulled `get_account_positions` / `get_account_balances` / `get_account_orders` / `get_account_trades` (`DAYS_7`) directly rather than relying solely on [holdings.md](../portfolio/holdings.md) (last full sync 2026-07-05; Freedom24 leg last screenshot 2026-06-07, unchanged). **Share counts for every scored equity are unchanged from the 07-05 sync** — the Composite/Valuation scores and bands below are current and safe to use. Two things changed:

### ⚠️⚠️ RGL's ungoverned order has now FULLY FILLED — the escalation flagged every session since 2026-07-01 has completed

`get_account_trades` (`DAYS_7`) shows the remaining 57,214 shares of RGL's 60,000-share GTC order (`order_id 630395618`) filled **2026-07-06T01:56:58Z**, overnight. `get_account_positions` confirms: **RGL position is now the full 60,000 shares** (was 2,786 as of the 07-05 sync), market value AUD $600.00 (≈ **$415.87 USD** at the live 0.6931166 rate). This is still a **≈0.71%** position (immaterial to sizing/cap math), but it is the first of this repo's recurring governance flags (AVGO, RGL, MBGL, the META 1-share orders, HDSN/MA/V/PDD/NOW) to go from "still working, could still be cancelled" to **fully executed with no Phase 01/02 evaluation ever run and no rationale ever supplied** — RiversGold Ltd is an ASX micro-cap gold explorer, about as far from this framework's quality-gate criteria (net margin >15%, ROIC >15%, 3+ years positive FCF) as a name can get.

**Side effect worth flagging alongside it:** `get_account_balances` now shows the **AUD cash balance at –$666.42** (net liquidation value for the AUD leg: –$83.65) — the RGL fill overdrew AUD cash into negative territory. This is a small-dollar item in absolute terms but is a genuine negative-cash/margin-usage event traceable directly to an unauthorized order, which is exactly the kind of exposure [/safe-guard](../.claude/commands/safe-guard.md) is designed to catch — recommend that routine's next run specifically check this AUD sub-balance.

### ⚠️ New order this morning — NVDA, partially but not exactly consistent with documented guidance

A new order appeared, placed **2026-07-06T07:54:29Z** (after the 07-05 close-out, same morning as this session): `order_id 639965927`, **BUY 5 NVDA @ $191.55 LIMIT, GTC**. This is the first of the recurring undocumented-order pattern (HDSN, MA, V, PDD, the NOW duplicate, the four-then-more META 1-share orders) that is **directionally consistent** with an actual documented recommendation: [2026-07-05's NVDA rescore](2026-07-05-rescore-nvda.md) concluded "**CONFIRMED BUY — top up ~4 shares (~$779, to reach an 18-share / 6.39% target)**" at a buy-price ceiling of $237.60, R/R 2.13:1. The new order's limit ($191.55, below both live price ~$195.50 and the $237.60 ceiling) is more conservative than the ceiling, but the **quantity (5 vs. the documented 4) and exact limit price don't match any figure written down in the session** — so, same as V/PDD before it, there's no exact rationale on record for *these specific* terms, even though the general direction (buy NVDA) has a documented, passing basis. Flagged for the user to confirm this is a deliberate manual execution of the 07-05 recommendation (with rounding) rather than a repeat of the unauthorized-order pattern.

### Carried forward, unchanged since 2026-07-05 (see [override-log.md](../portfolio/override-log.md) and prior rebalance sessions for full detail)

- **HDSN** BUY 200 @ $4.96 — contradicts the [2026-07-03 new-position PASS](2026-07-03-new-position-hdsn.md) (Quality Score 24.7, needs 80.0+); no order should exist.
- **MA** BUY 4 @ $464.00 — contradicts the [2026-06-22 rescore](../watchlist/not-in-portfolio/MA/MA-2026-06-22.md) ("Trade does NOT execute," R/R 1.33:1).
- **V** BUY 9 @ $285.00 — contradicts the [2026-07-05 rescore](2026-07-05-rescore-v.md) (HOLD, R/R fails 2:1).
- **PDD** BUY 10 @ $72.55 — doesn't match the [2026-07-01 new-position](2026-07-01-new-position-pdd.md) sizing (~44 sh at a $128.74 ceiling).
- **NOW** BUY 20 @ $80.00 — a straight duplicate of an order live since 2026-06-25.
- **META** — now five orders total (2 buy, 3 sell, one a `REPLACED` self-replace), none with any rationale on record anywhere in this repo.
- **AVGO** override-log's "Open — under review" status line is stale text (the 2026-07-04 rescore resolved the score itself: Quality 82.1, Composite 43.1) — still not corrected, 6th consecutive session.
- **RBRK, STIM** — still carry no `override-log.md` entry despite standing exit-review flags, 8th consecutive month.
- **TLT** — still exceeds the 15% cap with no fixed-income sizing/valuation methodology (see §4).

**None of HDSN/MA/V/PDD/NOW/META have filled.** No tool in this repo places, modifies, or cancels a broker order — this remains for the user to resolve directly in TWS/Client Portal.

---

## 1. Staleness check (operating-calendar.md)

**Every scored holding carries a Last Review date of 01–05 Jul 2026** — all fresh, all post-dating the 2026-06-29 Quality Score/Composite methodology change, so no watchlist-methodology staleness remains among held names (the last four — AMZN, CSGP, GOOG, SPOT — cleared it on 2026-07-05, see §2).

**Earnings-based staleness cannot be independently confirmed this session.** The [2026-07-05 weekly sync](weekly-briefs/2026-07-05-weekly-brief.md) already reported a data-gap: `yfinance`'s TLS handshake fails through this environment's egress proxy, and a plain-`requests` fallback against Yahoo hit a `401 Invalid Crumb`. No earnings dates are guessed or carried forward from memory per Rule 0. That sync also confirmed **no open `rescore-due` GitHub issue** exists, so there is no known pending earnings-triggered re-score — but this is an inherited gap, not an independent confirmation. Recommend the next `/healthcheck` (Routine 7, daily) verify whether the proxy/TLS issue has cleared.

**Conclusion: no holding is flagged as stale this session.**

---

## 2. Phase 05 — Dynamic Trimming

### 🎯 Headline finding: zero trim triggers fire this month — a reversal from every session since 2026-06-20

The last six sessions (through 2026-07-04) carried a standing caveat: AMZN, CSGP, GOOG, and SPOT all sat in the 70.0+ "Expensive"/"Very Expensive" trim bands **on raw Valuation Score alone**, with Quality Score still `?` — provisional pending rescore. Between 2026-07-04 and 2026-07-05, **all four were rescored** ([sessions/2026-07-05-rescore-*.md](.)) and now carry real Quality Scores. Exactly as happened with META in June, folding in Quality pulled every one of them **out of the trim band**:

| Ticker | Valuation Score (old lookup) | Quality Score (new) | **Composite Score (correct lookup)** | Band |
|---|---|---|---|---|
| AMZN | 81.8 | 57.6 | **62.1** | 50.0–69.9 Fair Value — no trim |
| CSGP | 80.5 | 68.4 | **56.1** | 50.0–69.9 Fair Value — no trim |
| GOOG | 67.4 | 73.7 | **46.9** | 30.0–49.9 Cheap — no trim |
| SPOT | 84.2 | 73.2 | **55.5** | 50.0–69.9 Fair Value — no trim |

Per [strategy.md](../framework/strategy.md) §"Phase 03/05," once a Quality Score exists the **Composite Score is the correct lookup**, not the raw Valuation Score. **This confirms the exact concern flagged provisionally for the last six sessions** — the "expensive" reading on these four names was an artifact of using Valuation Score alone; on the framework's own blended metric, none of them are actually rich.

### Full board check — no ticker sits at Composite (or Valuation, where Composite doesn't yet exist) ≥70.0

| Band | Tickers |
|---|---|
| 70.0–79.9 (trim 25–30%) | **None** |
| 80.0–89.9 (trim to 50%) | **None** |
| 90.0–100.0 (trim to 1–2%) | **None** |
| 50.0–69.9 (hold, watch only) | AMZN (62.1), CSGP (56.1), SPOT (55.5), NVO (47.6)* |
| 30.0–49.9 (hold, Cheap) | AVGO (43.1), DUOL (36.4), GOOG (46.9), NFLX (43.0), NKE (34.8, override — quality-gate fail), NOW (41.3), SPGI (34.6), UBER (40.3), ZS (41.9, override — quality-gate fail) |
| 0.0–29.9 (Very Cheap — recycling candidates) | ADBE (8.1), META (22.8), MSFT (28.6), NVDA (21.3), TRN (21.4), V (29.3, boundary), VEEV (29.7, boundary) |

*NVO's 47.6 sits just under the 50.0 Watchlist line per holdings.md's rounding — treated here in the Cheap band, no trim either way; flagged for precision, not a substantive dispute.

**Result: no trim executes or is even proposed this month.** No Phase 05 action is needed on any held equity.

---

## 3. Phase 06 — Full Exit Triggers

**None fired.** The highest Composite Score on the book is AMZN at 62.1 — nowhere near the 90.0–100.0 sustained-2-quarters exit trigger. No fundamental-deterioration, growth-thesis-broken, or balance-sheet-crisis trigger surfaced this session either.

RGL remains outside Phase 06's scope (never entered under Phase 01–03 — see §0, a governance case, not a valuation-driven exit). STIM and RBRK carry pre-existing, carried-forward exit-review flags (8th consecutive month unaddressed — see §7).

---

## 4. Upgrade 7 — 15% Single-Position Cap Check

Using [holdings.md](../portfolio/holdings.md)'s 2026-07-05 combined total ($58,226.21; live IBKR NLV this morning is $43,049.87 vs. $43,102.67 at the 07-05 sync, an immaterial –$52.80 intraday move — no share-count changes among scored equities, see §0): **15% cap = $8,733.93.**

| Ticker | Weight | Value (2026-07-05 sync) | Breach? | Action required |
|---|---|---|---|---|
| **MSFT** | 14.84% | $8,640.77 | **No — still tight** (~$93 of headroom) | 6th consecutive session hovering at/near the cap. No trim needed or recommended, continued monitoring warranted. |
| **TLT** | 28.54% | $16,617.76 | **Yes — by ~$7,884** | **8th consecutive month carried forward**, no new finding. Framework still has no fixed-income valuation/sizing methodology (logged in [override-log.md](../portfolio/override-log.md)). Repeating the recommendation from the last two sessions: this should graduate from a routine monthly re-flag to a dedicated framework-development session. |
| All others | ≤9.65% | — | No | — |

---

## 5. Recycling Plan

Per Phase 05, "proceeds always reinvested into current Score 0.0–29.9 names only." **Since no trim fired this month (§2), there are no trim proceeds to recycle.** For visibility, the current 0.0–29.9 "Very Cheap" qualifying destinations, should proceeds become available from any future trim or fresh capital:

| Ticker | Composite Score | Notes |
|---|---|---|
| ADBE | 8.1 | Documented ~17-share target from the [2026-06-12 new-position session](2026-06-12-new-position-adbe.md); 7 shares (~$1,538) still open. |
| NVDA | 21.3 | First-ever Quality Score (91.7) computed 2026-07-05; [rescore session](2026-07-05-rescore-nvda.md) recommends topping up ~4 sh to an 18-sh/6.39% target — see §0 for the new order that's directionally consistent but not an exact match. |
| META | 22.8 | Zero executable headroom to its 8% Phase 03 ceiling (combined value already above $4,658.10 ceiling minus <$560 room) — not a usable destination this cycle. |
| TRN | 21.4 | Large remaining gap to its documented target; standing `REPLACED` 900-share order still needs manual TWS/Client Portal verification. |
| MSFT | 28.6 | **New this session** — previously 33.9 (Cheap band); the 2026-07-05 rescore's Quality Score (78.3) pulled its Composite down to 28.6, a Very Cheap read. Already at the 15% cap (§4) — not a usable destination regardless of score. |
| V | 29.3 | Boundary (Composite 29.3, just inside 0.0–29.9); single-share position, an undocumented 9-share buy order is already live (§0) with no valid R/R on record — do not add mechanically pending that resolution. |
| VEEV | 29.7 | Marginal/boundary result per the [2026-07-01 rescore](2026-07-01-rescore-veev.md)'s own caveat ("a marginal, boundary-sitting result, not a robust one"). Flag for a deliberate human sizing decision, not mechanical recycling. |

**No allocation is proposed this month** — this table exists purely so the next session (or the next trim) has a ready reference, not as an action item.

---

## 6. Upgrade 4 — Turnaround Sub-Gate Review Check

Searched [override-log.md](../portfolio/override-log.md) and every file under `decisions/` for any position **entered** under the Turnaround Sub-Gate ("Conditional Watch, 2–3% max," mandatory 2-quarter review). No hits beyond the rule's own description (the automation-schedule and glossary-formatting entries) — no position has ever actually been logged as entered under this gate.

**Result: none found — same conclusion as all seven prior months. No turnaround-review-due items this month.**

**Carried-forward recommendation, still not actioned (5th consecutive cycle):** NKE's [2026-07-01 rescore](2026-07-01-rescore-nke.md) §10 recommends formally converting NKE's standing value-trap override into a documented Upgrade 4 Turnaround Sub-Gate entry + `override-log.md` row. Still not done.

---

## 7. Other open items carried forward

| Ticker/Item | Status | Carried from | This session's note |
|---|---|---|---|
| **RGL** | **Order fully filled overnight — position now 60,000 sh** | [2026-07-01](2026-07-01-rebalance.md) §0 | **See §0 — the escalation is now complete, not just pending.** No Phase 01/02 evaluation ever existed for this ticker. Recommend urgent user review: was this fill intended? |
| **NVDA (new order)** | 5-sh @ $191.55 GTC, placed this morning | New this session | **See §0.** Directionally consistent with the 07-05 CONFIRMED BUY recommendation, but exact terms (qty, price) aren't on record — confirm intent. |
| **HDSN / MA / V / PDD / NOW-dup / META (×5)** | Unfilled, undocumented orders | [2026-07-05 weekly brief](weekly-briefs/2026-07-05-weekly-brief.md) | Unchanged, still `NEW`, none filled. Same recommendation: confirm or cancel each in TWS/Client Portal. |
| **MBGL** | Ungoverned position, likely corporate-action-sourced | [2026-07-01](2026-07-01-rebalance.md) §0 | Unchanged, still uninvestigated ($19.45, low urgency). |
| **AVGO** | Score current (Composite 43.1) but override-log status text stale | [2026-06-22](2026-06-22-rebalance.md) §7 | **6th consecutive month** — override rationale still not on record; status line still reads "Open — under review" despite the score being resolved. |
| **STIM** | "Not scored — going-concern override," 1.21% | [2026-06-07](2026-06-07-rebalance.md) §6 | **8th consecutive month unaddressed.** Standing Phase 06 exit-review trigger, independent of the monthly cycle. |
| **RBRK** | "Not scored — fails quality gates," 0.43% | [2026-06-07](2026-06-07-rebalance.md) §6 | **8th consecutive month unaddressed.** Needs an `override-log.md` entry. |
| **TLT** | 28.54%, non-equity, no methodology | [2026-06-07](2026-06-07-rebalance.md) §6 | See §4 — 8 consecutive months carried forward. |
| **AUD cash balance** | –$666.42 (new) | New this session | Side effect of the RGL fill (§0) — flagging for `/safe-guard`'s next run. |

---

## 8. Summary table — proposed actions

| Ticker/Item | Score | Weight | Proposed action | Driven by |
|---|---|---|---|---|
| **RGL** | not scored | ~0.71% | **Urgent — confirm whether the overnight full fill (57,214 sh) was intended; the order is now closed out, not cancellable** | Governance — ungoverned position, now fully executed |
| **NVDA (new order)** | Composite 21.3 | 4.68% (pre-fill) | Confirm the 5-sh/$191.55 order's exact terms against the 07-05 CONFIRMED BUY recommendation (4 sh/$237.60 ceiling) | Governance — order doesn't exactly match documented sizing |
| **HDSN, MA, V, PDD, NOW (dup), META (×5)** | n/a | n/a | Confirm or cancel each undocumented order in TWS/Client Portal | Governance — unauthorized order pattern |
| **AMZN, CSGP, GOOG, SPOT** | Composite 62.1 / 56.1 / 46.9 / 55.5 | 9.65% / 1.29% / 0.61% / 0.84% | **Hold — no trim.** Prior months' provisional 70.0+ trim triggers resolved downward once Quality Score computed 07-05 | Phase 05 — Composite Score now current |
| **MSFT** | Composite 28.6 | 14.84% | Hold — no trim; cap headroom thin (~$93) | Concentration (Upgrade 7) — monitor |
| **TLT** | n/a | 28.54% | No action — unresolved structural gap, 8th consecutive month | Framework gap |
| All other held equities | 0.0–49.9 bands | ~24% combined | Hold — no trim | Phase 05 |
| **AVGO** | Composite 43.1 (current) | 3.73% | No valuation action — override-log status text still stale, 6th month | Governance |
| **NKE** | Composite 34.8 (Quality 44.4 fails gate) | 1.51% | Hold existing, do not add; formalize Turnaround Sub-Gate entry (5th month overdue) | Governance / Upgrade 4 |
| STIM, RBRK | not scored | 1.64% combined | Carried forward, 8th consecutive month | Fundamental (Phase 06) / governance |
| **Recycling plan** | — | — | None proposed — no trim proceeds this month; reference table only (§5) | Phase 05 |

**Recommended sequencing:**
1. **Confirm the RGL overnight full fill** — the single most urgent item this session, since (unlike prior months) it's no longer a standing order that can simply be cancelled; the position is now real and full-sized.
2. Confirm intent on the new NVDA order (§0) and the six still-unfilled undocumented orders (HDSN/MA/V/PDD/NOW-dup/META) in TWS/Client Portal.
3. No trim or exit action needed this month — Phase 05/06 are both clean, a first for this cycle.
4. Resolve the AVGO override-log text (6th month), the RBRK/STIM `override-log.md` gaps (8th month), and formalize NKE's Turnaround Sub-Gate entry (5th month).
5. TLT's 15% cap breach remains a standalone framework-development item (8 consecutive months carried forward) — recommend it graduate out of the routine monthly re-flag.

*Session complete. No trades executed — this is a proposal for human review. Log any executed trims/exits in `decisions/` and refresh `holdings.md` via `/sync-portfolio` once anything settles.*

---

## Glossary

- **Composite Score:** this framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; drives Phase 03/05 action-table lookups once a Quality Score exists — see [quality-scoring.md](../framework/quality-scoring.md).
- **FX (foreign exchange) rate:** the price of converting one currency into another; this framework only uses live, broker-reported FX rates, never an assumed rate, per Rule 0.
- **GTC (Good-Til-Cancelled):** an order instruction telling the broker to keep a limit order open indefinitely until it fills or is manually cancelled.
- **Human Override:** a position opened or held outside the framework's own rules. Tracked for life in `override-log.md`.
- **Hybrid Upgrade:** one of 7 framework-specific rule additions layered on the base 6-phase strategy (Upgrade 4 = Turnaround Sub-Gate, Upgrade 7 = the 15% position cap).
- **NLV (Net Liquidation Value) / NAV (Net Asset Valuation):** a broker's headline account value — all positions at current market price, plus cash, minus liabilities (IBKR calls this NLV, Freedom24 calls it NAV).
- **Quality Score:** this framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02.
- **R/R (Risk/Reward ratio):** (expected gain) ÷ (expected loss) on a trade; this framework requires at least 2:1 before entering.
- **REPLACED / PARTIALLY_FILLED (order status):** IBKR order-lifecycle statuses. `REPLACED` means the order was superseded by a new order; `PARTIALLY_FILLED` means some but not all of the order quantity has executed (RGL's order moved from this status to fully filled overnight — see §0).
- **Turnaround Sub-Gate:** the conditional path (Hybrid Upgrade 4) letting a company failing some quality criteria still enter as a small (2–3%) position if it passes 5 specific tests.
- **Valuation Score:** this framework's 0.0–100.0 continuous score (0.0 = cheapest, 100.0 = most expensive).
- **Watchlist (action band):** the framework's recommendation for a valuation score of 50.0–69.9: fairly-to-fully valued, "no new entry." (Distinct from the repo's `watchlist/` directory.)

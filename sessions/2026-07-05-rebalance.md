# 2026-07-05 — Rebalance Session

**Task type:** REBALANCE
**Scope:** Portfolio-wide trim/hold/exit review across [holdings.md](../portfolio/holdings.md), applying Phase 05 (Dynamic Trimming) and Phase 06 (Exit Triggers) from [strategy.md](../framework/strategy.md) to current scores, the Upgrade 7 15% single-position cap, and the Upgrade 4 Turnaround Sub-Gate review-due check. This is Routine 5's monthly Rebalance / Trim Review run ([automation-schedule.md](../framework/automation-schedule.md)), following [2026-07-01](2026-07-01-rebalance.md), [2026-07-03](2026-07-03-rebalance.md), and [2026-07-04](2026-07-04-rebalance.md).

**No trades executed. This is a proposal for human review only.**

---

## 0. Rule 0 — live data pull

Per Rule 0, this session pulled `get_account_positions` / `get_account_balances` / `get_account_orders` / `get_account_trades` directly rather than relying solely on `holdings.md` (last full IBKR sync 2026-06-28; Freedom24 last synced 2026-06-07, unchanged — no new screenshot this round).

**Account is financially static since the 2026-07-04 session** — IBKR Net Liquidation Value is unchanged to the cent ($43,102.65), no share-count changes across any of the 25 previously-tracked tickers, RGL, or MBGL, and `get_account_trades` (`DAYS_7`) shows no new fills since the 2026-07-01 RGL trades and 2026-06-30 EUR/GBP conversion. Combined portfolio total: **$58,226.19** (IBKR $43,102.65 + Freedom24 $15,123.54, unchanged).

**⚠️ New finding — an undocumented HDSN order was placed, directly contradicting this framework's own analysis.** A live GTC order appeared: `BUY 200 HDSN @ $4.96` (order ID 569919342, placed **2026-07-04T16:37:43Z**). This is materially different from the AVGO/RGL/META governance flags already on record — those had *no* evaluation at all. HDSN **does** have a session on record: [sessions/2026-07-03-new-position-hdsn.md](2026-07-03-new-position-hdsn.md), run the day before this order was placed, which computed a Quality Score of **24.7** (net margin 5.7%, ROIC 6.5%, 3yr revenue CAGR −8.8%, gross margin halved from 50%→24.6% in 3 years, negative trailing FCF) — **55.3 points under the 80.0 gate** — and concluded explicitly: *"PASS. Stop before Phase 02... No Phase 02 valuation score, fair value, or order setup is computed — doing so would violate the gate."* No Buy Price, Fair Value, or order setup was computed or recommended anywhere in that session. The order does not appear in `override-log.md`, `decisions/`, or any `sessions/` file. **Flagged for the user as the most urgent item this session** — this isn't a documentation gap like the other open governance flags, it's a live order that runs directly counter to a documented Quality Score gate failure. Recommend cancelling the order or supplying a rationale (and logging it in `override-log.md` as a quality waiver, per that log's own rule, if intentional) before it can fill.

Other carried-forward items, unchanged since 2026-07-04 (see §7 for full detail): the 4 undocumented 1-share META GTC orders (placed 2026-07-03, still no rationale on record) and RGL's `PENDING_CANCEL_REPLACE` order (id 630395618, still unresolved, now >48h since the cancel/replace was submitted).

Every held holding's Composite Score is unchanged from `holdings.md` — no `/rescore` or `/new-position` ran on a held name today before this session started (the AMZN/AVGO/CSGP/DUOL/GOOG/MSFT/NFLX/NOW/NVDA/NVO/SPGI Quality Score computations landed **before** today's session, closing out most of the gap the last two rebalance sessions had flagged — see §2).

| Ticker | Combined USD value (live) | Weight % | Score used | Type | Last Review | Band |
|---|---|---|---|---|---|---|
| ADBE | $2,197.10 | 3.77% | 8.1 | **Composite** | 04 Jul 2026 | 0.0–29.9 Very Cheap |
| AMZN | $5,618.70 | 9.65% | 62.1 | **Composite** | 04 Jul 2026 | 50.0–69.9 Fair Value |
| AVGO | $2,172.00 | 3.73% | 43.1 | **Composite** | 04 Jul 2026 | 30.0–49.9 Cheap |
| CSGP | $750.00 | 1.29% | 56.1 | **Composite** | 04 Jul 2026 | 50.0–69.9 Fair Value |
| DUOL | $4,627.84 | 7.95% | 36.4 | **Composite** | 04 Jul 2026 | 30.0–49.9 Cheap |
| GOOG | $355.11 | 0.61% | 46.9 | **Composite** | 04 Jul 2026 | 30.0–49.9 Cheap |
| **MBGL** | $19.80 | 0.03% | not scored — ungoverned, see §7 | — | n/a | special |
| META | $4,098.95 | 7.04% | 22.8 | Composite | 1 Jul 2026 | 0.0–29.9 Very Cheap |
| MSFT | $8,641.60 | 14.84% | 28.6 | **Composite** | 05 Jul 2026 | 0.0–29.9 Very Cheap |
| NFLX | $931.31 | 1.60% | 43.0 | **Composite** | 05 Jul 2026 | 30.0–49.9 Cheap |
| NKE | $881.80 | 1.51% | 34.8 (Quality 44.4 — **fails 80.0+ gate**) | Composite | 1 Jul 2026 | 30.0–49.9 Cheap (override — do NOT add) |
| NOW | $1,275.84 | 2.19% | 41.3 | **Composite** | 05 Jul 2026 | 30.0–49.9 Cheap |
| NVDA | $2,722.16 | 4.68% | 21.3 | **Composite** | 05 Jul 2026 | 0.0–29.9 Very Cheap |
| NVO | $252.15 | 0.43% | 47.6 | **Composite** | 05 Jul 2026 | 30.0–49.9 Cheap |
| RBRK | $250.26 | 0.43% | not scored — fails quality gates | — | Jun 2026 | special — see §7 |
| **RGL** | $21.27 | 0.04% | not scored — ungoverned, see §7 | — | n/a | special |
| SPGI | $433.80 | 0.75% | 34.6 | **Composite** | 05 Jul 2026 | 30.0–49.9 Cheap |
| SPOT | $489.86 | 0.84% | 80.5 (Quality Score still `?`) | Valuation (no Quality yet) | 20 Jun 2026 | 80.0–89.9 Very Expensive (provisional) |
| STIM | $705.00 | 1.21% | not scored — going-concern override | — | Jun 2026 | special — see §7 |
| TLT | $16,620.17 | 28.55% | not scored — non-equity | — | Jun 2026 | special — see §4 |
| TRN | $1,746.25 | 3.00% | 10.0 (Quality Score still `?`) | Valuation (no Quality yet) | 24 Jun 2026 | 0.0–29.9 Very Cheap (partial fill) |
| UBER | $223.05 | 0.38% | 34.8 (Quality Score still `?`) | Valuation (no Quality yet) | 20 Jun 2026 | 30.0–49.9 Cheap |
| V | $361.71 | 0.62% | 39.2 (Quality Score still `?`) | Valuation (no Quality yet) | 20 Jun 2026 | 30.0–49.9 Cheap |
| VEEV | $575.28 | 0.99% | 29.7 (Quality 85.7 — passes gate, marginal/boundary) | Composite | 01 Jul 2026 | 0.0–29.9 Very Cheap (boundary) |
| XEON | $1,710.97 | 2.94% | not scored — cash-equivalent | — | Jun 2026 | out of scope |
| ZS | $147.13 | 0.25% | 36.3 (Quality Score still `?`) | Valuation (no Quality yet) | 20 Jun 2026 | 30.0–49.9 Cheap (override — quality-gate fail, see override-log) |
| CASH (IBKR) | $342.67 | 0.59% | — | — | — | liquidity |
| CASH (Freedom24) | $106.85 | 0.18% | — | — | — | liquidity |

*STIM's weight above reflects the 500-share equity position only ($705.00); the short 5-contract covered call (market value −$50.00) is excluded, same convention as prior sessions.*

---

## 1. Staleness check (operating-calendar.md)

**None.** No holding has had an earnings release since its last review that hasn't already been re-scored. NKE (earnings 2026-06-30) was re-scored 2026-07-01 and is current. Per the [2026-06-28 weekly brief](weekly-briefs/2026-06-28-weekly-brief.md), the next earnings in the book are NFLX (2026-07-16), CSGP (2026-07-21), NOW (2026-07-22), GOOG (2026-07-23), SPOT/V (2026-07-28), META/MSFT (2026-07-29), AMZN/SPGI (2026-07-30) — none have occurred yet.

Separate from earnings-driven staleness, five holdings (SPOT, TRN, UBER, V, ZS) still lack a Quality Score under the 2026-06-29 methodology (tracked in [watchlist/STALE.md](../watchlist/STALE.md)) — down from 16 as of the 2026-07-04 session, now that AMZN, AVGO, CSGP, DUOL, GOOG, MSFT, NFLX, NOW, NVDA, NVO, and SPGI have all been rescored under the current methodology in the last two days.

---

## 2. Phase 05 — Dynamic Trimming

### ⚠️ Reversal from the last two sessions — read before the trim table

The 2026-07-03 and 2026-07-04 sessions each flagged **AMZN, CSGP, and GOOG** for a 25–30% trim, explicitly **provisional** pending each ticker's Quality Score — both sessions recommended `/rescore` on all four (AMZN, CSGP, GOOG, SPOT) before executing anything. All four have since been rescored (see git history: `461aec9`, `ead7c06`, `8ce8db6`, and SPOT still pending). **The Composite Score pulls three of the four out of the trim band entirely:**

| Ticker | Raw Valuation Score (used last session) | Quality Score (new) | Composite Score (new) | Band under Composite |
|---|---|---|---|---|
| AMZN | 73.4 (Expensive — trim 25–30%) | 57.6 (fails 80 gate) | **62.1** | **50.0–69.9 Fair Value — no trim** |
| CSGP | 79.0 (Expensive — trim 25–30%) | 68.4 (fails 80 gate) | **56.1** | **50.0–69.9 Fair Value — no trim** |
| GOOG | 73.1 (Expensive — trim 25–30%) | 73.7 (fails 80 gate) | **46.9** | **30.0–49.9 Cheap — no trim** |
| SPOT | 80.5 (Very Expensive — trim to 50%) | still `?` | still `?` | still provisional on raw score only |

This is exactly the outcome the caveat in the 2026-07-03/07-04 sessions warned was possible — a lower Quality Score (all three fail the 80.0+ gate) pulls the blended Composite down well below the raw Valuation Score's trim bands. **No trim should have been executed off last session's provisional numbers, and none was** (correctly — both sessions flagged this as "no trades executed, proposal only"). This is a good illustration of why Phase 05 requires the Composite Score, not the raw Valuation Score, once available.

### Trim 25–30% (Score 70.0–79.9)

**None.** (AMZN, CSGP, GOOG all cleared once their Composite Score applied — see reversal note above.)

### Trim to 50% (Score 80.0–89.9)

| Ticker | Score | Position | Trim to 50% | Reasoning |
|---|---|---|---|---|
| **SPOT** | 80.5 (raw Valuation — **Quality Score still not computed**, provisional) | $489.86 (1 sh, IBKR, live) | **Not executable** (1 sh) | "Very Expensive" band on raw score, unchanged since 2026-06-20. Standing GTC sell-limit confirmed still live: SELL 1 @ $518.00 (live $489.86). No change recommended. **Recommend `/rescore SPOT` before this trigger can be trusted** — same caveat that correctly flagged AMZN/CSGP/GOOG turned out to matter. |

### Trim to tracking (1–2%) — Score 90.0–100.0

None. No holding scores ≥90.0 on either raw Valuation Score or Composite Score.

### Hold, no trim — Fair Value and Cheap bands

AMZN (62.1), CSGP (56.1) sit in the 50.0–69.9 Fair Value band — hold, watch only, no trim. AVGO (43.1), DUOL (36.4), GOOG (46.9), MSFT (28.6 — Very Cheap, not trim-eligible), NFLX (43.0), NOW (41.3), NVDA (21.3 — Very Cheap), NVO (47.6), SPGI (34.6), UBER (34.8), V (39.2), ZS (36.3), NKE (34.8, override), ADBE (8.1), TRN (10.0), META (22.8), VEEV (29.7) all sit below 70.0 — hold, no trim.

---

## 3. Phase 06 — Full Exit Triggers

**None fired.** No holding sits in the 90.0–100.0 band on either raw Valuation Score or Composite Score, let alone sustained for 2+ quarters. No new fundamental-deterioration, thesis-broken, or balance-sheet-crisis triggers surfaced this session.

RGL and the new HDSN order (§0) are governance/override issues, not Phase 06 exit cases — neither ever passed Phase 01–03. STIM and RBRK carry pre-existing, carried-forward exit-review flags (§7).

---

## 4. Upgrade 7 — 15% Single-Position Cap Check

15% of $58,226.19 = **$8,733.93**.

| Ticker | Weight | Value (live) | Breach? | Action required |
|---|---|---|---|---|
| **MSFT** | 14.84% | $8,641.60 | **No — but tight** ($92.33 of headroom) | Now Very Cheap on Composite (28.6) — would otherwise be a BUY-band recycling destination, but cap headroom leaves no room to add. No trim needed. |
| **TLT** | 28.55% | $16,620.17 | **Yes — by $7,886.24** | **No new finding — 8th consecutive month carried forward** (2026-06-07 through 2026-07-04, now 07-05). Framework still has no fixed-income valuation/sizing methodology — logged in [override-log.md](../portfolio/override-log.md). Recommend this graduate from a routine carry-forward line to a dedicated framework-development session rather than continuing to re-flag it monthly with no path to resolution. |
| All others | ≤9.65% | — | No | — |

---

## 5. Recycling Plan

Per Phase 05 — "proceeds always reinvested into current Score 0.0–29.9 names only." **No trims fired this session (§2), so no new proceeds were generated.** This is a change from the last two sessions, which (incorrectly, on a provisional basis) assumed AMZN/CSGP trim proceeds would fund the recycling plan below.

**Held, currently-qualifying Score 0.0–29.9 destinations (all pre-existing, no new funding source):** ADBE (8.1), META (22.8), MSFT (28.6 — but at the 15% cap, no headroom), NVDA (21.3 — new addition to this list, its Composite Score having just cleared), TRN (10.0, raw score), VEEV (29.7, marginal/boundary).

**Idle cash on hand:** IBKR $342.67 + Freedom24 $106.85 = **$449.52 combined** — well short of ADBE's remaining ~$1,537.97 gap to its documented 17-share target, and not a Phase 05 "recycling proceeds" event in the strict sense (no trim occurred to generate it). Flagged for awareness only; recommend not mechanically deploying it without a deliberate sizing decision, consistent with how VEEV's marginal signal has been treated in prior sessions.

**No new destinations found.** Same watchlist sweep conclusion as 2026-07-04 — ORANY, OUST, and WBX all failed the Quality Score gate; PDD's pending order (still `NEW`/unfilled, order ID 1150965513) is a new-position buy, not a Phase 05 recycling destination; HDSN (§0) explicitly failed the gate and should not be treated as a destination at all — which makes the live HDSN buy order especially hard to reconcile with any documented rationale.

---

## 6. Upgrade 4 — Turnaround Sub-Gate Review Check

Searched [override-log.md](../portfolio/override-log.md) and every file under `decisions/` for any position **entered** under the Turnaround Sub-Gate ("Conditional Watch, 2–3% max," mandatory 2-quarter review). No hits beyond the routine-schedule and glossary-formatting entries describing the rule itself, not an entry made under it.

**Result: none found — same conclusion as all seven prior months.** No turnaround-review-due items this month.

**Carried-forward recommendation, still not actioned (now 5th consecutive cycle it's been raised):** NKE's [2026-07-01 rescore](2026-07-01-rescore-nke.md) §10 recommends formally converting NKE's standing value-trap override into a documented Upgrade 4 Turnaround Sub-Gate entry + `override-log.md` row. Still not done.

---

## 7. Other open items carried forward

| Ticker/Item | Status | Carried from | This session's note |
|---|---|---|---|
| **HDSN (new order)** | Live GTC buy order for a name that explicitly failed the Quality Score gate (24.7) one day earlier | **New this session** | **See §0 — most urgent item this session.** No rationale anywhere in the repo; recommend cancellation or an explicit override-log entry if intentional. |
| **META (new orders)** | 4 undocumented 1-share GTC orders (2 buy, 2 sell) | [2026-07-04](2026-07-04-rebalance.md) §0 | Unchanged, still no rationale on record. 2nd consecutive session flagged. |
| **RGL** | Ungoverned position; order still `PENDING_CANCEL_REPLACE`, now >48h | [2026-07-04](2026-07-04-rebalance.md) §0 | Unchanged — still not confirmed cancelled. Recommend confirming final order status in TWS/Client Portal. |
| **MBGL** | Ungoverned position, likely corporate-action-sourced | [2026-07-01](2026-07-01-rebalance.md) §0 | Unchanged, still uninvestigated ($19.80, low urgency). |
| **AVGO** | Composite 43.1 (Cheap), 3.73% | [2026-06-22](2026-06-22-rebalance.md) §7 | **6th consecutive month.** Rescored 2026-07-04 (resolves the stale-modifier flag), but the original 2026-06-16 override rationale is still not on record in [override-log.md](../portfolio/override-log.md). |
| **STIM** | "Not scored — going-concern override," 1.21% | [2026-06-07](2026-06-07-rebalance.md) §6 | **8th consecutive month unaddressed.** Standing Phase 06 exit-review trigger, independent of the monthly cycle. |
| **RBRK** | "Not scored — fails quality gates," 0.43% | [2026-06-07](2026-06-07-rebalance.md) §6 | **8th consecutive month unaddressed.** Needs an `override-log.md` entry. |
| **TLT** | 28.55%, non-equity, no methodology | [2026-06-07](2026-06-07-rebalance.md) §6 | See §4 — 8 consecutive months carried forward. |
| **CSGP / TLT standing orders** | `REPLACED`, no live successor (CSGP sell since 2026-05-26, TLT buy since 2026-06-01) | Prior sessions | Unchanged, now 6+ weeks stale. |
| **TRN 900-sh order** | `REPLACED`, `cum_shares_qty: 0`, no live successor | Prior sessions | Unchanged — still needs manual TWS/Client Portal verification. |

---

## 8. Summary table — proposed actions

| Ticker | Score | Weight | Proposed action | Driven by |
|---|---|---|---|---|
| **HDSN (new order)** | Quality 24.7 (fails gate) | n/a (unfilled) | **Cancel or justify** — order contradicts the session's own explicit FAIL recommendation | Governance — undocumented order contradicting a documented gate failure |
| **META (new orders)** | n/a | n/a | Confirm intent behind the 4 undocumented 1-share GTC orders | Governance — undocumented order activity |
| **RGL** | not scored | 0.04% | Confirm the `PENDING_CANCEL_REPLACE` order resolves to fully cancelled in TWS/Client Portal | Governance — ungoverned position |
| **MBGL** | not scored | 0.03% | Investigate source (likely corporate action); no action pending that | Governance — ungoverned position |
| **AMZN, CSGP, GOOG** | 62.1 / 56.1 / 46.9 (Composite) | 9.65% / 1.29% / 0.61% | **No trim** — reversed from provisional flags in the last two sessions now that Composite Score clears them (§2) | Valuation (Phase 05) |
| **SPOT** | 80.5 (raw, provisional) | 0.84% | Trim triggered but not executable (1 sh); standing sell-limit @ $518 unchanged; `/rescore SPOT` recommended before trusting this | Valuation (Phase 05) — data gap |
| **MSFT** | 28.6 (Composite) | 14.84% | Hold — Very Cheap on Composite but cap headroom too thin to add ($92.33) | Concentration (Upgrade 7) — monitor |
| **TLT** | n/a | 28.55% | No action — unresolved structural gap, 8th consecutive month | Framework gap |
| **ADBE, TRN, META, NVDA, VEEV** | 8.1 / 10.0 / 22.8 / 21.3 / 29.7 | combined ~19.3% | Qualifying Score 0.0–29.9 destinations, but **no trim proceeds generated this cycle** to fund them (§5); MSFT also qualifies but is cap-constrained | Recycling (Phase 05) — unfunded this cycle |
| **NKE** | Composite 34.8 (Quality 44.4 fails gate) | 1.51% | Hold existing, do not add; formalize Turnaround Sub-Gate entry (overdue, 5th cycle) | Governance / Upgrade 4 |
| **AVGO** | 43.1 (Composite) | 3.73% | No trim; original override rationale still missing (6th consecutive month) | Data integrity / governance |
| DUOL, NFLX, NOW, NVO, SPGI, UBER, V, ZS | 30.0–69.9 | ~18.2% combined | Hold — Cheap/Fair Value bands, no trim | Valuation (Phase 05) |
| STIM, RBRK | not scored | 1.64% combined | Carried forward, 8th consecutive month | Fundamental (Phase 06) / governance |

**Recommended sequencing:**
1. **Resolve the HDSN order (§0)** — either cancel it or document the rationale; this is the one item this session that looks like it may have bypassed the framework's own explicit gate failure, not just an undocumented-but-benign entry.
2. **Confirm the 4 META GTC orders** are intentional — same undocumented-order pattern, 2nd consecutive session.
3. **Confirm RGL's cancel/replace resolved** in TWS/Client Portal — now >48h pending.
4. No trim execution needed this cycle — the AMZN/CSGP/GOOG triggers from the last two sessions do not survive contact with their Composite Scores (§2); nothing to recycle.
5. Run `/rescore SPOT` to settle whether its provisional trim-to-50% actually holds once a Quality Score exists.
6. Verify the TRN 900-share and CSGP/TLT standing orders in TWS/Client Portal.
7. Resolve the AVGO and RBRK override-log gaps (6th–8th consecutive month).
8. Formalize NKE's Turnaround Sub-Gate entry in `override-log.md` (overdue 5 cycles).
9. TLT's structural gap remains a standalone framework-development item (8 consecutive months carried forward).

*Session complete. No trades executed — this is a proposal for human review. Log any executed trims/exits in `decisions/` and refresh `holdings.md` via `/sync-portfolio` once they settle.*

---

## Glossary

- **Composite Score:** this framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; drives Phase 03/05 action-table lookups once a Quality Score exists — see [quality-scoring.md](../framework/quality-scoring.md).
- **FX (foreign exchange) rate:** the price of converting one currency into another; this framework only uses live, broker-reported FX rates, never an assumed rate, per Rule 0.
- **GTC (Good-Til-Cancelled):** an order instruction telling the broker to keep a limit order open indefinitely until it fills or is manually cancelled.
- **Human Override:** a position (or, as flagged this session, a live but unfilled order) opened outside the framework's own rules. Tracked for life in `override-log.md`.
- **Hybrid Upgrade:** one of 7 framework-specific rule additions layered on the base 6-phase strategy (Upgrade 4 = Turnaround Sub-Gate, Upgrade 7 = the 15% position cap).
- **NLV (Net Liquidation Value) / NAV (Net Asset Valuation):** a broker's headline account value — all positions at current market price, plus cash, minus liabilities (IBKR calls this NLV, Freedom24 calls it NAV).
- **Quality Score:** this framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02.
- **PENDING_CANCEL_REPLACE / REPLACED (order status):** IBKR order-lifecycle statuses. `PENDING_CANCEL_REPLACE` means a cancel-and-replace instruction has been submitted but not yet confirmed by the exchange; `REPLACED` means the order was superseded by a new order (doesn't confirm whether the replacement filled or is still working).
- **Turnaround Sub-Gate:** the conditional path (Hybrid Upgrade 4) letting a company failing some quality criteria still enter as a small (2–3%) position if it passes 5 specific tests.
- **Valuation Score:** this framework's 0.0–100.0 continuous score (0.0 = cheapest, 100.0 = most expensive).
- **Watchlist (action band):** the framework's recommendation for a valuation score of 50.0–69.9: fairly-to-fully valued, "no new entry." (Distinct from the repo's `watchlist/` directory.)

# 2026-07-03 — Rebalance Session

**Task type:** REBALANCE
**Scope:** Portfolio-wide trim/hold/exit review across [holdings.md](../portfolio/holdings.md), applying Phase 05 (Dynamic Trimming) and Phase 06 (Exit Triggers) from [strategy.md](../framework/strategy.md) to current scores, the Upgrade 7 15% single-position cap, and the Upgrade 4 Turnaround Sub-Gate review-due check. This is Routine 5's monthly Rebalance / Trim Review run ([automation-schedule.md](../framework/automation-schedule.md)), following [2026-06-07](2026-06-07-rebalance.md), [2026-06-15](2026-06-15-rebalance.md), [2026-06-22](2026-06-22-rebalance.md), [2026-06-29](2026-06-29-rebalance.md), and [2026-07-01](2026-07-01-rebalance.md).

**No trades executed. This is a proposal for human review only.**

---

## 0. Rule 0 — live data pull

Per Rule 0 ("always fetch live prices first"), this session pulled `get_account_positions` / `get_account_balances` / `get_account_orders` / `get_account_trades` directly rather than relying solely on `holdings.md` (last full IBKR sync 2026-06-28; Freedom24 last synced 2026-06-07, unchanged).

**No share-count changes since the 2026-07-01 rebalance** across any of the 25 previously-tracked tickers, RGL, or MBGL — only prices, cash/FX, and one order status changed. Two items worth flagging:

- **RGL order status changed.** The still-live 60,000-share GTC buy order flagged as this framework's top priority item on 2026-07-01 (`order_id 630395618`, `PARTIALLY_FILLED`, 2,786 of 60,000 filled) now shows **`PENDING_CANCEL_REPLACE`** as of **2026-07-03T08:37:54Z** (this morning) — `cum_shares_qty` still 2,786, `remaining_shares_qty` still 57,214. This is consistent with someone having initiated a cancel/replace action on the order since the last session, but **it has not yet confirmed as cancelled** — the position is not growing further (no new RGL trades in the last 7 days per `get_account_trades`), but the order is not definitively closed either. Recommend confirming final resolution in TWS/Client Portal; do not treat this as resolved until the order shows `CANCELLED` or a final fill status.
- **A new pending order appeared:** `Buy 10 PDD @ $72.55` (GTC, placed 2026-07-02) — this follows the [2026-07-01 new-position PDD evaluation](2026-07-01-new-position-pdd.md). Not yet filled, so PDD is not a current holding and carries no rebalance action this session; noted for context only.

**MBGL** (1 share, $19.80, $0.00 cost basis) remains unchanged and still uninvestigated — carried forward from 2026-07-01, see §7.

**Combined total (broker-reported, live):** IBKR Net Liquidation Value **$43,134.55** (`get_account_balances`, BASE row) + Freedom24 Net Asset Valuation **$15,123.54** (last screenshot sync, 2026-06-07, unchanged) = **$58,258.09**.

Scores are unchanged from `holdings.md` for every ticker. `holdings.md` itself is current on scores as of this session — it already reflects the 2026-07-01 rescores of **NKE** (13.9 / Quality 44.4 / Composite 34.8), **VEEV** (45.1 / Quality 85.7 / Composite 29.7 — first-ever score), and **META** (35.6 / Quality 90.0 / Composite 22.8). Where a ticker has a computed Quality Score, this session uses the **Composite Score** for Phase 03/05 lookups per [strategy.md](../framework/strategy.md) ("Blend the Valuation Score with the Quality Score into a single Composite Score... before applying the Phase 03 and Phase 05 action tables"); where Quality Score is still `?`, this session falls back to the raw Valuation Score, same convention as the five prior rebalance sessions — see the important caveat on this in §2.

| Ticker | Combined USD value (live) | Weight % | Score used | Type | Last Review | Band |
|---|---|---|---|---|---|---|
| ADBE | $2,197.10 | 3.77% | 0.0 | Valuation (no Quality yet) | 20 Jun 2026 | 0.0–29.9 Very Cheap |
| AMZN | $5,618.70 | 9.65% | 73.4 | Valuation (no Quality yet) | 20 Jun 2026 | 70.0–79.9 Expensive |
| AVGO | $2,172.00 | 3.73% | 69.5 (**stale — predates 2026-06-20 modifier**) | Valuation (no Quality yet) | 14 Jun 2026 | see §7 |
| CSGP | $750.00 | 1.29% | 79.0 | Valuation (no Quality yet) | 20 Jun 2026 | 70.0–79.9 Expensive |
| DUOL | $4,627.84 | 7.94% | 53.7 | Valuation (no Quality yet) | 20 Jun 2026 | 50.0–69.9 Fair Value |
| GOOG | $355.11 | 0.61% | 73.1 | Valuation (no Quality yet) | 20 Jun 2026 | 70.0–79.9 Expensive |
| **MBGL** | $19.80 | 0.03% | not scored — ungoverned, see §7 | — | n/a | special |
| META | $4,098.95 | 7.04% | **22.8** | **Composite** | 1 Jul 2026 | 0.0–29.9 Very Cheap |
| MSFT | $8,641.60 | 14.84% | 33.9 | Valuation (no Quality yet) | 26 Jun 2026 | 30.0–49.9 Cheap |
| NFLX | $931.31 | 1.60% | 61.2 | Valuation (no Quality yet) | 20 Jun 2026 | 50.0–69.9 Fair Value |
| NKE | $881.80 | 1.51% | **34.8** (Quality 44.4 — **fails 80.0+ gate**) | **Composite** | 1 Jul 2026 | 30.0–49.9 Cheap (override — do NOT add) |
| NOW | $1,275.84 | 2.19% | 42.3 | Valuation (no Quality yet) | 20 Jun 2026 | 30.0–49.9 Cheap |
| NVDA | $2,722.16 | 4.67% | 48.5 | Valuation (no Quality yet) | 20 Jun 2026 | 30.0–49.9 Cheap |
| NVO | $252.15 | 0.43% | 47.6 | Valuation (no Quality yet) | 20 Jun 2026 | 30.0–49.9 Cheap |
| RBRK | $250.26 | 0.43% | not scored — fails quality gates | — | Jun 2026 | special — see §7 |
| **RGL** | $21.29 | 0.04% | not scored — ungoverned, see §7 | — | n/a | special |
| SPGI | $433.80 | 0.74% | 33.4 | Valuation (no Quality yet) | 20 Jun 2026 | 30.0–49.9 Cheap |
| SPOT | $489.86 | 0.84% | 80.5 | Valuation (no Quality yet) | 20 Jun 2026 | 80.0–89.9 Very Expensive |
| STIM | $705.00 | 1.21% | not scored — going-concern override | — | Jun 2026 | special — see §7 |
| TLT | $16,620.17 | 28.53% | not scored — non-equity | — | Jun 2026 | special — see §4 |
| TRN | $1,775.97 | 3.05% | 10.0 | Valuation (no Quality yet) | 24 Jun 2026 | 0.0–29.9 Very Cheap (partial fill) |
| UBER | $223.05 | 0.38% | 34.8 | Valuation (no Quality yet) | 20 Jun 2026 | 30.0–49.9 Cheap |
| V | $361.71 | 0.62% | 39.2 | Valuation (no Quality yet) | 20 Jun 2026 | 30.0–49.9 Cheap |
| VEEV | $575.28 | 0.99% | **29.7** (Quality 85.7 — passes gate, but **marginal/boundary**, see §5) | **Composite** | 1 Jul 2026 | 0.0–29.9 Very Cheap (boundary) |
| XEON | $1,712.40 | 2.94% | not scored — cash-equivalent | — | Jun 2026 | out of scope |
| ZS | $147.13 | 0.25% | 36.3 | Valuation (no Quality yet) | 20 Jun 2026 | 30.0–49.9 Cheap (override — quality-gate fail, see override-log) |
| CASH (IBKR) | $342.93 | 0.59% | — | — | — | liquidity |
| CASH (Freedom24) | $106.85 | 0.18% | — | — | — | liquidity |

*STIM's weight above reflects the 500-share equity position only ($705.00); the short 5-contract covered call (market value −$50.00) is excluded, same convention as prior sessions.*

---

## 1. Staleness check (operating-calendar.md)

No holding shows a confirmed earnings release since its last review that hasn't yet been re-scored — the last three earnings-driven re-scores (NKE, META, MSFT/META window) are all reflected in current scores. Two staleness flags carry forward, both **methodology** staleness rather than earnings staleness:

1. **AVGO (69.5, scored 14 Jun 2026)** predates the 2026-06-20 Upside/Downside Modifier — see §7. Needs `/rescore AVGO` before its band assignment can be trusted.
2. **16 in-portfolio holdings still show `?` for Quality Score / Composite Score** under the 2026-06-29 methodology change (ADBE, AMZN, AVGO, CSGP, DUOL, GOOG, MSFT, NFLX, NOW, NVDA, NVO, SPGI, SPOT, TRN, UBER, V, ZS — full list also tracked in [watchlist/STALE.md](../watchlist/STALE.md)). This is not cosmetic this month — see the caveat in §2 below, since four of today's trim triggers come from this exact set.

---

## 2. Phase 05 — Dynamic Trimming

### ⚠️ Important caveat before the trim table

Per [strategy.md](../framework/strategy.md), Phase 05 trim triggers should be evaluated on the **Composite Score**, not the raw Valuation Score, once a Quality Score exists. **AMZN, CSGP, GOOG, and SPOT — every trim trigger firing this session — all still show `Quality Score = ?`**, so the bands below use the raw Valuation Score only, same fallback convention this session inherited from the five prior rebalance runs. **This is not guaranteed to survive a rescore.** META is the live proof: its raw Valuation Score alone (35.6) would sit in the 30.0–49.9 Cheap band, cleanly out of any trim discussion — but that's not the trim-relevant example. The sharper illustration is that META's **Quality Score (90.0)** pulled its Composite *down* to 22.8, i.e. quality can move a name a full band once blended in. The same mechanism could just as easily pull AMZN/CSGP/GOOG/SPOT **out of** the 70.0+ trim bands (if their Quality Scores turn out high) or **confirm/deepen** the trim (if Quality Scores turn out mediocre) — there is no way to know which without running the actual Quality Score calculation, and this session will not invent one. **Recommend `/rescore AMZN`, `/rescore CSGP`, `/rescore GOOG`, and `/rescore SPOT` before executing any of the trims below** — treat them as provisional triggers, not confirmed ones.

### Trim 25–30% (Score 70.0–79.9)

| Ticker | Score | Position | Trim (25–30%) | Reasoning |
|---|---|---|---|---|
| **AMZN** | 73.4 (provisional — see caveat) | $5,618.70 combined (12 sh IBKR @ live $243.00 = $2,916.00 + 11 sh Freedom24 @ $245.70 last-known = $2,702.70; 23 sh total) | **6 sh** ($1,458.00, **26.1%** — cleanly inside the 25–30% band; 7 sh = 30.4%, just outside) | "Expensive" band on raw score, unchanged since 2026-06-20. Recommend trimming the IBKR leg (live-executable); Freedom24's 11 sh are screenshot-only. |
| **CSGP** | 79.0 (provisional — see caveat) | $750.00 (25 sh, IBKR, live $30.00) | **7 sh** ($210.00, **28.0%** — inside the 25–30% band) | "Expensive" band on raw score, unchanged since 2026-06-22. |
| **GOOG** | 73.1 (provisional — see caveat) | $355.11 (1 sh, IBKR, live) | **Not executable** (1 sh) | "Expensive" band on raw score. See execution-mechanics note below. |

### Trim to 50% (Score 80.0–89.9)

| Ticker | Score | Position | Trim to 50% | Reasoning |
|---|---|---|---|---|
| **SPOT** | 80.5 (provisional — see caveat) | $489.86 (1 sh, IBKR, live) | **Not executable** (1 sh) | "Very Expensive" band on raw score, unchanged since 2026-06-20. |

### Trim to tracking (1–2%) — Score 90.0–100.0

None. No holding scores ≥90.0 on either raw Valuation Score or Composite Score.

**⚠️ Execution-mechanics note — GOOG & SPOT (unchanged, now 5th consecutive month):** both remain single-share positions where the trim can't be executed in whole shares. Standing GTC sell-limits confirmed still live this session: GOOG SELL 1 @ $389.00 (live $355.11) and SPOT SELL 1 @ $518.00 (live $489.86). No change recommended to either order.

### Hold, no trim — Fair Value and Cheap bands

DUOL (53.7), NFLX (61.2) sit in the 50.0–69.9 Fair Value band — hold, watch only, no trim (per the 2026-06-07 rule change: fair value alone is not a sell signal). MSFT (33.9), NOW (42.3), NVDA (48.5), NVO (47.6), SPGI (33.4), UBER (34.8), V (39.2), ZS (36.3), NKE (Composite 34.8), ADBE (0.0), TRN (10.0), META (Composite 22.8), VEEV (Composite 29.7) all sit below 70.0 — hold, no trim.

---

## 3. Phase 06 — Full Exit Triggers

**None fired.** No holding sits in the 90.0–100.0 band on either raw Valuation Score or Composite Score, let alone sustained for 2+ quarters. No new fundamental-deterioration, thesis-broken, or balance-sheet-crisis triggers surfaced this session.

**RGL is still not treated as a Phase 06 exit case** — it never entered under Phase 01–03, so there is no framework-compliant position to exit from; the correct lens remains override/governance review (§7), not a valuation-driven exit. STIM and RBRK carry pre-existing, carried-forward exit-review flags (now 6th consecutive month unaddressed — see §7).

---

## 4. Upgrade 7 — 15% Single-Position Cap Check

15% of $58,258.09 = **$8,738.71**.

| Ticker | Weight | Value (live) | Breach? | Action required |
|---|---|---|---|---|
| **MSFT** | 14.84% | $8,641.60 | **No — but tight** ($97.11 of headroom) | MSFT has hovered at or just under the cap for four consecutive sessions (breached 2026-06-22, 2026-06-29; back under 2026-07-01 and again this session). No trim needed or recommended, but continued monitoring is warranted — the margin is thin enough that ordinary price movement could push it back over next cycle. |
| **TLT** | 28.53% | $16,620.17 | **Yes — by $7,881.46** | **No new finding — 6th consecutive month carried forward** (2026-06-07, 06-15, 06-22, 06-29, 07-01, now 07-03). Framework still has no fixed-income valuation/sizing methodology — logged in [override-log.md](../portfolio/override-log.md). Recommend this graduate from a routine carry-forward line to a dedicated framework-development session rather than continuing to re-flag it monthly with no path to resolution. |
| All others | ≤9.65% | — | No | — |

---

## 5. Recycling Plan

Per Phase 05 — "proceeds always reinvested into current Score 0.0–29.9 names only." Four held, scored names now qualify: **ADBE (0.0)**, **TRN (10.0)**, **META (Composite 22.8)**, and — new this session — **VEEV (Composite 29.7)**.

### Proceeds available (whole-share-executable trims only)

| Source | Amount | Driver |
|---|---|---|
| AMZN trim (6 sh, IBKR, live $243.00) | $1,458.00 | Phase 05 (valuation, provisional — see §2 caveat) |
| CSGP trim (7 sh, IBKR, live $30.00) | $210.00 | Phase 05 (valuation, provisional — see §2 caveat) |
| **Subtotal** | **$1,668.00** | |

### Allocation

1. **First $1,537.97 → ADBE.** ADBE sits at 3.77% (10 sh IBKR) vs. its ~17-share target ([2026-06-12 new-position session](2026-06-12-new-position-adbe.md)): **7 shares remain**, at today's live $219.71 = **$1,537.97**, completing the documented target (10 → 17 sh). Unambiguous, same conclusion as the last five sessions.
2. **Remainder ($130.03) — two options, same unresolved choice carried from prior sessions:**
   - **Option A (conservative):** remainder → cash. No new TRN allocation until the `REPLACED` 900-share order (order_id 1551402669, still `cum_shares_qty: 0` as of this session's live pull) is manually verified in TWS/Client Portal.
   - **Option B (continue the pattern):** remainder → a further small TRN top-up. At live GBP 2.216/share × live FX 1.33572 = $2.960/share, $130.03 buys **≈43 shares** — a small step toward the ~953-share gap (953 shares needed at current price/FX ≈ $2,821 to complete the target), consistent with the partial-fill-then-top-up pattern already used for ADBE and TRN itself.

**VEEV is a new-this-session candidate, but not a funded destination.** Its Composite Score (29.7) clears the 0.0–29.9 threshold by only 0.3 points, and the [2026-07-01 rescore session](2026-07-01-rescore-veev.md) itself flags this as "a marginal, boundary-sitting result, not a robust one" — R/R clears the 2:1 floor by only 0.16:1 (2.16:1), and several judgment calls in that session's fundamentals (Gaps #1, #3, #4) could plausibly move VEEV into the 30.0–49.9 Standard band or back to Hold on a re-run. Separately, the $130.03 of remaining proceeds this session wouldn't cover even one share of VEEV's ~16.71-share gap to its 6–8% target (~$3,204 at live $191.76) regardless. **Recommendation: do not size VEEV up mechanically off this session's trim proceeds — flag for a deliberate human decision on whether the marginal signal warrants a full position, separate from the routine recycling cycle.**

**META still has zero executable headroom.** Combined value $4,098.95 vs. its 8% Phase 03 ceiling of $4,660.65 (8% × $58,258.09) leaves only **$561.70** of room — less than one additional IBKR share at live $584.88. Not a usable destination this cycle, same conclusion as the last four sessions.

**Watchlist sweep — no new destinations found.** No new `not-in-portfolio` evaluation since 2026-07-01 clears the 80.0+ Quality gate at a qualifying valuation score; PDD's evaluation session exists but the resulting order (§0) is a pending new-position buy, not a recycling destination in the Phase 05 sense.

---

## 6. Upgrade 4 — Turnaround Sub-Gate Review Check

Searched [override-log.md](../portfolio/override-log.md) and every file under `decisions/` for any position **entered** under the Turnaround Sub-Gate ("Conditional Watch, 2–3% max," mandatory 2-quarter review). Grepped for "Turnaround Sub-Gate," "turnaround sub-gate," and "Upgrade 4" — the only decisions/ hits are the routine-schedule and glossary-formatting decisions describing the rule itself, not an entry made under it.

**Result: none found — same conclusion as all five prior months.** No turnaround-review-due items this month.

**Carried-forward recommendation, still not actioned (now 3rd consecutive rescore/rebalance cycle it's been raised):** NKE's [2026-07-01 rescore](2026-07-01-rescore-nke.md) §10 recommends formally converting NKE's standing value-trap override into a documented Upgrade 4 Turnaround Sub-Gate entry + `override-log.md` row. This still has not been done, so NKE remains untrackable under this section's mechanical check even though the underlying recommendation is overdue.

---

## 7. Other open items carried forward

| Ticker | Status | Carried from | This session's note |
|---|---|---|---|
| **RGL** | Ungoverned position; order now `PENDING_CANCEL_REPLACE` | [2026-07-01](2026-07-01-rebalance.md) §0 | **Status changed since last session — see §0.** No longer confirmed still actively growing (no new fills in the last 7 days), but not confirmed cancelled either. Recommend confirming final order status in TWS/Client Portal. |
| **MBGL** | Ungoverned position, likely corporate-action-sourced | [2026-07-01](2026-07-01-rebalance.md) §0 | Unchanged, still uninvestigated ($19.80, low urgency). |
| **AVGO** | Score 69.5, predates 2026-06-20 modifier, 3.73% | [2026-06-22](2026-06-22-rebalance.md) §7 | **4th consecutive month.** Override rationale still not on record in [override-log.md](../portfolio/override-log.md). |
| **STIM** | "Not scored — going-concern override," 1.21% | [2026-06-07](2026-06-07-rebalance.md) §6 | **6th consecutive month unaddressed.** Standing Phase 06 exit-review trigger, independent of the monthly cycle. |
| **RBRK** | "Not scored — fails quality gates," 0.43% | [2026-06-07](2026-06-07-rebalance.md) §6 | **6th consecutive month unaddressed.** Needs an `override-log.md` entry. |
| **TLT** | 28.53%, non-equity, no methodology | [2026-06-07](2026-06-07-rebalance.md) §6 | See §4 — 6 consecutive months carried forward. |
| **Stale-methodology trim triggers** | AMZN, CSGP, GOOG, SPOT all trimmed on raw Valuation Score, no Quality Score yet | New this session | See §2 — recommend prioritizing these four for `/rescore` given they're the ones actually driving this month's proposed trims. |

---

## 8. Summary table — proposed actions

| Ticker | Score | Weight | Proposed action | Driven by |
|---|---|---|---|---|
| **RGL** | not scored | 0.04% | Confirm the `PENDING_CANCEL_REPLACE` order resolves to fully cancelled in TWS/Client Portal | Governance — ungoverned position (§0, §7) |
| **MBGL** | not scored | 0.03% | Investigate source (likely corporate action); no action pending that | Governance — ungoverned position (§7) |
| **AMZN** | 73.4 (provisional) | 9.65% | Trim 6 sh from IBKR leg (~$1,458, 26.1%) → recycle; confirm via `/rescore` first | Valuation (Phase 05) — see §2 caveat |
| **CSGP** | 79.0 (provisional) | 1.29% | Trim 7 sh (~$210, 28%) → recycle; confirm via `/rescore` first | Valuation (Phase 05) — see §2 caveat |
| **GOOG** | 73.1 (provisional) | 0.61% | Trim triggered but not executable (1 sh); standing sell-limit @ $389 unchanged | Valuation (Phase 05) — execution gap |
| **SPOT** | 80.5 (provisional) | 0.84% | Trim triggered but not executable (1 sh); standing sell-limit @ $518 unchanged | Valuation (Phase 05) — execution gap |
| **MSFT** | 33.9 | 14.84% | Hold — no trim needed, cap headroom thin ($97.11) | Concentration (Upgrade 7) — monitor |
| **TLT** | n/a | 28.53% | No action — unresolved structural gap, 6th consecutive month | Framework gap |
| **ADBE** | 0.0 | 3.77% | Recycling destination: $1,537.97 completes the 17-sh target | Recycling (Phase 05) |
| **TRN** | 10.0 | 3.05% | Partial recycling destination (~$130 remainder, Option A/B); large gap remains, order-status caveat | Recycling (Phase 05) |
| **VEEV** | Composite 29.7 (marginal) | 0.99% | Newly qualifies on score but not funded this cycle — flagged for deliberate human sizing decision | Recycling (Phase 05) — marginal signal |
| **META** | Composite 22.8 | 7.04% | Qualifies on score, zero executable headroom to 8% ceiling | Recycling (Phase 05) — sizing gap |
| **NKE** | Composite 34.8 (Quality 44.4 fails gate) | 1.51% | Hold existing, do not add; formalize Turnaround Sub-Gate entry (overdue) | Governance / Upgrade 4 |
| **AVGO** | 69.5 (stale) | 3.73% | No action — methodology-stale, missing override rationale, 4th consecutive month | Data integrity / governance |
| DUOL, NFLX, NOW, NVDA, UBER, V, ZS, NVO, SPGI | 30.0–69.9 | ~20.3% combined | Hold — Cheap/Fair Value bands, no trim | Valuation (Phase 05) |
| STIM, RBRK | not scored | 1.64% combined | Carried forward, 6th consecutive month | Fundamental (Phase 06) / governance |

**Recommended sequencing:**
1. **Confirm RGL's cancel/replace resolved** in TWS/Client Portal — it's in-progress, not closed.
2. Run `/rescore` on **AMZN, CSGP, GOOG, SPOT** before executing any trim — this month's triggers are provisional pending Quality Score (§2).
3. Once confirmed, execute (or re-propose) the AMZN/CSGP trims; route $1,537.97 of proceeds to ADBE.
4. Verify the TRN `REPLACED` 900-share order in TWS/Client Portal (now overdue several sessions).
5. Resolve the AVGO data-integrity flag and the RBRK override-log gap (4th–6th consecutive month).
6. Decide on VEEV's marginal Buy signal as a standalone decision, not a mechanical recycling allocation.
7. Formalize NKE's Turnaround Sub-Gate entry in `override-log.md` (overdue 3 cycles).
8. TLT's structural gap remains a standalone framework-development item (6 consecutive months carried forward).

*Session complete. No trades executed — this is a proposal for human review. Log any executed trims/exits in `decisions/` and refresh `holdings.md` via `/sync-portfolio` once they settle.*

---

## Glossary

- **Composite Score:** this framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; drives Phase 03/05 action-table lookups once a Quality Score exists — see [quality-scoring.md](../framework/quality-scoring.md).
- **Corporate action:** an event initiated by a company (e.g., a spin-off, merger, or stock dividend) that changes shareholders' holdings without a discretionary trade — the likely explanation for MBGL's $0 cost basis (§0).
- **FX (foreign exchange) rate:** the price of converting one currency into another; this framework only uses live, broker-reported FX rates, never an assumed rate, per Rule 0.
- **GTC (Good-Til-Cancelled):** an order instruction telling the broker to keep a limit order open indefinitely until it fills or is manually cancelled — the mechanism by which the RGL order (§0) kept buying unattended.
- **Human Override:** a position opened or held outside the framework's own rules. Tracked for life in `override-log.md`.
- **Hybrid Upgrade:** one of 7 framework-specific rule additions layered on the base 6-phase strategy (Upgrade 4 = Turnaround Sub-Gate, Upgrade 7 = the 15% position cap).
- **NLV (Net Liquidation Value) / NAV (Net Asset Valuation):** a broker's headline account value — all positions at current market price, plus cash, minus liabilities (IBKR calls this NLV, Freedom24 calls it NAV).
- **Quality Score:** this framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02.
- **R/R (Risk/Reward ratio):** (expected gain) ÷ (expected loss) on a trade; this framework requires at least 2:1 before entering.
- **REPLACED / PENDING_CANCEL_REPLACE (order status):** IBKR order-lifecycle statuses. `REPLACED` means the order was superseded by a new order (doesn't confirm whether the replacement filled or is still working); `PENDING_CANCEL_REPLACE` means a cancel-and-replace instruction has been submitted but not yet confirmed by the exchange.
- **Turnaround Sub-Gate:** the conditional path (Hybrid Upgrade 4) letting a company failing some quality criteria still enter as a small (2–3%) position if it passes 5 specific tests.
- **Valuation Score:** this framework's 0.0–100.0 continuous score (0.0 = cheapest, 100.0 = most expensive).
- **Watchlist (action band):** the framework's recommendation for a valuation score of 50.0–69.9: fairly-to-fully valued, "no new entry." (Distinct from the repo's `watchlist/` directory.)

# 2026-07-04 — Rebalance Session

**Task type:** REBALANCE
**Scope:** Portfolio-wide trim/hold/exit review across [holdings.md](../portfolio/holdings.md), applying Phase 05 (Dynamic Trimming) and Phase 06 (Exit Triggers) from [strategy.md](../framework/strategy.md) to current scores, the Upgrade 7 15% single-position cap, and the Upgrade 4 Turnaround Sub-Gate review-due check. This is Routine 5's monthly Rebalance / Trim Review run ([automation-schedule.md](../framework/automation-schedule.md)), following [2026-06-07](2026-06-07-rebalance.md), [2026-06-15](2026-06-15-rebalance.md), [2026-06-22](2026-06-22-rebalance.md), [2026-06-29](2026-06-29-rebalance.md), [2026-07-01](2026-07-01-rebalance.md), and [2026-07-03](2026-07-03-rebalance.md).

**No trades executed. This is a proposal for human review only.**

---

## 0. Rule 0 — live data pull

Per Rule 0, this session pulled `get_account_positions` / `get_account_balances` / `get_account_orders` / `get_account_trades` directly rather than relying solely on `holdings.md` (last full IBKR sync 2026-06-28; Freedom24 last synced 2026-06-07, unchanged — no new screenshot this round).

**No share-count changes across any of the 25 previously-tracked tickers, RGL, or MBGL since the 2026-07-03 rebalance** — `get_account_trades` (`DAYS_7`) shows no new trades since the 2026-07-01 RGL fills and a 2026-06-30 EUR/GBP FX conversion. Prices moved only fractionally; combined portfolio total is essentially flat (**$58,226.19** vs **$58,258.09** on 2026-07-03, **‑$31.90 / ‑0.05%**, immaterial). Two things changed since the last session, one new and one still open:

- **⚠️ New — four undocumented META GTC orders appeared.** Placed **2026-07-03T16:05:10Z** (after the 07-03 session's data pull), all 1-share: `BUY 1 META @ $579.85`, `SELL 1 META @ $611.10`, `BUY 1 META @ $550.84`, `SELL 1 META @ $611.01` (order IDs 21429034–21429037). None of these appear in any `sessions/` or `decisions/` file, in `override-log.md`, or in the last `ibkr-orders.md` sync (2026-06-28) — same pattern as the still-unresolved AVGO and RGL governance flags. At 1 share apiece they carry no material sizing/cap impact, but per Rule 10 ("act only on documented triggers... every session should be saved"), any manually-placed order should have a corresponding rationale on record. **Flagged for the user to confirm whether these were an intentional manual scale-in/profit-ladder on META or unauthorized/automated activity to investigate**; not actioned this session.
- **RGL's `PENDING_CANCEL_REPLACE` order (id 630395618) is still unresolved**, now **>24 hours** since the cancel/replace was submitted (`order_time` unchanged at 2026-07-03T08:37:54Z, `cum_shares_qty` still 2,786 of 60,000, `remaining_shares_qty` still 57,214). No new RGL fills in the last 7 days. Recommend confirming final resolution (`CANCELLED` vs. still working) in TWS/Client Portal — carried forward from 2026-07-03, not yet closed out.

**Combined total (broker-reported, live):** IBKR Net Liquidation Value **$43,102.65** (`get_account_balances`, BASE row) + Freedom24 Net Asset Valuation **$15,123.54** (last screenshot sync, 2026-06-07, unchanged) = **$58,226.19**.

Scores are unchanged from `holdings.md` / the 2026-07-03 session for every ticker — no `/rescore` or `/new-position` ran on a held name between the two sessions. Same convention as the last six rebalance sessions: where a Quality Score exists, this session uses the **Composite Score** for Phase 03/05 lookups; where it's still `?`, it falls back to the raw Valuation Score (see the caveat in §2).

| Ticker | Combined USD value (live) | Weight % | Score used | Type | Last Review | Band |
|---|---|---|---|---|---|---|
| ADBE | $2,197.10 | 3.77% | 0.0 | Valuation (no Quality yet) | 20 Jun 2026 | 0.0–29.9 Very Cheap |
| AMZN | $5,618.70 | 9.65% | 73.4 | Valuation (no Quality yet) | 20 Jun 2026 | 70.0–79.9 Expensive |
| AVGO | $2,172.00 | 3.73% | 69.5 (**stale — predates 2026-06-20 modifier**) | Valuation (no Quality yet) | 14 Jun 2026 | see §7 |
| CSGP | $750.00 | 1.29% | 79.0 | Valuation (no Quality yet) | 20 Jun 2026 | 70.0–79.9 Expensive |
| DUOL | $4,627.84 | 7.95% | 53.7 | Valuation (no Quality yet) | 20 Jun 2026 | 50.0–69.9 Fair Value |
| GOOG | $355.11 | 0.61% | 73.1 | Valuation (no Quality yet) | 20 Jun 2026 | 70.0–79.9 Expensive |
| **MBGL** | $19.80 | 0.03% | not scored — ungoverned, see §7 | — | n/a | special |
| META | $4,098.95 | 7.04% | **22.8** | **Composite** | 1 Jul 2026 | 0.0–29.9 Very Cheap |
| MSFT | $8,641.60 | 14.84% | 33.9 | Valuation (no Quality yet) | 26 Jun 2026 | 30.0–49.9 Cheap |
| NFLX | $931.31 | 1.60% | 61.2 | Valuation (no Quality yet) | 20 Jun 2026 | 50.0–69.9 Fair Value |
| NKE | $881.80 | 1.51% | **34.8** (Quality 44.4 — **fails 80.0+ gate**) | **Composite** | 1 Jul 2026 | 30.0–49.9 Cheap (override — do NOT add) |
| NOW | $1,275.84 | 2.19% | 42.3 | Valuation (no Quality yet) | 20 Jun 2026 | 30.0–49.9 Cheap |
| NVDA | $2,722.16 | 4.68% | 48.5 | Valuation (no Quality yet) | 20 Jun 2026 | 30.0–49.9 Cheap |
| NVO | $252.15 | 0.43% | 47.6 | Valuation (no Quality yet) | 20 Jun 2026 | 30.0–49.9 Cheap |
| RBRK | $250.26 | 0.43% | not scored — fails quality gates | — | Jun 2026 | special — see §7 |
| **RGL** | $21.27 | 0.04% | not scored — ungoverned, see §7 | — | n/a | special |
| SPGI | $433.80 | 0.75% | 33.4 | Valuation (no Quality yet) | 20 Jun 2026 | 30.0–49.9 Cheap |
| SPOT | $489.86 | 0.84% | 80.5 | Valuation (no Quality yet) | 20 Jun 2026 | 80.0–89.9 Very Expensive |
| STIM | $705.00 | 1.21% | not scored — going-concern override | — | Jun 2026 | special — see §7 |
| TLT | $16,620.17 | 28.55% | not scored — non-equity | — | Jun 2026 | special — see §4 |
| TRN | $1,746.25 | 3.00% | 10.0 | Valuation (no Quality yet) | 24 Jun 2026 | 0.0–29.9 Very Cheap (partial fill) |
| UBER | $223.05 | 0.38% | 34.8 | Valuation (no Quality yet) | 20 Jun 2026 | 30.0–49.9 Cheap |
| V | $361.71 | 0.62% | 39.2 | Valuation (no Quality yet) | 20 Jun 2026 | 30.0–49.9 Cheap |
| VEEV | $575.28 | 0.99% | **29.7** (Quality 85.7 — passes gate, marginal/boundary, see 2026-07-01 rescore) | **Composite** | 1 Jul 2026 | 0.0–29.9 Very Cheap (boundary) |
| XEON | $1,710.52 | 2.94% | not scored — cash-equivalent | — | Jun 2026 | out of scope |
| ZS | $147.13 | 0.25% | 36.3 | Valuation (no Quality yet) | 20 Jun 2026 | 30.0–49.9 Cheap (override — quality-gate fail, see override-log) |
| CASH (IBKR) | $342.67 | 0.59% | — | — | — | liquidity |
| CASH (Freedom24) | $106.85 | 0.18% | — | — | — | liquidity |

*STIM's weight above reflects the 500-share equity position only ($705.00); the short 5-contract covered call (market value −$50.00) is excluded, same convention as prior sessions.*

---

## 1. Staleness check (operating-calendar.md)

No holding shows a confirmed earnings release since its last review that hasn't yet been re-scored. Two staleness flags carry forward, unchanged since 2026-07-03:

1. **AVGO (69.5, scored 14 Jun 2026)** predates the 2026-06-20 Upside/Downside Modifier — see §7. Needs `/rescore AVGO` before its band assignment can be trusted.
2. **16 in-portfolio holdings still show `?` for Quality Score / Composite Score** under the 2026-06-29 methodology change (ADBE, AMZN, AVGO, CSGP, DUOL, GOOG, MSFT, NFLX, NOW, NVDA, NVO, SPGI, SPOT, TRN, UBER, V, ZS — full list tracked in [watchlist/STALE.md](../watchlist/STALE.md)). Four of this month's trim triggers still come from this exact set — see §2 caveat.

---

## 2. Phase 05 — Dynamic Trimming

### ⚠️ Important caveat before the trim table (unchanged from prior sessions)

Per [strategy.md](../framework/strategy.md), Phase 05 trim triggers should be evaluated on the **Composite Score** once a Quality Score exists. **AMZN, CSGP, GOOG, and SPOT — every trim trigger firing this session — all still show `Quality Score = ?`**, so the bands below use the raw Valuation Score only, same fallback convention as the last six sessions. **This is provisional, not confirmed** — a computed Quality Score could pull any of these four out of the 70.0+ trim band (as it did for META, whose Quality Score of 90.0 pulled its Composite down to 22.8) or could deepen the trim case. **Recommend `/rescore AMZN`, `/rescore CSGP`, `/rescore GOOG`, and `/rescore SPOT` before executing any of the trims below** — now the 2nd consecutive session flagging this exact same unresolved gap with no rescore having happened in between.

### Trim 25–30% (Score 70.0–79.9)

| Ticker | Score | Position | Trim (25–30%) | Reasoning |
|---|---|---|---|---|
| **AMZN** | 73.4 (provisional — see caveat) | $5,618.70 combined (12 sh IBKR @ live $243.00 = $2,916.00 + 11 sh Freedom24 @ $245.70 last-known = $2,702.70; 23 sh total) | **6 sh** ($1,458.00, **26.1%** — inside the 25–30% band) | "Expensive" band on raw score, unchanged since 2026-06-20. Recommend trimming the IBKR leg (live-executable); Freedom24's 11 sh are screenshot-only. |
| **CSGP** | 79.0 (provisional — see caveat) | $750.00 (25 sh, IBKR, live $30.00) | **7 sh** ($210.00, **28.0%** — inside the 25–30% band) | "Expensive" band on raw score, unchanged since 2026-06-22. |
| **GOOG** | 73.1 (provisional — see caveat) | $355.11 (1 sh, IBKR, live) | **Not executable** (1 sh) | "Expensive" band on raw score. See execution-mechanics note below. |

### Trim to 50% (Score 80.0–89.9)

| Ticker | Score | Position | Trim to 50% | Reasoning |
|---|---|---|---|---|
| **SPOT** | 80.5 (provisional — see caveat) | $489.86 (1 sh, IBKR, live) | **Not executable** (1 sh) | "Very Expensive" band on raw score, unchanged since 2026-06-20. |

### Trim to tracking (1–2%) — Score 90.0–100.0

None. No holding scores ≥90.0 on either raw Valuation Score or Composite Score.

**⚠️ Execution-mechanics note — GOOG & SPOT (unchanged, now 6th consecutive month):** both remain single-share positions where the trim can't be executed in whole shares. Standing GTC sell-limits confirmed still live: GOOG SELL 1 @ $389.00 (live $355.11) and SPOT SELL 1 @ $518.00 (live $489.86). No change recommended to either order.

### Hold, no trim — Fair Value and Cheap bands

DUOL (53.7), NFLX (61.2) sit in the 50.0–69.9 Fair Value band — hold, watch only, no trim. MSFT (33.9), NOW (42.3), NVDA (48.5), NVO (47.6), SPGI (33.4), UBER (34.8), V (39.2), ZS (36.3), NKE (Composite 34.8), ADBE (0.0), TRN (10.0), META (Composite 22.8), VEEV (Composite 29.7) all sit below 70.0 — hold, no trim.

---

## 3. Phase 06 — Full Exit Triggers

**None fired.** No holding sits in the 90.0–100.0 band on either raw Valuation Score or Composite Score, let alone sustained for 2+ quarters. No new fundamental-deterioration, thesis-broken, or balance-sheet-crisis triggers surfaced this session.

**RGL is still not treated as a Phase 06 exit case** — it never entered under Phase 01–03, so the correct lens remains override/governance review (§7), not a valuation-driven exit. STIM and RBRK carry pre-existing, carried-forward exit-review flags (now 7th consecutive month unaddressed — see §7).

---

## 4. Upgrade 7 — 15% Single-Position Cap Check

15% of $58,226.19 = **$8,733.93**.

| Ticker | Weight | Value (live) | Breach? | Action required |
|---|---|---|---|---|
| **MSFT** | 14.84% | $8,641.60 | **No — but tight** ($92.33 of headroom) | MSFT has hovered at or just under the cap for five consecutive sessions. No trim needed or recommended, but continued monitoring is warranted. |
| **TLT** | 28.55% | $16,620.17 | **Yes — by $7,886.24** | **No new finding — 7th consecutive month carried forward** (2026-06-07 through 2026-07-03, now 07-04). Framework still has no fixed-income valuation/sizing methodology — logged in [override-log.md](../portfolio/override-log.md). Recommend this graduate from a routine carry-forward line to a dedicated framework-development session rather than continuing to re-flag it monthly with no path to resolution. |
| All others | ≤9.65% | — | No | — |

---

## 5. Recycling Plan

Per Phase 05 — "proceeds always reinvested into current Score 0.0–29.9 names only." Four held, scored names qualify: **ADBE (0.0)**, **TRN (10.0)**, **META (Composite 22.8)**, and **VEEV (Composite 29.7)**.

### Proceeds available (whole-share-executable trims only)

| Source | Amount | Driver |
|---|---|---|
| AMZN trim (6 sh, IBKR, live $243.00) | $1,458.00 | Phase 05 (valuation, provisional — see §2 caveat) |
| CSGP trim (7 sh, IBKR, live $30.00) | $210.00 | Phase 05 (valuation, provisional — see §2 caveat) |
| **Subtotal** | **$1,668.00** | |

### Allocation

1. **First $1,537.97 → ADBE.** ADBE sits at 3.77% (10 sh IBKR) vs. its ~17-share target ([2026-06-12 new-position session](2026-06-12-new-position-adbe.md)): **7 shares remain**, at today's live $219.71 = **$1,537.97**, completing the documented target (10 → 17 sh). Unambiguous, same conclusion as the last six sessions.
2. **Remainder ($130.03) — same unresolved choice carried from prior sessions:**
   - **Option A (conservative):** remainder → cash. No new TRN allocation until the `REPLACED` 900-share order (order_id 1551402669, still `cum_shares_qty: 0`) is manually verified in TWS/Client Portal.
   - **Option B (continue the pattern):** remainder → a further small TRN top-up. At live GBP 2.18/share × live FX 1.33505 = ~$2.91/share, $130.03 buys **≈44 shares** — a small step toward the remaining gap to the ~1,553-share target.

**VEEV is a qualifying candidate, but not a funded destination.** Its Composite Score (29.7) clears the 0.0–29.9 threshold by only 0.3 points, and the [2026-07-01 rescore session](2026-07-01-rescore-veev.md) itself flags this as "a marginal, boundary-sitting result, not a robust one." Separately, the $130.03 of remaining proceeds this session wouldn't cover even one share of VEEV's ~16.7-share gap to its 6–8% target regardless. **Recommendation unchanged: do not size VEEV up mechanically off routine trim proceeds — flag for a deliberate human decision.**

**META still has zero executable headroom.** Combined value $4,098.95 vs. its 8% Phase 03 ceiling of $4,658.10 (8% × $58,226.19) leaves only **$559.15** of room — less than one additional IBKR share at live $584.88. Not a usable destination this cycle, same conclusion as the last five sessions. (Note: the four new undocumented META GTC orders flagged in §0 do not change this — none have filled.)

**Watchlist sweep — no new destinations found.** ORANY, OUST, and WBX (evaluated 2026-07-01/07-03) all failed the Phase 01 Quality Score gate before any valuation score was computed — none clear the 80.0+ gate at a qualifying valuation score. PDD's evaluation exists but the resulting order (§0, still `NEW`/unfilled) is a pending new-position buy, not a recycling destination in the Phase 05 sense.

---

## 6. Upgrade 4 — Turnaround Sub-Gate Review Check

Searched [override-log.md](../portfolio/override-log.md) and every file under `decisions/` for any position **entered** under the Turnaround Sub-Gate ("Conditional Watch, 2–3% max," mandatory 2-quarter review). No `decisions/` hits beyond the routine-schedule and glossary-formatting entries describing the rule itself, not an entry made under it.

**Result: none found — same conclusion as all six prior months.** No turnaround-review-due items this month.

**Carried-forward recommendation, still not actioned (now 4th consecutive cycle it's been raised):** NKE's [2026-07-01 rescore](2026-07-01-rescore-nke.md) §10 recommends formally converting NKE's standing value-trap override into a documented Upgrade 4 Turnaround Sub-Gate entry + `override-log.md` row. Still not done.

---

## 7. Other open items carried forward

| Ticker | Status | Carried from | This session's note |
|---|---|---|---|
| **META (new orders)** | 4 undocumented 1-share GTC orders (2 buy, 2 sell) | New this session | **See §0.** Placed 2026-07-03T16:05:10Z, no rationale on record anywhere in the repo. Flagged for confirmation, not actioned. |
| **RGL** | Ungoverned position; order still `PENDING_CANCEL_REPLACE`, now >24h | [2026-07-03](2026-07-03-rebalance.md) §0 | Unchanged — still not confirmed cancelled. Recommend confirming final order status in TWS/Client Portal. |
| **MBGL** | Ungoverned position, likely corporate-action-sourced | [2026-07-01](2026-07-01-rebalance.md) §0 | Unchanged, still uninvestigated ($19.80, low urgency). |
| **AVGO** | Score 69.5, predates 2026-06-20 modifier, 3.73% | [2026-06-22](2026-06-22-rebalance.md) §7 | **5th consecutive month.** Override rationale still not on record in [override-log.md](../portfolio/override-log.md). |
| **STIM** | "Not scored — going-concern override," 1.21% | [2026-06-07](2026-06-07-rebalance.md) §6 | **7th consecutive month unaddressed.** Standing Phase 06 exit-review trigger, independent of the monthly cycle. |
| **RBRK** | "Not scored — fails quality gates," 0.43% | [2026-06-07](2026-06-07-rebalance.md) §6 | **7th consecutive month unaddressed.** Needs an `override-log.md` entry. |
| **TLT** | 28.55%, non-equity, no methodology | [2026-06-07](2026-06-07-rebalance.md) §6 | See §4 — 7 consecutive months carried forward. |
| **Stale-methodology trim triggers** | AMZN, CSGP, GOOG, SPOT all trimmed on raw Valuation Score, no Quality Score yet | [2026-07-03](2026-07-03-rebalance.md) §2 | 2nd consecutive session flagging this unresolved — recommend prioritizing these four for `/rescore`. |

---

## 8. Summary table — proposed actions

| Ticker | Score | Weight | Proposed action | Driven by |
|---|---|---|---|---|
| **META (new orders)** | n/a | n/a | Confirm intent behind the 4 new 1-share GTC orders (§0); no rationale on record | Governance — undocumented order activity |
| **RGL** | not scored | 0.04% | Confirm the `PENDING_CANCEL_REPLACE` order resolves to fully cancelled in TWS/Client Portal | Governance — ungoverned position (§0, §7) |
| **MBGL** | not scored | 0.03% | Investigate source (likely corporate action); no action pending that | Governance — ungoverned position (§7) |
| **AMZN** | 73.4 (provisional) | 9.65% | Trim 6 sh from IBKR leg (~$1,458, 26.1%) → recycle; confirm via `/rescore` first | Valuation (Phase 05) — see §2 caveat |
| **CSGP** | 79.0 (provisional) | 1.29% | Trim 7 sh (~$210, 28%) → recycle; confirm via `/rescore` first | Valuation (Phase 05) — see §2 caveat |
| **GOOG** | 73.1 (provisional) | 0.61% | Trim triggered but not executable (1 sh); standing sell-limit @ $389 unchanged | Valuation (Phase 05) — execution gap |
| **SPOT** | 80.5 (provisional) | 0.84% | Trim triggered but not executable (1 sh); standing sell-limit @ $518 unchanged | Valuation (Phase 05) — execution gap |
| **MSFT** | 33.9 | 14.84% | Hold — no trim needed, cap headroom thin ($92.33) | Concentration (Upgrade 7) — monitor |
| **TLT** | n/a | 28.55% | No action — unresolved structural gap, 7th consecutive month | Framework gap |
| **ADBE** | 0.0 | 3.77% | Recycling destination: $1,537.97 completes the 17-sh target | Recycling (Phase 05) |
| **TRN** | 10.0 | 3.00% | Partial recycling destination (~$130 remainder, Option A/B); large gap remains, order-status caveat | Recycling (Phase 05) |
| **VEEV** | Composite 29.7 (marginal) | 0.99% | Qualifies on score but not funded this cycle — flagged for deliberate human sizing decision | Recycling (Phase 05) — marginal signal |
| **META** | Composite 22.8 | 7.04% | Qualifies on score, zero executable headroom to 8% ceiling | Recycling (Phase 05) — sizing gap |
| **NKE** | Composite 34.8 (Quality 44.4 fails gate) | 1.51% | Hold existing, do not add; formalize Turnaround Sub-Gate entry (overdue) | Governance / Upgrade 4 |
| **AVGO** | 69.5 (stale) | 3.73% | No action — methodology-stale, missing override rationale, 5th consecutive month | Data integrity / governance |
| DUOL, NFLX, NOW, NVDA, UBER, V, ZS, NVO, SPGI | 30.0–69.9 | ~20.4% combined | Hold — Cheap/Fair Value bands, no trim | Valuation (Phase 05) |
| STIM, RBRK | not scored | 1.64% combined | Carried forward, 7th consecutive month | Fundamental (Phase 06) / governance |

**Recommended sequencing:**
1. **Confirm the 4 new META GTC orders** are intentional (§0) — undocumented order activity is the same pattern that produced the still-open AVGO and RGL governance flags.
2. **Confirm RGL's cancel/replace resolved** in TWS/Client Portal — it's in-progress, not closed, now >24h.
3. Run `/rescore` on **AMZN, CSGP, GOOG, SPOT** before executing any trim — this month's triggers are provisional pending Quality Score (§2), now flagged for 2 consecutive sessions.
4. Once confirmed, execute (or re-propose) the AMZN/CSGP trims; route $1,537.97 of proceeds to ADBE.
5. Verify the TRN `REPLACED` 900-share order in TWS/Client Portal (overdue several sessions).
6. Resolve the AVGO data-integrity flag and the RBRK override-log gap (5th–7th consecutive month).
7. Decide on VEEV's marginal Buy signal as a standalone decision, not a mechanical recycling allocation.
8. Formalize NKE's Turnaround Sub-Gate entry in `override-log.md` (overdue 4 cycles).
9. TLT's structural gap remains a standalone framework-development item (7 consecutive months carried forward).

*Session complete. No trades executed — this is a proposal for human review. Log any executed trims/exits in `decisions/` and refresh `holdings.md` via `/sync-portfolio` once they settle.*

---

## Glossary

- **Composite Score:** this framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; drives Phase 03/05 action-table lookups once a Quality Score exists — see [quality-scoring.md](../framework/quality-scoring.md).
- **Corporate action:** an event initiated by a company (e.g., a spin-off, merger, or stock dividend) that changes shareholders' holdings without a discretionary trade — the likely explanation for MBGL's $0 cost basis (§0).
- **FX (foreign exchange) rate:** the price of converting one currency into another; this framework only uses live, broker-reported FX rates, never an assumed rate, per Rule 0.
- **GTC (Good-Til-Cancelled):** an order instruction telling the broker to keep a limit order open indefinitely until it fills or is manually cancelled.
- **Human Override:** a position opened or held outside the framework's own rules. Tracked for life in `override-log.md`.
- **Hybrid Upgrade:** one of 7 framework-specific rule additions layered on the base 6-phase strategy (Upgrade 4 = Turnaround Sub-Gate, Upgrade 7 = the 15% position cap).
- **NLV (Net Liquidation Value) / NAV (Net Asset Valuation):** a broker's headline account value — all positions at current market price, plus cash, minus liabilities (IBKR calls this NLV, Freedom24 calls it NAV).
- **Quality Score:** this framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02.
- **R/R (Risk/Reward ratio):** (expected gain) ÷ (expected loss) on a trade; this framework requires at least 2:1 before entering.
- **REPLACED / PENDING_CANCEL_REPLACE (order status):** IBKR order-lifecycle statuses. `REPLACED` means the order was superseded by a new order (doesn't confirm whether the replacement filled or is still working); `PENDING_CANCEL_REPLACE` means a cancel-and-replace instruction has been submitted but not yet confirmed by the exchange.
- **Turnaround Sub-Gate:** the conditional path (Hybrid Upgrade 4) letting a company failing some quality criteria still enter as a small (2–3%) position if it passes 5 specific tests.
- **Valuation Score:** this framework's 0.0–100.0 continuous score (0.0 = cheapest, 100.0 = most expensive).
- **Watchlist (action band):** the framework's recommendation for a valuation score of 50.0–69.9: fairly-to-fully valued, "no new entry." (Distinct from the repo's `watchlist/` directory.)

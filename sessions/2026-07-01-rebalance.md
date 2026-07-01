# 2026-07-01 — Rebalance Session

**Task type:** REBALANCE
**Scope:** Portfolio-wide trim/hold/exit review across [holdings.md](../portfolio/holdings.md), applying Phase 05 (Dynamic Trimming) and Phase 06 (Exit Triggers) from [strategy.md](../framework/strategy.md) to current scores, the Upgrade 7 15% single-position cap, and the Upgrade 4 Turnaround Sub-Gate review-due check. This is the fifth run of Routine 5 ([decisions/2026-06-13-automation-routine-schedule.md](../decisions/2026-06-13-automation-routine-schedule.md)), following [2026-06-07](2026-06-07-rebalance.md), [2026-06-15](2026-06-15-rebalance.md), [2026-06-22](2026-06-22-rebalance.md), and [2026-06-29](2026-06-29-rebalance.md).

**No trades executed. This is a proposal for human review only.**

---

## 0. ⚠️ Headline finding — two ungoverned positions found live in the IBKR account, not in `holdings.md`

Per Rule 0 ("always fetch live prices first"), this session pulled `get_account_positions` / `get_account_balances` / `get_account_orders` / `get_account_trades` directly rather than relying solely on the 2026-06-28 `holdings.md` sync. That live pull surfaced **two positions that exist in the brokerage account but do not appear anywhere in `holdings.md`, `override-log.md`, `sessions/`, or `watchlist/`:**

### RGL (RiversGold Ltd, ASX) — **the priority item this session**

- **2,786 shares** held, price **AUD $0.009** (0.9 cents), market value **AUD $27.86 (≈USD $19.19)**.
- Built from **4 partial fills** (10, 79, 80, 2,617 shares) between 2026-06-30 23:59 UTC and 2026-07-01 05:25 UTC, all against a single **still-live GTC limit order** (`order_id 630395618`: **BUY 60,000 RGL @ $0.009 AUD, GTC, PARTIALLY_FILLED, 57,214 shares remaining**).
- **No Phase 01 quality screen, no Phase 02 valuation score, no `sessions/` entry, no `override-log.md` entry exists for this ticker anywhere in this repo.** RiversGold is an ASX-listed micro-cap gold exploration company — a sub-cent, pre-revenue explorer is close to a worst-case fit against this framework's own Phase 01 criteria (net margin >15%, ROIC >15%, positive FCF 3+ years), which is exactly why no evaluation session was ever run: **this position did not originate from this framework's process.**
- **The order is still open and will keep buying** (57,214 shares remaining at $0.009 = up to another ≈AUD $515 if it fully fills) **until it is cancelled or expires.** This is time-sensitive, not just a data-hygiene gap.
- **Action recommended:** verify in TWS/Client Portal whether this order was placed intentionally (e.g., a manual trade outside this framework) or is unrecognized/unauthorized activity, and cancel it if not intended. Logged below as a retroactive override-log entry (rationale not on record) so it's tracked rather than silently absorbed into the next sync.

### MBGL (Mobility Global Inc) — lower priority

- **1 share**, market value **$20.25**, **average cost $0.00** — the zero cost basis strongly suggests a corporate action (e.g., a spin-off distribution from an existing or former holding) rather than a discretionary purchase; no matching trade appears in `get_account_trades` for `DAYS_30`, consistent with that theory, but this session did not run the research needed to confirm the source security. Flagged for investigation, not urgent given the ~$20 size.

**Both are carried in the tables below as unscored, ungoverned rows — not scored, no action bands applied (there is nothing to trim/hold/exit against without a Phase 01/02 evaluation), consistent with how RBRK/STIM/TLT are already carried as "not scored" rows.**

---

## 1. Holdings pull & staleness check

`holdings.md` states it was synced 2026-06-28 (IBKR) + 2026-06-07 (Freedom24, unchanged). **This is now stale in a way that matters**, not just cosmetically: the live IBKR pull this session (2026-07-01) shows two new, unrecorded positions (§0 above) and a materially different cash picture (EUR cash cash grew from $5.18 → $227.49; the GBP cash balance flagged negative in every rebalance since 2026-06-24 has been resolved via an **EUR→GBP conversion** on 2026-06-30, not the USD→GBP conversion previously discussed — `get_account_trades`: SELL EUR 1,477.69 → GBP, 2026-06-30T05:50:03Z). **Recommend running `/sync-portfolio` before the next scheduled routine** to bring `holdings.md` back to parity with the live account, including formally onboarding (or removing) RGL/MBGL.

For this session's own calculations, live data was pulled directly (Rule 0) rather than waiting on a sync. **No share-count changes since 2026-06-29** for any of the 25 previously-tracked tickers — only cash/FX and the two new positions changed. Scores are unchanged from `holdings.md` except **NKE**, rescored 2026-07-01 (Telegram-triggered, post-FY2026-Q4-earnings) — see [sessions/2026-07-01-rescore-nke.md](2026-07-01-rescore-nke.md): valuation score 43.1→13.9, first-ever Quality Score 44.4 (**fails the 80.0+ gate**), Composite Score **34.8**. Action unchanged: **HOLD existing, do NOT add** (R/R 1.79:1 at the turnaround buy price, still below the 2:1 floor).

**Combined total (broker-reported, live):** IBKR Net Liquidation Value **$41,967.85** (`get_account_balances`, BASE row) + Freedom24 Net Asset Valuation **$15,123.54** (last screenshot sync, 2026-06-07, unchanged) = **$57,091.39**. (A bottom-up sum of position market values + cash gives ≈$57,137, a ~$46 gap consistent with the recurring GPV-vs-NLV intraday timing gap already documented in [ibkr.md](../portfolio/snapshots/ibkr.md) — not a calculation error.)

| Ticker | Weight % | USD value (live, 2026-07-01) | Score | Last Review | Band (Phase 03/05) |
|---|---|---|---|---|---|
| ADBE | 3.65% | $2,083.60 | 0.0 | 20 Jun 2026 | 0.0–29.9 Very Cheap |
| AMZN | 9.75% | $5,566.26 | 73.4 | 20 Jun 2026 | 70.0–79.9 Expensive |
| AVGO | 3.94% | $2,250.00 | 69.5 (**stale**) | 14 Jun 2026 | predates 2026-06-20 modifier — see §7 |
| CSGP | 1.25% | $712.75 | 79.0 | 20 Jun 2026 | 70.0–79.9 Expensive |
| DUOL | 7.61% | $4,343.44 | 53.7 | 20 Jun 2026 | 50.0–69.9 Fair Value |
| GOOG | 0.62% | $354.27 | 73.1 | 20 Jun 2026 | 70.0–79.9 Expensive |
| **MBGL** | **0.04%** | **$20.25** | **not scored — ungoverned, see §0** | n/a | special |
| META | 7.18% | $4,099.65 | 17.2 | 26 Jun 2026 | 0.0–29.9 Very Cheap |
| MSFT | 14.71% | $8,395.20 | 33.9 | 26 Jun 2026 | 30.0–49.9 Cheap |
| NFLX | 1.52% | $868.06 | 61.2 | 20 Jun 2026 | 50.0–69.9 Fair Value |
| NKE | 1.42% | $812.23 | **13.9 (Comp. 34.8)** | **1 Jul 2026** | 30.0–49.9 Cheap (override — do NOT add, see §1 note) |
| NOW | 2.18% | $1,245.48 | 42.3 | 20 Jun 2026 | 30.0–49.9 Cheap |
| NVDA | 4.87% | $2,779.00 | 48.5 | 20 Jun 2026 | 30.0–49.9 Cheap |
| NVO | 0.42% | $240.80 | 47.6 | 20 Jun 2026 | 30.0–49.9 Cheap |
| RBRK | 0.43% | $243.00 | not scored | Jun 2026 | special — see §7 |
| **RGL** | **0.03%** | **$19.19** | **not scored — ungoverned, see §0** | n/a | special |
| SPGI | 0.69% | $392.00 | 33.4 | 20 Jun 2026 | 30.0–49.9 Cheap |
| SPOT | 0.81% | $461.00 | 80.5 | 20 Jun 2026 | 80.0–89.9 Very Expensive |
| STIM | 1.13% | $645.00 | not scored | Jun 2026 | special — see §7 |
| TLT | 29.09% | $16,609.39 | not scored | Jun 2026 | special — see §4 |
| TRN | 2.86% | $1,634.90 | 10.0 | 24 Jun 2026 | 0.0–29.9 Very Cheap (partial fill) |
| UBER | 0.38% | $217.72 | 34.8 | 20 Jun 2026 | 30.0–49.9 Cheap |
| V | 0.60% | $343.19 | 39.2 | 20 Jun 2026 | 30.0–49.9 Cheap |
| VEEV | 0.95% | $540.00 | **blank** | **blank** | needs `/rescore` — see §7 |
| XEON | 2.98% | $1,702.16 | not scored | Jun 2026 | out of scope |
| ZS | 0.25% | $142.50 | 36.3 | 20 Jun 2026 | 30.0–49.9 Cheap |
| CASH (IBKR) | 0.59% | $334.57 | — | — | liquidity (now positive — see §1) |
| CASH (Freedom24) | 0.19% | $106.85 | — | — | liquidity |

*STIM's weight excludes the −$25.00 short covered-call market value, same convention as prior sessions.*

---

## 2. Phase 05 — Dynamic Trimming (applied to current scores, live prices)

### Trim 25–30% (Score 70.0–79.9)

| Ticker | Score | Position | Trim (25–30%) | Reasoning |
|---|---|---|---|---|
| **AMZN** | 73.4 | $5,566.26 combined (12 sh IBKR @ live $238.63 = $2,863.56 + 11 sh Freedom24 @ $245.70 last-known = $2,702.70; 23 sh total) | **6–7 sh** ($1,431.78, 26.1% — $1,670.41, 30.4%) | "Expensive" band, pure valuation-driven trim, unchanged since 2026-06-20. Recommend trimming the IBKR leg (live-executable); Freedom24's 11 sh are screenshot-only. |
| **CSGP** | 79.0 | $712.75 (25 sh, IBKR, live $28.51) | **7 sh** ($199.57, **28.0%** — squarely inside the 25–30% band; 6 sh = 24.0%, 8 sh = 32.0%, both slightly outside) | "Expensive," unchanged band since 2026-06-22. **Correction from prior sessions' math:** 7 shares is the best whole-share fit (25–30% of 25 shares = 6.25–7.5 shares, and 7 falls inside that range), not the 6-or-8 split proposed in the 2026-06-29 session. |
| **GOOG** | 73.1 | $354.27 (1 sh, IBKR, live) | **Not executable** (1 sh) | "Expensive." See execution-mechanics note below. |

### Trim to 50% (Score 80.0–89.9)

| Ticker | Score | Position | Trim to 50% | Reasoning |
|---|---|---|---|---|
| **SPOT** | 80.5 | $461.00 (1 sh, IBKR, live) | **Not executable** (1 sh) | "Very Expensive," unchanged since 2026-06-20. |

### Trim to tracking (1–2%) — Score 90.0–100.0

None. No holding scores ≥90.0.

**⚠️ Execution-mechanics note — GOOG & SPOT (unchanged, now 4th consecutive month):** both remain single-share positions where the trim can't be executed in whole shares. Standing GTC sell-limits confirmed still live this session: GOOG SELL 1 @ $389.00 (live $354.27) and SPOT SELL 1 @ $518.00 (live $461.00). No change recommended to either order.

---

## 3. Phase 06 — Full Exit Triggers

**None fired on valuation grounds.** No holding sits in the 90.0–100.0 band, let alone for 2+ consecutive quarters.

No new fundamental-deterioration, thesis-broken, or balance-sheet-crisis triggers from this session's inputs. STIM and RBRK carry pre-existing, carried-forward exit-review flags (now **5th consecutive month** unaddressed — see §7). **RGL (§0) is not treated as a Phase 06 exit case** — it never entered under Phase 01–03 in the first place, so there's no framework-compliant position to "exit" from; the correct lens is override/governance review, not a valuation-driven exit.

---

## 4. Upgrade 7 — 15% Single-Position Cap Check

15% of $57,091.39 = **$8,563.71**.

| Ticker | Weight | Value (live) | Breach? | Action required |
|---|---|---|---|---|
| **MSFT** | 14.71% | $8,395.20 | **No — breach resolved.** | MSFT had breached the cap for 2 consecutive months (2026-06-22, 2026-06-29), growing each time. This session it's **back under the cap by $168.51**, driven by the denominator growing (portfolio total up ~$2,200 since 2026-06-28, mostly the EUR cash correction in §1) faster than MSFT's own price gain. **No trim needed or recommended.** Recommend continued monitoring rather than treating this as fully closed — the same live-price-sensitivity swings that caused the breach to grow in prior months can just as easily push it back over. |
| **TLT** | 29.09% | $16,609.39 | **Yes — by $8,045.68** | **No new finding — 5th consecutive month carried forward** (2026-06-07, 06-15, 06-22, 06-29, now 07-01). Same structural gap logged in [override-log.md](../portfolio/override-log.md); framework still has no fixed-income valuation/sizing methodology. Recommend this graduate from a routine carry-forward line to a dedicated framework-development session. |
| All others | ≤ 9.75% | — | No | — |

---

## 5. Recycling Plan

Per Phase 05 — "proceeds always reinvested into current Score 0.0–29.9 names only." Three held, scored names qualify: **ADBE (0.0)**, **META (17.2)**, and **TRN (10.0)**.

**ADBE remains the fully-documented, unambiguous destination.** ADBE sits at 3.65% (10 sh IBKR) vs. its ~17-share target ([2026-06-12 new-position session](2026-06-12-new-position-adbe.md)): **7 shares remain**, at today's live $208.36 = **$1,458.52**.

**META still has zero executable headroom.** Combined value $4,099.65 vs. its 8% Phase 03 ceiling of $4,567.31 (8% × $57,091.39) leaves only **$467.66** of room — less than one additional IBKR share at today's live $585.00. **Not a usable destination this cycle**, same conclusion as the last three sessions.

**TRN's gap has grown again.** 953 shares remain toward the ~1,553-share target ([sessions/2026-06-24-new-position-trn.md](2026-06-24-new-position-trn.md)). At today's live price (GBP 2.058/share) and live FX (1.32412): 953 × £2.058 × 1.32412 ≈ **$2,597.35**.

**⚠️ TRN order-status question is now unresolved for a 4th consecutive session (06-29, and now 07-01) — recommend resolving before next month's cycle regardless of which recycling option is chosen.** Order 1551402669 (`Buy 900 TRN` @ GBX 161.50, placed 2026-06-24) still shows `REPLACED`, `cum_shares_qty: 0`, with no live successor in this session's `get_account_orders` fetch.

### Proceeds available (whole-share-executable trims only)

| Source | Amount | Driver |
|---|---|---|
| AMZN trim (6–7 sh, IBKR, live $238.63) | $1,431.78 – $1,670.41 | Phase 05 (valuation) |
| CSGP trim (7 sh, IBKR, live $28.51) | $199.57 | Phase 05 (valuation) |
| **Subtotal** | **$1,631.35 – $1,869.98** | |

### Allocation

1. **First $1,458.52 → ADBE**, completing the documented 17-share target (10 → 17 sh). Unambiguous.
2. **Remainder (≈$172.83 – $411.46) — same two options as 2026-06-29, unresolved:**
   - **Option A (conservative):** remainder → cash. No new TRN allocation until the `REPLACED` 900-share order is manually verified in TWS/Client Portal.
   - **Option B (continue the pattern):** remainder → a further small TRN top-up, consistent with the partial-fill-then-top-up pattern already used for ADBE and TRN.

**Watchlist sweep — no new destinations found.** Checked every `not-in-portfolio` evaluation since the last rebalance: **CRCL** (Quality Score 69.0, fails 80.0+ gate — [2026-06-30 session](2026-06-30-new-position-crcl.md)), **AMD** (Quality Score 55.7, fails gate — [2026-06-30 session](2026-06-30-new-position-amd.md)), **OUST** (hard FCF-positivity disqualifier — [2026-07-01 session](2026-07-01-new-position-oust.md)). None qualify as recycling destinations.

---

## 6. Upgrade 4 — Turnaround Sub-Gate Review Check

Searched [override-log.md](../portfolio/override-log.md) and `decisions/` for any position **entered** under the Turnaround Sub-Gate ("Conditional Watch, 2–3% max," mandatory 2-quarter review).

**Result: none found — same conclusion as all four prior months.** The Override Log carries one entry (AVGO, a valuation override, not a Turnaround Sub-Gate entry).

**No turnaround-review-due items this month** under the strict "entered via Upgrade 4" reading. **Note carried forward:** NKE's own 2026-07-01 rescore ([session](2026-07-01-rescore-nke.md) §10) recommends, for the **third consecutive rescore** (2026-06-07, 2026-06-20, 2026-07-01), formally converting NKE's standing value-trap override into a documented Upgrade 4 Turnaround Sub-Gate entry + `override-log.md` row — this has not been done, so NKE is not yet trackable under this section's mechanical check, but the underlying recommendation is now overdue.

---

## 7. Other open items carried forward

| Ticker | Status | Carried from | This session's note |
|---|---|---|---|
| **RGL** | Ungoverned position, actively growing via a live order | **New this session** | See §0 — priority item, recommend immediate TWS/Client Portal review and an `override-log.md` entry (added below). |
| **MBGL** | Ungoverned position, likely corporate-action-sourced | **New this session** | See §0 — low urgency ($20.25), needs source investigation. |
| **AVGO** | Score 69.5, predates 2026-06-20 modifier, 3.94% | [2026-06-22](2026-06-22-rebalance.md) §7 | **3rd consecutive month.** [watchlist/STALE.md](../watchlist/STALE.md) still lists AVGO as current under the 2026-06-29 methodology's own note flagging the unresolved 2026-06-20 contradiction. Override rationale still not on record. |
| **STIM** | "Not scored — going-concern override," 1.13% | [2026-06-07](2026-06-07-rebalance.md) §6 | **5th consecutive month unaddressed.** Standing Phase 06 exit-review trigger, independent of the monthly cycle. |
| **RBRK** | "Not scored — fails quality gates," 0.43% | [2026-06-07](2026-06-07-rebalance.md) §6 | **5th consecutive month unaddressed.** Needs an `override-log.md` entry. |
| **VEEV** | Blank score/review, 0.95% | [2026-06-15](2026-06-15-rebalance.md) §1 | **4th consecutive month unaddressed.** Still needs `/rescore`; no entry record anywhere. |
| **TLT** | 29.09%, non-equity, no methodology | [2026-06-07](2026-06-07-rebalance.md) §6 | See §4 — 5 consecutive months carried forward. |
| **NKE — STALE.md registry gap** | Registry-maintenance note | New this session | NKE's pre-rescore score (43.1, scored 2026-06-20) was never added to [watchlist/STALE.md](../watchlist/STALE.md)'s 2026-06-29 methodology table, even though every other in-portfolio numeric-scored holding was. Self-resolved by the 2026-07-01 rescore (NKE is now current), but flagged as the same class of registry-bookkeeping gap noted for MA in the 2026-06-29 session. |

---

## 8. Summary table — proposed actions

| Ticker | Score | Weight | Proposed action | Driven by |
|---|---|---|---|---|
| **RGL** | not scored | 0.03% | **Urgent: verify/cancel the live 60,000-share GTC order in TWS/Client Portal; log rationale in `override-log.md` (added below) or unwind** | Governance — ungoverned position (§0) |
| **MBGL** | not scored | 0.04% | Investigate source (likely corporate action); no action pending that | Governance — ungoverned position (§0) |
| **AMZN** | 73.4 | 9.75% | Trim 6–7 sh from IBKR leg (~$1,432–$1,670, ~26–30%) → recycle | Valuation (Phase 05) |
| **CSGP** | 79.0 | 1.25% | Trim 7 sh (~$200, 28%) → recycle | Valuation (Phase 05) |
| **GOOG** | 73.1 | 0.62% | Trim triggered but not executable (1 sh); standing sell-limit @ $389 unchanged | Valuation (Phase 05) — execution gap |
| **SPOT** | 80.5 | 0.81% | Trim triggered but not executable (1 sh); standing sell-limit @ $518 unchanged | Valuation (Phase 05) — execution gap |
| **MSFT** | 33.9 | 14.71% | Hold — cap breach resolved this session, no trim needed | Concentration (Upgrade 7) — resolved |
| **TLT** | n/a | 29.09% | No action — unresolved structural gap, 5th consecutive month | Framework gap |
| **ADBE** | 0.0 | 3.65% | Recycling destination: $1,458.52 completes the 17-sh target | Recycling (Phase 05) |
| **TRN** | 10.0 | 2.86% | Recycling destination (~$2,597 gap); allocation deferred pending TWS order verification | Recycling (Phase 05) — order-status caveat |
| **META** | 17.2 | 7.18% | Qualifies on score, zero executable headroom to 8% ceiling | Recycling (Phase 05) — sizing gap |
| **AVGO** | 69.5 (stale) | 3.94% | No action — methodology-stale, missing override rationale, 3rd consecutive month | Data integrity / governance |
| **VEEV** | blank | 0.95% | Needs `/rescore` — 4th consecutive month | Data gap |
| DUOL, NFLX, NOW, NVDA, UBER, V, ZS, NKE, NVO, SPGI | 30.0–69.9 | ~20.6% combined | Hold — Cheap/Fair Value bands, no trim | Valuation (Phase 05) |
| STIM, RBRK | not scored | 1.56% combined | Carried forward, 5th consecutive month | Fundamental (Phase 06) / governance |

**Recommended sequencing:**
1. **Resolve RGL first** — verify the live 60,000-share order in TWS/Client Portal; cancel if unintended, or supply rationale for the `override-log.md` entry below if intentional.
2. Run `/sync-portfolio` to bring `holdings.md` current (onboards or removes RGL/MBGL, refreshes cash/FX).
3. Execute (or re-propose) the AMZN/CSGP trims; route $1,458.52 of proceeds to ADBE.
4. Verify the TRN `REPLACED` 900-share order in TWS/Client Portal (now 4 sessions overdue).
5. Resolve the AVGO data-integrity flag and the RBRK override-log gap (both 3rd–5th consecutive month).
6. `/rescore VEEV` (4th consecutive month with no score at all).
7. TLT's structural gap remains a standalone framework-development item (5 consecutive months carried forward).

*Session complete. No trades executed — this is a proposal for human review. Log any executed trims/exits in `decisions/` and refresh `holdings.md` via `/sync-portfolio` once they settle.*

---

## Glossary

- **Corporate action:** an event initiated by a company (e.g., a spin-off, merger, or stock dividend) that changes shareholders' holdings without a discretionary trade — the likely explanation for MBGL's $0 cost basis (§0).
- **Composite Score:** this framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; see [quality-scoring.md](../framework/quality-scoring.md).
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

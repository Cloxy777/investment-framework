# 2026-09-27 — Rebalance Session (Monthly Rebalance / Trim Review)

**Task type:** REBALANCE
**Scope:** Portfolio-wide trim/hold/exit review across [holdings.md](../portfolio/holdings.md), applying Phase 05 (Dynamic Trimming) and Phase 06 (Exit Triggers) from [strategy.md](../framework/strategy.md) to current scores, plus the Upgrade 7 15% single-position cap. This falls under Routine 5's monthly cadence ([automation-schedule.md](../framework/automation-schedule.md)), run a few weeks after the [2026-09-07 session](2026-09-07-rebalance.md) at the user's request.

**No trades executed. This is a proposal for human review only.**

---

## 0. Rule 0 — live data pull vs. the 2026-09-20 sync, and two new undocumented fills

Per Rule 0, live `get_account_positions`, `get_account_balances`, `get_account_orders`, and `get_account_trades` (DAYS_7) were pulled directly from IBKR rather than relying on [holdings.md](../portfolio/holdings.md)'s 2026-09-20 sync (7 days old).

**🚨 Two undocumented fills since the last sync — both change actual portfolio composition:**

| Ticker | What happened | Evidence |
|---|---|---|
| **ADBE** | Share count **doubled, 10 → 20** | Trade confirmed: `BUY 10 ADBE @ $240.00 LIMIT GTC`, filled 2026-09-22T15:37:13Z, order 1071856795, net $2,400.00. No `sessions/`, `decisions/`, or `override-log.md` entry authorizes this. holdings.md's 2026-09-20 sync (pre-dating this fill) still shows the old 10-share weight (4.06%); live weight is now **7.64%** (§4 table). |
| **BKNG (Booking Holdings)** | A previously-flagged *undocumented pending order* has now **filled into a live 10-share position** — and BKNG has **never appeared as a row in `holdings.md` at all** | Trade confirmed: `BUY 10 BKNG @ $159.00 LIMIT GTC`, filled 2026-09-23T13:32:36Z, order 483688084, net $1,590.00. This is the same order flagged as undocumented and open across multiple prior syncs (e.g. [2026-09-07 session](2026-09-07-rebalance.md) §7: "BKNG order — remains open and undocumented across multiple syncs"). It has now filled — the position exists live at **2.67% weight** (§4) with **no Phase 01/02 evaluation ever run**, the same governance pattern as RGL and MBGL below. |

Neither fill is a Phase 03 entry, Phase 05 trim, or Phase 06 exit under this framework's own rules — both are undocumented human actions outside the system. Flagged here per Rule 0; **not** treated as authorized by this session. Recommend an `override-log.md` entry for each (Valuation override for ADBE — see note below; Quality waiver for BKNG, no evaluation exists) and a retroactive rationale from the user.

**Note on ADBE specifically:** its last Composite Score (8.4, Very Cheap) calls for a "Full position — 6–8% of portfolio" under Phase 03, and the new 7.64% weight happens to land inside that band — so this fill is directionally *consistent* with the framework's own sizing guidance, even though it was never logged as a deliberate Phase 03 entry. That coincidence doesn't resolve the governance gap (no `sessions/`/`decisions/` record), but it's a materially different situation from BKNG, which has no evaluation to be consistent or inconsistent with.

**Other order-book changes noticed while pulling live orders (informational, not this session's focus):**
- The previously-flagged undocumented **TSM ($369 BUY), NVDA ($199.56 BUY), and PDD** orders no longer appear in the live order book, and none of those tickers shows a new position — most likely cancelled or expired rather than filled. Worth a manual TWS confirmation, but no portfolio-composition impact found.
- The previously-flagged **AVGO BUY 5 @ $310.60** order (contradicting the 2026-09-15 AVGO rescore's HOLD call) is also gone from the live order book; AVGO's share count is unchanged at 6 — appears cancelled, not filled. Good news if confirmed, but unconfirmed by this session.
- The **TRN BUY 900 @ £1.756 GTC** order (order 1528612089) is still present but its status changed to **`PENDING_CANCEL`** as of 2026-09-26T14:25:58Z — someone/something has initiated cancelling it since the last sync. Not yet fully cancelled as of this pull; worth confirming it clears.
- Three other working GTC orders exist that predate this framework's visibility window and aren't newly concerning: `SELL 1 GOOG @ $389`, `SELL 20 NKE @ $54.20`, `SELL 25 CSGP @ $35.50` (REPLACED status), plus **still-open** `BUY 9 V @ $285` and `BUY 4 MA @ $464` and `BUY 20 NOW @ $80` — all carried forward from the 2026-07-05 weekly brief per prior sessions, unchanged. Full order reconciliation is `/safe-guard` and `/update-orders`' scope, not `/rebalance`'s — noted here only because they surfaced during the Rule 0 pull.

**Live totals used for this session (superseding the 2026-09-20 sync for weights):**
- IBKR Net Liquidation Value (BASE/USD): **$50,737.75** (`get_account_balances`, consolidated across USD/EUR/GBP/AUD segments at live FX)
- Freedom Finance: **$10,889.96** implied total (unchanged — last screenshot 2026-08-22, no live API, per [sync-sop.md](../portfolio/sync-sop.md))
- **Combined total this session: $61,627.71** (vs. $61,220.66 at the 2026-09-20 sync — up modestly, mostly the ADBE/BKNG buys plus ordinary price drift)

---

## 1. Staleness check (operating-calendar.md)

Two holdings are already flagged stale in `holdings.md` itself, via open Rule 9 GitHub issues, and remain unresolved:

| Ticker | Issue | Trigger | Due | Days overdue (as of 2026-09-27) |
|---|---|---|---|---|
| **RBRK** | [#801](https://github.com/Cloxy777/investment-framework/issues/801) | +15.4% move 2026-09-14, no earnings catalyst found | 2026-09-17 | **10 days** |
| **ZS** | [#802](https://github.com/Cloxy777/investment-framework/issues/802) | +16.3% move 2026-09-14, no earnings catalyst found | 2026-09-17 | **10 days** |

Both issues remain **open** (confirmed via live GitHub search this session). Both tickers have moved further since: RBRK now $109.55 (live), ZS now $193.02 (live) — both up again from the $107.00/$198.15 levels noted in the 2026-09-20 `holdings.md` flag (ZS has pulled back slightly from that peak; RBRK has continued higher).

`yfinance`/live earnings-calendar cross-check for the rest of the book was not independently re-run this session (no open `rescore-due` issue exists for any other ticker per the live GitHub search) — this mirrors the approach in the [2026-09-07 session](2026-09-07-rebalance.md) §1, relying on Routine 1's issue-tracking as the staleness signal rather than re-deriving it. **RBRK and ZS are the only holdings flagged stale.** Per [quality-scoring.md](../framework/quality-scoring.md) and this framework's own Composite Score gate, RBRK carries no numeric score at all (fails quality gates) and ZS's Composite (44.3) is shown below for reference only, not as a reliable trim/hold basis.

**Action: run `/rescore RBRK` and `/rescore ZS` before either score is used for any further trim/hold decision.**

---

## 2. Phase 05 — Dynamic Trimming (Valuation-Driven)

Per [strategy.md](../framework/strategy.md) Phase 02/05, the **Composite Score** (Quality + Valuation, 50/50) is the correct lookup for Phase 05's action bands — and only for holdings whose Quality Score clears the 80.0+ gate; otherwise the Composite is reference-only (per [quality-scoring.md](../framework/quality-scoring.md)), regardless of how `holdings.md` happens to annotate it.

| Band | Tickers (Composite Score) — gate-passing only |
|---|---|
| 90.0–100.0 (trim to 1–2%) | **None** |
| 80.0–89.9 (trim to 50%) | **None** |
| 70.0–79.9 (trim 25–30%) | **None** |
| 50.0–69.9 (hold, watch only — no trim) | DUOL (51.0, Quality 83.2) |
| 30.0–49.9 (hold, Cheap) | AVGO (42.3, Quality 86.3), V (34.5, Quality 85.6), VEEV (40.0, Quality 86.0) |
| 0.0–29.9 (Very Cheap — recycling candidates) | ADBE (8.4, Quality 83.3), META (26.0, Quality 87.5) |
| n/a — Composite not adopted (Quality <80.0) | MSFT (29.5, Quality 79.9 — fails by 0.1), AMZN (63.0, Quality 56.7), CSGP (57.8, Quality 69.2), GOOG (46.4, Quality 71.4), NFLX (39.8, Quality 69.8), NKE (47.5, Quality 39.5), NOW (51.4, Quality 73.2), NVO (42.1, Quality 67.2), SPGI (31.8, Quality 67.7), TRN (21.8, Quality 66.4), UBER (39.1, Quality 59.3), ZS (44.3, Quality 59.4 — ⚠️ also stale, §1) |
| n/a — no Phase 02 score at all | MBGL (Quality 51.0, fails gate), RBRK (fails quality gates, ⚠️ stale, §1), RGL (ungoverned, no evaluation ever run), BKNG (🚨 ungoverned, no evaluation ever run — new this session, §0), TLT (non-equity, framework gap), XEON (cash-equivalent, out of scope) |

**Result: zero Phase 05 trim triggers fire this month.** The highest gate-passing Composite Score on the book is DUOL at 51.0 — squarely "Fair Value, hold and watch," nowhere near the 70.0 trim threshold. This continues the pattern of every rebalance session on file (see [2026-09-07](2026-09-07-rebalance.md) §2 and earlier). Twelve of the book's twenty-six positions have a Quality Score below 80.0 and therefore no usable Composite for a trim/hold call at all — a large and growing share of the book sits outside what Phase 05 can mechanically act on.

---

## 3. Phase 06 — Full Exit Triggers

**None fired.** No holding sits in the 90.0–100.0 sustained-2-quarters band (§2). No fundamental-deterioration, growth-thesis-broken, or balance-sheet-crisis signal surfaced from this session's scope (a full Phase 04 qualitative review is outside `/rebalance`'s mechanical checks — this reflects the last documented `/rescore` for each name, not fresh qualitative research this session).

RBRK's standing "not scored" exit-review flag is unchanged (still fails Phase 01 quality gates; no `override-log.md` entry exists despite this being long overdue — carried forward, see §6).

---

## 4. Upgrade 7 — 15% Single-Position Cap Check

Using this session's live combined total of **$61,627.71** (§0): **15% cap = $9,244.16.**

| Ticker | Combined Value (live) | Weight | Breach? | Action |
|---|---|---|---|---|
| **TLT** | $17,617.54 (IBKR $7,938.00 @ 100 sh live + Freedom24 $9,679.54 @ 118 sh, last screenshot 2026-08-22) | **28.59%** | **Yes — by $8,373.38 (13.59pp)** | **Carried forward — unresolved for many consecutive months** (see [2026-09-07](2026-09-07-rebalance.md) §4 and every prior rebalance session). No fixed-income valuation/sizing methodology exists in this framework. Recommend this graduate from a routine monthly re-flag to a dedicated framework-development session, as every recent rebalance session has also recommended. |
| MSFT | $8,804.30 (IBKR only, 17 sh; Freedom24 leg confirmed sold) | 14.29% | No — but closest active approach to the cap on record | Up from 13.66% at the 2026-09-07 session, on price appreciation alone (no share-count change) — MSFT's live price has risen from ~$499 to $517.90. Only **$439.86** of headroom remains before a breach. Worth flagging for the user given its history of two breaches in three months from price appreciation alone; no share change occurred, so no action triggered by Phase 05/06, but this is the name to watch first if the book rallies further. |
| **ADBE** | $4,710.00 (IBKR, 20 sh — doubled this week, §0) | 7.64% | No | New weight, but well clear of the cap. See §0 for the governance flag on how it got here. |
| DUOL | $5,471.64 (IBKR $4,306.20 @ 30 sh + Freedom24 $1,165.44, last screenshot) | 8.88% | No | — |
| NVDA | $4,274.96 | 6.94% | No | — |
| All other holdings | ≤6.07% (META, the next-highest) | — | No | — |

**Result: one active breach — TLT, unchanged in substance from every prior session — plus MSFT now materially closer to the cap than at the last session.**

---

## 5. Recycling Plan

Per Phase 05, "proceeds always reinvested into current Score 0.0–29.9 names only." **No trim fired this session (§2, §4) — there are no proceeds to recycle this month.** For visibility, the current gate-passing Score 0.0–29.9 destinations (should a future trim or fresh capital become available) are:

| Ticker | Composite Score | Current Weight (live) | Room to 6–8% Phase 03 target | Notes |
|---|---|---|---|---|
| **ADBE** | 8.4 | 7.64% | Already inside the 6–8% band (post the undocumented 09-22 buy, §0) | Deepest "Very Cheap" score on the book, unstale, and now already fully sized under Phase 03's own guidance — governance gap aside, no further headroom to add. |
| META | 26.0 | 6.07% | ~$1.75–$2,660 (to reach 6.5–8%) | Meaningful headroom remains; unstale, current score (26 Aug PM review). |
| TRN (ref only, gate fail) | 21.8 | 2.51% | n/a | Not a usable destination — Quality Score fails the 80.0 gate, and the CMA "drip pricing" probe (still open) is an independent reason not to add. |

**Effectively, ADBE's usual role as the primary recycling destination is now already filled** by the undocumented 2026-09-22 buy — a further reason that fill needs a retroactive rationale rather than being left as an ungoverned event: if capital does free up next month, META is now the more clearly available destination.

---

## 6. Other open items carried forward (from [holdings.md](../portfolio/holdings.md)'s 2026-09-20 sync and [override-log.md](../portfolio/override-log.md) — not re-investigated in full this session, out of `/rebalance`'s scope except where the live pull in §0 surfaced new information)

| Ticker/Item | Status |
|---|---|
| **ADBE** | 🚨 New this session — share count doubled 10→20 via an undocumented 2026-09-22 buy. See §0. Needs an `override-log.md` entry + retroactive rationale. |
| **BKNG** | 🚨 New this session — previously-flagged pending order has filled into a live, ungoverned 10-share position with zero Phase 01/02 evaluation and no `holdings.md` row. See §0. Needs a `/new-position`-style retroactive evaluation or an `override-log.md` Quality-waiver entry, same pattern as RGL/MBGL. |
| **TSM, NVDA, PDD, AVGO orders** | The four previously-flagged undocumented pending orders no longer appear in the live order book and no matching position changes were found — most likely cancelled/expired. Improvement over prior sessions, but unconfirmed; recommend a manual TWS check to close the loop. |
| **TRN order** | BUY 900 @ £1.756 GTC (order 1528612089) — status changed to `PENDING_CANCEL` as of 2026-09-26, not yet fully cleared. Still contradicts the 2026-09-10 rescore's HOLD/no-top-up call while it remains even partially live. |
| **TLT short call (order 1040104046)** | Still absent from the live orders fetch — worth a manual TWS check for fill/expiry/cancellation, per every recent sync. |
| **SPOT** | 1-share position and its matching GTC sell order both remain absent from live IBKR data pulled this session — still unresolved, per [holdings.md](../portfolio/holdings.md). |
| **Cash jump** | +$2,523.36 unexplained jump flagged 2026-08-09, still unresolved. |
| **AVGO override-log status** | "Open — under review" text is stale (score was resolved 2026-07-04) — still not corrected. |
| **RGL** | Ungoverned 60,000-share ASX micro-cap position, no Phase 01/02 evaluation ever run — same standing gap as BKNG now shares. |
| **MBGL** | Ungoverned 1-share position, formally evaluated 2026-08-09 (Quality Score 51.0, fails gate) — HOLD, no forced action. |
| **RBRK** | Still carries no `override-log.md` entry despite a standing exit-review flag and the stale Rule 9 rescore (§1). |
| **NOW** | Weight still carries the 2026-08-10 undocumented 3-share trim — unresolved. |
| **TRN** | CMA "drip pricing" investigation still open per the 2026-09-10 rescore. HOLD, no top-up. |

---

## 7. Summary table — proposed actions

| Ticker/Item | Score | Weight (live) | Proposed action | Driven by |
|---|---|---|---|---|
| **TLT** | n/a, non-equity | 28.59% | No mechanical action proposed — unresolved structural framework gap, carried forward for many consecutive months; recommend escalating to a dedicated framework-development session | Upgrade 7 — hard cap, no methodology exists |
| **RBRK, ZS** | not scored / Composite 44.3 (⚠️ both stale) | 0.53% / 0.31% | Run `/rescore RBRK` and `/rescore ZS` before either score is used for any further trim/hold decision — both 10 days past their Rule 9 due date | Staleness (operating-calendar.md), issues [#801](https://github.com/Cloxy777/investment-framework/issues/801)/[#802](https://github.com/Cloxy777/investment-framework/issues/802) |
| **ADBE** | Composite 8.4 (Quality 83.3) | 7.64% | Log the 2026-09-22 doubling in `override-log.md` with the user's rationale — sizing happens to already match Phase 03's 6–8% band for this score, but was never a documented decision | Governance (Rule 0 finding, §0) |
| **BKNG** | not scored — no evaluation ever run | 2.67% | Log the fill in `override-log.md` (Quality waiver, same pattern as RGL) and/or run a retroactive `/new-position` evaluation | Governance (Rule 0 finding, §0) |
| MSFT | Composite 29.5, ref only (Quality 79.9 fails gate by 0.1) | 14.29% | Hold — no trim available (Composite not adopted); flag as closest to the 15% cap on the book, worth monitoring if price continues rising | Upgrade 7 proximity |
| All other scored equities | 8.4–63.0 bands | ~57% combined | Hold — no trim, no exit | Phase 05/06 — clean this month |
| **Recycling plan** | — | — | No proceeds this month (zero trims fired); META is now the primary informational destination should capital free up (ADBE's own headroom is largely used up by §0's undocumented buy) | Phase 05 recycling principle |
| TSM/NVDA/PDD/AVGO orders, TRN order, TLT short call, SPOT, cash jump, AVGO override text, RGL, MBGL, RBRK override gap, NOW, TRN CMA probe | — | — | Carried forward — see §6 for what's new vs. unchanged this session | Governance |

**Recommended sequencing:**
1. **Confirm and log the ADBE and BKNG fills** (§0) — these are the most consequential findings this session: two ungoverned trades that materially changed portfolio composition since the last sync.
2. **Run `/rescore RBRK` and `/rescore ZS`** — both 10 days past their Rule 9 due date (issues #801/#802 still open).
3. **TLT's structural cap breach** still warrants a dedicated framework-development session rather than continued monthly re-flagging; MSFT is now the second name to watch on cap proximity.
4. Confirm the TRN order's pending cancellation actually clears, and manually verify the TLT short call and SPOT position/order directly in TWS/Client Portal.
5. Confirm the unexplained cash jump, correct the AVGO override-log status text, and formalize the RBRK/RGL/BKNG override-log gaps — all long overdue.

*Session complete. No trades executed — this is a proposal for human review. Log any executed trims in `decisions/` and refresh `holdings.md` via `/sync-portfolio` once the ADBE/BKNG fills and the RBRK/ZS rescores are addressed.*

---

## Glossary

- **Composite Score:** this framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; drives Phase 03/05 action-table lookups once a Quality Score exists — see [quality-scoring.md](../framework/quality-scoring.md).
- **FX (foreign exchange) rate:** the price of converting one currency into another; this framework only uses live, broker-reported FX rates, never an assumed rate, per Rule 0.
- **GTC (Good-Til-Cancelled):** an order instruction telling the broker to keep a limit order open indefinitely until it fills or is manually cancelled.
- **Human Override:** a position opened or held outside the framework's own rules. Tracked for life in `override-log.md`.
- **Hybrid Upgrade:** one of 7 framework-specific rule additions layered on the base 6-phase strategy (Upgrade 7 = the 15% position cap).
- **NLV (Net Liquidation Value) / NAV (Net Asset Valuation):** a broker's headline account value — all positions at current market price, plus cash, minus liabilities (IBKR calls this NLV, Freedom24 calls it NAV).
- **Quality Score:** this framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02 and for the Composite Score to be usable for trim/hold decisions.
- **Rule 0:** this framework's non-negotiable requirement to pull live prices/data before any calculation, never inferring or estimating financial figures.
- **Rule 9:** this framework's rule requiring an immediate re-score after any >15% unexplained price move or a defined fundamental trigger (earnings, guidance, M&A, management change, macro shift).
- **Stale score:** a Last Review date that predates a holding's most recent earnings release, or an unresolved Rule 9 trigger — the score must be refreshed via `/rescore` before it's used for a trim/hold decision.
- **Valuation Score:** this framework's 0.0–100.0 continuous score (0.0 = cheapest, 100.0 = most expensive).
- **Watchlist (action band):** the framework's recommendation for a Composite Score of 50.0–69.9: fairly-to-fully valued, "no new entry, no trim." (Distinct from the repo's `watchlist/` directory.)

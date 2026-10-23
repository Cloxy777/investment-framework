# 2026-10-05 — Rebalance Session (Monthly Rebalance / Trim Review)

**Task type:** REBALANCE
**Scope:** Portfolio-wide trim/hold/exit review across [holdings.md](../portfolio/holdings.md), applying Phase 05 (Dynamic Trimming) and Phase 06 (Exit Triggers) from [strategy.md](../framework/strategy.md) to current scores, the Upgrade 7 15% single-position cap, and the Upgrade 4 Turnaround Sub-Gate review-due check. **This is Routine 5's first-Monday-of-the-month Monthly Rebalance / Trim Review** ([automation-schedule.md](../framework/automation-schedule.md)) — today (2026-10-05) is the first Monday of October.

**No trades executed. This is a proposal for human review only.**

---

## 0. Rule 0 — live data pull vs. the 2026-10-04 sync

Per Rule 0, live `get_account_positions`, `get_account_balances`, and `get_account_orders` were pulled directly from IBKR (account U19421206) rather than relying solely on [holdings.md](../portfolio/holdings.md)'s 2026-10-04 sync (one day old).

- **Every scored equity's share count is unchanged** from the 10-04 sync — no new undocumented trades to report this session. All 25 IBKR tickers match (ADBE 20, AMZN 12, AVGO 6, BKNG 10, CSGP 25, DUOL 30, GOOG 1, MBGL 1, META 5, MSFT 17, NFLX 12, NKE 20, NOW 9, NVDA 19, NVO 5, RBRK 3, RGL 60,000, SPGI 1, TLT 100, TRN 600, UBER 3, V 1, VEEV 3, XEON 10, ZS 1).
- IBKR Net Liquidation Value (BASE/USD): **$50,498.12**, up modestly from $50,411.80 at the 10-04 sync — ordinary price drift, nothing crossing the Rule 9 ±15% unexplained-move threshold.
- Freedom Finance leg unchanged (last screenshot 2026-08-22, per [sync-sop.md](../portfolio/sync-sop.md) — no live API): $10,889.96 implied total.
- **Combined total this session: $50,498.12 + $10,889.96 = $61,388.08** (vs. $61,301.76 at the 10-04 sync).
- **The TRN BUY 900 @ £1.756 order (1528612089) is now fully gone from the live order book** — resolved since the 09-26 `PENDING_CANCEL` status flagged in [holdings.md](../portfolio/holdings.md). Confirms that order no longer contradicts TRN's HOLD/no-top-up rescore call.
- Previously-flagged open orders unchanged and still undocumented: `BUY 20 NFLX @ 46.97`, `BUY 1800 LM8 @ 0.30` (not a holding), `BUY 5 AVGO @ 265.34`, `BUY 9 V @ 285`, `BUY 4 MA @ 464`, `BUY 20 NOW @ 80`, plus GOOG/CSGP/NKE sell-side orders carried from prior sessions (CSGP's sell re-appeared as a fresh `NEW` order at $35.55, a $0.05 reprice from the prior $35.50 `REPLACED` order — immaterial). The TLT short-call order and the SPOT position remain absent from live data, unresolved.

---

## 1. Staleness check (operating-calendar.md)

Three holdings are flagged stale via open Rule 9 / earnings-release GitHub issues, confirmed still open via live GitHub search this session:

| Ticker | Issue | Trigger | Due | Days overdue (as of 2026-10-05) |
|---|---|---|---|---|
| **RBRK** | [#801](https://github.com/Cloxy777/investment-framework/issues/801) | +15.4% move 2026-09-14, no earnings catalyst found | 2026-09-17 | **18 days** |
| **ZS** | [#802](https://github.com/Cloxy777/investment-framework/issues/802) | +16.3% move 2026-09-14, no earnings catalyst found | 2026-09-17 | **18 days** |
| **NKE** | [#870](https://github.com/Cloxy777/investment-framework/issues/870) | Earnings released 2026-10-01 | 2026-10-06 (3 business days) | Not yet due, but Last Review (11 Sep 2026) predates this release — stale as of now |

No other open `RESCORE:`-titled issue exists. **RBRK, ZS, and NKE are the only holdings flagged stale this session.** Per [quality-scoring.md](../framework/quality-scoring.md), RBRK carries no numeric score at all (fails quality gates); ZS's Composite (44.3, Quality 59.4) and NKE's Composite (47.5, Quality 39.5) are both reference-only regardless of staleness, since both already fail the 80.0+ Quality gate — the stale flag doesn't change their actionability (neither was usable for a trim/hold call even current).

**Action: run `/rescore RBRK`, `/rescore ZS`, and `/rescore NKE`** — RBRK/ZS now 18 days past due, NKE due 2026-10-06.

---

## 2. Phase 05 — Dynamic Trimming (Valuation-Driven)

Per [strategy.md](../framework/strategy.md) Phase 02/05, the **Composite Score** (Quality + Valuation, 50/50) is the correct lookup for Phase 05's action bands — and only for holdings whose Quality Score clears the 80.0+ gate; otherwise the Composite is reference-only (per [quality-scoring.md](../framework/quality-scoring.md)), regardless of how `holdings.md` happens to annotate it.

| Band | Tickers (Composite Score) — gate-passing only |
|---|---|
| 90.0–100.0 (trim to 1–2%) | **None** |
| 80.0–89.9 (trim to 50%) | **None** |
| 70.0–79.9 (trim 25–30%) | **None** |
| 50.0–69.9 (hold, watch only — no trim) | DUOL (51.0, Quality 83.2) |
| 30.0–49.9 (hold, Cheap) | AVGO (42.5, Quality 86.3), V (34.5, Quality 85.6), VEEV (40.0, Quality 86.0) |
| 0.0–29.9 (Very Cheap — recycling candidates) | ADBE (8.4, Quality 83.3), META (26.0, Quality 87.5), NVDA (23.0, Quality 90.3) |
| n/a — Composite not adopted (Quality <80.0) | MSFT (29.5, Quality 79.9 — fails by 0.1), AMZN (63.0, Quality 56.7), CSGP (57.8, Quality 69.2), GOOG (46.4, Quality 71.4), NFLX (39.8, Quality 69.8), NKE (47.5, Quality 39.5 — ⚠️ also stale, §1), NOW (51.4, Quality 73.2), NVO (42.1, Quality 67.2), SPGI (31.8, Quality 67.7), TRN (21.8, Quality 66.4), UBER (39.1, Quality 59.3), ZS (44.3, Quality 59.4 — ⚠️ also stale, §1) |
| n/a — no Phase 02 score at all | MBGL (Quality 51.0, fails gate), RBRK (fails quality gates, ⚠️ stale, §1), RGL (ungoverned, no evaluation ever run), BKNG (ungoverned — the Quality/Composite figures `holdings.md` carries for it trace to the 2026-08-05 "WATCHLIST ONLY — do not enter" session, never a completed Phase 01/02 evaluation; treated the same as every prior session), TLT (non-equity, framework gap), XEON (cash-equivalent, out of scope) |

**Result: zero Phase 05 trim triggers fire this month.** The highest gate-passing Composite Score on the book is DUOL at 51.0 — squarely "Fair Value, hold and watch," nowhere near the 70.0 trim threshold. This continues the pattern of every rebalance session on file (see [2026-09-27](2026-09-27-rebalance.md) §2 and earlier). Twelve of the book's twenty-six positions have a Quality Score below 80.0 and therefore no usable Composite for a trim/hold call at all.

---

## 3. Phase 06 — Full Exit Triggers

**None fired.** No holding sits in the 90.0–100.0 sustained-2-quarters band (§2). No fundamental-deterioration, growth-thesis-broken, or balance-sheet-crisis signal surfaced from this session's scope (a full Phase 04 qualitative review is outside `/rebalance`'s mechanical checks — this reflects the last documented `/rescore` for each name, not fresh qualitative research this session).

RBRK's standing "not scored" exit-review flag is unchanged (still fails Phase 01 quality gates; no `override-log.md` entry exists despite this being long overdue — carried forward, see §6).

---

## 4. Upgrade 7 — 15% Single-Position Cap Check

Using this session's live combined total of **$61,388.08** (§0): **15% cap = $9,208.21.**

| Ticker | Combined Value (live) | Weight | Breach? | Action |
|---|---|---|---|---|
| **TLT** | $17,399.54 (IBKR $7,720.00 @ 100 sh live + Freedom24 $9,679.54 @ 118 sh, last screenshot 2026-08-22) | **28.35%** | **Yes — by $8,191.33 (13.35pp)** | **Carried forward — unresolved for many consecutive months** (see [2026-09-27](2026-09-27-rebalance.md) §4 and every prior rebalance session). No fixed-income valuation/sizing methodology exists in this framework. Recommend this graduate from a routine monthly re-flag to a dedicated framework-development session, as every recent rebalance session has also recommended. |
| **MSFT** | $8,842.85 (IBKR only, 17 sh; Freedom24 leg confirmed sold) | **14.41%** | No — but closer to the cap than at the last two sessions | Up from 14.29% at 2026-09-27 and 13.66% at 2026-09-07, on price appreciation alone (no share-count change — live price risen to $520.17). Only **$365.36** of headroom remains before a breach. This is now the third consecutive monthly session flagging MSFT's unbroken climb toward the cap purely from price, worth escalating alongside the TLT discussion. |
| ADBE | $4,784.00 (IBKR, 20 sh) | 7.79% | No | Within the 6–8% Phase 03 band for its Composite Score (8.4). |
| DUOL | $5,485.44 (IBKR $4,320.00 @ 30 sh + Freedom24 $1,165.44, last screenshot) | 8.93% | No | — |
| NVDA | $4,470.70 | 7.28% | No | — |
| All other holdings | ≤5.91% (META, the next-highest) | — | No | — |

**Result: one active breach — TLT, unchanged in substance from every prior session — plus MSFT narrowing its headroom to the cap for a third straight month.**

---

## 5. Recycling Plan

Per Phase 05, "proceeds always reinvested into current Score 0.0–29.9 names only." **No trim fired this session (§2, §4) — there are no proceeds to recycle this month.** For visibility, the current gate-passing Score 0.0–29.9 destinations (should a future trim or fresh capital become available) are:

| Ticker | Composite Score | Current Weight (live) | Room to 6–8% Phase 03 target | Notes |
|---|---|---|---|---|
| **ADBE** | 8.4 | 7.79% | Already inside the 6–8% band — little room left | Deepest "Very Cheap" score on the book, unstale, but close to fully sized under Phase 03's own guidance. |
| META | 26.0 | 5.91% | ~$368–$1,278 (to reach 6.5–8%) | Meaningful headroom remains; unstale, current score (26 Aug PM review). |
| NVDA | 23.0 | 7.28% | Already inside the 6–8% band — little room left | Little headroom left before hitting its own Phase 03 ceiling. |
| TRN (ref only, gate fail) | 21.8 | ~2.50% | n/a | Not a usable destination — Quality Score fails the 80.0 gate, and the CMA "drip pricing" probe (still open) is an independent reason not to add. |

**META is the only destination with meaningful headroom left** — ADBE and NVDA are both already near the top of their own Phase 03 sizing bands, so if capital frees up next month (e.g. via a TLT resolution), META is the clearer recycling target.

---

## 6. Upgrade 4 — Turnaround Sub-Gate Review Check

Searched [override-log.md](../portfolio/override-log.md) and every file under `decisions/` for any position **entered** under the Turnaround Sub-Gate ("Conditional Watch, 2–3% max," mandatory 2-quarter review, the 5 conditions in [strategy.md](../framework/strategy.md)). No hits beyond the rule's own description — no position has ever actually been logged as entered under this gate.

**Result: none found — same conclusion as every prior month. No turnaround-review-due items this month.**

**Carried-forward recommendation, still not actioned:** NKE's [2026-07-01 rescore](2026-07-01-rescore-nke.md) §10 recommends formally converting NKE's standing value-trap override into a documented Upgrade 4 Turnaround Sub-Gate entry + `override-log.md` row. Still not done as of this session — and NKE is now also stale (§1, issue #870), so that formalization should wait for the pending `/rescore NKE`.

---

## 7. Other open items carried forward (from [holdings.md](../portfolio/holdings.md)'s 2026-10-04 sync and [override-log.md](../portfolio/override-log.md) — not re-investigated in full this session, out of `/rebalance`'s scope except where the live pull in §0 surfaced new information)

| Ticker/Item | Status |
|---|---|
| **TRN order** | ✅ Resolved this session — BUY 900 @ £1.756 GTC (order 1528612089) no longer appears in live orders at all, confirming the 09-26 `PENDING_CANCEL` completed. No longer contradicts TRN's HOLD/no-top-up call. |
| **ADBE** | 🚨 Undocumented 2026-09-22 doubling (10→20 shares) still has no `override-log.md` entry or retroactive rationale, per [2026-09-27 session](2026-09-27-rebalance.md) §0/§6. |
| **BKNG** | 🚨 Still an ungoverned 10-share fill with zero Phase 01/02 evaluation and no `override-log.md` entry — unresolved since first flagged. |
| **NFLX/AVGO/LM8/V/MA/NOW orders** | All still open, undocumented, unchanged this session — see §0. |
| **TLT short call (order 1040104046)** | Still absent from the live orders fetch — worth a manual TWS check for fill/expiry/cancellation, per every recent sync. |
| **SPOT** | 1-share position and its matching GTC sell order both remain absent from live IBKR data pulled this session — still unresolved, per [holdings.md](../portfolio/holdings.md). |
| **Cash jump** | +$2,523.36 unexplained jump flagged 2026-08-09, still unresolved. |
| **AVGO override-log status** | "Open — under review" text is stale (score was resolved 2026-07-04) — still not corrected. |
| **RGL** | Ungoverned 60,000-share ASX micro-cap position, no Phase 01/02 evaluation ever run. |
| **MBGL** | Ungoverned 1-share position, formally evaluated 2026-08-09 (Quality Score 51.0, fails gate) — HOLD, no forced action. |
| **RBRK** | Still carries no `override-log.md` entry despite a standing exit-review flag and the stale Rule 9 rescore (§1). |
| **NOW** | Weight still carries the 2026-08-10 undocumented 3-share trim — unresolved. |
| **TRN** | CMA "drip pricing" investigation still open per the 2026-09-10 rescore. HOLD, no top-up. |

---

## 8. Summary table — proposed actions

| Ticker/Item | Score | Weight (live) | Proposed action | Driven by |
|---|---|---|---|---|
| **TLT** | n/a, non-equity | 28.35% | No mechanical action proposed — unresolved structural framework gap, carried forward for many consecutive months; recommend escalating to a dedicated framework-development session | Upgrade 7 — hard cap, no methodology exists |
| **MSFT** | Composite 29.5, ref only (Quality 79.9 fails gate by 0.1) | 14.41% | Hold — no trim available (Composite not adopted); third straight month narrowing toward the 15% cap purely on price — flag for escalation alongside TLT | Upgrade 7 proximity |
| **RBRK, ZS, NKE** | not scored / Composite 44.3 / Composite 47.5 (⚠️ all stale) | 0.58% / 0.32% / 1.10% | Run `/rescore RBRK`, `/rescore ZS`, `/rescore NKE` before any score is used for a trim/hold decision | Staleness (operating-calendar.md), issues [#801](https://github.com/Cloxy777/investment-framework/issues/801)/[#802](https://github.com/Cloxy777/investment-framework/issues/802)/[#870](https://github.com/Cloxy777/investment-framework/issues/870) |
| All other scored equities | 8.4–63.0 bands | ~56% combined | Hold — no trim, no exit | Phase 05/06 — clean this month |
| **Recycling plan** | — | — | No proceeds this month (zero trims fired); META is the primary informational destination with real headroom left | Phase 05 recycling principle |
| ADBE, BKNG undocumented trades; NFLX/AVGO/LM8/V/MA/NOW orders; TLT short call; SPOT; cash jump; AVGO override text; RGL; MBGL; NOW trim | — | — | Carried forward — see §7 for what's new (TRN order resolved) vs. unchanged this session | Governance |

**Recommended sequencing:**
1. **Run `/rescore RBRK`, `/rescore ZS`, and `/rescore NKE`** — RBRK/ZS 18 days past their Rule 9 due date (issues #801/#802 still open), NKE newly due 2026-10-06 (#870).
2. **TLT's structural cap breach** still warrants a dedicated framework-development session rather than continued monthly re-flagging; MSFT is the second name to watch, now 3 straight months closer to the cap.
3. Formalize the ADBE/BKNG `override-log.md` gaps — long overdue, unchanged since first flagged.
4. Manually verify the TLT short call and SPOT position/order directly in TWS/Client Portal; confirm the unexplained cash jump.
5. Correct the AVGO override-log status text and formalize the RBRK override-log gap.

*Session complete. No trades executed — this is a proposal for human review. Log any executed trims in `decisions/` and refresh `holdings.md` via `/sync-portfolio` once the pending rescores are addressed.*

---

## Glossary

- **Composite Score:** this framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; drives Phase 03/05 action-table lookups once a Quality Score exists — see [quality-scoring.md](../framework/quality-scoring.md).
- **FX (foreign exchange) rate:** the price of converting one currency into another; this framework only uses live, broker-reported FX rates, never an assumed rate, per Rule 0.
- **GTC (Good-Til-Cancelled):** an order instruction telling the broker to keep a limit order open indefinitely until it fills or is manually cancelled.
- **Human Override:** a position opened or held outside the framework's own rules. Tracked for life in `override-log.md`.
- **Hybrid Upgrade:** one of 7 framework-specific rule additions layered on the base 6-phase strategy (Upgrade 4 = Turnaround Sub-Gate, Upgrade 7 = the 15% position cap).
- **NLV (Net Liquidation Value) / NAV (Net Asset Valuation):** a broker's headline account value — all positions at current market price, plus cash, minus liabilities (IBKR calls this NLV, Freedom24 calls it NAV).
- **Quality Score:** this framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02 and for the Composite Score to be usable for trim/hold decisions.
- **Rule 0:** this framework's non-negotiable requirement to pull live prices/data before any calculation, never inferring or estimating financial figures.
- **Rule 9:** this framework's rule requiring an immediate re-score after any >15% unexplained price move or a defined fundamental trigger (earnings, guidance, M&A, management change, macro shift).
- **Stale score:** a Last Review date that predates a holding's most recent earnings release, or an unresolved Rule 9 trigger — the score must be refreshed via `/rescore` before it's used for a trim/hold decision.
- **Turnaround Sub-Gate:** the conditional path (Hybrid Upgrade 4) letting a company failing some quality criteria still enter as a small (2–3%) position if it passes 5 specific tests.
- **Valuation Score:** this framework's 0.0–100.0 continuous score (0.0 = cheapest, 100.0 = most expensive).
- **Watchlist (action band):** the framework's recommendation for a Composite Score of 50.0–69.9: fairly-to-fully valued, "no new entry, no trim." (Distinct from the repo's `watchlist/` directory.)

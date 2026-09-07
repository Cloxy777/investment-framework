# 2026-09-07 — Rebalance Session (Monthly Rebalance / Trim Review)

**Task type:** REBALANCE
**Scope:** Portfolio-wide trim/hold/exit review across [holdings.md](../portfolio/holdings.md), applying Phase 05 (Dynamic Trimming) and Phase 06 (Exit Triggers) from [strategy.md](../framework/strategy.md) to current scores, the Upgrade 7 15% single-position cap, and the Upgrade 4 Turnaround Sub-Gate review-due check. **This is Routine 5's first-Monday-of-the-month Monthly Rebalance / Trim Review** ([automation-schedule.md](../framework/automation-schedule.md)) — today (2026-09-07) is the first Monday of September.

**No trades executed. This is a proposal for human review only.**

---

## 0. Rule 0 — live data pull vs. the 2026-09-06 sync

Per Rule 0, live `get_account_positions` / `get_account_balances` were pulled directly from IBKR (account U19421206) rather than relying solely on [holdings.md](../portfolio/holdings.md)'s 2026-09-06 sync (one day old).

- **Every scored equity's share count is unchanged** from the 09-06 sync — no undocumented trades to report this session.
- IBKR Net Liquidation Value: **$51,280.40** (BASE currency), up modestly from $51,245.21 at the 09-06 sync — ordinary price drift, nothing crossing the Rule 9 ±15% unexplained-move threshold.
- Freedom Finance leg unchanged (last screenshot 2026-08-22, per [sync-sop.md](../portfolio/sync-sop.md) — no live API): $10,889.96 implied total.
- **Combined total this session: $51,280.40 + $10,889.96 = $62,170.36** (vs. $62,135.17 at the 09-06 sync).
- `yfinance` remains unreachable in this environment this session (no `curl_cffi`/`yfinance` package installed, and this environment's prior TLS-handshake workaround from the [2026-08-03 session](2026-08-03-rebalance.md) §0 doesn't apply here) — the independent earnings-date staleness cross-check that session ran could not be repeated. Staleness below relies on Routine 1's `rescore-due` issue-tracking mechanism instead (see §1).
- All 24 IBKR positions carry undocumented/unresolved order and position flags already logged in [holdings.md](../portfolio/holdings.md) (TSM and NVDA orders contradicting current analysis, the vanished TLT short-call order, SPOT's still-missing position, the still-unresolved +$2,523.36 cash jump) — out of `/rebalance`'s scope, carried forward unchanged, see §7.

---

## 1. Staleness check (operating-calendar.md)

With `yfinance` unreachable this session (§0), staleness relies on Routine 1's earnings-detection mechanism: an open `RESCORE:` GitHub issue means Routine 1 confirmed an earnings release postdating the holding's Last Review.

**One open `rescore-due` issue found:** [#709 — "RESCORE: ZS - earnings released 2026-09-03"](https://github.com/cloxy777/investment-framework/issues/709). ZS's Last Review in [holdings.md](../portfolio/holdings.md) is 05 Jul 2026 — clearly stale against the 2026-09-03 earnings release.

No other open `RESCORE:`-titled issue exists, and no other holding's Last Review date is more than one earnings cycle old based on the last several `/rescore` sessions on file (AVGO 03 Sep, DUOL 01 Sep, NVDA 04 Sep, MCD 06 Sep — all current). **ZS is the only holding flagged stale this session** — its Composite Score (41.9) is shown below for reference only, not as a reliable basis for a trim/hold call.

---

## 2. Phase 05 — Dynamic Trimming (Valuation-Driven)

Per [strategy.md](../framework/strategy.md) Phase 02/05, the **Composite Score** (Quality + Valuation, 50/50) is the correct lookup for Phase 05's action bands, not the raw Valuation Score — and only for holdings whose Quality Score clears the 80.0+ gate (otherwise the Composite is reference-only, per [quality-scoring.md](../framework/quality-scoring.md)).

| Band | Tickers (Composite Score) |
|---|---|
| 90.0–100.0 (trim to 1–2%) | **None** |
| 80.0–89.9 (trim to 50%) | **None** |
| 70.0–79.9 (trim 25–30%) | **None** |
| 50.0–69.9 (hold, watch only) | AMZN (63.0), CSGP (57.8), DUOL (51.0), NOW (51.4 — ref only, Quality Score 73.2 fails gate) |
| 30.0–49.9 (hold, Cheap) | AVGO (40.2), GOOG (46.4), NFLX (39.8), NKE (34.8), NVO (42.1 — ref only, Quality Score 67.2 fails gate), SPGI (31.8), UBER (44.1), V (34.5), VEEV (40.0), ZS (41.9 — ⚠️ stale, §1) |
| 0.0–29.9 (Very Cheap — recycling candidates) | ADBE (8.1), META (26.0), NVDA (24.1), TRN (21.4 — ref only, Quality Score 67.2 fails gate) |
| n/a — Composite not adopted | MSFT (29.5, reference only — Quality Score 79.9 fails the 80.0 gate by 0.1) |
| n/a — no Phase 02 score | MBGL, RBRK, RGL, TLT, XEON (quality-gate fail / ungoverned / non-equity / cash-equivalent) |

**Result: zero Phase 05 trim triggers fire this month.** The highest Composite Score on the book is AMZN at 63.0 — comfortably inside "Fair Value, hold and watch," nowhere near the 70.0 trim threshold. This continues the pattern of every rebalance session on file (see [2026-08-03](2026-08-03-rebalance.md) §2 and earlier).

**Caveat on ZS (§1):** its current Composite read (41.9) sits mid-band, well below the 70.0 trim threshold, so the stale score is unlikely to be concealing a live trim trigger — but per the operating brief this is a caveat, not a substitute for running `/rescore ZS`.

---

## 3. Phase 06 — Full Exit Triggers

**None fired.** No holding sits in the 90.0–100.0 sustained-2-quarters band (§2). No fundamental-deterioration, growth-thesis-broken, or balance-sheet-crisis signal surfaced from this session's scope (a full Phase 04 qualitative review is outside `/rebalance`'s mechanical checks — this reflects the last documented `/rescore` for each name, not fresh qualitative research this session).

RBRK and STIM's standing "not scored" exit-review flags: RBRK still fails Phase 01 quality gates (no change); STIM's going-concern override was resolved via forced option assignment on 2026-08-21 (see [override-log.md](../portfolio/override-log.md)) and no longer appears in holdings.md — nothing left to track there.

---

## 4. Upgrade 7 — 15% Single-Position Cap Check

Using this session's live combined total of **$62,170.36** (§0): **15% cap = $9,325.55.**

| Ticker | Combined Value (live) | Weight | Breach? | Action |
|---|---|---|---|---|
| **TLT** | $17,903.54 (IBKR $8,224.00 @ 100 sh live + Freedom24 $9,679.54 @ 118 sh, last screenshot 2026-08-22) | **28.80%** | **Yes — by $8,577.99 (13.80pp)** | **Carried forward — unresolved for many consecutive months** (see [2026-08-03](2026-08-03-rebalance.md) §4 and every prior rebalance session). No fixed-income valuation/sizing methodology exists in this framework (see [override-log.md](../portfolio/override-log.md) historical audit: "TLT — Asset class override... No exit criteria defined"). Recommend this graduate from a routine monthly re-flag to a dedicated framework-development session, as every recent rebalance session has also recommended. |
| MSFT | $8,489.99 (IBKR only, 17 sh; Freedom24 leg confirmed sold) | 13.66% | No | Resolved since the 2026-08-03 breach (16.77% → 13.66%) — the Freedom24-side sale plus no further price momentum kept it clear of the cap this month. Second-highest weight on the book; worth continued monitoring given its history of two breaches in three months from price appreciation alone. |
| DUOL | $5,803.89 (IBKR $4,638.45 @ 30 sh + Freedom24 $1,165.44, last screenshot) | 9.34% | No | — |
| NVDA | $4,360.25 | 7.01% | No | — |
| All other holdings | ≤4.99% (AMZN, the next-highest) | — | No | — |

**Result: one active breach — TLT, unchanged in substance from every prior session.** No new breach this month; MSFT's prior breach remains resolved.

---

## 5. Recycling Plan

Per Phase 05, "proceeds always reinvested into current Score 0.0–29.9 names only." **No trim fired this session (§2, §4) — there are no proceeds to recycle this month.** For visibility, the current Score 0.0–29.9 destinations (should a future trim or fresh capital become available) are:

| Ticker | Composite Score | Current Weight (live) | Room to 6–8% Phase 03 target | Notes |
|---|---|---|---|---|
| **ADBE** | 8.1 | 4.29% ($2,665.00 @ 10 sh) | ~$1,058–$2,309 | Deepest "Very Cheap" score on the book, unstale. **Primary destination if capital becomes available.** |
| **NVDA** | 24.1 | 7.01% ($4,360.25 @ 19 sh) | Already inside 6–8% target band | Little headroom left before hitting its own Phase 03 ceiling. |
| META | 26.0 | 4.95% ($3,075.99 @ 5 sh) | ~$695–$1,918 | Meaningful headroom; unstale, current score. |
| TRN (ref only, gate fail) | 21.4 | 2.53% | n/a | Not a usable destination — Quality Score fails the 80.0 gate, and the CMA "drip pricing" probe (still open, see [holdings.md](../portfolio/holdings.md)) is an independent reason not to add. |

No mandated allocation this month — this table is informational only, per Phase 05's recycling principle, in case the TLT structural review (§4) or a future trim frees capital.

---

## 6. Upgrade 4 — Turnaround Sub-Gate Review Check

Searched [override-log.md](../portfolio/override-log.md) and every file under `decisions/` for any position **entered** under the Turnaround Sub-Gate ("Conditional Watch, 2–3% max," mandatory 2-quarter review, the 5 conditions in [strategy.md](../framework/strategy.md)). No hits beyond the rule's own description — no position has ever actually been logged as entered under this gate.

**Result: none found — same conclusion as every prior month. No turnaround-review-due items this month.**

**Carried-forward recommendation, still not actioned:** NKE's [2026-07-01 rescore](2026-07-01-rescore-nke.md) §10 recommends formally converting NKE's standing value-trap override into a documented Upgrade 4 Turnaround Sub-Gate entry + `override-log.md` row. Still not done as of this session.

---

## 7. Other open items carried forward (from [holdings.md](../portfolio/holdings.md)'s 2026-09-06 sync and [override-log.md](../portfolio/override-log.md) — not re-investigated this session, out of `/rebalance`'s scope)

| Ticker/Item | Status |
|---|---|
| **TSM order** | BUY 10 @ $369.00 GTC, placed 2026-09-06 — contradicts the same-day new-position session's "WATCHLIST ONLY — do not enter" call (buy ceilings $258.88–$277.37). Undocumented, flagged for the user. |
| **NVDA order** | BUY 10 @ $199.56 GTC, placed 2026-08-31 — predates both the 2026-09-01 and 2026-09-04 rescores, neither of which records placing an order. Undocumented, flagged for the user. |
| **TLT short call (order 1040104046)** | No longer appears in the orders fetch — worth a manual TWS check for fill/expiry/cancellation. |
| **BKNG order** | BUY 10 @ $159.00 GTC — remains open and undocumented across multiple syncs. |
| **SPOT** | 1-share position and its matching GTC sell order both remain absent — 7 consecutive syncs, unconfirmed exit. |
| **Cash jump** | +$2,523.36 unexplained jump flagged 2026-08-09, still unresolved. |
| **AVGO** | Override-log's "Open — under review" status text is stale (score was resolved 2026-07-04) — still not corrected. |
| **RGL** | Ungoverned 60,000-share ASX micro-cap position, no Phase 01/02 evaluation ever run. |
| **DOCS** | Resolved 2026-08-21 (expired worthless) — governance gap noted, no further tracking needed. |
| **MBGL** | Ungoverned 1-share position, formally evaluated 2026-08-09 (Quality Score 51.0, fails gate) — HOLD, no forced action. |
| **RBRK** | Still carries no `override-log.md` entry despite a standing exit-review flag (fails Phase 01 quality gates). |
| **NOW** | Weight still carries the 2026-08-10 undocumented 3-share trim — unresolved. |
| **TRN** | CMA "drip pricing" investigation still open, no finding as of the 2026-08-31 rescore. HOLD, no top-up. |

---

## 8. Summary table — proposed actions

| Ticker/Item | Score | Weight (live) | Proposed action | Driven by |
|---|---|---|---|---|
| **TLT** | n/a, non-equity | 28.80% | No mechanical action proposed — unresolved structural framework gap, carried forward for many consecutive months; recommend escalating to a dedicated framework-development session | Upgrade 7 — hard cap, no methodology exists |
| **ZS** | Composite 41.9 (⚠️ stale) | 0.27% | Run `/rescore ZS` before its score is used for any further trim/hold decision | Staleness (operating-calendar.md), issue #709 |
| All other scored equities | 8.1–63.0 bands | ~63% combined | Hold — no trim, no exit | Phase 05/06 — clean this month |
| **Recycling plan** | — | — | No proceeds this month (zero trims fired); ADBE/NVDA/META listed as informational destinations should capital free up | Phase 05 recycling principle |
| NKE | Composite 34.8 (Quality 44.4 fails gate) | 1.24% | Hold existing, do not add; formalize Turnaround Sub-Gate entry (still overdue) | Governance / Upgrade 4 |
| RBRK | not scored | 0.45% | Carried forward, unaddressed | Fundamental (Phase 06) / governance |
| TSM order, NVDA order, BKNG order, TLT short call, SPOT, cash jump, AVGO, RGL, DOCS, MBGL, NOW, TRN | — | — | Carried forward from 09-06 sync — no new findings this session | Governance (§7) |

**Recommended sequencing:**
1. **Run `/rescore ZS`** before its score is used for any further trim/hold decision (issue #709 already open).
2. **TLT's structural cap breach** still warrants a dedicated framework-development session rather than continued monthly re-flagging.
3. Confirm the TSM/NVDA/BKNG undocumented orders and the vanished TLT short-call order directly in TWS/Client Portal — none contradicts the current session's math, but all four remain unresolved governance gaps.
4. Confirm the SPOT position/order and the unexplained cash jump directly in TWS/Client Portal.
5. Formalize NKE's Turnaround Sub-Gate entry and the RBRK `override-log.md` gap — both long overdue.

*Session complete. No trades executed — this is a proposal for human review. Log any executed trims in `decisions/` and refresh `holdings.md` via `/sync-portfolio` once anything settles.*

---

## Glossary

- **Composite Score:** this framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; drives Phase 03/05 action-table lookups once a Quality Score exists — see [quality-scoring.md](../framework/quality-scoring.md).
- **FX (foreign exchange) rate:** the price of converting one currency into another; this framework only uses live, broker-reported FX rates, never an assumed rate, per Rule 0.
- **GTC (Good-Til-Cancelled):** an order instruction telling the broker to keep a limit order open indefinitely until it fills or is manually cancelled.
- **Human Override:** a position opened or held outside the framework's own rules. Tracked for life in `override-log.md`.
- **Hybrid Upgrade:** one of 7 framework-specific rule additions layered on the base 6-phase strategy (Upgrade 4 = Turnaround Sub-Gate, Upgrade 7 = the 15% position cap).
- **NLV (Net Liquidation Value) / NAV (Net Asset Valuation):** a broker's headline account value — all positions at current market price, plus cash, minus liabilities (IBKR calls this NLV, Freedom24 calls it NAV).
- **Quality Score:** this framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02.
- **Rule 0:** this framework's non-negotiable requirement to pull live prices/data before any calculation, never inferring or estimating financial figures.
- **Rule 9:** this framework's rule requiring an immediate re-score after any >15% unexplained price move or a defined fundamental trigger (earnings, guidance, M&A, management change, macro shift).
- **Stale score:** a Last Review date that predates a holding's most recent earnings release — the score must be refreshed via `/rescore` before it's used for a trim/hold decision (operating-calendar.md).
- **Turnaround Sub-Gate:** the conditional path (Hybrid Upgrade 4) letting a company failing some quality criteria still enter as a small (2–3%) position if it passes 5 specific tests.
- **Valuation Score:** this framework's 0.0–100.0 continuous score (0.0 = cheapest, 100.0 = most expensive).
- **Watchlist (action band):** the framework's recommendation for a valuation score of 50.0–69.9: fairly-to-fully valued, "no new entry." (Distinct from the repo's `watchlist/` directory.)

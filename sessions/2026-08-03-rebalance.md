# 2026-08-03 — Rebalance Session (Monthly Rebalance / Trim Review)

**Task type:** REBALANCE
**Scope:** Portfolio-wide trim/hold/exit review across [holdings.md](../portfolio/holdings.md), applying Phase 05 (Dynamic Trimming) and Phase 06 (Exit Triggers) from [strategy.md](../framework/strategy.md) to current scores, the Upgrade 7 15% single-position cap, and the Upgrade 4 Turnaround Sub-Gate review-due check. **This is Routine 5's first-Monday-of-the-month Monthly Rebalance / Trim Review** ([automation-schedule.md](../framework/automation-schedule.md)) — today (2026-08-03) is the first Monday of August.

**No trades executed. This is a proposal for human review only.**

---

## 0. Rule 0 — live data pull vs. the 2026-08-02 sync, and a data-gap fix

Per Rule 0, live `get_account_positions` / `get_account_balances` were pulled directly from IBKR (account U19421206) rather than relying solely on [holdings.md](../portfolio/holdings.md)'s 2026-08-02 sync. **Every scored equity's share count is unchanged** from that sync — no undocumented trades to report this session — but prices moved again in the ~24 hours since:

- **MSFT climbed further**: $461.81 (2026-08-02 sync) → **$475.65 live** (+3.0% in one trading day, +23.2% over the ~9 trading days this cap-breach has been building — see holdings.md's standing flag). This directly worsens the already-confirmed 15% position-cap breach — see §4.
- IBKR Net Liquidation Value: **$46,521.67** (BASE currency), up from $45,705.49 at the 08-02 sync.
- Freedom Finance leg unchanged (still last screenshot 2026-06-07, per [sync-sop.md](../portfolio/sync-sop.md) — no live API): $15,123.54.
- **New combined total this session: $46,521.67 + $15,123.54 = $61,645.21** (vs. $60,829.03 at the 08-02 sync).

**Data-gap fix worth recording:** the last several rebalance sessions (e.g. [2026-07-06](2026-07-06-rebalance.md) §1) carried a standing note that `yfinance`'s TLS handshake fails through this environment's egress proxy, blocking earnings-date lookups needed for the staleness check below. This session found a working fix: `curl_cffi`'s default browser-impersonation profile (`chrome`) causes a TLS reset through the proxy, but pinning an older profile (`impersonate="chrome110"`, confirmed with `safari15_5` and `edge101` also working) connects cleanly. **This unblocks the earnings-date staleness check for the first time in several cycles** — see §1. Recommend `/healthcheck` (Routine 7) adopt the same pinned-impersonation-profile workaround if its own `yfinance` check has been silently degraded the same way.

---

## 1. Staleness check (operating-calendar.md)

Every scored holding's Last Review date (from [holdings.md](../portfolio/holdings.md)) was checked against its actual most recent earnings release date, pulled live via `yfinance.Ticker.get_earnings_dates()` (see §0 for the connectivity fix). Operating-calendar.md's rule: a re-score is due within 3 business days of each earnings release — a Last Review date that predates the most recent release is stale.

| Ticker | Last Review | Most Recent Earnings | Stale? |
|---|---|---|---|
| ADBE | 29 Jul 2026 | 11 Jun 2026 | No |
| AMZN | 01 Aug 2026 | 30 Jul 2026 | No |
| AVGO | 04 Jul 2026 | 03 Jun 2026 | No |
| **CSGP** | **04 Jul 2026** | **28 Jul 2026** | **Yes — 24 days stale, due ~31 Jul** |
| DUOL | 04 Jul 2026 | 05 May 2026 (next: 05 Aug, not yet reported) | No |
| GOOG | 22 Jul 2026 | 22 Jul 2026 | No (reviewed same day) |
| **META** | **28 Jul 2026** | **29 Jul 2026** | **Yes — review 1 day *before* the release; due today (03 Aug)** |
| MSFT | 30 Jul 2026 | 29 Jul 2026 | No |
| NFLX | 17 Jul 2026 | 16 Jul 2026 | No |
| NKE | 01 Jul 2026 | 30 Jun 2026 | No |
| **NOW** | **05 Jul 2026** | **22 Jul 2026** | **Yes — 12 days stale, due ~27 Jul** |
| NVDA | 05 Jul 2026 | 20 May 2026 (next: 26 Aug, not yet reported) | No |
| NVO | 05 Jul 2026 | 05 May 2026 (next: 05 Aug, not yet reported) | No |
| **SPGI** | **05 Jul 2026** | **28 Jul 2026** | **Yes — 6 days stale, due ~31 Jul** |
| **TRN** | **05 Jul 2026** | **30 Jul 2026** | **Yes — 4 days stale, due ~04 Aug (not yet overdue)** |
| UBER | 14 Jul 2026 | 06 May 2026 (next: 05 Aug, not yet reported) | No |
| V | 29 Jul 2026 | 28 Jul 2026 | No |
| VEEV | 01 Jul 2026 | 03 Jun 2026 | No |
| ZS | 05 Jul 2026 | 26 May 2026 (next: 02 Sep, not yet reported) | No |

**Five holdings are flagged stale and need `/rescore` before their Composite Scores can be relied on for trim/hold decisions: CSGP, META, NOW, SPGI, TRN.** No open `rescore-due` GitHub issue currently covers these (Routine 1's earnings-detection issues would normally catch this — worth checking whether Routine 1 has the same `yfinance` connectivity gap this session's §0 fix addresses). Per the operating brief, their current Composite Scores below are shown for reference but **not treated as a reliable basis** for a trim/hold call this month.

---

## 2. Phase 05 — Dynamic Trimming (Valuation-Driven)

Per [strategy.md](../framework/strategy.md) Phase 02/05, the **Composite Score** (Quality + Valuation, 50/50) is the correct lookup for Phase 05's action bands, not the raw Valuation Score.

| Band | Tickers (Composite Score) |
|---|---|
| 90.0–100.0 (trim to 1–2%) | **None** |
| 80.0–89.9 (trim to 50%) | **None** |
| 70.0–79.9 (trim 25–30%) | **None** |
| 50.0–69.9 (hold, watch only) | AMZN (63.0), CSGP (56.1 — ⚠️ stale) |
| 30.0–49.9 (hold, Cheap) | AVGO (43.1), DUOL (36.4), GOOG (46.4), NFLX (39.8), NKE (34.8, override — quality-gate fail), NOW (41.3 — ⚠️ stale), SPGI (34.6 — ⚠️ stale), UBER (39.2), V (34.5), ZS (41.9, override — quality-gate fail) |
| 0.0–29.9 (Very Cheap — recycling candidates) | ADBE (8.1), META (20.7 — ⚠️ stale), NVDA (21.3), TRN (21.4 — ⚠️ stale), VEEV (29.7) |
| n/a — Composite not adopted | MSFT (29.5, reference only — Quality Score 79.9 fails the 80.0 gate by 0.1) |

**Result: zero Phase 05 trim triggers fire this month.** The highest Composite Score on the book is AMZN at 63.0 — comfortably inside "Fair Value, hold and watch," nowhere near the 70.0 trim threshold. This continues the pattern of the last several months (see [2026-07-06](2026-07-06-rebalance.md) §2) once Quality Scores are folded in.

**Caveat on the five stale names (§1):** none of CSGP/META/NOW/SPGI/TRN's current Composite reads sit anywhere near the 70.0 trim band either (highest is CSGP at 56.1), so a stale score is very unlikely to be concealing a live trim trigger this month — but per the operating brief this is a caveat, not a substitute for actually running `/rescore` on all five.

---

## 3. Phase 06 — Full Exit Triggers

**None fired.** No holding sits in the 90.0–100.0 sustained-2-quarters band (§2). No fundamental-deterioration, growth-thesis-broken, or balance-sheet-crisis signal surfaced from this session's scope (a full Phase 04 qualitative review is outside `/rebalance`'s mechanical checks — this reflects the last documented `/rescore` for each name, not fresh qualitative research this session).

RBRK and STIM continue to carry standing "not scored" exit-review flags from prior sessions (RBRK fails Phase 01 quality gates; STIM is a going-concern override) — carried forward, unaddressed for many consecutive cycles, see §7.

---

## 4. Upgrade 7 — 15% Single-Position Cap Check

Using this session's live combined total of **$61,645.21** (§0): **15% cap = $9,246.78.**

| Ticker | Combined Value (live) | Weight | Breach? | Action |
|---|---|---|---|---|
| **MSFT** | $10,337.93 (IBKR $9,512.93 @ 20 sh live + Freedom24 $825.00 @ 2 sh, last screenshot) | **16.77%** | **Yes — by $1,091.15 (1.77pp)** | **Trim recommended — see below** |
| **TLT** | $18,271.90 (IBKR $8,236.00 @ 100 sh live + Freedom24 $10,035.90 @ 118 sh, last screenshot) | **29.65%** | **Yes — by $9,025.12 (14.65pp)** | **Carried forward, 9th consecutive month** — no fixed-income valuation/sizing methodology exists in this framework (see [override-log.md](../portfolio/override-log.md)); recommend this graduate from a routine monthly re-flag to a dedicated framework-development session, as the last several rebalance sessions have also recommended. |
| All other holdings | ≤9.79% (AMZN, the next-highest) | — | No | — |

### MSFT trim recommendation (governance-driven, not Phase 05 — its Composite Score is reference-only, gate-fail)

This is the **second consecutive month** MSFT has breached the hard cap, and the breach has **worsened** since yesterday's sync (16.54% → 16.77%) purely from continued price appreciation — Upgrade 7 is explicit that this cap applies "never... under any circumstances," independent of score.

- **Minimum trim to clear the cap:** $1,091.15 ÷ $475.6463/share (live) = **2.29 shares → round up to 3 shares** (leaves MSFT at 17 IBKR + 2 Freedom24 = 19 sh, combined value $8,910.99, **weight 14.45%**).
- **Recommended trim (with buffer):** given MSFT has re-breached the cap twice in two months purely from price momentum (+23.2% in ~9 trading days), a bare-minimum trim risks a third breach next week. Trimming **4 shares** from the IBKR leg (20 → 16 sh; Freedom24's 2 sh untouched — no IBKR tool can act on the Freedom24 account) leaves MSFT at 18 total shares, combined value $8,435.34, **weight 13.68%** — a ~1.3pp buffer below the cap.
- Proceeds: 4 sh × $475.6463 ≈ **$1,902.59** (live price at time of this session — will differ at actual execution; per Rule 0, do not treat this as a fill price).

---

## 5. Recycling Plan

Per Phase 05, "proceeds always reinvested into current Score 0.0–29.9 names only" — applying the same principle to the MSFT cap-driven trim proceeds (§4), since Upgrade 7 doesn't specify its own recycling rule and the framework's general philosophy is to always redeploy freed capital into the cheapest currently-held names:

| Ticker | Composite Score | Current Weight (live) | Room to 6–8% Phase 03 target | Notes |
|---|---|---|---|---|
| **ADBE** | 8.1 | 4.18% ($2,575.00 @ 10 sh) | ~$1,167.79–$2,383.79 | Deepest "Very Cheap" unstale score on the book; continues the documented partial-fill build-out from [2026-06-12](2026-06-12-new-position-adbe.md). **Primary recommended destination.** |
| **VEEV** | 29.7 | 1.02% ($627.03 @ 3 sh) | ~$3,022.71–$4,239.29 | Largest proportional headroom to target, but its own score is a marginal/boundary result per its [2026-07-01 rescore](2026-07-01-rescore-veev.md) caveat — flagged there for deliberate human sizing, not mechanical recycling. **Secondary/alternative destination.** |
| NVDA | 21.3 | 6.12% ($3,773.55 @ 19 sh) | ~$616.51–$1,092.77 | Already inside its own 6–8% target band — modest room only. |
| META (⚠️ stale) | 20.7 | 6.49% | n/a | **Not a usable destination this month** — score needs refresh (§1) before any add, and it's already mid-band on weight with limited headroom regardless. |
| TRN (⚠️ stale) | 21.4 | 3.22% | ~$1,676–$2,893 | Meaningful headroom, but score needs refresh (§1) first — provisional destination only. |

**Illustrative split of the ~$1,902.59 MSFT trim proceeds (§4), not a mandated allocation:** ~$1,200 (≈4.7 sh) to ADBE, ~$700 (≈3.3 sh) to VEEV. This is a proposal for the user's own sizing judgment — no order is placed by this session.

---

## 6. Upgrade 4 — Turnaround Sub-Gate Review Check

Searched [override-log.md](../portfolio/override-log.md) and every file under `decisions/` for any position **entered** under the Turnaround Sub-Gate ("Conditional Watch, 2–3% max," mandatory 2-quarter review, the 5 conditions in strategy.md). No hits beyond the rule's own description — no position has ever actually been logged as entered under this gate.

**Result: none found — same conclusion as every prior month. No turnaround-review-due items this month.**

**Carried-forward recommendation, still not actioned:** NKE's [2026-07-01 rescore](2026-07-01-rescore-nke.md) §10 recommends formally converting NKE's standing value-trap override into a documented Upgrade 4 Turnaround Sub-Gate entry + `override-log.md` row. Still not done as of this session.

---

## 7. Other open items carried forward (from [holdings.md](../portfolio/holdings.md)'s 2026-08-02 sync and [override-log.md](../portfolio/override-log.md) — not re-investigated this session, out of `/rebalance`'s scope)

| Ticker/Item | Status |
|---|---|
| **SPOT** | 1-share position and its matching GTC sell order both vanished, undocumented — unconfirmed exit, flagged for the user to confirm directly in TWS/Client Portal. |
| **META (+1 share)** | Share count moved 5→6 undocumented, coincident with a `REPLACED` sell order — mechanism unconfirmed. |
| **AVGO** | Override-log's "Open — under review" status text is stale (score was resolved 2026-07-04) — still not corrected. |
| **RGL** | Ungoverned 60,000-share ASX micro-cap position, fully filled since 2026-07-06, no Phase 01/02 evaluation ever run. |
| **DOCS** | Short put position, no evaluation of that specific instrument on record. |
| **MBGL** | Ungoverned 1-share position, likely corporate-action-sourced, still uninvestigated. |
| **RBRK, STIM** | Still carry no `override-log.md` entry despite standing exit-review flags. |

---

## 8. Summary table — proposed actions

| Ticker/Item | Score | Weight (live) | Proposed action | Driven by |
|---|---|---|---|---|
| **MSFT** | Composite 29.5 (ref only, gate fail) | 16.77% | **Trim 3–4 shares (IBKR leg) to clear the 15% cap** — minimum 3 sh (→14.45%), recommended 4 sh (→13.68%) for buffer against continued momentum | Upgrade 7 — hard 15% cap, 2nd consecutive month breached, breach worsening |
| **TLT** | n/a, non-equity | 29.65% | No action proposed — unresolved structural framework gap, 9th consecutive month; recommend escalating to a dedicated framework-development session | Upgrade 7 — hard cap, no methodology exists |
| **CSGP, META, NOW, SPGI, TRN** | Various (see §1) | 1.18% / 6.49% / 2.25% / 0.68% / 3.22% | **Run `/rescore` before next month's rebalance** — Last Review predates the most recent earnings release for all five | Staleness (operating-calendar.md) |
| All other scored equities | 0.0–63.0 bands | ~30% combined | Hold — no trim, no exit | Phase 05/06 — clean this month |
| **Recycling plan** | — | — | ~$1,902.59 in MSFT trim proceeds proposed for ADBE (primary) / VEEV (secondary) — illustrative split, not mandated | Phase 05 recycling principle, applied to the cap-driven trim |
| NKE | Composite 34.8 (Quality 44.4 fails gate) | 1.37% | Hold existing, do not add; formalize Turnaround Sub-Gate entry (still overdue) | Governance / Upgrade 4 |
| RBRK, STIM | not scored | 0.36% / 1.65% | Carried forward, unaddressed | Fundamental (Phase 06) / governance |
| SPOT, META (+1 sh), RGL, DOCS, MBGL, AVGO, RBRK, STIM | — | — | Carried forward from 08-02 sync — no new findings this session | Governance (§7) |

**Recommended sequencing:**
1. **Resolve the MSFT cap breach** — trim 3–4 shares of the IBKR leg; this is the only fresh, quantified, actionable item this session.
2. **Run `/rescore` on CSGP, META, NOW, SPGI, TRN** before their scores are used for any further trim/hold decision — all five are earnings-stale.
3. If MSFT is trimmed, consider deploying proceeds toward ADBE and/or VEEV per §5 — illustrative only, not mandatory.
4. Confirm the SPOT and META(+1) undocumented position changes directly in TWS/Client Portal (§7).
5. TLT's structural cap breach (9th consecutive month) still warrants a dedicated framework-development session rather than continued monthly re-flagging.
6. Formalize NKE's Turnaround Sub-Gate entry and the RBRK/STIM `override-log.md` gaps — both long overdue.

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
- **Stale score:** a Last Review date that predates a holding's most recent earnings release — the score must be refreshed via `/rescore` before it's used for a trim/hold decision (operating-calendar.md).
- **Turnaround Sub-Gate:** the conditional path (Hybrid Upgrade 4) letting a company failing some quality criteria still enter as a small (2–3%) position if it passes 5 specific tests.
- **Valuation Score:** this framework's 0.0–100.0 continuous score (0.0 = cheapest, 100.0 = most expensive).
- **Watchlist (action band):** the framework's recommendation for a valuation score of 50.0–69.9: fairly-to-fully valued, "no new entry." (Distinct from the repo's `watchlist/` directory.)

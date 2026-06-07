# 2026-06-07 — Rebalance Session

**Scope:** Portfolio-wide trim/hold/exit review across all rows in [holdings.md](../portfolio/holdings.md) (combined total ≈ **$53,893.38**), applying Phase 05 (Dynamic Trimming), Phase 06 (Exit Triggers), and the Upgrade 7 15% position cap from [strategy.md](../framework/strategy.md) — **as just revised earlier today** (see [decisions/2026-06-07-framework-fixes-investor-philosophy-alignment.md](../decisions/2026-06-07-framework-fixes-investor-philosophy-alignment.md)).

**⚠️ Headline finding — read this before the trim list below:** this session surfaced a same-day timing collision. The Rate Environment Gate's Step 1 mechanism changed *this afternoon* (hard "do not open" veto → **+0.5 additive scoring modifier**), but every score in `holdings.md` was produced *this morning* by [sessions/2026-06-07-rescore-full-portfolio.md](2026-06-07-rescore-full-portfolio.md), under the *old* gate form — which never touched the score at all (it only blocked new entries). That means **18 of 19 scoreable names are sitting on a score that may now be running half a point light**, and three of them are close enough to a banding edge that re-applying the modifier correctly would change which names are even on the trim list. Full breakdown in §2 — **my recommendation is to run a Rate Environment Gate refresh / partial rescore before executing anything proposed here.**

---

## 1. Holdings pull

Source: [holdings.md](../portfolio/holdings.md), live-synced 2026-06-07 from IBKR + Freedom24 (see §5 of [sync-sop.md](../portfolio/sync-sop.md) for methodology). **No staleness from an earnings standpoint** — every scored row carries "Last Review: Jun 2026," i.e., today; this morning's full-portfolio rescore baseline is the freshest possible starting point. The only staleness this session found is the rule-change collision in §2, which is a *framework* staleness, not a *data* staleness — `/rescore` per se isn't strictly required (no new earnings), but a **Rate Environment Gate refresh applying the new Step 1 modifier** effectively is, before any trim executes.

| Ticker | Weight % | USD (derived from weight × $53,893.38) | Last Score | Status |
|---|---|---|---|---|
| MSFT | 16.84% | $9,075.65 | 6 | Scored — hold band (post-update) |
| TLT | 30.77% | $16,582.99 | not scored — non-equity, framework gap | Special — see §6 |
| AMZN | 10.49% | $5,653.42 | 8 | Scored — trim band |
| DUOL | 7.60% | $4,095.90 | 4 | Scored — buy band, capacity-constrained |
| CASH (IBKR) | 7.39% | $3,982.75 | — | Liquidity |
| META | 5.47% | $2,947.97 | 5 | Scored — buy band (borderline, see §2) |
| NVDA | 5.30% | $2,856.35 | 6 | Scored — hold band (post-update) |
| XEON | 3.19% | $1,719.20 | not scored — cash-equivalent | Out of scope |
| NOW | 2.47% | $1,331.17 | 6 | Scored — hold band (post-update) |
| NFLX | 1.82% | $980.86 | 7 | Scored — hold band (borderline, see §2) |
| NKE | 1.59% | $856.90 | 4 | Scored — buy band, qualitative override (value-trap flags) |
| CSGP | 1.57% | $846.13 | 8 | Scored — trim band |
| STIM | 0.83% | $447.32 | not scored — going-concern override | Special — see §6 |
| SPOT | 0.92% | $495.82 | 8 | Scored — trim band |
| SPGI | 0.79% | $425.76 | 5 | Scored — buy band (borderline, see §2) |
| GOOG | 0.68% | $366.47 | 8 | Scored — trim band |
| V | 0.60% | $323.36 | 6 | Scored — hold band (post-update) |
| RBRK | 0.40% | $215.57 | not scored — fails quality gates | Special — see §6 |
| NVO | 0.40% | $215.57 | 4 | Scored — buy band, qualitative override (thesis looks broken) |
| UBER | 0.39% | $210.18 | 6 | Scored — hold band (post-update) |
| ZS | 0.24% | $129.34 | 6 (low-confidence) | Scored — hold band (post-update) |
| CASH (Freedom24) | 0.20% | $107.79 | — | Liquidity |

---

## 2. ⚠️ Why the trim list below should be treated as provisional

[sessions/2026-06-07-rescore-full-portfolio.md §3](2026-06-07-rescore-full-portfolio.md) ran the Rate Environment Gate's Step 1 spread test (`Spread = EY − 4.55%` against a +1.5% pass bar) for every scoreable name and found **18 of 19 FAIL** (NVO is the lone pass, at +3.23%). Under the gate's *old* form, a "FAIL" only meant "don't deploy fresh capital here" — it left the recorded score untouched. As of [today's framework-fixes session](../decisions/2026-06-07-framework-fixes-investor-philosophy-alignment.md), a "FAIL" now means **+0.5 to the valuation score**.

Re-applying that already-documented spread-test result as a +0.5 modifier (using `strategy.md`'s existing "round X.5 up" boundary rule) projects as follows. **This is a mechanical projection for flagging purposes only — not a new authoritative score** (a proper refresh should re-run the full weighted calculation, not just bolt a modifier onto a finished number):

| Ticker | Spread result | Recorded score | Score + 0.5 → rounded | Band before → after | Why it matters |
|---|---|---|---|---|---|
| **NFLX** | FAIL (−0.48%) | 7 | 7.5 → **8** | Hold (6–7) → **Trim 25–30% (8)** | Would become a *new* trim candidate not on today's list |
| **META** | FAIL (+0.94%, closest miss) | 5 | 5.5 → **6** | Buy zone (4–5) → **Hold/Watchlist (6)** | Drops out of the buy band entirely — the rescore session's flagged "BUY-band score that fails the gate" tension resolves itself the other way |
| **SPGI** | FAIL (+0.23%) | 5 | 5.5 → **6** | Buy zone (4–5) → **Hold/Watchlist (6)** | The session called SPGI "the cleanest BUY candidate in the book" — that status would not survive the modifier |
| AMZN | FAIL (−1.14%) | 8 | 8.5 → **9** | Trim 25–30% (8) → **Trim to 50% (9)** | Deepens an already-planned trim |
| CSGP | FAIL (−2.17%) | 8 | 8.5 → **9** | Trim 25–30% (8) → **Trim to 50% (9)** | Deepens an already-planned trim |
| GOOG | FAIL (−0.68%) | 8 | 8.5 → **9** | Trim 25–30% (8) → **Trim to 50% (9)** | Deepens an already-planned trim |
| SPOT | FAIL (−1.56%) | 8 | 8.5 → **9** | Trim 25–30% (8) → **Trim to 50% (9)** | Deepens an already-planned trim |
| MSFT | FAIL (−0.11%) | 6 | 6.5 → **7** | Hold (6–7) → Hold (6–7) | No band change |
| DUOL | FAIL (−1.67%) | 4 | 4.5 → **5** | Buy (4–5) → Buy (4–5) | No band change |
| NKE | FAIL (−0.38%) | 4 | 4.5 → **5** | Buy (4–5) → Buy (4–5) | No band change |
| NOW | FAIL (−0.48%) | 6 | 6.5 → **7** | Hold (6–7) → Hold (6–7) | No band change |
| UBER | FAIL (+0.45%) | 6 | 6.5 → **7** | Hold (6–7) → Hold (6–7) | No band change |
| V | FAIL (−0.40%) | 6 | 6.5 → **7** | Hold (6–7) → Hold (6–7) | No band change |
| ZS | FAIL (−1.25%) | 6 (low-conf.) | 6.5 → **7** | Hold (6–7) → Hold (6–7) | No band change (already flagged low-confidence for other reasons) |
| NVDA | FAIL (gate result confirmed in [sessions/2026-06-07-rescore-nvda.md](2026-06-07-rescore-nvda.md), exact spread not restated here) | 6 | 6.5 → **7** | Hold (6–7) → Hold (6–7) | No band change |
| NVO | **PASS** (+3.23%) | 4 | 4 (no modifier) | Buy (4–5) → Buy (4–5) | Unaffected — already flagged separately as a thesis-broken override candidate |

**Net effect if the projection holds:** the trim list would grow from 4 names to 5 (adding NFLX), shrink the buy-zone from 5 names to 3 (losing META and SPGI to the hold band), and escalate four existing trim candidates (AMZN, CSGP, GOOG, SPOT) from a 25–30% trim to a 50% trim. That is too large a swing to treat the §3 list below as final. **Recommended sequencing: run the Rate Environment Gate refresh (already due quarterly per [operating-calendar.md](../framework/operating-calendar.md), and now also triggered by today's mechanism change) before executing any trim from this session.**

---

## 3. Phase 05 / Phase 06 applied — using the scores currently recorded in `holdings.md`

*(Per §2, treat this as the "if we acted today, on today's recorded numbers" view — not the final word.)*

### Trim candidates (Score 8 → trim 25–30%, recycle into Score 1–3 names)

| Ticker | USD value | 25% trim | 30% trim | Reasoning |
|---|---|---|---|---|
| **AMZN** | $5,653.42 | $1,413.36 | $1,696.03 | Score 8 = "Expensive." [Rescore session](2026-06-07-rescore-full-portfolio.md) shows it failing the rate gate (−1.14% spread) with no offsetting fundamental break — a clean valuation-driven trim, not an exit. |
| **CSGP** | $846.13 | $211.53 | $253.84 | Score 8, small position (1.57%) — trim reduces an expensive name without much portfolio impact either way. |
| **GOOG** | $366.47 | $91.62 | $109.94 | Score 8, smallest of the trim group (0.68%) — same logic, minimal portfolio impact. |
| **SPOT** | $495.82 | $123.96 | $148.75 | Score 8, small position (0.92%) — same logic. |
| **Subtotal** | — | **$1,840.47** | **$2,208.56** | Proceeds destination: see §5 (cash, not recycled — no Score 1–3 name exists). |

None of these four show a *fundamental* break in the baseline rescore (no margin compression, no thesis breakdown reported) — these are pure valuation-driven trims under Phase 05, exactly the kind the framework is designed to fire mechanically rather than on a gut call.

### Hold — Fair Value band (Score 6–7): no trim, per today's rule change

Under the *old* Phase 05 rule (trim trigger at Score 6–7), **all seven of these names would have been on the trim list today.** Under the rule [just changed this session](../decisions/2026-06-07-framework-fixes-investor-philosophy-alignment.md) — because trimming the moment a position becomes merely "fairly valued" was a higher-turnover posture than Buffett/Munger/Smith's documented practice — they are now correctly held:

| Ticker | Score | Weight | Reasoning |
|---|---|---|---|
| MSFT | 6 | 16.84% | Fair value, intact thesis (Owner-Earnings-adjusted, per Upgrade 1) — would have been a 25–30% trim candidate yesterday; today it's a hold. *(Separately breaches the position cap — see §4, a compliance issue, not a valuation one.)* |
| NFLX | 7 | 1.82% | Fair value — but flagged in §2 as the name most likely to flip into the trim band once the gate refresh lands; worth a priority re-check. |
| NOW | 6 | 2.47% | Fair value, small position — hold and watch. |
| NVDA | 6 | 5.30% | Fair value — separately confirmed in its [own rescore session](2026-06-07-rescore-nvda.md) as failing the rate gate (no new capital), consistent with a hold-not-add stance. |
| UBER | 6 | 0.39% | Fair value, immaterial weight — hold. |
| V | 6 | 0.60% | Fair value, immaterial weight, clean balance sheet per the rescore notes — hold. |
| ZS | 6 (low-confidence) | 0.24% | Fair value on a low-confidence score (distorted GAAP base post-acquisition) — hold, but flagged for priority re-score once the earnings base normalizes (per the baseline session's note). |

### Buy-zone holds (Score 4–5): no trim — these are watch-for-add candidates, not sell candidates

| Ticker | Score | Weight | Reasoning |
|---|---|---|---|
| META | 5 | 5.47% | Buy-band score, but the baseline session flagged it as failing the rate gate by the narrowest margin in the book (+0.94% vs. +1.5% needed) — under the new modifier (§2) this would likely become a Score 6 hold. No action either way: hold, do not add. |
| SPGI | 5 | 0.79% | Called "the cleanest BUY candidate in the book" — meaningfully underweight, no value-trap flags — but also fails the gate (+0.23%) and would likely become a Score 6 under the refresh (§2). For now: hold, set a limit-order watch rather than deploying fresh capital (per Step 2 of [fair-value-methodology.md](../framework/fair-value-methodology.md)). |
| DUOL | 4 | 7.60% | Clean buy-band score, but **structurally capacity-constrained** — already at 7.60%, within half a point of the 8% legacy reference and well inside the new 15% cap, but adding here concentrates further into a name with a documented quality waiver (FCF negative at entry, logged in [override-log.md](../portfolio/override-log.md)). Hold, do not add. |
| NKE | 4 | 1.59% | Buy-band score **overridden** by qualitative value-trap flags (per the baseline session, §4 there) — hold, do not add, refer to the Turnaround Sub-Gate review path (Upgrade 4). |
| NVO | 4 | 0.40% | Buy-band score, and the *only* name to pass the rate gate (+3.23%) — but the baseline session flags the growth thesis as likely broken (continuing GLP-1 share loss to Lilly, the exact "key market lost" trigger in [fair-value-methodology.md](../framework/fair-value-methodology.md) Step 3). A passing gate plus a cratering thesis is not a buy signal — treat as an EXIT REVIEW candidate, not an add. |

### Phase 06 full-exit triggers: none fired on valuation grounds

No name carries a Score 9–10 (the only purely-valuation-driven exit trigger is "Score 10 sustained 2+ quarters"). **STIM and RBRK are flagged for exit review on fundamental — not valuation — grounds; see §6.**

---

## 4. Position cap check (Upgrade 7 — hard 15% single-position cap)

This is a **compliance constraint, independent of valuation score** — a position can be a "hold" on fundamentals and still require a trim purely because it has grown too large for prudent concentration risk (this is, not coincidentally, exactly what Buffett did with Apple in 2024 — size discipline operating alongside, not instead of, the valuation view).

| Ticker | Weight | USD value | 15% cap (= $8,084.01) | Breach? | Action required |
|---|---|---|---|---|---|
| **MSFT** | 16.84% | $9,075.65 | Exceeds by **$991.64** | **Yes** | Cap-compliance trim of at least $991.64 (to land exactly at 15%); trimming toward **14%** ($7,545.07, a cut of ~$1,530.58) would build in a buffer against passive drift (dividend reinvestment, index-linked flows — the kind of thing the baseline session specifically flagged as worth watching for MSFT). This is **independent of and additive to** the Score-6 "hold" verdict above — MSFT is a hold on valuation and a forced trim on concentration, simultaneously, and both are correct at once. |
| **TLT** | 30.77% | $16,582.99 | Exceeds by **$8,498.99** | **Yes — but see §6** | Not actionable as a routine trim: more than half the position would need to move, and the framework has *no* methodology for sizing or valuing a fixed-income / duration-hedge instrument. This is the documented structural gap — flagged again below, not solved here. |
| All others | ≤ 10.49% | — | Within cap | No | — |

*(AMZN, at 10.49%, was a cap breach under the old 8% figure but clears the current 15% cap comfortably — exactly the outcome [decisions/2026-06-07-framework-change-position-cap.md](../decisions/2026-06-07-framework-change-position-cap.md) anticipated when the cap was raised.)*

---

## 5. Recycling plan

Per Phase 05's explicit rule — **"proceeds always reinvested into current Score 1–3 names only"** — and per the baseline rescore's finding that **no Score 1–3 name exists anywhere in the current book** (the cheapest scores are 4s — DUOL, NKE, NVO — and each carries its own override flag that disqualifies it as a clean destination):

> **All trim proceeds should sit in cash** (joining the existing $4,090.54 combined cash position across both brokers) until a future re-score establishes a genuine Score 1–3 destination. Recycling into a guess would itself be an undocumented-trigger violation of the framework's "act only on documented triggers" rule.

This mirrors the precedent already set in the [NVDA rescore session](2026-06-07-rescore-nvda.md) and reaffirmed in the baseline portfolio rescore — not a new interpretation, just a consistent application of an existing one.

**Projected cash position if the four Score-8 trims (at the midpoint, ~27.5%) plus a 14%-target MSFT compliance trim all execute:**
≈ $4,090.54 (current combined cash) + ~$2,024.50 (trim proceeds, midpoint estimate) + ~$1,530.58 (MSFT compliance trim) ≈ **$7,645.62**, or roughly **14.2% of the portfolio** — a meaningful liquidity buffer, appropriate given that the portfolio currently has no clean Score 1–3 reinvestment target.

---

## 6. Special cases — not standard trim/hold/exit logic

| Ticker | Status | Recommended handling |
|---|---|---|
| **TLT** (30.77%) | Non-equity; "not scored — framework gap" | The single largest open issue in the book. Breaches the position cap by more than half its own size, and the framework has no fixed-income valuation or sizing methodology to act on that breach with. This needs its own dedicated framework-development session (not a routine rebalance line item) — see the baseline rescore's §7.1 for the full writeup of the gap. Recommend opening a `decisions/` entry scoping that work, separate from this session. |
| **STIM** (0.83%) | "Not scored — going-concern override" | The baseline rescore explicitly flagged this as **not waiting for a scheduled review** — a going-concern flag is itself an immediate EXIT REVIEW trigger (Phase 06: "balance sheet crisis"). Recommend running that EXIT REVIEW before the next earnings cycle, independent of this rebalance. |
| **RBRK** (0.40%) | "Not scored — fails quality gates" | Fails the Phase 01 Quality Gate outright — the gate that's supposed to prevent a name like this from being considered at all. Either this is a documented, reviewed exception that belongs in [override-log.md](../portfolio/override-log.md) (it currently isn't logged there), or the gate wasn't applied at entry. Either way: small position (0.40%, $215.57), low urgency on sizing, but worth a clean documented review so it doesn't sit unexamined. |
| **XEON** (3.19%) | "Not scored — cash-equivalent, out of scope" | EUR-denominated cash-equivalent; no valuation logic applies. No action. |
| **CASH** (IBKR + Freedom24, combined 7.59%) | Liquidity | No action — this is exactly the kind of dry powder Phase 05's recycling rule (§5) is about to need more of. |

---

## 7. Recommended sequencing

1. **Run a Rate Environment Gate refresh first.** It's already due quarterly (July 2026) per [operating-calendar.md](../framework/operating-calendar.md), and today's mechanism change (hard veto → +0.5 modifier) gives it independent urgency — re-running it properly (full weighted recalculation, not a bolt-on) will settle whether NFLX, META, and SPGI actually cross the band edges projected in §2, and whether AMZN/CSGP/GOOG/SPOT escalate from a 25–30% trim to a 50% trim.
2. **Then execute (or re-propose) the trim list** from §3, informed by whatever the refresh produces — proceeds to cash per §5.
3. **Separately and in parallel:** open the STIM exit review (urgent — going-concern flag), the RBRK override-log review (low urgency, small size), and the TLT framework-gap discussion (large — needs its own session, not a rebalance line item).
4. **MSFT's cap-compliance trim (§4) can proceed independent of all of the above** — it's driven by concentration, not valuation, so it isn't affected by the gate-refresh question.

**Nothing in this session has been executed.** Per the operating brief, trims/exits are proposed here for review; log any that are actually carried out in `decisions/`, and update [holdings.md](../portfolio/holdings.md) via the next [`/sync-portfolio`](../portfolio/sync-sop.md) once they settle.

---

## 8. Summary table — proposed actions

| Ticker | Score | Weight | Proposed action | Driven by |
|---|---|---|---|---|
| AMZN | 8 | 10.49% | Trim 25–30% (~$1,413–$1,696) → cash | Valuation (Phase 05) — *pending §2 refresh, may deepen to 50%* |
| CSGP | 8 | 1.57% | Trim 25–30% (~$212–$254) → cash | Valuation (Phase 05) — *pending §2 refresh, may deepen to 50%* |
| GOOG | 8 | 0.68% | Trim 25–30% (~$92–$110) → cash | Valuation (Phase 05) — *pending §2 refresh, may deepen to 50%* |
| SPOT | 8 | 0.92% | Trim 25–30% (~$124–$149) → cash | Valuation (Phase 05) — *pending §2 refresh, may deepen to 50%* |
| MSFT | 6 | 16.84% | Hold on valuation; **trim ~$992–$1,531 → cash for cap compliance** | Concentration (Upgrade 7) — independent of score |
| TLT | n/a | 30.77% | No action this session — open a dedicated framework-gap discussion | Structural gap (no methodology) |
| NFLX | 7 | 1.82% | Hold — but flagged as the top candidate to flip into the trim band on refresh | Pending §2 refresh |
| META, SPGI | 5 | 6.26% combined | Hold, do not add (limit-order watch only); flagged as likely to drop out of the buy band on refresh | Pending §2 refresh |
| NOW, NVDA, UBER, V, ZS | 6 | 8.40% combined | Hold — fair value, no trim under the new rule | Valuation (Phase 05) |
| DUOL, NKE, NVO | 4 | 9.59% combined | Hold, do not add — each carries its own override flag | Qualitative overrides |
| STIM | n/a | 0.83% | Open an EXIT REVIEW — going-concern trigger | Fundamental (Phase 06) |
| RBRK | n/a | 0.40% | Open an override-log review | Quality-gate compliance |
| XEON, CASH | n/a | 10.78% combined | No action | Liquidity / out of scope |

*Session complete. No trades executed — this is a proposal for review per the operating brief. Recommended next step: Rate Environment Gate refresh (§7.1), then re-confirm or revise this trim list.*

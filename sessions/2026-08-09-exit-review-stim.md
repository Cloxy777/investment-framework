# EXIT REVIEW — STIM (Neuronetics, Inc.)

**Task type:** EXIT REVIEW (Phase 06), triggered by an unaddressed Rule 9 price-move trigger
**Trigger:** GitHub issue [#337](https://github.com/cloxy777/investment-framework/issues/337) — "RESCORE (Rule 9): STIM moved 24.38% on 2026-07-20 - no known catalyst," opened 2026-07-20, **left unaddressed for 20 calendar days**.
**Date:** 2026-08-09
**Current position:** 500 shares STIM (equity) + short 5 contracts `STIM Aug21'26 $2.50 CALL` (covered call, expires 2026-08-21) — 1.63% of the combined portfolio (equity leg only; the short call is excluded from the weight, per standing convention).

**Why this is an EXIT REVIEW, not a standard RESCORE:** STIM has never received a Phase 01/02 numeric score. Per [portfolio/override-log.md](../portfolio/override-log.md)'s "Historical Override Audit," STIM is a documented **quality waiver override** (micro-cap, no FCF) with an explicit standing rule: **"Exit at next review unless thesis documented."** The [2026-06-07 portfolio-wide rescore](2026-06-07-rescore-full-portfolio.md) went further, finding STIM in active going-concern crisis and recommending **escalation to a dedicated EXIT REVIEW** — a session that, as flagged in the 2026-06-11 backfill note, was never actually run. This session is that overdue EXIT REVIEW, triggered into being by the 2026-07-20 Rule 9 price move.

> *Jargon decoded on first use — see closing Glossary section.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$2.41** | IBKR `get_price_snapshot` (contract_id 324062325), last trade, bid/ask not both populated at fetch time (thin micro-cap liquidity — see §2). |
| Prior close | $2.25 | IBKR `prior_close`. |
| 52-week range | $0.80 – $4.29 | IBKR `misc_statistics`. |
| YTD change | +74.64% | IBKR `year_to_date_change`. |
| Price at last review (2026-06-07) | $1.29 | [2026-06-07 session](2026-06-07-rescore-full-portfolio.md). |
| **Change since last review** | **+86.8%** | Computed — nearly doubled in 9 weeks, entirely on sentiment/analyst catalysts (§3), not a resolved going-concern picture (§4). |
| Short call (`STIM Aug21'26 $2.50 CALL`) live price | **$0.25** (ask) / $0.20 (bid) | IBKR `get_price_snapshot` (contract_id 840079341). Cost to buy back and close all 5 contracts at the ask: 5 × 100 × $0.25 = **$125.00**. |

---

## 2. Independent Investigation of the 2026-07-20 Rule 9 Trigger

The triggering GitHub issue was opened as "no known catalyst" — checked independently rather than assumed either way.

**IBKR daily price history** confirms the move is real, not a data artifact: close $1.62 (07-17) → open $1.74 / close $2.02 (07-20), **+24.7%**, on volume of 11,040,453 shares — roughly **11–17× STIM's typical daily volume** in the surrounding weeks (typically 0.6M–2M shares/day). This is a genuine, high-conviction market move, not noise.

**What actually happened, per independent web research (not the Telegram/issue text):**
1. **CFO transition announced 2026-07-20:** Nir Naor appointed CFO; prior CLO Andrew Macan departed the same announcement. This is the **third C-suite change** on top of the "full C-suite turnover" already flagged in the 2026-06-07 session — a continuing, not resolving, governance-instability signal.
2. **BTIG initiated coverage 2026-07-20 with a Buy rating and a $5.00 price target** — more than double the pre-move price ($1.62). Sell-side initiation-driven pops are common in illiquid micro-caps and are a sentiment/analyst catalyst, not a fundamental one.

**Conclusion:** the move is explained (an analyst upgrade + leadership announcement), not an unexplained Rule 9 event in the "mystery move" sense — but neither event **resolves or even addresses** the going-concern/liquidity picture that drove the original EXIT REVIEW recommendation. A bullish price target from one sell-side shop does not substitute for verified balance-sheet improvement.

Sources: [Why Is Neuronetics Stock Soaring Monday?](https://www.sahmcapital.com/news/content/why-is-neuronetics-stock-soaring-monday-2026-07-20), [StockTitan — STIM news](https://www.stocktitan.net/news/STIM/)

---

## 3. Going-Concern / Balance-Sheet Status — Re-Checked Against the Most Recent Filing

**Critical timing flag: Neuronetics reports Q2 2026 earnings before market open on Tuesday 2026-08-11 — two calendar days after this session.** The most recent filing on record as of today is still the **Q1 2026 10-Q** (period ended 2026-03-31, filed ~May 2026) — the *same* filing the 2026-06-07 session already reviewed. There is no fresher balance-sheet data available to re-check yet; this session cannot claim an update it doesn't have.

**Per the Q1 2026 10-Q (SEC EDGAR, [stim-20260331x10q.htm](https://www.sec.gov/Archives/edgar/data/1227636/000110465926055322/stim-20260331x10q.htm)):**

| Item | Value | Change vs. 06-07 session's understanding |
|---|---|---|
| Cash & cash equivalents (2026-03-31) | $13.2M | Same figure as before — no new data. |
| Outstanding on Perceptive Facility | $65.0M | Same. |
| Q1 2026 revenue | $34.5M (up from $32.0M YoY) | Modest improvement. |
| Q1 2026 net loss | $10.8M (narrowed from $12.7M YoY) | Loss narrowing, still substantial — implied net margin ≈ **−31.3%** this quarter, roughly consistent with (slightly worse than) the −26% figure cited 06-07. |
| Operating cash outflow | $9.4M (improved from prior) | Still burning cash. |
| **Management's own disclosed going-concern basis** | Projects breaching the **TTM revenue covenant for the period ending 2027-03-31** | **Unchanged, still formally disclosed.** This is the company's own management assessment under ASC 205-40, not an outside allegation. |

**Mitigating context found this session (not previously on record):** Neuronetics has amended its Perceptive credit agreement **five times**, most recently **Amendment No. 5 (2026-03-12)** — a $5.0M principal paydown paired with adjusted covenants — and Amendment No. 3 (2025-08-01) lowered the minimum-liquidity covenant to $2.0M through 2026-09-30. This is a real, relevant fact: **the lender has a demonstrated, repeated pattern of amending terms rather than forcing default**, which meaningfully changes the probability distribution of outcomes versus a company with no such track record. It does not, however, retroactively resolve the formally disclosed going-concern doubt — that disclosure stands as of the only filing available.

**No fresher information exists to update this picture before Q2 2026 earnings land in 2 days.**

Source: [Neuronetics amends Perceptive credit line, gains $10M cash, adds warrants](https://www.stocktitan.net/sec-filings/STIM/8-k-neuronetics-inc-reports-material-event-528d8bb95224.html), [Amendment history — Sahm Capital](https://www.sahmcapital.com/news/content/neuronetics-amends-credit-agreement-with-perceptive-credit-holdings-2026-01-22)

---

## 4. Phase 06 Exit Trigger Analysis

Per [framework/strategy.md](../framework/strategy.md) Phase 06 and [framework/fair-value-methodology.md](../framework/fair-value-methodology.md) Step 3's "Fundamental Sell Triggers (override price target)":

| Trigger | Applies to STIM? |
|---|---|
| Balance sheet crisis — leverage spikes, dilutive capital raise | **✅ YES** — going-concern doubt formally disclosed, driven by projected covenant breach on $65.0M of secured debt against $13.2M cash. This is the exact enumerated trigger. |
| Thesis broken — management change | **✅ YES, compounding** — a third C-suite change (CFO, 2026-07-20) since the going-concern flag was first raised, continuing rather than stabilizing the leadership picture. |
| ROIC below cost of capital | **N/A — not computable.** STIM has never cleared the Phase 01 quality gate (no numeric Quality Score exists; net losses make ROIC not meaningful as a standard input). |
| Extreme overvaluation (Score 90.0+ sustained 2 quarters) | **N/A** — no valuation score has ever been computed (Phase 02 was never reached, same treatment as RBRK/MBGL). |

**Two of the framework's own enumerated Full Exit triggers are independently satisfied.** Per Phase 06, either alone is a valid exit reason; per fair-value-methodology.md, a Fundamental Sell Trigger **overrides any price target** — meaning the recent bullish price action and the $5.00 BTIG target are explicitly not a reason to wait, under this framework's own rules.

### Weighing the counter-case (documenting a thesis), per the override-log's own "unless thesis documented" clause

**The case for continuing to hold:**
- Revenue is growing (+7.8% YoY) and losses are narrowing — not a company in immediate collapse.
- The lender (Perceptive) has amended terms five times rather than forcing default — a real, repeated pattern suggesting continued cooperation is more likely than a forced liquidation.
- Q2 2026 earnings, two days away, could plausibly show the covenant risk easing (if TTM revenue trends improve further) or a fresh capital/covenant event.
- A $5.00 analyst target (vs. $2.41 live) implies over 100% upside if BTIG's thesis plays out.

**The case for exiting now:**
- The going-concern doubt is **management's own disclosure**, not a rumor — it has stood, unresolved, since before the 2026-06-07 session and remains the most current information available.
- **No thesis has ever actually been written down** for STIM anywhere in this repo in the ~2 months since the override-log's rule took effect — the "unless documented" condition has not been met, and continuing to hold without documenting one **is** the failure mode the override-log exists to prevent ("overrides are untracked, unreviewed, and therefore never corrected").
- The +86.8% run since 06-07 is analyst-sentiment-driven (§2), not evidence of resolved fundamentals — this is precisely the pattern where "the price went up so it must be fine" becomes a post-hoc rationalization for an override that was never actually re-underwritten.
- Waiting specifically *because* Q2 earnings are 2 days away would repeat the same deferral pattern that already let this run 20 days late on a Rule 9 trigger, and nearly 2 months late on the original EXIT REVIEW recommendation — the framework's rule has no "wait for the next catalyst" clause, only "exit or document."
- Position size is trivial (~$990, 1.63% only because the rest of the book is concentrated in TLT) — there is no diversification or tax-loss reason weighing toward holding through the earnings print.

**Conclusion: EXIT.** The going-concern/balance-sheet-crisis trigger and the compounding management-change trigger are both independently satisfied per the framework's own written rules, no documented thesis exists to invoke the override-log's exception, and there is no principled reason (only the temptation of a 2-day-away earnings print) to defer a decision that was already overdue by 20 days on this specific trigger and by nearly 2 months on the standing EXIT REVIEW recommendation.

---

## 5. Order Setup — Exit Mechanics (recommendation only; no order placed by this session)

The position has two legs that must be closed together, or the exit is incomplete:

| Leg | Action | Basis |
|---|---|---|
| 500 shares STIM (long) | **SELL** at live price ($2.41) or better | Full exit of the equity leg. |
| 5 contracts `STIM Aug21'26 $2.50 CALL` (short) | **BUY TO CLOSE** at ask ($0.25) or better — total cost **≈$125.00** | These 5 contracts cover exactly 500 shares (1 contract = 100 shares). Selling the stock **without** closing this leg would convert a fully-covered short-call position into a **naked short call** — an uncovered, undefined-risk position this framework has never evaluated or authorized. The two legs must be closed together for the exit to actually reduce risk rather than change its shape. |

**Net cash impact of a full exit today:** ≈ (500 × $2.41) − $125.00 buy-back ≈ **$1,080** (before commissions), against a cost basis the framework doesn't have on record (not tracked in this session — see Data Gaps).

**Alternative considered and rejected:** letting the short calls simply expire/get assigned at $2.50 on 2026-08-21 instead of buying them back now. Rejected because (a) it leaves the position open through the 2026-08-11 earnings print — the opposite of an exit decision — and (b) assignment is not guaranteed (the stock could sit below $2.50 at expiry, leaving both legs still open past the point this review concluded they should be closed).

**This is a recommendation only.** No order-placement tool exists in this repo (per every prior session's standing scope note) — executing this exit is the human investor's action to take.

---

## 6. Data Gaps / Flags

1. **No cost basis on record for the 500 STIM shares** anywhere in this repo's `sessions/`, `decisions/`, or `override-log.md` — realized P&L on the recommended exit cannot be computed here. Flagged for the human to pull from broker records at execution time.
2. **Q2 2026 earnings land 2026-08-11, two days after this session** — the going-concern determination in §3 is necessarily based on the Q1 2026 10-Q (the only filing available), not fresher data. If Q2 results materially change the covenant/liquidity picture, this conclusion should be revisited promptly (see §7) — but per §4, that is not a reason to defer today's decision.
3. **No independent verification of the BTIG $5.00 price target's underlying thesis** was performed (would require the actual BTIG research note, not publicly available) — treated as a named, dated fact (an analyst initiated coverage with that rating/target) rather than as evidence about STIM's actual fundamentals.
4. Bid was unpopulated in the equity snapshot at fetch time (thin micro-cap liquidity) — last-trade price used instead, consistent with this framework's Rule 0 practice for thinly-traded names.

No data was invented anywhere above.

---

## 7. Next Review Trigger

- **Immediate:** if the recommended exit (§5) is executed, no further review needed for this position.
- **If NOT executed** (i.e., the human chooses to continue holding): Q2 2026 earnings (2026-08-11, 2 days out) become an **immediate, mandatory Rule 9 trigger** for a follow-up review — and per §4, continuing to hold past that print without executing this exit constitutes an undocumented override that should be logged with an explicit, written thesis in `override-log.md`, not left as an implicit default.
- **Standing triggers:** any further C-suite change, any additional Perceptive Facility amendment or covenant waiver, or confirmation/removal of the going-concern disclosure in the Q2 2026 10-Q.

---

## 8. Housekeeping

- [holdings.md](../portfolio/holdings.md) STIM row updated: Last Review 09 Aug 2026, status text updated to reflect this session's EXIT recommendation (still "not scored" — the going-concern hard disqualifier means no numeric Quality/Valuation score is computed, consistent with the RBRK/MBGL precedent).
- [override-log.md](../portfolio/override-log.md) STIM row (Historical Override Audit table) updated: Current Status and Action columns updated to reflect this session's EXIT conclusion, replacing the standing "Monitoring" placeholder.
- New dated watchlist entry created: [watchlist/in-portfolio/STIM/STIM-2026-08-09.md](../watchlist/in-portfolio/STIM/STIM-2026-08-09.md) (status/action changed from the 2026-06-07 entry — a new dated file per convention, not an append).
- No STIM row existed in [watchlist/STALE.md](../watchlist/STALE.md) — confirmed nothing to clear.
- Two new glossary.md terms added: **Covenant (credit facility)**, **Perceptive Facility**.

---

## Glossary

| Term | Meaning |
|---|---|
| **ASC 205-40** | The U.S. GAAP accounting standard requiring management to formally evaluate and disclose "substantial doubt about an entity's ability to continue as a going concern" when relevant conditions exist — the basis for Neuronetics' own going-concern disclosure cited in §3. |
| **Balance sheet crisis** | One of this framework's six enumerated Phase 06 Full Exit triggers — leverage spikes or a dilutive capital raise, overriding any price target per fair-value-methodology.md. |
| **Buy to close** | An options order that closes an existing **short** option position by buying back the same contract, as opposed to opening a new long position. |
| **Covenant (credit facility)** | A condition a borrower must maintain under a loan agreement (e.g. a minimum revenue level, a maximum leverage ratio, a minimum cash balance) — breaching one can let the lender demand immediate repayment or renegotiate terms. STIM's Perceptive Facility carries a trailing-twelve-month revenue covenant it is currently projected to breach. *(New term.)* |
| **Covered call** | An options strategy where a trader who owns the underlying shares sells (writes) call options against them — caps upside above the strike in exchange for premium income, and (unlike a naked call) carries defined, hedged risk because the shares themselves can be delivered if assigned. |
| **Full Exit trigger (Phase 06)** | One of four framework-enumerated valid reasons to fully exit a position regardless of price: fundamental deterioration, growth thesis broken, extreme sustained overvaluation, or balance sheet crisis. |
| **Going-concern doubt** | A formal disclosure (see **ASC 205-40**) that a company's own management believes there is substantial doubt about its ability to continue operating without additional financing, asset sales, or covenant relief — distinct from an outside short-seller's going-concern *allegation* (see the existing glossary entry), since this is the company's own assessment. |
| **Human Override** | A position opened or held outside the framework's own rules — tracked for life in `override-log.md`. STIM is a documented quality-waiver override with a standing "exit at next review unless thesis documented" rule. |
| **Naked short call** | A short call option position **not** backed by ownership of the underlying shares — carries theoretically unlimited risk if the stock rises, unlike a covered call. Selling STIM's shares without closing the short calls would create this exposure. |
| **Perceptive Facility** | Neuronetics' senior secured credit facility with Perceptive Advisors/Perceptive Credit Holdings — $65.0M outstanding as of 2026-03-31, amended five times to date, and the source of the covenant STIM's going-concern disclosure is based on. *(New term.)* |
| **Phase 06** | The final stage of this framework's six-phase process — the Full Exit decision, evaluated independently of (and able to override) any standing price target. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule, including a >15% stock-price move with no identified cause — the trigger that reopened this review. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results — the basis for the revenue covenant STIM is projected to breach for the period ending 2027-03-31. |

# New Position Evaluation (Rule 9 Re-run) — TRN (Trainline plc, LSE:TRN)

**Task type:** NEW POSITION (Rule 9 management-change re-run of the 2026-06-22 evaluation)
**Date:** 2026-06-24
**10Y US Treasury Yield:** 4.493% (^TNX, yfinance live quote, 2026-06-24; cross-checked against WebSearch/tradingeconomics ~4.49–4.50% same day)
**Rate Regime Modifier in effect:** +5 (3.5–5% bracket)

---

## 0. Trigger and why this is a re-run, not a fresh evaluation

**Trigger:** Telegram post, `t.me/bolshegold` #9617 (~07:10 UTC 2026-06-24). The post reports Trainline plc appointing **Ian Brown** (former CEO of Flutter UK & Ireland; previously CEO of Booking.com's Trips Business Unit; also previously CEO of ANS Group) as the company's next Chief Executive Officer, joining 7 September 2026 to begin an orderly handover and assuming the CEO role/Board seat with effect from **28 September 2026**, succeeding **Jody Ford** (who had separately announced in an earlier RNS his intention to step down after 6+ years leading the company).

**Per Rule 0 / CLAUDE.md, the Telegram post text is used only as a trigger — no number from it is used anywhere in this scoring.** The CEO-change fact itself was independently corroborated via WebSearch against:
- [Trainline Names Ian Brown As Next Chief Executive Officer](https://www.directorstalkinterviews.com/trainline-names-ian-brown-as-next-chief-executive-officer/4121254603) (Directors Talk)
- [Trainline Appoints Ian Brown As CEO](https://www.rttnews.com/3662247/trainline-appoints-ian-brown-as-ceo.aspx) (RTTNews)
- [Directorate change | Company Announcement | Investegate](https://www.investegate.co.uk/announcement/rns/trainline--trn/directorate-change/9633069) — **Trainline's own RNS regulatory disclosure**, the primary-source confirmation
- [Trainline appoints Flutter's Ian Brown as CEO from September](https://www.lse.co.uk/news/trainline-appoints-flutters-ian-brown-as-ceo-from-september-e78qakw9464aeya.html) (lse.co.uk)
- [Trainline appoints Flutter's Ian Brown as CEO from September](https://global.morningstar.com/en-gb/news/alliance-news/1782288515077054000/trainline-appoints-flutters-ian-brown-as-ceo-from-september) (Morningstar)
- [Trainline names former Flutter UK and Ireland boss for top job](https://uk.finance.yahoo.com/news/trainline-names-former-flutter-uk-082423129.html) (Yahoo Finance UK)

All confirm the same facts independently. **This is real, corroborated news**, not a Telegram-only claim.

**Why a re-run, and why a new dated file (not an append):** TRN already has a watchlist entry at [watchlist/not-in-portfolio/TRN/TRN-2026-06-22.md](../watchlist/not-in-portfolio/TRN/TRN-2026-06-22.md) — BUY, full position 6–8%, score 10.0, from a prior Telegram trigger on 2026-06-22 (`t.me/bolshegold` #9608, re: a GBR-delay claim). That entry's own "Next review trigger" field names **"management change"** explicitly. A new CEO appointment is unambiguously a management-change Rule 9 event per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 9 ("Mandatory re-valuation upon: ... Management change ..."). Per [watchlist/README.md](../watchlist/README.md#what-goes-in-an-entry)'s "significant change" rule: *"A Rule 9 fundamental-event trigger fires ... even if the score/action ends up unchanged, the reasoning has changed and is worth a fresh pointer."* This session therefore produces a **new dated file**, `TRN-2026-06-24.md`, leaving `TRN-2026-06-22.md` untouched as history — same convention as the existing META series (META-2026-06-07/12/20/23.md).

**TRN is confirmed not held** — absent from [portfolio/holdings.md](../portfolio/holdings.md); the 2026-06-22 BUY recommendation was never executed (trade execution is human-only per framework hard constraints).

---

## 1. Live price (Rule 0 — fetched first, before any valuation work)

- **IBKR `get_price_snapshot`(contract_id=371871705, Trainline plc, LSE:TRN):** last **204.6186 GBX** (pence), bid 204.00 / ask 204.60, change **−8.38 (−3.93%)** intraday, 52-week range 178.00–304.00 GBX (13-week high 255.60 / low 198.70).
- **yfinance `TRN.L` cross-check:** currentPrice/regularMarketPrice **204.72 GBp**, previousClose 213.00 GBp — consistent with the IBKR snapshot within normal bid/ask noise (both reflect the same sharp intraday move).
- **Price of record for this session: 204.6186 GBX = 2.046186 GBP** (IBKR, used throughout for consistency with the 2026-06-22 session's convention of using the IBKR snapshot as the price of record).
- **FX rate:** `GBPUSD=X` (yfinance), most recent close 2026-06-24 = **1.318774** USD/GBP. → 204.6186 GBX = 2.046186 GBP = **$2.6985 USD**.
- **Same ticker resolution as before:** Trainline plc, LSE:TRN, IBKR contract_id 371871705, yfinance `TRN.L` — confirmed correct entity (4 unrelated companies share the "TRN" symbol; see [TRN-2026-06-22.md](../watchlist/not-in-portfolio/TRN/TRN-2026-06-22.md) §0 for the full disambiguation, unchanged and re-confirmed here).

**Note on the price move itself:** Press coverage independently reports Trainline shares fell ~5.2% to ~202.00 GBX shortly after the CEO announcement broke this morning — directionally and magnitude-consistent with the IBKR snapshot's −3.93% intraday move captured at the time of this session. This is **the market's live reaction to the CEO-change news itself**, not an unexplained move requiring separate Rule 9 investigation — it is fully explained by the same event already triggering this session. Per Rule 9, "NOT valid [exit/action trigger]: price dropped on intact thesis" — the price move is not itself an independent action signal; it is informative context only, folded into the qualitative judgment in §7 below. Panmure Liberum analyst Sean Kealy was quoted reacting constructively to the appointment ("looks like a good appointment given his experience at Booking.com").

All figures below are stated in GBP/GBX unless marked USD.

---

## 2. Data gaps flagged

- **5-year historical PE range:** re-checked fresh — `t.get_earnings_dates(limit=40)` on `TRN.L` still returns no usable historical Reported-EPS rows (one forward-dated row only, NaN values). **Still no 5yr PE history reconstructable.** Same documented no-history fallback applies: `FwdPE_Score = 50.0`, flagged neutral. No change from 2026-06-22.
- **PEG/Fast-Grower eligibility:** still ruled **not applicable** — same basis as before (see §5). FY26 is one fiscal year old; the FY23 anomalous 4.0% effective tax rate and the "only the most recent fiscal year clears Phase 01's >15% ROIC/net-margin bar" pattern are unchanged two days later (no new earnings release occurred in this window — FYE is end-February, next report is the FY2027 interim/H1 release per the existing "Next review trigger").
- **Peer comparables:** same Rule 5 caveat as before — BKNG/EXPE/MMYT/TRIP remain 20–145x Trainline's market cap; still discounted 20% per the same methodology.

No new data gaps from the CEO-change event itself — succession announcements do not require new financial data inputs; they are evaluated qualitatively (§7).

---

## 3. Phase 01 — Quality Gate (re-verified with fresh price; fundamentals unchanged)

FY2026 (FYE 28-Feb-2026) annual financials confirmed **identical** to the 2026-06-22 session via fresh `yfinance` pull — no new earnings release occurred between the two sessions, so only price-derived metrics (FCF yield, EV/EBIT, Forward PE) move.

| Criterion | Threshold | TRN (FY2026) | Basis | Result |
|---|---|---|---|---|
| Net margin | >15% (>12% pre-screen) | **17.63%** | NI 79.813M / Rev 452.684M | ✅ |
| ROIC | >15% | **20.51%** (FY26 only; FY23–25 were 7.24%/8.81%/14.80%, unchanged) | NOPAT (EBIT×(1−30% tax)) / Invested Capital 431.498M | ✅ (current yr) |
| Revenue CAGR 3yr | >10% (>8% pre-screen) | **11.43%** | FY23 327.147M → FY26 452.684M | ✅ |
| Gross margin | >40% or expanding | **82.59%**, expanding (unchanged trend 77.10%→76.95%→79.69%→82.59%) | Gross Profit / Revenue | ✅ |
| FCF positive, 3 consecutive years | required | **4/4 years positive**: 4.387M / 81.846M / 95.886M / 79.547M | yfinance cashflow, FY23–26 | ✅ |
| Net Debt/EBITDA | <2.5x | **1.001x** (FY26); FY23–25 unchanged | Net Debt 167.426M / EBITDA 167.243M | ✅ |
| FCF/NI conversion (2yr) | >70% | **99.67%** (FY26); FY25 164.33% | unchanged | ✅ |
| Share issuance pattern | non-dilutive | **Net buybacks**, unchanged — diluted avg shares 460.83M→417.26M (FY25→FY26) | yfinance | ✅ |

**Result: 8/8 PASS — identical to 2026-06-22.** Same caveat carried forward: ROIC clears >15% only in the most recent fiscal year (FY26); this remains the basis for the PEG ineligibility ruling below, not a Phase 01 failure.

**Phase 01 PASSES → proceed to Phase 02.**

---

## 4. Rate Environment Gate

- **Step 1 — Earnings Yield Spread Test:** Forward PE (fresh, computed from live price ÷ forward EPS 0.26552 GBP) = 204.6186/100 ÷ 0.26552 = **7.706x** → EY = 1/7.706 = **12.976%**. Spread = 12.976% − 4.493% = **+8.483pp** ≥ +1.5% → **no flag** (Step 1 = +0).
- **Step 2 — Rate Regime Modifier:** 10Y = 4.493%, in the 3.5–5% bracket → **+5**.
- **Combined Rate Gate modifier: +5.** Unchanged from 2026-06-22 (rate bracket hasn't shifted).

---

## 5. Phase 02 — Valuation Score

### PEG (Upgrade 3) eligibility — re-affirmed, unchanged

No new earnings release occurred in this 2-day window, so the same ruling stands: **PEG is NOT applicable.** FY23's anomalous 4.0% effective tax rate still distorts the multi-year earnings base used for EPS-growth measurement, and net margin/ROIC still only cross Phase 01's >15% threshold in the single most recent fiscal year (FY26) — the disqualifying "recently-profitable, unreliable base" pattern named in the 2026-06-20 PEG clarification. **PEG's 15% weight remains redistributed to EV/EBIT** (EV/EBIT → 40%; FCF stays 40%; FwdPE stays 20%).

### Sub-scores (recomputed with fresh price/shares)

**FCF Yield (40% weight).**
Shares outstanding (yfinance, fresh) = 351,503,062. Market Cap = 351,503,062 × 2.046186 GBP = **719,240,644 GBP**.
FCF Yield = 79,547,000 / 719,240,644 = **11.060%** (up from 10.417% on 2026-06-22 — cheaper, because price fell while FCF is unchanged).
FCF_Score = clamp(100×(1 − 11.060/10), 0, 100) = **0.00** (already clamped at the floor; no change in output despite the input moving cheaper).

**EV/EBIT (40% weight, redistributed from PEG).**
Same transparent-build discipline as before (yfinance's `enterpriseValue` field of 1,005,699,776 still does not reconcile cleanly with a manually built EV — consistent with the 2026-06-22 finding; built from live components instead):
EV = (351,503,062 shares × 2.046186 GBP) + Total Debt 261,946,000 − Cash 59,703,000 = **921,483,644 GBP**.
EV/EBIT = 921,483,644 / 126,429,000 = **7.289x** (down from 7.640x — cheaper).
EV/EBIT_Score = clamp((7.289−12)/23×100, 0, 100) = **0.00** (still clamped at the floor).

**Forward PE + Historical PE Modifier (20% weight).**
Forward PE (fresh) = **7.706x**. No 5yr PE history reconstructable (§2) → **no-history fallback**: FwdPE_Score = **50.0** (neutral, flagged) — unchanged.

**PEG (15% weight):** N/A — redistributed to EV/EBIT.

### Raw weighted score

| Sub-score | Weight | Score | Weighted |
|---|---|---|---|
| FCF Yield | 40% | 0.00 | 0.00 |
| EV/EBIT | 40% | 0.00 | 0.00 |
| Forward PE | 20% | 50.00 | 10.00 |
| **Raw weighted score** | | | **10.00** |

Identical to 2026-06-22 — both FCF and EV/EBIT sub-scores remain saturated at their floor (0.00) even though the underlying inputs got cheaper; only the no-history FwdPE fallback (always 50.0, price-independent) contributes a nonzero weighted term.

### Modifiers

**Rate Gate modifier: +5** (from §4, unchanged).

**Upside/Downside (Expected-Return) Modifier** — fair value derived fresh in §6 below. Summary:
- Blended FV (fresh) = **345.01 GBX** (vs 337.3 GBX on 2026-06-22 — DCF component is identical since FY26 financials/guidance are unchanged; the small uplift comes entirely from peers' multiples drifting over the 2-day window).
- Gap to blended FV = (345.01/204.6186) − 1 = **+68.61%**.
- Catalyst window = 2.0 years (GBR platform/FY2027–28 clarity, unchanged — no new GBR-timeline news this cycle; WebSearch confirms GBR establishment still "expected late 2026 at the earliest," same slow-moving target as 2026-06-22) → annualized gap = **34.30%/yr**.
- Intrinsic growth = **11.5%/yr** (midpoint of FY2027 guided adjusted-EBITDA-to-net-ticket-sales ratio rising to ~2.9% from 2.80% — guidance reconfirmed unchanged by WebSearch this session: FY2027 revenue £440–455M, net ticket sales £6.2–6.45bn).
- Shareholder yield = 0% dividend + **9.46%** net buyback yield (diluted avg shares 460.83M→417.26M, FY25→FY26, unchanged) = **9.46%**.
- **E = 34.30 + 11.5 + 9.46 = 55.26%.** H = 10%. E ≥ H → uncapped M = −15×clamp((55.26−10)/15, 0, 1) = **−15.00** (hits the floor, same as before — and by an even wider margin, since the gap widened as price fell).
- **Guardrail 1 applied — capped at −5.0**, same rationale as 2026-06-22: the GBR catalyst's timeline remains unreliable in practice (still no firm launch date; the independent UBS cannibalization-risk note from the prior session stands unrefreshed and unresolved). Nothing about the CEO-change event changes this guardrail's basis — see §7 for the explicit judgment call on whether it should.

**Final Score = 10.00 (raw) + 5 (Rate Gate) − 5.0 (Upside/Downside, guardrail-capped) = 10.0.**

Per the score-boundary rule (round to nearest 0.1, ties round up): **Final Score = 10.0 — unchanged from 2026-06-22.**

---

## 6. Fair Value Derivation (re-run)

### DCF (3-stage) — scenario assumptions unchanged from 2026-06-22

FY26 financials, FY2027 guidance, and the WACC/growth scenario inputs are all unchanged in this 2-day window (no new earnings release, no revised guidance, no GBR-timeline news). The DCF is **per-share output-identical** to the prior session since it depends only on FCF0, share count, net debt, and the scenario assumptions — none of which moved:

| Scenario | Stage 1 (yrs 1–5) | Stage 2 fade | Terminal | WACC | FV/share |
|---|---|---|---|---|---|
| Bull (25%) | 9% | 7%→3% | 2.5% | 8.0% | 560.5 GBX |
| Base (50%) | 3% | 1.5% | 2.0% | 8.5% | 325.2 GBX |
| Bear (25%) | −3% | −2%→0% | 1.5% | 9.5% | 171.5 GBX |

**PW Fair Value (DCF)** = 0.25×560.5 + 0.50×325.2 + 0.25×171.5 = **345.6 GBX** (unchanged).

### Multiples (fresh peer pulls — Rule 5 caveat unchanged: 20% discount applied for comp-quality/scale mismatch)

Peer EV/EBITDA (yfinance, fresh): BKNG 12.918x / EXPE 11.394x / MMYT 28.143x / TRIP 11.715x (TCOM excluded — still negative EV/EBITDA) → median **12.317x** → implied EV = 12.317 × EBITDA 167.243M = 2,059.16M GBP → implied equity = 2,059.16M − Net Debt 167.426M = 1,891.73M GBP → implied FV/share = 1,891.73M/351,503,062 = 538.38 GBX → discounted 20% → **430.70 GBX**.

Peer Forward PE (fresh): BKNG 13.731x / EXPE 10.610x / MMYT 21.263x / TRIP 7.683x → median **12.170x** × forward EPS 0.26552 GBP = 3.2315 GBP = 323.15 GBX → discounted 20% → **258.52 GBX**.

**Multiples-Based FV = average(430.70, 258.52) = 344.61 GBX.**

### Blended Fair Value (40% DCF / 60% Multiples)

**Blended FV = 0.40×345.6 + 0.60×344.61 = 345.01 GBX.**

### Sanity check

13-analyst consensus (yfinance, fresh): target mean **351.46 GBX** / median **350.0 GBX**, range 220–580 GBX → implies +71.8–71.0% upside from the live price. The independently-derived 345.01 GBX (+68.6% upside) again lands within ~2% of consensus — cross-validates the approach.

---

## 7. Final Score + Action Recommendation — and the CEO-change judgment call

**Final Score: 10.0 → 0.0–29.9 band → BUY, Full position 6–8%. Unchanged from the 2026-06-22 entry.**

### Does the new CEO change anything?

This is the substantive qualitative question this re-run exists to answer — not a data input, a judgment call, shown transparently per the operating brief's "no black box" rule:

**What changed:** Trainline named an external successor (Ian Brown) to outgoing CEO Jody Ford, with a defined transition (joins 7 Sept, full handover/Board seat 28 Sept 2026). Brown's track record — scaling Flutter's UK & Ireland division with "sustained double-digit growth," running Booking.com's Trips Business Unit (a travel-marketplace scaling role directly analogous to Trainline's own ticketing-marketplace model), and a CEO stint at ANS Group — is a plausible, on-thesis fit for a consumer travel-tech marketplace. Sell-side reaction (Panmure Liberum) was constructive on the appointment itself.

**What this does NOT change:**
1. **Guardrail 1's basis is about GBR-catalyst timing reliability, not management quality.** The −15→−5 cap was applied because the GBR launch date keeps slipping (a *political/regulatory* catalyst risk) and because of the independent UBS cannibalization-risk note — neither concern is a management-execution question. An externally-hired CEO, however strong, does not accelerate a government legislative/regulatory timeline (GBR's establishment remains contingent on the Railways Bill and franchise-transfer schedule, confirmed unchanged by WebSearch this session — Chiltern transfers 20 Sept, GWR 13 Dec 2026, GBR itself still "expected late 2026 at the earliest"). **Guardrail 1 stays applied at −5.0, unchanged.**
2. **Phase 01 fundamentals, the Rate Gate, and all four weighted sub-scores are mechanically unchanged** (§3–5) — no earnings event occurred, so there is nothing in the financial-statement-driven score for a CEO change to move.
3. A management change *could* matter to the score if it signaled (a) a board-level loss of confidence in the existing strategy, (b) an unplanned/abrupt departure suggesting hidden problems, or (c) a successor with a track record of strategy reversals at scale-stage consumer-tech businesses. **None of these apply here**: Ford's departure was announced separately, well in advance, described by Ford himself as a planned handover ("the right time to handover to new leadership... position Trainline strongly for its next chapter") after doubling sales/profits over 6+ years — the textbook *good* succession pattern (planned, telegraphed, external hire with directly relevant marketplace-scaling experience), not a *distress* signal.
4. **If anything, this modestly *increases* qualitative confidence in execution risk being well-managed** going forward (a travel-marketplace scaling specialist replacing a long-tenured incumbent in an orderly, well-telegraphed process) — but per the framework's own discipline (Rule 9 lists "management change" as a trigger to re-examine, not a scorable input in itself; the four weighted sub-scores are financial-statement-derived by design, see "Why Forward Guidance Is Not a Sub-score" in valuation-scoring.md for the same reasoning applied to soft/qualitative inputs generally), this stays a qualitative narrative note, not a score adjustment. It does not change the Guardrail 1 cap, and it does not on its own justify uncapping toward the full −15.0 the raw E calculation would otherwise support — the GBR-timing risk that justified the cap is independent of who runs the company.

**Net effect: the new-CEO event does not change the score, the gate result, or the recommendation.** It is exactly the kind of Rule-9 event the framework's watchlist convention is designed to surface and explicitly re-examine — and having re-examined it, the conclusion is "thesis intact, reasoning re-confirmed," which per [watchlist/README.md](../watchlist/README.md) is itself worth a fresh dated pointer even with an unchanged score/action.

**Recommendation: BUY — full 6–8% position, enter now at the live price** (price has fallen further below fair value since 2026-06-22, strengthening rather than weakening the case on pure valuation grounds) **— unchanged from the 2026-06-22 recommendation, now additionally informed by a resolved management-change review that finds no reason to revise it.**

---

## 8. Order Setup

- **Fair Value (blended):** 345.01 GBX
- **Margin of Safety:** 20% (top of the 15–20% range for this score band, same choice as before — weak peer-comp set + live regulatory/political overhang + a fresh leadership-transition period to monitor)
- **Buy Price** = 345.01 × 0.80 = **276.01 GBX**
- Live price (204.62 GBX) is **below** the buy price (by 25.9%) → **enter now** at the live price.
- **Sell Target (primary, base case):** 345.01 GBX
- **Bull-Case Trim Target:** 560.5 × 0.90 = **504.45 GBX**

**Stop Loss — re-anchoring required (flagged transparently):**

The documented formula `Stop Loss = Buy Price × (1 − Max Acceptable Loss%)` produces a **degenerate result this session**: at both ends of the permitted 20–25% range, `Buy Price × (1−loss%)` (220.80 GBX at 20%, down to 207.00 GBX at 25%) sits **above** the live entry price of 204.62 GBX. This happens because the live price has fallen so far below the formal Buy Price (−25.9%, near the bottom of its 52-week range) that a stop computed off the *theoretical* Buy Price would trigger immediately on entry — the same class of artifact the 2026-06-22 session flagged at its 20% boundary, but here it affects the *entire* permitted range, not just one edge.

**Resolution:** since the score band's own action rule defines entry at the **live price** when live price is already below the formal Buy Price ("Score 0.0–29.9 → Stock at or below buy price → Enter now" — fair-value-methodology.md Step 2), the live price is the operative entry point this session, exactly as Step 6's R/R formula already uses "Entry Price" (not the theoretical Buy Price) for its own calculation. Re-anchoring the Stop Loss formula to the actual entry price (live price) rather than the now largely theoretical Buy Price resolves the degeneracy without inventing a new rule — it applies the existing formula's intent (a bounded % loss *from the price actually paid*) consistently with how R/R is already computed:

| Max loss % (from live entry, re-anchored) | Stop Loss (GBX) | R/R | vs. 52wk low (178.0 GBX) |
|---|---|---|---|
| 20% (chosen) | **163.69** | **3.43:1** | below — flagged, see note |
| 22.5% | 158.58 | 3.05:1 | below |
| 25% | 153.46 | 2.74:1 | below |

**Stop Loss = 163.69 GBX (20% max loss from live entry — the tightest end of the permitted range, chosen to minimize the dollar risk per share while still clearing the R/R minimum comfortably).**

**Flag:** all three candidate stops sit below the 52-week low of 178.0 GBX — a mechanical consequence of price already trading near (within ~15% of) its 52-week low at entry, leaving no stop within the framework's permitted 20–25% band that sits above the 52-week low. This is shown transparently rather than silently overridden; it does not change the recommendation (R/R still clears 2:1 by a wide margin at all three candidate stops), but it does mean this stop is wider, in absolute terms, than the stock's own recent trading range — a fair description of the real situation (a thesis that the market is currently pricing skeptically) rather than an artifact to paper over.

**R/R = (345.01 − 204.62) / (204.62 − 163.69) = 140.39 / 40.93 = 3.43:1** — clears the 2:1 minimum comfortably.

**Position Sizing:**
- Portfolio value: $55,813.07 (unchanged since the 2026-06-22 sync — IBKR $40,689.53 + Freedom24 $15,123.54, per `holdings.md`; no new sync has run in this 2-day window).
- Entry (USD) = 2.046186 GBP × 1.318774 (GBPUSD, fresh 2026-06-24 close) = **$2.6985/share**.
- Stop (USD) = 1.6369 GBP × 1.318774 = **$2.1592/share**.
- Risk/share = $2.6985 − $2.1592 = **$0.5393**.
- Max $ risk = 1.5% × $55,813.07 = **$837.20**.
- Risk-based shares = $837.20 / $0.5393 ≈ **1,553 shares** → ≈ **$4,191.30** (≈7.51% of portfolio).
- Allocation cap for Score 0.0–29.9: 6–8% of portfolio = $3,348.78–$4,465.05.
- **Position Size = min(risk-based ≈$4,191.30, allocation cap $4,465.05) = ≈$4,191.30 (≈7.51% of portfolio, ≈1,553 shares at $2.6985/share)** — the risk-based figure binds this time (unlike 2026-06-22, where the cap bound), because the wider re-anchored stop distance increases risk-per-share enough to pull risk-based sizing down into the cap range on its own.
- Cross-check vs. the hard 15% single-position cap (Upgrade 7): $8,371.96 — well under. **PASS.**

**This recommendation is not executed by this session — trade execution remains exclusively human, per the framework's hard constraints.**

---

## 9. Portfolio Rebalancing Summary

N/A — TRN is not currently held; this remains a new-position evaluation, not a rebalance.

---

## 10. Next Review Trigger

- **Mandatory:** Trainline's FY2027 interim/H1 results (next scheduled report) — Rule 9.
- Any GBR-related announcement in either direction (further delay, concrete platform launch date, confirmation/denial of Trainline's continuing retailer role).
- **New, specific to this event:** **Ian Brown's effective start (7 Sept 2026) and full Board/CEO handover (28 Sept 2026)** — worth a check-in once he is actually in seat and has had the opportunity to signal strategic direction (continuity vs. a new capital-allocation or international-expansion posture); not a re-score trigger on its own unless it comes with a fundamental change (e.g. a strategy reset, guidance revision, or M&A signal).
- "Management change" is **dropped** from the trigger list below — this session resolves that specific open item from the 2026-06-22 entry.
- >15% unexplained price move from 204.62 GBX (Rule 9) — note today's ~4–5% move is *explained* by the CEO-change news itself and does not count toward this threshold.
- Standard Rule 9 triggers: guidance revision, M&A.
- Same open Rule 5 item as before: expanding the comparables set past the four distant peers (BKNG/EXPE/MMYT/TRIP) would strengthen compliance if revisited, though not required to act on the current score.

---

## Glossary

- **52-week range** — the lowest and highest price a stock has traded at over the past year.
- **CAGR** — Compound Annual Growth Rate.
- **DCF** — Discounted Cash Flow.
- **EBIT / EBITDA** — Earnings Before Interest (and Taxes) / before Depreciation & Amortization too.
- **EPS** — Earnings Per Share.
- **EV** — Enterprise Value.
- **EV/EBIT, EV/EBITDA** — Enterprise Value divided by operating profit measures.
- **EY (Earnings Yield)** — 1 ÷ Forward PE.
- **Fast Grower** — Peter Lynch's term for >15%/yr EPS growth for 3+ years; this framework's PEG-eligibility trigger.
- **FCF** — Free Cash Flow.
- **FCF Yield** — FCF ÷ Market Cap (or EV).
- **FCF/NI conversion ratio** — FCF ÷ Net Income; checks earnings quality.
- **Forward PE** — Price ÷ next-12-months expected EPS.
- **FV (Fair Value)** — the analyst's estimate of intrinsic worth.
- **GBR (Great British Railways)** — UK rail-nationalization program; see glossary.md.
- **GBX / pence (GBp)** — 1/100th of a British pound; LSE quoting convention.
- **MoS (Margin of Safety)** — discount below fair value used for the buy price.
- **Net Debt/EBITDA** — leverage ratio; this framework's balance-sheet-risk gate.
- **NOPAT** — Net Operating Profit After Tax (EBIT × (1 − tax rate)) — used to compute ROIC.
- **PE (Price-to-Earnings) ratio**, **PEG ratio** — standard valuation multiples; PEG = PE ÷ growth rate.
- **PW (Probability-Weighted) Fair Value** — 25% bull + 50% base + 25% bear blended estimate.
- **R/R (Risk/Reward ratio)** — expected gain ÷ expected loss on a trade; 2:1 minimum required.
- **Rate Environment Gate / Rate Regime Modifier** — the mandatory pre-score interest-rate check.
- **RNS (Regulatory News Service)** — the LSE's official company-announcement disclosure channel; the UK equivalent of a US SEC 8-K filing. Used here for the qualitative narrative only, never as a scoring input.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — always fetch a live price before any valuation work.
- **Rule 5** — comparables-set quality requirement (peers within ±50% revenue scale, 5 minimum).
- **Rule 7** — Probability-Weighted (bull/base/bear) fair value blending.
- **Rule 9** — fundamental events that force an immediate re-score (earnings, guidance, M&A, management change, macro shift, >15% unexplained move).
- **Rule 10** — catalyst + timeline requirement for crediting large expected upside.
- **Shareholder yield** — dividend yield + net buyback yield.
- **Upside/Downside Modifier (Expected-Return Modifier)** — the ±15 additive score adjustment based on expected annual return.
- **WACC** — Weighted Average Cost of Capital; the DCF discount rate.

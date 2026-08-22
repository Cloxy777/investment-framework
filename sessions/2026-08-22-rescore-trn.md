# RESCORE — TRN (Trainline plc, LSE:TRN) — mode `--both`

**Task type:** RESCORE (Rule 9 re-score — >15% unexplained-move threshold breached since the 2026-08-16 portfolio sync)
**Date:** 2026-08-22
**10Y US Treasury Yield:** **4.74%** (2026-08-21 close, per tradingeconomics.com — FRED's own CSV endpoint returned HTTP 403 to WebFetch this session; cross-checked against CNBC/WebSearch reporting "around 4.7%, tested a 20-month high of 4.75% earlier in the week" — consistent, not identical to the decimal)
**Rate Regime Modifier in effect:** +5 (3.5–5% bracket — unchanged)
**Last review:** 2026-07-05 (Valuation Score 10.0, Quality Score 67.2 — fails 80.0+ gate, Composite 21.4 reference-only; HOLD, do not complete partial-fill top-up)
**Position status:** Held, 600 shares, unchanged since 2026-06-24 (confirmed via this morning's `/sync-portfolio`); weight 2.65% per [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session was triggered

This morning's `/sync-portfolio` (2026-08-22) flagged TRN's price down **22.4%** since the 2026-08-16 sync (£2.544 → £1.975/share, i.e. GBX 254.4 → 197.5), well past the ±15% Rule 9 "unexplained move" threshold. Share count was unchanged (600) — a pure price move, not a trade. This session investigates the cause and re-scores.

---

## 1. Live price (Rule 0 — fetched first)

- **IBKR `get_price_snapshot` (contract_id 371871705):** last **197.5 GBX**, no halt.
- **Cross-check:** `yfinance` `TRN.L` `currentPrice`/`regularMarketPrice` = **197.5** — exact match.
- **Price of record for this session: 197.5 GBX = 1.9750 GBP.**
- **FX rate:** live GBP→USD from IBKR `get_account_balances` (fetched this session, same-day sync) = **1.3644824**. → 197.5 GBX = **$2.6949 USD**.
- **Move context:** down −9.4% from the 2026-07-05 session's 218.00 GBX, but the path matters — TRN actually *rose* to ~254.4 GBX by 2026-08-16 (+16.7% from 07-05) before the event below erased that gain and more.

---

## 2. What caused the move — CMA "drip pricing" investigation (2026-08-19)

The UK Competition and Markets Authority (CMA) opened a formal investigation into whether Trainline engaged in **drip pricing** — presenting mandatory booking fees (cited: 59p–£2.79 per train booking, £1.50 per coach ticket) later in the purchase flow rather than in the headline price. Shares fell ~14% on the announcement (Wed 2026-08-19, to 208.4p), then a further ~9% the next day (to ~190p, session low 181p) — a combined **~£188M market-cap loss over two sessions**.

**Key facts, cited:**
- **Maximum potential fine: ≈£45.3M** (10% of FY2026 global turnover, £452.7M) — the regulator can also order customer compensation for fees charged since its consumer powers took effect April 2025. This is only ~6.7% of TRN's current ~£674M market cap — the fine itself is not existential; the market's reaction (4.2× the max fine) reflects fear of a bigger structural risk to the fee-based revenue model.
- **Early stage — no finding of wrongdoing.** Investigation status, no completion timeline disclosed.
- **Management response (cited):** confirmed the company has "been working proactively for months" and is "modifying how some fees are displayed" — no formal guidance revision issued.
- **Analyst targets are stale relative to this event** — the consensus figures found this session (mean ~GBX 397.67 / ~360, sourced 2026-08-18) **predate the CMA announcement by 1–3 days** and have not been revised down; even JPMorgan's most bearish rated target (Sell, 220p) still sits above the ~190–197.5p trading range.

**Why this matters directly to this framework's existing TRN thesis, not just generically:** the 2026-07-05 session's Moat Signal checklist already marked **Brand Premium FALSE**, citing independent testing showing Trainline is consistently the *most expensive* booking option specifically because of its booking fee, losing head-to-head price comparisons to fee-free rivals (TrainPal, Railboard). The CMA probe is a formal regulatory escalation of exactly that same weakness — not a new, unrelated risk.

Sources: [ts2.tech](https://ts2.tech/en/trainlines-188-million-selloff-prices-more-than-four-times-its-maximum-cma-fine/), [Yahoo Finance UK](https://uk.finance.yahoo.com/news/trainline-shares-drop-14-competition-075000085.html), [Proactive Investors](https://www.proactiveinvestors.com.au/companies/news/1097255/trainline-shares-drop-14-as-competition-watchdog-opens-drip-pricing-probe-1097255.html), [The Stock Observer](https://www.thestockobserver.com/2026/08/19/trainline-lontrn-shares-down-14-1-heres-why.html).

**No other Rule 9 trigger found this session:** no new earnings release (FY2027 H1/interim not yet due — FYE 28-Feb, next report expected ~Oct 2026); no CEO/CFO-level management change (Ian Brown's handover, effective 7 Sept / full 28 Sept 2026, is scheduled, unchanged, not yet occurred); no guidance revision (FY26 figures are the latest on record, same as 07-05 — confirmed via fresh `yfinance` pull, see §3 below, identical to the pound); no M&A.

---

## 3. Data refresh — fresh `yfinance` pull, TRN.L (this session)

Unlike the 2026-07-05 session (where EBIT/EBITDA/cashflow/balance-sheet modules returned null/inconsistent for this ticker), this session's pull returned full, populated financials. All FY2026 (FYE 28-Feb-2026) figures **match the 07-05 session's carried-forward figures exactly, to the pound** — confirming no new fiscal year has reported and no restatement occurred:

| Field | Value (FY2026) |
|---|---|
| Total Revenue | £452,684,000 |
| Net Income | £79,813,000 |
| EBIT | £126,429,000 |
| EBITDA | £167,243,000 |
| Free Cash Flow | £79,547,000 |
| Operating Cash Flow | £133,019,000 |
| Net Debt | £167,426,000 |
| Total Debt | £261,946,000 |
| Cash | £59,703,000 |
| Invested Capital | £431,498,000 |
| Total Equity | £204,369,000 |

**Known vendor quirk, reconfirmed:** `yfinance`'s aggregate `info["ebitda"]` field still returns £125,823,000 — below the independently-verified EBIT (£126,429,000), which is impossible (EBITDA = EBIT + D&A, D&A can't be negative). Same inconsistency flagged 2026-06-22/07-05; the line-item `financials.loc["EBITDA"]` (£167,243,000) is used instead, as before. Similarly `info["enterpriseValue"]` (£947,232,256) doesn't reconcile with a manually-built EV (MarketCap + Total Debt − Cash, see §5) — the manual build is used throughout, consistent with prior sessions.

**Shares outstanding (fresh):** 341,488,172 (down from 349,035,615 on 07-05 — a further ~2.16% reduction over 48 days from the ongoing buyback program). Market Cap = 341,488,172 × 1.9750 GBP = **£674,439,139.7** (matches `yfinance`'s own `marketCap` field, 674,439,104, to the pound).

**Forward EPS (fresh):** 0.26487 GBP (vs. 0.26552 on 07-05 — a marginal downward revision, immaterial).

**5-year historical PE range:** still unavailable (same no-history gap as every prior TRN session) — `FwdPE_Score` uses the no-history fallback (50.0, neutral, flagged), unchanged.

---

## 4. Quality Score — recomputed fresh, same FY2026 base

Per [quality-scoring.md](../framework/quality-scoring.md). All inputs reconfirmed live this session (§3) rather than blindly carried forward.

**Hard disqualifier check:**

| Disqualifier | TRN status | Result |
|---|---|---|
| FCF/NI <70% for 2+ consecutive years | FY26 99.667%, FY25 164.33% | ✅ PASS |
| Net Debt/EBITDA over threshold (2.5× standard) | 1.00109× | ✅ PASS |
| Not FCF-positive for 3+ consecutive years | FCF positive 4/4 reconstructable years | ✅ PASS |

No hard disqualifier fires.

**Profitability (25%):**
```
Net Margin = 79,813,000 / 452,684,000 = 17.632%
ROIC = (126,429,000 × 0.70) / 431,498,000 = 88,500,300 / 431,498,000 = 20.510%
NetMargin_Component = clamp((17.632/30)×100) = 58.77
ROIC_Component       = clamp((20.510/30)×100) = 68.37
Profitability_Score  = (58.77 + 68.37) / 2 = 63.57
```

**Margins (15%):**
```
Gross Margin = 82.591% (yfinance grossMargins 0.82591003, matches prior session)
GrossMargin_Score = clamp((82.591/80)×100, 0, 100) = 100.0
```

**Growth (20%):**
```
Revenue 3yr CAGR = 11.43% (FY23 327,147,000 → FY26 452,684,000, unchanged — same FY base)
Growth_Score (base) = clamp((11.43/25)×100) = 45.72
```
TAM-expansion modifier (+10) and structural-deceleration modifier (−10): both carried forward unchanged — no new fiscal year has reported to re-test either the International Consumer/Solutions TAM evidence or the guided flat-to-down FY2027 revenue trend cited 07-05. Net to zero, same as before.
```
Growth_Score = 45.72 + 10 − 10 = 45.72
```

**Balance Sheet (15%):**
```
Net Debt/EBITDA = 167,426,000 / 167,243,000 = 1.00109×
BalanceSheet_Score = clamp(100×(1 − 1.00109/4), 0, 100) = 74.97
```

**Moat Signal (15%)** — re-examined fresh against this session's news, not blindly carried forward:

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** (unchanged) | No new evidence contradicts the 07-05 finding (est. 51/100 UK train tickets, ~72% of the independent online rail-retail market). |
| Brand premium (pricing power) | **FALSE** (unchanged, reinforced) | The 07-05 finding — Trainline is consistently the *most expensive* booking option due to its booking fee — is now the **explicit subject of a formal CMA drip-pricing investigation** (§2). A regulator opening a case specifically because fees are opaque/back-loaded is corroborating, not new, evidence against a "customers pay willingly" brand-premium read. Not credited, same as before — now on stronger evidentiary footing. |
| Network effect | **FALSE** (unchanged) | Multi-homing evidence (TrainPal/Railboard price comparison) still applies; unaffected by this session's news. |
| Switching costs | **TRUE** (unchanged) | App stickiness mechanism (saved journeys/payment methods, delay notifications) is unrelated to the fee-display controversy. |
| Scale cost advantage | **FALSE** (unchanged) | No new cost-per-unit data found this session. |

```
Moat_Score = (2/5) × 100 = 40.0   (unchanged, but Brand Premium's FALSE call is now regulator-corroborated)
```

**FCF Quality (10%):**
```
FCF/NI = 79,547,000 / 79,813,000 = 99.667%
FCFQuality_Score = clamp(((0.99667 − 0.40)/0.60)×100, 0, 100) = 99.44
```

### Quality Score total

```
Quality Score = 63.57×0.25 + 100.0×0.15 + 45.72×0.20 + 74.97×0.15 + 40.0×0.15 + 99.44×0.10
             = 15.8925 + 15.00 + 9.144 + 11.2455 + 6.00 + 9.944
             = 67.23 → 67.2
```

**Quality Score = 67.2 — still FAILS the 80.0+ gate**, numerically identical to 07-05 (same FY2026 fundamentals; the CMA news is a forward-looking regulatory/reputational risk that hasn't yet moved any of the six graded sub-scores — it reinforces the already-uncredited Brand Premium signal rather than changing its verdict).

---

## 5. Rate Environment Gate

- **Step 1 — Earnings Yield Spread Test:** Forward PE = 197.5/100 GBP ÷ 0.26487 GBP forward EPS = **7.4566×**. EY = 1/7.4566 = **13.411%**. Spread = 13.411% − 4.74% = **+8.671pp** ≥ +1.5% → no flag (+0).
- **Step 2 — Rate Regime Modifier:** 10Y = 4.74%, in the 3.5–5% bracket → **+5**.
- **Combined Rate Gate modifier: +5** — same bracket as 07-05.

---

## 6. Valuation Score

### Sub-scores (fresh price, fresh shares outstanding)

**FCF Yield (40% weight):**
```
FCF Yield = 79,547,000 / 674,439,104 = 11.797%
FCF_Score = clamp(100×(1 − 11.797/10), 0, 100) = 0.00   (floor-saturated — even more so than 07-05's 10.454%, price fell faster than nothing)
```

**EV/EBIT (40% weight, PEG-redistributed — see below):**
```
EV = MarketCap 674,439,104 + Total Debt 261,946,000 − Cash 59,703,000 = 876,682,104 GBP
EV/EBIT = 876,682,104 / 126,429,000 = 6.934×
EV/EBIT_Score = clamp((6.934−12)/23×100, 0, 100) = 0.00   (floor-saturated)
```

**Forward PE + Historical PE Modifier (20% weight):**
```
Forward PE = 7.4566× (from §5). No 5yr PE history reconstructable (§3) → no-history fallback:
FwdPE_Score = 50.0 (neutral, flagged) — unchanged
```

**PEG:** N/A — same reasoning as 07-05 (no new fiscal year to re-test the clean-earnings-base condition). Redistributed to EV/EBIT (→40%).

### Raw weighted score

| Sub-score | Weight | Score | Weighted |
|---|---|---|---|
| FCF Yield | 40% | 0.00 | 0.00 |
| EV/EBIT | 40% | 0.00 | 0.00 |
| Forward PE | 20% | 50.00 | 10.00 |
| **Raw weighted score** | | | **10.00** |

**+ Rate Gate modifier: +5** → **15.00** (before Upside/Downside).

### Upside/Downside (Expected-Return) Modifier

**Fair Value:**
- **DCF component: 345.6 GBX — carried forward, with an explicit caveat this session.** Same FY26-financials-based 3-scenario DCF as 07-05 (Bull 560.5 / Base 325.2 / Bear 171.5 GBX, 25/50/25 weighted). **This Bear case predates the CMA investigation (§2) and does not incorporate any scenario for a forced fee-structure change or take-rate compression.** Re-deriving the DCF from scratch with a CMA-specific downside scenario would require assumptions (probability of an adverse finding, magnitude of any forced fee reduction, resulting take-rate impact) not available from any cited source this session — inventing those inputs would violate this framework's "never invent or estimate financial data" rule more than the alternative of flagging the gap explicitly. **Treat this session's Blended FV as likely somewhat optimistic pending a bear-case revision once the CMA investigation's shape becomes clearer** (see §8 next-review triggers).
- **Multiples component — fresh peer pull this session:**
  - Peer EV/EBITDA (fresh): BKNG 15.482× / EXPE 13.296× / MMYT 37.179× / TRIP 11.126× (TCOM excluded, still negative EV/EBITDA at −1.067×) → median **14.389×** → implied EV = 14.389 × TRN EBITDA 167,243,000 = 2,406,459,527 GBP → implied equity = 2,406,459,527 − Net Debt 167,426,000 = 2,239,033,527 GBP → implied FV/share = 2,239,033,527/341,488,172 = 6.5566 GBP = 655.66 GBX → discounted 20% (Rule 5, thin/size-mismatched peer set) → **524.53 GBX**.
  - Peer Forward PE (fresh): BKNG 16.937× / EXPE 13.296× / MMYT 24.355× / TRIP 9.303× → median **15.1165×** × forward EPS 0.26487 GBP = 4.0033 GBP = 400.33 GBX → discounted 20% → **320.26 GBX**.
  - **Multiples-Based FV = average(524.53, 320.26) = 422.40 GBX.**
- **Blended FV = 0.40×345.6 + 0.60×422.40 = 138.24 + 253.44 = 391.68 GBX.**

**Sanity check:** analyst consensus figures found this session — mean ~GBX 397.67, 13-analyst 12-month target ~360 (sourced 2026-08-18, i.e. **1–3 days before the CMA announcement**, not yet revised). Our 391.68 GBX sits within/close to this pre-CMA range, but **both numbers are now stale relative to the news** — this is not a meaningful independent confirmation this session, just a note that our model hasn't drifted further from the (also-stale) consensus than before.

```
Gap Upside % = (391.68 / 197.5) − 1 = +98.32%
Catalyst window = 2.0 years (unchanged — GBR timeline, see below)
Annualized gap = 98.32% / 2.0 = 49.16%/yr
Intrinsic growth = 11.5%/yr (carried forward — no new FY26/27 guidance since 07-05)
Shareholder yield = 0% dividend + 9.46% net buyback yield (FY26 annual company-disclosed figure, carried forward — corroborated qualitatively by the further ~2.16% share-count reduction observed this session over the 48-day window)

E = 49.16 + 11.5 + 9.46 = 70.12%.  H = 10%.  E ≥ H → uncapped M would be −15.0 (floor)
```

**Guardrail 1 (catalyst reliability) — unchanged, still applied:** GBR's full operational launch is still tracked to 2027, not confidently inside an 18–24 month window from today — same basis as 07-05, no new information found this session narrowing that timeline. **Guardrail 1 stays applied — capped at −5.0.**

**Additional caveat this session (not a formal guardrail, since none in the framework covers "fresh negative regulatory catalyst not yet in the FV"):** the size of `E` (70.12%, driven mostly by the 98.32% price-gap term) is inflated by the same DCF-staleness issue flagged above — the price fell on real new information the Bear case doesn't yet reflect. The −5.0 guardrail cap is doing more work than usual this session; it is not a coincidence that it lands at exactly the same place as 07-05.

**M = −5.0.**

### Final Valuation Score

```
Final Score = 15.00 (raw + Rate Gate) + (−5.0) (Upside/Downside, guardrail-capped) = 10.00
```

**Final Valuation Score = 10.0 — numerically unchanged from 07-05**, despite the 22.4%/9.4% price moves — both floor-saturated sub-scores and the guardrail-capped modifier absorbed the entire move without the final number budging. Worth stating plainly since it could otherwise look like a stale or ignored result: the framework's structure, not oversight, produces this.

---

## 7. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 67.2) + 0.50 × 10.0
                = 16.4 + 5.0
                = 21.4
```

**Composite Score = 21.4 — numerically unchanged from 07-05.** Lands in the "BUY — Full position 6–8%" band (0.0–29.9) by the numbers alone. **Per this framework's established practice for held positions whose Quality Score fails the 80.0+ gate, this is a false green light and is not acted on at face value** — same standing rule applied 07-05.

---

## 8. Action recommendation — HOLD existing 600 shares; do **NOT** add; heightened Quality Watch

**The bottom-line action is unchanged from 07-05: HOLD, do not top up.** The Quality Score (67.2 < 80.0) was already the sole, sufficient blocker before this session, and remains so — the CMA news doesn't change that conclusion, it adds a second, independent reason not to add capital right now even setting the gate aside.

**What's different this session:** a live, formal regulatory investigation directly targeting the exact weakness (fee opacity / no genuine brand premium) this framework's own Moat Signal checklist had already identified and marked FALSE. This is exactly the kind of "signal worth surfacing" the Phase 04 Quality Watch escalation exists for — not yet a Phase 06 Full Exit trigger (no balance-sheet crisis, no management change, no confirmed finding of wrongdoing — the CMA hasn't concluded anything), but a live risk that should stay front-of-mind, not filed away as "checked, no action."

**Two Phase 06 triggers were checked and do NOT fire:**
- Balance sheet crisis: no — leverage (Net Debt/EBITDA 1.00×) and liquidity are unaffected; the max theoretical fine (~£45.3M) is ~6.9% of market cap and well within the balance sheet's capacity to absorb if it materialized.
- Management change: no — Ian Brown's CEO handover remains a scheduled, previously-known transition (7/28 Sept 2026), not a reactive departure tied to this investigation.

**Not recommending a forced trim or exit on this session's evidence alone** — the CMA case is at an early, unresolved stage, and this framework's discipline (Phase 05, "fair value alone is not a sell") argues against reactive trimming on an investigation with no finding yet. But this is now a name to watch closely, not a name to add to.

### Informational-only order setup (shown for transparency — NOT being executed, same as 07-05)

```
Blended Fair Value = 391.68 GBX  (caveated — see §6, likely optimistic pending bear-case revision)
Buy Price (20% MoS) = 391.68 × 0.80 = 313.34 GBX
Live price (197.5 GBX) vs. Buy Price: 37.0% below → would read "enter now" if gate-eligible
Primary Sell Target = 391.68 GBX
Bull-Case Trim Target = 560.5 × 0.90 = 504.45 GBX  (DCF Bull carried forward, same caveat)
Stop Loss — re-anchored to live entry (same degeneracy as prior sessions, Buy-Price-anchored stop is meaningless when price has fallen this far below it):
  20% below live entry → 197.5 × 0.80 = 158.00 GBX
  Flag: this stop sits below the 52-week low (178.00 GBX, yfinance) — a real consequence of trading near/below 52-week lows, not a calculation error.
R/R = (391.68 − 197.5) / (197.5 − 158.00) = 194.18 / 39.50 = 4.92:1 — clears the 2:1 minimum by a wide margin

Portfolio context (fresh, this morning's /sync-portfolio): combined total ≈ $61,101.89
Entry (USD) = 1.9750 GBP × 1.3644824 = $2.6949/share
Stop (USD)  = 1.5800 GBP × 1.3644824 = $2.1559/share
Risk/share  = $0.5390
Max $ risk (1.5%) ≈ $916.53
Risk-based target shares ≈ 916.53 / 0.5390 ≈ 1,700 shares (≈$4,581, ≈7.50% of portfolio)
Allocation cap (Score 0.0–29.9): 6–8% ≈ $3,666.11–$4,888.15
Position Size = min(risk-based ≈$4,581, cap) ≈ $4,581 — well inside the 15% hard cap (~$9,165)
Incremental top-up implied: ≈1,700 − 600 ≈ 1,100 shares (≈$2,964 at live price)
```
**Not executed.** The Quality Gate governs, independent of how attractive these mechanics look — same standing conclusion as 07-05, now reinforced by the CMA overhang.

---

## 9. Portfolio Rebalancing Summary

N/A — single-ticker rescore, no other position touched this session.

---

## 10. Next Review Trigger

- **Mandatory, new this session:** any update on the CMA drip-pricing investigation — a finding of wrongdoing (or clearance), a fine/remedy amount, or a fee-structure change Trainline makes in response. This is now the binding near-term catalyst, ahead of the FY2027 results.
- **Mandatory:** Trainline's FY2027 interim/H1 results (next scheduled report, expected ~Oct 2026) — will also let the DCF Bear case be properly re-derived with post-CMA information rather than carried forward with the caveat in §6.
- Ian Brown's full CEO/Board handover (28 Sept 2026) — a check-in once in seat, not a re-score trigger alone unless paired with a strategy reset or the CMA response.
- Any GBR-related announcement — still the binding constraint on Guardrail 1's −5 cap.
- Re-test the Moat's Brand Premium and Network Effect signals once the CMA situation clarifies — a forced fee-structure change could flip Brand Premium from "actively FALSE" to "structurally impossible to credit for the foreseeable future," or (less likely) a favorable resolution could ease the price-competition pressure cited against it.
- Standard Rule 9 triggers: guidance revision, M&A, >15% unexplained price move, management change.

---

## 11. Glossary

- **CAGR** — Compound Annual Growth Rate.
- **CMA (Competition and Markets Authority)** — the UK's competition/consumer-protection regulator; opened the drip-pricing investigation into Trainline this session.
- **Composite Score** — this framework's 0.0–100.0 blended ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; computed only for reference here since Quality fails the gate.
- **D&A** — Depreciation & Amortization.
- **DCF** — Discounted Cash Flow.
- **Drip pricing** — presenting mandatory charges later in a purchase flow rather than in the advertised headline price; the specific practice the CMA is investigating.
- **EBIT / EBITDA** — operating profit before interest and taxes / before interest, taxes, depreciation and amortization.
- **EPS** — Earnings Per Share.
- **EV / EV/EBIT, EV/EBITDA** — Enterprise Value / Enterprise Value divided by operating-profit measures.
- **EY (Earnings Yield)** — 1 ÷ Forward PE.
- **FCF / FCF Yield / FCF/NI conversion ratio** — Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks earnings quality).
- **Forward PE** — Price ÷ next-12-months expected EPS.
- **FV / PW Fair Value** — Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear).
- **GBR (Great British Railways)** — UK rail-nationalization program; relevant to TRN as a regulatory/political risk to its retailer role.
- **GBX / pence (GBp)** — 1/100th of a British pound; LSE quoting convention.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of weighted score.
- **Hurdle rate** — the minimum acceptable annual return (10% in this framework).
- **Moat** — a durable competitive advantage protecting a business's profits.
- **MoS (Margin of Safety)** — the discount below fair value demanded before buying.
- **Multi-homing** — customers using multiple competing platforms rather than committing to one, diluting an otherwise-plausible network effect.
- **Net Debt/EBITDA** — leverage ratio; this framework's balance-sheet-risk gate.
- **NOPAT** — Net Operating Profit After Tax (EBIT × (1 − tax rate)).
- **PE (Price-to-Earnings) ratio**, **PEG ratio** — standard valuation multiples; PEG = PE ÷ growth rate.
- **Phase 04 Quality Watch** — this framework's escalation flag for a held position whose Quality Score sits below the 80.0+ gate or is deteriorating.
- **Phase 06** — this framework's exit-review phase (balance-sheet crisis, management change, and other full-exit triggers).
- **PW (Probability-Weighted) Fair Value** — 25% bull + 50% base + 25% bear blended estimate.
- **Quality Score** — this framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02 valuation scoring.
- **Rate Environment Gate / Rate Regime Modifier** — the mandatory pre-score interest-rate check.
- **R/R (Risk/Reward ratio)** — expected gain ÷ expected loss on a trade; 2:1 minimum required.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — always fetch a live price before any valuation work.
- **Rule 5** — comparables-set quality requirement (discount applied for thin/mismatched peer sets).
- **Rule 9** — fundamental events that force an immediate re-score; this session's trigger (>15% unexplained price move, subsequently explained by the CMA news).
- **Upside/Downside Modifier (Expected-Return Modifier)** — the ±15 additive score adjustment based on expected annual return.

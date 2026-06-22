# New Position Evaluation — TRN (Trainline plc, LSE:TRN)

**Task type:** NEW POSITION
**Date:** 2026-06-22
**10Y US Treasury Yield:** 4.483% (^TNX, yfinance, close 2026-06-22)
**Rate Regime Modifier in effect:** +5 (3.5–5% bracket)

**Trigger:** Telegram post, t.me/bolshegold #9608 (~10:50 UTC 2026-06-22, edited). The channel admin commented that Keir Starmer's departure delays the GBR (Great British Railways) project, creating "another 0.5–1 year of political shock," and named ticker $TRN. **The post text is used only as a trigger to look at this ticker — no number from it is used anywhere in this scoring.** All data below is sourced from yfinance, IBKR, and WebSearch as cited inline.

---

## 0. Ticker resolution (multi-candidate symbol)

"TRN" is shared by at least four listed companies. IBKR `search_contracts("TRN")` returned, among others:

| Company | Exchange | Contract ID |
|---|---|---|
| Terna SpA | BVME (Italy) | 30664870 |
| Trinity Industries Inc | NYSE | 12974 |
| **Trainline plc** | **LSE** | **371871705** |
| Trans Polonia SA | WSE (Poland) | 403408873 |

Plus several unrelated TRN-prefixed tickers (TRNO, TRNFP, TRNS, etc.) that are not plausible matches.

**Resolution: Trainline plc, LSE:TRN, IBKR contract_id 371871705, yfinance ticker `TRN.L`.** The Telegram post's context (UK rail policy, "GBR," "Keir Starmer") only plausibly maps to a UK rail-ticketing business. Independent WebSearch confirms Trainline is widely reported as "ticker $TRN" and that "Trainline will maintain a role as a ticket retailer even after GBR is established" — directly on-topic for the post's GBR-delay claim. Terna (Italian electricity grid operator), Trinity Industries (US railcar manufacturer), and Trans Polonia (Polish logistics) have no connection to UK rail nationalization. TRN has zero prior watchlist entries, so per `telegram-scan.md` step 4 this requires a full `/new-position` evaluation (this session).

---

## 1. Live price (Rule 0 — fetched first, before any valuation work)

- **IBKR `get_price_snapshot`(contract_id=371871705):** last **216.2 GBX** (pence), bid 215.99 / ask 216.40, change −2.2 (−1.01%), 52-week range 177.99–303.99 GBX (13-week high 255.6 / low 198.7).
- **yfinance `TRN.L` cross-check:** currentPrice 215.8 GBp — consistent with IBKR within normal bid/ask noise.
- **Price of record for this session: 216.2 GBX = 2.162 GBP.**
- **FX rate:** `GBPUSD=X` (yfinance), most recent close 2026-06-22 = **1.326929** USD/GBP. → 216.2 GBX = 2.162 GBP = **$2.8688 USD**.

All figures below are stated in GBP/GBX unless marked USD, per the GBX/pence glossary note.

---

## 2. Data gaps flagged

- **5-year historical PE range:** `t.get_earnings_dates(limit=40)` on `TRN.L` returns no usable historical Reported-EPS rows (only one forward-dated row, NaN values); `quarterly_financials`/`earnings_history` are likewise empty. **No 5yr PE history is reconstructable.** This is the documented "no-history fallback" case in valuation-scoring.md (not a stop condition) — `FwdPE_Score = 50.0`, flagged neutral.
- **PEG/Fast-Grower eligibility:** ruled **not applicable** — see Phase 02 §4 below. Not a missing-data gap; a methodology eligibility call.
- **Peer comparables:** the only public companies with comparable EV/EBITDA and forward-PE data (Booking Holdings, Expedia, MakeMyTrip, Tripadvisor) are 30–150x Trainline's market cap — a Rule 5 (comparables) violation, since no peer sits within the ±50% revenue band. Trainline's closest true peers (e.g. Omio) are private/VC-backed with no public multiples. Flagged and discounted (see §6), not blocking.

None of these gaps block the evaluation; all are handled via documented framework fallbacks, flagged transparently below (same treatment as the 2026-06-21 WSE session for the same kind of gap).

---

## 3. Phase 01 — Quality Gate

| Criterion | Threshold | TRN (FY2026, FYE Feb-2026) | Basis | Result |
|---|---|---|---|---|
| Net margin | >15% (>12% pre-screen) | **17.63%** | NI 79.813M / Rev 452.684M | ✅ |
| ROIC | >15% | **20.46%** (FY26 only; FY23–25 were 7.24%/8.81%/14.80%) | NOPAT (EBIT×(1−tax)) / Invested Capital | ✅ (current yr) |
| Revenue CAGR 3yr | >10% (>8% pre-screen) | **11.43%** | FY23 327.147M → FY26 452.684M | ✅ |
| Gross margin | >40% or expanding | **82.59%**, expanding (77.10%→76.95%→79.69%→82.59%) | Gross Profit / Revenue, FY23–26 | ✅ |
| FCF positive, 3 consecutive years | required | **4/4 years positive**: 4.387M / 81.846M / 95.886M / 79.547M | yfinance cashflow, FY23–26 | ✅ |
| Net Debt/EBITDA | <2.5x (Debt Gate, Upgrade 5 standard) | **1.001x** (FY26); FY23–25: 1.109x/0.506x/0.563x | Net Debt 167.426M / EBITDA 167.243M | ✅ |
| FCF/NI conversion (2yr) | >70% | **99.67%** (FY26); FY25 164.33% | FCF/NI, latest 2 years | ✅ |
| Share issuance pattern | non-dilutive | **Net buybacks**, not dilutive — diluted avg shares fell 460.83M→417.26M (FY25→FY26), £150M buyback program, £294M repurchased since Sept-2023 (≈23% of issued share capital; WebSearch) | yfinance + WebSearch | ✅ |

**Result: 8/8 PASS.** One caveat shown transparently: ROIC only clears the >15% bar in the single most recent fiscal year (FY26 20.46%); FY23–25 (7.24%/8.81%/14.80%) were below or marginal. This is the basis for ruling out Fast-Grower/PEG eligibility below (Upgrade 3's "reliable, non-distorted 3+ year earnings base" requirement) — it is **not** treated as a Phase 01 failure, since the current-year figure clears the bar and the trend is a consistent multi-year improvement, not a one-off spike.

**Phase 01 PASSES → proceed to Phase 02.**

---

## 4. Rate Environment Gate

- **Step 1 — Earnings Yield Spread Test:** Forward PE = 8.127x (yfinance) → EY = 1/8.127 = **12.304%**. Spread = 12.304% − 4.483% = **+7.821pp** ≥ +1.5% → **no flag** (Step 1 = +0).
- **Step 2 — Rate Regime Modifier:** 10Y = 4.483%, in the 3.5–5% bracket → **+5**.
- **Combined Rate Gate modifier: +5.**

---

## 5. Phase 02 — Valuation Score

### EPS growth / PEG (Upgrade 3) eligibility check

EPS growth is nominally very high: FY24→25 +78.6%, FY25→26 +51.1%, 3yr CAGR +62.2% (raw), even higher tax-normalized. **Ruled NOT a qualifying Fast Grower** for PEG purposes:
1. FY23's effective tax rate was an anomalous **4.0%** vs. ~28–30% in FY24–26 — this distorts the earnings base the growth rate is measured from.
2. Net margin and ROIC only crossed Phase 01's >15% threshold in the single most recent fiscal year (FY26), not across a reliable, established 3+ year base — exactly the disqualifying pattern named in the 2026-06-20 PEG clarification ("recent IPO / recently-profitable / one-off-distorted EPS does NOT qualify").

**Decision: PEG's 15% weight is redistributed to EV/EBIT** (EV/EBIT → 40% total weight; FCF stays 40%; FwdPE stays 20%).

### Sub-scores

**FCF Yield (40% weight).**
Market Cap = 353,214,738 shares × 2.162 GBP = **763,650,264 GBP**.
FCF Yield = 79,547,000 / 763,650,264 = **10.417%**.
FCF_Score = clamp(100×(1 − 10.417/10), 0, 100) = **0.00**.

**EV/EBIT (40% weight, redistributed from PEG).**
yfinance's `enterpriseValue` field (1,026,069,120) did not reconcile with manually-built EV (gap ~60M GBP / ~6%; capital leases checked and ruled out as the cause — already fully included in Total Debt). Per the never-invent/never-trust-a-black-box rule, **EV was built transparently from live components**:
EV = (353,214,738 shares × 2.162 GBP) + Total Debt 261,946,000 − Cash 59,703,000 = **965,893,264 GBP**.
EV/EBIT = 965,893,264 / 126,429,000 = **7.640x**.
EV/EBIT_Score = clamp((7.640−12)/23×100, 0, 100) = **0.00**.

**Forward PE + Historical PE Modifier (20% weight).**
Forward PE (yfinance) = **8.127x**. No 5yr PE history reconstructable (see §2 data gap) → **no-history fallback applies**: FwdPE_Score = **50.0** (neutral, flagged).

**PEG (15% weight):** N/A — redistributed to EV/EBIT per above.

### Raw weighted score

| Sub-score | Weight | Score | Weighted |
|---|---|---|---|
| FCF Yield | 40% | 0.00 | 0.00 |
| EV/EBIT | 40% | 0.00 | 0.00 |
| Forward PE | 20% | 50.00 | 10.00 |
| **Raw weighted score** | | | **10.00** |

### Modifiers

**Rate Gate modifier: +5** (from §4).

**Upside/Downside (Expected-Return) Modifier** — see fair value derivation in §6 first. Summary:
- Gap to blended FV = (337.3/216.2) − 1 = **+56.01%**.
- Catalyst window = 2.0 years (GBR platform/FY2027–28 clarity) → annualized gap = **28.01%/yr**.
- Intrinsic growth = **11.5%/yr** (midpoint of FY2027 guided adjusted-EBITDA growth 10–13%; revenue itself is guided flat, so EBITDA growth is the cleaner intrinsic-growth proxy here).
- Shareholder yield = 0% dividend + **9.46%** net buyback yield (diluted avg shares 460.83M→417.26M, FY25→FY26) = **9.46%**.
- **E = 28.01 + 11.5 + 9.46 = 48.97%**. H = 10%. E ≥ H → uncapped M = −15×clamp((48.97−10)/15, 0, 1) = **−15.00** (hits the floor).
- **Guardrail 1 applied — capped at −5.0.** Rationale: although the nominal 2.0yr catalyst window is inside the 18–24mo guardrail band, the GBR catalyst's timing is demonstrably unreliable in practice — the very news event triggering this session *is* a fresh delay announcement, layered on a pre-existing, independent UBS note flagging GBR-cannibalization-risk uncertainty (WebSearch). A catalyst that keeps slipping does not meet the spirit of "a documented, specific event expected to close the gap" (Rule 10) reliably enough to license the full −15. This is a judgment call, shown transparently rather than hidden in the number.

**Final Score = 10.00 (raw) + 5 (Rate Gate) − 5.0 (Upside/Downside, guardrail-capped) = 10.0.**

Per the score-boundary rule (round to nearest 0.1, ties round up): **Final Score = 10.0.**

---

## 6. Fair Value Derivation

### DCF (3-stage; WebSearch-informed assumptions reflecting FY2027 guidance of essentially flat revenue, £440–455M vs FY26's £452.7M, and UBS's GBR-cannibalization-risk note)

FCF0 = 79,547,000 GBP. Shares = 353,214,738. Net debt = 167,426,000 GBP.

| Scenario | Stage 1 (yrs 1–5) | Stage 2 fade | Terminal | WACC | FV/share |
|---|---|---|---|---|---|
| Bull (25%) | 9% | 7%→3% | 2.5% | 8.0% (GBR delayed further) | 560.5 GBX |
| Base (50%) | 3% | 1.5% | 2.0% | 8.5% | 325.2 GBX |
| Bear (25%) | −3% | −2%→0% | 1.5% | 9.5% (GBR launches; Trainline retains partial retailer role per WebSearch) | 171.5 GBX |

**PW Fair Value (DCF)** = 0.25×560.5 + 0.50×325.2 + 0.25×171.5 = **345.6 GBX**.

### Multiples (Rule 5 caveat: peer set is 30–150x Trainline's market cap — no peer within ±50% revenue band; closest true peers e.g. Omio are private. A 20% discount is applied to both multiples-derived figures to reflect this comp-quality/scale mismatch.)

- EV/EBITDA: peers BKNG 13.13x / EXPE 11.20x / MMYT 28.22x / TRIP 12.22x (TCOM excluded — negative EV/EBITDA) → median **12.6725x** → implied FV 552.6 GBX → discounted 20% → **442.1 GBX**.
- Forward PE: peers median 10.4296x × forward EPS 0.26552 GBP = 276.9 GBX → discounted 20% → **221.5 GBX**.
- **Multiples-Based FV = average(442.1, 221.5) = 331.8 GBX.**

### Blended Fair Value (Rule 7: 40% DCF / 60% Multiples)

**Blended FV = 0.40×345.6 + 0.60×331.8 = 337.3 GBX.**

### Sanity check

13-analyst consensus (WebSearch): target mean 351.46 GBX / median 350.0 GBX → implies +61.9–62.6% upside from 216.2 GBX. The independently-derived 337.3 GBX (+56.01% upside) lands within ~5% of consensus — cross-validates the conservative, WebSearch-grounded approach rather than overshooting it.

---

## 7. Final Score + Action Recommendation

**Final Score: 10.0 → 0.0–29.9 band → BUY, Full position 6–8%.**

---

## 8. Order Setup

- **Fair Value (blended):** 337.3 GBX
- **Margin of Safety:** 20% (top of the 15–20% range for this score band — chosen given the weak peer-comp set and the live regulatory/political overhang)
- **Buy Price** = 337.3 × 0.80 = **269.84 GBX**
- Live price (216.2 GBX) is already **below** the buy price → **enter now** at the live price, no limit order needed to wait for a better entry.
- **Sell Target (primary, base case):** 337.3 GBX
- **Bull-Case Trim Target:** 560.5 × 0.90 = 504.4 GBX
- **Stop Loss:** chose 25% max acceptable loss (top of the 20–25% range for this score band, given political-risk volatility wider than the stock's own beta of 0.391 alone would suggest) = 269.84 × 0.75 = **202.38 GBX** (above the 52-week low of 178.0 GBX, so not already breached)
- **R/R sensitivity across the permitted stop range** (entry = live price 216.2):

| Max loss % | Stop Loss (GBX) | R/R |
|---|---|---|
| 20% (degenerate — stop ≈ buy price, not entry) | 215.84 | ~336:1 (artifact, not meaningful — flagged, not used) |
| 22.5% | 209.13 | 17.04:1 |
| 25% (chosen) | 202.38 | **8.74:1** |

R/R = (337.3 − 216.2) / (216.2 − 202.38) = 121.1 / 13.82 = **8.74:1** — clears the 2:1 minimum by a wide margin. (The 20% figure is a mechanical artifact of the buy price sitting almost exactly at the stop threshold when MoS is large and price is already below FV; the 25% figure is the representative, decision-relevant R/R.)

- **Position Sizing:**
  - Portfolio value: $55,813.07 (IBKR $40,689.53 + Freedom24 $15,123.54, per `holdings.md`).
  - Risk-based: Max $ risk = 1.5% × $55,813.07 = $837.20. Entry = $2.8688 USD/share, Stop = 202.38 GBX = 2.0238 GBP = $2.6850 USD/share. Risk/share = $0.1838. Shares = $837.20/$0.1838 ≈ 4,555 shares → ≈ $13,068.72 (23.42% of portfolio) — **far exceeds caps**.
  - Allocation cap for Score 0.0–29.9: 6–8% of portfolio = $3,348.78–$4,465.05.
  - **Position Size = min(risk-based, allocation cap) = $4,465.05 (8% of portfolio, ≈1,556 shares at $2.8688/share).**
  - Cross-check vs. the hard 15% single-position cap (Upgrade 7): $8,371.96 — $4,465.05 is well under. **PASS.**

**Recommendation: BUY — full 6–8% position, enter now at the live price (no need to wait for a pullback to the formal buy price, since price is already below it). Use a GTC stop at 202.38 GBX (25% max loss) and a primary sell target of 337.3 GBX, with a bull-case trim trigger at 504.4 GBX.**

This recommendation is **not executed** by this session — trade execution remains exclusively human per the framework's hard constraints; this session is score/recommendation only.

---

## 9. Portfolio Rebalancing Summary

N/A — TRN is not currently held; this is a new-position evaluation, not a rebalance.

---

## 10. Next Review Trigger

- **Mandatory:** Trainline's FY2027 interim/H1 results (next scheduled report) and any further news on the GBR platform timeline (the precise event class that triggered this session) — Rule 9.
- Any GBR-related announcement in either direction (further delay, concrete platform launch date, confirmation/denial of Trainline's continuing retailer role).
- >15% unexplained price move from 216.2 GBX (Rule 9).
- Standard Rule 9 triggers: guidance revision, management change, M&A.
- If revisited and the comp set still cannot be expanded past the four distant peers used here, that remains an open Rule 5 caveat worth flagging again (not necessarily blocking).

---

## Glossary

- **52-week range** — see definition in [glossary.md](../framework/glossary.md).
- **CAGR** — Compound Annual Growth Rate.
- **CapEx** — Capital Expenditure.
- **D&A** — Depreciation & Amortization.
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
- **GTC (Good-Til-Cancelled)** — an order left open until filled or cancelled.
- **MoS (Margin of Safety)** — discount below fair value used for the buy price.
- **Net Debt/EBITDA** — leverage ratio; this framework's balance-sheet-risk gate.
- **NOPAT** — Net Operating Profit After Tax (EBIT × (1 − tax rate)) — used to compute ROIC.
- **PE (Price-to-Earnings) ratio**, **PEG ratio** — standard valuation multiples; PEG = PE ÷ growth rate.
- **PW (Probability-Weighted) Fair Value** — 25% bull + 50% base + 25% bear blended estimate.
- **R/R (Risk/Reward ratio)** — expected gain ÷ expected loss on a trade; 2:1 minimum required.
- **Rate Environment Gate / Rate Regime Modifier** — the mandatory pre-score interest-rate check.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — always fetch a live price before any valuation work.
- **Rule 5** — comparables-set quality requirement (peers within ±50% revenue scale, 5 minimum).
- **Rule 7** — Probability-Weighted (bull/base/bear) fair value blending.
- **Rule 9** — fundamental events that force an immediate re-score.
- **Rule 10** — catalyst + timeline requirement for crediting large expected upside.
- **Shareholder yield** — dividend yield + net buyback yield.
- **Upside/Downside Modifier (Expected-Return Modifier)** — the ±15 additive score adjustment based on expected annual return.
- **WACC** — Weighted Average Cost of Capital; the DCF discount rate.

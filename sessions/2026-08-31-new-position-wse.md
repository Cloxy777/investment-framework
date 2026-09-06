# NEW POSITION (confirmation re-run) — Wise Group plc (Nasdaq: WSE / LSE secondary: WISE) — 2026-08-31

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, automated/unattended run)
**Date:** 31 Aug 2026
**10Y US Treasury Yield:** ~4.72% (TradingEconomics, "held steady at 4.72%" 2026-08-31; intraday touched 4.75% — "highest since January 2025" per Bloomberg — a genuine macro move, but still inside the 3.5–5% Rate Regime bracket, see §3)
**WSE portfolio weight:** 0% — not held, no row in [holdings.md](../portfolio/holdings.md)
**Prior coverage — important correction to this run's brief:** the orchestrating brief for this run assumed the last WSE evaluation was 2026-06-26 (Phase 01 FAIL, old binary gate) and pointed at `watchlist/not-in-portfolio/WSE/WSE-2026-06-26.md`. **That assumption is stale.** `git fetch origin main` at the start of this session surfaced a materially more recent evaluation not visible on this session's starting branch: **[sessions/2026-08-27-new-position-wise.md](2026-08-27-new-position-wise.md)** (PR #647, merged), filed under `watchlist/not-in-portfolio/WISE/WISE-2026-08-27.md` — only **4 days** before this run, triggered by the *same* Telegram channel (`bolshegold`) reporting essentially the *same* underlying facts (OCC national-trust-charter denial, Brussels AML investigation, securities class action). That session independently verified all of it, computed a full Quality/Valuation/Composite score under the current (2026-06-29) methodology, and concluded **WATCHLIST ONLY** (Composite 44.6, R/R gate fails). This session's job is therefore **not** a first-principles re-derivation but an honest check: *has anything material changed in the 4 days since 2026-08-27?* See §0 and §7.

**Repo-hygiene flag (not fixed unilaterally, noted for a human/next session):** WSE and WISE are the same company (Nasdaq primary ticker **WSE**, LSE secondary ticker **WISE**), but the watchlist now has *two* separate ticker folders — `not-in-portfolio/WSE/` (stale, last touched 2026-06-26, Phase 01 FAIL under the old binary gate) and `not-in-portfolio/WISE/` (current, 2026-08-27, full Quality/Composite score). `portfolio/snapshots/telegram-watch.md` already links to the `WISE/` path, so this session treats **`WISE/` as canonical** and updates it, while adding a short pointer note to the old `WSE/` file so it doesn't read as an orphaned dead-end. Consolidating the two folders under one canonical ticker name is left to a future session/human — out of scope to do safely and correctly inside this unattended run.

**Sector:** Financial Technology — cross-border consumer/business money transfer and payments infrastructure

---

## 0. Trigger — Telegram post and independent verification

**Source:** `t.me/bolshegold`, post `bolshegold/10062` (2026-08-31T14:50:01 UTC, a forwarded post/image). Transcribed claim: Wise is "under criminal investigation for money laundering," Brussels prosecutors investigating >€500M through customer accounts "with alleged links to fraud, corruption, and drug trafficking," the case "nearing completion... preparing to refer it to criminal court," OCC "denied Wise US a national trust bank license" in July, "multiple investor lawsuits," and "shares dropped more than 20% on the news." Per this framework's non-negotiable rule, **none of this post text is used as financial data below** — every claim is checked independently.

**Independent verification, claim by claim (WebSearch, primary/wire sources, not the Telegram post):**

| Claim | Independently verified? | What the record actually shows |
|---|---|---|
| Brussels AML criminal investigation, >€500M, fraud/corruption/drug-trafficking links | **Confirmed — but not new.** Same status as both 2026-06-26 and 2026-08-27. | Reuters/TBIJ/Euronews/American Banker (dated **2026-06-01**, the original report): Brussels prosecutors investigating Wise Europe SA over >€500M in flagged transactions, "at an advanced stage... finalizing a direct summons" to send the case to criminal court, "no charges have been filed and no findings have been formally communicated to Wise." A fresh search today (2026-08-31, queries for July/August/September updates) surfaces **no new statement, no filed charges, no referral** — the same June 1 "advanced stage / finalizing" language is what every subsequent article (including this week's law-firm press releases) still cites. **This is 3-month-old news being recirculated, not an escalation.** |
| OCC denied Wise US a national trust bank license, "in July" | **Confirmed — but not new as of this session.** Already known and fully evaluated in the 2026-08-27 session, 4 days ago. | OCC's own decision document (Corporate Decision #1381, occ.gov) + BankingDive/American Banker/GuruFocus/StockTitan SEC 6-K coverage: OCC denied Wise's **application** for a national trust bank charter on **2026-07-24**, citing AML-control and management-experience deficiencies. This is a **new-charter denial**, not a loss of an existing license — Wise continues operating in the US under its existing state money-transmission licenses, unaffected. |
| "Multiple investor lawsuits" | **Confirmed — but not new.** Same open litigation already tracked as of 2026-08-27. | Numerous law firms (Bronstein Gewirtz, Robbins LLP, SBS Law, Levi & Korsinsky, Glancy Prongay, Pomerantz, Bragar Eagel) have filed/announced a federal securities class action, class period **2026-05-11 to 2026-07-23**, alleging Wise understated AML/regulatory risk. **Lead-plaintiff deadline: 2026-09-29** — still open, unresolved. Several of the press releases found today are dated **2026-08-31 itself** (e.g. GlobeNewswire 3353568, 3353485, 3353429) — but these are routine "reminder" solicitations from law firms drumming up lead-plaintiff clients for the *same, already-known* suit, not new legal developments. |
| "Shares dropped more than 20% on the news" | **Not confirmed as stated — a mischaracterization.** | The securities-complaint press releases themselves give the actual mechanics: **-16.05%** over June 1–3, 2026 (the AML-investigation news) and a **separate -6.2%** move on July 24, 2026 (the OCC-denial news) — two distinct events, months apart, neither one a single >20% move. Cumulative decline from the post-listing 52-week high ($17.47, reached before either event) to today's price ($13.04) is **-25.4%**, but that is a multi-month drift across two separate catalysts plus general trading, not a single "drop on the news" event as the post implies. |

**Net verdict: nothing in this Telegram post is materially new relative to the framework's own state of knowledge 4 days ago (2026-08-27).** Every fact in the post was already independently verified and fully scored in that session. This run exists to honestly check for drift since then, not to re-discover already-known information — see §7.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used (WSE, Nasdaq)** | **$13.04** | IBKR live snapshot, contract 881566839, intraday 2026-08-31 (`is_close: false`) — today's session: open $12.97/$12.92 (two consecutive snapshots), low $12.92, high $13.09, volume ~255K shares |
| Cross-check | $13.04 | Yahoo Finance `quoteSummary` (`regularMarketPrice`), direct API pull, same session — **exact match** |
| Bid/Ask (IBKR) | $13.02 / $13.06 | Tight, liquid spread |
| 52-week range | $10.36 – $17.47 | IBKR + Yahoo, consistent |
| Analyst consensus (bull-case sanity check, not used in FV) | Mean **$17.16**, median $16.90, 13 analysts | Yahoo `financialData` |
| Shares outstanding | 983,729,421 | Yahoo `defaultKeyStatistics` — **identical to the 2026-08-27 session's figure**, confirming no new share issuance/buyback-driven count change of note |
| Market cap | **$12,828.0M** (983.729M × $13.04) | Computed; cross-checks Yahoo's own `marketCap` field ($12,827.8M) to <0.01% |

**vs. 2026-08-27's $13.23:** price is down **-1.44%** over 4 days — well below the 15% "unexplained move" trigger, and explained (to the extent it needs explaining at all) by the broader macro move in long rates this week (10Y UST briefly topped 4.75%, "highest since January 2025" — Bloomberg), not by any Wise-specific news.

---

## 2. Quality Score — Phase 01 (methodology version 2026-06-29) — carried forward, verified unchanged

**No new fiscal disclosure exists to change this score.** Wise's FY2026 Form 20-F (filed 2026-06-25) remains the latest annual filing; Q1 FY2027 (reported 2026-07-16, next full update ~November 2026) doesn't restate FY2026 annuals. The only SEC filings found between 2026-08-27 and today are two routine 6-Ks disclosing ongoing share buyback executions (Aug 3–7 and Aug 10–14, part of the previously-known £405M/~$540M buyback program) and a debt-guarantor accession to Wise's existing £2bn EMTN programme — administrative, not a Rule 9 fundamental-event trigger, and not a change to any Quality Score input.

Given that, this session **independently re-verifies the arithmetic** of the 2026-08-27 session's Quality Score rather than re-deriving it from scratch off identical inputs (which would just reproduce the same numbers):

```
NetMargin_Component = clamp((19.926/30)×100) = 66.419
ROIC_Component       = clamp((19.738/30)×100) = 65.794    [NOPAT 446.07 / Invested Capital 2,259.9]
Profitability_Score  = (66.419+65.794)/2 = 66.107          (no FCF-positivity cap — positive every year on record)

GrossMargin_Score = clamp((78.924/80)×100) = 98.655        [Gross profit = Net rev 2,502.8 − Transaction exp 513.6 − Transaction/credit losses 13.9 = 1,975.3]

Revenue 3yr CAGR = (2,502.8/1,197.0)^(1/3) − 1 = 27.873%   [FY2023 $1,197M → FY2026 $2,502.8M, stockanalysis.com USD series, cross-checked against SEC XBRL for FY24-26]
Growth_Score = clamp((27.873/25)×100) = 100.0 (capped) + TAM-expansion modifier (documented: $43T addressable opportunity per Wise IR materials; FY26 cross-border volume +31% YoY vs. ~7.9% CAGR industry-wide — Grand View Research; Q1 FY27 growth accelerated further to +25% YoY) — capped, no numeric effect at ceiling. Growth_Score = 100.0

Net Debt/EBITDA = 334.7 / 605.1 = 0.553×   [no-cash-netting convention — customer float too large to split cleanly, conservative choice]
BalanceSheet_Score = clamp(100×(1−0.553/4)) = 86.172

Moat_Score = (3/5)×100 = 60.0
  TRUE: Market share (Wise passed Western Union's cross-border volume in 2022 — Bloomberg Second Measure;
        FY26 volume growth 31% vs. ~7.9% market CAGR — continued share gain)
  FALSE: Brand premium (take rate has been CUT 0.67%→0.52%, FY24→FY26 — the opposite of pricing power)
  TRUE: Network effect (direct connections to 8 domestic payment systems; internal netting deepens with volume)
  TRUE: Switching costs (Wise Platform — Morgan Stanley, Standard Chartered, Nubank, Monzo integrated —
        caveated: applies to the B2B/Platform segment, not the low-switching-friction retail product)
  FALSE: Scale cost advantage (no cost-per-unit figure benchmarked against a specific smaller competitor found)
  [Sensitivity, carried forward from 2026-08-27: 2/5 → Quality Score 80.3 (still passes); 1/5 → 77.3 (fails).
   Genuinely close, moat-signal-sensitive — flagged, not smoothed over.]

FCF/NI Ratio (FY2026, own-funds FCF construction) = 532.8/498.7 = 106.838%
FCFQuality_Score = clamp(((1.06838−0.40)/0.60)×100) = 100.0 (capped)

Hard disqualifiers (re-checked): FCF/NI <70% 2+ yrs — NO (106.8%, 97.4%, both >70%). Net Debt/EBITDA over threshold — NO (0.55× vs 2.5×). Not FCF-positive 3+ yrs — NO (positive every year on record). No disqualifier fires.

Quality Score = (66.107×0.25)+(98.655×0.15)+(100.0×0.20)+(86.172×0.15)+(60.0×0.15)+(100.0×0.10)
              = 16.527+14.798+20.000+12.926+9.000+10.000 = 83.251 → 83.3
```

**Quality Score = 83.3/100.0 — clears the 80.0+ gate**, confirmed unchanged from 2026-08-27 (same fundamentals, independently re-verified arithmetic matches to 0.001). Proceeding to Phase 02 with a fresh price.

---

## 3. Rate Environment Gate

```
Forward PE = $13.04 / $0.694 (Yahoo forward EPS, direct API pull) = 18.789×
Earnings Yield = 1/18.789 = 5.322%
10Y UST = 4.72% (TradingEconomics, 2026-08-31 — flagging the intraday high of 4.75% this week, "highest since Jan 2025," a real macro move worth watching, but the bracket outcome below is unaffected either way)
Spread = 5.322% − 4.72% = +0.602pp   (< +1.5% threshold → Step 1 flag, +5)
```

10Y yield 4.72% (or even the intraday 4.75%) sits in the **3.5–5% bracket → Step 2 Rate Regime Modifier = +5**. **Combined Rate Gate adjustment: +10** — unchanged from 2026-08-27 despite this week's rate move, because both readings stay inside the same bracket.

---

## 4. Valuation Score — Phase 02 (fresh price, fundamentals carried forward)

### 4.1 PEG / Fast-Grower eligibility
**Not applicable** — FY26 net income fell 9.4% YoY, decisively failing the Fast-Grower EPS-growth test. PEG's 15% weight redistributes to EV/EBIT (→ 40%), unchanged from 2026-08-27.

### 4.2 Sub-scores (recomputed at today's price/market cap)

```
FCF Yield (40%): FCF (own-funds, FY26, unchanged) $532.8M / Market Cap $12,828.0M = 4.153%
  FCF_Score = clamp(100×(1−4.153/10)) = 58.47

EV/EBIT (40%, PEG redistributed): EV = 12,828.0 + 334.7 (debt, no cash netting) = 13,162.7
  EV/EBIT = 13,162.7 / 590.7 = 22.284×
  EV/EBIT_Score = clamp((22.284−12)/23×100) = 44.71

Forward PE (20%): no-history fallback, unchanged reasoning (three reporting-regime discontinuities —
  legacy IFRS → "underlying basis" IFRS → US-GAAP post-Nasdaq-listing — make a reconstructed 5yr
  trailing-PE series unreliable). FwdPE_Score = 50.0 (neutral, flagged)
```

```
Raw weighted score = (58.47×0.40) + (44.71×0.40) + (50.0×0.20) = 23.388+17.884+10.000 = 51.272
Plus Rate Gate (+10) = 61.272 before the Upside/Downside Modifier
```

### 4.3 Upside/Downside Modifier

**DCF and multiples-based fair value carried forward unchanged from 2026-08-27** — no fundamental input (financials, guidance, peer multiples, WACC components other than a 0.07pp risk-free tick that doesn't move the deliberately-above-CAPM 8.5% base WACC) has changed in 4 days. Re-running an identical DCF off identical inputs would reproduce the same $10.10/share PW Fair Value; only the **live price** and its dependent ratios are refreshed below, per Rule 0.

```
PW Fair Value = $10.10/share (carried forward: 0.25×$13.858 Bull + 0.50×$9.550 Base + 0.25×$7.434 Bear,
  40% DCF/60% multiples blend — full derivation in [2026-08-27 session §4.3](2026-08-27-new-position-wise.md#43-upsidedownside-modifier--full-calc-shown))

Gap Upside % = (10.10/13.04) − 1 = −22.55%
Catalyst window: still none identified within 18–24mo (OCC re-application timeline unknown, Brussels
  outcome unknown, litigation runs at least to 2026-09-29 and likely beyond) — 2yr default window (Rule 10)
Annualized gap = −22.55%/2 = −11.28%/yr
Intrinsic growth = +2.774%/yr (Stage-1 FCF CAGR, carried forward — margin-compression-aware base case)
Shareholder yield = FY26 buybacks $473.4M / today's market cap $12,828.0M = +3.691%
  (Q1 FY27 buyback continuation confirmed via two routine 6-Ks this session, Aug 3-7 and Aug 10-14 —
  doesn't change the FY26-anchored numerator used here)

E = −11.28 + 2.774 + 3.691 = −4.815%
E < 0 → M = 5 + 10×clamp((−E)/10pp, 0, 1) = 5 + 10×clamp(4.815/10, 0, 1) = 5 + 4.815 = 9.815
```

### 4.4 Final Valuation Score

```
Valuation Score = 51.272 (raw) + 10 (Rate Gate) + 9.815 (Upside/Downside Modifier)
                = 71.087 → rounds to 71.1
```

(vs. 72.5 on 2026-08-27 — the ~1.4pp improvement is mechanical: a slightly lower live price makes every cheapness-oriented sub-score and the expected-return gap slightly more attractive, exactly as it should.)

---

## 5. Composite Score

```
Composite Score = 0.50×(100 − 83.3) + 0.50×71.1 = 8.35 + 35.55 = 43.90 → 43.9
```

**Composite Score = 43.9/100.0** — Per the Action Table, 30.0–49.9 mechanically maps to **"BUY — Standard position 3–5%."** As on 2026-08-27, this is shown faithfully, but §6 explains why it isn't acted on. Essentially unchanged from the 08-27 reading of 44.6 (a 0.7-point drift entirely explained by the 1.4% price move — not a new fact about the business).

---

## 6. Fair Value & Order Setup

```
Blended (PW) Fair Value = $10.10/share
MoS band (Score 30.0–49.9): 25–30%   |   Max Loss band: 25–30%
Sell Target = Fair Value = $10.10
```

| MoS | Buy Price | Max Loss | Stop Loss | R/R |
|---|---|---|---|---|
| 25% | $7.575 | 25% | $5.681 | 1.33:1 |
| 25% | $7.575 | 30% | $5.303 | 1.11:1 |
| 30% | $7.070 | 25% | $5.303 | **1.71:1 (best case)** |
| 30% | $7.070 | 30% | $4.949 | 1.43:1 |

**Every combination inside the prescribed grid falls short of the mandatory 2:1 minimum** — best case 1.71:1, essentially identical to 2026-08-27's 1.71:1 (the Buy Price/Stop Loss/Sell Target are all anchored to the unchanged $10.10 modeled Fair Value and the unchanged score-band percentages, not to today's live price — a lower live price alone doesn't fix this). Per fair-value-methodology.md Step 6: pass on the trade, don't set a limit order and wait. No position sized.

---

## 7. What actually changed vs. what didn't — direct answer to this run's mandate

This run was specifically tasked with resolving whether independently-verified research confirms a **material update** to the AML investigation, the OCC decision, the lawsuits, or the price, beyond what the framework already knew. Answering each directly:

- **AML "Next review trigger" (Brussels prosecutor's office inquiry resolution, formal charges, regulatory clearance):** **NOT triggered.** The investigation remains exactly where it was on 2026-06-01 (first reported), 2026-06-26, and 2026-08-27: "advanced stage... finalizing a direct summons," no charges filed, no outcome communicated to Wise. No escalation, no resolution, no formal referral found as of 2026-08-31.
- **OCC national trust bank charter denial:** **Confirmed as fact, but not new information to this framework** — it was independently verified and fully incorporated into the Quality/Valuation/Composite score 4 days ago, in the 2026-08-27 session. It is new only relative to the 2026-06-26 entry the orchestrating brief was (stale-)aware of.
- **Securities class-action lawsuits:** **Confirmed as fact, likewise not new** — same open suit, same 2026-09-29 lead-plaintiff deadline, already tracked since 2026-08-27. Today's several law-firm press releases are routine lead-plaintiff solicitations for the *existing* suit, not a new legal development.
- **">20% drop on the news":** **Not confirmed as a single event** — it conflates two separate, already-known moves (-16.05% Jun 1–3, -6.2% Jul 24) months apart. No fresh >15% unexplained move occurred around this post (price is -1.4% over the last 4 days).

**Net: this Telegram post added zero new verified information to the framework's existing WSE/WISE record.** It re-surfaced a screenshot of facts the framework had already independently verified and fully scored 4 days prior.

---

## 8. Recommendation

# **WATCHLIST ONLY — do not enter. No change from 2026-08-27.**

Composite Score 43.9 mechanically qualifies for "BUY — Standard position 3–5%," but the mandatory Risk/Reward gate fails (best case 1.71:1 against a 2:1 minimum) across every combination of the prescribed Margin-of-Safety/Stop-Loss grid — unchanged from 4 days ago. The underlying business remains genuinely strong (Quality Score 83.3: FCF-positive every year on record, net-cash-adjusted balance sheet at 0.55× Net Debt/EBITDA, 27.9% 3yr revenue CAGR), but a live, unresolved regulatory/legal risk cluster (unresolved Brussels AML investigation, a denied OCC bank-charter application, an open securities class action through at least 2026-09-29) sits directly on top of a valuation this session's own DCF/multiples work reads as already fair-to-rich ($10.10 PW Fair Value vs. $13.04 live price), not cheap. **No position opened.**

**Next review trigger (unchanged from 2026-08-27):** (a) resolution, in either direction, of the Brussels AML investigation (formal charges filed, referral to criminal court, or a clearance/settlement); (b) any update on Wise's planned re-application for US bank/trust access (national trust bank re-filing, or a GENIUS Act stablecoin-framework filing); (c) the 2026-09-29 lead-plaintiff deadline and any subsequent securities-litigation development; (d) Wise's Q2 FY27 earnings (quarter ended 30 Sep 2026, expected ~November 2026) — specifically whether operating margin has begun stabilizing per FY27 guidance; (e) standard Rule 9 triggers (>15% unexplained price move, guidance revision, management change).

---

## 9. Glossary

*(Pulled from [glossary.md](../framework/glossary.md); all terms used below already exist there as of this session — no new terms to add.)*

| Term | Meaning |
|---|---|
| **AML (Anti-Money Laundering)** | Laws and internal controls to stop criminal proceeds moving through legitimate financial channels — the deficiency the OCC cited in denying Wise's charter application, and the subject of the Brussels criminal investigation. |
| **CAGR** | Compound Annual Growth Rate. |
| **Composite Score** | This framework's blend of Quality Score and Valuation Score (50/50, inverted for consistent orientation) — 0 = most attractive, 100 = least. |
| **DCF (Discounted Cash Flow)** | A valuation method estimating a company's worth as the present value of its projected future free cash flows. |
| **EBIT / EBITDA** | Operating profit, before/also-before depreciation & amortization. |
| **EV/EBIT** | Enterprise Value ÷ EBIT — a core cheapness sub-score in this framework. |
| **FCF (Free Cash Flow) / FCF Yield** | Cash generated after running the business; FCF ÷ market cap. |
| **Form 20-F / Form 6-K** | The annual/interim reports foreign private issuers file with the SEC — the international equivalents of a 10-K/8-K. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of its weighted score. |
| **Lead plaintiff (securities litigation)** | The court-appointed representative investor in a class-action lawsuit; a filing deadline to seek this role (here, 2026-09-29) is a standard early-litigation milestone, not a resolution of the case. |
| **Moat Signal** | This framework's five-point qualitative checklist (market share, brand premium, network effect, switching costs, scale cost advantage) feeding 15% of the Quality Score. |
| **National trust bank charter** | A federal bank charter (OCC-granted) letting a company operate as a nationally-chartered trust institution instead of relying on state money-transmission licenses; the OCC denied Wise's application for this on 2026-07-24. |
| **Net Debt/EBITDA** | Net debt ÷ EBITDA — this framework's primary balance-sheet-risk gate. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the ROIC numerator. |
| **OCC (Office of the Comptroller of the Currency)** | The US federal regulator that charters and supervises national banks and trust companies. |
| **PW (Probability-Weighted)** | The bull/base/bear scenario blend (25%/50%/25%) used to compute a single Fair Value estimate. |
| **Quality Score** | This framework's 0.0–100.0 score (higher = better) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss on a trade; this framework requires ≥2:1. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0** | Always fetch a live price first — never infer from multiples or stale data. |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **Upside/Downside Modifier** | An additive, bounded (±15) adjustment to the Valuation Score based on expected annual return vs. a 10% hurdle. |
| **WACC** | Weighted Average Cost of Capital — the discount rate used in a DCF. |

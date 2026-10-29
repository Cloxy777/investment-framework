# RESCORE — GOOG (Alphabet Inc., Class C) — 2026-10-29

**Task type:** RESCORE (mode `--both`)
**Date:** 29 Oct 2026
**Trigger:** Standard quarterly re-score — Alphabet reported Q3 FY2026 on 28 Oct 2026 after the close (Rule 9 earnings trigger). GOOG fell ~12% on the print.
**10Y US Treasury Yield:** 5.05% (Treasury par-curve close 28 Oct 2026, per 247wallst.com 29 Oct; prior close 4.99%; overnight 29 Oct dipped to 4.999% at 1:42 AM ET). **Knife-edge:** the bracket boundary is exactly 5.00%. I used the last official *close* (5.05%) → Step 2 = **+10**. At 4.999% Step 2 would be +5 and the Valuation Score would be **32.1** instead of 37.1 (script run, see §5). Same action either way.
**Rate Regime Modifier (Step 2):** +10 (10Y >5%) — up from +5 in the 3.5–5% bracket last session.
**Position:** 1 share, IBKR, 0.67% of portfolio (holdings.md, 2026-10-25 sync, pre-drop), avg cost $295.70.
**Last review:** 22 Jul 2026 (Valuation 64.2, Quality 71.4, Composite 46.4, HOLD).

*Plain-English note: GOOG = Alphabet Class C (no votes); GOOGL = Class A. Same economics, treated interchangeably.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$282.74** (bid 282.74 / ask 282.86) | IBKR `get_price_snapshot` (contract_id 208813720), 29 Oct 2026 regular session |
| Change vs prior close | −$39.15, **−12.16%** (prior close $321.89) | IBKR; Yahoo (`currentPrice` 282.22, `previousClose` 321.89) agrees |
| 52-week range | $270.87 – $404.23 | IBKR `misc_statistics` — price sits just above the 52-wk low |
| Analyst consensus PT | Yahoo mean $422.36 / median $427.50, range $340–$485, n=14 | **Mixed vintage** — post-earnings revisions not confirmed (no post-print target list found); treat as stale-ish |

---

## 2. The Earnings Release — Primary-Source Data

Source: Alphabet 8-K Ex 99.1, 28 Oct 2026 (fetched via SEC.gov). Call color: MarketBeat/Yahoo, Investing.com and FinanceFeeds coverage (secondary — labelled where used).

| Metric (US$M) | Q3 2025 | Q3 2026 | YoY |
|---|---|---|---|
| Revenue | 102,346 | 127,577 | +25% |
| — Google Search & other | 56,567 | 63,350 | **+12%** (was +17% in Q2) |
| — YouTube ads | 10,261 | 11,207 | +9% |
| — Google Services | 87,052 | 96,302 | +11% (was +15% in Q2) |
| — Google Cloud | 15,157 | 30,709 | **+103%** (TPU system sales "a meaningful contributor") |
| Operating income | 31,228 | 40,576 | +30% (margin 31.8% vs 30.5%) |
| Cloud segment op. income | 3,594 | 11,121 | margin 36.2% vs 23.7% |
| Other income (expense), net | +12,759 | **−8,221** | incl. equity-securities loss −8,664 |
| Net income | 34,979 | 26,468 | −24% |
| Diluted EPS (GAAP) | $2.87 | **$2.12** | consensus $3.02 |
| CapEx | 23,953 | **51,355** | +114% |
| Operating cash flow | 48,414 | 42,290 | −13% |
| FCF (OCF − CapEx) | +24,461 | **−9,065** | 2nd straight negative quarter |
| Stock-based comp | 6,368 | 8,630 | +36% |
| Buybacks | 11,504 | **0** | paused all of 2026 |

**Rule 6 normalisation.** The 8-K footnote states the $8.7B equity-securities loss (SpaceX stake mark-down per call coverage) *decreased* net income by **$6.7B** and diluted EPS by **$0.55**. Normalised Q3'26: NI = 26,468 + 6,700 = **$33,168M**; EPS = 2.12 + 0.55 = **$2.67** (matches yfinance "Reported EPS" 2.67; consensus was $3.02 → still a ~12% EPS miss on a clean basis, Alphabet's first top-and-bottom-line miss in ~4 years per CNBC).

**Why the stock fell (secondary sources, partly conflicting):** (1) clean EPS miss; (2) Search growth slowed 17%→12% — mgmt attributes it mostly to FX, retail (EU de-minimis end), media comps (World Cup in Q2) and lower AI Mode monetisation; FinanceFeeds attributes it to AI Mode. **Sources disagree; I did not treat it as proven structural** (§3c). (3) FCF −$9.1B vs −$2.7B expected. (4) 2026 CapEx guide held at $195–205B, but 2027 will "increase significantly" (no number); depreciation and DC costs rising; third-party compute capacity in Q4 pressures Cloud margin. Positives: Cloud backlog $561B (~55% recognised within 24 months), Gemini app 1B users.

**Balance sheet (30 Sep 2026):** cash+securities $265,098M; long-term debt $125,102M (+$28.7B notes in Q3); equity $677,549M; mandatory convertible preferred ~$19.0B face (carrying 18,023 inside APIC line); shares 12,294M (+0.5% QoQ via $12.4B ATM issuance; $27.6B ATM capacity left).

### TTM reassembly (Q4'25–Q3'26) = prior TTM (Q3'25–Q2'26, 2026-07-22 session) − Q3'25 + Q3'26

| Metric | Computation | TTM |
|---|---|---|
| Revenue | 445,866 − 102,346 + 127,577 | **471,097** |
| Gross profit | 271,517 − 60,977 + 76,158 | **286,698** (60.86%) |
| EBIT | 164,011 − 31,228 + 40,576 | **173,359** |
| D&A (depreciation line) | 25,237 − 5,611 + 8,369 | **27,995** |
| EBITDA | 173,359 + 27,995 | **201,354** |
| CapEx | release TTM table | **159,804** |
| OCF | release TTM table | **179,551** |
| FCF | release TTM table (matches) | **19,747** |
| SBC | 28,147 − 6,368 + 8,630 | **30,409** |
| Net income, Rule-6 normalised | 68,333 (Q4'25+Q1'26, carried) + 35,093 (Q2'26) + 33,168 (Q3'26) | **136,594** |

Cross-check: Q4'25 NI 34,455 (yfinance) + Q1'26 normalised 33,878 = 68,333 ✓ (Q1'26 EPS 2.76 ✓). Growth CapEx = (159,804 − 27,995)/159,804 = **82.5%** → Owner Earnings adjustment (Upgrade 1) still applies. Owner Earnings = NI normalised + D&A − maintenance-CapEx proxy (= D&A) = **$136,594M**.

Caveats: the carried Q3'25-inclusive prior TTM treated Q3'25 NI as raw (it held a $10.7B equity gain); that quarter has now rolled off, so the new TTM is cleaner than the last one. `fetch_fundamentals` vendor TTM fields (FCF 53,273; NI 244B; ROIC 53%; EBITDA 173B) were **still pre-Q3** and distorted by the 2026 equity gains — not used for scoring.

### fetch_fundamentals output (pasted; market data live, financial-statement TTM stale)

```
Market Cap = 3,453,978,411,008 | EV = 3,833,054,625,792 (vendor, stale balance sheet) | Forward PE = 18.445
FCF Yield 1.542% (stale TTM) | EV/EBIT 12.712 (distorted: vendor EBIT) | Net Margin 54.771% (gain-distorted)
Gross Margin 60.896 | ROIC 53.278% (gain-distorted) | Revenue 3yr CAGR 12.512% | FCF positive 3yr+ = True
FCF/NI annual (oldest first) = [100.1%, 94.2%, 72.7%, 55.4%]
5yr PE avg/low/high = 24.613 / 18.181 / 35.452 (n=20 quarters)   [uses yfinance "Reported EPS" = normalised 2.76/2.85/2.67 — verified above]
SBC block: SBC/FCF 52.8% (stale TTM) | FCF yield after SBC 0.73% (stale)
Advisory flags: cycle_peak UNKNOWN | value_trap_candidate UNKNOWN
```

**Advisory block handling (no score effect):** `python -m scripts.scoring.flags_common --eps-now 19.16 --forward-pe 18.466 --eps-growth 27.7` → `cycle_peak UNKNOWN` (data gap: TTM GAAP EPS a year ago not obtainable — yfinance lacks Q1'25), `multiple_ceiling NONE` (fwd PE 18.5, growth 27.7%), `value_trap_candidate UNKNOWN` (data gap: trailing EPS growth). Judgement: cycle_peak is moot — headline GAAP EPS is gain-inflated, which is why everything here uses normalised EPS; value-trap does not fit (fwd PE 18.5 > 15 and consensus EPS growing +28% FY27). The SBC block *is* material and is addressed below (§3 hard disqualifier).

---

## 3. Quality Score

Inputs file built from §2 (see JSON fields in the script output). **Script run as-is:**

```
# FAILS GATE
Reason: SBC 30,409 is >= 100% of TTM FCF 19,747 (or FCF <= 0) with no documented one-off explanation
```

**This is a NEW hard disqualifier trip** (methodology 2026-10-12, SBC-as-a-cost): TTM SBC ($30.4B) now exceeds TTM FCF ($19.7B) because the AI CapEx ramp has pushed FCF down 63% vs the last TTM ($53.3B). It is not a one-off, so I did **not** waive it. Previous GOOG scores were all below 80 anyway (73.7 → 71.4), so the gate status is unchanged — but the failure is now a hard rule, not just a weak score.

**Reference arithmetic** (re-run with the SBC disqualifier waived *only* to display sub-scores — NOT a real waiver; labelled "REFERENCE ONLY" in the input):

```
Profitability: NetMargin 28.99% -> 96.63 ; ROIC 26.84% -> 89.47 ; score 93.05
  (NOPAT = 173,359 x (1-16.78%) = 144,269 [FY2025 clean tax rate, as prior sessions];
   Invested capital = 125,102 + 677,549 - 265,098 = 537,553)
Margins: GM 60.86% -> 76.08
Growth: 12.51% CAGR -> 50.04 ; +10 TAM (Cloud +103%, backlog $561B) -> 60.04 ; no deceleration deduction (see below)
Balance sheet: ND/EBITDA = (125,102-265,098)/201,354 = -0.695x -> 100.0
Moat: 3/5 TRUE -> 60.0 (share stable: StatCounter ~91% Aug 2026, 89.3–91.6% band since Jan 2024; network effect; switching costs - Gemini Enterprise ~90% of Fortune 100, $561B backlog)
FCF Quality: (FCF-SBC)/NI = (19,747-30,409)/136,594 = -7.8% -> 0.00
Quality = 23.26 + 11.41 + 12.01 + 15.00 + 9.00 + 0.00 = 70.68 -> 70.7
```

**Quality Score = 70.7 (reference) — FAILS the 80.0+ gate and also trips the SBC≥FCF hard disqualifier.** Down 0.7 from 71.4. A perfect 5/5 moat would add only +6 (→ ~76.7), so the gate verdict is not a moat judgement call.

**(c) Growth-deceleration call (judgement, disclosed):** Search +12% (from +17%) and Services +11% (from +15%) are real slowdowns in the core, but sources conflict on cause (FX/retail/media vs AI Mode monetisation) and total revenue *accelerated* to +25%. The sub-score requires "structural, cited" deceleration; the evidence is not clean enough, so **no −10 deduction**. If Q4 Search stays ≤12% ex-FX the deduction should be applied (−10 × 20% weight = −2.0 → Quality ~68.7).

**Phase 04 Quality Watch: escalates.** Third+ consecutive sub-80 print, now with a hard-rule trip. Existing holdings are not force-exited on quality alone; flagged for the user.

---

## 4. Rate Environment Gate

```
Forward PE = 282.74 / 15.311 = 18.466x  (forward EPS $15.311 = Yahoo NTM consensus, current vintage)
EY = 1/18.466 = 5.415%  ; Spread = 5.415 - 5.05 = +0.37pp  (< +1.5pp) -> Step 1 = +5
10Y 5.05% (>5%) -> Step 2 = +10
Combined Rate Modifier = +15
```

---

## 5. Valuation Score (script output, pasted)

Inputs: Owner Earnings yield = 136,594 / 3,476,006 = **3.93%** (market cap = $282.74 × 12,294M sh); EV = 3,476,006 + 19,000 (preferred) + 125,102 − 265,098 = **3,355,010**; EV/EBIT = 3,355,010 / 173,359 = **19.35×**; PEG not scored (kept off per the 2026-07-22 clean-earnings ruling: consensus growth rates still straddle the gain-distorted base) → 15% redistributed to EV/EBIT; 5yr PE 18.181 / 24.613 / 35.452.

Scenarios (same architecture as prior sessions; bull/bear assumptions held at last session's levels, base multiple = own normalised 5yr avg): Bull = 15.311×1.07×28.0 = **$458.73**; Base = 15.311×24.613 = **$376.86**; Bear = $13.00×19.0 = **$247.00** (held — Search deceleration/FCF/capex arguably strengthen it, but no basis for a new number).

```
FCF_Score = clamp(100x(1 - 3.9300/10)) = 60.700   [Owner Earnings basis]
EV/EBIT_Score = clamp((19.353 - 12)/23 x 100) = 31.970
FwdPE_Score (raw) = clamp((18.466 - 18.181)/(35.452 - 18.181) x 100) = 1.650
Deviation vs 5yr avg = (18.466 - 24.613)/24.613 = -24.975% -> Historical PE Modifier -10 -> FwdPE_Score 0.000
PEG: not applicable -> weights 40/40/20
Raw = 60.7x0.4 + 31.97x0.4 + 0x0.2 = 37.068
Rate Modifier = +15
PW Fair Value = 0.25x458.73 + 0.50x376.86 + 0.25x247.0 = 364.8625 ; Gap = +29.05% ; annualised (2yr) = 14.52%/yr
E = 14.52 + 12.0 (intrinsic growth) + 0.481 (div 0.311 + gross buyback 0.170; TTM buyback $5,899M = Q4'25 only) = 27.00%/yr
E >= 10% -> M = -15 x clamp((27.00-10)/15,0,1) = -15.000 (cap)
Final = 37.068 + 15 - 15.000 = 37.068 -> 37.1
```

# Valuation Score = 37.1 — down from 64.2 (price −17.5% vs last session's $342.61, plus forward EPS up ~4%, plus a wider rate modifier).

**Sensitivities (script re-runs):**
- 10Y = 4.999% (overnight print) → Rate Modifier +10 → **32.1**.
- Base FV at today's multiple instead of 5yr avg (base = $282.74) → modifier −8.7 → **43.4**.
All three versions sit in the sub-50 "Buy" valuation band; none changes the action.

---

## 6. Composite Score

`python -m scripts.scoring.composite_score --set quality_score=70.7 --set valuation_score=37.1` →
`Composite Score REFUSED — Quality Score 70.7 < 80.0 — fails the gate; Composite not computed for a company that hasn't cleared Phase 01`.

Reference only (hand calc, same convention used in holdings.md for gate-failers): 0.50×(100−70.7) + 0.50×37.1 = 14.65 + 18.55 = **33.2 — not actionable**.

---

## 7. Action Recommendation

**HOLD — keep the 1-share position. No add, no trim, no exit.**

- **No add:** numeric valuation is cheap (37.1), but quality fails the 80.0 gate *and* trips the SBC≥FCF hard disqualifier. The framework does not buy gate-failers; "cheap" here is partly the market pricing the same FCF/CapEx concerns, not a free lunch.
- **No trim:** Valuation 37.1 is far below the 70.0 trim bands; a price-only drop is never a trigger.
- **Exit triggers:** none fired. Operating income +30%, Cloud +103% with 36% margin, net cash ~$140B, ROIC 26.8%. Guidance: CapEx held (not cut/raised); no Rule 9 guidance revision. The −12% move is explained (earnings), not "unexplained >15%".
- **Order setup:** not applicable (HOLD).
- **Watch items:** (1) Search growth ex-FX in Q4 — would justify the −10 deceleration deduction; (2) FCF vs SBC — needs FCF > $30B TTM to clear the disqualifier, unlikely before 2027 given "significant" 2027 CapEx increase; (3) buyback resumption (none in 2026); (4) ATM dilution ($27.6B capacity left); (5) 10Y vs 5.00% line; (6) post-earnings analyst PT/EPS revisions (not confirmed here).

---

## 8. Next Review Trigger

Alphabet Q4/FY2026 earnings (~early Feb 2027; Yahoo shows 3 Feb 2027) — standard rescore within 3 business days. Earlier on a Rule 9 event (CapEx guide change, M&A, >15% unexplained move, evidence Search share loss is structural).

---

## Glossary

- **8-K**: SEC "current report" disclosing a material event; earnings releases ride on one as Exhibit 99.1.
- **ATM Program (At-the-Market)**: Company sells new shares into the open market over time via an agent.
- **Backlog**: Contracted future revenue not yet recognised.
- **CapEx**: Capital expenditure — spending on long-lived assets (data centers, servers).
- **Composite Score**: `0.50×(100−Quality)+0.50×Valuation`, only valid if Quality ≥ 80.0.
- **D&A**: Depreciation & amortisation.
- **EBIT / EBITDA**: Earnings before interest & taxes / plus depreciation & amortisation.
- **EPS**: Earnings per share. **GAAP**: official accounting rules.
- **EV / EV/EBIT**: Enterprise value (market cap + debt + preferred − cash) and its ratio to EBIT.
- **EY (Earnings Yield)**: 1 ÷ Forward PE; compared with the 10Y yield in the Rate Environment Gate.
- **FCF / FCF Yield**: Operating cash flow minus CapEx / divided by market cap.
- **Forward PE**: Price ÷ next-12-month expected EPS.
- **Hard disqualifier**: A rule that fails a company regardless of its weighted score.
- **Hurdle rate**: 10%/yr minimum expected return used by the Upside/Downside Modifier.
- **Mandatory convertible preferred**: Preferred stock that must convert into common shares by a set date.
- **Moat**: Durable competitive advantage.
- **NOPAT / ROIC**: After-tax operating profit / divided by invested capital.
- **Owner Earnings**: Net income + D&A − maintenance-only CapEx; used for growth-capex reinvestors like Alphabet (Upgrade 1).
- **Quality Score**: 0–100.0 grade of profitability, margins, growth, balance sheet, moat, FCF quality; 80.0+ is the gate.
- **Rate Environment Gate / Rate Regime Modifier**: Compares earnings yield with the 10Y Treasury and adds score points when rates are high.
- **Rule 0 / 6 / 9**: Fetch live price first / normalise one-offs before valuing / forced re-valuation on specific events.
- **SBC (Stock-Based Compensation)**: Pay in shares; this framework treats it as a real cost.
- **TTM**: Trailing twelve months.
- **Valuation Score**: 0–100.0 (lower = cheaper) combining FCF yield, EV/EBIT, Forward PE, rate and upside modifiers.

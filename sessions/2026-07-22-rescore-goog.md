# RESCORE — GOOG (Alphabet Inc., Class C) — 2026-07-22

**Task type:** RESCORE (mode `--both`)
**Date:** 22 Jul 2026
**Trigger:** Automated Telegram-scan (Routine 6) awareness that Alphabet reported Q2 FY2026 earnings today. Per this repo's Rule 0/non-negotiables, the triggering Telegram post text itself was **not** used as a financial input — every figure below is independently fetched fresh this session: IBKR live price/history, Alphabet's own official Q2 2026 earnings-release exhibit (8-K Exhibit 99.1, primary source), Yahoo Finance (cookie+crumb HTTP session — `yfinance`'s `curl_cffi` backend still fails with `SSLError: Recv failure: Connection reset by peer` through this environment's proxy, same known issue as prior sessions), stockanalysis.com, FRED/WebSearch for the 10Y yield, and WebSearch for search-market-share corroboration. This **is** a genuine Rule 9 "quarterly earnings release" trigger — the first real post-earnings rescore for GOOG since 2026-07-04/07-16 were price/news-driven refreshes with no new quarterly filing.
**10Y US Treasury Yield:** ~4.65% (TradingEconomics live read "4.66–4.67%" and a WebSearch aggregation both reporting 2026-07-22; FRED's own official `DGS10` series lags to 2026-07-20's 4.60% print — consistent with the observed short uptrend 4.60%→4.63%→~4.65% over the three days). Used 4.65% as the working figure.
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket, unchanged bracket vs. prior sessions)
**Current GOOG position:** 1 share, IBKR, 0.59% of portfolio (per `holdings.md`), avg cost $295.70
**Sector:** Communication Services — Internet, Search & Digital Advertising / Cloud
**Last review:** 16 Jul 2026 (Valuation Score 66.3, Quality Score 73.7 — fails 80.0+ gate, Composite 46.3, action HOLD). That session and the 07-04 session before it both explicitly flagged "next review trigger: Alphabet's Q2 FY2026 earnings release, expected ~28–29 Jul 2026" — the release actually landed earlier, **today, 22 Jul 2026**, ahead of that estimate.

*Plain-English note: GOOG = Alphabet's Class C share (no voting rights); GOOGL = Class A (voting). The economics are identical share-for-share and this framework treats them interchangeably for scoring.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$342.61** | IBKR `get_price_snapshot` (contract_id 208813720, NASDAQ), last trade ts ~20:22:31 UTC (4:22:31 PM EDT), cross-checked against Yahoo's live `postMarketPrice` (~$343.99 at a similar timestamp, ~0.4% apart — consistent). |
| ⚠️ **Volatility flag — this is a genuinely still-forming after-hours price, not a settled one** | Alphabet's Q2 2026 results (8-K Exhibit 99.1) were released at/just after the 4:00 PM ET close, and the earnings conference call begins **4:30 PM ET** — i.e. at the moment of this data pull, the market had the headline numbers but the call itself (where management typically gives forward commentary, including capex guidance) had not yet started. Five consecutive live snapshots taken over ~13 minutes swung from $339.80 → $344.13 → $342.74 → $342.67 → $342.61 (vs. the regular-session close of $341.91, itself down −1.24% on the day pre-earnings) — a ±1.3% range on thin after-hours liquidity. The figure used here ($342.61) is the freshest cross-validated read at time of analysis, not a claim that the price has stabilized; the next trading session's open is the more reliable "settled" read and is flagged in §10 as a follow-up check. | IBKR, Yahoo |
| Regular-session close (pre-earnings) | $341.91, −1.24% vs. prior close $346.19 | IBKR `get_price_history` + Yahoo `regularMarketPrice`/`regularMarketChangePercent` — both agree to the cent; also matches stockanalysis.com's independently-fetched $341.90/−1.24% figure used to trigger this rescore. |
| 52-week range | $188.27 – $404.47 (IBKR) | Unchanged band from recent sessions. |
| Analyst consensus PT | Yahoo: mean $430.07 / median $439.00 (range $340–$475, n=14) · stockanalysis.com: $430.07 mean, "Strong Buy" | **Pre-earnings vintage** — minutes-old post-earnings analyst target revisions are not yet reflected in any consensus aggregator; flagged, not treated as post-earnings-informed. |
| Prior session price | $346.19 (21 Jul 2026 close, per IBKR) / $353.74 (16 Jul 2026, last full rescore) | GOOG drifted down modestly into today's print, then the −1.24% regular-session move (pre-earnings, unrelated to results), then the volatile AH move described above. |

---

## 2. The Earnings Release — Primary-Source Data (Rule 0/Rule 6)

Alphabet's official Q2 2026 results (8-K Exhibit 99.1, "Alphabet Announces Second Quarter 2026 Results," MOUNTAIN VIEW, Calif. – July 22, 2026, fetched directly from Alphabet's own investor-relations CDN) are the primary source for everything in this section — not a vendor aggregator.

### ⚠️ Material finding — Q2 2026 GAAP results are dominated by a $98.0B one-off, non-cash gain (even larger than Q1 2026's $36.9B one)

Per the release: *"Other income reflected a net gain of $98.0 billion, primarily the result of net unrealized gains on our equity securities... Net income available to common stockholders increased 298% and EPS increased 294% to $9.11."* The footnote to the "Other Income (Expense), Net" table is explicit: *"the net effect of the gain on equity securities of $99.0 billion increased the provision for income tax, net income, and diluted net income per common share by $21.9 billion, $77.1 billion, and $6.26, respectively."*

This is Rule 6 ("Normalize Before You Value") territory — a second consecutive quarter (after Q1 2026's $36.9B gain, flagged 2026-07-04) where a large, non-cash, mark-to-market gain on Alphabet's equity-securities portfolio (likely reflecting its stakes in AI-related private companies) swamps the operating result. Stripped per the company's own disclosed reconciliation:

```
Normalized Net Income (Q2 2026) = GAAP Net Income $112,193M − $77,100M (disclosed gain effect) = $35,093M
Normalized Diluted EPS (Q2 2026) = $9.11 − $6.26 (disclosed EPS effect) = $2.85
```

**Read against consensus, this is a mixed print, not the blowout the headline $9.11 suggests:** normalized EPS $2.85 is *slightly below* Yahoo's pre-earnings consensus EPS estimate of $2.91 (`calendarEvents.earnings.earningsAverage`), even as revenue beat comfortably ($119.796B vs. $116.976B consensus, +2.4%) and Google Cloud accelerated sharply. **Operating income (true GAAP EBIT, unaffected by the equity-gain distortion) grew a clean 30% YoY to $40,770M, with operating margin expanding 2pp to 34%** — a genuinely strong, undistorted operating result, cited directly from the release rather than inferred.

### Q2 2026 headline operating results (unaffected by the one-off; in millions)

| Metric | Q2 2025 | Q2 2026 | YoY |
|---|---|---|---|
| Revenue | $96,428 | $119,796 | +24% (12th consecutive quarter of double-digit growth, per the release) |
| — Google Services | $82,543 | $94,540 | +15% |
| — Google Cloud | $13,624 | $24,768 | **+82%** (a sharp *acceleration* from Q1 2026's +63% YoY) |
| — Google Search & other | $54,190 | $63,271 | +17% |
| — YouTube ads | $9,796 | $11,055 | +13% |
| Operating income (EBIT) | $31,271 | $40,770 | +30% |
| Operating margin | 32% | 34% | +2pp |
| — Google Cloud segment operating income | $2,826 | $8,814 | +212% (Cloud segment margin ~35.6% vs. ~20.7% a year ago) |
| Total TAC (Traffic Acquisition Costs) | $14,705 | $16,179 | +10% |
| D&A (property & equipment) | $4,998 | $7,104 | +42% |
| CapEx | $22,446 | $44,924 | **+100%** |
| Operating cash flow | $27,747 | $39,069 | +41% |
| Free cash flow (company-defined, OCF − CapEx) | $5,301 | **−$5,855** | First negative quarterly FCF print flagged in this framework's GOOG history |

**Segment/qualitative color cited directly from the release, relevant to §5's Moat checklist:** "nearly 90% of the Fortune 100" now use Gemini Enterprise; the Gemini App has 950 million monthly active users; Gemini models process 22 billion API tokens per minute; Google Cloud's acceleration was "led by an increase in Google Cloud Platform (GCP) across enterprise AI Solutions and enterprise AI Infrastructure, as well as core GCP services."

### Balance sheet & capital structure — a genuinely new, material capital-raise event (Rule 9)

| Item | 31 Dec 2025 | 30 Jun 2026 | Source |
|---|---|---|---|
| Cash + marketable securities | $126,843M | **$242,474M** | Balance sheet |
| Long-term debt | $46,547M | **$98,165M** | Balance sheet |
| Mandatory convertible preferred stock (carrying value) | $0 | **$18,023M** | Balance sheet (19,000 shares × $1,000 liquidation preference ≈ $19.0B face value) |
| Total stockholders' equity | $415,265M | $640,480M | Balance sheet |
| Total shares outstanding (Class A+B+C) | 12,088M | **12,230M** (+114M, +0.94%) | Balance sheet |

The release explains why: *"In June 2026, we issued a combination of Class A stock and Class C stock and mandatory convertible preferred stock for aggregate net proceeds of $49.6 billion... Additionally, we entered into an [ATM Program] to sell up to $40.0 billion of our Class A stock and Class C stock... In the second quarter of 2026, we issued senior unsecured notes [new bonds not backed by specific collateral] for net proceeds of $20.3 billion."* Both explicitly earmarked for AI-infrastructure/compute capex. **Net effect: real, disclosed shareholder dilution (+0.94% share count) funding a real, disclosed jump in net cash position** (Net Debt swings from −$36.4B at Q1'26 to roughly −$125B to −$144B now, depending on preferred-stock treatment — see §5). **Also notable: Alphabet repurchased $0 of stock in both Q1 and Q2 2026** (vs. $28.3B in H1 2025) — buybacks are fully paused this half, redirecting capital to the raise-funded AI buildout instead. All cited directly from the cash-flow statement and press release, not inferred.

### TTM reassembly (Q3 2025 – Q2 2026), Rule-6-normalized

Q3'25/Q4'25/Q1'26 figures carried forward unchanged from the 2026-07-04/07-16 sessions (same primary-source basis, no restatement found); Q2'26 added fresh from today's release.

| Metric | TTM (Q2'25–Q1'26, last session) | TTM (Q3'25–Q2'26, **this session**) |
|---|---|---|
| Revenue | $422,499M | **$445,866M** |
| Gross Profit / Gross Margin | $255,053M / 60.37% | **$271,517M / 60.90%** |
| EBIT (GAAP operating income) | $157,435M | **$164,011M** |
| D&A | $23,131M | **$25,237M** |
| EBITDA | $180,566M | **$189,248M** |
| CapEx | $109,924M | **$132,402M** (matches Alphabet's own disclosed TTM CapEx in the release's FCF-reconciliation table exactly) |
| Operating cash flow | $174,353M | **$185,675M** (matches Alphabet's own disclosed TTM OCF exactly) |
| FCF (OCF − CapEx) | $64,429M | **$53,273M** (matches Alphabet's own disclosed TTM FCF exactly) |
| Net Income (GAAP, raw) | $160,208M | **$244,205M** |
| Net Income (Rule-6 normalized, one-off gains stripped) | $131,508M | **$138,405M** |

Growth CapEx test (Upgrade 1): maintenance-CapEx proxy = D&A TTM $25,237M; Growth CapEx = $132,402M − $25,237M = $107,165M = **80.9%** of total CapEx (up from 79.0% last session) — comfortably over the 30% threshold, so the Owner Earnings adjustment continues to apply, more so than ever.

```
Owner Earnings (TTM, normalized) = Net Income (normalized) $138,405M + D&A $25,237M − Maintenance CapEx (D&A proxy) $25,237M
                                  = $138,405M   (D&A and maintenance-CapEx proxy cancel exactly, as in every prior GOOG session)
```

No metric in this section was invented or estimated — every figure traces to Alphabet's own 8-K Exhibit 99.1 (fetched directly), a carried-forward and cited prior-session figure, or a disclosed reconciliation (the $99.0B/$21.9B/$77.1B/$6.26 gain-stripping figures Alphabet itself published).

---

## 3. Quality Score (Phase 01 gate) — recomputed with fresh Q2 2026 TTM data

**Hard disqualifier check:**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs *without growth-capex explanation*? | TTM 38.5% (normalized), well below 70% | disqualify unless growth-capex-explained | ✅ **PASS (carve-out applies)** — the growth-capex ramp is now even more extreme (80.9% of CapEx is growth capex, up from 79.0%), the strongest form of the documented Upgrade 1 carve-out yet. |
| Net Debt/EBITDA over threshold? | Net cash, deeply negative either way preferred stock is treated (see §5) | disqualify if >2.5× | ✅ PASS |
| FCF-positive 3+ consecutive years? | FY2023–2025 all positive; **TTM $53,273M still positive**, though the standalone Q2 2026 quarter was **FCF-negative (−$5,855M)** for the first time in this framework's GOOG history | disqualify if annual/TTM not positive | ✅ PASS on the annual/TTM basis this check is defined on — but the single-quarter negative print is flagged as a real, notable data point (record quarterly CapEx of $44.9B, +100% YoY) worth tracking, not itself a disqualifier. |

No hard disqualifier triggers. Proceeding to the weighted score.

### (a) Profitability (25% weight)
```
Net Margin (TTM, normalized) = $138,405M / $445,866M = 31.04% → NetMargin_Component = 100.0 (saturates)
NOPAT = EBIT $164,011M × (1 − 16.78%) = $136,490M   [tax rate: FY2025 clean annual effective rate, carried
                                                       forward unchanged — the cleanest available normalized
                                                       rate; this quarter's own residual tax-rate decomposition
                                                       (~11.7% on the ex-gain pretax base) is noisy/single-quarter
                                                       and not used, per the same discipline as prior sessions]
Net Invested Capital = Total Debt $98,165M + Total Equity $640,480M − Cash+STI $242,474M = $496,171M
ROIC = $136,490M / $496,171M = 27.51%   (down from 29.61% last session — see note below)
ROIC_Component = clamp((27.51/30)×100) = 91.70
Profitability_Score = (100.0 + 91.70) / 2 = 95.85
```
**Why ROIC fell despite EBIT growing:** the $496,171M invested-capital base jumped mainly because the $49.6B equity/preferred raise and $20.3B debt raise both sit (for now) as freshly-raised capital not yet deployed into revenue-generating assets — a temporary, mechanical dilution of ROIC from a real capital-structure event, not an operating deterioration. Worth re-checking once the raised capital is deployed into the AI buildout it was earmarked for.

### (b) Margins (15% weight)
```
Gross Margin (TTM) = $271,517M / $445,866M = 60.90% → GrossMargin_Score = clamp((60.90/80)×100) = 76.12
```
No structural-trend bonus (already far above the 40% threshold).

### (c) Growth (20% weight)
```
Revenue 3yr CAGR (FY2022 $282,836M → FY2025 $402,836M) = 12.51% → base Growth_Score = 50.04
```
(Unchanged basis — FY2025 remains the latest closed fiscal year; no new annual figure to recompute against.) TAM/pricing-power evidence **strengthened and freshly re-confirmed this session, primary-sourced**: Google Cloud revenue growth *accelerated* to +82% YoY in Q2 2026 (from +63% in Q1 2026), per Alphabet's own release — a materially stronger, more current data point than the 07-04 session's Statista-sourced figure. No decelerating-growth evidence (headline revenue growth itself accelerated to +24% YoY, the fastest in the 12-consecutive-quarter double-digit-growth streak the release cites).
```
Growth_Score = clamp(50.04 + 10) = 60.04
```

### (d) Balance Sheet (15% weight)
```
Net Debt/EBITDA = −144,309 / 189,248 = −0.76×   [Net Debt = Total Debt $98,165M − Cash+STI $242,474M,
                                                    per the framework's literal Total-Debt-based formula;
                                                    preferred stock excluded from this leverage ratio —
                                                    see the EV-treatment note in §5 for the separate, standard-
                                                    convention choice to include it in EV instead]
BalanceSheet_Score = clamp(100×(1 − (−0.76)/4)) = 100.0 (saturates — deep net cash either way preferred is treated)
```

### (e) Moat Signal (15% weight) — re-verified this session with fresh, primary-sourced evidence where available

| Signal | Marked | Status this session |
|---|---|---|
| Market share stable/growing | TRUE | **Freshly re-confirmed via WebSearch**: StatCounter's global search-referral share for Google reads 91.25% (June 2026), up from 89.5% (June 2025) — stable-to-growing on a fresher data point than the prior session's Apr/May 2026 read. Google Cloud's own infrastructure share continues rising (Cloud revenue +82% YoY this quarter, the fastest acceleration of the three hyperscalers cited in prior sessions — no contrary evidence found this quarter that this has reversed). |
| Brand premium | FALSE | Unchanged gap (no cited pricing-power/price-increase-without-volume-loss evidence located this session either). |
| Network effect | TRUE | Unchanged mechanism (YouTube + Search). |
| Switching costs | TRUE | Unchanged mechanism (Workspace/Cloud integration depth), **now reinforced by a new, concrete, primary-sourced enterprise-adoption data point**: "nearly 90% of the Fortune 100" using Gemini Enterprise, per today's release — evidence of deepening enterprise integration/lock-in, not just a bare mechanism claim. |
| Scale cost advantage | FALSE | Unchanged gap (still no cited cost-per-unit/cost-per-query comparison vs. smaller competitors). |

```
Moat_Score = (3/5) × 100 = 60.0
```
**Robustness check, updated:** even marking **all 5** signals TRUE (Moat_Score = 100.0), Quality Score would reach only **77.4** — still below the 80.0 gate (vs. the 07-04 session's near-miss of 79.7 under the same hypothetical). The gate failure is now **more robustly driven by Profitability/FCF-Quality erosion, not remotely sensitive to the Moat judgment call.**

### (f) FCF Quality (10% weight)
```
FCF/NI (TTM, normalized) = $53,273M / $138,405M = 38.49%
FCFQuality_Score = clamp(((0.3849 − 0.40)/0.60)×100) = clamp(−2.52) = 0.0   (floors at zero — ratio is now
                                                                              below the sub-score's own 40% floor)
```
**This is the headline quality-side finding of this session.** FCF Quality fell from 14.98 (last two sessions) to a hard **0.0** — not because operations weakened (operating income grew a clean 30% YoY, margin expanded), but because **CapEx accelerated hard this quarter** ($35.7B Q1 → $44.9B Q2, +26% sequentially) rather than the deceleration this framework's last three sessions had flagged as a "watch item." The record $44.9B single-quarter CapEx print is the direct cause of both the negative single-quarter FCF (§3, hard-disqualifier table) and this sub-score's floor.

### Quality Score — Final
```
Quality Score = (95.85×0.25) + (76.12×0.15) + (60.04×0.20) + (100.0×0.15) + (60.0×0.15) + (0.0×0.10)
              = 23.963 + 11.418 + 12.008 + 15.000 + 9.000 + 0.000
              = 71.39
```

**Quality Score = 71.4 — FAILS the 80.0+ gate, and DOWN 2.3 points from 73.7 (2026-07-04/07-16).** This is the first time GOOG's Quality Score has moved since it was first computed on 2026-07-04 — a real, quantified deterioration driven almost entirely by the FCF Quality collapse (§3f) and a smaller ROIC-dilution drag from the fresh capital raise (§3a), only modestly offset by a slightly better Gross Margin and a stronger, primary-sourced Growth/TAM read. **Phase 04 Quality Watch escalation: continues, and this quarter shows it is not improving as the last two sessions' flagged "watch whether FCF Quality recovers as CapEx decelerates" hoped — the opposite happened.**

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = 23.35× (see §5)
EY = 1 ÷ 23.35 = 4.28%
Spread = EY − 10Y Treasury = 4.28% − 4.65% = −0.37pp
```
Spread < +1.5% → **fails** → **+5 additive** (yellow flag, not a veto).

**Step 2 — Rate Regime Modifier**
10Y ≈ 4.65% → 3.5–5% bracket → **+5**

**Combined Rate Modifier: +10** (unchanged bracket vs. prior sessions)

---

## 5. Valuation Score (Phase 02)

### Market Cap / EV (computed from live price and today's fresh balance sheet, Rule 0/Rule 6 — not a stale vendor field)

```
Market Cap = $342.61 × 12,230M shares = $4,190,120M
Preferred stock (added to EV, standard convention — liquidation preference ≈$19.0B, close to the $18.0B carrying
                 value; excluded from the Quality Score's Net Debt/EBITDA leverage ratio in §3d per that formula's
                 literal Total-Debt basis — first time this framework has had to make this call for GOOG, flagged
                 for future consistency)
EV = Market Cap $4,190,120M + Preferred $19,000M + Total Debt $98,165M − Cash+STI $242,474M = $4,064,811M
```
⚠️ Yahoo's own stale `enterpriseValue` field (still reading ~$4.16T, computed off pre-earnings Q1'26 balance-sheet data that hasn't yet ingested today's capital raise) was **not** used — same "compute EV independently, don't trust a lagging vendor field" discipline as every prior GOOG session, now more consequential than usual given how much the balance sheet moved this quarter.

### FCF Yield (40% weight) — Owner Earnings adjustment (Upgrade 1)
```
Owner Earnings Yield = $138,405M / $4,190,120M = 3.30%
FCF_Score = clamp(100×(1 − 3.30/10)) = 66.97
```

### EV/EBIT (25% weight, **redistributed to 40% — see PEG note below**)
```
EV/EBIT = $4,064,811M / $164,011M = 24.78×
EV/EBIT_Score = clamp((24.78 − 12)/23 × 100) = 55.58
```

### Forward PE + Historical PE Modifier (20% weight)

**5-year PE range reconstruction — methodology note (tooling constraint, fully disclosed):** `yfinance`'s documented `get_earnings_dates`-based method again failed (`curl_cffi` TLS reset, same as every prior session). Yahoo's `fundamentals-timeseries` HTTP endpoint (the manual workaround used successfully on 07-04) this time returned only ~5 trailing quarters regardless of the date range requested — insufficient depth. Reconstructed instead from: (1) stockanalysis.com's quarterly diluted-EPS table (Q3 2021–Q2 2026, 20 quarters, split-adjusted); (2) 3 additional back-quarters (Q4 2020–Q2 2021 EPS) sourced via WebSearch to complete a full rolling-TTM series back to Q3 2021; (3) IBKR's 5-year daily price history, paired at each **quarter-end** date (rather than the documented method's post-earnings-date pairing — a disclosed adaptation, since exact historical earnings-report dates weren't independently re-verified this session; this uses the price the market was assigning *before* that quarter's own results were known, a defensible but not identical proxy to the documented method). Q1 2026 and Q2 2026 EPS used in the series are **Rule-6 normalized** (one-off gains stripped: $2.76 and $2.85 respectively), consistent with prior sessions' treatment of Q1 2026.

```
Result: 5yr Avg PE 23.92× | 5yr Low PE 17.42× | 5yr High PE 31.27×
(vs. 07-04/07-16 sessions' 24.88× / 18.00× / 32.28× — a modest downward shift, expected since this
 reconstruction adds the new Q2 2026 point, drops the oldest quarter, and uses a different price-pairing
 convention; both reconstructions place GOOG's current multiple in a similar relative position within its
 own range, so this methodology difference does not appear to be doing outsized work in the final score)
```

```
Forward EPS (NTM consensus, Yahoo — pre-earnings vintage, not yet refreshed for today's print, flagged) = $14.674
Forward PE = $342.61 / $14.674 = 23.35×
FwdPE_Score = clamp((23.35 − 17.42)/(31.27 − 17.42) × 100) = 42.80
```
**Historical PE Modifier (Upgrade 2):** Forward PE vs 5yr avg (23.92×): (23.35 − 23.92)/23.92 × 100 = **−2.4%** → within ±10% → no separate modifier (already folded into the range positioning).

### PEG (15% weight) — **redistributed to EV/EBIT this session; Fast-Grower PEG not scored**

**This is a genuine methodology call, flagged explicitly.** GOOG has been ruled Fast-Grower-eligible in two prior sessions based on a clean FY2022→FY2025 annual Net Income trend (undistorted by one-offs). That structural eligibility is unchanged. But the framework's PEG clean-earnings clarification (2026-06-20) also requires the **specific growth-rate input feeding this quarter's PEG ratio** to be reliable — and every readily-available growth-rate field checked this session is now distorted by the one-off gains:
- Yahoo `pegRatio` (1.36) and `trailingEps` ($13.12) haven't yet ingested Q2 2026's raw $9.11 EPS — about to become badly distorted once they do.
- Yahoo `earningsGrowth` (82.0%) and `earningsTrend` (`0y` growth 31.96%, `+1y` growth just 2.87%) are all measured against the gain-inflated 2026 actuals — the anomalously low `+1y` 2.87% forward-growth estimate is itself the tell-tale sign of a distorted comp base, not a genuine deceleration signal.

Per valuation-scoring.md's explicit escape hatch ("redistribute PEG's 15% to EV/EBIT rather than forcing PEG off an unreliable base"), and consistent with "never invent or estimate financial data" (computing a "clean" PEG myself would require substituting my own assumed growth rate, not a sourced one), **PEG is not scored this session; its 15% weight redistributes to EV/EBIT (25%→40%)**. This is a session-specific deviation from the 07-04/07-16 treatment, to be revisited once the one-off gains roll out of the trailing/consensus windows (Q1 2026's $36.9B gain rolls off TTM at the Q1 2027 mark) or sell-side analysts re-base their models (which can take days-to-weeks post-earnings).

### Raw Weighted Score
```
Raw = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.40) + (FwdPE_Score × 0.20)
    = (66.97 × 0.40) + (55.58 × 0.40) + (42.80 × 0.20)
    = 26.79 + 22.23 + 8.56
    = 57.58
```

---

## 6. Upside/Downside Modifier (Expected-Return Modifier)

Scenario architecture follows the same 25/25/50 Bull/Base/Bear structure as every prior GOOG session, refreshed for current price, EPS basis, and the updated 5yr multiple range. **Given today's genuinely positive Cloud-acceleration data point (§3c), the bull-case narrative gets stronger supporting evidence this session — but per Rule 7's discipline against over-reacting to a single quarter, the bull/base/bear assumption levels themselves are held at the same conservative levels as before, not mechanically improved.**

| Scenario | Wt | Assumption | EPS basis | Multiple | Fair Value |
|---|---|---|---|---|---|
| Bull | 25% | AI monetization continues to prove out — today's Cloud +82% YoY and "90% of Fortune 100" Gemini Enterprise adoption are concrete evidence *for* this case, not just a hoped-for scenario | $14.674 × 1.07 = $15.70 | 28.0× | **$439.64** |
| Base | 50% | Consensus forward EPS (pre-earnings vintage, flagged), multiple = own normalized 5yr avg (23.92×) | $14.674 | 23.92× | **$351.01** |
| Bear | 25% | AI-search/Gemini competitive-disruption risk (Gemini 3.5 Pro delay + DeepMind talent exodus, flagged 2026-07-16) — no new contrary evidence located this session on the *consumer/search* side specifically (today's strength is concentrated in Cloud/enterprise), so this scenario is held unchanged | $13.00 | 19.0× | **$247.00** |

```
PW (probability-weighted) Fair Value = 0.25×439.64 + 0.50×351.01 + 0.25×247.00 = $347.16
Gap Upside % = $347.16 ÷ $342.61 − 1 = +1.33%
```
**Sanity check:** bull FV $439.64 sits comfortably inside the (pre-earnings-vintage) analyst consensus range ($340–$475, mean $430.07) — not stretched beyond the Street.

**Step 2 — catalyst & annualization (Rule 10).** Same 2-year catalyst window as prior sessions (AI monetization proof-points, sustained Cloud profitability, demonstrated defense of core search/ad share) — unchanged; still within the 18–24mo guardrail.
```
Annualized gap = +1.33% / 2 = +0.66%/yr
```

**Step 3 — expected annual return E.**
```
Intrinsic growth = +12%/yr (held conservatively, same rationale as every prior session — notably *below*
                   today's actual 24% YoY headline revenue growth and 82% YoY Cloud growth, i.e. this
                   assumption remains conservative even after today's strong print, not stale)
Shareholder yield = dividend 0.257% (Q2 2026 declared $0.22/share quarterly common dividend, annualized
                     $0.88 ÷ $342.61 — matches stockanalysis.com's independently-stated 0.26% almost exactly)
                   + TTM gross buyback yield 0.415% ($17,403M TTM buybacks [= FY2025's $45,709M total minus
                     H1 2025's $28,306M, since **both Q1 and Q2 2026 buybacks were $0** — a real, disclosed
                     capital-allocation shift toward the debt/equity-funded AI buildout, §2] ÷ $4,190,120M
                     market cap)
                   = 0.672%   (down sharply from ~1.3% in prior sessions — the buyback suspension is a real,
                     quantified drag on this component, not an oversight)

E = +0.66% + 12.0% + 0.672% = +13.33%/yr
```

**Step 4 — map E to M** (hurdle H = 10%):
```
E (13.33%) ≥ H → M = −15 × clamp((13.33 − 10)/15, 0, 1) = −15 × 0.222 = −3.33
```

**Upside/Downside Modifier M = −3.3** (a modest rescue, similar magnitude to the 07-16 session's −3.2 — the live price sits almost exactly at the scenario-blended fair value, so most of the rescue continues to come from the intrinsic-growth and shareholder-yield components, not a large price/fair-value gap).

---

## 7. Final Valuation Score

```
Final Score = Raw Weighted (57.58) + Rate Modifier (+10) + Upside/Downside Modifier (−3.33)
            = 64.24 → rounds to 64.2
```

**Valuation Score = 64.2 — "Fair Value"** (50.0–69.9 band) — a further, modest de-rate cheaper from 66.3 (2026-07-16), continuing the same band for the third consecutive session. Driven by a mix of: a lower live price base, a wider/lower 5yr PE range pulling the FwdPE sub-score down slightly, the PEG→EV/EBIT redistribution (net roughly neutral to slightly cheaper, since EV/EBIT_Score 55.58 sits below where PEG_Score would likely have landed given the now-distorted growth inputs), and a broadly similar Upside/Downside rescue to last session.

---

## 8. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 71.39) + 0.50 × 64.24
                = 0.50 × 28.61 + 32.12
                = 14.31 + 32.12
                = 46.43 → rounds to 46.4
```

**Composite Score = 46.4 — numerically lands in the "BUY — Standard position 3–5%" band (30.0–49.9), essentially flat vs. 46.3 (2026-07-16).**

**⚠️ Same false-green-light caveat as every prior GOOG session, unchanged: GOOG's Quality Score (71.4) still fails the 80.0+ gate — and by a wider, more robust margin than before (§3e's robustness check: even a perfect 5/5 moat only reaches 77.4).** Per valuation-scoring.md, the Composite Score "isn't computed for, and doesn't rescue, a company failing the quality gate" — shown here for transparency per established practice, **not a basis for adding to this position.**

---

## 9. Action Recommendation

**Net Action: HOLD — maintain the existing 1-share position as-is. No trim, no add. No change in action category from the last three sessions.**

**No trim:** Valuation Score (64.2) remains within the **50.0–69.9 "Fair Value" band** — "Hold — watch only, no new entry, no trim" per the current Action Table. Comfortably inside the band, not near either boundary.

**No add:** Composite Score's numeric BUY-band placement is not actionable given the Quality Gate failure (§3, §8), same reasoning as every prior session — and now a more decisive gate failure than before.

**⚠️ Did a trim or exit trigger fire this run? NO.** Valuation Score sits in the Hold band (not the 70.0+ trim bands), and none of the Full Exit triggers (fundamental deterioration, broken growth thesis, balance-sheet crisis, or 90.0–100.0 score sustained 2+ quarters) are close to tripping:
- **Fundamentals are not deteriorating on the operating side** — operating income +30% YoY, operating margin +2pp to 34%, revenue growth *accelerated* to +24% YoY (fastest in the cited 12-quarter streak), Google Cloud accelerated to +82% YoY. ROIC remains high in absolute terms (27.5%, comfortably above cost of capital) despite the mechanical capital-raise dilution flagged in §3a.
- **Balance sheet got materially *stronger*, not weaker** — net cash position roughly tripled/quadrupled this quarter via the $49.6B equity+preferred raise and $20.3B debt issuance (see §2) — the opposite of a "balance sheet crisis."
- **The one real, quantified negative this session — the FCF Quality collapse to 0.0 and the FCF-negative quarter (§3f)** — is a *quality* concern (feeds the Quality Score, which is already below the entry/rescue gate and cannot fall further into "failing" than it already was) rather than a valuation or balance-sheet trigger, and does not on its own meet the Phase 06 bar (it reflects an accelerating, disclosed, strategic capex ramp — not margin compression, ROIC-below-cost-of-capital, or a broken growth thesis).

**Phase 04 Quality Watch escalation: continues, and has gotten worse, not better, this quarter.** GOOG's Quality Score has now failed the 80.0+ gate in three consecutive rescores (73.7 → 73.7 → **71.4**), the first actual *decline* since the score was first computed. The "watch whether FCF Quality recovers as CapEx decelerates" item flagged in the 07-04 and 07-16 sessions resolved in the wrong direction this quarter — CapEx *accelerated* sharply instead ($35.7B→$44.9B sequentially). Flagged prominently for the next session.

**This is a HOLD outcome — does not count as a trim/exit trigger firing** for any upstream priority-tier decision this Telegram-scan run may be making across other tickers.

No order setup is produced (per operating-brief.md, only required for BUY/TRIM actions).

---

## 10. Next Review Trigger

**Date/event:** Alphabet's Q3 FY2026 earnings release, expected late October 2026 — standard re-score within 3 business days per the operating calendar.

**Earlier trigger on:** a >15% unexplained price move (Rule 9), a guidance revision, material M&A, a management change, or credible new evidence on the Gemini 3.5 Pro delay/DeepMind-talent-exodus thread (07-16 session) translating into actual consumer search/ad share loss (today's strength was concentrated in Cloud/enterprise, not a direct read on that specific risk).

**Specifically flag for the next session/near-term follow-up:**
1. **The earnings call itself** (4:30 PM ET, 22 Jul 2026 — concurrent with/just after this session) will likely include forward CapEx guidance and management commentary on the FCF-negative quarter; not available in time for this pull. Worth an early informal check (even outside the standard quarterly cadence) if guidance materially changes the AI-capex trajectory picture.
2. **The next trading session's open price** — a more settled read than the still-volatile pre-call after-hours print used in §1.
3. **Does the FCF Quality sub-score reverse itself** — this quarter's move was the wrong direction (CapEx accelerated, not decelerated); worth confirming whether $44.9B/quarter is a new elevated run-rate or a one-quarter spike.
4. **ROIC trend** as the newly-raised $49.6B+ of capital gets deployed — the current 27.5% reading is depressed by a mechanical, temporary invested-capital jump, not an operating problem, and should mean-revert upward as that capital is put to work (or stay depressed if it sits idle for multiple quarters, which would be a genuinely worse sign).
5. **Re-verify the PEG redistribution call (§5)** once Q1 2026's one-off gain rolls out of the trailing window (Q1 2027) or once sell-side consensus growth estimates re-base post-earnings — PEG scoring should likely resume once the earnings-base distortion clears.
6. **Analyst price-target revisions** in the days following today's release, once fully digested (this session's PT data is pre-earnings vintage).

---

## Glossary

- **8-K**: A US company's "current report" filed with the SEC to disclose a material event between regular filings — earnings releases are typically furnished as an exhibit to one.
- **ATM Program (At-the-Market Offering Program)**: A facility letting a company sell newly issued shares directly into the open market over time through a sales agent, rather than in one bulk-priced offering.
- **Beta**: A stock's sensitivity to overall market moves.
- **bps / pp**: Basis points (0.01 percentage points) / percentage points.
- **Buyback yield (gross)**: The rate at which a company's share count would shrink per year from repurchasing its own stock, not netted against new share issuance.
- **CAGR**: Compound Annual Growth Rate.
- **CapEx**: Capital Expenditure.
- **Catalyst window**: The timeframe within which a documented event is expected to close the price/fair-value gap.
- **Composite Score**: This framework's blended 0.0–100.0 ranking number — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — computed only after a company clears the 80.0+ Quality Score gate.
- **D&A**: Depreciation & Amortization.
- **EBIT / EBITDA**: Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **EPS**: Earnings Per Share.
- **EV**: Enterprise Value — market cap + debt − cash.
- **EV/EBIT**: Enterprise Value ÷ EBIT, a valuation multiple independent of capital structure.
- **EY (Earnings Yield)**: 1 ÷ Forward PE, compared against bond yields in the Rate Environment Gate.
- **Fast Grower**: Peter Lynch's term for EPS growth >15%/yr for 3+ years — this framework's PEG-sub-score trigger.
- **FCF (Free Cash Flow)**: Cash generated after running and maintaining the business.
- **FCF Yield**: FCF ÷ Market Cap (or EV) — higher is cheaper.
- **FCF/NI conversion ratio**: FCF ÷ Net Income — a cash-quality check.
- **Forward PE**: Price ÷ next-twelve-months expected EPS.
- **FV (Fair Value)**: The analyst's estimate of intrinsic worth, independent of market price.
- **GAAP**: Generally Accepted Accounting Principles.
- **Gross Margin**: Gross Profit ÷ Revenue.
- **Hard disqualifier**: A Quality Score condition that fails a company regardless of its weighted score, subject to specific documented carve-outs.
- **Hurdle rate**: The minimum acceptable annual return (10% in this framework) the Upside/Downside Modifier measures expected return against.
- **Mandatory Convertible Preferred Stock**: A class of preferred stock that must convert into common shares by a set future date, paying a fixed preferred dividend until then.
- **Moat**: A durable competitive advantage protecting a business's profits from competitors.
- **MoS (Margin of Safety)**: How far below fair value the buy price is set.
- **Net Debt/EBITDA**: A leverage ratio — this framework's primary balance-sheet-risk gate.
- **Net Margin**: Net Income ÷ Revenue.
- **NI**: Net Income.
- **NOPAT**: Net Operating Profit After Tax.
- **NTM**: Next Twelve Months.
- **Owner Earnings**: Net Income + D&A − maintenance-only CapEx — used instead of raw FCF for moat-building reinvestors including Alphabet (Hybrid Upgrade 1).
- **PEG ratio**: PE ÷ earnings growth rate.
- **Phase 01–06**: The six sequential stages of this framework.
- **PT (Price Target)**: An analyst's price forecast.
- **PW (Probability-Weighted) Fair Value**: This framework's blended fair value — 25% bull + 50% base + 25% bear.
- **Quality Score**: This framework's 0.0–100.0 score (higher = better) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score.
- **Rate Environment Gate / Rate Regime Modifier**: The mandatory pre-score check comparing Earnings Yield against the 10-Year Treasury, and the resulting additive score adjustment.
- **ROIC**: Return on Invested Capital.
- **Rule 0 / Rule 6 / Rule 9 / Rule 10**: This framework's standing instructions to always fetch a live price first; normalize distorted earnings before valuing; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline.
- **TAC (Traffic Acquisition Costs)**: Payments Alphabet makes to distribution partners and network members to be the default search provider or host ads — a direct cost of generating ad revenue.
- **TAM**: Total Addressable Market.
- **TTM**: Trailing Twelve Months.
- **Upside/Downside Modifier (Expected-Return Modifier)**: The additive ±15 adjustment based on expected annual return vs. the 10% hurdle.
- **Valuation Score**: This framework's 0.0–100.0 score (lower = cheaper) combining the Phase 02 sub-scores, Rate Gate, and Upside/Downside Modifier.

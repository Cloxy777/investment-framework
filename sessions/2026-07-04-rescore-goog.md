# RESCORE — GOOG (Alphabet Inc., Class C) — 2026-07-04

**Task type:** RESCORE (mode `--both`)
**Date:** 04 Jul 2026
**10Y US Treasury Yield:** 4.49% (WebSearch: Advisor Perspectives "Treasury Yields Snapshot: July 2, 2026" — most recent available; US Treasury market observed the July 4th holiday on Fri 3 Jul, then the weekend, so 2 Jul is the latest print. Same figure independently used in this session's AVGO rescore earlier today.)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current GOOG position:** 1 share, IBKR, 0.61% of portfolio, avg cost $295.70
**Sector:** Communication Services — Internet, Search & Digital Advertising / Cloud
**Last review:** 20 Jun 2026 (Valuation Score 73.1; Quality Score never computed — GOOG was flagged stale pending the 2026-06-29 Quality Score/Composite Score methodology addition, see [watchlist/STALE.md](../watchlist/STALE.md)). This session computes GOOG's Quality Score for the first time and refreshes the Valuation Score with live data.

*Plain-English note: GOOG = Alphabet's Class C share (no voting rights); GOOGL = Class A (voting). The economics are identical share-for-share and this framework treats them interchangeably for scoring.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$356.18** | IBKR `get_price_history` (contract_id 208813720, NASDAQ), most recent daily bar close = **2026-07-02** (last trading session before the market observed the July 4th holiday on Fri 3 Jul, ahead of the Sat 4 Jul/Sun 5 Jul weekend). Cross-validated against Yahoo Finance's live chart API `regularMarketPrice`, independently reading the identical **$356.18**. |
| ⚠️ Tooling flag | IBKR `get_price_snapshot`'s `last` field returned **$357.89** flagged `is_close: true` — this is stale by one session: it matches the **2026-07-01** close, not the most recent one (2026-07-02, $356.18). `get_account_positions`' cached `market_price` read a third value ($355.11), also not the freshest. Used the cross-validated $356.18 figure per Rule 0, consistent with the same stale-snapshot pattern already flagged in this session's AVGO rescore. |
| 52-week range | $173.88 – $404.47 (Yahoo) / $173.48 – $404.47 (IBKR `misc_statistics`) | Sources agree closely (<0.3% low-end difference, immaterial). Price sits ~12% off the 52-week high, ~105% above the 52-week low. |
| Analyst consensus PT | Mean $426.62 / median $430.00 (range $340–$475, n=13), rating "Strong Buy" | Yahoo `financialData` — essentially unchanged from the 2026-06-20 session's $426.62 mean. Used only as a bull-case sanity anchor (§6). |
| Prior session price | $367.46 (20 Jun 2026) | GOOG is **−3.1%** since the last rescore — well below the 15% Rule 9 threshold; this rescore is calendar/methodology-driven (Quality Score first computed + routine refresh), not price-driven. |

---

## 2. Data Gathered — Sources, Method, and a Material Data-Quality Finding

**Tooling note:** `yfinance`'s own crumb-negotiation was rate-limited all session (`YFRateLimitError`) despite the `requests.Session()` workaround used in the AVGO session. Worked around by reproducing `yfinance`'s own underlying HTTP calls directly (Yahoo's `fundamentals-timeseries` API for financials, its `quoteSummary` API for snapshot fields, and its `calendar/earnings` HTML endpoint for the trailing-EPS/PE reconstruction) using a plain cookie+crumb session — same public Yahoo data source `yfinance` itself wraps, no substitute data used.

### ⚠️ Material finding — Alphabet's Q1 2026 GAAP results are contaminated by a $36.9B one-off, non-cash gain

Alphabet's Q1 2026 10-Q/8-K (filed 29 Apr 2026) reports a **$36,915M net gain on non-marketable equity securities** (unrealized, mark-to-market — likely reflecting Alphabet's stakes in AI-related private companies), which **increased Q1 2026 tax provision, net income, and diluted EPS by $8.2B, $28.7B, and $2.35/share respectively** (Alphabet's own press release language, confirmed via the SEC 8-K exhibit 99.1). This is exactly the kind of one-off, non-operating item Rule 6 ("Normalize Before You Value") requires stripping out before using Net Income in any valuation or quality calculation — comparable in kind (though far larger in size) to the AMD tax-release and DUOL deferred-tax-allowance precedents already in [glossary.md](../framework/glossary.md).

**This also exposed a vendor data-quality bug independent of the one-off itself:** Yahoo's own quarterly "EBIT" field for Q1 2026 reads **$77,945M** — but Alphabet's actual **GAAP operating income** for the quarter (per the 8-K) is **$39,696M**. The ~$38.2B gap is Yahoo's EBIT field silently pulling in the non-operating equity-securities gain (visible in pretax income) rather than true operating income. The same distortion propagates into Yahoo's quarterly "EBITDA" field. **Both were replaced with the true, 8-K-sourced GAAP figures throughout this session** — this matters materially: using Yahoo's contaminated Q1 2026 EBIT/Net-Income figures as-is would have understated GOOG's TTM EV/EBIT and Owner Earnings yield by a wide margin (shown as a side-by-side comparison in §7).

**TTM window used throughout:** Q2 2025 – Q1 2026 (trailing four quarters ending 2026-03-31), reconstructed from Yahoo's `fundamentals-timeseries` quarterly series and cross-checked against the FY2025 annual 10-K figures (unchanged since the 2026-06-20 session, which used FY2025 annual only).

| Metric | Q2'25 | Q3'25 | Q4'25 | Q1'26 (as reported) | Q1'26 (normalized, gain stripped) | **TTM** |
|---|---|---|---|---|---|---|
| Revenue | $96,428M | $102,346M | $113,829M | $109,896M | — (unaffected) | **$422,499M** |
| Gross Profit | $57,389M | $60,977M | $68,062M | $68,625M | — (unaffected) | **$255,053M** (GM 60.37%) |
| GAAP Operating Income (EBIT) | $34,194M | $44,130M | $39,415M | $39,696M *(corrected — see finding above; Yahoo's raw field read $77,945M)* | n/a | **$157,435M** |
| D&A | $4,998M | $5,611M | $6,040M | $6,482M | — (unaffected) | **$23,131M** |
| CapEx | $22,446M | $23,953M | $27,851M | $35,674M | — (unaffected) | **$109,924M** |
| Operating Cash Flow | $27,747M | $48,414M | $52,402M | $45,790M | — (unaffected, non-cash gain adds back) | **$174,353M** |
| **FCF** (OCF − CapEx) | $5,301M | $24,461M | $24,551M | $10,116M | — | **$64,429M** |
| Net Income (GAAP) | $28,196M | $34,979M | $34,455M | $62,578M | **$33,878M** (62,578 − 28,700) | **raw $160,208M / normalized $131,508M** |

Sources: Yahoo `fundamentals-timeseries` (`quarterlyTotalRevenue`, `quarterlyGrossProfit`, `quarterlyEBIT`, `quarterlyDepreciationAmortizationDepletion`, `quarterlyCapitalExpenditure`, `quarterlyOperatingCashFlow`, `quarterlyNetIncome`), cross-checked against Alphabet's Q1 2026 8-K (SEC EDGAR, `googexhibit991q12026.htm`) for the corrected operating income and the equity-gain figures.

**Balance sheet (as of 2026-03-31, most recent quarter-end):**

| Item | Value | Source |
|---|---|---|
| Total shares outstanding | **12,116M** (Class A 5,824M + Class B 836M + Class C 5,456M) | Alphabet Q1 2026 10-Q/8-K — confirms Alphabet's total consolidated share count across all three classes, **not** the ~5.5B Class C-only figure Yahoo's `sharesOutstanding` field reports for the GOOG ticker (a **dual-class-shares data trap**, same category as the FUBO/CHTR precedents in [glossary.md](../framework/glossary.md) — verified against Yahoo's own `marketCap ÷ price` implied share count of ~12.20B, consistent with the true consolidated figure, not the per-ticker field). |
| Total Debt | $90,484M | Yahoo `quarterlyTotalDebt` |
| Cash + Short-Term Investments | $126,840M | Yahoo `quarterlyCashCashEquivalentsAndShortTermInvestments` |
| Net Debt | **−$36,356M** (net cash position) | Computed |
| Total Stockholders' Equity | $478,746M | Yahoo `quarterlyStockholdersEquity` |
| Forward EPS (consensus, NTM) | $14.55771 | Yahoo `financialData`/`defaultKeyStatistics` |
| Forward PE | 24.467× | Yahoo (price $356.18 ÷ forward EPS) |
| Trailing PEG | 1.4 | Yahoo `defaultKeyStatistics.pegRatio` |
| Beta | 1.247 | Yahoo `info.beta` |
| Dividend yield | 0.25% | Yahoo `summaryDetail` |
| FY2025 gross buybacks | $45,709M | Yahoo `annualRepurchaseOfCapitalStock` |

**Market Cap / EV (computed from live price, Rule 0 — not a stale vendor field):**
```
Market Cap = $356.18 × 12,116M shares = $4,315,477M
EV = Market Cap + Net Debt = $4,315,477M + (−$36,356M) = $4,279,121M
```
Cross-check: Yahoo's own (likely slightly stale-timed) `enterpriseValue` field reads $4,284,513M — within 0.13% of the figure computed here; immaterial difference, own computation used for full transparency.

**5-year historical PE reconstruction (framework's documented `get_earnings_dates`-equivalent method):** replicated using Yahoo's `calendar/earnings` endpoint (20 quarterly reported-EPS points, Feb 2021–Apr 2026 trailing-PE series, n=20 ≈ 5 years) — **the Apr 2026 quarter's EPS was normalized ($5.11 → $2.76, stripping the $2.35/share one-off gain per the 8-K) before computing that quarter's trailing PE**, to avoid the one-off artificially lowering the trailing PE at that point and distorting the 5-year range. Full table in scratch calculation; headline results:

| | 5yr Avg PE | 5yr Low PE | 5yr High PE |
|---|---|---|---|
| **Normalized (used for scoring)** | **24.88×** | **18.00×** | **32.28×** |
| Raw/uncorrected (for comparison only) | 24.59× | 18.00× | 30.84× |

No other metric was invented or estimated — every figure above traces to a live fetch (IBKR or Yahoo), a primary-source SEC filing, or a disclosed, labeled modeling assumption (§6).

---

## 3. Quality Score (Phase 01 gate) — first ever computed for GOOG

**Hard disqualifier check (must pass before the weighted score matters):**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs *without a documented growth-capex explanation*? | FY2024 72.7%, FY2025 55.4%, TTM 49.0% (normalized) — below 70% | disqualify if <70% for 2+ yrs **and no growth-capex explanation** | ✅ **PASS (carve-out applies)** — Alphabet's heavy, explicitly disclosed AI-infrastructure CapEx ramp (guided to **$190B for FY2026**) is the documented growth-capex explanation Upgrade 1 (Owner Earnings) exists for; this is the *same* carve-out already invoked for GOOG in the 2026-06-20 valuation session. The carve-out waives the hard disqualifier only — **it does not exempt the continuous FCF Quality sub-score below, which still scores this ratio on its own terms** (see §3f). |
| Net Debt/EBITDA over threshold? | **Net cash** (−0.201×) | disqualify if >2.5× | ✅ PASS |
| FCF-positive 3+ consecutive years? | FY2023 $69.5B, FY2024 $72.8B, FY2025 $73.3B, TTM $64.4B — all positive | disqualify if not | ✅ PASS |

No hard disqualifier triggers. Proceeding to the weighted score.

### (a) Profitability (25% weight)

```
Net Margin (TTM, normalized) = $131,508M / $422,499M = 31.13%
NetMargin_Component = clamp((31.13/30)×100, 0, 100) = 100.0  (saturates)

ROIC — Rule-6-normalized NOPAT ÷ Net Invested Capital:
  EBIT (TTM, corrected) = $157,435M
  Normalized effective tax rate = 16.78% (FY2025 clean annual rate: $26,656M tax / $158,826M pretax —
    FY2025 has no comparable one-off gain, so this is the cleanest available rate; Q1 2026's own
    effective rate is itself distorted by the gain's outsized $8.2B tax effect)
  NOPAT = $157,435M × (1 − 0.1678) = $130,986M
  Net Invested Capital = Total Debt $90,484M + Total Equity $478,746M − Cash+STI $126,840M = $442,390M
  ROIC = $130,986M / $442,390M = 29.61%
ROIC_Component = clamp((29.61/30)×100, 0, 100) = 98.70

Profitability_Score = (100.0 + 98.70) / 2 = 99.35
```
No FCF-positivity cap applies (FCF-positive well beyond 3 years).

### (b) Margins (15% weight)

```
Gross Margin (TTM) = $255,053M / $422,499M = 60.37%
GrossMargin_Score = clamp((60.37/80)×100, 0, 100) = 75.46
```
No structural-trend bonus applicable (already far above the 40% threshold the bonus targets).

### (c) Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $282,836M → FY2025 $402,836M) = (402,836/282,836)^(1/3) − 1 = 12.51%
Growth_Score (base) = clamp((12.51/25)×100, 0, 100) = 50.05
```
**TAM/pricing-power evidence (cited):** Google Cloud revenue +63% YoY in Q1 2026 — the fastest growth among the three major hyperscalers (AWS +19%, Azure +40%), cloud remaining accretive market share (13% and rising) despite starting from third place (WebSearch: businesstats.com/Statista-sourced Q1 2026 cloud-infrastructure market-share data; Alphabet's own Q1 2026 earnings release). Documented, third-party-corroborated evidence of TAM expansion → **+10**.
No decelerating-growth evidence exists (revenue growth is *re-accelerating* — 22% YoY in Q1 2026 vs ~15% for FY2025 overall) — no −10 applies.
```
Growth_Score = clamp(50.05 + 10, 0, 100) = 60.05
```

### (d) Balance Sheet (15% weight)

```
Net Debt = −$36,356M (net cash)
EBITDA (TTM, corrected) = EBIT $157,435M + D&A $23,131M = $180,566M
Net Debt/EBITDA = −36,356 / 180,566 = −0.201×
BalanceSheet_Score = clamp(100×(1 − (−0.201)/4), 0, 100) = 100.0  (saturates — net cash beats the 0× ceiling)
```
Standard /4 denominator (GOOG is not a payment network/exchange; Upgrade 5 override doesn't apply).

### (e) Moat Signal (15% weight) — checklist, cited evidence per signal (strict bar, per the AVGO-session precedent for this checklist)

| Signal | Marked | Cited evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | StatCounter Global Stats: Google's global search-referral share was 90.02% (Apr 2026) / 90.46% (May 2026) — stable/dominant. Separately, Google Cloud's infrastructure market share is *growing* (13% and rising, fastest of the Big Three at +63% YoY, Q1 2026 — Statista/businesstats.com-sourced). Two independent third-party-tracked share metrics, both stable-to-growing. |
| Brand premium | **FALSE** | No cited pricing-power evidence (documented price increases without volume loss) located this session — Alphabet no longer breaks out paid-click/CPC trend data as clearly as in past filings. Flagged as a gap, not a negative finding. |
| Network effect | **TRUE** | Documented two-sided-marketplace mechanisms: YouTube (creator/viewer/advertiser flywheel) and Search's query-volume-driven relevance-improvement loop — both are well-established, structurally documented mechanisms of Alphabet's core products, not merely asserted. |
| Switching costs | **TRUE** | Google Workspace/Cloud enterprise integration depth (BigQuery, Vertex AI, Workspace document/email migration) — a documented data-migration/workflow-lock-in mechanism, the same category of evidence as AVGO's VMware citation in the 2026-07-04 AVGO session. |
| Scale cost advantage | **FALSE** | No cited cost-per-unit (e.g. cost-per-query) comparison vs. smaller AI-search entrants located this session, despite Alphabet's large disclosed capex base ($190B FY2026 guide) being suggestive of scale — the checklist's bar specifically requires cost-per-unit data, which wasn't sourced here. |

```
Moat_Score = (3/5) × 100 = 60.0
```

**Robustness check (unlike the AVGO session, this is *not* a knife-edge call):** even under the most generous possible re-scoring of this checklist — marking all 5 signals TRUE (Moat_Score = 100.0) — the overall Quality Score would rise only to **79.7**, still **below** the 80.0 gate (see §3f for the full number). The gate result here is **not** sensitive to the Moat judgment call; it is driven by the Growth and FCF Quality sub-scores below.

### (f) FCF Quality (10% weight)

```
FCF/NI (TTM, normalized Net Income) = $64,429M / $131,508M = 48.99%
FCFQuality_Score = clamp(((0.4899 − 0.40)/0.60)×100, 0, 100) = 14.98
```
**Note — using normalized (not raw GAAP) Net Income here is the more conservative and more correct choice, not a favorable one:** using the raw, gain-inflated Net Income ($160,208M) would actually produce an *even lower* FCFQuality_Score (40.22% ratio → 0.37), since the non-cash gain inflates the denominator without a matching cash inflow. Either way this sub-score reads low — this is a genuine, not an artifact-driven, finding: Alphabet's heavy FY2026 AI-capex ramp ($109.9B TTM, guided to $190B for the full year) is compressing free cash flow conversion materially, exactly the dynamic Upgrade 1 (Owner Earnings) exists to keep from unfairly penalizing the *valuation* score (§5) — but the Quality Score's continuous FCF Quality sub-score has **no equivalent carve-out** (per quality-scoring.md: the growth-capex explanation waives only the *hard disqualifier*, "independent of this continuous score"). This is a real tension in the framework worth flagging for future review, not one this session is authorized to resolve by overriding the formula.

### Quality Score — Final

```
Quality Score = (99.35×0.25) + (75.46×0.15) + (60.05×0.20) + (100.0×0.15) + (60.0×0.15) + (14.98×0.10)
              = 24.838 + 11.319 + 12.010 + 15.000 + 9.000 + 1.498
              = 73.664
```

**Quality Score = 73.7 — FAILS the 80.0+ gate** (first-ever computed Quality Score for GOOG). Per [quality-scoring.md](../framework/quality-scoring.md) and the RESCORE process (rescore.md step 3): **an existing holding failing the Quality Gate is not retroactively force-exited**, but this is new information warranting a **Phase 04 Quality Watch escalation** — flagged prominently here and carried into §9's action discussion and the watchlist entry.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = 24.467×
EY = 1 ÷ 24.467 = 4.087%
Spread = EY − 10Y Treasury = 4.087% − 4.49% = −0.40pp
```
Spread (−0.40%) < +1.5% → **fails** → **+5 additive** (yellow flag, not a veto).

**Step 2 — Rate Regime Modifier**
10Y = 4.49% → 3.5–5% bracket → **+5**

**Combined Rate Modifier: +10** (unchanged bracket vs. the 2026-06-20 session)

---

## 5. Valuation Score (Phase 02)

### FCF Yield (40% weight) — Owner Earnings adjustment (Upgrade 1) required for Alphabet

```
Growth CapEx test: Maintenance proxy = D&A (TTM) $23,131M
                    Growth CapEx = Total CapEx $109,924M − $23,131M = $86,793M = 78.96% of total CapEx
                    (» 30% threshold) → Owner Earnings adjustment APPLIES
Owner Earnings (TTM, normalized) = Net Income (normalized) $131,508M + D&A $23,131M − Maintenance CapEx $23,131M
                                  = $131,508M   (D&A and the maintenance-CapEx proxy cancel exactly,
                                                  as in the 2026-06-20 session, since D&A is the maintenance proxy)
Owner Earnings Yield = $131,508M / $4,315,477M = 3.047%
FCF_Score = clamp(100×(1 − 3.047/10), 0, 100) = 69.53
```
*(For comparison, reported/unadjusted FCF yield = $64,429M / $4,315,477M = 1.49% — far lower, exactly what the Owner Earnings adjustment corrects for a heavy AI-reinvestor.)*

### EV/EBIT (25% weight)

```
EV/EBIT = $4,279,121M / $157,435M = 27.18×
EV/EBIT_Score = clamp((27.18 − 12)/23 × 100, 0, 100) = 66.00
```

### Forward PE + Historical PE Modifier (20% weight)

5yr *range* available (normalized) → primary formula:
```
FwdPE_Score = clamp((24.467 − 18.00)/(32.28 − 18.00) × 100, 0, 100) = clamp(45.29, 0, 100) = 45.29
```
**Historical PE Modifier (Upgrade 2):** Forward PE vs 5yr avg (24.88×): (24.467 − 24.88)/24.88 × 100 = **−1.66%** → within ±10% → **no change** (already folded in via the range positioning; no separate ±10 applied, consistent with the framework's no-double-counting rule).

### PEG (15% weight) — Fast-Grower eligibility ruling carried forward

**Ruling maintained from 2026-06-20:** Alphabet's Net Income grew cleanly (no one-off distortion) from $60.0B (FY2022) → $73.8B (FY2023) → $100.1B (FY2024) → $132.2B (FY2025), a clean multi-year >15%/yr base → **Fast-Grower eligible**, PEG scored.
```
PEG = 1.4 (Yahoo defaultKeyStatistics.pegRatio)
PEG_Score = clamp((1.4 − 0.5)/2.0 × 100, 0, 100) = 45.00
```

### Raw Weighted Score

```
Raw = (69.53×0.40) + (66.00×0.25) + (45.29×0.20) + (45.00×0.15)
    = 27.812 + 16.500 + 9.058 + 6.750
    = 60.12
```

---

## 6. Upside/Downside Modifier (Expected-Return Modifier)

Scenario architecture follows the same structure established in the 2026-06-20 session (AI-monetization bull / consensus base / AI-search-disruption bear), refreshed for current price, forward EPS, and the updated 5yr multiple range.

**Step 1 — scenario fair values.** Forward EPS (NTM consensus) = $14.55771 ≈ $14.56.

| Scenario | Wt | Assumption | EPS basis | Multiple | Fair Value |
|---|---|---|---|---|---|
| Bull | 25% | AI monetization proves out, Cloud margins inflect (63% YoY growth continuing), ad share defended; modest re-rate | $14.56 × 1.07 = $15.58 | 28.0× | **$436.24** |
| Base | 50% | Consensus forward EPS, multiple = own normalized 5yr avg (24.88×) | $14.56 | 24.88× | **$362.20** |
| Bear | 25% | AI-search disruption erodes core query/ad share, EPS pressured, de-rate toward the 5yr low | $13.00 | 19.0× | **$247.00** |

```
PW (probability-weighted) Fair Value = 0.25×436.24 + 0.50×362.20 + 0.25×247.00 = $351.91
Gap Upside % = $351.91 ÷ $356.18 − 1 = −1.20%
```
**Sanity check (Rule 0/bull-case):** bull FV $436.24 sits comfortably inside the analyst consensus range ($340–$475, mean $426.62, median $430.00) — not stretched beyond the Street.

**Step 2 — catalyst & annualization (Rule 10).** Same documented catalyst as the 2026-06-20 session: AI monetization proof-points, sustained Google Cloud profitability at scale, and demonstrated defense of core search/ad share against generative-AI answer engines — identifiable within **2 years** (unchanged; still within the 18–24mo guardrail window, so the upside-side −5 cap does not bind).
```
Annualized gap = −1.20% / 2 = −0.60%/yr
```

**Step 3 — expected annual return E.**
```
Intrinsic growth = +12%/yr (forward EPS CAGR, held conservatively — Street nearer 13–15%, haircut retained
                   for AI-search-disruption risk to the core, unchanged from the 2026-06-20 session)
Shareholder yield = dividend 0.25% + gross buyback yield ($45,709M FY2025 buybacks / $4,315,477M market cap
                   = 1.06%) = 1.31%   (gross, not net of SBC-driven share issuance — flagged as approximate,
                   feeds only this small component of E, same caveat as the 2026-06-20 session)

E = −0.60% + 12.0% + 1.31% = +12.71%/yr
```

**Step 4 — map E to M** (hurdle H = 10%):
```
E (12.71%) ≥ H → M = −15 × clamp((12.71 − 10)/15, 0, 1) = −15 × clamp(0.181, 0, 1) = −2.71
```

**Upside/Downside Modifier M = −2.7** (a modest rescue — not close to saturating either bound).

**⚠️ Transparency flag — this result sits close to the Fair-Value/Trim (70.0) boundary and is genuinely assumption-sensitive, shown here rather than hidden:**
- If intrinsic growth is trimmed to a more conservative **10%/yr** (vs. 12% used above): E = 10.71% → M = −0.71 → Final score = 60.12 + 10 − 0.71 = **69.41** — still Fair Value, but only just.
- If intrinsic growth is trimmed further to **8%/yr**: E = 8.71% (now *below* the 10% hurdle) → M = +5×(10−8.71)/10 = **+0.65** → Final score = 60.12 + 10 + 0.65 = **70.76** — this **would** cross into the 70.0–79.9 Trim band.
- The headline result (67.4, §7) is **not** knife-edge-fragile like a coin flip, but it is close enough to the boundary that the specific 12%/yr intrinsic-growth assumption is doing real work. Flagged per Guardrail 3 ("show the full calc... no black box") rather than presented with false precision.

---

## 7. Final Valuation Score

```
Final Score = Raw Weighted (60.12) + Rate Modifier (+10) + Upside/Downside Modifier (−2.71)
            = 67.41 → rounds to 67.4
```

**Valuation Score = 67.4 — "Fair Value"** (50.0–69.9 band) — a **de-rate out of the Expensive/Trim band** from the prior 73.1 (2026-06-20).

**What actually moved it, shown transparently (side-by-side with what a naive, uncorrected calculation would have produced):**

| Component | This session (Rule-6-corrected) | If Yahoo's raw, uncorrected Q1'26 EBIT/NI fields had been used instead |
|---|---|---|
| FCF_Score (Owner Earnings) | 69.53 (OE yield 3.05%) | 62.88 (OE yield 3.71%, using contaminated NI $160.2B) |
| EV/EBIT_Score | 66.00 (EV/EBIT 27.18×) | 42.90 (EV/EBIT 21.87×, using contaminated EBIT $195.7B) |
| FwdPE_Score | 45.29 (range 18.00–32.28×) | 50.39 (range 18.00–30.84×, uncorrected Apr'26 trailing PE) |
| Raw weighted | 60.12 | 52.71 |
| **Final (+ Rate +10, + U/D ≈ −2.7 both cases)** | **67.4** | **≈ 60.0** |

Both land in the same 50.0–69.9 Fair Value band, so the *action* conclusion is unaffected here — but the ~7-point gap between the corrected and uncorrected final scores shows the Q1 2026 one-off gain was **not** an immaterial rounding issue; a less careful pull of this quarter's data would have made GOOG look meaningfully cheaper than it is. This is the single most consequential finding of this session.

Compared to the 2026-06-20 session's 73.1: the de-rate is driven mainly by (a) FwdPE_Score dropping from 57.7→45.3 as the 5-year PE range widened (new Apr-2026 quarter entered the rolling window) while forward PE itself eased slightly, and (b) the live price falling ~3.1% since the last review, both partially offset by a smaller Upside/Downside rescue (−2.7 vs −0.8, since the price-to-fair-value gap moved from −5.3% to −1.2%, still both modestly *negative* — GOOG remains priced *above*, not below, its scenario-blended fair value).

---

## 8. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 73.664) + 0.50 × 67.41
                = 0.50 × 26.336 + 33.705
                = 13.168 + 33.705
                = 46.873 → rounds to 46.9
```

**Composite Score = 46.9 — numerically lands in the "BUY — Standard position 3–5%" band (30.0–49.9).**

**⚠️ This is a false-green-light risk and must not be acted on at face value — same caveat this repo's most recent rescore (NKE, 2026-07-01) applied to an analogous situation.** GOOG's Quality Score (73.7) **fails** the 80.0+ gate (§3). Per [valuation-scoring.md](../framework/valuation-scoring.md): "Composite Score isn't computed for, and doesn't rescue, a company failing the quality gate" — it is shown here for transparency and because this repo's established practice (the NKE precedent) is to compute and display it with the caveat attached, rather than suppress it, but **the Composite Score's numeric BUY-band placement is not a basis for adding to this position.** See §9 for the actual net action, which is governed by the Valuation Score and the Quality Watch flag, not the Composite number.

*(Unlike NKE's case, this is not a "value trap" driven by deteriorating moat/brand evidence — GOOG's gate failure is driven mainly by the Growth and FCF Quality sub-scores, the latter itself a byproduct of the same heavy, disclosed AI-capex reinvestment that Upgrade 1 already treats as quality-additive on the valuation side. Still a real gate failure, just a different character of one — flagged as such rather than conflated with NKE's situation.)*

---

## 9. Action Recommendation

**Net Action: HOLD — maintain the existing 1-share position as-is. No trim, no add.**

**No trim:** the Valuation Score (67.4) sits in the **50.0–69.9 "Fair Value" band** — per the current Action Table (strategy.md, unchanged since the 2026-06-07 revision), this band is "Hold — watch only, no new entry, no trim." This is a genuine change from the prior session's 73.1 (70.0–79.9, "Trim 25–30%") — GOOG has moved **out of** the trim band on fresh data, not merely held steady. §6/§7 show the calculation is close enough to the 70.0 boundary to flag as a "watch closely next quarter" item, not a comfortable Hold.

**No add:** even though the Composite Score (46.9) nominally reads "Cheap — Standard position," the Quality Score gate failure (§3, §8) means this number is not a reliable BUY signal here — consistent with the operating brief's "informs, never overrides" posture and this repo's NKE precedent. Independently, GOOG's current 0.61% weight is a legacy/small position, not one under active sizing consideration this session.

**No fundamental sell trigger is tripped:** margins intact (ROIC 29.6%, far above cost of capital), no balance-sheet stress (net cash position), Valuation Score is not in the 90+ sustained-exit zone, and the Quality gate failure — while a real escalation — does not itself meet the Phase 06 bar (no evidence of moat erosion, TAM shrinkage, or lost pricing power; the gate miss is mechanical, driven by capex-timing and a strict evidentiary bar on 2 of 5 moat signals per §3e's robustness check).

**Phase 04 Quality Watch escalation (recorded, not resolved this session):** this is GOOG's first-ever computed Quality Score, and it fails the 80.0+ gate. Flagged prominently here and in the watchlist entry. Worth re-checking at the next rescore whether the FCF Quality sub-score recovers as FY2026 CapEx growth decelerates off its current AI-buildout peak (per the 2026-06-20 session's own flagged "re-examine the Owner Earnings maintenance-CapEx proxy... if Alphabet's CapEx normalizes" — the same underlying dynamic now shows up quantitatively in the Quality Score too).

No order setup is produced (per operating-brief.md, only required for BUY/TRIM actions).

---

## 10. Next Review Trigger

**Date/event:** Alphabet's Q2 FY2026 earnings release, expected **~28–29 July 2026** (based on Alphabet's historical quarterly reporting cadence — Q1 2026 was reported 29 Apr 2026). Standard re-score within 3 business days per the operating calendar.

**Earlier trigger on:** a >15% unexplained price move (Rule 9), a guidance revision, material M&A, a management change, or new third-party evidence bearing on the two open Moat_Score gaps (brand-premium pricing data, cost-per-query scale data) or the Growth/FCF-Quality tension flagged in §3f.

**Specifically flag for the next session:** re-verify whether Alphabet's Q2 2026 CapEx guidance still points toward the full $190B FY2026 figure (if it decelerates, the FCF Quality sub-score should mechanically improve) and confirm the Q1 2026 equity-securities-gain normalization approach used here holds up against the fuller 10-Q disclosure (this session relied on the 8-K/press-release-level detail).

---

## Glossary

- **8-K**: A US company's "current report" filed with the SEC to disclose a material event between regular filings — earnings releases are typically furnished as an exhibit to one.
- **10-Q**: A US company's quarterly report filed with the SEC, containing unaudited financial statements and disclosures.
- **Beta**: A stock's sensitivity to overall market moves.
- **bps / pp**: Basis points (0.01 percentage points) / percentage points.
- **Buyback yield (net buyback yield)**: The rate at which a company's share count shrinks per year from repurchasing its own stock net of new issuance; this session used the *gross* buyback figure (not net of SBC-driven issuance), flagged as approximate.
- **CAGR**: Compound Annual Growth Rate.
- **CapEx**: Capital Expenditure.
- **Catalyst window**: The timeframe within which a documented event is expected to close the price/fair-value gap — required before the Upside/Downside Modifier can credit large expected upside.
- **Composite Score**: This framework's blended 0.0–100.0 ranking number — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — computed only after a company clears the 80.0+ Quality Score gate (shown here despite the gate failure, per established practice, with a "do not act on it" caveat attached).
- **D&A**: Depreciation & Amortization.
- **Dual-class shares**: A capital structure with two or more common-stock classes with different voting rights — a data-integrity trap where a vendor's `sharesOutstanding` field for one ticker (e.g. GOOG) may report only that class, not the company's true total consolidated share count across all classes.
- **EBIT / EBITDA**: Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **EPS**: Earnings Per Share.
- **EV**: Enterprise Value — market cap + debt − cash.
- **EV/EBIT**: Enterprise Value ÷ EBIT, a valuation multiple independent of capital structure.
- **EY (Earnings Yield)**: 1 ÷ Forward PE, compared against bond yields in the Rate Environment Gate.
- **Fast Grower**: Peter Lynch's term for EPS growth >15%/yr for 3+ years — this framework's PEG-sub-score trigger.
- **FCF (Free Cash Flow)**: Cash generated after running and maintaining the business.
- **FCF Yield**: FCF ÷ Market Cap (or EV) — higher is cheaper.
- **FCF/NI conversion ratio**: FCF ÷ Net Income — a cash-quality check; a low ratio without a growth-capex explanation is a red flag for earnings-quality games.
- **Forward PE**: Price ÷ next-twelve-months expected EPS.
- **FV (Fair Value)**: The analyst's estimate of intrinsic worth, independent of market price.
- **GAAP**: Generally Accepted Accounting Principles.
- **Gross Margin**: Gross Profit ÷ Revenue.
- **Hard disqualifier**: A Quality Score condition that fails a company regardless of its weighted score, subject to specific documented carve-outs.
- **Hurdle rate**: The minimum acceptable annual return (10% in this framework) the Upside/Downside Modifier measures expected return against.
- **Invested Capital**: The total capital (debt + equity, net of cash here) put to work in a business — the denominator of ROIC.
- **IRR**: Internal Rate of Return.
- **Moat**: A durable competitive advantage protecting a business's profits from competitors.
- **MoS (Margin of Safety)**: How far below fair value the buy price is set.
- **Net Debt/EBITDA**: A leverage ratio — this framework's primary balance-sheet-risk gate.
- **Net Margin**: Net Income ÷ Revenue.
- **NI**: Net Income.
- **NOPAT**: Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the numerator of ROIC here.
- **Owner Earnings**: Net Income + D&A − maintenance-only CapEx — used instead of raw FCF for moat-building reinvestors including Alphabet (Hybrid Upgrade 1), since D&A used as the maintenance-CapEx proxy makes Owner Earnings collapse to Net Income here.
- **PEG ratio**: PE ÷ earnings growth rate.
- **Phase 01–06**: The six sequential stages of this framework.
- **PT (Price Target)**: An analyst's price forecast.
- **PW (Probability-Weighted) Fair Value**: This framework's blended fair value — 25% bull + 50% base + 25% bear.
- **Quality Score**: This framework's 0.0–100.0 score (higher = better) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score.
- **Rate Environment Gate / Rate Regime Modifier**: The mandatory pre-score check comparing Earnings Yield against the 10-Year Treasury, and the resulting additive score adjustment.
- **ROIC**: Return on Invested Capital.
- **Rule 0 / Rule 6 / Rule 9 / Rule 10**: This framework's standing instructions to always fetch a live price first; normalize distorted earnings before valuing; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline.
- **SBC (Stock-Based Compensation)**: Employee pay in company shares/options — a non-cash expense that dilutes existing shareholders over time.
- **TAM**: Total Addressable Market.
- **TTM**: Trailing Twelve Months.
- **Upside/Downside Modifier (Expected-Return Modifier)**: The additive ±15 adjustment based on expected annual return vs. the 10% hurdle.
- **Valuation Score**: This framework's 0.0–100.0 score (lower = cheaper) combining the Phase 02 sub-scores, Rate Gate, and Upside/Downside Modifier.

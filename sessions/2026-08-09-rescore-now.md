# RESCORE — NOW (ServiceNow, Inc.)

**Task type:** RESCORE (single ticker, mode `--both`)
**Trigger:** [GitHub issue #361](https://github.com/cloxy777/investment-framework/issues/361) — "RESCORE: NOW - earnings released 2026-07-22." Overdue: earnings released 22 Jul 2026, this session runs 2026-08-09 (18 calendar days later, well past the "within 3 business days" operating-calendar target).
**Date:** 2026-08-09 (Sunday — markets closed; most recent trading session 2026-08-07)
**10Y US Treasury Yield:** 4.66% (Yahoo `^TNX` `regularMarketPrice`, 2026-08-07 close; prior close 4.67%) — up from 4.49% (07-05), still inside the same 3.5–5% bracket. Consistent with the 2026-08-07 UBER session's same-week reading (4.656%).
**Rate Regime Modifier (Step 2):** +5 (unchanged bracket)
**Last review on record:** NOW **Valuation 61.3 · Quality 78.7 (FAILS 80.0+ gate) · Composite 41.3 (reference only, not adopted)** — 2026-07-05, [sessions/2026-07-05-rescore-now.md](2026-07-05-rescore-now.md). Action: HOLD existing 2.16–2.19% position, no add (R/R independently failed 2:1 anyway).
**Current NOW portfolio weight:** 2.19% per [holdings.md](../portfolio/holdings.md) (as of the 2026-08-02 combined-broker sync) — recomputed informally below using this session's live price for context only (weight refresh is `/sync-portfolio`'s job, not this session's).

**Rule 0 data-fetch note:** `yfinance` failed in-sandbox this session with the same recurring `curl_cffi` TLS-impersonation/connection-reset failure documented across many prior sessions (most recently the 2026-08-07 UBER session). Worked around per Rule 0's documented contingency: plain `requests` (using the sandbox's CA bundle, which the proxy already injects via `REQUESTS_CA_BUNDLE`) hitting Yahoo Finance's `quoteSummary` and `fundamentals-timeseries` endpoints directly (session-warmed cookie + crumb from `query2.finance.yahoo.com`), cross-checked against IBKR for the live price and confirmed against ServiceNow's own SEC 10-Q (via `WebFetch`) for the balance-sheet figures below. All figures trace to these primary/near-primary sources, not to any single vendor field taken uncritically.

> *Jargon decoded on first use — see closing Glossary section.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$124.88** | IBKR `get_price_history` (contract_id 109911821, NYSE), most recent daily bar close = **2026-08-07** (Friday; today, 2026-08-09, is a Sunday with markets closed). Cross-checked exactly against Yahoo Finance `regularMarketPrice` ($124.88, `marketState: CLOSED`). |
| ⚠️ Tooling flag | IBKR `get_price_snapshot`'s `last` field returned **$124.75** (real-time tick, `is_close: false`) — a small, immaterial (~$0.13, 0.1%) discrepancy from the confirmed Friday close, the same recurring stale/off-tick-snapshot pattern flagged in prior NOW/MSFT/AVGO sessions. Resolved using the confirmed daily-bar close, cross-validated by two independent sources (IBKR history bar + Yahoo). |
| 52-week range | $81.24 – $194.73 | Yahoo `summaryDetail` (`fiftyTwoWeekLow`/`fiftyTwoWeekHigh`); IBKR `misc_statistics` 52w low $81.25/high $194.60, consistent within rounding. |
| Change vs. Friday's prior close ($117.35) | **+6.42%** intraday on the earnings/quarter-context rally that began 22 Jul and continued through this week | Yahoo `price.regularMarketChangePercent` |
| Analyst consensus PT | mean **$140.25**, median $140.00, range $72–$248, n=46, "Strong Buy" (recommendation mean 1.47) | Yahoo `financialData` — bull-case sanity check only (Rule 0 Step 4), not a scored input. |
| Price vs. 07-05 review ($106.32) | **+17.46%** | Explained by a real, documented fundamental trigger (Q2 FY2026 earnings beat + raised guidance, §2) — not an "unexplained" Rule 9 move, though it is itself the earnings-release Rule 9 trigger this session is responding to. |

---

## 2. Rule 9 Trigger Check (2026-07-05 → 2026-08-09)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | **YES — the trigger for this session.** | Q2 FY2026 results released 22 Jul 2026 after close. Total revenue $3,987M (+24% YoY, +22.5% CC); subscription revenue $3,877M (+24.5% YoY, +23% CC), beating the high end of guidance by 150bps. RPO $29.0B (+21% YoY CC); cRPO $13.20B (+21% YoY). AI ACV crossed $1B; 123 deals >$1M net-new ACV (+40% YoY); 658 customers with $5M+ ACV. Source: [ServiceNow Q2 2026 press release](https://investor.servicenow.com/news/news-details/2026/ServiceNow-Reports-Second-Quarter-2026-Financial-Results/default.aspx), [SEC 8-K exhibit](https://www.sec.gov/Archives/edgar/data/1373715/000137371526000072/erq2fy26.htm). |
| Guidance revision | **YES.** | FY2026 subscription revenue guidance raised to **$15.760–$15.780B** (+21% CC), up modestly from the 07-05 session's on-record $15.735–$15.775B. Q3 2026 subscription guidance issued: $3.975–$3.980B (+20% CC). An upward, not downward, revision — reinforces rather than undercuts the growth thesis. |
| M&A | No new deal this window; **but a major financing/balance-sheet consequence of the already-known Armis deal newly shows up in this session's data** — see §3 flag 1 and §4. Armis itself closed 20 Apr 2026, before the 07-05 review (not new); the **debt used to fund it, and its partial refinancing, both completed and settled onto the balance sheet between the 07-05 review and this session's Q2-end data** (Term Loan drawn April 2026, senior notes issued/Term Loan repaid May 2026) — this is genuinely new information this session, even though the underlying acquisition was already known. |
| Management change | No | None found. |
| Macro shift | No bracket change | 10Y ticked from 4.49% (07-05) to 4.66% (08-09) — still inside the "3.5–5%" bracket, no Rate Regime Modifier change. |
| >15% unexplained price move | **+17.46% since 07-05, but explained** | The move coincides with, and is consistent in direction/magnitude with, the confirmed Q2 earnings beat and guidance raise above — not an *unexplained* move, so this doesn't independently fire as a separate trigger beyond the earnings release itself. |

**Conclusion: this session is triggered by (a) the scheduled Q2 FY2026 earnings release (the GitHub issue's own basis) and (b) an independent guidance revision, both legitimate Rule 9 events. The balance-sheet financing item in §3/§4 is folded into the same data refresh, not treated as a separate trigger.**

---

## 3. Data Gaps / Flags

1. **Material balance-sheet shift: net cash → net debt, driven by the Armis-acquisition Term Loan and its May 2026 refinancing.** Per ServiceNow's own 10-Q (Note 11, confirmed via direct SEC filing fetch, not a vendor field taken uncritically):
   - **April 2026:** ServiceNow borrowed **$4.0B** under a senior unsecured Term Loan to fund the ~$7.8B Armis acquisition.
   - **May 2026:** ServiceNow issued **$4.0B** of five-series fixed-rate senior unsecured notes (4.25% due 2028 / 4.70% due 2031 / 5.05% due 2033 / 5.40% due 2036 / 6.30% due 2056; net proceeds $3.9B) and used the proceeds to repay the Term Loan.
   - **Balance as of 2026-06-30 (10-Q):** short-term debt, net $2,082M + long-term debt, net $5,435M = **$7,517M total debt** (up from $2,431M at 2026-03-31, the figure used in the 07-05 session). Cash & cash equivalents $2,503M + short-term marketable securities $2,161M = **$4,664M** (matches Yahoo `financialData.totalCash` exactly, confirming this is the right "cash + ST investments" basis — the same convention used every prior NOW session).
   - **Net Debt = $7,517M − $4,664M = $2,853M** — a swing of **~$5.6B** from the 07-05 session's **−$2,751M (net cash)** position. This is a real, disclosed, primary-source-confirmed capital-structure change, not a data artifact — flagged prominently because it materially affects both the Balance Sheet Quality sub-score (§5) and EV/EBIT (§7) this session.
   - *Sensitivity note:* Yahoo's own directly-reported `quarterlyNetDebt` field returned $5,014M and its `enterpriseValue`-implied net debt was $3,789M — neither matches the 10-Q-sourced $2,853M used here, the same kind of cross-source net-debt reconciliation gap flagged in the 2026-08-07 UBER session. **This session uses the SEC 10-Q-sourced figure ($2,853M) as primary** since it traces to the filed balance sheet directly (Rule 0's spirit of primary-source verification), not a vendor-computed aggregate.
2. **PEG / Fast-Grower eligibility — still not qualifying, unchanged from every prior NOW session.** FY2022–2025 diluted EPS ($0.32 → $1.684 → $1.368 → $1.67) is unchanged this session — still shows the FY2023 one-off **deferred tax valuation allowance release** spike followed by an FY2024 decline, not a clean 3-year >15%/yr GAAP earnings base. PEG stays **Not Applicable**; its 15% weight redistributed to EV/EBIT (→ 40%), consistent with every prior NOW session.
3. **5yr avg/range Forward-PE — not recomputed this session; carried forward from 07-05 (67.78× avg, 23.10×–122.80× range), flagged as a genuine data gap, not silently reused.** The framework's documented method (`get_earnings_dates` + price-history reconstruction, ~20 quarters) requires `yfinance`, which failed (see header). The `requests`-based fallback's `fundamentals-timeseries` endpoint caps quarterly history at **5 quarters** regardless of the requested date range (confirmed by direct test this session) — far short of the ~20 quarters needed for a 5-year reconstruction, so it cannot substitute. Reusing the 07-05 figure (35 days old, same underlying ~5-year window minus one incremental quarter) is judged a defensible, documented carry-forward under Rule 6 rather than an invented estimate — but it is explicitly flagged, not silently treated as fresh.
4. **Moat Signal checklist carried forward unchanged from 07-05**, not independently re-verified this session (time/tooling constraints) — same open item pattern flagged for UBER's market-share citation (2026-08-07 session: "still March 2024... over two years stale"). Nothing in this session's Q2 data packet contradicts the prior determination (3 of 5 signals TRUE: market share, brand premium, switching costs; FALSE: network effect, scale cost advantage), but it is not re-derived from fresh evidence here — flagged as an open item for the next pass.
5. **`operatingMargins` field discrepancy (not used).** Yahoo's `financialData.operatingMargins` (TTM) reads 4.06%, wildly inconsistent with this session's EBIT-based figure (TTM EBIT $2,429M ÷ TTM Revenue $14,732M = 16.48%). The EBIT figure used throughout this session (§4) is the same `quarterly EBIT` time-series field used in every prior NOW session — its Q2'25–Q1'26 quarterly values ($477M/$700M/$546M/$679M) match the 07-05 session's figures for the same quarters exactly, confirming continuity of methodology. `operatingMargins` is flagged as an inconsistent/differently-scoped Yahoo field and **not used**.
6. **D&A jumped sharply in Q2 2026** ($258M in Q1'26 → $407M in Q2'26) — almost certainly the amortization of Armis's acquired intangible assets beginning to run through the income statement post-close (a normal, expected purchase-accounting consequence of a $7.8B deal, not an anomaly). Included as-is in EBITDA (§4); not adjusted out, since D&A is an ordinary (not one-off/restructuring) operating item under Rule 6.
7. **Shareholder yield refreshed this session:** no dividend. Net buyback yield from TTM-ending diluted-average-share change: 1,045M (TTM-ending Q2'25) → 1,034M (TTM-ending Q2'26) = **+1.05%** net share-count reduction (buybacks continuing to outpace SBC-driven dilution, consistent with the trend flagged in 07-05).

No data was invented anywhere below. Every fallback/flag above is the documented one from the framework, not an ad hoc substitute.

---

## 4. NOW — Inputs Collected (this session; Yahoo `fundamentals-timeseries` + `quoteSummary`, cross-checked against ServiceNow's Q2 FY2026 10-Q)

**Sector:** Technology — Enterprise Software (Workflow Automation / SaaS, ITSM)

| Item | Value | Source |
|---|---|---|
| Shares outstanding | 1,033,862,000 | Yahoo `defaultKeyStatistics.sharesOutstanding` |
| **Market Cap** | 1,033,862,000 × $124.88 = **$129,108.69M** | Computed — matches Yahoo `marketCap` ($129,108,688,896) essentially exactly |
| Total debt (2026-06-30, short + long, net) | $2,082M + $5,435M = **$7,517M** | ServiceNow 10-Q balance sheet (SEC, direct fetch), §3 flag 1 |
| Cash + ST investments (2026-06-30) | $2,503M + $2,161M = **$4,664M** | Same 10-Q; matches Yahoo `financialData.totalCash` exactly |
| **Net Debt** | $7,517M − $4,664M = **$2,853M (net debt — flipped from net cash)** | Computed, §3 flag 1 |
| **EV** | $129,108.69M + $2,853M = **$131,961.69M** | Computed |
| TTM EBIT (Q3'25–Q2'26) | $700M + $546M + $679M + $504M = **$2,429M** | `yfinance`-equivalent quarterly-EBIT series (`fundamentals-timeseries`), continuity-verified vs. 07-05, §3 flag 5 |
| TTM Operating Cash Flow | $813M + $2,238M + $1,670M + $587M = $5,308M | Same, matches Yahoo `financialData.operatingCashflow` exactly |
| TTM CapEx | $244M + $238M + $141M + $114M = $737M | Same |
| **TTM FCF** (OCF − CapEx) | $5,308M − $737M = **$4,571M** | Computed — a small vendor-aggregate discrepancy exists (Yahoo's own `freeCashflow` field reads $5,149M) but the bottom-up OCF−CapEx figure is used, per this framework's continuity practice |
| TTM Net Income | $502M + $401M + $469M + $298M = **$1,670M** | Matches Yahoo `netIncomeToCommon` exactly |
| TTM Revenue | $3,407M + $3,568M + $3,770M + $3,987M = **$14,732M** | Matches Yahoo `totalRevenue` exactly |
| Net Margin (TTM) | 11.336% | Computed — exact match to Yahoo `profitMargins` (0.11336) |
| TTM Pretax Income / Tax Provision | $2,346M / $676M | Quarterly rollforward |
| Effective tax rate (TTM) | 676/2,346 = **28.815%** | Computed |
| TTM D&A | $194M+$212M+$258M+$407M = $1,071M | Quarterly rollforward, §3 flag 6 |
| EBITDA (TTM) | $2,429M + $1,071M = $3,500M | Computed |
| **Net Debt/EBITDA (TTM)** | $2,853M ÷ $3,500M = **0.815× (net debt, no longer net cash)** | Computed |
| Gross Margin (TTM) | 11,015/14,732 = **74.77%** | Computed — exact match to Yahoo `grossMargins` (0.74769) |
| Revenue 3yr CAGR (FY2022 $7.245B → FY2025 $13.278B) | (13.278/7.245)^(1/3)−1 = **22.38%** | Unchanged annual figures from 07-05 |
| Forward EPS (NTM) | $5.00619 | Yahoo `defaultKeyStatistics.forwardEps` |
| **Forward PE** | $124.88 ÷ $5.00619 = **24.945×** | Computed — matches Yahoo `forwardPE` (24.945118) |
| 5yr avg/range PE | avg **67.78×**, range **23.10×–122.80×** — **carried forward from 07-05, not recomputed**, §3 flag 3 | Data-gap flagged |
| FCF/NI conversion (TTM) | 4,571/1,670 = **273.7%** | Computed — high-quality, consistent with FY2022–2025 annual ratios of 156–669% |
| Total Stockholders' Equity (2026-06-30) | $12,516M | ServiceNow 10-Q |
| **Invested Capital** (Debt+Equity convention) | $7,517M + $12,516M = **$20,033M** | Computed |
| **NOPAT** | $2,429M × (1−0.28815) = **$1,729.1M** | Computed |
| **ROIC (TTM)** | $1,729.1M ÷ $20,033M = **8.63%** | Computed — down materially from 07-05's 12.53%, driven by the much larger invested-capital base post-debt-raise, not a NOPAT decline (NOPAT actually rose slightly) |
| Diluted avg shares (TTM-ending-Q2'26 vs. Q2'25) | 1,034M vs. 1,045M | Net buyback yield ≈ **+1.05%**, §3 flag 7 |
| Dividend yield | None (no dividend) | Yahoo |

---

## 5. NOW — Quality Score (2026-06-29 methodology)

**Hard disqualifier check (all must pass before the weighted score matters):**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs unexplained? | Annual FY2022–2025: 668.6% / 156.0% / 236.8% / 259.3% — all comfortably ≥70% every year; TTM 273.7% | disqualify if <70% for 2+ yrs *without* explanation | ✅ PASS |
| Net Debt/EBITDA over threshold? | **0.815× (net debt now, up from net cash)** | disqualify if >2.5× (standard; NOW is not an asset-light payment network/exchange, so the 4× Upgrade 5 override does not apply) | ✅ PASS, comfortably, despite the balance-sheet shift |
| FCF-positive 3+ consecutive years? | FCF-positive every year on record (FY2022–2025 and TTM) | disqualify if not | ✅ PASS |

No hard disqualifier triggers, even with the new debt load. Proceeding to the weighted score.

### Profitability (25% weight)

```
Net Margin (TTM)    = $1,670M / $14,732M = 11.336%
NetMargin_Component = clamp((11.336/30)×100, 0, 100) = 37.79

ROIC (TTM)           = $1,729.1M / $20,033M = 8.63%
ROIC_Component       = clamp((8.63/30)×100, 0, 100) = 28.77

Profitability_Score  = (37.79 + 28.77) / 2 = 33.28   (no FCF cap — FCF-positive every year on record)
```
**Down sharply from 07-05's 41.86** — the entire drop is the ROIC component (41.77 → 28.77), diluted by the ~$18B increase in invested capital from the Armis-related debt, even though NOPAT itself rose modestly ($1,773.8M → $1,729.1M is actually a slight *decline*, not a rise — see note: the effective tax rate rose from 26.15% to 28.815%, more than offsetting EBIT growth).

### Margins (15% weight)

```
Gross Margin (TTM) = 74.77%
GrossMargin_Score = clamp((74.77/80)×100, 0, 100) = 93.46
```
Down modestly from 07-05's 95.70 (76.56% → 74.77%, a 1.79pp decline) — below the 3pp structural-break threshold that would trigger a Rule 3 sell-trigger flag, but worth watching next quarter. No trend bonus applicable (already well above the 40% threshold the bonus targets).

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $7.245B → FY2025 $13.278B) = 22.38%
Growth_Score = clamp((22.38/25)×100, 0, 100) = 89.51
```
**+10 (documented TAM expansion / pricing power, cited, refreshed this session):**
- Q2 FY2026: AI ACV **crossed $1B** (on track toward the $1.5B FY2026 target set at Investor Day, still not yet fully realized); RPO $29.0B (+21% YoY CC); cRPO $13.20B (+21% YoY); 123 deals >$1M net-new ACV, **+40% YoY**; 658 customers with $5M+ ACV.
- FY2026 subscription revenue guidance **raised** (again) to $15.760–$15.780B (+21% CC) — the second consecutive guidance raise this framework has tracked for NOW.

Real, cited, company-disclosed evidence of continued market/product-line expansion — no deceleration evidence exists (guidance raised, not cut).
```
Growth_Score (with bonus) = clamp(89.51 + 10, 0, 100) = 99.51
```

### Balance Sheet (15% weight)

```
Net Debt/EBITDA = 0.815×  (net debt, flipped from net cash)
BalanceSheet_Score = clamp(100×(1 − 0.815/4), 0, 100) = clamp(79.62, 0, 100) = 79.62
```
**Down sharply from 07-05's 100.0 (net-cash ceiling) to 79.62** — the direct, mechanical consequence of the Armis-financing balance-sheet shift (§3 flag 1, §4). Standard /4 denominator applies — NOW is not a payment network/exchange, so the Upgrade 5 asset-light override doesn't apply.

### Moat Signal (15% weight) — carried forward from 07-05, not re-verified this session (§3 flag 4)

| Signal | Marked | Basis |
|---|---|---|
| Market share stable/growing | **TRUE** | Carried forward: Gartner Magic Quadrant leadership (ITSM, 9 consecutive years; sole Leader in AI Applications for ITSM, 2nd consecutive year as Leader); No. 1 in six Gartner segments. |
| Brand premium | **TRUE** | Carried forward: 3–7% standard annual price escalators; Now Assist AI add-on priced $15–75/user/month on top of base licensing, with accelerating adoption. |
| Network effect | **FALSE** | Carried forward: no documented two-sided-marketplace mechanism for the core ITSM/workflow platform. |
| Switching costs | **TRUE** | Carried forward: the CMDB (Configuration Management Database) as deeply-embedded IT-estate system of record. |
| Scale cost advantage | **FALSE** | Carried forward: no cost-per-unit citation found vs. smaller ITSM competitors. |

```
Moat_Score = (3/5) × 100 = 60.0
```

### FCF Quality (10% weight)

```
FCF/NI (TTM) = $4,571M / $1,670M = 273.7%
FCFQuality_Score = clamp(((2.737 − 0.40)/0.60)×100, 0, 100) = clamp(389.5, 0, 100) = 100.0
```

### Quality Score — Final

```
Quality Score = (33.28×0.25) + (93.46×0.15) + (99.51×0.20) + (79.62×0.15) + (60.0×0.15) + (100.0×0.10)
              = 8.320 + 14.019 + 19.902 + 11.943 + 9.000 + 10.000
              = 73.184 → rounds to 73.2
```

# Quality Score = 73.2 — FAILS the 80.0+ gate, and more decisively than 07-05.

**This is a materially worse result than the 07-05 session's 78.7, and — importantly — no longer a "one judgment call away from passing."** Recomputing with the most generous possible Moat Signal reading (4/5 = 80.0, crediting either Network Effect or Scale Cost Advantage) still only yields **76.2** — still short of the 80.0 gate. The 07-05 session's "sensitive to one moat judgment call, 78.7 vs. 81.7" framing **no longer applies**: this quarter's Quality Score failure is now robust to that ambiguity, driven almost entirely by the real capital-structure shift (Profitability_Score 41.86→33.28, BalanceSheet_Score 100.0→79.62) rather than a qualitative judgment call. Per [quality-scoring.md](../framework/quality-scoring.md) and [rescore.md](../.claude/commands/rescore.md) step 3: a held position's Quality Score failing the gate is a **Phase 04 Quality Watch escalation**, not a forced exit (quality-gate failure alone is not one of strategy.md's four valid Phase 06 exit reasons). The Valuation Score and a **reference-only** Composite Score are still computed below, per NOW's own established practice (06-20/07-05 sessions).

---

## 6. NOW — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 24.945 = 4.0088%
Spread = EY − 10Y Treasury = 4.0088% − 4.66% = −0.6512%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (−0.6512%, ~2.15pp short) → **+5 additive**.

**Step 2 — Rate Regime Modifier**
10Y = 4.66% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for NOW = +10**

---

## 7. NOW — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF_Yield% = $4,571M / $129,108.69M = 3.5405%
FCF_Score = clamp(100 × (1 − 3.5405/10), 0, 100) = 64.595
```
→ Contribution: 64.595 × 0.40 = **25.838**

**EV/EBIT — 25% + 15% (PEG redistributed, §3 flag 2) = 40% weight**
```
EV/EBIT = $131,961.69M / $2,429M = 54.328×
EV/EBIT_Score = clamp((54.328 − 12)/23 × 100, 0, 100) = clamp(184.0, 0, 100) = 100.0
```
→ Contribution: 100.0 × 0.40 = **40.0** (still saturated at ceiling — the EV/EBIT multiple got even richer this session: 44.50× → 54.33×, both the price rally and the new debt pushed EV up while EBIT grew only modestly)

**Forward PE (fallback formula — 5yr avg, carried forward per §3 flag 3) — 20% weight**
```
Deviation% = (24.945 − 67.78)/67.78 × 100 = −63.20%
FwdPE_Score = clamp(50 + (−63.20)×2.5, 0, 100) = clamp(−108.0, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — 15% weight: N/A this session** (not a qualifying Fast Grower, §3 flag 2) — weight redistributed to EV/EBIT above.

**Raw weighted score:**
```
= 25.838 + 40.0 + 0.0 = 65.838
```
**+ Rate Modifier (+10) = 75.838** (before the Upside/Downside Modifier)

---

## 8. NOW — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario architecture rebuilt this session** (not mechanically carried forward), given the material capital-structure change (§3 flag 1) and fresh Q2 data — using the current NTM consensus forward EPS ($5.006) as the base-case anchor and haircutting the exit multiples further than 07-05 to reflect both (a) the ongoing SaaS de-rating regime and (b) this session's real Quality Score decline (78.7 → 73.2):

| Scenario | Weight | EPS | Exit PE | Rationale | Fair Value |
|---|---|---|---|---|---|
| **Bull** | 25% | $5.35 | 28× | AI monetization continues toward the $1.5B FY26 ACV target (already crossed $1B, +40% YoY net-new $1M+ deal growth); Armis cross-sell accelerates faster than guided. Exit multiple stays below the analyst-implied 28.02× (mean PT $140.25 ÷ fwd EPS $5.006) — not the rosy point (Guardrail 2) — and far below the 67.78× 5yr average. | $5.35 × 26 = **$139.10** |
| **Base** | 50% | $5.006 (= current NTM consensus forward EPS) | 20× | Consensus ~20–21% CC subscription growth (per raised guidance) continues; exit multiple haircut vs. 07-05's 22× reflects both the persistent SaaS de-rating regime and this session's real balance-sheet/Quality Score deterioration (net cash → net debt, Quality Score 78.7→73.2) — a documented, not arbitrary, basis for the more conservative multiple. | $5.006 × 20 = **$100.12** |
| **Bear** | 25% | $4.60 | 15× | Growth decelerates toward high-teens; Armis integration costs/dis-synergies linger past the FY2027 normalization management has guided to; de-rating persists near the 52-week-low-implied multiple. | $4.60 × 15 = **$69.00** |

```
PW Fair Value = 0.25×139.10 + 0.50×100.12 + 0.25×69.00 = 34.775 + 50.06 + 17.25 = $102.09
```
Sits well below the $140.25 analyst consensus mean — conservative, sanity check passes (Guardrail 2).

**Robustness check (Guardrail 3 spirit — showing this isn't an artifact of the multiple haircut):** re-running with 07-05's *unchanged* multiples (Bull 28×, Base 22×, Bear 17×) instead gives PW FV = $112.07, Gap = −10.26%, E = +13.92%, M = −3.92, Final = 65.838+10−3.92 = **71.9** — still lands in the 70.0–79.9 Trim band, just less deep. **The conclusion (Valuation Score crossing from Hold into Trim territory) is robust to this session's specific multiple choice, not an artifact of it.**

**Step 1 — Expected annual return E (primary calc, this session's multiples).**
```
Gap Upside %     = ($102.09 ÷ $124.88) − 1              = −18.25%   (price now trades ABOVE the
                                                                       scenario-weighted fair value —
                                                                       the opposite sign from 07-05's +6.75%)
Catalyst window  = 2 years (unchanged — AI/Now Assist monetization ramp + Armis integration
                   normalizing by FY2027, both within Rule 10's 18–24mo window)
Annualized gap   = −18.25% ÷ 2                            = −9.13%
Intrinsic growth = +18%/yr   (kept below the raised 20–21% CC subscription guidance, conservative,
                   unchanged basis from prior sessions)
Shareholder yield = +1.05%   (refreshed this session, §3 flag 7 — net buyback, no dividend)

E = −9.13% + 18% + 1.05% = +9.93%
```

**Step 2 — Map E to the modifier (hurdle H = 10%).**
```
E = 9.93% < H (10%), E ≥ 0 → M = +5 × (H − E)/H = +5 × (10 − 9.93)/10 = +5 × 0.007 = +0.04
```
**Modifier M = +0.04** — essentially neutral. A striking reversal from 07-05's −11.857 (materially attractive): the ~17.5% price rally since 07-05 outran this session's (now more conservative, and for good documented reason) fair-value estimate, flipping the gap from positive to negative, while intrinsic growth and shareholder yield stayed roughly flat. The modifier landing this close to its neutral pivot (E≈H) is a genuine output of the inputs above, not engineered to land there.

**Guardrail checks:**
1. **Catalyst:** documented (Now Assist/AI-monetization ramp, Armis integration normalizing FY2027), within 18–24 months. Not binding here since M is barely positive, well within [−15,+15] regardless. ✓
2. **Scenario-weighted, not the rosy point:** PW FV ($102.09) sits well below the $140.25 analyst consensus mean; Bull exit multiple (26×) kept below the analyst-implied 28.02×. ✓
3. **Full calc shown** (above), plus an explicit robustness check against last session's multiples. ✓
4. **Bounded ±15:** +0.04 sits well within bounds. ✓

---

## 9. NOW — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE = Raw weighted (65.838) + Rate Modifier (+10) + Upside/Downside (+0.04)
                       = 75.878
```
Boundary rule: not a ".X5" case → standard rounding → **Final Valuation Score = 75.9**

| | Value |
|---|---|
| Raw weighted | 65.838 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | +0.04 (E = +9.93%) |
| **FINAL VALUATION SCORE** | **75.9** |
| Prior valuation score | 61.3 (07-05) |
| **Quality Score** | **73.2 (FAILS 80.0+ gate — robustly, not sensitivity-dependent, see §5)** |

**Valuation Score band: 75.9 → 70.0–79.9 "Expensive" → TRIM 25–30% of position.** This is a full band change from 07-05's 61.3 ("Fair Value" / Hold) — the raw Valuation Score, independent of the Quality Score question, now sits in the Trim band for the first time in this name's session history.

**Composite Score — reference only, per NOW's own established practice (06-20/07-05 sessions) for a held position whose Quality Score fails the gate:**
```
Composite Score = 0.50×(100 − 73.2) + 0.50×75.9 = 0.50×26.8 + 0.50×75.9 = 13.4 + 37.95 = 51.35
```
Boundary rule: exactly on a ".X5" → **round UP** → **Composite Score = 51.4**

**Composite Score = 51.4 — lands in the "HOLD — watch only" band (50.0–69.9), a full band *more relaxed* than the raw Valuation Score's own "Trim 25–30%" read.** This is the **opposite-direction** false-signal pattern from 07-05 (where blending in the failed Quality Score made the number look *more* attractive/cheap than warranted): here, inverting the failed Quality Score (100−73.2=26.8, a moderately low "attractiveness" contribution) pulls the blended number *down* enough to mask the raw Trim signal underneath. **Per this framework's own explicit text — "Composite Score... doesn't rescue a company failing the quality gate" (quality-scoring.md) — and per NOW's own repeated precedent (06-20, 07-05) of treating the raw Valuation Score as binding when the Quality Score fails the gate, the Composite Score is NOT adopted to drive the action below.** (Flagged explicitly: at least one other ticker in this book — AMZN, 2026-07-04 session — chose the opposite convention, letting a failed-gate Composite Score govern and mute a raw Trim signal into a Hold. This is a genuine, unresolved cross-session inconsistency worth a `decisions/` entry; not resolved here, but NOW's own direct precedent is followed for continuity.)

---

## 10. NOW — Action Recommendation & Order Setup

**Action: TRIM 25–30% of the position**, per the raw Valuation Score (75.9, 70.0–79.9 band), independent of the Composite Score's masked Hold read (§9).

### Fair Value — two methods, triangulated (Rule 1: Tech/Growth sector → DCF primary, multiples secondary)

**Method A — 3-Stage DCF (Rule 2).**
```
WACC build:
  Cost of equity = Rf (4.66%) + Beta (0.93) × ERP (5.0%, assumed) = 9.31%
  Cost of debt (pretax) = weighted-avg coupon of the new $4.0B senior-notes tranche (the best available
    current market-rate proxy for NOW's now-much-larger debt stack) = 5.191%; after-tax (28.815%) = 3.70%
  Weights: E/(D+E) = 94.50% (Market Cap $129,108.69M), D/(D+E) = 5.50% (Total Debt $7,517M)
  WACC = 94.50%×9.31% + 5.50%×3.70% = 8.798% + 0.204% = 9.00%

Stage 1 (yrs 1–5), FCF Year 0 = $4,571M (TTM), taper 19%→17%→15%→13%→11% (below the 20-21% CC
  subscription-revenue guidance, reflecting FCF's typically slower/lagged conversion of subscription growth):
  y1 $5,439.5M | y2 $6,364.2M | y3 $7,318.8M | y4 $8,270.3M | y5 $9,180.0M

Stage 2 (yrs 6–10), fade from 9.0% to the 2.5% terminal rate:
  y6 $10,006.2M | y7 $10,744.2M | y8 $11,362.0M | y9 $11,830.6M | y10 $12,126.4M

Terminal Value (at y10) = $12,126.4M × 1.025 / (0.0900 − 0.025) = $191,192.1M
PV of Terminal Value (at 9.00% WACC, 10yr) = $80,753.5M
Terminal Value as % of total DCF EV = 59.1% (under the 75% Rule 4 sanity cap — no Stage 2 extension needed)

Sum of discounted FCFs (yrs 1–10) = $55,936.1M
Enterprise Value (DCF) = $55,936.1M + $80,753.5M = $136,689.6M
Equity Value = $136,689.6M − Net Debt $2,853M = $133,836.6M
DCF Fair Value / share = $133,836.6M / 1,033,862,000 = $129.45
```

**Method B — Scenario-weighted multiples (the same PW Fair Value used for the Upside/Downside Modifier, §8): $102.09**

```
Triangulation (Rule 3, Tech/Growth weights): Blended FV = 40% × DCF + 60% × Multiples
                                            = 0.40 × $129.45 + 0.60 × $102.09
                                            = $51.78 + $61.25
                                            = $113.06
```

### Order Setup Checklist

```
[✓] Valuation Score (incl. Upside/Downside Mod):  75.9 — "Expensive" (70.0–79.9 band, Trim 25–30%)
[✓] Expected annual return E / catalyst window:   +9.93% / 2yr (feeds the Upside/Downside Modifier)
[✓] Upside/Downside Modifier applied:             +0.04 (near-neutral)
[✓] DCF Fair Value:                               $129.45
[✓] Multiples-Based Fair Value (PW):              $102.09
[✓] Blended Fair Value:                           $113.06
[ ] Buy Price / Stop Loss / R/R:                  N/A — this is a TRIM of an existing position, not a
    new entry; the 2:1 minimum R/R check (Rule 6/fair-value-methodology.md Step 6) governs entries, not
    exits, and is not applicable here.
[✓] PRIMARY SELL TARGET (trim execution reference): $113.06 (Blended FV) — already exceeded: live price
    $124.88 sits +10.46% above it.
[✓] BULL-CASE TRIM TARGET:                        $139.10 × 0.90 = $125.19 (essentially at today's price —
    not a meaningfully higher stretch target worth waiting for)
[✓] POSITION SIZE (trim): see below
```

Since live price ($124.88) already trades **above** both the Blended Fair Value ($113.06) and effectively at the Bull-Case Trim Target ($125.19), there is no reason to wait for a higher limit — **execute the trim at/near current market**, not at the (already-exceeded) lower Sell Target.

### Trim sizing

```
Current position: 12 shares (IBKR, contract_id 109911821), avg cost $92.799, market value
  12 × $124.88 = $1,498.56 at this session's live price
25–30% of position = 3.0–3.6 shares → round to whole shares: SELL 3 SHARES (25%, the conservative/
  attainable end of the band given the position's small absolute share count)
Remaining position after trim: 9 shares (75% of original)
Estimated proceeds: 3 × $124.88 ≈ $374.64 (before commissions/slippage; actual fill price will vary)
Estimated realized gain: 3 × ($124.88 − $92.799) ≈ $96.24 (before taxes/costs)
```

**Recommended execution:** a GTC limit sell order for 3 shares at or a few cents below the current bid (~$124.50–$124.88) — the position is small enough (12 shares total) that a single simple limit order is appropriate; no tiered/scaled structure is warranted at this size.

**Recycling note (Phase 05, strategy.md):** the framework recommends recycling trim proceeds into Score 0.0–29.9 names. Per [holdings.md](../portfolio/holdings.md), **ADBE (score 0.0)** is currently the only holding flagged as actionable-BUY with room to its target size — noted as a pointer only; actual capital-recycling execution across the book is `/rebalance`'s job, out of scope for this single-ticker rescore.

**Position cap check (Upgrade 7):** current weight 2.19% (07-05 sync basis); recomputed informally with this session's live price and position value ($1,498.56) against the 2026-08-02 combined-portfolio total (~$60,829.03) ≈ **2.46%** (context only — not authoritative until the next `/sync-portfolio`). Either figure is nowhere near the 15% hard cap — **not a binding constraint here**, and the trim (reducing weight further, to roughly 1.8–1.9%) moves it even further from the cap, not toward it.

**No Full Exit trigger:** margins are not structurally broken (74.77% TTM gross margin, only a 1.79pp QoQ dip, well under the 3pp Rule 3 structural-break threshold); ROIC (8.63%) remains comfortably above the ~9.00% WACC computed above is actually *slightly below* WACC this session — flagged explicitly as a genuine yellow flag (ROIC < WACC implies the marginal dollar of invested capital, including the new debt-funded Armis acquisition, is not yet earning its cost of capital) but not itself one of strategy.md's four Full Exit triggers (fundamental deterioration must be *structural*, not a single-quarter post-acquisition dip while integration is still normalizing per management's own FY2027 guidance); no balance sheet crisis (leverage is still moderate at 0.815× Net Debt/EBITDA, investment-grade-rated notes); Valuation Score (75.9) is well short of the 90.0–100.0 sustained-2-quarters Full Exit bar. This ROIC<WACC flag is the most important item to re-check at the next earnings print.

---

## 11. Next Review Trigger

- **Routine:** NOW Q3 FY2026 earnings, confirmed **28 Oct 2026** (Yahoo `calendarEvents.earnings.earningsDate`, estimate) — will refresh every TTM fundamental used here, and is the natural point to see whether ROIC recovers above WACC as Armis integration normalizes per management's FY2027 guidance.
- **Execute this session's trim** (sell 3 of 12 shares) — flagged for the human investor to place; no MCP tool in this repo places live orders.
- **Open item (elevated priority): ROIC (8.63%) now sits slightly below this session's own computed WACC (9.00%)** — watch closely next quarter; if this persists alongside continued margin compression, it would start to build a case for the "fundamental deterioration: ROIC below cost of capital" Full Exit trigger (not yet met — a single quarter mid-integration is not "structural").
- **Open item: Composite-vs-raw-Valuation-Score governance inconsistency** (§9) — NOW's own precedent (raw score governs when Quality Score fails the gate) diverges from AMZN's 2026-07-04 session (Composite governs even on a gate failure). Worth a `decisions/` entry to settle framework-wide, not resolved here.
- **Open item: Moat Signal checklist not re-verified this session** (§3 flag 4) — carried forward from 07-05; worth fresh citations next pass, especially given the Quality Score is now failing the gate by a wide-enough margin that even a full moat re-credit (80.0) wouldn't close the gap (§5) — lower priority than it was in 07-05 for that reason.
- **Open item: 5yr avg/range Forward-PE not recomputed this session** (§3 flag 3) — needs a working `yfinance`/`get_earnings_dates` environment or an alternative reconstruction method; carried forward again if the tooling issue persists.
- **Rule 9 triggers (standing):** further guidance revision, M&A, management change, a >15% unexplained price move, or the 28 Oct 2026 earnings print itself.

---

## Glossary

| Term | Meaning |
|---|---|
| **10-Q (Quarterly Report)** | The quarterly financial-disclosure report a US public company files with the SEC, containing unaudited (reviewed) financial statements — this session's primary source for ServiceNow's Q2 FY2026 balance sheet (debt, cash, equity) and its Term Loan/senior-notes financing note. |
| **ACV (Annual Contract Value)** | The annualized value of a signed customer contract at signing — ServiceNow's Now Assist AI product crossed $1B in ACV in Q2 2026, tracking toward a $1.5B FY2026 target. |
| **Beta** | A stock's sensitivity to overall market moves — used with the risk-free rate and Equity Risk Premium to estimate cost of equity in this session's DCF WACC build. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **CMDB (Configuration Management Database)** | ServiceNow's system of record cataloging an organization's IT assets/applications — the switching-cost Moat Signal mechanism, carried forward this session. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed for reference this session (51.4) but **not adopted** to drive the action, since it masks the raw Valuation Score's Trim signal (§9). |
| **cRPO** | Current Remaining Performance Obligations — the portion of RPO expected to be recognized as revenue within 12 months; see RPO below. |
| **D&A** | Depreciation & Amortization. |
| **DCF** | Discounted Cash Flow — a valuation method estimating a company's worth today by projecting and discounting its future cash flows; Method A of this session's fair-value work. |
| **Deferred tax valuation allowance release** | A one-off GAAP event that inflated NOW's FY2023 EPS — the reason PEG stays inapplicable (§3). |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EPS** | Earnings Per Share. |
| **Equity Risk Premium (ERP)** | The extra return equity investors demand over the risk-free rate — an assumed WACC input in this session's DCF. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield in the Rate Environment Gate. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years on a clean earnings base — NOW still doesn't qualify (§3). |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear, Rule 7). |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score — none triggered this session. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Invested Capital** | Debt + Equity put to work in a business — the ROIC denominator; grew ~$5.9B this session from the Armis-related debt. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying — not applicable to a TRIM of an existing position. |
| **Net Debt/EBITDA** | Leverage ratio — flipped from net cash (−0.849×) to net debt (0.815×) this session, the central new finding. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **NTM** | Next Twelve Months. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. NOW: 73.2 this session (fails the gate more robustly than 07-05's 78.7). |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter; an entry-only concept, N/A for this session's trim. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **Risk-free rate (Rf)** | The 10-Year Treasury yield, used as the base input to cost of equity in this session's DCF. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital; fell to 8.63% this session, now slightly below WACC. |
| **RPO (Remaining Performance Obligations)** | The total contracted-but-not-yet-recognized subscription/services revenue — $29.0B for NOW in Q2 2026 (+21% YoY CC), a forward demand/backlog metric cited as Growth sub-score evidence. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work. |
| **Rule 1–8, Rule 10 (10-Rule Fair Value Framework)** | The numbered rules in [fair-value-methodology.md](../framework/fair-value-methodology.md) governing sector-appropriate valuation method choice (Rule 1), the 3-stage DCF standard (Rule 2), the weighted "football field" blend of valuation methods (Rule 3), sanity-check protocols including the 75% terminal-value cap (Rule 4), comparable-company standards (Rule 5), normalizing one-off items before valuing (Rule 6), mandatory bull/base/bear scenario weighting (Rule 7), margin-of-safety discipline by confidence level (Rule 8), and separating intrinsic value from market price with a documented catalyst (Rule 10). Rule 9 (model-refresh triggers) has its own standalone glossary entry. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% unexplained stock-price move. |
| **SaaS (Software-as-a-Service)** | A software delivery model where customers pay a recurring subscription to access hosted software. |
| **Senior unsecured notes / Term Loan** | Two forms of corporate borrowing: a Term Loan is typically drawn from a bank/syndicate on negotiated terms (often used for speed, e.g. to fund an acquisition quickly); senior unsecured notes are bonds sold to public/institutional debt investors, typically at fixed coupons across several maturities. ServiceNow drew a $4.0B Term Loan in April 2026 to fund the Armis acquisition, then replaced it with $4.0B of senior unsecured notes (five maturities, 2028–2056) in May 2026 — the central balance-sheet event this session. |
| **Shareholder yield** | Dividend yield + net buyback yield combined; +1.05% for NOW this session (no dividend, net buybacks). |
| **TAM** | Total Addressable Market. |
| **Terminal Value** | In a multi-stage DCF, the value assigned to all cash flows beyond the explicit forecast period — 59.1% of this session's DCF EV, under the 75% Rule 4 sanity cap. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle; landed at a near-neutral +0.04 this session (down from 07-05's −11.86), the single biggest driver of the score's move into the Trim band. |
| **WACC** | Weighted Average Cost of Capital — 9.00% for NOW this session, used as the DCF discount rate; ROIC (8.63%) now sits fractionally below it, a flag worth tracking. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |

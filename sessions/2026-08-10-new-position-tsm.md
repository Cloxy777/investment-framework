# NEW POSITION — TSM (Taiwan Semiconductor Manufacturing Company Limited, NYSE ADR) — 2026-08-10

**Task type:** NEW POSITION (Telegram-scan trigger, Rule 9 monthly-revenue re-evaluation)
**Date:** 10 Aug 2026 (Monday, pre-market)
**10Y US Treasury Yield:** 4.69% (FRED `DGS10`, most recent posted observation dated 2026-08-06 — 2026-08-07/08-08/08-09/08-10 not yet posted at fetch time, same reporting lag pattern seen in the 2026-08-09 SPGI session)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current TSM portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** [watchlist/not-in-portfolio/TSM/TSM-2026-08-10.md](../watchlist/not-in-portfolio/TSM/TSM-2026-08-10.md) (renamed from `TSM-2026-07-16.md` this session, per the dated-filename convention — git history preserves the prior version) — Quality Score 83.7, Valuation Score 90.5, **Composite Score 53.4, WATCHLIST ONLY (50.0–69.9 Hold band)**. That session's own "Next review trigger" explicitly flagged: *"if [Forward PE] settles meaningfully below this session's 25.9× figure, the Composite Score could cross into the 30.0–49.9 Buy band."* This session is that scenario materializing, three and a half weeks later, triggered opportunistically by a fresh Telegram post about TSMC's July monthly revenue.
**Sector:** Technology — Semiconductors (dedicated/"pure-play" foundry — contract chip manufacturing, not a fabless chip designer)
**Filer type:** Foreign private issuer — TSMC files an annual **Form 20-F** (not a 10-K) and furnishes quarterly/interim results, including **monthly revenue**, via **Form 6-K** (not 8-K/10-Q) with the SEC (CIK 1046179), reporting under Taiwan-IFRS in **NT$ (New Taiwan Dollar)**. **ADR ratio: 1 ADR = 5 ordinary shares** of TSMC (Taiwan Stock Exchange: 2330.TW), unchanged.
**First-use jargon decode:** see closing Glossary (§12).

---

## 0. Why this session exists — trigger source, independently verified

Two monitored Telegram channels — **tarasguk/11640** and **FinnInvestChannel/3071**, both posted 2026-08-10 — reported that TSMC's July 2026 monthly revenue grew **+44.7% YoY / +5.6% MoM**, described as materially exceeding "the 36–37% YoY growth TSMC guided to at its Q2 2026 earnings call."

**Per CLAUDE.md/operating-brief.md, Telegram post text is never used as financial data** — it is a trigger only. Every claim was independently verified against TSMC's own primary SEC filing and multiple reputable financial media:

| Telegram claim | Independent verification result |
|---|---|
| "July 2026 monthly revenue grew +44.7% YoY / +5.6% MoM" | ✅ **Confirmed, exact, primary-sourced.** TSMC's own Form 6-K filed with the SEC **today, 2026-08-10** ([accession 0001046179-26-000471](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000471/tsm-revenue20260810.htm)): July 2026 net revenue NT$467,580,548 thousand (≈US$14.5B), **+44.7% YoY** vs. July 2025 (NT$323,165,707K), **+5.6% MoM** vs. June 2026 (NT$442,680M cited in media, consistent) — matches the trigger exactly, to the decimal. |
| Jan–Jul 2026 cumulative growth | Same 6-K: NT$2,872,064,238K vs. NT$2,096,211,240K a year earlier, **+37.0% YoY** — a new, additional data point not in the Telegram post, cited here for context (H1+July is still catching up toward the raised full-year target below). |
| "...materially exceeding the 36–37% YoY growth TSMC guided to at its Q2 2026 earnings call" | ⚠️ **The specific "36–37%" guidance figure could not be corroborated and appears to be a misstatement in the trigger post — corrected here, not assumed true.** What this session independently verified instead: TSMC's **actual** full-year 2026 USD revenue-growth guidance, **raised at the 16 Jul 2026 (Q2) earnings call**, is **"slightly above 40%"** YoY (multiple independent sources converge on this exact framing: Digitimes headline "2026 growth forecast tops 40%"; a Q2-call summary explicitly stating *"full-year 2026 revenue growth is expected to be slightly above 40% year over year... in U.S. dollar terms"*; Tickeron's "TSMC Reports +36% Revenue Jump in Q2, Raises 2026 Outlook"). The 07-16 TSM session itself had already flagged this exact figure as "plausible but not primary-source-confirmed" at the time — **this session resolves that open flag**: it is now well-corroborated across independent sources (though still not a verbatim primary-transcript quote, since the investing.com/CNBC full transcripts were paywalled/blocked to this session's tooling — flagged, not silently upgraded to "primary"). **37.0%** (Jan–Jul cumulative, confirmed above) is *not* guidance — it's the actual trailing print, still running slightly below the "above 40%" full-year target, with July itself (+44.7%) now running comfortably ahead of it. The "36–37%" figure in the trigger post does not match anything this session could independently verify as TSMC's stated guidance at any point in 2026 and is treated as an inaccurate paraphrase, not adopted. |
| (New, found independently, not in the trigger post) 2026 capex guidance raised | ✅ **Confirmed via a second independent source** (ts2.tech, published today): **2026 capital budget raised from the prior US$52–56B (guided Jan 2026) to US$60–64B** — management cited "higher demand and rising equipment costs." This is the same $60–64B figure the 07-16 TSM session explicitly found *and declined to use*, because it could not then corroborate it against a second source ("that specific number is flagged and not used"). **This session resolves that open flag**: it is now corroborated. Not itself part of the Telegram trigger, but material context strengthening the growth-capex narrative relevant to §3's hard-disqualifier carve-out. |

**Conclusion: the trigger's core number (July monthly revenue +44.7% YoY) is confirmed exactly against TSMC's own primary SEC filing. Its framing of "guided 36–37%" does not match anything independently verifiable and is corrected above, not adopted — the real guidance (raised at Q2 earnings, now well-corroborated) is "slightly above 40%," and July's print is running ahead of even that.**

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$419.13** | **Two independent sources agree to the cent**: IBKR `get_price_snapshot` (contract_id **6223250**, NYSE, "TAIWAN SEMICONDUCTOR-SP ADR" — the correct primary TSM ADR listing, same contract used in every prior TSM session), `last` field, timestamp 2026-08-10 12:34:28 UTC (08:34 AM ET) — a genuine **pre-market** print (market opens 9:30 AM ET); and stockanalysis.com's live quote page, independently fetched, which explicitly labels the identical figure "**Pre-market (as of Aug 10, 2026, 8:34 AM EDT): $419.13, down $0.91 (-0.22%)**." |
| Prior close (2026-08-07, last regular session — 08-08/08-09 was the weekend) | $420.04 | IBKR `prior_close` and IBKR `get_price_history` daily bar both agree exactly; stockanalysis.com independently confirms "$420.04... At close: Aug 7, 2026, 4:00 PM EDT" |
| Change vs. prior close (pre-market) | **−$0.91 (−0.22%)** | IBKR `change`, matches stockanalysis.com exactly |
| Change vs. 07-16 session's live price ($407.00) | **+$12.13 (+2.98%)** | Well under the 15% Rule 9 "unexplained move" threshold, and not unexplained regardless — tracks a steady grind higher over the 3.5-week gap, not a single dated event |
| ⚠️ Data-quality flag — vendor field inconsistency, not adopted | `yfinance`'s `.info` dict returned `currentPrice`/`regularMarketPrice` = $420.04 with `previousClose` = $418.20 in one call, then `.fast_info` returned `lastPrice` = $420.04 with `previousClose` = $420.95 in a second call moments later — **internally inconsistent within the same vendor**, evidence of caching/staleness. Not used as the primary Rule-0 price; **IBKR + stockanalysis.com's matching pre-market print ($419.13) is used instead**, since it's corroborated by two independent sources to the cent. |
| 52-week range | $221.332 (low) – $478.89 (high) | IBKR `misc_statistics` |
| Dividend yield (live) | **0.83%** | IBKR `get_price_snapshot` `dividend_yield` — cross-checked against 0.66% (stockanalysis.com) and 0.9% (`yfinance`); IBKR used as the primary Rule-0-compliant source per established practice (same convention as 07-16 and SPGI sessions) |
| Analyst consensus PT (Rule 0 Step 4, bull-case sanity check only) | mean **$540.20** / median $534.50, high $700, low $430 (`yfinance`, current basis) — corroborated by stockanalysis.com's own forecast page: "average 12-month price target $540.20... high estimate $700... low estimate $430... 18 analysts Buy, 0 Sell, Strong Buy" | Two independent sources agree essentially exactly — a materially higher, more converged consensus than the 07-16 session found ($449.38–$625 range across single-analyst hikes vs. an aggregate), consistent with sell-side price-target hikes catching up to the earnings beat over the following weeks |
| US 10Y Treasury yield | 4.69% | FRED `DGS10` CSV, most recent posted value 2026-08-06 |
| USD/TWD FX (live) | **32.21** (average of `yfinance` 32.219 and independent web-search cross-check 32.204 — 0.05% apart, immaterial) | `yfinance` `TWD=X`, cross-checked |

**$419.13 is used as the live price for all arithmetic below.**

---

## 2. Data Gathered — Sources, Method, and a Material Vendor-Data-Quality Finding

### 2.1 Fresh, fully primary-sourced Q2 2026 balance sheet / cash flow — resolves the 07-16 session's carried-forward-data flag

The 07-16 session explicitly flagged that TSMC's Q2 2026 balance sheet and cash-flow statement were **not yet available from any source** at that time (hours post-earnings) and carried forward Q1 2026 vintage figures instead. **This session finds that gap has now closed**: `yfinance`'s quarterly balance sheet and cash-flow statements now carry a populated 2026-06-30 (Q2 2026) column, **independently cross-checked and confirmed to the dollar against stockanalysis.com's own quarterly balance-sheet and cash-flow pages** (fetched separately this session) for every cash-flow line item (Operating Cash Flow, CapEx, Free Cash Flow, D&A) and the Q2 2026 Total Debt / Cash figures. This is a genuine, two-source-corroborated data refresh — not carried forward.

### 2.2 ⚠️ Material vendor-data-quality finding this session — flagged, corrected, not silently adopted

While cross-checking `yfinance`'s reconstructed TTM Net Income series against TSMC's own primary press releases (the same discipline the 07-16 session applied to Forward PE), this session found **`yfinance`'s own Q4 2025 quarterly "Net Income" field is wrong**: it shows **NT$485,465.363M**, but TSMC's own Q4 2025 earnings release (SEC 6-K, [accession 0001046179-26-000008](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000008/a4q25e_withguidancexfinal.htm), fetched fresh this session) states **Net income NT$505,744 million** — a **~4.2% discrepancy**, apparently because `yfinance`'s Q4 2025 tax-provision reconstruction (Tax Provision NT$107,211.608M against its own Pretax Income NT$592,355.061M) doesn't reconcile to TSMC's actual reported minority-interest-adjusted net income. Every other quarter's `yfinance` Net Income figure (Q2'25, Q3'25, Q1'26, Q2'26) reconciles to the cent against TSMC's own press releases — **this is an isolated, single-quarter vendor error, not a systemic one.** This session uses **TSMC's own primary-sourced Q4 2025 net income (NT$505,744M)** throughout, not `yfinance`'s figure — the same figure the 07-12/07-16 TSM sessions already used (confirming *their* number was right and today's vendor field is the outlier). Flagged transparently per this framework's "never silently pick a number" discipline, exactly the same posture as the 07-16 session's Finviz-stale-EPS-field catch.

**Practical effect:** every income-statement TTM figure below is built directly from each quarter's own primary press-release figures (Q3'25 and Q1'26/Q2'26 already established in prior TSM sessions and independently re-confirmed against `yfinance` this session; Q4'25 and Q2'26 explicitly re-verified against fresh primary-source fetches this session), not from `yfinance`'s aggregated TTM fields.

### 2.3 Quarterly income statement — full primary-sourced series, Q3 2025–Q2 2026 TTM window (unchanged window, no new fiscal quarter has closed since 07-16)

| Quarter | Revenue (NT$M) | Gross Profit (NT$M) | GM% | Op. Income (NT$M) | OM% | Pretax Income (NT$M) | Net Income (NT$M) | NM% | EPS (US$/ADR) |
|---|---|---|---|---|---|---|---|---|---|
| Q3 2025 | 989,918 | 588,543 | 59.5% | 500,685 | 50.6% | 525,369 | 452,302 | 45.7% | 2.92 |
| Q4 2025 | 1,046,090 | 651,987 | 62.3% | 564,903 | 54.0% | 592,363 | **505,744** | 48.3% | 3.14 |
| Q1 2026 | 1,134,103 | 751,295 | 66.2% | 658,966 | 58.1% | 687,800 | 572,480 | 50.5% | 3.49 |
| Q2 2026 | 1,270,381 | 860,311 | 67.72% | 766,603 | 60.35% | 862,430 | 706,562 | 55.63% | 4.31 |

Q2 2026 figures re-confirmed directly against TSMC's own press release text ("Income before tax 862,430... Net income 706,562") fetched fresh this session — **this resolves the 07-16 session's own flagged tax-rate imputation gap** (it had used a placeholder "Pretax Income = NI / (1−20% guided rate) = 883,200," explicitly flagged as an approximation; the actual disclosed figure, 862,430, is now used).

```
TTM Revenue (NT$M)      = 989,918 + 1,046,090 + 1,134,103 + 1,270,381 = 4,440,492
TTM Gross Profit (NT$M) = 588,543 + 651,987 + 751,295 + 860,311      = 2,852,136   → GM TTM = 64.23%
TTM Op Income (NT$M)    = 500,685 + 564,903 + 658,966 + 766,603      = 2,491,157   → OM TTM = 56.10%
TTM Pretax (NT$M)       = 525,369 + 592,363 + 687,800 + 862,430      = 2,667,962
TTM Net Income (NT$M)   = 452,302 + 505,744 + 572,480 + 706,562      = 2,237,088   → NM TTM = 50.38%
TTM effective tax rate  = (2,667,962 − 2,237,088) / 2,667,962         = 16.15%
TTM EPS (US$/ADR, summed) = 2.92 + 3.14 + 3.49 + 4.31 = $13.86   (unchanged from 07-16 — same window, no new quarter)
TTM-implied avg FX = TTM Revenue NT$M / TTM Revenue US$M (as-reported each quarter: 33.10+33.73+35.90+40.20=142.93B)
                    = 4,440,492 / 142,930 = 31.068
```

Revenue/Net-Income figures reconcile almost exactly with the 07-16 session's own figures (TTM Revenue 4,440,491→4,440,492, GM 64.22%→64.23%, NM 50.38%→50.38%) — confirms the underlying fundamentals are genuinely unchanged since Q2 earnings; only the balance-sheet/cash-flow and Forward PE inputs are materially refreshed this session.

### 2.4 Balance sheet & cash flow — **fresh Q2 2026 actual data** (two-vendor corroborated, resolves 07-16's carried-forward flag)

| | Q3 2025 | Q4 2025 | Q1 2026 | **Q2 2026 (fresh)** |
|---|---|---|---|---|
| Cash & equivalents (NT$M) | 2,470,759 | 2,767,856 | 3,035,637 | **3,134,218** |
| Total Debt (NT$M) | 1,025,433 | 1,064,583 | 1,090,769 | **982,447** |
| Total Equity, incl. minority interest (NT$M) | 5,035,578 | 5,396,219 | 5,932,389 | **6,474,471** |
| Operating CF (NT$M) | 426,829 | 725,509 | 698,976 | **783,365** |
| CapEx (NT$M) | 288,443 | 361,468 | 350,763 | **496,002** |
| Free Cash Flow (NT$M) | 138,386 | 364,041 | 347,270 | **287,363** |
| D&A (NT$M) | 162,787 | 162,112 | 165,450 | **198,538** |

⚠️ **Flagged discrepancy, not silently resolved:** the Q1 2026 Total Debt figure now shown by both `yfinance` and stockanalysis.com (1,090,769) differs from the figure the 07-12/07-16 sessions carried (1,016,270 — sourced then from the SEC 6-K balance-sheet excerpt directly). The two current vendors agree with each other to the dollar (1,090,768.715 vs. 1,090,769), and their **cash-flow** figures for the same quarters independently reconcile exactly against each other and against OCF−CapEx=FCF internally — giving reasonable confidence in the current data even though it doesn't match the prior session's number. Most likely explanation: a different debt-definition convention (e.g. inclusion of lease liabilities) between the earlier session's SEC-excerpt read and the current vendor aggregate — not investigated further this session, since **only the fresh Q2 2026 figure (982,447, itself corroborated by two vendors) drives this session's calculations**, and TSMC is emphatically net-cash either way (Net Debt/EBITDA computed below stays deeply negative under either debt convention).

```
Net Debt (Q2 2026, NT$M) = 982,447 − 3,134,218 = −2,151,771   (net cash)
TTM D&A (NT$M) = 162,787 + 162,112 + 165,450 + 198,538 = 688,887
TTM EBITDA (NT$M) = TTM Op Income 2,491,157 + TTM D&A 688,887 = 3,180,044
Net Debt/EBITDA = −2,151,771 / 3,180,044 = −0.677×   (net cash — materially more negative than 07-16's carried-forward −0.70×... nearly identical, both deeply net-cash)

TTM FCF (NT$M) = 138,386 + 364,041 + 347,270 + 287,363 = 1,137,060
FCF/NI (TTM) = 1,137,060 / 2,237,088 = 50.83%   (down from 07-16's carried-forward 54.75% — genuine, driven by Q2 2026's CapEx surge to 496,002 NT$M, +41.4% QoQ, as the raised $60–64B 2026 capex guide (§0) kicks in)
```

**Q2 2026's capex jump is the single most consequential fresh data point this session** — it mechanically pulls the FCF Quality sub-score down materially (§3) even as every income-statement metric improved, and is itself well-explained (not a red flag): TSMC's own capacity-expansion guidance was raised, not merely maintained, over this same window.

### 2.5 Shares outstanding — fresh, essentially unchanged

```
Ordinary shares (Q2 2026, common) = 25,932.370M ÷ 5 = 5,186.474M ADR-equivalent shares (vs. 5,186.2M in 07-16 — immaterial)
Market Cap (ADR basis) = $419.13 × 5,186.474M = $2,173,806.85M
Net Debt (USD, at live spot FX 32.21) = −2,151,771 / 32.21 = −$66,804.44M
EV = Market Cap + Net Debt = 2,173,806.85 − 66,804.44 = $2,107,002.41M
```

### 2.6 Annual figures FY2021–FY2025 — unchanged (no new fiscal year has closed since 07-16)

**Revenue 3yr CAGR (FY2022→FY2025):** unchanged, `18.94%`
**5yr PE range (2021–2025, annual):** unchanged — Avg **20.74×**, Low **11.44×**, High **26.73×**

### 2.7 Forward PE — the single most consequential input this session, full transparent methodology

**This is where the score moves the most, and it is shown in full — three separate, independently-motivated constructions, not one number picked and hidden.**

The core issue (a known, named pattern in this framework — see the glossary's **NTM** entry, added by the 2026-08-09 SPGI session for exactly this problem): "Forward PE" means different things depending on how a data vendor anchors it once a fiscal year is more than half complete. Today (10 Aug 2026), FY2026 is ~58% through by calendar and further along by revenue-weighting (H2 is TSMC's stronger half) — materially different from the 07-16 session (right after Q2 earnings, when a "FY2026 forward EPS" anchor was still a reasonable full-year-ahead read).

| Construction | Forward EPS basis | Forward PE | Source / method |
|---|---|---|---|
| **A — FY2026 anchor** (same convention 07-16 used) | $16.82 (`yfinance` current-FY consensus, 13 analysts, range $15.23–$17.57) | **24.92×** | Now the *most* stale of the three — FY2026 is now mostly reported/locked in, not genuinely "forward" |
| **B — FY2027 anchor** (next full fiscal year — the convention both live vendors now default to) | avg of `yfinance` $21.61 (13 analysts) and stockanalysis.com's implied $21.97 → **$21.79** | **19.24×** | Two independent vendors converge closely (1.7% apart) on "Forward PE" ≈19.1–19.4× once queried directly |
| **C — Constructed NTM** (literal "next twelve months" per this framework's own definition) | Q3'26 consensus $4.45 + Q4'26 consensus $4.95 + half of FY2027 consensus ($21.61/2 = $10.80) = **$20.20** | **20.75×** | Built directly from `yfinance`'s `eps_trend`/`earnings_estimate` quarterly consensus — assumes even quarterly split of FY2027, a disclosed approximation (TSMC's H2-weighted seasonality means this could modestly overstate H1 2027 EPS, i.e. modestly *understate* this NTM figure's true forward PE — flagged, not corrected without better data) |

**Construction B is used as primary** — it is the only one of the three that is *directly, independently vendor-corroborated* rather than self-constructed, and it reflects the standard convention both real vendors have already rolled to now that FY2026 is well past its midpoint. **A and C are shown in full as sensitivity, not discarded** — see §7 for how much each moves the final score, and note in advance: **the recommendation in §9 does not depend on which of the three is chosen** (all three are tested against the R/R gate).

```
FwdPE_Score(B, primary) = clamp((19.24 − 11.44)/(26.73 − 11.44) × 100, 0, 100) = 51.02
  Historical PE Modifier: (19.24 − 20.74)/20.74 × 100 = −7.23% → within ±10% → 0
  FwdPE_Score = 51.02

FwdPE_Score(A, sensitivity) = clamp((24.92−11.44)/15.29×100) = 88.15; modifier (24.92−20.74)/20.74=+20.15%→+10 → FwdPE_Score = 98.15
FwdPE_Score(C, sensitivity) = clamp((20.75−11.44)/15.29×100) = 60.89; modifier (20.75−20.74)/20.74=+0.05%→0 → FwdPE_Score = 60.89
```

### 2.8 PEG — still NOT APPLIED, redistributed to EV/EBIT

Unchanged conclusion. FY2023's −14.2% cyclical EPS decline is still inside the relevant trailing-3-fiscal-year window (FY2023–FY2025, since no new FY has closed) — TSM still doesn't qualify as a clean-earnings Fast Grower per Upgrade 3. PEG's 15% weight redistributed to EV/EBIT (→ 40%).

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology, unchanged version)

### 3.1 Hard disqualifier check

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ **consecutive** fiscal years w/o growth-capex explanation | Fiscal-year window unchanged (no new FY closed): FY2023 34.3% (fail) · FY2024 75.1% (pass, breaks the streak) · FY2025 58.4% (fail). **TTM (fresh, §2.4): 50.83%** — a real data point, but the disqualifier test operates on fiscal years, not TTM (per [quality-scoring.md](../framework/quality-scoring.md)'s rolling-window clarification). | disqualify if 2+ **consecutive** FYs <70% w/o carve-out | ✅ Does **not** fire — same as every prior TSM session (FY2024 still breaks the FY2023/FY2025 streak). **The growth-capex carve-out is now more strongly evidenced than ever**: 2026 capex guidance was raised to $60–64B (from $52–56B, §0/§2.4), and Q2 2026's own capex (496,002 NT$M) jumped +41.4% QoQ — directly consistent with "capacity expansion, not maintenance spend." **⚠️ Forward-looking watch item (new this session, not a current disqualifier):** if FY2026's full-year FCF/NI conversion comes in below 70% (increasingly plausible given the TTM trend and rising capex), the *next* rolling window (FY2024 pass / FY2025 fail / FY2026 fail) would contain two **consecutive** failing years for the first time — at that point the growth-capex carve-out becomes the single load-bearing reason the disqualifier still doesn't fire, not a secondary consideration. Flagged now as a genuine item to re-examine carefully at TSM's next full-fiscal-year-end evaluation, not an alarm today. |
| Net Debt/EBITDA over threshold (2.5× standard) | TTM (fresh): **−0.677×** (net cash) | disqualify if >2.5× | ✅ PASS, overwhelmingly |
| FCF-positive 3+ consecutive years | FY2023/24/25 all positive (unchanged, annual figures not affected by Q2 2026 data) | disqualify if not | ✅ PASS |

**No hard disqualifier fires.**

### 3.2 Quality Score — full computation

```
PROFITABILITY (25% weight):
  Net Margin (TTM, fresh) = 50.38%   → NetMargin_Component = clamp((50.38/30)×100) = 100.0 (saturates)
  ROIC (TTM, fresh — see §3.3 below) = 48.32%   → ROIC_Component = clamp((48.32/30)×100) = 100.0 (saturates)
  Profitability_Score = (100.0 + 100.0) / 2 = 100.0   (no FCF-positivity cap — 3yr positive confirmed above)

MARGINS (15% weight):
  Gross Margin (TTM, fresh) = 64.230%   (vs. 64.22% in 07-16 — essentially unchanged, same window)
  GrossMargin_Score = clamp((64.230/80)×100) = 80.29

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2022→FY2025, unchanged) = 18.94%
  Growth_Score(raw) = clamp((18.94/25)×100) = 75.76
  TAM/pricing-power modifier: +10 applied, evidence now further strengthened by this session's own findings —
    (a) July 2026 monthly revenue +44.7% YoY, a new all-time-high monthly print (§0, primary-sourced 6-K);
    (b) full-year 2026 revenue-growth guidance raised to "slightly above 40%" at the Q2 2026 call, now well-corroborated (§0);
    (c) 2026 capex guidance raised to $60–64B (from $52–56B) explicitly to fund capacity for this demand (§0/§2.4) —
        capacity expansion in response to demand is itself evidence of pricing-power-supporting, not merely cyclical, growth;
    (d) unchanged foundry market-share/advanced-node-mix citations from prior TSM sessions.
  Growth_Score = clamp(75.76 + 10) = 85.76   (vs. 85.8 in 07-16 — unchanged, evidence refreshed)

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (TTM, fresh) = −0.677×
  BalanceSheet_Score = clamp(100×(1 − (−0.677)/4)) = 116.9 → clamp to 100.0   (saturates)

MOAT SIGNAL (15% weight) — unchanged conclusions (4/5 TRUE), evidence refreshed:
  Market share stable/growing:  TRUE — unchanged citation, reinforced by the July revenue print.
  Brand premium (pricing power): TRUE — unchanged citation (documented advanced-node price increases without share loss); further reinforced by capex being raised specifically to meet demand rather than TSMC needing to discount to win volume.
  Network effect:  FALSE — unchanged (a dedicated foundry has no two-sided-marketplace mechanism distinct from switching costs).
  Switching costs:  TRUE — unchanged citation (OIP ecosystem, PDK lock-in, $2–5B re-design cost estimates).
  Scale cost advantage:  TRUE — unchanged citation (Intel's yield/cost gap); reinforced by TSMC's ability to fund an $8–12B capex raise from internally generated cash while remaining deeply net-cash.
  Moat_Score = (4/5) × 100 = 80.0   (unchanged)

FCF QUALITY (10% weight):
  FCF/NI (TTM, fresh) = 50.83%   (down from 07-16's carried-forward 54.75% — genuine, driven by the Q2 2026 capex surge, §2.4)
  FCFQuality_Score = clamp(((0.5083 − 0.40)/0.60)×100) = 18.05   (down from 24.6 — the main driver of this session's Quality Score decline)

QUALITY SCORE = 100.0×0.25 + 80.29×0.15 + 85.76×0.20 + 100.0×0.15 + 80.0×0.15 + 18.05×0.10
             = 25.000 + 12.044 + 17.152 + 15.000 + 12.000 + 1.805
             = 83.00 (82.9998, rounds to 83.0)
```

### 3.3 ROIC computation (fresh Q2 2026 data)

```
Invested Capital (Q2 2026) = Total Debt 982,447 + Total Equity 6,474,471 − Cash 3,134,218 = 4,322,700 NT$M
NOPAT = TTM Op Income 2,491,157 × (1 − 16.15% eff. tax rate) = 2,088,837 NT$M
ROIC = 2,088,837 / 4,322,700 = 48.32%
```

**Quality Score = 83.0 / 100.0 — clears the 80.0+ gate**, down modestly from 83.7 (07-16). The entire delta is driven by the FCF Quality sub-score (24.6→18.05) — every other sub-score is either unchanged or already saturated at its 100.0 ceiling. **This decline is well-explained (TSMC investing more, not less, in capacity — §2.4/§3.1) and is not itself a quality red flag**, though it is the first sub-score in this framework's TSM coverage to genuinely worsen quarter-over-quarter, and is now flagged as a forward-looking watch item (§3.1) rather than a footnote.

**Gate result: PASS.** Proceed to the Rate Environment Gate and Phase 02 valuation scoring.

---

## 4. Rate Environment Gate

```
Step 1 — Earnings Yield Spread Test (using primary Forward PE, Construction B = 19.24×)
EY = 1 / 19.24 = 5.198%
Spread = EY − 10Y Treasury = 5.198% − 4.69% = +0.508%
Threshold: Spread ≥ +1.5% → PASS. Spread < +1.5% → FAIL → additive +5.
Result: FAIL → +5
```

**Robustness check across all three Forward PE constructions:** A (24.92×) → EY 4.01%, spread −0.68% → FAIL +5. C (20.75×) → EY 4.82%, spread +0.13% → FAIL +5. **Step 1's conclusion (FAIL, +5) is robust across every construction tested** — same finding as the 07-16 session.

```
Step 2 — Rate Regime Modifier
10Y = 4.69% → 3.5–5% bracket → +5
```

**Combined Rate Gate additions: +5 (Step 1) + 5 (Step 2) = +10** — unchanged from 07-16 (10Y moved only 4.58%→4.69%, staying within the same bracket).

---

## 5. Phase 02 — Valuation Score

### 5.1 FCF Yield (40% weight)

```
FCF Yield = TTM FCF (USD) / Market Cap
TTM FCF (USD) = NT$1,137,060M / 31.068 (TTM-implied avg FX, §2.3) = $36,599.5M
FCF Yield = 36,599.5 / 2,173,806.85 = 1.684%
FCF_Score = clamp(100×(1 − 1.684/10)) = 83.16
```

### 5.2 EV/EBIT (40% weight — PEG redistribution, §2.8)

```
TTM Op Income (USD) = NT$2,491,157M / 31.068 = $80,185.0M
EV/EBIT = $2,107,002.41M / $80,185.0M = 26.28×
EV/EBIT_Score = clamp((26.28 − 12)/23 × 100) = 62.07
```

Modestly more expensive than 07-16's 25.54× (58.87) — the live price rose 2.98% since 07-16 while TTM EBIT is essentially flat (same fundamental quarters, now more precisely primary-sourced rather than partially derived) — a mechanical, expected drift, not a surprise.

### 5.3 Forward PE + Historical PE Modifier (20% weight) — see §2.7 for full methodology

```
FwdPE_Score (Construction B, primary) = 51.02
```

**⚠️ This is the dominant driver of this session's Valuation Score decline vs. 07-16** (FwdPE_Score 100.0 [capped] → 51.02, a ~49-point swing on this one sub-score). Full reasoning in §2.7 — the 07-16 session used a forward PE (25.9×) sourced *hours* after the Q2 earnings beat, explicitly flagged then as unsettled vendor data; that session's own "next review trigger" predicted exactly this outcome once consensus digested the beat.

### 5.4 Raw Weighted Score

```
Raw (primary, Construction B) = (83.16×0.40) + (62.07×0.40) + (51.02×0.20)
                              = 33.264 + 24.828 + 10.204 = 68.296

+ Rate Environment Gate (§4): +10

Raw + Rate Gate = 78.296
```

**Sensitivity (Constructions A and C, §2.7):**
```
Raw(A, FY2026 anchor)    = 33.264 + 24.828 + 98.15×0.20 = 33.264+24.828+19.630 = 77.722  → +10 = 87.722
Raw(C, constructed NTM)  = 33.264 + 24.828 + 60.89×0.20 = 33.264+24.828+12.178 = 70.270  → +10 = 80.270
```

---

## 6. Upside/Downside Modifier (Expected-Return Modifier)

**Step 1 — scenario fair values (Rule 7).** Anchored to fresh FY2026 analyst consensus EPS dispersion (avg/low/high across 13 analysts, `yfinance` `earnings_estimate`) — a **sourced range**, not an invented spread — combined with the same bull/base/bear multiple convention the 07-16 session used (kept unchanged for continuity; no new evidence specifically argues for revising the multiples themselves):

| Scenario | Wt | EPS (FY2026 consensus) | Multiple | Fair Value |
|---|---|---|---|---|
| Bull | 25% | $17.57 (analyst high, 13 analysts) | 28× (unchanged from 07-16) | **$491.96** |
| Base | 50% | $16.82 (analyst avg, up from 07-16's $15.73 — a genuine, sourced upward revision reflecting the confirmed earnings beat + raised guidance) | 24× (unchanged) | **$403.68** |
| Bear | 25% | $12.00 (unchanged from 07-16 — still meaningfully below TTM $13.86, kept conservative and comparable rather than mechanically raised alongside the bull/base cases) | 15× (unchanged) | **$180.00** |

```
PW Fair Value = 0.25×491.96 + 0.50×403.68 + 0.25×180.00 = $369.83
```

**Sanity check (Rule 4):** PW FV ($369.83) sits ~32% below the analyst consensus PT range found this session (mean $540.20/median $534.50) — a conservative, not rosy, scenario blend, consistent with Rule 7.

**Step 2 — catalyst window & annualization (Rule 10).** Documented, dated catalysts within 18–24 months, unchanged: **Q3 2026 earnings** (mid-October 2026, guidance already on record from the Q2 release: revenue $44.6–45.8B, GM 65–67%, OM 56–58%) and the continuing 2nm(N2)/A16 ramp. Standard 2yr window used (Guardrail 1 satisfied).

```
Gap Upside % = (369.83 / 419.13) − 1 = −11.76%
Annualized gap (2yr) = −11.76% / 2 = −5.88%/yr
```

**Step 3 — expected annual return E.**
```
Intrinsic growth = 10%/yr — unchanged disclosed judgment call from 07-16, kept for consistency: TSM's trailing 3yr EPS CAGR
  (FY2022→FY2025, still 19.6%, still unchanged since no new FY closed) remains distorted by the FY2023 cyclical trough and the
  ongoing AI-capex supercycle, so the same ~50% conservative haircut is applied. A case could reasonably be made to raise this
  given the confirmed acceleration (§0) — not made here, in favor of comparability and conservatism.
Shareholder yield = dividend yield 0.83% (IBKR live, §1) + buyback yield 0% (unchanged — capex, not buybacks, is where 2026
  capital is being deployed, now even more so given the raised $60–64B capex guide).
E = −5.88 + 10 + 0.83 = 4.95%/yr
```

**Step 4 — map E to M** (hurdle H = 10%, 0 ≤ E < H branch):
```
M = +5 × (10 − 4.95)/10 = +5 × 0.505 = +2.53
```
A thin, positive (mild trim-pressure) reading — smaller than 07-16's +3.4, since the price/fair-value gap narrowed (−11.76% vs. −15.20%) as base/bull EPS assumptions rose with consensus. No guardrail cap applies (real catalysts exist).

**This modifier is decoupled from the disputed Forward PE input (§2.7)** — it stays constant (+2.53) across all three Forward-PE-construction scenarios in §7.

---

## 7. Final Valuation Score & Composite Score

```
Primary (Construction B — FY2027 vendor-anchor, two-source-corroborated):
  Raw weighted + Rate Gate           78.296
  Upside/Downside Modifier           +2.526
  FINAL VALUATION SCORE              80.822 → rounds to 80.8
```

| | Value |
|---|---|
| **Quality Score** | **83.0** (PASSES 80.0+ gate) |
| **Final Valuation Score (primary)** | **80.8** |

```
Composite Score (primary) = 0.50 × (100 − 83.0) + 0.50 × 80.8 = 8.50 + 40.40 = 48.9
```

**Composite Score = 48.9** — falls in the **30.0–49.9 "Cheap / BUY — Standard position (3–5%)"** band, crossing out of Hold territory for the first time in TSM's coverage under this framework.

### ⚠️ Full disclosed sensitivity — Forward PE construction, carried through to its logical conclusion

| Construction | Final Valuation Score | Composite Score | Action band |
|---|---|---|---|
| **B — FY2027 vendor-anchor (primary)** | **80.8** | **48.9** | Buy — Standard (30.0–49.9) |
| C — Constructed NTM | 82.8 | 49.9 | Buy — Standard, at the very edge of the band |
| A — FY2026 anchor (same convention as 07-16) | 90.2 | 53.6 | Hold — watch only (50.0–69.9) |

**Two of three defensible constructions land in the Buy band; the third (A) — now the most conventionally stale of the three, since FY2026 is well past its midpoint — lands in Hold, just past the boundary.** This session reports B as official (§2.7 explains why), but **critically, §8 below shows the actual entry recommendation does not hinge on this choice at all** — the Risk/Reward gate independently blocks entry whether the Composite Score is 48.9, 49.9, or 53.6.

---

## 8. Order Setup — Score Says "Buy," the R/R Gate Says No

Per fair-value-methodology.md Step 2, a Composite Score of 48.9 (30.0–49.9 band) nominally calls for **"Approaching buy price → Set limit order,"** not a Watchlist-only conclusion. Per TSM's own established convention (07-12/07-16 sessions; consistent with the MA/2026-07-09 precedent for tickers where PW Fair Value serves directly as the order-setup "Blended Fair Value"), this session's **Blended Fair Value = PW Fair Value = $369.83** (§6).

### Order Setup Checklist

```
[x] Composite Score:                          48.9   (Buy — Standard, 30.0–49.9 band)
[x] Blended Fair Value (= PW FV):              $369.83
[x] Margin of Safety % (band range):           25–30%
[x] Max Acceptable Loss % (band range):        25–30%
```

**R/R identity across the full applicable band** (R/R = MoS / [(1−MoS)×MaxLoss]):

| MoS | Max Loss | Buy Price | Stop Loss | R/R |
|---|---|---|---|---|
| 25% | 25% | $277.37 | $208.03 | 1.33:1 |
| 25% | 30% | $277.37 | $194.16 | 1.11:1 |
| 30% | 25% | $258.88 | $194.16 | **1.71:1 (best in band)** |
| 30% | 30% | $258.88 | $181.22 | 1.43:1 |

**R/R ranges 1.11:1–1.71:1 across the entire applicable band — fails the 2:1 minimum at every combination, including the most favorable one tested.** Per fair-value-methodology.md Step 6 ("If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely"), **no order should be placed.**

**Why:** PW Fair Value ($369.83) sits **11.76% below** the live price ($419.13) — the Valuation Score improved (cheaper *relative to TSM's own history and absolute yardsticks*, driven by the Forward PE resolution, §2.7/§5.3) even though the stock is still **priced above** this session's own scenario-weighted fair value in absolute terms. The Composite Score and the R/R gate are answering different questions (relative cheapness vs. an absolute margin-of-safety anchor) and they disagree here — exactly the situation the 2026-07-09 MA and 2026-06-19 DB1 sessions document as a real, structural feature of this framework, not a bug to route around.

**Robustness — this conclusion does not depend on the Forward PE construction chosen (§7):**
- Under Construction A (Composite 53.6, Hold band): no order setup is produced at all (Score 50.0–69.9 → "No MoS → Watchlist only").
- Under Construction C (Composite 49.9, still nominally Buy band): the identical R/R math applies (PW FV unchanged) — **still fails 2:1 throughout**.

**Every tested scenario this session converges on the same action: do not enter.**

**Hypothetical, NOT a recommendation** (shown for transparency only, at the best-case band point — MoS 30%, Max Loss 25%): Buy $258.88, Stop $194.16, Risk/share $64.72, Max $ Risk (1.5% of $65,925.08 portfolio) = $988.88 → 15.3 shares → position size $3,955.50 (6.00% of portfolio) — this would also exceed the Buy-Standard band's 3–5% allocation cap, a second reason (moot, since R/R already fails first) this setup is not actionable as computed.

---

## 9. Recommendation

# **WATCHLIST ONLY — do not enter. Composite Score 48.9 (primary) nominally crosses into the 30.0–49.9 Buy band, but the Risk/Reward gate independently fails throughout the entire applicable band (1.11:1–1.71:1, vs. the 2:1 minimum) — and this conclusion is robust across every Forward-PE-construction sensitivity tested.**

This is a genuinely different situation from every prior TSM session (07-12: 53.2/Hold; 07-16: 53.4/Hold) — **for the first time, TSM's Valuation Score has moved into "Cheap" territory**, driven almost entirely by the Forward PE sub-score resolving downward as post-earnings analyst consensus fully digested TSMC's Q2 2026 beat and the market rolled its forward-looking anchor to FY2027 — exactly the mechanism the 07-16 session's own "next review trigger" predicted. Quality remains excellent (83.0, comfortably clears the 80.0+ gate) though it declined modestly this session, driven by a well-explained but real drop in the FCF Quality sub-score as TSMC's capex guidance was raised (§2.4/§3).

**But the score crossing into Buy territory does not, by itself, make this an executable trade.** This framework's R/R gate exists precisely to catch cases like this: TSM looks cheaper *relative to its own multiples history* (which is what the Valuation Score measures) while still trading **above** this session's own absolute, scenario-weighted fair value ($419.13 live vs. $369.83 PW FV — an 11.76% *negative* margin of safety, not a positive one). No combination of the standard 25–30% MoS / 25–30% Max Loss parameters produces a 2:1 setup. **No order, no position, no capital deployed.**

This session's trigger (TSMC's July 2026 monthly revenue, +44.7% YoY, independently confirmed against TSMC's own primary 6-K filing, §0) was real, material, and well ahead of even TSMC's own recently-raised guidance — the underlying business is executing exceptionally well. That is fully reflected in this session's improved sub-scores; it just isn't, on its own, sufficient to overcome the gap between the live price and this framework's own conservative fair-value estimate.

---

## 10. Next Review Trigger

- **The Forward PE construction question (§2.7/§7) is the single highest-value thing to re-check.** All three constructions converge on "no order this session" only because of the R/R gate — but if PW Fair Value itself rises meaningfully at the next earnings print (plausible, given the confirmed growth acceleration), the R/R gate could clear even with today's Forward PE dispersion unresolved. Conversely, if consensus estimates continue converging tightly around Construction B/C's readings, that specific ambiguity becomes moot going forward.
- **A pullback toward or below this session's own PW Fair Value (~$370)** would meaningfully improve the entry case — a modestly higher bar than the 07-16 session's ~$345 threshold (base/bull EPS assumptions rose with consensus), but still well below the live price.
- **TSMC's August/September 2026 monthly revenue reports** (next: ~2026-09-10 for August) — a useful interim data point on whether the accelerating trajectory (§0) holds; per one cited source, TSMC needs August+September to each average NT$479.8–499.0B to hit its own Q3 guidance floor.
- **Q3 2026 earnings**, expected mid-October 2026 (guidance on record: revenue $44.6–45.8B, GM 65–67%, OM 56–58%) — the next scheduled full re-derivation, and the point at which the FCF Quality watch item (§3.1) gets its next real data point.
- **The forward-looking FCF/NI hard-disqualifier watch item (§3.1)** — worth deliberate attention once FY2026 closes, given the rising capex trend.
- Any Taiwan Strait geopolitical escalation, new US/China export-control action, or standard Rule 9 triggers (management change, material M&A, a further >15% unexplained move from $419.13).

**No position opened — nothing to log in `decisions/`.**

---

## 11. Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. All terms below were already defined there prior to this session (most recently by the 2026-08-09 SPGI session's **NTM** entry, directly relevant to §2.7's methodology); no new terms were introduced this session.

| Term | Meaning |
|---|---|
| **ADR (American Depositary Receipt)** | A US-exchange-listed security representing shares of a non-US company; TSM = 1 ADR representing 5 TSMC ordinary shares. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure — TSMC's 2026 guidance was raised this session's window from $52–56B to $60–64B, a material driver of this session's Quality Score decline and R/R-gate math. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — **48.9 for TSM this session** (primary construction), the first time it has crossed below 50.0 (out of the Hold band) in TSM's coverage. |
| **D&A** | Depreciation & Amortization. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization. |
| **EDGAR** | The SEC's public filing database — source for every primary TSMC filing cited this session (the July 2026 revenue 6-K and the Q4 2025 earnings 6-K). |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT; TSM's is 26.28× this session, up modestly from 25.54× (07-16) on the price move. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury in the Rate Environment Gate. |
| **Fabless** | A chip company that designs but doesn't manufacture semiconductors (TSMC's customer base). |
| **Fast Grower** | A company growing EPS >15%/yr for 3+ years on a clean, non-distorted earnings base; TSM still does not qualify (§2.8). |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income — TSM's TTM FCF/NI fell to 50.83% this session (from 54.75%) as capex accelerated. |
| **Foundry (pure-play foundry)** | A contract chip manufacturer for other companies' designs; TSMC is the dominant one. |
| **Form 6-K** | A furnished report foreign private issuers file with the SEC — this session's trigger source (TSMC's own July 2026 monthly-revenue 6-K, filed 2026-08-10). |
| **Form 20-F** | The annual report foreign private issuers file with the SEC (TSMC's equivalent of a 10-K). |
| **Forward PE** | Price ÷ forward-looking expected EPS — the central, most-disputed input this session (§2.7), with three separately-constructed readings shown in full. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear, Rule 7); **$369.83 this session**, up from $345.13 (07-16) as base/bull EPS assumptions rose with analyst consensus. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score; none fired for TSM, though §3.1 flags a forward-looking watch item. |
| **Hurdle rate** | The minimum acceptable annual return (10%) the Upside/Downside Modifier measures expected return against. |
| **Invested Capital** | Debt + Equity − Cash, the ROIC denominator. |
| **Moat** | A durable competitive advantage; scored 80.0 (4 of 5 signals) for TSM this session, unchanged. |
| **Net Debt/EBITDA** | This framework's primary balance-sheet-risk gate; TSM's is −0.677× (net cash), refreshed with real Q2 2026 data this session. |
| **Net Margin** | Net Income ÷ Revenue. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate). |
| **NTM (Next Twelve Months)** | A forward-looking estimate covering the next twelve months from today, distinct from a "current" or "next fiscal year" consensus figure — the exact ambiguity resolved (via three separate labeled constructions) in this session's §2.7 Forward PE discussion. |
| **PEG ratio** | PE ÷ earnings growth rate; still not scored for TSM (§2.8). |
| **Process node (e.g. "2nm"/"N2", "A16")** | A generation of semiconductor manufacturing technology. |
| **PT (Price Target)** | An analyst's price forecast; consensus mean $540.20 this session, discussed qualitatively only. |
| **Quality Score** | This framework's 0.0–100.0 continuous score; 80.0+ required for Phase 02. TSM scored **83.0** this session, down modestly from 83.7 (07-16). |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-score check comparing Earnings Yield to the 10-Year Treasury, plus the additive Treasury-bracket adjustment; unchanged +10 this session. |
| **R/R (Risk/Reward ratio)** | (Expected gain) ÷ (Expected loss); this framework's hard 2:1 minimum — **the gate that blocks entry this session** despite a passing Composite Score (§8). |
| **ROIC** | Return on Invested Capital; 48.32% this session (fresh Q2 2026 data), up from 46.92% (carried-forward, 07-16). |
| **Rule 0 / Rule 4 / Rule 6 / Rule 7 / Rule 9 / Rule 10** | This framework's standing instructions: always fetch live price first; sanity-check implied returns; strip out one-time items before valuing; use a scenario-weighted fair value; force re-valuation on fundamental triggers; separate intrinsic value from market price with a documented catalyst/timeline. |
| **Shareholder yield** | Dividend yield plus net buyback yield. |
| **TAM** | Total Addressable Market. |
| **Treasury yield (10Y)** | This framework's risk-free-rate benchmark; 4.69% this session (unchanged bracket from 07-16). |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | The additive ±15 valuation-score adjustment; computed at +2.53 for TSM this session (vs. +3.4, 07-16) as the price/fair-value gap narrowed. |
| **Wafer** | The silicon disc a foundry manufactures chips on and prices its capacity by. |


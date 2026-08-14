# NEW POSITION — RDDT (Reddit, Inc.)

**Task type:** NEW POSITION
**Date:** 2026-08-14
**10Y US Treasury yield:** ~4.65% (2026-08-13 close, via web search cross-check of TradingEconomics/Investing.com secondary reporting — captured for the record only; the Rate Environment Gate is never reached this session, see below)
**Rate Regime Modifier (would apply, not applied):** 3.5–5% bracket → +5

**Trigger:** Unattended Telegram-scan (Routine 6). Post on [t.me/tarasguk](https://t.me/tarasguk) (post #11680, ~10:53 UTC 2026-08-14) claimed: *"$RDDT додали в індекс S&P500"* ("$RDDT added to the S&P 500 index"). RDDT had no existing watchlist entry and is not a current holding, so per `telegram-scan.md` step 4 ("no watchlist entry exists at all") this triggers a full `/new-position` evaluation. Per Rule 0, the Telegram text is a trigger only — treated as unverified until independently confirmed below, and the evaluation proceeds on fundamentals regardless of whether the claim holds up.

---

## 0. Rule 0 — Live Price (fetched fresh this session)

IBKR `get_price_snapshot`, contract_id 692025016 (REDDIT INC-CL A, NYSE), fetched at session start:

| Field | Value |
|---|---|
| Last | **$178.71** |
| Bid / Ask | $178.50 / $178.75 |
| Change vs. prior close | +$20.59 (**+13.02%**) |
| Volume (day) | ~8.70M shares |
| 52-week high / low | $282.81 / $119.27 |
| 13-week high | $208.00 |

This supersedes the pre-session $179.35 snapshot handed off at trigger time (same order of magnitude, re-fetched independently per Rule 0 rather than reused secondhand). A +13% single-session move is itself a Rule 9 trigger ("stock moves >15% without known fundamental trigger" — this one is just under that threshold but still large enough, and has an identifiable candidate cause below, so investigated fully rather than dismissed).

---

## 1. Investigating the trigger — was RDDT actually added to the S&P 500?

**Independently confirmed: YES, materially true, though the Telegram post's tense is slightly off** — Reddit has not yet been *added*; S&P Dow Jones Indices *announced* the addition, effective a few days after this post.

Primary source fetched directly: [S&P Dow Jones Indices press release, spglobal.com, 2026-08-13](https://press.spglobal.com/2026-08-13-Reddit-Set-to-Join-S-P-500-and-Sun-Communities-to-Join-S-P-MidCap-400) — "Reddit Set to Join S&P 500 and Sun Communities to Join S&P MidCap 400":
- Reddit, Inc. (NYSE: RDDT) will replace AvalonBay Communities Inc. (NYSE: AVB) in the S&P 500, **effective prior to the market open Tuesday, August 18, 2026**.
- AvalonBay is being removed because it is being acquired by Equity Residential (NYSE: EQR); the combined entity will be renamed Vivmark Residential (NYSE: VMRK) and remains in the S&P 500.
- Reddit is classified under the **Communication Services** sector for index purposes.

Cross-checked against independent secondary reporting, all consistent: [CNBC](https://www.cnbc.com/2026/08/13/reddit-shares-jump-11percent-on-inclusion-in-sp-500.html), [Reuters via BNN Bloomberg](https://www.bnnbloomberg.ca/business/company-news/2026/08/14/reddit-surges-on-sp-500-inclusion-set-to-replace-avalonbay/), [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/reddit-added-p-500-130000497.html), [PRNewswire](https://www.prnewswire.com/news-releases/reddit-set-to-join-sp-500-and-sun-communities-to-join-sp-midcap-400-302851432.html) — all report the same 18 August effective date and AvalonBay replacement, no contradictions found.

**This explains the price move.** The announcement (13 August, after market close) triggered an initial after-hours jump (~11–13% per multiple outlets), which is continuing to show up in today's (14 August) regular-session move — the classic S&P 500 index-inclusion mechanics: S&P 500-tracking passive funds must all buy the stock at once on the 18 August effective date, and the anticipated forced buying gets priced in as soon as the announcement is public, days ahead of the actual effective date. This is a **market-structure event, not a change in Reddit's underlying fundamentals** — it has no bearing on the Quality Score computed below, and per this framework's Action Table a valuation/trim decision is never made on a price move alone without a documented fundamental trigger. It is being treated here purely as the reason the Telegram scan surfaced this name, consistent with the rest of this session evaluating Reddit strictly on its filed fundamentals.

**Ruled out as an alternative explanation:** Reddit's most recent 8-K (filed 2026-08-12, two days before this scan) is unrelated — it discloses the planned departure of Chief Legal Officer Benjamin Lee (effective 14 September 2026) with an immediate named successor (Paul Cappuccio), a routine executive transition, not a material driver of a 13% move. Reddit's last earnings release was 30 July 2026 (Q2 2026, per its 2026-07-30 8-K) — well before this move and already reflected in the pre-announcement price. Next earnings date: 4 November 2026.

---

## 2. Quality Score (Phase 01) — full calculation

Per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29. All figures below are TTM (trailing twelve months ended 2026-06-30) unless marked FY (fiscal/calendar year), reconstructed as **FY2025 annual − H1 2025 + H1 2026** from SEC EDGAR XBRL. **Data sourcing:** `yfinance` was not attempted given the documented environment failure noted in prior sessions (e.g. 2026-07-19 DOCU) — went straight to the established fallback: SEC EDGAR XBRL `companyfacts` API (CIK 0001713445, primary source, directly filed figures) for every quantitative input, cross-checked against `stockanalysis.com`'s independently-computed TTM figures. Every cross-check below matched to within rounding.

### Raw inputs (SEC XBRL, USD thousands unless noted)

| Line item | FY2022 | FY2023 | FY2024 | FY2025 | TTM (ended 2026-06-30) |
|---|---|---|---|---|---|
| Revenue | 666,701 | 804,029 | 1,300,205 | 2,202,506 | **2,778,834** |
| Cost of revenue | 104,799 | 111,011 | 123,595 | 194,216 | **237,802** |
| Gross profit | 561,902 | 693,018 | 1,176,610 | 2,008,290 | **2,541,032** |
| Operating income (EBIT) | (172,162) | (140,161) | (560,568) | 441,984 | **784,998** |
| Net income | (158,550) | (90,824) | (484,276) | 529,721 | **871,095** |
| Income tax expense/(benefit) | 622 | 3,801 | (931) | (1,031) | **6,863** |
| Pretax income | (157,928) | (87,023) | (485,207) | 528,690 | **877,958** |
| D&A | 8,000 | 13,702 | 15,643 | 15,948 | **16,519** |
| Operating cash flow | (94,021) | (75,114) | 222,068 | 690,875 | **1,026,095** |
| CapEx | 6,233 | 9,724 | 6,248 | 6,706 | **7,446** |
| **FCF (OCF − CapEx)** | **(100,254)** | **(84,838)** | **215,820** | **684,169** | **1,018,649** |

TTM = FY2025 − H1'2025 + H1'2026 for each flow line, using the same quarter-boundary reconstruction method this framework has used since the 2026-06-20 5yr-PE-automation change (verified internally consistent: TTM revenue $2,778,834K and TTM EBIT $784,998K independently match `stockanalysis.com`'s reported $2,779M / $785M almost exactly). Balance-sheet lines below are the 2026-06-30 (most recent 10-Q) instant values, not FY-end.

| Balance sheet item (2026-06-30) | Value |
|---|---|
| Cash and cash equivalents | $1,486,838K |
| AFS debt securities (current) | $1,299,519K |
| Total debt (long-term + short-term) | **$0** — no debt line items exist in Reddit's XBRL filings; confirmed net-cash balance sheet |
| Stockholders' equity | $3,285,700K |

### Sub-score calculations

**Profitability (25% weight)**
```
Net Margin (TTM) = 871,095 / 2,778,834 = 31.35%
NetMargin_Component = clamp((31.35/30)×100, 0, 100) = 100.0

Effective tax rate (TTM) = 6,863 / 877,958 = 0.78%  (near-zero — Reddit is drawing down historical
  NOL carryforwards from its 2022-2023 loss years; a real, filed figure, not invented)
NOPAT (TTM) = EBIT × (1 − tax rate) = 784,998 × (1 − 0.0078) = 778,860

Invested Capital (2026-06-30) = Total Debt + Equity − (Cash + AFS securities)
                               = 0 + 3,285,700 − (1,486,838 + 1,299,519) = 499,343

ROIC (TTM) = NOPAT / Invested Capital = 778,860 / 499,343 = 155.98%
ROIC_Component = clamp((155.98/30)×100, 0, 100) = 100.0

Uncapped Profitability_Score = (100.0 + 100.0) / 2 = 100.0
```
Reddit's ROIC reads extremely high because its invested-capital base is genuinely tiny relative to earnings (asset-light forum/ad business, no debt, and a large IPO-era cash/securities pile that gets netted out) — cross-checked directionally against `stockanalysis.com`'s own independently-computed "current" ROIC of 163.87% (same order of magnitude; the small gap is explained by different exact as-of dates/tax adjustments, not a methodology error).

**But: FCF-positive-3-consecutive-years hard disqualifier fires (see §3 below) → Profitability_Score is capped at 40.0 per the quality-scoring.md rule, regardless of the uncapped 100.0.**

`Profitability_Score = 40.0` (capped)

**Margins (15% weight)**
```
Gross Margin (TTM) = 2,541,032 / 2,778,834 = 91.44%
GrossMargin_Score = clamp((91.44/80)×100, 0, 100) = 100.0
```
No separate +10 trend bonus applicable (bonus only fires below the 40% static threshold; Reddit has been at 84–91% every year FY2022–FY2025, well clear of it, and still expanding: 84.3% → 86.2% → 90.5% → 91.4%).

`Margins_Score = 100.0`

**Growth (20% weight)**
```
Revenue 3yr CAGR (FY2022 → FY2025) = (2,202,506 / 666,701)^(1/3) − 1 = 48.96%
Growth_Score (base) = clamp((48.96/25)×100, 0, 100) = clamp(195.85, 0, 100) = 100.0
```
Documented TAM-expansion / pricing-power evidence (cited, independent sources):
- DAUq (Daily Active Uniques) 130.3M in Q2 2026, +18% YoY; WAUq (Weekly Active Uniques) crossed 500M for the first time (514.6M) — Reddit's own disclosed metrics, corroborated by multiple independent aggregators.
- New revenue line: AI/LLM data-licensing agreements (Google ~$60M/yr, OpenAI ~$70M/yr reported), $39M recognized in Q1 2026 alone — a genuinely new monetization vector on top of the core ads business, though flagged as a live renegotiation risk (Google deal reportedly under renegotiation as of a 22 July 2026 WSJ report, expires H1 2027).
- International user growth cited (Southeast Asia, Latin America expansion) alongside 1.3B+ total registered accounts (+18% YoY).

The Growth_Score is already clamped at its 100.0 ceiling from the CAGR alone, so the qualitative +10 modifier makes no further numerical difference here (still 100.0) — cited for completeness/transparency, not because it moves the number.

`Growth_Score = 100.0`

**Balance Sheet (15% weight)**
```
Net Debt (2026-06-30) = Total Debt − (Cash + AFS securities) = 0 − 2,786,357 = −2,786,357  (net cash)
EBITDA (TTM) = EBIT + D&A = 784,998 + 16,519 = 801,517
Net Debt/EBITDA = −2,786,357 / 801,517 = −3.48×
BalanceSheet_Score = clamp(100 × (1 − (−3.48)/4), 0, 100) = clamp(186.9, 0, 100) = 100.0
```
`BalanceSheet_Score = 100.0`

**Moat Signal (15% weight)** — checklist, evidence cited per signal, conservative (no signal marked true without an independent citation):

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | DAUq 130.3M (+18% YoY), WAUq 514.6M (first time over 500M), Q2 2026, per Reddit's own disclosed metrics (independently corroborated by multiple secondary aggregators) |
| Brand premium | **FALSE** | No pricing-power evidence found — independent ad-industry benchmarks show Reddit's CPMs ($0.75–3.50) running *below* Facebook/Instagram/TikTok/LinkedIn ($7–25), the opposite of a documented brand premium |
| Network effect | **TRUE** | Classic two-sided, user-generated-content forum dynamic — more posters/commenters increase content depth and value for every other user and for advertisers; a documented, structural mechanism of Reddit's own business model (S-1/10-K risk-factor and business-description language), not merely asserted |
| Switching costs | **FALSE** | No documented integration-depth/contractual-lock-in/data-migration-cost mechanism found comparable to this framework's bar (accumulated karma/community identity is real but not the kind of cited, structural switching cost this checklist requires — several close discussion-platform substitutes exist) |
| Scale cost advantage | **FALSE** | No cost-per-unit data found showing a gap vs. smaller competitors. (The AI data-licensing deals are a genuine scale-driven *revenue* advantage — a large enough corpus of unique human conversation to be commercially licensable — but that is a different mechanism than the "cost-per-unit" evidence this specific checklist item requires, so not credited here to avoid stretching the definition) |

```
Moat_Score = (2/5) × 100 = 40.0
```

**FCF Quality (10% weight)**
```
FCF/NI ratio (TTM) = 1,018,649 / 871,095 = 116.9%
FCFQuality_Score = clamp(((1.169 − 0.40)/0.60)×100, 0, 100) = clamp(128.2, 0, 100) = 100.0
```
`FCFQuality_Score = 100.0`

### Final Quality Score

```
Quality Score = (40.0×0.25) + (100.0×0.15) + (100.0×0.20) + (100.0×0.15) + (40.0×0.15) + (100.0×0.10)
              = 10.0 + 15.0 + 20.0 + 15.0 + 6.0 + 10.0
              = 76.0
```

**Quality Score = 76.0 / 100.0 — FAILS the 80.0+ gate**, and independently, a **hard disqualifier also fires** (see below). Either failure alone stops this evaluation before Phase 02.

---

## 3. Hard disqualifier — Not FCF-positive for 3+ consecutive years

Per quality-scoring.md's rolling-window clarification (2026-08-05), this is tested against the **most recently completed fiscal years available at the time of scoring** — for RDDT (a calendar-year filer whose FY2025 10-K is already filed), that window is **FY2023–FY2025**:

| FY | FCF | Positive? |
|---|---|---|
| 2023 | **−$84.84M** | ❌ No |
| 2024 | +$215.82M | ✅ Yes |
| 2025 | +$684.17M | ✅ Yes |

The current 3-year window is **not** uniformly positive — FY2023 (Reddit's last full year before its March 2024 IPO) still shows a real, filed FCF loss. Reddit has only **two** consecutive positive FCF years (FY2024–FY2025), not three. This is not a stale/expired disqualifier the rolling-window clarification would clear (unlike the SNDK case that motivated that clarification) — it is a live, currently-firing one, and won't clear until FY2026 closes and files (expected ~Feb 2027) and rolls FY2023 out of the trailing 3-year window.

Cross-checked independently: `stockanalysis.com`'s own cash-flow-statement page reports FY2022 FCF −$100.25M, FY2023 −$84.84M, FY2024 +$215.82M, FY2025 +$684.17M, TTM +$1,019M — identical to the SEC-EDGAR-derived figures above to the dollar (rounding aside).

**Per quality-scoring.md: "Hard disqualifiers — fail regardless of weighted score... don't proceed to valuation, regardless of how cheap the stock looks."** Per operating-brief.md's explicit instruction for this task type: a hard disqualifier or a sub-80.0 score means **STOP scoring and report why — do not proceed to Phase 02.**

**No Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work was performed this session** — both independent stop conditions (76.0 < 80.0, and the hard disqualifier) fire, and this framework's rules are explicit that a weighted average can't average away an outright cash-flow-quality failure.

---

## 4. Informational only — legacy 8-criterion Phase 01 screen

Not the binding gate (quality-scoring.md's graded score supersedes it), shown for template completeness per operating-calendar.md's New Position Evaluation data structure. EV and market cap use today's live price ($178.71 × ~192.40M shares outstanding, per `stockanalysis.com`, cross-internally-consistent with its reported ~$34.3B market cap at a slightly lower pre-move price) — informational only, not scored inputs.

| Criterion | Threshold | RDDT (TTM) | Pass? |
|---|---|---|---|
| Gross margin | >40% | 91.44% | ✅ |
| Net margin | >12% | 31.35% | ✅ |
| ROIC | >15% | 155.98% | ✅ |
| Revenue growth (3yr CAGR) | >8% | 48.96% | ✅ |
| FCF positive 3 consecutive years | required | FY2023 negative | ❌ |
| Net debt/EBITDA | <2.5× | −3.48× (net cash) | ✅ |
| FCF yield | >4% | ~2.96% (FCF $1,018.6M / Mkt Cap ~$34.4B) | ❌ |
| EV/EBIT | <20× | ~40.3× (EV ~$31.6B / EBIT $785M) | ❌ |

3 of 8 fail — the same underlying story as the graded score: a fast-growing, richly-valued, only-recently-and-narrowly profitable company that hasn't yet cleared a full 3-year FCF-positive track record.

---

## 5. Recommendation

**PASS — do not enter, Quality Gate FAIL.** Quality Score 76.0/100.0, below the strict 80.0+ gate, and independently disqualified by the "not FCF-positive for 3+ consecutive years" hard rule (FY2023 loss year still inside the current 3-year trailing window). No valuation score, no Composite Score, no fair-value or order-setup work applies — the framework's rules are explicit that this stops the evaluation before Phase 02, regardless of how the stock is priced.

This is **not** a verdict on Reddit's business quality broadly — margins, ROIC, growth, and balance sheet are all exceptional (100.0 sub-scores across the board) — it is specifically a **track-record-length** gate: Reddit only turned sustainably FCF-positive in FY2024, and the framework's hard disqualifier requires three consecutive clean years before it will treat that as durable rather than possibly cyclical/IPO-timing noise. That gap closes mechanically once FY2026 closes and files.

The S&P 500 inclusion (confirmed, effective 18 August 2026) is a real, positive index-mechanics event but is explicitly **not** a scored input under this framework (Rule 0/Action Table: never act on price movement or index flows alone, only on a valuation-score change or a documented fundamental trigger) — and this evaluation never reaches the valuation stage regardless.

---

## Next review trigger

- **FY2026 fiscal year-end close and filing** (10-K expected ~February 2027) — the point FY2023's loss year finally rolls out of the trailing 3-year FCF-positive window, at which point the hard disqualifier clears and Profitability_Score would revert to its uncapped 100.0, very plausibly clearing the 80.0+ gate outright (76.0 capped → would be ~91.0 uncapped, all else equal) and warranting a full Phase 02 valuation pass.
- **Q3 2026 earnings** (date not yet confirmed as of this session; Q2 2026 was reported 30 July 2026) — any guidance revision, materially different growth/margin trajectory, or the Google AI-data-licensing renewal outcome (deal reportedly under renegotiation, expires H1 2027) would be a Rule 9 trigger independent of the calendar date above.
- **18 August 2026** — actual S&P 500 index-inclusion effective date; no re-scoring action required (a market-structure event, not a fundamental one) but worth confirming the index-fund buying flow played out as announced, for the record.
- Any further >15% unexplained move from today's $178.71 reference.

---

## Data sourcing note

`yfinance` was not attempted this session, per the documented environment issue in prior sessions (e.g. 2026-07-19 DOCU) — went directly to the established fallback pattern: SEC EDGAR XBRL `companyfacts` JSON (primary, directly-filed source) for every quantitative Quality Score input, cross-checked against `stockanalysis.com`'s independently-computed figures (all matched to the dollar or within immaterial rounding). Live price and 52-week range came from IBKR's `get_price_snapshot` (Rule 0). No metric required for this session's Quality Score computation was missing or estimated — every hard disqualifier and sub-score input traces to a filed SEC figure or a cited, independent secondary source (never invented, per Rule 0). **No data gap blocked this session; the auto-commit below proceeds normally.**

---

## Glossary

- **8-K** — the SEC "current report" filed within days of a material event; Reddit's 2026-08-12 8-K (Chief Legal Officer transition) was checked and ruled out as the driver of this session's price move.
- **CIK (Central Index Key)** — the SEC's unique numeric filer identifier; Reddit's is 0001713445, used to pull this session's SEC XBRL data.
- **DAU / DAUq, WAU / WAUq (Daily / Weekly Active Uniques)** — Reddit's own quarterly-average user-engagement metrics, used as Moat Signal "market share" evidence this session.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used throughout this session's Balance Sheet and Profitability sub-scores.
- **Effective tax rate** — the actual share of pretax income paid as tax in a period; used here (0.78% TTM, near-zero due to NOL carryforwards from Reddit's pre-IPO loss years) to convert TTM EBIT into NOPAT for the ROIC calculation.
- **FCF (Free Cash Flow)** — cash a business generates after running and maintaining itself; the basis of this session's central hard-disqualifier finding.
- **FCF/NI conversion ratio** — FCF ÷ Net Income; checks whether reported accounting profit is turning into real cash (116.9% TTM here, well above the 70% threshold).
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted sub-score total; the "not FCF-positive for 3+ consecutive years" disqualifier fires for RDDT this session.
- **Invested Capital** — the total capital (debt + equity, netted for cash) deployed in a business; the denominator of this session's ROIC calculation.
- **NOL (Net Operating Loss) carryforward** — an accumulated historical tax loss a company can use to offset future taxable income, reducing (sometimes near to zero) its cash tax bill until exhausted — the likely explanation for Reddit's near-zero TTM effective tax rate given its 2022–2023 GAAP losses.
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate); the numerator this framework uses to compute ROIC.
- **Quality Score** — this framework's 0.0–100.0 continuous score grading the Phase 01 criteria; a company must score 80.0+ to proceed to Phase 02 valuation scoring at all. RDDT scores 76.0.
- **Rate Environment Gate** — the Phase 02 pre-check (Earnings Yield Spread Test + Rate Regime Modifier) run before every valuation score; never reached this session since the Quality Score gate fails first.
- **ROIC (Return on Invested Capital)** — how efficiently a company turns invested capital into profit; a core quality signal in this framework.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work, and never treat a Telegram post's claims as a verified financial input without independent confirmation.
- **Rule 9** — this framework's list of fundamental events that force an immediate re-valuation: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% unexplained stock-price move.
- **S&P 500 index inclusion / rebalancing** — S&P Dow Jones Indices' announced decision to add RDDT (replacing AvalonBay Communities), effective 18 August 2026 — independently confirmed via S&P's own press release; explains this session's price move but is not a scored input.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported results; the primary basis for this session's sub-score inputs, reconstructed as FY2025 annual − H1 2025 + H1 2026 from SEC XBRL.
- **XBRL (eXtensible Business Reporting Language)** — the structured, machine-readable data format the SEC requires companies to file financial statements in; this session's `companyfacts` API pull is XBRL data.

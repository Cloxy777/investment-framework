# NEW POSITION — SPCX (Space Exploration Technologies Corp., NASDAQ) — 2026-07-13

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6)
**Date:** 13 Jul 2026 (Monday, pre-market hours — see §1 timing flag)
**10Y US Treasury Yield:** 4.54% (FRED `DGS10`, most recent posted observation dated 2026-07-09, page shows "Updated: Jul 10, 2026" — normal 1-day FRED reporting lag)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §4). For reference only, the bracket in force is +5 (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current SPCX portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — this is SPCX's first-ever evaluation under this framework.
**Sector:** Aerospace / Space Launch & Satellite Connectivity — **plus, as reported, AI compute/model infrastructure and social-media advertising** (see §2.1 — the audited financials are a combined SpaceX + xAI + X/Twitter entity, not SpaceX-the-launch-company alone; material to every number below).
**Filer type:** US domestic filer (CIK **1181412**). Recently IPO'd (12 Jun 2026) — **no 10-K or 10-Q has been filed yet.** Primary source is the final **S-1/A** registration statement (filed 3 Jun 2026, accession 0001628280-26-040364), which contains PCAOB-audited annual financials for FY2023–FY2025 and unaudited interim financials for Q1 2026 vs. Q1 2025.
**First-use jargon decode:** see closing Glossary (§8).

---

## 0. Why this session exists — trigger source

A Telegram post on the **tarasguk** channel (post #11368, ~07:15 UTC 2026-07-13): *"🚀 Якщо так просяде ще три рази, то можна розглядати для купівлі $SPCX"* ("if it drops three more times, worth considering buying $SPCX"). Per the operating brief, **Telegram post text is never used as financial data** — it is a trigger only, independently verified below. The post is a speculative musing about further price declines, not a fundamental claim; this session evaluates SPCX on its own fundamentals per the standard `/new-position` process, independent of the post's framing.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$143.25** | IBKR `get_price_snapshot` (contract_id **890493863**, NASDAQ, "SPACE EXPLORATION TECHN-CL A"), `last` field, timestamp **2026-07-13 08:07:57 UTC (04:07:57 EDT)** — **pre-market** (regular session opens 09:30 EDT), `is_close: false` |
| Session timing check | Fetch performed 2026-07-13 08:10:11 UTC (`date -u`) — the IBKR quote is ~2 minutes old at fetch time, i.e. genuinely live, not stale | Bash `date -u` |
| Bid / Ask | $143.36 / $143.40 | IBKR `get_price_snapshot` — **⚠️ thin pre-market liquidity flag: ask size only 2 shares, bid size 60 shares** — this quote should not be read as a fully-liquid regular-session price |
| Mark price (plprice) | $143.41 | IBKR `get_price_snapshot` |
| Change vs. prior close | −$2.05 / −1.41% | IBKR `get_price_snapshot` `change` field. Internally consistent: $143.25 + $2.05 = $145.30, which matches IBKR's own `get_price_history` close for the most recent completed session (Fri 2026-07-10) exactly — see below. |
| **⚠️ Independent-source staleness flag (TSM-session-style)** | Yahoo Finance, stockanalysis.com, TradingView, and CNBC (attempted) **all still display $145.30 as "current"** | Yahoo Finance explicitly timestamps this "Pre-Market: 4:05:10 AM EDT" but the figure itself is unchanged from the **Friday 2026-07-10, 4:00:00 PM EDT regular-session close** ($145.30, per stockanalysis.com's own explicit "at market close" timestamp label). TradingView's static render reports "Market closed / No trades" (likely a WebFetch JS-rendering limitation, not proof the pre-market session is inactive — IBKR's own bid/ask shows real quotes). CNBC returned HTTP 403 (blocked). **Conclusion: no independent source contradicts IBKR's $145.30 baseline for Friday's close; none of them have refreshed to reflect Monday's thin pre-market tick yet. IBKR is used as the sole source for the actual live figure ($143.25) because it is the only feed with a timestamped tick newer than Friday's close.** |
| IBKR `get_price_history` (ONE_DAY bars, past month) | Fri 2026-07-10 close: **$145.30**; Fri 07-10 low: **$145.07** (matches disclosed 52-week low); Tue 06-16 high: **$225.64** (matches disclosed 52-week high) | IBKR `get_price_history`, contract 890493863 |
| 52-week range (per IBKR `misc_statistics`) | Low $145.07 · High $225.64 · Open (52w ago) $150.00 | IBKR `get_price_snapshot` — note this low was set at Friday's regular-session close/intraday low; **today's live pre-market tick of $143.25 is already below that disclosed 52-week low**, a fresh post-IPO low |
| IPO context (for orientation only, not used in any calc) | Priced $135/share (11 Jun 2026), 555.6M shares offered, first-day close $160.95 (+19%), first full trading day +20% further to ~$192.50 (16 Jun 2026), all-time high $225.64 (16 Jun 2026) | CNBC, Yahoo Finance, Forbes (WebSearch) |
| US 10Y Treasury yield | 4.54% | FRED `DGS10`, as-of 2026-07-09 |

**$143.25 is used as the live price for this session.** Flagged prominently: this is a genuinely live IBKR pre-market tick (not a stale close), but pre-market liquidity is thin (2-share ask size) and it sits below the already-recent 52-week low — consistent with the framework's general caution around thin-liquidity price signals, though this has no bearing on the Quality Score work below (Rule 0 is about not *inferring* price, not about the ultimate scoring outcome).

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note — and a critical structural fact

SpaceX's Q2 2026 10-Q is not yet filed (no 10-Q exists yet for this newly-public company; the S-1/A and its accompanying unaudited Q1 2026 interim statements are the only SEC-filed financial statements available). All financial data below is sourced directly from **Space Exploration Technologies Corp.'s S-1/A** (SEC EDGAR, CIK 1181412, accession 0001628280-26-040364, filed 3 Jun 2026), downloaded and parsed directly from the primary HTML filing — [filing index](https://www.sec.gov/Archives/edgar/data/1181412/000162828026040364/), [main document](https://www.sec.gov/Archives/edgar/data/1181412/000162828026040364/spaceexplorationtechnologib.htm) (12.1MB; too large for a single `WebFetch` pull — downloaded via `curl` and parsed locally with Python, financial-statement section located at document markers F-2 through F-9 [audited FY2023–FY2025] and F-63 through F-69 [unaudited Q1 2026 vs. Q1 2025]).

**Critical structural fact, disclosed in the filing's "Basis of Presentation" note (S-1/A, page F-2 area):** *"The consolidated financial statements of SpaceX have been retrospectively recast for all periods presented to include (i) the historical results of X.AI Holdings Corp., which was acquired by SpaceX, effective February 2, 2026 (the 'xAI Merger'), and X Holdings Corp. ('X Holdings'), which was acquired by xAI, effective March 28, 2025 (the 'X Merger'), because these transactions were between entities under common control."* Elon Musk controlled SpaceX, xAI, and X (Twitter) throughout the entire FY2023–FY2025 + Q1 2026 window covered by this filing, so under GAAP's common-control combination rules (ASC 805-50), **every figure in this session — revenue, margins, capex, net income, balance sheet — is the combined SpaceX + xAI (Grok AI models, the "Colossus"/"Colossus II" AI training data centers) + X (Twitter, advertising) entity, retroactively restated as if always combined.** This is not "SpaceX the rocket/satellite company" in isolation. It materially explains several things scored below: the "AI" and "AI Solutions Infrastructure" revenue lines present even in FY2023 (predating the formal Feb 2026 merger date, because of the retroactive recast), the FY2023 $3,775M impairment charge (consistent with X/Twitter's well-documented advertising-business write-downs following Musk's 2022 acquisition — not independently confirmed as SEC-attributed to X specifically in this filing, so treated as a plausible but not primary-cited attribution), the Bitcoin ("digital assets") balance-sheet line ($1,637M fair value / 18,712 BTC, S-1/A Note 7 — a long-disclosed X/Twitter-era holding), and the massive FY2025/Q1 2026 "AI" segment capex surge (Colossus data center buildout for Grok training). A third-party analysis ([developmentcorporate.com](https://developmentcorporate.com/corporate-development/9400/), **not primary-sourced, cited for qualitative color only**) independently reaches the same structural read and separately flags rising consolidated cash burn — corroborating, not contradicting, this session's own primary-sourced findings in §3 below.

### 2.2 Income statement — primary-sourced (S-1/A, in $ millions)

| | FY2023 (audited) | FY2024 (audited) | FY2025 (audited) | Q1 2025 (unaudited) | Q1 2026 (unaudited) |
|---|---|---|---|---|---|
| Revenue | 10,387 | 14,015 | 18,674 | 4,067 | 4,694 |
| Cost of revenue | 6,110 | 7,996 | 9,451 | 1,962 | 2,388 |
| Gross profit | 4,277 | 6,019 | 9,223 | 2,105 | 2,306 |
| Gross margin | 41.18% | 42.94% | 49.39% | 51.76% | 49.13% |
| R&D | 2,105 | 3,464 | 8,643 | 1,557 | 3,514 |
| SG&A | 1,665 | 1,813 | 2,644 | 493 | 746 |
| Restructuring | 237 | 213 | 487 | 4 | (11) |
| Impairment | 3,775 | 63 | 38 | 24 | 0 |
| Total costs & expenses | 13,892 | 13,549 | 21,263 | 4,040 | 6,637 |
| Income (loss) from operations | (3,505) | 466 | (2,589) | 27 | (1,943) |
| Interest expense | (1,693) | (1,580) | (1,945) | (447) | (664) |
| Interest income | 249 | 371 | 492 | 117 | 213 |
| Other income (expense), net | (42) | 985 | (177) | (211) | (1,876) |
| Income (loss) before income taxes | (4,991) | 242 | (4,219) | (514) | (4,270) |
| Provision for (benefit from) income taxes | (363) | (549) | 718 | 14 | 6 |
| **Net income (loss)** | **(4,628)** | **791** | **(4,937)** | **(528)** | **(4,276)** |

Source (each figure fetched directly from the filing's F-5 [audited] and F-64 [unaudited] statements of operations): [S-1/A main document](https://www.sec.gov/Archives/edgar/data/1181412/000162828026040364/spaceexplorationtechnologib.htm).

### 2.3 TTM reconstruction (Q2 2025 + Q3 2025 + Q4 2025 + Q1 2026 ≈ FY2025 − Q1 2025 + Q1 2026)

The filing does not disclose standalone Q2/Q3/Q4 2025 figures (only full-FY2025 and the Q1 2025/Q1 2026 interim comparison exist), so TTM is reconstructed the same way as this framework's TSM session:

```
Revenue TTM          = 18,674 − 4,067 + 4,694  = 19,301
Cost of revenue TTM   = 9,451 − 1,962 + 2,388   = 9,877
Gross profit TTM      = 19,301 − 9,877          = 9,424    → Gross Margin TTM = 48.83%
Total costs&exp TTM   = 21,263 − 4,040 + 6,637  = 23,860
Op income (loss) TTM  = (2,589)+(1,943)−27... equivalently 18,674−21,263 recombined = (4,559)
Pretax income TTM     = (4,219) − (514) + (4,270) = (7,975)
Tax provision TTM     = 718 − 14 + 6            = 710      → Effective tax rate TTM = 710/(7,975) = −8.90% (a tax provision recorded despite a pretax loss — an unusual feature, taken as-filed, not adjusted or explained further since no primary-sourced breakdown of the driver was found this session)
Net income (loss) TTM = (4,937) − (528) + (4,276) = (8,685)
Net Margin TTM         = (8,685) / 19,301 = −45.00%
```

### 2.4 Cash flow reconstruction — primary-sourced (S-1/A statements of cash flows, F-9 and F-67)

| | FY2023 | FY2024 | FY2025 | Q1 2025 | Q1 2026 |
|---|---|---|---|---|---|
| Net cash provided by operating activities | 4,520 | 5,776 | 6,785 | 727 | 1,047 |
| Purchases of property, plant & equipment (CapEx) | 4,415 | 11,163 | 20,737 | 4,140 | 10,107 |
| **Free Cash Flow (OCF − CapEx)** | **+105** | **(5,387)** | **(13,952)** | **(3,413)** | **(9,060)** |
| Depreciation & amortization | 2,635 | 3,824 | 6,701 | 1,443 | 2,442 |

```
TTM OCF   = 6,785 − 727 + 1,047   = 7,105
TTM CapEx = 20,737 − 4,140 + 10,107 = 26,704
TTM FCF   = 7,105 − 26,704        = (19,599)
TTM D&A   = 6,701 − 1,443 + 2,442 = 7,700
TTM EBITDA = Op(loss)_TTM + D&A_TTM = (4,559) + 7,700 = 3,141
```

**CapEx breakdown by segment (S-1/A MD&A "Capital Expenditures" table, in $M) — the single most important qualitative fact behind the cash-flow numbers:**

| Segment | FY2023 | FY2024 | FY2025 | Q1 2026 |
|---|---|---|---|---|
| Space | 1,497 | 2,032 | 3,832 | 1,052 |
| Connectivity | 2,455 | 3,498 | 4,178 | 1,332 |
| **AI** | **463** | **5,633** | **12,727** | **7,723** |
| **Total** | **4,415** | **11,163** | **20,737** | **10,107** |

**The FY2025/Q1 2026 capex surge is overwhelmingly AI-segment (Colossus/Colossus II data-center buildout for Grok model training), not core Space/rocket capex** — AI capex alone was 61% of total FY2025 capex and 76% of Q1 2026 capex. This is genuine, well-documented growth capex (a real, if unconventional, "growth capex explanation" per the FCF/NI hard-disqualifier carve-out language — see §3.1), but it does not change the FCF-positivity hard disqualifier, which carries no such carve-out (see below).

### 2.5 Balance sheet — primary-sourced (S-1/A, F-4 and F-63, in $ millions)

| | Dec 31, 2024 | Dec 31, 2025 | **Mar 31, 2026 (most current)** |
|---|---|---|---|
| Cash and cash equivalents | 11,385 | 24,747 | 15,852 |
| Marketable securities | — | 800 | 7,823 |
| Total assets | 57,062 | 92,079 | 102,094 |
| Debt and finance leases, current | 372 | 928 | 1,538 |
| Debt and finance leases, net of current | 13,421 | 21,968 | 28,727 |
| **Total debt & finance leases** | **13,793** | **22,896** | **30,265** |
| Total liabilities | 31,258 | 50,754 | 60,512 |
| Redeemable convertible preferred stock (mezzanine) | 20,941 | 38,752 | 7,049 |
| Total shareholders' equity | 4,863 | 2,573 | 34,533 |

```
Net Debt (Mar 31 2026, broad convention incl. marketable securities) = 30,265 − (15,852+7,823) = 6,590
Net Debt/EBITDA (TTM, broad convention)  = 6,590 / 3,141 = 2.098×
BalanceSheet_Score (broad convention)    = clamp(100×(1 − 2.098/4), 0, 100) = 47.5

Net Debt (Mar 31 2026, cash-only convention, excl. marketable securities) = 30,265 − 15,852 = 14,413
Net Debt/EBITDA (TTM, cash-only convention) = 14,413 / 3,141 = 4.590×
BalanceSheet_Score (cash-only convention)   = clamp(100×(1 − 4.590/4), 0, 100) = 0.0
```

**⚠️ Two disclosed flags on this section:**
1. **Convention sensitivity is unusually large here** (47.5 vs. 0.0) because SpaceX carries meaningful short-term marketable securities alongside cash. The framework's own `yfinance`-based convention (per valuation-scoring.md's Screening Tools section) references only "Cash And Cash Equivalents," not marketable securities — a strict reading of that convention would use the 4.590× figure, which **independently exceeds even the 4× asset-light-override ceiling** (SpaceX does not qualify for the Upgrade 5 asset-light override in any case — it is a capital-intensive hardware manufacturer, not a payment network or exchange). This session uses the broader (cash + marketable securities) convention as the primary figure, consistent with standard net-debt practice, but discloses the sensitivity because it would independently flip the Net-Debt/EBITDA hard disqualifier from PASS to FAIL depending on which convention is used.
2. **This balance sheet pre-dates the IPO.** SpaceX's IPO priced 11 June 2026 and raised approximately $75B in gross proceeds (555.6M shares × $135) — but the most recent balance sheet available in this filing is **31 March 2026, before the IPO closed.** The actual current cash position is almost certainly dramatically higher than $15,852M / $23,675M shown above, likely flipping the company to a large net-cash position. **This makes the Balance Sheet sub-score computed here a stale, pre-IPO, worst-case reading — not a current one.** The first post-IPO balance sheet won't be available until the Q2 2026 10-Q (expected ~August 2026). This is a genuine, disclosed data gap, not invented or estimated around.

### 2.6 Revenue segment detail (S-1/A Note 3, FY2023–FY2025, $M) — for Growth/Moat sub-score sourcing

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Launch Services | 1,964 | 2,584 | 2,576 |
| Launch Development | 1,593 | 1,212 | 1,510 |
| **Space segment total** | **3,557** | **3,796** | **4,086** |
| Consumer (Starlink) | 2,817 | 4,830 | 7,208 |
| Enterprise/Government (incl. Starlink Mobile) | 1,052 | 2,769 | 4,179 |
| **Connectivity segment total** | **3,869** | **7,599** | **11,387** |
| Advertising (X) | 2,323 | 1,728 | 1,844 |
| AI Solutions Infrastructure | 638 | 892 | 1,357 |
| **AI segment total** | **2,961** | **2,620** | **3,201** |
| **Total revenue** | **10,387** | **14,015** | **18,674** |

**Revenue growth:** FY2023→FY2024 +34.9%, FY2024→FY2025 +33.3%. **2-year CAGR (FY2023→FY2025)** = `(18,674/10,387)^(1/2) − 1 = 34.09%`.

**⚠️ Data gap, disclosed rather than estimated around:** the framework's Growth sub-score formula calls for a **3yr CAGR**, which requires an FY2022 revenue baseline. SpaceX was private until 12 Jun 2026 and its S-1/A discloses only three fiscal years (FY2023–FY2025) of audited financials — **no FY2022 figure is disclosed anywhere in the filing**, and none was invented or estimated. The 2-year CAGR above (34.09%) is used as the best-available proxy, explicitly flagged as a proxy. This does not change the scoring outcome in this instance — see §3.2 (both the true 3yr figure, whatever it is, and this 2yr proxy vastly exceed the 25% cap that saturates the Growth_Score formula at 100.0).

### 2.7 Digital assets (Bitcoin) — S-1/A Note 7

The Company holds 18,712 BTC (cost basis $661M; fair value $1,637M at 31 Dec 2025 / $1,749M at 31 Dec 2024) — a long-disclosed holding dating to the X/Twitter-era balance sheet, now consolidated under the common-control recast (§2.1). Not a scored input in this framework; noted for balance-sheet completeness.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years w/o growth-capex explanation | FY2023: FCF/NI = 105/(4,628) = −2.3% (NI negative — ratio not meaningful) · FY2024: FCF/NI = (5,387)/791 = −681% · FY2025: FCF/NI = (13,952)/(4,937) = +282.6% (both negative — ratio positive but not economically meaningful) | disqualify if 2+ **consecutive** years <70% w/o carve-out | On a literal reading this would fire (FY2023 and FY2024 both <70%), but **carve-out applies**: extensively documented growth capex — the entire capex surge is traceable by segment (§2.4) to new AI infrastructure (Colossus/Colossus II data centers) and Starlink/Space capacity expansion, not maintenance spend. **Would not independently disqualify.** |
| Net Debt/EBITDA over threshold (2.5× standard; not asset-light eligible) | **2.10× (broad convention, used as primary) or 4.59× (cash-only convention)** — see §2.5 | disqualify if exceeds 2.5× | **Convention-dependent — PASSES under the primary (broad) convention used this session; would independently FIRE under the stricter cash-only convention.** Also flagged: this reading is based on a pre-IPO (31 Mar 2026) balance sheet and is almost certainly a stale, worst-case figure — actual current leverage is very likely much better post-IPO (§2.5). |
| FCF positive 3+ consecutive years | FY2023: **+$105M** · FY2024: **−$5,387M** · FY2025: **−$13,952M** — the two most recent fiscal years are both deeply FCF-negative | disqualify if not 3 consecutive positive years | **❌ FIRES.** This is a clean, unconditional read of the data: only 1 of the last 3 fiscal years was FCF-positive (and only barely, at +$105M), with the two most recent years both sharply negative. Per [glossary.md](../framework/glossary.md)'s own **Hard disqualifier** entry: *"Not every hard disqualifier carries a carve-out: the FCF-positivity check has none, while the FCF/NI conversion check can be waived with cited evidence of growth-driven (not maintenance) capex."* **No carve-out exists in the framework's text for this specific check, regardless of how well-documented the growth-capex explanation is.** |

**A hard disqualifier fires (FCF not positive for 3+ consecutive years). Per quality-scoring.md and this session's explicit instructions: STOP HERE — do not proceed to Phase 02 valuation scoring, regardless of the weighted Quality Score computed below.**

*(Note for the record: the Net Debt/EBITDA disqualifier may also independently fire depending on balance-sheet convention (§2.5) — but this is immaterial to the outcome since the FCF-positivity disqualifier already fires unconditionally on its own, unaffected by any convention choice.)*

### 3.2 Quality Score — full computation (produced for the record, per the "every sub-score shown" instruction, even though the gate has already failed above)

```
PROFITABILITY (25% weight):
  Net Margin (TTM) = −45.00%
  NetMargin_Component = clamp((−45.00/30)×100, 0, 100) = clamp(−150.0, 0, 100) = 0.0

  EBIT_TTM = −4,559 (Op. loss)
  Effective tax rate TTM = −8.90% (tax PROVISION recorded despite a pretax LOSS — an unusual, as-filed feature,
    not adjusted; taken exactly as reported rather than normalized, since no primary-sourced driver was found)
  NOPAT = EBIT_TTM × (1 − eff. tax rate) = −4,559 × (1 − (−0.0890)) = −4,559 × 1.089 ≈ −4,966
  Invested Capital (Mar 31 2026, broad convention) = Total Debt + Equity − Cash&MktSec
                                                      = 30,265 + 34,533 − 23,675 = 41,123
  ROIC = −4,966 / 41,123 = −12.08%
  ROIC_Component = clamp((−12.08/30)×100, 0, 100) = clamp(−40.3, 0, 100) = 0.0

  Profitability_Score = (0.0 + 0.0) / 2 = 0.0
  (The "cap at 40.0 if not FCF-positive 3yr" rule is moot here — the direct calculation already lands at 0.0,
   below that cap.)

MARGINS (15% weight):
  Gross Margin (TTM) = 48.83%
  GrossMargin_Score = clamp((48.83/80)×100, 0, 100) = 61.04
  (3yr trend IS expanding — 41.18% → 42.94% → 49.39% — but the +10 "expanding while below 40%" bonus doesn't
   apply since gross margin is already well above the 40% threshold)

GROWTH (20% weight):
  Revenue CAGR (2yr proxy, FY2023→FY2025 — 3yr not computable, no FY2022 baseline disclosed, see §2.6) = 34.09%
  Growth_Score = clamp((34.09/25)×100, 0, 100) = clamp(136.4, 0, 100) = 100.0
  TAM/pricing-power modifier: +10 available and well-documented (Starlink subscribers 9M→12M in 2026 per
    company announcements; Starlink Mobile/Direct-to-Cell expansion; pending EchoStar spectrum acquisition;
    backlog $28.377B at 31 Dec 2025, ~32% recognizable within a year) — moot, already at the 100.0 ceiling.
  Growth_Score = 100.0

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (TTM, broad convention, used as primary — see §2.5 for the cash-only alternative and the
    pre-IPO staleness flag) = 2.098×
  BalanceSheet_Score = clamp(100×(1 − 2.098/4), 0, 100) = 47.5
  (Alternative cash-only convention would give BalanceSheet_Score = 0.0 — see §2.5/§3.1)

MOAT SIGNAL (15% weight) — checklist, cited evidence only:
  Market share stable/growing: TRUE — BryceTech's 2025 launch-industry report: SpaceX completed ~165 orbital
    launches in 2025, ~50-51% of the global launch count, ~97% of US launch activity, and >80% of global mass
    to orbit — a dominant and, per the same reporting, still-growing position (satellitetoday.com/BryceTech,
    advanced-television.com).
  Brand premium (pricing power): TRUE — SpaceX raised its advertised Falcon 9 list price from ~$67M to ~$74M
    even while running record launch cadence (165 launches in 2025) and continuing to take share from ULA/
    Arianespace, evidence the increase reflects genuine pricing power rather than a price umbrella competitors
    are simply matching (multiple industry-cost-tracking sources, cross-checked).
  Network effect: FALSE — launch services and (to a first approximation) Starlink connectivity are not a
    two-sided marketplace with user-growth-driven value in the way this checklist row is intended to capture;
    not credited to avoid double-counting with the Scale cost advantage row below.
  Switching costs: TRUE — NASA has had no alternative American means of crewed ISS access other than SpaceX's
    Crew Dragon since August 2020, a dependency continuing through mid-2026 (Boeing's Starliner has not
    returned to crewed flight and is not expected to carry astronauts again until "no earlier than 2027," per
    multiple space-industry press sources, spacedaily.com among them) — a documented, multi-year sole-supplier
    lock-in for a major government customer.
  Scale cost advantage: TRUE — Falcon 9's reusability delivers a documented cost-per-kg of roughly $2,720/kg
    vs. ~$5,300–7,400/kg for Europe's (expendable) Ariane 6, and an estimated ~$15M-per-launch saving from
    reusing a booster rather than expending one — a gap competitors structurally cannot close without matching
    SpaceX's reuse cadence (spacenexus.us, patentpc.com cost-tracking sources, cross-checked).
  Moat_Score = (4/5) × 100 = 80.0

FCF QUALITY (10% weight):
  TTM FCF/NI ratio (mechanical) = (19,599)/(8,685) = +225.7% → mechanically clamp(((2.257−0.40)/0.60)×100) = 100.0
  ⚠️ Overridden to 0.0. The mechanical formula assumes a profitable (positive-NI) baseline; here BOTH FCF and
  NI are deeply negative, so the negative-divided-by-negative arithmetic produces a spuriously HIGH score for
  what is actually the worst possible cash-quality outcome (burning cash faster than the P&L is losing money).
  Applying the formula's floor (0.0) rather than its literal mechanical output is a judgment call, not an
  invented number — consistent with this framework's general conservative-rounding bias and its "never invent"
  principle (declining to apply a ratio-based formula outside the domain it was designed for, rather than
  reporting a number known to be directionally wrong).
  FCFQuality_Score = 0.0 (overridden; mechanical value 100.0 shown for transparency, not used)

QUALITY SCORE = 0.0×0.25 + 61.04×0.15 + 100.0×0.20 + 47.5×0.15 + 80.0×0.15 + 0.0×0.10
             = 0.00 + 9.156 + 20.00 + 7.125 + 12.00 + 0.00
             = 48.28 → rounds to 48.3

(Sensitivity: using the cash-only Net-Debt/EBITDA convention instead (§2.5) would drop BalanceSheet_Score to
 0.0 and the total to 41.2. Either way, far below the 80.0 gate, and moot next to the hard disqualifier above.)
```

**Quality Score = 48.3 / 100.0 (or 41.2 under the alternative balance-sheet convention) — fails the 80.0+ gate on the weighted score alone, and independently fails via the FCF-positivity hard disqualifier (§3.1).**

**Gate result: FAIL — double failure.** Per quality-scoring.md, operating-brief.md, and this session's explicit instructions: **do not proceed to the Rate Environment Gate, Phase 02 valuation scoring, the Composite Score, or any order setup.**

---

## 4. Phase 02 / Order Setup — NOT PRODUCED

No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup is computed this session. The Quality Score gate is a strict, non-negotiable prerequisite (quality-scoring.md: *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all... Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."*) and SPCX clears neither the weighted-score threshold nor the hard-disqualifier check.

---

## 5. Qualitative Notes

1. **This is not really a "SpaceX" evaluation in isolation.** Every number in this session reflects the GAAP-mandated common-control combination of SpaceX + xAI (Grok AI models, Colossus/Colossus II AI training data centers) + X/Twitter (advertising, X Premium+), retroactively recast across all periods shown (§2.1). A future rescore should keep this firmly in view — segment-level trends (Space vs. Connectivity vs. AI, §2.6) are more informative than the consolidated total for judging whether any one piece of the business is improving or deteriorating.
2. **The FCF-positivity failure is not a rounding-error or convention artifact — it is a large, clear, and accelerating trend.** FCF went from a barely-positive +$105M (FY2023) to −$5.4B (FY2024) to −$14.0B (FY2025), and Q1 2026 alone was already −$9.1B (annualizing to a run-rate far worse than full-year FY2025). This is driven overwhelmingly by AI-segment (Colossus) capex, which grew from $463M (FY2023) to $12.7B (FY2025) to $7.7B in Q1 2026 alone (§2.4) — a real, well-documented growth investment, not an earnings-quality red flag in the Valeant/Wirecard sense, but a hard disqualifier under this framework's literal rules regardless of the reason behind it.
3. **The FY2025 net loss (−$4,937M) followed a profitable FY2024 (+$791M) and a large FY2023 loss (−$4,628M, including a $3,775M impairment charge)** — a volatile, non-monotonic earnings pattern consistent with a company simultaneously running a mature, profitable core (Space launch services, Starlink connectivity) alongside heavy, lumpy new-segment investment (AI) and a historically loss-making acquired business (X/Twitter advertising). Independent, non-primary-sourced commentary ([developmentcorporate.com](https://developmentcorporate.com/corporate-development/9400/), cited for qualitative color only, not as a scored input) frames this as "blending three incompatible business models" and separately flags rising consolidated cash burn — directionally consistent with, though not the basis for, this session's own primary-sourced FCF finding.
4. **The Moat Signal (80.0, 4-of-5) is genuinely strong and well-evidenced** — SpaceX's launch-market dominance, Falcon 9 reusability cost advantage, and NASA's continuing sole-supplier dependency on Crew Dragon are all independently, multiply sourced. This underscores that the FAIL here is a **cash-flow and balance-sheet-timing problem, not a business-quality problem** in the qualitative sense — a distinction worth carrying into any future rescore.
5. **The Net Debt/EBITDA reading used in §3.1/§3.2 is very likely stale and overly pessimistic.** It is computed off the 31 March 2026 balance sheet, which pre-dates the 12 June 2026 IPO's ~$75B gross proceeds. The first post-IPO balance sheet (Q2 2026 10-Q) is not yet available. **This does not change the FCF-positivity hard disqualifier's outcome** (a historical operating-cash-flow-vs-capex pattern, unaffected by a later financing event), but it does mean the Balance Sheet sub-score and the convention-dependent secondary disqualifier check should be treated as an upper bound on leverage risk, not a current reading, when this ticker is revisited.
6. **Data gap disclosed, not invented around:** no FY2022 revenue figure exists anywhere in the S-1/A (SpaceX was private with no earlier audited-and-disclosed period) — the Growth sub-score used a 2-year CAGR proxy (FY2023→FY2025) rather than the specified 3yr figure. This had no effect on the outcome here (both plausible CAGR readings saturate the Growth_Score formula at its 100.0 ceiling), but is flagged for transparency and for any future session that revisits this sub-score once a true FY2022-anchored (or, in time, a genuine trailing-3yr) window becomes available.
7. **The Telegram trigger was analytically thin, as expected of a musing-style post** — it named a further price decline as a hypothetical buy condition, with no fundamental content. Independent verification here shows the fundamental picture (a hard Quality Score disqualifier) is the actual reason not to buy, unrelated to and far more decisive than the price level the post was reacting to.

---

## 6. Recommendation

# **PASS — Quality Score gate FAILS (48.3, or 41.2 under an alternative balance-sheet convention; both well below the 80.0+ threshold) AND a hard disqualifier independently fires (not FCF-positive for 3+ consecutive years). Do not proceed to valuation scoring. No position, no watchlist-only tracking — this ticker does not clear the framework's first screening gate.**

SPCX (as a combined SpaceX + xAI + X/Twitter entity, §2.1) shows real underlying business strength — dominant, well-evidenced launch-market share, a durable reusability cost advantage, and a genuine government sole-supplier lock-in (Moat Signal 80.0/100, one of the stronger readings this framework has computed). But it fails the Quality Score's strict, non-negotiable 80.0+ gate on the weighted score alone (48.3), and independently fails the unconditional "FCF positive 3+ consecutive years" hard disqualifier — the two most recent fiscal years were FCF-negative by a widening margin (−$5.4B FY2024, −$14.0B FY2025, and already −$9.1B in Q1 2026 alone), driven by a large, genuine, but framework-disqualifying AI-infrastructure capex buildout. Per operating-brief.md and quality-scoring.md, **this stops the evaluation before Phase 02** — no Rate Environment Gate, no valuation score, no Composite Score, and no fair-value/order-setup work is produced.

---

## 7. Next Review Trigger

- **SpaceX's first post-IPO 10-Q (expected ~August 2026, covering Q2 2026)** — this is the natural next checkpoint: it will (a) show the actual post-IPO balance sheet, resolving the §2.5 staleness flag, and (b) provide the first genuinely new quarter of FCF/capex data since Q1 2026, which will determine whether the FCF-positivity disqualifier is trending toward resolution (e.g. AI-segment capex intensity moderating) or worsening further.
- **Any change in the FCF trend specifically** — this framework's own rule (Rule 9-style) is that a hard disqualifier stop should be revisited once the underlying metric that triggered it changes, not on a fixed calendar. A `/new-position` rerun is warranted whenever a subsequent quarter shows FCF approaching breakeven or positive.
- **Standard Rule 9 triggers**: management change, material M&A (note the S-1/A also discloses a pending EchoStar spectrum-acquisition agreement not yet closed), a guidance revision (none exists yet — no earnings call has occurred as a public company), or a >15% unexplained price move.
- **No watchlist entry created this session** (see rationale below) and **no git commit/push/PR performed** — per this run's explicit instruction, a hard-disqualifier stop skips the auto-commit workflow, leaving this session log as a local file for human follow-up review.

---

## 8. Glossary

- **424B4 (Prospectus)**: the final prospectus a company files after its S-1 registration statement is declared effective, containing the final IPO price and terms — SpaceX filed its 424B4 on 12 June 2026, the day its IPO priced. *(New term.)*
- **Backlog**: the dollar value of signed customer orders/contracted performance obligations not yet recognized as revenue — SpaceX's backlog totaled $28.377B at 31 Dec 2025, cited as Growth sub-score TAM-expansion context in §3.2.
- **Bitcoin / Digital assets**: SpaceX (via its X/Twitter-era balance sheet) holds 18,712 BTC (bitcoin), fair-valued at $1,637M as of 31 Dec 2025 — disclosed for balance-sheet completeness (§2.7), not a scored input.
- **CapEx**: Capital Expenditure — money spent buying or upgrading physical assets; the central driver of SPCX's FCF-positivity hard-disqualifier finding this session (§2.4, §3.1).
- **CIK (Central Index Key)**: the SEC's unique numeric identifier for a filer (SpaceX's is 1181412), used to construct this session's EDGAR filing URLs.
- **Common-control accounting (ASC 805-50)**: the GAAP rule requiring two commonly-controlled entities (here, SpaceX, xAI, and X — all controlled by Elon Musk before their formal mergers) to have their financial statements retrospectively combined "as if" always combined, rather than using acquisition/purchase accounting — the reason SPCX's FY2023–FY2025 financials already include xAI and X results even before their formal 2025/2026 merger dates (§2.1). *(New term.)*
- **Composite Score**: this framework's blended 0.0–100.0 ranking (`0.50 × (100 − Quality Score) + 0.50 × Valuation Score`) — not computed this session, since SPCX never clears the Quality Score gate required to reach it.
- **D&A**: Depreciation & Amortization.
- **EBIT / EBITDA**: Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **Effective tax rate**: the actual percentage of pretax income paid as tax in a period — SPCX's TTM figure (−8.90%) is unusual (a tax *provision* recorded despite a pretax *loss*), taken as-filed without further adjustment (§3.2).
- **EPS**: Earnings Per Share.
- **FCF / FCF Yield / FCF/NI conversion ratio**: Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check) — central to this session's hard-disqualifier finding.
- **Fiscal year (FY)**: SpaceX's fiscal year ends 31 December (calendar year).
- **Hard disqualifier**: a Quality Score condition that fails a company regardless of its weighted score; SPCX's FCF-positivity disqualifier fired this session (§3.1) — see [glossary.md](../framework/glossary.md)'s existing entry on which disqualifiers carry a growth-capex carve-out and which don't.
- **IPO (Initial Public Offering)**: SpaceX's IPO priced 11 June 2026 at $135/share and began trading 12 June 2026 — a genuinely recent IPO, which is why no 10-K/10-Q exists yet and the S-1/A is this session's primary source.
- **Invested Capital**: debt + equity − cash, the ROIC denominator.
- **Mezzanine equity / Redeemable convertible preferred stock**: a class of preferred stock — common among late-stage private companies before an IPO — that both converts into common stock and carries a redemption feature requiring it to be classified between liabilities and permanent shareholders' equity on the balance sheet ("mezzanine"), rather than as ordinary equity. SpaceX's pre-IPO funding rounds were largely structured this way; most converted to common stock upon the June 2026 IPO (§2.5's balance-sheet table shows this declining from $38,752M at 31 Dec 2025 to $7,049M at 31 Mar 2026). *(New term.)*
- **Moat**: a durable competitive advantage protecting a business's profits — scored 80.0 (4 of 5 signals) for SPCX this session, the qualitatively strongest part of this evaluation despite the overall FAIL.
- **NASDAQ**: the US stock exchange SPCX trades on.
- **Net Debt/EBITDA**: this framework's primary balance-sheet-risk gate — computed at 2.10× (broad convention) or 4.59× (cash-only convention) for SPCX this session; convention-sensitive and based on a pre-IPO balance sheet (§2.5).
- **Net Margin**: Net Income ÷ Revenue — SPCX's TTM figure is −45.00% (a net loss), driving the Profitability sub-score to 0.0.
- **NOPAT**: Net Operating Profit After Tax — EBIT × (1 − effective tax rate).
- **PCAOB (Public Company Accounting Oversight Board)**: the US regulator overseeing audits of public companies; SpaceX's FY2023–FY2025 financials carry a PCAOB-standard audit opinion (PricewaterhouseCoopers LLP) despite the company not yet being publicly traded at the time of audit, since an S-1 registrant's financials must meet the same audit standard as an existing public filer. *(New term.)*
- **Quality Score**: this framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to reach Phase 02. SPCX scored 48.3 (or 41.2 under an alternative convention) and separately failed via a hard disqualifier.
- **Redeemable convertible preferred stock**: see Mezzanine equity above.
- **ROIC**: Return on Invested Capital — SPCX's TTM figure is negative (≈−12%), driving the Profitability sub-score to 0.0.
- **S-1 / S-1/A (Registration Statement)**: the SEC form a company files to register securities for a public offering; an "S-1/A" is an amendment. This is SpaceX's primary Rule-0-compliant fundamentals source this session, since no 10-K or 10-Q yet exists. *(New term.)*
- **SEC EDGAR**: the SEC's public filing database, used to source SpaceX's S-1/A directly.
- **TAM**: Total Addressable Market.
- **Total Addressable Market (TAM) expansion**: cited as Growth sub-score modifier evidence (Starlink subscriber growth, Starlink Mobile/Direct-to-Cell, pending EchoStar spectrum deal) — moot this session since the Growth_Score already saturates at its ceiling.
- **Treasury yield (10Y)**: this framework's risk-free-rate benchmark; not used in any calculation this session since Phase 02 is never reached, but recorded in the session header per the standard output format.
- **TTM (Trailing Twelve Months)**: the most recent 12 months of reported financial results — reconstructed for SPCX this session from FY2025 minus Q1 2025 plus Q1 2026, since no standalone Q2/Q3/Q4 2025 figures are disclosed (§2.3).
- **xAI Merger**: SpaceX's acquisition of X.AI Holdings Corp. (Elon Musk's AI company, itself the post-merger parent of X/Twitter following the March 2025 "X Merger"), effective 2 February 2026 — combined SpaceX's space/satellite business with xAI's Grok AI models, X's social/advertising platform, and AI compute infrastructure (the Colossus data centers) into the single consolidated public company evaluated in this session. *(New term.)*

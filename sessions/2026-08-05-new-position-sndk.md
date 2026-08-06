# NEW POSITION — SNDK (Sandisk Corporation, NASDAQ) — 2026-08-05

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6; re-evaluation of a prior FAIL — SNDK is not currently held)
**Date:** 2026-08-05
**10Y US Treasury Yield:** 4.63% (FRED `DGS10`, most recent posted observation dated 2026-08-04 — normal 1-day FRED reporting lag)
**Rate Regime Modifier:** +5 (10Y in the 3.5–5% bracket) — see §5.
**Current SNDK portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** [watchlist/not-in-portfolio/SNDK/SNDK-2026-07-15.md](../watchlist/not-in-portfolio/SNDK/SNDK-2026-07-15.md) — Quality Score 51.3, **Phase 01 FAIL** (hard disqualifier: FCF not positive for 3+ consecutive years, FY2023 −$932M / FY2024 −$475M / FY2025 −$120M). That entry's own "Next review trigger" named exactly the event that fired this session: *"SanDisk's FY2026 10-K (expected ~August 2026)... Also any Rule 9 event: guidance revision... a revision at the actual Q4 print would trigger review."*
**Sector:** Semiconductors / NAND Flash Memory & Data Storage — spun off from Western Digital (WDC) 21 February 2025.
**Filer type:** US domestic filer, CIK **0002023554**. Fiscal year ends the last Friday in June/early July (FY2026 ended **3 July 2026**).
**First-use jargon decode:** see closing Glossary (§10).

---

## 0. Why this session exists — trigger source

A post on `t.me/myroslavkorol` (post **2627**, ~21:39:55 UTC, 2026-08-05) claimed SanDisk reported Q4 FY2026 + full FY2026 results: a beat on Q4 estimates, "not superb" Q1 FY27 guidance, a new $15.5B buyback authorization, and a −6.5% post-market stock move. **Per Rule 0 and CLAUDE.md, no figure from this post is used as data anywhere below** — it is a trigger only. Every figure in this session is independently re-pulled from IBKR (price), SEC EDGAR (the 8-K/Exhibit 99.1 press release, accession `0001628280-26-053346`, filed 2026-08-05), and cross-checked against independent financial press.

**Independent verification of the post's claims (for context, not as data source):**
- Q4 FY2026 beat: **confirmed** — revenue $8,965M vs. ~$8.42B consensus (CNBC-compiled, per press coverage); non-GAAP diluted EPS $39.25 vs. ~$34.45 consensus.
- "Not superb" Q1 FY27 guidance: **directionally confirmed** — Q1 FY27 revenue guidance midpoint ($10.55B) came in ~2.5% *below* the ~$10.82B Street consensus, and the stock fell despite the Q4 beat; RBC's Srini Pajjuri reiterated Sector Perform, "warning the stock price may already be pricing in peak earnings." Goldman Sachs, by contrast, raised its price target to $2,200 (from $1,200) and kept a Buy rating — reaction was genuinely mixed, not uniformly negative.
- $15.5B buyback authorization: **confirmed, exact match** — SEC 8-K/Exhibit 99.1: "an additional $14 billion buyback program, bringing total remaining authorization to $15.5 billion."
- −6.5% post-market move: **broadly consistent but not identical** — this session's own live IBKR fetch (§1) shows −6.92% vs. the prior close at the time of fetch; small variance is expected given different snapshot timing (post-market vs. this session's fetch) and is not treated as a discrepancy worth resolving further, since the live IBKR figure — not the post's — is what's actually used.

SNDK's watchlist file has no `⚠️ STALE SCORE` banner and no row in [watchlist/STALE.md](../watchlist/STALE.md) (confirmed via grep before this session) — its prior entry was a Phase 01 FAIL with no Phase 02 score, and per [watchlist/README.md](../watchlist/README.md), stale-score marking only applies to entries carrying a numeric Phase 02 score. Nothing to clear on that front; this is a fresh Rule-9-triggered re-evaluation under the same (2026-06-29 Quality Score / 2026-06-29 Valuation Score) methodology version as the prior entry.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price (used)** | **$1,257.11** | IBKR `get_price_snapshot` (contract_id **760250490**, NASDAQ, "SANDISK CORP" — confirmed the correct standalone equity, not one of the leveraged/inverse single-stock-ETF products (SNXX, SNDU, SNDQ, SNDG, SNDC, SANS, SADP) that also match a `search_contracts` query for "SNDK"), `last.price`, ts epoch 1785975149 = **2026-08-05T21:32:29Z** |
| Change vs. prior close | **−$93.39 / −6.92%** | IBKR `change` field |
| Bid / Ask | $1,256.53 / $1,259.00 | IBKR `get_price_snapshot` |
| 52-week range | Low **$40.53** · High **$2,354.39** · Open (52w ago) $42.53 | IBKR `misc_statistics` — still an extraordinary ~58x low-to-high range |
| US 10Y Treasury yield | 4.63% | FRED `DGS10`, as of 2026-08-04 |

**$1,257.11 is used as the live price for this session** — fetched fresh via IBKR, not inferred from any multiple and not carried from the prior 2026-07-15 session's $1,509.13.

---

## 2. Data Gathered — Sources & Method

### 2.1 Q4 FY2026 / FY2026 results — primary source

**Source:** SEC EDGAR, [8-K filed 2026-08-05](https://www.sec.gov/Archives/edgar/data/2023554/000162828026053346/0001628280-26-053346-index.htm), Exhibit 99.1 press release (`sndkq4-26ex991xpressrelease.htm`), Items 2.02/8.01/9.01. **No FY2026 10-K has been filed yet** (expected in the following weeks, per the FY2025 filing cadence — 10-K filed roughly two weeks after the Q4 FY2025 earnings 8-K last year). The 8-K/Exhibit 99.1 GAAP statements are a Rule-0-compliant primary source in their own right (same convention as this framework's MELI 2026-08-05 and AAPL 2026-07-31 sessions, both of which scored off an 8-K exhibit ahead of the fuller 10-Q/10-K).

**GAAP Consolidated Statements of Operations ($ millions except per-share):**

| | Q4 FY2026 | Q4 FY2025 | **FY2026 (full year)** | FY2025 (full year) |
|---|---|---|---|---|
| Revenue, net | 8,965 | 1,901 | **20,248** | 7,355 |
| Cost of revenue | 1,383 | 1,403 | **5,776** | 5,143 |
| Gross profit | 7,582 | 498 | **14,472** | 2,212 |
| R&D | 348 | 285 | **1,328** | 1,132 |
| SG&A | 197 | 162 | **676** | 573 |
| Goodwill impairment | 0 | 0 | **0** | 1,830 |
| Operating income (loss) | 7,037 | 18 | **12,389** | (1,377) |
| Interest and other income, net | 812 | (36) | **628** | (102) |
| Income tax expense | 946 | 5 | **1,584** | 162 |
| **Net income (loss)** | **6,903** | (23) | **11,433** | (1,641) |
| Diluted EPS (GAAP) | $43.97 | $(0.16) | **$73.76** | $(11.32) |
| Diluted shares (wtd avg) | 157M | 145M | **155M** | 145M |

Non-GAAP (company-adjusted, not scored, shown for context only per "Why Forward Guidance Is Not a Sub-score" / non-GAAP scoring convention): Q4 non-GAAP diluted EPS $39.25; FY2026 non-GAAP diluted EPS $70.88; FY2026 non-GAAP net income $10,987M.

**GAAP Balance Sheet, as of 3 July 2026 ($ millions):**

| | Jul 3, 2026 |
|---|---|
| Cash and cash equivalents | **4,762** |
| Marketable equity securities (non-current) | 1,777 |
| Total assets | 22,507 |
| Current portion of long-term debt | **0** |
| Long-term debt | **0** |
| Total liabilities | 6,771 |
| Total shareholders' equity | 15,736 |
| Common stock issued and outstanding | **149M** |

SanDisk's $1.9B Term Loan Facility (already reported repaid 4 March 2026 in the prior session) — the FY2026 cash-flow financing activities confirm a further **$1,900M debt repayment** line this fiscal year, consistent with full repayment. SanDisk remains **debt-free**. **Note on "Marketable equity securities" ($1,777M):** a new balance-sheet line this fiscal year, not present in the 2026-07-15 session's data — appears to be an investment of a portion of the company's large post-supercycle cash pile into equity securities. Not netted into Net Debt below (this framework's convention nets only cash *and cash equivalents*, not longer-dated investment holdings with price risk); flagged for transparency, consistent with "show every calculation."

**GAAP Cash Flow Statement, FY2026 vs FY2025 ($ millions):**

| | FY2026 | FY2025 |
|---|---|---|
| Net cash provided by operating activities | **11,671** | 84 |
| Capital expenditures | **(177)** | (204) |
| **Free Cash Flow (OCF − CapEx)** | **11,494** | **(120)** |
| Depreciation & amortization | 149 | 163 |
| Repurchases of common stock (financing) | **(4,524)** | — |
| Stock issuance (financing) | 53 | — |
| Dividends paid | **none — SanDisk pays no dividend** | — |

### 2.2 Multi-year FCF history (for the hard-disqualifier check, §3.1)

Combining this session's fresh FY2026 figure with the 2026-07-15 session's primary-sourced (10-K) FY2023–FY2025 figures, re-confirmed unchanged (no restatement found in the FY2026 filing):

| Fiscal Year | Free Cash Flow | Source |
|---|---|---|
| FY2023 | **−$932M** | FY2025 10-K (filed 2025-08-21), carried forward, unchanged |
| FY2024 | **−$475M** | FY2025 10-K, carried forward, unchanged |
| FY2025 | **−$120M** | FY2025 10-K, carried forward, unchanged |
| **FY2026** | **+$11,494M** | **This session — fresh, 8-K/Exhibit 99.1, §2.1** |

### 2.3 Moat evidence — refreshed this session, carried forward where unchanged

| Signal | Result | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** (unchanged) | TrendForce's most recent vendor-level NAND share data found this session is still **Q1 2026** (SanDisk 13.9%, tied 4th with Micron, up from 12.4% in Q3 2025) — a fresh search this session (TrendForce's 21 Jul 2026 report on 2027 supply/demand) turned up no newer vendor-level share breakdown. Flagged: **no Q2/Q3 2026 TrendForce share update found**, carrying forward the last-available figure rather than inventing a newer one. |
| Brand premium | **FALSE** (unchanged) | Same reasoning as 2026-07-15: no third-party citation of a sustained retail price premium *without volume loss*; the ASP surge is industry-wide (all top-5 NAND suppliers grew in lockstep through the supercycle), not company-specific pricing power. |
| Network effect | **FALSE** (unchanged) | Hardware/component manufacturer — no two-sided marketplace dynamic. |
| Switching costs | **TRUE** (unchanged) | Same cited mechanism: SanDisk's own 10-K risk factors describe "lengthy product qualifications" as an industry dynamic creating real re-qualification switching costs for enterprise/cloud customers once qualified. |
| Scale cost advantage | **FALSE** (unchanged) | No cost-per-unit ($/GB) citation vs. Samsung/SK Hynix/Kioxia/Micron found this session either. |

```
Moat_Score = (2 of 5 TRUE) / 5 × 100 = 40.0   — unchanged from 2026-07-15
```

### 2.4 Qualitative context — cycle status, unchanged framing, updated data

The NAND pricing supercycle that drove the 2026-07-15 session's entire analysis is now reflected in a **complete fiscal year** of results, not just a partial-year TTM reconstruction — FY2026 revenue $20,248M (+175% YoY), gross margin 71.5% (vs. 30.1% FY2025, 16.1% FY2024, 7.1% FY2023). TrendForce's own July 2026 report ("NAND Flash Supply Growth to Outpace Demand in 2027, Easing Supply Constraints in 2H27") is the most direct evidence this framework has that the *current* cycle's durability is explicitly, independently flagged as time-limited — a risk this session weights heavily in the DCF/valuation work below (§6), consistent with this framework's own DRAM/NAND glossary characterization ("commoditized, boom-bust cyclical businesses with little durable pricing power") and Rule 6's "normalize before you value" discipline for cyclicals.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology, unchanged version)

### 3.1 Hard disqualifier check — the pivotal determination this session

**FCF-positivity disqualifier — two readings shown, per this session's explicit instruction to determine the correct rolling window, not assume the prior FAIL repeats:**

| Reading | Window tested | Result |
|---|---|---|
| **A — Permanent-scar** (the 2026-07-15 session's own stated expectation: *"cannot mechanically resolve before the FY2028 10-K"*) | Requires a *fresh* run of 3 consecutive **positive** years to clear a once-fired disqualifier | FY2026 alone doesn't satisfy this — **still fires** |
| **B — Rolling window** (this session's determination — see [decisions/2026-08-05-framework-clarification-fcf-disqualifier-rolling-window.md](../decisions/2026-08-05-framework-clarification-fcf-disqualifier-rolling-window.md) for full reasoning) | Test the **current** most-recently-completed 3 fiscal years fresh each session, same convention as every other rolling metric in this framework (TTM ratios, 3yr CAGR, Net Debt/EBITDA) and the same treatment the MELI 2026-08-05 session already applied to the *sibling* FCF/NI disqualifier | FY2024 (−$475M, negative), FY2025 (−$120M, negative), FY2026 (**+$11,494M, positive**) — **not all 3 negative → does not fire** |

**This session adopts Reading B (rolling window)**, for the reasons documented in full in the linked `decisions/` entry: it is the only reading internally consistent with how the framework's *other* hard disqualifier (FCF/NI conversion) and every other trailing metric in this framework are actually applied; Reading A's literal consequence — that any 3-year bad patch anywhere in a company's history permanently and irrecoverably disqualifies it, no matter how strong or complete a subsequent turnaround — has no support elsewhere in this framework and is a materially harsher rule than the disqualifier's own stated rationale ("sustained quality requires sustained cash generation") was written to assert.

**⚠️ This is a genuine interpretive judgment call, not a mechanical recomputation — flagged as the single highest-stakes determination in this session.** Its practical consequence is partially defused by the R/R gate finding in §7 below (no capital is actually deployed under *either* reading), but the Quality Score gate *outcome itself* — PASS vs. FAIL — depends entirely on it, so both readings' full downstream consequences are shown side by side in §3.2.

| Other hard disqualifiers | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years w/o growth-capex explanation | FY2025: not economically meaningful (both FCF and NI negative — dividing a negative by a negative isn't a genuine conversion signal, same issue flagged for FY2023–25 in the prior session). **FY2026 (meaningful, both positive): 11,494/11,433 = 100.53%** | disqualify if 2+ consecutive meaningful years <70% | **✅ PASS**, comfortably — only 1 economically meaningful year exists, and it's well above 70% |
| Net Debt/EBITDA over threshold (2.5× standard) | Net Debt = 0 − 4,762 = **−$4,762M** (net cash). TTM EBITDA = Op income 12,389 + D&A 149 = **12,538**. Net Debt/EBITDA = **−0.3799×** | disqualify if exceeds 2.5× | **✅ PASS**, comfortably — deeply net-cash |

### 3.2 Quality Score — full computation, both readings

**Shared inputs (identical under both readings):**

```
Profitability inputs:
  Net Margin (FY2026) = 11,433 / 20,248 = 56.4649%
  NetMargin_Component = clamp((56.4649/30)×100, 0, 100) = 100.0   (capped)

  EBIT (FY2026) = 12,389 ; Pretax income = 12,389 + 628 = 13,017
  Effective tax rate = 1,584 / 13,017 = 12.167%
  NOPAT = 12,389 × (1 − 0.12167) = 10,881.6
  Invested Capital = Total Debt + Equity − Cash = 0 + 15,736 − 4,762 = 10,974
  ROIC = 10,881.6 / 10,974 = 99.16%
  ROIC_Component = clamp((99.16/30)×100, 0, 100) = 100.0   (capped)

  Raw Profitability_Score = (100.0 + 100.0) / 2 = 100.0

MARGINS (15%):
  Gross Margin (FY2026) = 14,472 / 20,248 = 71.4737%
  GrossMargin_Score = clamp((71.4737/80)×100, 0, 100) = 89.3421
  3yr trend: FY2023 7.07% → FY2024 16.09% → FY2025 30.08% → FY2026 71.47% — genuinely
    expanding, but already far above the 40% bonus-eligibility ceiling, so no +10 bonus applies
  Margins_Score = 89.3421

GROWTH (20%):
  Revenue 3yr CAGR, FY2023 ($6,086M, 10-K-sourced, genuine standalone/comparative figure — NOT
    carve-out data, unlike the prior session's FY2022 baseline) → FY2026 ($20,248M)
  CAGR = (20,248/6,086)^(1/3) − 1 = 49.28%
  Growth_Score = clamp((49.28/25)×100, 0, 100) = 100.0   (capped)
  TAM/pricing-power modifier: NOT applied — same reasoning as 2026-07-15, this is an
    industry-wide commodity pricing cycle, not company-specific pricing power (moot anyway,
    already capped)
  Growth_Score = 100.0

BALANCE SHEET (15%):
  Net Debt/EBITDA = −0.3799× (net cash, §3.1)
  BalanceSheet_Score = clamp(100×(1 − (−0.3799)/4), 0, 100) = clamp(109.5, 0, 100) = 100.0

MOAT SIGNAL (15%): 2 of 5 TRUE (§2.3) = 40.0

FCF QUALITY (10%):
  FY2026 FCF/NI = 11,494 / 11,433 = 100.5337%
  FCFQuality_Score = clamp(((1.005337 − 0.40)/0.60)×100, 0, 100) = clamp(100.89, 0, 100) = 100.0
```

**Reading B (rolling window — adopted, §3.1) — disqualifier does NOT fire, no Profitability cap:**

```
Profitability_Score = 100.0   (no cap)

Quality Score = 100.0×0.25 + 89.3421×0.15 + 100.0×0.20 + 100.0×0.15 + 40.0×0.15 + 100.0×0.10
             = 25.00 + 13.4013 + 20.00 + 15.00 + 6.00 + 10.00
             = 89.4013 → rounds to 89.4
```

**Reading A (permanent-scar — rejected, shown for transparency) — disqualifier fires, Profitability capped at 40.0** (quality-scoring.md: *"If the company isn't FCF-positive for 3+ consecutive years, cap Profitability_Score at 40.0"*):

```
Profitability_Score = 40.0   (capped)

Quality Score = 40.0×0.25 + 89.3421×0.15 + 100.0×0.20 + 100.0×0.15 + 40.0×0.15 + 100.0×0.10
             = 10.00 + 13.4013 + 20.00 + 15.00 + 6.00 + 10.00
             = 74.4013 → rounds to 74.4
```

**Gate result:**

| Reading | Quality Score | vs. 80.0 gate | Hard disqualifier |
|---|---|---|---|
| **B — Rolling window (adopted)** | **89.4** | **PASS** | Does not fire |
| A — Permanent-scar (rejected) | 74.4 | FAIL | Fires independently |

**This session proceeds under Reading B: Quality Score = 89.4, PASSES the 80.0+ gate.** Phase 02 valuation scoring below is therefore performed — the first time SNDK has cleared this framework's Phase 01 gate. See §3.1 and the linked `decisions/` entry for the full reasoning behind adopting Reading B, and the explicit acknowledgment that this is a judgment call, not an unambiguous mechanical result.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test:**

Forward PE input: no reliable full-year FY2027 consensus was directly extractable (paywalled beyond headline figures), so this session uses `stockanalysis.com`'s cited **FY2027 consensus EPS $212.95** (non-GAAP, dated 2026-08-05 — i.e. freshly updated post-earnings, not stale pre-print data) against this session's own live price, rather than mixing a third-party's own stale price snapshot into the ratio:

```
Forward PE = $1,257.11 / $212.95 = 5.903×
EY = 1 / 5.903 = 16.9406%
Spread = EY − 10Y = 16.9406% − 4.63% = +12.3106%
```

**Pass threshold: Spread ≥ +1.5%. Result: PASS, comfortably** (+12.31pp cushion) → no Step 1 additive.

⚠️ **Data-quality flag:** a $212.95 consensus EPS implies FY2027 earnings roughly triple FY2026's — an aggressive Street assumption this session does **not** take at face value for valuation purposes (see the DCF/multiples work in §6, which explicitly builds more conservative Base/Bear paths). It is used here only for the Rate Environment Gate's EY test, consistent with this input being a market-observable consensus figure, not a scored fundamental.

**Step 2 — Rate Regime Modifier:** 10Y yield 4.63% falls in the **3.5–5% bracket → +5**.

**Total Rate Modifier for SNDK = +5.**

---

## 5. Phase 02 — Valuation Score

### 5.1 PEG eligibility

SanDisk's EPS history: FY2023/24/25 all GAAP losses, FY2026 a single (extraordinary) profitable year. This does **not** meet the "EPS growth >15% for 3+ years on a clean, non-distorted earnings base" Fast-Grower test — same carve-out language valuation-scoring.md already specifies for a company "only recently turned GAAP-profitable." **PEG not applicable; its 15% weight redistributed to EV/EBIT** (EV/EBIT effectively 40%).

### 5.2 Market cap / EV inputs

```
Shares outstanding (2026-07-03 balance sheet, primary-sourced) = 149M
Market Cap = $1,257.11 × 149M = $187,309.39M
EV = Market Cap + Total Debt − Cash = 187,309.39 + 0 − 4,762 = $182,547.39M
```

### 5.3 Sub-scores

```
FCF Yield (40% weight):
  FCF Yield = FY2026 FCF / Market Cap = 11,494 / 187,309.39 = 6.1364%
  FCF_Score = clamp(100×(1 − 6.1364/10), 0, 100) = clamp(38.636, 0, 100) = 38.64

EV/EBIT (40% weight, redistributed from PEG):
  EV/EBIT = 182,547.39 / 12,389 = 14.734×
  EV/EBIT_Score = clamp((14.734−12)/23×100, 0, 100) = clamp(11.887, 0, 100) = 11.89

Forward PE (20% weight):
  No-history fallback — SNDK has traded standalone only since 21 Feb 2025 (~17 months),
  well short of the 5yr/20-quarter minimum this framework requires before reconstructing a
  historical PE range/average (valuation-scoring.md's own explicit caveat). Same fallback
  used in the 2026-07-15 session (which never reached Phase 02, but the data gap is unchanged).
  FwdPE_Score = 50.0   (neutral, flagged)

PEG (15% weight): N/A — redistributed to EV/EBIT (§5.1)
```

### 5.4 Fair Value — Method A (DCF) and Method B (Multiples)

Given SNDK's extreme, well-documented cyclicality (FY2023–2025 losses immediately followed by a record FY2026), Rule 6 ("normalize before you value") and Rule 7 (mandatory bull/base/bear scenario weighting) apply with unusual force here. **Both scenarios and all assumptions are shown explicitly — this is inherently the most judgment-heavy section of this session, flagged as such throughout.**

**DCF (Method A) — WACC and terminal assumptions:**

```
Risk-free rate = 4.63% (10Y Treasury, §0 header)
Beta: no reliable measured beta exists over SNDK's own ~17-month trading history (same kind
  of data-insufficiency this framework already treats specially for 5yr PE reconstruction) —
  this session uses an ESTIMATED beta of 2.0, a judgment input (standard practice for a WACC
  calculation, distinct from inventing a historical/reported fact) reflecting a small,
  extremely volatile cyclical semiconductor name (52-week range ~58×, single-day moves of
  ±7–14% observed twice in this framework's own two SNDK sessions alone).
Equity Risk Premium ≈ 5% (standard working assumption)
Base-case WACC = 4.63% + 2.0×5% = 14.63%, rounded to 15% for conservatism
Terminal growth = 2.5% (GDP cap, Rule 2)
```

| | **Bull** | **Base** | **Bear** |
|---|---|---|---|
| Assumption basis | "NAND undersupply extends beyond 2026" (TrendForce, cited §2.4 prior session); cycle persists near-peak through FY2028 | Q1 FY27 guidance run-rate roughly holds for FY2027, then fades as 2027 industry capacity additions (TrendForce, §2.4) pressure pricing | Cycle turns down faster than guided — consistent with the market's own post-print reaction (§0) and TrendForce's own flagged 2027 oversupply risk; reverts toward FY2024/25-like economics within 2 years |
| Year 1 (FY2027) FCF | $38,000M | $22,000M | $12,000M |
| Fade path (Yrs 2–5) | −5%/yr | −20%/yr | Sharp: $6,000M→$1,500M→$0M→−$200M |
| Yrs 6–10 | Fade −15%/yr toward $13,733M | Fade toward $3,200M | Slow recovery to $1,800M |
| WACC | 11% | 15% | 16% |
| Terminal value (undiscounted) | $165,600M | $26,240M | $13,114M |
| **PV of explicit FCFs + TV** | **$231,000M** | **$68,242M** | **$20,218M** |
| + Net cash ($4,762M) | | | |
| **DCF Equity Value** | **$235,762M** | **$73,004M** | **$24,980M** |
| ÷ 149M shares | **$1,582** | **$490** | **$168** |

```
DCF PW Fair Value = 0.25×1,582 + 0.50×490 + 0.25×168 = 395.5 + 245.0 + 42.0 = $682.5
```

**Multiples (Method B) — cyclical-appropriate multiple applied to each scenario's Year-1 (or blended near-term) FCF-per-share**, reflecting the standard cyclical-investing convention of using a *below-market* multiple on peak/near-peak earnings (the market correctly assigns high multiples at cyclical *troughs* and low multiples at cyclical *peaks* — the "reverse ROE effect"):

```
Bull:  ($38,000M / 149M) × 12× = $255.03 × 12 = $3,060.4
Base:  ($22,000M / 149M) × 10× = $147.65 × 10 = $1,476.5
Bear:  (avg of Yr1–3 FCF: ($12,000+6,000+1,500)/3 = $6,500M / 149M) × 6× = $43.62 × 6 = $261.7

Multiples PW Fair Value = 0.25×3,060.4 + 0.50×1,476.5 + 0.25×261.7 = 765.1 + 738.25 + 65.4 = $1,568.75
```

**Blended (Football Field) Fair Value — Rule 3, 40% DCF / 60% Multiples, applied per scenario then probability-weighted (mathematically equivalent to blending the two PW figures directly):**

```
Bull Blended  = 0.40×1,582 + 0.60×3,060.4 = 632.8 + 1,836.24 = $2,469.0
Base Blended  = 0.40×490 + 0.60×1,476.5 = 196.0 + 885.9 = $1,081.9
Bear Blended  = 0.40×168 + 0.60×261.7 = 67.2 + 157.0 = $224.2

PW Fair Value = 0.25×2,469.0 + 0.50×1,081.9 + 0.25×224.2 = 617.25 + 540.95 + 56.05 = $1,214.25
```

**Blended Fair Value = $1,214.25.** Cross-check: this sits well inside the analyst range (low PT $1,000, average $2,218, median $2,250, high $3,169 — 23 analysts, "Buy" consensus rating) but materially below the average/median PT — consistent with this framework's Rule 7 guardrail to use scenario-weighted PW Fair Value, "never the rosy point" (a single optimistic analyst-consensus target).

### 5.5 Upside/Downside Modifier

```
Gap Upside % = (PW FV / Live Price) − 1 = (1,214.25 / 1,257.11) − 1 = −3.410%
Catalyst window: no narrower catalyst identified beyond the ongoing cyclical dynamics already
  built into the DCF/multiples fade paths themselves — use default 2yr per rule.
Annualized gap = −3.410% / 2 = −1.705%/yr

Intrinsic growth rate: a THROUGH-CYCLE structural estimate of +5%/yr, reflecting durable
  AI-datacenter-driven NAND demand growth (TrendForce's own "undersupply extends beyond 2026"
  framing) net of the commodity cyclicality already captured in the gap term above — an
  explicit judgment estimate, flagged as such, NOT a company-guided or historical figure
  (near-term growth per this session's own DCF fade paths is actually negative — this 5% is
  a longer-horizon structural estimate, not a near-term read, and is not double-counted with
  the gap calc, which already prices in cyclical normalization).

Shareholder yield: no dividend (§2.1). Net buyback yield = (FY2026 buybacks $4,524M − stock
  issuance $53M) / Market Cap $187,309.39M = 4,471 / 187,309.39 = 2.387%

E = −1.705% + 5.00% + 2.387% = 5.682%
```

`E` (5.682%) sits between 0 and hurdle H=10% → thin/moderate-attractive-but-below-hurdle band:

```
M = +5 × (H − E)/H = +5 × (10 − 5.682)/10 = +5 × 0.4318 = +2.159 → +2.16
```

Guardrail check: this modifier is positive (mild score-raising direction, not a discount), so the "no catalyst within 18–24mo caps the *upside* (negative) side at −5" guardrail does not bind here — no issue.

**Upside/Downside Modifier = +2.16.**

### 5.6 Final Valuation Score

```
Raw weighted = FCF_Score×0.40 + EV/EBIT_Score×0.40 + FwdPE_Score×0.20
             = 38.64×0.40 + 11.89×0.40 + 50.0×0.20
             = 15.456 + 4.756 + 10.00
             = 30.212

Final Score = 30.212 + Rate Modifier(+5) + Upside/Downside Modifier(+2.16)
            = 37.372 → rounds to 37.4
```

**Valuation Score = 37.4** → per the Action Table alone, Score 30.0–49.9 → BUY — Standard position 3–5%.

---

## 6. Composite Score

```
Composite Score = 0.50×(100 − Quality Score) + 0.50×Valuation Score
                = 0.50×(100 − 89.4) + 0.50×37.4
                = 0.50×10.6 + 0.50×37.4
                = 5.30 + 18.70
                = 24.0
```

**Composite Score = 24.0** → per the Phase 03 action table applied to the Composite Score (valuation-scoring.md's "Composite Score" section — the correct table to use once a Quality Score exists): **Score 0.0–29.9 → BUY — Full position 6–8%.** SNDK's high Quality Score (89.4) pulls the blended number into the *deeper* buy band than the raw Valuation Score (37.4, "Standard position 3–5%") alone would indicate — the same mechanical effect this framework's META 2026-07-01 session documented in the opposite direction (a high Quality Score pulling a *richer*-looking raw score back into a favorable band).

**⚠️ This Composite Score inherits the Reading-B judgment call from §3.1 in full.** Under Reading A (Quality Score 74.4, FAIL), no Composite Score or Phase 02 work would be computed at all — the session would stop exactly where the 2026-07-15 session stopped.

---

## 7. Fair Value + Order Setup — computed per the operating brief (required for any BUY-band action), but see the R/R gate finding below

```
[x] Composite Score (drives action band):        24.0   (≤29.9 → Full-position entry indicated)
[x] Raw Valuation Score (incl. Upside/Downside):  37.4
[x] Expected annual return E / catalyst window:   +5.682% / 2yr
[x] Upside/Downside Modifier applied:             +2.16
[x] Blended Fair Value (PW, Rule 7):              $1,214.25
[x] Margin of Safety %:                           20%   (top of the 15–20% "high quality, predictable
                                                          FCF" band — SNDK's Quality Score is genuinely
                                                          high, but its FCF history is anything but
                                                          "predictable"; the top of the range is used
                                                          deliberately for extra conservatism)
[x] BUY PRICE (limit):      $1,214.25 × (1 − 0.20)                  = $971.40
[x] PRIMARY SELL TARGET:    = Blended FV                            = $1,214.25
[x] BULL-CASE TRIM TARGET:  $2,469.0 × 0.90                         = $2,222.10
[x] STOP LOSS:               $971.40 × (1 − 0.25)                   = $728.55   (top of the 20–25%
                                                                         band — this name's own
                                                                         trading history shows single
                                                                         -day moves of ±7–14%, a tight
                                                                         stop would likely be whipsawed)
[✗] Risk/Reward Ratio (base-case, Primary Sell Target):
      ($1,214.25 − $971.40) / ($971.40 − $728.55) = $242.85 / $242.85 = 1.00:1   — FAILS the 2:1 minimum
[x] Risk/Reward Ratio (bull-case, Trim Target):
      ($2,222.10 − $971.40) / $242.85 = $1,250.70 / $242.85 = 5.15:1   — clears comfortably
[x] Max $ Risk (1.5% of portfolio $60,829.03, per portfolio/holdings.md combined total):  $912.44
[x] Shares at that risk budget: $912.44 / $242.85 = 3.76 → 3 shares
[x] Position Size ($) at that share count:        3 × $971.40 = $2,914.20  (≈4.79% of portfolio —
                                                                below the 6–8% cap this score band
                                                                would otherwise allow; risk-based
                                                                sizing, not the cap, is binding)
```

**The base-case Risk/Reward Ratio (using the Primary/baseline Fair Value as the sell target — this framework's default reward reference, same convention used in every prior session that has hit this gate, e.g. AVGO 2026-07-04, DUOL 2026-07-04, META 2026-07-01) is exactly 1.00:1 — below the mandatory 2:1 minimum.** Per fair-value-methodology.md: *"If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely."* Only the bull-case trim target (5.15:1) clears the bar — the same recurring shape this framework has already documented for META across multiple sessions (base-case R/R pinned near 1.00:1, only the bull-case target clearing 2:1), not a one-off quirk of this specific calculation.

**Per operating-brief.md's BUY/SELL ORDER SETUP rule ("Minimum 2:1. Below 2:1 = do not enter."), this is a hard gate — independent of the Composite Score's favorable band. No entry is placed this session, regardless of which FCF-disqualifier reading (§3.1) is adopted.**

---

## 8. Recommendation

# **WATCHLIST ONLY — do not enter. Composite Score (24.0) supports a Buy-Full-position signal, but the base-case Risk/Reward Ratio (1.00:1) independently fails the 2:1 minimum gate. No position opened.**

This is a materially different outcome from the 2026-07-15 session's clean Phase 01 FAIL, but it is **not** a green light to buy today. Two independent gates govern SNDK this session, and they point in different directions:

1. **The Quality Score gate now PASSES (89.4, under this session's adopted Reading B — §3.1)** — a genuine reversal from the 2026-07-15 FAIL (51.3), driven almost entirely by a real, complete, primary-sourced fiscal year of extraordinary results (FY2026 net income $11.4B, FCF $11.5B, against FY2023–2025's cumulative ~$4.5B of losses and ~$1.5B of cash burn). This reversal rests on a genuine interpretive judgment call about how the "FCF-positive 3+ consecutive years" hard disqualifier should be re-evaluated once a new fiscal year prints after a disqualifying streak — documented in full in §3.1 and [decisions/2026-08-05-framework-clarification-fcf-disqualifier-rolling-window.md](../decisions/2026-08-05-framework-clarification-fcf-disqualifier-rolling-window.md). The alternative reading keeps the gate at FAIL (74.4).
2. **The Risk/Reward gate FAILS (1.00:1 vs. the 2:1 minimum) regardless of which disqualifier reading is used**, because it only comes into play once Phase 02/order-setup work is triggered — and it fails on its own terms, off this session's own Blended Fair Value ($1,214.25) sitting only modestly below the live price ($1,257.11, a −3.4% gap) once a genuinely conservative, cycle-normalized valuation is applied (§5.4/§5.5). The Composite Score being "cheap" (favorable Quality Score blended with a middling Valuation Score) does not by itself guarantee an executable trade — this is the same pattern already established for AVGO, DUOL, and META in this repo: a favorable score band is necessary but not sufficient; the R/R gate is independent and binding.

**Net effect: no capital is deployed under either interpretation of §3.1** — the R/R gate is the actual controlling constraint this session, which meaningfully de-risks the consequence of the Reading-B judgment call (it does not, by itself, put money at risk today).

**What would change this:** a pullback toward the $971.40 buy-price limit (a further ~22.7% decline from today's live price) would clear the MoS entry condition, but would still need the R/R math re-checked against the fair value estimate current at that time (both move together as new data arrives) — a limit order at $971.40 is **not** placed this session, since the R/R gate would still need to independently clear at that price, which is not guaranteed without a fresh reassessment closer to that level.

---

## 9. Next Review Trigger

- **SanDisk's FY2026 10-K** (expected in the coming weeks, per the FY2025 filing cadence) — will provide the audited version of this session's 8-K-sourced figures and any restatement risk; also the natural point to look for updated TrendForce/IDC vendor-share data if the 10-K's own MD&A cites any.
- **Q1 FY2027 earnings** (next quarterly print) — the first real test of whether the guided $10.3–10.8B revenue / 83–85% gross margin / $44–46 non-GAAP EPS range holds, beats, or misses — directly informs whether the Base-case DCF/multiples path in §5.4 or the more bearish Bear-case path is tracking closer to reality.
- **Standard Rule 9 triggers:** any further guidance revision, management change, material M&A, macro shift, or a >15% unexplained price move.
- **A price pullback toward the $971.40 buy-price limit** — per §8, would warrant a fresh R/R recheck, not an automatic entry.
- **TrendForce/IDC vendor-share update** (Q2/Q3 2026 NAND market share) — would refresh the Moat Signal's "market share" evidence, currently carried forward unchanged from Q1 2026 data (§2.3).

---

## 10. Watchlist & Stale-Score Housekeeping

- **New watchlist entry:** [watchlist/not-in-portfolio/SNDK/SNDK-2026-08-05.md](../watchlist/not-in-portfolio/SNDK/SNDK-2026-08-05.md) — renamed from `SNDK-2026-07-15.md` per [watchlist/README.md](../watchlist/README.md)'s rule that a Rule 9 earnings-triggered re-evaluation with a changed score/status (Phase 01 FAIL → PASS, first-ever Phase 02/Composite Score computed) warrants a fresh dated pointer.
- **Stale-score mechanism:** not applicable — SNDK had no numeric Phase 02 score to go stale (2026-07-15 was a Phase 01 FAIL only), and this session's methodology version (2026-06-29) is unchanged from the prior entry, so nothing to clear in [STALE.md](../watchlist/STALE.md).
- **Framework file changed:** [framework/quality-scoring.md](../framework/quality-scoring.md) — added the rolling-window clarification note under Hard Disqualifiers (§3.1 above); full rationale in [decisions/2026-08-05-framework-clarification-fcf-disqualifier-rolling-window.md](../decisions/2026-08-05-framework-clarification-fcf-disqualifier-rolling-window.md).

---

## 11. Glossary

*(Pulled from [glossary.md](../framework/glossary.md); one new term added this session — Marketable equity securities)*

| Term | Meaning |
|---|---|
| **8-K** | A US-listed company's SEC filing disclosing a material event — the vehicle for SanDisk's Q4/FY2026 earnings release, used as this session's primary financial-data source ahead of the fuller 10-K. |
| **Beta** | A stock's sensitivity to overall market moves — used with the risk-free rate to estimate the cost of equity in a DCF's WACC; this session used an *estimated* beta (2.0) given SNDK's own trading history is too short (~17 months) for a reliable measured beta. |
| **Carve-out financial statements** | Historical financials prepared for a business unit that didn't previously report standalone — relevant to the *prior* SNDK session's FY2022 baseline; this session's Growth sub-score instead uses two genuine, standalone/10-K-sourced years (FY2023, FY2026), avoiding that caveat. |
| **CIK (Central Index Key)** | The SEC's unique numeric filer identifier — SanDisk's standalone entity is CIK 0002023554. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking (`0.50 × (100 − Quality Score) + 0.50 × Valuation Score`) — computed for the first time for SNDK this session (24.0), only reachable after clearing the Quality Score gate. |
| **D&A** | Depreciation & Amortization. |
| **DCF** | Discounted Cash Flow — a valuation method projecting future cash flows and discounting them to present value; Method A of this session's fair-value work (§5.4). |
| **Diluted EPS / diluted shares** | Earnings per share (and the share count) after including the dilutive effect of options, RSUs, and similar instruments. |
| **DRAM/NAND** | The two main families of memory chip; both commoditized, boom-bust cyclical businesses with little durable pricing power — the central framing behind this session's conservative DCF/multiples treatment (§5.4). |
| **EBIT/EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, D&A. |
| **Effective tax rate** | The actual percentage of pretax income paid as tax — SNDK's FY2026 figure is 12.17%. |
| **Equity Risk Premium (ERP)** | The extra return equity investors demand over the risk-free rate — a WACC input, estimated (not observed) in this session at ~5%. |
| **EV/EBIT** | Enterprise Value ÷ operating profit — a valuation multiple; this session's redistributed (40%-weight) sub-score. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE — used in the Rate Environment Gate's Step 1 test. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income — central to both the hard-disqualifier check (§3.1) and the FCF Yield sub-score (§5.3) this session. |
| **GAAP** | Generally Accepted Accounting Principles — the standard scored across this framework, in preference to any company's own Non-GAAP presentation. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted score — the crux of this entire session (§3.1). |
| **Invested Capital** | Debt + equity − cash — the ROIC denominator; $10,974M for SNDK this session. |
| **Marketable equity securities** | A balance-sheet line for a company's holdings of another entity's publicly-traded equity, held as an investment rather than for operating use — distinct from cash and cash equivalents, and not netted into this framework's Net Debt calculation. New on SanDisk's balance sheet this fiscal year ($1,777M), reflecting a post-supercycle cash-deployment choice — flagged, not netted, in this session's Balance Sheet sub-score. *(New term.)* |
| **MoS (Margin of Safety)** | How far below fair value the buy price is set — this session used the top of the 15–20% band (20%) for extra conservatism. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the ROIC numerator. |
| **Non-GAAP** | A company's own adjusted presentation, not independently audited to the GAAP standard — shown for context only, never scored, per this framework's convention. |
| **PW (Probability-Weighted) Fair Value** | This framework's blended fair value — 25% bull + 50% base + 25% bear — $1,214.25 for SNDK this session. |
| **Quality Score** | This framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to reach Phase 02. SNDK scored 89.4 (adopted reading) or 74.4 (alternative reading) — see §3.1. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss on a trade — minimum 2:1 to enter; SNDK's base-case R/R (1.00:1) is the gate that blocks entry this session despite a favorable Composite Score. |
| **ROIC** | Return on Invested Capital — 99.16% for SNDK this session (an extreme, cycle-peak reading, not a "normal-year" figure). |
| **Spin-off** | A corporate transaction separating part of a business into a new, independently-traded company — SanDisk's 21 Feb 2025 spin-off from Western Digital. |
| **TrendForce** | An independent semiconductor/memory-industry market-research firm — this session's (carried-forward, no newer data found) source for SanDisk's NAND market-share evidence. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results — this session largely uses the cleaner **FY2026 full fiscal year** instead, since it is now complete and primary-sourced. |
| **WACC** | Weighted Average Cost of Capital — the DCF discount rate; this session used 15% (Base), 11% (Bull), 16% (Bear), reflecting genuine cyclical-risk differentiation across scenarios. |

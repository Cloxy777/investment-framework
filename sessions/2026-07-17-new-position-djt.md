# NEW POSITION — DJT (Trump Media & Technology Group Corp, NASDAQ) — 2026-07-17

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, first-ever evaluation)
**Date:** 17 Jul 2026 (Friday)
**10Y US Treasury Yield:** 4.55% (FRED `DGS10`, most recent posted observation dated 2026-07-15 — normal 1-day FRED reporting lag; recorded for completeness only, since this session stops at the Quality Gate (§3) before the Rate Environment Gate would apply)
**Current DJT portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md); grep for "DJT" returns no match)
**Prior coverage:** None — first-ever `/new-position` or `/rescore` pass on this ticker (no existing file in `watchlist/in-portfolio/DJT/` or `watchlist/not-in-portfolio/DJT/`, confirmed via `find`)
**Sector:** Communication Services — Internet Content & Information / social media, streaming, and (since 2025) a bitcoin/digital-asset treasury
**Filer type:** US domestic filer — CIK **1849635** ("Trump Media & Technology Group Corp.," Nasdaq: DJT), Form 10-K/10-Q, went public via de-SPAC merger (Digital World Acquisition Corp. → TMTG, completed March 2024)
**First-use jargon decode:** see closing Glossary (§8).

---

## 0. Why this session exists — trigger source

A Telegram post on **tarasguk** (post tarasguk/11414, 2026-07-17, ~06:47 UTC) reported that Trump Media is launching a paid service giving subscribers — reportedly including Wall Street firms and institutions — faster access to Truth Social posts (including Donald Trump's own) ahead of the general public, framed as a potential trading edge. Per the operating brief and this repo's standing convention, **Telegram post text is never used as financial data** — it is a trigger only, and its substantive claim is not verified or relied upon anywhere in this session. DJT has no existing watchlist entry in this repo and is not a current holding (confirmed via `find` above), so per this repo's established precedent for first-ever ticker mentions, this warrants a full first-time evaluation regardless of the mention's substance. (For the record: the FY2025 10-K reviewed below, filed 2026-02-27, does disclose a "Patriot Package" premium-subscription beta launched July 2025 — see §2.5 — but contains no mention of an institutional/Wall-Street-targeted early-access product; if the Telegram post describes a genuinely new, more recent announcement, it postdates this filing and is not itself scored here, consistent with Rule 0/9.)

---

## 1. Live Price (Rule 0)

Contract confirmed via `search_contracts("DJT")`: contract_id **517641765**, exchange **NASDAQ**, description "TRUMP MEDIA & TECHNOLOGY GRO" — the correct unambiguous match (other `DJT`-symbol results returned were the unrelated Dow Jones Transportation Average index (CME) and various unrelated Dow Jones Titans sub-indices, a delisted "Trump Hotels & Casino Resorts" legacy contract, a leveraged ETF, and Kalshi prediction-market contracts — none of which are the common stock).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$9.39** | IBKR `get_price_snapshot`, `last` field, timestamp 1784269444 (2026-07-17T06:24:04Z), contract_id **517641765** (NASDAQ), `is_close: false` (live, pre-market) |
| Day change | **−$0.24 (−2.49%)** | IBKR `get_price_snapshot` `change` field |
| Prior close | $9.63 | IBKR `get_price_snapshot` `prior-close` field |
| Bid/Ask | $9.40 / $9.43 (size 66 / 1) | IBKR `get_price_snapshot` `bid_ask` field |
| 52-week high | $20.92 | IBKR `misc_statistics` `high_52w` |
| 52-week low | $6.96 | IBKR `misc_statistics` `low_52w` (identical to `low_13w`/`low_26w` — the 52-week low was itself set within the last 13 weeks) |
| Open 52 weeks ago | $18.97 | IBKR `misc_statistics` `open_52w` |
| US 10Y Treasury yield | 4.55% | FRED `DGS10`, as-of 2026-07-15 (not used this session — see header) |

$9.39 sits well below the midpoint of the 52-week range ($6.96–$20.92) and close to the 52-week low, which was set very recently (within the last 13 weeks). This price is used for reference throughout this session; no order-setup arithmetic is performed, since the Quality Gate fails decisively below (§3).

Shares outstanding (most recent SEC cover-page date, 2026-05-06 10-Q): **276,953,828** → implied market cap ≈ **$2.60B** at the live price above (context only, not used in any scoring formula).

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note

All financial figures below are sourced directly from Trump Media & Technology Group's own SEC EDGAR XBRL data (`data.sec.gov/api/xbrl/companyfacts/CIK0001849635.json`), cross-referenced against the underlying **FY2025 10-K** (filed 2026-02-27, accession 0001140361-26-007174, fiscal year ended 2025-12-31) and the **Q1 2026 10-Q** (period ended 2026-03-31, filed 2026-05-06). No `yfinance` fallback was needed — SEC XBRL tags provided every input this session required, at the primary-source level, with no vendor-reconciliation step. Quarterly figures not separately disclosed (Q2 2025, Q4 2025) are derived by subtraction from cumulative 6-/9-month and full-year figures, shown explicitly below — the same method used in this framework's prior TTM reconstructions (e.g. the 2026-07-16 MTCH session).

### 2.2 TTM reconstruction (Q2 2025 + Q3 2025 + Q4 2025 + Q1 2026)

Most recent completed quarter is Q1 2026 (ended March 31, 2026); Q2 2026 earnings are not yet released. Q4 2025 has no standalone SEC filing (10-Qs report cumulative periods) and is derived below by subtraction.

**Revenue, Cost of Revenue, Gross Profit (all $, primary-sourced):**

| Item | Q2 2025 | Q3 2025 | Q4 2025 (derived) | Q1 2026 | TTM |
|---|---|---|---|---|---|
| Revenue | 883,300 | 972,900 | 1,005,200 | 871,200 | **3,732,600** |
| Cost of revenue | 342,900 | 446,800 | 548,800 | 1,501,000 | **2,839,500** |
| Gross profit | 540,400 | 526,100 | 456,400 | (629,800) | **893,100** |

```
Q4 2025 Revenue        = FY2025 (3,682,600) − 9mo Jan–Sep 2025 (2,677,400)          = 1,005,200
Q4 2025 Cost of revenue = FY2025 (1,675,200) − 9mo Jan–Sep 2025 (1,126,400)          = 548,800

TTM Gross Margin = 893,100 / 3,732,600 = 23.93%
```

**Q1 2026 alone shows COGS ($1,501,000) exceeding revenue ($871,200) — a negative single-quarter gross margin (−72.3%)**, a sharp deterioration from FY2025's already-declining annual gross margin. Annual gross margin trend, all from primary filings:

| Fiscal Year | Revenue | COGS | Gross Margin |
|---|---|---|---|
| FY2022 | 1,470,500 | 54,500 | 96.29% |
| FY2023 | 4,131,100 | 164,900 | 96.01% |
| FY2024 | 3,618,800 | 619,000 | 82.89% |
| FY2025 | 3,682,600 | 1,675,200 | 54.51% |

Gross margin has **contracted sharply and consistently** every year since FY2023, and TTM (23.93%) is materially below even the already-compressed FY2025 annual figure — the opposite of the "structural expansion" pattern the Margins sub-score's trend bonus looks for.

**Revenue trajectory (annual, primary-sourced) — flags the 3yr-CAGR base-effect issue used in §3.2:**

| FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| $1.4705M | $4.1311M (+181%) | $3.6188M (**−12.4%**) | $3.6826M (+1.76%) |

Revenue roughly tripled FY2022→FY2023, then **declined** FY2023→FY2024, then was essentially flat FY2024→FY2025. Q1 2026 revenue ($871,200) was only +6.1% over Q1 2025 ($821,200) — still barely above the FY2024/FY2025 flat-to-declining trend, not a re-acceleration.

**Operating Income (Loss) — TTM, primary-sourced:**

| Q2 2025 | Q3 2025 | Q4 2025 (derived) | Q1 2026 | TTM |
|---|---|---|---|---|
| (43,508,000) | (57,658,400) | (432,342,300) | (293,487,900) | **(826,996,600)** |

```
Q4 2025 Op. loss = FY2025 (−573,043,700) − 9mo Jan–Sep 2025 (−140,701,400) = −432,342,300
```

**What is driving the FY2025/Q1 2026 operating loss is disclosed in the company's own XBRL tag `CryptoAssetRealizedAndUnrealizedGainLossOperating`** — a realized/unrealized loss on TMTG's own bitcoin/digital-asset holdings, run through *operating* income:

| | FY2025 | Q1 2026 |
|---|---|---|
| Digital-asset realized/unrealized gain (loss), operating | **($403,222,600)** | **($243,961,400)** |

This single line item is **~70% of the FY2025 operating loss and ~83% of the Q1 2026 operating loss** — i.e. the majority of the company's reported operating losses in the two most recent periods come from marking a bitcoin/crypto treasury to market, not from the core Truth Social/Truth+ media business. See §2.5 and the Digital-asset treasury strategy glossary entry (§8) for the underlying capital raise. This framework scores off the filed GAAP figures as reported (per "never invent or estimate," and consistent with how this framework treats other companies' self-labeled non-GAAP adjustments — see Adjusted EBITDA/Core/AOI precedents in the Glossary) — the crypto-loss detail is shown here as required qualitative context (Rule 6, "normalize before you value"), not as a basis for excluding the loss from the scored figures.

**D&A — same derivation method (`DepreciationDepletionAndAmortization`):**

```
Q1 2025 = 1,779,200
Q2 2025 (derived) = 3,612,700 (6mo) − 1,779,200 (Q1) = 1,833,500
Q3 2025 (derived) = 5,516,800 (9mo) − 3,612,700 (6mo) = 1,904,100
Q4 2025 (derived) = 7,421,300 (FY) − 5,516,800 (9mo)  = 1,904,500
Q1 2026            = 1,866,400

D&A_TTM = 1,833,500 + 1,904,100 + 1,904,500 + 1,866,400 = 7,508,500
EBITDA_TTM = EBIT_TTM + D&A_TTM = −826,996,600 + 7,508,500 = −819,488,100
```

**Net Income (Loss) available to common stockholders — TTM, primary-sourced (`NetIncomeLossAvailableToCommonStockholdersBasic`):**

| Q2 2025 | Q3 2025 | Q4 2025 (derived) | Q1 2026 | TTM |
|---|---|---|---|---|
| (19,982,300) | (54,808,100) | (605,544,400) | (405,813,500) | **(1,086,148,300)** |

```
Q4 2025 = FY2025 (−712,061,400) − 9mo Jan–Sep 2025 (−106,517,000) = −605,544,400
Net Margin (TTM) = −1,086,148,300 / 3,732,600 = −29,099.0%
```

**Income tax provision — TTM (`IncomeTaxExpenseBenefit`), for the ROIC/NOPAT tax-rate input:**

| Q2 2025 | Q3 2025 | Q4 2025 (derived) | Q1 2026 | TTM |
|---|---|---|---|---|
| 310,300 | 84,600 | 165,200 | 98,800 | **658,900** |

A tiny tax provision (**~$659K**) against a **$1.09B** TTM net loss — consistent with the company drawing down deferred-tax **NOL carryforwards** (see Glossary) rather than any unusual tax benefit; not a data anomaly.

### 2.3 Cash flow (primary-sourced, `NetCashProvidedByUsedInOperatingActivities` and `PaymentsToAcquirePropertyPlantAndEquipment`)

**Annual FCF (Operating Cash Flow − CapEx), all primary-sourced:**

| Fiscal Year | OCF | CapEx | FCF |
|---|---|---|---|
| FY2022 | (24,201,500) | 84,500 | **(24,286,000)** |
| FY2023 | (9,733,500) | 2,200 | **(9,735,700)** |
| FY2024 | (60,982,700) | 5,033,800 | **(66,016,500)** |
| FY2025 | 14,758,100 | 573,500 | **14,184,600** |

**Company has never been FCF-positive for 3 consecutive years** — three straight negative years (FY2022–FY2024) precede the single positive year (FY2025).

**TTM FCF (Q2 2025 + Q3 2025 + Q4 2025 derived + Q1 2026):**

```
OCF_TTM   = 2,303,100 + 10,073,500 + 12,119,300 + 17,890,000 = 42,385,900
CapEx_TTM = 552,500 + 14,000 + 3,800 + 7,300                 = 577,600
FCF_TTM   = 42,385,900 − 577,600                              = 41,808,300
```

### 2.4 Balance sheet — primary-sourced (Q1 2026 10-Q, condensed consolidated balance sheet, March 31, 2026)

| Item | Value ($) | Source |
|---|---|---|
| Cash and cash equivalents | 249,066,900 | 10-Q balance sheet |
| Short-term investments | 207,370,700 | 10-Q balance sheet |
| Long-term debt, current portion | 958,135,600 | 10-Q balance sheet (`LongTermDebtCurrent`) — the entire ~$958M convertible-note balance is classified **current** as of FY2025 year-end onward (up from $4.7–5.0M current in prior quarters) |
| Long-term debt, noncurrent | 451,200 | 10-Q balance sheet |
| **Total debt** | **958,586,800** | sum of the two lines above |
| Total Trump Media & Technology Group, Inc. stockholders' equity | 1,252,823,700 | 10-Q balance sheet — **positive**, unlike MTCH's negative-equity case, funded by the May 2025 PIPE |
| Total assets | 2,236,354,100 | 10-Q balance sheet |
| Total liabilities | 983,450,500 | 10-Q balance sheet |

```
Net Debt (cash only)          = 958,586,800 − 249,066,900                        = 709,519,900
Net Debt (cash + ST invest.)  = 958,586,800 − 249,066,900 − 207,370,700          = 502,149,200
Invested Capital = Total Debt + Equity − Cash
                 = 958,586,800 + 1,252,823,700 − 249,066,900                     = 1,962,343,600
```

**Why the debt is almost entirely classified current:** the ~$958M reflects $1.0B face value of 0.00%-coupon convertible senior secured notes due 2028 issued in the May 2025 PIPE (§2.5) — the current/noncurrent split in the FY2025 10-K balance sheet appears driven by a note-specific reclassification trigger (e.g. a conversion or redemption feature), not a near-term cash maturity crisis; the notes carry a 2028 stated maturity per the 10-K's own description (§2.5). This nuance does not change any calculation below (Net Debt totals the current and noncurrent portions either way) but is flagged so the "current" label isn't misread as an imminent repayment obligation.

### 2.5 Digital-asset treasury strategy and capital raise — FY2025 10-K, Item 1 (Business)

Per the company's own 10-K: **"TMTG has implemented a bitcoin and digital asset treasury strategy... (i) issuing debt or equity securities or engaging in other capital raising transactions and (ii) using the proceeds of such capital raises to acquire bitcoin."** On **30 May 2025**, TMTG closed a private placement (PIPE) with ~50 investors: common stock for ~$1.44B plus $1.0B face value of 0.00%-coupon convertible senior secured notes due 2028, for aggregate proceeds of **~$2.44B**. On 25 August 2025, TMTG also exchanged 2,797,985 shares of its own common stock plus $50,000 cash for 684,427,004 units of Cronos (CRO), a separate cryptocurrency token. The 10-K states TMTG ended FY2025 with **~$2,473.2M** of combined cash/short-term investments/equity securities/digital assets against **~$947.1M** of debt.

This is the direct explanation for: (a) the large jump in total assets/equity/debt on the balance sheet from FY2024 to FY2025 (§2.4), (b) the FY2025/Q1 2026 operating-loss spikes (§2.2, driven by marking the resulting bitcoin/CRO holdings to market), and (c) why straightforward "cheap on paper" balance-sheet ratios (e.g. the Net Debt/EBITDA edge case flagged in §3.1/§3.2) don't behave as the framework's formulas assume for an operating company — TMTG in FY2025–2026 is simultaneously (i) a small, structurally low-revenue media business and (ii) a large, leveraged, volatile bitcoin/crypto holding company, and its consolidated GAAP financials blend both without separating them.

### 2.6 Product/competitive disclosures — FY2025 10-K, Items 1 and 1A

Per the 10-K's own language: **"The industries in which TMTG operates or plan to operate—social media, streaming video, and financial products—are all highly competitive,"** and **"TMTG's business is highly competitive. Competition presents an ongoing threat to the success of TMTG's business."** TMTG states it aims to compete "by offering high-quality products, maintaining a steadfast commitment to free speech, and leveraging its unique brand," and separately warns: **"If TMTG's efforts to build and maintain strong brand identity, improve the user base for Truth Social and Truth+, and develop additional products are not successful, TMTG may not be able to attract or retain users."**

The 10-K discloses **no Monthly/Daily Active User counts, no subscriber counts, and no market-share figures** for Truth Social, Truth+, or any other product — a genuine, primary-source-confirmed data gap (§7), not an omission on this session's part. It does disclose the **"Patriot Package,"** a premium Truth Social subscription tier that began public beta testing 9 July 2025, later (September 2025) adding post-editing/scheduling and a "Truth gems" rewards system built on Crypto.com's wallet infrastructure — but no revenue, subscriber count, or adoption-rate figures tied to it were found.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| **FCF/NI conversion <70% for 2+ consecutive years w/o growth-capex explanation** | FY2023: 16.73% · FY2024: 16.47% · TTM: −3.85% (all shown below) | disqualify if 2+ consecutive years <70%, absent a documented growth-capex explanation | ❌ **FAILS — hard disqualifier fires** |
| Net Debt/EBITDA over threshold (2.5× standard) | EBITDA_TTM is **negative** (−$819.49M) — see formula-edge-case flag below | disqualify if >2.5× | ⚠️ **Undefined / not meaningfully testable** — see flag below; not a clean pass |
| **FCF-positive 3+ consecutive years** | FY2022 (−$24.29M) · FY2023 (−$9.74M) · FY2024 (−$66.02M) · FY2025 (+$14.18M) — 3 straight negative years, never 3 consecutive positive years | disqualify if not | ❌ **FAILS — hard disqualifier fires** |

**FCF/NI conversion detail:**

```
FY2023: FCF −9,735,700  / NI −58,189,200  = 16.73%
FY2024: FCF −66,016,500 / NI −400,864,800 = 16.47%
TTM:    FCF  41,808,300 / NI −1,086,148,300 = −3.85%   (sign-mismatched: FCF positive, NI negative)
```

All three periods sit far below the 70% threshold. **No growth-capex explanation applies** — CapEx across every period shown is trivial ($2,200–$5.03M, never more than ~1.4% of revenue), nowhere near the scale that would explain a cash-vs-accounting gap this large. The actual driver is the reverse of the framework's classic Valeant/Wirecard concern (management inflating reported earnings while starving cash): here, **GAAP net income is far more negative than actual cash burn**, driven by large non-cash charges — FY2024's $225.9M `FairValueAdjustmentOfWarrants` loss (a legacy SPAC-warrant mark-to-market charge, see Glossary) and FY2025/Q1 2026's $403.2M/$244.0M digital-asset mark-to-market losses (§2.2, §2.5). The rule's literal test still fires regardless of which direction the mismatch runs — a large, unexplained multi-year FCF/NI gap is exactly the earnings-quality signal this hard disqualifier is designed to catch, even where (as here) the mechanism is different from the graveyard-audit precedents that motivated it.

**Net Debt/EBITDA — formula edge case, flagged rather than asserted as a clean pass:**

```
EBITDA_TTM = −$819,488,100   (deeply negative — see §2.2)
Net Debt (cash + ST investments) = $502,149,200
Net Debt/EBITDA = 502,149,200 / (−819,488,100) = −0.613×
Net Debt (cash only)             = $709,519,900  →  Net Debt/EBITDA = −0.866×
```

Both variants produce a **negative** ratio, which is **below** the 2.5× threshold on a literal numeric comparison — but this is a formula artifact, not evidence of balance-sheet strength. With EBITDA deeply negative, TMTG cannot service ~$959M of debt from operating earnings **at all**, regardless of what the raw ratio says (dividing a positive net-debt figure by a negative EBITDA denominator flips the sign in a way the formula was never designed to interpret). This session does **not** claim the disqualifier "passes" — it is undefined/not meaningfully testable in this edge case, and is flagged here (in the same spirit as the MTCH session's negative-equity ROIC caveat and the 2026-06-11 backfill's flagged Rate Environment Gate inconsistency) as a gap worth a framework clarification, rather than silently resolved either way. **It does not matter to the outcome below** — the other two hard disqualifiers already fail the company independently and unambiguously.

**Two of three hard disqualifiers fire cleanly.** Per [quality-scoring.md](../framework/quality-scoring.md), this fails the company **regardless of the weighted score below** — "a weighted average can't average away an outright balance-sheet or cash-flow-quality failure." The full weighted computation is still shown below for completeness and audit trail, per this framework's "show every calculation" discipline and precedent (e.g. the 2026-07-16 MTCH, 2026-07-06 CCL, and 2026-07-10 ORCL sessions).

### 3.2 Quality Score — full computation

```
PROFITABILITY (25% weight):
  Net Margin (TTM) = −1,086,148,300 / 3,732,600 = −29,099.0%
  NetMargin_Component = clamp((−29,099.0/30)×100, 0, 100) = 0.0

  NOPAT_TTM = EBIT_TTM − Tax_TTM = −826,996,600 − 658,900 ≈ −$827,655,500
    (tax provision treated as a near-zero-rate NOL drawdown, not a meaningful positive
    effective tax rate — see §2.2; sign of NOPAT is unaffected either way, since EBIT
    alone is already deeply negative)
  Invested Capital = Total Debt + Equity − Cash = 958,586,800 + 1,252,823,700 − 249,066,900
                    = $1,962,343,600
  ROIC = −827,655,500 / 1,962,343,600 = −42.18%
  ROIC_Component = clamp((−42.18/30)×100, 0, 100) = 0.0

  Profitability_Score = (0.0 + 0.0) / 2 = 0.0
  (FCF-positive-3-years cap of 40.0 does not bind — computed value is already 0.0)

MARGINS (15% weight):
  Gross Margin (TTM) = 893,100 / 3,732,600 = 23.93%
  GrossMargin_Score = clamp((23.93/80)×100, 0, 100) = 29.91

  3yr trend check (FY2022→FY2025, annual): 96.29% → 96.01% → 82.89% → 54.51% — sharply
  CONTRACTING every year, not expanding. The +10 structural-trend bonus requires
  EXPANSION while below 40% — the opposite pattern holds here (contraction, and TTM
  23.93% is below 40% only because of the contraction, not despite it). No bonus applies.

  Margins_Score = 29.91

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2022→FY2025) = (3,682,600/1,470,500)^(1/3) − 1 = 35.80%
  Growth_Score (raw) = clamp((35.80/25)×100, 0, 100) = 100.0  (formula-capped)

  Structural deceleration modifier: −10 applies. Documented, cited evidence (§2.2):
  revenue DECLINED −12.4% FY2023→FY2024, was essentially flat (+1.76%) FY2024→FY2025,
  and Q1 2026 vs Q1 2025 grew only +6.1% — a multi-year, primary-source-confirmed
  structural deceleration, not a single cyclical quarter. The 35.80% headline 3yr CAGR
  is a base-effect artifact of an unusually small FY2022 starting figure ($1.47M), not
  a genuine ongoing growth trajectory — flagged explicitly (§4 item 2) as a case where
  the formula's literal output overstates the underlying trend, similar in spirit to
  MTCH's negative-equity ROIC inflation and Match Group's own flagged caveats.

  Growth_Score = clamp(100.0 − 10, 0, 100) = 90.0

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (TTM, cash + ST investments) = −0.613×  (EBITDA negative — see §3.1 flag)
  BalanceSheet_Score = clamp(100×(1 − (−0.613)/4), 0, 100) = clamp(115.3, 0, 100) = 100.0

  FLAGGED AS A FORMULA ARTIFACT, not a genuine balance-sheet-strength finding — see the
  full explanation in §3.1. A company that cannot cover interest or debt service from
  operating earnings at all should not literally score at the ceiling of this sub-score;
  this is exactly the kind of edge case "never invent or estimate" argues for flagging
  rather than silently resolving. The robustness check below shows the Quality Score
  outcome is unchanged even crediting this sub-score at 0.0 instead.

MOAT SIGNAL (15% weight) — 5-signal checklist, every signal evaluated against a specific
citation from the FY2025 10-K (§2.6):

  Market share stable/growing — FALSE. No MAU/DAU, subscriber count, or market-share
    figure is disclosed anywhere in the 10-K for Truth Social, Truth+, or any other
    product (confirmed absent, not merely unfound) — a data gap, not credited.

  Brand premium — FALSE. No pricing-power evidence (price increases without volume
    loss, or a premium vs. competitors) was found. The Patriot Package premium tier
    (§2.6) launched in beta July 2025, but no revenue, adoption, or ARPU figures tied
    to it are disclosed.

  Network effect — FALSE. No documented mechanism (two-sided marketplace dynamics,
    user-growth-driven value) was found in the 10-K's business or risk-factor sections.

  Switching costs — FALSE. No documented mechanism (contractual lock-in, integration
    depth, data-migration cost) was found — unlike MTCH's explicit "low switching
    costs" admission, DJT's 10-K simply does not address this dimension at all (a data
    gap rather than a negative statement, but not credited either way absent evidence).

  Scale cost advantage — FALSE. No cost-per-unit data vs. smaller competitors was found.

  Moat_Score = (0/5) × 100 = 0.0

FCF QUALITY (10% weight):
  FCF/NI (TTM) = 41,808,300 / −1,086,148,300 = −3.85%
  FCFQuality_Score = clamp(((−0.0385 − 0.40)/0.60)×100, 0, 100) = clamp(−73.1, 0, 100) = 0.0

QUALITY SCORE = 0.0×0.25 + 29.91×0.15 + 90.0×0.20 + 100.0×0.15 + 0.0×0.15 + 0.0×0.10
             = 0.000 + 4.4865 + 18.000 + 15.000 + 0.000 + 0.000
             = 37.4865 → rounds to 37.5
```

**Robustness check (not just a point estimate) — even in the maximally generous reading of the two flagged edge-case sub-scores (Balance Sheet's negative-EBITDA artifact, Growth's tiny-base-effect CAGR), the Quality Score is 37.5 — nowhere close to 80.0.** Conversely, reading those same two sub-scores at their more economically meaningful values (Balance Sheet at 0.0 — a company that cannot cover its debt from operating earnings at all should not score at the ceiling; Growth judged on the flat/declining recent-quarters trend rather than the tiny-base 3yr CAGR, which nets to 0.0 after the deceleration modifier):

```
0.0×0.25 + 29.91×0.15 + 0.0×0.20 + 0.0×0.15 + 0.0×0.15 + 0.0×0.10 = 4.49
```

**The Quality Score falls somewhere in a 4.5–37.5 range depending on how the two flagged edge cases are read — and every point in that range fails the 80.0+ gate by a wide margin.** This is not a marginal or close call in either direction.

### 3.3 Gate result

**Quality Score = 37.5 / 100.0 (upper bound of a 4.5–37.5 robustness range) — FAILS the 80.0+ gate**, and **independently** fails via two of three hard disqualifiers (FCF/NI conversion <70% for 2+ consecutive years, and not FCF-positive for 3+ consecutive years — §3.1). DJT fails multiple independent ways simultaneously. Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md): **stop here — do not proceed to the Rate Environment Gate, Phase 02 valuation scoring, the Composite Score, or fair-value/order-setup work.**

---

## 4. Qualitative Notes

1. **This is fundamentally two businesses bolted together, and the framework's formulas were built for one at a time.** TMTG is simultaneously (a) a small, low-revenue, structurally-thinning-margin social-media/streaming business (~$3.7M TTM revenue, gross margin collapsing from 96% to 24% over three years) and (b) a large, debt-and-equity-funded bitcoin/digital-asset holding vehicle (~$2.47B of combined liquid assets/digital assets against ~$959M of debt, per the 10-K's own framing, §2.5). Consolidated GAAP financials blend both without separating them, which is exactly why the Net Debt/EBITDA and 3yr-CAGR sub-scores produced the flagged edge-case artifacts in §3.1–3.2 — the crypto-treasury swings dominate the P&L enough to make ratios built around "normal operating company" assumptions behave unpredictably.
2. **The 35.80% headline revenue CAGR is real arithmetic on a genuinely misleading base.** FY2022's $1.47M revenue figure was itself a very early, thin number; growth to FY2023 was real but growth has since stalled and partially reversed (§2.2). A reader who saw only "Growth_Score = 90.0" without this context would draw the wrong conclusion about the underlying trajectory — flagged explicitly here per "show every calculation, no black box."
3. **The Net Debt/EBITDA hard disqualifier's formula behavior with negative EBITDA is a genuine, unresolved framework gap**, not specific to DJT — any sufficiently unprofitable company with net debt will produce a negative (and therefore literally sub-threshold) ratio under the current formula, which is the opposite of the intended signal. This session does not attempt to silently patch the rule; it is flagged here as a candidate item for a future `decisions/` entry and `quality-scoring.md` clarification (e.g. "if EBITDA_TTM ≤ 0, treat the Net Debt/EBITDA hard disqualifier as automatically triggered rather than computing a ratio"), consistent with the framework's own precedent of recording such gaps rather than quietly resolving them mid-session (see the 2026-06-11 watchlist backfill's flagged Rate Environment Gate inconsistency).
4. **The gate failure here is overdetermined** — unlike a close call, DJT fails on Profitability (0.0, the largest-weighted sub-score at 25%), FCF Quality (0.0), Moat (0.0), two independent hard disqualifiers, and a Balance Sheet sub-score that would also read as a fail (0.0) under the more defensible edge-case interpretation. Even the single most generous plausible reading of every disputed input tops out at 37.5 — less than half the 80.0 bar.
5. **The triggering Telegram post's substantive claim (a paid, faster-access product marketed toward institutional/Wall-Street trading use) is not addressed anywhere in the FY2025 10-K or Q1 2026 10-Q reviewed here** (§0, §2.6) — if real and recent, it postdates the primary sources available to this session and is not itself a scored input under Rule 0/9. Nothing in this session either confirms or denies that claim; it was used only as the reason to run this evaluation.

---

## 5. Recommendation

# **PASS — Quality Gate FAIL (Quality Score 37.5 upper-bound / 4.5 lower-bound, both < 80.0; independently confirmed by two hard disqualifiers — FCF/NI conversion <70% for 2+ consecutive years, and not FCF-positive for 3+ consecutive years). Do not enter.**

Trump Media & Technology Group fails the framework's strict 80.0+ Quality Score gate by a wide margin under every plausible reading of its two formula-edge-case sub-scores, and independently fails two of the three hard disqualifiers outright. **No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup was computed**, per the Quality Score protocol (stop at the gate). The Telegram post that triggered this session — a claimed new institutional-access paid product — is not addressed in either primary source reviewed and was not itself relied upon for any scoring conclusion.

---

## 6. Next Review Trigger

- **DJT's Q2 2026 earnings** (date not yet disclosed in sources reviewed) — the standard Rule 9 quarterly trigger; will show whether the FY2025/Q1 2026 pattern of crypto-treasury-driven operating losses continues, whether gross margin stabilizes or keeps contracting, and whether the ~$959M convertible-note balance's "current" classification (§2.4) resolves into an actual near-term repayment/refinancing event worth tracking as a Rule 9 balance-sheet trigger in its own right.
- **Any confirmed announcement of the institutional/Wall-Street-targeted early-access product** referenced in the triggering Telegram post — if it materializes into a disclosed, material revenue line, it would be a legitimate Rule 9 trigger for re-evaluation (though on current financials it would need to be extraordinarily large to move the Profitability/FCF Quality sub-scores meaningfully).
- **Standard Rule 9 triggers:** management change, material M&A, a macro/rate shift, a >15% unexplained price move (today's −2.49% move is minor and not itself a trigger), or a material swing in the company's bitcoin/digital-asset holdings' fair value large enough to flip FY2026 operating income.

**No position opened — nothing to log in `decisions/`.**

---

## 7. Data Gaps Flagged

1. **User metrics** (MAU, DAU, subscriber counts) for Truth Social, Truth+, or the Patriot Package tier — not disclosed anywhere in the FY2025 10-K or Q1 2026 10-Q reviewed; confirmed absent via primary-source text review (§2.6), not merely unfound. Non-blocking — the Moat Signal checklist treats an undisclosed metric as a data gap (FALSE, not credited), consistent with "never invent or estimate," and the gate fails independently regardless.
2. **Market-share data** for Truth Social/Truth+ vs. competing platforms — not disclosed by the company and no independent third-party source was reviewed for this session (out of scope given the gate already fails decisively on primary-sourced figures). Non-blocking for the same reason.
3. **Cost-per-unit data** vs. smaller competitors, needed to credit the "Scale cost advantage" Moat Signal — not found; scored FALSE as a data gap, not a negative finding.
4. **Institutional/Wall-Street early-access product** referenced in the triggering Telegram post — not found in either primary source reviewed (§0, §4 item 5); if real, it postdates the filings available to this session.
5. **Precise reclassification trigger** for the ~$958M convertible-note balance moving from noncurrent to current between FY2024 and FY2025 year-end — noted in §2.4 as likely a note-specific conversion/redemption feature rather than a near-term cash-maturity crisis, based on the notes' disclosed 2028 stated maturity, but the exact contractual trigger was not independently traced to a specific indenture clause within this session's scope. Non-blocking for the gate conclusion.

None of these gaps affect the Quality Gate conclusion (§3.3), which is driven by well-sourced, primary-cited figures and two independently-firing hard disqualifiers.

---

## 8. Glossary

| Term | Meaning |
|---|---|
| **Bitcoin / Digital assets** | See also **Digital-asset (crypto) treasury strategy** below. A decentralized cryptocurrency; TMTG holds bitcoin (and separately, Cronos/CRO tokens) as a balance-sheet treasury asset, marked to fair value each reporting period. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. Flagged this session (§3.2, §4) as capable of being misleading when the starting value is unusually small. |
| **CIK (Central Index Key)** | The unique numeric identifier the SEC assigns to every company that files with EDGAR — used to construct the filing-lookup paths this framework pulls SEC data from. |
| **de-SPAC merger** | The transaction in which a SPAC completes its combination with a private operating company, converting the private company into a publicly-traded one under the SPAC's listing. Trump Media & Technology Group went public this way in March 2024 (Digital World Acquisition Corp. → TMTG), the origin of the SPAC-era warrant liability referenced below. |
| **Digital-asset (crypto) treasury strategy** | A corporate strategy of raising capital specifically to acquire and hold cryptocurrency as a balance-sheet reserve asset. TMTG adopted this in 2025, raising ~$2.44B via a PIPE and convertible notes to fund bitcoin (and Cronos/CRO) purchases — see full Glossary entry in [glossary.md](../framework/glossary.md). |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / — before Interest, Taxes, Depreciation, and Amortization — operating profit, and a rough proxy for cash operating profit, respectively. TMTG's TTM EBITDA is deeply negative. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check) — the FCF/NI check independently failed TMTG this session. |
| **Hard disqualifier** | One of three Quality Score conditions that fail a company regardless of its weighted score. TMTG independently fired two of the three. |
| **Invested Capital** | The total capital (debt + equity, netted for cash) put to work in a business — the denominator in this framework's ROIC calculation. |
| **Mezzanine equity / PIPE / de-SPAC / Warrant** | See individual entries — all relate to TMTG's 2024 SPAC-merger and 2025 capital-raise history. |
| **NOL (Net Operating Loss) carryforward** | Accumulated tax losses a company can use to offset future taxable income — the reason TMTG's income-tax provision is near-zero despite a very large GAAP net loss. Full entry in [glossary.md](../framework/glossary.md). |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; this framework's primary balance-sheet-risk gate. Flagged this session as producing a formula artifact when EBITDA is negative (§3.1). |
| **Net Margin** | Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit. |
| **PIPE (Private Investment in Public Equity)** | A private placement of newly-issued stock (and sometimes debt) sold directly to institutional investors. TMTG's ~$2.44B May 2025 PIPE funded its bitcoin treasury strategy. Full entry in [glossary.md](../framework/glossary.md). |
| **Quality Score** | This framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to proceed to valuation scoring. TMTG scored in a 4.5–37.5 range depending on edge-case interpretation, well below the gate either way. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns invested capital into profit; a core quality signal in this framework. TMTG's TTM ROIC is deeply negative (−42.18%). |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work. |
| **Rule 6** | This framework's instruction to normalize/separate non-recurring or non-operating items before valuing a business — applied here to flag the crypto-treasury mark-to-market losses as distinct from TMTG's core media-business economics, without excluding them from the scored GAAP figures. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move. |
| **SPAC** | Special Purpose Acquisition Company — the shell-company structure TMTG used to go public in March 2024, leaving a distorted early public financial history (large one-off warrant fair-value charges). |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure. |
| **Warrant (fair-value adjustment)** | A stock-purchase right, commonly issued in SPAC deals, that must be marked to fair value each period when liability-classified — TMTG's FY2024 results included a $225.9M non-cash loss from this. Full entry in [glossary.md](../framework/glossary.md). |
| **XBRL (eXtensible Business Reporting Language)** | The structured, machine-readable data format the SEC requires public companies to tag their financial-statement figures in — the primary data source for this session. |

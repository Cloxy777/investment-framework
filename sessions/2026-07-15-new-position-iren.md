# NEW POSITION — IREN (IREN Limited, formerly Iris Energy, NASDAQ) — 2026-07-15

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — fully automated, no human in loop)
**Date:** 15 Jul 2026
**10Y US Treasury Yield:** 4.62% (FRED `DGS10`, most recent posted observation as of this session, dated 2026-07-13 — normal 1-day FRED reporting lag; consistent with the value used in this same day's SNDK, ASML, BRK, and PYPL sessions)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §4). For reference only, the bracket in force is +5 (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current IREN portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — this is IREN's first-ever evaluation under this framework.
**Sector:** Bitcoin mining, pivoting to vertically-integrated AI Cloud / data center infrastructure — owns its own power, real estate, and data centers rather than leasing capacity from a third party.
**Filer type:** SEC domestic filer since FY2025 (10-K/10-Q), CIK **0001878848**. Previously filed as a foreign private issuer under Form 20-F (through FY2024) as "Iris Energy Ltd" (renamed to "IREN Ltd" 2024-11-29; originally "Iris Energy Pty Ltd"). Headquartered in Sydney, Australia. Fiscal year ends **30 June**.
**First-use jargon decode:** see closing Glossary (§9).

---

## 0. Why this session exists — trigger source

A Telegram post (**FinnInvestChannel, ~18:34 UTC, 2026-07-15**) mentioned IREN hired two senior executives from Oracle and Google to develop its AI Cloud platform and build new data centers, and plans to expand energy capacity to 5 GW for AI infrastructure. Per the operating brief, **Telegram post text is never used as financial data or even treated as a confirmed fact** — it is a trigger only. IREN had no watchlist entry anywhere in the repo and is not a current holding, which unconditionally triggers a first-ever `/new-position` evaluation.

**Independent verification performed (all before any of it was used as input to scoring):**
- **Executive hires:** confirmed via IREN's own press release (GlobeNewswire, 2 Jul 2026, "IREN Appoints Chief Product Officer and Chief Development Officer") — Kambiz Aghili (ex-Oracle Cloud Infrastructure VP of Products) named Chief Product Officer; Michael Nudelman (ex-Google, CyrusOne, Beale Infrastructure) named Chief Development Officer, tasked with expanding the "5GW secured grid-connected power portfolio."
- **5 GW target:** confirmed via IREN's own NVIDIA partnership announcement and multiple independent trade-press sources (Data Center Knowledge, Yahoo Finance) — a strategic partnership with NVIDIA to deploy up to 5 GW of AI infrastructure, with a broader disclosed pipeline of ~5.8 GW across North America, Europe, and Australia.
- **The broader AI Cloud pivot context:** independently confirmed via IREN's own 3 Nov 2025 GlobeNewswire release — a 5-year, ~$9.7B GPU cloud services agreement with Microsoft (NVIDIA GB300 GPUs, 20% prepayment), alongside a ~$5.8B GPU/equipment purchase agreement with Dell.

The post's claims check out factually. Independent verification below (SEC EDGAR primary filings) shows the underlying business — despite this real, well-documented strategic pivot — currently fails this framework's quality gate on both cash-generation and balance-sheet grounds.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$38.17** | IBKR `get_price_snapshot` (contract_id **526906130**, NASDAQ, "IREN LTD" — confirmed correct entity via `search_contracts`, disambiguated from: Investis Holding SA (Swiss, also ticker "IREN" on EBS), IREN SpA (Italian multi-utility, ticker "IRE" on BVME), Irenic Acquisition Corp (SPAC, "IACQ"/"IACQU"), and five leveraged/derivative single-stock ETF products tracking IREN — IREX (TRADR 2x Long), IREZ (TRDR 2x Short), IREG (Leverage Shares 2x), IRN3/3IRN (Leverage Shares 3x Long ETP, LSE/AEB-listed), IREY/YIRE (Incomeshares option-income ETP) — none of which are the underlying operating company), `last` field, timestamp fetched 2026-07-15 20:05:41 UTC (confirmed via `date -u` at fetch time) |
| Change vs. prior close | **−$0.42 / −1.09%** | IBKR `get_price_snapshot` `change` field (prior close $38.59) |
| Bid / Ask | $38.20 / $38.32 | IBKR `get_price_snapshot` |
| 52-week range | Low **$14.72** · High **$76.87** · Open (52w ago) $17.33 | IBKR `get_price_snapshot` `misc_statistics` — a wide ~5.2x range, consistent with a name that has re-rated sharply on the AI Cloud pivot and Microsoft contract news since late 2025 |
| Independent cross-check | ~$39.02 (aggregated web quote feed, 2026-07-15) — within normal intraday timing variance of the IBKR live snapshot | WebSearch, 2026-07-15 |
| Analyst consensus PT (bull-case sanity reference only, not used in any calculation) | ~$80.93 average (S&P Global aggregation, 16 analysts, consensus rating "Buy": 15 Buy / 7 Hold / 1 Sell) | WebSearch, 2026-07-15 |
| US 10Y Treasury yield | 4.62% | FRED `DGS10`, as-of 2026-07-13 |

**$38.17 is used as the live price for this session.**

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note — filer-status history

IREN converted from a foreign private issuer (Form 20-F, IFRS-adjacent presentation) to a US domestic filer (Form 10-K/10-Q, US GAAP) beginning with its **first 10-K, filed 2025-08-28, covering FY2025** (fiscal year ended 30 June 2025). All figures used below are pulled directly from SEC EDGAR's XBRL `companyfacts` API (`data.sec.gov/api/xbrl/companyfacts/CIK0001878848.json`) and cross-checked against the underlying 10-K/10-Q HTML filings. Unlike SanDisk's carve-out-financials situation (2026-07-15 session), IREN's FY2023 revenue figure reported under the old 20-F/IFRS basis ($75.509M) matches **exactly** the FY2023 figure later reported under the new 10-K/US GAAP basis ($75.509M) — an internal consistency check indicating this is a genuine basis-conversion, not a carve-out/pro-forma restatement. No comparability flag is needed for the income-statement figures used here.

### 2.2 Income statement — primary-sourced, US GAAP ($ millions)

| | FY2023 (10-K) | FY2024 (10-K) | FY2025 (10-K) |
|---|---|---|---|
| Revenue | 75.509 | 187.192 | 501.023 |
| Cost of revenue | 39.419 | 87.067 | 158.992 |
| Gross profit | 36.090 | 100.125 | 342.031 |
| Gross margin | 47.79% | 53.49% | 68.27% |
| Operating income (loss) | (157.241) | (27.234) | **17.327** |
| **Net income (loss)** | **(171.827)** | **(28.920)** | **86.941** |

Source: [10-K filed 2025-08-28](https://www.sec.gov/Archives/edgar/data/1878848/000187884825000063/0001878848-25-000063-index.htm) (`us-gaap:Revenues`, `CostOfRevenue`, `OperatingIncomeLoss`, `NetIncomeLoss`).

**Most recent quarterly data — 9 months ended 31 Mar 2026, 10-Q filed 2026-05-08** ($ millions):

| | 9mo ended 31-Mar-2026 | 9mo ended 31-Mar-2025 (comparative) |
|---|---|---|
| Revenue | 569.782 | 313.731 |
| Cost of revenue | 186.369 | 106.104 |
| Operating income (loss) | (426.331) | (0.561) |
| Net income (loss) | (18.622) | (89.735) |
| Operating cash flow (OCF) | 289.326 | 142.745 |
| CapEx (PP&E purchases) | 1,669.157 | 389.342 |
| D&A | 305.647 | 117.319 |

Source: [10-Q filed 2026-05-08](https://www.sec.gov/Archives/edgar/data/1878848/000187884826000026/iren-20260331.htm), Condensed Consolidated Statements of Operations and Cash Flows.

### 2.3 TTM reconstruction (ending 31 Mar 2026)

Standard method (FY2025 full year − 9mo comparative ended 31-Mar-2025 + 9mo current ended 31-Mar-2026):

```
Revenue TTM         = 501.023 − 313.731 + 569.782  = 757.074   ($M)
Cost of revenue TTM = 158.992 − 106.104 + 186.369   = 239.257
Gross profit TTM     = 757.074 − 239.257            = 517.817   → Gross Margin TTM = 68.40%
Op income TTM        = 17.327 − (−0.561) + (−426.331)= −408.443
Net income TTM       = 86.941 − (−89.735) + (−18.622)= 158.054  → Net Margin TTM = 20.88%
OCF TTM               = 245.886 − 142.745 + 289.326  = 392.467
CapEx TTM             = 573.456 − 389.342 + 1,669.157 = 1,853.271
FCF TTM (OCF−CapEx)   = 392.467 − 1,853.271          = (1,460.804)
D&A TTM                = 181.136 − 117.319 + 305.647 = 369.464
EBITDA TTM (OpInc+D&A) = −408.443 + 369.464           = (38.979)
```

### 2.4 Cash flow — 3 fiscal years, FCF by year ($ millions)

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Operating cash flow (OCF) | 5.729 | 52.219 | 245.886 |
| CapEx (PP&E purchases) | 116.064 | 141.855 | 573.456 |
| **Free Cash Flow (OCF − CapEx)** | **(110.335)** | **(89.636)** | **(327.570)** |

Source: [10-K filed 2025-08-28](https://www.sec.gov/Archives/edgar/data/1878848/000187884825000063/0001878848-25-000063-index.htm), Consolidated Statements of Cash Flows (`us-gaap:NetCashProvidedByUsedInOperatingActivities`, `PaymentsToAcquirePropertyPlantAndEquipment`).

**All three most recently completed fiscal years are FCF-negative, and the deficit is widening — not narrowing — as the AI infrastructure buildout accelerates** (9-month FY2026 CapEx of $1,669.157M is already 4.3x the same period a year earlier).

### 2.5 Balance sheet — primary-sourced (10-Q filed 2026-05-08, $ millions, as of 31 Mar 2026)

| | 31-Mar-2026 |
|---|---|
| Cash and cash equivalents | 2,213.274 |
| Total assets | 7,264.897 |
| Convertible notes payable (non-current) | 3,687.832 |
| Finance lease liability | 274.256 |
| **Total debt** | **3,962.088** |
| Total liabilities | 4,600.369 |
| Total shareholders' equity | 2,664.528 |

```
Net Debt (31 Mar 2026)  = Total Debt − Cash = 3,962.088 − 2,213.274 = 1,748.814   ($M)
Net Debt / EBITDA (TTM) = 1,748.814 / (38.979)  → undefined / not computable as a meaningful finite multiple
                            (positive net debt divided by NEGATIVE trailing EBITDA — see §3.1)
```

**⚠️ This balance sheet materially understates IREN's current leverage.** Per the 10-Q's own Note 22 (Subsequent Events) and independent financial-press reporting (Cointelegraph, 18 Jun 2026; cryptobriefing.com), after 31 Mar 2026:
- A **~$3.0B additional convertible senior notes offering** (upsized from an initially-marketed $2.6B) closed in **May 2026**.
- A **~$3.6B delayed-draw financing package** (Goldman Sachs / JPMorgan; $1.5B delayed-draw term loan + $2.1B senior notes due 2031), tied to satisfying obligations under the Microsoft Agreement, was still only a **binding commitment letter** as of the 10-Q's filing date — "subject to... execution of definitive agreements" — not yet drawn or reflected on this balance sheet.
- Independent industry analysis (Blocksbridge Consulting via VanEck data, cited across multiple outlets in June 2026) estimates IREN faces a **~$21.1B funding gap** to complete its disclosed AI infrastructure buildout — the largest of any public Bitcoin miner pursuing an AI pivot.

**This does not block completing the Quality Score** (the filed 31-Mar-2026 balance sheet is a genuine, primary-sourced snapshot), but it is flagged explicitly, not silently substituted around: the true current leverage picture is worse than what's computed below.

### 2.6 Revenue segmentation — Bitcoin mining vs. AI Cloud Services (9 months ended 31 Mar 2026, $ millions)

| Segment | Revenue | % of total | Segment cost of revenue | Segment gross profit | Segment gross margin |
|---|---|---|---|---|---|
| Bitcoin mining | 511.502 | **89.8%** | 178.649 | 332.853 | 65.06% |
| AI Cloud Services | 58.280 | **10.2%** | 7.720 | 50.560 | 86.75% |
| **Total** | **569.782** | 100% | 186.369 | 383.413 | 67.30% |

Source: [10-Q filed 2026-05-08](https://www.sec.gov/Archives/edgar/data/1878848/000187884826000026/iren-20260331.htm), Note 4 (Segment Information). The Group began separately reporting these two segments only in the quarter ended 30 Sep 2025 (previously reported as a single segment); comparative periods were recast.

**Despite the market-moving Microsoft/NVIDIA news, IREN's actual, realized business today is still overwhelmingly Bitcoin mining (89.8% of the most recent 9 months' revenue).** AI Cloud Services revenue is growing very fast off a small base ($9.431M → $58.280M over the comparable 9-month periods, +518% YoY) and shows meaningfully better unit economics (86.75% segment gross margin vs. 65.06% for Bitcoin mining) — a genuinely positive forward signal — but is too small today to be the primary driver of either the consolidated Growth sub-score or the Moat evidence scored below.

### 2.7 Earnings-quality flag — the source of IREN's reported net income

TTM Net Income of +$158.054M (§2.3) is **not representative of operating profitability**. TTM Operating Income is deeply negative (−$408.443M). The gap is explained by a large, disclosed, non-operating, non-cash item:

```
us-gaap:UnrealizedGainLossOnInvestments, quarter ended 30-Sep-2025 (Q1 FY2026): +$664.993M
```

This is a mark-to-market gain on IREN's **Prepaid Forward Contracts** — equity derivatives entered alongside several tranches of its Convertible Notes (2029–2033) to reduce future share-count dilution — driven by IREN's own stock price rising sharply during that quarter. This single line item is larger than IREN's entire Q1 FY2026 revenue ($240.295M) and single-handedly explains that quarter's reported net income of +$384.611M. A related, smaller version of the same dynamic (+$77.518M) also lifted FY2025's reported net income.

**Sensitivity check (informational only — not substituted into the scored formula, consistent with "never invent or estimate financial data"):** excluding this one disclosed, quantified item, TTM Net Income would be approximately $158.054M − $664.993M ≈ **−$506.9M**, an operating-basis net margin of roughly **−67%**, essentially the mirror image of the as-reported +20.88% figure used in the formula below. This is flagged prominently throughout §3.

### 2.8 Moat evidence — cited sources

| Signal | Result | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE (weak signal, flagged)** | IREN operated a **36.0 EH/s** Bitcoin mining hash rate (38.0 EH/s installed) as of 31 Mar 2026, reaching a self-reported 50 EH/s milestone shortly after (The Block, 2026); CoinShares' Q1 2026 Bitcoin Mining Report places IREN's installed hashrate at ~46 EH/s, roughly **5–6% of the ~1,020–1,160 EH/s global Bitcoin network** — among the larger public miners by this measure, and growing in absolute terms. **⚠️ This reflects commodity Bitcoin-mining scale (a function of capital deployed into ASIC hardware and secured power, not customer-facing differentiation) — a similarly weak, cyclical-commodity caveat as this framework's existing DRAM/NAND framing (see glossary). Credited per the letter of the checklist given a genuine, cited, third-party share figure exists, but flagged as not evidence of a durable, customer-facing moat.** |
| Brand premium | **FALSE** | No third-party or primary-source evidence located of IREN commanding a price premium (in either Bitcoin mining hosting or nascent AI Cloud services) without volume loss. AI Cloud Services is a brand-new business line (10.2% of revenue, effectively one material contracted customer to date) — too early for pricing-power evidence to exist. |
| Network effect | **FALSE** | Neither Bitcoin mining nor GPU-cloud hosting exhibits two-sided marketplace dynamics. |
| Switching costs | **Not credited** | IREN's 5-year, ~$9.7B Microsoft GPU Cloud Services Agreement (20% prepayment; GlobeNewswire, 3 Nov 2025) is real, binding, and documented — but it primarily evidences revenue *visibility* for IREN and lock-in *for Microsoft* as the customer paying into physical infrastructure. No specific mechanism (early-termination penalty, integration-depth, migration-cost detail) was located in the primary sources reviewed this session demonstrating that IREN's *own* customers face a durable switching cost protecting IREN's future pricing power from competition — the same "mechanism required, not just contract existence" standard applied in this framework's SNDK session. Not credited absent that specificity. |
| Scale cost advantage | **FALSE** | Secondary commentary (Yahoo Finance, Simply Wall St) asserts IREN's vertically-integrated ownership of power, real estate, and data centers should produce a cost advantage vs. competitors leasing capacity — plausible, but no specific $/MW, $/EH, or $/GPU-hour cost-per-unit comparison against named competitors was located in primary filings or cited third-party research this session. Not credited absent that citation, consistent with this framework's identical non-credit for SNDK (§2.6 of that session) and Toyota Production System (glossary) for the same reason. |

```
Moat_Score = (1 of 5 TRUE) / 5 × 100 = 20.0
```

### 2.9 Going-concern check

No going-concern language was located in the FY2025 10-K or the Q3 FY2026 10-Q (text-searched directly). This does not offset the hard-disqualifier findings below, but is noted for completeness per quality-scoring.md's disqualifier checklist.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF positive 3+ consecutive years | FY2023: **($110.335)M** · FY2024: **($89.636)M** · FY2025: **($327.570)M** — all three most recent complete fiscal years FCF-negative, and **worsening**, not narrowing | disqualify if not 3 consecutive positive years | **❌ FIRES, cleanly and unambiguously.** Zero of the last 3 complete fiscal years were FCF-positive. Per [glossary.md](../framework/glossary.md)'s **Hard disqualifier** entry, this specific check carries **no carve-out** — the well-documented cause (a genuine, large-scale AI infrastructure capital buildout) does not exempt it. |
| Net Debt/EBITDA over threshold (2.5× standard; not asset-light eligible — a capital-intensive hardware/infrastructure operator, not a payment network or exchange) | Net debt $1,748.814M (§2.5, itself understated — see the subsequent-events flag) against **negative** TTM EBITDA of ($38.979)M (§2.3) | disqualify if exceeds 2.5× | **❌ EFFECTIVELY FIRES.** The ratio is not computable as a meaningful finite multiple — positive net debt divided by negative EBITDA. The formula's literal mechanics would spuriously flip this to a *negative* ratio (read by the scoring formula below as a "better than 0×" balance sheet), which is the opposite of what a company carrying ~$4.0B of debt (before ~$3B+ of additional financing raised/pending after this filing) against **negative** trailing operating cash profitability actually represents. Flagged as an edge-case the raw formula doesn't handle, not silently computed at face value — see §3.2 for the conservative score applied instead. |
| FCF/NI conversion <70% for 2+ consecutive years w/o growth-capex explanation | FY2023: (110.335)/(171.827) = 64.2% (both negative — not economically meaningful) · FY2024: (89.636)/(28.920) = 309.9% (both negative, small NI denominator — not economically meaningful) · FY2025: (327.570)/86.941 = **−376.8%** (FCF deeply negative while NI positive — a genuine, meaningful, and clearly bad signal: reported accounting profit is not converting to cash at all) | disqualify if 2+ **consecutive** years <70% w/o carve-out | **Ambiguous under the literal formula** (sign-mixing across years prevents a clean "ratio < 70% for 2 consecutive years" reading, the same convention issue flagged in this framework's SNDK/SPCX sessions) — **not** independently relied upon to fire this gate, since the other two checks already do so unambiguously. Shown for transparency; qualitatively consistent with poor cash-earnings quality throughout. |

**Two of three hard disqualifiers fire (FCF-positivity cleanly; Net Debt/EBITDA via the negative-EBITDA edge case). Per quality-scoring.md and this session's explicit instructions: STOP HERE — do not proceed to Phase 02 valuation scoring, regardless of the weighted Quality Score computed below.**

### 3.2 Quality Score — full computation (produced for the record, per the "every sub-score shown" instruction, even though the gate has already failed above)

```
PROFITABILITY (25% weight):
  Net Margin (TTM) = 158.054 / 757.074 = 20.88%
  ⚠️ Heavily distorted by the one-off, non-cash Prepaid Forward Contract mark-to-market gain (§2.7).
    Excluding that single disclosed item, TTM Net Margin would be approximately −67.0% (sensitivity
    only, not substituted into the formula).
  NetMargin_Component = clamp((20.88/30)×100, 0, 100) = 69.6

  EBIT_TTM = −408.443  (deeply negative — see §2.3)
  Invested Capital (31 Mar 2026) = Total Debt + Equity − Cash = 3,962.088 + 2,664.528 − 2,213.274
                                  = 4,413.342
  ⚠️ NOPAT approximated as EBIT_TTM directly (a meaningful effective-tax-rate adjustment could not be
    derived this period — TTM pretax income is negative and swung by large, volatile one-off tax items,
    e.g. a $190.687M tax expense in Q1 FY2026 alone against the one-off gain in §2.7 — flagged rather
    than invented; the sign of ROIC is unaffected by this simplification since EBIT is unambiguously
    negative regardless of a reasonable tax-rate assumption).
  ROIC = −408.443 / 4,413.342 = −9.26%
  ROIC_Component = clamp((−9.26/30)×100, 0, 100) = clamp(−30.9, 0, 100) = 0.0

  Raw Profitability_Score = (69.6 + 0.0) / 2 = 34.8
  FCF-positivity cap check: raw score (34.8) is already below the 40.0 cap ceiling — cap does not
    additionally reduce it.
  Profitability_Score = 34.8

MARGINS (15% weight):
  Gross Margin (TTM) = 68.40%
  GrossMargin_Score = clamp((68.40/80)×100, 0, 100) = 85.5
  3yr trend IS expanding (FY2023 47.8% → FY2024 53.5% → FY2025 68.3% → TTM 68.4%), but the "+10 while
    below 40%" bonus condition requires gross margin to currently be below 40%; TTM (68.4%) is already
    well above that threshold, so the bonus does not apply.
  Margins_Score = 85.5

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2022 $59.037M → FY2025 $501.023M) = (501.023/59.037)^(1/3) − 1 = 103.95%
  Growth_Score = clamp((103.95/25)×100, 0, 100) = clamp(415.8, 0, 100) = 100.0  (saturated)
  TAM/pricing-power modifier: NOT applied. The consolidated 3yr CAGR is overwhelmingly explained by
    Bitcoin mining revenue growth (89.8% of the most recent 9 months, §2.6) — a function of Bitcoin
    price appreciation and hash rate expansion, a commodity-cyclical dynamic similar to this framework's
    existing DRAM/NAND caution (glossary), not yet the AI Cloud TAM-expansion story driving market
    attention. The AI Cloud segment itself IS growing on a genuine, documented catalyst (Microsoft
    $9.7B contract, NVIDIA 5GW partnership) but remains too small (10.2% of revenue) to be the primary
    driver of the metric being scored. Moot for the final number either way — the score is already
    saturated at the 100.0 ceiling regardless of whether a +10 modifier would apply.
  Growth_Score = 100.0

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (TTM) = $1,748.814M / ($38.979M) — undefined as a meaningful finite ratio (§3.1).
  ⚠️ The raw formula `clamp(100 × (1 − NetDebt/EBITDA / 4), 0, 100)` would compute NetDebt/EBITDA as a
    NEGATIVE number here (positive net debt ÷ negative EBITDA), which the formula would then read as
    BETTER than a 0× (net-cash) balance sheet — clamping to a spurious 100.0. This is a formula blind
    spot for the negative-EBITDA case, not a genuine reading of balance-sheet strength: a company
    carrying ~$4.0B of debt (understated per §2.5) against NEGATIVE trailing operating cash profitability
    cannot service that debt from current operations by any reasonable interpretation of what this ratio
    is meant to measure. Per this session's discretion (flagged explicitly, not invented data) the
    conservative score is used instead of the formula's face-value output.
  BalanceSheet_Score = 0.0  (conservative override; raw formula's spurious 100.0 shown, not used)

MOAT SIGNAL (15% weight) — see §2.8 for full evidence:
  1 of 5 TRUE (Market share stable/growing, flagged as a weak/commodity signal) — Brand premium,
   Network effect, Switching costs, Scale cost advantage all not credited for lack of qualifying evidence.
  Moat_Score = (1/5) × 100 = 20.0

FCF QUALITY (10% weight):
  TTM FCF/NI = (1,460.804) / 158.054 = −924.3%
  FCFQuality_Score = clamp(((−9.243 − 0.40)/0.60)×100, 0, 100) = clamp(−1607.2, 0, 100) = 0.0
  (Unlike the Balance Sheet sub-score above, this formula's clamp correctly handles the negative-ratio
   case — a deeply negative FCF/NI ratio is driven straight to the 0.0 floor as intended, no override
   needed.)

QUALITY SCORE = 34.8×0.25 + 85.5×0.15 + 100.0×0.20 + 0.0×0.15 + 20.0×0.15 + 0.0×0.10
             = 8.700 + 12.825 + 20.000 + 0.000 + 3.000 + 0.000
             = 44.525 → rounds to 44.5
```

**Quality Score = 44.5 / 100.0 — fails the 80.0+ gate by a wide margin on the weighted score alone, AND independently fails via two hard disqualifiers (FCF-positivity cleanly; Net Debt/EBITDA via the negative-EBITDA edge case). A more decisive multi-pronged failure than this framework's 2026-07-15 SNDK session (which failed on the weighted score plus a single hard disqualifier).**

**Gate result: FAIL.** Per quality-scoring.md, operating-brief.md, and this session's explicit instructions: **do not proceed to the Rate Environment Gate, Phase 02 valuation scoring, the Composite Score, or any order setup.**

---

## 4. Phase 02 / Order Setup — NOT PRODUCED

No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup is computed this session. The Quality Score gate is a strict, non-negotiable prerequisite and IREN clears neither the weighted-score threshold (44.5 vs. 80.0 required) nor either of two applicable hard-disqualifier checks.

---

## 5. Qualitative Notes

1. **The Telegram trigger's factual claims are all independently verified as accurate.** IREN genuinely hired Kambiz Aghili (ex-Oracle Cloud Infrastructure) and Michael Nudelman (ex-Google) into senior AI Cloud leadership roles (2 Jul 2026 press release), and genuinely has a disclosed, partnered 5 GW+ AI infrastructure buildout underway (NVIDIA partnership, ~5.8 GW total pipeline). This is a real, well-documented strategic pivot — not hype unsupported by primary sources.
2. **The pivot doesn't change today's Quality Score outcome.** Even crediting the genuine strategic momentum, IREN today is (a) still 89.8% a Bitcoin-mining-revenue business by the most recent 9-month segment data, (b) burning cash at an accelerating rate to fund the AI buildout (FY2025 FCF −$327.6M, and TTM FCF −$1,460.8M — a materially worse trailing-twelve-month figure than any full prior fiscal year), and (c) has taken on a rapidly growing, already-large debt load (~$4.0B of convertible notes and finance leases as of 31 Mar 2026, understated relative to the true current position given ~$3B+ raised/committed since) against currently-negative EBITDA.
3. **The reported net income figures materially overstate current profitability.** TTM net income (+$158.1M) and FY2025 net income (+$86.9M) are both substantially inflated by non-cash, non-operating mark-to-market gains on Prepaid Forward Contracts tied to IREN's own rapidly-rising share price (§2.7) — not by improving operating economics. TTM operating income remains deeply negative (−$408.4M). A reader relying on the reported "profitable" headline without this context would materially misjudge the business's current earnings quality.
4. **This is a decisive fail, not a marginal one.** Unlike SNDK's session (a single clean hard-disqualifier fire plus a below-threshold weighted score), IREN fails on the weighted score by a wide margin (44.5 vs. 80.0) AND fires two separate hard disqualifiers (one cleanly, one via a flagged formula edge-case that nonetheless reflects genuine balance-sheet weakness). The independently-reported ~$21.1B funding gap (Blocksbridge Consulting/VanEck, cited across multiple financial-press outlets) is external corroboration that this framework's own bottom-up finding (heavy, accelerating cash burn against a rapidly-growing debt load) is not an artifact of this session's specific calculation choices.
5. **The one genuinely encouraging signal — AI Cloud segment unit economics — is real but too small and too early to move today's score.** At 86.75% segment gross margin vs. 65.06% for Bitcoin mining (§2.6), the AI Cloud business's economics, if they scale, would be a meaningfully better business than the Bitcoin-mining base it's being built on top of. But at 10.2% of revenue with essentially one material contracted customer (Microsoft) and no multi-year track record, there isn't yet a documented, cited mechanism supporting a Moat Signal credit for it (§2.8), and it cannot offset three consecutive years of FCF-negative results in the hard-disqualifier check.
6. **Data gap disclosed, not invented around:** the balance sheet used in §2.5/§3 (as of 31 Mar 2026) is the most recent primary-sourced figure available, but it excludes a ~$3.0B convertible-note raise that closed in May 2026 and a ~$3.6B Microsoft-tied financing package still pending definitive documentation as of the 10-Q's filing date. This did not block completing the Quality Score (enough primary-sourced data existed for every sub-score), so per this session's instructions the evaluation proceeds to completion, but the true current leverage picture is understood to be materially worse than what's computed above — flagged explicitly rather than estimated.

---

## 6. Recommendation

# **PASS — Quality Score gate FAILS (44.5, well below the 80.0+ threshold) AND two hard disqualifiers independently fire (not FCF-positive for 3+ consecutive years; Net Debt/EBITDA effectively unbounded against negative TTM EBITDA). Do not proceed to valuation scoring. No position, no watchlist-only tracking recommendation beyond a monitoring pointer — this ticker does not clear the framework's first screening gate.**

IREN's strategic pivot from Bitcoin mining to vertically-integrated AI Cloud infrastructure is real, well-financed by contract (a genuine ~$9.7B, 5-year Microsoft agreement), and independently verified — the Telegram trigger's factual claims all check out. But the framework's Quality Score is explicitly designed to look through a story and at the numbers a business has actually produced: IREN fails the strict, non-negotiable 80.0+ gate on the weighted score alone (44.5, dragged down primarily by a deeply negative ROIC, a spuriously-computed-but-substantively-poor Balance Sheet sub-score, and a fully-saturated-at-zero FCF Quality sub-score), and it independently fails two of the three hard disqualifiers — three consecutive FCF-negative fiscal years with a widening (not narrowing) deficit, and a debt load that cannot be serviced from currently negative operating cash profitability. The one bright spot (AI Cloud segment unit economics) is real but still too small (10.2% of revenue) to move today's outcome. Per operating-brief.md and quality-scoring.md, **this stops the evaluation before Phase 02** — no Rate Environment Gate, no valuation score, no Composite Score, and no fair-value/order-setup work is produced.

---

## 7. Next Review Trigger

- **IREN's FY2026 10-K** (fiscal year ends 30 June 2026; expected ~August/September 2026 based on the FY2025 filing cadence) — the natural next checkpoint. It will be the first annual report to show a full year of AI Cloud revenue scaling post-Microsoft-contract, the true post-financing balance sheet (including the ~$3.0B May 2026 convertible-note raise and, if drawn, the ~$3.6B Microsoft-tied facility), and whether operating cash burn is narrowing or still widening.
- **The FCF-positivity hard disqualifier mechanically cannot clear before the FY2028 10-K** (the first year in which FY2026, FY2027, and FY2028 could all register FCF-positive) — a multi-year, not near-term, resolution path, contingent on the AI Cloud buildout reaching a self-funding scale.
- **Standard Rule 9 triggers**: guidance revision, a material new AI Cloud customer/contract announcement, execution (or abandonment) of the pending ~$3.6B Microsoft-tied delayed-draw financing, management change, a macro shift, or a >15% unexplained price move.
- **Segment-mix milestone worth tracking independent of a full re-score**: if/when AI Cloud Services revenue crosses roughly a third to a half of total revenue, the Growth and Moat sub-score qualitative reasoning in this session (currently anchored on a still-Bitcoin-mining-dominated revenue base) would need to be revisited even before the FY2026 10-K formally triggers a re-score.

---

## 8. Watchlist & Stale-Score Housekeeping

- **New watchlist entry created:** [watchlist/not-in-portfolio/IREN/IREN-2026-07-15.md](../watchlist/not-in-portfolio/IREN/IREN-2026-07-15.md) — first-ever entry for this ticker (Phase 01 FAIL).
- **Stale-score mechanism:** not applicable — IREN never previously had an entry, so there is nothing to clear from [watchlist/STALE.md](../watchlist/STALE.md).

---

## 9. Glossary

- **AI Cloud Services**: IREN's newer business segment — leasing GPU compute capacity in its data centers to AI customers (currently, primarily Microsoft) — as distinct from its legacy Bitcoin mining segment (§2.6).
- **ASIC (Application-Specific Integrated Circuit)**: a chip custom-designed for one specific task (existing glossary entry, cited for GPU/TPU examples) — a Bitcoin-mining ASIC is the same concept applied to the SHA-256 hashing task Bitcoin mining requires, the hardware underlying IREN's hash rate (§2.8).
- **Capped call transactions**: derivative transactions a company enters alongside a convertible-note offering to reduce potential share dilution upon conversion (existing glossary context, under "Convertible senior notes") — IREN has layered several such transactions (2029 through 2033 tranches) alongside its Convertible Notes.
- **CapEx**: Capital Expenditure — money spent buying or upgrading physical assets; central to this session's hard-disqualifier finding (§2.4, §3.1) given the scale of IREN's AI data-center buildout spend.
- **CIK (Central Index Key)**: the SEC's unique numeric filer identifier — IREN's is 0001878848.
- **CoinShares**: an independent digital-asset investment and research firm; its quarterly Bitcoin Mining Report is a third-party (non-company-sourced) citation basis for Moat Signal "market share" evidence in this framework, e.g. IREN's ~46 EH/s installed hash rate figure (§2.8). *(New term.)*
- **Composite Score**: this framework's blended 0.0–100.0 ranking (`0.50 × (100 − Quality Score) + 0.50 × Valuation Score`) — not computed this session, since IREN never clears the Quality Score gate required to reach it.
- **D&A**: Depreciation & Amortization.
- **EBIT / EBITDA**: Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — IREN's TTM EBITDA is negative (§2.3, §3.1).
- **EH/s (Exahash per second)**: a unit of Bitcoin mining hash rate (computational power dedicated to solving the network's proof-of-work puzzle) — one exahash equals 10^18 hashes per second. IREN operated ~36–46 EH/s as of early 2026, roughly 5–6% of the global Bitcoin network's total hash rate (§2.8). *(New term.)*
- **FCF / FCF Yield / FCF/NI conversion ratio**: Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check) — central to this session's hard-disqualifier finding (§3.1).
- **Foreign private issuer / Form 20-F**: the SEC status/filing type for a non-US company that hasn't elected domestic-filer status (existing glossary entry for Form 20-F) — IREN filed this way through FY2024 before converting to 10-K/10-Q domestic-filer status for FY2025 (§2.1).
- **Gross Margin**: Gross Profit ÷ Revenue — one of this framework's Quality Score Margins sub-score inputs; IREN's TTM figure is 68.4% (§3.2), though this blends two very different underlying segment margins (§2.6).
- **Hard disqualifier**: a Quality Score condition that fails a company regardless of its weighted score; IREN's session fires two of the three this session (§3.1) — a more severe outcome than this framework's typical single-disqualifier fail.
- **Invested Capital**: debt + equity − cash, the ROIC denominator.
- **Moat**: a durable competitive advantage protecting a business's profits from competitors — scored 20.0 (1 of 5 signals, itself flagged as weak) for IREN this session (§2.8).
- **NASDAQ**: the US stock exchange IREN trades on.
- **Net Debt/EBITDA**: this framework's primary balance-sheet-risk gate — undefined as a meaningful finite multiple for IREN this session, given negative trailing EBITDA (§3.1, §3.2).
- **Net Margin**: Net Income ÷ Revenue — IREN's TTM figure (20.88%) is heavily distorted by a one-off non-cash gain (§2.7); flagged, not corrected for, in the scored formula.
- **NOPAT**: Net Operating Profit After Tax — EBIT × (1 − effective tax rate); approximated directly by EBIT this session given a non-meaningful effective tax rate on negative pretax income (§3.2).
- **PP&E (Property, Plant & Equipment)**: physical long-lived business assets — IREN's PP&E purchases (CapEx) are the primary driver of its negative FCF (§2.4).
- **Prepaid Forward Contract**: an equity derivative in which a company prepays a financial-institution counterparty for the future delivery of its own shares (typically entered alongside a convertible-note issuance, to offset dilution similar in spirit to a capped call) — marked to fair value each period, so a rising share price produces a large unrealized (non-cash) accounting gain unrelated to operating performance. IREN's Prepaid Forward Contracts produced a $664.993M unrealized gain in Q1 FY2026 alone, the primary driver of that quarter's reported net income (§2.7). *(New term.)*
- **ROIC**: Return on Invested Capital — IREN's TTM figure is deeply negative (−9.26%, §3.2).
- **SEC EDGAR / XBRL**: the SEC's public filing database and the machine-readable financial-data format within it (existing glossary entries) — the primary data source for this session's income statement, cash flow, and balance sheet figures.
- **Segment (reportable segment)**: a distinct part of a company's business that management reports separately (e.g. IREN's Bitcoin mining and AI Cloud Services segments, §2.6) because it's evaluated separately internally.
- **TTM (Trailing Twelve Months)**: the most recent 12 months of reported financial results — reconstructed for IREN this session from FY2025 minus the 9-month comparative period ended 31 Mar 2025 plus the 9-month period ended 31 Mar 2026 (§2.3).

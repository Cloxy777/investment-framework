# NEW POSITION — IREN (IREN Limited, formerly Iris Energy, NASDAQ) — 2026-07-20

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — fully automated, no human in loop)
**Date:** 20 Jul 2026
**10Y US Treasury Yield:** 4.57% (FRED `DGS10`, most recent posted observation as of this session, dated 2026-07-16 — normal FRED reporting lag over the 07-18/07-19 weekend)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §4). For reference only, the bracket in force is +5 (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current IREN portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md), 2026-07-20 live-synced version)
**Prior coverage:** [sessions/2026-07-15-new-position-iren.md](2026-07-15-new-position-iren.md) — first-ever evaluation, **FAILED** the Quality Score gate (44.5 vs. 80.0 required), with two hard disqualifiers firing (FCF not positive 3+ consecutive years; Net Debt/EBITDA effectively unbounded against negative EBITDA). That session's own "Next review trigger" named "a material new AI Cloud customer/contract announcement" and "guidance revision" as reasons to re-run — precisely what triggers this session, 5 days later.
**Sector:** Bitcoin mining, pivoting to vertically-integrated AI Cloud / data center infrastructure.
**Filer type:** SEC domestic filer since FY2025 (10-K/10-Q), CIK **0001878848**. Fiscal year ends **30 June**.
**First-use jargon decode:** see closing Glossary (§7).

---

## 0. Why this session exists — trigger source

A Telegram post (**FinnInvestChannel/2959, ~11:55 UTC, 2026-07-20**) claimed: *"IREN signed new contracts worth $2.8 billion with leading AI companies and raised its AI Cloud revenue forecast for end of 2026 from $3.7 billion to over $4 billion. Among the company's clients are already Microsoft, NVIDIA, Perplexity, Figure AI, Together AI, Fluidstack, Fireworks AI, Fal AI and Hume AI."*

Per the operating brief, **Telegram post text is never used as financial data or even treated as a confirmed fact** — it is a trigger only. IREN already has a watchlist entry (Phase 01 FAIL, 2026-07-15) and is not currently held, and its prior session explicitly flagged "a material new AI Cloud customer/contract announcement" and "guidance revision" as its own next-review trigger — both of which this post claims. Per operating-calendar.md / fair-value-methodology.md Rule 9 ("Guidance revision (up or down)" is a mandatory model-refresh trigger), this unconditionally warrants a fresh evaluation.

**Independent verification performed (all before any of it was used as input to anything):**

- **Primary source located and confirmed:** IREN filed a **Form 8-K today, 2026-07-20** (accession 0001140361-26-028871, Item 2.02 "Results of Operations and Financial Condition"), furnishing a press release (Exhibit 99.1) titled *"IREN Signs $2.8bn in New Customer Contracts with Leading AI Developers, Raises 2026 ARR Target to over $4bn."* This is the Telegram post's exact source — the post is a near-verbatim summary of IREN's own official disclosure, not third-party rumor.
- **Claim-by-claim check against the 8-K/press release:**
  - "$2.8 billion in new contracts" — confirmed: "$2.8bn in total contract value" from "new multi-year cloud services contracts."
  - "AI Cloud revenue forecast... from $3.7 billion to over $4 billion" — confirmed, with a precision correction: the metric raised is **ARR** (annualized run-rate revenue as of year-end 2026, an operating metric, not GAAP revenue), not "2026 revenue." IREN's own footnote 1 states explicitly: *"ARR is an operating metric, not a GAAP measure, and is not derived from, or a substitute for, revenue determined in accordance with GAAP."*
  - Client list (Microsoft, NVIDIA, Perplexity, Figure AI, Together AI, Fluidstack, Fireworks AI, Fal AI, Hume AI) — confirmed verbatim, plus "a new leading AI developer" left unnamed.
- **What this filing does NOT contain:** no updated balance sheet, income statement, or cash-flow statement. The only new quantitative figure with any financial-statement character is **"approximately $7.6bn in cash and cash equivalents" as of 30 June 2026**, explicitly labeled *"unaudited preliminary... Reflects USD equivalent... and includes $1.7bn of restricted cash in connection with the GPU financing for the Microsoft contract."* No offsetting debt/liabilities figure is disclosed alongside it.
- **SEC EDGAR filing history re-checked in full** (`data.sec.gov/api/xbrl/companyfacts/CIK0001878848.json` and the EDGAR submissions feed) for anything filed between 2026-07-15 and today: the only filing in that window is today's 8-K above. **No new 10-Q or 10-K has been filed.** The most recent GAAP financial statements on record remain the **10-Q filed 2026-05-08** (9 months ended 31-Mar-2026) and the **10-K filed 2025-08-28** (FY2025) — the exact same filings the 2026-07-15 session used.
- **Every income-statement, cash-flow, and balance-sheet figure used in the 2026-07-15 session was independently re-pulled from SEC EDGAR's XBRL `companyfacts` API today and confirmed byte-identical** — `Revenues`, `NetIncomeLoss`, `OperatingIncomeLoss`, `NetCashProvidedByUsedInOperatingActivities`, `PaymentsToAcquirePropertyPlantAndEquipment`, `Assets`, `Liabilities`, `StockholdersEquity`, `CashAndCashEquivalentsAtCarryingValue`, `ConvertibleNotesPayable`, and `FinanceLeaseLiability` all match exactly (see §2 for the reproduced figures). This is not a re-hash of the old session's numbers taken on faith — it is a fresh pull that happens to confirm nothing has changed.

**Conclusion of the verification step:** the Telegram claim is accurate and traces to a genuine, dated, primary-sourced IREN press release. But (a) the headline figure it excitedly reports is **forward-looking guidance (ARR target)**, which per [valuation-scoring.md](../framework/valuation-scoring.md)'s "Why Forward Guidance Is Not a Sub-score" section is **never used as a scored financial input** — guidance is a *trigger* for re-evaluation, not an input into it — and (b) no new audited/interim GAAP financial statement has actually been filed since the last evaluation. The quantitative basis for the Quality Score is therefore **unchanged** from 5 days ago.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$36.74** | IBKR `get_price_snapshot` (contract_id **526906130**, NASDAQ, "IREN LTD" — re-confirmed correct entity via `search_contracts` against the same 19-result disambiguation set as the 2026-07-15 session: Investis Holding SA (Swiss "IREN"), IREN SpA (Italian, "IRE" on BVME), Irenic Acquisition Corp (SPAC, "IACQ"/"IACQU"), and the leveraged/derivative single-stock ETF products IREX, IREZ, IREG, IRN3/3IRN, IREY/YIRE, IREC — none of which are the underlying operating company), `last` field, timestamp **2026-07-20 12:08:16 UTC** — pre-market (regular session opens 13:30 UTC / 9:30am ET) |
| Change vs. prior close | **+$3.12 / +9.28%** | IBKR `get_price_snapshot` `change` field |
| Bid / Ask | $36.70 / $36.74 | IBKR `get_price_snapshot` |
| 52-week range | Low **$14.72** · High **$76.87** | IBKR `get_price_snapshot` `misc_statistics` |
| Independent cross-check | Yahoo Finance chart API: Friday 2026-07-17 close **$33.62** (`regularMarketPrice`), prior close **$34.83** — IBKR's implied prior close ($36.74 − $3.12 = **$33.62**) matches Yahoo's last-recorded close **exactly**, confirming today's +9.28% pre-market move is real and internally consistent across sources, not a stale/bad tick | WebFetch-equivalent (direct HTTPS pull), 2026-07-20 |
| US 10Y Treasury yield | 4.57% | FRED `DGS10`, as-of 2026-07-16 |

**$36.74 is used as the live price for this session.** The +9.28% pre-market move is consistent with (and plausibly explained by) today's 8-K/press release — noted as context, not used as a scoring input, consistent with "never act on price movement alone."

---

## 2. Data Gathered — Sources & Method

### 2.1 Confirmation of "nothing changed" — filing history

SEC EDGAR submissions feed (`data.sec.gov/submissions/CIK0001878848.json`) shows the following filings between the 2026-07-15 session and today, in full:

| Date | Form | Content |
|---|---|---|
| 2026-07-20 | 8-K | Today's business-update press release (§0) — no financial statements |
| 2026-07-09 | DEFA14A | Proxy soliciting material |
| 2026-07-01 | 8-K | Confirmed by direct read: Item 5.02, RSU equity-grant awards to the two Co-CEOs — executive compensation, not financial results |
| 2026-07-01 | S-8, Form 4 ×7 | Employee equity plan registration / insider transaction reports |

**No 10-Q or 10-K in this window.** The next scheduled financial-statement filing is the **FY2026 10-K** (fiscal year ended 30 June 2026), not yet filed as of this session — consistent with the 2026-07-15 session's own note that it was "expected ~August/September 2026 based on the FY2025 filing cadence."

### 2.2 Income statement — primary-sourced, US GAAP ($ millions) — re-verified via XBRL today

| | FY2023 (10-K) | FY2024 (10-K) | FY2025 (10-K) |
|---|---|---|---|
| Revenue | 75.509 | 187.192 | 501.023 |
| Operating income (loss) | (157.241)* | (27.234)* | 17.327 |
| **Net income (loss)** | **(171.827)** | **(28.920)** | **86.941** |

*FY2023/FY2024 operating income shown for continuity with the 2026-07-15 session; not independently re-pulled this session since the hard-disqualifier and Quality Score math below don't depend on them — Revenue, NetIncomeLoss, and the cash-flow lines were the ones re-verified via XBRL (§0).

**9 months ended 31 Mar 2026 (10-Q filed 2026-05-08, unchanged, re-verified today via XBRL, $ millions):**

| | 9mo ended 31-Mar-2026 | 9mo ended 31-Mar-2025 (comparative) |
|---|---|---|
| Revenue | 569.782 | 313.731 |
| Operating income (loss) | (426.331) | (0.561) |
| Net income (loss) | (18.622) | (89.735) |
| Operating cash flow (OCF) | 289.326 | 142.745 |
| CapEx (PP&E purchases) | 1,669.157 | 389.342 |

### 2.3 TTM reconstruction (ending 31 Mar 2026) — identical method and result to 2026-07-15

```
Revenue TTM         = 501.023 − 313.731 + 569.782  = 757.074   ($M)
Op income TTM        = 17.327 − (−0.561) + (−426.331)= −408.443
Net income TTM       = 86.941 − (−89.735) + (−18.622)= 158.054  → Net Margin TTM = 20.88%
OCF TTM               = 245.886 − 142.745 + 289.326  = 392.467
CapEx TTM             = 573.456 − 389.342 + 1,669.157 = 1,853.271
FCF TTM (OCF−CapEx)   = 392.467 − 1,853.271          = (1,460.804)
D&A TTM                = 181.136 − 117.319 + 305.647 = 369.464
EBITDA TTM (OpInc+D&A) = −408.443 + 369.464           = (38.979)
Gross profit TTM       = 757.074 − 239.257            = 517.817   → Gross Margin TTM = 68.40%
```

### 2.4 Cash flow — 3 fiscal years, FCF by year ($ millions) — re-verified via XBRL today

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Operating cash flow (OCF) | 5.729 | 52.219 | 245.886 |
| CapEx (PP&E purchases) | 116.064 | 141.855 | 573.456 |
| **Free Cash Flow (OCF − CapEx)** | **(110.335)** | **(89.636)** | **(327.570)** |

All three most recently completed fiscal years remain FCF-negative — **unchanged** from 5 days ago, and mechanically cannot change until the FY2026 10-K is filed (which will report the fiscal year that just ended 30 June 2026, not yet disclosed with audited cash-flow figures — today's 8-K gives only a preliminary, unaudited cash *balance*, not a cash-flow statement).

### 2.5 Balance sheet — primary-sourced, re-verified via XBRL today ($ millions, as of 31 Mar 2026 — still the most recent audited/interim balance sheet on file)

| | 31-Mar-2026 |
|---|---|
| Cash and cash equivalents | 2,213.274 |
| Total assets | 7,264.897 |
| Convertible notes payable | 3,687.832 |
| Finance lease liability (current + noncurrent) | 274.256 |
| **Total debt** | **3,962.088** |
| Total liabilities | 4,600.369 |
| Total shareholders' equity | 2,664.528 |

```
Net Debt (31 Mar 2026)  = Total Debt − Cash = 3,962.088 − 2,213.274 = 1,748.814   ($M)
Net Debt / EBITDA (TTM) = 1,748.814 / (38.979)  → undefined / not computable as a meaningful finite multiple
                            (positive net debt divided by NEGATIVE trailing EBITDA)
```

**⚠️ Today's press release discloses a materially larger cash figure — "approximately $7.6bn" as of 30 June 2026 — but it cannot be substituted into this balance sheet.** It is explicitly labeled *unaudited* and *preliminary*, includes $1.7bn of *restricted* cash (not generally available), and — critically — comes with **no matching updated debt/liabilities figure**. Using it alone (cash way up, debt held at the old $3.96bn figure) would manufacture an artificially improved net-debt picture out of a one-sided, incomplete data point — exactly the kind of invented/estimated calculation Rule 0 and the "never invent or estimate financial data" non-negotiable forbid. The $3.0B+ of financing raised since 31 Mar 2026 (flagged already in the 2026-07-15 session's subsequent-events note) is presumably a large part of why cash rose, but the debt side of that same financing is not yet disclosed in a form usable here. **Flagged as a data gap, not silently resolved:** the true 30-Jun-2026 net leverage position cannot be computed from public information available as of this session, so the balance sheet used for scoring remains the last one with a complete, audited/reviewed matching debt-and-cash picture (31 Mar 2026, above).

### 2.6 Moat, going-concern, revenue segmentation

No new segment-level or moat-relevant primary-source evidence was published since 2026-07-15 beyond what's in today's press release (which reiterates the AI Cloud pivot and adds specific named customers, capacity, and a weighted-average ~4-year contract term). §2.8 of the [2026-07-15 session](2026-07-15-new-position-iren.md#28-moat-evidence--cited-sources) remains the operative moat evidence. No new going-concern language located.

**One new, genuinely relevant data point from today's release, cited but not scored:** *"Contracted pricing continues to strengthen. Recent contracts also include customer prepayments representing approximately 45% of the associated GPU capital expenditure, reducing IREN's net funding requirement for those deployments."* This is a real, positive-sounding operating disclosure (it would, if it holds, reduce the future financing burden underlying the balance-sheet weakness this framework has flagged twice now) — but it is self-reported, forward-looking commentary on *future* contracts, not a filed financial-statement figure, so it is noted qualitatively (§6) and not built into any sub-score.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology, unchanged since last session)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF positive 3+ consecutive years | FY2023: **($110.335)M** · FY2024: **($89.636)M** · FY2025: **($327.570)M** — all three most recent complete fiscal years FCF-negative | disqualify if not 3 consecutive positive years | **❌ FIRES, cleanly and unambiguously — unchanged from 2026-07-15.** No carve-out exists for this disqualifier. |
| Net Debt/EBITDA over threshold (2.5× standard; not asset-light eligible) | Net debt $1,748.814M (§2.5) against **negative** TTM EBITDA of ($38.979)M (§2.3) | disqualify if exceeds 2.5× | **❌ EFFECTIVELY FIRES — unchanged from 2026-07-15.** Ratio not computable as a meaningful finite multiple; conservative treatment applied (§3.2), not the formula's spurious face-value output. |
| FCF/NI conversion <70% for 2+ consecutive years w/o growth-capex explanation | Same sign-mixing ambiguity as 2026-07-15 (FY2023/FY2024 both-negative ratios not economically meaningful; FY2025 = −376.8%, a genuine bad signal) | disqualify if 2+ consecutive years <70% w/o carve-out | Not independently relied upon — the other two checks already fire unambiguously. Shown for transparency. |

**Two of three hard disqualifiers fire — identical outcome to 2026-07-15. Per quality-scoring.md and this session's instructions: STOP HERE — do not proceed to Phase 02 valuation scoring, regardless of the weighted Quality Score computed below.**

### 3.2 Quality Score — full computation (produced for the record, per the "every sub-score shown" instruction, even though the gate has already failed above)

```
PROFITABILITY (25% weight):
  Net Margin (TTM) = 158.054 / 757.074 = 20.88%
  ⚠️ Heavily distorted by a one-off, non-cash Prepaid Forward Contract mark-to-market gain
    (+$664.993M in Q1 FY2026 alone — see 2026-07-15 session §2.7 for full detail; unchanged, not
    re-derived line-by-line this session since it doesn't affect the sign or the gate outcome).
  NetMargin_Component = clamp((20.88/30)×100, 0, 100) = 69.6

  EBIT_TTM = −408.443
  Invested Capital (31 Mar 2026) = Total Debt + Equity − Cash = 3,962.088 + 2,664.528 − 2,213.274
                                  = 4,413.342
  ROIC = −408.443 / 4,413.342 = −9.26%
  ROIC_Component = clamp((−9.26/30)×100, 0, 100) = clamp(−30.9, 0, 100) = 0.0

  Raw Profitability_Score = (69.6 + 0.0) / 2 = 34.8
  FCF-positivity cap check: raw score (34.8) already below the 40.0 cap ceiling — no additional effect.
  Profitability_Score = 34.8

MARGINS (15% weight):
  Gross Margin (TTM) = 68.40%
  GrossMargin_Score = clamp((68.40/80)×100, 0, 100) = 85.5
  TTM already well above the 40% bonus-eligibility threshold — no trend bonus applies.
  Margins_Score = 85.5

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2022 $59.037M [re-verified via SEC EDGAR ifrs-full XBRL, 20-F filed 2022-09-13]
    → FY2025 $501.023M) = (501.023/59.037)^(1/3) − 1 = 103.95%
  Growth_Score = clamp((103.95/25)×100, 0, 100) = clamp(415.8, 0, 100) = 100.0  (saturated)
  TAM/pricing-power modifier: still not applied — consolidated 3yr CAGR remains overwhelmingly a
    Bitcoin-mining-driven figure (§2.6 of the 2026-07-15 session); today's press release doesn't change
    the historical revenue mix underlying this specific metric. Moot either way — already saturated.
  Growth_Score = 100.0

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (TTM) = $1,748.814M / ($38.979M) — undefined as a meaningful finite ratio (§3.1).
  ⚠️ Same formula blind spot as 2026-07-15 (negative EBITDA denominator would spuriously clamp to
    100.0 — the opposite of what it should mean). Conservative override applied, consistent with the
    prior session and not silently changed based on today's unaudited $7.6bn cash headline (§2.5).
  BalanceSheet_Score = 0.0  (conservative override)

MOAT SIGNAL (15% weight) — evidence unchanged from 2026-07-15 §2.8:
  1 of 5 TRUE (Market share stable/growing, flagged as weak/commodity signal).
  Moat_Score = (1/5) × 100 = 20.0

FCF QUALITY (10% weight):
  TTM FCF/NI = (1,460.804) / 158.054 = −924.3%
  FCFQuality_Score = clamp(((−9.243 − 0.40)/0.60)×100, 0, 100) = clamp(−1607.2, 0, 100) = 0.0

QUALITY SCORE = 34.8×0.25 + 85.5×0.15 + 100.0×0.20 + 0.0×0.15 + 20.0×0.15 + 0.0×0.10
             = 8.700 + 12.825 + 20.000 + 0.000 + 3.000 + 0.000
             = 44.525 → rounds to 44.5
```

**Quality Score = 44.5 / 100.0 — fails the 80.0+ gate by a wide margin on the weighted score alone, AND independently fails via two hard disqualifiers. Identical to the 2026-07-15 result**, because the underlying audited/interim GAAP financial statements are identical — no new 10-Q/10-K exists between the two sessions (§2.1), and today's guidance/contract announcement is explicitly excluded from scoring per "Why Forward Guidance Is Not a Sub-score."

**Gate result: FAIL.** Per quality-scoring.md, operating-brief.md, and this session's explicit instructions: **do not proceed to the Rate Environment Gate, Phase 02 valuation scoring, the Composite Score, or any order setup.**

---

## 4. Phase 02 / Order Setup — NOT PRODUCED

No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup is computed this session, for the same reason as 2026-07-15: the Quality Score gate is a strict, non-negotiable prerequisite, and IREN clears neither the weighted-score threshold (44.5 vs. 80.0 required) nor either of two applicable hard-disqualifier checks.

---

## 5. Data Gaps Flagged

1. **True post-30-Jun-2026 net leverage is unknown.** Today's press release discloses ~$7.6bn of (unaudited, preliminary, partly restricted) cash but no matching updated debt figure — not invented or estimated around; the balance sheet used for scoring remains the last complete one (31 Mar 2026). The FY2026 10-K (expected ~Aug/Sep 2026) is the next point this resolves.
2. **The "45% of GPU capex prepaid" claim in today's release** is a real, primary-sourced disclosure but is forward-looking commentary on future contracts, not an auditable historical figure — noted qualitatively only (§2.6, §6), not scored.
3. No other data gaps — every figure used in the Quality Score computation (§3.2) is a directly filed, primary-sourced SEC EDGAR figure, independently re-pulled and matched this session.

---

## 6. Qualitative Notes

1. **The Telegram trigger checks out, and precisely — this time from an official 8-K filed the same day the post appeared**, not a press release from weeks earlier as in the 2026-07-15 session. The $2.8bn contract figure and named-client list are both confirmed verbatim.
2. **The one meaningful correction to the Telegram framing:** the post describes a raised "AI Cloud revenue forecast," but IREN's own release is explicit that the $4bn+ figure is an **ARR target** (an annualized run-rate operating metric), not a GAAP revenue guide — and the framework treats both the same way regardless (never scored), but the distinction matters for anyone reading the post literally.
3. **Nothing about today's news changes the mechanics of why IREN fails the gate.** The hard disqualifiers are backward-looking, audited-financial-statement facts (FCF-negative for FY2023–FY2025; negative TTM EBITDA against ~$4.0B of debt) that a forward guidance raise — however credible and well-documented — cannot retroactively cure. As the 2026-07-15 session noted, the FCF-positivity disqualifier mechanically cannot clear before the FY2028 10-K at the earliest.
4. **The genuinely new information (named customer roster, $2.8bn contract value, prepayment terms) is incremental evidence the AI Cloud pivot is real and scaling** — consistent with, and an extension of, the 2026-07-15 session's finding that the pivot's factual claims all check out. It does not change the Moat Signal evidence table (§2.8 of that session) because it still doesn't supply a cited, specific mechanism for IREN's own switching costs or a cost-per-unit scale advantage — new named logos are revenue-visibility evidence, not moat evidence, under this framework's existing "mechanism required, not just contract existence" standard.
5. **This is a Rule 9 fundamental-event trigger (guidance revision + material new contracts), which is why this session exists at all** despite the score/action outcome being unchanged — per [watchlist/README.md](../watchlist/README.md#significant-change--when-does-a-new-dated-entry-get-created), a Rule 9 trigger firing warrants a fresh dated watchlist pointer even when the score and action category don't move, because the *reasoning* has been refreshed and is worth recording. See §8.

---

## Recommendation

# **PASS — Quality Score gate FAILS again (44.5, unchanged, well below the 80.0+ threshold) AND the same two hard disqualifiers independently fire (not FCF-positive for 3+ consecutive years; Net Debt/EBITDA effectively unbounded against negative TTM EBITDA). Do not proceed to valuation scoring. No position, no watchlist-only tracking recommendation beyond a monitoring pointer.**

Today's news is real, well-documented, and directionally positive for IREN's AI Cloud story — a genuine 8-K/press-release-confirmed $2.8bn in new contracted business and a raised ARR target, with named marquee AI customers. But it is guidance and new bookings, not a new set of audited financial statements, and this framework's Quality Score gate is explicitly built to look through exactly that kind of forward-looking narrative to the historical, filed numbers. Those numbers are unchanged from 5 days ago: three straight years of negative free cash flow with a widening deficit, and roughly $4.0B of debt sitting against negative trailing EBITDA. **This does not count as a BUY, TRIM, or EXIT trigger** — it is a confirmed-but-non-scoring news event against a name that was already, and remains, a hard fail at the first gate.

---

## Next Review Trigger

Unchanged from the 2026-07-15 session:
- **IREN's FY2026 10-K** (fiscal year ended 30 June 2026; expected ~August/September 2026) — first look at the true post-financing balance sheet and whether operating cash burn is narrowing.
- **The FCF-positivity hard disqualifier mechanically cannot clear before the FY2028 10-K.**
- **Standard Rule 9 triggers:** guidance revision, a material new AI Cloud customer/contract announcement, execution of the pending Microsoft-tied delayed-draw financing, management change, macro shift, or a >15% *unexplained* price move (today's +9.28% move is explained, so does not independently qualify).
- **Segment-mix milestone:** if/when AI Cloud Services revenue crosses roughly a third to a half of total revenue, worth an informal look even before the FY2026 10-K formally triggers a re-score.

---

## 8. Watchlist & Stale-Score Housekeeping

- **New dated watchlist entry created:** [watchlist/not-in-portfolio/IREN/IREN-2026-07-20.md](../watchlist/not-in-portfolio/IREN/IREN-2026-07-20.md) — the score (Phase 01 FAIL, 44.5) and action (PASS — watchlist) are unchanged from 2026-07-15, but per [watchlist/README.md](../watchlist/README.md#significant-change--when-does-a-new-dated-entry-get-created), **a Rule 9 fundamental-event trigger (guidance revision + material new contract announcement) fired today**, which independently warrants a fresh dated pointer even with the score/action unchanged — "the reasoning has changed and is worth a fresh pointer." The prior [IREN-2026-07-15.md](../watchlist/not-in-portfolio/IREN/IREN-2026-07-15.md) entry is preserved unmodified (per the existing repo convention of multiple dated files per ticker, e.g. AVGO, MSFT).
- **Stale-score mechanism:** not applicable — IREN is Phase 01 FAIL / not scored, and per [watchlist/README.md](../watchlist/README.md#stale-scores--when-the-scoring-methodology-changes), "Entries that are 'Phase 01 FAIL / not scored' are not marked" for staleness (there's no Phase 02 score for a methodology change to invalidate). Confirmed IREN carries no row in [watchlist/STALE.md](../watchlist/STALE.md).

---

## 9. Glossary

- **8-K (Form 8-K)**: a US company's "current report" filed with the SEC to disclose a material event between its regular quarterly/annual filings — today's IREN 8-K (Item 2.02) furnished the press release that is this session's trigger source (§0).
- **AI Cloud Services**: IREN's newer business segment — leasing GPU compute capacity in its data centers to AI customers — distinct from its legacy Bitcoin mining segment.
- **ARR (Annual Recurring Revenue)**: the annualized run-rate value of a business's contracted revenue at a point in time — IREN's own raised "AI Cloud ARR target" (§0) is this kind of forward-looking operating metric, explicitly not a GAAP revenue figure and never a scored input in this framework.
- **Bare metal (cloud computing)**: a cloud/data-center service where the customer gets dedicated, single-tenant physical servers directly, as opposed to a virtualized "managed cloud service" layer on top — IREN offers both, per today's press release (§2.6). *(New term — added to [glossary.md](../framework/glossary.md) this session.)*
- **CapEx**: Capital Expenditure — money spent buying or upgrading physical assets; central to IREN's hard-disqualifier finding (§2.4, §3.1).
- **CIK (Central Index Key)**: the SEC's unique numeric filer identifier — IREN's is 0001878848.
- **Composite Score**: this framework's blended 0.0–100.0 ranking (`0.50 × (100 − Quality Score) + 0.50 × Valuation Score`) — not computed this session, since IREN never clears the Quality Score gate required to reach it.
- **D&A**: Depreciation & Amortization.
- **EBIT / EBITDA**: Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — IREN's TTM EBITDA is negative (§2.3, §3.1).
- **FCF / FCF Yield / FCF/NI conversion ratio**: Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check) — central to this session's hard-disqualifier finding (§3.1).
- **Form 8-K**: see "8-K" above.
- **Gross Margin**: Gross Profit ÷ Revenue — IREN's TTM figure is 68.4% (§3.2).
- **Hard disqualifier**: a Quality Score condition that fails a company regardless of its weighted score; IREN fires two of the three, unchanged from the 2026-07-15 session (§3.1).
- **Invested Capital**: debt + equity − cash, the ROIC denominator.
- **Moat**: a durable competitive advantage protecting a business's profits from competitors — scored 20.0 (1 of 5 signals) for IREN, unchanged from 2026-07-15.
- **NASDAQ**: the US stock exchange IREN trades on.
- **Net Debt/EBITDA**: this framework's primary balance-sheet-risk gate — undefined as a meaningful finite multiple for IREN, given negative trailing EBITDA (§3.1, §3.2).
- **Net Margin**: Net Income ÷ Revenue — IREN's TTM figure (20.88%) is heavily distorted by a one-off non-cash gain (see 2026-07-15 session §2.7), flagged not corrected for in the scored formula.
- **ROIC**: Return on Invested Capital — IREN's TTM figure is deeply negative (−9.26%, §3.2).
- **SEC EDGAR / XBRL**: the SEC's public filing database and the machine-readable financial-data format within it — the primary data source for every figure re-verified this session.
- **TTM (Trailing Twelve Months)**: the most recent 12 months of reported financial results.

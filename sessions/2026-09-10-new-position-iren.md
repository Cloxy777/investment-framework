# NEW POSITION — IREN (IREN Limited, formerly Iris Energy, NASDAQ) — 2026-09-10

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — fully automated, no human in loop)
**Date:** 10 Sep 2026
**10Y US Treasury Yield:** 4.80% (FRED `DGS10`, most recent posted observation, dated 2026-09-08 — 2026-09-09 not yet posted as of this session, normal FRED reporting lag, same pattern noted in the 2026-07-20 session)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §4). For reference only, the bracket in force is +5 (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current IREN portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** [sessions/2026-07-15-new-position-iren.md](2026-07-15-new-position-iren.md) (first evaluation, Quality Score 44.5, FAIL) and [sessions/2026-07-20-new-position-iren.md](2026-07-20-new-position-iren.md) (Rule 9 re-check, Quality Score 44.5 unchanged, FAIL). Both sessions' "Next review trigger" named IREN's FY2026 10-K (fiscal year ended 30 June 2026, expected ~Aug/Sept 2026) as the next scheduled re-score point — this session exists because that 10-K has now been filed, **and** because of a fresh Telegram-flagged news item.
**Sector:** Bitcoin mining, pivoting to vertically-integrated AI Cloud / data center infrastructure.
**Filer type:** SEC domestic filer since FY2025 (10-K/10-Q), CIK **0001878848**. Fiscal year ends **30 June**.
**First-use jargon decode:** see closing Glossary (§9).

---

## 0. Why this session exists — trigger source

A Telegram post (**FinnInvestChannel/3199, 2026-09-10 11:57 UTC**) claimed: *"Nvidia plans to deploy up to 2 GW of AI infrastructure in Australia by 2027, collaborating with firms like Firmus and IREN. The company will provide chips, networking equipment, and software, along with guidance on building AI clusters. IREN intends to apply this framework across its data centers, including the 800 MW Bundey campus in South Australia."*

Per the operating brief, Telegram post text is never used as financial data or trusted at face value — it is a trigger only. Two independent things make this session warranted regardless of how the Telegram claim checks out: (1) both prior IREN sessions explicitly flagged the FY2026 10-K as the next scheduled re-score trigger, and it has now been filed (§1.1 below); (2) fair-value-methodology.md Rule 9 treats "material M&A announcement" / new infrastructure-partnership news as a mandatory model-refresh trigger, which is exactly what this post claims.

**Independent verification performed (before any of it was used as input to anything):**

- **SEC EDGAR filing history re-checked in full** (`data.sec.gov/submissions/CIK0001878848.json`, cross-checked against `browse-edgar`) for everything filed since the 2026-07-20 session. Result: IREN filed its **FY2026 Form 10-K on 2026-08-27** (accession 0001878848-26-000052, period ended 2026-06-30) — the trigger both prior sessions were waiting on. Also filed in the window: four more 8-Ks (2026-08-03, 08-04, 08-13, 08-27) and a Form D (2026-08-18, exempt-offering notice, not examined further — not needed for the scored figures). **No IREN-specific 8-K exists yet for the specific Nvidia/Firmus/Australia announcement named in today's Telegram post** — the most recent EDGAR filing of any kind for CIK 0001878848 remains 2026-08-27, twelve days before this Telegram post.
- **The Nvidia/Firmus/Australia claim was independently corroborated anyway, through a different primary source.** It traces to **NVIDIA's own newsroom press release**, "*NVIDIA Expands AI Infrastructure Capacity in Partnership With Australia's Data Center Ecosystem*," dated **2026-09-09** (`nvidianews.nvidia.com`), also distributed via GlobeNewswire and independently reported by multiple outlets (TheNextWeb, SMBtech, Australian Manufacturing, Manila Times, crypto.news, StockTitan) — a genuine, dated, multi-source-corroborated announcement, not a rumor. Claim-by-claim check:
  - "Up to 2 GW of AI infrastructure in Australia by 2027" — **confirmed**, NVIDIA's own figure.
  - "Collaborating with firms like Firmus and IREN" — **confirmed**: 8 named Australian partners (Firmus, Sharon AI, IREN, Megaport, ResetData, CDC, NEXTDC, AirTrunk); NVIDIA delivers the **DSX** platform (compute, networking, software, reference architecture — see Glossary), the partners build/operate the physical "AI factory" sites.
  - "IREN intends to apply this framework across its data centers, including the 800 MW Bundey campus in South Australia" — **confirmed and independently double-sourced**: NVIDIA's release quotes IREN's blueprint language, and separately, IREN's own FY2026 10-K (filed 2026-08-27, *before* this NVIDIA release) already lists "Bundey, South Australia, Australia | 800MW" in its data-center capacity table (§2.6) — so the campus's existence and size is confirmed by IREN's own audited filing, independent of the NVIDIA press release or the Telegram post.
  - No dollar figures or contract terms are disclosed in NVIDIA's release for the Australia buildout specifically.
- **Conclusion of the verification step:** the Telegram claim is accurate and well-corroborated (NVIDIA primary source + IREN's own 10-K capacity table + multiple independent news outlets), but it is an **operational/capacity-partnership announcement** — not a financial statement, not GAAP data, and not scored regardless of how credible it is (see "Why Forward Guidance Is Not a Sub-score," valuation-scoring.md). It is treated here exactly like the 2026-07-20 session treated the AI-customer-contract news: real, cited, qualitatively noted (§6), not built into any sub-score.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$44.25** | IBKR `get_price_snapshot` (contract_id **526906130**, NASDAQ, "IREN LTD" — re-confirmed correct entity via `search_contracts` against the same 19-result disambiguation set used in both prior sessions: Investis Holding SA [Swiss "IREN"], IREN SpA [Italian, "IRE" on BVME], Irenic Acquisition Corp [SPAC, "IACQ"/"IACQU"], and leveraged/derivative single-stock ETF products IREX, IREZ, IREG, IRN3/3IRN, IREY/YIRE, IREC — none of which are the underlying operating company), `last` field, timestamp **2026-09-10 12:19:58 UTC** |
| Change vs. prior close | **−$1.12 / −2.47%** | IBKR `get_price_snapshot` `change` field (prior close derived: $44.25 − (−$1.12) = $45.37; the snapshot's own `prior_close` field returned empty this call) |
| Bid / Ask | $44.18 / $44.28 | IBKR `get_price_snapshot` |
| 52-week range | Low **$28.93** · High **$76.87** | IBKR `get_price_snapshot` `misc_statistics` (13w high $63.17, 26w high $70.71, 26w low $28.93) |
| US 10Y Treasury yield | 4.80% | FRED `DGS10`, as-of 2026-09-08 |

**$44.25 is used as the live price for this session.** Today's −2.47% move is small and unremarkable — well short of the >15% "unexplained move" Rule 9 trigger — and is noted as context only, consistent with "never act on price movement alone."

---

## 2. Data Gathered — Sources & Method

### 2.1 The FY2026 10-K — primary trigger for this session

IREN filed its **Form 10-K for fiscal year ended 30 June 2026 on 2026-08-27** (accession 0001878848-26-000052, main document `iren-20260630.htm`), audited by KPMG. This is the first full-year audited financial statement since the FY2025 10-K (filed 2025-08-28) that both prior sessions were working from — it supersedes the 9-months-ended-31-Mar-2026 10-Q TTM reconstruction used in the 2026-07-15 and 2026-07-20 sessions with actual, complete, audited FY2026 figures. All figures below are pulled directly from SEC EDGAR's XBRL `companyfacts` API (`data.sec.gov/api/xbrl/companyfacts/CIK0001878848.json`), cross-checked against the 10-K's own business-description text.

### 2.2 Income statement — primary-sourced, US GAAP ($ millions)

| | FY2024 (10-K) | FY2025 (10-K) | **FY2026 (10-K, new)** |
|---|---|---|---|
| Revenue | 187.192 | 501.023 | **707.007** |
| Cost of revenue | 87.067 | 158.992 | **219.706** |
| Gross profit | 100.125 | 342.031 | **487.301** |
| Operating income (loss) | (27.234) | 17.327 | **(1,046.714)** |
| **Net income (loss)** | **(28.920)** | **86.941** | **(702.621)** |
| Depreciation & amortization | 50.470 | 181.136 | **417.729** |
| EPS, diluted | (0.29) | 0.39 | **(2.22)** |
| Weighted avg. diluted shares (M) | 99.641 | ~223 (implied) | **~316.1** |
| Interest expense on debt | 0.000 | 10.453 | **46.574** |
| Share-based compensation | 23.636 | 42.642 | **205.023** |

FY2025's positive net income was flagged in the prior two sessions as heavily distorted by a one-off $665M non-cash Prepaid Forward Contract mark-to-market gain. FY2026 flips to a **$702.6M net loss** despite revenue growth — this is the AI Cloud buildout's financing/depreciation/interest/stock-comp costs (D&A +130% YoY, interest expense +346% YoY, stock comp +381% YoY) outrunning revenue growth, not a comparable one-off distortion this time.

### 2.3 Cash flow — FY2024–FY2026, FCF by year ($ millions)

| | FY2024 | FY2025 | **FY2026 (new)** |
|---|---|---|---|
| Operating cash flow (OCF) | 52.219 | 245.886 | **2,100.418** |
| CapEx (PP&E purchases) | 141.855 | 573.456 | **2,998.006** |
| **Free Cash Flow (OCF − CapEx)** | **(89.636)** | **(327.570)** | **(897.588)** |

OCF turned sharply positive in FY2026 (customer prepayments flowing through operating cash flow — consistent with the "~45% of GPU capex prepaid" disclosure noted in the 2026-07-20 session), but CapEx scaled even faster, so **FCF is still negative, and by a wider dollar amount than any prior year.**

### 2.4 Balance sheet — as of 30 June 2026 ($ millions)

| | 30-Jun-2025 | **30-Jun-2026 (new)** |
|---|---|---|
| Cash and cash equivalents (unrestricted) | 564.526 | **5,895.591** |
| Restricted cash (current + noncurrent) | 0.000 | **1,723.936** |
| Total assets | 2,940.323 | **15,790.039** |
| Long-term debt (current + noncurrent, carrying value) | 962.765 | **7,592.944** |
| Finance lease liability (current + noncurrent) | 0.000 | **243.796** |
| Total liabilities | 1,122.835 | **11,604.426** |
| Total shareholders' equity | 1,817.488 | **4,185.613** |

The unrestricted cash + restricted cash total ($5,895.591M + $1,723.936M = **$7,619.5M**) matches the "~$7.6bn" preliminary/unaudited figure the 2026-07-20 session flagged as a data gap (disclosed then without a matching debt figure) — that gap is now resolved with a full audited balance sheet.

```
Total debt-like obligations = Long-term debt + Finance lease liability
                             = 7,592.944 + 243.796 = 7,836.740   ($M)
Net Debt (30 Jun 2026)       = Total debt − unrestricted cash
                             = 7,836.740 − 5,895.591 = 1,941.149  ($M)
```
Restricted cash ($1,723.936M, tied up as collateral for GPU financing per the 2026-07-20 session's prior disclosure) is **excluded** from the cash side of this netting, consistent with treating it as unavailable general-purpose cash — the same conservative convention flagged (for a smaller, unaudited version of this same cash figure) in the 2026-07-20 session.

### 2.5 TTM reconstruction — not needed this session

Both prior sessions had to reconstruct a trailing-twelve-month figure from a stub 10-Q period. This session doesn't need that: the FY2026 10-K's fiscal year (1 Jul 2025 – 30 Jun 2026) **is** the trailing twelve months as of the live-price date. All figures above are used directly.

### 2.6 Moat, revenue segmentation, and today's Nvidia/Firmus news — qualitative evidence, cited sources

Pulled directly from the FY2026 10-K's Item 1 (Business) and risk-factor sections:

- **Customer concentration:** the 10-K explicitly flags "significant customer concentration" in AI Cloud Services as a risk factor — consistent with, not contradicting, the framework's continued skepticism about counting named-logo announcements as moat evidence on their own.
- **Competitive position:** IREN names AWS, Google Cloud, Microsoft Azure, and Oracle Cloud as competitors and states plainly that "many of our competitors have greater financial, technical or commercial resources... compared to us" — no market-share claim is made for AI Cloud Services itself (only the pre-existing Bitcoin-mining hash-rate share figure, carried forward unchanged).
- **Contract structure (new specific evidence this session):** "We primarily offer our AI Cloud Services under multi-year reserved capacity arrangements" specifying "amount and type of capacity, service levels, pricing, contract term, **customer prepayments**, deployment schedules, testing and acceptance conditions and ramp periods." Multi-year, prepayment-backed reserved-capacity contracts are a genuine, citable **switching-cost mechanism** (a customer that has prepaid a large fraction of the GPU capex tied to a specific IREN site has a real economic disincentive to relocate that workload) — this is new, audited-filing-sourced evidence, not just a named-logo announcement, and is credited below (§3.2, Moat signal 2 of 5).
- **Scale claim, not credited:** the 10-K states "procurement scale, deployment experience and direct control over the data center layer enables us to coordinate long-lead equipment... at scale" — a qualitative self-description without the cost-per-unit data the framework's Moat Signal table requires for the "scale cost advantage" signal, so it is **not** credited (same evidentiary bar applied in both prior sessions).
- **NVIDIA relationship (broader than today's Telegram post):** the 10-K discloses a **May 2026 strategic partnership with NVIDIA** covering "up to 5GW of NVIDIA DSX-aligned AI infrastructure" globally, plus NVIDIA's right to invest up to $2.1bn in IREN ordinary shares tied to GPU delivery milestones, and IREN's "NVIDIA Preferred Partner" / "NVIDIA Exemplar Cloud" status. Today's Nvidia/Firmus/Australia press release (§0) is a **regional subset** of this already-disclosed global partnership, not a new standalone relationship.
- **Bundey campus:** confirmed at 800MW in South Australia, per the 10-K's own data-center capacity table — matching the Telegram post's figure exactly.
- **Going concern:** no going-concern language found in the reviewed sections (risk factors instead state "we have a history of operating losses, and we may incur net losses in the future," a standard risk disclosure, not a going-concern flag).

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

Per quality-scoring.md's 2026-08-05 rolling-window clarification, both consecutive-year tests below are evaluated on the **most recently completed fiscal years as of this session** — now FY2024–FY2026, rolled forward one year from the FY2023–FY2025 window used in both prior sessions.

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF positive 3+ consecutive years | FY2024: **($89.636)M** · FY2025: **($327.570)M** · FY2026: **($897.588)M** — all three most recently completed fiscal years FCF-negative, deficit still widening in dollar terms | disqualify if not 3 consecutive positive years | **❌ FIRES.** Same disqualifier as both prior sessions, now re-tested against the rolled-forward window and still failing — cleanly and unambiguously. |
| Net Debt/EBITDA over threshold (2.5× standard; not asset-light eligible) | Net debt $1,941.149M (§2.4) against **negative** TTM/FY2026 EBITDA of **($628.985)M** (EBITDA = Operating income (1,046.714) + D&A 417.729 = −628.985, §2.2) | disqualify if exceeds 2.5× | **❌ EFFECTIVELY FIRES.** Ratio not computable as a meaningful finite multiple (positive net debt over negative EBITDA); conservative treatment applied (§3.2), not the formula's spurious face-value output — same treatment as both prior sessions. |
| FCF/NI conversion <70% for 2+ consecutive years w/o growth-capex explanation | FY2025 FCF/NI = −327.570/86.941 = **−376.8%** (mixed sign: FCF negative, NI positive) · FY2026 FCF/NI = −897.588/−702.621 = **+127.7%** (both negative — see §3.2 note on why this is not treated as a genuinely "good" ratio) | disqualify if 2+ consecutive years <70% w/o carve-out | Not independently relied upon — the other two checks already fire unambiguously. Shown for transparency, same as both prior sessions. |

**Two of three hard disqualifiers fire — same as both prior sessions, independently re-verified against fresh FY2026 audited figures. Per quality-scoring.md and this session's instructions: STOP HERE — do not proceed to Phase 02 valuation scoring, regardless of the weighted Quality Score computed below.**

### 3.2 Quality Score — full computation (produced for the record, per the "every sub-score shown" instruction, even though the gate has already failed above)

```
PROFITABILITY (25% weight):
  Net Margin (FY2026) = −702.621 / 707.007 = −99.38%
  NetMargin_Component = clamp((−99.38/30)×100, 0, 100) = clamp(−331.3, 0, 100) = 0.0

  EBIT (FY2026, operating income) = −1,046.714
  Invested Capital (30 Jun 2026) = Total debt-like obligations + Equity − Cash
                                  = 7,836.740 + 4,185.613 − 5,895.591 = 6,126.762
  ROIC = −1,046.714 / 6,126.762 = −17.08%
  ROIC_Component = clamp((−17.08/30)×100, 0, 100) = clamp(−56.9, 0, 100) = 0.0

  Raw Profitability_Score = (0.0 + 0.0) / 2 = 0.0
  FCF-positivity cap check: not FCF-positive 3+ years → cap at 40.0; raw score already below cap.
  Profitability_Score = 0.0

MARGINS (15% weight):
  Gross Margin (FY2026) = 487.301 / 707.007 = 68.92%
  GrossMargin_Score = clamp((68.92/80)×100, 0, 100) = 86.2
  Already well above the 40% bonus-eligibility threshold — no trend bonus applies.
  Margins_Score = 86.2

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2023 $75.509M → FY2026 $707.007M, most recently completed 3-year window)
    = (707.007/75.509)^(1/3) − 1 = 110.77%
  Growth_Score = clamp((110.77/25)×100, 0, 100) = clamp(443.1, 0, 100) = 100.0  (saturated)
  TAM/pricing-power modifier: moot — already saturated at the ceiling.
  Growth_Score = 100.0

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (FY2026) = $1,941.149M / ($628.985M) — undefined as a meaningful finite ratio (§3.1).
  Same formula blind spot as both prior sessions (negative EBITDA denominator would spuriously clamp
    to 100.0 — the opposite of what it should mean). Conservative override applied.
  BalanceSheet_Score = 0.0

MOAT SIGNAL (15% weight):
  1. Market share stable/growing — TRUE (carried forward, weak/commodity signal: Bitcoin hash-rate share).
  2. Brand premium — not credited (no pricing-power evidence located).
  3. Network effect — not credited (no documented mechanism).
  4. Switching costs — TRUE (new this session): FY2026 10-K discloses AI Cloud Services contracts are
     structured as multi-year reserved-capacity arrangements with customer prepayments tied to specific
     site capex (§2.6) — a genuine, cited, filed-document mechanism for customer lock-in, not just a
     named-logo announcement.
  5. Scale cost advantage — not credited (qualitative "procurement scale" claim in the 10-K, no
     cost-per-unit data vs. competitors — same evidentiary bar as both prior sessions).
  Moat_Score = (2/5) × 100 = 40.0

FCF QUALITY (10% weight):
  FY2026 FCF/NI = −897.588 / −702.621 = +127.7%
  Formula-literal: FCFQuality_Score = clamp(((1.277 − 0.40)/0.60)×100, 0, 100) = clamp(146.2, 0, 100) = 100.0
  ⚠️ Flagged, not used at face value: a ratio of two negative numbers (FCF negative, NI negative) landing
    "above 100%" is a sign-cancellation artifact, not evidence of strong cash-conversion quality — the
    same category of formula blind spot as the Balance Sheet's negative-EBITDA case just above (both are
    "negative-denominator/negative-input produces a spuriously high score" scenarios). Conservative
    override applied, consistent with that same-session precedent.
  FCFQuality_Score = 0.0  (conservative override — see flag above)

QUALITY SCORE = 0.0×0.25 + 86.2×0.15 + 100.0×0.20 + 0.0×0.15 + 40.0×0.15 + 0.0×0.10
             = 0.000 + 12.930 + 20.000 + 0.000 + 6.000 + 0.000
             = 38.930 → rounds to 38.9
```

**Quality Score = 38.9 / 100.0 — fails the 80.0+ gate by a wide margin on the weighted score alone, AND independently fails via two hard disqualifiers.** This is *lower* than the 44.5 computed in both prior sessions — mainly because Profitability_Score dropped from 34.8 to 0.0 (FY2025's net-margin figure was inflated by a one-off gain; FY2026 shows a genuine, large net loss instead) and FCF Quality stayed at 0.0 under the conservative override, only partly offset by Moat_Score rising from 20.0 to 40.0 (new switching-cost evidence) and the Growth/Margins components remaining saturated/strong.

**Gate result: FAIL.** Per quality-scoring.md, operating-brief.md, and this session's explicit instructions: **do not proceed to the Rate Environment Gate, Phase 02 valuation scoring, the Composite Score, or any order setup.**

---

## 4. Phase 02 / Order Setup — NOT PRODUCED

No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup is computed this session, for the same reason as both prior sessions: the Quality Score gate is a strict, non-negotiable prerequisite, and IREN clears neither the weighted-score threshold (38.9 vs. 80.0 required) nor either of two applicable hard-disqualifier checks.

---

## 5. Data Gaps Flagged

1. **No IREN-specific SEC filing exists yet for the Nvidia/Firmus/Australia partnership** named in today's Telegram post — it is independently corroborated via NVIDIA's own press release and multiple news outlets (§0), but if/when IREN itself files an 8-K on it (as it did for the July contract-wins news), that filing may add detail not yet public (contract value, timeline specifics, capex commitments) — worth checking at the next review.
2. **Exact dollar/contract terms of the Australia buildout are not disclosed** in NVIDIA's release for IREN specifically — flagged, not estimated around.
3. **Weighted-average diluted share count for FY2025** (~223M) shown in §2.2 is an approximation implied by EPS diluted (0.39) and reported net income (86.941), since the exact XBRL diluted-share tag for FY2025 wasn't independently pulled this session (FY2024 and FY2026 diluted-share/EPS figures were pulled directly). Doesn't affect any scored figure.
4. No other data gaps — every figure used in the Quality Score computation (§3.2) is a directly filed, primary-sourced SEC EDGAR XBRL figure from the audited FY2026 10-K.

---

## 6. Qualitative Notes

1. **The Telegram trigger checks out, corroborated through a different primary source than usual.** No IREN 8-K exists for it yet, but NVIDIA's own newsroom release (2026-09-09), independently repeated across several outlets, confirms the partner list, the 2GW/2027 Australia figure, and the Bundey 800MW campus detail — the last of which is *also* independently confirmed in IREN's own FY2026 10-K, filed two weeks before the Telegram post existed.
2. **This is a regional subset of an already-disclosed relationship, not new information about the relationship's existence.** IREN's FY2026 10-K (filed 2026-08-27) already discloses a much larger May-2026 global NVIDIA strategic partnership (up to 5GW of DSX-aligned infrastructure, a $2.1bn share-investment right for NVIDIA tied to GPU delivery). Today's Australia-specific, 8-company-consortium announcement is a specific regional application of that broader partnership.
3. **Nothing about today's Nvidia/Firmus news, or the FY2026 10-K's much larger and more consequential disclosures, changes the mechanics of why IREN fails the gate.** The hard disqualifiers are backward-looking, audited-financial-statement facts — three straight fiscal years of negative free cash flow (now FY2024–FY2026, deficit still widening in dollar terms: −$89.6M → −$327.6M → −$897.6M) and negative operating-level (and thus EBITDA) profitability against roughly $7.8B of debt-like obligations. A capacity-partnership announcement, however credible, cannot retroactively cure that.
4. **The FY2026 10-K itself is the more consequential event this session, independent of the Telegram trigger.** It replaces last session's partial-year TTM reconstruction with full audited figures, and the picture it shows is mixed: operating cash flow turned sharply positive (prepayment-driven), Moat evidence strengthened slightly (a real, cited switching-cost mechanism now exists), but net income swung from a one-off-inflated small gain to a genuine $702.6M loss, and free cash flow burn *widened* in dollar terms even as the business scaled — a capital-intensity profile that still doesn't clear this framework's cash-generation bar, and mechanically cannot until CapEx growth decelerates below OCF growth for a sustained multi-year stretch.
5. **This is a Rule 9 fundamental-event trigger (quarterly/annual earnings release — the FY2026 10-K — plus a material new infrastructure-partnership announcement), which is why this session exists at all**, and the underlying weighted Quality Score did move (44.5 → 38.9) even though the gate outcome (FAIL) did not — see §8.

---

## Recommendation

# **PASS — Quality Score gate FAILS again (38.9, down from 44.5, well below the 80.0+ threshold) AND the same two hard disqualifiers independently fire (not FCF-positive for 3+ consecutive years; Net Debt/EBITDA effectively unbounded against negative TTM EBITDA). Do not proceed to valuation scoring. No position, no watchlist-only tracking recommendation beyond a monitoring pointer.**

The FY2026 10-K — the trigger both prior sessions were explicitly waiting for — is now in, and it doesn't change the outcome: IREN scores *lower* on the weighted Quality Score than it did two sessions ago, not higher, because a full audited year shows a genuine $702.6M net loss and a wider (not narrower) FCF deficit, only partly offset by new, real switching-cost moat evidence. The Nvidia/Firmus/Australia news is accurate and well-corroborated but is capacity-partnership news, not a financial statement, and doesn't move any scored input. **This does not count as a BUY, TRIM, or EXIT trigger.**

---

## 7. Next Review Trigger

- **IREN's FY2027 10-K** (fiscal year ends 30 June 2027; expected ~August/September 2027) or, more likely sooner, its **FY2027 Q1–Q3 10-Qs**, which will show whether OCF growth is starting to outpace CapEx growth as the AI Cloud buildout matures — the FCF-positivity disqualifier mechanically requires 3 consecutive *positive* fiscal years going forward, so cannot clear before FY2029 at the absolute earliest even under an optimistic path.
- **Standard Rule 9 triggers:** guidance revision, a material new AI Cloud customer/contract announcement, an IREN-specific 8-K on the Nvidia/Firmus Australia buildout (if filed), management change, macro shift, or a >15% *unexplained* price move.
- **Segment-mix milestone:** if/when AI Cloud Services revenue crosses roughly a third to a half of total revenue (not yet disclosed as a standalone segment split in the reviewed 10-K excerpt), worth an informal look even before the next scheduled trigger.

---

## 8. Watchlist & Stale-Score Housekeeping

- **New dated watchlist entry created:** [watchlist/not-in-portfolio/IREN/IREN-2026-09-10.md](../watchlist/not-in-portfolio/IREN/IREN-2026-09-10.md) — per [watchlist/README.md](../watchlist/README.md#significant-change--when-does-a-new-dated-entry-get-created), warranted on two independent grounds: (1) **the underlying weighted Quality Score numerically changed** (44.5 → 38.9, even though both remain "Phase 01 FAIL"), and (2) **a Rule 9 fundamental-event trigger fired** (the FY2026 10-K annual earnings release, plus the Nvidia/Firmus infrastructure news). The prior [IREN-2026-07-15.md](../watchlist/not-in-portfolio/IREN/IREN-2026-07-15.md) and [IREN-2026-07-20.md](../watchlist/not-in-portfolio/IREN/IREN-2026-07-20.md) entries are preserved unmodified.
- **Stale-score mechanism:** not applicable — IREN is Phase 01 FAIL / not scored, and per watchlist/README.md, "Entries that are 'Phase 01 FAIL / not scored' are not marked" for staleness. Confirmed IREN carries no row in [watchlist/STALE.md](../watchlist/STALE.md) (re-checked this session).

---

## 9. Glossary

- **8-K (Form 8-K)**: a US company's "current report" filed with the SEC to disclose a material event between its regular quarterly/annual filings.
- **AI Cloud Services**: IREN's newer business segment — leasing GPU compute capacity in its data centers to AI customers — distinct from its legacy Bitcoin mining segment.
- **CapEx**: Capital Expenditure — money spent buying or upgrading physical assets; central to IREN's hard-disqualifier finding (§2.3, §3.1).
- **CIK (Central Index Key)**: the SEC's unique numeric filer identifier — IREN's is 0001878848.
- **Composite Score**: this framework's blended 0.0–100.0 ranking (`0.50 × (100 − Quality Score) + 0.50 × Valuation Score`) — not computed this session, since IREN never clears the Quality Score gate required to reach it.
- **D&A**: Depreciation & Amortization.
- **DSX (NVIDIA) / "AI factory"**: NVIDIA's full-stack reference architecture for a large-scale AI data center (facilities/power, compute, networking, software as one integrated design); "AI factory" is NVIDIA's marketing term for a data center built to that blueprint. Central to today's Nvidia/Firmus/Australia announcement (§0, §2.6).
- **EBIT / EBITDA**: Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — IREN's FY2026 EBITDA is negative (§3.1, §3.2).
- **EDGAR / XBRL**: the SEC's public filing database and the machine-readable financial-data format within it — the primary data source for every figure used this session.
- **FCF / FCF Yield / FCF/NI conversion ratio**: Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check) — central to this session's hard-disqualifier finding (§3.1).
- **Form 10-K**: the annual audited financial-disclosure report a US public company files with the SEC — this session's central new data source (§2.1).
- **Gross Margin**: Gross Profit ÷ Revenue — IREN's FY2026 figure is 68.9% (§3.2).
- **Hard disqualifier**: a Quality Score condition that fails a company regardless of its weighted score; IREN fires two of the three, again this session (§3.1).
- **Invested Capital**: debt + equity − cash, the ROIC denominator.
- **Moat**: a durable competitive advantage protecting a business's profits from competitors — scored 40.0 (2 of 5 signals) for IREN this session, up from 20.0 (1 of 5) previously (§3.2).
- **NASDAQ**: the US stock exchange IREN trades on.
- **Net Debt/EBITDA**: this framework's primary balance-sheet-risk gate — undefined as a meaningful finite multiple for IREN, given negative FY2026 EBITDA (§3.1, §3.2).
- **Net Margin**: Net Income ÷ Revenue — IREN's FY2026 figure is −99.4%, a genuine net loss (not a one-off-gain distortion as in FY2025) (§2.2, §3.2).
- **ROIC**: Return on Invested Capital — IREN's FY2026 figure is deeply negative (−17.1%, §3.2).
- **TTM (Trailing Twelve Months)**: the most recent 12 months of reported financial results; not needed as a separate reconstruction this session since the FY2026 10-K's fiscal year already is the TTM window (§2.5).

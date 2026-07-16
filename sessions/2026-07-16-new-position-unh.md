# NEW POSITION — UNH (UnitedHealth Group Incorporated, NYSE) — 2026-07-16

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, re-evaluation)
**Date:** 16 Jul 2026 (Thursday)
**10Y US Treasury Yield:** 4.58% (FRED `DGS10`, most recent posted observation dated 2026-07-14) — recorded for completeness; not used, since this session again stops at the Quality Gate (§4) before reaching the Rate Environment Gate.
**Current UNH portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** [UNH-2026-07-16.md](../watchlist/not-in-portfolio/UNH/UNH-2026-07-16.md) (renamed from UNH-2026-07-13.md via `git mv`, history preserved) — 2026-07-13 entry: Quality Score 36.1, Phase 01 FAIL. That entry's own "Next review trigger" named today's Q2 2026 earnings release as "the single most important near-term trigger."
**Sector:** Healthcare — Managed Care / Health Insurance (UnitedHealthcare segment) + Health Services (Optum segment)
**Filer type:** US domestic filer — CIK **731766**, Form 10-K/10-Q.
**First-use jargon decode:** see closing Glossary (§9); most terms carry over from the 2026-07-13 entry.

---

## 0. Why this session exists — trigger source

A Telegram post on **FinnInvestChannel** (post #2942, 2026-07-16T12:02:59Z) reported (translated from Ukrainian): *"UNITEDHEALTH GROUP Q2'26 — Revenue: $112.0B (Est. $110.8B), no growth — Adj. EPS: $6.38 (Est. $4.85) +56% YoY — Improved 2026 guidance — [poster's own P&L note, not used]."* Per the operating brief, **Telegram post text is never used as financial data** — it is a trigger only, independently verified below against UnitedHealth Group's own SEC filing.

This is exactly the documented Rule 9 trigger the 2026-07-13 watchlist entry flagged in advance ("UNH's Q2 2026 earnings, 2026-07-16"), so per `/telegram-scan` step 4's second bullet (held-or-not, a claimed Rule 9 event on a name with a due review trigger) this warrants a fresh `/new-position` run — UNH is not held, but its `not-in-portfolio` entry explicitly named this date as the next review trigger, which is the third-bullet "materially new information" case.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$443.81** | IBKR `get_price_snapshot`, `last` field, timestamp 1784203674 (≈11:41 UTC 2026-07-16), contract_id **13272** (NYSE, "UNITEDHEALTH GROUP INC", exact-symbol US primary listing confirmed via `search_contracts`), `is_close: false` (intraday, market open) |
| Day change | **+$25.29 (+6.04%)** | IBKR `get_price_snapshot` `change` field — a same-day post-earnings pop, corroborating the Telegram post's "beat" framing independently, via price action rather than the post's own claims |
| Bid/Ask | $444.00 / $444.50 | IBKR `get_price_snapshot` `bid_ask` field |
| US 10Y Treasury yield | 4.58% | FRED `DGS10`, as-of 2026-07-14 |

$443.81 is used as the live price for reference throughout this session — no order-setup arithmetic is performed, since the Quality Gate fails below (§4), same as 2026-07-13.

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note

Q2 2026 quarterly figures are **primary-sourced** from UnitedHealth Group's own **Form 8-K filed 2026-07-16** (accession **0000731766-26-000191**), Exhibit 99.1, "UnitedHealth Group Reports Second Quarter 2026 Results" — fetched directly from SEC EDGAR (`https://www.sec.gov/Archives/edgar/data/731766/000073176626000191/earningsrelease2q26_7152.htm`) and cross-checked line-by-line against the figures programmatically extracted from Yahoo Finance's `quoteSummary` API (both independently agree on Q2 2026 revenue $112,032M and net earnings to common $5,484M). All FY2023–FY2025 annual figures, the Q1 2026 balance sheet, and the FY2022 revenue figure are carried forward unchanged from the [2026-07-13 session](2026-07-13-new-position-unh.md) (§2 there), which cited each by exact SEC EDGAR URL — not re-fetched, since nothing about the historical record changed in three days.

### 2.2 Q2 2026 quarterly income statement — primary-sourced (SEC EDGAR 8-K, Exhibit 99.1)

| Item | Q2 2026 ($M) | Q2 2025 ($M, comparative) |
|---|---|---|
| Revenue | 112,032 | 111,616 |
| Medical costs | 75,358 | 78,585 |
| Operating costs | 14,268 | 13,778 |
| Cost of products sold | 13,375 | 13,019 |
| Depreciation & amortization | 1,040 | 1,084 |
| Total operating costs | 104,041 | 106,466 |
| Earnings from operations | 7,991 (≈"$8.0B" as stated) | 5,150 |
| Interest expense | (962) | (1,027) |
| Loss on sale of subsidiary/held-for-sale | (61) | (41) |
| Earnings before income taxes | 6,968 | 4,082 |
| Provision for income taxes | (1,298) | (510) |
| Net earnings | 5,670 | 3,572 |
| Earnings attributable to noncontrolling interests | (186) | (166) |
| **Net earnings attributable to UNH common shareholders** | **5,484** | 3,406 |
| Diluted EPS (GAAP) | $6.04 | $3.74 |
| Diluted EPS (company-adjusted, non-GAAP) | $6.38 | $4.08 |

Medical Care Ratio: **86.7%** (Q2 2026) vs. 89.4% (Q2 2025) — a 270bps YoY improvement, company-attributed to "product design changes, improved medical management and better aligned pricing," with $860M of net favorable prior-period reserve development. **UnitedHealth Group raised full-year 2026 guidance** the same release: diluted GAAP EPS to $18.45–$18.95 (from a prior >$17.10 floor set 2026-01-27) and adjusted EPS to $19.50–$20.00 (from a prior >$17.75 floor) — a genuine, primary-sourced guidance revision, itself an independent Rule 9 event, layered on top of the earnings release itself.

**Medicare Advantage membership continued contracting**, not reversing: "Seniors served through Medicare Advantage... have contracted by 965,000 since year-end 2025" (release, UnitedHealthcare segment detail); the release's own performance-metrics table shows Medicare Advantage membership at 7,565K (30 Jun 2026) vs. 8,350K (30 Jun 2025) — a **9.4% YoY decline**, continuing exactly the structural deceleration documented in the 2026-07-13 session (§4.2 there), not a one-quarter blip.

### 2.3 TTM reconstruction (Q3 2025 + Q4 2025 + Q1 2026 + Q2 2026 — rolling Q2 2025 out, Q2 2026 in)

Q3 2025 / Q4 2025 / Q1 2026 figures carried forward unchanged from the 2026-07-13 session's primary-sourced table (§2.2 there).

```
Revenue TTM             = 113,161 + 113,215 + 111,721 + 112,032 = 450,129
Medical Costs TTM        = 79,958 + 82,041 + 73,489 + 75,358     = 310,846
Operating Costs TTM      = 15,223 + 16,997 + 15,390 + 14,268     = 61,878
Cost of Products Sold TTM = 12,566 + 12,680 + 12,823 + 13,375    = 51,444
D&A TTM                  = 1,099 + 1,117 + 1,029 + 1,040         = 4,285
Total Op. Costs TTM      = 108,846+112,835+102,731+104,041       = 428,453  (cross-check: 310,846+61,878+51,444+4,285 = 428,453 ✓)
EBIT (Earnings from Ops) TTM = 4,315+380+8,990+7,991             = 21,676   (cross-check: 450,129−428,453 = 21,676 ✓)
Interest Expense TTM     = 1,003+974+955+962                     = 3,894
Pretax Income TTM        = 3,229+(−720)+7,963+6,968              = 17,440
Tax TTM (net, signed)    = −686+938−1,482−1,298                  = −2,528  (net expense)
Net Earnings TTM         = 17,440 − 2,528                        = 14,912  (cross-check: 2,543+218+6,481+5,670 = 14,912 ✓)
Net Earnings, Common TTM = 2,348+10+6,280+5,484                  = 14,122
Diluted EPS TTM (summed) = 2.59+0.01+6.90+6.04                   = $15.54
Effective tax rate TTM   = 2,528/17,440                          = 14.50%
```

### 2.4 Balance sheet — primary-sourced (Q2 2026 8-K condensed consolidated balance sheet, June 30, 2026)

| Item | Value ($M) | Source |
|---|---|---|
| Cash and cash equivalents, end of period | 28,585 | 8-K Exhibit 99.1, condensed cash-flow statement (the precise "cash and cash equivalents" reconciliation line — deliberately used instead of the balance sheet's broader "Cash and short-term investments" $31,468M line, to keep the same strict cash definition as the 2026-07-13 session's Q1 2026 figure) |
| Short-term borrowings + current maturities of LT debt | 3,827 | 8-K Exhibit 99.1, condensed balance sheet |
| Long-term debt, less current maturities | 69,501 | same |
| **Total debt** | **73,328** | 3,827 + 69,501 |
| Equity | 104,513 | same (condensed presentation; the 8-K does not break out UNH shareholders' equity vs. nonredeemable NCI the way the Q1 2026 10-Q did — flagged as a minor presentation-granularity gap, non-blocking, will reconcile once the Q2 2026 10-Q files) |
| Total assets | 309,727 | same |

```
Net Debt = Total Debt − Cash = 73,328 − 28,585 = 44,743
```

### 2.5 Cash flow — primary-sourced (8-K Exhibit 99.1, six-months-ended comparative cash-flow statement)

| Period | Operating CF ($M) | CapEx ($M) | FCF ($M) |
|---|---|---|---|
| 6mo 2026 (H1) | 19,964 | 1,562 | 18,402 |
| 6mo 2025 (H1) | 12,644 | 1,784 | 10,860 |
| Q2 2026 (derived: H1 2026 − Q1 2026) | 11,052 | 799 | 10,253 |
| Q2 2025 (derived: H1 2025 − Q1 2025) | 7,188 | 886 | 6,302 |

Q1 2026 and Q1 2025 OCF/CapEx carried forward from the 2026-07-13 session (Q1 2026: OCF 8,912 / CapEx 763; Q1 2025: OCF 5,456 / CapEx 898, both there primary-sourced to the Q1 2026 10-Q).

```
New TTM OCF   = Old TTM OCF (23,153) − Q2 2025 OCF (7,188) + Q2 2026 OCF (11,052) = 27,017
New TTM CapEx = Old TTM CapEx (3,487) − Q2 2025 CapEx (886) + Q2 2026 CapEx (799) = 3,400
New TTM FCF   = 27,017 − 3,400 = 23,617
```

### 2.6 Annual income statement, FY2022–FY2025 — unchanged, carried forward from 2026-07-13 (§2.6 there)

Revenue 3yr CAGR (FY2022→FY2025) = 11.35% — unaffected by this quarter, since it is computed off completed fiscal years only.

---

## 3. Rule 9 Context Update (read alongside 2026-07-13 session §3, not a replacement)

The 2026-07-13 session's five numbered Rule 9 items (CEO change, 2025 guidance suspension/re-establishment, the open DOJ investigation, the Q4 2025 one-time charge, and the 2026 guidance/Q1 2026 beat) all still stand unchanged and are not repeated here. This session adds:

6. **Q2 2026 results + a second consecutive guidance raise (16 Jul 2026):** Revenue $112.0B, GAAP EPS $6.04, adjusted EPS $6.38 (vs. $4.08 a year earlier), medical care ratio improved 270bps YoY to 86.7%. Full-year 2026 guidance raised for the second time this year (originally >$17.10 GAAP / >$17.75 adjusted on 2026-01-27; now $18.45–$18.95 GAAP / $19.50–$20.00 adjusted). **This is itself an independent Rule 9 guidance-revision trigger**, on top of the earnings release.
7. **DOJ investigation still open, still unresolved:** the release's own forward-looking risk-factor language references "the DOJ's legal actions concerning our participation in the Medicare program" with no settlement, charge, or resolution disclosed — tracked as before, in neither direction.
8. **Medicare Advantage membership decline continued, not reversed:** −965,000 seniors served since year-end 2025; MA membership down 9.4% YoY (7,565K vs. 8,350K). This directly confirms — rather than calls into question — the 2026-07-13 session's Growth sub-score structural-deceleration modifier (§4.2 there): the trend it was based on is still actively playing out, not a stale one-time observation.

**Framework treatment, unchanged from 2026-07-13:** this session's Quality Score is built on the rolled-forward **TTM window Q3 2025–Q2 2026** per the standard methodology, off filed GAAP figures, not company-adjusted non-GAAP metrics — consistent with framework precedent (glossary.md's PepsiCo/Stellantis/S&P Global adjusted-metric treatments).

---

## 4. Phase 01 — Quality Score (2026-06-29 methodology)

### 4.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years w/o growth-capex explanation | FY2023 114.7% · FY2024 143.7% · FY2025 133.3% · **TTM (new) 167.2%** | disqualify if 2+ consecutive years <70% | ✅ PASS, by a wide margin every period shown |
| Net Debt/EBITDA over threshold (2.5× standard — UNH still does not qualify for the Upgrade 5 asset-light override) | **TTM (new): Net Debt $44,743M / EBITDA $25,961M (=EBIT $21,676M + D&A $4,285M) = 1.723×** (improved from 2.155× on 2026-07-13) | disqualify if >2.5× | ✅ PASS |
| FCF-positive 3+ consecutive years | FY2023 $25,682M · FY2024 $20,705M · FY2025 $16,075M — all positive | disqualify if not | ✅ PASS |

**No hard disqualifier fires** — same conclusion as 2026-07-13.

### 4.2 Quality Score — full computation

```
PROFITABILITY (25% weight):
  Net Margin (TTM, common) = 14,122 / 450,129 = 3.137%   (up from 2.678% on 2026-07-13)
  NetMargin_Component = clamp((3.137/30)×100, 0, 100) = 10.46

  NOPAT = EBIT_TTM × (1 − eff. tax rate) = 21,676 × (1 − 0.1450) = $18,534M
  Invested Capital = Total Debt + Equity − Cash (Jun 30 2026) = 73,328 + 104,513 − 28,585 = $149,256M
  ROIC = 18,534 / 149,256 = 12.42%   (up from 10.78% on 2026-07-13)
  ROIC_Component = clamp((12.42/30)×100, 0, 100) = 41.39

  Profitability_Score = (10.46 + 41.39) / 2 = 25.92   (no FCF-positivity cap — 3yr positive confirmed above)
    [2026-07-13: 22.43]

MARGINS (15% weight):
  Gross Profit TTM = Revenue − Medical Costs − Cost of Products Sold = 450,129 − 310,846 − 51,444 = $87,839M
    [Same judgment-call construction as 2026-07-13 §4.2 — Medical Costs + Cost of Products Sold as the
     cost-of-revenue analog for a managed-care company with no single "Cost of Revenue" line.]
  Gross Margin (TTM) = 87,839 / 450,129 = 19.51%   (up from 18.80% on 2026-07-13)
  GrossMargin_Score = clamp((19.51/80)×100, 0, 100) = 24.39   [2026-07-13: 23.50]

  3yr trend check (unchanged — annual data, unaffected by this quarter): FY2023 24.48% → FY2024 22.33% →
  FY2025 18.53% — still DECLINING. No +10 structural-trend bonus applies. Note for human review: this
  quarter's TTM gross-margin uptick (18.80%→19.51%) is a genuine improving signal, but the framework's trend
  test is defined on completed fiscal years, not interpolated with partial-year data — FY2026's close (~Jan
  2027) is the next point this trend check can legitimately move.

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2022→FY2025) = 11.35%   (unchanged — annual data)
  Growth_Score = clamp((11.35/25)×100, 0, 100) = 45.4
  Structural deceleration modifier: −10 still applies — this quarter's own release CONFIRMS continuation,
  not reversal, of the trend (§3 item 8): MA membership down 9.4% YoY, −965,000 since year-end 2025.
  Growth_Score = clamp(45.4 − 10, 0, 100) = 35.4   [unchanged from 2026-07-13]

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (TTM, new) = 1.723×
  BalanceSheet_Score = clamp(100×(1 − 1.723/4), 0, 100) = 56.91   [2026-07-13: 46.13, the single largest
    mover this session — driven by both debt reduction (Net Debt 49,916→44,743) and higher trailing EBITDA
    as Q2 2026 replaces Q2 2025 in the window]

MOAT SIGNAL (15% weight) — same 5-signal checklist, evidence re-examined, no signal flips:
  Market share stable/growing: still FALSE — this quarter's own release confirms continued MA share/volume
    decline (§3 item 8), not stabilization.
  Brand premium: still FALSE — no new pricing-power evidence found this session.
  Network effect: still FALSE.
  Switching costs: still FALSE — no new, current-dated retention citation found this session either.
  Scale cost advantage: still TRUE (unchanged evidence: Optum Rx ~1.66B 2025 adjusted claims, one of three
    PBMs handling ~80% of US prescription volume, per Drug Channels, cited 2026-07-13). Note for the record:
    this quarter's own release shows Optum Rx *quarterly* adjusted scripts fell to 387M (Q2 2026) from 414M
    (Q2 2025), company-attributed to "membership declines within UnitedHealthcare and other customers" — a
    volume dip tied to UNH's own shrinking membership base, not necessarily third-party market-share loss,
    so this alone isn't treated as contradicting the annual-claims-volume evidence the TRUE signal rests on.
    Flagged for a closer look once FY2026 Optum Rx claims volume is available (next annual data point).
  Moat_Score = (1/5) × 100 = 20.0   [unchanged from 2026-07-13]

FCF QUALITY (10% weight):
  FCF/NI (TTM, new) = 23,617/14,122 = 167.24%
  FCFQuality_Score = clamp(((1.6724 − 0.40)/0.60)×100, 0, 100) = clamp(212.1, 0, 100) = 100.0
  [unchanged sub-score from 2026-07-13, still capped at 100.0; the same Q4 2025-charge-driven-denominator
   flag from that session still applies, since Q4 2025 remains inside this TTM window]

QUALITY SCORE = 25.92×0.25 + 24.39×0.15 + 35.4×0.20 + 56.91×0.15 + 20.0×0.15 + 100.0×0.10
             = 6.480 + 3.6585 + 7.08 + 8.5365 + 3.00 + 10.00
             = 38.76 → rounds to 38.8
```

**Robustness check (not just a point estimate):** even under the same maximally generous, evidence-unsupported alternate reading crediting Growth_Score = 100.0 and Moat_Score = 100.0:

```
25.92×0.25 + 24.39×0.15 + 100×0.20 + 56.91×0.15 + 100×0.15 + 100×0.10
= 6.480 + 3.6585 + 20.00 + 8.5365 + 15.00 + 10.00 = 63.68
```

**Still well below the 80.0 gate** (up from a 61.05 ceiling on 2026-07-13, but the improvement — entirely from the Balance Sheet sub-score's genuine deleveraging — isn't remotely enough). The gate-FAIL conclusion is not sensitive to this session's Moat/Growth judgment calls, same as before.

### 4.3 Gate result

**Quality Score = 38.8 / 100.0 — FAILS the 80.0+ gate** (up from 36.1 on 2026-07-13, a genuine +2.7 improvement, driven almost entirely by deleveraging (Balance Sheet sub-score +10.8) plus modest margin/ROIC gains as the worst 2025 quarter's drag partially dilutes — not by a change in the company's structural growth or moat picture, both of which remain unchanged or, on Growth, actively confirmed this quarter). No hard disqualifier independently fires. Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md): **stop here — do not proceed to the Rate Environment Gate, Phase 02 valuation scoring, the Composite Score, or fair-value/order-setup work.**

---

## 5. Structural Caveat for Human Review — unchanged, carried forward

Same managed-care-margin-calibration caveat as the 2026-07-13 session (§5 there) — this framework's Profitability/Margins formulas are calibrated against asset-light business models and may structurally understate quality for a business where a 2–5% net margin is normal, not distressed. Not re-litigated in full here; see that session for the complete discussion. Not adjusted this session either, per "never invent or estimate."

---

## 6. Qualitative Notes

1. **The Telegram trigger was accurate and, this time, the underlying event was analytically real** (unlike the 2026-07-13 session's "generic earnings-calendar reminder" trigger) — the post named genuine beat-and-raise figures, independently confirmed against the primary SEC filing (§2.1–2.2) to the dollar.
2. **This is a genuine, multi-quarter improving trend, not a one-quarter blip** — Q1 2026 and Q2 2026 have now both beaten and the company has raised full-year guidance twice in six months (Jan 2026, now July 2026). The next TTM roll-forward (Q3 2026 report, replacing Q3 2025's 4,315 EBIT quarter with a fresher one) is likely to show further improvement, absent a surprise.
3. **The single largest driver of this session's score change is balance-sheet, not operating, improvement** — Net Debt/EBITDA fell from 2.155× to 1.723× in three months, moving the Balance Sheet sub-score from 46.13 to 56.91 (+10.8, the largest single sub-score move). This reflects real deleveraging (debt-to-capital ratio improved from 42.9% to 41.2% YoY, per the release) plus a higher trailing EBITDA base — both genuine, not an artifact.
4. **The Q4 2025 one-time charge is still inside this TTM window** and will remain so until the Q4 2026 report rolls it out (~Jan 2027) — it still partially depresses trailing net margin/ROIC and still partially inflates the FCF/NI ratio, exactly as flagged on 2026-07-13. This is the single most important thing to watch for the next 1–2 quarters, alongside whether the Medicare Advantage membership decline stabilizes or the DOJ investigation resolves.
5. **Framework-fit note:** if UNH were re-evaluated once the FY2026 annual figures are available (Jan 2027, replacing the still-elevated FY2023 in the 3yr Revenue CAGR window and fully rolling the Q4 2025 charge out of the TTM), the Quality Score would very likely rise further on both Profitability and FCF Quality — worth flagging now as a name to actively re-check around that date rather than waiting for another Telegram trigger.

---

## 7. Recommendation

# **PASS — Quality Gate FAIL (Quality Score 38.8 < 80.0). Do not enter.**

UnitedHealth Group's Q2 2026 results were a genuine beat with a raised full-year guidance — independently confirmed against the company's own SEC filing, not just the Telegram post that triggered this session — and lift the Quality Score from 36.1 to 38.8. That improvement is real (mostly balance-sheet deleveraging, with modest profitability gains) but nowhere near enough: even the maximally generous robustness-check ceiling (63.68) remains well under the strict 80.0+ gate. **No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup was computed** — this session again stops at the Quality Gate per the command specification, same outcome category as 2026-07-13, now on a fresher and more favorable data point.

---

## 8. Next Review Trigger

- **UnitedHealth Group's Q3 2026 earnings** (expected mid-October 2026, exact date not yet announced as of this session) — will roll Q3 2025's still-depressed-relative-to-current-run-rate EBIT out of the TTM window; check whether the beat-and-raise trend (§6 item 2) continues.
- **FY2026 fiscal year-end close (~Jan 2027 report)** — fully replaces FY2023 in the 3yr Revenue CAGR window, fully rolls the Q4 2025 one-time charge out of the TTM Profitability/FCF-Quality inputs, and is the next point the Margins sub-score's 3yr-trend test can legitimately move. Flagged in §6 item 5 as a name worth proactively re-checking around that date.
- **Any DOJ investigation development** (settlement, charges, or a stated resolution) — unchanged trigger from 2026-07-13.
- **CMS's 2027 final risk-adjustment rule** (chart-review exclusion) — unchanged trigger from 2026-07-13.
- **Standard Rule 9 triggers:** further management change, material M&A, a macro/rate shift, or a >15% unexplained price move (note: today's +6.04% move is fully explained by the earnings release, not unexplained — no separate Rule 9 price-move trigger fires from this session).

**No position opened — nothing to log in `decisions/`.**

---

## 9. Glossary

All terms carry over from the [2026-07-13 UNH session Glossary](2026-07-13-new-position-unh.md#9-glossary) and [glossary.md](../framework/glossary.md) unchanged — no new jargon introduced this session. Key terms used above: **CIK**, **Composite Score**, **D&A**, **DOJ**, **EBIT/EBITDA**, **EPS**, **FCF / FCF Yield / FCF/NI conversion ratio**, **Hard disqualifier**, **Managed care**, **MCR/MLR**, **Medicare Advantage (MA)**, **NOPAT**, **Optum**, **PBM**, **Quality Score**, **Risk adjustment / "upcoding" / "chart review"**, **ROIC/ROE**, **Rule 0/6/9**, **TTM**, **XBRL** — see the 2026-07-13 session for full definitions.

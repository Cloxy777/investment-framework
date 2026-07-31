# NEW POSITION — AAPL (Apple Inc.)

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — unattended run; mandatory Rule 9 re-check named explicitly by the prior session)
**Date:** 2026-07-31 (Friday)
**10Y US Treasury Yield:** Not fetched this session — evaluation stops at the Phase 01 Quality Score gate (same precedent as the 2026-07-06 AAPL session and the 2026-07-30 HOOD session) before the Rate Environment Gate would otherwise apply.
**Current AAPL portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** [sessions/2026-07-06-new-position-aapl.md](2026-07-06-new-position-aapl.md) / [watchlist/not-in-portfolio/AAPL/AAPL-2026-07-06.md](../watchlist/not-in-portfolio/AAPL/AAPL-2026-07-06.md) — Quality Score 76.2, Phase 01 FAIL (weighted-score gate miss by 3.8 points; no hard disqualifier fired). That session's own "Next review trigger" specifically named Apple's fiscal Q3 2026 Form 10-Q, expected filed early August 2026, as "the most direct path to a different result" via "a sustained re-acceleration in consolidated revenue growth."
**Sector:** Technology — Consumer Hardware & Services
**Filer type:** US SEC filer, CIK 0000320193, California-incorporated, fiscal year ending the last Saturday of September.
**First-use jargon decode:** see closing Glossary.

---

## 0. Why this session exists — trigger source

Apple reported fiscal Q3 2026 results after market close on 2026-07-30. A Telegram post (`tarasguk`, ~20:33:10 UTC 2026-07-30) reported the headline numbers (revenue $109.42B vs. est. $108.65B, EPS $2.02 vs. est. $1.89, gross margin 50.1% vs. est. 47.92%, iPhone revenue $54.25B, Services revenue $30.74B, Mac revenue $10.35B, Greater China revenue $18.82B — all beats). **Per Rule 0/CLAUDE.md, the post's text is a trigger only, never a financial input.** Every figure in this session is independently fetched from Apple's own SEC 8-K (Exhibit 99.1, filed 2026-07-30) and prior-quarter SEC XBRL data — not copied from the post. Every one of the post's headline figures independently reconciled exactly (or to the nearest disclosed rounding) against the primary-source 8-K pulled in §2 below; noted for completeness, not used as a substitute for that independent pull.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| Contract identity | "APPLE INC", NASDAQ, contract_id **265598** (same contract as the 2026-07-06 session) | IBKR |
| **Live price** | **$313.19** (last trade, intraday, not a stale snapshot) | IBKR `get_price_snapshot` |
| Change vs. prior close | **−$20.24 / −6.07%** (prior close $333.43, 2026-07-30's regular-session close — the pre-earnings-reaction close, since results were released *after* that close) | IBKR `get_price_snapshot` (`change` field), cross-checked against `get_price_history` (2026-07-30 daily close = $333.43, matches exactly) |
| 52-week range | $200.879 (low) – $344.57 (high, also the 13-week and 26-week high — set within the trailing quarter, on 2026-07-29, the day before this earnings release) | IBKR `misc_statistics` |
| Dividend yield | 0.31% | IBKR `dividend_yield` |

**Context only (not a scoring input, not acted on per Rule 9):** the stock is down sharply (−6.07% intraday) despite an apparent across-the-board earnings beat — a "sell the news" reaction, plausibly related to the ~2pp of the quarter's gross-margin beat and ~$0.11 of EPS being flagged by Apple itself as a one-off tariff-refund benefit (see §3.2 Margins), guidance for the seasonally-important December quarter, or broader market/sector conditions not investigated further this session. This is observed, not interpreted as a trading signal — per Rule 9, "price dropped... short-term earnings miss" is explicitly **not** a valid basis for action on its own, and this wasn't even a miss. Not used anywhere in the scoring below.

**Live price used throughout this session: $313.19.**

---

## 2. Data Sourcing Note

Apple's fiscal Q3 2026 Form 10-Q (period ended 2026-06-27) **has not yet been filed** as of this session (confirmed via SEC EDGAR `submissions` API — the most recent 10-Q on file remains the 2026-05-01 filing for the quarter ended 2026-03-28). Apple did, however, file an **8-K on 2026-07-30** (accession `0000320193-26-000018`) furnishing its Q3 FY2026 earnings press release as **Exhibit 99.1**, containing the full unaudited Condensed Consolidated Statements of Operations, Balance Sheets, and Statements of Cash Flows for the quarter and nine months ended 2026-06-27 (with FY2025 comparatives) — read directly from `sec.gov/Archives/edgar/data/320193/000032019326000018/a8-kex991q3202606272026.htm`. This is a primary-source SEC filing (furnished under Item 2.02/9.01), not a third-party aggregator or the triggering Telegram post, and is used here exactly as the 2026-07-30 HOOD session used its own subject company's newly-filed 10-Q — the earliest primary-source document containing the quarter's full financial statements. `yfinance` was not separately attempted, per the now-repeatedly-documented `curl_cffi` TLS failure in this environment (see 2026-07-06 AAPL, 2026-07-30 HOOD, and multiple other recent sessions).

**TTM reconstruction (window: Q4 FY2025 + Q1 FY2026 + Q2 FY2026 + Q3 FY2026, i.e. through 2026-06-27):**

Q3 FY2025, Q4 FY2025 (derived), Q1 FY2026, and Q2 FY2026 figures are carried forward unchanged from the 2026-07-06 session's own SEC-XBRL-sourced reconstruction (re-verified present in this session's fresh 8-K's prior-year comparative columns, which match exactly). Q3 FY2026 is new this session, from the 8-K above; its D&A/OCF/CapEx quarterly figures aren't separately disclosed and are derived by subtracting the already-established H1 FY2026 (Q1+Q2) figures from the freshly-disclosed 9-month FY2026 YTD figures.

| Line item ($M) | Q4 FY25 (derived) | Q1 FY26 | Q2 FY26 | Q3 FY26 (new) | **TTM total** |
|---|---|---|---|---|---|
| Revenue | 102,466 | 143,756 | 111,184 | 109,417 | **466,823** |
| Net Income | 27,466 | 42,097 | 29,578 | 29,789 | **128,930** |
| Gross Profit | 48,341 | 69,231 | 54,781 | 54,770 | **227,123** |
| Operating Income (EBIT) | 32,427 | 50,852 | 35,885 | 35,695 | **154,859** |
| D&A | 3,127 | 3,214 | 3,439 | 3,320 *(derived)* | **13,100** |
| Pretax income | 32,804 | 51,002 | 35,833 | 36,267 | **155,906** |
| Income tax expense | 5,338 | 8,905 | 6,255 | 6,478 | **26,976** |
| Operating cash flow | 29,728 | 53,925 | 28,702 | 34,369 *(derived)* | **146,724** |
| CapEx | 3,242 | 2,373 | 1,971 | 2,455 *(derived)* | **10,041** |

*(Q3 FY2026 D&A/OCF/CapEx derived as: 9-month-FY2026-YTD figure from this session's 8-K [D&A $9,973M, OCF $116,996M, CapEx $6,799M] minus H1 FY2026 [Q1+Q2, both already-established XBRL figures] — e.g. D&A: 9,973 − (3,214+3,439) = 3,320.)*

TTM Free Cash Flow = $146,724M − $10,041M = **$136,683M**. TTM effective tax rate = $26,976M / $155,906M = **17.30%**. TTM EBITDA = $154,859M + $13,100M = **$167,959M**.

**Balance sheet (as of 2026-06-27, from this session's 8-K):** Cash $39,544M; Marketable securities (current $22,855M + non-current $84,118M) = $106,973M; **liquid assets total $146,517M**. Commercial paper $1,997M + Term debt (current $11,007M + non-current $71,340M) = **Total debt $84,344M**. Total shareholders' equity $107,520M.

**Cross-check against the triggering post's headline figures (not used as an input, confirmation only):** revenue $109,417M ≈ "$109.42B" ✓; diluted EPS $2.02 = "$2.02" ✓; gross margin 54,770/109,417 = 50.05% ≈ "50.1%" ✓ (Apple's own release rounds to 50.1%); iPhone $54,252M ≈ "$54.25B" ✓; Services $30,739M ≈ "$30.74B" ✓; Mac $10,352M ≈ "$10.35B" ✓; Greater China $18,816M ≈ "$18.82B" ✓. All independently confirmed from the 8-K itself.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | AAPL data (refreshed) | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FY2021–FY2025 unchanged from 2026-07-06 (FCF-positive every year: $92.953B, $111.443B, $99.584B, $108.807B, $98.767B). TTM FCF (through 2026-06-27, this session) also strongly positive at **$136,683M**. | **PASS — does not fire.** |
| **Net Debt/EBITDA over threshold (2.5× standard)** | Net debt = Total debt $84,344M − liquid assets $146,517M = **−$62,173M (net cash)**. TTM EBITDA = $167,959M. Net Debt/EBITDA = **−0.37×**. | **PASS — does not fire (net cash, unchanged).** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years** | FY history unchanged (FY2021 98.18%, FY2022 111.66%, FY2023 102.67%, FY2024 116.08%, FY2025 88.17% — all comfortably above 70%). TTM (new) = 136,683/128,930 = **106.0%**. | **PASS — does not fire.** |

No hard disqualifier fires — same as 2026-07-06. AAPL's outcome is again decided entirely by the weighted score.

### 3.2 Sub-scores

**Profitability (25%)** — Net Margin (TTM) = 128,930/466,823 = **27.62%** → NetMargin_Component = clamp((27.62/30)×100) = **92.06**. ROIC: NOPAT = TTM EBIT × (1 − eff. tax rate) = 154,859 × (1 − 0.1730) = **$128,064M**. Invested Capital = Total Debt ($84,344M) + Equity ($107,520M) − liquid assets ($146,517M) = **$45,347M**. ROIC = 128,064/45,347 = **282.4%** → ROIC_Component = clamp((282.4/30)×100) = clamp(941.4) = **100.0** (clamped — same structural driver as 2026-07-06: decades of buybacks have shrunk book equity far below TTM NOPAT, a real and disclosed feature of Apple's capital structure, not a data error). Profitability_Score = (92.06+100.0)/2 = **96.03** (no FCF-positivity cap — every year on record is FCF-positive).

**Margins (15%)** — Gross Margin (TTM) = 227,123/466,823 = **48.66%**. GrossMargin_Score = clamp((48.66/80)×100) = **60.82**. No +10 structural-trend bonus (margin has been above the 40% bonus-eligibility ceiling throughout the lookback, consistent with the 2026-07-06 finding). **Rule 6 normalization note:** Apple's own Q3 FY2026 release discloses the quarter's 50.1% gross margin "includ[ed] a favorable impact of approximately 2 percentage points from tariff refunds" — a one-off, not a durable margin improvement. Since Q3 FY2026 is only one of the four quarters in this TTM window (≈23.4% revenue weight), a rough back-out of that one-off (2pp × 0.234 ≈ 0.47pp) would put normalized TTM Gross Margin at ≈48.19% and GrossMargin_Score at ≈60.24 — a 0.58-point sub-score difference, ≈0.09 points at the 15% weight on the final Quality Score. Immaterial to the outcome (see §3.3's much larger 3.4-point gate margin); flagged per Rule 6 rather than silently absorbed, not separately recomputed into the primary score below.

**Growth (20%)** — **Primary methodology (fiscal-year basis, consistent with the 2026-07-06 AAPL session and this framework's other new-position sessions, e.g. HOOD):** Revenue 3yr CAGR uses the most recent **complete** fiscal year vs. 3 years prior. FY2026 does not close until 2026-09-26 and is therefore not yet a complete fiscal year — so the base years are **unchanged from 2026-07-06**: FY2022 $394.328B → FY2025 $416.161B (both directly filed 10-K figures, re-verified via SEC XBRL this session) = (416,161/394,328)^(1/3) − 1 = **+1.81%/yr**. Base = clamp((1.81/25)×100) = **7.25**.

**TAM-expansion / pricing-power modifier — fresh Q3 FY2026 evidence, independently sourced (not from the trigger post):** the acceleration flagged as a "flagged judgment call" in the 2026-07-06 session is now **materially confirmed, not just directionally suggested**: 9-month FY2026 YTD revenue is $364,357M vs. $313,695M in the same period of FY2025, **+16.15% YoY** — a sharp step-up from FY2025's already-positive +6.4% full-year growth, and Q3 FY2026 alone grew **+16.4% YoY** (109,417 vs. 94,036). Every reported segment grew double-digits YoY this quarter (iPhone +21.7%, Mac +28.6%, Services +12.1%, and "double-digit revenue growth... in every geographic segment" per Apple's own release) — a broader-based acceleration than the Services-only mix-shift story credited last session. **+10 applied** (same direction as 2026-07-06, now on stronger evidence). Growth_Score (primary, FY-basis) = 7.25 + 10 = **17.25**.

> **Flagged methodology ambiguity — material to the outcome, surfaced for human review rather than resolved unilaterally.** [quality-scoring.md](../framework/quality-scoring.md) specifies "Revenue 3yr CAGR%" without stating whether it should be computed on a fiscal-year or trailing-twelve-month (TTM) basis. This session's fresh TTM revenue ($466,823M) vs. the TTM figure from **3 years earlier** (independently reconstructed via SEC XBRL quarterly deltas: Q4 FY2022 [derived, $90,146M] + Q1–Q3 FY2023 [$117,154M + $94,836M + $81,797M] = **$383,933M**, TTM ending ~2023-07-01) gives a **TTM-basis 3yr CAGR of +6.73%/yr** — nearly 4× the FY-basis figure, because it captures the just-reported quarter's re-acceleration instead of being anchored to FY2025 as the "most recent complete year." Under TTM-basis, Growth_Score would be clamp((6.73/25)×100) + 10 = 26.94 + 10 = **36.94** instead of 17.25 — and, worked through §3.3 below, **this single methodology choice is the difference between a 76.6 FAIL and an 80.5 PASS.** This session uses the **FY-basis figure as primary**, for consistency with the identical calculation basis used in every other session in this repo (2026-07-06 AAPL itself, and HOOD's FY2022→FY2025 growth calc) — switching to a more generous basis specifically because it flips a borderline result is exactly the kind of ad hoc, outcome-driven discretion Rule 0/"no black-box outputs" is designed to prevent. But this ambiguity is now demonstrably outcome-determinative (not just a rounding nuance) and is flagged explicitly for a `decisions/`-level framework clarification, analogous to the 2026-06-20 PEG clean-earnings ruling that followed DUOL being scored inconsistently across sessions.

**Balance Sheet (15%)** — Net Debt/EBITDA = −0.37× (§3.1). BalanceSheet_Score = clamp(100×(1−(−0.37)/4)) = clamp(109.25) = **100.0**.

**Moat Signal (15%)** — re-checked all 5 signals against fresh Q3 FY2026 disclosures and current third-party data:

| Signal | Fresh evidence checked this session | Verdict |
|---|---|---|
| Market share stable/growing | Apple captured a **record 20% global smartphone shipment share for a Q2-calendar quarter** (= Apple's fiscal Q3 2026) per Counterpoint Research, growing iPhone shipments **+3% YoY even as the total market fell 11% YoY** to its lowest Q2 level since 2013 — Apple was "the only major OEM that avoided price hikes during the quarter." **Nuance flagged:** Samsung retook the overall #1 vendor rank this quarter (24% vs. Apple's 20%, on aggressive Galaxy S26 promotions) — a change from the picture in the 2026-07-06 session, which had cited Apple provisionally atop Q1 2026 rankings. The signal as defined ("stable or growing," not "#1 ranked") is about Apple's own share trajectory, which continued to grow YoY against a shrinking market — credited TRUE, with the Samsung-retake context shown for balance rather than omitted. | **TRUE** (nuance flagged) |
| Brand premium | ~71% share of the global $600+ premium smartphone segment (Counterpoint, 2024 baseline — unchanged citation from 2026-07-06) reaffirmed via 2026 secondary commentary describing Apple's "record quarter reinforc[ing] its grip on the premium segment at a moment when mid-range and budget brands are absorbing the worst of the [memory-chip] crisis." Not independently re-measured to decimal precision this session — same proxy-evidence flag as before. | **TRUE** (flagged as proxy evidence, unchanged) |
| Network effect | Apple's CFO Kevan Parekh stated on the Q3 FY2026 earnings call (2026-07-30) that the installed base of **over 2.5 billion active devices reached another all-time high across all major product categories and geographic segments**, with the wearables installed base also hitting a new all-time high — fresh, direct confirmation from the company's own investor communication, same mechanism (App Store ecosystem two-sided-marketplace dynamics) credited in 2026-07-06. | **TRUE** |
| Switching costs | Same documented mechanism as 2026-07-06 (iMessage ~1B MAU, iCloud data/photo/backup migration friction, cross-device Continuity/Find My/purchased-content lock-in; ~92% retention / ~4% annual Android-switch rate per a secondary aggregator source) — a structural, slow-moving mechanism not tied to a single quarter's results, not independently re-sourced this session. Same secondary-aggregator sourcing caveat as before. | **TRUE** (carried forward, unchanged) |
| Scale cost advantage | This session's own 8-K data: Apple's Products-segment gross margin (9-month FY2026 basis) = (272,629−163,810)/272,629 = **39.92%**. Xiaomi's own disclosed Q1 2026 smartphone-hardware gross margin **fell to 10.1%** (from 12.4% a year earlier), per Xiaomi's own reported results (Quartr summary), pressured by memory-chip costs up >300%. The margin gap **widened to ~4×** (vs. the ~3× gap cited in the 2026-07-06 session using FY2025 Products margin of 36.8% vs. Xiaomi's then-~10.9%) — a real, cited, apples-to-apples hardware-segment comparison. | **TRUE** |

Moat_Score = (5/5)×100 = **100.0** (unchanged from 2026-07-06, refreshed evidence).

**FCF Quality (10%)** — FCF/NI (TTM) = 136,683/128,930 = **106.01%** → clamp(((1.0601−0.40)/0.60)×100) = clamp(110.02) = **100.0**.

### 3.3 Final weighted Quality Score

```
Quality Score = (96.03 × 0.25) + (60.82 × 0.15) + (17.25 × 0.20) + (100.0 × 0.15) + (100.0 × 0.15) + (100.0 × 0.10)
              = 24.008 + 9.123 + 3.450 + 15.000 + 15.000 + 10.000
              = 76.581 → 76.6 (rounded to nearest 0.1)
```

**76.6 < 80.0 — fails the gate, by 3.4 points.** This is a marginal **improvement** over the 2026-07-06 session's 76.2 (+0.4), driven by fresher TTM Profitability/Margins/FCF-Quality data, but the Growth sub-score itself — the dominant driver both times — is mechanically **unchanged** at 17.25, because the FY-basis 3-year CAGR is still anchored to FY2025 as the most recent *complete* fiscal year. Despite an unambiguously strong, accelerating quarter, Apple's fiscal year doesn't close until 2026-09-26, so this specific input hasn't yet moved.

**Sensitivity checks (transparency only, per this framework's precedent):**

| Scenario | Growth_Score | Moat_Score | Quality Score | Gate (80.0+) |
|---|---|---|---|---|
| **Primary (as scored above)** | 17.25 | 100.0 | **76.6** | **FAIL by 3.4** |
| No Growth modifier (0 instead of +10) | 7.25 | 100.0 | 74.6 | FAIL by 5.4 |
| Moat 4/5 (Market Share signal dropped, given Samsung's #1 retake) | 17.25 | 80.0 | 73.6 | FAIL by 6.4 |
| Both of the above (most conservative combined reading) | 7.25 | 80.0 | 71.6 | FAIL by 8.4 |
| **TTM-basis Growth CAGR instead of FY-basis** (§3.2's flagged ambiguity) | 36.94 | 100.0 | **80.5** | **PASS by 0.5** |
| TTM-basis Growth CAGR, no modifier | 26.94 | 100.0 | 78.5 | FAIL by 1.5 |

**The outcome is robust to every discretionary call in this session except one:** switching the Growth sub-score's revenue-CAGR basis from fiscal-year to trailing-twelve-month, which is not what this session (or its 2026-07-06 predecessor, or the HOOD precedent) actually used, but is a plausible reading of quality-scoring.md's unspecified "Revenue 3yr CAGR%" wording. See the flagged methodology note in §3.2 — this is surfaced explicitly rather than silently decided, since it is now demonstrably outcome-determinative for a real candidate.

### Result: **Phase 01 FAIL (primary methodology)**

Per [new-position.md](../.claude/commands/new-position.md) step 2: *"If it's below 80.0... stop and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed.**

---

## 4. Recommendation

**PASS.** Do not open a position. No Rate Environment Gate, no Phase 02 valuation score, no fair-value work, and no order setup — consistent with a name that does not clear this framework's Quality Score gate under the methodology used consistently across this repo.

This is, again, not a verdict that Apple had a weak quarter — the opposite is true. Revenue grew +16.4% YoY (its fastest quarterly growth in years), every product category and every geography posted double-digit growth, EPS grew +29% YoY, operating cash flow set a June-quarter record, and the installed base hit a fresh all-time high. Four of the six Quality Score axes remain at or near this framework's ceiling (Balance Sheet 100.0, Moat 100.0, FCF Quality 100.0, Profitability 96.03). The gate miss is again driven almost entirely by the **Growth** sub-score (17.25) and, to a smaller extent, **Margins** (60.82) — both structural consequences of Apple's scale (a ~$451–467B TTM-revenue company mechanically cannot sustain the 25%+ multi-year CAGR this sub-score is calibrated to reward) **and**, this session specifically, of a **methodology quirk**: the Growth sub-score's fiscal-year-basis calculation can't yet "see" the very re-acceleration this earnings report demonstrates, because FY2026 isn't a complete fiscal year until late September. As flagged in §3.2/§3.3, a defensible alternate (TTM-basis) reading of the same underlying data would flip this to a PASS at 80.5 — a genuinely close call this session did not have the authority to resolve unilaterally in either direction, so it defaulted to the methodology already used consistently across this repo's prior sessions (including AAPL's own) rather than switching bases in the direction that happens to favor entry.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Mechanical trigger (the one most likely to resolve the FY-basis vs. TTM-basis ambiguity in Apple's favor):** Apple's **FY2026 Form 10-K** (fiscal year ends 2026-09-26; historically filed ~5 weeks later, so expected ~early November 2026). Once FY2026 is a complete fiscal year, the FY-basis 3yr CAGR base years roll forward to FY2023→FY2026 — a window that will include the current re-acceleration rather than excluding it, and is very likely (based on the 9-month YTD trend already in hand) to produce a materially higher Growth_Score under the *same* primary methodology used in this session, without needing to resolve the TTM-vs-FY ambiguity at all.
- **Sooner, if warranted:** Apple's fiscal Q4 2026 results (the seasonally-important December-quarter holiday results are actually FY2027 Q1 for Apple's fiscal calendar — but Apple's **FY2026 Q4** results, covering the September quarter, are expected ~late October 2026 alongside or just before the 10-K) — another mandatory Rule 9 quarterly re-check regardless of the above.
- **Framework-process trigger (not ticker-specific):** the flagged methodology ambiguity in §3.2 (fiscal-year vs. TTM basis for the Growth sub-score's "Revenue 3yr CAGR%") is recommended for explicit resolution in `quality-scoring.md` via a `decisions/`-level entry before it next becomes outcome-determinative for another large, decelerating-by-scale incumbent — this session intentionally did not make that call unilaterally.
- **Other Rule 9 events:** a guidance revision, management change, material M&A, or a >15% stock-price move with no identified cause (today's −6.07% move is itself well short of that threshold).
- Absent any of the above, future Telegram mentions of AAPL should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## 7. Watchlist Actions

- Updated `watchlist/not-in-portfolio/AAPL/AAPL-2026-07-06.md` with a **new dated row (2026-07-31)** — the Quality Score changed (76.2 → 76.6) and a Rule 9 earnings-release trigger fired, both independently sufficient per [watchlist/README.md](../watchlist/README.md)'s "significant change" criteria, even though the action category (Phase 01 FAIL / PASS) is unchanged. Filename kept as `AAPL-2026-07-06.md` per this framework's existing within-file accumulation convention (same pattern as `MU-2026-06-20.md`) — a new dated row is added inside the existing file, and per this task's explicit instruction to add a "new dated row only if the score/action/scored-status changed," which it did (score moved, and the underlying reasoning materially changed even though the FAIL verdict itself did not).
- Checked `watchlist/STALE.md` for an AAPL row: **none found** — AAPL was never flagged stale (both its 2026-07-06 and current scores are computed under the current 2026-06-29 methodology), so no stale-clearing action needed.

---

## 8. Data Gaps Flagged (summary — none blocked scoring)

1. **Apple's fiscal Q3 2026 Form 10-Q had not yet been filed** as of this session (confirmed via SEC EDGAR submissions API) — used the company's own 8-K/Exhibit 99.1 earnings press release instead, a primary SEC filing furnished the same day as the earnings release, containing the full unaudited financial statements. Every figure independently cross-checked against the triggering Telegram post's headline numbers (all matched); the post itself was not used as a data source.
2. **Q3 FY2026 standalone D&A/OCF/CapEx were not directly disclosed** (only 9-month YTD figures) — derived by subtraction against the already-established H1 FY2026 figures (§2). Low materiality: this only affects the TTM FCF/EBITDA figures used in already-clamped-at-100.0 sub-scores (Balance Sheet, FCF Quality), so even a modest revision would not change the outcome.
3. **`yfinance` not attempted** — documented, repeatedly-confirmed `curl_cffi` TLS environment failure (see 2026-07-06 AAPL, 2026-07-30 HOOD, and numerous other recent sessions). SEC XBRL/8-K used directly instead, per this task's provided workaround.
4. **Methodology ambiguity (Growth sub-score's CAGR basis) is outcome-determinative this session** — not a missing-data gap, but a genuine gap in [quality-scoring.md](../framework/quality-scoring.md)'s specification, flagged explicitly in §3.2/§3.3 and §6 rather than resolved unilaterally.

None of these gaps blocked scoring — every input used in the Quality Score calculation was ultimately obtained and cross-validated across independent sources.

---

## Glossary

- **8-K** — The "current report" a US public company must file with the SEC within days of a material event; Apple's Q3 FY2026 earnings press release was furnished via an 8-K exhibit ahead of the fuller 10-Q, and used as this session's primary financial-statement source.
- **CAGR (Compound Annual Growth Rate)** — The smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx (Capital Expenditure)** — Money spent buying or upgrading physical assets (factories, equipment, tooling).
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every EDGAR filer (Apple's is 0000320193).
- **D&A (Depreciation & Amortization)** — The non-cash expense spreading the cost of long-lived assets over time.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and profitability ratios.
- **Effective tax rate** — The actual percentage of pretax income paid as tax in a period — used here to convert TTM EBIT into NOPAT for the ROIC calculation.
- **FCF (Free Cash Flow)** — Cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score — none fired for AAPL this session.
- **Invested Capital** — The total capital (debt + equity, netted for cash) deployed in a business — the denominator of this session's ROIC calculation.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; a negative figure means net cash, as found for AAPL here.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. AAPL scores 76.6 this session (up from 76.2 on 2026-07-06), still below the gate.
- **ROIC (Return on Invested Capital)** — How efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input.
- **Rule 6** — This framework's "normalize before you value" discipline — strip out one-time items (e.g. the tariff-refund benefit flagged in §3.2) before drawing conclusions from a reported figure.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure — the basis used throughout most of this session's sub-scores, and the center of the flagged Growth sub-score methodology ambiguity.
- **XBRL (eXtensible Business Reporting Language)** — The SEC's structured, machine-readable data-tagging format for filed financial statements — the source of the independently-reconstructed prior-period figures in this session, pulled via the SEC's `companyconcept` API.

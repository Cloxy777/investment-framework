# NEW POSITION — HIMS (Hims & Hers Health, Inc.) — 2026-08-11

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — unattended run)
**Date:** 2026-08-11 (Tuesday)
**10Y US Treasury Yield:** Not fetched this session — evaluation stops at the Phase 01 Quality Score gate (§3) before the Rate Environment Gate would otherwise apply, same precedent as the 2026-08-07 NET and 2026-08-10 KSPI sessions.
**Current HIMS portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** [HIMS-2026-06-12.md](../watchlist/not-in-portfolio/HIMS/HIMS-2026-06-12.md), addendum dated 2026-07-09 — Quality Score **49.1/100.0, FAIL** under the 2026-06-29 methodology. That addendum's own "Next review trigger" named "HIMS's Q2 2026 earnings release (expected 10 August 2026)" as the critical re-check.
**Sector:** Healthcare — Direct-to-Consumer Telehealth & Wellness (personalized subscription health platform: weight loss/GLP-1, sexual health, dermatology, mental health)
**Filer type:** US SEC filer, CIK 0001773751, Delaware-incorporated, calendar fiscal year.
**IBKR contract used:** `contract_id` 466188387 — NYSE, symbol HIMS, description "HIMS & HERS HEALTH INC," `country_code` US — same contract confirmed in the 06-12/07-09 sessions.
**First-use jargon decode:** see closing Glossary (§9) — several new terms this session, added to [glossary.md](../framework/glossary.md) before being cited here.

---

## §0. Why this session exists — trigger source

**Trigger:** A Telegram post on `FinnInvestChannel` (post `FinnInvestChannel/3079`, ~07:00 UTC 2026-08-11) quoted CEO Andrew Dudum discussing the Novo Nordisk partnership and a Wegovy tablet launch, claiming US revenue +16%, international revenue +17%, and total revenue +38% growth. This matches the shape of a Rule 9 earnings/results-event claim, and lands one day after the 07-09 addendum's own named "next review trigger" (HIMS Q2 2026 earnings, expected 10 August 2026).

**Per Rule 0 / CLAUDE.md, no figure from the Telegram post is used as financial data below.** Every number in this session is independently re-sourced from HIMS's own SEC filings (8-K Exhibit 99.1 and the full 10-Q), cross-checked against the SEC's structured XBRL company-facts API. The independent verification below is deliberately built as a claim-by-claim corroboration table, exactly so any gap between the Telegram post and the primary filing is visible rather than silently smoothed over:

| Telegram claim | Independent verification against primary SEC filings |
|---|---|
| Q2 2026 earnings were released, with CEO commentary | ✅ **Confirmed.** HIMS filed an 8-K (Items 2.02/9.01, accession `0001773751-26-000161`) and a full 10-Q (accession `0001773751-26-000163`) on **2026-08-10**, both covering the quarter ended **2026-06-30 (Q2 2026)** — one day before the Telegram post. This is a genuine, dated, primary-sourced Rule 9 earnings trigger. |
| Total revenue +38% YoY | ✅ **Confirmed almost exactly.** Q2 2026 revenue $753.214M vs. Q2 2025 $544.833M = **+38.24% YoY** (SEC XBRL `RevenueFromContractWithCustomerExcludingAssessedTax`, 10-Q). |
| US revenue +16% YoY | ✅ **Confirmed.** US revenue not separately XBRL-tagged, but the 8-K Exhibit 99.1 press release states US revenue of $621.8M, **+16% YoY**. |
| International revenue +17% YoY | ❌ **NOT confirmed — materially contradicted.** The 8-K Exhibit 99.1 reports "Rest of World" revenue of **$131.4M, up 1,641% YoY** (vs. $7.5M in Q2 2025) — not +17%. The filing attributes essentially all of this growth to the **Eucalyptus Health acquisition** (Hepsiburada platform), which closed 2 June 2026 and is now consolidated for a nearly-full quarter against a Q2 2025 base that barely included it. This is a genuine, material discrepancy between the Telegram post's headline claim and the primary filing — flagged explicitly, not smoothed over. It doesn't change this session's approach (Telegram figures are never used as data regardless), but is worth noting as a data-quality flag on the trigger source itself. |
| CEO Andrew Dudum discussed the Novo Nordisk partnership and a Wegovy tablet launch | ⚠️ **Not independently corroborated in the primary filed documents.** Neither the 8-K Exhibit 99.1 earnings press release nor the full Q2 2026 10-Q (including its MD&A) mentions "Novo Nordisk" or "Wegovy" anywhere. Both documents do describe HIMS's own strategic shift toward "branded GLP-1 receptor agonist medications" in general terms, without naming a specific manufacturer partner or product. If this commentary was made, it was most likely on the earnings call (not itself an SEC filing, and not checked this session — a genuine, flagged data gap, see §8) rather than in the furnished/filed materials. This claim is neither confirmed nor actively disproven by what was checked — just not corroborated by the primary source this session used. |

**Net effect:** the trigger is real — HIMS did report Q2 2026 earnings, one day before the Telegram post, and the headline total/US revenue growth figures check out almost exactly. But the post's international-growth figure is wrong by roughly 100×, and its specific Novo Nordisk/Wegovy-tablet attribution is unconfirmed by the primary filed record. This session proceeds on the confirmed earnings event as the Rule 9 trigger, using only independently-sourced figures throughout.

---

## §1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$29.49** | IBKR `get_price_snapshot`, `contract_id` 466188387, `last.price`, timestamp Unix 1786436041 = **2026-08-11 08:14:01 UTC** (pre-market — NYSE regular session opens 13:30 UTC / 9:30 ET; this is a genuine live pre-market print, not a stale prior-day close) |
| Cross-check | $29.44, ts 08:11:29 UTC (same snapshot call ~3 min earlier) — consistent | IBKR |
| Prior session close (2026-08-10, per daily bar) | $29.60 | IBKR `get_price_history`, `ONE_DAY` bars, `outside_rth: true` |
| ⚠️ IBKR `change`/`prior-close` fields | `prior-close: {}` (empty — unavailable this pre-market snapshot); the `change` field on an earlier snapshot implied a prior close of ~$31.77 (Friday 2026-08-07's close of $31.67, one trading day stale — Monday 2026-08-10 is skipped) rather than Monday's actual $29.60 close. **Not used** — flagged as a vendor-data-quality note (same category of issue as the KSPI dividend-yield staleness flag in the 2026-08-10 session), resolved instead by reading Monday's close directly off the daily price-history bar. | IBKR |
| 52-week range | $13.74 (low) – $65.29 (high) | IBKR `misc-statistics` |
| Dividend yield | 0.0% | IBKR `dividend-yield` |

**$29.49 is used as the live price for all context below.** Since the Quality Score gate fails decisively (§3–§4), no fair-value/order-setup work is performed this session, so this price plays a limited role — primarily for the Rule 9 price-move check (§0-adjacent, see below) and general context.

**Price-move context (not a scored input, informational only):**
- vs. 06-12 session price ($28.87): **+2.15%**
- vs. 07-09 addendum price ($35.66): **−17.30%** — a >15% move, which would trigger Rule 9's "unexplained price move" category on magnitude alone. **Explained, not unexplained**: the move is fully consistent with the timing and content of the Q2 2026 earnings release confirmed in §0 (GAAP net loss widened materially, gross margin compressed further — see §2) — a documented, dated, primary-sourced cause, not a mystery move.
- Day-over-day (2026-08-10 close $29.60 → current $29.49): essentially flat (−0.37%), despite the prior day (earnings day itself) showing a wide intraday range ($29.20–$34.70) — consistent with an initial post-earnings pop that fully reversed intraday as the market digested the GAAP net-loss miss.

---

## §2. Data Sourcing

All figures below are sourced directly from SEC EDGAR: the Q2 2026 8-K (Exhibit 99.1 earnings press release, accession `0001773751-26-000161`, filed 2026-08-10), the Q2 2026 10-Q (accession `0001773751-26-000163`, filed 2026-08-10, including its own condensed balance sheet — `R2.htm` — read directly rather than relying on a text-summarization pass), and the SEC's structured XBRL company-facts API (`data.sec.gov/api/xbrl/companyfacts/CIK0001773751.json`), cross-checked against three earlier quarterly 8-Ks (Q3 2025: accession `0001773751-25-000352`; Q4/FY2025: accession `0001773751-26-000019`; Q1 2026: accession `0001773751-26-000074`) for the non-GAAP Adjusted EBITDA figures XBRL doesn't carry (that metric is self-reported, not GAAP-tagged). Every dollar figure used in this session's Quality Score was independently pulled from a primary filing, not carried forward from the 07-09 addendum without re-verification — where a prior figure is reused (e.g. FY2023/FY2024 FCF), it was re-derived from the same XBRL source and cross-checked against the prior addendum's cited value (all matched, see §3.5).

**TTM window (rolls forward from the 07-09 addendum's window): Q3 2025 (Jul–Sep) + Q4 2025 (Oct–Dec) + Q1 2026 (Jan–Mar) + Q2 2026 (Apr–Jun)** — i.e. Q2 2025 rolls off and Q2 2026 rolls on, exactly as the framework's standard TTM-rolling convention requires.

### 2.1 TTM income statement, reconstructed from SEC XBRL company-facts ($M)

| | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 | **TTM sum** | Derivation note |
|---|---|---|---|---|---|---|
| Revenue | 598.976 | 617.818 | 608.104 | 753.214 | **2,578.112** | Q4'25 = FY2025 (2,347.637) − 9mo2025 (1,729.819) |
| Gross Profit | 442.058 | 444.435 | 396.787 | 480.803 | **1,764.083** | Q4'25 = FY2025 GP (1,733.378) − 9mo2025 GP (1,288.943) |
| Operating Income | 11.807 | 9.186 | (78.323) | (97.192) | **(154.522)** | Q4'25 = FY2025 op. income (105.613) − 9mo2025 (96.427) |
| Pretax Income | 12.223 | 18.353 | (101.551) | (92.633) | **(163.608)** | Q4'25 = FY2025 (123.924) − 9mo2025 (105.571) |
| Tax Benefit/(Expense) | (3.551)† | (2.248) | (9.436) | (6.343) | **(21.578)**† | †negative = a *benefit* here throughout (pretax loss); Q4'25 = FY2025 (−4.441) − 9mo2025 (−2.193) |
| Net Income | 15.774 | 20.601 | (92.115) | (86.290) | **(142.030)** | Check: Pretax − Tax = −163.608 − (−21.578) = −142.030 ✓ matches |
| D&A | 17.669 | 18.092 | 21.953 | 29.477 | **87.191** | Q3'25 = H1'25-cum-to-9mo (36.410) − H1'25 (18.741); Q4'25 = FY2025 (54.502) − 9mo (36.410) |
| Adjusted EBITDA (company non-GAAP, from each quarter's own 8-K) | 78.4 | 66.3 | 44.3 | 60.3 | **249.3** | Sourced from each quarter's Exhibit 99.1, not GAAP-tagged in XBRL |

```
TTM Gross Margin  = 1,764.083 / 2,578.112 = 68.425%
TTM Net Margin    = -142.030 / 2,578.112  = -5.509%
TTM GAAP EBITDA (Op. Income + D&A) = -154.522 + 87.191 = -67.331M  (negative — see §3.4 balance-sheet caveat)
```

### 2.2 What changed vs. the 07-09 addendum, and why

**Net loss widened, it did not turn positive.** Q2 2026 posted a GAAP net loss of **$86.290M**, swinging from Q2 2025's net income of **$42.505M**. This directly answers the 07-09 addendum's own stated "critical re-check": that addendum said the Profitability sub-score would stop floor-ing at 0.0 only "if Q2 2026 NI > $92.1M, reversing the Q1 2026 loss on a trailing basis" — instead, Q2 2026 added a *second* consecutive quarterly loss on top of Q1 2026's, deepening the TTM hole from −$13.235M (as of 07-09) to **−$142.030M** now. **This is the single most important finding of this session: profitability did not swing positive — if anything it swung further negative.**

**Gross margin continued compressing.** Q2 2026 GAAP gross margin was 63.8% (480.803/753.214), down from 76.3% in Q2 2025 — the same multi-quarter compression trend already flagged in the 06-12/07-09 sessions (82% → 79% → 74% → 65.3% → 63.8%), not a new development but a continuation. The Q2 2026 10-Q attributes part of this to $28.5M of restructuring-related charges embedded in cost of revenue (tied to the ongoing US weight-loss strategic pivot) and to the newly-consolidated, lower-margin Eucalyptus/Hepsiburada revenue.

**A large new debt issuance landed on the balance sheet.** HIMS priced $402.5M of 0.00%-coupon convertible senior notes due 2032 (conversion price ≈$29.53/share — notably close to today's $29.49 live price, i.e. the notes are close to at-the-money) via an 8-K filed 2026-05-21 (accession `0001193125-26-234847`) — this predates both the 06-12 and 07-09 sessions, but its balance-sheet effect only shows up now: the 07-09 addendum's balance-sheet figures were sourced from the Q1 2026 (31 Mar 2026) 10-Q, which closed *before* this note issuance. Convertible senior notes, net rose from $974.106M (Q1 2026) to **$1,365.299M** (Q2 2026) as a direct result. This is old news (not a new Rule 9 trigger), but it materially changes this session's Balance Sheet sub-score (§3.4).

**Two Eucalyptus-related liabilities appeared for the first time.** The Q2 2026 10-Q's balance sheet (`R2.htm`, read directly) shows, for the first time, a **Deferred acquisition payable** ($537.381M current + $165.624M noncurrent = $703.005M) and **Earn-out consideration** ($81.364M current + $81.600M noncurrent = $162.964M), both tied to the Eucalyptus Health acquisition that closed 2 June 2026 — consistent with, and quantifying, what the 07-09 addendum could only describe qualitatively. See §3.4 for why this matters to the Balance Sheet sub-score.

**Guidance was revised.** FY2026 guidance moved from **revenue $2.8B–$3.0B / Adjusted EBITDA $275M–$350M** (per the Q1 2026 8-K, cited in the 07-09 addendum) to **revenue $3.1B–$3.3B / Adjusted EBITDA $275M–$325M** (per this quarter's 8-K) — a genuine Rule 9 guidance-revision trigger, mixed in direction (revenue range raised, Adjusted EBITDA ceiling trimmed).

**A management change was disclosed.** An 8-K filed 2026-07-17 (Item 5.02, accession `0001773751-26-000149`) discloses Chief Accounting Officer **Irene Becklund's** resignation, effective **2026-10-09**, with an explicit statement of "no dispute or disagreement with the Company's accounting principles or practices or financial statements and disclosures," and a follow-on advisory agreement through July 2027. This post-dates the 07-09 addendum and is a genuine (if minor — CAO, not CEO/CFO) new Rule 9 management-change trigger. CEO Andrew Dudum and CFO Yemi Okupe are unchanged.

**The FDA's PCAC review occurred.** The Pharmacy Compounding Advisory Committee meeting flagged as "pending" in the 07-09 addendum convened 23–24 July 2026 and voted to recommend 6 of the 7 reviewed peptides (BPC-157, KPV, TB-500, MOTS-c, Semax, epitalon) for the Section 503A Bulk Drug Substances list — a favorable panel vote, though this only starts a formal rulemaking process (proposed rule, public comment, final determination) and does not itself legalize compounding; realistic availability is late 2027 at the earliest per contemporaneous reporting. **None of the 6 recommended peptides include semaglutide or tirzepatide** (HIMS's core GLP-1 franchise), so this remains a sector-relevant but not directly material development for HIMS, consistent with the 07-09 addendum's framing. *(Source: FDA advisory-committee calendar, STAT News, AJMC — sector context only, not used as a scored input.)*

---

## §3. Phase 01 — Quality Score (methodology version 2026-06-29, unchanged since the 07-09 addendum — no stale-score mark applies)

### 3.1 Hard disqualifier check

| Hard disqualifier | HIMS data (this session) | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FY2023 +$46.983M, FY2024 +$198.284M, FY2025 +$57.406M — all independently re-derived and confirmed this session directly from SEC XBRL (`NetCashProvidedByUsedInOperatingActivities` − `PaymentsToAcquireProductiveAssets`), matching the 06-12/07-09 sessions' cited figures exactly. TTM FCF is also positive: +$68.100M (Q3'25 +79.3, Q4'25 −2.6, Q1'26 +59.6, Q2'26 −68.2). | **PASS** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | Most recent 2 complete fiscal years (rolling window, per the 2026-08-05 clarification): FY2024 = 198.284/126.038 = **157.32%** (above 70%); FY2025 = 57.406/128.365 = **44.72%** (below 70%). Only 1 of the 2 years is below threshold — same conclusion as 07-09 (no new complete fiscal year exists to roll the window forward). | **PASS — does not fire** (only 1 of 2 years qualifies) |
| **Net Debt/EBITDA over its applicable threshold (2.5× standard)** | **Primary reading** (formal debt — convertible notes only): Net Debt = $1,365.299M − $609.811M cash − $231.237M AFS securities = **$524.251M**; ÷ TTM Adjusted EBITDA $249.3M = **2.10x** → under 2.5x. **Conservative cross-check** (+ the new $703.005M deferred acquisition payable, a fixed, non-contingent M&A obligation — see §2.2/§3.4): Net Debt = $1,227.256M ÷ $249.3M = **4.92x** → **would independently fire this disqualifier.** See §3.4 for full discussion of this judgment call. | **PASS on primary reading; would FAIL on the conservative reading** — flagged explicitly, doesn't change this session's outcome either way (§3.5) |

**No hard disqualifier fires under this session's primary reading**, consistent with the 06-12/07-09 sessions — HIMS proceeds to the full weighted score. The Net Debt/EBITDA judgment call is discussed fully in §3.4 and flagged as a genuine framework-definition gap worth the user's attention (in the spirit of the 2026-08-10 KSPI session's FCF/NI growth-lending carve-out flag), even though it is moot to this session's final recommendation (§3.5 shows the weighted score fails the 80.0 gate decisively regardless of which Net Debt/EBITDA reading is used).

### 3.2 Sub-score computations

**PROFITABILITY (25% weight):**
```
TTM Net Margin = -142.030 / 2,578.112 = -5.509%
  NetMargin_Component = clamp((-5.509/30)x100) = clamp(-18.36) = 0.0

Invested Capital = Convertible Notes ($1,365.299M) + Equity ($324.072M) - Cash ($609.811M) - AFS securities ($231.237M)
                 = $848.323M
TTM effective tax rate = TTM Tax Benefit / TTM Pretax Income = -21.578 / -163.608 = 13.19%
NOPAT = TTM EBIT x (1 - eff. tax rate) = -154.522 x (1 - 0.1319) = -$134.142M
ROIC = -134.142 / 848.323 = -15.81%
  Cross-check (standard 21% tax rate, since the effective rate here reflects a tax *benefit* on a pretax loss,
    same distortion this framework has flagged before for AMD/COIN-style loss-making periods):
    NOPAT = -154.522 x 0.79 = -$122.072M; ROIC = -122.072/848.323 = -14.39%
  Both readings decisively negative -- doesn't change the clamp.
  ROIC_Component = clamp((-15.81/30)x100) = clamp(-52.7) = 0.0

Profitability_Score = (0.0 + 0.0) / 2 = 0.0   (no FCF-positivity cap needed -- already at the floor;
                                                  FCF-positive 3yr confirmed in §3.1 regardless)
```
**Profitability_Score = 0.0**

**MARGINS (15% weight):**
```
TTM Gross Margin = 1,764.083 / 2,578.112 = 68.425%
GrossMargin_Score = clamp((68.425/80)x100) = 85.53
```
No structural-trend bonus (only applies when gross margin is *below* 40% and expanding — HIMS's is well above 40% and, per §2.2, *contracting* for the fifth straight quarter). **Margins_Score = 85.53** — down from the 07-09 addendum's 89.65, continuing the trend the prior session already flagged.

**GROWTH (20% weight):**
```
Revenue 3yr CAGR (FY2022 $526.916M -> FY2025 $2,347.637M) = (2,347.637/526.916)^(1/3) - 1 = 64.55%
Growth_Score(raw) = clamp((64.55/25)x100) = clamp(258.2) = 100.0 (saturates -- same base year, no new complete FY since 07-09)
```
TAM-expansion modifier: documented evidence exists (Eucalyptus Health/Hepsiburada international consolidation now generating real revenue — $131.4M in Q2 2026 alone, up from $7.5M a year ago; the company's own 10-Q language on shifting toward "branded GLP-1" products) — **+10 would apply, but is moot**, already capped at 100.0. Structural-deceleration modifier: **does not apply** — Q2 2026 revenue growth (+38.24% YoY) *reaccelerated* sharply from Q1 2026's +4% YoY, the opposite of a deceleration signal. **Growth_Score = 100.0**

### 3.3 Balance Sheet (15% weight) — full detail on the debt-definition judgment call

```
PRIMARY (formal debt only -- convertible senior notes, net of cash and short-term AFS securities,
  consistent with the definition used in the 06-12/07-09 HIMS sessions and the 2026-08-10 KSPI/2026-08-07 NET sessions):
    Net Debt = $1,365.299M - $609.811M - $231.237M = $524.251M
    Net Debt/EBITDA = $524.251M / $249.3M (TTM Adjusted EBITDA) = 2.10x
    BalanceSheet_Score = clamp(100 x (1 - 2.10/4)) = clamp(100 x 0.4744) = 47.43
```

**Two flagged caveats on this primary figure:**

1. **EBITDA basis.** The denominator uses the company's own non-GAAP Adjusted EBITDA ($249.3M TTM), not a GAAP-derived figure, because **TTM GAAP EBITDA (Operating Income + D&A) is actually negative (−$67.331M)** this session — computing Net Debt/EBITDA off a negative GAAP EBITDA produces a mathematically nonsensical ratio (Net Debt ÷ a negative number), so it is not used, consistent with the 07-09 addendum's identical caveat and Non-GAAP treatment elsewhere in this framework (see the Adjusted EBITDA glossary entry).

2. **Whether the new Eucalyptus-related deferred acquisition payable should count as "debt."** Quality-scoring.md's Net Debt/EBITDA formula doesn't define exactly which balance-sheet liabilities count as "debt." This session's primary reading (financial borrowings only) is consistent with how this exact ticker's own prior sessions, and other tickers' sessions (KSPI, NET), have always applied the formula. But a reasonable alternative reading would include the **$703.005M Deferred acquisition payable** — a *fixed*, non-contingent dollar obligation from the completed Eucalyptus acquisition, economically closer to a promissory note than to a routine trade payable — in "debt":

```
CONSERVATIVE (+ Deferred acquisition payable, excluding the contingent Earn-out consideration):
    Net Debt = $524.251M + $703.005M = $1,227.256M
    Net Debt/EBITDA = $1,227.256M / $249.3M = 4.92x   -- exceeds the 2.5x hard-disqualifier threshold

MOST CONSERVATIVE (+ Earn-out consideration too, though it is contingent/fair-valued rather than fixed):
    Net Debt = $1,227.256M + $162.964M = $1,390.220M
    Net Debt/EBITDA = $1,390.220M / $249.3M = 5.58x
```

**This session uses the PRIMARY reading as its score of record**, for consistency with established precedent across this ticker's own history and the framework's other recent sessions, and because deferred/contingent M&A consideration is not classified as "debt" on HIMS's own GAAP balance sheet (it sits in separate line items, distinct from "Convertible senior notes, net"). But this is a genuine, material judgment call — under the conservative reading, HIMS would fail the Quality Score gate on a **hard disqualifier** rather than (as this session concludes) on the weighted score alone. **Flagged explicitly as a candidate framework clarification** (should material, fixed-dollar deferred M&A consideration count toward "debt" in the Net Debt/EBITDA gate?) for the user's consideration in a future `decisions/` entry — in the same spirit as the 2026-08-10 KSPI session's "growth-lending carve-out" flag. **It does not change this session's ultimate recommendation** (§3.5 — the weighted score fails by 36+ points regardless of which reading is used).

**BalanceSheet_Score = 47.43** (primary reading, used in §3.5's final computation) — down sharply from the 07-09 addendum's 79.4, driven almost entirely by the $402.5M note issuance (§2.2).

### 3.4 Moat Signal (15% weight)

Carried forward from the 07-09 addendum's evidence base, refreshed against this quarter's fresh disclosures:

| Signal | Evidence | Verdict |
|---|---|---|
| Market share / scale | 2.9M subscribers as of Q2 2026, **+19% YoY** (8-K Exhibit 99.1, primary source) — continues the largest-DTC-telehealth-platform positioning already cited in 07-09 (FierceHealthcare, 2M+ patients). | **TRUE** |
| Brand premium / pricing power | Monthly Revenue per Average Subscriber (MRPAS) rose 21% YoY in Q2 2026 ($92 vs. $76) but only 4% YoY over H1 2026 ($84 vs. $81) — the filing does not break out how much of this reflects price increases on existing products vs. mix-shift toward higher-ARPU branded weight-loss subscriptions. The *same* quarter's gross margin compressed 12.5pp (76.3%→63.8%), which argues against clean pricing power (a company genuinely raising prices without volume loss would generally see margin hold or expand, not compress) — the more parsimonious read is monetization growth driven by product mix, not price increases with static costs. Kept **FALSE**, consistent with the 07-09 addendum's conservative read, with this quarter's margin data as additional counter-evidence, not new supporting evidence. | **FALSE** |
| Network effect | No two-sided marketplace mechanism found or newly disclosed this quarter. | **FALSE** |
| Switching costs | Same internally-contradictory third-party evidence gap as 07-09 (DrugPatentWatch's own caveat that "the moat is not yet deep") — no primary-source confirmation found. | **FALSE** |
| Scale cost advantage | No cost-per-unit data vs. competitors found or newly disclosed. | **FALSE** |

**Moat_Score = (1/5) × 100 = 20.0** — unchanged from the 07-09 addendum.

### 3.5 FCF Quality (10% weight)

```
TTM FCF/NI: TTM FCF (+$68.100M) / TTM NI (-$142.030M) is not economically meaningful (negative denominator) --
  same "not meaningful" treatment as the 07-09 addendum. Using FY2025 (most recent complete fiscal year) as primary:
  FCF/NI = $57.406M / $128.365M = 44.72%
  FCFQuality_Score = clamp(((0.4472 - 0.40)/0.60)x100) = clamp(7.87) = 7.87
  Cross-check, FY2024: $198.284M / $126.038M = 157.32% (unchanged, well above threshold -- consistent with §3.1)
```
**FCFQuality_Score = 7.87** — essentially unchanged from the 07-09 addendum's 7.8.

### 3.6 Final weighted Quality Score

```
Quality Score = (0.0 x 0.25) + (85.53 x 0.15) + (100.0 x 0.20) + (47.43 x 0.15) + (20.0 x 0.15) + (7.87 x 0.10)
              = 0.000 + 12.830 + 20.000 + 7.114 + 3.000 + 0.787
              = 43.73  -> rounds to 43.7
```

**Quality Score = 43.7 / 100.0 — fails the 80.0+ gate by 36.3 points**, and is **worse** than the 07-09 addendum's 49.1 (a −5.4 point decline). The gate does not open.

**Sensitivity (Moat only — the sole qualitative judgment call in this computation):**

| Moat reading | Moat_Score | Quality Score | Gate result |
|---|---|---|---|
| Conservative (0/5 — drop market share too) | 0.0 | 40.7 | FAIL |
| **Primary (this session)** | **20.0** | **43.7** | **FAIL** |
| Generous (2/5 — add brand premium) | 40.0 | 46.7 | FAIL — still 33.3pts short |

**Also robust to the Balance Sheet judgment call from §3.4**: even on the *primary* (more favorable) Net Debt/EBITDA reading, the weighted score still fails by 36.3 points; the conservative reading would fail the gate even more directly, via the hard disqualifier itself. Neither judgment call this session made is close to decisive to the outcome.

### Result: **Phase 01 FAIL**

No Rate Environment Gate, no Phase 02 valuation score, and no Composite Score computed — consistent with the strict gate rule in quality-scoring.md.

---

## §4. Gate Result — Phase 02 / Composite Score / Order Setup NOT computed

Per quality-scoring.md: *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all... Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."* HIMS scores 43.7 — **this session stops here.** No fair-value work, no buy/sell/stop levels, no position sizing.

---

## §5. Recommendation

# **PASS — Quality Score gate FAILS at 43.7/100.0, a decline from the 07-09 addendum's already-failing 49.1. No order setup, no fair-value work, no BUY/TRIM/EXIT action.**

The task-setting context for this session flagged that HIMS's prior 49.1 score was driven largely by a floored Profitability sub-score (negative TTM net margin/ROIC), and asked whether a confirmed Q2 2026 earnings report would show profitability swinging "sharply and structurally positive." **It did not — the opposite happened.** Q2 2026 added a second consecutive quarterly GAAP net loss ($86.290M, following Q1 2026's $92.115M), pushing TTM Net Income from −$13.235M (as of 07-09) to **−$142.030M** now. Profitability remains floored at 0.0, exactly as before, but now backed by a materially worse trailing number. Layered on top of that: (1) gross margin compression continued for a fifth straight quarter (76.3%→63.8% YoY this quarter alone), pulling the Margins sub-score down slightly (89.65→85.53); and (2) a $402.5M convertible-note issuance (closed May 2026, landing on the balance sheet for the first time this quarter) roughly tripled Net Debt/EBITDA (0.82x→2.10x), pulling the Balance Sheet sub-score down sharply (79.4→47.43). Growth (100.0, capped), Moat (20.0), and FCF Quality (7.87) are all essentially unchanged.

The business itself is not without real positives independently confirmed this session — revenue growth reaccelerated to +38% YoY (vs. +4% in Q1 2026), subscriber count grew to 2.9M (+19% YoY), and FY2026 revenue guidance was raised (though its Adjusted EBITDA ceiling was trimmed). But none of that reaches this framework's central, decisive gap: **HIMS remains GAAP-unprofitable, with the loss now widening rather than narrowing, and its balance sheet took on meaningfully more leverage this quarter.** The 80.0+ Quality Score gate exists specifically to keep a "good narrative, bad trailing financials" story like this one out of Phase 02 valuation work — see the **Value trap** glossary entry.

**No position opened. Nothing to log in `decisions/`** (per task instructions, a `decisions/` entry is only required if a position is actually opened).

---

## §6. Watchlist Actions

- Created `watchlist/not-in-portfolio/HIMS/HIMS-2026-08-11.md` (new dated entry) — warranted under [watchlist/README.md](../watchlist/README.md#significant-change--when-does-a-new-dated-entry-get-created)'s explicit rule that a Rule 9 fundamental-event trigger firing (confirmed Q2 2026 earnings, §0/§2) warrants a fresh dated entry even though the score/action category is unchanged (Phase 01 FAIL both before and after) — the reasoning behind the number has materially changed (an actual, worse-than-before earnings print now backs the score).
- No stale-score mark applies — methodology version (2026-06-29) is unchanged since the 07-09 addendum, and HIMS carries no numeric score computed under an older version.

---

## §7. Next Review Trigger

- **HIMS's Q3 2026 earnings release.** Based on this year's cadence (Q1 reported 11 May, Q2 reported 10 Aug), Q3 2026 would be expected roughly early-to-mid November 2026. This is now the standing mandatory Rule 9 re-check — specifically worth watching whether the net-loss trend seen in Q1 and Q2 2026 continues, stabilizes, or reverses, and whether gross margin compression (now 5 straight quarters) finally levels off.
- **Mechanical trigger, sharpened this session:** Profitability (0.0) and Balance Sheet (47.43, down from 79.4) are now the two largest drags, alongside Moat (20.0) and FCF Quality (7.87). The single most direct path to a materially different result remains sustained, GAAP-basis profitability — not yet observed, and now trending the wrong direction for a second straight quarter.
- **A framework clarification worth the user's consideration** (flagged in §3.4, not decided by this session): whether a material, fixed-dollar deferred acquisition payable from a completed M&A deal should count as "debt" in the Net Debt/EBITDA hard-disqualifier check. Under a conservative reading, this would already independently fail HIMS's gate today via the hard disqualifier rather than the weighted score.
- Other standard Rule 9 events: a further guidance revision, a CEO/CFO-level management change (the CAO departure disclosed this session is a minor one), material new M&A, a macro/regulatory shift with direct GLP-1 relevance (the July PCAC vote did not touch semaglutide/tirzepatide), or a further >15% unexplained price move from $29.49.

---

## §8. Data Gaps Flagged (summary — none blocked scoring)

1. **Earnings-call commentary (Novo Nordisk partnership / Wegovy tablet launch) not independently verified.** As detailed in §0, neither the 8-K earnings press release nor the full 10-Q mentions Novo Nordisk or Wegovy by name — this session did not have access to (and did not attempt to source) an earnings-call transcript, which is not itself an SEC filing. If this CEO commentary was made, it may exist only there. Non-blocking: no scored input in this session depends on it, since forward-looking management commentary is explicitly excluded from the Quality/Valuation Score engines per this framework's design (see "Why Forward Guidance Is Not a Sub-score," valuation-scoring.md).
2. **Net Debt/EBITDA debt-definition judgment call** (§3.4) — flagged prominently above, not resolved by existing framework text, doesn't change this session's outcome.
3. **CFO status** — confirmed unchanged (Yemi Okupe) only by the *absence* of any Item 5.02 8-K naming a CFO change since the last session, not by an affirmative same-day confirmation from a company source. Standard practice for this framework; noted for completeness.
4. **Q2 2026 earnings-call date/time and any post-call analyst commentary** — not sourced this session; only the furnished/filed written materials (8-K, 10-Q) were used, consistent with Rule 0's "primary filing over secondary commentary" discipline.

None of these gaps blocked scoring.

---

## §9. Glossary

New terms added to [framework/glossary.md](../framework/glossary.md) this session (in alphabetical position) before being cited here: **AFS (Available-for-Sale) securities**, **Deferred acquisition payable**, **Earn-out consideration**, **MRPAS (Monthly Revenue per Average Subscriber)**, **PCAC (Pharmacy Compounding Advisory Committee)**.

| Term | Meaning |
|---|---|
| **8-K** | A US public company's filing disclosing a material event (here, quarterly earnings, a management-change disclosure, and a debt-issuance disclosure) to the SEC promptly after it occurs. |
| **10-Q** | The quarterly financial-disclosure report a US public company files with the SEC between annual 10-Ks — this session's primary balance-sheet/cash-flow source for Q2 2026. |
| **Adjusted EBITDA** | A company's own non-GAAP variant of EBITDA that strips out items management deems non-recurring (e.g. restructuring charges) — used here as the Net Debt/EBITDA denominator because TTM *GAAP* EBITDA is negative this session (§3.4), not directly comparable to a GAAP-derived figure. |
| **AFS (Available-for-Sale) securities** | A balance-sheet classification for liquid debt securities held as a cash-management buffer; HIMS's $231.2M of short-term AFS securities is netted into cash for this session's Net Debt calculation. |
| **CAGR** | Compound Annual Growth Rate. |
| **CAO (Chief Accounting Officer)** | A company's senior accounting officer, typically the "Principal Accounting Officer" for SEC-reporting purposes — HIMS's CAO disclosed her resignation this session (§2.2), a minor Rule 9 management-change trigger. |
| **CIK (Central Index Key)** | The unique numeric identifier the SEC assigns to every EDGAR filer (HIMS's is 0001773751). |
| **Deferred acquisition payable** | A fixed-dollar liability for consideration owed on a completed acquisition, not yet paid in cash — $703.0M on HIMS's balance sheet this quarter, tied to the Eucalyptus Health acquisition, and central to this session's Net Debt/EBITDA judgment call (§3.4). |
| **DTC (Direct-to-Consumer)** | A business model selling directly to end customers rather than through intermediaries — HIMS's core telehealth model. |
| **Earn-out consideration** | A contingent (performance-dependent) liability for additional M&A purchase-price payments — $163.0M on HIMS's balance sheet this quarter, distinct from the (fixed) deferred acquisition payable above. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization. |
| **FCF (Free Cash Flow) / FCF/NI conversion ratio** | Cash generated after running and maintaining the business; FCF ÷ Net Income, an earnings-quality check — HIMS's FY2025 ratio (44.72%) remains below the 70% threshold, though not for 2 consecutive years (§3.1). |
| **GAAP** | Generally Accepted Accounting Principles — the standard this framework scores off, as opposed to a company's own non-GAAP "Adjusted" figures. |
| **Gross Margin** | Gross Profit ÷ Revenue — HIMS's continued to compress this quarter (§2.2/§3.2). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted score; none independently fires for HIMS under this session's primary reading (§3.1), though one would under a conservative Net Debt/EBITDA reading (§3.4). |
| **Invested Capital** | Debt + Equity − Cash (and cash-equivalents), the ROIC denominator; $848.323M for HIMS this session. |
| **Moat** | A durable competitive advantage; scored 20.0 (1 of 5 signals) for HIMS this session, unchanged from 07-09. |
| **MRPAS (Monthly Revenue per Average Subscriber)** | HIMS's own monetization metric; rose 21% YoY in Q2 2026 but only 4% YoY over H1 2026 — ambiguous evidence on pricing power, discussed in §3.4. |
| **Net Debt/EBITDA** | This framework's primary balance-sheet-risk gate; 2.10x on this session's primary reading, 4.92x–5.58x on more conservative readings that count Eucalyptus-related deferred/contingent liabilities as debt (§3.4). |
| **Net Margin** | Net Income ÷ Revenue; TTM −5.51% for HIMS this session, worse than the 07-09 addendum's −0.56%. |
| **NI (Net Income)** | Accounting profit after all expenses, interest, and taxes. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **PCAC (Pharmacy Compounding Advisory Committee)** | An FDA advisory committee that convened 23–24 July 2026 to review peptides for the compounding bulk-substances list — occurred during this session's review window, sector-relevant but not HIMS-GLP-1-specific (§2.2). |
| **Pretax income** | Net Income + Tax Expense (or − Tax Benefit) — the base an effective tax rate is computed against; HIMS's TTM pretax income (−$163.608M) reflects a tax *benefit*, not expense, on its pretax loss. |
| **Quality Score** | This framework's 0–100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02. HIMS scores 43.7 this session, down from 49.1 in the 07-09 addendum. |
| **Rate Environment Gate** | The pre-Phase-02 check comparing Earnings Yield to the 10-Year Treasury; not reached this session. |
| **ROIC** | Return on Invested Capital; −15.81% for HIMS this session (TTM, effective-tax-rate basis), decisively negative under any reasonable tax-rate assumption. |
| **Rule 0** | Always fetch a live price before any valuation work — never infer price, and never treat a Telegram post's figures as financial data. |
| **Rule 9** | This framework's list of events that force an immediate re-valuation: earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move — three of these fired between the 07-09 addendum and this session (earnings, guidance revision, management change), see §2.2. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results — this session's window is Q3 2025–Q2 2026, rolled forward one quarter from the 07-09 addendum's Q2 2025–Q1 2026 window. |
| **Value trap** | A stock that looks statistically attractive on a narrative basis but stays weak because underlying business quality is deteriorating — the risk this framework's 80.0+ Quality Score gate is specifically designed to surface, cited in §5's recommendation. |
| **XBRL (eXtensible Business Reporting Language)** | The SEC's structured, machine-readable data-tagging format for filed financial statements — this session's primary sourcing method via `data.sec.gov`'s API. |

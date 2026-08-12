# NEW POSITION (Telegram-Triggered Q2 FY2026 Earnings Re-score) — Tencent Holdings (0700-HK) — 2026-08-12

**Task type:** NEW POSITION (full re-evaluation of an existing not-in-portfolio watchlist entry — not a fresh candidate discovery)
**Date:** 12 Aug 2026
**Trigger:** `/telegram-scan` (Routine 6) — bolshegold channel, post #9959, ~09:58 UTC 2026-08-12, claimed Tencent's Q2 FY2026 results (net income ~68.4B yuan, revenue ~204.8B yuan, +11% YoY). Per CLAUDE.md Rule 0 and the `/telegram-scan` command, **the Telegram post's numbers were treated only as a trigger, never as financial input** — every figure below is independently re-sourced from Tencent's own primary filings and wire mirrors. This also lands squarely inside the 2026-07-06 session's own documented "Next review trigger": Q2 FY2026 earnings, mid-August 2026, Rule 9 mandatory re-score.
**10Y US Treasury Yield:** 4.72% (2026-08-10 print — most recent available; 2026-08-11/08-12 not yet posted to FRED as of this session)
**Rate Regime Modifier (Step 2):** +5
**Current 0700-HK portfolio weight:** 0% — confirmed not held ([holdings.md](../portfolio/holdings.md))
**Last review on record:** 22.0 / Quality 75.5 / Composite 23.3 (2026-07-06, [session](2026-07-06-new-position-0700-hk.md); [watchlist entry](../watchlist/not-in-portfolio/0700-HK/0700-HK-2026-07-06.md)) — current methodology (2026-06-29), not stale.

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EBITDA = operating profit before depreciation/amortization; EV/EBIT = enterprise value ÷ operating profit; PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; CAGR = compound annual growth rate; pp = percentage points; EY = earnings yield (1 ÷ PE); NOPAT = net operating profit after tax; ROIC = return on invested capital; TAM = total addressable market; TTM = trailing twelve months; NCI = non-controlling interests; IFRS = International Financial Reporting Standards (Tencent's actual reporting basis — see Data Gap/Correction #6 below); MAU = monthly active users.*

---

## 1. Live Price (Rule 0) & Listing Choice

**Listing choice: HK primary listing (0700.HK / SEHK:700, HKD), not the TCEHY US OTC ADR** — same convention as every prior session (TCEHY pricing flagged unreliable). All calculations below are in HKD (converted from Tencent's RMB-denominated financial statements).

| Field | Value | Source |
|---|---|---|
| **Live price used (0700.HK)** | **HKD 461.60** | IBKR `get_price_history` (contract_id 152791428, SEHK, symbol "700", `re-verified via search_contracts this session — unchanged`), 1-day bar close for 2026-08-12 | 
| Cross-check | HKD 461.60 (exact match) | Yahoo Finance chart endpoint (`query1.finance.yahoo.com/v8/finance/chart/0700.HK`), `regularMarketPrice` |
| Prior close | HKD 470.80 (2026-08-11) | IBKR `get_price_history` / Yahoo, agree exactly |
| Day range | HKD 456.20 – 467.20 | IBKR / Yahoo |
| 52-week range | HKD 411.00 – 683.00 | Yahoo Finance chart endpoint (`fiftyTwoWeekLow` / `fiftyTwoWeekHigh`) — unchanged from 2026-07-06 |
| USD/HKD | 7.8469 | WebSearch, 2026-08-12 |
| CNY/HKD | 1.1631 | WebSearch, 2026-08-12 (mid-market) |
| Shares outstanding | **8.98B** (8,980,000,000) | stockanalysis.com, dated "updated 2026-08-05" — see Data Gap #1 |
| Market cap (at HKD 461.60) | HKD 4,145,168M | Computed: 8.98B × 461.60 |
| Analyst consensus PT (12-month) | RMB 595.65 (≈HKD 692.66 at CNY/HKD 1.1631) — 45 analysts, "Buy" | MarketScreener, 2026-08-12 — bull-case sanity anchor only, never a score input |

**Important timing flag — the price above does NOT yet reflect the earnings reaction.** IBKR's `get_price_snapshot` returned no live quote this session (market closed — HKEX regular session ends 16:00 HKT / 08:00 UTC; this session ran ~12:00–13:30 UTC, after close). Tencent's Q2 2026 results were released **after** the 2026-08-12 HK market close (board meeting/announcement, per multiple sources), so today's closing price of HKD 461.60 is the price *going into* the results, not a post-earnings price. The market's reaction (if any) will first show up at HKEX's next open (2026-08-13 09:30 HKT). This is flagged explicitly rather than treated as "stale" — it is genuinely the most current live/settled print available under Rule 0 at the time of this session, and both IBKR and Yahoo agree on it exactly.

---

## 2. Q2 FY2026 Earnings — Primary-Source Confirmation

**Confirmed via primary source: YES.** Tencent Holdings Limited announced unaudited consolidated results for the quarter ended 30 June 2026 ("2Q2026") on **12 August 2026** (Hong Kong). Primary basis for this session:

- **Tencent's own Q2 2025 results PDF** (`static.www.tencent.com/uploads/2025/08/13/56af6c5c98acdc7bd757a7bd208d8189.pdf`) — fetched and read in full (all 9 pages, including the condensed income statement, comprehensive income statement, other financial information table, and full balance sheet) — used as the YoY comparative base (2Q2025 actuals), and as the template confirming Tencent's own EBITDA/Net-cash/Capex formula definitions (footnotes a–d).
- **PRNewswire's "TENCENT ANNOUNCES 2026 SECOND QUARTER RESULTS"**, mirrored verbatim (same PRNewswire copy) via The Manila Times (`manilatimes.net/2026/08/12/.../tencent-announces-2026-second-quarter-results/2403765`) and Sina Hong Kong's PRNewswire-Asia syndication — same sourcing pattern as the prior session's Q1 2026 citations. This mirror reproduces the full condensed consolidated income statement (2Q2026 / 2Q2025 / 1Q2026 columns), the Other Financial Information table (EBITDA, Adjusted EBITDA, Net cash, Capex), and the free-cash-flow definition sentence verbatim.
- **Independent cross-checks**, all agreeing on the headline figures to the exact million: MarketScreener's news wire ("China's Tencent posts 11% second-quarter revenue rise, profit misses estimates" — net profit 56.0bn RMB vs. 61.8bn RMB consensus, a ~9.4% miss); a First Squawk real-time headline tweet (Rev 204.79B, Oper profit 67.28B, Net income 56.02B, Capex 52.78B — all exact matches); Longbridge's news summary (profit attributable RMB56.02bn, +0.7%, revenue RMB204.8bn, +11%).

**Note on the earlier Telegram rumor's accuracy:** the bolshegold post's "~68.4B yuan net income, ~204.8B yuan revenue, +11% YoY" turns out to match the officially-confirmed **non-IFRS** net income attributable (RMB68,415M) and revenue (RMB204,785M, +11%) almost exactly. This is coincidental accuracy, not vindication of the practice — the framework's Rule 0 discipline (independently re-source, never trust the post) is what allows catching, rather than assuming, this kind of match. It's also worth noting the rumor's "net income" figure quietly used the flattering non-IFRS number rather than the IFRS net income attributable to shareholders (RMB56,022M, +0.7% YoY, which **missed** analyst consensus by ~9.4%) — exactly the kind of self-reported-metric framing this framework's Rule 0 and "Why Forward Guidance Is Not a Sub-score" discipline exists to see through.

**No primary PDF for the Q2 2026 release itself could be located this session** (multiple URL-pattern guesses and searches for `static.www.tencent.com/uploads/2026/08/...` failed to resolve; one candidate URL returned a non-earnings Illustrator-generated PDF, not the actual release). All Q2 2026 figures below are sourced from the PRNewswire-mirror re-publication (which reproduces Tencent's own tables verbatim, same convention as prior sessions using wire mirrors) rather than the primary PDF directly — flagged as a minor sourcing-tier note, not a data-quality concern, given the 4-way independent cross-validation above.

---

## 3. Data Gathered — Fresh TTM Build (ended 30 June 2026)

### Quarterly & annual source figures (RMB millions, as officially reported)

| Line | FY2025 | Q1 2026 | Q2 2026 | Q2 2025 | Q1 2025 |
|---|---|---|---|---|---|
| Revenue | 751,766 | 196,458 | 204,785 | 184,504 | 180,022 |
| — VAS | — | 96,110 | 98,414 | 91,368 | 92,133 |
| — Marketing Services | — | 38,171 | 43,565 | 35,762 | 31,853 |
| — FinTech & Business Services | — | 59,885 | 60,286 | 55,536 | 54,907 |
| — Others | — | 2,292 | 2,520 | 1,838 | 1,129 |
| Gross profit | 422,593 | 111,265 | 118,433 | 105,013 | 100,493 |
| Gross margin | 56% | 57% | 58% | 57% | 56% |
| Operating profit (IFRS) | 241,562 | 67,375 | 67,276 | 60,104 | 57,566 |
| Non-IFRS operating profit | 280,656 | 75,627 | 75,636 | 69,248 | 69,320 |
| Net income attributable (IFRS) | 224,842 | 58,093 | 56,022 | 55,628 | 47,821 |
| Non-IFRS net profit attributable | 259,626 | 67,905 | 68,415 | 63,052 | 61,329 |
| **Diluted EPS (IFRS, RMB)** | **24.153** | **6.302** | **6.104** | **5.996** | **5.129** |
| Capital expenditures | 79,198 | 31,936 | 52,784 | 19,107 | 27,476 |
| Free cash flow | 182,600 | 56,700 | **(13,800)** | ~43,000 | 47,100 |
| EBITDA | 310,767 | 84,167 | 85,776 | 79,467 | 73,817 |
| Net cash (company-disclosed) | 107,145 | 146,860 | **58,191** | 74,592 | 90,229 |

Sources: [Q2 2025 results (Tencent IR PDF, full 9-page primary source, fetched and read this session)](https://static.www.tencent.com/uploads/2025/08/13/56af6c5c98acdc7bd757a7bd208d8189.pdf); [Q2 2026 results (PRNewswire, mirrored via Manila Times / Sina HK)](https://www.manilatimes.net/2026/08/12/tmt-newswire/pr-newswire/tencent-announces-2026-second-quarter-results/2403765); FY2025/Q1 2026/Q1 2025 figures carried forward from the 2026-07-06 session's own primary-source build (unchanged, re-verified against this session's Q2 2025 PDF re-read — the Q1 2025 column in that PDF, 47,821 net income / 5.129 diluted EPS / 180,022 revenue, matches the 2026-07-06 session's figures exactly, a clean cross-check).

**Free cash flow, exact definition (per Tencent's own release, verbatim):** *"negative free cash flow of RMB13.8 billion for 2Q2026, as net cash generated from operating activities of RMB52.7 billion was more than offset by capital expenditure payments of RMB59.3 billion, media content payments of RMB5.0 billion and lease liability payments of RMB2.2 billion."* Adjusting for prepayment timing, the company states free cash flow "would have been RMB37.6 billion" on an adjusted basis — same adjusted-FCF convention Tencent used in the 2026-07-06 session's Q1 2026 figures. **This session uses the unadjusted, as-reported FCF (−13,800 for Q2 2026) for the TTM roll-forward**, consistent with how every prior quarter in the table above is also unadjusted — using the adjusted figure only for Q2 2026 would inconsistently mix definitions across the roll-forward.

### TTM roll-forward (ended 30 June 2026) — FY2025 + (Q1 2026 + Q2 2026) − (Q1 2025 + Q2 2025), shown in full

```
Revenue        = 751,766 + (196,458+204,785) − (180,022+184,504) = 751,766 + 401,243 − 364,526 = 788,483
Gross profit   = 422,593 + (111,265+118,433) − (100,493+105,013) = 422,593 + 229,698 − 205,506 = 446,785
                 → Gross margin = 446,785 / 788,483 = 56.66%
EBIT (IFRS)    = 241,562 + (67,375+67,276) − (57,566+60,104)     = 241,562 + 134,651 − 117,670 = 258,543
Net income     = 224,842 + (58,093+56,022) − (47,821+55,628)     = 224,842 + 114,115 − 103,449 = 235,508
                 → Net margin = 235,508 / 788,483 = 29.87%
Diluted EPS    =  24.153 + (6.302+6.104) − (5.129+5.996)         =  24.153 + 12.406 − 11.125   =  25.434
Capex          =  79,198 + (31,936+52,784) − (27,476+19,107)     =  79,198 + 84,720 − 46,583   = 117,335
FCF            = 182,600 + (56,700−13,800) − (47,100+43,000)     = 182,600 + 42,900 − 90,100   = 135,400
EBITDA         = 310,767 + (84,167+85,776) − (73,817+79,467)     = 310,767 + 169,943 − 153,284 = 327,426
```

All in RMB millions. **The FCF drop is the headline finding of this session** — TTM FCF fell from RMB192,200M (as of 31 Mar 2026, the 2026-07-06 session's figure) to **RMB135,400M** (as of 30 Jun 2026), a −29.6% swing, driven entirely by Q2 2026's capex payments (RMB59.3bn cash-basis / RMB52.8bn accrual-basis, +176% YoY) tied to the AI infrastructure buildout. See §7 (Owner Earnings) and §5 (FCF Quality) below for how this flows through the score.

### 5-year historical PE (reused, unchanged from 2026-07-06 session)

| Year | PE ratio |
|---|---|
| 2021 | 14.53 |
| 2022 | 14.18 |
| 2023 | 22.05 |
| 2024 | 18.70 |
| 2025 | 22.32 |

**5yr low = 14.18 | 5yr high = 22.32 | 5yr avg = 18.35** — not re-sourced this session since no new fiscal year has closed since 2026-07-06 (FY2026 is still in progress); the trailing 5-completed-fiscal-year window (2021–2025) is unchanged.

### FY2026/FY2027 consensus (MarketScreener, 45 analysts, 2026-08-12 — refreshed from the 07-06 session's pull)

| Metric | FY2026E | FY2027E |
|---|---|---|
| Diluted EPS (RMB) | **25.62** (was 25.84 on 07-06 — a small downward revision) | 28.66 |
| Revenue (RMB millions) | 825,783 | 903,276 |
| Net income (RMB millions) | 234,453 | 259,381 |

Cross-check: consensus net income ÷ consensus EPS = 234,453/25.62 ≈ 9,151M diluted shares — in the same ballpark as the 8.98B period-end shares outstanding figure below (a full-year weighted average sits above a shrinking period-end count, consistent with ongoing buybacks through the year).

---

## 4. Data Gaps, Corrections & Flags

1. **Shares outstanding disagreement persists across sources, same class of issue flagged 2026-07-06.** stockanalysis.com (8.98B, "updated 2026-08-05") is used as primary this session — most specific and recently dated. Morningstar shows 9.00B; Google Finance shows 9.52B — a real spread. Not resolved further; flagged again for the next `/rescore`/`/new-position` pass.
2. **Full 30 June 2026 balance sheet (borrowings, notes payable, total equity, non-controlling interests) could not be sourced from a primary or reliable source this session**, despite multiple targeted fetch/search attempts (the PRNewswire mirror's balance-sheet table was truncated after the current-assets section in every fetch attempt; the one Tencent-hosted PDF URL located resolved to an unrelated Illustrator-generated file, not the earnings release). **What IS confirmed, primary-sourced:** cash and cash equivalents (RMB206,930M) and term deposits (RMB214,275M current + RMB52,724M non-current = RMB267,000M total) as of 30 June 2026, plus the company's own directly-disclosed aggregate **Net cash position (RMB58,191M)** — this is what's used for the Balance Sheet sub-score (§5), which only requires Net Debt/EBITDA, not the full liabilities/equity breakdown. **What could NOT be sourced:** the borrowings/notes payable/total-equity/NCI line items needed for a fresh Net Invested Capital (ROIC denominator). Per this repo's "never invent" rule, **ROIC this session uses the 31 March 2026 balance sheet** (already primary-sourced in full in the 2026-07-06 session: Total Debt RMB386,805M, Total Equity RMB1,211,627M, Cash+Term Deposits RMB496,711M) as a labeled, one-quarter-stale stand-in — explicitly flagged in §5 below, not presented as a fresh 30-June figure. A stockanalysis.com "balance sheet" pull returned a Total Debt/Total Equity pair for this date, but its bottom-up "Net Cash (Debt)" reconciliation (−RMB12,924M, i.e. net *debt*) directly contradicts the company's own disclosed net *cash* of +RMB58,191M — the same "bottom-up reconstruction doesn't tie to the company's own number" pattern flagged as Data Gap #5 in the 2026-07-06 session — so that aggregator pull is **not used** here.
3. **Q2 2026 "Other gains/(losses), net" and the "Profit before income tax" / "Income tax expense" split could not be sourced** (present in the Q2 2025 PDF read in full this session, but not reproduced in any Q2 2026 mirror located). Two downstream effects, both flagged and bounded rather than invented:
   - **TTM D&A (used only for the Owner Earnings growth-capex trigger test, §7)** is approximated as EBITDA − EBIT (327,426 − 258,543 = 68,883), omitting the small "Other gains/losses, net" adjustment term in Tencent's own D&A-reconciliation formula. Bounding the missing Q2 2026 term against its full historical quarterly range (−RMB3,578M to +RMB1,253M) moves the resulting Growth CapEx ratio between roughly 37% and 42% — comfortably above the 30% Upgrade-1 trigger threshold across the entire plausible range, so the conclusion (Owner Earnings applies) is robust to this gap.
   - **TTM effective tax rate for NOPAT (§5 Profitability)** uses the most recently computable rate — 16.78%, TTM ended 31 March 2026 (from the 2026-07-06 session) — as a labeled stand-in, rather than a freshly-computed 30-June rate.
4. **5yr historical PE series reused unchanged** (see §3) — not a gap, just noted for clarity since no fresh sourcing was attempted.
5. **Shareholder-yield buyback component re-derived this session from Q2 2026's actual disclosed repurchase spend** (~37.4 million shares, ~HKD16.9 billion, per the results release) rather than reusing the 07-06 session's YoY net-share-count-reduction proxy — annualized as (16,900 ÷ market cap) × 4 = 1.63%/yr. A cleaner, more current, empirical figure, but flagged as a single-quarter rate annualized (not a guided or full-year-realized figure).
6. **Terminology correction.** The 2026-07-06 session (and earlier ones) labeled Tencent's primary reporting basis "GAAP" throughout (e.g. "Diluted EPS (GAAP, continuing ops)"). **Tencent actually reports under IFRS (International Financial Reporting Standards), not US GAAP** — its own press releases explicitly say "On an IFRS basis" / "On a non-IFRS basis." This session uses the correct "IFRS" / "non-IFRS" terminology throughout, matching Tencent's own primary-source labeling and this repo's existing [glossary.md](../framework/glossary.md) IFRS entry. This is a labeling correction only — the underlying figures in the 07-06 session were Tencent's actual IFRS figures, just mislabeled; nothing about that session's math changes.

---

## 5. Phase 01 — Quality Gate Re-verification (fresh TTM data)

| Check | Tencent TTM value | Threshold | Result |
|---|---|---|---|
| Gross margin | 56.66% (TTM to 30 Jun 2026) | >40% | ✅ PASS |
| Net margin | 29.87% (TTM, IFRS attributable) | >12% (valuation-scoring.md) / >15% (strategy.md) | ✅ PASS |
| ROIC | ~19.53% (TTM NOPAT ÷ 31-Mar-2026 NIC — see flag below) | >15% | ✅ PASS (flagged) |
| Revenue CAGR 3yr | 10.67% (FY2022 RMB554,552M → FY2025 RMB751,766M, unchanged — no new FY closed) | >8% | ✅ PASS |
| FCF positive 3+ consecutive years | FY2024 RMB155.3B, FY2025 RMB182.6B, TTM RMB135.4B — all positive (TTM markedly lower, see §3) | required | ✅ PASS (watch flag) |
| Net debt/EBITDA | Net **cash** RMB58.19B (TTM EBITDA RMB327.4B) → −0.178× | <2.5x | ✅ PASS (net cash, shrinking) |
| FCF/NI conversion | FY2024 80.0%, FY2025 81.2% (**both completed fiscal years**, >70%) — TTM (partial FY2026) 57.49% | >70% (fiscal-year hard-disqualifier test) | ✅ PASS on the hard-disqualifier test (fiscal-year basis) — ⚠️ but see below |

**Gate result: 8/8 PASS on the hard-disqualifier tests, using fresh TTM/fiscal-year data. No hard disqualifier fires.** Per the 2026-08-05 rolling-window clarification in [quality-scoring.md](../framework/quality-scoring.md), the FCF/NI hard disqualifier is tested against "the most recently completed fiscal years" — FY2024 (80.0%) and FY2025 (81.2%) are the two most recent, and both clear 70% comfortably, so the disqualifier does **not** fire even though the in-progress TTM/quarterly figure has fallen sharply (see below).

**ROIC calculation, shown in full, with the balance-sheet-staleness flag from Data Gap #2:**

```
NOPAT = EBIT × (1 − effective tax rate) = 258,543 × (1 − 0.1678) = 215,159   [tax rate: 31-Mar-2026 TTM rate, stand-in — Data Gap #3]
Net Invested Capital (31 Mar 2026 balance sheet, one quarter stale — Data Gap #2)
  = Total Debt (386,805) + Total Equity (1,211,627) − Cash+TermDeposits (496,711) = 1,101,721
ROIC = 215,159 / 1,101,721 = 19.53%
```

This clears the >15% bar with real margin even under conservative staleness assumptions (a materially higher or lower 30-June invested-capital base would need to move by tens of percent to flip the PASS/FAIL result at 19.53% vs. a 15% bar) — but is explicitly flagged as **not** a fresh 30-June-2026 calculation, per Data Gap #2.

**Quarter-level FCF/NI weakness — a real, documented flag, not yet a disqualifier.** Q1 2026 FCF/NI = 56,700/58,093 = 97.6% (healthy); **Q2 2026 FCF/NI = −13,800/56,022 = −24.6%** (negative — FCF itself went negative). This is **one** quarter below the 70% bar, not the "2 consecutive quarters" that would trigger Phase 04's continuous-monitoring flag ("FCF/Net Income <70% for 2 consecutive quarters w/o capex explanation: flag immediately") — but it is worth watching closely at the next quarterly re-score. The cause is well-documented and explicit: capital expenditure payments of RMB59.3bn in Q2 2026 alone (+176% YoY), tied directly to management's own repeatedly-stated AI infrastructure buildout (Hy3, WorkBuddy, CodeBuddy — see §8 Growth discussion), not an unexplained cash-flow deterioration. This is exactly the kind of "documented growth-capex explanation" the framework's disqualifier carve-out language anticipates — consistent with why the mechanical fiscal-year test doesn't fire.

---

## 6. Quality Score (2026-06-29 methodology, second computation for 0700-HK)

```
Profitability (25%):
  Net Margin (TTM, IFRS)  = 235,508 / 788,483 = 29.87%
  ROIC (see §5)            = 19.53%

  NetMargin_Component = clamp((29.87/30)×100, 0, 100) = 99.56
  ROIC_Component       = clamp((19.53/30)×100, 0, 100) = 65.10
  Profitability_Score  = (99.56 + 65.10) / 2 = 82.33   (no FCF cap — FCF-positive every year on record)

Margins (15%): Gross margin 56.66% (TTM) — still structurally above the 40% threshold, roughly flat
  vs. FY2025's 56% (a slight uptick, not a reversal — the multi-year expansion trend from FY2022's 43%
  to FY2025's 56% remains intact).
  GrossMargin_Score = clamp((56.66/80)×100, 0, 100) = 70.83
  (No +10 trend bonus — that bonus applies only when margin is still below 40% and improving; Tencent's
   margin already clears 40% comfortably, so the raw formula already credits the level, same as 07-06.)

Growth (20%): Revenue 3yr CAGR unchanged (no new FY closed since 07-06) = 10.67%
  Growth_Score = clamp((10.67/25)×100, 0, 100) = 42.68
  + 10 (documented TAM expansion / pricing power, reinforced this quarter, no structural-deceleration
    evidence — if anything growth reaccelerated): Marketing Services revenue +22% YoY in Q2 2026
    (vs. +20% in Q1) explicitly tied to further AI-driven ad-model upgrades (Tencent's own MD&A
    language); Domestic Games +17% YoY on evergreen-title strength; FinTech & Business Services +9%
    YoY. Headline total revenue growth accelerated to +11% YoY in Q2 2026 from +9% in Q1 2026 — the
    opposite of structural deceleration, so no −10 penalty applies (and the Q1 2026 timing-related
    softness flagged in the 07-06 session, attributed by management to a Spring Festival calendar
    shift, is now confirmed as the cyclical/timing effect it was described as, not a trend break).
  Growth_Score (with bonus) = 52.68

Balance Sheet (15%): Net cash (company-disclosed) RMB58,191M; TTM EBITDA RMB327,426M
  Net Debt/EBITDA = −58,191 / 327,426 = −0.178×  (net cash position, though sharply smaller than
  31-Mar-2026's RMB146,860M — a −60.4% quarter-over-quarter decline, driven by the same AI capex
  surge discussed throughout this session)
  BalanceSheet_Score = clamp(100×(1−(−0.178)/4), 0, 100) = clamp(104.45, 0, 100) = 100.0

Moat Signal (15%) — checklist, cited evidence, re-verified with fresh Q2 2026 data:
  ✓ Market share stable/growing — TRUE. Combined Weixin/WeChat MAU 1,439M, +2% YoY / +0.5% QoQ (Q2
     2026 report) — still the dominant, still-growing Chinese social/messaging platform.
  ✓ Brand premium — TRUE. Marketing Services revenue +22% YoY (accelerating from Q1's +20%) explicitly
     tied to "AI-driven improvements to our advertising platform" per Tencent's own MD&A — direct,
     strengthening pricing-power evidence this quarter.
  ✓ Network effect — TRUE. Weixin's multi-sided ecosystem (messaging + Mini Shops merchants +
     advertisers + Tencent Cloud enterprise tools) unchanged and still reinforcing itself.
  ✓ Switching costs — TRUE. Deep Weixin-ecosystem embedding for consumers and merchants unchanged
     from 07-06's finding — no new contradicting evidence found this session.
  ✗ Scale cost advantage — FALSE (not credited). No new company-specific, cited cost-per-unit data
     point found this session — same treatment as 07-06.
  Moat_Score = (4/5) × 100 = 80.0

FCF Quality (10%): FCF/NI TTM = 135,400 / 235,508 = 57.49%
  FCFQuality_Score = clamp(((0.5749 − 0.40)/0.60)×100, 0, 100) = 29.15
  This is the single largest driver of this session's Quality Score decline (69.6 → 29.15 on this
  sub-score alone) — see §5 for the fiscal-year-vs-TTM distinction that keeps this from being a hard
  disqualifier, and §3/§7 for the capex-driven cause.

Quality Score = 82.33×0.25 + 70.83×0.15 + 52.68×0.20 + 100.0×0.15 + 80.0×0.15 + 29.15×0.10
              = 20.5825 + 10.6245 + 10.536 + 15.0 + 12.0 + 2.915
              = 71.658 → rounds to 71.7
```

**Quality Score = 71.7 — FAILS the 80.0+ gate, by a wider margin than 2026-07-06 (8.3 points short, vs. 4.5 points short last time).**

**Hard disqualifier check: none fire** (see §5 — the FCF/NI weakness is a TTM/quarterly phenomenon, not yet a fiscal-year one).

**Why this quarter's Quality Score fell rather than rose.** Four of the six sub-scores actually held steady or improved slightly (Profitability 81.65→82.33, Balance Sheet 100.0→100.0, Moat 80.0→80.0, Margins 70.5→70.83, Growth 52.7→52.68 — essentially flat). **The entire net decline (75.5→71.7, a 3.8-point drop) is attributable to the FCF Quality sub-score alone (69.6→29.15, a 40.5-point collapse in that sub-score, worth −4.05 points once weighted at 10%)** — driven mechanically by TTM FCF falling from RMB192.2B to RMB135.4B on a near-flat TTM Net Income (235.5B vs. 235.1B a quarter ago), as Q2 2026's capex payments (RMB59.3bn, +176% YoY) hit the cash-flow statement. This is a **real, documented, capex-driven** effect tied explicitly to management's own repeatedly-stated AI infrastructure investment cycle — not a sign of deteriorating core-business cash generation (Net Income and Non-IFRS Operating Profit both grew YoY this quarter). It is exactly the situation this framework's Upgrade 1 (Owner Earnings) exists to handle for the *valuation* score (see §7) — but the Quality Score's FCF Quality sub-score is deliberately **not** Owner-Earnings-adjusted (it scores the FCF/NI conversion ratio specifically, as a check on *accounting-profit quality*, independent of *why* capex is high) — so this quarter's capex surge mechanically pulls the Quality Score further from the 80.0 gate even though the underlying investment thesis (AI reinvestment funded by a still-growing, still-profitable core business) is arguably intact or even strengthening.

---

## 7. Fast Grower (Upgrade 3 — PEG) Determination

**Test: EPS growth >15% for 3+ consecutive years, on a clean/non-distorted base.** Extending the corrected, consistent, all-IFRS diluted EPS series from 07-06 with the fresh TTM figure:

| Period | Diluted EPS (IFRS, RMB) | YoY growth | >15%? |
|---|---|---|---|
| FY2022 | 19.341 | — | — |
| FY2023 | 11.887 | **−38.55%** | ❌ No (sharp decline) |
| FY2024 | 20.486 | **+72.35%** | ✅ Yes |
| FY2025 | 24.153 | **+17.90%** | ✅ Yes |
| TTM (ended 30 Jun 2026) | 25.434 | **+5.30%** (vs. FY2025) | ❌ No |

The FY2023 collapse still breaks the "3+ consecutive years" requirement outright, and the fresh TTM figure now also fails the >15% test on its own (Q2 2026's flat-to-down EPS growth — see §6 — pulls the trailing growth rate to +5.3%, well under 15%).

**Determination: 0700-HK does NOT meet the Fast-Grower test, now on two independent grounds** (the FY2023 break, and the TTM figure itself). **PEG's 15% weight is redistributed to EV/EBIT** (40% total), same conclusion as both prior sessions.

---

## 8. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test** (using the Forward PE computed in §9 below)
```
Forward PE = HKD 461.60 / HKD 29.80 (FY2026E EPS converted) = 15.490×
EY     = 1 ÷ 15.490 = 6.4558%
Spread = EY − 10Y Treasury = 6.4558% − 4.72% = +1.7358%
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** (+1.74%, above threshold) → **no additive** (Step 1 = 0).

**Step 2 — Rate Regime Modifier**
10Y = 4.72% → "3.5–5%" bracket → **+5**

**Total Rate Modifier = +5** (same direction/size as 2026-07-06, spread narrowed slightly as forward PE ticked up).

---

## 9. Phase 02 — Full Valuation Score Calculation

**Owner Earnings (Upgrade 1) applicability check — shown explicitly, and the key methodology flip this session:**
```
TTM Capex = 117,335 (RMB millions)
TTM D&A (maintenance-capex proxy, approximated as EBITDA − EBIT — Data Gap #3) = 327,426 − 258,543 = 68,883
Growth Capex = 117,335 − 68,883 = 48,452
Growth Capex % of total = 48,452 / 117,335 = 41.30%
```
**41.30% is now ABOVE the 30% Upgrade-1 trigger — a flip from 2026-07-06's 17.26% (which was well below the threshold).** This is the direct, mechanical consequence of Q2 2026's capex surge (see §3, §6). **Owner Earnings now DOES apply** for the FCF Yield sub-score:

```
Owner Earnings = Net Income + D&A − Maintenance CapEx
```
This framework proxies Maintenance CapEx as D&A (the same convention used to split Growth vs. Maintenance Capex above), so the D&A terms cancel algebraically:
```
Owner Earnings = Net Income + D&A − D&A = Net Income (TTM) = 235,508 (RMB millions)
```

**FCF Yield — 40% weight (Owner Earnings basis)**
```
Owner Earnings (HKD) = RMB235,508M × 1.1631 = HKD 273,919M
Market Cap            = HKD 4,145,168M
Owner Earnings Yield  = 273,919 / 4,145,168 = 6.608%

FCF_Score = clamp(100 × (1 − 6.608/10), 0, 100) = 33.92
```
→ Contribution: 33.92 × 0.40 = **13.568**

**For comparison — what raw (unadjusted) FCF Yield would have given, shown for transparency (not used in the score):**
```
TTM FCF (HKD) = RMB135,400M × 1.1631 = HKD 157,483M
Raw FCF Yield  = 157,483 / 4,145,168 = 3.799%
FCF_Score(raw) = clamp(100 × (1 − 3.799/10)) = 62.01
```
The Owner Earnings adjustment pulls this sub-score from 62.0 (would-be, unadjusted) down to 33.9 (as-scored) — a substantial swing, and exactly the intended effect of Upgrade 1: a temporary AI-buildout capex surge shouldn't be scored identically to a genuine decline in the underlying cash-generating power of the business, provided (as shown in §6) the business's Net Income and Non-IFRS Operating Profit both continued growing through the same quarter.

**EV/EBIT — 40% weight (PEG not applicable, redistributed from 25%)**
```
Net cash (HKD) = RMB58,191M × 1.1631 = HKD 67,683M
EV = Market Cap − Net cash = 4,145,168 − 67,683 = HKD 4,077,485M

EBIT TTM (HKD) = RMB258,543M × 1.1631 = HKD 300,711M

EV/EBIT = 4,077,485 / 300,711 = 13.559×

EV/EBIT_Score = clamp((13.559 − 12)/23 × 100, 0, 100) = clamp(6.778, 0, 100) = 6.778
```
→ Contribution: 6.778 × 0.40 = **2.711**

**Forward PE — 20% weight (PRIMARY formula — 5yr low/high range available)**
```
FY2026E EPS (RMB) = 25.62 (MarketScreener consensus, 45 analysts — refreshed, down from 25.84 on 07-06)
FY2026E EPS (HKD) = 25.62 × 1.1631 = 29.80
Forward PE        = 461.60 / 29.80 = 15.490×

5yr Low PE  = 14.18   |   5yr High PE = 22.32   |   5yr Avg PE = 18.35  (unchanged, see §3)

FwdPE_Score (raw) = clamp((15.490 − 14.18)/(22.32 − 14.18) × 100, 0, 100)
                   = clamp(1.31/8.14 × 100, 0, 100) = 16.09
```

**Historical PE Modifier (Upgrade 2):**
```
Deviation from 5yr avg = (15.490 − 18.35)/18.35 = −15.59%
```
Still falls in the same gray zone flagged 2026-07-06 (between the framework's named buckets: >20% below → −10; within ±10% → 0). **Modifier applied: 0** (same literal, conservative default — this gray-zone gap remains unresolved in the framework, flagged again).
```
FwdPE_Score (adjusted) = 16.09 + 0 = 16.09
```
→ Contribution: 16.09 × 0.20 = **3.218**

**PEG — not applicable (redistributed to EV/EBIT above, see §7)**

### Raw Weighted Score

```
Raw weighted = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.40) + (FwdPE_Score(adj) × 0.20)
             = 13.568 + 2.711 + 3.218
             = 19.497

+ Rate Regime Modifier (+5, Step 2 only — Step 1 passed) = 24.497
```

(Upside/Downside Modifier applied next, §10, before final rounding.)

---

## 10. Upside/Downside Modifier (Expected-Return Modifier)

**Scenario fair value (Rule 7), EV/EBIT-multiple method on forward EBIT** — same method as 07-06, updated for fresh TTM EBIT/net-cash/share-count base. The AI-monetization debate remains the operative driver, and this quarter's capex confirmation (176% YoY) sharpens rather than resolves it — bull/base/bear reflect how much credit the market ultimately gives the AI investment cycle:

| Scenario | Wt | Narrative | Forward EBIT (HKD, ×TTM EBIT 300,711) | Exit EV/EBIT | Equity Value (+Net Cash 67,683) | FV/share (÷8,980M sh) |
|---|---|---|---|---|---|---|
| Bull | 25% | AI products (Hy3, WorkBuddy, CodeBuddy — "breakout user growth" per Tencent's own Q2 language) scale fast enough to justify the capex; ad/cloud AI-driven growth (Marketing Services +22% YoY) continues accelerating | 300,711×1.20=360,853 | 16.0× | 360,853×16.0+67,683 = 5,841,331 | **HKD 650.48** |
| Base | 50% | Consensus-like continuation: steady ad/cloud/gaming growth, AI capex remains a near-term margin/FCF drag without a clear monetization inflection yet | 300,711×1.12=336,796 | 14.0× | 336,796×14.0+67,683 = 4,782,827 | **HKD 532.61** |
| Bear | 25% | AI monetization proof points keep slipping while capex stays elevated (this quarter's negative FCF becomes a recurring, not one-off, feature), investor patience for the buildout narrows further | 300,711×1.03=309,732 | 11.0× | 309,732×11.0+67,683 = 3,474,735 | **HKD 386.94** |

```
PW Fair Value = 0.25×650.48 + 0.50×532.61 + 0.25×386.94 = 162.62 + 266.31 + 96.74 = HKD 525.66
```

**Sanity check (Rule 4):** PW FV (HKD 525.66) sits below the bull case, above the bear case, and below the MarketScreener consensus PT of ~HKD 692.66 (consistent with 07-06's finding that this framework's scenario weighting reads more AI-monetization-skeptical than sell-side consensus) — a reasonable, moderately conservative placement, same pattern as last session.

**Step 2 — Gap, annualization, components**
```
Gap Upside %    = (525.66 ÷ 461.60) − 1 = +13.88%
Catalyst window = 2 years (default — still no single hard, dated re-rating catalyst identified; if
                   anything, this quarter's confirmed capex surge without a matching disclosed revenue
                   contribution from AI products makes the "several more quarters of proof points"
                   framing from 07-06 more apt, not less)
Annualized gap  = 13.88% ÷ 2 = +6.94%/yr
Intrinsic growth = +9.6%/yr (refreshed from 07-06's round +10% anchor — now grounded directly in the
                   FY2026E/FY2027E consensus revenue growth rates sourced this session: FY2026E
                   +9.85% YoY, FY2027E +9.39% YoY, averaging 9.6%)
Shareholder yield = Dividend yield 1.15% (HKD5.30/share last-paid annual dividend ÷ HKD461.60 current
                    price — no interim dividend declared alongside these Q2 2026 results, confirmed via
                    WebSearch, consistent with Tencent's historical annual-only dividend cadence) +
                    net buyback yield 1.63% (re-derived this session directly from Q2 2026's actual
                    disclosed repurchase spend: ~HKD16.9bn ÷ HKD4,145,168M market cap = 0.408% for the
                    quarter, annualized ×4 — a cleaner, more current empirical figure than the 07-06
                    session's YoY share-count-reduction proxy, see Data Gap #5)
                  = 2.78%
```
```
E (expected annual return) = 6.94 + 9.6 + 2.78 = +19.32%/yr
```

**Step 3 — Guardrail 1 (catalyst discipline).** E is on the **upside (E ≥ H)** side of the mapping. Per [valuation-scoring.md](../framework/valuation-scoring.md): *"If no catalyst identifiable within 18–24 months, cap upside (negative) side at −5."* No single hard, dated catalyst identified this session either (same conclusion as 07-06) — **the −5 cap applies.**

**Step 4 — Map E to the modifier, then apply the guardrail cap:**
```
E ≥ H (10%): M(uncapped) = −15 × clamp((E−H)/15pp, 0, 1) = −15 × clamp((19.32−10)/15, 0, 1)
           = −15 × clamp(0.6213, 0, 1) = −15 × 0.6213 = −9.32

Guardrail 1 cap (no dated catalyst within 18-24mo): M = max(−9.32, −5.0) = −5.0
```

**Interpretation:** as with 07-06, the raw expected-return math would earn substantial (though not maximal) discount credit absent the guardrail — the cap continues to do its job of preventing a broad, multi-quarter "AI investment eventually pays off" narrative from earning the full −15 credit without a dated, verifiable trigger. This quarter's confirmed capex acceleration, if anything, reinforces why that guardrail is doing real work here: the story got *more* capital-intensive and *not* more concretely dated this quarter.

---

## 11. Final Valuation Score, Quality Score, Composite Score

```
FINAL VALUATION SCORE = Raw weighted (19.497) + Rate Modifier (+5, already reflected in the 24.497
                         line above) + Upside/Downside Modifier (−5.0, capped)
                       = 19.497 + 5.0 − 5.0
                       = 19.497
```
Boundary rule: 19.497 → nearest 0.1 → not a ".X5" case → **Final Valuation Score = 19.5**

| | Value |
|---|---|
| Raw weighted (3 sub-scores, PEG redistributed) | 19.497 |
| Rate Regime Modifier (Step 2; Step 1 passed) | +5.0 |
| Upside/Downside Modifier (capped, Guardrail 1) | −5.0 |
| **FINAL VALUATION SCORE** | **19.5** |
| Prior valuation score | 22.0 (2026-07-06) |
| **Quality Score** | **71.7 (FAILS 80.0+ gate — wider miss than 07-06's 75.5)** |

```
Composite Score = 0.50 × (100 − 71.7) + 0.50 × 19.5
                = 0.50 × 28.3 + 0.50 × 19.5
                = 14.15 + 9.75
                = 23.90
```
Boundary rule: 23.90 → nearest 0.1 → not a ".X5" case → **Composite Score = 23.9**

---

## 12. Action & Why the Composite Score Must Not Be Read at Face Value

**Read in isolation, the numbers still look highly attractive:** Valuation Score 19.5 sits in the 0.0–29.9 "Very Cheap" band (→ "Full position 6–8%" per the Phase 03 table), and the blended Composite Score of 23.9 sits in the same band — even slightly cheaper-reading than 07-06's 22.0/23.3.

**This is exactly the "false green light" pattern this repo has documented repeatedly since the 2026-06-29 Quality Score addition** (AMZN, GOOG, MSFT, NOW, NFLX, NVO, SPGI, SPOT, TRN, UBER, ZS, NKE — and 0700-HK's own 2026-07-06 session). **0700-HK's Quality Score of 71.7 fails the strict 80.0+ gate** ([quality-scoring.md](../framework/quality-scoring.md)) — and this time by a **wider** margin than last quarter (8.3 points short vs. 4.5 previously). Per this session's explicit brief, the Composite Score above is shown **as a reference number only** — it must not be acted on at face value.

**What changed since 07-06, in one line:** the Quality Score got *worse* (75.5→71.7) specifically because Q2 2026's confirmed AI-capex surge (+176% YoY) collapsed TTM free cash flow (192.2B→135.4B RMB) and, with it, the FCF Quality sub-score (69.6→29.15) — even though Profitability, Balance Sheet, Moat, and Margins all held steady or improved slightly, and even though the *Valuation* Score's Owner Earnings adjustment (Upgrade 1, newly triggered this session as the growth-capex ratio crossed 30%) exists precisely to prevent this same capex surge from unfairly crushing the *cheapness* read. The two scores are telling a coherent, consistent story: the business's underlying profitability looks intact (hence Owner Earnings ≈ Net Income holding up, hence a still-very-cheap Valuation Score), but the *accounting-quality* bar the Quality Score's FCF Quality sub-score enforces — cash actually converting from reported profit, unadjusted for why — has gotten meaningfully worse this quarter, and that is a legitimate signal worth taking seriously rather than waving away with the Owner Earnings logic.

**Practical difference from the AMZN/GOOG-style precedent:** those are *existing holdings*, where a Quality Score failure is a Phase 04 "Quality Watch" flag, not an automatic force-exit, because of the framework's anti-turnover posture. **0700-HK is not held.** For a *candidate that has never cleared the entry gate*, there is no existing position to protect from over-trading — the Quality Score failure means Phase 01's entry gate has not been cleared, full stop, and this quarter it failed by a wider margin than before.

**Recommendation: PASS — do not open a new position.** The very-cheap Valuation Score (19.5) and resulting Composite Score (23.9) are real calculations, shown in full above, but they cannot override a Quality Score that has not only failed to clear the 80.0+ bar this quarter but moved further away from it. This is **not** a judgment that Tencent's core business deteriorated — Non-IFRS Operating Profit (+9% YoY), Net Income (+0.7% IFRS / +9% non-IFRS YoY), and revenue (+11% YoY, accelerating from Q1's +9%) all grew this quarter, and the Moat/Balance-Sheet/Profitability sub-scores are unchanged or improved. It is a statement that this quarter's capital-intensive AI investment cycle, whatever its eventual payoff, has genuinely and mechanically worsened the specific cash-conversion metric this framework's Quality Score gate tracks, and that the gate's job — refusing entry until quality clears the bar regardless of how cheap the stock looks — is again doing exactly what it was designed to do.

**No order setup is produced** — per [operating-brief.md](../framework/operating-brief.md) OUTPUT FORMAT step 6, the buy/sell/stop order-setup checklist in [fair-value-methodology.md](../framework/fair-value-methodology.md) applies only to a BUY or TRIM action; this session's action is PASS.

---

## 13. Watchlist & Stale-Score Update

Per [watchlist/README.md](../watchlist/README.md), this evaluation writes a new dated entry (`watchlist/not-in-portfolio/0700-HK/0700-HK-2026-08-12.md`) since a Rule 9 fundamental-event trigger (Q2 FY2026 earnings) fired — even though the action category (PASS) is unchanged from 07-06, the score and the underlying reasoning have materially changed, which per the README warrants a fresh dated pointer regardless. [STALE.md](../watchlist/STALE.md) was checked for a 0700-HK row: **none exists** — the ticker was already current under both the 2026-06-20 and 2026-06-29 methodology versions as of the 07-06 session, and no methodology version has changed since, so there was nothing to clear.

---

## 14. Next Review Triggers

- **Q3 FY2026 earnings** (Tencent's quarterly cadence points to mid-November 2026, per Rule 9) — the natural next checkpoint for whether the FCF/NI conversion ratio recovers as capex normalizes, or whether a second consecutive sub-70% quarter fires Phase 04's continuous-monitoring flag.
- **FCF quality watch, specifically:** if Q3 2026's FCF/NI conversion also comes in below 70%, that is 2 consecutive quarters — triggers Phase 04's "flag immediately, don't add until resolved" language even before any fiscal-year-level hard disqualifier could fire. Worth an interim check even outside the quarterly cadence if Q3 guidance/commentary signals continued heavy capex.
- **Growth CapEx ratio watch:** if the ratio stays above 30% (Owner Earnings continuing to apply) while Net Income growth decelerates, the Owner Earnings ≈ Net Income substitution used this session would start crediting a weakening, not just a temporarily-suppressed, cash-generation picture — worth re-examining if Net Income growth turns negative in a future quarter.
- **Any confirmed, dated AI-monetization catalyst** (a specific disclosed revenue contribution or margin inflection date for Hy3/WorkBuddy/CodeBuddy) would remove the Guardrail-1 cap on the Upside/Downside Modifier at the next rescore.
- **Quality Score watch:** re-verify Growth, Margins, and FCF Quality sub-scores at the next full evaluation — sustained double-digit-plus revenue growth, continued gross-margin expansion, and (most importantly given this session's finding) a recovery in FCF/NI conversion back above 70% would be the concrete path to clearing the 80.0+ gate.
- **Balance sheet detail (Data Gap #2) and Q2 2026 tax-split (Data Gap #3):** if a primary-source PDF for the Q2 2026 release becomes locatable, revisit the ROIC calc with a fresh 30-June-2026 balance sheet rather than the 31-March stand-in used this session.
- **Rule 9 standing triggers:** any Chinese gaming/WeChat regulatory action, management change, material M&A, or a >15% unexplained price move from HKD 461.60.

---

## 15. Glossary

(Pulled from [glossary.md](../framework/glossary.md) — terms actually used in this output)

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year. |
| **ADR (American Depositary Receipt)** | A US-exchange-listed security representing shares of a non-US company — not used here (TCEHY flagged unreliable). |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; drives Phase 03/05 action-table lookups only once a company has cleared the Quality gate. |
| **D&A** | Depreciation & Amortization. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years on a clean base — this framework's PEG-eligibility trigger. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted score, absent a documented carve-out. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **IFRS (International Financial Reporting Standards)** | The accounting standard most non-US companies (including Tencent) use for their audited financial statements, as opposed to US GAAP — Tencent's own releases label results "IFRS" and "non-IFRS" explicitly; this session corrects prior sessions' "GAAP" mislabeling of the same figures (see §3 Data Gap/Correction #6). |
| **MAU (Monthly Active Users)** | The number of unique users who engage with a product at least once in a given month. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying — not computed this session (no order setup produced). |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt (negative = net cash). |
| **NCI (Non-controlling interest)** | The portion of a consolidated subsidiary's equity that belongs to outside shareholders rather than the parent. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **Owner Earnings** | Net Income + D&A − maintenance capex only — used instead of raw FCF for moat-building reinvestors where growth capex exceeds 30% of total. **Newly triggered this session** (growth capex ratio 41.3%, up from 17.26% on 2026-07-06) — see §9. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0** | Always fetch a live price first — never infer from multiples. |
| **Rule 4** | Sanity-check protocol — e.g. comparing a probability-weighted fair value against analyst consensus. |
| **Rule 6** | Normalize earnings/margins/revenue/debt before valuing — strip out one-time items. |
| **Rule 7** | Scenario analysis is mandatory — bull/base/bear probability-weighted fair value (25/50/25). |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **Rule 10** | Separate intrinsic value from market price; assign a catalyst and timeline for the gap to close. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle, subject to a catalyst-discipline guardrail capping the upside side at −5 absent a dated catalyst within 18–24 months. |
| **Value trap** | A stock that looks statistically cheap but stays cheap because underlying quality is weaker than the multiple suggests — the exact risk this framework's Quality Score gate exists to surface. |

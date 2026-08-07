# New Position Evaluation — TTWO (Take-Two Interactive Software, Inc.)

**Task type:** NEW POSITION
**Date:** 2026-08-07
**10Y US Treasury yield:** 4.660% (2026-08-07 close, via yfinance `^TNX`)
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — `t.me/myroslavkorol`, post #2634, 2026-08-07T18:50:47Z: reports Take-Two Interactive disclosed Q1 FY2027 net bookings of approximately $1.39 billion, slightly exceeding the previously guided $1.32–$1.37 billion range, driven by the NBA 2K series and Grand Theft Auto franchise.

**This post is a trigger only, never data (Rule 0 / CLAUDE.md).** Every figure below is independently fetched from IBKR, yfinance, and Take-Two's own SEC 8-K/press release — none of it is taken from the Telegram post. As it happens, the post's $1.39B net-bookings figure and its framing turn out to be a reasonably accurate paraphrase of the real number ($1,385.9M) — but that is confirmed independently below, not assumed.

**Prior watchlist history:** TTWO has one prior entry — [watchlist/not-in-portfolio/TTWO/TTWO-2026-06-24.md](../watchlist/not-in-portfolio/TTWO/TTWO-2026-06-24.md), from [sessions/2026-06-24-new-position-ttwo.md](2026-06-24-new-position-ttwo.md) — **Phase 01 FAIL, not scored** (computed before the Quality Score engine existed; that engine went live 2026-06-29). That session named TTWO's **fiscal Q3 FY2027** earnings (the quarter containing GTA VI's confirmed November 19, 2026 launch) as the trigger most likely to flip the failing criteria, while flagging that a routine Telegram mention without new fundamental information should just be logged as "no change." **A new quarterly filing (Q1 FY2027, not yet Q3) has now landed** — Take-Two's fiscal Q1 FY2027 8-K was filed with the SEC today, 2026-08-07 — which is exactly the "new quarterly filing" condition that session said would warrant reconsideration. This session re-runs the full Quality Score gate fresh, under the current (2026-06-29) methodology, with TTM figures that now roll in the new quarter.

---

## 1. Live Price (Rule 0)

| Source | Price | Timestamp / detail |
|---|---|---|
| **IBKR live snapshot** (primary, contract_id 6478131, NASDAQ, "TAKE-TWO INTERACTIVE SOFTWRE") | **$246.48** | ts 1786132793 (2026-08-07) |
| yfinance `fast_info`/`currentPrice` (cross-check) | $246.50 | same session |

Bid/ask at snapshot: $245.25 / $246.26. Change on day: **+$14.01 (+6.03%)** — consistent with a positive market reaction to the Q1 FY2027 earnings beat and reiterated FY2027 guidance reported today. 52-week range (IBKR `misc_statistics`): low **$187.63** / high **$265.94** (13-week and 26-week highs also $265.94). 52-week open: $227.75.

**Live price used throughout this session: $246.48.**

Contract resolution: `search_contracts("TTWO")` returned the same NASDAQ primary listing used in the 2026-06-24 session (contract_id 6478131) plus secondary MEXI/EBS listings and a bond issuer entry — all describing the same underlying company. NASDAQ listing used throughout, per convention.

---

## 2. Data Sourcing Note — the new Q1 FY2027 quarter

**yfinance's structured quarterly statements have not yet ingested the new quarter** as of this session (expected — TTWO's earnings were released before market open *today*, 2026-08-07, and statement-vendor data typically lags the raw filing by some days). `t.quarterly_financials` / `t.quarterly_cashflow` / `t.quarterly_balance_sheet` all still end at the quarter ended **2026-03-31** (fiscal Q4 FY2026). `t.calendar` confirms `Earnings Date: 2026-08-07`.

**To independently verify the new quarter without relying on the Telegram post, three primary sources were cross-checked directly:**
1. **SEC EDGAR 8-K** (CIK 946581), filed 2026-08-07, accession 0001628280-26-054580, Items 2.02/9.01, exhibit `ttwo1q27earningsrelease.htm` — [direct filing link](https://www.sec.gov/Archives/edgar/data/946581/000162828026054580/ttwo1q27earningsrelease.htm).
2. **Businesswire press release** (the same Exhibit 99.1 text, wire-distributed) — [link](https://www.businesswire.com/news/home/20260806868549/en/Take-Two-Interactive-Software-Inc.-Reports-Results-for-Fiscal-First-Quarter-2027).
3. **yfinance** for all *prior* quarters (Q1 FY2026 through Q4 FY2026), used to build the TTM window's other three quarters.

Both primary sources (1) and (2) agree exactly on every figure. All Q1 FY2027 figures below are sourced from these, not from yfinance (which doesn't have the quarter yet) and not from the Telegram post.

**Q1 FY2027 (three months ended June 30, 2026) — GAAP, as filed:**

| Metric | Value |
|---|---|
| GAAP Net Revenue | $1,533.9M |
| Net Bookings (non-GAAP operating metric — see Glossary) | $1,385.9M |
| Gross Profit | $882.5M (57.5% gross margin) |
| GAAP Operating Loss | $(35.5)M |
| Interest income / expense | $22.8M / $(30.4)M |
| Benefit from income taxes | $(15.2)M |
| GAAP Net Loss | $(34.1)M |
| Diluted EPS | $(0.18)M, on 187.9M weighted avg. diluted shares |
| Operating cash flow | $(168.8)M |
| CapEx | $(25.0)M |
| Free Cash Flow | $(193.8)M |
| Depreciation | $40.1M |
| Amortization/impairment of software development costs & licenses | $107.5M |
| Stock-based compensation | $86.0M |
| Common stock issuance (financing CF) | $31.8M |
| Cash & equivalents (6/30/26) | $1,364.9M |
| Short-term investments (6/30/26) | $461.7M |
| Total debt (6/30/26) | $2,519.7M (ST $629.9M + LT $1,889.8M) |
| Total assets / liabilities / equity (6/30/26) | $9,064.2M / $5,455.8M / $3,608.4M |
| Shares outstanding (6/30/26) | 187.0M |
| FY2027 guidance (reiterated) | Net Bookings $8.0–8.2B; Net Revenue $7.9–8.1B; 189.4M diluted shares |

Net bookings ($1,385.9M) came in slightly above the previously guided $1.32–1.37B range — this is the real number behind the Telegram post's "~$1.39 billion" framing, confirmed independently rather than taken on the post's word. Company commentary (earnings call, per Seeking Alpha transcript and multiple financial-media summaries) describes GTA VI pre-order demand as "unprecedented," alongside continued NBA 2K strength — narrative context only, not a scored input (guidance/qualitative commentary is explicitly excluded from the scored inputs, see valuation-scoring.md's "Why Forward Guidance Is Not a Sub-score").

**Methodology note on EBIT/EBITDA construction:** yfinance's own "EBIT" field for TTWO's historical quarters diverges from the plain GAAP "Operating Income" field by a varying, unexplained amount in some quarters (e.g. Q4 FY2026: EBIT field $78.6M vs. Operating Income $10.0M) — likely a "Total Unusual Items" normalization yfinance applies inconsistently. Since Q1 FY2027 is only available from the primary GAAP source (no yfinance-normalized "EBIT" figure exists for it yet), this session uses the **plain GAAP Operating Income figure consistently across all four TTM quarters** (not yfinance's normalized EBIT field) for EBIT/EBITDA/ROIC purposes, to avoid mixing two different definitions across the TTM window. This is flagged as a data-consistency judgment call, not an invented number — every quarterly Operating Income figure used is sourced directly from yfinance's quarterly financials (for Q2–Q4 FY2026) or the SEC filing (Q1 FY2027).

---

## 3. Phase 01 — Quality Score (current 2026-06-29+ methodology)

This is TTWO's **first-ever Quality Score computation** — the 2026-06-24 session predates the Quality Score engine (live 2026-06-29) and only ran the old binary Phase 01 screen. All figures below use the **TTM window ending June 30, 2026** (Q2 FY2026 + Q3 FY2026 + Q4 FY2026 + Q1 FY2027) unless noted as fiscal-year (FY) figures, which use TTWO's fiscal year ending March 31.

### TTM Income Statement / Cash Flow build

| Quarter (fiscal) | Period end | Revenue | Net Income | Operating Income | Gross Profit | D&A | FCF | Source |
|---|---|---|---|---|---|---|---|---|
| Q2 FY2026 | 2025-09-30 | $1,773.8M | $(133.9)M | $(97.9)M | $980.5M | $361.1M | $96.5M | yfinance |
| Q3 FY2026 | 2025-12-31 | $1,699.0M | $(92.9)M | $(38.1)M | $945.5M | $308.2M | $236.2M | yfinance |
| Q4 FY2026 | 2026-03-31 | $1,679.8M | $(59.5)M | $10.0M | $938.7M | $345.7M | $198.6M | yfinance |
| Q1 FY2027 | 2026-06-30 | $1,533.9M | $(34.1)M | $(35.5)M | $882.5M | $147.6M | $(193.8)M | SEC 8-K / Businesswire |
| **TTM total** | **through 6/30/26** | **$6,686.5M** | **$(320.4)M** | **$(161.5)M** | **$3,747.2M** | **$1,162.6M** | **$337.5M** | — |

TTM EBITDA = TTM Operating Income + TTM D&A = $(161.5)M + $1,162.6M = **$1,001.1M**.

TTM Net Margin = $(320.4)M / $6,686.5M = **−4.79%**. (For comparison, FY2026 annual net margin was −4.48% — essentially unchanged; the new quarter did not flip the trailing picture positive, it's a similarly-sized loss quarter layered onto three already-known quarters.)

TTM Gross Margin = $3,747.2M / $6,686.5M = **56.04%**.

### ROIC (TTM)

```
TTM Tax Provision = $18.4M + $37.1M + $46.8M + $(15.2)M = $87.1M
TTM Pretax Income = $(115.5)M + $(55.8)M + $(12.7)M + $(49.3)M = $(233.3)M
TTM effective tax rate = $87.1M / $(233.3)M = −37.33%   (a positive tax provision against a pretax LOSS —
    an unusual but real combination, driven by geographic income mix; not smoothed or adjusted)

NOPAT = EBIT × (1 − tax rate) = $(161.5)M × (1 − (−0.3733)) = $(161.5)M × 1.3733 = $(221.8)M

Invested Capital (6/30/26) = Total Debt + Equity − Cash
                            = $2,519.7M + $3,608.4M − $1,364.9M = $4,763.2M

ROIC = NOPAT / Invested Capital = $(221.8)M / $4,763.2M = −4.66%
```

Negative, same directional finding as every fiscal year in the 2026-06-24 session (−1.12% to −89.88%). The unusual negative effective tax rate widens the loss somewhat versus a naive "apply FY2026's 40% rate" calc, but ROIC is decisively negative under any reasonable tax-rate assumption here — this is not a borderline case sensitive to that choice.

### Net Debt / EBITDA (point-in-time, 6/30/26 balance sheet ÷ TTM EBITDA)

```
Net Debt = Total Debt − Cash − Short-term Investments
         = $2,519.7M − $1,364.9M − $461.7M = $693.1M

Net Debt/EBITDA = $693.1M / $1,001.1M = 0.692×
```

Well inside both the standard 2.5× and even the asset-light 4× threshold — a genuine strength, and a meaningful improvement from FY2023's 4.566× (though that FY2023 figure was itself distorted by negative EBITDA in the denominator, as flagged in the 2026-06-24 session).

### FCF/NI Conversion (fiscal-year basis, per hard-disqualifier convention)

| FY | FCF | Net Income | FCF/NI ratio |
|---|---|---|---|
| FY2025 | $(214.6)M | $(4,478.9)M | 4.79% |
| FY2026 | $461.5M | $(298.2)M | −154.76% |

Both years are far below the 70% threshold — FY2025 because both figures are negative and cash burn nearly matched the loss; FY2026 because FCF flipped positive while NI stayed negative (a sign-flip that produces a *negative*, not merely low, ratio — still definitionally "<70%"). **Neither year has a documented growth-capex explanation for the shortfall.**

**Hard disqualifier fires: "FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation."** Per the [2026-08-05 rolling-window clarification](../decisions/2026-08-05-framework-clarification-fcf-disqualifier-rolling-window.md), this check is retested fresh each session against the current most-recently-completed 2 fiscal years (FY2025, FY2026) — and both genuinely fail it, so this is not a stale carry-forward mark; it is a fresh, current-window finding.

TTM FCF/NI ratio (for context, not the disqualifier basis): $337.5M / $(320.4)M = −105.34% — same non-meaningful sign-flip pattern.

### FCF-positivity hard disqualifier — re-tested, does NOT fire this session

| FY | FCF |
|---|---|
| FY2024 | $(157.8)M |
| FY2025 | $(214.6)M |
| FY2026 | $461.5M |

Per the same 2026-08-05 rolling-window clarification, the "not FCF-positive for 3+ consecutive years" hard disqualifier is retested against the current 3-year window (FY2024–FY2026, the most recently completed fiscal years — Q1 FY2027 alone doesn't complete a new FY). That window is **not uniformly negative** (FY2026 is positive) — so, unlike the 2026-06-24 session's finding (which read an *older* window, FY2023–FY2025, all three negative, as effectively disqualifying), **this disqualifier does not fire under the current window.** This is a genuine, documented change from the prior session — not because TTWO's cash generation somehow improved *this* session, but because the qualifying 3-year window itself rolled forward once FY2026 (already known, already positive) became the most recent complete year. It does not change the bottom-line gate outcome, since the FCF/NI conversion disqualifier above fires independently.

### Sub-score calculations

**Profitability (25% weight):**
```
NetMargin_Component = clamp((−4.79/30)×100, 0, 100) = 0.0
ROIC_Component       = clamp((−4.66/30)×100, 0, 100) = 0.0
Profitability_Score  = (0.0 + 0.0) / 2 = 0.0
```
(The "cap at 40.0 if not FCF-positive 3+ consecutive years" clause is moot here — the raw score is already 0.0, below any cap. For completeness: applying the same rolling-window reading used above to this identically-worded clause, the cap would not fire anyway, since FY2024–FY2026 isn't uniformly negative.)

**Margins (15% weight):**
```
GrossMargin_Score = clamp((56.04/80)×100, 0, 100) = 70.1
```
No structural-trend bonus applied — that bonus is specifically for margins *below* the 40% static threshold that are trending up; TTM gross margin (56.0%) is already well above 40% and is captured directly in the base formula. (For context: TTM margin, 56.0%, is essentially flat vs. FY2026's 57.23% — the multi-year 2023→2026 expansion trend, 42.7%→57.2%, is real and already reflected in the score via the higher base level, not double-counted as a separate bonus.)

**Growth (20% weight):**
```
3yr Revenue CAGR (FY2023 $5,349.9M → FY2026 $6,656.4M, unchanged from the 2026-06-24 session — 
  Q1 FY2027 doesn't complete a new fiscal year) = (6656.4/5349.9)^(1/3) − 1 = 7.56%
Growth_Score = clamp((7.56/25)×100, 0, 100) = 30.2
```
No TAM-expansion/pricing-power +10 modifier applied. GTA VI pre-order demand described as "unprecedented" by management on today's earnings call is compelling narrative, but this framework requires a **cited, documented mechanism** (specific market-share stat, a stated price premium, etc.) for this modifier — not inferred from adjectives in an earnings call or press coverage — and no such specific citation was found this session. Declining to apply the modifier is the conservative, "never invent" choice; it would not have changed the gate outcome regardless (+10 here would move Growth_Score to 40.2, adding ~0.16 to the weighted total — immaterial against a 35.0 vs. 80.0 gap).

**Balance Sheet (15% weight):**
```
BalanceSheet_Score = 100 × (1 − 0.692/4) = 82.7
```

**Moat Signal (15% weight)** — checklist, evidence cited or left unmarked (never inferred):

| Signal | True/False | Evidence |
|---|---|---|
| Market share stable or growing | **False** | No specific, cited market-share data verified this session (not re-derived from the 2026-06-24 session, which also didn't cite one). |
| Brand premium | **True** | Rockstar's GTA franchise is widely documented as one of entertainment's highest-grossing IP properties; today's earnings call and multiple independent financial-media summaries (Seeking Alpha transcript, BigGo Finance, MarketBeat) describe GTA VI pre-order demand as "unprecedented... no one's ever seen before at Take-Two or in the industry" (CEO Strauss Zelnick), alongside a reiterated $8.0–8.2B FY2027 net bookings guide built substantially on that demand. |
| Network effect | **True** | GTA Online, NBA 2K's online modes (MyTeam/MyCareer), and Zynga's mobile live-service portfolio are documented recurring-engagement ecosystems — Take-Two's own 10-K/10-Q filings disclose "recurrent consumer spending" (virtual currency, add-on content, subscriptions) as a distinct, growing revenue category, a standard network-effect mechanism in live-service gaming. |
| Switching costs | **False** | No specific documented mechanism (contractual lock-in, integration depth) verified this session. |
| Scale cost advantage | **False** | No cost-per-unit data verified this session. |

```
Moat_Score = (2/5) × 100 = 40.0
```

**FCF Quality (10% weight):**
```
TTM FCF/NI ratio = −105.34% (non-meaningful — negative NI base, same issue as the FY-basis figures above)
FCFQuality_Score = clamp(((−1.0534 − 0.40)/0.60)×100, 0, 100) = 0.0
```

### Final Quality Score

```
Quality Score = (0.0×0.25) + (70.1×0.15) + (30.2×0.20) + (82.7×0.15) + (40.0×0.15) + (0.0×0.10)
              = 0.000 + 10.508 + 6.044 + 12.404 + 6.000 + 0.000
              = 34.956 → rounds to 35.0
```

**Quality Score: 35.0 — fails the 80.0+ gate**, and independently, the **FCF/NI conversion hard disqualifier fires** (FY2025 4.8%, FY2026 −154.8%, both <70%, 2 consecutive years, no growth-capex explanation). Either finding alone is sufficient to fail Phase 01; both are present. Per quality-scoring.md and operating-brief.md: **stop here — no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, no fair-value/order-setup work.**

---

## 4. Does Q1 FY2027 change the picture versus the 2026-06-24 FAIL?

**Directionally, modestly — but not decisively, and not enough to move the gate outcome.** Specifically:

- **What changed for the better:** The FCF-positivity hard disqualifier no longer fires under the current rolling 3-year window (FY2024–FY2026 is not uniformly negative), whereas the 2026-06-24 session's older window (FY2023–FY2025) was. Net Debt/EBITDA (0.69× on a TTM/point-in-time basis) is clean and improved from FY2023's problematic 4.57×. Net bookings beat the low end of guidance and management reiterated an aggressive $8.0–8.2B FY2027 guide.
- **What did not change:** TTM net margin (−4.79%) is essentially unchanged from FY2026's −4.48% — Q1 FY2027 was itself a net-loss, operating-loss, and free-cash-flow-negative quarter ($(34.1)M net loss, $(35.5)M operating loss, $(193.8)M FCF), so it didn't pull the trailing picture into positive territory; if anything TTM FCF ($337.5M) is now *lower* than FY2026's standalone $461.5M, because the new quarter's cash burn outweighs the quarter it replaced in the trailing window. ROIC remains decisively negative. The FCF/NI conversion hard disqualifier still fires, on a slightly different pair of years than before but the same underlying pattern. Revenue growth (7.56% 3yr CAGR) is unchanged and still short of threshold. Share dilution continues (187.0M shares at 6/30/26 vs. 185.4M at FY2026 year-end, vs. 168.9M three years ago — now +10.7% cumulative, versus +9.8% as of the prior session).
- **Net result: still a decisive FAIL**, now for the first time expressed as a numeric Quality Score (35.0) rather than a binary screen. The 2026-06-24 session was correct that TTWO's trailing financials "won't change until a new quarterly filing lands" — one has now landed, and it moved the picture only at the margins. The session's own predicted trigger — **fiscal Q3 FY2027 (containing GTA VI's November 19, 2026 launch)** — remains the plausible point at which this could flip, not Q1.

---

## 5. Recommendation

**PASS.** Do not open a position, do not place a watch order. TTWO fails the Quality Score gate both on the weighted score (35.0, well under 80.0) and independently on a hard disqualifier (FCF/NI conversion <70% for FY2025 and FY2026). No Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is produced — computing any of that on a name that doesn't clear the quality gate would be exactly the black-box theater this framework declines to produce.

This is **the same bottom-line conclusion** as the 2026-06-24 session (PASS / no position), now expressed under the current Quality Score methodology rather than the old binary screen, with one genuine, documented change underneath it (the FCF-positivity disqualifier no longer independently fires) that does not change the overall outcome because a different hard disqualifier (FCF/NI conversion) fires in its place, and the weighted score remains far below the 80.0 bar regardless of either disqualifier.

---

## 6. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 7. Next Review Trigger

- **Routine re-screen:** not scheduled — Quality Score gate FAILs don't carry a numeric Phase 02 score to go stale, and don't get a recurring re-check cadence by default.
- **Rule 9 fundamental trigger** most likely to change the outcome: **TTWO's fiscal Q3 FY2027 earnings release** (expected ~early February 2027, per the company's typical reporting cadence), the quarter containing GTA VI's confirmed November 19, 2026 launch. That release — assuming it shows the durable GAAP profitability, positive ROIC, and normalized FCF/NI conversion management has guided toward — remains the single most plausible trigger for a materially different Quality Score outcome, consistent with the 2026-06-24 session's original framing. TTWO's **fiscal Q2 FY2027** (quarter ending Sep 30, 2026, reported ~early November 2026) is an earlier, lower-probability intermediate checkpoint — still pre-GTA-VI-launch, so unlikely on its own to flip the gate, but it will roll Q1 FY2026 (a smaller loss quarter) out of the TTM window.
- Absent one of those, future Telegram mentions of TTWO (including further GTA VI pre-order/marketing hype) should be logged as "last checked, no change" rather than triggering a full re-run — consistent with the 2026-06-24 session's own guidance and this session's finding that a full quarterly filing only moved the picture at the margins.

---

## Glossary

- **8-K** — the "current report" a US public company must file with the SEC within days of a material event (here, a quarterly earnings release furnished via Exhibit 99.1).
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **Composite Score** — this framework's single ranking number (0.0–100.0, 0.0 = most attractive) blending the Quality Score and Valuation Score 50/50 — not computed this session, since TTWO doesn't clear the Quality Score gate.
- **D&A** — Depreciation & Amortization — the non-cash accounting expense that spreads the cost of long-lived assets (including, for a game publisher, capitalized software development costs) over time.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and profitability ratios.
- **EPS (Earnings Per Share)** — Net income divided by shares outstanding; "diluted" EPS also accounts for shares that could be created from options/convertible securities.
- **EV/EBIT** — Enterprise Value divided by EBIT — a multiple comparing how expensive a company is relative to its operating profit; not computed this session (Phase 02 not reached).
- **FCF (Free Cash Flow)** — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. A low ratio without a documented capex explanation is a red flag for earnings-quality issues; not meaningful when Net Income is itself negative (produces a sign-flipped, nonsensical ratio).
- **GAAP** — Generally Accepted Accounting Principles — the standard US accounting rulebook companies use for official financial statements.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted sub-score total: not FCF-positive for 3+ consecutive years, Net Debt/EBITDA over threshold, or FCF/Net Income conversion under 70% for 2+ consecutive years without a documented growth-capex explanation.
- **Moat** — a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Bookings** — Take-Two's (and the video-game industry's) primary non-GAAP top-line operating metric: the total dollar amount of products/services sold in a period (in-game purchases, full-game sales, subscriptions, advertising), recognized at the point of transaction — distinct from GAAP Net Revenue, which recognizes some of that same activity over time per accounting rules (e.g. a game's online-service revenue spread over its expected play life). Self-reported and not scored directly by this framework, but useful context for gauging real-time demand ahead of how GAAP later recognizes it.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — operating profit after a tax adjustment but before financing costs; the numerator this framework uses to compute ROIC.
- **Quality Score** — this framework's 0–100.0 graded measure of business quality (higher = better); a company must score 80.0 or above to be eligible for valuation scoring at all.
- **Recurrent consumer spending** — a video-game-industry term (and a Take-Two-disclosed KPI) for ongoing player spending inside an already-released game (virtual currency, in-game items, subscriptions) as opposed to one-time full-game purchase revenue — the underlying mechanism behind the Network Effect Moat Signal credited in this session.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9** — this framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% unexplained stock-price move.
- **SBC (Stock-Based Compensation)** — employee pay in the form of company shares or stock options rather than cash; a real economic cost to existing shareholders through ongoing dilution.
- **SEC / SEC EDGAR** — the US Securities and Exchange Commission and its public database (EDGAR) of company filings.
- **TAM (Total Addressable Market)** — the total revenue opportunity available to a company if it captured 100% of its relevant market.
- **Treasury yield (10Y)** — the interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used in this framework's Rate Environment Gate (not invoked this session, since Phase 01 failed first).
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results, as opposed to a single fiscal-year or forward-looking figure. This session's core TTM window is Q2 FY2026 through Q1 FY2027 (July 2025 – June 2026).

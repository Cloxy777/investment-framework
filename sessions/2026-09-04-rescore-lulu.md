# RESCORE — LULU (Lululemon Athletica Inc.) — 2026-09-04

**Task type:** RESCORE (mode `--both` requested; valuation not reached — see §4)
**Trigger:** Rule 9 fundamental event — LULU reported Q2 FY2026 earnings after market close on 2026-09-03 (the mandatory next data point named in the [2026-07-09 watchlist entry](../watchlist/not-in-portfolio/LULU/LULU-2026-06-29.md)), cutting full-year guidance for the **second consecutive quarter** and triggering a same-day/next-morning share-price decline of **-19.11%** — independently a >15% unexplained-move trigger, though here the cause is fully documented (the earnings/guidance event itself), not unexplained.
**Date:** 04 Sep 2026
**10Y US Treasury Yield:** 4.77% (TradingEconomics, live read 2026-09-04: "held around 4.76% on Friday... actual figure 4.7650")
**Rate Regime Modifier (Step 2):** +5 (10Y in 3.5–5% bracket) — **for the record only, not applied** (see §4)
**Current LULU portfolio weight:** 0% — **not held**, confirmed absent from [holdings.md](../portfolio/holdings.md)
**Sector:** Consumer Discretionary — Apparel, Accessories & Luxury Goods (premium athletic apparel; vertically-integrated DTC/retail model)
**Last review:** 2026-06-29 NEW POSITION session — Quality Score 56.9, Phase 01 FAIL, not scored (Composite not computed); last routine check 2026-07-09, no change. See [session](../sessions/2026-06-29-new-position-lulu.md) and [watchlist entry](../watchlist/not-in-portfolio/LULU/LULU-2026-06-29.md).

---

## 0. Why a not-held ticker is being run through `/rescore`

LULU has never been a portfolio holding — it failed the Phase 01 Quality Gate at its only prior evaluation (2026-06-29 NEW POSITION) and was never bought. This session was invoked directly as `/rescore LULU`, and the ticker's own watchlist entry named "Q2 FY2026 earnings (expected ~September 2026)" as its mandatory next re-check trigger — which fired yesterday. Per [watchlist/README.md](../watchlist/README.md), `/rescore` is the command that creates/updates `in-portfolio/` entries, but since LULU isn't held, this session updates its existing `not-in-portfolio/LULU/` entry instead (no folder move — only `/sync-portfolio` moves tickers between the two directories, and LULU has never been synced into portfolio because it was never bought).

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$98.50** | IBKR `get_price_snapshot`, contract_id 45157951 (NASDAQ, re-verified via `search_contracts`: "LULULEMON ATHLETICA INC" — distinct from the unrelated ADX-listed "LULU RETAIL HOLDINGS PLC," contract_id 789881626, excluded), **REALTIME** status |
| Change vs. prior close | **-19.11%** (-$23.27) | IBKR `change` field — this is the post-earnings, post-guidance-cut reaction |
| 52-week range | $104.44 – $225.98 (13-week low $104.44, 26-week low $104.44, 52-week low $104.44 — today's print is a fresh 52-week low, below the 13/26-week windows too) | IBKR `misc_statistics` |
| Prior 52-week range (2026-06-29 session) | ~$117 – $423 | For context: the stock has now round-tripped from a ~$423 2025 peak through a ~$117 June 2026 low to today's ~$98.50 — a fresh, deeper low |

**$98.50 is the live price used for all reference calculations below**, per Rule 0.

---

## 2. Data Gathered — Q2 FY2026 Earnings (reported 2026-09-03, after market close)

**Source discipline note:** this repo's usual `yfinance` Python workflow was **not available in this session's execution environment** (module not installed, no working substitute found). All figures below are sourced directly from lululemon's own SEC 8-K exhibits (primary source, via WebFetch) and cross-checked against CNBC/Investing.com/BusinessWire coverage (via WebSearch) — no metric is invented or estimated, but the 5yr historical PE range (§4) could not be independently re-derived this session and is carried forward, explicitly flagged.

### Q2 FY2026 income statement (13 weeks ended 2026-08-02) vs. Q2 FY2025 (SEC 8-K Ex-99.1, [lulu-20260802xex991.htm](https://www.sec.gov/Archives/edgar/data/0001397187/000139718726000126/lulu-20260802xex991.htm))

| Metric | Q2 FY2026 | Q2 FY2025 | Change |
|---|---|---|---|
| Net Revenue | $2,415.6M | $2,525.2M | **-4.3%** |
| Gross Profit | $1,461.9M | $1,477.2M | -1.0% |
| Gross Margin | 60.5% | 58.5% | +200bps |
| SG&A | $1,006.3M | $951.7M | +5.7% |
| SG&A % of Revenue | 41.7% | 37.7% | +400bps |
| Operating Income | $453.7M | $523.8M | -13.4% |
| Operating Margin | 18.8% | 20.7% | -190bps |
| Net Income | $329.2M | $370.9M | -11.2% |
| Diluted EPS | $2.92 | $3.10 | -5.8% |
| Diluted weighted-avg shares | 112.9M | 119.7M | -5.7% (buybacks) |

**⚠️ One-off flag on Q2 EPS:** per WebSearch (Investing.com/CNBC coverage), **$0.86 of the $2.92 reported diluted EPS came from tariff refunds and associated interest income** (a non-operating, non-recurring item) — ex that item, comparable EPS would have been ~$2.06. This is a GAAP-reported, real cash item (not adjusted out below, consistent with this framework's "score off filed GAAP, not company-adjusted, figures" convention), but it inflates the TTM Net Income figure used in §3 relative to underlying operating economics — flagged, not backed out, per Rule 6 discipline (documented, not invented).

### Balance sheet (SEC 8-K Ex-99.1 + 10-Q [lulu-20260802.htm](https://www.sec.gov/Archives/edgar/data/0001397187/000139718726000127/lulu-20260802.htm))

| Item | 2026-08-02 | 2026-02-01 (FYE) | 2025-08-03 |
|---|---|---|---|
| Cash & equivalents | $1,389.7M | $1,807.2M | $1,155.8M |
| Inventories | $1,711.5M | $1,700.8M | $1,722.6M |
| Total debt/borrowings | **$0** (no revolver drawn) | $0 | $0 |
| Stockholders' equity | $4,791.2M | $4,961.8M | $4,387.3M |

### Shares outstanding (10-Q cover page, as of 2026-08-28)

Common shares 105,594,064 + exchangeable shares of Lulu Canadian Holding, Inc. 5,115,961 = **110,710,025 total economic shares** (same convention as the 2026-06-29 session: exchangeable shares are economically and contractually equivalent to common stock and included in the company's own diluted-EPS share count).

### TTM reconstruction (rolling window ended 2026-08-02) — built from Q1/Q2 FY2026 and Q1/Q2 FY2025 quarterly 8-Ks plus the FY2026 (FYE 2026-02-01) annual total already on file from the 2026-06-29 session

*Fiscal-year labeling note: this framework's prior LULU session labeled the year ended 2026-02-01 "FY26" — the same year the company's own current filings call "fiscal 2025." To avoid ambiguity, quarters below are identified by their actual end dates, not by a "FYxx" label.*

| Quarter (end date) | Revenue | Gross Profit | Op. Income (EBIT) | Net Income | OCF | Capex | Source |
|---|---|---|---|---|---|---|---|
| Q ended 2025-05-04 | $2,370.66M | $1,383.126M | $438.625M | $314.572M | -$118.954M | $106.842M | [Q1 FY2026 8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/0001397187/000139718726000077/lulu-20260503xex991.htm), comparative column |
| Q ended 2025-08-03 | $2,525.2M | $1,477.2M | $523.8M | $370.9M | $328.654M* | $213.158M* | Q2 FY2026 8-K Ex-99.1, comparative column (*derived: H1 FY2025 cumulative OCF $209.7M / capex $320.0M minus the Q1 row above) |
| Full year ended 2026-02-01 | $11,102.6M | $6,284.1M | $2,210.6M | $1,579.2M | $1,602.5M | $680.8M | Carried from 2026-06-29 session (yfinance, unchanged — a closed fiscal year) |
| **⇒ H2 (Q3+Q4) ended 2026-02-01** | $6,206.74M | $3,423.774M | $1,248.175M | $893.728M | $1,392.8M | $360.8M | Full year minus the two Q ended-2025 rows above |
| Q ended 2026-05-03 | $2,471.603M | $1,338.818M | $276.946M | $195.048M | $214.440M | $138.850M | [Q1 FY2026 8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/0001397187/000139718726000077/lulu-20260503xex991.htm), current-period column |
| Q ended 2026-08-02 | $2,415.6M | $1,461.9M | $453.7M | $329.2M | $374.86M* | $142.95M* | Q2 FY2026 8-K Ex-99.1, current-period column (*derived: H1 FY2026 cumulative OCF $589.3M / capex $281.8M minus the Q1 row above) |
| **TTM (ended 2026-08-02)** | **$11,093.943M** | **$6,224.492M** | **$1,978.821M** | **$1,417.976M** | **$1,982.1M** | **$642.6M** | Sum: H2-ended-2026-02-01 + Q-ended-2026-05-03 + Q-ended-2026-08-02 |

```
TTM Gross Margin = 6,224.492 / 11,093.943 = 56.10%
TTM Net Margin   = 1,417.976 / 11,093.943 = 12.78%
TTM FCF          = 1,982.1 − 642.6 = 1,339.5M
TTM FCF/NI        = 1,339.5 / 1,417.976 = 94.47%
Net Debt (2026-08-02) = $0 debt − $1,389.7M cash = −$1,389.7M (net cash)
```

No metric above is invented or estimated — every figure traces to a SEC 8-K exhibit or a direct sum/difference of 8-K-sourced figures, each cell sourced individually.

### Other inputs

| Input | Value | Source |
|---|---|---|
| Revenue 3yr CAGR | **11.03%** (unchanged — FY23→FY26 annual, FY ended 2026-02-01 still the most recently *completed* fiscal year) | Carried from 2026-06-29 session |
| 5yr PE (avg / low / high, n=20 quarters) | **34.90× / 9.22× / 65.94×** — **⚠️ carried forward, not re-derived this session** (`yfinance`/`get_earnings_dates` reconstruction unavailable — no working substitute found; per Rule 0's documented fallback for a hard-to-refresh figure, most-recently-verified value used, clearly flagged) | Carried from 2026-06-29 session |
| FY2026 full-year guidance (company, post-cut) | Revenue $10.35–10.50B (-5% to -7%); Diluted EPS $9.48–9.73; tax rate ~30% | Q2 FY2026 8-K Ex-99.1 |
| Q3 FY2026 guidance | Revenue $2.29–2.32B (-10% to -11% YoY); Diluted EPS $0.93–0.98 | Q2 FY2026 8-K Ex-99.1 |
| Comparable sales, Q2 FY2026 | **-9%** | WebSearch (CNBC) |
| Effective tax rate used for ROIC | **30%** (company's own current guided rate — up from the 21% normalization anchor carried in other framework tickers; used here since it's LULU's own most recent guided figure, not a carried-forward assumption) | Q2 FY2026 8-K Ex-99.1 |

---

## 3. Quality Score (Phase 01 gate) — recomputed with fresh TTM data

**Hard disqualifier check:**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years? | Annual basis unchanged from 2026-06-29 (FY23 38.35% / FY24 106.07% / FY25 87.26% / FY26 58.36% — no new completed fiscal year since); TTM basis now 94.47% | disqualify if 2 consecutive *fiscal years* <70%, no growth-capex carve-out | ✅ PASS (FY23 and FY26 both <70% but not consecutive — same reading as 2026-06-29) |
| Net Debt/EBITDA over threshold? | Net cash (-$1,389.7M) | disqualify if >2.5× | ✅ PASS |
| FCF-positive 3+ consecutive years? | FY23–FY26 all positive; TTM positive ($1,339.5M) | disqualify if not | ✅ PASS |

**No hard disqualifier fires.**

```
Net Margin (TTM) = 1,417.976 / 11,093.943 = 12.78%
NetMargin_Component = clamp((12.78/30)×100, 0, 100) = 42.6

Normalized EBIT = 1,978.821M (no acquisition-intangible add-back applicable — LULU carries none)
NOPAT = 1,978.821 × (1 − 0.30) = 1,385.175M
Net Invested Capital = Debt $0 + Equity $4,791.2M − Cash $1,389.7M = $3,401.5M
ROIC = 1,385.175 / 3,401.5 = 40.72%
ROIC_Component = clamp((40.72/30)×100, 0, 100) = 100.0   (saturates)

Profitability_Score = (42.6 + 100.0) / 2 = 71.3   (no FCF cap — FCF positive all years)

GrossMargin_Score = clamp((56.10/80)×100, 0, 100) = 70.1   (no trend bonus — already well above 40%)

Revenue 3yr CAGR (unchanged, FY23→FY26) = 11.03%
Growth_Score (raw) = clamp((11.03/25)×100, 0, 100) = 44.1
Structural-deceleration evidence (documented): Q2 FY2026 comp sales -9%; Q2 FY2026 revenue -4.3% YoY (an actual decline, not just deceleration); full-year guidance cut for the SECOND consecutive quarter (original 2026-03-17 guide $11.35-11.50B → 2026-06-04 cut to $11.00-11.15B → 2026-09-03 cut again to $10.35-10.50B); Q3 FY2026 guided -10% to -11% YoY (accelerating decline, not stabilizing)
Growth_Score = 44.1 − 10 (structural deceleration) = 34.1

BalanceSheet_Score = clamp(100×(1 − NetDebt/EBITDA), 0, 100) = 100.0   (net cash, ratio negative, clamps at ceiling)

Moat_Score: 1 of 5 signals TRUE (unchanged from 2026-06-29) — Brand premium TRUE (Q2 gross margin actually expanded +200bps YoY to 60.5% even as revenue fell, i.e. limited discounting/genuine pricing power); Market share FALSE (comp sales -9%, a continuation/acceleration of the documented Americas/global share erosion to Alo Yoga/Vuori cited in the 2026-06-29 session — if anything more decisively false now); Network effect, Switching costs, Scale cost advantage — none cited with supporting evidence
Moat_Score = (1/5) × 100 = 20.0

FCFQuality_Score = clamp(((0.9447 − 0.40)/0.60)×100, 0, 100) = 90.8

Quality Score = 71.3×0.25 + 70.1×0.15 + 34.1×0.20 + 100.0×0.15 + 20.0×0.15 + 90.8×0.10
              = 17.825 + 10.515 + 6.820 + 15.000 + 3.000 + 9.080
              = 62.24 → 62.2
```

**Quality Score = 62.2 — still fails the 80.0+ gate** (up from 56.9 on 2026-06-29, but the improvement is concentrated almost entirely in the FCF Quality sub-score, driven by an unusually strong H1 FY2026 operating-cash-flow swing — Q1 FY2025's OCF was deeply negative, -$118.954M, on a working-capital build, and Q1 FY2026's OCF recovered to +$214.440M, mechanically boosting the trailing ratio. The two sub-scores that actually measure the ongoing operating deterioration — **Growth (34.1)** and **Moat (20.0)** — did not improve and, on the qualitative evidence, arguably worsened (revenue is now *declining*, not just decelerating; comp sales -9% is the sharpest decline cited across either session).

**Sensitivity check (per "no black box" principle):** even crediting the maximum plausible Moat_Score of 40.0 (2 of 5 signals) instead of 20.0, Quality Score rises only to 65.2 — still 14.8 points short of the gate. This is not a close call.

---

## 4. Per quality-scoring.md's explicit stop-rule — Valuation Score NOT computed

[quality-scoring.md](../framework/quality-scoring.md): *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all. Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."*

LULU scores 62.2 — well below the gate. Per this explicit instruction, and consistent with how the 2026-06-29 NEW POSITION session treated the same stop-rule for this same (never-held) ticker, **no Valuation Score or Composite Score is computed this session.** This differs from how the framework treats *held* positions that drop below the gate (e.g. MSFT, NOW, NVO, TRN in [holdings.md](../portfolio/holdings.md), which carry "ref only, gate fail" Composite figures for existing-capital monitoring context) — LULU has no existing capital at risk to monitor, so there is no monitoring rationale for computing a valuation score the framework's own rule says not to compute. No order setup applies.

**Rate Environment Gate — shown for the record only, exactly as in the 2026-06-29 session, since it is moot:**

```
Forward PE (FY2026 company guidance midpoint EPS $9.605) = $98.50 / $9.605 = 10.255×
EY = 1 / 10.255 = 9.751%
Spread = EY − 10Y Treasury = 9.751% − 4.77% = +4.981pp  → passes Step 1 (≥+1.5%), no additive
Rate Regime Modifier (Step 2): 10Y in 3.5–5% bracket → +5 (not applied — gate fails)
```

For reference only: at $98.50 the stock trades at 10.3× the company's own (just-cut) forward EPS guidance, against a 5yr average PE of 34.90× (carried forward, flagged) — the market is pricing in continued deterioration, not a temporary air pocket. This is a valuation observation, not a score; Phase 01's gate is a quality/cash-flow question, and on that question the answer is still no.

---

## 5. Qualitative Update Since 2026-06-29

1. **Guidance discipline (Phase 04) — now a genuine 2-consecutive-cut pattern.** The 2026-06-29 session flagged the Q1 FY2026 cut as "a single cut so far — not yet a Phase 06-triggering pattern." That pattern has now completed: original guide (2026-03-17) → cut #1 (2026-06-04) → **cut #2 (2026-09-03)**, each cut larger than the last, with no one-off cause identified for either cut (the tariff-refund item in §2 is a one-off *gain* to this quarter's EPS, not an explanation for the guidance cut itself, which management attributed to continued Americas softness, a leggings-category slowdown, and lingering brand-perception drag from the earlier China controversy per CNBC's coverage of the earnings call). Per [strategy.md](../framework/strategy.md) Phase 06, "guidance cut 2+ consecutive quarters w/o a one-off explanation" is explicitly listed as "Growth thesis broken" exit-trigger evidence. **This is moot for a non-held name** (nothing to exit), but it materially reinforces the "do not enter" conclusion, and is exactly the kind of pattern that would make a future Turnaround Sub-Gate case (Upgrade 4) harder to build, not easier.
2. **Heidi O'Neill started as permanent CEO on 2026-09-08** — wait, that date is in the future relative to today (2026-09-04); she has not yet started. No new CEO commentary exists yet. This Q2 print and guidance cut were delivered by outgoing interim leadership (Meghan Frank), not the incoming CEO — her first public strategic commentary remains the next qualitative catalyst to watch, expected within days of this session.
3. **Comp-sales decline streak has deepened, not stabilized.** The 2026-06-29 session cited "5 consecutive quarters of Americas comp declines." This quarter's -9% *company-wide* comp figure (not broken out by geography in the sources reviewed this session) suggests the trend has not turned, consistent with the accelerating Q3 revenue-decline guidance (-10% to -11%, worse than Q2's actual -4.3%).
4. **No new CEO/CFO Form 4 insider purchase >$500K found** via this session's WebSearch — the Turnaround Sub-Gate's insider-buying condition remains unsatisfied, unchanged from both prior checks.

---

## 6. Recommendation

**No action — Phase 01 Quality Gate FAIL, Quality Score 62.2 (still well below the 80.0+ gate). Do not enter.** No Valuation Score or Composite computed (§4). No order setup applies. This is not a change in verdict from 2026-06-29/2026-07-09 (still "not scored, do not enter"), but the underlying evidence has shifted: the Quality Score itself rose (56.9 → 62.2), driven almost entirely by a mechanical FCF/NI improvement from an unusually weak year-ago comparison quarter, while the two sub-scores most directly tied to the operating thesis — Growth and Moat — show continued or worsening deterioration (an actual revenue decline, a second consecutive guidance cut, and no improvement in the competitive-share picture). The stock's ~19% single-day decline reflects the market reaching a similar conclusion in real time.

---

## 7. Next Review Trigger

Re-evaluate on any of the following Rule 9 triggers:

- **Heidi O'Neill's first public strategic commentary as CEO** (starts 2026-09-08, 4 days from this session) — a management-change trigger, and the first real read on strategic direction under new leadership.
- **Q3 FY2026 earnings release** (guided revenue $2.29–2.32B, EPS $0.93–0.98; expected ~December 2026 based on historical cadence) — the mandatory next data point. A **third** consecutive guidance cut would further reinforce the Phase 06 "Growth thesis broken" evidence (moot for a non-held name, but relevant context); a guidance *reaffirmation or raise* would be the first sign of stabilization since the leadership transition and product-cycle issues surfaced.
- **Any quarter showing comp-sales decline bottoming or reversing** — the single clearest sign the operating deterioration is turning.
- **A qualifying CEO/CFO Form 4 purchase >$500K** — would strengthen (not by itself satisfy) a future Turnaround Sub-Gate case.
- Routine news-flow absent a new quarterly filing or CEO strategic update should be logged as "last checked, no change."

---

## Glossary

| Term | Meaning |
|---|---|
| **bps (basis points)** | 1 bps = 0.01 percentage points; 200bps = 2 percentage points. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **Comparable sales (comps)** | Sales growth at stores open at least a year, stripping out the effect of opening new stores — the standard like-for-like organic-growth metric for retailers. LULU's Q2 FY2026 comps fell 9%. |
| **Composite Score** | `0.50×(100−Quality Score) + 0.50×Valuation Score` — combines quality and cheapness into one number, computed only for companies that clear the 80.0+ Quality Score gate. Not computed for LULU (gate not cleared). |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **EV/EBIT** | Enterprise Value divided by EBIT — a valuation multiple; not computed this session (Quality Gate failed before Phase 02). |
| **FCF (Free Cash Flow)** | Cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. LULU's TTM ratio (94.47%) looks strong mainly because of an unusually weak year-ago comparison quarter, not necessarily a durable improvement. |
| **Forward PE** | Price ÷ next twelve months' expected EPS. |
| **Form 4** | A SEC filing disclosing an insider's (officer/director/10%+ owner's) purchase or sale of company stock. |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook companies use for their official financial statements. |
| **Hard disqualifier** | One of three quality-gate conditions (FCF/NI conversion, Net Debt/EBITDA, FCF positivity) that fails a company outright regardless of its weighted Quality Score. None fire for LULU. |
| **Moat** | A durable competitive advantage (brand, scale, network effects, switching costs) that protects a business's profits from competitors. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − tax rate) — operating profit adjusted for the tax a company would pay on it, used as the numerator in ROIC. |
| **Quality Score** | A 0–100.0 grade (0 = lowest quality, 100 = highest) blending profitability, margins, growth, balance sheet, moat, and FCF quality into one number; a company must score ≥80.0 to be eligible for Phase 02 valuation scoring at all. LULU scores 62.2. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity − cash) into profit; a core quality signal in this framework. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 6** | This framework's instruction to normalize out one-off, non-operating items (documented, never invented) before assessing sustainable profitability. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **SG&A (Selling, General & Administrative expenses)** | The operating-expense line covering marketing/selling costs plus corporate overhead — everything between Gross Profit and Operating Income that isn't cost of goods sold. LULU's SG&A rose to 41.7% of revenue in Q2 FY2026 from 37.7% a year earlier, even as revenue fell — the direct driver of its operating-margin compression. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results, reconstructed here from four overlapping quarterly SEC filings since LULU's fiscal year doesn't align with the calendar year. |
| **Turnaround Sub-Gate** | The conditional path (Hybrid Upgrade 4) that lets a company failing 2–4 quality criteria still enter as a small (2–3%) position if it passes 5 specific tests. Not independently re-run this session — the continuous Quality Score engine has superseded the old binary 8-criterion checklist as the primary Phase 01 gate mechanism, and LULU's Quality Score (62.2) is not close enough to 80.0 for the distinction to matter. |
| **YoY (Year-over-Year)** | A growth-rate comparison against the same period one year earlier. |

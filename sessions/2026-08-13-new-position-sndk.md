# NEW POSITION — SNDK (Sandisk Corporation, NASDAQ) — 2026-08-13

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, unattended; re-evaluation of a prior WATCHLIST ONLY — SNDK is not currently held)
**Date:** 2026-08-13
**10Y US Treasury Yield:** 4.70% (FRED `DGS10`, most recent posted observation dated 2026-08-11 — a 2-day reporting lag, slightly longer than the usual 1-day lag, consistent with FRED not yet having posted 2026-08-12/08-13)
**Rate Regime Modifier:** +5 (10Y in the 3.5–5% bracket) — see §4.
**Current SNDK portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** [watchlist/not-in-portfolio/SNDK/SNDK-2026-08-05.md](../watchlist/not-in-portfolio/SNDK/SNDK-2026-08-05.md) — Quality Score 89.4 (adopted rolling-window reading), Valuation Score 37.4, **Composite Score 24.0**, **WATCHLIST ONLY** (base-case R/R exactly 1.00:1, failed the 2:1 minimum).
**Sector:** Semiconductors / NAND Flash Memory & Data Storage — spun off from Western Digital (WDC) 21 February 2025.
**Filer type:** US domestic filer, CIK **0002023554**. Fiscal year ends the last Friday in June/early July.
**First-use jargon decode:** see closing Glossary (§10).

---

## 0. Why this session exists — trigger source, and how it was independently verified

A post on `t.me/myroslavkorol` (post **2643**, ~19:30 UTC, 2026-08-12) flagged SanDisk's "Investor Day," scheduled 2026-08-13, as advance notice only — logged in [portfolio/snapshots/telegram-watch.md](../portfolio/snapshots/telegram-watch.md) and explicitly held for manual follow-up once the event produced an outcome. A new top post on the same channel (**2645**, ~15:44 UTC, 2026-08-13) reported the event's outcome, characterizing it as a reaffirmation of gross-margin/demand themes and citing a stock move.

**Per Rule 0 and CLAUDE.md, no figure from either Telegram post is used as data anywhere in this session** — the posts are triggers only. Every figure below is independently re-pulled from IBKR (live price), SEC EDGAR (SanDisk's most recent 8-K, filed 2026-08-05, accession `0001628280-26-053346` — the same FY2026 GAAP financials already scored in the prior session; **no new 8-K/10-Q/10-K has been filed as of this session's EDGAR check**), FRED (10Y yield), stockanalysis.com (forward-PE/consensus-EPS market data), and independent financial press (Yahoo Finance, StockTitan/press-release syndication, FinanceFeeds) covering the Investor Day itself.

**Independent verification of the Investor Day's content (context only, not a data source):**
- **Confirmed via press coverage independent of the Telegram post:** the 2026 SanDisk Investor Day ("SanDisk In Focus") ran 2026-08-13, 9:00am ET, CEO David Goeckeler and CFO Luis Visoso presenting. CFO commentary: total NAND market >$300B in 2026, >$500B in 2027, supply tight into 2028. Long-term (FY2028–FY2030) non-GAAP targets disclosed for the first time: **gross margin ≈80%**, **operating margin ≈75%**, **adjusted FCF margin ≈50%**, revenue growth "mid-to-high teens" (bit-growth-aligned). "New Business Model" long-term-agreement bit mix guided to ~50% of bits in FY2027, ~two-thirds in FY2028. Capital-return policy: intent to "return 100% of excess cash to shareholders after investing in the business" (no new buyback dollar figure disclosed beyond the $15.5B authorization already reported 2026-08-05). Sources: [StockTitan/press release](https://www.stocktitan.net/news/SNDK/sandisk-details-growth-strategy-and-long-term-financial-model-at-tfgp9oq5d8ja.html), [FinanceFeeds](https://financefeeds.com/sandisk-investor-day-sndk-what-to-watch/), [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/dear-sandisk-stock-fans-mark-151502073.html).
- **No new 8-K carrying audited/reviewed financial statements has been filed** — EDGAR's most recent SNDK 8-K remains the 2026-08-05 Q4/FY2026 earnings filing. The Investor Day is a qualitative/guidance event, not a new financial-statement filing.
- The Telegram post's "+14%" stock-move claim is **broadly consistent with, but not identical to**, this session's own live IBKR fetch (§1: +15.19% intraday) — small variance expected from snapshot timing; the IBKR figure, not the post's, is what's actually used.

**Why this is a Rule 9 trigger regardless:** guidance revision (here, a guidance *reaffirmation plus new long-term framework*) is one of the explicit Rule 9 mandatory re-valuation triggers in [fair-value-methodology.md](../framework/fair-value-methodology.md), independent of whether the guidance itself is scored. Per [valuation-scoring.md](../framework/valuation-scoring.md)'s "Why Forward Guidance Is Not a Sub-score," **none of the new FY2028–2030 targets described above are used as scored inputs anywhere in this session** — they are cited for context only, exactly like the Q1 FY27 guidance figures already excluded from scoring in the 2026-08-05 session.

SNDK's watchlist file carries no `⚠️ STALE SCORE` banner and no row in [watchlist/STALE.md](../watchlist/STALE.md) (methodology version 2026-06-29, unchanged since the prior session) — nothing to clear on that front.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price (used)** | **$1,548.46** | IBKR `get_price_snapshot` (contract_id **760250490**, NASDAQ, "SANDISK CORP" — re-confirmed via `search_contracts` as the correct standalone equity, distinct from the leveraged/inverse single-stock-ETF products SNXX/SNDU/SNDQ/SNDG/SNDC/SANS/SADP that also match a ticker search), `last.price`, ts epoch 1786639261 = **2026-08-13T16:41:01Z** |
| Change vs. prior close | **+$204.17 / +15.19%** | IBKR `change` field |
| Bid / Ask | $1,547.50 / $1,549.07 | IBKR `get_price_snapshot` |
| 52-week range | Low **$42.82** · High **$2,354.39** · Open (52w ago) $47.02 | IBKR `misc_statistics` |
| US 10Y Treasury yield | 4.70% | FRED `DGS10`, as of 2026-08-11 |

**$1,548.46 is used as the live price for this session** — fetched fresh via IBKR, not inferred from any multiple, not carried from the prior session's $1,257.11, and not taken from the Telegram post's characterization of the move.

---

## 2. Data Gathered — Sources & Method

### 2.1 Underlying financials — unchanged since the 2026-08-05 session

No new 10-K, 10-Q, or 8-K carrying financial statements has been filed since the 2026-08-05 Q4/FY2026 8-K already used to score SNDK in the prior session. SanDisk's fiscal year runs to early July; **FY2027 will not close until ~July 2027**, so there is no new completed fiscal year to fold into the Quality Score's trailing-window calculations. Every fundamental figure below (FY2026 revenue, gross profit, operating income, net income, FCF, balance sheet, share count) is therefore **identical to the 2026-08-05 session** — re-confirmed, not re-derived. See [sessions/2026-08-05-new-position-sndk.md §2.1–2.2](2026-08-05-new-position-sndk.md) for the full primary-sourced GAAP statements.

**Carried-forward figures used again this session:**

| Metric | FY2026 value | Source |
|---|---|---|
| Revenue | $20,248M | 8-K filed 2026-08-05, Exhibit 99.1 |
| Gross profit | $14,472M | same |
| Operating income (EBIT) | $12,389M | same |
| Net income | $11,433M | same |
| Free Cash Flow (OCF − CapEx) | $11,494M | same |
| Cash and cash equivalents | $4,762M | balance sheet as of 2026-07-03 |
| Total debt | $0 | same — debt-free |
| Shares outstanding | 149M | same balance sheet; also cross-checked against stockanalysis.com's live "Shares Outstanding: 149.00M" this session |
| FCF/NI ratio (FY2026, meaningful year) | 100.53% | same |
| Net Debt/EBITDA | −0.38× | same |

### 2.2 What's new this session

- **Live price**, up 15.19% intraday (§1) — the single largest driver of this session's score changes.
- **10Y Treasury yield**: 4.70% (was 4.63% on 2026-08-05) — a modest 7bp increase, stays within the same 3.5–5% Rate Regime bracket.
- **Forward consensus EPS**: stockanalysis.com's FY2027 consensus EPS is now **$213.23** (was $212.95 on 2026-08-05) — essentially unchanged, confirming the Street's earnings estimate itself didn't move materially even as the price did.
- **New long-term (FY2028–2030) guidance framework** disclosed at the Investor Day (§0) — cited for context, **not scored** (see above).
- **No newer TrendForce/IDC NAND vendor-share data found this session** — a fresh search turned up nothing more recent than the Q1 2026 figure (SanDisk 13.9%) already carried forward from 2026-08-05. Moat Signal evidence is therefore unchanged.

### 2.3 Moat evidence — re-checked, unchanged from 2026-08-05

| Signal | Result | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** (unchanged) | Still Q1 2026 TrendForce data (13.9%, up from 12.4% Q3 2025) — no Q2/Q3 2026 update found this session either. |
| Brand premium | **FALSE** (unchanged) | No third-party citation of a company-specific sustained price premium without volume loss; ASP surge remains industry-wide. |
| Network effect | **FALSE** (unchanged) | Hardware/component manufacturer. |
| Switching costs | **TRUE** (unchanged) | Same cited "lengthy product qualification" mechanism from SanDisk's own 10-K risk factors. |
| Scale cost advantage | **FALSE** (unchanged) | No cost-per-unit ($/GB) citation vs. peers found this session. |

```
Moat_Score = (2 of 5 TRUE) / 5 × 100 = 40.0   — unchanged
```

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology, unchanged version)

**No new fundamental data exists to change any Quality Score sub-score since the 2026-08-05 session** (§2.1). The hard-disqualifier rolling-window question that drove that session's central judgment call has since been **formally resolved and documented as a standing framework rule** — see the "Rolling-window clarification (2026-08-05)" note now permanently in [quality-scoring.md](../framework/quality-scoring.md)'s Hard Disqualifiers section, and [decisions/2026-08-05-framework-clarification-fcf-disqualifier-rolling-window.md](../decisions/2026-08-05-framework-clarification-fcf-disqualifier-rolling-window.md). This session applies that now-settled rule directly, without re-litigating it as two competing readings.

**Hard disqualifier re-check (current trailing window, unchanged from 2026-08-05):**

| Disqualifier | Window tested | Result |
|---|---|---|
| FCF not positive for 3+ consecutive years | FY2024 (−$475M), FY2025 (−$120M), FY2026 (+$11,494M) — rolling 3yr window, per the now-settled rule | **Does not fire** |
| FCF/NI conversion <70% for 2+ consecutive meaningful years | Only 1 economically meaningful year exists (FY2026, 100.53%) — well above 70% | **✅ PASS** |
| Net Debt/EBITDA over threshold | −0.38× (net cash) | **✅ PASS** |

**Quality Score computation (identical inputs to 2026-08-05 — reproduced for "no black-box" compliance, not re-derived):**

```
Profitability (25%): NetMargin_Component 100.0 (capped) + ROIC_Component 100.0 (capped) → 100.0
Margins (15%):       Gross Margin 71.4737% → GrossMargin_Score 89.3421 (no trend-bonus eligible, already >40%)
Growth (20%):        3yr Revenue CAGR 49.28% (FY2023→FY2026) → capped 100.0
Balance Sheet (15%): Net Debt/EBITDA −0.3799× → 100.0
Moat (15%):          2 of 5 signals TRUE → 40.0
FCF Quality (10%):   FY2026 FCF/NI 100.53% → capped 100.0

Quality Score = 100.0×0.25 + 89.3421×0.15 + 100.0×0.20 + 100.0×0.15 + 40.0×0.15 + 100.0×0.10
             = 25.00 + 13.4013 + 20.00 + 15.00 + 6.00 + 10.00
             = 89.4013 → rounds to 89.4
```

**Quality Score = 89.4 — PASSES the 80.0+ gate** (same result as 2026-08-05, now under the settled — not contested — rolling-window rule). Phase 02 valuation scoring proceeds.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test:**

```
Forward PE = Live Price / FY2027 consensus EPS = $1,548.46 / $213.23 = 7.2629×
EY = 1 / 7.2629 = 13.7686%
Spread = EY − 10Y = 13.7686% − 4.70% = +9.0686pp
```

⚠️ Same data-quality flag as 2026-08-05: this consensus EPS implies aggressive forward earnings growth this session does **not** take at face value for the DCF/multiples fair-value work below — used here only for the Rate Gate's market-observable EY test, per the framework's convention of not scoring self-reported/Street figures directly.

**Pass threshold: Spread ≥ +1.5%. Result: PASS, comfortably** (+9.07pp cushion) → no Step 1 additive.

**Step 2 — Rate Regime Modifier:** 10Y yield 4.70% falls in the **3.5–5% bracket → +5**.

**Total Rate Modifier for SNDK = +5.**

---

## 5. Phase 02 — Valuation Score

### 5.1 PEG eligibility

Unchanged from 2026-08-05: SanDisk's EPS history (GAAP losses FY2023–25, one extraordinary profitable year FY2026) still does not meet the "EPS growth >15% for 3+ years on a clean, non-distorted earnings base" Fast-Grower test. **PEG not applicable; 15% weight redistributed to EV/EBIT** (EV/EBIT effectively 40%).

### 5.2 Market cap / EV inputs (fresh live price, unchanged fundamentals)

```
Shares outstanding = 149M (unchanged, §2.1)
Market Cap = $1,548.46 × 149M = $230,720.54M
EV = Market Cap + Total Debt − Cash = 230,720.54 + 0 − 4,762 = $225,958.54M
```

### 5.3 Sub-scores

```
FCF Yield (40% weight):
  FCF Yield = FY2026 FCF / Market Cap = 11,494 / 230,720.54 = 4.9817%
  FCF_Score = clamp(100×(1 − 4.9817/10), 0, 100) = 50.18

EV/EBIT (40% weight, redistributed from PEG):
  EV/EBIT = 225,958.54 / 12,389 = 18.2386×
  EV/EBIT_Score = clamp((18.2386−12)/23×100, 0, 100) = clamp(27.1243, 0, 100) = 27.12

Forward PE (20% weight):
  No-history fallback — SNDK has traded standalone only since 21 Feb 2025 (~18 months),
  still well short of the 5yr/20-quarter minimum. Same fallback as both prior sessions.
  FwdPE_Score = 50.0   (neutral, flagged)

PEG (15% weight): N/A — redistributed to EV/EBIT (§5.1)
```

```
Raw weighted = FCF_Score×0.40 + EV/EBIT_Score×0.40 + FwdPE_Score×0.20
             = 50.18×0.40 + 27.12×0.40 + 50.0×0.20
             = 20.072 + 10.848 + 10.00
             = 40.92
```

### 5.4 Fair Value — carried forward, not re-derived from scratch, and why

**Blended Fair Value = $1,214.25 (carried forward unchanged from the 2026-08-05 session).** This is a deliberate choice, not an oversight — reasoning shown in full since it's the single most consequential judgment call in this session:

1. **No new audited/primary-sourced financial data exists** to feed a different DCF or multiples calculation — the 2026-08-05 session's Bull/Base/Bear FCF paths, WACC assumptions, and terminal-value work were all built from FY2026 actuals and SNDK's own trading-history-derived beta estimate, none of which have changed (§2.1).
2. **The new information this session (the Investor Day's FY2028–2030 targets) is exactly the category of input the framework's "Why Forward Guidance Is Not a Sub-score" section excludes from valuation work** — company-issued, unaudited, forward-looking, and (per that section's own reasoning) subject to the same gameable-input concern the FCF/NI conversion check was built to guard against. The 2026-08-05 session already explicitly declined to build its DCF off Street consensus or company guidance, instead using its own conservative, independently-derived scenario dollar figures — today's event doesn't change the soundness of that prior discipline, it just adds another data point of the same (excluded) category.
3. **Rule 9's "mandatory re-valuation upon guidance revision" is satisfied by re-running the full score** (fresh live price, fresh 10Y yield, fresh sub-scores, fresh Upside/Downside Modifier gap-to-FV calculation below) — it does not require inventing a new Blended FV number when no new fundamental data exists to justify moving it. Re-deriving a brand-new DCF anchored on the company's own newly-disclosed long-term margin targets would risk exactly the "invent/estimate financial data" failure mode this framework is built to avoid — an 80% *through-cycle* gross margin has no historical precedent for a commodity memory manufacturer (see the DRAM/NAND glossary characterization: "commoditized, boom-bust cyclical businesses with little durable pricing power"), and taking management's own claim about sustaining it at face value would substitute self-reported guidance for genuine bottom-up valuation work.
4. **This is flagged as a conservative, not aggressive, choice**: the live price ran up 15.19% while the fair-value estimate held flat, which — as shown in §5.5 below — makes the Upside/Downside Modifier meaningfully *less* favorable this session (bigger implied overvaluation gap), not more. A stale-FV critique would cut toward "the score should look even more expensive than it does," not the reverse.

**Sanity cross-check against analyst targets (unchanged discipline — never the rosy point):** current analyst consensus average price target is **$2,053.50** (23 analysts, "Strong Buy" consensus, per stockanalysis.com this session) — down slightly from the 2026-08-05 session's cited $2,218 average (a modest *decrease* in the average target despite the price rally, consistent with some analysts flagging "may already be pricing in peak earnings," per RBC's Srini Pajjuri, cited in the prior session). The $1,214.25 PW Blended FV sits well below this average, consistent with Rule 7's guardrail to use the scenario-weighted PW figure, never a single optimistic target.

*(Full DCF/Multiples scenario tables — bull/base/bear FCF paths, WACC 11%/15%/16%, terminal value work — are reproduced in [sessions/2026-08-05-new-position-sndk.md §5.4](2026-08-05-new-position-sndk.md#5-phase-02--valuation-score) and not repeated here verbatim; only the live-price-dependent outputs below are recomputed.)*

### 5.5 Upside/Downside Modifier

```
Gap Upside % = (PW FV / Live Price) − 1 = (1,214.25 / 1,548.46) − 1 = −21.5832%

Catalyst window: no narrower catalyst identified this session either — default 2yr per rule.
Annualized gap = −21.5832% / 2 = −10.7916%/yr

Intrinsic growth rate: unchanged +5.00%/yr structural estimate (same reasoning as 2026-08-05 —
  a longer-horizon estimate net of the cyclical normalization already priced into the gap term;
  NOT taken from today's Investor Day guidance, consistent with §5.4's discipline).

Shareholder yield: no dividend. Net buyback yield recomputed against TODAY's market cap
  (same FY2026 trailing buyback dollars, since no new fiscal-year data exists):
  = (FY2026 buybacks $4,524M − issuance $53M) / today's Market Cap $230,720.54M
  = 4,471 / 230,720.54 = 1.9381%

E = −10.7916% + 5.00% + 1.9381% = −3.8535%
```

`E` is negative → expected-loss band:

```
M = +5 + 10 × clamp((−E)/10pp, 0, 1) = +5 + 10 × clamp(3.8535/10, 0, 1) = +5 + 3.8535 = +8.8535 → +8.85
```

Guardrail check: modifier is positive (score-raising, trim-pressure direction) — the "no catalyst caps the *upside* (negative) side at −5" guardrail doesn't bind here (that guardrail only constrains the attractive/negative-modifier side).

**Upside/Downside Modifier = +8.85** — meaningfully larger than the 2026-08-05 session's +2.16, entirely because the price ran up ~15% while the fair-value anchor held flat (§5.4), pushing the expected-return estimate `E` from mildly positive (+5.68%) to negative (−3.85%).

### 5.6 Final Valuation Score

```
Final Score = 40.92 (raw weighted, §5.3) + 5 (Rate Modifier, §4) + 8.85 (Upside/Downside Modifier, §5.5)
            = 54.77 → rounds to 54.8
```

**Valuation Score = 54.8** — up from 37.4 on 2026-08-05, and now in the **50.0–69.9 "Fair Value / Hold, no new entry" band** if read as a standalone valuation score. (The Composite Score, not the raw valuation score, is the governing number once a Quality Score exists — see §6.)

---

## 6. Composite Score

```
Composite Score = 0.50×(100 − Quality Score) + 0.50×Valuation Score
                = 0.50×(100 − 89.4) + 0.50×54.8
                = 0.50×10.6 + 0.50×54.8
                = 5.30 + 27.40
                = 32.70 → 32.7
```

**Composite Score = 32.7** (up from 24.0 on 2026-08-05) → per the Composite Score action table, **Score 30.0–49.9 → BUY — Standard position 3–5%** (moved down one tier from the prior session's "Full position 6–8%" band — the live-price rally is the entire driver of this shift, since both raw scores that feed the composite moved in the expensive direction while Quality Score held flat).

---

## 7. Fair Value + Order Setup — computed per the operating brief (required for any BUY-band action), but see the R/R gate finding below

**MoS / Max-Loss band for Composite Score 32.7 (the 30.0–49.9 tier): MoS 25–30%, Max Acceptable Loss 25–30%.** Before picking a specific value within that range, the R/R ratio is checked across the *entire* range, since it turns out to be decisive regardless of which specific value is chosen:

```
R/R (base case) = MoS / [(1 − MoS) × Max Loss]     — derived algebraically from the order-setup formulas

Best case within this band (MoS 30%, Max Loss 25%): R/R = 0.30 / (0.70 × 0.25) = 0.30/0.175 = 1.7143:1
Worst case within this band (MoS 25%, Max Loss 30%): R/R = 0.25 / (0.75 × 0.30) = 0.25/0.225 = 1.1111:1
```

**Every combination of MoS and Max Loss allowed for this score band produces a base-case R/R between 1.11:1 and 1.71:1 — below the 2:1 minimum in every case.** This is a robust finding, not an artifact of picking an unfavorable point in the range. Full checklist shown using the *best-case* combination (MoS 30%, Max Loss 25%) — i.e., even under the most favorable legal choice, the gate still fails:

```
[x] Composite Score (drives action band):        32.7   (30.0–49.9 → Standard-position entry indicated, nominally)
[x] Raw Valuation Score (incl. Upside/Downside):  54.8
[x] Expected annual return E / catalyst window:   −3.85% / 2yr
[x] Upside/Downside Modifier applied:             +8.85
[x] Blended Fair Value (PW, Rule 7, carried fwd): $1,214.25   (§5.4 — not re-derived this session)
[x] Margin of Safety %:                           30%   (top of the 25–30% band — used since it's the
                                                          best case for R/R; still fails, see below)
[x] BUY PRICE (limit):      $1,214.25 × (1 − 0.30)                  = $849.98
[x] PRIMARY SELL TARGET:    = Blended FV                            = $1,214.25
[x] BULL-CASE TRIM TARGET:  $2,469.0 × 0.90 (unchanged Bull Blended FV, §5.4) = $2,222.10
[x] STOP LOSS:               $849.98 × (1 − 0.25)                   = $637.48   (bottom of the
                                                                         25–30% Max-Loss band — also
                                                                         chosen for the best-case R/R)
[✗] Risk/Reward Ratio (base-case, Primary Sell Target):
      ($1,214.25 − $849.98) / ($849.98 − $637.48) = $364.27 / $212.50 = 1.7143:1   — FAILS the 2:1 minimum,
                                                                                       even in the best case
[x] Risk/Reward Ratio (bull-case, Trim Target):
      ($2,222.10 − $849.98) / $212.50 = $1,372.12 / $212.50 = 6.457:1   — clears comfortably
[x] Max $ Risk (1.5% of portfolio ≈$65,925.08, per holdings.md's 2026-08-09 sync — informational
                                    only, since no order is placed this session):        $988.88
[x] Shares at that risk budget: $988.88 / $212.50 = 4.65 → 4 shares (risk-based)
[x] Position Size cap check: 5% of portfolio = $3,296.25 → 3.88 shares → 3 shares (cap-based, binding)
[x] Position Size ($) — informational only, no order placed:  3 × $849.98 = $2,549.94 (≈3.87% of portfolio)
```

**The base-case Risk/Reward Ratio fails the 2:1 minimum across the entire allowed MoS/Max-Loss range for this score band (1.11:1 to 1.71:1) — not a borderline or choice-sensitive result.** Per fair-value-methodology.md: *"If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely."* Per operating-brief.md's BUY/SELL ORDER SETUP rule, this is a hard, independent gate. **No entry is placed this session.**

---

## 8. Recommendation

# **WATCHLIST ONLY — do not enter. Composite Score (32.7) nominally supports a Buy-Standard-position signal (3–5%), but the base-case Risk/Reward Ratio (best case 1.71:1, worst case 1.11:1 within the allowed band) independently fails the 2:1 minimum gate across its entire range. No position opened.**

This is the same bottom-line outcome as the 2026-08-05 session (WATCHLIST ONLY, no entry), but reached through a materially different path:

1. **The Quality Score gate still PASSES (89.4, unchanged)** — no new fundamental data exists to move it either direction (§3). The rolling-window interpretive question that made the 2026-08-05 session's gate outcome a genuine judgment call has since been formally settled as a standing framework rule (§3 above); this session applies that settled rule directly.
2. **The Composite Score moved from 24.0 to 32.7 — still nominally in a BUY band, but one tier down (Full-position 6–8% → Standard-position 3–5%)** — driven entirely by the 15.19% intraday price rally (§1), which simultaneously widened the FCF Yield and EV/EBIT sub-scores toward "more expensive" and swung the Upside/Downside Modifier's expected-return estimate `E` from mildly positive (+5.68%, 2026-08-05) to negative (−3.85%, this session) against an unchanged fair-value anchor (§5.4–5.5).
3. **The Risk/Reward gate FAILS again, and more decisively this time** — not a knife-edge 1.00:1 as on 2026-08-05, but a full range (1.11:1 to 1.71:1) that never reaches 2:1 regardless of which allowed Margin-of-Safety/Stop-Loss combination is chosen (§7). The rally pushed the live price further from a Buy Price still anchored to the same $1,214.25 fair value, mechanically compressing the achievable reward-to-risk ratio.

**Net effect: today's Investor Day reaffirmed the bull thesis qualitatively (new FY2028–2030 targets, a large TAM, tight supply into 2028) but did not — and by this framework's explicit design, could not — move the scored fair value, because none of the new information is admissible as a scored input** (§5.4). The stock got materially more expensive relative to an unchanged, independently-derived fair-value estimate. This is the intended behavior of the framework's guidance-exclusion rule working as designed: a company can have genuinely good news and still fail the R/R gate if the market price already runs ahead of the number the framework is willing to underwrite.

**What would change this:** a pullback toward the $849.98 buy-price limit (a ~45% decline from today's live price) would clear the MoS entry condition at the best-case band parameters, but the R/R math would still need to be rechecked at that time against whatever fair-value estimate is current then — no limit order is placed this session.

---

## 9. Next Review Trigger

- **SanDisk's FY2027 Q1 earnings** (next quarterly print, expected ~November 2026 per the FY2026 filing cadence) — the first real test of whether the guided $10.3–10.8B revenue / 83–85% gross margin range holds, and the first data point on whether the FY2028–2030 long-term targets disclosed today are tracking.
- **Any SEC filing (8-K, 10-K) carrying updated financial statements** — the current DCF/Multiples fair-value work (§5.4) remains carried forward from 2026-08-05 until genuinely new fundamental data exists to justify re-deriving it.
- **Standard Rule 9 triggers:** any further guidance revision, management change, material M&A, macro shift, or a >15% unexplained price move (this session's own +15.19% move was explained by a documented fundamental trigger — the Investor Day — so does not itself separately qualify as an "unexplained" move).
- **A pullback toward the $849.98 buy-price limit** — would warrant a fresh R/R recheck, not an automatic entry.
- **Updated TrendForce/IDC NAND vendor-share data** — still carried forward unchanged from Q1 2026.

---

## 10. Watchlist & Stale-Score Housekeeping

- **New watchlist entry:** [watchlist/not-in-portfolio/SNDK/SNDK-2026-08-05.md](../watchlist/not-in-portfolio/SNDK/SNDK-2026-08-05.md) updated with a new dated row (2026-08-13) — warranted per [watchlist/README.md](../watchlist/README.md)'s "Rule 9 fundamental-event trigger fires... even if the score/action ends up unchanged, the reasoning has changed and is worth a fresh pointer" clause (score and composite both changed materially here, in addition to the Rule 9 trigger).
- **Stale-score mechanism:** not applicable — methodology version (2026-06-29) unchanged since the prior entry; nothing to clear in [STALE.md](../watchlist/STALE.md).
- **Framework files changed this session:** none — this session applies existing, already-settled rules (the rolling-window disqualifier clarification is now permanent framework text, not re-litigated here).
- **Glossary:** two new terms added — "Investor Day" and "New Business Model (SanDisk)" — see [framework/glossary.md](../framework/glossary.md).

---

## 11. Glossary

*(Pulled from [glossary.md](../framework/glossary.md); two new terms added this session)*

| Term | Meaning |
|---|---|
| **8-K** | A US-listed company's SEC filing disclosing a material event — SanDisk's most recent (2026-08-05) remains this session's primary financial-data source; no newer one has been filed. |
| **Adjusted FCF margin** | A company's own non-GAAP free-cash-flow-as-a-percentage-of-revenue metric — SanDisk guided a long-term (FY2028–2030) target of ≈50% at its 2026-08-13 Investor Day. Self-reported guidance, cited for context only, never a scored input under this framework's "guidance is a trigger, not a score" rule. |
| **Beta** | A stock's sensitivity to overall market moves — used in a DCF's WACC; SNDK's estimated beta (2.0, carried forward from 2026-08-05) is unchanged this session. |
| **Buyback yield (net buyback yield)** | The rate at which a company's share count shrinks per year from repurchasing its own stock, net of new issuance — a shareholder-yield component; recomputed this session against the new, higher market cap. |
| **CIK (Central Index Key)** | The SEC's unique numeric filer identifier — SanDisk's is 0002023554. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking (`0.50 × (100 − Quality Score) + 0.50 × Valuation Score`) — 32.7 for SNDK this session, up from 24.0 on 2026-08-05. |
| **DCF** | Discounted Cash Flow — a valuation method; this session's Blended Fair Value is carried forward from the 2026-08-05 DCF/Multiples work rather than re-derived (§5.4). |
| **EBIT/EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, D&A. |
| **EV/EBIT** | Enterprise Value ÷ operating profit — a valuation multiple; this session's redistributed (40%-weight) sub-score. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE — used in the Rate Environment Gate's Step 1 test. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income — central to the Quality Score hard-disqualifier check and the FCF Yield sub-score. |
| **GAAP** | Generally Accepted Accounting Principles — the standard scored across this framework, in preference to any company's own Non-GAAP presentation (including today's Investor Day targets, all disclosed non-GAAP). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted score — re-checked (not re-litigated) this session against the now-settled rolling-window rule. |
| **Investor Day** | A company-hosted event (distinct from a routine quarterly earnings call) where management presents a broader, often multi-year strategic and financial outlook to investors and analysts — SanDisk's first as a standalone company, held 2026-08-13. Like quarterly guidance, an Investor Day's forward-looking targets are self-reported management commentary: this framework treats it as a mandatory Rule 9 re-valuation *trigger*, never as a scored input in its own right. *(New term.)* |
| **New Business Model (SanDisk)** | SanDisk's term for shifting a growing share of its NAND output from spot/commodity-style sales to long-term supply agreements with customers — guided at the 2026-08-13 Investor Day to reach ~50% of bits sold in FY2027 and ~two-thirds in FY2028. If realized, this would reduce near-term revenue/margin volatility versus the historical commodity-cycle pattern, but as company-guided forward commentary it is not treated as a scored input, and this framework's Fair Value work (§5.4) does not assume its full realization. *(New term.)* |
| **Non-GAAP** | A company's own adjusted presentation, not independently audited to the GAAP standard — every FY2028–2030 target disclosed at today's Investor Day is non-GAAP; shown for context only, never scored. |
| **PW (Probability-Weighted) Fair Value** | This framework's blended fair value — 25% bull + 50% base + 25% bear — $1,214.25 for SNDK, carried forward unchanged from 2026-08-05 this session. |
| **Quality Score** | This framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to reach Phase 02. SNDK: 89.4, unchanged from 2026-08-05. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss on a trade — minimum 2:1 to enter; SNDK's base-case R/R (1.11:1–1.71:1 depending on MoS/stop choice within the allowed band) is the gate that blocks entry this session. |
| **ROIC** | Return on Invested Capital — 99.16% for SNDK (unchanged, cycle-peak reading). |
| **TrendForce** | An independent semiconductor/memory-industry market-research firm — SanDisk's NAND market-share evidence source; no newer data found this session, carried forward from Q1 2026. |
| **WACC** | Weighted Average Cost of Capital — the DCF discount rate; unchanged this session (11% Bull / 15% Base / 16% Bear, from 2026-08-05). |

# NEW POSITION — FICO (Fair Isaac Corporation) — 2026-06-14

**Task type:** NEW POSITION
**Date:** 14 Jun 2026
**10Y US Treasury Yield:** 4.49% (CNBC/TradingEconomics, market close Fri 12 Jun 2026 — most recent available; markets closed Sun 14 Jun)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket) — **not reached**, see below
**Current FICO portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md)), no prior watchlist entry
**Sector:** Financial analytics / scoring software — Scores segment (the FICO Score, a near-monopoly standard in US consumer lending) + Software segment (decisioning/analytics platforms for fraud, marketing, and credit decisions)

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$1,179.19** | WebSearch query 1: "FICO Fair Isaac stock price today" returned $1,179.19 with market cap $27.35B (consistent with $1,179.19 × 23.72M shares ≈ $27.96B). WebSearch query 2 (targeted): "FICO stock closing price June 12, 2026" independently confirmed **$1,179.19** as the Fri 12 Jun 2026 close. Two independent cross-checking queries agree. |
| 52-week range | $870.01 – $1,998.01 | WebSearch (aggregator, query 1) |
| Analyst consensus PT | ~$1,527.50 avg (20 analysts, range $707–$2,400); narrower "Buy"-only cohort (13 analysts) avg $1,715 (range $1,150–$2,200). Consensus rating "Buy" (16 buy / 4 hold / 1 sell of 20) | WebSearch (aggregator, query 2) |

**Context:** $1,179.19 sits roughly **41% below the 52-week high** ($1,998.01) and **~35% above the 52-week low** ($870.01) — meaningfully below the mid-point of its 52-week range, and **23–31% below the analyst consensus PT cluster** (~$1,527–$1,715).

⚠️ **Tooling flag:** Per the batch-level note, IBKR `get_price_snapshot` / `search_contracts` MCP tools were not attempted (prior agents in this batch received "permission denied"). WebSearch was used directly with 2 independent cross-checking queries returning the same figure ($1,179.19, 12 Jun 2026 close), internally consistent with the implied market cap from shares outstanding — treated as reliable.

---

## 2. Data Gathered (Phase 01 & 02 Inputs) & Gaps Flagged

### Revenue / Net Income / EPS history (fiscal year ends ~Sept 30)

| Fiscal Year | Revenue | YoY | GAAP Net Income | GAAP Diluted EPS | EPS YoY |
|---|---|---|---|---|---|
| FY2022 | $1.38B (10-K, "record revenues") | — | $374M | $14.18 | — |
| FY2023 | $1,513.557M | +10% | $429.4M | $16.93 | +19% |
| FY2024 | $1,717.526M | +13.4% | $513M | $20.45 / $20.78 | +21% |
| FY2025 | $1,990.869M | +15.9% | $651.9M / $652M | $26.54 / $26.90 | +27–30% |
| TTM (to 31 Mar 2026) | $2.256B | +22.6% | — | — | — |
| Q2 FY2026 (quarter) | $692M | +39% | — | — | EPS +69% YoY |

Sources: FICO 8-K quarterly/annual earnings releases (SEC EDGAR, exhibit 99.1 each quarter), cross-checked against FY2025 Annual Report and stockanalysis.com.

⚠️ Two FY2025 figures appear across sources for revenue ($1.991B per 10-K income statement vs. "$2.06B" per a market-cap-style aggregator) and EPS ($26.54 vs $26.90, and net income $651.9M vs $652M) — both pairs are within rounding distance of each other (likely GAAP-as-reported vs. a slightly different share-count/rounding basis). Used the 10-K-sourced figures ($1,990.869M revenue, $651.9M NI, $26.54 EPS) as primary; the aggregator figures are noted as cross-checks and do not change any threshold pass/fail.

### Revenue CAGR 3yr (FY2022 → FY2025)

```
3yr CAGR = (1,990.869 / 1,380)^(1/3) − 1 = 12.94%
```
(Using the $2.06B aggregator figure instead: (2,060/1,380)^(1/3) − 1 = 14.27%. Either way >10%.)

### Gross Margin trend (GAAP)

| FY | Cost of Revenue | Revenue | Gross Margin % |
|---|---|---|---|
| FY2023 | $311,053K | $1,513,557K | 79% |
| FY2024 | $348,206K | $1,717,526K | 80% |
| FY2025 | $353,722K | $1,990,869K | 82% |

Source: FICO FY2025 8-K / 10-K (cost of revenue as % of revenue stated directly: 21% FY2023 → 20% FY2024 → 18% FY2025). TTM gross margin 82.86% (stockanalysis.com) — consistent with the trend continuing into FY2026.

**Gross margin is >40% and structurally expanding** — 79% → 80% → 82% over 3 years, driven by strong operating leverage (cost of revenue +2% vs. revenue +16% FY2024→FY2025).

### Free Cash Flow / FCF-NI conversion

| FY | FCF | YoY | Net Income | FCF/NI |
|---|---|---|---|---|
| FY2022 | $503M (10-K, "+21% from previous year" → implies FY2021 ≈ $416M) | +21% | $374M | 134.5% |
| FY2024 | ≈$605.7M (implied: FY2025's $739M is stated as "+22% YoY") | — | $513M | ≈118.1% |
| FY2025 | $739M ("record annual free cash flow," +22% YoY) | +22% | $651.9M | ≈113.3% |
| TTM | $750.59M (stockanalysis.com: OCF $758.89M − CapEx $8.31M) | — | — | — |

**FCF positive for all years shown (FY2022/2024/2025, and implied FY2023), and FCF/NI conversion is well above 70% for both of the last two fiscal years** (118.1% FY2024, 113.3% FY2025).

### Capital expenditure / Owner Earnings (Upgrade 1) check

TTM CapEx is **$8.31M** against TTM revenue of ~$2.26B — **~0.4% of revenue**, immaterial. FICO is an asset-light software business (no manufacturing, minimal physical infrastructure). **Upgrade 1 (Owner Earnings) does not apply** — raw FCF is not understated by capex treatment here; CapEx is too small for the growth/maintenance split to matter.

### Balance sheet / leverage (most recent quarter: Q2 FY2026, ended 31 Mar 2026)

| Metric | Value | Source |
|---|---|---|
| Total debt | $3.64B (93% senior notes, weighted avg rate 5.5%; includes new $1B senior notes due 2034 issued in the quarter, redeeming $400M due May) | FICO Q2 FY2026 10-Q / earnings call |
| Cash & marketable investments | $272M | FICO Q2 FY2026 10-Q / earnings call |
| **Net debt** | **≈$3.368B** ($3.64B − $0.272B) | Computed |
| TTM EBITDA | ~$1.33B (implied by company-stated ratio below) | GuruFocus / company disclosure |
| **Net Debt/EBITDA** | **2.61×** (company-stated, "well below maximum covenant of 3.5×") | FICO Q2 FY2026 earnings call — directly disclosed |
| Total stockholders' equity (FY2025) | **−$1.7B to −$1.8B (deficit)** | FICO FY2025 10-K |
| Credit rating | **Ba2 (Moody's, Corporate Family Rating), stable outlook — sub-investment grade ("junk")** | Moody's rating action (Yahoo Finance / Moody's) |

⚠️ **Negative equity flag (per session brief):** FICO's FY2025 GAAP stockholders' equity is **−$1.7B to −$1.8B** (a deficit), driven by a multi-year, aggressive buyback program (3-yr buyback ratio +4.00%; most recently a new $2B repurchase program authorized 8 Jun 2026, funded partly by a new $1.5B term loan for an accelerated share repurchase). **Conventional ROE/ROIC (Net Income ÷ Equity) is undefined/meaningless here** — dividing positive net income by negative equity produces a negative "ROE" that does not reflect economic reality. Per "never invent or estimate financial data," I did not compute this ratio myself. Instead I report what aggregators show using **invested-capital-based ROIC methodologies** that sidestep the negative-equity denominator (see ROIC row below) — consistent with the MA 2026-06-07 precedent of flagging a substitution rather than forcing a distorted figure.

### Share issuance pattern

FICO has run a sustained, large-scale **buyback** program, not an issuance program: 3-Year Share Buyback Ratio +4.00% (10yr range −17.2 to +10.2, per GuruFocus); a $1B program (effective June 2025) was completed and replaced by a $1.5B program (Feb 2026), itself just replaced by a **new $2B program** (authorized 8 Jun 2026) — partly funded by a newly drawn $1.5B term loan used for an accelerated share repurchase (~1,055,100 shares prepaid to Wells Fargo Securities). **Not dilutive — clearly the opposite.**

### ROIC (flagged per negative-equity quirk)

| Source | Figure | Basis |
|---|---|---|
| GuruFocus / aggregator | 5-yr average ROIC **59.6%** | Among "best business services companies" — invested-capital basis |
| AlphaSpread | ROIC excl. cash, goodwill, intangibles **143.9%** | Invested-capital basis, more recent period |

Both figures are **aggregator-computed using invested-capital (not book-equity) denominators**, which is the appropriate substitution given FICO's negative GAAP equity. Both are far above the >15% threshold. **PASS, with the flag above** — used as-reported rather than recomputed from NI/Equity (which would be undefined/negative).

### Forward PE / 10yr Avg PE / EV/EBIT / PEG

| Metric | Value | Source |
|---|---|---|
| Forward PE | 24.23× | GuruFocus |
| Trailing PE | 36.10–40.33× (range across sources/dates — fullratio cites 37.91 as of 8 Jun 2026, "21% below the 10yr average of 48.21") | macrotrends / fullratio / GuruFocus |
| **10yr Avg PE** | **48.21×** (10yr high 93.53× in Sep 2024 quarter, 10yr low 28.73× in Sep 2022 quarter — a range *is* available) | macrotrends |
| EV/EBITDA | 28.74× | AlphaSpread |
| PEG (reported) | 0.87 | GuruFocus |
| Shares outstanding | 23.72M | stockanalysis.com |

### EV/EBIT inputs (computed)

```
Market Cap   = $1,179.19 × 23.72M ≈ $27,966.27M (≈$27.97B)
Net Debt     = $3,368M (computed above)
Enterprise Value = $27,966.27M + $3,368M ≈ $31,334.27M (≈$31.33B)
```

**TTM EBIT (operating income), computed via rollforward:**
```
FY2025 full-year operating income            = $925M       (FY2025 10-K)
− H1 FY2025 (6mo ended 31 Mar 2025)           = $425.176M   (FY2025 10-Q)
+ H1 FY2026 (6mo ended 31 Mar 2026)           = $636.514M   (FY2026 10-Q)
= TTM EBIT (Apr 2025 – Mar 2026)              = $1,136.338M
```

```
EV/EBIT (TTM) = $31,334.27M ÷ $1,136.338M ≈ 27.58×
```

⚠️ A separately-cited "EBIT of $990.3M" appears in one aggregator search result (likely an FY2025-only or slightly stale TTM figure) vs. my rollforward computation of $1,136.338M from primary-source quarterly operating income figures. Using $990.3M instead: EV/EBIT = $31,334.27M ÷ $990.3M ≈ 31.64×. I used the **rollforward from primary-source 10-Q/10-K operating income figures** ($1,136.338M / 27.58×) as the more directly traceable number, and flag the alternate for the record. (Both values are used in the EV/EBIT_Score sensitivity check in §5, in the event scoring is reached.)

### Data Gaps / Flags Summary

1. IBKR price-snapshot/contract-search MCP tools not attempted (per batch-level note) — used WebSearch, 2 independent cross-checking queries, consistent results.
2. Minor revenue/EPS figure discrepancies across sources (10-K $1,990.869M vs aggregator $2.06B; EPS $26.54 vs $26.90) — both pairs within rounding distance, does not change any Phase 01 threshold result.
3. TTM EBIT has a discrepancy between my rollforward computation ($1,136.338M, from primary-source 10-Q/10-K operating income) and an aggregator figure ($990.3M) — used the rollforward as primary, flagged the alternate.
4. **ROIC**: FICO's GAAP stockholders' equity is negative (−$1.7B to −$1.8B, FY2025), making conventional Net Income ÷ Equity ROIC undefined/meaningless. Used aggregator-reported invested-capital-basis ROIC (59.6% 5yr avg / 143.9% ex-cash-goodwill-intangibles) instead of computing a distorted figure myself — flagged explicitly per "never invent or estimate."
5. No metric was invented or estimated; all figures trace to FICO 8-K/10-Q/10-K filings (SEC EDGAR), the FY2025 Annual Report, the Q2 FY2026 earnings call, or named aggregators (stockanalysis.com, macrotrends, fullratio, GuruFocus, AlphaSpread), with derivations shown explicitly.

---

## 3. Phase 01 — Quality Gate

| Check | FICO Value | Threshold | Result |
|---|---|---|---|
| Net margin | FY2025 32.8% ($651.9M/$1,990.869M); TTM ≈33% | >15% (strategy.md) / >12% (pre-screen) | ✅ PASS — clears by ~2x |
| ROIC | 59.6% (5yr avg, invested-capital basis) / 143.9% (ex-cash-goodwill-intangibles) — **flagged: conventional NI/Equity ROIC undefined due to negative GAAP equity (−$1.7B to −$1.8B)** | >15% | ✅ PASS (on invested-capital basis), with flag |
| Revenue CAGR 3yr | 12.94% (FY2022 $1.38B → FY2025 $1.991B) | >10% (strategy.md) / >8% (pre-screen) | ✅ PASS |
| Gross margin | FY2025 82% (FY2023 79% → FY2024 80% → FY2025 82%, TTM 82.86%) | >40% or structurally expanding | ✅ PASS — well above 40% and expanding |
| FCF positive 3 consecutive years | FY2022 $503M / FY2024 ≈$605.7M / FY2025 $739M — all positive and growing (FY2023 implied positive) | required | ✅ PASS |
| **Net debt/EBITDA** | **2.61×** (company-disclosed, Q2 FY2026: net debt $3.368B ÷ EBITDA ~$1.33B) | **<2× (strategy.md)** / <2.5× (pre-screen) / <4× (Upgrade 5, asset-light — **conditional on investment-grade rating**) | ❌ **FAIL** |
| FCF/NI conversion ratio 2yr | FY2024 ≈118.1% / FY2025 ≈113.3% — both far above 70% | >70% for 2+ consecutive years | ✅ PASS |
| Share issuance pattern | Sustained, large-scale **buyback** (3yr buyback ratio +4.00%; $1B → $1.5B → new $2B program as of 8 Jun 2026) | not dilutive | ✅ PASS |
| Moat signal | FICO Score is the de facto industry standard for US consumer credit risk (mortgage, auto, card underwriting) — deeply embedded in lender workflows, regulatory/GSE reliance (Fannie Mae/Freddie Mac mandate FICO scores), extremely high switching costs | required | ✅ present qualitatively |

### Why this is a FAIL, not a pass-with-flag

FICO's **Net Debt/EBITDA = 2.61×** is a **company-disclosed, directly-sourced figure** (from the Q2 FY2026 earnings call, where management explicitly frames it against a 3.5× *covenant* maximum — i.e., this is the company's own leverage metric, not an estimate). It:

- **Fails strategy.md's Phase 01 core threshold of <2×** (by 0.61×, ~31% over)
- **Fails the valuation-scoring.md pre-screen threshold of <2.5×** (by 0.11×)
- Would **pass** Upgrade 5's asset-light exception (<4×) — FICO is unambiguously an asset-light, scoring/software business and its debt is "financial" (senior notes funding buybacks/operations, not operating leases or working-capital debt)
- **But Upgrade 5's <4× threshold is explicitly conditional**: *"provided interest coverage >15× **and** investment grade rated."* FICO's Moody's Corporate Family Rating is **Ba2 — sub-investment grade ("junk")**. This condition is **not met**, so the <4× exception **does not apply** to FICO.

This is not a hairline/rounding-error miss like the TTD net-margin near-miss (14.56% vs 15%, a 0.44pp gap) — it is a **directly company-disclosed leverage ratio that exceeds both the core <2× and the pre-screen <2.5× thresholds**, and the one framework provision that could excuse a higher ratio for an asset-light business (Upgrade 5) explicitly requires investment-grade rating, which FICO's leverage profile (built up specifically to fund the buyback program that also causes its negative-equity condition) has caused it to *not* hold.

**Gate result: FAIL on Net Debt/EBITDA (2.61× vs <2× core / <2.5× pre-screen; Upgrade 5's <4× asset-light exception does not apply because FICO is rated Ba2, sub-investment-grade).** All other 8 criteria pass — several (net margin, gross margin, FCF/NI conversion, ROIC on an invested-capital basis, share issuance pattern, moat) by wide margins. This is FICO's **only** Phase 01 failure point, but per the operating brief it is sufficient to stop here: **do not proceed to the Rate Environment Gate or Phase 02 scoring.**

---

## 4. Rate Environment Gate — NOT RUN

Per the operating brief: "If it fails, STOP — report exactly why, do not proceed to scoring." Phase 01 failed on Net Debt/EBITDA (2.61× vs <2×/<2.5× thresholds, Upgrade 5 asset-light exception inapplicable due to sub-investment-grade Ba2 rating). The Rate Environment Gate (Earnings Yield Spread Test + Rate Regime Modifier) and full Phase 02 valuation score are **not computed**.

*(For the record, if scoring had proceeded: Forward PE 24.23× → EY = 1/24.23 = 4.13%; spread vs 4.49% 10Y = −0.36%, which is <+1.5% and would have triggered the Step 1 +5 yellow flag. Step 2 Rate Regime Modifier would also be +5 [10Y in 3.5–5% bracket]. Neither of these is evaluated further since Phase 01 already failed.)*

---

## 5. Phase 02 — Full Valuation Score — NOT RUN

Not applicable — Phase 01 failed. No FCF Yield, EV/EBIT, Forward PE, or PEG sub-scores are computed. (Raw inputs that *were* gathered — TTM EBIT $1,136.338M, EV ≈$31.33B, TTM FCF $750.59M, Forward PE 24.23×, 10yr PE range 28.73×–93.53× with avg 48.21×, PEG 0.87 — are captured in §2 for a focused follow-up if the Net Debt/EBITDA picture improves, per the precedent set by the TTD session.)

---

## 6. Qualitative Notes (for the record, despite Phase 01 FAIL)

1. **Why are margins high?** The FICO Score is the dominant, almost universally-adopted standard for US consumer credit risk scoring — mortgage origination in particular is heavily reliant on FICO scores due to GSE (Fannie Mae/Freddie Mac) requirements. This regulatory/institutional embedding gives FICO significant pricing power (FICO has repeatedly raised per-score royalty pricing in recent years, a major driver of the Scores segment's revenue acceleration — note Q2 FY2026 revenue +39% YoY, "mortgage scores drive surge").
2. **Moat assessment:** Extremely strong — a multi-decade embedded standard with high switching costs (lenders, GSEs, and regulatory frameworks are all built around the FICO score specifically), reinforced by network effects (more lenders use it → more valuable as a common benchmark → harder for alternatives like VantageScore to displace it).
3. **Capital allocation track record:** Aggressive, sustained share buybacks (3yr buyback ratio +4.00%, escalating from a $1B → $1.5B → $2B program in roughly the past year) funded partly by new debt issuance (a new $1.5B term loan, new $1B senior notes due 2034) — this is the direct cause of both the negative book equity and the 2.61× leverage that triggers this session's Phase 01 failure. Whether this is prudent (returning excess cash generated by a high-ROIC, asset-light moat business to shareholders) or aggressive (taking sub-investment-grade leverage to fund buybacks at a price near 52wk-range midpoint) is a genuine judgment call the framework's quantitative gate resolves conservatively — by failing it.
4. **Growth sources next 3–5 years:** Continued FICO Score pricing power in mortgage/auto/card origination (the primary driver of the recent +39% quarterly revenue growth), plus Software segment growth in fraud/decisioning platforms.
5. **Best bear case:** (a) Regulatory or GSE action to reduce reliance on a single proprietary score (e.g., mandated multi-score or VantageScore adoption) would directly threaten the core moat; (b) the aggressive buyback-funded leverage (2.61× and rising, sub-investment-grade rating) reduces balance-sheet flexibility if origination volumes (mortgage-cycle-sensitive) turn down sharply; (c) negative book equity, while not itself a solvency signal for a strongly cash-generative business, is a structural feature that will keep tripping conventional screens (including this one) until either equity is rebuilt or the framework's thresholds are revisited for this specific profile.
6. **Disruption vector check:** A federally-mandated shift away from single-score reliance (already discussed at a policy level for mortgage underwriting in prior years) is the most plausible 5-year disruption vector — it would not eliminate FICO's business but could meaningfully dilute its pricing power on the highest-margin segment (mortgage scores).

---

## 7. Recommendation

# **PASS — Phase 01 FAIL. Do not proceed to scoring. Watchlist entry created (not scored).**

FICO fails the Phase 01 quality gate on a **single, well-sourced, company-disclosed criterion**: Net Debt/EBITDA of **2.61×**, which exceeds both strategy.md's core **<2×** threshold and the valuation-scoring.md pre-screen's **<2.5×** threshold. The one provision that could excuse a higher ratio for an asset-light business like FICO — Upgrade 5's <4× exception — explicitly requires **investment-grade rating**, and FICO is rated **Ba2 (Moody's)**, sub-investment-grade. The exception therefore does not apply.

This is despite FICO being, on every other dimension, an exceptionally high-quality business: ~33% net margins, 82%+ and expanding gross margins, ~13–14% revenue CAGR (recently accelerating to +22.6% TTM / +39% in the latest quarter), FCF/NI conversion well above 100% for two straight years, an extremely strong and arguably strengthening moat (the FICO Score's embedded role in US mortgage underwriting), and a clean (non-dilutive) capital return program. The leverage and negative-equity profile are themselves *artifacts of that same capital return program* — FICO has chosen to lever up specifically to fund buybacks, which is precisely the kind of balance-sheet decision the Net Debt/EBITDA gate (and its investment-grade-only exception for asset-light businesses) is designed to catch.

**No Phase 02 score was computed.** No order setup was produced (gate failed before Phase 02). **No position should be opened.**

---

## 8. Next Review Trigger

**Date/event:** FICO's next earnings release (Q3 FY2026, expected ~late July 2026) — re-check Net Debt/EBITDA at that time. Watch specifically for:
- Whether the leverage ratio **declines toward <2.5×** (e.g., if EBITDA growth from the current revenue acceleration outpaces the new debt drawn for the Feb/Jun 2026 buyback programs) — if it crosses back under the pre-screen's 2.5× threshold, Phase 01 would need a fresh full pass before Phase 02 could run.
- Any **credit rating change** (Moody's Ba2 → investment grade, i.e. Baa3 or higher, would unlock the Upgrade 5 <4× asset-light exception even if leverage stays elevated).
- Any **>15% unexplained price move** from $1,179.19 (Rule 9).
- Any **guidance revision, M&A, or management change** (Rule 9).

**No position opened — nothing to log in `decisions/`.**

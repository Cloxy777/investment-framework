# New Position Evaluation — ELF (e.l.f. Beauty, Inc.)

**Task type:** NEW POSITION (first-time evaluation)
**Date:** 2026-08-06
**10Y US Treasury yield:** not fetched — the Quality Score gate fails before Phase 02/the Rate Environment Gate would ever be invoked (see below), so it isn't needed this session.
**Trigger:** Telegram Stock-Mention Scan (Routine 6), unattended run. FinnInvestChannel top post (post `FinnInvestChannel/3053`, ~06:30:41 UTC 2026-08-06): "Revenue: $479.4M (Est. $429M) +36% YoY / Adj. EPS: $1.75 (Est. $0.71) / ...raising FY2027 revenue growth guidance to 18–20% from 12–14% / Rhode тепер тягне весь бренд... тепер по суті це інвестиція в Rhode, а не ELF" — a claimed Rule 9 earnings + guidance-revision event for e.l.f. Beauty (ticker ELF). **None of this post's text is used as a financial input below** — it only identified that ELF had reported earnings; every figure below was independently fetched from ELF's own SEC filings. ELF has no prior watchlist entry and is **not a current holding** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md) and `watchlist/{in,not-in}-portfolio/`) → triggers a first-time `/new-position ELF` per [telegram-scan.md](../.claude/commands/telegram-scan.md) step 4's first bullet.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any other work.

| Source | Value | Detail |
|---|---|---|
| **IBKR live snapshot** (contract_id 248682005, NYSE — "ELF BEAUTY INC", confirmed via `search_contracts` against the exact-symbol match, excluding the ~25 unrelated `ELF*`-prefixed ETF/bond tickers the search also returned) | **$85.76** | last trade, 08:05:10 UTC 2026-08-06 |
| Day change | **−0.71% (−$0.61)** | ordinary intraday move — notably *not* a large positive reaction despite the "beat and raise" headline; see §3 for why (tariff-refund-driven beat, offset by a real earnings-quality concern) |
| 52-week range (IBKR `misc_statistics`) | low **$48.85** / high **$150.93** (open 52 wk ago: $109.61) | live price sits well off the 52-week high, above the 52-week low |

**Live price used throughout this session: $85.76.**

---

## 2. Data Source — ELF's own SEC filings (primary source, Rule 0-compliant)

`yfinance` remains structurally blocked in this environment (`curl_cffi.requests.exceptions.SSLError: Recv failure: Connection reset by peer` on `get_info()`; direct `query1/query2.finance.yahoo.com` calls return HTTP 429 — consistent with the pattern noted in prior sessions). All fundamental data below is sourced directly from e.l.f. Beauty's own SEC filings (CIK 0001600033):

- **Form 10-K, FY ended March 31, 2026** (filed 2026-05-21, accession `0001600033-26-000020`) — audited annual financials for FY2024/FY2025/FY2026, plus the XBRL `companyfacts` API for quarterly reconstruction.
- **Form 8-K filed 2026-08-05** (accession `0001600033-26-000036`), Exhibit 99.1 — "e.l.f. Beauty Announces First Quarter Fiscal 2027 Results" (three months ended June 30, 2026), containing the unaudited condensed statements of operations, balance sheet, cash flows, and non-GAAP reconciliation tables. This independently confirms the Telegram post's headline figures (Revenue $479.4M vs Est. $429–434M, Adj. EPS $1.75 vs Est. $0.71) — also cross-checked via WebSearch (CNBC, StockStory, StreetInsider coverage of the same release).
- **Form 8-K filed 2026-05-20** (accession `0001600033-26-000018`), Exhibit 99.1 — "e.l.f. Beauty Announces Fourth Quarter Fiscal 2026 Results" — used to isolate the discrete Q4 FY2026 quarter (Jan–Mar 2026) that a TTM window requires but that isn't separately disclosed as its own filing.
- **SEC EDGAR XBRL `companyfacts` API** (`data.sec.gov/api/xbrl/companyfacts/CIK0001600033.json`) — used to pull exact, audited/reviewed `Revenues`, `NetIncomeLoss`, `GrossProfit`, `OperatingIncomeLoss`, `IncomeTaxExpenseBenefit`, `InterestIncomeExpenseNonoperatingNet`, `DepreciationDepletionAndAmortization`, `NetCashProvidedByUsedInOperatingActivities`, and `PaymentsToAcquirePropertyPlantAndEquipment` values (annual and quarterly, discrete quarters derived by subtracting cumulative year-to-date XBRL facts where the filing itself only discloses cumulative figures).

**Fiscal year convention:** ELF's fiscal year ends March 31. "FY2026" = year ended 2026-03-31; "Q1 FY2027" = three months ended 2026-06-30 (the quarter the triggering Telegram post refers to).

---

## 3. TTM Reconstruction — why the "beat and raise" headline doesn't translate to a large stock reaction

**TTM window = Q2 FY2026 (Jul–Sep 2025) + Q3 FY2026 (Oct–Dec 2025) + Q4 FY2026 (Jan–Mar 2026) + Q1 FY2027 (Apr–Jun 2026).**

```
TTM Revenue = $343.936M + $489.505M + $449.292M + $479.373M = $1,762.106M

TTM Net Income (GAAP) = $2.996M + $39.376M + (−$49.365M) + $66.599M = $59.606M
TTM Net Margin = 59.606 / 1,762.106 = 3.38%

TTM Gross Profit = $238.858M + $347.495M + $326.453M + $398.840M = $1,311.646M
TTM Gross Margin = 1,311.646 / 1,762.106 = 74.44%

TTM Operating Income = $7.716M + (−$50.333M) + $102.441M... 
  [Q2 FY26 $7.716M + Q3 FY26 $67.540M + Q4 FY26 (derived: FY26 full-year $73.632M − 9mo $123.965M = −$50.333M) + Q1 FY27 $102.441M]
  = $127.364M

TTM EBITDA (Net Income + Interest + Tax + D&A, company's own reconciliation formula):
  Interest expense, net: $9.153M + $12.351M + $11.148M + $7.808M = $40.460M
  Income tax provision:  −$6.985M + $14.488M + (−$11.165M) + $27.703M = $24.041M
  D&A: $18.286M + $21.555M + $26.328M + $26.101M = $92.270M
  TTM EBITDA = 59.606 + 40.460 + 24.041 + 92.270 = $216.377M
  (Cross-check via Operating Income + D&A: 127.364 + 92.270 = $219.634M — 1.5% higher,
   the gap being "other income/expense, net," not tax-effected in that approach. Using the
   bottom-up $216.377M, consistent with ELF's own EBITDA definition.)

TTM OCF = $23.415M + $59.405M + $102.458M + $111.665M = $296.943M
TTM Capex = $6.849M + $6.620M + $1.885M + $1.431M = $16.785M
TTM FCF = 296.943 − 16.785 = $280.158M
TTM FCF/NI = 280.158 / 59.606 = 470% (clamped to 100.0 in the sub-score — see §4)

Invested Capital (June 30, 2026 balance sheet):
  Total debt (current $30.000M + long-term $801.996M) = $831.996M
  + Total stockholders' equity $1,168.890M
  − Cash and cash equivalents $344.241M
  = $1,656.645M

NOPAT = TTM Operating Income × (1 − 25% effective tax rate*) = 127.364 × 0.75 = $95.523M
TTM ROIC = 95.523 / 1,656.645 = 5.77%

Net Debt = Total debt $831.996M − Cash $344.241M = $487.755M
Net Debt/EBITDA = 487.755 / 216.377 = 2.25×
```

*\*Tax-rate note: the raw TTM effective rate (24.041/83.647 pretax = 28.7%) is distorted by Q4 FY26's unusual pretax-loss/tax-benefit mismatch. Used ELF's own guided "adjusted effective tax rate" of 25–26% (per both the Q4 FY26 and Q1 FY27 releases) as a cleaner NOPAT tax-effecting assumption instead — a documented, cited figure, not an invented one.*

**Why the headline beat didn't move the stock much — two large, mostly-offsetting GAAP distortions inside this TTM window:**

1. **Q4 FY2026 (Jan–Mar 2026) GAAP net loss of $49.4M**, driven primarily by a **$57.6M "change in fair value of contingent consideration"** expense tied to the rhode (Hailey Bieber's brand) acquisition earnout — this is a real GAAP operating expense recorded *because rhode's revenue is outperforming* the earnout thresholds in the merger agreement, i.e. it's a cost that increases precisely when the acquired business does well, not a sign of operational weakness. It is a **purchase-accounting mechanic**, not a one-time restructuring/litigation/impairment charge, and there is no assurance it won't recur in future quarters as rhode keeps outperforming — so it was **not normalized away** from the score inputs below (see robustness check).
2. **Q1 FY2027 (Apr–Jun 2026) gross margin was boosted ~1,050 bps by an IEEPA tariff refund** (~$50M cash refund + interest, from tariffs struck down by the Supreme Court) — a one-time item of the same *kind* the framework's glossary already documents for Nike's FY2026 IEEPA benefit, but again **not normalized away** here (see robustness check) since Phase 01 uses actual TTM figures per [quality-scoring.md](../framework/quality-scoring.md), which doesn't invoke fair-value-methodology.md's Rule 6 normalization step (that step only governs Phase 03+ fair-value work, never reached this session).

**Robustness check (not part of the formal score, included for transparency):** reversing *both* distortions — adding back the $57.649M pretax contingent-consideration charge (~$43.2M after-tax) to TTM Net Income, then subtracting the ~$50M pretax IEEPA tariff-refund benefit (~$37.5M after-tax) — nets to +$5.7M, moving TTM Net Margin from 3.38% to only ~3.71%. **The two distortions roughly offset each other in this TTM window regardless of whether they're normalized**, so the choice not to normalize doesn't materially affect the outcome below.

---

## 4. Phase 01 — Quality Score (Gate)

### Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | Applies to ELF? | Basis |
|---|---|---|
| FCF/NI <70% for 2+ consecutive years, no growth-capex carve-out | No | FY2025 FCF/NI = $115.320M/$112.089M = **102.9%**; FY2026 FCF/NI = $190.062M/$26.318M = **722%** (both far above 70%; TTM = 470%). |
| Net debt/EBITDA over threshold (2.5× standard — ELF is a branded CPG business, not eligible for the Upgrade 5 asset-light 4× override) | No — but close | **2.25×**, under the 2.5× standard threshold. Elevated vs. ELF's pre-acquisition history (funded debt rose from near-zero to ~$832M to finance the rhode/Naturium acquisitions) and worth monitoring — a modest further EBITDA dip or additional debt-funded M&A could push this over the line. |
| Not FCF-positive for 3+ consecutive years | No | FCF positive all three most recently completed fiscal years: FY2024 $62.495M, FY2025 $115.320M, FY2026 $190.062M (TTM $280.158M). |

**No hard disqualifier fires.**

### Weighted Quality Score

| Sub-score (weight) | Inputs | Calculation | Result |
|---|---|---|---|
| **Profitability** (25%) | TTM Net Margin 3.38%; TTM ROIC (NOPAT basis) 5.77% — full derivation in §3 | NetMargin_Component = clamp((3.38/30)×100) = 11.28. ROIC_Component = clamp((5.77/30)×100) = 19.23. Avg = 15.26. No FCF-cap (FCF-positive all 3 years) | **15.26** |
| **Margins** (15%) | TTM Gross Margin 74.44% (FY2024 70.7% → FY2025 71.2% → FY2026 70.7% — essentially flat annually; the TTM figure runs a bit hot on the Q1 FY27 tariff-refund benefit noted in §3) | clamp((74.44/80)×100) = 93.05. No expansion-bonus applicable (bonus only fires when GM is *below* 40% and trending up) | **93.05** |
| **Growth** (20%) | Revenue 3yr CAGR: FY2023 $578.844M → FY2026 $1,636.472M = **41.4%** (inorganic-assisted — includes the Naturium and rhode acquisitions, not pure organic growth). TAM/pricing-power evidence: company states "7th consecutive year of net sales **and market share growth**" (Q4 FY2026 release) across a 5-brand portfolio spanning multiple price tiers and channels (US + international, retail + e-commerce). Deceleration considered: FY2027 guidance (18–20%) is below FY2026 actual (25%), but this guide was just **raised** from a prior 12–14% range on the strength of Q1 — i.e. accelerating vs. plan, not a structural deceleration signal | Base = clamp((41.4/25)×100) = clamp(165.6) = 100.0. +10 (cited TAM/share evidence) — already capped | **100.00** |
| **Balance Sheet** (15%) | Net Debt $487.755M; TTM EBITDA $216.377M (§3); standard /4 denominator | Net Debt/EBITDA = 2.25×. clamp(100×(1−2.25/4)) = clamp(43.75) | **43.64** |
| **Moat** (15%) | See evidence table below — 3 of 5 signals cleared the cited-evidence bar | (3/5)×100 | **60.00** |
| **FCF Quality** (10%) | TTM FCF/NI = 470% (§3) | clamp(((4.70−0.40)/0.60)×100) = clamp(716.7) | **100.00** |

**Moat signal evidence:**

| Signal | Evidence | Verdict |
|---|---|---|
| Market share stable/growing | Company's own claim: "7th consecutive year of net sales and market share growth" (Q4 FY2026 earnings release, 2026-05-20) — a company-disclosed, multi-year, quantified-trend claim | **TRUE** |
| Brand premium | Mixed: the core e.l.f. brand is explicitly mass/value-positioned (not premium pricing evidence). However, the rhode brand (acquired 2025) commands genuine pricing power — premium price points vs. mass beauty, documented rapid outperformance against its own acquisition-earnout thresholds (the very reason the $57.6M contingent-consideration charge fired in §3) is itself third-party-verifiable evidence of real, above-plan demand/pricing strength for that brand within the portfolio | **TRUE** (portfolio-level, driven by one brand — flagged as narrower than a company-wide premium position) |
| Network effect | No documented two-sided-marketplace or user-growth-driven-value mechanism — this is a branded CPG manufacturer/retailer, not a platform | **FALSE** |
| Switching costs | No integration depth, contractual lock-in, or data-migration cost for a cosmetics buyer — none found or plausible for this business model | **FALSE** |
| Scale cost advantage | TTM gross margin of ~70-74% is far above typical mass-beauty-peer levels (commonly cited in the 40-50% range for legacy CPG cosmetics), a data point ELF itself and analyst coverage attribute to a lean, founder-era-built supply chain and low overhead structure relative to legacy competitors — cost-per-unit data showing a gap vs. larger/smaller peers, though sourced from the company's own disclosure rather than an independent third-party cost study | **TRUE** (flagged: company-sourced comparison, not an independent third-party cost-per-unit study — a weaker citation than the evidence bar ideally wants) |

**Sensitivity note:** even using a stricter reading that drops the two flagged/narrower signals (Brand premium, Scale cost advantage) to FALSE — Moat_Score = (1/5)×100 = 20.0 — the Quality Score would fall to ~57.3, still failing the gate by an even wider margin. The Moat judgment calls above do not change the pass/fail outcome either way.

```
Quality Score = 15.26×0.25 + 93.05×0.15 + 100.00×0.20 + 43.64×0.15 + 60.00×0.15 + 100.00×0.10
              = 3.815 + 13.958 + 20.00 + 6.546 + 9.00 + 10.00
              = 63.32  →  63.3 (rounded to nearest 0.1)
```

### Result: **Quality Score 63.3 — fails the 80.0+ gate** (by 16.7 points)

Per [quality-scoring.md](../framework/quality-scoring.md) and [new-position.md](../.claude/commands/new-position.md) step 2: below 80.0 → stop, don't proceed to valuation. Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work were computed** this session.

**Why a "36% revenue growth, beat-and-raise" headline still fails the gate:** the gate is a *quality* (not growth or momentum) screen. ELF's Growth (100.0, capped) and FCF Quality (100.0, capped) sub-scores are both maxed out — the business is genuinely growing fast and its cash conversion is currently excellent. What fails the gate is **Profitability (15.26)** — TTM GAAP Net Margin (3.38%) and ROIC (5.77%) are both weak in absolute terms, a direct consequence of the debt-and-earnout-funded rhode/Naturium acquisition strategy compressing near-term GAAP earnings even as it accelerates revenue — plus a **Balance Sheet score (43.64)** reflecting leverage (2.25× Net Debt/EBITDA) that, while still under the 2.5× hard-disqualifier threshold, has risen materially from ELF's pre-acquisition near-zero-debt profile. A cheap-looking valuation multiple (which this session never got far enough to compute) would not change this: the framework's explicit design is that quality gates *before* price is even considered.

---

## 5. Recommendation

**PASS — do not open a position, watchlist only.** No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, no order setup — none of that is meaningful for a name that fails the quality gate, and forcing it through would violate this framework's explicit non-negotiable ("if it's below 80.0... stop and report why").

---

## 6. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance. `portfolio/holdings.md` not touched.

---

## 7. Next Review Trigger

- **Routine re-screen:** not scheduled — per [watchlist/README.md](../watchlist/README.md), "Phase 01 FAIL / not scored" entries carry no numeric Phase 02 score and so don't go stale on a methodology-version bump.
- **Rule 9 fundamental triggers that would warrant the next full re-look:** (a) Q2 FY2027 earnings (expected ~early November 2026) or any further guidance revision; (b) the rhode-acquisition contingent-consideration liability being resolved/settled (earnout period ending) — would remove the main source of GAAP-earnings volatility and is worth a fresh Profitability read once it happens; (c) Net Debt/EBITDA crossing the 2.5× hard-disqualifier threshold (currently 2.25×, limited headroom) — would fail the gate outright regardless of the weighted score; (d) an independent (non-company-sourced) cost-per-unit or market-share data point that would firm up or invalidate the two flagged/narrower Moat signals; (e) a management change or further material M&A.
- Absent any of the above, future Telegram mentions of ELF should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## Glossary

| Term | Meaning |
|---|---|
| **8-K** | The "current report" a US public company must file with the SEC within days of a material event — most commonly used to furnish (via an attached exhibit, typically "Exhibit 99.1") a quarterly earnings press release ahead of the fuller, audited 10-Q/10-K that follows weeks later. |
| **10-K (Annual Report)** | The annual financial-disclosure report a US public company must file with the SEC, containing full audited financial statements, MD&A, and risk factors. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **Contingent consideration (earn-out payment)** | A deferred, performance-contingent payment obligation from an acquirer to a seller, tied to the acquired business hitting agreed future milestones. ELF's rhode-acquisition earnout required a $57.6M fair-value markup in FY2026 — a real GAAP expense that increases precisely *because* rhode is outperforming, not a sign of weakness (see glossary's existing Coca-Cola/fairlife entry for the same mechanic). |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook companies use for their official financial statements. |
| **Hard disqualifier** | One of three Quality Score conditions (FCF/NI conversion, Net Debt/EBITDA, FCF positivity) that fails a company regardless of its weighted Quality Score. None fire for ELF, though Net Debt/EBITDA (2.25×) has limited headroom to its 2.5× threshold. |
| **IEEPA (International Emergency Economic Powers Act)** | A US law letting the President impose emergency economic tariffs/sanctions during a declared national emergency. ELF's Q1 FY2027 gross margin included a ~1,050bps one-time benefit from a refund of tariffs paid under a since-struck-down IEEPA order — the same mechanic already documented in this glossary for Nike's FY2026 results. |
| **Invested Capital** | The total capital (debt + equity, netted for cash) deployed in a business — the denominator of ROIC. |
| **Moat** | Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio. ELF is at 2.25× (up from near-zero pre-acquisition), driven by rhode/Naturium acquisition debt. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **Quality Score** | A 0–100.0 grade (0 = lowest quality, 100 = highest) blending profitability, margins, growth, balance sheet, moat, and FCF quality into one number; a company must score ≥80.0 to be eligible for Phase 02 valuation scoring at all. ELF scores 63.3. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **TAM** | Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results — this session's primary basis (Q2 FY2026 through Q1 FY2027). |

# NEW POSITION — ADSK (Autodesk, Inc.)

**Task type:** NEW POSITION
**Date:** 2026-08-23
**10Y US Treasury Yield:** 4.74% (TradingEconomics, "rose to 4.74% on Friday" 2026-08-21 close — same most-recent-available print used in this repo's same-day INTU session; markets closed over the weekend, no newer print exists).

**Trigger:** Automated Telegram-scan (Routine 6) flagged a first-time mention of Autodesk — the channel author's own earnings-week watchlist commentary naming ADSK among "SaaS names recovering from this year's downturn, expecting continued growth." **Checked both `watchlist/in-portfolio/ADSK/` and `watchlist/not-in-portfolio/ADSK/` directly (`ls` on both paths, plus a case-insensitive repo-wide `find -iname "*adsk*"`) before doing anything else** — neither exists; no prior ADSK entry anywhere in the repo. Per `telegram-scan.md` step 4's first bullet, this is a mandatory first-ever `/new-position` evaluation regardless of the triggering post's substance. **The Telegram post is used only as the trigger — it is not a financial data input.** Every figure below was independently fetched from IBKR, stockanalysis.com, SEC-adjacent sources, and general web search, cited individually. (Note: the post's "recovering from this year's downturn" framing is, as it happens, independently corroborated below by IBKR's own price-history stats — not taken on faith.)

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

- `search_contracts("ADSK")` → contract_id **265681**, NASDAQ, "AUTODESK INC", US primary listing (a Mexican secondary listing (MEXI) and an unrelated Autodesk corporate bond entry excluded).
- `get_price_snapshot(265681)`:

| Field | Value |
|---|---|
| **Last trade price** | **$253.82** |
| Prior close | $251.02 |
| Change | +$2.80 (+1.12%) |
| 52-week high / low | $329.09 / $185.50 |
| 13-week high / low | $260.74 / $185.50 |
| 26-week high | $264.75 |
| Dividend yield | 0.0% (Autodesk pays no dividend) |

**Live Price used throughout this session: $253.82.** Not inferred from any multiple — fetched directly. Note the 13-week low equals the 52-week low ($185.50) — the trough was recent (within the last quarter) — while today's price is meaningfully above both the 13-week high ($260.74 — nearly reached) and far above the 52-week low, consistent with a real, ongoing recovery off a 2026 trough (today's price is ~22.9% below the 52-week high and ~36.8% above the 52-week low).

---

## 2. Why the stock is down — required context before scoring moat/quality

**52-week high to low is a ~43.6% drawdown.** Web search findings (cited):

- **April 2024 accounting investigation:** Autodesk delayed its 10-K and launched an internal probe into how it accounted for multi-year enterprise subscription deals and calculated free cash flow — management had used upfront-billed multi-year contracts to pull forward revenue and hit short-term non-GAAP FCF targets in fiscal 2023. Resolution (May 2024): no restatement needed, but the CFO was replaced. [[Boardroom Alpha](https://www.boardroomalpha.com/starboard-challenges-autodesk-proxy-fight-looms-over-governance-performance/)]
- **Starboard Value activist campaign:** built a ~$500M stake following the investigation, launched proxy fights in 2024 and 2025, and has publicly pushed the board to evaluate CEO Andrew Anagnost's position and to target 45% operating margins by FY2028 via cost cuts. [[CNBC](https://www.cnbc.com/2024/08/06/starboard-pushes-autodesk-board-to-weigh-ceo-change-cost-cuts.html)] [[Bloomberg](https://www.bloomberg.com/news/articles/2024-08-22/starboard-urges-autodesk-to-hold-ceo-accountable-after-probe)]
- **Anagnost remains CEO as of 2026** — no management change occurred (checked explicitly; this is not a live Rule 9 management-change trigger). [[Wikipedia — Andrew Anagnost](https://en.wikipedia.org/wiki/Andrew_Anagnost)]
- **January 2026 restructuring:** ~7% workforce reduction (~1,000 roles, concentrated in go-to-market/sales), pre-tax charges $135–160M, explicitly to redirect resources toward AI platforms and industry-cloud development — plausibly a response to sustained Starboard cost-discipline pressure. [[Investing.com](https://www.investing.com/news/sec-filings/autodesk-announces-global-restructuring-with-7-workforce-reduction-93CH-4460545)]
- **Pricing-model transition:** a multi-year "Transition to Named User" (TNU) licensing shift plus 5–9% annual list-price increases (2020–2025 in the 5–7% range; January 2026's 6–9% increase is the largest yet), alongside removal of most renewal discounts — documented customer frustration (a 20%-increase complaint cited by one 25-year customer) but **no evidence of a resulting volume/growth hit**: revenue growth *accelerated* through the same window (FY2024 9.83% → FY2025 11.53% → FY2026 17.53% → TTM 18.28%). [[Graitec](https://graitec.com/us/tech-resources/upcoming-autodesk-price-renewal-changes-take-action-now/)] [[AutodeskAudits](https://autodesksaudits.com/blog/autodesk-subscription-pricing-2026/)]
- **Margin recovery underway:** non-GAAP operating margin rose to 38% in FY2026 (+200bps YoY), with FY2027 guidance of 38.5–39% and a longer-term FY2029 target of 41% (~45% "underlying"). [[Finsee](https://finsee.ai/earnings/adsk/2026/q4/en/)]

**Bottom line:** the ~2024 drawdown driver (accounting investigation + activist pressure + CEO-accountability overhang) is largely resolved/priced-in history, not a live Rule 9 event — but it left the stock trading at a much-compressed multiple relative to its 2021–2023 valuation regime, which matters directly for the Forward-PE sub-score below (§5.3) and is carried through explicitly into the DCF bear case (§5.4) and the disruption-vector check (§7).

**Next earnings: Q2 FY2027, August 27, 2026 — 4 days from today.** A mandatory Rule 9 re-valuation trigger, flagged prominently in §8.

---

## 3. Phase 01 Quality Score

Per [quality-scoring.md](../framework/quality-scoring.md) (methodology version 2026-06-29). **Autodesk's fiscal year runs 1 Feb – 31 Jan**; FY2026 (ended 31 Jan 2026) is the latest complete audited fiscal year, and TTM (through the fiscal quarter ended 30 April 2026) is used for the TTM-specified inputs. All figures from stockanalysis.com (financials/balance-sheet/cash-flow/ratios/statistics pages, WebFetch, 2026-08-23), cross-checked internally where flagged.

### Raw financial data (FY2022–FY2026 + TTM)

| Metric | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | TTM (Apr '26) |
|---|---|---|---|---|---|---|
| Revenue | $4,386M | $5,005M | $5,497M | $6,131M | $7,206M | $7,507M |
| Revenue growth | 15.73% | 14.11% | 9.83% | 11.53% | 17.53% | 18.28% |
| Gross Profit / Margin | $4,021M / 91.68% | $4,583M / 91.57% | $5,034M / 91.58% | $5,638M / 91.96% | $6,653M / 92.33% | $6,939M / 92.43% |
| Operating Income (EBIT) | $748M | $1,032M | $1,175M | $1,415M | $1,808M | $2,040M |
| Net Income / Margin | $497M / 11.33% | $823M / 16.44% | $906M / 16.48% | $1,112M / 18.14% | $1,124M / 15.60% | $1,463M / 19.49% |
| Diluted EPS | $2.24 | $3.78 | $4.19 | $5.12 | $5.23 | $6.85 |
| EPS growth YoY | −58.82% | +68.75% | +10.85% | +22.20% | +2.15% | +46.85% |
| Operating Cash Flow | $1,531M | $2,071M | $1,313M | $1,607M | $2,452M | $2,781M |
| CapEx | −$56M | −$40M | −$31M | −$40M | −$43M | −$52M |
| Free Cash Flow | $1,475M | $2,031M | $1,282M | $1,567M | $2,409M | $2,729M |
| FCF margin | 33.63% | 40.58% | 23.32% | 25.56% | 33.43% | 36.35% |
| FCF/NI conversion | 296.8% | 246.8% | 141.5% | 140.9% | 214.4% | 186.5% |

**Balance sheet (most recent quarter, Apr 30 2026, stockanalysis.com):** Cash & Equivalents $2,671M, Short-Term Investments $253M (Cash & ST Investments $2,924M), Total Debt $2,724M, Long-Term Debt $2,484M, **Net Cash (site-stated): $585M**, Shareholders' Equity $3,189M, Total Assets $11,932M, Shares Outstanding 211.15M.

**Cross-check on Net Cash (flagged, not silently trusted):** a naive Cash&STInvestments − TotalDebt = $2,924M − $2,724M = $200M, not the site's stated $585M. Reconciled independently via the statistics page's own Market Cap / EV: Market Cap $53.59B, EV $53.01B → implied Net Debt = EV − MktCap = −$0.58B (net cash ~$580M) — matches the balance-sheet page's own $585M line closely (small rounding/date differences), so **$585M is used** (cross-validated from two independently-sourced page, not invented). The site's own "Total Debt" figure likely nets differently against operating-lease liabilities than the net-cash line does; not something we can fully reconstruct from public labels, but the two pages agree with each other, so the risk of an invented number is low.

**Statistics (stockanalysis.com):** ROE 50.40%, ROIC 49.15%, ROA 11.32%, EV/EBITDA 24.78×, EV/EBIT 25.98×, Debt/Equity 0.85, Current Ratio 0.83, Trailing PE 37.08×, Forward PE 19.72×, vendor-computed PEG 0.98 (informational only — see §5.1, does not qualify under this framework's Fast-Grower test).

**Second cross-check (Net Debt/EBITDA mislabeling, same pattern as the 2026-08-23 INTU session):** Market Cap(live) = 211.15M × $253.82 = **$53,594.1M**. EV(live) = 53,594.1 − 585 = **$53,009.1M**. EBIT(TTM) = $2,040M → EV/EBIT = 53,009.1/2,040 = **25.99×** (matches the vendor's stated 25.98×). EBITDA implied by EV/EBITDA 24.78× = 53,009.1/24.78 = **$2,139.6M** → **true Net Debt/EBITDA = −585/2,139.6 = −0.2734×** (net cash). The statistics page's own "Net Debt/EBITDA: 1.24" figure instead reconciles with **gross** Debt/EBITDA (2,724/2,139.6 = 1.273×, ≈1.24 within rounding) — mislabeled, same as INTU's reconciliation. **−0.27× (net cash) is used below.**

**Hard disqualifier check (quality-scoring.md):**
- FCF/NI conversion <70% for 2+ consecutive years: **No** — every year FY2022–TTM is 140.9%–296.8%, far above 70%.
- Net Debt/EBITDA over threshold (2.5× standard): **No** — −0.27×, a net-cash position.
- Not FCF-positive for 3+ consecutive years: **No** — FCF positive and growing (with a dip in FY2024) every year shown.

**No hard disqualifier fires.**

### 3a. Profitability (25% weight)

```
NetMargin_Component = clamp((19.49/30)×100, 0, 100) = 64.97   (TTM net margin)
ROIC_Component       = clamp((49.15/30)×100, 0, 100) = clamp(163.83, 0, 100) = 100.0
Profitability_Score  = (64.97 + 100.0) / 2 = 82.48   (no FCF cap — FCF-positive every year shown)
```

*Flag: ROIC 49.15% is elevated largely because invested capital is structurally small — Autodesk has bought back stock aggressively enough that equity sits at only $3,189M against a $53.6B market cap. This is a real, sourced (stockanalysis.com statistics page) figure, not invented, but shown transparently since it's doing a lot of work in this sub-score.*

### 3b. Margins (15% weight)

```
GrossMargin_Score = clamp((92.43/80)×100, 0, 100) = clamp(115.5, 0, 100) = 100.0   (clamped)
```
Gross margin has drifted marginally *up* (91.68% FY2022 → 92.43% TTM) but this is moot — the score is already clamped at its 100.0 ceiling regardless of trend.

### 3c. Growth (20% weight)

```
Revenue 3yr CAGR (FY2023 $5,005M → FY2026 $7,206M) = (7,206/5,005)^(1/3) − 1 = 12.90%
Growth_Score (base) = clamp((12.90/25)×100, 0, 100) = 51.60
```

**TAM/pricing-power modifier — evidence and judgment shown in full:**
- *For a +10 modifier:* Autodesk is monetizing project-workflow automation via its "Autodesk Assistant" agentic-AI layer, explicitly framed by management as expanding TAM by monetizing more project activity through consumption as fewer people are needed per project; cross-selling into industry-cloud suites (Forma/construction, manufacturing collections) is management's stated growth driver, and — unlike a mere claim — this is corroborated by an actual, measured **acceleration** in consolidated revenue growth through the same period (9.83% → 11.53% → 17.53% → 18.28% TTM), concurrent with (not despite) the 2025–2026 price increases (§2). [[MatrixBCG](https://matrixbcg.com/blogs/growth-strategy/autodesk)]
- *Against a −10 penalty (structural deceleration):* **Does not apply** — growth has been accelerating, not decelerating, and FY2027 revenue guidance was raised mid-year (to $8.155–8.215B) following a Q1 FY2027 beat. No segment-level evidence of structural deceleration was found (contrast with INTU's TurboTax case, where a specific segment *was* found to be decelerating).
- **+10 modifier applied.**

```
Growth_Score = 51.60 + 10 = 61.60
```
*(Sensitivity: without the modifier, Growth_Score = 51.60 and Quality Score would be 82.9 instead of 84.9 — still clears the gate either way; see §3h.)*

### 3d. Balance Sheet (15% weight)

```
BalanceSheet_Score = clamp(100 × (1 − (−0.2734)/4), 0, 100) = clamp(106.8, 0, 100) = 100.0   (clamped)
```
No asset-light override needed — ADSK is already net-cash, far under even the standard 2.5× threshold.

### 3e. Moat Signal (15% weight)

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | AutoCAD holds ~38.65% share of the CAD-software category (vs. next-largest, SolidWorks, ~13.59%); Revit holds ~39.91% share of the BIM/architectural-design-software category — both category leaders, per third-party tracking. Regionally even more dominant: ~66% combined CAD share and ~45% BIM share among European architects, with Autodesk + Graphisoft covering 80–90% of the European AEC market. [[6sense](https://6sense.com/tech/cad-software/autodesk-revit-market-share)] [[USP Research](https://www.usp-research.com/insights/news/market-overview-of-bim-and-cad-software-usage-of-european-architects/)] |
| Brand premium | **TRUE** | Documented price increases *without* volume loss: 5–9% annual renewal/list-price increases every year 2020–2026 (2026's 6–9% is the largest), including a "Transition to Named User" (TNU) licensing shift, absorbed by customers while consolidated revenue growth *accelerated* over the identical window (11.53%→17.53%→18.28% TTM) — a direct match to the signal's definition of pricing power without customer attrition. [[AutodeskAudits](https://autodesksaudits.com/blog/autodesk-subscription-pricing-2026/)] [[Graitec](https://graitec.com/us/tech-resources/upcoming-autodesk-price-renewal-changes-take-action-now/)] |
| Network effect | **TRUE** | Autodesk Construction Cloud (now "Forma")'s Builders Network + BuildingConnected connects owners, GCs, subcontractors, and designers on a shared platform — BuildingConnected alone is used by "nearly one million subcontractors" — a documented multi-sided-network mechanism (more participants on each side → more valuable matching/collaboration for everyone → more participants). [[Autodesk / Digital Builder](https://www.autodesk.com/blogs/construction/autodesk-construction-cloud-industry-footprint/)] |
| Switching costs | **TRUE** | Named-User licensing plus multi-year enterprise commitments create real lock-in: documented enterprise buyers face "multi-year commitment premiums of 8–18%" and absorb double-digit fee increases (one 25-year customer cited a 20% hike) rather than migrating off the platform — a workflow/data-lock-in mechanism (designs, BIM models, and trained staff are all built around AutoCAD/Revit file formats and workflows). [[AutodeskAudits](https://autodesksaudits.com/blog/autodesk-named-user-licensing-explained/)] |
| Scale cost advantage | **FALSE** | No cost-per-unit data found comparing Autodesk's per-seat/per-customer cost structure against smaller CAD competitors. The margin-expansion narrative (FY2026 non-GAAP op margin +200bps, FY2027 guided 38.5–39%) is about internal cost discipline/go-to-market restructuring, not a documented unit-cost gap vs. rivals — not marked true without a citation, per quality-scoring.md's rule. |

```
Moat_Score = (4/5) × 100 = 80.0
```

Unlike the same-day INTU session, no single Moat signal here rests on genuinely conflicting internal evidence (INTU's "Brand premium" call had to weigh QBO's pricing power against TurboTax's simultaneous guidance cut) — the price-increase-without-volume-loss pattern here holds at the consolidated level with no comparable internal contradiction found. Still shown at full transparency in §3h below.

### 3f. FCF Quality (10% weight)

```
FCF/NI (TTM) = $2,729M / $1,463M = 186.5%
FCFQuality_Score = clamp(((1.865 − 0.40)/0.60)×100, 0, 100) = clamp(244.2, 0, 100) = 100.0   (capped)
```

### 3g. Full Quality Score — primary computation

```
Quality Score = (82.48×0.25) + (100.0×0.15) + (61.60×0.20) + (100.0×0.15) + (80.0×0.15) + (100.0×0.10)
              = 20.621 + 15.000 + 12.320 + 15.000 + 12.000 + 10.000
              = 84.941
              → rounds to 84.9
```

### 3h. Sensitivity table — how robust is the 80.0+ pass?

| Scenario | Moat_Score | Growth TAM modifier | Quality Score | Gate result |
|---|---|---|---|---|
| **Primary (as scored above)** | 80.0 (4/5) | +10 | **84.9** | **PASS** (+4.9) |
| Conservative Moat (any one signal → FALSE, 3/5) | 60.0 | +10 | **81.9** | PASS (+1.9) |
| Conservative Growth (no TAM bonus) | 80.0 (4/5) | 0 | **82.9** | PASS (+2.9) |
| Both conservative | 60.0 | 0 | **79.9** | **FAIL** (−0.1) |

**Reading:** the primary pass has a comfortable 4.9-point cushion, and either single conservative adjustment on its own still clears the gate. Only the joint "both conservative" combination — dropping a Moat signal *and* removing the Growth TAM bonus at the same time — tips it to a narrow 79.9 fail. This is meaningfully more robust than the same-day INTU session's 82.8-vs-79.8 razor's-edge pass, but is shown in full per the task's sensitivity-table instruction rather than presenting 84.9 as beyond question.

### Gate Result: ✅ **PASS** (84.9 ≥ 80.0) — proceeding to Phase 02.

---

## 4. Rate Environment Gate

Per [strategy.md](../framework/strategy.md) / [valuation-scoring.md](../framework/valuation-scoring.md).

**Step 1 — Earnings Yield Spread Test:**
```
Forward PE = 19.72× (stockanalysis.com's own "Forward PE" statistic; cross-checked against FY2027 non-GAAP
             EPS guidance midpoint $12.525 ($12.40–12.65 range) at live price: $253.82/$12.525 = 20.27× —
             both land in the same ~19.7–20.3× range)
EY = 1 / 19.72 = 5.071%
Spread = EY − 10Y = 5.071% − 4.74% = 0.331%
```
Spread < +1.5% → **fails Step 1 → +5 additive flag** (per operating-brief.md's 2026-06-07 rule — a yellow flag that raises the bar, not a veto).

**Step 2 — Rate Regime Modifier:** 10Y = 4.74% falls in the 3.5–5% bracket → **+5**.

**Combined Rate Modifier = +10** (unlike the same-day INTU session, where Step 1 passed — ADSK's much lower earnings yield at a 19.72× forward multiple, vs. INTU's 13.73×, is what tips Step 1 to a fail here).

---

## 5. Phase 02 — Valuation Score

### 5.1 PEG eligibility (Fast Grower check)

GAAP diluted EPS growth over the last 3 consecutive complete fiscal years: FY2024 +10.85%, FY2025 +22.20%, FY2026 +2.15%. **Only one of three years exceeds 15%** — this clearly fails the "EPS growth >15% for 3+ years" Fast-Grower eligibility test (no ambiguity about "clean earnings base" needed here, unlike INTU's case — the test fails outright on the raw growth-rate numbers). **PEG does NOT apply — redistribute its 15% weight to EV/EBIT (EV/EBIT weight becomes 40%).**

*(The vendor-stated PEG of 0.98 on the statistics page is a market-data-provider computation using its own growth-rate assumption, shown above for reference only — it is not used in this framework's score, since ADSK does not clear the Fast-Grower eligibility bar under this framework's own test.)*

### 5.2 Sub-score inputs

```
FCF Yield = FCF(TTM) / Market Cap(live) = $2,729M / $53,594.1M = 5.0925%
EV/EBIT (live) = $53,009.1M / $2,040M = 25.985×
Forward PE = 19.72× (see §4)
5yr PE (fiscal-year-end snapshots, stockanalysis.com "financials/ratios" page):
  FY2022 110.56× | FY2023 56.41× | FY2024 59.93× | FY2025 60.15× | FY2026 47.60×
  → Avg = 66.93×, Low = 47.60×, High = 110.56×
```

**Caveat on the 5yr PE range (same as the same-day INTU session):** these are five annual (fiscal-year-end) snapshots, not a true intra-year low/high range reconstructed from quarterly TTM EPS (yfinance has been broken with SSL errors since 2026-07-07, per repo precedent — that method is unusable). Treated as the **Fallback (average-only) formula**.

### 5.3 Sub-scores

```
FCF_Score      = clamp(100×(1 − 5.0925/10), 0, 100) = 49.08
EV/EBIT_Score  = clamp((25.985 − 12)/23×100, 0, 100) = 60.80
FwdPE_Score    = Deviation% = (19.72 − 66.93)/66.93×100 = −70.55%
               = clamp(50 + (−70.55×2.5), 0, 100) = clamp(50 − 176.4, 0, 100) = 0.0
               (fallback formula — already folds in the Historical PE Modifier, no separate ±10 applied)

Raw weighted = (49.08×0.40) + (60.80×0.40) + (0.0×0.20)      [PEG N/A → EV/EBIT carries 40%]
             = 19.632 + 24.320 + 0.000
             = 43.952
```

**Note on the FwdPE_Score = 0.0 extreme:** a −70.6% deviation from the 5yr average PE reflects that ADSK traded at a 48–111× GAAP-earnings multiple through FY2022–2026 (a rich, pre-accounting-investigation/ZIRP-era SaaS multiple regime) and now trades at ~19.7× forward earnings after both the 2024 accounting-investigation de-rating (§2) and real subsequent earnings growth. As with the same-day INTU session's structurally-similar finding, this is as much a statement about a sector/company-specific multiple *regime change* as about fresh mispricing — shown transparently, per Rule 4's "multiple sanity" discipline, rather than hidden or overridden.

### 5.4 Fair Value (Rule 7 — scenario analysis, bull/base/bear)

**Method A — 3-stage DCF** (Rule 2: unlevered FCF; WACC = Rf + β×ERP; terminal growth ≤3% per the GDP cap). Beta sourced at 1.30 (Yahoo Finance 5Y monthly; other sources ranged 1.21–1.45 — Investing.com 1.45, GuruFocus 1.21 — 1.30 used as a documented mid-estimate). Base-case Year-1 growth/margin anchored to Autodesk's own FY2027 guidance (revenue $8.155–8.215B, FCF $2.725–2.8B) — used here as DCF *modeling input*, not as a scored valuation sub-score, consistent with "Why Forward Guidance Is Not a Sub-score":

| | Bull (WACC 10.24%, terminal g 3.0%) | Base (WACC 11.24%, terminal g 2.5%) | Bear (WACC 12.24%, terminal g 2.0%) |
|---|---|---|---|
| Rev growth Y1→Y5 | 15%→11% | 13.58%(guidance)→10% | 10%→6% |
| FCF margin Y1→Y5 | 35%→43% | 33.76%(guidance)→40% | 32%→29% |
| Y5 Revenue | $13,271.4M | $12,479.1M | $10,583.5M |
| Y5 FCF | $5,706.7M | $4,991.6M | $3,069.2M |
| Terminal Value | $81,190.6M | $58,547.6M | $30,572.3M |
| PV(FCFs) + PV(TV) | $15,436.4M + $49,850.9M | $13,667.1M + $34,377.3M | $10,111.1M + $17,164.9M |
| Enterprise Value | $65,287.3M | $48,044.4M | $27,276.0M |
| Equity Value (+ net cash $585M) | $65,872.3M | $48,629.4M | $27,861.0M |
| **DCF FV/share** (÷211.15M shares) | **$311.98** | **$230.31** | **$131.95** |

*Sanity checks (Rule 4):* Bull terminal FCF multiple = TV/Y5 FCF = 81,190.6/5,706.7 = **14.2×** — not an absurd exit multiple. **Bear-case FV ($131.95) sits below the actual 52-week low ($185.50)** — flagged explicitly, not hidden: this reflects a scenario where the AI-disruption-to-design-software risk (§7) becomes realized rather than merely feared, which is worse than anything the market has actually priced in the last year — a legitimate bear scenario, not a modeling error, but worth carrying forward as a real tail-risk flag.

**Method B — Peer comparable multiples** (Rule 5: 6 peers, median not mean, all forward PE, live/recent): PTC 15.42×, Bentley Systems (BSY) 30.69×, Cadence Design Systems (CDNS) 44.68×, Synopsys (SNPS) 36.31×, Trimble (TRMB) 14.98×, Procore (PCOR) 35.71× → sorted 14.98/15.42/30.69/35.71/36.31/44.68 → **median (n=6) = (30.69+35.71)/2 = 33.20×**.

```
Base:  FY2027 non-GAAP EPS guidance midpoint $12.525 × peer median 33.20×                    = $415.83
Bull:  $12.525 × highest-quality EDA-duopoly peer multiple (CDNS 44.68×)                       = $559.62
Bear:  $12.525 × lowest peer multiple (TRMB 14.98× — a "market re-rates ADSK to a legacy
       hardware-adjacent-software multiple despite unchanged EPS" scenario)                     = $187.62
```
*(The historical-PE cross-check in Rule 3's "W4" — Current EPS × 5yr avg PE = $6.85(TTM GAAP)×66.93 = $458.47 — is deliberately **excluded** from this blend: it fails Rule 4's multiple-sanity check outright, for the same structural-multiple-regime-change reason flagged in §5.3. Shown, not hidden, then discarded — same treatment as the same-day INTU session.)*

**Blended FV per scenario** (Fair Value = 40% DCF + 60% Multiples, per fair-value-methodology.md Step 1):

```
Bull:  0.40×311.98 + 0.60×559.62 = 124.79 + 335.77 = $460.56
Base:  0.40×230.31 + 0.60×415.83 =  92.12 + 249.50 = $341.62
Bear:  0.40×131.95 + 0.60×187.62 =  52.78 + 112.57 = $165.35

PW Blended Fair Value = 0.25×460.56 + 0.50×341.62 + 0.25×165.35 = 115.14 + 170.81 + 41.34 = $327.29
```

**Base-Case Blended Fair Value (for order setup) = $341.62. PW Blended Fair Value (for the modifier below) = $327.29.**

*(Rule 0 Step 4 sanity check: Wall Street consensus 12-month price targets cluster in the $300–360 range across multiple sources — WallStreetZen $314.94, a 34-analyst average of $312.75, a $356.55 consensus, and a $359.13 25-analyst average. Our independently-derived Base Blended FV of $341.62 sits squarely inside this external range — a good cross-check that the number isn't an outlier.)*

### 5.5 Upside/Downside Modifier

```
Gap Upside % = (PW FV / Live Price) − 1 = (327.29 / 253.82) − 1 = +28.95%

Catalyst & timeline (Rule 10): the next 2–3 quarterly earnings prints — the imminent Aug 27 2026 Q2 FY2027
  report (4 days away), Q3 FY2027 (~Nov 2026), and the FY2027 close + initial FY2028 guidance (~Feb 2027) —
  the window in which the recent reacceleration (17.53%→18.28% TTM revenue growth) either sustains into
  FY2028 guidance or fades back toward a more "steady-state" pace, and in which any AI-disruption-to-CAD
  risk analogous to what hit INTU's TurboTax segment would first show up in reported numbers, if real.
  Catalyst window = 18 months (within Rule 10's 18–24mo band).
Annualized gap = 28.95% / 1.5yr = 19.30%/yr

Intrinsic growth rate = 12%/yr (FY2028 consensus non-GAAP EPS growth, $9.64→$10.82 — chosen deliberately
  over the distorted 39.55% FY2027 estimate, which reflects a one-off base effect from FY2026 EPS being
  suppressed by the multi-year-contract-accounting transition, §2)
Shareholder yield = dividend yield 0% (no dividend) + net buyback yield 1.27% (stockanalysis.com
  statistics page) = 1.27%

E = 19.30% + 12.00% + 1.27% = 32.57%/yr
```

`E` ≥ H(10%) → strong-upside band:
```
M = −15 × clamp((E−10)/15, 0, 1) = −15 × clamp(22.57/15, 0, 1) = −15 × clamp(1.505, 0, 1) = −15 × 1.0 = −15.0
```

**Guardrail/sanity flag (shown, not hidden):** E = 32.6%/yr comfortably exceeds the +25%/yr level that already fully saturates the modifier at its ±15 cap — same pattern as the same-day INTU session. It's the arithmetic sum of three separately-defensible inputs (a re-rating gap annualized over a relatively short 1.5yr window, a double-digit intrinsic growth rate, and a real buyback yield), each individually reasonable but compounding into a number well past the point where the exact figure matters — the ±15 clamp does its job here regardless.

**Upside/Downside Modifier = −15.0** (maximum attractive).

### 5.6 Final Valuation Score

```
Final Score = 43.952 (raw weighted, §5.3) + 10 (Rate Modifier, §4) + (−15.0) (Upside/Downside Modifier, §5.5)
            = 38.952 → rounds to 39.0
```

**Valuation Score = 39.0** — within the 30.0–49.9 "Cheap, standard position" band.

---

## 6. Composite Score

```
Composite Score = 0.50×(100 − Quality Score) + 0.50×Valuation Score
                = 0.50×(100 − 84.9) + 0.50×39.0
                = 0.50×15.1 + 0.50×39.0
                = 7.55 + 19.50
                = 27.05 → exactly on a ".X5" boundary → rounds UP (more conservative) → 27.1
```

**Composite Score = 27.1** → per the Composite/Phase 03 Action Table: **Score 0.0–29.9 → BUY — Full position 6–8%** *(nominal reading — see §7 for why the mechanical R/R gate changes the actual order-setup recommendation).*

*(Sensitivity carried from §3h: even in the "both conservative" Moat/Growth reading, Quality Score would be 79.9 — a narrow gate fail that would mean this entire section doesn't exist. The primary reading here has a real 4.9-point cushion, materially more robust than the same-day INTU session's 82.8-vs-79.8 case.)*

---

## 7. Fair Value + Order Setup — and why the R/R gate overrides the nominal "Enter now" reading

**MoS / Max-Loss band for Composite Score 27.1 (the 0.0–29.9 tier): MoS 15–20%, Max Acceptable Loss 20–25%.**

### 7.1 Entry-price framing (same reasoning as the same-day INTU session)

Buy Price ceiling from Fair Value × (1−MoS), using Base Blended FV $341.62: at 20% MoS → $273.30; at 15% MoS → $290.38. **Live Price ($253.82) is already below both ceilings** — the "Score 0.0–29.9 → Stock at or below buy price → Enter now" case per fair-value-methodology.md's Integration table, not "Set limit order" in the naive reading. Per the same logic as INTU's §7.1, **Entry Price = Live Price ($253.82)** is used for the R/R check below (the real transaction, if made today, fills at the live price — not at a resting-limit ceiling nobody would actually pay).

Discount to Base FV at live price = 1 − 253.82/341.62 = **25.70%** — wider than the tier's 15–20% MoS floor, confirming the entry looks attractive on a pure-discount basis.

### 7.2 The R/R check — and where it fails

```
Stop @ 20% loss: $253.82×0.80 = $203.06 → R/R = (341.62−253.82)/(253.82−203.06) = 87.80/50.76 = 1.730:1
Stop @ 25% loss: $253.82×0.75 = $190.37 → R/R = (341.62−253.82)/(253.82−190.37) = 87.80/63.45 = 1.384:1
```

**R/R fails the 2:1 minimum across the ENTIRE allowed Max-Loss range (1.38:1–1.73:1) at the live price, using the Primary Sell Target.** This is a genuinely different outcome from the same-day INTU session, where the live-price reading *did* clear 2:1 (2.28:1) because INTU's discount-to-FV at live price (33.4%) was wide enough to carry the ratio. Here, a narrower 25.7% discount to a more modest (28.95% PW) upside isn't wide enough against a 20–25%-of-entry stop.

**Per fair-value-methodology.md Step 6: "If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely."** The tier's Max-Loss band floor (20%) is the tightest stop the framework's own table sanctions for this score band — solving for the entry price at which R/R = 2:1 using that 20% floor:

```
2.0 = (341.62 − Entry) / (Entry − 0.80×Entry) = (341.62 − Entry) / (0.20×Entry)
0.40×Entry = 341.62 − Entry
1.40×Entry = 341.62
Entry = $244.01
```

**A limit order at or below $244.01 (using the standard 20% stop) is required to satisfy the framework's 2:1 R/R minimum.** This is *tighter* than either MoS-derived buy ceiling ($273.30 at 20% MoS, $290.38 at 15% MoS) — meaning **R/R, not MoS, is the binding constraint** on this trade. $244.01 implies a ~28.6% discount to Base FV, deeper than even the top of this tier's stated 15–20% MoS band. Live price ($253.82) is only **~4.0% above** this threshold.

**Secondary reference only (does not rescue the primary check):** R/R against the Bull-Case Trim Target (Bull Blended FV × 0.90 = 460.56×0.90 = $414.50) at a 20% stop = (414.50−253.82)/50.76 = 3.166:1 — clears comfortably. But the framework's governing R/R check uses the **Primary** Sell Target (Base-Case FV), not the bull trim target — shown here for completeness, same as INTU's presentation, but it does not change the conclusion.

### 7.3 Order setup checklist (recommended limit price $244.01, informational — no order placed this session)

```
[x] Composite Score (nominal action band):        27.1   (0.0–29.9 → Full-position entry, nominally)
[x] Raw Valuation Score (incl. Upside/Downside):  39.0
[x] Expected annual return E / catalyst window:   +32.57% / 1.5yr
[x] Upside/Downside Modifier applied:             −15.0
[x] Base-Case Blended Fair Value:                 $341.62
[x] PW Blended Fair Value (for E, above):         $327.29
[x] LIVE PRICE:                                   $253.82  (R/R FAILS here — 1.38:1–1.73:1 across the tier's Max-Loss range)
[x] RECOMMENDED LIMIT PRICE (R/R = 2:1 at 20% stop): $244.01   ← binding constraint, tighter than the MoS ceiling
[x] PRIMARY SELL TARGET (= Base Blended FV):      $341.62
[x] BULL-CASE TRIM TARGET (Bull Blended FV × 0.90): $460.56 × 0.90 = $414.50
[x] STOP LOSS (20% below the $244.01 limit):      $244.01 × 0.80 = $195.21
[x] Risk/Reward Ratio at the limit price:          (341.62−244.01)/(244.01−195.21) = 97.61/48.80 = 2.00:1 — PASSES (at the boundary, by construction)
[x] Risk/Reward Ratio (bull-case trim target, at limit price): (414.50−244.01)/48.80 = 170.49/48.80 = 3.49:1 — clears comfortably
[x] Max $ Risk (1.5% of portfolio ≈$61,101.89, per holdings.md's 2026-08-22 combined-broker sync — informational
                                    only, no order placed this session):        $916.53
[x] Shares at that risk budget: $916.53 / $48.80 = 18.78 → 18 shares (risk-based, rounded down)
[x] Position Size cap check: 6–8% of portfolio = $3,666.11–$4,888.15 → risk-based size ($4,392.18) falls
                                    inside this band — no cap override needed
[x] POSITION SIZE ($) — informational only, no order placed: 18 × $244.01 = $4,392.18 (≈7.19% of portfolio)
[x] Hard 15% single-position cap (Upgrade 7): 7.19% — far under, no breach
```

---

## 8. Recommendation

**SET LIMIT ORDER at ≤$244.01 — NOT "enter now," despite the Composite Score (27.1) nominally sitting in the framework's most attractive 0.0–29.9 band.** This is the headline finding of this session: the Quality Gate (84.9), Rate Environment Gate, and Valuation Score (39.0, cheap) all point toward a full-position entry, and the Composite Score's own action-table lookup says "Enter now" since live price already sits below the MoS-derived buy ceiling — **but the framework's separate, hard Risk/Reward minimum (fair-value-methodology.md Step 6, operating-brief.md: "Below 2:1 = do not enter") fails at the live price across the tier's entire allowed stop-loss range (1.38:1–1.73:1)**, and that check is not optional or overridable by a favorable score. Live price ($253.82) is only about 4.0% above the $244.01 level at which R/R would actually clear 2:1.

**Three things for the human investor's judgment, beyond the mechanical output:**

1. **This is a real, structural finding, not a rounding artifact.** R/R fails everywhere in the allowed 20–25% Max-Loss band; it isn't close to marginal at the top of the band (1.38:1 at 25% loss) and only gets to a genuine boundary case (2.00:1) at a price ~4% below where the stock trades today.
2. **Earnings are 4 days away (Aug 27, 2026).** Per fair-value-methodology.md Rule 9, this is a mandatory re-valuation trigger regardless of outcome — Q2 FY2027 actuals, any FY2027 guidance revision, and confirmation or refutation of the reacceleration trend (§2, §5.5) will refresh nearly every input above within days. A limit order sitting unfilled into this print carries real gap risk in either direction; the framework has no rule instructing a delay ahead of a known catalyst, so this is surfaced as a judgment call, not an override.
3. **The Upside/Downside Modifier hit its −15 floor from a computed E (32.6%/yr) that is itself a sum of three separately-optimistic assumptions** (§5.5) — the underlying stack is more optimistic in combination than any single piece looks alone, same caveat as the same-day INTU session.

**No order is placed by this session** (per the task's explicit instruction — this produces a score/recommendation only).

---

## 9. Next Review Trigger

**Mandatory, near-term:** Autodesk's Q2 FY2027 earnings release, **2026-08-27** (4 days from this session) — a Rule 9 trigger regardless of outcome. Re-score immediately after, with particular attention to (a) whether the reacceleration in reported revenue growth (17.53%→18.28% TTM) persists into any FY2027 guidance revision, refreshing the Forward-PE and Upside/Downside Modifier inputs, and (b) whether the R/R gate's binding $244.01 limit-price threshold has been reached or passed by the market in the interim.

**Standing triggers (Rule 9):** guidance revision, M&A, management change (watch: ongoing Starboard activist pressure, §2 — no change has occurred as of this session, but this is the kind of situation where one plausibly could), macro shift, or a >15% unexplained move outside the above.

---

## 10. Watchlist Entry

Created `watchlist/not-in-portfolio/ADSK/ADSK-2026-08-23.md` — first-ever entry for this ticker (see §0/trigger). Full detail in that file; per watchlist/README.md convention it points back to this session as the canonical derivation record.

---

## Glossary

| Term | Meaning |
|---|---|
| **Autodesk Construction Cloud (ACC) / Forma** | Autodesk's cloud-based construction-industry platform (rebranded "Autodesk Forma") connecting owners, general contractors, subcontractors, and designers on a shared project dataset — cited as network-effect Moat Signal evidence in this session. |
| **Beta** | A stock's sensitivity to overall market moves — used (with the risk-free rate and Equity Risk Premium) to estimate the cost of equity in a DCF's WACC. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **Composite Score** | This framework's single ranking number blending the Quality Score and the Valuation Score 50/50 (0 = most attractive, 100.0 = least). ADSK scores 27.1. |
| **EV (Enterprise Value)** | A company's total value to all capital providers: market cap + debt − cash. |
| **EV/EBIT** | Enterprise Value divided by EBIT (operating profit) — a multiple used to compare how expensive companies are relative to operating profit, independent of capital structure. |
| **Fast Grower** | Peter Lynch's term for a company growing EPS faster than 15%/year for 3+ years — this framework's trigger for applying the PEG sub-score. ADSK does not qualify (only 1 of the last 3 fiscal years cleared 15%). |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. |
| **FCF Yield** | Free Cash Flow ÷ Market Cap — how much free cash a company throws off relative to its price; higher is cheaper. |
| **Forward PE** | Price ÷ next twelve months' expected earnings per share. |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook companies use for official financial statements. |
| **MoS (Margin of Safety)** | How far below fair value the buy price is set, as a cushion against being wrong. |
| **Moat Signal** | This framework's 5-point Quality Score checklist turning the general "Moat" concept into a scored input: market share stable/growing, brand premium, network effect, switching costs, and scale cost advantage, each markable TRUE only against a cited source. |
| **Named-User Licensing** | A software licensing model tying each subscription seat to one specific, non-shareable individual — Autodesk's "Transition to Named User" shift, paired with annual renewal-price increases, is cited as pricing-power/switching-cost Moat Signal evidence in this session. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt. |
| **Non-GAAP** | A company's own adjusted presentation of a financial measure that strips out items management deems non-recurring — this framework scores off GAAP figures, using Non-GAAP guidance only as context/DCF-modeling input, never as a scored sub-score. |
| **PEG (ratio)** | Forward PE ÷ expected EPS growth rate — a valuation check for fast-growing companies; a low PEG suggests cheap growth. |
| **Quality Score** | A 0–100.0 grade (0 = lowest quality, 100 = highest) blending profitability, margins, growth, balance sheet, moat, and FCF quality into one number; a company must score ≥80.0 to be eligible for Phase 02 valuation scoring. ADSK scores 84.9. |
| **Rate Environment Gate** | The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier. |
| **R/R (Risk/Reward Ratio)** | (Sell Target − Entry) ÷ (Entry − Stop Loss) — how much upside is on offer per unit of downside risked; this framework requires at least 2:1. ADSK's R/R fails at live price (1.38:1–1.73:1), which is the central finding of this session. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it into profit; a core quality signal in this framework. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% unexplained stock-price move. |
| **Shareholder yield** | Cash returned to shareholders as a percentage of share price — dividend yield plus net buyback yield combined. |
| **Terminal Value** | In a multi-stage DCF, the lump-sum value assigned to all cash flows beyond the explicit forecast period, discounted back to today. |
| **Upside/Downside Modifier** | An additive, ±15-bounded adjustment to the valuation score based on expected annual return — strong expected upside lowers the score, an expected loss raises it. |
| **WACC** | Weighted Average Cost of Capital — the blended cost a company pays for its debt and equity financing; used as the discount rate in a DCF. |

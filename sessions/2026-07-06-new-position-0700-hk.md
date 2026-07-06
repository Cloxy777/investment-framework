# NEW POSITION (Scheduled Watchlist Refresh) — Tencent Holdings (0700-HK) — 2026-07-06

**Task type:** NEW POSITION (full re-evaluation of an existing not-in-portfolio watchlist entry — not a fresh candidate discovery)
**Date:** 6 Jul 2026
**10Y US Treasury Yield:** 4.48% (last trade 2 Jul 2026 — US bond market closed 3–4 Jul 2026 for the Independence Day holiday; most recent available print, still inside the "3.5–5%" bracket)
**Rate Regime Modifier (Step 2):** +5
**Current 0700-HK portfolio weight:** 0% — confirmed not held ([holdings.md](../portfolio/holdings.md))
**Last review on record:** 31.0 (2026-06-14, [session](2026-06-14-new-position-tencent.md); [watchlist entry](../watchlist/not-in-portfolio/0700-HK/0700-HK-2026-06-14.md)) — flagged stale under **both** the 2026-06-20 (Upside/Downside Modifier) and 2026-06-29 (Quality Score + Composite Score) methodology tables in [STALE.md](../watchlist/STALE.md).
**First-ever Quality Score / Composite Score computation for 0700-HK this session.**

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EBITDA = operating profit before depreciation/amortization; EV/EBIT = enterprise value ÷ operating profit; PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; CAGR = compound annual growth rate; pp = percentage points; EY = earnings yield (1 ÷ PE); NOPAT = net operating profit after tax; ROIC = return on invested capital; TAM = total addressable market; TTM = trailing twelve months; NCI = non-controlling interests.*

---

## 1. Live Price (Rule 0) & Listing Choice

**Listing choice: HK primary listing (0700.HK / SEHK:700, HKD), not the TCEHY US OTC ADR** — consistent with the 2026-06-14 session's finding that TCEHY pricing is unreliable across sources. All calculations below are in HKD (converted from Tencent's RMB-denominated financial statements where needed).

| Field | Value | Source |
|---|---|---|
| **Live price used (0700.HK)** | **HKD 444.40** | IBKR `get_price_snapshot` (contract_id 152791428, SEHK, symbol "700" — resolved via `search_contracts`), `is_close: false` — live intraday quote, pulled this session |
| Prior close / intraday change | HKD 431.20 → 444.40 (+13.20, **+3.06%** today) | IBKR `get_price_snapshot` |
| Bid / Ask | HKD 444.20 / 444.40 | IBKR `get_price_snapshot` |
| 52-week range | HKD 411.00 – 683.00 | IBKR `misc_statistics` |
| Year-to-date change | **−25.93%** | IBKR `year_to_date_change` |
| USD/HKD | 7.8430 | WebSearch, 2026-07-06 |
| CNY/HKD | 1.1535 | WebSearch, 2026-07-06 |
| Shares outstanding | **9,056,427,794 (≈9.056B)** | companiesmarketcap.com, dated "July 2026" — see Data Gap #1 |
| Market cap (at HKD 444.40) | HKD 4,024,677M (≈HKD 4,024.7B) | Computed: 9.056B × 444.40 |
| Analyst consensus PT (12-month) | RMB 606.23 (≈HKD 699.29 at CNY/HKD 1.1535) — 45 analysts, consensus "Buy" | MarketScreener, 2026-07-06 — bull-case sanity anchor only, never a score input |

**Why the price is down ~26% YTD (context, not a score input):** per Bloomberg (30 Jun 2026) and corroborating coverage, 0700-HK has lost roughly $309B of market value since an October 2025 high (Hong Kong shares down over 35% from that peak) — driven by (a) investor doubts about the payback on Tencent's AI infrastructure spend (capex +16% YoY in Q1 2026, guided to more than double 2026 AI investment to >RMB36B), (b) a rotation of Chinese-market investor flows toward pure-play AI model developers, and (c) three straight months of mainland ("Southbound") net selling as of June 2026. Tencent has responded by accelerating buybacks (a record ~HKD9B repurchased in June 2026 alone). This is a sentiment/macro-driven de-rating, not a disclosed fundamental deterioration — Q1 2026 revenue and GAAP operating profit both grew (+9% and +17% YoY respectively) over the same window. Per [strategy.md](../framework/strategy.md) Phase 06, "price dropped" and "macro fear" are explicitly **not** valid reasons to act in either direction on their own — this is background color for the Upside/Downside Modifier's qualitative catalyst discussion (§7), not an input to the Quality or Valuation sub-scores themselves.

---

## 2. Data Gathered — Fresh TTM Build (ended 31 March 2026)

`yfinance` is unreachable this session (same persistent `curl_cffi`/TLS proxy failure documented across recent sessions, e.g. AMZN/META 2026-07 sessions). **All figures below are sourced directly from Tencent's own press releases (Q1 2026, FY2025, FY2024, FY2023 results announcements) via web fetch, not yfinance or an aggregator.**

### Quarterly & annual source figures (RMB millions, as officially reported)

| Line | FY2025 | Q1 2026 | Q1 2025 | FY2024 | FY2023 | FY2022 |
|---|---|---|---|---|---|---|
| Revenue | 751,766 | 196,458 | 180,022 | 660,257 | 609,015 | 554,552 |
| Gross profit | 422,593 | 111,265 | 100,493 | 349,246 | 293,109 | 238,746 |
| Gross margin | 56% | 57% | 56% | 53% | 48% | 43% |
| Operating profit (GAAP/IFRS) | 241,562 | 67,375 | 57,566 | 208,099 | 160,074 | 110,827 |
| Non-IFRS operating profit | 280,656 | 75,627 | 69,320 | 237,811 | — | — |
| Net income attributable (GAAP) | 224,842 | 58,093 | 47,821 | 194,073 | 115,216 | 188,243 |
| Non-IFRS net profit attributable | 259,626 | 67,905 | 61,329 | 222,703 | 157,688 | — |
| **Diluted EPS (GAAP, RMB)** | **24.153** | **6.302** | **5.129** | **20.486** | **11.887** | **19.341** |
| Capex | 79,198 | 31,936 | 27,476 | 76,760 | 23,893 | 18,014 |
| Free cash flow | 182,600 | 56,700 | 47,100 | 155,300 | — | — |
| EBITDA | 310,767 | 84,167 | 73,817 | 256,310 | — | — |
| Net cash (period-end, company-disclosed) | 107,145 | 146,860 | 90,229 | 76,798 | 54,740 | (14,832) net debt |
| Other gains/(losses), net | (3,177) | 1,253 | (1,397) | 8,002 | — | — |
| Pretax income | 277,200 | 73,969 | 63,442 | 241,500 | — | — |
| Income tax expense | 47,400 | 14,577 | 13,717 | 45,000 | — | — |

Sources: [Q1 2026 results (Tencent IR PDF)](https://static.www.tencent.com/uploads/2026/05/13/47382ae415a209fd161bc19a1f9b3704.pdf), [FY2025 annual results (PRNewswire)](https://www.prnewswire.com/apac/news-releases/tencent-announces-2025-annual-and-fourth-quarter-results-302717280.html), [FY2023 annual results (PRNewswire)](https://www.prnewswire.com/apac/news-releases/tencent-announces-2023-annual-and-fourth-quarter-results-302094552.html), plus WebSearch aggregation for FY2024 FCF (RMB155.3B) and Q1 2025 FCF (RMB47.1B, both cross-checked against Tencent's own "up X% YoY" framing in the Q1 2026 / FY2025 releases).

### Balance sheet as of 31 March 2026 (Q1 2026 report)

| Item | Value (RMB millions) |
|---|---|
| Cash and cash equivalents | 217,770 |
| Term deposits (current) | 205,537 |
| Term deposits (non-current) | 73,404 |
| Borrowings (current + non-current) | 51,114 + 207,881 = 258,995 |
| Notes payable (current + non-current) | 3,460 + 124,350 = 127,810 |
| **Total debt (borrowings + notes payable)** | **386,805** |
| Total equity (incl. non-controlling interests) | 1,211,627 |
| Non-controlling interests | 83,975 |
| **Net cash (company-disclosed)** | **146,860** |

### TTM roll-forward (ended 31 March 2026) — FY2025 + Q1 2026 − Q1 2025, shown in full

```
Revenue        = 751,766 + 196,458 − 180,022 = 768,202
Gross profit   = 422,593 + 111,265 − 100,493 = 433,365   → Gross margin = 56.42%
EBIT (GAAP)    = 241,562 +  67,375 −  57,566 = 251,371
Net income     = 224,842 +  58,093 −  47,821 = 235,114   → Net margin = 30.61%
Diluted EPS    =  24.153 +   6.302 −   5.129 =  25.326
Capex          =  79,198 +  31,936 −  27,476 =  83,658
FCF            = 182,600 +  56,700 −  47,100 = 192,200
EBITDA         = 310,767 +  84,167 −  73,817 = 321,117
Pretax income  = 277,200 +  73,969 −  63,442 = 287,727
Tax expense    =  47,400 +  14,577 −  13,717 =  48,260   → Effective tax rate = 16.78%
D&A (derived, EBITDA = OpProfit − OtherGains,net + D&A per Tencent's own formula):
  FY2025 D&A  = 310,767 − 241,562 + (−3,177) = 66,028
  Q1 2026 D&A =  84,167 −  67,375 +   1,253  = 18,045
  Q1 2025 D&A =  73,817 −  57,566 + (−1,397) = 14,854
  TTM D&A     = 66,028 + 18,045 − 14,854 = 69,219
```

All in RMB millions.

### 5-year historical PE (wisesheets.io, 2026-07-06 — used for the 2026-06-20 5yr-lookback methodology)

| Year | PE ratio |
|---|---|
| 2021 | 14.53 |
| 2022 | 14.18 |
| 2023 | 22.05 |
| 2024 | 18.70 |
| 2025 | 22.32 |

**5yr low = 14.18 | 5yr high = 22.32 | 5yr avg = 18.35** (internally consistent — the stated average matches the mean of the five listed years exactly). Cross-checked against stockanalysis.com's own annual-PE series (15.79 / 14.77 / 21.63 / 18.44 / 21.63, avg ≈18.45) — broadly the same shape, but that series repeats an identical value for 2023 and 2025, an internal inconsistency that makes wisesheets the more reliable of the two (see Data Gap #2).

### FY2026 consensus (MarketScreener, 45 analysts, 2026-07-06)

| Metric | FY2026E | FY2027E |
|---|---|---|
| Diluted EPS (RMB) | **25.84** | 29.31 |
| Revenue (RMB millions) | 828,028 | — |
| Net income (RMB millions) | 236,156 | — |

Cross-check: consensus net income ÷ consensus EPS = 236,156/25.84 ≈ 9,138M diluted shares — within ~0.9% of the 9,056M shares-outstanding figure used above, a reasonable (not exact) consistency check.

---

## 3. Data Gaps, Corrections & Flags

1. **Shares outstanding disagree meaningfully across sources.** companiesmarketcap.com (9,056,427,794, dated "July 2026") is used as primary — it is specific, dated, and close to the 2026-06-14 session's independently-computed 9.02B (market cap ÷ price at that time) and to the consensus-implied ~9.14B cross-check above. Two other readings conflict: stockanalysis.com's own market-cap page (HKD 3.87T at ~HKD444.20, implying only ~8.71B shares) and a separate aggregator citing "9.52–9.56B shares" — a ~9% spread across sources for the same figure. This is the same class of cross-source data-integrity issue flagged for this ticker in the 2026-06-14 session (there: 52-week-low and ROIC disagreement). Not resolved further this session; flagged for the next `/rescore`.
2. **5-year historical PE series** — wisesheets.io's per-year table is internally consistent (the stated average matches the listed years); stockanalysis.com's competing series repeats an identical PE for 2023 and 2025, which cannot both be independently correct — treated as the less reliable of the two and not used.
3. **Historical PE Modifier gray zone (§6).** Forward PE sits −18.76% versus the 5yr average — inside neither of [valuation-scoring.md](../framework/valuation-scoring.md)'s two named buckets ("&gt;20% below" → −10, "within ±10%" → 0). The rule does not define the 10–20% zone. Applied **0** (no modifier) as the literal, conservative default since neither named condition is met — flagged as a framework gap worth an explicit clarification (in the spirit of the 2026-06-20 PEG clean-earnings clarification), not silently resolved by inventing an interpolation formula.
4. **Data-quality correction — the 2026-06-14 session's EPS series mixed GAAP and non-IFRS figures across years without saying so.** That session's table (labeled "Diluted EPS (GAAP, continuing ops)") showed FY2022 19.341, FY2023 16.320, FY2024 23.505, FY2025 24.153. Cross-checking against Tencent's own primary filings this session: FY2022 (19.341) and FY2025 (24.153) do match the official **GAAP** diluted EPS, but FY2023's **true GAAP** diluted EPS is **11.887** (not 16.320) and FY2024's is **20.486** (not 23.505). The 16.320/23.505 figures are extremely close to the **non-IFRS (adjusted)** diluted EPS instead (independently reconstructed here as ≈16.27 and ≈23.51 respectively, using each year's non-IFRS profit ÷ implied diluted share count) — i.e., the prior session silently blended two different earnings bases across years. **This session uses a single, consistent, all-GAAP diluted EPS series** (19.341 / 11.887 / 20.486 / 24.153) throughout. This is a data-quality correction discovered this session, not a change in the underlying business, but it materially changes the EPS-growth trajectory used for the Fast-Grower/PEG test (§5) — the corrected series shows an even sharper FY2023 decline (−38.55% vs. the previously-reported −15.6%), reinforcing (not reversing) the prior conclusion that PEG doesn't apply.
5. **Net cash reconciliation.** A bottom-up reconstruction (cash + term deposits − borrowings − notes payable) from the disclosed balance-sheet lines doesn't precisely tie out to Tencent's own disclosed "Net cash" figure (a gap of several tens of billions of RMB, likely due to an undisclosed narrower definition of "term deposits and others" in the company's own formula). Per Rule 0 discipline, this session uses Tencent's own **directly-disclosed** Net cash figures (RMB146,860M at 31 Mar 2026; RMB107,145M at 31 Dec 2025) rather than a bottom-up reconstruction, rather than presenting an invented number.
6. **Shareholder-yield buyback component is an estimate, not a guided figure.** No single "FY2026 buyback budget" was found (Tencent's May 2026 AGM authorized a mandate to repurchase up to ~912M shares, ~10% of shares — a ceiling/authorization, not a spending commitment). Used the ~1.24% YoY net share-count reduction (companiesmarketcap.com) as the net buyback-yield proxy for the Upside/Downside Modifier (§7) — an empirical, realized figure rather than a bottom-up guess.
7. **Consensus estimates (EPS, revenue, net income) sourced from a single aggregator (MarketScreener, 45 analysts)** — not cross-validated against a second consensus provider this session.

---

## 4. Phase 01 — Quality Gate Re-verification (fresh data)

| Check | Tencent TTM value | Threshold | Result |
|---|---|---|---|
| Gross margin | 56.42% (TTM to 31 Mar 2026) | >40% | ✅ PASS |
| Net margin | 30.61% (TTM, GAAP attributable) | >12% (valuation-scoring.md) / >15% (strategy.md) | ✅ PASS |
| ROIC | 18.99% (TTM — see §5 Profitability for full calc) | >15% | ✅ PASS |
| Revenue CAGR 3yr | 10.67% (FY2022 RMB554,552M → FY2025 RMB751,766M) | >8% | ✅ PASS |
| FCF positive 3+ consecutive years | FY2024 RMB155.3B, FY2025 RMB182.6B, TTM RMB192.2B — all positive and growing | required | ✅ PASS |
| Net debt/EBITDA | Net **cash** RMB146.86B (TTM EBITDA RMB321.1B) → −0.457× | <2.5x | ✅ PASS (net cash) |
| FCF/NI conversion | FY2024 80.0%, FY2025 81.2%, TTM 81.75% — comfortably above 70% both full years on record | >70% | ✅ PASS |

**Gate result: 8/8 PASS, confirmed with fresh TTM data.** No hard disqualifier fires (see §5). Proceeds to the full Quality Score.

---

## 5. Quality Score (first-ever computation for 0700-HK, 2026-06-29 methodology)

```
Profitability (25%):
  Net Margin (TTM, GAAP)  = 235,114 / 768,202 = 30.61%
  NOPAT = EBIT × (1 − effective tax rate) = 251,371 × (1 − 0.1678) = 209,191
  Net Invested Capital = Total Debt (386,805) + Total Equity (1,211,627) − Cash+TermDeposits (496,711)
                       = 1,101,721
  ROIC = 209,191 / 1,101,721 = 18.99%

  NetMargin_Component = clamp((30.61/30)×100, 0, 100) = 100.0   (clamped — margin exceeds the 30% anchor)
  ROIC_Component       = clamp((18.99/30)×100, 0, 100) = 63.3
  Profitability_Score  = (100.0 + 63.3) / 2 = 81.65   (no FCF cap — FCF-positive every year on record)

Margins (15%): Gross margin 56.42% (TTM) — structurally expanding for 4 straight years
  (FY2022 43% → FY2023 48% → FY2024 53% → FY2025 56% → TTM 56.4%)
  GrossMargin_Score = clamp((56.42/80)×100, 0, 100) = 70.5
  (No +10 trend bonus — that bonus applies only when margin is still *below* 40% and improving;
   Tencent's margin already clears 40% comfortably, so the raw formula already credits the level.)

Growth (20%): Revenue 3yr CAGR, FY2022 RMB554,552M → FY2025 RMB751,766M
  CAGR = (751,766/554,552)^(1/3) − 1 = 10.67%
  Growth_Score = clamp((10.67/25)×100, 0, 100) = 42.7
  + 10 (documented TAM expansion / pricing power, no structural-deceleration evidence found:
    Marketing Services revenue +20% YoY in Q1 2026 on an upgraded AI-driven ad-recommendation model
    and "improved ad performance and pricing" (direct pricing-power citation, Tencent's own MD&A);
    Business Services (cloud) revenue +20% YoY on AI-related demand and "a more favorable pricing
    environment"; International Games +13% YoY (14% constant-currency) on Clash Royale/Wuthering
    Waves/VALORANT PC. Q1 2026's headline revenue growth (+9% YoY, below FY2025's +14%) is explicitly
    attributed by management to Spring Festival calendar timing shifting revenue recognition out of
    the quarter — a documented *cyclical/timing* effect, not the *structural* deceleration this
    framework's −10 penalty is reserved for, so no penalty applied.)
  Growth_Score (with bonus) = 52.7

Balance Sheet (15%): Net cash (company-disclosed) RMB146,860M; TTM EBITDA RMB321,117M
  Net Debt/EBITDA = −146,860 / 321,117 = −0.457×  (net cash position)
  BalanceSheet_Score = clamp(100×(1−(−0.457)/4), 0, 100) = clamp(111.4, 0, 100) = 100.0

Moat Signal (15%) — checklist, cited evidence:
  ✓ Market share stable/growing — TRUE. Combined Weixin/WeChat MAU 1,432M, +2% YoY / +1% QoQ
     (Q1 2026 report) — the dominant, still-growing Chinese social/messaging platform. Evergreen
     games Honour of Kings, Peacekeeper Elite, and Delta Force each hit "life-time highs" in quarterly
     gross receipts in Q1 2026 (Tencent's own MD&A) — sustained #1 domestic gaming franchise position.
  ✓ Brand premium — TRUE. Marketing Services revenue +20% YoY explicitly tied to "improved ad
     performance and pricing" following an AI-driven ad-model upgrade — a direct, cited pricing-power
     data point, on top of Weixin's decades-long default-super-app status in China.
  ✓ Network effect — TRUE. Weixin is a textbook multi-sided network (personal messaging + Mini
     Shops/Mini Programs merchants + advertisers + Tencent Cloud enterprise tools) — Mini Shops GMV
     "sustained a rapid year-on-year growth rate" per Q1 2026 MD&A, and buyer/merchant/advertiser
     participation reinforce each other on the same platform.
  ✓ Switching costs — TRUE. The Weixin ecosystem is deeply embedded for both consumers (social graph,
     payment history, Mini Program usage habits) and merchants (Mini Shops storefronts, the AIM+
     automated ad-campaign tool now powering ~30% of total marketing-services ad spend) — migrating
     off the platform means rebuilding both audience and campaign infrastructure from zero.
  ✗ Scale cost advantage — FALSE (not credited). No company-specific, cited cost-per-unit data point
     (e.g. cost-per-server, cost-per-DAU infrastructure efficiency) was found this session to support
     this signal independently of the other four — consistent with this framework's practice of not
     crediting scale advantages without a specific citation (cf. NVDA/MSFT sessions' treatment of
     CoWoS/PUE evidence).
  Moat_Score = (4/5) × 100 = 80.0

FCF Quality (10%): FCF/NI TTM = 192,200 / 235,114 = 81.75%
  FCFQuality_Score = clamp(((0.8175 − 0.40)/0.60)×100, 0, 100) = 69.6
  FY2024 FCF/NI = 155,300/194,073 = 80.0%; FY2025 = 182,600/224,842 = 81.2% — both years comfortably
  above 70%; no hard-disqualifier risk.

Quality Score = 81.65×0.25 + 70.5×0.15 + 52.7×0.20 + 100.0×0.15 + 80.0×0.15 + 69.6×0.10
              = 20.4125 + 10.575 + 10.54 + 15.0 + 12.0 + 6.96
              = 75.4875 → rounds to 75.5
```

**Quality Score = 75.5 — FAILS the 80.0+ gate, narrowly (4.5 points short).**

**Hard disqualifier check: none fire.** FCF/NI conversion is comfortably above 70% both years on record (no need for a growth-capex carve-out); Net Debt/EBITDA is a net-cash position; FCF-positive every year on record.

**Why this is a near-miss, not a red flag.** Three of the six sub-scores are at or near the 100.0 ceiling (Balance Sheet 100.0, Moat 80.0, and Profitability 81.65, which is itself capped by a Net Margin already above the scale's 30% anchor). The two sub-scores holding the total back are **Growth (52.7)** and **Margins (70.5)** — not because Tencent's growth or margins are weak in absolute terms (10.67% revenue CAGR clears the >8–10% Phase 01 bar comfortably, and 56.4% gross margin clears the >40% bar by a wide margin), but because this framework's 0–100.0 anchors for those two sub-scores are set high (25% CAGR and 80% gross margin both map to 100.0) — the same dynamic seen in other large, mature-but-still-growing compounders scored under this engine (e.g. AMZN's 56.93 Growth sub-score, GOOG's ~99 Profitability but comparatively modest Growth). **This is the framework's strict 80.0+ gate doing exactly what it was designed to do** (per [quality-scoring.md](../framework/quality-scoring.md): "a deliberately high bar... to be loosened later only if it screens out too much of the investable universe") — it is not a signal that Tencent's underlying business quality has deteriorated. A meaningfully faster growth cadence or continued gross-margin expansion toward the 65–70%+ range would be the concrete path to clearing 80.0 at a future rescore.

**Conglomerate/investment-portfolio caveat (carried from the 2026-06-14 session's ROE finding).** Tencent's balance sheet carries a very large non-operating investment portfolio (RMB912.2B combined listed + unlisted investee fair value at 31 Mar 2026, per the Q1 2026 report). This inflates the Net Invested Capital denominator used for ROIC above (relative to a "core operating business only" calculation), meaning the 18.99% ROIC figure — while already comfortably clearing the >15% Phase 01 bar — likely **understates** the core operating business's true return on capital, the same direction of distortion flagged for ROE in the prior session. Not adjusted for here (no clean methodology to isolate "core" invested capital without inventing a number), but noted as a conservative-direction caveat on the Profitability sub-score.

---

## 6. Fast Grower (Upgrade 3 — PEG) Determination

**Test: EPS growth >15% for 3+ consecutive years, on a clean/non-distorted base.** Using the corrected, consistent, all-GAAP diluted EPS series (§3 Data Gap #4):

| Year | Diluted EPS (GAAP, RMB) | YoY growth | >15%? |
|---|---|---|---|
| FY2022 | 19.341 | — | — |
| FY2023 | 11.887 | **−38.55%** | ❌ No (sharp decline) |
| FY2024 | 20.486 | **+72.35%** | ✅ Yes |
| FY2025 | 24.153 | **+17.90%** | ✅ Yes |

Two of the last three years clear 15%, but FY2023's −38.55% collapse breaks the "3+ consecutive years" requirement outright. The FY2022 base itself is also flagged as distorted: FY2022's GAAP net income (RMB188.243B) was unusually high relative to FY2022's own operating profit (RMB110.827B) and relative to FY2023's clean RMB115.216B — consistent with a large one-off/investment-revaluation gain inflating the FY2022 earnings base (Tencent's investment portfolio saw large swings across 2022's market conditions). This is exactly the "recent one-off-distorted EPS" carve-out in [valuation-scoring.md](../framework/valuation-scoring.md)'s Fast-Grower eligibility clarification (2026-06-20).

**Determination: 0700-HK does NOT meet the Fast-Grower test — neither on the "3+ consecutive years" count nor on having a clean, non-distorted base.** **PEG's 15% weight is redistributed to EV/EBIT** (40% total), same conclusion as the 2026-06-14 session, now on a corrected and more clearly-supported data basis.

---

## 7. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test** (using the Forward PE computed in §8 below)
```
Forward PE = HKD 444.40 / HKD 29.808 (FY2026E EPS converted) = 14.909×
EY     = 1 ÷ 14.909 = 6.7074%
Spread = EY − 10Y Treasury = 6.7074% − 4.48% = +2.2274%
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** (+2.23%, above threshold) → **no additive** (Step 1 = 0).

**Step 2 — Rate Regime Modifier**
10Y = 4.48% → "3.5–5%" bracket → **+5**

**Total Rate Modifier = +5** (unchanged in direction/size from the 2026-06-14 session).

---

## 8. Phase 02 — Full Valuation Score Calculation

**Owner Earnings (Upgrade 1) applicability check — shown explicitly:**
```
TTM Capex = 83,658 (RMB millions); TTM D&A (maintenance-capex proxy) = 69,219
Growth Capex = 83,658 − 69,219 = 14,439
Growth Capex % of total = 14,439 / 83,658 = 17.26%
```
17.26% is **below** the 30% Upgrade-1 trigger → **Owner Earnings does NOT apply**; raw reported FCF is used (same conclusion as the 2026-06-14 session, now with an explicit growth-capex-ratio calc to support it — Tencent is meaningfully less capex-intensive in its AI buildout than MSFT/GOOGL/META/AMZN, all four of which the framework mandates Owner Earnings for).

**FCF Yield — 40% weight**
```
TTM FCF (HKD) = RMB192,200M × 1.1535 = HKD 221,742M
Market Cap    = HKD 4,024,677M
FCF Yield     = 221,742 / 4,024,677 = 5.510%

FCF_Score = clamp(100 × (1 − 5.510/10), 0, 100) = 44.90
```
→ Contribution: 44.90 × 0.40 = **17.960**

**EV/EBIT — 40% weight (PEG not applicable, redistributed from 25%)**
```
Net cash (HKD) = RMB146,860M × 1.1535 = HKD 169,398M
EV = Market Cap − Net cash = 4,024,677 − 169,398 = HKD 3,855,279M

EBIT TTM (HKD) = RMB251,371M × 1.1535 = HKD 289,957M

EV/EBIT = 3,855,279 / 289,957 = 13.296×

EV/EBIT_Score = clamp((13.296 − 12)/23 × 100, 0, 100) = clamp(5.635, 0, 100) = 5.635
```
→ Contribution: 5.635 × 0.40 = **2.254**

**Forward PE — 20% weight (PRIMARY formula — 5yr low/high range available)**
```
FY2026E EPS (RMB) = 25.84 (MarketScreener consensus, 45 analysts)
FY2026E EPS (HKD) = 25.84 × 1.1535 = 29.808
Forward PE        = 444.40 / 29.808 = 14.909×

5yr Low PE  = 14.18
5yr High PE = 22.32
5yr Avg PE  = 18.35

FwdPE_Score (raw) = clamp((14.909 − 14.18)/(22.32 − 14.18) × 100, 0, 100)
                   = clamp(0.729/8.14 × 100, 0, 100) = 8.96
```

**Historical PE Modifier (Upgrade 2):**
```
Deviation from 5yr avg = (14.909 − 18.35)/18.35 = −18.76%
```
−18.76% falls **between** the framework's two named buckets (>20% below → −10; within ±10% → 0) — see Data Gap #3. **Modifier applied: 0** (literal, conservative default; flagged as an unaddressed gray zone, not resolved by an invented interpolation).
```
FwdPE_Score (adjusted) = 8.96 + 0 = 8.96
```
→ Contribution: 8.96 × 0.20 = **1.792**

**PEG — not applicable (redistributed to EV/EBIT above, see §6)**

### Raw Weighted Score

```
Raw weighted = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.40) + (FwdPE_Score(adj) × 0.20)
             = 17.960 + 2.254 + 1.792
             = 22.006

+ Rate Regime Modifier (+5, Step 2 only — Step 1 passed) = 27.006
```

(Upside/Downside Modifier applied next, §9, before final rounding.)

---

## 9. Upside/Downside Modifier (Expected-Return Modifier)

**Scenario fair value (Rule 7), EV/EBIT-multiple method on forward EBIT** — chosen over a full DCF for time efficiency, consistent with the AMZN/GOOG 2026-07-04 rescore precedent. Three scenarios reflecting the AI-monetization debate that is the actual driver of the current de-rating (§1):

| Scenario | Wt | Narrative | Forward EBIT (HKD, ×TTM EBIT 289,957) | Exit EV/EBIT | Equity Value (+Net Cash 169,398) | FV/share (÷9,056.4M sh) |
|---|---|---|---|---|---|---|
| Bull | 25% | AI products (Hy3, WorkBuddy) scale faster than the market currently prices; ad/cloud AI-driven growth (both +20% YoY in Q1 2026) continues; "operating profit excluding new AI products" gap narrows as new products monetize | 289,957×1.20=347,948 | 16.0× | 347,948×16.0+169,398 = 5,736,566 | **HKD 633.55** |
| Base | 50% | Consensus-like continuation: steady ad/cloud/gaming growth, AI investment remains a near-term margin drag, gradual proof points | 289,957×1.12=324,752 | 14.0× | 324,752×14.0+169,398 = 4,715,926 | **HKD 520.75** |
| Bear | 25% | AI monetization doubts persist/worsen, continued investor rotation to pure-play AI names and Southbound selling keep the multiple compressed regardless of steady fundamentals | 289,957×1.03=298,656 | 11.0× | 298,656×11.0+169,398 = 3,454,614 | **HKD 381.51** |

```
PW Fair Value = 0.25×633.55 + 0.50×520.75 + 0.25×381.51 = 158.39 + 260.38 + 95.38 = HKD 514.14
```

**Sanity check (Rule 4):** PW FV (HKD 514.14) sits below the bull case, above the bear case, and below the MarketScreener consensus PT of ~HKD 699.29 (which likely reflects a less AI-monetization-skeptical view than this framework's own scenario weighting) — a reasonable, moderately conservative placement.

**Step 2 — Gap, annualization, components**
```
Gap Upside %    = (514.14 ÷ 444.40) − 1 = +15.696%
Catalyst window = 2 years (default — no single hard, dated re-rating catalyst identified; the AI-
                   monetization proof-point story plays out over several more quarterly earnings
                   releases rather than one specific event, similar to AMZN's capex-cycle framing)
Annualized gap  = 15.696% ÷ 2 = +7.848%/yr
Intrinsic growth = +10%/yr (anchored to the 10.67% 3yr revenue CAGR and consensus long-run EPS
                   growth estimates of ~11-12%/yr cited across aggregators; used as a round, slightly
                   conservative figure)
Shareholder yield = Dividend yield 1.29% (HKD 5.30/share FY2025 dividend, per multiple aggregators,
                    as of 2026-06-28) + net buyback yield 1.24% (realized YoY net share-count
                    reduction, companiesmarketcap.com — buybacks net of any SBC-driven issuance)
                  = 2.53%
```
```
E (expected annual return) = 7.848 + 10.0 + 2.53 = +20.378%/yr
```

**Step 3 — Guardrail 1 (catalyst discipline).** E is on the **upside (E ≥ H)** side of the mapping. Per [valuation-scoring.md](../framework/valuation-scoring.md): *"If no catalyst identifiable within 18–24 months, cap upside (negative) side at −5."* No single hard, dated catalyst was identified this session (the AI-monetization narrative is a multi-quarter proof-point story, not a specific event with a date) — **the −5 cap applies.**

**Step 4 — Map E to the modifier, then apply the guardrail cap:**
```
E ≥ H (10%): M(uncapped) = −15 × clamp((E−H)/15pp, 0, 1) = −15 × clamp((20.378−10)/15, 0, 1)
           = −15 × clamp(0.6919, 0, 1) = −15 × 0.6919 = −10.38

Guardrail 1 cap (no dated catalyst within 18-24mo): M = max(−10.38, −5.0) = −5.0
```

**Interpretation:** without the guardrail, the raw expected-return math (a ~20%/yr blended expected return, driven mostly by durable intrinsic growth and a modest re-rating gap) would have earned close to the full −15 "strongly attractive" credit. The framework's catalyst-discipline guardrail exists precisely for this situation — a broad, multi-quarter "AI monetization eventually proves out" story without one dated, verifiable trigger — and caps the credit at −5 rather than letting an appealing narrative award the maximum discount.

---

## 10. Final Valuation Score, Quality Score, Composite Score

```
FINAL VALUATION SCORE = Raw weighted (22.006) + Rate Modifier (+5, already in raw weighted total
                         above at line "27.006") + Upside/Downside Modifier (−5.0, capped)
                       = 22.006 + 5.0 − 5.0
                       = 22.006
```
Boundary rule: 22.006 → nearest 0.1 → not a ".X5" case → **Final Valuation Score = 22.0**

| | Value |
|---|---|
| Raw weighted (4 sub-scores) | 22.006 |
| Rate Regime Modifier (Step 2; Step 1 passed) | +5.0 |
| Upside/Downside Modifier (capped, Guardrail 1) | −5.0 |
| **FINAL VALUATION SCORE** | **22.0** |
| Prior valuation score | 31.0 (2026-06-14, pre-Upside/Downside-Modifier methodology) |
| **Quality Score (first-ever)** | **75.5 (FAILS 80.0+ gate)** |

```
Composite Score = 0.50 × (100 − 75.5) + 0.50 × 22.0
                = 0.50 × 24.5 + 0.50 × 22.0
                = 12.25 + 11.0
                = 23.25
```
Boundary rule: 23.25 is exactly a ".X5" case → round **up** (conservative) → **Composite Score = 23.3**

---

## 11. Action & Why the Composite Score Must Not Be Read at Face Value

**Read in isolation, the numbers look highly attractive:** Valuation Score 22.0 sits in the 0.0–29.9 "Very Cheap" band (→ "Full position 6–8%" per the Phase 03 table), and the blended Composite Score of 23.3 sits in the same band.

**This is exactly the "false green light" pattern this repo has documented repeatedly since the 2026-06-29 Quality Score addition** (AMZN, GOOG, MSFT, NOW, NFLX, NVO, SPGI, SPOT, TRN, UBER, ZS, NKE — see each ticker's 2026-07 rescore session). **0700-HK's Quality Score of 75.5 fails the strict 80.0+ gate** ([quality-scoring.md](../framework/quality-scoring.md)): *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all... Composite Score isn't computed for, and doesn't rescue, a company failing the quality gate."* Per this session's explicit brief, the Composite Score above is shown **as a reference number only** — it must not be acted on at face value.

**Practical difference from the AMZN/GOOG precedent:** those are *existing holdings*, where a Quality Score failure is treated as a Phase 04 "Quality Watch" flag (not an automatic force-exit), because the position is already owned and the framework's anti-turnover posture applies. **0700-HK is not held.** For a *candidate that has never cleared the entry gate*, there is no existing position to protect from over-trading — the Quality Score failure here means Phase 01's entry gate has not been cleared, full stop, regardless of how cheap the valuation score reads.

**Recommendation: PASS — do not open a new position.** The very-cheap Valuation Score (22.0) and resulting Composite Score (23.3) are real calculations, shown in full above, but they cannot override a Quality Score that hasn't cleared the 80.0+ bar this framework requires before Phase 02/03 sizing logic applies at all. This is **not** a judgment that Tencent is a poor business — as §5 details, the Quality Score is a narrow, 4.5-point miss driven by two sub-scores (Growth 52.7, Margins 70.5) that reflect the framework's high anchors more than any actual weakness, and the other four sub-scores (Profitability, Balance Sheet, Moat, FCF Quality) are strong-to-excellent. It is a statement that **this specific candidate does not yet meet this specific framework's strict quality bar for a new entry**, and the currently-depressed price (down ~26% YTD on AI-monetization sentiment, not disclosed fundamentals) does not change that gate.

**No order setup is produced** — per [operating-brief.md](../framework/operating-brief.md) OUTPUT FORMAT step 6, the buy/sell/stop order-setup checklist in [fair-value-methodology.md](../framework/fair-value-methodology.md) applies only to a BUY or TRIM action; this session's action is PASS.

---

## 12. Watchlist & Stale-Score Update

Per [watchlist/README.md](../watchlist/README.md), this evaluation writes a new dated entry (`watchlist/not-in-portfolio/0700-HK/0700-HK-2026-07-06.md`) since the score, the action category, and the scored-metric set (first-ever Quality/Composite Scores) have all changed from the 2026-06-14 entry. Both `⚠️ STALE SCORE` banners on that prior entry are removed in the new file. Per this session's explicit scope, the orchestrator (not this session) is responsible for deleting 0700-HK's two rows in [watchlist/STALE.md](../watchlist/STALE.md) and for not running any `git` commands here.

---

## 13. Next Review Triggers

- **Q2 FY2026 earnings** — Tencent's quarterly cadence points to a mid-August 2026 release (the natural next checkpoint for whether the AI-monetization proof points — narrowing the "operating profit excluding new AI products" gap, continued ad/cloud AI-driven growth — materialize, per Rule 9).
- **Any confirmed, dated AI-monetization catalyst** (e.g., a specific disclosed revenue contribution or margin inflection date for Hy3/WorkBuddy/Yuanbao) would remove the Guardrail-1 cap on the Upside/Downside Modifier at the next rescore, materially changing the Valuation Score.
- **Quality Score watch:** re-verify Growth and Margins sub-scores at the next full evaluation — sustained double-digit-plus revenue growth or continued gross-margin expansion toward 60%+ would be the concrete path to clearing the 80.0+ gate.
- **Rule 9 standing triggers:** any Chinese gaming/WeChat regulatory action, management change, material M&A, or a >15% unexplained price move from HKD 444.40.
- **`yfinance` restoration:** if proxy/TLS access is restored, cross-check this session's manually-reconstructed TTM figures and the 5yr PE range against the automated method in [valuation-scoring.md](../framework/valuation-scoring.md), and resolve the shares-outstanding and Historical-PE-Modifier-gray-zone flags (Data Gaps #1, #3) with a cleaner data source.

---

## 14. Glossary

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
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying — not computed this session (no order setup produced). |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt (negative = net cash). |
| **NCI (Non-controlling interest)** | The portion of a consolidated subsidiary's equity that belongs to outside shareholders rather than the parent. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **Owner Earnings** | Net Income + D&A − maintenance capex only — used instead of raw FCF for moat-building reinvestors where growth capex exceeds 30% of total (not triggered here; Tencent's ratio is 17.26%). |
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
| **SBC (Stock-Based Compensation)** | Employee pay in company shares/options — a non-cash expense that dilutes existing shareholders over time. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle, subject to a catalyst-discipline guardrail capping the upside side at −5 absent a dated catalyst within 18–24 months. |
| **Value trap** | A stock that looks statistically cheap but stays cheap because underlying quality is weaker than the multiple suggests — the exact risk this framework's Quality Score gate exists to surface. |

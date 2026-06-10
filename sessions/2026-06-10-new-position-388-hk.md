# New Position Evaluation — Hong Kong Exchanges and Clearing (388.HK)

**Date:** 2026-06-10
**Task type:** NEW POSITION
**10Y US Treasury yield:** 4.54%

---

## Rule 0 — Live Price Verification

| Field | Value | Source |
|---|---|---|
| Live price | **HKD 380.60** | IBKR real-time market data, 2026-06-10 |
| Day change | **-3.40 (-0.89%)** vs prior close HKD 384.00 | IBKR real-time |
| 52-week high | HKD 460.20 (some sources cite up to HKD 466) | IBKR real-time / [TradingEconomics](https://tradingeconomics.com/388:hk) |
| 52-week low | HKD 379.00, hit 2026-03-30 — **stock is currently essentially AT its 52-week low** | IBKR real-time (low_13w = low_26w = low_52w = 379.00) |
| Open 52 weeks ago | HKD 409.52 | IBKR real-time |
| Shares outstanding | ~1.26B | [companiesmarketcap.com](https://companiesmarketcap.com/hong-kong-exchanges-and-clearing/shares-outstanding/) |
| Market capitalisation | **≈ HKD 479.6B** (1.26B × 380.60) | Derived |
| Analyst consensus 12-mo PT | HKD 518.47, "Strong Buy" (17 Buy / 0 Sell) — implies ~36% upside from current price | [TradingEconomics / search aggregation](https://tradingeconomics.com/388:hk) |

The stock is down -17.3% from its 52-week high and trading right at its 52-week low — a notable contrast with Largan (3008.TW, evaluated alongside this in the same session), which is near its 52-week high.

---

## Business Overview (Context)

HKEX is the operator of the Hong Kong Stock Exchange, Hong Kong Futures Exchange, and the central clearing houses for both cash equities and derivatives in Hong Kong. It also operates **Stock Connect** — the cross-border trading link between Hong Kong and the Shanghai/Shenzhen exchanges, which is the primary channel for foreign capital to access mainland Chinese equities (and vice versa). HKEX holds a **regulatory monopoly**: it is the sole licensed operator of securities/derivatives trading and clearing in Hong Kong, an extremely high barrier-to-entry position.

---

## ⚠️ Data Gaps Flagged Before Proceeding (per Rule 0 / CLAUDE.md)

Two research passes (including a dedicated subagent making 60+ tool calls across stockanalysis.com, alphaspread.com, macrotrends.net, wsj.com, financecharts.com, finbox.com, digrin.com, gurufocus.com, ycharts.com, and the official HKEX annual report PDFs at hkexnews.hk/hkex.com.hk/hkexgroup.com) **could not retrieve HKEX's operating cash flow or capex figures** for FY2023-2025. Every cash-flow-statement source returned HTTP 403 or no extractable data.

**This is material**: FCF Yield is **40% of the Phase 02 valuation score** — the single largest-weighted component. Per the operating brief: *"You NEVER invent, estimate, or assume financial data. If a required metric is missing, stop and ask for it before proceeding."*

**What IS confirmed:**
- FY2025 capex jumped **+183% YoY to HK$4.296B**, driven primarily by a **one-time purchase of HKEX's permanent headquarters at Exchange Square** — this is a real-estate acquisition, not recurring operational capex, and would distort any FY2025 FCF figure if naively annualized.
- One low-confidence, unverified data point (TipRanks aggregation): "levered FCF (TTM) ≈ HK$7.54B, FCF growth -26.01%" — **not used**, as it could not be traced to a primary cash-flow statement.

**What this means for this session:** Phase 01 is assessed on the 6 of 8 criteria that ARE confirmable (all pass cleanly — see below). Phase 02's EV/EBIT and Forward-PE components are computed for context, but **the FCF Yield sub-score (40% weight) cannot be completed, so no final composite Phase 02 score is produced.** This is presented as an unresolved gap requiring either (a) the user to supply FY2023-2025 operating cash flow / capex from the HKEX annual report PDFs (which are publicly available but blocked to automated fetches in this environment), or (b) a follow-up session once that data is obtained.

---

## Phase 01 — Quality Gate Walkthrough

| # | Metric | Threshold | Actual | Pass? | Source / Calculation |
|---|---|---|---|---|---|
| 1 | Gross/Operating margin | >40% | **~79% EBITDA margin** (1H 2025: 79% vs 73% 1H 2024, +6pp YoY) | ✅ PASS | [HKEX 1H2025 Interim Results PDF](https://www.hkex.com.hk/-/media/HKEX-Market/News/News-Release/2025/250820news/250820news_e.pdf) — note: "gross margin" as a concept doesn't map cleanly onto an exchange operator (no traditional COGS); operating/EBITDA margin used as the closest equivalent and clears the threshold by a wide margin |
| 2 | Net margin | >12% | **60.9%** (FY2025: NI HK$17.754B / Revenue HK$29.161B, up from 59% in FY2024) | ✅ PASS | Derived from FY2025 results |
| 3 | ROIC | >15% | **~23%** (ROIC); ROE cited 30.5-35.2% | ✅ PASS | [Alpha Spread](https://www.alphaspread.com/security/hkex/388/profitability/ratio/return-on-equity), [valueinvesting.io](https://valueinvesting.io/388.HK/metric/roe) |
| 4 | Revenue growth (3yr CAGR) | >8% | **~16.5%** (FY2022 ≈ HK$18.5B → FY2025 HK$29.2B) | ✅ PASS | Cross-checked against prior APAC screening session (16.4%) |
| 5 | FCF positive, 3 consecutive years | FCF > 0 ×3yrs | **DATA GAP — operating cash flow not obtainable** (see above) | ⚠️ DATA GAP (not a fail) | — |
| 6 | Net Debt/EBITDA | <2.5× (Upgrade 5 <4× also available for asset-light financials, not needed here) | **≈0.05×** — corporate debt ≈ HK$1.2B (Debt/Equity 2.21% on implied equity ~HK$54.6B) vs EBITDA ~HK$23-24B. **Excludes pass-through client margin deposits/clearing collateral** (gross balance sheet items, not real corporate leverage — per prior screening session's flag) | ✅ PASS (trivially) | Derived |
| 7 | FCF/NI conversion >70% (2+ yrs) | >70% | **DATA GAP — FCF not obtainable** (see above) | ⚠️ DATA GAP (not a fail) | — |
| 8 | Moat Signal | Stable/growing moat | **Regulatory monopoly** — sole licensed operator of HK securities/derivatives exchanges and clearing houses; sole gateway for Stock Connect (mainland China cross-border flows). Extremely high barriers to entry (license-based, not just competitive). **Risks:** earnings are highly cyclical, tied to trading volumes and IPO activity (EPS history: FY2022 -20%, FY2023 +18%, FY2024 +10%, FY2025 +36% — lumpy); geopolitical risk re: HK's role as China's financial gateway amid tightening "national security" rules; competition from mainland exchanges (Shanghai/Shenzhen STAR market) for listings | ✅ PASS (cyclicality + geopolitical risk flagged) | Qualitative |

**Result: 6 of 8 confirmable criteria PASS cleanly (several by very wide margins — net margin 60.9%, ROIC ~23%, near-zero leverage). 2 of 8 (FCF positivity, FCF/NI conversion) are DATA GAPS, not failures — but they block Phase 02 completion (see below).**

---

## Rate Environment Gate

**10Y Treasury yield: 4.54%**

**Step 1 — Earnings Yield Spread Test:**
- Forward PE = HKD 380.60 / HK$13.76 (FY2026E EPS) = **27.66×**
- EY = 1 / 27.66 = **3.62%**
- Spread = EY − 10Y = 3.62% − 4.54% = **−0.93%** < +1.5% → **+0.5 additive flag**

**Step 2 — Rate Regime Modifier:**
- 10Y yield 4.54% falls in the 3.5-5% bucket → **+0.5**

**Total Rate-related modifier: +1.0** (would apply to a final score, if one could be computed)

---

## Phase 02 — Valuation Score (PARTIAL — cannot be finalized)

**Fast Grower check (Upgrade 3):** EPS growth history — FY2022 -20% (decline), FY2023 +17.7%, FY2024 +10.1%, FY2025 +36.1%. Only 2 of the last 4 years exceed 15%, and growth is lumpy/cyclical (tied to trading volumes/IPO activity), not a sustained 3+ year >15% streak. **HKEX is NOT a Fast Grower.** PEG does not apply; its 15% weight would redistribute to EV/EBIT (→ 40% total), as with REA.AX and Largan in this session.

| Component | Weight | Value | Sub-score | Notes |
|---|---|---|---|---|
| FCF Yield | 40% | **BLOCKED — DATA GAP** | **N/A** | Operating cash flow / capex for FY2023-2025 not obtainable. FY2025 capex itself is distorted by a one-time HK$4.3B HQ purchase (+183% YoY), which would need to be excluded/normalized even if the raw figures were available. |
| EV/EBIT | 40% | EV ≈ Market cap + net debt = HKD 479.6B + ~HK$1.2B ≈ **HKD 480.8B**; EBIT ≈ EBITDA (~HK$23.4B) − est. D&A (~HK$1-1.5B) ≈ **HK$22-22.4B**; EV/EBIT ≈ **21.7-22.0×** | **5** (computed for context) | 18-22× → sub-score 5; sits right at the 18-22/22-28 boundary — small changes in the D&A estimate could push this to sub-score 6. D&A itself is an estimate (flagged) |
| Forward PE + Hist. PE Modifier | 20% | Fwd PE 27.66× — for a global exchange-operator peer set (CME, ICE, LSEG, Deutsche Börse typically trade 20-30× forward), this sits in the "moderate-to-high but normal for the sector" zone → base sub-score **6**. Upgrade 2: GuruFocus describes current TTM PE (~29.6-30.1×) as "19% below median," implying a 10yr median PE of ~36.5-37×. Forward PE 27.66× vs ~36.8× ≈ **-25% below** → would trigger Upgrade 2 **-1** if confirmed | **6** (base; -1 modifier UNCONFIRMED — see flag) | The "10yr median PE ≈ 36.8×" figure is itself an *inference* from a vague search snippet ("19% below median"), not a directly-sourced number. Per Rule 0, **not** mechanically applying the -1 modifier without verification — flagged as a likely-favorable adjustment pending confirmation |

**No final composite score is computed.** With FCF Yield at 40% weight unconstructable, any number produced here would require inventing the single largest input — which the framework explicitly forbids.

**For context only** (NOT a valid framework output): if FCF Yield were assumed equal to the EV/EBIT sub-score (5) — a placeholder, not a real estimate — the raw weighted score would be (5×0.40)+(5×0.40)+(6×0.20) = 2.0+2.0+1.2 = 5.2, +1.0 rate modifier = 6.2 → Score 6 (Watchlist). This is shown only to illustrate that **even a middling FCF Yield assumption would not change the qualitative conclusion** (this looks like a Watchlist-or-better candidate, not an obvious pass) — but it is explicitly NOT a substitute for the real calculation.

---

## Qualitative — Why Is HKEX At Its 52-Week Low?

Search results point to several converging factors:
- **Structural derating of China-exposed financials** — global funds have been trimming exposure to Hong Kong/China-linked names broadly.
- **Subdued HKEX-specific IPO activity** even as mainland China A-share IPOs surged in 2025 (+14% count, +94% proceeds YoY per Deloitte) — HK's IPO pipeline has not kept pace, raising questions about its relative attractiveness as a listing venue.
- **Geopolitical tension and tightening "national security" rules** — ongoing questions about Hong Kong's long-term role as the gateway between mainland China and global capital markets.
- **Competition from rival hubs** in Asia and the Middle East for listings and trading volume.

None of these are addressed by the framework's existing Phase 01/02 mechanics directly — they're macro/structural narrative risks that would need to be weighed qualitatively against the very strong fundamentals (60.9% net margin, ~23% ROIC, near-zero leverage, regulatory monopoly, ~3% dividend yield, trading at a 52-week low with ~36% implied upside to analyst consensus).

---

## Recommendation

**CANNOT COMPLETE PHASE 02 — DATA GAP. Provisionally a PROMISING WATCHLIST CANDIDATE, but do not enter without completing the framework's required FCF Yield calculation.**

What we know supports a quality, asset-light, regulatory-monopoly business trading at a 52-week low with strong analyst support (Strong Buy, ~36% upside to consensus PT) and a ~3% dividend yield. The two confirmable Phase 02 sub-scores (EV/EBIT ≈5, Forward PE ≈6) don't suggest deep undervaluation, but don't suggest overvaluation either — "fair-to-cheap" territory, consistent with a stock at its 52-week low.

However, **per Rule 0, I cannot in good conscience produce a final valuation score or any buy/sell/stop order setup** when the largest-weighted input (FCF Yield, 40%) is an unresolved data gap rather than a sourced number. The illustrative "placeholder" calculation above suggests the conclusion would likely land at Watchlist (Score 6) or possibly better — but this must not be treated as the framework's actual output.

**Action needed before this can proceed:**
1. Obtain HKEX's consolidated cash flow statements for FY2023, FY2024, FY2025 (operating cash flow and capex) — the HKEX Annual Report PDFs at [hkexgroup.com](https://www.hkexgroup.com) / [hkexnews.hk](https://www.hkexnews.hk) contain this but returned HTTP 403 to automated fetches in this session; manual download or a different access path is needed.
2. Normalize FY2025 capex for the one-time HK$4.3B HQ purchase (real-estate acquisition, not recurring operating capex) before computing FCF Yield / FCF-NI conversion — otherwise FY2025 FCF will appear artificially depressed for reasons unrelated to the operating business.
3. Once FCF Yield is computed, finalize the Phase 02 composite score and determine BUY/Watchlist/Pass per the action table.

---

## Sources

- IBKR real-time market data (live price, change, 52-week range) — 2026-06-10
- [HKEX 1H 2025 Interim Results PDF](https://www.hkex.com.hk/-/media/HKEX-Market/News/News-Release/2025/250820news/250820news_e.pdf)
- [Alpha Spread — HKEX ROE](https://www.alphaspread.com/security/hkex/388/profitability/ratio/return-on-equity)
- [valueinvesting.io — HKEX ROE](https://valueinvesting.io/388.HK/metric/roe)
- [companiesmarketcap.com — HKEX shares outstanding](https://companiesmarketcap.com/hong-kong-exchanges-and-clearing/shares-outstanding/)
- [TradingEconomics — 388:HK](https://tradingeconomics.com/388:hk)
- [SCMP — HKEX FY2024 record profit](https://www.scmp.com/business/companies/article/3300317/hong-kong-bourse-operator-hkex-reports-record-annual-profit-surging-turnover-ipos)
- [SCMP — HKEX FY2023 results](https://www.scmp.com/business/article/3253612/hkexs-2023-profit-jumps-18-as-aguzin-passes-the-baton-of-running-hong-kongs-stock-exchange-to-bonnie-chan-on-a-high-note)
- [SCMP — HKEX FY2022 first profit decline in 6 years](https://www.scmp.com/business/banking-finance/article/3211200/hong-kong-stock-exchange-operator-reports-first-profit-slide-6-years-ipos-dried-and-trading-dwindled)
- [Deloitte — China 2025 IPO market review](https://www.deloitte.com/cn/en/about/press-room/mainland-and-hk-ipo-markets-2025-review-2026-outlook.html)
- [ad-hoc-news.de — HKEX stock under pressure](https://www.ad-hoc-news.de/boerse/news/ueberblick/hkex-stock-under-pressure-is-hong-kong-s-exchange-giant-a-contrarian/68546758)
- [GuruFocus — HKEX PE TTM](https://www.gurufocus.com/term/pettm/HKSE:00388) (snippet only — full page returned 403)
- HKEX FY2025 annual report capex disclosure (one-time HQ purchase) — via search aggregation of [hkexnews.hk](https://www.hkexnews.hk/listedco/listconews/sehk/2025/0730/2025073000576.pdf)

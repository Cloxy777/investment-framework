# 2026-09-15 — SCREENING: Emerging Markets (EM)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [EM](../framework/screening-coverage-log.md) (China, India, Brazil, Mexico, and other major EM, all sectors). Selected per the rotation rule: oldest "Last screened" date in the matrix (2026-08-25, three weeks prior — see [prior session](2026-08-25-screening-emerging-markets.md)); all other rows (NA-2 09-05, JP 09-01, EU 08-29, NA-1 09-08, APAC-EX-JP 09-12) are more recent.

**Unattended scheduled routine** (fired as the "Monthly Universe Screening Slice" — markets closed on Saturdays, but 2026-09-15 is a Tuesday, not a Saturday; the stored routine prompt's cadence description continues not to match when it actually fires. No user available to paste a TIKR/Koyfin export, so per `screen.md` Step 0 this session goes to a documented fallback.)

**Note on this session's automation prompt — same stale-instruction discrepancy flagged in every EM session since 2026-07-14, recurring again:** the routine's stored instructions referenced an `EODHD_API_KEY`/"Path A" automated screener and a monthly cadence. Both are outdated: EODHD was deliberately removed from this framework on 2026-06-19 (see [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)) — the committed `EODHD_API_KEY` was flagged there as a **compromised credential, not to be reused without rotation** — and `framework/automation-schedule.md` Routine 4 has since been retitled "Twice-Weekly Universe Screening Slice" (Tuesday + Saturday, 14:00 UTC). This session followed the current, authoritative `.claude/commands/screen.md` and did **not** touch the `EODHD_API_KEY` env var.

**Major sourcing change this round — `yfinance`/direct Yahoo access is reachable again**, for the first time since it went down on 2026-07-07 (every EM round since 07-14 documented the same `curl_cffi` SSL connection-reset failure). This changes the primary sourcing methodology for this session — see below.

---

## Sourcing methodology this round

`yfinance` was re-tested at the start of this session and worked cleanly for all 21 candidates (income statement, cash flow, balance sheet, live price). Two real data-integrity issues surfaced while building the quantitative table, both handled by cross-checking against `stockanalysis.com` rather than trusting either source blindly (CLAUDE.md Rule 0 — never invent or silently pick a number when sources conflict):

1. **Currency mismatch on price-dependent ratios.** For every ADR/dual-listed name in this pool (Tencent, ANTA, WuXi Biologics — HKD-quoted with CNY-reporting financials; NetEase, Trip.com, PDD, Full Truck Alliance — USD-quoted with CNY-reporting financials; XP Inc — USD-quoted with BRL-reporting financials), `yfinance`'s raw market cap is in the trading currency while its income statement/balance sheet are in the reporting currency. Combining them unconverted silently corrupts EV/EBIT, FCF yield, and Net Debt/EBITDA (e.g. an uncorrected pull put Tencent's EV/EBIT at 14.45x purely from this mismatch). Fixed by pulling live FX rates (`HKD=X`, `CNY=X`, `BRL=X` via `yfinance`) and converting market cap into the financial-statement currency before computing any ratio.
2. **`yfinance`'s derived "EBIT" field is unreliable for names with large equity-method/investment income** (demonstrated concretely on Trip.com: `yfinance`-derived ROIC came out at 25.82% and EV/EBIT at 3.16x, vs. `stockanalysis.com`'s live 10.87% / 7.51x — a ~2.5x EBIT discrepancy, most likely `yfinance` folding "Earnings From Equity Interest" into EBIT). Given this, **ROIC and EV/EBIT for every candidate below are taken from `stockanalysis.com`'s live "Current" figures**, not recomputed from `yfinance`'s EBIT line. Gross margin, net margin, revenue 3yr CAGR, and the FCF-positive-3-years check are straightforward income-statement/cash-flow line items that cross-checked cleanly against `stockanalysis.com` (e.g. Tencent's GM/NM/RevCAGR matched to within 0.05pp) and are taken from `yfinance` directly. Net Debt/EBITDA and FCF yield use the FX-corrected `yfinance` calculation, following the framework's documented FCF/Market-Cap definition exactly; where `stockanalysis.com`'s own live FCF yield diverged meaningfully (Kweichow Moutai: 3.67% mine vs. 7.31% theirs — the underlying FCF figure or basis appears to differ), the framework-formula-consistent number is used and the discrepancy is flagged rather than picking whichever number passes.

This is a more rigorous (if more laborious) sourcing process than prior EM rounds' single-source `stockanalysis.com` WebFetch approach — worth carrying into future rounds as the default methodology while `yfinance` stays reachable.

---

## Step 1 — Structural triage

**Candidate pool: the 19 names from the 2026-08-25 session, re-verified, plus 2 new names** added this pass to broaden coverage — one Chinese asset-light logistics-platform name and one Brazilian asset-light financial-services name, both segments not yet represented in this slice's pool:

| Ticker | Company | Country | Sector |
|---|---|---|---|
| 0700.HK / TCEHY | Tencent Holdings | China | Internet/gaming/social/fintech |
| PDD | PDD Holdings (Pinduoduo/Temu) | China | E-commerce |
| 600519.SH | Kweichow Moutai | China | Premium liquor (consumer staples) |
| 2020.HK | ANTA Sports Products | China | Sportswear/athletic apparel |
| NTES | NetEase | China | Gaming |
| TCOM | Trip.com Group | China | Online travel agency |
| 2269.HK | WuXi Biologics | China | Biologics CRO/CDMO |
| 603605.SH | Proya Cosmetics | China | Domestic cosmetics/skincare brand |
| INFY | Infosys | India | IT services |
| TCS.NS | Tata Consultancy Services | India | IT services |
| ASIANPAINT.NS | Asian Paints | India | Paints/consumer |
| PIDILITIND.NS | Pidilite Industries | India | Specialty chemicals/adhesives |
| DIVISLAB.NS | Divi's Laboratories | India | Pharma API/CRAMS |
| ITC.NS | ITC Limited | India | Tobacco/FMCG conglomerate |
| NAUKRI.NS | Info Edge (India) | India | Internet classifieds (Naukri.com) |
| PERSISTENT.NS | Persistent Systems | India | IT services |
| MELI | MercadoLibre | LatAm | E-commerce/fintech |
| WEGE3.SA | WEG S.A. | Brazil | Industrial motors/automation |
| B3SA3.SA | B3 S.A. | Brazil | Exchange/clearing |
| XP | XP Inc | Brazil | Digital brokerage/wealth platform *(new this pass)* |
| YMM | Full Truck Alliance | China | Digital freight-matching platform *(new this pass)* |

**Structurally excluded without a fresh quantitative pull** (unchanged from every prior EM session — categorical, business-model grounds):

| Eliminated | Why |
|---|---|
| HDFC Bank, ICICI Bank, Itaú Unibanco, Banco Bradesco, Grupo Financiero Banorte | Banks — regulated balance-sheet businesses |
| Saudi Aramco, Petrobras, Vale, PetroChina, Sinopec, China Shenhua | Commodity cyclicals |
| Reliance Industries | Diversified conglomerate — no segment clears the bar |
| Alibaba, Meituan, JD.com | Multi-year margin compression from competition + regulatory crackdown |
| China Mobile, China Telecom, América Móvil, Bharti Airtel | Regulated, capital-intensive telecom |
| GAP/OMAB/ASUR (Mexican airports) | Asset-heavy regulated infrastructure |
| Walmex, Raia Drogasil, Magazine Luiza, Lojas Renner, Titan Company | Thin-margin retail/jewelry |
| FEMSA, Ambev | Beverage bottling — structurally sub-40% gross margins |
| Naspers/Prosus | Holding company (NAV-discount dynamics) |
| Yandex | Russia-domiciled — sanctions/delisting complications |
| TSMC, MediaTek, Samsung, SK Hynix, Hon Hai, Coupang, Sea Ltd/Grab | Belong to the **APAC-EX-JP** slice, not EM |
| Yum China | Structurally thin gross margins |

**Process note this round:** XP Inc (below) cleared this triage step but turned out, on inspection, to have the same structural mismatch as a bank/financial-services firm — its "debt" is largely customer-lending/margin-financing, its net margin is unusually inflated, and `stockanalysis.com` doesn't even publish an EV/EBIT for it. It should arguably have been triaged out here rather than run through Step 2. Flagged so future rounds screen candidate sector fit (financial-services/brokerage business models) before running the full quantitative gate, not after.

---

## Step 2 — Full Phase 01 quantitative gate

Filters ([valuation-scoring.md](../framework/valuation-scoring.md)): Gross margin >40% · Net margin >12% · ROIC >15% · Revenue growth >8% (3yr CAGR) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x

**Sources:** `yfinance` (GM, NM, Rev 3yr CAGR, FCF-3yr-positive, Net Debt/EBITDA, FCF yield — FX-corrected) cross-checked against `stockanalysis.com` (ROIC, EV/EBIT — authoritative for these two, per the sourcing note above).

| Ticker | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF 3yr+ | Net D/EBITDA | FCF yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **Tencent (0700.HK)** | 56.21% ✅ | 29.91% ✅ | 18.27% ✅ | 10.67% ✅ | ✅ | −0.11x ✅ | 4.92% ✅ | **12.99x** ✅ | **PASS — 8/8 clean.** EV/EBIT resolved from 20.10x (08-25 miss) to 12.99x — real, cross-verified with `yfinance`'s independent 11.48x |
| **PDD Holdings (PDD)** | 56.28% ✅ | 22.66% ✅ | 22.75%* ✅ | 49.00% ✅ | ✅ | −3.40x ✅ | 14.60% ✅ | **3.21x** ✅ | **PASS — 8/8.** Dramatically cheaper than 08-25 (7.73x→3.21x EV/EBIT, 9.40%→14.60% FCF yield) — confirmed a real analyst-driven sell-off, not a data artifact (see Step 3) |
| Kweichow Moutai (600519.SH) | 91.34% ✅ | 47.85% ✅ | 37.31% ✅ | 10.49% ✅ | ✅ | −0.44x ✅ | **3.67%** ❌ | 14.15x ✅ | **FAIL — FCF yield only** (3.67% vs >4%; `stockanalysis.com`'s live figure of 7.31% diverges materially — flagged, not used, since it's inconsistent with the framework's FCF/MarketCap definition applied to the same sourced FCF figure used every prior round) |
| **ANTA Sports (2020.HK)** | 62.00% ✅ | 16.94% ✅ | 23.30% ✅ | 14.35% ✅ | ✅ | −0.23x ✅ | 11.44% ✅ | 7.80x ✅ | **PASS — 8/8 clean**, continues qualified |
| NetEase (NTES) | 64.29% ✅ | 29.98% ✅ | 368.26%† | **5.29%** ❌ | ✅ | −4.09x ✅ | 9.90% ✅ | 8.77x ✅ | **FAIL — Rev 3yr CAGR only** (unchanged 4th straight round) |
| Trip.com (TCOM) | 80.58% ✅ | 53.35% ✅ | **10.87%** ❌ | 46.04% ✅‡ | ✅ | −0.99x ✅ | 8.19% ✅ | 7.51x ✅ | **FAIL — ROIC only** (continuing to hover just under 15%: 7.94%→10.91%→11.23%→10.87%); EV/EBIT improved sharply from 18.12x |
| WuXi Biologics (2269.HK) | 45.98% ✅ | 22.53% ✅ | **13.88%** ❌ | 12.59% ✅ | ✅ | −1.43x ✅ | **1.51%** ❌ | **22.33x** ❌ | **FAIL — ROIC + FCF yield + EV/EBIT** (worse than 08-25's 2-filter miss; EV/EBIT newly failing, up from 17.08x) |
| Proya Cosmetics (603605.SH) | 73.26% ✅ | 14.13% ✅ | 57.81% ✅ | 18.40% ✅ | ✅ | −2.06x ✅ | 7.53% ✅ | 11.63x ✅ | **PASS — 8/8 quantitatively.** ⚠️ **Qualitative pass this round is a FAIL, not a flag — see Step 3** |
| Infosys (INFY) | **30.16%** ❌ | 16.44% ✅ | 41.69% ✅ | **3.44%** ❌ | ✅ | −0.55x ✅ | 8.36% ✅ | 10.49x ✅ | **FAIL — Gross margin + Rev 3yr CAGR** |
| TCS (TCS.NS) | 45.10% ✅ | 18.43% ✅ | 66.38% ✅ | **5.80%** ❌ | ✅ | −0.42x ✅ | 6.05% ✅ | 11.12x ✅ | **FAIL — Rev 3yr CAGR only** (unchanged) |
| Asian Paints (ASIANPAINT.NS) | 43.39% ✅ | 12.17% ✅ | 25.49% ✅ | **1.10%** ❌ | ✅ | −0.63x ✅ | **2.37%** ❌ | **37.66x** ❌ | **FAIL — Rev CAGR, FCF yield, EV/EBIT** |
| Pidilite Industries (PIDILITIND.NS) | 54.90% ✅ | 16.83% ✅ | 34.88% ✅ | **7.38%** ❌ | ✅ | −1.01x ✅ | **1.44%** ❌ | **44.52x** ❌ | **FAIL — Rev CAGR, FCF yield, EV/EBIT** |
| Divi's Laboratories (DIVISLAB.NS) | 59.14% ✅ | 24.51% ✅ | 19.67% ✅ | 10.98% ✅ | ✅ (thin) | −0.83x ✅ | **0.09%** ❌ | **69.98x** ❌ | **FAIL — FCF yield, EV/EBIT only** (quality metrics all pass, extreme valuation, unchanged) |
| ITC Limited (ITC.NS) | 57.81% ✅ | 26.45% ✅ | 35.59% ✅ | **3.65%** ❌ | ✅ | −0.71x ✅ | 5.00% ✅ | 12.48x ✅ | **FAIL — Rev 3yr CAGR only** (unchanged) |
| Info Edge (NAUKRI.NS) | 59.00% ✅ | 44.14%◊ ✅ | **2.56%** ❌ | 11.88% ✅ | ✅ | −1.91x ✅ | **1.24%** ❌ | **69.89x** ❌ | **FAIL — ROIC, FCF yield, EV/EBIT** |
| Persistent Systems (PERSISTENT.NS) | **28.05%** ❌ | 12.65% ✅ (narrow) | 29.80% ✅ | 20.88% ✅ | ✅ | −0.54x ✅ | **1.46%** ❌ | **31.60x** ❌ | **FAIL — Gross margin, FCF yield, EV/EBIT** |
| MercadoLibre (MELI) | 44.50% ✅ | **6.91%** ❌ | **14.20%** ❌ | 38.91% ✅ | ✅ | 1.54x ✅ | 12.88% ✅ | **35.71x** ❌ | **FAIL — Net margin, ROIC, EV/EBIT.** ROIC is a **newly failing** filter this round (28.19% → 14.20%, `stockanalysis.com`'s own live figure) — real, sourced deterioration, not a data artifact; flagged for the next rescore trigger |
| WEG S.A. (WEGE3.SA) | **33.53%** ❌ | 15.63% ✅ | 38.28% ✅ | 10.91% ✅ | ✅ (declining) | −0.20x ✅ | **1.94%** ❌ | **27.26x** ❌ | **FAIL — Gross margin, FCF yield, EV/EBIT** |
| B3 S.A. (B3SA3.SA) | 73.51% ✅ | 45.55% ✅ | 26.47% ✅ | **3.47%** ❌ | ✅ | −0.02x ✅ | 6.75% ✅ | 12.19x ✅ | **FAIL — Rev 3yr CAGR only** (unchanged) |
| XP Inc (XP) *(new)* | **26.00%** ❌ | 64.89%◊ | **2.80%** ❌ | 10.28% ✅ | ✅ | **4.88x** ❌ | 25.85%◊ | N/A◊ | **FAIL — Gross margin, ROIC, Net Debt/EBITDA at minimum.** Financial-services/brokerage capital structure is a poor structural fit for this filter set (see Step 1 process note) — `stockanalysis.com` doesn't even publish EV/EBIT for it |
| **Full Truck Alliance (YMM)** *(new)* | 63.02% ✅ | 35.29%◊ ✅ | 16.66% ✅ | 22.87% ✅ | ✅ | −4.02x ✅ | 11.58% ✅ | 7.89x ✅ | **PASS — 8/8 clean quantitatively.** ⚠️ Net margin is meaningfully inflated by interest income on a large cash pile, not pure take-rate economics — see Step 3 |

*PDD's ROIC is not meaningful (net-cash-position denominator distortion) — ROE (22.75%) used as proxy, consistent with the prior round's ROCE (22.40%) proxy convention.
†NetEase's ROIC (368.26% per `stockanalysis.com`, 691.73% per `yfinance`) is a net-cash-position denominator artifact, not relied on for the verdict — ROE (20.37%) is the meaningful figure, and the verdict is driven by revenue CAGR regardless.
‡Trip.com's Rev 3yr CAGR uses FY2022 (a COVID-depressed base year) — real and sourced but not representative of a normalized run rate; doesn't change the FAIL verdict (blocked on ROIC regardless).
◊See Step 4 (data gaps) — Info Edge's net margin is inflated by non-operating stake gains; XP Inc's net margin/FCF yield look anomalously high for a brokerage and EV/EBIT isn't published; Full Truck Alliance's net margin is inflated by treasury income (quantified in Step 3).

---

## ✅ Qualified Quality List — 5 names clear the quantitative gate (up from 3 last round)

**Tencent Holdings (0700.HK)** — new this round, a flip from FAIL (EV/EBIT-only miss at 20.10x three weeks ago, now 12.99x — a real, cross-verified move, not a data artifact).
**PDD Holdings (PDD)** and **ANTA Sports Products (2020.HK)** — both carried forward, both clean.
**Proya Cosmetics (603605.SH)** — carried forward, clean quant, but **qualitative pass has been upgraded from "flag" to an outright FAIL this round** (see Step 3) — do not treat as investable off this list.
**Full Truck Alliance (YMM)** — new candidate, clean quant pass with a qualitative flag on net-margin quality (see Step 3).

### Near-miss watchlist

- **Kweichow Moutai (600519.SH)** — fails only FCF yield (3.67% vs >4%), essentially unchanged from 08-25's 3.39% miss; note the FCF-yield data-source discrepancy flagged above.
- **Trip.com (TCOM)** — fails only ROIC (10.87% vs >15%), roughly flat across four rounds (7.94%→10.91%→11.23%→10.87%); EV/EBIT has improved sharply (18.12x→7.51x).
- **NetEase (NTES)** — fails only Rev 3yr CAGR (5.29% vs >8%), unchanged for the 4th straight round.
- **Divi's Laboratories (DIVISLAB.NS)** — clears every quality metric, blocked purely by extreme valuation (FCF yield 0.09%, EV/EBIT 69.98x), unchanged read.
- **TCS, ITC, B3** — each a clean single-filter Rev CAGR miss, unchanged from last pass.
- **MercadoLibre (MELI)** — now a 3-filter miss (was 2 last round) — **ROIC newly failing** (28.19%→14.20%), worth tracking as a real deterioration signal rather than assuming it's noise.

---

## Step 3 — Qualitative pass (Tencent, PDD, ANTA, Proya, Full Truck Alliance)

Run as 5 parallel research agents via `WebSearch`, in batches of 2 concurrent per the batch-processing policy in [new-position.md](../.claude/commands/new-position.md) (batch 1: Tencent + PDD; batch 2: ANTA + Proya; batch 3: Full Truck Alliance solo).

### Tencent Holdings (0700.HK) — new qualifier, first full pass since re-qualifying

1. **Why are margins high?** Structural, not cyclical — gross margin expanded from 47.5% to 57.8% over three years on a mix shift toward higher-margin games, AI-improved ad targeting, and maturing fintech/cloud economics, underpinned by WeChat's 1.4B-user network-effect moat giving near-zero marginal user-acquisition cost.
2. **What would it take to compete?** Very hard — replicating a regulator-approved super-app with 1.4B MAU, a games-publishing license portfolio clearing China's NPPA approval gate, and now AI-infrastructure scale (capex +65-176% YoY quarterly, RMB185-250B forecast 2026-28).
3. **Capital allocation (5-10yr):** A disciplined shift from "invest everywhere" (Meituan, JD, Pinduoduo stakes) to divestment + shareholder returns — cumulative buybacks of HK$187.6bn by Dec 2024, a record HK$112bn in 2024 alone, dividends up 5yr CAGR +28.7%. A March 2026 pivot toward redirecting capital from buybacks to AI capex was read negatively by the market (stock −7% that day) — a recent regime change worth monitoring.
4. **Where's growth coming from (3-5yr)?** Gaming (~10% YoY domestic), advertising (+22% YoY on AI targeting, Video Accounts ad-load headroom), cloud/AI services (accelerating to low-20s% growth), and WeChat AI Agent monetization of the 4M+ mini-program ecosystem (targeting Q3 2026 full deployment).
5. **Best bear case:** ByteDance/Douyin's usage-time and ad-share gains are real, measurable erosion of Tencent's core distribution advantage (Douyin surpassed WeChat on total usage time in July 2026); AI-capex could outpace monetization; China's incoming AI regulatory framework and continued gaming anti-addiction scrutiny; the Jan 2025 US DoD Section 1260 "Chinese Military Companies" list addition is a reputational/commercial overhang.
6. **Disruption vector:** The most important flag — AI agents work by removing the need to know which app holds which service, the opposite logic of a walled-garden super-app. Tencent's countermove (building the agent layer inside WeChat itself, A2A deals with major phone-makers) looks credible and the market rewarded the announcement (+10.5%, +$53B market cap), but this is an evolving, unresolved bet, not a settled moat.

**Conclusion: Pass-with-flags.** Clean quant screen; qualitative underpinnings support proceeding, but ByteDance/ad-share erosion, the buyback-to-capex pivot, and the AI-agent disruption vector should be carried as explicit monitoring triggers.
**Recommendation:** `/new-position Tencent` — proceed, with those three flags named for tracking.

### PDD Holdings (PDD) — refresh

**What changed since 08-25:** the multiple compression (7.73x→3.21x EV/EBIT) is a genuine, analyst-confirmed sell-off, not a data artifact — Arete Research downgraded PDD to Hold on 2026-09-07/08 (target cut $169→$130) citing "core ad deceleration and 1P pivot" risk; JPMorgan cut its target $110→$95 on 2026-09-10 on margin concerns; a director sold his entire direct ADS position on 2026-09-03; Q3 2026 consensus calls for EPS −15.5% YoY despite ~16% revenue growth; the stock is down ~34% YTD.

1. **Why are margins high?** Historically genuine — a lean commission/ad-take-rate model with minimal fulfillment risk. But that advantage is being spent down deliberately via the RMB100bn, 3-year Xin Pin Mu first-party-brand pivot, a structurally lower-margin model by design.
2. **What would it take to compete?** Deep pockets and years of sustained losses — exactly what Alibaba, JD, and Douyin are now doing; PDD's domestic GMV share (~23.1%) is being actively contested. Internationally, Temu's low-landed-cost moat was structurally undermined by the US/EU de minimis changes — a regulatory tailwind that reversed.
3. **Capital allocation:** Heavy reinvestment, ~$63-67bn net cash, zero dividend/buyback. Xin Pin Mu is the largest discretionary reinvestment commitment in company history, made as two of three growth legs are decelerating — a high-conviction, high-risk bet.
4. **Where's growth coming from (3-5yr)?** All three vectors (domestic GMV/ad growth, Temu international, Xin Pin Mu) are currently under visible strain, not accelerating.
5. **Best bear case:** A three-front war — domestic deceleration under regulatory "anti-involution" pressure and well-funded competition, Temu's international economics permanently impaired by the end of de minimis, and a self-funded pivot to a lower-margin model with no proof of concept yet. Two independent sell-side shops cut rating/target in the same week on the same margin-visibility thesis.
6. **Disruption vector:** Not a new technology — regulatory and competitive convergence happening now (China's new algorithmic-pricing rules effective Apr 2026 target the exact mechanics PDD's edge was built on; the end of de minimis is a realized, not hypothetical, disruption of Temu's delivery model).

**Conclusion: Pass-with-flags.** Still clears the quant gate with elite margins and a fortress balance sheet, but the qualitative picture has deteriorated, not stabilized, since 08-25 — the cheapness is explainable by fundamentals, not just sentiment.
**Recommendation:** Keep on the Qualified Quality List; do not treat the multiple compression alone as a buy signal. Hold at current sizing (or below) pending Q3 2026 earnings — continued monitoring, not a documented buying trigger yet.

### ANTA Sports Products (2020.HK) — refresh

1. **Why are margins high?** H1 2026 group gross margin rose to 63.9%, operating margin to 27.0% — but increasingly a premiumization/multi-brand-mix story: the "other brands" segment (Arc'teryx/Descente) grew 44.2% revenue at a 28.7%+ margin, while the flagship ANTA brand grew only 4.8% and its own margin fell 0.8pp.
2. **What would it take to compete?** Very hard — a portfolio of genuinely premium technical brands built via multi-year M&A (2019 €4.6bn Amer Sports LBO, 2009 FILA-China deal) plus #1 China distribution scale (23% share vs. Nike 20.7%). The pending Puma stake (29.06%, China-antitrust-cleared Sept 2026) extends this playbook.
3. **Capital allocation:** Disciplined and value-accretive M&A (Amer Sports went loss-making→profitable→NYSE IPO) plus a stable dividend since 2011 and an HKD10bn buyback program.
4. **Where's growth coming from (3-5yr)?** Increasingly the premium/international portfolio (Arc'teryx China +40% H1 2026, FY guidance raised to 24%) rather than the core brand, which management confirms is exiting hyper-growth.
5. **Best bear case:** Real single-brand concentration risk — the flagship brand is stalling while group growth/margin expansion depends on Arc'teryx, which is itself normalizing off a hyper-growth base. The $1.8bn Puma commitment is into a genuinely troubled brand with its own turnaround risk.
6. **Disruption vector:** Low probability — the moat is physical distribution scale and brand-portfolio breadth, not a channel a new technology trivially disintermediates.

**Conclusion: Pass-with-flags.** Moat intact and arguably widening via Puma, but real, growing dependency on Arc'teryx to carry group numbers is a concentration risk to flag for scoring, not a screening failure.
**Recommendation:** `/new-position ANTA Sports` — proceed; flag core-brand deceleration and Arc'teryx growth-normalization as watch items; monitor the Puma deal close (expected end-2026).

### Proya Cosmetics (603605.SH) — refresh, ⚠️ escalated to FAIL

The prior session (08-25) found Proya's FY2025 decline and Q1 2026 continuation as a flag, not a disqualifier. This refresh found the deterioration has **continued and deepened through H1 2026**, plus three new red flags.

1. **Why are margins high?** 73-74% gross margin from an asset-light OEM/ODM model plus patented-actives positioning, but the gap to net margin is now dominated by platform traffic-buying: sales/marketing expense hit a **record ~53% of revenue** in H1 2026. Looks more like a lucky 2020-2023 cycle than durable pricing power.
2. **What would it take to compete?** Not very hard — manufacturing is outsourced, ingredient patents are narrow, and the real contested resource (Douyin/Tmall livestream buying power) has proven highly contestable within a single platform cycle (KANS overtook Proya on Douyin 2023-24, then itself lost its lead to a resurgent L'Oréal in 2026).
3. **Capital allocation:** The Flower Knows step-acquisition (May 2026) generated a one-time RMB445m fair-value gain that made H1 2026 headline net profit look up 46.3% YoY, while **core net profit ex non-recurring items actually fell 13.8%** — flattering the P&L via accounting mechanics rather than operating improvement. The Hong Kong listing (filed Oct 2025) remains unexecuted 11 months on, with CSRC queries still unresolved as of July 2026.
4. **Where's growth coming from (3-5yr)?** Color cosmetics (Caitang, Flower Knows) and international expansion (still ~1.3-3% of revenue) — none has offset the flagship brand's decline, which is continuing (-10.4% FY2025, -7.2% H1 2026).
5. **Best bear case:** Multi-quarter deterioration, not one-off — FY2025 first-ever decline, Q3 2025 the worst quarter since listing (revenue -11.63%), Q1 2026 and H1 2026 both still negative on a core basis. Plus a quality-of-earnings problem (the M&A-driven profit headline), a stalled/regulator-scrutinized HK listing, and a new governance overhang: ~RMB2bn (~15% of the company) of co-founder Fang Yuyou's shares frozen in an unrelated family litigation.
6. **Disruption vector:** Two live vectors — the existing "moat" sits on a platform substrate that reshuffles leadership every 1-2 years, and China's AI-driven personalized-skincare segment (already commercialized by rivals) targets Proya's exact hero-SKU value proposition with no comparable AI-native response from Proya yet.

**Conclusion: FAIL on qualitative grounds**, upgraded from last round's "not a clean pass" flag — the picture has worsened, not stabilized.
**Recommendation:** Do not add to the Qualified Quality List or initiate a new position; do not run `/new-position Proya` off the trailing quant numbers. Treat as a trim/watch candidate if ever held, pending H2 2026 results and the HK listing outcome.

### Full Truck Alliance (YMM) — new candidate, first full pass

1. **Why are margins high?** Two things stacked: real operating leverage from a now-~complete commission-model rollout (94.7% of eligible cities, up from 58% in Q3 2023; non-GAAP operating margin hit a record 46.7% in Q2 2026) — but a meaningful chunk of the headline 35.29% net margin is **treasury/interest income** on a RMB33.4bn cash pile, not core take-rate economics (FY2025 operating income RMB4,146M vs. net income RMB4,408M).
2. **What would it take to compete?** The 2017 Yunmanman/Huochebang merger created hard-to-replicate two-sided liquidity at scale (4.78M active truckers), but the moat is narrower than it looks — truckers multi-home easily across apps, Huolala is a real competitor, and the bigger structural threat is Alibaba/JD/Meituan's logistics arms internalizing freight matching.
3. **Capital allocation:** Conservative to passive 2021-2023 (cash hoarding, no dividends), a first $300M buyback in March 2024, then a formal shareholder-return policy adopted January 2026 (≥50% of prior-year non-GAAP net income annually). Improving discipline; the years of hoarding before formalizing are a mild governance yellow flag.
4. **Where's growth coming from (3-5yr)?** The easy monetization-conversion lever (commission rollout) is largely spent; forward growth depends on fulfillment-rate improvement (record 47%, still headroom) and value-added services — a natural deceleration point.
5. **Best bear case:** The net margin overstates core economics; headline revenue growth (+4.4% YoY) is decelerating and partly optical versus transaction revenue (+33% YoY); April 2026 China-wide gig-worker labor rules (full compliance due 2027) create a credible, dated cost/margin risk specific to platform-gig models.
6. **Disruption vector:** The most credible medium-term threat — China's autonomous-trucking buildout (assisted-driving trucks logging >1M km/day industry-wide) could displace the fragmented independent-owner-operator base that FTA's matching moat depends on, in favor of direct fleet-to-shipper contracts that bypass the marketplace.

**Conclusion: Pass-with-flags.** A real, scale-driven marketplace with improving capital discipline, but the headline net margin needs an explicit core-vs-treasury-income adjustment, and the labor-reform and autonomous-trucking vectors are genuine multi-year watch items.
**Recommendation:** `/new-position Full Truck Alliance` — proceed to Phase 02, but apply an explicit margin-quality adjustment and flag the 2027 labor-reform deadline and autonomous-trucking penetration for the next rescore.

---

## Step 4 — Data gaps (CLAUDE.md Rule 0 — none estimated)

- **Kweichow Moutai FCF yield discrepancy**: `stockanalysis.com`'s live figure (7.31%) diverges materially from the framework-formula-consistent calculation (3.67%, FCF/MarketCap using the same sourced FY2025 FCF figure used every prior round). Not reconciled — flagged as an open data-source discrepancy for a future session to resolve against Moutai's primary annual report cash-flow statement.
- **Trip.com EBIT/ROIC discrepancy**: `yfinance`'s derived EBIT produces a ROIC of 25.82% and EV/EBIT of 3.16x, materially different from `stockanalysis.com`'s live 10.87%/7.51x. `stockanalysis.com`'s figures were used (closer to the prior round's own number, and `yfinance`'s "EBIT" line appears to include equity-method/investment earnings for this name) — flagged as a `yfinance`-specific data-quality issue to watch for on any EM name with large equity-method investees.
- **PDD Holdings and NetEase ROIC**: both show extreme, non-meaningful ROIC values (PDD: undefined/negative invested capital; NetEase: 368.26-691.73%) due to net-cash-position denominator effects — ROE used as the proxy for both, consistent with the framework's "ROE/ROIC/ROCE — whichever is meaningful" allowance.
- **Info Edge (Naukri) net margin**: inflated by non-operating stake-sale/investment gains, flagged rather than adjusted — doesn't change the FAIL verdict (already fails on ROIC, FCF yield, and EV/EBIT independently).
- **XP Inc data fit**: net margin (64.89%) and FCF yield (25.85%) both look anomalously high for a brokerage business and were not independently decomposed into core-vs-non-operating this session; `stockanalysis.com` does not publish an EV/EBIT for XP at all (likely because its debt structure, mostly customer-lending/margin-financing, doesn't map cleanly to the metric) — flagged as a structural-fit gap, not resolved by estimation. The FAIL verdict doesn't depend on resolving it (already fails Gross Margin, ROIC, and Net Debt/EBITDA independently).
- **Full Truck Alliance net margin**: quantified and explained in Step 3 (treasury income on a RMB33.4bn cash pile), not merely flagged — this is a resolved data-quality finding, not an open gap.
- **Currency-conversion basis**: documented in the sourcing-methodology note above; all price-dependent ratios for currency-mismatched tickers (Tencent, ANTA, WuXi Biologics, NetEase, Trip.com, PDD, Full Truck Alliance, XP Inc) use live FX rates fetched the same session (`HKD=X`, `CNY=X`, `BRL=X` via `yfinance`), not a stale or estimated rate.

---

## Next steps

- `/new-position Tencent` (0700.HK) — proceed; carry ByteDance/ad-share erosion, the buyback-to-capex pivot, and the AI-agent disruption vector as monitoring triggers.
- `/new-position ANTA Sports` (2020.HK) — proceed; flag core-brand deceleration/Arc'teryx normalization; monitor the Puma deal close (expected end-2026).
- `/new-position Full Truck Alliance` (YMM) — proceed with an explicit margin-quality (core vs. treasury-income) adjustment; flag the 2027 labor-reform deadline and autonomous-trucking penetration.
- **PDD (PDD)** — keep qualified but do not treat the cheap multiple as a buy signal; hold current sizing pending Q3 2026 earnings.
- **Proya Cosmetics (603605.SH)** — do **not** run `/new-position` on this name; qualitative FAIL, deterioration continuing through H1 2026, plus new governance/listing-status red flags.
- **MercadoLibre (MELI)** — ROIC newly failing (28.19%→14.20%) is a real, sourced change worth a closer look at the next EM pass, not assumed noise.
- **Kweichow Moutai FCF-yield discrepancy** — resolve against the primary annual report at the next EM pass.
- Process note: screen candidate sector/business-model fit (e.g., financial-services/brokerage capital structures) at Step 1 before running the full Phase 01 quantitative gate — XP Inc should have been triaged out, not run through Step 2, given the parallel to the bank exclusion category.
- Coverage log updated below — next "oldest Last screened" slice will be **EU**, last screened 2026-08-29.

---

## Glossary

- **CAGR (Compound Annual Growth Rate)** — the smoothed annual growth rate that would take a starting value to an ending value over N years, accounting for compounding.
- **ROE (Return on Equity)** — net income as a percentage of shareholders' equity.
- **ROIC (Return on Invested Capital)** — net operating profit after tax divided by total invested capital (debt + equity − cash); a cleaner profitability measure than ROE for companies with unusual capital structures or large cash balances.
- **ROCE (Return on Capital Employed)** — a close cousin of ROIC, used as a proxy where ROIC isn't meaningful or published.
- **FCF (Free Cash Flow)** — operating cash flow minus capital expenditure.
- **FCF Yield** — FCF divided by market cap; how much free cash the business throws off relative to what you're paying for it.
- **EV/EBIT (Enterprise Value / Earnings Before Interest & Tax)** — a capital-structure-neutral valuation multiple; lower means cheaper relative to operating earnings.
- **Net Debt/EBITDA** — a leverage ratio; negative means net cash (more cash than debt).
- **Gross margin** — (revenue − cost of goods sold) ÷ revenue.
- **Net margin** — net income ÷ revenue.
- **GTV (Gross Transaction Value)** — total value of transactions processed through a marketplace platform, before the platform's commission.
- **Take rate** — the percentage (commission) a marketplace keeps from the gross value of each transaction it facilitates.
- **VIE (Variable Interest Entity)** — a legal structure many Chinese companies use to give foreign (e.g. US-listed) shareholders economic exposure without direct equity ownership, due to Chinese foreign-ownership restrictions; carries structural legal/enforceability risk.
- **MAU / DAU (Monthly / Daily Active Users)** — count of unique users engaging with a platform in that window.
- **De minimis** — a customs threshold below which imported parcels enter duty-free; its removal for US/EU imports raised landed costs for low-value China-origin shipments (core to Temu's model).
- **1P (first-party) model** — a retail model where the platform itself owns/sources and sells inventory (vs. 3P/third-party marketplace).
- **Moat** — a durable competitive advantage that protects a business's profits from competitors over time.
- **A2A (Agent-to-Agent)** — a protocol/arrangement letting one AI assistant hand off tasks to another.
- **Section 1260 / CMC List** — the U.S. Department of Defense's list of "Chinese Military Companies," restricting U.S. federal procurement from listed firms but not a broad trade sanction.
- **SAMR** — State Administration for Market Regulation, China's chief antitrust/market regulator.
- **Anti-involution campaign** — Chinese regulators' term for cracking down on self-destructive price wars among platforms.
- **L4 autonomous driving** — SAE Level 4 automation: a vehicle can drive itself in defined conditions/routes without a human driver, but not unconditionally.
- **Data gap** — a required metric that could not be sourced, or a sourced figure with an internal-consistency problem, flagged rather than estimated or silently substituted (CLAUDE.md Rule 0).

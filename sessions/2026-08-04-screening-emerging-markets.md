# 2026-08-04 — SCREENING: Emerging Markets (EM)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [EM](../framework/screening-coverage-log.md) (China, India, Brazil, Mexico, and other major EM, all sectors). Selected per the rotation rule: oldest "Last screened" date in the matrix (2026-07-14, three weeks prior — see [prior session](2026-07-14-screening-emerging-markets.md)).

**Unattended scheduled routine** (fired as the "Monthly Universe Screening Slice," first Saturday of the month — markets closed). No user available to paste a TIKR/Koyfin export, so per `screen.md` Step 0 this session goes to a documented fallback.

**Note on this session's automation prompt — same stale-instruction discrepancy flagged in the 2026-07-14 EM session, recurring:** the routine's own stored instructions again referenced an "EODHD_API_KEY... Path A" automated screener and described the cadence as monthly. Both are outdated: EODHD was deliberately removed from this framework on 2026-06-19 (see [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)) — the committed `EODHD_API_KEY` was flagged there as a compromised credential not to be reused without rotation — and `framework/automation-schedule.md` Routine 4 has since been retitled "Twice-Weekly Universe Screening Slice" (Tuesday + Saturday, 14:00 UTC), not monthly. The current, authoritative `.claude/commands/screen.md` no longer mentions EODHD at all: for an unattended run it goes straight to the quality-factor-ETF-holdings fallback (MOAT/QUAL/QGRW for US, IQLT for international). This session followed that current `screen.md` and did **not** touch the `EODHD_API_KEY` env var (confirmed present but unused).

**Sourcing note:** no EM-wide quality-factor ETF exists in this framework's documented fallback list (MOAT/QUAL/QGRW are US-only; IQLT tracks *developed* markets ex-US and holds no EM names) — same gap the 2026-07-14 session documented. This session again reused/refreshed the domain-knowledge structural-triage candidate pool rather than an ETF holdings list, and verified every candidate's Phase 01 numbers directly against `stockanalysis.com`'s ratios/financials/cash-flow-statement pages via `WebFetch` (`yfinance`/direct Yahoo confirmed blocked again this session — `curl_cffi` SSLError "Connection reset by peer" on the cookie/crumb endpoint, the same failure mode as every session since 2026-07-07).

---

## Step 1 — Structural triage

**Candidate pool: the 15 names from the 2026-07-14 session, re-verified, plus 2 new names** added this pass to broaden coverage (per the "a great business should never be missed" principle):

| Ticker | Company | Country | Sector |
|---|---|---|---|
| HKG:0700 / TCEHY | Tencent Holdings | China | Internet/gaming/social/fintech |
| NTES | NetEase | China | Gaming |
| SHA:600519 | Kweichow Moutai | China | Premium liquor (consumer staples) |
| PDD | PDD Holdings (Pinduoduo/Temu) | China | E-commerce |
| TCOM | Trip.com Group | China | Online travel agency |
| HKG:2020 | ANTA Sports Products | China | Sportswear/athletic apparel (multi-brand: ANTA, FILA, Amer Sports) *(new this pass)* |
| HKG:2269 | WuXi Biologics | China | Biologics CRO/CDMO *(new this pass)* |
| INFY | Infosys | India | IT services |
| TCS.NS | Tata Consultancy Services | India | IT services |
| ASIANPAINT.NS | Asian Paints | India | Paints/consumer |
| PIDILITIND.NS | Pidilite Industries | India | Specialty chemicals/adhesives |
| DIVISLAB.NS | Divi's Laboratories | India | Pharma API/CRAMS |
| ITC.NS | ITC Limited | India | Tobacco/FMCG conglomerate |
| NAUKRI.NS | Info Edge (India) | India | Internet classifieds (Naukri.com) |
| MELI | MercadoLibre | LatAm (Argentina HQ; Brazil/Mexico primary markets) | E-commerce/fintech |
| WEGE3.SA | WEG S.A. | Brazil | Industrial motors/automation |
| B3SA3.SA | B3 S.A. — Brasil Bolsa Balcão | Brazil | Exchange/clearing |

**Structurally excluded without a fresh quantitative pull** (categorical, one-line reasons — same exclusions the prior two EM sessions already documented; still valid on business-model grounds):

| Eliminated | Why |
|---|---|
| HDFC Bank, ICICI Bank, Itaú Unibanco, Banco Bradesco, Grupo Financiero Banorte | Banks — regulated balance-sheet businesses, gross margin/EV-EBIT framing doesn't fit |
| Saudi Aramco, Petrobras, Vale, PetroChina, Sinopec, China Shenhua | Commodity cyclicals (oil, mining, coal) — margin/FCF instability through cycles |
| Reliance Industries | Diversified conglomerate — commodity-cyclical refining/petrochemicals + capital-intensive telecom + thin-margin retail, no segment clears the bar |
| Alibaba, Meituan, JD.com | Multi-year margin compression from competition + 2021-2023 regulatory crackdown — fails "structurally expanding margins" trend test |
| China Mobile, China Telecom, América Móvil, Bharti Airtel | Regulated, capital-intensive telecom |
| GAP/OMAB/ASUR (Mexican regulated airports) | Asset-heavy regulated infrastructure |
| Walmex, Raia Drogasil, Magazine Luiza, Lojas Renner, Titan Company | Thin-margin retail/jewelry |
| FEMSA, Ambev | Beverage bottling — structurally sub-40% gross margins |
| Naspers/Prosus | Holding company (Tencent-stake wrapper, NAV-discount dynamics) |
| Yandex | Russia-domiciled — sanctions/delisting complications |
| TSMC, MediaTek, Samsung, SK Hynix, Hon Hai/Foxconn, Coupang, Sea Ltd/Grab | Taiwan/Korea/Singapore — belong to the **APAC-EX-JP** rotation slice, not EM |
| Yum China | Restaurant chain — structurally thin gross margins |

---

## Step 2 — Quantitative Phase 01 gate

Filters ([valuation-scoring.md](../framework/valuation-scoring.md)): Gross margin >40% · Net margin >12% · ROIC (ROE/ROIC/ROCE proxy) >15% · Revenue growth >8% (3yr CAGR) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x

**Source: `stockanalysis.com`** — `/financials/`, `/financials/ratios/`, `/financials/cash-flow-statement/` pages per ticker, fetched via `WebFetch` (all reachable this session). HK-listed tickers use the `stockanalysis.com/quote/hkg/<code>/` path (not `/stocks/<TICKER>.HK/`, which 404s); NSE-listed use `/quote/nse/<CODE>/`; B3-listed use `/quote/bvmf/<CODE>/`; Shanghai-listed use `/quote/sha/<CODE>/`. Revenue 3yr CAGR computed from FY(n-3)→FY(n) (oldest vs. most recent of the 4 fiscal years the site displays), formula shown per ticker.

| Ticker | Gross M | Net M | ROE/ROIC/ROCE | Rev 3yr CAGR | FCF 3yr positive? | Net Debt/EBITDA | FCF yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **Tencent (0700.HK)** | 56.25% (FY25) ✅ | 29.91% (FY25) ✅ | ROE 20.52% / ROIC 17.57% ✅ | 10.68% — (751,766/554,552)^(1/3)−1, FY22→FY25 ✅ | ✅ FY23 200,954 / FY24 195,594 / FY25 215,570 CNY mn | −0.19 (net cash) ✅ | 5.95% ✅ | 14.23x ✅ | **PASS — 8/8 clean** |
| **PDD Holdings (PDD)** | 56.28% (FY25) ✅ | 22.63% (FY25) ✅ | ROE 23.17% / ROCE 23.29% ✅ | 49.0% — (431,846/130,558)^(1/3)−1, FY22→FY25 ✅ | ✅ FY23 93,579 / FY24 120,962 / FY25 105,794 CNY mn | −4.39 (net cash) ✅ | 12.32% ✅ | 4.53x ✅ | **PASS — 8/8 clean** |
| **Kweichow Moutai (600519.SH)** | 91.19% (FY25) ✅ | 48.76% (FY25) ✅ | ROE 31.20% / ROIC 40.82% ✅ | 10.82% — (168,838/124,100)^(1/3)−1, FY22→FY25 ✅ | ✅ FY23 63,973 / FY24 87,785 / FY25 58,395 CNY mn | −0.44 (net cash) ✅ | 4.62% ✅ | 14.52x ✅ | **PASS — 8/8 clean** *(FY25 was a YoY decline — qualitative flag below)* |
| **ANTA Sports Products (2020.HK)** *(new)* | 62.00% (FY25) ✅ | 16.94% (FY25) ✅ | ROE 22.51% / ROIC 21.49% ✅ | 14.36% — (80,219/53,651)^(1/3)−1, FY22→FY25 ✅ | ✅ FY23 18,473 / FY24 14,483 / FY25 18,491 CNY mn | −0.37 (net cash) ✅ | 9.56% ✅ | 9.50x ✅ | **PASS — 8/8 clean** |
| NetEase (NTES) | 64.29% ✅ | 29.98% ✅ | ROE 10.69% / ROIC 343.5%* ✅ | 5.28% ❌ (96,496→112,626, FY22→FY25) | ✅ all 3yr positive | −3.97 ✅ | 9.08% ✅ | 10.90x ✅ | **FAIL — Rev 3yr CAGR only** |
| Trip.com (TCOM) | 80.58% (FY25) ✅ | 53.50% (FY25) ✅ | ROE 18.62% / ROIC 10.91% ❌ | 46.04% ✅ (reusing sourced FY22 20,039 CNY mn vs. this session's FY25 62,409; unchanged historical figure) | ✅ FY23 21,398 / FY24 19,034 / FY25 13,582 CNY mn | −3.07 ✅ | 6.75% ✅ | 9.44x ✅ | **FAIL — ROIC only** (10.91% vs >15%, improved from 7.94% last pass but still short) |
| Infosys (INFY) | 30.16% (FY26) ❌ | 16.45% (FY26) ✅ | ROE 15.98% ✅ | 7.98% ❌ (0.02pp miss, unchanged from last pass) | ✅ all 3yr positive | DATA GAP (shown as "—") | 7.67% ✅ | **42.48x** ❌ (flagged — see Step 4) | **FAIL — Gross margin, Rev CAGR, EV/EBIT** |
| TCS (TCS.NS) | 40.31% (FY26) ✅ (narrow) | 18.43% (FY26) ✅ | ROE 47.74% / ROIC 66.38% ✅ | 5.80% ❌ | ✅ all 3yr positive | −0.47 ✅ | 5.41% ✅ | 12.49x ✅ | **FAIL — Rev 3yr CAGR only** |
| Asian Paints (ASIANPAINT.NS) | 43.30% (FY26) ✅ | 12.16% (FY26) ✅ (narrow) | ROIC 25.49% ✅ (ROE not published this pass) | 5.26%† ❌ (carried forward — FY22/23 not shown this pass, see Step 4) | ✅ all 3yr positive | −0.68 ✅ | 2.11% ❌ | 42.34x ❌ | **FAIL — Rev CAGR, FCF yield, EV/EBIT** |
| Pidilite Industries (PIDILITIND.NS) | 55.04% (FY26) ✅ | 16.77% (FY26) ✅ | ROE 23.52% / ROIC 34.94% ✅ | **7.36%** ❌ (117,991→146,008, FY23→FY26 — correct 3yr span this pass, resolves the 07-14 session's 4yr-span flag; still a near-miss) | ✅ all 3yr positive | −1.03 ✅ | 1.36% ❌ | 47.39x ❌ | **FAIL — Rev CAGR, FCF yield, EV/EBIT** |
| Divi's Laboratories (DIVISLAB.NS) | 59.06% (FY26) ✅ | 24.32% (FY26) ✅ | ROIC 19.67% ✅ (ROE not published this pass) | **10.79%** ✅ (77,670→105,600, FY23→FY26 — correct 3yr span; now clears, vs. the 07-14 session's 4.19% 4yr-span read) | ✅ FY24 2,580 / FY25 2,150 / FY26 2,180 INR mn (thin but positive) | −0.81 ✅ | 0.10% ❌ | 62.80x ❌ | **FAIL — FCF yield, EV/EBIT only** (quality metrics all now pass; priced at extreme premium) |
| ITC Limited (ITC.NS) | 57.84% (FY26) ✅ | 26.23% (FY26, ex-one-off) ✅ | ROIC 35.59% ✅ (ROE not published this pass) | 3.60% ❌ (709,369→788,684, FY23→FY26) | ✅ all 3yr positive | −0.87 ✅ | 4.53% ✅ | 13.88x ✅ | **FAIL — Rev 3yr CAGR only** |
| Info Edge (NAUKRI.NS) | 55.76% ✅ | 44.14% (inflated by non-operating stake gains — flagged) ✅ | ROE 4.57% / ROIC 2.04% ❌ | 11.88% ✅ | ✅ all 3yr positive | −3.85 ✅ | 1.22% ❌ | 76.38x ❌ | **FAIL — ROE/ROIC, FCF yield, EV/EBIT** |
| MercadoLibre (MELI) | 44.50% (FY25) ✅ | 6.91% (FY25) ❌ | ROE 27.37% / ROIC 16.70% ✅ | 38.9% ✅ | ✅ FY23 4,631 / FY24 7,058 / FY25 10,773 $mn | 1.70 ✅ | 12.28% ✅ | 33.77x ❌ | **FAIL — Net margin, EV/EBIT** |
| WEG S.A. (WEGE3.SA) | 33.53% (FY25) ❌ | 15.63% (FY25) ✅ | ROE 30.79% / ROIC 38.28% ✅ | 10.92% ✅ (reusing sourced FY22 29,905 R$mn vs. this session's FY25 40,804; unchanged historical figure) | ✅ FY23 5,436 / FY24 5,472 / FY25 3,888 R$mn (declining but positive) | −0.35 ✅ | 2.05% ❌ | **25.89x** ❌ (widened from 23.73x) | **FAIL — Gross margin, FCF yield, EV/EBIT** |
| B3 S.A. (B3SA3.SA) | 95.49% (FY25) ✅ | 45.55% (FY25) ✅ | ROE 26.74% / ROIC 24.98% ✅ | 3.45% ❌ (reusing sourced FY22 9,092 R$mn vs. this session's FY25 10,068; unchanged historical figure) | ✅ FY23 3,686 / FY24 9,200 / FY25 4,213 R$mn | 0.08 ✅ | 8.19% ✅ | 11.24x ✅ | **FAIL — Rev 3yr CAGR only** |
| WuXi Biologics (2269.HK) *(new)* | 45.98% (FY25) ✅ | 22.53% (FY25) ✅ | ROE 11.64% / ROIC 12.99% ❌ | 12.59% ✅ | ✅ FY23 622 / FY24 1,288 / FY25 2,656 CNY mn (FY22 was −327, excluded — only the 3 most recent years need to be positive) | −1.59 ✅ | 1.78% ❌ | **21.42x** ❌ (narrow miss) | **FAIL — ROE/ROIC, FCF yield, EV/EBIT** |

*NetEase ROIC (343.5%) — net-cash-position denominator artifact, not relied on; ROE (10.69%) and revenue growth alone drive the verdict, unchanged read from the last two passes.
†Asian Paints revenue CAGR figure carried forward from the 2026-07-14 session (4yr-span, flagged there) since this pass's `stockanalysis.com` financials table only showed FY2024–FY2026 — see Step 4.

**No new PASS/FAIL flips versus the 2026-07-14 session's 3 qualified names** — all three (Tencent, PDD, Moutai) still clear cleanly. **ANTA Sports Products is a genuinely new qualified name**, added to the candidate pool this pass specifically to broaden coverage beyond the prior rotation's set.

---

## ✅ Qualified Quality List — 4 names, all clean 8/8 passes

**Tencent Holdings (0700.HK / TCEHY)**, **PDD Holdings (PDD)**, **Kweichow Moutai (600519.SH)**, **ANTA Sports Products (2020.HK)** — up from 3 last pass. ANTA is a first-time pass, added to the candidate pool this session.

### Near-miss watchlist

- **Divi's Laboratories (DIVISLAB.NS)** — now clears every quality metric (revenue CAGR corrected to a proper 3yr span, 10.79% vs >8%) but fails decisively on valuation: FCF yield 0.10%, EV/EBIT 62.80x. Priced far above what the framework's valuation filters tolerate.
- **Trip.com (TCOM)** — fails only on ROIC (10.91% vs >15%), same single-metric miss as the last two passes, narrowing slightly each time (7.94% → 10.91%).
- **NetEase (NTES)** — fails only on revenue 3yr CAGR (5.28% vs >8%), same single-metric miss as both prior passes.
- **WuXi Biologics (2269.HK)** — new candidate, narrowly misses EV/EBIT (21.42x vs <20x) plus ROE/ROIC and FCF yield; the closest of the two new names to qualifying.
- **Pidilite Industries (PIDILITIND.NS)** — quality metrics near-clean; revenue CAGR now measured correctly at 7.36% (3yr span), a narrow miss; still blocked mainly by valuation (FCF yield 1.36%, EV/EBIT 47.39x).

---

## Step 3 — Qualitative pass (Tencent, PDD, Kweichow Moutai, ANTA Sports)

Sourced via `WebSearch` for developments since the 2026-07-14 session (three weeks) for the three carried-forward names, and a full first pass for ANTA Sports.

### Tencent Holdings (0700.HK)

1. **Why are margins high?** WeChat/Weixin super-app (messaging, payments, mini-programs, ads) plus a top-tier gaming portfolio — software/digital-distribution economics with near-zero marginal cost. Unchanged, structural.
2. **What would it take to compete?** WeChat's ~1.3B-user network effect remains unmatched; no competitor has displaced it.
3. **Capital allocation (5–10yr):** Continued disciplined reinvestment, consistent with prior sessions' read.
4. **Where's growth coming from (3–5yr)?** The Xiaowei AI assistant (flagged integrating into WeChat last session) is now in active testing within Weixin's Chinese version, working through China's regulatory compliance process ahead of a public launch — no confirmed launch date yet. Tencent shares reportedly jumped ~10% on expectations the AI agent nears release ([SCMP](https://www.scmp.com/tech/big-tech/article/3355651/tencent-shares-jump-expectations-ai-agent-within-wechat-super-app)).
5. **Best bear case:** Revenue growth has slowed to 8% YoY in Q1 2026 as gaming regulation tightens and ad spend softens ([TipRanks](https://www.tipranks.com/news/global-markets/tencent-paces-toward-ai-as-gaming-space-heats-up)); WeChat also tightened its own content-governance rules to ban non-human AI/script-driven content publishing on official/service accounts — a new compliance overhead layered on top of the AI buildout, not a relaxation.
6. **Disruption vector:** Low-to-medium, unchanged — the live risk remains regulatory/compliance pacing, not a technological challenger to WeChat's daily-life embeddedness.

**Conclusion:** Still a clean 8/8 pass. Growth deceleration (8% Q1 2026) is a real, incremental negative versus the improving-regulatory read from last session, balanced by the AI-agent progress. No change to the standing recommendation: `/new-position Tencent` to compute Quality/Valuation scores against live pricing.

Sources: [SCMP — Tencent shares jump on WeChat AI agent](https://www.scmp.com/tech/big-tech/article/3355651/tencent-shares-jump-expectations-ai-agent-within-wechat-super-app), [CNBC — Tencent tests AI assistant in WeChat](https://www.cnbc.com/2026/06/22/tencent-ai-assistant-wechat-china.html), [TipRanks — Tencent paces toward AI as gaming space heats up](https://www.tipranks.com/news/global-markets/tencent-paces-toward-ai-as-gaming-space-heats-up), [SCMP — Tencent moves to rein in AI content flood on WeChat](https://www.scmp.com/tech/article/3349696/tencent-moves-rein-ai-content-flood-wechat-stricter-rules)

### PDD Holdings (PDD)

1. **Why are margins high?** Asset-light, algorithm-driven social/group-buying commerce plus Temu's international extension, monetized via transaction fees + ads. Unchanged.
2. **What would it take to compete?** Domestic wedge still real but Temu remains in a contested, capital-intensive global low-price fight now directly exposed to tariff policy.
3. **Capital allocation (5–10yr):** Continues reinvesting aggressively; large net-cash balance sheet, no debt.
4. **Where's growth coming from (3–5yr)?** Some tariff relief materialized since the last session: effective mid-May, the de minimis tariff rate on low-value Chinese imports was cut from 120% to 54%, a planned per-item duty increase ($100→$200) was suspended, and general China import tariffs were lowered to 10% ([TipRanks](https://www.tipranks.com/news/pdd-holdings-pdd-q2-pre-earnings-heres-what-to-expect)) — a partial reversal of the de minimis termination flagged as fully "realized" pain last session.
5. **Best bear case:** Despite the partial relief, margin pressure continued into Q1 2026: revenue grew 10% YoY to $13.18B (below consensus), while adjusted operating profit fell 36% YoY and adjusted operating margin compressed from 32.9% to 19.1% ([TipRanks](https://www.tipranks.com/news/pdd-holdings-pdd-q2-pre-earnings-heres-what-to-expect)). Next earnings due 2026-08-25 — a near-term catalyst that will show whether the partial tariff relief is showing up in the P&L yet.
6. **Disruption vector:** Medium, unchanged.

**Conclusion:** Still a clean 8/8 pass. The qualitative picture is mixed rather than purely worse this time — tariff *policy* eased somewhat, but the Q1 2026 print shows the margin damage still working through the business. Standing recommendation unchanged: `/new-position PDD` proceed, but explicitly weigh the realized/still-unfolding margin compression, and flag the 2026-08-25 earnings date as a trigger worth re-checking before or shortly after sizing.

Sources: [TipRanks — PDD Q2 pre-earnings preview](https://www.tipranks.com/news/pdd-holdings-pdd-q2-pre-earnings-heres-what-to-expect), [Simply Wall St — PDD valuation check amid Temu regulatory scrutiny](https://simplywall.st/stocks/us/retail/nasdaq-pdd/pdd-holdings/news/pdd-holdings-pdd-valuation-check-as-temu-regulatory-scrutiny)

### Kweichow Moutai (600519.SH)

1. **Why are margins high?** Ultra-premium baijiu (Feitian Moutai) — extreme brand/scarcity pricing power. Unchanged, though visibly under more active management intervention than at any point in this framework's coverage.
2. **What would it take to compete?** Still one of the strongest moats covered, but under real strain (see below).
3. **Capital allocation (5–10yr):** Management raised Feitian's price for the **second time in months** — retail price on its official e-commerce platform up 100 yuan to 1,639 yuan/bottle and ex-factory price up 100 yuan to 1,369 yuan/bottle, effective 18 July 2026 ([Bloomberg](https://www.bloomberg.com/news/articles/2026-07-20/moutai-hikes-price-of-flagship-liquor-for-second-time-in-months)), explicitly framed as "matching supply with demand" and closing the gap between official and street prices — a continuation, not a reversal, of the market-driven pricing reform flagged last session.
4. **Where's growth coming from (3–5yr)?** Still genuinely uncertain. The iMoutai app rollout (flagged last session) has now added 6.28 million new users since accelerating Feitian's presence on the platform — larger than the 2.7M/9-day figure cited previously, suggesting the digital-channel pivot is scaling.
5. **Best bear case:** Despite the two price hikes, "swollen inventories, weak sell-through, and strained distributors still weigh on the industry" ([Bloomberg](https://www.bloomberg.com/news/articles/2026-07-20/moutai-hikes-price-of-flagship-liquor-for-second-time-in-months)) — wholesale prices remain in the 1,500–2,100 yuan range, well below the 3,000+ yuan prior peak. Raising official prices while street/wholesale prices stay soft is a real signal management is trying to manufacture a floor rather than responding to organic demand recovery.
6. **Disruption vector:** Low technologically; the open question is still the generational/cultural demand question flagged last session — not resolved.

**Conclusion:** Still an 8/8 clean quantitative pass, but the qualitative picture has **not stabilized** — a second price hike in months, against a backdrop of soft wholesale prices and distributor strain, reads as active life-support for pricing rather than a demand recovery. Standing recommendation unchanged: `/new-position Moutai` proceed with explicit extra scrutiny on Phase 02 growth/FCF-trend inputs; this remains a "clears the gate today, needs the freshest possible re-verification" case.

Sources: [Bloomberg — Moutai hikes price of flagship liquor for second time in months](https://www.bloomberg.com/news/articles/2026-07-20/moutai-hikes-price-of-flagship-liquor-for-second-time-in-months), [BigGo Finance — Moutai's direct sales reform shakes market](https://finance.biggo.com/news/_oky2psBpPlmmn5lrW6C)

### ANTA Sports Products (2020.HK) — new candidate, first qualitative pass

1. **Why are margins high?** ANTA operates a "single-focus, multi-brand" portfolio (ANTA mainline, FILA China, plus Amer Sports brands — Arc'teryx, Salomon, Wilson) spanning mass-market to premium/technical athletic wear, with heavy vertical integration and R&D spend (RMB 2B+ in 2024) funding proprietary performance technologies rather than commodity manufacturing.
2. **What would it take to compete?** A 12,000+-touchpoint direct-to-consumer (DTC) network gives ANTA first-party data and inventory/pricing control most competitors selling through wholesale don't have, and the multi-brand structure protects each brand's individual positioning while capturing multiple consumer segments simultaneously — a rare combination for a sportswear company outside Nike/Adidas scale.
3. **Capital allocation (5–10yr):** ANTA's playbook is explicit: acquire distressed/undervalued brands (its 2019 €4.6B Amer Sports acquisition being the largest), transform them via DTC-channel control and Greater China distribution access, then recycle the resulting capital gains (e.g. Amer Sports' own 2024 US IPO) to fund the next acquisition. A repeatable, capital-recycling M&A model rather than one-off deal-making.
4. **Where's growth coming from (3–5yr)?** Amer Sports brands (Arc'teryx in particular) scaling in China via ANTA's distribution access is the clearest growth vector; ANTA also used the Milano Cortina 2026 Winter Olympics as a global showcase, outfitting ten Chinese national teams under the ANTA brand plus FILA China (freestyle skiing) and Descente (alpine skiing/snowboard) — brand-visibility investment ahead of the 2026 Games.
5. **Best bear case:** FY2025 net income (13,588 CNY mn) declined versus FY2024 (15,596 CNY mn) despite revenue growth (70,826→80,219 CNY mn) — a margin-compression signal (net margin 22.02%→16.94%) not yet explained by a specific one-off in the sources reviewed this session; worth a specific line-item check before sizing. Multi-brand M&A integration risk (Amer Sports was a large, complex acquisition) and Chinese-consumer discretionary-spending sensitivity are the standing structural risks for any China consumer name in this framework's current environment read.
6. **Disruption vector:** Low-to-medium — sportswear/apparel isn't prone to sudden technological displacement, but fashion-cycle/brand-relevance risk is real and not fully insulated by the multi-brand structure.

**Conclusion:** Clean 8/8 Phase 01 pass and a first-time qualified name. The FY2025 net-margin compression (flagged in point 5) is the one open item worth resolving before proceeding — not disqualifying at Phase 01, but a specific question for `/new-position ANTA Sports` to answer with the underlying line items (likely candidates: Amer Sports integration costs, FX, or increased brand-marketing spend around the Olympics, none confirmed from sources reviewed this session).

Sources: [Sporting Goods Intelligence — ANTA Sports: the making of a global multi-brand machine](https://www.sgieurope.com/strategies/anta-sports-the-making-of-a-global-multi-brand-machine/121214.article), [Double V Consulting — Anta multi-brand strategy](https://www.doublevconsulting.com/post/anta-multi-brand-strategy-china-sportswear-global-acquisition), [MatrixBCG — ANTA growth strategy](https://matrixbcg.com/blogs/growth-strategy/anta)

---

## Step 4 — Data gaps (CLAUDE.md Rule 0 — none estimated)

- **Infosys (INFY) EV/EBIT (42.48x)**: this session's `stockanalysis.com` read is roughly 4x the 2026-07-14 session's figure (10.76x) with no comparable move in the other ratios (ROE actually improved slightly). Flagged as a genuine data-quality concern rather than accepted at face value — either a large, real re-rating or a source/extraction inconsistency. **Not substituted or averaged with the prior figure** (would be estimating); reported as sourced, flagged for re-verification at the next INFY touchpoint. Doesn't change the FAIL verdict (INFY already fails on gross margin and revenue CAGR regardless).
- **Infosys Net Debt/EBITDA**: shown as "—" (blank) on the source page this session — genuine data gap, not substituted. Moot for the verdict.
- **Asian Paints revenue 3yr CAGR**: this session's `stockanalysis.com` financials table only displayed FY2024–FY2026 (no FY2022/FY2023 revenue), so the last session's already-flagged 4yr-span figure (5.26%, FY2022→FY2026) was carried forward rather than re-derived — the underlying historical revenue number doesn't change between sessions, so this isn't an estimate, but it's flagged since it wasn't freshly re-pulled this pass. Doesn't change the verdict either way (fails decisively on FCF yield/EV-EBIT regardless).
- **WEG S.A. / B3 S.A. FY2022 revenue**: same carry-forward situation — this session's financials tables only went back to FY2023, so FY2022 revenue (used for the 3yr CAGR denominator) was reused from the 2026-07-14 session's sourced figure rather than re-fetched. Both figures are unchanged historical facts, not estimates.
- **Trip.com (TCOM) TTM figures**: this session's TTM revenue/gross-profit/gross-margin extraction (64,787 / 39,162 / 60.45%) is internally inconsistent with FY2025 (62,409 / 50,287 / 80.58%) — a TTM gross margin *lower* than the prior full year while TTM revenue is barely above FY2025 revenue implies TTM gross profit fell in absolute terms even as revenue rose, which doesn't reconcile cleanly. Treated as an unreliable extraction and **not used** — FY2025 annual figures used instead for the gross margin / net margin filter checks, consistent with the FY2025-based verdict already reached on ROIC regardless.
- **ANTA Sports (2020.HK) FY2025 net-margin compression**: flagged qualitatively above (point 5) — no specific cause identified from the sources reviewed this session. Reported as an open item, not estimated.

No currency-translation or ADR-vs-ordinary gaps beyond the above this session — `stockanalysis.com` continues to provide directly comparable, single-sourced figures for every candidate.

---

## Next steps

- `/new-position Tencent` (0700.HK / TCEHY) — still cleanest pass; note the Q1 2026 growth deceleration (8% YoY) as a data point for Phase 02.
- `/new-position PDD` — proceed, but explicitly weigh the still-unfolding margin compression (Q1 2026 adjusted operating margin 19.1% vs 32.9% prior) against the partial tariff relief; 2026-08-25 earnings is a near-term trigger.
- `/new-position Moutai` (600519.SH) — proceed with extra scrutiny; the second price hike in months against soft wholesale prices is a live, unresolved qualitative flag, not a resolved one. Confirm Stock Connect/IBKR tradability first (carried-over note, still not verified).
- `/new-position ANTA Sports` (2020.HK) — new qualified name; resolve the FY2025 net-margin-compression question with underlying line items before sizing.
- Watchlist: **Divi's Laboratories (DIVISLAB.NS)** — now clears every quality filter, blocked purely by extreme valuation (EV/EBIT 62.80x); **Trip.com (TCOM)** — fails only on ROIC, narrowing each pass; **NetEase (NTES)** — fails only on revenue CAGR, unchanged; **WuXi Biologics (2269.HK)** — new name, narrowly misses EV/EBIT (21.42x).
- **Pidilite** — quality metrics near-clean, revenue CAGR now correctly measured at 7.36% (a narrow miss); still blocked by extreme valuation.
- Coverage log updated below — next "oldest Last screened" slice is **NA-2**, last screened 2026-07-25.

---

## Glossary

- **CAGR (Compound Annual Growth Rate)** — the smoothed annual growth rate that would take a starting value to an ending value over N years, accounting for compounding.
- **ROE (Return on Equity)** — net income as a percentage of shareholders' equity; a profitability/efficiency measure.
- **ROIC (Return on Invested Capital)** — net operating profit after tax divided by total invested capital (debt + equity); a cleaner measure than ROE for companies with unusual capital structures.
- **ROCE (Return on Capital Employed)** — a close cousin of ROIC, used here as a proxy where a source doesn't publish ROIC directly.
- **FCF (Free Cash Flow)** — operating cash flow minus capital expenditure; cash actually available to the business after maintaining/growing operations.
- **FCF Yield** — FCF divided by market cap (or enterprise value); how much free cash the business throws off relative to what you're paying for it.
- **EV/EBIT (Enterprise Value / Earnings Before Interest & Tax)** — a capital-structure-neutral valuation multiple; lower means cheaper relative to operating earnings.
- **Net Debt/EBITDA** — a leverage ratio; negative means the company holds more cash than debt (net cash).
- **Gross margin** — (revenue − cost of goods sold) ÷ revenue; a measure of pricing power/production efficiency before operating costs.
- **Net margin** — net income ÷ revenue; the percentage of each dollar of sales that becomes profit after all costs.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial data, used as a rolling "current" snapshot between annual reports.
- **ADR (American Depositary Receipt)** — a US-listed security representing shares of a foreign company, letting US investors trade it without a foreign brokerage account.
- **Moat** — a durable competitive advantage that protects a business's profits from competitors over time (network effects, brand, switching costs, scale, etc.).
- **DTC (Direct-to-Consumer)** — a distribution model where a company sells directly to end customers rather than through third-party wholesalers/retailers, giving it pricing control and first-party data.
- **Structural triage** — Step 1 of the `/screen` process: eliminating obviously-disqualified candidates on business-model grounds before spending analysis effort on detailed financials.
- **Data gap** — a required metric that could not be sourced (or, here, a sourced figure with an internal-consistency problem) and, per CLAUDE.md Rule 0, is flagged rather than estimated or silently substituted.

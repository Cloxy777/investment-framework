# 2026-07-14 — SCREENING: Emerging Markets (EM)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [EM](../framework/screening-coverage-log.md) (China, India, Brazil, Mexico, and other major EM, all sectors). Selected per the rotation rule: oldest "Last screened" date in the matrix (2026-06-14, one full month ago — see [prior session](2026-06-14-screening-emerging-markets.md)).

**Unattended scheduled routine** (Monthly Universe Screening Slice, first Saturday of the month — markets closed). No user available to paste a TIKR/Koyfin export, so per `screen.md` Step 0 this session goes straight to a documented fallback. However: unlike a true "no screener access" case, this session found `stockanalysis.com` directly reachable (200 OK via `curl`/`WebFetch`) — the network-policy block that forced a WebSearch-only approach in the 2026-06-14 EM session (and the ETF-holdings-only path envisioned by the unattended-routine fallback) did not apply here. `yfinance`/Yahoo remained blocked (`curl_cffi` SSL "Connection reset by peer", same failure mode as the 2026-07-07/07-11 sessions). Given a live `stockanalysis.com` connection, this session reused the prior session's **structural-triage candidate pool** (domain-knowledge-built, since no single EM-wide quality-factor ETF exists in the framework's documented list — MOAT/QUAL/QGRW are US-only, IQLT tracks *developed* markets ex-US and holds no EM names) and verified every candidate's real Phase 01 numbers directly against `stockanalysis.com`'s financials/ratios/cash-flow-statement pages — a materially stronger data source than the WebSearch-snippet method used 2026-06-14. Flagged here per Rule 0 transparency.

**Note on this session's automation prompt:** the routine's own instructions referenced an "EODHD_API_KEY... Path A" automated screener. That path was deliberately removed from this framework on 2026-06-19 (see [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)) — EODHD's free-plan endpoints were unreliable, and the committed API key was flagged as a compromised credential not to be reused without rotation. The current `.claude/commands/screen.md` no longer mentions EODHD at all. This session followed the **current, authoritative `screen.md`** (manual/ETF-fallback Step 0) rather than the stale instruction, and did not touch the `EODHD_API_KEY` env var.

---

## Step 1 — Structural triage

**Candidate pool: the 12 names from the 2026-06-14 session, re-verified, plus 3 new names** added this pass to broaden coverage (per the "a great business should never be missed" principle — same 12 names every rotation would just re-confirm last month's answer):

| Ticker | Company | Country | Sector |
|---|---|---|---|
| HKG:0700 | Tencent Holdings | China | Internet/gaming/social/fintech |
| NTES | NetEase | China | Gaming |
| SHA:600519 | Kweichow Moutai | China | Premium liquor (consumer staples) |
| PDD | PDD Holdings (Pinduoduo/Temu) | China | E-commerce |
| TCOM | Trip.com Group | China | Online travel agency *(new this pass)* |
| INFY | Infosys | India | IT services |
| TCS.NS | Tata Consultancy Services | India | IT services |
| ASIANPAINT.NS | Asian Paints | India | Paints/consumer |
| PIDILITIND.NS | Pidilite Industries | India | Specialty chemicals/adhesives |
| DIVISLAB.NS | Divi's Laboratories | India | Pharma API/CRAMS |
| ITC.NS | ITC Limited | India | Tobacco/FMCG conglomerate *(new this pass)* |
| NAUKRI.NS | Info Edge (India) | India | Internet classifieds (Naukri.com) *(new this pass)* |
| MELI | MercadoLibre | LatAm (Argentina HQ; Brazil/Mexico primary markets) | E-commerce/fintech |
| WEGE3.SA | WEG S.A. | Brazil | Industrial motors/automation |
| B3SA3.SA | B3 S.A. — Brasil Bolsa Balcão | Brazil | Exchange/clearing |

**Structurally excluded without a fresh quantitative pull** (categorical, one-line reasons — same exclusions the 2026-06-14 EM session already documented; not re-derived, still valid on business-model grounds a month later):

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

Filters ([valuation-scoring.md](../framework/valuation-scoring.md)): Gross margin >40% · Net margin >12% · ROIC>15% (ROE/ROIC-proxy) · Revenue growth >8% (3yr CAGR) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x

**Source: `stockanalysis.com`** — `/financials/ratios/`, `/financials/`, `/financials/cash-flow-statement/` pages per ticker, fetched directly via `WebFetch` (all reachable this session, unlike 2026-06-14). "TTM"/"Current" = the site's live column dated Jul 14, 2026. Revenue 3yr CAGR computed from the oldest vs. most recent of the fiscal years the site displays, formula shown per ticker below.

| Ticker | Gross M | Net M | ROE/ROIC (TTM) | Rev 3yr CAGR | FCF 3yr positive? | Net Debt/EBITDA | FCF yield (TTM) | EV/EBIT (TTM) | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **Tencent (0700.HK)** | 56.25% (FY2025) ✅ | 29.91% (FY2025) ✅ | ROE 20.52% / ROIC 17.57% ✅ | 10.7% — (751,766/554,552 CNY mn)^(1/3)−1, FY2022→FY2025 ✅ | ✅ FY2023 200,954 / FY2024 195,594 / FY2025 215,570 CNY mn | −0.19 (net cash) ✅ | 6.38% ✅ | 13.29x ✅ | **PASS — 8/8 clean** |
| **PDD Holdings (PDD)** | 56.28% (FY2025) ✅ | 22.63% (FY2025) ✅ | ROE 23.17% / ROCE 23.29% (ROIC not published; ROE/ROCE proxy used) ✅ | 49.0% — (431,846/130,558 CNY mn)^(1/3)−1, FY2022→FY2025 ✅ | ✅ FY2023 93,579 / FY2024 120,962 / FY2025 105,794 CNY mn | −4.34 (net cash) ✅ | 13.08% ✅ | 4.13x ✅ | **PASS — 8/8 clean** |
| **Kweichow Moutai (600519.SH)** | 91.19% (FY2025) ✅ | 48.76% (FY2025) ✅ | ROE 31.20% / ROIC 40.82% ✅ | 10.81% — (168,838/124,100 CNY mn)^(1/3)−1, FY2022→FY2025 ✅ | ✅ FY2023 63,973 / FY2024 87,785 / FY2025 58,395 CNY mn | −0.69 (net cash) ✅ | 5.07% ✅ | 13.21x ✅ | **PASS — 8/8 clean** *(see qualitative flag below — FY2025 itself was a YoY decline)* |
| **NetEase (NTES)** | 64.29% (FY2025) ✅ | 30.90% (FY2025) ✅ | ROE 10.69% / ROIC 343.53%* ✅ | 5.29% — (112,626/96,496 CNY mn)^(1/3)−1, FY2022→FY2025 ❌ | ✅ all 3yr positive, growing | −4.09 (net cash) ✅ | 9.20% ✅ | 10.87x ✅ | **FAIL — Rev 3yr CAGR only** (5.29% vs >8%; *ROIC figure is a net-cash denominator artifact, flagged not relied on*) |
| **Trip.com (TCOM)** | 80.58% (FY2025) ✅ | 52.93% (FY2025) ✅ | ROE 15.27% / ROIC 7.94% ❌ | 46.04% — (62,409/20,039 CNY mn)^(1/3)−1, FY2022→FY2025 ✅ | ✅ all 3yr positive | −2.44 (net cash) ✅ | **DATA GAP** (TTM cell blank on source page; FY2025 was 4.16%, not substituted) | 8.32x ✅ | **FAIL — ROIC (7.94% < 15%)**; FCF yield DATA GAP |
| **Infosys (INFY)** | 30.16% (FY2026) ❌ | 16.45% (FY2026) ✅ | ROE 15.38% / ROIC 23.79% ✅ | 7.98% — (1,884,460/1,496,680 $mn)^(1/3)−1, FY2023→FY2026 ❌ *(0.02pp miss)* | ✅ all 3yr positive | −0.60 (net cash) ✅ | 8.01% ✅ | 10.76x ✅ | **FAIL — Gross margin, Rev 3yr CAGR** (both near-misses) |
| **TCS (TCS.NS)** | 40.31% (FY2026) ✅ (narrow — IT-services cost-of-revenue accounting) | 18.43% (FY2026) ✅ | ROE 47.74% / ROIC 66.38% ✅ | 5.80% — (2,670,210/2,254,580 ₹mn)^(1/3)−1, FY2023→FY2026 ❌ | ✅ all 3yr positive | −0.47 (net cash) ✅ | 6.05% ✅ | 11.12x ✅ | **FAIL — Rev 3yr CAGR only** |
| **Asian Paints (ASIANPAINT.NS)** | 43.30% (FY2026) ✅ | 12.16% (FY2026) ✅ (narrow) | ROE 20.89% / ROIC 22.64% ✅ | 5.26%† ❌ | ✅ all 3yr positive | −0.74 (net cash) ✅ | 2.21% ❌ | 44.32x ❌ | **FAIL — Rev CAGR, FCF yield, EV/EBIT** |
| **Pidilite Industries (PIDILITIND.NS)** | 55.04% (FY2026) ✅ | 16.77% (FY2026) ✅ | ROE 23.52% / ROIC 32.82% ✅ | 10.14%† ✅ | ✅ all 3yr positive | −1.10 (net cash) ✅ | 1.39% ❌ | 50.05x ❌ | **FAIL — FCF yield, EV/EBIT** (quality metrics all pass, priced at extreme premium) |
| **Divi's Laboratories (DIVISLAB.NS)** | 61.24% (FY2026) ✅ | 24.32% (FY2026) ✅ | ROE 16.19% / ROIC 17.64% ✅ | 4.19%† ❌ | ✅ all 3yr positive | −0.99 (net cash) ✅ | 0.12% ❌ | 60.71x ❌ | **FAIL — Rev CAGR, FCF yield, EV/EBIT** |
| **ITC Limited (ITC.NS)** | 57.84% (FY2026) ✅ | 26.23% (FY2026, ex-one-off) ✅ | ROE 29.34% / ROIC 36.85% ✅ | 3.59% — (788,684/709,369 ₹mn)^(1/3)−1, FY2023→FY2026 ❌ | ✅ all 3yr positive | −0.81 (net cash) ✅ | 4.65% ✅ | 12.65x ✅ | **FAIL — Rev 3yr CAGR only** |
| **Info Edge (NAUKRI.NS)** | 56.34% (FY2026) ✅ | 44.14% (FY2026, inflated by non-operating stake gains — flagged) ✅ | ROE 4.57% / ROIC 2.05% ❌ | 11.88% — (32,847/23,457 ₹mn)^(1/3)−1, FY2023→FY2026 ✅ | ✅ all 3yr positive | −3.78 (net cash) ✅ | 1.30% ❌ | 71.49x ❌ | **FAIL — ROE/ROIC, FCF yield, EV/EBIT** |
| **MercadoLibre (MELI)** | 44.50% (FY2025) ✅ | 6.91% (FY2025) ❌ | ROE 27.37% / ROIC 16.70% ✅ | 38.91% — (28,893/10,780 $mn)^(1/3)−1, FY2022→FY2025 ✅ | ✅ all 3yr positive | 1.27 ✅ | 12.48% ✅ | 33.25x ❌ | **FAIL — Net margin, EV/EBIT** |
| **WEG S.A. (WEGE3.SA)** | 33.53% (FY2025) ❌ | 15.63% (FY2025) ✅ | ROE 32.52% / ROIC 39.16% ✅ | 10.91% — (40,804/29,905 R$mn)^(1/3)−1, FY2022→FY2025 ✅ | ✅ all 3yr positive | −0.21 (net cash) ✅ | 2.47% ❌ | 23.73x ❌ (narrow) | **FAIL — Gross margin, FCF yield, EV/EBIT** |
| **B3 S.A. (B3SA3.SA)** | 95.49% (FY2025) ✅ | 45.55% (FY2025) ✅ | ROE 26.74% / ROIC 24.98% ✅ | 3.46% — (10,068/9,092 R$mn)^(1/3)−1, FY2022→FY2025 ❌ | ✅ all 3yr positive | 0.16 ✅ | 8.46% ✅ | 10.88x ✅ | **FAIL — Rev 3yr CAGR only** |

*NetEase ROIC (343.53%) — net-cash position shrinks the invested-capital denominator toward zero, producing a mathematically extreme ratio; not relied on as the pass/fail input given ROE (10.69%) tells a very different story. Verdict driven by revenue growth regardless.
†Asian Paints/Pidilite/Divi's Labs CAGR used a 4-year span (FY2022→FY2026, n=4) rather than the standard 3-year span — a sourcing-agent deviation flagged here for auditability. Does not change any verdict: Asian Paints and Divi's Labs fail decisively on FCF yield/EV-EBIT regardless of the CAGR precision question, and Pidilite's CAGR already clears >8% under either window.

**No DATA GAPs beyond the two flagged above (TCOM FCF yield)** — a marked improvement in data quality over the 2026-06-14 session's WebSearch-only sourcing, which had 20+ unresolved data gaps across the same-ish candidate set.

---

## ✅ Qualified Quality List — 3 names, all clean 8/8 passes

**Tencent Holdings (0700.HK / TCEHY)**, **PDD Holdings (PDD)**, **Kweichow Moutai (600519.SH)** — up from 2 PASS-leaning names (with unresolved data gaps) in the 2026-06-14 session. Both Tencent and Moutai's prior open items (ROE/ROIC data gap for Tencent; FCF-completeness gap for Moutai) fully resolved this pass, cleanly clearing every filter.

### Near-miss watchlist

- **Infosys (INFY)** — misses revenue 3yr CAGR by 0.02 percentage points (7.98% vs >8%) and gross margin (30.16% vs >40%, though IT-services cost-of-revenue accounting structurally compresses this metric — strategy.md's margin-trend OR-alternative not evaluated). Closest near-miss in the pool.
- **NetEase (NTES)** — fails only on revenue 3yr CAGR (5.29% vs >8%), same single-metric miss as the 2026-06-14 session (was 4.5% then) — growth has re-accelerated slightly but still short of the bar.
- **WEG S.A. (WEGE3.SA)** — EV/EBIT 23.73x, narrowly over the 20x bar; also fails gross margin (structural, industrial manufacturer) and FCF yield.

---

## Step 3 — Qualitative pass (Tencent, PDD, Kweichow Moutai)

Sourced via `WebSearch` for developments since the 2026-06-14 session (one month), combined with established company knowledge already in the framework's record for Tencent/PDD.

### Tencent Holdings (0700.HK)

1. **Why are margins high?** WeChat/Weixin super-app (messaging, payments, mini-programs, ads) and a top-tier gaming portfolio (Honor of Kings, PUBG Mobile, plus Riot/Supercell/Epic stakes) — software/digital-distribution economics with near-zero marginal cost. Structural, not cyclical.
2. **What would it take to compete?** WeChat's ~1.3B-user network effect (social graph + payments + merchant ecosystem) remains one of the strongest moats globally; no competitor has displaced it. Gaming requires top studios + IP + global distribution.
3. **Capital allocation (5–10yr):** Continuing pattern of disciplined reinvestment — this month brought news Tencent is **reassessing minority stakes in Japanese game studios** and **raising long-dated USD fixed-rate debt** to fund AI/cloud infrastructure, while being more selective about capital tied up in overseas gaming equity. Reads as continued capital discipline, consistent with the 2021-23 special-dividend/buyback pattern already on record.
4. **Where's growth coming from (3–5yr)?** New this month: **Xiaowei**, Tencent's AI assistant, was integrated directly into WeChat, tying AI capability to the user base and payment rails. Separately, **Q2 2026 gaming-license approvals rose 13% YoY (483 licenses)** — described in press coverage as a "turning point" easing years of regulatory pressure on the gaming industry. Both are incremental positives versus the June session's more cautious regulatory read.
5. **Best bear case:** AI/data compliance scrutiny is a new-ish overhang now that Xiaowei is wired into WeChat's payment rails; the large investment portfolio remains exposed to China-tech derating/ADR-delisting geopolitical risk; domestic competitive intensity in short-video/e-commerce continues.
6. **Disruption vector:** Low-to-medium, unchanged from June — WeChat's daily-life embeddedness is extremely hard to disrupt via a new delivery mechanism; the live risk is regulatory, not technological.

**Conclusion:** Upgraded from "PASS-leaning, ROE/ROIC unresolved" to a clean 8/8 Phase 01 pass, with the regulatory backdrop (gaming licenses) improving rather than worsening since June. Strongest name in this pass — recommend `/new-position Tencent` to compute Quality/Valuation scores against live pricing.

### PDD Holdings (PDD)

1. **Why are margins high?** Asset-light, algorithm-driven social/group-buying commerce (China) monetized via transaction fees + ads, plus Temu's international extension of the same model.
2. **What would it take to compete?** Domestic wedge (social/group-buying discovery + factory-direct sourcing) remains real but less differentiated than Tencent's network-effect moat; Temu is now in a heavily contested, capital-intensive global low-price land-grab against Shein, Amazon, and Western retailers, and its edge is mainly a cost advantage that tariffs directly attack.
3. **Capital allocation (5–10yr):** Continues reinvesting aggressively (subsidies, Temu buildout) rather than returning capital; $59.6B+ net cash, no debt, no value-destructive M&A on record.
4. **Where's growth coming from (3–5yr)?** Q1 2026 revenue +11% YoY (RMB106.2B) — continued deceleration from the hyper-growth phase (49% trailing 3yr CAGR is now backward-looking, not representative of the current run-rate). Temu's business model is reportedly "transitioning" toward a less capital-intensive, more monetizable "semi-managed" structure in response to tariff pressure.
5. **Best bear case — materially worse than June's flagged risk, not just repeated:** The June session flagged Temu's tariff/de-minimis exposure as a forward risk. It has since **materialized**: the US formally terminated the de-minimis exemption for sub-$800 packages, and PDD's Q1 2026 results showed **net income down 15% YoY** on a "massive bottom-line miss," driven by weaker-than-expected operating margin directly attributed to tariffs. This is now a realized, multi-quarter earnings impact, not a hypothetical.
6. **Disruption vector:** Medium, unchanged — PDD is itself a disruptor but is now on the receiving end of targeted regulatory action (the de-minimis change) aimed specifically at its cross-border shipping model.

**Conclusion:** Clears all 8 Phase 01 filters, but the qualitative picture has **deteriorated, not improved**, since June — the tariff bear case is no longer speculative. The apparent cheapness (FCF yield 13.08%, EV/EBIT 4.13x) may partly reflect the market correctly pricing sustained Temu margin compression rather than pure mispricing (Marks' second-level thinking, same caution flagged in June). Recommend `/new-position PDD` proceed but weigh the realized tariff impact explicitly and re-verify whether the growth/FCF trend embedded in Phase 02 inputs still holds given the deceleration.

### Kweichow Moutai (600519.SH)

1. **Why are margins high?** Ultra-premium baijiu (Feitian Moutai) — extreme brand/scarcity pricing power; minimal input cost relative to price (91%+ gross margin); functions as a cultural gifting/collectible asset as much as a beverage in China.
2. **What would it take to compete?** Historically one of the strongest moats in the framework's coverage — geographic-indication-protected production (Guizhou terroir), decades of brand cultivation, deep gifting-culture entrenchment. **But the moat is visibly under strain for the first time**: FY2025 was Moutai's **first annual profit and revenue decline since its 2001 listing** (net profit −4.5% to ¥82.32B, revenue −1.2% to ¥168.84B — a 25-year growth streak ended), and wholesale prices for Feitian have fallen from above ¥3,000 to the ¥1,500–2,100 range.
3. **Capital allocation (5–10yr):** Historically minimal capex, high payout. In direct response to the demand slump, management launched a **market-driven dynamic-pricing reform** for the direct-retail channel and pushed hard into a new digital channel — the **iMoutai app** gained 2.7M new users and 400K transactions within 9 days of putting Feitian on-platform. This is an unusually aggressive strategic pivot for a company that had never previously needed to compete on distribution or price.
4. **Where's growth coming from (3–5yr)?** Genuinely uncertain — a first for this name in the framework's record. Bull case (Goldman Sachs): the pricing reform accelerates channel-price normalization, with the sector potentially bottoming and rebounding in H2 2026. Bear case: this is structural demand softening (economic caution, mortgage-debt-crisis wealth effect, fading cachet among younger consumers), not a cyclical air pocket.
5. **Best bear case:** Chinese consumer caution amid a cooling economy and mortgage-debt stress; baijiu still ~94% of Chinese spirits consumption but younger-generation appeal reportedly waning; gifting/entertainment-budget demand (a meaningful share of ultra-premium volume) is exposed to anti-extravagance sentiment and slower corporate/government spend; management has essentially zero historical experience navigating a genuine down-cycle, which is itself a qualitative risk the pristine trailing financials don't capture.
6. **Disruption vector:** Low from a new-technology standpoint — nothing displaces a luxury collectible spirit via a new delivery mechanism. The real risk is generational/cultural: if younger Chinese consumers structurally prefer other categories, no channel innovation reverses that. Rated **open, not resolved**.

**Conclusion:** Clears all 8 trailing Phase 01 filters cleanly (3yr revenue CAGR is still positive at 10.81% across FY2022→FY2025 despite the FY2025 dip; margins/returns/balance sheet remain pristine) — but this is the first name in EM coverage to combine a clean quantitative pass with a live, headline-grade demand-deterioration story. The trailing CAGR is backward-looking and may not reflect the FY2025 inflection. Recommend `/new-position Moutai` proceed with explicit extra scrutiny on Phase 02 growth/FCF-trend inputs and the bear case above before any sizing — this is a "clears the gate today, needs the freshest possible re-verification" case, not a mechanical pass-through. Also re-confirm Shanghai Stock Connect/IBKR tradability for this A-share (same practical note carried over from the June session, not re-verified this pass).

---

## Step 4 — Data gaps (CLAUDE.md Rule 0 — none estimated)

- **Trip.com (TCOM)**: FCF yield (TTM/"Current" column) not published on the source page — reported as a genuine data gap rather than substituting the FY2025 figure (4.16%). Moot for the pass/fail call since ROIC (7.94%) already fails cleanly.
- **NetEase (NTES)**: TTM ROIC (343.53%) is a real sourced figure but a denominator artifact from NetEase's large net-cash position — flagged as unreliable and not used as the deciding input (revenue growth alone determines the FAIL).
- **Info Edge (NAUKRI)**: net margin (44.14%) is inflated by non-operating investment/stake-revaluation gains (its FY2022 net margin was 802.98% on the same effect) — reported as sourced but flagged as not representative of core operating profitability. Moot for the verdict (fails cleanly on ROE/ROIC, FCF yield, EV/EBIT regardless).
- **ITC Limited**: FY2025 net margin (46.13%) was distorted by a one-time ₹150,160M discontinued-operations gain; the clean FY2026 figure (26.23%) was used instead — noted for transparency, not a gap.
- **Asian Paints / Pidilite / Divi's Labs revenue CAGR**: sourced using a 4-year span (FY2022→FY2026) rather than the standard 3-year span due to a subagent methodology deviation — flagged above (†) with the underlying figures shown; does not change any verdict.

No currency-translation, ADR-vs-ordinary, or local-GAAP gaps this session — `stockanalysis.com` provided directly comparable, single-sourced figures for every candidate (unlike the 2026-06-14 session's WebSearch-blended TTM/quarterly/annual figures).

---

## Next steps

- `/new-position Tencent` (0700.HK / TCEHY) — cleanest pass this rotation; regulatory backdrop improving.
- `/new-position PDD` — proceed, but weigh the now-realized Temu tariff/margin impact (Q1 2026 net income −15% YoY) explicitly against the FCF-yield/EV-EBIT cheapness.
- `/new-position Moutai` (600519.SH) — proceed with extra scrutiny given the FY2025 profit/revenue decline (first since 2001 listing) and active pricing-reform pivot; confirm Stock Connect/IBKR tradability first.
- Watchlist: **Infosys (INFY)** — misses revenue CAGR by 0.02pp, closest near-miss in the pool; **NetEase (NTES)** — fails only on revenue CAGR, re-check next EM rotation; **WEG (WEGE3.SA)** — EV/EBIT narrowly over 20x.
- **Pidilite** — excellent quality metrics (all 6 non-valuation filters clean) but priced at an extreme premium (EV/EBIT 50x); worth a re-check on a meaningful pullback.
- Coverage log updated below — next "oldest Last screened" slice is **EU (Europe)**, last screened 2026-06-19.

---

## Glossary

- **CAGR (Compound Annual Growth Rate)** — the smoothed annual growth rate that would take a starting value to an ending value over N years, accounting for compounding.
- **ROE (Return on Equity)** — net income as a percentage of shareholders' equity; a profitability/efficiency measure.
- **ROIC (Return on Invested Capital)** — net operating profit after tax divided by total invested capital (debt + equity); a cleaner measure than ROE for companies with unusual capital structures (net-cash balance sheets, etc.).
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
- **Structural triage** — Step 1 of the `/screen` process: eliminating obviously-disqualified candidates on business-model grounds before spending analysis effort on detailed financials.
- **Data gap** — a required metric that could not be sourced and, per CLAUDE.md Rule 0, is flagged rather than estimated.

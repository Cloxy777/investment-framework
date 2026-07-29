# NEW POSITION — CAJPY (Canon Inc., traded here via the sponsored ADR; primary listing Tokyo Stock Exchange 7751)

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — unattended run)
**Date:** 2026-07-25 (Saturday — US and Japan markets closed; most recent live trade is Friday 2026-07-24's regular-session close)
**10Y US Treasury Yield:** Not fetched this session — evaluation stops at the Phase 01 Quality Score gate (see §3) before the Rate Environment Gate would otherwise apply (same precedent as the 2026-07-25 COIN/HOOD/NET sessions and the 2026-07-24 QCOM session before them).
**Current CAJPY portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session (the only Canon-adjacent hit anywhere in the repo is an unrelated mention of Canon as a lithography-equipment customer in the 2026-07-06 HNHPF session) — first-ever evaluation of this ticker under this framework.
**Sector:** Technology / Industrials — Diversified Imaging, Office, Medical & Industrial Equipment (cameras/lenses, office printers/copiers/MFPs, network cameras, medical imaging systems, semiconductor lithography & industrial equipment)
**Filer type:** Japanese primary listing (Tokyo Stock Exchange 7751, JPY-denominated financials); as a foreign private issuer, Canon files **Form 20-F** (annual) and **Form 6-K** (interim/material disclosures) with the SEC rather than a standard 10-K/10-Q. Traded on this account via the US OTC **sponsored** ADR **CAJPY** (confirmed sponsored, not unsponsored — IBKR's contract description reads "CANON INC-SPONS ADR").
**First-use jargon decode:** see closing Glossary.

---

## 0. Why this session exists — trigger source

A Telegram post today (`bolshegold/9832`, ~16:02 UTC, 2026-07-25) was a casual "earnings to watch next week" round-up mentioning $CAJPY by cashtag. Per the operating brief, **Telegram post text is never used as financial data** — it is a trigger only, and this post made no financial claims to independently verify either way. CAJPY had no watchlist entry anywhere in this repo (checked both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/`), so per [telegram-scan.md](../.claude/commands/telegram-scan.md) step 4's first bullet ("no watchlist entry exists at all → `/new-position`"), this triggers a full first-time evaluation.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Contract identity** | Confirmed via `mcp__Interactive-Brokers__search_contracts`: "CANON INC-SPONS ADR", **PINK**, contract_id **12340038**, country_code US. Canon's primary Tokyo listing (7751, TSEJ, contract_id 13905840) was also located but is not used for pricing — no US-account market-data permission was even attempted for it since the ADR is this account's actual tradable instrument (same precedent as the 2026-07-24 EVO/EVVTY session). | IBKR |
| **Live price used** | **$27.73** (`last.price`, `is_close: false`) | IBKR `get_price_snapshot` |
| **Cross-check** | `get_price_history` (`ONE_DAY` bars, `TWO_WEEKS`) confirms **2026-07-24 (Friday, the last completed regular session before today's Saturday date) closed at $27.73**, up from **2026-07-23's $27.52 close** — the snapshot's `prior-close` ($27.52) and `change` (+$0.21, +0.76%) reconcile exactly against this history. **No staleness issue** (unlike the HOOD/NET sessions earlier today). | IBKR `get_price_history` |
| 52-week range | $25.07 – $32.34 | IBKR `misc_statistics` |
| Dividend yield | IBKR reports **1.8%**; `stockanalysis.com`'s OTC:CAJPY page reports **3.65%** ($1.01/share ÷ $27.73) — a real discrepancy between sources, not reconciled this session (possibly a trailing-vs-forward or ADR-fee-adjusted difference). **Flagged**; not load-bearing for the Quality Score gate below. | IBKR; `stockanalysis.com` |
| Primary-listing cross-check | ¥4,526.00 (Tokyo, 7751), market cap ¥3.84 trillion, 849.31M shares outstanding | `stockanalysis.com` (TYO:7751) |
| Implied ADR economics | Canon's ADR ratio is publicly documented as 1 ADR : 1 ordinary share. Cross-check: ¥4,526 ÷ $27.73 = **163.2 JPY/USD**, consistent with prevailing JPY/USD spot in this period (mid-160s) — internally consistent, no ratio adjustment needed. | Derived |
| Market Cap (USD, ADR basis) | 849.31M shares × $27.73 ≈ **$23.55B** — reconciles closely with `stockanalysis.com`'s independently reported $23.48B (OTC:CAJPY page, small snapshot-timing difference) | Derived + `stockanalysis.com` |
| Analyst consensus (Tokyo listing) | 11 analysts, consensus **"Hold"**, average 12-month price target **¥4,777** (+5.55% from ¥4,526) | `stockanalysis.com` (TYO:7751) |
| US 10Y Treasury yield | Not fetched — moot, see header (gate fails before the Rate Environment Gate is reached) | — |

**Live price used throughout this session: $27.73** (CAJPY ADR, IBKR).

---

## 2. Data Sourcing Note

**`yfinance`/Yahoo Finance was unreachable this entire session** — a direct `python3` call to `yf.Ticker("CAJPY").info` and `yf.Ticker("7751.T").info` both failed with `curl_cffi.requests.exceptions.SSLError` ("Recv failure: Connection reset by peer"), and a plain `curl` to `query1.finance.yahoo.com/v8/finance/chart/AAPL` (a US mega-cap, not CAJPY-specific) returned **HTTP 429 "Too Many Requests"** directly from Yahoo's edge — confirmed via `$HTTPS_PROXY/__agentproxy/status` showing zero relay failures, i.e. not a proxy-side problem. This is the identical, session-wide Yahoo-side block pattern already documented in every 2026-07-24/2026-07-25 session today (QCOM, EVO, COIN, HOOD, NET) — not specific to Canon.

Fundamentals below are sourced entirely from **`stockanalysis.com`**'s Tokyo-listing pages (`/quote/tyo/7751/`, `/financials/`, `/financials/balance-sheet/`, `/financials/cash-flow-statement/`, `/financials/ratios/`) — Canon's primary-listing financials, reported in **JPY millions**, Japanese GAAP/IFRS convention. The OTC:CAJPY page itself (`/quote/otc/CAJPY/`) carries only headline price/dividend/market-cap data, not the detailed financial statements needed for Quality Score sub-scores (its `/financials/` sub-page 404'd), so the primary Tokyo listing's statement pages were used instead — the same underlying company, same audited consolidated financials, just reported in JPY rather than converted to USD. No FX conversion was needed for the Quality Score calculation below, since every sub-score formula (margins, ratios, growth rates) is scale/currency-invariant.

No required Phase 01 input was invented, estimated, or inferred from the triggering post.

**TTM window used:** stockanalysis.com's own TTM column, labeled "TTM (Mar '26)" for balance-sheet items and "TTM" for income-statement items — reconciled against the FY2025 annual figures plus visible quarterly deltas; treated as the vendor's standard trailing-twelve-month reconstruction.

### 2.1 Core financial data (JPY millions unless noted)

| Metric | TTM | FY2025 | FY2024 | FY2023 | FY2022 |
|---|---|---|---|---|---|
| Revenue | 4,659,984 | 4,624,727 | 4,509,821 | 4,180,972 | 4,031,414 |
| Gross Profit | 2,166,321 | 2,161,955 | 2,143,095 | 1,968,910 | 1,827,802 |
| Operating Income (EBIT) | 440,285 | 465,432 | 457,817 | 386,466 | 379,340 |
| Net Income | 308,125 | 332,053 | 160,025 | 264,513 | 243,961 |
| Net Margin | 6.61% | 7.18% | 3.55% | 6.33% | 6.05% |
| Operating Cash Flow | 428,470 | 475,903 | 606,831 | 451,190 | 262,603 |
| CapEx | (272,771) | (262,165) | (237,001) | (230,308) | (188,527) |
| Free Cash Flow | 155,699 | 213,738 | 369,830 | 220,882 | 74,076 |
| Total Debt | 1,233,355 | 946,159 | 663,500 | 517,317 | 417,413 |
| Cash & Equivalents | 639,490 | 585,981 | 501,565 | 401,323 | 362,101 |
| Net Debt | 582,023 | 327,732 | 157,160 | 112,172 | 44,407 |
| ROIC | 7.71% | 8.75% | 7.39% | 7.91% | 8.74% |
| ROE | 9.37% | 9.65% | 5.04% | 8.18% | 8.07% |
| EV/EBIT | 10.57× | 10.41× | 11.87× | 10.43× | 8.40× |
| EV/EBITDA | 6.15× | 6.87× | 7.84× | 6.45× | 5.26× |

Source: `stockanalysis.com` TYO:7751 income statement, balance sheet, cash-flow statement, and ratios pages.

**EBITDA (TTM) derived, not separately disclosed by this source:** since `stockanalysis.com` reports both EV/EBIT (10.57×) and EV/EBITDA (6.15×) off the same EV, `EBITDA = EBIT × (EV/EBIT ÷ EV/EBITDA) = 440,285 × (10.57/6.15) = 440,285 × 1.7187 ≈ 756,718` (JPY millions). Used only for the Balance Sheet sub-score below (Net Debt/EBITDA); flagged as a derived, not directly-disclosed, figure.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Hard disqualifier check (fires regardless of weighted score)

| Hard disqualifier | CAJPY data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF positive in every year shown: FY2022 ¥74,076M, FY2023 ¥220,882M, FY2024 ¥369,830M, FY2025 ¥213,738M, TTM ¥155,699M. **5 consecutive years positive.** | **PASS — does not fire.** |
| **Net Debt/EBITDA over threshold (2.5× standard)** | Net Debt (TTM) ¥582,023M ÷ EBITDA (TTM, derived) ¥756,718M = **0.77×** — well under 2.5×. Canon is not a payment network/exchange, so the Upgrade 5 asset-light override doesn't apply (and isn't needed — passes the standard threshold comfortably). | **PASS — does not fire.** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | FCF/NI: TTM 155,699/308,125 = **50.5%**; FY2025 213,738/332,053 = **64.4%** — both under 70%, two most-recent consecutive periods. **This would fire the disqualifier on its face** — but a **documented growth-capex explanation exists**: Canon's CapEx has risen every year shown (¥188,527M FY2022 → ¥272,771M TTM, +45%), driven explicitly by a new semiconductor-lithography-equipment plant at its Utsunomiya site — a ¥50 billion ($320M), 67,000m² facility, Canon's **first plant expansion in two decades**, intended to **triple lithography output** (300+ systems/yr across three fabs by 2027) to meet AI-driven semiconductor demand. Canon's own CEO is quoted describing this as capacity/growth investment ("It is our duty to strengthen our system to ensure a stable supply of equipment"), and independent reporting explicitly characterizes it as growth, not maintenance, capex. Sources: [movesilicon.com — "Canon bets on nanoimprint: new Japan fab targets advanced chipmaking"](https://movesilicon.com/news/canon-bets-on-nanoimprint-new-japan-fab-targets-advanced-chipmaking), [digitimes.com — "Canon builds first fab in 20 years to chase back-end boom"](https://www.digitimes.com/news/a20250804PD241/canon-ic-manufacturing-equipment-packaging-plant.html), Canon's own FY2025 results materials (`global.canon/en/ir/conference/pdf/conf2025e-note.pdf` — capex ¥262.2B in 2025 explicitly tied to "future growth," though the PDF itself could not be parsed as text this session and is cited via the WebSearch summary of its contents, not a direct quote). | **Does not fire — documented growth-capex carve-out applies.** |

No hard disqualifier fires. **This does not change the outcome** — see §3.3, where the weighted score alone fails the 80.0 gate by a wide margin regardless.

### 3.2 Sub-scores (all six, per the weighted formula)

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | Net Margin (TTM) = 308,125/4,659,984 = **6.61%** → NetMargin_Component = clamp((6.61/30)×100, 0, 100) = **22.04**. ROIC (TTM, `stockanalysis.com` directly-reported) = **7.71%** → ROIC_Component = clamp((7.71/30)×100, 0, 100) = **25.70**. Profitability_Score = (22.04 + 25.70)/2 = **23.87** (no FCF-positivity cap applied — already 5yrs positive, §3.1). | **23.87** |
| **Margins (15%)** | Gross Margin (TTM) = 2,166,321/4,659,984 = **46.49%**. GrossMargin_Score = clamp((46.49/80)×100, 0, 100) = **58.11**. Gross margin has ranged 45.3%–47.5% across FY2022–TTM (45.34% → 47.09% → 47.52% → 46.75% → 46.49%) — essentially range-bound, not a clean structural expansion, and moot regardless since it's already above the 40% threshold the +10 bonus is conditioned on ("even while below 40%"). No bonus applied. | **58.11** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 ¥4,031,414M → FY2025 ¥4,624,727M) = (4,624,727/4,031,414)^(1/3) − 1 = **4.68%**. Base = clamp((4.68/25)×100, 0, 100) = **18.74**. **+10 TAM-expansion modifier applied**, documented this session: network camera sales "more than doubled compared with 2021" (+~20% YoY most recently), semiconductor lithography systems sold **doubling** on AI-driven demand, medical segment sales growth **>5%/yr** post-pandemic, and Canon posting **all-time-high net sales for the second consecutive year** in 2025 with FY2026 sales guidance raised further (¥4.765T vs. ¥4.625T actual 2025) [Built In "Canon Inc. Company Growth, Stability & Outlook 2026"; Forbes/Canon BrandVoice "Canon Expands Its Next Phase Of Growth"]. **No −10 structural-deceleration modifier applied**: the one genuine deceleration signal found — the broader interchangeable-lens-camera (ILC) *industry* unit market projected to decline ~2.6% in 2026 as the DSLR→mirrorless conversion wave matures [PhotoWorkout "Camera Market Shares 2025"] — describes a market segment that is **not** Canon's growth driver (per the same sources, B2B: semiconductor/medical/network-camera is what's carrying consolidated growth) and consolidated revenue is not declining, unlike the EVO precedent where the declining segment (Europe) was that company's largest region and was dragging *consolidated* revenue below its prior-year peak. **Flagged as a judgment call nonetheless** — a reader weighting the camera-industry-wide unit decline more heavily could reasonably net this to 0 instead of +10, per the same transparency practice used in the 2026-07-24 EVO session. Growth_Score = **28.74**. | **28.74** |
| **Balance Sheet (15%)** | Net Debt/EBITDA (TTM, derived per §2.1) = 582,023/756,718 = **0.77×**. BalanceSheet_Score = clamp(100×(1 − 0.77/4), 0, 100) = **80.77**. | **80.77** |
| **Moat Signal (15%)** | See evidence table below — **1 of 5 signals** cleared the cited-evidence bar. (1/5)×100 | **20.0** |
| **FCF Quality (10%)** | FCF/NI (TTM) = 155,699/308,125 = **50.54%**. FCFQuality_Score = clamp(((0.5054 − 0.40)/0.60)×100, 0, 100) = **17.57**. (The growth-capex carve-out in §3.1 exempts this from being a hard *disqualifier*, but does not exempt it from scoring low on the continuous sub-score — both are correct simultaneously, per quality-scoring.md's own note: "a ratio below 70%... is a hard disqualifier, independent of this continuous score.") | **17.57** |

**Moat signal evidence (cited, per signal):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable/growing | **Cited, company-sourced.** Canon has held the **No. 1 global share of the interchangeable-lens digital camera market for 23 consecutive years** (2003–2025) [Canon Global press release, `global.canon/en/news/2026/20260224.html`]. | **TRUE** |
| Brand premium | **No supporting evidence found; evidence found points the opposite way.** No documented instance of Canon raising camera/imaging prices without volume loss was found. The one relevant data point found — Fujifilm's imaging-segment operating margin (~27%) is **nearly double Canon's (~14.5%)** in the same premium camera segment [PhotoWorkout] — cuts *against* crediting Canon with a pricing-power/brand-premium edge over its closest quality peer. | **FALSE** |
| Network effect | No documented two-sided-marketplace or usage-driven-value mechanism found for any Canon business line (cameras, printers, medical imaging, and semiconductor equipment are all single-sided hardware/equipment sales, not platforms). | **FALSE** |
| Switching costs | **Plausible but not Canon-specifically documented this session.** Semiconductor lithography equipment is well known industry-wide to create severe fab-integration lock-in (the cited example found, however, was **ASML's** lock-in, not a Canon-specific citation), and Canon's own materials describe a "design-in" collaborative product-development style with semiconductor customers — suggestive, but this session found no quantified, Canon-specific switching-cost figure (e.g. a dollar cost, a contract-value multiple, or a documented customer-retention statistic) of the kind the signal's evidence bar requires (contrast with EVO's cited €15–25M figure, or NET's cited Magic Transit/Zero Trust integration-depth mechanism). Not credited without a stronger citation, per "never mark a signal true without a cited source." | **FALSE** |
| Scale cost advantage | No cost-per-unit data vs. smaller competitors was found for any Canon segment this session. | **FALSE** |

Moat_Score = (1/5) × 100 = **20.0**

### 3.3 Final weighted Quality Score

```
Quality Score = (23.87 × 0.25) + (58.11 × 0.15) + (28.74 × 0.20) + (80.77 × 0.15) + (20.0 × 0.15) + (17.57 × 0.10)
              = 5.9675 + 8.7165 + 5.748 + 12.1155 + 3.000 + 1.757
              = 37.3045 → 37.3 (rounded to nearest 0.1)
```

**37.3 < 80.0 — fails the gate, by 42.7 points.** A decisive, not a close, miss. No sub-score is anywhere near its ceiling except Balance Sheet (80.77) — Profitability (23.87), Margins (58.11), Growth (28.74, even after the generous +10 modifier), Moat (20.0), and FCF Quality (17.57) are all weak-to-poor by this framework's standard. Canon reads as a mature, modestly-profitable, capital-intensive diversified-hardware conglomerate rather than a high-quality compounder: single-digit net margins (6.6%), single-digit ROIC (7.7%), slow consolidated top-line growth (4.7% 3yr CAGR even before any modifier), and only one of five Moat signals clearing this framework's cited-evidence bar.

**Sensitivity check** (holding Profitability, Margins, Balance Sheet, and FCF Quality fixed — none are discretionary judgment calls; each is a direct arithmetic result of the sourced financial data):

| Growth / Moat reading | Growth_Score | Moat_Score | Quality Score | Gate result |
|---|---|---|---|---|
| Most conservative (Growth modifier nets to 0 per the camera-industry-decline argument flagged in §3.2; Moat drops to 0/5 by also discounting Market Share as "not exclusive enough") | 18.74 | 0.0 | 33.0 | FAIL |
| Conservative (Growth nets to 0; Moat stays at 1/5) | 18.74 | 20.0 | 35.3 | FAIL |
| **Primary reading (this session)** | **28.74** | **20.0** | **37.3** | **FAIL** |
| Generous (also credit Switching Costs on the plausible-but-uncited semiconductor/medical lock-in argument → Moat 2/5) | 28.74 | 40.0 | 40.3 | FAIL |
| Maximally generous (credit Switching Costs AND Scale cost advantage → Moat 3/5, plus Growth modifier at its most generous +10 already applied) | 28.74 | 60.0 | 43.3 | **FAIL — still 36.7pts short** |

**The gate outcome is robust to every plausible reading of the discretionary inputs** — the ceiling of what CAJPY could plausibly score under this session's real, sourced data is 43.3, less than half the strict 80.0 bar. This is a genuinely decisive miss driven by structurally low profitability/ROIC and a thin Moat case, not a marginal judgment-call-dependent result the way the 2026-07-24 EVO session was (81.6, a 1.6-point pass).

### Result: **Phase 01 FAIL**

Per [operating-brief.md](../framework/operating-brief.md) and [quality-scoring.md](../framework/quality-scoring.md): a company scoring below 80.0 does not proceed to Phase 02. Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed.**

---

## 4. Recommendation

**FAIL — does not clear the Quality Score gate**, at **37.3 vs. the strict 80.0+ bar**, missing by 42.7 points, robust to every sensitivity checked (ceiling of 43.3 under the most generous defensible reading of every discretionary input). No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup were computed — that work is reserved for names that clear this framework's quality bar first.

Canon is a large ($23.5B market cap), profitable, financially conservative (net debt/EBITDA 0.77×, 5 consecutive years FCF-positive) global equipment maker with real, if modest, growth drivers in semiconductor lithography (AI-demand-driven, backed by a genuine ¥50B capacity expansion), medical imaging, and network cameras, plus an enduring #1 share in the camera market it originally built its brand on. But by this framework's specific bar for what counts as a "high-quality compounder," it falls well short on almost every axis that matters most: **Profitability (23.87) and ROIC (7.71%) are structurally single-digit** — a diversified hardware/equipment conglomerate margin profile, not a compounder's; **consolidated revenue growth is slow (4.68% 3yr CAGR)** even crediting the segment-level AI/semiconductor tailwind; and **only one of five Moat signals** (a genuinely durable #1 camera-market-share position) cleared this session's cited-evidence bar — brand premium is actually undercut by a smaller competitor's superior segment margin, and the plausible semiconductor/medical switching-cost story lacked a Canon-specific citation strong enough to credit.

The triggering post was a passing cashtag mention in a generic "earnings to watch" round-up, not a claimed fundamental event, and per Rule 9's non-negotiables, no action is warranted from the trigger itself.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Mechanical trigger:** Profitability (23.87) and FCF Quality (17.57), together 35% of total weight, are the two weakest sub-scores by a wide margin, both downstream of Canon's structurally single-digit net margin (6.6%) and ROIC (7.7%). A material, sustained step-change in either (e.g. a multi-year margin-expansion program, or the semiconductor/medical segments growing large enough within the consolidated mix to lift blended margins meaningfully) would be the most direct path to a materially different result — but even the maximally generous sensitivity check above only reaches 43.3, so no single input change closes this gap; it would take coordinated improvement across several sub-scores simultaneously.
- **Rule 9 events:** Canon's next earnings release (Q2/H1 2026 results, not yet confirmed as of this session — treat any earnings release as a standing Rule 9 trigger), a guidance revision, management change, material M&A, or a >15% stock-price move with no identified cause.
- Absent any of the above, future Telegram mentions of CAJPY should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## 7. Watchlist & Stale-Score Actions

- Created `watchlist/not-in-portfolio/CAJPY/CAJPY-2026-07-25.md` (first-ever entry for this ticker — nothing to supersede or mark stale).

---

## 8. Data Gaps Flagged (summary — none blocked scoring)

1. **`yfinance`/Yahoo Finance was unreachable this entire session** (`curl_cffi` SSL/connection-reset errors on both `CAJPY` and `7751.T`; a plain `curl` to Yahoo's own edge for a US mega-cap ticker returned HTTP 429) — the same recurring, session-wide Yahoo-side block pattern as every other 2026-07-24/2026-07-25 session (QCOM, EVO, COIN, HOOD, NET). Fundamentals sourced from `stockanalysis.com`'s Tokyo-listing pages instead. Flagging again for `/healthcheck` — now a multi-day, persistent pattern.
2. **Dividend yield discrepancy between IBKR (1.8%) and `stockanalysis.com` (3.65%)** for the CAJPY ADR — not reconciled this session; not load-bearing for the Quality Score gate (dividend yield is not a Quality Score input).
3. **EBITDA (TTM) was not directly disclosed** by `stockanalysis.com`'s ratios page — derived from the ratio of its reported EV/EBIT and EV/EBITDA figures (§2.1). Used only for the Balance Sheet sub-score, which passes comfortably (0.77×) even accounting for reasonable estimation error in this derived figure.
4. **The FY2025 results PDF (`global.canon/en/ir/conference/pdf/conf2025e-note.pdf`) could not be parsed as text** this session (returned as binary/corrupted content to the fetch tool) — the growth-capex narrative it was expected to corroborate was instead sourced from two independent secondary reports (movesilicon.com, digitimes.com) that were successfully parsed and both independently confirm the same Utsunomiya-plant/growth-capex facts.
5. **Two genuine judgment calls flagged and stress-tested** (§3.2 Growth modifier net-zero-vs-+10 argument; §3.3 Moat signal count for Switching Costs) — shown in the sensitivity table not to change the FAIL outcome under any combination tested.

None of these gaps blocked scoring — every required Phase 01 input was ultimately obtained and cross-checked, and the flagged judgment calls were shown not to affect the final FAIL result.

---

## Glossary

- **ADR (American Depositary Receipt)** — see [glossary.md](../framework/glossary.md).
- **Sponsored ADR / Unsponsored ADR** — see [glossary.md](../framework/glossary.md). CAJPY is confirmed sponsored (IBKR contract description: "CANON INC-SPONS ADR").
- **CAGR (Compound Annual Growth Rate)** — see [glossary.md](../framework/glossary.md).
- **EBIT / EBITDA** — see [glossary.md](../framework/glossary.md).
- **Form 20-F / Form 6-K** — see [glossary.md](../framework/glossary.md). Canon's SEC filing forms as a foreign private issuer.
- **Gross Margin** — see [glossary.md](../framework/glossary.md).
- **Hard disqualifier** — see [glossary.md](../framework/glossary.md).
- **IFRS (International Financial Reporting Standards)** — see [glossary.md](../framework/glossary.md).
- **Moat** — see [glossary.md](../framework/glossary.md).
- **Net Debt/EBITDA** — see [glossary.md](../framework/glossary.md).
- **Net Margin** — see [glossary.md](../framework/glossary.md).
- **Phase 01–06** — see [glossary.md](../framework/glossary.md).
- **Quality Score** — see [glossary.md](../framework/glossary.md). CAJPY scores 37.3.
- **ROIC (Return on Invested Capital)** — see [glossary.md](../framework/glossary.md).
- **Rule 0** — see [glossary.md](../framework/glossary.md).
- **Rule 9** — see [glossary.md](../framework/glossary.md).
- **TAM (Total Addressable Market)** — see [glossary.md](../framework/glossary.md).
- **TTM (Trailing Twelve Months)** — see [glossary.md](../framework/glossary.md).

No new terms coined this session — all jargon used already exists in [framework/glossary.md](../framework/glossary.md).

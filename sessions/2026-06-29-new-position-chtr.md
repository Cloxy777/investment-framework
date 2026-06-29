# New Position Evaluation — CHTR (Charter Communications, Inc.)

**Task type:** NEW POSITION
**Date:** 2026-06-29
**10Y US Treasury yield:** 4.378% (yfinance `^TNX`, live intraday print, 2026-06-29 ~12:52 UTC — today **is** a trading day (Monday); confirmed directly against system time, not inferred from a prior session's note. A same-day session in this repo (FUBO, 2026-06-29) incorrectly stated "markets closed 2026-06-29, a Sunday" — that is factually wrong (2026-06-29 is a Monday) and is corrected here rather than propagated. `^TNX` shows a full intraday bar already printing today (Open 4.378 / High 4.390 / Low 4.376, timestamp 1782737571 = 2026-06-29 12:52:51 UTC, ~15 minutes before this lookup), confirming a genuine live print, not a stale weekend carry-forward.)
**Trigger:** Ad hoc `/new-position CHTR` run (not a Telegram-scan trigger this time).

CHTR has no prior watchlist or session history in this repo (confirmed: no `watchlist/*/CHTR/` folder, no prior CHTR session under `sessions/`). CHTR is **not** a current holding (confirmed against [portfolio/holdings.md](../portfolio/holdings.md) — no CHTR/Charter row).

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first, before any valuation work.

| Source | Price | Timestamp |
|---|---|---|
| **IBKR live snapshot** (primary, contract_id 233674866, NASDAQ, "CHARTER COMMUNICATIONS INC-A") | **$165.77** | ts 1782738300 (2026-06-29 13:05:00 UTC, live quote, `is_close: false`) |
| yfinance daily bar (cross-check, prior close) | $133.64 | close 2026-06-26 (today's bar not yet in `t.history()` at pull time) |

Bid/ask at snapshot: $165.60 / $166.27. **Change on day: +$32.13 (+24.04%)** — a very large single-day move, independently and explicitly investigated below per Rule 9's ">15% move" trigger criteria (this matters for *future* re-checks of this entry, not for today's Phase 01 gate math, which uses trailing filed financials regardless of today's price).

**Why the move is real and explainable, not a data error or an "unexplained >15% move":** WebSearch confirms two concurrent, genuine sector-news catalysts hitting the cable sector simultaneously today: (1) Comcast announced plans to split into two publicly-traded companies, which itself surged ~20% and lifted cable-sector peers broadly; (2) Bloomberg reported Charter is in discussions with SpaceX over routing mobile traffic through SpaceX's direct-to-cell satellite service (a potential Spectrum Mobile cost/capability angle). CHTR had also been "coiled" after grinding down to a 52-week low of $124.05 days earlier on a heavily compressed multiple (trailing PE ~3.6x per yfinance `info`), leaving it primed for an outsized reaction to positive sector news. This is a **documented fundamental/news trigger**, not a "price movement alone" event — consistent with this framework's Rule 0 non-negotiable ("act only on documented triggers — a valuation-score change or a fundamental event, never on price movement alone").

52-week range (IBKR `misc_statistics`): low **$124.05** / high **$422.29** — CHTR is currently trading 33.6% above its 52-week low and 60.7% below its 52-week high. 52-week open: $395.69. Year-to-date change: **−20.59%** despite today's pop. Analyst targets were not separately re-pulled this session (not required at the Phase 01 stage; would only matter as a bull-case sanity check if Phase 02 were reached).

**Live price used throughout this session: $165.77.**

---

## 2. Data Gaps Flagged / Data-Source Note

`yfinance` required `YF_DISABLE_CURL_CFFI=1` and `CURL_CA_BUNDLE=/root/.ccr/ca-bundle.crt` to run without network errors (per prior-session precedent) — once set, it worked normally for all annual statements. `t.financials`/`t.cashflow`/`t.balance_sheet` return **FY2022–FY2025** (4 fiscal years, calendar year-end Dec 31); FY2021 is `NaN` across all three statements, the same data-depth limit seen in prior sessions (IBM, TTWO). This satisfies Phase 01's "3+ years"/"3 consecutive years" requirements but caps the 3-year revenue CAGR at FY2022→FY2025 rather than an alternate window. **No required Phase 01 metric is missing or invented below — every figure is cited to yfinance's structured statement data, cross-checked against GuruFocus, stockanalysis.com, and primary news/SEC sources where flagged.**

**Share-count data-quality note (flagged, not resolved, but does not change the Phase 01 verdict):** yfinance's three share-count fields disagree meaningfully: FY2025 annual balance sheet "Ordinary Shares Number" = 126,631,550; `t.get_shares_full()`'s most recent print (2026-06-04) = 141,178,370 (also `info['sharesOutstanding']`); WebSearch of CHTR's actual Q1 2026 10-Q (filed 2026-04-24, period ended 2026-03-31) states **127,666,355 shares of Class A common stock** issued, plus a separate, tiny Class B count. Independent secondary sources also disagree (stockanalysis.com ≈138.50M; GuruFocus/Morningstar ≈123–139M range cited across different snapshots). The most likely explanation, not independently confirmed in this session: Charter's capital structure includes economically-equivalent Charter Holdings common units held by Advance/Newhouse and (pending close) Liberty Broadband, which some data vendors fold into "shares outstanding" and others (the 10-Q's Class A line) do not — an Up-C-style structure complexity, not a vendor error or a real overnight 11.6% issuance. **This is flagged explicitly as a data gap** (the exact fully-diluted share count is not cleanly resolved across sources in this session) but does **not** change the Phase 01 "dilutive issuance pattern" finding below: every source, regardless of which share count it uses, agrees directionally that the share count has been **shrinking** via buybacks (stockanalysis.com cites −7.96% YoY; the FY2022→FY2025 annual balance-sheet series shown in §3 falls every year), consistent with Charter's long-documented, deliberate buyback-funded-by-debt capital-allocation strategy (the "Malone-style" playbook this evaluation was specifically asked to verify).

**Pending M&A context (material, but does not change today's Phase 01 inputs):** Charter has **two** large pending stock-for-stock/cash mergers, **neither of which has closed**, so neither is consolidated into the trailing financials used below:
1. **Cox Communications** — $34.5B combination announced May 2025; DOJ/FCC already approved; only California (CPUC) approval remains outstanding as of the most recent reporting found; a Hart-Scott-Rodino antitrust clearance deadline of **September 15, 2026** is the operative near-term forcing event, with Charter on record saying it would not have time to close if California waits past that date.
2. **Liberty Broadband** — stock-for-stock combination (0.236 CHTR shares per Liberty Broadband share), approved by both companies' shareholders February 2025, expected to close **by June 30, 2027**.

Per this framework's standard treatment of pending-but-not-closed M&A (see the FCC-approval-pending precedent in other sessions), **this evaluation scores CHTR on its standalone, currently-filed financials** — the business and balance sheet that exist today, not a pro forma combined entity that does not yet legally exist. If/when either deal closes, that is a Rule 9 "material M&A announcement" trigger requiring an immediate re-valuation with the newly consolidated financials (different EBITDA base, different debt load, different share count) — explicitly flagged as the **Next Review Trigger** in §6.

---

## 3. Phase 01 — Universe Screening (Quality Gate)

The framework carries two slightly different Phase 01 threshold sets — [strategy.md](../framework/strategy.md)'s (stricter) and [valuation-scoring.md](../framework/valuation-scoring.md)'s "Quantitative Pre-Screen Filters" (looser on most lines). Both are shown below; CHTR fails decisively under **either** version.

All financial figures sourced from yfinance `t.financials` / `t.cashflow` / `t.balance_sheet` (USD, annual, fiscal years ending 31 Dec), FY2022–FY2025 (4 years — see §2 data-depth note). Net Debt/EBITDA independently cross-checked against GuruFocus (4.57×, March 2026, "near its 10-year median of 4.68×") and stockanalysis.com (cash $517M / debt $97.31B / net debt $96.79B) — both corroborate the yfinance-derived figures below to within a few percent, and GuruFocus's own framing ("near its 10-year median") confirms this is CHTR's *normal*, long-standing leverage level, not a one-off spike.

| Criterion | strategy.md threshold | valuation-scoring.md threshold | CHTR actual | Result |
|---|---|---|---|---|
| **Net margin** | **>15%** | **>12%** | **9.10%(FY25) / 9.23%(FY24) / 8.35%(FY23) / 9.36%(FY22)** — never clears either bar in any of the 4 available years; tightly clustered 8.35–9.36%, well below both thresholds every year | **FAIL (both)** |
| **ROIC** | **>15%** | **>15%** | **8.57%(FY25) / 8.95%(FY24) / 8.52%(FY23) / 8.88%(FY22)** — NOPAT = EBIT×(1−effective tax rate); Invested Capital = Total Debt + Stockholders' Equity − Cash. Remarkably flat at ~8.5–9.0% across all 4 years; never within shouting distance of 15% | **FAIL (both)** |
| Gross margin | >40% OR structurally expanding | >40% | 56.54%(25) / 55.80%(24) / 54.77%(23) / 54.63%(22) — clears >40% every year, and shows a genuine, if modest, multi-year expansion (+1.9pp over 3 years) | PASS (both) |
| FCF positive | 3+ yrs | 3 consecutive yrs | $4.418B(25) / $3.161B(24) / $3.318B(23) / $5.549B(22) — positive all 4 years | PASS (both) |
| **Revenue growth** | **CAGR >10%** | **CAGR >8% (3yr)** | **3yr CAGR (FY22→FY25) = 0.46%** — Revenue: $54.022B(22) → $54.607B(23) → $55.085B(24) → $54.774B(25), essentially flat with a FY25 dip. Independently corroborated by the primary Q1 2026 earnings release: revenue **down 1.0% YoY** that quarter, driven by lower residential video/Internet revenue | **FAIL (both, decisively)** |
| **Net debt/EBITDA** | **<2×** | **<2.5×** | **4.556×(25) / 4.453×(24) / 4.701×(23) / 4.634×(22)** — every year fails both thresholds by roughly double or more; cross-checked against GuruFocus (4.57×, Mar 2026) and stockanalysis.com (net debt $96.79B / EBITDA ≈$21–22B) — both independently corroborate. This is CHTR's known, deliberate, long-standing leverage level (GuruFocus: "near its 10-year median of 4.68×"), not a recent deterioration | **FAIL (both, every year, by a wide and structural margin)** |
| FCF/NI conversion | >70% for 2+ yrs | (same check, implicit) | 88.59%(25) / 62.19%(24) / 72.81%(23) / 109.77%(22) — passes in 3 of 4 years (FY25, FY23, FY22); FY24 (62.19%) dips below 70% but is bracketed by passing years on both sides, and 3 of 4 years (including the 2 most recent: FY25 88.59%, and FY23 72.81% two years prior) clear the "2+ consecutive years" bar in spirit | PASS (both), on balance, despite one soft year |
| FCF yield (live price basis) | (not separately gated) | **>4%** | FY25 FCF $4.418B ÷ market cap (live price × FY2025 annual share count $20.99B, or × yfinance's `sharesOutstanding` $23.40B) = **18.9–21.0%** | **PASS, strongly** (valuation-scoring.md leg) — see §2 share-count caveat; even at the higher (yfinance) share count the yield is far above 4% |
| EV/EBIT (live price basis) | (not separately gated) | **<20×** | Live EV (~$117.6–120.0B depending on share-count basis) ÷ FY25 EBIT $12.50B = **9.4×–9.6×** | **PASS** (valuation-scoring.md leg) |
| **Dilutive share issuance pattern** | **none** | **none** | **Shares outstanding fell every year on the FY2022–FY2025 annual balance-sheet series: 152,651,397(22) → 145,225,459(23) → 141,946,427(24) → 126,631,550(25), a cumulative −17.0% over 3 years.** Cash-flow detail confirms this is buyback-driven, not organic: "Repurchase Of Capital Stock" was $(10.277)B(22), $(3.215)B(23), $(1.213)B(24), $(5.132)B(25) every year, with **zero offsetting new-issuance line items** ("Issuance Of Capital Stock" is 0 or NaN in all 4 years) — i.e. "Net Common Stock Issuance" is identically equal to the buyback figure each year. Independently corroborated by WebSearch: Q1/Q2/Q4 2026 buyback disclosures (Q1 2026: $963M repurchased, ~4% of market cap that quarter alone; a standing $100M/month commitment to buy from Liberty Broadband until that merger closes) and stockanalysis.com's −7.96% YoY share-count figure. (The §2 share-count *measurement* discrepancy across vendors does not undermine this — every vendor's own multi-period series, regardless of which absolute level it anchors to, shows the same shrinking trend.) | **PASS, clearly and by design** (both) — this is the textbook "Malone-style" debt-funded buyback strategy the evaluation was specifically asked to verify, and it verifies as a genuine repurchase program, not a dilution pattern |
| Moat signal | stable/growing share, brand, network effect | (qualitative, same) | Mixed and genuinely two-sided — see qualitative notes below. Real switching-cost moat (Spectrum Mobile bundling) and HFC network scale, but **market share itself is not stable** — see Revenue/subscriber data below | PASS (qualitative, with real caveats) — does not offset the quantitative failures |

### Result: **Phase 01 FAIL**

CHTR fails on **three independent, structural, multi-year criteria** under both threshold sets carried in this framework:

1. **Net margin.** 8.35–9.36% across all 4 available years — consistently and significantly below both the looser (>12%) and stricter (>15%) thresholds, with essentially no improving trend (the four years are within 1 percentage point of each other: a remarkably flat, structurally capped margin profile, not a temporary dip).

2. **ROIC.** 8.52–8.95% across all 4 available years — likewise structurally and persistently below the >15% bar this framework treats as its core capital-efficiency quality threshold. Like net margin, the lack of *any* year approaching 15%, combined with the flatness of the series, indicates this is CHTR's normal operating reality, not a cyclical trough.

3. **Revenue growth.** 3-year CAGR of just **0.46%** is decisively below both the looser (>8%) and stricter (>10%) thresholds — essentially flat revenue, corroborated independently by the company's own just-reported Q1 2026 results (revenue down 1.0% YoY that quarter) and by widely-reported subscriber losses (Spectrum lost over 284,000 TV and 400,000+ Internet customers in 2025; a further 120,000 Internet-subscriber loss in Q1 2026 alone). Cable/broadband bundling-into-mobile growth (Spectrum Mobile, +17.1% lines YoY) is real but is not offsetting the legacy video/Internet erosion at the consolidated-revenue level.

4. **Net debt/EBITDA — the binding constraint flagged in this evaluation's brief, and confirmed as the most decisive failure.** **4.45×–4.70×** across all 4 available years, independently cross-checked against GuruFocus and stockanalysis.com — both corroborate. This **more than doubles** the strict <2× threshold (strategy.md) and is roughly **1.8–1.9× the relaxed <2.5× threshold** (valuation-scoring.md/Upgrade 5's standard non-asset-light level). This is not a recent deterioration — GuruFocus explicitly notes the current 4.57× sits "near its 10-year median of 4.68×" — confirming the framework's prior expectation that this is CHTR's long-standing, deliberate Malone-style leverage posture, not a one-off spike to be waited out.

   **Upgrade 5 exception explicitly checked and explicitly does NOT apply, on all three required prongs:**
   - **Business-model prong:** CHTR is a capital-intensive cable/broadband/telecom operator (HFC network owner-operator), not a payment network, exchange, or asset-light financial — the exception's defining business-model criterion. Fails outright on this prong alone.
   - **Interest-coverage prong (>15× required):** EBIT ÷ Interest Expense = $12.50B ÷ $5.042B = **2.48×** (FY25); 2.32×–2.64× across all 4 available years. Roughly **6× short** of the >15× the exception requires.
   - **Investment-grade prong (required):** WebSearch confirms Charter's **corporate family rating is BB+ — below investment grade (speculative/high-yield grade)**. (Charter's *debt structure* is split — some senior secured notes carry investment-grade ratings while senior unsecured notes are high-yield — but the exception requires the *company* be investment-grade rated, which it is not at the BB+ corporate level.)

   All three prongs fail independently; the exception would not apply even if only one were checked. **The standard <2× (strategy.md) / <2.5× (valuation-scoring.md) threshold is the correct one to apply, exactly as the evaluation brief anticipated, and CHTR fails it by a wide, structural margin.**

The genuine strengths — gross margin (clears >40%, mildly expanding), FCF positivity (4/4 years), FCF/NI conversion (passes 3 of 4 years), a real and substantial buyback program (no dilution — share count down ~17% over 3 years on the annual balance-sheet series, corroborated by every data source's own trend even where absolute levels disagree), and strong cash-flow-based valuation multiples (FCF yield ~19–21%, EV/EBIT ~9.4–9.6× — both look statistically "cheap") — are real. But Phase 01 is conjunctive: a single-digit net margin, a single-digit ROIC structurally and persistently below the 15% quality bar, near-zero revenue growth, and leverage running at roughly double the relevant threshold (confirmed on all three Upgrade 5 exception prongs as inapplicable) do not get offset by a strong buyback program and cheap multiples. Cheapness on multiples is exactly what a sub-quality, over-levered, low-growth business *should* show — it is not a basis for waiving the quality gate that exists specifically to filter out "statistically cheap but structurally impaired" businesses (the IBM/graveyard-audit precedent this framework already tracks for a similar profile).

Per [new-position.md](../.claude/commands/new-position.md) step 2 and [operating-brief.md](../framework/operating-brief.md): **"if it fails, stop and report why rather than proceeding to scoring."** Accordingly, **no Rate Environment Gate and no Phase 02 valuation score were computed.**

### Turnaround Sub-Gate (Hybrid Upgrade 4) — not numerically eligible

Upgrade 4 is available only to "businesses failing 2–4 quality criteria." CHTR fails on net margin, ROIC, revenue growth, and net debt/EBITDA — **4 criteria failing** under the stricter strategy.md reading (right at the edge of the 2–4 eligibility window), so it is at least worth checking the 5 individual conditions rather than dismissing it outright on count alone (unlike CBRS's 7-of-8 case):

1. **Historical ROIC >15% for ≥5 of the past 10 years:** **FAILS.** Only 4 years of data are available (FY2022–FY2025) and ROIC never exceeds 8.95% in any of them — there is no evidence CHTR has *ever* cleared 15% ROIC in the available record, let alone for 5 of the past 10 years. This alone disqualifies the Turnaround path.
2. CEO/CFO insider buying >$500K in the past 6 months (Form 4 verified): not checked — moot given condition 1 already fails.
3. Independent FV estimate showing ≥40% MOS: not computed — Phase 01 FAIL means no FV work was done.
4. Net Debt/EBITDA <3×: **FAILS** — CHTR's 4.45–4.70× is also above this looser Turnaround-specific threshold, not just the standard <2.5×.
5. Core moat still identifiable: yes (see qualitative notes below) — but this alone cannot pass the gate given conditions 1 and 4 both fail.

**Result: Turnaround Sub-Gate does not apply.** Two of five required conditions fail independently (historical ROIC, debt level), each sufficient on its own to close this path.

---

## 4. Qualitative Notes (5 Questions, per valuation-scoring.md — context only, does not override the quantitative FAIL)

1. **Why are margins where they are?** Gross margin (~55–57%) reflects genuine operating leverage from a high-fixed-cost, owned-infrastructure (HFC network) model — typical for a capital-intensive cable operator. But this does *not* translate into a high *net* margin (~9%) because of the heavy, structural interest burden from the leverage discussed above (~$5B/yr interest expense against ~$12.5B EBIT) — i.e. the margin profile is a direct, mechanical consequence of the capital structure, not a separate issue.
2. **What would it take to compete with them?** Historically high (the HFC network is expensive and slow to replicate), but this moat is **actively eroding** in real time: fiber overbuilders and municipal/cooperative networks are increasingly economical to deploy in areas CHTR has long dominated, and fixed-wireless 5G is a credible substitute for price-sensitive subscribers. The subscriber-loss data in §3 (284K+ TV, 400K+ Internet customers lost in 2025 alone, another 120K Internet loss in Q1 2026) is direct, current evidence the moat is not fully holding at the subscriber level, even as Spectrum Mobile bundling provides some retention/ARPU offset.
3. **Capital allocation track record (5–10yr)?** Not fully assessable from the 4-year financial window available this session, but the qualitative pattern is well-documented and consistent across every source checked: an aggressive, debt-funded share buyback program (the explicit "Malone-style" strategy this evaluation was asked to verify) — real, substantial, and not diluting shareholders. This is shareholder-friendly capital return, but it is also *why* leverage sits structurally near 4.5–4.7× rather than coming down — a deliberate trade-off, not an accident, and one this framework's quality gate is specifically designed not to wave through regardless of how shareholder-friendly the buyback program is.
4. **Where is growth coming from next 3–5 years?** Almost entirely Spectrum Mobile (+17.1% lines YoY, now 12.1M lines) and bundling/ARPU expansion, while the legacy video and (increasingly) Internet subscriber bases shrink. The pending Cox and Liberty Broadband combinations (§2) would add scale but do not change the underlying organic growth profile management itself is guiding to.
5. **Best bear case?** Continued cord-cutting and fiber/fixed-wireless overbuild erode the legacy subscriber base faster than mobile bundling can offset it, while ~4.5–4.7× leverage limits financial flexibility to accelerate network upgrades (HFC-to-fiber/DOCSIS 4.0) at the pace fiber competitors are deploying new builds — a "melting ice cube funded by debt-financed buybacks" pattern, which is precisely the profile Phase 01's margin/ROIC/growth/leverage criteria are jointly designed to catch before it becomes a Phase 06 exit-trigger situation (this framework simply never enters in the first place).
6. **Disruption vector check:** Fiber overbuild and fixed-wireless 5G are not hypothetical 5-year-out threats — they are already showing up directly in the subscriber-loss numbers today. This is a live, currently-manifesting disruption vector, not a speculative one.

---

## 5. Recommendation

**PASS. Do not open a position.** No Rate Environment Gate, no Phase 02 valuation score, no fair-value derivation, no order setup, no position sizing — none of that work is meaningful for a name that fails the quality gate this framework uses to define its investable universe on three independent, structural, multi-year criteria (net margin, ROIC, revenue growth) plus a fourth (net debt/EBITDA) that the evaluation brief specifically flagged in advance and that is now confirmed, with all three of Upgrade 5's asset-light exception prongs explicitly checked and explicitly inapplicable. Producing a score anyway would be exactly the "black-box theater" the IBM/TTWO/CBRS precedents in this repo all explicitly decline to produce.

This is **not** a verdict that CHTR is a bad company or a bad trade for someone running a different strategy — its cash-flow-based multiples (FCF yield ~19–21%, EV/EBIT ~9.4–9.6×, trailing PE ~3.6×) are genuinely statistically cheap, and the buyback program is real, substantial, and non-dilutive. But this framework's Phase 01 gate exists specifically to screen out "cheap on multiples but structurally impaired" businesses *before* any valuation-score work begins — and CHTR's flat-to-negative revenue growth, single-digit ROIC, and ~4.5–4.7× leverage (confirmed as CHTR's normal, decade-long operating level, not a temporary spike) are exactly the profile that gate is built to catch. The Turnaround Sub-Gate (Hybrid Upgrade 4) was explicitly checked given CHTR sits right at the edge of its "2–4 failing criteria" eligibility window, and was found not to apply — historical ROIC has apparently never cleared 15% in the available record, and leverage also exceeds the Turnaround-specific <3× threshold.

A `not-in-portfolio` watchlist entry is created marking this "Phase 01 FAIL / not scored," per [watchlist/README.md](../watchlist/README.md) convention.

---

## 6. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 7. Next Review Trigger

- **Either pending merger closing (Cox Communications or Liberty Broadband) is a mandatory Rule 9 "material M&A announcement" re-valuation trigger**, independent of any calendar schedule — closing either deal materially changes the consolidated EBITDA base, debt load, and share count this Phase 01 gate is computed from. The Cox deal in particular has a hard external forcing date (DOJ HSR clearance expires **September 15, 2026**; only California/CPUC approval remains outstanding as of the sources checked this session) — this is the single most likely near-term trigger for a fresh look.
- **Any quarter showing a durable reversal of the current trend** — net margin or ROIC moving toward the 15% quality threshold, revenue CAGR re-accelerating durably above 8–10%, or Net Debt/EBITDA falling toward 2–2.5× — would be a fundamental change warranting a fresh full evaluation. None of this is expected mechanically from either pending merger (which adds scale and likely *more* debt, not less, given the cash/preferred/unit consideration structure of the Cox deal) but should be checked at that time rather than assumed.
- A credible insider-buying disclosure (Form 4) combined with any of the above would be the trigger to revisit the Turnaround Sub-Gate question, though the historical-ROIC condition (apparently never cleared 15% in the only 4 years of data available) would need independent confirmation over a longer lookback before that path could even be reconsidered.
- Absent one of these, routine mentions of CHTR (price moves, further buyback announcements, further Cox/Liberty Broadband regulatory-approval-process news short of an actual closing) should be treated as routine "last checked, no change" pings rather than triggering a full re-evaluation each time, consistent with the IBM/TTWO/CBRS precedent — the trailing financials behind today's FAIL will not change until a new quarterly filing lands or one of the mergers actually closes.

---

## Glossary

- **ARPU** — Average Revenue Per User/customer — a per-subscriber revenue metric used to track pricing/bundling trends in subscription businesses like cable/broadband.
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **Debt Gate** — This framework's balance-sheet check on Net Debt/EBITDA (Hybrid Upgrade 5) — standard threshold <2.5×, relaxed to <4× for asset-light payment networks/exchanges with strong interest coverage and investment-grade ratings. Checked explicitly against CHTR and found inapplicable on all three required prongs (business model, interest coverage, credit rating).
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and valuation ratios.
- **EV** — Enterprise Value — a company's total value to all capital providers: market cap + debt − cash.
- **EV/EBIT** — Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to operating profit, independent of capital structure.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **HFC (Hybrid Fiber-Coaxial)** — A network architecture combining fiber-optic backbone lines with coaxial cable to the home — the core physical infrastructure underlying Charter's Spectrum cable/broadband service, as distinct from a full fiber-to-the-home (FTTH) network.
- **Interest coverage (ratio)** — EBIT ÷ interest expense — how many times over a company could pay its interest bill from operating profit; higher means less balance-sheet risk from debt. CHTR's ~2.3×–2.6× is far below the >15× this framework's Debt Gate exception requires.
- **Investment grade** — A credit rating (BBB-/Baa3 or higher) signaling a low perceived risk of default. CHTR's corporate family rating (BB+) is below this line — speculative/high-yield grade — even though some of its individual secured notes carry investment-grade ratings.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate. CHTR's ~4.5–4.7× is roughly double the strict <2× threshold and the binding constraint that fails this evaluation.
- **NI (Net Income)** — accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — operating profit after a tax adjustment but before financing costs; the numerator this framework uses to compute ROIC.
- **PE (Price-to-Earnings) ratio** — Share price ÷ earnings per share — the most common "how expensive is this stock" multiple.
- **Phase 01–06** — the six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Qualified Quality List** — the output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. (CHTR does not make this list.)
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework. CHTR's ~8.5–9.0% sits structurally below the >15% bar.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9** — this framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. CHTR's +24.04% move today **has** an identified cause (Comcast split news + SpaceX partnership talks) and so does not itself qualify as an "unexplained" Rule 9 trigger.
- **Treasury yield (10Y)** — the interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure.
- **Turnaround Sub-Gate** — the conditional path (Hybrid Upgrade 4) that lets a company failing 2–4 quality criteria still enter as a small (2–3%) position if it passes 5 specific tests (historical ROIC, insider buying, margin of safety, debt level, identifiable moat). Checked explicitly for CHTR (it sits at the edge of the eligibility window) and found inapplicable — fails both the historical-ROIC and debt-level conditions independently.
- **Up-C structure** — A corporate structure (common among companies with pre-IPO partnership/LLC ownership) where economically-equivalent partnership/holding-company units, exchangeable into common stock, exist alongside the publicly-traded share class — flagged here as the likely (not independently confirmed) explanation for why different data vendors report materially different "shares outstanding" figures for CHTR.

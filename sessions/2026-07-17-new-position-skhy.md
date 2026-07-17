# NEW POSITION — SKHY (SK Hynix Inc. — Nasdaq-listed sponsored ADR) — 2026-07-17

**Task type:** NEW POSITION (first-ever evaluation — Telegram-scan trigger, Routine 6)
**Date:** 17 Jul 2026
**Ticker / instrument:** SKHY (IBKR contract_id **899700992**, exchange NASDAQ, description "SK HYNIX INC", country_code US) — confirmed via `search_contracts` as an **exact symbol match**. Explicitly **not** SKHZ ("Leverage Shares 1x Short SKHY," a leveraged/inverse derivative on BATS) or SKUU ("Granite 2x Long SKHY ETF," a leveraged ETF on NASDAQ) — both returned by the same search and excluded.
**Sector:** Memory semiconductors — DRAM, NAND flash, and HBM (High-Bandwidth Memory, the premium stacked-DRAM format used in AI accelerator GPUs). Same commoditized, boom-bust hardware-cycle category as MU (Micron), evaluated in this framework's 2026-06-20/06-22/06-24/07-08 sessions.
**Current portfolio weight:** 0% — not held, no prior watchlist entry (confirmed via glob of `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` — no `SKHY/` folder existed before this session).

---

## 0. Why this session exists — trigger source

Telegram channel `https://t.me/myroslavkorol`, post `myroslavkorol/2580` (~06:40 UTC, 2026-07-17): a repost embedding a YouTube video titled *"№411: Падіння IBM на 25%. Ризики по виробникам чіпів пам'яті: Micron, Sandisk, SK hynix"* ("#411: IBM's 25% Fall. Risks for Memory Chip Manufacturers: Micron, SanDisk, SK hynix"). SK Hynix is named as one of three memory-chip manufacturers under a discussed "risk" framing — no specific price or financial claim. Per the operating brief, **the Telegram post/video title is a trigger only, never financial data** — nothing from it is used in any calculation below. Because no watchlist entry for SK Hynix/SKHY existed, this is a first-ever evaluation, run per this repo's established precedent for first-ever-mention tickers (e.g. `sessions/2026-07-16-new-position-mtch.md`, `sessions/2026-07-16-new-position-smr.md`).

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$146.99** (last trade) | IBKR `get_price_snapshot`, contract_id 899700992, ts 2026-07-17 08:24:25 UTC |
| Bid / Ask | $146.88 / $146.97 | Same snapshot |
| Prior close | $152.31 | IBKR `prior-close` |
| Today's change so far | **−$5.32 / −3.49%** | IBKR `change` |
| 5-day price history (IBKR, daily bars, RTH) | 10 Jul: O170.00 H177.00 L166.19 C168.01 · 13 Jul: O152.62 H162.28 L151.30 C152.35 · 14 Jul: O168.11 H194.80 L165.50 C193.92 · 15 Jul: O181.81 H187.95 L166.48 C176.46 · 16 Jul: O165.82 H168.20 L151.38 C152.31 | IBKR `get_price_history`, ONE_MONTH/ONE_DAY |
| `misc_statistics` 52-week range | High $194.80 (13w/26w/52w — set 14 Jul), Low $151.30 (13w/26w/52w — set 13 Jul), Open-52w $170.00 | IBKR snapshot — **flagged as stale below** |
| IPO price (10 Jul 2026) | $149.00 per ADS (177.9M ADSs sold, $26.5B raised) | WebSearch, corroborated by CNBC/Yahoo Finance/TheStreet coverage of the listing |

**Data-integrity flag:** today's live price ($146.99) is **below** the `misc_statistics` 52-week low ($151.30) returned in the same snapshot — that field is a lagging, not-yet-refreshed statistic (last computed off the 13 Jul session low), not a live figure. Today's $146.99 is a new post-listing low, now **below the $149.00 IPO price** just seven trading days after the 10 Jul 2026 debut, having spiked as high as $194.80 (14 Jul) in between. This is an extraordinarily volatile five-trading-day price history for a $26.5B listing — treated as important context (§2.2), not smoothed over.

---

## 2. Special complication: what SKHY actually is, and the ADR-premium dislocation

### 2.1 Instrument structure — resolved, not a data-sourcing dead end

The task brief flagged a real risk: that SKHY might be a thin, non-SEC-reporting depositary vehicle with no independently sourceable financials. **Investigated and ruled out** — SKHY is a **sponsored** American Depositary Receipt (ADR/ADS; 1 ADS = 0.1 Korean ordinary share, i.e. 10 ADSs = 1 KRX:000660 common share), listed 10 Jul 2026, that:

- **Replaced a thin, unsponsored OTC program** (ticker HXSCL) that traded independently of the company and carried no SEC reporting obligation — this is the "unsponsored ADR" risk the task brief anticipated, but it describes the *pre-2026-07-10* situation, not the current SKHY listing.
- **Was registered with the SEC via a Form F-1**, and its final prospectus — **Form 424B4**, filed and confirmed on SEC EDGAR (CIK 0002120882, accession `000119312526299963`) — contains **full audited consolidated IFRS financial statements for FY2023, FY2024, and FY2025**, plus unaudited Q1 2026/Q1 2025 interim statements. This is the primary source for every Quality Score input below.
- **Carries ongoing periodic SEC reporting** as a foreign private issuer — Form 6-K filings already on record post-listing (e.g. a Q2 2026 earnings-call-schedule 6-K, a 6-K on a 17.79M-share capital increase), consistent with standard foreign-private-issuer obligations (Form 20-F annual report expected once a full fiscal year post-listing has closed).

**Conclusion: SKHY is Rule-0-compliant SEC-sourced data, not a data gap.** DART (Korea's FSS disclosure system) was not needed as a fallback — flagged in the Glossary as available if a future SKHY data point is only in SK Hynix's Korean, not SEC, filings.

### 2.2 The complication that *does* apply: extreme ADR-premium dislocation (price-integrity flag)

- SK Hynix's Korea Exchange-listed ordinary shares (**KRX:000660**) suffered a **15.4% single-day plunge on 13 Jul 2026** — the stock's biggest one-day drop ever, triggering a market-wide KOSPI circuit breaker/trading halt.
- Because SKHY (Nasdaq) and 000660 (KRX) are the same underlying business trading on two exchanges with limited two-way conversion in the first days of listing, the **SKHY ADR price detached from parity** with the Korean shares — reported premiums as high as **~51% over the KRX-implied value on 14 Jul 2026**, compressing to ~25-26% by 15-16 Jul as reporting suggests arbitrage/conversion activity narrowed the gap.
- **Why this matters even though this session stops at the Quality Gate (§3) and never reaches valuation:** it means a "live price" fetch for SKHY specifically, in this specific post-IPO window, is not a stable, arbitrage-anchored number the way a live price for an established single-listing stock is — a genuine Rule 0-adjacent caveat for *any* future SKHY session, not just this one. Flagged explicitly per the task brief's request; added to the Glossary as **ADR premium (parity gap)**.
- No credit-rating-related risk flag needed for the Debt Gate: S&P raised SK Hynix to **BBB+, positive outlook** (5 Feb 2026) — investment grade — though this doesn't change today's outcome (§3).

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

All figures sourced from SK Hynix's SEC Form 424B4 prospectus ("Summary Financial and Other Information" / consolidated financial statements section) unless otherwise noted — audited, IFRS (K-IFRS, Korea's IFRS adoption), reported in KRW billions. Where a public press release (SK Hynix's own FY2025 results release, syndicated via PRNewswire/CNBC/TrendForce) cited a slightly different operating-profit figure (₩47,206bn vs. the prospectus's ₩47,378bn — a ~0.4% gap, likely a rounding/consolidation-scope difference between the earnings-release and registration-statement presentations), **the SEC-filed prospectus figure is used as primary** per this framework's preference for the audited regulatory filing over a press release.

### 3.1 Source financial data (KRW billions, FY-end 31 Dec)

| Metric | FY2025 | FY2024 | FY2023 | FY2022 |
|---|---|---|---|---|
| Revenue | 97,147 | 66,193 | 32,766 | 44,648 |
| Cost of Sales | 38,456 | 34,365 | 33,299 | — |
| Gross Profit (Loss) | 58,691 | 31,828 | (533) | — |
| Operating Profit (Loss) | 47,378 | 23,468 | (12,640) | 7,007 |
| Profit before income tax | 50,466 | 23,885 | (11,658) | — |
| Income tax expense (benefit) | 7,518 | 4,088 | (2,520) | — |
| Net Income (Loss) | 42,948 | 19,797 | (9,138) | 2,439 |
| D&A (cash-flow statement) | 13,890 | 12,545 | 13,619 | — |
| Operating Cash Flow | 53,373 | 29,796 | 4,278 | — |
| Capital Expenditures | 27,519 | 15,946 | 8,325 | — |
| Total Assets | 176,108 | 119,855 | 100,330 | — |
| Total Liabilities | 55,441 | 45,940 | 46,826 | — |
| Total Equity | 120,667 | 73,916 | 53,504 | — |
| Cash & Equivalents | 14,924 | 11,205 | 7,587 | — |
| Total Borrowings (current + non-current) | 22,248 | 22,683 | — | — |

Source: SEC Form 424B4 (SK hynix Inc., filed 2026, accession 000119312526299963), *Summary Financial and Other Information* section. FY2022 revenue/operating profit/net income cross-sourced from SK Hynix's own "2022 and Fourth Quarter Financial Results" press release (PRNewswire/SK hynix Newsroom, Jan 2023) — needed only for the 3-year revenue CAGR denominator, not in the prospectus's 3-year table.

**Data-integrity note:** one WebSearch aggregator surfaced FY2025 total assets of ₩222.8 trillion / total equity ₩164.4 trillion — materially inconsistent with the SEC-filed prospectus figures above (₩176.1tn / ₩120.7tn). The prospectus figures are used as authoritative (audited, SEC-filed, directly extracted from the "Summary Financial and Other Information" table); the aggregator figure is disregarded as unverified and likely conflated with a different period or a different (e.g. non-consolidated, or post-Q1-2026) balance-sheet date.

### 3.2 Hard disqualifier check (fails regardless of weighted score)

- **FCF/NI conversion <70% for 2+ consecutive years without growth-capex explanation:** FY2025 FCF/NI = 60.2% (below 70%); FY2024 FCF/NI = 70.0% (exactly at, not below, threshold) — only one of the two most recent years is clearly below 70%, so this disqualifier does **not** independently fire. It would in any case have a documented growth-capex explanation: FY2025 capex rose 72.6% YoY (₩15,946bn → ₩27,519bn) for named expansion projects (Yongin semiconductor cluster, Cheongju P&T7 fab, EUV lithography equipment) tied to HBM4/AI-memory capacity — not maintenance spend.
- **Net Debt/EBITDA over threshold:** computed below (§3.3) at 0.12× — far under the 2.5× standard threshold. Does not fire. (SK Hynix is a heavy-capex fab manufacturer, not asset-light — the Upgrade 5 4×/6× override does not apply.)
- **Not FCF-positive for 3+ consecutive years: FIRES.**
  ```
  FY2023 FCF = Operating Cash Flow − CapEx = 4,278 − 8,325 = −4,047bn KRW  (negative)
  FY2024 FCF = 29,796 − 15,946 = 13,850bn KRW  (positive)
  FY2025 FCF = 53,373 − 27,519 = 25,854bn KRW  (positive)
  ```
  FY2023 (the 2022-2023 global memory-chip downturn, the same industry-wide down-cycle that also disqualified MU in this framework's 2026-07-08 MU session) sits inside the current FY2023-FY2025 three-fiscal-year window and was FCF-negative. **This alone fails the Quality Gate regardless of the weighted score below** — directly analogous to MU's own hard-disqualifier finding.

### 3.3 Weighted sub-scores

```
Profitability (25% weight):
  Net Margin (FY2025) = 42,948/97,147 = 44.2%
  NetMargin_Component = clamp((44.2/30)×100, 0, 100) = 100.0  (capped)

  Invested Capital = Total Debt + Total Equity − Cash = 22,248 + 120,667 − 14,924 = 127,991bn KRW
  Effective tax rate (FY2025) = 7,518/50,466 = 14.9%
  NOPAT = Operating Profit × (1 − eff. tax rate) = 47,378 × 0.851 = 40,319bn KRW
  ROIC = NOPAT/Invested Capital = 40,319/127,991 = 31.5%
  ROIC_Component = clamp((31.5/30)×100, 0, 100) = 100.0  (capped)

  Raw Profitability_Score = (100.0+100.0)/2 = 100.0
  --> capped at 40.0 (hard disqualifier: not FCF-positive 3 consecutive years, §3.2)
  Profitability_Score = 40.0

Margins (15% weight):
  Gross Margin (FY2025) = 58,691/97,147 = 60.4%
  GrossMargin_Score = clamp((60.4/80)×100, 0, 100) = 75.5
  (Well above the 40% trend-bonus threshold — no bonus applicable either way. Flagged qualitatively:
   this 60.4% is a sharp cyclical recovery from FY2023's −1.6% gross margin, not a stable multi-year
   level — see §4.1 note on cyclicality.)
  Margins_Score = 75.5

Growth (20% weight):
  Revenue 3yr CAGR = (97,147/44,648)^(1/3) − 1 = 29.6%
  Growth_Score = clamp((29.6/25)×100, 0, 100) = 100.0  (capped)
  TAM/pricing-power modifier: moot — already clamped at 100.0. Flagged qualitatively (not scored):
   this 3yr CAGR runs from a cyclical trough (FY2022) to a cyclical/AI-driven peak (FY2025) and
   significantly overstates a "durable" growth rate — treated the same cautious way MU's sessions
   treat its own cyclical revenue swings, i.e. not credited as evidence of a structurally higher
   sustainable growth rate even though the clamp makes the distinction numerically moot here.
  Growth_Score = 100.0

Balance Sheet (15% weight):
  Net Debt = Total Debt − Cash = 22,248 − 14,924 = 7,324bn KRW
  EBITDA (GAAP-derived) = Operating Profit + D&A = 47,378 + 13,890 = 61,268bn KRW
    (cross-check: prospectus's own non-GAAP "Adjusted EBITDA" FY2025 = 61,096bn — within 0.3%,
     internally consistent)
  Net Debt/EBITDA = 7,324/61,268 = 0.12×
  BalanceSheet_Score = clamp(100×(1 − 0.12/4), 0, 100) = 97.0

Moat Signal (15% weight) — checklist, only cited-evidence signals marked true:
  Market share stable/growing: MARKED TRUE — IDC data (Q1 2026): HBM 56.4% share (#1 globally,
    "global leadership" per SK Hynix's own F-1/424B4 disclosure), DRAM 29.1% share (#2 globally),
    NAND 18.5% share (#2). Multiple independent analyst sources (Goldman Sachs, UBS) project SK
    Hynix sustaining >50% HBM share through 2026 and ~70% share of Nvidia's HBM4/Rubin-platform
    orders.
  Brand premium: NOT marked true — DRAM/NAND are largely commodity-priced by supply/demand; no
    cited pricing-power-vs-competitors evidence beyond cyclical ASP swings (consistent with this
    framework's existing DRAM/NAND glossary characterization: "commoditized, boom-bust cyclical
    businesses with little durable pricing power").
  Network effect: NOT marked true — not applicable to a chip manufacturer.
  Switching costs: MARKED TRUE — HBM requires lengthy, multi-generation technical qualification
    with a GPU platform vendor before a supplier is designed in; SK Hynix was first to mass-produce
    HBM3E and has secured ~70% of Nvidia's HBM4 orders for the Rubin platform (UBS estimate) — a
    documented, cited integration/qualification-depth mechanism, not invented.
  Scale cost advantage: NOT marked true — no cited cost-per-bit/cost-per-unit data showing a
    SK-Hynix-specific cost edge vs. Samsung or Micron.
  Moat_Score = (2/5)×100 = 40.0

FCF Quality (10% weight):
  FCF/NI ratio (FY2025) = 25,854/42,948 = 60.2%
  FCFQuality_Score = clamp(((0.602−0.40)/0.60)×100, 0, 100) = 33.7

Quality Score = 40.0×0.25 + 75.5×0.15 + 100.0×0.20 + 97.0×0.15 + 40.0×0.15 + 33.7×0.10
              = 10.000 + 11.325 + 20.000 + 14.550 + 6.000 + 3.370
              = 65.245  →  rounds to 65.2
```

**Quality Score = 65.2 / 100.0 — below the 80.0 gate, and independently failed by the "not FCF-positive for 3+ consecutive years" hard disqualifier (FY2023, §3.2).**

**Gate result: FAIL — on both the hard disqualifier and the weighted score.** Per `operating-brief.md`/`quality-scoring.md`: stop here, do not proceed to the Rate Environment Gate or Phase 02 valuation scoring.

---

## 4. Qualitative Notes

1. **This is a genuine memory-chip supercycle story, not a marginal quality case.** SK Hynix's HBM leadership (56.4% share, ~70% of Nvidia's next-gen HBM4 orders) is real, well-documented, and the strongest Moat evidence found for any memory-chip name evaluated in this framework so far (MU credited only 1/5 signals; SK Hynix credits 2/5). But moat strength alone cannot override the hard disqualifier or the 80.0 gate.
2. **The same 2023 industry down-cycle that disqualified MU also disqualifies SK Hynix.** Both companies' FY2023 (a severe, industry-wide DRAM/NAND price collapse) produced negative free cash flow — the hard disqualifier is structural to the memory-chip commodity cycle in this window, not company-specific mismanagement. This is a useful cross-check on the framework's internal consistency: two competitors in the same brutal cyclical business, evaluated independently, fail the same way for the same underlying reason.
3. **FY2025/Q1 2026 profitability is extraordinary and should be read with caution, not extrapolated.** FY2025 net margin (44.2%) and Q1 2026 net margin (reported ~77%, net income ₩40,346bn on revenue ₩52,576bn per SK Hynix's own 1Q26 results release — not used in the scoring above, which relies on the FY2025 audited annual figures, but noted here as directional confirmation the upcycle continued into 2026) reflect an acute AI-driven memory shortage, not a normalized, sustainable margin structure. Rule 6 ("normalize before you value") would apply heavily to any future Phase 02 valuation work on this name.
4. **The ADR-premium dislocation (§2.2) is a live, ongoing price-integrity risk**, independent of and in addition to the Quality Gate failure — flagged for any future SKHY session, not just this one.
5. **Instrument-structure risk, the complication flagged in the task brief, did not materialize as a blocker.** SKHY carries full SEC-filed audited IFRS financials via its Form 424B4 registration statement — this session did not need to fall back to DART or an unaudited aggregator for any core Quality Score input.

---

## 5. Rate Environment Gate — NOT RUN

Not applicable — the Quality Gate stops the process first (§3.3). No 10Y Treasury comparison, Earnings Yield Spread Test, or Rate Regime Modifier is computed.

---

## 6. Phase 02 — Valuation Score / Composite Score — NOT RUN

Not applicable — Quality Gate failed. No FCF Yield, EV/EBIT, Forward PE, or PEG sub-scores are computed into a valuation score; no Composite Score exists; no fair value, buy/sell/stop levels, or position sizing are produced.

---

## 7. Recommendation

# **PASS — Quality Gate FAIL (Quality Score 65.2 < 80.0, hard disqualifier also fires). Do not enter.**

SK Hynix (SKHY) does not clear this framework's 80.0+ Quality Score gate, and independently fails on the "not FCF-positive for 3+ consecutive years" hard disqualifier (FY2023's global memory-downturn loss year). No Phase 02 valuation score or Composite Score was computed; no fair value, order setup, or position sizing was produced. **No position should be opened.**

This is a first-ever evaluation for this ticker — a new dated watchlist entry is created (§ below), not an appended note.

---

## 8. Next Review Trigger

- **FY2026 fiscal year-end close and filing** (~Q1 2027) — the point at which FY2023's loss year finally rolls out of the FCF-positive-3-years window, removing that hard disqualifier. FY2026's extraordinary early-year profitability (§4.3) would also materially change the revenue-CAGR/profitability inputs once the full year closes.
- **SK Hynix's first Form 20-F** (expected once a full post-listing fiscal year has closed) — would supersede the 424B4 prospectus as the primary ongoing SEC data source.
- **Resolution of the ADR-premium dislocation** (§2.2) — watch for the premium/discount to KRX:000660 stabilizing near zero as two-way conversion normalizes; any future live-price fetch for this name should re-check the premium before treating the Nasdaq quote as economically representative.
- Any further >15% unexplained single-day move, guidance revision, or management change (Rule 9).
- Any confirmation or refutation of the industry-wide memory-chip "risk" narrative referenced in the triggering Telegram video (re: Micron, SanDisk, SK hynix), independent of this session's Quality Gate outcome.

**No position opened — nothing to log in `decisions/`.**

---

## Glossary

- **424B4 (Prospectus)** — The final prospectus a company files with the SEC after its registration statement is declared effective; SK Hynix's 424B4 is this session's primary financial-data source.
- **ADR (American Depositary Receipt)** / **ADS (American Depositary Share)** — A US-exchange-listed security representing shares of a non-US company; SKHY represents SK Hynix's Korean ordinary shares at a 1 ADS = 0.1 share ratio.
- **ADR premium (parity gap)** — The percentage by which an ADR's US-dollar price diverges from the value implied by its underlying home-market shares — theoretically near zero via arbitrage, but able to widen sharply when arbitrage/conversion is constrained. SKHY traded at premiums as high as ~51% over its KRX-listed shares in its first week, a live price-integrity risk flagged in this session. *(New term.)*
- **BBB+ / Investment grade** — See Investment grade below; S&P's BBB+ rating (positive outlook) for SK Hynix.
- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate between a start and end value.
- **CIK (Central Index Key)** — The SEC's unique numeric identifier for an EDGAR filer; SK Hynix's is 0002120882.
- **Composite Score** — This framework's blended Quality + Valuation ranking number; not computed here since the Quality Gate failed first.
- **DART** — South Korea's Financial Supervisory Service electronic disclosure system, the Korean equivalent of the SEC's EDGAR — not needed as a data source this session since SKHY's SEC filings sufficed. *(New term.)*
- **D&A** — Depreciation & Amortization, the non-cash expense spreading long-lived-asset costs over time.
- **DRAM / NAND** — The two main memory-chip families: DRAM is working memory, NAND is flash storage. Both are commoditized, cyclical businesses.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **F-1 (Registration Statement)** — The SEC form a foreign private issuer files to register securities for a US public offering — the foreign-issuer counterpart to a US company's S-1. SK Hynix filed an F-1 ahead of its Nasdaq listing. *(New term.)*
- **FCF** — Free Cash Flow, cash left after running and maintaining the business.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income; checks whether accounting profit is turning into real cash.
- **Foreign private issuer** — SEC classification for a qualifying non-US company, subject to Form 20-F/6-K reporting instead of Form 10-K/8-K.
- **GAAP** — Generally Accepted Accounting Principles, the standard US accounting rulebook (contrast with IFRS below).
- **Hard disqualifier** — A Quality Score condition that fails a company regardless of its weighted score.
- **HBM (High-Bandwidth Memory)** — A premium, stacked-DRAM format used in AI accelerator GPUs; SK Hynix's primary current competitive strength.
- **IDC (International Data Corporation)** — An independent global tech-market-research firm; its DRAM/NAND/HBM market-share tracking is the third-party source for this session's Moat Signal evidence. *(New term.)*
- **IFRS (International Financial Reporting Standards)** — The accounting standard most non-US companies use for audited financial statements, as opposed to US GAAP.
- **Invested Capital** — The total capital (debt + equity, net of cash) put to work in a business; the denominator in this framework's ROIC calculation.
- **Investment grade** — A credit rating (BBB-/Baa3 or higher) signaling low perceived default risk.
- **K-IFRS (Korea-adopted IFRS)** — Korea's mandated national adoption of IFRS for Korea Exchange-listed companies' consolidated statements since 2011 — materially the same standard as global IFRS. *(New term.)*
- **KRX (Korea Exchange) / KOSPI** — South Korea's national stock exchange, and KOSPI, its main benchmark index. SK Hynix's primary listing is KRX:000660; SKHY is a secondary, dollar-denominated ADR wrapper. A market-wide KOSPI circuit breaker was triggered 13 Jul 2026 amid SK Hynix's 15.4% single-day plunge. *(New term.)*
- **Moat** — A durable competitive advantage protecting a business's profits from competitors.
- **Net Debt/EBITDA** — A leverage ratio measuring years of cash profit needed to pay off all debt.
- **Net Margin** — Net Income ÷ Revenue.
- **NOPAT** — Net Operating Profit After Tax, EBIT × (1 − effective tax rate); the numerator this framework uses to compute ROIC.
- **Quality Score** — This framework's 0.0–100.0 continuous score grading Phase 01 criteria; 80.0+ required to proceed to valuation scoring.
- **Rate Environment Gate** — The mandatory pre-check before Phase 02 scoring, comparing Earnings Yield to the 10-Year Treasury yield.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 6** — This framework's instruction to normalize earnings/margins before valuing a business, stripping out one-time or cyclically-distorted items.
- **Rule 9** — Fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move.
- **S-1 / S-1/A (Registration Statement)** — The SEC form a US company files to register securities for a public offering; F-1 (above) is the foreign-issuer counterpart.
- **Sponsored ADR / Unsponsored ADR** — An unsponsored ADR is created by a depositary bank without the underlying company's involvement, typically thin and carrying no company SEC reporting; a sponsored ADR is established with the company's direct participation, its own SEC registration, and ongoing periodic filings. SKHY upgraded from a thin unsponsored OTC program (HXSCL) to a sponsored, SEC-registered Nasdaq listing on 10 Jul 2026. *(New term.)*
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results.
- **XBRL** — A structured, machine-readable data format the SEC requires public companies to tag financial-statement figures in.

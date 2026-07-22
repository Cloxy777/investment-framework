# NEW POSITION — DOCN (DigitalOcean Holdings, Inc., NYSE) — 2026-07-22

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — unattended run)
**Date:** 22 Jul 2026 (Wednesday, pre-market — regular session for 2026-07-22 had not yet opened at evaluation time)
**10Y US Treasury Yield:** 4.63% (as of 2026-07-21 close — most recent posted observation; +0.03pp vs. the prior session)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §4). For reference only, the bracket in force would be **+5** (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current DOCN portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — this is DOCN's first-ever evaluation under this framework.
**Sector:** Technology — Software/Infrastructure (cloud IaaS/PaaS/SaaS, increasingly AI inference/GPU compute)
**Filer type:** US domestic filer, NYSE-listed. Full 10-K/10-Q history available (IPO March 2021).
**First-use jargon decode:** see closing Glossary (§8).

---

## 0. Why this session exists — trigger source

A Telegram post on the **FinnInvestChannel** channel (post #2969, ~06:57 UTC 2026-07-22): *"DigitalOcean підвищує ціни на погодинну оренду окремих GPU від Nvidia та AMD приблизно на 30% з 1 серпня через високий попит на обчислювальні потужності для AI"* ("DigitalOcean is raising hourly rental prices on select Nvidia and AMD GPUs by ~30% effective August 1, due to high demand for AI compute"). Per the operating brief, **Telegram post text is never used as financial data** — it is a trigger only. DigitalOcean had no prior watchlist or holdings entry in this framework, so per `/telegram-scan` step 4 ("No watchlist entry exists at all → `/new-position`"), a full first-time evaluation is triggered regardless of the post's content. The GPU price-increase claim is independently verified in §5 (Moat Signal) directly from DigitalOcean's own blog, not from the Telegram post.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$136.45** | Yahoo Finance chart API, `regularMarketPrice`, `regularMarketTime` 2026-07-21 20:00:03 UTC (16:00 ET — the regular-session close; 2026-07-22's regular session had not yet opened, `currentTradingPeriod.regular.start` = 2026-07-22 13:30 UTC) |
| Prior close | $119.09 | Same source, `chartPreviousClose` (2026-07-20 close) |
| Implied 1-day move (07-20 → 07-21) | **+14.6%** | ($136.45 − $119.09) / $119.09 — **flagged**: close to, but just under, Rule 9's ">15% move without a fundamental trigger" threshold. Independently confirmed via WebSearch as part of an ongoing AI-driven re-rating (RPO pre-announcement 2026-07-07, continued momentum through 2026-07-21) rather than a single unexplained jump — see §5.1. |
| 52-week range | $25.56 – $187.50 | Yahoo Finance `summaryDetail` |
| Analyst target (mean / median) | $177.69 / $179.00 | Yahoo Finance `financialData` |
| Market Cap | $15.952B | Yahoo Finance `summaryDetail` (116,908,096 shares × $136.45 — internally consistent) |
| US 10Y Treasury yield | 4.63% | WebSearch, tradingeconomics.com, as of 2026-07-21 close |

**$136.45 is used as the live price for this session.** Formal Q2 2026 earnings are **not yet reported** (scheduled before market open, **4 August 2026** — confirmed via WebSearch of DigitalOcean's own investor-relations announcement, 21 Jul 2026). The stock has already re-rated hard this year: from a $77.00/share Q1 2026 equity offering price (see §3, Balance Sheet) to an all-time high of $181.29 (15 Jun 2026), pulling back and re-accelerating since, including a 10.4% jump on 2026-07-07 after DigitalOcean pre-announced record preliminary Q2 2026 results (RPO expected to exceed $800M, +10x YoY). This context matters for interpreting the valuation work that would follow Phase 02 (not reached this session — see §4).

---

## 2. Data Gathered — Sources & Method

### 2.1 Primary data source

Yahoo Finance `quoteSummary` and `fundamentals-timeseries` endpoints (annual and quarterly), fetched directly (crumb-authenticated) since the local `yfinance` Python package could not establish a TLS connection in this session's sandboxed network path — the underlying data is the same Yahoo Finance source `yfinance` itself wraps, fetched via the same public API. Cross-checked against DigitalOcean's own SEC-filed press releases (8-K exhibits) and investor-relations site for anything Yahoo's normalization could obscure (one-off items, non-GAAP reconciliations) — sourced via WebSearch of `investors.digitalocean.com`, `businesswire.com`, and `stocktitan.net` (which mirrors 8-K filings).

### 2.2 Income statement — annual (Yahoo Finance, $ thousands)

| | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| Total Revenue | 576,322 | 692,884 | 780,615 | 901,427 |
| Gross Profit | 364,395 | 397,497 | 465,943 | 539,592 |
| Gross Margin | 63.23% | 57.37% | 59.69% | 59.86% |
| EBIT | (15,489) | 35,721 | 106,812 | 224,602 |
| Normalized EBITDA | 87,150 | 174,474 | 236,864 | 313,947 |
| Net Income (GAAP) | (27,804) | 19,409 | 84,492 | 259,262 |
| Normalized Income (Yahoo, excl. unusual items net of tax) | (27,482) | 34,549 | 84,492 | 221,260 |
| Total Unusual Items | (407) | (20,887) | 0 | +48,104 |

**Revenue 3yr CAGR (FY2022→FY2025)** = `(901,427/576,322)^(1/3) − 1 = 16.09%`

**⚠️ FY2025's net income is materially inflated by one-off items**, confirmed independently via WebSearch of DigitalOcean's own Q3 2025 earnings release: a **$69.9M release of a US deferred-tax valuation allowance**, plus a **gain on debt extinguishment**, together lifted Q3 2025 diluted EPS growth to +358% YoY and net income margin to 69% that quarter alone. Yahoo's own "Normalized Income" field ($221.26M) already backs most of this out; used as the profitability basis below in preference to the raw $259.26M GAAP figure, consistent with Rule 6 ("normalize before you value").

### 2.3 TTM reconstruction (Q2 2025 + Q3 2025 + Q4 2025 + Q1 2026) — most recent 4 quarters, since Q2 2026 has not yet reported

| ($ thousands) | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 | **TTM** |
|---|---|---|---|---|---|
| Total Revenue | 218,700 | 229,634 | 242,390 | 257,905 | **948,629** |
| Gross Profit | 130,945 | 136,933 | 142,270 | 144,710 | **554,858** (58.49% margin — matches Yahoo's cached TTM `grossMargins` exactly, a consistency cross-check) |
| EBIT | 44,687 | 95,356 | 40,971 | 35,049 | **216,063** |
| Normalized EBITDA | 77,721 | 82,043 | 81,385 | 83,224 | **324,373** |
| Net Income (GAAP) | 37,027 | 158,371 | 25,660 | 15,771 | **236,829** (24.96% margin — matches Yahoo's cached `profitMargins` exactly) |
| Normalized Income | 37,262 | 120,156 | 25,660 | 17,510 | **200,588** (21.15% margin) |
| Operating Cash Flow | 92,447 | 95,787 | 57,280 | 46,921 | **292,435** (matches Yahoo's cached `operatingCashflow` exactly) |
| CapEx (Yahoo/GAAP convention) | (35,432) | (38,522) | (129,586) | (56,539) | **(260,079)** |
| **FCF (GAAP: OCF − CapEx)** | 57,015 | 57,265 | (72,306) | (9,618) | **32,356** |
| Company's own disclosed **Adjusted FCF** (non-GAAP; see §2.4) | 57,000 | 85,000 | 27,000 | 2,189 | **171,189** |
| Tax Provision | 5,421 | (68,057) | 6,860 | 8,725 | (47,051) net benefit (driven by the Q3 valuation-allowance release) |

### 2.4 Company-reported "Adjusted Free Cash Flow" — independent cross-check

DigitalOcean discloses its own non-GAAP "Adjusted Free Cash Flow" each quarter (OCF minus only property/equipment and internal-use-software capex, excluding certain financing-related capex Yahoo's broader "Free Cash Flow" field captures): **Q2 2025 $57M (26% margin), Q3 2025 $85M (37% margin), Q4 2025 $27M (11% margin), FY2025 total $168M (19% margin), Q1 2026 $2.189M (1% margin — explicit reconciliation confirmed: OCF $46.921M − property/equipment capex $39.992M − software capex $4.740M = $2.189M)** — all confirmed via WebSearch of DigitalOcean's own quarterly earnings press releases (businesswire.com / investors.digitalocean.com). This figure is materially different from, and in most quarters larger than, the Yahoo/GAAP-convention "Free Cash Flow" figure in §2.3 — used below as a disclosed sensitivity, not the primary input, since the framework's own documented `yfinance` methodology (valuation-scoring.md "Screening Tools" section) pulls the GAAP `Free Cash Flow` field, not a company's own non-GAAP variant.

**⚠️ Data gap, flagged rather than invented around:** Hybrid Upgrade 1 (Owner Earnings) would apply if growth capex exceeds 30% of total capex — plausible here given the scale of the AI/GPU buildout (total capex nearly doubled YoY in FY2025), but **DigitalOcean does not publicly disclose a maintenance-vs-growth capex split** (confirmed by direct inspection of the Q1 2026 earnings-release capex reconciliation — only "property and equipment" and "internal-use software" lines exist, no further breakdown). Owner Earnings could not be computed without inventing a maintenance-capex assumption, which Rule 0 prohibits. FCF Yield below therefore uses the GAAP FCF figure (primary) with the company's Adjusted FCF shown as a sensitivity — this does not change the qualitative conclusion (see §3).

### 2.5 Balance sheet — quarterly (Yahoo Finance, $ thousands)

| | Q4 2025 (2025-12-31) | **Q1 2026 (2026-03-31, most current)** |
|---|---|---|
| Total Debt | 1,602,105 | **1,299,895** |
| Cash and Equivalents | 254,475 | **741,363** |
| Stockholders' Equity | (28,690) | **887,376** |

**⚠️ This balance-sheet swing is real and independently confirmed, not a data artifact — a direct parallel to the fair-value-methodology.md "SPGI Price Inference Error" lesson about not using stale data.** Using only the FY2025-year-end (2025-12-31) balance sheet would show Net Debt/EBITDA = (1,602,105−254,475)/324,373 = **4.29×** — a Debt Gate hard-disqualifier breach. But WebSearch confirms (Motley Fool/AOL Q1 2026 earnings-call coverage, DigitalOcean's own Q1 2026 press release) that DigitalOcean **raised $887.9M net proceeds in a registered equity offering at $77.00/share in Q1 2026**, using proceeds to **fully repay its $500M Term Loan A** (saving ~$50M/yr in cash interest) and fund retirement of its 2026 convertible notes — a confirmed, primary-sourced capital-structure event, not a Yahoo data inconsistency. Using the current (2026-03-31) balance sheet:

```
Net Debt (2026-03-31) = 1,299,895 − 741,363 = 558,532
Net Debt/EBITDA (TTM) = 558,532 / 324,373 = 1.722×
```

**Using the live, current balance sheet, Net Debt/EBITDA passes comfortably (1.72× vs. the 2.5× standard threshold) — a materially different conclusion from the stale FY2025-only reading (4.29×, which would have wrongly fired the Debt Gate hard disqualifier).** This is exactly the kind of stale-data trap Rule 0 exists to prevent, even though Rule 0 is framed around live *prices* — the same discipline applies to using the most current *balance sheet* available rather than the latest full fiscal year when a quarter more recent than it exists.

### 2.6 Qualitative / Moat evidence (independently sourced, not from the Telegram post)

- **Pricing power (independently confirmed):** DigitalOcean's own blog (`digitalocean.com/blog/price-changes-gpus`) confirms an on-demand GPU (Nvidia/AMD) pricing update effective 1 August 2026, attributed to "strong demand for advanced GPU capacity" — independently verifying the Telegram post's claim from a primary source, per Rule 0's requirement that the post itself never be used as data.
- **Net Dollar Retention (NDR):** Q1 2026 overall NDR 101% (barely above flat); Digital Native Enterprise segment 102%, $500K+ customers 106%, $1M+ customers 115% (WebSearch, DigitalOcean IR).
- **Market position:** DigitalOcean holds an estimated 2.73% of the Cloud/IaaS market, #3 behind AWS (6.65%) and Google Cloud (5.96%) — a single-point-in-time estimate, not a documented multi-year share trend (WebSearch, third-party market-share estimate).
- **Growth/TAM evidence:** Q1 2026 revenue +22% YoY; ARR $1.03B (+22% YoY); AI Customer ARR $170M (+221% YoY); Million+ Dollar Customer ARR $183M (+179% YoY); RPO pre-announced to exceed $800M for Q2 2026 (+10x YoY) with weighted-average contract life extending from 1.6 to 3+ years; incremental 20MW of data-center capacity secured for late 2027/early 2028 (total committed ~155MW) — all confirmed via WebSearch of DigitalOcean's own investor-relations releases.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years w/o growth-capex explanation | FY2024: 96,202/84,492 = **113.9%** (pass) · FY2025: 41,089/259,262 = **15.85%** (fail) | disqualify if 2+ **consecutive** years <70% w/o carve-out | **Does not fire** — only 1 of the last 2 fiscal years is below 70%, not 2+ consecutive. Flagged as a sharply worsening trend worth watching at the next rescore; a documented growth-capex explanation is already available if it does become 2 consecutive years (AI/GPU infrastructure buildout — capex nearly doubled YoY in FY2025, see §2.3/§2.4). |
| Net Debt/EBITDA over threshold (2.5× standard; not asset-light eligible — DigitalOcean is a capital-intensive cloud-infrastructure operator, not a payment network/exchange) | **1.722×** (current, 2026-03-31 balance sheet — see §2.5) | disqualify if exceeds 2.5× | **Passes.** Would have wrongly fired at 4.29× under a stale FY2025-year-end-only reading — see §2.5's flagged Rule-0-style lesson. |
| FCF positive 3+ consecutive years | FY2022 +$74.9M · FY2023 +$110.1M · FY2024 +$96.2M · FY2025 +$41.1M — all four years positive | disqualify if not 3 consecutive positive years | **Passes** — FCF positive every year shown, though the FY2025 level is the lowest of the four and well below FY2023's peak. |

**No hard disqualifier fires.** Proceeding to the full weighted Quality Score.

### 3.2 Quality Score — full computation

```
PROFITABILITY (25% weight):
  Net Margin (TTM, normalized — excl. Q3 2025 tax-valuation-allowance release / debt-extinguishment gain) = 21.15%
  NetMargin_Component = clamp((21.15/30)×100, 0, 100) = 70.5

  EBIT_TTM = 216,063
  Effective tax rate: company's own disclosed non-GAAP long-term projected rate = 16% (Q1 2026 earnings release) —
    used in preference to the raw TTM GAAP rate (which is a NET TAX BENEFIT of −24.8%, itself an artifact of the
    Q3 2025 one-off valuation-allowance release being normalized away here, not a sustainable rate)
  NOPAT = 216,063 × (1 − 0.16) = 181,493
  Invested Capital (2026-03-31) = Total Debt + Equity − Cash = 1,299,895 + 887,376 − 741,363 = 1,445,908
  ROIC = 181,493 / 1,445,908 = 12.55%
  ROIC_Component = clamp((12.55/30)×100, 0, 100) = 41.8
  (Sensitivity: using the raw, one-off-inclusive TTM effective tax rate instead would give ROIC ≈18.65%,
   ROIC_Component ≈62.2 — shown for transparency; not used, since it's inflated by the same one-off already
   excluded from the Net Margin input above, and mixing a normalized numerator with a non-normalized tax rate
   would be inconsistent)

  Profitability_Score = (70.5 + 41.8) / 2 = 56.15
  (FCF-positive-3yr cap does not apply — DOCN is FCF-positive all 4 years shown)

MARGINS (15% weight):
  Gross Margin (TTM) = 58.49%
  GrossMargin_Score = clamp((58.49/80)×100, 0, 100) = 73.1
  3yr trend: 63.23% (FY22) → 57.37% (FY23) → 59.69% (FY24) → 58.49% (TTM) — not structurally expanding
  (dipped then partially recovered); no bonus applies, and margin is already well above the 40% bonus-eligible
  ceiling regardless.

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2022→FY2025) = 16.09%
  Growth_Score = clamp((16.09/25)×100, 0, 100) = 64.4
  TAM/pricing-power modifier: +10 — well-documented (RPO pre-announced +10x YoY to $800M+, AI Customer ARR
    +221% YoY, Million+ Dollar Customer ARR +179% YoY, independently-confirmed GPU price increase, new data
    center capacity — see §2.6). No documented structural deceleration (accelerating: 22%→29% guided YoY).
  Growth_Score = 64.4 + 10 = 74.4

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (TTM, current 2026-03-31 balance sheet) = 1.722× (see §2.5/§3.1)
  BalanceSheet_Score = clamp(100×(1 − 1.722/4), 0, 100) = 57.0

MOAT SIGNAL (15% weight) — checklist, cited evidence only:
  Market share stable/growing: FALSE — 2.73% Cloud/IaaS share (#3) is a single snapshot (§2.6); no cited
    multi-period trend showing it's stable or growing, so not credited without that evidence.
  Brand premium (pricing power): TRUE — independently confirmed via DigitalOcean's own blog: an on-demand
    Nvidia/AMD GPU price increase effective 1 Aug 2026, explicitly attributed to "strong demand" (§2.6) —
    a real, primary-sourced pricing-power signal (distinct from the Telegram post that triggered this session).
  Network effect: FALSE — no documented two-sided-marketplace/user-growth-driven-value mechanism.
  Switching costs: FALSE — NDR (101% blended, higher for large-customer cohorts) is suggestive but not itself
    the "documented mechanism" (integration depth, contractual lock-in, migration cost) this checklist row
    requires; not credited without a more specific citation.
  Scale cost advantage: FALSE — at 2.73% share DigitalOcean is smaller than the two leading hyperscalers
    (AWS 6.65%, Google Cloud 5.96%) it's benchmarked against here; no cost-per-unit data vs. smaller
    competitors was found to support a scale advantage in the other direction.
  Moat_Score = (1/5) × 100 = 20.0

FCF QUALITY (10% weight):
  FCF/NI ratio (TTM, GAAP FCF ÷ Normalized NI, consistent with this framework's documented yfinance-sourced
    convention) = 32,356 / 200,588 = 16.13%
  FCFQuality_Score = clamp(((0.1613 − 0.40)/0.60)×100, 0, 100) = 0.0 (floor)
  ⚠️ Sensitivity: using the company's own disclosed Adjusted FCF (§2.4) instead — 171,189/200,588 = 85.35% —
  would give FCFQuality_Score ≈75.6. Shown for transparency; the GAAP-convention figure is used as primary
  since it matches this framework's own documented sourcing method (valuation-scoring.md), and because the
  large gap between the two conventions is itself informative (heavy near-term capex intensity from the
  AI/GPU buildout, §2.3/§2.4).

QUALITY SCORE = 56.15×0.25 + 73.1×0.15 + 74.4×0.20 + 57.0×0.15 + 20.0×0.15 + 0.0×0.10
             = 14.0375 + 10.965 + 14.88 + 8.55 + 3.00 + 0.00
             = 51.43 → rounds to 51.4

(Sensitivity, combining the most generous plausible reading of every ambiguous input at once — raw-tax-rate
 ROIC_Component 62.2 instead of 41.8, and Adjusted-FCF-based FCFQuality_Score 75.6 instead of 0.0 — would raise
 the total to approximately 61.5. Still far below the 80.0 gate under any combination of conventions tested.)
```

**Quality Score = 51.4 / 100.0 (range 51.4–61.5 across every sensitivity tested) — fails the 80.0+ gate by a wide, convention-robust margin.**

**Gate result: FAIL.** Per quality-scoring.md, operating-brief.md, and this session's explicit instructions: **do not proceed to the Rate Environment Gate, Phase 02 valuation scoring, the Composite Score, or any order setup.**

---

## 4. Phase 02 / Order Setup — NOT PRODUCED

No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup is computed this session. The Quality Score gate is a strict, non-negotiable prerequisite (quality-scoring.md: *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all... Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."*) and DOCN's Quality Score (51.4, or up to ~61.5 under the most generous sensitivity combination) falls well short under every convention tested in §3.2.

*(For context only, not used in any decision: at the current $136.45 price the stock already trades at ~76× TTM EV/EBIT and ~73× forward PE with no reconstructable 5yr PE range — see §5.4 — a valuation picture that would very likely have driven an expensive Phase 02 score even had the Quality Gate been cleared. This is noted for completeness, not as a substitute for the gate result above.)*

---

## 5. Qualitative Notes

1. **This evaluation reversed itself mid-session on the Debt Gate** — the FY2025-year-end-only balance sheet implied a disqualifying 4.29× Net Debt/EBITDA, but the current (2026-03-31) balance sheet, reflecting a confirmed $887.9M Q1 2026 equity raise used to retire debt, shows a comfortable 1.72×. This is flagged prominently (§2.5) as a live example of why Rule 0's "always fetch live, current data" discipline matters beyond just price — a stale balance sheet would have produced the wrong hard-disqualifier verdict here.
2. **The Quality Score failure is not close** — 51.4 against an 80.0 gate, and even the most generous combination of every ambiguous input tested (tax-rate convention, FCF definition) only reaches ~61.5. The Moat Signal (1 of 5, 20.0) is the single weakest sub-score and the largest driver: DigitalOcean has one clearly-evidenced pricing-power signal (the GPU price increase that triggered this session) but no documented, cited evidence for the other four checklist items at this evaluation.
3. **FY2025's reported profitability is significantly better than its underlying, normalized profitability** — GAAP net margin (28.8% reported) overstates true earnings power once the Q3 2025 one-off deferred-tax valuation-allowance release and gain on debt extinguishment are excluded (normalized net margin 21.15%, TTM basis). This is exactly the kind of earnings-quality distortion this framework's existing "clean earnings" PEG eligibility rule and Rule 6 ("normalize before you value") are designed to catch — DigitalOcean would not have qualified as a PEG-eligible "Fast Grower" in any case (its GAAP profitability history is too short and too one-off-distorted to meet the "reliable, non-distorted earnings base" bar), had Phase 02 been reached.
4. **No 5-year historical PE range or average is reconstructable** — Yahoo's quarterly EPS history for DOCN only extends 5 quarters back via the API used this session (vs. the ~20 quarters/5 years the framework's documented method calls for), and the company's EPS was negative/near-zero for much of its 2021–2023 history in any case. Had Phase 02 been reached, the Forward PE sub-score would have used the documented "no-history fallback" (50.0, neutral, flagged) rather than an invented range.
5. **A large ($888M) capex-funded AI/GPU infrastructure buildout is the dominant story in every number this session touched** — the sharp swing from FY2024 to FY2025 FCF (down from $96.2M to $41.1M despite revenue growth), the balance-sheet deleveraging (funded by an equity raise, not organic cash generation), and the GPU price increase that triggered this session are all the same underlying capital-allocation story: DigitalOcean is investing heavily and financing that investment externally (equity) rather than fully from internal cash flow, ahead of demand it has not yet reported (Q2 2026 earnings due 4 Aug 2026). This is a legitimate, well-documented growth story but is exactly the kind of "great narrative, not yet reflected in trailing financial quality" situation this framework's Quality Score gate exists to filter before any valuation work begins.
6. **The stock has already re-rated sharply ahead of the Quality Score work above** (from a $77.00 Q1 2026 offering price to $136.45 now, having touched $181.29) with formal Q2 2026 results still two weeks away (4 Aug 2026) as of this session. Entering a new position into an already-large run, ahead of an earnings print the market has partly pre-digested via a preliminary pre-announcement, would run against this framework's "never act on price movement alone" and "act only on documented triggers" non-negotiables even had the Quality Gate been cleared.

---

## 6. Recommendation

# **PASS — Quality Score gate FAILS (51.4, range 51.4–61.5 across every sensitivity tested; well below the 80.0+ threshold). Do not proceed to valuation scoring. No position, no watchlist-only tracking beyond the "not held / gate FAIL" pointer below — this ticker does not clear the framework's first screening gate.**

DigitalOcean shows genuine, well-documented top-line momentum (revenue accelerating from 22% to a guided 29% YoY, RPO pre-announced +10x YoY, AI Customer ARR +221% YoY) and one clearly-evidenced pricing-power signal (the GPU price increase that triggered this session, independently confirmed from the company's own blog). But it fails the Quality Score's strict, non-negotiable 80.0+ gate by a wide margin (51.4, or at most ~61.5 under the most generous combination of ambiguous-input conventions) — driven mainly by a thin Moat Signal (1 of 5 checklist items credited with cited evidence), modest ROIC (~12.6%) relative to how richly the stock already trades, and a sharply weakening FCF/Net-Income conversion ratio in the most recent fiscal year (15.85%, though not yet 2 consecutive years so no hard disqualifier fires). Per operating-brief.md and quality-scoring.md, **this stops the evaluation before Phase 02** — no Rate Environment Gate, valuation score, Composite Score, or fair-value/order-setup work is produced.

---

## 7. Next Review Trigger

- **DigitalOcean's Q2 2026 earnings (4 August 2026)** — the natural next checkpoint: will show whether the pre-announced RPO/revenue acceleration holds up formally, provide a second consecutive data point on the FCF/NI conversion trend (currently 1 of 2 years below the 70% threshold — a second consecutive low reading would still likely be covered by the documented AI-capex growth-capex carve-out, but is worth re-checking explicitly), and update the Moat Signal evidence base (a full quarter of GPU-price-increase realization, further NDR/market-share data).
- **Any Rule 9 event**: guidance revision, management change, material M&A, or macro shift — none identified this session beyond the routine earnings-date announcement.
- **A first-ever watchlist entry is created this session** (`watchlist/not-in-portfolio/DOCN/DOCN-2026-07-22.md`) recording the "Phase 01 FAIL" outcome, per the standard `/new-position` convention for a first-time evaluation.

---

## 8. Glossary

- **8-K**: a US company's "current report" filed with the SEC to disclose a material event between regular filings; DigitalOcean's quarterly earnings press releases are furnished as 8-K exhibits.
- **Adjusted EBITDA / Adjusted Free Cash Flow**: a company's own non-GAAP variants of EBITDA/FCF that strip out or redefine certain items — DigitalOcean's own disclosed Adjusted FCF is used as a sensitivity, not the primary input, in §2.4/§3.2.
- **ARR (Annual Recurring Revenue)**: the annualized run-rate value of DigitalOcean's contracted recurring revenue ($1.03B at Q1 2026, +22% YoY).
- **CapEx**: Capital Expenditure — the dominant driver of DOCN's FCF trend this session (§2.3–2.4).
- **Composite Score**: this framework's blended 0.0–100.0 ranking — not computed this session, since DOCN never clears the Quality Score gate required to reach it.
- **Deferred tax valuation allowance release**: a one-off GAAP accounting event that inflates net income/EPS in the period it's recognized — DigitalOcean's Q3 2025 $69.9M release materially distorts its FY2025 reported profitability (§2.2, §5.3).
- **EBIT / EBITDA**: Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **Effective tax rate**: the actual percentage of pretax income paid as tax in a period — DOCN's TTM GAAP rate is a net *benefit* (−24.8%) due to the Q3 2025 one-off; this session used the company's own disclosed 16% long-term non-GAAP rate instead for the ROIC calculation (§3.2).
- **EV/EBIT, EV/EBITDA**: Enterprise Value ÷ EBIT/EBITDA — not scored this session (Phase 02 not reached) but noted for context in §4 (~76× TTM).
- **Fast Grower**: Peter Lynch's term for EPS growth >15%/yr for 3+ years on a reliable earnings base — DOCN would not have qualified given its short, one-off-distorted GAAP profitability history.
- **FCF / FCF Yield / FCF/NI conversion ratio**: Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check) — central to §3.2's FCF Quality sub-score and the (non-firing) hard-disqualifier check in §3.1.
- **Forward PE**: Price ÷ next-twelve-months' expected EPS; ~73× for DOCN, noted for context only (§4).
- **Gain on debt extinguishment**: a one-off gain from retiring debt below carrying value, contributing alongside the tax-valuation-allowance release to DOCN's inflated Q3 2025 reported net income. *(New term — added to glossary.md this session.)*
- **GAAP**: Generally Accepted Accounting Principles — the standard US accounting rulebook.
- **Gross Margin**: Gross Profit ÷ Revenue — one of this framework's Quality Score Margins sub-score inputs (58.49% TTM for DOCN).
- **Hard disqualifier**: a Quality Score condition that fails a company regardless of weighted score — none fired for DOCN this session (§3.1), though the FCF/NI conversion check is trending toward one.
- **Hurdle rate**: the minimum acceptable annual return (10%) this framework's Upside/Downside Modifier measures against — not reached this session (Phase 02 not computed).
- **IaaS (Infrastructure as a Service)**: the cloud-computing model (raw compute/storage/networking) that is DigitalOcean's core business. *(New term — added to glossary.md this session.)*
- **Invested Capital**: debt + equity − cash, the ROIC denominator ($1.446B for DOCN as of 2026-03-31).
- **Moat**: a durable competitive advantage protecting a business's profits — scored 20.0 (1 of 5 signals) for DOCN this session, the single largest driver of the Quality Score shortfall.
- **NDR (Net Dollar/Revenue Retention)**: the percentage of recurring revenue from an existing customer cohort retained/expanded a year later — DOCN's blended Q1 2026 NDR was 101%, higher for larger customer segments. *(New term — added to glossary.md this session.)*
- **Net Debt/EBITDA**: this framework's primary balance-sheet-risk gate — 1.722× for DOCN using the current (2026-03-31) balance sheet, vs. a stale 4.29× using only the FY2025 year-end figures (§2.5).
- **Net Margin**: Net Income ÷ Revenue — DOCN's TTM normalized figure is 21.15%.
- **NOPAT**: Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the ROIC numerator.
- **NYSE**: the US stock exchange DOCN trades on.
- **PEG ratio**: PE ÷ earnings growth rate — not computed this session (Phase 02 not reached; DOCN would not have qualified as a Fast Grower regardless — see above).
- **Quality Score**: this framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to reach Phase 02. DOCN scored 51.4 (range 51.4–61.5 across sensitivities tested).
- **Registered direct offering**: a public share offering sold directly to selected investors — DigitalOcean's Q1 2026 $887.9M raise (and a further one announced July 2026) used this structure. *(New term — added to glossary.md this session.)*
- **RPO (Remaining Performance Obligations)**: the total dollar value of DigitalOcean's contracted-but-not-yet-recognized revenue, pre-announced to exceed $800M for Q2 2026 (+10x YoY) — cited as Growth sub-score TAM-expansion evidence (§2.6, §3.2).
- **ROIC**: Return on Invested Capital — DOCN's TTM figure is ~12.55% using the company's own disclosed long-term tax-rate convention, below the framework's general 15% Phase 01 quality bar.
- **Term Loan A**: a senior secured term-loan tranche; DigitalOcean fully repaid its $500M Term Loan A using Q1 2026 equity-offering proceeds (§2.5).
- **Treasury yield (10Y)**: this framework's risk-free-rate benchmark (4.63% this session); not used in any calculation since Phase 02 is never reached, but recorded per the standard output format.
- **TTM (Trailing Twelve Months)**: the most recent 12 months of reported results — reconstructed for DOCN this session from Q2 2025 through Q1 2026, since Q2 2026 has not yet reported (§2.3).

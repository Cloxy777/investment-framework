# NEW POSITION — TM (Toyota Motor Corporation, NYSE Sponsored ADR) — 2026-07-12

**Task type:** NEW POSITION (Telegram-scan trigger)
**Date:** 12 Jul 2026 (Sunday — US markets closed since Fri 10 Jul; most recent completed session's close used as the live price, per Rule 0, consistent with today's ASML/TSM sessions)
**10Y US Treasury Yield:** 4.54% (FRED `DGS10`, most recent posted observation, reused/reconfirmed from today's ASML/TSM sessions — **not actually invoked this session**, since the Quality Score gate fails first; see §3)
**Rate Regime Modifier:** Not computed — Phase 02/Rate Environment Gate is never reached (see §3, Result: FAIL)
**Current TM portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — this is Toyota's first-ever `/new-position` evaluation under this framework.
**Sector:** Consumer Discretionary — Automobile Manufacturers (mass-market + luxury, via Lexus), with a large, fully-consolidated captive financial-services arm (Toyota Financial Services / Toyota Motor Credit Corp) that funds vehicle loans and leases.
**Filer type:** Foreign private issuer — Toyota files an annual **Form 20-F** (not a 10-K) and furnishes results via **Form 6-K** (not 8-K/10-Q) with the SEC (CIK **0001094517**), reporting under **US GAAP** (not IFRS — a long-standing NYSE-listing-driven choice, unlike most foreign filers) in **JPY**. Fiscal year = **April 1 – March 31**; "FY2026" = the year ended **31 March 2026**, Toyota's most recently completed and reported fiscal year (Q1 FY2027, April–June 2026, has not yet been reported as of this session).
**ADR structure:** NYSE ticker **TM**, contract_id **275241** ("TOYOTA MOTOR CORP -SPON ADR", confirmed via `search_contracts`) — a conventional **sponsored ADR**. **1 ADS represents 10 ordinary (common) shares** of Toyota (Tokyo Stock Exchange: 7203), effective 1 October 2021 (a ratio change from the prior 1:2, timed alongside Toyota's 5-for-1 forward stock split of its ordinary shares — confirmed via the contemporaneous NYSE/BNY Mellon "DR Ratio Change" notice). This ratio is used throughout §2.5 to convert Toyota's ordinary-share count to ADR-equivalent shares for market cap.
**First-use jargon decode:** see closing Glossary.

---

## 0. Why this session exists — trigger source

A Telegram post on the **tarasguk** channel (post #11362, ~16:35 UTC 2026-07-12) referenced "a new video analyzing Toyota shares and robot manufacturers." Per the operating brief and Rule 0, **Telegram post text is never used as financial data** — it is a trigger only. The post carries no verifiable financial claim to check (it is a promo for third-party video content, not a specific factual assertion about Toyota) — this session independently sources 100% of the data below from Toyota's own SEC filings and cross-checked third-party vendors, exactly as it would for any other `/new-position` run.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$176.45** | IBKR `get_price_history` (contract_id 275241, NYSE), daily bar close for **2026-07-10** (most recent completed trading session — today, 2026-07-12, is a Sunday) |
| ⚠️ Tooling flag | `get_price_snapshot`'s `last` field returned **$174.32** (`is_close: true`) — this exactly matches the **2026-07-09** close in `get_price_history` ($174.32), one session stale, the same recurring `get_price_snapshot`-staleness pattern flagged in today's ASML/TSM sessions and prior sessions (e.g. TSM, NVO). Resolved by using `get_price_history`'s freshest daily bar instead. |
| Independent cross-check | **$176.45**, +1.22% on the day | WebSearch — multiple independent sources agree Toyota (TM) closed 10 Jul 2026 at $176.45 |
| 52-week range | $163.033 (low) – $245.03 (high) | IBKR `get_price_snapshot` `misc_statistics` |
| Dividend yield (live) | 3.4% | IBKR `get_price_snapshot` `dividend_yield` — cross-checked against 3.03% (stockanalysis.com); used IBKR's live figure as the primary Rule-0-compliant source, per this framework's stated broker-data preference (same convention as the TSM session) |
| Analyst consensus PT | $256.52 (avg, "Buy" consensus) | stockanalysis.com — discussed qualitatively only, never as a scored input |
| US 10Y Treasury yield | 4.54% | FRED `DGS10`, reused/reconfirmed from today's ASML/TSM sessions (same date) — flagged here per the standard session header template even though, as shown in §3, the Rate Environment Gate this yield feeds is never reached |

**$176.45 is used as the live price for all arithmetic below.**

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note

Toyota's FY2026 (year ended 31 March 2026) results were furnished via **Form 6-K** on **10 June 2026** (alongside the annual Form 20-F) and are the most current full-year audited-adjacent figures available — Q1 FY2027 (April–June 2026) has not yet been reported. All financial figures below are sourced primarily from Toyota's own SEC 6-K financial-summary exhibits — [FY2026 (filed 2026-06-10)](https://www.sec.gov/Archives/edgar/data/1094517/000119312526213363/d125424dex991.htm), [FY2024 (filed 2024-05-08)](https://www.sec.gov/Archives/edgar/data/1094517/000119312524133537/d735266dex991.htm), and [FY2022 (filed 2022-05-11)](https://www.sec.gov/Archives/edgar/data/1094517/000119312522146839/d323794dex991.htm) — each containing the current and prior fiscal year's full Unaudited Consolidated Statement of Income, Balance Sheet, and Cash Flow Statement. Cross-checked throughout against [stockanalysis.com](https://stockanalysis.com/stocks/tm/financials/) (income statement, balance sheet, cash-flow-statement, and overview pages) and SEC XBRL (`dei:EntityCommonStockSharesOutstanding`, CIK 0001094517) for shares outstanding. Every figure below reconciles between the primary SEC source and the vendor cross-check to within rounding — material exceptions are flagged explicitly (see §2.3, §2.4).

### 2.2 Income statement — 5 fiscal years (JPY millions, primary SEC-sourced, cross-checked stockanalysis.com)

| FY (ended Mar 31) | Revenue | Operating Income | Income Before Taxes | Income Tax Expense | Net Income (incl. NCI) | **Net Income Attributable to Toyota** | Diluted EPS (¥/ordinary share) |
|---|---|---|---|---|---|---|---|
| FY2022 | 31,379,507 | 2,995,697 | — | — | — | 2,850,110 | 205.23 |
| FY2023 | 37,154,298 | 2,725,025 | — | — | — | 2,451,318 | 179.47 |
| FY2024 | 45,095,325 | 5,352,934 | — | — | — | 4,944,933 | 365.94 |
| FY2025 | 48,036,704 | 4,795,586 | 6,414,590 | 1,624,835 | 4,789,755 | 4,765,086 | 359.56 |
| **FY2026** | **50,684,952** | **3,766,216** | **5,152,996** | **1,167,234** | **3,985,761** | **3,848,098** | **295.25** |

Sources: FY2026 and FY2025 — [FY2026 6-K exhibit](https://www.sec.gov/Archives/edgar/data/1094517/000119312526213363/d125424dex991.htm) (Unaudited Consolidated Statement of Income). FY2024 and FY2023 — [FY2024 6-K exhibit](https://www.sec.gov/Archives/edgar/data/1094517/000119312524133537/d735266dex991.htm). FY2022 — [FY2022 6-K exhibit](https://www.sec.gov/Archives/edgar/data/1094517/000119312522146839/d323794dex991.htm).

⚠️ **NCI note (material, used consistently throughout this session):** stockanalysis.com's "Net Income" line (e.g. FY2026: ¥3,985,760M) is **consolidated net income before allocation to noncontrolling interests** — it does not net out the ~¥137,664M (FY2026) / ~¥24,670M (FY2025) attributable to minority shareholders in Toyota's consolidated subsidiaries. **This session uses "Net Income Attributable to Toyota Motor Corporation" throughout** (the shareholder-relevant figure, and the one the company's own diluted EPS is computed from) — cross-tie confirmed: ¥3,848,098M ÷ 13,033,931,974 ordinary shares = ¥295.24/share, matching the reported diluted EPS of ¥295.25 to the cent.

**Cross-check:** revenue and operating income match stockanalysis.com's figures exactly (e.g. FY2026 revenue 50,684,952 vs. stockanalysis's 50,685,000 — rounding only).

**Gross Margin (TTM = FY2026, stockanalysis.com, no separate "Gross Profit" line in Toyota's own SEC income-statement presentation — Toyota's format runs straight from Net Revenues to Cost of Revenues to Operating Income without an intermediate subtotal, so this figure is vendor-derived as Revenue − Cost of Revenues):**

| FY | Gross Margin |
|---|---|
| FY2022 | 19.03% |
| FY2023 | 16.99% |
| FY2024 | 20.77% |
| FY2025 | 19.94% |
| **FY2026** | **16.70%** |

**Not structurally expanding** — the 3yr trend (FY2024 20.77% → FY2025 19.94% → FY2026 16.70%) is a clear **contraction**, driven substantially by US tariffs (see §2.6) — no Margins trend bonus applies.

### 2.3 Balance sheet (JPY millions, primary SEC-sourced)

| Item | FY2026 (2026-03-31) | FY2025 (2025-03-31) |
|---|---|---|
| Cash and cash equivalents | 12,659,622 | 8,982,404 |
| Short-term + current portion of LT debt | 17,581,104 | 15,829,516 |
| Long-term debt | 25,624,365 | 22,963,363 |
| **Total interest-bearing debt** | **43,205,469** | **38,792,879** |
| Total liabilities | 64,502,263 | 56,722,437 |
| Toyota Motor Corporation shareholders' equity | 39,918,854 | 35,924,826 |
| Non-controlling interests | 1,101,214 | 954,088 |
| **Total shareholders' equity (incl. NCI)** | **41,020,068** | **36,878,913** |
| Total assets | 105,522,331 | 93,601,350 |

Source: [FY2026 6-K exhibit](https://www.sec.gov/Archives/edgar/data/1094517/000119312526213363/d125424dex991.htm) (Unaudited Consolidated Balance Sheet — "Total interest-bearing debt" is a sum of the two disclosed debt lines, not a single reported subtotal). Cross-checked against stockanalysis.com's "Total Debt" (43,205,500) and "Cash & Equivalents" (12,659,600) — match to the hundred-million.

⚠️ **Conglomerate rule ([strategy.md](../framework/strategy.md) line 18) applied:** the ¥43,205,469M interest-bearing debt figure above is Toyota's **fully consolidated** balance-sheet total, which already includes **Toyota Financial Services' (TFS) captive-financing debt** (funding the group's global vehicle loan and lease receivables book) — no separate industrial-only breakout was carved out, consistent with the rule's instruction to consolidate rather than exclude captive-financing debt, and with how this framework treated the identical situation for Stellantis's captive-financing subsidiary in the 2026-07-07 STLA session ("already consolidated per the rule, no add-back needed"). This is the central driver of the Balance Sheet sub-score finding in §3.

### 2.4 Cash flow statement — the CapEx/FCF definitional question (the pivotal judgment call this session)

**Two different, both fully SEC-disclosed, "Capital Expenditures" figures exist for an automaker with a large captive-leasing business, and they diverge enormously for Toyota:**

1. **Toyota's own headline figure** — "Capital Expenditures" as presented in its own investor-facing financial summary — is **purchases of property, plant and equipment only** (factories, tooling, equipment), **excluding** spending on vehicles placed into Toyota's own operating-lease programs.
2. **A fuller figure** (matching stockanalysis.com's "Capital Expenditures"/"Free Cash Flow" cash-flow-statement lines) **adds** a second, separately-disclosed SEC line item: **"expenditures for vehicles and equipment on operating leases"** — the cash Toyota spends acquiring the vehicles it leases out to retail/fleet customers through its captive-finance arm, capitalized as "Equipment on operating leases" and depreciated over the lease term.

Both lines are independently confirmed, real, primary-sourced SEC disclosures — reconciled exactly against stockanalysis.com's aggregated figures for every year checked:

| FY | Operating CF | CapEx — PP&E only | CapEx — Equipment on operating leases | **CapEx — Full (both lines)** | **FCF — narrow (OCF − PP&E only)** | **FCF — full (OCF − both lines)** |
|---|---|---|---|---|---|---|
| FY2022 | 3,722,615 | 1,197,266 | 2,286,893 | 3,484,159 | 2,525,349 | **238,456** |
| FY2023 | 2,955,076 | 1,450,196 | 1,907,356 | 3,357,552 | 1,504,880 | **−402,476** |
| FY2024 | 4,206,373 | 1,846,447 | 2,867,660 | 4,714,107 | 2,359,926 | **−507,734** |
| FY2025 | 3,696,934 | 2,134,800 | ~2,768,930* | ~4,903,730 | 1,562,134 | **~−1,206,796** |
| **FY2026** | **5,472,920** | **2,390,600** | ~2,523,940* | **~4,914,540** | **3,082,320** | **~558,380** |

\*FY2025/FY2026 "Equipment on operating leases" lines are backed out as (stockanalysis.com's aggregated CapEx − Toyota's own disclosed PP&E-only CapEx), since a fetch of the individually-itemized SEC line for these two years specifically was not obtained this session — flagged as a light data gap; the FY2022–FY2024 rows are fully itemized from primary SEC sourcing and reconcile exactly to stockanalysis.com's totals, which is why this backing-out method is used with confidence for the two most recent years rather than treated as invented.

**This session adopts the FULL definition (both CapEx lines) as the primary scored FCF, for three reasons, stated explicitly per this framework's "never invent, never silently pick the flattering number" discipline:**
1. **It is fully disclosed, real, cited cash spending** — not an invented or estimated figure — Toyota's own 20-F/6-K separately itemizes both lines every year.
2. **It is the more conservative reading**, consistent with this framework's general skepticism toward a company's own preferred/narrower non-GAAP-adjacent framing (see the Adjusted EBITDA / Core EPS / AOI glossary entries) — Toyota's own headline "Capital Expenditures" line is the company's *chosen* presentation, not an audited GAAP subtotal, and excluding the leasing-fleet spend understates the cash genuinely consumed running the group's captive-finance arm every year.
3. **It follows the same Conglomerate Rule logic already applied to debt in §2.3** — if TFS's captive-financing *debt* is consolidated into the Balance Sheet sub-score rather than carved out favorably, the *capital spending* that debt funds should be consolidated into the FCF calculation on the same basis, not excluded.

**This is flagged as a genuine, material judgment call — but see §3.1: the ultimate Phase 01 FAIL conclusion is robust regardless of how this specific question is resolved**, because the Net Debt/EBITDA hard disqualifier fires unambiguously on its own, independent of this CapEx question entirely.

**D&A** (stockanalysis.com, used for EBITDA below): FY2022 1,821,880 / FY2023 2,039,900 / FY2024 2,087,070 / FY2025 2,251,230 / **FY2026 2,392,520** — a smooth, plausible upward trend consistent with Toyota's growing PP&E/leased-asset base (Total Assets grew ¥67.7T → ¥105.5T over the same period); not independently cross-checked against a primary SEC D&A line this session, flagged as a light data gap that does not change this session's conclusion (see §3.1 robustness note).

### 2.5 Shares outstanding / ADR ratio / Market Cap

```
Ordinary shares outstanding (31 Mar 2026, SEC XBRL dei:EntityCommonStockSharesOutstanding) = 13,033,931,974
÷ 10 (ADR ratio, 1 ADS = 10 ordinary shares, effective 1 Oct 2021)                          = 1,303,393,197 ADR-equivalent shares

Market Cap (ADR basis) = $176.45 × 1,303,393,197 = $230,013,905,020  (≈ $230.0B)
```

⚠️ **Vendor discrepancy flagged:** stockanalysis.com's own headline "Market Cap" figure reads **$206.95B** — roughly 10% below this session's own computed $230.0B using SEC-sourced shares outstanding, the confirmed ADR ratio, and this session's own live price. The source of the gap could not be cleanly identified this session (possibly a stale price snapshot or a different share-count convention on the vendor's end) — this session's own from-first-principles calculation above (SEC share count ÷ confirmed ADR ratio × Rule-0 live price) is used instead of the vendor's headline figure, consistent with Rule 0's "never infer, always verify independently" discipline. This does not affect the Quality Score (which uses no market-cap-based inputs) but would matter if this session proceeded to Phase 02 (it does not — see §3).

### 2.6 Qualitative context — growth, tariffs, and moat evidence (cited)

- **Global sales leadership:** Toyota sold **11,322,575 vehicles worldwide in 2025** — its **sixth consecutive year as the world's largest automaker**, ahead of Volkswagen Group's 8.98M. [Source: CBT News, "Toyota retains global sales crown in 2025."]
- **Hybrid dominance:** Toyota sold **4.4 million hybrid vehicles globally in 2025** — no competitor came close to matching that volume; US hybrid sales alone rose **+17.6% YoY** to 1,183,248 units, with electrified vehicles (hybrid/PHEV/EV/fuel-cell) reaching **nearly half of all US sales**. [Source: Carbuzz, "Toyota Sold 4.4 Million Hybrids In 2025."]
- **Electrification targets:** Toyota targets >5.5M annual electrified-vehicle sales (incl. ≥1M zero-emission) by 2030, and 3.5M annual BEV sales by 2030 — a company-disclosed forward target, cited here as directional TAM-expansion context (not a scored guidance input, per valuation-scoring.md's explicit rule against scoring self-reported guidance).
- **US tariffs — a real, material, documented headwind:** US tariffs cut Toyota's consolidated FY2026 operating income by **¥1,380.0 billion (~$8.8B)**, turning Toyota's North America segment **operating-loss-making** (a −1.4% margin) for the year despite record US unit sales (+8.0% to 2,518,071 vehicles). Toyota's own **FY2027 guidance** (furnished, not scored per this framework's guidance rule) projects **further** profit deterioration — operating income guided to ¥3,000.0B (down from ¥3,766.2B), driven by persistent tariff costs plus a new ¥670B Middle East materials/expense headwind. [Sources: WardsAuto "US tariffs erase all of Toyota's North America profits in FY2026"; TradingKey; Investing.com FY2026 slides coverage.] This guidance is cited here as *qualitative risk context* only — it is not used to compute the Growth sub-score's +10/−10 modifier (see §3.2), consistent with the framework's rule that forward guidance is a re-valuation *trigger*, never a scored input.
- **Credit rating:** S&P **A+** (affirmed, as of 31 May 2026); Moody's **A1** (affirmed, outlook stable, June 2025) — solidly investment-grade. [Sources: cbonds.com; investing.com/Moody's coverage.] Cited for context in the Balance Sheet discussion (§3.1) — Toyota does **not** qualify for the Upgrade 5 asset-light override regardless of this rating (see §3.1).
- **Brand premium / resale value:** Toyota won Kelley Blue Book's **Best Resale Value: Brand** award for the **sixth consecutive year** in 2026 (53% average 5-year retained value); Lexus won **Best Resale Value: Luxury Brand** for the **fifth consecutive year** (47% average). [Source: Kelley Blue Book 2026 Best Resale Value Award Winners, prnewswire.com/kbb.com.]

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | Toyota data (FY2026 = TTM equivalent, per §2.1) | Verdict |
|---|---|---|
| **Net Debt/EBITDA over its applicable threshold** (2.5× standard, or 4× under the Upgrade 5 asset-light override) | Net Debt = Total interest-bearing debt (43,205,469) − Cash (12,659,622) = **¥30,545,847M**. EBITDA = Operating Income (3,766,216) + D&A (2,392,520) = **¥6,158,736M**. **Net Debt/EBITDA = 30,545,847 / 6,158,736 = 4.96×.** Toyota does **not** qualify for the Upgrade 5 asset-light override in the first place (it is a large PP&E-heavy manufacturer, not a payment network/exchange, and its debt is not 100% financial — a meaningful share funds industrial manufacturing capacity, not just TFS receivables) — but even under that override's more permissive 4× threshold, **4.96× still exceeds it.** **Robustness check:** even if the D&A figure (§2.4, vendor-sourced, not independently primary-verified) were 20% understated, EBITDA would rise to ~¥7.4T and the ratio would still be ~4.13× — still over both thresholds. This conclusion does not depend on the CapEx/FCF judgment call in §2.4 at all. | **FIRES — unambiguously, robust to reasonable data-precision variation.** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | Using this session's adopted **full** CapEx/FCF definition (§2.4): FCF/NI(attributable) — FY2024: −507,734/4,944,933 = **−10.3%** · FY2025: −1,206,796/4,765,086 = **−25.3%** · FY2026: 558,380/3,848,098 = **+14.5%**. **All three of the most recent three fiscal years sit far below 70%** — including the current (FY2026) year, which does *not* break the streak (unlike the narrower-definition sensitivity check below). No growth-capex carve-out applies: the leased-vehicle spending driving this is **recurring core-business capex** (replenishing an ongoing captive-leasing fleet), not a one-off, documented capacity-expansion program in the TSM 2nm/N2-node sense — there is no cited evidence this is temporary or will reverse. | **FIRES under this session's adopted (full) definition.** ⚠️ *Sensitivity check, disclosed for transparency:* under the narrower, Toyota-preferred definition (PP&E-only CapEx), FY2024 (47.7%) and FY2025 (32.8%) are also both below 70%, but FY2026 recovers to 80.1% — breaking the most-recent-window streak, meaning this specific disqualifier would **not** currently fire under that alternative reading. **This does not change the overall Phase 01 result** — the Net Debt/EBITDA disqualifier above fires independently either way. |
| **Not FCF-positive for 3+ consecutive years** | Full-definition FCF: FY2023 −402,476 / FY2024 −507,734 / FY2025 −1,206,796 (three consecutive negative years) / **FY2026 +558,380** (positive, breaking the streak). Applying the same "most recent window, broken streak" reading this framework applied to TSM's FCF/NI check on 2026-07-12: the currently-live window does not show 3+ consecutive negative years, since the freshest year (FY2026) is positive. | **Does not currently fire** (narrowly — a genuine monitoring item: three of the last four years were negative under this definition). |

**Two independent hard disqualifiers fire** (Net Debt/EBITDA unambiguously; FCF/NI conversion under this session's adopted, fully-disclosed and reasoned CapEx definition). Per [quality-scoring.md](../framework/quality-scoring.md): *"Hard disqualifiers — fail regardless of weighted score."* The full weighted score is still computed below in full per this framework's "show every calculation, no black-box outputs" standard, and per precedent (the 2026-07-07 STLA session).

### 3.2 Quality Score — full computation

```
PROFITABILITY (25% weight):
  Net Margin (FY2026, NI attributable to Toyota) = 3,848,098 / 50,684,952 = 7.593%
  NetMargin_Component = clamp((7.593/30)×100, 0, 100) = 25.31

  Effective tax rate (FY2026) = Income tax expense / Pretax income = 1,167,234 / 5,152,996 = 22.65%
  NOPAT = EBIT × (1 − eff. tax rate) = 3,766,216 × (1 − 0.2265) = ¥2,913,057M
  Invested Capital = Total Debt + Total Equity − Cash = 43,205,469 + 41,020,068 − 12,659,622 = ¥71,565,915M
  ROIC = 2,913,057 / 71,565,915 = 4.070%
  ROIC_Component = clamp((4.070/30)×100, 0, 100) = 13.57
  *(Low ROIC is a structural artifact of Toyota's captive-finance arm: a large, matched-book leverage
    structure (borrow to fund loan/lease receivables) inflates Invested Capital far more than it inflates
    NOPAT, the same "low-ROA-but-leveraged" dynamic a bank shows — not treated as an error, shown plainly.)*

  Profitability_Score = (25.31 + 13.57) / 2 = 19.44
  FCF-positivity cap check: not FCF-positive for 3+ consecutive years (§3.1) → cap at 40.0 — does not bind
    (19.44 already below the cap).

MARGINS (15% weight):
  Gross Margin (FY2026) = 16.70% (§2.2)
  GrossMargin_Score = clamp((16.70/80)×100, 0, 100) = 20.9
  3yr trend: FY2024 20.77% → FY2025 19.94% → FY2026 16.70% — CONTRACTING, not expanding
    (US tariffs, §2.6) — no +10 trend bonus.

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2023 → FY2026) = (50,684,952 / 37,154,298)^(1/3) − 1 = 10.91%
  Growth_Score (base) = clamp((10.91/25)×100, 0, 100) = 43.6
  TAM/pricing-power modifier: +10 APPLIED. Documented evidence (§2.6, all independently cited, third-party
    or company-primary-sourced): (a) Toyota's sixth consecutive year as the world's #1 automaker by volume
    (11.3M vehicles, 2025, CBT News); (b) unmatched hybrid-vehicle leadership (4.4M hybrids sold globally in
    2025, no competitor close, Carbuzz), with US hybrid sales growing +17.6% YoY; (c) a genuine, cited
    brand-premium/pricing-power signal — Kelley Blue Book's Best Resale Value: Brand award for the sixth
    consecutive year (53% average retained value) — high resale value is a direct, market-priced signal of
    sustained demand without discounting. Tariff-driven margin/profit pressure (§2.6) is real but is a
    trade-policy cost shock layered on top of continuing volume/demand strength, not evidence the underlying
    addressable market is shrinking — that distinction is why this modifier is scored +10 rather than netted
    against a −10 (the tariff effect is instead captured in the Margins sub-score above, avoiding
    double-counting the same fact in two sub-scores).
  Growth_Score = clamp(43.6 + 10, 0, 100) = 53.6

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (FY2026) = 4.96× (§3.1)
  BalanceSheet_Score = clamp(100×(1 − 4.96/4), 0, 100) = clamp(100×(1 − 1.24), 0, 100) = clamp(−24.0, 0, 100) = 0.0

MOAT SIGNAL (15% weight) — checklist, cited evidence only:
  Market share stable/growing:  TRUE — 6th consecutive year as world's #1 automaker by volume, a record
    11.3M vehicles in 2025 (CBT News, §2.6) — a large, multi-year-stable #1 position, not a single-source
    claim.
  Brand premium (pricing power): TRUE — Kelley Blue Book Best Resale Value: Brand, 6 consecutive years
    (Toyota) / 5 consecutive years (Lexus, luxury category) — high, sustained resale value directly reflects
    demand/brand strength without requiring discounting (§2.6).
  Network effect:  FALSE — a mass-market/luxury auto OEM selling a discrete physical product; no two-sided
    marketplace or user-growth-driven value mechanism identified or applicable (consistent with this
    framework's STLA precedent for the same industry).
  Switching costs:  FALSE — a vehicle purchase is a discrete transaction; no material contractual lock-in,
    integration depth, or data/workflow migration cost was found or is applicable (consistent with the STLA
    precedent).
  Scale cost advantage:  FALSE (uncredited) — the Toyota Production System's lean-manufacturing cost
    discipline is widely described qualitatively, but no **cost-per-unit data showing a gap vs. smaller
    competitors** (the framework's specific evidentiary bar) was found this session — left uncredited per
    "never mark a signal true without a cited source," the same standard applied to ASML's and TSM's
    scale-cost-advantage checklist rows on 2026-07-12.
  Moat_Score = (2/5) × 100 = 40.0

FCF QUALITY (10% weight):
  FCF/NI (FY2026, full definition, §2.4/§3.1) = 558,380 / 3,848,098 = 14.51%
  FCFQuality_Score = clamp(((0.1451 − 0.40)/0.60)×100, 0, 100) = clamp(−42.5, 0, 100) = 0.0

QUALITY SCORE = 19.44×0.25 + 20.9×0.15 + 53.6×0.20 + 0.0×0.15 + 40.0×0.15 + 0.0×0.10
             = 4.860 + 3.135 + 10.720 + 0.000 + 6.000 + 0.000
             = 24.715 → rounds to 24.7
```

**Quality Score = 24.7 / 100.0 — fails the 80.0+ gate decisively**, roughly 55 points below the bar. Toyota's genuine operating strengths (global #1 volume leadership, unmatched hybrid franchise, a well-documented brand-premium/resale-value moat signal, investment-grade credit) are real and are credited above — but they are heavily outweighed by the two sub-scores this framework's specific formulas are most sensitive to for a captive-finance-heavy manufacturer: **Balance Sheet (0.0/100, driven by TFS's fully-consolidated leverage against a comparatively modest EBITDA base)** and **FCF Quality (0.0/100, driven by heavy, recurring leased-vehicle-fleet capital spending consuming most-to-all of operating cash flow in 4 of the last 5 fiscal years)**. Even setting aside the two hard disqualifiers entirely, the weighted score alone (24.7) would not come close to clearing 80.0.

### Result: **Phase 01 FAIL**

Per [new-position.md](../.claude/commands/new-position.md) step 2 / operating-brief.md: *"If it's below 80.0, or a hard disqualifier fires, stop and report why rather than proceeding to scoring."* Two independent hard disqualifiers fire (§3.1), and the weighted score (24.7) sits far below the gate regardless. **No Rate Environment Gate, no Phase 02 valuation score, no Composite Score, no DCF/fair-value work, and no order setup were computed** — none of that work is meaningful for a name that fails the quality gate this decisively.

**This is a structural/accounting-conglomerate finding, not a going-concern one.** Unlike the 2026-07-07 STLA session (a genuinely distressed company with negative margins, negative ROIC, and zero moat signals), Toyota's underlying operating business is manifestly healthy — record global sales, industry-leading hybrid volumes, investment-grade credit, a real and cited brand-premium moat signal. The FAIL here is driven almost entirely by how this framework's specific Net Debt/EBITDA and FCF/NI-conversion formulas interact with a large, fully-consolidated captive vehicle-finance/leasing segment — the same structural pattern that would likely affect any major automaker with a large captive-finance arm (Ford, GM, Honda, BMW, etc.) under this framework's current rules. This is worth flagging as a possible framework-methodology gap (see §6) rather than treating it as a verdict on Toyota's business quality per se — but per this framework's explicit rules, the gate is applied as written, not worked around.

---

## 4. Recommendation

# **PASS. Do not open a position.**

No Rate Environment Gate, no Phase 02 valuation score, no Composite Score, no DCF/comparables fair-value work, and no order setup — none of that work is meaningful for a name that fails the 80.0+ Quality Score gate this decisively (24.7/100.0), with two independent hard disqualifiers firing on top. The Telegram trigger (a video-promo post) carried no analytical claim to independently verify or refute beyond naming Toyota as a subject — this session's own independent, from-first-principles Quality Score work is the entire basis for this recommendation.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Any framework-methodology change to how the Conglomerate Rule / Balance Sheet sub-score / FCF Quality sub-score treats a large, fully-consolidated captive-finance segment** — flagged in §3.2 as a possible gap worth discussing in `decisions/` given this session's finding likely generalizes to other major automakers with large captive-finance arms, not just Toyota. Not itself a trigger to re-score Toyota, but a trigger to revisit *whether* this session's specific judgment calls (§2.4's CapEx definition; the "consolidate, don't carve out" application of the Conglomerate Rule to capex as well as debt) were the right call.
- **Toyota's next earnings release** (Q1 FY2027, expected ~August 2026) — standard Rule 9 trigger; would refresh all figures in this session but is unlikely to change the qualitative conclusion (the Net Debt/EBITDA gap to the 2.5×/4× thresholds is far too large — 4.96× vs. 2.5× — to plausibly close in a single quarter).
- Any management change, material M&A, or a >15% unexplained price move (standard Rule 9 triggers).
- **No position opened — nothing to log in `decisions/`.**

---

## Glossary

- **ADR (American Depositary Receipt) / ADS (American Depositary Share)** — a US-exchange-listed security representing shares of a non-US company; Toyota's is a conventional sponsored ADR, 1 ADS = 10 ordinary (Tokyo-listed) shares.
- **BalanceSheet_Score** — this framework's Quality Score sub-score derived from Net Debt/EBITDA; Toyota scored 0.0 (4.96× vs. a 2.5×/4× threshold).
- **CAGR** — Compound Annual Growth Rate.
- **CapEx (Capital Expenditure)** — money spent buying or upgrading physical assets; this session identified two distinct, both real, SEC-disclosed CapEx figures for Toyota (PP&E-only vs. full-including-leased-vehicles) that diverge materially — see §2.4.
- **CIK (Central Index Key)** — the SEC's unique numeric identifier for Toyota (0001094517), used to construct this session's EDGAR filing citations.
- **Composite Score** — this framework's blended 0.0–100.0 ranking (`0.50 × (100 − Quality Score) + 0.50 × Valuation Score`) — not computed this session, since Toyota never clears the Quality Score gate that's a prerequisite for it.
- **Conglomerate rule** — this framework's instruction ([strategy.md](../framework/strategy.md)) to consolidate a captive financial subsidiary's debt into the Net Debt/EBITDA ratio rather than carving it out favorably; the central driver of Toyota's Balance Sheet sub-score finding this session (and, by this session's extension, the CapEx/FCF treatment in §2.4).
- **D&A** — Depreciation & Amortization.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **Effective tax rate** — the actual percentage of pretax income paid as tax in a given period; Toyota's FY2026 rate was 22.65%, used to compute NOPAT.
- **Equipment on operating leases** *(new — not yet in glossary.md)* — vehicles or equipment a company places into its own operating-lease programs (e.g. a customer leasing a Toyota through Toyota Financial Services) rather than selling outright; capitalized on the balance sheet and depreciated over the lease term, with additions to this pool appearing as a distinct, separately-disclosed cash-flow "investing activities" line for automakers with large captive-leasing businesses. This session's central data-sourcing finding (§2.4) is that Toyota's own headline "Capital Expenditures" figure excludes this line, while a fuller, equally SEC-disclosed figure includes it — and the choice between the two materially changes the FCF Quality hard-disqualifier outcome.
- **EPS** — Earnings Per Share.
- **FCF / FCF Yield / FCF-NI conversion ratio** — Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check) — not computed to a Valuation Score this session (Phase 02 never reached), but FCF/NI conversion is central to §3.1's hard-disqualifier finding.
- **Form 6-K** — a furnished report foreign private issuers file with the SEC between annual filings — this session's primary source for Toyota's fiscal-year results.
- **Form 20-F** — the annual report foreign private issuers file with the SEC — Toyota's equivalent of a US 10-K; Toyota is unusual among foreign filers in preparing its 20-F financial statements under **US GAAP** rather than IFRS.
- **Hard disqualifier** — a Quality Score condition that fails a company regardless of weighted score; two independently fire for Toyota this session (Net Debt/EBITDA; FCF/NI conversion, the latter under this session's adopted CapEx definition).
- **Invested Capital** — debt + equity − cash, the ROIC denominator; Toyota's is inflated by its captive-finance segment's leverage.
- **Kelley Blue Book (KBB) Best Resale Value Award** *(new — not yet in glossary.md)* — an annual US automotive-industry award (and associated retained-value study) recognizing vehicle brands/models with the highest projected resale value after a 5-year ownership period; cited in this session as third-party, cited evidence for Toyota's/Lexus's Moat Signal "brand premium" checklist row (Toyota: 6 consecutive years; Lexus: 5 consecutive years).
- **Moat** — a durable competitive advantage protecting a business's profits — scored 40.0 (2 of 5 signals) for Toyota this session.
- **NCI (Noncontrolling Interest)** — the portion of a consolidated subsidiary's equity/earnings belonging to outside shareholders rather than the parent; a material, disclosed distinction this session between Toyota's "Net Income" (before NCI) and "Net Income Attributable to Toyota" (after NCI) — the latter is used throughout.
- **Net Debt/EBITDA** — this framework's primary balance-sheet-risk gate; Toyota's is 4.96×, well over both the standard 2.5× and the (inapplicable) 4× asset-light-override threshold.
- **Net Margin** — Net Income ÷ Revenue.
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator used to compute ROIC.
- **Phase 01–06** — the six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **PT (Price Target)** — an analyst's price forecast; Toyota's sell-side mean target ($256.52) is discussed qualitatively only, never as a scored input.
- **Quality Score** — this framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to reach Phase 02/Composite Score. Toyota scored **24.7**.
- **Qualified Quality List** — the output of Phase 01 screening; Toyota does not make this list.
- **ROIC** — Return on Invested Capital — how efficiently a company turns invested capital into profit; Toyota's is 4.07%, depressed by its captive-finance segment's leverage structure.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price (and primary financial data) before any valuation work.
- **Rule 9** — this framework's list of fundamental events that force an immediate re-valuation: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% unexplained price move.
- **Toyota Production System (TPS)** *(new — not yet in glossary.md)* — Toyota's proprietary lean-manufacturing methodology (just-in-time production, jidoka/built-in-quality, continuous improvement) — widely credited as the origin of "lean manufacturing" globally and a genuine, qualitatively well-documented source of Toyota's cost discipline, though this session did not find the specific cost-per-unit citation this framework's Moat Signal "scale cost advantage" checklist row requires, so it was not credited (§3.2).
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results; for Toyota's April–March fiscal year, this session used FY2026 (ended 31 March 2026) as the TTM-equivalent period, since no newer quarter has yet been reported.
- **XBRL (eXtensible Business Reporting Language)** — the structured, machine-readable format the SEC requires financial-statement figures to be tagged in; used here to confirm Toyota's exact shares-outstanding figure.

# NEW POSITION — MTCH (Match Group, Inc., NASDAQ) — 2026-07-16

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, first-ever evaluation)
**Date:** 16 Jul 2026 (Thursday)
**10Y US Treasury Yield:** 4.58% (FRED `DGS10`, most recent posted observation dated 2026-07-14 — normal 1-day FRED reporting lag; recorded for completeness only, since this session stops at the Quality Gate (§3) before the Rate Environment Gate would apply)
**Current MTCH portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md); grep for "MTCH" returns no match)
**Prior coverage:** None — first-ever `/new-position` or `/rescore` pass on this ticker (no existing file in `watchlist/in-portfolio/MTCH/` or `watchlist/not-in-portfolio/MTCH/`)
**Sector:** Communication Services — Internet Content & Information (online dating / "social connection apps")
**Filer type:** US domestic filer — CIK **891103** ("Match Group, Inc.," Nasdaq: MTCH — confirmed via SEC `submissions` API against a second, unrelated CIK 1575189 "Match Group Holdings II, LLC" that shares the search name but is not the public filer), Form 10-K/10-Q.
**First-use jargon decode:** see closing Glossary (§8).

---

## 0. Why this session exists — trigger source

A Telegram post on **FinnInvestChannel** (post #2945, 2026-07-16, ~15:01 UTC) reported "52-week highs: UnitedHealth Group (UNH) and Tinder" (and separately, 52-week lows for Oklo, NuScale, Oracle). Per the operating brief, **Telegram post text is never used as financial data** — it is a trigger only. Tinder is a brand/app wholly owned by Match Group, Inc.; it has no independent stock listing of its own, so "Tinder" in a 52-week-high context unambiguously resolves to Match Group's own ticker, **MTCH** (NASDAQ). MTCH has no existing watchlist entry in this repo and is not a current holding, so per [`/telegram-scan`](../.claude/commands/telegram-scan.md) step 4's first bullet ("No watchlist entry exists at all → `/new-position <TICKER>`"), this warrants a full first-time evaluation — independent of whether the post's own "52-week high" claim turns out to be accurate once checked against a live, independently-sourced price (§1).

---

## 1. Live Price (Rule 0)

Contract disambiguation: `search_contracts("MTCH")` returned several candidates sharing the "MATCH GROUP" name — the correct one is selected on an **exact symbol match** (`MTCH`) on the **NASDAQ** primary US listing, per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0 and the IBKR tool's own disambiguation guidance:

| Candidate | Exchange | Verdict |
|---|---|---|
| **`MTCH`, contract_id 430252818, "MATCH GROUP INC"** | NASDAQ | ✅ **Used** — exact symbol, US primary listing |
| `MTCH.OLD`, contract_id 212813173 | VALUE | ❌ Legacy/delisted contract wrapper, not tradeable |
| `MTCH1`, contract_id 431809070 | MEXI (Mexico) | ❌ Secondary Mexican listing, not the US primary |
| `MTCH1`, contract_id 54386910, "MATECH CORP" | DOLLR4LOT | ❌ Different company entirely (Matech Corp, not Match Group) |
| `MTCH.STK` / `MTCH.CSH`, CORPACT | n/a | ❌ Tender-offer corporate-action wrapper contracts, not the common stock |

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$40.80** | IBKR `get_price_snapshot`, `last` field, timestamp 1784218785 (2026-07-16T16:19:45Z), contract_id **430252818** (NASDAQ, "MATCH GROUP INC"), `is_close: false` (intraday, market open) |
| Day change | **+$0.69 (+1.72%)** | IBKR `get_price_snapshot` `change` field |
| Bid/Ask | $40.73 / $40.77 | IBKR `get_price_snapshot` `bid_ask` field |
| 52-week high (pre-today) | $40.165 | IBKR `misc_statistics` (`high_13w`/`high_26w`/`high_52w` all equal $40.165, i.e. the prior high was itself set within the last 13 weeks) |
| 52-week low | $28.629 | IBKR `misc_statistics` `low_52w` |
| US 10Y Treasury yield | 4.58% | FRED `DGS10`, as-of 2026-07-14 (not used this session — see header) |

Today's $40.80 print exceeds the pre-existing 52-week high of $40.165 — **this independently corroborates, via live IBKR data rather than the post's own text, that MTCH is trading at a fresh 52-week high today**, consistent with (but not sourced from) the triggering Telegram post. $40.80 is used as the live price for reference throughout this session; no order-setup arithmetic is performed, since the Quality Gate fails below (§3).

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note and known data-access issue

`yfinance`'s default HTTP backend (`curl_cffi` with Chrome TLS impersonation) failed in this session's network environment (`SSLError: Connection reset by peer` on every request, reproduced against a bare `curl_cffi` session with `impersonate="chrome"`, while a bare session with no impersonation succeeded) — worked around by setting `YF_DISABLE_CURL_CFFI=1`, which falls back to plain `requests` with a standard browser User-Agent header. This successfully returned all needed `yfinance` fields, and every load-bearing figure it returned (revenue, net income, cash, debt, operating cash flow, capital expenditure) was independently **cross-checked to the dollar against Match Group's own primary SEC filings** below — the one field that did *not* reconcile (`yfinance`'s quarterly "EBIT"/"Operating Income" fields, which add back "Impairment and amortization of intangibles" as if non-operating) was discarded in favor of GAAP Operating Income reconstructed directly from the filings (§2.3), consistent with "never invent or estimate financial data" / never trusting a vendor figure that doesn't reconcile to the primary source.

Primary sources used:
- **10-K for FY2025**, filed 2026-02-26, accession 0000891103-26-000025 (`mtch-20251231.htm`)
- **10-Q for Q1 2026** (three months ended March 31, 2026), filed 2026-05-06, accession 0000891103-26-000073 (`mtch-20260331.htm`) — includes Q1 2025 comparatives
- **10-Q for Q3 2025** (three and nine months ended September 30, 2025), filed 2025-11-05, accession 0000891103-25-000180 (`mtch-20250930.htm`) — includes Q3 2024/9mo 2024 comparatives, used to back out Q2 2025 and Q4 2025 standalone quarters by subtraction (no standalone Q2/Q4 filing exists; both are always reported cumulatively)
- `yfinance` (fallback mode) for quarterly Pretax Income, Tax Provision, Net Income, Operating Cash Flow, and Capital Expenditure lines — each independently verified against the 10-Q figures below

### 2.2 TTM reconstruction (Q2 2025 + Q3 2025 + Q4 2025 + Q1 2026)

Most recent completed quarter is Q1 2026 (ended March 31, 2026); Q2 2026 earnings are not yet released (calendar shows **2026-08-04**, per `yfinance`). Q4 2025 and Q2 2025 have no standalone SEC filing (10-Qs report cumulative six/nine-month periods) and are derived below by subtraction — shown explicitly, not asserted.

**Revenue, Net Income (all $M, primary/cross-checked):**

| Item | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 | TTM |
|---|---|---|---|---|---|
| Revenue | 863.738 | 914.275 | 878.006 | 863.934 | **3,519.953** |
| Net income attrib. to MTCH shareholders | 125.478 | 160.756 | 209.649 | 166.837 | **662.720** |

Revenue TTM cross-checks exactly to `yfinance`'s own `totalRevenue` field (3,519,952,896); Net income TTM cross-checks to `netIncomeToCommon` (662,713,024) within $7K (a Q3 2025 noncontrolling-interest rounding difference between the `yfinance` field, 160.749, and the 10-Q's own 160.756 — immaterial).

**GAAP Operating Income (used as EBIT) — reconstructed directly from primary filings, not `yfinance`'s field (see §2.1):**

```
FY2025 Operating income (10-K, full year)              = $872.529M
Nine months ended Sep 30, 2025 Operating income (10-Q)  = $587.848M
  → Q4 2025 (derived)  = 872.529 − 587.848             = $284.681M

Nine months ended Sep 30, 2025 Operating income (10-Q)  = $587.848M
Q3 2025 (10-Q, three months standalone)                 = $221.334M
Q1 2025 (10-Q, three months standalone, from Q1'26 10-Q)= $172.593M
  → Q2 2025 (derived)  = 587.848 − 221.334 − 172.593    = $193.921M
  [check: 172.593 + 193.921 + 221.334 = 587.848 ✓]

Q1 2026 (10-Q, three months standalone)                 = $236.416M

EBIT_TTM = 193.921 + 221.334 + 284.681 + 236.416 = $936.352M
```

**D&A (Depreciation + Impairment/amortization of intangibles, both income-statement lines) — same derivation method:**

```
Q1 2026: Depreciation 14.132 + Impair./amort. intangibles 33.767  = 47.899
Q4 2025 (derived): FY2025 D&A (67.112+38.548=105.660) − 9mo D&A (54.635+29.897=84.532) = 21.128
Q3 2025: Depreciation 14.845 + Impair./amort. intangibles 8.921    = 23.766
Q2 2025 (derived): 9mo D&A (84.532) − Q1'25 (21.729+10.478=32.207) − Q3'25 (23.766)     = 28.559
  [check: 32.207 + 28.559 + 23.766 = 84.532 ✓]

D&A_TTM = 28.559 + 23.766 + 21.128 + 47.899 = $121.352M
EBITDA_TTM = EBIT_TTM + D&A_TTM = 936.352 + 121.352 = $1,057.704M
```

**Pretax income / tax (via `yfinance`, cross-checked to the 10-Qs/10-K exactly — see below):**

| Item | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 | TTM |
|---|---|---|---|---|---|
| Pretax income | 157.705 | 193.638 | 254.707 | 200.531 | **806.581** |
| Tax provision | 32.227 | 32.882 | 45.051 | 33.686 | **143.846** |

Cross-checks: Q1+Q2+Q3 2025 pretax (139.953+157.705+193.638=491.296) matches the 10-Q's own nine-months-ended-Sep-30-2025 figure ($491,296K) exactly; Q4 2025 pretax (254.707) = FY2025 (746.003) − 9mo (491.296) = 254.707 ✓; Q4 2025 tax (45.051) = FY2025 tax (132.542) − 9mo tax (87.491) = 45.051 ✓. **Effective tax rate TTM = 143.846 / 806.581 = 17.84%.**

**Cash flow (via `yfinance`, cross-checked to the Q1 2026 10-Q's cash-flow statement exactly — OCF $194,358K and CapEx $20,384K both match to the dollar):**

| Item | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 | TTM |
|---|---|---|---|---|---|
| Operating cash flow | 243.842 | 320.641 | 322.780 | 194.358 | **1,081.621** |
| Capital expenditure | 12.870 | 13.803 | 14.665 | 20.384 | **61.722** |
| **FCF** | 230.972 | 306.838 | 308.115 | 173.974 | **1,019.899** |

OCF TTM cross-checks exactly to `yfinance`'s `operatingCashflow` field (1,081,620,992).

### 2.3 Balance sheet — primary-sourced (Q1 2026 10-Q, condensed consolidated balance sheet, March 31, 2026)

| Item | Value ($M) | Source |
|---|---|---|
| Cash and cash equivalents | 1,020.095 | 10-Q balance sheet, cross-checks `yfinance` quarterly figure exactly |
| Long-term debt, net | 3,550.473 | 10-Q balance sheet |
| Current maturities of long-term debt (face value) | 423.854 | 10-Q debt-schedule footnote |
| **Total debt** | **3,974.327** | 3,550.473 + 423.854 (cross-checks `yfinance`'s `totalDebt` of 3,974.202 within ~$0.1M — an immaterial discount/premium classification nuance on the current-portion figure) |
| **Total Match Group, Inc. shareholders' equity** | **−218.117** | 10-Q balance sheet, "Total Match Group, Inc. shareholders' equity" line — **negative** (see Glossary; Match Group has reported negative consolidated equity every fiscal year-end from FY2022 through FY2025 and every quarter-end in between) |
| Total assets | 4,407.937 | 10-Q balance sheet |

```
Net Debt        = 3,974.327 − 1,020.095                          = $2,954.232M
Invested Capital = Total Debt + Equity − Cash
                 = 3,974.327 + (−218.117) − 1,020.095             = $2,736.115M
```

Debt composition (10-Q footnote): $450M 4.625% Senior Notes due 2028, $500M 5.625% Senior Notes due 2029, $350M 4.125% Senior Notes due 2030, $500M 3.625% Senior Notes due 2031, $500M 6.125% Senior Notes due 2033, $700M 0.875% Exchangeable Senior Notes due 2026, $423.854M 2.00% Exchangeable Senior Notes due 2030, plus a further ~$575M item in the debt schedule not independently re-labeled in this session's text extraction — total reconciles to the $3,998.854M face-value "Total debt" line in the footnote (before unamortized discount/issuance costs). An undrawn revolving Credit Facility (~$499.4M available) exists alongside this, secured by subsidiary stock, with covenant leverage ceilings of 4.25× (dividend/buyback restriction) and 5.0× (springing maturity) on the company's own (looser, non-GAAP) leverage definition — cited as capital-structure context, not used as a substitute for this framework's own Net Debt/EBITDA calculation.

**No primary-sourced credit rating (Moody's/S&P/Fitch) was found** for Match Group in the filings reviewed or an SEC full-text search — flagged as a data gap (§4.1 explains why it does not change this session's conclusion regardless).

### 2.4 Payers and RPP — company-disclosed KPIs (FY2025 10-K, MD&A)

| | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| **Total Payers (thousands)** | 15,602 | 14,898 (−4.5%) | 14,165 (−4.9%) |
| — Tinder | 10,375 | 9,696 (−7%) | 9,026 (−7%) |
| — Hinge | 1,242 | 1,532 (+23%) | 1,801 (+18%) |
| — Evergreen & Emerging | 3,066 | 2,666 (−13%) | 2,282 (−14%) |
| — MG Asia | 919 | 1,004 (+9%) | 1,056 (+5%) |
| **Total RPP ($/payer/month)** | 17.67 | 19.12 (+8%) | 20.09 (+5%) |
| — Tinder RPP | 15.40 | 16.68 (+8%) | 17.20 (+3%) |

**Total Revenue growth decelerated from +3% (FY2024 vs FY2023) to ~0% (FY2025 vs FY2024, +$7.8M)** — Tinder's continued Payers decline (the dominant brand, 64% of FY2025 Payers) is offsetting Hinge's growth and RPP gains across the portfolio. See Glossary for **Payers** / **RPP** definitions.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years w/o growth-capex explanation | FY2022 131.7% · FY2023 127.3% · FY2024 160.0% · FY2025 166.9% · **TTM 153.9%** | disqualify if 2+ consecutive years <70% | ✅ PASS, by a wide margin every period shown |
| **Net Debt/EBITDA over threshold (2.5× standard)** | **TTM: Net Debt $2,954.232M / EBITDA $1,057.704M = 2.793×** | disqualify if >2.5× (or >4× under Upgrade 5 asset-light override) | ❌ **FAILS — hard disqualifier fires** |
| FCF-positive 3+ consecutive years | FY2022 $476.563M · FY2023 $829.379M · FY2024 $882.141M · FY2025 $1,023.615M — all positive | disqualify if not | ✅ PASS |

**Does the Upgrade 5 asset-light override (4× threshold) apply?** No. Upgrade 5 is scoped to "payment networks, exchanges, or asset-light businesses **where 100% of debt is financial**" with interest coverage >15× and an investment-grade rating. Match Group's debt is ordinary corporate leverage (senior notes and exchangeable notes issued to fund acquisitions and buybacks, secured revolving credit facility) — not a payments/exchange settlement-float balance sheet, so it fails the override's business-type test regardless of rating or coverage. (For completeness: TTM interest coverage = EBIT $936.352M / Interest expense TTM $154.821M [42.525+43.111+37.024+32.160] = **6.05×**, also well under the 15× bar Upgrade 5 would separately require, and no primary-sourced credit rating was found either — §2.3. All three of the override's conditions are unmet or unverifiable; none of that changes the standard 2.5× threshold applying here.)

**Robustness check across EBITDA definitions:** the 2.5× breach holds under every reasonable EBITDA figure this session computed or cross-checked — this session's primary GAAP-reconstructed EBITDA (2.793×), the sum of `yfinance`'s quarterly "EBITDA" line (Net Debt/$1,065.181M = 2.773×), and even `yfinance`'s own (higher, less conservative) trailing `ebitda` info field ($1,107.014M = 2.669×) all exceed 2.5×.

**Hard disqualifier fires: Net Debt/EBITDA (2.793×) exceeds the 2.5× standard threshold.** Per [quality-scoring.md](../framework/quality-scoring.md), this fails the company **regardless of the weighted score below** — "a weighted average can't average away an outright balance-sheet or cash-flow-quality failure." The full weighted computation is still shown below for completeness and audit trail, per this framework's "show every calculation" discipline and precedent (e.g. the 2026-07-06 CCL and 2026-07-10 ORCL sessions).

### 3.2 Quality Score — full computation

```
PROFITABILITY (25% weight):
  Net Margin (TTM) = 662.720 / 3,519.953 = 18.827%
  NetMargin_Component = clamp((18.827/30)×100, 0, 100) = 62.76

  NOPAT = EBIT_TTM × (1 − eff. tax rate) = 936.352 × (1 − 0.1784) = $769.31M
  Invested Capital = Total Debt + Equity − Cash = 3,974.327 + (−218.117) − 1,020.095 = $2,736.115M
  ROIC = 769.31 / 2,736.115 = 28.12%
  ROIC_Component = clamp((28.12/30)×100, 0, 100) = 93.72

  Profitability_Score = (62.76 + 93.72) / 2 = 78.24   (no FCF-positivity cap — 4yr positive confirmed above)

  ⚠️ Data-interpretation caveat: Match Group's negative shareholders' equity (−$218.117M) shrinks the
  Invested Capital denominator, which mechanically inflates the computed ROIC relative to what it would be
  with positive book equity — a genuine artifact of the debt-funded-buyback capital structure, not
  necessarily improved capital efficiency. Not adjusted (per "never invent or estimate"), flagged for human
  review. See Glossary "Negative stockholders' equity."

MARGINS (15% weight):
  Gross Margin (TTM) = 2,597.831 / 3,519.953 = 73.80%
  GrossMargin_Score = clamp((73.80/80)×100, 0, 100) = 92.25

  3yr trend check (FY2022→FY2025, completed fiscal years): 69.90% → 71.64% → 71.51% → 72.80% — modestly
  EXPANDING (+2.9pp over the window), but the +10 structural-trend bonus only applies "while below 40%" per
  quality-scoring.md — moot here since gross margin is already far above 40%. No modifier applies.

  Margins_Score = 92.25

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2022→FY2025) = (3,487.197/3,188.843)^(1/3) − 1 = 3.03%
  Growth_Score (raw) = clamp((3.03/25)×100, 0, 100) = 12.10

  Structural deceleration modifier: −10 applies. Documented, cited evidence (§2.4): Total Payers declined in
  3 consecutive fiscal years (15,602K→14,898K→14,165K), Tinder Payers (64% of FY2025 Payers) fell 7% YoY in
  BOTH FY2024 and FY2025, and total revenue growth itself decelerated from +3% (FY2024) to ~0% (FY2025,
  +$7.8M) — a multi-year, company-disclosed structural pattern, not a single cyclical quarter.

  Growth_Score = clamp(12.10 − 10, 0, 100) = 2.10

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (TTM) = 2,954.232 / 1,057.704 = 2.793×
  BalanceSheet_Score = clamp(100×(1 − 2.793/4), 0, 100) = 30.18

MOAT SIGNAL (15% weight) — 5-signal checklist, every signal evaluated against a specific citation:

  Market share stable/growing — FALSE. Company's own 10-K, verbatim: "The industry for social connection
    apps is competitive and has no single, dominant brand globally." Total Payers declined for 3 straight
    fiscal years (§2.4) — the opposite of "stable or growing."

  Brand premium — FALSE. RPP (price per payer) did rise across most brands in FY2025 (Tinder +3%, Hinge +7%,
    E&E +8%), but for Tinder — the dominant brand at 64% of FY2025 Payers — the RPP increase came WITH a
    simultaneous 7% Payers decline, i.e. a price increase with volume loss, not the "price increases WITHOUT
    volume loss" evidentiary bar quality-scoring.md requires. Hinge alone shows the qualifying pattern
    (Payers +18%, RPP +7%), but Hinge is only 12.7% of total FY2025 Payers — not representative of the
    business as a whole, so not credited at the portfolio level.

  Network effect — FALSE. Dating apps are structurally two/multi-sided matching marketplaces, which would
    ordinarily support a documented mechanism, but the company's own 10-K explicitly frames the industry as
    one where "a large portion of customers use multiple services... concurrently or sequentially" (i.e.
    users multi-home across MG's own brands, and — per the adjacent "low switching costs" risk factor,
    quoted below — likely competitors' apps too). Multi-homing undercuts rather than evidences a
    strengthening network effect, since users aren't locked into growing density on one platform.

  Switching costs — FALSE. Company's own 10-K, verbatim (appears twice in the filing): "The industry for
    social connection apps is competitive, with low switching costs and a consistent stream of new services
    and entrants."

  Scale cost advantage — FALSE. The 10-K describes a "One MG" shared-services model (centralized legal,
    finance, tech, and data functions across ~45 brands) that plausibly reduces overhead, but no cost-per-unit
    figure vs. smaller competitors was found in the filing or elsewhere. quality-scoring.md requires
    "cost-per-unit data showing a gap vs. smaller competitors" — unavailable, so not credited (data gap, not a
    negative finding).

  Moat_Score = (0/5) × 100 = 0.0

FCF QUALITY (10% weight):
  FCF/NI (TTM) = 1,019.899 / 662.720 = 153.9%
  FCFQuality_Score = clamp(((1.539 − 0.40)/0.60)×100, 0, 100) = clamp(189.8, 0, 100) = 100.0

QUALITY SCORE = 78.24×0.25 + 92.25×0.15 + 2.10×0.20 + 30.18×0.15 + 0.0×0.15 + 100.0×0.10
             = 19.560 + 13.838 + 0.420 + 4.527 + 0.000 + 10.000
             = 48.345 → rounds to 48.3
```

**Robustness check (not just a point estimate):** even crediting the two judgment-call sub-scores at their most generous, evidence-unsupported alternate reading (Growth without the structural-deceleration modifier, Moat = 5/5 instead of 0/5):

```
78.24×0.25 + 92.25×0.15 + 12.10×0.20 + 30.18×0.15 + 100×0.15 + 100×0.10
= 19.560 + 13.838 + 2.420 + 4.527 + 15.000 + 10.000 = 65.35
```

**Still well below the 80.0 gate.** The gate-FAIL conclusion is not sensitive to this session's Growth/Moat judgment calls — both of which are, in any case, grounded in the company's own explicit filing language rather than an ambiguous read. And unlike the weighted score, the Net Debt/EBITDA hard disqualifier (§3.1) is a purely GAAP-arithmetic finding with no judgment-call inputs at all — it fails MTCH independently of every sub-score shown above.

### 3.3 Gate result

**Quality Score = 48.3 / 100.0 — FAILS the 80.0+ gate**, and **independently** fails via the Net Debt/EBITDA hard disqualifier (2.793× > 2.5×, §3.1). MTCH fails two independent ways simultaneously, exactly the pattern seen in the 2026-07-06 CCL and 2026-07-10 ORCL sessions. Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md): **stop here — do not proceed to the Rate Environment Gate, Phase 02 valuation scoring, the Composite Score, or fair-value/order-setup work.**

---

## 4. Qualitative Notes

1. **The Telegram trigger's factual claim checked out** — MTCH did print a fresh 52-week high today ($40.80 vs. a pre-existing $40.165 high), independently confirmed via live IBKR data (§1), not the post's own text. A genuinely accurate trigger, unlike some prior sessions' generic reminders — but a 52-week-high price print is explicitly **not** one of this framework's valid triggers for scoring conclusions (Rule 0/CLAUDE.md: "act only on documented triggers... never on price movement alone"); this session's PASS conclusion rests entirely on the primary-sourced fundamentals in §2–3, not on the price action itself.
2. **The single largest driver of the gate failure is leverage, not softness alone** — MTCH's Profitability (78.24) and FCF Quality (100.0) sub-scores are both genuinely strong; a subscription-app business with ~74% gross margins and >150% FCF/NI conversion is a real cash machine. What sinks the Quality Score is a combination of (a) a 2.79× Net Debt/EBITDA ratio — a genuine hard disqualifier, driven by ~$4.0B of debt raised substantially to fund share buybacks (FY2022–2025 buybacks: $482M, $546M, $753M, $789M) against a company that has been shrinking its own equity base rather than growing it, and (b) a near-stalled top line (3.03% 3yr revenue CAGR, decelerating further to ~0% in FY2025) masking a structurally declining flagship brand (Tinder, −7% Payers in each of the last two years) offset only partially by a much smaller, faster-growing Hinge.
3. **The company's own risk-factor language is unusually candid about a weak moat** — two separate, verbatim admissions ("no single, dominant brand globally," "low switching costs... consistent stream of new entrants") drove 3 of the 5 Moat Signal checks to FALSE directly from primary-source text, not inference. This is a case where the standard "risk factors are boilerplate-cautious" prior did not apply; the disclosures were unusually on-point for this framework's specific checklist.
4. **Data gap, non-blocking:** no primary-sourced credit rating (Moody's/S&P/Fitch) for Match Group's debt was found in the filings reviewed or an SEC EDGAR full-text search. This does not change the session's conclusion (§3.1 explains the Upgrade 5 override fails on the business-type test regardless of rating), but is flagged per "never invent or estimate financial data" rather than silently assuming a rating tier.
5. **Framework-fit note for future re-evaluation:** if Hinge's growth (+18-23% Payers YoY across FY2024–2025) continues to scale while Tinder's decline decelerates, and if MTCH begins directing more FCF toward debt paydown rather than buybacks, both the Balance Sheet and Growth sub-scores could improve materially at a future re-check — worth revisiting on the next Rule 9 trigger (e.g. the 2026-08-04 Q2 earnings release) rather than waiting for another Telegram mention.

---

## 5. Recommendation

# **PASS — Quality Gate FAIL (Quality Score 48.3 < 80.0, independently confirmed by the Net Debt/EBITDA hard disqualifier at 2.793× > 2.5×). Do not enter.**

Match Group clears several individual quality bars comfortably (gross margin ~74%, FCF/NI conversion >150%, FCF-positive every year shown) but fails the framework's strict 80.0+ Quality Score gate by a wide margin, and independently fails the hard balance-sheet disqualifier — two separate reasons neither of which the other's absence would cure. **No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup was computed**, per the Quality Score protocol (stop at the gate). Today's 52-week-high price print — the fact that triggered this session — was independently confirmed but is not itself a valid basis for any scoring conclusion under this framework's rules.

---

## 6. Next Review Trigger

- **MTCH's Q2 2026 earnings** (2026-08-04, per `yfinance` calendar) — the standard Rule 9 quarterly trigger; will show whether Tinder's Payers decline is decelerating or continuing, and whether the FY2025 buyback pace (which drove the Net Debt/EBITDA breach) persists into 2026.
- **Any credit-rating action or disclosure** (a rating agency report becoming available would resolve the data gap noted in §4 item 4, though it would not on its own change the Upgrade 5 business-type conclusion).
- **Any capital-allocation shift toward debt paydown** — would be the most direct path to curing the hard disqualifier at a future re-check; absent one, expect the Balance Sheet sub-score to stay depressed.
- **Standard Rule 9 triggers:** management change, material M&A, a macro/rate shift, or a >15% unexplained price move (today's +1.72% move is minor and not itself a trigger).

**No position opened — nothing to log in `decisions/`.**

---

## 7. Data Gaps Flagged

1. **Credit rating** (Moody's/S&P/Fitch) for Match Group's debt — not found in filings reviewed or SEC full-text search; non-blocking (§3.1, §4 item 4).
2. **Cost-per-unit data** vs. smaller dating-app competitors, needed to credit the "Scale cost advantage" Moat Signal — not found; the signal is scored FALSE as a data gap, not a negative finding (§3.2).
3. **TAM-expansion evidence** — no documented evidence of category-level (not just company-level) TAM expansion was found for the "social connection apps" industry; not credited, consistent with "never invent or estimate."

None of these gaps affect the Quality Gate conclusion (§3.3), which is driven by well-sourced, primary-cited figures.

---

## 8. Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CIK (Central Index Key)** | The unique numeric identifier the SEC assigns to every company that files with EDGAR — used to construct the filing-lookup paths this framework pulls SEC data from. |
| **Convertible senior notes** | A bond that can convert into a fixed number of the issuer's shares instead of being repaid in cash, letting the issuer borrow at a lower coupon in exchange for that upside option. Match Group's economically equivalent instruments are labeled "Exchangeable Senior Notes" in its own filings — the same structure under a different house term. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / — before Interest, Taxes, Depreciation, and Amortization — operating profit, and a rough proxy for cash operating profit, respectively. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check) — all comfortably passed by MTCH this session. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted score. MTCH's Net Debt/EBITDA (2.793×) independently fired this check. |
| **Interest coverage (ratio)** | EBIT ÷ interest expense — how many times over a company could pay its interest bill from operating profit. MTCH's TTM figure (6.05×) is well under the 15× bar the Upgrade 5 asset-light override would separately require. |
| **Invested Capital** | The total capital (debt + equity, netted for cash) put to work in a business — the denominator in this framework's ROIC calculation. |
| **Investment grade** | A credit rating (BBB-/Baa3 or higher) signaling low perceived default risk; MTCH's own rating was not found in the sources reviewed (data gap). |
| **Multi-homing** | When customers on one or both sides of a platform routinely use multiple competing platforms at once rather than committing to just one — a documented mechanism that dilutes an otherwise-plausible network effect, cited against MTCH's Network Effect Moat Signal this session. |
| **Negative stockholders' equity (shareholders' deficit)** | When a company's total liabilities exceed its total assets, producing a negative "Total shareholders' equity" line — commonly from funding buybacks with debt faster than retaining earnings. Not itself evidence of insolvency, but shrinks the Invested Capital denominator in this framework's ROIC calculation, inflating computed ROIC without necessarily reflecting improved capital efficiency. MTCH has reported this every year-end since FY2022. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; this framework's primary balance-sheet-risk gate. MTCH's TTM figure is 2.793×, above the 2.5× standard threshold. |
| **Net Margin** | Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit. One of this framework's Quality Score Profitability sub-score inputs (alongside ROIC). |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **Payers** | Match Group's own disclosed metric for the average number of users who paid for at least one of its products in a period — its core paying-user KPI. MTCH's total Payers declined for three consecutive fiscal years. |
| **Quality Score** | This framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to proceed to valuation scoring. MTCH scored 48.3. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns invested capital into profit; a core quality signal in this framework. |
| **RPP (Revenue Per Payer)** | Match Group's own per-user monetization metric — direct revenue ÷ Payers ÷ months in the period. Rose across most brands in FY2025, but for Tinder came alongside a Payers decline, not the "price increase without volume loss" evidentiary bar this framework requires for a Brand Premium credit. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure. |

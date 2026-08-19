# NEW POSITION — MRK (Merck & Co., Inc., NYSE)

**Task type:** NEW POSITION (unattended Telegram-scan trigger, Routine 6, first-ever evaluation)
**Date:** 2026-08-19
**10Y US Treasury yield:** ~4.70% (TradingEconomics, 2026-08-19 snapshot — recorded for the record only; the Rate Environment Gate is never reached this session, see §5)
**Current MRK portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None — first-ever `/new-position` or `/rescore` pass on this ticker (no existing file in `watchlist/in-portfolio/MRK/` or `watchlist/not-in-portfolio/MRK/`, confirmed before this session started)
**Sector:** Health Care — Pharmaceuticals (Large-Cap Diversified Biopharma)

---

## 0. Why this session exists — trigger source

New post on **FinnInvestChannel** (Telegram, post #3118, ~14:48 UTC 2026-08-19): Moderna and Merck announced successful Phase 3 results for a personalized mRNA cancer vaccine (intismeran autogene + KEYTRUDA) reducing melanoma recurrence/spread risk. MRK has no existing watchlist entry and is not a current holding, so per `telegram-scan.md`'s "no watchlist entry exists at all" rule this triggers a full `/new-position` evaluation regardless of the mention's substance — established precedent (2026-08-17 RACE, 2026-08-16 HD/WMT, 2026-08-14 RDDT, 2026-07-19 DOCU first-ever evaluations).

**Independent verification of the trigger (not used as a financial input):** confirmed via WebSearch against primary/press sources — Merck and Moderna jointly announced 2026-08-19 that the Phase 3 **INTerpath-001** trial (1,137 patients with high-risk resected cutaneous melanoma) of **intismeran autogene** (V940/mRNA-4157) plus **KEYTRUDA** (pembrolizumab) met both its primary endpoint (recurrence-free survival, RFS) and key secondary endpoint (distant metastasis-free survival, DMFS) against KEYTRUDA alone, "statistically significant and clinically meaningful" per the companies, with no specific hazard-ratio/percentage data yet disclosed. ([STAT News](https://www.statnews.com/2026/08/19/mrna-cancer-vaccine-trial-melanoma-merck-moderna/), [Merck.com press release](https://www.merck.com/news/merck-and-moderna-announce-phase-3-interpath-001-trial-of-intismeran-autogene-plus-keytruda-met-endpoints-of-recurrence-free-survival-rfs-and-distant-metastasis-free-survival-dmfs-in-patient/), [Fierce Biotech](https://www.fiercebiotech.com/biotech/merck-and-modernas-personalized-cancer-vaccine-slows-recurrence-ph-3-trial), [CNBC](https://www.cnbc.com/2026/08/19/moderna-merck-cancer-vaccine-shows-initial-late-stage-melanoma-data.html)) The Telegram post's characterization checks out. **Nothing about this trial result is used as a quantitative input anywhere below** — every financial figure is independently pulled live per Rule 0, and the trial is treated only as a qualitative Rule 9 catalyst note (§8).

---

## 1. Live Price (Rule 0)

Contract confirmed via `search_contracts("MRK")`: contract_id **70101545**, exchange **NYSE**, description "MERCK & CO INC" — correct primary US listing (Merck KGaA/Germany, MEXI/Mexico cross-listing, and TSE/Canada listings returned but not used — unrelated German conglomerate Merck KGaA and the Canadian cross-listing of this same company).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$149.83** | IBKR `get_price_snapshot`, `last` field, contract_id 70101545 (intraday, ts 2026-08-19 16:14:18 UTC, regular NYSE session — `halted: false`) |
| Cross-check | $149.83 | Yahoo Finance chart API, same intraday minute bar (ts 16:12:06 UTC) — **exact match, $0.00 difference** |
| Prior close | $135.17 | Yahoo Finance chart API (2026-08-18 regular close) |
| Change | +$14.66 (+10.85%) intraday | IBKR `get_price_snapshot` — matches Yahoo's independently-computed $14.66/10.85% exactly |
| 52-week high / low | $151.80 / $77.58 | Yahoo Finance chart `meta` (today's session made a new 52-week high — today's regular-session high hit $151.80) |
| 52-week high / low (IBKR) | $137.91 / $76.35 | IBKR `misc_statistics` — **flagged stale**: IBKR's rolling high/low field had not yet updated to reflect today's intraday move at the time of this snapshot; Yahoo's real-time `fiftyTwoWeekHigh` (which already reflects today's $151.80 print) is used as the operative figure |
| Today's day range | $144.90 – $151.80 | Yahoo Finance chart API |
| Dividend yield | 2.49% | IBKR `get_price_snapshot` |
| Today's volume | ~19.2M shares | IBKR `get_price_snapshot` |

**MRK is up +10.85% intraday** on the INTerpath-001 announcement — a genuine, well-corroborated fundamental catalyst (§0), not an unexplained move; the >15% Rule 9 threshold isn't crossed but is worth flagging given the day's volatility. Analyst consensus 12-month price target sits meaningfully **below** today's live price: **$132–$138** across several polls (S&P Global's 28-analyst poll: $136.85; a 26-analyst poll: $137.73) — noted for context only, not used in any calculation below. This gap suggests the broader analyst consensus has not yet caught up to today's news; a handful of individual analysts moved same-day (Daiwa to $143 from $120; JPMorgan to $150 from $140), but the aggregate consensus figure predates or lags the announcement. ([TradingKey](https://www.tradingkey.com/news/market-movers/262118272-market-movers-mrk-20260819), [Investing.com](https://ca.investing.com/news/stock-market-news/why-is-merck-stock-surging-today-93CH-4807804), [StocksToTrade](https://stockstotrade.com/news/merck-company-inc-mrk-news-2026_08_19/))

---

## 2. Data Sourcing & Method

**`yfinance`'s Python client failed this session** with the same `curl_cffi` TLS/connection-reset error against the outbound proxy documented in prior sessions (e.g. 2026-08-17 RACE, 2026-08-14 CIEN) — a proxy-layer incompatibility, not a data-availability issue. Worked around as those sessions did: calling Yahoo Finance's underlying REST APIs directly via `curl`.

**A further wrinkle this session:** Yahoo's `quoteSummary` endpoint (which normally provides `financialData`/`defaultKeyStatistics`/`summaryDetail`) requires an authenticated crumb/cookie exchange that returned `Invalid Crumb`/`Invalid Cookie` on every attempt today (multiple retries, fresh cookie jars, page-priming) — a harder failure than prior sessions saw. Worked around by using the **`fundamentals-timeseries`** endpoint (works unauthenticated, no crumb needed) for every primary financial-statement figure below (income statement, cash flow, balance sheet, share counts — both annual and quarterly), and **WebSearch/WebFetch against stockanalysis.com, macrotrends.net, and primary company/SEC sources** for market-derived ratios that `fundamentals-timeseries` doesn't carry (forward PE, PEG, 5yr historical PE, market cap/EV cross-checks, credit rating, moat evidence). Every figure used is cited to its specific source below; none is invented or estimated.

**A second, more consequential wrinkle:** MRK's TTM GAAP figures are heavily distorted by two large, real, disclosed one-time charges (§4.2) — flagged extensively throughout §4 with both a primary (unadjusted GAAP) and a normalized-sensitivity reading shown side by side, per "show every calculation."

---

## 3. Data Gathered

### 3.1 Income statement — Yahoo Finance `fundamentals-timeseries` (USD, annual, fiscal year = calendar year)

| Fiscal Year | Revenue | Gross Profit | EBIT | Pretax Income | Tax Provision | Net Income | Diluted EPS |
|---|---|---|---|---|---|---|---|
| FY2022 | $59,283M | $41,872M | $17,406M | $16,444M | $1,918M | $14,519M | $5.71 |
| FY2023 | $60,115M | $43,989M | $3,035M | $1,889M | $1,512M | $365M | $0.14 |
| FY2024 | $64,168M | $48,975M | $21,207M | $19,936M | $2,803M | $17,117M | $6.74 |
| FY2025 | $65,011M | $48,629M | $22,424M | $21,067M | $2,804M | $18,254M | $7.28 |

**FY2023's collapse (EBIT $17.4B → $3.0B, Net Income $14.5B → $0.4B) is the same phenomenon flagged for the TTM window below** — a large acquired-IPR&D charge (~$5.5B, Prometheus Biosciences acquisition) hit R&D expense that year. This is directly relevant background for §4.4's Growth modifier and §7's normalization discussion: this is not the first time Merck's GAAP earnings have been depressed by a large one-time deal-related charge.

**TTM (Q3 2025–Q2 2026, `trailing*` fields, `fundamentals-timeseries`):**

| Metric | TTM value |
|---|---|
| Revenue | $66,569M |
| Gross Profit | $48,573M |
| EBIT | $7,691M |
| Pretax Income | $5,948M |
| Tax Provision | $2,779M |
| Net Income | $3,173M |
| Operating Cash Flow | $19,967M |
| Capital Expenditure | −$3,904M |
| Free Cash Flow | $16,063M |
| Normalized EBITDA | $14,653M |

**Quarterly detail behind the TTM window** (`fundamentals-timeseries`, quarterly fields):

| Quarter | Revenue | EBIT | Pretax Income | Net Income | Diluted EPS |
|---|---|---|---|---|---|
| Q3 2025 (2025-09-30) | $17,276M | $7,072M | $6,745M | $5,785M | $2.32 |
| Q4 2025 (2025-12-31) | $16,400M | $3,831M | $3,420M | $2,963M | $1.19 |
| Q1 2026 (2026-03-31) | $16,286M | −$3,055M | −$3,534M | −$4,240M | −$1.72 |
| Q2 2026 (2026-06-30) | $16,607M | −$158M | −$683M | −$1,335M | −$0.541 |

**Q1 and Q2 2026 both show GAAP operating and net losses despite Revenue growing every quarter** — the reason is identified and quantified in §4.2.

### 3.2 Cash flow & balance sheet — `fundamentals-timeseries`

| Fiscal Year | Operating Cash Flow | Free Cash Flow | Net Income | FCF/NI |
|---|---|---|---|---|
| FY2022 | $19,095M | $14,707M | $14,519M | 101.3% |
| FY2023 | $13,006M | $9,143M | $365M | 2,505%* |
| FY2024 | $21,468M | $18,096M | $17,117M | 105.7% |
| FY2025 | $16,472M | $12,360M | $18,254M | 67.7% |

*FY2023's FCF/NI ratio is meaningless as a percentage (Net Income near-zero from the Prometheus IPR&D charge, denominator effect) — shown for completeness, not used in any check below.

**FCF-positive 3+ consecutive years:** FY2022 ($14,707M) → FY2023 ($9,143M) → FY2024 ($18,096M) → FY2025 ($12,360M) → TTM ($16,063M) — **positive every year, 4+ consecutive years.** Hard disqualifier does not fire.

**FCF/NI rolling-window check (most recently completed 2 fiscal years, per quality-scoring.md's rolling-window clarification):** FY2024 105.7%, FY2025 67.7% — only **one** of the two most recent years is below 70%. Hard disqualifier ("<70% for 2+ consecutive years") does **not** fire.

**Balance sheet — quarterly (most recent 5 quarters, `fundamentals-timeseries`):**

| Item | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 |
|---|---|---|---|---|---|
| Total Debt | $35,402M | $41,374M | $49,339M | $49,117M | $53,906M |
| Cash & Equivalents | $8,007M | $18,169M | $14,565M | $5,327M | $6,849M |
| Stockholders' Equity | $48,993M | $51,850M | $52,606M | $45,878M | $41,933M |
| Invested Capital | $84,395M | $93,224M | $101,945M | $94,995M | $95,839M |

Total Debt climbed from $35.4B (Q2 2025) to $53.9B (Q2 2026) — funding the Cidara and Terns acquisitions (§4.2). Stockholders' Equity fell from a Q4 2025 peak of $52.6B to $41.9B by Q2 2026, tracking the two quarters of GAAP net losses.

**Net Debt (most recent balance sheet, Q2 2026):** $53,906M − $6,849M = **$47,057M**

### 3.3 Credit rating (external cross-check)

Moody's upgraded Merck to **Aa3** (from A1); S&P rates Merck **A+**, both stable outlook, per Merck's May 2026 senior-notes pricing disclosures — both solidly investment-grade, and the Moody's move was an *upgrade*, not a downgrade, occurring in the same year as the two large debt-funded acquisitions below. ([SEC 424B5 prospectus supplement](https://www.sec.gov/Archives/edgar/data/0000310158/000162828026036914/merck-prospectussupplement.htm), [Investing.com](https://www.investing.com/news/stock-market-news/merck--co-sees-ratings-upgrade-to-aa3-by-moodys-ratings-93CH-3945424)) Cited in §7 as external corroboration that rating agencies do not read Merck's current leverage as a genuine credit-risk deterioration — relevant context for, but not a determinant of, the hard-disqualifier check in §4.1.

### 3.4 Growth & moat evidence — cited sources

- **Keytruda market position (Market share):** Keytruda held **~46.2% of the global checkpoint-inhibitor market in 2025** and generated **~$32B in 2025 sales** (pharma's best-selling drug), with H1 2026 sales of $16.40B (+4.2% YoY) — approved for 44 indications across 19 tumor types plus 2 tumor-agnostic approvals in the US, with 2,800+ active clinical studies. Main competitors: Bristol Myers' Opdivo ($4.63B H1 2026, −3.9%) and AstraZeneca's Imfinzi ($3.55B H1 2026, +29%) — both smaller. ([Grand View Research market report](https://www.grandviewresearch.com/industry-analysis/keytruda-market-report), [BioSpace](https://www.biospace.com/business/keytruda-hangs-on-to-best-seller-crown-as-glp-1s-gain-ground))
- **Keytruda pricing power (Brand premium):** Keytruda's US list price rose to **$210,000/year in 2026, a 6% increase YoY**, despite competitive and IRA (Inflation Reduction Act) price-setting pressure looming for 2028 — a price increase sustained alongside continued volume/revenue growth, the textbook pricing-power signal. ([ICIJ investigation](https://www.icij.org/investigations/cancer-calculus/report-mercks-blockbuster-cancer-drug-topped-200000-a-year-under-trump/))
- **Keytruda patent cliff (structural growth-deceleration risk, cited for §4.4):** Keytruda's core patent/exclusivity protection expires **2028**; Merck itself has flagged the drug will be subject to Medicare IRA "price-setting" starting January 1, 2028, and biosimilar competition is widely expected to cut Keytruda sales by an estimated 10–20%+ over the following several years. A newer subcutaneous reformulation ("Keytruda Qlex," approved September 2025) extends patent protection on that specific formulation beyond 2030, but does not prevent biosimilar entry against the original IV formulation. ([Fierce Pharma](https://www.fiercepharma.com/pharma/merck-confident-post-keytruda-future-70b-opportunity-next-decade-growth-drivers), [Pearce IP](https://www.pearceip.law/2025/02/25/merck-msds-keytruda-to-undergo-government-price-setting-in-2026/))
- **Pipeline/TAM-expansion evidence (cited for §4.4):** Merck guides to **$70B+ in new annual revenue opportunity over the next decade** from its post-Keytruda pipeline (oncology combinations, WINREVAIR/sotatercept for pulmonary arterial hypertension, cardiometabolic candidates, and — the subject of this session's trigger — intismeran autogene, the first Phase 3-validated individualized neoantigen cancer vaccine). Animal Health (a diversifying, non-Keytruda segment) is targeted to **double from its 2024 base by the mid-2030s**. ([Fierce Pharma](https://www.fiercepharma.com/pharma/merck-confident-post-keytruda-future-70b-opportunity-next-decade-growth-drivers))
- **Gardasil — a documented, already-materialized structural growth headwind:** FY2025 Gardasil/Gardasil 9 sales fell **39%** to $5.2B, driven mainly by a collapse in Chinese demand (well-documented local-competition and destocking dynamics in the China HPV-vaccine market) — a real, already-realized (not merely forward-looking) structural deceleration sitting inside the trailing 3yr revenue CAGR computed in §4.4. ([BusinessWire Q2 2026 results](https://www.businesswire.com/news/home/20260804781126/en/Merck-Co.-Inc.-Rahway-N.J.-USA-Announces-Second-Quarter-2026-Financial-Results-Highlights-Key-Regulatory-and-Clinical-Milestones-Across-Broad-Diverse-Pipeline))

### 3.5 Moat signal evidence

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | Keytruda ~46.2% of the global checkpoint-inhibitor market (2025), world's best-selling drug, 44 approved US indications (§3.4) — a commanding, well-corroborated #1 position in its class. |
| Brand premium | **TRUE** | Keytruda's US list price rose 6% YoY to $210,000/year in 2026 even as volume/revenue kept growing and competitive/regulatory pricing pressure loomed (§3.4) — sustained price increase without volume loss, the framework's specified evidence bar. |
| Network effect | **FALSE** | No two-sided-marketplace or user-growth-driven-value mechanism — Merck is a manufacturer/innovator of patented drugs, not a platform business. Not applicable. |
| Switching costs | **FALSE** | No specific, cited switching-cost mechanism found (e.g. a documented contractual-lock-in or workflow-migration cost). Prescriber/formulary inertia during patent life is plausible but not backed by a specific citation this session — marked FALSE per "never mark a signal true without a cited source." |
| Scale cost advantage | **FALSE** | Merck is the #1 pharma company by R&D spend ($15.78B in 2025, per PharmaShots' industry ranking) — R&D-scale leadership, not the specific **cost-per-unit** evidence quality-scoring.md requires for this signal. No cost-per-unit-vs-smaller-competitor data found. Marked FALSE per the same "cited source" discipline. |

```
Moat_Score = (2/5) × 100 = 40.0
```

---

## 4. Phase 01 — Quality Score (2026-06-29 methodology)

### 4.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years without a documented growth-capex explanation | FY2024 105.7% / FY2025 67.7% (the two most recently completed fiscal years) — only 1 of 2 below 70% | disqualify if 2+ consecutive years sub-70% | ✅ **PASS** |
| FCF-positive 3+ consecutive years | Positive every year FY2022–FY2025 and TTM (5 consecutive periods) | disqualify if not | ✅ **PASS**, clean |
| Net Debt/EBITDA over its applicable threshold (2.5× standard) | **GAAP TTM: 3.211×** ($47,057M Net Debt ÷ $14,653M TTM EBITDA) | disqualify if >2.5× | ❌ **FIRES** on the primary (unadjusted GAAP) reading — see §4.2 for full context |

**One hard disqualifier fires on the primary GAAP basis.** Per quality-scoring.md: *"fail regardless of weighted score."* Full context and a normalized sensitivity reading follow immediately below (§4.2) before the rest of the weighted score is shown for completeness (§4.3–4.8), consistent with "show every calculation" — but the gate result (§4.9) does not wait on that weighted total.

### 4.2 Why the primary reading looks this way — the IPR&D charges, shown in full

Merck's TTM GAAP EBIT ($7,691M) and Net Income ($3,173M) are both severely depressed by **two large, real, dollar-quantified, publicly disclosed acquired-IPR&D (in-process research & development) charges** that GAAP requires be expensed immediately (not capitalized) because the acquired research programs had no alternative future use at each deal's close:

| Acquisition | Charge | Per-share impact | Quarter recognized | Source |
|---|---|---|---|---|
| Cidara Therapeutics | **$9.0 billion** | $3.62/share | Q1 2026 | [TIKR](https://www.tikr.com/blog/merck-reports-16-3b-q1-revenue-despite-a-9b-one-time-cidara-charge), Merck FY2026 guidance disclosures |
| Terns Pharmaceuticals | **$5.7 billion** | $2.31/share | Q2 2026 | [TradingView/Quartr summary](https://www.tradingview.com/news/urn:summary_document_report:quartr.com:3672524:0-mrk-q2-2026-revenue-rose-5-to-16-6b-but-net-loss-reached-1-3-b-due-to-acquisition-related-r-d-charges/), Merck Q2 2026 earnings release |
| **Combined, both inside the TTM window (Q3 2025–Q2 2026)** | **$14.7 billion** | $5.93/share | — | — |

Both charges fall inside this session's TTM window (Q3 2025–Q2 2026), which is why GAAP TTM EBIT/Net Income read so much lower than the FY2024/FY2025 annual figures in §3.1. **This is not the first time**: a ~$5.5B IPR&D charge from the 2023 Prometheus Biosciences acquisition depressed FY2023 EBIT to $3.0B and Net Income to just $0.4B (§3.1) — a recognizable pattern from Merck's pipeline-replenishment M&A strategy (addressing the 2028 Keytruda patent cliff, §3.4), not a one-off in the strictest sense.

**This framework's Non-GAAP glossary entry and Rule 6 both bear directly on how to treat this:** Rule 6 ("normalize before you value") explicitly calls for stripping out one-time items, while the Non-GAAP entry (added in an earlier MRK-unrelated session) states this framework "scores off GAAP figures throughout... consistent with not scoring self-reported, company-adjusted metrics." Reconciling these: **this session uses the unadjusted GAAP TTM figures as the primary, scored/binding basis** (below and in §4.3–4.8) — consistent with treating quality-scoring.md's hard disqualifiers as strict and non-discretionary by design ("a weighted average can't average away an outright balance-sheet or cash-flow-quality failure" — the same design intent should extend to not letting analyst judgment average away a hard-disqualifier breach either). A full **normalized sensitivity reading**, excluding both specifically-quantified charges, is shown in §4.9 as required context — not as a substitute for the primary score.

**Independent corroboration that the market/rating agencies do not read this as a genuine leverage deterioration:** Moody's *upgraded* Merck to Aa3 in the same period these charges were recognized (§3.3) — a credit-rating agency explicitly modeling forward cash flows and leverage capacity concluded the opposite of what the raw GAAP TTM Net Debt/EBITDA ratio alone would suggest. This is exactly the kind of context the framework wants shown, not silently resolved either way.

### 4.3 Profitability (25% weight)

```
Net Margin (TTM, GAAP) = $3,173M / $66,569M = 4.77%
NetMargin_Component = clamp((4.77/30)×100, 0, 100) = 15.89
```

**ROIC:**
```
Effective tax rate (TTM, GAAP) = $2,779M / $5,948M = 46.72%   (distorted upward — the IPR&D charges reduce pretax
                                                                 income without a corresponding tax benefit, since at
                                                                 least the Cidara charge is disclosed as non-tax-deductible)
NOPAT (TTM) = EBIT × (1 − eff. tax rate) = $7,691M × (1 − 0.4672) = $4,098M
Average Invested Capital (Q1+Q2 2026) = ($94,995M + $95,839M) / 2 = $95,417M
ROIC = $4,098M / $95,417M = 4.29%
ROIC_Component = clamp((4.29/30)×100, 0, 100) = 14.31
```

```
Profitability_Score = (15.89 + 14.31) / 2 = 15.10   (no FCF-positivity cap — FCF positive every year, §3.2)
```

### 4.4 Margins (15% weight)

```
Gross Margin (TTM) = $48,573M / $66,569M = 72.97%
GrossMargin_Score = clamp((72.97/80)×100, 0, 100) = 91.21
```

**No +10 structural-trend bonus:** gross margin is already far above the 40% threshold (70.6% FY2022 → 73.2% FY2023 → 76.3% FY2024 → 74.8% FY2025 → 72.97% TTM) — the bonus is explicitly reserved for a margin *below* 40% that's structurally improving, which doesn't apply here. No meaningful structural trend either way in recent years (broadly flat-to-slightly-declining off a 2024 peak).

`Margins_Score = 91.21`

### 4.5 Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $59,283M → FY2025 $65,011M) = (65,011/59,283)^(1/3) − 1 = 3.12%
Growth_Score (raw) = clamp((3.12/25)×100, 0, 100) = 12.49
```

**Modifier — genuinely mixed evidence, shown in full rather than picking a side:**
- **Structural-deceleration case (−10 candidate):** Gardasil's FY2025 revenue fell 39% ($5.2B), an *already-materialized* structural headwind (Chinese-market collapse, not cyclical) sitting directly inside the 3.12% trailing CAGR computed above; separately, Keytruda's well-documented 2028 patent cliff (§3.4) is a forward, structural (not cyclical) risk to the company's largest single revenue line (~50% of pharma sales).
- **TAM-expansion case (+10 candidate):** Merck's own guided $70B+ in new decade-ahead revenue opportunity from its post-Keytruda pipeline, Animal Health's planned doubling by the mid-2030s, and — the subject of this session's trigger — a first-ever Phase 3-validated individualized neoantigen cancer vaccine (intismeran autogene) now positioned for a future regulatory filing (§0, §3.4).

**Net treatment: 0 (the two documented, cited signals are applied and shown to cancel)** rather than arbitrarily picking one side — the deceleration evidence is concrete and already-realized (Gardasil) while the expansion evidence is real but more forward/pipeline-dependent (regulatory approval and commercial launch still ahead for most of it, including today's melanoma-vaccine data). Showing both and netting to zero is the more defensible, transparent treatment given quality-scoring.md doesn't specify how to weigh genuinely conflicting evidence.

```
Growth_Score = 12.49 + 0 = 12.49
```

### 4.6 Balance Sheet (15% weight)

```
Net Debt/EBITDA (TTM GAAP, primary) = $47,057M / $14,653M = 3.211×
BalanceSheet_Score = clamp(100 × (1 − 3.211/4), 0, 100) = 19.71
```
`BalanceSheet_Score = 19.71` — and, independently of this continuous score, the same 3.211× figure is what fires the hard disqualifier in §4.1 (see §4.2 and §4.9 for the normalized-basis alternative, 1.603×).

### 4.7 Moat Signal (15% weight)

Per §3.5: 2 of 5 signals TRUE (Market share, Brand premium).
```
Moat_Score = (2/5) × 100 = 40.0
```

### 4.8 FCF Quality (10% weight)

```
TTM FCF/NI = $16,063M / $3,173M = 506.2%   (>>100%, purely a denominator effect — Net Income is severely
                                              depressed by the IPR&D charges while FCF, a cash-flow-statement
                                              measure, is barely affected since the charges are non-cash)
FCFQuality_Score = clamp(((5.062 − 0.40)/0.60)×100, 0, 100) = 100.0  (capped)
```
`FCFQuality_Score = 100.0` — **flagged as not a meaningful "excellent cash quality" signal in this instance**: it's an artifact of the same Net Income distortion driving the low Profitability score, not genuine evidence of unusually strong earnings-to-cash conversion. FY2025's own audited annual ratio (67.7%, §3.2) — itself right at the 70% disqualifier line — is the more representative read of Merck's normal-year cash conversion.

### 4.9 Quality Score — final calculation (primary, GAAP TTM)

```
Quality Score = (Profitability × 0.25) + (Margins × 0.15) + (Growth × 0.20)
              + (BalanceSheet × 0.15) + (Moat × 0.15) + (FCFQuality × 0.10)

              = (15.10 × 0.25) + (91.21 × 0.15) + (12.49 × 0.20)
              + (19.71 × 0.15) + (40.0 × 0.15) + (100.0 × 0.10)

              = 3.775 + 13.6815 + 2.498 + 2.9565 + 6.00 + 10.00

              = 38.91  →  rounds to 38.9
```

**Gate result: FAIL — 38.9 < 80.0** (41.1 points short), **and independently, the Net Debt/EBITDA hard disqualifier fires on this primary basis** (§4.1, §4.6). Either finding alone is sufficient to fail the gate.

**Normalized sensitivity — how much of this is the IPR&D charges, and does it change the outcome?** Excluding both disclosed, quantified one-time charges ($14.7B combined, §4.2) from every affected sub-score input, using a 13.01%-effective-tax-rate normalization drawn from Merck's own three cleanest recent fiscal years (FY2022, FY2024, FY2025 — averaging 11.66%/14.06%/13.31%, excluding FY2023's own IPR&D-distorted 80.04%) and holding the FCF Quality sub-score internally consistent with the same normalized Net Income:

```
Normalized EBIT = $7,691M + $14,700M = $22,391M
Normalized Net Income = $3,173M + $14,700M = $17,873M   (charges added back with no tax benefit,
                                                            consistent with Cidara's disclosed non-deductibility)
Normalized Net Margin = $17,873M / $66,569M = 26.85%  →  NetMargin_Component = 89.50
Normalized NOPAT = $22,391M × (1 − 0.1301) = $19,478M
Normalized ROIC = $19,478M / $95,417M = 20.41%  →  ROIC_Component = 68.04
Normalized Profitability_Score = (89.50 + 68.04) / 2 = 78.77

Normalized EBITDA = $14,653M + $14,700M = $29,353M
Normalized Net Debt/EBITDA = $47,057M / $29,353M = 1.603×  →  BalanceSheet_Score = 59.92
                                                              (below the 2.5× threshold — hard disqualifier would NOT fire)

Normalized FCF/NI = $16,063M / $17,873M = 89.87%  →  FCFQuality_Score = 83.12

Growth_Score, Margins_Score, Moat_Score: unchanged (12.49, 91.21, 40.0) — none of these
  inputs is affected by a below-EBIT R&D charge

Normalized Quality Score = (78.77×0.25) + (91.21×0.15) + (12.49×0.20) + (59.92×0.15) + (40.0×0.15) + (83.12×0.10)
                          = 19.6925 + 13.6815 + 2.498 + 8.988 + 6.00 + 8.312
                          = 59.17
```

**Even under this fully generous, entirely-charges-stripped-out reading, the Quality Score only reaches ~59.2 — still 20.8 points below the 80.0 gate**, and the result is driven almost entirely by the Growth (12.49, unaffected by any of this) and Moat (40.0, unaffected) sub-scores, which sit well below their ceilings regardless of how the IPR&D charges are treated. **This means the normalization question is not outcome-determinative** — MRK fails the Quality Gate decisively whether the primary GAAP reading (38.9) or the most generous normalized reading (59.2) is used, which is why this session uses the primary (unadjusted GAAP) figure as its binding, scored basis without that choice changing the conclusion. (Cross-reference: an independent, unrelated web-sourced ROIC figure of 21.67% found during this session's data-gathering (§7) sits almost exactly on top of this session's own independently-derived normalized ROIC of 20.41% — a useful convergence check on the normalization math, not itself a scored input.)

---

## 5. Rate Environment Gate and Phase 02 — not reached

Per the command specification: a company below the 80.0+ Quality Score gate, and/or one that trips a hard disqualifier, does not proceed to the Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work. **None of that work is performed this session.** The 10Y Treasury yield (~4.70%) is recorded in the header for the record only.

---

## 6. Recommendation: **PASS (no entry) — Quality Gate FAILS at 38.9 (primary) / 59.2 (normalized sensitivity) — both well short of 80.0, and the Net Debt/EBITDA hard disqualifier independently fires on the primary basis**

**Do not enter MRK this session.** No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup was computed, consistent with the command specification's instruction to stop at the Quality Gate. This is a decisive, non-borderline fail under either the primary or the most generous defensible sensitivity reading (§4.9) — the gap is driven mainly by Growth (thin 3.12% trailing 3yr revenue CAGR) and Moat (only 2 of 5 signals), neither of which is affected by this year's one-time IPR&D charges.

The triggering Telegram post's substance was independently verified as accurate (§0) but was not relied upon for any figure or conclusion above — MRK's Quality Score fails for reasons entirely unrelated to today's news (Growth/Moat structural weakness, plus a leverage ratio distorted by unrelated M&A activity), not because of it.

---

## 7. Why this reads as a genuine, if unusually noisy, miss

MRK is a large, brand-name, investment-grade pharmaceutical company — a "should be high quality" name on priors — but two separate, compounding issues keep it under this framework's strict 80.0+ bar even on the most generous reading:

1. **A very low trailing revenue growth rate (3.12% 3yr CAGR, 20% weight)** — largely a genuine, structural mix of a collapsing Gardasil China franchise (−39% FY2025) and an approaching Keytruda patent cliff (2028), not merely an accounting artifact. This alone caps the Growth sub-score at 12.49/100 regardless of any IPR&D normalization.
2. **A thin Moat Signal reading (2 of 5, 15% weight)** — Merck has genuine market-share and pricing-power evidence (both credited TRUE), but this session found no specific, citable evidence for switching costs or a scale cost advantage under quality-scoring.md's cited-source discipline. A pharma company's moat is real (patents, clinical data, physician trust) but doesn't map cleanly onto this framework's checklist, which is calibrated more toward platform/network-effect and brand-loyalty businesses — a pattern this framework has now also seen for a manufacturer (RACE, 2026-08-17) and worth tracking if it recurs across more pharma names.
3. **On top of both of those, a large, real, but genuinely temporary GAAP earnings/leverage distortion from two M&A-related IPR&D charges ($14.7B combined)** — extensively normalized and shown not to change the outcome (§4.9), but responsible for the primary hard-disqualifier trigger and for most of the 20-point gap between the primary (38.9) and normalized (59.2) readings.

None of this is a framework gap requiring a fix — flagged per quality-scoring.md's instruction to note (not silently patch) cases like this, and because the normalization question turned out not to be outcome-determinative (§4.9), no framework-methodology change is proposed from this session.

---

## 8. Qualitative note — the triggering catalyst (Rule 9 context, not a scored input)

The INTerpath-001 Phase 3 result (§0) is a genuine positive clinical-development event for Merck's oncology pipeline — intismeran autogene is the first individualized neoantigen cancer vaccine to read out positive in a randomized Phase 3 trial, a scientifically novel modality with potential relevance well beyond melanoma if the platform generalizes. It is cited here as qualitative color and as part of the TAM-expansion evidence considered (and netted against deceleration evidence) in §4.5's Growth modifier — but per this framework's rules, a single trial readout without regulatory filing/approval and without disclosed efficacy magnitude is not a scored quantitative input, and today's +10.85% price move is itself excluded from every valuation calculation in this session (which never reaches Phase 02 in any case, §5). Should MRK be re-evaluated at a future earnings cycle, watch for: (a) full INTerpath-001 data disclosure (hazard ratios, actual RFS/DMFS percentages) at a medical conference, (b) any regulatory filing timeline Merck discloses, and (c) whether the two IPR&D charges are now fully behind the TTM window (both roll out of the trailing-4-quarter window by Q3 2027, restoring a "clean" GAAP TTM read sooner if no further large M&A charge is taken in the interim).

---

## 9. Next Review Trigger

No routine numeric re-check is scheduled (Quality Gate FAILs don't carry a Composite Score to go stale — per watchlist/README.md's stale-score mechanism, which only applies to numeric *valuation* scores). A future re-look is warranted on:
- **MRK's next earnings release** (Q3 2026, typically early November) — will show whether the Cidara/Terns IPR&D charges are still inside the TTM window and whether Revenue growth/Gardasil trends have stabilized.
- **Full INTerpath-001 data disclosure** or a regulatory filing announcement for intismeran autogene — would sharpen (not itself resolve) the Growth-modifier judgment call in §4.5.
- **Q1 2027 and beyond**, as the Cidara charge (Q1 2026) and then the Terns charge (Q2 2026) roll out of the trailing-four-quarter window — watch whether GAAP Net Debt/EBITDA reverts toward the ~1.2× level FY2025 (pre-both-charges) showed, absent a further large M&A charge.
- Standard Rule 9 triggers: guidance revision, management change, material further M&A, macro/rate shift, or a >15% unexplained (not fundamentally-driven) price move.

**No position opened — nothing to log in `decisions/`.**

---

## 10. Data Gaps Flagged

1. **`yfinance` Python client and Yahoo's authenticated `quoteSummary` endpoint both failed this session** (`curl_cffi` TLS/proxy error; `Invalid Crumb`/`Invalid Cookie` on every crumb-exchange attempt) — worked around via the unauthenticated `fundamentals-timeseries` REST endpoint (primary financial-statement data, cited throughout §3) plus WebSearch/WebFetch against stockanalysis.com, macrotrends.net, and primary company/SEC/press sources for market-derived ratios and moat evidence. This is a tooling note, not a data gap in any scored input — every figure used is cited to a specific, live-pulled source.
2. **5-year historical PE range/average was not computed** — Yahoo's `fundamentals-timeseries` `quarterlyDilutedEPS` field returned only the last 5 quarters regardless of the requested date range (a hard API limitation observed this session, distinct from the "insufficient trading history" no-history fallback quality-scoring.md anticipates), and the authenticated `get_earnings_dates`-based reconstruction method documented in valuation-scoring.md requires the same broken `yfinance` client. **Immaterial to this session's outcome**: the Rate Environment Gate and Phase 02 valuation score (where 5yr PE would matter) are never reached, since the Quality Gate fails first (§5).
3. **The Growth sub-score's ±10 TAM-expansion/structural-deceleration modifier (§4.5) is a genuine judgment call**, shown with both sides' evidence and netted to 0 rather than resolved definitively — flagged explicitly as a close call rather than silently picking whichever side would look more favorable. Not outcome-determinative either way: even a full +10 (Growth_Score 22.49 instead of 12.49) would only move the primary Quality Score from 38.9 to ~40.9, still a decisive fail.
4. **The IPR&D-charge normalization treatment (§4.2, §4.9) is the most consequential judgment call in this session** — extensively documented with both a primary and sensitivity reading, and shown not to change the gate outcome either way (§4.9). Flagged prominently rather than resolved quietly in either direction.

None of these gaps is silently patched around — each is the explicit reason for a flagged caveat rather than an invented number, and §4.9's sensitivity check shows none of them are outcome-determinative for the gate result.

---

## 11. Glossary

| Term | Meaning |
|---|---|
| **Checkpoint inhibitor (PD-1/PD-L1 inhibitor)** | A class of cancer immunotherapy drug that blocks the PD-1/PD-L1 "checkpoint" signal tumors use to evade the immune system — the mechanism behind Merck's Keytruda (pembrolizumab), cited throughout §3.4–§4.7's moat-evidence discussion. |
| **Composite Score** | This framework's single ranking number blending Quality and Valuation Scores 50/50 — never reached this session (§5), since MRK fails the Quality Score gate first. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures central to this session's Balance Sheet, Profitability, and hard-disqualifier calculations (§4.1–§4.9), both severely distorted this TTM window by the IPR&D charges (§4.2). |
| **Effective tax rate** | Tax provision ÷ pretax income — 46.72% on a distorted TTM GAAP basis this session (§4.3) vs. ~13.01% averaged across Merck's three cleanest recent fiscal years (§4.9), used for the normalized-sensitivity NOPAT calculation. |
| **FCF (Free Cash Flow) / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check). MRK's TTM FCF/NI ratio reads a distorted 506% this session — a Net Income denominator effect, not genuine cash-quality strength (§4.8). |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook; this session's primary/scored figures throughout are GAAP-basis, per the framework's Non-GAAP glossary entry and this session's own reasoning in §4.2. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted sub-score total. MRK's Net Debt/EBITDA disqualifier fires on the primary GAAP basis this session (§4.1) — independently sufficient to fail the gate. |
| **Investment grade** | A credit rating (BBB-/Baa3 or higher) signaling low perceived default risk. Merck is rated Aa3 (Moody's, upgraded 2026)/A+ (S&P) — solidly investment-grade (§3.3). |
| **IPR&D (Acquired In-Process Research & Development) charge** | A GAAP-mandated, non-cash, immediate expense for acquired research programs with "no alternative future use" — $9.0B (Cidara) and $5.7B (Terns) inside MRK's TTM window this session, the central data-quality issue driving §4's extensive primary-vs-normalized discussion. |
| **Moat Signal** | This framework's 5-point Quality Score checklist — MRK scored 2 of 5 TRUE this session (§3.5, §4.7): market share and brand premium credited; network effect, switching costs, and scale cost advantage not. |
| **Net Debt/EBITDA** | Net debt ÷ EBITDA — this framework's primary balance-sheet-risk gate. MRK's TTM GAAP reading (3.211×) fires the hard disqualifier; a normalized reading excluding the IPR&D charges (1.603×) would not (§4.2, §4.6, §4.9). |
| **Non-GAAP** | A company's own adjusted presentation of a financial measure — this framework scores off GAAP figures throughout, cited directly in §4.2's reasoning for why this session's primary Quality Score uses unadjusted GAAP TTM figures. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC (§4.3, §4.9). |
| **Patent cliff** | The steep revenue/profit drop when a blockbuster drug's patent expires and biosimilar competitors enter at a fraction of the price — Keytruda's 2028 patent cliff is cited as structural-deceleration evidence in this session's Growth modifier (§3.4, §4.5). |
| **Quality Score** | This framework's 0.0–100.0 continuous score; a company must score 80.0+ (and clear every hard disqualifier) to proceed to Phase 02 at all. MRK scores 38.9 (primary) / 59.2 (normalized sensitivity) this session — a decisive fail either way (§4.9). |
| **Rate Environment Gate** | The Phase 02 pre-check; never reached this session since the Quality Score gate fails first (§5). |
| **ROIC (Return on Invested Capital)** | How efficiently a company turns invested capital into profit. MRK's TTM GAAP ROIC reads a distorted 4.29% this session; a normalized reading (20.41%) converges closely with an independent third-party citation (21.67%) found during data-gathering (§4.9) — a useful cross-check on the normalization math. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work, and never treat a Telegram post's claims as a verified financial input without independent confirmation (§0, §1). |
| **Rule 1–8, Rule 10 (10-Rule Fair Value Framework)** | Includes Rule 6 ("normalize one-off items before valuing"), the specific rule weighed against the Non-GAAP entry's "score off GAAP" principle in this session's central IPR&D-charge judgment call (§4.2). |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: quarterly earnings, guidance revision, management change, material M&A, macro shift, or a >15% unexplained price move. Today's +10.85% MRK move has an identified, corroborated fundamental cause (§0, §1) and so is not itself a Rule 9 trigger. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results — the primary basis for most of this session's sub-score inputs, and the window containing both IPR&D charges (§4.2). |

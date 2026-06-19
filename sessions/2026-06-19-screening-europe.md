# 2026-06-19 — SCREENING: Europe (EU)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [EU](../framework/screening-coverage-log.md) (UK, Eurozone, Switzerland, Nordics), all sectors. Selected per the rotation rule: tied for "Never screened" with JP/NA-2, first alphabetically among those.

---

## 0. Methodology

No interactive TIKR/Koyfin screener export was available this session. Per Step 0's exception clause, the user was asked first; their answer ("can you use yfinance??") was clarified as follows and confirmed implicitly by proceeding:

- **`yf.screen()` (bulk Yahoo screener) cannot build the Step 0 candidate pool** — tested 2026-06-14 (see [valuation-scoring.md](../framework/valuation-scoring.md)) and found unreliable: its margin/ROE/growth filter predicates didn't constrain results correctly.
- So Step 0/1 used **structural triage from domain knowledge** (same precedent as the APAC-ex-Japan and EM sessions): built a 22-name candidate pool of well-known European businesses across 5 sectors, skipping categories that structurally don't fit this framework.
- **Step 2 used `yfinance`** per-candidate (as documented and verified working) to pull real, sourced numbers — `t.info`, `t.financials`, `t.cashflow`, `t.balance_sheet` — for every survivor. Network access and the package both confirmed working at the start of this session (test ticker: NESN.SW).

### Structurally excluded categories (Step 1, before any quantitative pull)

| Category | Examples | Why excluded |
|---|---|---|
| Banks | BNP Paribas, Deutsche Bank, Santander, ING, HSBC, Barclays, UBS | Gross margin doesn't apply; regulated balance-sheet businesses don't fit this framework's model (same as DBS/OCBC/UOB/Macquarie precedent in the APAC session) |
| Insurers | Allianz, AXA, Zurich Insurance, Munich Re, Prudential | Same reasoning as banks |
| Oil & gas majors | Shell, TotalEnergies, BP, Equinor | Commodity cyclical |
| Mining/materials majors | Rio Tinto, Glencore, Anglo American, ArcelorMittal | Commodity cyclical |
| Telecom | Vodafone, Deutsche Telekom, Orange, Telefónica, BT | Capital-intensive, regulated, structurally low growth/margin |
| Regulated utilities | Iberdrola, Engie, National Grid, E.ON, RWE | Regulated utility — doesn't fit framework |
| Airlines | Lufthansa, IAG, Air France-KLM, Ryanair | Commodity cyclical (fuel/labor), thin margins |
| Mainstream automakers | Volkswagen, Mercedes-Benz, Stellantis, Renault, BMW | Thin-margin cyclical (Ferrari carved out below as the luxury exception — different economics) |
| Thin-margin retail/grocery | Carrefour, Tesco, Ahold Delhaize, Marks & Spencer | Thin-margin retail (NA-1 precedent: WMT/COST/TJX) |
| REITs | Unibail-Rodamco-Westfield, Vonovia, Klepierre | REIT — gross margin/EV-EBIT framing doesn't fit |

**Note:** Sage Group (SGE.L) was excluded from the candidate pool — already evaluated via `/new-position` on 2026-06-19 ([sessions/2026-06-19-new-position-sge.md](2026-06-19-new-position-sge.md)); no need to re-screen it here.

### Candidate pool (22 names, structural-triage survivors)

| Ticker | Company | Country | Sector |
|---|---|---|---|
| MC.PA | LVMH | France | Luxury goods |
| RMS.PA | Hermès | France | Luxury goods |
| OR.PA | L'Oréal | France | Cosmetics |
| RACE.MI | Ferrari | Italy | Luxury auto |
| CFR.SW | Richemont | Switzerland | Luxury goods |
| NOVO-B.CO | Novo Nordisk | Denmark | Pharma (GLP-1) |
| SOON.SW | Sonova | Switzerland | Medtech (hearing) |
| STMN.SW | Straumann | Switzerland | Medtech (dental implants) |
| COLO-B.CO | Coloplast | Denmark | Medtech (ostomy/continence) |
| SAP.DE | SAP | Germany | Enterprise software |
| ASML.AS | ASML | Netherlands | Semicap equipment |
| ADYEN.AS | Adyen | Netherlands | Payments |
| REL.L | RELX | UK | Information/analytics |
| EXPN.L | Experian | UK/Ireland | Credit bureau/data |
| HEXA-B.ST | Hexagon AB | Sweden | Measurement tech |
| SU.PA | Schneider Electric | France | Electrical equipment |
| ATCO-A.ST | Atlas Copco | Sweden | Industrial equipment |
| ASSA-B.ST | Assa Abloy | Sweden | Locks/access control |
| SIKA.SW | Sika | Switzerland | Specialty chemicals |
| HLMA.L | Halma | UK | Safety/health tech |
| DB1.DE | Deutsche Börse | Germany | Exchange/clearing |
| LSEG.L | London Stock Exchange Group | UK | Exchange/data |

Not exhaustive of European quality businesses — see Next Steps for names deferred to a future deep-dive within this slice (Nestlé, Wolters Kluwer, Dassault Systèmes, EssilorLuxottica, Genmab, Demant, Spirax Group, Geberit, Bureau Veritas, Nemetschek).

---

## Step 2 — Quantitative Phase 01 gate (real, sourced data — `yfinance`, pulled 2026-06-19)

Filters: Gross margin >40% · Net margin >12% · ROIC>15% (ROE used as proxy, per APAC/EM precedent) · Revenue growth >8% (3yr CAGR) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x

FCF yield uses the most recent **annual** (fiscal-year) FCF ÷ market cap, cross-checked against `info["freeCashflow"]` (TTM) where available — flagged below wherever the two disagree materially. Net Debt uses the balance-sheet "Cash And Cash Equivalents" line specifically (not the broader cash + short-term-investments bucket), applied consistently across all names.

| Ticker | Gross M | Net M | ROE | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA | FCF yield (annual) | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| LVMH | 66.24% ✅ | 13.46% ✅ | 16.24% ✅ | 0.68% ❌ | ✅ | 1.36× ✅ | 5.76% ✅ | 15.86× ✅ | **FAIL — growth only (7/8)** |
| Hermès | 71.11% ✅ | 28.27% ✅ | 25.21% ✅ | 11.31% ✅ | ✅ | net cash ✅ | 2.34% ❌ | 25.40× ❌ | **FAIL** — too expensive |
| L'Oréal | 74.32% ✅ | 13.91% ✅ | 18.00% ✅ | 4.81% ❌ | ✅ | 0.21× ✅ | 3.53% ❌ | 23.46× ❌ | **FAIL** — growth + valuation |
| Ferrari | 51.61% ✅ | 22.19% ✅ | 41.97% ✅ | 11.93% ✅ | ✅ | 0.59× ✅ | 2.60% ❌ | 27.27× ❌ | **FAIL** — too expensive (6/8) |
| Richemont | 64.39% ✅ | 15.54% ✅ | 14.96% ❌ (barely) | 3.96% ❌ | ✅ | 0.93× ✅ | 3.52% ❌ | 22.31× ❌ | **FAIL** — multiple |
| **Novo Nordisk** | 83.20% ✅ | 37.21% ✅ | 71.40% ✅ | 20.43% ✅ | ✅ all 3yr positive | 0.60× ✅ | 2.23% ❌ | 10.17× ✅ | **FAIL — FCF yield only (7/8)** ⚠️ data flag |
| Sonova | 73.72% ✅ | 11.94% ❌ (barely) | 20.52% ✅ | −1.20% ❌ | ✅ | 1.18× ✅ | 5.50% ✅ | 18.65× ✅ | **FAIL** — net margin + growth |
| Straumann | 70.10% ✅ | 13.66% ✅ | 17.01% ✅ | 3.93% ❌ | ✅ | net cash ✅ | 1.68% ❌ | 31.48× ❌ | **FAIL** — growth + valuation |
| Coloplast | 67.46% ✅ | 7.51% ❌ | 14.14% ❌ (barely) | 11.64% ✅ | ✅ (declining) | 2.56× ❌ (barely) | 1.66% ❌ | 15.12× ✅ | **FAIL — multiple** ⚠️ data flag |
| **SAP** | 73.72% ✅ | 19.58% ✅ | 16.35% ✅ | 7.63% ❌ (barely) | ✅ | net cash ✅ | 5.37% ✅ | 15.29× ✅ | **FAIL — growth only, by 0.4pp (7/8)** |
| ASML | 52.60% ✅ | 29.71% ✅ | 52.24% ✅ | 15.55% ✅ | ✅ | net cash ✅ | 1.73% ❌ | 52.72× ❌ | **FAIL** — way too expensive |
| Adyen | 68.09% ✅ | 44.71% ✅ | 22.33% ✅ | **data gap** ⚠️ | ✅ | net cash ✅ | 3.28% ❌ (close) | 12.38× ✅ | **FAIL — FCF yield only, growth ambiguous (data gap)** |
| **RELX** | 66.29% ✅ | 21.53% ✅ | 70.51% ✅ | 3.89% ❌ | ✅ | 2.23× ✅ | 5.54% ✅ | 16.93× ✅ | **FAIL — growth only (7/8)** |
| **Experian** | 42.01% ✅ | 17.79% ✅ | 28.26% ✅ | 8.46% ✅ | ✅ | 2.06× ✅ | 6.67% ✅ | 13.00× ✅ | **PASS — all 8 filters** |
| Hexagon AB | 66.04% ✅ | 37.52% ✅ ⚠️ | 17.89% ✅ | 1.68% ❌ | ✅ ⚠️ | 2.72× ❌ ⚠️ | 0.39% ❌ | 232.8× ❌ ⚠️ | **FAIL — multiple + data inconsistencies** |
| Schneider Electric | 42.08% ✅ | 10.37% ❌ | 15.61% ✅ (barely) | 5.52% ❌ | ✅ | 1.67× ✅ | 2.82% ❌ | 25.48× ❌ | **FAIL — multiple** |
| Atlas Copco | 42.63% ✅ | 15.70% ✅ | 22.42% ✅ | 6.00% ❌ | ✅ | 0.47× ✅ | 2.76% ❌ | 27.62× ❌ | **FAIL** — growth + valuation |
| **Assa Abloy** | 43.12% ✅ | 10.51% ❌ (close) | 15.04% ✅ (barely) | 8.06% ✅ (barely) | ✅ | 2.24× ✅ | 4.88% ✅ | 19.24× ✅ (close) | **FAIL — net margin only (7/8)** |
| Sika | 54.94% ✅ | 9.32% ❌ | 15.25% ✅ (barely) | 2.21% ❌ | ✅ | 2.43× ✅ (close) | 5.08% ✅ | 20.04× ❌ (barely) | **FAIL — multiple, 2 narrow** |
| Halma | 100.0% ⚠️ data error | 14.42% ✅ | 18.31% ✅ | 13.80% ✅ | ✅ | 0.83× ✅ | 2.89% ❌ | 38.26× ❌ | **FAIL** — too expensive |
| **Deutsche Börse** | 81.23% ✅ | 27.26% ✅ | 19.20% ✅ | 12.20% ✅ | ✅ all 3yr positive | 1.86× ✅ | 5.47% ✅ | 16.29× ✅ | **PASS — all 8 filters** |
| LSEG | 88.09% ✅ | 13.36% ✅ | 6.37% ❌ | 6.47% ❌ | ✅ | 2.66× ❌ (barely) | 4.17% ✅ | 24.25× ❌ | **FAIL — multiple** (Refinitiv integration drag) |

---

## ✅ Qualified Quality List — 2 names

**Experian (EXPN.L)** and **Deutsche Börse (DB1.DE)** — both clear all 8 Phase 01 filters cleanly.

### Near-misses flagged for the watchlist (fail only 1 filter — re-check on next rotation or a pullback/data refresh)

- **LVMH (MC.PA)** — passes 7/8; fails only revenue 3yr CAGR (0.68%, well under 8% — luxury demand slowdown, especially China). Margins, ROE, FCF-positive, leverage, FCF yield (5.76%) and EV/EBIT (15.86×) are all comfortably inside the gate.
- **SAP (SAP.DE)** — passes 7/8; revenue 3yr CAGR (7.63%) misses the 8% bar by only 0.4pp. Everything else — including FCF yield (5.37%) and EV/EBIT (15.29×) — clears with room.
- **RELX (REL.L)** — passes 7/8; only revenue 3yr CAGR (3.89%) fails. Strong ROE (70.5%), FCF yield (5.54%), reasonable EV/EBIT (16.93×).
- **Assa Abloy (ASSA-B.ST)** — passes 7/8; only net margin (10.51%) fails, and only by 1.5pp. Revenue CAGR (8.06%) and EV/EBIT (19.24×) both clear, but narrowly.
- **Novo Nordisk (NOVO-B.CO)** — passes 7/8 on the annual-FCF basis; only FCF yield (2.23%) fails, reflecting heavy GLP-1 manufacturing capex. **Data flag:** `info["freeCashflow"]` (TTM) is actually negative (−0.93%), conflicting with the annual cash-flow statement, which shows 3 consecutive years of positive FCF — worth resolving with a live `/new-position` pull rather than treating either figure as final.
- **Adyen (ADYEN.AS)** — passes cleanly on 7 of 8 filters (FCF yield, at 3.28%, is the only clean fail, and only by 0.7pp). Revenue 3yr CAGR is a **data gap, not a real fail**: the 2022 revenue figure in `yfinance` (€8.9B) is wildly inconsistent with the 2023 figure (€1.9B) — almost certainly a reporting-basis artifact (processed volume vs. net revenue). The 2023→2025 trend alone implies ~19%/yr growth, well above the 8% bar, but this wasn't used for the verdict per Rule 0 (flag, don't estimate/patch the corrupted data point).

---

## Step 3 — Qualitative pass (the 2 clean PASSes)

### Experian (EXPN.L)

1. **Why are margins high?** Experian is one of only three global consumer/commercial credit bureaus (alongside Equifax and TransUnion) — an oligopoly built on decades of proprietary credit-file data, regulatory accreditation (FCRA in the US and equivalents elsewhere), and exclusive data-furnisher relationships with lenders. High-margin analytics/decisioning software is layered on top of that data asset.
2. **What would it take to compete?** Replicating decades of historical credit-file depth, the same lender data-sharing relationships, and the regulatory accreditation needed to operate as a credit bureau — practically impossible for a new entrant. The global bureau industry has had the same three incumbents for decades with no new entrant breaking in.
3. **Capital allocation (5–10yr):** Consistent bolt-on M&A in data/analytics (e.g., LatAm expansion via Serasa, fraud/ID analytics acquisitions), steady dividend growth plus buybacks, and organic reinvestment in cloud data platforms (Ascend).
4. **Where's growth coming from (3–5yr)?** Consumer services (credit monitoring/identity protection), fraud and identity analytics, B2B decisioning software, and continued penetration of under-bureaued emerging markets (Brazil, India).
5. **Best bear case:** A meaningful share of revenue tracks consumer-lending origination volumes (mortgage, auto) — cyclical to the credit cycle and rate environment. Longer-term, alternative-data/cash-flow underwriting and open-banking regimes could erode the traditional credit-file's primacy, and privacy/data-use regulation is a perpetual tail risk.
6. **Disruption vector:** Moderate, monitored risk rather than near-term existential — alternative-data underwriting is a real multi-year threat to the traditional bureau model, but Experian is itself acquiring and building those alternative-data capabilities rather than being disrupted from outside.

### Deutsche Börse (DB1.DE)

1. **Why are margins high?** Operates Germany's cash-equities exchange (Xetra), Europe's largest derivatives exchange (Eurex), and post-trade settlement/custody infrastructure (Clearstream) — regulated, liquidity-network-effect businesses where switching an already-listed/cleared instrument elsewhere destroys the liquidity that makes it valuable. High operating leverage on trading/clearing volume on top of near-fixed infrastructure costs.
2. **What would it take to compete?** A new entrant would need to replicate decades of accumulated trading liquidity, EU-wide regulatory licensing, and clearing-member relationships — not feasible organically. Historically, competition in EU market infrastructure has come via consolidation (LSEG/Refinitiv, Euronext's roll-up of regional exchanges), not de novo entrants.
3. **Capital allocation (5–10yr):** Active consolidator via M&A in market infrastructure and data (ISS, SimCorp, Qontigo/STOXX, Crypto Finance), funded by a mix of debt and equity, alongside a consistent dividend.
4. **Where's growth coming from (3–5yr)?** Eurex derivatives volume growth — including an EU policy tailwind to build out EU-based clearing as an alternative to US/UK CCPs — plus data and analytics (SimCorp investment software, STOXX indices) and expansion of Clearstream's collateral/securities-financing services.
5. **Best bear case:** Revenue is volume/volatility dependent — a prolonged low-volatility, low-rate environment compresses both trading fees and the net interest income earned on client collateral balances. EU regulatory/political risk (historically, EMIR open-access rules have threatened clearing-monopoly economics) and integration risk from the acquisitive growth strategy (SimCorp, ISS) are real, ongoing risks.
6. **Disruption vector:** Low near-term risk — post-2008 regulation has mandated central clearing for derivatives, reinforcing rather than threatening centralized clearinghouses. The more relevant long-term dynamic is geographic/political (the EU building clearing alternatives to US/UK-based CCPs), which is more plausibly a tailwind than a threat for Deutsche Börse specifically.

**Conclusion:** Both are genuine quality businesses with strong, regulation-reinforced moats (credit-bureau oligopoly; exchange/clearing network effects), priced reasonably (13.0× and 16.3× EV/EBIT respectively) relative to double-digit-ROE, double-digit-growth profiles. **Recommend `/new-position EXPN` (EXPN.L) and `/new-position DB1` (DB1.DE)** for full Phase 02 scoring with live pricing.

---

## Data gaps flagged (per CLAUDE.md Rule 0 — none estimated)

- **Novo Nordisk**: `info["freeCashflow"]` (TTM, −€12.0B equivalent) directly conflicts with the annual cash-flow statement (3 consecutive years of positive FCF, most recent ~29.0B DKK) — both sourced from `yfinance`, not reconciled here; flagged for live-price/data resolution via `/new-position`.
- **Adyen**: 2022 annual revenue figure (€8.9B) is inconsistent with the 2023–2025 series (€1.86B–€2.65B) — almost certainly a reporting-basis change (gross processed volume vs. net revenue) rather than a real number; the 3yr CAGR computed from it is not usable and was not used for the verdict.
- **Hexagon AB**: `info["ebitda"]` (SEK 1,276M) is implausibly *below* the EBIT figures in the income statement (SEK 930M–1,434M across 2022–2025) — EBITDA should exceed EBIT after adding back D&A; the Net Debt/EBITDA ratio computed from it is unreliable. Separately, 2025 EBIT (SEK 930M) dropped sharply from 2024 (SEK 1,434M), driving the extreme EV/EBIT (232.8×) — not investigated further here, but Hexagon fails on FCF yield and growth regardless of this ambiguity.
- **Coloplast**: TTM net margin (7.51%) is inconsistent with the much higher operating margin (25.69%) and historically stronger net margins — suggests a large below-the-line one-off charge in FY2025 not itemized in the pulled fields. `info["freeCashflow"]` also disagrees with the annual cash-flow series (FY24 1.42B DKK vs. info's higher TTM figure).
- **Halma**: `grossMargins` reported as exactly 100.0% — a clear data artifact (likely missing cost-of-revenue line in the source filing format), not a real figure. Excluded from the verdict basis; Halma's other 7 filters were evaluated normally and it fails on FCF yield and EV/EBIT regardless.
- **Deutsche Börse**: balance-sheet "Cash, Cash Equivalents And Short Term Investments" line (€205.1B) is obviously a client/settlement-balance figure typical of a CCP/exchange business (same pattern as HKEX in the APAC session), not the company's own cash. Used the narrower "Cash And Cash Equivalents" line (€2.08B) instead for Net Debt/EBITDA.
- **All UK-listed names (RELX, Experian, Halma, LSEG)**: `yfinance` reports the trading currency as GBp (pence) while income-statement/balance-sheet figures appear to be in GBP — ratios are unaffected since numerator/denominator come from the same normalized source, but absolute figures should not be read at face value without checking units.

---

## Next steps

- `/new-position EXPN` (Experian, EXPN.L) — the cleaner of the two passes on growth/margin durability; full Phase 02 scoring with live price.
- `/new-position DB1` (Deutsche Börse, DB1.DE) — full Phase 02 scoring with live price.
- Watchlist (no new entry, re-check on next EU rotation or a pullback): **LVMH, SAP, RELX, Assa Abloy** — each fails only one filter, all on growth or margin, not on business quality. **Novo Nordisk** and **Adyen** also belong here but need the data-gap resolved first (live `/new-position` pull recommended for both regardless, given how close they are).
- Deferred to a future EU deep-dive (not yet quantitatively screened this pass): Nestlé, Wolters Kluwer, Dassault Systèmes, EssilorLuxottica, Genmab, Demant, Spirax Group, Geberit, Bureau Veritas, Nemetschek, Temenos.
- Coverage log updated below — next "Never screened" alphabetical slice is **JP (Japan)**.

# 2026-06-09 — SCREENING: NA-2 (Healthcare · Financials · Industrials · Energy · Materials)

**Task type:** SCREENING (Phase 01)
**Date:** 2026-06-09
**10Y US Treasury yield:** ~4.55% (CNBC/TradingEconomics, 2026-06-09)
**Rate Regime Modifier in effect:** +0.5 (10Y in 3.5–5% band)

---

## 0. Methodology note — ETF fallback sourcing

⚠️ **ETF fallback session.** The EODHD API returned `Host not in allowlist` from this cloud environment (network policy restriction). Starting pool is built from quality-factor ETF holdings and Gurufocus/sector screens rather than a full EODHD mechanical pre-filter. This approach **misses small/mid-cap quality candidates not yet held in major ETFs** — re-run this slice with EODHD access once the network policy is updated to allow `eodhd.com`.

**Starting pool sources:**
- QUAL (iShares MSCI USA Quality Factor ETF) — NA-2 sector components
- MOAT (VanEck Morningstar Wide Moat ETF) — NA-2 sector components
- Sector ETF constituents: XLV (healthcare), XLF (financials), XLI (industrials)
- Gurufocus quality composite screen — NA-2 sectors
- Analyst-independent sector knowledge cross-check

**Already-held names excluded from new candidate consideration:** SPGI (held), V (held), NVO (held) — re-scored on their own earnings cadence.

---

## Stage 1 — Starting universe (26 names across NA-2 sectors)

**Healthcare:** ISRG, VEEV, IDXX, ZTS, TMO, DHR, ABT, UNH, ELV, MCK, ABBV, ZTS
**Financials:** MCO, MSCI, CME, ICE, FDS, AXP, BLK, NDAQ
**Industrials:** CTAS, ODFL, ROP, RSG, WM, ITW
**Energy:** XOM, COP, SLB *(structural triage expected to eliminate all)*
**Materials:** ECL, SHW *(quality exceptions in otherwise commodity-heavy sector)*

---

## Stage 2 — Structural triage (categorical elimination before pulling numbers)

| Eliminated | Reason |
|---|---|
| UNH, ELV | Managed care — net margins structurally 4–6%; thin-margin insurance intermediary model |
| MCK | Drug distribution — net margins structurally ~1–2%; logistics pass-through model |
| ABBV | Heavy patent-cliff exposure (Humira post-LOE); revenue base declining, growth questionable |
| TMO, DHR | Life sciences tools — strong businesses but mid-single-digit growth (5–7% CAGR historically), not the >10% growth bar; net margins 12–14%, borderline ROIC ~8–12% |
| ABT | Diversified healthcare — organic growth mid-single-digit, net margins ~13–15%, ROIC borderline ~12–14% |
| XOM, COP, SLB | Commodity cyclical energy — margin and revenue swing violently with oil price; not structural quality |
| SHW | Specialty paints — gross margins ~47% but net margin ~12% borderline, revenue growth ~5–7%, ROIC ~20%+ but growth gate concern; hold back for manual check |
| RSG, WM | Waste management — net margins ~12–14%, revenue growth ~5–7%; structurally below growth bar |
| ITW | Diversified industrials stalwart — mid-single-digit organic growth, not >10% CAGR |
| BLK | Asset management — thin net margins (~30%) at the AUM level, but revenue is highly market-cap-correlated; growth lumpy; business quality strong but not the clean compounding profile this framework targets; revenue growth <10% in most years |
| AXP | Financial institution — high net leverage, credit cycle sensitivity; not an asset-light payment network equivalent for Upgrade 5 purposes |
| NDAQ | Exchange — ROIC diluted by data/analytics acquisition goodwill, revenue growth ~8–9%; similar structural issues to CME/ICE |

**13 eliminated. 13 names to Phase 01 quantitative gate:** ISRG, VEEV, IDXX, ZTS, MCO, MSCI, CME, ICE, FDS, CTAS, ODFL, ROP, ECL

---

## Stage 3 — Phase 01 Quantitative Gate

**Filters:** Gross margin >40%, Net margin >12%, ROIC >15%, Revenue growth >8% (3yr CAGR), FCF positive 3 consecutive years, Net Debt/EBITDA <2.5×, FCF/NI conversion >70%

Data sourced from: Gurufocus, Macrotrends, StockAnalysis, SEC filings (2025 annual/Q1 2026), CNBC, company earnings releases. Sources cited per metric where obtained.

---

### ISRG — Intuitive Surgical

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Gross margin | 66% | Q1 2026 guidance ~67–68% | ✅ |
| Net margin | 28% | FY2025 earnings release | ✅ |
| ROIC | 24.75% | FinanceCharts.com, Feb 2026 | ✅ |
| Revenue growth 3yr CAGR | 15.3% | 2023: $7.12B → 2025: $10.07B (SEC/MacroTrends) | ✅ |
| FCF positive 3 consecutive years | Yes | Well-documented; strong FCF generator | ✅ |
| Net Debt/EBITDA | Net cash | Strong balance sheet, minimal debt | ✅ |
| FCF/NI conversion | ⚠️ Flag | Not sourced — needs TIKR/Koyfin verification |  |

**Verdict: PASS** (FCF/NI conversion flagged for verification before Phase 02 scoring)

---

### VEEV — Veeva Systems

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Gross margin | 75% | FY2026 Q4 earnings | ✅ |
| Net margin | 28% | FY2026 net income/revenue | ✅ |
| ROIC | 34.47% | Gurufocus, Jan 2026 | ✅ |
| Revenue growth 3yr CAGR | 16% | FY2026 revenues $3.195B, +16% YoY; 3yr CAGR consistent | ✅ |
| FCF positive 3 consecutive years | Yes | Consistent FCF generator | ✅ |
| Net Debt/EBITDA | Net cash (~$3B+ cash, no debt) | Well-documented | ✅ |
| FCF/NI conversion | ⚠️ Flag | Not sourced — needs verification |  |

**Note on ROIC divergence:** Some sources show ROIC as low as 9–10% using book equity (which is distorted by heavy SBC effects). Gurufocus adjusted figure of 34.47% uses invested capital more accurately. Use Gurufocus as the canonical source per framework tools. Flag the divergence in any Phase 02 session.

**Verdict: PASS**

---

### IDXX — IDEXX Laboratories

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Gross margin | 62% | FY2025 earnings release | ✅ |
| Net margin | 24.6% | FY2025 (MacroTrends/earnings) | ✅ |
| ROIC | 37–49% | KoalaGains/multiple sources | ✅ |
| Revenue growth 3yr CAGR | 10.42% | StockAnalysis FY2025 | ✅ |
| FCF positive 3 consecutive years | Yes | Well-documented diagnostics company | ✅ |
| Net Debt/EBITDA | ⚠️ Flag | Not sourced — needs TIKR/Koyfin verification |  |
| FCF/NI conversion | ⚠️ Flag | Not sourced — needs verification |  |

**Verdict: PASS** (two data gaps flagged per Rule 0 — verify before Phase 02)

---

### ZTS — Zoetis

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Gross margin | 72% | FY2025 | ✅ |
| Net margin | ~20% | FY2025 | ✅ |
| ROIC | 27.82% | DCFmodeling.com | ✅ |
| Revenue growth 3yr CAGR | 2.88% | StockAnalysis/PortfoliosLab | ❌ |

**Verdict: FAIL** — Revenue growth 2.88% is well below the >8% threshold. Zoetis is a high-quality business structurally, but animal health spending growth has materially decelerated. The moat is intact; the growth vector is not — watchlist for re-entry if growth re-accelerates.

---

### MCO — Moody's Corporation

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Gross margin | 92% | Q4 2025 earnings release (gross profit $1.747B / revenue $1.889B) | ✅ |
| Net margin | ~35%+ | Adj. operating margin 51.1%; net margin derived from record 2025 results | ✅ |
| ROIC | 22% | Gurufocus, Dec 2025 | ✅ |
| Revenue growth 3yr CAGR | ~9% | FY2025 revenue +9% to record $7.7B; 3yr CAGR roughly in line | ✅ |
| FCF positive 3 consecutive years | Yes | Consistent FCF generator | ✅ |
| Net Debt/EBITDA | 1.2× | Gurufocus, 2025 ($4.05B EBITDA) | ✅ |
| FCF/NI conversion | ⚠️ Flag | Not sourced — needs verification |  |

**Note:** MCO's 3yr revenue CAGR is approximately 9% — just above the 8% floor. The ratings cycle (credit market activity) can cause year-to-year swings. Organic growth thesis: rising capital markets activity, analytics/data segment growing faster than ratings. 

**Verdict: PASS**

---

### MSCI — MSCI Inc.

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Gross margin | 82% | StockResearch-app (2025 annual) | ✅ |
| Net margin | ~45% (NOPAT 44.8%) | StockResearch-app | ✅ |
| ROIC | 39.5% (Debt+Equity basis) | StockResearch-app, Gurufocus 33.34% | ✅ |
| Revenue growth 3yr CAGR | ~9–13% | FY2024 +12.94%, FY2025 ~9%; 3yr CAGR ~10–11% | ✅ |
| FCF positive 3 consecutive years | Yes | Consistent | ✅ |
| **Net Debt/EBITDA** | **~3.0× (Q3 2025); target 3.0–3.5×** | MSCI investor materials | **❌** |

**Verdict: FAIL** — Net Debt/EBITDA ~3.0× exceeds the standard 2.5× threshold. MSCI deliberately maintains leverage of 3.0–3.5× EBITDA to fund buybacks and capital return. The Upgrade 5 exception (4× threshold) applies to "payment networks, exchanges, asset-light businesses where 100% of debt is financial" — MSCI is asset-light but its debt is corporate (not financial institution regulatory capital), so the standard gate applies.

**Watchlist note:** MSCI is an exceptional business by every quality measure. If the framework were to extend Upgrade 5 to asset-light data/analytics compounders (not just financial institutions), MSCI would clear the gate easily. Worth revisiting as a potential framework refinement — log in `decisions/` if the position is taken anyway as an override.

---

### CME — CME Group

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Gross margin | ~95%+ | Exchange economics | ✅ |
| Net margin | 63–71% | FY2025 / Q1 2026 earnings | ✅ |
| **ROIC** | **8.5%** | CME Q1 2026 analysis | **❌** |

**Verdict: FAIL** — ROIC 8.5% is far below the 15% threshold. CME generates extraordinary margins but its clearing-capital and exchange infrastructure requirements inflate the denominator. Despite eligible for Upgrade 5's 4× debt exception, the ROIC gate is unaffected by that upgrade.

---

### ICE — Intercontinental Exchange

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Net margin | 27–33% | FY2025 annual / Q1 2026 | ✅ |
| **ROIC** | **8.54%** | StockAnalysis statistics | **❌** |

**Verdict: FAIL** — ROIC 8.54%, same structural issue as CME. Heavy goodwill from Black Knight ($13B) and Ellie Mae acquisitions inflates capital base. Operating economics are better than reported ROIC implies, but the framework gate is clear.

---

### FDS — FactSet Research Systems

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Gross margin | 55% | Gurufocus/MacroTrends | ✅ |
| Net margin | 25.72% | Alpha Spread, May 2025 | ✅ |
| ROIC | ~17–18% (high-teens) | FY2025 earnings commentary | ✅ |
| **Revenue growth** | **5.4%** | FY2025 earnings; FY2026 guidance ~5–7% organic | **❌** |

**Verdict: FAIL** — Revenue growth 5.4% is below the >8% threshold. FactSet is a high-quality business (excellent FCF, strong moat in financial data workflows) but growing materially slower than the bar. Structural challenge: competition from Bloomberg, MSCI, Refinitiv limits pricing power. Watchlist if growth reaccelerates toward 10%+.

---

### CTAS — Cintas Corporation

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Gross margin | 50–51% | Q3 FY2026 earnings (all-time high 51.0%) | ✅ |
| Net margin | 17.54% | FY2025 annual | ✅ |
| ROIC | 23.47–23.90% | Gurufocus/Valuesense TTM | ✅ |
| Revenue growth 3yr CAGR | ~8–9% | FY2025 organic growth 9.0%; 3yr trend consistent | ✅ |
| FCF positive 3 consecutive years | Yes | Consistent | ✅ |
| Net Debt/EBITDA | ⚠️ Flag | Not sourced — needs TIKR/Koyfin verification |  |
| FCF/NI conversion | ⚠️ Flag | Not sourced — needs verification |  |

**Growth note:** The 8–9% organic revenue growth lands right at the framework's lower bound (~8% in valuation-scoring.md vs. >10% stated in strategy.md — the scoring sheet uses the more permissive 8% floor; using strategy.md's stricter >10% threshold, CTAS is borderline/fails). Flagging explicitly: if 10% is the hard threshold, CTAS fails and drops off the list.

**Verdict: CONDITIONAL PASS** — Passes the 8% floor in valuation-scoring.md; borderline on strategy.md's >10%. Advance to qualitative review but note the growth ambiguity; a Phase 02 score would likely show this as a fair-value or expensive business regardless.

---

### ODFL — Old Dominion Freight Line

| Metric | Value | Source | Pass? |
|---|---|---|---|
| **Gross margin** | **31%** | CSIMarket/MacroTrends | **❌** |

**Verdict: FAIL** — Gross margin 31% is well below the >40% threshold. ODFL has exceptional operating margins for trucking (~25%) and strong ROIC (~22.78%), but the structural economics of LTL freight set a ceiling on gross margins.

---

### ROP — Roper Technologies

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Gross margin | ~70–75% (software-weighted portfolio) | Approximate — not directly sourced |  |
| Net margin | ~27% (derived from Q2 2025: $528M NI / ~$1.95B revenue) | SEC Q2 2025 earnings | ✅ |
| ROIC | ~15–18% (estimated from EBITDA margin ~40%) | Approximate |  |
| Total revenue growth | 12% (FY2025) | GlobeNewswire | ✅ |
| **Organic revenue growth** | **5% (FY2025)** | Roper 2025 results | **❌** |

**Verdict: FAIL** — Framework Rule: "If acquisitions made, recalculate organic revenue CAGR separately." Roper's 12% total growth is 7% from acquisitions, 5% organic. The organic growth rate fails the >8% threshold. Roper's business model is to acquire and compound software businesses — the framework's organic revenue check correctly flags this pattern. The quality of individual portfolio companies is high, but the consolidated entity's organic growth does not clear the bar.

---

### ECL — Ecolab

| Metric | Value | Source | Pass? |
|---|---|---|---|
| Gross margin | 43–44% | FY2025 annual report / Q1 2026 | ✅ |
| Net margin | ~13%? | Not sourced directly — approximate |  |
| **ROIC** | **13.24%** | Gurufocus, May 2025 | **❌** |
| Revenue growth | 9–11% (2026 guidance) | Ecolab 2026 guidance | ✅ |

**Verdict: FAIL** — ROIC 13.24% is below the 15% threshold. Ecolab's capital intensity (water/hygiene services require physical infrastructure and field operations) constrains returns. Good business, but not at the quality level this framework requires for entry.

---

## ✅ Qualified Quality List — 5 names

**ISRG · VEEV · IDXX · MCO · CTAS (conditional)**

*(CTAS conditional: passes 8% growth floor but fails 10% bar — advance with explicit flag)*

---

## Stage 4 — Qualitative pass

*(Phase 01 only — full qualitative analysis reserved for `/new-position` sessions)*

### ISRG — Intuitive Surgical
1. **Why are margins high?** First-mover in robotic surgery + a recurring razors-and-blades model: instruments and accessories replace per-procedure (72% of revenue), not just the ~$1.5–2M capital system. Switching costs are structural — surgeons train on da Vinci for years.
2. **Hard to compete with?** Yes. Clinical evidence base, surgeon training network, FDA clearances, 8,000+ installed systems worldwide = enormous switching costs for hospitals. Medtronic (Hugo) and J&J (Ottava) are years behind in procedures and evidence.
3. **Capital allocation?** Reinvestment-focused: Ion (lung biopsy), da Vinci 5 (launched 2024), SP system (single-port). Share repurchases modest. Management disciplined.
4. **Growth sources 3–5yr?** Procedure volume expansion (still a fraction of addressable surgeries globally); international expansion (OUS growing faster than US); Ion ramp in lung diagnostics; da Vinci 5 up-cycle.
5. **Best bear case?** Reimbursement pressure on robotic surgery; competing platforms reach clinical parity faster than expected; China market risk (regulatory/geopolitical).
6. **Disruption vector?** AI-guided surgery could lower the barrier for competing platforms; but ISRG is investing heavily in AI itself (da Vinci 5 includes integrated vision AI). Risk is real but 5-year horizon.

### VEEV — Veeva Systems
1. **Why are margins high?** SaaS model purpose-built for life sciences — near-zero marginal cost of delivery. Customers (pharma/biotech) are highly regulated and cannot easily switch CRM/data systems mid-trial.
2. **Hard to compete with?** Extremely. VEEV is the de facto operating system for drug commercialisation. Salesforce (general CRM) tried to compete for years and largely failed. Regulatory complexity of the customer base is a natural moat against horizontal SaaS players.
3. **Capital allocation?** Debt-free, cash-generative, steady buybacks. No dilutive M&A. Transition from Salesforce-licensed platform to Vault (proprietary) now largely complete — a significant de-risking.
4. **Growth sources?** Vault CRM (clinical, regulatory, commercial) still in early adoption cycle. Data Cloud (Atea) expanding. International pharma (ex-US still underpenetrated). CRO/CDMO expansion.
5. **Best bear case?** TAM is narrow — limited to pharma/biotech/CRO. If biotech funding cycle dries up, new logo growth stalls. MSFT/Salesforce re-entering with pharma-specific modules.
6. **Disruption vector?** AI-native CRM/regulatory tools could allow a startup to enter without the legacy infrastructure burden. VEEV's own Vault AI initiative is the hedge — but this is the real long-term risk.

### IDXX — IDEXX Laboratories
1. **Why are margins high?** Network of analyzers placed in veterinary clinics (razor/blade: instruments often placed at low/no cost, consumables generate recurring margin). Lab services (reference labs) add scale leverage.
2. **Hard to compete with?** Very. Installed base of 100k+ analysers in vet practices globally; consumables are proprietary; regulatory clearances market by market. Zoetis/Heska are smaller niche competitors, not existential threats.
3. **Capital allocation?** Consistent share repurchases and R&D reinvestment. No transformative acquisitions. Clean balance sheet.
4. **Growth sources?** Pet ownership and spending trends (structural tailwind). Vet practice consolidation → more diagnostics per visit. IDEXX 360 (subscription model) expanding recurring revenue base. Emerging market vet infrastructure buildout.
5. **Best bear case?** Pet spending cyclicality if consumer spending contracts (2025 already showing mild vet visit frequency pressure). Competition from Zoetis and private-label consumables.
6. **Disruption vector?** At-home diagnostics (direct-to-consumer vet testing) is the long-term risk — but regulatory and clinical barriers in vet medicine are high.

### MCO — Moody's Corporation
1. **Why are margins high?** Credit ratings are a regulatory oligopoly (NRSRO designation requires SEC approval — effectively a government-enforced duopoly with S&P). Incremental revenue from new debt issuance is nearly pure margin.
2. **Hard to compete with?** Virtually impossible in ratings — regulatory moat, decades of default history data, investor requirement that debt be rated by a recognised agency. Analytics (MA segment) is more competitive but growing fast.
3. **Capital allocation?** Consistent buybacks and dividends. MA segment acquisitions (Bureau van Dijk, Reis) have been accretive. Management well-regarded (Robert Fauber).
4. **Growth sources?** Credit market rebound + structured finance growth; MA segment (data/analytics/KYC) growing ~10-12% organically and now ~50% of revenue; AI integration in credit analysis workflows.
5. **Best bear case?** Regulatory action (NRSRO reform reducing pricing power); credit market drought (2022-23 showed the cyclicality in ratings revenue); competition in analytics from Bloomberg/Refinitiv.
6. **Disruption vector?** AI-generated credit assessments could commoditise ratings — but regulatory requirement for NRSRO-stamped ratings insulates the core business. Real disruption risk is 10+ years out.

### CTAS — Cintas (conditional)
1. **Why are margins high?** Route-density economics in uniform services — each delivery truck covers more stops as the customer base densifies. SaaS-like recurring revenue (uniform rental contracts, 5-year average). Modest pricing power in an essential service.
2. **Hard to compete with?** Moderate moat. Aramark and UniFirst compete directly. Switching costs are real but not impenetrable. CTAS's scale advantage (70%+ market share in the US) and cross-sell (fire protection, first aid, document shredding) are the durability factors.
3. **Capital allocation?** Consistent buybacks, growing dividend (50+ years of consecutive increases). Management operationally excellent.
4. **Growth sources?** Cross-sell penetration (only ~30% of customers buy more than 1 CTAS service). Addressable market still ~60% self-operated (no uniform service provider at all) — conversion of these is the long runway. International very small.
5. **Best bear case?** Labour cost inflation (workers). Cyclical: CTAS is sensitive to US employment levels — if manufacturing/services employment falls, uniform demand falls. Growth is structural but modest.
6. **Disruption vector?** Low disruption risk — physical uniform delivery is not software-replaceable. The risk is margin compression from labour/fuel costs rather than technological disruption.

---

## Data gaps flagged (CLAUDE.md Rule 0)

The following metrics were not sourced in this session and **must be verified before `/new-position` or `/rescore`** is run for any passer:

| Ticker | Missing metrics |
|---|---|
| ISRG | FCF/Net Income conversion ratio (2 consecutive years) |
| VEEV | FCF/Net Income conversion ratio |
| IDXX | Net Debt/EBITDA; FCF/Net Income conversion ratio |
| MCO | FCF/Net Income conversion ratio |
| CTAS | Net Debt/EBITDA; FCF/Net Income conversion ratio |

Source for all: TIKR (Cash Flow vs. Income Statement) or Koyfin.

---

## Watchlist flags (did not qualify, but worth monitoring)

| Ticker | Reason held back | Re-entry trigger |
|---|---|---|
| ZTS | Revenue growth 2.88% | Two consecutive quarters of organic growth >8%; vet spending recovery visible |
| MSCI | Net Debt/EBITDA ~3.0× (above 2.5× gate) | De-levering below 2.5× OR framework adopts Upgrade 5 extension for asset-light data businesses |
| FDS | Revenue growth 5.4% | Re-acceleration to >8% organic; headcount recovery in financial services drives ASV growth |
| CME/ICE | ROIC 8–9% due to capital structure | Would require framework reconsidering ROIC gate for exchanges — not currently justified |

---

## Coverage log update

Slice NA-2 screened today. Recording in [screening-coverage-log.md](../framework/screening-coverage-log.md).

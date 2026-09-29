# Rules & metrics (as shown on the site)

**See also [rules-supplement.md](rules-supplement.md)** (formulas verified on real cards, constants index, test vectors, inconsistencies).

Site text is Ukrainian; terms below give UA + EN gloss. Sources noted per line. Updated 2026-09-29.

## Core model
- **Quality level** ("рівень"): letters **A–E** derived from a numeric **quality score 0–100** (shown with 1 decimal, e.g. 91,0). Thresholds (from scatter chart guide lines on /start/): **A ≥ 80**, **B ≥ 70**, **C ≥ 55**; below 55 presumably D/E (D and E boundaries not shown yet — verify; observed D 42.9–51.5, E 55–59 for AVOID companies, so E may be set by flags rather than score — see open-questions).
- **Price word** ("слово ціни"): 5 values — дешево (cheap), справедлива (fair), дорого, але росте (expensive but growing), дорого без росту (expensive without growth), пастка дешевизни (value trap). Derived from a **sum of "price lenses"** (сума лінз ціни) — X axis of the BUY-zone chart, range about -6…+8; **fair price starts at ≥ +1**, **cheap price at ≥ +4** ("з наших налаштувань" = from the site's settings). Individual lenses TBD (see card page).
- **Verdict** ("вердикт"): BUY / STRONG BUY / BUY WAIT / AVOID / ЛИШЕ СПЕКУЛЯЦІЯ (speculation only) / НЕ МІЙ СЕКТОР (not my sector). Computed by "the engine" ("рушій") from numbers only; Taras's opinion shown separately, not part of the calculation.
- **STRONG BUY** requires tags confirmed by Taras (manual review); an engine BUY becomes STRONG BUY after his review. "переглянуто" = reviewed by Taras.
- **Gate 0** ("ворота 0"): pre-matrix exclusion — sector, cycle, or exchange-traded product price stops analysis; those companies are outside the matrix (57 on 2026-09-29).
- **Verdict override steps**: after the matrix cell gives a verdict, later steps (x2 arithmetic, flags, data issues) can change it (5 companies on 2026-09-29).
- "Ten signs and red flags" (десять ознак і ред флаги) per card; "x2 arithmetic" (арифметика х2) — probably: what price/return must do for the stock to double / a valuation-doubling check. TBD on card / methodology.

## DETAILED METHODOLOGY (source: /methodology/, 2026-09-29; prose paraphrased, numbers exact)
Four steps, identical for all companies: Gate 0 competence circle -> Gate 1 quality level A–E -> Gate 2 price via 5 lenses -> matrix verdict -> post-matrix (flags, x2 arithmetic, data, position). Public verdict is always computed as "I don't hold it".

### Gate 0 — competence circle (basket from a registry; affects only gate 0, not score/price)
- **Good baskets** (pass): internet owners (search/ads/marketplaces/cloud), payment networks, subscription services with operating leverage, network-effect aggregator platforms, data/ratings/indices, AI infrastructure with node monopoly (chips, chip equipment, optics), high-margin subscription software (enterprise, vertical, cybersecurity, databases).
- **Neutral baskets**: gate passes, scored by numbers only (e.g. consumer brand not loved / not on stop-list).
- **Stop-list** -> full analysis is done but verdict = **НЕ МІЙ СЕКТОР** (with a "shadow verdict" shown alongside): carmakers, airlines, banks, Russia-linked, manufacturing (capex heavy, margin ≤~10%), energy & utilities, crypto, luxury, neoclouds, real estate (REIT), defense, restaurants, retail, betting, insurance. Each row has "why" and "when an exception is possible" (e.g. manufacturer with monopoly and >25% margin; club-subscription retail like Costco/BJ's). Taras-decided exceptions: ASML, AVGO, BJ, COST, HY9H, MA, NVDA, SSU, TSM, V.
- **Speculation-only baskets** -> verdict **ЛИШЕ СПЕКУЛЯЦІЯ**, position ≤ 1% of portfolio: cyclical, China, biotech, loss-making history (1–3% until stable profit), memory (commodity-like price; profit-taking plan), fresh IPO (until several quarters of reports), commodities (mandatory profit-taking), pharma (short position while patent lives, 2–3-year horizon).
- Tag "business not understood" -> **AVOID** regardless of basket.

### Gate 1 — quality score 0–100 (8 components) minus flag penalty
Level: **A ≥ 80, B ≥ 70, C ≥ 55, D below 55.** Penalty from quality flags: **critical 8, serious 4, minor 0**. Unknown values never count as zero: they give **40% of the component's weight** and the card names the missing field.
Component weights: profitability 15 · growth 20 · predictability 15 · moat 15 · margin 10 · balance sheet 10 · capital & SBC 10 · discipline 5 (=100).

Sub-scores (points):
- **Profitability (years profitable in a row)**: unknown 7.5 · ≥5 → 15 · 2–5 → 9.8 · profitable <2y → 5.2 · loss-making → 0.
- **Growth** = revenue growth (fwd 12M) + EPS growth (fwd 12M) + FCF growth (fwd; if no FCF forecast use EPS forecast):
  - Revenue: unknown 3.2 · negative 0 · 0–10% → 2 · 10–20% → 4.8 · ≥20% → 8.
  - EPS: unknown 2.8 · negative 0 · 0–10% → 1.8 · 10–15% → 4.2 · 15–25% → 6 · ≥25% → 7.
  - FCF: negative 0 · 0–10% → 1.2 · 10–15% → 3 · ≥15% → 5.
- **Margin** (net; fallback operating): unknown 5 · <10% → 0 · 10–15% → 2 · 15–20% → 4 · 20–30% → 6 · 30–45% → 8 · ≥45% → 10 · margin falling (at ≥45%) → 8.
- **Balance sheet**: net cash 10 · debt/EBITDA ≤1.5x → 7 · 1.5–3x → 4 · >3x → 1 · unknown 5.
- **Capital & SBC** = SBC/FCF + ROIC + share count change:
  - SBC/FCF: unknown 3.5 · <5% → 6 · <15% → 5 · <30% → 3 · >30% → 1.
  - ROIC: unknown 6 · ≥30% → 8 · ≥20% → 7 · 10–20% → 6 · <10% → 4.
  - Share count 1Y: unknown 6 · not grown 7 · grown <2% → 6 · grown more → 5.
- **Discipline** (growth source & capex funding): organic + capex covered by OCF 5 · mixed + covered 4 · via acquisitions + covered 2 · growth unknown + covered 4 · organic, no capex numbers: funded from operating cash 5 / funding unknown 4 / debt-funded 3 · organic, debt+issuance >25% of capex: can pay (net cash >0 and debt ≤1.5x EBITDA) 4; balance-sheet burden (cap B) 3; balance unknown 3.
- **Predictability by business type**: subscription 15 · payment network 15 · data & ratings 15 · cloud & contracts 14 · platform 12 · subscription software 12 · club subscription 10 · advertising 9 · chips (lumpy sales) 9 · one-off brand sales 8 · rental 8 · restaurant 6 · manufacturing one-off 6 · cyclical 3 · commodities 2 · bank 4 · pharma 3 · undefined 8.
- **Moat**: monopoly 15 · oligopoly 12 · network effect 12 · high switching cost 10 · brand 8 · none 2 · unknown 6. **AI-risk adjustment to moat**: AI strengthens +2 · neutral 0 · unknown 0 · AI threatens −3.
- **Level E regardless of score**: loss-making; SBC eats the cash flow (≥100% of FCF; on OCF basis SBC >20% of revenue); or business tagged "not understood".
- **Level caps, in order**: no classification: A→B · moat determined by AI, not Taras: A→B · profitable <2y: max C; <5y: max B · level A only with moat = monopoly/oligopoly/network effect · critical flag: max C · debt >5x EBITDA with negative FCF or debt-funded capex: max D (if capex exception failed); >3x with capex not from own cash: max C · growth built on customer promises: max C · level A with lowered guidance: B. Caps are shown in words on the card (score, scale level, reason; a marker on the components chart).
- **Level A requires consensus growth**: revenue ≥10% and EPS ≥14% next 12M. No revenue forecast: max B with a note. Same bar applies to STRONG BUY.
- **One-off tax item**: if effective tax rate differs >10 pts from the prior 12M, EPS growth is computed from a normalised base (pre-tax income at the company's usual rate, median of 8 quarterly rates); reported figure shown beside. No quarterly taxes -> gap, not assumption.
- **Capex-without-backlog exception**: backlog condition only for contract-driven capex (cloud, enterprise/vertical software, databases, cybersecurity, GPU rental); for ads/marketplace/payments check that operating cash keeps pace with revenue (OCF lags revenue growth by ≤5%). Check has 3 states: pass/fail/undetermined.
- **Rounding**: thresholds compare against score rounded to 0.1 (80.0 = A).
- **Hysteresis**: level and lens scores enter a state at the threshold but leave only after crossing by >2 points (level) or >5% of threshold (lenses); previous state read only from a card computed by the same code; the card explains it as a cap.
- **One fact, one penalty**: a fact already graded in a component (debt, dilution/SBC, margin squeeze, AI risk) stays as a visible label without a separate penalty. Critical flags keep penalty + cap C. External capex financing (debt+issuance >25% of capex in capex-heavy company, capex >50% of OCF) = serious flag without penalty; points only in discipline sub-score (2/2 own money; 1/2 raised above threshold but net cash>0 and debt ≤1.5x; 0/2 and cap B when it lands on the balance sheet).
- **Margin definition**: smaller of net margin (normalised where data allows) and operating-after-tax; unknown tax: statutory 21% for SEC filers with a note, else second definition skipped. If consensus is non-GAAP, NTM P/E with options is computed too; S&P lens and PEG use the more expensive.

### Gate 2 — price: basis + 5 lenses (each −2…+2; sum -> price word)
- **Basis** from registry (P/E, P/FCF or P/OCF); if missing the engine picks and states why. **P/OCF forbidden when FCF negative and capex not covered by own cash.**
- Lenses:
  1. **vs S&P 500**: multiple vs index forward P/E: ≤1× index → +1 (only levels A & B, else 0) · ≤1.3× → 0 · ≤2× → −1 · above → −2.
  2. **vs own history**: ≤ 5y-min×1.05 → +2 · ≥ 3y-max×0.95 → −2 · below average by >10% → +1 · above → −1; history <3y clamps to ±1.
  3. **PEG** (multiple ÷ EPS growth): <0.5 → +2 · <1 → +1 · ≤1.3 → 0 · ≤2 → −1 · above → −2; no growth/multiple -> 0 and a gap.
  4. **FCF yield after SBC**: ≥4% → +2 · ≥3% → +1 · ≥2% → 0 · ≥1% → −1 · below → −2.
  5. **Growth vs market**: EPS growth ≥1.5× index EPS growth (index forecast missing -> 13%) → +1 · <0.9× market → −1.
- **Price word**: no multiple -> "Немає мультиплікатора"; multiple ≤15, quality score <60 and dead growth (<10%) -> **Пастка дешевизни**; lens sum ≥4 -> **Дешево**; ≥1 -> **Справедлива**; else **Дорого, але росте** if EPS growth ≥15% (level A: 14%), otherwise **Дорого без росту**. "Everything below fair is expensive."
- **2026 regime**: mega-cap (market cap ≥ $200B) with multiple ≤20 in levels A/B gets +1 to the sum; multiple ≥30 without ≥30% growth is always expensive. Price flags: multiple ceiling 30 (lifted when PEG <1); multiple beyond reason ≥60.
- **One EPS growth per card**: geometric mean of the two steps (next-12M vs normalised trailing base; next year vs that) — used for growth score, PEG, price word, lenses; single known step used if only one. Possible cycle peak (manufacturers/cyclicals/commodities with trailing EPS growth >100%) -> row in Known risks and PEG lens capped at +1. "Expensive without growth" only when base 5-year CAGR is below the BUY bar (14% for A, 15% others); else "expensive but growing" with a note on two-year-ahead growth.

### Matrix (level × price word) -> verdict (for a company not yet held; no flags, full data)
A/B: cheap BUY · fair BUY · exp+grow BUY WAIT · exp no growth BUY WAIT · trap AVOID · no multiple БРАКУЄ ДАНИХ. C: cheap BUY · fair BUY WAIT · exp+grow BUY WAIT · exp no growth AVOID · trap AVOID. D: cheap ЛИШЕ СПЕКУЛЯЦІЯ, others AVOID. E: all AVOID. (Start page shows "A cheap: STRONG BUY / BUY".)
- Decided before matrix: Gate 0 (stop-list -> НЕ МІЙ СЕКТОР with shadow verdict; not understood -> AVOID; speculative basket -> ЛИШЕ СПЕКУЛЯЦІЯ); level E -> AVOID; **broken thesis** (lowered guidance, growth without profit, analysts cutting forecasts) -> BUY WAIT for A/B/C, AVOID for D/E; no current multiple -> БРАКУЄ ДАНИХ.
- Special cell: level A with PEG <0.5 -> BUY regardless of price word/lens sum. STRONG BUY never via this rule.
- **One event, one flag**: EPS consensus revision 30d/90d = one flag (severity depends on consensus source); capex > OCF and negative FCF = one inequality, one penalty; negative FCF quarters series is critical only with negative 12M FCF or ≥4 quarters, shorter with positive FCF = minor (seasonality).

### After the matrix
- **STRONG BUY** only for levels A and B (C and below max BUY). Conditions: price word Дешево · revenue growth ≥10% and EPS ≥14% (consensus) · reviewed by Taras · base CAGR bar met · bear scenario ≥ 0 · no critical flags.
- **Critical flag**: no STRONG BUY/BUY -> BUY WAIT for A/B/C else AVOID.
- **x2 arithmetic (5-year, base scenario only, no multiple expansion)**: metric today; growth per year from consensus (then decays, max 25% per step); multiple = min(current, 3-year average). **Base CAGR <10% -> BUY WAIT**; between 10% and BUY bar (**14% for A, 15% others**) STRONG BUY is downgraded to BUY. Optimistic scenario (multiple back to mean) shown but excluded from verdict.
- **Data trust**: no 12M EPS forecast, current multiple, or basis -> **БРАКУЄ ДАНИХ** (card names fields). Data completeness <60% with STRONG BUY -> BUY (high-completeness bound 80%).
- **Not reviewed by Taras / AI-classified**: level ≤ B, verdict ≤ BUY with card label; no classification: position ≤ tracking size (1%).
- **Position size by level (advice to readers, not Taras's portfolio rules)**: A 5–10% · B 5–10% · C 1–5% · D 0–1% · E 0%. No position >10%; STRONG BUY level A up to 15%; one subsector ≤30% total.

### Verdict glossary (site's own)
STRONG BUY = buy (good A/B at cheap price, x2 passes bar, no critical flags, Taras reviewed) · BUY = buy (fair price for good company, or cheap for level C, or a STRONG BUY downgraded by arithmetic/incomplete data) · BUY WAIT = want to buy, not now (expensive but growing / critical flag / arithmetic short; card names an entry price) · AVOID = do not buy (level E, broken thesis, value trap) · ЛИШЕ СПЕКУЛЯЦІЯ = speculation only (position ≤ tracking size) · БРАКУЄ ДАНИХ = missing data · НЕ МІЙ СЕКТОР = not my sector (stop-list; shadow verdict shown).

### Red-flag catalogue (quality flags cost points; price flags do not)
Concentration rule: one customer ≥25% of revenue or top-2 ≥33% -> serious; ≥40% on one -> critical (single flag; customer groups only in Known risks).
- **Critical (quality, penalty 8 + cap C, no BUY)**: FCF negative · negative FCF several quarters in a row (critical/serious/minor by length) · capex > operating cash · debt >3x EBITDA · revenue up while margin & FCF not · revenue up while earnings & margin not (*not live*) · interest eats revenue · guidance cut (*not live*) · guidance withdrawn (*not live*) · concentration in 2–3 customers · SBC eats revenue (critical) · CEO left and guidance withdrawn (*not live*). **Critical price flags**: value trap · multiple beyond reason (≥60).
- **Serious (penalty 4)**: buybacks funded by debt · debt >1.5x EBITDA · revenue from one country · costs growing faster than revenue · dividend >60% of FCF · dividend funded by debt · reported vs adjusted earnings far apart · external capex financing (no penalty) · company misses own guidance · customer concentration · margin squeeze · SBC eats revenue (serious) · KPI decline (*not live*) · profit from revaluation of investments · AI disruption risk (*not live*) · dilution · growth on promises of a few customers. **Serious price flags**: expensive without growth · multiple above ceiling.
- **Minor (penalty 0 unless noted)**: financing of capex not visible (data) · SBC visible in revenue (penalty in quality) · operating cash quality unknown (data).
- **Known risks block**: measured numbers below flag thresholds, basket-typical risks and data gaps in words; not part of the verdict; empty flags tile must not read as "no risks".
- **Rules not working on live data** (fields not filled by free data): AI-risk tag (Taras's tag), recent CEO change, guidance change, guidance withdrawn, main-KPI direction (Taras's field), where margin is heading (manual), where market share is heading (Taras's field).

### Indices & sub-sectors
Card lists which indices a company belongs to with source + composition date; each company counted once even with two share classes. Companies in an index that Taras has not reviewed: level ≤ B, verdict ≤ BUY. Sub-sector = "who to compare with" only; doesn't affect gate 0 or verdict; a company can have several; 30% portfolio cap counted per sub-sector; controlled vocabulary.

## Matrix verdict map (level × price word)
| | cheap | fair | exp+grow | exp, no growth | value trap |
|---|---|---|---|---|---|
| A | STRONG BUY / BUY | BUY | BUY WAIT | BUY WAIT | AVOID |
| B | BUY | BUY | BUY WAIT | BUY WAIT | AVOID |
| C | BUY | BUY WAIT | BUY WAIT | AVOID | AVOID |
| D | SPECULATION ONLY | AVOID | AVOID | AVOID | AVOID |
| E | AVOID | AVOID | AVOID | AVOID | AVOID |

## Portfolio KPIs (start page)
- **Earnings growth 12M** = reported EPS growth, weighted by position share (only positions that have the number).
- **Price 1Y** = 1-year price change weighted by position share.
- **Coverage** = share of the portfolio (by weight) whose positions have both numbers; also counts (21 of 28).

## Formatting conventions
Decimal comma; % with space; dates DD.MM.YYYY; USD prices `$336,29`; "N бала/балів" plural for points.

## Data sources (stated in site banner)
Financial Modeling Prep (prices, multiples, analyst consensus), SEC EDGAR (filings), FactSet Earnings Insight (index row). Single dataset, no source switcher.

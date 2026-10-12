# Red-flag catalogue — thresholds recovered from card sentences (2026-10-03)

Full list of 36 methodology rows with keys, severity, category, penalty and "live" marker: `methodology-rules.json -> flags.rows`. Below: only what the 20 cards revealed about **numbers**. Penalty logic: quality.md section 9. Flag sentences and the "Відомі ризики" block are captured per card in `data/cards/<T>.json -> flags`.
Status: Fitted(sample) unless noted; "below" = a below-threshold measurement printed in "Відомі ризики" (these state the exact threshold!).

| Flag key | Severity | Threshold evidence |
|---|---|---|
| `leverage_above_threshold` | serious | net debt/EBITDA > **1.5x** ("вище порога 1,5x": CRM 2.8x, ORCL 2.9x); below-line printed for AAPL "0,1x (прапорець від 1,5x)" |
| `leverage_high` | critical | > **3x** EBITDA (methodology; none in sample) |
| `sbc_revenue_*` (minor/major/critical/hard) | minor / serious / critical | SBC to revenue: keys `red_flags.thresholds.sbc_revenue_major = 5 %`, `_critical = 10 %`, `_hard = 20 %`. AAPL 2.9 % -> "прапорець від 5,0 %" (below); ADBE 8 % and ABNB 13 % and PLTR 13.6 % -> serious. A 10 %+ ratio stays serious (not critical) when mitigated: ABNB "кількість акцій за рік не зросла, тому серйозний, а не критичний"; PLTR "при такому рості не критично; SBC до FCF падає: рік тому 43 %, зараз 25 %" |
| `share_dilution` | serious | diluted share count +1 % per year ("розмиття за рік 0,9 % (прапорець від 1,0 %)" AMZN below; AMD +1.8 %, ORCL +3.1 % flagged) — same 1 % as ten-signs and key `quality.dilution_max` is 2 % for the capital score |
| `capex_external_financing` | serious | (net debt raised + shares issued) / capex over 12M **> 25 %** in a capex-heavy company (AMZN 44 %, GOOG 82 %, META 34 %, ORCL 73 %, TSLA 45 %); MSFT below at -1 % |
| `capex_exceeds_ocf` | critical (or minor when "waiver passed") | capex > OCF; mitigated to minor "пом'якшено: capex фінансується власними грошима, waiver пройдено" (AMZN) when capex is own-cash funded under contracts and ROIC (3y avg) is good (19 %). ORCL (capex $75.7 B > OCF $46.9 B, external funding) stays critical |
| `fcf_negative_streak` | critical / minor | negative FCF 6 quarters in a row and TTM negative (ORCL) = critical; AMZN "FCF від'ємний ... capex під законтрактований беклог" mitigated to minor |
| `growth_without_cash` | minor (mitigated) | META "FCF падає при рості виручки, але це capex за свої, під контракти і при ROIC 37 %" -> minor |
| `growth_without_profit` | critical | revenue +12 % while operating margin -2 % and EPS -20 % in 12M (TSLA) |
| `customer_concentration_major` | serious | one customer **>= 25 %** of revenue/backlog (AVGO ~32 %, TSM Apple ~25 %); below-line: AMD largest customer 18 % "(прапорець від 25 %)"; NVDA two largest 31 % "(прапорець від 33 %)" (top-2 threshold 33 %) |
| `customer_concentration` | critical | >= **40 %** on one customer (ORCL: OpenAI ~50 % of revenue or backlog) |
| `country_concentration` | serious | >= **35 %** of revenue outside the home country, home country by filing type (TSM: US 74 %, 20-F filer, home TW) |
| `margin_compression` | serious | operating margin down 3 % points in a year (V "Операційна маржа за рік стиснулась на 3 %"); chart marks quarters where the 12M operating margin is >= 2 pp lower (threshold "поріг стиснення маржі ... таких кварталів 5") |
| `profit_from_investments` | serious | revaluation of stakes is a large share of net income (AMZN, GOOG, CRM: "59 % чистого прибутку це переоцінка часток"; threshold unknown, penalty 4) |
| `misses_own_guidance` | serious | consensus beaten in only 33 % of quarters in 3 years (TSLA; "прогнозованість слабка") — threshold unknown |
| `dividend_from_debt` | serious | dividend paid while FCF negative (ORCL) |
| `payout_too_high` | serious | dividend > 60 % of FCF (methodology) |
| `multiple_ceiling` | serious (price) | multiple above **30** and growth does not justify (AAPL 35 "ріст його не виправдовує"; COST 40) — lifted when PEG < 1 |
| `multiple_absurd` | critical (price) | multiple >= **60** (PLTR 91, TSLA 165) "за такі гроші не окупиться навіть ідеальний бізнес" |
| `expensive_no_growth` | serious (price) | word == EXPENSIVE_NO_GROWTH (AAPL, COST) with sentence "Мультиплікатор 35,0 при очікуваному рості EPS 10 %" |
| `capex_funding_unknown` / `ocf_quality_unknown` | minor (data) | "Компанія capex-важка, а розбивки операційного кешу на власний і передоплати клієнтів у даних немає" (AMZN, GOOG, META, MSFT, ORCL, TSLA) |

## Measurements printed below thresholds ("Відомі ризики") — exact threshold pairs
SBC/revenue 5.0 % (flag from); net debt/EBITDA 1.5x; largest customer 25 %; top-2 customers 33 %; dilution 1.0 %/yr; external capex financing 25 % of capex; 10-K disclosure threshold for named customers 10 % of revenue.
Also printed: "джерело часток клієнтів" (EDGAR XBRL customer-concentration tags, filing id), buy-back stopped notes ("викуп акцій зупинено з <date>"), AI-drafted press-release and one-off-item notes (guidance direction "чернетка ШІ, впевненість medium/high"; one-offs excluded from EPS growth base when below 25 % of quarter net income or consensus already adjusted).

## Still unknown
Numeric triggers for: `guidance_*`, `kpi_down`, `ai_negative` (not live), `interest_eats_revenue`, `adjusted_heavy`, `opex_outgrows_revenue`, `buyback_debt`, `profit_from_investments`, `misses_own_guidance`, `growth_on_promises` (ORCL text: growth rests on a few large customers' promises and is debt financed), `fcf_negative_ttm`.

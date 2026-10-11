# Ten signs of a good company — recovered pass/fail thresholds

Source: 20 cards x 10 signs (parsed in `data/cards/<T>.json -> ten_signs.items`, mark pass/fail/unknown). Thresholds are inferred from the boundary between passing and failing observed values; each is "Fitted(sample)" (n=20). The card shows the value after each sign name.

| # | Sign | Value shown | Pass | Fail (observed) | Inferred threshold |
|---|---|---|---|---|---|
| 1 | Ріст виручки | NTM revenue growth % | 11, 12, 13, 15 ... 99 | none | <= 11 passes; fail edge unknown (probably 10 % — same as quality `revenue.weak`) |
| 2 | Ріст прибутків EPS | EPS growth % "24 міс." (the single EPS growth) | 13.8 (ADBE), 15.0 | 9.8, 9.7, 9.3, 3.2, -2.7 | threshold in (9.8, 13.8]: 10 % (Hypothesis) |
| 3 | Висока маржа | net margin % | 16 (AMD), 17, 20 ... | 3 (COST), 4 (TSLA) | threshold in (4, 16]: 10 or 15 % (Hypothesis; quality "weak" 10 %) |
| 4 | Повторювана виручка | business type | subscription, platform, software, cloud_hyperscaler, advertising, payments_network, club/retail_membership | **manufacturer, semis_monopoly** (lumpy chips) | by type: fail for chips-lumpy and manufacturing/one-off |
| 5 | Ріст FCF | TTM FCF growth % | 10 (ADBE), 13 ... 197 | 1, 2, 3 (MA, TSLA, V), negative (AMZN, ORCL, GOOG -24, META -24, MSFT -11) | threshold in (3, 10]: 5 or 10 % |
| 6 | Баланс без боргу | net cash or net debt/EBITDA | net cash; 1.0x (UBER), 0.9x ... | 2.8x (CRM), 2.9x (ORCL) | <= 1.5x (matches quality `debt_to_ebitda.ok`) |
| 7 | Capex-лайт | capex % of revenue | 0-12 (TSLA 12 %) | 22 (AMZN), 30, 35, 39, 105 | threshold in (12, 22]: 15 or 20 % |
| 8 | Buybacks без розмиття | share-count change 1Y (and buyback yield) | <= +1 % (AMZN/GOOG/AVGO/TSLA +1) | +2 (AMD), +3 (ORCL) | dilution <= 1 % (printed "поріг розмиття 1 % на рік") |
| 9 | Без концентрації клієнтів | largest customer % of revenue/backlog | none >= 10 % disclosed; AMD 18, V 11 | NVDA 22, TSM 25 (Apple), AVGO 32, ORCL 50 (OpenAI) | threshold in (18, 22]: 20 % (Hypothesis); pass text "у звіті немає клієнта від 10 % виручки" when no customer >= 10 % |
| 10 | Capex з власного кешу | OCF vs capex | OCF covers capex | AMZN, ORCL (capex > OCF) | OCF >= capex |
Unknown mark ("?"): TSM signs 7 and 8 ("capex або виручки за 12 місяців у нашому джерелі немає" / "джерела фінансування capex не видно, грошового потоку немає").
Header "N зелених, M невідомих з 10"; green = pass, red = fail, grey = unknown. "Позитивні сигнали" sentences (ABNB): "Ріст не просто триває, а прискорюється: останній період на 3 % вище за попередні"; "Дешевше за індекс і росте швидше за індекс одночасно" (= S&P lens >= 0 style AND growth lens +1); others seen in the baseline: "beats consensus in 100 % of quarters over 3 years", "revenue and margin growing together".

---
# UPDATE 2026-10-03: thresholds refitted on 488 cards (`analysis/fit_ten_signs.py`, raw: `formulas/ten-signs-fit.json`)
| # | Sign | Pass / fail boundary found |
|---|---|---|
| 1 | Revenue growth NTM | pass >= 8 %, fail <= 8 % (display rounding, threshold about **8 %**; 4 unknown) |
| 2 | EPS growth ("24 міс.") | fail <= 10.0 %, pass >= 10.1 % -> **10 %** |
| 3 | Net margin | fail <= 15 %, pass >= 15 % -> **15 %** |
| 4 | Recurring revenue | by business type: pass = platform, subscription, software, cloud_hyperscaler, advertising, payments_network, retail_membership, data_monopoly; fail = cyclical, manufacturer, pharma, semis_monopoly (chips lumpy), bank, retail; unknown = unclassified |
| 5 | FCF growth | fail <= 5 %, pass >= 5 % -> **5 %**; negative FCF = fail; 28 unknown |
| 6 | No debt | pass <= **2.0x** net debt/EBITDA (or net cash), fail >= 2.0x (the quality scale uses 1.5x/3x; this sign uses 2x) |
| 7 | Capex-light | pass <= **15 %** of revenue, fail >= 15 % |
| 8 | Buy-backs without dilution | pass share-count change <= +1 %, fail >= +1 % -> **1 %** |
| 9 | No customer concentration | pass: largest customer <= 18 % (or none >= 10 %), fail >= 22 % -> about **20 %**; 412 cards unknown/"немає клієнта від 10 %" |
| 10 | Capex from own cash | OCF >= capex |
Each tile header: "N зелених, M невідомих з 10".

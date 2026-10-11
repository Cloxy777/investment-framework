# Screen: Screener ("Скринер") — `/screener/`

- Nav: Скринер -> Усі компанії. Captured 2026-09-29. Screenshots: `screener__default.jpg`, `screener__filtered-buy-b.jpg`, `screener__verdict-dropdown-open.jpg`.
- Page title: "Скринер: усі компанії за матрицею Тараса Гука". Filter/sort state lives in the **URL hash**, e.g. `/screener/#verdict=BUY&level=B&sort=score&dir=1` (=> shareable/bookmarkable; also a "скопіювати посилання" button).
- Inbound: start-page CTA buttons ("Відкрити в скринері з цими фільтрами", "Усі 16 компаній зони BUY у скринері"), nav menus.
- Note: on first paint the header briefly showed a "Увійти" (sign-in) button in place of "Кабінет" (auth state resolves after load) — see open-questions.

## Purpose
Filterable, sortable table of **all company cards** (164 total; default view "показано 104 з 164").

## Inputs
### Primary filters (always visible; native `<select>`)
| Control | Options (label = value) |
|---|---|
| Verdict (default "усі вердикти") | STRONG BUY · BUY · BUY WAIT · AVOID · ЛИШЕ СПЕКУЛЯЦІЯ (`SPEC_ONLY`) · БРАКУЄ ДАНИХ (`NEED_DATA`) · НЕ МІЙ СЕКТОР (`NOT_MINE`) |
| Level (default "усі рівні") | A · B · C · D · E |
| Price word (default "будь-яка ціна") | дешева ціна (`CHEAP`) · справедлива ціна (`FAIR`) · дорого, але росте (`EXPENSIVE_GROWING`) · дорого без росту (`EXPENSIVE_NO_GROWTH`) · пастка дешевизни (`VALUE_TRAP`) · ціну не оцінено (`NO_MULTIPLE`) |
### "Ще 16 фільтрів" (expandable extra filters, button)
- Valuation-change quadrant (`будь-яка зміна оцінки`): cheaper_on_business "Дешевшає, а бізнес росте (buying opportunity)" · cheaper_on_estimates "Дешевшає, бо прогнози гіршають" · pricier_on_business "Дорожчає разом з бізнесом" · pricier_without_reason "Дорожчає без підстав".
- Basket (`усі кошики`, ~28 values): auto, bank, biotech, manufacturer, internet owners, data/ratings/indices, energy&utilities, loss-making story, other, China, crypto, luxury, neoclouds, REIT, defense, memory (spec-only), subscription, payment networks, aggregator platforms, restaurants, retail, commodity, subscription software, consumer brand, betting, insurance, pharma, AI infrastructure.
- Sub-sector (`усі субсектори`, ~80 values; same vocabulary as methodology page).
- Review (`будь-який перегляд`): "переглянув" (reviewed) · "частково" (partial) · "лише рушій" (engine only).
- Valuation basis (`будь-який базис`): NTM P/E · P/NTM OCF · P/NTM FCF · P/FFO.
- Known risks: "є відомі ризики" · "без відомих ризиків".
- Numeric text boxes: **"CAGR від, %"**, **"PEG до"**, **"доходність від, %"**, **"просадка від, %"** (min 5y CAGR, max PEG, min yield, min drawdown; validation not tested), and **"як у тікера"** (ticker search text).
- Level ceiling (`стеля будь-яка`): "стеля через перегляд" · "через прапорці" · "через борг" · "через моат".
- New only (`усі, не лише нові`): "став BUY за тиждень" (became BUY this week).
- Index membership (`лише реєстр Тараса` default): Nasdaq 100 · S&P 500.
- Flags (`прапорці будь-які`): "з критичним прапорцем".
- Matrix position (`будь-яке місце в матриці`): "у клітинці матриці" · "поза матрицею: ворота 0" · "вердикт змінили наступні кроки".
### Buttons
`скинути` (reset filters) · `скопіювати посилання` (copy shareable URL) · `CSV` (export table; NOT clicked — download).
### Column chooser ("Колонки", collapsible with checkboxes)
Вердикт · Бал · Ознаки · Ціна · Базис · Мультиплікатор · Ріст EPS NTM · PEG · Дохідність · Зміна оцінки · Дохідність за 5 років · Ризики · До наступного вердикту · Перегляд · Оцінка Тараса (all on by default except possibly the last).
### Sorting
Click a column header: first click = best -> worst, second = reverse (caption text); default sort `score` descending (URL `sort=score&dir=1`).
### Row action
☆ button at row start (add to watchlist; not clicked); ticker link -> `/t/<TICKER>/`.

## Outputs
- Counter top-right: `показано N з 164`.
- **Chart "Вердикти компаній / Вердикти всіх компаній"** (collapsible): horizontal bars, count per verdict: STRONG BUY 2 · BUY 10 · BUY WAIT 25 · AVOID 20 · ЛИШЕ СПЕКУЛЯЦІЯ 20 · НЕ МІЙ СЕКТОР 27 (green for STRONG BUY/BUY, brown BUY WAIT/SPEC ONLY, red AVOID, grey NOT MINE). Does not react to filters.
- **Table columns** (ordered): Компанія/назва (☆, logo, ticker link, name) · Вердикт (chip) · Бал (e.g. `A 91,0`, level letter + score) · Ознаки (`8 зелених, 0 невідомих з 10`) · Ціна (price word) · Базис (NTM P/E etc.) · Мультиплікатор (`19,1`) · Ріст EPS NTM (`+56,6 %`) · PEG (`0,34`) · Дохідність (FCF yield, `2,2 %`) · Зміна оцінки (quadrant or `н/д` = n/a) · Дохідність за 5 років, % на рік (`20,4 % / 21,7 %` = base / optimistic CAGR, subtext "вердикт тримає базовий" or "базовий нижче межі; оптимістичний у вердикт не входить") · Ризики (count + `N крит. · M серйоз.`) · До наступного вердикту (text on what would change the verdict, e.g. "price alone doesn't change it: in most companies of basket X ...") · Перегляд (`частково`/reviewed/engine only) · Оцінка Тараса (Taras's own score).
- **Pagination**: 100 rows per page; controls `← попередні`, `наступні →` and a `показати ще N` button (loads remaining N).
- Empty/missing values shown as `н/д`.
- Filtered example: verdict=BUY + level=B -> "показано 10 з 164" (ADSK first: B 81,5, справедлива ціна, NTM P/E 15,9, +8,3 %, PEG 1,93, yield 4,9 %).

## Business rules visible
Filters map 1:1 to engine attributes (verdict, level, price word, basis, flags, ceilings, matrix position). "Ceiling" = why the displayed level is lower than the score would give (review, flags, debt, moat).

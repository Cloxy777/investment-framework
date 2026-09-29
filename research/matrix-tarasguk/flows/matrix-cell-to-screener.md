# Flow: matrix cell -> company list -> screener with filters

1. `/start/` (or an index page): matrix loads ("Завантажуємо перелік компаній…" while data loads).
2. Click a cell (level row × price-word column). Page scrolls to a result block "Рівень B · справедлива ціна: 8 компаній": company tiles (logo, ticker, name, `level · score бала` + verdict chip).
3. Click a tile -> company card; or click **"Відкрити в скринері з цими фільтрами"** -> `/screener/#level=B&ціна=FAIR&…` (filters preselected, table sorted by score).
4. In screener: adjust filters (selects + "Ще 16 фільтрів" + numeric boxes), sort by clicking headers, hide/show columns, `скопіювати посилання` for a shareable URL, `CSV` to export.
5. Click ticker -> card.
Also: "Зараз у зоні BUY: 16" block -> "Усі 16 компаній зони BUY у скринері"; "Ідеї" page presets -> screener with preset hash.

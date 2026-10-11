# Screen: Earnings calendar ("Звіти" / Календар звітів компаній) — `/reports/`

Nav: Що нового -> Календар звітів. Captured 2026-09-29. Screenshots: `reports__top.jpg`, `reports__what-to-watch-open.jpg`.

## Purpose
Upcoming earnings-report dates for all covered companies, with the engine's verdict and "what to watch".

## Content
- Intro: report dates come only from the source and are shown with its caption; the source doesn't provide a "date confirmed" flag, so the date may shift — stated in each row.
- **Filter**: checkbox "лише мій вочліст (порожній)" (only my watchlist — currently empty) · button **"завантажити ICS"** (download calendar file; NOT clicked) · counter "показано 161 з 161".
- **Table grouped by month** (headings "вересень 2026", "жовтень 2026", …), columns: `Дата` (DD.MM.YYYY) · `Компанія` (ticker link + name) · `Рівень` (A–E) · `Вердикт` (chip text) · `Що дивиться`(button "що дивитись" toggles an inline row; button text becomes "згорнути").
- Expanded "what to watch" row: bullets — kill-lines (e.g. revenue growth below 10 %, guidance cut on revenue or margin, second consecutive drop of key KPI); fields missing now (e.g. guidance); source of date ("Financial Modeling Prep (FMP): analyst consensus; date per FMP earnings calendar, may shift").
- Rows sorted by date ascending; horizontally scrollable table region on narrow screens.

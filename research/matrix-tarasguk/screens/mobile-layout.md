# Mobile layout (390 px wide) — observed 2026-09-29

Method: window resize had no effect on the viewport, so pages were loaded in a **same-origin 390 px iframe** (media queries respond to iframe width; effective content width 375 px, no horizontal page scroll: scrollWidth 375). Screenshots: `mobile__start.jpg`, `mobile__menu-overlay.jpg`, `mobile__screener.jpg`, `mobile__company-card.jpg` (framed by a grey backdrop). Breakpoint value unknown (between 390 and ~1100 px).

## Global chrome
- **Banner** stays on top but text is truncated ("Закрите тестува… ▶ Подробиці про дані і доступ").
- **Header**: logo + three icon-only buttons: theme (sun), account (person; = "Кабінет" menu, label still available to screen readers), **hamburger "Меню"**. The 5 desktop nav items collapse into the hamburger.
- **Menu overlay** ("Меню", × close): full-height panel with section headings in small caps — З ЧОГО ПОЧАТИ (Перші кроки, Як читати картку), СКРИНЕР (Усі компанії, Порівняти компанії), ІНДЕКСИ (Nasdaq 100, **S&P 500 🔒** — lock icon; its accessible text says "у платному рівні" = in paid tier), ЩО НОВОГО (Що змінилось сьогодні, Підсумок тижня, Ідеї, Календар звітів), then bold "Портфель Тараса". The account menu items (Мій портфель/вочліст/сповіщення/доступ/Вийти) live in the account icon menu.
- **Search**: full-width pill, placeholder truncated ("Введіть тікер або назву ко…"), "Знайти" button inside; the `/` shortcut chip is hidden on touch width.

## Start page
- Matrix 5×5 kept as a grid (labels shrink; long labels e.g. "STRONG BUY / BUY" and "ЛИШЕ СПЕКУЛЯЦІЯ" use smaller font). Column headers wrap to two lines. **Cell counts change format from "N · переглянуто M" to "N / M"** (as the site text says: "on phone two numbers separated by slash"); empty cells still show "порожньо".

## Screener
- Table becomes a **card list**: each row = ☆ button, logo, ticker link, name, verdict chip at right; below, wrapped facts `A 91,0 · дешева ціна · NTM P/E 19,1 · EPS +56,6 %` / `PEG 0,34 · x2 20,4 % / 21,7 % · 8 зелених, 0 невідомих з 10` / `дохідність 2,2 % · зміна оцінки н/д · ризики 10 · переглянув`.
- Column-header sorting is replaced by a **select "Сортувати: Бал"** (options Тікер, Назва, Вердикт, Бал, …) and a direction button ("навпаки ↓").
- Primary filters (3 selects) wrap to two lines; "Ще 16 фільтрів" button full-width-ish; the "Вердикти компаній" bar chart is **collapsed by default** (toggle "+"); counter "показано 104 з 164" stays.

## Company card
- Header lines wrap (verdict, chips, "що означає" on its own line); action buttons wrap (`у вочліст`, `порівняти з …`, `зберегти PDF`); price strip wraps into a bordered box.
- **Tile grid is 2 columns** (was 3): each tile shows label + value; the "Оцінка" tile keeps its coloured left bar (green = fair/cheap).
- Mode switch and methodology link unchanged.

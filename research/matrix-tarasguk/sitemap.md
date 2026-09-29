# Sitemap — matrix.tarasguk.com

Site language: Ukrainian (UI labels kept in Ukrainian with English gloss). Site title "Матриця Тараса Гука" (Taras Huk's Matrix). Observed logged in (Кабінет menu shows "Вийти"); account details masked. Light/dark theme toggle exists.

Discovered 2026-09-29 from the global header on `/start/` (start page also reachable as `/`; "Перші кроки" links to `/`).

## Global chrome (every page, seen on /start/)
1. **Top banner** (grey strip): "Close testing. Company data from Financial Modeling Prep and SEC filings." + expander link "Подробиці про дані і доступ" (details about data and access).
2. **Header nav**
   | Menu | Item (UA) | Item (EN gloss) | href |
   |---|---|---|---|
   | logo "Матриця Тараса Гука" | — | home | `/` |
   | З чого почати | Перші кроки | First steps (= start page) | `/` |
   | | Як читати картку | How to read a card | `/how-to-read/` |
   | Скринер | Усі компанії | All companies (screener) | `/screener/` |
   | | Порівняти компанії | Compare companies | `/compare/` |
   | Індекси | Nasdaq 100 | | `/nasdaq100/` |
   | | S&P 500 (lock/crown icon => plan-restricted?) | | `/sp500/` |
   | Що нового | Що змінилось сьогодні | What changed today | `/changes/` |
   | | Підсумок тижня | Week summary | `/week/` |
   | | Ідеї | Ideas | `/ideas/` |
   | | Календар звітів | Earnings/report calendar | `/reports/` |
   | (link) | Портфель Тараса | Taras's portfolio | `/portfolio/` |
   | theme button | Тема: світла/темна | light/dark toggle | — |
   | Кабінет (account menu) | Мій портфель | My portfolio | `/my/` |
   | | Мій вочліст | My watchlist | `/watchlist/` |
   | | Сповіщення | Alerts/notifications | `/alerts/` |
   | | Мій доступ | My access (plan) | `/account/` |
   | | Вийти | Log out — NEVER click | (button) |
3. **Global search**: input "Введіть тікер або назву компанії, наприклад: NVDA, Apple, ASML" + "Знайти" button; hotkey hint `/` focuses the search. (Combobox, suggestions to be documented.)
4. **Floating widget** at right edge (3 small icons) — to identify.
5. **Footer / disclaimer**: "Not financial advice, do your own analysis, especially risk analysis."

## Other linked destinations (from start page body)
- Company card pages (click ticker) — URL pattern TBD (see screens/company-card.md)
- Methodology page ("Як рахує рушій: методологія") — URL TBD
- "Усі 16 компаній зони BUY у скринері" -> screener with a BUY filter
- "Підсумок тижня" / "Що змінилось сьогодні" links (week/changes)

## Connection graph (text)
```
/ (start) -> /how-to-read/ , /screener/ , /compare/ , /nasdaq100/ , /sp500/ ,
             /changes/ , /week/ , /ideas/ , /reports/ , /portfolio/ ,
             /my/ , /watchlist/ , /alerts/ , /account/ , company cards, methodology
every page -> global header + search
```

---
# Additions (2026-09-29, later exploration)

## Additional URLs discovered
| URL | Purpose | Doc |
|---|---|---|
| `/methodology/` (also `/methodology.html`, anchors like `#verdict-BUY`) | rule book | screens/methodology.md |
| `/t/<TICKER>/` (hash `#tile=<id>`: level, valuation, returns, ttm, fin_cashflow; portfolio page `#tile=pf-quality`) | company card | screens/company-card.md |
| `/screener/#…` filter hash keys: `verdict` (comma list), `level` (comma list), `ціна` (CHEAP,FAIR,…), `quadrant`, `dd_min`, `newbuy`, `sort`, `dir` | screener state | screens/screener.md |
| `/compare/#T1/T2/…` | compare set | screens/compare.md |
| `/access/` | sign-in (email code / invite code) | screens/access.md |
| `/how-to-enter/`, `/welcome/`, `/no-access/` | access help / landing | screens/auth-and-marketing-pages.md |
| `/privacy/` | privacy policy | screens/report-error-and-privacy.md |
| `/my/` (tab Портфель), `/watchlist/` (tab Вочліст), `/alerts/`, `/account/` | user area | screens/user-area.md |
| `/nasdaq100/`, `/sp500/` | indices | screens/indices.md |
| `/changes/`, `/week/`, `/ideas/`, `/reports/` | what's new | screens/changes-week.md, ideas.md, reports.md |

## Page-level components common to all pages
- Header: banner (data/access expander) + nav + search + theme + Кабінет; **footer** (present on non-card pages): "Data as of DD.MM.YYYY, next recalculation overnight, companies 546. Методологія · Як читати картку. Матриця Тараса Гука · matrix.tarasguk.com" + "Повідомити про помилку" form.
- Loading placeholders: "Відкриваємо дані для цієї сторінки…", "Відкриваємо картку…", "Завантажуємо перелік компаній…".
- Browser-persisted UI preferences: card mode (просто/детально), theme, watchlist, portfolio, alert preferences.

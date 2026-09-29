# Screens: user area — My portfolio `/my/`, My watchlist `/watchlist/`, Alerts `/alerts/`, My access `/account/`

Nav: header "Кабінет" menu (Мій портфель, Мій вочліст, Сповіщення, Мій доступ, Вийти). Captured 2026-09-29 in the invite-code test session (NOT an email account). Screenshots: `my-portfolio__empty.jpg`, `watchlist__empty.jpg`, `alerts__top.jpg`, `account__invite-access.jpg`. **Nothing was added, saved or submitted** (forms are local/browser-only but left untouched per view-only rule).

## `/my/` — Мій портфель (My portfolio) — tab "Портфель" (tab pair Портфель | Вочліст)
- Purpose: reader's own positions with share of each; shows verdict + level (from the public card) for each holding, reminds about position limits for readers, computes a total.
- Storage: **in the browser (localStorage-like), until accounts exist**; not visible to anyone, never used in verdict calculation; broker file import planned "after login".
- Inputs (row of controls): ticker combobox ("тікер або назва компанії", type-ahead from the 546 cards, must be one of our cards) · "частка, %" (share %) · "або кількість, шт." (or quantity) · button **"додати"** · button **"завантажити CSV"** (download/export or import — not tested). Validation/errors: not observed.
- Outputs: empty state "Поки порожньо. Додайте перший тікер: він має бути серед наших карток." · summary "Разом 0,0 % портфеля. Межі з наших налаштувань це порада читачеві, а не правило портфеля Тараса." (per-row limits from settings: position ≤10 % etc.). Rows with holdings NOT captured (would require adding data) — see open-questions.

## `/watchlist/` — Мій вочліст (My watchlist) — tab "Вочліст"
- Purpose: up to **20 tickers** followed: current verdict and level, and a mark for when a company enters the BUY zone. Star (★/☆) button in the screener and on cards adds a company.
- Storage: browser only; "in private mode it is empty and that's normal".
- Empty state text: "Вочліст порожній. Кнопка ★ на картці або в скринері додає компанію (до 20 тікерів)."
- Inputs: none on page (adds happen via ☆ buttons elsewhere). Limit 20 tickers.

## `/alerts/` — Сповіщення (Notifications)
- Purpose: choose e-mail/Telegram alerts for companies in your watchlist. **Feature not live**: "notifications are not sent yet; the screen and storage are ready, the channel connects together with accounts. What you choose now is saved in the browser and will move to the database with the account."
- Inputs: **Канал** select (`пошта` = email · `Telegram`); 4 checkboxes: (1) "вердикт картки змінився" (card verdict changed, e.g. BUY WAIT became BUY) — checked by default; (2) "ціна увійшла в зону BUY" (entry price taken from the card, not invented) — checked; (3) "зʼявився критичний прапорець" (critical flag appeared — the same flag that removes "good company" status) — checked; (4) "за два дні до звіту компанії" (two days before earnings; only for watchlist companies) — unchecked.
- Section **"Як це виглядатиме"** (what it will look like): a mock-up using real changes from the "Що змінилось" page.

## `/account/` — Мій доступ (My access)
- In invite-code session: shows only "Payment on the site only from an account: sign in with email first. Signing in with an invitation code does not open payment." + link **"Увійти поштою"** (-> `/access/`).
- For email accounts (not seen): expected subscription/club status, payment management (paid tier). Unknown.

---
# Addendum: filled states (tested 2026-09-29 with user's OK; test data added then removed)
Screenshots: `watchlist__filled-nvda.jpg`, `my-portfolio__filled-nvda-12pct.jpg`. After the test, browser storage was restored (keys removed; the card-mode preference I had set was also reset).

## Storage model (all browser-local, no server)
- `localStorage.watchlist` = JSON array of tickers, e.g. `["NVDA"]`. Max 20. "Stored in your browser, does not go to the server."
- `localStorage["matrix:portfolio"]` = JSON array of positions (ticker + share/quantity).
- `localStorage.cardmode` = `detail` (card просто/детально preference). Other stored: none seen. Cookie `matrix_access_until` (invite-access expiry) and a `visit` sessionStorage key.

## Watchlist — adding / removing
- Add: `☆` button in screener rows (class `watch`, becomes `★` with class `on`) — the card-header button "☆ у вочліст" did **not** toggle in my test (button label stayed "☆ у вочліст" and nothing was stored) — possible bug or click needed on a different hit-area; screener star worked. Remove: click `★` on `/watchlist/`.
- Filled `/watchlist/`: text "У вочлісті 1 з 20. Зберігаються у вашому браузері, на сервер не йде." Table columns: `Компанія` (★ toggle, ticker link, name) · `Вердикт` (chip) · `Бал` (`A · 91,0`) · `Ознаки` (`8 зелених, 0 невідомих з 10`) · `Ціна` (price word) · `Зміна` (valuation-change arrow + %, e.g. `↓ 26,5 %`) · `х2: базовий / оптимістичний` (`20,4 % / 21,7 %`) · `Оцінка Тараса` (`STRONG BUY 18.09.2026`). Note below: "BUY-zone entry notifications are a club feature; here the mark comes from our verdict changes over day and week."
- Empty again after removal: message "Вочліст порожній…".

## My portfolio — adding a position
- Form: ticker combobox (type-ahead shows `NVDA NVIDIA (Нвідіа)` — Ukrainian alias) -> selecting turns it into a chip `NVDA ×` (× removes); `частка, %` OR `або кількість, шт.`; button **"додати"**. Adding with ticker but no share/quantity: silently does nothing (no error text). After adding with share 12 the form resets.
- Result (share 12 % of NVDA): table `тікер | частка | рівень | вердикт | межа для читача | [прибрати]`:
  - row: `NVDA · 12,0 % · A · STRONG BUY · "до 10,0 % · вище межі" + "для вашої позиції: зменшити до межі"` (limit rule: level A/B ≤10 % per position; red share text when over limit); button **"прибрати"** removes the row.
  - **Portfolio KPI tiles** (same 5 as Taras's portfolio, computed on your holdings, "покрито 1 з 1"): Якість портфеля `A 91,0` · NTM P/E і PEG `19,1 · PEG 0,34` · CAGR 5 років `+20,4 % / +21,7 %` · Ріст EPS 5 років `+20,4 %` · Ріст виручки 12 міс. `+98,1 %`.
  - **Basket table** `кошик | частка | ліміт для читача`: "AI infrastructure with node monopoly · 12,0 % · basket has no limit, the 30 % limit is counted per sub-sector".
  - **Sub-sector table** `субсектор | частка | ліміт для читача`: "чіпи · 12,0 % · до 30,0 %".
  - Footer line: "Разом 12,0 % портфеля. Limits from our settings are advice to the reader, not Taras's portfolio rule."
- Not tested: `завантажити CSV` (labelled as broker-file upload/"download" — behaviour unclear), quantity-based entry, duplicates, >100 % or non-numeric shares (validation messages unknown).

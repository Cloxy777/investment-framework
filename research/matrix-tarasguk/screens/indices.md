# Screens: Indices — Nasdaq 100 (`/nasdaq100/`) and S&P 500 (`/sp500/`)

- Nav: Індекси -> Nasdaq 100 / S&P 500 (S&P 500 item has a small lock/crown icon => paid-tier marker). Captured 2026-09-29. Screenshots: `nasdaq100__top.jpg`, `sp500__top.jpg`.
- Same template for both pages.

## Purpose
Run the same engine over all constituents of an index and show the index-level matrix + a browsable constituent list.

## Content (top -> bottom)
1. **H1** index name.
2. **Intro paragraph**: "All N companies of the index are computed by the same engine as the rest of the cards. Taras did not review them, therefore level ≤ B and verdict ≤ BUY: it's a numbers-based rating, not his opinion. K of them were already in his registry and are marked separately: level A possible for those."
   - Nasdaq 100: "101 companies"; 40 already in registry. S&P 500: "500 companies"; 65 already in registry.
3. **Source line**: Nasdaq: `api.nasdaq.com, list nasdaq100, as of 19.09.2026`; S&P: `Financial Modeling Prep (FMP): S&P 500 composition, as of 23.09.2026`. "Cards not yet built for 1 company of the composition: listed below without numbers" (Nasdaq: 1; S&P: 1 — GOOGL).
4. **S&P 500 only – paywall block "Це в платному рівні" (This is in the paid tier)**: composition (ticker, name, sector) visible to all; level, price, verdict and other numbers for companies not in the testing set open on sign-in with an account. Link **"Увійти акаунтом або оформити підписку"** -> `/access/`. S&P 500 cards computed on FMP data only, open only when logged in with an account.
5. **"Матриця: де зараз компанії індексу"**: same 5×5 matrix component as start page but only index members (Nasdaq 100 sample: A-cheap 2/2, B-cheap 4/0, B-fair 6/2, B-exp+grow 7/1, B-exp-nogrow 4/0, C-cheap 1/0, C-fair 4/2, C-exp+grow 4/0, C-exp-nogrow 3/0, … ; banners "Outside matrix, gate 0: 48…", "Verdict changed by later steps: 3…"). Clickable cells like the start page.
6. **Scatter "Карта матриці: ціна і якість"** (S&P): X = sum of price lenses (−6…+8?), Y = quality score; guide lines A≥80, B≥70, C≥55; fair price ≥ +1; cheap ≥ +4. Dot colors: BUY/STRONG BUY green, BUY WAIT/SPEC ONLY brown, NOT MY SECTOR/NO DATA grey, AVOID red. Collapsible details.
7. Line "Без поточного мультиплікатора: 3" (3 companies with no current multiple).
8. Button "Усі 117 компаній індексу у скринері: сортування за будь-якою колонкою і фільтри" -> screener with index filter (`лише реєстр Тараса` select -> index).
9. **"Добірки в індексі"** (preset collections; probably links/buttons to filtered lists): "рівень B за справедливою або дешевою ціною (13)" · "просадка понад 30 % (30)" · "з критичним прапорцем (39)".
10. Note: "In the index: 500, with cards in this build: 117, shown 100 per page." **Constituent table** columns `Тікер | Назва | Сектор` (sector = basket name, e.g. "споживчий бренд", "фармацевтика", "страхування", "Платформи-агрегатори з мережевим ефектом"); pagination 100 per page. Ticker links to card when a card exists.

## Inputs
Matrix cells (buttons), collection buttons, screener CTA, pagination, login/subscribe link; no form fields.

## Business rules visible
- Non-reviewed index members capped: level ≤ B, verdict ≤ BUY (unless in Taras's registry -> A possible).
- Access tiers: composition public; full numbers for non-test-set S&P 500 companies require an account/subscription (see `/access/`).

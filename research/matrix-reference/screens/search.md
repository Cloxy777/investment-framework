# Screen/component: Global company search (header, every page)

Screenshots: `search__typeahead-asm.jpg`, `search__no-results.jpg`. Captured 2026-09-29.

## Inputs
- Combobox `type=search`, placeholder "Введіть тікер або назву компанії, наприклад: NVDA, Apple, ASML"; keyboard hint chip `/` (pressing `/` focuses the field); submit button **"Знайти"**; **×** clear button appears when text present.
- Free text; matches ticker, English name and **Ukrainian transliterated alias** (e.g. "ASML Holding (АСМЛ)", "Alphabet (Гугл)", "Meta Platforms (Мета)").

## Outputs
- **Type-ahead dropdown** (under field, updates as you type; shown after 1+ chars, "asm" already matched): each row = `TICKER  Company name (UA alias)  <basket description>  ·  <level letter>  ·  <verdict>` e.g. `ASML  ASML Holding (АСМЛ)  AI-інфраструктура з монополією на своєму вузлі · A · BUY WAIT`.
- **No match**: single line "нічого не знайшли: у нас 164 компанії" ("nothing found: we have 164 companies") — 164 = size of the current test set; footer elsewhere says 546 companies computed in total. Pressing Enter with no match stays on the same page (no navigation, no error page).
- Selecting a row / Enter with a match -> `/t/<TICKER>/` (not tested by click; behavior inferred).

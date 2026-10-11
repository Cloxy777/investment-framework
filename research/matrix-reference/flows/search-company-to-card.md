# Flow: search a company -> read its card

1. Any page: focus header search (click, or press `/`).
2. Type ticker/name (EN or UA alias, e.g. "asm", "Гугл"). Dropdown shows `TICKER Name (alias) basket · level · verdict`. No match -> "нічого не знайшли: у нас 164 компанії".
3. Choose a row (or Enter/"Знайти") -> `/t/<TICKER>/` ("Відкриваємо картку…" loading text).
4. Read the header: verdict, price word, level; check "Подробиці вердикту" reason; price strip -> "графіки" for 5y price, verdict history, price vs EPS, drawdown.
5. Mode "просто": open tiles (Gate 0, Level, Ten signs, Flags, Valuation, Valuation change, x2, TTM multiples, Next report); mode "детально": 8-step explanation.
6. Optional: `порівняти з …` -> `/compare/#TICKER/`; `☆ у вочліст` (adds to browser watchlist); `зберегти PDF`.
7. Bottom sections: financial breakdown tiles, "Детальні фінанси" (quarters), "Чого рушій не бачить", revenue geography, SEC events.
Deep-link variants: `/t/<T>/#tile=<id>`.

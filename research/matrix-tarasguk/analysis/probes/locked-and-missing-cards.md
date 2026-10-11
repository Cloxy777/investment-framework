# Probe: what a locked / missing card looks like
Raw: `data/raw/probe.locked-and-missing-cards.txt` (17 URLs).
- `/t/<any non-free ticker>/` (JPM XOM WMT UNH KO PEP HD CAT BA LLY NVDA.KS 005930.KS MU ASML SOFI) and unknown `ZZZZ` -> client redirect to `/paid-only/`, title "Це в платному рівні", text "Безкоштовно відкрита вітрина: двадцять компаній з вердиктом рушія і всіма механізмами. Решта компаній, портф[ель Тараса, ...]" + links "Повернутись до безкоштовної вітрини" (`/free/`) and "Відкрити платний рівень" (`/account/`). No distinction between a real paid ticker and a non-existent one.
- Lowercase `/t/nvda/` -> stays on `/free/t/nvda/`, title "Сторінку не знайдено".
- Paid-only routes: `/week/`, `/portfolio/`, `/alerts/`. Free routes: `/free/`, `how-to-read`, `screener`, `compare`, `nasdaq100`, `sp500`, `changes`, `ideas`, `reports`, `my`, `watchlist`, `account`, `access`, `methodology`, `privacy`, `no-access`, `welcome`, `how-to-enter`.

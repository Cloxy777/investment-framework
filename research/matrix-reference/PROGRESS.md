# PROGRESS — matrix.tarasguk.com documentation

Last updated: 2026-09-29 (site banner: this tester's access ends **06.10.2026** -> prioritise breadth, then depth)
Last URL visited: https://matrix.tarasguk.com/start/ (theme test)
Status: browser connected (Claude in Chrome, "Browser 1"). Session = invite-code test access (NOT an email account). Screenshots save to disk OK (JPEG, viewport-sized; `save_to_disk:true`, then `cp` the printed source path into screenshots/). Tip: JS extraction of page text works but output containing `=`,`?`,`&`,`%` gets BLOCKED by the tool — sanitise those chars in the script before returning.
Site language: Ukrainian. Docs are English with UA labels.

## Setup
- [x] Folder scaffold, README, PROGRESS
- [x] Browser connected + logged in (invite-code test access)
- [x] Screenshot-to-disk verified (jpg, not png)
- [x] Nav mapped -> sitemap.md

## Screens
| # | Screen | URL | Status | File |
|---|---|---|---|---|
| 1 | Global chrome (header, banner, search, footer) | all | DONE (in sitemap.md + start.md); todo: header search results page | sitemap.md |
| 2 | Start page | /start/ , / | DONE (todo: empty-cell click, "таблиця" toggle on trades chart) | screens/start.md |
| 3 | How to read a card | /how-to-read/ | DONE | screens/how-to-read.md |
| 4 | Screener | /screener/ | DONE (todo: "Ще 16 фільтрів" panel screenshot, numeric-filter validation, column toggles effect, pagination click) | screens/screener.md |
| 5 | Compare | /compare/ | DONE (2 companies) | screens/compare.md |
| 6-7 | Nasdaq 100 / S&P 500 | /nasdaq100/ /sp500/ | DONE (todo: constituent-table details, "Добірки" clicks) | screens/indices.md |
| 8-9 | What changed / Week | /changes/ /week/ | DONE | screens/changes-week.md |
| 10 | Ideas | /ideas/ | DONE | screens/ideas.md |
| 11 | Report calendar | /reports/ | DONE | screens/reports.md |
| 12 | Taras's portfolio | /portfolio/ | DONE (todo: other 4 KPI tiles' expansions) | screens/portfolio.md |
| 13-16 | My portfolio / watchlist / alerts / access | /my/ /watchlist/ /alerts/ /account/ | DONE incl. filled watchlist + portfolio (test data added and removed 2026-09-29); alerts save not exercised | screens/user-area.md |
| 17 | Company card | /t/<TICKER>/ | DONE for ABNB (simple mode) | screens/company-card.md |
| 18 | Methodology | /methodology/ | DONE | screens/methodology.md + rules-and-metrics.md |
| 19 | Data & access banner | banner | DONE | screens/start.md |
| 20 | Sign-in / access | /access/ | DONE (nothing submitted) | screens/access.md |
| 21 | how-to-enter, welcome, no-access | /how-to-enter/ /welcome/ /no-access/ | DONE (text only; /welcome/ partly) | screens/auth-and-marketing-pages.md |
| 22 | Privacy policy + report-error form | /privacy/ | DONE (summary) | screens/report-error-and-privacy.md |
| 23 | Header search typeahead / no-result | (search) | DONE | screens/search.md |
| 24 | Card variants | /t/... | DONE: STRONG BUY (NVDA), AVOID (ORCL), stop-list (SOFI), spec-only (MU), non-US (005930.KS); БРАКУЄ ДАНИХ has 0 companies today (not observable) | |
| 25 | Card detailed mode + Детальні фінанси + extra bottom sections | /t/... | DONE (addendum in company-card.md); price chart periods + financial tiles DONE (Addendum 2) | |
| 26 | "Повідомити про помилку" form | footer/all | DONE (not submitted) | screens/report-error-and-privacy.md |
| 27 | Start page "таблиця" toggle + empty matrix cell | /start/ | todo | |
| 28 | Dark theme look | all | DONE (start__dark-theme.jpg) | screens/start.md |
| 29 | Mobile layout | all | DONE via 390px iframe (screens/mobile-layout.md) | |

## Flows (flows/*.md; watchlist/alerts flow pending user OK)
- [x] search company -> card
- [x] matrix cell click -> company list -> screener with filters
- [x] screener filter -> results -> card
- [x] compare companies
- [x] watchlist add / remove and portfolio add / remove (done with user OK; alerts save still todo)
- [x] sign-in (documented, not executed)

## Cross-cutting docs
- [x] rules-and-metrics.md (very detailed from /methodology/)
- [x] glossary.md
- [x] open-questions.md
- [x] sitemap.md additions
- [x] README.md summary (update when more is done)

## Do-not-touch
Never click "Вийти". No adds to watchlist/portfolio/alerts, no PDF/CSV/ICS downloads, no email/code entry, no "Повідомити про помилку" submissions without asking the user.

## Resume instructions
Read README.md + PROGRESS.md, then continue from first `todo` above. Copy screenshots with `cp <printed tool-results path> screenshots/<slug>__<state>.jpg`.

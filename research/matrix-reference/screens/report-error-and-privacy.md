# Components: "Повідомити про помилку" (report an error) and Privacy page

Captured 2026-09-29. Screenshot: `report-error__form.jpg`. **Form opened but NOT submitted.**

## Report-error form (footer button on every page)
- Trigger: footer button **"Повідомити про помилку"**; toggles to **"Згорнути"** once open; form expands inline under the footer (not a modal).
- Title "Що не так на цій сторінці" (What's wrong on this page). Intro: describe in a few words what you saw; page address is added automatically (shown as `Сторінка: <current URL>`).
- Fields:
  | Field | Type | Required | Limits/placeholder |
  |---|---|---|---|
  | Що не так (what's wrong) | textarea | yes (implied) | placeholder "e.g. the verdict row says one thing and the tile says another"; **max 1000 chars**, live counter "0 / 1000" |
  | Пошта (необов'язково) | email input, placeholder "ваша@пошта.com" | optional | note: without email the report still arrives, but no reply |
  | hidden field labelled "Не заповнюйте це поле" | text | must stay empty | honeypot anti-spam |
- Button **"Надіслати"** (submit). Success/error messages: not observed.
- Also used on the login page as the channel to request a new invitation code or report a missing payment.

## `/privacy/` — Політика конфіденційності
Long legal page (text only, not screenshotted). Content summary (paraphrased; personal identifiers of the site operator intentionally not recorded here): states who is the data controller and how to contact them (requests answered within 30 calendar days); the project name/IP belong to Taras; site collects a minimum — account sign-in, club-member access, site emails, abuse protection; data stored: email, IP, user agent, time and text of consent (for waiting list) etc.; explains purposes and deletion rights. Remaining sections not read in detail.

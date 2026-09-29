# Screen: Sign-in / access ("Вхід") — `/access/`

- Reached from: S&P 500 paywall link "Увійти акаунтом або оформити підписку"; probably also from Кабінет -> Мій доступ. Captured 2026-09-29. Screenshot: `access__login.jpg`. **No data was entered on this page.**
- **Important context**: the tester session is a "test access" (invite-code based): page says "You are currently in test access. Sign in with email to see your subscription and club access." The Кабінет menu is visible, but the user is not signed in with an email account.

## Purpose
Passwordless sign-in for paying club members and testers; explains club/subscription link.

## Inputs
| Field | Type | Required | Notes |
|---|---|---|---|
| Пошта (email) | `email` input, placeholder "імʼя@пошта.com" | yes | user enters email -> button **"Надіслати код"** (send code). No password: "we send a code; account is needed so access and payment stay with you, not the browser" |
| Collapsible "Маю код запрошення на тестування" (I have a test invitation code) | text input, placeholder format `ABCD-EFGH-JKMN` (3 groups of 4, letters without ambiguous chars) + button **"Увійти"** | conditional | link "У мене немає коду" -> `/no-access/` |
Validation/error texts: not observed (nothing submitted).

## Links
- "Ви в клубі? Як увійти поштою, з якої оплачуєте клуб" -> `/how-to-enter/` (club members: use the email used for payment).
- "На сторінку запрошення" -> `/welcome/` (invitation landing).
- "Політика конфіденційності" -> `/privacy/`.
- Footer: data-as-of + universe count (546 companies), Методологія, Як читати картку, "Повідомити про помилку".

## Business rules
- Access model: (1) invite-code test access (this tester; ends 06.10.2026 per banner), (2) email-code login for paying club members / subscribers ("club" = Taras's community; payments outside this site).
- Paid tier gating seen on: S&P 500 page (non-test-set companies), AI аналітика tile on cards (🔒).

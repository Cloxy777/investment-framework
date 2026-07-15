# NEW POSITION — PYPL (PayPal Holdings, Inc.) — 2026-07-15

**Task type:** NEW POSITION (Rule 9 re-check of an existing not-in-portfolio watchlist entry)
**Date:** 15 Jul 2026
**Trigger:** Telegram scan (Routine 6) — tarasguk #11387 (~10:39 UTC): "Stripe пропонує викупити PayPal по $60 за акцію" (Stripe proposes to buy PayPal at $60/share); corroborated by FinnInvestChannel #2935 (~12:04 UTC): "Stripe хочу купити PayPal і бути гігантом" (Stripe wants to acquire PayPal and become a giant). Per Rule 0/CLAUDE.md, neither post's text is used as financial data — both are treated only as a prompt to independently verify live price and news.
**Prior watchlist entry:** [PYPL-2026-06-14.md](../watchlist/not-in-portfolio/PYPL/PYPL-2026-06-14.md) — Phase 01 **FAIL** (Revenue CAGR 3yr 6.46% vs >8–10% required), price $41.24 at that time.
**Current PYPL portfolio weight:** 0% — not held ([holdings.md](../portfolio/holdings.md))
**Sector:** Financial Technology — Digital Payments

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$56.13** | IBKR `get_price_snapshot` (contract 199169591, NASDAQ), last trade, not halted |
| Prior close | $47.37 | IBKR `get_price_snapshot` |
| **Change** | **+$8.76 / +18.49%** intraday | IBKR `get_price_snapshot` |
| Bid/ask | $56.11 / $56.19 | IBKR `get_price_snapshot` |
| Volume (intraday, at fetch time) | ~11.3M shares | IBKR `get_price_snapshot` |
| 52-week range | $38.34 – $79.08 | IBKR `misc_statistics` |

**This +18.49% move on its own is a Rule 9 trigger** ("a >15% stock-price move with no identified cause") — except the cause *is* identified (§2), so this session treats it as one combined M&A/price-move Rule 9 event, not two separate ones.

---

## 2. Independent News Verification (Rule 0 — never trust the Telegram post text itself)

WebSearch corroboration, multiple independent outlets, all reporting the same core facts:

- **Reuters** (via [CNBC](https://www.cnbc.com/2026/07/15/stripe-advent-offer-to-buy-paypal-for-more-than-53-billion-reuters.html), [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-15/stripe-advent-offer-to-buy-paypal-for-53-billion-reuters-says), [US News](https://money.usnews.com/investing/news/articles/2026-07-14/exclusive-stripe-advent-offer-to-buy-paypal-for-more-than-53-billion-sources-say)): Stripe and private-equity firm Advent International have made an **unsolicited joint proposal to acquire PayPal at $60.50/share** (~28% premium to Tuesday's close), valuing the deal at **>$53 billion**, with ~$50B in bank financing commitments reportedly lined up. Stripe/Advent would each hold a 50% stake if the deal closes.
- **Status: proposal only, not a signed/accepted deal.** As of this session, PayPal has not confirmed or responded publicly; Stripe and Advent reportedly aim to finalize *an agreement* (not a completed deal) by end of month. No 8-K or joint press release from PayPal itself was found confirming acceptance.
- The Telegram-reported "$60" figure is a rounded version of the reported $60.50/share figure — directionally correct, not exact; this session uses only the independently-verified $60.50 figure as context, not as scored data (the framework has no valuation input for an unconfirmed take-out price).
- PayPal's own live price ($56.13, +18.49%) is consistent with the market pricing in real deal-completion risk against the reported $60.50 offer (a ~7% spread to the reported offer price is a normal risk-arb discount for an unconfirmed, unsigned proposal).

**Sources:** [CNBC](https://www.cnbc.com/2026/07/15/stripe-advent-offer-to-buy-paypal-for-more-than-53-billion-reuters.html) · [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-15/stripe-advent-offer-to-buy-paypal-for-53-billion-reuters-says) · [US News](https://money.usnews.com/investing/news/articles/2026-07-14/exclusive-stripe-advent-offer-to-buy-paypal-for-more-than-53-billion-sources-say) · [GuruFocus](https://www.gurufocus.com/news/8959057/stripe-and-advent-international-propose-6050-per-share-acquisition-of-paypal)

---

## 3. Has Anything the Phase 01 Gate Scores Actually Changed?

WebSearch confirms **PayPal has not yet reported Q2 2026 earnings** — consensus/company-guided date is **28 Jul–4 Aug 2026**, i.e. still ~2 weeks out from this session. No new 10-Q/8-K has been filed since the 5 May 2026 Q1 2026 release already incorporated into the 2026-06-14 evaluation.

This means **every Phase 01 input (TTM revenue, TTM net income, margins, ROIC, balance sheet, buyback pattern) is unchanged** from the prior session — an M&A proposal is not a fundamental-financial-statement event, and this framework does not re-estimate financials off a takeover rumor (Rule 0: never invent or estimate).

| Check | PYPL Value (unchanged since 2026-06-14) | Threshold | Result |
|---|---|---|---|
| Net margin | TTM 14.97% / FY2025 15.75% | >15% / >12% pre-screen | ✅ PASS (FY basis) |
| ROIC | ~21–24% | >15% | ✅ PASS |
| **Revenue CAGR 3yr** | **6.46%** | **>10% (strategy.md) / >8% (pre-screen)** | ❌ **FAIL** |
| Gross margin | 41.5%, expanding 2yr | >40% or expanding | ✅ PASS |
| FCF positive 3yr | FY2023–25 all positive | required | ✅ PASS |
| Net debt/EBITDA | Net cash (~−$1.9B) | <2–4x | ✅ PASS |
| FCF/NI conversion 2yr | 160.2% / 107.1% | >70% | ✅ PASS |
| Share issuance | Net buybacks | not dilutive | ✅ PASS |

**Gate result: FAIL — unchanged from 2026-06-14, on the same single criterion (Revenue CAGR 3yr).** Per the operating brief, this session stops here; Phase 02 valuation scoring is not run (and would not be meaningful against an unconfirmed takeover price in any case — this framework has no merger-arbitrage/deal-spread scoring mechanism).

---

## 4. Recommendation

# **WATCHLIST ONLY — no position, no order setup. Phase 01 gate still fails; the M&A proposal is real but outside this framework's mandate.**

PayPal is genuinely the subject of a credible, multi-outlet-reported **$60.50/share, >$53B unsolicited joint acquisition proposal from Stripe and Advent International**, and the live price (+18.49% to $56.13) confirms the market is pricing this as real, pending deal-completion risk. That is a legitimate Rule 9 event and this session's independent verification (§2) treats it as such — but:

1. **This framework is a quality-value long-term fundamental framework, not a merger-arbitrage strategy.** It has no scoring mechanism for "buy the spread to an unconfirmed takeover price," and this session does not invent one.
2. **The Phase 01 quality gate — the only thing this session's data can actually move — is unchanged**, because no new fundamental (earnings, guidance, financials) has been released since 2026-06-14. The gate still fails on Revenue CAGR 3yr (6.46%), for the same reasons documented in that entry.
3. If the deal is confirmed/signed at or near $60.50, that is a corporate action (cash-out merger) for existing PYPL shareholders to evaluate under their own broker's process — not something this framework scores or recommends a new entry into at a price close to the reported deal terms (little to no margin of safety left even if the deal closes, and full downside back toward $47–48 if it falls through).

**No order recommendation, no broker action.** Flagging for the user: if you want to evaluate whether to speculatively enter the deal spread as a distinct trade idea, that would need to go through the **speculation module** ([speculation-module.md](../framework/speculation-module.md)) as a separate, explicitly-gated satellite-sleeve decision — not this core-framework new-position path — since it is not a quality/growth thesis but a binary deal-completion bet.

---

## 5. Next Review Trigger

**Date/event:** PayPal's Q2 2026 earnings release (expected 28 Jul–4 Aug 2026) — re-run Phase 01 with refreshed TTM Revenue CAGR 3yr. **Separately**, a confirmed/signed merger agreement, a rejection of the proposal, or a further >15% unexplained move from $56.13 (Rule 9) would each warrant an immediate ad hoc re-check regardless of the earnings calendar.

**No position opened — nothing to log in `decisions/`.**

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this entry:

| Term | Meaning |
|---|---|
| **Composite Score** | This framework's blended Quality + Valuation ranking number; not computed this session — Phase 01 gate failed before Phase 02 valuation scoring would apply. |
| **FCF (Free Cash Flow) / NI (Net Income) conversion** | FCF ÷ Net Income — how much of accounting profit actually shows up as cash; PYPL's is 160.2% (FY2024) and 107.1% (FY2025), both well above the >70% quality bar. |
| **M&A** | Mergers & Acquisitions — one company buying or combining with another; the Stripe/Advent proposal for PayPal is an M&A event under Rule 9. |
| **Net Debt/EBITDA** | A leverage ratio measuring years of cash profit needed to pay off all debt; PayPal is net cash (negative), passing trivially. |
| **Phase 01–06** | The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit. This session stops at Phase 01 (screening/quality gate). |
| **Quality Score** | This framework's 0.0–100.0 continuous quality grade; not computed this session since the underlying Phase 01 pass/fail gate (a precondition) still fails on Revenue CAGR. |
| **ROIC (Return on Invested Capital)** | How efficiently a company turns invested capital into profit; PayPal's is ~21–24%, well above the >15% bar. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price (and never trust a secondary source's text as financial data) before any valuation work. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, material M&A, macro shifts, or a >15% unexplained price move — two of which (M&A proposal, +18.49% price move) fired together this session. |
| **Speculation module** | A separate, smaller satellite sleeve for short-horizon speculative trades, gated by the same 80.0+ Quality Score bar as the core framework — the appropriate (but separate) place to evaluate a deal-spread trade idea, not this core new-position path. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results; unchanged since the 2026-06-14 entry because PayPal has not yet reported Q2 2026 earnings. |

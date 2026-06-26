# NEW POSITION (re-run) — WSE (Wise Group plc) — 2026-06-26

**Trigger:** Telegram post [t.me/bolshegold/9628](https://t.me/bolshegold/9628), posted 2026-06-25 20:54:10 UTC, reporting Wise's first post-Nasdaq-listing quarterly/FY2026 results (revenue $2.5B +19% YoY, 21% client growth, cross-border volume +31%, income before tax $660.4M at a 26% margin, a new $500M buyback). This is the exact mandatory trigger named in the prior watchlist entry ([watchlist/not-in-portfolio/WSE/WSE-2026-06-21.md](../watchlist/not-in-portfolio/WSE/WSE-2026-06-21.md)): *"Mandatory — Wise FY2026 results, expected 2026-06-25... for Rule 9 re-score and to see whether the AML investigation is resolved/escalated."*

**Rule 0 compliance:** No figure from the Telegram post text was used as a financial input anywhere below. Price was pulled fresh from Interactive Brokers and cross-checked against a second source. Fundamentals were pulled fresh and independently from Wise Group plc's audited SEC Form 20-F (FY2026, filed since the company's primary listing moved to Nasdaq) — **not** from `yfinance`, which remains structurally blocked in this environment (see §1 data-quality note), and **not** from the Telegram post or the press release that accompanied it.

---

## 1. Data-quality note — yfinance unavailable, fallback to primary filing

`yfinance` failed with the same `SSLError` (`curl_cffi` browser-TLS-impersonation rejected by this environment's policy-enforcing proxy) previously documented for AAPL in `portfolio/snapshots/telegram-watch.md`. Plain `curl`/`requests` reach Yahoo's price endpoint (200 OK) but Yahoo's `quoteSummary` fundamentals endpoint 401s ("Invalid Crumb") even via plain `requests` — fundamentals are categorically unavailable through Yahoo in this environment right now, not just for this ticker.

Rather than logging this as an unresolvable data gap, fundamentals were instead pulled directly from Wise Group plc's **Form 20-F** for the fiscal year ended 31 March 2026, filed with the SEC ([accession 0001193125-26-282911](https://www.sec.gov/Archives/edgar/data/0002099039/000119312526282911/d17323d20f.htm)) — a primary audited regulatory filing, consistent with Rule 0 and with the prior WSE session's own precedent of using company disclosures (WebSearch-sourced "own cash" figure, AML detail) when `yfinance`'s structured fields were missing or distorted. This is judged a *stronger* source than the press release that accompanied the Telegram post, which lacked balance sheet, cash flow, EPS, and AML-status detail entirely.

**Continuity note:** Wise Group plc is a newly reorganized holding company (Scheme of Arrangement completed 2026-05-08, Nasdaq primary listing 2026-05-11) that now reports in **USD** under **US GAAP**, replacing the prior entity's GBP/IFRS reporting. The 20-F provides 3 fiscal years of income-statement/cash-flow comparatives (FY2024–FY2026) and 2 years of balance-sheet comparatives (FY2025–FY2026) — one year short of the prior session's 4-year GBP dataset. This is flagged as a data-continuity note, not a blocking gap: the 2-year revenue CAGR available here (see §3) clears the Phase 01 threshold by a wide enough margin that splicing in the prior session's older GBP-translated figures isn't required to reach a conclusion.

---

## 2. Live price (Rule 0 — fetched first, cross-checked)

| Source | Value |
|---|---|
| Interactive Brokers (live snapshot, NASDAQ:WSE, contract 881566839) | **$11.60** last trade, bid $11.61 / ask $11.89, volume **200 shares** (thin), change +4.88% vs. prior close |
| Cross-check (WebSearch aggregator, same-day) | Day's range ~$10.90–$11.66, intraday move consistent with a post-earnings pop |
| 52-week range (IBKR) | $10.36–$17.47 |

**$11.60** is used throughout. Flagging explicitly: today's IBKR print traded on only 200 shares — thin enough that a single odd-lot print could be noisy — but it sits inside the cross-checked aggregator range for the day, so it is used as-is per Rule 0 rather than substituted with a guess about a "fairer" price. This is +7.0% from the prior session's $10.84 (2026-06-21), consistent with a market reaction to the FY2026 print and the new buyback announcement.

**Shares outstanding:** 1,025,164,562 Class A + 204,338,749 Class B = **1,229,503,311** (most recent count disclosed in the 20-F, as of May 31, 2026 — used over the March 31, 2026 fiscal-year-end count of 1,234,555,520 because it's more current and still a primary-sourced, not estimated, figure).

**Market cap** = 1,229,503,311 × $11.60 = **$14,262.2M**

---

## 3. Financials — extracted from Form 20-F (USD millions, FY ended March 31)

### Income Statement

| | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Net revenue | 1,776.1 | 2,098.9 | 2,502.8 |
| Transaction expense | (331.5) | (378.0) | (513.6) |
| Transaction and credit losses | (15.7) | (11.6) | (13.9) |
| Technology and development | (287.6) | (314.1) | (434.3) |
| Servicing | (216.9) | (287.5) | (396.6) |
| Marketing and sales | (79.6) | (106.1) | (171.8) |
| General and administrative | (194.7) | (273.4) | (381.9) |
| **Total operating expenses** | (1,126.0) | (1,370.7) | (1,912.1) |
| **Operating income** | 650.1 | 728.2 | 590.7 |
| Other income/(loss), net | 6.6 | (10.7) | 69.7 |
| **Income before tax** | 656.7 | 717.5 | 660.4 |
| Income tax expense | (155.2) | (167.2) | (161.7) |
| **Net income** | 501.5 | 550.3 | 498.7 |
| EPS basic (¢) | 48.57 | 53.31 | 48.92 |
| Weighted avg shares basic (M) | 1,032.6 | 1,032.3 | 1,019.5 |

### Balance Sheet (2-yr comparative only, as filed)

| | FY2025 | FY2026 |
|---|---|---|
| Cash and cash equivalents | 18,066.3 | 27,802.2 |
| Available-for-sale debt securities | 6,013.6 | 4,582.7 |
| Total assets | 24,781.1 | 33,259.8 |
| Funds payable and amounts due to customers | 22,279.9 | 30,254.2 |
| Short-term debt | 128.4 | 6.0 |
| Long-term debt | 0.0 | 328.7 |
| Total liabilities | 23,043.7 | 31,334.6 |
| Total shareholders' equity | 1,737.4 | 1,925.2 |

### Cash Flow Statement

| | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Net income | 501.5 | 550.3 | 498.7 |
| D&A | 14.3 | 9.7 | 14.4 |
| Δ Funds payable/due to customers (float swing) | 3,571.5 | 5,138.4 | 6,999.7 |
| **Net cash from operating activities** | 4,075.1 | 5,719.5 | 7,553.9 |
| Purchase of PP&E | (13.4) | (44.1) | (19.6) |
| Purchase of intangible assets | (3.0) | (1.2) | (1.8) |
| Repurchases of shares | (86.2) | (92.5) | (473.4) |

---

## 4. Data-quality corrections (same character of fix as the prior WSE session)

**(a) Customer float distorts OCF.** The "Funds payable and amounts due to customers" working-capital swing ($6,999.7M in FY2026) is segregated client money in transit, not company-generated cash — it's 93% of the $7,553.9M raw operating cash flow figure. Using the raw OCF/FCF would overstate FCF yield by roughly an order of magnitude, exactly the error the prior session flagged.

> Adjusted OCF = OCF − customer float swing
> Adjusted FCF = Adjusted OCF − CapEx (PP&E + intangibles)

| | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Adjusted OCF | 503.6 | 581.1 | 554.2 |
| CapEx | 16.4 | 45.3 | 21.4 |
| **Adjusted FCF** | **487.2** | **535.8** | **532.8** |

Cross-check against the prior session's GBP figures (£362.6M FY2025 Adjusted FCF, FX-translated) is reasonable given the reporting-currency change.

**(b) Gross balance-sheet cash conflates customer float with Wise's own cash.**

> Own cash = Cash & equivalents + AFS debt securities − Funds payable/due to customers
> FY2025: 18,066.3 + 6,013.6 − 22,279.9 = **$1,800.0M**
> FY2026: 27,802.2 + 4,582.7 − 30,254.2 = **$2,130.7M**

Cross-checks reasonably against the prior session's £1.4B own-cash figure once the reporting-currency change and five-quarter gap are accounted for.

> Total debt FY2026 = $6.0M (ST) + $328.7M (LT) = $334.7M
> **Net debt FY2026 = $334.7M − $2,130.7M = −$1,796.0M (net cash)**

---

## 5. Phase 01 — Quality Gate

Using `valuation-scoring.md`'s Quantitative Pre-Screen Filters (the documented governing threshold set):

| Check | WSE Value (FY2026, on corrected basis) | Threshold | Result |
|---|---|---|---|
| Gross margin | 78.9% (Net revenue − Transaction expense − Transaction/credit losses; no "gross profit" subtotal is presented in the 20-F, so this uses the direct-cost-of-service line items as the COGS proxy — see note below) | >40% | ✅ PASS |
| Net margin | 19.92% (down from 26.22% FY25, 28.24% FY24) | >12% | ✅ PASS — but **margin compression flagged**, see §6 |
| ROIC (NOPAT/Invested Capital) | 19.72% (down from ~29.9% FY25 on the same methodology) | >15% | ✅ PASS — same compression flag |
| Revenue growth (CAGR) | 18.72% (2yr CAGR, FY24→FY26 — only 3 FY of USD data exist post-reorganization, see §1) | >8% | ✅ PASS |
| FCF positive 3 consecutive years | Adjusted FCF positive all 3 years ($487.2M / $535.8M / $532.8M) | required | ✅ PASS |
| Net debt/EBITDA | Net cash (−$1,796.0M FY26, own-cash-corrected) | <2.5× | ✅ PASS |
| **FCF yield** | Adj. FCF $532.8M / Market Cap $14,262.2M = **3.74%** | >4% | ❌ **FAIL** |
| **EV/EBIT** | EV = $14,262.2M + $334.7M debt − $2,130.7M own cash = $12,466.2M; EBIT (Operating income) = $590.7M; **21.11×** | <20× | ❌ **FAIL** |

**Note on gross margin methodology:** the 20-F doesn't present a "gross profit" subtotal (unlike the prior session's `yfinance`-sourced 72.4% FY25 figure, which used Yahoo's own cost classification under the old GBP/IFRS presentation). Using "Transaction expense + Transaction and credit losses" as the direct cost-of-service proxy gives 78.9–81.4% across FY24–26; even the broader alternative of also including "Servicing" costs as COGS gives 63.1–68.2% — either way, comfortably clears the 40% gate, so the exact definition doesn't change the gate outcome.

### Gate result: **FAIL — 6 of 8 criteria pass.**

Per `new-position.md` step 2 ("Walk the Phase 01 quality gate — if it fails, stop and report why rather than proceeding to scoring"), **this session stops here and does not proceed to the full Phase 02 valuation-scoring engine.** No Rate Environment Gate run, no DCF/comparables fair-value triangulation, no Upside/Downside Modifier, no order setup — none of that work is meaningful once the entry-eligibility gate itself has failed.

**Why this matters, and why it's a real result and not a rounding artifact:** five days ago (2026-06-21), WSE passed this same gate 8/8, including FCF yield (4.43%) and EV/EBIT (12.01–12.07×) by comfortable-to-narrow margins. Both of those same two filters have now flipped to FAIL. The mechanism is visible directly in the data pulled this session:

1. **Price rose** (+7.0%, $10.84 → $11.60) on what the market read as a good print and a new buyback.
2. **But EBIT and Adjusted FCF both went the other way.** Operating income fell **18.9%** YoY ($728.2M → $590.7M) and Adjusted FCF fell **0.6%** YoY ($535.8M → $532.8M, on a currency/restatement-adjusted view), because operating expenses grew **39.5%** YoY ($1,370.7M → $1,912.1M) against 19.2% revenue growth — Technology & development +38%, Servicing +38%, Marketing & sales +62%, G&A +40%, all materially outpacing revenue.
3. A higher price divided by a *lower* EBIT/FCF mechanically pushes EV/EBIT and 1/FCF-yield up by more than the price move alone would suggest — which is exactly what happened (EV/EBIT roughly 12× → 21×).

This is the opposite of what the Telegram post's framing implied. The post highlighted revenue growth, client growth, cross-border volume growth, and the buyback — all real and independently confirmed in the 20-F — but did not mention that operating income fell 18.9% and net income fell 9.4% YoY, or that net margin compressed from 26.2% to 19.9%. Read together with the price reaction, the independently-verified fundamentals say WSE got *more* expensive on the two multiples this framework gates on, not less — a direct example of why Rule 0 (never trust the post's framing, always re-derive) exists.

---

## 6. AML investigation status — independently confirmed from the 20-F

The prior session's "Next review trigger" explicitly required determining whether the Belgian AML investigation was resolved or escalated. The 20-F's own Legal Proceedings disclosure (Item 8.A), independently located and read in full for this session:

> *"In June 2026, the media reported on an ongoing money laundering inquiry by the Brussels prosecutor's office relating to Wise Europe SA, which we discussed further in our Form 6-K on June 1, 2026. The inquiry is incomplete, with no known timeline or outcome."*

**Status: still open, neither resolved nor escalated to formal charges.** This independently confirms (from Wise's own primary regulatory disclosure, not from the Telegram post's claim) that there is no AML update in either direction this period. The investigation remains a live, unresolved risk overhang exactly as it was on 2026-06-21.

Separately, Note 22 (Subsequent Events) confirms the $500M share purchase program announced 2026-06-25 (~40% via the recurring employee-share-trust purchase program) — independently verifying that part of the Telegram post's claim as well, from the primary filing rather than the post text.

---

## 7. Other prior-entry review triggers — resolved this session

- **"Confirmation over 2+ more periods of whether revenue growth is genuinely decelerating"** — **No.** Revenue growth was 18.18% (FY24→25) and 19.24% (FY25→26) — modestly *accelerating*, not decelerating.
- **">15% unexplained price move from $10.84"** — Price moved +7.0% to $11.60; below the 15% trigger threshold, and the move is explained by the earnings/buyback reaction rather than unexplained.
- **PEG/Fast-Grower (Upgrade 3) eligibility** — still not applicable, now on stronger grounds than before: EPS actually *declined* FY25→26 (53.31¢ → 48.92¢, −8.2%), so the "EPS growth >15% for 3+ years" Fast-Grower bar is not just unproven (as in the prior session) but actively failing this period. Moot in any case, since the gate failed before Phase 02 weighting would matter.
- **Management change / guidance revision** — none disclosed in Note 22 (Subsequent Events) or elsewhere reviewed in the 20-F.

For reference only (Phase 02 wasn't run, so this isn't part of the score): the 10Y US Treasury yield is ~4.38–4.45% as of 2026-06-25, which would have placed the Rate Regime Modifier in the +5 bracket (3.5–5%) had a score been computed.

---

## 8. Recommendation

**WATCHLIST ONLY — do not enter.** No change to the action category from the prior entry, but the underlying picture has moved in the *wrong* direction, not the right one: the Phase 01 quality gate that previously passed 8/8 (if narrowly, on the same two filters) now fails 6/8, specifically on the two valuation-multiple filters (FCF yield, EV/EBIT), driven by a post-earnings price pop landing on top of operating-margin compression rather than improvement. The AML overhang remains open and unresolved. No order setup is produced — there is no valuation score to size a position against, and the gate itself says this isn't presently a quality-value entry candidate at this price/fundamentals combination.

---

## 9. Next review trigger

- **Mandatory:** any AML investigation update in either direction (Brussels prosecutor's office inquiry resolution, formal charges, or regulatory clearance).
- A pullback in price and/or a recovery in operating margin that would mechanically bring FCF yield back above 4% and/or EV/EBIT back below 20× (re-clearing the Phase 01 gate) — re-run `/new-position` at that point.
- Standard Rule 9 triggers: next earnings report, guidance revision, management change.
- >15% unexplained price move from $11.60.

---

## Glossary

- **AML (Anti-Money Laundering):** laws and internal controls against moving criminal proceeds through legitimate financial channels; an AML investigation is a regulator/prosecutor probe into whether a company's controls failed.
- **CAGR:** Compound Annual Growth Rate — the smoothed yearly growth rate between a start and end value.
- **CapEx:** Capital Expenditure — money spent on physical/long-lived assets.
- **D&A:** Depreciation & Amortization — non-cash expense spreading asset costs over time.
- **EBIT:** Earnings Before Interest and Taxes — operating profit.
- **EPS:** Earnings Per Share — net income ÷ shares outstanding.
- **EV (Enterprise Value):** market cap + debt − cash; a company's total value to all capital providers.
- **EV/EBIT:** Enterprise Value ÷ EBIT — how expensive a company is relative to its operating profit, independent of capital structure.
- **FCF (Free Cash Flow) / FCF Yield:** cash generated after running/maintaining the business; FCF ÷ market cap.
- **FCF/NI conversion ratio:** FCF ÷ Net Income — checks whether reported profit is turning into real cash.
- **Form 20-F:** the annual report non-US companies listed in the US file with the SEC — the international equivalent of a Form 10-K; a primary audited disclosure.
- **Form 6-K:** a report foreign private issuers furnish to the SEC between annual 20-F filings for material news — roughly the international equivalent of an 8-K.
- **Net Debt/EBITDA:** net debt ÷ EBITDA — a leverage ratio; this framework's primary balance-sheet-risk gate.
- **NOPAT:** EBIT × (1 − effective tax rate) — the numerator used to compute ROIC.
- **Own cash:** a payments company's own deployable corporate cash, distinct from customer/client balances it holds in transit.
- **Phase 01 (Quality Gate):** this framework's pre-screen filter set that a company must pass before a valuation score is computed.
- **PEG ratio:** PE ratio ÷ earnings growth rate.
- **pp (percentage points):** a direct difference between two percentages.
- **Rate Regime Modifier:** an additive adjustment to the valuation score based on where the 10-Year Treasury yield sits.
- **ROIC:** Return on Invested Capital — NOPAT ÷ (debt + equity); a core quality signal.
- **Safeguarded/segregated customer funds:** money a regulated payments company holds for customers in transit, ring-fenced from its own cash — must be stripped out before computing FCF yield, EV, or Net Debt/EBITDA.
- **Treasury yield (10Y):** the interest rate on US 10-year government bonds; the risk-free-rate benchmark for the Rate Environment Gate.

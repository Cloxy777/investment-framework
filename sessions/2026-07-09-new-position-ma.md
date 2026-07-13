# NEW POSITION (watchlist refresh) — MA (Mastercard Incorporated) — 2026-07-09

**Task type:** NEW POSITION (not-in-portfolio watchlist refresh — Quality Score / Composite Score addition only, per explicit scope)
**Date:** 2026-07-09 (Thursday — US markets open, intraday)
**10Y US Treasury Yield:** 4.58% (WebSearch: TradingEconomics, 2026-07-09 intraday print — 4.581%. Not used to recompute anything this session; cited for context only. Still inside the "3.5–5%" bracket that produced the +5 Step 2 modifier baked into the existing 38.0 Valuation Score, so the Rate Regime Modifier is unchanged.)
**Last review on record:** MA **38.0** (2026-06-22, BUY — Standard position 3–5%, but trade gated — R/R 1.33:1 <2:1) — [watchlist/not-in-portfolio/MA/MA-2026-06-22.md](../watchlist/not-in-portfolio/MA/MA-2026-06-22.md), [session](2026-06-22-rescore-ma.md). Computed under the **current** (2026-06-20) Upside/Downside Modifier methodology — **not stale on that count**. Flagged stale **only** for missing the Quality Score / Composite Score added 2026-06-29 — see [watchlist/STALE.md](../watchlist/STALE.md).
**Current MA portfolio weight:** 0% — **not held** (absent from [holdings.md](../portfolio/holdings.md)). This is the not-in-portfolio watchlist-maintenance use of `/new-position`.
**Sector:** Payment network (duopoly with Visa) — asset-light financial
**Purpose of this session:** per explicit scope — MA already has a **current** Valuation Score (38.0, computed under the 2026-06-20 methodology) and cleared Phase 01 cleanly (net margin 45.8%, ROIC ~95%, all 9 criteria) in its prior sessions. This session (1) checks for a Rule 9 trigger since 2026-06-22, (2) if none, computes MA's **first-ever Quality Score** under the 2026-06-29 engine, (3) blends it with the existing 38.0 Valuation Score into the Composite Score, and (4) re-verifies the R/R gate conclusion at today's live price. The Valuation Score itself is **not** recomputed this session (no Rule 9 trigger found — see §2).

> *Jargon decoded on first use — see closing Glossary section.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$520.05** | IBKR `get_price_snapshot` (contract_id 38685693, NYSE — resolved via `search_contracts`), `last` field, intraday 2026-07-09. Cross-checked against `stockanalysis.com` (WebFetch), which independently read **$519.82** at "Jul 9, 2026, 2:38 PM EDT — Market open" — a $0.23 (0.04%) gap, consistent with normal quote-timing noise between two independently-polled sources, not a data-quality concern. **Used the IBKR figure** as the primary broker-sourced quote, consistent with this framework's Rule 0 preference order. |
| ⚠️ Tooling note | `yfinance` (the fallback used in the 2026-06-22 MA session, when IBKR's `get_price_snapshot` had returned an "OAuth Service Unavailable" 503) failed this session with a `curl_cffi` TLS/connection-reset error before returning any data — IBKR was available and used directly instead, so no fallback was needed. |
| 52-week range | $464.58 – $598.78 (IBKR `misc_statistics`) | Live price sits ~11.9% above the 52-week low and ~13.1% below the 52-week high — comfortably inside the range, not at either extreme. |
| Intraday change | +$1.06 (+0.20%) | IBKR `change` field |
| Bid/Ask | $519.92 / $520.15 | IBKR `bid_ask` |
| Price vs. 2026-06-22 review ($489.79) | **+6.18%** | Well under the 15% Rule 9 "unexplained move" threshold — see §2. |

---

## 2. Rule 9 Trigger Check (2026-06-22 → 2026-07-09)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | **No** | Q2 2026 results confirmed for **Thursday, 30 July 2026, after close** (Mastercard investor-relations conference-call announcement, businesswire, stocktitan) — **not yet reported** as of today. Not a trigger this session. |
| Guidance revision | **No** | The only "Q2 guidance at the low end of low double digits" / cross-border-travel-deceleration-from-Middle-East-conflict commentary found in web coverage traces back to CFO Sachin Mehra's remarks at the **JPMorgan 54th Annual Global TMC Conference on 19 May 2026** — a date that **predates** the 06-22 review, not a fresh disclosure this window. (One secondary aggregator mischaracterized this as a "1 Jul 2026 call" and a "Q2 2026 earnings call on 23 Jul 2026" — both checked directly against Mastercard's own investor-relations page and the official conference-call announcement, which confirm the Q2 print is 30 Jul 2026 and no earnings/guidance event occurred 1 Jul or 23 Jul; treated as a search-summarization error, not used.) Full-year 2026 guidance (currency-neutral net revenue growth at the "high end of the low-double-digit to low-teens range") is unchanged from what the 06-22 session already used as its intrinsic-growth input. |
| Management change | **No (predates window)** | The CFO/C-suite reorganization (Ling Hai succeeding Sachin Mehra as CFO; Linda Kirkpatrick, Demi Dosis, Craig Vosburg, Raj Seshadri all moving roles) was **announced 2 June 2026**, effective 3 August 2026 — before the 06-22 review, not new this window. CEO Michael Miebach unchanged. KBW called it a "constructive reorganization... no impact to full-year guidance" at the time. |
| M&A | **No (still pending, unchanged)** | The BVNK stablecoin-infrastructure acquisition (~$1.8B, announced 17 March 2026) remains **pending regulatory approval**, expected to close **late 2026** — not yet closed, no new disclosure since 06-22. |
| Macro shift | **No** | 10Y Treasury moved 4.451% (06-22) → 4.58% (07-09) — still inside the "3.5–5%" bracket; no Rate Regime Modifier bracket change. |
| >15% unexplained price move | **No** | +6.18% since 06-22 (§1) — well under the 15% threshold, and not "unexplained" regardless (broad market/sector drift, no company-specific shock identified). |
| Other company-specific events checked | **No trigger** | A federal judge granted **preliminary** approval to the revised $38B Visa/Mastercard swipe-fee antitrust settlement on **10 June 2026** — before the 06-22 review, not new. Revised scam-merchant-monitoring standards and enhanced crypto-transaction classification standards take effect **24 July 2026** (routine network-rules updates, not a fundamental/valuation trigger). |

**Conclusion: no Rule 9 trigger fired.** This is a routine, scheduled watchlist refresh — the substantive finding is the **first-ever MA Quality Score computation** (§4) and the resulting Composite Score (§5), independent of any Rule 9 event, which materially changes the operative action-table input (see §6–7). Per scope, the **Valuation Score is not recomputed** this session — the existing 38.0 (2026-06-22, current 2026-06-20 methodology) is reused as-is.

---

## 3. Governance Flag (found incidentally, not part of this session's scope to resolve)

**[holdings.md](../portfolio/holdings.md)'s 2026-07-05 sync note flags a live, unauthorized IBKR order still open on MA:** order ID 862563682, BUY 4 shares @ $464.00 LIMIT, GTC, placed 2026-07-05 — which **directly contradicts** the 2026-06-22 session's explicit "Trade does NOT execute" finding (R/R 1.33:1, below the 2:1 minimum), and per holdings.md has in fact been live under different order IDs since 2026-06-16, silently re-issued. This session's own R/R re-verification (§7) reaches the same "does not clear 2:1" conclusion at today's price and fair value, reinforcing that this order should not be left to fill as-is. **Resolving or cancelling it is outside this command's scope** (no MCP tool in this repo can cancel an order — that is `/update-orders`' and the user's own TWS/Client Portal job) — flagged here for visibility and carried into §8's next-review-trigger list.

---

## 4. MA — Quality Score (first-ever computation, 2026-06-29 methodology)

Inputs are the same TTM period (ended 31 March 2026) already sourced and cross-checked in the [2026-06-22 rescore](2026-06-22-rescore-ma.md) — no new quarter has reported since, so these are **carried forward, not re-invented**, per that session's own citations (Mastercard 8-K/10-Q filings, SEC EDGAR). ROIC is recomputed below using the NOPAT ÷ Invested-Capital convention this framework's 2026-07 batch has standardized on (V, MSFT, NOW sessions) rather than the 06-14 session's stockanalysis.com-sourced 94.92% figure (different, unstated methodology) — flagged transparently; it does not change the scoring outcome either way (§4a).

**Hard disqualifier check (all must pass before the weighted score matters):**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs unexplained? | FY2022–2025: 101.7% / 97.3% / 105.5% / 109.8%; TTM 109.66% — all comfortably ≥70% every year | disqualify if <70% for 2+ yrs *without* explanation | ✅ PASS, comfortably |
| Net Debt/EBITDA over threshold? | **0.531×** (standard 2.5× or 4× asset-light-override threshold — both cleared with enormous headroom) | disqualify if over applicable threshold | ✅ PASS, comfortably |
| FCF-positive 3+ consecutive years? | FCF-positive and growing every year on record (FY2022–2025 and TTM) | disqualify if not | ✅ PASS |

No hard disqualifier triggers. Proceeding to the weighted score.

### 4a. Profitability (25% weight)

```
Net Margin (TTM)     = $15,570M / $33,939M = 45.88%
NetMargin_Component  = clamp((45.88/30)×100, 0, 100) = clamp(152.9, 0, 100) = 100.0
```

**ROIC — recomputed this session on the NOPAT/Invested-Capital convention** (Total Debt + Stockholders' Equity, period-end 2026-03-31, consistent with the V/MSFT/NOW 2026-07-05 sessions):
```
TTM Pretax Income = $19,359M; TTM Tax Provision = $3,789M → TTM effective tax rate = 19.57%
                    (stockanalysis.com quarterly income-statement data, Q2'25–Q1'26)
NOPAT             = TTM EBIT × (1 − tax rate) = $19,655M × (1 − 0.1957) = $15,808.5M
Total Debt (2026-03-31) = $18,960M; Stockholders' Equity (2026-03-31) = $6,722M (stockanalysis.com)
Invested Capital  = $18,960M + $6,722M = $25,682M
ROIC (TTM)        = $15,808.5M / $25,682M = 61.56%
ROIC_Component    = clamp((61.56/30)×100, 0, 100) = clamp(205.2, 0, 100) = 100.0
```
*(For the record: the 2026-06-14 session's stockanalysis.com-sourced ROIC of 94.92% uses an unstated/different methodology — likely a return-on-equity-flavored measure inflated by MA's very small buyback-shrunk equity base. Both readings are far above the 30% ceiling this sub-score saturates at, so the discrepancy is immaterial to the Quality Score here — flagged for consistency awareness, not resolved further.)*

```
Profitability_Score = (100.0 + 100.0) / 2 = 100.0   (no FCF cap — FCF-positive and growing every year on record)
```

### 4b. Margins (15% weight)

Gross-margin proxy = operating margin (payment networks report ~100% "gross margin" per data aggregators due to a revenue-recognition quirk with no traditional COGS line — the same treatment used consistently since MA's 2026-06-14 session):
```
Operating Margin (TTM, GAAP "Total Operating Income As Reported") = $19,655M / $33,939M = 57.91%
GrossMargin_Score = clamp((57.91/80)×100, 0, 100) = clamp(72.39, 0, 100) = 72.39
```
No structural-trend bonus applicable — already well above the 40% threshold the bonus targets.

### 4c. Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 → FY2025) = 13.82%
Growth_Score = clamp((13.82/25)×100, 0, 100) = 55.28
```
**+10 (documented TAM expansion / pricing power, cited):**
- **Value-Added Services and Solutions (VAS)** net revenue grew **22% (18% currency-neutral)** in Q1 2026, with the increase "driven primarily by growth in our underlying key drivers, our security solutions, digital and authentication solutions, business and market insights and consumer acquisition and engagement services, **and pricing**" — verbatim from Mastercard's Q1 2026 8-K earnings release. A genuine new-TAM, pricing-power-evidencing revenue line growing faster than the core network-toll business.
- **MA's own revenue 3yr CAGR (13.82%, FY2022→FY2025) outpaces Visa's over the identical window (10.921%, FY2022→FY2025 — this repo's [2026-07-05 V session](2026-07-05-rescore-v.md))** — direct, same-window, same-repo evidence MA is gaining share *within* the Visa/Mastercard duopoly specifically, not merely riding overall payments-industry growth.
- The pending BVNK stablecoin-infrastructure acquisition (still closing, §2) represents a further TAM-expansion vector once it closes, cited directionally only (not yet closed, not counted as realized evidence).

**No structural-deceleration evidence found.** The one growth headwind identified in research (Middle East conflict compressing cross-border/travel volumes, flagged by CFO Mehra at the 19 May 2026 JPMorgan conference — see §2) was explicitly characterized by management as **cyclical/geopolitical**, "most pronounced in Q2" with "progressive recovery in Q3 and Q4," and **full-year guidance was maintained**, not cut — this does not meet the Growth sub-score's "documented evidence growth is decelerating *structurally* (not cyclically)" bar for a −10. No penalty applies.

```
Growth_Score (with bonus) = clamp(55.28 + 10, 0, 100) = 65.28
```

### 4d. Balance Sheet (15% weight)

```
Net Debt/EBITDA (TTM) = $11,054M / $20,822M = 0.531×
```
**Asset-light override (Upgrade 5) applies** — Mastercard is a payment network, effectively 100% of its debt is financial (senior notes), interest coverage is 26.17× (far above the 15× threshold), and it carries an investment-grade rating (Aa3 Moody's / A+ S&P, both stable — per the 4 June 2026 SEC FWP filing already cited in the 2026-06-22 session, carried forward here, not re-verified this session). Using the /6 denominator:
```
BalanceSheet_Score = clamp(100×(1 − 0.531/6), 0, 100) = clamp(91.15, 0, 100) = 91.15
```
(For reference, the standard /4 denominator would give 86.73 — the override adds ~4.4 points; either way the score is high, since Net Debt/EBITDA is far below both thresholds.)

### 4e. Moat Signal (15% weight) — checklist, cited evidence per signal

| Signal | Marked | Cited evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | Mastercard holds **26% of US credit-card purchase volume** vs. Visa's 61% (Capital One Shopping market-share research, updated 3 June 2026) — a stable #2 duopoly position, not eroding (no share-loss evidence found in any source checked). **Growing:** MA's own revenue 3yr CAGR (13.82%) outpaces Visa's over the identical FY2022→FY2025 window (10.921%, this repo's 2026-07-05 V session) — direct evidence of MA gaining ground within the duopoly, not just riding market growth. |
| Brand premium (pricing power) | **TRUE** | Mastercard's Q1 2026 8-K explicitly cites "**pricing**" as one of the drivers of VAS net revenue growth (+22%/+18% CC) alongside underlying volume/key-driver growth — see §4c. Price increases contributing to a fast-growing, high-margin revenue line without disclosed volume loss is direct evidence of pricing power. |
| Network effect | **TRUE** | Textbook two-sided network, documented in Mastercard's own 10-K business description: the four-party model (issuer, acquirer, merchant, cardholder) where MA "switches more than 70% of all transactions for Mastercard and Maestro-branded cards, including nearly all cross-border transactions" — each additional merchant/issuer increases the network's value to every existing participant. Mechanism is documented, not merely asserted. |
| Switching costs | **FALSE** | Checked directly against Mastercard's own FY2025 10-K risk factors (Item 1A): the company explicitly discloses "**loss of substantial business from significant customers, competitor relationships with our customers**" as a material risk, and — per the pricing/incentive structure disclosed in the same filings — Mastercard's rebates and incentives paid to customers to retain and win volume **grew 16% in FY2025 (to $20,522M) and 23% YoY in Q1 2026 (19% currency-neutral)**, outpacing total net revenue growth (16%/12% CC) in the same period. Customer relationships are documented as largely non-exclusive, with the company itself flagging it must **increase** incentives to stay competitive — the opposite of a documented lock-in mechanism. Marked FALSE on this cited evidence, consistent with the rigor applied to V's own FALSE "Scale cost advantage" signal in the 2026-07-05 session. |
| Scale cost advantage | **TRUE** | Mastercard's operating margin (~59.9–60.8%, per Mastercard's own FY2025 adjusted-margin disclosure and independent July 2026 coverage) is dramatically wider than American Express's (~17.4–21.2% EBIT/operating margin, same sources) — Yahoo Finance/24-7 Wall St, 2 July 2026, attributing the gap to Mastercard's asset-light, "toll booth" open-loop network model (massive fixed-infrastructure cost spread over enormous transaction volume) versus Amex's closed-loop, capital-intensive issuer-plus-lender model. A direct cost-structure/margin gap vs. a named smaller competitor. |

```
Moat_Score = (4/5) × 100 = 80.0
```

**Sensitivity check (shown transparently, "no black box"):** if "Switching costs" were instead credited TRUE (5/5 = 100.0), the Quality Score would move to **87.6**; if "Scale cost advantage" were instead credited FALSE alongside it (3/5 = 60.0), the Quality Score would fall to **81.6** — even under this more conservative reading, **the gate result does not flip**: MA clears 80.0+ either way.

### 4f. FCF Quality (10% weight)

```
FCF/NI (TTM) = $17,074M / $15,570M = 109.66%
FCFQuality_Score = clamp(((1.0966 − 0.40)/0.60)×100, 0, 100) = clamp(116.1, 0, 100) = 100.0
```

### 4g. Quality Score — Final

```
Quality Score = (100.0×0.25) + (72.39×0.15) + (65.28×0.20) + (91.15×0.15) + (80.0×0.15) + (100.0×0.10)
              = 25.000 + 10.8585 + 13.056 + 13.6725 + 12.000 + 10.000
              = 84.587 → rounds to 84.6
```

# Quality Score = 84.6 — PASSES the 80.0+ gate (comfortably, and robust to the moat-signal sensitivity check above).

**This is MA's first-ever computed Quality Score, and it passes.** Per the established practice for a **passing** Quality Score (mirroring V, NVDA, AVGO in this same 2026-07 batch): the Composite Score below is **fully adopted**, not a reference-only/"false green light" number — there is no quality-gate concern gating the action recommendation here.

---

## 5. MA — Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 84.6) + 0.50 × 38.0
                = 0.50 × 15.4 + 19.0
                = 7.7 + 19.0
                = 26.7
```

| | Value |
|---|---|
| Valuation Score (2026-06-22, current 06-20 methodology, reused unchanged — §2) | 38.0 |
| Quality Score (first-ever, this session) | 84.6 (PASSES 80.0+ gate) |
| **Composite Score** | **26.7** |

**Composite Score = 26.7 → falls in the 0.0–29.9 "Very Cheap" band** (nominal Full position, 6–8%) — **one full band more attractive than the raw Valuation Score's own "Cheap" band** (30.0–49.9, Standard position 3–5%). MA's high, comfortably-passing Quality Score (84.6) genuinely earns extra credit in the blend here, rather than laundering a gate failure — per the task's nuance rule, there is no reason to discount this number. **Not boundary-sensitive:** 26.7 sits 3.2 points inside the Very Cheap band, and even the moat-signal sensitivity check's worst case (Quality 81.6 → Composite 27.2) stays inside the same band.

---

## 6. MA — Action Table Read

**Composite Score 26.7 → nominal action: BUY — Full position (6–8% of portfolio), per the current Action Table (0.0–29.9 band).**

Per the operating brief, the full order setup is re-run below using the Composite-Score-implied band's Margin-of-Safety/Stop parameters (0.0–29.9 → MoS 15–20%, Max Loss 20–25% — [fair-value-methodology.md](../framework/fair-value-methodology.md)), not the 06-22 session's own 30.0–49.9-band parameters (25%/25%), since the Composite Score — not the raw Valuation Score — now governs the Phase 03 action table once a company is quality-scored (see [valuation-scoring.md](../framework/valuation-scoring.md) "Composite Score" section). The **Blended Fair Value itself is unchanged** ($640.67, the PW Fair Value from the 06-22 session's Upside/Downside Modifier scenario work) — only the MoS/Stop percentages the score band selects have changed, since the Valuation Score (and the fair-value scenario architecture behind it) is not being recomputed this session (§2).

---

## 7. Order Setup & R/R Gate Re-verification

```
Blended Fair Value (= PW FV, carried forward from 2026-06-22, unchanged): $640.67
PRIMARY SELL TARGET (= Blended FV):                                        $640.67
BULL-CASE TRIM TARGET (bull × 0.90, carried forward): $740.33 × 0.90 =    $666.30
```

**Full applicable range (0.0–29.9 band: MoS 15–20%, Max Loss 20–25%) — structural identity, same form documented in the 06-22 MA and 2026-07-05 V/AVGO sessions:**
```
R/R = MoS / [(1 − MoS) × MaxLoss%]
Max R/R  (MoS=20%, MaxLoss=20%): 0.20 / (0.80×0.20) = 0.20/0.16 = 1.25:1
Min R/R  (MoS=15%, MaxLoss=25%): 0.15 / (0.85×0.25) = 0.15/0.2125 = 0.71:1
```
**R/R ranges 0.71:1 – 1.25:1 across the entire applicable band — fails the 2:1 minimum throughout, at every combination.** (Notably *worse* than the 06-22 session's own 30.0–49.9-band R/R of 1.33:1 — a tighter MoS band mechanically compresses the achievable R/R further under this identity, an intrinsic property of the framework's math worth flagging, not something to "fix" here.)

**Concrete check at the conservative end of the band (MoS 20%, Max Loss 25% — mirrors the convention used in the 2026-07-05 V session):**
```
BUY PRICE (limit)     = $640.67 × (1 − 0.20)              = $512.54
STOP LOSS              = $512.54 × (1 − 0.25)              = $384.40
R/R at formal entry    = ($640.67 − $512.54) / ($512.54 − $384.40) = $128.13 / $128.13 = 1.00:1   ❌ below 2:1
R/R at live price ($520.05) = ($640.67 − $520.05) / ($520.05 − $384.40) = $120.62 / $135.65 = 0.89:1   ❌ far below 2:1
```

**Per fair-value-methodology.md Step 6 ("Below 2:1 = do not enter... wait for lower entry, find tighter stop, or pass on the trade entirely"): R/R fails the minimum threshold across the entire applicable Composite-band MoS/Stop range. No order should be placed.**

**The 2026-06-22 session's R/R gate conclusion still holds** — in fact the gate reads *more clearly* fails-worthy under the Composite-Score-selected band than it did under the raw-Valuation-Score band. This directly reinforces §3's governance flag: the live unauthorized BUY order (4 sh @ $464.00) sits below even the tightest computed buy price in this band ($512.54 at 20% MoS), so it is not simply "early" relative to a documented entry — it does not correspond to any officially computed buy price under either the 06-22 or this session's parameters, and the underlying R/R math argues against entering at all at current fair-value inputs.

**Net: WATCHLIST ONLY — do not enter.** MA is not held (0% weight); no position exists to hold or trim. The Composite Score (26.7, "Very Cheap") is a **more attractive score** than the raw Valuation Score (38.0, "Cheap") once quality is folded in — but, as with V and AVGO in this same batch, a favorable score band does not automatically mean an executable trade: the R/R gate independently blocks entry regardless of which side of any band boundary the score falls on.

---

## 8. Next Review Trigger

- **Routine:** MA's Q2 2026 earnings release, confirmed **30 July 2026, after close** — will refresh every TTM fundamental used here and is the next scheduled full Valuation Score recompute (per the 2026-06-22 session's own next-review note).
- **Watch (highest priority): the R/R gate.** If price pulls back toward the ~$512–545 buy-price range (or the fair-value/PW-FV inputs move favorably at the next earnings print) without a fundamental deterioration, re-run the order setup — R/R could clear 2:1 well before the next scheduled earnings-driven rescore.
- **Governance item (§3, unresolved, flagged not fixed):** the live, unauthorized BUY order (862563682, 4 sh @ $464.00 GTC) that contradicts this framework's own "do not enter" finding — needs the user's attention in TWS/Client Portal directly (no tool in this repo can cancel it), or resolution via `/safe-guard`/`/update-orders`.
- **Rule 9 triggers (standing):** any guidance revision, management change, the BVNK acquisition closing (a material M&A completion event), a 10Y Treasury decline below 3.5% (Step 2 modifier would drop +5 → 0), a >15% unexplained price move from $520.05, or the 30 Jul 2026 earnings print itself.

---

## Glossary

| Term | Meaning |
|---|---|
| **10-K (Annual Report)** | The annual SEC financial-disclosure filing, including audited statements and risk factors — this session's source for MA's Moat Signal "Switching costs" evidence (Item 1A Risk Factors). |
| **BVNK** | A stablecoin-infrastructure startup Mastercard agreed to acquire (~$1.8B, announced March 2026) — still pending regulatory approval, expected to close late 2026. |
| **CAGR** | Compound Annual Growth Rate. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate. **Fully adopted for MA this session** (84.6 Quality Score passes the gate cleanly; Composite = 26.7). |
| **Cross-border (payments/volume)** | Transactions between a cardholder and merchant in different countries — a growth/margin-sensitive segment flagged as softening cyclically (Middle East conflict) but not structurally this session. |
| **D&A** | Depreciation & Amortization. |
| **Debt Gate** | This framework's balance-sheet check on Net Debt/EBITDA (Hybrid Upgrade 5) — standard threshold <2.5×, relaxed to <4× for asset-light payment networks/exchanges with strong interest coverage and investment-grade ratings. Applied to MA (a payment network) again this session. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT — not recomputed this session (Valuation Score reused unchanged). |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years on a clean earnings base — MA's existing Fast Grower classification (from the 06-22 session) is unaffected this session. |
| **Form 8-K** | A US company's "current report" filed with the SEC to disclose a material event between its regular quarterly/annual filings — this session's primary source for MA's Q1 2026 VAS revenue-growth driver language and for confirming Rule 9 trigger timing. |
| **FWP (Free Writing Prospectus)** | An SEC filing type used here (4 June 2026) as the source for MA's credit ratings, carried forward unchanged. |
| **GTC (Good-Til-Cancelled)** | An order type that remains active until filled or manually cancelled — the type of the flagged unauthorized MA buy order in §3. |
| **Hard disqualifier** | A Quality Score condition (FCF/NI conversion, Net Debt/EBITDA, FCF-positivity) that fails a company regardless of weighted score. |
| **Interest coverage (ratio)** | EBIT ÷ interest expense — how many times over a company can pay its interest from operating profit; part of the asset-light Debt Gate override test. |
| **Invested Capital** | The total capital (debt + equity) put to work in a business — the denominator of ROIC, recomputed this session on the NOPAT/Invested-Capital convention. |
| **Investment grade** | A credit rating (Aa3/A+ for MA) indicating a low-risk borrower, a requirement for the asset-light Debt Gate override. |
| **Moat** | A durable competitive advantage protecting a business's profits — this framework's Quality Score grades it as a 5-signal checklist (§4e). |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **Net Margin** | Net Income ÷ Revenue. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **PW (Probability-Weighted) Fair Value** | This framework's blended fair value — 25% bull + 50% base + 25% bear — carried forward unchanged from the 06-22 session ($640.67). |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. MA's first-ever computation this session: **84.6 — passes the gate**. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss on a trade; this framework requires ≥2:1 to enter — MA fails this at every point in the applicable band this session. |
| **Rate Regime Modifier** | The additive ±10 score adjustment based on the current 10-Year Treasury yield band — unchanged this session (still +5, 3.5–5% bracket). |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital; recomputed this session on the standardized convention (§4a). |
| **Rule 0 / Rule 9** | This framework's standing instructions to always fetch a live price first, and to force re-valuation only on specific documented fundamental triggers (earnings, guidance, M&A, management change, macro shift, >15% unexplained move). |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results — unchanged this session (same period as the 06-22 session, since no new quarter has reported). |
| **VAS (Value-Added Services and Solutions)** | Mastercard's non-core-network product line (fraud/risk tools, tokenization, advisory, issuing/acceptance support) — its fastest-growing revenue segment and the cited evidence for this session's Growth and Brand-premium sub-score findings. |

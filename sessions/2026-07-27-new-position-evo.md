# NEW POSITION (RE-EVALUATION) — EVO (Evolution AB, Stockholm-listed; traded here via EVVTY, OTC Pink ADR) — 2026-07-27

**Task type:** NEW POSITION re-run (Telegram-scan trigger, Routine 6 — unattended run)
**Date:** 27 Jul 2026 (Monday; US market not yet open at time of data pull — see §1)
**10Y US Treasury Yield:** 4.67% (WebSearch, Friday 2026-07-24 close — most recent available read)
**Rate Regime Modifier:** +5 (10Y in the 3.5–5% bracket, unchanged)
**Current EVO/EVVTY portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** [EVO-2026-07-24.md](../watchlist/not-in-portfolio/EVO/EVO-2026-07-24.md) / [2026-07-24 session](2026-07-24-new-position-evo.md) — Quality Score 81.6 (PASS, marginal), Valuation Score 0.0, Composite 9.2 ("Very Cheap"), **R/R 1.29:1 — FAILED the 2:1 minimum**, watchlist only.
**Sector:** Consumer Discretionary — Gambling/Gaming B2B (live-dealer casino & digital table-game solutions for licensed online operators)
**Filer type:** Swedish primary listing (Nasdaq Stockholm, IFRS reporting, EUR-denominated financials); traded on this account via the unsponsored US OTC Pink ADR **EVVTY** (1:1 ratio).
**First-use jargon decode:** see closing Glossary (§9).

---

## 0. Why this session exists — trigger source

A Telegram post today (`bolshegold/9837`, edited, ~07:55 UTC, 2026-07-27) discussed a Swiss/Swedish-style "mandatory bid at the highest price paid in the last 6 months" situation, naming only an investor nicknamed "Дарт" (Dart) — no ticker was spelled out in the post text itself. The immediately preceding two posts in the same channel (`bolshegold/9835`, `bolshegold/9836`, both ~05:12 UTC, forwarded from "NotLocal") carried the hashtag `#EVVTY` and an unlabelled photo, forming one continuous narrative with `/9837`. Per Rule 0, **a Telegram post's text is never used as financial data, and a ticker is never guessed** — so this identification was independently corroborated via WebSearch before any action was taken:

**Independently verified (WebSearch, not from the post):**
- **Candle Lake Limited** (the investment vehicle of **Kenneth Dart**) disclosed on **24 July 2026** that its stake in **Evolution AB** had crossed **~30.02%** of voting rights — the threshold that triggers a **mandatory takeover offer obligation** under **Chapter 3, Section 1 of the Swedish Act on Public Takeovers** (Sweden, not Switzerland — the post's "Швейция"/Switzerland framing is the poster's own imprecision, not something this framework repeats as fact). Sources: [Dealroom.co](https://app.dealroom.co/news/note/kenneth-dart-s-candle-lake-crosses-30-in-evolution-triggering-mandatory-bid), [Cision (Candle Lake's own disclosure)](https://news.cision.com/candle-lake-limited/r/candle-lake-limited-has-acquired-shares-in-evolution-ab--thereby-triggering-a-mandatory-offer-obliga,c4377561), [MarketScreener](https://www.marketscreener.com/news/kenneth-dart-crosses-the-mandatory-bid-threshold-in-evolution-ce7f51dcdb89f425).
- Candle Lake now has **~4 weeks from disclosure (i.e. by roughly 21 Aug 2026)** to either **launch a mandatory offer for all remaining shares or sell down below 30%**.
- Market commentary (MarketScreener, "*Evolution Shareholders Should Not Expect a Generous Bid from Dart*") suggests the market does **not** expect a premium tender price.
- This is a genuine, material, previously-undocumented **Rule 9 M&A/ownership event** — the 2026-07-24 watchlist entry's "Next review trigger" section names "material M&A" as a standing trigger and does not reflect this disclosure (that session's own trigger was the same-day UKGC settlement story, unrelated). **No watchlist entry exists that captures the Candle Lake situation → this re-evaluation is warranted per `/telegram-scan` step 4.**

This is a **re-run of the full new-position process** (not a first-time evaluation) — fundamentals are unchanged since 2026-07-24 (no new quarterly release identified), but price, FX, 10Y yield, and — critically — analyst consensus targets are refreshed live, and the Candle Lake situation is folded in as qualitative context per §6.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$71.40** (EVVTY, IBKR `get_price_snapshot`, `last`, contract_id 245152296) | IBKR |
| **Data note — this is a closing price, not an intraday trade.** `is_close: true`, volume 0. Confirmed via `get_price_history` (ONE_DAY bars): the most recent bar is **2026-07-24** (close $71.395); no new bar exists for 07-25/07-26 (weekend) or 07-27 (US market had not yet opened at the time of this data pull, ~08:00 UTC). This is the correct "most recent available" live-price read per Rule 0 — flagged rather than silently treated as a fresh intraday print. | IBKR |
| Prior-session live price (2026-07-24, intraday) | $71.72 | 2026-07-24 session |
| SEK cross-check | ~695.00 SEK (same last-available-close convention) | WebSearch (Investing.com aggregation) |
| Implied FX cross-check | 695.00 / 71.40 = **9.734 SEK/USD** | Derived |
| Live EUR/USD | **1.1396059** | IBKR `get_account_balances` |
| 52-week range (fresh) | Low $56.88 / High $92.84 (misc_statistics) | IBKR |
| 13-week / 26-week high (fresh) | **$77.75** (identical for both windows — the 26-week high was set within the last 13 weeks) | IBKR `get_price_snapshot` misc_statistics |
| Analyst consensus 12-mo target (fresh) | Avg **667.06 SEK**, high **1,056.10 SEK**, low **516.70 SEK**; rating **Neutral** (4 Buy / 6 Sell / 6 Hold, 17 analysts) — **down from the 2026-07-24 read (avg 699.72 SEK)**, consistent with the market pricing in a "no generous bid" expectation post-Candle Lake-disclosure | WebSearch (MarketScreener aggregation) |
| US 10Y Treasury yield | 4.67% (Friday 07-24 close, most recent available) | WebSearch |

---

## 2. Quality Score (Phase 01) — recomputed, inputs unchanged

**No new quarterly release identified since the 2026-07-24 session** (TTM window still ends Jun'26; no earnings date has passed in the intervening 3 days). Recomputing the same formula against the same sourced inputs (stockanalysis.com STO:EVO financial-statement pages) necessarily reproduces the same result — reproduced here in full rather than merely cited, per the "no black-box outputs" rule:

| Sub-score | Value | Weight | Contribution |
|---|---|---|---|
| Profitability | 100.0 (Net Margin 50.50%, ROIC 32.40%, both capped) | 25% | 25.0 |
| Margins | 100.0 (capped; data caveat — source reports 100% gross margin, no separate COGS line) | 15% | 15.0 |
| Growth | 53.08 (3yr Rev CAGR 13.27%; +10 NA TAM-expansion / −10 Europe structural-deceleration modifiers net to 0) | 20% | 10.616 |
| Balance Sheet | 100.0 (net cash every year shown) | 15% | 15.0 |
| Moat Signal | 40.0 (2/5: market share ~60–70% vs. Playtech ~15%; switching costs ~€15–25M/18–24mo, secondary-sourced) | 15% | 6.0 |
| FCF Quality | 100.0 (FCF/NI 116.4%) | 10% | 10.0 |

```
Quality Score = 25.0 + 15.0 + 10.616 + 15.0 + 6.0 + 10.0 = 81.616 → 81.6
```

**Hard disqualifiers:** unchanged, none fire (FCF/NI clear, net cash every year, FCF-positive every year shown).

**⚠️ Quality Score = 81.6 — still clears the 80.0+ gate by only 1.6 points**, same sensitivity note as 07-24: a 1/5 Moat reading (dropping the secondary-sourced switching-costs signal) would drop this to 78.6 and FAIL. Unchanged since no new Moat evidence has emerged.

**PASSES the 80.0+ gate (marginally, unchanged) — proceeds to Phase 02.**

---

## 3. Phase 02 — Valuation Score (refreshed price/FX/consensus)

**PEG eligibility:** unchanged — not a Fast Grower (FY2024→FY2025 EPS −11.5%). **PEG not applicable — 15% weight redistributed to EV/EBIT (→ 40%).**

**Market Cap:** 191.49M shares × $71.40 = **$13,672.4M**

**FCF Yield (40%):** TTM FCF €1,236M × 1.1396059 = $1,408.55M. FCF Yield = 1,408.55 / 13,672.4 = **10.30%**. FCF_Score = clamp(100×(1−10.30/10)) = clamp(−3.0) → **0.0**

**EV/EBIT (40%, PEG-redistributed):** Total Debt €90.2M → $102.80M; Cash €1,154M → $1,315.1M. EV = 13,672.4 + 102.80 − 1,315.1 = **$12,460.1M**. EBIT TTM €1,238M → $1,410.8M. EV/EBIT = 12,460.1/1,410.8 = **8.83×**. EV/EBIT_Score = clamp((8.83−12)/23×100) = clamp(−13.8%) → **0.0**

**Forward PE (20%):** Price moved −0.45% vs. 07-24 ($71.40 vs $71.72); no new EPS estimate identified. Forward PE ≈ 10.71 × (71.40/71.72) = **10.66**, Trailing PE ≈ **11.67** — both still below the cited 5yr low (13.4×) → **FwdPE_Score = 0.0** (unchanged floor; Historical PE Modifier moot, already at floor).

```
Raw weighted score = 0.0×0.40 + 0.0×0.40 + 0.0×0.20 = 0.0
+ Rate Regime Modifier: +5.0 (10Y 4.67%, 3.5–5% bracket, unchanged)
```

### Upside/Downside Modifier (refreshed)

**Step 1 — Expected annual return E:**
- PW Fair Value inputs — **fresh analyst-consensus spread** (WebSearch, MarketScreener, this session): Bull $1,056.10÷9.734 = **$108.51**, Base $667.06÷9.734 = **$68.55**, Bear $516.70÷9.734 = **$53.09**.
- `PW Fair Value = 0.25×108.51 + 0.50×68.55 + 0.25×53.09 = $74.68`
- `Gap Upside % = (74.68/71.40) − 1 = +4.60%`
- **Catalyst window: kept at the default 2 years — deliberately NOT shortened to the ~4-week Candle Lake decision deadline.** Using the mandatory-offer deadline as the convergence timeline would require assuming the tender price lands at the PW analyst-consensus target ($74.68) — an unfounded assumption Rule 0 disallows. The actual near-term outcome is genuinely binary and its price is undocumented: Candle Lake either (a) launches a mandatory offer at an as-yet-undisclosed price (market commentary suggests it will not be generous), or (b) sells down below 30% with no confirmed price effect either way. Flagging this explicitly as a discretionary call rather than silently picking the aggressive interpretation.
- `Annualized gap = 4.60% / 2 = 2.30%/yr`
- Intrinsic growth: Forward-vs-Trailing PE ratio (11.67/10.66 − 1) = **+9.43%/yr** (unchanged — a pure EPS-estimate ratio, unaffected by the small 3-day price move; no new EPS estimate identified).
- Shareholder yield: **~4.46%** dividend yield (scaled for the small price move; buyback authorization still deliberately excluded from quantification — see 07-24 session's reasoning, unchanged).
- `E = 2.30 + 9.43 + 4.46 = 16.19%/yr`

**Step 2 — Guardrail check:** documented catalysts exist within the 18–24 month window (Europe sequential stabilization, NA state-by-state approval, buyback authorization) independent of the Candle Lake situation — no cap applied.

```
E (16.19%) ≥ H (10%): M = −15 × clamp((16.19−10)/15, 0, 1) = −15 × 0.4127 = −6.19
```

```
Final Valuation Score = clamp(0.0 + 5.0 − 6.19, 0, 100) = clamp(−1.19, 0, 100) = 0.0
```

**Valuation Score = 0.0 — unchanged** (still floors at 0.0 after modifiers).

---

## 4. Composite Score

```
Composite Score = 0.50×(100 − Quality Score) + 0.50×Valuation Score
                = 0.50×(100 − 81.6) + 0.50×0.0
                = 9.2 + 0.0 = 9.2
```

**Composite Score = 9.2 — "Very Cheap" (0.0–29.9) band, unchanged from 07-24.**

---

## 5. Fair Value & Order Setup ([fair-value-methodology.md](../framework/fair-value-methodology.md))

**Method A — DCF (simplified single-stage, same caveat as 07-24):**
- FCF/share TTM: €1,236M ÷ 191.49M shares = €6.455 → $7.356 (×1.1396059)
- Base-case near-term FCF growth: **+3%/yr** (unchanged) → FCF₁ = $7.577
- WACC: Rf(4.67%) + Beta(0.70) × ERP(5%) = 8.17%, +1.35pp foreign-domicile/regulatory-headwind premium → **WACC ≈ 9.52%**
- Terminal growth: **2.5%**
- `DCF FV/share = 7.577 / (0.0952 − 0.025) = $107.93`

**Method B — Multiples (PW blend from §3):** **$74.68/share** (down from $78.16 on 07-24 — driven by the lower fresh analyst-consensus targets, not a change in the underlying business)

```
Blended FV = 0.40×107.93 + 0.60×74.68 = 43.17 + 44.81 = $87.98
```

**Margin of Safety:** Composite still in the 0.0–29.9 row (15–20% MoS). Same reasoning as 07-24 for using the conservative end (thin 1.6pt quality-gate margin, genuine analyst split) — **now reinforced by the added Candle Lake binary-outcome uncertainty** — used **20%**.

```
Buy Price = 87.98 × (1 − 0.20) = $70.38
```

**Live price ($71.40) is now ~1.4% ABOVE this buy-price ceiling** — a change from 07-24, where live price ($71.72) sat marginally *below* its (higher) buy ceiling ($72.12). This shift is driven almost entirely by the **lower fresh analyst-consensus targets** (avg 667.06 SEK vs. 699.72 SEK), not by any price collapse (live price only moved −0.45%). Per this framework's established convention (see 2026-06-20 NOW/NVO/V/SPGI sessions, 2026-06-22 MA), **when live price sits above the computed buy price, R/R is evaluated at the buy (limit) price, not the live price** — this is not an "enter now" case.

```
Entry Price used for R/R = Buy Price = $70.38 (limit)
Sell Target (baseline FV)   = $87.98
Bull-Case Trim Target       = 108.51 × 0.90 = $97.66
Stop Loss (20% max loss — tightest permitted for this Composite tier)
                            = 70.38 × 0.80 = $56.30

R/R = (87.98 − 70.38) / (70.38 − 56.30) = 17.60 / 14.08 = 1.25:1
```

**R/R = 1.25:1 — FAILS the mandatory 2:1 minimum** (marginally worse than 07-24's 1.29:1). Per fair-value-methodology.md Step 6: *"If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely."* No order placed regardless of live-vs-buy-price positioning, since even the disciplined limit price doesn't clear the gate.

---

## 6. Recommendation

**PASS — do not enter. Watchlist only. No change from 2026-07-24's conclusion.**

The Quality Score (81.6), Valuation Score (0.0), and Composite Score (9.2, "Very Cheap") are all unchanged from the prior session — this is a genuine re-verification, not a new number. The trade still fails on the same two independent gates as before:

1. **Quality Score gate passes by only 1.6 points**, hinging on the same single secondary-sourced Moat signal.
2. **The mandatory 2:1 Risk/Reward gate fails outright (1.25:1)** — slightly worse than 07-24's 1.29:1, driven by fresh analyst-consensus targets that came down (not by a price collapse).

**What's new and materially important, even though it doesn't move the score:** Kenneth Dart's Candle Lake Limited crossed Evolution AB's 30% mandatory-bid threshold on 2026-07-24 and has until roughly **21 Aug 2026** to launch a full mandatory tender offer or sell back down below 30%. This is a real, verified, dated, binary corporate-action event that this framework has never before had to price around for this name:

- **If Candle Lake launches an offer:** Swedish law requires the tender price be at least the highest price Candle Lake itself paid for shares in the preceding six months. We do not have that specific transaction price, but IBKR's own 26-week high for EVVTY ($77.75) is a rough, unconfirmed floor reference (~+8.9% above the current $71.40) — flagged as directional context only, deliberately not built into the score (see §3's guardrail note on why the 4-week deadline wasn't used as the catalyst window). Market commentary (MarketScreener) explicitly warns shareholders not to expect a *generous* premium above that floor.
- **If Candle Lake instead sells down below 30%** (the other legally compliant path), there may be no price effect at all, or downward pressure if the market had been pricing in offer optionality.
- Either way, this is a **binary, dated event worth tracking closely** — recommend treating **21 Aug 2026** (or whenever Candle Lake's decision is disclosed, if earlier) as a standing Rule 9 trigger regardless of the "Next review trigger" wording below.

This remains a name worth re-visiting if (a) Candle Lake's actual offer price is disclosed (would let this framework replace the rough $77.75 floor reference with a real number and re-run R/R against it), (b) Europe's sequential improvement continues into a confirmed multi-quarter trend, or (c) the price falls further without fundamental deterioration.

---

## 7. Watchlist & Stale-Score Actions

Per the new-position process: a new dated row is added only if the score, the scored↔unscored status, or the action category changed. **None did** — Quality 81.6, Valuation 0.0, Composite 9.2, and the action ("PASS — watchlist only, R/R fails") are all identical to 2026-07-24. Appended a **"Last checked (no significant change)"** line to the existing [EVO-2026-07-24.md](../watchlist/not-in-portfolio/EVO/EVO-2026-07-24.md) entry instead, documenting the refreshed price/FV/buy-price/R-R figures and — most importantly — the Candle Lake mandatory-offer disclosure, and updated the "Next review trigger" to explicitly name the ~21 Aug 2026 Candle Lake decision deadline.

No stale-score banner existed on this entry (scoring methodology version 2026-06-29, unchanged) — nothing to clear.

---

## 8. Data Gaps Flagged (summary)

1. **Live price is a last-available close (2026-07-24), not a fresh intraday trade** — US market had not yet opened at the time of this data pull (~08:00 UTC Monday). Not a Rule 0 violation (most-recent-available price used and flagged), but noted for the record.
2. **The exact price at which Candle Lake crossed 30% is not confirmed** from sources found this session — the $77.75 26-week-high figure used in §6 is a rough, IBKR-sourced *proxy* floor reference, not a confirmed mandatory-offer price. Not used in any score calculation; qualitative context only.
3. Same data caveats carried forward from 07-24 (unchanged, still apply): "100% gross margin" is a data-source artifact (no separate COGS line); ROIC TTM not separately disclosed (FY2025 proxy used); switching-costs Moat signal is secondary-sourced; buyback authorization deliberately excluded from the shareholder-yield quantification.

None of these blocked scoring — flagged for transparency, not as reasons to skip this evaluation.

---

## 9. Glossary

See [framework/glossary.md](../framework/glossary.md) for full definitions. Terms used in this session: **ADR (American Depositary Receipt)**, **OTC Pink Sheets**, **Mandatory Offer (Mandatory Takeover Bid)** *(new term added this session)*, **CAGR**, **TAM**, **Moat**, **Net Debt/EBITDA**, **EBITDA**, **Fast Grower**, **PEG ratio**, **Shareholder yield**, **Buyback yield (net buyback yield)**, **Beta**, **Equity Risk Premium (ERP)**, **WACC**, **Terminal Value**, **TTM (Trailing Twelve Months)**, **M&A**.

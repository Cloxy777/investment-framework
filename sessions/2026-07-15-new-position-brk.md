# New Position Evaluation: BRK.B (Berkshire Hathaway Inc.) — 2026-07-15

**Task type:** NEW POSITION
**Ticker:** BRK.B — NYSE, IBKR contract_id 72063691
**Company:** Berkshire Hathaway Inc. — diversified holding company / conglomerate (insurance & reinsurance incl. GEICO, BNSF railroad, Berkshire Hathaway Energy (BHE), manufacturing/service/retailing businesses, plus a large publicly-traded equity-securities portfolio)
**Analyst:** Claude (automated session)
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — [t.me/tarasguk](https://t.me/tarasguk) post #11392, ~15:11 UTC 2026-07-15, reporting a new CNBC interview in which Warren Buffett says he personally initiated Berkshire's Alphabet (GOOG) position, observes excessive speculation in markets, plans to distribute all his BRK shares to charity within the next 8 years, and currently holds stock positions worth over $140 billion. **The Telegram post is used only as a trigger to evaluate BRK — no financial data, score, or conclusion in this session is drawn from the post itself.** BRK had no watchlist entry anywhere in `watchlist/in-portfolio/` or `watchlist/not-in-portfolio/` (confirmed) and is not a current holding (confirmed against [portfolio/holdings.md](../portfolio/holdings.md) — no `BRK` row exists). Per [.claude/commands/telegram-scan.md](../.claude/commands/telegram-scan.md) step 4, "no watchlist entry exists at all" unconditionally triggers a first-ever `/new-position` evaluation regardless of the mention's newsworthiness.

**Independent verification of the trigger's factual claims (not used as scored input):** Berkshire's Alphabet position is real and independently confirmed via 13F filings — first disclosed in the Q3 2025 13F (filed 2026-11-14): 17.85M GOOG shares, ~$4.3B. By the Q1 2026 13F (as of 2026-03-31), the position had grown to 68,462,015 Class A + 17,944,778 Class C shares (~$30.7B), and a further $10B private placement (announced 2026-06-01) brought the combined stake to ~$41B — now Berkshire's 4th-largest single-company equity holding (behind AAPL, AXP, and ahead of KO). The Telegram post's "$140 billion" stock-positions figure was not reconciled to any specific reported figure this session (Berkshire's own-disclosed public-equity portfolio, at fair value, was $297.778B at 2025-12-31 and $288.034B at 2026-03-31 per its 10-K/10-Q — both far above $140B; the $140B figure may reference something else, e.g. a stale or partial number) — this discrepancy is noted but not investigated further, consistent with the instruction that the Telegram post is a trigger only, never a data source. Buffett's charitable-distribution and market-speculation commentary are qualitative remarks, not fundamental data, and are not used in any calculation below.

---

## 0. Ticker confirmation

`search_contracts("BRK")` returns many BRK-prefixed instruments (a Canadian CDR, an unrelated UK wealth manager "Brooks Macdonald," an unrelated Australian small-cap "Brookside Energy," multiple Berkshire-affiliated bonds, and several Berkshire-tracking leveraged/derivative ETFs). Among genuine Berkshire Hathaway common-stock listings:

| Class | Exchange | Contract ID | Note |
|---|---|---|---|
| **Class B (BRK.B)** | NYSE | **72063691** | Used throughout this session |
| Class A (BRK.A) | NYSE | 5222 | ~1,500× the per-share price of Class B; economically ~1,500 Class B shares but with proportionally *fewer* voting rights per dollar (1/10,000th of a Class A vote per B share, a deliberate Buffett-era structure to prevent Class B from being used as a control instrument) |

**BRK.B is used** — the standard retail-traded class, the one accessible at ordinary position-sizing dollar amounts (BRK.A trades at ~$490.19 × 1,500 ≈ $735,000/share, impractical for the position sizes this framework computes), and the class most standard brokerage/data infrastructure (including this repo's own IBKR access) defaults to. Economically near-identical per-dollar exposure to the underlying business; no strong reason to prefer Class A for this evaluation.

### 0a. Business-model mismatch flagged up front

Berkshire Hathaway is a **diversified holding company / conglomerate** — insurance and reinsurance (GEICO, Berkshire Hathaway Reinsurance Group, Berkshire Hathaway Primary Group), a Class I railroad (BNSF), a regulated utility/energy holding company (Berkshire Hathaway Energy), a large slate of manufacturing/service/retailing subsidiaries (from Duracell to See's Candies to NetJets), *and* a roughly $290–300B portfolio of publicly-traded equity securities (AAPL, AXP, KO, CVX, GOOG, etc.). The framework's Phase 01/02 methodology has **no documented carve-out for a conglomerate of this kind**, and several sub-scores are mechanically distorted by this structure in ways distinct from (though thematically related to) the previously-documented bank/depository-institution gap (SOFI 2026-06-21, Citigroup 2026-07-12, JPM 2026-07-14):

1. **GAAP net income is dominated by non-cash, unrealized investment gains/losses on the equity portfolio.** Since ASU 2016-01 (effective 2018), US GAAP requires unrealized gains/losses on equity securities to run through net income every quarter, regardless of whether anything was sold. This is a mandated accounting rule, not an aggressive or gameable choice by management — but it makes single-year (or even TTM) "Net Income" swing wildly with stock-market moves unrelated to the operating businesses' actual performance (Berkshire posted a **-$22.8B net loss in FY2022**, a bear-market year for its equity holdings, despite its insurance/rail/energy/manufacturing businesses being profitably run that entire year). Buffett has explicitly told investors for years to ignore this GAAP "bottom line" and focus on **operating earnings** instead.
2. **"Gross Margin" blends businesses with fundamentally different margin structures** (insurance loss-ratio economics, a railroad's operating ratio, a utility's rate-base economics, and ordinary retail/manufacturing cost-of-goods-sold) into one number that is computable but not cleanly comparable to a single-business company's gross margin, nor internally consistent from year to year as segment mix shifts.
3. **Enterprise Value is highly convention-dependent** because Berkshire holds an unusually large "excess" liquidity/investment position — $51.5B cash & equivalents, **$339.3B in short-term US Treasury Bills**, and a further **$288–298B equity-securities portfolio**, against total debt of only ~$129B and a market cap of ~$1.06T. Whether some, all, or none of the T-Bill hoard and/or the equity portfolio should be netted out of Enterprise Value (and out of Net Debt for the Balance Sheet sub-score) is a genuine methodological choice with no single "right" answer for a company whose core business model *is* investing insurance float — this is shown explicitly in Sections 2d and 4 below, since it swings the EV/EBIT multiple from ~9× to ~20× depending purely on which convention is used.
4. **Operating cash flow and reported net income diverge for two separate, independently documented reasons** rather than one: (a) the same investment-gains/losses distortion as #1 above, and (b) a real, disclosed, quantified **growth-capex buildout** at Berkshire Hathaway Energy and BNSF (Section 2f) that legitimately depresses Free Cash Flow relative to earnings — this is examined in detail in Section 2f against the Quality Score's own documented "growth-capex" hard-disqualifier carve-out.

Every quality-score input below is computed and shown exactly as the framework's documented formula requires; every place the formula doesn't cleanly map to a conglomerate of this kind is flagged explicitly, and — per the same "illustrative/override" convention used in the SOFI/Citigroup/JPM sessions — an illustrative alternative is shown alongside the primary mechanical computation rather than silently invented or patched.

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

| Source | Value | Note |
|---|---|---|
| **IBKR live snapshot** (contract_id 72063691) | **$490.19** | Last trade, `is_close: false` — genuine live intraday quote, 2026-07-15, timestamp 2026-07-15T16:08:07Z |
| IBKR `change` | −$0.90 (−0.18%) vs. prior close ($491.09) | Small, unremarkable intraday move — no fundamental trigger implied |
| IBKR `misc_statistics` | 52-week range: **$455.25 – $516.82**; 13-week/26-week high **$512.57**; open 52 weeks ago **$475.40** | Currently mid-range, ~5.1% below the 52-week high |
| IBKR `dividend_yield` | **0.0%** | Berkshire has never paid a dividend under Buffett — retains and reinvests all earnings, or repurchases stock when management judges price below intrinsic value |
| IBKR `bid_ask` | $490.13 / $490.24 | Very tight spread, consistent with an extremely large-cap, highly liquid name |

**$490.19 is used throughout.**

---

## 2. Phase 01 Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

All figures below are sourced from Berkshire Hathaway's own SEC filings (10-K, 10-Q — via SEC EDGAR's XBRL company-facts API, which serves exact tagged values from the filings themselves) and, where the exact concept isn't cleanly filed (e.g. a single "Operating Income"/EBIT line, which Berkshire's income-statement presentation hasn't reported as a discrete XBRL-tagged concept since 2013), from stockanalysis.com as a vendor-derived cross-check, explicitly flagged as such. `yfinance` was not attempted this session given its recurring environment failures documented in the 2026-07-12 Citigroup and 2026-07-14 JPM sessions — WebSearch/WebFetch against SEC EDGAR and stockanalysis.com were used directly instead.

### 2a. Profitability (25% weight)

**TTM basis** (FY2025 − Q1 2025 + Q1 2026, all SEC-XBRL-sourced "Revenues" and "NetIncomeLoss" — the latter is Berkshire's GAAP net earnings attributable to shareholders):

```
TTM Revenue    = $371,444M (FY2025) − $89,725M (Q1 2025) + $93,675M (Q1 2026) = $375,394M
TTM Net Income = $66,968M (FY2025) − $4,603M (Q1 2025) + $10,106M (Q1 2026) = $72,471M

TTM Net Margin = 72,471 / 375,394 = 19.30%
NetMargin_Component = clamp((19.30 / 30) × 100, 0, 100) = 64.33
```

**ROIC proxy: ROE.** Computing a literal NOPAT ÷ Invested-Capital ROIC would require (a) an assumed effective tax rate not cleanly available this session and (b) the same vendor-derived EBIT figure already flagged as internally inconsistent in Section 2d below — compounding one estimation problem on top of another. ROE (fully GAAP-sourced on both sides — net income and shareholders' equity are both SEC-filed figures, no assumption required) is used instead, consistent with how ROE substitutes for ROIC in this framework's bank sessions, though for a different underlying reason (there, ROIC doesn't conceptually apply to a bank at all; here, ROIC is conceptually valid but not cleanly computable without introducing an unsupported assumption).

```
Average Shareholders' Equity = ($717,419M [2025-12-31] + $727,181M [2026-03-31]) / 2 = $722,300M
TTM ROE = 72,471 / 722,300 = 10.03%
ROIC_Component (ROE proxy) = clamp((10.03 / 30) × 100, 0, 100) = 33.43

Profitability_Score (primary, GAAP TTM basis) = (64.33 + 33.43) / 2 = 48.88
```

**FCF-positive-3-years check (feeds the Profitability cap):** **PASSES** — Free Cash Flow was positive in every year FY2021–FY2025 (Section 2f) — no cap applied.

**Illustrative alternative — Operating Earnings basis (shown for transparency, not scored primarily):** Berkshire's own consistently-disclosed, non-GAAP "operating earnings" measure excludes investment/derivative gains and losses — the figure Buffett and now CEO Greg Abel explicitly ask investors to focus on instead of GAAP net earnings, precisely because of the ASU 2016-01 distortion described in Section 0a. TTM operating earnings ≈ $44.49B (FY2025) − ~$9.6B (Q1 2025, rounded, per company earnings-release coverage) + ~$11.3B (Q1 2026, rounded) = **~$46.19B**.

```
Illustrative TTM Op-Earnings Net Margin = 46,190 / 375,394 = 12.31%  → Component = 41.02
Illustrative TTM Op-Earnings "ROE"      = 46,190 / 722,300 = 6.40%   → Component = 21.32
Illustrative Profitability_Score (Op-Earnings basis) = (41.02 + 21.32) / 2 = 31.17
```

Note the illustrative alternative is **lower**, not higher, than the primary GAAP-basis score this particular TTM period — because this specific trailing-twelve-month window happened to include net *investment gains* on top of operating earnings, not losses. This is the point of flagging it: which direction the distortion cuts is not fixed, it swings with the market, which is exactly why a single-period GAAP Net Margin/ROE is an unreliable quality signal for this company. **Primary computation (48.88) is used for the Quality Score below**, per the strict "score off filed GAAP figures" convention already established for guidance/non-GAAP measures elsewhere in this framework (valuation-scoring.md, "Why Forward Guidance Is Not a Sub-score").

### 2b. Margins (15% weight)

```
GrossMargin_Score = clamp((29.53 / 80) × 100, 0, 100) = 36.91
```

FY2025 gross margin 29.53% (stockanalysis.com, vendor-computed — Berkshire's own income-statement presentation does not report a discrete "Gross Profit" line, since insurance premiums/losses, railroad/utility revenues and costs, and ordinary retail/manufacturing COGS don't share a common "cost of revenue" concept). **Flagged, not treated as N/M**: unlike a bank (which has no gross-margin concept at all), a number is genuinely computable here — but it blends businesses with structurally different margin profiles (insurance loss-ratio economics vs. a railroad's operating ratio vs. utility rate-base economics vs. ordinary retail/manufacturing COGS), so year-over-year moves in this blended figure more likely reflect segment-revenue-mix shift than a single business's pricing power or cost structure changing. **No structural-expansion +10 bonus applied**: the blended margin did move from ~25.2–25.5% (2022–2023) to ~29.0–29.5% (2024–2025) per the same vendor source, but with no single documented mechanism (pricing power, mix shift, or a specific segment's margin improvement) cited this session to attribute it to a real structural trend rather than segment-mix noise — applying the bonus without that citation would violate quality-scoring.md's "never infer this modifier without a documented source."

### 2c. Growth (20% weight)

```
Revenue 3yr CAGR = (FY2025 Revenue $371,444M / FY2022 Revenue $302,089M)^(1/3) − 1 = 7.13%
Growth_Score = clamp((7.13 / 25) × 100, 0, 100) = 28.52
```

(Both figures SEC-XBRL "Revenues," full fiscal year.)

**TAM/pricing-power modifier: declined, not applied.** Berkshire Hathaway Energy has real, quantified, documented growth capex — $33.3B planned for 2026–2028 (+16% vs. $28.7B in 2023–2025), including $15.8B in transmission & distribution (up from $12.2B) and a $3.2B HVDC transmission joint venture with Grid United, driven substantially by data-center/AI-related electricity-demand growth — but this evidence is specific to **one segment** (Energy) out of roughly five major segments (Insurance, BNSF, BHE, Manufacturing/Service/Retailing, plus the investment portfolio). Applying quality-scoring.md's company-wide +10 TAM modifier off a single-segment citation would overstate a partial signal as a whole-conglomerate one — declined for that reason, though noted here as a genuine positive data point for the Energy segment specifically. **No documented structural-deceleration −10 modifier applied either**: CEO Greg Abel's public comments about insurance becoming "increasingly competitive" (Section 4) speak to underwriting *margin* pressure, not documented *revenue-growth* deceleration specifically — conflating the two would misapply the modifier, so it's declined here too.

### 2d. Balance Sheet (15% weight)

Net Debt/EBITDA, using FY2025 SEC-filed figures:

```
Total Debt (FY2025)              = $129,081M
D&A (FY2025, SEC XBRL)            = $13,476M
EBIT (FY2025, vendor-derived — see caveat below) = $58,040M
EBITDA (FY2025)                   = 58,040 + 13,476 = $71,516M
```

**EBIT sourcing caveat:** Berkshire has not reported a discrete "OperatingIncomeLoss" XBRL concept since 2013 (its post-ASU-2016-01 income-statement presentation folds operating results and investment gains/losses into a smaller set of line items) — the $58,040M FY2025 EBIT figure above is stockanalysis.com's vendor-computed approximation, not a company-filed number. **This figure is internally inconsistent with the same vendor's own separately-published EV/EBIT ratio** (stockanalysis.com shows EV/EBIT = 7.61× against an EV of $793.17B, which implies an EBIT of ~$104.2B — nearly double the $58,040M figure the same vendor's financials page shows directly). This inconsistency could not be resolved this session and is flagged as a genuine data-quality gap, not silently picked one way or the other — see Section 4 for the full EV/EBIT discussion (moot for this session's outcome, since Phase 02 is never reached, but material if this name is ever re-evaluated).

**Net Debt — two readings, both shown:**

```
(a) Narrow — "cash and cash equivalents" only ($51,877M, FY2025):
    Net Debt = 129,081 − 51,877 = $77,204M
    Net Debt/EBITDA = 77,204 / 71,516 = 1.08×
    BalanceSheet_Score = clamp(100 × (1 − 1.08/4), 0, 100) = 73.01

(b) Broad — including the $339.3B short-term US Treasury Bill position (Q1 2026 10-Q disclosure;
    "cash, cash equivalents, and U.S. Treasury Bills, net" = $373.5B combined):
    Net Debt = 128,886M (TTM debt) − 373,500M ≈ −$244,614M   (a NET CASH position)
    Net Debt/EBITDA is negative → BalanceSheet_Score clamps to 100.0
```

**Broad reading (100.0) used as primary** — Treasury Bills are, for practical leverage-risk purposes, cash-equivalent (near-zero credit/duration risk, extremely liquid), and Berkshire's own disclosure explicitly presents cash and T-Bills as a single combined liquidity figure; treating them as unavailable to offset debt would understate what is, by a wide margin, one of the strongest balance sheets of any company in this framework's book (this reading is directionally consistent with Berkshire's AA+/Aa2-class credit ratings — not independently re-verified this session). **Narrow reading (73.01) shown as the conservative mechanical alternative.** Either way, this sub-score is not what drives the Quality Score outcome (Section 2h).

**Conglomerate rule check:** consolidated Total Debt ($129,081M) already includes BNSF's and BHE's own reported debt (both are wholly-owned subsidiaries fully consolidated onto Berkshire's balance sheet, not off-balance-sheet financing vehicles) — no additional captive-subsidiary adjustment needed.

### 2e. Moat Signal (15% weight)

| Signal | Evidence | Result |
|---|---|---|
| Market share stable/growing | GEICO ranks #2 in US auto insurance (~18% share, trailing only State Farm); FY2025 premiums written +5.2% to $45.2B, driven by growing policies-in-force. BNSF operates in a near-duopoly in the Western US (with Union Pacific) for Class I freight rail. | ✅ TRUE |
| Brand premium | See's Candies (a long-cited Buffett case study) has demonstrated repeated pricing power (price increases sustained over decades without material volume loss) — a small subsidiary by Berkshire's overall scale, but a genuine, specifically documented pricing-power example within the conglomerate. | ✅ TRUE |
| Network effect | No documented two-sided-marketplace or user-growth-driven network mechanism identified across Berkshire's core segments (insurance, railroad, utility, manufacturing/retail don't exhibit this dynamic) this session. | ❌ not established |
| Switching costs | BNSF's industrial rail-freight customers typically build sidings/facilities physically tied to BNSF's specific network — a documented physical-infrastructure lock-in mechanism, distinct from (and less contestable than) GEICO's auto-insurance book, where 2025 company commentary specifically flagged "unprecedented comparison shopping" among policyholders (a countervailing, low-switching-cost signal for the insurance segment specifically). | ✅ TRUE (rail) |
| Scale cost advantage | No specific cost-per-unit citation vs. smaller rail or insurance competitors sourced this session (GEICO's 12.4% FY2025 expense ratio is suggestive of a low-cost direct-to-consumer model but wasn't benchmarked against a named competitor's expense ratio this session). | ❌ not established |

```
Moat_Score = (3/5) × 100 = 60.0
```

### 2f. FCF Quality (10% weight) & the growth-capex hard-disqualifier question

```
FY2021 FCF = $26,151M   FY2021 NI = $89,937M   → FCF/NI = 29.08%
FY2022 FCF = $21,886M   FY2022 NI = −$22,819M  → FCF/NI = negative (NI loss)
FY2023 FCF = $29,787M   FY2023 NI = $96,223M   → FCF/NI = 30.96%
FY2024 FCF = $11,616M   FY2024 NI = $88,995M   → FCF/NI = 13.05%
FY2025 FCF = $25,042M   FY2025 NI = $66,968M   → FCF/NI = 37.40%
```
(FCF = Operating Cash Flow − CapEx, both stockanalysis.com-sourced and cross-checked directionally against SEC XBRL D&A/debt figures above; NI = SEC-XBRL NetIncomeLoss.)

```
FCFQuality_Score (primary, FY2025 GAAP-NI basis) = clamp(((0.374 − 0.40) / 0.60) × 100, 0, 100) = 0.0   (clamped)
```

**Hard disqualifier check — "FCF/NI conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation":** the literal ratio is below 70% in every one of the last 5 years. Two independent, documented explanations were found for why this does **not** reflect a Valeant/Wirecard-style cash-conversion quality problem:

1. **Documented growth capex.** CapEx grew from $13,276M (FY2021) to $20,927M (FY2025), +58% — driven substantially by Berkshire Hathaway Energy's disclosed growth buildout ($33.3B planned 2026–2028, +16% vs. 2023–2025; transmission, grid modernization, renewable generation, driven by rising electricity demand) and BNSF's own capital plan (~$3.6B for 2026). This is a real, quantified, company-disclosed growth-capex story — the same category of carve-out the disqualifier rule's own text anticipates ("without a documented growth-capex explanation"), and the same logic Hybrid Upgrade 1 already applies to MSFT/GOOGL/META/AMZN.
2. **GAAP Net Income embeds non-cash investment gains/losses (Section 0a/2a)** unrelated to the cash-generating operating businesses — inflating (or in 2022, deflating) the ratio's denominator independent of any operating-cash-flow weakness.

**Resolution: the hard disqualifier is treated as NOT firing**, on the strength of the documented growth-capex carve-out plus the independently-documented GAAP-NI distortion — but this is flagged as a judgment call, not a clean-cut reading, consistent with how the JPM session declined a similar carve-out because no comparable growth-capex citation existed there. **This is ultimately moot for this session's outcome** (Section 2h): even with no hard disqualifier firing, the weighted Quality Score fails the 80.0 gate by a wide margin regardless.

**Illustrative alternative (Operating-Earnings basis, FY2025):** FCF $25,042M / Operating Earnings $44,490M = 56.3% → `FCFQuality_Score` (illustrative) = clamp(((0.563−0.40)/0.60)×100) = 27.17. Still below 70%, still clamped well short of full credit — the growth-capex effect alone doesn't fully explain the gap even after removing the investment-gains noise from the denominator.

### 2g. Full Quality Score — primary computation

```
Quality Score = (Profitability × 0.25) + (Margins × 0.15) + (Growth × 0.20) + (BalanceSheet × 0.15) + (Moat × 0.15) + (FCFQuality × 0.10)

              = (48.88 × 0.25) + (36.91 × 0.15) + (28.52 × 0.20) + (100.0 × 0.15) + (60.0 × 0.15) + (0.0 × 0.10)
              = 12.22 + 5.5365 + 5.704 + 15.00 + 9.00 + 0.00
              = 47.46 → 47.5
```

### 2h. Illustrative ceiling (most generous resolution of every ambiguous input — shown for robustness, not to override the result)

Granting every ambiguous judgment call its most generous reading simultaneously (higher of the two Profitability readings; +10 Margins structural bonus; +10 Growth TAM modifier; broad-cash Balance Sheet; a 4th Moat signal credited; the Operating-Earnings-basis FCF Quality reading):

```
Illustrative ceiling = (48.88×0.25) + (46.91×0.15) + (38.52×0.20) + (100.0×0.15) + (80.0×0.15) + (27.17×0.10)
                     = 12.22 + 7.0365 + 7.704 + 15.00 + 12.00 + 2.717
                     = 56.68
```

**Even under the single most generous possible resolution of every ambiguous or vendor-flagged input, the score (56.68) sits decisively below the 80.0 gate.** Conservative reading (47.46, using the narrow-cash Balance Sheet reading of 73.01 instead of 100.0 would give 43.42) and generous reading (56.68) bracket a range that never approaches 80.0.

### Gate Result: ❌ **FAIL**

- Primary computed Quality Score: **47.5** (or 43.4 under the more conservative narrow-cash Balance Sheet reading).
- Illustrative best-case ceiling: **56.7** — still well short of 80.0.
- The hard-disqualifier question (Section 2f) is treated as not firing on a documented growth-capex + GAAP-distortion basis, but is **moot**: the weighted score fails the gate independent of that judgment call.
- Per [.claude/commands/new-position.md](../.claude/commands/new-position.md) and quality-scoring.md, **this evaluation stops here — no Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is performed.**

---

## 3. Why this reads as a framework-calibration gap, not a genuine red flag on Berkshire itself

Unlike the JPM/Citigroup/SOFI cases (where a *hard disqualifier* mechanically fired due to a cash-flow-classification artifact specific to banks), Berkshire's failure here is different in character: it is decisively below the 80.0 gate on the **weighted score itself**, largely because this framework's Profitability, Growth, and Margins sub-scores are calibrated with ceilings (30% ROIC/margin, 25% revenue CAGR, 80% gross margin) that reward high-growth, high-margin, capital-efficient businesses — a profile Berkshire, by design and by its sheer scale (~$1.06T market cap, ~$720B equity base), structurally cannot fit, even though it is arguably one of the highest-quality, most conservatively-financed, most durably-moated businesses in existence by Buffett/Munger/Graham's own standards (this framework's foundational influences — see [investor-philosophy-alignment.md](../framework/investor-philosophy-alignment.md)). A ~7% revenue CAGR and ~10% ROE are unremarkable by this framework's growth-company-calibrated yardsticks, but are what one should *expect* from a fully-mature, deliberately-conservative, insurance-float-funded conglomerate of this size — this tension (a framework built partly on Buffett's own philosophy scoring a Buffett-run company this low) is worth flagging explicitly as a candidate framework-calibration gap, alongside the now-three-times-documented bank FCF-classification gap and the newly-observed conglomerate-specific distortions in Sections 0a, 2a, 2d, and 4 (GAAP-investment-gains noise in Net Income; ambiguous Enterprise Value/Net-Debt conventions when a company holds a $600B+ combined cash/T-Bill/equity-portfolio position). **Recommended as a candidate item for a future `decisions/` entry** — not resolved within this session (no framework file was edited here), consistent with how the JPM/SOFI/Citigroup sessions flagged their own gap without unilaterally patching quality-scoring.md.

---

## 4. Additional context (not scored — informational only, since Phase 02 was not run)

- **Insurance float:** $176B at 2025-12-31 (up from $171B at 2024-12-31, $88B at 2015-12-31) — the low-cost (sometimes negative-cost, when underwriting is profitable) pool of policyholder funds Berkshire invests; a structural source of investable capital distinct from debt, and a large part of why standard leverage metrics undersell Berkshire's financial flexibility.
- **FY2025 operating earnings by segment** (company-disclosed, non-GAAP, cited for color only): Insurance underwriting $7.26B (down from $9.0B in FY2024), Insurance investment income $12.5B (down from $13.6B), with BNSF, BHE, and Manufacturing/Service/Retailing also contributing — total operating earnings $44.49B, down ~6.2% from FY2024's $47.44B, driven primarily by the underwriting-profit decline. CEO Greg Abel (Buffett's successor as CEO, effective 2026) has publicly characterized the insurance market as "increasingly competitive."
- **The EV/EBIT ambiguity (Section 2d), spelled out fully:** using live market cap (~$1,057.3B, at $490.19 × 1,437,903 Class-A-equivalent shares × 1,500) plus FY2025 total debt ($129,081M), Enterprise Value ranges from **~$1,134.5B** (netting only narrow cash-and-equivalents, $51,877M) down to **~$813.0B** (netting the full $373.5B cash+T-Bill position) down to **~$515.0B** (additionally netting the ~$297.8B equity-securities portfolio as a non-operating asset) — a swing of more than 2× depending purely on convention. Against the same (vendor-flagged-as-inconsistent) $58,040M EBIT figure, that's an EV/EBIT range of **~8.9× to ~19.6×** — the difference between "looks expensive" and "looks cheap" on this single metric, driven entirely by an unresolved definitional question rather than by any new information about the business. This is flagged here for whoever next evaluates BRK under Phase 02, since it will need to be resolved (or at minimum, explicitly chosen and justified) before an EV/EBIT sub-score can be trusted.
- **Buybacks/capital return:** Berkshire resumed share repurchases in March 2026 after a nearly two-year hiatus (last prior buyback May 2024) — repurchases are only made when the CEO (in consultation with the Chairman) judges the price below Berkshire's own conservatively-determined intrinsic value; no fixed minimum or maximum commitment. No dividend, and none planned near-term per Abel's public comments.
- **GOOG position:** independently confirmed real and growing (Section header) — not itself a scored input, cited only to verify the Telegram trigger's factual claim.

---

## 5. Data sourcing note

`yfinance` was not attempted this session (recurring `curl_cffi` TLS/connection-reset failures documented in the 2026-07-12 Citigroup and 2026-07-14 JPM sessions in this same environment). **Fallback used: SEC EDGAR's XBRL company-facts API** (`data.sec.gov/api/xbrl/companyconcept/CIK0001067983/...`) for all officially-filed figures (Revenues, NetIncomeLoss, StockholdersEquity, DepreciationDepletionAndAmortization, EquitySecuritiesFvNi — all pulled directly from Berkshire's own 10-K/10-Q XBRL tags), **WebSearch** for company earnings-release commentary and third-party reporting (operating earnings by segment, float, buybacks, capex plans, GEICO/BNSF moat evidence), and **stockanalysis.com** (via WebFetch) for the handful of figures Berkshire doesn't file as a discrete XBRL concept (vendor-derived EBIT/"Operating Income," Gross Margin, EV/EBITDA/EV/EBIT ratios) — each such figure is explicitly flagged as vendor-derived above, including one flagged internal inconsistency (Section 2d) that could not be resolved this session. IBKR's `get_price_snapshot` and `search_contracts` (Rule 0 live price) worked normally.

---

## 6. Recommendation: **PASS**

**The Phase 01 Quality Score gate fails.** Primary computed Quality Score **47.5** (range 43.4–56.7 across every tested reading of the conglomerate-specific ambiguities identified above), decisively below the 80.0 threshold under every resolution tested. Per [.claude/commands/new-position.md](../.claude/commands/new-position.md), the evaluation stops here — **no Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work was performed.**

This is a different class of finding than the SOFI/Citigroup/JPM bank sessions (a mechanically-firing hard disqualifier): here, the weighted score itself falls well short, largely because this framework's growth/margin/ROIC calibration doesn't fit a mega-cap, mature, deliberately-conservative conglomerate — even one this framework's own philosophical influences (Buffett, Munger) would regard as an exceptionally high-quality business. Combined with the genuinely ambiguous Enterprise Value/Net-Debt conventions and the ASU-2016-01 GAAP-net-income distortion documented above, this is flagged as a **candidate framework-calibration gap** worth a future `decisions/` discussion — not resolved within this session.

Added to the not-in-portfolio watchlist (Section 7), flagged for re-evaluation on (a) a documented framework carve-out or calibration adjustment for mega-cap conglomerates/insurance-float-funded businesses, or (b) a further Rule 9 fundamental trigger (next scheduled one: Q2 2026 earnings, expected early August 2026, alongside Berkshire's own Q2 10-Q).

---

## 7. Watchlist entry

See [watchlist/not-in-portfolio/BRK/BRK-2026-07-15.md](../watchlist/not-in-portfolio/BRK/BRK-2026-07-15.md) — new entry (first time BRK has been evaluated under this framework).

---

## Glossary

| Term | Meaning |
|---|---|
| **ASU 2016-01** | The US GAAP accounting standards update (effective 2018) requiring companies to run unrealized gains/losses on equity-security investments through net income every period, rather than through other comprehensive income as under the prior rule. The reason Berkshire Hathaway's GAAP "net earnings" swings sharply with stock-market moves (e.g. a $22.8B net *loss* in FY2022) even when its actual operating businesses are performing consistently — Buffett has repeatedly told investors to look at operating earnings instead. *(New term.)* |
| **BHE (Berkshire Hathaway Energy)** | Berkshire's regulated utility/energy holding-company subsidiary (electric/gas utilities, transmission, and a large renewables portfolio) — one of Berkshire's core operating segments alongside insurance, BNSF, and Manufacturing/Service/Retailing. *(New term.)* |
| **BNSF** | Burlington Northern Santa Fe, the Class I freight railroad Berkshire Hathaway wholly owns — one of only two major Class I railroads serving the Western United States (the other being Union Pacific), a structural near-duopoly. *(New term.)* |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **Combined ratio** | An insurer's loss ratio (claims paid ÷ premiums earned) plus its expense ratio (operating costs ÷ premiums earned) — below 100% means the insurer made an underwriting profit before any investment income; above 100% means the underwriting book alone lost money. GEICO's FY2025 combined ratio was 84.7% (up from 81.5% in FY2024, still a solid underwriting profit). *(New term.)* |
| **D&A** | Depreciation & Amortization — the non-cash accounting expense that spreads the cost of long-lived assets over time. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization — standard operating-profit measures; flagged in this session as not cleanly filed by Berkshire as a discrete line item since 2013, requiring a vendor-derived approximation. |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **EV (Enterprise Value)** | A company's total value to all capital providers: market cap + debt − cash. Flagged in this session as unusually convention-dependent for Berkshire, given its very large combined cash/Treasury-Bill/equity-portfolio position. |
| **Float (insurance float)** | The pool of money an insurer holds between collecting premiums and eventually paying out claims — Berkshire can invest this money in the meantime, effectively a low-cost (sometimes negative-cost) source of investable capital distinct from debt. Berkshire's float was $176B at 2025-12-31. *(New term.)* |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook companies use for their official financial statements. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted score — see [quality-scoring.md](../framework/quality-scoring.md). |
| **Moat** | A durable competitive advantage that protects a business's profits from competitors. |
| **Operating earnings (Berkshire)** | Berkshire Hathaway's own consistently-disclosed non-GAAP profitability measure, which excludes investment and derivative gains/losses — distinct from (and, per Buffett/Abel, more representative of underlying business performance than) GAAP net earnings, which includes those swings per ASU 2016-01. FY2025 operating earnings were $44.49B, down from $47.44B in FY2024. |
| **Owner Earnings** | Warren Buffett's own adjusted cash-flow measure: Net Income + D&A − Maintenance CapEx only (excludes growth CapEx) — this framework's Hybrid Upgrade 1, used for moat-building reinvestors like MSFT/GOOGL/META/AMZN. |
| **Quality Score** | This framework's 0.0–100.0 continuous score grading profitability, margins, growth, balance sheet, moat signal, and FCF quality. A company must score 80.0+ to proceed to Phase 02 valuation scoring. See [quality-scoring.md](../framework/quality-scoring.md). |
| **ROE** | Return on Equity — Net Income ÷ shareholder equity; used here as a proxy for ROIC. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns invested capital (debt + equity − cash) into profit. |
| **T-Bills (Treasury Bills)** | Short-maturity (≤1 year) US government debt securities — effectively cash-equivalent in credit/liquidity risk. Berkshire held $339.3B of these at 2026-03-31, on top of $51.5B in cash and equivalents — a combined liquidity position roughly 7× its total debt. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results. |
| **XBRL** | eXtensible Business Reporting Language — the structured, machine-readable data format the SEC requires companies to tag their financial-statement figures in, allowing exact figures to be pulled programmatically from official filings rather than parsed from prose or a third-party vendor's re-presentation. |

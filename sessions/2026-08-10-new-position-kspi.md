# NEW POSITION — KSPI (JSC Kaspi.kz, Nasdaq ADR) — 2026-08-10

**Task type:** NEW POSITION (Telegram-scan trigger — no prior watchlist entry existed for this ticker in either `in-portfolio/` or `not-in-portfolio/`, per `/telegram-scan` step 4's first bullet)
**Date:** 10 Aug 2026 (Monday)
**10Y US Treasury Yield:** 4.69% — reused from the same-day [2026-08-10 TSM session](2026-08-10-new-position-tsm.md)'s FRED `DGS10` pull (most recent posted observation dated 2026-08-06); this session's own repeated attempts to re-fetch `fredgraph.csv` timed out / returned empty replies through the network proxy (three attempts, all failed at the transport layer, not a data-availability issue). Reusing a same-calendar-day, already-Rule-0-sourced figure from a sibling session is judged acceptable here since the underlying FRED series would return the identical value regardless of which session pulls it — flagged for transparency rather than silently treated as freshly fetched. **This yield is not used in this session's scoring anyway** — see §4 below, the Rate Environment Gate is never reached.
**Rate Regime Modifier:** Not applicable this session — see §4.
**Current KSPI portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — this is KSPI's first-ever evaluation under this framework.
**Sector:** Consumer Finance / Fintech — a diversified "Super App" platform (Payments, Marketplace/e-Commerce, Fintech lending) headquartered in Almaty, Kazakhstan, with a growing Türkiye subsidiary (Hepsiburada e-commerce + newly acquired Hepsi Bank).
**Filer type:** Foreign private issuer — Kaspi.kz files an annual **Form 20-F** (not a 10-K) and furnishes interim results via **Form 6-K** (not 8-K/10-Q) with the SEC (CIK 1985487), reporting under **IFRS** in **KZT (Kazakhstani Tenge)**. **ADR ratio: 1 ADS = 1 ordinary share** (confirmed via SEC filing search — multiple Kaspi.kz F-1/424B4/Form 4 filings consistently describe this 1:1 ratio; also internally consistent with `yfinance`'s reported shares-outstanding matching the balance sheet's ordinary-share count).
**IBKR contract used:** `contract_id` 679110496 — confirmed via `search_contracts`: NASDAQ, symbol KSPI, description "JSC KASPI.KZ ADR," `country_code` US, sections STK/BAG/CFD/OPT. The Frankfurt SWB2 "KKS" listing and the VALUE "KSPI.USD" synthetic (`contract_id` 450732746) were explicitly **not** used, per the task instructions.
**First-use jargon decode:** see closing Glossary (§8).

---

## 0. Trigger — Telegram post, independently verified against primary sources

**Trigger:** Telegram post `bolshegold/9947` (~14:35 UTC, 2026-08-10) forwarded a Q2 2026 earnings write-up for Kaspi.kz claiming: revenue KZT 1.1T (+15% YoY), adjusted EBITDA KZT 397B (+5% YoY), an 18% dividend increase, e-commerce as the primary growth driver, an AI-assistant launch, and a Türkiye bank acquisition.

**Per CLAUDE.md/operating-brief.md Rule 0 and the explicit task instruction, none of these figures were used as financial inputs.** Every claim was independently re-derived from Kaspi.kz's own primary SEC filing (not the Telegram text):

| Telegram claim | Independent verification |
|---|---|
| Revenue KZT 1.1T, +15% YoY | ✅ **Confirmed against Kaspi.kz's own SEC Form 6-K, filed today (2026-08-10)**, accession `0001985487-26-000024`, Exhibit 99.1: "Kaspi.kz revenue increased 15% year-over-year to KZT1.1 trillion ($2.3 billion)." |
| Adjusted EBITDA KZT 397B, +5% YoY | ✅ Confirmed, same filing: "Adjusted EBITDA increased 5% year-over-year to KZT397 billion ($826 million)." Reconciles exactly to the sum of the three disclosed platform-level Adjusted EBITDA figures: Marketplace 128B + Payments 98B + Fintech 171B = 397B. |
| 18% dividend increase | ✅ Confirmed: Board proposed increasing the quarterly dividend to KZT1,000/ADS from KZT850/ADS (+17.6%, rounds to "18%"), subject to shareholder approval at a 9 September 2026 EGM (also filed today, Exhibit 99.2 of the same 6-K). |
| E-commerce = primary growth driver | ✅ Confirmed: "e-Commerce continued to be our main growth driver" — constant-currency e-Commerce GMV +28% YoY, e-Commerce revenue +35% YoY (constant currency), VAS revenue +49% YoY (constant currency). |
| AI-assistant launch | ✅ Confirmed: "Kasper," a personal AI shopping assistant, began rolling out in July 2026, now available to all e-Commerce consumers in Kazakhstan. |
| Türkiye bank acquisition | ✅ Confirmed: completed acquisition of Rabobank A.Ş. in Türkiye in July 2026, rebranded "Hepsi Bank" — company states intent to capitalize it with ~$300M and expand Fintech lending in Türkiye from 2027. |

**Conclusion: every figure in the trigger post is confirmed, essentially exactly, against Kaspi.kz's own primary SEC filing published the same day.** This is a materially real, same-day earnings event — not a stale or mischaracterized repost. This also explains the day's large price move (see §1).

**Note on data-availability limits of the primary source used:** the 6-K's Exhibit 99.1 press release embeds its detailed consolidated income-statement/balance-sheet tables as **images** (not machine-readable text), and no companion exhibit with full unaudited interim financial statements was filed alongside it (confirmed: the filing has exactly three documents — the 6-K cover, Exhibit 99.1 press release, Exhibit 99.2 EGM notice). This means the granular Q2 2026 balance sheet and cash-flow statement are **not yet available in a Rule-0-compliant, machine-verifiable form** as of this session. See §2 for how this was handled.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$95.06** | IBKR `get_price_snapshot`, `contract_id` 679110496, `last.price`, timestamp Unix 1786378228 = **2026-08-10 16:10:28 UTC** (12:10 PM ET, regular session) |
| Prior close | $90.30 | IBKR `prior-close.priorClose` |
| Change vs. prior close | **+$4.76 (+5.27%)** | IBKR `change` field — a large, single-day move, consistent with the same-day Q2 2026 earnings beat confirmed in §0 (a documented fundamental trigger, not an unexplained price move — satisfies Rule 9's ">15% unexplained move" test trivially since this move *is* explained) |
| Bid / Ask | $95.01 / $95.52 | IBKR `bid-ask` |
| 52-week range | $65.66 (low) – $95.32 (high) | IBKR `misc-statistics` — **today's price is at/near a new 52-week high** (the `high_52w`/`high_26w`/`high_13w` fields all read $95.32, essentially today's intraday level) |
| Dividend yield (IBKR field) | 0.0% | ⚠️ IBKR `dividend-yield` returned 0.0%, which is almost certainly stale/wrong for a company that just proposed an 18% dividend increase (§0) — **not used**; not needed for this session's scoring since Phase 02 is never reached (§4), but flagged as a vendor-data-quality note for any future session that needs it. |
| US 10Y Treasury yield | 4.69% | See header note — reused from same-day TSM session; not used in this session's calculations |

**$95.06 is used as the live price for all arithmetic below** (a very limited role — see §4, since Phase 02 is not reached and no fair-value/order-setup work is performed this session).

---

## 2. Data Sourcing — yfinance access, currency handling, and a genuine data-availability gap

### 2.1 yfinance access note

Initial `yfinance` calls failed with a TLS/connection-reset error specific to `curl_cffi`'s browser-impersonation layer (the library's default HTTP backend) when routed through this environment's egress proxy — plain `curl`/`requests`-style traffic through the same proxy worked normally. Resolved by setting `YF_DISABLE_CURL_CFFI=1` (a documented `yfinance` 1.5.2 environment variable that falls back to a plain `requests` session with a standard browser User-Agent). All `yfinance` data in this session was fetched this way. Flagged for future sessions in this environment.

### 2.2 Currency handling — KZT vs. USD, and a vendor data-quality finding

Kaspi.kz reports its financial statements in **KZT (native, IFRS)**; the ADR trades in **USD**. `yfinance`'s `.info` dict mixes the two inconsistently for this ticker: e.g. `trailingEps` (11.53) and `forwardEps` (6803.44) are on wildly different scales relative to each other and relative to the KZT-denominated `Diluted EPS` figures in `t.financials` (thousands of KZT/share) — internally inconsistent, and neither is safely usable at face value. **`info.grossMargins` (0.69238, i.e. 69.2%) is a materially wrong/stale figure** — reconstructing gross margin directly from `t.financials`' `Gross Profit`/`Total Revenue` (both KZT, internally consistent) gives 47.4% for FY2025 and a TTM figure of 51.1% (§3), a large (~18–22pp) discrepancy from the vendor's `.info` field. **This session does not use any `.info`-dict derived margin, EPS, or PE figure** — every quantitative input below is reconstructed directly from `t.financials` / `t.quarterly_financials` / `t.balance_sheet` / `t.quarterly_balance_sheet` / `t.cashflow` / `t.quarterly_cashflow` (all internally KZT-consistent, cross-checked against the primary 6-K in §0 where overlapping), consistent with this framework's "never invent or estimate" discipline and its established practice of flagging (not silently adopting) vendor-data-quality issues.

### 2.3 Genuine data-availability gap: Q2 2026 balance sheet / cash flow not yet machine-readable

As noted in §0, Kaspi.kz's fresh Q2 2026 print (filed today) only discloses headline revenue/EBITDA/net-income figures in parseable text; the full balance sheet and cash-flow statement are embedded as images in the press release and no machine-readable companion exhibit exists yet. **`yfinance`'s structured quarterly statements (`t.quarterly_financials`, `t.quarterly_balance_sheet`, `t.quarterly_cashflow`) likewise do not yet carry a Q2 2026 (2026-06-30) column** — the most recent structured quarter available is **Q1 2026 (2026-03-31)**.

**Resolution used this session:** every ratio requiring a balance-sheet snapshot (Net Debt/EBITDA, Invested Capital/ROIC) uses the **Q1 2026 (2026-03-31) balance sheet** — the most recent Rule-0-compliant, machine-verifiable data available — rather than inventing or estimating a Q2 2026 figure. Every ratio requiring only income-statement flow data uses a **TTM window of Q2 2025 through Q1 2026** (the last four fully-structured quarters), reconstructed and summed directly from `yfinance`'s quarterly income statement (independently cross-checked against Kaspi's own annual FY2022–FY2025 filings for consistency — annual and quarterly figures reconcile to within ~0.1–0.2%, an immaterial gap). **This session's quantitative TTM window therefore ends one quarter before today's fresh earnings print** — a genuine, explicitly-flagged limitation, consistent with how the 2026-08-10 TSM session (same day) handled an analogous gap for a different ticker. This is judged the correct call over attempting to reconstruct an approximate Q2 2026 balance sheet by extrapolation, which would cross into "estimating financial data."

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 TTM income statement (Q2 2025 – Q1 2026), reconstructed from `t.quarterly_financials`, KZT Billions

| | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 | **TTM sum** |
|---|---|---|---|---|---|
| Total Revenue | 969.512 | 1,098.762 | 1,143.502 | 1,079.419 | **4,291.195** |
| Gross Profit | 682.365 | 500.607 | 519.479 | 490.025 | **2,192.476** |
| Operating Income | 542.254 | 335.102 | 352.950 | 321.090 | **1,551.396** |
| EBITDA (`yfinance` `Normalized EBITDA`, ≈ Op. Income + small D&A) | 543.226 | 335.102 | 352.950 | 324.306 | **1,555.584** |
| Pretax Income | 321.956 | 346.514 | 355.996 | 322.301 | **1,346.767** |
| Net Income | 257.327 | 279.418 | 284.376 | 249.394 | **1,070.515** |

```
TTM Gross Margin  = 2,192.476 / 4,291.195 = 51.09%
TTM Net Margin    = 1,070.515 / 4,291.195 = 24.95%
TTM Effective tax rate = (1,346.767 − 1,070.515) / 1,346.767 = 20.51%
```

**Cross-check against the primary 6-K (§0):** the fresh Q2 2026 quarter alone (not in this TTM window) posted revenue "KZT1.1 trillion (+15% YoY)" and net income "stable at KZT259 billion" — both roughly in line with the trailing quarters shown above (Q1 2026 net income was 249.394B), supporting that this TTM window, while one quarter stale, is not stale in a way that materially misstates the company's current run-rate.

### 3.2 Annual figures, FY2022–FY2025 (from `t.financials`/`t.cashflow`), KZT Billions — **the central finding of this session**

| FY | Revenue | Gross Margin | Net Margin | CapEx | CapEx/Rev | FCF | Net Income | **FCF/NI** |
|---|---|---|---|---|---|---|---|---|
| 2022 | 1,254.208 | 69.41% | 46.65% | 59.468 | 4.74% | 961.516 | 585.026 | **164.4%** |
| 2023 | 1,890.290 | 64.46% | 44.51% | 50.257 | 2.66% | 1,055.871 | 841.351 | **125.5%** |
| 2024 | 2,520.927 | 62.34% | 41.24% | 95.726 | 3.80% | 486.166 | 1,039.739 | **46.76%** |
| 2025 | 4,027.824 | 47.38% | 26.64% | 182.513 | 4.53% | 491.098 | 1,073.177 | **45.76%** |

```
Revenue 3yr CAGR (FY2022 -> FY2025) = (4,027.824 / 1,254.208)^(1/3) − 1 = 47.54%
```

**Two structural findings, both material to this session's conclusion:**

1. **Gross margin has compressed sharply and consistently every year** — 69.4% -> 64.5% -> 62.3% -> 47.4% over FY2022–FY2025. This is a genuine, multi-year, **contracting** (not expanding) margin trend. The quality-scoring.md formula has no explicit penalty for margin contraction (only a +10 bonus for *expansion* while below 40%, not applicable here since GM is well above 40%), so it does not mechanically move the Margins sub-score beyond what the TTM level itself implies — but it is flagged here as a significant qualitative concern independent of the score formula. The most plausible driver, based on the primary-source evidence in §0: the January 2025 Hepsiburada (Türkiye e-commerce) consolidation and its lower-margin, still-scaling cost structure, compounded by the July 2026 Hepsi Bank acquisition.

2. **FCF/Net Income conversion has been below 70% for the two most recent consecutive completed fiscal years (FY2024: 46.76%, FY2025: 45.76%)** — this is a direct, live hit on quality-scoring.md's hard disqualifier: *"FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation."* Per the 2026-08-05 rolling-window clarification, the test is evaluated against "the most recently completed fiscal years available at the time of scoring" — FY2024 and FY2025 are exactly that window as of this session (FY2025 closed Dec 2025; FY2026 is not yet complete). **This condition is live and fires** — see §3.3 for the full investigation of whether a documented carve-out applies.

### 3.3 Investigating the FCF/NI shortfall — is there a documented growth-*capex* explanation?

**No.** CapEx is small and stable relative to revenue across every year shown (2.7%–4.7% of revenue) — even its largest year-over-year jump (FY2024→FY2025, +90.7% in absolute KZT terms) only moves it from 3.80% to 4.53% of revenue, nowhere close to explaining a swing of hundreds of billions of KZT between Net Income and FCF. Decomposing the FY2025 gap directly from `t.cashflow`:

```
FY2025 Net Income                              = 1,073.177B
FY2025 Operating Cash Flow                      =   673.611B   (already 399.6B below NI)
FY2025 CapEx                                    =  −182.513B
FY2025 Free Cash Flow                           =   491.098B
```

The **Operating Cash Flow ↔ Net Income gap (399.6B) is larger than the CapEx deduction itself (182.5B)** — CapEx is not the dominant driver. The dominant driver, from the annual cash-flow statement's working-capital lines: **`Change In Receivables` was −1,675.6B (FY2025) and −1,624.99B (FY2024)** — a large, sustained cash outflow — confirmed in the TTM window too (`Change In Receivables` = −1,483.9B, Q2'25–Q1'26). This is **loan-portfolio growth in the Fintech platform**, not capex: the same 2026-08-10 6-K explicitly discloses Fintech's "average net loan portfolio increased by 18% year-over-year" in Q2 2026 alone (§0), a well-documented, real, ongoing dynamic — new loans originated are a use of operating cash (an increase in a receivable asset) under IFRS/GAAP cash-flow classification, exactly analogous in spirit to how this framework already treats MercadoLibre's fintech-lending cash-flow dynamics (see the **Adjusted Free Cash Flow** glossary entry, sourced from MELI's 2026-07-10 Quality Score addendum) as a real, structural, non-capex distortion of the naive GAAP FCF figure for a fintech lender.

**Conclusion on the carve-out:** the FCF/NI shortfall is genuine, well-documented, and driven by a legitimate, growth-related use of cash (funding a rapidly growing loan book) — but quality-scoring.md's hard-disqualifier carve-out is written specifically and narrowly as **"a documented growth-*capex* explanation,"** and loan-portfolio growth is not capex under any standard accounting definition (it is a financial asset, not property/plant/equipment). **This session does not extend the carve-out by analogy** — doing so would be inventing a broader reading of an explicit, narrowly-worded rule rather than following it as written, which this framework's operating brief does not license an unattended session to do. **The hard disqualifier therefore fires as written.**

This is flagged explicitly as a candidate framework gap worth the user's attention: a "growth-lending" carve-out analogous to Upgrade 1's Owner-Earnings/growth-capex treatment, scoped specifically to regulated-lender/fintech subsidiaries with a documented, disclosed loan-portfolio-growth rate, would be a defensible, narrow extension — but that is a framework-authorship decision for the user to make deliberately and record in `decisions/`, not one this session makes unilaterally.

### 3.4 Other hard disqualifiers — checked, both pass

| Check | Value | Threshold | Result |
|---|---|---|---|
| Net Debt/EBITDA over threshold | **−0.248×** (net cash) — see §3.6 | disqualify if >2.5× (standard) | ✅ PASS, overwhelmingly |
| FCF-positive 3+ consecutive years | FY2023 (+1,055.9B), FY2024 (+486.2B), FY2025 (+491.1B) — all positive | disqualify if not | ✅ PASS |

### 3.5 Quality Score — full weighted computation (shown for transparency, per this framework's established practice of computing the full score even when a hard disqualifier fires — see the 2026-07-13 SPCX precedent)

```
PROFITABILITY (25% weight):
  Net Margin (TTM) = 24.95%   -> NetMargin_Component = clamp((24.95/30)x100) = 83.16
  ROIC (TTM) = 51.61%  (see §3.6)   -> ROIC_Component = clamp((51.61/30)x100) = 100.0 (saturates)
  Profitability_Score = (83.16 + 100.0) / 2 = 91.58   (no FCF-positivity cap — 3yr positive confirmed §3.4)

MARGINS (15% weight):
  Gross Margin (TTM) = 51.09%
  GrossMargin_Score = clamp((51.09/80)x100) = 63.87
  Trend bonus: not applicable (GM is well above the 40% threshold the +10 bonus requires, and is contracting, not
    expanding — see §3.2 finding 1). No modifier applied.

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2022->FY2025) = 47.54%
  Growth_Score(raw) = clamp((47.54/25)x100) = 190.1 -> clamp to 100.0 (saturates)
  TAM/pricing-power modifier: documented evidence exists (Türkiye market entry via Hepsiburada/Hepsi Bank; Kasper AI
    assistant launch; e-Commerce VAS revenue +49% CC YoY; e-Commerce 3P take rate +160bps YoY to 16.1% — all §0/§7) —
    +10 would apply but has no effect, already saturated at 100.0.
  Structural-deceleration modifier: Q2 2026 revenue grew "only" +15% YoY vs. FY2025's blended +59.8% YoY — a large
    apparent deceleration, but FY2025's blended rate is heavily inflated by the January 2025 Hepsiburada acquisition
    (which entered the YoY comparison base only partway through FY2025), making the two rates not like-for-like.
    Q2 2026 vs. Q2 2025 (both fully post-Hepsiburada) is a cleaner comparison, and 15% still reflects genuine,
    real growth, not a stall. Evidence for a *structural* (not base-effect-driven) deceleration is not clearly
    established here — no −10 modifier applied, though this is flagged as worth re-examining at the next full-year mark.
  Growth_Score = 100.0

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (Q1 2026 balance sheet / TTM EBITDA) = −0.248x  (see §3.6)
  BalanceSheet_Score = clamp(100x(1 − (−0.248)/4)) = 106.2 -> clamp to 100.0 (saturates)
  ⚠️ Caveat: Kaspi.kz operates a licensed banking subsidiary; `yfinance`'s "Total Debt" figure (borrowings/bonds) 
    appears to exclude customer deposits (consistent with its small scale — 411.6B KZT — against 11.1T KZT of 
    total assets), the same convention gap this framework has already flagged qualitatively for JPM/C/SCHW's CET1 
    ratios being more meaningful than a standard Net Debt/EBITDA gate for a depository institution. Computed per 
    the framework's standard formula since no bank-specific alternative is defined here; flagged, not silently 
    substituted.

MOAT SIGNAL (15% weight):
  Market share stable or growing: TRUE — cited (independent research write-ups, not an official industry-data 
    provider: ~65% Kazakhstan digital-payments share, ~77% e-commerce share; company's own Q2 2026 release confirms 
    continued volume growth — Marketplace GMV +15% CC, Payments TPV +13% YoY — §7).
  Brand premium (pricing power): TRUE — e-Commerce 3P take rate +160bps YoY to 16.1% with purchases-per-consumer 
    *increasing* (11.6 -> 15.8), i.e. monetization rose without an observable volume/engagement tradeoff (§0/§7).
  Network effect: TRUE — documented two/three-sided Super App marketplace mechanism (merchants + consumers + 
    Fintech), cited by independent competitive analysis and consistent with the company's own "ecosystem" framing.
  Switching costs: TRUE — 77 monthly transactions per active consumer (company-disclosed, §0), reflecting deep 
    Super App embeddedness across payments/banking/e-commerce/government services in a single app.
  Scale cost advantage: FALSE — available third-party evidence is mixed/contradicting rather than supportive: a 
    cited competitive analysis notes rival Wildberries undercuts Kaspi's own Marketplace take rate (5-10% vs. 
    Kaspi's 9-10%) while growing share faster in e-commerce specifically — no clean cost-per-unit citation 
    supports a Kaspi cost advantage over this competitor.
  Moat_Score = (4/5) x 100 = 80.0

FCF QUALITY (10% weight):
  FCF/NI (TTM) = 65.03%   (see §3.1's TTM cashflow figures)
  FCFQuality_Score = clamp(((0.6503 − 0.40)/0.60)x100) = 41.71

QUALITY SCORE = 91.58x0.25 + 63.87x0.15 + 100.0x0.20 + 100.0x0.15 + 80.0x0.15 + 41.71x0.10
             = 22.895 + 9.5805 + 20.000 + 15.000 + 12.000 + 4.171
             = 83.6 (83.6465, rounds to 83.6)
```

**Weighted Quality Score = 83.6 / 100.0 — would clear the 80.0+ gate on the weighted average alone.**

**But the hard disqualifier identified in §3.3 (FCF/NI conversion <70% for FY2024 and FY2025, no documented growth-capex explanation) fails the gate regardless of the weighted score, per quality-scoring.md's explicit rule: *"A weighted average can't average away an outright balance-sheet or cash-flow-quality failure."*** This is precisely the scenario the hard-disqualifier mechanism exists to catch.

### 3.6 ROIC and Net Debt/EBITDA computation detail (Q1 2026 balance sheet)

```
Total Debt (Q1 2026)   = 411.639B KZT
Cash & Equivalents     = 797.075B KZT
Total Equity           = 2,775.068B KZT
Net Debt = 411.639 − 797.075 = −385.436B KZT   (net cash)
Net Debt/EBITDA = −385.436 / 1,555.584 (TTM EBITDA) = −0.248x

Invested Capital = Total Debt + Total Equity − Cash = 411.639 + 2,775.068 − 797.075 = 2,389.632B KZT
NOPAT = TTM Operating Income x (1 − eff. tax rate) = 1,551.396 x (1 − 20.51%) = 1,233.17B KZT
ROIC = 1,233.17 / 2,389.632 = 51.61%
```

Sanity check: `yfinance`'s `.info` field `returnOnEquity` (46.75%) is in the same broad range as this session's independently-computed ROIC (51.6%) — both very high, consistent with a historically strong-margin, net-cash business, even after the FY2025 margin compression. Unlike `grossMargins` (§2.2), this particular `.info` field does not appear to be materially wrong — cited only as a rough cross-check, not used as a scored input.

---

## 4. Gate Result — Phase 02 / Composite Score / Order Setup NOT computed

**Per quality-scoring.md: "A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all... Below 80.0 [or if a hard disqualifier fires], stop — don't proceed to valuation, regardless of how cheap the stock looks."**

KSPI's hard disqualifier (§3.3) fires. **This session stops here.** The Rate Environment Gate, the full Phase 02 valuation score (FCF Yield, EV/EBIT, Forward PE, PEG), the Composite Score, and the fair-value/order-setup work (blended FV, buy price, sell target, stop loss, R/R, position size) are **not computed** — doing so would be inconsistent with the gate's explicit design, and would require additional FX-conversion and forward-EPS work that isn't needed for a session that stops here regardless of the answer.

**For context only, not used in any calculation above:** KSPI's Nasdaq ADR has traded only since 19 January 2024 (~2.6 years, well under 20 quarters/5 years of price history) — had this session reached Phase 02, the Forward PE sub-score would have used the **no-history fallback (50.0, flagged)** per valuation-scoring.md, since a 5-year historical PE range/average cannot be reconstructed from the available trading history.

---

## 5. Recommendation

# **PASS — Quality Score gate FAILS (hard disqualifier: FCF/Net Income conversion below 70% for FY2024 and FY2025, both consecutive completed fiscal years, without a documented growth-*capex* explanation). Do not proceed to valuation scoring or order setup. This is a valid, expected stopping point per quality-scoring.md, not a data gap or an incomplete evaluation.**

KSPI's weighted Quality Score (83.6) would comfortably clear the 80.0+ gate on its own — the business itself shows excellent profitability (TTM ROIC 51.6%, TTM Net Margin 24.9%), very high revenue growth (47.5% 3yr CAGR), a deeply net-cash balance sheet, and a credible 4-of-5 Moat Signal read. **The disqualifying issue is specifically cash-conversion quality**: FCF has trailed Net Income by more than half in each of the last two fiscal years, driven by a real and well-documented — but non-capex — cause (funding rapid Fintech loan-portfolio growth, +18% YoY as of the fresh Q2 2026 print). Quality-scoring.md's hard-disqualifier carve-out is written narrowly around growth-*capex*, and this session does not stretch that language to cover loan-portfolio growth without an explicit framework decision authorizing it — flagged in §3.3 as a genuine candidate for the user to consider adding to the framework in a future `decisions/` entry, not something this session decides unilaterally.

Separately and independently, Kaspi's gross margin has compressed sharply and consistently for four straight fiscal years (69.4% -> 47.4%) — not itself a hard disqualifier under the current formula, but a real structural trend worth the user's attention regardless of how the FCF/NI question is eventually resolved.

**No position opened. Nothing to log in `decisions/`** (per task instructions, a `decisions/` entry is only required if a position is actually opened).

---

## 6. Watchlist / Stale-Score Housekeeping

- `watchlist/not-in-portfolio/KSPI/KSPI-2026-08-10.md` created — first-ever entry for this ticker (see §7).
- No stale-score banner or `watchlist/STALE.md` row to clear — this is a first entry, computed fresh under the current (2026-06-29) methodology from the outset.

---

## 7. Next Review Trigger

- **Kaspi.kz's next full-fiscal-year close (FY2026, expected to report ~February 2026)** is the single highest-value re-check: it will replace the rolling FY2024/FY2025 disqualifying window with FY2025/FY2026, and will show whether the FCF/NI ratio (i) recovers as loan-portfolio growth normalizes, or (ii) stays depressed, reinforcing the case that this is a structural, not transient, feature of the business's current growth phase.
- **Q3 2026 earnings** (Kaspi's historical cadence points to a November 2026 release) — will also fill the Q2 2026 balance-sheet/cash-flow gap flagged in §2.3, allowing a fully up-to-date TTM window.
- **A framework decision on whether a "growth-lending" carve-out (analogous to growth-capex) should be added** for regulated-lender/fintech-subsidiary businesses — flagged in §3.3/§5 for the user's consideration; if adopted, this ticker would warrant an immediate re-score under the revised rule (which would very plausibly clear the gate at 83.6).
- Continued gross-margin trend (§3.2 finding 1) — worth watching whether FY2026 stabilizes or continues compressing.
- Any standard Rule 9 trigger: guidance revision, management change, material M&A (beyond the already-disclosed Hepsi Bank acquisition), macro shift, or a >15% unexplained price move.

---

## 8. Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. New terms added this session (Kaspi.kz/Kazakhstan-fintech-specific vocabulary not previously needed by this framework): **BNPL**, **Cost of funding**, **Cost of risk**, **EGM**, **NPL ratio**, **Super App**, **Take rate**.

| Term | Meaning |
|---|---|
| **ADR / ADS (American Depositary Receipt / Share)** | A US-exchange-listed security representing shares of a non-US company; KSPI = 1 ADS representing 1 Kaspi.kz ordinary share. |
| **BNPL (Buy Now, Pay Later)** | A point-of-sale installment-credit product; one of the loan types inside Kaspi's Fintech portfolio. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure — shown this session to be a small, stable share of Kaspi's revenue (2.7%-4.7%), and specifically *not* the driver of its FCF/Net Income shortfall (§3.3). |
| **Cost of funding** | The average interest rate a lender pays on deposits/borrowings that fund its loan book; Kaspi's rose 150bps YoY to 14.5% in Q2 2026. |
| **Cost of risk** | A lender's loan-loss provisioning expense as a % of its average loan portfolio (forward-looking); Kaspi's was 0.7% in Q2 2026. |
| **EGM (Extraordinary General Meeting)** | A shareholder meeting called outside the regular annual cycle; Kaspi called one for 9 September 2026 to approve its proposed dividend increase. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value / EV divided by EBIT — not computed this session (Phase 02 not reached). |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income — the central finding of this session (§3.2/§3.3): KSPI's FCF/NI fell to 46.76% (FY2024) and 45.76% (FY2025), triggering the hard disqualifier. |
| **Form 6-K** | A furnished report foreign private issuers file with the SEC — this session's trigger source (Kaspi.kz's own Q2 2026 6-K, filed 2026-08-10). |
| **Form 20-F** | The annual report foreign private issuers file with the SEC (Kaspi's equivalent of a 10-K). |
| **Forward PE** | Price ÷ forward-looking expected EPS — not computed this session; would have used the no-history fallback (§4) had Phase 02 been reached. |
| **GDR (Global Depositary Receipt)** | A non-US-market depositary receipt structure — not KSPI's structure (KSPI is a US-listed ADR), noted only to distinguish it from other frameworks-covered tickers that do use GDRs. |
| **GMV (Gross Merchandise Volume)** | Total dollar value of transactions processed through a marketplace platform before the platform's own take rate; Kaspi's e-Commerce GMV grew 28% YoY (constant currency) in Q2 2026. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of its weighted score; the FCF/NI conversion disqualifier fired for KSPI this session (§3.3). |
| **IFRS (International Financial Reporting Standards)** | The accounting standard Kaspi.kz (and most non-US filers) use, as opposed to US GAAP. |
| **Invested Capital** | Debt + Equity − Cash, the ROIC denominator. |
| **Moat** | A durable competitive advantage; scored 80.0 (4 of 5 signals) for KSPI this session. |
| **Net Debt/EBITDA** | This framework's primary balance-sheet-risk gate; KSPI's is −0.248× (net cash), though flagged with a bank-subsidiary caveat (§3.5). |
| **Net Margin** | Net Income ÷ Revenue; TTM 24.95% for KSPI. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate). |
| **NPL (Non-Performing Loan) ratio** | The % of a lender's loan book that is significantly delinquent/in default; Kaspi's was 7.0% in 6M 2026. |
| **PEG ratio** | PE ÷ earnings growth rate — not computed this session. |
| **Quality Score** | This framework's 0.0-100.0 continuous score; 80.0+ required (plus no hard disqualifier) to proceed to Phase 02. KSPI's weighted score was 83.6 but the gate still fails on the hard disqualifier. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-score check comparing Earnings Yield to the 10-Year Treasury; not reached this session. |
| **ROIC** | Return on Invested Capital; 51.61% for KSPI this session (TTM, Q1 2026 balance sheet). |
| **Rule 0 / Rule 9** | This framework's standing instructions: always fetch live price first; force re-valuation on a fundamental trigger event (earnings, in this case). |
| **Super App** | A single app bundling multiple consumer services (payments, e-commerce, lending, etc.); Kaspi's core business-model term, cited as the basis for its network-effect/switching-cost Moat Signals. |
| **Take rate** | The % of gross transaction value a platform keeps as revenue; Kaspi's e-Commerce 3P take rate rose to 16.1% in Q2 2026. |
| **TAM** | Total Addressable Market. |
| **Total Debt** | Borrowed funds/bonds — for a company with a banking subsidiary like Kaspi, this figure appears to exclude customer deposits (§3.5 caveat). |
| **TPV (Total Payment Volume)** | Total dollar value of payments processed through a fintech platform; Kaspi's Payments TPV grew 13% YoY in Q2 2026. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results — this session's TTM window (Q2 2025-Q1 2026) is one quarter behind the freshest available headline data, per the data-availability gap in §2.3. |


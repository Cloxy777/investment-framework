# NEW POSITION — KO (The Coca-Cola Company)

**Date:** 2026-07-28
**Task type:** NEW POSITION
**Trigger:** Telegram-scan (Routine 6) — top post on t.me/FinnInvestChannel (#3004, ~18:42 UTC 2026-07-28) reporting Coca-Cola's Q2 2026 earnings beat and Coca-Cola Zero Sugar revenue growth. KO had no existing watchlist entry ([watchlist/not-in-portfolio/KO/](../watchlist/not-in-portfolio/KO/), [watchlist/in-portfolio/KO/](../watchlist/in-portfolio/KO/) both empty prior to this session) and is not a current holding ([portfolio/holdings.md](../portfolio/holdings.md) — not present) — per `/telegram-scan`'s decision rule, "no watchlist entry exists at all → `/new-position`."
**10Y US Treasury yield:** 4.62% (2026-07-28)

**Per CLAUDE.md Rule 0 and the operating brief: the Telegram post's text was used only as the trigger.** Every financial figure below was independently fetched from IBKR (live price) and Coca-Cola's own SEC filings / earnings releases (via Yahoo Finance's underlying data API and stockanalysis.com as an aggregator/cross-check), never from the Telegram post's framing.

---

## 0. Data-sourcing note (technical substitution, not a data gap)

The framework's documented `yfinance` workflow ([valuation-scoring.md](../framework/valuation-scoring.md)) failed in this session: `yfinance`'s `curl_cffi` HTTP backend does browser-TLS-fingerprint impersonation that is incompatible with this session's TLS-terminating egress proxy (`SSLError: Recv failure: Connection reset by peer`, reproducible even with the proxy's CA bundle correctly set). Plain `curl`/`requests` through the same proxy worked fine (confirmed via a direct probe returning HTTP 429 from Yahoo, i.e. a real, non-proxy-blocked round trip).

**Substitution used instead (same underlying data, different HTTP client):**
- **Live price (Rule 0):** IBKR MCP `get_price_snapshot` — the framework's own primary broker-data source, unaffected by this issue.
- **Company fundamentals:** Yahoo Finance's underlying JSON API (`query1/query2.finance.yahoo.com`), hit directly via Python `requests` with a browser `User-Agent` and a fetched crumb/cookie — the exact same data `yfinance` itself would return, just via a proxy-compatible client. Free-tier access capped annual history at 4 fiscal years and quarterly at 5 quarters (matching the caveat already documented in valuation-scoring.md for `yfinance`'s free tier).
- **5-year PE range / TTM cross-checks:** stockanalysis.com (a financial-data aggregator sourcing from the same SEC filings), used to fill the gap where Yahoo's free API capped history short of 5 years, and as an internal-consistency cross-check (e.g. its FCF yield and P/FCF figures invert to the same number).
- **Q2 2026 earnings figures, one-off cash-flow items, and moat evidence:** primary sources — Coca-Cola's own investor-relations press release/8-K and independent third-party sources (Interbrand, Euromonitor-derived reporting), verified via WebSearch, never the triggering Telegram post.

No required Quality Score input was missing or invented as a result of this substitution — every number below is real and sourced. One **methodology cross-check discrepancy** is flagged explicitly in §2 (ROIC) rather than silently resolved.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price** | **$88.15** | IBKR `get_price_snapshot`, contract_id 8894 (NYSE:KO), last trade ts 2026-07-28 |
| Day change | +$4.08 / **+4.85%** | IBKR (Yahoo's independent feed shows +$4.20 / +5.00% off a $84.07 prior close — same move, small feed-timing difference) |
| Bid / Ask | $87.88 / $88.15 | IBKR |
| 52-week low | $64.45 | IBKR `misc_statistics` |
| 52-week high (pre-today) | $85.67 | IBKR `misc_statistics` (stale field — see below) |
| **Today's intraday high** | **$90.22** | Yahoo Finance (regularMarketDayHigh) — a new 52-week (and likely all-time) high set today, not yet reflected in IBKR's `misc_statistics` 52w-high field, which is computed on a lag |
| YTD change | +26.95% | IBKR |
| Analyst mean target | $88.30 (23 analysts, consensus "Buy") | Yahoo `financialData` |

The +4.85–5.00% move is the market's reaction to the Q2 2026 earnings release (see §5). **Note:** I did **not** independently verify the Telegram post's specific framing ("best performance since 2009") — I confirmed today's ~+5% move via IBKR and Yahoo directly, but have not sourced or scored the "since 2009" comparison itself, consistent with Rule 0 (never treat the post's text as data).

---

## 2. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md))

### Hard disqualifiers — checked first

| Disqualifier | Result | Evidence |
|---|---|---|
| Not FCF-positive for 3+ consecutive years | **Does not fire** | FCF positive every year FY2022–FY2025 and TTM: $9.53B, $9.75B, $4.74B, $5.30B, $14.30B (TTM) — never negative. |
| Net Debt/EBITDA over applicable threshold (2.5× standard) | **Does not fire** | TTM Net Debt/EBITDA = $27.17B / $15.89B = **1.71×** (well under 2.5×; KO is not an asset-light payment-network/financial, so the standard denominator applies, not the Upgrade 5 override). |
| FCF/Net Income conversion ratio <70% for 2+ consecutive years, no documented growth-capex explanation | **FIRES** | See below. |

**FCF/NI ratio by fiscal year** (FCF and NI both from Coca-Cola's filed cash-flow/income statements, via Yahoo fundamentals-timeseries):

| FY | FCF ($M) | Net Income ($M) | FCF/NI |
|---|---|---|---|
| 2022 | 9,534 | 9,542 | 99.9% |
| 2023 | 9,747 | 10,714 | 91.0% |
| **2024** | **4,741** | 10,631 | **44.6%** |
| **2025** | **5,296** | 13,107 | **40.4%** |
| TTM (through Q2 2026) | 14,297 | 14,316 | 99.9% (informational — see note) |

FY2024 and FY2025 are two **consecutive fiscal years** below 70%. Both causes are documented, real, and independently verified — but **neither is a growth-capex explanation**, the only carve-out quality-scoring.md's hard-disqualifier text recognizes:
- **FY2024:** a ~$6.23B working-capital swing (inventory/receivables timing in certain international markets), vs. only $846M the prior year — a working-capital timing item, not capex.
- **FY2025:** a **$6.1 billion contingent-consideration (earn-out) payment** to fairlife LLC's founders in Q1 2025, tied to fairlife's 2020 acquisition — a one-time, GAAP-classified *operating* cash outflow, not capex. (Company-disclosed: full-year 2025 FCF ex-this-payment was $11.4B, which alone would put FY2025 at ~87% conversion — comfortably above 70%. But the *reported*, GAAP figure is what the disqualifier text reads, and it is 40.4%.)

Per the same literal-carve-out standard applied in today's LITE and COHR sessions (growth capex specifically, no broader "any documented one-off" exception), **this disqualifier fires for KO.** The TTM figure (99.9%) looks fine only because the anomalous Q1 2025 quarter has since rolled out of the trailing-12-month window — it doesn't erase that FY2024 and FY2025, the two most recently *completed fiscal years*, both cleared below 70% on a GAAP basis.

**Result: hard disqualifier fires.** Per quality-scoring.md, this fails the company regardless of the weighted score below. The full weighted calculation is still shown in full per "no black-box outputs."

### Sub-score calculations

**Profitability (25% weight):**
```
Net Margin (TTM) = 28.56%   (Net Income $14,316M / Revenue $50,129M, TTM through Q2 2026 — stockanalysis.com, cross-checked against Yahoo's profitMargins field)
ROIC (TTM) = 20.41%          (stockanalysis.com; NOPAT/Invested Capital, exact denominator not fully disclosed by source)

NetMargin_Component = clamp((28.56/30)×100, 0, 100) = 95.2
ROIC_Component       = clamp((20.41/30)×100, 0, 100) = 68.0
Profitability_Score  = (95.2 + 68.0) / 2 = 81.6
```
No FCF-positive-3yr cap applies (KO clears that check every year — see disqualifier table above).

**⚠️ Cross-check discrepancy flagged (not resolved, per "never invent/estimate"):** recomputing ROIC from primary components — EBIT (TTM) $14,854M × (1 − 16.41% effective tax rate) = NOPAT $12,418M, divided by FY2025 year-end book Invested Capital $77,661M (Yahoo `annualInvestedCapital`, most recent full-year figure available since a TTM invested-capital figure wasn't obtainable) — gives **15.99%**, notably lower than stockanalysis.com's 20.41%. The gap likely reflects a different invested-capital denominator (e.g. netting cash, an average rather than year-end base, or excluding KO's large equity-method bottler investments from "invested capital," which a stricter operating-ROIC calc typically would), not a data error — but I'm flagging rather than silently picking one. **This does not change the bottom-line conclusion:** using the lower 15.99% ROIC instead (ROIC_Component 53.3, Profitability_Score 74.25) still yields a Quality Score of ~55.8, and KO still fails the gate by a wide margin either way, and the hard disqualifier above fires independent of this number entirely.

**Margins (15% weight):**
```
Gross Margin (TTM) = 61.89%   ($31,024M / $50,129M, TTM — stockanalysis.com)
GrossMargin_Score = clamp((61.89/80)×100, 0, 100) = 77.4
```
3yr trend: FY2022 58.14% → FY2023 59.53% → FY2024 61.07% → FY2025 61.62% → TTM 61.89% — clearly, structurally expanding. No bonus applies (bonus is only for a company below the 40% static threshold that's improving; KO is already well above 40%).

**Growth (20% weight):**
```
Revenue 3yr CAGR (FY2022 → FY2025, GAAP reported) = ($47,941M / $43,004M)^(1/3) − 1 = 3.69%
Growth_Score (base) = clamp((3.69/25)×100, 0, 100) = 14.8
```
+10 documented TAM-expansion/pricing-power modifier applied: Coca-Cola's own Q2 2026 earnings release (businesswire.com/investors.coca-colacompany.com, 2026-07-28) documents Trademark Coca-Cola volume +5% (strongest quarterly growth in 17 years excluding pandemic recovery), Coca-Cola Zero Sugar +16% (accelerating from +13% in Q1 2026), price/mix +2% *without* volume loss (volume grew, didn't shrink — genuine pricing power, not just price hikes offsetting decline), and a raised FY2026 organic-revenue guidance (to ~5% from 4–5%) — real, cited, current-quarter evidence of demand strength, not inferred.
```
Growth_Score = 14.8 + 10 = 24.8
```
**Note on GAAP-reported vs. organic growth:** Coca-Cola's own Q2 2026 organic revenue growth was 6% (7% reported) — both non-GAAP/company-disclosed figures. Per this framework's "guidance/self-reported metrics are not scored" principle (same treatment as PepsiCo's "Core" EPS and Novo Nordisk's CER growth elsewhere in this framework), the **scored** Growth_Score input uses GAAP-reported, filed revenue (3.69% 3yr CAGR) — the organic/CER-basis growth is cited only as qualitative TAM-evidence feeding the +10 modifier, not substituted in as the scored base figure.

**Balance Sheet (15% weight):**
```
Total Debt (TTM) = $43.54B   Cash (TTM) = $16.37B   Net Debt = $27.17B   (stockanalysis.com TTM, post-Q2-2026)
EBITDA (TTM) = $15.89B
Net Debt/EBITDA = 27.17 / 15.89 = 1.71×
BalanceSheet_Score = clamp(100 × (1 − 1.71/4), 0, 100) = 57.2
```
(Standard /4 denominator — KO is not a payment network/asset-light financial, so the Upgrade 5 override doesn't apply.)

**Moat Signal (15% weight):**

| Signal | Result | Evidence (cited) |
|---|---|---|
| Market share stable/growing | **TRUE** | ~30% of global carbonated-soft-drink segment volume (Euromonitor-sourced reporting), sustained multi-decade category leadership; Q2 2026 Trademark Coca-Cola volume +5% — strongest in 17 years — shows share holding/expanding, not eroding. |
| Brand premium | **TRUE** | Interbrand's 2025 Best Global Brands: Coca-Cola ranked **#6 overall**, the highest-ranked beverage/CPG brand on the entire list. Q2 2026 price/mix +2% achieved *alongside* volume growth (not volume decline) — genuine pricing power, not just a price hike masking demand loss. |
| Network effect | **FALSE** | No documented two-sided-marketplace or user-growth-driven-value mechanism exists for a packaged-beverage manufacturer — not claimed. |
| Switching costs | **TRUE** | Coca-Cola's bottling-partner contracts grant exclusive territorial rights and are structured as perpetual (legacy) or 10-year, bottler-renewable-indefinitely (modern "participating bottler CBA") agreements across ~225 bottling partners — a documented, multi-decade lock-in mechanism that also limits competitors' shelf/cooler access at the retail level (cited via SEC 10-K bottling-agreement disclosures and independent reporting). |
| Scale cost advantage | **TRUE** | World's largest beverage distribution system; the bottler system's local-monopoly structure spreads fixed distribution costs over a very large volume base per territory, a documented mechanism (not just an assertion) for a structural per-unit cost advantage over smaller regional competitors. |

```
Moat_Score = (4/5) × 100 = 80.0
```

**FCF Quality (10% weight):**
```
FCF/NI ratio (FY2025, most recent complete fiscal year — same basis as the hard-disqualifier check above) = 40.4%
FCFQuality_Score = clamp(((0.404 − 0.40)/0.60) × 100, 0, 100) = 0.7
```
(For transparency: using the TTM figure instead — 99.9% — would give FCFQuality_Score ≈ 99.8. I've used the FY2025 basis for consistency with the disqualifier check above, since the TTM figure's apparent strength is an artifact of the anomalous Q1 2025 quarter having rolled out of the trailing window, not a genuine change in underlying cash-conversion quality.)

### Final Quality Score

```
Quality Score = (81.6 × 0.25) + (77.4 × 0.15) + (24.8 × 0.20) + (57.2 × 0.15) + (80.0 × 0.15) + (0.7 × 0.10)
              = 20.40 + 11.60 + 4.96 + 8.59 + 12.00 + 0.07
              = 57.6
```

**Quality Score: 57.6 / 100.0 — fails the 80.0+ gate**, by 22.4 points on the weighted score alone, **and** a hard disqualifier (FCF/NI conversion <70% for 2+ consecutive years, FY2024 and FY2025, no growth-capex explanation) fires independently. Both point to the same conclusion.

Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md): **this stops the evaluation here.** No Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is computed — same pattern as today's LITE and COHR sessions.

---

## 3. Appendix — valuation inputs already gathered (reference only, NOT a scored Phase 02 valuation)

Shown purely for completeness/transparency (operating-brief.md's "show every calculation" applies to what was computed, even when the gate stops further scoring) — **these numbers do not combine into a Valuation Score or Composite Score**, since KO never clears the Quality Gate that step is conditioned on:

| Metric | Value | Note |
|---|---|---|
| FCF Yield (TTM) | 3.79% | FCF $14.30B / Market cap ≈ $377.8B |
| EV/EBIT (TTM) | 27.25× | EV ≈ $405B / EBIT $14.85B |
| Forward PE | ~25.3× | $88.15 live price / $3.483 forward EPS consensus |
| 5yr fiscal-year-end PE (2021–2025) | Low 23.00× (FY2025) / High 29.05× (FY2022) / Avg 25.51× | stockanalysis.com annual PE-ratio table; a fiscal-year-end-snapshot proxy, not the full 20-quarter reconstructed series the methodology describes (Yahoo's free-tier API capped quarterly history at 5 quarters — see §0) |
| Fast Grower (PEG) eligibility | **No** | EPS growth has not exceeded 15% for 3+ consecutive years on a clean base (FY2022→2023 +12.8%, FY2023→2024 −0.4%, FY2024→2025 +23.6% but distorted by the fairlife-payment-year cash/tax dynamics) — PEG's 15% weight would redistribute to EV/EBIT (40% total) if scoring proceeded. |
| Dividend yield | 2.47–2.52% | IBKR / Yahoo, current |

---

## 4. Q2 2026 Earnings — independently verified context (Rule 9 relevance)

All figures below are from Coca-Cola's own Q2 2026 earnings release (businesswire.com / investors.coca-colacompany.com, published 2026-07-28) and independent reporting, fetched via WebSearch — **not** from the triggering Telegram post:

- **Net revenues:** $13.4B, **+7% reported / +6% organic** (organic = ex-FX, non-GAAP, cited as context only — not scored, see §2 Growth note)
- **EPS:** Reported EPS $1.03 (+16% YoY); Comparable (non-GAAP) EPS $0.97 (+11% YoY) — beat consensus by ~4.3% on EPS, ~1.8% on revenue
- **Unit case volume:** +5%; **Trademark Coca-Cola volume +5%**, the strongest quarterly growth in 17 years excluding the pandemic-recovery period
- **Coca-Cola Zero Sugar: +16%**, accelerating from +13% in Q1 2026, growth across all geographic segments — this is the specific figure the triggering Telegram post referenced; **independently confirmed here via Coca-Cola's own press release**, not taken on the post's word
- **Price/mix:** +2%; concentrate sales +4%
- Other brands: fairlife +18% (H1 2026), POWERADE +8%, Mr. Pibb +20%+ (post-relaunch)
- **FY2026 guidance raised:** organic revenue growth to ~5% (from 4–5%); comparable currency-neutral EPS growth to 7–8% (from 6–7%)
- Tailwinds cited by management: FIFA World Cup marketing campaign, broad-based consumer engagement

This is genuinely strong, real, verified operating performance — but it doesn't change the Quality Score outcome above, which turns on a **balance-sheet/cash-flow-quality structural check** (the FCF/NI hard disqualifier and the still-low 3yr revenue CAGR that predates this quarter), not on whether the most recent quarter was good. A single strong quarter is exactly the kind of signal Rule 9 flags for re-valuation, not a reason to override a structural gate — consistent with how this framework treats "price dropped/rose on an earnings beat" as context, not an independent trigger (operating-brief.md's action-table note: never act on price movement or a single quarter alone).

---

## 5. Recommendation

**PASS — watchlist only, do not enter a position.** Quality Score 57.6 fails the 80.0+ gate by a wide margin, and a hard disqualifier (FCF/Net Income conversion ratio <70% for 2 consecutive fiscal years, FY2024 and FY2025, without a documented growth-capex explanation) independently fires. No Composite Score exists to check against the Phase 03 action table, and no fair-value/order-setup work is produced, per [fair-value-methodology.md](../framework/fair-value-methodology.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md) (both gate that step on a passing Quality Score).

**Next review trigger:** re-score at KO's next quarterly earnings release (Q3 2026, expected mid-October 2026) to check whether (a) the FY2024/FY2025 FCF/NI shortfall pattern resolves once FY2026 closes as a full fiscal year without a similar one-off, and (b) whether the 3yr revenue CAGR improves as FY2023's comparatively soft year rolls out of the trailing window. Also re-score immediately on any Rule 9 fundamental trigger (guidance revision, M&A, management change, or a >15% unexplained move).

---

## Glossary

- **Contingent consideration (earn-out payment)** — the deferred, performance-tied M&A payment (here, Coca-Cola's $6.1B fairlife earn-out) whose GAAP operating-cash-flow classification is central to why the FCF/NI hard disqualifier fires for KO this session.
- **CAGR** — Compound Annual Growth Rate, used for KO's 3.69% 3-year revenue growth figure.
- **D&A** — Depreciation & Amortization.
- **EBIT** — Earnings Before Interest and Taxes (operating profit).
- **EBITDA** — EBIT plus Depreciation & Amortization; used in the Net Debt/EBITDA balance-sheet check.
- **EV/EBIT** — Enterprise Value ÷ EBIT, a standard valuation multiple (shown here for reference only, not scored).
- **FCF (Free Cash Flow)** — cash generated after running and maintaining the business; the FCF/Net Income conversion ratio is the deciding factor in this session's hard disqualifier.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company outright regardless of its weighted sub-score total; the FCF/NI conversion ratio disqualifier fires for KO.
- **Interbrand (Best Global Brands)** — the independent brand-valuation ranking (Coca-Cola #6 overall, 2025) cited as Moat Signal "brand premium" evidence.
- **Net Debt/EBITDA** — leverage ratio measuring years of cash profit needed to repay all debt; this framework's primary balance-sheet gate. KO's 1.71× comfortably clears the 2.5× standard threshold.
- **Organic revenue growth** — revenue growth excluding FX/M&A effects — a non-GAAP, company-disclosed figure cited as qualitative context (Q2 2026: +6%) but not the scored Growth input.
- **Owner Earnings** — Buffett's adjusted cash-flow measure; not applied to KO (Upgrade 1 only applies to Growth CapEx >30%-of-total names like MSFT/GOOGL/META/AMZN).
- **PEG ratio** — PE ÷ earnings growth; not applicable to KO, which doesn't meet the Fast Grower threshold.
- **Price/mix** — the portion of revenue growth from pricing/mix vs. unit volume; KO's Q2 2026 price/mix was +2%.
- **Quality Score** — this framework's 0.0–100.0 score (higher = better) gating eligibility for Phase 02 valuation scoring; KO scored 57.6, below the required 80.0+.
- **Rate Environment Gate / Rate Regime Modifier** — the mandatory pre-Phase-02 check comparing earnings yield to the 10Y Treasury; not reached this session since the Quality Gate stopped the evaluation first.
- **ROIC** — Return on Invested Capital; KO's ROIC carries a flagged cross-check discrepancy between sources (20.41% vs. a self-computed 15.99%) in this session.
- **TTM (Trailing Twelve Months)** — the most recent 12 reported months of results, as opposed to a fiscal-year figure; used throughout §2–3 for KO's post-Q2-2026 figures.
- **Treasury yield (10Y)** — the US government's 10-year borrowing rate (4.62% today), the Rate Environment Gate's benchmark (not reached this session).
- **Unit case volume** — Coca-Cola's own standardized volume metric (192oz-equivalent cases); +5% in Q2 2026, cited as Growth sub-score modifier evidence.

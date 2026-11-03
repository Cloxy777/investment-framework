# NEW POSITION — CAP (Capgemini SE) — 2026-11-03

**Task type:** NEW POSITION (manual `/new-position CAP`)
**Date:** 03 Nov 2026
**Result:** **Phase 01 FAIL — PASS, do not open a position.** Weighted Quality Score 27.8 (gate 80.0); a Net Debt/EBITDA hard disqualifier also fires on the framework's lease-inclusive basis (2.76× > 2.5×).
**Current portfolio weight:** 0% — not held. No prior watchlist/session coverage (first evaluation).
**Rate Gate / Phase 02 / Composite / order setup:** not computed — gate fails first (operating brief: stop and report).
**Currency:** Capgemini reports in **EUR** under IFRS; every figure below is EUR, no FX conversion needed.

## 0. Ticker resolution

"CAP" is ambiguous. IBKR `search_contracts("CAP")` returns: Capgemini SE (Euronext Paris/SBF, contract_id 29612147), Capgemini on SIX Swiss (EBS, 172603852), Capitea SA (Warsaw), and others. The only large, liquid, quality-screen-plausible match is **Capgemini SE, Euronext Paris** — used here (`yfinance` symbol `CAP.PA`). *Assumption — if a different CAP was meant, say so and rerun.*

## 1. Live price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price** | **€123.55** | IBKR `get_price_snapshot`, contract 29612147, `last` (feed status DELAYED) |
| Bid / Ask | €123.50 / €123.55 | same call |
| 52-wk range | €85.62 – €153.05 | same call (`misc_statistics`) |
| Cross-check | €123.50 | `yfinance` `currentPrice` |

Market cap = 165,252,200 shares × €123.55 = **€20,417M**.

## 2. Data sourcing — why `fetch_fundamentals` could not run

```
$ python -m scripts.fetch_fundamentals CAP.PA
ERROR: yfinance field missing from TTM EBIT: row 'EBIT' not found
```

`yfinance` returns **no quarterly statements** for CAP.PA (European issuers report half-yearly), so the script's 4-quarter TTM sums cannot run. Per the stop-and-ask rule nothing was estimated. Instead TTM was rebuilt from **primary filings**, the same method as the VOW3 (2026-09-04) session:

`TTM = FY2025 − H1 2025 + H1 2026`, from Capgemini's *Condensed interim consolidated financial statements, half-year ended June 30, 2026* (statements of financial position and cash flows; in the Universal Registration Document PDF on investors.capgemini.com) and the H1 / FY2025 press releases. Annual rows (FY2022–FY2025 revenue, gross profit, net income, FCF, SBC) from `yfinance`.

Sources: [H1 2026 results](https://investors.capgemini.com/en/publication/2026-h1-results/) · [FY2025 results](https://www.capgemini.com/news/press-releases/full-year-2025-results/) · [Q3 2026 revenues](https://www.capgemini.com/news/press-releases/q3-2026-momentum-drives-upgrade-in-capgeminis-2026-outlook/) · IBKR / `yfinance`.

### 2.1 TTM build (EUR M)

| Item | FY2025 | H1 2025 | H1 2026 | **TTM** |
|---|---|---|---|---|
| Revenue | 22,465 | 11,107 | 12,082 | **23,440** |
| Net profit, Group share | 1,601 | 724 | 498 | **1,375** |
| Operating profit (reported, after restructuring) | 2,199 | 976 | 878 | **2,101** |
| D&A incl. lease right-of-use + impairment | 698 | 350 | 414 | **762** |
| EBITDA (= operating profit + D&A) | | | | **2,863** |
| Income tax | 534 | 260 | 305 | **579** |
| Profit before tax (profit + tax) | 2,141 | 986 | 805 | **1,960** |
| Operating cash flow | 2,482 | 370 | 357 | |
| Capex (gross PP&E + intangibles) | 287 | 131 | 123 | |
| FCF = OCF − capex | 2,195 | 239 | 234 | **2,190** |
| Stock-based comp (SBC incl. employee ownership plan) | 266 (223 + 43) | 116 | 92 | **242** |
| Net outflows on Capgemini SE share transactions (buybacks) | 543 | (+1) | 325 | **869** |

Derived: net margin 1,375 / 23,440 = **5.866%**; effective tax 579 / 1,960 = 29.54%; NOPAT = 2,101 × (1 − 0.2954) = 1,480.

Balance sheet, 30 Jun 2026: borrowings 8,245 + 811 = 9,056; lease liabilities 842 + 280 = 1,122; **gross debt incl. leases 10,178**; cash & equivalents 2,279; **net debt incl. leases 7,899**; total equity 11,640. Invested capital = 10,178 + 11,640 − 2,279 = **19,539**. ROIC = 1,480 / 19,539 = **7.576%**.
Net debt/EBITDA = 7,899 / 2,863 = **2.759×** (lease-inclusive, cash-and-equivalents only — the `yfinance` "Total Debt − Cash" convention `fetch_fundamentals` uses).

Annual (`yfinance`): gross margin FY2025 6,075 / 22,465 = **27.04%**; revenue FY2022 21,995 → FY2025 22,465, 3-yr CAGR **0.707%**; FCF/NI FY2022–FY2025 (oldest first) **143.95%, 136.26%, 132.32%, 137.10%**; FCF positive all 4 years.
TTM FCF/NI = 2,190 / 1,375 = 159.3%; (FCF − SBC) / NI = (2,190 − 242) / 1,375 = **141.67%**; SBC/FCF 11.05%; SBC yield 1.19% of market cap; FCF yield = 2,190 / 20,417 = 10.73%; gross buyback yield 4.26%.
EV = 20,417 + 10,178 − 2,279 + 25 (non-controlling interests) = 28,341 → **EV/EBIT 13.49×**. Forward PE = 123.55 / €13.11 (FY2026E consensus, `yfinance` `0y`) = **9.42×** — but consensus is on Capgemini's *normalised* EPS (see Glossary); trailing GAAP-basis PE ≈ 15×.

⚠️ **Data caveats (flagged, not estimated):**
1. TTM built from half-year filings, not quarterly data; H1 SBC is the cash-flow-statement "expenses relating to share based compensation" line.
2. `yfinance` FCF excludes lease repayments (€293M TTM = 296 − 147 + 144) and net interest; Capgemini's own *organic FCF* (guided €1.8–1.9B for FY2026; H1 2026 only €37M) is stricter. Even after leases, TTM FCF/NI ≈ 138% — the conversion test is not at risk.
3. Operating profit used as EBIT is *after* Fit-for-Growth restructuring (other operating expense €784M FY2025, €628M H1 2026). Pre-restructuring operating margin TTM = 2,983 − 1,377 + 1,506 = 3,112 (13.3%) — context only, not scored (restructuring recurred two years running).
4. Net debt definition decides the disqualifier: Capgemini's own net debt (excl. leases, incl. cash-management assets) = 6,454 → 6,454 / 2,863 = **2.25×** passes; lease-inclusive per framework convention = **2.76×** fails. Disclosed as a judgment, see §3.
5. 5-yr PE history unavailable (`pe_mode: none` — no reconstructable TTM EPS); cycle-peak and value-trap flags `UNKNOWN` (no quarterly EPS).
6. IBKR price feed is delayed; no tick-exact price needed since no order is placed.

### 2.2 Advisory flags (no score effect)

```
Advisory flags (no score effect; † = uncalibrated placeholder threshold)
  cycle_peak             UNKNOWN                EPS TTM now or 1y ago unavailable
  multiple_ceiling       NONE                   forward PE 9.4, EPS growth 9.7%
  value_trap_candidate   UNKNOWN                forward PE or trailing EPS growth unavailable
```
Handling: `UNKNOWN` ×2 recorded as data gaps (no quarterly EPS series for a half-year reporter); `multiple_ceiling` NONE. SBC/FCF 11% — mild, no flag.

## 3. Phase 01 — Quality Score

**Moat evidence:** none credited. No cited market-share series, pricing-power data, retention/renewal data or cost-per-unit gap was sourced this session; "never mark a signal true without a cited source". Operating margin is flat (13.3% FY2025 vs FY2024; H1 2026 12.5%, +0.1pt). TAM / deceleration modifiers: neither applied (growth is acquisition-led — WNS, Cloud4C closed Q4 2025 — with ~5pt inorganic contribution; no cited organic TAM source).

### 3.1 Script output — base case (lease-inclusive net debt, framework convention) — verbatim

```
# FAILS GATE
Reason: Net Debt/EBITDA 2.759x exceeds the 2.5x threshold
```

### 3.2 Script output — sensitivity: Capgemini's own net debt (leases excluded, 2.254×) so the weighted score is shown — verbatim

```
## Quality Score

**Profitability (25%)**
NetMargin_Component = clamp((5.866/30)x100) = 19.55
ROIC_Component = clamp((7.576/30)x100) = 25.25
Profitability_Score = (19.55 + 25.25) / 2 = 22.40
**Margins (15%)**
GrossMargin_Score = clamp((27.042/80)x100) = 33.80
**Growth (20%)**
Growth_Score = clamp((0.707/25)x100) = 2.83
Growth_Score (final, clamped) = 2.83
**Balance Sheet (15%)**
BalanceSheet_Score = clamp(100x(1 - 2.254/4)) = 43.65
**Moat Signal (15%)**
Moat_Score = (0/5) x 100 = 0.00   [all five signals False — evidence rows as above]
**FCF Quality (10%)**
FCFQuality_Score = clamp(((1.4167 - 0.40)/0.60)x100) = 100.00  [ratio = (FCF - SBC)/NI]
**Quality Score — Final**
Quality Score = (22.40x0.25) + (33.80x0.15) + (2.83x0.20) + (43.65x0.15) + (0.00x0.15) + (100.00x0.10)
= 27.784 -> rounds to 27.8

# Quality Score = 27.8 — FAILS the 80.0+ gate
```

### 3.3 Robustness

| Scenario | Net Debt/EBITDA | Moat | Quality Score | Gate |
|---|---|---|---|---|
| Base (lease-inclusive) | 2.759× | 0/5 | DQ fires (weighted 25.9 = 22.40×.25 + 33.80×.15 + 2.83×.20 + 31.03×.15 + 0 + 100×.10) | **FAIL** |
| Capgemini net debt (ex-leases) | 2.254× | 0/5 | **27.8** | **FAIL** |
| Best case: ex-leases **and** all 5 moat signals credited (hypothetical) | 2.254× | 5/5 | 42.8 | **FAIL** |

The fail is **not** a knife-edge on the lease or moat judgment: even the unrealistically generous case is ~37 points below the gate. The binding weaknesses are structural to the scoring formulas: net margin 5.9% (vs a 30% full-credit level), ROIC 7.6%, 0.7% 3-yr revenue CAGR (acquisition-driven growth is not in the FY2022–FY2025 base), gross margin 27%. Strengths: FCF conversion (>130% for 4 straight years) and a modest ~11% SBC/FCF.

## 4. Recommendation

# **PASS. Do not open a position.**

Phase 01 FAIL (Quality Score 27.8 vs 80.0+ gate; plus the lease-inclusive Net Debt/EBITDA disqualifier). No Rate Environment Gate, Phase 02 valuation, Composite Score, fair-value work or order setup was run — per the operating brief, none of it is meaningful for a name that fails the gate. Cheap-looking multiples (forward PE 9.4× on normalised EPS, FCF yield 10.7%) are not a trigger: the framework acts only on documented triggers, and the multiples sit on an adjusted-earnings basis that excludes recurring restructuring.

## 5. Portfolio rebalancing summary

N/A — not a holding; nothing opened; no `decisions/` entry.

## 6. Next review trigger

- FY2026 results (scheduled 2027-02-16) — standard Rule 9 re-check; WNS-driven growth enters the 3-yr CAGR only gradually, and Fit-for-Growth cash costs (≈ +€200M restructuring outflow in 2026) weigh on net debt.
- Net debt: end-2026 net debt/EBITDA below 2.5× on the lease-inclusive basis would clear the disqualifier, but the weighted score would still need a ~50-point improvement — realistically a multi-year path.
- Q3 2026 revenue (2026-10-30, €6,073M, +11.7% constant-currency; FY guidance raised to +9.0–9.5%) is operationally positive but does not touch the margin/ROIC/CAGR drivers.
- Any >15% unexplained price move, management change or material M&A (Rule 9).
- Data gap to close if re-evaluating: quarterly EPS history and 5-yr PE range for a non-quarterly reporter.

---

## Glossary

Terms from [framework/glossary.md](../framework/glossary.md) (new terms added there this session are marked *new*).

- **Cash management assets** *(new)* — Capgemini's short-term financial investments it nets into its own net debt; excluded here (conservative).
- **Composite Score** — blend of Quality and Valuation scores; not computed (gate failed).
- **Euronext Paris (SBF)** *(new)* — Paris exchange where CAP trades, in EUR.
- **EV/EBIT** — enterprise value ÷ operating profit; 13.49×.
- **FCF / FCF yield** — free cash flow (operating cash flow − capex); FCF ÷ market cap, 10.73%.
- **Fit-for-Growth** *(new)* — Capgemini's restructuring programme booked in "other operating expenses".
- **Forward PE** — price ÷ next-year consensus EPS; 9.42× on normalised EPS.
- **Hard disqualifier** — a condition failing a company regardless of weighted score; Net Debt/EBITDA > 2.5× fires on the lease-inclusive basis.
- **IFRS 16** *(new)* — lease accounting that puts leases in debt; the reason net debt basis matters.
- **Moat** — durable competitive advantage; 0/5 credited (no cited evidence).
- **Net Debt/EBITDA** — leverage ratio; 2.76× lease-inclusive, 2.25× on Capgemini's own definition.
- **Normalized EPS (Capgemini)** *(new)* — company-adjusted EPS excluding restructuring and amortisation.
- **NOPAT / ROIC** — operating profit after tax; NOPAT ÷ invested capital (7.58%).
- **Organic free cash flow (Capgemini)** *(new)* — company's stricter FCF incl. leases and interest.
- **Quality Score** — 0–100 quality grade; 80.0+ gate; CAP scores 27.8.
- **Rule 0** — always fetch a live price/primary data first.
- **SBC (stock-based compensation)** — shares granted to staff as pay, treated as a cost: €242M TTM.
- **TTM** — trailing twelve months; rebuilt here as FY2025 − H1 2025 + H1 2026.

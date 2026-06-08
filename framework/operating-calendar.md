# Routine Operating Calendar

## Schedule at a Glance

| Frequency | Task | Trigger | Claude Needed? |
|-----------|------|---------|----------------|
| Daily (market days) | News & alert scan | Price move >5% intraday | No — human monitors |
| Weekly (Monday) | Earnings calendar check | Calendar-based | No — human prep |
| **After every earnings release** | **Quarterly Re-score** | Company reports earnings | **Yes — core task** |
| **Quarterly (Jan, Apr, Jul, Oct)** | **Rate Environment Gate update** | Quarter begins | **Yes** |
| **Annually (January)** | **Rate-Normalised PE recalc** | Year begins | **Yes** |
| **Annually (January)** | **Full universe re-screen** | Year begins | **Yes** |
| **Event-triggered** | **Rule 9 model refresh** | See triggers | **Yes** |
| **Event-triggered** | **Short thesis engagement** | Short report published | **Yes** |
| **Event-triggered** | **Turnaround sub-gate review** | Every 2 quarters after entry | **Yes** |

> **"Full universe re-screen" = one full pass through the [global coverage matrix](screening-coverage-log.md).** Run `/screen` slice by slice (it self-selects the next least-recently-covered region/sector when called with no argument) until every row shows a current-year "Last screened" date — that's what makes the January target "global, not just US large-cap" in practice rather than in name only.

---

## Quarterly Post-Earnings Re-Score (Core Claude Task)

**When:** Within 3 business days of each holding's earnings release.
**Session type:** `RESCORE`

**Data to pull before the session:**

| Metric | Where to Get It |
|--------|-----------------|
| FCF (or Owner Earnings for MSFT/META/GOOGL/AMZN) | TIKR — Cash Flow statement |
| EV/EBIT (trailing and forward) | TIKR or Koyfin |
| Forward PE | Koyfin or Finviz |
| 10-year average PE | Macrotrends.net |
| Revenue CAGR 3yr | TIKR — Income statement |
| ROIC | Koyfin or Gurufocus |
| Gross margin (current + 3yr trend) | TIKR |
| Net debt / EBITDA | TIKR or Koyfin |
| FCF / Net Income conversion ratio | Calculate: FCF ÷ Net Income (TIKR) |
| Current 10Y Treasury yield | TradingEconomics.com or CNBC |
| Current holding weight in portfolio | Your broker |

---

## Event-Triggered Rule 9 Model Refresh

| Trigger | Action Required |
|---------|-----------------|
| Stock moves >15% without known fundamental trigger | Re-score immediately. Investigate reason. |
| Quarterly earnings release | Standard re-score |
| Guidance revision (up or down) | Re-score + update fair value |
| Management change (CEO, CFO) | Re-score + thesis review + moat re-evaluation |
| Material M&A announcement | Re-score + recalculate debt ratios + moat impact |
| Macro shift (central bank policy, commodity shock) | Update Rate Environment Gate + re-score |
| Credible short report published | Short thesis engagement protocol |

---

## Data Input Template — Standard Re-Score

```
Task: RESCORE
Date: [DD MMM YYYY]
10Y US Treasury Yield: [X.XX%]
Rate Regime Modifier (active): [e.g. +0.5]

Ticker | Sector | FCF Yield (OE-adj?) | EV/EBIT | Fwd PE | 10yr Avg PE | Rev CAGR 3yr | ROIC | Gross Margin | Net Margin | Net Debt/EBITDA | FCF/NI Conv | Current Weight% | Last Score | Last Review
[TICK] | [...]  | [X.X%] (OE: Y/N)   | [XX×]  | [XX×]  | [XX×]  | [X%] | [X%] | [X%] | [X%] | [X×] | [X%] | [X%] | [X] | [MMM YYYY]

Fundamental changes since last review:
[List any: earnings beat/miss, guidance revision, M&A, management change, margin trend, organic revenue check, EPS vs revenue gap]
```

## Data Input Template — New Position Evaluation

```
Task: NEW POSITION
Date: [DD MMM YYYY]
10Y US Treasury Yield: [X.XX%]

Ticker: [TICK]
Sector: [sector]
Current Price: $[X]

Quality Gate (Phase 01):
  Net margin: [X%]  (threshold: >15%)
  ROIC: [X%]  (threshold: >15%)
  Revenue CAGR 3yr: [X%]  (threshold: >10%)
  Gross margin: [X%]  (threshold: >40% or expanding)
  FCF positive 3 consecutive years: [Y/N]
  Net debt/EBITDA: [X×]  (threshold: <2x)
  FCF/NI conversion ratio 2yr: [X%]  (threshold: >70%)
  Share issuance pattern: [dilutive Y/N]

Valuation Inputs (Phase 02):
  FCF Yield (Owner Earnings adjusted if applicable): [X%]
  EV/EBIT: [X×]
  Forward PE: [X×]
  10yr average PE: [X×]
  PEG (if EPS growth >15%): [X]

Fair Value Inputs:
  Last 12m FCF (or Owner Earnings): $[X]M
  FCF growth rate estimate: [X%]
  WACC: [X%]
  Shares outstanding: [X]M
  Net debt: $[X]M
  3–5 peer multiples: [list]

Qualitative Notes:
  Why are margins high?
  Moat assessment:
  Capital allocation track record:
  Growth sources next 3–5 years:
  Best bear case:
  Disruption vector check:
```

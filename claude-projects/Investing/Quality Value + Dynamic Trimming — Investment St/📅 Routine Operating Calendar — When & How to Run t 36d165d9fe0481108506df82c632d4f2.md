# 📅 Routine Operating Calendar — When & How to Run the Framework

# Overview

This calendar defines every operational task in the framework — what it is, when to run it, what data to prepare, and what Claude outputs. Follow this calendar to keep the portfolio fully aligned with the framework at all times.

> **Rule:** Every task that involves scoring, trimming, or buying requires pasting the System Prompt first.
> 

---

# 📅 Routine Schedule at a Glance

| Frequency | Task | Trigger | Claude Needed? |
| --- | --- | --- | --- |
| Daily (market days) | News & alert scan | Price move >5% intraday | No — human monitors |
| Weekly (Monday) | Earnings calendar check | Calendar-based | No — human prep |
| **After every earnings release** | **Quarterly Re-score** | Company reports earnings | **Yes — core task** |
| **Quarterly (each Jan, Apr, Jul, Oct)** | **Rate Environment Gate update** | Quarter begins | **Yes** |
| **Annually (first week of January)** | **Rate-Normalised PE recalc** | Year begins | **Yes** |
| **Annually (January)** | **Full universe re-screen** | Year begins | **Yes** |
| **Event-triggered** | **Rule 9 model refresh** | See triggers below | **Yes** |
| **Event-triggered** | **Short thesis engagement** | Short report published | **Yes** |
| **Event-triggered** | **Turnaround sub-gate review** | Every 2 quarters after entry | **Yes** |

---

# 🗓️ DAILY — Alert Monitoring (Human Task)

**When:** Any market day

**Who:** You (not Claude)

**Purpose:** Catch sudden fundamental news before the next scheduled review

**Watch for these triggers — if any fire, escalate immediately to an Event-Triggered Re-score:**

- Any holding moves >10% in a single session
- Earnings surprise >10% vs consensus (beat or miss)
- Regulatory action, lawsuit, CEO departure announced
- Short report published by a major fund or investigative outlet
- M&A announcement (acquirer or target)

**Tools:** Set price alerts in your broker. Use Google News alerts per ticker. Check OpenInsider for insider activity weekly.

---

# 🗓️ WEEKLY — Earnings Calendar Prep (Human Task, Monday)

**When:** Every Monday morning, pre-market

**Who:** You (not Claude)

**Purpose:** Know what is reporting this week so you can pull data immediately after release

**Steps:**

1. Check earnings calendar for the week (Earnings Whispers, TIKR, or Koyfin)
2. Flag any holding or watchlist name reporting this week
3. Pull pre-earnings baseline metrics from TIKR/Koyfin — have them ready before the report drops
4. Note analyst consensus EPS and revenue estimates

**Output:** A short prep note per company reporting that week. No Claude needed.

---

# 🗓️ QUARTERLY — Post-Earnings Re-Score (Core Claude Task)

**When:** Within **3 business days** of each holding’s earnings release

**Session type:** `RESCORE`

**Approx. time commitment:** 30–60 minutes per company

## Data to Pull Before the Session

| Metric | Where to Get It |
| --- | --- |
| FCF (or Owner Earnings for MSFT/META/GOOGL/AMZN) | TIKR — Cash Flow statement |
| EV/EBIT (trailing and forward) | TIKR or Koyfin |
| Forward PE | Koyfin or Finviz |
| 10-year average PE | [Macrotrends.net](http://Macrotrends.net) (search “[ticker] PE ratio”) |
| Revenue CAGR 3yr | TIKR — Income statement |
| ROIC | Koyfin or Gurufocus |
| Gross margin (current + 3yr trend) | TIKR |
| Net debt / EBITDA | TIKR or Koyfin |
| FCF / Net Income conversion ratio | Calculate: FCF ÷ Net Income (TIKR) |
| Organic revenue (if acquisitions made) | Earnings release or 10-Q |
| EPS vs revenue growth gap check | TIKR — compare YoY EPS and Revenue growth |
| Current 10Y Treasury yield | [TradingEconomics.com](http://TradingEconomics.com) or CNBC |
| Current holding weight in portfolio | Your broker |

## What to Paste to Claude

1. System Prompt
2. Task type: RESCORE
3. Date + 10Y Treasury yield
4. Table of metrics per ticker (copy from template below)
5. Any news/fundamental changes since last review (quote directly from earnings call or press release)

## What Claude Outputs

- Rate Environment Gate pass/fail per ticker
- Full scored calculation (all sub-scores + modifiers shown)
- Updated valuation score vs previous score
- Action: HOLD / ADD / TRIM (%) / EXIT
- If TRIM or BUY: full order setup (buy price, sell target, stop loss, R/R, position size)
- Next review trigger

---

# 🗓️ QUARTERLY — Rate Environment Gate Update

**When:** First week of January, April, July, October

**Session type:** `RESCORE` (with rate update flag)

**Takes:** 10–15 minutes

## Steps

1. Look up current 10Y US Treasury yield
2. Determine which Rate Regime Modifier applies (see table in main framework)
3. If the modifier has **changed** from last quarter, re-score all current holdings with the new modifier and check if any action thresholds have shifted
4. Record the active modifier in the portfolio page

## What to Paste to Claude

System Prompt + task: “Rate Environment Gate quarterly update. Previous modifier was [X]. Current 10Y yield is [Y%]. Re-apply modifier to all current holdings and flag any score changes that cross action thresholds.” + current holdings metrics table.

---

# 🗓️ ANNUAL — Rate-Normalised Historical PE Recalculation

**When:** First week of January

**Session type:** `RESCORE` (annual task flag)

**Applies to:** Top 5 holdings by portfolio weight only

**Takes:** 30–45 minutes

## Purpose

The 10-year average PE built into the Historical PE Modifier (Upgrade 2) was partly formed in near-zero rate conditions (2012–2022). This annual recalculation removes those distorted years and gives a rate-normalised average for more accurate scoring.

## Steps

1. For each of the top 5 holdings, pull **annual PE ratios for the past 10 years** ([Macrotrends.net](http://Macrotrends.net))
2. Filter to only years where the 10Y Treasury was within ±1% of today’s yield
3. Calculate the average PE across those filtered years = Rate-Normalised PE Average
4. If this normalised average is materially lower than the raw 10yr average, flag it for Claude and apply +0.5 to that company’s score for the year

## What to Paste to Claude

System Prompt + task: “Annual Rate-Normalised PE recalculation. Current 10Y yield: [X%]. For each ticker below, I have pulled annual PE by year. Filter to years where yield was within ±1% of [X%] and calculate the rate-normalised average. Compare vs raw 10yr average and flag any +0.5 score adjustments.”

---

# 🗓️ ANNUAL — Full Universe Re-Screen

**When:** January (combine with Rate-Normalised PE week)

**Session type:** `SCREENING`

**Takes:** 2–3 hours (data gathering) + 45 min Claude session

## Purpose

Re-run Phase 01 quality gate on the full watchlist and any new names identified during the year. Refresh the qualified quality list (∼50–150 companies).

## Steps

1. In Finviz, run quantitative pre-screen: Gross margin >40%, Net margin >12%, ROIC >15%, Revenue growth >8% 3yr CAGR, FCF positive 3 consecutive years, Net debt/EBITDA <2.5x, FCF yield >4%, EV/EBIT <20x
2. Export results
3. Add any names from: 13F filings (Fundsmith, Akre, Constellation, Baillie Gifford adds), spin-offs in the past 12 months, sector rotation candidates
4. Feed the shortlist to Claude for Phase 01 quality gate pass and Phase 02 scoring

## What to Paste to Claude

System Prompt + task: SCREENING + full metrics table from Finviz export + 10Y Treasury yield

---

# ⚡ EVENT-TRIGGERED — Rule 9 Model Refresh

**When:** Any of the following occur

**Session type:** `RESCORE` or `EXIT REVIEW`

| Trigger | Action Required |
| --- | --- |
| Stock moves >15% without a known fundamental trigger | Re-score immediately. Investigate reason. |
| Quarterly earnings release | Standard re-score (see Quarterly task above) |
| Guidance revision (up or down) | Re-score + update fair value |
| Management change (CEO, CFO) | Re-score + thesis review + moat re-evaluation |
| Material M&A announcement | Re-score + recalculate debt ratios + moat impact |
| Macro shift (central bank policy, commodity shock) | Update Rate Environment Gate + re-score affected holdings |
| Credible short report published | See short thesis task below |

**What to Paste to Claude:** System Prompt + task: RESCORE + trigger description + updated metrics + any relevant quotes from press release or filing.

---

# ⚡ EVENT-TRIGGERED — Short Thesis Engagement

**When:** A credible short thesis is published (major short fund, investigative journalism, regulatory filing)

**Session type:** Special — do NOT use standard re-score prompt

## Rule

Disagreeing with a short thesis without a documented rebuttal is not due diligence. The framework requires engaging with the specific argument, not dismissing it.

## What to Paste to Claude

System Prompt + “A short thesis has been published on [ticker]. Here is the core argument: [paste the specific claims — do not summarise, paste the actual argument]. Evaluate each claim against our holding data. For each claim: (1) is the data accurate? (2) does it change any quality metric in the framework? (3) does it affect the valuation score? (4) is there a documented rebuttal or does this require an exit review?”

## Output

Claude produces a point-by-point rebuttal or flags which claims are valid and require score revision. Save the output to the Human Override Log.

---

# ⚡ EVENT-TRIGGERED — Turnaround Sub-Gate Review

**When:** Every 2 quarters after a Fallen Angel / Turnaround entry (Upgrade 4)

**Session type:** `RESCORE` with turnaround flag

## Review Checklist

- [ ]  Has ROIC improved toward the historical >15% threshold?
- [ ]  Are gross margins recovering or still declining?
- [ ]  Has the insider buying thesis held (no insider selling)?
- [ ]  Is Net Debt/EBITDA still <3×?
- [ ]  Is the core moat still identifiable?
- [ ]  Have any of the 5 entry conditions been violated?

**If quality gate fully re-passes:** eligible to increase to full position (score permitting).

**If conditions deteriorating:** exit at 2-quarter review. Do not hold a failed turnaround.

---

# 📊 Data Input Template — Standard Re-Score

Copy and fill in before each Claude session:

```
Task: RESCORE
Date: [DD MMM YYYY]
10Y US Treasury Yield: [X.XX%]
Rate Regime Modifier (active): [e.g. +0.5]

Ticker | Sector | FCF Yield (OE-adj?) | EV/EBIT | Fwd PE | 10yr Avg PE | Rev CAGR 3yr | ROIC | Gross Margin | Net Margin | Net Debt/EBITDA | FCF/NI Conv | Current Weight% | Last Score | Last Review
-------|--------|--------------------|---------|---------|---------|----|----|----|----|----|----|----|----|---------
[TICK] | [...]  | [X.X%] (OE: Y/N)   | [XX×]  | [XX×]  | [XX×]  | [X%] | [X%] | [X%] | [X%] | [X×] | [X%] | [X%] | [X] | [MMM YYYY]

Fundamental changes since last review:
[List any: earnings beat/miss, guidance revision, M&A, management change, margin trend, organic revenue check, EPS vs revenue gap]
```

---

# 📊 Data Input Template — New Position Evaluation

Copy and fill in for any new name not previously scored:

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
  P/S vs Gross Margin check (if high growth): [X vs X]

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

---

> *Created: May 2026 · Part of Quality Value + Dynamic Trimming Framework · Review and update whenever the framework operating rules change*
>
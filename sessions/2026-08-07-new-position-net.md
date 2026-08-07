# NEW POSITION — NET (Cloudflare, Inc., Class A)

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — unattended run)
**Date:** 2026-08-07 (session run date; the triggering post and the underlying earnings event both landed 2026-08-06)
**10Y US Treasury Yield:** Not fetched this session — evaluation stops at the Phase 01 Quality Score gate (see §3) before the Rate Environment Gate would otherwise apply, same precedent as the 2026-07-25 NET session and others.
**Current NET portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** [NET-2026-07-25.md](../watchlist/not-in-portfolio/NET/NET-2026-07-25.md) — Quality Score 57.7, FAIL, watchlist only. That entry's own "Next review trigger" named "Cloudflare's Q2 2026 earnings, scheduled Thursday, August 6, 2026" verbatim.
**Sector:** Technology — Internet Infrastructure / Security (CDN, DNS, DDoS mitigation, Zero Trust network security, edge compute)
**Filer type:** US SEC filer, CIK 0001477333, Delaware-incorporated, calendar fiscal year.
**First-use jargon decode:** see closing Glossary (all terms already defined in [glossary.md](../framework/glossary.md) from the 2026-07-25 NET session — no new terms this session).

---

## 0. Why this session exists — trigger source

A Telegram post (`bolshegold/9926`, ~21:14:39 UTC, 2026-08-06) explicitly named `$NET` and claimed a Q2 FY2026 earnings beat (Non-GAAP EPS $0.29 beat by $0.02; revenue $696.1M, +35.9% YoY, beat by $29.75M) plus raised Q3 2026 guidance ($736.0–$737.0M vs. $722.63M consensus) — two of Rule 9's six enumerated trigger categories. This is the current top post on `bolshegold` at scan time (advancing the channel's marker from `bolshegold/9922` to `bolshegold/9926`, a post-ID delta of 4 — posts #9923 (DKNG earnings), #9924 (ABNB earnings), and #9925 (a one-line ABNB buyback follow-up) were superseded and not individually evaluated per the command's latest-post-only scope; read for the record, see the accompanying `telegram-watch.md` mention-log rows).

Per [telegram-scan.md](../.claude/commands/telegram-scan.md) step 4's third bullet: NET is not held, has a prior `not-in-portfolio` entry, and the post claims materially new information — the actual earnings release itself, superseding the July 25 entry's placeholder ("earnings to watch next week," no figures) — and this matches that entry's own documented Next Review Trigger almost exactly (the actual report landed one day after the "expected" date, consistent with Cloudflare's typical after-market-close reporting cadence). This triggers a full `/new-position NET` re-run.

**Per Rule 0, no figure from the Telegram post is used as financial data below** — every number in this session is independently re-sourced from Cloudflare's own SEC filings.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| Contract identity | "CLOUDFLARE INC - CLASS A", NYSE, contract_id **382633646** (same contract confirmed in the 2026-07-25 session) | IBKR |
| `get_price_snapshot` | `last.price` **$331.77** (ts `2026-08-07T00:05:45Z` = 2026-08-06 20:05 ET — genuine after-hours quote, ~3h after Cloudflare's post-close earnings release and during its 5pm ET investor call, not a stale prior-day print) | IBKR |
| Cross-check | `get_price_history` (`ONE_DAY` bars, outside RTH included): 2026-08-06 bar — open $290.01, high $336.07, low $274.51, **close $330.69**, volume 1,938,191. Consistent with the $331.77 snapshot (within the day's own high/low range) — not stale. | IBKR |
| Prior close | $284.43 | IBKR `change`/`prior-close` |
| Day change | **+16.64%** (+$47.34) — itself a >15% single-day move, fully explained by the earnings/guidance release (not an "unexplained" Rule 9 move) | IBKR |
| 52-week range | $158.84 (low) – $336.07 (high, today's intraday print — the `misc_statistics` field still showed the stale pre-earnings $303.76 high, superseded by today's actual bar above) | IBKR |
| Shares outstanding | 355.931M (322.176M Class A + 33.755M Class B, per the 10-Q balance sheet as of 2026-06-30) | SEC 8-K Ex-99.1 (filed 2026-08-06) |
| Market Cap (at $331.77) | ≈ $118.10B | Derived, internally consistent |

**Live price used throughout this session: $331.77.**

---

## 2. Data Sourcing Note

This session sources fundamentals directly from **SEC EDGAR** — Cloudflare's Q2 FY2026 8-K (accession `0001477333-26-000053`, filed 2026-08-06, Exhibit 99.1) and its XBRL company-facts API (`data.sec.gov/api/xbrl/companyconcept` and `companyfacts`, CIK 0001477333) — cross-checked against the Q3 2025 (`0001477333-25-000140`) and Q4/FY2025 (`0001477333-26-000008`) earnings exhibits for quarters not separately reported as discrete 3-month XBRL facts (cash-flow-statement items are filed cumulative-YTD, not discrete-quarter, so quarterly figures below are derived by subtraction between consecutive cumulative filings). This is a stronger sourcing chain than the 2026-07-25 session's (`stockanalysis.com`, `yfinance` unreachable that day) — primary-source SEC filings throughout, not a third-party aggregator.

**TTM window (rolls forward from the 07-25 session): Q3 2025 (Jul–Sep) + Q4 2025 (Oct–Dec) + Q1 2026 (Jan–Mar) + Q2 2026 (Apr–Jun)** — i.e. Q2 2025 rolls off and Q2 2026 rolls on.

| Line item ($M) | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 | **TTM total** | Derivation |
|---|---|---|---|---|---|---|
| Revenue | 562.03 | 614.51 | 639.76 | 696.06 | **2,512.35** | Q4'25 = FY2025 ($2,167.94M) − 9mo2025 ($1,553.43M) |
| Gross Profit | 415.71 | 452.55 | 455.60 | 499.52 | **1,823.38** | Q4'25 = FY2025 GP ($1,615.41M) − 9mo2025 GP ($1,162.86M) |
| Operating Income (EBIT) | (37.46) | (49.23) | (61.99) | (205.70) | **(354.38)** | Q4'25 = FY2025 op. loss (−$207.21M) − 9mo2025 (−$157.97M) |
| Net Income | (1.29) | (12.08) | (22.93) | (169.98) | **(206.28)** | Q4'25 = FY2025 NI (−$102.27M) − 9mo2025 NI (−$90.19M) |
| Operating Cash Flow | 167.12 | 190.41 | 158.33 | 117.56 | **633.43** | Cumulative-YTD subtraction each quarter (see below) |
| Capex — PP&E | 84.64 | 85.19 | 65.23 | 49.96 | **285.02** | Cumulative-YTD subtraction |
| Capex — capitalized internal-use software | 7.51 | 5.78 | 9.03 | 11.22 | **33.53** | Cumulative-YTD subtraction across the Q3'25/FY2025/Q2'26 press-release cash-flow reconciliations (this line isn't separately XBRL-tagged in a standard `us-gaap` concept in recent filings — sourced from each period's own Exhibit 99.1 cash-flow statement instead; flagged in §8) |
| **Free Cash Flow** (OCF − both capex lines) | 74.97 | 99.44 | 84.08 | 56.38 | **314.87** | |

TTM Gross Margin = 1,823.38 / 2,512.35 = **72.57%**. TTM Net Margin = −206.28 / 2,512.35 = **−8.21%**. TTM FCF margin = 314.87 / 2,512.35 = **12.53%**.

**Balance sheet as of 2026-06-30 (10-Q, filed with the 8-K):** Cash & equivalents $1,663.77M + Available-for-sale securities $2,499.03M = **$4,162.80M** liquid assets. Convertible senior notes: current $1,293.26M + noncurrent $1,977.01M = **$3,270.27M** total debt. **Net Debt = 3,270.27 − 4,162.80 = −$892.53M** (a net cash position, wider than July's −$639.23M — the gap grew, consistent with continued FCF generation). Total stockholders' equity $1,620.02M.

### 2.1 What changed vs. the 07-25 session, and what didn't

Cloudflare's **Q2 2026 GAAP net loss widened sharply to $170.0M** (vs. $50.4M in Q2 2025), **not** because the underlying business deteriorated — revenue grew 36% YoY and non-GAAP operating income grew from $72.3M to $96.1M — but because of a one-time **$150.7M restructuring and other charge** tied to the company's disclosed shift to an "agentic AI-first operating model" (workforce reduction; see the 8-K's forward-looking-statements section). Excluding that one-time charge, GAAP operating loss would have been roughly −$55.0M, a modest **improvement** on Q2 2025's −$67.3M. This session's TTM figures include the charge as reported (no adjustment made — Rule 0 forbids inventing an "adjusted" GAAP figure not itself reported by the company), which is why TTM Net Income fell from −$86.75M (as of the 07-25 session's window) to −$206.28M this session, even though the underlying trend (non-GAAP profitability, revenue growth, gross margin) is stable-to-improving. This is flagged explicitly because it is the single largest driver of this session's headline numbers, and a future session evaluating a quarter without a comparable one-time charge should expect the TTM Net Income figure to improve mechanically as this quarter rolls out of the window in FY2027.

**Unchanged:** Cloudflare still has **not reported a single GAAP-profitable fiscal year** in this framework's lookback — the structural gap this framework's Quality Score is built to catch (see §3).

### 2.2 ROIC calculation

Invested Capital = Total Debt ($3,270.27M) + Equity ($1,620.02M) − Cash & AFS securities ($4,162.80M) = **$727.49M**. NOPAT ≈ TTM EBIT (−$354.38M) × (1 − 21% standard corporate tax rate, same simplified approach as the 07-25 session given the consolidated pretax loss obscures an effective rate) ≈ **−$280.16M**. ROIC ≈ −280.16 / 727.49 ≈ **−38.5%** — decisively negative regardless of the exact tax-rate assumption used (even a 0% tax adjustment still yields ROIC ≈ −48.7%), consistent with the 07-25 session's directionally-negative finding.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29 — unchanged since 07-25, no stale-score mark applies)

### 3.1 Hard disqualifier check

| Hard disqualifier | NET data (this session) | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | TTM FCF is **+$314.87M** (see §2 table — every quarter in the TTM window individually positive: $74.97M / $99.44M / $84.08M / $56.38M), continuing the FY2023–FY2025 positive streak established in the 07-25 session. | **PASS — does not fire.** |
| **Net Debt/EBITDA over threshold** | Net Debt = **−$892.53M** (net cash, wider than July's −$639.23M) — negative under any denominator. | **PASS — well under threshold.** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | Net Income is negative every year in the lookback and in this TTM window; FCF/NI is opposite-signed (+FCF ÷ −NI), the same edge case flagged in the 07-25 session. **Same precedent-following treatment applied: does not independently fire on opposite-signed years.** This judgment call does not change the outcome — see §3.3, where the weighted score fails the gate by a wide margin regardless. | **Does not independently fire (see caveat, unchanged from 07-25).** |

No hard disqualifier fires this session, consistent with 07-25.

### 3.2 Sub-scores

| Sub-score (weight) | Formula & inputs (this session's TTM, §2) | Result |
|---|---|---|
| **Profitability (25%)** | Net Margin (TTM) = −206.28/2,512.35 = **−8.21%** → NetMargin_Component = clamp((−8.21/30)×100) = clamp(−27.4) = **0.0**. ROIC (TTM, §2.2) ≈ **−38.5%** → ROIC_Component = clamp((−38.5/30)×100) = clamp(−128.3) = **0.0**. Profitability_Score = (0.0+0.0)/2 = **0.0** | **0.0** |
| **Margins (15%)** | Gross Margin (TTM) = **72.57%** (down modestly from July's 73.32% — Q2 2026's GAAP gross margin of 71.8% pulled the TTM average down as it replaced Q2 2025's 74.9% in the window; still comfortably above the 40%/80% band). GrossMargin_Score = clamp((72.57/80)×100) = **90.71**. No trend bonus (already >40%, and the multi-year trend remains a mild compression, not an expansion). | **90.71** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $975.24M → FY2025 $2,167.94M, no new FY completed since 07-25) = (2,167.94/975.24)^(1/3) − 1 = **+30.53%** → base = clamp((30.53/25)×100) = clamp(122.1) = **100.0** (cap). Q2 2026 revenue growth (+36% YoY) shows continued acceleration, not deceleration — no −10 modifier; the +10 TAM-expansion modifier (documented in 07-25 via Workers AI/Zero Trust/Developer Platform evidence, reaffirmed by this quarter's "Agentic Internet" positioning in the 8-K) is moot given the cap. | **100.0** |
| **Balance Sheet (15%)** | Net Debt = **−$892.53M** (net cash). BalanceSheet_Score = clamp(100×(1 − NetDebt/EBITDA/4)) evaluates well above 100 with a negative numerator and clamps to **100.0**, regardless of TTM EBITDA's exact value (not separately reconciled this session — moot given the clamp). | **100.0** |
| **Moat Signal (15%)** | **Carried forward unchanged from the 07-25 session** (3 of 5 signals: Market share stable/growing, Network effect, Switching costs — each with cited evidence; Brand premium and Scale cost advantage remain FALSE) — no new moat-relevant evidence was sought or claimed this session, and nothing in Cloudflare's Q2 print bears on the underlying competitive-position evidence. See the 07-25 session's full evidence table for citations. | **60.0** |
| **FCF Quality (10%)** | FCF/NI (TTM) = 314.87 / −206.28 = **−1.526** (**−152.6%**) — same positive-FCF/negative-NI edge case as 07-25 (formula not designed for this combination; floors mechanically regardless of FCF's absolute size). FCFQuality_Score = clamp(((−1.526−0.40)/0.60)×100) = clamp(−321.0) = **0.0**. | **0.0** |

### 3.3 Final weighted Quality Score

```
Quality Score = (0.0 × 0.25) + (90.71 × 0.15) + (100.0 × 0.20) + (100.0 × 0.15) + (60.0 × 0.15) + (0.0 × 0.10)
              = 0.000 + 13.6065 + 20.000 + 15.000 + 9.000 + 0.000
              = 57.6065 → 57.6 (rounded to nearest 0.1)
```

**57.6 < 80.0 — fails the gate, by 22.4 points.** Essentially unchanged from the 07-25 session's 57.7 (a −0.1pt move, within rounding/data-refresh noise) — the Q2 2026 earnings event, despite its size (+16.64% price reaction, a genuine revenue/guidance beat), does not move the needle on this framework's Quality Score, because the dominant gap (Profitability + FCF Quality, 35% combined weight, both floored at 0.0 by persistent GAAP unprofitability) is untouched by one quarter's results — if anything the GAAP net loss *widened* this quarter (due to the one-time restructuring charge, see §2.1), even as the underlying non-GAAP business improved.

**Sensitivity (Moat only — the sole qualitative judgment call, held against the same 07-25 evidence):**

| Moat reading | Moat_Score | Quality Score | Gate result |
|---|---|---|---|
| Conservative (2/5 — drop Switching costs) | 40.0 | 54.6 | FAIL |
| **Primary (this session, unchanged from 07-25)** | **60.0** | **57.6** | **FAIL** |
| Maximally generous (5/5) | 100.0 | 63.6 | **FAIL — still 16.4pts short** |

Robust to every Moat reading, exactly as in July — the gate outcome does not turn on this session's one discretionary judgment call.

### Result: **Phase 01 FAIL**

No Rate Environment Gate, no Phase 02 valuation score, and no Composite Score computed — consistent with the strict gate rule.

---

## 4. Recommendation

**FAIL — does not clear the Quality Score gate**, at **57.6 vs. the strict 80.0+ bar**, missing by 22.4 points, robust to every Moat sensitivity checked. No order setup, no fair-value work, no BUY/TRIM/EXIT action.

Cloudflare delivered a genuine, well-documented Q2 FY2026 beat-and-raise (revenue +36% YoY, non-GAAP operating income and EPS both up YoY, Q3 guidance raised) — independently confirmed against the company's own 8-K, not the triggering Telegram post. The market's +16.64% reaction is a real, well-explained Rule 9 price move. None of that changes this framework's conclusion: Cloudflare's Quality Score remains anchored by **persistent GAAP unprofitability** (TTM Net Income −$206.28M, actually *wider* this session due to a one-time $150.7M restructuring charge layered onto an otherwise-improving non-GAAP picture) — the same structural gap identified in July, worth 35% of total weight at a full floor (Profitability 0.0, FCF Quality 0.0) that no amount of Growth (100.0), Balance Sheet (100.0), or Margin (90.7) strength can offset.

**PASS — watchlist only. No position opened.**

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Mandatory Rule 9 re-check:** Cloudflare's Q3 FY2026 earnings (guided for $736.0–$737.0M revenue; based on this quarter's cadence, expected ~early November 2026). Specifically worth checking whether the Q2 2026 restructuring charge was genuinely one-time (as disclosed) — if so, TTM Net Income should mechanically improve once Q2 2026 rolls out of the window and a cleaner quarter rolls in, independent of any further operating improvement.
- **Mechanical trigger, unchanged from 07-25:** Profitability and FCF Quality remain the dominant, decisive gaps (35% combined weight, both floored). The single most direct path to a materially different result is Cloudflare reporting **sustained, non-one-off GAAP net income** — still not observed this quarter (if anything, the reported GAAP loss widened, albeit for a disclosed one-time reason).
- **Other Rule 9 events:** a further guidance revision, management change, material M&A, or a >15% stock-price move with no identified cause.
- Absent any of the above, future Telegram mentions of NET should be logged as "last checked, no change" rather than triggering a full re-evaluation each time (same standing instruction as the 07-25 entry, reaffirmed here).

---

## 7. Watchlist Actions

- Created `watchlist/not-in-portfolio/NET/NET-2026-08-07.md` (new dated entry, superseding `NET-2026-07-25.md`) — warranted under [watchlist/README.md](../watchlist/README.md#significant-change--when-does-a-new-dated-entry-get-created)'s explicit rule that **a Rule 9 fundamental-event trigger firing warrants a fresh dated entry even when the score/action category ends up unchanged**, since the reasoning behind the number has materially changed (an actual earnings print now backs the score, not a placeholder "earnings to watch" note).
- No stale-score mark applies (methodology version unchanged since 07-25).

---

## 8. Data Gaps Flagged (summary — none blocked scoring)

1. **Capitalized internal-use software** (a cash-flow-statement line Cloudflare reports but does not tag under a standard `us-gaap` XBRL concept in recent filings — confirmed via a full company-facts tag search, which found only pre-2020 usage of `CapitalizedComputerSoftwareAdditions`) — sourced instead by reading the as-reported cash-flow reconciliation directly from each of the three relevant Exhibit 99.1 press releases (Q3 2025, Q4/FY2025, Q2 2026) and deriving the missing quarters by cumulative-YTD subtraction. Cross-checked internally: Q1 2026 and Q2 2026's derived/reported figures ($9.03M / $11.22M) sum exactly to the Q2 2026 press release's own directly-stated 6-month figure ($20.24M). Non-blocking — a small line item (1.3% of TTM revenue) with no effect on which side of the Quality Score's clamps the result lands.
2. **EBITDA (D&A add-back)** not independently reconciled this session — Cloudflare's cash-flow-statement D&A tag (`DepreciationDepletionAndAmortization`) diverged materially from the 07-25 session's `stockanalysis.com`-sourced D&A figures (e.g. Q2 2025: $45.48M via XBRL vs. $70.84M cited in July), likely reflecting a different D&A definition (e.g. amortization of deferred contract acquisition costs reported separately by Cloudflare, per the Q2 2026 cash-flow statement's own line items). Not resolved this session because it's immaterial to the outcome — Balance Sheet Score clamps to 100.0 from the net-debt sign alone, independent of the exact EBITDA denominator. Flagged for a future session if EBITDA is ever needed for a non-clamped calculation.
3. **Moat evidence not re-sourced this session** — carried forward from 07-25 on the judgment that one quarter's earnings doesn't bear on the underlying competitive-position evidence (market share, network effect, switching-cost citations). Flagged as a carry-forward, not a fresh finding.

None of these gaps blocked scoring.

---

## Glossary

- **8-K** — A US public company's filing disclosing a material event (here, quarterly earnings) to the SEC promptly after it occurs.
- **CAGR (Compound Annual Growth Rate)** — The smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every EDGAR filer (Cloudflare's is 0001477333).
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and profitability ratios.
- **FCF (Free Cash Flow)** — Cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; see §3.2 for this session's edge case (positive FCF, negative NI).
- **GAAP** — Generally Accepted Accounting Principles — the standard US accounting rules a public company's official financial statements must follow, as opposed to a company's own "non-GAAP" adjusted figures.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score — none independently fired for NET this session.
- **Invested Capital** — The total capital (debt + equity, netted for cash) deployed in a business — the denominator of this session's ROIC calculation.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **Non-GAAP** — A company's own adjusted financial measures (here, excluding items like stock-based compensation, restructuring charges, and amortization of acquired intangibles) presented alongside GAAP figures; useful supplementally but not a substitute for GAAP results per this framework's Rule 0 discipline.
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. NET scores 57.6 this session.
- **ROIC (Return on Invested Capital)** — How efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure — the basis used throughout this session's sub-scores.
- **XBRL (eXtensible Business Reporting Language)** — The SEC's structured, machine-readable data-tagging format for filed financial statements — this session's primary sourcing method via `data.sec.gov`'s API.

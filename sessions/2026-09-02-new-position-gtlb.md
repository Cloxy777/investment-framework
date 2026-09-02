# NEW POSITION — GTLB (GitLab Inc.) — 2026-09-02

**Task type:** NEW POSITION (Telegram-scan triggered — see §0)
**Date:** 2 Sep 2026
**Ticker:** GTLB (GitLab Inc., NASDAQ)
**10Y US Treasury yield:** 4.80% (Rate Regime bracket: 3.5–5% → +5, for reference only — not reached this session, see below)
**Prior sessions:** [2026-06-12-new-position-gtlb.md](2026-06-12-new-position-gtlb.md) (Phase 01 FAIL, pre-Quality-Score-engine) → [2026-07-09-new-position-gtlb.md](2026-07-09-new-position-gtlb.md) (first Quality Score computation: 56.0/100.0, fails the 80.0+ gate, also independently failed by the FCF-positivity hard disqualifier)
**Current GTLB portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session exists

Triggered by the hourly Telegram-scan routine (Routine 6): FinnInvestChannel post #3174 (2026-09-02 19:48:48 UTC) — "Gitlab вже 50$ 🫠😎🥹 …" (casual price commentary, not a claimed Rule 9 event; per this framework's rules the post's text is a *trigger only*, never a data source). GTLB is not held and carries a prior not-in-portfolio entry (56.0 Quality Score, gate fail, 2026-07-09). Two things made this worth an independent re-check rather than a routine "no change" skip:

1. The 07-09 entry's own **"Next review trigger"** was GTLB's Q2 FY2027 earnings release, expected "~early September 2026" — today falls squarely inside that window.
2. The post's implied ~$50 price vs. the $34.16 on record (+~46%) is large enough to warrant independently verifying whether something material happened, via live data — not by trusting the post's number.

This is a full, fresh Quality Score recomputation per the task's instructions (not a lightweight addendum this time), since the prior addendum flagged this exact earnings date as the next mandatory Rule 9 check.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$49.60** | IBKR `get_price_snapshot`, contract_id 520512263 (NASDAQ, same contract resolved in the 07-09 session), snapshot ts 1788379549 → **2026-09-02 20:05:49 UTC**, `is_close: false` |
| Bid / Ask | $49.00 / $49.80 | Same snapshot |
| Day change | +10.0% (+$4.51) vs. prior close ≈$45.09 | Same snapshot |
| 52-week range | $18.73 – $52.38 | `misc_statistics`, same snapshot |
| 13-week / 26-week high | $46.65 / $46.65 | Same snapshot (today's price is already above both — a fresh high) |
| Baseline (07-09) | $34.16 | Prior session |
| Change since 07-09 | **+45.2%** | Computed |

The Telegram post's "already $50" is close to, but not exactly, the verified $49.60 — consistent with the post being informal color, not a precise quote. Live price fetched from IBKR before any other work, per Rule 0.

---

## 2. Rule 9 check — all 6 categories

| Category | Result |
|---|---|
| **Earnings** | **YES — fires.** GitLab reported **Q2 FY2027 results (quarter ended 2026-07-31) on 2026-09-01**, after the 07-09 session's flagged "~early September" window. This is the confirmed trigger. Full detail in §3. |
| Guidance revision | Folded into the earnings release: FY2027 revenue guidance raised to $1,129–$1,133M (from a lower prior figure) and non-GAAP operating income guidance to $148–$152M — an *upward* revision, consistent with the earnings beat, not scored on its own (guidance is never a scored input, only a trigger — see [valuation-scoring.md](../framework/valuation-scoring.md)). |
| Management change | **Minor, non-alarming.** GitLab's Chief Accounting Officer, Simon Mundy, is departing effective 2026-09-16 "to pursue an opportunity outside of the Company"; CFO Jessica Ross assumes the additional principal-accounting-officer role, no added pay. The 8-K explicitly states the departure "was not the result of any disagreement with the Company regarding its financial reporting, accounting practices, or internal controls." Not a CEO/CFO change, no restatement flag — noted for completeness, not treated as an independent red flag. |
| M&A | None found. |
| Macro shift | None identified specific to GTLB. |
| >15% unexplained price move | The cumulative +45.2% since 07-09 is large, but explained: the earnings beat + guidance raise (§3) drove roughly a +15.9% one-day pop on 2026-09-01 per third-party reporting, continuing into today's own +10.0% intraday move — both fall inside the earnings-reaction window, not "unexplained." |

**Net effect: Rule 9 fires on Earnings** — this session recomputes the Quality Score fresh from the new TTM window (as instructed), rather than treating this as a "no significant change" addendum.

---

## 3. Q2 FY2027 earnings — confirmed reported, full detail

**Source:** GitLab's own Q2 FY2027 8-K/press-release exhibit, fetched directly from SEC EDGAR (`sec.gov/Archives/edgar/data/0001653482/000162828026059820/gitlab-ex99120260731fy27.htm`), cross-checked against the same filing's GAAP statements as reproduced by StockTitan's SEC-filing summary.

### GAAP income statement — three months ended July 31 (in $ thousands)

| Item | Q2 FY2027 (2026) | Q2 FY2026 (2025, prior year) |
|---|---|---|
| Subscription revenue | $258,311 | $212,684 |
| License/other revenue | $27,943 | $23,276 |
| **Total revenue** | **$286,254** | **$235,960** |
| Total cost of revenue | $45,638 | $28,505 |
| **Gross profit** | **$240,616** | **$207,455** |
| Sales & marketing | $134,363 | $109,583 |
| R&D | $94,980 | $71,488 |
| G&A | $68,208 | $44,735 |
| **Total operating expenses** | **$297,551** | **$225,806** |
| **Loss from operations** | **($56,935)** | **($18,351)** |
| Interest income | $12,202 | $11,511 |
| **Net loss (attributable to GitLab)** | **($36,844)** | **($9,208)** |
| Diluted EPS | ($0.22) | ($0.06) |
| Stock-based compensation | $75.0M | $54.284M |

**Why the GAAP loss widened despite a revenue beat:** GitLab initiated a restructuring program ("2027 Plan," workforce reduction, announced ~June 2026); this quarter recognized restructuring charges of roughly $19–23M (severance, retention costs, asset write-downs, some SBC acceleration — third-party sources gave slightly different exact figures; the underlying driver is consistently identified as the restructuring program, not an operating deterioration). Per Rule 6 ("normalize before you value"), this is a documented one-off, but this session scores off the **unadjusted GAAP figures**, consistent with this framework's established GTLB/CDR/SNDK precedent of never substituting non-GAAP "adjusted" numbers into the Quality Score engine — the restructuring context is shown here for transparency, not used to inflate the score.

### Cash flow — three months ended July 31, 2026 (in $ thousands)

| Item | Value |
|---|---|
| Net cash used in operating activities | **($3,092)** |
| Capital expenditures | ($213) |
| Non-recurring **JiHu** (China JV) payment | $14,036 — company's own non-GAAP add-back |
| Company-reported "adjusted FCF" | $9,750 |

Operating cash flow went negative largely on a **$57.3M swing in accounts receivable collections** (timing, not a demand problem) per third-party reporting, on top of the JiHu payment and restructuring cash outlays. This session uses the GAAP OCF figure (−$3.092M) as reported, not the company's adjusted FCF.

### Balance sheet (as of 2026-07-31, per 10-Q)

| Item | Value |
|---|---|
| Cash and cash equivalents | $226.491M |
| Short-term investments | $1,030.495M |
| Total assets | $1,661.832M |
| Total liabilities | $690.345M |
| Total stockholders' equity | $971.487M |
| Total debt | $0 |

### Business/growth highlights (qualitative, cited — not separately scored)

- Net ARR grew ~42% YoY ("second-highest quarterly growth rate in the last four years")
- Dollar-Based Net Retention Rate: 117% (essentially flat vs. the 117–118% cited in the 07-09 session)
- Total RPO ~$1.2B, +16% YoY (down from the +18–20% YoY cited 07-09 — a deceleration in backlog growth rate, though still solidly double-digit); committed RPO (cRPO) $744.7M, +20% YoY (down from +24% YoY cited 07-09)
- Share repurchases: ~3.5M shares, ~$105M in Q2 alone ($154.7M for the six months) under the $400M buyback authorized Q4 FY2026

---

## 4. Refreshed TTM financials (new window: Q3 FY2026 through Q2 FY2027, quarter ended 2026-07-31)

**Rolling-window mechanics:** per the 2026-08-05 rolling-window clarification in [quality-scoring.md](../framework/quality-scoring.md), the TTM window rolls forward one quarter: drop Q2 FY2026 (quarter ended 2025-07-31), add Q2 FY2027 (quarter ended 2026-07-31). The other three quarters (Q3 FY2026, Q4 FY2026, Q1 FY2027) are unchanged from the 07-09 session, sourced there directly from GitLab's own 8-K exhibits.

| Quarter end | Revenue | Gross Profit | GAAP Net Loss | Operating Loss | OCF | CapEx | SBC |
|---|---|---|---|---|---|---|---|
| 2025-10-31 (Q3 FY26) | $244.4M | $212.1M | −$8.3M | (n/a, not separately re-derived) | $31.43M | $3.04M | $51.682M |
| 2026-01-31 (Q4 FY26) | $260.4M | $225.42M | −$2.6M | (n/a) | $45.76M | $3.97M | $53.158M |
| 2026-04-30 (Q1 FY27) | $264.158M | $226.670M | −$4.972M | (n/a) | $149.2M | $2.393M | $50.061M |
| 2026-07-31 (Q2 FY27) | $286.254M | $240.616M | **−$36.844M** | **−$56.935M** | **−$3.092M** | $0.213M | $75.0M |
| **New TTM** | **$1,055.212M** | **$904.806M** | **−$52.716M** | **(see below)** | **$223.298M** | **$9.613M** | **$229.901M** |

Quarterly figures for Q3 FY26 / Q4 FY26 / Q1 FY27 carried forward unchanged from the 07-09 session (already sourced to primary 8-K exhibits there); Q2 FY27 figures sourced fresh this session per §3. TTM sums recomputed by rolling the window (old TTM total − Q2 FY26 figure + Q2 FY27 figure), cross-checked against a direct sum of the four quarters shown — both methods agree to the cent on revenue, gross profit, and net loss.

### Recomputed ratios (TTM through Q2 FY2027)

```
Net Margin (TTM)   = −$52.716M / $1,055.212M = −5.00%
  (07-09: −2.50% TTM through Q1 FY27 — the Q2 FY27 restructuring-driven loss widens the TTM margin back out,
   reversing most of the narrowing trend the 07-09 session noted)

Gross Margin (TTM) = $904.806M / $1,055.212M = 85.75%
  (07-09: 86.7% — still a clear pass on the >40% Phase 01 threshold, continuing the same mild multi-year
   declining trend already noted 07-09: ~90% FY2024 → ~87% FY2026 → 85.75% TTM now)

TTM Operating Loss = Old TTM Op Loss ($51.757M, per 07-09) − Q2 FY26 Op Loss ($18.351M) + Q2 FY27 Op Loss ($56.935M)
                    = $90.341M loss

Invested Capital (2026-07-31) = Total Equity $971.487M − Cash & Equivalents $226.491M − $0 Debt = $744.996M
  (consistent with the 07-09 session's methodology: nets cash only, not short-term investments)

ROIC (TTM) = −$90.341M / $744.996M = −12.13%
  (07-09: −7.44% computed / −4.57% third-party cross-check — more negative this quarter, driven by the
   restructuring-charge-inflated operating loss)
```

**Both previously-failing Phase 01 criteria (net margin, ROIC) remain decisively negative** — if anything, more negative than the 07-09 snapshot, because Q2 FY27's restructuring charges replaced Q2 FY26's smaller loss in the trailing window. Both are far below the >15% net margin / >15% ROIC thresholds.

### GAAP net income / SBC / insider-buying re-check

- **GAAP net income positive in any quarter? NO.** All 4 TTM quarters remain net-loss; Q2 FY27's −$36.844M is the *largest* quarterly loss in the current TTM window (restructuring-driven), a step backward from Q4 FY26's near-breakeven −$2.6M.
- **Material SBC policy change? NO**, but the ratio ticked up: TTM SBC $229.901M / TTM Revenue $1,055.212M = **21.79%** (07-09: 20.8%) — some of this quarter's SBC increase is tied to restructuring-related accelerated vesting (a one-off), not a base compensation-structure change; no new equity-plan/policy disclosure found.
- **CEO/CFO insider buying reported this cycle? Not independently re-verified.** No new Form 4 filings were searched this session beyond what 07-09 already covered (the last known purchases remain the 2026-06-30 and 2026-03-31 10b5-1-plan buys, ~$252K combined, already below the $500K/discretionary bar). This doesn't change the Turnaround Sub-Gate conclusion below, since condition 1 fails outright regardless.

**Turnaround Sub-Gate (Upgrade 4) — condition 1 still fails outright and structurally cannot change on any short timeframe:** GitLab IPO'd October 2021 and has never posted a GAAP-profitable, high-ROIC fiscal year as a public company — "historical ROIC >15% for ≥5 of the past 10 years" requires a public/reported history GitLab doesn't have and won't have for years. The sub-gate remains closed; not re-walked in full detail this session since this condition is a structural, near-permanent fact rather than something a single quarter could change.

---

## 5. Quality Score Engine — recomputed fresh (methodology version 2026-06-29)

Per [framework/quality-scoring.md](../framework/quality-scoring.md).

| Sub-score (weight) | Inputs | Value |
|---|---|---|
| **Profitability (25%)** | NetMargin_Component = clamp((−5.00/30)×100, 0, 100) = 0.0; ROIC_Component = clamp((−12.13/30)×100, 0, 100) = 0.0; both negative → clamped to floor. FCF-positivity cap (40.0) doesn't bind — unclamped average is already 0.0 | **0.0** |
| **Margins (15%)** | GrossMargin_Score = clamp((85.75/80)×100, 0, 100) = clamp(107.2, 0, 100) = 100.0 (capped). No structural-trend bonus — the 3yr trend is mildly *declining* (~90%→~87%→85.75%), not expanding, and the score is already capped regardless | **100.0** |
| **Growth (20%)** | Growth_Score = clamp((31.06/25)×100, 0, 100) = clamp(124.2, 0, 100) = 100.0 (capped). Revenue 3yr CAGR unchanged from 07-09 (FY2023 $424.3M → FY2026 $955.2M = 31.06%; no new annual print exists yet, FY2027 isn't complete until 2027-01-31). No structural-deceleration penalty applied — this quarter's guidance *raise* and accelerating 42% YoY Net ARR growth argue against, not for, a documented structural deceleration | **100.0** |
| **Balance Sheet (15%)** | Net debt is negative (net cash $1.257B: cash $226.491M + ST investments $1,030.495M vs. $0 debt) → clamps to ceiling | **100.0** |
| **Moat (15%)** | Unchanged from 07-09 — no new dated evidence found this session for a 3rd signal. **Brand premium/pricing power (TRUE):** 117% NRR (Q2 FY2027), consistent with the 07-09 figure, plus previously-cited Duo/Duo Enterprise pricing-escalation evidence. **Switching costs (TRUE):** Total RPO $1.2B (+16% YoY) / cRPO $744.7M (+20% YoY) — growth decelerated slightly vs. 07-09's +18-20%/+24% figures but still evidences multi-year contractual lock-in. **Market share** (FALSE — still only a stale snapshot, no cited trend), **Network effect** (FALSE), **Scale cost advantage** (FALSE) all unchanged | **40.0** |
| **FCF Quality (10%)** | TTM FCF = OCF $223.298M − CapEx $9.613M = $213.685M (positive). TTM NI = −$52.716M (negative). Literal ratio = 213.685 / −52.716 = −405.4%. FCFQuality_Score = clamp(((−4.054 − 0.40)/0.60)×100, 0, 100) = clamp(−742.3, 0, 100) = 0.0. Same negative-NI/positive-FCF edge case flagged 07-09 — mechanically clamped per the stated formula, GAAP-sourced inputs, not a data gap | **0.0** |

```
Quality Score = 0.0×0.25 + 100.0×0.15 + 100.0×0.20 + 100.0×0.15 + 40.0×0.15 + 0.0×0.10
              = 0.00 + 15.00 + 20.00 + 15.00 + 6.00 + 0.00
              = 56.0
```

**Quality Score = 56.0 / 100.0 — fails the 80.0+ gate.** Identical to the 07-09 figure, though the underlying inputs moved (net margin/ROIC more negative, FCF/NI ratio less extreme but still clamped to 0.0) — every sub-score happened to land on the same formula-clamp ceiling/floor as before, so the weighted total is coincidentally unchanged at 56.0.

### Hard disqualifier re-check

- **Disqualifier #3 — "not FCF-positive for 3+ consecutive years": still fires.** Per the rolling-window clarification, this is evaluated on the *most recently completed fiscal years* at the time of scoring. GitLab's fiscal year ends 2026-01-31 (FY2026); FY2027 doesn't complete until 2027-01-31 — **five months from now** — so the current 3-year window is still **FY2024 (positive, +$35.0M OCF) → FY2025 (negative, −$64.0M OCF) → FY2026 (positive, +$232.9M OCF)**, unchanged from the 07-09 session. FY2025's negative year still breaks the streak. This window will not roll forward until GitLab reports its FY2027 annual results (~March 2027).
- **Disqualifier #2 — Net debt/EBITDA:** passes trivially (net cash, $0 debt), same as always.
- **Disqualifier #1 — FCF/NI conversion <70% for 2+ years:** same interpretive tension flagged 07-09 (NI negative every fiscal year on record, so a literal reading would fire this too) — moot, since disqualifier #3 already independently fails the gate.

**GTLB fails the 80.0+ gate two independent ways at once, exactly as in the 07-09 session: the weighted score (56.0 < 80.0) and the FCF-positivity hard disqualifier (FY2025 negative GAAP OCF).**

---

## 6. Recommendation

# **PASS — Quality Score 56.0/100.0, fails the 80.0+ gate (also independently failed by the FCF-positivity hard disqualifier). Do not enter.**

Per this framework's rules ([quality-scoring.md](../framework/quality-scoring.md), [.claude/commands/new-position.md](../.claude/commands/new-position.md)): a company failing the 80.0+ Quality Score gate does not proceed to the Rate Environment Gate, Phase 02 valuation scoring, the Composite Score, or fair-value/order-setup work. **None of that was computed this session** — it would be moot regardless of how attractive GTLB's price action looks, and computing it would violate the framework's own strict-gate discipline (quality-scoring.md: "stop, don't proceed to Phase 02, regardless of how cheap the stock looks").

GitLab genuinely reported a strong *operational* quarter — revenue beat, guidance raised, Net ARR accelerating, record bookings — and the market's ~46% re-rating since 07-09 reflects that. But this framework's Quality Score is a **GAAP-financials-based, trailing quality grade**, not a forward growth-story score, and on that basis nothing has changed: GitLab still has never posted a GAAP-profitable fiscal year as a public company, TTM net margin and ROIC are both meaningfully negative (and slightly *more* negative than 07-09, due to this quarter's restructuring charges), and the FCF-positivity hard disqualifier remains open until FY2027 reports and the window rolls past FY2025's negative year. The Telegram post's "$50" framing is a price observation with no bearing on this conclusion — confirmed independently via live data exactly as Rule 0 requires, not taken on the post's word.

**No position opened — nothing to log in `decisions/`.**

**Next review trigger:** GitLab's **Q3 FY2027 earnings release** (quarter ending ~2026-10-31, historically reported ~early December based on this framework's Q1/Q2 FY2027 cadence) — mandatory Rule 9 re-check. Also watch for: the FCF-positivity disqualifier's window finally rolling forward once **FY2027 annual results** report (~March 2027, dropping FY2024 and adding FY2027 to the 3-year test — note this still requires FY2025 to roll *out* of the window, and a positive FY2027, before the disqualifier can clear); GAAP net income turning positive in any quarter (still hasn't); a discretionary (non-10b5-1) CEO/CFO insider purchase crossing $500K in a 6-month window; the CAO transition (effective 2026-09-16) resolving without incident (no financial-reporting-disagreement flag currently raised); and any further deceleration in RPO/cRPO growth rates (16%/20% YoY this quarter, down from 18-20%/24% at 07-09 — still healthy, but worth tracking as a trend, not yet a documented structural-deceleration case).

---

## 7. Files touched this session

- `sessions/2026-09-02-new-position-gtlb.md` — this file
- `watchlist/not-in-portfolio/GTLB/GTLB-2026-09-02.md` — **new dated file** (score/status/action all unchanged from 07-09 in outcome, but a Rule 9 fundamental-event trigger fired — earnings reported — per [watchlist/README.md](../watchlist/README.md)'s "significant change" criteria, which explicitly calls for a fresh dated pointer whenever "a Rule 9 fundamental-event trigger fires... even if the score/action ends up unchanged")
- `framework/glossary.md` — added **JiHu** (new term; all other terms used this session — NRR, RPO/cRPO, Gartner Magic Quadrant, Russell Reconstitution, Restructuring charge, 10b5-1 Trading Plan, Hard disqualifier, Composite Score, Rate Regime Modifier, Earnings Yield Spread Test, etc. — were already present from prior sessions)
- `watchlist/STALE.md` — **not touched.** GTLB was never listed there (it's excluded per the registry's own note: "not in-portfolio entries that are Phase 01 FAIL / not scored... GTLB" — a Quality-Score-gate-fail case has no Phase 02/Composite Score for a methodology version bump to invalidate, so there was never a stale mark to clear)
- `decisions/` — not touched (no position opened)

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **10b5-1 Trading Plan** — a pre-arranged, scheduled insider stock-trading plan; not treated by this framework as satisfying the Turnaround Sub-Gate's discretionary insider-buying condition.
- **8-K** — a US company's "current report" filed with the SEC disclosing a material event between regular filings; the primary source for GitLab's quarterly earnings-release exhibits used here.
- **CAGR** — Compound Annual Growth Rate.
- **CapEx** — Capital Expenditure.
- **Composite Score** — this framework's blended Quality + Valuation ranking number; not computed this session since GTLB fails the Quality Score gate.
- **cRPO** — the portion of RPO expected to be recognized as revenue within the next 12 months.
- **EPS** — Earnings Per Share.
- **FCF** — Free Cash Flow.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income, an earnings-quality check; not meaningful in the conventional sense when Net Income is negative and FCF is positive, as here.
- **Form 4** — the SEC filing disclosing an insider's change in beneficial ownership.
- **GAAP** — Generally Accepted Accounting Principles.
- **Gartner Magic Quadrant** — an analyst-firm vendor ranking; GitLab has been named a Leader for four consecutive years.
- **Gross Margin** — Gross Profit ÷ Revenue.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted score; GTLB's FCF-positivity check (FY2025 GAAP OCF negative) fires this one independently.
- **Invested Capital** — the capital (debt + equity, net of cash) put to work in a business; the ROIC denominator.
- **JiHu** — GitLab's China-market joint venture; a one-off cash payment related to it appears in this quarter's cash-flow statement.
- **Moat** — a durable competitive advantage.
- **Net Margin** — Net Income ÷ Revenue.
- **Net Retention Rate (NRR)** — the percentage of recurring revenue retained/expanded from an existing customer cohort over 12 months; GitLab's 117% is cited as pricing-power/switching-cost Moat Signal evidence.
- **NOPAT** — Net Operating Profit After Tax, the numerator of ROIC.
- **Quality Score** — this framework's 0–100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02. GTLB scores 56.0.
- **Restructuring charge** — a cost booked for reorganizing operations (severance, facility closures, etc.), typically flagged by the company as non-recurring; GitLab's Q2 FY2027 "2027 Plan" workforce-reduction charges widened its GAAP operating loss this quarter.
- **ROIC** — Return on Invested Capital.
- **RPO (Remaining Performance Obligations)** — contracted-but-unrecognized subscription revenue; a forward demand/backlog metric.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 6** — this framework's fair-value-methodology instruction to normalize (strip out) one-time items like restructuring charges before valuing a business — not applied to the Quality Score itself, which scores off unadjusted GAAP figures.
- **Rule 9** — this framework's list of events that force an immediate re-valuation: earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move.
- **SBC (Stock-Based Compensation)** — non-cash employee pay in company shares/options; a real dilutive cost to shareholders even though it inflates FCF relative to GAAP net income.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results; the window rolls forward one quarter each time a new quarter reports.
- **Turnaround Sub-Gate** — the conditional path (Hybrid Upgrade 4) letting a company failing some quality criteria still enter as a small position if it passes 5 specific tests; not reachable here (fails condition 1 outright — GitLab has never had a public GAAP-profitable fiscal year).

# RESCORE — MSFT — 2026-07-05

**Task type:** RESCORE (mode `--both`)
**Date:** 05 Jul 2026 (Sunday — markets closed; most recent trading session 02 Jul 2026)
**10Y US Treasury Yield:** 4.49% (TradingEconomics/dshort "Treasury Yields Snapshot," 2 Jul 2026 close — most recent available; markets observed the July 4th holiday Fri 3 Jul, then the weekend)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket, unchanged)
**Last review on record:** MSFT **33.9** (2026-06-26, BUY-Standard band — [sessions/2026-06-26-rescore-msft.md](2026-06-26-rescore-msft.md)); Composite Score never computed (predates the 2026-06-29 Quality Score/Composite Score methodology change — flagged stale, see [watchlist/STALE.md](../watchlist/STALE.md)).
**Current MSFT portfolio weight:** 15.09% per [holdings.md](../portfolio/holdings.md) (26 Jun 2026 sync — not recomputed this session; weight refresh is `/sync-portfolio`'s job). **Marginally over the 15% hard cap (Upgrade 7) — checked explicitly below given the score would otherwise recommend BUY.**
**First-ever Quality Score / Composite Score computation for MSFT this session.**

> *Jargon decoded on first use: FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EBITDA = operating profit before depreciation/amortization; EV/EBIT = enterprise value ÷ operating profit; PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; D&A = depreciation and amortization; capex = capital expenditure; NOPAT = net operating profit after tax; ROIC = return on invested capital; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; CAGR = compound annual growth rate; pp = percentage points; TTM = trailing twelve months; NTM = next twelve months.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$390.49** | IBKR `get_price_history` (contract_id 272093, NASDAQ), most recent daily bar close = **2026-07-02** (last trading session before markets observed the July 4th holiday Fri 3 Jul, ahead of the Sat–Sun weekend). Cross-validated exactly against `yfinance`'s `currentPrice`/`regularMarketPrice` fields, both independently reading $390.49. |
| ⚠️ Tooling flag | IBKR `get_price_snapshot`'s `last` field returned **$384.28** (marked `is_close: true`) — this is stale by one session: it matches the **2026-07-01** close, not the most recent 07-02 close (`get_price_history` and `yfinance` both confirm 07-01 close = $384.28, 07-02 close = $390.49). Same known one-session-stale-snapshot pattern flagged in the 2026-07-04 AVGO session — used the fresher, cross-validated $390.49 instead. |
| 52-week range | $349.20 – $552.28 (IBKR `misc_statistics`) | Unchanged from 06-26; still within it. |
| Year-to-date change | −20.36% (IBKR) | vs. −23.6% cited 06-26 — the 07-01/07-02 bounce narrowed the YTD loss. |
| Analyst consensus PT | $561.11 mean (55 analysts, "Strong Buy"), range $400–$870 | `yfinance` `targetMeanPrice`/`targetHighPrice`/`targetLowPrice` — matches the $561.11/$561–570 cluster cited across every prior MSFT session; bull-case sanity check only (Rule 0 Step 4), not a scored input. |
| Price vs. 06-26 review ($368.65) | **+5.94%** | Recovered off the fresh 52-week low touched that week; well under the 15% Rule 9 threshold. |

---

## 2. Rule 9 Trigger Check (2026-06-26 → 2026-07-05)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No | Next report confirmed **28 Jul 2026, after close** (FY2026 Q4) — unchanged from prior sessions' "late July" estimate, now dated precisely. |
| Guidance revision | No | No new formal guidance issued this window. |
| M&A (of an external company) | No | See below — the "Microsoft Frontier Co." item is an internal unit investment, not an acquisition of another company. |
| Management change | No | None found. |
| Macro shift | No | 10Y ticked from 4.38% (06-26) to 4.49% (07-02) — still inside the "3.5–5%" bracket, no Rate Regime bracket change. |
| >15% unexplained price move | No | +5.94% over 9 days, explained (see below), well under threshold. |

**Qualitative items found, none meeting the Rule 9 bar:**
1. **Escalated workforce-reduction reporting.** Business Insider (2 Jul 2026, via Fox Business/GeekWire) reports Microsoft could cut **~2.5% of its global workforce**, spanning Xbox, sales, and consulting — a wider scope than the ~1,000-person, Xbox-only figure flagged 06-26. **Still press reporting citing unnamed sources, not a company-confirmed 8-K, earnings-call disclosure, or formal WARN filing** — same treatment as 06-26's narrower version: **does not meet a Rule 9 trigger**, but the escalated scope is flagged as an elevated Phase 04 monitoring item, likely to be quantified (headcount, severance cost, segment-margin impact) at the 28 Jul earnings call.
2. **"Microsoft Frontier Co." — $2.5B AI-implementation-unit investment, announced 2 Jul 2026 (company-confirmed; stock +1.6% that day).** A new internal unit helping enterprises deploy customized AI systems — this is a **company-confirmed strategic investment**, but it is an internal-unit buildout, not an acquisition of an external business, and no formal guidance figure accompanied it. **Does not meet the M&A or guidance-revision Rule 9 categories** as currently defined; noted as a qualitative watch item, not folded into the Quality Score's Growth modifier or the Upside/Downside Modifier's scenario assumptions this session (consistent with how META's unconfirmed "Meta Compute" report was treated 2026-07-01).
3. **Securities class action — case No. 26-cv-02071, same litigation flagged 06-23/06-26.** Lead-plaintiff deadline confirmed unchanged at **11 Aug 2026**; multiple additional law firms (BFA Law, Robbins Geller, Rosen) continue independently soliciting lead-plaintiff applicants for the identical underlying claims (Copilot adoption/functionality disclosures). **No escalation, no new case, not a fresh Rule 9 trigger.**
4. **MSFT's H1 2026 performance context:** stock fell ~23% in H1 2026 (worst half since 2000), −20% in June alone (worst month since the dot-com era) — consistent with, not a revision to, the AI-capex/litigation-overhang/gaming-weakness thesis already embedded in the scenario model. **Not an unexplained move; not a Rule 9 trigger.**

**Conclusion: no Rule 9 trigger fired.** This remains a routine price-refresh rescore — but see §4 for a material, non-Rule-9 **data correction** discovered this session (net debt), and §6 for the **first-ever MSFT Quality Score computation**, both of which materially change the analysis even without a Rule 9 event.

---

## 3. Tooling Note — `yfinance` Access Restored

Unlike the 06-26 session (which hit a `curl_cffi`/TLS proxy error and had to carry forward every fundamental), `yfinance` was reachable this session via a plain `requests.Session()` passed to `yf.Ticker()` (after an initial `YFRateLimitError` cleared on retry) — the same transport-layer workaround used in the 2026-07-04 AVGO session. This let every fundamental below be **freshly re-pulled and cross-checked** for the first time since 06-20, rather than carried forward — including the Quality Score's Phase 01 inputs (gross margin, ROIC, revenue CAGR), which were explicitly flagged "not refreshed" as far back as the 2026-06-12 session (Data Gap #5, that session) since they weren't needed for scoring until the Quality Score existed.

---

## 4. Data Gaps / Flags

1. **Upgrade 1 (Owner Earnings) — still unresolved (7th consecutive session).** MSFT still discloses no maintenance-vs-growth capex split. **Raw TTM Free Cash Flow used** as the FCF_Score input, as in every session back to 06-07.

2. **🚩 MAJOR CORRECTION — Net Debt was overstated by ~$63B across 4 prior sessions (06-12 through 06-26).** The 06-12 session recorded "Total debt $103.194B" (cited to the same FY26 Q3 10-Q, period ended 3/31/2026) and "Net debt = $24.922B," and this figure was carried forward unchanged through 06-20, 06-23, and 06-26. **This session, cross-checking `yfinance`'s fresh balance-sheet pull directly against the actual SEC 10-Q for the identical balance-sheet date (3/31/2026, via WebFetch on the filing itself), the correct figures are:**
   ```
   Current portion of long-term debt (3/31/2026):  $8,839M
   Long-term debt (3/31/2026):                    $31,423M
   Total interest-bearing notes debt:              $40,262M   ← not $103,194M
   Cash and cash equivalents:                      $32,105M
   Short-term investments:                          $46,167M
   Cash + ST investments:                          $78,272M   (this part WAS correct — matches all prior sessions exactly)

   Net Debt (notes only, standard EV convention, excl. operating leases) = $40,262M − $78,272M = −$38,010M
   → MSFT is in a NET CASH position of ~$38.0B, not net debt of $24.922B as carried forward for 4 sessions.
   ```
   *(Robustness check: even including the $16,703M long-term operating-lease liability as "debt" — a broader, non-standard convention this framework doesn't otherwise use — net debt is still −$21,307M, i.e. still net cash. The qualitative correction holds either way.)*
   I could not identify exactly how the original $103.194B figure was derived (it does not match any single balance-sheet line item or combination I could reconstruct), but it is contradicted by the primary-source SEC filing for the same date. **This corrects EV, EV/EBIT, and the Quality Score's Net Debt/EBITDA sub-score for this session** — see §5–§7. Flagging prominently per "never invent or estimate financial data" / "show every calculation": this is a correction to a primary source, not a new estimate.

3. **🚩 Quality Score gate result is NOT robust to one judgment call (Moat Signal, "Scale cost advantage").** See §6 — Quality Score is **78.3** (fails the 80.0 gate) or **81.3** (passes) depending on whether one moat signal is credited, a margin of only ~1.3–1.7 points either way. Shown transparently, mirroring the same-shape disclosure in the 2026-07-04 AVGO session (Quality Score 82.1, flagged as hinging on one signal by a 2.1-point margin).

4. **TTM D&A refreshed:** $43.629B (fresh quarterly rollforward this session) vs. $41.549B carried in prior sessions (originally resolved from a three-way vendor discrepancy in 06-12). Immaterial (~$2.1B, ~0.7% of EBITDA) — does not change any sub-score band.

5. **Shareholder yield recomputed fresh (bottom-up) rather than carried forward:** dividend yield 0.891% + net buyback yield 0.696% = **1.588%**, vs. the 1.96% carried across 06-20/06-23/06-26 (which had been carried since `yfinance` access failed on those dates). Fresh figure used this session.

6. **5yr avg/range PE — re-verified live, unchanged.** Recomputed the full `get_earnings_dates`-based reconstruction (same method as prior sessions) with working `yfinance` access: **avg 31.9693×, range 24.1686×–38.8030× (n=20 quarters, through the 29 Apr 2026 earnings print)** — an *exact* match to the figure carried forward since 06-20. Confirms the carry-forward was valid (no new earnings print occurred to move the underlying series).

7. **Quality Score inputs (gross margin, ROIC, revenue 3yr CAGR, moat evidence) computed fresh for the first time** — flagged "not refreshed" as Phase 01 inputs as far back as 06-12 since they weren't needed until the Quality Score existed. All sourced via `yfinance` quarterly/annual financials this session; ROIC cross-checked against external range (20.85%–27.24% across GuruFocus/stockanalysis.com/FinanceCharts) — my computed 26.55% sits within that range.

8. **FCF/NI conversion ratio (TTM) = 58.23%** ($72.916B ÷ $125.216B) — below the 70% Quality Score threshold, consistent with every prior session (58.2%), explained by the same documented, cited AI/datacenter growth-capex ramp (FY26 capex guided to ~$190B, +63% YoY) that already justifies the (unresolved) Upgrade 1 Owner Earnings treatment. **Does not trigger the hard disqualifier** — the annual FY2022–2025 ratios (89.6% / 82.2% / 84.0% / 70.3%) are all ≥70%; only the in-progress TTM figure dips below, with a standing, cited explanation, not "2+ consecutive years" unexplained.

---

## 5. MSFT — Inputs Collected (fresh this session)

**Sector:** Technology — Software, Cloud Infrastructure (Azure) & Productivity

| Item | Value | Source |
|---|---|---|
| Shares outstanding | 7,428,434,704 | `yfinance` (exact match to 10-Q cover page used in every prior session) |
| **Market Cap** | 7,428,434,704 × $390.49 = **$2,900.729B** | Computed |
| Total notes debt (current + LT) | $40.262B | SEC 10-Q, 3/31/2026 (§4 flag 2) |
| Cash + ST investments | $78.272B | Same 10-Q |
| **Net Debt (corrected)** | **−$38.010B (net cash)** | Computed — see §4 flag 2 |
| **EV** | $2,900.729B − $38.010B = **$2,862.719B** | Computed |
| TTM EBIT (operating income) | Q3FY26 $38.398B + Q2FY26 $38.275B + Q1FY26 $37.961B + Q4FY25 $34.323B = **$148.957B** | `yfinance` quarterly financials rollforward (fresh; ~$28M above the 06-26 session's $148.929B, immaterial) |
| **EV/EBIT** | $2,862.719B ÷ $148.957B = **19.218×** | Computed (was 18.5552× at 06-26's $368.65 with the *uncorrected* net debt — the price rise and the net-debt correction move in opposite directions) |
| TTM Operating Cash Flow | $170.141B | `yfinance` quarterly rollforward (matches 06-26's $170.14B) |
| TTM CapEx | $97.225B | Same (exact match to every prior session) |
| **TTM FCF** | $170.141B − $97.225B = **$72.916B** | Computed — exact match to every prior session |
| **FCF Yield** | $72.916B ÷ $2,900.729B = **2.5137%** | Computed |
| TTM Net Income | $125.216B | `yfinance` quarterly rollforward (matches prior sessions' $125.22B) |
| TTM Revenue | $318.273B | `yfinance` quarterly rollforward (matches the 06-12 session's $318.27B exactly) |
| Net Margin (TTM) | 39.34% | Computed |
| TTM D&A | $43.629B | Fresh (§4 flag 4) |
| EBITDA (TTM) | $148.957B + $43.629B = $192.586B | Computed |
| **Net Debt/EBITDA (corrected)** | −$38.010B ÷ $192.586B = **−0.197×** (net cash) | Computed — well past the "0×" best-case row on the Quality Score's Balance Sheet table |
| FCF/NI conversion (TTM) | 58.23% | See §4 flag 8 |
| Forward EPS (NTM) | $19.3688 | `yfinance` `forwardEps` |
| **Forward PE** | $390.49 ÷ $19.3688 = **20.165×** | Computed |
| 5yr avg PE (anchor) | 31.9693× (range 24.1686×–38.8030×, n=20q) | Re-verified live, unchanged (§4 flag 6) |
| TTM EPS/NI growth (Fast Grower test) | FY2024 +21.8%, FY2025 +15.5%, TTM +23.4% — **all >15% → Fast Grower confirmed** | `yfinance` annual + TTM rollforward |
| PEG | 20.165 ÷ 23.4 = **0.8616** | Computed |
| Effective tax rate (TTM) | 18.96% (Tax Provision $29.287B ÷ Pretax Income $154.503B) | `yfinance` quarterly rollforward |
| Total Stockholders' Equity (3/31/2026) | $414.367B | `yfinance` / SEC 10-Q |
| Gross Margin (TTM) | 68.31% ($217.410B ÷ $318.273B) | `yfinance` quarterly rollforward |
| Revenue 3yr CAGR (FY2022→FY2025) | (($281.724B/$198.270B)^(1/3)) − 1 = **12.42%** | `yfinance` annual financials |

---

## 6. MSFT — Quality Score (first-ever computation, 2026-06-29 methodology)

**Hard disqualifier check (all must pass before the weighted score matters):**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs unexplained? | Annual FY2022–2025 all ≥70% (89.6/82.2/84.0/70.3%); only the in-progress TTM (58.2%) dips below, with a standing, cited growth-capex explanation | disqualify if <70% for 2+ yrs *without* explanation | ✅ PASS |
| Net Debt/EBITDA over threshold? | **−0.197× (net cash)** — see §4/§5 correction | disqualify if >2.5× | ✅ PASS, comfortably |
| FCF-positive 3+ consecutive years? | FCF-positive every year on record (well beyond 3 years) | disqualify if not | ✅ PASS |

No hard disqualifier triggers. Proceeding to the weighted score.

### Profitability (25% weight)

```
Net Margin (TTM)     = $125.216B / $318.273B = 39.34%
NetMargin_Component  = clamp((39.34/30)×100, 0, 100) = 100.0   (>30% cap)

ROIC:
  NOPAT = EBIT × (1 − effective tax rate) = $148.957B × (1 − 0.1896) = $120.721B
  Invested Capital = Total Debt ($40.262B) + Total Equity ($414.367B) = $454.629B
    (this exact figure matches yfinance's own precomputed "Invested Capital" balance-sheet
    field — used as a cross-check on methodology, not as a separate independent source)
  ROIC = $120.721B / $454.629B = 26.55%
  Cross-check: external sources (GuruFocus 20.85%, stockanalysis.com 27.24%, FinanceCharts
  21.49%, a cited "26.1% LTM" figure) bracket 20.85%–27.24% — my computed 26.55% sits
  inside that range.
ROIC_Component = clamp((26.55/30)×100, 0, 100) = 88.50

Profitability_Score = (100.0 + 88.50) / 2 = 94.25   (no FCF cap — FCF-positive every year on record)
```

### Margins (15% weight)

```
Gross Margin (TTM) = 68.31%
GrossMargin_Score = clamp((68.31/80)×100, 0, 100) = 85.39
```
No structural-trend bonus applicable — gross margin is already well above the 40% threshold the bonus targets (bonus only applies to a *below*-40%-but-expanding margin), and the 4-year trend itself is not a clean expansion (FY2022 68.40% → FY2023 68.92% → FY2024 69.76% → FY2025 68.83% → TTM 68.31% — essentially flat with noise, not a directional trend).

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $198.270B → FY2025 $281.724B) = 12.42%
Growth_Score = clamp((12.42/25)×100, 0, 100) = 49.69
+ 10 (documented TAM expansion, cited): Azure guided to 39–40% constant-currency growth next
  quarter (above the 37% Street consensus), management describing Azure as capacity-constrained
  through 2026 — i.e. demand exceeding even what Microsoft can currently supply — plus the fresh
  $2.5B "Microsoft Frontier Co." AI-implementation-unit investment (2 Jul 2026, company-confirmed).
  Real, cited, company-disclosed evidence of market expansion.
Growth_Score (with bonus) = clamp(49.69 + 10, 0, 100) = 59.69
```
No decelerating-growth evidence exists (Azure growth is accelerating per guidance, not decelerating) — no −10 applies. *Note: total-company revenue CAGR (12.4%) is muted relative to Azure's own ~39–40% segment growth because mature segments (Windows, Office, gaming) dilute the consolidated figure — not a sign Azure itself is slowing.*

### Balance Sheet (15% weight)

```
Net Debt/EBITDA = −0.197× (net cash — see §4/§5 correction)
BalanceSheet_Score = clamp(100×(1 − (−0.197)/4), 0, 100) = clamp(104.94, 0, 100) = 100.0
```
Standard /4 denominator applies (MSFT is not a payment network/exchange — the Upgrade 5 asset-light override doesn't apply, and isn't needed here regardless).

### Moat Signal (15% weight) — checklist, cited evidence per signal

| Signal | Marked | Cited evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | Third-party data (Synergy Research Group, Q1 2026) puts Azure at ~21–25% global cloud-infrastructure share, second behind AWS — but Microsoft's own earnings disclosure shows Azure revenue growing **40% YoY**, faster than AWS's 19% YoY, and management describes Azure as capacity-constrained (demand exceeding supply). A softer basis than an outright #1-share claim, but a specific, cited, company-disclosed growth figure showing genuine share momentum against the category leader — flagged transparently that Google Cloud grew even faster (63% YoY, from a smaller base) over the same period, a countervailing data point. |
| Brand premium | **TRUE** | Specific, cited pricing-power evidence: Microsoft 365 Copilot is priced as a genuine premium add-on ($21–30/user/month on top of a base M365 license, 2–3× the base seat cost combined) with 30–50% Fortune 500 seat penetration despite the premium, and a *new, higher-priced* "Frontier Suite" (E7, $99/user/month) launched 1 May 2026 bundling Copilot — sustained/expanding premium pricing with continued adoption, not a price cut to defend volume. |
| Network effect | **TRUE** | LinkedIn (wholly owned) is a textbook two-sided professional network — recruiters/companies on one side, professionals/job-seekers on the other, value compounding with each side's growth — a well-established, structural mechanism, not requiring a fresh numeric citation (same treatment as META's Family-of-Apps network-effect signal in the 2026-07-01 session). |
| Switching costs | **TRUE** | Documented mechanism: deep enterprise identity/security/productivity-stack integration (Entra ID, the M365 E3/E5/E7 suite tiers) — migrating an organization off Microsoft's identity and productivity stack requires enterprise-wide re-platforming, a well-established data/workflow migration cost. |
| Scale cost advantage | **FALSE** | The checklist requires "cost-per-unit data showing a gap vs. smaller competitors." The best evidence found is an *industry-wide* hyperscaler efficiency statistic (data-center Power Usage Effectiveness, PUE, of ~1.1–1.2 for hyperscale operators vs. ~1.5–2.0 for legacy/smaller facilities) — a genuine per-unit efficiency metric, but the specific cited figure (1.10) is for Google's fleet, not Microsoft's own disclosed PUE, and the comparison is hyperscaler-class-wide rather than an MSFT-specific number against a named smaller competitor. Total FY26 capex ($190B) is a scale *input*, not a cost-per-unit *output*. Marked FALSE for lacking the precise evidentiary type the checklist calls for — consistent with the rigor the 2026-07-04 AVGO session applied to its own three FALSE signals. |

```
Moat_Score = (4/5) × 100 = 80.0
```

**⚠️ This is a close call for the overall 80.0+ gate — shown transparently, "no black box":** if the "scale cost advantage" signal above were instead credited TRUE (a defensible alternate read — hyperscaler-class PUE data is real, cited, per-unit efficiency evidence, and Azure unambiguously operates at that scale even though the specific 1.10 figure cited is Google's), Moat_Score would be **100.0** instead of 80.0, and the final Quality Score below would be **81.3** (passes the gate) instead of **78.3** (fails). The gate result here is **not robust to this one judgment call** — flagged explicitly, mirroring the same-shape disclosure in the 2026-07-04 AVGO session (that gate result hinged on a different single moat signal, by a 2.1-point margin; this one, by ~1.3–1.7 points, hinges on this one).

### FCF Quality (10% weight)

```
FCF/NI (TTM) = $72.916B / $125.216B = 58.23%
FCFQuality_Score = clamp(((0.5823 − 0.40)/0.60)×100, 0, 100) = 30.39
```
Below 70% (see §4 flag 8), but the 2+ year hard-disqualifier does not fire — the annual FY2022–2025 figures are all ≥70%, and the in-progress TTM dip has a standing, cited growth-capex explanation (the same one that underlies the unresolved Upgrade 1/Owner-Earnings question for this name).

### Quality Score — Final

```
Quality Score = (94.25×0.25) + (85.39×0.15) + (59.69×0.20) + (100.0×0.15) + (Moat×0.15) + (30.39×0.10)

  With Moat_Score = 80.0 (primary determination, §6 above):
  = 23.5625 + 12.8085 + 11.938 + 15.00 + 12.00 + 3.039
  = 78.348 → rounds to 78.3

  Sensitivity — with Moat_Score = 100.0 (alternate read, scale-cost signal credited):
  = 23.5625 + 12.8085 + 11.938 + 15.00 + 15.00 + 3.039
  = 81.348 → rounds to 81.3
```

# Quality Score = 78.3 (primary determination) — FAILS the 80.0+ gate. Sensitivity: 81.3 (would PASS) if the one flagged Moat judgment call is read the other way.

**This is the first time any currently-held position's Quality Score has failed the 80.0+ gate** (META passed comfortably at 90.0 on 2026-07-01; AVGO passed narrowly at 82.1 on 2026-07-04, also flagged as hinging on one judgment call). Per [quality-scoring.md](../framework/quality-scoring.md): *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all. Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."* Per [rescore.md](../.claude/commands/rescore.md) step 3: *"a held position dropping below the gate is itself a signal worth surfacing, even though existing holdings aren't retroactively force-exited on quality alone."* **Neither rule forces an exit here** — quality-gate failure alone is not one of the four valid Phase 06 exit reasons in [strategy.md](../framework/strategy.md) — but this is flagged as a **Phase 04 Quality Watch escalation**, the most significant open item from this session (see §10, §11).

---

## 7. MSFT — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 20.165 = 4.9601%
Spread = EY − 10Y Treasury = 4.9601% − 4.49% = +0.4701%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.4701%, ~1.03pp short) → **+5 additive**.

**Step 2 — Rate Regime Modifier**
10Y = 4.49% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for MSFT = +10** (unchanged bracket vs. every session since 06-12)

---

## 8. MSFT — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 2.5137/10), 0, 100) = 74.863
```
→ Contribution: 74.863 × 0.40 = **29.945**

**EV/EBIT — 25% weight**
```
EV/EBIT_Score = clamp((19.218 − 12)/23 × 100, 0, 100) = 31.384
```
→ Contribution: 31.384 × 0.25 = **7.846**

**Forward PE (fallback formula — 5yr avg only) — 20% weight**
```
Deviation% = (20.165 − 31.9693)/31.9693 × 100 = −36.94%
FwdPE_Score = clamp(50 + (−36.94)×2.5, 0, 100) = clamp(−42.35, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — 15% weight (Fast Grower confirmed, §5)**
```
PEG = Forward PE ÷ TTM EPS growth% = 20.165 ÷ 23.4 = 0.8616
PEG_Score = clamp((0.8616 − 0.5)/2.0 × 100, 0, 100) = 18.08
```
→ Contribution: 18.08 × 0.15 = **2.712**

**Raw weighted score:**
```
= 29.945 + 7.846 + 0.0 + 2.712 = 40.503
```
**+ Rate Modifier (+10) = 50.503** (before the Upside/Downside Modifier)

---

## 9. MSFT — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario architecture carried forward (bull/base/bear exit multiples 31.0×/27.0×/21.0× unchanged — no new fundamental information since 06-26 to revise the underlying narrative), refreshed at the fresh forward-EPS estimate and live price.**

NTM EPS = $19.3688 (fresh `yfinance` `forwardEps`, cross-checked: Live Price ÷ Forward PE = $390.49/20.165 = $19.3661 — within 0.01%, consistent)

| Scenario | Weight | PE applied | Rationale (unchanged from 06-20 onward) | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | 31.0× | Azure/AI monetization re-accelerates; multiple re-rates to ~5yr average (31.97×). Still below the ~$561–570 analyst consensus PT. | $19.3688 × 31.0 = **$600.43** |
| **Base** | 50% | 27.0× | Consensus mid-teens EPS growth but a haircut multiple vs. the 31.97× 5yr average to reflect litigation overhang, gaming-segment weakness/escalated layoff scope, and capex-margin concerns. | $19.3688 × 27.0 = **$522.96** |
| **Bear** | 25% | 21.0× | Growth decelerates / AI-capex returns disappoint; multiple de-rates near the low end of the 5yr band (24.17×) — bear FV lands close to the analyst $400 low PT. | $19.3688 × 21.0 = **$406.75** |

```
PW Fair Value = 0.25×600.43 + 0.50×522.96 + 0.25×406.75 = $513.27
```
(Up from 06-26's $510.88 — driven by the slightly higher forward-EPS base, not a scenario-assumption change. Sits below the ~$561–570 analyst consensus — sanity check passes.)

**Step 1 — Expected annual return E.**
```
Gap Upside %     = (513.27 ÷ 390.49) − 1               = +31.44%
Catalyst window  = 2 years (unchanged — FY26 Q4 earnings 28 Jul 2026 confirmed + FY27
                   Azure/AI re-acceleration cycle; still within Rule 10's 18–24mo window)
Annualized gap   = 31.44% ÷ 2                          = +15.72%
Intrinsic growth = +13%/yr   (unchanged — deliberately below consensus EPS CAGR of +16–20.7%)
Shareholder yield = +1.588%  (fresh bottom-up computation this session — §4 flag 5:
                   dividend yield 0.891% + net buyback yield 0.696%)

E = 15.72% + 13% + 1.588% = +30.31%
```

**Step 2 — Map E to the modifier (hurdle H = 10%).**
```
E = 30.31% ≥ H → M = −15 × clamp((30.31 − 10)/15, 0, 1) = −15 × clamp(1.354, 0, 1) = −15 × 1 = −15.0
```
**Modifier M = −15.0** (the maximum attractive bound — 8th consecutive session at this floor since 06-20, though the margin above the saturation threshold narrowed slightly with the fresher, lower shareholder-yield input).

**Guardrail checks:**
1. **Catalyst:** documented (28 Jul 2026 earnings + FY27 Azure/AI cycle), within 18–24 months → upside credit allowed. ✓
2. **Scenario-weighted, not the rosy point:** PW FV ($513.27) below the ~$561–570 analyst consensus; bear case underwritten near the $400 low PT. ✓
3. **Full calc shown** (above). ✓
4. **Bounded ±15:** at the −15 floor. ✓

---

## 10. MSFT — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE = Raw weighted (40.503) + Rate Modifier (+10) + Upside/Downside (−15.0)
                       = 35.503
```
Boundary rule: not a ".X5" case → standard rounding → **Final Valuation Score = 35.5**

| | Value |
|---|---|
| Raw weighted | 40.503 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | −15.0 (E = +30.31%) |
| **FINAL VALUATION SCORE** | **35.5** |
| Prior valuation score | 33.9 (06-26) |
| **Quality Score** | **78.3 (FAILS 80.0+ gate — primary determination; 81.3 sensitivity, see §6)** |

**Composite Score: per [quality-scoring.md](../framework/quality-scoring.md) and the "Composite Score" section of [valuation-scoring.md](../framework/valuation-scoring.md), the Composite Score is NOT computed for a company that fails the 80.0+ Quality Score gate — "isn't computed for, and doesn't rescue, a company failing the quality gate."** MSFT's primary-determination Quality Score (78.3) fails that gate. **No Composite Score is being adopted this session.**

*Reference only (not the operative Composite Score, shown for transparency per "no black box"):*
```
If Quality = 78.3 (primary):  Composite = 0.50×(100−78.3) + 0.50×35.5 = 10.85 + 17.75 = 28.6
If Quality = 81.3 (alt/pass): Composite = 0.50×(100−81.3) + 0.50×35.5 =  9.35 + 17.75 = 27.1
```
Both reference numbers would land in the 0.0–29.9 "Very Cheap" band — even further into "buy" territory than the raw Valuation Score alone. **This reference calculation is not being used to drive the action recommendation below**, precisely because the gate technically hasn't been cleared; flagging it only so the number exists in the record if the gate question is later resolved the other way.

**Action recommendation basis:** with no adopted Composite Score, this session falls back to the **raw Valuation Score (35.5)** against the Action Table — the same basis every MSFT session used before the Composite Score mechanism existed (pre-06-29).

---

## 11. MSFT — Action Recommendation & Position Cap Check

**Raw Valuation Score 35.5 → nominally BUY — Standard position 3–5% (30.0–49.9 band)** — same band as 06-26's 33.9 (no band change from the score alone).

**But THREE independent gates now block adding capital, up from two:**

1. **🚫 Position cap (Upgrade 7).** MSFT is at **15.09%** of the portfolio per [holdings.md](../portfolio/holdings.md) (26 Jun 2026 sync, not recomputed this session) — **0.09pp over the hard 15% cap**, which strategy.md states must "never exceed... under any circumstances." **This alone blocks any addition regardless of score.** 7th consecutive session flagging this (06-07, 06-11 backfill, 06-12, 06-20, 06-23, 06-26, and now 07-05).
2. **🚫 Risk/Reward ratio.** See §12 — both the formal-entry and live-price R/R checks fail the 2:1 minimum (1.33:1 and 1.21:1 respectively).
3. **🚫 NEW — Quality Score gate (primary determination).** Quality Score 78.3 fails the 80.0+ bar this framework requires before a company is eligible for Phase 02 scoring / the Composite Score at all. This doesn't retroactively force an exit (§6), but it is an **independent, new-in-kind reason** — on top of the pre-existing cap and R/R blocks — that this position sits outside what the current framework's own rules would newly originate today. Given MSFT is a large, pre-existing holding (not a new candidate), this is best read as a **Phase 04 Quality Watch escalation**, not a Phase 06 exit trigger (quality-gate failure alone is not one of strategy.md's four valid exit reasons).

**Net: no fresh capital added — the same conclusion as every session since 06-20, now reinforced by a third, independent reason.** The open compliance trim from the 2026-06-15 rebalance remains the standing housekeeping action; given the new Quality Watch flag, **this session recommends escalating that trim's priority** rather than continuing to defer it, and separately recommends the user decide whether MSFT's continued full-size holding despite a (marginally, sensitively) failed quality gate should be logged as a **Human Override** in [override-log.md](../portfolio/override-log.md) — mirroring the precedent already set for ZS (held despite a Phase 01 quality-gate fail) — a decision this session flags but does not make unilaterally, and does not edit override-log.md itself (out of this session's scope).

---

## 12. Order Setup (shown for completeness — nominal BUY band — both gates below block it)

```
Blended Fair Value (= PW FV):        $513.27
Margin of Safety (raw score 30–49.9 band): 25%   (lower end; wide-moat rationale — now itself
                                                   under question given §6's gate finding)
BUY PRICE (limit):                   $513.27 × (1 − 0.25) = $384.96
  → Live price $390.49 is ABOVE the formal buy price (+1.44%) — NOT at/below the entry trigger
    (a reversal from 06-26, where the live price sat below the then-lower buy price).
PRIMARY SELL TARGET (blended FV):    $513.27
BULL-CASE TRIM TARGET (bull × 0.90): $600.43 × 0.90 = $540.39
STOP LOSS (Buy × (1 − 25%)):         $384.96 × 0.75 = $288.72
R/R at formal entry = (513.27 − 384.96) ÷ (384.96 − 288.72) = 128.31 ÷ 96.24 = 1.33:1
R/R at live price   = (513.27 − 390.49) ÷ (390.49 − 288.72) = 122.78 ÷ 101.77 = 1.21:1
```

**⚠️ Both R/R checks fail the 2:1 minimum (Rule 6).** The live-price R/R (1.21:1) is *worse* than 06-26's 1.75:1 — the price recovery moved live price further from the wide 25%-MoS stop without a proportional increase in the FV gap. **Per Rule 6, R/R below 2:1 = do not enter, independent of the score band, the position cap, or the Quality Score question.**

---

## 13. Portfolio / Compliance Note (independent of valuation score)

MSFT sits at **~15.09%** per `portfolio/holdings.md` (26 Jun 2026 sync; not recomputed here — weight refresh is `/sync-portfolio`'s responsibility). This is the same structural concentration issue flagged across the last **7 consecutive sessions**. **New this session:** the Quality Score gate finding (§6) adds a second, independent dimension (not just "too large a position," but "a position this framework's own current quality bar would not, on this session's primary determination, admit fresh") to the case for prioritizing the standing compliance trim from the [2026-06-15 rebalance](../../sessions/2026-06-15-rebalance.md).

---

## 14. Next Review Trigger

- **Routine:** MSFT FY2026 Q4 earnings, confirmed **28 Jul 2026, after close** — will refresh every TTM fundamental used here (last refreshed live this session for the first time since 06-20) and is the natural point to re-run the Quality Score with a fresh TTM window (which will also resolve whether the FCF/NI dip persists into a genuine 2-consecutive-year pattern or reverts).
- **🚨 Open item (new, highest priority): resolve the Quality Score gate question (§6).** Either (a) obtain a harder, MSFT-specific cost-per-unit citation for the "scale cost advantage" moat signal to settle the 78.3-vs-81.3 ambiguity, or (b) accept the primary 78.3 determination and decide how to treat a 15%+ held position that fails the framework's own 80.0+ quality gate — log as a Human Override (per the ZS precedent) or treat purely as a Phase 04 Quality Watch item pending the next rescore.
- **Open compliance item (7th flag, now elevated priority): dedicated `/rebalance` execution of the position-cap trim** — recommend this be prioritized ahead of the routine cadence given §6/§11.
- **Open methodology item:** Owner Earnings (Upgrade 1) decision for non-disclosing mega-caps — 7th consecutive session.
- **Monitoring items (not Rule 9 triggers):** (1) the securities class action, case No. 26-cv-02071 (lead-plaintiff deadline 11 Aug 2026); (2) the escalated ~2.5%-workforce-reduction report (spanning Xbox/sales/consulting) — watch for formal disclosure/quantification at the 28 Jul earnings call; (3) "Microsoft Frontier Co." — watch for it to develop into a scored input if it becomes a disclosed, quantified revenue line.
- **Watch:** if price re-rates toward fair value, the Upside/Downside Modifier shrinks from its current −15.0 floor and the raw Valuation Score will rise back toward the HOLD band — re-derive at the next earnings print regardless.

---

## Glossary

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year. |
| **8-K (Form 8-K)** | A US company's "current report" disclosing a material event between regular filings. |
| **bps / pp (percentage points)** | A direct difference between two percentages, distinct from a "%" change. |
| **Buyback yield** | The rate at which a company's share count shrinks per year from repurchases, net of new issuance. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate; not adopted for MSFT this session. |
| **D&A** | Depreciation & Amortization. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **Effective tax rate** | Tax provision ÷ pretax income for a given period — used to compute NOPAT for the ROIC calculation. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years — this framework's PEG-eligibility trigger. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Gross Margin** | Gross Profit ÷ Revenue. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score. |
| **Human Override** | A position held outside the framework's own rules — tracked in `override-log.md`; flagged (not adopted) for MSFT this session pending user decision. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Hyperscaler** | An operator of very-large-scale, globally-distributed cloud/data-center infrastructure (e.g. Microsoft Azure, AWS, Google Cloud) — a business-model tier defined by scale, distinct from smaller regional cloud/hosting providers. |
| **Invested Capital** | The total capital (debt + equity) put to work in a business — the denominator of ROIC. |
| **IRR** | Internal Rate of Return. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt; negative means a net-cash position. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **Net Margin** | Net Income ÷ Revenue. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **NTM** | Next Twelve Months. |
| **Owner Earnings** | Net Income + D&A − maintenance capex only — used instead of raw FCF for moat-building reinvestors (Upgrade 1; unresolved for MSFT, Data Gap #1). |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **PUE (Power Usage Effectiveness)** | A data-center efficiency metric: total facility power ÷ power delivered to computing equipment. Lower is better (1.0 = no overhead); hyperscale operators typically achieve ~1.1–1.2 vs. ~1.5–2.0 for smaller/legacy facilities — used in §6 as candidate (ultimately not adopted, for lacking an MSFT-specific citation) evidence for the Moat Signal's "scale cost advantage" checklist item. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. MSFT's first-ever computation this session: 78.3 (fails the gate), sensitivity 81.3. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0 / Rule 6 / Rule 9 / Rule 10** | This framework's standing instructions to always fetch a live price first; require a minimum 2:1 risk/reward before entering; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline. |
| **SEC 10-Q** | A US public company's quarterly report filed with the Securities and Exchange Commission, containing unaudited financial statements — the primary source used in §4 to correct the net-debt figure. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |

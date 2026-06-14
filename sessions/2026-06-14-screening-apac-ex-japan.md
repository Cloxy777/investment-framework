# 2026-06-14 — SCREENING: Developed Asia-Pacific ex-Japan (APAC-EX-JP)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [APAC-EX-JP](../framework/screening-coverage-log.md) (Australia, Hong Kong, Singapore, South Korea, Taiwan), all sectors. Selected per the rotation rule: tied for "Never screened" with EM/EU/JP/NA-2, first alphabetically among those.

---

## 0. Methodology — EODHD path blocked, hybrid fallback used

**Path A (EODHD automated screener) failed at the first call**: both `/api/screener` and `/api/fundamentals/{ticker}` returned `HTTP 403 — "Only EOD data allowed for free users"`. This is a **plan limitation**, not the "Host not in allowlist" network case the command anticipates, so the documented workaround (adjust network policy) doesn't apply — the current EODHD API key's plan simply doesn't include screener/fundamentals access.

**Path B (TIKR/Koyfin manual export)** isn't directly actionable in this session (no interactive access to those tools), and the user had no preference on fallback when asked.

**Approach taken** (flagged prominently per the "do not silently fall back to ETF holdings" instruction — this *is* a step beyond the documented Path B, done with the user's implicit go-ahead):
1. **Structural triage from domain knowledge** (Step 1, brought forward) — built a 13-name candidate pool of well-known APAC-ex-Japan businesses with plausibly durable high-margin models (exchanges, semiconductors, medtech, online marketplaces, gaming), explicitly skipping categories that structurally don't fit this framework (banks — gross margin doesn't apply; REITs; diversified retail conglomerates).
2. **Real, sourced fundamentals per candidate** — pulled live from stockanalysis.com (income statement, cash flow, balance sheet, ratios pages) for each name, cited by URL. No figures were estimated.
3. Applied the full Phase 01 quantitative gate to the sourced data.

IQLT (the framework's named "international" quality-factor ETF) was checked first but rejected as a starting pool — its visible holdings are dominated by Japan/Europe with negligible APAC-ex-Japan representation, and the full 331-name list sits behind a paid wall.

**Candidate pool (13 names):**

| Ticker | Company | Country | Sector |
|---|---|---|---|
| TSM (TWSE:2330) | TSMC | Taiwan | Semiconductors |
| TWSE:2454 | MediaTek | Taiwan | Semiconductors |
| TWSE:2308 | Delta Electronics | Taiwan | Power electronics |
| HKG:0388 | Hong Kong Exchanges & Clearing | Hong Kong | Exchange/clearing |
| HKG:0669 | Techtronic Industries | Hong Kong | Power tools (Milwaukee/Ryobi) |
| SGX:S68 | Singapore Exchange | Singapore | Exchange/clearing |
| ASX:CSL | CSL Limited | Australia | Biopharma (plasma) |
| ASX:COH | Cochlear | Australia | Medical devices |
| ASX:RMD / NYSE:RMD | ResMed | Australia | Medical devices |
| ASX:REA | REA Group | Australia | Online real-estate marketplace |
| ASX:ALL | Aristocrat Leisure | Australia | Gaming machines |
| ASX:CAR | CAR Group (Carsales) | Australia | Online auto marketplace |
| ASX:XRO | Xero | Australia/NZ | SMB accounting SaaS |

**Structurally excluded without quantitative pull** (Step 1, categorical):
| Eliminated | Why |
|---|---|
| DBS, OCBC, UOB (Singapore banks) | Banks — gross margin metric doesn't apply; regulated balance-sheet businesses don't fit this framework's model |
| AIA Group (HK insurer) | Financial sector — same reasoning |
| Macquarie Group (AU) | Investment bank/financial — same reasoning |
| Goodman Group (AU REIT) | REIT — gross margin/EV-EBIT framing doesn't fit |
| Wesfarmers, JB Hi-Fi (AU retail) | Thin-margin retail — structurally below net-margin bar (per NA-1 precedent for WMT/COST/TJX) |
| Samsung Electronics, SK Hynix (Korea) | Memory/semiconductor conglomerates with well-documented cyclical margin and FCF swings — fails "FCF positive + stable margins" structurally in down-cycles; flagged for a dedicated look if/when memory-cycle timing is favorable |

---

## Step 2 — Quantitative Phase 01 gate (real, sourced data — stockanalysis.com, pulled 2026-06-14)

Filters: Gross margin >40% · Net margin >12% · ROIC>15% (ROE proxy) · Revenue growth >8% (3yr CAGR) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x

| Ticker | Gross M | Net M | ROE (ROIC proxy) | Rev 3yr CAGR | FCF 3yr (positive?) | Net Debt/EBITDA | FCF yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| TSM (TSMC) | 61.87% ✅ | 46.97% ✅ | 34.03% ✅ | 18.85% ✅ | ✅ all 3yr positive | −0.40 (net cash) ✅ | 1.76% ❌ | 26.64× ❌ | **FAIL** — too expensive (FCF yield, EV/EBIT) |
| MediaTek | 47.03% ✅ | 16.92% ✅ | 25.42% ✅ | 2.81% ❌ ⚠️ | ✅ | −1.43 (net cash) ✅ | 1.73% ❌ | 66.93× ❌ | **FAIL** — growth + valuation |
| Delta Electronics | 35.50% ❌ | 11.83% ❌ | 24.28% ✅ | 13.10% ✅ | ✅ | −0.75 (net cash) ✅ | 0.96% ❌ | 58.12× ❌ | **FAIL** — margins + valuation |
| **HKEX (0388.HK)** | 96.54% ✅ | 62.46% ✅ | 35.00% ✅ | 16.49% ✅ | ✅ all 3yr positive | −7.33 (net cash) ✅ | **6.64%** ✅ (derived, see note) | 13.81× ✅ | **PASS — all 8 filters** |
| Techtronic Industries | 41.2% ✅ | 7.85% ❌ | 17.99% ✅ | 4.9% ❌ | ✅ | ≈0.05 ✅ | 8.00% ✅ | 16.32× ✅ | **FAIL** — net margin + growth |
| Singapore Exchange | 94.6% ✅ | 47.3% ✅ | 31.15% ✅ | 7.6% ❌ (close) | ✅ | net cash ✅ | 4.86% ✅ | 20.63× ❌ (close) | **FAIL** — 2 narrow misses (growth, EV/EBIT) |
| CSL Limited | 51.9% ✅ | 19.3% ✅ | 15.37% ✅ (barely) | 13.8% ✅ | ✅ | **data gap** (annual EBITDA not found) | 3.85% ❌ (close, FY25) | 21.73× ❌ (close, FY25) | **DATA GAP / borderline — see note** |
| Cochlear | 73.74% ✅ | 16.60% ✅ | 20.52% ✅ | 12.4% ✅ | ✅ (but FY25 FCF −46% YoY) | ≈0.10 ✅ | 0.89% ❌ | 37.31× ❌ | **FAIL** — valuation |
| **ResMed** | 59.36% ✅ | 27.22% ✅ | 25.86% ✅ | 12.92% ✅ | ✅ all 3yr positive | 0.44 ✅ | 4.40% ✅ | 22.20× ❌ (close) | **FAIL — narrow miss, EV/EBIT only** |
| REA Group | 62.19% ✅ | 35.74% ✅ | 37.93% ✅ | 10.57% ✅ | ✅ | net cash ✅ | 2.11–3.83% ❌ | 22.42–39.60× ❌ | **FAIL** — valuation |
| Aristocrat Leisure | 60.94% ✅ | 26.05% ✅ | 18.45% ✅ | 4.15% ❌ ⚠️ | ✅ | 0.86 ✅ | 3.67–5.05% mixed | 17.40–22.91× mixed | **FAIL** — growth (others mixed/borderline) |
| CAR Group | 84.69% ✅ | 23.27% ✅ | 9.78% ❌ | 30.9% ✅ ⚠️ (M&A-driven) | ✅ | 2.51–2.55× ❌ (borderline) | 3.62–5.61% mixed | 23.89–34.09× ❌ | **FAIL** — ROIC, leverage, valuation |
| Xero | 83.86% ✅ | 6.08% ❌ | 4.41–12.70% ❌ | 25.1% ✅ | ✅ | ≈3.16× ❌ | 6.00% ✅ | 32.05× ❌ | **FAIL** — margins, ROIC, leverage, valuation |

---

## ✅ Qualified Quality List — 1 name

**HKEX — Hong Kong Exchanges and Clearing (0388.HK)** — clears all 8 Phase 01 filters.

### Near-misses flagged for the watchlist (fail only on 1–2 narrow valuation/growth metrics — re-check on next rotation or a pullback)

- **ResMed (RMD)** — passes 7/8; only EV/EBIT (22.20×) is over the 20× cap, by ~11%. Everything else (margins, ROE 25.86%, 3yr revenue CAGR 12.92%, FCF yield 4.40%, net debt/EBITDA 0.44×) is comfortably inside the gate.
- **Singapore Exchange (S68)** — passes 6/8; revenue 3yr CAGR (7.6%) is just under the 8% bar and EV/EBIT (20.63× FY25) is just over 20×. Same business-quality profile as HKEX (regulatory monopoly exchange/clearing), just slightly pricier and slightly slower-growing.

### CSL Limited — data gap, not cleanly classified

CSL passes 6/8 cleanly (gross margin, net margin, ROE, revenue CAGR, FCF-positive, and — on a "current" basis — net cash). Two metrics are ambiguous:
- **Net Debt/EBITDA**: net debt (~$9.99B USD) is sourced, but a clean annual EBITDA figure wasn't found (only a half-year FY2026 figure of $3,130M USD, not usable without doubling/estimating — which we won't do per Rule 0).
- **FCF yield / EV-EBIT**: FY2025 figures (3.85% / 21.73×) both narrowly fail; but stockanalysis.com's "current" ratios (8.76% / 11.60×) both pass — and CSL's price is down **−55.4% over the trailing year**, so "current" multiples reflect a materially different price than the FY2025-period multiples. Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0 ("always fetch live prices first"), this discrepancy should be resolved with a live-price pull before CSL is classified — **recommend a `/new-position CSL` pass** to resolve this rather than guessing here.

---

## Step 3 — Qualitative pass (HKEX only — the sole clean PASS)

1. **Why are margins high?** HKEX runs Hong Kong's only securities/derivatives exchange and central clearing/depository (HKSCC). 96.5% gross margin reflects a near-zero marginal cost of processing trades plus substantial net interest income earned on ~HK$170B of client margin/collateral balances — revenue with effectively no COGS. This is structural (regulatory monopoly), not a lucky cycle, though the interest-income component is rate-sensitive.
2. **What would it take to compete?** Essentially nothing short of a new HK government-granted exchange license — not happening. Combined with liquidity network effects (deepest pool for HK/China-linked listings and Stock Connect flows), this is one of the strongest moats achievable.
3. **Capital allocation (5–10yr):** High dividend payout policy (~90% of distributable profit historically); infrastructure reinvestment (Orion trading platform); the one major outside bet is the 2012 London Metal Exchange acquisition (~$2.2B) — a mixed-but-defensible diversification, no other major value-destructive M&A.
4. **Where's growth coming from (3–5yr)?** Stock Connect expansion (Northbound/Southbound), continued mainland-China IPO pipeline shifting toward HK amid US listing friction, derivatives/commodities volume growth, RMB product expansion. FY2025 revenue +29.55% YoY — likely partly cyclical (elevated HK/China equity trading volumes).
5. **Best bear case:** (a) Revenue is transaction-volume-dependent — a prolonged HK/China bear market would sharply cut fee revenue, and FY2025's +29.55% growth may not repeat; (b) net interest income on client balances is HKD-rate-sensitive (HKD peg → Fed policy matters) — a rate-cutting cycle compresses this; (c) geopolitical risk to HK's status as financial gateway to China; (d) at 13.81× EV/EBIT it's "cheap" largely *because* FY2025 may be a cyclical peak — a normalized multiple could be meaningfully higher.
6. **Disruption vector:** Low near/medium-term risk — regulated securities clearing in a capital-controlled market (China-HK) structurally requires centralized infrastructure; blockchain/DeFi disintermediation of clearinghouses is a multi-decade question at best for this market. The bigger risk is geographic/political (flow shifting to Shanghai/Shenzhen) rather than technological.

**Conclusion:** HKEX is a genuine quality business with one of the strongest moats screened to date (regulatory monopoly + network effects), priced inexpensively (13.81× EV/EBIT) relative to its own growth — but FY2025's +29.55% revenue growth and the net-interest-income tailwind both look partly cyclical, so the "cheap" read should be sanity-checked for normalization risk before sizing. **Recommend `/new-position HKEX` (0388.HK)** for full Phase 02 scoring with live pricing.

---

## Data gaps flagged (per CLAUDE.md Rule 0 — none estimated)

- **HKEX FCF yield**: not directly published; *derived* as FY2025 FCF (20,746M HKD) ÷ Enterprise Value (312,311M HKD) = 6.64% — both inputs sourced, the division is shown, not invented.
- **TSMC, MediaTek, Delta, HKEX**: raw annual EBITDA dollar figures not published (only derived EV/EBITDA and Debt/EBITDA ratios were available).
- **MediaTek, Delta**: explicit total-debt/cash figures not found (only net-debt/EBITDA ratios, both net-cash).
- **CSL**: annual EBITDA not found; FCF yield / EV-EBIT classification ambiguous due to the −55% trailing-year price move (see above) — needs `/new-position` live-price resolution.
- **ResMed**: USD market cap not found (only AUD, from the ASX cross-listing page).
- **Xero**: stockanalysis.com's reported market cap (12.54B AUD) looks anomalously low for its scale — flagged by the research agent as possibly stale/cached. Doesn't change Xero's PASS/FAIL outcome here (it fails on net margin and ROE independent of market cap), but any future EV-based work on Xero should re-verify market cap from a second source.
- **MediaTek revenue CAGR**: FY2023 revenue declined sharply (433,446M TWD vs FY2022's 548,796M TWD), distorting the 3yr CAGR to 2.81% — flagged as a cyclical-trough-base-year artifact rather than a genuine growth-rate signal, though MediaTek fails on valuation regardless.
- **Aristocrat Leisure revenue series**: FY22→FY25 (5,574 → 6,296 → 5,673 → 6,297 AUD millions) is non-monotonic, likely a reporting/segment-basis change — the resulting 4.15% CAGR may understate underlying growth, but Aristocrat's other metrics are mixed/borderline regardless.
- **CAR Group FY23 net margin** (82.64%) reflects a one-off 486.53M AUD gain — normalized FY24/25 figures (~22-23%) were used instead.
- **Samsung Electronics, SK Hynix**: excluded at structural-triage stage (Step 1) without a quantitative pull — flagged for a dedicated look if a future session wants to evaluate memory-cycle timing specifically.

---

## Next steps

- `/new-position HKEX` (0388.HK) — the one clean Phase 01 pass; full Phase 02 scoring with live price.
- Watchlist: **ResMed (RMD)** and **Singapore Exchange (S68)** — both near-misses on valuation alone; worth a quick re-check if either pulls back ~10%, or on the next APAC-EX-JP rotation.
- `/new-position CSL` (or fold into the next ASX-focused rotation) — resolve the live-price/EBITDA data gaps before classifying.
- Coverage log updated below — next "Never screened" alphabetical slice is **EM (Emerging Markets)**.

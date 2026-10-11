# Part 1 — Verification of the Matrix research (`research/matrix-reference/`)

Scope: re-derive the worked examples and test vectors, audit internal consistency, resolve or sharpen the open items, and grade each rule block as a spec for re-implementation. **Proposals only — no source file was edited.** Status of this document: draft for user review.

Notation: **[F]** fact (read directly in a file), **[I]** inference (my deduction), **[O]** opinion. Paths are relative to the repo root. `RM` = `research/matrix-reference/rules-and-metrics.md`, `RS` = `research/matrix-reference/rules-supplement.md`, `CC` = `research/matrix-reference/screens/company-card.md`, `OQ` = `research/matrix-reference/open-questions.md`.

> Site access was **not** used. Everything below is re-computation or cross-reading of what was already captured. Facts that need the live site are marked `LIVE` and collected in [open-questions-for-user.md](open-questions-for-user.md).

## 1. Re-derivation of RS section B (worked examples) and section D (test vectors)

**Method.** Python arithmetic on the captured numbers (script reproduced in Appendix A). Tolerance: ±0.2% relative for anything that passes through display rounding (growth rates are printed to 0.1 pp, EPS to $0.01, prices to $0.01). Status values: **verified** (reproduces within tolerance), **failed** (cannot be reproduced under the stated rule), **cannot-verify** (input not captured).

### 1.1 B1 — five-year "x2" arithmetic (ABNB)

| # | Claim (RS line) | Re-derivation | Result | Status |
|---|---|---|---|---|
| V1 | EPS5 = 6.02 × 1.189 × 1.198 × 1.188 × 1.179 × 1.170 ≈ 14.05; card 14.03 (RS:64) | Path 6.02 → 7.16 → 8.58 → 10.19 → 12.01 → **14.052** | Δ = 0.16% vs card (growth inputs are rounded to 0.1 pp) | **verified** |
| V2 | Years 3–5 decay ≈ ×0.95 per step (RS:63) | 18.8/19.8 = 0.949; 17.9/18.8 = 0.952; 17.0/17.9 = 0.950 | Constant ratio ≈ 0.95 | **verified** (the "25% per step" cap: see E14, cannot-verify) |
| V3 | Base price5 = 14.03 × 21.8 = 305.87 (RS:66) | 305.85 | Δ 0.007% | **verified** |
| V4 | Pessimistic: growth = consensus steps ×0.50 for years 1–2, then decay; 9.5, 9.9, 9.4, 8.9, 8.5 (RS:68); EPS 9.36; price 149.68 | 0.5×18.9 = 9.45 ≈ 9.5 ✓; 0.5×19.8 = 9.9 ✓; decay 9.9×0.95 = 9.4 ✓; ×0.95 = 8.9 ✓; ×0.95 = 8.5 ✓. EPS5 = **9.364**; ×16 = 149.83 (card 149.68, Δ 0.1%) | Confirms the decay is applied **after** the ×0.50 haircut on the last consensus step | **verified** |
| V5 | Optimistic: 14.01 × 26.2 = 367.04 (RS:66) | 367.06 | Δ 0.005% | **verified**. Side note: optimistic EPS5 (14.01) differs from base EPS5 (14.03) although only the multiple should differ — see E15 (display rounding, low significance) |
| V6 | CAGR base 14.4 / pess −0.8 / opt 18.7 (RS:67) | (305.85/156.08)^0.2−1 = **14.40%**; (149.76/156.08)^0.2−1 = **−0.82%**; (367.06/156.08)^0.2−1 = **18.65%** | Base and pessimistic exact; optimistic rounds to 18.6/18.7 boundary | **verified** |
| V7 | "x2 reached in year 3.9" for optimistic (RS:193 lists the formula as unknown) | Yearly price path = EPS_t × 26.2 with EPS_t = EPS1 × Π(1+g_i, i≤t): ratio to P0 = 1.710 at t=3, 2.016 at t=4; linear interpolation → **3.947 ≈ 3.9**. The closed form ln2/ln(1+CAGR) gives 4.04 | Interpolation on the yearly path reproduces the card; the closed form does not | **verified** (one data point; resolves E7, [I]) |
| V8 | EPS1 = NTM EPS (6.02) then five growth steps (RS:62-64) — does this overshoot by one year? | Because the multiple is the *forward* (NTM) P/E, price at t=5 = NTM-EPS(t=5) × NTM-P/E is internally consistent; five steps from an NTM base is right. | No timing error | **verified** (logic check, [I]) |
| V9 | NVDA prices $313.46 / $578.80 / $611.16 (CC:66) and CAGR 6.5 / 20.4 / 21.7 (CC:66, RS:168) vs P0 $228.86 | (313.46/228.86)^0.2−1 = 6.49%; 578.80 → 20.39%; 611.16 → 21.71% | The three price/CAGR pairs are one-to-one; ordering is pessimistic / base / optimistic | **verified** |
| V10 | The geometric-mean "one EPS growth per card" (RM:65) | ABNB: √(1.367 × 1.189) − 1 = **27.49%** = the card's "+27.5% over 24 months" (RS:80). Note that the second step is 18.9% (the x2 path's g1), **not** the EPS-forecast tile's "next year +17.5%" (CC:100) | Confirms geometric mean of *NTM growth* and *the re-segmented next-12-month growth*. The tile (17.5%, 19.4%) and the x2 path (18.9%, 19.8%) come from different segmentations of the same consensus | **verified** (formula); the re-segmentation itself = **cannot-verify** (`changes-week.md`: "5-year growth now computed from annual consensus in 12-month segments") |

### 1.2 B2 — five price lenses

| # | Claim | Re-derivation | Status |
|---|---|---|---|
| V11 | ABNB PEG 0.94 → +1 | 25.9 / 27.5 = 0.942; `<1` → +1 | **verified** |
| V12 | ABNB FCF yield after SBC 3.4% vs 4% → +1 | ≥3% → +1 (RM:61) | **verified** |
| V13 | ABNB vs S&P: 25.9 vs 20.1 → −1 | ratio 1.2886; methodology `≤1.3× → 0` (RM:58). Rounding cannot explain it: the ratio range over the display-rounding interval is 1.283–1.294 | **failed** as a straight application → E1 |
| V14 | ABNB vs own history: 34.6 vs 3y avg 29.1 → −1 | +18.9% above average → −1 (RM:59) | **verified** |
| V15 | ABNB growth vs market: 27.5 / 13.6 = 2.02 → +1 | ≥1.5× → +1 | **verified** |
| V16 | ABNB sum +1 → "fair" | +1 +1 −1 −1 +1 = +1; fair ≥ +1 | **verified** (given the −1 on the S&P lens as printed) |
| V17 | NVDA S&P +1 | 19.1/20.1 = 0.95 ≤ 1× and level A → +1 | **verified** |
| V18 | NVDA PEG 0.34 shown, lens capped at +1 by the cycle-peak note | 19.1/56.6 = 0.337; trailing EPS growth +109% > 100% → cap (RM:65) | **verified** |
| V19 | NVDA FCF yield 2.2% → 0 | ≥2% → 0 | **verified** |
| V20 | NVDA growth 56.6/13.6 = 4.2× → +1 | ≥1.5× → +1 | **verified** |
| V21 | NVDA vs own history +2 (trailing 28.8 vs 3y avg 52.3) | 28.8 is 45% below the 3y average → rule gives +1 unless ≤ 5y-min×1.05 → +2 (RM:59); the 5y minimum is not captured | **cannot-verify** (`LIVE`: NVDA history chart stats) |
| V22 | NVDA sum 6 = 1+2+1+0+1 = 5, +1 mega-cap tweak (RS:81) | mega-cap: cap ≥ $200B, multiple 19.1 ≤ 20, level A → +1 | **verified** conditional on V21 |
| V23 | Scatter x-axis range −6…+8 (RM:9) and OQ#5 "how can the sum reach +8 when lenses cap at ±2?" | Lens maxima are +1 (S&P; only levels A/B), +2, +2, +2, +1 (growth) → max **+8**, +1 with the mega-cap tweak = **+9**; minima −2, −2, −2, −2, −1 → **−9**. RS:194 (E8) says "lens caps imply ±10 max" — that is wrong; the actual bound is +8/−9 (+9 with tweak) | **verified**; corrects E8 |

### 1.3 B3 — quality-score example

| # | Claim | Re-derivation | Status |
|---|---|---|---|
| V24 | ABNB components sum 71.6 vs shown 71.5 (RS:98) | 9.8+13.8+12.0+12.0+4.0+10.0+5.0+5.0 = 71.6 | **verified** (Δ0.1 = display rounding) |
| V25 | NVDA 91.0 | 15+17+9+15+10+10+10+5 = 91.0 | **verified** |
| V26 | ABNB profitability 9.8 = "2–5 years profitable" bucket (RM:31) | ABNB EPS bars show FY2021 loss and profits FY2022–FY2025 (CC:99) → 4 consecutive profitable years → bucket 2–5 → 9.8 | **verified** (consistent) |
| V27 | Predictability: ABNB 12 (platform), NVDA 9 (chips), META 9 (advertising) (RS:88, RM:43) | table values platform 12, chips 9, advertising 9 | **verified** (3 of 3) |
| V28 | ABNB moat 12 (network effect 12), NVDA moat 15 (monopoly 15; AI +2 clamped) (RM:44) | matches | **verified** (NVDA clamp is [I]) |
| V29 | ABNB balance 10, NVDA 10 (net cash) | matches | **verified** |
| V30 | ABNB margin 4.0 | net margin shown "20%" (CC:27); the 15–20% bucket gives 4; would be 6 at ≥20.0% (RM:36) — depends on rounding or on the "smaller of net and operating-after-tax" definition (RM:53) | **cannot-verify** (plausible) |
| V31 | ABNB growth 13.8 (RS:188) | revenue +17% → 4.8; FCF +13% → 3.0; EPS bucket 15–25% → 6.0 gives **13.8**; but EPS growth on the card is 27.5% (V10) which would give bucket ≥25% → 7.0 → 14.8 | **failed** as stated → E2: the EPS growth used inside the Growth component is *not* the 27.5% shown for PEG |
| V32 | Capital & SBC weight 10 (RM:28) built from SBC/FCF (max 6), ROIC (max 8), share count (max 7) (RM:39-41) | Sub-point maxima sum to **21**, not 10. NVDA 10.0 is reproducible only if the raw 21 is rescaled by 10/21. ABNB 5.0 is not reproducible under any integer combination of the listed buckets (SBC/FCF 35% → 1; ROIC ≥20% → 7, 10–20% → 6, <10% → 4; shares fell → 7; raw 12–15 → rescaled 5.7–7.1) | **failed** → E12 (probable mis-transcription) |
| V33 | "Unknown = 40% of weight" (RM:27) | 40% holds for revenue growth (3.2/8) and EPS growth (2.8/7) and moat (6/15). It does **not** hold for profitability (7.5/15 = 50%), margin (5/10 = 50%), balance (5/10 = 50%), SBC/FCF (3.5/6 = 58%), ROIC (6/8 = 75%), share count (6/7 = 86%) | **failed** → E13 |

### 1.4 B4 — verdict paths, and section D test vectors

| # | Check | Result | Status |
|---|---|---|---|
| V34 | Cell mapping for every D-table row: NVDA A×cheap → STRONG BUY (reviewed) ; NFLX A×cheap → STRONG BUY; ABNB B×fair → BUY; ADSK B×fair → BUY; GOOG B×fair → BUY; META, MA, ASML, MSFT, V (exp+grow) → BUY WAIT; ORCL D×exp+grow → AVOID; MU/005930.KS gate-0 speculation; SOFI stop-list | All rows agree with the map (RM:98-102) | **verified** |
| V35 | Level vs score: ADSK score 81.5 but level B (RS:181) | Level A needs consensus EPS growth ≥ 14% next 12M (RM:47); ADSK EPS growth 8.3% → cap A→B | **verified** ([I] cap identified; the card names the ceiling as "growth/review" in the screener "ceiling" filter) |
| V36 | V (Visa) level B → A on the change feed with an unchanged score 85.0 (`changes-week.md`) | Consistent with a cap lifting (e.g. growth bar 14.9% ≥ 14% for level A) rather than a score change | **verified** ([I]) |
| V37 | V price word "expensive but growing" with EPS +14.9% | Rule: ≥15% (level A: 14%) → 14.9 passes only because V is level A | **verified** |
| V38 | ASML NTM P/E 31.4 ≥ 30 "always expensive without ≥30% growth" (RM:64) → EPS +52.1% ≥ 30% | passes → not forced to "expensive without growth" | **verified** |
| V39 | PEG column of D-table = NTM P/E ÷ EPS growth NTM | NVDA 0.337 (0.34 ✓), MA 1.457 (1.46 ✓), ASML 0.603 (0.6 ✓), MSFT 1.249 (1.25 ✓), NFLX 0.714 (0.71 ✓), V 1.644 (1.65 ✓), ADSK 1.916 (1.93 ✓ within 8.25–8.35% growth rounding), 005930.KS 0.052 (0.05 ✓). **ABNB** PEG 0.94 only reproduces with the 24-month geometric mean 27.5%, not with NTM 36.7% (0.71) | **verified** for 8 of 9; ABNB shows the PEG denominator differs by surface → E11 |
| V40 | "Missing" arithmetic in "next verdict" text: ORCL 55 − 51.5 = 3.5; GOOG 80 − 78.0 = 2.0, base CAGR 15 − 13.2 = 1.8; META 80 − 75.2 = 4.8 | all exact | **verified** |
| V41 | Verdict counts: 2+10+25+20+20+27 = 104 (RS:182) | = "104 shown" | **verified** |
| V42 | Matrix cell counts vs verdicts: STRONG BUY 2 = A·cheap 2 (2/2 reviewed) ✓; BUY 10 = B·cheap 4 + B·fair 6 ✓; A·exp+grow 4/4 reviewed = MA, ASML, MSFT, V ✓ | consistent | **verified** |
| V43 | "B·fair: 6 (3 reviewed)" vs an expanded list of 8 (OQ#3) | If final BUY = 10 = 4 + 6, the two extra names in the expanded list are cell-BUY names whose verdict was changed by later steps (5 overridden overall) | **plausible** ([I]); explains E4 partially |
| V44 | BUY zone 16 vs 12 plotted (OQ#5) | 12 = STRONG BUY 2 + BUY 10 = final-verdict BUY set; 16 likely = matrix-cell BUY set incl. 4 later downgraded ([I]) | **plausible** ([I]) |
| V45 | x2 CAGR pairs for other tickers in D (MA 14.7/18.9, ASML 13.5/17.7, MSFT 17.5/21.8, NFLX 18.0/20.1, V 12.3/16.5, ADSK 12.2/17.5, META 17.4) | EPS paths and multiples not captured | **cannot-verify** |
| V46 | ORCL: level D 51.5 "missing 3.5 to >55" with "critical flags: capex > operating cash, customer concentration 2–3 clients, FCF negative several quarters" | Independently consistent with this repo's own view: Phase 01 FAIL on ROIC 9.05%, FCF 3-year positivity, Net Debt/EBITDA 2.93× (`watchlist/not-in-portfolio/ORCL/ORCL-2026-06-12.md`, 2026-06-12 row). Prices differ ($182.77 then, $132.63 in the Matrix) | **verified** (direction) |

## 2. Internal-consistency audit (RM vs RS vs `screens/*`)

Each row: location, problem, proposed correction (no file was edited).

| # | Where | Problem | Proposed correction |
|---|---|---|---|
| C1 | `RM:8` vs `RM:27,45` | Line 8 says D/E boundaries are "not shown yet… below 55 presumably D/E"; line 27 states D = below 55 and line 45 lists the E triggers | Delete/mark line 8 as superseded |
| C2 | `RM:27` vs `RM:31-44` | "Unknown = 40% of the component's weight" is true for growth/moat only (V33) | "Unknown values get a neutral, component-specific value (about 40–86% of the sub-score maximum); never zero" |
| C3 | `RM:28` vs `RM:39-41` | Capital & SBC sub-point maxima 6+8+7 = 21 ≠ weight 10 (V32) | Re-capture the table or state a rescale factor; do **not** implement from the current text |
| C4 | `RM:74` (STRONG BUY needs price word "Дешево") vs `RS:107`, `RS:181`, `RM:76` | GOOG (B, fair) is told "BUY → STRONG BUY at score > 80 or base CAGR > 15%", ADSK (B, fair) "would be STRONG BUY after review", and `RM:76` says a STRONG BUY "is downgraded to BUY" by the CAGR check — all imply fair-priced STRONG BUY candidates. But A×fair = BUY in the map (`RM:98`) | Either STRONG BUY can also come from A/B×fair or the compare-page text is generic. Mark `LIVE` (E9) |
| C5 | `RM:63` vs `RM:65` | "Expensive but growing" = EPS growth ≥ 15% (A: 14%) in one line; "expensive without growth only when base CAGR is below the BUY bar (14%/15%)" in the next | State precedence (which test first) or that both must hold |
| C6 | `RM:59` vs `RS:80,168` | History lens defined with **5y min ×1.05 / 3y max ×0.95 / average**; the card shows "3-year average"; NVDA +2 needs the 5y min, which is not printed | Print all three reference values per lens; `LIVE` |
| C7 | `RS:66` (x2 base = min(current, **3-year average** 21.8)) vs `RS:80` (history lens "3y trailing average 29.1", forward history "6 days of 365 snapshots") | Two different "3-year averages" for the same company; the x2 one (21.8) cannot have come from the 6 forward snapshots | Document the source of each (probably a vendor-provided historical ratio series for x2 vs own trailing series for the lens) — E10, `LIVE` |
| C8 | `RS:63`, `RM:76` | "Max 25% per step" for the decay — the observed step is 5% relative (×0.95) | Clarify: relative reduction ≤ 25% per step, or floor? (E14) |
| C9 | `RS:194` (E8) | "Lens caps imply ±10 max" | Replace by +8/−9 (+9 with the mega-cap tweak) — V23 |
| C10 | `RS:191` (E5) | "E triggers wider than the score scale suggests" | RBRK/CRWD/NET are loss-making software companies; `RM:45` "loss-making" already explains Level E regardless of score (consistent with this repo's own "RBRK: fails quality gates", `portfolio/holdings.md:69`) — resolved, [I] |
| C11 | `RS:169` vs `CC:27` | ABNB "share count flat" (flag text) vs ten-signs "shares −5%, buyback 4%" | Reconcile the two statements (probably 1-year vs current); cosmetic |
| C12 | `RS:170` vs `RS:174` | ORCL "NTM P/E 15" while trailing P/E 21.0 vs 3y 37.6: check that "15" is NTM and not a typo for 25 (price −53% in a year makes 15 plausible) | Low priority; cannot-verify |
| C13 | `RS:174` GOOG/META | The compare page values "NTM P/E 20.5, PEG 0.49, EPS +42.3% (11 analysts)" are attributed ambiguously to one of GOOG/META; PEG 0.49 = 20.5/42.3 ✓ internally consistent, but for META the "buy at NTM P/E 14.3, price < $477" (`RS:107`) implies NTM EPS ≈ $33.4, which would make current NTM P/E for a $578 price ≈ 17.3 — a P/E of 20.5 fits GOOG | Assign +42.3% / 20.5 / 0.49 to GOOG [I] and re-capture META's row (`LIVE`) |
| C14 | `RS:79-81` "cheap ≥ +4" and STRONG BUY | ABNB "fair ≥ +1"; there is no printed rule for what happens between +1 and +3 (fair) vs "cheap" for level C (map says C·cheap → BUY) | Fine, only a documentation note |
| C15 | `RM:69` | "Special cell: level A with PEG < 0.5 → BUY regardless of price word/lens sum." No D-table row exercises it (NVDA has PEG 0.34 but is already A·cheap) | Keep as "unverified rule"; do not import |
| C16 | `RS:182` "164 in the tester's set / 546 computed" vs `screens/screener.md:8` "164 total" | Two different universe definitions; not explained on the site | Note only |
| C17 | `RM:8` "range about −6…+8" | Only a practical range; theoretical −9…+9 (V23) | Add theoretical bounds |

## 3. Supplement section E and `open-questions.md`: resolve or sharpen

| Item | Status now | What I could establish | Needs live site? |
|---|---|---|---|
| E1 — ABNB S&P lens −1 | **Sharpened** | `RM:53`: "if consensus is non-GAAP, NTM P/E with options is also computed; S&P lens and PEG use the more expensive". If the with-options multiple is > 26.13 (= 1.3 × 20.1), the −1 follows. Rounding excluded (V13). But then PEG 0.94 would also use it, and 25.9/27.5 = 0.94 shows the plain multiple — so the with-options multiple is either not used in PEG or the card prints the plain one | **Yes** — does the ABNB card show a with-options P/E? |
| E2 — Growth 13.8 | **Sharpened** | 13.8 = 4.8 + 6.0 + 3.0 is the only arithmetic combination (V31) → EPS bucket 15–25%. Candidate explanations [I]: (a) the growth component uses the *second-step* 18.9% only, not the geometric mean; (b) it uses a tax-normalised NTM growth; (c) an FCF bucket differs. (a) or (b) most likely | **Yes** — ABNB "Рівень якості" tile text ("EPS growth used …") |
| E3 — BUY bar for level A | **Open, testable** | A-level card with base CAGR in [14.0, 15.0): MA (A) shows 14.7% — its x2 tile would print "BUY from 14.0%" or "15.0%" | **Yes** — MA x2 tile |
| E4 — Counts | **Partly resolved** | 104 = sum of verdict bars (V41); STRONG BUY 2 and BUY 10 reconcile to cells (V42); the extra two in B·fair are downgraded later (V43); 164 vs 546 are different universes ([I]) | No (residual: the exact definition of 57) |
| E5 — Level E at score 55–59 | **Resolved** [I] | loss-making rule (`RM:45`) — see C10 | No |
| E6 — "Gate 3" | **Open** | Methodology lists Gate 0, 1, 2 + matrix + "post-matrix" (`RM:17`); "gate 3" is probably the post-matrix step [I] | **Yes** (basis-switcher wording) |
| E7 — "x2 reached in year N" | **Resolved** [I] | linear interpolation on the yearly price path (V7) | Optional second data point |
| E8 — scatter bound and 4 unplotted | **Resolved / corrected** | bound is +8 (+9); 4 unplotted = cell-BUY names downgraded later [I] (V23, V44) | No |
| OQ#1, #2, #8, #9, #10 | **Not needed** for the review | access, writes, mobile, privacy — irrelevant to the framework comparison | — |
| OQ#3 | see E4 | | |
| OQ#4 | see E5 | | |
| OQ#11 (data freshness) | **Resolved** | nightly recompute; histories accumulate from 14–19.09.2026 (`RS:131`) | No |
| OQ#12 (600+ thresholds in settings) | **Fact-check** | Constants in `RS:137-162` are the *printed* subset. Any re-implementation must treat the remaining settings as unknown | No |
| OQ#13 bullets | see below | | |
| x2 "buy-price" table rows | **Not needed** | The design defines it from first principles: `BuyPrice(target) = Price5_base / (1+target)^5` (identical to the site's *purpose*); the site's exact rows add nothing | No |
| Decay formula 3–5 | **Resolved** | ×0.95 per step (V2, V4) | No |
| Flag thresholds | **Open** | Only debt (1.5×/3×/5×), concentration (25/33/40%), dividend 60% of FCF, SBC 30% FCF kill-line, tax 10 pts, OCF-vs-revenue 5% are printed | Yes, one pass over the flag table would help (see open-questions-for-user.md) |
| Basis switcher, the author "Оцінка" values, ambiguous GOOG/META row | **Open** | low value for this review | Optional |

## 4. Confidence grading — rule blocks as a re-implementation spec

| Rule block | Confidence | Why |
|---|---|---|
| Matrix map (level × price word → verdict) | **High** | 5×5 map stated twice (`RM:68`, `RM:98`) and reproduced by 13 test-vector rows (V34) |
| Level cut-offs A ≥ 80 / B ≥ 70 / C ≥ 55 / D < 55, rounding to 0.1 | **High** | multiple sources |
| Quality: profitability, margin, balance, discipline, growth buckets | **Medium-High** | values reproduce (V24-V29); growth EPS bucket unresolved (V31) |
| Quality: predictability (by business type) | **High** as a table; **Low** as automation | manual tag by the author |
| Quality: moat + AI adjustment | **Medium** | values consistent, AI tag is manual |
| Quality: capital & SBC | **Low** | arithmetic inconsistent (V32) |
| Unknown-value handling | **Low-Medium** | rule text contradicted by its own tables (V33) |
| Level caps and E triggers | **Medium** | list clear, order/interplay not observed |
| Hysteresis (2 pts level, 5% lenses) | **Medium** | parameters stated, no observed instance |
| Lenses: PEG, FCF-yield-after-SBC, growth vs market | **High** | verified on ABNB and NVDA |
| Lens: vs S&P | **Medium** | E1 unresolved |
| Lens: vs own history | **Medium** | window/source ambiguity (C6, C7) |
| Price-word rules (trap, cheap ≥ 4, fair ≥ 1, expensive but growing) | **Medium-High** | plus C5 precedence question |
| Mega-cap 2026 tweak | **Medium** | one instance |
| x2 arithmetic (base/pessimistic/optimistic; decay; CAGR) | **High** | reproduced on two companies (V1–V9); segmentation of consensus into 12-month steps is **Low** |
| BUY / lower CAGR bars 15/14 and 10 | **Medium** | A-level bar unobserved (E3) |
| STRONG BUY conditions | **Low-Medium** | C4 contradiction; review flag is manual |
| Red-flag catalogue | **Low** (thresholds mostly hidden), **Medium** for the ~8 numeric ones | `OQ#13` |
| Data completeness (97%, 80%, 60%) | **Low-Medium** | critical field list unknown |
| Portfolio aggregation (skip and renormalise) | **High** | fully specified with a worked example (`RS:122`) |
| Change feed / history / "what must change" logic | **Medium** | behaviour observed, generation logic inferred (`RS:110`) |
| Reader position limits by level (10/15/5/1) | **High** as stated but **not a rule of the engine** (advice) | `RS:125` |

## Appendix A — reproduction script (Python, no external data)

```python
import math
eps1, g = 6.02, [.189, .198, .188, .179, .170]
path = [eps1]
for x in g: path.append(path[-1] * (1 + x))          # 6.02 ... 14.052
P0 = 156.08
for M, eps in [(21.8, 14.03), (16, 9.36), (26.2, 14.01)]:
    print(round(eps * M, 2), round(((eps * M / P0) ** .2 - 1) * 100, 2))   # 305.85 14.40 | 149.76 -0.82 | 367.06 18.65
# pessimistic growth path: halve consensus steps 1-2, then x0.95
pg = [.945, .099, .099 * .95, .099 * .95 ** 2, .099 * .95 ** 3]
# doubling year, constant optimistic multiple
r = [e * 26.2 / P0 for e in path]                     # 1.710 at t=3, 2.016 at t=4
t = 3 + (2 - r[3]) / (r[4] - r[3])                    # 3.947
geo = math.sqrt(1.367 * 1.189) - 1                    # 0.2749
```

## Glossary

Terms already in [framework/glossary.md](../../framework/glossary.md): **EPS** (earnings per share — net income ÷ shares outstanding); **CAGR** (compound annual growth rate); **Forward PE** (price ÷ next-twelve-months expected EPS); **NTM** (next twelve months); **TTM** (trailing twelve months); **FCF yield** (free cash flow ÷ market cap or EV); **PEG ratio**; **SBC** (stock-based compensation); **ROIC**; **Moat**; **Net Debt/EBITDA**; **Effective tax rate**; **Composite Score / Quality Score / Valuation Score**; **8-K / 10-K** (SEC filings); **EDGAR**.

New terms (not yet in glossary.md — proposed definitions):
- **Consensus** — the average of professional analysts' published forecasts for a company (e.g. next-year EPS).
- **Lens (Matrix)** — one of five separate price checks in the Matrix, each scoring −2 … +2; their sum decides the "price word".
- **Price word (Matrix)** — the Matrix's one-word verdict on valuation: cheap / fair / expensive-but-growing / expensive-without-growth / value trap.
- **Gate 0 / competence circle** — a pre-analysis filter that asks "do I understand this business type at all?" (Buffett's "circle of competence").
- **x2 arithmetic** — the Matrix's five-year projection: EPS path × an assumed future multiple → future price → yearly return (CAGR).
- **Hysteresis** — a rule that makes a state change harder to reverse than to trigger (enter at 80, leave only below 78), preventing flip-flopping around a threshold.
- **Cycle peak** — earnings temporarily inflated by the top of a business cycle (e.g. memory-chip prices), making a stock look cheaper than it is.
- **Tax-normalised EPS** — EPS recomputed with the company's usual tax rate instead of a one-off unusually low/high tax charge.
- **Rounding to display** — numbers on the site are shown to one decimal, so recomputed values differ slightly.

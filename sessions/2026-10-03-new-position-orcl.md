# NEW POSITION — ORCL (Oracle Corporation) — 2026-10-03 re-check

## 1. Session Header

| | |
|---|---|
| **Task type** | NEW POSITION (re-evaluation of a previously failed candidate) |
| **Date** | 2026-10-03 (Saturday; last IBKR print is Friday 2026-10-02 after-hours) |
| **Prior state on file** | [2026-09-11 session](2026-09-11-new-position-orcl.md): Quality Score **40.2 / 100.0**, FAILS the 80.0+ gate, action **PASS** (watchlist only). Reference price then: $159.62 (after-hours, post Q1 FY2027 earnings). |
| **Rate Environment Gate** | Not run — the Quality gate fails first, so no Phase 02 inputs are needed. |

## 2. Data Gaps Flagged

- No new completed fiscal year and no new quarterly report since the 2026-09-11 session. Oracle's Q1 FY2027 10-Q (quarter ended 2026-08-31, [accession 0001193125-26-389274](https://www.sec.gov/Archives/edgar/data/0001341439/000119312526389274/orcl-20260831.htm)) appeared in search results. Its figures are the same quarter already used from the 8-K Exhibit 99.1 (accession 0001193125-26-387905). I did not re-extract the 10-Q line items this session; they are not expected to differ from the earnings release, but I did not verify that.
- Search results contained a conflicting, unsourced credit-rating line (Moody's "Ba2, stable"). It contradicts the previously verified Baa2/negative-outlook record and is **not used**. Flagged for verification, not accepted.
- Press items below (force majeure, Tencent lease) come from secondary news aggregators, not primary filings. They are qualitative Rule 9 context only and feed no scored input.

## 3. Live Price (Rule 0)

IBKR, contract_id 272800 (NYSE, ORACLE CORP), fetched first this session:

| Field | Value |
|---|---|
| Last trade | **$142.37**, ts 2026-10-02 23:59:48 UTC (7:59 PM EDT, Friday after-hours), `is_close: false` |
| Prior close | $138.07 |
| Change | +$4.30 / +3.11% |
| Dividend yield (trailing) | 1.45% |
| 52-week range | $114.51 – $320.53 |
| 13-week high / 26-week high | $170.67 / $250.24 |

Independent cross-check: a press snippet (GuruFocus, 2026-10-02) states ORCL rose 3.1% to $142.30, consistent with IBKR within 0.05%.

Price vs prior references:
- vs $159.62 (2026-09-11): (142.37 − 159.62) / 159.62 = **−10.81%**. Under the 15% Rule 9 threshold.
- vs $125.99 (2026-07-16): **+13.00%**.

## 4. Rule 9 Event Check Since 2026-09-11

| Trigger | Finding |
|---|---|
| Earnings | None new. Q1 FY2027 was reported 2026-09-10 and is already in the 09-11 re-derivation. Next: Q2 FY2027 (~early December 2026). |
| Guidance | No new guidance found. FY2027 capex of $90–95B is already on record (07-16 entry). |
| Management change | None found. |
| M&A / capital plan | Press reports a ~$7B Tencent cloud-compute lease (about 100,000 AI chips) and a Wisconsin power commitment tied to the data-center buildout. Qualitative; not primary-source verified. |
| Credit / macro | No verified new rating action. S&P BBB- (2026-07-09) stands. The Moody's "Ba2" snippet is unverified and conflicts with the record (see Data Gaps). |
| Operational | Press reports Oracle filed a **force majeure** notice on its New Mexico data-center build, and the stock fell close to 5% on the news (late September). This is a delay/cost-overrun risk on the $18B financed site. It adds to, and does not relieve, the existing cash-burn thesis. |
| Dividend | $0.50 quarterly dividend, ex-date 2026-10-09. |
| Price move >15% | No (−10.81% vs the 09-11 reference). |

Net: no new fundamental data that changes any Quality Score input. The new items are qualitative and, if anything, point the same direction as the existing disqualifiers (capex intensity, delivery risk, funding reliance).

## 5. Quality Score (Phase 01)

No input to the 09-11 computation has changed (no new completed fiscal year, no new financial statements). The prior computation is carried forward unchanged:

```
Quality Score = Profitability 40.0×0.25 + Margins 79.9×0.15 + Growth 51.9×0.20
              + Balance Sheet 11.9×0.15 + Moat 40.0×0.15 + FCF Quality 0.0×0.10
              = 10.00 + 11.985 + 10.38 + 1.785 + 6.00 + 0.00 = 40.15 → 40.2
```

Full sub-score derivations, the TTM reconstruction and the SEC sources are in [2026-09-11-new-position-orcl.md](2026-09-11-new-position-orcl.md#4-quality-score-recomputation-phase-01--full-re-derivation-2026-06-29-engine-unchanged-version). Because the inputs are identical, the engine result is identical; I did not re-run the scripts on unchanged inputs.

Hard disqualifiers (current rolling window FY2024–FY2026) remain in force:
- **Not FCF-positive 3+ consecutive years**: FY2025 −$0.394B, FY2026 −$23.686B; TTM FCF −$28.72B. Fires unconditionally.
- **Net Debt/EBITDA over threshold**: 2.62× (narrow) to 3.52× (broad) TTM vs 2.5× standard; asset-light override does not apply. Fires.

**Quality Score = 40.2 / 100.0. FAILS the 80.0+ gate.** Per quality-scoring.md, Phase 02 (Rate Gate, valuation score, Composite Score, order setup) is not run.

## 6. Recommendation

**PASS — watchlist only, do not buy.** No change in score, status or action category versus the 2026-09-11 session. The stock is roughly 11% lower than the post-earnings print, but the framework acts on trailing financial facts and documented triggers, not price movement, and the trailing facts (cash burn, leverage) have not changed.

**Next review trigger:** Q2 FY2027 earnings (~early December 2026); any verified credit-rating action (confirm or refute the Moody's "Ba2" snippet); resolution of the New Mexico force-majeure / delivery-delay question; the first full fiscal year showing FCF stabilizing (FY2027 10-K, ~July 2027); Net Debt/EBITDA below 2.5× on a full-FY basis; ROIC above 15%; a >15% unexplained price move from the new reference price of **$142.37**.

## Glossary

Definitions live in [framework/glossary.md](../framework/glossary.md). Terms used in this session: 8-K, 10-K, After-hours trading, Composite Score, EBITDA, FCF, Force majeure (new this session, added to glossary.md), Gate (Quality 80.0+), Hard disqualifier, Invested Capital, Net Debt/EBITDA, Quality Score, Rate Environment Gate, ROIC, Rule 0, Rule 9, TTM (Trailing Twelve Months), Investment grade.

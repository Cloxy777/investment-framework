# Part 4 — Implementation-ready designs for the top proposals

Selected (by priority and leverage): **P-003 kill-lines**, **P-007 SBC**, **P-013 spec fixes**, **P-001 x2 arithmetic**, **P-002 cycle-peak flag**, **P-008 `/flags`**, **P-009 three-state gate**, **P-010 snapshot store**. P-016 (next-band solver) is sketched at the end because it depends on P-010. **Nothing here is applied** — code blocks are design text; command-file edits are shown as diffs inside this document only.

Conventions inherited from `scripts/scoring/` (all designs follow them):

- `python -m scripts.<module> --input file.json [--set key=value]…` (`--set` JSON-parses values, see `quality_score.py:270-281`).
- Missing/ambiguous input ⇒ `MissingInputError`, message printed to **stderr**, **exit 2** (`common.py:10-24`, `quality_score.py:310-312`). Gate failure ⇒ exit **1** (`quality_score.py:306-309`). New in this design: **exit 3** = "input present but the computation is undefined" (e.g. non-positive EPS) — printed as a normal, explicit result, never a guess.
- Output = markdown that **prints every sub-step** (`render_markdown` pattern), so the caller can paste it verbatim into the session log ("no black-box outputs", `operating-brief.md:12`).
- Shared helpers from `scripts/scoring/common.py`: `MissingInputError`, `require`, `clamp`, `round_boundary`, `format_md_table`.
- Score rounding unchanged: `round_boundary` (half-up).

Test-case checklist used in every design (from the brief): **negative EPS**, **missing consensus**, **recent IPO** (no history), **fiscal-year change** (non-calendar year, or a change of year-end), **non-USD listing**.

---

## D1 — P-003: kill-lines (`scripts/kill_lines.py`)

### Input schema (`generate`)

```json
{
  "ticker": "ABNB",
  "report_date": "2026-11-05",
  "currency": "USD",
  "asset_light_override": false,
  "prior": {
    "revenue_yoy_pct": 9.6,
    "gross_margin_pct": 82.1,
    "gross_margin_pct_prior_year_quarter": 82.9,
    "fcf_ni_ttm_pct": 118.0,
    "fcf_ni_quarterly_below_70_count": 0,
    "net_debt_to_ebitda": -0.4,
    "eps_growth_minus_rev_growth_pp": 4.0,
    "eps_growth_minus_rev_growth_years_over_10pp": 0,
    "guidance_cut_consecutive_quarters": 0,
    "sbc_pct_fcf": 13.0
  },
  "lines": [                                   // optional overrides / additions (K8)
    {"id": "K8", "metric": "nights_and_seats_booked_yoy_pct", "operator": "<", "threshold": 0.0,
     "consecutive": 2, "action": "RESCORE", "source": "company KPI table"}
  ]
}
```

`generate` fills K1–K7 from the repo's **existing** thresholds (constants in the module with the doc line each came from) and appends user-defined lines. Nothing numeric is invented: K1 threshold is read from a single constant `PHASE01_REVENUE_FLOOR_PCT` that P-013(c) pins to `quality-scoring.md`.

### Input schema (`check`) — after the report

```json
{ "ticker": "ABNB", "report_date": "2026-11-05",
  "actual": {"revenue_yoy_pct": 8.1, "gross_margin_pct": 81.0, "gross_margin_pct_prior_year_quarter": 82.9,
             "fcf_ni_quarterly_below_70": false, "net_debt_to_ebitda": -0.3,
             "eps_growth_minus_rev_growth_pp": 3.0, "guidance_cut": "unknown",
             "sbc_pct_fcf": 15.0, "nights_and_seats_booked_yoy_pct": null} }
```

### Function signatures

```python
# scripts/kill_lines.py
from dataclasses import dataclass
from scripts.scoring.common import MissingInputError, require

@dataclass(frozen=True)
class KillLine:
    id: str                # "K1".."K8"
    metric: str
    operator: str          # "<" | ">" | "<=" | ">="
    threshold: float | int | bool
    consecutive: int       # how many consecutive periods must breach (1 or 2)
    action: str            # "RESCORE" | "PHASE06_REVIEW" | "NO_ADD_UNTIL_RESOLVED"
    source_rule: str       # e.g. "strategy.md:86"

def default_lines(asset_light: bool) -> list[KillLine]: ...
def generate(d: dict) -> dict: ...            # returns {"lines": [KillLine...], "markdown": str}
def evaluate_line(line: KillLine, actual: dict, prior: dict) -> str: ...
    # returns "TRIGGERED" | "OK" | "UNKNOWN"; None / "unknown" -> UNKNOWN (never OK)
def check(d: dict) -> dict: ...               # per-line status + overall next steps
def render_markdown(result: dict) -> str: ...
```

### Rules (pseudocode)

```
K1 revenue_yoy_pct        <  PHASE01_REVENUE_FLOOR_PCT      -> TRIGGERED, action RESCORE
K2 gross_margin_pct       <  prior_year_quarter - 3.0         -> RESCORE        (strategy.md:85; fair-value-methodology.md:92)
K3 fcf_ni quarter <70 and prior count == 1                   -> RESCORE + NO_ADD (strategy.md:86: 2 consecutive quarters)
K4 guidance_cut == True and prior consecutive >= 1           -> PHASE06_REVIEW   (strategy.md:90,111); single cut with named one-off -> RESCORE only
K5 net_debt_to_ebitda     >  (4.0 if asset_light else 2.5)     -> RESCORE + NO_ADD (quality-scoring.md:21)
K6 eps_growth - rev_growth > 10 and prior years_over_10 >= 1  -> RESCORE        (strategy.md:89)
K7 sbc_pct_fcf            >  30.0  (optional, needs P-007)    -> RESCORE
K8 analyst-defined
UNKNOWN never collapses to OK: an UNKNOWN line prints "DATA NEEDED: <field>" and keeps the RESCORE due.
```

### CLI

```
python -m scripts.kill_lines generate --input abnb_pre.json  > portfolio/kill-lines/ABNB.md
python -m scripts.kill_lines check    --input abnb_post.json          # exit 0 all OK, 1 any TRIGGERED, 2 missing input
```

### Output format (markdown; all lines printed)

```
## Kill-lines — ABNB — report 2026-11-05
| ID | Metric | Rule | Threshold | Prior | Action if breached | Source rule |
|----|--------|------|-----------|-------|--------------------|-------------|
| K1 | revenue YoY % | < | 10.0 | 9.6 | RESCORE | strategy.md:16 |
…
## Result
| ID | Actual | Status |
| K1 | 8.1 | TRIGGERED |
| K4 | unknown | UNKNOWN — DATA NEEDED: guidance |
Next steps: /rescore ABNB within 3 business days (operating-calendar.md:31); K3 TRIGGERED → no add until resolved.
```

### Tests (`scripts/tests/test_kill_lines.py`)

| Case | Expectation |
|---|---|
| Boundary: K1 with actual == threshold | OK (strict `<`) |
| K3: first quarter <70 | OK; second consecutive ⇒ TRIGGERED |
| **Negative EPS** (K6 inputs use EPS growth): actual EPS growth undefined | K6 = UNKNOWN, not OK |
| **Missing consensus** | K1–K8 do not use consensus ⇒ generation still works (documented) |
| **Recent IPO** (no prior-year quarter) | K2 = UNKNOWN |
| **Fiscal-year change** (short transition quarter) | K1/K2 flagged `UNKNOWN` when `period_days` outside 350–380 for yoy fields |
| **Non-USD** | thresholds are percentages; no currency conversion; `currency` echoed |
| Asset-light | K5 threshold 4.0 |
| Unknown guidance | K4 = UNKNOWN and RESCORE stays due |

### Command-file edits (diff shown, not applied) — see section "Diffs" at the end.

---

## D2 — P-007: SBC disclosure (A) and SBC-adjusted FCF yield (B)

### Inputs added to the existing JSON schemas (`valuation_score.py` docstring lines 13-39)

```json
{
  "sbc_ttm": 640.0,                     // SBC in the same currency and units as fcf, market cap
  "fcf_ttm": 1980.0,
  "market_cap": 45000.0,
  "owner_earnings_used": false,         // true if Upgrade 1 replaced FCF with Owner Earnings
  "sbc_adjust": false                   // Phase A: false. Phase B (after adoption): true
}
```

### Functions

```python
# scripts/scoring/sbc.py
def sbc_metrics(sbc_ttm: float, fcf_ttm: float, market_cap: float) -> dict:
    """Returns {"sbc_pct_fcf": float | None, "fcf_after_sbc_yield_pct": float}.
       sbc_pct_fcf is None when fcf_ttm <= 0 (printed as 'n/a — FCF <= 0').
       market_cap <= 0 or missing -> MissingInputError."""

# scripts/scoring/valuation_score.py  (Phase B only, flag-controlled)
def _fcf_yield(d) -> tuple[float, list]:
    fy = require(d, "fcf_yield_pct")
    if d.get("sbc_adjust") and not d.get("owner_earnings_used"):
        sbc_y = require(d, "sbc_yield_pct", "SBC-adjusted FCF yield")      # 100*sbc_ttm/market_cap
        fy_used = fy - sbc_y
        steps = [f"FCF yield {fy}% - SBC yield {sbc_y}% = {fy_used}% (SBC treated as a cost; Owner Earnings names excluded because GAAP NI already bears SBC)"]
    else:
        fy_used, steps = fy, []
    score = clamp(100 * (1 - fy_used / 10))
    steps.append(f"FCF_Score = clamp(100x(1 - {fy_used}/10)) = {score:.3f}")
    return score, steps
```

`_upside_downside` gets one guard: if `sbc_adjust` is true, `net_buyback_yield_pct` must be the **gross cash** buyback yield (assert via a required field `buyback_yield_basis == "gross_cash"`), otherwise `MissingInputError` — prevents counting SBC dilution twice (once in the yield, once in shareholder yield).

### CLI

```
python -m scripts.scoring.sbc --input fundamentals.json            # Phase A: prints the block only
python -m scripts.scoring.valuation_score --input inputs.json --set sbc_adjust=true    # Phase B, after adoption
```

### Output format (Phase A block, added to `/new-position` and `/rescore` inputs)

```
SBC block (TTM)
  SBC $640.0M   FCF $1,980.0M   Market cap $45,000M
  SBC/FCF = 32.3%          -> above the 30% kill-line (P-003 K7)
  FCF yield (reported)      = 4.40%
  FCF yield after SBC       = 2.98%
```

### Tests (`test_sbc.py`, `test_valuation_score.py` additions)

| Case | Expectation |
|---|---|
| `fcf_ttm = 0`, or **negative** FCF | `sbc_pct_fcf = None`; after-SBC yield computed from `(fcf − sbc)` (negative) |
| `sbc_ttm > fcf_ttm` | after-SBC yield < 0 ⇒ `FCF_Score` = 100.0 (clamp) |
| **Negative EPS**/loss-making | independent of EPS; block still prints (SBC is the usual reason FCF ≫ NI) |
| **Missing** `sbc_ttm` | Phase A: prints `SBC: UNKNOWN`; Phase B: `MissingInputError` (exit 2) |
| **Recent IPO** with lumpy IPO-related SBC | flagged `one_off_sbc` (manual text field required to override) |
| **Fiscal-year change** | use TTM sum of last 4 quarters, never a stub year |
| **Non-USD listing** | all three quantities must be in the same currency; script refuses mismatched `currency` fields |
| Owner-Earnings name | `sbc_adjust` ignored, note printed |
| Double-count guard | `sbc_adjust=true` with `buyback_yield_basis != "gross_cash"` ⇒ exit 2 |

---

## D3 — P-013: specification fixes

**(a) PEG denominator** — documentation text for `valuation-scoring.md` (after line 87):

```
PEG growth input (clarified): PEG = Forward PE ÷ G, where
  G = 100 × ( sqrt( (1 + g_ntm) × (1 + g_next) ) − 1 )
  g_ntm  = consensus EPS growth for the next twelve months (decimal), on a clean earnings base (see P-018)
  g_next = consensus EPS growth for the following twelve months (decimal)
If only one step exists, G = that step. If neither exists, PEG is not applicable and its 15% weight is redistributed to EV/EBIT.
```

Check against a verified vector: ABNB g_ntm 0.367, g_next 0.189 ⇒ G = 27.49% (`01-verification.md` V10).

**(b) Historical-PE modifier, 10–20% band** — replace `valuation_score.py:96-131` with a helper (design; behaviour is identical outside the band):

```python
def _historical_pe_modifier(deviation: float, d: dict) -> tuple[float, str]:
    """Continuous fill of strategy.md Upgrade 2's undefined 10-20% band."""
    if deviation <= -20:      m, why = -10.0, ">20% below 5yr avg -> -10"
    elif deviation < -10:     m, why = -10.0 * (abs(deviation) - 10) / 10, "10-20% below avg -> linear -10..0"
    elif deviation <= 10:     m, why = 0.0, "within +-10% of 5yr avg -> 0"
    elif deviation < 20:      m, why = 10.0 * (deviation - 10) / 10, "10-20% above avg -> linear 0..+10"
    else:                     m, why = 10.0, ">20% above 5yr avg -> +10"
    if m > 0 and d.get("structural_quality_override"):
        evidence = d.get("structural_quality_override_evidence")
        if not evidence:
            raise MissingInputError("'structural_quality_override' is true but evidence is missing")
        return 0.0, f"{why}; Structural Quality Override applies ({evidence}) -> 0"
    return m, why
```

Tests (`test_valuation_score.py`): deviation −25 → −10; −20 → −10; −15 → −5; −10 → 0; 0 → 0; +10 → 0; +12 → +2; +15 → +5; +20 → +10; +15 with override → 0; +15 with override but no evidence → exit 2; `pe_mode="none"` unchanged (50.0); **negative EPS** (forward PE undefined) → existing `MissingInputError` path; **recent IPO** → `pe_mode="none"`; **fiscal-year change** → historical series must not mix stub periods (documented in `fetch_fundamentals`); **non-USD** → P/E is currency-neutral; the ratio uses one listing's price and its own-currency EPS.

**(c) Phase 01 threshold drift** — replace the duplicated numeric thresholds in `strategy.md:14-18`, `valuation-scoring.md:205-214`, `operating-calendar.md:92-100` with a link to `quality-scoring.md` and a one-line note. Decision needed: which numbers are canonical (the 80.0-gate formulas are the only *scored* rules). Until decided, the design suppresses none of them.

Version handling: (a) and (c) are documentation; (b) bumps `valuation-scoring.md:5` and triggers `python -m scripts.stale_score` (only entries whose recorded inputs fall in the band change score).

---

## D4 — P-001: x2 arithmetic (`scripts/scoring/x2_arithmetic.py`)

### Input schema

```json
{
  "ticker": "ABNB",
  "price0": 156.08,                 // Rule 0: live price (required)
  "currency": "USD",
  "basis": "ntm",                   // "ntm" | "ttm": ALL multiples and eps0 use this basis
  "eps0": 6.02,                     // > 0 required
  "g1": 0.189, "g2": 0.198,         // consensus growth steps (decimals). basis=ttm: g1 = NTM/TTM - 1
  "n_analysts": 22,                 // optional; below MIN_ANALYSTS (3, placeholder) -> exit 3 'thin consensus'
  "m_now": 25.9,
  "m_avg": 21.8,                    // optional; absent -> base multiple = m_now, flag NO_HISTORY
  "m_low": null,                    // optional; absent -> pessimistic scenario NOT computed (never a default)
  "decay": 0.95, "haircut": 0.5,    // optional overrides (placeholders documented in 03-proposals P-001)
  "n_years": 5,
  "targets_pct": [10, 15],          // buy-price curve targets (10 = repo hurdle H)
  "expected_annual_return_pct": null // optional E from valuation_score for the cross-check
}
```

### Signatures and pseudocode

```python
def growth_path(g1: float, g2: float, n: int, decay: float, haircut: float = 1.0) -> list[float]:
    g = [g1 * haircut if g1 > 0 else g1, g2 * haircut if g2 > 0 else g2]
    while len(g) < n:
        prev = g[-1]
        g.append(prev * decay if prev > 0 else prev)      # declines are not "decayed" toward zero
    return g[:n]

def eps_path(eps0: float, g: list[float]) -> list[float]:  # eps_t, t = 0..n
    out = [eps0]
    for x in g: out.append(out[-1] * (1 + x))
    return out

def scenario(eps0, g, m, price0, n) -> dict:
    e = eps_path(eps0, g)
    price_n = e[n] * m
    cagr = (price_n / price0) ** (1 / n) - 1
    ratios = [x * m / price0 for x in e]                   # doubling: first t with ratio >= 2, linear interpolation
    ...
    return {"eps_n": e[n], "price_n": price_n, "cagr": cagr, "doubling_year": dbl}

def buy_price(price_n_base: float, target_pct: float, n: int) -> float:
    return price_n_base / (1 + target_pct / 100) ** n

def compute(d: dict) -> dict: ...   # validates; raises MissingInputError (exit 2) or NotComputable (exit 3)
```

Validation rules (each a named exception, never a fallback): `price0 > 0`; `eps0 > 0` else `NotComputable("eps0 <= 0 (loss-making or missing base)")`; `0.75 <= decay <= 1.0`; `n_analysts` (if given) ≥ 3 else `NotComputable`; `m_now > 0`; `m_avg`/`m_low` > 0 if present; `basis` in `{"ntm","ttm"}`.

### CLI

```
python -m scripts.scoring.x2_arithmetic --input abnb_x2.json
python -m scripts.scoring.x2_arithmetic --input abnb_x2.json --set expected_annual_return_pct=17.1
```

### Expected output on the verified ABNB vector (Rule 0 date 2026-09-29; test fixture)

Reference vector (`01-verification.md`): `eps0 6.02, g1 0.189, g2 0.198, m_now 25.9, m_avg 21.8, price0 156.08, decay 0.95`. Design output computed with the spec above:

```
## x2 arithmetic — ABNB (basis: ntm, price0 $156.08, n = 5)
growth path (base):        18.90%  19.80%  18.81%  17.87%  16.98%        (decay 0.95 after step 2)
EPS path:                  6.02 → 7.16 → 8.58 → 10.19 → 12.01 → 14.047
| Scenario    | Growth used        | Multiple | Price in 5y | CAGR    | x2 reached |
| pessimistic | not computed (no m_low) | —   | —           | —       | —          |
| base        | consensus, decay   | 21.80 (min(25.9, 21.8)) | $306.23 | 14.43% | no |
| optimistic  | consensus, decay   | 25.90 (no compression)  | $363.82 | 18.44% | year 4.02 |
Buy-price curve (base price in 5y $306.23):
| Target CAGR | Buy price | vs live |
| 10%         | $190.14   | +21.8% |
| 15%         | $152.25   | −2.5%  |
Cross-check: E = n/a
```

Test-only variant: `m_low = 16` with `haircut 0.5` reproduces the Matrix's pessimistic case: growth 9.45, 9.90, 9.40, 8.93, 8.49% → EPS 9.363 → price $149.80 → CAGR −0.82% (card −0.8%).

### Tests (`test_x2_arithmetic.py`)

| Case | Expectation |
|---|---|
| ABNB fixture | base CAGR 14.43 ± 0.05; base price 306.23 ± 0.5; Matrix card 14.4% / $305.87 (±0.2% tolerance documented) |
| Pessimistic fixture (`m_low 16`) | CAGR −0.82 ± 0.05 |
| Doubling interpolation | optimistic year 4.02 ± 0.02 |
| Buy price identity | `price_n_base / (1 + t)^5`; at `t = CAGR_base` returns ≈ `price0` |
| **Negative EPS** (`eps0 <= 0`) | exit 3, message "loss-making base — not computable", no number printed |
| **Missing consensus** (`g1` null) | `MissingInputError` (exit 2) naming `g1` |
| **Thin consensus** (`n_analysts = 2`) | exit 3 |
| **Recent IPO** (no `m_avg`) | flag `NO_HISTORY`, base multiple = `m_now` |
| **Negative growth step** | `growth_path([-0.05, 0.02])` → [−0.05, 0.02, 0.019, 0.01805, 0.01715] (no decay on the negative step) |
| **Fiscal-year change** | `basis="ttm"` requires `g1` = NTM/TTM − 1 computed by the caller; a stub year ⇒ caller must not pass it (documented); test on `basis` mismatch (`m_avg` given on a different basis flag) ⇒ exit 2 |
| **Non-USD listing** | `currency` must match across fields; `price0` in listing currency; output states currency; no FX conversion inside |

---

## D5 — P-002: cycle-peak flag (`scripts/scoring/flags_common.py`)

### Function

```python
def cycle_peak(eps_ttm_now: float | None, eps_ttm_1y_ago: float | None, threshold_pct: float = 100.0) -> dict:
    """Returns {"flag": "CYCLE_PEAK_CANDIDATE" | "LOSS_TO_PROFIT_BASE" | "NONE" | "UNKNOWN",
                "growth_pct": float | None, "explain": str}"""
    if eps_ttm_now is None or eps_ttm_1y_ago is None:
        return UNKNOWN
    if eps_ttm_1y_ago <= 0 < eps_ttm_now:  return LOSS_TO_PROFIT_BASE      # PEG-ineligible base (valuation-scoring.md:105)
    if eps_ttm_1y_ago <= 0 and eps_ttm_now <= 0: return NONE (loss-making: not a cycle-peak question)
    g = (eps_ttm_now / eps_ttm_1y_ago - 1) * 100
    return CYCLE_PEAK_CANDIDATE if g > threshold_pct else NONE
```

Input fields (added to `fetch_fundamentals.py` output): `eps_ttm_now`, `eps_ttm_1y_ago` (GAAP diluted; from 8 quarterly values; missing quarter ⇒ `None`). Printed line in `/new-position` and `/rescore`: `Cycle-peak check: EPS TTM +109% → CYCLE_PEAK_CANDIDATE (analyst must state why the multiple is compared with a normalised base — Rule 6)`.

### Tests

Exactly 100.0% → `NONE` (strict `>`); 100.01% → flag; prior positive/now negative → `NONE` (not a peak question; already loss-making); prior ≤ 0 < now → `LOSS_TO_PROFIT_BASE`; **negative EPS** both → `NONE`; **missing** either → `UNKNOWN`; **recent IPO** (fewer than 8 quarters) → `UNKNOWN`; **fiscal-year change** (stub) → `UNKNOWN` if the four quarters do not span 350–380 days; **non-USD** → currency-neutral (ratio of EPS in the same currency).

---

## D6 — P-008: `/flags` (`scripts/flags.py`)

### Input schema (extends the `fetch_fundamentals` JSON)

```json
{
  "ticker": "ZS", "currency": "USD", "asset_light_override": false,
  "fcf_ttm": 890.3, "fcf_quarters": [210.5, 240.1, 220.0, 219.7],   // last 4-8, newest last
  "ocf_ttm": 1010.0, "capex_ttm": 120.0,
  "net_debt_to_ebitda": -1.1, "ebit_ttm": -12.0, "interest_expense_ttm": 30.0,
  "sbc_ttm": 470.0, "dividends_ttm": 0.0,
  "diluted_shares": [140.1, 145.3, 152.0, 158.2],                    // 3-4 fiscal years, oldest first
  "fcf_ni_annual_pct": [95, 88, "n/m"],
  "eps_growth_pct": [..], "revenue_growth_pct": [..],
  "gross_margin_pct": 77.1, "gross_margin_pct_year_ago": 79.0,
  "manual": {"customer_top1_pct": null, "customer_top2_pct": null, "guidance_cut": "unknown",
             "adjusted_vs_gaap_gap": "unknown", "revaluation_profit": "unknown", "foreign_revenue_pct": null}
}
```

### Function signatures

```python
@dataclass(frozen=True)
class Flag: id: str; name: str; severity: str; status: str; value: str; threshold: str; source: str; scored_in: str
def evaluate_all(d: dict) -> list[Flag]: ...       # never raises for missing optional fields: status = "UNKNOWN"
def render_markdown(flags: list[Flag]) -> str: ...
```

### Rule table (thresholds; every non-repo number is a placeholder marked †)

| ID | Test | Severity label | `scored_in` (to avoid double penalty) |
|---|---|---|---|
| F1 | `fcf_ttm < 0` | critical | Profitability cap (`quality_score.py:106`) |
| F2 | `count(fcf_quarters < 0) ≥ 4` or TTM < 0 → critical; 1–3 with TTM > 0 → minor | critical/minor | hard disqualifier |
| F3 | `capex_ttm > ocf_ttm and fcf_ttm < 0` | critical | — |
| F4 | ND/EBITDA `> 2.5` (`> 4.0` asset-light) serious; `> 4.0` (`> 6.0`) critical | serious/critical | BalanceSheet + hard disqualifier |
| F5 | `ebit_ttm / interest_expense_ttm < 3` † | serious | BalanceSheet (partly) |
| F6 | `sbc_ttm / fcf_ttm > 0.30` (if `fcf_ttm > 0`) | serious | FCF yield if P-007 B adopted |
| F7 | `dividends_ttm / fcf_ttm > 0.60` | serious | — |
| F8 | 3-year CAGR of `diluted_shares > 2%` † | serious | — |
| F9 | `fcf_ni_annual_pct` two consecutive `< 70` | serious | FCF Quality + hard disqualifier |
| F10 | `eps_growth − revenue_growth > 10 pp` two consecutive years | serious | — |
| F11 | `gross_margin − year_ago < −3 pp` | serious | Margins |
| F12 | `customer_top1 ≥ 25` or `top2 ≥ 33` serious; `top1 ≥ 40` critical | manual | — |
| F13–F16 | guidance cut, adjusted-vs-GAAP gap, revaluation profit, foreign revenue ≥ 35% | manual / info | — |

Each row prints `PASS`, `FAIL`, or `UNKNOWN — DATA NEEDED: <field>`; a `FAIL` never changes a score.

### CLI and output

```
python -m scripts.flags --input zs_flags.json
```
```
| Flag | Severity | Status  | Value        | Threshold | Source        | Scored in      |
| F1 FCF negative TTM | critical | PASS | +890.3 | ≥ 0 | yfinance cashflow | Profitability cap |
| F6 SBC eats FCF | serious | FAIL | 52.8% | ≤ 30% † | cashflow SBC row | (P-007 B) |
| F12 customer concentration | serious | UNKNOWN — DATA NEEDED: 10-K customer table | | | manual | — |
Summary: 0 critical · 1 serious · 1 unknown
```

### Tests

Boundary at each threshold (strict vs inclusive as written); **negative EPS** → F10 `UNKNOWN`; **negative FCF** → F6 `n/a`; **missing consensus** → n/a (no consensus dependency); **recent IPO** → F8/F10 `UNKNOWN` (< 3 years); **fiscal-year change** → annual series with a stub year → `UNKNOWN`; **non-USD** → ratios only, `currency` echoed; asset-light thresholds; empty manual block → four `UNKNOWN` rows.

---

## D7 — P-009: three-state gate

### Schema additions

```json
{ "prior_gate_state": "PASS", "gate_band_pts": 2.0 }      // optional; default prior "NONE", band 2.0
```

### Function (in `quality_score.py`)

```python
GATE_BAND_PTS = 2.0   # placeholder = Matrix level hysteresis; calibrate on the watchlist history (05-validation.md)

def gate_state(score: float, disqualified: bool, prior_state: str, band: float = GATE_BAND_PTS) -> str:
    if disqualified:                                         return "FAIL"
    if score >= QUALITY_GATE:                                return "PASS"
    if prior_state in ("PASS", "AMBER") and score >= QUALITY_GATE - band:  return "AMBER"
    return "FAIL"
```

`compute()` keeps its current fields and adds `"gate_state"`; `passes_gate` stays `score >= 80.0` (so **entries and adds** still need `PASS`); `render_markdown` prints `Gate: AMBER (held; no adds; Composite adopted for hold/trim only)`. `composite_score.py`: `GateFailure` remains for `FAIL` and for new entries; for `AMBER` with `--held` returns the Composite tagged `gate_state=AMBER` (design: an explicit `--held` flag so it cannot be reached by accident).

### CLI

```
python -m scripts.scoring.quality_score --input msft.json --set prior_gate_state=\"PASS\"
python -m scripts.scoring.composite_score --input msft_pair.json --held
```

### Tests

| Case | Expectation |
|---|---|
| 79.9, prior PASS | AMBER |
| 79.9, prior NONE (new candidate) | FAIL |
| 78.0 exactly, prior AMBER | AMBER (inclusive lower bound); 77.9 → FAIL |
| 85.0 but hard disqualifier | FAIL |
| 80.0 exactly | PASS (existing rule) |
| **Negative EPS/loss-making** | Profitability inputs already handle; gate result unaffected |
| **Missing** prior state | defaults to NONE; printed |
| **Recent IPO** | prior NONE ⇒ no hysteresis |
| **Fiscal-year change** / **non-USD** | scoring unchanged |
| AMBER never reaches `order_setup` for a new entry | `/speculate` gate reads `passes_gate` (unchanged) |

Version handling: bump `quality-scoring.md:5` and `valuation-scoring.md:5`; stale-run scope = entries with a stored score in [78.0, 80.0) and a prior PASS — today only MSFT (79.9) per `portfolio/holdings.md:63`.

---

## D8 — P-010: snapshot store (`scripts/snapshot.py`)

### Record schema (`portfolio/snapshots/scores/2026-09-28.json`)

```json
{
  "date": "2026-09-28",
  "methodology_version": "2026-06-29",
  "source": "rescore|weekly|seed",
  "tickers": {
    "AVGO": {
      "price": 352.39, "currency": "USD",
      "quality": 86.3, "valuation": 71.3, "composite": 42.5,
      "gate_state": "PASS", "band": "30.0-49.9",
      "basket": "ai_infrastructure", "lynch_category": "stalwart",
      "flags": ["F6:PASS", "F1:PASS"],
      "session": "sessions/2026-09-28-rescore-avgo.md",
      "provenance": {"quality": "parsed|script", "valuation": "parsed|script"}
    }
  }
}
```

### Functions

```python
def record(tickers: dict, date: str, version: str, source: str) -> Path: ...
def diff(older: dict, newer: dict) -> dict:
    # per ticker: band change, gate_state change, added/removed flags, price change, and
    # distance to current buy limit if present in the record
def seed_from_watchlist(root: Path) -> dict:
    # regex over the FIRST table row of each watchlist/**/<T>-YYYY-MM-DD.md: date, price, valuation, quality, composite.
    # every field carries provenance="parsed"; any field the regex cannot extract is null (never guessed).
def prior_state(ticker: str, snapshots_dir: Path) -> str: ...   # feeds P-009
```

### CLI

```
python -m scripts.snapshot seed --root watchlist            # one-off bootstrap
python -m scripts.snapshot record --input today.json
python -m scripts.snapshot diff --since 2026-09-21           # markdown "what changed"
```

### Output (diff)

```
## What changed since 2026-09-21
| Ticker | Composite | Band | Gate | Flags | Price |
| AVGO | 40.0 → 42.5 | Cheap → Cheap | PASS → PASS | — | 340.1 → 352.4 |
| MSFT | 29.5 (ref) → 29.5 | — | AMBER (new) | — | … |
Unparsed fields in this diff: 2 (see provenance)
```

### Bootstrap plan

1. Day 0: `seed` from watchlist (26 in-portfolio names, 30+ not-in-portfolio); mark `provenance="parsed"`, spot-check against `holdings.md` (target ≥ 90% match).
2. From day 0: `record` at each `/rescore`/`/new-position` and in Routine 2 (weekly).
3. Consensus-revision quadrants need ~13 weekly snapshots ⇒ available ≈ 3 months after day 0; until then the output prints "not defined — accumulating (n of 13)".

### Tests

Fixture rows copied from three real watchlist tables (NVDA 2026-09-17, MSFT 2026-07-30 with the `Valuation 38.9 / Quality 79.9` prose format, ASML 2026-09-11 with `Quality Score 82.4 … Composite Score 56.1`); **negative** values (Composite can't be negative, but a valuation modifier can); **missing** score ⇒ `null` + provenance `unparsed`; **recent IPO** (no earlier snapshot) ⇒ `diff` reports `new`; **fiscal-year change** irrelevant; **non-USD** (TRN GBP, XEON EUR, RGL AUD) ⇒ `currency` stored and never converted; malformed JSON ⇒ exit 2.

---

## D9 (sketch) — P-016 `next_band`

Needs raw price-dependent inputs (`fcf_ttm`, `ebit_ttm`, `net_debt`, `shares`, `eps_fwd`, `peg_growth`, `pe_5yr_*`, fair values). Algorithm: `f(p) = composite(compute(inputs with price=p))`; monotone increasing in `p`, so bisect on `[0.2·live, 3·live]` for the largest `p` with `f(p) ≤ 49.9` and `≤ 29.9` (tolerance $0.01, max 60 iterations); if `f(0.2·live) > target` print "unreachable at any price ≥ 20% of live (quality side binding)". Quality side: `missing = 80.0 − Q`; headroom = `max_i (100 − sub_i) × w_i` from `quality_score.compute()["sub_scores"]`. Tests: known-inverse case (choose inputs, compute `f`, then solve for that price), non-monotone guard (assert `f` monotone on 20 sample points else refuse), negative EPS (forward PE undefined ⇒ refuse).

---

## Diffs — exact edits to command / routine files (shown only; nothing applied)

### `.claude/commands/rescore.md` (P-003, P-009, P-008, P-007, P-010)

```diff
@@ Steps: (after line 11)
+0. **Kill-line check (post-earnings).** If the ticker has `portfolio/kill-lines/<TICKER>.md`, run `python -m scripts.kill_lines check --input <post.json>` and paste its full output at the top of the session log. Every TRIGGERED line goes into "Fundamental changes since last review"; an UNKNOWN line is a data gap to close before scoring, not a pass.
 1. Fetch live prices first (Rule 0 in [fair-value-methodology.md](../../framework/fair-value-methodology.md)) — never infer from PE × EPS. Skip if `--quality-only` …
@@ step 2 (line 13), append:
+   Also print: the SBC block (`python -m scripts.scoring.sbc`), the flags table (`python -m scripts.flags`) and the cycle-peak line; paste all three.
@@ step 3 (line 14), replace the sentence "Flag if it has dropped below 80.0 …" with:
-   Flag if it has dropped below 80.0 (`FAILS GATE` output, or a passing score under 80.0 — Phase 04 Quality Watch escalation) — a held position dropping below the gate is itself a signal worth surfacing, even though existing holdings aren't retroactively force-exited on quality alone.
+   Read the prior gate state from the latest snapshot (`python -m scripts.snapshot prior-state <TICKER>`) and pass `--set prior_gate_state=<PASS|AMBER|FAIL|NONE>`. Report the three-state result: PASS; AMBER (held name within 2.0 pts below 80.0 — hold/trim allowed, **no adds**); FAIL. A move PASS → AMBER or AMBER → FAIL is itself a Phase 04 Quality Watch escalation; existing holdings are still not force-exited on quality alone.
@@ after the watchlist paragraph (line 23):
+**Snapshot:** after writing the watchlist entry, run `python -m scripts.snapshot record --input <today.json>` and paste its path.
```

### `.claude/commands/new-position.md` (P-006, P-007, P-008, P-002, P-001, P-016)

```diff
@@ Steps: (before line 10)
+0. **Gate 0 — competence circle.** Look up the company's basket in `framework/competence-circle.md` (`python -m scripts.competence lookup --basket <basket>`). State the basket and its state (core / stop / unclear) as the first line of the session. `stop` ⇒ stop here and report; `unclear` ⇒ ask the user to classify before any scoring.
 2. Run `python -m scripts.fetch_fundamentals <TICKER>` … Paste its output.
@@ append to step 2 (line 11):
+   Then run `python -m scripts.flags`, `python -m scripts.scoring.sbc` and the cycle-peak check; paste their output. Record `lynch_category` (analyst-assigned, with the reason).
@@ after step 4 (line 13):
+4b. **Expected-return cross-check.** Run `python -m scripts.scoring.x2_arithmetic --input <x2.json>` (consensus growth steps required; if unavailable, say so — do not estimate). Paste the scenario table, the buy-price curve (10% / 15%) and the E-vs-consensus line. It never changes the score; it informs the limit price and the R/R discussion.
@@ step 5 (line 14), append:
+   Add the "next band" line: `python -m scripts.scoring.next_band --input <inputs.json>` (P-016) once available.
```

### `.claude/commands/rebalance.md` (P-011, P-012, P-016)

```diff
@@ Steps (after line 8)
+1b. Run `python -m scripts.portfolio_metrics` and paste the weighted Quality / Valuation / Composite with **coverage (total and equity)**, the missing tickers by name, and the stale entries excluded. Never zero-fill a missing metric.
@@ after step 4 (line 16)
+4b. Cluster report: `python -m scripts.portfolio_metrics --clusters portfolio/clusters.md`. If any cluster ≥ 30% of the book, write a one-paragraph acknowledgement (why the shared risk thesis is understood) in the session log. This is a report, not a cap.
```

### `.claude/commands/screen.md` (P-006, P-008, P-002)

```diff
@@ Step 1 — Structural triage (lines 21-23)
-Before spending analysis budget on every candidate, eliminate names that plainly fail Phase 01 on well-documented business-model grounds: thin-margin volume retail, commodity cyclicals, patent-cliff pharma, regulated utilities, etc. Flag every elimination with one-line reason so any name can be pulled back on request.
+Before spending analysis budget on every candidate, look up each name's basket in `framework/competence-circle.md`: baskets in state `stop` are eliminated with the registry's one-line reason; `unclear` is listed for the user. Names whose basket is not in the registry are triaged as before (structural grounds) and proposed for the registry. Flag every elimination with a one-line reason so any name can be pulled back on request.
@@ Step 2 (line 27), append:
+Print the F1–F4 flag subset and the cycle-peak line next to each survivor's numbers.
```

### `.claude/commands/telegram-scan.md` (P-006, P-003)

```diff
@@ step 4, decision list (after line 21)
+     - Resolved ticker whose basket is `stop` in `framework/competence-circle.md` and no watchlist entry exists → **no action**; log "stop-list — <basket>" in the mention row. (Saves a full `/new-position` run.)
@@ step 4 (after the Rule 9 bullet, line 20)
+   - If the post names an earnings date within 7 days for a held name and no `portfolio/kill-lines/<TICKER>.md` exists, generate it (`python -m scripts.kill_lines generate`).
```

### `framework/automation-schedule.md` — Routine 2 prompt (P-003, P-010, P-011)

```diff
@@ Routine 2 prompt, after step 2 (line 177)
+2b. For each holding with an earnings date in the next 7 days, run
+   `python -m scripts.kill_lines generate --input <ticker>_pre.json` and commit
+   portfolio/kill-lines/<TICKER>.md in the same PR; list the ticker and the
+   file in the weekly brief.
@@ after step 5 (line 191)
+5b. Run `python -m scripts.snapshot record` and `python -m scripts.portfolio_metrics`;
+   include the weighted Quality/Composite with coverage in the weekly brief and
+   the "what changed since last week" table (`python -m scripts.snapshot diff --since <last Monday>`).
```

### `framework/valuation-scoring.md`, `strategy.md`, `quality-scoring.md` (P-013, P-007, P-009)

```diff
@@ valuation-scoring.md line 87 (after "No-history fallback"): add the PEG-growth paragraph from D3(a).
@@ valuation-scoring.md line 70 / strategy.md Upgrade 2 table (155-159): add the two linear rows for the 10–20% bands (D3(b)).
@@ quality-scoring.md line 15: append "Held names that previously cleared the gate keep an AMBER status (hold/trim, no adds) between 78.0 and 79.9; see P-009."
```

(All version-header bumps and `decisions/` entries are drafted in [06-roadmap.md](06-roadmap.md).)

## Glossary

From [framework/glossary.md](../../framework/glossary.md): **Composite Score**, **Quality Score**, **Valuation Score**, **Hard disqualifier**, **FCF yield**, **FCF/NI conversion ratio**, **SBC (Stock-Based Compensation)**, **Owner Earnings**, **PEG ratio**, **Forward PE**, **EPS**, **Diluted EPS**, **NTM / TTM**, **Net Debt/EBITDA**, **Interest coverage (ratio)**, **CAGR**, **Hurdle rate**, **Rule 9**, **Effective tax rate**, **Deferred tax valuation allowance release**, **Buyback yield (net buyback yield)**.

New terms (not yet in glossary.md — proposed definitions):
- **Kill-line** — a pre-written threshold checked when a company reports; crossing it forces a re-score or an exit review.
- **Three-state gate (PASS / AMBER / FAIL)** — PASS ≥ 80.0; AMBER = already held, 78.0–79.9 (keep, no adds); FAIL otherwise or with a hard disqualifier.
- **Cycle-peak candidate** — trailing EPS more than doubled year over year; the multiple may look cheap only because earnings are at a temporary high.
- **x2 arithmetic / buy-price curve** — 5-year projection of EPS × a future P/E; the buy-price curve is the price at which that projection gives a chosen yearly return.
- **Exit code 3 (not computable)** — the tool received input but the maths is undefined (e.g. negative EPS); it prints why and does not guess.
- **Provenance (`parsed` / `script`)** — a label saying whether a stored number was extracted from text or produced by a script.
- **Precheck** — a dry run listing all missing inputs at once.

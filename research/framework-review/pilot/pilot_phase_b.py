#!/usr/bin/env python3
"""Phase B pilot — sensitivity of the proposed scored changes on current holdings.

Plan: research/framework-review/07-phase-b-plan.md. READ-ONLY analysis: nothing in the
framework, scripts/scoring or any score file is changed by running this.

Method (sensitivity, not a full re-score): every full re-score needs manual inputs (moat
evidence, fair values, 10Y gate) that a batch run cannot produce. So each proposed change is
applied to ONLY the sub-score it touches, using live yfinance data for that sub-score's
inputs, and the difference is added to the score last recorded in portfolio/holdings.md:

    B1  SBC-adjusted FCF yield     dValuation = 0.40 * (FCF_Score(after SBC) - FCF_Score(reported))
    B2  SBC >= 100% of FCF         count of holdings that would be disqualified
    B3  Operating-margin Margins   dQuality   = 0.15 * (OpMargin_Score - GrossMargin_Score)
    B5  Hysteresis (2.0 buffer)    replay of Composite histories in watchlist/in-portfolio/
    B6  Advisory flags             cycle_peak (EPS history) / multiple_ceiling (proxy growth)
    B4  Capex / growth source      NOT piloted: needs qualitative per-company evidence

Limits (also stated in the report): live inputs are today's, the recorded scores are from
their own review dates; Upgrade-1 Owner-Earnings names (MSFT, GOOG, META, AMZN) are exempt
from B1 by design; B3's scale (EBIT margin 0-40% -> 0-100) and B5's buffer are placeholders.

Usage:  python research/framework-review/pilot/pilot_phase_b.py [--out results.json]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from scripts.fetch_fundamentals import fetch  # noqa: E402
from scripts.scoring import flags_common  # noqa: E402
from scripts.scoring.common import MissingInputError, clamp  # noqa: E402

OWNER_EARNINGS = {"MSFT", "GOOG", "META", "AMZN"}  # strategy.md Upgrade 1
YF_SYMBOL = {"TRN": "TRN.L"}
EDGES = [30.0, 50.0, 70.0, 80.0, 90.0]  # Composite action-band edges (strategy.md)
BUFFER = 2.0  # placeholder dead-band width (points)
OM_FULL = 40.0  # placeholder: EBIT margin that earns a full Margins score


def parse_holdings() -> dict:
    out = {}
    for line in (ROOT / "portfolio/holdings.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| \*{0,2}([A-Z]{2,5})\*{0,2}\s*\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|", line)
        if not m:
            continue
        t = m.group(1)
        num = lambda s: (re.match(r"\s*(-?\d+(?:\.\d+)?)", s) or [None, None])[1]
        v, q, c = num(m.group(3)), num(m.group(4)), num(m.group(5))
        if q is None:
            continue
        out[t] = {"valuation": float(v) if v else None, "quality": float(q), "composite": float(c) if c else None}
    return out


def band(c: float) -> int:
    return sum(c >= e for e in EDGES)


def hysteresis_state(series: list[float], buffer: float = BUFFER) -> list[int]:
    half = buffer / 2
    s = band(series[0])
    states = [s]
    for c in series[1:]:
        # move up only once past the edge by `half`; move down only once below it by `half`
        while s < len(EDGES) and c >= EDGES[s] + half:
            s += 1
        while s > 0 and c < EDGES[s - 1] - half:
            s -= 1
        states.append(s)
    return states


def history(ticker: str) -> list[tuple[str, float]]:
    d = ROOT / "watchlist/in-portfolio" / ticker
    files = sorted(d.glob(f"{ticker}-*.md")) if d.exists() else []
    if not files:
        return []
    rows = []
    for line in files[-1].read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5 and re.match(r"\d{4}-\d{2}-\d{2}$", cells[0]):
            m = re.match(r"\**(-?\d+(?:\.\d+)?)", cells[4])
            if m:
                rows.append((cells[0], float(m.group(1))))
    return sorted(set(rows))


def margin_inputs(t) -> dict:
    qf = t.quarterly_financials
    ebit = float(qf.loc["EBIT"].iloc[:4].sum())
    rev = float(qf.loc["Total Revenue"].iloc[:4].sum())
    return {"ebit_margin_pct": ebit / rev * 100}


def analyse(ticker: str, rec: dict) -> dict:
    import yfinance as yf

    r = {"ticker": ticker, "recorded": rec}
    try:
        t = yf.Ticker(YF_SYMBOL.get(ticker, ticker))
        f = fetch(t)
        mi = margin_inputs(t)
        info = t.info
    except Exception as exc:  # report, never guess
        r["error"] = f"{type(exc).__name__}: {exc}"
        return r

    adv = f["advisory"]
    fcf_y = f["fcf_yield_pct"]
    r["fcf_yield_pct"] = fcf_y

    # --- B1 / B2
    sbc = adv["sbc"]
    r["sbc"] = sbc
    if sbc:
        before = clamp(100 * (1 - fcf_y / 10))
        after = clamp(100 * (1 - sbc["fcf_yield_after_sbc_pct"] / 10))
        exempt = ticker in OWNER_EARNINGS
        dval = 0.0 if exempt else 0.40 * (after - before)
        r["b1"] = {"exempt_owner_earnings": exempt, "fcf_score_before": before, "fcf_score_after": after, "d_valuation": dval}
        if rec.get("valuation") is not None:
            nv = clamp(rec["valuation"] + dval)
            r["b1"]["new_valuation"] = nv
            if rec.get("composite") is not None and rec["quality"] >= 80:
                nc = 0.5 * (100 - rec["quality"]) + 0.5 * nv
                r["b1"]["new_composite"] = nc
                r["b1"]["band_change"] = band(nc) != band(rec["composite"])
        r["b2_disqualified"] = sbc["severity"] == "severe"

    # --- B3
    gm = f["gross_margin_pct"]
    cur = clamp(gm / 80 * 100)
    cand = clamp(mi["ebit_margin_pct"] / OM_FULL * 100)
    dq = 0.15 * (cand - cur)
    r["b3"] = {"gross_margin_pct": gm, "ebit_margin_pct": mi["ebit_margin_pct"], "score_gross": cur, "score_op": cand, "d_quality": dq}
    nq = clamp(rec["quality"] + dq)
    r["b3"]["new_quality"] = nq
    r["b3"]["gate_change"] = (rec["quality"] >= 80) != (nq >= 80)

    # --- B6 (advisory flags; growth is a PILOT PROXY = forwardEps / trailingEps - 1)
    r["cycle_peak"] = adv["cycle_peak"]["flag"]
    fe, te = info.get("forwardEps"), info.get("trailingEps")
    proxy = (fe / te - 1) * 100 if fe and te and te > 0 else None
    r["fwd_eps_growth_proxy_pct"] = proxy
    r["multiple_ceiling"] = flags_common.multiple_ceiling(f["forward_pe"], proxy)["flag"]
    r["forward_pe"] = f["forward_pe"]

    # --- B5 replay
    h = history(ticker)
    if len(h) >= 2:
        series = [c for _, c in h]
        base = [band(c) for c in series]
        hyst = hysteresis_state(series)
        flips = lambda s: sum(a != b for a, b in zip(s, s[1:]))
        r["b5"] = {"n": len(series), "series": h, "flips_baseline": flips(base), "flips_hysteresis": flips(hyst)}
    if rec.get("composite") is not None:
        c = rec["composite"]
        nearest = min(EDGES, key=lambda e: abs(c - e))
        r["edge_distance"] = {"composite": c, "nearest_edge": nearest, "distance": round(c - nearest, 2)}
    return r


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(Path(__file__).with_name("pilot-results-2026-10-12.json")))
    a = ap.parse_args()
    holdings = parse_holdings()
    results = []
    for ticker, rec in sorted(holdings.items()):
        print(f"... {ticker}", file=sys.stderr)
        results.append(analyse(ticker, rec))
        time.sleep(1)
    Path(a.out).write_text(json.dumps(results, indent=2, default=str), encoding="utf-8")
    print(f"wrote {a.out} ({len(results)} tickers)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

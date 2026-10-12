#!/usr/bin/env python3
"""Quality-side SBC pilot — FCF Quality computed on (FCF - SBC) / Net Income.

Read-only sensitivity analysis (see pilot_phase_b.py for the method). Applies ONE change:

    FCFQuality_Score = clamp(((FCF/NI - 0.40) / 0.60) * 100, 0, 100)      [quality-scoring.md]
    proposed:          FCF/NI  ->  (FCF - SBC)/NI

    dQuality = 0.10 * (FCFQuality_after - FCFQuality_before)             [10% weight]

and, for names that pass the 80.0 gate, combines it with the Valuation-side change (B1,
non-Owner-Earnings names only) to show the combined Composite effect and any band/gate change.
Also checks the existing FCF/NI hard disqualifier (< 70% for 2+ consecutive fiscal years)
re-run on the after-SBC ratio.

Independent of fetch_fundamentals (reads only FCF, Net Income and SBC), so coverage is
wider than the B1-B6 pilot. Missing data -> reported as a gap, never estimated.

Usage: python research/framework-review/pilot/pilot_quality_sbc.py [--out results.json]
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

from pilot_phase_b import OWNER_EARNINGS, YF_SYMBOL, band, parse_holdings  # noqa: E402
from scripts.scoring.common import clamp  # noqa: E402


def fcfq(ratio: float) -> float:
    return clamp((ratio - 0.40) / 0.60 * 100)


def ttm(df, row):
    if df is None or row not in df.index:
        return None
    s = df.loc[row].iloc[:4]
    return None if len(s) < 4 or s.isna().any() else float(s.sum())


def annual(t) -> list[dict]:
    """Fiscal years, oldest first, where FCF, SBC and Net Income are all available."""
    cf, fin = t.cashflow, t.financials
    out = []
    for col in cf.columns:
        try:
            fcf = cf.loc["Free Cash Flow", col]
            sbc = cf.loc["Stock Based Compensation", col]
            ni = fin.loc["Net Income", col]
        except KeyError:
            continue
        if any(x != x for x in (fcf, sbc, ni)) or ni <= 0:
            continue
        out.append({"year": str(col)[:10], "fcf_ni": float(fcf / ni), "adj_fcf_ni": float((fcf - sbc) / ni)})
    return sorted(out, key=lambda r: r["year"])


def analyse(ticker: str, rec: dict) -> dict:
    import yfinance as yf

    r = {"ticker": ticker, "recorded": rec}
    try:
        t = yf.Ticker(YF_SYMBOL.get(ticker, ticker))
        qf, qcf = t.quarterly_financials, t.quarterly_cashflow
        ni, fcf, sbc = ttm(qf, "Net Income"), ttm(qcf, "Free Cash Flow"), ttm(qcf, "Stock Based Compensation")
        mc = t.info.get("marketCap")
        info_fcf_y = fcf / mc * 100 if fcf is not None and mc else None
        ann = annual(t)
    except Exception as exc:
        r["error"] = f"{type(exc).__name__}: {exc}"
        return r
    if None in (ni, fcf, sbc):
        r["error"] = "missing TTM " + ", ".join(n for n, v in (("Net Income", ni), ("FCF", fcf), ("SBC", sbc)) if v is None)
        return r
    if ni <= 0:
        r["error"] = "TTM net income <= 0 (FCF/NI undefined)"
        return r

    before, after = fcf / ni, (fcf - sbc) / ni
    qb, qa = fcfq(before), fcfq(after)
    dq = 0.10 * (qa - qb)
    r.update(
        fcf_ni=before, adj_fcf_ni=after, fcfq_before=qb, fcfq_after=qa, d_quality=dq,
        new_quality=clamp(rec["quality"] + dq), annual=ann,
        gate_change=(rec["quality"] >= 80) != (clamp(rec["quality"] + dq) >= 80),
    )
    # existing hard disqualifier re-run on the after-SBC ratio: < 70% in each of the last 2 FYs
    last2 = ann[-2:]
    r["disq_now"] = len(last2) == 2 and all(y["fcf_ni"] < 0.70 for y in last2)
    r["disq_after_sbc"] = len(last2) == 2 and all(y["adj_fcf_ni"] < 0.70 for y in last2)

    # combined with the Valuation-side change (non-Owner-Earnings only), gate passers only
    if info_fcf_y is not None:
        y_after = (fcf - sbc) / mc * 100
        dval = 0.0 if ticker in OWNER_EARNINGS else 0.40 * (clamp(100 * (1 - y_after / 10)) - clamp(100 * (1 - info_fcf_y / 10)))
        r["d_valuation"] = dval
        if rec["valuation"] is not None and rec["composite"] is not None:
            nq, nv = r["new_quality"], clamp(rec["valuation"] + dval)
            if rec["quality"] >= 80 and nq >= 80:
                nc = 0.5 * (100 - nq) + 0.5 * nv
                r["combined"] = {"new_quality": nq, "new_valuation": nv, "new_composite": nc, "band_change": band(nc) != band(rec["composite"])}
    return r


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(HERE / "pilot-quality-sbc-2026-10-12.json"))
    a = ap.parse_args()
    results = []
    for ticker, rec in sorted(parse_holdings().items()):
        print(f"... {ticker}", file=sys.stderr)
        results.append(analyse(ticker, rec))
        time.sleep(1)
    Path(a.out).write_text(json.dumps(results, indent=2, default=str), encoding="utf-8")
    print(f"wrote {a.out} ({len(results)} tickers)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

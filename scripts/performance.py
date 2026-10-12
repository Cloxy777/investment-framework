#!/usr/bin/env python3
"""Framework-account performance statistics (time-weighted return) with the transferred-out
positions removed "as if they never existed".

Background (see portfolio/accounts.md and portfolio/performance/README.md): RGL, LM8 and TLT
were moved in-kind out of U19421206 on 2026-10-12. IBKR PortfolioAnalyst's TWR already treats
that transfer as a withdrawal, but it still contains those positions' performance *before* the
transfer. This script rebuilds the account's history without them.

Method (daily, flow-adjusted):
    E_t   market value of the excluded positions (ledger quantities x frozen close prices x FX)
    F_t   framework value = NAV_t - E_t - cumulative excluded income
    flow  PA's implied external flow  f_t = NAV_t - NAV_{t-1} * (1 + r_PA_t)
    x_t   capital that moved between the framework sleeve and the excluded sleeve:
              buy  : +cost incl. commission   (cash left the framework sleeve)
              sell : -proceeds net of commission
              transfer_out : -market value    (already inside f_t, so it must not hit F)
    r_t   = (F_t - (f_t - x_t)) / F_{t-1} - 1          (flows assumed end-of-day, like PA)
Windows chain r_t geometrically.

Inputs (all under portfolio/performance/):
    nav-history.csv       date,nav,pa_return,pa_flow   - raw PortfolioAnalyst daily series
    excluded-ledger.csv   quantity ledger of the excluded positions
    excluded-prices.csv   frozen daily closes for TLT / RGL / LM8 / AUDUSD (history only)
    excluded-income.csv   dividends etc. received on excluded positions (USD) - optional

IBKR PortfolioAnalyst data is MCP-only (see scripts/TOKEN-OPTIMIZATION-PLAN.md finding #1), so
Claude fetches `get_pa_performance_all_periods`, writes the period object it needs to a JSON
file, and `ingest` merges it.

Usage (the token-cheap path is `status` -> one MCP call only if stale -> `run`):
    python -m scripts.performance status [--today YYYY-MM-DD]        # fresh? which PA period to fetch?
    python -m scripts.performance run [--inline "START@NAV D:NAV:CPS ..."] [--months 2 5] [--years 1 2]
    python -m scripts.performance ingest (--inline "..." | FILE.json [--period 1Y])
    python -m scripts.performance report [--as-of YYYY-MM-DD] [--months ..] [--years ..] [--out FILE]
"""

import argparse
import csv
import datetime as dt
import json
import math
import sys
from pathlib import Path

PERF_DIR = Path(__file__).resolve().parent.parent / "portfolio" / "performance"
NAV_FILE = "nav-history.csv"
LEDGER_FILE = "excluded-ledger.csv"
PRICES_FILE = "excluded-prices.csv"
INCOME_FILE = "excluded-income.csv"

PRICE_COL = {"TLT": ("tlt_usd", "USD"), "RGL": ("rgl_aud", "AUD"), "LM8": ("lm8_aud", "AUD")}


def _d(s):
    return dt.date.fromisoformat(s)


def _read(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


# ---------------------------------------------------------------- loading

def load_nav(path):
    return [
        {"date": _d(r["date"]), "nav": float(r["nav"]), "ret": float(r["pa_return"]), "flow": float(r["pa_flow"])}
        for r in _read(path)
    ]


def load_ledger(path):
    rows = []
    for r in _read(path):
        rows.append({
            "date": _d(r["date"]), "ticker": r["ticker"], "action": r["action"],
            "qty": float(r["qty"]), "price": float(r["price"]) if r["price"] else None,
            "ccy": r["ccy"], "commission": float(r["commission"] or 0),
        })
    return rows


def load_prices(path):
    return {
        _d(r["date"]): {"TLT": float(r["tlt_usd"]), "RGL": float(r["rgl_aud"]),
                        "LM8": float(r["lm8_aud"]), "AUD": float(r["audusd"])}
        for r in _read(path)
    }


def load_income(path):
    p = Path(path)
    if not p.exists():
        return []
    return [{"date": _d(r["date"]), "usd": float(r["usd"])} for r in _read(p)]


# ---------------------------------------------------------------- core maths

def _price_on(prices, d):
    """Frozen close on or before `d` (forward fill)."""
    ks = [k for k in prices if k <= d]
    if not ks:
        raise ValueError(f"no excluded-position price on or before {d}")
    return prices[max(ks)]


def _usd(ticker, local_amount, px):
    return local_amount * (px["AUD"] if PRICE_COL[ticker][1] == "AUD" else 1.0)


def excluded_series(nav_rows, ledger, prices, income=()):
    """Per NAV row: (E_t, x_t, cumulative_income_t). Hard-fails if the ledger is inconsistent."""
    dates = [r["date"] for r in nav_rows]
    qty = {t: 0.0 for t in PRICE_COL}
    out = []
    pending = sorted(ledger, key=lambda r: r["date"])
    inc = sorted(income, key=lambda r: r["date"])
    cum_inc, prev = 0.0, None
    for d in dates:
        try:
            px = _price_on(prices, d)
        except ValueError:
            px = None  # before the first frozen price (the anchor row) - nothing is held yet
        x = 0.0
        # ledger rows whose effective date falls in (prev, d]
        due = [r for r in pending if (prev is None or r["date"] > prev) and r["date"] <= d]
        for r in due:
            t = r["ticker"]
            if t not in PRICE_COL:
                raise ValueError(f"unknown excluded ticker {t!r}")
            if r["action"] == "open":
                qty[t] += r["qty"]
            elif r["action"] == "buy":
                x += _usd(t, r["qty"] * r["price"] + r["commission"], px)
                qty[t] += r["qty"]
            elif r["action"] == "sell":
                x -= _usd(t, r["qty"] * r["price"] - r["commission"], px)
                qty[t] -= r["qty"]
            elif r["action"] == "transfer_out":
                if abs(qty[t] - r["qty"]) > 1e-6:
                    raise ValueError(
                        f"{t}: ledger holds {qty[t]:g} on {d} but transfer_out is {r['qty']:g} - ledger inconsistent")
                x -= _usd(t, qty[t] * px[t], px)
                qty[t] = 0.0
            else:
                raise ValueError(f"unknown ledger action {r['action']!r}")
            if qty[t] < -1e-6:
                raise ValueError(f"{t}: negative quantity after {r}")
        cum_inc += sum(i["usd"] for i in inc if (prev is None or i["date"] > prev) and i["date"] <= d)
        e = sum(_usd(t, qty[t] * px[t], px) for t in PRICE_COL if qty[t]) if px else 0.0
        out.append((e, x, cum_inc))
        prev = d
    return out


def framework_daily(nav_rows, ledger, prices, income=()):
    """Daily framework-only rows. The first row (base date) carries no return."""
    ex = excluded_series(nav_rows, ledger, prices, income)
    opens = [r["date"] for r in ledger if r["action"] == "open"]
    base = min(opens) if opens else None
    rows, prev_f = [], None
    for r, (e, x, ci) in zip(nav_rows, ex):
        if base is None:
            base = r["date"]
        if r["date"] < base:
            continue
        f = r["nav"] - e - ci
        flow_f = r["flow"] - x
        ret = None if prev_f is None else (f - flow_f) / prev_f - 1
        rows.append({"date": r["date"], "nav": r["nav"], "excluded": e, "framework": f,
                     "pa_flow": r["flow"], "x": x, "ret": ret, "pa_ret": None if prev_f is None else r["ret"]})
        prev_f = f
    return rows


def chain(returns):
    p = 1.0
    for r in returns:
        p *= 1 + r
    return p - 1


def _sub_months(d, n):
    y, m = divmod(d.year * 12 + d.month - 1 - n, 12)
    m += 1
    last = [31, 29 if y % 4 == 0 and (y % 100 or y % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1]
    return dt.date(y, m, min(d.day, last))


def _baseline(rows, target):
    """Last row date on or before `target` (the close the window starts from)."""
    ks = [r["date"] for r in rows if r["date"] <= target]
    return max(ks) if ks else None


def window_stats(rows, start_target, as_of, clamp_days=7):
    """Stats for returns dated in (baseline, as_of]. None if history is too short."""
    base_date = rows[0]["date"]
    clamped = False
    baseline = _baseline(rows, start_target)
    if baseline is None:
        if (base_date - start_target).days > clamp_days:
            return None
        baseline, clamped = base_date, True
    sel = [r for r in rows if baseline < r["date"] <= as_of]
    if not sel:
        return None
    fw = [r["ret"] for r in sel]
    pa = [r["pa_ret"] for r in sel]
    curve, peak, mdd = 1.0, 1.0, 0.0
    for r in fw:
        curve *= 1 + r
        peak = max(peak, curve)
        mdd = min(mdd, curve / peak - 1)
    days = (sel[-1]["date"] - baseline).days
    total = chain(fw)
    ann = (1 + total) ** (365 / days) - 1 if days >= 360 else None
    vol = None
    if len(fw) >= 20:
        mean = sum(fw) / len(fw)
        vol = math.sqrt(sum((x - mean) ** 2 for x in fw) / (len(fw) - 1)) * math.sqrt(252)
    return {"from": baseline, "to": sel[-1]["date"], "framework": total, "reported": chain(pa),
            "annualized": ann, "max_drawdown": mdd, "vol": vol, "days": days, "clamped": clamped}


def standard_windows(as_of, months=(), years=()):
    wins = [("1D", as_of - dt.timedelta(days=1)), ("1W", as_of - dt.timedelta(days=7)),
            ("MTD", as_of.replace(day=1) - dt.timedelta(days=1)),
            ("1M", _sub_months(as_of, 1)), ("3M", _sub_months(as_of, 3)), ("6M", _sub_months(as_of, 6)),
            ("YTD", dt.date(as_of.year - 1, 12, 31)), ("1Y", _sub_months(as_of, 12))]
    wins += [(f"{n}M", _sub_months(as_of, n)) for n in months if n not in (1, 3, 6, 12)]
    wins += [(f"{n}Y", _sub_months(as_of, 12 * n)) for n in years if n != 1]
    return wins


def _pct(x, nd=2):
    return "n/a" if x is None else f"{x * 100:+.{nd}f}%"


def build_report(rows, as_of, months=(), years=()):
    last = max(r["date"] for r in rows if r["date"] <= as_of)
    lines = [
        f"# Framework-account performance - as of {last}",
        "",
        "Time-weighted return (TWR) of **U19421206 with RGL / LM8 / TLT removed from the whole history** "
        "(\"Framework\"), next to IBKR PortfolioAnalyst's own TWR (\"Reported\", which only neutralises the "
        "transfer day). Method: [portfolio/performance/README.md](README.md).",
        "",
        "| Window | From (close) | To | Framework TWR | Reported TWR | Framework - Reported | Annualised | Max drawdown | Volatility (ann.) |",
        "|--------|--------------|----|--------------:|-------------:|---------------------:|-----------:|-------------:|------------------:|",
    ]
    wins = standard_windows(last, months, years) + [("Since start", rows[0]["date"] - dt.timedelta(days=1))]
    for label, target in wins:
        s = window_stats(rows, target, last)
        if s is None:
            lines.append(f"| {label} | - | - | n/a (history starts {rows[0]['date']}) | n/a | n/a | n/a | n/a | n/a |")
            continue
        note = " *" if s["clamped"] else ""
        diff = None if s["reported"] is None else s["framework"] - s["reported"]
        vol = "n/a" if s["vol"] is None else "%.1f%%" % (s["vol"] * 100)
        lines.append(
            f"| {label}{note} | {s['from']} | {s['to']} | **{_pct(s['framework'])}** | {_pct(s['reported'])} | "
            f"{_pct(diff)} | {_pct(s['annualized'])} | {_pct(s['max_drawdown'])} | "
            f"{vol} |")
    lines += [
        "",
        f"`*` window starts at the first history date ({rows[0]['date']}), not the nominal calendar date.",
        "",
        "Annualised is shown only for windows of ~1 year or more; volatility only for windows of 20+ trading days. "
        "Past returns are descriptive statistics, not a forecast or advice.",
    ]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- ingest

def ingest_pa(obj, nav_rows, period="1Y"):
    """Merge a PortfolioAnalyst period object into nav_rows (in place). Returns (added, updated)."""
    if "accounts" in obj:
        obj = obj["accounts"]["account"]["periods"][period]
    start = dt.datetime.strptime(obj["start_date"], "%Y%m%d").date()
    by_date = {r["date"]: r for r in nav_rows}
    if nav_rows and start > max(by_date):
        raise ValueError(f"gap: stored history ends {max(by_date)} but the series starts {start}; "
                         "ingest a longer period (1M / YTD / 1Y)")
    prev_nav, prev_c = obj["start_nav"], 0.0
    added = updated = 0
    for ds, nav, c in zip(obj["dates"], obj["nav"], obj["cps"]):
        d = dt.datetime.strptime(ds, "%Y%m%d").date()
        ret = (1 + c) / (1 + prev_c) - 1
        flow = nav - prev_nav * (1 + ret)
        new = {"date": d, "nav": round(nav, 2), "ret": round(ret, 8), "flow": round(flow, 2)}
        if d in by_date:
            old = by_date[d]
            if abs(old["nav"] - new["nav"]) > 0.01 or abs(old["ret"] - new["ret"]) > 1e-8:
                old.update(new)
                updated += 1
        else:
            nav_rows.append(new)
            by_date[d] = new
            added += 1
        prev_nav, prev_c = nav, c
    nav_rows.sort(key=lambda r: r["date"])
    return added, updated


def save_nav(path, nav_rows):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        fh.write("date,nav,pa_return,pa_flow\n")
        for r in nav_rows:
            fh.write(f"{r['date']},{r['nav']:.2f},{r['ret']:.8f},{r['flow']:.2f}\n")


# ---------------------------------------------------------------- CLI


# ---------------------------------------------------------------- status / inline ingest / glossary

GLOSSARY_TERMS = ["TWR (time-weighted return)", "Max drawdown", "NLV (Net Liquidation Value)",
                  "Excluded sleeve", "In-kind (free-of-payment) transfer", "Framework account"]


def latest_weekday(today):
    d = today
    while d.weekday() >= 5:
        d -= dt.timedelta(days=1)
    return d


def status(nav_rows, today):
    """Is the stored history current, and which (cheapest sufficient) PA period must be fetched?

    A PA period fits when its start_date is on or before the last stored date (otherwise ingest
    refuses a gap). 7D/MTD/1M/YTD/1Y are tried smallest-first."""
    last = max(r["date"] for r in nav_rows)
    target = latest_weekday(today)
    gap = (target - last).days
    if gap <= 0:
        return {"last": last, "target": target, "stale": False, "period": None}
    starts = [("7D", target - dt.timedelta(days=7)),
              ("MTD", target.replace(day=1) - dt.timedelta(days=1)),
              ("1M", _sub_months(target, 1)),
              ("YTD", dt.date(target.year - 1, 12, 31)),
              ("1Y", _sub_months(target, 12))]
    period = next((name for name, st in starts if st <= last), "1Y")
    return {"last": last, "target": target, "stale": True, "period": period, "gap_days": gap}


def parse_inline(text):
    """`START_YYYYMMDD@START_NAV YYYYMMDD:NAV:CPS ...` -> a PA period object (same shape ingest_pa takes)."""
    toks = text.split()
    if not toks or "@" not in toks[0]:
        raise ValueError("inline format: 'START_YYYYMMDD@START_NAV YYYYMMDD:NAV:CPS ...'")
    start, start_nav = toks[0].split("@")
    dates, navs, cps = [], [], []
    for t in toks[1:]:
        d, n, c = t.split(":")
        dates.append(d)
        navs.append(float(n))
        cps.append(float(c))
    if not dates:
        raise ValueError("inline series has no data points")
    return {"start_date": start, "start_nav": float(start_nav), "dates": dates, "nav": navs, "cps": cps}


def glossary_block(path=Path("framework/glossary.md")):
    from scripts.glossary_lookup import lookup
    lines = ["", "## Glossary", ""]
    for r in lookup(GLOSSARY_TERMS, path):
        lines.append(f"- **{r['term']}**: {r['definition'].replace('](../', '](../../')}" if r["found"]
                     else f"- NOT FOUND: {r['term']} - add it to framework/glossary.md")
    return "\n".join(lines) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(sp, report=False, ingest=False):
        sp.add_argument("--dir", type=Path, default=PERF_DIR)
        if ingest:
            sp.add_argument("--inline", help="'START@NAV D:NAV:CPS ...' (see module doc)")
        if report:
            sp.add_argument("--as-of", type=_d)
            sp.add_argument("--months", type=int, nargs="*", default=[])
            sp.add_argument("--years", type=int, nargs="*", default=[])
            sp.add_argument("--out", type=Path)

    common(sub.add_parser("status"))
    sub.choices["status"].add_argument("--today", type=_d, default=dt.date.today())
    common(sub.add_parser("report"), report=True)
    rn = sub.add_parser("run")
    common(rn, report=True, ingest=True)
    ip = sub.add_parser("ingest")
    common(ip, ingest=True)
    ip.add_argument("file", type=Path, nargs="?")
    ip.add_argument("--period", default="1Y")
    a = ap.parse_args(argv)

    nav = load_nav(a.dir / NAV_FILE)
    if a.cmd == "status":
        st = status(nav, a.today)
        if not st["stale"]:
            print(f"FRESH: history ends {st['last']} (latest weekday {st['target']}). No IBKR call needed - run `run`.")
        else:
            print(f"STALE by {st['gap_days']}d: history ends {st['last']}, latest weekday {st['target']}. "
                  f"Call get_pa_performance_all_periods and take period {st['period']} (smallest that bridges the gap), then "
                  f"`run --inline \"<START>@<start_nav> <DATE>:<nav>:<cps> ...\"`.")
        return 0

    if a.cmd in ("ingest", "run") and (a.inline or getattr(a, "file", None)):
        if a.inline:
            obj, period = parse_inline(a.inline), "1Y"
        else:
            obj, period = json.loads(a.file.read_text(encoding="utf-8")), a.period
        added, updated = ingest_pa(obj, nav, period)
        save_nav(a.dir / NAV_FILE, nav)
        print(f"ingested: {added} new day(s), {updated} revised; history now {nav[0]['date']} .. {nav[-1]['date']}")
        if a.cmd == "ingest":
            return 0
    elif a.cmd == "ingest":
        ap.error("ingest needs --inline or a FILE")

    rows = framework_daily(nav, load_ledger(a.dir / LEDGER_FILE), load_prices(a.dir / PRICES_FILE),
                           load_income(a.dir / INCOME_FILE))
    text = build_report(rows, a.as_of or rows[-1]["date"], a.months, a.years)
    if a.cmd == "run":
        text += glossary_block()
    if a.out or a.cmd == "run":
        (a.out or a.dir / "latest.md").write_text(text, encoding="utf-8")
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())

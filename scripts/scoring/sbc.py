#!/usr/bin/env python3
"""SBC disclosure block — Phase A of the SBC treatment (no score effect).

Stock-based compensation (SBC) is a real cost to owners (dilution) but is added back in
reported free cash flow. This module only *discloses* it beside the reported FCF yield so the
analyst sees the gap; it never changes the Valuation or Quality score. Scoring the
SBC-adjusted yield is a separate, later methodology change (see
decisions/2026-10-12-framework-change-advisory-flags-and-sbc-disclosure.md).

Usage:
    python -m scripts.scoring.sbc --sbc 640 --fcf 1980 --market-cap 45000
    python -m scripts.scoring.sbc --input fundamentals.json   # keys: sbc_ttm, fcf_ttm, market_cap

All three quantities must be TTM figures in the same currency and units. Missing input ->
MissingInputError (exit 2); never defaulted or estimated.

Thresholds are PLACEHOLDERS (marked †) — taken from an external reference system's printed
constants, not yet calibrated on this repo's holdings:
    † SBC/FCF >= 30%  -> "elevated"
    † SBC/FCF >= 100% (or FCF <= 0 with SBC > 0) -> "severe"
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from scripts.scoring.common import MissingInputError, require

SBC_ELEVATED_PCT_OF_FCF = 30.0  # †
SBC_SEVERE_PCT_OF_FCF = 100.0  # †


def sbc_metrics(sbc_ttm: float, fcf_ttm: float, market_cap: float) -> dict:
    """Return SBC/FCF, reported and after-SBC FCF yield, and a severity label.

    sbc_pct_fcf is None when FCF <= 0 (ratio undefined); severity is then "severe" if SBC > 0.
    """
    if sbc_ttm is None or fcf_ttm is None or market_cap is None:
        raise MissingInputError("sbc_metrics needs sbc_ttm, fcf_ttm and market_cap (all non-None)")
    if market_cap <= 0:
        raise MissingInputError("market_cap must be > 0")
    if sbc_ttm < 0:
        raise MissingInputError("sbc_ttm must be >= 0 (pass the cost as a positive number)")

    sbc_pct_fcf = sbc_ttm / fcf_ttm * 100 if fcf_ttm > 0 else None
    reported = fcf_ttm / market_cap * 100
    after = (fcf_ttm - sbc_ttm) / market_cap * 100

    if fcf_ttm <= 0:
        severity = "severe" if sbc_ttm > 0 else "none"
    elif sbc_pct_fcf >= SBC_SEVERE_PCT_OF_FCF:
        severity = "severe"
    elif sbc_pct_fcf >= SBC_ELEVATED_PCT_OF_FCF:
        severity = "elevated"
    else:
        severity = "none"

    return {
        "sbc_ttm": sbc_ttm,
        "fcf_ttm": fcf_ttm,
        "market_cap": market_cap,
        "sbc_pct_fcf": sbc_pct_fcf,
        "fcf_yield_reported_pct": reported,
        "fcf_yield_after_sbc_pct": after,
        "severity": severity,
    }


def render(m: dict) -> str:
    ratio = f"{m['sbc_pct_fcf']:.1f}%" if m["sbc_pct_fcf"] is not None else "n/a — FCF <= 0"
    note = {
        "none": "",
        "elevated": f"  -> at/above the {SBC_ELEVATED_PCT_OF_FCF:.0f}% † watch line",
        "severe": "  -> SEVERE: SBC consumes all (or more than all) of FCF †",
    }[m["severity"]]
    return "\n".join(
        [
            "SBC block (TTM, advisory — no score effect)",
            f"  SBC {m['sbc_ttm']:,.1f}   FCF {m['fcf_ttm']:,.1f}   Market cap {m['market_cap']:,.1f}",
            f"  SBC/FCF = {ratio}{note}",
            f"  FCF yield (reported)  = {m['fcf_yield_reported_pct']:.2f}%",
            f"  FCF yield after SBC   = {m['fcf_yield_after_sbc_pct']:.2f}%",
        ]
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", help="JSON file with sbc_ttm, fcf_ttm, market_cap")
    parser.add_argument("--sbc", type=float)
    parser.add_argument("--fcf", type=float)
    parser.add_argument("--market-cap", type=float)
    args = parser.parse_args(argv)

    try:
        if args.input:
            data = json.loads(Path(args.input).read_text())
            sbc = require(data, "sbc_ttm")
            fcf = require(data, "fcf_ttm")
            mc = require(data, "market_cap")
        else:
            sbc, fcf, mc = args.sbc, args.fcf, args.market_cap
        print(render(sbc_metrics(sbc, fcf, mc)))
    except MissingInputError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

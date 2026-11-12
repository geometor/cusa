"""Standalone Rational Trigonometry demonstration of *De Docta Ignorantia* I.14–15.

Models flattening isosceles triangles ``T_n`` with fixed base ``B = (-1, 0)``, ``C = (1, 0)``
and apex ``A_n = (0, 1/n)``, verifying exact rational spreads, Wildberger's Triple Spread
Formula, and the vanishing Triple Quad Formula collinearity residual ``16 / n^2 -> 0``.
"""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT / "src"))

import sympy as sp  # noqa: E402

from geometor.cusa.coincidentia_triangle_line import (  # noqa: E402
    compute_flattening_triangle_metrics,
    construct_flattening_triangles,
    verify_triangle_line_coincidence,
)


def run_demo() -> None:
    """Execute and print the complete *De Docta Ignorantia* I.14–15 symbolic demonstration."""
    print("=" * 78)
    print("GEOMETOR • cusa — De Docta Ignorantia I.14: Infinite Triangle as Straight Line")
    print("=" * 78)

    rows = [compute_flattening_triangle_metrics(n) for n in (1, 2, 4, 8, 16, 64)]
    print("\n1. Rational Trigonometry Invariants of Flattening Triangles T_n:")
    print(
        f"   {'n':>3} | {'Q(A_n, B)':<10} | {'Apex Spread s_A':<16} | "
        f"{'Base Spread s_B':<15} | {'TQF Residual':<12}"
    )
    print("   " + "-" * 68)
    for r in rows:
        print(
            f"   {r.step_n:>3} | {str(r.q_leg):<10} | {str(r.spread_apex):<16} | "
            f"{str(r.spread_base):<15} | {str(r.triple_quad_residual):<12}"
        )

    proof = verify_triangle_line_coincidence()
    print("\n2. Exact Symbolic Proof over Q(n):")
    print(f"   Apex spread s_A(n)            : {proof['spread_apex']} -> {proof['limit_spread_apex']}")
    print(f"   Base spread s_B(n)            : {proof['spread_base']}")
    print(f"   Triple Spread Formula == 0    : {proof['triple_spread_identity']}")
    print(
        f"   Triple Quad residual 16*Area^2: {proof['triple_quad_residual']} -> "
        f"{proof['limit_triple_quad']}"
    )
    print(
        f"   Rationalized side excess      : {proof['side_excess_rationalized']} -> "
        f"{proof['limit_side_excess']}"
    )

    model = construct_flattening_triangles()
    floats = [pt for pt in model.points if pt.has(sp.Float)]
    assert not floats, f"Float contamination: {floats}"
    print(
        f"\n3. Exactness Gate: {len(model.points)} constructed points verified "
        "100% rational over Q (zero sp.Float)."
    )


if __name__ == "__main__":
    run_demo()

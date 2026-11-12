"""Standalone symbolic demonstration of *De Docta Ignorantia* I.13 (Circle & Straight Line).

Constructs the tangent circle pencil ``C_R`` above straight horizon ``AB``, prints the
exact radical sagitta table at ``x = 1``, proves the scaling limit ``lim R * h(x, R) = x^2 / 2``,
and verifies conformal Möbius inversion mapping ``C_R`` onto rational circles converging
to ``C'_inf`` = inverted line ``AB``.
"""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT / "src"))

import sympy as sp  # noqa: E402

from geometor.cusa.coincidentia_circle_line import (  # noqa: E402
    compute_tangent_pencil_table,
    construct_circle_line_inversion,
    construct_tangent_circle_pencil,
    verify_mobius_inversion_coincidence,
    verify_sagitta_and_curvature_limits,
)


def run_demo() -> None:
    """Execute and print the complete *De Docta Ignorantia* I.13 symbolic demonstration."""
    print("=" * 78)
    print("GEOMETOR • cusa — De Docta Ignorantia I.13: Coincidence of Circle & Line")
    print("=" * 78)

    table = compute_tangent_pencil_table((1, 2, 4, 8, 16, 64))
    print("\n1. Tangent Circle Pencil C_R at Origin O = (0, 0) Along Secant x = 1:")
    print(f"   {'R':>4} | {'Exact Sagitta h(1, R)':<24} | {'Decimal':>12} | {'Curvature 1/R':>14}")
    print("   " + "-" * 64)
    for row in table:
        dec = float(row.secant_ordinate.evalf())
        print(
            f"   {str(row.radius):>4} | {str(row.secant_ordinate):<24} | "
            f"{dec:12.8f} | {str(row.curvature):>14}"
        )

    limits = verify_sagitta_and_curvature_limits()
    print("\n2. Symbolic Asymptotics as R -> oo:")
    print(f"   Rationalized sagitta  : h(x, R) = {limits['sagitta_rationalized']}")
    print(f"   Identity verified     : {limits['identity_holds']}")
    print(f"   lim_{{R->oo}} h(x, R)   : {limits['sagitta_limit']}")
    print(f"   lim_{{R->oo}} R*h(x, R) : {limits['scaled_sagitta_limit']}")
    print(f"   lim_{{R->oo}} kappa(R)  : {limits['curvature_limit']}")

    inv = verify_mobius_inversion_coincidence((1, 2, 4, 8, 16))
    print("\n3. Conformal Möbius Inversion in Unit Circle at Pole S = (0, -1):")
    print(f"   Inverted center M_R   : (0, {inv['pole_inverted_center_y']})")
    print(f"   Inverted radius rho_R : {inv['pole_inverted_radius']}")
    print(
        f"   Limit R -> oo         : center (0, {inv['limit_center_y']}), "
        f"radius {inv['limit_radius']} (== inverted straight line y = 0)"
    )

    m_pencil = construct_tangent_circle_pencil()
    m_inv = construct_circle_line_inversion()
    for name, mdl in (("tangent_pencil", m_pencil), ("mobius_inversion", m_inv)):
        floats = [pt for pt in mdl.points if pt.has(sp.Float)]
        assert not floats, f"Float contamination in {name}: {floats}"
    print(
        f"\n4. Exactness Gate: {len(m_pencil.points)} pencil points + {len(m_inv.points)} "
        "inversion points verified 100% free of sp.Float."
    )


if __name__ == "__main__":
    run_demo()

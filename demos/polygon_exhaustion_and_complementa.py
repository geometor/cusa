"""Standalone symbolic demonstration of Polygon Exhaustion (I.3) & Scripta Mathematica (1445–1459).

Verifies:
1. Inscribed regular n-gon exhaustion (n = 3, 4, 6, 8, 12) in nested quadratic radicals,
2. Cusa's 1445 *sesquiquarta* (5 : 4) equilateral-triangle rectification yielding
   ``pi_Cusa = 24 * sqrt(21) / 35 ~= 3.14233762``,
3. Cusa's 1458–1459 *Aurea Propositio* three-ray conservation ``|AI| + |AK| + |AL| = 3``
   and fifth-order Maclaurin error ``theta^5 / 180 + O(theta^7)``.
"""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT / "src"))

import sympy as sp  # noqa: E402

from geometor.cusa.polygon_exhaustion_and_complementa import (  # noqa: E402
    compute_polygon_exhaustion_table,
    construct_aurea_propositio,
    construct_polygon_exhaustion,
    construct_transmutatio_isoperimetra,
    verify_cusa_snellius_approximation,
    verify_transmutatio_1445,
)


def run_demo() -> None:
    """Execute and print the polygon exhaustion and *Scripta Mathematica* demonstrations."""
    print("=" * 80)
    print("GEOMETOR • cusa — Polygon Exhaustion (I.3) & Scripta Mathematica (1445–1459)")
    print("=" * 80)

    poly_rows = compute_polygon_exhaustion_table()
    print("\n1. Inscribed & Circumscribed Regular Polygon Exhaustion (DI I.3 & DMC 1453):")
    print(f"   {'n':>3} | {'Prima Linea r_n = cos(pi/n)':<28} | {'Inscribed P_n/2':>15} | {'Circum. Q_n/2':>14}")
    print("   " + "-" * 68)
    for row in poly_rows:
        p_in = float(row.inscribed_semiperimeter.evalf())
        p_out = float(row.circumscribed_semiperimeter.evalf())
        print(
            f"   {row.sides:>3} | {str(row.prima_linea_inradius):<28} | "
            f"{p_in:15.8f} | {p_out:14.8f}"
        )

    tr1445 = verify_transmutatio_1445()
    print("\n2. De Geometricis Transmutationibus (1445, §§9–11) — Sesquiquartal 5:4 Law:")
    print(f"   Quarter-side ray |AE| : {tr1445['ae_length']}")
    print(f"   Isoperimetric |AH|    : {tr1445['ah_radius']}")
    print(
        f"   Implied pi_Cusa,1445  : {tr1445['pi_cusa_1445']} "
        f"(~= {float(tr1445['pi_cusa_1445'].evalf()):.8f}, error {tr1445['abs_error']:+.6e})"
    )

    au1459 = verify_cusa_snellius_approximation()
    print("\n3. De Mathematica Perfectione (1458) & Aurea Propositio (1459):")
    print(f"   Cusa–Snellius formula : L/2 = {au1459['cusa_approx']}")
    print(f"   Three-ray invariance  : {au1459['tangent_ratio_equal']}")
    print(
        f"   Maclaurin residual    : theta^5 * ({au1459['coeff_theta_5']}) + "
        f"theta^7 * ({au1459['coeff_theta_7']}) + theta^9 * ({au1459['coeff_theta_9']}) + O(theta^11)"
    )
    print(
        f"   Implied pi at pi/6    : {au1459['pi_at_pi_over_6']} "
        f"(~= {float(au1459['pi_at_pi_over_6'].evalf()):.8f})"
    )
    print(
        f"   Implied pi at pi/12   : {au1459['pi_at_pi_over_12']} "
        f"(~= {float(au1459['pi_at_pi_over_12'].evalf()):.10f})"
    )

    for name, builder in (
        ("polygon_exhaustion", construct_polygon_exhaustion),
        ("transmutatio_1445", construct_transmutatio_isoperimetra),
        ("aurea_propositio_1459", construct_aurea_propositio),
    ):
        mdl = builder()
        floats = [pt for pt in mdl.points if pt.has(sp.Float)]
        assert not floats, f"Float contamination in {name}: {floats}"
    print("\n4. Exactness Gate: All 3 constructive models verified 100% free of sp.Float.")


if __name__ == "__main__":
    run_demo()

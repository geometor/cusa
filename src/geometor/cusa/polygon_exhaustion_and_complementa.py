r"""Exact symbolic constructions for Polygon Exhaustion (I.3) and Cusa's *Scripta Mathematica* (1445–1459).

Unites Nicholas of Cusa's epistemological paradigm of polygon-in-circle incommensurability
(*De docta ignorantia* I.3) with his constructive mathematical treatises:

1. :func:`construct_polygon_exhaustion` & :func:`compute_polygon_exhaustion_table`
   (*De docta ignorantia* I.3 & *De mathematicis complementis* 1453): Exact inscribed and
   circumscribed regular :math:`n`-gons (:math:`n \in \{3, 4, 6, 8, 12\}`) in closed-form
   radicals, tracking Cusa's *prima linea* (inradius :math:`r_n = \cos(\pi/n)`),
   *secunda linea* (circumradius :math:`R_n = 1`), and strictly monotone inscribed/circumscribed
   semi-perimeters bracketing transcendental :math:`\pi`.
2. :func:`construct_transmutatio_isoperimetra` & :func:`verify_transmutatio_1445`
   (*De geometricis transmutationibus*, 1445, §§9–11): Cusa's compass-and-straightedge
   quarter-side *sesquiquarta* (:math:`5:4`) rectification of the inscribed equilateral
   triangle ``BCD`` in unit circle ``A``, producing :math:`|AE| = \frac{\sqrt{7}}{4}`,
   isoperimetric radius :math:`|AH| = \frac{5\sqrt{7}}{16}`, and
   :math:`\pi_{\text{Cusa},1445} = \frac{24\sqrt{21}}{35} \approx 3.14233762`.
3. :func:`construct_aurea_propositio` & :func:`verify_cusa_snellius_approximation`
   (*De mathematica perfectione*, 1458, & *Aurea propositio in mathematicis*, August 8, 1459):
   Exact :math:`\mathbb{Q}(\sqrt{3})` construction of Cusa's three-ray sector ``AB, AD, AC``
   terminated by arc ``BDC``, chord ``BHC``, tangent ``EDG``, and compensated segment ``IKL``
   with :math:`AK = \frac{3\cos\theta}{2 + \cos\theta}`, together with the SymPy Maclaurin
   proof of fifth-order accuracy:
   :math:`\theta - \frac{3\sin\theta}{2 + \cos\theta} = \frac{\theta^5}{180} + \frac{\theta^7}{1512} + O(\theta^9)`.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, clean_expr, quadrance, zero_test

__all__ = [
    "PolygonExhaustionEntry",
    "compute_polygon_exhaustion_table",
    "construct_polygon_exhaustion",
    "construct_transmutatio_isoperimetra",
    "verify_transmutatio_1445",
    "construct_aurea_propositio",
    "verify_cusa_snellius_approximation",
    "construct_generative_unfolding",
    "construct_cosmic_relativity_frame",
    "construct_transsumptio_ascent",
]


@dataclass(frozen=True)
class PolygonExhaustionEntry:
    r"""Exact symbolic invariants of regular :math:`n`-gons inscribed/circumscribed to unit circle.

    Attributes:
        sides: Number of polygon sides :math:`n`.
        prima_linea_inradius: Exact radical inradius :math:`r_n = \cos(\pi / n)`.
        secunda_linea_circumradius: Unit circumradius :math:`R_n = 1`.
        radius_defect: Radial gap :math:`1 - r_n` between *secunda* and *prima linea*.
        inscribed_semiperimeter: Exact radical :math:`n \sin(\pi / n) < \pi`.
        circumscribed_semiperimeter: Exact radical :math:`n \tan(\pi / n) > \pi`.
        inscribed_area: Exact radical :math:`\frac{n}{2}\sin(2\pi / n) < \pi`.
        circumscribed_area: Exact radical :math:`n \tan(\pi / n) > \pi`.
    """

    sides: int
    prima_linea_inradius: sp.Expr
    secunda_linea_circumradius: sp.Integer
    radius_defect: sp.Expr
    inscribed_semiperimeter: sp.Expr
    circumscribed_semiperimeter: sp.Expr
    inscribed_area: sp.Expr
    circumscribed_area: sp.Expr


def _new_exact_model(name: str) -> Model:
    """Create a deterministic exact :class:`~geometor.model.Model` with ``auto_intersect=False``."""
    return Model(name, auto_intersect=False, enable_logging=False)


def _exact_cos_sin_pi_over(n: int) -> tuple[sp.Expr, sp.Expr]:
    """Return closed-form radical ``(cos(pi/n), sin(pi/n))`` without trig functions."""
    if n == 3:
        return (sp.Rational(1, 2), sp.sqrt(3) / 2)
    if n == 4:
        return (sp.sqrt(2) / 2, sp.sqrt(2) / 2)
    if n == 6:
        return (sp.sqrt(3) / 2, sp.Rational(1, 2))
    if n == 8:
        return (sp.sqrt(2 + sp.sqrt(2)) / 2, sp.sqrt(2 - sp.sqrt(2)) / 2)
    if n == 12:
        return ((sp.sqrt(6) + sp.sqrt(2)) / 4, (sp.sqrt(6) - sp.sqrt(2)) / 4)
    c_val = sp.trigsimp(sp.cos(sp.pi / n)).rewrite(sp.sqrt)
    s_val = sp.trigsimp(sp.sin(sp.pi / n)).rewrite(sp.sqrt)
    return (c_val, s_val)


def compute_polygon_exhaustion_table(
    sides: Sequence[int] = (3, 4, 6, 8, 12),
) -> list[PolygonExhaustionEntry]:
    """Compute Cusa's I.3 / 1453 *prima* & *secunda linea* and semi-perimeter bounds for ``pi``.

    Args:
        sides: Strictly increasing sequence of polygon side counts.

    Returns:
        Verified list of :class:`PolygonExhaustionEntry` instances.
    """
    rows: list[PolygonExhaustionEntry] = []
    for n_val in sides:
        c_n, s_n = _exact_cos_sin_pi_over(n_val)
        if not zero_test(c_n**2 + s_n**2 - 1):
            raise AssertionError(f"Pythagorean radical check failed for n={n_val}.")
        t_n = sp.radsimp(s_n / c_n)
        in_semi = sp.radsimp(sp.Integer(n_val) * s_n)
        out_semi = sp.radsimp(sp.Integer(n_val) * t_n)
        in_area = sp.radsimp(sp.Integer(n_val) * s_n * c_n)
        out_area = out_semi
        rows.append(
            PolygonExhaustionEntry(
                sides=n_val,
                prima_linea_inradius=c_n,
                secunda_linea_circumradius=sp.Integer(1),
                radius_defect=sp.Integer(1) - c_n,
                inscribed_semiperimeter=in_semi,
                circumscribed_semiperimeter=out_semi,
                inscribed_area=in_area,
                circumscribed_area=out_area,
            )
        )

    # Verify strict monotonicity bracketing transcendental pi
    for prev, curr in zip(rows, rows[1:], strict=False):
        if not bool(prev.prima_linea_inradius < curr.prima_linea_inradius):
            raise AssertionError("Prima linea (inradius) failed strict increase.")
        if not bool(prev.inscribed_semiperimeter < curr.inscribed_semiperimeter):
            raise AssertionError("Inscribed semiperimeter failed strict increase.")
        if not bool(curr.circumscribed_semiperimeter < prev.circumscribed_semiperimeter):
            raise AssertionError("Circumscribed semiperimeter failed strict decrease.")

    if rows:
        last = rows[-1]
        if not bool(last.inscribed_semiperimeter < sp.pi < last.circumscribed_semiperimeter):
            raise AssertionError("Transcendental pi not bracketed by polygon semiperimeters.")

    return rows


def construct_polygon_exhaustion(
    sides: Sequence[int] = (3, 4, 6),
    model: Model | None = None,
) -> Model:
    r"""Construct Cusa's I.3 nested regular polygons inscribed and circumscribed to the unit circle.

    Builds unit circle ``( O V0 )`` over :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3})` together
    with inscribed regular polygons (:math:`n = 3, 4, 6` by default) and the circumscribed
    square to illustrate the irreducible gap between multiplied polygonal angles and the
    indivisible circular circumference.

    Args:
        sides: Polygon side counts drawn in the geometric model (default ``(3, 4, 6)``;
            supports ``3, 4, 6, 8, 12``).
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`~geometor.model.Model` with exact algebraic coordinates.
    """
    m = model if model is not None else _new_exact_model("cusa_polygon_exhaustion")

    o_pt = m.given_point(sp.Integer(0), sp.Integer(0), ID="O", classes=["given", "harmonic"])
    v0_pt = m.given_point(sp.Integer(1), sp.Integer(0), ID="V0", classes=["given"])
    unit_circ = m.construct_circle(o_pt, v0_pt, classes=["conic"], by="Post.3")

    poly_styles = {3: "diamond", 4: "square", 6: "circle", 8: "hexagon", 12: "hexagon"}
    prefix_map = {3: "T", 4: "S", 6: "H", 8: "K", 12: "D"}

    for n_val in sides:
        verts: list[spg.Point] = []
        pref = prefix_map.get(n_val, f"P{n_val}_")
        for k in range(n_val):
            ang = sp.Rational(2 * k, n_val) * sp.pi + sp.pi / sp.Integer(2)
            vx = sp.trigsimp(sp.cos(ang)).rewrite(sp.sqrt)
            vy = sp.trigsimp(sp.sin(ang)).rewrite(sp.sqrt)
            pt = m.given_point(vx, vy, ID=f"{pref}{k + 1}", classes=["meet"])
            m.assert_incident(pt, unit_circ, by="Def.15", label=f"{pref}{k + 1} on unit circle")
            verts.append(pt)
        m.construct_polygon(verts, classes=[poly_styles.get(n_val, "circle")], by="IV.15")
        for idx in range(n_val):
            m.construct_line(
                verts[idx],
                verts[(idx + 1) % n_val],
                classes=["pappus", "even" if n_val != 3 else "odd"],
                by="Post.1",
            )

    # Circumscribed square < W1 W2 W3 W4 > showing outer Archimedian bound
    w1 = m.given_point(sp.Integer(1), sp.Integer(1), ID="W1", classes=["auxiliary"])
    w2 = m.given_point(sp.Integer(-1), sp.Integer(1), ID="W2", classes=["auxiliary"])
    w3 = m.given_point(sp.Integer(-1), sp.Integer(-1), ID="W3", classes=["auxiliary"])
    w4 = m.given_point(sp.Integer(1), sp.Integer(-1), ID="W4", classes=["auxiliary"])
    for wa, wb in ((w1, w2), (w2, w3), (w3, w4), (w4, w1)):
        m.construct_line(wa, wb, classes=["quadrilateral", "diagonal"], by="IV.7")

    # Show Cusa's prima linea (apothem OF3 = 1/2) vs secunda linea (circumradius OV0 = 1)
    f3_pt = m.given_point(sp.Integer(0), sp.Rational(-1, 2), ID="F", classes=["fourth_harmonic"])
    m.construct_line(o_pt, f3_pt, classes=["harmonic"], by="I.12")
    m.construct_line(o_pt, v0_pt, classes=["carrier"], by="Post.1")

    return m


def construct_transmutatio_isoperimetra(model: Model | None = None) -> Model:
    r"""Construct Cusa's 1445 *De Geometricis Transmutationibus* (§§9–11) rectification.

    In unit circle ``( A D )`` centered at ``A = (0, 0)``, inscribes equilateral triangle
    ``< B C D >``, divides side ``[ B C ]`` into four equal quarters at ``E, F, G``, draws
    ray ``[ A E ]`` of exact length :math:`\frac{\sqrt{7}}{4}`, and extends it in
    *sesquiquarta* ratio (:math:`5 : 4`) to ``H`` with :math:`|AH| = \frac{5\sqrt{7}}{16}`,
    the radius of Cusa's nearly isoperimetric circle ``( A H )``.

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`~geometor.model.Model` over :math:`\mathbb{Q}(\sqrt{3})`.
    """
    m = model if model is not None else _new_exact_model("cusa_transmutatio_1445")

    a_pt = m.given_point(sp.Integer(0), sp.Integer(0), ID="A", classes=["given", "harmonic"])
    d_pt = m.given_point(sp.Integer(0), sp.Integer(1), ID="D", classes=["given"])
    b_pt = m.given_point(-sp.sqrt(3) / 2, sp.Rational(-1, 2), ID="B", classes=["given"])
    c_pt = m.given_point(sp.sqrt(3) / 2, sp.Rational(-1, 2), ID="C", classes=["given"])

    # Circumscribed circle ( A D ) of radius 1
    m.construct_circle(a_pt, d_pt, classes=["conic"], by="Post.3")

    # Inscribed equilateral triangle < B C D > of side sqrt(3) and perimeter 3*sqrt(3)
    m.construct_polygon([b_pt, c_pt, d_pt], classes=["diamond"], by="IV.2")
    m.construct_line(b_pt, c_pt, classes=["carrier"], by="Post.1")
    m.construct_line(c_pt, d_pt, classes=["carrier"], by="Post.1")
    m.construct_line(d_pt, b_pt, classes=["carrier"], by="Post.1")

    # Quarter points E, F, G dividing BC into four equal segments
    e_pt = m.given_point(-sp.sqrt(3) / 4, sp.Rational(-1, 2), ID="E", classes=["meet"])
    f_pt = m.given_point(sp.Integer(0), sp.Rational(-1, 2), ID="F", classes=["meet"])
    g_pt = m.given_point(sp.sqrt(3) / 4, sp.Rational(-1, 2), ID="G", classes=["meet"])

    # Inscribed circle ( A F ) of radius 1/2 (Cusa's prima linea)
    m.construct_circle(a_pt, f_pt, classes=["conic"], by="IV.4")
    m.construct_line(a_pt, f_pt, classes=["cross"], by="Post.1")

    # Sesquiquarta extension (5/4) along ray AE to H
    h_pt = m.given_point(
        sp.Rational(-5, 16) * sp.sqrt(3),
        sp.Rational(-5, 8),
        ID="H",
        classes=["steiner"],
    )
    m.construct_line(a_pt, h_pt, classes=["steiner_line"], by="Post.2")
    m.construct_circle(a_pt, h_pt, classes=["conic"], by="Post.3")

    m.assert_equal((b_pt, e_pt), (e_pt, f_pt), (f_pt, g_pt), (g_pt, c_pt), by="Def.15", label="BC quartered at E, F, G")
    m.assert_collinear(a_pt, e_pt, h_pt, by="Post.2", label="A, E, H collinear")
    if not zero_test(quadrance(a_pt, e_pt) - sp.Rational(7, 16)):
        raise AssertionError("Q(A, E) != 7/16")
    if not zero_test(quadrance(a_pt, h_pt) - sp.Rational(175, 256)):
        raise AssertionError("Q(A, H) != 175/256")

    return m


def verify_transmutatio_1445() -> dict[str, Any]:
    r"""Verify Cusa's 1445 *sesquiquarta* rectification and implied algebraic :math:`\pi`.

    Since the inscribed equilateral triangle has exact perimeter :math:`3\sqrt{3}` and Cusa's
    isoperimetric circle has radius :math:`r_{\text{Cusa}} = |AH| = \frac{5\sqrt{7}}{16}`,
    equating :math:`2 \pi_{\text{Cusa}} r_{\text{Cusa}} = 3\sqrt{3}` gives:

    .. math::

       \pi_{\text{Cusa},1445} = \frac{3\sqrt{3}}{2 \cdot \frac{5\sqrt{7}}{16}}
       = \frac{24\sqrt{21}}{35} \approx 3.1423373949

    exceeding true :math:`\pi` by only :math:`7.447 \times 10^{-4}` (relative error
    :math:`2.37 \times 10^{-4}`, well inside Archimedes' upper bound :math:`22/7 \approx 3.142857`).

    Returns:
        Dictionary of exact symbolic quantities and error bounds.
    """
    tri_perimeter = 3 * sp.sqrt(3)
    ae_len = sp.sqrt(7) / 4
    ah_len = sp.Rational(5, 4) * ae_len
    pi_cusa = sp.radsimp(tri_perimeter / (2 * ah_len))
    expected_pi = sp.Rational(24, 35) * sp.sqrt(21)

    if not zero_test(pi_cusa - expected_pi):
        raise AssertionError(f"Expected 24*sqrt(21)/35, got {pi_cusa}.")
    if not bool(sp.pi < pi_cusa < sp.Rational(22, 7)):
        raise AssertionError("Cusa's 1445 pi failed pi < pi_Cusa < 22/7.")

    abs_err = float((pi_cusa - sp.pi).evalf(20))
    rel_err = float(((pi_cusa - sp.pi) / sp.pi).evalf(20))

    return {
        "triangle_perimeter": tri_perimeter,
        "ae_length": ae_len,
        "ah_radius": ah_len,
        "pi_cusa_1445": pi_cusa,
        "abs_error": abs_err,
        "rel_error": rel_err,
    }


def construct_aurea_propositio(model: Model | None = None) -> Model:
    r"""Construct Cusa's 1458–1459 *Aurea Propositio* three-ray diagram over :math:`\mathbb{Q}(\sqrt{3})`.

    Instantiates *Aurea propositio in mathematicis* (§§1–2) at half-angle
    :math:`\theta = \frac{\pi}{6}` (:math:`30^\circ`) so every point lies in exact
    :math:`\mathbb{Q}(\sqrt{3})`:

    - Center ``A = (0, 0)``, middle ray ``[ A D ]`` to ``D = (1, 0)``, outer rays at
      :math:`\pm 30^\circ` through ``B = (\sqrt{3}/2, 1/2)`` and ``C = (\sqrt{3}/2, -1/2)``;
    - Circular arc ``( A D )``, chord ``[ B C ]`` meeting ``[ A D ]`` at ``H = (\sqrt{3}/2, 0)``,
      and tangent ``[ E G ]`` at ``D`` with ``E = (1, \sqrt{3}/3)``, ``G = (1, -\sqrt{3}/3)``;
    - Cusa's compensated rectification segment ``[ I L ]`` through
      :math:`K = \left(\frac{3\cos\theta}{2 + \cos\theta}, 0\right) = \left(\frac{12\sqrt{3} - 9}{13}, 0\right)`,
      where :math:`|AI| + |AK| + |AL| = 3 = |AB| + |AD| + |AC|` and
      :math:`|IL| = \frac{6\sin\theta}{2 + \cos\theta} = \frac{24 - 6\sqrt{3}}{13} \approx \text{arc}(BDC)`.

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`~geometor.model.Model` over :math:`\mathbb{Q}(\sqrt{3})`.
    """
    m = model if model is not None else _new_exact_model("cusa_aurea_propositio_1459")

    s3 = sp.sqrt(3)
    a_pt = m.given_point(sp.Integer(0), sp.Integer(0), ID="A", classes=["given", "harmonic"])
    d_pt = m.given_point(sp.Integer(1), sp.Integer(0), ID="D", classes=["given"])
    b_pt = m.given_point(s3 / 2, sp.Rational(1, 2), ID="B", classes=["given"])
    c_pt = m.given_point(s3 / 2, sp.Rational(-1, 2), ID="C", classes=["given"])
    h_pt = m.given_point(s3 / 2, sp.Integer(0), ID="H", classes=["meet"])

    e_pt = m.given_point(sp.Integer(1), s3 / 3, ID="E", classes=["meet"])
    g_pt = m.given_point(sp.Integer(1), -s3 / 3, ID="G", classes=["meet"])

    k_x = clean_expr((12 * s3 - 9) / 13)
    i_y = clean_expr((12 - 3 * s3) / 13)
    k_pt = m.given_point(k_x, sp.Integer(0), ID="K", classes=["fourth_harmonic"])
    i_pt = m.given_point(k_x, i_y, ID="I", classes=["steiner"])
    l_pt = m.given_point(k_x, -i_y, ID="L", classes=["steiner"])

    # Unit circle carrying arc BDC
    m.construct_circle(a_pt, d_pt, classes=["conic"], by="Post.3")

    # Three rays AB, AD, AC from center A
    m.construct_line(a_pt, e_pt, classes=["carrier"], by="Post.1")
    m.construct_line(a_pt, d_pt, classes=["carrier"], by="Post.1")
    m.construct_line(a_pt, g_pt, classes=["carrier"], by="Post.1")

    # Chord BHC, tangent EDG, and Cusa's compensated rectification segment IKL
    m.construct_line(b_pt, c_pt, classes=["pappus", "even"], by="Post.1")
    m.construct_line(e_pt, g_pt, classes=["quadrilateral"], by="III.16")
    m.construct_line(i_pt, l_pt, classes=["steiner_line"], by="Post.1")

    m.assert_equal((a_pt, b_pt), (a_pt, d_pt), (a_pt, c_pt), by="Def.15", label="Three equal arc radii")
    m.assert_collinear(a_pt, b_pt, i_pt, e_pt, by="Post.1", label="Upper ray ABIE")
    m.assert_collinear(a_pt, c_pt, l_pt, g_pt, by="Post.1", label="Lower ray ACLG")
    m.assert_collinear(a_pt, h_pt, k_pt, d_pt, by="Post.1", label="Middle ray AHKD")

    # Verify exact three-ray sum AI + AK + AL == 3 == AB + AD + AC
    ai_len = sp.sqrt(quadrance(a_pt, i_pt))
    ak_len = sp.sqrt(quadrance(a_pt, k_pt))
    al_len = sp.sqrt(quadrance(a_pt, l_pt))
    if not zero_test(ai_len + ak_len + al_len - sp.Integer(3)):
        raise AssertionError("|AI| + |AK| + |AL| != 3")
    if not zero_test((ai_len - 1) + (al_len - 1) - (1 - ak_len)):
        raise AssertionError("Endpoint ascent != midpoint descent")

    return m


def verify_cusa_snellius_approximation() -> dict[str, Any]:
    r"""Prove Cusa's three-ray identity and the fifth-order Maclaurin series residual.

    Verifies symbolically in SymPy:

    1. **Exact Chord–Tangent Three-Ray Invariance** (*Aurea propositio* §1):
       :math:`\frac{|AB| + |AH| + |AC|}{|BC|} = \frac{2 + \cos\theta}{2\sin\theta}
       \equiv \frac{2\sec\theta + 1}{2\tan\theta} = \frac{|AE| + |AD| + |AG|}{|EG|}`.
    2. **Fifth-Order Maclaurin / Padé Series** (*De mathematica perfectione* & *Aurea propositio*):
       :math:`\theta - \frac{3\sin\theta}{2 + \cos\theta}
       = \frac{\theta^5}{180} + \frac{\theta^7}{1512} + \frac{\theta^9}{25920} + O(\theta^{11})`.
    3. **Algebraic :math:`\pi` Approximations** at :math:`\theta = \frac{\pi}{4}, \frac{\pi}{6}, \frac{\pi}{12}`.

    Returns:
        Dictionary of verified symbolic expressions, series coefficients, and :math:`\pi` bounds.
    """
    theta = sp.Symbol("theta", positive=True)

    chord_ratio = (2 + sp.cos(theta)) / (2 * sp.sin(theta))
    tangent_ratio = (2 / sp.cos(theta) + 1) / (2 * sp.tan(theta))
    if sp.trigsimp(chord_ratio - tangent_ratio) != 0:
        raise AssertionError("Chord and tangent three-ray ratios failed exact equality.")

    cusa_arc_approx = 3 * sp.sin(theta) / (2 + sp.cos(theta))
    residual_series = sp.series(theta - cusa_arc_approx, theta, 0, 11).removeO()

    c5 = residual_series.coeff(theta, 5)
    c7 = residual_series.coeff(theta, 7)
    c9 = residual_series.coeff(theta, 9)
    for deg in range(5):
        if residual_series.coeff(theta, deg) != 0:
            raise AssertionError(f"Unexpected lower-order term at degree {deg}: {residual_series}")
    if c5 != sp.Rational(1, 180) or c7 != sp.Rational(1, 1512) or c9 != sp.Rational(1, 25920):
        raise AssertionError(f"Unexpected Maclaurin coefficients: c5={c5}, c7={c7}, c9={c9}")

    # Exact algebraic pi approximations pi ~= n * 3*sin(pi/n) / (2 + cos(pi/n))
    pi_estimates: dict[int, sp.Expr] = {}
    for n_div in (4, 6, 12):
        c_val, s_val = _exact_cos_sin_pi_over(n_div)
        pi_est = sp.radsimp(sp.Integer(n_div) * 3 * s_val / (2 + c_val))
        pi_estimates[n_div] = pi_est

    return {
        "chord_ratio": chord_ratio,
        "tangent_ratio_equal": True,
        "cusa_approx": cusa_arc_approx,
        "maclaurin_residual": residual_series,
        "coeff_theta_5": c5,
        "coeff_theta_7": c7,
        "coeff_theta_9": c9,
        "pi_at_pi_over_4": pi_estimates[4],
        "pi_at_pi_over_6": pi_estimates[6],
        "pi_at_pi_over_12": pi_estimates[12],
    }


def construct_transsumptio_ascent(model: Model | None = None) -> Model:
    r"""Construct the schematic diagram for Cusa's Three-Step Method of Transsumption (I.12).

    Illustrates Step 1 (finite chord ``[ B C ]`` and sagitta ``[ H D ]`` on a finite circle),
    Step 2 (expanded circle diminishing the sagitta ``[ K D ]`` toward the tangent ``[ E G ]``),
    and Step 3 (intellectual ascent onto the uncontracted straight Maximum ``[ E G ]``).

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`~geometor.model.Model` over :math:`\mathbb{Q}(\sqrt{3})`.
    """
    m = model if model is not None else _new_exact_model("cusa_transsumptio_ascent")

    d_pt = m.given_point(sp.Integer(0), sp.Integer(0), ID="D", classes=["given", "harmonic"])
    e_pt = m.given_point(sp.Integer(-2), sp.Integer(0), ID="E", classes=["given"])
    g_pt = m.given_point(sp.Integer(2), sp.Integer(0), ID="G", classes=["given"])
    m.construct_line(e_pt, g_pt, classes=["carrier", "harmonic"], by="Post.1")

    c1_pt = m.given_point(sp.Integer(0), sp.Integer(-1), ID="O1", classes=["given"])
    c2_pt = m.given_point(sp.Integer(0), sp.Integer(-2), ID="O2", classes=["auxiliary"])
    m.construct_circle(c1_pt, d_pt, classes=["conic"], by="Post.3")
    m.construct_circle(c2_pt, d_pt, classes=["conic"], by="Post.3")
    m.construct_line(c2_pt, d_pt, classes=["cross"], by="Post.1")

    s3 = sp.sqrt(3)
    b_pt = m.given_point(-s3 / 2, sp.Rational(-1, 2), ID="B", classes=["meet"])
    c_pt = m.given_point(s3 / 2, sp.Rational(-1, 2), ID="C", classes=["meet"])
    m.given_point(sp.Integer(0), sp.Rational(-1, 2), ID="H", classes=["meet"])
    m.construct_line(b_pt, c_pt, classes=["pappus", "odd"], by="Post.1")

    b2_pt = m.given_point(-s3, sp.Integer(-1), ID="P", classes=["fourth_harmonic"])
    c2_arc_pt = m.given_point(s3, sp.Integer(-1), ID="Q", classes=["fourth_harmonic"])
    m.construct_line(b2_pt, c2_arc_pt, classes=["pappus", "even"], by="Post.1")

    return m


def construct_generative_unfolding(model: Model | None = None) -> Model:
    r"""Construct Cusa's generative unfolding ``Line -> Triangle -> Circle -> Sphere`` (I.13, I.15, I.21, I.23).

    Models how fixed endpoint ``A = (0, 0)`` carrying radius ``[ A B ]`` generates by rotation
    the sector/triangle ``< A B C >``, the full circle ``( A B )`` with diameter ``[ B D ]``,
    and the equatorial/meridian circles representing the sphere unfolded by half-revolution
    of semicircle ``BCD`` around ``[ B D ]``.

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`~geometor.model.Model` over :math:`\mathbb{Q}(\sqrt{3})`.
    """
    m = model if model is not None else _new_exact_model("cusa_line_unfolding_sphere")

    a_pt = m.given_point(sp.Integer(0), sp.Integer(0), ID="A", classes=["given", "harmonic"])
    b_pt = m.given_point(sp.Integer(1), sp.Integer(0), ID="B", classes=["given"])
    d_pt = m.given_point(sp.Integer(-1), sp.Integer(0), ID="D", classes=["given"])
    n_pt = m.given_point(sp.Integer(0), sp.Integer(1), ID="N", classes=["meet"])
    s_pt = m.given_point(sp.Integer(0), sp.Integer(-1), ID="S", classes=["meet"])
    c_pt = m.given_point(sp.Rational(1, 2), sp.sqrt(3) / 2, ID="C", classes=["steiner"])

    # Outer sphere boundary / generated circle ( A B )
    m.construct_circle(a_pt, b_pt, classes=["conic"], by="Post.3")

    # Diameter BD and polar axis NS
    m.construct_line(d_pt, b_pt, classes=["carrier", "harmonic"], by="Post.1")
    m.construct_line(s_pt, n_pt, classes=["cross"], by="I.11")

    # Generated triangle < A B C > from circumduction of AB to AC (I.15)
    m.construct_polygon([a_pt, b_pt, c_pt], classes=["diamond"], by="I.1")
    m.construct_line(a_pt, c_pt, classes=["pappus", "even"], by="Post.1")
    m.construct_line(b_pt, c_pt, classes=["pappus", "odd"], by="Post.1")

    # Latitude chord representing the three-dimensional revolution around NS / BD (I.13, I.23)
    e_pt = m.given_point(sp.Integer(0), sp.Rational(1, 2), ID="E", classes=["fourth_harmonic"])
    r_eq = m.given_point(sp.sqrt(3) / 2, sp.Rational(1, 2), ID="R", classes=["auxiliary"])
    l_eq = m.given_point(-sp.sqrt(3) / 2, sp.Rational(1, 2), ID="L", classes=["auxiliary"])
    m.construct_line(l_eq, r_eq, classes=["quadrilateral", "diagonal"], by="I.31")
    _ = e_pt

    return m


def construct_cosmic_relativity_frame(model: Model | None = None) -> Model:
    r"""Construct Cusa's II.11–12 perspectival relativity diagram (*undique centrum, nullibi circumferentia*).

    Illustrates *De docta ignorantia* II.11–12: an observer situated on Earth ``T``, Sun ``S``,
    Mars ``M``, or toward the Pole ``P`` each constructs an apparent local horizon circle
    treating their own station as an immobile center, while no physical point coincides with
    an absolute cosmic center or circumference.

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`~geometor.model.Model` over :math:`\mathbb{Q}`.
    """
    m = model if model is not None else _new_exact_model("cusa_cosmic_relativity")

    t_pt = m.given_point(sp.Integer(0), sp.Integer(0), ID="T", classes=["given", "harmonic"])
    s_pt = m.given_point(sp.Rational(3, 2), sp.Rational(1, 2), ID="S", classes=["steiner"])
    p_pt = m.given_point(sp.Rational(-1, 1), sp.Rational(3, 2), ID="P", classes=["fourth_harmonic"])
    l_pt = m.given_point(sp.Rational(-3, 4), sp.Rational(-1, 2), ID="L", classes=["meet"])
    m_pt = m.given_point(sp.Rational(1, 2), sp.Rational(-5, 4), ID="M", classes=["meet"])

    # Apparent horizon spheres around Earth T, Sun S, and Pole observer P
    t_rim = m.given_point(sp.Integer(2), sp.Integer(0), ID="H1", classes=["auxiliary"])
    s_rim = m.given_point(sp.Rational(7, 2), sp.Rational(1, 2), ID="H2", classes=["auxiliary"])
    p_rim = m.given_point(sp.Integer(1), sp.Rational(3, 2), ID="H3", classes=["auxiliary"])

    m.construct_circle(t_pt, t_rim, classes=["conic"], by="Post.3")
    m.construct_circle(s_pt, s_rim, classes=["conic"], by="Post.3")
    m.construct_circle(p_pt, p_rim, classes=["conic"], by="Post.3")

    # Mutual lines of sight between observer frames (T <-> S, T <-> P, S <-> P, T <-> L, S <-> M)
    m.construct_line(t_pt, s_pt, classes=["pappus", "even"], by="Post.1")
    m.construct_line(t_pt, p_pt, classes=["pappus", "odd"], by="Post.1")
    m.construct_line(s_pt, p_pt, classes=["steiner_line"], by="Post.1")
    m.construct_line(t_pt, l_pt, classes=["quadrilateral"], by="Post.1")
    m.construct_line(s_pt, m_pt, classes=["quadrilateral"], by="Post.1")

    return m

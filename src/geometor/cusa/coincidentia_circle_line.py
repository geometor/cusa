r"""Exact symbolic constructions and proofs for *De Docta Ignorantia* I.13 (Circle & Straight Line).

Models Nicholas of Cusa's celebrated coincidence of the infinite circle and tangent arc
with the infinite straight line (*De docta ignorantia*, Book I, Chapter 13):

1. :func:`construct_tangent_circle_pencil`: Coaxial parabolic pencil of circles
   :math:`C_R: x^2 + (y - R)^2 = R^2` (:math:`R \in \{1, 2, 4, 8\}`) tangent to the
   horizon line :math:`y = 0` at :math:`O = (0, 0)`, intersected by the secant lines
   :math:`x = \pm 1` in exact quadratic radicals (:math:`1, 2-\sqrt{3}, 4-\sqrt{15}, 8-3\sqrt{7}`).
2. :func:`verify_sagitta_and_curvature_limits`: Exact SymPy symbolic rationalization of
   the sagitta :math:`h(x, R) = R - \sqrt{R^2 - x^2} = \frac{x^2}{R + \sqrt{R^2 - x^2}}`,
   proving :math:`\lim_{R \to \infty} h(x, R) = 0`,
   :math:`\lim_{R \to \infty} R \cdot h(x, R) = \frac{x^2}{2}`, and curvature
   :math:`\kappa(R) = \frac{1}{R} \to 0`.
3. :func:`construct_circle_line_inversion` & :func:`verify_mobius_inversion_coincidence`:
   Exact Möbius circle-inversion proofs demonstrating both (a) inversion at :math:`O = (0, 0)`
   mapping every circle :math:`C_R` to the horizontal straight line :math:`y = \frac{1}{2R} \to 0`,
   and (b) bounded inversion in the unit circle :math:`\Omega` centered at :math:`S = (0, -1)`
   mapping every :math:`C_R` to the rational circle :math:`C'_R` centered at
   :math:`\left(0, -\frac{R}{2R+1}\right)` of radius :math:`\frac{R}{2R+1}`, whose continuous
   limit :math:`C'_\infty` at :math:`\left(0, -\frac{1}{2}\right)` of radius :math:`\frac{1}{2}`
   is identically the inverse image of the straight horizon line :math:`y = 0`.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any

import sympy as sp
from geometor.model import Model, clean_expr, quadrance, zero_test

__all__ = [
    "TangentPencilEntry",
    "InversionCircleEntry",
    "compute_tangent_pencil_table",
    "construct_tangent_circle_pencil",
    "verify_sagitta_and_curvature_limits",
    "construct_circle_line_inversion",
    "verify_mobius_inversion_coincidence",
]


@dataclass(frozen=True)
class TangentPencilEntry:
    r"""Exact metrics of a circle :math:`C_R` in Cusa's I.13 tangent pencil at secant :math:`x = 1`.

    Attributes:
        radius: Exact rational radius :math:`R`.
        center_y: Center ordinate :math:`R` on the normal axis :math:`x = 0`.
        secant_ordinate: Exact quadratic radical ordinate :math:`R - \sqrt{R^2 - 1}` at :math:`x = 1`.
        rationalized_ordinate: Conjugate-rationalized sagitta :math:`\frac{1}{R + \sqrt{R^2 - 1}}`.
        curvature: Exact rational curvature :math:`\kappa = 1 / R`.
    """

    radius: sp.Rational
    center_y: sp.Rational
    secant_ordinate: sp.Expr
    rationalized_ordinate: sp.Expr
    curvature: sp.Rational


@dataclass(frozen=True)
class InversionCircleEntry:
    r"""Image of :math:`C_R` (or horizon :math:`y = 0`) under Möbius inversion in :math:`\Omega(S, 1)`.

    Attributes:
        label: Source locus label (``"R=1"``, ``"R=2"``, ..., or ``"R=oo (line y=0)"``).
        inverted_center_y: Exact rational center ordinate :math:`-\frac{R}{2R + 1}` (or :math:`-\frac{1}{2}`).
        inverted_radius: Exact rational radius :math:`\frac{R}{2R + 1}` (or :math:`\frac{1}{2}`).
        antipode_y: Lower :math:`y`-intercept :math:`-\frac{2R}{2R + 1}` (or :math:`-1`).
    """

    label: str
    inverted_center_y: sp.Rational
    inverted_radius: sp.Rational
    antipode_y: sp.Rational


def _new_exact_model(name: str) -> Model:
    """Create a deterministic exact :class:`~geometor.model.Model` with ``auto_intersect=False``."""
    return Model(name, auto_intersect=False, enable_logging=False)


def compute_tangent_pencil_table(
    radii: Sequence[int] = (1, 2, 4, 8),
) -> list[TangentPencilEntry]:
    """Compute exact symbolic ordinates, rationalized sagittae, and curvatures at ``x = 1``.

    Args:
        radii: Positive integer radii :math:`R_k >= 1`.

    Returns:
        List of :class:`TangentPencilEntry` rows verified by ``zero_test``.
    """
    rows: list[TangentPencilEntry] = []
    for r_int in radii:
        if r_int < 1:
            raise ValueError(f"Radius must be >= 1 for secant x=1; got {r_int}.")
        r_val = sp.Rational(r_int)
        rad_term = sp.sqrt(r_val**2 - sp.Integer(1))
        sec_ord = clean_expr(r_val - rad_term)
        rat_ord = sp.Integer(1) / (r_val + rad_term)
        if not zero_test(sec_ord - rat_ord):
            raise AssertionError(f"Sagitta rationalization failed for R={r_int}.")
        rows.append(
            TangentPencilEntry(
                radius=r_val,
                center_y=r_val,
                secant_ordinate=sec_ord,
                rationalized_ordinate=rat_ord,
                curvature=sp.Rational(1, r_int),
            )
        )
    return rows


def construct_tangent_circle_pencil(
    radii: Sequence[int] = (1, 2, 4, 8),
    model: Model | None = None,
) -> Model:
    r"""Construct Cusa's I.13 coaxial pencil of circles tangent to the straight line ``AB`` at ``O``.

    Builds horizon line ``[ A B ]`` (:math:`y = 0`), tangency origin ``O = (0, 0)``,
    normal axis ``[ O C_max ]`` (:math:`x = 0`), circles ``( C_R O )`` for each
    :math:`R \in \text{radii}`, and symmetric vertical secants :math:`x = \pm 1`
    cutting the arcs in exact quadratic radicals :math:`P_R = (1, R - \sqrt{R^2 - 1})`
    and :math:`Q_R = (-1, R - \sqrt{R^2 - 1})`.

    Args:
        radii: Strictly positive integer radii (default ``(1, 2, 4, 8)``).
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`~geometor.model.Model` with zero floating-point coordinates.
    """
    m = model if model is not None else _new_exact_model("cusa_circle_line_pencil")

    o_pt = m.given_point(sp.Integer(0), sp.Integer(0), ID="O", classes=["given", "harmonic"])
    a_pt = m.given_point(sp.Integer(-2), sp.Integer(0), ID="A", classes=["given"])
    b_pt = m.given_point(sp.Integer(2), sp.Integer(0), ID="B", classes=["given"])
    w_pt = m.given_point(sp.Integer(-1), sp.Integer(0), ID="W", classes=["auxiliary"])
    x_pt = m.given_point(sp.Integer(1), sp.Integer(0), ID="X", classes=["given"])

    # Straight tangent horizon line AB (Cusa's linea infinita ab in I.13)
    m.construct_line(a_pt, b_pt, classes=["carrier", "harmonic"], by="Post.1")

    max_r = max(radii)
    top_pt = m.given_point(sp.Integer(0), sp.Integer(max_r), ID=f"C{max_r}", classes=["given"])
    m.construct_line(o_pt, top_pt, classes=["cross"], by="Post.1")

    # Vertical secant lines x = 1 and x = -1 measuring the sagitta h(1, R)
    x_up = m.given_point(sp.Integer(1), sp.Integer(1), ID="P1", classes=["meet"])
    w_up = m.given_point(sp.Integer(-1), sp.Integer(1), ID="Q1", classes=["meet"])
    sec_right = m.construct_line(x_pt, x_up, classes=["quadrilateral", "diagonal"], by="I.11")
    sec_left = m.construct_line(w_pt, w_up, classes=["quadrilateral", "diagonal"], by="I.11")

    for r_int in radii:
        r_sym = sp.Integer(r_int)
        if r_int == max_r:
            c_pt = top_pt
        else:
            c_pt = m.given_point(sp.Integer(0), r_sym, ID=f"C{r_int}", classes=["given"])

        circ = m.construct_circle(c_pt, o_pt, classes=["conic"], by="Post.3")

        if r_int == 1:
            p_pt = x_up
            q_pt = w_up
        else:
            # Horizontal diameter y = R separates the lower tangent-side arc from the upper arc
            horiz_ref = sp.geometry.Point(sp.Integer(1), r_sym)
            p_pt = m.intersect(
                sec_right,
                circ,
                side_of=(c_pt, horiz_ref, -1),
                ID=f"P{r_int}",
                classes=["meet"],
                by="Def.15",
            )
            q_pt = m.intersect(
                sec_left,
                circ,
                side_of=(c_pt, horiz_ref, -1),
                ID=f"Q{r_int}",
                classes=["meet"],
                by="Def.15",
            )

        expected_y = r_sym - sp.sqrt(r_sym**2 - sp.Integer(1))
        if not zero_test(p_pt.y - expected_y):
            raise AssertionError(f"Exact sagitta ordinate mismatch at R={r_int}: {p_pt.y}")
        m.assert_equal((c_pt, p_pt), (c_pt, o_pt), by="Def.15", label=f"P{r_int} on circle R={r_int}")
        m.construct_line(q_pt, p_pt, classes=["pappus", "even"], by="Post.1")

    return m


def verify_sagitta_and_curvature_limits() -> dict[str, sp.Expr | bool]:
    r"""Prove Cusa's I.13 asymptotic coincidence of circular arc and tangent line in SymPy.

    Returns:
        Dictionary of exact symbolic expressions and verified limit booleans.
    """
    r_sym = sp.Symbol("R", positive=True)
    x_sym = sp.Symbol("x", real=True, nonzero=True)

    sagitta = r_sym - sp.sqrt(r_sym**2 - x_sym**2)
    sagitta_rationalized = x_sym**2 / (r_sym + sp.sqrt(r_sym**2 - x_sym**2))
    curvature = sp.Integer(1) / r_sym

    identity_holds = sp.simplify(sagitta - sagitta_rationalized) == 0
    sagitta_limit = sp.limit(sagitta, r_sym, sp.oo)
    scaled_sagitta_limit = sp.limit(r_sym * sagitta, r_sym, sp.oo)
    curvature_limit = sp.limit(curvature, r_sym, sp.oo)

    if not identity_holds:
        raise AssertionError("Conjugate rationalization of sagitta failed.")
    if sagitta_limit != 0:
        raise AssertionError(f"Expected sagitta limit 0, got {sagitta_limit}.")
    if sp.simplify(scaled_sagitta_limit - x_sym**2 / 2) != 0:
        raise AssertionError(f"Expected R*h limit x^2/2, got {scaled_sagitta_limit}.")
    if curvature_limit != 0:
        raise AssertionError(f"Expected curvature limit 0, got {curvature_limit}.")

    return {
        "sagitta": sagitta,
        "sagitta_rationalized": sagitta_rationalized,
        "identity_holds": identity_holds,
        "sagitta_limit": sagitta_limit,
        "scaled_sagitta_limit": scaled_sagitta_limit,
        "curvature": curvature,
        "curvature_limit": curvature_limit,
    }


def construct_circle_line_inversion(
    radii: Sequence[int] = (1, 2, 4),
    model: Model | None = None,
) -> Model:
    r"""Construct the Möbius circle-inversion model unifying Cusa's tangent circles and straight line.

    Inverts the coaxial pencil :math:`C_R: x^2 + (y - R)^2 = R^2` and the horizon line
    :math:`y = 0` in the unit circle :math:`\Omega: x^2 + (y + 1)^2 = 1` centered at
    :math:`S = (0, -1)` passing through :math:`O = (0, 0)`:

    - Every finite circle :math:`C_R` maps to the exact rational circle :math:`C'_R`
      with center :math:`M_R = \left(0, -\frac{R}{2R + 1}\right)` and radius
      :math:`r'_R = \frac{R}{2R + 1}` tangent at :math:`O = (0, 0)`.
    - The straight horizon line :math:`y = 0` maps to :math:`C'_\infty` with center
      :math:`M_\infty = \left(0, -\frac{1}{2}\right)` and radius :math:`r'_\infty = \frac{1}{2}`
      passing through :math:`O = (0, 0)` and the inversion pole :math:`S = (0, -1)`.

    Args:
        radii: Positive integer source radii (default ``(1, 2, 4)``).
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`~geometor.model.Model` over :math:`\mathbb{Q}`.
    """
    m = model if model is not None else _new_exact_model("cusa_mobius_inversion")

    o_pt = m.given_point(sp.Integer(0), sp.Integer(0), ID="O", classes=["given", "harmonic"])
    a_pt = m.given_point(sp.Rational(-3, 2), sp.Integer(0), ID="A", classes=["given"])
    b_pt = m.given_point(sp.Rational(3, 2), sp.Integer(0), ID="B", classes=["given"])
    s_pt = m.given_point(sp.Integer(0), sp.Integer(-1), ID="S", classes=["steiner"])

    # Straight horizon line AB (y = 0) and vertical symmetry axis
    m.construct_line(a_pt, b_pt, classes=["carrier", "harmonic"], by="Post.1")
    top_ref = m.given_point(sp.Integer(0), sp.Rational(3, 2), ID="Z", classes=["auxiliary"])
    m.construct_line(s_pt, top_ref, classes=["cross"], by="Post.1")

    # Unit inversion circle Omega centered at S=(0,-1) passing through O=(0,0)
    m.construct_circle(s_pt, o_pt, classes=["conic"], by="Post.3")

    # Source circle R=1 above the horizon for visual reference
    c1_src = m.given_point(sp.Integer(0), sp.Integer(1), ID="C1", classes=["given"])
    m.construct_circle(c1_src, o_pt, classes=["conic"], by="Post.3")

    for r_int in radii:
        r_rat = sp.Rational(r_int)
        yc = -r_rat / (2 * r_rat + 1)
        m_pt = m.given_point(sp.Integer(0), yc, ID=f"M{r_int}", classes=["meet"])
        n_pt = m.given_point(sp.Integer(0), 2 * yc, ID=f"N{r_int}", classes=["auxiliary"])
        m.construct_circle(m_pt, o_pt, classes=["conic"], by="Post.3")
        m.assert_equal(
            (m_pt, n_pt),
            (m_pt, o_pt),
            by="Def.15",
            label=f"Inverted circle C'_{r_int} passes through antipode N{r_int} and O",
        )

    # Limit circle C'_oo = inverse image of the straight horizon line y = 0
    m_inf = m.given_point(sp.Integer(0), sp.Rational(-1, 2), ID="Minf", classes=["fourth_harmonic"])
    c_inf = m.construct_circle(m_inf, o_pt, classes=["conic"], by="Post.3")
    m.assert_equal(
        (m_inf, s_pt),
        (m_inf, o_pt),
        by="Def.15",
        label="Horizon line image C'_oo passes through both O=(0,0) and pole S=(0,-1)",
    )

    # Sample secant point X=(1,0) on y=0 and its exact inverse X'=(1/2, -1/2) on C'_oo
    x_pt = m.given_point(sp.Integer(1), sp.Integer(0), ID="X", classes=["given"])
    xp_pt = m.given_point(
        sp.Rational(1, 2),
        sp.Rational(-1, 2),
        ID="Xp",
        classes=["fourth_harmonic"],
    )
    m.construct_line(s_pt, x_pt, classes=["steiner_line"], by="Post.1")
    m.assert_collinear(s_pt, xp_pt, x_pt, by="Post.1", label="S, X', X collinear along inversion ray")
    m.assert_incident(xp_pt, c_inf, by="Def.15", label="X'=(1/2, -1/2) lies on C'_oo")
    if not zero_test(quadrance(s_pt, x_pt) * quadrance(s_pt, xp_pt) - sp.Integer(1)):
        raise AssertionError("Inversion power |SX|^2 * |SX'|^2 != 1")

    return m


def verify_mobius_inversion_coincidence(
    radii: Sequence[int] = (1, 2, 4, 8),
) -> dict[str, Any]:
    r"""Verify symbolically both Möbius inversion theorems for Cusa's I.13 pencil.

    1. **Origin Inversion** at :math:`O = (0, 0)`: maps :math:`x^2 + (y - R)^2 = R^2`
       to the horizontal line :math:`v = \frac{1}{2R}`, converging to :math:`v = 0`.
    2. **Pole Inversion** at :math:`S = (0, -1)` in :math:`\Omega: x^2 + (y + 1)^2 = 1`:
       maps :math:`C_R` to :math:`u^2 + \left(y' + \frac{R}{2R+1}\right)^2 = \left(\frac{R}{2R+1}\right)^2`,
       converging as :math:`R \to \infty` to :math:`u^2 + \left(y' + \frac{1}{2}\right)^2 = \frac{1}{4}`,
       the exact image of the straight line :math:`y = 0`.

    Args:
        radii: Sample integer radii for tabular output.

    Returns:
        Dictionary of verified symbolic identities and :class:`InversionCircleEntry` rows.
    """
    r_sym = sp.Symbol("R", positive=True)
    u_sym, v_sym = sp.symbols("u v", real=True)

    # 1. Inversion at O=(0,0): x = u/(u^2+v^2), y = v/(u^2+v^2)
    denom_o = u_sym**2 + v_sym**2
    xo = u_sym / denom_o
    yo = v_sym / denom_o
    circle_eq_o = sp.simplify((xo**2 + (yo - r_sym) ** 2 - r_sym**2) * denom_o)
    # circle_eq_o == 1 - 2*R*v == 0  <=>  v = 1/(2*R)
    origin_line_v = sp.solve(circle_eq_o, v_sym)[0]
    if sp.simplify(origin_line_v - sp.Integer(1) / (2 * r_sym)) != 0:
        raise AssertionError("Origin inversion failed to yield v = 1/(2R).")

    # 2. Inversion at S=(0,-1): x = U/(U^2+V^2), y+1 = V/(U^2+V^2), where U=x', V=y'+1
    yp_sym = sp.Symbol("yp", real=True)
    big_u = u_sym
    big_v = yp_sym + sp.Integer(1)
    denom_s = big_u**2 + big_v**2
    xs = big_u / denom_s
    ys = big_v / denom_s - sp.Integer(1)

    circle_eq_s = sp.simplify((xs**2 + (ys - r_sym) ** 2 - r_sym**2) * denom_s / (2 * r_sym + 1))
    yc_sym = -r_sym / (2 * r_sym + 1)
    rc_sym = r_sym / (2 * r_sym + 1)
    target_eq_s = big_u**2 + (yp_sym - yc_sym) ** 2 - rc_sym**2
    if sp.simplify(circle_eq_s - target_eq_s) != 0:
        raise AssertionError("Pole inversion circle equation mismatch.")

    # Straight line y = 0 image under S=(0,-1) inversion:
    line_eq_s = sp.simplify(ys * denom_s)  # V - (U^2 + V^2) == 0
    horizon_target = big_u**2 + (yp_sym + sp.Rational(1, 2)) ** 2 - sp.Rational(1, 4)
    if sp.simplify(-line_eq_s - horizon_target) != 0:
        raise AssertionError("Horizon line inversion equation mismatch.")

    limit_center_y = sp.limit(yc_sym, r_sym, sp.oo)
    limit_radius = sp.limit(rc_sym, r_sym, sp.oo)
    if limit_center_y != sp.Rational(-1, 2) or limit_radius != sp.Rational(1, 2):
        raise AssertionError("Inverted pencil limit did not match horizon image.")

    entries = [
        InversionCircleEntry(
            label=f"R={r_int}",
            inverted_center_y=sp.Rational(-r_int, 2 * r_int + 1),
            inverted_radius=sp.Rational(r_int, 2 * r_int + 1),
            antipode_y=sp.Rational(-2 * r_int, 2 * r_int + 1),
        )
        for r_int in radii
    ]
    entries.append(
        InversionCircleEntry(
            label="R=oo (line y=0)",
            inverted_center_y=sp.Rational(-1, 2),
            inverted_radius=sp.Rational(1, 2),
            antipode_y=sp.Rational(-1, 1),
        )
    )

    return {
        "origin_inverted_line_v": origin_line_v,
        "origin_limit_v": sp.limit(origin_line_v, r_sym, sp.oo),
        "pole_inverted_center_y": yc_sym,
        "pole_inverted_radius": rc_sym,
        "limit_center_y": limit_center_y,
        "limit_radius": limit_radius,
        "entries": entries,
    }

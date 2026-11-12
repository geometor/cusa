r"""Exact Rational Trigonometry constructions & proofs for *De Docta Ignorantia* I.14–15.

Models Nicholas of Cusa's proof that the infinite triangle coincides with the infinite
straight line (*De docta ignorantia*, Book I, Chapters 14–15):

Given fixed base endpoints :math:`B = (-1, 0)` and :math:`C = (1, 0)` (matching Cusa's
printed base ``bc`` in the 1514/1565/1913 diagrams of ``I.14``) and flattening apexes
:math:`A_n = \left(0, \frac{1}{n}\right)` for :math:`n \in \mathbb{Z}_{>0}`:

- Base quadrance :math:`Q_{BC} = 4`, equal side quadrances :math:`Q_{BA_n} = Q_{A_n C} = 1 + \frac{1}{n^2}`.
- Pure rational base spreads :math:`s_B = s_C = \frac{1}{n^2 + 1} \in \mathbb{Q}` and
  apex spread :math:`s_{A_n} = \frac{4n^2}{(n^2 + 1)^2} \in \mathbb{Q}`, satisfying
  Wildberger's **Triple Spread Formula** identically and :math:`\lim_{n \to \infty} s_{A_n} = 0`
  (as the obtuse apex angle approaches two right angles, :math:`180^\circ`).
- Wildberger's **Triple Quad Formula** asymmetry
  :math:`\mathcal{Q}(Q_{BC}, Q_{BA_n}, Q_{A_n C}) = (Q_{BC} + Q_{BA_n} + Q_{A_n C})^2 - 2(Q_{BC}^2 + Q_{BA_n}^2 + Q_{A_n C}^2) = \frac{16}{n^2} = 16\,\text{Area}^2 \to 0`,
  vanishing identically when the triangle resolves into the simple straight line ``BC``.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, quadrance, vertex_spread, zero_test

__all__ = [
    "FlatteningTriangleMetrics",
    "compute_flattening_triangle_metrics",
    "construct_flattening_triangles",
    "verify_triangle_line_coincidence",
]


@dataclass(frozen=True)
class FlatteningTriangleMetrics:
    r"""Exact Rational Trigonometry invariants for :math:`\triangle B A_n C`.

    Attributes:
        step_n: Integer flattening index :math:`n` (:math:`h_n = 1/n`).
        altitude: Rational altitude :math:`1/n`.
        q_base: Base quadrance :math:`Q(B, C) = 4`.
        q_leg: Leg quadrance :math:`Q(B, A_n) = Q(A_n, C) = 1 + 1/n^2`.
        spread_base: Rational base spread :math:`s_B = s_C = \frac{1}{n^2 + 1}`.
        spread_apex: Rational apex spread :math:`s_{A_n} = \frac{4n^2}{(n^2 + 1)^2}`.
        triple_quad_residual: :math:`(Q_a + Q_b + Q_c)^2 - 2(Q_a^2 + Q_b^2 + Q_c^2) = 16/n^2`.
        area: Rational triangle area :math:`1/n`.
        side_excess: Exact radical excess :math:`2\sqrt{1 + 1/n^2} - 2` of two sides over base.
    """

    step_n: int
    altitude: sp.Rational
    q_base: sp.Rational
    q_leg: sp.Rational
    spread_base: sp.Rational
    spread_apex: sp.Rational
    triple_quad_residual: sp.Rational
    area: sp.Rational
    side_excess: sp.Expr


def _new_exact_model(name: str) -> Model:
    """Create a deterministic exact :class:`~geometor.model.Model` with ``auto_intersect=False``."""
    return Model(name, auto_intersect=False, enable_logging=False)


def compute_flattening_triangle_metrics(step_n: int) -> FlatteningTriangleMetrics:
    """Compute exact quadrances, rational spreads, Triple Quad residual, and side excess for ``n``.

    Args:
        step_n: Strictly positive integer step ``n``.

    Returns:
        :class:`FlatteningTriangleMetrics` verified via ``geometor.model`` invariants.
    """
    if step_n < 1:
        raise ValueError(f"step_n must be >= 1; got {step_n}.")

    b_pt = spg.Point(sp.Integer(-1), sp.Integer(0))
    c_pt = spg.Point(sp.Integer(1), sp.Integer(0))
    h_rat = sp.Rational(1, step_n)
    a_pt = spg.Point(sp.Integer(0), h_rat)

    q_base = sp.Rational(quadrance(b_pt, c_pt))
    q_leg_left = sp.Rational(quadrance(b_pt, a_pt))
    q_leg_right = sp.Rational(quadrance(a_pt, c_pt))
    if q_leg_left != q_leg_right:
        raise AssertionError("Isosceles leg quadrances failed symmetry.")

    s_base = sp.Rational(vertex_spread(a_pt, b_pt, c_pt))
    s_apex = sp.Rational(vertex_spread(b_pt, a_pt, c_pt))

    tqf_res = sp.Rational(
        (q_base + 2 * q_leg_left) ** 2 - 2 * (q_base**2 + 2 * q_leg_left**2)
    )
    tsf_res = (2 * s_base + s_apex) ** 2 - 2 * (2 * s_base**2 + s_apex**2) - 4 * s_base**2 * s_apex
    if not zero_test(tsf_res):
        raise AssertionError(f"Triple Spread Formula failed at n={step_n}: {tsf_res}")
    if tqf_res != sp.Rational(16, step_n**2):
        raise AssertionError(f"Triple Quad residual mismatch at n={step_n}: {tqf_res}")

    side_excess = 2 * sp.sqrt(q_leg_left) - sp.Integer(2)

    return FlatteningTriangleMetrics(
        step_n=step_n,
        altitude=h_rat,
        q_base=q_base,
        q_leg=q_leg_left,
        spread_base=s_base,
        spread_apex=s_apex,
        triple_quad_residual=tqf_res,
        area=h_rat,
        side_excess=side_excess,
    )


def construct_flattening_triangles(
    steps: Sequence[int] = (1, 2, 4, 8),
    model: Model | None = None,
) -> Model:
    r"""Construct Cusa's I.14–15 family of flattening triangles over :math:`\mathbb{Q}`.

    Builds fixed base ``[ B C ]`` with ``B = (-1, 0)``, ``C = (1, 0)``, midpoint
    ``M = (0, 0)``, and apexes ``A1, A2, A4, A8`` at :math:`(0, 1/n)` whose obtuse
    apex angle opens toward :math:`180^\circ` (:math:`s_{A_n} \to 0`) as the two sides
    ``[ B A_n ] + [ A_n C ]`` collapse onto the single line ``[ B C ]``.

    Args:
        steps: Positive integer sequence of altitude denominators (default ``(1, 2, 4, 8)``).
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`~geometor.model.Model` over :math:`\mathbb{Q}`.
    """
    m = model if model is not None else _new_exact_model("cusa_flattening_triangles")

    b_pt = m.given_point(sp.Integer(-1), sp.Integer(0), ID="B", classes=["given"])
    c_pt = m.given_point(sp.Integer(1), sp.Integer(0), ID="C", classes=["given"])
    m_pt = m.given_point(sp.Integer(0), sp.Integer(0), ID="M", classes=["given", "harmonic"])

    m.construct_line(b_pt, c_pt, classes=["carrier", "harmonic"], by="Post.1")

    min_step = min(steps)
    top_pt = m.given_point(
        sp.Integer(0),
        sp.Rational(1, min_step),
        ID=f"A{min_step}",
        classes=["meet"],
    )
    m.construct_line(m_pt, top_pt, classes=["cross"], by="I.11")

    for idx, n_val in enumerate(steps):
        if n_val == min_step:
            a_pt = top_pt
        else:
            a_pt = m.given_point(
                sp.Integer(0),
                sp.Rational(1, n_val),
                ID=f"A{n_val}",
                classes=["meet" if idx < len(steps) - 1 else "fourth_harmonic"],
            )

        line_cls = ["pappus", "odd" if idx % 2 else "even"]
        m.construct_line(b_pt, a_pt, classes=line_cls, by="Post.1")
        m.construct_line(a_pt, c_pt, classes=line_cls, by="Post.1")
        poly_cls = "diamond" if idx == 0 else ("circle" if idx == 1 else "square")
        m.construct_polygon([b_pt, a_pt, c_pt], classes=[poly_cls], by="Def.19")

        expected_s_apex = sp.Rational(4 * n_val**2, (n_val**2 + 1) ** 2)
        m.assert_equal((b_pt, a_pt), (a_pt, c_pt), by="I.5", label=f"Isosceles legs at n={n_val}")
        if not zero_test(vertex_spread(b_pt, a_pt, c_pt) - expected_s_apex):
            raise AssertionError(f"Apex spread mismatch at n={n_val}")

    return m


def verify_triangle_line_coincidence() -> dict[str, Any]:
    r"""Prove Cusa's I.14 triangle-to-line limit symbolically via Rational Trigonometry.

    Establishes over :math:`\mathbb{Q}(n)` for symbolic positive :math:`n`:

    1. :math:`s_A(n) = \frac{4n^2}{(n^2 + 1)^2}` and :math:`s_B(n) = s_C(n) = \frac{1}{n^2 + 1}`
       satisfy the **Triple Spread Formula** identically;
    2. :math:`\lim_{n \to \infty} s_A(n) = 0` and :math:`\lim_{n \to \infty} s_B(n) = 0`;
    3. The **Triple Quad Formula** asymmetry equals :math:`\frac{16}{n^2} \to 0`;
    4. The side-excess :math:`(|BA_n| + |A_n C| - |BC|) = \frac{2}{n^2\left(\sqrt{1 + 1/n^2} + 1\right)} \to 0`.

    Returns:
        Dictionary of symbolic invariants and limit checks.
    """
    n_sym = sp.Symbol("n", positive=True)

    q_c = sp.Integer(4)
    q_a = sp.Integer(1) + sp.Integer(1) / n_sym**2
    q_b = q_a

    # Cross law: (Q_a + Q_b - Q_c)^2 = 4 Q_a Q_b (1 - s_C_apex)
    s_apex = sp.simplify(sp.Integer(1) - (q_a + q_b - q_c) ** 2 / (4 * q_a * q_b))
    s_base = sp.simplify(sp.Integer(1) - (q_a + q_c - q_b) ** 2 / (4 * q_a * q_c))

    expected_s_apex = 4 * n_sym**2 / (n_sym**2 + 1) ** 2
    expected_s_base = sp.Integer(1) / (n_sym**2 + 1)
    if sp.simplify(s_apex - expected_s_apex) != 0:
        raise AssertionError(f"Symbolic apex spread mismatch: {s_apex}")
    if sp.simplify(s_base - expected_s_base) != 0:
        raise AssertionError(f"Symbolic base spread mismatch: {s_base}")

    triple_spread = sp.simplify(
        (2 * s_base + s_apex) ** 2
        - 2 * (2 * s_base**2 + s_apex**2)
        - 4 * s_base * s_base * s_apex
    )
    triple_quad = sp.simplify((q_a + q_b + q_c) ** 2 - 2 * (q_a**2 + q_b**2 + q_c**2))
    side_excess = 2 * sp.sqrt(1 + 1 / n_sym**2) - 2
    side_excess_rat = 2 / (n_sym**2 * (sp.sqrt(1 + 1 / n_sym**2) + 1))

    if triple_spread != 0:
        raise AssertionError("Symbolic Triple Spread Formula failed.")
    if sp.simplify(triple_quad - 16 / n_sym**2) != 0:
        raise AssertionError(f"Symbolic Triple Quad Formula mismatch: {triple_quad}")
    if sp.simplify(side_excess - side_excess_rat) != 0:
        raise AssertionError("Side-excess rationalization mismatch.")
    if sp.limit(s_apex, n_sym, sp.oo) != 0:
        raise AssertionError("Apex spread limit did not vanish.")
    if sp.limit(triple_quad, n_sym, sp.oo) != 0:
        raise AssertionError("Triple Quad residual limit did not vanish.")
    if sp.limit(side_excess, n_sym, sp.oo) != 0:
        raise AssertionError("Side-excess limit did not vanish.")

    return {
        "q_base": q_c,
        "q_leg": q_a,
        "spread_apex": s_apex,
        "spread_base": s_base,
        "triple_spread_identity": triple_spread == 0,
        "triple_quad_residual": triple_quad,
        "side_excess": side_excess,
        "side_excess_rationalized": side_excess_rat,
        "limit_spread_apex": sp.Integer(0),
        "limit_triple_quad": sp.Integer(0),
        "limit_side_excess": sp.Integer(0),
    }

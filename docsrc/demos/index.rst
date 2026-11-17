:order: 25
:nav_title: Demos

.. _demos:

=====
Demos
=====

.. rubric:: 100% Exact Symbolic SymPy Models, Möbius Inversion & Rational Trigonometry Proofs

In strict accordance with **GEOMETOR's Content / Code Separation**, the historical Book Codex (:doc:`/de_docta_ignorantia/index`) embeds zero Python scripts. All executable geometric constructions live in the ``geometor.cusa`` package and the standalone ``demos/*.py`` scripts documented below, verified over :math:`\mathbb{Q}`, :math:`\mathbb{Q}(\sqrt{2}, \sqrt{3}, \sqrt{6}, \sqrt{7}, \sqrt{15}, \sqrt{21})`, and :math:`\mathbb{Q}(n)` using ``Model(..., auto_intersect=False)`` with **zero floating-point approximations**.

----

1. *De Docta Ignorantia* ``I.13`` — Tangent Circle Pencil & Conformal Möbius Inversion
--------------------------------------------------------------------------------------

*Codex Reference*: :doc:`Capitula XIII–XV — De Coincidentia Figurarum (Notes) </de_docta_ignorantia/liber_i/cap_13_15/notes>` · *Script*: ``demos/coincidentia_circle_line.py``

.. picture:: /_static/figures/cusa_circle_line_pencil.svg
   :caption: Tangent circle pencil C_1, C_2, C_4, C_8 above straight horizon AB (y = 0) with exact radical sagittae 1, 2 - sqrt(3), 4 - sqrt(15), 8 - 3*sqrt(7) along vertical secant x = 1.

.. picture:: /_static/figures/cusa_mobius_inversion.svg
   :caption: Bounded conformal inversion in unit circle Omega at pole S = (0, -1), mapping C_R to finite rational circles C'_R centered at (0, -R/(2R+1)) converging smoothly to C'_inf = inverted line AB.

* **Exact Symbolic Verification**:
  Rationalizing the sagitta :math:`h(x, R) = R - \sqrt{R^2 - x^2} = \frac{x^2}{R + \sqrt{R^2 - x^2}}` proves :math:`\lim_{R \to \infty} h(x, R) = 0`, :math:`\lim_{R \to \infty} R\,h(x, R) = \frac{x^2}{2}`, and curvature :math:`\kappa(R) = \frac{1}{R} \to 0`. Under unit-circle inversion at :g:`S` :math:`= (0, -1)`, every circle :math:`C_R` maps to the exact rational circle centered at :math:`\left(0, -\frac{R}{2R+1}\right)` of radius :math:`\frac{R}{2R+1}`, whose :math:`R \to \infty` limit at :g:`Minf` :math:`= \left(0, -\frac{1}{2}\right)` is identically the inverted straight line :g:`[ A B ]`.

.. code-block:: python

   import sympy as sp
   from geometor.cusa import (
       construct_tangent_circle_pencil,
       verify_mobius_inversion_coincidence,
       verify_sagitta_and_curvature_limits,
   )

   model = construct_tangent_circle_pencil()
   assert not any(pt.has(sp.Float) for pt in model.points)

   limits = verify_sagitta_and_curvature_limits()
   assert limits["identity_holds"] and limits["sagitta_limit"] == 0

   mobius = verify_mobius_inversion_coincidence()
   assert mobius["limit_center_y"] == sp.Rational(-1, 2)
   assert mobius["limit_radius"] == sp.Rational(1, 2)

----

2. *De Docta Ignorantia* ``I.14–15`` — Flattening Triangles in Rational Trigonometry
------------------------------------------------------------------------------------

*Codex Reference*: :doc:`Capitula XIII–XV — De Coincidentia Figurarum (Notes) </de_docta_ignorantia/liber_i/cap_13_15/notes>` · *Script*: ``demos/coincidentia_triangle_line.py``

.. picture:: /_static/figures/cusa_flattening_triangles.svg
   :caption: Nested isosceles triangles B A_n C over fixed base BC = 2 with altitudes 1/n: pure rational apex spreads s_A = 4n^2/(n^2+1)^2 -> 0 and Triple Quad collinearity residual 16/n^2 -> 0.

* **Exact Rational Trigonometry Proof**:
  For :g:`B` :math:`= (-1, 0)`, :g:`C` :math:`= (1, 0)`, and apex :math:`A_n = (0, 1/n)` (:g:`A1`, :g:`A2`, :g:`A4`, :g:`A8` descending toward :g:`M`), :person:`Wildberger's <wildberger>` invariants belong purely to :math:`\mathbb{Q}(n)`: :math:`Q(A_n, B) = 1 + \frac{1}{n^2}`, :math:`s_B = s_C = \frac{1}{n^2+1} \to 0`, :math:`s_{A_n} = \frac{4n^2}{(n^2+1)^2} \to 0`, the **Triple Spread Formula** vanishes identically, and the **Triple Quad Formula** residual equals :math:`\frac{16}{n^2} \to 0`.

.. code-block:: python

   import sympy as sp
   from geometor.cusa import (
       compute_flattening_triangle_metrics,
       verify_triangle_line_coincidence,
   )

   m4 = compute_flattening_triangle_metrics(4)
   assert m4.spread_apex == sp.Rational(64, 289)
   assert m4.triple_quad_residual == sp.Integer(1)

   proof = verify_triangle_line_coincidence()
   assert proof["triple_spread_identity"] is True
   assert proof["limit_triple_quad"] == 0

----

3. Polygon Exhaustion (``I.3``) & *Scripta Mathematica* (``1445–1459``)
-----------------------------------------------------------------------

*Codex Reference*: :doc:`Liber I, Cap. I–IV (Notes) </de_docta_ignorantia/liber_i/cap_01_04/notes>` & :doc:`De Geometricis Transmutationibus (Notes) </de_mathematicis_complementis/transmutatio_1445/notes>` · *Script*: ``demos/polygon_exhaustion_and_complementa.py``

.. picture:: /_static/figures/cusa_transmutatio_1445.svg
   :caption: De Geometricis Transmutationibus (1445, §§9–11): quarter-side ray AE = sqrt(7)/4 extended in 5:4 sesquiquartal ratio to AH = 5*sqrt(7)/16, implying pi ~= 24*sqrt(21)/35 ~= 3.14233762.

.. picture:: /_static/figures/cusa_aurea_propositio_1459.svg
   :caption: Aurea Propositio in Mathematicis (1459, §§1–2) over Q(sqrt(3)) at theta = pi/6: balanced rectifying segment IKL satisfying |AI| + |AK| + |AL| = 3 and fifth-order Maclaurin accuracy theta^5/180.

* **Exact Symbolic Verification**:
  Verifies (a) monotone radical apothems :math:`r_n = \cos(\pi/n)` across :math:`n \in \{3, 4, 6, 8, 12\}`, (b) Cusa's 1445 *sesquiquartal* equilateral-triangle rectification :math:`\pi_{\text{Cusa},1445} = \frac{24\sqrt{21}}{35}`, and (c) Cusa's 1458–1459 three-ray law :math:`L_{\text{Cusa}}(\theta) = \frac{6\sin\theta}{2 + \cos\theta}` with exact Maclaurin series error :math:`\theta - \frac{3\sin\theta}{2+\cos\theta} = \frac{\theta^5}{180} + \frac{\theta^7}{1512} + \frac{\theta^9}{25920} + O(\theta^{11})`.

.. code-block:: python

   import sympy as sp
   from geometor.cusa import (
       verify_cusa_snellius_approximation,
       verify_transmutatio_1445,
   )

   tr = verify_transmutatio_1445()
   assert sp.simplify(tr["pi_cusa_1445"] - 24 * sp.sqrt(21) / 35) == 0

   au = verify_cusa_snellius_approximation()
   assert au["tangent_ratio_equal"] is True
   assert au["coeff_theta_5"] == sp.Rational(1, 180)

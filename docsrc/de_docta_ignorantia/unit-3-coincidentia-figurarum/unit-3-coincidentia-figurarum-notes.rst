:layout: book
:type: notes
:title: Unit III — Coincidence of Infinite Circle, Straight Line, Triangle & Sphere — Notes
:canonical_id: DI I.13–15 (1440)
:original_id: DI I.13–15 (1440)
:folio: DI I.13–15 (1440)

.. _unit-3-coincidentia-figurarum-notes:

=========================================================================================================
Unit III — Coincidence of Infinite Circle, Straight Line, Triangle & Sphere — Critical Commentary & Notes
=========================================================================================================

.. rubric:: Exact Symbolic Reconstruction, Latin Philology & Canon Reception · DI I.13–15 (1440)

.. picture:: /_static/figures/cusa_circle_line_pencil.svg
   :alt: Coincidence of Infinite Circle, Straight Line, Triangle & Sphere
   :caption: Book I, Chapter 13 — Tangent Circle Pencil C_1, C_2, C_4, C_8 at Origin O = (0, 0) Above Horizon Line AB (y = 0): Exact Radical Secant Sagittae at x = 1 Shrink as 1, 2 - sqrt(3), 4 - sqrt(15), 8 - 3 sqrt(7) -> 0 as Curvature Resolves into Rectitude.

.. picture:: /_static/figures/cusa_flattening_triangles.svg
   :alt: Book I, Chapter 14 — That the Infinite Line Is a Triangle
   :caption: Book I, Chapter 14 — Flattening Isosceles Triangles T_n with Fixed Base BC = 2 and Apex A_n = (0, 1/n): Exact Rational Trigonometry Spreads s_A = 4n^2/(n^2+1)^2 -> 0 and Triple Quad Residual 16/n^2 -> 0 as T_n Resolves into Line BC.

.. picture:: /_static/figures/cusa_mobius_inversion.svg
   :alt: Book I, Chapter 15 — That That Triangle Is a Circle and a Sphere
   :caption: Book I, Chapters 13 & 15 — Projective-Conformal Realization via Unit-Circle Inversion at Pole S = (0, -1): Every Tangent Circle C_R Maps to a Finite Rational Circle C'_R Converging Smoothly to C'_inf at (0, -1/2), Radius 1/2—Identical to the Inverted Tangent Line AB.

I. Exact Symbolic Demonstrations of `DI I.13–15`
------------------------------------------------

1. **Sagitta Asymptotics & Radical Secants (`DI I.13 §2`)**: Let :math:`C_R` be the circle of
   radius :math:`R > 0` with center :math:`O_R = (0, R)` tangent to the straight line :math:`AB`
   (:math:`y = 0`) at :math:`O = (0, 0)`, so :math:`x^2 + (y - R)^2 = R^2`. At fixed horizontal
   abscissa :math:`x \neq 0` (with :math:`|x| \le R`), the exact :term:`sagitta <sagitta>` is:

   .. math::

      h(x, R) = R - \sqrt{R^2 - x^2} = \frac{x^2}{R + \sqrt{R^2 - x^2}}.

   Along the secant :math:`x = 1` for :math:`R \in \{1, 2, 4, 8\}` (modeled in
   ``geometor.cusa.coincidentia_circle_line``), the exact symbolic heights are
   :math:`1`, :math:`2 - \sqrt{3} \approx 0.26795`, :math:`4 - \sqrt{15} \approx 0.12702`, and
   :math:`8 - 3\sqrt{7} \approx 0.06275`, with :math:`\lim_{R \to \infty} h(x, R) = 0`,
   :math:`\lim_{R \to \infty} R\,h(x, R) = \frac{x^2}{2}`, and curvature :math:`\kappa(R) =
   \frac{1}{R} \to 0`.

2. **Projective-Conformal Proof via Möbius Circle Inversion**: Under inversion in the unit circle
   :math:`\Omega` centered at :math:`S = (0, -1)` (which fixes the point of tangency :math:`O =
   (0, 0)`), every circle :math:`C_R` of radius :math:`R` maps to a **bounded rational circle**
   :math:`C'_R` with exact center and radius:

   .. math::

      M_R = \left(0,\; -\frac{R}{2R + 1}\right), \qquad
      \rho_R = \frac{R}{2R + 1}.

   Meanwhile, the straight horizon line :math:`y = 0` maps to the circle :math:`C'_\infty` with
   center :math:`(0, -\frac{1}{2})` and radius :math:`\frac{1}{2}`. Taking :math:`R \to \infty`
   on the Riemann sphere :math:`\widehat{\mathbb{C}}`, :math:`M_R \to (0, -\frac{1}{2})` and
   :math:`\rho_R \to \frac{1}{2}` smoothly in Hausdorff metric: **on the conformal sphere, the
   straight line literally IS the circle through the point at infinity** (:cite:`casey:sequel:1886`,
   :cite:`klein:elementary:1908`).

3. **Rational Trigonometry Proof of the Flattening Triangle (`DI I.14 §§2–3`)**: For the isosceles
   triangle :math:`T_n` with fixed base :math:`B = (-1, 0)`, :math:`C = (1, 0)` (:math:`Q_{\text{base}}
   = 4`) and apex :math:`A_n = (0, \frac{1}{n})` over :math:`\mathbb{Q}(n)` (modeled in
   ``geometor.cusa.coincidentia_triangle_line`` using :person:`Wildberger's <wildberger>`
   invariants, :cite:`wildberger:divine:2005`):

   .. math::

      Q(A_n, B) = Q(A_n, C) = 1 + \frac{1}{n^2} = \frac{n^2 + 1}{n^2}, \qquad
      s_B = s_C = \frac{1}{n^2 + 1}, \qquad
      s_{A_n} = \frac{4n^2}{(n^2 + 1)^2}.

   Every :math:`T_n` satisfies the **Triple Spread Formula** :math:`(s_{A_n} + 2s_B)^2 -
   2(s_{A_n}^2 + 2s_B^2) - 4 s_{A_n} s_B^2 = 0` identically over :math:`\mathbb{Q}(n)`, while the
   **Triple Quad Formula** collinearity residual equals :math:`(4 + 2Q_{\text{leg}})^2 - 2(16 +
   2Q_{\text{leg}}^2) = \frac{16}{n^2} \to 0` as :math:`n \to \infty`!

II. Archival Scan Collation: Rotta (1913) vs. Klibansky & Paris (1514)
----------------------------------------------------------------------

Direct multimodal inspection of McGill University Library's digitized scan of :person:`Raymond
Klibansky's <klibansky>` annotated copy of :person:`Paolo Rotta's <klibansky>` 1913 Laterza edition
(:cite:`cusa:rotta:1913`, pp. 28 and 31; cf. :cite:`cusa:heidelberg:1932`) revealed **two classic
scribal/typesetting eye-skip omissions (*homeoteleuton*) in Rotta's printed text**, both restored
in pencil in Klibansky's own hand from the 1514 Paris and manuscript witnesses and incorporated in
our Latin text:

- **`DI I.13 §2` (Rotta p. 28)**: Rotta's typesetter jumped from the first *minoris circuli* to the
  second, omitting ``et ille plus a curvitate recedit quam arcus gh adhuc minoris circuli``—even
  though Rotta's own marginal woodcut right beside the paragraph explicitly labels all four lines
  ``a b``, ``c d``, ``e f``, and ``g h``!
- **`DI I.14 §3` (Rotta p. 31)**: Rotta printed ``ut b d c, et superficies minor``, accidentally
  dropping ``tanto minus vincunt lineae bd et dc lineam bc`` between ``ut bdc`` and ``et
  superficies minor``—again restored in Klibansky's pencil margin at the foot of page 31.


IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions, Rational Trigonometry proofs, and series-error audits for **Unit III** live in ``src/geometor/cusa/`` and the companion walkthrough :doc:`/demos/index`.

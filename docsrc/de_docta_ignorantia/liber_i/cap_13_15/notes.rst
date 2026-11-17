:order: 30
:layout: book
:type: notes
:title: Coincidence of Infinite Circle, Straight Line, Triangle & Sphere — Notes
:canonical_id: DI I.13–15
:original_id: DI I.13–15
:folio: DI I.13–15 (1440)
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _cap_13_15-notes:
.. _unit-3-coincidentia-figurarum-notes:

==============================================================================================
Coincidence of Infinite Circle, Straight Line, Triangle & Sphere — Critical Commentary & Notes
==============================================================================================

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

I. Exact Symbolic Geometry of the Tangent Circle Pencil (`DI I.13`)
-------------------------------------------------------------------

Let circles :math:`C_R` of radius :math:`R > 0` be centered at :math:`(0, R)` tangent to line
:math:`y = 0` at the origin :math:`(0, 0)`. Along the vertical secant :math:`x = 1`:

.. math::

   h(1, R) = R - \sqrt{R^2 - 1} = \frac{1}{R + \sqrt{R^2 - 1}}.

Across the harmonic sequence :math:`R \in \{1, 2, 4, 8\}`:

- :math:`R = 1`: :math:`h = 1`
- :math:`R = 2`: :math:`h = 2 - \sqrt{3} \approx 0.267949`
- :math:`R = 4`: :math:`h = 4 - \sqrt{15} \approx 0.129171`
- :math:`R = 8`: :math:`h = 8 - 3\sqrt{7} \approx 0.062996`

In the limit :math:`R \to \infty`, :math:`h \to 0` and curvature :math:`\kappa = 1/R \to 0`.
Under unit-circle inversion at pole :math:`S = (0, -1)`, the unbounded tangent pencil maps to a
compact family of rational circles centered at :math:`\left(0, -\frac{R}{2R+1}\right)` with
radii :math:`\frac{R}{2R+1}`, whose limit circle at :math:`R \to \infty` is centered at
:math:`\left(0, -\frac{1}{2}\right)` with radius :math:`\frac{1}{2}`—the exact inverse of the
horizon line :math:`y = 0`.

II. Klibansky's Archival Restorations in Rotta (1913)
-----------------------------------------------------

Inspection of Raymond Klibansky's personal annotated copy of Rotta (1913) at McGill University
Library reveals two critical omissions restored in this digital edition:

- **`DI I.13 §2` (Rotta p. 28)**: Rotta jumped by homeoteleuton from the first occurrence of
  ``curvitate recedit`` to the second, omitting ``et ille plus a curvitate recedit quam arcus gh
  adhuc minoris circuli``.
- **`DI I.14 §3` (Rotta p. 31)**: Rotta printed ``ut b d c, et superficies minor``, accidentally
  dropping ``tanto minus vincunt lineae bd et dc lineam bc`` between ``ut bdc`` and ``et
  superficies minor``.


IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions, Rational Trigonometry proofs, and series-error audits for **Coincidence of Infinite Circle, Straight Line, Triangle & Sphere** live in ``src/geometor/cusa/`` and the companion walkthrough :doc:`/demos/index`.

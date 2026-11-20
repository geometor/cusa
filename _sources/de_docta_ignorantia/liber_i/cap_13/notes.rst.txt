:order: 80
:layout: book
:type: notes
:title: Properties of the Maximal Infinite Line: Curvature Resolves into Rectitude — Notes
:canonical_id: DI I.13
:original_id: DI I.13
:folio: DI I.13 (1440)
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _cap_13-notes:
.. _cap_13_15-notes:
.. _unit-3-coincidentia-figurarum-notes:

========================================================================================================
Properties of the Maximal Infinite Line: Curvature Resolves into Rectitude — Critical Commentary & Notes
========================================================================================================

.. rubric:: Exact Symbolic Reconstruction, Latin Philology & Canon Reception · DI I.13 (1440)

.. picture:: /_static/figures/cusa_circle_line_pencil.svg
   :alt: Properties of the Maximal Infinite Line: Curvature Resolves into Rectitude
   :caption: Book I, Chapter 13 — Tangent Circle Pencil C_1, C_2, C_4, C_8 at Origin O = (0, 0) Above Horizon Line AB (y = 0): Exact Radical Secant Sagittae at x = 1 Shrink as 1, 2 - sqrt(3), 4 - sqrt(15), 8 - 3 sqrt(7) -> 0 as Curvature Resolves into Rectitude.

I. Exact Symbolic Geometry of the Tangent Circle Pencil (`DI I.13`)
-------------------------------------------------------------------

Let circles :math:`C_R` of radius :math:`R > 0` be centered at :math:`(0, R)` tangent to line :math:`y = 0` at the origin :math:`(0, 0)`. Along the vertical secant :math:`x = 1`:

.. math::

   h(1, R) = R - \sqrt{R^2 - 1} = \frac{1}{R + \sqrt{R^2 - 1}}.

Across the harmonic sequence :math:`R \in \{1, 2, 4, 8\}`:

- :math:`R = 1`: :math:`h = 1`
- :math:`R = 2`: :math:`h = 2 - \sqrt{3} \approx 0.267949`
- :math:`R = 4`: :math:`h = 4 - \sqrt{15} \approx 0.129171`
- :math:`R = 8`: :math:`h = 8 - 3\sqrt{7} \approx 0.062996`

In the limit :math:`R \to \infty`, :math:`h \to 0` and curvature :math:`\kappa = 1/R \to 0`.

II. Klibansky's Archival Restoration in Rotta (1913)
----------------------------------------------------

- **`DI I.13 §2` (Rotta p. 28)**: Rotta jumped by homeoteleuton from the first occurrence of ``curvitate recedit`` to the second, omitting ``et ille plus a curvitate recedit quam arcus gh adhuc minoris circuli``; restored from Klibansky's annotated copy at McGill University Library.


IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions, Rational Trigonometry proofs, and series-error audits for **Properties of the Maximal Infinite Line: Curvature Resolves into Rectitude** live in ``src/geometor/cusa/`` and the companion walkthrough :doc:`/demos/index`.

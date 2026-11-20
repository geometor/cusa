:order: 40
:layout: book
:type: notes
:title: That Precise Truth Is Incomprehensible: Polygon Exhaustion & the Circle — Notes
:canonical_id: DI I.3
:original_id: DI I.3
:folio: DI I.3 (1440)
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _cap_03-notes:

=====================================================================================================
That Precise Truth Is Incomprehensible: Polygon Exhaustion & the Circle — Critical Commentary & Notes
=====================================================================================================

.. rubric:: Exact Symbolic Reconstruction, Latin Philology & Canon Reception · DI I.3 (1440)

.. picture:: /_static/figures/cusa_polygon_exhaustion.svg
   :alt: That Precise Truth Is Incomprehensible: Polygon Exhaustion & the Circle
   :caption: Book I, Chapter 3 — Inscribed Regular Polygons P_3, P_4, P_6, P_8, P_12 in Unit Circle C: Monotonically Increasing Apothem r_n = cos(pi/n) -> 1 Without Finite Identity Between Polygon and Circle.

I. Exact Symbolic Analysis of Polygon Exhaustion (`DI I.3`)
-----------------------------------------------------------

In `DI I.3 §2`, :person:`Nicholas of Cusa <cusanus>` elevates :person:`Archimedes' <archimedes>` method of exhaustion (:cite:`archimedes:dimensio`) into the foundational epistemological theorem of :term:`learned ignorance <docta-ignorantia>`. For a regular :math:`n`-gon inscribed in the unit circle :math:`x^2 + y^2 = 1`:

.. math::

   r_n = \cos\!\left(\frac{\pi}{n}\right), \qquad
   s_n = 1 - r_n = 2\sin^2\!\left(\frac{\pi}{2n}\right), \qquad
   P_n = 2n\sin\!\left(\frac{\pi}{n}\right).

Across the constructible tower :math:`n \in \{3, 4, 6, 8, 12\}` modeled in ``geometor.cusa.polygon_exhaustion_and_complementa``, every vertex, apothem, and sagitta lies in an exact nested quadratic radical field over :math:`\mathbb{Q}`:

- :math:`n = 3`: :math:`r_3 = \frac{1}{2}`, :math:`s_3 = \frac{1}{2}`, :math:`Q_{\text{side}} = 3`.
- :math:`n = 4`: :math:`r_4 = \frac{\sqrt{2}}{2}`, :math:`s_4 = 1 - \frac{\sqrt{2}}{2}`, :math:`Q_{\text{side}} = 2`.
- :math:`n = 6`: :math:`r_6 = \frac{\sqrt{3}}{2}`, :math:`s_6 = 1 - \frac{\sqrt{3}}{2}`, :math:`Q_{\text{side}} = 1`.
- :math:`n = 8`: :math:`r_8 = \frac{\sqrt{2+\sqrt{2}}}{2}`, :math:`s_8 = 1 - \frac{\sqrt{2+\sqrt{2}}}{2}`, :math:`Q_{\text{side}} = 2 - \sqrt{2}`.
- :math:`n = 12`: :math:`r_{12} = \frac{\sqrt{6}+\sqrt{2}}{4}`, :math:`s_{12} = 1 - \frac{\sqrt{6}+\sqrt{2}}{4}`, :math:`Q_{\text{side}} = 2 - \sqrt{3}`.

Because :math:`r_n < 1` strictly for every finite :math:`n`, the gap between polygon and circle never closes in the finite domain: discursive reason can multiply angles indefinitely without ever reaching identity with the curved continuum.


IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions, Rational Trigonometry proofs, and series-error audits for **That Precise Truth Is Incomprehensible: Polygon Exhaustion & the Circle** live in ``src/geometor/cusa/`` and the companion walkthrough :doc:`/demos/index`.

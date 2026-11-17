:order: 80
:layout: book
:type: notes
:title: De Geometricis Transmutationibus — Isoperimetric Extrema and the Sesquiquartal Radius — Notes
:canonical_id: DGT (1445)
:original_id: DGT (1445)
:folio: DGT (1445)
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _transmutatio_1445-notes:

===================================================================================================================
De Geometricis Transmutationibus — Isoperimetric Extrema and the Sesquiquartal Radius — Critical Commentary & Notes
===================================================================================================================

.. rubric:: Exact Symbolic Reconstruction, Latin Philology & Canon Reception · DGT (1445)

.. picture:: /_static/figures/cusa_transmutatio_1445.svg
   :alt: De Geometricis Transmutationibus — Isoperimetric Extrema and the Sesquiquartal Radius
   :caption: De Geometricis Transmutationibus (1445, §§9–11) — Equilateral Triangle B–C–D Inscribed in Unit Circle A with Quarter-Point E: Ray AE Extended in 5:4 Sesquiquartal Ratio to H Yields AH = 5*sqrt(7)/16.

.. picture:: /_static/figures/cusa_transmutatio_1445.svg
   :alt: De Geometricis Transmutationibus (1445, §§1–11) — To Paolo dal Pozzo Toscanelli: Isoperimetric Extrema and the Sesquiquartal Radius
   :caption: De Geometricis Transmutationibus (1445, §§9–11) — Inscribed Equilateral Triangle BCD in Unit Circle A: Quarter-Point E on Side BC Extended in Sesquiquartal Ratio 5:4 Yields Isoperimetric Radius AH = (5/16) sqrt(7), Implying pi ~= (24/35) sqrt(21) ~= 3.142337.

I. Exact Algebraic Audit of De Geometricis Transmutationibus (1445)
-------------------------------------------------------------------

In the unit circle :math:`R = 1` centered at :g:`A` at :math:`(0, 0)`, the inscribed equilateral
triangle :g:`B`–:g:`C`–:g:`D` has side :math:`|BC| = \sqrt{3}` and perimeter :math:`P_3 = 3\sqrt{3}`.
Dividing :math:`BC` into four equal segments at :g:`E`, :g:`F`, :g:`G`, the midpoint :g:`F` satisfies
:math:`Q(A, F) = \frac{1}{4}` and the quarter-point :g:`E` satisfies:

.. math::

   Q(A, E) = |AF|^2 + |FE|^2 = \frac{1}{4} + \left(\frac{\sqrt{3}}{4}\right)^2
   = \frac{7}{16} \implies |AE| = \frac{\sqrt{7}}{4}.

Extending :math:`AE` in :term:`sesquiquartal ratio <proportio-sesquiquarta>` :math:`5:4` gives
Cusa's isoperimetric radius :math:`|AH| = \frac{5\sqrt{7}}{16}` (:math:`Q(A, H) = \frac{175}{256}`),
implying:

.. math::

   \pi_{\text{Cusa},1445} = \frac{P_3}{2|AH|} = \frac{3\sqrt{3}}{5\sqrt{7}/8}
   = \frac{24\sqrt{21}}{35} \approx 3.14233762,

which exceeds true :math:`\pi \approx 3.14159265` by only :math:`+7.45 \times 10^{-4}` (lying
strictly inside :person:`Archimedes' <archimedes>` 96-gon bounds :math:`3\frac{10}{71} < \pi <
3\frac{1}{7}`, though :person:`Regiomontanus <regiomontanus>` later showed via tighter bounds
that :math:`\frac{24\sqrt{21}}{35} > \pi`; :cite:`regiomontanus:quadratura:1533`).


IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions, Rational Trigonometry proofs, and series-error audits for **De Geometricis Transmutationibus — Isoperimetric Extrema and the Sesquiquartal Radius** live in ``src/geometor/cusa/`` and the companion walkthrough :doc:`/demos/index`.

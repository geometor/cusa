:order: 90
:layout: book
:type: notes
:title: That the Infinite Line Is a Triangle: Flattening Triangle & Triple Quad Limit — Notes
:canonical_id: DI I.14
:original_id: DI I.14
:folio: DI I.14 (1440)
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _cap_14-notes:

===========================================================================================================
That the Infinite Line Is a Triangle: Flattening Triangle & Triple Quad Limit — Critical Commentary & Notes
===========================================================================================================

.. rubric:: Exact Symbolic Reconstruction, Latin Philology & Canon Reception · DI I.14 (1440)

.. picture:: /_static/figures/cusa_flattening_triangles.svg
   :alt: That the Infinite Line Is a Triangle: Flattening Triangle & Triple Quad Limit
   :caption: Book I, Chapter 14 — Fixed Base BC with Descending Apices A_n = (0, 1/n) for n = 1, 2, 4, 8: Apex Spread s_A = 4n^2/(n^2 + 1)^2 -> 0 and Triple Quad Residual 16/n^2 -> 0 as the Triangle Resolves into Line BC.

I. Exact Rational Trigonometry of Flattening Triangles (`DI I.14`)
------------------------------------------------------------------

In ``geometor.cusa.coincidentia_triangle_line``, fixed base :math:`B = (-1, 0)`, :math:`C = (1, 0)` (:math:`Q_{\text{base}} = 4`) and descending apices :math:`A_n = (0, 1/n)` satisfy :math:`Q_{\text{leg}} = 1 + 1/n^2`, apex spread :math:`s_A = \frac{4n^2}{(n^2 + 1)^2} \to 0`, and Triple Quad Formula residual :math:`(Q_1 + Q_2 + Q_3)^2 - 2(Q_1^2 + Q_2^2 + Q_3^2) = \frac{16}{n^2} \to 0`.

II. Klibansky's Archival Restoration in Rotta (1913)
----------------------------------------------------

- **`DI I.14 §3` (Rotta p. 31)**: Rotta printed ``ut b d c, et superficies minor``, accidentally dropping ``tanto minus vincunt lineae bd et dc lineam bc`` between ``ut bdc`` and ``et superficies minor``; restored from Klibansky's McGill collation.


IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions, Rational Trigonometry proofs, and series-error audits for **That the Infinite Line Is a Triangle: Flattening Triangle & Triple Quad Limit** live in ``src/geometor/cusa/`` and the companion walkthrough :doc:`/demos/index`.

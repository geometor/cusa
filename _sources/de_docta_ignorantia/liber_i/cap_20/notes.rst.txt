:order: 150
:layout: book
:type: notes
:title: Why a Quaternity or More Is Impossible: Minimal Polygon Theorem — Notes
:canonical_id: DI I.20
:original_id: DI I.20
:folio: DI I.20 (1440)
:tracks: English: index | Latin: la | Summary: summary | Notes: notes

.. _cap_20-notes:

=============================================================================================
Why a Quaternity or More Is Impossible: Minimal Polygon Theorem — Critical Commentary & Notes
=============================================================================================

.. rubric:: Exact Symbolic Reconstruction, Latin Philology & Canon Reception · DI I.20 (1440)

I. Why the Maximum Is Triune and Not Quaternary (`DI I.20`)
-----------------------------------------------------------

`Capitulum XX` supplies a purely topological-combinatorial proof of why polygonal resolution halts at three: in two-dimensional simplicial decomposition, the triangle (:math:`n = 3`) is the unique minimal polygon (*minima figura polygonia, qua minor esse nequit*). Every :math:`k`-gon for :math:`k \ge 4` decomposes into :math:`k - 2` triangles (cf. :person:`Euclid <euclid>` *Elements* I.32 and VI.20) and is therefore composite and strictly greater than the minimal polygon; hence a quadrangle cannot coincide with the simplest :term:`Minimum <minimum>` or serve as the universal measure of triangles. Moreover, Cusa enumerates the exact four-element dimensional basis of spatial measurement:

- **1D Length**: :term:`Maximal Infinite Line <linea-infinita>`
- **2D Rectilinear Breadth**: :term:`Maximal Triangle <triangulus-infinitus>`
- **2D Circular Breadth**: :term:`Maximal Circle <circulus-infinitus>`
- **3D Depth**: :term:`Maximal Sphere <sphaera-infinita>`


IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions, Rational Trigonometry proofs, and series-error audits for **Why a Quaternity or More Is Impossible: Minimal Polygon Theorem** live in ``src/geometor/cusa/`` and the companion walkthrough :doc:`/demos/index`.

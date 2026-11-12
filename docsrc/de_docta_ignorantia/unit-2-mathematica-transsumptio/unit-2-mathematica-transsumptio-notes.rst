:layout: book
:type: notes
:title: Unit II — Incorruptible Certitude & the Three-Step Method of Mathematical Transsumption — Notes
:canonical_id: DI I.11–12 (1440)
:original_id: DI I.11–12 (1440)
:folio: DI I.11–12 (1440)

.. _unit-2-mathematica-transsumptio-notes:

=====================================================================================================================
Unit II — Incorruptible Certitude & the Three-Step Method of Mathematical Transsumption — Critical Commentary & Notes
=====================================================================================================================

.. rubric:: Exact Symbolic Reconstruction, Latin Philology & Canon Reception · DI I.11–12 (1440)

.. picture:: /_static/figures/cusa_transsumptio_ascent.svg
   :alt: Incorruptible Certitude & the Three-Step Method of Mathematical Transsumption
   :caption: Book I, Chapters 11–12 — Three-Tier Epistemological Ascent of Transsumptio: (I) Finite Figures in Ratio -> (II) Coincident Infinite Limit in Intellectus -> (III) Transsumption to the Figure-Free Simple Infinite.

I. Epistemological Structure of *Transsumptio* (`DI I.11–12`)
-------------------------------------------------------------

Why does :person:`Nicholas of Cusa <cusanus>` privilege geometry over every sensible or verbal
analogy for divine science? In `DI I.11 §2`, Cusa locates :term:`mathematicalia <mathematicalia>`
at the exact epistemological fulcrum between material instability and pure intellectual simplicity:

1. **Incorruptible Certitude**: Sensible things waver continually because material possibility
   abounds in them, whereas mathematical figures—constructed by the mind itself—are *nobis
   certissima* ("most certain to us").
2. **Refutation of Atomism (`DI I.11 §3`)**: Echoing :person:`Aristotle's <aristotle>` *Physics* VI
   and the Pythagorean discovery of the incommensurability of the square's diagonal, Cusa notes
   that mathematical demonstration alone refutes Epicurus's indivisible magnitude-atoms: if a
   unit square were composed of :math:`N` indivisible atoms per side, its diagonal would require
   :math:`N\sqrt{2}` atoms, contradicting integer indivisibility.
3. **The Three-Tier Operator (`DI I.12 §1`)**: Let :math:`\mathcal{F}_R` denote a one-parameter
   family of finite geometric figures indexed by scale parameter :math:`R \in \mathbb{Q}_{>0}`,
   and let :math:`\mathcal{I}(\mathcal{F}_R)` be an algebraic invariant (such as curvature,
   sagitta, or vertex spread):

   - **Step 1 (*Consideratio finitorum*)**: Compute :math:`\mathcal{I}(\mathcal{F}_R)` exactly
     over :math:`\mathbb{Q}` or radical extensions for finite :math:`R`.
   - **Step 2 (*Translatio ad infinitum*)**: Evaluate :math:`\lim_{R \to \infty}
     \mathcal{I}(\mathcal{F}_R)` in intellectual vision, revealing the coincidence of properties
     that were strictly incompatible for every finite :math:`R`.
   - **Step 3 (*Transsumptio ad simplex absolutum*)**: Transfer that coincidence beyond spatial
     extension altogether to the figure-free :term:`Absolute Maximum <maximum-absolutum>`.

II. Historical & Textual Context
--------------------------------

- **Patristic & Twelfth-Century Antecedents (`DI I.12 §2`)**: Cusa synthesizes four classic
  theological symbols: (i) :person:`Anselm of Canterbury's <anselm>` *De Veritate* on supreme truth
  as *rectitudo*; (ii) pseudo-Hermetic and Chartrian formulas from the twelfth-century *Liber XXIV
  philosophorum* ("Deus est sphaera infinita cuius centrum est ubique, circumferentia nusquam");
  (iii) :person:`Boethius <boethius>` (*De Institutione Arithmetica* I.1–2) on multitude and
  magnitude; and (iv) :person:`Augustine's <augustine>` *De quantitate animae*, which ascends from
  point, line, triangle, and circle to the incorporeal soul.
- **Kepler's Tribute**: In Chapter II of *Mysterium Cosmographicum* (:cite:`kepler:mysterium:1596`),
  :person:`Johannes Kepler <kepler>` hailed Cusa (*divinus mihi Cusanus*) specifically for this
  transsumptive correlation of the curved and the straight as the supreme mathematical emblem of
  Creator and creature.


IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions, Rational Trigonometry proofs, and series-error audits for **Unit II** live in ``src/geometor/cusa/`` and the companion walkthrough :doc:`/demos/index`.

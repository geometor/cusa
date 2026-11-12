:layout: book
:type: notes
:title: Unit I — Learned Ignorance, Polygon Exhaustion & the Coincidence of Maximum and Minimum — Notes
:canonical_id: DI Ded., I.1–4, Ep. (1440)
:original_id: DI Ded., I.1–4, Ep. (1440)
:folio: DI Ded., I.1–4, Ep. (1440)

.. _unit-1-maximum-ignorantia-notes:

=====================================================================================================================
Unit I — Learned Ignorance, Polygon Exhaustion & the Coincidence of Maximum and Minimum — Critical Commentary & Notes
=====================================================================================================================

.. rubric:: Exact Symbolic Reconstruction, Latin Philology & Canon Reception · DI Ded., I.1–4, Ep. (1440)

.. picture:: /_static/figures/cusa_polygon_exhaustion.svg
   :alt: Learned Ignorance, Polygon Exhaustion & the Coincidence of Maximum and Minimum
   :caption: Book I, Chapter 3 — Inscribed Regular Polygons P_3, P_4, P_6, P_8, P_12 in Unit Circle C: Monotonically Increasing Apothem r_n = cos(pi/n) -> 1 Without Finite Identity Between Polygon and Circle.

I. Exact Symbolic Analysis of Polygon Exhaustion (`DI I.3`)
-----------------------------------------------------------

In `DI I.3 §2`, :person:`Nicholas of Cusa <cusanus>` elevates :person:`Archimedes' <archimedes>`
method of exhaustion (:cite:`archimedes:dimensio`) into the foundational epistemological theorem of
:term:`learned ignorance <docta-ignorantia>`. For a regular :math:`n`-gon inscribed in the unit
circle :math:`x^2 + y^2 = 1`:

.. math::

   r_n = \cos\!\left(\frac{\pi}{n}\right), \qquad
   s_n = 1 - r_n = 2\sin^2\!\left(\frac{\pi}{2n}\right), \qquad
   P_n = 2n\sin\!\left(\frac{\pi}{n}\right).

Across the constructible tower :math:`n \in \{3, 4, 6, 8, 12\}` modeled in
``geometor.cusa.polygon_exhaustion_and_complementa``, every vertex, apothem, and sagitta lies in
an exact nested quadratic radical field over :math:`\mathbb{Q}`:

- :math:`n = 3`: :math:`r_3 = \frac{1}{2}`, :math:`s_3 = \frac{1}{2}`, :math:`Q_{\text{side}} = 3`.
- :math:`n = 4`: :math:`r_4 = \frac{\sqrt{2}}{2}`, :math:`s_4 = 1 - \frac{\sqrt{2}}{2}`,
  :math:`Q_{\text{side}} = 2`.
- :math:`n = 6`: :math:`r_6 = \frac{\sqrt{3}}{2}`, :math:`s_6 = 1 - \frac{\sqrt{3}}{2}`,
  :math:`Q_{\text{side}} = 1`.
- :math:`n = 8`: :math:`r_8 = \frac{\sqrt{2 + \sqrt{2}}}{2}`, :math:`Q_{\text{side}} = 2 - \sqrt{2}`.
- :math:`n = 12`: :math:`r_{12} = \frac{\sqrt{6} + \sqrt{2}}{4}`, :math:`Q_{\text{side}} = 2 - \sqrt{3}`.

Crucially, Cusa distinguishes **metric convergence** (:math:`s_n \to 0`, :math:`P_n \to 2\pi`)
from **ontological-definitional identity**: for every finite :math:`n \in \mathbb{N}`, the
polygon remains piecewise-rectilinear with :math:`n` discrete vertices where curvature is
concentrated, whereas the circle's being consists in uniform, indivisible equidistance from its
center. Finite :term:`reason <ratio-et-intellectus>` moves endlessly along the sequence :math:`n
\mapsto 2n`; only :term:`intellectus <ratio-et-intellectus>` grasps the limit where polygon
resolves into circle.

II. Latin Philology & Textual Witnesses
---------------------------------------

- **Title & Socratic-Aristotelian Synthesis (`DI I.1 §2`)**: Cusa weaves together :person:`Socrates'
  <socrates>` *Apology* (`21d`), Ecclesiastes `1:8`, Job `28:20–21`, and :person:`Aristotle's
  <aristotle>` night-owl simile (*Metaphysics* II.1, `993b9–11`, Latin *nocticorax*). Our archival
  inspection of :person:`Paolo Rotta's <klibansky>` 1913 edition (:cite:`cusa:rotta:1913`, p. 4)
  confirms the spelling *nocticoraci* alongside Rotta's apparatus notes to Bonaventure and Dante.
- **Anselmian Formula Transposed (`DI I.2 §1` & `I.4 §§1–2`)**: Cusa adopts :person:`Anselm's
  <anselm>` *Proslogion* definition (*quo nihil maius cogitari / esse potest*) but immediately
  pairs it with its symmetric superlative twin, *quo minus esse non potest* (:term:`minimum
  <minimum>`). Subtracting quantitative contraction (*subtrahendo intellectualiter magnum et
  parvum*), both superlatives coincide in :term:`absolute maximality <maximum-absolutum>`.
- **The Sea-Voyage Colophon (`DI Ep.`)**: Returning from Constantinople with the Byzantine
  delegation to the Council of Ferrara–Florence between November 27, 1437 and February 8, 1438,
  Cusa received the governing intuition of *incomprehensibilia incomprehensibiliter amplecti* and
  signed the completed codex in his native Kues (*Complevi in Cusa 1440, XII. februarii*).

III. Reception in the GEOMETOR Canon
------------------------------------

Cusa's contrast between comparative *ratio* and transcendent *intellectus* transforms
:person:`Plato's <plato>` Divided Line (*Republic* VI, `509d–511e`; :cite:`plato:opera`),
:person:`Proclus's <proclus>` theory of mathematical projection in the imagination
(:cite:`proclus:in-euclidem`), and :person:`Thomas Aquinas's <aquinas>` doctrine of *materia
intelligibilis* and *judicium* (:cite:`aquinas:boethius`), anticipating :person:`Petrus Hoenen's
<hoenen>` *De Noetica Geometriae* (:cite:`hoenen:noetica:1954`).


IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions, Rational Trigonometry proofs, and series-error audits for **Unit I** live in ``src/geometor/cusa/`` and the companion walkthrough :doc:`/demos/index`.

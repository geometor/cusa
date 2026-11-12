"""Scholarly structural summaries and critical notes for the five units of GEOMETOR • cusa."""

from __future__ import annotations

UNIT_SUMMARIES: dict[str, str] = {
    "unit-1-maximum-ignorantia": """\
I. Argumentative Synopsis
-------------------------

1. **Dedicatory Prologue (`DI Ded.`)**: Addressing his Paduan teacher :person:`Cardinal Julian
   Cesarini <cesarini>`, :person:`Nicholas of Cusa <cusanus>` echoes :person:`Aristotle's <aristotle>`
   dictum in *Metaphysics* I.2 that philosophical inquiry begins in wonder (*admiratio*), framing
   the paradoxical title :term:`De Docta Ignorantia <docta-ignorantia>` as an intellectual hunger
   through which the mind perfects its own nature.
2. **Comparative Proportion & the Inaccessibility of the Infinite (`DI I.1`)**: Every discursive
   investigation judges the unknown through comparative :term:`proportion <proportio>` to something
   already presupposed as certain, just as later geometric theorems reduce through chains of media
   to first axioms. Because proportion requires agreement and difference articulated by number, and
   the infinite escapes every finite ratio (*infiniti ad finitum proportio non est*), the infinite
   qua infinite remains unknowable to comparative :term:`reason <ratio-et-intellectus>`. Like
   :person:`Socrates <socrates>` and :person:`Aristotle's <aristotle>` night-owl before the sun,
   human wisdom culminates in knowing its own ignorance.
3. **Threefold Architecture of the Maximum (`DI I.2`)**: Cusa defines the :term:`Maximum <maximum-absolutum>`
   in :person:`Anselmian <anselm>` terms as *quo nihil maius esse potest* and outlines the three
   books of the treatise: Book I investigates the Absolute Maximum (God); Book II investigates the
   contracted universal maximum (the cosmos existing solely in plurality through :term:`contraction
   <contractio>`); Book III investigates the maximum at once contracted and absolute.
4. **Polygon Exhaustion & Ungraspable Precision (`DI I.3`)**: Among finite things equality is always
   gradual; between measure and measured an irreducible gap remains. Hence the finite intellect
   stands to truth as an inscribed :term:`polygon <polygonia>` stands to a circle: multiplying the
   angles increases likeness indefinitely without ever producing identity unless the polygon
   resolves itself into the circle.
5. **Coincidence of Maximum and Minimum (`DI I.4`) & Sea-Voyage Colophon (`DI Ep.`)**: Because the
   Absolute Maximum admits neither exceeding nor exceeded, nothing can oppose it; stripped of
   quantitative contraction into "large" and "small," superlative :term:`Maximum <maximum-absolutum>`
   and superlative :term:`Minimum <minimum>` coincide (:term:`coincidentia oppositorum
   <coincidentia-oppositorum>`). The concluding letter records Cusa's illumination at sea returning
   from Constantinople (winter 1437/1438) and dates completion at Kues to **February 12, 1440**.

II. Interactive Diagram Guide (`cusa_polygon_exhaustion.svg`)
-------------------------------------------------------------

- Center :g:`O` at :math:`(0, 0)` and unit circle around :g:`H1` represent indivisible circular truth.
- Regular inscribed polygons for :math:`n = 3, 4, 6, 12` (:g:`H1`–:g:`H3`–:g:`H5`, square vertices
  :g:`S2` and :g:`S4`, hexagon :g:`H1`–:g:`H2`–:g:`H3`–:g:`H4`–:g:`H5`–:g:`H6`, and dodecagon
  mid-arc vertices :g:`W1`, :g:`W2`, :g:`W3`, :g:`W4` with triangle apothem midpoint :g:`F`)
  illustrate how the apothem (*prima linea*) :math:`r_n = \\cos(\\pi/n)` climbs strictly from
  :eq:`r_3 = 1/2` through :eq:`r_4 = \\sqrt{2}/2`, :eq:`r_6 = \\sqrt{3}/2`, and
  :eq:`r_{12} = (\\sqrt{6}+\\sqrt{2})/4` toward :math:`1` without attaining circular curvature at
  any finite :math:`n`.
""",
    "unit-2-mathematica-transsumptio": """\
I. Argumentative Synopsis
-------------------------

1. **Ontological Status of Mathematical Entities (`DI I.11`)**: Visible things are symbolic mirrors
   of invisible realities (1 Cor. 13:12), yet sensible bodies fluctuate continually owing to
   material possibility. :term:`Mathematical entities <mathematicalia>`, abstracted from sensible
   flux while retaining imaginable figure, possess incorruptible stability and certainty. Cusa
   marshals an unbroken canon—:person:`Pythagoras <pythagoras>`, :person:`Plato <plato>`,
   :person:`Aristotle <aristotle>` ("as the triangle is in the quadrangle, so the lower form is in
   the higher," *De Anima* II.3, `414b29`), :person:`Augustine <augustine>`, and
   :person:`Boethius <boethius>`—culminating in the mathematical refutation of Epicurean indivisible
   atoms via geometric divisibility.
2. **The Three-Step Method of Transsumption (`DI I.12`)**: Since every imaginable figure is finite
   whereas the Absolute Maximum is figure-free, simple analogy fails; one must "leap beyond simple
   likeness" (*simplicem similitudinem transilire*) through a rigorous three-tier :term:`transsumption
   <transsumptio>`:

   - **Step 1 (Finite Ratio)**: Examine finite geometric figures together with their exact metric
     properties and ratios (*passiones et rationes*).
   - **Step 2 (Infinite Limit in Intellectus)**: Transfer those ratios correspondingly to infinite
     figures of the same kind, where finite oppositions collapse into identity.
   - **Step 3 (Transsumptive Leap)**: Transsume the intelligible ratios of those infinite figures
     still higher to the Simple Infinite wholly absolved from every figure whatsoever.

3. **Unifying the Patristic & Medieval Geometric Symbols (`DI I.12 §2`)**: Cusa announces that
   :person:`Anselm's <anselm>` infinite rectitude, the infinite right-angled triangle, the infinite
   circle, and the infinite sphere are not competing metaphors but mathematically identical in the
   infinite limit.

II. Interactive Diagram Guide (`cusa_transsumptio_ascent.svg`)
--------------------------------------------------------------

- **Step 1 (Finite Ratio)**: Finite chord :g:`B`–:g:`H`–:g:`C` and circles centered at :g:`O1` and
  :g:`O2` through contact vertex :g:`D` remain mutually distinct under finite
  :term:`ratio <ratio-et-intellectus>`.
- **Step 2 (Infinite Limit)**: Tangent horizon :g:`E`–:g:`D`–:g:`G` absorbs expanding circles into
  coincident rectitude under :term:`intellectus <ratio-et-intellectus>`.
- **Step 3 (Transsumptive Axis)**: Upper transcendent axis :g:`P`–:g:`Q` marks the leap beyond
  every spatial figure.
""",
    "unit-3-coincidentia-figurarum": """\
I. Argumentative Synopsis
-------------------------

1. **Coincidence of Infinite Circle and Straight Line (`DI I.13 §§1–2`)**: A circle's circumference
   is less curved in proportion as its diameter is larger. In the tangent family along straight
   line :g:`A`–:g:`B`, arc *cd* of a larger circle recedes further from :term:`curvature
   <curvitas-et-rectitudo>` than arc *ef* of a smaller circle, and *ef* further than arc *gh* of a
   still smaller circle. Hence the circumference of the :term:`maximal circle <circulus-infinitus>`,
   which cannot be greater, is minimally curved and therefore maximally straight: curvature and
   rectitude coincide.
2. **Potency of the Finite Line & Actual Infinity (`DI I.13 §§3–5`)**: Swinging finite segment *ab*
   about fixed endpoint *a* to *c* generates a triangle; completing the revolution generates a
   circle; swinging to opposite endpoint *d* forms diameter *bd* and a semicircle; revolving that
   semicircle about *bd* generates a sphere—the ultimate figure in the potency of the line. Because
   the :term:`infinite line <linea-infinita>` is in act everything that the finite line is in
   potency, it is simultaneously straight line, triangle, circle, and sphere.
3. **Coincidence of Infinite Triangle and Straight Line (`DI I.14`)**: Two independent proofs
   demonstrate that the infinite line is the :term:`maximal triangle <triangulus-infinitus>`:
   (a) *Metric-cardinal proof*: By the triangle inequality (:person:`Euclid <euclid>` *Elements*
   I.20), if one side is infinite, the other two cannot be smaller; since every part of the
   infinite is infinite and there cannot be multiple distinct infinites, the three infinite sides
   are one simple line. (b) *Quantitative limit proof*: By *Elements* I.32, the three angles sum to
   two right angles; as the apex angle (*bac* -> *bdc*) approaches two right angles while base *bc*
   stays fixed, the side excess :math:`(|BD| + |DC|) - |BC|` and enclosed area vanish until the
   triangle resolves into a single line.
4. **Coincidence with Infinite Circle and Sphere (`DI I.15`)**: Swinging infinite radius *ab*
   generates infinite arc *bc*, which is both straight and—since a part of the infinite equals the
   whole—the complete circumference; its return upon itself completes the revolution into the
   :term:`infinite sphere <sphaera-infinita>`.

II. Interactive Diagram Guide
-----------------------------

- **`cusa_circle_line_pencil.svg`**: Tangent circles centered at :g:`C1`, :g:`C2`, and higher radii
  share common tangent :g:`A`–:g:`B` at :g:`O`; along vertical secants through :g:`X` and :g:`W`,
  exact radical sagittae at :g:`P1`, :g:`P2`, :g:`P4`, :g:`P8` (and symmetric :g:`Q1`–:g:`Q8`)
  converge monotonically toward :g:`X`.
- **`cusa_flattening_triangles.svg`**: Fixed base :g:`B`–:g:`C` with flattening apices :g:`A1`,
  :g:`A2`, :g:`A4`, :g:`A8` descending to midpoint :g:`M`.
- **`cusa_mobius_inversion.svg`**: Conformal inversion in unit circle centered at pole :g:`S` maps
  the tangent pencil to finite rational circles centered at :g:`M1`, :g:`M2`, :g:`M4` converging to
  the inverted horizon circle centered at :g:`Minf`.
""",
    "unit-4-linea-sphaera-infinita": """\
I. Argumentative Synopsis
-------------------------

1. **The Infinite Line as Essence & Most Adequate Measure (`DI I.16–17`)**: Translating `I.13–15` to
   metaphysics (with explicit appeals to :person:`Pseudo-Dionysius <dionysius>` and Maimonides),
   Cusa shows that just as an infinite line composed of one-foot segments equals one composed of
   two-foot segments, the Infinite Essence is the sole exact :term:`measure <mensura>` (*adaequatissima
   mensura*) of all finite essences—neither larger (because Minimum) nor smaller (because Maximum).
   Finite lines are divisible in magnitude yet indivisible in the intelligible ratio of "line";
   the infinite line is whole in every finite line without being contracted to any one of them.
2. **Immediate vs. Mediate Participation (`DI I.18`)**: Finite straight lines participate in
   infinite rectitude more immediately (analogous to substances, which do not admit of more and
   less in their substantial ratio), whereas curves participate mediately through rectitude in
   varying degrees (analogous to accidents). Above both stands the *supersubstantial* Maximum.
3. **Triunity & the Exclusion of Quaternity (`DI I.19–20`)**: Because the maximal line is the
   maximal triangle without numerical multiplication ("when you begin to count the Trinity, you
   step outside the truth," :person:`Augustine <augustine>`), distinction and indistinction
   coincide in the :term:`Unitrine <unitrinum>` principle. Crucially, `I.20` proves geometrically
   why divine reality cannot be quaternary or higher: the triangle is the minimal polygon into
   which all polygons resolve, whereas a quadrangle is composite and larger than the minimal, so it
   cannot coincide with the simplest Maximum or measure triangles adequately.
4. **Circular Theology, Providence & the Infinite Sphere (`DI I.21–23`)**: In the :term:`infinite
   circle <circulus-infinitus>` (`I.21`), center (efficient cause), diameter (formal cause), and
   circumference (final cause) are identical, grounding a "circular theology" in which divine
   attributes verify one another reciprocally. In `I.22`, divine providence :term:`enfolds
   <complicatio-et-explicatio>` actuals, unactualized possibles, and contraries eternally without
   abrogating contingency. In `I.23`, length, breadth, and depth concur identically in the center
   of the :term:`infinite sphere <sphaera-infinita>`—pure actuality and maximal rest measuring all
   cosmic motions.

II. Interactive Diagram Guide (`cusa_line_unfolding_sphere.svg`)
----------------------------------------------------------------

- Fixed pivot :g:`A` at :math:`(0, 0)` and generating segment :g:`A`–:g:`B` unfold rotationally to
  sector vertex :g:`C` (triangle), antipodal point :g:`D` (diameter :g:`B`–:g:`D` and semicircle),
  and orthogonal meridian circles representing the sphere in three-space.
""",
    "unit-5-cosmologia-complementa": """\
I. Argumentative Synopsis
-------------------------

1. **Relativity of Motion & the Noble Moving Earth (`DI II.11–12`, 1440)**: Because no unqualified
   minimum of motion or exact physical equidistance can exist in the contracted universe, neither
   the earth nor any celestial body can occupy a fixed cosmic center, nor do fixed celestial poles
   exist (`II.11`). Like a passenger on a ship in midstream unable to see the riverbanks (`II.12
   §1`), every observer—whether on earth, the sun, the moon, or Mars—judges himself to stand at a
   motionless center. Thus the :term:`fabric of the world <machina-mundi>` exists *quasi habens
   undique centrum et nullibi circumferentiam*, and the moving earth is rehabilitated from medieval
   baseness as a *stella nobilis*.
2. **Isoperimetric Extrema & Sesquiquartal Radius (`De Geometricis Transmutationibus`, 1445)**:
   Dedicated to :person:`Paolo dal Pozzo Toscanelli <toscanelli>`, Cusa frames curve-straight
   :term:`rectification <quadratura-et-rectilineatio>` via :term:`isoperimetric <isoperimetra>`
   regular polygons: the equilateral triangle has minimal capacity and maximal gap between inradius
   and circumradius, whereas the circle has maximal capacity where both radii coincide. Dividing
   side :math:`BC` of an inscribed equilateral triangle into quarters at :math:`E, F, G` and
   extending :math:`AE` in :term:`sesquiquartal ratio <proportio-sesquiquarta>` :math:`5:4` yields
   :math:`AH = \\frac{5\\sqrt{7}}{16}`, equivalent to :math:`\\pi \\approx \\frac{24\\sqrt{21}}{35}
   \\approx 3.142337`.
3. **Critique of Archimedes' Spiral & Prima/Secunda Linea (`De Mathematicis Complementis`, 1453)**:
   Thanking :person:`Pope Nicholas V <nicholas-v>` for Jacobus Cremonensis's Latin translation of
   :person:`Archimedes <archimedes>`, Cusa diagnoses why *On Spirals* is kinematically circular for
   constructing :math:`\\pi`, defines the :term:`first line <prima-et-secunda-linea>` (inradius) and
   *second line* (circumradius), and proves geometrically (`§10`) that polygon area equals
   inradius times semiperimeter.
4. **Visio Intellectualis & the Cusa–Snellius Law (`De Mathematica Perfectione`, 1458)**: Writing
   to :person:`Cardinal Antonio Cerdà <cerda>`, Cusa invokes intellectual vision of the vanishing
   :term:`sagitta <sagitta>` where minimal chord and minimal arc coincide, deriving for right
   triangle :math:`abc` the celebrated law :math:`\\theta / \\sin\\theta \\approx 3R / (2R + R\\cos\\theta)`.
5. **Three-Ray Sum Invariance (`Aurea Propositio in Mathematicis`, August 8, 1459)**: Cusa's final
   mathematical gem reformulates his 1458 law as a symmetric three-ray conservation principle: when
   circular arc *bdc* is rectified into perpendicular segment *ikl*, the outward ascent of
   endpoints *i, l* balances the inward descent of midpoint *k* so that :math:`|AI| + |AK| + |AL|
   = 3R`—yielding :math:`L_{\\text{Cusa}}(\\theta) = \\frac{6R\\sin\\theta}{2 + \\cos\\theta}` with
   fifth-order Maclaurin accuracy :math:`\\frac{\\theta^5}{180}`.

II. Interactive Diagram Guide
-----------------------------

- **`cusa_cosmic_relativity.svg`**: Symmetric observer horizons around :g:`T` (Terra), :g:`S`
  (Sol), :g:`L` (Luna), and :g:`P` (Polus).
- **`cusa_transmutatio_1445.svg`**: Unit circle about :g:`A`, equilateral triangle :g:`B`–:g:`C`–:g:`D`,
  quarter-point :g:`E`, and sesquiquartal radius :g:`H`.
- **`cusa_aurea_propositio_1459.svg`**: Exact :math:`\\mathbb{Q}(\\sqrt{3})` sector (:math:`\\theta =
  \\pi/6`) showing chord :g:`B`–:g:`H`–:g:`C`, arc midpoint :g:`D`, tangent :g:`E`–:g:`D`–:g:`G`,
  and Cusa's balanced rectifying segment :g:`I`–:g:`K`–:g:`L`.
""",
}


UNIT_NOTES: dict[str, str] = {
    "unit-1-maximum-ignorantia": """\
I. Exact Symbolic Analysis of Polygon Exhaustion (`DI I.3`)
-----------------------------------------------------------

In `DI I.3 §2`, :person:`Nicholas of Cusa <cusanus>` elevates :person:`Archimedes' <archimedes>`
method of exhaustion (:cite:`archimedes:dimensio`) into the foundational epistemological theorem of
:term:`learned ignorance <docta-ignorantia>`. For a regular :math:`n`-gon inscribed in the unit
circle :math:`x^2 + y^2 = 1`:

.. math::

   r_n = \\cos\\!\\left(\\frac{\\pi}{n}\\right), \\qquad
   s_n = 1 - r_n = 2\\sin^2\\!\\left(\\frac{\\pi}{2n}\\right), \\qquad
   P_n = 2n\\sin\\!\\left(\\frac{\\pi}{n}\\right).

Across the constructible tower :math:`n \\in \\{3, 4, 6, 8, 12\\}` modeled in
``geometor.cusa.polygon_exhaustion_and_complementa``, every vertex, apothem, and sagitta lies in
an exact nested quadratic radical field over :math:`\\mathbb{Q}`:

- :math:`n = 3`: :math:`r_3 = \\frac{1}{2}`, :math:`s_3 = \\frac{1}{2}`, :math:`Q_{\\text{side}} = 3`.
- :math:`n = 4`: :math:`r_4 = \\frac{\\sqrt{2}}{2}`, :math:`s_4 = 1 - \\frac{\\sqrt{2}}{2}`,
  :math:`Q_{\\text{side}} = 2`.
- :math:`n = 6`: :math:`r_6 = \\frac{\\sqrt{3}}{2}`, :math:`s_6 = 1 - \\frac{\\sqrt{3}}{2}`,
  :math:`Q_{\\text{side}} = 1`.
- :math:`n = 8`: :math:`r_8 = \\frac{\\sqrt{2 + \\sqrt{2}}}{2}`, :math:`Q_{\\text{side}} = 2 - \\sqrt{2}`.
- :math:`n = 12`: :math:`r_{12} = \\frac{\\sqrt{6} + \\sqrt{2}}{4}`, :math:`Q_{\\text{side}} = 2 - \\sqrt{3}`.

Crucially, Cusa distinguishes **metric convergence** (:math:`s_n \\to 0`, :math:`P_n \\to 2\\pi`)
from **ontological-definitional identity**: for every finite :math:`n \\in \\mathbb{N}`, the
polygon remains piecewise-rectilinear with :math:`n` discrete vertices where curvature is
concentrated, whereas the circle's being consists in uniform, indivisible equidistance from its
center. Finite :term:`reason <ratio-et-intellectus>` moves endlessly along the sequence :math:`n
\\mapsto 2n`; only :term:`intellectus <ratio-et-intellectus>` grasps the limit where polygon
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
""",
    "unit-2-mathematica-transsumptio": """\
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
   :math:`N\\sqrt{2}` atoms, contradicting integer indivisibility.
3. **The Three-Tier Operator (`DI I.12 §1`)**: Let :math:`\\mathcal{F}_R` denote a one-parameter
   family of finite geometric figures indexed by scale parameter :math:`R \\in \\mathbb{Q}_{>0}`,
   and let :math:`\\mathcal{I}(\\mathcal{F}_R)` be an algebraic invariant (such as curvature,
   sagitta, or vertex spread):

   - **Step 1 (*Consideratio finitorum*)**: Compute :math:`\\mathcal{I}(\\mathcal{F}_R)` exactly
     over :math:`\\mathbb{Q}` or radical extensions for finite :math:`R`.
   - **Step 2 (*Translatio ad infinitum*)**: Evaluate :math:`\\lim_{R \\to \\infty}
     \\mathcal{I}(\\mathcal{F}_R)` in intellectual vision, revealing the coincidence of properties
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
""",
    "unit-3-coincidentia-figurarum": """\
I. Exact Symbolic Demonstrations of `DI I.13–15`
------------------------------------------------

1. **Sagitta Asymptotics & Radical Secants (`DI I.13 §2`)**: Let :math:`C_R` be the circle of
   radius :math:`R > 0` with center :math:`O_R = (0, R)` tangent to the straight line :math:`AB`
   (:math:`y = 0`) at :math:`O = (0, 0)`, so :math:`x^2 + (y - R)^2 = R^2`. At fixed horizontal
   abscissa :math:`x \\neq 0` (with :math:`|x| \\le R`), the exact :term:`sagitta <sagitta>` is:

   .. math::

      h(x, R) = R - \\sqrt{R^2 - x^2} = \\frac{x^2}{R + \\sqrt{R^2 - x^2}}.

   Along the secant :math:`x = 1` for :math:`R \\in \\{1, 2, 4, 8\\}` (modeled in
   ``geometor.cusa.coincidentia_circle_line``), the exact symbolic heights are
   :math:`1`, :math:`2 - \\sqrt{3} \\approx 0.26795`, :math:`4 - \\sqrt{15} \\approx 0.12702`, and
   :math:`8 - 3\\sqrt{7} \\approx 0.06275`, with :math:`\\lim_{R \\to \\infty} h(x, R) = 0`,
   :math:`\\lim_{R \\to \\infty} R\\,h(x, R) = \\frac{x^2}{2}`, and curvature :math:`\\kappa(R) =
   \\frac{1}{R} \\to 0`.

2. **Projective-Conformal Proof via Möbius Circle Inversion**: Under inversion in the unit circle
   :math:`\\Omega` centered at :math:`S = (0, -1)` (which fixes the point of tangency :math:`O =
   (0, 0)`), every circle :math:`C_R` of radius :math:`R` maps to a **bounded rational circle**
   :math:`C'_R` with exact center and radius:

   .. math::

      M_R = \\left(0,\\; -\\frac{R}{2R + 1}\\right), \\qquad
      \\rho_R = \\frac{R}{2R + 1}.

   Meanwhile, the straight horizon line :math:`y = 0` maps to the circle :math:`C'_\\infty` with
   center :math:`(0, -\\frac{1}{2})` and radius :math:`\\frac{1}{2}`. Taking :math:`R \\to \\infty`
   on the Riemann sphere :math:`\\widehat{\\mathbb{C}}`, :math:`M_R \\to (0, -\\frac{1}{2})` and
   :math:`\\rho_R \\to \\frac{1}{2}` smoothly in Hausdorff metric: **on the conformal sphere, the
   straight line literally IS the circle through the point at infinity** (:cite:`casey:sequel:1886`,
   :cite:`klein:elementary:1908`).

3. **Rational Trigonometry Proof of the Flattening Triangle (`DI I.14 §§2–3`)**: For the isosceles
   triangle :math:`T_n` with fixed base :math:`B = (-1, 0)`, :math:`C = (1, 0)` (:math:`Q_{\\text{base}}
   = 4`) and apex :math:`A_n = (0, \\frac{1}{n})` over :math:`\\mathbb{Q}(n)` (modeled in
   ``geometor.cusa.coincidentia_triangle_line`` using :person:`Wildberger's <wildberger>`
   invariants, :cite:`wildberger:divine:2005`):

   .. math::

      Q(A_n, B) = Q(A_n, C) = 1 + \\frac{1}{n^2} = \\frac{n^2 + 1}{n^2}, \\qquad
      s_B = s_C = \\frac{1}{n^2 + 1}, \\qquad
      s_{A_n} = \\frac{4n^2}{(n^2 + 1)^2}.

   Every :math:`T_n` satisfies the **Triple Spread Formula** :math:`(s_{A_n} + 2s_B)^2 -
   2(s_{A_n}^2 + 2s_B^2) - 4 s_{A_n} s_B^2 = 0` identically over :math:`\\mathbb{Q}(n)`, while the
   **Triple Quad Formula** collinearity residual equals :math:`(4 + 2Q_{\\text{leg}})^2 - 2(16 +
   2Q_{\\text{leg}}^2) = \\frac{16}{n^2} \\to 0` as :math:`n \\to \\infty`!

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
""",
    "unit-4-linea-sphaera-infinita": """\
I. Infinite Transfinite Equivalence & Geometric Measure (`DI I.16–20`)
----------------------------------------------------------------------

1. **Dedekind-Style Infinite Bijection (`DI I.16 §5`)**: Four centuries before Bolzano, Dedekind,
   and Cantor defined infinite sets by equipollence with proper subsets, :person:`Nicholas of Cusa
   <cusanus>` argues that an infinite line composed of :math:`\\infty` one-foot segments and one
   composed of :math:`\\infty` two-foot segments are necessarily equal (*cum infinitum non sit
   maius infinito*), because every part of the infinite is convertible with the whole infinite.
2. **Why the Maximum Is Triune and Not Quaternary (`DI I.20 §§2–3`)**: `Capitulum XX` supplies a
   purely topological-combinatorial proof of why polygonal resolution halts at three: in
   two-dimensional simplicial decomposition, the triangle (:math:`n = 3`) is the unique minimal
   polygon (*minima figura polygonia, qua minor esse nequit*). Every :math:`k`-gon for :math:`k
   \\ge 4` decomposes into :math:`k - 2` triangles (cf. :person:`Euclid <euclid>` *Elements* I.32
   and VI.20) and is therefore composite and strictly greater than the minimal polygon; hence a
   quadrangle cannot coincide with the simplest :term:`Minimum <minimum>` or serve as the universal
   measure of triangles. Moreover, Cusa enumerates the exact four-element dimensional basis of
   spatial measurement:

   - **1D Length**: :term:`Maximal Infinite Line <linea-infinita>`
   - **2D Rectilinear Breadth**: :term:`Maximal Triangle <triangulus-infinitus>`
   - **2D Circular Breadth**: :term:`Maximal Circle <circulus-infinitus>`
   - **3D Depth**: :term:`Maximal Sphere <sphaera-infinita>`

II. Center, Diameter & Circumference in the Infinite Sphere (`DI I.21–23`)
--------------------------------------------------------------------------

In `DI I.21 §§3–4` and `I.23 §1`, Cusa demonstrates that in the infinite circle and sphere the
distinction between interior center, spanning diameter, and bounding circumference vanishes.
Mapping Aristotle's four causes onto circular geometry (`I.21 §4`), Cusa identifies **center** with
efficient cause (*dans esse*), **diameter** with formal cause (*gubernans*), and **circumference**
with final cause (*conservans*). In `I.22`, Cusa applies his signature pair :term:`complicatio et
explicatio <complicatio-et-explicatio>` via the Asymmetric Implication Law (*posita complicatione
non ponitur res complicata, sed posita explicatione ponitur complicatio*), preserving creaturely
contingency within immutable divine providence.
""",
    "unit-5-cosmologia-complementa": """\
I. Centerless Cosmology & Kinematic Relativity (`DI II.11–12`, 1440)
--------------------------------------------------------------------

Over a century before Copernicus's *De revolutionibus* (1543), Bruno's *De l'infinito universo et
mondi* (1584), and Galileo's *Dialogo* (1632), `DI II.11–12` deduces three revolutionary physical
corollaries directly from :term:`learned ignorance <docta-ignorantia>`:

1. **Impossibility of an Immobile Cosmic Center or Fixed Poles (`II.11 §§1–4`)**: Because physical
   positions, figures, and motions in the contracted cosmos always admit of more and less, exact
   equidistance (*aequedistantia praecisa*) never occurs in nature; hence neither the earth nor the
   sun nor the eighth sphere possesses an immobile geometric center or fixed celestial poles.
2. **Ship-in-Midstream Principle of Relative Motion (`II.12 §1`)**: Motion is detectable solely
   relative to a chosen reference point (*Si enim quis ignoraret aquam fluere et ripas non videret
   existendo in navi in medio aquae, navem quomodo apprehenderet moveri?*). Every observer on
   Earth :g:`T`, Sun :g:`S`, Moon :g:`L`, or Mars constructs his own local horizon and poles,
   rendering the universe *quasi habens undique centrum et nullibi circumferentiam*.
3. **Astrophysical Homogeneity (`II.12 §§3–4`)**: Rejecting the Aristotelian sublunary/superlunary
   chasm, Cusa declares the moving earth a *stella nobilis* shining into space through its outer
   fiery envelope just as the sun shines toward us.

II. Exact Algebraic Audit of the *Scripta Mathematica* (1445–1459)
------------------------------------------------------------------

1. ***De Geometricis Transmutationibus* (1445, `§§9–11`)**: In the unit circle :math:`R = 1`
   centered at :g:`A` at :math:`(0, 0)`, the inscribed equilateral triangle :g:`B`–:g:`C`–:g:`D`
   has side :math:`|BC| = \\sqrt{3}` and perimeter :math:`P_3 = 3\\sqrt{3}`. Dividing :math:`BC`
   into four equal segments at :g:`E`, :g:`F`, :g:`G`, the midpoint :g:`F` satisfies :math:`Q(A, F)
   = \\frac{1}{4}` and the quarter-point :g:`E` satisfies:

   .. math::

      Q(A, E) = |AF|^2 + |FE|^2 = \\frac{1}{4} + \\left(\\frac{\\sqrt{3}}{4}\\right)^2
      = \\frac{7}{16} \\implies |AE| = \\frac{\\sqrt{7}}{4}.

   Extending :math:`AE` in :term:`sesquiquartal ratio <proportio-sesquiquarta>` :math:`5:4` gives
   Cusa's isoperimetric radius :math:`|AH| = \\frac{5\\sqrt{7}}{16}` (:math:`Q(A, H) =
   \\frac{175}{256}`), implying:

   .. math::

      \\pi_{\\text{Cusa},1445} = \\frac{P_3}{2|AH|} = \\frac{3\\sqrt{3}}{5\\sqrt{7}/8}
      = \\frac{24\\sqrt{21}}{35} \\approx 3.14233762,

   which exceeds true :math:`\\pi \\approx 3.14159265` by only :math:`+7.45 \\times 10^{-4}` (lying
   strictly inside :person:`Archimedes' <archimedes>` 96-gon bounds :math:`3\\frac{10}{71} < \\pi <
   3\\frac{1}{7}`, though :person:`Regiomontanus <regiomontanus>` later showed via tighter bounds
   that :math:`\\frac{24\\sqrt{21}}{35} > \\pi`; :cite:`regiomontanus:quadratura:1533`).

2. ***De Mathematicis Complementis* (1453, `§§3–10`)**: Cusa astutely observes that Archimedes'
   spiral :math:`r(\\varphi) = a\\varphi` presupposes the synchronized velocity ratio of uniform
   rectilinear motion along the radius to uniform circular motion along the circumference—the very
   transcendental ratio :math:`1 : 2\\pi` sought by quadrature! His dissection proof in `§10`
   establishes :math:`\\operatorname{Area}(P_n) = r_n \\cdot \\frac{P_n}{2}` purely by Euclidean
   rectangle-halving.

3. ***De Mathematica Perfectione* (1458) & *Aurea Propositio in Mathematicis* (1459)**: Both
   treatises converge on the **Cusa–Snellius–Huygens Law** (:cite:`cusa:perf:1458`,
   :cite:`cusa:aurea:1459`, :cite:`snellius:huygens:1654`). Let rays at angles :math:`\\pm\\theta`
   (:math:`0 < \\theta \\le \\frac{\\pi}{4}`) and central ray :math:`0` issue from :g:`A` at
   :math:`(0, 0)` across unit circle :math:`R = 1`, meeting a vertical rectifying line :math:`x =
   x_K` at :g:`I`, :g:`K`, :g:`L`, so :math:`|AK| = x_K` and :math:`|AI| = |AL| = \\frac{x_K}{\\cos\\theta}`.
   Enforcing Cusa's **Three-Ray Sum Invariance**:

   .. math::

      |AI| + |AK| + |AL| = 3 \\iff x_K\\!\\left(1 + \\frac{2}{\\cos\\theta}\\right) = 3
      \\implies x_K = \\frac{3\\cos\\theta}{2 + \\cos\\theta}.

   At :math:`\\theta = \\frac{\\pi}{6}` (modeled over :math:`\\mathbb{Q}(\\sqrt{3})` in
   ``cusa_aurea_propositio_1459.svg``), :math:`x_K = \\frac{3\\sqrt{3}/2}{2 + \\sqrt{3}/2} =
   \\frac{12\\sqrt{3} - 9}{13}`, the outer rays have length :math:`|AI| = |AL| =
   \\frac{24 - 6\\sqrt{3}}{13}`, the combined endpoint ascent :math:`2(|AI| - 1) =
   \\frac{22 - 12\\sqrt{3}}{13}` equals the midpoint descent :math:`1 - x_K`, and the rectified
   length is:

   .. math::

      L_{\\text{Cusa}}(\\theta) = 2 x_K \\tan\\theta = \\frac{6\\sin\\theta}{2 + \\cos\\theta}
      = 2\\theta - \\frac{\\theta^5}{90} - \\frac{\\theta^7}{756} - O(\\theta^9),

   so for the half-arc :math:`\\theta - \\frac{3\\sin\\theta}{2 + \\cos\\theta} =
   \\frac{\\theta^5}{180} + \\frac{\\theta^7}{1512} + O(\\theta^9)`! Because :math:`\\cos\\theta`
   and :math:`\\sin\\theta` cancel through third order in the `[1/1]` Padé-type rational weight
   :math:`\\frac{3}{2 + \\cos\\theta}`, Cusa achieved **fifth-order accuracy**—yielding at
   :math:`\\theta = \\frac{\\pi}{6}` an implied :math:`\\pi` estimate of
   :math:`\\frac{18}{2 + \\sqrt{3}/2} = \\frac{36(4 - \\sqrt{3})}{26} \\approx 3.140237`, within
   :math:`0.043\\%` of :math:`\\pi`!
""",
}

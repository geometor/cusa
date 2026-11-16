"""Canonical Book Codex unit specifications for GEOMETOR • cusa.

Defines the 11 atomic units across *De Docta Ignorantia* (Liber I & Liber II)
and Cusa's *De Mathematicis Complementis* & *Scripta Mathematica* (1445–1459).
"""

from __future__ import annotations

from dataclasses import dataclass

from geometor.cusa.texts_u1_u3 import (
    UNIT_1_SECTIONS,
    UNIT_2_SECTIONS,
    UNIT_3_SECTIONS,
    BilingualSectionData,
)
from geometor.cusa.texts_u4 import UNIT_4_SECTIONS
from geometor.cusa.texts_u5 import UNIT_5_SECTIONS


@dataclass(frozen=True)
class CodexUnitSpec:
    """Specification for one 4-track synchronized Book Codex unit."""

    unit_number: str
    slug: str
    book_slug: str
    title: str
    subtitle: str
    canonical_id: str
    locus_summary: str
    figure_svg: str
    figure_caption: str
    epigraph_la: str
    epigraph_en: str
    epigraph_locus: str
    demo_doc: str
    sections: tuple[BilingualSectionData, ...]
    unit_key: str = ""
    legacy_slugs: tuple[str, ...] = ()

    @property
    def doc_rel_dir(self) -> str:
        """Relative path under ``docsrc/`` for this unit (e.g. ``de_docta_ignorantia/liber_i/cap_01_04``)."""
        return f"{self.book_slug}/{self.slug}"

    @property
    def key(self) -> str:
        """Unique lookup key for commentary and resources."""
        return self.unit_key or self.slug

    @property
    def source_prefix(self) -> str:
        """Normalized filename prefix for source witness text files."""
        return f"{self.book_slug.replace('/', '-')}-{self.slug}"


CODEX_UNITS: tuple[CodexUnitSpec, ...] = (
    # =========================================================================
    # DE DOCTA IGNORANTIA — LIBER I: DE MAXIMO ABSOLUTO (1440)
    # =========================================================================
    CodexUnitSpec(
        unit_key="cap_01_04",
        slug="cap_01_04",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitula I–IV",
        canonical_id="DI I.1–4",
        title="Learned Ignorance, Polygon Exhaustion & the Coincidence of Maximum and Minimum",
        subtitle=(
            "De Docta Ignorantia · Dedicatio, Liber I, Capitula I–IV & Epistola Auctoris "
            "(Kues, February 12, 1440)"
        ),
        locus_summary="DI Ded., I.1–4, Ep. (1440)",
        figure_svg="cusa_polygon_exhaustion.svg",
        figure_caption=(
            "Book I, Chapter 3 — Inscribed Regular Polygons P_3, P_4, P_6, P_8, P_12 in Unit "
            "Circle C: Monotonically Increasing Apothem r_n = cos(pi/n) -> 1 Without Finite "
            "Identity Between Polygon and Circle."
        ),
        epigraph_la=(
            "Intellectus igitur, qui non est veritas, numquam veritatem adeo praecise "
            "comprehendit, quin per infinitum praecisius comprehendi possit, habens se ad "
            "veritatem sicut polygonia ad circulum."
        ),
        epigraph_en=(
            "The intellect, therefore, which is not truth, never comprehends truth so precisely "
            "that it could not be comprehended infinitely more precisely, standing to truth as "
            "a polygon stands to a circle."
        ),
        epigraph_locus="De Docta Ignorantia I.3 §2",
        demo_doc="/demos/index",
        sections=UNIT_1_SECTIONS,
        legacy_slugs=("unit-1-maximum-ignorantia",),
    ),
    CodexUnitSpec(
        unit_key="cap_11_12",
        slug="cap_11_12",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitula XI–XII",
        canonical_id="DI I.11–12",
        title="Incorruptible Certitude & the Three-Step Method of Mathematical Transsumption",
        subtitle="De Docta Ignorantia · Liber I, Capitula XI–XII (1440)",
        locus_summary="DI I.11–12 (1440)",
        figure_svg="cusa_transsumptio_ascent.svg",
        figure_caption=(
            "Book I, Chapters 11–12 — Three-Tier Epistemological Ascent of Transsumptio: "
            "(I) Finite Figures in Ratio -> (II) Coincident Infinite Limit in Intellectus -> "
            "(III) Transsumption to the Figure-Free Simple Infinite."
        ),
        epigraph_la=(
            "Primo necesse est figuras mathematicas finitas considerare cum suis passionibus et "
            "rationibus, et ipsas rationes correspondenter ad infinitas tales figuras transferre, "
            "post haec tertio adhuc altius ipsas rationes infinitarum figurarum transumere ad "
            "infinitum simplex absolutissimum etiam ab omni figura."
        ),
        epigraph_en=(
            "First we must consider finite mathematical figures with their properties and ratios, "
            "next transfer those ratios correspondingly to infinite figures of the same kind, "
            "and third transsume the ratios of those infinite figures still higher unto the "
            "Simple Infinite wholly absolved from every figure."
        ),
        epigraph_locus="De Docta Ignorantia I.12 §1",
        demo_doc="/demos/index",
        sections=UNIT_2_SECTIONS,
        legacy_slugs=("unit-2-mathematica-transsumptio",),
    ),
    CodexUnitSpec(
        unit_key="cap_13_15",
        slug="cap_13_15",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitula XIII–XV",
        canonical_id="DI I.13–15",
        title="Coincidence of Infinite Circle, Straight Line, Triangle & Sphere",
        subtitle="De Docta Ignorantia · Liber I, Capitula XIII–XV (1440)",
        locus_summary="DI I.13–15 (1440)",
        figure_svg="cusa_circle_line_pencil.svg",
        figure_caption=(
            "Book I, Chapter 13 — Tangent Circle Pencil C_1, C_2, C_4, C_8 at Origin O = (0, 0) "
            "Above Horizon Line AB (y = 0): Exact Radical Secant Sagittae at x = 1 Shrink as "
            "1, 2 - sqrt(3), 4 - sqrt(15), 8 - 3 sqrt(7) -> 0 as Curvature Resolves into "
            "Rectitude."
        ),
        epigraph_la=(
            "Si esset linea infinita, illa esset recta, illa esset triangulus, illa esset "
            "circulus et esset sphaera; immo curvitas in ipsa maxima linea est rectitudo."
        ),
        epigraph_en=(
            "If there were an infinite line, it would be a straight line, a triangle, a circle, "
            "and a sphere; nay rather, within that maximal line itself curvature is rectitude."
        ),
        epigraph_locus="De Docta Ignorantia I.13 §§1–2",
        demo_doc="/demos/index",
        sections=UNIT_3_SECTIONS,
        legacy_slugs=("unit-3-coincidentia-figurarum",),
    ),
    CodexUnitSpec(
        unit_key="cap_16_17",
        slug="cap_16_17",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitula XVI–XVII",
        canonical_id="DI I.16–17",
        title="The Infinite Line as Universal Essence & Most Adequate Measure",
        subtitle="De Docta Ignorantia · Liber I, Capitula XVI–XVII (1440)",
        locus_summary="DI I.16–17 (1440)",
        figure_svg="cusa_line_unfolding_sphere.svg",
        figure_caption=(
            "Book I, Chapters 16–17 — The Maximal Infinite Line as Universal Essence and Most "
            "Adequate Measure of All Finite Things."
        ),
        epigraph_la=(
            "Ipsa igitur maxima linea est adaequatissima mensura omnium linearum, ita quod nec "
            "minor est, quia non exceditur ab aliqua, nec maior, quia nulla eam excedit."
        ),
        epigraph_en=(
            "Therefore the maximal line itself is the most adequate measure of all lines, being "
            "neither smaller—since it is not exceeded by any—nor larger, since none exceeds it."
        ),
        epigraph_locus="De Docta Ignorantia I.16 §3",
        demo_doc="/demos/index",
        sections=UNIT_4_SECTIONS[0:2],
        legacy_slugs=("unit-4-linea-sphaera-infinita",),
    ),
    CodexUnitSpec(
        unit_key="cap_18_20",
        slug="cap_18_20",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitula XVIII–XX",
        canonical_id="DI I.18–20",
        title="Transsumption of the Triangle: Divine Triunity & Exclusion of Quaternity",
        subtitle="De Docta Ignorantia · Liber I, Capitula XVIII–XX (1440)",
        locus_summary="DI I.18–20 (1440)",
        figure_svg="cusa_line_unfolding_sphere.svg",
        figure_caption=(
            "Book I, Chapters 18–20 — Generative Unfolding of the Finite Line into the Maximal "
            "Triangle, Revealing the Unitrine Principle and the Necessary Exclusion of Quaternity."
        ),
        epigraph_la=(
            "Cum enim incipis numerare trinitatem, tunc exis veritatem. Unitas igitur est "
            "trinitas; et econverso trinitas unitas."
        ),
        epigraph_en=(
            "For when you begin to count the Trinity, you step outside the truth. Unity, "
            "therefore, is Trinity, and conversely Trinity is Unity."
        ),
        epigraph_locus="De Docta Ignorantia I.19 §1",
        demo_doc="/demos/index",
        sections=UNIT_4_SECTIONS[2:5],
        legacy_slugs=(),
    ),
    CodexUnitSpec(
        unit_key="cap_21_23",
        slug="cap_21_23",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitula XXI–XXIII",
        canonical_id="DI I.21–23",
        title="The Infinite Sphere Where Center, Diameter & Circumference Coincide",
        subtitle="De Docta Ignorantia · Liber I, Capitula XXI–XXIII (1440)",
        locus_summary="DI I.21–23 (1440)",
        figure_svg="cusa_line_unfolding_sphere.svg",
        figure_caption=(
            "Book I, Chapters 13, 19–21 & 23 — Generative Unfolding of the Finite Line AB "
            "Through Sector Triangle ABC, Circle, and Semicircle BD into the Sphere, Whose "
            "Center, Diameter, and Circumference Coincide in the Infinite Limit."
        ),
        epigraph_la=(
            "Patet ergo centrum, diametrum et circumferentiam idem esse. Ex quo docetur "
            "ignorantia nostra incomprehensibile maximum esse, cui minimum non opponitur; sed "
            "centrum est in ipso circumferentia."
        ),
        epigraph_en=(
            "Clearly, therefore, center, diameter, and circumference are identical; thereby our "
            "ignorance is taught that the incomprehensible Maximum is that to which the Minimum "
            "is not opposed, and that within it the center is the circumference."
        ),
        epigraph_locus="De Docta Ignorantia I.21 §3",
        demo_doc="/demos/index",
        sections=UNIT_4_SECTIONS[5:8],
        legacy_slugs=(),
    ),
    # =========================================================================
    # DE DOCTA IGNORANTIA — LIBER II: DE UNIVERSO ET COSMOLOGIA (1440)
    # =========================================================================
    CodexUnitSpec(
        unit_key="di_liber_ii_cap_11_12",
        slug="cap_11_12",
        book_slug="de_docta_ignorantia/liber_ii",
        unit_number="Capitula XI–XII",
        canonical_id="DI II.11–12",
        title="Centerless Cosmology, Kinematic Relativity & the Fabric of the World",
        subtitle="De Docta Ignorantia · Liber II, Capitula XI–XII (1440)",
        locus_summary="DI II.11–12 (1440)",
        figure_svg="cusa_cosmic_relativity.svg",
        figure_caption=(
            "Book II, Chapters 11–12 — Centerless Cosmic Relativity Frame: Observers on "
            "Terra (T), Sol (S), Luna (L), and Polus (P) Construct Symmetric Horizon Circles "
            "in a Universe Having Its Center Everywhere and Its Circumference Nowhere."
        ),
        epigraph_la=(
            "Unde erit machina mundi quasi habens undique centrum et nullibi circumferentiam, "
            "quoniam eius circumferentia et centrum est Deus, qui est undique et nullibi."
        ),
        epigraph_en=(
            "Thus the fabric of the world will be as though having its center everywhere and its "
            "circumference nowhere, because its circumference and center are God, who is "
            "everywhere and nowhere."
        ),
        epigraph_locus="De Docta Ignorantia II.12 §1",
        demo_doc="/demos/index",
        sections=UNIT_5_SECTIONS[0:2],
        legacy_slugs=("unit-5-cosmologia-complementa",),
    ),
    # =========================================================================
    # DE MATHEMATICIS COMPLEMENTIS & SCRIPTA MATHEMATICA (1445–1459)
    # =========================================================================
    CodexUnitSpec(
        unit_key="transmutatio_1445",
        slug="transmutatio_1445",
        book_slug="de_mathematicis_complementis",
        unit_number="De Geometricis Transmutationibus",
        canonical_id="DGT (1445)",
        title="De Geometricis Transmutationibus — Isoperimetric Extrema and the Sesquiquartal Radius",
        subtitle="To Paolo dal Pozzo Toscanelli: Isoperimetric Extrema and the Sesquiquartal Radius (1445)",
        locus_summary="DGT (1445)",
        figure_svg="cusa_transmutatio_1445.svg",
        figure_caption=(
            "De Geometricis Transmutationibus (1445, §§9–11) — Equilateral Triangle B–C–D "
            "Inscribed in Unit Circle A with Quarter-Point E: Ray AE Extended in 5:4 "
            "Sesquiquartal Ratio to H Yields AH = 5*sqrt(7)/16."
        ),
        epigraph_la=(
            "Omnium figurarum isoperimetrarum capacior est circulus, et minimae capacitatis "
            "triangulus. Inter has extremitates omnes aliae figurae continentur."
        ),
        epigraph_en=(
            "Of all isoperimetric figures the circle has greatest capacity, and the triangle "
            "least capacity; between these extremes all other figures are contained."
        ),
        epigraph_locus="De Geometricis Transmutationibus §1",
        demo_doc="/demos/index",
        sections=UNIT_5_SECTIONS[2:3],
        legacy_slugs=("scripta-geom-trans-1445",),
    ),
    CodexUnitSpec(
        unit_key="complementa_1453",
        slug="complementa_1453",
        book_slug="de_mathematicis_complementis",
        unit_number="De Mathematicis Complementis",
        canonical_id="DMC (1453)",
        title="De Mathematicis Complementis — Inradius, Circumradius, and Archimedes' Spiral",
        subtitle="To Pope Nicholas V: Archimedes' Spiral and the Convergence of Inradius and Circumradius (1453)",
        locus_summary="DMC (1453)",
        figure_svg="cusa_polygon_exhaustion.svg",
        figure_caption=(
            "De Mathematicis Complementis (1453, §§3–10) — The First Line (Inradius) and Second "
            "Line (Circumradius) of Inscribed and Circumscribed Regular Polygons Converging to the "
            "Circular Arc."
        ),
        epigraph_la=(
            "Prima linea est perpendicularis a centro ad latus polygoniae ducta; secunda linea "
            "est a centro ad angulum producta. Crescente numero angulorum prima et secunda linea "
            "coincidunt in radio circuli."
        ),
        epigraph_en=(
            "The first line is the perpendicular drawn from center to polygon side; the second "
            "line is drawn from center to angle. As the number of angles increases, first and "
            "second line coincide in the radius of the circle."
        ),
        epigraph_locus="De Mathematicis Complementis §3",
        demo_doc="/demos/index",
        sections=UNIT_5_SECTIONS[3:4],
        legacy_slugs=("scripta-math-compl-1453",),
    ),
    CodexUnitSpec(
        unit_key="perfectio_1458",
        slug="perfectio_1458",
        book_slug="de_mathematicis_complementis",
        unit_number="De Mathematica Perfectione",
        canonical_id="DMP (1458)",
        title="De Mathematica Perfectione — Vanishing Sagitta and Intellectual Vision",
        subtitle="To Cardinal Antonio Cerdà: Intellectual Vision of the Vanishing Sagitta and the Cusa–Snellius Law (1458)",
        locus_summary="DMP (1458)",
        figure_svg="cusa_circle_line_pencil.svg",
        figure_caption=(
            "De Mathematica Perfectione (1458) — In Right Triangle abc, as Sagitta Vanishes, "
            "Arc Approximates 3*R*sin(theta) / (2*R + R*cos(theta))."
        ),
        epigraph_la=(
            "Visio intellectualis transit supra omnem rationem discursivam, ubi minimum "
            "chordae coincidit cum minimo arcus."
        ),
        epigraph_en=(
            "Intellectual vision rises above all discursive reason to where the minimal "
            "chord coincides with the minimal arc."
        ),
        epigraph_locus="De Mathematica Perfectione §2",
        demo_doc="/demos/index",
        sections=UNIT_5_SECTIONS[4:5],
        legacy_slugs=("scripta-math-perf-1458",),
    ),
    CodexUnitSpec(
        unit_key="aurea_propositio_1459",
        slug="aurea_propositio_1459",
        book_slug="de_mathematicis_complementis",
        unit_number="Aurea Propositio in Mathematicis",
        canonical_id="APM (1459)",
        title="Aurea Propositio in Mathematicis — Three-Ray Sum Invariance and the Golden Proposition",
        subtitle="Three-Ray Radial Sum Invariance and the Complete Geometric Proof of the Golden Proposition (August 8, 1459)",
        locus_summary="APM (1459)",
        figure_svg="cusa_aurea_propositio_1459.svg",
        figure_caption=(
            "Aurea Propositio in Mathematicis (August 8, 1459) — Exact Q(sqrt(3)) Sector "
            "(theta = pi/6): Balanced Rectifying Segment I–K–L with |AI| + |AK| + |AL| = 3R "
            "and Fifth-Order Maclaurin Residual theta^5/180."
        ),
        epigraph_la=(
            "Ipsa est aurea propositio, in qua per rectam lineam rectificatur circuli "
            "circumferentia, manente summa trium radiorum aequali tribus semidiametris."
        ),
        epigraph_en=(
            "This is the Golden Proposition, wherein through a straight line the circle's "
            "circumference is rectified while the sum of the three rays remains equal to three "
            "semidiameters."
        ),
        epigraph_locus="Aurea Propositio in Mathematicis §1",
        demo_doc="/demos/index",
        sections=UNIT_5_SECTIONS[5:6],
        legacy_slugs=("scripta-aurea-prop-1459",),
    ),
)

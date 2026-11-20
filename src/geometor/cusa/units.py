"""Canonical Book Codex unit specifications for GEOMETOR • cusa.

Defines the 25 atomic units across *De Docta Ignorantia* (Liber I & Liber II)
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
    figure_svg: str | None
    figure_caption: str | None
    epigraph_la: str
    epigraph_en: str
    epigraph_locus: str
    demo_doc: str
    sections: tuple[BilingualSectionData, ...]
    unit_key: str = ""
    legacy_slugs: tuple[str, ...] = ()

    @property
    def doc_rel_dir(self) -> str:
        """Relative path under ``docsrc/`` for this unit (e.g. ``de_docta_ignorantia/liber_i/cap_01``)."""
        return f"{self.book_slug}/{self.slug}"

    @property
    def key(self) -> str:
        """Unique lookup key for commentary and resources."""
        return self.unit_key or self.slug

    @property
    def anchor_slug(self) -> str:
        """Unique RST target slug for this unit (avoids Liber I / Liber II collisions)."""
        if self.book_slug.endswith("liber_ii"):
            return self.unit_key or f"liber_ii_{self.slug}"
        return self.slug

    @property
    def source_prefix(self) -> str:
        """Normalized filename prefix for source witness text files."""
        return f"{self.book_slug.replace('/', '-')}-{self.slug}"


CODEX_UNITS: tuple[CodexUnitSpec, ...] = (
    # =========================================================================
    # DE DOCTA IGNORANTIA — LIBER I: DE MAXIMO ABSOLUTO (1440)
    # =========================================================================
    CodexUnitSpec(
        unit_key="di_dedicatio",
        slug="dedicatio",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Dedicatio",
        canonical_id="DI Ded.",
        title="Dedicatory Prologue to Cardinal Julian Cesarini",
        subtitle="De Docta Ignorantia · Dedicatio ad Dominum Iulianum Cardinalem (1440)",
        locus_summary="DI Ded. (1440)",
        figure_svg=None,
        figure_caption=None,
        epigraph_la=(
            "Ita recte puto admirari, propter quod philosophari, sciendi desiderium praevenire, "
            "ut intellectus, cuius intelligere est esse, studio veritatis perficiatur."
        ),
        epigraph_en=(
            "In just this way I judge that wonder, on account of which philosophy begins, runs "
            "ahead of the desire to know, so that the intellect, whose very being is to "
            "understand, may be brought to perfection through the study of truth."
        ),
        epigraph_locus="De Docta Ignorantia, Dedicatio §2",
        demo_doc="/demos/index",
        sections=(UNIT_1_SECTIONS[0],),
        legacy_slugs=("cap_01_04", "unit-1-maximum-ignorantia"),
    ),
    CodexUnitSpec(
        unit_key="di_i_cap_01",
        slug="cap_01",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitulum I",
        canonical_id="DI I.1",
        title="How To Know Is Not-To-Know: Comparative Proportion & Socratic Ignorance",
        subtitle="De Docta Ignorantia · Liber I, Capitulum I (1440)",
        locus_summary="DI I.1 (1440)",
        figure_svg=None,
        figure_caption=None,
        epigraph_la=(
            "Omnis igitur inquisitio in comparativa proportione facili vel difficili existit; "
            "propter quod infinitum ut infinitum, cum omnem proportionem aufugiat, ignotum est."
        ),
        epigraph_en=(
            "Every inquiry, accordingly, consists in comparative proportion, whether easy or "
            "difficult; for which reason the infinite as infinite, since it escapes all "
            "proportion, remains unknown."
        ),
        epigraph_locus="De Docta Ignorantia I.1 §2",
        demo_doc="/demos/index",
        sections=(UNIT_1_SECTIONS[1],),
        legacy_slugs=(),
    ),
    CodexUnitSpec(
        unit_key="di_i_cap_02",
        slug="cap_02",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitulum II",
        canonical_id="DI I.2",
        title="Preliminary Elucidation of the Absolute, Contracted, and Joined Maximum",
        subtitle="De Docta Ignorantia · Liber I, Capitulum II (1440)",
        locus_summary="DI I.2 (1440)",
        figure_svg=None,
        figure_caption=None,
        epigraph_la=(
            "Maximum autem hoc dico, quo nihil maius esse potest. Abundantia vero uni convenit. "
            "Coincidit itaque maximitati unitas, quae est et entitas."
        ),
        epigraph_en=(
            "Now I call 'Maximum' that than which nothing can be greater. Yet fullness belongs "
            "to the One. Unity, therefore—which is also beingness—coincides with maximality."
        ),
        epigraph_locus="De Docta Ignorantia I.2 §1",
        demo_doc="/demos/index",
        sections=(UNIT_1_SECTIONS[2],),
        legacy_slugs=(),
    ),
    CodexUnitSpec(
        unit_key="di_i_cap_03",
        slug="cap_03",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitulum III",
        canonical_id="DI I.3",
        title="That Precise Truth Is Incomprehensible: Polygon Exhaustion & the Circle",
        subtitle="De Docta Ignorantia · Liber I, Capitulum III (1440)",
        locus_summary="DI I.3 (1440)",
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
        sections=(UNIT_1_SECTIONS[3],),
        legacy_slugs=(),
    ),
    CodexUnitSpec(
        unit_key="di_i_cap_04",
        slug="cap_04",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitulum IV",
        canonical_id="DI I.4",
        title="The Absolute Maximum and the Coincidence of Maximum and Minimum",
        subtitle="De Docta Ignorantia · Liber I, Capitulum IV (1440)",
        locus_summary="DI I.4 (1440)",
        figure_svg=None,
        figure_caption=None,
        epigraph_la=(
            "Maximum itaque absolutum cum sit omne id quod esse potest, est penitus in actu; "
            "et sicut non potest esse maius, eadem ratione nec minus, cum sit omne id quod "
            "esse potest. Minimum autem est, quo minus esse non potest."
        ),
        epigraph_en=(
            "Because the Absolute Maximum is everything that can be, it is wholly in act; and "
            "just as it cannot be greater, for the very same reason neither can it be smaller, "
            "since it is all that can be. Now the Minimum is that than which nothing can be smaller."
        ),
        epigraph_locus="De Docta Ignorantia I.4 §1",
        demo_doc="/demos/index",
        sections=(UNIT_1_SECTIONS[4],),
        legacy_slugs=(),
    ),
    CodexUnitSpec(
        unit_key="di_i_cap_11",
        slug="cap_11",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitulum XI",
        canonical_id="DI I.11",
        title="Incorruptible Certitude of Mathematical Entities in Apprehending Divine Truths",
        subtitle="De Docta Ignorantia · Liber I, Capitulum XI (1440)",
        locus_summary="DI I.11 (1440)",
        figure_svg="cusa_transsumptio_ascent.svg",
        figure_caption=(
            "Book I, Chapters 11–12 — Three-Tier Epistemological Ascent of Transsumptio: "
            "(I) Finite Figures in Ratio -> (II) Coincident Infinite Limit in Intellectus -> "
            "(III) Transsumption to the Figure-Free Simple Infinite."
        ),
        epigraph_la=(
            "In rebus enim incorruptibilibus et certis mathematicis signis utimur, quoniam "
            "corporalia in quadam instabili possibilitate fluctuant, mathematicalia vero "
            "abstracta stabilissima nobis sunt."
        ),
        epigraph_en=(
            "Therefore we employ mathematical signs, which are incorruptible and certain; for "
            "corporeal things fluctuate in a certain unstable possibility, whereas mathematical "
            "entities, being abstracted, possess the utmost stability for us."
        ),
        epigraph_locus="De Docta Ignorantia I.11 §1",
        demo_doc="/demos/index",
        sections=(UNIT_2_SECTIONS[0],),
        legacy_slugs=("cap_11_12", "unit-2-mathematica-transsumptio"),
    ),
    CodexUnitSpec(
        unit_key="di_i_cap_12",
        slug="cap_12",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitulum XII",
        canonical_id="DI I.12",
        title="The Three-Step Method of Mathematical Transsumption",
        subtitle="De Docta Ignorantia · Liber I, Capitulum XII (1440)",
        locus_summary="DI I.12 (1440)",
        figure_svg="cusa_transsumptio_ascent.svg",
        figure_caption=(
            "Book I, Chapter 12 — Three-Tier Epistemological Ascent of Transsumptio: "
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
        sections=(UNIT_2_SECTIONS[1],),
        legacy_slugs=(),
    ),
    CodexUnitSpec(
        unit_key="di_i_cap_13",
        slug="cap_13",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitulum XIII",
        canonical_id="DI I.13",
        title="Properties of the Maximal Infinite Line: Curvature Resolves into Rectitude",
        subtitle="De Docta Ignorantia · Liber I, Capitulum XIII (1440)",
        locus_summary="DI I.13 (1440)",
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
        sections=(UNIT_3_SECTIONS[0],),
        legacy_slugs=("cap_13_15", "unit-3-coincidentia-figurarum"),
    ),
    CodexUnitSpec(
        unit_key="di_i_cap_14",
        slug="cap_14",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitulum XIV",
        canonical_id="DI I.14",
        title="That the Infinite Line Is a Triangle: Flattening Triangle & Triple Quad Limit",
        subtitle="De Docta Ignorantia · Liber I, Capitulum XIV (1440)",
        locus_summary="DI I.14 (1440)",
        figure_svg="cusa_flattening_triangles.svg",
        figure_caption=(
            "Book I, Chapter 14 — Fixed Base BC with Descending Apices A_n = (0, 1/n) for "
            "n = 1, 2, 4, 8: Apex Spread s_A = 4n^2/(n^2 + 1)^2 -> 0 and Triple Quad Residual "
            "16/n^2 -> 0 as the Triangle Resolves into Line BC."
        ),
        epigraph_la=(
            "In omni enim triangulo duo latera simul iuncta tertio sunt maiora; sed si unum "
            "latus est infinitum, cetera non possunt esse minora."
        ),
        epigraph_en=(
            "In every triangle two sides joined together are greater than the third; yet if one "
            "side is infinite, the remaining sides cannot be smaller."
        ),
        epigraph_locus="De Docta Ignorantia I.14 §1",
        demo_doc="/demos/index",
        sections=(UNIT_3_SECTIONS[1],),
        legacy_slugs=(),
    ),
    CodexUnitSpec(
        unit_key="di_i_cap_15",
        slug="cap_15",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitulum XV",
        canonical_id="DI I.15",
        title="That That Triangle Is a Circle and a Sphere: Conformal Inversion & Unfolding",
        subtitle="De Docta Ignorantia · Liber I, Capitulum XV (1440)",
        locus_summary="DI I.15 (1440)",
        figure_svg="cusa_mobius_inversion.svg",
        figure_caption=(
            "Book I, Chapter 15 — Conformal Circle Inversion of Tangent Pencil C_R in Unit "
            "Circle at Pole S = (0, -1): Rational Image Circles Converge to Limit Circle "
            "Center (0, -1/2), Radius 1/2."
        ),
        epigraph_la=(
            "Et quoniam linea infinita est in actu id omne, quod in potentia est finita: "
            "sequitur eam esse triangulum, circulum et sphaeram."
        ),
        epigraph_en=(
            "And since the infinite line is in act all that which the finite line is in "
            "potency, it follows that it is a triangle, a circle, and a sphere."
        ),
        epigraph_locus="De Docta Ignorantia I.15 §3",
        demo_doc="/demos/index",
        sections=(UNIT_3_SECTIONS[2],),
        legacy_slugs=(),
    ),
    CodexUnitSpec(
        unit_key="di_i_cap_16",
        slug="cap_16",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitulum XVI",
        canonical_id="DI I.16",
        title="The Infinite Line as Universal Essence & Most Adequate Measure",
        subtitle="De Docta Ignorantia · Liber I, Capitulum XVI (1440)",
        locus_summary="DI I.16 (1440)",
        figure_svg="cusa_line_unfolding_sphere.svg",
        figure_caption=(
            "Book I, Chapter 16 — The Maximal Infinite Line as Universal Essence and Most "
            "Adequate Measure of All Finite Lines."
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
        sections=(UNIT_4_SECTIONS[0],),
        legacy_slugs=("cap_16_17", "unit-4-linea-sphaera-infinita"),
    ),
    CodexUnitSpec(
        unit_key="di_i_cap_17",
        slug="cap_17",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitulum XVII",
        canonical_id="DI I.17",
        title="Profoundest Doctrines Drawn from the Infinite Line: Indivisibility & Measure",
        subtitle="De Docta Ignorantia · Liber I, Capitulum XVII (1440)",
        locus_summary="DI I.17 (1440)",
        figure_svg=None,
        figure_caption=None,
        epigraph_la=(
            "Linea finita est divisibilis et infinita indivisibilis, quia infinitum non habet "
            "partes, in quo maximum coincidit cum minimo."
        ),
        epigraph_en=(
            "A finite line is divisible whereas the infinite line is indivisible, because the "
            "infinite—in which the Maximum coincides with the Minimum—has no parts."
        ),
        epigraph_locus="De Docta Ignorantia I.17 §1",
        demo_doc="/demos/index",
        sections=(UNIT_4_SECTIONS[1],),
        legacy_slugs=(),
    ),
    CodexUnitSpec(
        unit_key="di_i_cap_18",
        slug="cap_18",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitulum XVIII",
        canonical_id="DI I.18",
        title="Immediate and Mediate Participation in Rectitude and Beingness",
        subtitle="De Docta Ignorantia · Liber I, Capitulum XVIII (1440)",
        locus_summary="DI I.18 (1440)",
        figure_svg=None,
        figure_caption=None,
        epigraph_la=(
            "Rectitudo igitur infinita est mensura rectitudinis et curvitatis; sed recta linea "
            "immediatius participat rectitudinem, curva vero mediate."
        ),
        epigraph_en=(
            "Infinite rectitude is therefore the measure both of straightness and of curvature; "
            "yet a straight line participates in rectitude immediately, whereas a curved line "
            "participates mediately."
        ),
        epigraph_locus="De Docta Ignorantia I.18 §2",
        demo_doc="/demos/index",
        sections=(UNIT_4_SECTIONS[2],),
        legacy_slugs=("cap_18_20",),
    ),
    CodexUnitSpec(
        unit_key="di_i_cap_19",
        slug="cap_19",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitulum XIX",
        canonical_id="DI I.19",
        title="Transsumption of the Infinite Triangle to the Maximal Trinity",
        subtitle="De Docta Ignorantia · Liber I, Capitulum XIX (1440)",
        locus_summary="DI I.19 (1440)",
        figure_svg="cusa_line_unfolding_sphere.svg",
        figure_caption=(
            "Book I, Chapter 19 — Generative Unfolding of the Finite Line AB Through Sector "
            "Triangle ABC into the Maximal Triangle Where Three Sides Coincide."
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
        sections=(UNIT_4_SECTIONS[3],),
        legacy_slugs=(),
    ),
    CodexUnitSpec(
        unit_key="di_i_cap_20",
        slug="cap_20",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitulum XX",
        canonical_id="DI I.20",
        title="Why a Quaternity or More Is Impossible: Minimal Polygon Theorem",
        subtitle="De Docta Ignorantia · Liber I, Capitulum XX (1440)",
        locus_summary="DI I.20 (1440)",
        figure_svg=None,
        figure_caption=None,
        epigraph_la=(
            "Triangulus est minima figura polygonia, qua minor esse nequit; quadrangulus autem "
            "non est minima figura, quia componitur ex triangulis."
        ),
        epigraph_en=(
            "The triangle is the minimal polygonal figure, than which none can be smaller; "
            "whereas a quadrangle is not a minimal figure, because it is composed of triangles."
        ),
        epigraph_locus="De Docta Ignorantia I.20 §2",
        demo_doc="/demos/index",
        sections=(UNIT_4_SECTIONS[4],),
        legacy_slugs=(),
    ),
    CodexUnitSpec(
        unit_key="di_i_cap_21",
        slug="cap_21",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitulum XXI",
        canonical_id="DI I.21",
        title="The Infinite Circle Where Center, Diameter & Circumference Coincide",
        subtitle="De Docta Ignorantia · Liber I, Capitulum XXI (1440)",
        locus_summary="DI I.21 (1440)",
        figure_svg="cusa_line_unfolding_sphere.svg",
        figure_caption=(
            "Book I, Chapter 21 — Infinite Circle Whose Center, Diameter, and Circumference "
            "Coincide in Circular Theology."
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
        sections=(UNIT_4_SECTIONS[5],),
        legacy_slugs=("cap_21_23",),
    ),
    CodexUnitSpec(
        unit_key="di_i_cap_22",
        slug="cap_22",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitulum XXII",
        canonical_id="DI I.22",
        title="How Divine Providence Enfolds & Unites Contradictories",
        subtitle="De Docta Ignorantia · Liber I, Capitulum XXII (1440)",
        locus_summary="DI I.22 (1440)",
        figure_svg=None,
        figure_caption=None,
        epigraph_la=(
            "Posita complicatione non ponitur res complicata, sed posita explicatione ponitur "
            "complicatio."
        ),
        epigraph_en=(
            "When the enfolding is posited, the enfolded thing is not thereby posited, whereas "
            "when the unfolding is posited, the enfolding is necessarily posited."
        ),
        epigraph_locus="De Docta Ignorantia I.22 §2",
        demo_doc="/demos/index",
        sections=(UNIT_4_SECTIONS[6],),
        legacy_slugs=(),
    ),
    CodexUnitSpec(
        unit_key="di_i_cap_23",
        slug="cap_23",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Capitulum XXIII",
        canonical_id="DI I.23",
        title="Transsumption of the Infinite Sphere to the Actual Existence of God",
        subtitle="De Docta Ignorantia · Liber I, Capitulum XXIII (1440)",
        locus_summary="DI I.23 (1440)",
        figure_svg="cusa_line_unfolding_sphere.svg",
        figure_caption=(
            "Book I, Chapter 23 — Semicircle BD Unfolding into the Infinite Sphere, Where "
            "Length, Breadth, and Depth Concur Identically in the Center."
        ),
        epigraph_la=(
            "In sphaera infinita longitudo, latitudo et profunditas concurrunt in centro; "
            "centrum enim est ipsa sphaera, et ipsius sphaerae actus est omnium motuum quies."
        ),
        epigraph_en=(
            "In the infinite sphere length, breadth, and depth concur in the center; for the "
            "center is the sphere itself, and the actuality of that sphere is the rest of all motions."
        ),
        epigraph_locus="De Docta Ignorantia I.23 §1",
        demo_doc="/demos/index",
        sections=(UNIT_4_SECTIONS[7],),
        legacy_slugs=(),
    ),
    CodexUnitSpec(
        unit_key="di_epistola",
        slug="epistola",
        book_slug="de_docta_ignorantia/liber_i",
        unit_number="Epistola Auctoris",
        canonical_id="DI Ep.",
        title="Author's Epistolary Colophon: The Sea-Voyage Illumination (1440)",
        subtitle="De Docta Ignorantia · Epistola Auctoris ad Dominum Iulianum Cardinalem (Kues, February 12, 1440)",
        locus_summary="DI Ep. (1440)",
        figure_svg=None,
        figure_caption=None,
        epigraph_la=(
            "In mari me ex Graecia redeunte, credo superno dono a patre luminum, a quo omne "
            "datum optimum, ad hoc ductus sum, ut incomprehensibilia incomprehensibiliter "
            "amplecterer in docta ignorantia."
        ),
        epigraph_en=(
            "While I was returning by sea from Greece, I was led—I believe by a supernal gift "
            "from the Father of Lights, from whom comes every best gift—to embrace "
            "incomprehensible things incomprehensibly in learned ignorance."
        ),
        epigraph_locus="De Docta Ignorantia, Epistola Auctoris §1",
        demo_doc="/demos/index",
        sections=(UNIT_1_SECTIONS[5],),
        legacy_slugs=(),
    ),
    # =========================================================================
    # DE DOCTA IGNORANTIA — LIBER II: DE UNIVERSO ET COSMOLOGIA (1440)
    # =========================================================================
    CodexUnitSpec(
        unit_key="di_ii_cap_11",
        slug="cap_11",
        book_slug="de_docta_ignorantia/liber_ii",
        unit_number="Capitulum XI",
        canonical_id="DI II.11",
        title="Corollaries Concerning Motion: Impossibility of Fixed Center or Poles",
        subtitle="De Docta Ignorantia · Liber II, Capitulum XI (1440)",
        locus_summary="DI II.11 (1440)",
        figure_svg="cusa_cosmic_relativity.svg",
        figure_caption=(
            "Book II, Chapter 11 — Centerless Cosmic Relativity Frame: No Physical Body "
            "Attains Exact Equidistance or an Immobile Center."
        ),
        epigraph_la=(
            "In his enim non reperitur praecisa aequedistantia ad diversa, et propterea "
            "centrum mundi non potest esse terra aut aliqua sphaera."
        ),
        epigraph_en=(
            "Among physical things no exact equidistance to diverse points is ever found, and "
            "therefore neither the earth nor any sphere can be the fixed center of the world."
        ),
        epigraph_locus="De Docta Ignorantia II.11 §2",
        demo_doc="/demos/index",
        sections=(UNIT_5_SECTIONS[0],),
        legacy_slugs=("di_liber_ii_cap_11_12", "unit-5-cosmologia-complementa"),
    ),
    CodexUnitSpec(
        unit_key="di_ii_cap_12",
        slug="cap_12",
        book_slug="de_docta_ignorantia/liber_ii",
        unit_number="Capitulum XII",
        canonical_id="DI II.12",
        title="On the Conditions of the Earth: Kinematic Relativity & the Noble Star",
        subtitle="De Docta Ignorantia · Liber II, Capitulum XII (1440)",
        locus_summary="DI II.12 (1440)",
        figure_svg="cusa_cosmic_relativity.svg",
        figure_caption=(
            "Book II, Chapter 12 — Centerless Cosmic Relativity Frame: Observers on Terra (T), "
            "Sol (S), Luna (L), and Polus (P) Construct Symmetric Horizon Circles in a Universe "
            "Having Its Center Everywhere and Its Circumference Nowhere."
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
        sections=(UNIT_5_SECTIONS[1],),
        legacy_slugs=(),
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
        sections=(UNIT_5_SECTIONS[2],),
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
        sections=(UNIT_5_SECTIONS[3],),
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
        sections=(UNIT_5_SECTIONS[4],),
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
        sections=(UNIT_5_SECTIONS[5],),
        legacy_slugs=("scripta-aurea-prop-1459",),
    ),
)

"""Codex unit specifications for GEOMETOR • cusa (*De Docta Ignorantia* & *Scripta Mathematica*)."""

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
    title: str
    subtitle: str
    locus_summary: str
    figure_svg: str
    figure_caption: str
    epigraph_la: str
    epigraph_en: str
    epigraph_locus: str
    demo_doc: str
    sections: tuple[BilingualSectionData, ...]


CODEX_UNITS: tuple[CodexUnitSpec, ...] = (
    CodexUnitSpec(
        unit_number="Unit I",
        slug="unit-1-maximum-ignorantia",
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
    ),
    CodexUnitSpec(
        unit_number="Unit II",
        slug="unit-2-mathematica-transsumptio",
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
    ),
    CodexUnitSpec(
        unit_number="Unit III",
        slug="unit-3-coincidentia-figurarum",
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
    ),
    CodexUnitSpec(
        unit_number="Unit IV",
        slug="unit-4-linea-sphaera-infinita",
        title=(
            "The Infinite Line as Universal Measure & the Infinite Sphere Where Center, "
            "Diameter and Circumference Coincide"
        ),
        subtitle="De Docta Ignorantia · Liber I, Capitula XVI–XXIII (1440)",
        locus_summary="DI I.16–23 (1440)",
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
        sections=UNIT_4_SECTIONS,
    ),
    CodexUnitSpec(
        unit_number="Unit V",
        slug="unit-5-cosmologia-complementa",
        title=(
            "Centerless Cosmology & the Scripta Mathematica (1445–1459): Isoperimetric "
            "Transmutations and the Golden Proposition"
        ),
        subtitle=(
            "De Docta Ignorantia II.11–12 (1440) · De Geometricis Transmutationibus (1445) · "
            "De Mathematicis Complementis (1453) · De Mathematica Perfectione (1458) · "
            "Aurea Propositio in Mathematicis (1459)"
        ),
        locus_summary="DI II.11–12 · DGT · DMC · DMP · APM (1440–1459)",
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
        sections=UNIT_5_SECTIONS,
    ),
)

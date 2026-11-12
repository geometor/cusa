"""Cross-corpus concordance linking Nicholas of Cusa to the GEOMETOR canon.

Connects *De Docta Ignorantia* (1440) and Cusa's *Scripta Mathematica* (1445–1459)
to ``plato``, ``aristotle``, ``euclid``/``elements``, ``archimedes``, ``proclus``,
``aquinas``, ``hoenen``, ``pacioli``, ``durer``, ``kepler``, ``casey``, ``klein``,
and ``wildberger``.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

__all__ = [
    "CONCORDANCE_ENTRIES",
    "render_concordance_rst",
    "write_concordance_artifacts",
]

CONCORDANCE_ENTRIES: list[dict[str, Any]] = [
    {
        "id": "cusa:ddi:dedicatio",
        "locus": "De Docta Ignorantia, Dedicatio & Epistola auctoris (Feb 12, 1440)",
        "unit": "unit-1-maximum-ignorantia",
        "theme": "Wonder (admiratio) & the Sea-Voyage Illumination of Coincidentia Oppositorum",
        "ancient_medieval_links": [
            "plato: Theaetetus 155d (wonder as origin of philosophy)",
            "aristotle: Metaphysics I.2, 982b12 (propter admirari philosophari)",
            "dionysius: Mystica Theologia I.1–3 (apophatic ascent)",
        ],
        "renaissance_modern_links": [
            "kepler: Mysterium Cosmographicum (1596), Cap. II ('divinus mihi Cusanus')",
            "hoenen: De Noetica Geometriae (1954), Cap. I (intellectual insight)",
        ],
        "symbolic_hook": "geometor.cusa.coincidentia_circle_line.verify_sagitta_and_curvature_limits",
    },
    {
        "id": "cusa:ddi:I.1",
        "locus": "De Docta Ignorantia I.1 (Quomodo scire est ignorare)",
        "unit": "unit-1-maximum-ignorantia",
        "theme": "Comparative Inquiry via Proportion, Number & Socratic Learned Ignorance",
        "ancient_medieval_links": [
            "plato: Apology 21d & Meno 80d–84c (knowing one's ignorance as spur to inquiry)",
            "aristotle: Metaphysics II.1, 993b9–11 (night-owl / bat before the sun)",
            "euclid: Elements I, Common Notions & Book V (reduction to first principles via media)",
        ],
        "renaissance_modern_links": [
            "pacioli: De Divina Proportione (1509), Caps. V–VII (proportion as medium of all science)",
            "hoenen: De Noetica Geometriae (1954), Cap. IV (axiomatic nexus)",
        ],
        "symbolic_hook": "geometor.cusa.polygon_exhaustion_and_complementa.compute_polygon_exhaustion_table",
    },
    {
        "id": "cusa:ddi:I.2-4",
        "locus": "De Docta Ignorantia I.2 & I.4 (Maximum absolutum & Coincidentia minimi)",
        "unit": "unit-1-maximum-ignorantia",
        "theme": "The Absolute Maximum and Coincidence of Maximum & Minimum Beyond Non-Contradiction",
        "ancient_medieval_links": [
            "plato: Parmenides 137c–142a & Philebus 24a–25d (the 'more and less' vs. uncontracted One)",
            "aristotle: Metaphysics IV.3, 1005b19 (principle of non-contradiction in discursive ratio)",
            "aquinas: Summa Theologiae I, q. 7 & In Boethium de Trinitate q. 6 (judgment above imagination)",
        ],
        "renaissance_modern_links": [
            "klein: Elementarmathematik II (projective identification of +oo and -oo on P^1(R))",
        ],
        "symbolic_hook": "geometor.cusa.coincidentia_circle_line.verify_mobius_inversion_coincidence",
    },
    {
        "id": "cusa:ddi:I.3",
        "locus": "De Docta Ignorantia I.3 (Quod praecisa veritas sit incomprehensibilis)",
        "unit": "unit-1-maximum-ignorantia",
        "theme": "Inscribed Polygon Exhaustion & Incommensurability of Non-Circle with Circle",
        "ancient_medieval_links": [
            "euclid: Elements IV.2–15 & XII.2 (inscribed/circumscribed polygons & exhaustion)",
            "archimedes: Dimensio Circuli Props. 1–3 (96-gon rational bounds on pi)",
            "aristotle: Physics VII.4, 248a10–b7 (incomparability of circular arc and straight line)",
        ],
        "renaissance_modern_links": [
            "pacioli: De Divina Proportione (1509), Cap. V (irrationality as divine emblem)",
            "durer: Underweysung der Messung (1525), Book II (constructive polygon series)",
        ],
        "symbolic_hook": "geometor.cusa.polygon_exhaustion_and_complementa.construct_polygon_exhaustion",
    },
    {
        "id": "cusa:ddi:I.11",
        "locus": "De Docta Ignorantia I.11 (Quod mathematica nos iuvet plurimum)",
        "unit": "unit-2-mathematica-transsumptio",
        "theme": "Incorruptible Certainty of Mathematical Signs & Refutation of Indivisible Atoms",
        "ancient_medieval_links": [
            "plato: Republic VI–VII, 510b–527c (mathematicals drawing soul toward essence)",
            "aristotle: Metaphysics VIII.3, 1043b33 (species compared to numbers) & De Anima II.3, 414b29 (triangle in quadrangle)",
            "proclus: In Euclidem Prologue I, Friedlein pp. 3–32 (intermediate status of mathematicals)",
            "aquinas: In Boethium de Trinitate q. 5 a. 3 & q. 6 a. 2 (materia intelligibilis & certitudo mathematicae)",
        ],
        "renaissance_modern_links": [
            "hoenen: De Noetica Geometriae (1954), Caps. II–III (abstraction of geometric extension)",
        ],
        "symbolic_hook": "geometor.cusa.polygon_exhaustion_and_complementa.construct_transsumptio_ascent",
    },
    {
        "id": "cusa:ddi:I.12",
        "locus": "De Docta Ignorantia I.12 (Quomodo signis mathematicalibus sit utendum)",
        "unit": "unit-2-mathematica-transsumptio",
        "theme": "The Three-Step Method of Mathematical Transsumption (Finitum -> Infinitum -> Simplex)",
        "ancient_medieval_links": [
            "plato: Republic VI, 510b–511d (ascent from hypothetical figures to unhypothetical first principle)",
            "proclus: In Euclidem pp. 51–56 (projection of forms in geometric imagination)",
        ],
        "renaissance_modern_links": [
            "kepler: Ad Vitellionem Paralipomena (1604), Cap. IV.4 (principle of continuity from ellipse to parabola to straight line)",
        ],
        "symbolic_hook": "geometor.cusa.polygon_exhaustion_and_complementa.construct_transsumptio_ascent",
    },
    {
        "id": "cusa:ddi:I.13",
        "locus": "De Docta Ignorantia I.13 (De passionibus lineae maximae et infinitae)",
        "unit": "unit-3-coincidentia-figurarum",
        "theme": "Coincidence of the Infinite Circle & Tangent Arc with the Infinite Straight Line",
        "ancient_medieval_links": [
            "plato: Parmenides 137e (definitions of straight and round)",
            "euclid: Elements III.16 (horn angle between circle and tangent smaller than any rectilinear angle)",
            "proclus: In Euclidem pp. 103–113 (dialectic of straight and circular lines)",
        ],
        "renaissance_modern_links": [
            "kepler: Mysterium Cosmographicum (1596), Cap. II (curved and straight in Cusanus)",
            "casey: Sequel to Euclid (1886), VI.5 (inversion of coaxial tangent circle pencil into parallel lines)",
            "klein: Elementarmathematik II (Möbius group Equivalence of lines and circles on S^2)",
        ],
        "symbolic_hook": "geometor.cusa.coincidentia_circle_line.construct_tangent_circle_pencil",
    },
    {
        "id": "cusa:ddi:I.14",
        "locus": "De Docta Ignorantia I.14 (Quod infinita linea sit triangulus)",
        "unit": "unit-3-coincidentia-figurarum",
        "theme": "Collapse of the Flattening Triangle onto the Straight Line as Apex Approaches Two Right Angles",
        "ancient_medieval_links": [
            "euclid: Elements I.20 (triangle inequality BA + AC > BC) & I.32 (angle sum = 2 right angles)",
            "proclus: In Euclidem pp. 321–326, 379–384 (on Elements I.20 and I.32)",
        ],
        "renaissance_modern_links": [
            "wildberger: Divine Proportions (2005), Chs. 3–4 (apex spread s_A = 4n^2/(n^2+1)^2 -> 0 & Triple Quad residual 16/n^2 -> 0)",
        ],
        "symbolic_hook": "geometor.cusa.coincidentia_triangle_line.construct_flattening_triangles",
    },
    {
        "id": "cusa:ddi:I.15",
        "locus": "De Docta Ignorantia I.15 (Quod ille triangulus sit circulus et sphaera)",
        "unit": "unit-3-coincidentia-figurarum",
        "theme": "Generative Circumduction of the Infinite Line into Triangle, Circle & Sphere",
        "ancient_medieval_links": [
            "euclid: Elements I, Post. 3 & XI, Def. 14 (sphere defined by semicircle rotation around fixed diameter)",
            "proclus: In Euclidem pp. 185–187 (kinematic generation of circle by revolving line)",
        ],
        "renaissance_modern_links": [
            "durer: Underweysung der Messung (1525), Book I (kinematic generation of curves and solids)",
            "klein: Elementarmathematik II (compactification of R^2 to S^2)",
        ],
        "symbolic_hook": "geometor.cusa.polygon_exhaustion_and_complementa.construct_generative_unfolding",
    },
    {
        "id": "cusa:ddi:I.16-18",
        "locus": "De Docta Ignorantia I.16–18 (Mensura adaequatissima & Participatio rectitudinis)",
        "unit": "unit-4-linea-sphaera-infinita",
        "theme": "The Infinite Line as Exact Measure of All Lines & Rectitude as Measure of the Curved",
        "ancient_medieval_links": [
            "plato: Phaedo 100b–e (participation in the single Idea, cited via Calcidius in I.17)",
            "aristotle: Metaphysics X.1, 1052b18 (first as measure) & De Anima I.5, 411a5 (rectum est iudex sui et obliqui)",
            "aquinas: Summa Theologiae I, q. 13 & q. 44 (exemplar causality and analogical participation)",
        ],
        "renaissance_modern_links": [
            "hoenen: De Noetica Geometriae (1954), Cap. VII (measure and continuum)",
        ],
        "symbolic_hook": "geometor.cusa.coincidentia_circle_line.verify_sagitta_and_curvature_limits",
    },
    {
        "id": "cusa:ddi:I.19-23",
        "locus": "De Docta Ignorantia I.19, I.21–23 (Triangulus, Circulus & Sphaera Infinita)",
        "unit": "unit-4-linea-sphaera-infinita",
        "theme": "Coincidence of Center, Diameter & Circumference in the Infinite Circle and Sphere",
        "ancient_medieval_links": [
            "plato: Parmenides 137e & Timaeus 33b (spherical equidistance and perfection)",
            "proclus: In Euclidem pp. 146–155 (symbolic theology of center, radii, and circumference)",
            "dionysius: De Divinis Nominibus V.6 & IX (center containing all radii)",
        ],
        "renaissance_modern_links": [
            "pacioli: De Divina Proportione (1509), Cap. V (trinitarian geometry)",
            "kepler: Harmonices Mundi (1619), Book IV, Ch. 1 (spherical archetype of the Trinity)",
        ],
        "symbolic_hook": "geometor.cusa.polygon_exhaustion_and_complementa.construct_generative_unfolding",
    },
    {
        "id": "cusa:ddi:II.11-12",
        "locus": "De Docta Ignorantia II.11–12 (Corollaria de motu & De condicionibus terrae)",
        "unit": "unit-5-cosmologia-complementa",
        "theme": "Decentered Universe, Perspectival Relativity of Motion & the Noble Moving Earth",
        "ancient_medieval_links": [
            "plato: Timaeus 30b, 34a–b, 40b–c (world as living organism & axial/cosmic motions)",
            "aristotle: De Caelo II.13–14, 293a15–298a20 (geocentric rest refuted by Cusa)",
        ],
        "renaissance_modern_links": [
            "kepler: Astronomia Nova (1609) & Epitome Astronomiae Copernicanae (1618) (optical relativity of motion & celestial physics)",
            "klein: Erlangen Program (invariance under change of observer frame)",
        ],
        "symbolic_hook": "geometor.cusa.polygon_exhaustion_and_complementa.construct_cosmic_relativity_frame",
    },
    {
        "id": "cusa:transmut:1445:9-11",
        "locus": "De Geometricis Transmutationibus (1445), §§1–5, 9–11",
        "unit": "unit-5-cosmologia-complementa",
        "theme": "Quarter-Side Sesquiquarta (5:4) Rectification of the Inscribed Equilateral Triangle",
        "ancient_medieval_links": [
            "euclid: Elements IV.2, IV.4 & I.47 (inscribed triangle, incircle, and Pythagorean quadrance Q(A,E)=7/16)",
            "archimedes: Dimensio Circuli Prop. 3 (pi < 22/7; Cusa obtains 24*sqrt(21)/35 ~= 3.142337 < 22/7)",
        ],
        "renaissance_modern_links": [
            "durer: Underweysung der Messung (1525), Book II (compass-and-straightedge approximate quadratures)",
            "wildberger: Divine Proportions (2005) (exact rational quadrance Q(A,H)=175/256)",
        ],
        "symbolic_hook": "geometor.cusa.polygon_exhaustion_and_complementa.construct_transmutatio_isoperimetra",
    },
    {
        "id": "cusa:compl:1453:1-10",
        "locus": "De Mathematicis Complementis (1453), §§1–10",
        "unit": "unit-5-cosmologia-complementa",
        "theme": "Critique of Archimedes' Spiral & Theory of Prima Linea (Inradius) and Secunda Linea (Circumradius)",
        "ancient_medieval_links": [
            "archimedes: De Lineis Spiralibus Prop. 18 & Dimensio Circuli Prop. 1",
            "euclid: Elements VI.13 (mean proportional squaring rectangle r * (P/2))",
        ],
        "renaissance_modern_links": [
            "regiomontanus: De Quadratura Circuli (1464/1533) (trigonometric audit of Cusa's polygon interpolations)",
        ],
        "symbolic_hook": "geometor.cusa.polygon_exhaustion_and_complementa.compute_polygon_exhaustion_table",
    },
    {
        "id": "cusa:aurea:1458-1459",
        "locus": "De Mathematica Perfectione (1458) §§1–6 & Aurea Propositio in Mathematicis (1459) §§1–7",
        "unit": "unit-5-cosmologia-complementa",
        "theme": "Three-Ray Chord–Arc–Tangent Invariance & Fifth-Order Snellius–Cusa Rectification Law",
        "ancient_medieval_links": [
            "euclid: Elements III.16, III.18 & VI.4 (similar right triangles equating chord and tangent three-ray ratios)",
            "archimedes: Dimensio Circuli Prop. 3 (half-angle bisection improved from O(theta^3) to O(theta^5))",
        ],
        "renaissance_modern_links": [
            "snellius & huygens: Cyclometricus (1621) & De Circuli Magnitudine Inventa (1654) (theta - 3 sin theta / (2 + cos theta) = theta^5/180 + O(theta^7))",
        ],
        "symbolic_hook": "geometor.cusa.polygon_exhaustion_and_complementa.construct_aurea_propositio",
    },
]


def render_concordance_rst() -> str:
    """Render ``docsrc/de_docta_ignorantia/concordance.rst``."""
    lines = [
        ":order: 90",
        ":layout: book",
        ":type: apparatus",
        ":title: Cross-Corpus Concordance",
        "",
        ".. _concordance:",
        "",
        "========================",
        "Cross-Corpus Concordance",
        "========================",
        "",
        ".. rubric:: Linking Cusanus (1440–1459) to Ancient, Scholastic, Renaissance & Modern Geometry",
        "",
        (
            f"Systematic concordance of **{len(CONCORDANCE_ENTRIES)} canonical loci** across "
            "*De Docta Ignorantia* and Cusa's *Scripta Mathematica*, cross-referenced to "
            "``plato``, ``aristotle``, ``euclid``/``elements``, ``archimedes``, ``proclus``, "
            "``aquinas``, ``hoenen``, ``pacioli``, ``durer``, ``kepler``, ``casey``, "
            "``klein``, and ``wildberger``."
        ),
        "",
    ]

    for entry in CONCORDANCE_ENTRIES:
        heading = f"{entry['locus']}"
        lines.extend(
            [
                f".. _{entry['id'].replace(':', '-')}:",
                "",
                heading,
                "-" * len(heading),
                "",
                f"- **Codex Unit**: :doc:`{entry['unit']}/{entry['unit']}-en`",
                f"- **Central Thesis**: {entry['theme']}",
                f"- **Symbolic Verification Hook**: ``{entry['symbolic_hook']}``",
                "",
                "**Ancient & Medieval Antecedents**",
                "",
            ]
        )
        for item in entry["ancient_medieval_links"]:
            lines.append(f"- {item}")
        lines.extend(
            [
                "",
                "**Renaissance & Modern Mathematical Reception**",
                "",
            ]
        )
        for item in entry["renaissance_modern_links"]:
            lines.append(f"- {item}")
        lines.append("")

    return "\n".join(lines)


def write_concordance_artifacts(repo_root: str | Path) -> dict[str, Path]:
    """Write ``concordance.json`` to ``resources/`` & ``resources/cusa/`` and ``concordance.rst``."""
    root = Path(repo_root)
    written: dict[str, Path] = {}
    payload = {
        "corpus": "geometor-cusa",
        "count": len(CONCORDANCE_ENTRIES),
        "entries": CONCORDANCE_ENTRIES,
    }
    for folder in (root / "resources", root / "resources" / "cusa"):
        folder.mkdir(parents=True, exist_ok=True)
        target = folder / "concordance.json"
        target.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        written[str(target.relative_to(root))] = target

    rst_path = root / "docsrc" / "de_docta_ignorantia" / "concordance.rst"
    rst_path.parent.mkdir(parents=True, exist_ok=True)
    rst_path.write_text(render_concordance_rst(), encoding="utf-8")
    written[str(rst_path.relative_to(root))] = rst_path
    return written

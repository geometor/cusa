"""Scholarly apparatus registries (glossary, persons, bibliography) for *geometor-cusa*.

Exports canonical JSON dictionaries to ``resources/`` and ``resources/cusa/`` for
``photon-platform/publish`` inline roles (``:term:``, ``:person:``, ``:cite:``) and
compiles ``glossary.rst``, ``persons.rst``, and ``bibliography.rst`` for the Book Codex.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

__all__ = [
    "CITATIONS_DATA",
    "GLOSSARY_DATA",
    "PERSONS_DATA",
    "render_bibliography_rst",
    "render_glossary_rst",
    "render_persons_rst",
    "write_apparatus_artifacts",
]

GLOSSARY_DATA: dict[str, dict[str, str]] = {
    "docta-ignorantia": {
        "headword": "docta ignorantia",
        "greek": "σοφὴ ἀμαθία / εἰδέναι ὅτι οὐκ οἶδεν",
        "latin": "docta ignorantia",
        "translation": "Learned ignorance",
        "loci": "Dedicatio; I.1; I.3; I.12; I.16–17; II.11–12; Epistola auctoris",
        "definition": (
            "Cusa's central epistemological method: rigorous mathematical and dialectical "
            "knowledge of why finite comparative reason (ratio) cannot comprehend precise "
            "infinite truth, turning that self-knowledge into intellectual vision."
        ),
    },
    "coincidentia-oppositorum": {
        "headword": "coincidentia oppositorum",
        "greek": "σύμπτωσις τῶν ἐναντίων",
        "latin": "coincidentia oppositorum / contradictoriorum",
        "translation": "Coincidence of opposites",
        "loci": "I.2; I.4; I.13–16; I.22; Epistola auctoris; De math. perf. §2",
        "definition": (
            "The noetic principle—revealed to Cusa at sea returning from Constantinople in "
            "1437/1438—that predicates opposed in the finite domain of 'more and less' "
            "(maximum/minimum, straight/curved, chord/arc, center/circumference) coincide "
            "identically in the infinite Maximum."
        ),
    },
    "maximum-absolutum": {
        "headword": "maximum absolutum",
        "greek": "τὸ ἁπλῶς μέγιστον",
        "latin": "maximum absolutum / maximum simpliciter",
        "translation": "The Absolute Maximum",
        "loci": "I.2; I.4; I.12; I.16–23",
        "definition": (
            "That than which nothing can be greater (quo nihil maius esse potest), freed "
            "from all quantitative contraction and relative opposition, in which all "
            "possibility is eternally actual and with which the Absolute Minimum coincides."
        ),
    },
    "minimum": {
        "headword": "minimum",
        "greek": "τὸ ἐλάχιστον",
        "latin": "minimum",
        "translation": "The Minimum",
        "loci": "I.2; I.4; I.13; II.11; De math. perf. §§3–4",
        "definition": (
            "That than which nothing can be lesser; when abstracted from finite quantity, "
            "the superlative minimum coincides with the superlative maximum, and in Cusa's "
            "1458 calculus of chords the unassignable minimal chord coincides with its arc."
        ),
    },
    "proportio": {
        "headword": "proportio / habitudo",
        "greek": "λόγος / ἀναλογία",
        "latin": "proportio / comparativa proportio / habitudo",
        "translation": "Proportion / Comparative ratio",
        "loci": "I.1; I.3; I.11; De geom. trans. §§4–11; Aurea prop. §§1–7",
        "definition": (
            "Simultaneous agreement in one respect and alterity in another, presupposing "
            "number; all finite inquiry proceeds by comparative proportion from the known "
            "to the unknown, whereas the infinite escapes all finite proportion (infiniti "
            "ad finitum proportionem non esse)."
        ),
    },
    "transsumptio": {
        "headword": "transsumptio",
        "greek": "μετάληψις / ἀναγωγή",
        "latin": "transsumptio / translative ascendere",
        "translation": "Mathematical transsumption (three-step ascent)",
        "loci": "I.12; I.16; I.19; I.21; I.23",
        "definition": (
            "Cusa's three-stage symbolic method in Book I, Chapter 12: (1) inspect finite "
            "mathematical figures and their demonstrated invariants; (2) transfer those "
            "relations to corresponding infinite figures; (3) transsume them beyond all "
            "figure to the simple Infinite."
        ),
    },
    "mathematicalia": {
        "headword": "mathematicalia",
        "greek": "τὰ μαθηματικά",
        "latin": "mathematicalia / signa mathematicalia",
        "translation": "Mathematical objects and signs",
        "loci": "I.11–12",
        "definition": (
            "Abstract intelligible figures free from the fluctuating material instability "
            "of sensible bodies while retaining imaginative clarity, giving them 'incorruptible "
            "certainty' (incorruptibilis certitudo) as symbols of divine truth."
        ),
    },
    "linea-infinita": {
        "headword": "linea infinita",
        "greek": "ἄπειρος γραμμή",
        "latin": "linea maxima et infinita",
        "translation": "The infinite line",
        "loci": "I.13–19; I.23",
        "definition": (
            "Cusa's primary geometric paradigm: an uncontracted straight line that is "
            "actually triangle, circle, and sphere, indivisible yet the exact ratio and "
            "measure (adaequatissima mensura) of every finite straight and curved line."
        ),
    },
    "circulus-infinitus": {
        "headword": "circulus infinitus",
        "greek": "ἄπειρος κύκλος",
        "latin": "circulus maximus et infinitus",
        "translation": "The infinite circle",
        "loci": "I.12–13; I.15; I.21; Aurea prop. §3",
        "definition": (
            "Limit of coaxial circles of increasing radius: as diameter grows without bound, "
            "curvature (1/R) vanishes so the circumference is minimally curved and maximally "
            "straight, coinciding with its tangent line and identifying center, diameter, "
            "and circumference."
        ),
    },
    "triangulus-infinitus": {
        "headword": "triangulus infinitus",
        "greek": "ἄπειρον τρίγωνον",
        "latin": "triangulus maximus et infinitus",
        "translation": "The infinite triangle",
        "loci": "I.12; I.14–15; I.19",
        "definition": (
            "Limit of a triangle whose apex angle opens toward two right angles (180°, "
            "spread s_C -> 0) or whose base becomes infinite: without composition of parts, "
            "its three sides and three angles are one simple infinite line (*unitrinum*)."
        ),
    },
    "sphaera-infinita": {
        "headword": "sphaera infinita",
        "greek": "ἄπειρος σφαῖρα",
        "latin": "sphaera maxima et infinita",
        "translation": "The infinite sphere",
        "loci": "I.12–13; I.15; I.23; II.11–12",
        "definition": (
            "Ultimate actuality of the line's generative unfolding by semicircle revolution, "
            "in which length, breadth, and depth concur and center, diameter, and "
            "circumference are identical."
        ),
    },
    "polygonia": {
        "headword": "polygonia",
        "greek": "πολύγωνον",
        "latin": "polygonia inscripta / isopleura / isoperimetra",
        "translation": "Regular / isoperimetric polygon",
        "loci": "I.3; De geom. trans. §§4–11; De math. compl. §§4–10",
        "definition": (
            "Multi-angled rectilinear figure whose inscribed multiplication of sides "
            "approaches circularity monotonically without ever attaining exact algebraic "
            "identity with the indivisible circle unless resolved into circularity itself."
        ),
    },
    "curvitas-et-rectitudo": {
        "headword": "curvitas & rectitudo",
        "greek": "καμπυλότης καὶ εὐθύτης",
        "latin": "curvitas / rectitudo",
        "translation": "Curvature and straightness",
        "loci": "I.12–13; I.16; I.18; De geom. trans. §§2–3",
        "definition": (
            "Classic Aristotelian-Euclidean contraries (cf. Parmenides 137e, Aristotle "
            "Physics VII.4): Cusa argues that finite curvature admits 'more and less' by "
            "participating indivisible rectitude, with which minimal curvature coincides."
        ),
    },
    "sagitta": {
        "headword": "sagitta",
        "greek": "βέλος / κάθετος",
        "latin": "sagitta (versed sine)",
        "loci": "I.13; De math. perf. §§3–4",
        "translation": "Sagitta (arc-to-chord rise)",
        "definition": (
            "Perpendicular rise h(x, R) = R - sqrt(R^2 - x^2) = x^2 / (R + sqrt(R^2 - x^2)) "
            "between chord and arc; vanishes at O(1/R) as R -> oo and at O(theta^2) as "
            "theta -> 0."
        ),
    },
    "chorda-et-arcus": {
        "headword": "chorda & arcus",
        "greek": "χορδὴ καὶ περιφέρεια",
        "latin": "chorda / semichorda / arcus / semiarcus",
        "translation": "Chord and circular arc",
        "loci": "I.13; I.15; De math. perf. §§2–6; Aurea prop. §§1–6",
        "definition": (
            "Rectilinear subtense versus curved circular portion; their ratio sin(theta)/theta "
            "is approximated to fifth order by Cusa's harmonic-radial formula 3 / (2 + cos theta)."
        ),
    },
    "prima-et-secunda-linea": {
        "headword": "prima & secunda linea",
        "greek": "κάθετος ἐγγεγραμμένου / ἐκκέντρου",
        "latin": "prima linea (inradius) / secunda linea (circumradius)",
        "translation": "First line (inradius) & second line (circumradius)",
        "loci": "De math. compl. §§4–10; De math. perf. §§5–6",
        "definition": (
            "In De mathematicis complementis (1453), Cusa names the apothem from center to "
            "side-midpoint the 'first line' (r_n = cos(pi/n)) and the vertex radius the "
            "'second line' (R_n); maximally distinct in the equilateral triangle, they "
            "coincide in the circle."
        ),
    },
    "proportio-sesquiquarta": {
        "headword": "proportio sesquiquarta",
        "greek": "ἐπιτέταρτος λόγος (5:4)",
        "latin": "proportio sesquiquarta",
        "translation": "Sesquiquarta ratio (5 : 4)",
        "loci": "De geom. trans. §§9–10",
        "definition": (
            "Superparticular ratio 5:4 by which Cusa extends ray AE (from center A to the "
            "quarter-division point E of inscribed equilateral triangle side BC) to AH = "
            "5*sqrt(7)/16, implying pi_Cusa = 24*sqrt(21)/35 ~= 3.142337."
        ),
    },
    "isoperimetra": {
        "headword": "isoperimetra",
        "greek": "ἰσοπερίμετρος",
        "latin": "figura isoperimetra",
        "translation": "Isoperimetric figure (equal perimeter)",
        "loci": "De geom. trans. §§4–11; De math. compl. §§5–8",
        "definition": (
            "Figures sharing an identical perimeter: Cusa invokes Zenodorus's and Pappus's "
            "isoperimetric hierarchy from the minimum-capacity equilateral triangle up to "
            "the maximum-capacity circle."
        ),
    },
    "quadratura-et-rectilineatio": {
        "headword": "quadratura circuli & rectilineatio curvae",
        "greek": "τετραγωνισμὸς τοῦ κύκλου",
        "latin": "quadratura circuli / rectilineatio curvae",
        "translation": "Quadrature of the circle & rectification of the curve",
        "loci": "De geom. trans. §§2–10; De math. compl. §§1–8; Aurea prop. §§1–6",
        "definition": (
            "Constructing a square equal in area to a circle or a straight segment equal "
            "in length to an arc; via Archimedes' Dimensio circuli Prop. 1 and Euclid VI.13, "
            "Cusa reduces area quadrature directly to perimeter rectification."
        ),
    },
    "ratio-et-intellectus": {
        "headword": "ratio vs. intellectus",
        "greek": "διάνοια vs. νοῦς",
        "latin": "ratio / discursus vs. intellectus / visio intellectualis",
        "translation": "Discursive reason vs. intellectual vision",
        "loci": "I.4; I.12; I.14; II.11; De math. perf. §§3–4",
        "definition": (
            "Discursive ratio enforces the Aristotelian principle of non-contradiction "
            "among finite magnitudes, whereas higher intellectus beholds the coincidence "
            "of opposites prior to contraction."
        ),
    },
    "complicatio-et-explicatio": {
        "headword": "complicatio & explicatio",
        "greek": "συναίρεσις καὶ ἀνάπτυξις",
        "latin": "complicatio / explicatio",
        "translation": "Enfolding and unfolding",
        "loci": "I.13–16; I.22–23; II.3; II.11",
        "definition": (
            "As unity enfolds all number and the point/infinite line enfolds triangle, "
            "circle, and sphere while finite figures unfold that potency successively, "
            "God is the complicatio omnium and the cosmos their explicatio."
        ),
    },
    "contractio": {
        "headword": "contractio",
        "greek": "συστολή / μέθεξις",
        "latin": "contractio / maximum contractum",
        "translation": "Ontological contraction",
        "loci": "I.2; I.4; II.2; II.4; II.11–12",
        "definition": (
            "Restriction of infinite unity or rectitude to a determinate finite degree, "
            "species, place, and motion; the physical universe is the 'contracted Maximum' "
            "subsisting solely in plurality."
        ),
    },
    "mensura": {
        "headword": "mensura adaequatissima",
        "greek": "μέτρον ἀκριβέστατον",
        "latin": "adaequatissima mensura / metrum et mensura",
        "translation": "Most adequate / exact measure",
        "loci": "I.16–18; I.21; I.23",
        "definition": (
            "Expanding Aristotle Metaphysics X.1 (1052b18), Cusa demonstrates that only "
            "where Maximum and Minimum coincide can one simple essence measure every large "
            "and small finite entity without defect or excess."
        ),
    },
    "unitrinum": {
        "headword": "unitrinum / triunum",
        "greek": "τριὰς ἐν μονάδι",
        "latin": "unitrinum / triunum",
        "translation": "Unitrine / Triune principle",
        "loci": "I.19; II.11; Aurea prop. §7",
        "definition": (
            "Coincidence of unity and trinity prior to numerical counting, symbolized both "
            "by the infinite line that is three angles/sides in one and by the three rays "
            "of Aurea propositio §7."
        ),
    },
    "machina-mundi": {
        "headword": "machina mundi",
        "greek": "κόσμου σύστημα",
        "latin": "machina mundi / machina mundana",
        "translation": "Fabric / architecture of the universe",
        "loci": "II.11–12",
        "definition": (
            "Cusa's decentered physical cosmos—neither absolutely infinite nor enclosed "
            "within a fixed physical sphere—whose center is everywhere and circumference "
            "nowhere (quasi habens undique centrum et nullibi circumferentiam)."
        ),
    },
    "coniectura": {
        "headword": "coniectura",
        "greek": "στοχασμός / εἰκασία",
        "latin": "coniectura",
        "translation": "Conjecture (participative approximation)",
        "loci": "II.11; De math. perf. §1",
        "definition": (
            "Positive human assertion participating truth in otherness: all astronomical "
            "measurements of poles, centers, and orbital periods remain conjectural because "
            "no physical body moves around an immobile mathematical point."
        ),
    },
}

PERSONS_DATA: dict[str, dict[str, str]] = {
    "cusanus": {
        "name": "Nicholas of Cusa (Nicolaus Cusanus / Nikolaus Krebs von Kues)",
        "dates": "1401 – August 11, 1464",
        "role": "German Cardinal, Philosopher, Canonist & Speculative Geometer",
        "bio": (
            "Born at Kues on the Moselle, educated at Heidelberg, Padua (where he befriended "
            "Paolo dal Pozzo Toscanelli), and Cologne; author of De docta ignorantia (1440), "
            "De coniecturis (c. 1442), and eleven mathematical treatises (1445–1459) uniting "
            "coincidence of opposites, projective limits, and decentered cosmology."
        ),
    },
    "cesarini": {
        "name": "Cardinal Julian Cesarini (Iulianus Caesarinus)",
        "dates": "1398 – November 10, 1444",
        "role": "Papal Legate, Teacher of Cusa at Padua & Dedicatee of De Docta Ignorantia",
        "bio": (
            "Humanist canonist who taught Cusa at Padua and presided at the Council of Basel; "
            "dedicated recipient of both De docta ignorantia (1440) and De coniecturis."
        ),
    },
    "toscanelli": {
        "name": "Paolo dal Pozzo Toscanelli (Paulus physicus Florentinus)",
        "dates": "1397 – May 10, 1482",
        "role": "Florentine Mathematician, Physician, Astronomer & Lifelong Friend of Cusa",
        "bio": (
            "Fellow student of Cusa at Padua, advisor to Brunelleschi and Columbus, dedicatory "
            "recipient of De geometricis transmutationibus (1445), and interlocutor of Cusa's "
            "1457 Dialogus de circuli quadratura; stood at Cusa's deathbed at Todi in 1464."
        ),
    },
    "nicholas-v": {
        "name": "Pope Nicholas V (Tommaso Parentucelli)",
        "dates": "1397 – March 24, 1455",
        "role": "Humanist Pope, Founder of the Vatican Library & Dedicatee of De Mathematicis Complementis",
        "bio": (
            "Commissioned Jacobus Cremonensis's Latin translation of Archimedes' Opera and "
            "presented it directly to Cardinal Nicholas of Cusa in 1453, inspiring De "
            "mathematicis complementis."
        ),
    },
    "cerda": {
        "name": "Cardinal Antonio Cerdá y Lloscos",
        "dates": "1390 – September 12, 1459",
        "role": "Cardinal Priest of S. Grisogono, Scholastic Theologian & Dedicatee of De Mathematica Perfectione",
        "bio": (
            "Majorcan theologian and friend of Cusa to whom Cusa dedicated De mathematica "
            "perfectione (1458) along with De beryllo."
        ),
    },
    "pythagoras": {
        "name": "Pythagoras of Samos",
        "dates": "c. 570 – c. 495 BC",
        "role": "Founder of Harmonic & Arithmetical Philosophy",
        "bio": (
            "Honored in De docta ignorantia I.1 and I.11 as 'first philosopher in name and "
            "deed' for grounding all comparative proportion and inquiry in number."
        ),
    },
    "socrates": {
        "name": "Socrates of Athens",
        "dates": "469 – 399 BC",
        "role": "Exemplar of Self-Critical Ignorance",
        "bio": (
            "Cited in De docta ignorantia I.1 as knowing nothing save that he did not know, "
            "anticipating Cusa's methodological docta ignorantia."
        ),
    },
    "plato": {
        "name": "Plato of Athens",
        "dates": "428/427 – 348/347 BC",
        "role": "Founder of the Academy & Author of Meno, Republic, Parmenides & Timaeus",
        "bio": (
            "Cited across I.11, I.17 (via Calcidius), and II.12; Cusa's three-step mathematical "
            "transsumption transforms Republic VI–VII's Divided Line and Parmenides 137e on "
            "straight and round (geometor/plato)."
        ),
    },
    "aristotle": {
        "name": "Aristotle of Stagira",
        "dates": "384 – 322 BC",
        "role": "Author of the Metaphysics, Physics, De Anima & De Caelo",
        "bio": (
            "Cited in I.1 (owl before the sun, Metaph. II.1), I.11 (species as numbers; "
            "triangle in quadrangle, De Anima II.3), I.17 (first as measure, Metaph. X.1), "
            "and I.18 (straight as measure of itself and the curved, De Anima I.5), while "
            "his fixed-center geocentrism is overturned in II.11–12 (geometor/aristotle)."
        ),
    },
    "euclid": {
        "name": "Euclid of Alexandria",
        "dates": "fl. c. 300 BC",
        "role": "Author of the Elements",
        "bio": (
            "Supplies the geometric foundations of Cusa's demonstrations: triangle inequality "
            "(I.20), angle sum of two right angles (I.32), greater side opposite greater angle "
            "(I.18–19), tangent perpendicularity (III.16, III.18), inscribed polygons (Book IV), "
            "and mean proportional quadrature (VI.13; Cusa cites Campanus's numbering VI.9) "
            "(geometor/euclid, geometor/elements)."
        ),
    },
    "archimedes": {
        "name": "Archimedes of Syracuse",
        "dates": "c. 287 – 212 BC",
        "role": "Author of Measurement of a Circle & On Spirals",
        "bio": (
            "Studied intensely by Cusa in Jacobus Cremonensis's 1450s Latin translation; "
            "De mathematicis complementis §§2–3 & §8 engage Dimensio circuli Prop. 1 and "
            "critique the kinematic postulate of De lineis spiralibus."
        ),
    },
    "proclus": {
        "name": "Proclus Diadochus",
        "dates": "412 – 485 CE",
        "role": "Neoplatonic Commentator on Euclid Book I & Plato's Parmenides",
        "bio": (
            "Cusa owned and heavily annotated manuscripts of Proclus's Commentary on the "
            "Parmenides and Elements; Proclus's ontology of mathematicals in the imagination "
            "directly parallels De docta ignorantia I.11–12 (geometor/proclus)."
        ),
    },
    "dionysius": {
        "name": "Pseudo-Dionysius the Areopagite",
        "dates": "fl. c. 500 CE",
        "role": "Author of Mystical Theology & On Divine Names",
        "bio": (
            "Cited repeatedly in I.16–18 for apophatic theology ('theology is simultaneously "
            "maximal and minimal') and supersubstantiality above affirmation and negation."
        ),
    },
    "augustine": {
        "name": "Aurelius Augustinus (St. Augustine of Hippo)",
        "dates": "354 – 430 CE",
        "role": "Patristic Philosopher of Divine Number & Trinity",
        "bio": (
            "Cited in I.11 for De quantitate animae's geometric method and in I.19 for "
            "'When you begin to number the Trinity, you depart from the truth.'"
        ),
    },
    "boethius": {
        "name": "Anicius Manlius Severinus Boethius",
        "dates": "c. 477 – 524 CE",
        "role": "Author of De Institutione Arithmetica & De Trinitate",
        "bio": (
            "Praised in I.11 as 'most learned of the Romans' for teaching that all truth is "
            "comprehended in multitude and magnitude (Quadrivium)."
        ),
    },
    "anselm": {
        "name": "St. Anselm of Canterbury",
        "dates": "1033 – 1109",
        "role": "Author of the Proslogion & De Veritate",
        "bio": (
            "Inspires both I.2's formula of the Maximum (quo nihil maius esse potest) and "
            "I.12's comparison of supreme Truth to infinite rectitude (rectitudo infinita)."
        ),
    },
    "aquinas": {
        "name": "St. Thomas Aquinas",
        "dates": "1225 – 1274",
        "role": "Scholastic Philosopher of Mathematical Abstraction & Judgment",
        "bio": (
            "Articulated the threefold degree of abstraction and intelligible matter (In "
            "Boethium de Trinitate q. 5–6), against whose strict Aristotelian non-contradiction "
            "in finite ratio Cusa distinguishes higher intellectus (geometor/aquinas)."
        ),
    },
    "regiomontanus": {
        "name": "Johannes Müller von Königsberg (Regiomontanus)",
        "dates": "1436 – 1476",
        "role": "Renaissance Trigonometrician & Critic of Cusa's Quadratures",
        "bio": (
            "In De triangulis et quadratura circuli (composed 1464, printed 1533), subjected "
            "Cusa's algebraic rectifications to rigorous trigonometric error bounds using "
            "Archimedes' 96-gon inequalities, proving their non-exactness while confirming "
            "their remarkable numerical accuracy."
        ),
    },
    "pacioli": {
        "name": "Fra Luca Pacioli",
        "dates": "c. 1447 – 1517",
        "role": "Author of Summa de Arithmetica & De Divina Proportione (1509)",
        "bio": (
            "Shared Cusa's mathematical-theological conviction that irrational geometric "
            "proportion reveals divine unity, trinity, and incommensurability (geometor/pacioli)."
        ),
    },
    "durer": {
        "name": "Albrecht Dürer",
        "dates": "1471 – 1528",
        "role": "Author of Underweysung der Messung (1525)",
        "bio": (
            "Transmitted Renaissance constructive transmutations of curved and rectilinear "
            "magnitudes into German workshop geometry within a decade of Faber Stapulensis's "
            "1514 edition of Cusa."
        ),
    },
    "kepler": {
        "name": "Johannes Kepler",
        "dates": "1571 – 1630",
        "role": "Imperial Mathematician & Author of Mysterium Cosmographicum (1596)",
        "bio": (
            "Hailed Nicholas of Cusa in Mysterium Cosmographicum Chapter II as 'divinus mihi "
            "Cusanus' explicitly for Cusa's transsumption of curved and straight as the "
            "archetypal symbol of Creator and created cosmos, and adopted Cusa's Principle "
            "of Continuity in Ad Vitellionem Paralipomena (1604) on conic foci at infinity."
        ),
    },
    "snellius": {
        "name": "Willebrord Snellius & Christiaan Huygens",
        "dates": "1580–1626 / 1629–1695",
        "role": "Seventeenth-Century Provers of the Cusa–Snellius–Huygens Inequality",
        "bio": (
            "Snellius rediscovered Cusa's 1458–1459 formula theta ~= 3 sin(theta)/(2 + cos theta) "
            "in Cyclometricus (1621), and Huygens rigorously proved in De circuli magnitudine "
            "inventa (1654) that it forms a strict fifth-order lower bound on arc length."
        ),
    },
    "klein": {
        "name": "Jean-Victor Poncelet, John Casey & Felix Klein",
        "dates": "1788–1867 / 1820–1891 / 1849–1925",
        "role": "Architects of Projective Continuity, Circle Inversion & Erlangen Geometry",
        "bio": (
            "Provided the modern synthetic and analytic realization of Cusa's I.13–14 "
            "theorems through points at infinity, Möbius circle inversion, and projective "
            "degeneration of conics and triangles."
        ),
    },
    "wildberger": {
        "name": "Norman J. Wildberger",
        "dates": "b. 1955",
        "role": "Founder of Rational Trigonometry (Divine Proportions, 2005)",
        "bio": (
            "Replaces transcendental distance and angle by algebraic quadrance Q and spread s; "
            "under Rational Trigonometry, Cusa's I.14 flattening triangle exhibits pure "
            "rational spread s_A = 4n^2/(n^2+1)^2 -> 0 and Triple Quad residual 16/n^2 -> 0 "
            "(geometor/wildberger)."
        ),
    },
    "hoenen": {
        "name": "Petrus H. J. Hoenen, S.J.",
        "dates": "1880 – 1961",
        "role": "Author of De Noetica Geometriae (1954)",
        "bio": (
            "Analyzed geometric abstraction and intellectual judgment of necessity from "
            "singular phantasmata, illuminating Cusa's contrast between sensible imagination "
            "and visio intellectualis (geometor/hoenen)."
        ),
    },
    "klibansky": {
        "name": "Jacques Lefèvre d'Étaples, Paolo Rotta & Raymond Klibansky",
        "dates": "c. 1455–1536 / 1873–1962 / 1905–2005",
        "role": "Critical Editors of De Docta Ignorantia (Paris 1514, Bari 1913, Leipzig 1932)",
        "bio": (
            "Lefèvre d'Étaples (Faber Stapulensis) edited the monumental 1514 Paris Opera; "
            "Rotta produced the 1913 Laterza text; Klibansky's handwritten collations in his "
            "personal copy of Rotta (now at McGill Library) prepared the 1932 Heidelberg "
            "Academy edition (h I) and restored Rotta's eye-skip omissions in I.13 and I.14."
        ),
    },
}

CITATIONS_DATA: dict[str, dict[str, str]] = {
    "cusa:ddi:1440": {
        "author": "Nicolaus Cusanus",
        "work": "De Docta Ignorantia Libri Tres (completed at Kues, February 12, 1440)",
        "locus": "Dedicatio; Lib. I, Caps. 1–26; Lib. II, Caps. 1–13; Lib. III, Caps. 1–12; Epistola auctoris",
        "notes": "Foundational treatise introducing learned ignorance, coincidence of opposites, infinite geometric figures, and the decentered moving Earth.",
    },
    "cusa:transmut:1445": {
        "author": "Nicolaus Cusanus",
        "work": "De Geometricis Transmutationibus, ad Paulum Dominici Florentinum (1445)",
        "locus": "§§1–36 (esp. §§1–11)",
        "notes": "Introduces Cusa's compass-and-straightedge quarter-side sesquiquarta (5:4) rectification of the inscribed equilateral triangle, yielding pi_Cusa = 24*sqrt(21)/35.",
    },
    "cusa:compl:1453": {
        "author": "Nicolaus Cusanus",
        "work": "De Mathematicis Complementis, ad Nicolaum V Pontificem Maximum (1453–1454)",
        "locus": "Lib. I–II (esp. Dedicatio §§1–3 & §§4–10)",
        "notes": "Written upon receiving Archimedes' Opera in Latin from Pope Nicholas V; develops the theory of prima linea (inradius) and secunda linea (circumradius) across isoperimetric polygons.",
    },
    "cusa:perf:1458": {
        "author": "Nicolaus Cusanus",
        "work": "De Mathematica Perfectione, ad Antonium Cardinalem S. Chrysogoni (1458)",
        "locus": "Dedicatio & §§1–24",
        "notes": "Derives from the coincidence of minimal chord and minimal arc the fifth-order harmonic rectification hc : bc ~= 3*ac : (2*ac + ab).",
    },
    "cusa:aurea:1459": {
        "author": "Nicolaus Cusanus",
        "work": "R. D. N. Cardinalis S. Petri in Mathematicis Aurea Propositio (Rome, August 8, 1459)",
        "locus": "§§1–7 & Colophon",
        "notes": "Cusa's crowning three-ray formulation equating endpoint ascent and midpoint descent (theta ~= 3 sin theta / (2 + cos theta), residual theta^5/180).",
    },
    "cusa:paris:1514": {
        "author": "Nicolaus Cusanus (ed. Jacques Lefèvre d'Étaples / Faber Stapulensis)",
        "work": "Haec accurata recognitio trium voluminum operum Clariss. P. Nicolai Cusae Cardinalis (Paris: Jodocus Badius Ascensius, 1514)",
        "locus": "Vol. I (De docta ignorantia); Vol. II, fols. 33r–114v (Mathematica)",
        "notes": "Monumental Renaissance humanist edition preserving full mathematical woodcuts and text witnesses prior to Rotta's 1913 omissions.",
    },
    "cusa:basel:1565": {
        "author": "Nicolaus Cusanus",
        "work": "Nicolai de Cusa Cardinalis, utriusque iuris doctoris, in omnique philosophia incomparabilis viri, Opera, 3 vols. (Basel: Ex Officina Henricpetrina, August 1565)",
        "locus": "pp. 1–75 (DDI), pp. 939–966 (Transmut.), pp. 1005–1090 (Compl.), pp. 1120–1136 (Perf.)",
        "notes": "Standard early modern Basel edition read by Giordano Bruno, Johannes Kepler, and Willebrord Snellius.",
    },
    "cusa:rotta:1913": {
        "author": "Nicolaus Cusanus (ed. Paolo Rotta)",
        "work": "Nicolai Cusani De Docta Ignorantia Libri Tres (Bari: Gius. Laterza & Figli, Classici della Filosofia Moderna 19, 1913)",
        "locus": "pp. 1–189",
        "notes": "Early twentieth-century critical edition; McGill Library holds Raymond Klibansky's annotated copy recording Rotta's homeoteleuton omissions at p. 28 (I.13) and p. 31 (I.14).",
    },
    "cusa:heidelberg:1932": {
        "author": "Nicolaus Cusanus (eds. Ernst Hoffmann & Raymond Klibansky)",
        "work": "Nicolai de Cusa Opera Omnia, iussu et auctoritate Academiae Litterarum Heidelbergensis, Vol. I: De Docta Ignorantia (Leipzig: Felix Meiner, 1932)",
        "locus": "h I, pp. 1–163",
        "notes": "Reference critical apparatus establishing the manuscript stemma (Codex Cusanus 218 et al.).",
    },
    "cusa:folkerts:2010": {
        "author": "Nicolaus Cusanus (ed. Menso Folkerts)",
        "work": "Nicolai de Cusa Opera Omnia, Vol. XX: Scripta Mathematica (Hamburg: Felix Meiner, 2010)",
        "locus": "h XX",
        "notes": "Definitive philological edition and mathematical analysis of Cusa's eleven mathematical treatises (1445–1459).",
    },
    "defelice:eos:2020": {
        "author": "De Felice, Federica (ed.)",
        "work": "Niccolò Cusano: Scritti matematici (Berlin: Max Planck Institute for the History of Science, Edition Open Sources 13, 2020)",
        "locus": "Chs. 7, 11, 16, 17",
        "notes": "Open-access edition preserving digital transcriptions and figures of Cusa's mathematical corpus.",
    },
    "hofmann:cusa:1952": {
        "author": "Hofmann, Joseph Ehrenfried (trans. Josepha Hofmann)",
        "work": "Nikolaus von Cues: Die mathematischen Schriften (Hamburg: Felix Meiner, 1952; 2nd ed. 1979)",
        "locus": "Introduction & Notes",
        "notes": "Landmark modern mathematical reconstruction of Cusa's algebraic approximations and series expansions.",
    },
    "plato:opera": {
        "author": "Plato",
        "work": "Meno (82b–85d), Republic VI–VII (509d–534e), Parmenides (137e, 145b), & Timaeus (31b–36d)",
        "locus": "Stephanus pagination",
        "notes": "Platonic foundations of recollection, mathematical dianoia vs. noesis, straight vs. round, and World-Soul harmony (geometor/plato).",
    },
    "aristotle:opera": {
        "author": "Aristotle",
        "work": "Metaphysics II.1 (993b9), X.1 (1052b18); Physics VII.4 (248a10–b7); De Anima I.5 (411a5), II.3 (414b29); De Caelo II.13–14",
        "locus": "Bekker pagination",
        "notes": "Aristotelian doctrines on the incomparability of straight and curved, unity as measure, and geocentric rest engaged and transformed by Cusa (geometor/aristotle).",
    },
    "euclid:elements": {
        "author": "Euclid",
        "work": "Elements, Books I, III, IV, VI & XII (ed. Heiberg; trans. Heath 1926)",
        "locus": "I.18–20, I.32, III.16, III.18, IV.2–15, VI.13, XII.2",
        "notes": "Classical axiomatic baseline for Cusa's triangle, tangent, polygon-exhaustion, and quadrature arguments (geometor/euclid, geometor/elements).",
    },
    "archimedes:dimensio": {
        "author": "Archimedes",
        "work": "Dimensio Circuli (Measurement of a Circle) & De Lineis Spiralibus (On Spirals)",
        "locus": "Dim. circ. Props. 1–3 (3+10/71 < pi < 3+1/7); Spir. Defs. & Prop. 18",
        "notes": "Primary ancient foil for Cusa's polygon bounds and critique of kinematic spiral rectification.",
    },
    "proclus:in-euclidem": {
        "author": "Proclus Diadochus",
        "work": "In Primum Euclidis Elementorum Librum Commentarii (ed. Friedlein 1873)",
        "locus": "Prologues I–II (pp. 3–70) & on Defs. 2–4, 15–17 (pp. 97–113, 153–162)",
        "notes": "Neoplatonic philosophy of limit/unlimited, circular simplicity, and imaginative projection studied by Cusa (geometor/proclus).",
    },
    "dionysius:mystica": {
        "author": "Pseudo-Dionysius the Areopagite",
        "work": "De Mystica Theologia, De Divinis Nominibus, & Epistola I ad Gaium",
        "locus": "MT I.1–3, V; DN I, V, XIII",
        "notes": "Apophatic theological source explicitly cited in De docta ignorantia I.16–18.",
    },
    "aquinas:boethius": {
        "author": "Thomas Aquinas",
        "work": "Expositio super Librum Boethii de Trinitate, qq. 5–6",
        "locus": "q. 5 a. 3; q. 6 a. 1–2",
        "notes": "Scholastic account of mathematical abstraction and terminatio ad imaginationem (geometor/aquinas).",
    },
    "regiomontanus:quadratura:1533": {
        "author": "Regiomontanus (Johannes Müller)",
        "work": "De Quadratura Circuli Dialogus, Secundum Nicolaum Cusensem (composed 1464; Nuremberg: Johannes Petreius, 1533)",
        "locus": "Appendix to De Triangulis Omnimodis",
        "notes": "Demonstrated by Archimedean bounds that Cusa's 1450s rectifications slightly miss exact transcendental pi while honoring their ingenuity.",
    },
    "pacioli:divina:1509": {
        "author": "Pacioli, Fra Luca",
        "work": "De Divina Proportione (Venice: Paganino Paganini, 1509)",
        "locus": "Compendio Caps. V–VII",
        "notes": "Parallels Cusa in treating irrational geometric proportion as an emblem of the incommensurable, triune Divine (geometor/pacioli).",
    },
    "durer:underweysung:1525": {
        "author": "Dürer, Albrecht",
        "work": "Underweysung der Messung, mit dem Zirckel und Richtscheyt (Nuremberg, 1525)",
        "locus": "Books I–II",
        "notes": "Applies constructive circle-quadrature and polygon transmutations in Northern Renaissance craft geometry.",
    },
    "kepler:mysterium:1596": {
        "author": "Kepler, Johannes",
        "work": "Prodromus Dissertationum Cosmographicarum, continens Mysterium Cosmographicum (Tübingen, 1596) & Ad Vitellionem Paralipomena (1604)",
        "locus": "Myst. Cosm. Cap. II; Paralipomena Cap. IV.4",
        "notes": "Celebrates 'divinus mihi Cusanus' on curved/straight symbolism and extends Cusa's coincidence into the projective continuity of conic sections.",
    },
    "snellius:huygens:1654": {
        "author": "Snellius, Willebrord & Huygens, Christiaan",
        "work": "Cyclometricus (Leiden, 1621) & De Circuli Magnitudine Inventa (Leiden: Elzevier, 1654)",
        "locus": "Huygens Props. 10–16",
        "notes": "Rediscovers and rigorously proves the fifth-order Cusa–Snellius inequality 3 sin(theta)/(2 + cos theta) < theta.",
    },
    "casey:sequel:1886": {
        "author": "Casey, John",
        "work": "A Sequel to the First Six Books of the Elements of Euclid, 4th ed. (Dublin: Hodges, Figgis & Co., 1886)",
        "locus": "Book VI, Section V (Theory of Inversion & Coaxal Circles)",
        "notes": "Synthetic theory of circle inversion and parabolic coaxial pencils formalizing Cusa's I.13 circle-line unity.",
    },
    "klein:elementary:1908": {
        "author": "Klein, Felix",
        "work": "Elementarmathematik vom höheren Standpunkte aus, Bd. II: Geometrie (Leipzig: Teubner, 1908)",
        "locus": "Part II (Projective & Möbius Transformations)",
        "notes": "Erlangen group-theoretic unification of lines and circles on the Riemann/Möbius sphere.",
    },
    "hoenen:noetica:1954": {
        "author": "Hoenen, Petrus H. J., S.J.",
        "work": "De Noetica Geometriae: Origine Theoriae Cognitionis (Rome: Analecta Gregoriana 63, 1954)",
        "locus": "Caps. I–IV, IX",
        "notes": "Epistemological study of insight into geometric necessity in concrete diagrams (geometor/hoenen).",
    },
    "wildberger:divine:2005": {
        "author": "Wildberger, Norman J.",
        "work": "Divine Proportions: Rational Trigonometry to Universal Geometry (Sydney: Wild Egg, 2005)",
        "locus": "Chs. 3–6 (Quadrance, Spread, Triple Quad & Triple Spread Formulas)",
        "notes": "Algebraic trigonometry proving pure rational convergence of Cusa's I.14 flattening triangle to collinearity (geometor/wildberger).",
    },
}


def _slug_anchor(prefix: str, key: str) -> str:
    """Convert an apparatus key into a clean RST anchor token."""
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", key).strip("-").lower()
    return f"{prefix}-{cleaned}"


def render_glossary_rst() -> str:
    """Render ``docsrc/de_docta_ignorantia/glossary.rst``."""
    lines = [
        ":order: 93",
        ":layout: book",
        ":type: apparatus",
        ":title: Glossary of Cusan Mathematical & Noetic Terms",
        "",
        ".. _glossary:",
        "",
        "=============================================",
        "Glossary of Cusan Mathematical & Noetic Terms",
        "=============================================",
        "",
        ".. rubric:: Latin, Greek & Constructive Lexicon of *De Docta Ignorantia* & *Scripta Mathematica*",
        "",
        (
            f"Systematic lexicon of **{len(GLOSSARY_DATA)} technical concepts** governing "
            "Nicholas of Cusa's *docta ignorantia*, *coincidentia oppositorum*, three-step "
            "mathematical *transsumptio*, infinite figures, decentered cosmology, and "
            "circle rectification."
        ),
        "",
    ]
    for key, entry in GLOSSARY_DATA.items():
        head = entry["headword"]
        lines.extend(
            [
                f".. _{_slug_anchor('term', key)}:",
                "",
                head,
                "-" * len(head),
                "",
                f"- **Latin**: *{entry['latin']}*  |  **Greek**: *{entry['greek']}*",
                f"- **Rendering**: {entry['translation']}",
                f"- **Primary Loci**: ``{entry['loci']}``",
                "",
                entry["definition"],
                "",
            ]
        )
    return "\n".join(lines)


def render_persons_rst() -> str:
    """Render ``docsrc/de_docta_ignorantia/persons.rst``."""
    lines = [
        ":order: 92",
        ":layout: book",
        ":type: apparatus",
        ":title: Index of Persons, Dedicatees & Geometers",
        "",
        ".. _persons:",
        "",
        "========================================",
        "Index of Persons, Dedicatees & Geometers",
        "========================================",
        "",
        ".. rubric:: Ancient Authorities, Fifteenth-Century Interlocutors & Modern Mathematical Successors",
        "",
        (
            f"Biographical register of **{len(PERSONS_DATA)} philosophers, humanists, "
            "dedicatees, geometers, astronomers, and critical editors** connected with "
            "Nicholas of Cusa's *De Docta Ignorantia* and mathematical treatises."
        ),
        "",
    ]
    for key, entry in PERSONS_DATA.items():
        heading = f"{entry['name']} ({entry['dates']})"
        lines.extend(
            [
                f".. _{_slug_anchor('person', key)}:",
                "",
                heading,
                "-" * len(heading),
                "",
                f"**{entry['role']}**",
                "",
                entry["bio"],
                "",
            ]
        )
    return "\n".join(lines)


def render_bibliography_rst() -> str:
    """Render ``docsrc/de_docta_ignorantia/bibliography.rst``."""
    lines = [
        ":order: 91",
        ":layout: book",
        ":type: apparatus",
        ":title: Bibliography & Critical Editions",
        "",
        ".. _bibliography:",
        "",
        "================================",
        "Bibliography & Critical Editions",
        "================================",
        "",
        ".. rubric:: Primary Latin Witnesses, Renaissance Printings, Critical Editions & Geometric Studies",
        "",
        (
            f"Authoritative Latin editions, classical mathematical treatises, and modern "
            f"studies (**{len(CITATIONS_DATA)} entries**) cited across ``geometor-cusa``."
        ),
        "",
    ]
    for key, entry in CITATIONS_DATA.items():
        lines.extend(
            [
                f".. _{_slug_anchor('cite', key)}:",
                "",
                f"**{entry['author']} — {entry['work']}**",
                "",
                f"- **Citation Key**: ``{key}``  |  **Locus**: ``{entry['locus']}``",
                f"- **Significance**: {entry['notes']}",
                "",
            ]
        )
    return "\n".join(lines)


def write_apparatus_artifacts(repo_root: str | Path) -> dict[str, Path]:
    """Write ``glossary.json``, ``persons.json``, ``citations.json`` & apparatus ``.rst`` pages."""
    root = Path(repo_root)
    written: dict[str, Path] = {}

    json_payloads = {
        "glossary.json": GLOSSARY_DATA,
        "persons.json": PERSONS_DATA,
        "citations.json": CITATIONS_DATA,
    }

    for filename, payload in json_payloads.items():
        for folder in (root / "resources", root / "resources" / "cusa"):
            folder.mkdir(parents=True, exist_ok=True)
            target = folder / filename
            target.write_text(
                json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            written[str(target.relative_to(root))] = target

    rst_dir = root / "docsrc" / "de_docta_ignorantia"
    rst_dir.mkdir(parents=True, exist_ok=True)
    for filename, content in (
        ("glossary.rst", render_glossary_rst()),
        ("persons.rst", render_persons_rst()),
        ("bibliography.rst", render_bibliography_rst()),
    ):
        target = rst_dir / filename
        target.write_text(content, encoding="utf-8")
        written[str(target.relative_to(root))] = target

    return written

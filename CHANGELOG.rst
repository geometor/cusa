=========
changelog
=========

0.1.3
-----
*2026-11-14*

- Standardized top-level ``About`` page (``docsrc/about/index.rst`` promoted to top header ``:order: 10``) with the three-pillar GEOMETOR semantic-extraction mission and archival provenance; retired ``docsrc/mission/`` stubs cleanly into Home and ``About``.

0.1.2
-----
*2026-11-14*

- Standardized Book Title Page, top-level Header Navigation (``Book``, ``People``, ``Bibliography``, ``Usage``), Reader's Guide (``docsrc/usage/``), featured Author/Translator profiles in ``People``, and English structural terminology.

0.1.1 (2026-11-13)
------------------

- **added**: Added track-aware primary-source folio map (``resources/cusa/folio_map.json``) resolving 248/248 folio directives and 20/20 header badges to verified Latin and English text loci across *De Docta Ignorantia* and *Scripta Mathematica*.

0.1.0 (2026-11-12)
------------------

Initial scholarly edition and exact symbolic modeling release of ``geometor-cusa`` (*De Docta Ignorantia* [1440] & *Scripta Mathematica* [1445–1459]):

* **4-Track Synchronized Book Codex** (``docsrc/de_docta_ignorantia/``, ``:layout: book``):

  - **Unit I — Maximum & Learned Ignorance** (``Dedicatio``, ``I.1–4``, ``Epistola auctoris``): Comparative proportion, the Absolute Maximum, polygon-in-circle exhaustion (``I.3``), and the *coincidentia oppositorum*.
  - **Unit II — Mathematical Signs & Transsumption** (``I.11–12``): Epistemic privilege of mathematical symbols and Cusa's three-step method of transsumption (*positio finita → transsumptio in infinitum → transitus in simplex maximum*).
  - **Unit III — Coincidence of Infinite Figures** (``I.13–15``): Coincidence of the infinite circle and tangent arc with the straight line, collapse of the flattening triangle onto the base line, and unity of the infinite line, triangle, circle, and sphere (restoring two Rotta 1913 homeoteleuton omissions via Paris 1514 / Basel 1565 and Klibansky's collation).
  - **Unit IV — The Infinite Line & Infinite Sphere** (``I.16–23``): The infinite line as *essentia* and *mensura* of all figures, participation of rectitude, Trinitarian *complicatio*/*explicatio*, and the infinite sphere (*centrum cum circumferentia coincidit*).
  - **Unit V — Perspectival Cosmology & Mathematical Complementa** (``II.11–12`` + *De Geometricis Transmutationibus* 1445, *De Mathematicis Complementis* 1453, *De Mathematica Perfectione* 1458, & *Aurea Propositio in Mathematicis* 1459): Decentered universe, relativity of motion, moving Earth, *sesquiquarta* rectification, and the fifth-order Snellius–Cusa law.

* **Exact Symbolic Geometry Engine & Interactive ``.euclid-graphic`` SVGs** (``src/geometor/cusa/``):

  - Exact SymPy ``geometor.model`` constructions (``auto_intersect=False``, zero ``sp.Float``) for coaxial tangent circle pencils and Möbius circle inversion (``coincidentia_circle_line.py``), Rational Trigonometry flattening triangles and Triple Quad Formula vanishing (``coincidentia_triangle_line.py``), regular polygon exhaustion, 1445 *sesquiquarta* rectification (:math:`\pi_{\text{Cusa}} = \frac{24\sqrt{21}}{35}`), and 1458–1459 *Aurea Propositio* fifth-order Maclaurin series residual (:math:`\theta^5 / 180`) (``polygon_exhaustion_and_complementa.py``).
  - Nine dark/light theme-adaptive ``.euclid-graphic`` SVGs in ``docsrc/_static/figures/`` and three runnable symbolic demonstration scripts in ``demos/``.

* **Cross-Corpus Concordance & Scholarly Apparatus**:

  - Comprehensive concordance linking Cusa's chapters and theorems to ``plato``, ``aristotle``, ``proclus``, ``aquinas``, ``hoenen``, ``pacioli``, ``durer``, ``kepler``, ``archimedes``, ``casey``, ``wildberger``, and ``klein``, paired with SHA-256 ``sources_manifest.json``, ``glossary.json``, ``persons.json``, and ``citations.json``.

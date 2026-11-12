===============
GEOMETOR • cusa
===============

**Nicholas of Cusa (*Nicolaus Cusanus*, 1401–1464): *De Docta Ignorantia* (1440) & *Scripta Mathematica* (1445–1459)** — Synchronized 4-Track Latin/English Digital Scriptorium Book Codex and 100% Exact Symbolic SymPy Demonstrations.

Overview
--------

``geometor/cusa`` (``geometor-cusa``) unites into a single critical edition and symbolic geometry package:

1. **Four-Track Synchronized Book Codex** (``docsrc/de_docta_ignorantia/``, ``:layout: book``):
   Every unit is presented across **English** (100% original GEOMETOR translation rendered directly from the Latin), **Latin (1440 / 1514–1913)** (collated from Rotta 1913 with Raymond Klibansky's McGill archival restorations and the 1514 Paris / 1565 Basel *Opera*), **Summary**, and **Critical Notes**:

   - **Unit I (`unit-1-maximum-ignorantia`)**: *Dedicatio*, *De Docta Ignorantia* Book I, Chapters 1–4 (*Comparative Proportion, Polygon-in-Circle Exhaustion & Coincidence of Maximum and Minimum*), and *Epistola auctoris* (Kues, February 12, 1440).
   - **Unit II (`unit-2-mathematica-transsumptio`)**: Book I, Chapters 11–12 (*Incorruptible Certitude of Mathematicalia & the Three-Step Method of Transsumptio*).
   - **Unit III (`unit-3-coincidentia-figurarum`)**: Book I, Chapters 13–15 (*Coincidence of Infinite Circle, Straight Line, Triangle & Sphere*).
   - **Unit IV (`unit-4-linea-sphaera-infinita`)**: Book I, Chapters 16–23 (*The Infinite Line as Universal Measure, Triunity vs. Quaternity & the Infinite Sphere*).
   - **Unit V (`unit-5-cosmologia-complementa`)**: Book II, Chapters 11–12 (*Centerless Cosmic Relativity & the Noble Moving Earth*) + *De Geometricis Transmutationibus* (1445), *De Mathematicis Complementis* (1453), *De Mathematica Perfectione* (1458), and the complete *Aurea Propositio in Mathematicis* (August 8, 1459).

2. **100% Exact Symbolic Geometry Engine (`src/geometor/cusa/`)**:
   Built on ``geometor.model`` with ``Model(..., auto_intersect=False)`` and **zero floating-point coordinates**:

   - **Circle–Line Coincidence & Möbius Inversion (`coincidentia_circle_line.py`)**: Exact quadratic-radical sagittae (:math:`1, 2-\sqrt{3}, 4-\sqrt{15}, 8-3\sqrt{7}`), scaling law :math:`\lim_{R\to\infty} R\,h(x,R) = x^2/2`, and conformal unit-circle inversion mapping :math:`C_R` to finite rational circles :math:`M_R = (0, -\frac{R}{2R+1})` converging to :math:`C'_\infty = (0, -\frac{1}{2})`.
   - **Triangle–Line Coincidence in Rational Trigonometry (`coincidentia_triangle_line.py`)**: Pure rational spreads :math:`s_{A_n} = \frac{4n^2}{(n^2+1)^2} \to 0`, :math:`s_B = \frac{1}{n^2+1} \to 0`, Triple Spread Formula identity, and Triple Quad collinearity residual :math:`\frac{16}{n^2} \to 0`.
   - **Polygon Exhaustion & *Scripta Mathematica* (`polygon_exhaustion_and_complementa.py`)**: Radical polygon tower (:math:`n = 3, 4, 6, 8, 12`), 1445 *sesquiquartal* rectification (:math:`\pi_{\text{Cusa}} = \frac{24\sqrt{21}}{35} \approx 3.14233762`), and 1458–1459 three-ray law :math:`\theta \approx \frac{3\sin\theta}{2+\cos\theta}` with fifth-order Maclaurin residual :math:`\frac{\theta^5}{180}`.
   - **Nine Dark/Light `.euclid-graphic` SVGs (`render.py`)**: Exported to ``docsrc/_static/figures/`` with interactive ``data-ref`` and ``data-latex-*`` attributes.

Verification & Build
--------------------

.. code-block:: bash

   # Compile all 4-track Codex units, SVGs, witness manifests & apparatus
   python -m geometor.cusa compile

   # Run standalone symbolic demonstrations
   python demos/coincidentia_circle_line.py
   python demos/coincidentia_triangle_line.py
   python demos/polygon_exhaustion_and_complementa.py

   # Lint, test & build Sphinx Book Codex
   ruff check src demos tests
   pytest -v
   publish build

License
-------

MIT License. Primary Latin witnesses are in the public domain; all English translations in ``geometor/cusa`` are 100% original GEOMETOR scholarly translations released under MIT.

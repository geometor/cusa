# GEOMETOR • cusa

Scholarly 4-track Bilingual Book Codex (*De Docta Ignorantia* [1440] & *Scripta Mathematica* [1445–1459]: collated public-domain Latin & original GEOMETOR English translation) and 100% exact SymPy / Rational Trigonometry / Möbius inversion symbolic library for **Nicholas of Cusa (*Nicolaus Cusanus*, 1401–1464)**.

---

## 1. Purpose & Scope

`geometor/cusa` (`geometor-cusa`) establishes the fifteenth-century hinge between ancient/medieval speculative geometry (`plato`, `aristotle`, `proclus`, `aquinas`, `archimedes`) and early modern projective, synthetic, and cosmological mathematics (`pacioli`, `durer`, `kepler`, `desargues`, `casey`, `klein`, `wildberger`, `hoenen`) across five 4-track Codex units:

1. **Unit I (`unit-1-maximum-ignorantia`)**: *Dedicatory Prologue* to Cardinal Julian Cesarini + *De Docta Ignorantia* Book I, Chapters 1–4 + *Author's Epistolary Colophon* (Kues, February 12, 1440) — Knowing by comparison and proportion, the Absolute Maximum, polygon-in-circle exhaustion (`I.3`), and the *coincidentia oppositorum*.
2. **Unit II (`unit-2-mathematica-transsumptio`)**: *De Docta Ignorantia* Book I, Chapters 11–12 — Why mathematical signs possess incorruptible certainty and Cusa's three-step method of **mathematical transsumption** (*mathematicalia → transsumptio in infinitum → transitus in simplex maximum*).
3. **Unit III (`unit-3-coincidentia-figurarum`)**: *De Docta Ignorantia* Book I, Chapters 13–15 — Coincidence of the infinite circle and tangent arc with the infinite straight line (`I.13`), collapse of the flattening triangle onto the infinite line (`I.14`), and unity of the infinite triangle, circle, and sphere (`I.15`).
4. **Unit IV (`unit-4-linea-sphaera-infinita`)**: *De Docta Ignorantia* Book I, Chapters 16–23 — The infinite line as *essentia* and precise measure (*mensura*) of all finite figures (`I.16–18`), Trinitarian and circular transsumption (`I.19–22`), and the infinite sphere (*centrum, diameter, et circumferentia idem sunt*, `I.23`).
5. **Unit V (`unit-5-cosmologia-complementa`)**: *De Docta Ignorantia* Book II, Chapters 11–12 (*machina mundi quasi habens undique centrum et nullibi circumferentiam*, perspectival relativity of motion, and the noble moving Earth) + Cusa's *Scripta Mathematica*: *De Geometricis Transmutationibus* (1445 `§§1–11`), *De Mathematicis Complementis* (1453 `§§1–10`), *De Mathematica Perfectione* (1458 `§§1–6`), and the complete *Aurea Propositio in Mathematicis* (Rome, August 8, 1459 `§§1–7`).

---

## 2. Key Modules (`src/geometor/cusa/`)

- `coincidentia_circle_line.py`: Exact `geometor.model.Model(..., auto_intersect=False)` construction of Cusa's `I.13` coaxial parabolic pencil of tangent circles $C_R$ ($R \in \{1, 2, 4, 8\}$), SymPy proof of sagitta vanishing $h(x, R) = R - \sqrt{R^2 - x^2} = \frac{x^2}{R + \sqrt{R^2 - x^2}} \to 0$ and curvature $\kappa = 1/R \to 0$, and **Möbius circle-inversion proofs** establishing that tangent circles and their horizon line form a single generalized-circle family.
- `coincidentia_triangle_line.py`: Exact `geometor.model` construction of Cusa's `I.14–15` flattening triangle family over $\mathbb{Q}$ ($B=(-1,0), C=(1,0), A_n=(0, 1/n)$) verified via **Wildberger Rational Trigonometry**: quadrances $Q_{BC}=4$, $Q_{BA_n}=Q_{A_n C}=1+\frac{1}{n^2}$, pure rational apex spread $s_{A_n}=\frac{4n^2}{(n^2+1)^2} \to 0$, Triple Spread Formula identity, and Triple Quad Formula residual $\frac{16}{n^2} \to 0$.
- `polygon_exhaustion_and_complementa.py`:
  - `I.3` inscribed & circumscribed regular $n$-gon exhaustion ($n=3, 4, 6, 8, 12$) in exact quadratic/nested radicals (*prima* & *secunda linea*).
  - *De Geometricis Transmutationibus* (1445 `§§9–11`) quarter-side *sesquiquarta* ($\frac{5}{4}$) compass-and-straightedge rectification yielding $|AH| = \frac{5\sqrt{7}}{16}$ and $\pi_{\text{Cusa,1445}} = \frac{24\sqrt{21}}{35}$.
  - *De Mathematica Perfectione* (1458) & *Aurea Propositio* (1459) exact $\mathbb{Q}(\sqrt{3})$ three-ray chord/arc/tangent construction ($IKL$ with $AK = \frac{3\cos\theta}{2+\cos\theta}$) and SymPy Maclaurin proof of the fifth-order Snellius–Cusa residual $\theta - \frac{3\sin\theta}{2+\cos\theta} = \frac{\theta^5}{180} + \frac{\theta^7}{1512} + O(\theta^9)$.
- `render.py`: Theme-adaptive `.euclid-graphic` SVG exporter generating 9 dark/light interactive figures in `docsrc/_static/figures/`.
- `texts.py`, `apparatus.py`, `concordance.py`, `compile_codex.py`: Structured public-domain Latin sources, 100% original GEOMETOR English translations, glossary, prosopography, bibliography, cross-corpus concordance, and deterministic 4-track Codex compiler.
- `sphinx_ext.py`: Sphinx extension labeling the `-la` companion track `"Latin (1440 / 1514–1913)"` in `photon_platform.publish.book`.
- `cli.py`: Rich CLI (`geometor-cusa compile|figures|concordance|verify`).

---

## 3. Architectural & Copyright Mandates

1. **100% Exact Symbolic Precision**: Zero `float` or `sp.Float` in `geometor.model.Model`; always construct with `Model(..., auto_intersect=False)` and explicit intersections/subconstructions.
2. **Strict Content / Code Separation**: Zero inline `py_file` or `.. code-block:: python` directives inside `docsrc/de_docta_ignorantia/`. Executable symbolic constructions live strictly in `src/geometor/cusa/`, `demos/`, and `docsrc/demos/`.
3. **100% Public-Domain Latin & Original English**: Latin texts are collated directly from the public-domain witnesses (Paris 1514 Faber Stapulensis, Basel 1565 Henricpetri, Paolo Rotta 1913 Laterza with Klibansky marginalia, and Heidelberg textual witness) with SHA-256 verification in `resources/cusa/sources_manifest.json`. All English translations are authored 100% originally for GEOMETOR directly from the Latin.

---

## 4. Verification Commands (Python 3.13 / Offline Sandbox)

```bash
ruff check src demos tests
uv run --no-sync pytest
publish build
```

GEOMETOR • cusa
===============

**Visit the Online Archive:** https://geometor.github.io/cusa/

**Nicholas of Cusa • De Docta Ignorantia, De Mathematicis Complementis • semantic digital archive**

Mission
-------

``geometor/cusa`` is part of the interconnected `GEOMETOR <https://geometor.com>`_ semantic digital archive. It provides a synchronized four-track Latin-English Book Codex and exact symbolic geometry engine for the philosophical and mathematical treatises of Nicholas of Cusa (*Nicolaus Cusanus*). The archive liberates Cusa's groundbreaking investigations of the coincidence of opposites (*coincidentia oppositorum*), mathematical *transsumptio*, infinite circle-line transformations, and centerless cosmology from isolated print bounds into addressable semantic units, calibrated theme-adaptive vector diagrams, primary-source manuscript provenance, and exact symbolic geometry across the GEOMETOR corpus.

Books in This Archive
---------------------

- **`On Learned Ignorance & Mathematical Writings (1440) <https://geometor.github.io/cusa/de_docta_ignorantia/>`_** — *De Docta Ignorantia* Book I (Chapters 1–23) and Book II (Chapters 11–12), developing the maximum and minimum, the coincidence of geometric figures, the infinite sphere, and centerless cosmology.
- **`De Mathematicis Complementis <https://geometor.github.io/cusa/de_mathematicis_complementis/>`_** — Cusa's *Scripta Mathematica* (1445–1459), including *De Geometricis Transmutationibus*, *De Mathematicis Complementis*, *De Mathematica Perfectione*, and the *Aurea Propositio*.

Repository Contents
-------------------

- ``docsrc/`` — Four-track Book Codex, apparatus, and Sphinx documentation compiled by `PHOTON publish <https://github.com/photon-platform/publish>`_.
- ``resources/`` — Collated Latin sources, witness manifests, apparatus datasets (persons, citations, glossary), and cross-corpus concordances.
- ``src/geometor/cusa/`` — Python modules for exact symbolic circle-line coincidence, Rational Trigonometry models, polygon exhaustion, and diagram generation.

Local Build & Verification
--------------------------

.. code-block:: bash

   publish build
   uv run --no-sync pytest

Part of the GEOMETOR Knowledge Archive
--------------------------------------

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.

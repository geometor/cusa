:navigation: header
:order: 20
:nav_title: Usage

==================
Using This Edition
==================

.. rubric:: Reader's Guide to the Interactive 4-Track Book Codex & Symbolic Environment

Welcome to the GEOMETOR critical digital edition of Nicholas of Cusa's *De Docta Ignorantia* (1440) and *Scripta Mathematica* (1445–1459). This edition integrates a rigorous philological reconstruction with interactive geometric visualization and executable symbolic algebra.

----

1. Synchronized Reading Tracks
------------------------------

Every unit in the Book Codex (:doc:`/de_docta_ignorantia/index`) is organized across four synchronized tracks accessible from the book header bar:

* **English**: A freshly authored, 100% original GEOMETOR translation rendered directly from the primary Latin witnesses (MIT licensed; zero modern copyrighted translation text).
* **Latin**: The collated Latin text based on Paolo Rotta's 1913 edition, Raymond Klibansky's McGill collations, and the 1514 Paris and 1565 Basel *Opera*.
* **Summary**: Structural synopses detailing the argumentative architecture, geometric premises, and logical progression of each section.
* **Notes**: Critical apparatus combining historical commentary, philological analysis, and exact symbolic proofs.

Switch between tracks at any time using the track navigation bar at the top of each chapter. The reader maintains your reading position across companion tracks.

----

2. Primary-Source Folio Milestones
----------------------------------

Every paragraph and proposition is keyed to historic witness loci:

* Marginal folio badges (such as ``[DI I.13 §2]`` or ``[f. 33r]``) anchor the text to primary manuscripts and early print witnesses.
* Clicking a milestone badge reveals high-resolution archival scan metadata or opens the collated source witness in the repository manifest.
* The header **Folio** indicator confirms the exact textual span of the current unit within Cusa's *Opera*.

----

3. Interactive Diagrams & Deductive Links
-----------------------------------------

The edition features nine custom ``.euclid-graphic`` SVG diagrams rendered from exact symbolic geometry:

* **Element Hovering**: Hovering over or clicking diagram labels (*A*, *B*, *C*, *D*, tangent circles, secant lines) highlights the corresponding elements in the diagram and cross-references them with text assertions.
* **Deductive Assertions**: Geometric justifications link directly to Euclid's *Elements* (:person:`Euclid <euclid>`), Archimedes (:person:`Archimedes <archimedes>`), and modern projective geometry (:person:`Klein <klein>`).
* **Scale Invariance**: Diagrams remain crisp and legible at any zoom level, supporting dark and light reading modes seamlessly.

----

4. Full-Text Search with In-Page Highlighting
---------------------------------------------

A high-performance client-side search index indexes both the English and Latin tracks:

* Enter terms into the search bar in the left navigation sidebar.
* Search results link directly to the matching chapter and paragraph.
* Search matches are automatically highlighted in-page using ``?highlight=`` parameters for immediate visual discovery.

----

5. Categories, Tags, Document Types & Collection Views
------------------------------------------------------

Explore the treatise through interconnected taxonomic facets in the sidebar:

* **Taxonomy Facets**: Browse texts by philosophical category (*coincidence of opposites*, *infinite figures*, *quadrature*), historical figures, or document type.
* **Collection Views**: Collection index pages (such as the :doc:`/log/index`) support instant view toggling between **Cards**, **Banners**, and **List** layouts to optimize research workflows.

----

6. People, Bibliography & Glossary Tooltips
-------------------------------------------

Rich contextual knowledge is embedded directly into the reading flow:

* **People Tooltips**: Hover over any highlighted person (such as :person:`Nicholas of Cusa <cusanus>`, :person:`Plato <plato>`, or :person:`Kepler <kepler>`) to preview concise biographical dates, roles, and historical significance. Click to jump to the full scholarly profile in the :doc:`/persons` registry.
* **Citations**: Inline bibliographic citations (such as :cite:`cusa:paris:1514`) display full publication details and manuscript loci on hover, linking to the :doc:`/bibliography`.
* **Technical Terms**: Specialized Latin and Greek terminology (such as :term:`docta ignorantia <docta-ignorantia>` or :term:`coincidentia oppositorum <coincidentia-oppositorum>`) offers instant definition cards via the glossary.
* **Theme Toggle**: Use the theme switcher in the navigation bar to toggle between light parchment and dark themes.

----

7. Command-Line & Python API
----------------------------

For computational geometers and researchers, ``geometor.cusa`` provides a complete Python API and command-line interface:

Verifying Codex Parity and Integrity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the automated verification suite to audit Latin/English paragraph parity, milestone alignment, and source digests:

.. code-block:: bash

   cusa verify

Regenerating Codex Artifacts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compile all four reading tracks, SVG figures, and apparatus registries:

.. code-block:: bash

   cusa compile

Interactive Symbolic Geometry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Import Cusa's geometric constructions into Python scripts and Jupyter notebooks using exact SymPy models:

.. code-block:: python

   from geometor.cusa import construct_aurea_propositio, construct_tangent_circle_pencil

   # Construct Cusa's 1459 Golden Proposition three-ray model
   model = construct_aurea_propositio()
   print(f"Elements in model: {len(model.elements)}")

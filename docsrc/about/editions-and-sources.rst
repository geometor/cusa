:navigation: header
:order: 25

====================
Editions and Sources
====================

.. rubric:: Primary Latin Witnesses (1440 / 1514–1913), Archival Scan Collation & Original GEOMETOR Translation

I. Primary Latin Witnesses
--------------------------

All Latin texts in ``geometor/cusa`` (staged with SHA-256 checksums in ``resources/cusa/sources/`` and ``resources/cusa/sources_manifest.json``) derive exclusively from public-domain witnesses verified by multimodal archival scan inspection:

1. **Paris Editio Princeps (1514)** (:cite:`cusa:paris:1514`):
   *Haec accurata recognitio trium voluminum operum Clariss. P. Nicolai Cusae Cardinalis*, edited by :person:`Jacques Lefèvre d'Étaples <klibansky>` (*Faber Stapulensis*) and printed by Jodocus Badius Ascensius at Paris. Volume I contains *De Docta Ignorantia* alongside woodcut geometric diagrams; Volume II contains the *Opuscula Mathematica*.
2. **Basel Edition (1565)** (:cite:`cusa:basel:1565`):
   *Nicolai de Cusa Cardinalis, utriusque iuris doctoris, in omnique philosophia incomparabilis viri, Opera*, printed by Heinrich Petri (*Henricpetri*) at Basel—the first printing to include Cusa's final mathematical treatise, *Aurea Propositio in Mathematicis* (August 8, 1459, pp. 1145–1146).
3. **Rotta Edition (1913) & Klibansky's McGill Collation** (:cite:`cusa:rotta:1913`, :cite:`cusa:heidelberg:1932`):
   :person:`Paolo Rotta's <klibansky>` *Nicolai Cusani De docta ignorantia libri tres* (Bari: Gius. Laterza & Figli, 1913). Direct multimodal inspection of the digitized McGill University Library copy owned and annotated in pencil by :person:`Raymond Klibansky <klibansky>` (while preparing the 1932 Heidelberg Academy edition, ``h I``) identified and restored two typesetting eye-skip (*homeoteleuton*) omissions in Rotta's printed Latin:

   * **Book I, Chapter 13 §2 (Rotta p. 28)**: Restored ``et ille plus a curvitate recedit quam arcus gh adhuc minoris circuli`` (confirmed by Rotta's own marginal woodcut depicting ``ab``, ``cd``, ``ef``, and ``gh``).
   * **Book I, Chapter 14 §3 (Rotta p. 31)**: Restored ``tanto minus vincunt lineae bd et dc lineam bc`` between ``ut bdc`` and ``et superficies minor``.

II. Original GEOMETOR English Translation & Licensing
-----------------------------------------------------

Because standard twentieth-century English translations of Nicholas of Cusa (including Germain Heron 1954, Jasper Hopkins 1981/1985, and H. Lawrence Bond 1997) remain under modern copyright, **every English sentence across all five Codex units (124 paragraphs across 21 treatise sections) was freshly translated directly from the Latin witnesses specifically for GEOMETOR** and is released under the repository's permissive **MIT License**.

Our translation adheres to three strict philological principles:

1. **Terminological Consistency**: Key Cusan concepts—:term:`docta ignorantia <docta-ignorantia>` (*learned ignorance*), :term:`coincidentia oppositorum <coincidentia-oppositorum>` (*coincidence of opposites*), :term:`transsumptio <transsumptio>` (*transsumption*), :term:`complicatio / explicatio <complicatio-et-explicatio>` (*enfolding / unfolding*), :term:`contractio <contractio>` (*contraction*), :term:`prima / secunda linea <prima-et-secunda-linea>` (*first / second line*), and :term:`proportio sesquiquarta <proportio-sesquiquarta>` (*sesquiquartal ratio* :math:`5:4`)—are rendered uniformly and linked to the critical apparatus.
2. **Geometric Letter Fidelity**: All diagram labels (*ab*, *cd*, *ef*, *gh*, *bac*, *bdc*, *ikl*) match the historic woodcuts and interactive ``.euclid-graphic`` SVGs.
3. **1-to-1 Paragraph Synchronization**: Every English paragraph stands in verified 1-to-1 bijection (`verify_unit_parity`) with its corresponding Latin witness paragraph and ``.. folio::`` milestone.

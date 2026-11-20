"""Codex compiler generating the 4-track synchronized Book Codex and source manifests for Cusa."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path

from geometor.cusa.apparatus import write_apparatus_artifacts
from geometor.cusa.commentary import UNIT_NOTES, UNIT_SUMMARIES
from geometor.cusa.concordance import write_concordance_artifacts
from geometor.cusa.render import export_all_codex_figures
from geometor.cusa.texts_u1_u3 import BilingualSectionData
from geometor.cusa.units import CODEX_UNITS, CodexUnitSpec


def _slugify_milestone(milestone: str) -> str:
    """Convert a milestone string (e.g. ``'DI I.13 §2'``) into a clean RST anchor slug."""
    cleaned = milestone.replace("§", "s-").lower()
    return re.sub(r"[^a-z0-9]+", "-", cleaned).strip("-")


def _picture_block(svg_name: str, alt: str, caption: str) -> list[str]:
    """Render an interactive ``.. picture::`` RST directive block."""
    return [
        f".. picture:: /_static/figures/{svg_name}",
        f"   :alt: {alt}",
        f"   :caption: {caption}",
        "",
    ]


def _all_unit_pictures(unit: CodexUnitSpec) -> list[str]:
    """Render the primary unit figure plus any distinct section-specific figures for Summary/Notes."""
    blocks: list[str] = []
    if unit.figure_svg and unit.figure_caption:
        blocks.extend(_picture_block(unit.figure_svg, unit.title, unit.figure_caption))
    for sec in unit.sections:
        if sec.figure_svg and sec.figure_caption and sec.figure_svg != unit.figure_svg:
            blocks.extend(_picture_block(sec.figure_svg, sec.heading_en, sec.figure_caption))
    return blocks


def verify_unit_parity(unit: CodexUnitSpec) -> dict[str, object]:
    """Verify strict 1-to-1 Latin/English paragraph and milestone parity for a unit.

    Args:
        unit: :class:`CodexUnitSpec` to inspect.

    Returns:
        Dictionary of section-level and unit-level paragraph counts and parity flags.

    Raises:
        ValueError: If any section has mismatched Latin/English paragraph counts or milestones.
    """
    total_la = 0
    total_en = 0
    section_reports: list[dict[str, object]] = []
    for sec in unit.sections:
        n_la = len(sec.la_paragraphs)
        n_en = len(sec.en_paragraphs)
        if n_la != n_en:
            msg = (
                f"Paragraph parity mismatch in {unit.slug}/{sec.section_id}: "
                f"{n_la} Latin vs {n_en} English"
            )
            raise ValueError(msg)
        la_miles = [m for m, _ in sec.la_paragraphs]
        en_miles = [m for m, _ in sec.en_paragraphs]
        if la_miles != en_miles:
            msg = f"Milestone mismatch in {unit.slug}/{sec.section_id}: {la_miles} != {en_miles}"
            raise ValueError(msg)
        total_la += n_la
        total_en += n_en
        section_reports.append(
            {
                "section_id": sec.section_id,
                "folio_prefix": sec.folio_prefix,
                "witness": sec.witness_note,
                "la_paragraphs": n_la,
                "en_paragraphs": n_en,
            }
        )
    return {
        "slug": unit.slug,
        "book_slug": unit.book_slug,
        "doc_rel_dir": unit.doc_rel_dir,
        "unit_number": unit.unit_number,
        "canonical_id": unit.canonical_id,
        "locus_summary": unit.locus_summary,
        "section_count": len(unit.sections),
        "la_paragraph_count": total_la,
        "en_paragraph_count": total_en,
        "parity_verified": True,
        "sections": section_reports,
    }


def _render_plain_witness(sections: tuple[BilingualSectionData, ...], *, lang: str) -> str:
    """Serialize a unit's Latin or English text to canonical plain-text source format."""
    lines: list[str] = []
    for sec in sections:
        heading = sec.heading_la if lang == "la" else sec.heading_en
        paras = sec.la_paragraphs if lang == "la" else sec.en_paragraphs
        lines.append(f"### {heading}")
        lines.append(f"# Witness: {sec.witness_note}")
        lines.append("")
        for milestone, text in paras:
            lines.append(f"[{milestone}] {text}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_source_witnesses(repo_root: str | Path) -> dict[str, Path]:
    """Write canonical ``.la.txt`` / ``.en.txt`` source witnesses, ``sources_manifest.json``, and ``folio_map.json``."""
    root = Path(repo_root)
    sources_dir = root / "resources" / "cusa" / "sources"
    sources_dir.mkdir(parents=True, exist_ok=True)

    # Clean legacy unit-* files and legacy bundled cap_*_* witness files
    expected_prefixes = {unit.source_prefix for unit in CODEX_UNITS}
    for old_file in sources_dir.glob("*.txt"):
        stem = old_file.name.removesuffix(".la.txt").removesuffix(".en.txt")
        if stem.startswith("unit-") or stem not in expected_prefixes:
            try:
                old_file.unlink()
            except OSError:
                pass

    written: dict[str, Path] = {}
    unit_entries: list[dict[str, object]] = []
    folio_entries: dict[str, dict[str, str]] = {}

    for unit in CODEX_UNITS:
        parity_info = verify_unit_parity(unit)
        la_text = _render_plain_witness(unit.sections, lang="la")
        en_text = _render_plain_witness(unit.sections, lang="en")

        la_path = sources_dir / f"{unit.source_prefix}.la.txt"
        en_path = sources_dir / f"{unit.source_prefix}.en.txt"
        la_path.write_text(la_text, encoding="utf-8")
        en_path.write_text(en_text, encoding="utf-8")
        la_rel = str(la_path.relative_to(root))
        en_rel = str(en_path.relative_to(root))
        written[la_rel] = la_path
        written[en_rel] = en_path

        folio_entries[unit.locus_summary] = {
            "la": f"{la_rel}#L1",
            "en": f"{en_rel}#L1",
            "default": f"{la_rel}#L1",
        }
        la_lines = {
            m.group(1): idx
            for idx, line in enumerate(la_text.splitlines(), start=1)
            if (m := re.match(r"^\[([^\]]+)\]\s+", line))
        }
        en_lines = {
            m.group(1): idx
            for idx, line in enumerate(en_text.splitlines(), start=1)
            if (m := re.match(r"^\[([^\]]+)\]\s+", line))
        }
        for milestone, la_lineno in la_lines.items():
            en_lineno = en_lines.get(milestone, la_lineno)
            folio_entries[milestone] = {
                "la": f"{la_rel}#L{la_lineno}",
                "en": f"{en_rel}#L{en_lineno}",
                "default": f"{la_rel}#L{la_lineno}",
            }

        la_sha = hashlib.sha256(la_text.encode("utf-8")).hexdigest()
        en_sha = hashlib.sha256(en_text.encode("utf-8")).hexdigest()
        unit_entries.append(
            {
                **parity_info,
                "la_source": la_rel,
                "en_source": en_rel,
                "la_sha256": la_sha,
                "en_sha256": en_sha,
            }
        )

    manifest = {
        "corpus": "geometor-cusa",
        "author": "Nicolaus Cusanus (Nicholas of Cusa, 1401–1464)",
        "works": [
            "De Docta Ignorantia (completed Kues, February 12, 1440)",
            "De Geometricis Transmutationibus (1445)",
            "De Mathematicis Complementis (1453)",
            "De Mathematica Perfectione (1458)",
            "Aurea Propositio in Mathematicis (Rome, August 8, 1459)",
        ],
        "latin_witnesses": [
            "Paolo Rotta, Nicolai Cusani De docta ignorantia libri tres (Bari: Laterza, 1913), "
            "collated with Raymond Klibansky's annotated copy (McGill University Library)",
            "Jacques Lefèvre d'Étaples (Faber Stapulensis), Haec accurata recognitio trium "
            "voluminum operum Clariss. P. Nicolai Cusae Cardinalis (Paris: Badius Ascensius, 1514)",
            "Nicolai de Cusa Opera (Basel: Henricpetri, 1565)",
            "Heidelberg Academy Edition concordance markers (h I, 1932; h XX, 2010)",
        ],
        "english_translation": (
            "100% Original GEOMETOR Scholarly Translation Rendered Directly from the Public-Domain "
            "Latin Witnesses (MIT Licensed; Zero Modern Copyrighted Translation Text)"
        ),
        "unit_count": len(CODEX_UNITS),
        "total_la_paragraphs": sum(int(u["la_paragraph_count"]) for u in unit_entries),
        "total_en_paragraphs": sum(int(u["en_paragraph_count"]) for u in unit_entries),
        "units": unit_entries,
    }
    manifest_path = root / "resources" / "cusa" / "sources_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    written[str(manifest_path.relative_to(root))] = manifest_path

    folio_map_payload = {
        "_corpus": "geometor-cusa",
        "_edition": "cusa",
        "_schema": "geometor-codex-folio-map-v1",
        "_description": "Primary-source milestone and unit folio map for Nicolaus Cusanus codex",
        "folios": folio_entries,
    }
    folio_map_path = root / "resources" / "cusa" / "folio_map.json"
    folio_map_path.write_text(
        json.dumps(folio_map_payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    written[str(folio_map_path.relative_to(root))] = folio_map_path
    return written


def _render_unit_en_rst(unit: CodexUnitSpec, order_num: int) -> str:
    """Render primary ``index.rst`` (English track)."""
    lines = [
        f":order: {order_num}",
        ":layout: book",
        f":title: {unit.title}",
        f":canonical_id: {unit.canonical_id}",
        f":original_id: {unit.canonical_id}",
        f":folio: {unit.locus_summary}",
        ":tracks: English: index | Latin: la | Summary: summary | Notes: notes",
        "",
        f".. _{unit.anchor_slug}:",
        f".. _{unit.anchor_slug}-en:",
    ]
    for leg in unit.legacy_slugs:
        if leg not in [sec.section_id for sec in unit.sections]:
            lines.append(f".. _{leg}:")
            lines.append(f".. _{leg}-en:")

    lines.extend(
        [
            "",
            "=" * len(unit.title),
            unit.title,
            "=" * len(unit.title),
            "",
            f".. rubric:: {unit.subtitle}",
            "",
            ".. epigraph::",
            "",
            f"   *{unit.epigraph_la}*",
            "",
            f"   {unit.epigraph_en} — **{unit.epigraph_locus}**",
            "",
        ]
    )
    if unit.figure_svg and unit.figure_caption:
        lines.extend(_picture_block(unit.figure_svg, unit.title, unit.figure_caption))

    for sec in unit.sections:
        lines.extend(
            [
                f".. _{sec.section_id}:",
                f".. _{sec.section_id}-en:",
                "",
                sec.heading_en,
                "-" * len(sec.heading_en),
                "",
                f"*Original GEOMETOR Translation from the Latin · {sec.witness_note}*",
                "",
            ]
        )
        if sec.figure_svg and sec.figure_caption and sec.figure_svg != unit.figure_svg:
            lines.extend(_picture_block(sec.figure_svg, sec.heading_en, sec.figure_caption))

        for milestone, para_text in sec.en_paragraphs:
            anchor = f"cusa-en-{_slugify_milestone(milestone)}"
            lines.extend(
                [
                    f".. _{anchor}:",
                    "",
                    f".. folio:: {milestone}",
                    "",
                    para_text,
                    "",
                ]
            )

    return "\n".join(lines)


def _render_unit_la_rst(unit: CodexUnitSpec, order_num: int) -> str:
    """Render ``la.rst`` (Latin track)."""
    heading_main = f"{unit.title} — Latin (1440 / 1514–1913)"
    lines = [
        f":order: {order_num}",
        ":layout: book",
        ":type: la",
        f":title: {heading_main}",
        f":canonical_id: {unit.canonical_id}",
        f":original_id: {unit.canonical_id}",
        f":folio: {unit.locus_summary}",
        ":tracks: English: index | Latin: la | Summary: summary | Notes: notes",
        "",
        f".. _{unit.anchor_slug}-la:",
    ]
    for leg in unit.legacy_slugs:
        if leg not in [sec.section_id for sec in unit.sections]:
            lines.append(f".. _{leg}-la:")

    lines.extend(
        [
            "",
            "=" * len(heading_main),
            heading_main,
            "=" * len(heading_main),
            "",
            (
                f".. rubric:: Textus Latinus Collatis Editionibus Parisiensi (1514), "
                f"Basileensi (1565) et Rottae (1913) · {unit.locus_summary}"
            ),
            "",
        ]
    )
    if unit.figure_svg and unit.figure_caption:
        lines.extend(_picture_block(unit.figure_svg, unit.title, unit.figure_caption))

    for sec in unit.sections:
        lines.extend(
            [
                f".. _{sec.section_id}-la:",
                "",
                sec.heading_la,
                "-" * len(sec.heading_la),
                "",
                f"*{sec.witness_note}*",
                "",
            ]
        )
        if sec.figure_svg and sec.figure_caption and sec.figure_svg != unit.figure_svg:
            lines.extend(_picture_block(sec.figure_svg, sec.heading_la, sec.figure_caption))

        for milestone, para_text in sec.la_paragraphs:
            anchor = f"cusa-la-{_slugify_milestone(milestone)}"
            lines.extend(
                [
                    f".. _{anchor}:",
                    "",
                    f".. folio:: {milestone}",
                    "",
                    para_text,
                    "",
                ]
            )

    return "\n".join(lines)


def _render_unit_summary_rst(unit: CodexUnitSpec, order_num: int) -> str:
    """Render ``summary.rst`` (Summary track)."""
    heading_main = f"{unit.title} — Structural Synopsis"
    lines = [
        f":order: {order_num}",
        ":layout: book",
        ":type: summary",
        f":title: {unit.title} — Summary",
        f":canonical_id: {unit.canonical_id}",
        f":original_id: {unit.canonical_id}",
        f":folio: {unit.locus_summary}",
        ":tracks: English: index | Latin: la | Summary: summary | Notes: notes",
        "",
        f".. _{unit.anchor_slug}-summary:",
    ]
    for leg in unit.legacy_slugs:
        if leg not in [sec.section_id for sec in unit.sections]:
            lines.append(f".. _{leg}-summary:")

    lines.extend(
        [
            "",
            "=" * len(heading_main),
            heading_main,
            "=" * len(heading_main),
            "",
            f".. rubric:: Argumentative Architecture & Interactive Diagram Guide · {unit.locus_summary}",
            "",
            *_all_unit_pictures(unit),
            UNIT_SUMMARIES[unit.key],
            "",
        ]
    )
    return "\n".join(lines)


def _render_unit_notes_rst(unit: CodexUnitSpec, order_num: int) -> str:
    """Render ``notes.rst`` (Notes track)."""
    heading_main = f"{unit.title} — Critical Commentary & Notes"
    lines = [
        f":order: {order_num}",
        ":layout: book",
        ":type: notes",
        f":title: {unit.title} — Notes",
        f":canonical_id: {unit.canonical_id}",
        f":original_id: {unit.canonical_id}",
        f":folio: {unit.locus_summary}",
        ":tracks: English: index | Latin: la | Summary: summary | Notes: notes",
        "",
        f".. _{unit.anchor_slug}-notes:",
    ]
    for leg in unit.legacy_slugs:
        if leg not in [sec.section_id for sec in unit.sections]:
            lines.append(f".. _{leg}-notes:")

    lines.extend(
        [
            "",
            "=" * len(heading_main),
            heading_main,
            "=" * len(heading_main),
            "",
            (
                f".. rubric:: Exact Symbolic Reconstruction, Latin Philology & Canon Reception · "
                f"{unit.locus_summary}"
            ),
            "",
            *_all_unit_pictures(unit),
            UNIT_NOTES[unit.key],
            "",
            "IV. Executable Symbolic Verification",
            "------------------------------------",
            "",
            (
                "In accordance with GEOMETOR's strict content/code separation for historical editions, "
                "executable ``geometor.model`` SymPy constructions, Rational Trigonometry proofs, and "
                f"series-error audits for **{unit.title}** live in ``src/geometor/cusa/`` and "
                f"the companion walkthrough :doc:`{unit.demo_doc}`."
            ),
            "",
        ]
    )
    return "\n".join(lines)


def render_de_docta_ignorantia_index_rst() -> str:
    """Render ``docsrc/de_docta_ignorantia/index.rst``."""
    h1_title = "On Learned Ignorance & Mathematical Writings (1440)"
    lines = [
        ":navigation: header",
        ":order: 1",
        ":nav_title: Learned Ignorance",
        ":layout: book",
        ":type: book",
        f":book_title: {h1_title}",
        (
            ":book_subtitle: Nicholas of Cusa (1401–1464) · Latin (1440 / 1514–1913) & "
            "Original GEOMETOR English Codex"
        ),
        ":author: Nicholas of Cusa",
        ":year: 1440",
        ":book_theme: classical-serif",
        "",
        ".. _de-docta-ignorantia:",
        "",
        "=" * len(h1_title),
        h1_title,
        "=" * len(h1_title),
        "",
        ".. rubric:: *De Docta Ignorantia Libri Tres* — Nicholas of Cusa (Kues, February 12, 1440)",
        "",
        ".. container:: title-page",
        "",
        "   | **Nicholas of Cusa** (*Nicolaus Cusanus*, 1401–1464)",
        "   | Cardinal Priest of San Pietro in Vincoli · Bishop of Brixen",
        "   |",
        "   | *First Edition*: Paris (Jodocus Badius Ascensius, 1514, ed. Jacques Lefèvre d'Étaples)",
        "   | *Critical Editions*: Bari (Paolo Rotta, 1913) · Heidelberg (Ernst Hoffmann & Raymond Klibansky, 1932)",
        "   | *GEOMETOR Digital Edition*: 100% Original English Translation with Synchronized Latin Witness",
        "",
        (
            "**De Docta Ignorantia** presents in a critical Digital "
            "Scriptorium edition the complete geometric, epistemological, and cosmological core of "
            ":person:`Nicholas of Cusa's <cusanus>` *De Docta Ignorantia* (completed at Kues on "
            "**February 12, 1440**)."
        ),
        "",
        (
            "Every chapter is presented across **four synchronized tracks**—**English** (a freshly "
            "authored, 100% original GEOMETOR translation rendered directly from the Latin), "
            "**Latin (1440 / 1514–1913)** (collated from :person:`Paolo Rotta's <klibansky>` 1913 "
            "edition with :person:`Raymond Klibansky's <klibansky>` archival restorations and the "
            "1514 Paris / 1565 Basel *Opera*), **Summary**, and **Critical Notes** (pairing interactive "
            "``.euclid-graphic`` SVG constructions with historical reception across antiquity, "
            "the Middle Ages, the Renaissance, and modern geometry)."
        ),
        "",
        "Books of the Treatise",
        "---------------------",
        "",
        ".. collection::",
        "   :sort: order",
        "",
        ".. toctree::",
        "   :hidden:",
        "   :maxdepth: 2",
        "",
        "   liber_i/index",
        "   liber_ii/index",
        "",
    ]
    return "\n".join(lines)


def render_liber_i_index_rst() -> str:
    """Render ``docsrc/de_docta_ignorantia/liber_i/index.rst``."""
    h1 = "Liber I — De Maximo Absoluto"
    lines = [
        ":order: 1",
        ":layout: book",
        ":type: part",
        f":title: {h1}",
        ":canonical_id: DI Liber I",
        f":book_title: {h1}",
        ":book_subtitle: The Absolute Maximum & Geometric Transsumption (1440)",
        ":author: Nicholas of Cusa",
        ":year: 1440",
        ":excerpt: Nicholas of Cusa's investigations into the Absolute Maximum, polygon exhaustion, and the three-step method of mathematical transsumption.",
        "",
        ".. _de-docta-ignorantia-liber-i:",
        "",
        "=" * len(h1),
        h1,
        "=" * len(h1),
        "",
        ".. rubric:: *De Docta Ignorantia · Liber Primus* — Nicholas of Cusa (1440)",
        "",
        ".. container:: title-page",
        "",
        "   | **Nicholas of Cusa** (*Nicolaus Cusanus*, 1401–1464)",
        "   |",
        "   | *Liber Primus: De Maximo Absoluto*",
        "   | Dedicated to Cardinal Julian Cesarini (*Dedicatio ad Dominum Iulianum Cardinalem*)",
        "   | Completed at Kues on February 12, 1440 (*Epistola Auctoris*)",
        "",
        (
            "Book I investigates the Absolute Maximum—that than which nothing can be greater—which "
            "transcends all comparative proportion and in which the superlative Minimum coincides. "
            "Through the mathematical transsumption of the straight line, triangle, circle, and sphere, "
            "Cusa demonstrates how geometric symbols serve as an incorruptible ladder to intellectual vision."
        ),
        "",
        "Capitula of Book I",
        "------------------",
        "",
        ".. collection::",
        "   :sort: order",
        "",
        ".. toctree::",
        "   :hidden:",
        "   :maxdepth: 2",
        "",
        *[
            f"   {u.slug}/index"
            for u in CODEX_UNITS
            if u.book_slug == "de_docta_ignorantia/liber_i"
        ],
        "",
    ]
    return "\n".join(lines)


def render_liber_ii_index_rst() -> str:
    """Render ``docsrc/de_docta_ignorantia/liber_ii/index.rst``."""
    h1 = "Liber II — De Universo et Cosmologia"
    lines = [
        ":order: 2",
        ":layout: book",
        ":type: part",
        f":title: {h1}",
        ":canonical_id: DI Liber II",
        f":book_title: {h1}",
        ":book_subtitle: Centerless Cosmology & the Fabric of the World (1440)",
        ":author: Nicholas of Cusa",
        ":year: 1440",
        ":excerpt: Nicholas of Cusa's revolutionary centerless cosmology: motion in the contracted universe, relativity of observers, and the moving Earth as a noble star.",
        "",
        ".. _de-docta-ignorantia-liber-ii:",
        "",
        "=" * len(h1),
        h1,
        "=" * len(h1),
        "",
        ".. rubric:: *De Docta Ignorantia · Liber Secundus* — Nicholas of Cusa (1440)",
        "",
        ".. container:: title-page",
        "",
        "   | **Nicholas of Cusa** (*Nicolaus Cusanus*, 1401–1464)",
        "   |",
        "   | *Liber Secundus: De Universo et Cosmologia*",
        "   | Kinematic Relativity & Astrophysical Homogeneity",
        "",
        (
            "Book II develops the cosmology of the contracted universe. Because exact physical "
            "equidistance never occurs in nature, no celestial body can occupy an immobile geometric "
            "center, nor do fixed celestial poles exist. The universe is as though having its center "
            "everywhere and its circumference nowhere (*quasi habens undique centrum et nullibi circumferentiam*)."
        ),
        "",
        "Capitula of Book II",
        "-------------------",
        "",
        ".. collection::",
        "   :sort: order",
        "",
        ".. toctree::",
        "   :hidden:",
        "   :maxdepth: 2",
        "",
        *[
            f"   {u.slug}/index"
            for u in CODEX_UNITS
            if u.book_slug == "de_docta_ignorantia/liber_ii"
        ],
        "",
    ]
    return "\n".join(lines)


def render_de_mathematicis_complementis_index_rst() -> str:
    """Render ``docsrc/de_mathematicis_complementis/index.rst``."""
    h1 = "De Mathematicis Complementis"
    lines = [
        ":navigation: header",
        ":order: 2",
        ":type: book",
        f":nav_title: {h1}",
        f":breadcrumb_title: {h1}",
        ":layout: book",
        f":book_title: {h1}",
        ":book_subtitle: Scripta Mathematica (1445–1459) — Nicholas of Cusa",
        ":author: Nicholas of Cusa",
        ":year: 1453",
        ":book_theme: classical-serif",
        ":excerpt: Nicholas of Cusa's constructive mathematical treatises on isoperimetric transmutations, Archimedes' spiral, circle quadrature, and the Golden Proposition.",
        "",
        ".. _de-mathematicis-complementis:",
        "",
        "=" * len(h1),
        h1,
        "=" * len(h1),
        "",
        ".. rubric:: *Scripta Mathematica* (1445–1459) — Nicholas of Cusa",
        "",
        ".. container:: title-page",
        "",
        "   | **Nicholas of Cusa** (*Nicolaus Cusanus*, 1401–1464)",
        "   | Cardinal Priest of San Pietro in Vincoli · Bishop of Brixen",
        "   |",
        "   | *First Edition*: Paris (Jodocus Badius Ascensius, 1514, ed. Jacques Lefèvre d'Étaples)",
        "   | *Critical Editions*: Heidelberg (*Opera Omnia* XX, 2010) · Paris / Basel (1514 / 1565)",
        "   | *GEOMETOR Digital Edition*: 100% Original English Translation with Synchronized Latin Witness",
        "",
        (
            "*De Mathematicis Complementis* and Cusa's companion *Scripta Mathematica* represent "
            "the cardinal's constructive geometric treatises composed between 1445 and 1459. "
            "Spanning isoperimetric polygons, circle rectification, the critical dissection of "
            "Archimedes' spiral, and the Golden Proposition (*Aurea Propositio*), these works apply "
            "the principles of learned ignorance to constructive geometry."
        ),
        "",
        "Treatises & Mathematical Writings",
        "---------------------------------",
        "",
        ".. collection::",
        "   :sort: order",
        "",
        ".. toctree::",
        "   :hidden:",
        "   :maxdepth: 2",
        "",
        "   transmutatio_1445/index",
        "   complementa_1453/index",
        "   perfectio_1458/index",
        "   aurea_propositio_1459/index",
        "",
    ]
    return "\n".join(lines)


def compile_all_codex(repo_root: str | Path, *, regen_figures: bool = True) -> dict[str, Path]:
    """Compile all 4-track Codex units, source manifests, apparatus JSON/RST, and SVG figures.

    Args:
        repo_root: Root directory of ``geometor/cusa``.
        regen_figures: When ``True`` (default), regenerate all 9 ``.euclid-graphic`` SVGs.

    Returns:
        Mapping of relative output paths to resolved :class:`~pathlib.Path` objects.
    """
    root = Path(repo_root)
    codex_dir = root / "docsrc" / "de_docta_ignorantia"
    dmc_dir = root / "docsrc" / "de_mathematicis_complementis"
    codex_dir.mkdir(parents=True, exist_ok=True)
    dmc_dir.mkdir(parents=True, exist_ok=True)

    # Clean legacy unit-* directories, bundled cap_*_* directories, and mislocated apparatus
    for old_slug in (
        "unit-1-maximum-ignorantia",
        "unit-2-mathematica-transsumptio",
        "unit-3-coincidentia-figurarum",
        "unit-4-linea-sphaera-infinita",
        "unit-5-cosmologia-complementa",
        "liber_i/cap_01_04",
        "liber_i/cap_11_12",
        "liber_i/cap_13_15",
        "liber_i/cap_16_17",
        "liber_i/cap_18_20",
        "liber_i/cap_21_23",
        "liber_ii/cap_11_12",
    ):
        target_dir = codex_dir / old_slug
        if target_dir.is_dir():
            shutil.rmtree(target_dir, ignore_errors=True)

    for app_fname in ("glossary.rst", "persons.rst", "bibliography.rst", "concordance.rst"):
        target_file = codex_dir / app_fname
        if target_file.is_file():
            try:
                target_file.unlink()
            except OSError:
                pass

    written: dict[str, Path] = {}

    if regen_figures:
        for fpath in export_all_codex_figures(root / "docsrc" / "_static" / "figures"):
            written[str(fpath.relative_to(root))] = fpath

    written.update(write_source_witnesses(root))
    written.update(write_apparatus_artifacts(root))
    written.update(write_concordance_artifacts(root))

    # Container pages
    di_index = codex_dir / "index.rst"
    di_index.write_text(render_de_docta_ignorantia_index_rst(), encoding="utf-8")
    written[str(di_index.relative_to(root))] = di_index

    lib_i_dir = codex_dir / "liber_i"
    lib_i_dir.mkdir(parents=True, exist_ok=True)
    lib_i_index = lib_i_dir / "index.rst"
    lib_i_index.write_text(render_liber_i_index_rst(), encoding="utf-8")
    written[str(lib_i_index.relative_to(root))] = lib_i_index

    lib_ii_dir = codex_dir / "liber_ii"
    lib_ii_dir.mkdir(parents=True, exist_ok=True)
    lib_ii_index = lib_ii_dir / "index.rst"
    lib_ii_index.write_text(render_liber_ii_index_rst(), encoding="utf-8")
    written[str(lib_ii_index.relative_to(root))] = lib_ii_index

    dmc_index = dmc_dir / "index.rst"
    dmc_index.write_text(render_de_mathematicis_complementis_index_rst(), encoding="utf-8")
    written[str(dmc_index.relative_to(root))] = dmc_index

    # Atomic leaf units across 4 tracks
    for idx, unit in enumerate(CODEX_UNITS, start=1):
        verify_unit_parity(unit)
        unit_dir = root / "docsrc" / unit.doc_rel_dir
        unit_dir.mkdir(parents=True, exist_ok=True)

        track_files = {
            "index.rst": _render_unit_en_rst(unit, idx * 10),
            "la.rst": _render_unit_la_rst(unit, idx * 10),
            "summary.rst": _render_unit_summary_rst(unit, idx * 10),
            "notes.rst": _render_unit_notes_rst(unit, idx * 10),
        }
        for fname, content in track_files.items():
            target = unit_dir / fname
            target.write_text(content, encoding="utf-8")
            written[str(target.relative_to(root))] = target

    return written

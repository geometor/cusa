"""Codex compiler generating the 4-track synchronized Book Codex and source manifests for Cusa."""

from __future__ import annotations

import hashlib
import json
import re
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
    """Render the primary unit figure plus any section-specific figures for Summary/Notes."""
    blocks = _picture_block(unit.figure_svg, unit.title, unit.figure_caption)
    for sec in unit.sections:
        if sec.figure_svg and sec.figure_caption:
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
        "unit_number": unit.unit_number,
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
    """Write canonical ``.la.txt`` / ``.en.txt`` source witnesses and ``sources_manifest.json``."""
    root = Path(repo_root)
    sources_dir = root / "resources" / "cusa" / "sources"
    sources_dir.mkdir(parents=True, exist_ok=True)
    written: dict[str, Path] = {}
    unit_entries: list[dict[str, object]] = []

    for unit in CODEX_UNITS:
        parity_info = verify_unit_parity(unit)
        la_text = _render_plain_witness(unit.sections, lang="la")
        en_text = _render_plain_witness(unit.sections, lang="en")

        la_path = sources_dir / f"{unit.slug}.la.txt"
        en_path = sources_dir / f"{unit.slug}.en.txt"
        la_path.write_text(la_text, encoding="utf-8")
        en_path.write_text(en_text, encoding="utf-8")
        written[str(la_path.relative_to(root))] = la_path
        written[str(en_path.relative_to(root))] = en_path

        la_sha = hashlib.sha256(la_text.encode("utf-8")).hexdigest()
        en_sha = hashlib.sha256(en_text.encode("utf-8")).hexdigest()
        unit_entries.append(
            {
                **parity_info,
                "la_source": str(la_path.relative_to(root)),
                "en_source": str(en_path.relative_to(root)),
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
        "total_la_paragraphs": sum(int(u["la_paragraph_count"]) for u in unit_entries),  # type: ignore[arg-type]
        "total_en_paragraphs": sum(int(u["en_paragraph_count"]) for u in unit_entries),  # type: ignore[arg-type]
        "units": unit_entries,
    }
    manifest_path = root / "resources" / "cusa" / "sources_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    written[str(manifest_path.relative_to(root))] = manifest_path
    return written


def _render_unit_en_rst(unit: CodexUnitSpec, order_num: int) -> str:
    """Render ``<slug>/<slug>-en.rst``."""
    heading_main = f"{unit.unit_number} — {unit.title}"
    lines = [
        f":order: {order_num}",
        ":layout: book",
        f":title: {heading_main}",
        f":canonical_id: {unit.locus_summary}",
        f":original_id: {unit.locus_summary}",
        f":folio: {unit.locus_summary}",
        "",
        f".. _{unit.slug}:",
        f".. _{unit.slug}-en:",
        "",
        "=" * len(heading_main),
        heading_main,
        "=" * len(heading_main),
        "",
        f".. rubric:: {unit.subtitle}",
        "",
        ".. epigraph::",
        "",
        f"   *{unit.epigraph_la}*",
        "",
        f"   {unit.epigraph_en} — **{unit.epigraph_locus}**",
        "",
        *_picture_block(unit.figure_svg, unit.title, unit.figure_caption),
    ]

    for sec in unit.sections:
        lines.extend(
            [
                f".. _{sec.section_id}-en:",
                "",
                sec.heading_en,
                "-" * len(sec.heading_en),
                "",
                f"*Original GEOMETOR Translation from the Latin · {sec.witness_note}*",
                "",
            ]
        )
        if sec.figure_svg and sec.figure_caption:
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


def _render_unit_la_rst(unit: CodexUnitSpec) -> str:
    """Render ``<slug>/<slug>-la.rst``."""
    heading_main = f"{unit.unit_number} — {unit.title} — Latin (1440 / 1514–1913)"
    lines = [
        ":layout: book",
        ":type: la",
        f":title: {heading_main}",
        f":canonical_id: {unit.locus_summary}",
        f":original_id: {unit.locus_summary}",
        f":folio: {unit.locus_summary}",
        "",
        f".. _{unit.slug}-la:",
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
        *_picture_block(unit.figure_svg, unit.title, unit.figure_caption),
    ]

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
        if sec.figure_svg and sec.figure_caption:
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


def _render_unit_summary_rst(unit: CodexUnitSpec) -> str:
    """Render ``<slug>/<slug>-summary.rst``."""
    heading_main = f"{unit.unit_number} — {unit.title} — Structural Synopsis"
    lines = [
        ":layout: book",
        ":type: summary",
        f":title: {unit.unit_number} — {unit.title} — Summary",
        f":canonical_id: {unit.locus_summary}",
        f":original_id: {unit.locus_summary}",
        f":folio: {unit.locus_summary}",
        "",
        f".. _{unit.slug}-summary:",
        "",
        "=" * len(heading_main),
        heading_main,
        "=" * len(heading_main),
        "",
        f".. rubric:: Argumentative Architecture & Interactive Diagram Guide · {unit.locus_summary}",
        "",
        *_all_unit_pictures(unit),
        UNIT_SUMMARIES[unit.slug],
        "",
    ]
    return "\n".join(lines)


def _render_unit_notes_rst(unit: CodexUnitSpec) -> str:
    """Render ``<slug>/<slug>-notes.rst``."""
    heading_main = f"{unit.unit_number} — {unit.title} — Critical Commentary & Notes"
    lines = [
        ":layout: book",
        ":type: notes",
        f":title: {unit.unit_number} — {unit.title} — Notes",
        f":canonical_id: {unit.locus_summary}",
        f":original_id: {unit.locus_summary}",
        f":folio: {unit.locus_summary}",
        "",
        f".. _{unit.slug}-notes:",
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
        UNIT_NOTES[unit.slug],
        "",
        "IV. Executable Symbolic Verification",
        "------------------------------------",
        "",
        (
            "In accordance with GEOMETOR's strict content/code separation for historical editions, "
            "executable ``geometor.model`` SymPy constructions, Rational Trigonometry proofs, and "
            f"series-error audits for **{unit.unit_number}** live in ``src/geometor/cusa/`` and "
            f"the companion walkthrough :doc:`{unit.demo_doc}`."
        ),
        "",
    ]
    return "\n".join(lines)


def render_book_index_rst() -> str:
    """Render ``docsrc/de_docta_ignorantia/index.rst``."""
    lines = [
        ":order: 1",
        ":layout: book",
        ":book_title: De Docta Ignorantia et Scripta Mathematica",
        (
            ":book_subtitle: Nicholas of Cusa (1401–1464) · Latin (1440 / 1514–1913) & "
            "Original GEOMETOR English Codex"
        ),
        ":author: Nicholas of Cusa",
        ":book_theme: classical-serif",
        "",
        ".. _de-docta-ignorantia:",
        "",
        "======================================================================================",
        "De Docta Ignorantia et Scripta Mathematica — Coincidence of Opposites & Exact Geometry",
        "======================================================================================",
        "",
        (
            ".. rubric:: Synchronized 4-Track Book Codex "
            "(English · Latin 1440 / 1514–1913 · Summary · Critical Notes)"
        ),
        "",
        (
            "**De Docta Ignorantia et Scripta Mathematica** presents in a critical Digital "
            "Scriptorium edition the complete geometric, epistemological, and cosmological core of "
            ":person:`Nicholas of Cusa's <cusanus>` *De Docta Ignorantia* (completed at Kues on "
            "**February 12, 1440**) alongside his four landmark mathematical treatises: "
            "*De Geometricis Transmutationibus* (**1445**), *De Mathematicis Complementis* "
            "(**1453**), *De Mathematica Perfectione* (**1458**), and the complete *Aurea "
            "Propositio in Mathematicis* (**August 8, 1459**)."
        ),
        "",
        (
            "Every unit is presented across **four synchronized tracks**—**English** (a freshly "
            "authored, 100% original GEOMETOR translation rendered directly from the Latin), "
            "**Latin (1440 / 1514–1913)** (collated from :person:`Paolo Rotta's <klibansky>` 1913 "
            "edition with :person:`Raymond Klibansky's <klibansky>` archival restorations and the "
            "1514 Paris / 1565 Basel *Opera*), **Summary**, and **Critical Notes** (pairing nine "
            "interactive ``.euclid-graphic`` SVG constructions with reception across "
            ":person:`Plato <plato>`, :person:`Aristotle <aristotle>`, :person:`Euclid <euclid>`, "
            ":person:`Archimedes <archimedes>`, :person:`Proclus <proclus>`, "
            ":person:`Aquinas <aquinas>`, :person:`Regiomontanus <regiomontanus>`, "
            ":person:`Kepler <kepler>`, :person:`Snellius & Huygens <snellius>`, "
            ":person:`Klein <klein>`, and :person:`Wildberger <wildberger>`)."
        ),
        "",
        "Units I–V — De Docta Ignorantia & Scripta Mathematica",
        "-----------------------------------------------------",
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "   :caption: De Docta Ignorantia & Scripta Mathematica",
        "",
    ]

    for unit in CODEX_UNITS:
        lines.append(f"   {unit.slug}/{unit.slug}-en")

    lines.extend(
        [
            "",
            "Critical Apparatus & Cross-Corpus Concordance",
            "---------------------------------------------",
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :caption: Critical Apparatus",
            "",
            "   concordance",
            "   bibliography",
            "   persons",
            "   glossary",
            "",
            ".. toctree::",
            "   :hidden:",
            "",
        ]
    )

    for unit in CODEX_UNITS:
        lines.append(f"   {unit.slug}/{unit.slug}-la")
        lines.append(f"   {unit.slug}/{unit.slug}-summary")
        lines.append(f"   {unit.slug}/{unit.slug}-notes")

    lines.append("")
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
    codex_dir.mkdir(parents=True, exist_ok=True)

    written: dict[str, Path] = {}

    if regen_figures:
        for fpath in export_all_codex_figures(root / "docsrc" / "_static" / "figures"):
            written[str(fpath.relative_to(root))] = fpath

    written.update(write_source_witnesses(root))
    written.update(write_apparatus_artifacts(root))
    written.update(write_concordance_artifacts(root))

    index_path = codex_dir / "index.rst"
    index_path.write_text(render_book_index_rst(), encoding="utf-8")
    written[str(index_path.relative_to(root))] = index_path

    for idx, unit in enumerate(CODEX_UNITS, start=1):
        verify_unit_parity(unit)
        unit_dir = codex_dir / unit.slug
        unit_dir.mkdir(parents=True, exist_ok=True)

        track_files = {
            f"{unit.slug}-en.rst": _render_unit_en_rst(unit, idx * 10),
            f"{unit.slug}-la.rst": _render_unit_la_rst(unit),
            f"{unit.slug}-summary.rst": _render_unit_summary_rst(unit),
            f"{unit.slug}-notes.rst": _render_unit_notes_rst(unit),
        }
        for fname, content in track_files.items():
            target = unit_dir / fname
            target.write_text(content, encoding="utf-8")
            written[str(target.relative_to(root))] = target

    return written

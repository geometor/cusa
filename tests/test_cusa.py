"""Comprehensive verification test suite for ``geometor-cusa``."""

from __future__ import annotations

import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from types import SimpleNamespace

import pytest
import sympy as sp
from geometor.model import quadrance, zero_test

from geometor.cusa import (
    CITATIONS_DATA,
    CODEX_UNITS,
    CONCORDANCE_ENTRIES,
    GLOSSARY_DATA,
    PERSONS_DATA,
    __version__,
    compute_flattening_triangle_metrics,
    compute_polygon_exhaustion_table,
    compute_tangent_pencil_table,
    construct_aurea_propositio,
    construct_circle_line_inversion,
    construct_cosmic_relativity_frame,
    construct_flattening_triangles,
    construct_generative_unfolding,
    construct_polygon_exhaustion,
    construct_tangent_circle_pencil,
    construct_transmutatio_isoperimetra,
    construct_transsumptio_ascent,
    register_latin_track,
    render_svg_string,
    verify_cusa_snellius_approximation,
    verify_mobius_inversion_coincidence,
    verify_sagitta_and_curvature_limits,
    verify_transmutatio_1445,
    verify_triangle_line_coincidence,
    verify_unit_parity,
)
from geometor.cusa.cli import main as cli_main

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_version_semver() -> None:
    """Verify package semantic version string."""
    assert __version__ == "0.1.5"


@pytest.mark.parametrize(
    ("name", "builder"),
    [
        ("circle_line_pencil", construct_tangent_circle_pencil),
        ("mobius_inversion", construct_circle_line_inversion),
        ("flattening_triangles", construct_flattening_triangles),
        ("polygon_exhaustion", construct_polygon_exhaustion),
        ("transmutatio_1445", construct_transmutatio_isoperimetra),
        ("aurea_propositio_1459", construct_aurea_propositio),
        ("generative_unfolding", construct_generative_unfolding),
        ("cosmic_relativity", construct_cosmic_relativity_frame),
        ("transsumptio_ascent", construct_transsumptio_ascent),
    ],
)
def test_all_nine_models_100_percent_symbolic_no_floats(
    name: str,
    builder: object,
) -> None:
    """Verify every Model disables auto_intersect and has zero sp.Float coordinates."""
    model = builder()  # type: ignore[operator]
    assert model.auto_intersect is False, f"{name} must disable auto_intersect"
    assert len(model.points) >= 4, f"{name} should construct nontrivial point set"
    for pt in model.points:
        assert not pt.x.has(sp.Float), f"sp.Float found in {name} point {model[pt].ID}.x"
        assert not pt.y.has(sp.Float), f"sp.Float found in {name} point {model[pt].ID}.y"


def test_circle_line_pencil_and_sagitta_asymptotics() -> None:
    """Verify DI I.13 radical secant sagittae and curvature/scaling limits."""
    rows = compute_tangent_pencil_table((1, 2, 4, 8))
    expected = [
        sp.Integer(1),
        2 - sp.sqrt(3),
        4 - sp.sqrt(15),
        8 - 3 * sp.sqrt(7),
    ]
    for row, exp in zip(rows, expected, strict=True):
        assert zero_test(row.secant_ordinate - exp)
        assert zero_test(row.secant_ordinate - row.rationalized_ordinate)

    # Strict monotonic decrease toward zero
    vals = [float(r.secant_ordinate.evalf()) for r in rows]
    assert vals == sorted(vals, reverse=True)

    limits = verify_sagitta_and_curvature_limits()
    x_sym = next(iter(limits["scaled_sagitta_limit"].free_symbols))
    assert limits["identity_holds"] is True
    assert limits["sagitta_limit"] == 0
    assert zero_test(limits["scaled_sagitta_limit"] - x_sym**2 / 2)
    assert limits["curvature_limit"] == 0


def test_mobius_circle_inversion_coincidence() -> None:
    """Verify conformal circle inversion mapping C_R to rational circles converging to line AB."""
    res = verify_mobius_inversion_coincidence((1, 2, 4, 8))
    assert res["origin_limit_v"] == 0
    assert res["limit_center_y"] == sp.Rational(-1, 2)
    assert res["limit_radius"] == sp.Rational(1, 2)

    entries = res["entries"]
    assert entries[0].inverted_center_y == sp.Rational(-1, 3)
    assert entries[0].inverted_radius == sp.Rational(1, 3)
    assert entries[1].inverted_center_y == sp.Rational(-2, 5)
    assert entries[2].inverted_center_y == sp.Rational(-4, 9)
    assert entries[-1].inverted_center_y == sp.Rational(-1, 2)
    assert entries[-1].inverted_radius == sp.Rational(1, 2)


def test_flattening_triangles_rational_trigonometry() -> None:
    """Verify DI I.14 Rational Trigonometry spreads, TSF == 0, and TQF residual 16/n^2 -> 0."""
    m1 = compute_flattening_triangle_metrics(1)
    assert m1.q_base == sp.Integer(4)
    assert m1.q_leg == sp.Integer(2)
    assert m1.spread_apex == sp.Integer(1)
    assert m1.spread_base == sp.Rational(1, 2)
    assert m1.triple_quad_residual == sp.Integer(16)

    m4 = compute_flattening_triangle_metrics(4)
    assert m4.q_leg == sp.Rational(17, 16)
    assert m4.spread_base == sp.Rational(1, 17)
    assert m4.spread_apex == sp.Rational(64, 289)
    assert m4.triple_quad_residual == sp.Integer(1)

    with pytest.raises(ValueError, match=">= 1"):
        compute_flattening_triangle_metrics(0)

    proof = verify_triangle_line_coincidence()
    assert proof["triple_spread_identity"] is True
    assert proof["limit_spread_apex"] == 0
    assert proof["limit_triple_quad"] == 0
    assert proof["limit_side_excess"] == 0


def test_polygon_exhaustion_monotonicity() -> None:
    """Verify DI I.3 & DMC 1453 monotone apothems and Archimedean pi bracketing."""
    rows = compute_polygon_exhaustion_table((3, 4, 6, 8, 12))
    assert len(rows) == 5
    apothems = [float(r.prima_linea_inradius.evalf()) for r in rows]
    in_perims = [float(r.inscribed_semiperimeter.evalf()) for r in rows]
    out_perims = [float(r.circumscribed_semiperimeter.evalf()) for r in rows]
    pi_val = float(sp.pi.evalf())

    assert apothems == sorted(apothems)
    assert in_perims == sorted(in_perims)
    assert out_perims == sorted(out_perims, reverse=True)
    for p_in, p_out in zip(in_perims, out_perims, strict=True):
        assert p_in < pi_val < p_out


def test_transmutatio_1445_sesquiquarta_proof() -> None:
    """Verify Cusa's 1445 5:4 sesquiquartal equilateral-triangle rectification."""
    res = verify_transmutatio_1445()
    assert zero_test(res["ae_length"] - sp.sqrt(7) / 4)
    assert zero_test(res["ah_radius"] - 5 * sp.sqrt(7) / 16)
    assert zero_test(res["pi_cusa_1445"] - 24 * sp.sqrt(21) / 35)
    # Lies inside Archimedes' classic 96-gon bounds 223/71 < pi_Cusa < 22/7
    pi_cusa_f = float(res["pi_cusa_1445"].evalf())
    assert 223 / 71 < pi_cusa_f < 22 / 7

    model = construct_transmutatio_isoperimetra()
    pt_a = model.get_element_by_ID("A")
    pt_e = model.get_element_by_ID("E")
    pt_h = model.get_element_by_ID("H")
    assert quadrance(pt_a, pt_e) == sp.Rational(7, 16)
    assert quadrance(pt_a, pt_h) == sp.Rational(175, 256)


def test_aurea_propositio_1459_three_ray_and_maclaurin() -> None:
    """Verify Cusa's 1458–1459 three-ray invariance and fifth-order Maclaurin error."""
    res = verify_cusa_snellius_approximation()
    assert res["tangent_ratio_equal"] is True
    assert res["coeff_theta_5"] == sp.Rational(1, 180)
    assert res["coeff_theta_7"] == sp.Rational(1, 1512)
    assert res["coeff_theta_9"] == sp.Rational(1, 25920)
    assert zero_test(res["pi_at_pi_over_6"] - (72 - 18 * sp.sqrt(3)) / 13)

    model = construct_aurea_propositio()
    pt_a = model.get_element_by_ID("A")
    pt_i = model.get_element_by_ID("I")
    pt_k = model.get_element_by_ID("K")
    pt_l = model.get_element_by_ID("L")
    len_ai = sp.sqrt(quadrance(pt_a, pt_i))
    len_ak = sp.sqrt(quadrance(pt_a, pt_k))
    len_al = sp.sqrt(quadrance(pt_a, pt_l))
    assert zero_test(len_ai + len_ak + len_al - 3)
    assert zero_test(2 * (len_ai - 1) - (1 - len_ak))


def test_bilingual_corpus_parity_klibansky_restorations_and_manifest() -> None:
    """Verify 1-to-1 Latin/English paragraph parity, Klibansky collations, and SHA-256 digests."""
    assert len(CODEX_UNITS) == 5
    reports = [verify_unit_parity(u) for u in CODEX_UNITS]
    assert sum(int(r["la_paragraph_count"]) for r in reports) == 124  # type: ignore[arg-type]

    # Check Klibansky's two restored homeoteleuton clauses in Unit III
    u3 = next(u for u in CODEX_UNITS if u.slug == "unit-3-coincidentia-figurarum")
    ch13 = next(s for s in u3.sections if s.section_id == "di-bk1-ch13")
    ch14 = next(s for s in u3.sections if s.section_id == "di-bk1-ch14")
    assert "arcus gh adhuc minoris circuli" in ch13.la_paragraphs[1][1]
    assert "tanto minus vincunt lineae bd et dc lineam bc" in ch14.la_paragraphs[2][1]

    manifest_path = REPO_ROOT / "resources" / "cusa" / "sources_manifest.json"
    assert manifest_path.is_file()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    assert manifest["unit_count"] == 5
    assert manifest["total_la_paragraphs"] == 124
    assert manifest["total_en_paragraphs"] == 124
    for u_entry in manifest["units"]:
        la_file = REPO_ROOT / u_entry["la_source"]
        en_file = REPO_ROOT / u_entry["en_source"]
        assert hashlib.sha256(la_file.read_bytes()).hexdigest() == u_entry["la_sha256"]
        assert hashlib.sha256(en_file.read_bytes()).hexdigest() == u_entry["en_sha256"]


def test_strict_content_code_separation_and_four_tracks() -> None:
    """Ensure zero embedded Python code in docsrc/de_docta_ignorantia/ and all 4 tracks exist."""
    codex_dir = REPO_ROOT / "docsrc" / "de_docta_ignorantia"
    assert (codex_dir / "index.rst").is_file()

    for unit in CODEX_UNITS:
        for suffix in ("en", "la", "summary", "notes"):
            track_path = codex_dir / unit.slug / f"{unit.slug}-{suffix}.rst"
            assert track_path.is_file(), f"Missing {track_path}"
            txt = track_path.read_text(encoding="utf-8")
            assert ":layout: book" in txt
            assert ".. code-block:: python" not in txt
            assert ".. py_file::" not in txt


def test_nine_euclid_graphic_svgs_valid_xml_and_interactive_refs() -> None:
    """Verify all 9 exported SVGs parse cleanly and expose interactive data-ref attributes."""
    fig_dir = REPO_ROOT / "docsrc" / "_static" / "figures"
    svgs = sorted(fig_dir.glob("*.svg"))
    assert len(svgs) == 9
    for svg_path in svgs:
        raw = svg_path.read_text(encoding="utf-8")
        assert 'class="euclid-graphic"' in raw
        assert "data-ref=" in raw
        assert "NaN" not in raw
        root = ET.fromstring(raw)
        assert root.tag.endswith("svg")

    inline_svg = render_svg_string(construct_aurea_propositio(), graphic_id="test-aurea")
    assert 'data-graphic-id="test-aurea"' in inline_svg


def test_sphinx_ext_latin_track_registration() -> None:
    """Verify register_latin_track labels -la 'Latin (1440 / 1514–1913)' right after -en."""
    mock_book = SimpleNamespace(
        _TRACK_SUFFIX_PATTERNS=[
            (r"^(.+)[._-]en$", "en", "English"),
            (r"^(.+)[._-]summary$", "summary", "Summary"),
            (r"^(.+)[._-]notes$", "notes", "Notes"),
        ],
        _AUX_TRACK_BASENAMES={"summary", "notes"},
        _AUX_TRACK_PATTERNS=[re.compile(r"^.+[._-]summary$"), re.compile(r"^.+[._-]notes$")],
        _extract_unit_stem=lambda basename, _doc_dir: re.sub(
            r"-(en|la|summary|notes)$",
            "",
            basename,
        ),
        detect_companion_tracks=lambda _env, pagename: [
            {"key": "en", "label": "English", "docname": "u/u-en", "active": pagename.endswith("-en")},
            {"key": "summary", "label": "Summary", "docname": "u/u-summary", "active": False},
            {"key": "notes", "label": "Notes", "docname": "u/u-notes", "active": False},
        ],
    )
    assert register_latin_track(mock_book) is True
    env = SimpleNamespace(found_docs={"u/u-en", "u/u-la", "u/u-summary", "u/u-notes"})
    tracks = mock_book.detect_companion_tracks(env, "u/u-la")
    assert [t["key"] for t in tracks] == ["en", "la", "summary", "notes"]
    assert tracks[1]["label"] == "Latin (1440 / 1514–1913)"
    assert tracks[1]["active"] is True


def test_apparatus_concordance_and_cli() -> None:
    """Verify apparatus counts, concordance JSON, and CLI verify subcommand."""
    assert len(GLOSSARY_DATA) >= 25
    assert len(PERSONS_DATA) >= 25
    assert len(CITATIONS_DATA) >= 25
    assert len(CONCORDANCE_ENTRIES) >= 15

    for fname in ("glossary.json", "persons.json", "citations.json", "concordance.json"):
        assert (REPO_ROOT / "resources" / fname).is_file()
        assert (REPO_ROOT / "resources" / "cusa" / fname).is_file()

    assert cli_main(["verify"]) == 0
    assert cli_main(["compile", "--no-figures"]) == 0

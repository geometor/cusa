"""Command-line interface for ``geometor-cusa``."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from geometor.cusa.coincidentia_circle_line import (
    verify_mobius_inversion_coincidence,
    verify_sagitta_and_curvature_limits,
)
from geometor.cusa.coincidentia_triangle_line import verify_triangle_line_coincidence
from geometor.cusa.compile_codex import compile_all_codex, verify_unit_parity
from geometor.cusa.concordance import write_concordance_artifacts
from geometor.cusa.polygon_exhaustion_and_complementa import (
    compute_polygon_exhaustion_table,
    verify_cusa_snellius_approximation,
    verify_transmutatio_1445,
)
from geometor.cusa.render import export_all_codex_figures
from geometor.cusa.units import CODEX_UNITS


def _default_repo_root() -> Path:
    """Resolve the repository root relative to ``src/geometor/cusa/cli.py``."""
    return Path(__file__).resolve().parents[3]


def run_verification_suite() -> dict[str, object]:
    """Execute all exact symbolic proofs and bilingual parity checks, returning a JSON report."""
    import sympy as sp

    sagitta = verify_sagitta_and_curvature_limits()
    mobius = verify_mobius_inversion_coincidence()
    triangle = verify_triangle_line_coincidence()
    polygons = compute_polygon_exhaustion_table()
    transmut = verify_transmutatio_1445()
    aurea = verify_cusa_snellius_approximation()
    parity = [verify_unit_parity(u) for u in CODEX_UNITS]
    return {
        "sagitta_limit_verified": bool(
            sagitta["identity_holds"] and sagitta["sagitta_limit"] == 0
        ),
        "mobius_inversion_verified": bool(
            mobius["limit_center_y"] == sp.Rational(-1, 2)
            and mobius["limit_radius"] == sp.Rational(1, 2)
        ),
        "triangle_coincidence_verified": bool(
            triangle["triple_spread_identity"]
            and triangle["limit_spread_apex"] == 0
            and triangle["limit_triple_quad"] == 0
        ),
        "polygon_exhaustion_steps": len(polygons),
        "transmutatio_1445_pi_exact": str(transmut["pi_cusa_1445"]),
        "transmutatio_1445_pi_float": round(float(transmut["pi_cusa_1445"].evalf()), 8),
        "aurea_propositio_1459_verified": bool(
            aurea["tangent_ratio_equal"] and aurea["coeff_theta_5"] == sp.Rational(1, 180)
        ),
        "codex_units_verified": len(parity),
        "total_bilingual_paragraphs": sum(int(p["la_paragraph_count"]) for p in parity),  # type: ignore[arg-type]
    }


def build_parser() -> argparse.ArgumentParser:
    """Build the ``geometor-cusa`` CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="geometor-cusa",
        description=(
            "Compile and verify the GEOMETOR Nicholas of Cusa 4-track Latin/English Book Codex "
            "and exact symbolic SymPy demonstrations."
        ),
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=_default_repo_root(),
        help="Repository root directory (defaults to package checkout root).",
    )
    sub = parser.add_subparsers(dest="command")

    p_compile = sub.add_parser("compile", help="Compile all 4-track RST units, SVGs & apparatus.")
    p_compile.add_argument(
        "--no-figures",
        action="store_true",
        help="Skip regenerating .euclid-graphic SVG figures.",
    )

    sub.add_parser("figures", help="Export all 9 .euclid-graphic SVG constructions.")
    sub.add_parser("concordance", help="Regenerate concordance.json and concordance.rst.")
    sub.add_parser("verify", help="Run all exact symbolic proofs and bilingual parity checks.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point for ``geometor-cusa``."""
    parser = build_parser()
    args = parser.parse_args(argv)
    root: Path = args.root.resolve()
    cmd = args.command or "verify"

    if cmd == "compile":
        written = compile_all_codex(root, regen_figures=not args.no_figures)
        print(f"Compiled {len(written)} codex artifacts under {root}")
        return 0
    if cmd == "figures":
        figs = export_all_codex_figures(root / "docsrc" / "_static" / "figures")
        print(f"Exported {len(figs)} .euclid-graphic SVGs under {root / 'docsrc/_static/figures'}")
        return 0
    if cmd == "concordance":
        written = write_concordance_artifacts(root)
        print(f"Wrote {len(written)} concordance files under {root}")
        return 0
    if cmd == "verify":
        report = run_verification_suite()
        print(json.dumps(report, indent=2))
        return 0

    parser.print_help()
    return 1

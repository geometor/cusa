"""GEOMETOR • cusa: Exact symbolic geometry and 4-track Latin/English Book Codex of Cusa."""

from __future__ import annotations

from geometor.cusa.apparatus import (
    CITATIONS_DATA,
    GLOSSARY_DATA,
    PERSONS_DATA,
    write_apparatus_artifacts,
)
from geometor.cusa.coincidentia_circle_line import (
    InversionCircleEntry,
    TangentPencilEntry,
    compute_tangent_pencil_table,
    construct_circle_line_inversion,
    construct_tangent_circle_pencil,
    verify_mobius_inversion_coincidence,
    verify_sagitta_and_curvature_limits,
)
from geometor.cusa.coincidentia_triangle_line import (
    FlatteningTriangleMetrics,
    compute_flattening_triangle_metrics,
    construct_flattening_triangles,
    verify_triangle_line_coincidence,
)
from geometor.cusa.compile_codex import (
    compile_all_codex,
    verify_unit_parity,
    write_source_witnesses,
)
from geometor.cusa.concordance import CONCORDANCE_ENTRIES, write_concordance_artifacts
from geometor.cusa.polygon_exhaustion_and_complementa import (
    PolygonExhaustionEntry,
    compute_polygon_exhaustion_table,
    construct_aurea_propositio,
    construct_cosmic_relativity_frame,
    construct_generative_unfolding,
    construct_polygon_exhaustion,
    construct_transmutatio_isoperimetra,
    construct_transsumptio_ascent,
    verify_cusa_snellius_approximation,
    verify_transmutatio_1445,
)
from geometor.cusa.render import export_all_codex_figures, export_svg, render_svg_string
from geometor.cusa.sphinx_ext import register_latin_track
from geometor.cusa.units import CODEX_UNITS, CodexUnitSpec

__version__ = "0.1.1"

__all__ = [
    "CITATIONS_DATA",
    "CODEX_UNITS",
    "CONCORDANCE_ENTRIES",
    "CodexUnitSpec",
    "FlatteningTriangleMetrics",
    "GLOSSARY_DATA",
    "InversionCircleEntry",
    "PERSONS_DATA",
    "PolygonExhaustionEntry",
    "TangentPencilEntry",
    "__version__",
    "compile_all_codex",
    "compute_flattening_triangle_metrics",
    "compute_polygon_exhaustion_table",
    "compute_tangent_pencil_table",
    "construct_aurea_propositio",
    "construct_circle_line_inversion",
    "construct_cosmic_relativity_frame",
    "construct_flattening_triangles",
    "construct_generative_unfolding",
    "construct_polygon_exhaustion",
    "construct_tangent_circle_pencil",
    "construct_transmutatio_isoperimetra",
    "construct_transsumptio_ascent",
    "export_all_codex_figures",
    "export_svg",
    "register_latin_track",
    "render_svg_string",
    "verify_cusa_snellius_approximation",
    "verify_mobius_inversion_coincidence",
    "verify_sagitta_and_curvature_limits",
    "verify_transmutatio_1445",
    "verify_triangle_line_coincidence",
    "verify_unit_parity",
    "write_apparatus_artifacts",
    "write_concordance_artifacts",
    "write_source_witnesses",
]

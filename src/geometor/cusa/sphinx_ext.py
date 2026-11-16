"""Sphinx extension customizing the Latin (``-la``) companion track label in ``publish``."""

from __future__ import annotations

import os
import re
from types import ModuleType
from typing import Any

_PATCHED_ATTR = "_geometor_cusa_la_patched"
_LA_LABEL = "Latin (1440 / 1514–1913)"
_LA_SUFFIX_ENTRY = (r"^(.+)[._-]la$", "la", _LA_LABEL)
_LA_AUX_PATTERN = re.compile(r"^.+[._-]la$")


def register_latin_track(book_mod: ModuleType | object | None = None) -> bool:
    """Register and label the ``la`` companion track on ``photon_platform.publish.book``.

    Ensures that ``<slug>-la.rst`` tracks appear immediately after ``en`` with the
    scholarly tab label ``"Latin (1440 / 1514–1913)"``.

    Args:
        book_mod: Optional pre-imported ``photon_platform.publish.book`` module (or mock
            object in unit tests). When ``None``, imports it dynamically.

    Returns:
        ``True`` if ``photon_platform.publish.book`` is available and patched, ``False``
        otherwise.
    """
    if book_mod is None:
        try:
            from photon_platform.publish import book as imported_book
        except ImportError:
            return False
        book_mod = imported_book

    if getattr(book_mod, _PATCHED_ATTR, False):
        return True

    suffix_patterns = getattr(book_mod, "_TRACK_SUFFIX_PATTERNS", None)
    if isinstance(suffix_patterns, list):
        replaced = False
        for idx, (pat, key, _lbl) in enumerate(suffix_patterns):
            if key == "la":
                suffix_patterns[idx] = (pat, "la", _LA_LABEL)
                replaced = True
        if not replaced:
            suffix_patterns.append(_LA_SUFFIX_ENTRY)

    aux_basenames = getattr(book_mod, "_AUX_TRACK_BASENAMES", None)
    if isinstance(aux_basenames, set):
        aux_basenames.add("la")

    aux_patterns = getattr(book_mod, "_AUX_TRACK_PATTERNS", None)
    if isinstance(aux_patterns, list) and not any(
        getattr(p, "pattern", "") == _LA_AUX_PATTERN.pattern for p in aux_patterns
    ):
        aux_patterns.append(_LA_AUX_PATTERN)

    orig_detect = getattr(book_mod, "detect_companion_tracks")
    extract_stem = getattr(book_mod, "_extract_unit_stem")

    def _detect_with_latin(env: object, pagename: str) -> list[dict[str, Any]]:
        found_docs: set[str] = set(getattr(env, "found_docs", set()))
        if not found_docs:
            return []

        tracks: list[dict[str, Any]] = [dict(tr) for tr in orig_detect(env, pagename)]
        doc_dir = os.path.dirname(pagename)
        basename = os.path.basename(pagename)
        stem = str(extract_stem(basename, doc_dir))

        def _qual(local_name: str) -> str:
            return f"{doc_dir}/{local_name}" if doc_dir else local_name

        is_unit_dir = not doc_dir or stem == os.path.basename(doc_dir)
        la_cands = [_qual(f"{stem}.la"), _qual(f"{stem}_la"), _qual(f"{stem}-la")]
        if is_unit_dir:
            la_cands.append(_qual("la"))

        la_doc = next((cand for cand in la_cands if cand in found_docs), None)
        if la_doc is None:
            return tracks

        # Update label and ordering if orig_detect already included la_doc
        existing_la = next((tr for tr in tracks if tr.get("docname") == la_doc), None)
        if existing_la is not None:
            existing_la["key"] = "la"
            existing_la["label"] = _LA_LABEL
            tracks = [tr for tr in tracks if tr.get("docname") != la_doc]
        elif not tracks:
            en_cands = [_qual(f"{stem}.en"), _qual(f"{stem}_en"), _qual(f"{stem}-en")]
            if is_unit_dir:
                en_cands.append(_qual("en"))
                en_cands.append(_qual("index"))
            en_doc = next((cand for cand in en_cands if cand in found_docs), None)
            if en_doc and en_doc != la_doc:
                return [
                    {
                        "key": "en",
                        "label": "English",
                        "docname": en_doc,
                        "active": en_doc == pagename,
                    },
                    {
                        "key": "la",
                        "label": _LA_LABEL,
                        "docname": la_doc,
                        "active": la_doc == pagename,
                    },
                ]
            return []

        la_entry: dict[str, Any] = (
            existing_la
            if existing_la is not None
            else {
                "key": "la",
                "label": _LA_LABEL,
                "docname": la_doc,
                "active": la_doc == pagename,
            }
        )

        insert_idx = len(tracks)
        for idx, tr in enumerate(tracks):
            if tr.get("key") == "en":
                insert_idx = idx + 1
                break
            if tr.get("key") in {"commentary", "summary", "notes", "folio"}:
                insert_idx = idx
                break
        tracks.insert(insert_idx, la_entry)
        return tracks

    setattr(book_mod, "detect_companion_tracks", _detect_with_latin)
    setattr(book_mod, _PATCHED_ATTR, True)
    return True


def setup(app: object) -> dict[str, Any]:
    """Sphinx extension entry point registering the Cusanus Latin companion track.

    Args:
        app: Active Sphinx application object.

    Returns:
        Sphinx extension metadata dictionary.
    """
    _ = app
    register_latin_track()
    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

"""Resolve the XML's declared schema → the right xsdata root dataclass.

S1000D documents declare their schema via ``xsi:noNamespaceSchemaLocation``
on the root element. The URL ends in ``proced.xsd``, ``ddn.xsd``, etc.; the
basename (without ``.xsd``) is what we use as the ``schema_source`` short name
throughout the pipeline.

Pure functions only — no side effects, no IO into the model packages until
the registry is asked to dispatch.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import NamedTuple

XSI_NS = "{http://www.w3.org/2001/XMLSchema-instance}"
_SCHEMA_BASENAME_RE = re.compile(r"([A-Za-z0-9_]+)\.xsd\s*$")


class SchemaInfo(NamedTuple):
    schema_source: str  # short name, e.g. "proced"
    schema_location: str  # full URI as declared in the XML


def resolve_schema_from_root(root_attrib: dict[str, str]) -> SchemaInfo:
    """Given an lxml-style attribute dict from the document root, return the
    short schema name + the full schema location URI.

    Raises ValueError if no schema location is declared.
    """
    location = root_attrib.get(f"{XSI_NS}noNamespaceSchemaLocation")
    if location is None:
        # Fall back to plain noNamespaceSchemaLocation (rare; defensive only)
        location = root_attrib.get("noNamespaceSchemaLocation")
    if not location:
        raise ValueError(
            "Document root has no xsi:noNamespaceSchemaLocation attribute; "
            "cannot determine schema."
        )
    m = _SCHEMA_BASENAME_RE.search(location)
    if not m:
        raise ValueError(
            f"Cannot parse schema basename from location: {location!r}"
        )
    return SchemaInfo(schema_source=m.group(1), schema_location=location)


def schema_source_from_path(xsd_path: str | Path) -> str:
    """Short-name helper: ``schemas/proced.xsd`` → ``"proced"``."""
    return Path(xsd_path).stem


__all__ = ["SchemaInfo", "XSI_NS", "resolve_schema_from_root", "schema_source_from_path"]

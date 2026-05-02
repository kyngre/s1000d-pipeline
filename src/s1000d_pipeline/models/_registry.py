"""Schema-source → root dataclass dispatch.

Lazy imports keep startup cheap: parsing one DM type doesn't load the model
packages for the others. Each ``schema_source`` short name is the basename
of the corresponding flat XSD.

Adding a new schema:

1. Drop ``<name>.xsd`` into ``schemas/``.
2. Add an ``(<short>, "<root_python_class>")`` entry to ``_ROOT_CLASS_NAMES``.
3. Run ``python -m s1000d_pipeline.tools.generate_models``.
"""

from __future__ import annotations

import importlib
from typing import Type

# Map: schema short name → Python class name of the root dataclass.
# Determined empirically from each XSD's first ``<xs:element name="…"/>``
# declaration. Most S1000D schemas root at ``<dmodule>``; a handful have
# their own root.
_ROOT_CLASS_NAMES: dict[str, str] = {
    # Special roots
    "ddn": "Ddn",
    "pm": "Pm",
    "dml": "Dml",
    "update": "DataUpdateFile",
    "icnmetadata": "IcnMetadataFile",
    # All other DM types: <dmodule> root
    "proced": "Dmodule",
    "descript": "Dmodule",
    "ipd": "Dmodule",
    "brex": "Dmodule",
    "frontmatter": "Dmodule",
    "fault": "Dmodule",
    "checklist": "Dmodule",
    "crew": "Dmodule",
    "sb": "Dmodule",
    "schedul": "Dmodule",
    "process": "Dmodule",
    "learning": "Dmodule",
    "comrep": "Dmodule",
    "wrngdata": "Dmodule",
    "wrngflds": "Dmodule",
    "appliccrossreftable": "Dmodule",
    "condcrossreftable": "Dmodule",
    "prdcrossreftable": "Dmodule",
    "brdoc": "Dmodule",
    "container": "Dmodule",
    "comment": "Comment",
}


def get_root_class(schema_source: str) -> Type:
    """Return the xsdata root dataclass for the given schema short name.

    Raises ``KeyError`` for unregistered schemas.
    """
    class_name = _ROOT_CLASS_NAMES.get(schema_source)
    if class_name is None:
        raise KeyError(
            f"Unknown schema source: {schema_source!r}. Add an entry to "
            f"s1000d_pipeline/models/_registry.py and regenerate the "
            f"corresponding model package."
        )
    module = importlib.import_module(
        f"s1000d_pipeline.models.{schema_source}"
    )
    cls = getattr(module, class_name, None)
    if cls is None:
        raise ImportError(
            f"Schema {schema_source!r} is registered as rooting at "
            f"{class_name!r} but that class is not exported from "
            f"s1000d_pipeline.models.{schema_source}. Did model regeneration "
            f"complete? Re-run `python -m s1000d_pipeline.tools.generate_models`."
        )
    return cls


def known_schemas() -> list[str]:
    """Schema short names the registry knows about."""
    return sorted(_ROOT_CLASS_NAMES.keys())


__all__ = ["get_root_class", "known_schemas"]

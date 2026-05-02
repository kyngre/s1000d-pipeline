"""Extract DOCTYPE entity declarations.

xsdata's parser drops DOCTYPE entirely. S1000D procedural data modules use
DOCTYPE to declare ICN graphics:

    <!DOCTYPE dmodule [
      <!ENTITY ICN-C0419-S1000D0361-001-01
               SYSTEM "ICN-C0419-S1000D0361-001-01.CGM" NDATA cgm>
      <!NOTATION cgm PUBLIC "-//USA-DOD//NOTATION ...">
    ]>

The frontend needs the entity table to resolve ``<graphic infoEntityIdent="…"/>``
references without a separate API call. We capture it here as a small,
self-contained side-channel.

Implementation choice: regex over the raw text. The DOCTYPE block in S1000D
files is small (a few hundred bytes), well-formed, and confined to the
document head. lxml's DTD-iteration API is awkward across versions and adds
no value here.
"""

from __future__ import annotations

import re
from pathlib import Path

from s1000d_pipeline.ast.nodes import DocTypeEntity

# Match the inline DOCTYPE subset: `<!DOCTYPE name [ ... ]>`
_DOCTYPE_BLOCK_RE = re.compile(
    r"<!DOCTYPE\s+\S+\s*\[(?P<body>.*?)\]\s*>", re.DOTALL
)
_ENTITY_SYSTEM_RE = re.compile(
    r"""
    <!ENTITY \s+
    (?P<name>[\w\-\.]+) \s+
    SYSTEM \s+ "(?P<systemId>[^"]+)"
    (?: \s+ NDATA \s+ (?P<ndata>\w+) )?
    \s* >
    """,
    re.VERBOSE,
)
_ENTITY_PUBLIC_RE = re.compile(
    r"""
    <!ENTITY \s+
    (?P<name>[\w\-\.]+) \s+
    PUBLIC \s+ "(?P<publicId>[^"]+)" \s+ "(?P<systemId>[^"]+)"
    (?: \s+ NDATA \s+ (?P<ndata>\w+) )?
    \s* >
    """,
    re.VERBOSE,
)
_HEAD_BYTES = 32_768


def extract_doctype_entities(xml_path: str | Path) -> dict[str, DocTypeEntity]:
    """Return a name → entity-record map for the document's inline DOCTYPE.

    Returns ``{}`` if there is no DOCTYPE or no entity declarations.
    """
    head = _read_head(Path(xml_path))
    block = _DOCTYPE_BLOCK_RE.search(head)
    if not block:
        return {}
    body = block.group("body")
    out: dict[str, DocTypeEntity] = {}
    for m in _ENTITY_SYSTEM_RE.finditer(body):
        rec: DocTypeEntity = {"systemId": m.group("systemId")}
        if m.group("ndata"):
            rec["ndata"] = m.group("ndata")
        out[m.group("name")] = rec
    for m in _ENTITY_PUBLIC_RE.finditer(body):
        rec: DocTypeEntity = {
            "systemId": m.group("systemId"),
            "publicId": m.group("publicId"),
        }
        if m.group("ndata"):
            rec["ndata"] = m.group("ndata")
        out[m.group("name")] = rec
    return out


def _read_head(path: Path) -> str:
    """Read the first ~32KB. Plenty for an inline DOCTYPE declaration."""
    with path.open("rb") as f:
        raw = f.read(_HEAD_BYTES)
    return raw.decode("utf-8", errors="replace")


__all__ = ["extract_doctype_entities"]

"""End-to-end XML → ``ParsedDocument`` orchestrator.

Coordinates three concerns kept separate elsewhere:

* schema dispatch — picks the right xsdata root class via the registry.
* DOCTYPE side-channel — captures entity declarations xsdata drops.
* xsdata parsing — actual typed-tree construction.

Returns a ``ParsedDocument`` carrying everything the AST builder needs to
produce a self-contained ``DocumentNode``.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from lxml import etree
from xsdata.formats.dataclass.parsers import XmlParser

from s1000d_pipeline.ast.nodes import DocTypeEntity
from s1000d_pipeline.models._registry import get_root_class
from s1000d_pipeline.parsing.doctype import extract_doctype_entities
from s1000d_pipeline.parsing.schema_resolver import (
    XSI_NS,
    SchemaInfo,
    resolve_schema_from_root,
)


@dataclass
class ParsedDocument:
    """Everything the AST builder needs from a parsed S1000D document."""

    instance: Any  # xsdata root dataclass instance
    schema_source: str  # e.g. "proced"
    schema_location: str  # full URI from xsi:noNamespaceSchemaLocation
    doctype_entities: dict[str, DocTypeEntity] = field(default_factory=dict)
    xml_namespaces: dict[str, str] = field(default_factory=dict)
    xml_version: str = "1.0"
    xml_encoding: str = "UTF-8"
    standalone: bool | None = None


def parse_document(xml_path: str | Path) -> ParsedDocument:
    """Parse an S1000D XML file into a fully-typed ``ParsedDocument``.

    Steps:
    1. lxml pre-pass: read prolog, namespace map, and root attributes
       (cheap; we use the same parsed tree for nothing else, but lxml's
       prolog access is the only practical way to get xml_version/encoding).
    2. Resolve schema from root attributes.
    3. DOCTYPE side-channel: regex over the file head for entity declarations.
    4. xsdata parse using the registry-resolved root class.
    """
    path = Path(xml_path)

    # 1. Prolog + root attributes via lxml. We disable network and DTD loading
    #    so the parser doesn't try to resolve external entities at parse time.
    lxml_parser = etree.XMLParser(
        load_dtd=False,
        resolve_entities=False,
        no_network=True,
        huge_tree=True,
    )
    tree = etree.parse(str(path), lxml_parser)
    root = tree.getroot()
    docinfo = tree.docinfo

    # 2. Schema dispatch
    schema_info: SchemaInfo = resolve_schema_from_root(dict(root.attrib))
    root_class = get_root_class(schema_info.schema_source)

    # 3. DOCTYPE entities (lxml drops their bodies on parse with the flags
    #    above, so we go to the file directly).
    doctype_entities = extract_doctype_entities(path)

    # 4. xsdata parse — note: xsdata can read the file directly; we pass the
    #    path string so xsdata handles the encoding declaration itself.
    instance = XmlParser().parse(str(path), root_class)

    namespaces = {
        prefix: uri
        for prefix, uri in (root.nsmap or {}).items()
        if prefix is not None
    }

    return ParsedDocument(
        instance=instance,
        schema_source=schema_info.schema_source,
        schema_location=schema_info.schema_location,
        doctype_entities=doctype_entities,
        xml_namespaces=namespaces,
        xml_version=docinfo.xml_version or "1.0",
        xml_encoding=(docinfo.encoding or "UTF-8").upper(),
        standalone=docinfo.standalone,
    )


__all__ = ["ParsedDocument", "parse_document", "XSI_NS"]

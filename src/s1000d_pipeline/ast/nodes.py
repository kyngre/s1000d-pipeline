"""Canonical AST node shapes.

Three node kinds: ``DocumentNode`` (root wrapper), ``ElementNode`` (any XML
element), ``TextNode`` (string leaf inside mixed content).

All three share the ``{type, attributes, metadata, children}`` skeleton; text
nodes additionally carry ``text``. Field-level invariants live in the
docstrings below — see also ``s1000d_pipeline/ast/builder.py`` which is the
sole producer of these shapes.

Round-trip contract (must survive XML → AST → JSON → AST → XML):

* ``type``                    — original camelCase XML element name
* ``attributes``              — verbatim XML attributes, typed by xsdata
* ``children`` ordering       — never permuted
* ``TextNode.text``           — character-exact, whitespace included
* ``DocumentMetadata``        — rootElement, schemaLocation, xmlNamespaces,
                                 xmlVersion, xmlEncoding, docTypeEntities

Editor-only (derived; can be regenerated from the above):

* ``nodeKind``
* All of ``ElementMetadata``  — id, refIds, dataclassName, schemaSource,
                                 mixedContent, void, sourcePath, whitespace
"""

from typing import Literal, NotRequired, TypedDict, Union

# ── Attribute value shape ───────────────────────────────────────────────────
# xsdata returns typed Python values; the serializer normalizes Decimal → str,
# Enum → enum.value, date/datetime → ISO 8601, list[str] (tokens) → JSON array.
# We keep typed numbers/booleans because xsdata re-parses them losslessly on
# the way back to XML.
JsonAttrValue = Union[str, int, float, bool, list[str], None]

NodeKind = Literal["document", "block", "inline", "text"]


# ── Text leaf ───────────────────────────────────────────────────────────────
class TextNode(TypedDict):
    """A string fragment inside a mixed-content element.

    ``text`` preserves whitespace exactly. The optional ``whitespace`` flag in
    metadata-style position is omitted here — see ``ElementNode`` below for the
    convention. For text nodes we keep the shape minimal because the editor
    walks them by ``type == "#text"``.
    """

    type: Literal["#text"]
    nodeKind: Literal["text"]
    text: str
    whitespace: NotRequired[bool]


# ── Element metadata ────────────────────────────────────────────────────────
class ElementMetadata(TypedDict, total=False):
    """Editor-facing derived state. Never used for round-trip serialization."""

    id: str  # mirror of attributes["id"], hoisted for fast lookup
    refIds: list[str]  # union of applicRefId, internalRefId, controlAuthorityRefs, …
    dataclassName: str  # xsdata class name, e.g. "ProceduralStep"
    schemaSource: str  # short schema name, e.g. "proced"
    mixedContent: bool  # XSD declared mixed="true" on this element's type
    void: bool  # XSD allows no element children (attribute-only payload)
    sourcePath: str  # dotted path inside the dataclass tree (debug aid)


class ElementNode(TypedDict):
    type: str  # original camelCase XML element name
    nodeKind: NodeKind  # "block" or "inline" — "document" reserved for root
    attributes: dict[str, JsonAttrValue]
    metadata: ElementMetadata
    children: list["AstNode"]


# ── Document wrapper ────────────────────────────────────────────────────────
class DocTypeEntity(TypedDict):
    systemId: str
    ndata: NotRequired[str]
    publicId: NotRequired[str]


class DocumentMetadata(TypedDict, total=False):
    rootElement: str
    schemaLocation: str
    schemaSource: str
    xmlNamespaces: dict[str, str]
    xmlVersion: str
    xmlEncoding: str
    standalone: bool
    docTypeEntities: dict[str, DocTypeEntity]


class DocumentNode(TypedDict):
    type: Literal["#document"]
    nodeKind: Literal["document"]
    attributes: dict[str, JsonAttrValue]  # always {}; kept for shape uniformity
    metadata: DocumentMetadata
    children: list[ElementNode]  # exactly one: the root XML element


AstNode = Union[DocumentNode, ElementNode, TextNode]


# ── Constructors (small helpers used by builder.py) ─────────────────────────
def make_text(text: str, whitespace: bool = False) -> TextNode:
    node: TextNode = {"type": "#text", "nodeKind": "text", "text": text}
    if whitespace:
        node["whitespace"] = True
    return node

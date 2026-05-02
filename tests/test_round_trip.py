"""Round-trip integrity tests.

Two complementary assertions:

A. **XML → AST is lossless.** Every element, attribute, and non-trivial text
   fragment in the original document appears in the AST. Walks the lxml-parsed
   tree as ground truth and verifies the AST contains the same multiset.

B. **xsdata round-trips structurally.** Parse the XML via the pipeline,
   serialize the resulting dataclass back via xsdata, re-parse the
   serialization, and assert the two ``ParsedDocument`` dataclass trees are
   structurally identical. This is the strongest check we can run before
   ``ast/reverse.py`` exists — it validates that the pipeline's source of
   truth (the xsdata instance) survives serialization, which is the same
   serializer ``reverse.py`` will eventually use.

Whitespace handling: xsdata's serializer reformats inter-element indentation,
so byte-equality is not a goal. We compare *content* — element names,
attribute name/value pairs, text-stripped non-empty text fragments — across
both directions.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

import pytest
from lxml import etree
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from s1000d_pipeline import build_ast, parse_document
from s1000d_pipeline.models._registry import get_root_class
from s1000d_pipeline.parsing.parser import ParsedDocument
from s1000d_pipeline.parsing.schema_resolver import resolve_schema_from_root


# ── Helpers: walk an lxml tree and the AST in matching ways ─────────────────


def _local_name(tag: str) -> str:
    """Drop ``{namespace}`` prefix from a Clark-notation tag."""
    return tag.split("}", 1)[1] if tag.startswith("{") else tag


def _local_attr(name: str) -> str:
    """Strip namespace from an attribute name (for xlink/xml: attributes)."""
    return name.split("}", 1)[1] if name.startswith("{") else name


_LEADING_PLUS_NUMERIC = re.compile(r"^\+\d")


def _normalize_text(s: str | None) -> str:
    """Whitespace-fold for content comparison. Empty after fold → ''.

    Also strips a leading ``+`` from numeric-looking strings to match xsdata's
    xs:decimal canonicalization (e.g. ``"+0.8"`` ≡ ``"0.8"`` per XSD). Without
    this, every ``<quantityValue>+0.8</quantityValue>`` would look "lost"
    after typing through xsdata, when in fact it round-trips losslessly.
    """
    if not s:
        return ""
    folded = re.sub(r"\s+", " ", s).strip()
    if _LEADING_PLUS_NUMERIC.match(folded):
        folded = folded[1:]
    return folded


def _lxml_inventory(root: etree._Element) -> dict[str, Counter]:
    """Multisets of (path/element/attribute/text) appearances from an lxml tree."""
    elements: Counter = Counter()
    attrs: Counter = Counter()  # (element_local_name, attr_local_name, value)
    texts: Counter = Counter()  # non-trivial text fragments

    for elem in root.iter():
        if not isinstance(elem.tag, str):
            continue  # skip comments / PIs
        ename = _local_name(elem.tag)
        elements[ename] += 1
        for k, v in elem.attrib.items():
            local = _local_attr(k)
            # Skip xsi:noNamespaceSchemaLocation: it's document-level metadata
            # in our AST, not an element attribute.
            if local == "noNamespaceSchemaLocation":
                continue
            attrs[(ename, local, v)] += 1
        for t in (elem.text, elem.tail):
            n = _normalize_text(t)
            if n:
                texts[n] += 1

    return {"elements": elements, "attrs": attrs, "texts": texts}


def _ast_inventory(ast_node: dict) -> dict[str, Counter]:
    """Same multiset shape, walked over the AST. Skips the #document wrapper.

    Each AST attribute contributes one tuple PER permissible string form of
    its typed value. For ``bool``, that means both ``"true"``/``"false"`` and
    ``"1"``/``"0"`` so the XML side can match whichever it used.
    """
    elements: Counter = Counter()
    attrs: Counter = Counter()
    texts: Counter = Counter()

    def walk(node: dict) -> None:
        ntype = node.get("type")
        if ntype == "#text":
            n = _normalize_text(node.get("text"))
            if n:
                texts[n] += 1
            return
        if ntype == "#document":
            for c in node.get("children", []):
                walk(c)
            return
        elements[ntype] += 1
        for k, v in (node.get("attributes") or {}).items():
            for s in _attr_value_strings(v):
                attrs[(ntype, k, s)] += 1
        for c in node.get("children", []):
            walk(c)

    walk(ast_node)
    return {"elements": elements, "attrs": attrs, "texts": texts}


def _attr_value_strings(v) -> set[str]:
    """All string forms an XML attribute might take to encode this typed value.

    xsdata returns typed values; the XML may have stored them in any form the
    schema's type system permits. ``boolean="1"`` and ``boolean="true"`` both
    decode to Python ``True``; we accept both on the way back.
    """
    if isinstance(v, bool):
        return {"true", "false"} & ({"true"} if v else {"false"}) | {"1" if v else "0"}
    if isinstance(v, list):
        # Token-list attributes (xsd: list of XX) round-trip via space-join
        return {" ".join(str(x) for x in v)}
    if v is None:
        return {""}
    return {str(v)}


# ── A. XML → AST lossless ───────────────────────────────────────────────────


def _assert_ast_covers_xml(xml_path: Path) -> None:
    parsed = parse_document(xml_path)
    ast = build_ast(parsed)

    lxml_parser = etree.XMLParser(load_dtd=False, resolve_entities=False, no_network=True)
    tree = etree.parse(str(xml_path), lxml_parser)
    root = tree.getroot()

    xml_inv = _lxml_inventory(root)
    ast_inv = _ast_inventory(ast)

    # XML ⊆ AST. AST may legitimately carry extras: xsdata resolves XSD
    # ``default``/``fixed`` attribute values (e.g. xlink ``type="simple"``,
    # ``show="replace"``, ``actuate="onRequest"`` on every dmRef/internalRef).
    # That is information addition, not information loss — it round-trips
    # cleanly because xsdata will re-emit the same defaults next time.
    missing_elements = xml_inv["elements"] - ast_inv["elements"]
    assert not missing_elements, (
        f"Elements missing from AST for {xml_path.name}: {dict(missing_elements)}"
    )

    missing_attrs = xml_inv["attrs"] - ast_inv["attrs"]
    assert not missing_attrs, (
        f"Attributes missing from AST for {xml_path.name}\n"
        f"  examples: {dict(list(missing_attrs.items())[:5])}"
    )

    missing_text = xml_inv["texts"] - ast_inv["texts"]
    assert not missing_text, (
        f"Text fragments missing from AST for {xml_path.name}: "
        f"{list(missing_text.items())[:5]}"
    )


def test_golden_xml_to_ast_lossless(golden_samples):
    assert golden_samples, "no golden samples discovered"
    for sample in golden_samples:
        _assert_ast_covers_xml(sample)


def test_bike_xml_to_ast_lossless(bike_sample):
    _assert_ast_covers_xml(bike_sample)


# ── B. xsdata serialize → re-parse equality ────────────────────────────────


def _xsdata_round_trip_equal(xml_path: Path) -> None:
    parsed: ParsedDocument = parse_document(xml_path)

    serializer = XmlSerializer()
    serialized = serializer.render(parsed.instance)

    reparsed_parser = XmlParser()
    root_class = get_root_class(parsed.schema_source)
    reparsed = reparsed_parser.from_string(serialized, root_class)

    # xsdata dataclasses use ``@dataclass`` with eq=True by default, so == is
    # a structural recursive comparison.
    assert parsed.instance == reparsed, (
        f"xsdata round-trip mismatch for {xml_path.name} "
        f"(schema {parsed.schema_source!r})"
    )


def test_golden_xsdata_round_trip(golden_samples):
    assert golden_samples
    for sample in golden_samples:
        _xsdata_round_trip_equal(sample)


def test_bike_xsdata_round_trip(bike_sample):
    _xsdata_round_trip_equal(bike_sample)


# ── Parametrize over the bike data set ──────────────────────────────────────


def pytest_generate_tests(metafunc):
    """Parametrize ``bike_sample`` over every .XML in the bike data set."""
    if "bike_sample" not in metafunc.fixturenames:
        return
    from conftest import _bike_samples  # local import to avoid cycle

    samples = _bike_samples()
    if not samples:
        metafunc.parametrize("bike_sample", [], ids=[])
        return
    metafunc.parametrize(
        "bike_sample", samples, ids=lambda p: p.name
    )


# ── Schema-resolver unit ────────────────────────────────────────────────────


def test_resolve_schema_basic():
    info = resolve_schema_from_root(
        {"{http://www.w3.org/2001/XMLSchema-instance}noNamespaceSchemaLocation":
             "http://www.s1000d.org/S1000D_6/xml_schema_flat/proced.xsd"}
    )
    assert info.schema_source == "proced"


def test_resolve_schema_missing():
    with pytest.raises(ValueError):
        resolve_schema_from_root({})

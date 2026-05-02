"""Recursive xsdata-dataclass → AST builder.

The walker is *schema-agnostic*: it consumes whatever ``xsdata`` produced for
any flat S1000D XSD by reading ``dataclasses.fields()`` and the per-field
``metadata`` dict that ``xsdata`` populates. There is **one** explicit table
elsewhere — the inline/block lookup in ``classify.py``.

The four xsdata field-metadata patterns we handle:

1. ``{"type": "Attribute", "name": <camelCase>}``
       → entry in ``attributes`` dict.
2. ``{"type": "Element", "name": <camelCase>}``
       → child element (or list of). Value can be a dataclass instance, a raw
         string (for ``xs:string``-typed elements), or an ``Enum`` (for
         simple-typed elements). All three become ``ElementNode``s with a
         single ``TextNode`` child where appropriate.
3. ``{"type": "Wildcard", "mixed": True, "choices": (...)}``
       → mixed content. ``content: list[object]`` interleaves text fragments
         (``str``) and dataclass instances. We walk the list **in order** and
         emit ``TextNode``s and ``ElementNode``s accordingly. The XML tag for a
         dataclass child comes from the choices table.
4. Field with no ``metadata["type"]`` and ``name == "value"``
       → simple-content text on the *current* element. Emitted as a single
         child ``TextNode``.

Round-trip safety lives in ``attributes`` (verbatim, typed) and ``children``
(ordered). Everything in ``metadata`` is derived and re-derivable.
"""

from __future__ import annotations

import dataclasses
import warnings
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import Any, Iterable

# Module-level dedupe set for unclassified-in-mixed warnings.
# Using ``warnings.warn`` would route through Python's warning filters and
# emit one record per call-site; we want one record per (parent, child) pair
# regardless of where in the tree it shows up. The sweep test reads this set
# directly via ``unclassified_inline_candidates()``.
_UNCLASSIFIED_SEEN: set[tuple[str, str]] = set()


class UnclassifiedInlineWarning(UserWarning):
    """Emitted when a child element inside a mixed-content parent is not in
    ``classify.INLINE`` or ``classify.CONTEXT_SENSITIVE``. Defaults safely to
    ``block`` — see ``classify.py`` for the rationale.
    """


def _warn_unclassified(*, parent_cls: type, child_name: str) -> None:
    key = (parent_cls.__name__, child_name)
    if key in _UNCLASSIFIED_SEEN:
        return
    _UNCLASSIFIED_SEEN.add(key)
    warnings.warn(
        f"Unclassified inline candidate: <{child_name}> inside "
        f"mixed-content <{parent_cls.__name__}>",
        UnclassifiedInlineWarning,
        stacklevel=3,
    )


def unclassified_inline_candidates() -> set[tuple[str, str]]:
    """Return the (parent_class, child_xml_name) pairs warned during this run."""
    return set(_UNCLASSIFIED_SEEN)


def reset_unclassified_inline_candidates() -> None:
    """Clear the dedupe set. Used by the sweep test between runs."""
    _UNCLASSIFIED_SEEN.clear()

from s1000d_pipeline.ast.classify import classify, is_unclassified_in_mixed
from s1000d_pipeline.ast.nodes import (
    DocumentMetadata,
    DocumentNode,
    ElementMetadata,
    ElementNode,
    JsonAttrValue,
    TextNode,
    make_text,
)
from s1000d_pipeline.parsing.parser import ParsedDocument

# Attribute names that are interesting for refIds hoisting (editor convenience).
_REF_ATTRS = (
    "id",
    "applicRefId",
    "internalRefId",
    "controlAuthorityRefs",
    "reasonForUpdateRefIds",
    "derivativeClassificationRefId",
)


# ────────────────────────────── Public API ──────────────────────────────────


def build_ast(parsed: ParsedDocument) -> DocumentNode:
    """Convert a ``ParsedDocument`` into a ``DocumentNode``."""
    instance = parsed.instance
    root_xml_name = _xml_name_of_class(type(instance))
    root_element = _build_element(
        instance=instance,
        xml_name=root_xml_name,
        schema_source=parsed.schema_source,
        parent_is_mixed=False,
        path=root_xml_name,
    )

    doc_metadata: DocumentMetadata = {
        "rootElement": root_xml_name,
        "schemaLocation": parsed.schema_location,
        "schemaSource": parsed.schema_source,
        "xmlVersion": parsed.xml_version,
        "xmlEncoding": parsed.xml_encoding,
    }
    if parsed.xml_namespaces:
        doc_metadata["xmlNamespaces"] = dict(parsed.xml_namespaces)
    if parsed.standalone is not None:
        doc_metadata["standalone"] = parsed.standalone
    if parsed.doctype_entities:
        doc_metadata["docTypeEntities"] = dict(parsed.doctype_entities)

    return {
        "type": "#document",
        "nodeKind": "document",
        "attributes": {},
        "metadata": doc_metadata,
        "children": [root_element],
    }


# ───────────────────────── Element-level walker ─────────────────────────────


def _build_element(
    *,
    instance: Any,
    xml_name: str,
    schema_source: str,
    parent_is_mixed: bool,
    path: str,
) -> ElementNode:
    """Build an ElementNode from a dataclass instance plus its XML name.

    ``xml_name`` is passed in (rather than re-derived) because in mixed-content
    fields the same dataclass type can appear under different XML names — the
    name comes from the choices table on the parent's wildcard field.
    """
    cls = type(instance)
    attributes: dict[str, JsonAttrValue] = {}
    children: list[Any] = []
    # xsdata adds a defensive ``content: list[object]`` wildcard to many element
    # types (e.g. anything with xlink attributes) even when the XSD doesn't
    # declare them mixed. Schema-level flags would over-report, so we compute
    # ``mixedContent`` and ``void`` from what we actually emit. ``parent_mixed``
    # propagation still uses the schema-level flag — it's what governs the
    # *child*'s classification when the parent is theoretically mixed.
    schema_says_mixed = _schema_has_mixed_wildcard(cls)

    for f in dataclasses.fields(cls):
        meta = f.metadata
        meta_type = meta.get("type")
        meta_name = meta.get("name") or f.name
        value = getattr(instance, f.name)

        if meta_type == "Attribute":
            if _is_empty_attr(value):
                continue
            attributes[meta_name] = _encode_attr(value)
            continue

        if meta_type == "Element":
            for item, item_name in _element_items(value, meta_name):
                children.append(
                    _element_from_value(
                        value=item,
                        xml_name=item_name,
                        schema_source=schema_source,
                        parent_is_mixed=schema_says_mixed,
                        path=f"{path}.{item_name}",
                    )
                )
            continue

        if meta_type == "Elements":
            # xsdata "Elements" = an unordered choice group. Each item carries
            # its own XML name from the per-field choices table.
            choices = meta.get("choices") or ()
            for item in value or []:
                item_name = _xml_name_for_choice(item, choices)
                children.append(
                    _element_from_value(
                        value=item,
                        xml_name=item_name,
                        schema_source=schema_source,
                        parent_is_mixed=schema_says_mixed,
                        path=f"{path}.{item_name}",
                    )
                )
            continue

        if meta_type == "Wildcard":
            choices = meta.get("choices") or ()
            is_mixed = bool(meta.get("mixed", False))
            for item in value or []:
                if isinstance(item, str):
                    if is_mixed:
                        children.append(
                            make_text(item, whitespace=_is_whitespace_only(item))
                        )
                    # non-mixed wildcard with str item: rare, skip silently
                    continue
                if dataclasses.is_dataclass(item):
                    item_name = _xml_name_for_choice(item, choices)
                    # Surface unknown inline candidates exactly once per
                    # (parent_class, child_name) pair. The sweep test consumes
                    # these warnings to decide whether classify.py needs an
                    # entry. We default the child to ``block`` (safe) while
                    # waiting for human triage.
                    if is_mixed and is_unclassified_in_mixed(item_name):
                        _warn_unclassified(parent_cls=cls, child_name=item_name)
                    children.append(
                        _element_from_value(
                            value=item,
                            xml_name=item_name,
                            schema_source=schema_source,
                            parent_is_mixed=is_mixed or schema_says_mixed,
                            path=f"{path}.{item_name}",
                        )
                    )
            continue

        # No metadata.type → either a simple-content "value" field, or an
        # internal field xsdata uses for round-trip (we ignore unknowns).
        if f.name == "value" and value is not None:
            children.append(make_text(_stringify(value)))
            continue

    instance_mixed = any(
        isinstance(c, dict) and c.get("type") == "#text" for c in children
    ) and any(
        isinstance(c, dict) and c.get("type") != "#text" for c in children
    )
    is_void = not children
    metadata = _build_metadata(
        cls=cls,
        attributes=attributes,
        schema_source=schema_source,
        mixed_content=instance_mixed,
        is_void=is_void,
        path=path,
    )

    node_kind = classify(xml_name, parent_is_mixed=parent_is_mixed)

    return {
        "type": xml_name,
        "nodeKind": node_kind,
        "attributes": attributes,
        "metadata": metadata,
        "children": children,
    }


def _element_from_value(
    *,
    value: Any,
    xml_name: str,
    schema_source: str,
    parent_is_mixed: bool,
    path: str,
) -> ElementNode:
    """Coerce a plain value (dataclass / str / Enum / scalar) into ElementNode.

    For non-dataclass scalar values, we synthesize an element with a single
    text child — that's the AST representation of an ``<xs:string>``-typed
    element like ``<enterpriseName>ASD</enterpriseName>``.
    """
    if dataclasses.is_dataclass(value):
        return _build_element(
            instance=value,
            xml_name=xml_name,
            schema_source=schema_source,
            parent_is_mixed=parent_is_mixed,
            path=path,
        )

    children: list[Any] = []
    if value is not None:
        children.append(make_text(_stringify(value)))
    return {
        "type": xml_name,
        "nodeKind": classify(xml_name, parent_is_mixed=parent_is_mixed),
        "attributes": {},
        "metadata": {"schemaSource": schema_source, "void": False},
        "children": children,
    }


# ─────────────────────────── Metadata builder ───────────────────────────────


def _build_metadata(
    *,
    cls: type,
    attributes: dict[str, JsonAttrValue],
    schema_source: str,
    mixed_content: bool,
    is_void: bool,
    path: str,
) -> ElementMetadata:
    md: ElementMetadata = {
        "dataclassName": cls.__name__,
        "schemaSource": schema_source,
        "mixedContent": mixed_content,
        "void": is_void,
        "sourcePath": path,
    }
    if "id" in attributes and isinstance(attributes["id"], str):
        md["id"] = attributes["id"]
    ref_ids = _collect_ref_ids(attributes)
    if ref_ids:
        md["refIds"] = ref_ids
    return md


def _collect_ref_ids(attributes: dict[str, JsonAttrValue]) -> list[str]:
    refs: list[str] = []
    for key in _REF_ATTRS:
        v = attributes.get(key)
        if v is None:
            continue
        if isinstance(v, list):
            refs.extend(s for s in v if isinstance(s, str))
        elif isinstance(v, str):
            refs.append(v)
    # de-dupe but preserve order
    seen: set[str] = set()
    out: list[str] = []
    for r in refs:
        if r in seen:
            continue
        seen.add(r)
        out.append(r)
    return out


# ─────────────────────────── Field-shape helpers ────────────────────────────


def _element_items(value: Any, name: str) -> Iterable[tuple[Any, str]]:
    """Yield (item, xml_name) pairs from an ``Element``-typed field value."""
    if value is None:
        return
    if isinstance(value, list):
        for item in value:
            yield item, name
    else:
        yield value, name


def _xml_name_for_choice(item: Any, choices: tuple) -> str:
    """Resolve the XML element name for a choice/wildcard item.

    xsdata's choices entries look like ``{"name": "para", "type": Para, ...}``.
    """
    item_cls = type(item)
    for c in choices:
        if c.get("type") is item_cls:
            return c.get("name") or _xml_name_of_class(item_cls)
    # Fallback: derive from class metadata
    return _xml_name_of_class(item_cls)


def _xml_name_of_class(cls: type) -> str:
    """Best-effort XML name from a dataclass. Prefers ``Meta.name``."""
    meta = getattr(cls, "Meta", None)
    if meta is not None:
        name = getattr(meta, "name", None)
        if name:
            return name
    # Fallback: PascalCase → camelCase
    n = cls.__name__
    return n[0].lower() + n[1:] if n else n


def _schema_has_mixed_wildcard(cls: type) -> bool:
    """True if the dataclass declares a mixed-content Wildcard field.

    Note: xsdata sometimes adds this defensively (e.g. for xlink-aware element
    types) so this is *not* reliable as the AST node's ``mixedContent`` flag.
    Used only for ``parent_is_mixed`` propagation, which controls how children
    are classified.
    """
    for f in dataclasses.fields(cls):
        if f.metadata.get("type") == "Wildcard" and f.metadata.get("mixed"):
            return True
    return False


# ─────────────────────────── Value encoding ────────────────────────────────


def _is_empty_attr(value: Any) -> bool:
    """xsdata uses ``None`` for absent attributes and ``[]`` for absent token lists."""
    if value is None:
        return True
    if isinstance(value, list) and not value:
        return True
    return False


def _encode_attr(value: Any) -> JsonAttrValue:
    """xsdata-typed attribute → JSON-serializable form (lossless via xsdata)."""
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float, str)):
        return value
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, (date, datetime, time)):
        return value.isoformat()
    if isinstance(value, list):
        return [_encode_attr(v) for v in value]  # type: ignore[return-value]
    return str(value)


def _stringify(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, Enum):
        return str(value.value)
    if isinstance(value, (date, datetime, time)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return str(value)
    return str(value)


def _is_whitespace_only(text: str) -> bool:
    return text.strip() == ""


__all__ = ["build_ast"]

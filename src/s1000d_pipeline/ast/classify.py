"""Inline / block classification for S1000D elements.

The XSDs do not tag elements as inline or block; the editor needs that
distinction. We seed the inline set from ``proced.xsd``'s ``textElemGroup``
(lines ~920–942 in the flat schema) and verify against ``descript.xsd`` and
``ddn.xsd``. A small context-sensitive set covers elements like ``dmRef`` that
behave inline inside a mixed-content parent and block elsewhere.

S1000D legitimately allows **block elements inside mixed-content parents** —
``<para>`` may contain ``<randomList>`` etc. via the ``listElemGroup`` choice.
We track those known-block-in-mixed cases in ``BLOCK_IN_MIXED`` so the builder
can stay quiet when it encounters them. (Without this set, every ``<randomList>``
inside a ``<para>`` would generate a noisy "unclassified inline candidate"
warning that we'd then ignore — defeating the point of the warning, which is
to surface elements we've genuinely never seen before.)

Unknown elements default to ``block`` — that fails safely (an extra line
break in the editor) where the reverse would mangle layout. The builder logs
the first occurrence of an unknown element inside a mixed parent so the
table can be extended from real input rather than guesswork.
"""

from typing import Literal

from s1000d_pipeline.ast.nodes import NodeKind

# ── Always inline (members of textElemGroup) ────────────────────────────────
INLINE: frozenset[str] = frozenset(
    {
        "emphasis",
        "subScript",
        "superScript",
        "symbol",
        "verbatimText",
        "acronym",
        "acronymTerm",
        "footnote",
        "footnoteRef",
        "quantity",
        "internalRef",
        "inlineSignificantData",
        "changeInline",
        "terminologyRef",
        "circuitBreakerRef",
        "controlIndicatorRef",
        "functionalItemRef",
        # Surfaced via sweep over the bike data set:
        "indexFlag",  # text-stream index marker
        "variableRef",  # variable / template substitution reference
        "identNumber",  # inline NSN-style identifier reference
        "fullNatoStockNumber",  # NSN inline reference
    }
)

# ── Inline iff parent is mixed-content ──────────────────────────────────────
CONTEXT_SENSITIVE: frozenset[str] = frozenset(
    {
        "dmRef",
        "pmRef",
        "externalPubRef",
    }
)

# ── Block content that may legitimately appear inside a mixed parent ────────
# Adding to this set does NOT change classification (these stay ``block``);
# it only declares that we've thought about them so the builder doesn't warn.
BLOCK_IN_MIXED: frozenset[str] = frozenset(
    {
        # listElemGroup — lists embedded in <para>, <notePara>, …
        "randomList",
        "sequentialList",
        "definitionList",
        "attentionRandomList",
        "attentionSequentialList",
        # caption / structured groups
        "captionGroup",
        "quantityGroup",
        # block sections & wrappers seen inside generated mixed wildcards
        # (xsdata sometimes emits mixed=True defensively; these parents
        # technically allow these children even if not "really" mixed):
        "checkListInfo",
        "preliminaryRqmts",
        "externalPubIssue",
        "refs",
        "electricalEquipConnection",
        "productItem",
        "workArea",
    }
)


def classify(xml_name: str, parent_is_mixed: bool) -> NodeKind:
    """Return the editor's layout role for an element."""
    if xml_name in INLINE:
        return "inline"
    if xml_name in CONTEXT_SENSITIVE and parent_is_mixed:
        return "inline"
    return "block"


def is_unclassified_in_mixed(xml_name: str) -> bool:
    """True if we don't have an opinion about this element's role inside a
    mixed parent. The builder uses this to decide whether to emit a warning.
    """
    return (
        xml_name not in INLINE
        and xml_name not in CONTEXT_SENSITIVE
        and xml_name not in BLOCK_IN_MIXED
    )


__all__ = [
    "INLINE",
    "CONTEXT_SENSITIVE",
    "BLOCK_IN_MIXED",
    "classify",
    "is_unclassified_in_mixed",
]

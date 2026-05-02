"""AST → JSON-ready dict.

In practice the AST builder already returns JSON-friendly Python primitives
(str, int, float, bool, list, dict). This module exists to:

1. Provide a single place to handle any stray non-JSON-serializable values
   that slip through (Decimal, Enum, date, datetime).
2. Give callers a stable ``to_json(ast) -> dict`` entry point that they can
   trust to produce something ``json.dumps`` will accept.

Kept separate from ``builder.py`` so the builder is pure-Python and can be
unit-tested without going through serialization.
"""

from __future__ import annotations

from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum
from typing import Any


def to_json(node: Any) -> Any:
    """Recursively normalize an AST node tree into JSON-serializable values."""
    if node is None or isinstance(node, (bool, int, float, str)):
        return node
    if isinstance(node, dict):
        return {k: to_json(v) for k, v in node.items()}
    if isinstance(node, list):
        return [to_json(v) for v in node]
    if isinstance(node, tuple):
        return [to_json(v) for v in node]
    if isinstance(node, Decimal):
        return str(node)
    if isinstance(node, Enum):
        return node.value
    if isinstance(node, (date, datetime, time)):
        return node.isoformat()
    return str(node)


__all__ = ["to_json"]

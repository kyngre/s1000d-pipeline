"""S1000D XML → AST pipeline.

Public surface:

    from s1000d_pipeline import parse_to_ast
    ast = parse_to_ast("path/to/dm.xml")
"""

from s1000d_pipeline.ast.builder import build_ast
from s1000d_pipeline.ast.serializer import to_json
from s1000d_pipeline.parsing.parser import parse_document


def parse_to_ast(xml_path):
    """End-to-end: file path → AST root node (Python dict shape)."""
    parsed = parse_document(xml_path)
    return build_ast(parsed)


__all__ = ["parse_document", "build_ast", "to_json", "parse_to_ast"]

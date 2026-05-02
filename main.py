"""Smoke test: parse the golden procedural sample, build the AST, dump JSON.

Run from the repo root:

    venv/bin/python main.py
    venv/bin/python main.py samples/golden/ddn_sample.xml
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from s1000d_pipeline import build_ast, parse_document, to_json

REPO_ROOT = Path(__file__).resolve().parent
DEFAULT_SAMPLE = REPO_ROOT / "samples" / "golden" / "procedural_720A.xml"


def main(argv: list[str]) -> int:
    xml_path = Path(argv[1]) if len(argv) > 1 else DEFAULT_SAMPLE
    if not xml_path.exists():
        print(f"Sample not found: {xml_path}", file=sys.stderr)
        return 1

    parsed = parse_document(xml_path)
    ast = build_ast(parsed)
    payload = to_json(ast)

    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

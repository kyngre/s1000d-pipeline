"""Sweep a directory of S1000D XML files through the pipeline.

Reports, per file:

* parse outcome (ok / failed)
* schema_source resolved from the XML
* exception type & message if it failed
* unique unclassified-inline warnings emitted during build

Aggregates a summary across the whole directory: success/failure counts by
schema, the union of unclassified-inline candidates worth adding to
``classify.py``, and the first exception per failure type.

Usage:

    python -m s1000d_pipeline.tools.sweep "/path/to/Bike Data Set"
    python -m s1000d_pipeline.tools.sweep --json out.json /some/dir
"""

from __future__ import annotations

import argparse
import json
import sys
import traceback
import warnings
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from s1000d_pipeline import build_ast, parse_document
from s1000d_pipeline.ast.builder import (
    UnclassifiedInlineWarning,
    reset_unclassified_inline_candidates,
    unclassified_inline_candidates,
)


@dataclass
class FileResult:
    path: str
    schema_source: str | None = None
    ok: bool = False
    error_type: str | None = None
    error_msg: str | None = None
    unclassified: list[tuple[str, str]] = field(default_factory=list)


def sweep_file(path: Path) -> FileResult:
    """Parse one XML file. Captures exceptions + unclassified-inline warnings."""
    result = FileResult(path=str(path))
    reset_unclassified_inline_candidates()

    try:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always", UnclassifiedInlineWarning)
            parsed = parse_document(path)
            result.schema_source = parsed.schema_source
            build_ast(parsed)
            # Pull both: the dedupe set (canonical) and any extra warnings
            # that slipped through (defensive).
            result.unclassified = sorted(unclassified_inline_candidates())
            _ = caught  # caught list is informational; dedupe set is truth
        result.ok = True
    except Exception as exc:  # noqa: BLE001 — sweep is supposed to catch all
        result.error_type = type(exc).__name__
        result.error_msg = str(exc).split("\n")[0][:240]
        # Preserve traceback for debug if sweep is invoked with --debug
        result.error_msg = result.error_msg or traceback.format_exc(limit=1)
    return result


def sweep_dir(directory: Path) -> list[FileResult]:
    xml_files = sorted(p for p in directory.glob("*.XML"))
    return [sweep_file(p) for p in xml_files]


def summarize(results: list[FileResult]) -> dict:
    total = len(results)
    ok = sum(1 for r in results if r.ok)
    failed = total - ok

    by_schema_ok: dict[str, int] = defaultdict(int)
    by_schema_fail: dict[str, int] = defaultdict(int)
    failures_by_type: dict[str, list[dict]] = defaultdict(list)
    unclassified_union: set[tuple[str, str]] = set()
    unknown_schema: list[str] = []

    for r in results:
        key = r.schema_source or "<unknown>"
        if r.ok:
            by_schema_ok[key] += 1
            unclassified_union.update(r.unclassified)
        else:
            by_schema_fail[key] += 1
            failures_by_type[r.error_type or "?"].append(
                {"file": Path(r.path).name, "msg": r.error_msg, "schema": key}
            )
            if r.error_type == "KeyError" and "Unknown schema source" in (
                r.error_msg or ""
            ):
                unknown_schema.append(Path(r.path).name)

    return {
        "total": total,
        "ok": ok,
        "failed": failed,
        "by_schema_ok": dict(sorted(by_schema_ok.items())),
        "by_schema_fail": dict(sorted(by_schema_fail.items())),
        "unclassified_inline_candidates": sorted(unclassified_union),
        "failures_by_type": {
            k: v[:5] for k, v in failures_by_type.items()  # cap output
        },
        "unknown_schema_files": unknown_schema[:20],
    }


def _format_summary(s: dict) -> str:
    lines = [
        f"Files swept   : {s['total']}",
        f"  parsed ok   : {s['ok']}",
        f"  failed      : {s['failed']}",
        "",
        "By schema (ok / failed):",
    ]
    schemas = sorted(set(s["by_schema_ok"]) | set(s["by_schema_fail"]))
    for k in schemas:
        a = s["by_schema_ok"].get(k, 0)
        b = s["by_schema_fail"].get(k, 0)
        lines.append(f"  {k:25s}  {a:3d} ok   {b:3d} fail")
    lines.append("")
    if s["unclassified_inline_candidates"]:
        lines.append(
            f"Unclassified inline candidates ({len(s['unclassified_inline_candidates'])}):"
        )
        for parent, child in s["unclassified_inline_candidates"]:
            lines.append(f"  <{child}> inside <{parent}>")
    else:
        lines.append("No unclassified inline candidates.")
    if s["failures_by_type"]:
        lines.append("")
        lines.append("Failure summary:")
        for ekind, examples in s["failures_by_type"].items():
            lines.append(f"  {ekind} ({len(examples)} example(s) shown):")
            for ex in examples:
                lines.append(f"    {ex['file']}  [{ex['schema']}]  {ex['msg']}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", help="Directory to scan for *.XML files")
    parser.add_argument("--json", dest="json_out", help="Also write summary JSON to this path")
    args = parser.parse_args(argv)

    directory = Path(args.directory)
    if not directory.is_dir():
        print(f"Not a directory: {directory}", file=sys.stderr)
        return 2

    results = sweep_dir(directory)
    summary = summarize(results)
    print(_format_summary(summary))
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(summary, indent=2))
    return 0 if summary["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

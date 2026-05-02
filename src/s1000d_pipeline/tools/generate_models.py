"""Regenerate the ``s1000d_pipeline.models.*`` packages from XSDs.

Wraps the ``xsdata generate`` CLI with the project's pinned options so all
generated code looks the same regardless of who ran it.

Usage:

    python -m s1000d_pipeline.tools.generate_models           # default set
    python -m s1000d_pipeline.tools.generate_models proced    # one schema
    python -m s1000d_pipeline.tools.generate_models --all     # every XSD in schemas/
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

# Default to every schema the registry knows about. Keep this synchronized
# with ``s1000d_pipeline/models/_registry.py``. ``--all`` falls back to every
# .xsd file present in ``schemas/`` regardless of registration.
from s1000d_pipeline.models._registry import known_schemas

DEFAULT_SCHEMAS = tuple(known_schemas())

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SCHEMAS_DIR = REPO_ROOT / "schemas"
MODELS_DIR = REPO_ROOT / "s1000d_pipeline" / "models"


def _xsdata_args(xsd_path: Path, package: str) -> list[str]:
    # xsdata v26 defaults: postponed annotations on, kw-only on, frozen off,
    # filenames structure. We only need to pin --package; the rest is fine.
    return [
        sys.executable,
        "-m",
        "xsdata",
        "generate",
        "--package",
        package,
        str(xsd_path),
    ]


def regenerate(schema_source: str) -> None:
    xsd_path = SCHEMAS_DIR / f"{schema_source}.xsd"
    if not xsd_path.exists():
        raise FileNotFoundError(f"Schema not found: {xsd_path}")

    pkg_dir = MODELS_DIR / schema_source
    if pkg_dir.exists():
        shutil.rmtree(pkg_dir)

    package = f"s1000d_pipeline.models.{schema_source}"
    print(f"[generate] {schema_source}.xsd → {package}")
    subprocess.run(_xsdata_args(xsd_path, package), check=True, cwd=REPO_ROOT)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "schemas",
        nargs="*",
        help="Schema short names to regenerate (default: the priority set).",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Regenerate every .xsd file present in schemas/.",
    )
    args = parser.parse_args(argv)

    if args.all:
        targets = sorted(p.stem for p in SCHEMAS_DIR.glob("*.xsd"))
    elif args.schemas:
        targets = list(args.schemas)
    else:
        targets = list(DEFAULT_SCHEMAS)

    for name in targets:
        regenerate(name)
    print(f"[generate] done — {len(targets)} schema(s) regenerated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

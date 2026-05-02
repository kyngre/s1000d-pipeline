"""Shared test fixtures.

Discovers sample XMLs from two locations:

* ``samples/golden/`` — the curated golden cases (always run).
* The S1000D bike data set, if the configured path exists — used by the full
  round-trip sweep. Skipped automatically when the directory is missing so
  the suite still runs in environments without it (CI, fresh clones).
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
GOLDEN_DIR = REPO_ROOT / "samples" / "golden"

# Path to the bike data set. Override via the ``S1000D_BIKE_DATASET`` env var.
# Tests skip cleanly if the directory doesn't exist.
_DEFAULT_BIKE_PATH = "/Users/kkr/Downloads/S1000D Issue 6/Bike Data Set for Release number 6 R2"
BIKE_DATA_SET = Path(os.environ.get("S1000D_BIKE_DATASET", _DEFAULT_BIKE_PATH))


def _golden_samples() -> list[Path]:
    return sorted(p for p in GOLDEN_DIR.glob("*.xml") if p.is_file() or p.is_symlink())


def _bike_samples() -> list[Path]:
    if not BIKE_DATA_SET.is_dir():
        return []
    return sorted(BIKE_DATA_SET.glob("*.XML"))


@pytest.fixture(scope="session")
def golden_samples() -> list[Path]:
    return _golden_samples()


@pytest.fixture(scope="session")
def bike_samples() -> list[Path]:
    return _bike_samples()


def pytest_collection_modifyitems(config, items):
    """Skip bike-sample-parametrized tests when the bike data set is missing."""
    if BIKE_DATA_SET.is_dir():
        return
    skip_marker = pytest.mark.skip(reason="bike data set not available")
    for item in items:
        if "bike_sample" in item.fixturenames:
            item.add_marker(skip_marker)

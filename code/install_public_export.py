#!/usr/bin/env python3
"""Verify and install the database repository's public dashboard export."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path


EXPECTED_SCHEMAS = {
    "research.csv": [
        "label_paper_title",
        "status",
        "research_url",
        "doi",
        "main_cause_cat",
        "main_cause_cat_abbrev",
        "publication_status",
        "source_main",
    ],
    "rsx_evalr_rating.csv": [
        "research",
        "evaluator",
        "criteria",
        "middle_rating",
        "lower_CI",
        "upper_CI",
        "confidence_level",
        "row_created_date",
        "evaluator_is_anonymous",
    ],
    "evaluator_paper_level.csv": [
        "evaluation_stream",
        "hours_spent_manual_impute",
    ],
}

EMAIL_VALUE = re.compile(r"(?<![\w.+-])[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}(?![\w.-])")
PRIVATE_URL = re.compile(r"https?://(?:www\.)?coda\.io/", re.IGNORECASE)


class InstallError(ValueError):
    """Raised when a proposed public export is incomplete or unsafe."""


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_csv(path: Path, expected_columns: list[str]) -> int:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != expected_columns:
            raise InstallError(
                f"Unexpected schema for {path.name}: {reader.fieldnames!r}"
            )
        rows = list(reader)

    for line_number, row in enumerate(rows, start=2):
        for column, value in row.items():
            text = value or ""
            if EMAIL_VALUE.search(text):
                raise InstallError(
                    f"{path.name}:{line_number} contains an email-like value in {column}"
                )
            if PRIVATE_URL.search(text):
                raise InstallError(
                    f"{path.name}:{line_number} contains a private Coda URL in {column}"
                )
    return len(rows)


def install_public_export(source: Path, destination: Path) -> None:
    manifest_path = source / "manifest.json"
    if not manifest_path.is_file():
        raise InstallError("The public export has no manifest.json")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != 1:
        raise InstallError("Unsupported public-export schema version")
    if manifest.get("source") != "unjournal/unjournal-database":
        raise InstallError("Unexpected public-export source")

    expected_names = set(EXPECTED_SCHEMAS)
    actual_names = {path.name for path in source.iterdir() if path.is_file()}
    if actual_names != expected_names | {"manifest.json"}:
        raise InstallError(
            f"Public export file set differs from allowlist: {sorted(actual_names)}"
        )
    if set(manifest.get("files", {})) != expected_names:
        raise InstallError("Manifest file set differs from allowlist")

    for name, columns in EXPECTED_SCHEMAS.items():
        path = source / name
        row_count = validate_csv(path, columns)
        details = manifest["files"][name]
        if details.get("columns") != columns:
            raise InstallError(f"Manifest schema mismatch for {name}")
        if details.get("rows") != row_count:
            raise InstallError(f"Manifest row-count mismatch for {name}")
        if details.get("sha256") != sha256(path):
            raise InstallError(f"Manifest hash mismatch for {name}")

    destination.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=destination) as temporary:
        staging = Path(temporary)
        for name in EXPECTED_SCHEMAS:
            shutil.copyfile(source / name, staging / name)
        shutil.copyfile(manifest_path, staging / "public_export_manifest.json")
        for path in staging.iterdir():
            path.replace(destination / path.name)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--destination", type=Path, default=Path("data"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    install_public_export(args.source, args.destination)
    print(f"Verified and installed public data from {args.source}")


if __name__ == "__main__":
    main()

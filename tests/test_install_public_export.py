import csv
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "code" / "install_public_export.py"
SPEC = importlib.util.spec_from_file_location("install_public_export", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
InstallError = MODULE.InstallError
install_public_export = MODULE.install_public_export
EXPECTED_SCHEMAS = MODULE.EXPECTED_SCHEMAS


class InstallPublicExportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.source = self.root / "source"
        self.destination = self.root / "destination"
        self.source.mkdir()
        files = {}
        for name, columns in EXPECTED_SCHEMAS.items():
            path = self.source / name
            with path.open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=columns, lineterminator="\n")
                writer.writeheader()
                writer.writerow({column: "" for column in columns})
            files[name] = {
                "columns": columns,
                "rows": 1,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
        (self.source / "manifest.json").write_text(json.dumps({
            "schema_version": 1,
            "source": "unjournal/unjournal-database",
            "files": files,
        }))

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_installs_exact_allowlist(self) -> None:
        install_public_export(self.source, self.destination)
        self.assertEqual(
            {path.name for path in self.destination.iterdir()},
            set(EXPECTED_SCHEMAS) | {"public_export_manifest.json"},
        )

    def test_rejects_unlisted_file(self) -> None:
        (self.source / "private.csv").write_text("email\nprivate@example.org\n")
        with self.assertRaises(InstallError):
            install_public_export(self.source, self.destination)


if __name__ == "__main__":
    unittest.main()

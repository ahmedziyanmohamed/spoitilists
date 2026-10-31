#!/usr/bin/env python3
"""Build packaged Mornye extension archives from sources/ entries."""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SOURCES_DIR = ROOT / "sources"
EXTENSIONS_DIR = ROOT / "extensions"
REGISTRY_PATH = ROOT / "registry.json"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def package_source(source_dir: Path) -> Path:
    manifest_path = source_dir / "manifest.json"
    index_path = source_dir / "index.js"
    if not manifest_path.exists():
        raise FileNotFoundError(f"Missing manifest.json in {source_dir}")
    if not index_path.exists():
        raise FileNotFoundError(f"Missing index.js in {source_dir}")

    archive_name = f"{source_dir.name}.sflx"
    archive_path = EXTENSIONS_DIR / archive_name
    EXTENSIONS_DIR.mkdir(exist_ok=True)

    with ZipFile(archive_path, "w") as zf:
        zf.write(manifest_path, arcname="manifest.json")
        zf.write(index_path, arcname="index.js")

    return archive_path


def ensure_registry_entry(entry_id: str, archive_path: Path):
    registry = load_json(REGISTRY_PATH)
    manifest = load_json(SOURCES_DIR / entry_id / "manifest.json")
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    entry = {
        "id": entry_id,
        "name": entry_id,
        "display_name": manifest.get("displayName", manifest.get("name", entry_id)),
        "version": manifest.get("version", "0.0.0"),
        "author": manifest.get("author", ""),
        "description": manifest.get("description", ""),
        "download_url": f"https://raw.githubusercontent.com/ahmedziyanmohamed/spoitilists/main/extensions/{archive_path.name}",
        "sha256": sha256_file(archive_path),
        "category": "integration",
        "tags": ["spotify", "mornye", "metadata", "playlist", "homefeed", "library"],
        "downloads": 0,
        "updated_at": updated,
        "min_app_version": manifest.get("minAppVersion", "4.1.0")
    }

    entries = registry.get("extensions", [])
    for i, item in enumerate(entries):
        if item.get("id") == entry_id:
            entries[i] = entry
            break
    else:
        entries.append(entry)

    registry["extensions"] = entries
    registry["updated_at"] = updated
    with REGISTRY_PATH.open("w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)
        f.write("\n")


def main(argv: list[str]) -> int:
    if not SOURCES_DIR.exists():
        raise FileNotFoundError(f"Missing sources directory: {SOURCES_DIR}")

    selected = argv[1:]
    if selected:
        source_dirs = [SOURCES_DIR / name for name in selected]
    else:
        source_dirs = sorted(p for p in SOURCES_DIR.iterdir() if p.is_dir())

    if not source_dirs:
        raise FileNotFoundError(f"No source folders found under {SOURCES_DIR}")

    for source_dir in source_dirs:
        archive_path = package_source(source_dir)
        ensure_registry_entry(source_dir.name, archive_path)
        print(f"Created {archive_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

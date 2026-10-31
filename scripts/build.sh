#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if [[ ! -f "scripts/build_packages.py" ]]; then
  echo "::error::Missing script: scripts/build_packages.py"
  exit 1
fi

python3 scripts/build_packages.py

echo "Build complete. Generated archives and registry metadata are up to date."

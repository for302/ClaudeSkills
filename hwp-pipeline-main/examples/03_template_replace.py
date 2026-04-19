#!/usr/bin/env python3
"""Replace placeholders in a template HWPX and normalize namespaces.

Based on hwpx-skill by airmang (https://github.com/airmang/hwpx-skill)
Licensed under MIT License.
"""

from __future__ import annotations

import argparse
import os
import sys
import tempfile
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from fix_namespaces import fix_namespaces
from zip_replace_all import parse_replace_args, zip_replace_all


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Replace placeholders in a template HWPX and normalize namespaces."
    )
    parser.add_argument("input_hwpx", help="Template .hwpx path")
    parser.add_argument("output_hwpx", help="Output .hwpx path")
    parser.add_argument(
        "--replace",
        nargs="+",
        required=True,
        metavar="OLD=NEW",
        help="Replacement pairs such as {name}=John",
    )
    return parser.parse_args()


def _make_temp_path(directory: Path) -> str:
    fd, temp_path = tempfile.mkstemp(prefix="hwpx-example-", suffix=".hwpx", dir=directory)
    os.close(fd)
    return temp_path


def main() -> None:
    args = _parse_args()
    input_path = Path(args.input_hwpx).resolve()
    output_path = Path(args.output_hwpx).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    replacements = parse_replace_args(args.replace)

    # 1) Replace placeholders at ZIP level.
    temp_path = Path(_make_temp_path(output_path.parent))
    replace_stats = zip_replace_all(str(input_path), str(temp_path), replacements)

    try:
        # 2) Parse+re-serialize to normalize namespace declarations.
        ns_stats = fix_namespaces(str(temp_path), str(output_path))
    finally:
        temp_path.unlink(missing_ok=True)

    print(f"[OK] wrote: {output_path}")
    print(f"[REPLACE] {replace_stats}")
    print(f"[NS] {ns_stats}")


if __name__ == "__main__":
    main()

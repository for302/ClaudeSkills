#!/usr/bin/env python3
"""Extract text and inspect table count from an existing HWPX document.

Based on hwpx-skill by airmang (https://github.com/airmang/hwpx-skill)
Licensed under MIT License.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from hwpx import ObjectFinder, TextExtractor


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract text and inspect table count from an HWPX document."
    )
    parser.add_argument(
        "input_hwpx",
        nargs="?",
        default=str(Path(__file__).resolve().parent / "out" / "01_created.hwpx"),
        help="Input .hwpx path (default: examples/out/01_created.hwpx)",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    input_path = Path(args.input_hwpx).resolve()

    with TextExtractor(str(input_path)) as extractor:
        text = extractor.extract_text(include_nested=True)

    finder = ObjectFinder(str(input_path))
    tables = finder.find_all(tag="tbl")

    print("[TEXT]")
    print(text)
    print()
    print(f"[TABLES] {len(tables)}")


if __name__ == "__main__":
    main()

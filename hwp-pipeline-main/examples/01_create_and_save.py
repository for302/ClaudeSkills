#!/usr/bin/env python3
"""Create a new HWPX document with paragraphs and a table.

Based on hwpx-skill by airmang (https://github.com/airmang/hwpx-skill)
Licensed under MIT License.
"""

from __future__ import annotations

from pathlib import Path

from hwpx import HwpxDocument


def main() -> None:
    output_path = Path(__file__).resolve().parent / "out" / "01_created.hwpx"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    doc = HwpxDocument.new()
    doc.add_paragraph("Sample Document Title")
    doc.add_paragraph("This is an auto-generated HWPX document.")

    table = doc.add_table(3, 2)
    table.set_cell_text(0, 0, "Field")
    table.set_cell_text(0, 1, "Value")
    table.set_cell_text(1, 0, "Date")
    table.set_cell_text(1, 1, "2026-01-01")
    table.set_cell_text(2, 0, "Contact")
    table.set_cell_text(2, 1, "example@example.com")

    doc.save_to_path(str(output_path))
    print(f"[OK] wrote: {output_path}")


if __name__ == "__main__":
    main()

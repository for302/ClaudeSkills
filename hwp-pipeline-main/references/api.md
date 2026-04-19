# python-hwpx API Reference

API signatures and usage notes for `python-hwpx`, extracted for quick reference.

Based on [hwpx-skill](https://github.com/airmang/hwpx-skill) by airmang (MIT License).

| python-hwpx version | Status | Notes |
|---|---|---|
| 2.5+ | Verified | Baseline version for this skill |
| 2.0-2.4 | Mostly compatible | Minor API signature differences possible |
| 1.x | Incompatible | HwpxDocument API not supported |

- Import name: `hwpx`

## Contents

- Installation
- `HwpxDocument`
- `TextExtractor`
- `ObjectFinder`
- `HwpxPackage`
- Exceptions

## Installation

```bash
pip install -U python-hwpx lxml
```

```python
from hwpx import HwpxDocument, HwpxPackage, ObjectFinder, TextExtractor
from hwpx.opc.package import HwpxPackageError, HwpxStructureError
```

## HwpxDocument

### Open, create, save

```python
from hwpx import HwpxDocument

doc = HwpxDocument.new()
doc.add_paragraph("Auto-generated document")
doc.save_to_path("output.hwpx")

with HwpxDocument.open("input.hwpx") as doc:
    doc.add_paragraph("Additional paragraph")
    doc.save_to_path("edited.hwpx")
```

Key points:

- `HwpxDocument.open(source)`
- `HwpxDocument.new()`
- `save_to_path(path)` is the primary save API.
- `save()` is a deprecated compatibility wrapper.
- Use `to_bytes()` when bytes are needed.

### Paragraphs and tables

```python
from hwpx import HwpxDocument

doc = HwpxDocument.new()
doc.add_paragraph("Document Title")

table = doc.add_table(2, 2)
table.set_cell_text(0, 0, "Name")
table.set_cell_text(0, 1, "Value")
table.set_cell_text(1, 0, "Date")
table.set_cell_text(1, 1, "2026-01-01")

doc.save_to_path("table-example.hwpx")
```

Measured signatures (v2.8):

- `add_table(rows, cols, *, section=None, section_index=None, width=None, height=None, border_fill_id_ref=None, para_pr_id_ref=None, style_id_ref=None, char_pr_id_ref=None, run_attributes=None, **extra_attrs) -> HwpxOxmlTable`
- `set_cell_text(row_index, col_index, text, *, logical=False, split_merged=False) -> None`

Notes:

- `set_cell_text()` is a method on the table object returned by `add_table()`, not on `HwpxDocument`.
- Use `logical=True` to write to merged cells by logical coordinates.

### Memos

```python
from hwpx import HwpxDocument

doc = HwpxDocument.new()
paragraph = doc.add_paragraph("Sentence that needs review.")

memo, anchor_paragraph, field_value = doc.add_memo_with_anchor(
    "Please double-check this expression.",
    paragraph=paragraph,
    author="Reviewer",
)
```

Measured signature (v2.8):

- `add_memo_with_anchor(text="", *, paragraph=None, section=None, section_index=None, paragraph_text=None, memo_shape_id_ref=None, memo_id=None, char_pr_id_ref=None, attributes=None, field_id=None, author=None, created=None, number=1, anchor_char_pr_id_ref=None) -> tuple[HwpxOxmlMemo, HwpxOxmlParagraph, str]`

### Style-based run search and replace

```python
with HwpxDocument.open("input.hwpx") as doc:
    red_runs = doc.find_runs_by_style(text_color="#FF0000")

    replaced = doc.replace_text_in_runs(
        "TODO",
        "DONE",
        text_color="#FF0000",
        underline_type="SOLID",
        limit=3,
    )

    doc.save_to_path("output.hwpx")
```

Measured signatures (v2.8):

- `find_runs_by_style(*, text_color=None, underline_type=None, underline_color=None, char_pr_id_ref=None) -> list[HwpxOxmlRun]`
- `replace_text_in_runs(search, replacement, *, text_color=None, underline_type=None, underline_color=None, char_pr_id_ref=None, limit=None) -> int`

Notes:

- Empty search strings are not allowed.
- `replace_text_in_runs()` operates at the run level.
- For global replacement that covers table cells, use `scripts/zip_replace_all.py`.

### Export

```python
with HwpxDocument.open("input.hwpx") as doc:
    text = doc.export_text()
    html = doc.export_html()
    markdown = doc.export_markdown()
```

Measured methods:

- `export_text(**kwargs) -> str`
- `export_html(**kwargs) -> str`
- `export_markdown(**kwargs) -> str`

These methods pass keyword arguments through to internal exporters.

### Headers and footers

`set_header_text()` and `set_footer_text()` may produce inconsistent layouts in some documents. In automated pipelines, verify output files after applying these.

## TextExtractor

`TextExtractor` is for read-only text collection without building an editing DOM.

### Full text extraction

```python
from hwpx import TextExtractor

tex = TextExtractor("input.hwpx")
text = tex.extract_text(
    paragraph_separator="\n",
    skip_empty=True,
    include_nested=True,
)
```

Measured signature (v2.8):

- `extract_text(*, paragraph_separator="\n", skip_empty=True, include_nested=True, object_behavior="skip", object_placeholder=None, preserve_breaks=True, annotations=None) -> str`

### Paragraph iteration

```python
from hwpx import TextExtractor

tex = TextExtractor("input.hwpx")
for paragraph in tex.iter_document_paragraphs(include_nested=True):
    print(paragraph.section.index, paragraph.index, paragraph.path, paragraph.text())
```

Measured signature (v2.8):

- `iter_document_paragraphs(*, include_nested=True) -> Iterator[ParagraphInfo]`

`ParagraphInfo` commonly used fields:

- `section.index`
- `index`
- `path`
- `is_nested`
- `text()`

## ObjectFinder

For exhaustive search of specific OWPML tags or attributes.

```python
from hwpx import ObjectFinder

finder = ObjectFinder("input.hwpx")
tables = finder.find_all(tag="tbl")
texts = finder.find_all(tag="t", limit=20)
first_table = finder.find_first(tag="tbl")
```

Measured signatures (v2.8):

- `find_all(*, tag=None, attrs=None, xpath=None, section_filter=None, limit=None) -> list[FoundElement]`
- `find_first(*, tag=None, attrs=None, xpath=None, section_filter=None) -> FoundElement | None`

`FoundElement` commonly used fields:

- `tag`
- `path`
- `section.index`
- `text()`
- `get("attribute_name")`

## HwpxPackage

For part-level access, recovery, and advanced inspection.

```python
from hwpx import HwpxPackage

pkg = HwpxPackage.open("input.hwpx")
names = pkg.part_names()
main_xml = pkg.get_xml("Contents/section0.xml")
```

Commonly used methods:

- `open(path)`
- `part_names()`
- `get_part(name)`
- `get_xml(name)`
- `set_xml(name, element)`
- `read(name)`
- `write(name, data)`

## Exceptions

```python
from hwpx.opc.package import HwpxPackageError, HwpxStructureError
```

- Use `HwpxPackageError` and `HwpxStructureError` when handling corrupted ZIP/OWPML structures.
- Only `.hwpx` files are supported, not `.hwp`.
- After ZIP-level string replacement, run `scripts/fix_namespaces.py` or `scripts/zip_replace_all.py --auto-fix-ns` for post-processing.

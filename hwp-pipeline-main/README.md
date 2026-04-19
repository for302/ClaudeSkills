# hwp-pipeline

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skill for reading, converting, and editing Korean Hangul documents (`.hwp` / `.hwpx`) — without Hancom Office.

## Why

Korean government forms, academic templates, and institutional documents are distributed as `.hwp` files. Editing them typically requires Hancom Office (Windows-only subscription). This skill provides a complete pipeline for working with HWP/HWPX on any OS:

```
.hwp → [read] → JSON / Markdown / HTML
.hwp → [convert] → .hwpx → [edit] → filled form
```

## Features

| Capability | Backend | Requires |
|-----------|---------|----------|
| Read HWP (JSON, Markdown, HTML) | [@ohah/hwpjs](https://github.com/niceoasi/hwpjs) | Node.js 18+ |
| Convert HWP to HWPX | [hwp2hwpx](https://github.com/neolord0/hwp2hwpx) | Java 11+, Maven |
| Edit HWPX (create, template fill, replace) | [python-hwpx](https://github.com/niceoasi/python-hwpx) | Python 3.10+ |

## Quick start

### 1. Install

```bash
git clone https://github.com/Yoojin-nam/hwp-pipeline.git
cp -r hwp-pipeline ~/.claude/skills/hwp-pipeline
cd ~/.claude/skills/hwp-pipeline
bash setup.sh
```

### 2. Use with Claude Code

The skill activates automatically when you mention HWP/HWPX files or Korean document editing. Examples:

- "Convert this HWP to Markdown"
- "Fill in the placeholders in this government form"
- "Extract text from this HWPX file"

### 3. Use scripts directly

**Extract text from HWPX:**
```bash
python3 scripts/text_extract.py document.hwpx --include-nested
```

**Replace placeholders:**
```bash
python3 scripts/zip_replace_all.py template.hwpx output.hwpx \
  --replace "{name}=John" "{date}=2026-01-01" --auto-fix-ns
```

**Convert HWP to HWPX:**
```bash
java -jar java/hwp2hwpx-fat.jar input.hwp output.hwpx
```

## Project structure

```
hwp-pipeline/
├── SKILL.md              # Claude Code skill definition
├── setup.sh              # One-command dependency installer
├── java/
│   ├── Convert.java      # HWP→HWPX CLI wrapper
│   └── pom.xml           # Maven build with shade plugin (fat JAR)
├── scripts/
│   ├── text_extract.py   # HWPX text extraction CLI
│   ├── zip_replace_all.py # Global placeholder replacement
│   └── fix_namespaces.py # XML namespace normalization
├── references/
│   └── api.md            # python-hwpx API reference
└── examples/
    ├── 01_create_and_save.py
    ├── 02_extract_and_inspect.py
    └── 03_template_replace.py
```

## Acknowledgments

This skill integrates work from:

- **[hwp2hwpx](https://github.com/neolord0/hwp2hwpx)** by neolord0 — HWP to HWPX conversion (Apache 2.0)
- **[python-hwpx / hwpx-skill](https://github.com/airmang/hwpx-skill)** by airmang — HWPX editing library and skill (MIT)
- **[@ohah/hwpjs](https://github.com/niceoasi/hwpjs)** by ohah — HWP to JSON/Markdown/HTML (MIT)

## License

[MIT](LICENSE)

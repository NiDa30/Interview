#!/usr/bin/env python3
"""Extract Mermaid blocks from Markdown for separate renderer validation."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
output = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/brse-mermaid")
output.mkdir(parents=True, exist_ok=True)
count = 0
for file in sorted((root / "book" / "chapters").rglob("*.md")):
    src = file.read_text(encoding="utf-8")
    for i, block in enumerate(re.findall(r"```mermaid\s*\n([\s\S]*?)\n```", src), start=1):
        name = file.relative_to(root).as_posix().replace("/", "__").replace(".md", "")
        (output / f"{name}__{i}.mmd").write_text(block + "\n", encoding="utf-8")
        count += 1
print(f"Extracted {count} diagrams into {output}")

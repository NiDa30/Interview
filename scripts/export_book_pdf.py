#!/usr/bin/env python3
"""Produce a print-oriented Japanese/Vietnamese PDF from the consolidated Markdown manuscript."""
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "deliverables" / "BRSE-Interview-Master.md"
TARGET = ROOT / "deliverables" / "BRSE-Interview-Master.pdf"

def prepare(work):
    work.mkdir(parents=True, exist_ok=True)
    diagrams = work / "diagrams"
    diagrams.mkdir(exist_ok=True)
    text = SOURCE.read_text(encoding="utf-8")
    counter = 0
    def replace(match):
        nonlocal counter
        name = f"diagram_{counter:03d}"
        (diagrams / (name + ".mmd")).write_text(match.group(1).strip() + "\n", encoding="utf-8")
        counter += 1
        return f'\n\n<figure class="diagram"><img src="diagrams/{name}.png" alt="Sơ đồ {counter}"></figure>\n\n'
    processed = re.sub(r"```mermaid\s*\n([\s\S]*?)\n```", replace, text)
    (work / "book-prepared.md").write_text(processed, encoding="utf-8")
    if counter != 53:
        raise SystemExit(f"Expected 53 Mermaid diagrams, found {counter}")
    print(f"Prepared {counter} diagrams", flush=True)

def render(work):
    import markdown
    from weasyprint import HTML
    content = (work / "book-prepared.md").read_text(encoding="utf-8")
    body = markdown.markdown(content, extensions=["tables", "fenced_code", "sane_lists", "toc"])
    if len(list((work / "diagrams").glob("diagram_*.png"))) != 53:
        raise SystemExit("Not all 53 PNG diagrams were rendered")
    css = """
    @page { size: A4; margin: 19mm 17mm 20mm 18mm;
      @bottom-center { content: "BRSE Interview Master  •  " counter(page); font-size: 8pt; color: #657486; }
    }
    body { font-family: "Noto Sans CJK JP", "Noto Sans", "DejaVu Sans", sans-serif;
      font-size: 10.1pt; line-height: 1.60; color: #182333; }
    h1 { font-size: 24pt; color: #173a60; line-height: 1.22; margin-top: 22pt; }
    h2 { font-size: 17pt; color: #174f76; margin-top: 20pt; border-bottom: 1px solid #cee0ec;
      padding-bottom: 5pt; break-after: avoid; }
    h3 { font-size: 13.6pt; color: #203f5b; margin-top: 16pt; break-after: avoid; }
    h4 { font-size: 11.5pt; color: #315676; margin-top: 12pt; break-after: avoid; }
    h5, h6 { font-size: 10.5pt; break-after: avoid; }
    a { color: #1a527b; text-decoration: none; overflow-wrap: anywhere; }
    strong { font-weight: 700; }
    blockquote { border-left: 3px solid #9abdd4; padding-left: 10pt; margin: 9pt 0; color: #4b6175; }
    p { orphans: 2; widows: 2; }
    li { margin-bottom: 2pt; }
    table { border-collapse: collapse; width: 100%; font-size: 8.8pt; margin: 9pt 0; }
    th, td { border: 0.5pt solid #bdcbd7; padding: 5pt 6pt; vertical-align: top; overflow-wrap: anywhere; }
    th { background: #edf3f8; color: #263e54; font-weight: 700; }
    tr { break-inside: avoid; }
    pre { font-family: "DejaVu Sans Mono", monospace; font-size: 8pt; white-space: pre-wrap; }
    code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.6pt; overflow-wrap: anywhere; }
    figure.diagram { margin: 10pt 0 13pt; text-align: center; break-inside: avoid; }
    figure.diagram img { display: block; max-width: 100%; max-height: 165mm; margin: auto; }
    hr { border: 0; border-top: 1pt solid #d7e2eb; margin: 22pt 0; }
    """
    page = '<!DOCTYPE html><html lang="ja"><head><meta charset="UTF-8"></head><body>' + body + '</body></html>'
    from weasyprint import CSS
    HTML(string=page, base_url=str(work)).write_pdf(str(TARGET), stylesheets=[CSS(string=css)])
    if TARGET.stat().st_size < 10000:
        raise SystemExit("PDF unexpectedly small")
    print(f"PDF output: {TARGET} ({TARGET.stat().st_size} bytes)", flush=True)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("command", choices=["prepare", "render"])
    p.add_argument("work_dir", type=Path)
    args = p.parse_args()
    if args.command == "prepare": prepare(args.work_dir)
    else: render(args.work_dir)

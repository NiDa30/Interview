#!/usr/bin/env python3
"""Check the consolidated book against its 49 source lessons (stdlib only)."""
from pathlib import Path
from urllib.parse import urlsplit
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BOOK = ROOT / "deliverables" / "BRSE-Interview-Master.md"
SRC = ROOT / "book" / "chapters"
SOURCE_LINK = re.compile(r"^\*Nguồn: \[([^]]+)\]\(https://github\.com/NiDa30/Interview/blob/main/(book/chapters/[^)]+)\)\*$", re.M)
QUESTION = re.compile(r"^\*\*(?:面接官|深掘り)(?:（[^）]+）)?：\*\*", re.M)
LINK = re.compile(r"!?\[[^]]+\]\(([^)]+)\)")

def inspect():
    errors, warnings = [], []
    lessons = sorted(p for p in SRC.glob("chapter-*/*.md") if re.match(r"\d{2}-\d{2}-", p.name))
    book = BOOK.read_text(encoding="utf-8") if BOOK.is_file() else ""
    links = SOURCE_LINK.findall(book)
    chapters = re.findall(r"^## Chương (\d{2})\b", book, re.M)
    mermaid_sources = 0
    q12, q12_missing, q12_duplicate = 0, 0, 0
    if len(lessons) != 49: errors.append("lesson-count: expected 49, got " + str(len(lessons)))
    if chapters != [f"{i:02d}" for i in range(1, 15)]: errors.append("chapter-headings: expected chapters 01-14 in order")
    if len(links) != 49: errors.append("source-link-count: expected 49, got " + str(len(links)))
    if len(set(path for _, path in links)) != len(links): errors.append("duplicate lesson source links")
    expected = [p.relative_to(ROOT).as_posix() for p in lessons]
    received = [path for _, path in links]
    if received != expected: errors.append("book source order does not match sorted lesson paths")
    for lesson in lessons:
        text = lesson.read_text(encoding="utf-8").strip()
        mermaid_sources += len(re.findall(r"^```mermaid\b", text, re.M))
        shifted = re.sub(r"^(#{1,6}) ", lambda m: "#" * min(6, len(m.group(1)) + 2) + " ", text, flags=re.M)
        if shifted[:130] not in book:
            errors.append("content-sample missing: " + lesson.name)
        if not ("面接官" in text and "応募者" in text):
            warnings.append("lesson dialogue needs inspection: " + lesson.name)
        if "【" in text:
            warnings.append("personalization placeholders: " + lesson.name)
        if lesson.parent.name == "chapter-12":
            lines = text.splitlines()
            for n, line in enumerate(lines):
                if QUESTION.match(line):
                    q12 += 1
                    matches = sum(1 for z in lines[n+1:n+4] if z.startswith("**Dịch câu hỏi:**"))
                    if matches == 0: q12_missing += 1
                    if matches > 1: q12_duplicate += 1
    mermaid_book = len(re.findall(r"^```mermaid\b", book, re.M))
    if mermaid_book != mermaid_sources: errors.append(f"mermaid counts mismatch: source={mermaid_sources} book={mermaid_book}")
    if len(re.findall(r"^```", book, re.M)) % 2:
        errors.append("unpaired Markdown code fence in combined book")
    bad_links = [x for x in LINK.findall(book) if not (urlsplit(x).scheme or x.startswith("#") or x.startswith("//"))]
    if bad_links: errors.append("unresolved relative links: " + repr(bad_links[:5]))
    if q12 != 107 or q12_missing or q12_duplicate:
        errors.append(f"chapter12 bilingual prompts: count={q12} missing={q12_missing} duplicates={q12_duplicate}")
    result = {"status": "PASS" if not errors else "FAIL",
              "chapters": len(chapters), "source_lessons": len(lessons),
              "consolidated_lessons": len(links), "mermaid_fences": mermaid_book,
              "chapter12_questions": q12, "chapter12_missing_translations": q12_missing,
              "chapter12_duplicate_translations": q12_duplicate,
              "errors": errors, "warnings": warnings,
              "scope": "Static integrity only. No native Japanese, audio, real hardware, learner or final PDF review."}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1

if __name__ == "__main__":
    sys.exit(inspect())

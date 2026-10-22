#!/usr/bin/env python3
"""Local static QA for BRSE Interview Master. No external dependencies."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "book" / "chapters"
CHAPTER_RE = re.compile(r"chapter-(\d{2})")
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
MERMAID_RE = re.compile(r"```mermaid\s*\n([\s\S]*?)\n```")
VALID_DIAGRAM = re.compile(r"^(?:flowchart|graph|sequenceDiagram|classDiagram|stateDiagram(?:-v2)?|erDiagram|gantt|pie|mindmap|timeline|journey|gitGraph|requirementDiagram|quadrantChart)\b")
DUP_TRANSLATION = (
    "Trả lời trực tiếp câu hỏi bổ sung",
    "Nội dung trọng tâm:",
    "Đây là cách ứng xử gợi ý",
)

def report():
    files = sorted(CHAPTERS.rglob("*.md"))
    lessons = [f for f in files if re.match(r"^\d{2}-\d{2}-", f.name)]
    issues, warnings = [], []
    count_mermaid = 0
    for file in files:
        relative = file.relative_to(ROOT).as_posix()
        body = file.read_text(encoding="utf-8")
        chapter = CHAPTER_RE.search(file.parent.name)
        for link in LINK_RE.findall(body):
            target = unquote(link.strip().split("#", 1)[0])
            if not target or urlsplit(target).scheme or target.startswith("//"):
                continue
            actual = (file.parent / target).resolve()
            if not actual.is_relative_to(ROOT.resolve()) or not actual.exists():
                issues.append({"file":relative,"rule":"broken-relative-link","detail":link})
        # Verify fences are matched. Backticks appearing inline are not fences.
        fences = re.findall(r"^```(?:\w+)?\s*$", body.replace("```","```"), flags=re.M)
        if len(fences) % 2:
            issues.append({"file":relative,"rule":"unpaired-fence","detail":str(len(fences))})
        for block in MERMAID_RE.findall(body):
            count_mermaid += 1
            if not VALID_DIAGRAM.match(block.lstrip()):
                issues.append({"file":relative,"rule":"invalid-mermaid-header","detail":block[:80]})
        if "```mermaid" in body and len(MERMAID_RE.findall(body)) != body.count("```mermaid"):\n            issues.append({"file":relative,"rule":"unterminated-mermaid-fence","detail":"check triple-backtick pair"})\n        if any(p in body for p in DUP_TRANSLATION):
            warnings.append({"file":relative,"rule":"generic-translation-placeholder","detail":"check bilingual dialogue"})
        if "【" in body:
            warnings.append({"file":relative,"rule":"personalization-needed","detail":"verify CV/evidence before interview"})
        if chapter and file in lessons and not ("面接官" in body and "応募者" in body):
            warnings.append({"file":relative,"rule":"missing-dialogue","detail":"interviewer/candidate"})
    result = {
        "files_scanned":len(files), "lesson_files":len(lessons),
        "mermaid_fences":count_mermaid, "errors":issues, "warnings":warnings,
        "note":"Static checks only; diagrams are not rendered and Japanese is not native-reviewed."
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return int(bool(issues))

if __name__ == "__main__":
    sys.exit(report())

#!/usr/bin/env python3
"""Assemble the complete 49-lesson book and 49 lesson-specific deep-dive modules."""
from pathlib import Path
from urllib.parse import urlsplit
import json
import re

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "book" / "chapters"
DEEP = ROOT / "book" / "deep-dives"
OUTPUT = ROOT / "deliverables" / "BRSE-Interview-Master.md"
REPO = "https://github.com/NiDa30/Interview/blob/main"
CHAPTER_NAMES = [
    "自己紹介・自己PR", "志望動機・キャリアプラン",
    "職務経歴・プロジェクト説明", "プログラミング・Web技術",
    "フレームワーク・データベース", "システム設計・クラウド",
    "開発工程・品質管理", "要件定義・仕様確認",
    "顧客対応・問題解決", "報連相・ビジネス日本語",
    "類似表現・自然な日本語", "Smart Farm IoT — 技術デモ",
    "模擬面接・深掘り質問", "面接直前対策"
]
LINK_RE = re.compile(r"(!?\[[^]]+\])\(([^)]+)\)")

def adjust(text: str, source_path: Path) -> str:
    text = text.strip().replace("\r\n", "\n")
    # Source file is nested within the manuscript. Promote headings two levels.
    text = re.sub(r"^(#{1,6})([ \t]+)", lambda m: "#" * min(6, len(m.group(1)) + 2) + m.group(2),
                  text, flags=re.M)
    def link(m):
        label, target = m.groups()
        if target.startswith("#") or target.startswith("//") or urlsplit(target).scheme:
            return m.group(0)
        file_target = (source_path.parent / target).resolve()
        try:
            relative = file_target.relative_to(ROOT.resolve()).as_posix()
        except ValueError:
            raise ValueError(f"Link outside repository: {source_path} -> {target}")
        if not file_target.is_file():
            raise ValueError(f"Broken Markdown link: {source_path} -> {target}")
        return f"{label}({REPO}/{relative})"
    return LINK_RE.sub(link, text)

def build():
    lesson_files = sorted(
        p for p in CHAPTERS.glob("chapter-*/*.md")
        if re.match(r"^\d{2}-\d{2}-.*\.md$", p.name)
    )
    deep_files = sorted(DEEP.glob("??-??.md"))
    if len(lesson_files) != 49 or len(deep_files) != 49:
        raise RuntimeError(f"Expected 49 source lessons and deep dives, got {len(lesson_files)}, {len(deep_files)}")
    original_ids = [p.name[:5] for p in lesson_files]
    expanded_ids = [p.stem for p in deep_files]
    if original_ids != expanded_ids:
        raise RuntimeError(f"Deep-dive IDs do not match source lessons: {set(original_ids) ^ set(expanded_ids)}")
    out = [
        "# BRSE Interview Master — 日本語で突破するBrSE面接",
        "",
        "*Bản mở rộng chuyên sâu V2 — 22/10/2026*",
        "",
        "**Phạm vi:** 14 chương, 49 bài học với 49 phần ⑪ 深掘り・実務演習 bổ sung.",
        "**Trình độ định hướng:** N3–N2 giao tiếp phỏng vấn; phần thuật ngữ kỹ thuật có thể cao hơn mức JLPT.",
        "**Giới hạn:** Chưa có đánh giá độc lập của người Nhật bản ngữ, người học thử và phần cứng IoT thật. Các chỗ 【】 phải được điền bằng thông tin thật. Ví dụ kỹ thuật phải phân biệt nội dung trong source và kịch bản thực hành.",
        "",
        "## Mục lục",
        ""
    ]
    for ch in range(1, 15):
        number = f"{ch:02d}"
        count = len([p for p in lesson_files if p.parent.name == f"chapter-{number}"])
        out.append(f"- [Chương {number}: {CHAPTER_NAMES[ch-1]}](#chapter-{number}) — {count} bài")
    out.extend(["", "## Cách học bản chuyên sâu", "",
      "1. Tự trả lời câu hỏi phỏng vấn trong 20–40 giây trước khi xem mẫu.",
      "2. Đọc cơ chế, cách hoạt động, rủi ro và trade-off; đối chiếu ví dụ dự án với nguồn.",
      "3. Thực hiện nhiệm vụ trong mục ⑪, tạo sản phẩm đầu ra có thể kiểm tra.",
      "4. Giải thích lại bằng tiếng Nhật: kết luận → cơ chế → ví dụ → giới hạn, sau đó ghi âm và kiểm lỗi.",
      "5. Không nhận demo, mô phỏng hoặc một commit là bằng chứng vận hành production hay đóng góp cá nhân.",
      ""])
    mermaid_count, deep_count, chapter = 0, 0, None
    for lesson in lesson_files:
        curr = lesson.parent.name[-2:]
        if curr != chapter:
            chapter = curr
            out.extend(["", "---", "", f'<a id="chapter-{chapter}"></a>',
                        f"## Chương {chapter} — {CHAPTER_NAMES[int(chapter)-1]}", ""])
        original = adjust(lesson.read_text(encoding="utf-8"), lesson)
        extra_path = DEEP / f"{lesson.name[:5]}.md"
        advanced = adjust(extra_path.read_text(encoding="utf-8"), extra_path)
        if not advanced.startswith("#### ⑪ 深掘り・実務演習"):
            raise RuntimeError(f"Wrong deep-dive heading: {extra_path}")
        mermaid_count += len(re.findall(r"^```mermaid\b", original, flags=re.M))
        deep_count += 1
        link = f"{REPO}/{lesson.relative_to(ROOT).as_posix()}"
        out.extend([original, "", advanced, "",
                    f"*Nguồn: [{lesson.name}]({link})*", ""])
    if mermaid_count != 53:
        raise RuntimeError(f"Expected 53 Mermaid diagrams, found {mermaid_count}")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    book = "\n".join(out).strip() + "\n"
    OUTPUT.write_text(book, encoding="utf-8")
    print(json.dumps({"chapters":14, "lessons":len(lesson_files), "deep_dives":deep_count,
                      "mermaid":mermaid_count, "markdown_chars":len(book)}, ensure_ascii=False))

if __name__ == "__main__":
    build()

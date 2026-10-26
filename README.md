# BRSE Interview Master — 日本語で突破するBrSE面接

> Bộ khung biên soạn sách luyện phỏng vấn BrSE bằng tiếng Nhật. Repository đang ở giai đoạn biên soạn sớm: có 7 bài draft (5 bài mẫu theo master prompt đã đủ), chờ rà soát.

## Mục tiêu

Xây dựng nội dung có thể luyện nói trong phỏng vấn BrSE: hội thoại tiếng Nhật, câu trả lời ngắn, câu hỏi đào sâu, giải thích kỹ thuật rõ ràng và bản dịch tiếng Việt. Nội dung cần dựa trên nguồn có thể kiểm chứng hoặc ghi rõ trạng thái xác minh.

## Bắt đầu

- Đọc [quy chuẩn dành cho tác nhân và cộng tác viên](AGENTS.md).
- Xem [đặc tả sách](docs/BOOK_SPECIFICATION.md), [chuẩn nội dung](docs/CONTENT_STANDARDS.md) và [lộ trình](docs/ROADMAP.md).
- Dùng mẫu trong `book/templates/` khi bắt đầu biên soạn.
- Thêm tài liệu nguồn vào `sources/` và kiến thức đã được tổ chức vào `knowledge-base/` trước khi viết chương dựa trên chúng.

## Trạng thái

- Có khung thư mục cho 14 chương; tên chương xem [đặc tả sách](docs/BOOK_SPECIFICATION.md).
- Bài mẫu ngoài Chapter 12: [01.01 自己紹介](book/chapters/chapter-01/01-01-self-introduction.md), [04.01 REST API](book/chapters/chapter-04/04-01-rest-api.md), [09.01 仕様変更への対応](book/chapters/chapter-09/09-01-change-request.md).
- Chapter 12 — **技術デモ・プレゼンテーション**, case study Smart Farm IoT Management System: bài 12.01–12.03 và 12.05 ở trạng thái draft ([mục lục chương](book/chapters/chapter-12/README.md)). Căn cứ: [Project Knowledge Base](knowledge-base/case-studies/smart-farm-iot.md).
- `data/question-bank.json` chỉ chứa câu hỏi đã có trong bài học; câu trả lời mẫu trong đó là bản chép nguyên văn từ bài. `data/visual-manifest.json` ghi mọi sơ đồ thực có trong bài.
- Sơ đồ viết bằng Mermaid ngay trong bài.

## Kiểm tra trước khi commit

```bash
npm install                # lần đầu: cài mermaid-cli
npm run validate           # schema JSON, đối chiếu câu hỏi/sơ đồ với bài, cấu trúc 11 phần, link
npm run validate:render    # như trên + render mọi sơ đồ Mermaid
```

Script: [scripts/validation/validate.mjs](scripts/validation/validate.mjs). Khi sửa câu trả lời mẫu trong bài, cập nhật bản tương ứng trong `question-bank.json` — script sẽ báo lỗi nếu hai bên lệch nhau. Render dùng Chrome/Edge có sẵn trên máy; có thể chỉ định trình duyệt bằng biến môi trường `PUPPETEER_EXECUTABLE_PATH`.

## Quy tắc đóng góp

Không bịa kinh nghiệm, vai trò, số liệu hay kết quả dự án. Mỗi nhận định kỹ thuật cần dẫn nguồn hoặc ghi trạng thái xác minh. Không sinh hàng loạt bài học tự động.


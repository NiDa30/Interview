# Book Specification

## Định danh

- **Tên:** BRSE Interview Master
- **Phụ đề:** 日本語で突破するBrSE面接
- **Đối tượng:** Người học/ứng viên BrSE cần chuẩn bị phỏng vấn bằng tiếng Nhật, đặc biệt người cần diễn đạt rõ vai trò cầu nối kỹ thuật.
- **Ngôn ngữ biên soạn:** Tiếng Nhật cho hội thoại/câu trả lời mẫu; tiếng Việt cho giải thích và bản dịch.
- **Quy mô:** 14 chương, theo master prompt [BOOK_SPECIFICATION.txt](../sources/technical-reference/BOOK_SPECIFICATION.txt) (R1.3, mục 4).

## Bản đồ chương

| # | Tên | Trọng tâm |
|---|---|---|
| 01 | 自己紹介・自己PR | Tự giới thiệu 30/60 giây, điểm mạnh/yếu |
| 02 | 志望動機・キャリアプラン | Lý do làm việc tại Nhật, định hướng SE/BrSE, kế hoạch N2/N1 |
| 03 | 職務経歴書・プロジェクト説明 | Giải thích CV, dự án, STAR, nhất quán với CV |
| 04 | プログラミング・Web技術 | OOP, HTTP, REST API, JSON, luồng xử lý Web |
| 05 | フレームワーク・データベース | Spring Boot, React, RDB, ORM, transaction |
| 06 | システム設計・クラウド | Kiến trúc, modular monolith, AWS, bảo mật, mở rộng |
| 07 | 開発工程・品質管理 | SDLC, Agile, Git, kiểm thử, CI/CD |
| 08 | 要件定義・仕様確認 | Hearing, làm rõ đặc tả, acceptance criteria |
| 09 | 顧客対応・問題解決 | Feasibility, escalation, thay đổi phạm vi, rủi ro |
| 10 | 報連相・ビジネス日本語 | 報告・連絡・相談, kính ngữ, email, họp |
| 11 | 類似表現比較・自然な日本語 | Biểu đạt gần nghĩa, sắc thái, tránh dịch từng từ |
| 12 | 技術デモ・プレゼンテーション | Case study chính: Smart Farm IoT Management System |
| 13 | 模擬面接・深掘り質問 | Mock interview HR/kỹ thuật/kiến trúc/BrSE |
| 14 | 面接直前対策・総合評価 | Checklist trước phỏng vấn, reverse question, closing |

## Mục tiêu học tập

Sau khi hoàn thiện, người học có thể luyện trả lời phỏng vấn BrSE bằng tiếng Nhật trong thời lượng ngắn, xử lý câu hỏi đào sâu, diễn giải kiến thức kỹ thuật và mô tả kinh nghiệm có căn cứ.

## Cấu trúc dự kiến của một bài

Tùy chủ đề, bài học nên có: mục tiêu; bối cảnh/câu hỏi phỏng vấn; hội thoại Nhật–Việt; câu trả lời chính 15–30 giây; câu hỏi đào sâu; giải thích kỹ thuật; điểm dễ nhầm; bài tập phản xạ; hình minh họa nếu hữu ích; nguồn và trạng thái xác minh.

## Chapter 12

**Tên:** 技術デモ・プレゼンテーション — case study chính: Smart Farm IoT Management System

Chương này dùng dự án Smart Farm IoT Management System làm tình huống xuyên suốt; kế hoạch 10 bài (12.01–12.10) nằm ở mục 11 của master prompt. Căn cứ dự án: [Project Knowledge Base](../knowledge-base/case-studies/smart-farm-iot.md). Bài về vai trò cá nhân (12.08) và demo (12.09) cần thêm chứng cứ trước khi viết. Không suy diễn kiến trúc, vai trò, công nghệ, quy mô hoặc kết quả từ tên dự án. Ghi rõ các khoảng trống thông tin và cần xác nhận với chủ sở hữu dự án.

## Tiêu chí hoàn thiện sách

- Đủ 14 chương theo mục tiêu và thứ tự đã được thống nhất.
- Mỗi nội dung tuân thủ `CONTENT_STANDARDS.md` và `AGENTS.md`.
- Nhận định kỹ thuật có nguồn/trạng thái; ví dụ và kinh nghiệm được phân định rõ.
- Hình ảnh có nguồn/quyền sử dụng hoặc được tạo nội bộ, có mô tả và ghi nhận trong manifest.
- Metadata JSON hợp lệ, liên kết tới tài liệu hiện hữu.


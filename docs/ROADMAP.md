# Roadmap

Đây là thứ tự làm việc, không phải tuyên bố rằng nội dung đã hoàn thành.

1. **Khởi tạo nền tảng** — hoàn thiện cấu trúc, quy chuẩn, template và metadata rỗng hợp lệ.
2. **Lập bản đồ chương** — thống nhất tên, mục tiêu, đối tượng và liên kết giữa 14 chương.
3. **Thu thập tri thức** — bổ sung câu hỏi phỏng vấn, tài liệu kỹ thuật, cách diễn đạt Nhật ngữ và case study có nguồn vào `sources/` và `knowledge-base/`.
4. **Xác minh case study** — xây dựng Project Knowledge Base Smart Farm từ tài liệu/đầu vào có thẩm quyền; xác nhận vai trò, kiến trúc, quyết định và kết quả trước khi viết Chapter 12.
5. **Biên soạn theo chương** — viết từng bài bằng template, không sinh hàng loạt tự động.
6. **Rà soát** — dùng checklist Nhật ngữ và kỹ thuật; xử lý trạng thái `needs-verification`.
7. **Xuất bản** — cập nhật manifest cho tài sản thực có và tạo bản xuất khi nội dung được duyệt.

## Trạng thái hiện tại (2026-10-26)

- Bộ khung 14 chương: đã tạo. Tên và trọng tâm từng chương: đã thống nhất theo master prompt (xem [BOOK_SPECIFICATION.md](BOOK_SPECIFICATION.md)).
- Chapter 12: có bản draft 12.01–12.03 và 12.05 (bài mẫu Command/ACK); 12.04, 12.06–12.10 chưa biên soạn (xem [chapter-12/README.md](../book/chapters/chapter-12/README.md)).
- Các chương khác: mỗi chương 01, 04, 09 có một bài mẫu (01.01, 04.01, 09.01 — số bài tạm thời); các chương còn lại chưa có bài.
- Question bank (schema master prompt §7) và visual manifest (schema addendum R1.4 §8): đã chuẩn hóa; kiểm tra tự động bằng `npm run validate`.
- Template và rubric chuẩn: đã có ([lesson-template.md](../book/templates/lesson-template.md), [ASSESSMENT_RUBRIC.md](ASSESSMENT_RUBRIC.md)).
- Bài mẫu theo master prompt (5 bài): **đã đủ 5/5** — Self-introduction (01.01), REST API (04.01), BrSE Problem Solving (09.01), Smart Farm System Architecture (12.02), Smart Farm Command/ACK (12.05). Bước tiếp theo theo master prompt (Phase 4): kiểm định 5 bài mẫu (reviewer tiếng Nhật, BrSE thực tế) trước khi biên soạn toàn bộ sách.
- Project Knowledge Base Smart Farm: đã có [bản đầu](../knowledge-base/case-studies/smart-farm-iot.md) từ mô tả của chủ dự án; còn thiếu vai trò cá nhân, bối cảnh, lý do chọn công nghệ, số liệu và bằng chứng test/demo.
- `sources/interview-feedback/` có ghi chú góp ý phỏng vấn thử — có thể dùng làm căn cứ định hướng cho Chapter 01, 02, 14 sau khi lọc thông tin cá nhân.
- Rà soát tiếng Nhật bởi reviewer: chưa thực hiện.


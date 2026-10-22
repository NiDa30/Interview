# BÁO CÁO KIỂM THỬ — BRSE Interview Master

**Ngày kiểm tra:** 22/10/2026  
**Repository:** https://github.com/NiDa30/Interview  
**Bản sách được kiểm tra:** [BRSE-Interview-Master.md](BRSE-Interview-Master.md)  
**Commit sách đã qua CI:** `09cc39101a46638d195dd107bb87696114ca5c21`  
**Bằng chứng chạy CI:** https://github.com/NiDa30/Interview/actions/runs/39805354821

## 1. Kết luận

**PASS — kiểm tra cấu trúc/tích hợp bản sách Markdown tại commit ứng viên.**

GitHub Actions run `39805354821` đã **completed/success** với hai job `markdown-static` và `mermaid-render`. Log chi tiết cho thấy script kiểm tra bản sách trả về `"status": "PASS"`, `"errors": []`; Mermaid CLI ghi `Total=66 Passed=66 Failed=0`; unit tests cho QA ghi `Ran 5 tests`.

**KHÔNG ĐỒNG NGHĨA** đã kiểm chứng ngữ âm, tiếng Nhật bản ngữ, thực hành phỏng vấn của người học, tính an toàn thiết bị thật, kiến trúc triển khai thực tế, bản quyền hoặc bản in PDF. Các hạng mục đó được đánh dấu **NOT RUN / BLOCKED**, không phải PASS.

## 2. Ma trận kiểm thử và kết quả

| Mã | Phương pháp | Kết quả | Minh chứng / giới hạn |
|---|---|---|---|
| T01 | Đếm chương trong bản sách | **PASS** | **14/14** chương, thứ tự 01–14 |
| T02 | Đếm bài nguồn và bài hợp nhất | **PASS** | **49/49**, 49 liên kết nguồn duy nhất |
| T03 | Các mục chính ①–⑩ trong mỗi bài | **PASS (static)** | 49/49 bài có đủ ký hiệu mục sau sửa 12.07, 12.08, 12.09 |
| T04 | Đối chiếu hỏi–dịch Chương 12 | **PASS (static)** | **107** câu hỏi; **0** thiếu bản dịch gần kề, **0** bản dịch trùng |
| T05 | Kiểm tra Markdown fences bản sách | **PASS** | 53 sơ đồ Mermaid; 106 code-fence lines bắt đầu bằng `&#96;&#96;&#96;`, số chẵn |
| T06 | Liên kết tương đối ở bản ghép | **PASS** | Đã sửa 26 liên kết chương 12; lúc quét lại **0** liên kết tương đối chưa xử lý |
| T07 | So khớp đoạn nội dung đầu mỗi bài với nguồn | **PASS** | `scripts/qa_release.py`: 49/49 mẫu đầu bài có mặt |
| T08 | Kiểm tra tĩnh Markdown nguồn | **PASS** | `scripts/qa_book.py` trong GitHub Actions |
| T09 | Biên dịch Python QA scripts | **PASS** | `python -m py_compile` trên GitHub Actions |
| T10 | Unit regression QA | **PASS** | `python -m unittest discover`: **5** tests |
| T11 | Render Mermaid từ tài liệu nguồn | **PASS** | **66/66** sơ đồ render thành công trong CI; bao gồm foundation và 49 bài |
| T12 | Review tiếng Nhật bản ngữ / Keigo / cách đọc | **NOT RUN** | 0/49 được người bản ngữ nghiệm thu |
| T13 | Giọng nói, ghi âm và mock interview với người học N3–N2 | **NOT RUN** | Không có mẫu người học, bản ghi âm hoặc điểm rubric thật |
| T14 | Thử thiết bị IoT, AWS runtime và tác động bơm/van | **NOT RUN** | Không có kiểm thử thực nghiệm phần cứng/production |
| T15 | Xuất PDF/EPUB và soát glyph, dàn trang, sơ đồ khi in | **NOT RUN** | Đầu ra phát hành hiện tại là Markdown |
| T16 | Kiểm tra pháp lý, bản quyền, sự đồng ý reviewer và release v1.0.0 | **BLOCKED** | Chưa có tài liệu nghiệm thu |

**Diễn giải T11:** 66 là số sơ đồ trong toàn bộ tài liệu nguồn mà workflow trích xuất; **53** là số sơ đồ có trong cuốn sách hợp nhất 49 bài. Hai số không mâu thuẫn.

## 3. Cảnh báo còn tồn tại

- **23/49 bài** có placeholder dạng `【...】`: cố ý dành chỗ cho hồ sơ, dự án hoặc minh chứng riêng của người học; **không** được dùng như câu trả lời cá nhân hoàn chỉnh.
- Các tuyên bố trong nội dung như `本番`, `実機`, `安全`, `ACK` cần đọc theo ngữ cảnh. Đếm từ khóa và static scan **không đủ** để chứng minh hoạt động sản xuất hay an toàn thiết bị.
- Kiểm tra 107 bản dịch là kiểm tra **sự hiện diện, số lượng và việc trùng** của bản dịch câu hỏi, **không phải xác nhận 100% độ tự nhiên hoặc nghĩa của mọi bản dịch**.
- Đúng cú pháp Mermaid không bảo đảm nội dung sơ đồ kỹ thuật chính xác.
- Chưa kiểm tra toàn bộ chất lượng hiển thị ở đầu đọc EPUB/PDF; không được suy diễn từ việc Markdown hiển thị trên GitHub.

## 4. Cách tái hiện

Tại checkout repository:

```bash
python -m py_compile scripts/qa_book.py scripts/qa_release.py scripts/extract_mermaid.py scripts/test_qa_book.py
python -m unittest discover -s scripts -p 'test_qa_book.py' -v
python scripts/qa_book.py
python scripts/qa_release.py
```

Mermaid CLI được cấu hình và chạy trong [GitHub Actions Book QA](https://github.com/NiDa30/Interview/blob/main/.github/workflows/book-qa.yml). Bằng chứng run áp dụng trực tiếp cho source SHA ghi ở đầu báo cáo, không tự động thay thế kết quả của commit khác.

## 5. Quyết định test

**ACCEPT cho giai đoạn review Markdown** (nội bộ); **REJECT việc công bố đã nghiệm thu toàn bộ R2–R8 hoặc phát hành chính thức** trước khi các test T12–T16 có bằng chứng. Người kiểm định tiếng Nhật, người học thử và môi trường phần cứng thực tế là những phụ thuộc chưa thể thay bằng test tĩnh.

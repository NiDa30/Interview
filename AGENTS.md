# Quy tắc biên soạn

Áp dụng cho toàn bộ repository. Đây là các điều kiện bắt buộc khi tạo hoặc sửa nội dung sách.

1. Mọi kiến thức được dạy phải có hội thoại phỏng vấn bằng tiếng Nhật.
2. Câu trả lời chính cần phù hợp khoảng 15–30 giây khi nói. Ưu tiên ngắn, trực tiếp và có cấu trúc.
3. Bài học phải có ít nhất một câu hỏi đào sâu (深掘り質問) và hướng trả lời hoặc tiêu chí luyện tập.
4. Cung cấp bản dịch tiếng Việt cho hội thoại và các phần tiếng Nhật cần người học hiểu.
5. Giải thích rõ kiến thức kỹ thuật liên quan; không dùng thuật ngữ như thể người học đã biết.
6. Khi có nguy cơ nhầm lẫn, so sánh cách diễn đạt/khái niệm gần nhau và nêu khác biệt thực tế.
7. Có bài tập luyện phản xạ, chẳng hạn trả lời có giới hạn thời gian, thay đổi điều kiện hoặc hỏi tiếp.
8. Thêm hình minh họa khi hình thực sự giúp hiểu cấu trúc, luồng hoặc quan hệ. Không thêm hình chỉ để trang trí.
9. Mỗi nhận định kỹ thuật cần có nguồn có thể truy nguyên hoặc trạng thái xác minh rõ ràng (ví dụ: `verified`, `needs-verification`, `author-experience—unverified`). Ghi ngày truy cập khi phù hợp.
10. Không bịa kinh nghiệm cá nhân, vai trò, phạm vi trách nhiệm, số liệu hay kết quả dự án. Ví dụ giả định phải được gắn nhãn rõ; dữ liệu dự án chỉ được viết từ Project Knowledge Base đã được cung cấp/xác minh.

## Quy trình

- Trước khi viết, xem chuẩn trong `docs/` và tìm căn cứ trong `sources/` hoặc `knowledge-base/`.
- Phân biệt sự kiện nguồn, diễn giải và ví dụ giả định. Đánh dấu nội dung còn cần xác minh.
- Lưu tài liệu nguồn vào thư mục phù hợp trong `sources/`; ghi xuất xứ, chủ sở hữu/quyền sử dụng và ngày lấy nếu biết.
- Dùng template trong `book/templates/`. Không tự động tạo hàng loạt bài học.
- Cập nhật metadata/manifest chỉ khi có mục tương ứng thật; không tạo mục placeholder gây hiểu nhầm là nội dung đã tồn tại.
- Chapter 12 chỉ được biên soạn sau khi `knowledge-base/case-studies/` có Project Knowledge Base đủ căn cứ. Hiện trạng thái là chờ dữ liệu.


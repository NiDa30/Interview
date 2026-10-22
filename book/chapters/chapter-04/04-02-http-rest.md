# 第04.02課 — HTTP・REST API

> **BRSE Interview Master · Draft / Pending review**  
> Trình độ N3–N2; mục tiêu hội thoại chính 15–30 giây. Nội dung giải thích kỹ thuật là học liệu; không khẳng định người học từng làm các thao tác nếu chưa có bằng chứng. Các endpoint/sơ đồ minh họa không phải đặc tả dự án khi không được xác nhận.

## ① 学習目標 — Mục tiêu

Hiểu và giải thích được **HTTP・REST API**, trả lời một câu hỏi kỹ thuật chính, xử lý ít nhất một follow-up, sử dụng từ vựng IT tiếng Nhật, và chuyển kiến thức sang tình huống mới.

## ② 面接質問・質問の意図

**面接官：** REST APIとは何ですか。

**Nhà tuyển dụng đánh giá:** Năng lực hiểu khái niệm, giải thích mục đích sử dụng và phân biệt kiến thức thực tế với giả định.

## ③ 技術知識・思考プロセス

**Cách tư duy:** Định nghĩa / tình huống → công dụng → rủi ro hoặc giới hạn → ví dụ. Khi hỏi về quyết định kỹ thuật của dự án, phải phân biệt *lợi ích chung* với *lý do lựa chọn thực tế được xác nhận*.

GET lấy tài nguyên; POST thường gửi nội dung để tạo/xử lý.

## ④ 図解 — Hình minh họa

```mermaid
sequenceDiagram
participant UI as React
participant API as REST API
UI->>API: GET /devices/123 (illustrative)
API-->>UI: 200 + JSON
```

**Chú giải:** Sơ đồ có tính giáo dục. Không suy ra hạ tầng hoặc endpoint tương ứng đang tồn tại trong mã nguồn Smart Farm.

**日本語で説明してみよう：** まず全体の流れを確認します。次に、それぞれの役割を説明します。最後に、データの受け渡しや確認が必要な点をまとめます。

**Dịch:** Nắm luồng tổng thể, giải thích trách nhiệm các tầng, nêu điểm trao đổi dữ liệu và vấn đề cần xác minh.

## ⑤ 面接対話 — Hội thoại Nhật–Việt

**面接官：** REST APIとは何ですか。

**応募者（Standard）：** RESTの考え方に沿ってリソースを扱うAPIです。一般的にHTTPのメソッドやステータスコードを利用します。

**ベトナム語訳：** REST API là API tuân theo các nguyên tắc REST, thường sử dụng phương thức và mã trạng thái HTTP.

**面接官（深掘り）：** GETとPOSTの違いは何ですか。

**Câu hỏi đào sâu (Việt):** GET và POST khác nhau như thế nào?

**応募者：** GETは主に取得に使い、POSTはデータを送って処理や作成を依頼する時に使います。

**ベトナム語訳：** GET chủ yếu dùng để lấy dữ liệu; POST gửi dữ liệu để yêu cầu xử lý hoặc tạo tài nguyên.

**質問の型:** 何ですか → なぜ必要ですか → 具体的にはどうしますか. Khi có câu hỏi tiếp theo, ưu tiên giải thích một ý mới, không lặp toàn bộ định nghĩa.

## ⑥ 類似表現比較 — Cách diễn đạt phù hợp

- **使っています:** công nghệ đang dùng, không tự bao hàm lý do lựa chọn.
- **採用しました:** đã áp dụng; cần xác minh vai trò quyết định trước khi dùng ở ngôi cá nhân.
- **確認します / 検証します:** kiểm tra thông tin / kiểm chứng qua phương pháp.
- **実現できます / 可能性があります:** có thể thực hiện / có khả năng; không hứa tuyệt đối khi chưa đánh giá rủi ro.

## ⑦ 語彙・文法 — Từ vựng chuyên ngành

| 日本語 | 読み方 | Nghĩa |
|---|---|---|
| 資源 | しげん | Tài nguyên (resource) |
| 取得 | しゅとく | Lấy dữ liệu |
| 送信 | そうしん | Gửi |
| 要求 | ようきゅう | Yêu cầu/request |
| 応答 | おうとう | Phản hồi/response |
| 状態コード | じょうたいコード | Mã trạng thái |

**Mẫu câu phỏng vấn:** GETは主にデータを取得する時に使います。

**Dịch sát nghĩa:** GET chủ yếu dùng khi lấy dữ liệu.

## ⑧ 実践練習 — Bài tập

1. Trả lời câu chính trong 15–30 giây không nhìn mẫu.
2. Trả lời câu đào sâu trong 10–25 giây.
3. GET lấy tài nguyên; POST thường gửi nội dung để tạo/xử lý.
4. Trả lời câu hỏi BrSE: 「お客様に説明するなら、どう言い換えますか。」 bằng từ ngữ dễ hiểu hơn.
5. **AI Interviewer:** あなたは日本企業のBrSE技術面接官です。「HTTP・REST API」について一問ずつ質問し、回答を待ってください。内容に沿って一つだけ深掘りし、最後に簡潔な改善点を示してください。

## ⑨ 評価・改善 — Rubric /20

Tự chấm năm tiêu chí 0–4: đúng trọng tâm, chính xác kỹ thuật, tiếng Nhật tự nhiên, diễn giải mạch lạc, phản xạ follow-up. Thang 16–20 tốt, 12–15 cần chỉnh, dưới 12 học lại là thước đo **nội bộ**. Không tự chấm phát âm khi không có audio.

**Quy trình sửa:** Rút ngắn câu, chỉ ra giới hạn cần xác minh, thử giải thích lại cho khách hàng không chuyên và làm mới ví dụ.

## ⑩ 出典・検証状況

- Kiến thức cơ bản về lập trình / kiến trúc / QA / yêu cầu là **nội dung giáo dục tổng quát**, không trích xuất trực tiếp từ source code.
- Với Smart Farm, brief cung cấp: ESP32/Wokwi, AWS IoT Core, MQTT/TLS/X.509, backend Java 21/Spring Boot/Spring JDBC/modular monolith, PostgreSQL, React/REST/polling, kiểm thử JUnit/Spring Boot Test/Playwright; backend và DB chủ yếu local, luồng ESP32/Wokwi–AWS–backend có bằng chứng chạy thử theo mô tả.
- **Chưa xác nhận:** cấu hình production, khả năng vận hành bơm/van nông nghiệp thật, benchmark, endpoints và triển khai các công nghệ minh họa không có trong brief.
- Cần đối chiếu mã nguồn, kiểm thử render Mermaid, rà soát tiếng Nhật và thử trả lời có bấm giờ trước khi đánh dấu Reviewed.

# 第06.02課 — AWS IoT Core・TLS・X.509

> **BRSE Interview Master · Draft / Pending review**  
> Trình độ N3–N2; mục tiêu hội thoại chính 15–30 giây. Nội dung giải thích kỹ thuật là học liệu; không khẳng định người học từng làm các thao tác nếu chưa có bằng chứng. Các endpoint/sơ đồ minh họa không phải đặc tả dự án khi không được xác nhận.

## ① 学習目標 — Mục tiêu

Hiểu và giải thích được **AWS IoT Core・TLS・X.509**, trả lời một câu hỏi kỹ thuật chính, xử lý ít nhất một follow-up, sử dụng từ vựng IT tiếng Nhật, và chuyển kiến thức sang tình huống mới.

## ② 面接質問・質問の意図

**面接官：** AWS IoT Coreをどのように使用していますか。

**Nhà tuyển dụng đánh giá:** Năng lực hiểu khái niệm, giải thích mục đích sử dụng và phân biệt kiến thức thực tế với giả định.

## ③ 技術知識・思考プロセス

**Cách tư duy:** Định nghĩa / tình huống → công dụng → rủi ro hoặc giới hạn → ví dụ. Khi hỏi về quyết định kỹ thuật của dự án, phải phân biệt *lợi ích chung* với *lý do lựa chọn thực tế được xác nhận*.

TLS chưa đủ chứng minh bảo mật toàn hệ thống.

## ④ 図解 — Hình minh họa

```mermaid
flowchart LR
E[ESP32 with X509] <-->|MQTT TLS| I[AWS IoT Core]
I <-->|MQTT WSS SigV4| B[Spring Boot]
B <-->|REST| UI[React]
```

**Chú giải:** Sơ đồ có tính giáo dục. Không suy ra hạ tầng hoặc endpoint tương ứng đang tồn tại trong mã nguồn Smart Farm.

**日本語で説明してみよう：** まず全体の流れを確認します。次に、それぞれの役割を説明します。最後に、データの受け渡しや確認が必要な点をまとめます。

**Dịch:** Nắm luồng tổng thể, giải thích trách nhiệm các tầng, nêu điểm trao đổi dữ liệu và vấn đề cần xác minh.

## ⑤ 面接対話 — Hội thoại Nhật–Việt

**面接官：** AWS IoT Coreをどのように使用していますか。

**応募者（Standard）：** ESP32とバックエンドの間でMQTTメッセージをやり取りするために使っています。デバイスの接続にはTLSと証明書を使っています。

**ベトナム語訳：** AWS IoT Core trao đổi MQTT giữa thiết bị/backend, thiết bị kết nối TLS/chứng chỉ.

**面接官（深掘り）：** これでシステム全体は安全ですか。

**Câu hỏi đào sâu (Việt):** Như vậy toàn hệ thống đã an toàn chưa?

**応募者：** いいえ。アクセス権限やAPI認証、デバイスごとの設定も確認する必要があります。

**ベトナム語訳：** Chưa. Còn cần kiểm tra phân quyền, xác thực API và cấu hình cho từng thiết bị.

**質問の型:** 何ですか → なぜ必要ですか → 具体的にはどうしますか. Khi có câu hỏi tiếp theo, ưu tiên giải thích một ý mới, không lặp toàn bộ định nghĩa.

## ⑥ 類似表現比較 — Cách diễn đạt phù hợp

- **使っています:** công nghệ đang dùng, không tự bao hàm lý do lựa chọn.
- **採用しました:** đã áp dụng; cần xác minh vai trò quyết định trước khi dùng ở ngôi cá nhân.
- **確認します / 検証します:** kiểm tra thông tin / kiểm chứng qua phương pháp.
- **実現できます / 可能性があります:** có thể thực hiện / có khả năng; không hứa tuyệt đối khi chưa đánh giá rủi ro.

## ⑦ 語彙・文法 — Từ vựng chuyên ngành

| 日本語 | 読み方 | Nghĩa |
|---|---|---|
| 証明書 | しょうめいしょ | Chứng chỉ |
| 暗号化 | あんごうか | Mã hóa |
| 認証 | にんしょう | Xác thực |
| 認可 | にんか | Phân quyền |
| 権限 | けんげん | Quyền truy cập |
| 通信経路 | つうしんけいろ | Đường truyền |

**Mẫu câu phỏng vấn:** TLSで通信を保護しますが、権限の設定も確認する必要があります。

**Dịch sát nghĩa:** TLS bảo vệ đường truyền nhưng vẫn cần kiểm tra cấu hình phân quyền.

## ⑧ 実践練習 — Bài tập

1. Trả lời câu chính trong 15–30 giây không nhìn mẫu.
2. Trả lời câu đào sâu trong 10–25 giây.
3. TLS chưa đủ chứng minh bảo mật toàn hệ thống.
4. Trả lời câu hỏi BrSE: 「お客様に説明するなら、どう言い換えますか。」 bằng từ ngữ dễ hiểu hơn.
5. **AI Interviewer:** あなたは日本企業のBrSE技術面接官です。「AWS IoT Core・TLS・X.509」について一問ずつ質問し、回答を待ってください。内容に沿って一つだけ深掘りし、最後に簡潔な改善点を示してください。

## ⑨ 評価・改善 — Rubric /20

Tự chấm năm tiêu chí 0–4: đúng trọng tâm, chính xác kỹ thuật, tiếng Nhật tự nhiên, diễn giải mạch lạc, phản xạ follow-up. Thang 16–20 tốt, 12–15 cần chỉnh, dưới 12 học lại là thước đo **nội bộ**. Không tự chấm phát âm khi không có audio.

**Quy trình sửa:** Rút ngắn câu, chỉ ra giới hạn cần xác minh, thử giải thích lại cho khách hàng không chuyên và làm mới ví dụ.

## ⑩ 出典・検証状況

- Kiến thức cơ bản về lập trình / kiến trúc / QA / yêu cầu là **nội dung giáo dục tổng quát**, không trích xuất trực tiếp từ source code.
- Với Smart Farm, brief cung cấp: ESP32/Wokwi, AWS IoT Core, MQTT/TLS/X.509, backend Java 21/Spring Boot/Spring JDBC/modular monolith, PostgreSQL, React/REST/polling, kiểm thử JUnit/Spring Boot Test/Playwright; backend và DB chủ yếu local, luồng ESP32/Wokwi–AWS–backend có bằng chứng chạy thử theo mô tả.
- **Chưa xác nhận:** cấu hình production, khả năng vận hành bơm/van nông nghiệp thật, benchmark, endpoints và triển khai các công nghệ minh họa không có trong brief.
- Cần đối chiếu mã nguồn, kiểm thử render Mermaid, rà soát tiếng Nhật và thử trả lời có bấm giờ trước khi đánh dấu Reviewed.

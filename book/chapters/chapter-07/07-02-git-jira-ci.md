# 第07.02課 — Git・Jira・CI/CD

> **BRSE Interview Master · Draft / Pending review**  
> Trình độ N3–N2; mục tiêu hội thoại chính 15–30 giây. Nội dung giải thích kỹ thuật là học liệu; không khẳng định người học từng làm các thao tác nếu chưa có bằng chứng. Các endpoint/sơ đồ minh họa không phải đặc tả dự án khi không được xác nhận.

## ① 学習目標 — Mục tiêu

Hiểu và giải thích được **Git・Jira・CI/CD**, trả lời một câu hỏi kỹ thuật chính, xử lý ít nhất một follow-up, sử dụng từ vựng IT tiếng Nhật, và chuyển kiến thức sang tình huống mới.

## ② 面接質問・質問の意図

**面接官：** GitとJiraはどう使い分けますか。

**Nhà tuyển dụng đánh giá:** Năng lực hiểu khái niệm, giải thích mục đích sử dụng và phân biệt kiến thức thực tế với giả định.

## ③ 技術知識・思考プロセス

**Cách tư duy:** Định nghĩa / tình huống → công dụng → rủi ro hoặc giới hạn → ví dụ. Khi hỏi về quyết định kỹ thuật của dự án, phải phân biệt *lợi ích chung* với *lý do lựa chọn thực tế được xác nhận*.

CI kiểm tra tích hợp; CD liên quan tự động hóa phân phối/triển khai.

## ④ 図解 — Hình minh họa

```mermaid
flowchart LR
C[Code Commit] --> PR[Pull Request]
PR --> CI[Automated Checks]
CI --> Rev[Review]
Rev --> M[Merge]
```

**Chú giải:** Sơ đồ có tính giáo dục. Không suy ra hạ tầng hoặc endpoint tương ứng đang tồn tại trong mã nguồn Smart Farm.

**日本語で説明してみよう：** まず全体の流れを確認します。次に、それぞれの役割を説明します。最後に、データの受け渡しや確認が必要な点をまとめます。

**Dịch:** Nắm luồng tổng thể, giải thích trách nhiệm các tầng, nêu điểm trao đổi dữ liệu và vấn đề cần xác minh.

## ⑤ 面接対話 — Hội thoại Nhật–Việt

**面接官：** GitとJiraはどう使い分けますか。

**応募者（Standard）：** Gitはコードの変更履歴を管理するために使います。Jiraはタスクや課題の進捗管理に使います。

**ベトナム語訳：** Git quản lý code; Jira quản lý issue và tiến độ.

**面接官（深掘り）：** CIとCDは何ですか。

**Câu hỏi đào sâu (Việt):** CI và CD là gì?

**応募者：** CIは変更を継続的に統合して検証する考え方です。CDはリリース準備やデプロイの自動化に関係します。

**ベトナム語訳：** CI là thực hành tích hợp và kiểm tra thay đổi liên tục. CD liên quan đến tự động hóa quá trình phân phối hoặc triển khai phần mềm.

**質問の型:** 何ですか → なぜ必要ですか → 具体的にはどうしますか. Khi có câu hỏi tiếp theo, ưu tiên giải thích một ý mới, không lặp toàn bộ định nghĩa.

## ⑥ 類似表現比較 — Cách diễn đạt phù hợp

- **使っています:** công nghệ đang dùng, không tự bao hàm lý do lựa chọn.
- **採用しました:** đã áp dụng; cần xác minh vai trò quyết định trước khi dùng ở ngôi cá nhân.
- **確認します / 検証します:** kiểm tra thông tin / kiểm chứng qua phương pháp.
- **実現できます / 可能性があります:** có thể thực hiện / có khả năng; không hứa tuyệt đối khi chưa đánh giá rủi ro.

## ⑦ 語彙・文法 — Từ vựng chuyên ngành

| 日本語 | 読み方 | Nghĩa |
|---|---|---|
| 変更履歴 | へんこうりれき | Lịch sử thay đổi |
| 課題管理 | かだいかんり | Quản lý issue |
| 自動テスト | じどうテスト | Kiểm thử tự động |
| 統合 | とうごう | Tích hợp |
| レビュー | レビュー | Review |
| ブランチ | ブランチ | Nhánh code |

**Mẫu câu phỏng vấn:** Gitで変更履歴を管理し、Jiraで課題と進捗を管理します。

**Dịch sát nghĩa:** Tôi dùng Git quản lý lịch sử thay đổi và Jira quản lý issue, tiến độ.

## ⑧ 実践練習 — Active recall và chuyển ngữ cảnh

**Bước 1 — 20 giây:** Tự trả lời câu phỏng vấn chính không nhìn mẫu. Nêu kết luận, lý do, giới hạn và ghi âm để tự đối chiếu.

**Bước 2 — Câu hỏi ứng dụng:**

**面接官：** CIのチェックが失敗した時、どのように対応しますか。

**Dịch câu hỏi:** Khi kiểm tra CI thất bại, bạn xử lý thế nào?

**応募者（回答例）：** 失敗したテストとログを確認し、変更内容との関係を調べます。原因が不明なら状況を共有します。

**Dịch câu trả lời:** Tôi kiểm tra bài test và log lỗi, xem liên quan thay đổi mã thế nào; chưa rõ nguyên nhân thì chia sẻ tình hình.

**Bước 3 — Tình huống chuyên biệt:** Viết một Jira bug giả định: hiện tượng, điều kiện tái hiện, kết quả mong đợi, mức ảnh hưởng. Không nói repo hiện có pipeline đã pass.

**Bước 4 — BrSE transfer:** Hãy nói lại câu trả lời cho khách hàng bằng tiếng Nhật dễ hiểu, tách điều đã kiểm tra khỏi đề xuất/giả định; không tự cam kết production, an toàn hoặc deadline.

**Bước 5 — Tự đánh giá:** 0–4 cho mỗi tiêu chí: đúng kiến thức, rõ ràng, tiếng Nhật tự nhiên, đúng trọng tâm và phản hồi câu đào sâu. Tổng /20. Không chấm phát âm qua văn bản nếu chưa có ghi âm.

**AI Interviewer:** あなたは日本企業のBrSE面接官です。上記の内容について一問ずつ質問し、私の回答を待ってください。その回答に基づいて深掘りを一つ行い、最後に自然な言い方と事実関係の注意点を教えてください。

## ⑨ 評価・改善 — Rubric /20

Tự chấm năm tiêu chí 0–4: đúng trọng tâm, chính xác kỹ thuật, tiếng Nhật tự nhiên, diễn giải mạch lạc, phản xạ follow-up. Thang 16–20 tốt, 12–15 cần chỉnh, dưới 12 học lại là thước đo **nội bộ**. Không tự chấm phát âm khi không có audio.

**Quy trình sửa:** Rút ngắn câu, chỉ ra giới hạn cần xác minh, thử giải thích lại cho khách hàng không chuyên và làm mới ví dụ.

## ⑩ 出典・検証状況

- Kiến thức cơ bản về lập trình / kiến trúc / QA / yêu cầu là **nội dung giáo dục tổng quát**, không trích xuất trực tiếp từ source code.
- Với Smart Farm, brief cung cấp: ESP32/Wokwi, AWS IoT Core, MQTT/TLS/X.509, backend Java 21/Spring Boot/Spring JDBC/modular monolith, PostgreSQL, React/REST/polling, kiểm thử JUnit/Spring Boot Test/Playwright; backend và DB chủ yếu local, luồng ESP32/Wokwi–AWS–backend có bằng chứng chạy thử theo mô tả.
- **Chưa xác nhận:** cấu hình production, khả năng vận hành bơm/van nông nghiệp thật, benchmark, endpoints và triển khai các công nghệ minh họa không có trong brief.
- Cần đối chiếu mã nguồn, kiểm thử render Mermaid, rà soát tiếng Nhật và thử trả lời có bấm giờ trước khi đánh dấu Reviewed.

# 第05章 — フレームワーク・データベース | Framework và Database

> **BRSE Interview Master** · N3–N2 · **Draft: chương nền tảng, chưa phải bộ bài chuyên sâu đầy đủ**.  
> Các câu trả lời chính là **ví dụ luyện tập** (mục tiêu 15–30 giây), không tự nhận là kinh nghiệm cá nhân hoặc mẫu được người Nhật thẩm định. Với câu có 【】, phải thay bằng dữ liệu có bằng chứng trước phỏng vấn.

## ① 学習目標 — Mục tiêu

Hiểu các khái niệm chính của chương **Framework và Database**, trình bày bằng tiếng Nhật gọn, trả lời câu hỏi đào sâu, phân biệt dữ kiện với nhận định, và tự đánh giá. Học theo chu trình **Understand → Think → Answer → Follow-up → Retry**.

## ② 技術知識・考え方 — Kiến thức và phương pháp

### 05.01 — Spring Bootは何に使いますか。

**質問の意図:** Nhà tuyển dụng đánh giá khả năng hiểu câu hỏi, đưa lý do và trả lời có căn cứ.

**Khung tư duy:** **Kết luận → Lý do → ví dụ/giới hạn**; với kinh nghiệm: **Vai trò thực → Hành động thực → kết quả xác minh**.

**面接官：** Spring Bootは何に使いますか。

**応募者（Standard）：** JavaでREST APIや業務処理を実装するために使います。Smart Farmではデータ処理やコマンド管理を行います。

**ベトナム語訳（diễn giải）：** Nội dung trọng tâm: framework và database, trả lời trực tiếp, không nói vượt quá phạm vi đã biết. Hãy tự diễn giải lại câu Nhật sang tiếng Việt trong khi học để kiểm tra hiểu nghĩa.

**深掘り・面接官：** Spring JDBCとは。

**応募者：** JavaからSQLを使ってデータベースを操作する仕組みです。

**応用練習:** Đổi bối cảnh sang một dự án khác và trả lời lại trong tối đa 30 giây; nếu là kinh nghiệm cá nhân chỉ dùng sự kiện đã xác minh.

### 05.02 — Reactは何に使いますか。

**質問の意図:** Nhà tuyển dụng đánh giá khả năng hiểu câu hỏi, đưa lý do và trả lời có căn cứ.

**Khung tư duy:** **Kết luận → Lý do → ví dụ/giới hạn**; với kinh nghiệm: **Vai trò thực → Hành động thực → kết quả xác minh**.

**面接官：** Reactは何に使いますか。

**応募者（Standard）：** ユーザーが操作するWeb画面を作ります。REST APIを通じてバックエンドからデータを取得します。

**ベトナム語訳（diễn giải）：** Nội dung trọng tâm: framework và database, trả lời trực tiếp, không nói vượt quá phạm vi đã biết. Hãy tự diễn giải lại câu Nhật sang tiếng Việt trong khi học để kiểm tra hiểu nghĩa.

**深掘り・面接官：** Vueとの違いは。

**応募者：** どちらもUI開発に使えますが、設計や記述方法が異なります。

**応用練習:** Đổi bối cảnh sang một dự án khác và trả lời lại trong tối đa 30 giây; nếu là kinh nghiệm cá nhân chỉ dùng sự kiện đã xác minh.

### 05.03 — トランザクションとは何ですか。

**質問の意図:** Nhà tuyển dụng đánh giá khả năng hiểu câu hỏi, đưa lý do và trả lời có căn cứ.

**Khung tư duy:** **Kết luận → Lý do → ví dụ/giới hạn**; với kinh nghiệm: **Vai trò thực → Hành động thực → kết quả xác minh**.

**面接官：** トランザクションとは何ですか。

**応募者（Standard）：** 複数の操作を一つのまとまりとして扱う仕組みです。データの整合性を守るために重要です。

**ベトナム語訳（diễn giải）：** Nội dung trọng tâm: framework và database, trả lời trực tiếp, không nói vượt quá phạm vi đã biết. Hãy tự diễn giải lại câu Nhật sang tiếng Việt trong khi học để kiểm tra hiểu nghĩa.

**深掘り・面接官：** ロールバックは。

**応募者：** 失敗した操作を取り消す必要がある時に使います。

**応用練習:** Đổi bối cảnh sang một dự án khác và trả lời lại trong tối đa 30 giây; nếu là kinh nghiệm cá nhân chỉ dùng sự kiện đã xác minh.

## ③ 図解 — Minh họa

```mermaid
flowchart LR
 UI[React] --> API[Spring Boot REST]
 API --> DB[(PostgreSQL)]
```

**日本語で説明：** まず質問の意図を確認します。次に、結論と理由を短く説明します。必要な場合は具体例を加え、確認できていないことは区別します。

## ④ 語彙・表現 — Từ vựng

| 日本語 | 読み方 | Nghĩa |
|---|---|---|
| 取引 | とりひき | Giao dịch |
| 整合性 | せいごうせい | Tính nhất quán |
| 操作 | そうさ | Thao tác |

**類似表現比較:** 「確認しました」 (đã kiểm tra) khác 「検証しました」 (đã kiểm chứng bằng phương pháp); 「できます」 (có thể) khác 「本番で運用しています」 (đang vận hành production). Hãy chọn theo bằng chứng và ngữ cảnh.

## ⑤ 会話練習 — Luyện tập

1. Trả lời không nhìn mẫu ba câu hỏi trong chương.
2. AI interviewer hỏi từng câu bằng tiếng Nhật, đợi bạn trả lời, sau đó hỏi một câu sâu hơn dựa trên chính câu vừa nói.
3. Chuyển bối cảnh hoặc dữ liệu của câu hỏi, không lặp lại nguyên văn câu mẫu.
4. Tự trình bày một khái niệm bằng tiếng Nhật trong 20–30 giây và giải thích lại ý bằng tiếng Việt.

**Prompt để luyện:** あなたはBrSE面接官です。第05章「フレームワーク・データベース」について、一問ずつ質問してください。毎回私の回答を待ち、関連する深掘り質問を一つだけしてください。最後に簡潔なフィードバックをください。経験が未確認なら事実として扱わないでください。

## ⑥ 評価・改善 — Rubric /20

Chấm 0–4 cho mỗi tiêu chí: **đúng trọng tâm**, **kiến thức chính xác**, **tiếng Nhật tự nhiên**, **diễn đạt mạch lạc**, **đối đáp đào sâu**. 16–20 tốt, 12–15 cần sửa, dưới 12 ôn lại. Đây là thang tự luyện nội bộ; không chấm phát âm khi chỉ có văn bản.

## ⑦ 出典・検証状況 — Giới hạn nguồn

- Kiến thức và hội thoại chung là nội dung **biên soạn phục vụ học tập**, chưa được reviewer Nhật hoặc kỹ sư độc lập nghiệm thu.
- Các chi tiết Smart Farm nếu xuất hiện chỉ dựa trên mô tả người dùng: backend và PostgreSQL chủ yếu local, ESP32/Wokwi–AWS–backend có bằng chứng chạy thử theo mô tả, chưa xác nhận production hoặc bơm/van nông nghiệp thật.
- Những câu về CV, mục tiêu, điểm mạnh/yếu là **mẫu**, phải sửa theo sự thật; không dùng câu mẫu như một tuyên bố kinh nghiệm cá nhân.
- Chưa có bằng chứng đo thời gian nói/kiểm thử render Mermaid trong lần biên soạn này.

**Tiếp theo:** Tách ba chủ đề 05.01–05.03 thành bài học riêng sau khi kiểm định template, bổ sung câu trả lời Professional, bản dịch sát nghĩa và bài tập tình huống chuyên sâu.

# R1 — Báo cáo kiểm định chất lượng bản thảo BRSE Interview Master

**Ngày:** 2026-10-22  
**Phạm vi đợt này:** Rà soát nội dung trực tiếp năm file đại diện ở chương 01, 04, 10, 12, 14; đối chiếu khung biên soạn và sửa trực tiếp bài 01.01.  
**Giới hạn:** Chưa kiểm toán toàn bộ 49 bài, chưa có chứng nhận tiếng Nhật bản ngữ, chưa render Mermaid bằng công cụ, chưa kiểm chứng code Smart Farm thực tế. **Không đánh dấu toàn bộ giáo trình là Reviewed.**

## 1. Mẫu đã đọc

| File | Kết quả quan sát | Hành động |
|---|---|---|
| `chapter-01/01-01-self-introduction.md` | Câu ứng viên mô tả *cách* giới thiệu, không phải câu trả lời giới thiệu thực tế; phần gắn nhãn dịch Việt là hướng dẫn, không phải dịch sát tiếng Nhật | **Đã sửa trực tiếp**, giữ placeholder cần điền theo CV |
| `chapter-04/04-02-http-rest.md` | Có hội thoại, dịch tiếng Việt, Mermaid, rubric; từ vựng khá chung, chưa chuyên theo bài REST; một số diễn giải cần đối chiếu chuẩn HTTP | Chờ biên tập |
| `chapter-10/10-03-keigo-confirmation.md` | Có câu Nhật, dịch tương ứng và Mermaid; cần reviewer xét sắc thái lịch sự trong thực tế khách hàng | Chờ reviewer |
| `chapter-12/12-05-device-control-ack.md` | Có flow và sequence Mermaid; phân biệt publish, ACK, reported state, physical state; cần kiểm định theo firmware/DB/test thật | Chờ kiểm định kỹ thuật |
| `chapter-14/14-03-reverse-questions-evaluation.md` | Có hội thoại, dịch và bài tập; câu hỏi ngược cần phù hợp với JD cụ thể | Chờ thử với JD |

**Kết luận mẫu:** Số mục/tiêu đề không tương đương chất lượng sư phạm. Vấn đề rõ nhất là nội dung **gắn nhãn “dịch” nhưng thực chất là diễn giải hoặc hướng dẫn**; phải rà soát theo từng câu.

## 2. Quy tắc sửa bắt buộc — Definition of Done

- Mỗi câu **面接官** và **応募者** phải có bản dịch tiếng Việt **tương ứng từng phát ngôn**, không thay bằng nhận xét chung hoặc hướng dẫn học.
- Câu trả lời chính 2–4 câu, mục tiêu 15–30 giây; đo bằng tập nói, không chỉ đếm ký tự.
- Câu đào sâu phải tiếp nối ý trong câu trả lời chính; có đáp án, bản dịch, và tiêu chí đúng.
- Tách **kiến thức kỹ thuật** khỏi **script phỏng vấn**; nguồn thông tin kỹ thuật phải truy được, không tự thêm stack.
- Mỗi bài có từ vựng **đặc trưng chủ đề** bên cạnh từ vựng tái sử dụng. Ghi cách đọc đúng và ví dụ tự nhiên.
- Những nội dung ngôi thứ nhất có kinh nghiệm/CV phải dựa bằng chứng; giữ `【】` nếu chưa có dữ liệu và đánh dấu **needs personalization**.
- Mermaid: phải render thành công, có alt text, nêu sơ đồ **minh họa** hay **đã đối chiếu hệ thống**.
- Review tiếng Nhật: cần người hiểu business Japanese đánh giá hội thoại, không tự ghi native-reviewed.
- Kiểm định “đã kiểm thử” ≠ “production”; đặc biệt Smart Farm **ESP32/Wokwi–AWS–backend** chỉ có evidence thử nghiệm theo mô tả.
- Thử với người học N3–N2: trả lời không nhìn mẫu và chuyển ngữ cảnh; chấm 5 tiêu chí × 0–4.

## 3. Checklist ưu tiên

| Ưu tiên | Vấn đề | Phạm vi xử lý | Tình trạng |
|---|---|---|---|
| P0 | Nhãn dịch không phải bản dịch sát câu Nhật | Kiểm tra từng lời thoại của mọi bài | Đã sửa bài 01.01; còn lại chưa rà hết |
| P0 | Placeholder `【】` trong câu trả lời cá nhân | Chương 01–03, 13–14 và bài 12.08 | Cần CV/evidence |
| P1 | Từ vựng chung chung, thiếu chuyên ngành | Các bài mới 04–08 và nhiều foundation | Cần viết lại theo chủ đề |
| P1 | Chuẩn hóa mục lục, mục nhỏ và ID | 49 bài và 13 foundation | Chưa thực hiện toàn bộ |
| P1 | Mermaid rendering và accessibility | Toàn sách | Chưa chạy |
| P1 | Kiểm định kiến trúc Smart Farm bằng code | Chương 12 | Chưa thực hiện |
| P2 | Đo thời gian đáp án và mock interview | Người học N3–N2 | Chưa thực hiện |
| P2 | Reviewer tiếng Nhật chuyên ngành | Toàn sách | Chưa thực hiện |

## 4. Tiêu chí trạng thái

- **Draft:** file đã tạo nhưng chưa qua QA.
- **Needs Revision:** phát hiện lỗi nội dung/dịch/kỹ thuật chưa sửa.
- **Structurally Checked:** có hội thoại, giải thích, từ vựng, luyện tập và rubric; không ngụ ý chất lượng đã đạt.
- **Language Reviewed:** đã có bằng chứng reviewer và sửa ngôn ngữ.
- **Technical Reviewed:** các claim kỹ thuật đã được đối chiếu nguồn/code/kiểm thử trong phạm vi cần thiết.
- **Publish Ready:** đã đạt kiểm tra Markdown/Mermaid, dịch, sư phạm, khả năng ứng dụng và bảo đảm không nhầm claim.

## 5. Trình tự xử lý đề xuất

1. Tạo script quét 49 bài: link, Mermaid fences, heading, missing translations, placeholder.
2. Sửa P0 từng bài; **không thay bản dịch bằng diễn giải**.
3. Review tập trung ba chương 01, 03, 09; chuyển các mẫu chưa cá nhân hóa thành bài tập điền thông tin.
4. Thử roleplay 10 câu bằng tiếng Nhật, ghi evidence lỗi thật.
5. Kiểm định kiến trúc Smart Farm và render sơ đồ.
6. Chỉ cập nhật trạng thái từng bài có minh chứng.

**Kết quả thực hiện lần này:** sửa `01-01-self-introduction.md` và tạo báo cáo R1. Toàn bộ 49 bài vẫn chưa đạt trạng thái Reviewed.

## 6. Tiến độ sửa P0 — đợt tiếp theo (2026-10-22)

**Đã sửa trực tiếp thêm 8 bài:**

- `chapter-01/01-02-strengths-weaknesses.md`
- `chapter-01/01-03-learning-attitude.md`
- `chapter-03/03-01-cv-timeline.md`
- `chapter-03/03-02-project-story.md`
- `chapter-03/03-03-individual-contribution.md`
- `chapter-09/09-01-feasibility.md`
- `chapter-09/09-02-scope-conflict.md`
- `chapter-09/09-03-critical-bug.md`

Thay các mục `ベトナム語訳` vốn chỉ ghi hướng dẫn chung bằng **bản dịch đúng nội dung câu tiếng Nhật của ứng viên** ở câu chính và câu đào sâu. Kết hợp lần trước, **9 bài đã sửa** về lỗi P0 dạng này. Giữ nguyên những placeholder `【】` vì chưa có minh chứng kinh nghiệm cá nhân.

**Phạm vi chưa thực hiện:** chưa xác nhận 40 bài còn lại đều có lỗi tương tự; chưa rà soát toàn bộ lời của người phỏng vấn, chưa kiểm thử Mermaid, chưa native review. Các bản đã sửa vẫn ở trạng thái Draft chờ QA bổ sung.


## 7. Đợt R1 tiếp theo — chương 04–08 (2026-10-22)

**Đã sửa trực tiếp 15/15 bài riêng của chương 04–08**. Phát hiện một lỗi cấu trúc nghiêm trọng: các code fence `mermaid` trước đó chứa **lời hướng dẫn văn bản**, không phải cú pháp Mermaid; tất cả đã được thay bằng **source Mermaid dạng flowchart, sequenceDiagram hoặc classDiagram** phù hợp với từng bài. Cũng đã bổ sung bản dịch tiếng Việt **cho câu hỏi đào sâu** và điều chỉnh phần dịch của đáp án follow-up theo từng nội dung.

**Kiểm tra sau commit:** đọc lại đúng 15 file và xác nhận mỗi file có fence Mermaid bắt đầu bằng `flowchart`, `sequenceDiagram` hoặc `classDiagram`, đồng thời có nhãn `Câu hỏi đào sâu (Việt)`. **Chưa có bằng chứng các sơ đồ đã render thành công trong công cụ Mermaid**; đây là kiểm tra tĩnh có giới hạn.

**Tổng tiến độ sửa file trực tiếp R1:** 24/49 bài đã được đụng tới bởi các đợt sửa (9 bài trước + 15 bài mới). Không suy ra 24 bài đạt Reviewed: vẫn thiếu review tiếng Nhật, kiểm tra bản dịch từng câu, luyện thời lượng và kiểm chứng các claim kỹ thuật.

**P0 tiếp theo:** chương 02, 10, 11, 13, 14 (15 bài) và đánh giá chương 12 (10 bài). **P1:** chuyển từ vựng chung chung sang thuật ngữ riêng từng bài, loại bỏ các ghi chú diễn giải không phải bản dịch; kiểm tra render Mermaid tự động.


## 8. Đợt R1 — chương 02, 10, 11, 13, 14 (2026-10-22)

**Đã sửa 15/15 bài riêng** của năm chương này: bổ sung **bản dịch tiếng Việt cho câu hỏi của người phỏng vấn và câu hỏi đào sâu**, thay ghi chú Professional/Keigo sao chép máy móc bằng hướng dẫn tùy ngữ cảnh. Riêng `10-03-keigo-confirmation.md` sửa cách xin xác nhận sang `こちらの認識で相違ないでしょうか`; `14-01-final-selfintro.md` thay lời hướng dẫn “tôi sẽ giới thiệu…” bằng **mẫu lời giới thiệu thực sự** có placeholder cần điền.

**Kết quả sửa file:** Tổng cộng **39/49 bài** đã được sửa trực tiếp trong R1 (9 + 15 + 15). Không tương đương đạt Reviewed: còn nhiều phần từ vựng lặp, template chưa cá nhân hóa, render Mermaid chưa kiểm thử, diễn đạt tiếng Nhật chưa được reviewer độc lập kiểm định.

**Các bước kế:** đánh giá 10 bài Chương 12 về bản dịch, độ chính xác kỹ thuật và Mermaid; rà lại chất lượng thực tế 39 bài đã sửa; ghi lỗi vào issue hoặc checklist từng bài; chỉ sau đó mới quyết định export.

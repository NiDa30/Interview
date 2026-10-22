# V2 — Báo cáo nâng cấp độ sâu học liệu BRSE Interview Master

**Ngày:** 22/10/2026  
**Trạng thái:** Đã biên soạn, đang kiểm thử bản sách dựng lại; **chưa nghiệm thu nội dung bản ngữ / thực hành người học**.

## Thay đổi so với V1

Thay vì chỉ dài hơn, mỗi bài có thêm **mục ⑪ 深掘り・実務演習** với sáu tầng:
1. Bản chất/cơ chế; 2. Case study áp dụng; 3. Rủi ro, trade-off và giới hạn; 4. Câu trả lời tiếng Nhật có dịch; 5. Bài lab có sản phẩm; 6. Tiêu chí đạt có thể kiểm tra.

**Phạm vi:** 49/49 bài có một tệp mở rộng riêng tại `book/deep-dives/<ID>.md`; bản sách `deliverables/BRSE-Interview-Master.md` có đủ 49 mục ⑪, 7 lab lập trình/contract/safety, 14 chương và 53 Mermaid sơ đồ. Các lab riêng sâu ở 04.02 (HTTP), 05.01 (JDBC/SQL), 05.03 (DB–MQTT/outbox), 08.03 (BDD), 12.04 (telemetry JSON), 12.05 (command state), 12.06 (hazard analysis).

## Phân bổ chương

| Chương | Phạm vi nâng cấp | Số bài |
|---|---|---:|
| 01 | Tự giới thiệu, điểm mạnh/yếu, phương pháp học có evidence | 3 |
| 02 | Động lực BrSE, làm việc Nhật, lộ trình năng lực | 3 |
| 03 | CV, kể dự án, traceability đóng góp cá nhân | 3 |
| 04 | OOP/invariants, REST contract, API incident | 3 |
| 05 | Spring/JDBC, React/polling, DB–MQTT transaction | 3 |
| 06 | Modular monolith, AWS IoT security, performance metrics | 3 |
| 07 | Agile/Scrum, Git/Jira/CI, chiến lược testing | 3 |
| 08 | Requirement hearing, làm rõ spec, change control/BDD | 3 |
| 09 | Feasibility, scope negotiation, critical bug | 3 |
| 10 | 報連相, 連絡/相談, business Keigo | 3 |
| 11 | Phân biệt 確認/検証/調査, 対応/処理, できます/可能です | 3 |
| 12 | Smart Farm: product, architecture, stack, telemetry, command ACK, safety, troubleshooting, contribution, demo, mock | 10 |
| 13 | Mock interview tổng hợp, technical, BrSE | 3 |
| 14 | Tổng kết 60 giây, trả lời chưa biết, reverse questions | 3 |

| **Tổng** | **49 tệp bổ sung theo đúng từng bài** | **49** |

## Ví dụ tiêu chuẩn đầu ra

- **REST/API:** Người học viết contract GET và command, phân biệt HTTP 200/202 với ACK và tác động vật lý.
- **Backend/DB:** Người học viết parameterized SQL, nhận diện transaction boundary và trạng thái DB commit thành công nhưng MQTT lỗi.
- **Cloud IoT:** Người học tách TLS/X.509, topic authorization, certificate lifecycle, xử lý sự cố.
- **BA/BrSE:** Người học lập requirement hearing, acceptance criteria Given/When/Then, change request và quyết định có owner.
- **IoT Safety:** Người học xây state machine command và hazard matrix; **Wokwi không được xem là proof bơm vật lý an toàn**.
- **Tiếng Nhật:** Người học diễn giải kết luận → cơ chế → minh chứng → giới hạn; đáp án mẫu không được tự nhận thành kinh nghiệm cá nhân.

## Kiểm chứng nguồn

Chương 12 trích dẫn để đối chiếu: [NiDa30/smart-farm-management-system commit 7f16662](https://github.com/NiDa30/smart-farm-management-system/tree/7f16662f78ad5d8fc83983bf7047c5d6a2ae4d56). Chỉ dùng để soát code theo snapshot, không tự suy ra API/firmware đã test runtime hoặc độ an toàn vật lý.

## Gate QA đang áp dụng

- **Static:** Python QA kiểm tra 49 lesson links, 49 nội dung ⑪ đặc trưng, 7 lab, số fences, link, 107 cặp câu hỏi–dịch Chương 12.
- **CI Mermaid:** Render nguồn bằng Mermaid CLI.
- **PDF:** Export bản mới từ compiled Markdown; kiểm tra số trang và glyph/đồ họa trên trang mẫu.
- **Chưa nghiệm thu:** Native Japanese review, đánh giá hiệu quả học với người thật, API/integration/hardware Wokwi/AWS runtime, kiểm tra đầy đủ trang PDF.

**Kết luận:** V2 là bản mở rộng thực chất cho tự học và chuẩn bị phỏng vấn. Chỉ công bố bản *Review Candidate* cho đến khi qua đánh giá độc lập.

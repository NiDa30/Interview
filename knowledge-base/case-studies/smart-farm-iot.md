# Project Knowledge Base — Smart Farm IoT Management System

> **Cập nhật:** 2026-10-26 · **Phạm vi:** Căn cứ cho Chapter 12 (技術デモ・プレゼンテーション)  
> **Nguồn dự án duy nhất hiện có:** [sources/project-evidence/smart-farm-overview.md](../../sources/project-evidence/smart-farm-overview.md) — mô tả do chủ dự án (người dùng) cung cấp. Chưa có mã nguồn, README, log test hay ảnh demo trong repository.

File này tổ chức lại dữ kiện từ nguồn trên để người biên soạn tra cứu nhanh. **Không thêm dữ kiện mới.** Mọi mục dự án dưới đây có trạng thái `author-experience—unverified` (chủ dự án mô tả, chưa có chứng cứ độc lập), trừ khi ghi khác.

## 1. Mức độ hoàn thiện — ba tầng phải phân biệt

| Tầng | Ý nghĩa | Hạng mục thuộc tầng này (theo nguồn) |
|---|---|---|
| **Implemented** (đã phát triển) | Có chức năng/code theo mô tả | Quản lý node, kênh cảm biến, khu vực, nhánh tưới gắn trạm nước; giám sát gần thời gian thực, lịch sử, cảnh báo, xuất CSV; bật/tắt có thời hạn; quy tắc tưới theo độ ẩm đất và lịch cho phép; quy trình tưới xác nhận từng bước, kiểm tra phản hồi van, điều kiện nước/mưa/lưu lượng; theo dõi phiên tưới, sự kiện, ước tính lượng nước kèm độ phủ dữ liệu |
| **Tested** (đã chạy thử) | Có bằng chứng chạy thử theo mô tả | Luồng ESP32/Wokwi → AWS IoT Core → backend. Các chức năng nâng cao **còn cần nghiệm thu thêm** |
| **Production Verified** | Đã vận hành thật | **Không có.** Chưa triển khai production; chưa xác nhận vận hành bơm/van nông nghiệp thực tế |

Môi trường hiện tại: backend và PostgreSQL chủ yếu chạy **local**, kết nối AWS IoT Core.

## 2. Công nghệ

| Thành phần | Công nghệ | Vai trò theo nguồn |
|---|---|---|
| Thiết bị | ESP32, C/C++, Arduino Framework, PlatformIO | Đọc cảm biến, gửi dữ liệu, xử lý lệnh |
| Mô phỏng | Wokwi | Mô phỏng nhiệt độ, độ ẩm, độ ẩm đất, nguồn nước, lưu lượng, thời tiết, actuator |
| Kết nối thiết bị | AWS IoT Core, MQTT, TLS, X.509 | Telemetry và lệnh điều khiển qua kết nối xác thực |
| Kết nối backend ↔ AWS | MQTT qua WSS / SigV4 (theo sơ đồ nguồn) | Backend nhận bản tin và publish lệnh |
| Backend | Java 21, Spring Boot, Spring JDBC, AWS IoT Device SDK | REST API, tiếp nhận dữ liệu, cảnh báo, quy trình tưới |
| Frontend | React, TypeScript, Vite, Tailwind CSS | Dashboard, khu vực, giám sát cảm biến, điều khiển |
| CSDL | PostgreSQL 16, Flyway | Dữ liệu cảm biến, cấu hình, lệnh, ACK, sự kiện, lịch sử phiên tưới |
| Công cụ | Python, Docker Compose, Git, Maven | Chuẩn bị thiết bị, môi trường dev, tự động hóa |
| Kiểm thử | JUnit, Spring Boot Test, PostgreSQL integration tests, Playwright | Nghiệp vụ, API, giao diện |

## 3. Kiến trúc

- **Backend:** modular monolith — module thiết bị, telemetry, cảnh báo, tự động hóa, điều khiển, báo cáo trong **một** ứng dụng Spring Boot. Không mô tả là microservices.
- **Thiết bị ↔ hệ thống:** publish/subscribe bất đồng bộ (MQTT qua AWS IoT Core).
- **Web ↔ backend:** REST API + polling.
- **Telemetry:** bản tin có mã thiết bị, boot ID, sequence, thời gian đo. Backend xác thực dữ liệu, xử lý trùng lặp, lưu lịch sử, đánh giá cảnh báo.
- **Điều khiển:** lưu mã lệnh và ý định **trước khi gửi**; sau đó đối chiếu riêng **kết quả gửi**, **ACK**, **trạng thái thiết bị**.
- **Actuator trong mô phỏng:** LED đại diện bơm/van.

## 4. Khoảng trống thông tin (chưa được cung cấp)

Không được viết các mục sau như sự thật cho tới khi có chứng cứ:

| Thiếu | Ảnh hưởng tới bài |
|---|---|
| Vai trò cá nhân, phạm vi phụ trách, tỷ lệ đóng góp | 12.08 không thể viết câu trả lời cá nhân hóa; mọi bài dùng mẫu điền 【 】 |
| Thời gian dự án, quy mô nhóm, bối cảnh (cá nhân / đồ án / công ty) | Không nói 「チームで」「一人で」「○か月」 |
| Lý do chọn công nghệ (MQTT, modular monolith, PostgreSQL…) do chủ dự án xác nhận | Lý do trong bài chỉ là `hypothetical` — lập luận hợp lý để luyện, không phải quyết định đã xác nhận |
| Tên topic MQTT, QoS sử dụng, chu kỳ polling, timeout ACK, schema bảng | Không nêu giá trị cụ thể |
| Số liệu latency, throughput, availability, tiết kiệm nước, coverage test | Không nêu số |
| Kết quả test từng chức năng, ảnh/video demo | 12.09 (demo) cần bằng chứng trước khi viết kịch bản |
| Có retry tự động / timeout lệnh hay không | 12.05 chỉ trình bày như hướng xử lý đề xuất |
| Ý nghĩa của ACK cấp ứng dụng ("đã nhận" hay "đã thực hiện"), có dùng persistent session không | Chỉ dùng cách nói trung lập: 「コマンドに対する応答」 |

## 5. Kiến thức kỹ thuật chung đã đối chiếu (dùng cho giải thích, không phải dữ kiện dự án)

Truy cập ngày 2026-10-26.

| Nhận định | Nguồn | Trạng thái |
|---|---|---|
| MQTT là giao thức nhắn tin chuẩn OASIS cho IoT, thiết kế publish/subscribe cực nhẹ | [mqtt.org](https://mqtt.org/) | `verified` |
| AWS IoT Core: MQTT (pub/sub) xác thực bằng X.509 client certificate qua TLS; MQTT over WebSocket xác thực bằng SigV4; HTTPS chỉ publish | [AWS — Device communication protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html) | `verified` |
| So với HTTPS trên AWS IoT Core, MQTT có overhead và điện năng thấp hơn, hỗ trợ subscribe | Như trên (bảng so sánh MQTT/HTTPS) | `verified` |
| AWS IoT Core hỗ trợ QoS 0 và 1, **không hỗ trợ QoS 2**; QoS 1 gửi ít nhất một lần tới khi nhận PUBACK; QoS 0 có thể giao 0 hoặc nhiều lần | [AWS — MQTT](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html) | `verified` |
| Giao bản tin theo QoS chỉ tính giữa một bên gửi và một bên nhận; broker giao cho từng client độc lập → PUBACK backend nhận là của broker, không phải của thiết bị | [OASIS — MQTT Version 3.1.1](https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/os/mqtt-v3.1.1-os.html), mục 4.3 | `verified` |
| AWS IoT xác thực client certificate bằng chế độ client authentication của TLS, kiểm tra private key tương ứng | [AWS — X.509 client certificates](https://docs.aws.amazon.com/iot/latest/developerguide/x509-client-certs.html) | `verified` |
| Kết nối MQTT có thể gián đoạn; thiết bị phải tự phát hiện mất kết nối và kết nối lại | [AWS — Device communication protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html) (Connection duration limits) | `verified` |
| Spring Modulith hỗ trợ module logic trong một ứng dụng Spring Boot; module có API cung cấp và phần nội bộ không cho module khác truy cập | [Spring Modulith — Fundamentals](https://docs.spring.io/spring-modulith/reference/fundamentals.html) | `verified` (khái niệm; dự án **không** được xác nhận là dùng Spring Modulith) |
| Flyway áp dụng versioned migration theo thứ tự và ghi lịch sử vào schema history table | [Flyway — Migrations](https://documentation.red-gate.com/fd/migrations-271585107.html) | `verified` |
| Transaction trong PostgreSQL gộp nhiều bước thành một thao tác all-or-nothing | [PostgreSQL 16 — Transactions](https://www.postgresql.org/docs/16/tutorial-transactions.html) | `verified` |
| REST là tập ràng buộc kiến trúc cho hệ thống phân tán | [MDN — REST](https://developer.mozilla.org/en-US/docs/Glossary/REST) | `verified` |

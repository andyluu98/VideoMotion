# Blueprint (bản vẽ kỹ thuật)

> Cả deck là một tờ bản vẽ thi công: nét trắng khô và chính xác trên giấy xanh, chỉ phần ghi chú mới được dí dỏm.

**Hợp:** xây dựng, kiến trúc, cơ khí, phần cứng, giải thích hệ thống kỹ thuật, quy trình sản xuất.
**Không hợp:** cảm xúc, thời trang, ẩm thực, trẻ em.
**Cảm xúc:** kỹ thuật, chính xác, cổ điển, trí tuệ.

## Hình dung
Mỗi slide là một "HÌNH n" trên cùng một tờ giấy cyanotype. Người xem có cảm giác đang đứng cạnh bàn vẽ của kỹ sư: đường tâm, đường kích thước, gạch mặt cắt, bóng số, khung tên. Vật chính là thứ được thiết kế (công trình, máy, chi tiết), vẽ hình chiếu 2D bằng nét.

## Bảng màu
```css
--bg: #1f4386;          /* giấy xanh Phổ */
--deep: #0f2350;        /* vết nước, vùng đậm */
--fill: #22488f;        /* tô "giấy" dưới đường bao để che nét phía sau */
--line: #e7f0f9;        /* nét chính, chữ */
--line-soft: rgba(231,240,249,.62);  /* nét phụ, kích thước */
--hair: rgba(231,240,249,.3);        /* nét mảnh, gạch mặt cắt */
--stamp: #d7392b;       /* con dấu đỏ: dùng đúng một lần trong deck, cho phán quyết */
```
Biến thể đêm (gợi ý): nền `#08101e`, lưới xanh mờ, nhấn vàng an toàn `#ffc21a` thay con dấu đỏ, cho chủ đề công trường, an toàn lao động.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
```
- Tiêu đề: Barlow Condensed 600, IN HOA, giãn chữ 0,03 đến 0,06em, như chữ kẻ trên bản vẽ.
- Thân: IBM Plex Sans 400 đến 500.
- Mã, số, nhãn kỹ thuật: JetBrains Mono ("KC-02", "HÌNH 3", "A-A").

## Bề mặt
Lưới hai cấp (48px mờ, 192px rõ hơn), hạt giấy, nếp gấp giữa tờ, mép tờ bạc màu, khung viền đôi quanh tờ, khung tên góc phải dưới.
```css
background-image:
  linear-gradient(rgba(231,240,249,.06) 1px,transparent 1px), linear-gradient(90deg,rgba(231,240,249,.06) 1px,transparent 1px),
  linear-gradient(rgba(231,240,249,.1) 1px,transparent 1px), linear-gradient(90deg,rgba(231,240,249,.1) 1px,transparent 1px),
  radial-gradient(120% 90% at 35% 30%, #2a58a6, #234c96 45%, #18336b);
background-size: 48px 48px,48px 48px,192px 192px,192px 192px,100% 100%;
```

## Ngôn ngữ minh họa
- Bốn độ dày nét: đường bao 4px, chi tiết 2,5px, kích thước 2px, gạch mặt cắt 1,2px; đầu nét tròn.
- Kiểu nét: đường tâm `22 6 4 6`, nét khuất `10 7`, đường di chuyển (phantom) `28 6 6 6 6 6`.
- Vật đặc tô `--fill` rồi mới viền, để che nét phía sau. Gạch mặt cắt 45 độ bằng `<pattern>`.
- Bóng số (vòng tròn có số + đường dẫn kết thúc bằng chấm) để gọi tên bộ phận; giải thích số ở bảng kê.
- Đường kích thước ghi bằng chữ ký hiệu (L, B), không ghi số đo bịa.
- Vẽ vật, không vẽ người.

## Chữ ký chuyển động
- **Nét tự vẽ theo thứ tự của kỹ sư:** đường bao trước, chi tiết sau, kích thước và bóng số cuối (`<g data-anim="draw" data-stagger="150">`, nhãn `fade`).
- **Tia laser quét ngang** khi chuyển slide, như máy in bản vẽ (một vạch sáng mảnh chạy qua sân khấu).
- **Lưới trượt nhẹ** giữa các slide (lớp lưới cố định đổi `transform` theo `data-scene`), như đang lia trên tờ giấy lớn.
- **Chấm sáng chạy theo đường phantom** (`animateMotion`) để chỉ dòng làm việc, dòng dữ liệu.
- **Con dấu đóng** (`stamp`) cho phán quyết cuối.
- Nhịp: dứt khoát, không nảy, không lắc.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** công trình hoặc cỗ máy tự dựng từng nét, cần trục đung đưa, khung tên góc phải ghi tên deck.
- **Quy trình:** các "trạm" trên một trục kích thước, chấm sáng chạy qua từng trạm.
- **Kiến trúc hệ thống:** mặt cắt một tòa nhà, mỗi tầng là một lớp, dữ liệu đi lên theo trục thang máy.
- **Kết:** bản vẽ hoàn thiện, con dấu "DUYỆT" đóng xuống.

## Nên tránh
Gradient nhiều màu, bóng đổ màu, hiệu ứng 3D, glow neon, nét chạy qua chữ, câu dài trong SVG, logo phần mềm thật.

## Họ hàng
`iso-infographic` (hình isometric màu tươi, hợp giải thích hệ thống cho người không chuyên), `engraving` (khắc đồng cổ điển, hợp bảo tàng, khoa học).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/blueprint.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** cả phim xảy ra trên một tờ giấy bản vẽ xanh Phổ. Vật được thiết kế là nhân vật: ở ảnh là cần trục giàn thép có cờ, hộp máy bánh răng có đồng hồ và ống thổi, đám mây bị lưới hứng, một luống trồng nhỏ; kèm nhãn "FIG. 3" và bảng danh mục chi tiết, khung tên ở góc dưới phải. Người chỉ hiện dưới dạng bóng bàn tay cầm bút hoặc chữ ký. Vật chiếm 2/3 khung, chừa vùng trống để ghi chú.
- **Chất liệu và ánh sáng:** nền gradient xanh Phổ không đều (hai tông xanh, vệt tráng, nếp gấp mờ, sờn mép nhạt). Nét trắng hơi ngả xanh, 4 độ dày (viền, chi tiết, mảnh, tóc), nét đứt cho đường tâm và đường khuất. Vật che khuất theo thứ tự vẽ: fill màu giấy rồi mới stroke viền. Gạch chéo 45 độ cho mặt cắt. Mây và vùng mềm có gạch chéo mảnh. Bóng chỉ hiện khi vật rời tờ giấy. Màu duy nhất ngoài xanh trắng dùng đúng một lần (dấu đỏ).
- **Máy quay và khung dọc 9:16:** máy lướt trên tờ giấy như mắt đọc bản vẽ. Cỡ trung, vật khoảng 80 phần trăm chiều cao, có trời trống một bên để ghi chú. Khung dọc: vật ở nửa trên, bảng chi tiết ở nửa dưới, hoặc đẩy cận từng bộ phận. Di máy bằng scale và translate cả tờ; cận cảnh 2 lần cắt trên nhịp mạnh.
- **Chuyển động:** nét vẽ lên theo độ dài đường (stroke-dashoffset) với đầu bút sáng, đúng thứ tự phác: đường tâm, viền, chi tiết, gạch chéo, kích thước, bóng số, nhãn. Cơ cấu bước theo lưới như cơ cấu đồng hồ, bánh răng tiến từng răng. Chi tiết tách ra rồi về từng nhịp. Hỏng thì chậm dần, sụp xuống. Ease mượt, cắt cứng trên nhịp.
- **Chữ trên hình:** chữ viết tay (kiểu kiến trúc sư) cho nhãn, ghi chú, phụ đề; chữ kỹ thuật cho ô khung tên; script cho chữ ký. Chữ được viết lên từ trái sang phải. Phụ đề là ghi chú bản vẽ: hộp trong suốt viền đôi trắng, ô "NOTE / n", đặt vào khoảng trời trống chứ không cố định ở đáy. Dùng Be Vietnam Pro cho chữ có dấu.
- **Nước đi đặc trưng:**
  - Vẽ theo thứ tự phác: vật tự dựng từng lớp mỗi nhịp (giải thích cấu tạo).
  - Chú thích sống: kích thước đo bộ phận đang động, bóng số bay theo chi tiết (cơ chế hoạt động).
  - FIG. số làm chuyển cảnh: gạch "FIG. 2" viết lại "FIG. 3 IN OPERATION" (các giai đoạn, phiên bản).
  - Tách rời chi tiết rồi gom lại (cấu tạo, sửa chữa).
  - Dấu đóng đỏ lên khung tên (kết luận, phê duyệt).
- **Bẫy:**
  - Nét trắng sáng rực như HUD, 3D: phải là nét vẽ tay kỹ thuật, 2D, hơi mềm.
  - Không chừa chỗ trống cho ghi chú: hình dày, chữ chen nhau.
  - Nét trắng đều một độ dày: dùng 4 độ dày, tăng theo zoom chậm.
  - Dùng nhiều màu: chỉ xanh trắng và một dấu đóng.

Phỏng theo `styles/blueprint/STYLE.md` của lemomo-ai/lemo-opuscar (MIT).

*Ý tưởng gốc: MotionFly / lemo-opuscar (MIT), qua SlideFly.*

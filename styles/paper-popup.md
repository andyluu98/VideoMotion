# Sách pop-up giấy (thẻ giấy bật lên từ trang sách)

> Một cuốn sách pop-up mở trên bàn: trang kem có nếp gấp giữa, tấm bìa dựng làm phông, mọi vật là thẻ giấy phẳng viền trắng ngà bật dựng lên khi lật trang.

**Hợp:** kể chuyện, marketing, giải thích xã hội, bài giảng cho trẻ em, giới thiệu sản phẩm thân thiện.
**Không hợp:** báo cáo trang trọng, tài chính, sơ đồ kỹ thuật dày, sự kiện tang lễ.
**Cảm xúc:** vui tươi, thủ công, ấm áp, kể chuyện.

## Hình dung
Hai thế giới: trang sách thật (ấm, tự nhiên) và thế giới giấy (rực màu) đứng trên đó. Mỗi lần lật trang, đồi, cây, nhà nấm, mặt trời trên cán bật dựng từ mép đáy; lật đi thì gập xuống. Không có gì tròn xoe kiểu 3D: vật "có chiều sâu" chỉ là vài thẻ phẳng chồng nhau. Mặt vật chỉ vài nét: hai chấm mắt, một nét cười, má hồng.

## Bảng màu
```css
--page: #FBF1DA;    /* trang sách kem, nền */
--ink: #4A2E1B;     /* mực nâu sẫm: mọi nét, chữ. Không bao giờ đen tuyền */
--muted: #6B4A33;
--bord: #FFF8EA;    /* viền giấy trắng ngà quanh mọi thẻ */
--edge: #CDB98F;    /* mép bìa cứng be xám */
--accent: #A82A18;  /* chữ nhấn */
/* thế giới giấy: phẳng, bão hòa kiểu sách thiếu nhi, không neon */
--sky: #8CCBEA; --grass-l: #A8D56B; --grass: #6DB655; --leaf: #4FA94A;
--yellow: #FFC93C; --orange: #F59E0B; --red: #D9382B; --coral: #FF7A59;
--purple: #A35BD6; --blue: #2F6FB8; --teal: #2FB3A3; --green-label: #2A8C4F;
```
Màu rực thuộc về thế giới giấy; chữ và trang sách giữ tông ấm trầm. Một mặt trời mỗi hình là đủ.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">
```
- Tiêu đề và nhãn: Baloo 2 800, tròn mập, vui.
- Thân: Nunito 400 đến 600.
- Số trắng trong huy hiệu tròn màu.
- Cả hai font có bộ chữ tiếng Việt (đã kiểm Google Fonts ngày 16/10/2026).

## Bề mặt
Trang kem có nếp gấp giữa (bóng gáy sách), tấm bìa dựng làm phông đổi màu theo trang (trời, hồng, chàm đêm, vàng bơ, cam hoàng hôn). Thẻ nội dung là giấy trắng ngà bo 22px, có bóng theo hình cắt.

## Ngôn ngữ minh họa
- **Mỗi mảnh giấy làm đủ bốn lớp:** bóng nâu `#3C2810` alpha .16 lệch (8, 12); mép bìa be xám lệch xuống 3px; viền trắng ngà 13px bo góc; màu phẳng và nét mực 3,4px.
- Một lát liềm tối cứng thay cho bóng mềm. Mặt xoay là lật ngang, không xoay quanh trục đứng.
- Mảnh ghép nhiều hình cùng một thẻ thì vẽ viền và mép cho cả nhóm trước, mực sau cùng.
- Hình mẫu: mặt trời trên cán (12 cánh tròn, mặt cười), huy hiệu số tròn, thanh giấy ghi chú có huy hiệu bên trái, thẻ kéo (pull-tab) có núm tròn san hô, vật hai tư thế (cũ nét đứt, mới đầy đủ), chân gấp chữ V dưới thẻ, mảnh giấy màu vãi ở góc.

## Chữ ký chuyển động
- **Bật dựng từ mép đáy:** thẻ mọc lên bằng cách tăng chiều cao từ đường đáy (`rise` với gốc biến đổi ở đáy, hoặc `rise-wipe`), dừng gọn như giấy cứng; rời slide thì gập ngược về đáy.
- **Lật trang qua nếp gấp:** chuyển chương bằng `data-transition="wipe"` từ nếp giữa ra; phông bìa đổi màu theo `data-scene`.
- **Kéo thẻ:** ý ẩn, đáp án, "sau" nằm sau một thẻ kéo; cú bấm (`data-step`) làm dải giấy trượt `right` và lộ nội dung qua cửa sổ cắt.
- **Mặt trời trên cán đung đưa:** `sway` nhẹ quanh chân cán; giữa các trang nó là `data-morph="mat-troi"` mọc cao hoặc hạ thấp.
- **Giấy màu vãi:** confetti `drop` lác đác ở góc khi tới khoảnh khắc vui.
- Nhịp: vui, dứt khoát, có điểm dừng. Không co giãn kiểu đất sét, không nảy dai.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** mở sách, hai lớp đồi bật dựng, cây và nhà nấm mọc lên, mặt trời trên cán vươn cao, tên deck trên thanh giấy ghi chú.
- **Câu hỏi và đáp án:** thẻ kéo có mũi tên, khán giả đoán rồi cú bấm kéo lộ đáp án.
- **Hành trình:** hàng rào làm trục, mỗi cột rào một huy hiệu số, các thẻ bật lên lần lượt theo `data-stagger`.
- **Kết:** trang đêm phông chàm, mặt trời gập xuống, giấy màu vãi, lời cảm ơn.

## Nên tránh
Màu neon, gradient mượt, bóng mềm kiểu 3D, glow, phối cảnh hội tụ, viền đen, mực đen tuyền, vật tròn xoe có chiều sâu, nhân vật hay giao diện của game, sách có thật, chữ Hán giả, số liệu bịa, chữ dài trong hình.

## Họ hàng
`clay-3d` (vui tươi cho trẻ em nhưng là khối đất nặn mềm có chiều sâu), `cat-giay-do` (cũng giấy cắt nhưng phẳng một màu đỏ, chất lễ hội truyền thống), `crayon-book` (sách thiếu nhi tô sáp nét tay, dịu và chậm hơn).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/paper-popup.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** một phông giấy nhiều lớp dựng đứng trên trang sách: nhà nấm mũ đỏ chấm kem, cây tròn, cây thông, hàng rào, bảng gỗ, mặt trời trên cán, đồi xanh chồng lên nhau, con đường be uốn lượn. Nhân vật chính là một sinh vật bé xíu đội mũ lá, có cánh trong, đứng trên đường, cao khoảng 1/6 khung. Mọi thứ là thẻ giấy phẳng viền trắng ngà, mép bìa be, nét mực nâu, mặt chỉ hai chấm mắt và nét cười.
- **Chất liệu và ánh sáng:** mỗi thẻ là một SVG nhóm: bóng nâu alpha thấp lệch xuống, mép bìa be lệch 3px, viền trắng ngà dày (stroke trắng trước rồi fill), màu phẳng, nét mực nâu. Một lát liềm tối cứng thay cho bóng mềm. Phủ hạt giấy bằng một lớp noise tĩnh. Ánh sáng là một vầng ấm nhẹ từ trên, vignette ấm ở góc. Hoa và cỏ ở tiền cảnh đặt mờ (filter blur chỉ để tĩnh) để tạo cảm giác macro.
- **Máy quay và khung dọc 9:16:** góc ngang tầm nhân vật, cỡ trung. Chia khung thành 3 lớp sâu: tiền cảnh mờ ở đáy, nhân vật giữa, phông xa. Di máy bằng scale và translate từng lớp với tốc độ khác nhau (parallax). Ở khung dọc xếp phông cao hơn: mặt trời và đồi ở trên, nhà nấm giữa, đường và nhân vật dưới.
- **Chuyển động:** thẻ bật dựng từ mép đáy (scaleY từ gốc đáy, `back.out` nhẹ), lớp xa lên trước, lớp gần lên sau. Cây, hoa, mặt trời đung đưa vài phần trăm radian quanh gốc. Nhân vật đi bằng bước nấc, lật hướng bằng scaleX. Giấy cứng nên không co giãn dai.
- **Chữ trên hình:** bảng gỗ hoặc thanh giấy ghi chú có viền trắng ngà, chữ mực nâu đậm; phụ đề bubble giấy trắng ở đáy, chữ nâu viền dày. Phông Baloo 2 hoặc Be Vietnam Pro, đủ dấu tiếng Việt.
- **Nước đi đặc trưng:**
  - Mở sách: tấm phông dựng lên, các lớp bật lần lượt từ xa tới gần (bìa, giới thiệu).
  - Lật trang: thẻ cũ gập xuống, thẻ mới bật lên, phông đổi màu (chuyển chương, đổi bước).
  - Thẻ kéo: dải giấy trượt để lộ đáp án (hỏi rồi đáp, trước và sau).
  - Mặt trời trên cán mọc cao hoặc hạ thấp (mở và kết cảnh).
  - Giấy màu vãi ở góc (khoảnh khắc vui, thành công).
- **Bẫy:**
  - Vẽ vật tròn xoe có chiều sâu kiểu 3D: phá cảm giác giấy phẳng, chỉ chồng vài thẻ phẳng.
  - Bóng mềm hoặc glow: dùng bóng liềm cứng và bóng lệch theo hình cắt.
  - Xoay quanh trục đứng làm lộ lưng trống: dùng lật scaleX.
  - Neon hoặc gradient mượt: giữ màu phẳng bão hòa kiểu sách thiếu nhi.

Phỏng theo `styles/paper-popup/STYLE.md` của lemomo-ai/lemo-opuscar (MIT).

*Ý tưởng gốc: MotionFly / lemo-opuscar (MIT), qua SlideFly.*

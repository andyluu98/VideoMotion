# Hoạt hình giữa thế kỷ (phim lớp học thập niên 50, in lệch màu)

> Một tấm thẻ hướng dẫn in màu phẳng: nét mực nâu đen, mảng cam cháy, xanh ngọc, mù tạt in lệch khỏi nét vài pixel, bumerang và sao nổ bay quanh.

**Hợp:** hướng dẫn từng bước, tài liệu trợ giúp khách hàng, bài giảng nhẹ nhàng, thẻ quy tắc, danh sách việc cần làm, onboarding.
**Không hợp:** công nghệ tương lai, neon, báo cáo tài chính nghiêm, chủ đề u buồn.
**Cảm xúc:** hoài cổ, vui tươi, ấm áp, in lệch màu.

## Hình dung
Người xem như đang xem một đoạn phim giáo dục cũ chiếu trong lớp học: tờ giấy in ấm có vân, mỗi mảng màu là một lớp in lệch xuống phải 4 đến 7px khỏi nét mực, nên mép trên trái hở khe giấy, mép dưới phải thò vệt màu. Hình học thay chi tiết: hộp bo tròn, đĩa, bumerang, sao nổ, tia nắng. Một hình một ý, có huy hiệu số 1, 2, 3 như sách hướng dẫn máy móc.

## Bảng màu
```css
--paper: #F5EAD0;   /* giấy in, nền */
--deep: #EBD9B2;    /* giấy đậm hơn, dải sàn */
--cream: #FBF3DC;   /* thẻ, chữ trên nền ngọc */
--ink: #261D18;     /* nét mực nâu đen: viền, chữ, huy hiệu */
--orange: #E4682A;  /* cam cháy: vật chính, bullet, mặt trời */
--accent: #B2441A;  /* cam đậm cho chữ nhấn đủ tương phản */
--teal: #1F9C96; --teal-deep: #0F6B68;  /* mảng nền hình, bóng lệch của thẻ */
--mustard: #F2B63D; /* sao nổ, tia sáng, bóng lệch phụ */
--muted: #5A4A3E;
```
Ba màu cộng mực, không thêm sắc nào khác. Không neon, không đen tuyền, không trắng tinh. Chữ kem chỉ đặt trên nền ngọc, chữ mực đặt trên thẻ kem.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Be+Vietnam+Pro:wght@400;500;600;700&display=swap" rel="stylesheet">
```
- Tiêu đề, con số, nhãn trong hình: Alfa Slab One (chân vuông dày, đúng chất áp phích thập niên 50). Có tiếng Việt (đã kiểm).
- Thân và nhãn: Be Vietnam Pro 400 đến 700. Bản gốc ghi rõ đã thay Jost bằng Be Vietnam Pro để có tiếng Việt.

## Bề mặt
Giấy in ấm có vân răng giấy và vệt chổi rất nhẹ, viền tối ấm ở bốn góc. Có thể thêm tia nắng tỏa và chấm bi mờ làm nền.
```css
background: radial-gradient(130% 100% at 50% 40%, #F5EAD0 60%, #EBD9B2);
```

## Ngôn ngữ minh họa
- **Lệch đăng là chữ ký:** vẽ mảng màu trước, dịch (6, 5), rồi vẽ nét mực cùng đường dẫn lên trên, không tô. Mảng nền lớn lệch 7 đến 8px, vật nhỏ lệch 3 đến 4px. Nét mực khép kín sạch bong và màu khớp tuyệt đối là mất chất.
- Nét: 4px đường bao, 2,5px chi tiết, 3,5px mũi tên cong nét đứt `10 8`; đầu và góc nét tròn.
- Hình mẫu: bumerang (bóng dáng của style), huy hiệu số tròn, thẻ nổi bóng lệch ngọc hoặc mù tạt, sao 4 cánh cho lấp lánh, sao nổ 14 đến 16 cánh cho kết quả, mũi tên cong kiểu sách hướng dẫn.
- Vẽ đồ dùng (máy chiếu, màn, thẻ, hình khối), không vẽ người, không nhân vật của hãng phim nào.

## Chữ ký chuyển động
- **Màu trượt vào khớp nét:** nét mực vẽ trước (`draw`), sau đó mảng màu trượt tới chỗ lệch đăng của nó (`fade` kèm dịch ngắn), như lớp in thứ hai vừa chạy qua máy.
- **Hoạt hình hạn chế:** vật đổi tư thế bằng cách thay hình tức thì, giữ yên vài nhịp rồi đổi tiếp (chuyển động có bậc, kiểu "vẽ trên hai khung"), không trôi mượt.
- **Bumerang bay vòng:** bumerang bay theo một cung rộng (`animateMotion`) vừa bay vừa xoay, rồi đậu đúng chỗ gọi tên ý chính.
- **Tia nắng quay chậm:** nền tia nắng tỏa `data-loop="spin"` với `data-loop-dur` dài, gần như không nhận ra.
- **Huy hiệu số bật theo thứ tự:** 1, 2, 3 bật bằng `pop` theo cú bấm, đường dẫn từ huy hiệu tới vật `draw` ngay sau.
- **Sao lấp lánh:** sao 4 cánh `data-loop="pulse"` ở nơi chuyển biến.
- Nhịp: vui, hơi giật, như phim hoạt hình tiết kiệm khung hình.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** tia nắng mù tạt tỏa sau tên deck, bumerang bay ngang khung rồi đậu cạnh chữ, sao nổ bật ở góc.
- **Hướng dẫn từng bước:** một vật lớn ở giữa, ba huy hiệu số lần lượt bật ra nối vào từng bộ phận.
- **Nên và không nên:** hai thẻ nổi bóng lệch, một bóng ngọc, một bóng mù tạt, dấu tích và dấu chéo in lệch.
- **Kết:** sao nổ lớn mang lời cảm ơn, mảng màu trượt vào khớp nét lần cuối.

## Nên tránh
Màu ngoài bảng, gradient trên vật, bóng mờ, 3D, glow, neon; nét và màu khớp tuyệt đối; nhân vật của hãng phim, logo, chữ ký có thật; số liệu bịa (dùng A, B, 1, 2, 3 hoặc nhãn VÍ DỤ); câu dài trong hình.

## Họ hàng
`retro-windows` (cũng hoài cổ vui, nhưng là cửa sổ máy tính chứ không phải giấy in), `pastel-geometry` (hình khối phấn nhẹ, không có nét mực và lệch đăng), `risograph` (cũng in lệch màu chồng lớp, nhưng rực rỡ indie hơn, không phải phim lớp học).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/midcentury-toon.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** một cảnh hướng dẫn: nền vàng mù tạt có tia nắng xòe, dải sàn vàng đậm, một đường chân trời đứt đoạn. Ở giữa là vòng tròn kem lớn, hai cánh cửa gỗ mở ra hai bên, bên trong là sản phẩm (đĩa tròn xanh ngọc). Bên phải là người thuyết trình hình học: đầu hình trứng, mũi nhô ra khỏi đường viền mặt, áo cam, quần xanh chàm, tay đeo găng bốn ngón, chỉ tay vào sản phẩm. Người cao khoảng 2/3 khung.
- **Chất liệu và ánh sáng:** mỗi mảng màu là một lớp riêng lệch vài px xuống phải so với nét mực nâu đen, nét mảnh có chỗ đứt (SVG path, dasharray lệch, hoặc stroke riêng). Đổ bóng bằng một bản sao hình dịch xuống phải ở sắc giấy. Tia sáng là khoảng 30 nêm bán trong suốt; điểm xuyết sao bốn cánh. Hạt giấy nhẹ, vignette ấm. Không gradient, không neon.
- **Máy quay và khung dọc 9:16:** máy là giá đứng, không rung. Cỡ trung, chủ thể chiếm hơn 1/3 chiều cao, tránh dải phụ đề ở đáy. Khung dọc: tiêu đề ở trên, vòng tròn sản phẩm giữa, người thuyết trình nhỏ hơn bên cạnh hoặc dưới. Đẩy chậm vài phần trăm; chuyển bước bằng iris tròn xuyên qua huy hiệu số.
- **Chuyển động:** dáng, bàn tay và độ lệch màu đổi 12 fps (twos); máy, iris, mũi tên mượt 24 fps. Thân người đứng im, chỉ tay, mắt, miệng cử động; mỗi cử chỉ có chuẩn bị, hành động nhanh ease-out, rồi lắng, rơi đúng nhịp. Huy hiệu, nhãn nảy vào bằng `back.out` mạnh khoảng 0.25 giây.
- **Chữ trên hình:** tiêu đề chữ script nghiêng đậm đặt trên bản màu lệch; dòng phụ bằng slab serif đậm; phụ đề là thẻ giấy bo tròn viền mực mảnh với hai sao nhỏ hai đầu, nằm dưới. Huy hiệu bước là đĩa mực với số kem và dòng "BƯỚC n / N". Phông Be Vietnam Pro cho mọi chữ có dấu.
- **Nước đi đặc trưng:**
  - Iris qua huy hiệu số: con số là cánh cửa sang bước sau (hướng dẫn nhiều bước).
  - Thân đứng im, tay làm việc: mỗi bước một động tác tay đúng nhịp (thao tác lắp, bấm, chỉnh).
  - Vòng tròn cận cảnh có đường dẫn: thông số rơi vào trong vòng (liều, giá trị, nút bấm).
  - Chia khung hai khối màu: đúng và sai, trước và sau (quy tắc an toàn, nâng cấp).
  - Đứng yên 3 giây ở khung cuối (tóm tắt, kêu gọi).
- **Bẫy:**
  - Fill khít với nét viền: mất cảm giác in lệch, phải luôn lệch vài px.
  - Gradient hoặc bóng mềm: chỉ dùng mảng phẳng và bóng là bản sao hình.
  - Cả cơ thể cử động liên tục: kiểu phim giữ thân, chỉ tay và mặt động.
  - Màu neon hoặc đen tuyền: dùng nâu đen ấm và màu bù hoài cổ.

Phỏng theo `styles/midcentury-toon/STYLE.md` của lemomo-ai/lemo-opuscar (MIT).

*Ý tưởng gốc: MotionFly / lemo-opuscar (MIT), qua SlideFly.*

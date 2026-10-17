# Hoạt hình viễn tưởng (sitcom khoa học viễn tưởng viền dày)

> Đĩa bay, cổng không gian, hành tinh có vành được đối xử như đồ gia dụng: viền tím đen dày, màu phẳng, mỗi slide là một thế giới màu mới.

**Hợp:** bài thuyết trình hài hước, thương hiệu công nghệ, video ngắn, deck giải thích ý tưởng nhẹ nhàng, ra mắt tính năng kiểu tếu.
**Không hợp:** báo cáo trang trọng, chủ đề nhạy cảm, văn hóa truyền thống.
**Cảm xúc:** vui nhộn, viền dày, màu phẳng, viễn tưởng.

## Hình dung
Một tập phim hoạt hình truyền hình cho người lớn: chuyện nhỏ nhặt (gửi một tấm slide, sửa một lỗi) được làm bằng phương tiện khổng lồ (đĩa bay, tia kéo, cổng không gian). Nhân vật chính là chính tấm slide có mắt trắng to, đồng tử bé tí, tay chân sợi mì. Mỗi slide là một hành tinh khác, đổi cả màu nền. Chỉ cổng không gian là thứ phát sáng.

## Bảng màu
```css
--ink: #2a1d3a;     /* viền tím đen, mắt, đồng tử: thứ giữ hình trên mọi nền */
--paper: #fff6c9;   /* thân slide, sao */
--fg: #241a33; --muted: #4a3a62;
--accent: #912a07;  /* chữ nhấn trên nền sáng */
/* mỗi slide một thế giới (--bg): xanh xô thơm #b6d7a9 (mở màn), bơ #f4dc82, tím #3b2a78,
   bạc hà #a8e0cf, san hô #f4a58f, đào #f9c6a5, aqua #9fd4d8, cực tím #2b1c5e, be #e8dcc2 (kết)
   trên nền tối: chữ #fff3d6, nhấn #ffb347 */
/* đồ vật: vàng đất #f4b942 bóng #d98d1e, hồng #f4a3c4, kính #bfe9f2, tím đồ vật #8f6bb3,
   san hô #ef8a6b, bạc hà #7ad3c4; cổng: #b25cff #5a1fb0 #efd3ff #fff3ff */
```
Màu tím hồng của cổng chỉ dành cho cổng. Bóng đổ là một mảng mực 20%, đúng một mảng mỗi hình, ở phía xa nguồn sáng.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Be+Vietnam+Pro:wght@400;500;600;700&family=VT323&display=swap" rel="stylesheet">
```
- Tiêu đề, nhãn: Baloo 2 800. Có tiếng Việt (đã kiểm).
- Thân: Be Vietnam Pro 400 đến 600.
- Dòng lệnh terminal: VT323 màu bạc hà trên khối mực. Có tiếng Việt (đã kiểm).

## Bề mặt
Nền phẳng một màu của thế giới, đáy là sàn phòng thí nghiệm lát ô có đường kẻ mực. Trang trí thưa: mặt trăng có miệng hố, hành tinh có vành, sao bốn cánh.
```css
background: var(--bg);  /* phẳng, không chuyển sắc; đổi theo từng slide */
/* sàn: dải đáy kẻ ô bằng nét màu --floor-line (#2a1d3a, trên nền tối đổi sang #8d78d6) */
```

## Ngôn ngữ minh họa
- Viền mực dày đều: 6 cho vật chính, 4,5 cho chi tiết, 3,5 cho nét nhỏ; đầu và góc nét tròn.
- Màu phẳng, mỗi hình một mảng bóng cứng. Không gradient, không 3D, không phối cảnh.
- **Mắt** tròn trắng viền mực, đồng tử 8 đến 10px nhìn lệch lên; mày là một cung. Bốn nét biểu cảm: trợn mắt mở miệng là bất ngờ, cười nhỏ là ổn, miệng phẳng là trung tính, mày cong và giọt mồ hôi là quá tải.
- Hình mẫu: đĩa bay (chân tím, vòm kính, người ngoài hành tinh hồng, năm đèn kem), cổng không gian (viền gợn, lòng tím đậm, tay xoáy, lõi sáng), slide có mặt, thẻ terminal, đường bay chấm tròn thưa có mũi tên.
- Tự bịa nhân vật và đạo cụ. Mỗi slide một nhân vật chính, phần còn lại là chấm phá.

## Chữ ký chuyển động
- **Cổng mở:** cổng `zoom` từ một điểm, tay xoáy bên trong `data-loop="spin"`; vật đi qua cổng là sang ý mới. Đây là thứ duy nhất được "phát sáng".
- **Nhảy qua thế giới:** chuyển slide bằng cổng: cổng nở to phủ khung, slide sau hiện ra với màu nền mới (`data-transition="zoom"`).
- **Đĩa bay lướt theo đường chấm:** đĩa đi theo tuyến (`animateMotion`), đến nơi thì chao nhẹ (`data-loop="sway"` trên lớp con).
- **Tia kéo hút lên:** chùm tia hình thang hiện (`wipe` từ trên xuống), vật bên dưới `rise` lên theo tia.
- **Nhịp hài:** đứng yên một nhịp, rồi biểu cảm đổi tức thì (mắt trợn, giọt mồ hôi `pop`). Khoảng lặng trước cú đổi là chỗ gây cười.
- **Terminal gõ lệnh:** dòng `> ...` hiện bằng `wipe`, con trỏ khối `data-loop="blink"`.
- Nhịp: nảy hài, dừng gắt, cắt nhanh kiểu sitcom.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** đĩa bay lướt vào, tia kéo thả xuống một tấm slide có mặt đang ngơ ngác; tên deck nằm cạnh.
- **Vấn đề:** slide có mặt toát mồ hôi dưới chồng chữ giả cao ngất, mày cong quá tải.
- **Giải pháp:** cổng mở, slide chui qua, sang thế giới màu mới với gương mặt cười.
- **Kết:** đĩa bay chở lời cảm ơn rời khung theo đường chấm, sao bốn cánh lóe.

## Nên tránh
Nhân vật, hình bóng, tổ hợp màu, câu cửa miệng, khẩu súng cổng của phim có thật; bộ ba xanh chanh chói, giọt nhầy chảy và chữ bong bóng lượn sóng đi cùng nhau; gradient, bóng mờ, glow ngoài cổng; màu tím cổng cho vật khác; hình quá đông; số liệu bịa.

## Họ hàng
`game-show` (cũng viền dày màu kẹo, đổi màu mỗi slide, nhưng là trường quay thi đấu và có bóng đổ lệch), `rubber-hose` (đồ vật có mặt, tay chân ống mì, nhưng đen trắng thập niên 30), `neon-cyber` (công nghệ tương lai thật sự nghiêm túc, nền tối, không có nhân vật).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/scifi-toon.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** Phòng thí nghiệm một màu xô thơm, tường có bảng đen phấn viết công thức giả, kệ bình thủy tinh màu bên phải, máy pha cà phê có mặt buồn bên trái, đồng hồ treo tròn, sàn lát ô. Hai nhân vật phản ứng ngược nhau: một nhà khoa học cao, trọc, kính trên trán, áo choàng xanh, dép hồng, mắt lờ đờ, tay cầm điều khiển có nút đỏ; một đứa nhỏ đội mũ bảo hiểm cam, áo tím, mắt trợn, đồng tử bé tí, giọt mồ hôi, đứng sát bàn. Giữa họ là một cổng không gian dựng đứng. Hai nhân vật cao khoảng 45 đến 60% khung, đủ đọc mặt.
- **Chất liệu và ánh sáng:** Viền tím đen `#2a1d3a` dày đều (6 cho vật chính, 4,5 cho chi tiết), đầu tròn, độ dày giữ nguyên khi phóng to (dùng `vector-effect: non-scaling-stroke`). Màu phẳng, mỗi hình một mảng bóng cứng ở phía xa nguồn sáng, không gradient. Thế giới này một bảng màu, nền phẳng. Chỉ cổng phát sáng: viền gợn, lòng xoáy nhiều lớp, lõi nhạt, vài tia lấp lánh và hai vòng trong mờ phẳng quanh cổng; không giọt nhầy. Viền boil bằng cách đổi qua ba bản path lệch nhẹ ở 12 fps.
- **Máy quay và khung dọc 9:16:** Cỡ trung hai người (two-shot), góc ngang, mặt hướng ra. Ở dọc, xếp hai nhân vật chồng theo chiều sâu: người cao ở sau, đứa nhỏ ở trước, cổng ở giữa, tiêu đề lớn ở trên; hoặc cắt cận từng gương mặt. Mỗi hình lạ được theo bằng một cận cảnh phản ứng. Di máy chỉ là push chậm trên hai người hoặc rush zoom vào cổng rồi quét xoáy sang thế giới mới.
- **Chuyển động:** Nhân vật tư thế giữ lâu, thay đổi nhỏ (đồng tử trượt, nuốt nước bọt, giọt mồ hôi hiện), diễn 12 fps theo nấc; camera, xoáy cổng, vật bay mượt 24 fps. Dừng một nhịp rồi biểu cảm đổi tức thì: khoảng lặng là chỗ gây cười. Rơi xuống có squash tắt dần, qua cổng thì kéo dãn về tâm. Cổng mở với `back.out` nhẹ, không nảy mạnh.
- **Chữ trên hình:** Tựa chữ dày tròn màu kem có viền tím đen và bóng lệch, đặt trên vòng quỹ đạo có sao bốn cánh; chữ Baloo 2 đậm cho chữ không dấu, chữ có dấu dùng Be Vietnam Pro 800, đủ dấu Việt, không dùng chữ bong bóng lượn sóng. Dòng lệnh terminal VT323 màu bạc hà trên khối mực. Phụ đề chữ trắng viền đen dày ở đáy cùng nhãn người nói màu theo nhân vật.
- **Nước đi đặc trưng:**
  - Hai nhân vật phản ứng ngược nhau cạnh cổng: hợp so sánh, đối thoại, người từng trải và người mới.
  - Cận cảnh phản ứng sau mỗi hình phi lý: hợp tiết lộ, kết quả buồn cười.
  - Rush zoom vào cổng rồi sang thế giới đổi màu nền: hợp chuyển ý, đổi phiên bản.
  - Công cụ khổng lồ làm việc vặt (bảng công thức cho tách cà phê): hợp ví von, tính năng.
  - Im lặng một nhịp rồi đổi biểu cảm: hợp giá, điều khoản, điểm đảo chiều.
- **Bẫy:** Viền co giãn theo scale khi cận cảnh làm mất độ dày đều. Tô gradient hay glow ngoài cổng phá luật phẳng. Dùng màu cổng cho vật khác thì mất ý duy nhất phát sáng. Nhồi quá nhiều vật vào phòng làm mặt hai nhân vật bị che; kiểm tra mặt và thân trên luôn nhìn thấy sau đồ đạc.

Phỏng theo `styles/scifi-toon/STYLE.md` của lemomo-ai/lemo-opuscar (MIT).

*Ý tưởng gốc: MotionFly / lemo-opuscar (MIT), qua SlideFly.*

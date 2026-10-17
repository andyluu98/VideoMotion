# Đồ chơi lắp ghép (thế giới gạch nhựa có núm)

> Mọi thứ được lắp từ những viên gạch nhựa cứng có núm tròn: ý tưởng hiện ra bằng cách xếp chồng, tách ra và lắp lại.

**Hợp:** đồ chơi trẻ em, giáo dục, lắp ráp sản phẩm, khởi nghiệp, chủ đề vũ trụ và công nghệ, giải thích "từng phần ghép thành tổng thể".
**Không hợp:** tang lễ, chủ đề nhạy cảm, tài chính trang trọng, văn hóa truyền thống.
**Cảm xúc:** vui nhộn, tươi sáng, thủ công, tuổi thơ.

## Hình dung
Một mô hình gạch vừa lắp xong trên mặt bàn sáng, nhìn thẳng từ phía trước, phòng phía sau nhạt và nhòe. Nhựa ABS bóng với một dải sáng gọn của đèn hộp trên mặt trên, vệt tối ở chỗ hai viên chạm nhau. Người xem đếm được số viên, số hàng: cấu trúc nằm ngay trong hình.

## Bảng màu
```css
--bg: #e3ebf2;      /* phòng sáng, nhòe */
--red: #c91a09;     /* gạch đỏ */
--blue: #0055bf;    /* gạch xanh: màu nhấn, nền thẻ */
--yellow: #f2cd37;  /* gạch vàng */
--green: #237841;   /* gạch xanh lá, tấm đế */
--black: #1b2a34;   /* chữ, gạch đen, viền mảnh */
--muted: #46586a;
/* gạch trắng #f2f2ee; gạch trong suốt cho lửa, ánh sáng: #f26a1b, #f59a22, #f9c923 (mờ 0,9) */
```
Chỉ sáu màu gạch cơ bản cộng ba màu gạch trong suốt. Mỗi slide một màu dẫn dắt (thường là xanh dương cho thẻ), các màu khác là gạch rời trang trí. Lửa và ánh sáng cũng là gạch, không phải gradient mềm.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Nunito:wght@500;600;700;800&display=swap" rel="stylesheet">
```
- Tiêu đề: Baloo 2 800, tròn mập như núm gạch. Có tiếng Việt (đã kiểm).
- Thân: Nunito 500 đến 600. Có tiếng Việt.
- Nhãn trong hình: Nunito 800, IN HOA, giãn 0,1em; số trong đồng tiền Baloo 2 800 trên đĩa trắng.

## Bề mặt
Nền xanh xám rất nhạt, vài vầng sáng trắng mờ như đèn studio, mép dưới là tấm đế xanh lá có núm đều (có thể kéo dài thành đường ray cho dòng thời gian).
```css
background: radial-gradient(70% 60% at 30% 20%, rgba(255,255,255,.55), transparent 70%), #e3ebf2;
```

## Ngôn ngữ minh họa
- **Quy cách một viên:** bước núm 80, thân cao 96, núm rộng 48 cao 20, bo 7. Hai viên chồng nhau cách đúng 96, viên trên che núm viên dưới.
- Mỗi viên: màu đặc, dải sáng trắng 30% ở mặt trên, mép sáng trái, mép tối phải, dải tối 20% ở đáy, viền mảnh `#1b2a34` 22%.
- Gạch dốc làm mũi tên lửa và mái; cửa sổ tròn kính xanh đậm; mặt rô-bốt là hai chấm đen và một cung cười.
- Bóng chạm bàn là elip dẹt đen 14% dưới chân mô hình. Đồng tiền số trắng cạnh viên gạch, không đè lên núm.
- Nhìn thẳng, phẳng có độ bóng: không 3D thật, không isometric. Gạch không uốn, không co giãn, không lệch bước núm.

## Chữ ký chuyển động
- **Lắp vào núm:** từng viên `drop` từ trên xuống, chạm là khựng một nhịp nhỏ cứng (nảy rất ngắn), xếp từ dưới lên (`data-stagger="110"`). Đây là động tác gốc của cả deck.
- **Tháp mọc:** cột gạch cao thêm từng viên theo cú bấm (`data-step`), hợp con số tăng trưởng: mỗi viên một mốc, không co giãn thanh.
- **Tháo ra, lắp lại:** cùng các viên gạch ở slide trước bay về chỗ mới ở slide sau thành mô hình khác (`data-morph` trên từng viên, đặt tên `b1`, `b2`...).
- **Gạch trượt ngang:** thẻ, khối chữ vào bằng `left` / `right` thẳng tắp, như đẩy gạch trên mặt bàn.
- **Tên lửa cất cánh:** tên lửa `rise` lên khỏi bệ, ngọn lửa gạch trong suốt `data-loop="pulse"`.
- Nhịp: tách tách, đều, mỗi viên một tiếng "cạch"; không mềm dẻo, không đàn hồi kiểu cao su.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** gạch rời rơi xuống tấm đế, lắp thành tên lửa cạnh tên deck; ngọn lửa bập bùng.
- **Từng phần ghép thành tổng thể:** ba khối màu (mỗi khối một thành phần) trượt vào, khớp nhau thành một bức tường.
- **Tăng trưởng:** ba cột gạch cao thấp khác nhau, số viên đúng bằng số liệu có nguồn, không bịa.
- **Kết:** rô-bốt gạch hoàn thiện, đồng tiền số cuối cùng bật lên trên đầu.

## Nên tránh
Màu ngoài bảng gạch, gradient, bóng mềm, ánh phát quang, 3D hay isometric; tên, logo, người nhựa của thương hiệu thật; in chữ lên núm; gạch bị uốn, xoay méo, lệch bước núm; số liệu bịa.

## Họ hàng
`clay-3d` (khối đất sét mềm, bo tròn, biến dạng được; ở đây mọi thứ cứng và có núm), `iso-infographic` (khối lập phương nhìn xéo, tông phẳng, giải thích hệ thống; ở đây nhìn thẳng và đồ chơi hơn), `paper-popup` (cũng là "dựng mô hình" nhưng bằng giấy gấp mở ra).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/brick-toy.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** đồ chơi lắp ghép đặt trên bàn thật, chụp macro. Ảnh có một tên lửa xếp từ gạch đỏ và trắng, mũi nhọn, cánh đỏ, ô cửa tròn có phi công nhỏ, lửa đẩy cũng là các viên gạch vàng cam. Đằng sau mờ là đồ vật thật (ấm trà, tách) thành phong cảnh, phía trước là những khối gạch trắng có núm. Nhân vật dựng từ gạch, nhìn thẳng, chiếm khoảng 1/2 chiều cao khung.
- **Chất liệu và ánh sáng:** mỗi gạch là hình chữ nhật bo góc trong SVG, fill phẳng, một vệt sáng chữ nhật cứng ở cạnh trên (highlight hộp đèn), một dải tối ở cạnh dưới, núm tròn trên mặt. Chỗ tiếp xúc giữa các viên có bóng tối mỏng (giả ambient occlusion). Nền: gradient xanh lạnh nhạt, mờ dần; vật thật phía sau vẽ đơn giản, blur chỉ để tĩnh. Màu trắng giữ lạnh nhẹ để không ngả kem. Lửa dựng từ gạch trong suốt cam vàng, xếp lại mỗi nhịp.
- **Máy quay và khung dọc 9:16:** góc thấp ngang đồ chơi, cỡ trung, nhân vật ở giữa, nền mờ hai bên. Khung dọc hợp tên lửa và tháp gạch đứng. Máy trượt mượt bằng scale và translate; lớp tiền cảnh mờ đặt thấp ở mép đáy, không che chủ thể.
- **Chuyển động:** gạch và nhân vật bước nấc 12 fps (twos); máy, lửa, vật bay mượt 24 fps. Gạch bay vào theo cung rồi chạm lại với một nhún rất nhỏ (vài frame). Tư thế lớn, giữ vài hình. Tay chân xoay tại khớp, gạch không co giãn.
- **Chữ trên hình:** viên thuốc tối bo tròn ở đáy kèm biểu tượng viên gạch nhỏ, chữ trắng. Tiêu đề hiện nấc như đặt một viên. Phông Fredoka hoặc Be Vietnam Pro, đủ dấu tiếng Việt, không in chữ trên núm.
- **Nước đi đặc trưng:**
  - Lắp ghép: các viên bay vào và khớp lại (ra mắt sản phẩm, quy trình dựng).
  - Vỡ mà không hại: tháp đổ, mảnh thành thứ mới (xoay hướng, tái chế).
  - Đồ thật làm phong cảnh: rack focus từ vật thật sang gạch (so sánh quy mô).
  - Phóng ra xa để lộ cả thế giới là đồ chơi trên bàn (kết, nhìn lại).
- **Bẫy:**
  - Gạch phẳng không có highlight chữ nhật và bóng tiếp xúc: trông dán lên.
  - Co giãn hoặc uốn cong gạch: mọi thứ cứng, chỉ xoay tại khớp.
  - Lửa dạng gradient mềm hoặc particle: phải là gạch rời.
  - Ánh vàng ấm làm gạch trắng ngả cam: giữ nền và tông lạnh.

Phỏng theo `styles/brick-toy/STYLE.md` của lemomo-ai/lemo-opuscar (MIT).

*Ý tưởng gốc: MotionFly / lemo-opuscar (MIT), qua SlideFly.*

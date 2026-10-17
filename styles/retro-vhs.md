# Retro VHS (băng video gia đình cuối thập niên 80)

> Hình hơi nhòe, lệch kênh đỏ xanh, sọc nhiễu chạy ngang, vệt tracking ở đáy, chữ khối đơn sắc của đầu máy (PLAY, ngày giờ), màu ấm bão hòa trong viền tivi ống bo góc.

**Hợp:** hoài niệm tuổi thơ, video kỷ niệm gia đình, kỷ yếu, mở màn sự kiện retro, trailer hoài cổ, nội dung về thập niên 80 và 90.
**Không hợp:** báo cáo số liệu dày, tài chính trang trọng, nội dung y tế, thương hiệu cần sạch và hiện đại.
**Cảm xúc:** hoài niệm, ấm áp, mong manh, ký ức.

## Hình dung
Một buổi chiều chủ nhật, cả nhà quây quanh tivi ống xem lại cuốn băng quay hồi nhỏ. Hình hơi nhòe và ngả màu, mép chữ rung nhẹ. Thỉnh thoảng một sọc nhiễu quét qua, dưới đáy băng bị xê dịch như ai chạm vào nút chỉnh. Góc màn hiện chữ trắng PLAY và dòng ngày tháng màu cam, nhắc rằng đây là một khoảnh khắc đã qua thật rồi.

## Bảng màu
```css
--bg: #0A0710;        /* màn tắt, gần đen có ánh tím */
--ink: #F4ECD8;       /* trắng ngà: chữ OSD */
--sky-top: #3B1F6E;   /* tím chạng vạng */
--sky-pink: #C2307C;  /* hồng cháy */
--sun-orange: #FF7A3D;/* cam hoàng hôn */
--sun-gold: #FFC76A;  /* vàng chân trời */
--vhs-red: #FF3B4E;   /* bóng lệch kênh đỏ */
--vhs-cyan: #27E0E8;  /* bóng lệch kênh xanh */
--osd-amber: #FF9A2E; /* ngày giờ của máy quay */
```
- Màu bão hòa ấm là chủ đạo. Đỏ và xanh lơ chỉ xuất hiện như bóng lệch kênh ở mép chữ và mép hình, không làm mảng màu.
- Đen chỉ dùng cho viền tivi và bóng người; tránh đen thuần trong ảnh.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=VT323&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
```
- Chữ OSD và tiêu đề: VT323 400 (có tiếng Việt), chữ khối đơn sắc như bộ tạo ký tự của đầu máy. Trắng kèm bóng đỏ và xanh lệch 3px, giãn 0,03em.
- Ngày giờ: VT323 màu cam `--osd-amber`, bóng đỏ xanh mảnh hơn.
- Thân và chú thích dài: Space Mono 400 và 700 (có tiếng Việt), dùng ít.

## Bề mặt
Hình đặt sau lớp nhòe nhẹ (blur 1px, tĩnh) và lớp sọc quét ngang cách đều 4px. Hai bản sao mờ của hình lệch sang trái đỏ và sang phải xanh vài px. Viền tối bo góc lớn như màn hình cong, kèm một quầng sáng mờ ở góc trên trái.
```css
#scan { background: repeating-linear-gradient(to bottom, rgba(0,0,0,.22) 0 2px, transparent 2px 4px); }
#tube { border-radius: 120px; box-shadow: 0 0 0 260px #040406, inset 0 0 150px 50px rgba(0,0,0,.78); }
```

## Ngôn ngữ minh họa
- **Cảnh đời thường nhìn qua ống kính cầm tay:** bãi biển lúc hoàng hôn, sân nhà, bữa tiệc sinh nhật. Hình đơn giản, phẳng, bóng người đen, cây cọ, mặt trời nửa chìm.
- **Lệch kênh:** nhân ba lớp hình, hai lớp phủ chỉ giữ kênh đỏ hoặc kênh xanh (bộ lọc tĩnh), lệch ngược chiều nhau.
- **Sọc nhiễu:** thanh ngang mảnh, độ đậm khác nhau, đặt ở vị trí tính sẵn; một dải sáng rộng mờ chạy dọc màn.
- **Vệt tracking đáy:** dải xám khoảng 70px ở đáy, hình bên trong bị xê ngang, rải gạch trắng ngắn.
- **Chữ OSD:** PLAY với tam giác (vẽ bằng CSS), mốc đếm giờ, ngày tháng ở góc dưới, đều đặt trong vùng an toàn cách mép 7%.

## Chữ ký chuyển động
- **Tua nhanh có sọc:** đầu cảnh hiện chữ `>> FF`, hàng chục sọc nhiễu lóe lên rồi tắt, khung hình giật dọc, chấm dứt khi chữ PLAY hiện.
- **Giật khung:** vài lần hình lệch 2 tới 6px rồi trở lại, đổi cứng không nội suy (`duration: 0`), thời điểm tính sẵn.
- **Chữ gõ từng ký tự:** mỗi ký tự hiện cách nhau khoảng 0,06 giây, con trỏ khối nhấp nháy rồi tắt.
- **Nhiễu lóe khi chuyển cảnh:** toàn màn trắng sọc 0,3 giây rồi cảnh mới hiện; vệt tracking trượt xuống đáy.
- **Vệt tracking xê dịch:** bản sao ở đáy nhảy ngang vài nấc rồi dừng.
- Nhịp: không đều, hơi lười, có chỗ khựng như băng cũ.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** nhiễu lóe, chữ PLAY hiện, tiêu đề gõ ra từng ký tự trên cảnh hoàng hôn.
- **Hồi tưởng:** chữ `<< REW` rồi nhiễu, hình đổi sang năm cũ, ngày tháng đổi theo.
- **Con số:** bộ đếm giờ góc phải chạy tới mốc quan trọng.
- **Kết:** chữ `STOP`, hình co về một vạch ngang rồi tắt hẳn.

## Nên tránh
Hình quá sắc nét, nhiễu phủ che hết chữ, màu pastel nhạt, gradient hiện đại bóng bẩy, dùng quá nhiều màu ngoài bộ ấm, chữ có chân, nhiễu ngẫu nhiên không tính sẵn, lệch kênh quá mạnh làm chữ khó đọc.

## Họ hàng
`ascii-crt` (cũng màn hình cũ nhưng là chữ ký tự và nền đen), `cel-anime-80s` (cùng gu thập niên 80, hoàng hôn neon nhưng nét hoạt hình), `y2k-chrome` (hoài niệm công nghệ nhưng sáng bóng, kim loại).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/retro-vhs.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** Một cảnh gia đình quay tay: bãi biển lúc hoàng hôn, mặt trời nửa chìm, vệt nắng bậc thang trên mặt biển, cây cọ ở trái. Ba bóng người (hai người lớn và một đứa trẻ) nắm tay đứng trên cát về phía phải khung, mỗi người cao khoảng 1/6 khung, có bóng đổ dài. Nhân vật phải có mặt trong cảnh.
- **Chất liệu và ánh sáng:** Trời gradient tím, hồng, cam, vàng. Biển chàm sẫm, cát nâu đỏ có viền sáng. Mọi hình phẳng, bóng người gần đen, một nguồn sáng duy nhất ở chân trời. Nhòe 1px tĩnh, hai lớp lệch kênh độ đậm 30%, sọc quét 4px, viền tivi ống. Chỉ tween transform, opacity, màu, visibility.
- **Máy quay và khung dọc 9:16:** Ngang tầm mắt, cỡ rộng, hơi lắc tay. Giật khung bằng đổi cứng vài px, không lia mượt. Khung dọc: trời chiếm nửa trên để chữ OSD và tiêu đề, bóng người ở giữa dưới, mặt trời lệch trục. Đáy chừa cho phụ đề và vệt tracking.
- **Chuyển động:** Cứng, bậc thang: `steps()` và `duration: 0`. Nhiễu lóe theo vị trí tính sẵn, giật khung dừng trước khi cảnh đứng yên. Không ease mượt cho nhiễu.
- **Chữ trên hình:** OSD VT323 trắng, bóng đỏ xanh: PLAY và tam giác ở trái trên, mốc giờ ở phải trên, ngày tháng cam ở góc dưới. Tiêu đề gõ từng ký tự. Phụ đề là thanh đen mờ (khoảng 78%) chữ ngà VT323, không viền, ngay trên vệt tracking. Phải đủ dấu tiếng Việt.
- **Nước đi đặc trưng:**
  - Tua nhanh `>> FF` với sọc nhiễu lóe để mở cảnh hoặc nhảy thời gian.
  - Chữ gõ từng ký tự kèm con trỏ khối nhấp nháy (hợp tiêu đề, lời dẫn).
  - Giật khung và xê dịch vệt tracking ở đáy khi cảm xúc chạm đỉnh.
  - `REW` quay ngược: nhiễu, hình đổi sang năm cũ, ngày tháng chạy lùi.
  - `STOP` kết: hình co thành một vạch ngang rồi tắt.
- **Bẫy:** Nhiễu ngẫu nhiên không tính sẵn làm mỗi lần render một khác. Lệch kênh bằng `mix-blend-mode` render ra khối trắng, dùng lớp phủ có độ đậm. Đổ nhiễu phủ kín chữ làm mất tiêu đề. Quên viền tivi và sọc quét khiến hình trông như hoàng hôn phẳng, mất chất băng.

*Style viết riêng cho VideoMotion.*

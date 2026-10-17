# ASCII CRT (màn hình đơn sắc hổ phách, mọi thứ là ký tự)

> Mọi hình trên màn đều là ký tự thật xếp trên lưới đơn cách, sáng bằng phosphor hổ phách của một màn CRT cũ. Cỡ chữ của lưới chính là máy quay.

**Hợp:** công cụ lập trình, viễn tưởng, thương hiệu công nghệ, nhật ký hệ thống, kể chuyện kiểu hồ sơ máy móc.
**Không hợp:** chủ đề ấm áp đời thường, ẩm thực, thời trang, nội dung cần ảnh thật hoặc nhiều màu.
**Cảm xúc:** lạnh, kiên nhẫn, máy móc điềm tĩnh, chờ đợi.

## Hình dung
Một màn hình duy nhất, kính cong nhẹ ở bốn góc, đen ấm khi chưa sáng. Trên đó, ánh hổ phách vẽ bầu trời thưa sao bằng dấu chấm và dấu cộng, mặt đất bằng những hàng chữ dày dần về phía gần, một hành tinh lớn dựng bằng chữ sáng tối theo độ đậm nét. Dưới đáy là dải LOG: nhãn đảo màu, dấu nhắc, một dòng chữ in hoa được gõ từng chữ và con trỏ khối. Cả cảnh chỉ có một màu phosphor; đến một lúc, đúng một vật xa đổi sang xanh băng nhạt.

## Bảng màu
```css
--bg: #0a0704;        /* kính chưa sáng, đen ấm, không đen thuần */
--ink: #ffb000;       /* phosphor hổ phách, chữ chính */
--ink-dim: #7a4310;   /* nét mờ, đường kẻ */
--ink-hot: #ffe39a;   /* điểm chói gần trắng */
--ice: #cfe8f7;       /* màu thứ hai, chỉ cho một vật */
/* thang hổ phách 6 bậc: #3a1f05 #7a4310 #b8680f #e89400 #ffb000 #ffe39a
   thang băng 6 bậc: #1c2a38 #3b5670 #6d93b0 #a6cbe2 #d6eefc #f6fcff */
```
Một phosphor mang mọi thứ. Tối đa một màu thứ hai, dùng cho một vật duy nhất và bật đúng một lần. Công cụ còn lại là độ sáng: mờ, thường, đậm, đảo màu.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=VT323&family=Be+Vietnam+Pro:wght@400;700&display=swap" rel="stylesheet">
```
- Mọi chữ trên màn: VT323 (có tiếng Việt, đã kiểm đủ dấu: Ắ ữ ặ ộ ỡ ề ể ễ ệ đ Đ). Ô chữ rộng 0,4 em, cao 0,8 em.
- Dự phòng: Be Vietnam Pro (có tiếng Việt) cho phụ đề ngoài lưới nếu cần chữ đọc rõ hơn.
- Dòng LOG và tiêu đề viết IN HOA, cỡ 44 đến 48px, như đầu ra của máy.

## Bề mặt
Kính tối ấm, vạch quét ngang mảnh (2px sáng, 2px tối), quầng vignette ở góc, góc bo lớn như ống đèn hình. Chữ có quầng sáng nhẹ cùng màu. Không có lưới ba màu, vì màn đơn sắc không có.
```css
background: radial-gradient(120% 100% at 50% 45%, #1a0f05 0%, #0a0704 70%);
/* vạch quét phủ trên cùng */
background: repeating-linear-gradient(to bottom, transparent 0 2px, rgba(0,0,0,.28) 2px 4px);
```

## Ngôn ngữ minh họa
- **Hình là ký tự:** mỗi ô lưới một ký tự chọn theo độ đậm nét (` .,'\`:-;+=*oOxXHKM#@`), thêm chút nhiễu băm theo ô. Ô quá tối để trống: khoảng trống làm hình đọc được.
- **Hình khối là bóng đổ:** hành tinh, núi, mặt người đều dựng từ silhouette rõ, phía tối chỉ có dấu chấm, phía sáng chữ đậm, viền sáng mảnh tách các lớp.
- **Chiều sâu:** xa thì tối và thưa, gần thì sáng và dày.
- **Thanh trạng thái:** đường nét đứt mờ, nhãn LOG đảo màu, dấu nhắc `>`, con trỏ khối.
- Không ảnh lọc thành ASCII, không sprite, không đường vector tự do.

## Chữ ký chuyển động
- **Bật máy:** một chấm thành vạch sáng rồi nở thành khung hình.
- **Gõ chữ:** chữ nhảy từng ô, đều và nhanh (khoảng 40ms mỗi chữ) cho máy, chậm và lệch nhịp cho người.
- **Quét hàng:** hình hiện theo từng hàng ký tự, từ trên xuống, bằng `steps()` chứ không trượt mượt.
- **Đổi màu một lần:** vật xa chuyển từ hổ phách sang xanh băng trong khoảng 0,1 giây, đúng nhịp, không quay lại.
- **Máy quay là cỡ chữ:** đẩy vào bằng scale nhẹ, kéo ra khi cần ngữ cảnh. Chuyển cảnh bằng xóa màn hoặc vẽ lại, không hòa trộn hai màn.
- Chỉ ba thứ chuyển động liền mạch: máy quay, vật lý ống đèn, hạt khi biến hình. Nhịp chậm, lạnh, có khoảng lặng.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** màn tối, vạch sáng nở ra, tên gõ như tên tệp, con trỏ nhấp nháy.
- **Chương mới:** xóa màn, một tiêu đề IN HOA gõ ra rồi kéo ra thành dòng đầu của danh sách.
- **Hình hiện:** một câu vỡ ra, chữ cái xếp theo độ đậm thành một cảnh chứa đúng những chữ đó.
- **Kết:** mọi dòng cuộn lên và biến mất, chỉ còn dấu nhắc và con trỏ đứng yên.

## Nên tránh
Mưa chữ xanh kiểu phim hacker, ảnh dán rồi phủ bộ lọc ASCII, nhiều màu nhấn, hiệu ứng 3D, bảng điều khiển viễn tưởng bay lơ lửng, phông không đơn cách cho hình, trộn hai màn bằng cross-fade.

## Họ hàng
`terminal-green` (cũng dòng lệnh, nhưng là cửa sổ phẳng nền GitHub, một màu xanh lá, không có kính cong và hình dựng bằng ký tự), `pixel-rpg` (cũng độ phân giải thấp nhưng là sprite và ô pixel tươi, không phải chữ), `retro-vhs` (cũng hoài cổ màn hình cũ nhưng là băng từ nhiều màu, nhiễu và lệch pha).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/ascii-crt.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** một màn CRT hổ phách. Trời đen thưa sao, một hành tinh lớn bằng chữ lơ lửng lệch phải, mặt đất là các cồn cát và miệng hố bằng chữ dày dần về phía gần, dải LOG ở đáy. Có một nhân vật bé dựng bằng ký tự (khoảng bốn hàng, cầm đèn) đứng cạnh một cột anten trên cồn bên trái, cao dưới 1/8 khung. Nhân vật phải có mặt trong cảnh.
- **Chất liệu và ánh sáng:** mọi thứ là chữ VT323 trên lưới 12 x 24px (cỡ 30px); dựng thành các hàng HTML hoặc Canvas 2D theo bậc sáng, không dùng ảnh. Quầng sáng là `text-shadow` tĩnh cùng màu; vạch quét, vignette và góc bo là lớp gradient phủ tĩnh. Hành tinh dùng cùng một lưới ký tự hai bảng màu (hổ phách và băng) chồng lên nhau, đổi bằng opacity. Chỉ tween transform, opacity, màu, clipPath.
- **Máy quay và khung dọc 9:16:** máy là cỡ chữ của lưới: đẩy vào bằng scale chậm 1 tới khoảng 1,04. Ngang tầm màn hình, không xoay. Khung dọc: hành tinh ở nửa trên, mặt đất nửa dưới, dải LOG dưới cùng, tăng cỡ chữ của lưới thay vì thêm cột.
- **Chuyển động:** bật máy (vạch sáng nở thành khung), mặt đất và hành tinh hiện theo hàng bằng `steps()`, chữ gõ từng ô, con trỏ nháy rồi đứng sáng. Chữ không trượt lệch ô, trừ lúc biến hình có chủ ý. Nghỉ cuối cảnh khoảng 0,5 giây.
- **Chữ trên hình:** phụ đề là dải LOG: đường nét đứt mờ, nhãn LOG đảo màu, dấu nhắc, câu IN HOA gõ từng chữ theo giọng đọc, con trỏ khối ở cuối. VT323 có đủ dấu tiếng Việt.
- **Nước đi đặc trưng:**
  - Bật máy: chấm thành vạch rồi thành khung (mở đầu, khởi động hệ thống).
  - Quét hàng: hình hiện từng hàng chữ (lập bản đồ, tải dữ liệu).
  - Đổi màu một lần: vật xa sang xanh băng đúng nhịp (khoảnh khắc có phản hồi, hy vọng).
  - Xóa màn rồi vẽ lại (chuyển chương, khởi động lại).
  - Đẩy vào một ký tự để thấy nó cấu thành từ chữ nhỏ hơn (chi tiết ẩn bên trong).
- **Bẫy:** ảnh lọc thành ASCII thay vì chữ thật; mọi ô tối đều thành chữ nên thành bức tường `-+-+` (phải để trống ô tối); chữ trượt lệch ô; dùng nhiều hơn một màu thứ hai; font không đơn cách làm lệch lưới.

Phỏng theo `styles/ascii-crt/STYLE.md` của lemomo-ai/lemo-opuscar (MIT), qua MotionFly.

*Ý tưởng gốc: lemomo-ai/lemo-opuscar (MIT), qua MotionFly.*

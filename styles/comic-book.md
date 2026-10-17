# Truyện tranh (trang truyện màu kiểu Mỹ)

> Cả deck là một trang truyện in màu: khung ô viền đen dày hơi nghiêng, chấm tram Ben-Day đỏ vàng xanh, ô dẫn chuyện vàng, bong bóng thoại, chữ tượng thanh khổng lồ có viền và tia nổ.

**Hợp:** kể chuyện vui, giới thiệu sản phẩm theo kiểu phiêu lưu, khóa học cho người trẻ, trailer mạng xã hội, bài nói về "người hùng" và "phản diện" (lỗi, rủi ro), sự kiện cộng đồng.
**Không hợp:** báo cáo tài chính, nội dung trang trọng hoặc tang lễ, bảng số liệu dày, thương hiệu cao cấp tối giản.
**Cảm xúc:** sôi nổi, hài hước, kịch tính, tuổi thơ, năng lượng.

## Hình dung
Người xem đang đọc một trang truyện màu mới in: mực đen đậm, ba màu cơ bản đỏ, vàng, xanh, nền ô nào cũng rắc chấm tram. Các ô nằm sát nhau, cạnh hơi xiên, không ô nào thẳng tuyệt đối. Trong ô có người hùng bay vút, ô dẫn chuyện vàng ở góc, bong bóng thoại trắng, và một chữ BÙM to như cả cái ô. Mỗi slide là một trang, không phải một tấm áp phích.

## Bảng màu
```css
--paper: #fff1cc;   /* giấy báo ngả kem, nền trang */
--ink: #14110f;     /* mực đen đậm: viền ô, nét, bóng khối */
--red: #e8281f;     /* đỏ in */
--yellow: #ffd21f;  /* vàng in: nền ô, ô dẫn chuyện */
--blue: #2456d6;    /* xanh in */
--skin: #ffd0a8;    /* da nhân vật */
--white: #ffffff;   /* bong bóng thoại, lõi tia nổ */
```
- Chỉ ba màu cơ bản và đen, trắng, giấy. Mỗi ô lấy một màu chủ đạo làm nền (vàng, xanh hoặc đỏ), các ô cạnh nhau khác màu.
- Độ đậm nhạt làm bằng chấm tram và mảng đen đặc, không bằng gradient.
- Chữ trên nền vàng là mực đen; chữ trên nền xanh hoặc đỏ là trắng hoặc đen trong bong bóng.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Bangers&family=Be+Vietnam+Pro:wght@700;800&display=swap" rel="stylesheet">
```
- Chữ tượng thanh và tiêu đề: Bangers 400 (có tiếng Việt), IN HOA, viền mực dày 14 đến 18px, nghiêng 8 đến 14 độ.
- Thoại và ô dẫn chuyện: Be Vietnam Pro 800 (có tiếng Việt), IN HOA, màu mực. Thân phụ dùng Be Vietnam Pro 700.
- Đã kiểm Google Fonts ngày 17/10/2026: Bangers có đủ bộ vietnamese.

## Bề mặt
Giấy báo ngả kem, phủ chấm tram đỏ rất nhạt. Mỗi ô có nền màu phẳng cộng một lớp chấm tram xoay 45 độ.
```css
background:
  radial-gradient(circle, rgba(232,40,31,.13) 22%, transparent 24%) 0 0 / 24px 24px,
  #fff1cc;
```
Trong SVG dùng `<pattern>` chấm tròn bước 24px, `patternTransform="rotate(45)"`. Viền ô là đa giác mực đen dày 14 đến 16px, góc nhọn (`stroke-linejoin: miter`).

## Ngôn ngữ minh họa
- **Khung ô:** đa giác bốn cạnh hơi xiên, rãnh giữa các ô khoảng 30 đến 40px, nội dung cắt theo khung (`clipPath`).
- **Chấm tram Ben-Day:** chấm tròn đều, bước không dưới 24px ở 1080p, một lớp mỗi ô, xoay 45 độ.
- **Nhân vật nét mực:** viền đen 8 đến 10px, tô phẳng bằng ba màu cơ bản, phần khuất sáng là mảng đen đặc (bóng khối), không tô chuyển sắc. Dáng chéo mạnh, tay chân vươn.
- **Đường tốc độ:** tam giác dài nhọn một đầu, đen đặc, xếp song song sau vật đang lao.
- **Bong bóng thoại:** elip trắng viền đen 8px, đuôi tam giác chỉ về người nói. **Ô dẫn chuyện:** chữ nhật vàng viền đen, nghiêng nhẹ, chữ IN HOA.
- **Tia nổ:** đa giác gai nhiều cạnh, hai lớp lồng nhau (vàng ngoài, trắng trong), chữ tượng thanh đè lên.
- Hình mẫu: thành phố bóng đen có cửa sổ vàng, ngôi sao ngực áo, áo choàng đỏ, bong bóng nghĩ (vòng tròn nhỏ dần), nhãn số trang, dấu chấm than lớn.

## Chữ ký chuyển động
- **Ô bật vào lần lượt:** mỗi ô phóng từ 0,5 lên 1 với `back.out`, xoay nhẹ 5 đến 6 độ về thẳng, theo thứ tự đọc trái sang phải, trên xuống dưới.
- **Máy quay lia từng ô:** cả trang là một lớp lớn, máy phóng vào ô đang kể rồi lia sang ô kế bằng `scale` và `translate`; cuối cùng kéo ra thấy trọn trang.
- **Chữ tượng thanh nổ:** tia nổ phóng ra từ tâm (`back.out` mạnh), chữ rung ngang tắt dần trong nửa giây.
- **Đường tốc độ quét:** các vệt đen trượt ngang vào khung rất nhanh (`power4.out`) rồi đứng.
- **Bong bóng hiện chậm hơn nhân vật:** nhân vật vào trước, ô dẫn chuyện trượt vào, bong bóng nảy lên cuối.
- Nhịp: dứt khoát, giật nhẹ như lật trang, mỗi ô một cú nảy chính.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** tên deck là chữ Bangers khổng lồ có viền, nhân vật phóng ra khỏi khung ô, nhãn "SỐ 1" ở góc.
- **Chương mới:** một ô dẫn chuyện vàng "NGAY LÚC ĐÓ..." trượt vào, nền đổi màu.
- **Điểm nhấn:** tia nổ BÙM chiếm cả ô, camera rung một nhịp.
- **Kết:** kéo máy ra thấy cả trang, ô cuối có dòng "CÒN TIẾP..." trong ô dẫn chuyện.

## Nên tránh
Gradient mượt, bóng đổ mờ, màu ngoài ba màu cơ bản, viền mảnh, ô thẳng tuyệt đối, tram quá mịn, tên hoặc nhân vật của truyện thật, câu thoại dài, chữ thường lẫn lộn kiểu chữ.

## Họ hàng
`halftone-dossier` (cũng chấm tram nhưng là hồ sơ vụ án trên giấy kem, nét navy, vật chứng và con dấu, không có khung ô và chữ tượng thanh), `retro-zine` (cắt dán thô, không có nhân vật nét mực), `midcentury-toon` (cùng nét dày và màu phẳng nhưng nhẹ nhàng, không kịch tính).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/comic-book.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** Một trang truyện ba ô: ô lớn bên trái nền vàng chấm đỏ, một người hùng đeo mặt nạ, áo xanh, sao vàng trước ngực, áo choàng đỏ bay ngược, tay đấm tới, lao chéo lên trên thành phố bóng đen; đường tốc độ đen sau lưng. Ô trên bên phải nền xanh chấm trắng có ô dẫn chuyện vàng và bong bóng thoại. Ô dưới bên phải nền đỏ chấm vàng có tia nổ và chữ BÙM. Người hùng cao khoảng 40% ô lớn.
- **Chất liệu và ánh sáng:** Mọi thứ là mảng phẳng và chấm tram, không gradient. Viền mực 8px quanh nhân vật, 16px quanh ô. Bóng là mảng đen đặc ở phía dưới thân, dưới cánh tay, trên áo choàng (một hướng sáng, từ trên trái). Chấm tram tính bằng `<pattern>`, bước 24px.
- **Máy quay và khung dọc 9:16:** Trang phẳng, nhìn thẳng; di máy bằng `scale` và `translate` cả trang, lia từng ô rồi kéo ra. Ở khung dọc xếp các ô chồng dọc: ô lớn trên, hai ô nhỏ dưới, máy lia từ trên xuống. Giữ 14% đáy cho phụ đề.
- **Chuyển động:** Ô bật vào có overshoot 0,35 đến 0,45 giây. Chữ nổ rung ngang tắt dần, mỗi cảnh chỉ một cú rung chính. Nhân vật có thể giật đổi tư thế hai khung (khoảng 8 fps), chấm tram và chữ thì đứng yên. Tránh trôi mượt kiểu hoạt hình 3D.
- **Chữ trên hình:** Chữ tượng thanh Bangers có viền, tia nổ phía sau. Thoại và ô dẫn chuyện Be Vietnam Pro 800 IN HOA, đủ dấu tiếng Việt. Phụ đề là thanh vàng viền đen, chữ mực, nghiêng 1 độ.
- **Nước đi đặc trưng:**
  - Lia từ ô này sang ô kia, mỗi ô bật vào khi máy tới (hợp kể chuyện theo bước).
  - Chữ tượng thanh nổ kèm rung và tia nổ phóng ra (hợp điểm nhấn, kết quả bất ngờ).
  - Đường tốc độ quét ngang khi nhân vật lao (hợp chuyển ý, tăng tốc, "nhanh").
  - Ô dẫn chuyện vàng trượt vào kèm "NGAY LÚC ĐÓ..." để nhảy thời gian hoặc địa điểm.
  - Kéo máy ra thấy trọn trang ở cuối (hợp tổng kết).
- **Bẫy:** Chấm tram bước dưới 14px bị moiré sau khi nén. Ô thẳng tuyệt đối trông như bảng biểu, giữ cạnh xiên. Tô gradient làm mất chất in. Máy phóng vào chữ khi chữ chưa dựng xong làm chữ nhòe. Thoại dài hơn hai dòng ngắn thì không đọc kịp trên điện thoại.


*Thẻ viết mới cho VideoMotion.*

# Neo-brutalism (thẻ kẹo viền đen bóng cứng)

> Nền màu kẹo, mọi khối viền đen dày 4 đến 6px và bóng đen cứng lệch 8px không mờ; nút như nút thật bị nhấn lún, huy hiệu tròn xoay nghiêng, sticker dán lệch, dải chữ chạy có dấu ✦.

**Hợp:** ra mắt app và sản phẩm số, khuyến mãi, thương mại điện tử, sự kiện giới trẻ, quảng cáo ngắn, hướng dẫn từng bước vui vẻ.
**Không hợp:** nội dung trang trọng, tài chính nghiêm túc, văn hóa truyền thống, chủ đề chữa lành, báo cáo cho lãnh đạo.
**Cảm xúc:** ồn ào, vui, dạn dĩ, nghịch ngợm, bấm là có phản hồi.

## Hình dung
Một bảng tin dán đầy sticker trên tường quán trà sữa: mỗi tấm thẻ là miếng bìa cứng sơn màu kẹo, cắt thô, viền mực đen, đặt nổi lên nhờ cái bóng đen đặc phía dưới bên phải. Nút thì như công tắc nhựa: bấm xuống là bóng biến mất, nhả ra là bật lại. Người xem thấy ngay chỗ nào để nhìn, chỗ nào để bấm.

## Bảng màu
```css
--bg: #FF8FC7;      /* hồng kẹo: nền chính */
--sky: #7DD3FC;     /* xanh trời: thẻ lớn */
--yellow: #FFE14D;  /* vàng: ô số liệu, dải chạy */
--banana: #B7F25E;  /* xanh lá chuối: nút, nhãn */
--paper: #FFF8E8;   /* kem: nền chữ, sticker */
--ink: #111111;     /* viền, chữ, bóng */
--sh: 8px 8px 0 #111111;  /* bóng cứng, không mờ */
```
- Bốn màu kẹo chia nhau diện tích, mỗi khối một màu, không pha sắc độ giữa chừng.
- Đen chỉ dùng cho viền, chữ và bóng; không đổ thành mảng nền lớn.
- Nền có thể đổi giữa hồng, xanh trời, vàng, xanh chuối từng cảnh, các khối bên trên chọn màu khác với nền.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@400;900&family=Space+Mono:wght@700&display=swap" rel="stylesheet">
```
- Tiêu đề và số: Lexend 900 (có tiếng Việt), IN HOA, dòng 0,95, giãn âm nhẹ.
- Thân: Lexend 400 (có tiếng Việt).
- Nhãn, sticker, dải chạy: Space Mono 700 (có tiếng Việt), IN HOA, giãn 0,06em.
- Chữ có dấu tiếng Việt nằm ở Lexend, đủ nặng để dấu không bị nuốt; cỡ tiêu đề không dưới 120px khi khung 1920.

## Bề mặt
Phẳng, màu đặc, không gradient, không mờ. Nền có thể lót chấm đen nhỏ rất thưa. Mọi khối đều có viền và bóng cứng.
```css
.khoi { border: 6px solid #111; box-shadow: 8px 8px 0 #111; border-radius: 0; }
.nut  { border: 5px solid #111; box-shadow: 8px 8px 0 #111; }
.nut:active { transform: translate(8px, 8px); box-shadow: 0 0 0 #111; }
```
Góc vuông là mặc định; chỉ huy hiệu và con trỏ được tròn hoặc nhọn.

## Ngôn ngữ minh họa
- **Thẻ lớn:** khối vuông viền 6px, bóng 8px, đặt nghiêng 1 đến 3 độ.
- **Nút:** khối màu chuối, chữ IN HOA, bóng 8px; trạng thái nhấn lún tịnh tiến đúng 8px và bóng về 0.
- **Huy hiệu tròn:** hình tròn viền dày, chữ ngắn như "MỚI", xoay nghiêng 10 đến 20 độ, nằm đè lên góc thẻ.
- **Ô số liệu:** khối vàng, số khổng lồ 200px trở lên, nhãn mono nhỏ bên dưới.
- **Ngôi sao, tia nổ, con trỏ chuột:** đa giác nhọn tô màu, viền đen, bóng cứng; con trỏ chỉ vào nút.
- **Dải chữ chạy:** băng ngang viền đen trên và dưới, chữ mono lặp lại cách nhau bằng dấu ✦.
- **Sticker dán lệch:** nhãn kem xoay vài độ, đè lên mép thẻ như băng dính.

## Chữ ký chuyển động
- **Thả nảy cứng:** khối rơi từ trên khung, chạm đáy nảy hai nhịp ngắn rồi đứng (`bounce.out`), không mềm.
- **Nhấn nút:** nút tịnh tiến xuống 8px, bóng thu về 0 trong khoảng 0,08 giây, giữ chốc lát rồi bật lại.
- **Dải chạy:** băng chữ trượt ngang đều, dừng gọn khi cảnh chốt.
- **Huy hiệu lắc:** xoay qua lại tắt dần quanh góc nghiêng gốc, như vừa bị vỗ.
- **Dán sticker:** scale từ 1,4 về 1 kèm xoay nhẹ, như bàn tay ấn xuống.
- Nhịp: dứt khoát, vui, cắt nhanh; không mờ dần, không trôi mượt.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** thẻ xanh trời rơi xuống, tiêu đề 150px, huy hiệu "MỚI" lắc ở góc, dải chạy trên đầu.
- **Con số:** ô vàng khổng lồ nảy vào, số đếm lên rồi đứng, sticker dán lệch bên cạnh.
- **Kêu gọi hành động:** con trỏ trượt tới nút, nút lún xuống, bật lại, cả khung rung nhẹ một nhịp.
- **Kết:** nền đổi sang vàng, thẻ lớn chữ đen, ngôi sao xoay chốt.

## Nên tránh
Bóng mờ, gradient, bo góc mềm, viền mảnh dưới 4px, chữ có chân, màu pastel nhạt, quá ba kiểu khối trên một khung, chuyển động trôi mượt.

## Họ hàng
`raw-grid` (cũng viền đen và bóng cứng nhưng nền trắng, viền 3px, hồng và xanh lá phấn, trật tự lưới), `neo-grid-bold` (biên tập thô mộc, không viền, vàng chanh), `block-frame` (khung khối màu rực).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/neo-brutalism.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** một mặt bàn quảng cáo đầy màu: nền hồng kẹo lót chấm thưa, thẻ xanh trời lớn nghiêng nhẹ ở giữa, ô số liệu vàng khổng lồ bên phải, nút chuối ở chân thẻ và con trỏ chuột đen đang chỉ vào nút. Nhân vật chính là chính cái nút và con trỏ; nếu cần người thì vẽ mặt tròn phẳng viền đen, hai chấm mắt, miệng một nét.
- **Chất liệu và ánh sáng:** hoàn toàn phẳng: màu đặc, viền đen 4 đến 6px, bóng cứng lệch 8px về dưới phải (khối đổ bóng bằng một khối đen đặt lệch, không blur). Không có nguồn sáng, không gradient. Độ sâu chỉ đến từ bóng cứng và thứ tự chồng lớp.
- **Máy quay và khung:** máy đứng yên, nhìn thẳng như một tấm áp phích; khung ngang 16:9 chia ba vùng (dải chạy trên cùng, thẻ lớn bên trái, số liệu và sticker bên phải). Khung dọc 9:16 xếp dọc: dải chạy, thẻ, ô số, nút. Cú rung máy nhẹ 6px một nhịp chỉ dùng khi nút lún.
- **Chuyển động:** khối thả xuống nảy cứng (`bounce.out`, 0,5 đến 0,7 giây), nút lún bằng tịnh tiến 8px trong 0,08 giây rồi bật lại `back.out`, huy hiệu lắc tắt dần, dải chạy đều rồi dừng `power3.out`. Không dùng ease mềm cho khối; không mờ dần.
- **Chữ trên hình:** tiêu đề Lexend 900 IN HOA 120 đến 160px trên thẻ; nhãn Space Mono trong viên kem; số liệu 200px trở lên. Mỗi cảnh một câu ngắn, một con số hoặc một động từ ra lệnh. Đủ dấu tiếng Việt, tránh cắt dấu ở dòng 0,95.
- **Nước đi đặc trưng:**
  - Thả thẻ: khối rơi, nảy hai nhịp, bóng dính theo (bóng là khối riêng đi cùng).
  - Bấm nút: con trỏ tới, nút lún, bóng về 0, bật lại; kết quả hiện ngay sau cú bấm.
  - Huy hiệu "MỚI" bật ra rồi lắc, báo điểm đáng chú ý.
  - Dải chạy quét ngang mở cảnh, chữ lặp lại cách nhau bằng ngôi sao.
  - Dán sticker: nhãn phóng to 1,4 rồi ấn xuống đúng chỗ, xoay lệch vài độ.
- **Bẫy:** bóng bị mờ hoặc làm bằng `filter` động; quên bóng cứng ở khối phụ nên khối trông phẳng lép; quá nhiều màu kẹo cùng cỡ làm hỏng thứ bậc; nút lún mà bóng không về 0 nên mất cảm giác bấm; chữ có dấu bị cắt vì dòng quá sát.

*Ý tưởng gốc: phong cách neo-brutalism phổ biến trong thiết kế web; thẻ viết riêng cho VideoMotion.*

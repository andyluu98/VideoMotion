# Ukiyo-e (tranh khắc gỗ Nhật trên giấy washi)

> Một tờ tranh khắc gỗ trên giấy washi, khung viền đôi mực sumi: mảng màu phẳng in từ từng bản khắc, nét khóa đen đè lên lệch vài pixel, và một vầng mặt trời đỏ son.

**Hợp:** văn hóa, du lịch Nhật, thơ ca, lịch sử, thương hiệu truyền thống.
**Không hợp:** công nghệ hiện đại, số liệu dày, nội dung vui nhộn cho trẻ em.
**Cảm xúc:** cổ điển, tĩnh lặng, trang trọng, đậm chất Nhật.

## Hình dung
Người xem cầm một tờ tranh in thủ công: giấy washi vàng nhạt, trời lau mờ dần (bokashi), núi hai mảng có chóp tuyết là giấy để trắng, dải sương ngang, hàng sóng vảy, cành thông hắt vào góc, phiến tiêu đề dọc và con dấu đỏ. Chiều sâu chỉ đến từ các lớp ngang xếp chồng. Deck có ba bản in: ngày, đêm (chương mới, câu trích), bình minh (kết).

## Bảng màu
```css
--washi: #EBDDB8;   /* giấy washi, nền */
--slip: #F4EACB;    /* phiến giấy, chỗ không in (bọt sóng, tuyết, sương) */
--sumi: #211E1B;    /* mực sumi: nét khóa, chữ */
--muted: #4A4136;
--ind: #1F3F73;     /* chàm Phổ: sắc chủ đạo cho trời, nước (sẫm #14284F, vừa #2E5088) */
--blue: #4F78A8; --pale: #8FB0CB;   /* nước, xanh nhạt */
--red: #C23B2B;     /* đỏ son: mặt trời, con dấu, một mảnh áo */
--beni: #9E2A1F;    /* chữ nhấn đỏ */
--ochre: #D2A24A; --wood: #9A6A3E; --pine: #587A4A;
```
Một sắc chủ đạo (chàm Phổ). Đỏ son hiếm: một điểm đỏ lớn mỗi slide là đủ.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif:wght@500;600;700;800&family=Be+Vietnam+Pro:wght@400;500;600&display=swap" rel="stylesheet">
```
- Tiêu đề và nhãn: Noto Serif 700, nhãn trong hình IN HOA 22 đến 34px.
- Thân: Be Vietnam Pro 400 đến 500.
- Số trong ô vuông đỏ: chữ màu giấy trên đỏ, như con dấu in.
- Cả hai font có bộ chữ tiếng Việt (đã kiểm Google Fonts ngày 16/10/2026). Phiến tiêu đề dọc dùng nét cọ trừu tượng, không dùng chữ Hán hay chữ Nhật.

## Bề mặt
Giấy washi có sợi, khung viền đôi mực sumi quanh tờ. Trời là bokashi: dải chàm lau mờ dần xuống, chỗ duy nhất được dùng chuyển màu. Thẻ nội dung là phiến giấy (`rgba(244,234,203,.7)`) góc vuông, khung mảnh bên trong cách 8px.

## Ngôn ngữ minh họa
- **Nét khóa** sumi: 2,8 (viền), 1,8 (chi tiết), 3 (khung phiến).
- **Lớp màu lệch đăng** 2 đến 3px so với nét khóa (dịch lớp màu, không dịch lớp nét).
- **Mảng tối đôi:** vật có hai mặt chia bằng hai sắc chàm; chóp tuyết khoét giấy.
- **Vảy sóng (seigaiha):** hàng nửa vòng tròn đè nhau, mỗi vảy có ba vòng bọt giấy mờ, hàng trên nhạt hàng dưới đậm.
- Hình mẫu: ô vuông đỏ có số, con dấu vuông khoét họa tiết giấy, phiến giấy có thẻ màu ở cạnh trái, tư thế bóng ma nét đứt, ba nét gió cong sau vật chuyển động, thuyền gỗ có dải đỏ ở mạn, người nhỏ phẳng màu chàm sẫm đội nón vàng.
- Phẳng có chủ ý: không phối cảnh hội tụ, chỉ lớp ngang song song.

## Chữ ký chuyển động
- **In từng bản khắc:** nét khóa `draw` trước, rồi từng bản màu `fade` vào lệch đúng 3px, theo thứ tự in (chàm, xanh, vàng đất, đỏ cuối cùng), cuối là chữ.
- **Sương trôi ngang:** dải kumo là lớp cố định theo `data-scene`, mỗi slide trôi tới một độ cao khác, như cuộn tranh được kéo dần.
- **Đổi bản in ngày, đêm, bình minh:** lớp màu nền đổi theo `data-scene`; mặt trời đỏ `data-morph` thành trăng màu giấy ở bản đêm.
- **Sóng dâng từng hàng:** hàng vảy sóng `rise` từ dưới lên, `data-stagger` khoảng 150ms.
- **Đóng dấu đỏ:** con dấu vuông `stamp` ở cuối mỗi chương hoặc ở trạm kết.
- Nhịp: chậm, tĩnh, có khoảng lặng giữa các lớp. Không lặp, không rung.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** trời bokashi, núi in từng lớp, mặt trời đỏ hiện cuối, phiến tiêu đề dọc và con dấu.
- **Hành trình:** dải sương vàng đất làm trục, mỗi trạm một con dấu vuông với họa tiết khác nhau.
- **Câu thơ, câu trích:** bản in đêm, trăng giấy, chữ màu giấy giữa nhiều khoảng chàm sẫm.
- **Kết:** bản in bình minh, con dấu đỏ đóng xuống góc tờ.

## Nên tránh
Màu ngoài bảng, đỏ son nhiều hơn một điểm nhấn mỗi hình, gradient trơn (trừ bokashi), bóng đổ, ánh sáng trên vật, 3D, glow, phối cảnh hội tụ, chữ Hán hay chữ Nhật thật hoặc giả, chép bố cục tranh nổi tiếng (sóng lớn, núi đỏ, cầu mưa), con dấu của nghệ nhân có thật, số liệu bịa.

## Họ hàng
`thuy-mac` (cũng Á Đông và tĩnh, nhưng là mực nước sắc độ loang, không có mảng màu in phẳng), `woodcut` (khắc gỗ thô kiểu phương Tây, mạnh và kịch tính, đen trắng nhiều hơn), `silkscreen-poster` (in từng lớp mực phẳng, nhưng không có nét khóa, chất poster du lịch phương Tây).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/ukiyoe.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** Một tờ tranh in đặt trên nền giấy mount màu be, có khung viền đôi mực sumi. Biển chàm với hàng vảy sóng, một đợt sóng khổng lồ cuộn thành hình ngọn núi xanh có vân trắng, một ngọn núi xa nhỏ có chóp tuyết ở chân trời, mỏm đá xám bên phải với cây thông nghiêng có các tán dẹt. Nhân vật rất nhỏ: một người phẳng đội nón rộng đứng trên mỏm đá, và một dáng trắng nhỏ ngồi trên đỉnh sóng. Mỗi người cao dưới 8% khung.
- **Chất liệu và ánh sáng:** Mảng màu phẳng, mỗi nhóm màu là một `<g>` riêng, dịch lệch 2 đến 3px so với nét khóa sumi (lớp màu dịch, lớp nét không dịch). Trời là bokashi: một gradient dọc tĩnh chàm nhạt tới kem, tính theo cột bằng nhiều dải `<rect>` có mép lượn, không để lộ đường nối. Sóng là hàng nửa vòng tròn đè nhau (seigaiha) hai ba sắc chàm, bọt là giấy để trắng. Phủ sợi giấy washi và vân gỗ rất nhẹ bằng canvas vẽ một lần, alpha khoảng 0,09. Không bóng đổ, không ánh sáng trên vật, đỏ son chỉ một điểm.
- **Máy quay và khung dọc 9:16:** Nhìn ngang, phẳng, chỉ xếp lớp ngang song song, không phối cảnh hội tụ. Ở dọc, trời chiếm phần trên, sóng núi khổng lồ ở giữa, biển ở dưới, thông và mỏm đá cắt mạnh một mép; có thể đặt thành cuộn tranh dọc. Di máy là handscroll: trượt cả tờ hoặc chuyển từ tờ này sang tờ kế qua khoảng giấy mount, bằng `x` hoặc `y`, mượt 24 fps.
- **Chuyển động:** Tranh phần lớn đứng yên, mỗi cảnh chỉ một hai việc nhỏ (sóng nhấp nhô, mây trôi, lá rơi). Nhân vật và thiên nhiên đổi tư thế 8 fps theo nấc, sóng 12 fps. Mỗi bản màu hiện trong khoảng 0,3 giây bằng `clipPath` quét chéo, trượt 5 đến 6px vào chỗ. Giữ một nhịp khoảng một giây để người xem đọc.
- **Chữ trên hình:** Chữ là phiến giấy kem viền đôi mực, đặt ở lề hoặc mép dưới, tiêu đề dọc là phiến nhỏ với nét cọ trừu tượng, không dùng chữ Hán hay Nhật. Chữ Noto Serif đậm cho chữ không dấu, chữ có dấu dùng Be Vietnam Pro, đủ dấu Việt. Con dấu vuông đỏ son có số là dấu chấm câu của mỗi tờ, đóng bằng `scale` 1,35 về 1 trong 0,2 giây.
- **Nước đi đặc trưng:**
  - In từng bản khắc: nét khóa vẽ trước, các bản màu đáp lệch rồi khớp: hợp mở cảnh, một thứ đang thành hình.
  - Trượt cuộn tranh từ phải sang trái: hợp hành trình, các bước, trạm.
  - Cùng một chủ thể đặt lệch khác nhau mỗi tờ: hợp so sánh, một thứ qua nhiều thời kỳ.
  - Đổi bản in ngày sang đêm, mặt trời đỏ thành trăng giấy: hợp chương mới, câu trích.
  - Con dấu đỏ đóng xuống góc tờ: hợp kết chương, kết luận.
- **Bẫy:** Chuyển sắc dùng nhiều dải `fillRect` hở nối thì lộ đường dọc. Đặt phối cảnh hội tụ cho đồng ruộng hay sóng làm hỏng độ phẳng. Quá nhiều vân và sợi làm vùng tối như giấy ráp, giữ alpha thấp. Con dấu dùng chế độ multiply sẽ biến mất trên nền tối, dùng chồng thường.

Phỏng theo `styles/ukiyoe/STYLE.md` của lemomo-ai/lemo-opuscar (MIT).

*Ý tưởng gốc: MotionFly / lemo-opuscar (MIT), qua SlideFly.*

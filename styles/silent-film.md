# Phim câm (rạp chiếu bóng thập niên 1920)

> Một cuốn phim bạc sepia chiếu giữa hai tấm màn nhung: không ai nói, chữ nằm trên thẻ đen viền trang trí, vệt xước và bụi chạy qua khung hình.

**Hợp:** kể chuyện, lịch sử, điện ảnh, thuyết trình cần giọng hài hước khô hoặc hoài niệm.
**Không hợp:** sản phẩm công nghệ mới, nội dung cần nhiều màu để phân biệt, số liệu dày.
**Cảm xúc:** hoài cổ, kịch tính, đen trắng, điện ảnh.

## Hình dung
Người xem ngồi trong rạp nhỏ: màn nhung hai bên, máy chiếu rè rè phía sau. Hình là bản in mực và màu nước xám chiếu trên phim bạc, mép phim cháy sẫm. Nhân vật nhỏ trong cảnh rộng, kể bằng dáng điệu, mặt gần như không đổi. Lời thoại và ý chốt không nằm trong hình mà trên thẻ chữ đen (intertitle), cắt vào dứt khoát.

## Bảng màu
```css
--black: #0E0A08;   /* thẻ chữ đen, khung phim */
--bg: #120A0A;      /* rạp tối quanh màn */
--ink: #1E1610;     /* mực, chữ trên phim */
--muted: #4A3C2C;
--sep: #DACEB2;     /* giấy phim */
--pale: #F2EBDA;    /* nền trời sáng */
--cream: #EFE4C8;   /* chữ và nét kem trên thẻ đen */
--amber: #E3B96C;   /* sắc hổ phách trên thẻ đen */
--ox: #8F2A1A;      /* đỏ nâu oxblood: chữ số, rất hiếm */
/* năm bậc xám bạc, sáng tới tối */
--f1: #E4DAC0; --f2: #C9BB98; --f3: #A8977A; --f4: #8F7A57; --f5: #6E5E46; --f6: #4A3C2C; --f7: #2E241A;
```
Một sắc bạc gánh cả bức tranh: giá trị sáng tối làm việc thay màu. Chỉ thêm hai màu: hổ phách trên thẻ đen và đỏ nâu cho con số quan trọng.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display+SC:wght@400;700;900&family=Newsreader:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&display=swap" rel="stylesheet">
```
- Tiêu đề và thẻ chữ: Playfair Display SC 700, chữ hoa nhỏ, giãn 0,03em, kem trên đen.
- Thân và lời dẫn: Newsreader 400 đến 500, nghiêng cho câu thoại.
- Cả hai font có bộ chữ tiếng Việt (đã kiểm Google Fonts ngày 16/10/2026).

## Bề mặt
Mặt phim sepia bạc, mép cháy tối dần (vignette), vệt xước dọc mảnh, vài hạt bụi, một sợi tóc trong khe chiếu. Ngoài khung là màn nhung và bóng tối rạp. Thẻ chữ đen có viền trang trí kiểu deco mảnh màu kem.

## Ngôn ngữ minh họa
- Vật là hình khối phẳng nhiều bậc xám, vùng tối phủ **gạch bóng 45 độ** (khoảng 6px, nét 1,5px, mờ 35 đến 55%). Vùng sáng không gạch.
- Xa nhạt (xám 1 đến 3), gần đậm (xám 5 đến 7): chiều sâu bằng giá trị, không bằng mờ nhòe.
- Nét viền mực 2,5px chỉ ở vật chính. Nhân vật: mũ lưỡi trai, mặt sáng, áo khoác tối, chân thẳng; giữ nhỏ trong cảnh rộng.
- Hình mẫu: khung phim đen có hai hàng lỗ răng cưa, vật có gạch bóng kèm một nét sáng cạo, đường bay chấm (`dasharray 2 9`), ba nét tốc độ, băng dính nối phim (dấu "cắt, tách"), số trong vòng tròn nét kem, bảng kê kiểu cue sheet.

## Chữ ký chuyển động
- **Iris mở và đóng:** bìa và kết mở bằng một vòng tròn từ tâm loang ra cả màn (`zoom` trên mặt nạ tròn), cảnh cuối thu lại về một chấm.
- **Cắt sang thẻ chữ:** ý chốt là một thẻ đen chiếm cả khung, vào bằng `data-transition="cut"`, chữ kem `fade` chậm sau 300ms như thợ chiếu đổi phim.
- **Đèn chiếu chập chờn:** lớp vệt xước và bụi là lớp cố định xuyên deck, độ sáng màn `blink` thật nhẹ (biên độ nhỏ), tối đa một thứ lặp nữa trên slide.
- **Màn nhung kéo ra:** ở bìa, hai tấm màn `left` và `right` rời khỏi giữa.
- **Dải phim chạy:** dải phim có lỗ răng cưa trôi ngang bằng `scan` cho ý "thời gian trôi, lưu trữ".
- Nhịp: máy quay nặng, cảnh đứng yên; chuyển động ở chỗ cắt và mở, không ở việc xoay hay phóng vật.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** màn nhung kéo ra, iris mở, thẻ chữ "PHẦN MỘT" trước khi cảnh đầu hiện.
- **Nguyên nhân và hậu quả:** một cảnh rộng duy nhất nhìn thấy cả hai, nhân vật nhỏ ném máy bay giấy theo đường chấm.
- **Trước và sau:** hai khung phim nối nhau bằng băng dính, khung "sau" chờ cú bấm.
- **Kết:** iris đóng về một chấm, thẻ chữ "HẾT" viền deco.

## Nên tránh
Màu rực, gradient màu, bóng đổ màu, glow, 3D, chân dung cận cảnh lớn, nhân vật giống Charlot (mũ phớt tròn, ria bàn chải, gậy), cảnh hay logo hãng phim có thật, số liệu bịa trong hình, câu dài trong hình (chữ thuộc về thẻ chữ).

## Họ hàng
`vintage-editorial` (giấy báo ấm, bố cục tạp chí, không có rạp và phim), `rubber-hose` (cũng đen trắng hoài cổ nhưng là hoạt hình nhí nhảnh có mặt cười), `engraving` (nét khắc đồng tinh xảo, học thuật, không có thẻ chữ và cắt cảnh).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/silent-film.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** Một phố nhỏ thập niên 1920 trong khung 4:3 giữa hai tấm màn nhung tối. Mặt tiền nhà nhiều cửa sổ chia ô, biển cửa hiệu, cửa gỗ lớn có bậc thềm. Hai nhân vật diễn bằng dáng: một người thợ bánh cao, đội mũ trắng, tạp dề dài, đứng thẳng; một đứa trẻ đội mũ nồi, áo khoác tối, ngồi trên bậc thềm ôm ổ bánh tròn. Người lớn cao khoảng 80% khung hình in, trẻ nhỏ hơn nhiều. Mặt sáng, gần như không đổi nét, người dựng bằng khối phẳng nhiều bậc xám.
- **Chất liệu và ánh sáng:** Chỉ giá trị xám trên nền sepia bạc: khối phẳng ở năm bậc xám, vùng tối phủ gạch bóng 45 độ (pattern `<pattern>` hoặc nhiều `<line>`, bước khoảng 6px, nét 1,5px, mờ 35 đến 55%), vùng sáng để trống. Nét viền mực 2,5px chỉ ở vật chính. Xa nhạt, gần đậm. Lớp phủ tĩnh: vignette mép cháy, vệt xước dọc mảnh, vài hạt bụi, một sợi tóc. Độ sáng cả màn nhấp nháy rất nhẹ bằng `opacity` lớp phủ. Không màu ngoài tông sepia; filter chỉ để tĩnh.
- **Máy quay và khung dọc 9:16:** Máy nặng, hầu hết cảnh đứng yên, cỡ toàn đến trung, nhân vật nhỏ trong cảnh rộng. Ở dọc, khung in 4:3 đặt giữa trên nền màn nhung, hai tấm màn chiếm phần trên và dưới thêm bóng tối rạp; chừa dải dưới cho thẻ chữ. Di máy chỉ là push rất chậm hoặc trượt ngang lớp nền; mở và đóng bằng iris (clipPath hình tròn).
- **Chuyển động:** Lấy mẫu như quay tay khoảng 16 fps: nhân vật và máy đổi tư thế theo nấc (`steps()`), còn xước, bụi, nhấp nháy đổi mỗi khung. Diễn xuất deadpan: mặt ít đổi, thân diễn (cúi trước khi làm, giữ dáng, giật hai khung khi bất ngờ). Cắt thẳng, iris, tối dần; không dissolve.
- **Chữ trên hình:** Chữ nằm trên thẻ đen (intertitle) chiếm cả khung, viền deco mảnh màu kem, vài chữ mỗi thẻ. Tiêu đề Playfair Display SC cho chữ không dấu, chữ có dấu dùng Be Vietnam Pro đậm; lời dẫn nghiêng dùng Newsreader nghiêng hoặc Be Vietnam Pro nghiêng, đủ dấu Việt. Biển cửa hiệu trong cảnh chỉ là chữ ngắn trên vật. Thẻ giữ tối thiểu 1,8 giây.
- **Nước đi đặc trưng:**
  - Cảnh rộng đứng yên, nhân vật nhỏ diễn một hành động: hợp kể nguyên nhân, hậu quả.
  - Cắt sang thẻ chữ đen, chữ kem hiện chậm sau 300ms: hợp ý chốt, đảo chiều.
  - Iris mở ở bìa, thu về một chấm ở kết: hợp mở và kết.
  - Iris dừng nửa chừng để nhân vật liếc khán giả: hợp bí mật, đồng lõa.
  - Màn nhung kéo ra rồi thẻ "PHẦN MỘT": hợp mở đầu.
- **Bẫy:** Thêm màu hay gradient màu làm mất chất phim bạc; mọi giá trị phải là xám sepia. Cận cảnh mặt lớn nhìn như ma-nơ-canh, giữ nhân vật nhỏ hoặc đặt trong iris. Nhồi nhiều hành động vào một cảnh nhỏ thì thành nhiễu; một chuỗi rõ, có nhịp dừng. Rèm đóng mà chỉ được sáng bởi màn tối thì đen kịt, thêm sáng chân rèm.

Phỏng theo `styles/silent-film/STYLE.md` của lemomo-ai/lemo-opuscar (MIT).

*Ý tưởng gốc: MotionFly / lemo-opuscar (MIT), qua SlideFly.*

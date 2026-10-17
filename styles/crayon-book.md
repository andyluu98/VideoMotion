# Sách tranh sáp màu (trang truyện thiếu nhi tô sáp)

> Mỗi slide là một trang sách tranh tô bằng sáp màu trên giấy có vân: nét chàm sần, màu lem ra ngoài viền, khe giấy trắng lấp lánh.

**Hợp:** bài giảng cho trẻ em, truyện kể trước giờ ngủ, giáo dục mầm non, câu chuyện thương hiệu dịu dàng.
**Không hợp:** báo cáo doanh nghiệp, công nghệ, số liệu tài chính, sự kiện trang trọng.
**Cảm xúc:** ngây thơ, ấm áp, thủ công, kể chuyện.

## Hình dung
Một cuốn sách tranh mở trên đùi, giọng kể dịu và chậm. Hình vẽ theo logic trẻ con: nhà có một mặt tiền thẳng và một mặt hông nghiêng, người to hơn cửa, mặt trời cười, ngôi sao có mắt. Sáp chỉ bám vào đỉnh vân giấy nên mảng màu nào cũng lốm đốm trắng. Mỗi trang kể một việc.

## Bảng màu
```css
--paper: #F4EFE3;    /* giấy có vân, cũng là màu hạt trắng */
--ink: #2A2850;      /* chàm đậm: viền, mắt, chữ. Không bao giờ đen */
--muted: #5A5675;    /* chữ phụ, nhãn viết tay */
--coral: #B8381F;    /* chữ nhấn (sáp san hô trong hình #D9543A, tối #C94632) */
--blue: #3F5FA8; --plum: #7A4A7C; --teal: #17706C;   /* màu chữ phụ */
/* hộp sáp trong hình */
--yellow: #F2B632; --orange: #EE8A2E; --green: #5E9A4A; --sky: #6F98D2;
--pink: #EE8FA0; --brown: #8B5A3C; --wash: #4C74D2; /* màu nước duy nhất, đặc 0,1 đến 0,2 */
```
Hộp khoảng 12 cây sáp, không hơn. Một mảng màu nước xanh là khách, sáp mới là chủ. Độ đậm nhạt đến từ lực tay (gạch thưa hay dày), không thêm màu mới.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Itim&family=Mali:wght@400;500;600;700&display=swap" rel="stylesheet">
```
- Tiêu đề và nhãn trong hình: Itim, tròn, thân thiện như chữ cô giáo viết.
- Thân: Mali 400 đến 600, nét viết tay dễ đọc.
- Cả hai font có bộ chữ tiếng Việt (đã kiểm Google Fonts ngày 16/10/2026).

## Bề mặt
Giấy ấm có vân sần, bóng gáy sách ở giữa, một mảng màu nước xanh nhạt loang ở một góc, dải cỏ sáp xanh ở đáy. Thẻ nội dung là giấy trắng hơi trong, bo góc lệch (`22px 30px 20px 28px`) như cắt bằng kéo.

## Ngôn ngữ minh họa
- **Viền kép:** một nét chàm đậm 4 đến 6px và một nét mảnh nửa độ dày lệch nhẹ, đầu nét tròn.
- **Mảng tô** là nhiều nét cong song song cách 6 đến 9px, dày 6 đến 8, vượt mép 3 đến 6px; vùng lớn thêm một lượt gạch chéo thưa. Phủ lên một lớp chấm giấy (pattern) để thành vân. Không bao giờ là mảng phẳng.
- Vật được vẽ trước, màu tô sau. Chừa nhiều giấy trống.
- Hình mẫu: ngôi sao có mặt (tối đa ba), mặt trời cười, chấm tròn tô sáp làm trạm, cây sáp làm chú thích, máy bay giấy với đường bay xoắn chấm chấm, số trong vòng tròn giấy, nhãn viết tay 2 đến 4 chữ.
- Mặt (hai chấm mắt, má hồng gạch, miệng một nét cong) chỉ cho vật chính.

## Chữ ký chuyển động
- **Vẽ rồi mới tô:** viền chàm hiện bằng `draw` theo thứ tự người vẽ, xong thì lớp tô sáp `wipe` qua như tay đang gạch màu, cuối cùng nhãn `fade`.
- **Lật trang sách:** chuyển chương bằng `data-transition="wipe"`, như ngón tay lật sang trang mới.
- **Mặt trời đung đưa:** mặt trời cười `sway` nhẹ ở góc trời; ngôi sao có mắt `pulse` chậm như đang chớp mắt.
- **Máy bay giấy bay vòng:** máy bay đi theo đường xoắn chấm bằng `<animateMotion>`, một lần, rồi đậu lại.
- **Vật rơi nhẹ vào trang:** quả táo, ngôi sao `drop` có nảy nhỏ, mỗi lần một vật.
- Nhịp: chậm, dịu, như giọng đọc truyện trước giờ ngủ. Tối đa hai thứ lặp mỗi slide.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** ngôi nhà góc nhìn trẻ con, cây táo, mặt trời cười vẽ dần rồi tô màu, tên truyện viết tay.
- **Đếm và so sánh:** các chấm tròn tô sáp hiện từng cái (`pop` + `data-stagger`), số chấm đúng bằng số trong lời kể.
- **Hành trình:** đường chấm sáp san hô uốn qua trang, mỗi trạm một chấm tròn, máy bay giấy bay dọc theo.
- **Kết:** bầu trời đêm, ba ngôi sao có mắt chớp, lời chúc ngủ ngon.

## Nên tránh
Mảng màu phẳng không có nét tô và vân, gradient mượt, bóng đổ, hiệu ứng thủy tinh, 3D, filter làm mờ, viền đen, hơn 12 màu sáp, hơn một màu nước, màu nước phủ lên nhân vật, nhân vật hay câu chữ của sách thật, số liệu bịa.

## Họ hàng
`whiteboard` (cũng nét tay nhưng là bút lông trên bảng, giảng giải cho người lớn), `paper-popup` (sách thiếu nhi nhưng là thẻ giấy cắt bật lên, màu rực và sạch), `clay-3d` (mềm mại vui tươi cho trẻ em, nhưng là khối đất nặn có chiều sâu, không có vân sáp).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/crayon-book.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** một trang sách tranh thiếu nhi vẽ bằng sáp màu, cảnh đêm. Nền trời xanh chàm đậm, sao trắng nhiều cánh, đồi xa xanh tối. Một mái nhà đỏ cam dốc chéo với ống khói nâu và cửa sổ tròn trên tường vàng. Trên mái ngồi một cô bé đầu tròn, tóc nâu buộc chỏm, má hồng, hai chấm mắt, váy hồng, tay ôm một con cừu bông. Nhân vật cao khoảng 1/3 khung; mái nhà chiếm nửa dưới.
- **Chất liệu và ánh sáng:** nền giấy có răng, dựng bằng `feTurbulence` tĩnh làm mặt nạ để sáp chỉ bám đỉnh hạt. Nét viền là `path` rung nhẹ, màu chàm hoặc nâu đậm, không bao giờ đen. Tô màu bằng nét zigzag chéo, chừa khe, tràn nhẹ ra ngoài viền. Màu nước xanh chàm là một lớp `multiply` đè lên trời, bị sáp trắng cản (sao và chấm trắng là sáp trắng, giữ nguyên). Không ánh sáng điện ảnh, chỉ độ đậm theo lực tay.
- **Máy quay và khung dọc 9:16:** cận trung nhìn thẳng, nhân vật đủ lớn ở một khoảng giấy trống để dành chỗ cho chữ. Dọc 9:16 thì trời chiếm phần trên, mái nhà chéo phía dưới. Di máy bằng translate chậm; có thể lùi ra tới mép trang để thấy trang là một vật.
- **Chuyển động:** mọi thứ vẽ bước nấc 12 fps (đổi seed mỗi 2 khung), nét rung nhẹ (boil) dưới 1 px; máy quay và lớp màu nước chạy mượt 24 fps. Nét hiện dọc theo chiều dài 0,4 đến 0,9 giây; tô màu từng hàng. Tư thế đổi bằng thay hình, không nội suy. Tô màu chính là hành động.
- **Chữ trên hình:** viết tay trên trang, từng chữ một. Tiêu đề dùng Mali đậm hoặc Itim, phụ đề là chữ in của sách, Itim, màu viền, đặt trên mảng giấy trắng rách mép, đủ dấu tiếng Việt, không dùng hộp tối.
- **Nước đi đặc trưng:**
  - Sáp trắng cản màu nước: giấu lời nhắn từ đầu, màu nước quét qua mới lộ; hợp lời tạm biệt, tính năng ẩn.
  - Thế giới tự vẽ ngay trước nhân vật; hợp hành trình, dòng thời gian.
  - Tô màu là hành động: cửa sổ sáng lên từng ô; hợp thành phố lên đèn, đội mặc đồng phục.
  - Lùi ra khỏi mép trang, lật trang; hợp tổng kết năm, thiệp cảm ơn.
- **Bẫy:** nét sạch và đều như vector thì mất chất sáp; màu nước phủ không kín để lại sọc trắng; nhân vật bị màu nước nhuộm xuống thì phải vẽ sau lớp nước; tô màu mờ nhạt rồi đè nước thì bùn, phải tô đậm hoặc đan chéo.

Phỏng theo `styles/crayon-book/STYLE.md` của lemomo-ai/lemo-opuscar (MIT).

*Ý tưởng gốc: MotionFly / lemo-opuscar (MIT), qua SlideFly.*

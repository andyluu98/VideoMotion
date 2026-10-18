# Vox Collage (báo chí cắt dán giấy, vàng dạ quang)

> Nền giấy báo ngà có thớ và nếp gấp, mọi vật là mảnh cắt rách mép viền trắng đổ bóng cứng, ảnh là bóng người phủ chấm tram, một màu vàng dạ quang duy nhất tô chữ, khoanh tròn, vẽ mũi tên.

**Hợp:** video giải thích tin tức và kinh tế, lý do một hiện tượng xảy ra, lịch sử ngắn, so sánh phe phái, điểm lại một sự kiện có mốc thời gian.
**Không hợp:** sản phẩm công nghệ bóng bẩy, nội dung trẻ em, lễ hội, chủ đề chữa lành, thứ cần cảm giác mượt và sang.
**Cảm xúc:** thời sự, tỉnh táo, tò mò, có chút thủ công.

## Hình dung
Một bàn làm việc của biên tập viên: tờ giấy báo trải phẳng, kéo, keo, băng keo giấy, bút dạ vàng. Người làm cắt tít khỏi tờ báo, xé ảnh in chấm, dán chồng lên nhau hơi lệch rồi gạch, khoanh, vẽ mũi tên. Người xem cảm thấy câu chuyện đang được ghép lại ngay trước mắt, từng mảnh một.

## Bảng màu
```css
--bg: #E6DEC9;       /* giấy báo ngả kem, nền (có thể đổi sang giấy kraft #CDB88F) */
--paper: #F7F2E4;    /* giấy trắng ngà của mảnh cắt */
--ink: #17130F;      /* mực in đen */
--gray: #BDB6A3;     /* xám tram nhạt, vùng phụ */
--accent: #FFD23F;   /* vàng dạ quang, màu nhấn duy nhất (có thể đổi đỏ #E63B2E hoặc xanh cobalt #2F5BD8) */
```
- Chọn một màu nhấn cho cả video rồi giữ nguyên. Mọi thứ còn lại chỉ là đen, trắng ngà, xám.
- Màu nhấn dùng cho vệt dạ quang, mũi tên, khoanh tròn, một mảng nền sau tiêu đề; không đổ cho cả khung hình.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Source+Serif+4:wght@400;700&family=Xanh+Mono&display=swap" rel="stylesheet">
```
- Tiêu đề: Anton 400 (có tiếng Việt), IN HOA, mỗi từ một mảnh giấy. Dấu tiếng Việt cao, chừa khoảng trống phía trên chữ trong mảnh giấy để dấu không bị cắt.
- Thân và tít mẩu báo: Source Serif 4 700 và 400 (có tiếng Việt).
- Chú thích, nhãn máy chữ: Xanh Mono 400 (có tiếng Việt), IN HOA, cỡ nhỏ.

## Bề mặt
Nền giấy báo có thớ (nhiễu tĩnh rất nhẹ), một nếp gấp dọc và một nếp gấp ngang kẻ bằng cặp nét tối và nét sáng. Mảnh cắt có mép rách lởm chởm, viền giấy trắng dày khoảng 10px quanh phần thân, bóng đổ ngắn và cứng lệch xuống dưới phải (không mờ). Mảnh xếp chồng, xoay lệch từ 1 đến 4 độ.
```css
.manh { filter: drop-shadow(8px 10px 0 rgba(23,19,15,.34)); /* bóng cứng, đặt tĩnh */ }
.tram { background: radial-gradient(circle, #17130F 32%, transparent 34%) 0 0/15px 15px; }
```

## Ngôn ngữ minh họa
- **Mảnh cắt rách mép:** đa giác có mép lệch ngẫu nhiên (tính bằng bộ số có hạt giống), viền trắng quanh, bóng cứng.
- **Ảnh chấm tram:** hình bóng người hoặc đồ vật vẽ bằng SVG, tô bằng pattern chấm xoay 45 độ, chấm to dần về phía tối. Không dùng ảnh thật.
- **Băng keo giấy:** dải vàng nhạt mờ, hai đầu răng cưa, dán chéo ở góc mảnh.
- **Mẩu báo cắt:** tít serif đậm, dòng chữ giả bằng các thanh xám, ô ảnh tram nhỏ.
- **Đồ họa thông tin:** bản đồ cắt dán (các mảng đất rách mép, ghim và đường đứt nét), biểu đồ đường trên giấy, trục thời gian, ô số liệu như mẩu giấy.
- **Nét tay màu nhấn:** vệt dạ quang tô chữ, vòng khoanh vẽ hơi lệch, mũi tên cong kèm nét mực mảnh, đường gạch bỏ.

## Chữ ký chuyển động
- **Mảnh trượt vào rồi dính:** mảnh giấy từ ngoài khung trượt vào, hơi xoay, lún nhẹ rồi dính lại, rung giấy một nhịp ngắn.
- **Khung thấp:** mọi chuyển động của mảnh và nét vẽ đi bước nấc khoảng 12 hình mỗi giây (ease `steps()`), như hoạt hình cắt giấy.
- **Dán đè:** mảnh mới luôn dán đè lên mảnh cũ, không đẩy mảnh cũ đi.
- **Vệt dạ quang quét:** vệt vàng quét ngang qua chữ từ trái sang phải khi từ khóa được nói.
- **Vẽ nét:** vòng khoanh và mũi tên được vẽ ra theo nét (`strokeDashoffset`), theo từng nấc.
- **Đẩy máy chậm:** cả cụm cắt dán được đẩy vào rất chậm, các lớp trước, giữa, sau trượt khác tốc độ để có thị sai.
- Nhịp: gọn, dứt khoát, như tiếng bấm kéo.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Mở đầu:** tiêu đề câu hỏi dán từng mảnh, từ khóa được vệt dạ quang tô.
- **Dòng thời gian:** các mẩu báo dán nối nhau trên một trục, mỗi mốc là một mảnh mới đè lên.
- **Bản đồ:** các mảng đất cắt dán rơi vào chỗ, ghim màu nhấn cắm xuống, đường đứt nét nối các ghim.
- **Kết luận:** một mảnh lớn dán đè giữa khung, gạch dưới đúng một ý.

## Nên tránh
Ảnh thật hoặc ảnh có độ chuyển sắc mượt, mép cắt thẳng tắp quá sạch, bóng đổ mờ kiểu giao diện, hơn một màu nhấn, nhiều phông hơn ba, chuyển động trơn mượt kiểu quảng cáo công nghệ, số liệu bịa đặt trình bày như thật.

## Họ hàng
`halftone-dossier` (cũng chấm tram nhưng chất hồ sơ in, ít thủ công), `paper-popup` (giấy cắt nhưng dựng khối nổi và ấm hơn), `retro-zine` (cắt dán kiểu tạp chí tự in, bừa và nhiều màu hơn), `comic-book` (chấm tram và nét đậm nhưng là truyện tranh, nhiều màu in).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/vox-collage.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** Một mặt bàn giấy báo ngà có nếp gấp, trên đó là cụm mảnh cắt dán lệch góc: ba mảnh tiêu đề chữ lớn xếp bậc thang bên trái, một ảnh chân dung phủ chấm tram bên phải (hình bóng người mặc vest có cà vạt, tóc là mảng mực), một mẩu báo có tít, một biểu đồ đường, một bản đồ nhỏ. Nhân vật là hình bóng, không có nét mặt; ở cú cận cảnh hình bóng chiếm khoảng một nửa chiều cao khung.
- **Chất liệu và ánh sáng:** Không có ánh sáng ba chiều. Chiều sâu đến từ viền giấy trắng và bóng đổ cứng lệch xuống dưới phải, đồng nhất cho mọi mảnh. Ảnh tram dùng pattern chấm xoay 45 độ, độ lớn chấm đổi theo mặt nạ chuyển sắc để tạo khối. Nền có nhiễu giấy tĩnh, nếp gấp, tối nhẹ ở rìa. Mọi hiệu ứng `filter` đặt tĩnh; chỉ tween transform, opacity, màu, clipPath, nét SVG.
- **Máy quay và khung:** Nhìn thẳng từ trên xuống, không phối cảnh. Cú đẩy vào chậm 2 đến 5 phần trăm trong vài giây, chia ba lớp (sau, giữa, trước) với tốc độ khác nhau. Khung dọc 9:16 xếp mảnh theo cột: tiêu đề trên, ảnh tram giữa, đồ họa dưới; khung ngang xếp tiêu đề bên trái, ảnh bên phải, đồ họa bên dưới.
- **Chuyển động:** Mảnh và nét vẽ đi bước nấc khoảng 12 hình mỗi giây; mảnh trượt vào hơi xoay, lún nhẹ, rung giấy một nhịp. Máy quay cũng đi nấc. Không nảy mềm, không ease trơn.
- **Chữ trên hình:** Tiêu đề Anton IN HOA, đen trên giấy ngà hoặc ngà trên mảnh đen, mỗi từ một mảnh. Từ khóa có vệt dạ quang sau chữ. Nhãn và chú thích bằng Xanh Mono. Phụ đề là một dải giấy đen rách mép, chữ ngà. Đủ dấu tiếng Việt.
- **Nước đi đặc trưng:**
  - Dán từng mảnh tiêu đề theo nhịp từ khóa, vệt dạ quang quét qua chữ khi từ được nói (hợp mở đầu, nêu câu hỏi).
  - Khoanh tròn vẽ tay kèm mũi tên cong chỉ vào điểm đáng chú ý trên biểu đồ (hợp chỉ ra điểm bất thường).
  - Mẩu báo cắt trượt vào, tít hiện bằng thanh giấy chạy ngang (hợp dẫn nguồn, kể mốc lịch sử).
  - Bản đồ cắt dán: các mảng đất dán lần lượt, ghim cắm xuống, đường đứt nét nối (hợp nói địa điểm, hành trình).
  - Gạch đỏ bỏ ý cũ bằng nét màu nhấn rồi dán ý mới đè lên (hợp phản bác, sửa nhầm lẫn).
- **Bẫy:** Dùng ảnh thật thay cho hình tram làm mất chất in báo. Bóng đổ mờ hoặc khác hướng giữa các mảnh làm hình rời rạc. Chữ có dấu bị cắt mất dấu vì sát mép trên của mảnh giấy, phải chừa chỗ phía trên chữ. Số liệu cụ thể trên biểu đồ mà nguồn không có, chỉ dùng nhãn "ví dụ minh họa" hoặc không ghi số.

*Thẻ viết mới cho VideoMotion, lấy cảm hứng từ phong cách video giải thích cắt dán của báo chí.*

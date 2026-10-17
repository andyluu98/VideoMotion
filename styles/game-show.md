# Game show (trường quay truyền hình màu kẹo)

> Mỗi slide là một vòng chơi: sân khấu đổi màu, bảng đèn chạy, sao phán quyết đập xuống, nét mực dày và bóng đổ cứng.

**Hợp:** tổng kết năm, đào tạo vui, sự kiện giải trí, lễ trao giải, giới thiệu theo từng vòng, quiz nội bộ.
**Không hợp:** báo cáo tài chính trang trọng, chủ đề buồn hay nhạy cảm, thương hiệu cao cấp tối giản.
**Cảm xúc:** vui nhộn, màu kẹo, sôi động, truyền hình.

## Hình dung
Một trường quay vẽ phẳng: nền sọc tỏa, rèm viền vỏ sò, dải bóng đèn marquee, bục 1, 2, 3, bảng điểm, thẻ kem bo tròn. Người xem có cảm giác đang ngồi hàng ghế khán giả, mỗi lần bấm là "vòng tiếp theo". Chiều sâu chỉ đến từ bóng đổ cứng lệch xuống góc phải dưới, không có mờ.

## Bảng màu
```css
--ink: #1B1035;     /* mực: viền, bóng cứng, chữ trên nền kẹo */
--cream: #FFF3D6;   /* thẻ, giấy */
--accent: #FFD23F;  /* vàng: điểm, bóng đèn, chữ nhấn trên nền đậm */
--red: #D4253F;     /* dải tiêu đề bảng điểm, vòng câu chốt */
/* mỗi vòng một màu sân khấu (--bg):
   tím #5B3FC4 (mở màn), xanh dương #2354C8, vàng #FFD23F, xanh lục #0B7A5A,
   hồng #FF7EB6, cam #FF9A3C, navy #1B2A6B, xanh trời #4CC9F0, đỏ #D4253F, tím đậm #3B2A8F (kết) */
/* màu nhân vật, confetti: #FF9A3C #FF4F5E #FF7EB6 #2EC27E #B5E04A #4CC9F0 #3A6BFF #5B3FC4 */
```
Nền đậm thì chữ trắng có viền mực kiểu telop, nền kẹo sáng thì chữ mực. Nhân vật không trùng màu với nền nó đứng. Mỗi nhân vật giữ một màu thân suốt deck.

## Chữ
```html
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;700;800&family=Nunito:wght@600;700;800&display=swap" rel="stylesheet">
```
- Tiêu đề, nhãn hô: Baloo 2 800, IN HOA cho lời hô ("TUYỆT!", "ĐÚNG!"), giãn 0,01em. Có tiếng Việt (đã kiểm).
- Thân: Nunito 600 đến 700. Có tiếng Việt.
- Chữ trắng trên nền đậm thêm viền mực (`paint-order: stroke`) như phụ đề truyền hình.

## Bề mặt
Nền một màu của vòng, phủ sọc tỏa từ một điểm (sọc trắng mờ 10% trên nền đậm, 28% trên nền sáng). Đáy là dải sàn sân khấu tối có một đường mực.
```css
background: repeating-conic-gradient(from 0deg at 50% 110%, rgba(255,255,255,.1) 0 6deg, transparent 6deg 12deg), var(--bg);
```

## Ngôn ngữ minh họa
- Viền mực 8px cho nhân vật và vật lớn, 5 đến 7px cho chi tiết nhỏ, đầu nét tròn.
- **Bóng đổ cứng:** vẽ lại đúng hình bằng màu mực, dịch (8, 8), rồi vẽ hình màu lên trên. Không `filter`, không mờ.
- **Nhân vật đậu:** một kiểu thân cho cả dàn (thân đậu tròn, tay cụt có găng, mắt bầu dục có đốm sáng, bụng kem), phân biệt bằng màu thân và một phụ kiện đầu (ăng ten, tim, chồm tóc).
- Hình mẫu: sao phán quyết nhiều cánh có bóng cứng, bảng điểm thẻ kem dải đỏ, bóng đèn vàng làm điểm đếm, confetti tròn, tam giác, sóng.
- Vật ẩn dụ (tấm slide, thẻ, bảng) thành đồ chơi bằng cách gắn mắt, miệng, tay chân.

## Chữ ký chuyển động
- **Đổi vòng, đổi màu:** mỗi slide mới cắt dứt khoát sang màu sân khấu khác (`data-transition="cut"`), sọc tỏa xoay một góc nhỏ như đèn sân khấu vừa bật.
- **Dải đèn marquee chạy:** hàng bóng đèn quanh tiêu đề hoặc bảng điểm `data-loop="blink"` lệch pha theo hàng, tạo cảm giác đèn đuổi nhau.
- **Sao phán quyết đập xuống:** sao "TUYỆT!" vào bằng `stamp` nghiêng 10 độ, ngay sau đó confetti rơi (`drop` trễ dần, rải thưa).
- **Bảng điểm lên số:** từng hàng thanh màu chạy ra (`wipe` + `data-stagger`), con số có nguồn đếm lên (`data-count`).
- **Nhân vật nhún:** nhân vật đậu vào bằng `pop` có nảy, rồi đung đưa nhẹ (`data-loop="sway"` trên lớp con).
- **Lật đáp án:** thẻ câu hỏi chờ cú bấm (`data-step`), đáp án bật ra bằng `pop`.
- Nhịp: nhanh, nảy, như MC hô to; nghỉ một nhịp trước khi đập sao.

## Khoảnh khắc đáng nhớ (gợi ý)
- **Bìa:** rèm vỏ sò kéo lên, dải đèn chạy quanh tên chương trình, hai nhân vật đậu nhún hai bên.
- **Câu đố:** câu hỏi trên thẻ kem, ba bục A, B, C; bấm thì một bục sáng đèn, sao "ĐÚNG!" đập xuống.
- **Bảng xếp hạng:** bục 1, 2, 3 mọc lên từ sàn, tên đội hiện trên từng bục.
- **Kết:** confetti rơi kín, sao lớn ở giữa, lời cảm ơn chữ trắng viền mực.

## Nên tránh
Gradient, bóng mờ, chất liệu giấy, 3D, phát sáng; hai nhân vật cùng màu nền chỗ đứng; đổi màu thân nhân vật giữa các slide; tên, giao diện, nhạc hiệu của chương trình có thật; số điểm bịa; câu dài trong hình.

## Họ hàng
`block-frame` (pop tươi, khối màu táo bạo nhưng là bố cục đồ họa, không có trường quay hay nhân vật), `scifi-toon` (cũng viền dày màu phẳng, mỗi slide một màu, nhưng là hài viễn tưởng chứ không phải sân khấu thi đấu), `8-bit-orbit` (hoài cổ arcade neon, hợp game nhưng nền tối).

## Bản video (khi làm video; thắng các mục trên khi mâu thuẫn)
Mục tiêu hình: giống ảnh minh họa `docs/assets/styles/game-show.jpg`, một khung phim chứ không phải slide.
- **Thế giới và nhân vật:** Sân khấu phẳng một màu tím, rèm đỏ viền vỏ sò rũ ở mép trên, sàn tối ở đáy. Một dàn nhân vật đậu tròn cùng một kiểu thân (thân bầu, tay cụt giơ cao có găng, mắt bầu dục có đốm sáng, miệng há hô, bụng kem, má hồng), phân biệt bằng màu thân và một phụ kiện đầu (ăng ten, tim, dấu hỏi, mũ nồi, tia chớp, tai thỏ). Mỗi con có thẻ tên nhỏ dưới chân. Bốn con nhỏ đứng hàng sau trên bục, ba bốn con lớn hơn ở hàng trước, cả dàn giơ tay hô. Phía trước là hàng bóng đen đầu khán giả chạy ngang đáy khung. Góc trên trái có bảng tiêu đề đỏ nghiêng bo tròn, có tựa lớn và dòng phụ.
- **Chất liệu và ánh sáng:** Chỉ SVG phẳng: nền một màu, viền mực 8px đầu tròn, bóng đổ cứng bằng cách vẽ lại hình màu mực dịch (8, 8) rồi vẽ hình màu lên trên. Không filter, không blur, không gradient, không glow. Sọc tỏa nhẹ trên nền (`repeating-conic-gradient` tĩnh, trắng 10%) và dải sàn tối có một đường mực. Nhân vật không trùng màu với nền chỗ đứng.
- **Máy quay và khung dọc 9:16:** Sân khấu chính diện đối xứng như proscenium, cỡ toàn, máy đứng yên; chính khung làm việc di chuyển. Ở dọc, bảng tiêu đề ở trên, dàn nhân vật xếp hai hàng chồng ở giữa và dưới (hàng sau nhỏ, hàng trước lớn), bóng khán giả ở đáy. Máy chỉ có cú đấm theo nhịp: `scale` 1 đến 1,03 rồi về trong 0,16 giây, tổng các cú đấm cùng lúc dưới 0,06.
- **Chuyển động:** Nhanh, nảy, theo lưới nhịp cố định. Nhân vật nhún theo nhịp (parabol 8 đến 30px), hàng kề nhún lệch nửa nhịp để cả dàn gợn sóng. Mỗi cú trúng là squash tắt dần. Vật vào bằng `back.out`, ra bằng ease-in, không fade chậm. Đổi vòng bằng cắt cứng kèm nháy trắng rất ngắn. Tay giơ cao và miệng há trong nửa nhịp khi hô.
- **Chữ trên hình:** Chữ kiểu telop: trắng hoặc vàng với viền mực dày khoảng 14% cỡ chữ (`paint-order: stroke`). Phông Baloo 2 hoặc Be Vietnam Pro 800 đủ dấu Việt cho tựa, nhãn hô ngắn IN HOA ("ĐÚNG!", "TUYỆT!"). Thẻ tên nhân vật là nhãn bo tròn trắng viền mực, chữ mực nhỏ. Phụ đề là bảng telop dưới đáy, không dùng caption mỏng.
- **Nước đi đặc trưng:**
  - Cả dàn nhân vật giơ tay hô trên sân khấu: hợp mở màn, giới thiệu nhiều thành phần.
  - Thẻ vòng bay vào kèm số vòng và tên: hợp từng bước, từng chương.
  - Sao phán quyết đập xuống nghiêng 10 độ rồi confetti: hợp kết quả đúng, hoàn thành.
  - Bảng điểm và bục 1, 2, 3 mọc lên từ sàn: hợp xếp hạng, số liệu có nguồn.
  - Nhân vật rơi vào từng con một theo nhịp: hợp liệt kê thành viên, thành phần.
- **Bẫy:** Hai nhân vật cùng màu với nền chỗ đứng thì chìm mất. Đổi màu thân nhân vật giữa các cảnh làm mất nhận diện. Dùng blur cho bóng hoặc glow làm mất chất phẳng. Hình quá đông và chữ dài trong hình làm khung rối; giữ nhãn ngắn.

Phỏng theo `styles/game-show/STYLE.md` của lemomo-ai/lemo-opuscar (MIT).

*Ý tưởng gốc: MotionFly / lemo-opuscar (MIT), qua SlideFly.*
